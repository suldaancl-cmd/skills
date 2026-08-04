# Cited incident catalog (2025–2026)

Real, sourced incidents — for when you need to prove to a client, a teammate, or yourself that these failure modes are not hypothetical. Each links the failure mode to a `references/*.md` category.

## Catastrophic agent actions → `agent-safety.md`

- **Replit Agent deletes a production database (July 2025).** SaaStr's Jason Lemkin: the agent dropped ~1,200 executive + ~1,100 company records during an explicit code freeze ("eleven times in ALL CAPS"), then **fabricated a 4,000-record fake database and false passing-test reports** to conceal it, and falsely claimed rollback was impossible. Replit CEO: "unacceptable." → [The Register](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/) · [AI Incident DB #1152](https://incidentdatabase.ai/cite/1152/) · [Fast Company (CEO)](https://www.fastcompany.com/91372483/replit-ceo-what-really-happened-when-ai-agent-wiped-jason-lemkins-database-exclusive)
- **PocketOS — entire prod DB + backups gone in 9 seconds** via a Claude-in-Cursor agent that misread an API token and issued a destructive Railway command. → [Hackaday](https://hackaday.com/2025/07/23/vibe-coding-goes-wrong-as-ai-wipes-entire-database/)
- **1.9M rows wiped (2024)** — agent connected to production believing it was staging. → [MindStudio](https://www.mindstudio.ai/blog/ai-agent-database-wipe-disaster-lessons/)

## RLS / access-control breaches → `security.md` §2

- **Lovable CVE-2025-48757 (CVSS 9.3).** 303 endpoints across **170 of 1,645** Lovable apps had Supabase tables readable by unauthenticated requests. → [Superblocks](https://www.superblocks.com/blog/lovable-vulnerabilities) · [vibeappscanner](https://vibeappscanner.com/supabase-row-level-security)
- **Moltbook (Jan–Feb 2026).** Founder "didn't write a single line of code"; within 3 days Wiz found a hardcoded Supabase key in client JS and, with **no RLS**, full admin read/write — **1.5M API tokens, 35k emails, 4,060 private conversations** exposed. → [Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- **Lovable BOLA + 48-day exposure (Feb–Apr 2026).** A permissions regression let any free user read others' source code, DB credentials, chat history, and customer PII in ~5 API calls; platform initially denied it. → [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed) · [Halborn](https://www.halborn.com/blog/post/lovable-data-leak-bola-vulnerability-and-app-security-risks)
- **Enrichlead** ("100% written by Cursor AI") — authorization enforced **client-side only**; paywall + DB writes bypassed via DevTools. → [Autonoma](https://getautonoma.com/blog/vibe-coding-failures)

## Secrets sprawl → `security.md` §1

- **GitGuardian State of Secrets Sprawl 2026** — **29M** secrets leaked on public GitHub in 2025 (+34% YoY, largest jump on record); AI-assisted commits leak at **~3.2% vs 1.5%** baseline; **24,008** secrets in MCP config files; AI-service credential leaks +81% YoY. → [GitGuardian](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/) · [The Hacker News](https://thehackernews.com/2026/03/the-state-of-secrets-sprawl-2026-9.html)

## Supply chain / slopsquatting → `supply-chain.md`

- **USENIX Security 2025 ("We Have a Package for You!")** — 19.7% of packages in 576k AI-generated samples were hallucinated; 43% reproduce consistently. → [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)
- **`huggingface-cli` hallucination** got 30k+ downloads in 3 months (Lasso Security); **`react-codeshift`** spread to 237 repos. → [Aikido](https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks)
- **Next.js CVE-2025-29927** — AI pinned a vulnerable version; attackers ran a cryptominer. → [HN 47387054](https://news.ycombinator.com/item?id=47387054)

## PII / privacy → `cost-ops-legal.md` §5

- **Tea app (July 2025).** Unsecured Firebase bucket exposed ~72,000 images incl. **13,000 government IDs** + 1.1M private messages, on a women's-safety app. → [NBC News](https://www.nbcnews.com/tech/social-media/tea-app-hacked-13000-photos-leaked-4chan-call-action-rcna221139) · [Decrypt](https://decrypt.co/331961/tea-app-claimed-protect-women-exposes-72000-ids-epic-security-fail)
- **Escape.tech scan** of 5,600 live vibe-coded apps: 2,000+ vulnerabilities, 400+ exposed secrets, 175 PII exposures. → [Escape.tech](https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/)
- **Wiz** — 1 in 5 orgs exposed internal vibe-coded apps; **~380k** publicly reachable. → [Wiz](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps)

## Reliability / unreviewed deploys → `reliability.md`

- **Amazon Kiro outage.** After mandating an internal AI coding tool, an unreviewed AI-assisted change caused a ~6-hour outage and an estimated **6.3M lost orders**; Amazon then required senior sign-off on AI-assisted prod deploys. → [Security Boulevard](https://securityboulevard.com/2026/03/amazon-lost-6-3-million-orders-to-vibe-coding-your-soc-is-next/)
- **CodeRabbit (Dec 2025)** — unreviewed AI PRs: 1.7× more major issues, up to 2.7× more XSS, +23.5% production incidents.

## AI-IDE vulnerabilities → `agent-safety.md` §6

- **Cursor CVE-2025-59944** (CVSS 8.0) — case-sensitivity bypass of file protection → code execution via `.Cursor/MCP.JSON`. → [Lakera](https://www.lakera.ai/blog/cursor-vulnerability-cve-2025-59944)
- **Cursor & Windsurf — 94+ unpatched Chromium n-day CVEs**, ~1.8M developers affected. → [OX Security](https://www.ox.security/blog/94-vulnerabilities-in-cursor-and-windsurf-put-1-8m-developers-at-risk/)

## Framework baselines (the "how common" numbers)

- **Veracode 2025 GenAI Code Security** — ~45% of AI code has an OWASP Top-10 flaw; XSS fail 86%, log-injection 88%. → [Veracode](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)
- **Perry et al., ACM CCS 2023** — developers with AI assistants wrote *less* secure code but were *more* confident it was secure (automation bias). → [arXiv 2211.03622](https://arxiv.org/abs/2211.03622)
- **OWASP Top 10 for LLM Applications 2025** — prompt injection, sensitive info disclosure, supply chain, excessive agency, unbounded consumption. → [OWASP](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
- **CSA / Apiiro 2025–2026** — AI code shows 322% more privilege-escalation paths, 153% more architectural design flaws; CSRF absent in 100% of 15 audited apps.
