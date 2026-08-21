# 08 — UI Registry

> **Starts empty. Fills itself.** This is the file that stops components drifting across
> sessions — the single most useful of the nine.

## The rule, for the agent

Before building any UI component:

1. Read this file.
2. **If a similar component exists — reuse it, or match its exact classes and structure.**
3. If it does not exist — build it from `06-ui-tokens.md` + `07-ui-rules.md`, then **add it here**.

Never build a second component that does what one here already does. Never restyle an entry
without updating it here. A component in the codebase and missing from this file is a bug.

## Registry

| Component | Path | Purpose | Variants | Key classes / props |
|---|---|---|---|---|
| | | | | |

<!-- Appended as components are built. Keep one row per component, alphabetical. -->

## Patterns

Recurring compositions, not single components — the shapes that repeat across screens.

| Pattern | Where it appears | Rule |
|---|---|---|
| e.g. page header | every route | title left, one primary action right, `--s-8` below |
| | | |

## Known inconsistencies

Found during a sweep, not yet fixed. Empty is the goal.

| What | Where | Fix |
|---|---|---|

## Sweeping

Periodically read the component tree against this file and list what drifted — duplicated
components, one-off spacing, hard-coded colors, buttons that are almost but not quite a variant.
Produce a fix list; do not auto-fix. Karim decides what gets changed.
