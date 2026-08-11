# 04 — Code Standards

> Write every convention down once. This is what stops the agent drifting into its own
> style by week two.

## Language rules

- **TypeScript:** strict on. No `any` — use `unknown` and narrow. Types over interfaces unless extending.
- **Exports:** <named vs default — pick one and say it>
- **Async:** <async/await only, no raw `.then` chains>
- **Nulls:** <how absence is represented — `null`, `undefined`, or a Result type>

## Naming

| Thing | Convention | Example |
|---|---|---|
| Files | | |
| Folders | | |
| Components | `PascalCase` | `JobCard.tsx` |
| Hooks | `useThing` | `useJobFilters.ts` |
| Server actions | verb-first | `createProfile` |
| Types | `PascalCase`, no `I` prefix | `JobListing` |
| Constants | `SCREAMING_SNAKE` | `MAX_RESULTS` |
| Booleans | `is` / `has` / `can` prefix | `isLoading` |

## Framework conventions

<Pin the version-specific ones. e.g. for Next.js: server components by default, `"use client"`
only at the leaf that needs it; route handlers in `app/api/*/route.ts`; `params` is a Promise.>

## Component structure

Order inside a component file: imports → types → constants → component → subcomponents → helpers.
One exported component per file. A component past ~150 lines gets split.

## Error handling

- Where errors are caught: <boundary/layer>
- What the user sees: <never a raw error string>
- What gets logged and where: <>
- Never swallow an error silently. Never `catch {}`.

## Server actions / API

- Validate every input at the boundary (<zod / valibot / manual>) — never trust the client.
- Return shape: <a consistent `{ data, error }` or thrown errors — pick one>
- No business logic in the route handler; it calls into `lib/`.

## Comments

Explain *why*, never *what*. No section-banner comments, no ASCII dividers, no `// ---- setup ----`.
A comment that restates the code gets deleted.

## Tests

<Framework, where they live, what must have one. "Every money path and every parser" is a
reasonable floor; not every function needs a test.>

## Commits

<Conventional commits or plain — pick one.> One logical change per commit.

## Never do

- Hard-code a hex value, spacing value, or font family — they live in `06-ui-tokens.md`.
- Add a dependency for something twenty lines of stdlib would do.
- Build an abstraction with one implementation.
- Leave commented-out code in a commit.
