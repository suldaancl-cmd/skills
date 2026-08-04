---
name: phased-plan
description: Break a feature or build into small, sequential phases where each phase is an independently user-testable vertical slice sized for a small PR review. Use this whenever the user asks to plan, spec, or scope a non-trivial feature, says "make a plan", "phase this", "break this down", or is about to start a multi-step build — especially before writing any code for a feature that will span more than one commit. Pairs with grill-me (run first to nail requirements) and phased-implementation (runs the plan one phase at a time).
---

# Phased Plan

Turn a feature request into a plan broken into **small, sequential phases**, where each phase is a slice a human can actually test and review. This exists because giant all-at-once plans produce 2,000-line PRs that nobody reviews properly — and an unreviewed AI diff is where bugs ship.

## When to use

Use for any feature that will take more than a single commit. For a tiny bug fix, skip this (or just run `grill-me`) — a plan would be ceremony.

Run **after** `grill-me` has resolved the open requirements questions. Garbage requirements in, garbage plan out.

## What makes a good phase

Each phase must be a **vertical slice**, not a horizontal layer. The test: *can the user open the app and see/try something new after this phase?*

- Good phase: "User can tap a Save button and the note persists locally" — touches UI + storage, testable by hand.
- Bad phase: "Build the entire data layer" — all backend, nothing to test, invites a 1,000-line unreviewable dump.

Size each phase so its PR is small enough to review carefully — aim for roughly **under ~300 changed lines**. If a phase is bigger, split it.

Order phases so each builds on the last and the app stays runnable at every step. Phase 1 should be the thinnest thing that proves the shape is right (often a walking skeleton), not the foundation for everything.

## Output format

Write the plan to `plans/<feature-slug>.md` (create the `plans/` dir if absent — it's a useful durable record and reviewable in a PR). Use this structure:

```markdown
# Plan: <Feature name>

## Goal
<One paragraph: what the user can do when this is done, and why.>

## Non-goals
<What this explicitly does NOT cover, so scope doesn't creep.>

## Phases

### Phase 1 — <short title>
- **User-testable outcome:** <what a human can try after this phase>
- **Touches:** <files / modules, roughly>
- **How to test:** <the concrete manual check>

### Phase 2 — <short title>
...

## Open questions for review
<Architectural / data-model / irreversible decisions you are NOT deciding
alone. Leave these for the human to answer. See "Team mode" below.>
```

## Team mode

If a less-technical teammate is driving (or the `mobile-app` / vibecode parent invoked this), do **not** silently guess on anything architectural — schema/migrations, auth model, third-party service choice, anything hard to reverse. Write those into **Open questions for review** and leave them unanswered, then let the human (the technical owner) answer them via `grill-me` before implementation starts. Deciding these silently is how AI plans go wrong in ways that are expensive to unwind.

## Handoff

End by telling the user the plan is written and offering to start `phased-implementation` on Phase 1 — which will build exactly one phase and stop for their review before continuing.
