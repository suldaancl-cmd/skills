# Pre-ship gate (run before every production deploy of AI-written code)

A hard gate. Nothing ships with a red box. Copy this into the PR/deploy ticket and tick each line. ~15 minutes; it is cheaper than every incident in `references/incidents.md`.

## 🔴 Blockers — fix before deploy

- [ ] **Secrets:** no key/token in source, git history, or client bundle. `.env` gitignored. Ran a secret scanner (`trufflehog` / GitGuardian). Rotated anything ever committed.
- [ ] **RLS / authz:** every DB table has RLS enabled with owner policies (Supabase Advisors = 0 warnings). Every authorization check is enforced server-side. Verified by calling an endpoint with another user's token.
- [ ] **IDOR:** every fetch-by-id also filters by current user. Probed by incrementing IDs as a low-priv user.
- [ ] **Agent ↔ prod:** no AI agent holds a write connection to the production database. Dev/staging/prod use separate credentials. Backups exist and a restore was tested.
- [ ] **Dependencies:** every installed package verified real on the registry. Lockfile committed. `npm audit` / `pip-audit` clean (no high/critical).
- [ ] **Payments/atomicity:** charge+save is transactional or idempotent (idempotency key + webhook confirmation). Cancelled subscriptions actually lose access.

## 🟠 Required — should be green

- [ ] **Auth:** real auth library; tokens HttpOnly + short TTL; reset/JWT TTL in minutes; CSRF protection on state-changing routes.
- [ ] **Injection:** parameterized queries only; no `Html.Raw`/`innerHTML`/`dangerouslySetInnerHTML` on untrusted data; server-side input validation everywhere.
- [ ] **Config:** CORS = explicit origin allow-list (not `*`); debug off; no stack traces to clients; security headers set; internal tools behind auth.
- [ ] **File upload:** MIME + size validated server-side; stored outside the executable path.
- [ ] **Rate limit / cost:** rate limiting on auth + LLM endpoints; provider spend caps set; per-user quotas; billing alerts at 50%/100%.
- [ ] **Tests:** real negative/adversarial tests exist and were **run by a human/CI**, not just claimed by the AI. SAST + dependency scan in CI, merge blocked on red.

## 🟡 Before real users / regulated data

- [ ] **Observability:** error tracking (Sentry), structured logging, uptime monitoring, DB audit logs on destructive ops.
- [ ] **PII/GDPR:** storage buckets private by default; no public-read on user files/IDs; consent layer + privacy policy if EU/UK/California users; data minimization.
- [ ] **Prompt injection:** any LLM feature treats retrieved/user content as untrusted data, not instructions; structured output validated before acting.
- [ ] **AI IDE:** tooling (Cursor/Windsurf/etc.) updated past known RCE-class CVEs; auto-run disabled outside a sandbox.

---

**Reviewer's mindset:** you are reviewing a pull request from a fast, confident, unsupervised junior. The code looking finished is not evidence that it is. Read the diff, run the scanner, run the tests yourself. If you can't tick a 🔴 box, it doesn't ship.
