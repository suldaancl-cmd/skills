# LangGraph design record

## Need and boundary

- Why a graph is required:
- What remains ordinary code:
- Durable job/queue boundary:
- Graph package and adapter versions:

## State contract

| Field | Type | Owner node | Merge/reducer | Persistence/retention | Sensitive |
|---|---|---|---|---|---|

## Node contract

| Node | Deterministic or agentic | Reads | Writes | Side effect | Idempotency | Retry policy |
|---|---|---|---|---|---|---|

## Identity and persistence

- `thread_id` mapping:
- Checkpointer:
- Durability mode:
- Long-term store:
- Tenant isolation:
- Retention/deletion:
- Schema migration:

## Interrupt record

- Pending action and fingerprint:
- Safe payload exposed:
- Approver and authorization:
- Expiry:
- Resume validation:
- Side effects before interrupt:

## Verification scenarios

- Crash before/after node side effect.
- Duplicate invocation/resume.
- Two workers target one thread.
- Approval action changed or expired.
- Checkpoint from an older graph schema.
- Cancellation while provider work is pending.
