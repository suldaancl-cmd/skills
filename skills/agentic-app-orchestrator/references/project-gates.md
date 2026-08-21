# Agentic app project gates

## 1. Product gate

Evidence: target user, urgent job, differentiated promise, payment trigger, AI unit economics, MVP exclusions, validation result.

Exit: proceed / validate first / do not build yet.

## 2. Experience gate

Evidence: primary flow, screen/state inventory, editable design tokens/components, LTR/RTL behavior, motion specification, accessibility expectations.

Exit: implementation-ready handoff with named gaps.

## 3. Architecture gate

Evidence: repository instructions, Expo/runtime facts, client/API/worker/system-of-record boundaries, auth/data model, client-cache policy, execution owner, queue semantics, knowledge/memory boundaries, provider and secret boundaries.

Exit: approved decision record and vertical delivery slices.

## 4. Foundation gate

Evidence: environments, authentication, navigation, database migrations/RLS, storage, API client, error model, telemetry foundation.

Exit: authenticated skeleton verified on representative devices.

## 5. Outcome slice gates

For each primary outcome verify UI, backend, authorization, durable execution where needed, failure/cancellation, cost/entitlement, analytics, and tests.

Exit: independently demonstrable outcome.

## 6. Hardening gate

Evidence: security audit, critical-flow tests, AI and retrieval evals, accessibility, RTL, performance, offline/lifecycle, provider degradation, queue recovery, knowledge deletion propagation, observability, recovery and reconciliation.

Exit: release-candidate go/no-go.

## 7. Beta gate

Evidence: signed preview/production-like builds, real-device TestFlight and Play internal/closed results, reviewer access, production backend readiness.

Exit: store-submission authorization.

## 8. Release and learning gate

Evidence: accurate metadata/privacy/payment declarations, submission status, staged rollout, dashboards, alerts, support, rollback/feature-disable, activation/retention/cost review.

Exit: measured iteration decision, not an automatic feature expansion.
