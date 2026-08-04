---
name: supabase-build-playbook
description: >
  Build a production Supabase backend the right way — schema design, Row-Level
  Security (RLS) policies, multi-tenant SaaS isolation (company_id / user_id /
  role), and Next.js App Router auth with @supabase/ssr. Use this whenever the
  user is starting or architecting a Supabase project, writing or debugging RLS
  policies, building a CRM / dashboard / CMS / SaaS on Supabase, wiring Supabase
  Auth into Next.js, or deciding "Supabase vs a custom backend". Especially reach
  for it on RLS errors like "new row violates row-level security policy" or
  "infinite recursion detected in policy for relation". Complements
  supabase-stack (Vite/React paste-prompts) and supabase-postgres-best-practices
  (query tuning) — this one owns greenfield architecture + the gotchas that bite.
---

# Supabase Build Playbook

Supabase is **just Postgres** with batteries (Auth, Storage, Realtime, Edge
Functions, auto-REST/GraphQL) bolted on. Everything good or bad that happens
flows from that one fact. This skill is the architecture + security layer:
*how to stand up a backend that won't leak and won't need rewriting.*

It assumes you already know the 15 concepts (tables, auth, RLS, policies, keys,
storage, realtime, edge functions, webhooks, migrations, relationships, roles,
multi-tenant). If not, read `references/concepts-ar.md` first (Arabic, with the
corrections baked in).

## When to use vs. when NOT to

Supabase shines for **greenfield** projects where you want to delete weeks of
boilerplate (auth + DB + storage + realtime in one place). It is a poor trade
when you already have a working hand-rolled backend.

```
Starting a new app / SaaS / CRM / dashboard?            → use Supabase. This skill.
Already have Express+Prisma+JWT+Socket.io that works?   → DON'T rip it out to "learn".
   Want managed auth/storage only?                       → Supabase is just Postgres:
                                                            point your ORM at it, adopt
                                                            Auth/Storage piecemeal. New
                                                            projects only — not a migration
                                                            of a working app.
Hitting an RLS error?                                     → references/rls-cookbook.md
Wiring auth into Next.js App Router?                      → references/nextjs-ssr-auth.md
Need a multi-tenant schema to copy?                       → references/multitenant-starter.sql
```

The Karpathy rule applies: **don't rewrite what isn't broken.** A matchmaking
app or any product with a functioning custom backend gains nothing user-facing
from a Supabase migration; it costs weeks. Use Supabase for the *next* thing.

## The one rule that prevents disasters

The #1 cause of Supabase data breaches is not exotic — it is a table with RLS
**off** in an exposed schema, or the **secret/`service_role` key shipped to the
browser**. Either one = anyone can dump your entire database from the client.

Two reflexes, every single time:

1. **`alter table <t> enable row level security;` immediately after every
   `create table`** in the `public` schema. A table with RLS off + the
   publishable key in the frontend is world-readable. No exceptions.
2. **The secret key (`sb_secret_...` / legacy `service_role`) lives server-side
   only** — Edge Functions, your server, CI. It *bypasses RLS entirely*. If it
   ever touches client code or a `NEXT_PUBLIC_*` / `VITE_*` var, treat it as
   compromised and rotate it.

Keys (2025 naming): `sb_publishable_...` (browser, safe, RLS-enforced) replaces
`anon`; `sb_secret_...` (server, all-powerful, RLS-bypassing) replaces
`service_role`. Old JWT names still work during migration.

## The golden build order

Do it in this sequence — each step depends on the one before:

1. **Schema** — model entities as tables, one entity per table. Add
   relationships with foreign keys (`1:1`, `1:many`, `many:many` via a join
   table). For any multi-tenant table, include `company_id` + `created_by` from
   day one (retrofitting tenancy later is painful).
2. **Enable RLS** on every `public` table — *before* inserting real data.
3. **Policies** — one per operation you allow. Remember `SELECT/DELETE` use
   `USING`, `INSERT` uses `WITH CHECK`, `UPDATE` needs **both**. Wrap
   `auth.uid()` as `(select auth.uid())` for performance. See the cookbook.
4. **Indexes** — index every column an RLS policy filters on and every foreign
   key. Postgres does **not** auto-index FKs; without it, every protected query
   is a sequential scan.
5. **Auth** — wire Supabase Auth. For Next.js App Router use `@supabase/ssr`
   with separate browser/server clients + middleware (cookie sessions). See the
   auth reference.
6. **Storage** — private buckets, `{auth.uid()}/{file}` paths, signed URLs.
   Never public buckets for user data.
7. **Server logic** — anything secret (Stripe webhooks, sending email, admin
   actions, AI calls with private keys) goes in Edge Functions, never the
   client.
8. **Migrations** — once past prototyping, stop editing schema by hand in the
   dashboard. Capture changes as migration files so they're reviewable and
   replayable (works with Claude Code / git / a team).

## The gotchas that bite (the 20% the tutorials skip)

These are the things that turn "it worked in the demo" into a 2-hour debugging
session. Full SQL for each is in `references/rls-cookbook.md`.

- **`USING` vs `WITH CHECK`.** "Policy = a `WHERE` clause" is only true for
  reads. `INSERT` has no existing row to filter, so it ignores `USING` and needs
  `WITH CHECK`. Forgetting it → `new row violates row-level security policy`.
- **`auth.uid()` per-row vs per-query.** Bare `auth.uid()` can be re-evaluated
  for every row. `(select auth.uid())` lets the planner compute it once
  (initPlan). On big tables this is the difference between fast and unusable.
- **Unindexed RLS/FK columns.** `user_id` / `company_id` must be indexed.
- **Multi-tenant recursion.** A policy on `projects` that sub-queries a table
  whose own policy queries back → `infinite recursion detected in policy`. Fix:
  read tenancy through a `security definer` helper function with a locked
  `search_path`, not an inline subquery. This is the single hardest part of
  multi-tenant — the starter `.sql` solves it for you.
- **`service_role` bypasses RLS.** It's not "be careful with it" — it sees and
  writes everything. Server-only, always.
- **Auth hardening is opt-in.** Email confirmation, leaked-password protection
  (HaveIBeenPwned), and MFA are all *off* by default. Turn them on.
- **`on delete cascade`** on FKs referencing `auth.users(id)` so deleting a user
  cleans up their rows instead of erroring.

## References

- `references/concepts-ar.md` — the 15 concepts in Arabic, corrected (the mental
  model layer; read first if shaky on fundamentals).
- `references/rls-cookbook.md` — copy-paste RLS patterns: enable, per-operation
  policies, the `(select auth.uid())` optimization, indexing, role-based access,
  and the multi-tenant `security definer` recursion fix.
- `references/nextjs-ssr-auth.md` — the modern `@supabase/ssr` two-client +
  middleware pattern for Next.js App Router (email/password + Google), with the
  email-verification UX. This is what the Vite-focused `supabase-stack` skill
  does not cover.
- `references/multitenant-starter.sql` — a ready-to-run schema for a
  CRM / DashboardOS: `companies`, `profiles` (linked to `auth.users`), role,
  a sample tenant table, all RLS + indexes + the tenancy helper. Adapt the
  table names and run it in the SQL editor or as a migration.
