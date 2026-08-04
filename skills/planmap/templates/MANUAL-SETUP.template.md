# MANUAL SETUP — {{PROJECT}}

Slug `{{SLUG}}` · drafted {{DATE}}

Everything on this page needs Karim's own hands, card, phone or signature. No AI agent —
Claude Code, Codex, Cowork, ChatGPT — can do any of it, and no amount of prompting changes
that. Rows come one-for-one from the integrations table in `PLANMAP.md`.

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

| Env var | Service | Local | Production store |
|---|---|---|---|
