# Durable job state machine

Adapt names to the existing schema; preserve equivalent semantics.

## Suggested user-visible states

- `queued`
- `running`
- `waiting_approval`
- `waiting_provider`
- `succeeded`
- `failed`
- `cancelled`

Terminal states are `succeeded`, `failed`, and `cancelled`. Reprocessing a terminal job requires a new job or an explicit audited recovery operation.

## Transition invariants

- Creation validates ownership and entitlement and establishes the idempotency key.
- Only the trusted control plane reserves/settles/refunds money.
- Only a worker holding the active lease advances executable states.
- Waiting states release compute but keep durable checkpoints.
- Approval resume validates that the stored approval matches the pending action.
- Provider webhooks validate signature, job/provider identity, and monotonic transition before applying.
- Terminal transition and financial settlement are idempotent and transactionally related or reconciled through an outbox.

## Minimum records

### Job

Identity, owner, type, status, input reference, idempotency key, priority, progress, result/error reference, timestamps, and version.

### Attempt

Job, attempt number, lease owner/expiry, graph checkpoint, start/end, classification, and resource usage.

### Event

Job, sequence, semantic type, safe public payload, private diagnostic reference, and timestamp.

### Provider operation

Provider, model, external job ID, request idempotency key, status, usage, cost, webhook sequence, and raw-response reference with retention controls.

### Approval

Job, action fingerprint, summary, requester, approver, scope, decision, expiry, and timestamps.

## Failure scenarios to simulate

1. Worker dies immediately before and after provider submission.
2. Queue delivers the same job twice.
3. Webhook is duplicated or arrives before polling state.
4. Approval is granted after the requested action changed.
5. Cancellation races with provider completion.
6. Charge commits while result write fails.
