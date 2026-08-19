---
name: planmap
description: Blueprint a whole project before any code exists. Interviews you in batches of multiple-choice questions until nothing material is unknown, then writes PLANMAP.md — sitemap, backend schema, AI gateway and model layer, integrations table, checkbox task list — plus MANUAL-SETUP.md, the counted list of accounts, API keys and human-only steps no AI can do for you. Pulls UI references from Mobbin, renders the map as FigJam diagrams, exports to Google Docs, and scaffolds the workspace with AGENTS.md as the instruction file. Invoke when Karim says "planmap", "map this project", "plan the build", "sitemap for X", "blueprint", "خريطة المشروع", or before starting any new product.
---

# planmap

Turns an idea into a build map plus an honest list of what Karim must do with his own hands.

Runs in Claude Code, Cowork, claude.ai (upload the folder as a skill), and Codex/ChatGPT via
`portable/PROMPT.md` in the plugin.

## Where the method comes from

The interview loop, the parallel tools setup, the checkbox plan file and the AGENTS.md
convention are lifted from Codesistency, *How to Build Real Mobile Apps with Claude — FULL
COURSE* (2026-07-31, chapter 1 at `08:41`), which documents a workflow that shipped an app to
the App Store in 14 days. His framing, verbatim from the transcript: the prompt exists so the
AI *"never guesses anything but instead asks us everything, right, so we are on the same page."*
Everything else here is Karim's own stack and rules.

## Read this first — Karim's rules

`references/karim-rules.md` is binding on every phase below. Eight rules: plan every angle ·
create `.env.local` and hand it over · count the manual steps · state the risks before he
commits · give choices in Arabic · plain language on first use of any term · verified tutorial
links only · read the vault playbook first.

It ends in a handover checklist. A plan that fails one of those boxes is not done, however good
the map looks.

## The seven phases

Do them in order. Phase 1 is the one that makes the difference — skipping it produces a plan
built on guesses, which is the failure mode this skill exists to kill.

## Phase 0 — scaffold

```bash
python C:/Users/user/.claude/skills/planmap/scripts/planmap_scaffold.py --project "<name>" --prompt "<his exact ask>"
```

Reuses `~/.claude/scripts/topic_workspace.py` — never reimplement the folder set. Never
overwrites. Then read `BRAIN.md` and `SKILLS.md` in the new folder before planning anything.
The second brain outranks general knowledge; when they disagree, say so in `NOTES.md`.

## Phase 1 — interview until nothing material is unknown

**Never guess. Ask.** Use `references/interview-questions.md` as the question bank.

Rules of the interview:

- **Batches of 3 to 6 questions, grouped by one topic per batch.** Not one at a time, not
  twenty at once. Use AskUserQuestion so he clicks instead of typing.
- **Every question is multiple choice** with concrete options, and exactly one marked
  `(recommended)` with a half-line reason. He overrides with free text whenever he wants.
- **Every question and option is written in Arabic as well as English** (rule 5), and any
  technical term gets a one-sentence plain-language definition the first time it appears
  (rule 6). A question he cannot fully read is a question he cannot answer.
- **Keep going in batches** until no material unknown is left. Six to ten batches is normal.
  Do not shortcut to the plan because the picture feels clear — feeling clear is the bug.
- **Two questions are mandatory** and are the ones people skip:
  - *What does "V1 is done" mean for you?* — the answer defines the scope boundary.
  - *What is explicitly OUT of V1?* — write the excluded list into `PLANMAP.md` verbatim.
- **Say when you disagree with his answer.** If he picks something that will hurt him later,
  say so in one line and build what he picked anyway. His call, stated risk.

Batch order: idea and money → users → screens and the order they come in → data model → AI
behaviour and what happens when it fails → stack → V1 boundary → done-definition.

## Phase 2 — tools setup, running in parallel

The best trick in the source video: while the AI drafts the next question batch, the human is
creating accounts and copying keys. Do not save the setup list for the end.

So the moment the stack is decided (usually batch 5), write the first cut of
`MANUAL-SETUP.md` and hand it to Karim mid-interview. He works down it while you keep asking.
It gets finalised with real counts in phase 5.

**Write the env files in the same breath** (rule 2) — `.env.example` committed with every
variable name and a where-to-get-it comment, `.env.local` empty and added to `.gitignore`
*before* the first commit. Tell him the full path, how many values it needs, and which ones
block the first deploy. Never ask him to paste a secret into the chat; the file is the channel.
Mark every `EXPO_PUBLIC_` / `NEXT_PUBLIC_` / `VITE_` line as publicly visible on the line
itself — a secret behind a public prefix is a leak, not a config.

## Phase 3 — write PLANMAP.md

Fill every section of `templates/PLANMAP.template.md` from the interview answers. Rules:

- **Sitemap is exhaustive.** Every route and screen, marked `public` / `auth` / `admin`, and
  the order the user meets them in — onboarding before auth, or auth before onboarding, is a
  decision, not a detail.
- **Backend map names tables, RLS policies, functions, jobs, buckets.** Long-running work goes
  to the job runner, never an edge function.
- **AI layer names a model per role**, cheap default and expensive escalation, with the failure
  path: retry, fall back, or ask the user to redo the input.
- **Integrations table carries the env-var name for every service.** It is the input to phase 5.
- **Section 11 is a checkbox task list**, one line per feature. This is the file the build loop
  ticks through.
- **Every angle from rule 1 has a row** — first launch, offline, payment failure, refund, AI
  failure, account deletion, permissions per table, free vs paid, secret storage, vendor
  disappearing. Undecided is written `TBD — needs decision: <the exact question>`, never
  omitted. A plan covering the happy path only is a demo script.
- No invented numbers. Unverified means write `unverified`.

## Phase 4 — references and diagrams

**Mobbin** — for each of the 5 to 8 screens that carry the product, call
`mcp__818ad881-...__search_screens` (ToolSearch by name first if the schema is not loaded).
Save each to `refs/mobbin/`: screen name, `mobbin_url`, one sentence on what to steal. A
reference without its link is worthless later.

**Figma** — two FigJam boards via `mcp__9f8892a0-...__generate_diagram`, Mermaid
`flowchart LR`, every label quoted:

1. Sitemap — routes grouped public / auth / admin.
2. System map — client, functions, database, AI gateway, job runner, third parties.

If the Figma MCP is not connected, write the Mermaid to `figma/sitemap.mmd` and say so. Never
fake a link.

## Phase 5 — MANUAL-SETUP.md, finalised with real counts

Fill `templates/MANUAL-SETUP.template.md` from the integrations table, using
`references/manual-vs-ai.md` as the checklist of what no AI can do. Opens with real counts:

```
Accounts to create:             N
API keys / secrets to generate: N
Human-only steps:               N
Blocking before first deploy:   N
Your hands-on time:             ~N minutes (+ N days waiting on someone else)
```

Split into blocking now / later / waiting-on-someone-else. Every row: what, where, which env
var, does it block, how long.

**Open the file with the risks section** (rule 4), answering four questions plainly: what can go
wrong · what it costs monthly at zero users and at working scale · what he is locking himself
into and the exit cost · what is irreversible. Lead with a recommendation, not a menu — he asked
to be guided, so "I'd do X because Y" comes before the alternatives.

**Attach a tutorial to every hands-on row** (rule 7) — but only links verified in this session
or already in the vault. No verified link means write the exact search phrase and label it
`unverified`. Check `index_video_lessons.md` first; a note he already owns beats a stranger's
video. A fabricated URL is worse than none.

Then append the **launch gate** from `references/build-loop.md` — the store-rejection list.
Privacy policy, terms, delete-account, Apple Sign-In whenever Google Sign-In is present. Those
are not polish; they are rejections.

## Phase 6 — set up the instruction files

`AGENTS.md` holds the project's real instructions; `CLAUDE.md` is one line that imports it.
Same convention as Karim's global setup, and the same one the source video uses — one file
that every agent reads, not two that drift.

`topic_workspace.py` already writes both. Merge the project's conventions into `AGENTS.md`
from `templates/AGENTS.template.md`; do not replace what is there.

## Phase 7 — export and hand over

1. `PLANMAP.md` to Google Docs via `mcp__727e7965-...__create_file`: `textContent` = the
   markdown, `contentMimeType` = `text/plain` (which auto-converts; `text/html` does not),
   title `PLANMAP — <project>`. Report the link.
2. Append the decisions to `NOTES.md` with today's date.
3. Hand him the build loop in `references/build-loop.md` as the next action.

## Verification gate

Point at proof before saying done:

- workspace path with `ls` output
- how many interview batches ran and that both mandatory questions were answered
- the Figma URL, or the `.mmd` fallback and the reason
- the Google Doc link
- the counts in `MANUAL-SETUP.md`, matching the integrations table row count
- **the `.env.example` / `.env.local` paths, the variable count, and proof `.env.local` is
  gitignored** (`git check-ignore .env.local` — if it prints the path, it is ignored)
- **the eight-box handover checklist at the end of `references/karim-rules.md`**, each box
  ticked or named as failed

Anything missing gets named and labelled `unverified` or `blocked`, never skipped quietly.

## Output to Karim

Bilingual: English, then Arabic RTL. Lead with the counts and the links. No phase narration.

Plain language throughout (rule 6) — every technical term gets a one-sentence definition the
first time it appears. Then, in this order: **the risks**, **what he must do with his own hands
and roughly how long**, **the `.env.local` path and how many values it needs**, and **what to
watch first** if there is a verified tutorial.
