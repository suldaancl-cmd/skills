# Cost, operations & legal failures

The mistakes that don't breach you but still end the project — a surprise bill, a silent outage, a regulator's letter.

## 1. No rate limiting

**What:** Endpoints work for normal use but have no cap on requests per user/IP. Enables brute-forcing logins, scraping, and cost-DoS on LLM/paid endpoints.

**Why AI does it:** Rate limiting is deliberate infrastructure the AI won't add unless asked; there's no visible failure until abuse.

**Fix:** Rate-limit middleware on all auth + sensitive + LLM endpoints (express-rate-limit, Upstash, Django ratelimit, or a Cloudflare/API-gateway rule independent of app code). *Evidence: Zuplo found only 1 of 15 vibe-coded apps had any rate limiting — and it was bypassable.*

## 2. Runaway LLM / cloud cost

**What:** An app calls OpenAI/Anthropic per request with no per-user quota, no caching, no spend cap, and defaults to the most expensive model for trivial tasks. A viral moment, a bot, or a stolen key runs up thousands overnight. Agentic loops compound it — by step 30 each call resends the whole history, so it costs ~30× step 1.

**Fix:**
- Hard monthly spend caps in the provider dashboard **before** writing code.
- Per-user token/request quotas in multi-tenant apps.
- Cache deterministic responses.
- **Model routing:** cheap model (Haiku, GPT-4o-mini) for simple tasks, flagship only for hard reasoning.
- Billing alerts at 50% and 100% of expected spend.

*Evidence: documented "$20→$200 overnight" Lambda blowups; 170M tokens in 2 days; stolen-key bills >$10k.*

## 3. No observability

**What:** App ships with no error tracking, no structured logging, no uptime/latency monitoring, no billing alerts. The first sign of trouble is a user complaint or a huge invoice.

**Why AI does it:** It scaffolds features, not observability — and the dev doesn't ask.

**Fix (≈30 min, prevents hours of blind debugging):** Sentry (one line) for errors; structured logging with levels (not `console.log`); uptime checks (Vercel/Railway/UptimeRobot); DB-level audit logs on destructive ops; billing alerts. Before deploy, answer: *"How will I know if something goes wrong?"*

*Evidence: Amazon Kiro — an unreviewed AI deploy caused a 6-hour outage, ~6.3M lost orders; billing alerts "weren't configured" is a near-universal omission in vibe-coded apps.*

## 4. Exposed internal tools

**What:** Admin dashboards, knowledge bases, and chatbots trained on company data get deployed to a public URL "just to test" with no auth — and stay there. The URL is the only thing hiding them.

**Fix:** Auth gate (even HTTP basic / Cloudflare Access / Vercel Password Protection) before the *first* deploy of anything internal.

*Evidence: Wiz — 1 in 5 orgs exposed internal vibe-coded apps; ~380k publicly reachable apps, ~5,000 leaking sensitive corporate data (vessel schedules, clinical-trial data, patient conversations).*

## 5. PII exposure & GDPR/CCPA gaps

**What:** Two failure modes. (a) Storage (Firebase/S3/Supabase Storage) left public-read by default → IDs, selfies, messages exposed. (b) No consent layer / privacy scaffolding — cookie consent, DPA, right-to-erasure, telemetry shipping PII without consent.

**Why AI does it:** It scaffolds functional code; privacy/regulatory scaffolding is invisible work it won't add unless asked.

**Fix:**
- Storage buckets private by default; per-user ACLs; never store identity docs in a publicly reachable path.
- Data minimization — only collect what you need, document why.
- Add a consent management platform (Cookiebot/CookieYes) and a lawyer-reviewed privacy policy before any EU/UK/California users.
- DAST scan (OWASP ZAP/Burp) before launch to find exposed endpoints.

*Evidence: Tea app — unsecured Firebase bucket exposed ~72,000 images incl. 13,000 government IDs + 1.1M private messages; a GDPR Art. 32 / 5(1)(f) breach. Escape.tech found 175 PII-exposure instances across 5,600 apps. GDPR fines reach 4% of global turnover.*
