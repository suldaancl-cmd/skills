# Queue design record

## Selection

| Option | Strength | Operational cost | Required semantics | Decision |
|---|---|---|---|---|
| Supabase Queues/PGMQ | | | | |
| Claimed job table | | | | |
| Trigger.dev queue | | | | |
| Dedicated broker | | | | |

## Message contract

- Type/version:
- Payload reference and maximum size:
- Tenant/job identity:
- Correlation/idempotency key:
- Visibility/lease and heartbeat:
- Retention/archive:

## Consumer contract

- Claim/read operation:
- Authorization recheck:
- Idempotent side-effect boundary:
- Acknowledge/delete/archive condition:
- Graceful shutdown:

## Retry/dead-letter matrix

| Error class | Retry | Backoff | Maximum | Final state | Operator action |
|---|---|---|---|---|---|

## Capacity

- Arrival rate and burst:
- Processing latency distribution:
- Concurrency bottleneck:
- Maximum queue age:
- Admission control:
- Database/HTTP pool budget:

## Failure evidence

- Duplicate delivery.
- Worker crash before/after state commit.
- Visibility expires during processing.
- Message schema from previous deployment.
- Poison message and replay.
- Outbox row never publishes.
