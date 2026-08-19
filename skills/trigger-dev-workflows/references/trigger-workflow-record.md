# Trigger.dev workflow record

## Adoption decision

- Workload and current runtime:
- Cloud or self-hosted:
- Why Trigger.dev is preferable:
- Source of truth:
- Migration/coexistence boundary:

## Task contract

| Task ID | Payload reference | Product job state | Queue/concurrency | Attempts | Idempotency scope/TTL | Result contract |
|---|---|---|---|---|---|---|

## Waiting and children

- Wait reason and resume source:
- Child task version relationship:
- Batch failure policy:
- Cancellation propagation:

## Environments and deployment

- SDK/CLI/platform versions:
- Dev/preview/staging/prod mapping:
- Secret ownership:
- Atomic promotion requirement:
- Replay policy:

## Reconciliation

- Trigger run ID storage:
- Status/result update path:
- Duplicate terminal update protection:
- Orphan run/job detection:
- Cost/usage reconciliation:

## Operational thresholds

- Maximum queue age:
- Concurrency saturation:
- Retry/dead-letter alert:
- Maximum run duration/cost:
- Event/log retention:
