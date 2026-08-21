# 02 — Architecture

## Stack

| Layer | Choice | Why this one |
|---|---|---|
| Framework | | |
| Language | | |
| Styling | | |
| Backend / DB | | |
| Auth | | |
| Storage | | |
| Payments | | |
| AI / model | | |
| Analytics | | |
| Hosting | | |

Versions that matter: <pin the ones where a major version changes the API — e.g. `Next.js 16`,
`Tailwind v4`, `Expo SDK 5x`. The agent will otherwise write last year's syntax.>

## Folder structure

```
<paste the real tree, two or three levels deep. Annotate anything non-obvious.>
```

## System boundaries — the rules that must never break

These are absolute. A violation is a bug even if the feature works.

- <e.g. API routes contain no UI logic>
- <e.g. Components contain no database logic>
- <e.g. Agent code in `agents/` never imports from `components/`>
- <e.g. Server actions never call agents directly>
- <e.g. Nothing outside `lib/db/` touches the client>

## Data flow

<Trace one request end to end: user action → what runs where → what comes back.
One paragraph or one diagram. This is what stops the agent inventing a second data path.>

## Database schema

```sql
-- or the ORM schema. Include the constraints and indexes, not just the columns —
-- the agent will add validation in app code if you hide the constraint here.
```

Row-level security / access rules: <who can read and write what>

## External services and their failure modes

| Service | Used for | What happens when it is down or rate-limited |
|---|---|---|
| | | |

## Secrets

Names only, never values. Values live in `.env.local` and are never read, printed, or committed.

- `<ENV_VAR_NAME>` — <what it unlocks>
