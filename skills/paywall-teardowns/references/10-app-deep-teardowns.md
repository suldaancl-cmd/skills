# Deep Funnel Teardowns: 10 Landmark Subscription Apps

**Scope:** onboarding → paywall → trial → retention, per app.
**Method:** desk research against published teardowns, screenshot libraries (screensdesign, paywallscreens, Mobbin), and vendor case studies (Superwall, RevenueCat, Adapty, Growth.design). Compiled 2026-07-20.

**Verification convention:** every specific claim carries a `[source: …]` tag. Claims I could not tie to a source are explicitly labelled **[unverified]**. Prices and mechanics change constantly (most of these apps A/B-test pricing live), so treat every figure as "as reported on the cited date/source," not a permanent list price.

---

## 1. Cal AI (AI calorie scanner)

**Onboarding flow**
- Standard quiz-style onboarding: goals, activity level, current/target weight, diet preferences, then straight into the subscription screen. [source: https://www.eesel.ai/blog/cal-ai-pricing]
- Multi-page onboarding flows are one of the tested formats; onboarding is the *primary* monetization surface (61 of their experiments were onboarding-paywall experiments). [source: https://superwall.com/case-studies/cal-ai]

**Where & how the paywall appears**
- Hard paywall at the end of onboarding — a valid payment method is required to start the 3-day trial. [source: https://www.eesel.ai/blog/cal-ai-pricing]
- Additional monetization gates *beyond* onboarding: camera/barcode/label scan gates, premium feature gates (macros, analytics, progress photos), and win-back flows for lapsed users. 46 trigger points total. [source: https://superwall.com/case-studies/cal-ai]

**Paywall layout**
- Signature format was a **spin-wheel paywall** that lets users "unlock" a discount (gamified pricing). Also tested video paywalls and multi-page flows. [source: https://superwall.com/case-studies/cal-ai]
- Weekly-equivalent price was displayed more prominently than the actual billed amount; trial toggle placed to de-emphasize auto-renewal — this got the app pulled from the App Store in April 2026 and reinstated after fixes. [source: https://www.eesel.ai/blog/cal-ai-pricing]

**Pricing & trial**
- Nominal: **$9.99/mo or $29.99/yr, 3-day free trial** (payment method required upfront). [source: https://www.eesel.ai/blog/cal-ai-pricing]
- Heavy A/B variance reported: $2.99/wk, $5.99/wk, $5.99/mo, $19.99/yr, $49.99/yr; Family Plan $59.99/yr. [source: https://www.eesel.ai/blog/cal-ai-pricing]
- 3-day trial is the shortest in the calorie-tracking category (rivals offer 7+ days). [source: https://www.eesel.ai/blog/cal-ai-pricing]

**Signature psychological tactics**
1. **Relentless live experimentation** — 123 A/B experiments, 160 unique paywall designs, 424 variants in 10 months (~5 experiments/month). [source: https://superwall.com/case-studies/cal-ai]
2. **Gamified discount unlock** (spin-wheel) — turns a price objection into a "win." [source: https://superwall.com/case-studies/cal-ai]
3. **Weekly-price framing** — anchoring on the small weekly number vs. the annual charge (the tactic Apple later forced them to soften). [source: https://www.eesel.ai/blog/cal-ai-pricing]

**Published conversion/revenue numbers**
- 3x+ monthly revenue growth in 10 months; +31% trial-to-paid; 87% paywall-presentation rate to new users; 63% checkout completion. [source: https://superwall.com/case-studies/cal-ai]

**Sources:** https://superwall.com/case-studies/cal-ai · https://www.eesel.ai/blog/cal-ai-pricing · https://screensdesign.com/apps/cal-ai-calorie-tracker

---

## 2. Duolingo

**Onboarding flow**
- User completes a lesson *before* being asked to create an account. Moving the sign-up wall behind the first lesson increased DAUs by ~20%. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]
- Soft-wall → hard-wall commitment sequence; sign-up requested only after value is delivered. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]

**Where & how the paywall appears**
- Reverse trial: new users get **14 days of Super Duolingo free**, experiencing premium before free. [source: https://www.revenuecat.com/blog/growth/cem-kansu-duolingo-sub-club-podcast-2026/]
- Paywall is **context-customized by entry point**: entered from the shop → emphasizes unlimited hearts; entered from an ad → emphasizes removing ads. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]

**Paywall layout**
- Multiple contextual paywall variants rather than one static screen; benefit emphasized matches the friction the user just hit (hearts, ads, etc.). [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]
- Detailed visual layout of the current plan-card screen: **[unverified]** (not captured with a screenshot source in this pass).

**Pricing & trial**
- 14-day Super Duolingo free trial → paid. [source: https://www.revenuecat.com/blog/growth/cem-kansu-duolingo-sub-club-podcast-2026/]
- Exact current Super/Max price points: **[unverified]** in this pass.

**Signature psychological tactics**
1. **Endowed progress / sunk cost** — completing a lesson before the sign-up wall makes abandoning feel like a loss. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]
2. **Reverse trial** — premium-first so the free tier feels like a downgrade. [source: https://www.revenuecat.com/blog/growth/cem-kansu-duolingo-sub-club-podcast-2026/]
3. **Contextual paywall targeting** — sell the exact benefit tied to the moment of friction. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html]
4. **Freemium as moat** — deliberately does *not* over-lock the free tier; engagement is the north star, not short-term conversion. [source: https://www.revenuecat.com/blog/growth/cem-kansu-duolingo-sub-club-podcast-2026/]

**Published conversion/revenue numbers**
- Onboarding converts at ~8.9% vs. ~2% industry average; +20% DAU from moving sign-up behind the first lesson. [source: https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html] *(single-source figure — flag)*

**Sources:** https://relaunch.ai/blog/duolingo-onboarding-teardown-7-b-tests-behind-their-9-conver.html · https://www.revenuecat.com/blog/growth/cem-kansu-duolingo-sub-club-podcast-2026/ · https://www.howtheygrow.co/p/how-duolingo-grows

---

## 3. Tinder

**Onboarding flow**
- Profile creation / swiping begins immediately; the upsell is woven into core swiping, not a front-loaded quiz. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)]

**Where & how the paywall appears**
- Gold paywall surfaces *after a few swipes*, triggered by the "someone already liked you" moment — the answer is locked behind the paywall. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)]
- Historically most paywalls merchandised Plus; Gold is increasingly pushed in top-converting paywalls. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)]

**Paywall layout / mechanic**
- **Blur-to-reveal**: profiles of people who liked you are shown blurred — visual tease says "something desirable is here," withholds "who?" Upgrading unblurs them. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)]
- Four tiers: Plus, Gold, Platinum, invite-only Select. Gold = Plus + "See Who Likes You." [source: https://www.androidauthority.com/tinder-plus-gold-platinum-3236244/]

**Pricing & trial**
- Gold typically **$25–$45/mo** depending on age/location; ~$39.99/mo or ~$23.33/mo on a 6-month plan; US users often see $20–$30/mo. Match does not publish one list price — dynamic A/B pricing by market. [source: https://www.g2a.com/news/features/how-much-is-tinder-gold-tinder-plus-vs-gold-vs-platinum-prices-features-and-which-is-worth-it/ · https://www.ad-hoc-news.de/boerse/news/ueberblick/tinder-gold-by-match-group-inc-subscription-tier-under-pricing-pressure/69784864]
- Trial: no standard free trial model reported; monetization is feature-unlock, not trial-to-paid. **[unverified]** on any trial offer.

**Signature psychological tactics**
1. **Curiosity gap / information withholding** — blurred likers create an itch only payment scratches. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)]
2. **Peak-moment paywall placement** — surfaced exactly when "someone likes you" dopamine hits. [source: same]
3. **Dynamic/age-based pricing** — price discrimination by cohort and market. [source: https://www.ad-hoc-news.de/boerse/news/ueberblick/tinder-gold-by-match-group-inc-subscription-tier-under-pricing-pressure/69784864]

**Published conversion/revenue numbers**
- ~8% of users upgrade to Gold specifically to see who liked them. [source: https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux (search summary)] *(single-source — flag)*

**Sources:** https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux · https://www.androidauthority.com/tinder-plus-gold-platinum-3236244/ · https://www.g2a.com/news/features/how-much-is-tinder-gold-tinder-plus-vs-gold-vs-platinum-prices-features-and-which-is-worth-it/ · https://unstar.app/blog/tinder-gold-bumble-premium-hinge-plus-dating-paywalls-2026

---

## 4. Calm

**Onboarding flow**
- Personalized questions about user goals early, used to tailor content and lift conversion; leans on statistics + social proof. [source: https://goodux.appcues.com/blog/calm-app-new-user-experience]
- "Get Started with Calm" dashboard section guides new users through features non-linearly / self-paced (autonomy-respecting). [source: https://goodux.appcues.com/blog/calm-app-new-user-experience]

**Where & how the paywall appears**
- Paywall presented *during onboarding* — the point where most purchases occur — paired with the 7-day free trial. [source: https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate]

**Paywall layout**
- **Single plan** (no tier comparison) to simplify the decision. [source: https://adapty.io/blog/the-10-types-of-mobile-app-paywalls/]
- Emphasizes 7-day free trial on the yearly plan; **strikethrough price** to signal discount; annual price broken down to a per-month figure to feel cheaper. [source: https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate]

**Pricing & trial**
- **$69.99/year with 7-day free trial** (single plan). [source: https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate]
- Ongoing experimentation noted — e.g., at one point the in-app trial was removed and made web-registration-only. [source: https://screensdesign.com/showcase/calm]

**Signature psychological tactics**
1. **Single-choice simplicity** — kills comparison paralysis. [source: https://adapty.io/blog/the-10-types-of-mobile-app-paywalls/]
2. **Price re-anchoring** — strikethrough + per-month breakdown on the annual plan. [source: https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate]
3. **Social proof + personalization** during onboarding to justify the price before it appears. [source: https://goodux.appcues.com/blog/calm-app-new-user-experience]

**Published conversion/revenue numbers:** **[unverified]** — no hard conversion % tied to a source in this pass.

**Sources:** https://goodux.appcues.com/blog/calm-app-new-user-experience · https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate · https://adapty.io/blog/the-10-types-of-mobile-app-paywalls/ · https://screensdesign.com/showcase/calm

---

## 5. Headspace

**Onboarding flow**
- Onboarding funnels users into "Basic": a 10-day beginner course, each session 3/5/10 min (user choice). Goal is completing day-1 meditation in the first session. [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]
- Anchors the "aha moment" in a **3-minute guided breathing session delivered inside onboarding**; instructor then asks users to notice how their state shifted — converting an abstract claim into a felt result. [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]

**Where & how the paywall appears**
- Soft paywall; the paywall appears **immediately after the "noticing" moment**, not before value is felt. [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]

**Paywall layout**
- Described as "exceptionally well-designed for trust." [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who] Exact card/CTA layout: **[unverified]** (no screenshot source captured this pass; see screensdesign showcase).

**Pricing & trial**
- **$12.99/mo with 7-day free trial**, or **$69.99/yr with 14-day free trial**. [source: https://www.choosingtherapy.com/headspace-review/ · https://www.headspace.com/subscriptions]
- Price-tests every ~6 months. [source: https://sbigrowth.com/insights/headspace-calm-pricing]

**Signature psychological tactics**
1. **Engineered aha before ask** — deliver a felt result (calmer state) *then* show the paywall. [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]
2. **Micro-commitment ramp** — 3/5/10-min sessions lower the mental cost of starting. [source: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]
3. **Longer trial on the annual plan** (14 vs 7 days) to steer toward the higher-LTV annual. [source: https://www.choosingtherapy.com/headspace-review/]

**Published conversion/revenue numbers:** brand valued ~$3B referenced narratively; no clean paywall-conversion % sourced → **[unverified]**. [context: https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who]

**Sources:** https://www.howtheygrow.co/p/how-headspace-grows-the-monk-who · https://www.choosingtherapy.com/headspace-review/ · https://www.headspace.com/subscriptions · https://sbigrowth.com/insights/headspace-calm-pricing · https://screensdesign.com/showcase/headspace-meditation-sleep

---

## 6. Blinkist

**Onboarding flow**
- **Soft paywall** — users can enter and look around, then are pushed to start a 7-day free trial. [source: https://www.funnelteardowns.net/teardown/blinkist]
- Asks low-stakes reading-preference questions early to build investment (sunk cost). [source: https://www.funnelteardowns.net/teardown/blinkist]

**Where & how the paywall appears**
- Trial-gate paywall after brief exploration; a redesign made the paywall about *trial mechanics and cancellation clarity* rather than features. [source: https://growth.design/case-studies/trial-paywall-challenge]

**Paywall layout**
- Winning variant **mentions zero features/benefits**; instead it visualizes the trial timeline and reassures about cancellation. Immediately after payment, offers to send a reminder "before the trial expires." [source: https://growth.design/case-studies/trial-paywall-challenge]

**Pricing & trial**
- 7-day free trial; freemium with unlimited access to 6,500+ titles + Blinkist Guides on premium. [source: https://www.funnelteardowns.net/teardown/blinkist] Exact $/yr not sourced this pass → **[unverified]** on the number.

**Signature psychological tactics**
1. **Loss-aversion over benefit-listing** — kill the "I'll forget to cancel and get charged" fear; that fear drove 33% of cancellations right after trial start. [source: https://growth.design/case-studies/trial-paywall-challenge]
2. **Transparency as conversion lever** — promising a pre-charge reminder built trust *and* opt-ins. [source: https://growth.design/case-studies/trial-paywall-challenge]
3. **Early sunk-cost priming** via preference questions. [source: https://www.funnelteardowns.net/teardown/blinkist]

**Published conversion/revenue numbers**
- +23% trial signups; push opt-in 6% → 74% (**+1,200%**); −55% customer complaints; +4% trial retention. [source: https://growth.design/case-studies/trial-paywall-challenge · https://b2bpricinginsights.substack.com/p/4-min-read-how-blinkists-new-paywall] *(two independent sources — well-corroborated)*

**Sources:** https://growth.design/case-studies/trial-paywall-challenge · https://www.funnelteardowns.net/teardown/blinkist · https://b2bpricinginsights.substack.com/p/4-min-read-how-blinkists-new-paywall · https://www.purchasely.com/blog/blinkist-paywall-transformation-revolutionizes-app-user-engagement

---

## 7. Flo (period & cycle tracker)

**Onboarding flow**
- **~70 screens** in onboarding — one of the longest in consumer health. [source: https://www.retention.blog/p/flo-is-an-amazing-success-story]
- A **"tap and hold" gesture** just before the paywall creates a moment of physical/psychological commitment. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]

**Where & how the paywall appears**
- Paywall at the end of the long personalization flow. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]

**Paywall layout**
- Toggle for a **14-day free trial**; primary offer is the yearly plan; scrolling reveals monthly and family options. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]
- **Post-purchase "gift"**: after subscribing, a special screen offers a 33% discount on the yearly plan to push an immediate upgrade off the trial. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]

**Pricing & trial**
- 14-day trial; yearly primary + monthly + family tiers. Exact $ not pinned to a source this pass → **[unverified]** on the number. [source: https://help.flo.health/hc/en-us/articles/4407228743956-Trying-Flo-Premium]

**Signature psychological tactics**
1. **Extreme personalization / sunk cost** — ~70 screens make quitting feel wasteful. [source: https://www.retention.blog/p/flo-is-an-amazing-success-story]
2. **Physical micro-commitment** — the tap-and-hold gesture primes commitment right before price. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]
3. **Immediate post-purchase upsell** — 33%-off "gift" converts trialists to annual before they cool off. [source: https://screensdesign.com/showcase/flo-period-pregnancy-tracker]

**Published conversion/revenue numbers**
- iOS paywall est. **~$8M/month** from ~2M monthly downloads; **$190M+ ARR**, ~50% of revenue from 1yr+ users. [source: https://www.paywallscreens.com/apps/flo-period-pregnancy-tracker-mobile-paywall-140b · https://www.retention.blog/p/flo-is-an-amazing-success-story] *(estimates from third parties — treat as directional)*

**Sources:** https://www.retention.blog/p/flo-is-an-amazing-success-story · https://screensdesign.com/showcase/flo-period-pregnancy-tracker · https://www.paywallscreens.com/apps/flo-period-pregnancy-tracker-mobile-paywall-140b · https://help.flo.health/hc/en-us/articles/4407228743956-Trying-Flo-Premium

---

## 8. Rocket Money (formerly Truebill)

**Onboarding flow**
- Connect financial accounts to surface subscriptions and spending; free tier is functional. Detailed screen-by-screen flow not captured with a screenshot source → **[unverified]** on screen count.

**Where & how the paywall appears**
- App is free; paywall gates specific features — bill negotiation, real-time syncing, budgeting, financial goals, net-worth tracking, credit-score tracking, and the subscription-cancellation concierge. Free tier capped at **2 budget categories**; Premium unlocks unlimited. [source: https://www.rocketmoney.com/learn/personal-finance/how-much-does-rocket-money-cost · https://financebuzz.com/truebill-review]

**Paywall layout / pricing**
- **"Pay-what-you-think-is-fair" slider**, roughly **$7–$14/mo** (sources also cite $6–$12/mo depending on period). User picks their own price within a band. [source: https://www.thepennyhoarder.com/budgeting/rocket-money-review/ · https://financebuzz.com/truebill-review]
- Bill-negotiation is success-fee based (a cut of realized savings — reported as able to exceed half the savings). [source: https://financebuzz.com/truebill-review]

**Signature psychological tactics**
1. **Pay-what-you-want pricing** — the slider gives users control (autonomy/endowment effect) and captures willingness-to-pay across a band; higher default anchors nudge up the chosen price. [source: https://www.thepennyhoarder.com/budgeting/rocket-money-review/]
2. **Problem-then-paywall** — surfaces forgotten subscriptions / overspend first, so Premium (which fixes it) feels earned. [source: https://financebuzz.com/truebill-review]
3. **Done-for-you concierge** — cancellation + negotiation removes the effort the user dreads, justifying recurring pay. [source: https://financebuzz.com/truebill-review]

**Published conversion/revenue numbers:** **[unverified]** — no funnel-conversion figure tied to a source this pass.

**Sources:** https://www.rocketmoney.com/learn/personal-finance/how-much-does-rocket-money-cost · https://financebuzz.com/truebill-review · https://www.thepennyhoarder.com/budgeting/rocket-money-review/ · https://www.cnbc.com/select/truebill-review/

---

## 9. ChatGPT (mobile)

**Onboarding flow**
- Minimal: install → sign in → immediate use of the free tier. No quiz funnel; product value is self-evident on first prompt. **[unverified]** on any structured onboarding screens.

**Where & how the paywall appears**
- Soft / feature-gated: free users hit caps or locked models and see the **Upgrade to Plus** screen contextually (e.g., when model access or limits are reached). Adapty catalogs a ChatGPT mobile paywall screen. [source: https://adapty.io/paywall-library/chatgpt/]

**Paywall layout**
- Upgrade screen lists Plus benefits (higher limits, advanced models, priority). Screenshot in Adapty's library. [source: https://adapty.io/paywall-library/chatgpt/] Exact card copy/CTA not transcribed this pass → **[unverified]** on verbatim copy.

**Pricing & trial**
- **ChatGPT Plus $19.99/mo, no annual option**, unchanged since Feb 2023. In-app purchase priced at $19.99. Regional variance ~$10.84 (Turkey) to ~$27.71 (Denmark). [source: https://www.u7buy.com/blog/chatgpt-plus-price-breakdown/ · https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus]
- No standard free trial on Plus (the free tier *is* the "trial"). [source: https://chatgpt.com/pricing/]

**Signature psychological tactics**
1. **Product-led / generous free tier as the funnel** — value proven before any ask; upgrade triggered by hitting real usage limits (natural friction, not manufactured). [source: https://adapty.io/paywall-library/chatgpt/]
2. **Flat, memorable single price ($20)** — no tier paralysis, no discount games; simplicity as trust. [source: https://www.u7buy.com/blog/chatgpt-plus-price-breakdown/]
3. **Capability gating** — locking newest models/limits behind Plus makes the upgrade about "the good stuff," timed to the moment of need. [source: https://adapty.io/paywall-library/chatgpt/]

**Published conversion/revenue numbers:** **[unverified]** in this pass (OpenAI does not publish mobile-paywall conversion rates).

**Sources:** https://adapty.io/paywall-library/chatgpt/ · https://www.u7buy.com/blog/chatgpt-plus-price-breakdown/ · https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus · https://chatgpt.com/pricing/

---

## 10. Noom

**Onboarding flow**
- **Web-to-app quiz funnel of up to 113 screens, ~10–15 minutes.** Detailed personal questions on health goals and eating habits generate a "personalized plan." [source: https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel/ · https://web2appworld.com/breakdowns/noom/]
- Described as "a masterclass in onboarding conversion — building commitment through personalization, education, and empathy." [source: https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel/]

**Where & how the paywall appears**
- Price is **not shown publicly** — you must complete the quiz to see your price. Paywall appears only after heavy time/effort/emotional investment. [source: https://web2appworld.com/breakdowns/noom/]

**Paywall layout**
- Quiz builds a personalized-plan reveal, then price; limited-time offers and urgency countdowns layered on. Exact card layout: **[unverified]** verbatim, but urgency copy documented. [source: https://web2appworld.com/breakdowns/noom/]

**Pricing & trial**
- Trial offered (often a low-cost/"$0.50"-style trial historically); typical monthly ~**$59.99/mo, rising to ~$70/mo** after intro promo. When the trial ends it's a **hard paywall — no free downgrade tier.** [source: https://web2appworld.com/breakdowns/noom/ · https://www.amyfoodjournal.com/blog/noom-review]

**Signature psychological tactics**
1. **Sunk cost via a very long quiz** — every answer is another reason not to quit. [source: https://web2appworld.com/breakdowns/noom/]
2. **Personalization = perceived value** — by the paywall, users believe the plan is built specifically for them. [source: https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel/]
3. **Manufactured urgency** — "your personalized plan expires in 24 hours" / "special pricing available now." [source: https://web2appworld.com/breakdowns/noom/]
4. **Price-after-commitment** — never reveal price until emotional buy-in is maxed. [source: https://web2appworld.com/breakdowns/noom/]

**Published conversion/revenue numbers:** funnel widely cited as best-in-class; no clean conversion % tied to a source this pass → **[unverified]** on the exact number. [context: https://www.paddle.com/studios/shows/fix-that-funnel/noom]

**Sources:** https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel/ · https://web2appworld.com/breakdowns/noom/ · https://www.retention.blog/p/the-longest-onboarding-ever · https://www.paddle.com/studios/shows/fix-that-funnel/noom · https://www.amyfoodjournal.com/blog/noom-review

---

# Cross-App Synthesis: What the Winners Share

Repeated moves that show up again and again across these 10 funnels:

1. **Value before the ask.** Deliver a felt result or investment *before* the paywall — Headspace's in-onboarding breathing "aha," Duolingo's first lesson before sign-up, Noom/Flo's long personalization quizzes. The paywall lands after the user already feels they've gained (or invested) something. [sources: howtheygrow, relaunch.ai, web2appworld, retention.blog]

2. **Sunk-cost / commitment ramp via long personalized onboarding.** Flo ~70 screens, Noom up to 113. Length isn't a bug — every answered question raises the cost of walking away and makes the resulting "plan" feel bespoke. [sources: retention.blog, revenuecat, web2appworld]

3. **Price re-anchoring on the annual plan.** Strikethrough prices, per-month breakdowns of annual cost, and longer trials on annual (Headspace 14 vs 7 days) all steer users to the higher-LTV yearly plan while making it feel cheap. [sources: kristenberman, choosingtherapy]

4. **Relentless live A/B testing of the paywall as a product surface.** Cal AI ran 123 experiments / 424 variants in 10 months; Tinder, Duolingo, Calm, and Headspace all test pricing/paywalls continuously (Headspace every ~6 months). No one treats the paywall as static. [sources: superwall, sbigrowth, ad-hoc-news]

5. **Loss-aversion beats benefit-listing.** Blinkist's biggest win came from a paywall that mentioned *zero* features and instead killed the "I'll forget to cancel and get charged" fear (+23% signups, complaints −55%). Fear-removal and trust reminders outperform aspirational feature lists. [source: growth.design]

6. **Curiosity gaps and contextual gating.** Tinder blurs who-liked-you; Duolingo tailors the paywall benefit to the exact friction the user hit; ChatGPT gates the newest models. Sell the specific thing the user wants *at the moment they want it.* [sources: startupspells, relaunch.ai, adapty]

7. **Post-purchase and win-back upsells.** Flo's immediate 33%-off "gift" after subscribing; Cal AI's family-plan/lifetime upsells and lapsed-user win-back flows. The funnel doesn't end at first purchase — it laddering into higher tiers and re-capture. [sources: screensdesign, superwall]

8. **Simplicity where the decision is hard.** Calm's single plan and ChatGPT's flat $20 remove comparison paralysis — the opposite lever from the long-quiz apps, but same goal: reduce the cognitive cost of the yes. [sources: adapty, u7buy]

---

## Methodology & confidence notes
- **Searched:** growth.design, screensdesign, paywallscreens, Superwall/RevenueCat/Adapty/Purchasely case studies, retention.blog, plus review/pricing sites for numbers. Fetched full text for the Cal AI (Superwall) and Blinkist (Growth.design) case studies for exact figures.
- **Strongest data (screens + tactics + numbers):** Cal AI, Duolingo, Blinkist, Flo, Noom, Calm, Headspace, Tinder — **8 of 10 solid.**
- **Thinner (tactics + pricing solid, but no sourced funnel-conversion number and no transcribed screen-by-screen):** Rocket Money, ChatGPT mobile — **2 of 10 partial.**
- **Excluded:** Photomath (chose Noom per the OR option, richer funnel literature).
- **Caveats:** Most pricing figures are A/B-tested and region/cohort-variable; third-party revenue estimates (Flo $8M/mo, $190M ARR) are directional. Single-source figures flagged inline (Duolingo 8.9%, Tinder ~8%). Verbatim paywall copy and exact live screen counts for several apps were not transcribed from a primary screenshot and are marked **[unverified]** rather than guessed.
