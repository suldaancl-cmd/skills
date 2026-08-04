-- ============================================================================
-- Multi-tenant starter schema for a CRM / DashboardOS on Supabase
-- ----------------------------------------------------------------------------
-- Run in the Supabase SQL Editor, or save as a migration:
--   supabase migration new init_multitenant   then paste, then  supabase db push
--
-- Model: an organization (company) has many members (profiles, each tied to a
-- Supabase auth user) with a role. Tenant data (here: clients) is isolated by
-- company_id. Every user sees only their own company's rows; admins get more.
--
-- Tenancy is read through SECURITY DEFINER helpers so policies never recurse.
-- Adapt "clients" into your real entities (projects, invoices, leads, ...).
-- ============================================================================

-- 1. Companies (the tenant) -------------------------------------------------
create table public.companies (
  id         uuid primary key default gen_random_uuid(),
  name       text not null,
  created_at timestamptz not null default now()
);
alter table public.companies enable row level security;

-- 2. Profiles (one per auth user) -------------------------------------------
-- company_id is nullable: a user exists before they create/join a company.
create table public.profiles (
  id         uuid primary key references auth.users(id) on delete cascade,
  company_id uuid references public.companies(id) on delete set null,
  full_name  text,
  role       text not null default 'member'
               check (role in ('owner','admin','member','viewer')),
  created_at timestamptz not null default now()
);
alter table public.profiles enable row level security;
create index on public.profiles (company_id);

-- Auto-create a profile row whenever a new auth user signs up.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.profiles (id, full_name)
  values (new.id, new.raw_user_meta_data ->> 'full_name');
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- 3. Tenancy helpers (SECURITY DEFINER → no policy recursion) ----------------
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

-- 4. Policies on profiles ----------------------------------------------------
-- A user can always read and edit their own profile.
create policy "profiles_select_self" on public.profiles
  for select to authenticated
  using ( (select auth.uid()) = id );

create policy "profiles_update_self" on public.profiles
  for update to authenticated
  using ( (select auth.uid()) = id )
  with check ( (select auth.uid()) = id );

-- Members can see other members of the same company (for a team list).
create policy "profiles_select_same_company" on public.profiles
  for select to authenticated
  using ( company_id = public.current_company_id() );

-- 5. Policies on companies ---------------------------------------------------
-- You can see the company you belong to.
create policy "companies_select_own" on public.companies
  for select to authenticated
  using ( id = public.current_company_id() );

-- Any authenticated user can create a company (becomes its owner — handle the
-- profile.company_id + role='owner' update in your app right after insert,
-- or in an Edge Function for atomicity).
create policy "companies_insert_any" on public.companies
  for insert to authenticated
  with check ( true );

-- Only owners/admins can rename the company.
create policy "companies_update_admin" on public.companies
  for update to authenticated
  using ( id = public.current_company_id()
          and public.current_role() in ('owner','admin') )
  with check ( id = public.current_company_id() );

-- 6. A tenant table: clients (copy this block per real entity) ---------------
create table public.clients (
  id         uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  created_by uuid not null default auth.uid()
               references public.profiles(id) on delete set null,
  name       text not null,
  email      text,
  phone      text,
  status     text not null default 'lead'
               check (status in ('lead','active','churned')),
  created_at timestamptz not null default now()
);
alter table public.clients enable row level security;
create index on public.clients (company_id);
create index on public.clients (created_by);

-- read: anyone in the company
create policy "clients_select_company" on public.clients
  for select to authenticated
  using ( company_id = public.current_company_id() );

-- insert: row must belong to your company (members and up)
create policy "clients_insert_company" on public.clients
  for insert to authenticated
  with check (
    company_id = public.current_company_id()
    and public.current_role() in ('owner','admin','member')
  );

-- update: your company's rows; can't move a row to another company
create policy "clients_update_company" on public.clients
  for update to authenticated
  using ( company_id = public.current_company_id()
          and public.current_role() in ('owner','admin','member') )
  with check ( company_id = public.current_company_id() );

-- delete: admins/owners only
create policy "clients_delete_admin" on public.clients
  for delete to authenticated
  using ( company_id = public.current_company_id()
          and public.current_role() in ('owner','admin') );

-- ============================================================================
-- Notes
-- - Creating a company + promoting the creator to owner touches two tables;
--   for true atomicity do it in one Edge Function (service role) or a SQL
--   function, rather than two client calls that can half-fail.
-- - Add `updated_at timestamptz` + a trigger if you need change tracking.
-- - Run Supabase's Database Advisors after applying: they flag tables with RLS
--   off, per-row auth re-evaluation, and unindexed foreign keys.
-- ============================================================================
