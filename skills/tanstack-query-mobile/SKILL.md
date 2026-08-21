---
name: tanstack-query-mobile
description: Design, implement, or debug TanStack Query server-state management in Expo/React Native, including query keys, freshness, invalidation, mutations, optimistic updates, Realtime integration, focus/network handling, persistence, and offline behavior. Not for SQL/database query design.
---

# TanStack Query for mobile

Use TanStack Query as a cache and synchronization layer for server state. It is not the durable database and should not become a second business-logic system.

## Inspect the existing data layer

- Verify the installed TanStack Query major version, Expo/React Native versions, navigation, fetch client, auth/session handling, persistence, and Realtime subscriptions.
- Preserve established query-key factories and API contracts. Do not install a second server-state library without evidence.
- Use `expo/fetch` or the project's supported fetcher with typed, normalized errors and `AbortSignal` support.

## Design query keys and ownership

- Query keys must encode every server-state input that changes the result: tenant, resource, filters, locale, pagination, and version where relevant.
- Use hierarchical key factories so detail/list invalidation is intentional and discoverable.
- Never include secrets, access tokens, unstable objects, or huge payloads in keys.
- Scope caches correctly when the signed-in user or organization changes; clear or separate private data before another identity can see it.

## Freshness and lifecycle

- Choose `staleTime`, garbage-collection time, polling, and retry per resource based on real freshness and cost—not one global value for every query.
- Configure React Native online status through the supported network source and `onlineManager`.
- Configure foreground/background focus through AppState and `focusManager`; screen focus refresh is a separate product decision.
- Avoid refetch storms from navigation, Realtime, and focus listeners all invalidating the same data.
- Cancel or ignore stale requests when parameters or screens change.

## Mutations and optimistic UI

- Put authorization, validation, idempotency, and business rules on the server; optimistic UI cannot make an operation safe.
- Prevent duplicate submission and attach a stable client operation ID for costly or mutating requests.
- For optimistic updates: cancel conflicting queries, snapshot affected data, apply the minimum patch, roll back on failure, then reconcile with authoritative server state.
- Do not optimistically finalize money, entitlement, deletion, publishing, or AI job success. Show a pending state until the server commits it.
- Invalidate narrowly; direct cache patches are appropriate only when the server response fully represents the canonical update.

## Realtime and long-running jobs

- Let Realtime events patch or invalidate TanStack Query data; do not maintain an unrelated duplicate global store.
- Include entity version/updated time so stale events cannot overwrite newer cache state.
- Subscribe only while needed and clean up on identity/resource change.
- For durable jobs, cache the persisted job state and use Realtime/polling as notification mechanisms. On reconnect, fetch the authoritative state.

## Persistence and offline

- Persist only data suitable for device storage. Exclude secrets and highly sensitive/private content by default.
- Version/bust persisted caches when schemas, identity, or environment change.
- Configure maximum age and storage limits; clear on logout when tenant data must not remain.
- Offline mutation replay requires server idempotency and a conflict policy. Do not automatically replay payments, destructive actions, messages, or expensive AI runs without explicit product semantics.

Use [references/query-cache-policy.md](references/query-cache-policy.md). Test identity switch, app background/foreground, network loss/reconnect, stale Realtime event, optimistic rollback, duplicate tap, expired session, schema/cache migration, and long list pagination.
