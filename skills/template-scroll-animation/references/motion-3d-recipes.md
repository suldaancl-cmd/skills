# Premium Motion, 3D & Rich-Media Recipes

12 patterns from an audit of 120 sites across the WebGL/Three.js/Spline/Rive/Lottie space, with the marketplace reality check for Webflow and Framer template sellers.

---

## 1. Kinetic typography reveal (per-char/word blur + y-offset stagger on scroll) — sellability 10

**What it looks like:** Headlines split into chars/words/lines that animate in with a stagger: each unit starts ~20-40px lower, blurred (4-8px), 0 opacity, then snaps to place over 0.6-1s ease-out; triggered on load for hero, on scroll-into-view for section headings. Often paired with a clip-path mask so text "rises out of a line."

**Why it sells:** Highest wow-per-byte effect: zero assets, works on any copy the buyer types, reads as "expensive agency site" in the first 2 seconds of a preview video.

**Example sites:** MONOLOG (Awwwards SOTD Jul 2026) — bymonolog.com · Ten Years Away — Studio375 — ten.375.studio/en · Obys Experiment Space — experiment.obys.agency · Osmo — osmo.supply

**Webflow build (shippable):** Webflow Interactions are GSAP-powered and default for Marketplace templates from May 1, 2026 — text splitting into chars/words/lines with stagger, blur, and transform is native, no embed. Build as a class-based interaction so buyers restyle by editing text only.

**Framer build (shippable):** Native Text Effects — animate characters/words/lines with Scale, Blur, Offset properties on Appear, Layer In View, or Section In View. No code. Ship presets on every H1/H2 style.

**Performance note:** Character-splitting inflates DOM node count fast on long headlines — reserve for H1/H2-length copy, and disable/simplify below ~600px where line-wrap changes make char-position math unstable.

---

## 2. Aurora / blur-morph gradient background (CSS-only WebGL impostor) — sellability 10

**What it looks like:** 3-5 large radial/conic gradient blobs in brand hues over a near-black base, blurred 80-150px, each slowly translating/scaling on a 10-20s loop so the background appears to "breathe." Staple background of Stripe/Linear/Vercel-class SaaS pages.

**Why it sells:** ~80% of a fluid-shader hero's wow at ~0 performance cost; instantly recolorable to the buyer's brand by changing 3 hex values — the ideal template property.

**Example sites:** Linear — linear.app/homepage · Resend — resend.com · Cursor — cursor.com · Raycast — raycast.com · Stripe (mesh-gradient signature) — stripe.com

**Webflow build (shippable):** Absolutely-positioned divs with radial-gradient backgrounds + blur filter, animated with a looping Interactions timeline (move/scale). No embed — ships clean through marketplace review. Expose blob colors as swatches.

**Framer build (shippable):** Gradient-filled frames with Blur layer effect, looped via Appear/loop transitions or a simple Scroll Transform; alternatively one background image + animated overlay frames. Fully no-code.

**Performance note:** `filter: blur(100px+)` on large elements can be GPU-heavy on low-end mobile — cap blob size/blur radius on small viewports or swap to a pre-rendered blurred PNG background below a breakpoint.

---

## 3. Interactive Spline 3D hero (mouse-follow + scroll-driven scene) — sellability 8

**What it looks like:** A Spline scene (product, abstract glass blob, iridescent shape, device) as the hero centerpiece; camera/object rotates on mouse move and plays a scroll-scrubbed animation as the user scrolls the first sections.

**Why it sells:** True 3D interactivity is the top preview-video wow factor, and Spline is the only real-3D path that is native (thus marketplace-safe) in BOTH builders.

**Example sites:** THREE DIMENSIONS — Dirk Lach (cloneable) · FlowDrinks — Diego Toda de Oliveira · NeoCultural Couture — Jordan Gilroy · Nike 360 product landing — Zoe Tang (all via webflow.com/made-in-webflow/spline)

**Webflow build (shippable):** Native Webflow ↔ Spline integration — paste the scene URL into the Spline element; hover/scroll interactions can drive scene states. No code embed, passes the no-custom-code template rule. Include a swap-the-scene instructions page.

**Framer build (shippable):** Native Spline component — paste the scene link, wire mouse/scroll events in Spline's own state machine. Zero code.

**Performance note:** Buyers must edit the 3D in Spline itself, not in the builder — ship 2-3 alternate scenes to reduce that friction, and keep scene poly-count modest since Spline scenes load a runtime + asset payload on top of the page.

---

## 4. Film grain / noise overlay — sellability 8

**What it looks like:** A full-viewport fixed overlay of tiled monochrome noise (transparent PNG or SVG `feTurbulence`) at 3-8% opacity, sometimes animated by cycling 2-3 noise frames, laid over gradients/video/imagery.

**Why it sells:** One layer converts flat digital gradients into something tactile and "filmic" — the cheapest possible premium signal, and it survives any buyer recoloring untouched.

**Example sites:** Awwwards texture collection — awwwards.com/websites/texture/ · Everlovin' Press (Line25 grain roundup) · Osmo — osmo.supply · Fey — feyapp.com

**Webflow build (shippable):** Fixed, `pointer-events: none` div with a tiled noise PNG background at low opacity; optional 8-step `background-position` loop via Interactions for animated grain. No code required.

**Framer build (shippable):** Fixed frame with noise image fill at low opacity above all sections; newer Framer versions also have a built-in Noise texture in fill options. Zero code.

**Performance note:** A tiled PNG at low opacity is essentially free; avoid large un-tiled noise images (multi-MB) — use a small (256-512px) tile repeated via CSS background-repeat.

---

## 5. Scroll-scrubbed Lottie hero/diagram animation — sellability 9

**What it looks like:** A Lottie (exported from After Effects) whose playhead is bound to scroll progress — product diagrams assembling, lines drawing, mascots reacting — plus small Lottie micro-animations on icons/cards on hover.

**Why it sells:** Vector-crisp motion at tiny file size, fully native in both builders, and buyers can swap the JSON from LottieFiles' 100k+ library without touching code — best customization story of any rich-media pattern.

**Example sites:** Sentry (animated heroes/characters) — sentry.io · Made in Webflow — Lottie/Spline education demos · LottieFiles Webflow plugin gallery — lottiefiles.com/plugins/webflow

**Webflow build (shippable):** Dedicated Lottie element (JSON/dotLottie); Interactions panel scrubs it "while scrolling in view" or plays on hover/click/load — explicitly supported without custom code, marketplace-safe.

**Framer build:** Native Lottie component (paste URL or upload), plays on appear/hover/loop — shippable. Scroll-scrub specifically needs a small code component or the free community Lottie-scroll component (allowed, since Framer permits clean code components).

**Performance note:** Lottie files are vector JSON, not raster video — file size stays small even at high visual complexity, making this the lightest-weight "premium diagram" option on the whole list.

---

## 6. Infinite marquee + scroll-velocity text ticker — sellability 8

**What it looks like:** Full-width looping strips — logos, oversized display words, image thumbnails — drifting continuously, and in the premium version accelerating/skewing with scroll velocity, sometimes reversing direction per row.

**Why it sells:** Constant ambient motion makes a static template preview feel alive, costs nothing to customize (buyers swap logos/words), signals "GSAP-grade" craft.

**Example sites:** GSAP — gsap.com · TRIONN — trionn.com · Osmo — osmo.supply

**Webflow build:** Basic infinite marquee is a native looping Interactions pattern on a duplicated track (no code, shippable). Velocity-reactive skew specifically needs GSAP ScrollTrigger custom code — NOT marketplace-legal; ship the constant-speed version as the template default.

**Framer build (shippable):** Native Ticker component ships with Framer (speed, direction, hover-pause). Velocity-reactive versions exist as marketplace code components (e.g. "Text Scroll Velocity," "Parallax ScrollText") — legal to include.

**Performance note:** Constant-speed CSS/native looping marquees cost nothing; velocity-reactive versions read scroll events on every frame — throttle with `requestAnimationFrame`, never a raw scroll listener, if building the custom version.

---

## 7. Parallax depth stack (multi-speed scroll layers) — sellability 9

**What it looks like:** Hero/section media split into 2-4 layers scrolling at different rates (background 40-80% speed, foreground 110-140%), often combined with a slight scale-up of images as they enter — the "deep space" feel.

**Why it sells:** Depth is the most universally understood premium cue; works with the buyer's own photos, customizes perfectly, demos well across niches (real estate, fashion, SaaS).

**Example sites:** 21 Hrs On The Moon — Studio 28K — 21hrs.space · Vero New-York — Rodéo studio — verostudio.com · Julien Calot — juliencalot.com

**Webflow build (shippable):** Native "while page is scrolling" Interactions with different move distances per layer; image scale-on-scroll via the same panel. 100% marketplace-safe and the backbone of most bestselling Webflow templates.

**Framer build (shippable):** Native Scroll Speed effect (set layers to 40%/80%/120%/140%) plus Scroll Transform for scale/opacity — Framer's own academy teaches exactly this. Zero code.

**Performance note:** Multiple full-bleed images each parallaxing independently multiplies paint area — compress and lazy-load offscreen layers, especially on image-heavy real-estate/fashion niches.

---

## 8. Video-first hero (full-bleed autoplay loop with quick cuts) — sellability 8

**What it looks like:** A 15-30s muted, autoplaying, quick-cut background video filling the hero viewport with text overlaid, optionally scroll-pinned.

**Why it sells:** Video heroes correlate with dramatically longer sessions per roundup data (Marketer Milk / SliderRevolution); in a preview, a moving hero out-performs any static one.

**Example sites:** Runway — runwayml.com · Cadigal Office Leasing — cadigal.com.au · Awwwards video collection — awwwards.com/websites/video/

**Webflow build (shippable):** Native Background Video element (auto-loops, muted); add a poster image for mobile since mobile browsers may block autoplay. Section-pinning the video during scroll needs custom code — omit for marketplace.

**Framer build (shippable):** Native video fill/component with autoplay+loop+muted; combine with Scroll Transform for fade/scale-away on scroll. Zero code.

**Performance note:** Buyers must supply footage — bundle 1-2 stock-video placeholders sized/encoded for web (H.264, under ~5MB for a 15-30s loop) so the template doesn't ship broken or bloated by default.

---

## 9. WebGL shader hero (fluid, refraction, particle fields) — sellability 7

**What it looks like:** True custom-shader centerpieces — fluid smoke reacting to cursor, glass refraction over type, particle systems forming logos. The ceiling of the wow scale, the floor of portability.

**Why it sells:** What wins Site of the Day; buyers actively search "WebGL template." But it's dev-owned tech, so the template version needs a no-code bridge or substitute.

**Example sites:** Vectr — Utsubo (Developer Award, SOTD) — vectrfl.com · Podium — San Rita (Developer Award, SOTD) — podium.global · Obys Experiment Space · Unicorn Studio (the no-code WebGL tool) — unicorn.studio

**Webflow build (NOT shippable on marketplace):** Three.js/Unicorn Studio require script embeds; custom code in site/embed/page settings is banned in Templates per submission guidelines. Substitutes: export the shader as an MP4 loop (native background video), or rebuild the look in Spline (native). Sell the real embed version off-marketplace as a cloneable + Unicorn Studio scene.

**Framer build (shippable — genuine differentiator):** Unicorn Studio (70+ WebGL effects, 36kb runtime, official Framer embed path) inside an Embed/code component, or a custom Three.js code component — Framer allows clean custom code and does no manual review.

**Performance note:** Real WebGL is the heaviest recipe on this list (GPU shader compilation + runtime) — always test on mid-tier mobile GPUs before shipping, and keep the baked-MP4 substitute as the default for anyone who can't verify performance across devices.

---

## 10. Rive interactive character / state-machine hero — sellability 6

**What it looks like:** Rive files with state machines — mascots that track the cursor, heroes reacting to hover/click, animated CTAs.

**Why it sells:** Interactivity beats playback: Notion reported doubled engagement vs. their previous iteration. Tiny runtime, resolution-independent. But authoring requires Rive skills, so it customizes poorly for average buyers.

**Example sites:** Rive websites use-case gallery (Figma, Shopify, Sentry, Notion cases) — rive.app/use-cases/websites · Vidflow — onepagelove.com/vidflow · Magician — onepagelove.com/magician

**Webflow build (NOT shippable on marketplace):** Requires the Rive JS runtime via script embed → blocked by the no-custom-code rule. Substitute: bake the animation to Lottie (native element), keep only autoplay/hover behavior. Full Rive versions are cloneable-only, sold off-marketplace.

**Framer build (shippable):** Rive community code components exist; embed the `.riv` URL and expose state-machine inputs as component props so buyers can at least toggle behaviors without touching Rive itself.

**Performance note:** Lowest customizability on this list — flag to buyers up front that changing the actual animation requires the Rive editor, not just prop toggles; this is the #1 support-ticket risk of shipping it.

---

## 11. Cursor-reactive polish kit (custom cursor, magnetic buttons, hover tilt) — sellability 7

**What it looks like:** A bundle of pointer micro-interactions: a custom dot/label cursor that morphs over links, magnetically-pulling buttons, 3D hover-tilt cards.

**Why it sells:** The details reviewers and buyers hover-test first in a live preview; they make a standard layout feel hand-built.

**Example sites:** TRIONN — trionn.com · Griflan — griflan.com · Noomo Showcase — showcase.noomoagency.com

**Webflow build:** Partial native — hover tilt via mouse-move Interactions (rotate X/Y on hover) is marketplace-safe. True custom cursors and magnetic buttons need JS; keep those out of the marketplace build, or make the cursor a follow-div driven by a mouse-move interaction (which IS native).

**Framer build (shippable):** Strong native story — built-in Custom Cursors per frame, hover Effects handle tilt/scale; magnetic pull needs a small code component (several free on the Framer marketplace) — allowed.

**Performance note:** Disable all cursor-follow effects below ~992px (touch has no cursor) — this is a hard requirement, not a nice-to-have, or the follow-div sits stuck on-screen on mobile.

---

## 12. Scroll-driven product tour (pinned section, swapping media states) — sellability 9

**What it looks like:** A section pins while the user scrolls through 3-5 steps: screenshots/3D angles crossfade or slide as step copy changes — the Apple-style narrative, now standard on SaaS feature pages. Full AirPods-style image-sequence scrub is the luxury variant.

**Why it sells:** Converts scrolling into storytelling and lets buyers showcase THEIR product shots — highly transferable across niches, spectacular in a scrolling preview capture.

**Example sites:** Apple iPad Pro — apple.com/ipad-pro · Fey (features pages) — fey.com/features/earnings · Linear — linear.app/homepage

**Webflow build (shippable base):** `position: sticky` wrapper + "while scrolling in view" Interactions to swap opacity/position of media per step — proven marketplace-legal pattern. Canvas image-sequence scrubbing needs JS → substitute a scroll-scrubbed Lottie or Spline scene to stay marketplace-legal.

**Framer build (shippable):** Sticky/pinned sections with Scroll Transforms per step; scroll-linked variant switching via Scroll Sections In View. Image-sequence scrub exists as marketplace code components if wanted.

**Performance note:** The opacity/position cross-fade version is cheap and marketplace-safe; only the full image-sequence variant carries the asset-weight cost described in the scroll-scrubbed video/image-sequence recipe — decide per-template which tier you're shipping.
