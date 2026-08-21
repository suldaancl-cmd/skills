---
name: durable-queue-architecture
description: Design, implement, or audit durable queue transport and worker consumption using Supabase Queues/PGMQ, PostgreSQL claims, Trigger.dev queues, or another broker. Use for visibility timeouts, acknowledgements, retries, concurrency, backpressure, ordering, outbox, and dead letters; not for UI caching.
---

# Durable queue architecture

Queues decouple acceptance from execution. They do not by themselves make external side effects exactly once.

## Choose the transport deliberately

- Use Supabase Queues/PGMQ when Postgres-native durable messages, moderate operational scope, and proximity to the system of record are advantages.
- Use a claimed job table when rich user-visible lifecycle/querying is primary and the team can maintain lease, retry, and indexing semantics.
- Use Trigger.dev queues when Trigger.dev owns task execution and managed concurrency/retries/waits are desired.
- Use a dedicated broker only when throughput, latency, partitioning, fan-out, or operational isolation justify another system.
- Avoid two transports for the same logical work unless an explicit bridge/outbox owns the boundary.

## Define message versus job

- A **message** is transport data: ID, type/version, payload reference, enqueue time, attempts, visibility/lease, and trace/idempotency identity.
- A **job** is product state: owner, authorization, progress, approval, result, billing, and user-visible lifecycle.
- Keep large files and sensitive payloads outside the queue; send validated references and a schema version.
- Consumers must re-read authoritative state and authorization before costly or consequential work.

## Delivery semantics

- Assume delivery can be repeated, delayed, or reordered around failures even when a queue advertises strong delivery within a visibility window.
- Make consumers idempotent using a durable operation key and database uniqueness/transaction boundaries.
- Set visibility/lease longer than normal processing or renew it with heartbeats. Detect and recover abandoned work.
- Acknowledge/delete/archive only after the intended durable state is committed.
- Never acknowledge merely because a model produced an answer; validate and settle the product outcome first.

## Retries and dead letters

- Classify errors as transient, permanent/input, policy/auth, user-action, provider-pending, cancellation, or budget exhaustion.
- Use bounded exponential backoff with jitter for transient failures and provider hints where available.
- Do not retry invalid input, revoked authorization, or an unprotected non-idempotent side effect.
- Preserve the last safe error classification and route exhausted messages to an inspectable dead-letter/failed state.
- Define operator replay as a new audited attempt with current authorization, version, and idempotency behavior.

## Concurrency, ordering, and backpressure

- Limit concurrency by the actual bottleneck: provider rate, tenant quota, destination, CPU/GPU, connection pool, or cost budget.
- Partition/order only where business semantics require it; global ordering destroys throughput.
- Measure queue age and oldest message, not only queue length.
- Apply admission control before enqueueing unlimited work the system cannot afford.
- Ensure workers use bounded database and HTTP pools and shut down gracefully without stealing new work.

## Transactions and outbox

When a database change and message publication must agree, use a transactional outbox or a queue operation in the same database transaction where supported. Make outbox publication idempotent and monitor unpublished rows. Do not use dual writes with no reconciliation.

## Supabase-specific boundary

- Verify current Queues/PGMQ docs and Postgres version before implementation.
- Keep queues server-side by default. Exposing queue APIs/Data API schemas requires deliberate grants and RLS; never expose raw queue tables casually to Expo.
- Basic/logged queues prioritize durability; unlogged variants trade durability for performance. Choose explicitly.

Use [references/queue-design-record.md](references/queue-design-record.md). Test duplicate delivery, worker death, visibility expiry, out-of-order completion, poison message, saturation, deployment during backlog, and acknowledgement/state-commit races.
