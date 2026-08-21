# Mobile release evidence

## Candidate identity

- Commit/build/version:
- Environment:
- API/database/worker versions:
- Feature flags:
- Test accounts and data class:

## Critical-flow matrix

| Flow | iOS result/device | Android result/device | Automated coverage | Failure evidence | Owner |
|---|---|---|---|---|---|

## AI and durable-job checks

- Valid request success.
- Invalid/unsafe request handling.
- Provider timeout and failure.
- Duplicate request/webhook.
- App closed and resumed.
- Approval allow/deny/expiry.
- Budget and rate-limit enforcement.
- Charge/refund idempotency.
- Output reporting/moderation.

## Nonfunctional evidence

- Accessibility and dynamic text.
- RTL/localization.
- Cold start and representative interaction performance.
- Offline/slow network.
- Privacy and telemetry payload inspection.
- Crash/error diagnostics with redaction.

## Decision

- Critical blockers:
- Accepted risks and owner:
- Rollback/feature-disable path:
- Go / conditional go / no-go:
