---
name: durable-agent-worker
description: Design, implement, or audit a durable AI worker for long-running multi-step jobs with queues, LangGraph-style checkpoints, tools, retries, approvals, provider webhooks, and progress events. Use when work must survive client closure or process restart; not for a single short completion.
---

# Durable agent worker

Make agent execution resumable, bounded, authorized, and financially safe.

## Decide whether a worker is warranted

Use a durable job when any of these apply:

- Execution can outlive a normal API request.
- A provider returns an asynchronous job or webhook.
- Work requires retries, approvals, multiple tools, or checkpoints.
- The user may close the app and return later.
- Duplicate execution can cost money or cause an external side effect.

Keep a simple synchronous completion synchronous. Do not create one service per named agent.

## Load the focused companion when needed

- Use `$langchain-agent-tooling` for model/provider integration, context engineering, and typed tool contracts.
- Use `$langgraph-agent-orchestration` when execution needs an explicit state graph, checkpointer, interrupt, or subgraph.
- Use `$durable-queue-architecture` to choose the transport and define delivery, lease, retry, backpressure, and dead-letter semantics.
- Use `$trigger-dev-workflows` only when Trigger.dev is the selected execution platform; do not run the same job concurrently in both Trigger.dev and a Contabo worker.

## Separate control plane and execution

- The control plane authenticates the user, validates entitlement, creates the durable job, reserves funds, and exposes status.
- The worker claims jobs, runs the graph, calls providers, records attempts and events, and publishes progress.
- The database is authoritative for job state. In-memory state is a cache, never the only checkpoint.
- Provider adapters normalize submission, polling/webhooks, cancellation, usage, result, and error semantics.

## Define the state machine first

Use explicit states and allowed transitions. A useful baseline is in [references/job-state-machine.md](references/job-state-machine.md). Separate:

- User-visible job state.
- Worker lease state.
- Graph checkpoint/state.
- Provider operation state.
- Financial reservation/settlement state.

Never infer financial completion merely from a natural-language agent message.

## Execute safely

- Claim atomically and attach a lease owner plus expiry/heartbeat.
- Use a stable correlation ID and idempotency key across API, queue, worker, provider, webhook, ledger, and notifications.
- Checkpoint after meaningful side effects and before waiting for user or provider input.
- Bound total steps, tool calls, retries, elapsed time, provider spend, output size, and parallelism.
- Classify errors as retryable, non-retryable, user-action required, provider-pending, or policy-blocked.
- Retry only idempotent operations or operations protected by a provider/idempotency key.
- Route exhausted work to a terminal/dead-letter state with an operator-visible reason.

## Tools and approval

- Give tools narrow schemas and least privilege. Validate tool input outside the model.
- Treat provider and retrieved content as untrusted data, not instructions that can override system policy.
- Require human approval immediately before payments, publishing, destructive changes, outbound messages, permission changes, or other consequential actions unless the product has an explicit pre-authorized policy.
- Store the approval subject, requested action, actor, timestamp, scope, and decision so resume cannot approve a different action.

## Money and usage

- Reserve estimated funds before costly execution.
- Record provider usage and cost independently from model output.
- Commit the charge once for a successful billable outcome; release or refund once according to deterministic rules.
- Reconcile ledger, provider usage, and job outcomes. Do not let retries duplicate settlement.

## Progress and privacy

- Emit semantic progress events such as planning, waiting for approval, provider processing, validating, and completed.
- Do not stream hidden reasoning, raw secrets, provider credentials, or sensitive tool payloads.
- Redact logs and retain only the data required for support, billing, evaluation, and audit.

## Verification

Test success, process crash after side effect, duplicate delivery, stale lease, provider timeout, webhook duplication/out-of-order arrival, user cancellation, approval denial, budget exhaustion, and refund idempotency. A happy-path demo is not sufficient.
