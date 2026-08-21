---
name: neon-postgres-platform
description: Evaluate, design, implement, or audit Neon Postgres for serverless/edge applications, connection methods and pooling, branches, migrations, security, backups, and pgvector. Use when Neon is selected or being compared; not as an automatic replacement for Supabase Auth/Storage/Realtime.
---

# Neon Postgres platform

Treat Neon as PostgreSQL infrastructure with platform capabilities. It does not automatically replace a complete Supabase product stack.

## Make the adoption decision first

- Inventory what the current platform provides: Postgres, Auth, RLS/API, Storage, Realtime, Queues, Edge Functions, dashboards, backups, and integrations.
- Use Neon when its Postgres, serverless connectivity, branching, isolation, or operational model solves a demonstrated need.
- For an existing Supabase application, prefer keeping Supabase as the product system of record unless a separate workload or measured limitation justifies Neon.
- If both exist, assign one authoritative owner per data domain and define one-way integration/outbox; never create unsupervised bidirectional replication.

## Verify current platform facts

- Inspect project/branch topology, Postgres version/extensions, region, compute settings, roles, connection strings, driver/ORM, pooling, backups/PITR, and plan limits.
- Verify current Neon docs before making claims about scale, connection counts, autosuspend, retention, or pricing.
- Keep schema and migrations portable PostgreSQL when practical; isolate platform-specific operations.

## Select the connection method

- Use a direct connection for migrations, administrative work, logical/session behavior, or long-lived services when required.
- Use a pooled connection for bursty/serverless clients that would otherwise exhaust database connections.
- Use the supported serverless/edge driver where the runtime cannot use a conventional TCP client.
- Do not put a client-side pool on top of a pooled Neon endpoint unless the documented architecture requires it.
- Keep pools bounded and align transaction/session expectations with PgBouncer/driver behavior.
- Never connect Expo or browser clients directly with a privileged database URL. Use a trusted API and application authorization.

## Branching and environments

- Use copy-on-write branches for development, preview, migration testing, data recovery experiments, or isolated agents where appropriate.
- Define branch creation source, expiry, owner, sensitive-data policy, migration direction, and cleanup.
- Do not expose production personal data to preview environments without authorization, minimization, and access controls.
- Treat merging application code and promoting database schema/data as separate operations with an explicit migration path.

## Security and data access

- Use separate least-privilege roles for application runtime, migrations, read-only analytics, and workers.
- Store connection credentials only in trusted secret stores and rotate suspected exposures.
- Enforce tenant authorization in the API/database design. Plain PostgreSQL does not provide Supabase's authenticated Data API automatically.
- Review network controls, TLS, role grants, default privileges, extensions, functions, search paths, and audit needs.

## pgvector and AI data

- Enable and version pgvector only when semantic retrieval is required.
- Store embedding model/version, source identity, chunk identity, tenant/ACL metadata, and deletion lineage.
- Select vector index and parameters from measured corpus/query behavior; benchmark recall, latency, build/update cost, and filtered retrieval.
- Keep raw knowledge sources and document ACLs authoritative outside an embedding alone.

## Operations and migration

- Validate schema changes on a branch with representative data, then apply through committed migrations.
- Monitor query latency, connection pressure, compute activation, storage growth, locks, index health, and expensive vector queries.
- Test backup/PITR and application recovery; a branch is useful but not a complete incident plan.
- Before migration, reconcile row counts, constraints, sequences, roles, extensions, time zones, large objects/files, and cutover writes.

Use [references/neon-adoption-record.md](references/neon-adoption-record.md). Report “keep Supabase” when Neon adds complexity without a concrete benefit.
