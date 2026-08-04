---
name: paywall-strategy-planner
description: How to PLAN a subscription paywall for a new or existing app end-to-end — pick a model (hard/soft/freemium/hybrid), trial mechanics, pricing architecture (weekly/monthly/annual, regional), paywall placement/frequency, funnel benchmarks, and the A/B experimentation program. Use when planning monetization for an app, choosing a pricing/trial structure, setting conversion targets, or auditing a subscription funnel. Backed by RevenueCat/Adapty/Superwall 2025-2026 benchmarks. Companion to paywall-psychology, paywall-design-patterns, paywall-compliance-guardrails, paywall-teardowns.
---

# Paywall Strategy Planner — Plan Monetization End-to-End

Full cited benchmarks (RevenueCat 2025/2026, Adapty, Superwall, Business of Apps): `references/monetization-strategy.md`.

## The 3 headline truths
1. **Ask for money early wins on money, not reach.** Hard paywalls convert download→paid ~5× better than freemium (**10.7% vs 2.1%** median, D35) and ~8× revenue-per-install (**$3.09 vs $0.38** at D60) — but discard the ~23% of freemium converters who buy 6+ weeks later. 2026 default for a new consumer app: **hybrid / trial-inclusive** (wins 64.5% of A/B tests).
2. **Weekly + short (3-day) trial is the highest-LTV package** for most consumer apps: adding a 3-day trial to weekly lifts 1-yr LTV **$7.40 → $54.50 (+636%)**; weekly now drives **55.6%** of subscription revenue. **Exception:** Health & Fitness (annual dominates, 60%+), Productivity/Lifestyle (direct buyers can beat trial users). Category decides — test.
3. **Monetization is an experimentation program, not a design.** Median ~14.7 experiments/yr; apps running 50+ tests earn ~18.7× the revenue premium. Trial-structure & localization tests beat visual/copy on win rate.

## The 8-step planning playbook

**Step 0 — Pick the model from product shape, not fashion.**
- Immediately-obvious utility / booking / AI value → **hard paywall or hard trial**.
- Habit / content / social, slow-building value → **soft / freemium or reverse trial** (protects late converters).
- New-app default bet → **hybrid / trial-inclusive** (short evaluation, then gate).

**Step 1 — Default package = weekly + 3-day trial** for most consumer apps. Switch to **annual** if Health & Fitness; test **direct-buy** if Productivity/Lifestyle.

**Step 2 — Price at/above median, localize.** Global medians: **$7.48/wk · $12.99/mo · $38.42/yr**. Price **+29–39% in Europe**. Don't fear premium — high-priced apps earn ~3× the LTV. Sell mostly full price (only ~10% of subs are discounted).

**Step 3 — Design around anchoring.** Default to annual, **reframe per-week** ("$0.76/week"), tag one plan "Most Popular," show savings vs a decoy monthly. (Layout mechanics → `paywall-design-patterns`.)

**Step 4 — Place the primary paywall in onboarding** (up to ~50% of trial starts) + **contextual placements** at gated features + measured session-N re-prompts. Build each placement so hard/soft gating is flippable from remote config.

**Step 5 — Win the first session.** 55% of 3-day-trial cancellations happen Day 0 — invest onboarding in delivering the "aha" before the trial reminder ever fires.

**Step 6 — Instrument the full funnel:** install → paywall-view → trial-start → trial-to-paid → renewal, plus **refund rate** and **billing-failure recovery** (critical on Android: **31% of Play cancels are billing errors** vs 14% on iOS).

**Step 7 — Run it as an experiment program.** Remote-config tooling (RevenueCat / Superwall / Adapty), ~10k views/variant, 14–30 days, decide on **D30 retained ARPU (≥+5%, p<0.05)**, isolate one lever at a time. **Test trial-structure / localization / pricing before visuals.**

## Funnel benchmarks to target (medians)

| Metric | Benchmark | Source |
|---|---|---|
| Download→paid (hard) | 10.7% (D35) | RevenueCat 2026 |
| Download→paid (freemium) | 2.1% (D35) | RevenueCat 2026 |
| Revenue/install (hard vs freemium, D60) | $3.09 vs $0.38 | RevenueCat 2026 |
| Trial→paid (cross-category avg) | ~53% | Adapty 2026 |
| Trial→paid by length | 42.5% (17–32d) vs 25.5% (<4d) | RevenueCat 2026 |
| Year-1 realized LTV | ~$21 (non-AI), ~$30 (AI) | RevenueCat 2026 |
| Annual cancellation, year 1 | ~72% (35% in month 1) | RevenueCat 2026 |

## Trial mechanics cheatsheet
- **Opt-out (card upfront)** converts ~2.5–3× opt-in but pulls 3–4× fewer signups. Hard paywalls get 78% of trials started in week 1.
- **Length paradox:** long trials (17–32d) convert ~70% better but cancel more (26% at 3d → 51% at 30d). Short trials = faster cash + lower refund exposure.
- **Reverse trial** (premium first, downgrade after) can capture the ~15% trial converters *and* keep the ~25% freemium stayers → 30%+ engaged vs ~5% for pure freemium.

## Watch-outs
- **RevenueCat paradox:** best-converting categories often churn fastest — retention must be a co-primary metric, or you optimize the paywall to select churn-prone users.
- **Vendor bias:** RevenueCat/Adapty/Superwall all sell paywall tooling; "test more / hard paywalls win" is triangulated across all three but each has incentive to push it.
- Two figures had no reliable public benchmark: avg number of paywalls shown, and win-back/dunning recovery rates — don't invent them.

Full tables, category splits, and the source ledger: `references/monetization-strategy.md`.
