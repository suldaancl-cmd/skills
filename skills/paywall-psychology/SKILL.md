---
name: paywall-psychology
description: The behavioral-science engine behind why users buy iOS/Android subscriptions — anchoring, decoy, loss aversion, endowment, present bias, charm/center-stage pricing, Cialdini's 7 principles, the Fogg B=MAT model, and the quiz-onboarding commitment ramp. Use when designing/critiquing a paywall or onboarding funnel, writing paywall copy, choosing pricing framing, or deciding which emotional lever fits a category. Companion to paywall-design-patterns, paywall-strategy-planner, paywall-compliance-guardrails, paywall-teardowns.
---

# Paywall Psychology — Why People Buy Subscriptions

People do not coolly weigh price against value. They buy through a stack of predictable cognitive shortcuts. The **onboarding flow inflates willingness-to-pay; the paywall is the persuasion surface where it cashes out.** Full cited research: `references/psychology-research.md`.

## The mental model in one line
Maximize **Motivation** (onboarding builds desire), remove friction on **Ability** (one-tap store billing), and fire the **Trigger** (paywall) at the peak-motivation moment — Fogg's `B = MAT`. If any of the three is missing at the decision moment, no purchase fires.

## The 9 core pricing/decision levers (apply these first)

| Lever | What it does | How to use on a paywall |
|---|---|---|
| **Anchoring** | First number seen sets the reference | Show the expensive plan/price first so the target plan looks cheap |
| **Decoy / asymmetric dominance** | A deliberately inferior 3rd option shifts choice to the target | Insert a weak middle/monthly tier so annual looks obviously smart (Ariely's *Economist* case: decoy lifted the bundle to ~84%) |
| **Loss aversion** | Losing hurts ~2× as much as gaining pleases | Frame as avoiding a loss ("don't lose your streak/progress/discount"), not gaining a feature |
| **Endowment (free trial)** | We over-value what we feel we own | Trial manufactures ownership → trial-end registers as a *loss* (show progress already made) |
| **Present bias / hyperbolic discounting** | Immediate cost weighted heavily, future discounted | "Free today, billed in 7 days" — the $0-now is what converts |
| **Free trial as commitment device** | Auto-renew binds the future self | Trial + auto-renew default: the future self who'd cancel is under-weighted |
| **Price framing (per-day/week)** | Same price, smaller unit feels cheaper | "$0.76/week" beats "$39.99/year" — framing, not a discount |
| **Charm / left-digit** | .99 reads as the lower left digit | $4.99 reads "4-something," not "5" |
| **Center-stage effect** | Middle option in a row feels default/popular | Put the plan you want chosen in the visual center, elevated |

## Cialdini's 7 principles → paywall moves
- **Reciprocity** — give real value free first (personalized report/plan) so subscribing feels like giving back.
- **Commitment & consistency** — quiz onboarding: after stating goals, subscribing is the *consistent* next act.
- **Social proof** — "Join 5M+ users," ratings, "most popular" badge, testimonials.
- **Authority** — "designed with doctors/trainers," clinical logos.
- **Liking** — warm tone, relatable avatars, "your plan" personalization.
- **Scarcity** — real time-boxed offers, launch discounts.
- **Unity** — shared identity ("runners like you," "the [Brand] family").

## Why quiz onboarding raises willingness-to-pay
Long interactive quizzes work through **three compounding effects**:
1. **IKEA effect** — we value what we help build; the "personalized plan" feels more valuable.
2. **Sunk cost + consistency** — every answered question is a micro-"yes" that makes the final "yes" consistent; quitting forfeits invested effort.
3. **Perceived personalization** — "your plan, built from your answers" raises perceived value, justifying higher prices.

This is why Noom (up to ~113 screens) and Flo (~70 screens) never show price until commitment is maxed.

## Emotional driver by category (tune copy to this)
- **Aspiration** (fitness/meditation) → visualize the future self ("calmer in 10 days"), convert progress into ownership.
- **Fear/anxiety** (health, dating FOMO) → loss/threat framing. Effective but ethically sensitive — never manufacture the fear.
- **Identity / Unity** → the app as who the user is.
- **Habit/streak** (Duolingo) → daily loss-aversion loop + variable reward.
- **Status** → premium tiers, badges, leaderboards.

## The ethics line (this is a guardrail, not optional)
Same lever is **persuasion** if all three hold, **manipulation** if any fails:
1. Is every claim **true**? (no phantom "was $99" prices, no fake timers)
2. Can the user **see and understand** price/renewal/cancellation terms?
3. Can they **act freely** — cancel as easily as they subscribed?

A "no" to any is a dark pattern and now carries real regulatory risk (see `paywall-compliance-guardrails`). Manipulation drives chargebacks, churn, and refunds — it loses money past the first charge.

## Honest caveats
- Psychological *principles* here are academically grounded (Kahneman/Tversky 1979, Huber-Payne-Puto, Cialdini, Laibson 1997, Thomas & Morwitz 2005, Valenzuela & Raghubir 2009, Fogg, Schultz). Conversion *percentages* are vendor benchmarks (RevenueCat/Adapty/Apphud) — directional, not universal constants. Kept separate on purpose.
- Dopamine→habit is well-evidenced; the habit→purchase step is inferred from benchmark correlation, not neuro-causal proof. Don't overstate it.

Full sourcing, study citations, and the ethical/manipulative comparison table: `references/psychology-research.md`.
