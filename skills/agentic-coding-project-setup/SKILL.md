---
name: agentic-coding-project-setup
description: Configure a software repository for reliable work by Codex, Claude Code, or another coding agent using scoped AGENTS.md instructions, verified commands, architecture boundaries, and task slicing. Use when starting, resetting, or stabilizing an AI-assisted coding project; not for ordinary one-file edits.
---

# Agentic coding project setup

Create a compact operating system for coding agents without turning repository instructions into a duplicated manual.

## Inspect before writing

- Find and read all applicable `AGENTS.md`, `CLAUDE.md`, skill files, package manifests, build configuration, CI workflows, and architecture documents.
- Determine instruction scope by directory. Preserve user-authored rules and unrelated repository changes.
- Run or inspect the actual scripts before documenting commands. Never invent a test, build, simulator, or deployment command.
- Record the framework and package versions from the repository. When behavior is version-sensitive, verify current primary documentation.

## Define the operating contract

Create or update only the smallest useful instruction files. Include:

- Product purpose and non-goals.
- Architecture map and source-of-truth systems.
- Directory ownership and generated-file boundaries.
- Commands for setup, typecheck, lint, tests, build, and targeted verification.
- Security invariants: secret locations, client/server boundary, authorization, destructive-action limits.
- UI invariants: design source, responsive behavior, RTL, accessibility, and platform-specific expectations.
- Data invariants: migrations, RLS, job state ownership, idempotency, and money handling.
- Definition of done and observable evidence required.

Keep temporary feature requirements in a task plan or issue, not permanent repository instructions.

## Plan work for an agent

- Start from the requested user outcome and inspect the relevant code path end-to-end.
- Divide work into vertical slices that can be verified independently.
- State assumptions and stop conditions. Ask only when a missing choice materially changes the result.
- For long tasks, maintain a short plan with one active step and update it when evidence changes.
- Use focused context: read the files and references needed for the current slice, not the whole repository by default.
- Never treat an AI agent as a microservice merely because it has a named role.

## Knowledge freshness

When the agent's remembered API may be stale, require it to:

1. Read installed types and local package code.
2. Check official documentation if local evidence is insufficient.
3. Pin decisions to the repository's installed version.
4. Note migrations or breaking changes instead of silently rewriting the stack.

## Deliverable

Use [references/agent-instructions-template.md](references/agent-instructions-template.md) as a menu, not a mandatory wall of text. Report:

- Files created or changed.
- Commands verified.
- Important boundaries encoded.
- Remaining unknowns or blocked checks.

Do not implement product features unless the user also requested them.
