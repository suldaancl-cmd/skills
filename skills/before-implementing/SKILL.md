---
name: before-implementing
description: Use BEFORE writing any non-trivial code — new modules, schema changes, refactors, and anything touching auth, money, migrations, or deletion. Enforces a research-then-propose contract: investigate the repo first, then produce Goal / Blocking questions (0-3, each with a recommended default) / numbered falsifiable Assumptions / Plan, then STOP and wait for approval. Invoke whenever the user says "implement", "build", "add this feature", "refactor", "write the code", "make a plan first", "don't start yet", or when a request is ambiguous enough that a wrong assumption would mean throwing work away rather than adjusting it. Also use when the user complains that you started coding too early or guessed at requirements.
version: 1.0.0
author: Karim
license: MIT
tags: [planning, discipline, assumptions, pre-implementation, scope-control, code]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# Before implementing

Work like a contractor who bills for rework: the cost of a wrong assumption is yours to avoid, and the cost of an unnecessary question is mine to pay.

## 1. Investigate before you ask

Read the relevant code, tests, configs, and dependency manifests first. Anything discoverable in under a minute of searching is not a question — it's research you owe me. Never ask about test framework, language version, lint rules, error handling conventions, directory layout, or existing abstractions that already exist in the repo. If the codebase contradicts itself, that's worth raising.

## 2. Then produce this, and stop

**Goal.** One paragraph restating what I asked for in your own words, including the acceptance criteria you'll hold yourself to. If your restatement is wrong, that's the cheapest possible place to find out.

**Blocking questions (0-3).** Only ask when a wrong answer means throwing work away, not adjusting it. Each question gets your recommended default so I can reply "yes to all" — never ask an open question where a proposed answer would do. If nothing is genuinely blocking, say so and list zero.

**Assumptions.** Numbered, specific, falsifiable. "Inputs are under 10k rows and fit in memory" is an assumption. "The code should be maintainable" is not. Cover whichever of these the task actually touches:

- Data: shape, volume, trust level, encoding, what a malformed input looks like
- Failure: what should happen on timeout, partial write, or downstream 500 — retry, fail loud, or degrade
- Boundaries: who calls this, what's public API vs. internal, backwards-compat obligations
- State: concurrency, idempotency, transactionality, ordering guarantees
- Environment: runtime version, where it deploys, what it's allowed to reach
- Scope: what you're deliberately *not* doing, and what you're leaving as TODO
- Testing: what you'll write tests for and what you'll leave uncovered

**Plan.** Files you'll create or modify, the key function/type signatures, and the order you'll work in. Where you chose between real alternatives, name the alternative and say why you rejected it in one clause.

Then wait. Do not begin implementing.

## 3. Proportionality

This ceremony scales with blast radius. A typo fix, a rename, or a change under ~20 lines with one obvious correct form: just do it. A new module, a schema change, anything touching auth, money, migrations, or deletion: full treatment, and be more suspicious than usual of your own assumptions.

## 4. After I approve

Implement the plan as approved. If you discover mid-implementation that an assumption was wrong or the plan doesn't survive contact with the code, stop and tell me — don't quietly improvise a different design and don't press on with an approach you now believe is wrong.
