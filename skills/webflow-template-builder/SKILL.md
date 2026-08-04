---
name: webflow-template-builder
description: Build a Webflow (or Framer) template designed to pass marketplace review and sell — required pages, Client-First class discipline, CMS structure, legal-vs-illegal interaction tech, submission checklist, and exactly which scroll/micro-interaction patterns to ship. Invoke whenever the user wants to build, audit, or price a template for the Webflow Template Marketplace (or an equivalent Framer template).
---

# Webflow Template Builder

Building a template is not building a website. A website only has to look good. A template has
to pass a graded rubric, survive a QA reviewer looking for reasons to reject it, and then get
picked out of thousands of near-identical thumbnails by a buyer scrolling for three seconds.
Every decision below is filtered through that lens.

Read the reference files as you reach each step — they carry the concrete values, the exact
build recipes, and the source citations. This file is the workflow and the gate-checks.

## Reference files

- `reference/submission-and-economics.md` — the compliance skeleton (required pages), the
  grading rubric's hard numbers, rejection landmines, the fixed price ladder, category
  arbitrage data, and listing/thumbnail rules.
- `reference/design-system-and-cms.md` — class-naming discipline (Client-First), Variables/Modes,
  Components (props/slots/variants), and CMS collection architecture.
- `reference/motion-legal-guide.md` — the single most consequential decision in a template build:
  which interaction tech is marketplace-legal in Webflow vs. Framer, plus ranked, sourced build
  recipes for the scroll and micro-interaction patterns worth shipping.

## Workflow

**1. Pick the platform and the niche before anything else.**
Webflow's marketplace sets fixed prices by feature tier and grades a strict rubric; Framer sets
no prices, does no manual review, and allows real custom code. If the concept depends on
WebGL/Rive/Three.js/velocity-reactive JS, it belongs on Framer or as an off-marketplace
cloneable — not a Webflow marketplace submission. See `motion-legal-guide.md` for the full
legality table before you commit to a "wow" effect you can't ship. Then pick a category — niche
verticals (Real Estate, Wellness, Home Services, Medical) out-rank saturated ones
(Portfolio & Agency, Technology) for sustained visibility. See the category table in
`submission-and-economics.md`.

**2. Decide the price tier you're building toward, and build to it.**
Webflow prices are fixed by a functionality checklist (CMS, Ecommerce, UI Kit, Memberships,
Multi Layout). Decide the tier up front — it determines whether you need a blog collection, a
UI-kit page set, or 3 layout variants of Home/About/Pricing — because retrofitting CMS or
Multi Layout after the static pages are built is the expensive way to do it. Table in
`submission-and-economics.md`.

**3. Build the design system before any page.**
One class-naming system for the whole project (Client-First is the de facto standard buyers
already know how to edit). Colors, type scale, and spacing as Webflow Variables with Variable
Modes per breakpoint. This is graded, and it's the #1 thing that makes a template feel
"finished" versus a one-off site. Details in `design-system-and-cms.md`.

**4. Build Navbar/Footer/CTA as Components first**, then assemble every section from them.
Components with props/slots/variants — never duplicate a nav across pages. Details in
`design-system-and-cms.md`.

**5. Wire the CMS.**
Any repeatable content (blog, projects, team, services, testimonials) becomes a Collection —
never a stack of static sections. 3-7 realistic dummy items per collection, dynamic SEO fields
wired to page settings, required/conditional fields set correctly. CMS is also what moves a
template up the price ladder. Details in `design-system-and-cms.md`.
**Ecommerce landmine:** never enter a real business address, shipping, tax, or payment info
into the project — doing so is irreversible and permanently disqualifies the template.

**6. Choose interactions from the legal list, ranked by sellability.**
Default to native Webflow Interactions (GSAP-powered as of May 1 2026 — this is now the
Marketplace default, legacy IX2 is discouraged). For the small set of effects that need a
script (character-split text, scroll-scrubbed video, smooth-scroll feel), the only
marketplace-safe custom code is a GSAP embed — document every animated selector and variable
on the Instructions page. Anything requiring a separate JS runtime (Three.js, Rive, Unicorn
Studio, Lenis, magnetic-button/cursor scripts) is not shippable in a Webflow Marketplace
template; substitute the native equivalent (Spline for 3D, Lottie for character animation, a
baked MP4 loop for a shader) or reserve it for a free cloneable outside the marketplace.
Full ranked pattern list with exact Webflow build steps in `motion-legal-guide.md`. Rule of
thumb from Webflow's own rubric: ship **1-2 signature "wow" moments**, not motion on every
element — more than that reads as "cognitive overload" and costs rubric points.

**7. Ship the compliance skeleton.**
Style Guide page (every tag styled), Instructions page (mandatory if using GSAP or hidden/
complex components — must list every animated selector, tweakable variable, and removal
step), Licenses page at `/licenses` with the required boilerplate + per-asset links, branded
404. All four get `<meta name="robots" content="noindex">`. Footer (as a Component, so it's
everywhere) links Licenses and includes "Powered by Webflow". Full requirements in
`submission-and-economics.md`.

**8. Run the pre-submission gate before calling it done.**
- PageSpeed: SEO 70-90+ and Accessibility 70-90+ minimum (90-100 SEO / 70-90 Performance for
  "Exceptional"). Total site weight under 10MB. Images compressed, WebP/AVIF, explicit
  width/height or aspect-ratio boxes, lazy-load below the fold.
- One H1 per page, no skipped heading levels, WCAG contrast including hover/focus/active states.
- Unique meta title (<60 chars) + description (150-160 chars) + 1200x630 OG image per page,
  including CMS templates.
- Naming: template name is 1-2 words, no lorem ipsum anywhere, thumbnail shows the homepage
  clean, hover-thumbnail shows a different section in the same tone.
- Zero custom code beyond the documented GSAP embed + the standard noindex/font-smoothing
  exceptions. Zero empty links. No real ecommerce data entered.
- 5+ failed requirements = outright rejection (doesn't count toward submission quota) — so
  this gate is the difference between a wasted submission slot and a live listing.

Full rubric numbers and rejection specifics are in `submission-and-economics.md`.

## The one decision that breaks templates most often

Every "amazing effect I saw on Awwwards" question reduces to: **is this native Webflow
Interactions, a GSAP embed, or does it need its own JS library?** Only the first two are
marketplace-legal for a Webflow template. Check `motion-legal-guide.md`'s legality table before
promising a client or a template concept any specific motion effect.
