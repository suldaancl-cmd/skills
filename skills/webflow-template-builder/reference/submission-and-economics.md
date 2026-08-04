# Submission Requirements & Template Economics

Source beat: Webflow Made-in-Webflow showcase, Template Marketplace bestsellers, submission
guidelines, and grading rubric (140 sites covered).

## The compliance skeleton (hard gate)

Every accepted template ships 3-4 hidden utility pages. Skip these and you risk outright
rejection.

- **Style Guide page** — every styled HTML tag on one page: H1-H6, paragraphs, lists,
  blockquotes, links, buttons, figures. This is also how buyers restyle the whole template in
  minutes (drives reviews and repeat purchases).
- **Instructions page** — mandatory if the template uses GSAP or any complex/hidden component.
  Must include a "How to Edit GSAP Animations" section: every animated selector, every tweakable
  variable (duration, ease, ScrollTrigger start point), and removal steps.
- **Licenses page** at slug `/licenses` — exact required boilerplate text plus a link for every
  licensed asset used.
- **Branded 404** — full nav and CTAs, not a bare error message.
- All four utility pages carry `<meta name="robots" content="noindex">`, use Title Case page
  names matching their slugs, and the footer (build it as a Component) on every page links to
  Licenses and includes "Powered by Webflow".

Reference: Webflow Submission Guidelines (Required Pages section) —
https://webflow.com/templates/submission-guidelines · Juniper by Elemis (official single-page
reference template) and Brick by Ragebite (official multi-page reference) —
https://webflow.com/templates/grading-rubric

## Grading rubric — hard numbers

- **Conversion design** is explicitly graded: CTAs must be "ubiquitous, placed in high-traffic
  locations such as the nav menu or homepage hero, stand out, and repeat appropriately."
  "Exceptional" requires intentional space for credibility, lure, objection-handling, social
  proof, ease-of-use, and results data. Every link must go somewhere — empty links are a
  requirements failure. Reference: Innoflow (ranked #1 SaaS template 2026) —
  https://www.flowsamurai.com/post/top-webflow-templates-for-saas-startups-ranked-2026 ·
  Kinetiq (B2B SaaS, trust-focused structure) — same source · Webflow Grading Rubric
  (Conversion best practices row) — https://webflow.com/templates/grading-rubric
- **Performance/accessibility budget** (pass/fail, not taste): "Good" = PageSpeed SEO 70-90,
  Accessibility 70-90; "Exceptional" = 90-100 SEO / 70-90 Performance. Site weight <10MB, images
  compressed (≤150KB target, 4MB hard max), WebP/AVIF, lazy-load below-fold, eager above-fold,
  explicit width/height or aspect-ratio boxes to prevent layout shift, minified CSS, Google/OFL
  fonts only (no Typekit/custom fonts), one H1 per page with no skipped heading levels, WCAG
  contrast including focus/hover/active states, unique meta title <60 chars + description
  150-160 chars + 1200x630 OG image per page including CMS templates. Reference: Webflow
  Grading Rubric (Site optimization + Accessibility rows) and Submission Guidelines (SEO /
  Accessibility / Images sections) — https://webflow.com/templates/grading-rubric ·
  https://webflow.com/templates/submission-guidelines
- **"Exceptional" UX bar is precise, not vague**: "an innovative wow factor or two without
  creating confusion" — i.e. 1-2 signature motion moments per template, not wall-to-wall
  animation. Treat this as a spec, not a suggestion.

## Rejection landmines

- **Ecommerce address is irreversible.** Entering a business address in a Webflow template
  project permanently disqualifies it from the marketplace. Every Ecommerce Setup Guide step
  (address, shipping, tax, payment, hosting, checkout) must stay unchecked.
- **5+ failed requirements = outright rejection** — doesn't count toward the submission quota.
  Fewer failures still get flagged with reviewer feedback and a revision round — effectively a
  free expert audit once you've internalized the checklist (source: Bryn Taylor's templates 2
  and 3 went submitted→approved with zero comments once he'd learned it —
  https://www.bryntaylor.co.uk/writing/selling-webflow-templates).
- **Custom code is banned except the documented GSAP exception** — see
  `motion-legal-guide.md` for exactly what that covers.
- **Naming rejects**: 1-2 words (prefer 1), unique, theme-relevant, no keyword stuffing, no
  brand/author name, no slang or odd caps.
- **Class-naming inconsistency** is a QA flag — pick one system (Title Case default,
  snake_case, Pascal, camel, kebab, BEM, or a named framework like Client-First) and use it
  everywhere.

## Fixed price ladder (Webflow sets the price, not the seller)

| Tier | Price | What it requires |
|---|---|---|
| One-page, no CMS | $24 | — |
| One-page CMS / multi-page no-CMS | $34 | one CMS collection or 2+ static pages |
| Multi-page CMS | $49 | CMS + multiple pages |
| CMS + Ecommerce, or CMS + UI Kit | $79 | — |
| Memberships | $99 | — |
| CMS + Ecommerce + UI Kit | $129 | — |
| Everything + multiple page variations (Multi Layout) | $149 | 3+ layout variations across 3 static pages (e.g. 3 Homes, 3 Abouts, 3 Pricings) |

Sellers earn a flat 80% commission. Featured/new templates on the marketplace homepage cluster
at $79-$169. Because a CMS collection turns a $24 template into a $34 one for roughly an hour of
extra work, **always include CMS**. Reference: Reader X by BRIX Templates ($129, Multi Layout),
Atlantic by Azwedo (official Multi Layout reference), LeadCraft by Ink Studio ($169 featured) —
https://webflow.com/templates/search/best-seller · https://webflow.com/templates/grading-rubric
· https://webflow.com/templates · Bryn Taylor pricing-tier breakdown —
https://www.bryntaylor.co.uk/writing/selling-webflow-templates

BRIX bundles the Figma source file with every $169 template — the single most copied
differentiator among top studios, and it costs nothing extra if you design in Figma first.
Reference: https://brixtemplates.com/

## Category arbitrage (live counts, July 2026)

Saturated (avoid as primary category): Portfolio & Agency 7,045, Technology 5,965.
Mid-density money niches: Wellness 720, Home Services 631, Food & Drink 648, Real Estate 498,
Medical 483, Professional Services 2,568, Retail & E-Commerce 1,123, Blog & Editorial 955.
Underserved: Transportation 175, Weddings & Events 175, Music & Audio 139, HR & Hiring 122,
Documentation 85, Launch & Coming Soon 55, Government 46.

A template in a 46-item category sits on page one indefinitely; the same template in Portfolio
& Agency is buried within days of leaving the "New" shelf. Pick up to 2 categories at
submission — content must genuinely fit ("content aligns with the primary tag" is a rubric
check). Use realistic niche dummy copy and niche-correct CMS collections (e.g. Treatments,
Practitioners, Locations for a clinic) — no lorem ipsum anywhere.

Reference: Dentalflow by BRIX Templates — https://brixtemplates.com/ · Webflow Templates
category index — https://webflow.com/templates/search/best-seller · Flowsamurai top-selling
categories analysis —
https://www.flowsamurai.com/post/top-selling-webflow-template-categories

Only 93 free templates exist across a ~7,427-template marketplace — one polished free template
gets outsized visibility in the Free filter and works as a zero-support-cost (community support
only, required) top-of-funnel for a paid catalog.

Webflow runs sitewide 50%-off promos visible on every marketplace page — sellers absorb this at
their 80% commission, an argument for also selling via an owned fulfillment link/store.

## Listing-card optimization

- Name: 1-2 words (1 preferred), unique, theme-relevant (e.g. "Orbit" for space, "Haven" for
  wellness), no keyword stuffing, no brand/author name, no slang/odd caps.
- Main thumbnail: homepage shown cleanly, no angled/tiled mockups.
- Second thumbnail (the hover state): a *different* section/page in the same visual tone — no
  badges, tool icons, category text, or CTAs overlaid.
- Design the hero to read at thumbnail scale: oversized display type, high contrast — the card
  is the entire top of funnel; buyers scan hundreds of same-size cards and the hover-swap is the
  only "demo" most will see before clicking.

Reference: ORIGIN Studio by Rick Mummery ($129 featured), Helios Solar by 108 Supply ($129
featured) — https://webflow.com/templates · Webflow Submission Guidelines (Template listing
information) — https://webflow.com/templates/submission-guidelines
