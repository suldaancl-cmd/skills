---
name: trigger-dev-workflows
description: Design, implement, deploy, or audit Trigger.dev v4 background tasks for long-running TypeScript work, retries, waits, queues, concurrency, idempotency, Realtime, schedules, and versioned deployments. Use when Trigger.dev is selected or being evaluated; not for client-side execution.
---

# Trigger.dev workflows

Use Trigger.dev as an execution runtime, not as the product's source of truth. The application database should still own users, jobs, entitlements, approvals, and billable outcomes.

## Decide before adopting

- Compare Trigger.dev Cloud, self-hosting, the existing Contabo worker, Supabase Queues, and ordinary server functions against the actual workload.
- Prefer Trigger.dev when managed long-running TypeScript execution, waits, retries, concurrency control, versioning, and run observability remove meaningful custom infrastructure.
- Keep an existing worker when migration cost, data residency, local tools, Python/GPU/runtime needs, or current reliability makes it the better choice.
- Never let Trigger.dev and another consumer execute the same logical queue without a single ownership/idempotency design.

## Verify current v4 APIs

- Inspect package and CLI versions, `trigger.config`, task directories, deployment environment, and official changelog/docs.
- Do not copy v3 task syntax or unpinned self-hosted images into a v4 project.
- Discover CLI flags from the installed version and keep SDK/build/CLI versions compatible and committed in the lockfile.

## Define task contracts

- Use stable task IDs and typed, validated payloads containing references rather than secrets or huge files.
- Trigger tasks only from a trusted backend with the environment's secret key. The Expo client calls the product API, not Trigger.dev with a server secret.
- Create/update the authoritative application job before triggering and store the returned run ID.
- Use idempotency keys based on the product operation, with a TTL that covers realistic duplicate delivery. Application-side uniqueness must still protect long-lived financial or external side effects.
- Record normalized result/error/usage back to the system of record once.

## Concurrency, queues, retries, and waits

- Assign concurrency limits by constrained resource: provider account, tenant, model, GPU, destination, or ordered entity.
- Queued/waiting runs and executing runs have different cost/concurrency behavior; verify current plan/runtime rules.
- Retry only transient errors and make every retried side effect idempotent.
- Use waits for time or external events instead of busy polling when supported.
- Use `triggerAndWait`/batch wait patterns only inside supported task contexts; inspect result success before consuming output.
- Do not wrap task wait calls in arbitrary `Promise.all` when the platform provides batch trigger-and-wait semantics.

## Realtime and client progress

- Expose only scoped public access or proxy progress through the trusted backend.
- Treat Trigger.dev run status as execution telemetry; reconcile it into the application's user-visible job state.
- Stream safe semantic output. Keep credentials, raw provider payloads, private logs, and hidden reasoning out of client subscriptions.

## Deployment and operations

- Separate dev, preview/staging, and production keys/environments.
- Understand task version locking, child-task version behavior, retries, and replay before deployment.
- Use atomic/skip-promotion workflows when application and task contracts must change together.
- For self-hosting, pin supported images and account for Postgres, Redis, ClickHouse/event retention, object storage, workers, security, backups, and upgrades. Docker Compose alone is not a production architecture.
- Monitor queue age, run duration, retry/exhaustion, concurrency saturation, cost, version, and reconciliation lag.

Use [references/trigger-workflow-record.md](references/trigger-workflow-record.md). Test duplicate trigger, crash around external side effect, wait/resume, cancellation, retry exhaustion, old-version run, partial batch failure, and application/Trigger state disagreement.
