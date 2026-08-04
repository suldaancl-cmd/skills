---
name: ayzz-web-design-method
description: >-
  The complete web-design method of Abdul Mutakabar Ayaz (@ayzz.thedesigner) — a
  264K-follower UI/UX designer/agency owner known for cinematic, editorial,
  "quiet-luxury" brand websites: designed in Figma, imagery AI-generated with the
  Higgsfield plugin, and shipped ~90% on Webflow + GSAP + Lenis + Barba.js. Use
  this whenever you are designing or art-directing a brand/product website or
  landing page (candle, skincare, supplement, coffee, fashion, premium DTC/SaaS),
  choosing the fonts + color palette for a site, building a hero, planning a
  sitemap, deciding motion / 3D, picking a build stack for a premium site, or when
  the user references "ayzz", "the designer", "that Instagram designer's style",
  "cinematic website", "editorial web design", or wants a site that "feels
  premium" instead of flat card layouts. Also use to critique a web design against
  a premium bar. Reach for this BEFORE writing layout code or CSS — the method
  front-loads understanding + a Colors & Fonts decision that change everything
  downstream.
metadata:
  type: reference
  source: "Primary analysis of @ayzz.thedesigner reels, build videos, and a process explainer (transcribed), June 2026"
---

# The ayzz.thedesigner Web Design Method

Abdul Mutakabar Ayaz (**@ayzz.thedesigner**, ~264K followers, agency **@zz.studio.design**, also on Dribbble/YouTube) designs brand websites that feel cinematic and expensive — the opposite of flat, tidy card layouts. This skill captures his repeatable method, aesthetic, and exact tooling, reverse-engineered from his build videos (VELOUR candle, CALMM supplements, Axirya skincare, a "Fresh Beans" coffee brand), his font reels, and a process explainer where he narrates the whole pipeline.

Use it to art-direct and build premium brand sites, or to judge whether a design clears his bar.

## The one idea behind everything

**Design to a *feeling*, not a feature list.** Every project he starts by restating the brief as a mood ("warm, atmospheric, editorial — the kind of site you linger on"), then makes every decision — type, color, imagery, motion — serve that mood. A site that just lists products in neat cards has no feeling. His sites have a feeling first, products second.

This is why the method front-loads understanding and atmosphere before any layout. Lock the feeling and the layout almost designs itself; skip it and you get generic AI slop.

## The workflow (his actual pipeline, in order)

The ordering is the point — most weak web design jumps straight to layout. In his words: *"Before we design anything, we just try to understand a few simple things."*

### 1. Understand — three questions
Before opening any canvas, answer:
1. **What is the brand about?**
2. **What does the website actually need to achieve?** (the business goal)
3. **What is the user supposed to *do*** on the site? (the one action)

Then restate it as a **mood statement** in the brand's voice — pull the sensory/emotional words forward. *"Luxury scented candle brand. Hand-poured, slow-burning. Warm, atmospheric, editorial, moody light. The kind of site you linger on."* If the brief is a feature list, translate it into a feeling first.

### 2. Sitemap
Decide the pages, **what goes on the homepage, and what actually deserves attention.** Structure before surface. He does this in Figma/FigJam.

### 3. Research & gather
A little **competitor research**, **get help from AI**, and **collect all assets** — branding, visuals, everything — into one place. You're matching a target mood, not designing blind.

### 4. Colors & Fonts deck FIRST — the signature move
**Before any layout, lock the type + color system on its own frame.** He always opens a "Colors & Fonts" frame with a giant `Aa` specimen and the palette swatches. Nothing gets composed until this is decided.

Why first: type and color *are* ~80% of the mood. Decide them in isolation and every section inherits a consistent feeling; decide them mid-layout and you fiddle forever and drift generic. See [references/typography-and-color.md](references/typography-and-color.md) for his exact fonts (tall condensed display + elegant serif) and mood→palette logic.

### 5. Design in Figma — cinematic & editorial
Compose the screens in Figma with his signature layout moves (full-bleed hero, **giant wordmark**, product-as-hero, big editorial copy, dark-cinematic → light-calm rhythm). Generate **all imagery with AI in-canvas** via the **Higgsfield Figma plugin** — hero, product shots, alternate angles, atmospheric scenes, even a promo video, *all from one product photo*. Full layout + imagery reference: [references/imagery-and-layout.md](references/imagery-and-layout.md).

Get the **conversion copy** right here too — headline, hero visual, CTA, and trust signals follow specific rules: [references/conversion-copy.md](references/conversion-copy.md).

### 6. Decide motion, then build a motion prototype
Explicitly decide: **do we need 3D here, is 2D enough, and where does motion actually add value?** Then make a **motion prototype** (in Figma, sometimes After Effects). That one prototype does three jobs:
1. **Shows the client** how the site will behave once built.
2. Becomes **portfolio / Instagram content**.
3. Is a **clear reference for the developer** — "we don't need to explain every animation, we just send the video."

This is a high-leverage habit: one artifact sells the work, markets the work, and specs the work.

### 7. Build — his real stack
He's candid that you **don't need heavy front-end experience**:
- **~90% Webflow** — handles layout, responsiveness, and base interactions.
- **GSAP** — "basically the standard" for scroll-based animation and transitions.
- **Lenis** — smooth scrolling.
- **Barba.js** — page transitions.
- **Fake 3D, mostly** — "a lot of the 3D-looking stuff isn't actually 3D; it's smart use of 2D, WebP files and videos with depth and motion." Add **real 3D only when it makes sense for the brand.**

If you're coding from scratch instead of Webflow, keep the same spirit: one strong type system, one tight palette, real cinematic imagery, and restrained motion (GSAP + Lenis covers most of it). This matches Karim's standing premium-web stack note (GSAP ScrollTrigger + Lenis, optional 3D/WebGL).

## Aesthetic signatures (the "ayzz look")
- **Type:** tall condensed display (Druk, Theater Cond, Moho Cond) for impact + elegant serif (Pandory) for luxury. Wordmark set huge as a graphic element.
- **Color:** one tonal palette pulled from the brand's mood/product; strong color-blocking; dark cinematic hero vs. clean off-white product sections.
- **Imagery:** cinematic, moody, atmospheric, dramatically lit. Quiet luxury. Never flat stock cutouts in the hero.
- **Copy:** short, confident, editorial — adjective triplets ("Powerful. Pure. Gentle."), bold claims ("Radical Transparency. Hide Nothing.").
- **Motion:** restrained and purposeful (his hook "your websites are too animated" is the tell). Scroll reveals, parallax, smooth scroll — not a tech demo.

## How to judge a design against his bar
1. Does it have a **feeling** in the first second, or is it just neat boxes?
2. Is there a **giant wordmark / display-type moment** anchoring the hero?
3. Is the imagery **cinematic and atmospheric**, or flat stock/cutouts?
4. Is the **palette tonal and mood-matched**, or default blue-grey?
5. Does the hero **lead with the product/result and a real benefit headline**, with trust signals up top? (see conversion-copy)
6. Is motion **restrained** and purposeful?

If it reads as a tidy card grid on a white page, it has failed his bar — push it toward atmosphere. (Matches Karim's standing note that flat card-on-panel layouts are "so bad".)

## References
- [references/typography-and-color.md](references/typography-and-color.md) — his font library (Druk, Theater Cond, Moho Cond, Pandory + free-font picks), pairing logic, mood→palette table, banned defaults.
- [references/imagery-and-layout.md](references/imagery-and-layout.md) — the Higgsfield one-photo→full-site imagery workflow, imagery direction, and section-by-section layout patterns with per-project examples.
- [references/conversion-copy.md](references/conversion-copy.md) — his landing-page conversion rules: headline, hero visual, CTA, and trust-signal placement (do-this-not-that).

## Related skills to chain
- Imagery step → `higgsfield-product-photoshoot`, `higgsfield-generate`, `ai-image-director`.
- Build/motion → `gsap`, `gsap-scrolltrigger`, `lenis-smooth-scroll`, `barba-js`, `webflow-premium-motion`.
- Type/color execution → `font-pairing-local`, `color-system`, `ui-ux-pro-max` (lock a design system).
- Content side (turning a build into reels) → `ayzz-design-reel-formula`.
