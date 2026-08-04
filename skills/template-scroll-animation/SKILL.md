---
name: template-scroll-animation
description: Scroll and motion recipe book for building SELLABLE Webflow/Framer templates — ranked recipes with real example sites, sellability scores, exact Webflow/Framer build steps, and marketplace-legality notes. Invoke when building, pitching, or QA-ing a premium Webflow or Framer template, especially anything involving scroll effects, parallax, 3D/WebGL, Lottie/Rive, cursors, or preview-video wow factor.
---

# Template Scroll & Motion Recipe Book

Source: research audit of 110-120 award-gallery sites per beat (scrollytelling, WebGL/3D/rich-media, micro-interactions) plus the Webflow and Framer marketplaces. Use this to pick which effects go into a template, in what order, and how to build each one on each platform without breaking marketplace submission rules.

## The one rule that decides everything: marketplace code policy

**Webflow Marketplace templates ban custom code entirely** — no embeds, no site-settings scripts, no page-settings scripts (per `webflow.com/templates/submission-guidelines`). This kills every GSAP/Three.js/Lenis/Rive/canvas-scrub recipe *as a marketplace template* — those are cloneable-only (sold off-marketplace) or must be substituted with a native equivalent (baked MP4 loop, Spline embed, Lottie).

**Exception (2026):** Webflow acquired GSAP; Webflow Interactions are now GSAP-powered natively and become the default for Marketplace templates from May 1, 2026. This makes text-splitting, blur, stagger, and timeline-based reveals native — no embed needed — where they used to require one. Recipes below are flagged where this changed the calculus.

**Framer Marketplace does no manual review and explicitly allows clean code components.** Anything needing real code (Rive runtime, Three.js/Unicorn Studio shaders, magnetic buttons, velocity-reactive tickers, cursor-follow trails) is legitimately shippable in a Framer template and not in a Webflow one. If a concept depends on code-driven motion, build it Framer-first and sell the Webflow version only as a cloneable.

Legend used below: **N** = fully native, no code, marketplace-safe on both platforms · **P** = native for the basic version, custom code needed for the premium version · **C** = requires custom code (Webflow: cloneable-only; Framer: shippable as a code component).

## Master ranked list (by sellability, wow-per-effort)

| # | Recipe | Score /10 | Webflow | Framer | File |
|---|---|---|---|---|---|
| 1 | Overflow-clip hover zoom + caption slide-up | 10 | N | N | micro-interactions.md |
| 1 | Sticky stacking cards | 10 | N | N | scroll-recipes.md |
| 1 | Scroll-scrubbed text reveal (line/word/char) | 10 | P (native from May 2026) | N | scroll-recipes.md |
| 1 | Kinetic typography reveal (blur+stagger) | 10 | P (native from May 2026) | N | motion-3d-recipes.md |
| 1 | Aurora / blur-morph gradient background | 10 | N | N | motion-3d-recipes.md |
| 6 | Pinned section, content swap (scrollytelling) | 9 | N | N | scroll-recipes.md |
| 6 | Zoom-scrub media hero (framed → full-bleed) | 9 | N | N | scroll-recipes.md |
| 6 | Section wipes / curtain overlaps | 9 | N | N | scroll-recipes.md |
| 6 | Scroll marquee / velocity ticker | 9 | P | N (base) / P (velocity) | scroll-recipes.md |
| 6 | Scroll-scrubbed Lottie hero/diagram | 9 | N | N (scrub needs small override) | motion-3d-recipes.md |
| 6 | Parallax depth stack (multi-speed layers) | 9 | N | N | motion-3d-recipes.md |
| 6 | Scroll-driven product tour (pinned steps) | 9 | N | N | motion-3d-recipes.md |
| 6 | Cursor-following image/video preview on list hover | 9 | P | C | micro-interactions.md |
| 6 | Marquee/ticker bands with hover-pause | 9 | N (CSS loop) / C (velocity) | N | micro-interactions.md |
| 15 | Horizontal scroll driven by vertical scroll | 8 | N | C | scroll-recipes.md |
| 15 | Multi-layer parallax hero | 8 | N | N | scroll-recipes.md |
| 15 | Lenis-style smooth scroll + inertia | 8 | C | C | scroll-recipes.md |
| 15 | Staggered grid/image reveal on scroll | 8 | N | N | scroll-recipes.md |
| 15 | Scroll-linked theme/background color morph | 8 | N | P | scroll-recipes.md |
| 15 | Interactive Spline 3D hero | 8 | N | N | motion-3d-recipes.md |
| 15 | Film grain / noise overlay | 8 | N | N | motion-3d-recipes.md |
| 15 | Infinite marquee + scroll-velocity text ticker | 8 | N (base) / C (velocity) | N | motion-3d-recipes.md |
| 15 | Video-first hero (full-bleed autoplay loop) | 8 | N | N | motion-3d-recipes.md |
| 15 | Blend-mode dot cursor with hover morph | 8 | P | P | micro-interactions.md |
| 15 | Full-screen wipe / mask page transitions | 8 | P | P | micro-interactions.md |
| 15 | Animated link underlines (draw-through, exit-right) | 8 | P (CSS embed for exit-swap) | P | micro-interactions.md |
| 15 | Character-split text on headings/links | 8 | C | N (appear) / C (hover ripple) | micro-interactions.md |
| 15 | Hover-to-play video cards | 8 | P | N | micro-interactions.md |
| 27 | Scroll-scrubbed video / image-sequence | 7 | C | C | scroll-recipes.md |
| 27 | WebGL shader hero (fluid/refraction/particles) | 7 | C — not shippable on marketplace | C — shippable | motion-3d-recipes.md |
| 27 | Cursor-reactive polish kit (magnetic + tilt) | 7 | P | P | motion-3d-recipes.md |
| 27 | Magnetic buttons / nav links | 7 | C | C | micro-interactions.md |
| 27 | Counter/curtain preloader | 7 | P (curtain) / C (counter) | P | micro-interactions.md |
| 27 | The premium easing recipe (expo-out, choreographed stagger) | 7 | N | N | micro-interactions.md |
| 33 | Rive interactive character / state machine | 6 | C — not shippable on marketplace | C — shippable | motion-3d-recipes.md |
| 33 | Image trail cursor effect | 6 | C | C | micro-interactions.md |

## How to use this for a template build

1. **Pick 5-7 recipes, not 20.** One hero effect (zoom-scrub or Spline or parallax), one scrollytelling section (pinned swap or sticky stacking cards), one ambient layer (marquee or grain+aurora combo), one micro-interaction pass (hover zoom + link underlines + easing recipe applied everywhere). More than that dilutes the preview video and bloats build time for no marketplace-score gain.
2. **Score-1 recipes first.** They are the highest sellability *and* fully native — lowest risk, fastest to build, safest to demo.
3. **Check the shippability column before committing to an effect.** If it's `C` on Webflow, decide up front: ship it as a paid cloneable off-marketplace, or substitute the native alternative named in the recipe (baked MP4 for WebGL, Lottie for Rive, canvas image-sequence swapped for a scroll-scrubbed Lottie/Spline scene).
4. **Preview video shot order should follow the ranked list**, highest score first — that's literally what buyers scroll-test in the first 5 seconds of a marketplace preview.
5. **Read `references/marketplace-rules-and-pricing.md` before pricing the template** — it has the arbitrage plays (Unicorn Studio, baked-WebGL substitution) and real marketplace price anchors for scroll-heavy templates.

## Reference files

- `references/scroll-recipes.md` — the 12 scrollytelling/parallax/scroll-scrub recipes, full Webflow + Framer build steps, performance notes.
- `references/motion-3d-recipes.md` — the 12 premium motion / 3D / rich-media recipes (Spline, Lottie, Rive, WebGL, grain, video hero), build steps + performance notes.
- `references/micro-interactions.md` — the 12 cursor / hover / marquee / transition recipes, build steps + performance notes.
- `references/marketplace-rules-and-pricing.md` — standout tricks, the Webflow-GSAP-acquisition shift, Unicorn Studio arbitrage, and real marketplace pricing anchors, with sources.
