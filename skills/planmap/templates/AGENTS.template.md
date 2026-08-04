# {{PROJECT}} — agent instructions

Merge this into the workspace's existing `AGENTS.md`. Do not replace what is there.

`AGENTS.md` is the one instruction file every agent reads — Claude Code, Codex, Cowork,
Cursor, anything. `CLAUDE.md` holds a single import line pointing here, so the two never drift:

```markdown
Read and follow @AGENTS.md before anything else in this project.
```

## What this project is

One line, plus a pointer: the full plan is `PLANMAP.md`, the human setup list is
`MANUAL-SETUP.md`.

## Always

- Read `PLANMAP.md` section 11 and work the top unchecked box. One feature at a time.
- Match the existing code's style, naming and comment density.
- Merge edits into files; never replace a file wholesale.
- Point at the output that proves a change works before calling it done.

## Never

- Never build anything on the "Explicitly OUT of V1" list in `PLANMAP.md`.
- Never tick a box in section 11 that has not been tested on the real device or simulator,
  reviewed, and committed.
- Never invent a number, a price, a package version or a URL. Unverified means say `unverified`.
- Never put a secret in the repo, a commit message or a chat message. Names go in
  `.env.example` with empty values.
- Never run a destructive operation — dropping a table, deleting a bucket, force-pushing,
  changing DNS — without asking first.

## Conventions

| | |
|---|---|
| Package manager | |
| Formatter / linter | |
| Commit style | |
| Branch naming | |
| Where tests live | |
| How to run the app | |

## The stack, and what each piece owns

| Layer | Choice | Owns |
|---|---|---|

## Gotchas

The things that cost an hour the first time. Add to this list as you hit them; it is the most
valuable section in the file after a month.

- 
