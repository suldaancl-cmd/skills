# 03 — Build Plan

> The agent never decides what comes next. It reads this.
> Sits *inside* the phase gates in `ADVISE.md` — that file owns the gates, this file owns the features.

**Total:** <N> features across <M> phases.

## Phase 1 — Foundations

| # | Feature | Goal (one line, checkable) | Depends on | Needs `/architect`? |
|---|---|---|---|---|
| 1 | | | — | no |
| 2 | | | 1 | yes — <what decision is unmade> |
| 3 | | | 1 | no |

## Phase 2 — <name>

| # | Feature | Goal | Depends on | Needs `/architect`? |
|---|---|---|---|---|
| 4 | | | | |

## Phase 3 — <name>

| # | Feature | Goal | Depends on | Needs `/architect`? |
|---|---|---|---|---|
| | | | | |

## Phase 4 — <name>

| # | Feature | Goal | Depends on | Needs `/architect`? |
|---|---|---|---|---|
| | | | | |

## Phase 5 — <name>

| # | Feature | Goal | Depends on | Needs `/architect`? |
|---|---|---|---|---|
| | | | | |

---

## How to size a feature

One feature = one `/develop` run = 2–3 files or one screen. If it needs more, split it.
A feature whose goal cannot be written as a checkable sentence is not scoped yet.

## The "needs architect" column

Mark `yes` when the feature would force an undecided choice: a provider, a data model,
a page design, an auth strategy. `/develop` will stop and route there anyway — marking it
here means you saw it coming instead of hitting it mid-build.

## Deviation log

The plan is allowed to change. Record it when it does, so `03` and reality stay one thing.

| Date | Was | Now | Why |
|---|---|---|---|
