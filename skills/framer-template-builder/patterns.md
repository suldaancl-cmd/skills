# Pattern catalog — Framer build technique, example, sellability

Full detail behind the ranked table in SKILL.md. Each entry: what it is, why buyers pay for it, exactly how to build it in Framer, and at least one real example from the research. Ranked within each category by sellability (1-10).

## Load / first impression

### Preloader-on-every-page (9/10)
A branded loading animation (wordmark counter, wipe, logo reveal) plays on every page load and the enter animation reads as one continuous choreography. Nakula ($129, marketplace bestseller) is explicitly praised for a "preloader animation on every page"; Porto (free) for "beautiful page transitions."
**Build in Framer:** a fixed-position overlay frame with an Appear effect (in) and a delayed exit animation (out) after N seconds recreates the preloader per page. There is no native cross-page transition API, so true seamless transitions between pages need a code override (framer-motion AnimatePresence-style pattern) — the overlay-per-page trick is what bestsellers actually ship, so start there. Keep it to 1-1.5 seconds since Framer sites already render fast.

### Full-screen wipe / mask page transition (8/10)
A colored panel wipes across or a mask/clip reveal plays on navigation, with persistent elements (logo, nav) staying fixed so the site feels like one surface. Amaterasu (amaterasu.ai) and Saisei (built in Webflow, cited as the transition benchmark) are the references.
**Build in Framer:** Framer supports link/page transition effects (fades, overlay-style effects) configured without code; pair the destination page's own Appear/stagger entrance with the transition so it reads as one move. Complex masks or pixel-dissolve transitions need a code component — the native fade+stagger combo is enough for a sellable template.

## Typography and text motion

### Native split-text Appear (per char/word/line) (10/10)
Headlines and section copy split into lines/words/characters that stagger in — blur+y-offset, clip-mask reveal, or scroll-triggered. This is the baseline that separates "premium" from "static" in a marketplace preview scroll (Xtract, Billie both praised for exactly this).
**Build in Framer:** fully native. Framer's text layers support built-in split-text Appear (by character/word/line) with spring transitions, triggered on load, on Appear, or on Layer/Section-in-view. Zero code — a genuine listing bullet Webflow templates can't claim natively (Webflow needs a GSAP SplitText embed for the same result). Set once on H1/H2 master components so buyer edits inherit it.

### Scroll-scrubbed text highlight/fill (9/10)
A large paragraph where words tint from grey to full color line-by-line as scroll progresses, usually pinned mid-viewport.
**Build in Framer:** two routes — (a) no-code: a component with grey/colored variants switched by Scroll Variants inside a sticky Scroll Section, one frame per line; (b) a small code override using framer-motion `useScroll` + per-word opacity for a true continuous scrub. Community remixes (Segment UI, Framer University) sell this pre-built; bundle one.

## Marquees and tickers

### Infinite logo/testimonial ticker (10/10)
A continuously looping horizontal strip of logos, testimonials, tech icons, or oversized text — present in effectively every top SaaS/agency Framer template (Vectura, Saalix — #2 weekly on selected.site).
**Build in Framer:** native Ticker component — drop in, connect frames/logos, set speed/direction/gap/fade-edges/pause-on-hover. Zero code. Velocity-reactive variant (accelerates/reverses with scroll speed) needs a code override reading `useVelocity` from framer-motion, or use it as-is since Framer ships the base ticker natively either way.

## Sticky / pinned scroll sections

### Sticky stacking cards (10/10)
A column of full-width cards where each pins and the next slides up over it, the buried card scaling to ~0.92 and dimming. 3-6 cards is the sweet spot; marketplace code components sell this standalone (Sticky Overlap, $12; Parallax Image Stack, $12).
**Build in Framer:** set each card's Position to Sticky within its section with an incremental pin offset, then add a Scroll Transform (scale 1→0.92, opacity) tied to progress. Fully native — turns a boring feature list into a physical-metaphor interaction with zero assets.

### Pinned section with content swap / product tour (9/10)
A section pins for 2-4 viewport heights while content swaps in steps: a phone/dashboard mockup stays fixed while screenshots or step copy change. The canonical SaaS scrollytelling block (Apple iPad Pro, Fey feature pages, Linear).
**Build in Framer:** Sticky position on the media frame inside a tall Scroll Section, then Scroll Variant triggers (or Scroll Section-in-view transitions) swap image/component variants as each text step passes. No code.

### Zoom-scrub media hero (9/10)
An image/video starts framed mid-viewport and scales to full-bleed (or the reverse) scrubbed to scroll position — the Apple-style "expensive SaaS" move. Sticky Zooming ($14 Framer component) sells this standalone.
**Build in Framer:** Sticky position + Scroll Transform on scale and border-radius tied to section scroll progress. Entirely native — one of the few "expensive-looking" effects Framer does with zero code, hence the paid components built around it.

### Scroll-driven 3D image/device transform (Fey-style) (8/10)
Product screenshots tilt in 3D perspective and flatten/rotate as you scroll. Reverse-engineered from fey.com by Framer University using "scroll transforms with hidden trigger frames."
**Build in Framer:** enable 3D in the Effects editor, add Scroll Transform with rotateX/rotateY/perspective mapped to scroll progress inside a Scroll Section. Use empty "hidden trigger frames" (invisible frames placed purely for scroll timing) to control when each rotation stage kicks in — this is the documented pro technique for Fey-class sequences, and it's still no-code.

### Section wipes / curtain overlaps (9/10)
Full-height sections pin as the next slides over them (dark wipes over light, footer revealed from "under" the page). Petralithe and the Unseen 2025 Annual Report use this for cinematic multi-section rhythm.
**Build in Framer:** Sticky sections stacked with ascending z-index; add a Scroll Transform scale/opacity on the outgoing section as the next one covers it. No code.

### Multi-layer parallax hero/depth stack (8-9/10)
3-6 layers (background, midground, foreground, headline) moving at different scroll speeds to fake depth. 21 Hrs On The Moon and Linear-style sites use this; the technique is the most-cloned scroll interaction in Webflow's ecosystem and Framer's easiest native equivalent.
**Build in Framer:** native Scroll Speed effect — one slider per layer (below 1 = slower/background, above 1 = faster/foreground). Add a Scroll Transform for scale/opacity on entering images. Zero code, one slider per layer.

### Horizontal scroll section (vertical-scroll-driven) (8/10)
A tall track pins a viewport-height container and translates panels on the X-axis as the user scrolls vertically — project galleries, timelines, product lineups (Theo, Canals Amsterdam).
**Build in Framer:** not clean natively — Framer's scroll effects don't remap vertical scroll to X-translation across a pinned track. Use a code component/override with framer-motion `useScroll` + `useTransform([0,1], ['0%','-75%'])` on a sticky container, or bundle an existing marketplace horizontal-scroll component.

## Hover and cursor micro-interactions

### Overflow-clip hover zoom + caption slide-up on cards (10/10)
Card image in an overflow-hidden wrapper scales 1.05-1.1 on hover while a caption/arrow slides up from the clipped edge. The single most-used hover across award galleries because it works on any content the buyer drops in.
**Build in Framer:** fully native — create a hover variant of the card component with the image scaled and the caption's y-offset at 0; set the transition to a spring or custom bezier. Framer auto-animates between variants, zero code.

### Custom/blend-mode cursor (8/10)
A small dot/label cursor follows the pointer with lag and morphs on hover (grows into a "View"/"Play" disc); premium versions use `mix-blend-mode: difference` so it inverts over any background. Waaarhol and Lux Expression are references.
**Build in Framer:** native Cursors feature — assign a custom cursor design per element/frame with follow smoothing and hover-swap states, no code for the basic version. The blend-mode invert specifically needs a small code override or custom CSS on the cursor layer, since blend-mode isn't an exposed control.

### Magnetic buttons/nav links (7/10)
Buttons translate toward the cursor within a proximity radius, then spring back on leave. Standard on agency sites (Codrops' canonical Magnetic Buttons demo).
**Build in Framer:** not native. Requires a code component/override (`onPointerMove` sets a motion value, `useSpring` returns it to 0 on leave). Reusable overrides circulate in the Framer community — package one file with the template rather than writing from scratch.

### Hover-to-play video cards (8/10)
Project cards hold a static poster; hovering fades in a muted looping video.
**Build in Framer:** effectively native — a hover variant swaps the poster frame for the video layer, and Framer's video component autoplay-muted-loop settings cover playback. No code for the standard version.

## Rich media

### Aurora / blur-morph gradient background (10/10)
3-5 large radial/conic gradient blobs in brand hues over a near-black base, blurred 80-150px, slowly translating on a 10-20s loop. The staple background of Stripe/Linear/Resend/Cursor/Raycast-class SaaS pages.
**Build in Framer:** gradient-filled frames with a Blur layer effect, looped via Appear/loop transitions or a simple Scroll Transform. Fully no-code and instantly recolorable to the buyer's brand by changing 3 hex values — the ideal template property.

### Film grain / noise overlay (8/10)
A fixed, full-viewport tiled noise layer at 3-8% opacity over gradients/imagery — the norm on the entire dark-premium-site aesthetic (Osmo, Fey).
**Build in Framer:** a fixed frame with a noise image fill at low opacity above all sections; newer Framer versions also expose a built-in Noise texture in fill options. Zero code.

### Interactive Spline 3D hero (8/10)
A Spline scene (product, glass blob, iridescent shape) as the hero centerpiece, rotating on mouse move or scrubbing on scroll.
**Build in Framer:** native Spline component — paste the scene link, wire mouse/scroll events in Spline's own state machine. Zero code. Buyers must edit the 3D in Spline itself, so ship 2-3 alternate scenes to reduce that friction.

### Scroll-scrubbed Lottie animation (9/10)
A Lottie whose playhead is bound to scroll progress (diagrams assembling, lines drawing), plus micro-Lottie loops on icons/hover.
**Build in Framer:** native Lottie component (paste URL or upload JSON), play on appear/hover/loop. Scroll-scrub specifically needs a small code component or a free community Lottie-scroll component — allowed since Framer permits clean code components. Vector-crisp at tiny file size and buyers can swap the JSON from LottieFiles' library without touching code — the best customization story of any rich-media pattern.

### WebGL shader hero via Unicorn Studio (7/10)
True custom-shader centerpieces — fluid smoke reacting to cursor, glass refraction, particle fields — the ceiling of the wow scale (Vectr, Podium, both Awwwards Developer Award winners).
**Build in Framer:** shippable via Unicorn Studio (70+ WebGL effects, ~36kb runtime, official embed path) inside an embed/code component, or a custom Three.js code component. Framer allows clean custom code and does no manual review, which is the concrete reason this is a genuine Framer-marketplace differentiator — the same effect is blocked outright in Webflow marketplace templates (no-custom-code rule).

### Rive interactive character/state-machine (6/10)
Mascots that track the cursor, heroes that react to hover/click. Notion reported doubled engagement after adding one.
**Build in Framer:** viable — Rive community code components exist for Framer, and clean code components are allowed. Embed the `.riv` URL and expose state-machine inputs as component props so buyers can toggle behaviors without reading code. Authoring the Rive file itself still requires Rive skills, so this customizes poorly for the average buyer — always ship a Lottie fallback.

## Content/commerce blocks

### CMS-everything architecture (9/10)
All repeatable content (case studies, team, testimonials, FAQ, blog) lives in CMS collections bound to designed components. Nitro (free), Nord-Å ($99), Mugen ($129, "advanced CMS") are the references. See `component-architecture.md` for the field-naming and empty-entry rules this pattern is graded on.
**Build in Framer:** native CMS collections with typed fields, collection lists bound to components, CMS-driven detail pages. Bind fields into component variants so cards restyle per category.

### SaaS pricing-section craft (9/10)
A dedicated, over-designed pricing section: monthly/yearly toggle, middle tier visually elevated, feature list with icon rows. Vectura ($99) is singled out for "exceptional pricing page design" as its selling feature.
**Build in Framer:** native — pricing card as a component with Monthly/Yearly variants, a toggle component switching variants via interaction. Animated price count-up needs a code component; the toggle+highlight itself is zero code.

### Playful drag/physics micro-interactions (6/10)
Draggable stickers/products the visitor can throw around (Donut Shop's drag-and-drop menu). Fits fun/consumer brands, not corporate SaaS.
**Build in Framer:** code override — framer-motion's `drag` prop (`drag`, `dragConstraints`, `dragElastic`) applied via override to any layer, ~10 lines, ships working inside the template file.

## The invisible layer: easing

### The premium easing recipe
Hover states at 0.4-0.6s and reveals at 0.8-1.2s using aggressive ease-out curves (`cubic-bezier(0.16,1,0.3,1)`/expo-out — fast start, long settle), never default "ease"; pair movement with a second property (opacity+y, scale+blur); 60-120ms stagger between siblings; exits 30-50% faster than entrances. Buyers can't name it but feel it — the same layout with default easing reads cheap.
**Build in Framer:** every transition accepts a custom bezier or a tuned spring (high stiffness, damping ~20-30); Appear effects support per-child stagger. Set the house curve once on master components so buyer edits inherit it — this is a one-time setup that upgrades every interaction in the template at once.
