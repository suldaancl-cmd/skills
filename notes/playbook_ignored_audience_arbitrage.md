# playbook — ignored-audience arbitrage (app niches) + Base44 reality check

Source: Jason Lee, "This app for seniors makes $100K/month (Full Vibe Coding Tutorial)", `youtu.be/HCBZFJ8H-Sw`, 2026-08-05, 14:33.
Captured 2026-08-05 via Firecrawl + Exa (youtube.com egress-blocked in the remote container, `yt-dlp` unusable).
Sponsored by Base44, disclosed on-camera. Affiliate link in description.

## The durable idea

Do not invent a market. Take a market with proven paying demand, then ask one question: **who inside it is being ignored?**

Worked example from the video: fitness is the most saturated App Store category. Instead of competing with MyFitnessPal, the winning operators targeted 60+ seniors — an audience with time, disposable income, and a doctor telling them to exercise, while nearly every fitness app is designed for 25-year-olds.

The resulting product is deliberately primitive: a list of exercises, a countdown timer, a progress tracker. For this audience simplicity is the feature, not a compromise.

## Revenue claims from the video — creator's numbers, unverified

| App | Claimed monthly revenue |
|---|---|
| Taichi app for seniors | $100K |
| Yoga, Taichi, Pilates (established) | $300K |
| Tai Chi Walking and Chair Yoga (new launch) | $40K |
| Solo copycat launched after the idea spread | $10K |

These read as third-party estimator figures (Sensor Tower / Appfigures class). Such estimates are routinely off by 2-5x, and they are gross — Apple takes 15-30% before anything reaches the operator. Treat the ranking as directional, the absolute numbers as unverified.

## Reusable prompting sequence (tool-agnostic — works in Claude Code too)

1. **Plan mode first.** Never build on the first prompt. Read the plan, confirm pages, palette, and feature list before a single file is generated.
2. **Pass a live URL as the content reference** — the competitor's store page — so the model researches features and copy instead of inventing them.
3. **Pass a design reference image** (he used a Dribbble screenshot) and instruct it to follow typography, colors, and UI elements. This is what stops the generic-AI-slop look.
4. **Be numerically explicit**: "at least 10 exercises", "a countdown timer per exercise", "character illustration per exercise".
5. **Animate characters externally, then import as `.webm`, never `.mp4`.** WebM carries an alpha channel; MP4 drags in a black or white background that will not blend into the app. Ask explicitly for transparent background and looping.
6. **Build the companion app on the same database.** Member app plus instructor dashboard sharing one DB is the pricing-power move — it turns a consumer app into a B2B tool an instructor pays for.
7. **Preview without a build:** Publish, open the URL in iPhone Safari, Share, Add to Home Screen. It runs chromeless and reads as native. This is a PWA, not a native binary — real App Store submission is a separate step.
8. **Compliance before submission:** Base44 runs an App Store guideline scan and offers "Fix with AI" to feed the violations straight back into the chat.

Steps 1-6 are the transferable part. They are prompting discipline, not Base44 features.

## Base44 — verified state, 2026-08-05

The video's figures are stale. It says "300,000 users and $3.5 million in revenue" — that is roughly the pre-acquisition mid-2025 picture.

Verified:

- Wix acquired Base44 in summer 2025 at an initial $80M valuation. With earn-outs, total consideration now exceeds $150M — including a further $41M paid to founder Maor Shlomo for beating performance targets (Calcalist, 2026-08-04).
- Base44 crossed $150M ARR in May 2026, roughly two months after crossing $100M ARR (TechCrunch, 2026-06-29). Lovable was at ~$500M ARR at the same point.
- Base44 shipped its own model, **Base 1**, in Q2 2026, to cut inference cost and reduce frontier-model dependence.
- Wix posted a $76.4M net loss in Q2 2026 on $563.1M revenue (+15% YoY), driven partly by Base44 compute and a 67% jump in sales and marketing spend.

**Read on that last point:** the unit economics are still being tuned in public. Expect credit allowances and pricing to keep moving. Do not architect a client deliverable that depends on today's credit ceiling.

## Pricing — verified as of 2026-07-26

| Plan | Annual (per mo) | Month-to-month | Message credits | Integration credits |
|---|---|---|---|---|
| Free | $0 | $0 | 25 | 100 |
| Starter | $16 | $20 | 100 | 2,000 |
| Builder | $40 | $50 | 250 | 10,000 |
| Pro | $80 | $100 | 500 | 20,000 |
| Elite | $160 | $200 | 1,200 | 50,000 |

The video's "starts at $16/month" is the annual-billing rate. The catch it does not mention: **custom domain and GitHub integration only unlock at Builder ($40)**. A $16 plan cannot ship a branded product.

## When to reach for Base44 vs the existing stack

Reach for Base44 only for the **service-provider internal tool** case: a client dashboard where the backend — database, auth, payments, SEO, domains, analytics — is bundled and time-to-value beats control. One job, roughly $40/mo, delivered same-day.

Everything else stays on the existing stack. `frontend-design` plus `premium-design-laws` plus Supabase gives full control over host, schema, and design system, and the design bar is higher than a template-driven generator will reach.

Speed note from the video: a mid-build edit landed in ~30 seconds in Base44 versus "a couple of minutes" in Claude Code or Codex. That is a UX-loop observation on one task, not a benchmark.

## How the video itself makes money — worth copying

A two-sided funnel, both sides disclosed or visible:

1. Sponsor fee plus affiliate revenue from Base44.
2. A free "Taichi App Research Report" lead magnet driving signups to the `thebreadcrumb.co` newsletter. The report is the real asset — competitor teardown, ASO keywords, Meta ads, thousands of scraped App Store complaints framed as opportunities.

The content formula: open with proof (a $100K/mo app) inside the first 15 seconds, tear it down, rebuild it live, close on the tool CTA. Retention is bought with the proof, not the tutorial.
