---
name: template-marketplace-strategy
description: Business-layer strategy for selling Webflow and Framer templates — which marketplace, which niche, what price, how to list — grounded in July 2026 marketplace research. Invoke when the user wants to decide what template to build, price it, choose a marketplace, or write the listing (not for the design/motion craft itself — see webflow-premium-motion / web-design skills for that).
---

# Template Marketplace Strategy

The business layer for template sellers: what to build, where to sell it, what to charge, and how to make the listing convert. Pair this with a design-craft skill (`webflow-premium-motion`, `frontend-design`, `ui-ux-pro-max`) for the actual build — this skill only covers the go-to-market decisions.

All numbers below trace to the July 2026 research citations in this folder. Where the research has no number, this file says "unverified" rather than guessing — do not fill gaps with invented figures.

## Step 1 — Pick the marketplace

| | Webflow Template Marketplace | Framer Marketplace |
|---|---|---|
| Catalog size | 7,000+ templates, ~300 approved creators | 7.6K templates |
| Who sets price | Webflow (fixed tiers by feature checklist) | Creator sets it freely |
| Observed price range | $24–$169 | Free–$149 (median band $39–$99) |
| Commission | Conflicting figures in research — see note below | 0% (100% to creator) + up to 50% referral commission for 12 months on subscriptions via remix links |
| Exclusivity | None — Webflow's own designer page offers "fulfillment links to sell your templates anywhere" | None — no exclusivity clause in the Creator Program help doc |
| Review | Strict QA, detailed rejectable checklist | Publishes instantly, quality/originality checked after the fact |
| 2025 creator payouts | Not disclosed by Webflow in this research | $6.5M paid to creators in 2025, $753K in one November (framer.com/creators) |
| Buyer intent | Higher-intent, business-tool buyers | Higher velocity, faster listing, better for a volume + free-funnel strategy |

**Commission-rate conflict — flag before quoting a number to a buyer or client.** One part of the research states Webflow raised designer commission to 95% (Webflow keeps 5%, cut from 20% in Oct 2025 — banner live on webflow.com/templates/applications). A separate part of the same research says "sellers earn a flat 80% commission." Both cite Webflow's own submission/marketplace pages but were captured at different times or read different pages. **Do not state a commission rate as fact — check the current live page at webflow.com/templates/applications before it affects a pricing or go/no-go decision.**

**Default read:** Framer wins on economics + pricing control + listing velocity → build volume there and run the free-template funnel. Webflow wins on buyer intent and (if the 95% figure holds) commission — but you don't control price, so profit comes from climbing the feature-stack ladder (Step 3). Neither is exclusive, so the strongest move is porting one validated design to both (Step 5).

Full comparison detail: `reference-creator-economics.md`.

## Step 2 — Pick the niche (demand vs. supply)

The research gives hard category-count data (supply/saturation) for both marketplaces, but only **two** categories have actual search-volume-vs-supply numbers. Everything else below is a supply-gap signal (thin competition), not a confirmed-demand signal — treat accordingly and say so if relaying this to a client.

**Verified demand > supply (search volume + template count both known):**
- **Framer e-commerce**: 1,900 monthly searches vs ~110 templates, opportunity score 83 (temlis.com, Jan 2025) — the single strongest documented gap in the whole dataset.
- (Inverse case, avoid): Webflow "agency" — 90 searches vs 660 templates — confirmed oversupply, not just a hunch.

**Supply-gap only (thin category, demand unconfirmed by search data) — good candidates, verify local demand yourself before committing:**
Government (Webflow 46), Church (Framer 12), Political (Framer 16), Launch & Coming Soon (Webflow 55), Brand Guidelines (Framer 59), Documentation (Webflow 85 / Framer 131), Non-profit (Framer 72), Conference (Framer 72), HR & Hiring (Webflow 122), Membership (Framer 94), Music & Audio (Webflow 139), Wedding (Webflow 175 / Framer 81), Transportation (Webflow 175).

**Mid-density money niches (moderate competition, higher deal size / repeat-buyer potential — agencies buy these weekly):**
Medical (Webflow 483), Real Estate (Webflow 498), Home Services / local trades (Webflow 631 — see the roofing/solar pattern below), Food & Drink (Webflow 648 / Framer 242), Wellness (Webflow 720), Fashion (Framer 238), Travel (Framer 241).

**Saturated — avoid unless you have a genuine differentiator:**
Portfolio & Agency (Webflow 7,045 / Framer 2.7K), Technology (Webflow 5,965 / Framer 2.6K), Professional Services (Webflow 2,568 / Framer 3.9K), Landing Page (Framer 2K), Retail & E-commerce on Webflow specifically (1,123 — note this is the *opposite* signal from the Framer e-commerce gap; the same product category is saturated on one marketplace and starved on the other).

**The one deliberate exception to "avoid saturated categories":** AI/SaaS "agent-ready" startup templates sit inside the saturated Technology category yet are rated the top-performing sellability pattern in the research (score 10/10) — e.g. Fluence AI ($49, Framer, "500+ copies sold"). The keyword "AI" rides marketplace search independent of category crowding, and funded AI startups are the buyer pool with the most money and the least time. This is the one case where riding a hot keyword beats hiding in a quiet category.

Full ranked shortlist with sourcing: `reference-niche-shortlist.md`.

## Step 3 — Price it

**Framer:** you set the price directly. Observed distribution: free (funnel), $29–$79 (volume band — most trending templates), $129–$149 (flagship anchor). Ship one free portfolio template to farm remixes (top free templates show 300–612 remixes) for the referral-commission funnel, a $39–$79 volume line, and one $129+ flagship to anchor your profile's perceived quality.

**Webflow: price is NOT yours to set — it's assigned by a feature checklist.** Two versions of the ladder appear in the research (likely different snapshots of the same policy); use the more granular one when scoping a build:

| Tier | Price | What triggers it |
|---|---|---|
| 1 | $24 | One-page, no CMS |
| 2 | $34 | One-page + CMS, OR multi-page no CMS |
| 3 | $49 | Multi-page + CMS |
| 4 | $79 | CMS + Ecommerce, OR CMS + UI Kit |
| 5 | $99 | Memberships |
| 6 | $129 | CMS + Ecommerce + UI Kit |
| 7 | $149–$169 | All of the above + 3+ layout variations across 3+ static pages ("Multi Layout") |

The lazy profitable move: the same design effort roughly doubles from a $49 CMS template to a $129–169 Multi-Layout + Ecommerce + UI-Kit template. Feature-stack toward the top tier rather than shipping a bare single-page template. Full mechanics and worked examples: `reference-creator-economics.md`.

**Never enter a real business address into a Webflow Ecommerce template project** — the setup steps (address, shipping, tax, payment, hosting, checkout) are irreversible and permanently disqualify the template from the marketplace the moment any one of them is completed.

## Step 4 — Build the listing (title, thumbnail, description, proof)

1. **Name:** Webflow wants 1–2 words, unique, theme-relevant, no keyword stuffing, no brand/author name (Orbit, Haven — not "MyAgencyTemplate"). Framer bestsellers use "Coined Name · Niche Template" (e.g. "Fluence · SaaS & AI Agent Template") because the subtitle carries the searchable keywords.
2. **Thumbnail:** main image = clean homepage top, no angled mockups, no badges/icons/CTAs baked into the image. Second (hover) thumbnail = a genuinely different interior section in the same visual tone — this is the only "demo" most browsers ever see.
3. **Description first line:** repeat the niche + buyer types ("Perfect for founders, agencies, and SaaS teams…") — this text is what marketplace search indexes.
4. **Named-animation list:** spell out the motion by name ("scroll-triggered text reveal, infinite logo marquee, animated pricing toggle") — buyers can't feel your interactions from a static screenshot, so tell them.
5. **Sold-count proof line, once true:** neither marketplace shows public sales counts (Framer shows likes/remixes only), so sellers write the number into the copy themselves — Fluence AI's listing states "500+ copies sold" directly. Don't fabricate this number; add it only once verified.
6. **Figma file included:** costs nothing if you designed in Figma first, and both top Webflow and top Framer bestsellers headline it — raises perceived value without touching price.

Full listing playbook (naming rules, thumbnail specs, description templates): `reference-listing-craft.md`.

## Step 5 — Multiply the design (dual-listing, no exclusivity)

Neither platform requires exclusivity:
- Webflow explicitly provides "fulfillment links" so you can sell the same template on your own site or elsewhere.
- Framer's Creator Program help doc imposes no exclusivity clause.

Practical sequence: validate a design in one marketplace, then port it to the other as a second SKU (near-zero extra design cost, proven market). Webflow IX2/GSAP interactions map roughly 1:1 to Framer's native Scroll Transform / Appear effects, so porting is mostly a rebuild of the interaction layer, not a redesign. Sell an "all-access bundle" off-marketplace on your own site to capture AOV that a fixed-price marketplace listing can't (Webflow's preset tiers cap what you earn per sale there; your own site has no such cap).

## Reality check on creator earnings (don't oversell the opportunity)

- Framer: public creator stories range $2,291–$24,080+/month; one creator's total career earnings hit $100K (framer.com/creators). Cedric reports $4–7K/month (segmentui.com).
- Webflow: seller Zoya Qib reports ~$4,800 in year one (11 templates, 138 sales), then ~$10,750 in the next 7 months (167 sales) — a realistic ramp curve, not overnight income.
- Bryn Taylor: $430 in the first 12 days on one $49 portfolio template — a plausible floor for a single average template's early traction.
- Fluence AI's "500+ copies sold" at $49 implies roughly $24.5K gross on that one listing — before whichever commission rate actually applies (see the conflict noted in Step 1).

Treat these as a realistic range, not a guarantee — none of the research quantifies build-time investment, so cost-per-hour ROI is unverified.

## Reference files in this folder

- `reference-creator-economics.md` — full marketplace mechanics: commission conflict detail, full Webflow price ladder with worked examples, Framer pricing bands, referral-commission structure, all creator-earnings citations.
- `reference-niche-shortlist.md` — every category count on both marketplaces with sources, full saturated/gap/mid-tier breakdown, named example sites per niche.
- `reference-listing-craft.md` — naming rules, thumbnail specs, description copy patterns, social-proof tactics, Made-in-Webflow / free-template funnel mechanics, all with named example sites and sources.
