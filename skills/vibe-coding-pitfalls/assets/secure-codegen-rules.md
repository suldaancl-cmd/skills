# Secure-by-default rules for AI coders (Prevent mode)

Paste this block into your Cursor rules, `CLAUDE.md`, `.windsurfrules`, Copilot instructions, or system prompt so the AI defaults to the safe pattern instead of the demo pattern. It targets the highest-frequency vibe-coding failure modes at the source.

---

```
## Security & reliability rules (non-negotiable)

SECRETS
- Never hardcode API keys, tokens, or passwords. Use environment variables only.
- Never put a secret key in client/browser code. Route third-party calls through a server endpoint.
- Ensure `.env` is in `.gitignore` before any commit.

ACCESS CONTROL
- Enable Row-Level Security on every database table; add explicit owner policies. Never rely on the anon key for protection.
- Enforce every authorization check on the SERVER. Frontend checks are UX only.
- For any fetch-by-id, also filter by the current user (ownership), e.g. `WHERE id = $1 AND user_id = $2`.

AUTH
- Use an established auth library (Auth.js, Passport, Supabase Auth, Clerk) — do not hand-roll auth or JWT verification.
- Store tokens in HttpOnly, Secure, SameSite cookies. Access-token TTL in minutes; password-reset/verification TTL 10–15 min.
- Use a CSPRNG (crypto.randomBytes / secrets.token_hex) for all tokens — never Math.random.

INJECTION & OUTPUT
- Parameterized queries / ORM only. Never build SQL by string concatenation.
- Render user data as text. Never use Html.Raw / innerHTML / dangerouslySetInnerHTML on untrusted input; sanitize with DOMPurify if HTML is unavoidable.
- Validate all input server-side (Zod/Pydantic/Joi): type, length, range, allow-listed enums. Validate file uploads by MIME type + size; store outside the executable path.

CONFIG
- CORS: explicit origin allow-list, never `*` (and never `*` with credentials).
- No debug mode, no stack traces to clients in production. Generic error + server-side log only.
- Set security headers (CSP, HSTS, X-Content-Type-Options, X-Frame-Options).
- Put internal/admin tools behind authentication, even for "just testing."

RELIABILITY
- Make multi-step side effects atomic or idempotent. Never charge-then-save without a transaction or idempotency key.
- Payments: idempotency key on every charge; confirm via webhook (verify signature); handle subscription.deleted/updated and payment_failed.
- Add rate limiting to auth and LLM endpoints. Set per-user quotas and provider spend caps.

DEPENDENCIES
- Only use packages that exist on the official registry under the exact correct name. If unsure, say so — do not invent a package name.
- Commit lockfiles. Assume `npm audit` / `pip-audit` will run in CI.

TESTING
- Write tests against the stated requirements (including null/boundary/wrong-type cases), not against your own output.
- Do not claim tests pass unless they were actually run; show the command and real output.

When a request conflicts with these rules, flag it instead of silently producing insecure code.
```

---

**Note:** This reduces the mistake rate but does **not** replace the Audit + Pre-ship passes. Prevention plus verification — not prevention alone. Research shows iterating with the AI can *increase* vulnerabilities over rounds, so still review the output.
