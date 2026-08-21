---
name: mobile-quality-observability
description: Establish or audit mobile quality gates, automated tests, real-device verification, performance, accessibility, analytics, crash monitoring, and AI evaluations. Use before beta/release or when failures cannot be diagnosed; not for store submission logistics alone.
---

# Mobile quality and observability

Create evidence that critical journeys work and enough telemetry to diagnose failures without collecting unnecessary private data.

## Start from risk, not test count

Identify the journeys and invariants whose failure would harm users or the business:

- Sign-up, sign-in, session restoration, and account deletion.
- Primary product outcome.
- Payment, entitlement, wallet reservation, refund, and cancellation.
- File upload/download and result ownership.
- Long-running job recovery and notification.
- Permission, offline, and degraded-provider paths.
- Moderation, reporting, and consequential tool approval.

Map each risk to the cheapest reliable test layer.

## Build a balanced verification system

- **Static:** formatting, types, lint, dependency/config validation, secret scanning.
- **Unit:** deterministic domain rules, reducers, parsers, cost/ledger logic, state transitions.
- **Integration:** auth, RLS, storage, API contracts, worker claims, webhooks, provider adapters with fixtures.
- **Component/UI:** states, accessibility semantics, localization, RTL, loading/error behavior.
- **End-to-end:** a small set of critical flows on representative iOS and Android builds.
- **Real device:** camera/audio, notifications, deep links, keyboard, lifecycle, memory/performance, and platform permissions.
- **AI evaluations:** task success, groundedness where required, policy compliance, tool selection, structured-output validity, latency, and cost.

Avoid tests that only snapshot generated wording or mirror implementation details.

## Observe product and system behavior

- Define a versioned event taxonomy with owner, trigger, properties, privacy class, and business question.
- Correlate client action, API request, durable job, provider operation, and ledger event with safe identifiers.
- Monitor crash-free sessions, API/job success, latency percentiles, queue age, provider error, retry, refund, and cost per successful outcome.
- Use traces and logs for diagnosis, analytics for behavior, and audit records for consequential actions; do not mix their retention or access casually.
- Default to excluding prompt/message contents, credentials, precise location, and personal files from telemetry.

## Performance and resilience

Measure cold/warm start, screen responsiveness, list/animation frame time, memory, network payload, first useful result, time to first token, and durable job completion. Test slow network, offline transitions, app backgrounding, process death, duplicate events, and provider degradation.

## Release evidence

Use [references/mobile-release-evidence.md](references/mobile-release-evidence.md). A release candidate is not ready when a critical check is merely “not tested.” Report:

- What was tested and on which build/device/environment.
- Observed results and artifacts.
- Known failures, severity, and mitigation.
- Checks blocked by unavailable credentials, hardware, or external systems.
- Go/no-go recommendation tied to risk.

Do not enable production analytics, send test notifications, or mutate live data unless the user authorized those actions.
