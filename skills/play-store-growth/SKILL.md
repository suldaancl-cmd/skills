---
name: play-store-growth
description: Use when growing installs and revenue for an Android app on Google Play — running store listing A/B experiments, building custom store listings per country or audience, setting up pre-registration, publishing LiveOps events, tuning Play Store search keywords, or reading Play Console acquisition reports. This is the Play-side counterpart to Apple ASO skills, which do not transfer — Play indexes the full long description, allows real split-testing inside the console, and surfaces live events in the store. Reach for this when the ask is installs, conversion rate, or Play Store marketing rather than the build itself.
---

# Play Store Growth

Apple ASO advice does not transfer to Google Play. The two stores index different fields, allow different experiments, and reward different behaviours. Applying App Store keyword tactics to Play wastes the single biggest advantage Play gives you.

**Companion skills.** Release mechanics and policy gates → `play-console-mastery`. Rejections → `store-rejection-defense`. Apple-side ASO → `aso-router`, `app-store-optimization`.

## The core difference

| | App Store (Apple) | Google Play |
|---|---|---|
| Keyword source | A hidden 100-character keyword field | The **full long description** is indexed |
| Description indexed? | No | **Yes** |
| Split testing | Product Page Optimization, limited | **Store listing experiments**, native and generous |
| Audience variants | Custom Product Pages | **Custom store listings** by country, install state, audience |
| Live events in store | Limited | **LiveOps events** surfaced in the store |
| Pre-launch | Pre-orders | **Pre-registration** with rewards |

The headline consequence: **on Play, the long description is marketing copy AND the keyword field at the same time.** Writing it as pure prose wastes ranking surface; writing it as a keyword dump reads as spam to humans and can trip policy. It has to do both jobs.

## Listing fields and how to use each

| Field | Ranking weight | How to write it |
|---|---|---|
| **App name** (30 chars) | Highest | Brand plus the single strongest keyword. Not a keyword sentence. |
| **Short description** (80 chars) | High | The one-line pitch shown before "read more". This is the conversion line — write it for a human, fit one keyword naturally. |
| **Long description** (4000 chars) | High, fully indexed | Front-load the primary keyword in the first two lines. Repeat core terms naturally 3–5 times across the body. Use short paragraphs and headers — most readers skim. |
| **Icon** | None directly | Drives tap-through, which drives ranking indirectly |
| **Feature graphic** | None directly | Shown above screenshots and in promos; often the first thing seen |
| **Screenshots** | None directly | The main conversion asset |
| **Promo video** | None directly | Optional; test it, do not assume it helps |

Keyword stuffing is a real policy risk under deceptive-behaviour and spam rules. The safe pattern is natural repetition inside genuinely useful copy.

## Store listing experiments — the biggest lever

Play lets you A/B test store listing assets natively, with real traffic and statistical reporting. Most developers never turn this on. That is free conversion left on the table.

What you can test:

- App icon
- Feature graphic
- Screenshots
- Short description
- Long description
- Promo video

How to run them properly:

1. **Test one variable at a time.** Testing icon and screenshots together tells you nothing about which moved the number.
2. **Start with the icon.** It is the highest-leverage single asset because it affects every impression, including search results and browse.
3. **Give it enough traffic.** Low-traffic apps produce noise. If the confidence interval never tightens, the app is too small to split-test that asset — improve it by judgement instead and revisit later.
4. **Let it run to significance.** Stopping early on a promising trend is how teams ship worse assets with confidence.
5. **Run the winner, then test the next variable.** Compounding small wins beats one redesign.
6. **Re-test seasonally.** A winner from a year ago is not a permanent winner.

Order of testing, highest expected value first: icon → first screenshot → short description → feature graphic → long description → video.

## Custom store listings

You can serve **different listings to different audiences** — up to a substantial number of variants. This is the localisation and targeting lever.

Segment by:

- **Country / language** — the obvious one, and the one most under-used
- **Install state** — users who have never installed vs lapsed users who uninstalled
- **Pre-registration** audience
- **Inactive users** — a win-back listing with a different pitch

The highest-return use for a MENA-facing app: **a genuinely Arabic listing, not a machine-translated one.** Most competitors in the region ship English-only or auto-translated listings, which reads as foreign and converts badly. A native Arabic short description, Arabic screenshot captions, and an Arabic long description is a real, defensible edge in an under-served market.

Screenshot captions must be localised too. Localising the text fields but leaving English screenshots is the most common half-done job.

## Pre-registration

Available ahead of launch, for a limited window.

- Users who pre-register are **auto-notified** at launch, and can be set to auto-install.
- Pre-registration rewards (an in-game item, a trial, unlocked content) materially lift sign-ups.
- The value is a **launch-day install spike**, which feeds the ranking signal at exactly the moment ranking is most malleable.

Use it when launch timing is controllable and there is any audience to point at it. Skip it if the app is already live or there is no audience yet — a pre-registration page with no traffic is just a delay.

## LiveOps events

Play surfaces time-bound events directly in the store — sales, new content, tournaments, major updates.

- Reaches both existing users (re-engagement) and browsers (acquisition).
- Eligibility depends on app category and standing; games get the richest treatment but non-game apps can use them.
- The discipline is a **content calendar**, not a one-off. Events work when they recur.

## Reading the Play Console reports

The reports that actually change decisions:

| Report | What it answers |
|---|---|
| **Store performance / acquisition** | Where installs come from — search, browse, third-party referral |
| **Store listing conversion rate** | Of people who saw the listing, how many installed |
| **Search terms** | Which queries brought people in — the closest thing Play gives to keyword data |
| **Retention** | Day 1 / 7 / 30 — the metric that decides whether growth compounds or leaks |
| **Android vitals** | Crash and ANR rates that can silently suppress discoverability |

The diagnostic split that matters:

- **Low impressions** → a discovery problem. Fix keywords, listing copy, and category.
- **High impressions, low conversion** → an asset problem. Fix icon and screenshots via experiments.
- **High installs, low retention** → a product problem. No listing change fixes it, and chasing installs on a leaky product just burns money faster.

Diagnose in that order. Teams routinely redesign screenshots when the actual problem is retention.

## Ratings and reviews

- Use the **in-app review API** rather than a custom "rate us" dialog. It is less intrusive and does not violate policy.
- Prompt after a **success moment**, never on launch or mid-task.
- **Never incentivise ratings.** Paying for or rewarding reviews is a policy violation with severe consequences.
- **Reply to reviews.** Replies are public, visible to future readers, and users often revise a low rating after a real response.
- Ratings are a ranking input and the strongest conversion factor on the listing page.

## Growth checklist

1. App name carries brand plus one strong keyword within 30 characters.
2. Short description reads as a human pitch and lands one keyword.
3. Long description front-loads the primary keyword and repeats core terms naturally.
4. At least one store listing experiment running, testing a single variable.
5. Custom store listings created for every meaningful market — with localised screenshot captions, not just translated text fields.
6. In-app review API wired to a success moment.
7. Review replies part of a weekly routine.
8. Android vitals inside thresholds, so growth work is not fighting a suppression penalty.
9. Retention measured before spending on acquisition.

## Verification

Before reporting Play growth work as done, point to:

- the experiment dashboard showing a running or concluded test with its confidence interval
- the store listing conversion rate before and after
- the search terms report showing the targeted keywords actually appearing

An untested listing change is a hypothesis, not a result. Label it as such.
