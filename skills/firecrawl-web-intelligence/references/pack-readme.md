# Firecrawl Agentic Skill Pack

Portable web-intelligence policy for:
- Claude Code
- Codex
- Hermes / LangGraph agents

## Files

- `SKILL.md` — canonical routing, cost, evidence, security, caching and ingestion rules
- `claude/CLAUDE.md` — Claude Code adapter
- `codex/AGENTS.md` — Codex adapter
- `hermes/LANGGRAPH.md` — Hermes/LangGraph adapter
- `config/firecrawl-policy.json` — default budgets and routing limits

## Install conceptually

Keep `SKILL.md` as the source of truth.
Platform adapters should reference it instead of duplicating logic.

For a production agent platform, implement the router as code/graph policy, not only as a prompt.
