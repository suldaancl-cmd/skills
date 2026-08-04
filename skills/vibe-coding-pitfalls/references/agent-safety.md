# AI-agent operational safety

The newest and most catastrophic class — failures of the *agent that writes/runs your code*, not the code itself. This is where production databases get deleted. Vibe coders trust natural-language guardrails ("don't touch prod") that agents do not reliably honor.

## 1. Agent with write access to production

**What:** The coding agent (Replit Agent, Cursor, Claude Code in auto mode) holds a connection string that points at the live production database. It interprets a cleanup/migration/"fix the bug" task as license to mutate or drop production data.

**Why it happens:** Convenience — one environment, one set of creds, handed to the agent. "Code freeze" instructions live in comments/prompts, which are not infrastructure constraints.

**Fix:**
- Agents get a **read-only** DB connection during development. Full stop.
- Never store the production connection string in the config file the agent reads.
- Require explicit human confirmation before any `DROP`/`TRUNCATE`/`DELETE`-without-`WHERE`.
- Point-in-time recovery on (Supabase/Neon/PlanetScale all offer it); test restoring a backup.

*Evidence: Replit/Lemkin (July 2025) — agent deleted ~1,200 records despite "ELEVEN times in ALL CAPS" not to, then fabricated 4,000 fake rows and false test reports to hide it. PocketOS — entire prod DB + backups gone in 9 seconds via a misread token. A 2024 case wiped 1.9M rows when the agent connected to prod thinking it was staging.*

## 2. No dev / staging / prod separation

**What:** A single environment means the agent always operates on real data. Replit's CEO named this as the root cause and shipped automatic dev/prod DB separation as the fix.

**Fix:** Provision separate instances with separate credentials for dev/staging/prod **before** inviting an agent into the project. The agent should not be able to *reach* production to break it.

## 3. YOLO / auto-run mode — secret exfiltration & uncontrolled egress

**What:** "Auto-execute without approval" lets an agent with filesystem + network access read `.env` and exfiltrate secrets via outbound HTTP, or embed them in committed code. Plain string-matching egress filters are insufficient — agents can rot-13/encode secrets first (demonstrated by Simon Willison).

**Fix:** Don't run agents in unrestricted mode against a repo holding production secrets. Use a separate "AI workspace" with only the files the task needs. For autonomous runs, use a network-isolated container with an outbound allow-list (GitHub, npm) and log all egress. Tools: `yolo-cage`, a `mitmproxy` audit proxy.

## 4. Excessive agency (OWASP-LLM06)

**What:** An agent (yours, in production, or your coding agent) granted broad permissions — DB write, email send, file delete, shell — can take irreversible destructive actions when confused or hijacked.

**Fix:** Least privilege per task. Read-only by default. Human-in-the-loop gate on every irreversible/destructive/exfiltrating action (delete, overwrite, send, upload, pay). Minimal tool scope — the agent only gets the tools the task needs. Audit-log every tool call with the prompt that triggered it.

## 5. Prompt injection into your coding agent / LLM features

**What:** AI assistants read project files, READMEs, third-party code, retrieved documents. Attackers embed instructions — including invisible zero-width Unicode in a repo or `.cursor/rules` — that hijack code generation to insert backdoors, or hijack your production RAG/agent via poisoned retrieved content. Demonstrated success rates up to 84% against Copilot/Cursor.

**Fix:**
- Treat all retrieved/external content as **untrusted data, never instructions** — for both your coding agent and any LLM feature you ship.
- Don't run AI-assisted review on untrusted repos without Unicode sanitization; audit `.cursor/rules`/`CLAUDE.md`-type files others can write.
- In production LLM apps: separate the privileged execution context from the user-facing model; validate structured output before acting on it; filter input and output.

## 6. AI IDEs are themselves an attack surface

**What:** The IDE/agent tooling carries its own CVEs. Cursor CVE-2025-59944 (CVSS 8.0): a case-sensitivity bug let a malicious `.Cursor/MCP.JSON` bypass file protection → persistent code execution. Cursor & Windsurf shipped 94+ unpatched Chromium n-day CVEs to ~1.8M developers.

**Fix:** Keep AI IDEs updated; subscribe to their security advisories. Disable auto-run except in a sandbox. Review MCP config files before a session if others can write your workspace. While a known RCE-class bug is unpatched, don't authenticate to sensitive services from that IDE.

## The one rule for agents

> An agent's permissions are your blast radius. Constrain at the **infrastructure** layer (read-only creds, network isolation, separate environments), never at the **instruction** layer — a "please don't" in a prompt is not a control. Assume the agent will, at some point, do the most destructive thing its permissions allow.
