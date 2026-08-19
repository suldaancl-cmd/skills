# Supabase platform record

## Deployment identity

- Cloud or self-hosted:
- Project/instance purpose:
- Postgres and CLI versions:
- Exposed schemas:
- Connection mode and pool:
- Source-of-truth domains:

## Access matrix

| Resource | anon | authenticated owner | authenticated member | trusted worker | admin |
|---|---|---|---|---|---|

Record Data API grants and RLS separately.

## Job system

- Queue/table:
- Claim operation:
- Lease/heartbeat:
- Retry and dead-letter policy:
- Idempotency boundary:
- Realtime progress channel:
- Result ownership:

## Money and entitlements

- Ledger model:
- Reservation/commit/refund operations:
- Uniqueness constraints:
- Reconciliation source:
- Agent permissions:

## Security checks

- Exposed tables have RLS and intended grants.
- Ownership/membership is present in every policy.
- Update policies use `USING` and `WITH CHECK`.
- Views and privileged functions are reviewed.
- Function execution grants are narrow.
- Storage policies include required upsert actions.
- Secret keys exist only in trusted runtimes.
- Auth deletion/session-revocation behavior is defined.

## Verification identities

Capture tests for anon, owner, non-owner, member roles, expired/revoked session, worker, and malformed input.
