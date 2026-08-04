# Motion & Interaction: Legality Guide + Ranked Build Recipes

Source beats: Webflow marketplace craft (140 sites), scroll/scrollytelling (110 sites),
micro-interactions (115 sites), premium motion/3D (120 sites).

## The legality rule (read this before designing any "wow" moment)

Webflow's Submission Guidelines ban custom code in site settings, embeds, and page settings for
Marketplace templates — with one major exception carved out since Webflow acquired GSAP: **GSAP
and its plugins (SplitText, ScrollTrigger, ScrollSmoother — all now free in Webflow) are treated
as the permitted custom-code path**, provided every animated selector, tweakable variable, and
removal step is documented on the template's Instructions page. Native Webflow Interactions are
now GSAP-powered by default for Marketplace templates as of **May 1, 2026** — legacy IX2 is
explicitly discouraged going forward.

**Caveat — the research sources aren't fully consistent on how far that exception reaches.**
The submission-guidelines beat states GSAP is "the ONLY permitted custom code... requires a full
GSAP edit-guide." The premium-motion beat separately states a velocity-reactive GSAP
ScrollTrigger marquee "is NOT marketplace-legal" and should ship at constant speed instead.
Read this as: **native Interactions-panel GSAP is always safe; a GSAP *embed* is a narrow,
documented exception for effects the panel can't do (text-splitting, video/canvas scrubbing,
smooth-scroll) — not a blanket license for every elaborate script.** Keep embeds minimal,
single-purpose, and always documented. Verify current Submission Guidelines before shipping
anything beyond the patterns below.

Anything that requires a **separate JS runtime** — Three.js, Rive's runtime, Unicorn Studio,
Lenis, standalone cursor/magnetic-button/image-trail scripts — is **not shippable in a Webflow
Marketplace template**, full stop. Three options when a concept needs one of these:
1. Substitute a native equivalent (Spline for real 3D, Lottie for character/vector animation, a
   baked MP4 loop for a shader effect).
2. Build it anyway and sell it as a **free cloneable outside the marketplace** (Made in Webflow
   showcase) — this is explicitly how top creators (Timothy Ricks, Osmo) monetize advanced
   effects: as lead-generation, not as marketplace inventory.
3. Move the concept to **Framer**, whose marketplace does no manual review and explicitly
   permits clean code components — Three.js heroes, Rive characters, and velocity-reactive
   tickers are all sellable there.

## Legal-tech quick reference

| Tech | Webflow Marketplace legal? | Use for |
|---|---|---|
| Native Interactions panel (GSAP-powered) | Yes, always | Reveals, hovers, scroll triggers, staggers, parallax, easing curves |
| Lottie element | Yes, native | Vector character/diagram animation, scroll-scrubbed via Interactions |
| Spline embed | Yes, native | Real interactive 3D hero |
| GSAP + plugins via documented embed | Yes, narrow exception | Text-splitting (SplitText), video/canvas scrub, ScrollSmoother |
| Pure CSS embed (keyframe loop, `::after` underline, blur/grain overlay) | Generally treated as the same low-risk category as the GSAP exception — document it | Marquee loops, link underlines, film-grain overlay |
| Three.js / React Three Fiber | No | Framer or free cloneable only |
| Rive runtime | No (bake to Lottie instead) | Framer or free cloneable only |
| Unicorn Studio (WebGL) | No | Framer only — official embed path there |
| Lenis smooth scroll | No (use GSAP ScrollSmoother instead) | Free cloneable only |
| Standalone cursor/magnetic-button/image-trail JS | No | Free cloneable or Framer code component |

## Ranked scroll patterns (sellability out of 10, legality tag, exact Webflow build)

**Sticky stacking cards — 10/10, native.** Column of full-width cards, each `position: sticky`
with an incremental `top` offset (2rem, 4rem, 6rem...) inside a `position: relative` parent. Add
an IX2 "While scrolling in view" interaction per card scaling it to ~0.92 and dimming opacity as
the next card arrives. 3-6 cards is the sweet spot. GSAP ScrollTrigger pin+scrub is an optional
smoother upgrade. Reference: Sticky overlap ($12) and Parallax Image Stack ($12) Framer
components — https://www.framer.com/marketplace/components/sticky-overlap/ ·
https://www.framer.com/marketplace/components/parallax-image-stack/ · Adidas Annual Report 2024
— https://report.adidas-group.com/2024/en/

**Overflow-clip hover zoom with caption slide-up — 10/10, native.** Card image in an
`overflow: hidden` wrapper; hover scales the image 1.05-1.1 over 0.6-0.9s ease-out while a
caption/arrow slides up from the clipped bottom edge. Zero custom code — pure IX2 hover +
scale/move actions. Reference: Pesquera Diez / P10 by Mubien —
https://pesqueradiez.com/en/about · Duten (texture hover reveal) —
https://duten.com/en/finish/brushed-stainless-steel/

**Scroll-scrubbed text reveal (word/char) — 10/10, GSAP embed required.** IX2 alone only
animates whole text blocks. Use GSAP SplitText (free with GSAP) in a page-level embed splitting
into words/chars, ScrollTrigger scrub with stagger on opacity/y. Document the split target and
stagger value on the Instructions page. Reference: GSAP Text Animations (Timothy Ricks
cloneable) — https://webflow.com/made-in-webflow/gsapscrolltrigger · Sticky Text Reveal ($10
Framer component) — https://www.framer.com/marketplace/components/sticky-text-reveal/

**Kinetic typography reveal (per-char blur + y-offset, scroll or load) — 10/10, native as of May
2026.** Webflow's GSAP-powered Interactions panel now supports text splitting into chars/words/
lines with stagger, blur, and transform built in — no embed needed. Build as a class-based
interaction so buyers restyle by editing text only. Reference: MONOLOG (Awwwards SOTD Jul 2026)
— https://bymonolog.com · Ten Years Away — Studio375 — https://ten.375.studio/en

**Aurora / blur-morph gradient background — 10/10, native.** 3-5 large radial/conic-gradient
divs in brand hues, `filter: blur(80-150px)`, each slowly translating/scaling on a 10-20s loop
via a looping Interactions timeline. Zero embed. Expose the blob colors as Variables so buyers
recolor by hex swap. Reference: Linear — https://linear.app/homepage · Resend —
https://resend.com · Stripe — https://stripe.com

**Scroll-scrubbed Lottie — 9/10, native.** Dedicated Lottie element (JSON/dotLottie); scrub it
"while scrolling in view" or trigger on hover/click/load — explicitly native, no code. Reference:
LottieFiles Webflow plugin gallery — https://lottiefiles.com/plugins/webflow

**Pinned section with content swap (feature tour) — 9/10, native-first.** Sticky media column
beside a scrolling text column; IX2 "scroll into view" per text step cross-fades the matching
image (opacity/z-index). GSAP ScrollTrigger with `pin: true` + a timeline is the smoother pro
version, still content stays CMS-editable. Reference: Fey — https://fey.com/features/earnings ·
Apple iPad Pro — https://apple.com/ipad-pro

**Zoom-scrub media hero — 9/10, native.** Sticky inner container in a 200-300vh wrapper; IX2
"while scrolling in view" maps scroll progress to `scale` (0.6→1) and `border-radius`
(24px→0px). Reference: Sticky Zooming ($14 Framer component) —
https://www.framer.com/marketplace/components/sticky-zooming/ · Apple October 2020 remake
(Webflow cloneable) — https://apple-october-2020.webflow.io/

**Section wipes / curtain overlaps — 9/10, native.** Sections `position: sticky; top: 0` with
ascending z-index so each one naturally slides over the last. Footer-reveal variant: give the
body a `margin-bottom` equal to footer height and fix the footer behind it. Reference:
Petralithe — https://petralithe.com/en · Unseen 2025 Annual Report — https://2025.unseen.co/

**Cursor-following image/video preview on hover list — 9/10, native-first.** IX2 "mouse move in
viewport" drives a fixed image wrapper with smoothing; per-row hover toggles which image is
visible and dims sibling rows. Smoother version needs a small GSAP `quickTo()` embed for x/y.
Reference: Gianluca Gradogna — https://gianlucagradogna.com/through-this-lens

**Scroll marquee / velocity ticker — 9/10, native for constant speed; GSAP embed (use
cautiously) for velocity-reactive.** Basic infinite loop is a pure CSS keyframe embed
(duplicate content, `translateX(-50%)` loop, `animation-play-state: paused` on hover) or a
native IX2 loop — no risk either way. Velocity-reactive acceleration needs GSAP
ScrollTrigger/Observer — see the legality caveat above before relying on this for a marketplace
submission. Reference: Scroll Marquee (Timothy Ricks cloneable) —
https://webflow.com/made-in-webflow/gsapscrolltrigger

**Staggered grid/image reveal on viewport entry — 8/10, native.** IX2 "Scroll into view"
trigger on a parent with child stagger, animating opacity/translateY/clip. Build once as a
class-based interaction so it applies to any element the buyer tags with that class.

**Multi-layer parallax hero — 8/10, native.** IX2 "while page is scrolling" with different
move-Y amounts per layer (background 0-10%, foreground 30-50%); a fixed gradient overlay
animates opacity for the fade-out. The single most-cloned Webflow interaction pattern.
Reference: Firewatch parallax (Webflow cloneable) — https://fire-watch-parallax.webflow.io/

**Interactive Spline 3D hero — 8/10, native.** Native Webflow ↔ Spline integration: paste the
scene URL into the Spline element; hover/scroll interactions can drive scene states. No embed,
so it passes the no-custom-code rule outright. Include 2-3 alternate scenes plus a "swap the
scene" note on the Instructions page. Reference: THREE DIMENSIONS by Dirk Lach —
https://webflow.com/made-in-webflow/spline

**Video-first hero — 8/10, native.** Native Background Video element (auto-loops, muted); add a
poster image for mobile autoplay fallback. Do not scroll-pin the video — that needs custom code
and isn't worth the risk for this effect. Reference: Runway — https://runwayml.com

**Film grain / noise overlay — 8/10, native.** Fixed, `pointer-events: none` div with a tiled
noise PNG at 3-8% opacity; optional `steps()` background-position loop via Interactions for
animated grain. Reference: Awwwards texture collection —
https://www.awwwards.com/websites/texture/

**Scroll-linked theme/background color morph — 8/10, native-first.** IX2 "scroll into view" per
section changing `background-color`/text color on body and navbar over ~0.6s; a GSAP snippet
reading `data-theme` attributes per section is the cleaner buyer-facing version if you need one
script driving all sections. Reference: Hadaka — https://hadaka.jp/

**Scroll-driven product tour with canvas/video substitute — 9/10 concept, native via Lottie/
Spline substitute (7/10 with real canvas scrub).** Sticky wrapper + IX2 step-based crossfades is
fully native and marketplace-safe. A true canvas image-sequence scrub (the luxury/Apple-style
version) needs JS — substitute a scroll-scrubbed Lottie or Spline scene instead of shipping raw
canvas code. Reference: Apple iPad Pro — https://apple.com/ipad-pro

**Horizontal scroll section driven by vertical scroll — 8/10, native.** Outer wrapper 300-500vh
tall, inner `position: sticky` div at 100vh with `overflow: hidden`, horizontal flex track
inside; IX2 "while page is scrolling" maps 0-100% of the wrapper to `translateX` of the track.
GSAP ScrollTrigger (scrub + `containerAnimation` for nested triggers) is the smoother option.
Reference: Theo — https://www.theo.be/ · Canals Amsterdam — https://canals-amsterdam.com/

## Ranked micro-interaction patterns

**Animated link underlines — 8/10, small CSS embed.** `::after` pseudo-element with
`transform-origin` swap (`right` at rest, `left` on hover) on a global `.link` class — the exit-
to-right detail (instead of reversing) is what reads as premium. This is the professional route
for templates; a weaker per-instance IX2 hover-scale version is the zero-embed fallback.

**Premium easing recipe — 7/10, native.** IX2 supports custom cubic-bezier curves per action —
set `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) as the house curve on every interaction; use
per-element delay steps for staggers. Bake the curve into the Style Guide page as a stated
selling point. This single choice is what separates a template that "feels expensive" from one
with default easing everywhere.

**Marquee with hover-pause — 9/10, CSS/native.** Same construction as the scroll marquee above;
`animation-play-state: paused` on `:hover`.

**Hover-to-play video cards — 8/10, mostly native.** IX2 hover fades the video wrapper in/out.
Actually starting/stopping playback on hover needs a tiny script (`video.play()`/`.pause()`) —
if avoiding any embed, let the Webflow background-video autoplay continuously instead (fully
native, costs bandwidth not code).

**Blend-mode dot cursor with hover morph — 8/10, native + tiny CSS.** Fixed div (high z-index,
`pointer-events: none`) moved via IX2 "mouse move in viewport" with 50-90% smoothing for lag;
hover morphs via per-class hover interactions scaling the dot and revealing a text child. The
`mix-blend-mode: difference` + `cursor: none` needs a 3-line CSS embed — treat it like the
GSAP exception (document it) rather than a full JS library. Disable below ~992px. Reference:
Waaarhol — https://waaarhol.com/

**Character-split text on headings/links — 8/10, GSAP embed.** GSAP SplitText targeting
`[data-split]` attributes in a site-wide embed; ScrollTrigger for scroll-based reveals. Package
as one reusable embed file so buyers never touch code directly.

**Cursor-following preview / magnetic buttons / image trail — 6-7/10, GSAP embed, heavier
risk.** All three need a script: magnetic buttons via mousemove + GSAP elastic ease-back;
image trail via a GSAP-driven cycle through a CMS-bound (not code-bound) image list. Keep these
as optional, clearly documented embeds — or reserve them for a free cloneable rather than the
paid marketplace submission if in doubt.

## The premium dark-site formula (bonus combo recipe, 4 layers, all native/legal)

Near-black base + 3-5 aurora gradient blobs (blurred, animated) + a 4% opacity grain overlay +
one kinetic-typography heading + one marquee. Four CSS/native layers reproduce the look of a
much more expensive agency build with zero custom code beyond what's already listed above as
native. This is the visible signature across Resend, Cursor, Warp, Fey, and Osmo (Dark.design
corpus).

## What to leave for Framer only (or a free cloneable)

WebGL shader heroes (fluid/refraction/particles — the Vectr/Podium/Obys Experiment Space
aesthetic), Rive interactive state-machine characters, Unicorn Studio scenes, and Lenis-driven
smooth scroll are all real, sellable effects — just not inside a Webflow Marketplace
submission. If the client or template concept specifically wants one of these:
- Rebuild the visual with Spline (3D) or Lottie (character/vector) and ship that instead, or
- Record the effect once as an MP4 loop and use it as a native Background Video (the "baked
  WebGL" trick — 80% of the wow, 0% of the code risk, static preview buyers can't tell the
  difference), or
- Point the build at Framer, where Unicorn Studio has an official embed path and clean code
  components (Three.js, Rive) are explicitly allowed with no manual review.
