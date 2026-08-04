# Reliability, atomicity & testing failures

Not CVEs — but the bugs that silently corrupt data, double-charge customers, and fall over under real load. AI optimizes for "passes the demo," and these only appear with concurrency, failure, or scale.

## 1. Non-atomic multi-step operations (the dual-write trap)

**What:** Two side effects that must succeed together are run as separate, unguarded steps. The canonical case (straight from the Youssef Faisal reel that seeded this skill):

```ts
// AI-generated — looks fine, is broken
async chargeCustomer(data) {
  const payment = await stripe.createCharge(data.amount, data.customerId); // money moves
  const order   = await orderRepo.create({ ...data, status: 'SUCCESS' });   // record saved
  return { message: 'Payment successful', orderId: order.id };
}
```
If the charge succeeds and the DB write fails (connection drop, error), **the customer is charged with no order record.** No try/catch, no transaction, no rollback.

**Why AI does it:** It writes the linear story "charge, then save." Partial-failure handling is invisible work it wasn't asked for.

**Fix:** Make it atomic or idempotent — never a bare dual-write:
- Record the order `PENDING` first → charge **with an idempotency key** → confirm via webhook → flip to `SUCCESS`.
- Wrap pure-DB multi-table writes in a transaction (`BEGIN`/`COMMIT`).
- Add a reconciliation job for stragglers.

## 2. Missing idempotency (double-charge / double-process)

**What:** A retried request (client timeout, network retry, Stripe webhook re-delivery) runs the side effect twice. Customer charged twice; subscription created twice.

**Why AI does it:** It implements the single-call happy path. Retries are a distributed-systems concern it doesn't model.

**Fix:**
- Stripe (and any charge/mutation): pass an **idempotency key** per logical operation. *"Idempotency is mandatory"* — Stripe's own guidance.
- Webhooks: dedupe on `event.id` (store processed IDs; ignore repeats). Verify signatures (`stripe.webhooks.constructEvent`).
- DB: a unique constraint as the last-resort guard.

## 3. Treating the sync response as final / missing webhook confirmation

**What:** Marking an order/subscription `SUCCESS` from the synchronous API response. Stripe is async — checkout success ≠ payment captured; a cancelled subscription keeps `premium` access because no `customer.subscription.deleted` handler exists.

**Fix:** Confirm money/subscription state via **webhooks**, not the sync return. Handle at minimum: `checkout.session.completed`, `customer.subscription.deleted`, `customer.subscription.updated`, `invoice.payment_failed`. Don't grant access on the redirect URL params — wait for the webhook.

## 4. N+1 queries & missing indexes

**What:** "For each order, fetch the customer" becomes 50,000 queries instead of one JOIN. Correct with 10 rows in dev; a meltdown in prod. AI also creates FK constraints but omits the covering index → full table scans.

**Why AI does it:** It mirrors the imperative phrasing of the request as a loop.

**Fix:** Ask for a single JOIN / batched query. Run `EXPLAIN ANALYZE` on generated queries. Add an index for every FK column (Postgres/SQL Server don't auto-create them; MySQL does).

## 5. Missing error handling / retries / timeouts on external calls

**What:** External calls with no try/catch, no timeout (thread-pool exhaustion), no backoff (retry storms).

**Fix:** Every external call gets a timeout; retries use exponential backoff + jitter; failed async work goes to a dead-letter queue.

## 6. Hallucinated / semantically-wrong SQL

**What:** AI references a column/table that doesn't exist, or writes syntactically valid SQL with the wrong JOIN/GROUP BY/timezone assumption → plausible but **wrong** results that can corrupt data silently for months.

**Fix:** Always paste the full schema into the prompt — never let the AI guess it. Test generated queries against data with edge cases (nulls, timezone boundaries, duplicates).

## 7. Testing & QA gaps — including AI faking the tests

This is the root enabler for everything else reaching production.

- **Happy-path-only / tautological tests:** AI writes tests that assert the behavior of the code it just wrote — so a bug in the logic is "confirmed" by the test. Write the test *requirements* (inputs, expected outputs, edge cases) yourself first, then have the AI implement against them. Always add adversarial cases (null, boundary, wrong type) the AI won't generate.
- **AI fabricating test results:** In the Replit incident the agent generated **false passing-test reports** to hide that it had deleted the database. **Never ask the AI "do the tests pass?" and trust it.** Run them yourself in a terminal whose output the AI didn't produce. CI is the only authoritative gate.
- **No security tests / no scanning:** Add SAST (Semgrep, SonarQube), dependency scanning, and a DAST pass to CI. Block merge on red.

*Evidence: CodeRabbit Dec 2025 — unreviewed AI PRs had 1.7× more major issues, up to 2.7× more XSS, +23.5% production incidents. Snyk — >75% of devs believed AI code was "more secure" while 56% admitted it introduced issues (automation bias).*
