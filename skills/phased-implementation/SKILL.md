---
name: phased-implementation
description: Execute a phased plan strictly one phase at a time, stopping for explicit human review and approval before moving to the next phase — never build multiple phases in one pass. Use this whenever you are implementing against a plan produced by phased-plan (or any multi-phase plan), when the user says "implement phase 1", "build this one phase at a time", "don't do it all at once", or when a teammate is shipping a feature that must stay reviewable. This is the guardrail that stops AI from writing 5,000 unreviewed lines in one go.
---

# Phased Implementation

Implement a plan **one phase at a time**, and **stop after each phase** until a human explicitly approves it. Then — and only then — commit or stage that phase and move on.

This exists because the failure mode is real and common: hand an AI a plan, it happily builds phases 1 through 8, you come back to a 5,000-line diff, and you cannot meaningfully review it. Small, gated increments keep a human genuinely in the loop.

## The loop

1. **Read the plan.** Find the plan file (usually `plans/<feature>.md`). Identify the current phase — the first one not yet approved.
2. **Build exactly that one phase.** Nothing from later phases, even if it's tempting or "would only take a second." Staying inside the phase boundary is the whole point.
3. **Prove it.** State the plan's user-testable outcome for this phase and show that it's met — the command to run, the screen to open, the test that passes, the output. Don't say "done"; point to the thing that proves it. If you couldn't verify it, say so plainly.
4. **Stop and ask.** Explicitly ask the human to review this phase and approve it. Do not proceed.
5. **On approval:** commit or stage this phase's changes (a small, self-contained commit — one phase per commit / PR), then return to step 1 for the next phase.
6. **On changes requested:** fix within the current phase, re-prove, ask again. Still don't advance.

## Hard rules (and why)

- **One phase per pass. Never combine phases into a single implementation or PR.** Combining is exactly the 5,000-line problem this skill prevents. If two phases feel too small to separate, that's a signal to fix the *plan*, not to merge them here.
- **Do not commit or merge without approval.** The stop-and-review gate is the safety mechanism; auto-advancing removes it.
- **If mid-phase you discover the plan is wrong** (a phase is bigger than it looked, or the ordering doesn't work), stop and say so rather than silently expanding scope. A quick plan revision beats a phase that quietly balloons.

## Handing back

When all phases are approved, summarize what shipped and confirm the feature matches the plan's Goal. If any phase surfaced an architectural or data-model question the plan flagged for review, make sure it was actually answered — don't let it slip through unresolved.
