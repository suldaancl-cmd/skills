---
name: project-context
description: "Scaffold and fill the nine context files (project overview, architecture, build plan, code standards, library docs, UI tokens, UI rules, UI registry, progress tracker) that a coding agent reads before it builds anything. Use this whenever Karim is planning a project, starting a new build, says 'plan this project', 'set up the project', 'context files', 'scaffold the project', 'what are we building', or opens a new _projects/<slug> folder — and also when an existing project keeps drifting between sessions, because that is the symptom these files cure. Run it before writing code, not after."
---

# Project Context

Nine files, written once, that stop the agent guessing. An agent with no context fills gaps
with its best guess, and guesses compound: by the third feature the codebase contradicts
itself and nobody can say exactly where it went wrong. These files close the nine gaps that
actually cause that.

Reading nine files costs far fewer tokens than generating code that gets thrown away. That is
the whole trade, and it is not close.

## What this skill does

1. Scaffolds `context/` into the project (never overwrites what is already there).
2. **Fills it from a conversation with Karim** — this is the part that matters. Copying blank
   templates is not the deliverable; a filled `01` and `02` is.
3. Leaves `06`/`07` blank until a design deck is approved, and `08`/`09` blank on purpose.

## Step 1 — Find the project folder

Every project lives in `_projects/<slug>/` (`C:\Users\user\.claude\_projects\`). If there is
no folder yet, create one before scaffolding. If Karim named an existing project, use that.

## Step 2 — Scaffold

```bash
python ~/.claude/skills/project-context/scripts/scaffold.py "<path to _projects/<slug>>"
```

It reports what it wrote and what it kept. **Existing files are never overwritten** — a
half-filled context file beats a fresh blank one. `--force <filename>` replaces one on purpose.

## Step 3 — Fill it, in this order

Work down the files. Do not ask nine questions in a row and do not ask about things you can
read — check the repo, the vault, and this conversation first, then ask only what is genuinely
undecided. Karim's time is the scarce input here, not yours.

| File | Fill from | Ask only when |
|---|---|---|
| `01-project-overview.md` | this conversation, the vault, the research note | the **out of scope** list is empty — that section is the whole anti-scope-creep mechanism and only he can draw the line |
| `02-architecture.md` | the existing repo if there is one; otherwise the stack he named | the stack is genuinely unpicked, or two options have real tradeoffs |
| `03-build-plan.md` | `01` — decompose it into phases and numbered features yourself, then show him | a feature's goal cannot be written as a checkable sentence |
| `04-code-standards.md` | the existing repo's actual conventions; otherwise sensible defaults for the stack | never — propose, let him correct |
| `05-library-docs.md` | one section per library, **only as each is first used** | never |
| `06-ui-tokens.md` | the approved deck option in `DESIGN.md` | **gated — do not fill before he picks a deck option** |
| `07-ui-rules.md` | same approved option | same gate |
| `08-ui-registry.md` | leave empty | never — it fills itself as components get built |
| `09-progress-tracker.md` | seed the checkboxes from `03`, all unchecked | never |

**The two gates are load bearing.** Filling `06`/`07` before the deck is approved means the
build proceeds against a direction Karim never chose, and every screen after that inherits it.
Filling `08` up front means inventing components nobody asked for.

## Step 4 — Wire it in

The project's `AGENTS.md` must tell both agents to read `context/` first, in order. If the
project used `_TEMPLATE/AGENTS.template.md`, that section is already there. If not, add it:

```
Read before any implementation, in this order:
01-project-overview → 02-architecture → 03-build-plan → 04-code-standards →
05-library-docs → 06-ui-tokens → 07-ui-rules → 08-ui-registry → 09-progress-tracker
```

## Step 5 — Report the gaps honestly

End by saying which files are filled, which are stubs, and which are deliberately blank.
A context file full of `<placeholders>` is worse than an absent one, because the agent reads
the placeholder as fact. Name every section still holding a placeholder.

## Keeping them alive

These are living files, not a one-time ceremony:

- After every feature: tick `09`, add any new component to `08`.
- After any decision: write it into the file that owns it, not into the chat.
- When the plan changes: log it in `03`'s deviation table rather than silently rewriting.
- A component in the codebase but missing from `08` is a bug. So is a decision that lives
  only in a conversation.

## What each file owns

Full descriptions are in `templates/README.md` — read it if you need the detail. In short:
`01` what and for whom · `02` how it is built · `03` what comes next · `04` how to write it ·
`05` how to use each library · `06` the exact values · `07` how the UI behaves ·
`08` what already exists · `09` where we stopped.

## Neighbours — do not duplicate them

- `planmap` / `ultraplan` — interview-driven blueprints for a project that has no shape yet.
  Run those **first** if the idea is still vague; this skill turns their output into files.
- `phased-plan` — slicing one feature into testable phases. That is `03` at finer grain.
- The installed `/scope`, `/audit`, `/architect`, `/develop`, `/sync` skills operate on the
  same idea with their own convention (`docs/scope/`, `docs/specs/`, `AGENTS.md`). Use whichever
  the project already uses. Do not run both conventions in one repo — two sources of truth is
  worse than either one alone.

## Standing rules that override anything here

`premium-design-laws` tokens beat any hex written into `06`. The default-fonts ban applies.
No UI code before the deck is picked. Done means pointing at the artifact that proves it.
