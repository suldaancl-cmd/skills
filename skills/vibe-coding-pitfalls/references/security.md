# Security failures in AI-generated code

The bulk of vibe-coding disasters are here. Each section: **what it is → why the AI does it → how to catch it → the fix**. OWASP/CWE mapping in headers so you can cite it.

## Table of contents
1. Secrets management (OWASP-LLM02 / GitGuardian)
2. Broken access control & RLS (OWASP A01)
3. IDOR — insecure direct object reference (CWE-639)
4. Authentication & session (OWASP A07)
5. Injection: SQL / command (OWASP A03, CWE-89/78)
6. XSS / insecure output handling (CWE-79, OWASP-LLM05)
7. Cryptographic failures (OWASP A02, CWE-330)
8. Security misconfiguration & deploy (OWASP A05 → #2 in 2025)
9. File upload → RCE (CWE-434)
10. Verbose errors / info leakage (OWASP A09)

---

## 1. Secrets management — the #1 AI amplifier

**What:** API keys, payment secret keys, SMTP/DB passwords, service-role keys hardcoded in source, committed to git, or shipped in the client JS bundle.

**Why AI does it:** It generates "make it work now" code and inlines whatever value gets the demo running. Developers paste real keys into the chat for context; the model writes them into files. Frontend-first scaffolds (Lovable/Bolt) call third-party APIs directly from the browser, embedding the key in the bundle.

**Catch it:**
- `git log -p | grep -iE "(api|secret|key|token|password)"` and scan the built client bundle (`/_next/static/...`, `dist/`) for `sk_`, `AIza`, `eyJ`, service-role JWTs.
- Confirm `.env` is in `.gitignore` **before** the first commit (git history keeps it forever otherwise).
- Run `trufflehog git file://.` or a GitGuardian/`git-secrets` pre-commit hook.

**Fix:**
- Secrets only in env vars / a secrets manager (Doppler, Vault, AWS Secrets Manager). Never in the repo, never in client code.
- All third-party calls that need a secret key go through a server function (API route, Edge Function, Worker) — the browser never sees the secret.
- **Rotate any key that ever touched source control**, even for one second — GitHub's index is near-real-time and bots scrape within minutes.
- Treat your AI tool's local chat-history/transcript files as sensitive (they store pasted secrets unencrypted, outside `.gitignore`).

*Evidence: GitGuardian 2026 — 29M secrets leaked in 2025, AI commits at ~3.2% vs 1.5% baseline; 24k secrets in MCP config files. Moltbook leaked 1.5M tokens via a hardcoded key in client JS.*

---

## 2. Broken access control & Row-Level Security — OWASP A01 (the #1 web risk)

**What:** Any authenticated user can read/modify data that isn't theirs because authorization isn't enforced server-side. The dominant vibe-coding form: **Supabase/Postgres tables with RLS disabled**, so the public `anon` key reads everything.

**Why AI does it:** Supabase creates tables with RLS **off by default**. The generated CRUD "works" because the developer tests it while authenticated as themselves. Neither the AI nor a non-technical builder thinks to enable RLS. Authorization is also frequently enforced **only client-side** (hide the admin button) because that's what produces a visible result.

**Catch it:**
- `SELECT tablename FROM pg_tables WHERE schemaname='public';` then confirm each has RLS: check `pg_policies`, or use Supabase Dashboard → Advisors (must show zero "RLS disabled in public").
- For every permission check in the frontend, find the corresponding **server-side** check. If the API trusts the client, it's broken. Test by calling the endpoint directly with `curl` using a different user's token.

**Fix:**
```sql
ALTER TABLE <table> ENABLE ROW LEVEL SECURITY;
-- deny-all first, then add explicit policies:
CREATE POLICY "owner_read" ON <table> FOR SELECT USING (user_id = auth.uid());
```
- Every authorization decision lives on the server / in the database. Frontend checks are UX only, never security.
- Never use the service-role key client-side.

*Evidence: Lovable CVE-2025-48757 — 303 endpoints across 170 apps readable unauthenticated. Enrichlead — client-side-only paywall bypassed via DevTools. Base44 — endpoints with zero auth.*

---

## 3. IDOR — insecure direct object reference — CWE-639

**What:** `GET /api/orders/100` → change to `101` → you get someone else's order. The query fetches by ID from the URL without checking ownership.

**Why AI does it:** It writes the literal request ("get the order with this id") and stops there. The ownership check is a separate concern it wasn't asked for. Passes basic testing because user A sees user A's data.

**Catch it:** For every route that takes an `:id`, confirm the query also constrains to the current user. Probe by incrementing IDs as a logged-in low-priv user.

**Fix:** Always scope by owner, not just ID:
```sql
SELECT * FROM orders WHERE id = $1 AND user_id = $2;  -- not just WHERE id = $1
```
At the DB layer, an RLS policy `USING (user_id = auth.uid())` makes it impossible to forget.

*Evidence: 43% of 100 scanned Cursor-built production repos had IDOR (dev.to/tgoldi scan).*

---

## 4. Authentication & session — OWASP A07

**What:** Missing auth on endpoints; hand-rolled JWT with `alg:none`/no signature check; plaintext or weakly-hashed passwords; tokens stored where the client can read them; password-reset/JWT tokens valid for days; no CSRF protection.

**Why AI does it:** It generates plausible-looking auth that handles the happy path. Token-lifetime and storage details are silent defaults it picks badly (long-lived refresh tokens, localStorage instead of `HttpOnly` cookies). CSRF is invisible until exploited.

**Catch it:**
- Is auth a real library (Auth.js, Passport, Supabase Auth, Clerk) or hand-rolled? Hand-rolled is a red flag.
- Token TTLs: access tokens minutes, reset tokens 10–15 min — not "a week."
- Where are tokens stored? Must be `HttpOnly`, `Secure`, `SameSite` cookies — not localStorage / a readable cookie.
- Is there CSRF protection on state-changing routes? (A 2026 audit found 100% of 15 vibe-coded apps lacked it.)

**Fix:** Proven auth library; `crypto.randomBytes`/`secrets.token_hex` for tokens (not `Math.random` — CWE-330); bcrypt/argon2 for passwords; short TTLs; `HttpOnly` cookies; SameSite + CSRF tokens.

---

## 5. Injection: SQL / command — OWASP A03, CWE-89 / CWE-78

**What:** User input concatenated into a SQL string (`WHERE name = '${input}'`) or a shell command. `Ali' OR 1=1 --` dumps the table; `; rm -rf` runs on the host.

**Why AI does it:** String interpolation is the shortest path to a working query in a demo. It defaults there unless explicitly told to parameterize.

**Catch it:** Grep for string-built SQL and any `exec`/`spawn`/`os.system` with interpolated input. Run sqlmap against inputs before shipping.

**Fix:** Parameterized queries / ORM only — never concatenate user input into SQL. For shell, avoid it; if unavoidable, use arg arrays (`execFile(cmd, [args])`), never a string.

*Evidence: Perry et al. (ACM CCS 2023) — developers with AI assistants produced more SQLi. Veracode 2025 — ~45% of AI code has an OWASP Top-10 flaw.*

---

## 6. XSS / insecure output handling — CWE-79, OWASP-LLM05

**What:** User-controlled data rendered as HTML — `Html.Raw(x)` (MVC), `element.innerHTML = x`, `dangerouslySetInnerHTML`. Attacker injects `<script>` that steals cookies/sessions/credit-card data. Also: LLM output rendered without sanitization.

**Why AI does it:** Rendering raw HTML is the direct way to "show this content." It doesn't distinguish trusted from untrusted strings.

**Catch it:** Grep for `Html.Raw`, `innerHTML`, `dangerouslySetInnerHTML`, `v-html`, `|safe`. Each is guilty until proven sanitized.

**Fix:** Render as text (JSX, auto-escaping templates are safe by default). If you must render user HTML, run it through DOMPurify/bleach first. Add a strict Content-Security-Policy header.

*Evidence: Veracode 2025 — 86% XSS failure rate, the worst single class tested.*

---

## 7. Cryptographic failures — OWASP A02, CWE-330

**What:** `Math.random()` for tokens/IDs; MD5/SHA-1 for passwords; hardcoded keys/IVs; self-rolled crypto; missing TLS.

**Why AI does it:** Insufficient randomness (CWE-330) is the single most-measured AI weakness — it reaches for the familiar `Math.random()`/`uuid` and confidently writes broken custom crypto.

**Fix:** CSPRNG only (`crypto.randomBytes`, `secrets.token_bytes`); bcrypt/argon2 for passwords; vetted libraries (libsodium); TLS 1.2+; never self-roll crypto.

---

## 8. Security misconfiguration & deploy — OWASP A05 (moved to #2 in OWASP 2025)

**What:** `Access-Control-Allow-Origin: *` (especially combined with credentials — forbidden by spec); debug mode on; missing security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options); internal/admin tools deployed to a public URL with no auth.

**Why AI does it:** Wildcard CORS is the least-resistance fix for a browser CORS error during dev — and it ships. "Internal" tools get a public URL "just to test" and stay there.

**Catch it:** Check CORS config, `NODE_ENV`/`DEBUG`, response headers, and whether any admin/internal route is reachable without auth.

**Fix:** CORS allowlist of explicit origins; `debug=False` in prod; security headers via Helmet/Django SecurityMiddleware; put every internal tool behind auth (Cloudflare Access, Vercel Password Protection) — the URL is not a secret.

*Evidence: Wiz — 1 in 5 orgs exposed internal vibe-coded apps publicly; ~380k publicly reachable apps found.*

---

## 9. File upload → remote code execution — CWE-434

**What:** Upload handler stores whatever it receives with no type/size validation. Attacker uploads an executable / web shell → runs commands → owns the server.

**Why AI does it:** It writes the happy-path "save the file" and skips validation; the dev tests with a valid image and calls it done.

**Fix:** Validate MIME type server-side (not just extension) against an allow-list; enforce size limits; store uploads in a bucket that is **not served as executable code**; randomize stored filenames.

---

## 10. Verbose errors / info leakage — OWASP A09

**What:** Production responses include `error.stack`, `error.sql`, schema details, internal paths — a free map of your system for an attacker.

**Why AI does it:** Developer-friendly errors help during local dev and ship unchanged.

**Fix:** Global error handler — log full detail server-side, return a generic message + error ID to the client. Set `NODE_ENV=production` so frameworks suppress stack traces.
