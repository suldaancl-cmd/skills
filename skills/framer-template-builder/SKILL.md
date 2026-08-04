---
name: framer-template-builder
description: Build a Framer template designed to pass marketplace review and sell — component/variant architecture, CMS structure, native-effect vs code-override decisions, and exactly which scroll/micro-interaction patterns to ship. Invoke whenever the user wants to build, audit, or price a Framer template for the Framer Marketplace.
---

# Framer template builder

A Framer template only sells if it clears two bars at once: Framer's own published quality checklist (self-audited, since Framer does no manual review), and the "looks custom-built, not templated" bar buyers judge in the first 3 seconds of the live preview. This skill sequences both.

Full detail lives in three linked files — read them at the point noted, don't front-load all three:

- `component-architecture.md` — shared styles, variants, CMS collections, breakpoints, native-vs-code decision order. Read before building anything.
- `patterns.md` — every scroll/motion/hover pattern with exact Framer build steps, a real example site, and a sellability score. Read when choosing which effects to ship.
- `marketplace.md` — self-audit checklist, pricing bands, listing craft. Read before submission.

## Build order

1. **Lock the style system first.** Text Styles + Color Styles for every heading level, body size, and brand/neutral/state color, before a single section is built. This is graded directly by Framer's requirements and is the #1 support-ticket reducer. → `component-architecture.md`
2. **Build the CMS structure.** Every repeatable content type (team, testimonials, case studies, FAQ, blog, pricing tiers if they vary) becomes a collection with human-readable field names, before content gets hand-duplicated into frames. → `component-architecture.md`
3. **Build components as variants**, not one-off frames — cards with hover variants, pricing cards with Monthly/Yearly variants, nav links with hover-underline variants. Bind CMS fields into variants so cards restyle per category automatically.
4. **Layer motion, native-first.** Work down the decision order in `component-architecture.md` (native Effects panel → code override → bundled code component → baked media) and pick patterns from the ranked list below / `patterns.md`.
5. **Self-audit against the marketplace checklist**, then write the listing. → `marketplace.md`

## Native effects vs. code — the one decision that shapes everything else

Framer's marketplace does **no manual review** and explicitly **permits clean code components**. This is the single biggest structural difference from Webflow (whose marketplace bans custom code in templates outright), and it's why several rich-media and interaction patterns below are sellable in a Framer template specifically:

| Tier | Use for | Examples |
|---|---|---|
| 1. Native Effects panel | The majority of motion — zero code, safest, fastest | Appear/split-text, Scroll Transform, Scroll Speed, Scroll Variant, Ticker, Cursors, Lottie/Spline/video components |
| 2. Code override on existing layer | Behavior a native slider doesn't expose | Magnetic buttons, drag physics, velocity-reactive ticker, horizontal-scroll-from-vertical-scroll |
| 3. Bundled code component w/ property controls | One signature/bespoke effect, buyer-tunable via sliders in the properties panel | WebGL hero (Unicorn Studio/Three.js), Rive state machine |
| 4. Baked media substitute | Effect too heavy/custom to hand to buyers | Record once as MP4 loop or Lottie instead of a live shader |

Full reasoning and the variant-transition limitation (single property transition per variant pair) in `component-architecture.md`.

## Ranked pattern shortlist (full build steps in `patterns.md`)

Ship 5-8 of these per template, not all of them — the research is explicit that bestsellers each lead with ONE clearly named feature (a preloader, a pricing page, advanced CMS, a customizable hero), not a feature-tour. Pick one signature effect for the marketplace-grid thumbnail and build the rest as the supporting baseline.

**Baseline (ship on every template, all native, no code):**
- Native split-text Appear (char/word/line stagger) — 10/10. The zero-cost baseline; its absence is what makes a template feel "dead" (Xtract, Billie).
- Overflow-clip hover zoom + caption slide-up on cards — 10/10. Works with any buyer content (Pesquera Diez, Duten).
- Aurora/blur-morph gradient background — 10/10. Recolors to any brand in 3 hex values (Linear, Resend, Cursor, Raycast).
- Infinite logo/testimonial ticker — 10/10, native Ticker component (Vectura, Saalix).
- Sticky stacking cards — 10/10, native Sticky + Scroll Transform (marketplace components sell this standalone at $12).

**Signature / hero-thumbnail candidates (pick one):**
- Preloader-on-every-page — 9/10 (Nakula, $129 bestseller).
- Pinned scrollytelling product tour — 9/10 (Apple iPad Pro, Fey, Linear).
- Zoom-scrub media hero — 9/10, one of the few "expensive" effects Framer does fully native (Sticky Zooming, $14 component).
- Customizable code-component hero (WebGL/particle via Unicorn Studio) — 8/10. Justifies the $129-149 pricing band on its own (Jet).
- Interactive Spline 3D hero — 8/10, native Spline component (THREE DIMENSIONS, FlowDrinks, Nike 360).

**Structural, not optional:**
- CMS-everything architecture — 9/10, directly graded by Framer's own checklist (Nitro, Nord-Å, Mugen).
- SaaS pricing-section craft (toggle + highlighted tier) — 9/10, native variants (Vectura's headline feature).

**Niche/lower-priority:**
- Magnetic buttons — 7/10, needs a code override.
- Playful drag/physics — 6/10, consumer/fun niches only, needs a code override.
- Rive state-machine character — 6/10, customizes poorly for average buyers, ship a Lottie fallback.

## Marketplace self-audit (before every submission)

- Shared Text/Color Styles used throughout — no one-off overrides.
- Custom 404 page (not Framer default).
- Zero lorem ipsum.
- CMS fields human-named; empty/placeholder entries deleted.
- Real `mailto:`/`tel:` links, not dead anchors.
- Alt text on every image.

Full pricing bands, listing craft, and the Webflow-vs-Framer legality gap (why WebGL/Rive/drag are sellable here but banned there) in `marketplace.md`.

## Common failure modes this skill exists to prevent

- **Building the hero effect before the style system.** Buyers restyle by editing 8-12 shared styles; skipping this means every future edit touches hundreds of individual layers instead.
- **Hand-duplicating repeatable content instead of using CMS.** Directly graded by Framer's checklist and the #1 thing that makes a template feel un-editable to a non-designer buyer.
- **Shipping every pattern in `patterns.md` at once.** Bestsellers sell on ONE named feature; a kitchen-sink template reads as unfocused in a 3-second preview scroll, not more premium.
- **Reaching for a code component when a native Effect already covers it.** Check the native-first decision order before writing an override — most of the 10/10-sellability patterns above are zero-code.
- **Forgetting the variant-transition limit.** A component variant pair animates one transition per property; effects needing an asymmetric enter/exit (underline that exits from the opposite origin, exit animations 30-50% faster than entrances) need a code override or custom CSS, not a third variant.

skipped: a full Framer-file starter/boilerplate — this skill is a build guide, not a shipped .framer file; add one when a specific template project needs a reusable starting point.
