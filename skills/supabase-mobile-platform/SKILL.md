---
name: supabase-mobile-platform
description: Design, implement, or audit Supabase as the mobile product system of record for Auth, Postgres, Storage, Realtime, Queues, RLS, and migrations. Use for Expo or agentic apps backed by Supabase; not for replacing a working Supabase project without evidence.
---

# Supabase mobile platform

Keep application truth centralized, authorized, recoverable, and observable.

## Verify before changing

- Inspect the actual project, schemas, migrations, policies, grants, functions, publications, extensions, auth settings, storage policies, queues, and relevant logs.
- Check the current Supabase changelog and official documentation for the products being changed. Pin advice to cloud versus self-hosted deployment and installed CLI/server versions.
- Treat Supabase Cloud and a self-hosted Supabase instance as separate systems. Select one source of truth for a data domain; never create accidental bidirectional writes.
- Preserve existing migrations and unrelated data. Use additive, reviewable migrations and explicit backfills.

## Data and authorization boundaries

- Enable RLS on every table in an exposed schema. Data API grants decide whether a role can reach the table; RLS separately decides which rows it may access.
- Use ownership, membership, or entitlement predicates in policies. `TO authenticated` alone is authentication, not row authorization.
- For update policies, define both `USING` and `WITH CHECK`; remember update also needs a matching select policy.
- Never authorize from user-editable user metadata. Use server-controlled app metadata or database membership tables, accounting for JWT staleness.
- Use `security_invoker` views where supported. Treat `SECURITY DEFINER` functions as privileged APIs: keep them out of exposed schemas where possible, validate caller identity, set a safe search path, and revoke default public execution before granting narrowly.
- Never expose a secret/service-role key to Expo, web clients, logs, analytics, or generated previews.

## Model durable product state

Prefer explicit lifecycle tables over storing everything in chat messages. Typical domains include:

- Profiles and organizations.
- Projects and assets.
- Agent jobs, attempts, events, approvals, and provider calls.
- Entitlements, wallet reservations, immutable ledger entries, refunds, and invoices.
- Notifications and outbox events.
- Audit records for sensitive actions.

Keep money in an append-only ledger or equally auditable deterministic model. An agent may request a charge or refund; it must not directly mutate balances.

## Mobile access pattern

- The Expo client uses the project URL, a publishable key, and the authenticated user's session. RLS remains the enforcement boundary.
- Store session material using the supported secure mobile adapter; do not invent a second token store around the auth client without need.
- Send direct-to-storage uploads using restricted paths/policies or signed flows. Storage upsert requires insert, select, and update permissions.
- Use Postgres Changes for modest row-change needs and private Broadcast for high-frequency progress when appropriate. Always authorize channel access.

## Worker access pattern

- A trusted worker may use a secret/service key or a constrained direct database role. Keep pools small and appropriate to connection mode.
- Claim queued work atomically. `FOR UPDATE SKIP LOCKED` or a queue primitive should prevent duplicate ownership.
- Write idempotency keys, attempts, leases/heartbeats, provider job IDs, and terminal results.
- Requeue stale work through an audited scheduled process with bounded retry and a dead-letter outcome.

Load `$durable-queue-architecture` before selecting between Supabase Queues, a leased jobs table, Trigger.dev, or another broker. Load `$knowledge-rag-memory` when pgvector or Supabase data backs RAG, so retrieval access control and source deletion remain aligned with product authorization. Use `$neon-postgres-platform` only when evaluating or implementing a deliberate Neon-owned data boundary; do not create two accidental systems of record.

## Change and verification workflow

1. Reproduce or inspect the current state.
2. Prototype SQL without polluting migration history when the environment allows.
3. Run database/security advisors and review grants, RLS, functions, views, and storage.
4. Generate a clean migration using the installed CLI's documented commands.
5. Apply in a safe environment and test as anon, authenticated owner, authenticated non-owner, and trusted server.
6. Verify rollback or forward-repair strategy, Realtime behavior, and data integrity.

Use [references/supabase-platform-record.md](references/supabase-platform-record.md) for architecture and audit work. Never perform destructive production changes unless the user explicitly requested them and the exact target is verified.
