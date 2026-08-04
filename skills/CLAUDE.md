# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is Karim's personal Claude Code skill library — the `~/.claude/skills/` directory Claude Code auto-loads at session start. It is **not** an app codebase. There is no build, no test runner, no package manifest. The unit of work is a single subdirectory containing a `SKILL.md` that Claude can invoke via the `Skill` tool.

Scale (as of init): **1051 skill folders + 12 symlinks** at root. Symlinks point at `~/.agents/skills/` (a sibling library that some skills are sourced from — keep the symlinks, do not copy their target contents in). Curated baseline is ~148 (per `~/.claude/skills-keep.txt`); the rest is opportunistic installs from upstream skill repos. Audit logs live in the memory vault — see *Memory & install logs* below.

There is no `README.md` and no git remote at this directory level (the parent `C:\Users\user\` is the git root). Treat this folder as a flat, editable corpus.

## Skill anatomy (what to write/edit)

Every skill folder MUST contain a `SKILL.md`. The hook `skill-quality-gate` enforces this at session start.

```
<skill-name>/
├── SKILL.md              # required: YAML frontmatter + body
├── README.md             # optional
├── scripts/              # optional Python/JS helpers the skill calls
├── references/           # optional supporting docs the skill links to
├── agents/, commands/, hooks/   # optional, used by full plugin-style skills
└── data/, assets/, expected_outputs/   # optional
```

`SKILL.md` frontmatter — minimum keys are `name` and `description`. Common optional keys seen across the corpus: `version`, `author`, `license`, `tags`, `compatible_tools`, `context`. Frontmatter names **must be unique across all installed skills** — duplicates break the skill loader. The auto-rename-on-collision rule lives in [feedback_skill_installs.md](C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory/feedback_skill_installs.md).

Description field is the primary trigger — it should state both what the skill does AND when to fire it. Be slightly pushy on triggers (Claude tends to under-invoke). See `skill-creator/SKILL.md` for the full authoring guide.

## Common operations

There is no test/lint/build. Operations are skill-management workflows:

| Task | How |
|---|---|
| Author or revise a skill | Invoke the `skill-creator` skill. It owns the draft → eval → iterate loop. |
| Audit an untrusted skill before install | Invoke `skill-security-auditor` BEFORE moving the folder into this directory. |
| Test a skill's triggering / output | Invoke `skill-tester`. |
| Find a skill matching a need | Invoke `find-skills`. |
| Bulk-install a skill repo | Use the workflow in [playbook_skill_repo_evaluation.md](C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory/playbook_skill_repo_evaluation.md): sandbox-clone first, security-audit, diff vs `~/.claude/skills-keep.txt`, graduate only real gaps. Never `/plugin marketplace add` blindly. Expected pick rate ~9% (aggregators) to ~25% (curated). |
| Prune / archive a skill | Move (don't delete) into `~/.claude/skills-archive/` and update the `MANIFEST-*.txt` restore command there. Pruning requires explicit confirmation per [feedback_skill_bloat_audit.md](C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory/feedback_skill_bloat_audit.md). |

## Sync — this directory is mirrored in real time to the VPS

`~/.claude/skills/` is one of three Syncthing folders kept bidirectionally live between this Windows machine and `vmi3164498` (37.60.243.30, accessible via `ssh vmi`). Any file you write here propagates to `/root/.claude/skills/` on the VPS within seconds, and vice versa.

Implications when editing:
- Don't write throwaway scratch files into this directory — they will replicate.
- A skill collision on either side breaks the loader on both. Resolve before saving.
- If a skill folder appears unexpectedly, check the VPS side before deleting — it may be the freshest copy.

Sync details and diagnostic commands: [reference_syncthing_realtime.md](C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory/reference_syncthing_realtime.md).

## Naming conventions (groups of skills to be aware of)

Several large families share a prefix and a source. Knowing the prefix prevents accidentally editing the wrong family:

- `antd-component-*` (~78) and `antd-*` — Ant Design component / migration / theme skills sourced from `ant-design/public/.well-known/agent-skills/`.
- `jdp-*` (~179) — Java Design Patterns library.
- `od-*` (~242), incl. `od-tpl-*` (~110) — "open design" templates and skills (nexu-io / open-design upstream).
- `design-md-*` (~71) — per-brand design-system specs (Apple, Linear, Stripe, Vercel, …). Each is a static reference card, not a tool.
- `refactor-ui-*` (~11) — Refactoring UI principles.
- `layers-*` (~9) — Jamie Mill product-thinking series.
- `bbg-*` (~15) — engineering "big book of …" knowledge packs.
- `frame-*`, `card-*`, `deck-*`, `tpl-*` — small templates used by visual-design skills.
- `vercel:*`, `figma:*`, `ai-plugins:*`, `claude-code-setup:*`, `agent-sdk-dev:*` — plugin-namespaced (loaded from Claude Code plugins, not from this folder).

When updating a family, update **all members** of that family rather than just the one you touched — they are designed to be consistent.

## Memory & install logs

The user keeps the system-of-record for this skill library in the memory vault, not in this directory. Before making non-trivial changes here, consult:

- `~/.claude/skills-keep.txt` — the explicit curated baseline list. The source of truth for "should this be installed."
- `~/.claude/skills-archive/MANIFEST-*.txt` — what was pruned and how to restore.
- `C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory/MEMORY.md` — index. Look for `reference_install_*` (one per install batch) and `playbook_skill_repo_evaluation.md`.

## Proactive skill use — MANDATORY for any task in this repo

This directory holds Karim's full skill arsenal. On **every** task — code, design, content, debug, planning, research, deploy, anything — scan the available-skills list and invoke every skill topically relevant to the request via the `Skill` tool **before** writing any answer. Default to **too many skills rather than too few**.

Concrete trigger map (non-exhaustive — apply by analogy):

| If the task involves… | Invoke skills matching… |
|---|---|
| Writing/reviewing code, refactors, bug fixes | `karpathy-coder`, `senior-backend`, `senior-frontend`, `senior-architect`, `senior-qa`, `code-reviewer`, `focused-fix`, `bughunter`, `diagnose`, `test-driven-development` |
| Frontend / web / landing / UI / app | `ui-ux-pro-max` (FIRST — locks the design system), then `frontend-design`, `impeccable`, plus aesthetic packs (`taste-skill`, `minimalist-skill`, `brutalist-skill`, `soft-skill`) and motion (`gsap*`, `motion-dev`) |
| Design system / colors / fonts / spacing | `color-expert`, `color-system`, `typography-scale`, `spacing-system`, `design-token`, `refactor-ui-*` |
| Content / copy / marketing / sales | `copywriting`, `cold-email`, `marketing-psychology`, `content-strategy`, `content-humanizer`, `brand`, `brand-guidelines`, `ad-creative` |
| Strategy / C-suite / planning | `ceo-advisor`, `cfo-advisor`, `cto-advisor`, `cmo-advisor`, `ciso-advisor`, `chief-of-staff`, `executive-mentor`, `senior-pm`, `senior-architect` |
| Regulatory / med-device / compliance | `fda-consultant-specialist`, `mdr-745-specialist`, `quality-manager-qms-iso13485`, `gdpr-dsgvo-expert`, `risk-management-specialist`, `regulatory-affairs-head` |
| Data / analytics / finance | `financial-analyst`, `data-visualization`, `data-report`, `campaign-analytics`, `product-analytics`, `business-investment-advisor` |
| Deck / slides / docs / pdf | `slides`, `presentation-deck`, `deck-*`, `pdf`, `pptx`, `docx`, `pptx-generator` |
| Video / motion / Higgsfield / Kling | `higgsfield-*`, `kling-motion-web-p`, `motion-dev`, `remotion`, `hyperframes`, `video-content-strategist` |
| Auth / payments / infra | `auth-implementation`, `stripe-sdk`, `senior-devops`, `docker-development`, `supabase-postgres-best-practices` |
| Skill management itself (rare) | `skill-creator`, `skill-tester`, `skill-security-auditor`, `find-skills` |

**Process skills first, implementation skills second.** `brainstorming` / `diagnose` / `executing-plans` / `karpathy-coder` shape *how* to approach; domain skills shape *what* to produce.

**Multi-skill fanout in parallel.** When a request spans domains, send a single message that invokes multiple Skill calls in parallel — do not serialize.

**No meta-commentary.** Never announce "I'm going to use skill X." Invoke silently, deliver the synthesized result.

## User-level conventions that apply here

Two things from `~/.claude/CLAUDE.md` (user-global) are easy to forget when working *inside* the skill folder, so they are restated:

- **Skill invocations are silent.** When applying skills to a task, do not announce which skills are being used. Deliver the synthesized result only. Exception: user explicitly asks.
- **`using-superpowers` + `karpathy-coder` first.** On any non-trivial turn, these two skills are invoked first (enforced by the Stop hook). Domain skills come after.

## What lives in `.claude/` here

The `.claude/` subfolder inside this directory is a VS Code workspace config, not Claude Code config:

- `launch.json` — VS Code launch targets for Karim's apps (`calaf-app/backend`, `calaf-app/frontend`, `calaf-app/mobile`, `my-video` Remotion, `xshack-assets` server). This directory is opened as a VS Code workspace because it sits at `~/.claude/skills/`; the launch configs point *outward* at the actual app projects. Don't add new launch targets unless asked.
- `settings.local.json` — Bash/MCP permission allow-list scoped to this workspace.

Claude Code's own settings live at `~/.claude/settings*.json`, not here.
