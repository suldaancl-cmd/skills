# TanStack Query cache policy

## Resource policy

| Resource | Key factory | Freshness | GC/persistence | Retry | Refetch triggers | Realtime action |
|---|---|---|---|---|---|---|

## Identity boundary

- User/organization fields in key:
- Cache action on login/logout/switch:
- Sensitive resources excluded from persistence:
- Environment/schema cache buster:

## Mutation policy

| Mutation | Client operation ID | Optimistic patch | Rollback | Invalidation/reconcile | Offline replay allowed |
|---|---|---|---|---|---|

## Realtime policy

- Channel/topic authorization:
- Event version ordering:
- Patch versus invalidate decision:
- Reconnect authoritative fetch:
- Subscription cleanup:

## Mobile lifecycle

- Online source:
- AppState focus behavior:
- Screen-focus refresh exceptions:
- Background polling policy:
- Request cancellation:

## Failure checks

- Two identities on one device.
- Optimistic update followed by server rejection.
- Duplicate mutation and delayed response.
- Realtime event arrives before/after mutation response.
- Persisted cache from an older schema or environment.
