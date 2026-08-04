---
name: vibe-coding-pitfalls
description: >-
  The field guide to mistakes AI coding tools make and how to catch them. Use this WHENEVER you
  review, audit, harden, or ship AI-generated / "vibe-coded" software — anything produced by
  Cursor, Claude Code, GitHub Copilot, Lovable, v0, Bolt, Replit Agent, Windsurf, or similar.
  Trigger it for "review this AI code", "is this safe to deploy", "security check my app",
  "audit my Supabase/Stripe/auth", "why did my vibe-coded app get hacked", before any
  production deploy of agent-written code, and when setting up rules to PREVENT an AI coder from
  making these mistakes in the first place. Covers security, reliability, AI-agent operational
  safety, supply-chain (slopsquatting), and cost/ops/legal. Built from 5-source research
  (Reddit, Hacker News, YouTube, incident postmortems, OWASP/Veracode/GitGuardian/USENIX).
---

# Vibe-Coding Pitfalls

## Why this exists

AI writes working-looking code fast. The danger is the gap between *looks done* and *is done*:
the missing ownership check, the secret in the client bundle, the non-atomic payment, the
hallucinated package, the agent with a write connection to prod. These don't show up in the
happy-path demo — they show up as a breach, a double charge, a deleted database, or a $10k bill.

The hard numbers behind this (cited in `references/incidents.md`):

- **~45%** of AI-generated code samples contain an OWASP Top-10 vulnerability (Veracode 2025); XSS fail rate **86%**.
- AI-assisted commits leak secrets at **~2× the human rate**; **29M** secrets hit public GitHub in 2025 (GitGuardian).
- **19.7%** of AI-suggested package names are hallucinated (USENIX 2025) — and **43%** repeat, so attackers can pre-register them.
- Real losses: Replit agent **deleted a production database**; Lovable **CVE-2025-48757 exposed 170 apps**; Tea app leaked **13,000 government IDs**; Amazon **lost ~6.3M orders** to an unreviewed AI deploy.

The fix is not "stop using AI." It's: **treat every AI output like a pull request from a fast, confident, unsupervised junior** — useful, but it does not get merged unread. This skill is the checklist for reading it.

## The three ways to use this

| Mode | When | What to do |
|---|---|---|
| **Prevent** | Before/while the AI writes code | Paste `assets/secure-codegen-rules.md` into your Cursor rules / `CLAUDE.md` / system prompt so the AI defaults to the safe pattern. |
| **Audit** | Reviewing existing AI code | Run the **Priority-10 checklist** below; open the relevant `references/*.md` for the deep dive on any category that's in scope. |
| **Pre-ship** | Before a production deploy | Run `assets/pre-ship-checklist.md` as a hard gate. Nothing ships red. |

Most sessions are **Audit** + **Pre-ship**. Reach for the reference files when you hit a category that applies — don't try to hold all of it in your head.

## The Priority-10 checklist (audit pass)

Ordered by real-world frequency × blast radius. For each: the one question that catches it. Deep dives + fix code are in the linked reference file.

| # | Category | The check that catches it | Deep dive |
|---|---|---|---|
| 1 | **Secrets** | Any key/token in source, client JS bundle, or git history? Is `.env` gitignored? Did anyone paste a real key into the AI chat? | `references/security.md` |
| 2 | **Access control / AuthZ** | Does every "fetch my X" query filter by the current user (not just the ID)? Is Supabase/Firebase **RLS enabled on every table**? | `references/security.md` |
| 3 | **AI-agent operational safety** | Does the agent have a **write connection to production**? Separate dev/staging/prod creds? Did you *run the tests yourself* or trust the AI's word? | `references/agent-safety.md` |
| 4 | **Supply chain / slopsquatting** | Does every `npm/pip install` name actually exist on the real registry, from the expected publisher? Lockfile committed? `npm audit` clean? | `references/supply-chain.md` |
| 5 | **Authentication / session** | Real auth library (not hand-rolled)? Tokens `HttpOnly`, short-lived? Password-reset/JWT TTL minutes not days? CSRF protection present? | `references/security.md` |
| 6 | **Injection (SQLi / command / XSS)** | Parameterized queries only (no string-built SQL)? Output rendered as text, never raw HTML (`Html.Raw`/`innerHTML`/`dangerouslySetInnerHTML`)? | `references/security.md` |
| 7 | **Misconfiguration / deploy** | CORS locked to known origins (not `*`)? Debug off, no stack traces to users? Security headers set? Internal tools behind auth? | `references/security.md` |
| 8 | **Reliability / atomicity / idempotency** | Multi-step writes (charge → save) wrapped in a transaction or idempotent? Payment handlers use idempotency keys + webhook confirmation? | `references/reliability.md` |
| 9 | **Cost / rate-limiting / abuse** | Rate limit on auth + LLM endpoints? Hard spend caps set? Per-user quotas? | `references/cost-ops-legal.md` |
| 10 | **Testing & QA gaps** | Real negative/adversarial tests (not AI testing its own assumptions)? SAST + dependency scan in CI? Did anything block-merge unread? | `references/reliability.md` |

Plus two cross-cutting checks that don't fit a single row: **PII/GDPR** (are you storing IDs/PII with public-read defaults or no consent layer? → `references/cost-ops-legal.md`) and **prompt injection into your own LLM features / coding agent** (untrusted content treated as instructions? → `references/agent-safety.md`).

## Fast triage — if you only have five minutes

These four cause the majority of documented real-world disasters. Check them first, always:

1. **Secrets exposed** — grep the repo and the client bundle for keys; check git history; confirm `.env` is gitignored. *(Drives the GitHub-secrets explosion + most "my bill exploded" stories.)*
2. **RLS / server-side authz off** — every table has RLS; every data fetch checks ownership. *(Lovable CVE-2025-48757, Moltbook 1.5M tokens, the IDOR-in-43%-of-repos finding.)*
3. **Agent can reach prod** — no AI agent holds a write connection to a production database; dev/prod are separate. *(Replit, PocketOS, the 1.9M-row wipe.)*
4. **Hallucinated dependencies** — every installed package is real and correctly named. *(Slopsquatting — `huggingface-cli` got 30k downloads as a hallucination.)*

## The non-negotiable framing

When you read AI-generated code, the failure mode is **automation bias** — research shows experienced developers get *more* trusting over a session, and AI states "tests pass" even when it fabricated them. So the rule is mechanical, not vibes-based:

> **AI code is an untrusted contribution until a human or a non-AI tool has verified it.** Run the tests in your own terminal. Run the scanner. Read the diff. The AI's confidence is not evidence.

This is why you (the human) are still accountable, still in demand, and still paid: when it breaks in production, "the AI wrote it" is not a defense anyone accepts.

## Reference index

- `references/security.md` — secrets, access control/RLS/IDOR, auth/session, injection, XSS, crypto, misconfiguration, file upload, error leakage. Maps each to OWASP / CWE.
- `references/reliability.md` — atomicity, idempotency, payments & webhooks, N+1 queries, transactions, retries, testing gaps, AI-fabricated tests.
- `references/agent-safety.md` — prod DB access, dev/prod separation, YOLO-mode/egress, excessive agency, prompt injection into agents, AI-IDE CVEs.
- `references/supply-chain.md` — slopsquatting, vulnerable pinned deps, verification workflow, lockfiles, SCA.
- `references/cost-ops-legal.md` — rate limiting, runaway LLM cost, observability, exposed internal tools, PII/GDPR.
- `references/incidents.md` — the cited catalog of real 2025–2026 incidents (Replit, Moltbook, Lovable, Tea, Amazon Kiro, slopsquatting) with sources, for when you need to show someone "this is real."
- `assets/secure-codegen-rules.md` — paste-in rules to make an AI coder safe-by-default (Prevent mode).
- `assets/pre-ship-checklist.md` — the hard pre-deploy gate (Pre-ship mode).
