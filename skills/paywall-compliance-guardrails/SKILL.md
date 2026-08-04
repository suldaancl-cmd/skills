---
name: paywall-compliance-guardrails
description: What Apple App Store & Google Play actually require and prohibit on subscription paywalls, the dark-pattern taxonomy behind "dark psychology" tactics, the grey zone, and real FTC/EU enforcement ($2.5B Amazon, $100M Vonage). Use before shipping a paywall, when reviewing one for App Store/Play rejection risk, when a tactic feels manipulative, or to stay on the legal side of persuasion. Companion to paywall-psychology, paywall-design-patterns, paywall-strategy-planner.
---

# Paywall Compliance Guardrails — Stay Persuasive, Not Punishable

The line between persuasion and manipulation is now enforced with real money. Full sourced detail: `references/store-compliance.md` (store rules) and `references/dark-patterns-taxonomy.md` (taxonomy + enforcement). **Verify exact clause text at the linked store URLs before quoting to a client — Apple/Google wording changes.**

## Must-disclose on/near the paywall BEFORE purchase (both stores)
- **Price**, **billing period/frequency**, **auto-renewal terms**, **trial length + what's lost when it ends**, **whether a subscription is required to use the app**, and **how to cancel**.
- Apple **3.1.2(c)**: "Before asking a customer to subscribe, you should clearly describe what the user will get for the price." Terms must be visible **without requiring extra taps/links**.
- Apple **3.1.1** (trials): must disclose duration, content lost at trial end, and downstream charges **before** the trial starts. Auto-renewable subs must be **≥7 days**.
- Google Play: cost, cadence, auto-renewal, and trial-conversion terms must be disclosed with **no additional action needed** to see them; free trials **3 days–3 years**.

## Required controls
- **Restore Purchases** mechanism (Apple 3.1.1 explicitly).
- **Cancellation path** — Google requires a clear in-app *and* web cancel route (deep-link to Play subscription center); cancel must not be harder than signup.
- **Visible dismiss/close** — neither store's primary text names a literal "close button" rule, but hard-to-close paywalls are rejected/enforced under the **anti-deception / bait-and-switch** clauses (Apple 3.1.2(a): scam/bait-and-switch subs "will be removed… you may be removed from the Apple Developer Program"). Practitioner consensus: always ship a visible, tappable close.
- **Terms of Use + Privacy Policy links** in the paywall UI itself, not just the store listing.

## The dark-pattern taxonomy (what "dark psychology" actually names)
Sources: Brignull's deceptive.design, FTC *Bringing Dark Patterns to Light* (2022), Mathur et al. 2019.

| Pattern | What it is |
|---|---|
| **Forced continuity** | Trial silently converts to paid, card charged with no fresh consent |
| **Roach motel** | Easy to subscribe, very hard to cancel |
| **Hidden costs** | Low advertised price, fees appear at billing |
| **Sneak into basket** | Add-on/sub auto-enrolled without clear consent |
| **Confirmshaming** | Guilt copy on decline ("No thanks, I don't want to save money") |
| **Preselection** | Paid plan/add-on pre-checked by default |
| **Trick questions** | Double-negative toggles that obscure the real choice |
| **Fake urgency / scarcity** | Fake countdowns that reset, "1 left" that isn't true |
| **Bait-and-switch** | Trial converts to a materially different paid obligation |
| **Obstruction** | Cancel requires phone-only, hold times, a maze of pages |
| **Nagging** | Repeated prompts for an action already declined |
| **Visual interference** | Tiny "X," low-contrast decline next to a big Subscribe |
| **Comparison prevention** | Obfuscated pricing so plans can't be compared |

## Enforcement — this is now board-level P&L risk
- **FTC v. Amazon (Prime)** — dark-pattern enrollment + "Iliad" cancel maze → **$2.5B** total ($1B penalty + $1.5B refunds), settled Sept 2025.
- **FTC v. Vonage** — cancel-by-phone-only obstruction → **$100M** refunds.
- **FTC v. Age of Learning (ABCmouse)** — pre-checked boxes + reset cancel flow → **$10M**.
- **"Click to Cancel" rule** was vacated on procedural grounds July 2025, but **ROSCA + the 1973 Negative Option Rule remain in force** (they were the actual basis for Amazon/Vonage); FTC restarted rulemaking Jan 2026.
- **EU:** CPC Network sweep found ~40% of retail sites/apps use dark patterns; Omnibus Directive allows fines **up to 4% of turnover** in the member states concerned. (An EU-vs-X €120M DSA figure circulated but was unconfirmed against a primary EC source — don't cite it as fact.)

## The grey zone (converts, but skirts the line — decide deliberately)
Preselected annual default · delayed/timed close button · trial-reminder timed to be missed. Legal where reversible and findable, but California's dark-pattern definition ("substantial effect of subverting or impairing user autonomy") is broad enough to reach aggressive versions even without outright deception. Disclosure compliance does **not** by itself neutralize manipulative framing — that's exactly what regulators are moving to reach.

## The 3-question ship test
Before shipping a paywall, every "yes":
1. Is every claim **true**? (no phantom prices, no fake timers)
2. Can the user **see & understand** price/renewal/cancel terms without hunting?
3. Can they **cancel as easily as they subscribed**?

Any "no" = dark pattern = rejection + enforcement + chargeback/churn risk. The business case against dark patterns is that they lose money after the first charge (refunds, disputes, platform removal).

Full store-rule quotes, per-clause citations, and the enforcement ledger: `references/store-compliance.md` + `references/dark-patterns-taxonomy.md`.
