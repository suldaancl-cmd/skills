# context/ — the nine files the agent reads before it builds

Adapted from the JavaScript Mastery workflow ([[reference_jsmastery_agentic_workflow]]).
The idea it gets right: **the agent guesses whenever you leave a gap, and guesses compound.**
Nine files close the nine gaps. Written once, they travel with the project for its whole life.

Copy this folder into any new `_projects/<slug>/`. Fill what you know, leave the rest —
files 08 and 09 are *supposed* to start empty and fill themselves.

## Read order (this order is load bearing)

| # | File | Closes the gap about |
|---|---|---|
| 01 | `01-project-overview.md` | what we're building, for whom, and **what we are not** |
| 02 | `02-architecture.md` | stack, folders, boundaries, and the rules that must never break |
| 03 | `03-build-plan.md` | what comes next, so the agent never picks |
| 04 | `04-code-standards.md` | how we write it |
| 05 | `05-library-docs.md` | how *this project* uses each library, and which MCP to check first |
| 06 | `06-ui-tokens.md` | the exact colors, spacing, radii, type steps |
| 07 | `07-ui-rules.md` | how the UI behaves — the design system in prose |
| 08 | `08-ui-registry.md` | which components already exist (**starts empty, fills itself**) |
| 09 | `09-progress-tracker.md` | where we stopped (**starts empty, fills itself**) |

Also keep `context/designs/` beside these — one visual reference per screen. The agent
matches a reference instead of inventing a layout.

## How this fits the rest of the template

These files do **not** replace anything already in `_TEMPLATE/`:

- `CLAUDE.md` stays the app identity + store-policy contract.
- `AGENTS.md` stays the two-agent roster (opus architects, sonnet builds).
- `ADVISE.md` stays the phase gates. `03-build-plan.md` is the feature-level detail *inside* those phases.
- `DESIGN.md` stays the 3-option deck Karim picks from. **`06` and `07` are written after he picks** — they are the chosen option, made machine-readable. Do not fill 06/07 before the deck is approved.

## The installed skills that maintain them

Nine skills from `JavaScript-Mastery-Pro/skills` are installed in `~/.claude/skills/`:

| Skill | Touches |
|---|---|
| `/scope` | 01, 03 |
| `/audit` | bootstraps 01, 02, 04, 05 from a real repo |
| `/architect` | writes a spec before a load-bearing decision gets guessed |
| `/develop` | builds from the spec, advances 09 |
| `/check verify` \| `/check review` | proves it against the spec, then reviews on a fresh model |
| `/test` | test suite for the change |
| `/document` | PR body, changelog, release note, postmortem |
| `/sync` | reconciles 02/03/09 with what the repo actually shows |
| `/debug` | root-cause loop, hands a regression test to `/test` |

They write to `docs/scope/`, `docs/specs/`, `docs/reviews/`. That is their convention, not ours —
if a project already uses `_checkpoints/` per `AGENTS.md`, keep `_checkpoints/` and tell the skill.

## Standing rules that override anything here

`premium-design-laws` tokens beat any hex you invent in `06`. The default-fonts ban applies.
No UI code before the colors+fonts deck is picked. G4 still binds: done means pointing at the
artifact that proves it.
