# User Preferences

## Skill usage — be proactive

The user has ~350 skills installed across `~/.claude/skills/`, plugin-namespaced skills, and standalone tools. They want every skill to pull its weight.

**Rule:** Before doing any task, scan the available skills list for anything topically relevant, and invoke matching skills via the Skill tool rather than answering from general knowledge alone. Prefer to **use too many skills than too few** — the user has explicitly asked for this.

Concretely:
- Any marketing/content task → check `marketing:*`, `marketing-*`, `cold-email`, `copywriting`, `content-*`, `brand-voice:*`, etc.
- Any engineering task → check `engineering:*`, `senior-*`, `code-reviewer`, `tdd-guide`, `focused-fix`, etc.
- Any sales task → check `sales:*`, `apollo:*`, `common-room:*`, `cold-email`.
- Any design/UI task → check `design:*`, `design-taste-frontend`, `frontend-design`, `ui-design-system`, `minimalist-ui`, `high-end-visual-design`, `apple-hig-expert`, etc.
- Any data/analytics task → check `data:*`, `statistical-analyst`, `financial-analyst`, `analytics-tracking`.
- Any C-suite / strategy task → check `c-level-advisor`, `cfo-advisor`, `ceo-advisor`, `coo-advisor`, `chief-of-staff`, `executive-mentor`, `board-meeting`, etc.
- Any regulatory / healthtech / QMS task → check `ra-qm-team`, `fda-consultant-specialist`, `mdr-745-specialist`, `qms-audit-expert`, `iso*`, `gdpr-dsgvo-expert`.
- Any medical / bio task → check `bio-research:*`, the ClinicalTrials / bioRxiv / ChEMBL MCP tools.

**Don't just acknowledge skills exist — invoke them.** If a skill is named `cto-advisor` and the user is asking a CTO-level question, call it. If they ask for a marketing campaign, call `marketing:campaign-plan`. If they ask for UX copy, call `design:ux-copy`.

**Multi-skill tasks:** When a request spans domains (e.g. "launch a product"), invoke multiple relevant skills in parallel and synthesize results rather than picking just one.

**Fully automatic — no announcement.** Do NOT say "I'm going to use skills X, Y, Z" before acting. Just invoke the relevant skills silently and deliver the synthesized answer. The user does not want meta-commentary about which skills are being used — only the final result. Exception: if the user explicitly asks which skills you used, then list them.

## Infra the user owns

- **Server vmi3164498** (37.60.243.30) — Ubuntu 24.04 KVM VPS, root access via `ssh vmi` (key auth configured). Runs Docker + social-media automation scripts. ~350 skills + 4 Claude Code plugins mirrored from local.
- Local skills live in `C:\Users\user\.claude\skills\` (~347) plus plugin-namespaced skills injected at session start.
- Memory index: `C:\Users\user\.claude\projects\C--Users-user--claude-skills\memory\MEMORY.md`.
