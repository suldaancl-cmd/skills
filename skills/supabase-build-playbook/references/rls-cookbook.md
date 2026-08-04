# RLS Cookbook

Copy-paste Row-Level Security patterns. RLS is the single line that turns a
shared Postgres table into a secure multi-tenant backend — and the single
biggest source of "why doesn't this work" bugs. Every pattern below is correct
as written; adapt table/column names.

## Table of contents

1. Enable RLS (do this first, always)
2. Per-operation policies (USING vs WITH CHECK)
3. The `(select auth.uid())` performance rule
4. Index the columns policies filter on
5. Per-user ownership (the simplest secure table)
6. Role-based access (admin / member / viewer)
7. Multi-tenant + the recursion fix (security definer)
8. Debugging RLS

---

## 1. Enable RLS — first, always

A table in the `public` schema with RLS **off** is readable and writable by
anyone holding the publishable key (i.e. any visitor). Enable it the instant the
table exists, before any real data goes in.

```sql
alter table public.clients enable row level security;
```

With RLS on and **no policies**, the table is locked to everyone except the
secret/`service_role` key. You then open access deliberately, one policy per
operation. Default-deny is the safe direction.

---

## 2. Per-operation policies — `USING` vs `WITH CHECK`

This is the #1 RLS confusion. "A policy is a `WHERE` clause" is only true for
reads.

| Operation | `USING` (filters existing rows) | `WITH CHECK` (validates new/changed rows) |
|-----------|:---:|:---:|
| `SELECT`  | ✅ | — |
| `DELETE`  | ✅ | — |
| `INSERT`  | — | ✅ |
| `UPDATE`  | ✅ | ✅ |

- `INSERT` has no pre-existing row, so `USING` does nothing — you **must** use
  `WITH CHECK`. Forgetting it is what produces
  `new row violates row-level security policy`.
- `UPDATE` checks `USING` against the old row (can you touch it?) **and**
  `WITH CHECK` against the new row (is the result still allowed?). Omit
  `WITH CHECK` and a user could update a row's `user_id` to someone else's.

```sql
-- read your own rows
create policy "select_own" on public.notes
  for select to authenticated
  using ( (select auth.uid()) = user_id );

-- insert only rows owned by you
create policy "insert_own" on public.notes
  for insert to authenticated
  with check ( (select auth.uid()) = user_id );

-- update only your rows, and you can't reassign ownership away
create policy "update_own" on public.notes
  for update to authenticated
  using ( (select auth.uid()) = user_id )
  with check ( (select auth.uid()) = user_id );

-- delete your own rows
create policy "delete_own" on public.notes
  for delete to authenticated
  using ( (select auth.uid()) = user_id );
```

Always scope policies to a role (`to authenticated`) so they don't apply to
anonymous visitors unless you mean them to.

---

## 3. The `(select auth.uid())` performance rule

Write `(select auth.uid())`, not bare `auth.uid()`. Wrapping it in a subselect
lets Postgres evaluate it **once per query** (an initPlan) instead of once per
row. On a table with thousands of rows this is the difference between instant and
seconds. This is an official Supabase recommendation, not folklore. The same
applies to `auth.jwt()` and any `current_setting(...)` call inside a policy.

```sql
-- slow on large tables: function re-checked per row
using ( auth.uid() = user_id )

-- fast: evaluated once, cached for the query
using ( (select auth.uid()) = user_id )
```

---

## 4. Index the columns policies filter on

Every RLS policy adds an implicit filter to every query. If the filtered column
isn't indexed, that filter is a sequential scan. Postgres does **not** create
indexes on foreign keys automatically — you must.

```sql
create index on public.clients (user_id);
create index on public.clients (company_id);
```

Supabase's Database Advisors will flag both "RLS enabled, no policy", "policy
re-evaluates auth function per row", and "unindexed foreign key" — run them.

---

## 5. Per-user ownership — the simplest secure table

The minimum viable secure table: a `user_id` column tied to the logged-in user,
plus the four policies from section 2.

```sql
create table public.notes (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null default auth.uid()
               references auth.users(id) on delete cascade,
  body       text not null,
  created_at timestamptz not null default now()
);
alter table public.notes enable row level security;
create index on public.notes (user_id);
-- then the 4 policies from section 2
```

`default auth.uid()` means the client never has to send `user_id` — and the
`WITH CHECK` policy guarantees it can't forge one. `on delete cascade` cleans up
when the user is deleted.

---

## 6. Role-based access (admin / member / viewer)

Roles live in a column on `profiles` (see the multi-tenant starter). Read the
role through a `security definer` helper (section 7 explains why a helper, not an
inline subquery). Then gate operations by role.

```sql
-- everyone in the company can read; only admins can delete
create policy "clients_delete_admin_only" on public.clients
  for delete to authenticated
  using (
    company_id = public.current_company_id()
    and public.current_role() in ('owner','admin')
  );
```

Pattern: viewers get `SELECT` only, members get `SELECT/INSERT/UPDATE`, admins
additionally get `DELETE` and access to other members' rows within the company.

---

## 7. Multi-tenant + the recursion fix

Goal: every user sees only their company's rows. Naive version puts a subquery
inline:

```sql
-- ❌ causes: infinite recursion detected in policy for relation "profiles"
using (
  company_id = (select company_id from public.profiles where id = auth.uid())
)
```

If `profiles` itself has RLS that references the same lookup, Postgres recurses
and errors. The fix is a `security definer` function: it runs with the
definer's rights, so reading `profiles` inside it does **not** re-trigger the
caller's RLS. Lock its `search_path` to `''` so it can't be hijacked.

```sql
create or replace function public.current_company_id()
returns uuid
language sql
security definer
set search_path = ''
stable
as $$
  select company_id from public.profiles where id = (select auth.uid())
$$;

create or replace function public.current_role()
returns text
language sql
security definer
set search_path = ''
stable
as $$
  select role from public.profiles where id = (select auth.uid())
$$;
```

Then tenancy policies are clean and non-recursive:

```sql
create policy "clients_select_same_company" on public.clients
  for select to authenticated
  using ( company_id = public.current_company_id() );

create policy "clients_insert_same_company" on public.clients
  for insert to authenticated
  with check ( company_id = public.current_company_id() );
```

`stable` lets the planner cache the result within a statement. The full schema
that uses these helpers is in `multitenant-starter.sql`.

---

## 8. Debugging RLS

- **"new row violates row-level security policy"** → missing or wrong
  `WITH CHECK` on `INSERT`/`UPDATE`.
- **"infinite recursion detected in policy"** → an inline subquery against a
  table whose policy loops back; move the lookup into a `security definer`
  function (section 7).
- **Empty result set, no error** → RLS is on but no `SELECT` policy matches.
  Default-deny is working; you haven't granted read.
- **It works with the secret key but not in the browser** → that's RLS doing its
  job. The secret key bypasses RLS; the publishable key doesn't. Fix the policy,
  don't reach for the secret key.
- **To inspect as a user**, in the SQL editor:
  ```sql
  set role authenticated;
  set request.jwt.claims = '{"sub":"<a-real-user-uuid>"}';
  select * from public.clients;   -- now filtered as that user
  reset role;
  ```
