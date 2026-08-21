# MANUAL SETUP — {{PROJECT}}

Slug `{{SLUG}}` · drafted {{DATE}}

Everything on this page needs Karim's own hands, card, phone or signature. No AI agent —
Claude Code, Codex, Cowork, ChatGPT — can do any of it, and no amount of prompting changes
that. Rows come one-for-one from the integrations table in `PLANMAP.md`.

## Before you start — read this part

Plain language, no jargon. Every technical word gets explained the first time it shows up.

### What can go wrong

Ranked by how likely it actually is, not by how scary it sounds.

| # | What could go wrong | How likely | What it would cost you | How we reduce it |
|---|---|---|---|---|
| 1 | | | | |

### What this costs to run

| When | Monthly cost | What drives it |
|---|---|---|
| Zero users (today) | | |
| When it starts working (~N users) | | |

Every figure carries the assumption it rests on. A number without its assumption is a guess —
write `unverified` instead of guessing.

### What you are locking yourself into

Decisions that are expensive or impossible to reverse later. Name the exit cost for each.

| Decision | Reversible? | What it costs to change later |
|---|---|---|

### What is irreversible

These get a stop-and-confirm gate during the build. Nothing on this list happens without you
saying yes first.

- e.g. publishing the bundle ID · destructive migration · DNS cutover · deleting a bucket

### My recommendation

One paragraph. What I would do and why, before the alternatives. Not a neutral menu — you asked
to be guided.

## Counts

```
Accounts to create:            N
API keys / secrets to generate: N
Human-only steps:              N
Blocking before first deploy:  N
Your hands-on time:            ~N minutes  (+ N days of waiting on someone else)
```

Fill these from the tables below. If the numbers do not match the row counts, the plan is
wrong, not the count.

## Blocking — do these before the first deploy

| # | What | Where | Lands in | Time | Why it blocks |
|---|---|---|---|---|---|
| 1 | | | `ENV_VAR` | | |

## Later — do these before launch, not before the first deploy

| # | What | Where | Lands in | Time | Needed by |
|---|---|---|---|---|---|

## Waiting on someone else

The ones that take days and cannot be rushed. Start them first even though they block last.

| # | What | Typical wait | Start by |
|---|---|---|---|

## What an AI can do once you have handed over the keys

Listed so the split is unambiguous — this is where the agents take over again.

- Write and run the migrations, functions, tests and CI
- Wire the SDKs and webhook handlers against the keys you pasted
- Deploy to an already-connected project and read back the logs
- Draft the store listing copy, screenshots and privacy answers for you to submit

## Where the keys go

Never in a chat message, never committed. One `.env.local` for local, the platform's own
secret store for production. The repo's `.env.example` lists the names with empty values so
the agent knows what to expect without ever seeing a value.

**Your file is here:**

```
{{PROJECT_PATH}}/.env.local        ← paste your values here. N values needed, N of them blocking.
{{PROJECT_PATH}}/.env.example      ← committed. Names only, never values.
```

`.env.local` is in `.gitignore` — verify with `git check-ignore .env.local`; if it prints the
path back, you are safe. If it prints nothing, **stop and fix that before the first commit.**

A variable starting `EXPO_PUBLIC_` / `NEXT_PUBLIC_` / `VITE_` ships inside the app and **anyone
can read it**. That is fine for a public key, and a leak for a secret one. The `Public?` column
below says which is which.

| Env var | Service | Public? | Where to get it | Blocks deploy? | Production store |
|---|---|---|---|---|---|

## Watch this first

Short walkthroughs for the steps above. Links here are **verified only** — if a row says
`unverified`, that is a search phrase to type, not a link that exists.

| Step | Watch / read | Length | Verified? |
|---|---|---|---|

Check the vault before searching outward — `index_video_lessons.md` and the `playbook_*` notes
may already hold the walkthrough, and a note you already own beats a stranger's video.
