# Micro-Interaction & Cursor-Polish Recipes

12 patterns from an audit of 115 sites covering custom cursors, magnetic buttons, hover states, link underlines, marquees, image trails, page transitions, preloaders, and premium easing.

---

## 1. Overflow-clip hover zoom with caption slide-up on cards — sellability 10

**What it looks like:** Card image in an `overflow: hidden` wrapper; on hover the image scales 1.05-1.1 over 0.6-0.9s ease-out, while a caption/arrow slides up from the clipped bottom edge, card may lift 4-8px. Variants: grayscale-to-color, dark gradient scrim fade-in, texture/alt-image cross-reveal (Duten's brushed-steel finish pages).

**Why it sells:** The single most-used hover in award galleries, works on every niche (agency, real estate, e-commerce) so buyers see their own content working in it; zero-JS makes it bulletproof to customize.

**Example sites:** Pesquera Diez / P10 by Mubien — pesqueradiez.com/en/about · Duten (texture hover reveal) — duten.com/en/finish/brushed-stainless-steel/ · Made by Analogue — madebyanalogue.co.uk/studio/ · Gianluca Gradogna — gianlucagradogna.com/through-this-lens

**Webflow build (shippable):** Fully native IX2 — hover trigger on the card, scale action on the child image, move action on the absolutely-positioned caption; wrapper `overflow: hidden`. Custom cubic-bezier easing in the interaction panel. No custom code at all.

**Framer build (shippable):** Fully native — hover variant of the card component with image scaled and caption y-offset 0; transition set to a spring or custom bezier. Framer auto-animates between variants.

**Performance note:** Pure transform/opacity hover — zero perf cost, works identically at any grid size. The safest recipe on the whole book to ship as the template default.

---

## 2. Cursor-following image/video preview on list hover — sellability 9

**What it looks like:** A text-only project/menu list where hovering a row makes a floating image or muted video appear next to the cursor and follow it with lag; moving to the next row cross-fades to that row's media. Non-hovered rows often dim to 30-50% opacity.

**Why it sells:** Turns the cheapest layout (a text list) into the most memorable moment of a portfolio template — huge wow-per-effort in a marketplace preview video.

**Example sites:** Gianluca Gradogna — gianlucagradogna.com/through-this-lens · Awwwards "List image hover" — awwwards.com/inspiration/list-image-hover · Webflow cloneable: Smooth Effects for Mouse Cursor (Manish Pandey) · Webflow cloneable: Mouse Tooltip Next Project Teaser (Jonas Arleth) — both via webflow.com/made-in-webflow/custom-cursor

**Webflow build:** Doable natively — IX2 "Mouse move in viewport" drives a fixed image wrapper (with smoothing), per-row hover interactions toggle which image is visible + dim sibling rows. Shippable in that form. Smoother version needs a ~10-line GSAP embed using `gsap.quickTo()` for x/y (cloneable-only).

**Framer build:** Row-dimming and image swap work with hover variants (native), but the cursor-following float needs a code override (`useMotionValue` + `useSpring` on pointermove) or a marketplace cursor-follow component — common in premium Framer portfolio templates, legal to ship.

**Performance note:** Keep the floating preview to a single image/video element that swaps `src`, not one element per row — mounting N videos simultaneously to enable instant swaps is the usual perf mistake here.

---

## 3. Magnetic buttons and nav links — sellability 7

**What it looks like:** Buttons/nav items translate toward the cursor within a proximity radius (up to ~30% of element size, label moves slightly more for parallax), then spring back on leave. Often combined with a fill-swipe hover inside the button.

**Why it sells:** The "pulled toward you" physicality is shorthand for expensive interaction design; demonstrably draws attention to CTAs in preview videos.

**Example sites:** Codrops Magnetic Buttons demo — tympanus.net/Development/MagneticButtons/ · Webflow cloneable: Magnetic Call To Action (Dhruv Sachdev) · Webflow made-in-webflow magnetic tag (many cloneables) · Alec Tear — alectear.com

**Webflow build (cloneable-only):** Not truly native — IX2 "mouse move over element" fakes a weak tilt/shift version only. The real spring-back version needs a small custom-code embed: mousemove listener + GSAP elastic ease on mouseleave. Ships as site-wide JS targeting a `.magnetic` class, but that's a marketplace-code violation.

**Framer build (shippable):** Not native — requires a code component or override (`onPointerMove` sets a motion value, `useSpring` returns it to 0 on leave). Reusable overrides circulate in the Framer community; package one override file with the template.

**Performance note:** Bind the mousemove listener only while the cursor is within the proximity radius (not globally on scroll/resize) — the common bug is a page-wide mousemove listener firing constantly even far from any magnetic element.

---

## 4. Marquee / ticker bands with hover-pause — sellability 9

**What it looks like:** Infinitely looping horizontal strips — oversized display-text statements between sections, client-logo walls, sponsor tickers. Premium versions run two rows in opposite directions, pause/slow on hover; fanciest reverse/accelerate with scroll velocity. Off+Brand wraps a marquee around the entire site frame.

**Why it sells:** Adds constant motion to a static screenshot-y template for near-zero performance cost; buyers understand instantly how to swap their own logos/words in.

**Example sites:** Eight Pixel, FlowFest 2024, OnePageFlip, Off+Brand — all via One Page Love roundup: onepagelove.com/marquees · Webflow made-in-webflow marquee tag

**Webflow build (shippable base):** Pure-CSS keyframe embed (duplicate content twice, `translateX(-50%)` loop, `animation-play-state: paused` on hover — the No-Code Supply snippet approach) or IX2 loop animation. Scroll-velocity-reactive direction needs a GSAP ScrollTrigger embed (Off+Brand's free template shows the pattern) — cloneable-only for that variant.

**Framer build (shippable):** Fully native — built-in Ticker component with speed, gap, direction, and hover-pause controls. Only scroll-velocity reactivity needs an override.

**Performance note:** CSS keyframe/native looping is compositor-only and essentially free; the "marquee wraps the entire site frame" variant (Off+Brand) needs care that it doesn't intercept clicks on content beneath it — set `pointer-events: none` except on the ticker's own links.

---

## 5. Counter / curtain preloader with content reveal — sellability 7

**What it looks like:** On first load, a full-screen panel shows a 0→100 counter or animating wordmark/logo, then lifts away (curtain slide-up, mask/clip reveal) while hero elements stagger in. Best versions tie the reveal easing to the hero entrance for one choreographed sequence.

**Why it sells:** The first 2 seconds of a marketplace preview ARE the preloader — sets the "premium site" frame before buyers see anything else.

**Example sites:** Grégory Lallé (homepage loader reveal) — gregorylalle.com · SPYLT by Tubik — spylt.com · Henri Heymans — henriheymans.com · The Art of Documentary by DashDigital · Monolith NYC by CUSP — monolith.nyc

**Webflow build (mostly shippable):** IX2 "Page load" trigger animates the overlay div (initial state visible) — wordmark/curtain versions are pure IX2, no code. A live 0-100 counter needs a ~10-line JS embed incrementing a text node (cloneable-only for that piece). Include a "delete this div to remove loader" note for buyers.

**Framer build:** No native preloader primitive. Fake it with a full-screen overlay frame with an Appear effect + delayed exit animation (layer animates off after N seconds) — native. A live counter requires code. Because Framer sites render fast, keep it to a 1-1.5s branded curtain.

**Performance note:** A preloader that blocks interaction while assets are still loading behind it can make load times feel worse, not better, if it runs longer than the actual asset load — cap it at 1-2s regardless of real load time, it's theatrical, not functional.

---

## 6. Full-screen wipe / mask page transitions — sellability 8

**What it looks like:** Clicking a link plays an exit animation — a colored panel wipes across, the page masks/clips away (Amaterasu), or a pixelation dissolve (TeleTech) — then the destination enters with the reverse move. Persistent elements (logo, nav) stay fixed so the site feels like one continuous surface.

**Why it sells:** Transitions are the clearest "this cost $20k" tell; whole Awwwards collections are organized around them, and buyers cannot build this themselves — justifies premium pricing.

**Example sites:** Amaterasu (mask reveal) — amaterasu.ai · TeleTech (pixelated transition) — teletech.events/archive · Inkfish NYC · Elementis — elementis.co · Cyd Stumpel — cydstumpel.nl · Saisei (Webflow-built) — saisei-sbj.webflow.io

**Webflow build:** Not native across pages. Two template-safe approaches: (a) the overlay trick — IX2 click animation plays the wipe, navigation delayed ~600ms, plus a page-load enter animation on every page (pure Webflow, shippable, used by Saisei-style templates); (b) real cross-fade/persistent-element transitions via a Barba.js/Swup embed (more fragile, cloneable-only, document it if used).

**Framer build (shippable base):** Partially native — Framer supports link/page transition effects (fades, overlay-style effects) configured without code; appear effects on the destination page complete the illusion. Complex masks/pixel dissolves need a code component.

**Performance note:** The delayed-navigation overlay trick (~600ms) adds a fixed perceived-latency tax to every navigation — keep the delay tight and test it doesn't feel laggy on fast connections where the wipe outlasts the actual page-load time.

---

## 7. Animated link underlines (draw-through, exit-right) — sellability 8

**What it looks like:** Nav/inline links where a 1-2px line scales in from the left on hover and — the premium detail — exits to the right on mouse-leave instead of reversing (transform-origin swap). Variants: duplicate-text roll-up links, squiggly SVG underlines.

**Why it sells:** Cheap, everywhere, and one of the details reviewers actually check; the origin-swap exit is a recognized "polish tell" separating premium templates from defaults.

**Example sites:** FreeFrontend CSS link styles collection (30+ snippets) — freefrontend.com/css-link-styles/ · Alec Tear — alectear.com · Opositive Films by Buzzworthy — opos.buzzworthystudio.com/about

**Webflow build (shippable):** Pure-CSS embed using `::after` with `transform-origin` swap (`right` on base, `left` on `:hover`) applied to a global `.link` class — most robust for buyers; or IX2 hover animation scaling a 1px underline div (visual but per-instance, no origin-swap). The CSS route is the professional choice.

**Framer build:** Native via component variants — link component with underline layer at `scaleX 0`, hover variant `scaleX 1`. The exit-to-right origin swap is NOT expressible in variants (single transition per property) — needs custom CSS in site settings or a code component (still shippable on Framer).

**Performance note:** Essentially free either way (one pseudo-element transform); the only real risk is applying the CSS globally to `.link` without scoping — audit that it doesn't catch unintended anchor tags (e.g. inside rich-text CMS content) during QA.

---

## 8. Character-split text effects on headings and links — sellability 8

**What it looks like:** Headings split into chars/words that stagger in on load or scroll (y-offset + blur/fade, 20-40ms stagger), menu links whose letters ripple, scramble, or roll to a duplicate on hover.

**Why it sells:** Typography IS the design in modern minimal templates — animating it per-character is the highest-visibility polish available without any imagery.

**Example sites:** Eva Sánchez (ripple text hover) — evasanchez.info · Radiance (interactive hero letters) — radiance.family · Wodniack.dev — wodniack.dev · Stas Bondar — stabondar.com

**Webflow build (cloneable-only):** Needs custom code — GSAP SplitText (free with GSAP) in a site-wide embed targeting `[data-split]` attributes; scroll trigger via ScrollTrigger. No native char-splitting in IX2 outside the May-2026 GSAP-powered Interactions update (see kinetic-typography recipe in motion-3d-recipes.md for the load/scroll-reveal case — this recipe's hover-ripple variant still needs code). Hover letter-ripples are GSAP-only. Package as one embed file with data-attributes so buyers never touch code.

**Framer build:** Largely native — Text Effects split text by character/word/line with stagger presets (fade, blur, slide) on appear, no code. Hover-triggered scramble/ripple on links still needs a code component (shippable on Framer).

**Performance note:** Same DOM-inflation caveat as kinetic typography — reserve for short strings (headings, nav links), never body copy or long paragraphs.

---

## 9. Hover-to-play video cards — sellability 8

**What it looks like:** Project/work cards hold a static poster; on hover a muted looping video fades in and plays (resetting or pausing on leave), often with the custom cursor morphing to a "Play" disc at the same time.

**Why it sells:** Makes portfolio grids feel alive in marketplace previews and demos motion-design work — the exact buyer (agencies, videographers, studios) for premium templates.

**Example sites:** Accordion (autoplay video on hover) — accordion.net.au/work · Webflow cloneable: Smooth Effects for Mouse Cursor — video on hover (Manish Pandey)

**Webflow build (half-native):** IX2 hover can fade the video wrapper in/out (shippable), but actually starting/stopping playback needs a small JS embed (`video.play()`/`pause()` on mouseenter/leave) since Webflow background video autoplays continuously otherwise (works too, just costs bandwidth). Cloneables exist for the JS-controlled version.

**Framer build (shippable):** Effectively native — hover variant swaps poster frame for the video layer; Framer's video component playback settings cover autoplay-muted-loop, so entering the hover variant starts it. No code for the standard version.

**Performance note:** If skipping the JS play/pause control on Webflow, every video in the grid autoplays continuously in the background even off-hover — that's real bandwidth cost on a grid of 6-12 cards; budget for it or add the small embed.

---

## 10. Image trail cursor effect (hero) — sellability 6

**What it looks like:** Moving the mouse across a hero spawns a trail of images at the pointer position — each new image pops in rotated/scaled and fades/shrinks away, drawing a temporary collage along the mouse path. Canonical Codrops technique.

**Why it sells:** Pure spectacle — the single highest-wow-factor cursor effect for a template preview video; buyers just swap the image array.

**Example sites:** Codrops Image Trail Effects — tympanus.net/codrops/2019/08/07/image-trail-effects/ · Webflow cloneable: 9 Image Motion Trail Effect — image-motion-trail-effect.webflow.io · Webflow cloneable: Trailing Cursor (Kevin Haag)

**Webflow build (cloneable-only):** Custom code only — GSAP embed measuring mouse distance and cycling absolutely-positioned images from a hidden CMS-bound list (so buyers edit images via CMS, not code). Proven cloneables exist to adapt.

**Framer build (shippable):** Not native — needs a code component (pointermove distance threshold + motion animate in/out on a pooled image array). Community components exist; bundle one with editable image props.

**Performance note:** Pool and reuse a fixed set of image elements (don't create new DOM nodes per trail point) — the naive "spawn a new img on every mousemove" implementation is the classic memory-leak version of this effect.

---

## 11. The premium easing recipe (expo-out, long durations, choreographed stagger) — sellability 7

**What it looks like:** The invisible pattern behind every recipe above: hover states at 0.4-0.6s and reveals at 0.8-1.2s using aggressive ease-out curves (`cubic-bezier(0.16,1,0.3,1)` / expo.out — fast start, very long settle), never default "ease"; movement paired with a second property (opacity+y, scale+blur); 60-120ms stagger between siblings; exit animations 30-50% faster than entrances.

**Why it sells:** Buyers can't name it but they feel it — the same layout with default easing reads cheap, with expo-out reads expensive; the cheapest possible upgrade to every interaction in a template.

**Example sites:** Grégory Lallé (loader-to-hero choreography) — gregorylalle.com · Amaterasu (mask reveals) · Pesquera Diez (consistent easing site-wide) — pesqueradiez.com/en/projects · Elementis — elementis.co

**Webflow build (shippable):** Fully native — IX2 supports custom cubic-bezier curves per action; set `(0.16,1,0.3,1)` as the house curve on every interaction, staggers via per-element delay steps. For GSAP embeds use `expo.out`/`power4.out`. Bake the curve into the template's style guide page as a selling point.

**Performance note / Framer build:** Fully native on Framer too — every transition accepts a custom bezier or tuned spring (high stiffness, damping ~20-30); Appear effects support stagger on children. Set once on master components so buyer edits inherit it. Zero perf cost either way — this recipe is pure timing-curve discipline, not new code.
