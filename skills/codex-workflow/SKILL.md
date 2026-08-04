---
name: codex-workflow
description: Use this when you want Codex to work through a task with disciplined engineering flow: clarify the goal, inspect the local context, make minimal changes, verify the result, and summarize clearly.
---

# Codex Workflow

This workflow captures the default operating style for Codex in a shared local workspace.

## Core Principles

1. Inspect before acting.
   Read the relevant files, commands, docs, or current state before making claims or edits.

2. State assumptions.
   If the task has multiple plausible meanings, name the assumption being used. Ask only when guessing would be risky.

3. Keep changes surgical.
   Touch only the files needed for the request. Match the existing style. Avoid unrelated refactors.

4. Prefer simple solutions.
   Do the smallest thing that fully satisfies the goal. Add abstractions only when they clearly reduce real complexity.

5. Verify the outcome.
   Run the narrowest meaningful checks first, then broader checks when the blast radius warrants it.

6. Protect user work.
   Do not revert or overwrite unrelated changes. Treat unrecognized local edits as user-owned.

7. Report what matters.
   Summarize the change, verification, and any remaining risk without flooding the user with logs.

## Default Loop

Use this loop for coding, debugging, refactoring, local setup, and repository maintenance.

1. Define the goal.
   Convert the request into a concrete success condition.

2. Gather context.
   Use fast search first, usually `rg` or `rg --files`. Read only the files needed to understand the surface area.

3. Choose the smallest plan.
   Prefer existing project patterns and local helpers over new frameworks or broad rewrites.

4. Edit carefully.
   Use targeted patches for manual edits. Keep comments rare and useful.

5. Verify.
   Run formatters, tests, type checks, builds, or browser checks that are relevant to the changed behavior.

6. Iterate if needed.
   If verification fails, diagnose from the failure and make the next smallest correction.

7. Close cleanly.
   Tell the user what changed, where, what was verified, and what could not be verified.

## Frontend Addendum

For UI work, the goal is not merely "it compiles." The result should feel usable and intentional.

- Build the actual app or tool, not a landing page, unless the request asks for one.
- Reuse the existing design system and interaction patterns.
- Use responsive constraints so text and controls do not overlap or jump.
- Prefer real product, place, or brand assets when they matter.
- Verify significant frontend changes in a browser when a local target is available.

## Safety Rules

- Never run destructive git or filesystem commands unless the user explicitly asked for them.
- Request approval for network installs, external writes, GUI launches, or sandbox-escalated commands.
- Do not expose secrets. If secrets appear in logs, stop quoting them and summarize safely.
- For current facts, prices, laws, APIs, releases, or schedules, verify with an authoritative source.

## Final Response Shape

Keep the final response short and useful:

- What changed.
- Where it changed.
- What verification ran.
- Any caveats or next logical action.

Avoid dumping command output unless the user specifically asked for it.
