---
name: paywall-design-patterns
description: The visual/layout anatomy of high-converting mobile subscription paywalls — hero zone, benefit-list styles, plan selectors, trial toggles, CTA copy, social proof, close-button treatment, plus 20 named design patterns and 15 documented A/B-test outcomes (Superwall/RevenueCat/Adapty/Growth.design). Use when designing, building, or critiquing a paywall screen or onboarding-to-paywall flow, or picking a layout for a category. Companion to paywall-psychology, paywall-strategy-planner, paywall-compliance-guardrails.
---

# Paywall Design Patterns — Layout Anatomy That Converts

Distilled from paywall teardown libraries and vendor A/B datasets. Full cited research with every source URL: `references/design-anatomy.md`.

## Canonical paywall layout (top → bottom)
1. **Hero / visual zone** — product screenshot, icon benefit-grid, or (rising in 2026) a short product/ad video. A **personalized "plan loader"** ("Analyzing your preferences… building your plan") is a common pre-paywall hero step. *Superwall test: a stripped hero (one image + headline + "Continue") beat a detailed feature-comparison hero by +111%.*
2. **Benefit list** — two proven styles: **checkmark value-stack** (short, icon-led, action verbs: "Unlock / Remove / Access") works across the board; **free-vs-Pro comparison table** works better for feature-dense productivity/AI tools. They are not interchangeable — category decides.
3. **Plan selector** — 2-card (Annual + Weekly) often beats 3-tier; preselect annual with a "MOST POPULAR" / "BEST VALUE" badge; reframe the annual total per-week ("only $0.76/week"); use a decoy monthly to make annual look smart.
4. **Trial toggle** — a "free trial enabled" switch frames the trial as an opt-in bonus. 2026 trend: restrict trials to the **annual plan only**.
5. **CTA** — "Start Free Trial" > "Subscribe"; generic "Continue" beat high-pressure "Unlock All Features" (+111%); put "Cancel anytime" / "No commitment" microcopy directly beneath.
6. **Social proof zone** — ratings, review counts, "join 10M users," testimonials (essential in JP/APAC).
7. **Close button** — must be visible & tappable (store requirement). Growth.design's Blinkist redesign: a clearly visible close + cancellation-transparency copy drove **+23% trial signups, push opt-in 6%→74%, −55% complaints**.
8. **Footer** — Terms, Privacy, **Restore Purchases**, auto-renew legalese (required by both stores — see `paywall-compliance-guardrails`).

## The 20 named patterns (pick by intent)

| # | Pattern | One-line | Example apps |
|---|---|---|---|
| 1 | Anchor & Decoy | High price beside discounted annual | MacroFactor, Calm, SCRL |
| 2 | Value Stack | Icon-led checkmark benefit list | MyFitnessPal, ChatOn, ClassDojo |
| 3 | Social Proof Engine | Ratings/testimonials/user counts | Flo, YAZIO, Speak |
| 4 | Soft Commitment | "Free / cancel anytime" framing | Strava, Cal AI, Lose It! |
| 5 | Now-or-Never Offer | Countdown / one-time discount | Captions, Finch, YAZIO |
| 6 | Standard Non-Scrollable | Everything on one screen, no scroll | Moonly |
| 7 | Landing-Page (Scrollable) | Long-form with FAQs/comparisons | Napper, Meditopia |
| 8 | Modal (Carousel) | Popup with swipeable benefits | Hinge |
| 9 | Trial Timeline | Visual day-by-day → charge date | Flinch, Loora |
| 10 | Trial Toggle | Switch buy-now vs start-trial | Lensa |
| 11 | Single-Plan | One tier, no comparison | Calm, HotspotShield |
| 12 | Multiplan + "Most Popular" | Tiers with one tagged | Asana Rebel, Go Fasting |
| 13 | Offer Paywall | Prominent limited-time/lifetime deal | Balance |
| 14 | Donation / PWYW | Free + suggested voluntary pay | Rocket Money, Balance, Being |
| 15 | Personalized/Segmented | Content varies by segment | (SDK-driven) |
| 16 | Personalized Plan Loader | Pre-paywall "building your plan" bar | fitness/weight-loss category |
| 17 | Post-Paywall Recovery Offer | Discount drawer only for non-converters | (10–15% ARPU impact) |
| 18 | Multi-Page "Design Your Trial" | value → terms → reminder → buy | cross-category |
| 19 | Price-Relatability Anchor | "less than a cup of coffee" | Blossom |
| 20 | Identity/Commitment Device | User signs a pledge before paywall | ME+ |

## Onboarding-to-paywall choreography
- **Quiz funnel** (Noom ~113 screens / Cal AI): goal questions → loading pauses → personalized plan reveal → price. Low-pressure escape valves ("I haven't decided"), reassurance after sensitive questions, and a projected result date that shifts as you answer.
- **When to show it:** onboarding-placed paywalls convert highest (~1.35% avg vs ~0.89% gated) **but only if context/value is established first** — a paywall before value "feels jarring."
- **Why choreography matters:** for 3-day trials, **55.4% of cancellations happen Day 0, 84% by Day 1**; ~44.5% of purchases are Day 0. Win the first session, not the reminder email.

## Motion/visual specifics designers copy
Gradient/high-contrast CTA · "SAVE 82%" plan badges · monthly-shown-first price anchoring · countdown timers (with confetti on completion) · theme shift (white→black/gold) between tiers to signal premium · **native Apple-system-styled paywalls beat heavily custom-branded ones** (familiarity/trust).

## Documented A/B wins (use as priors, always test)
- Simplified hero vs comparison chart: **+111%**
- Trial added to weekly plan: 12-mo LTV **$7.40→$54.50 (+636%)**
- Blinkist close+copy redesign: **+23%** trials, **−55%** complaints
- Food/diet redesign (simplify + trial toggle + real reviews): **+72%** install-to-trial
- Party-game redesign (short layout + toggle + "SAVE 83%"): **+31%** trial, **+64%** revenue
- Hard vs freemium: **10.7% vs 2.1%** trial-to-paid, ~8× revenue/install
- **A/B win rates by test type:** localization 62%, trial-structure 60%, plan-duration 59% — **visual/copy only 35%.** Test packaging/pricing before pixels.

## Open contradictions (don't pick blindly)
- Comparison table vs simplified hero — both "used by winners"; comparison for feature-dense tools, simplified for low-consideration buys. Category decides — test it.
- Close-button "delay 1–2s" is practitioner lore, not a canonical study — the button must still resolve to visible & tappable or the store rejects it.

Full anatomy, all 15 sourced A/B tests, and the contradiction analysis: `references/design-anatomy.md`.
