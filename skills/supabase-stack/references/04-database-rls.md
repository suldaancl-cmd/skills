# 04 — Per-user tables with RLS

One column (`user_id`) + four policies = a multi-tenant SaaS backend on Postgres.

## The shape

```sql
-- The table. Every row carries the owner.
create table public.notes (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null references auth.users(id) on delete cascade,
  title       text not null,
  content     text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

-- Turn on Row Level Security. Without this line the policies are inert.
alter table public.notes enable row level security;

-- Four policies, one per operation. All filter by the signed-in user.
create policy "notes_select_own" on public.notes
  for select using (auth.uid() = user_id);

create policy "notes_insert_own" on public.notes
  for insert with check (auth.uid() = user_id);

create policy "notes_update_own" on public.notes
  for update using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "notes_delete_own" on public.notes
  for delete using (auth.uid() = user_id);

-- Optional: keep updated_at fresh.
create or replace function public.set_updated_at() returns trigger as $$
begin new.updated_at = now(); return new; end;
$$ language plpgsql;

create trigger notes_set_updated_at
  before update on public.notes
  for each row execute function public.set_updated_at();

-- Optional: index for the common per-user listing query.
create index notes_user_id_idx on public.notes (user_id);
```

## Paste-ready prompt — let the agent generate the schema from the UI

This mirrors Profit Studio's flow: don't hand-write the SQL, let the AI infer it from the screens.

```text
Generate the Supabase SQL needed to back the data this app uses.

1) Look at the UI in this project and figure out what data needs to be saved per user.

2) For each entity, write a CREATE TABLE statement that:
   - Uses uuid primary keys with `default gen_random_uuid()`.
   - Has a `user_id uuid not null references auth.users(id) on delete cascade` column.
   - Includes `created_at timestamptz not null default now()` and `updated_at timestamptz not null default now()`.

3) For each table, also write:
   - `alter table <name> enable row level security;`
   - Four RLS policies named `<name>_select_own`, `<name>_insert_own`,
     `<name>_update_own`, `<name>_delete_own`, all filtering by `auth.uid() = user_id`.
   - An index on `user_id`.

4) Return one single SQL block I can paste into Supabase → SQL Editor and run.

5) Do not change any frontend code in this step — just print the SQL.
```

## Paste-ready prompt — wire the frontend to the table

After the SQL has been run, ask the agent to wire CRUD:

```text
Wire the existing UI in this project to the `notes` table in Supabase
(using the client at src/supabaseClient.js).

1) Listing — on the notes page, on mount:
   - `supabase.from("notes").select("*").order("created_at", { ascending: false })`
   - Filter is handled by RLS; do not send a `.eq("user_id", ...)`.

2) Create:
   - `supabase.from("notes").insert({ title, content, user_id: user.id })`
   - Get `user` from `supabase.auth.getUser()` once at the top of the handler.

3) Update:
   - `supabase.from("notes").update({ title, content }).eq("id", noteId)`

4) Delete:
   - `supabase.from("notes").delete().eq("id", noteId)`

5) On any error from Supabase, show the message in the existing error UI
   (do not invent new components).

6) Do not change the visual design — only the data wiring.

Show me only the files you changed.
```

## Manual steps (Supabase dashboard)

1. Open **SQL Editor** → New query → paste the SQL block → Run.
2. **Table Editor** → confirm the table exists, columns are right, RLS is enabled.
3. **Authentication → Policies** (or the table's Policies tab) → confirm all four policies are listed and active.

## Verifying RLS actually works (do this once per project)

A common silent failure: RLS isn't enabled, and the app appears to work because the user happens to only see their own rows. Test:

1. Sign in as user A. Insert a row.
2. Sign in as user B. Run `select * from notes` (via the app or the SQL editor with "Run as user B").
3. You should see **zero rows**, not user A's row.

If user B sees user A's row, RLS is off or the policy is wrong.

## When to break out of this pattern

- **Shared resources** (e.g. a "team workspace") — add a `team_id` and a join table; policies join through it.
- **Public reads, private writes** — change `using (...)` on SELECT to `using (true)`, keep the others scoped.
- **Admin role** — use `auth.jwt() ->> 'role' = 'admin'` in the policy `using` clause.

For complex policy work, defer to [`supabase-postgres-best-practices`](../../supabase-postgres-best-practices/SKILL.md) — that skill covers query plans, indexes, and partial indexes.
