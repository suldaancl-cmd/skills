# Scroll & Scrollytelling Recipes

12 patterns from an audit of 110 sites across award galleries and the Webflow/Framer marketplaces. Sellability score is out of 10. "Shippable" = usable inside a marketplace template as-is; "cloneable-only" = Webflow blocks the custom-code version from marketplace submission, sell it as a paid cloneable instead.

---

## 1. Sticky stacking cards — sellability 10

**What it looks like:** A column of full-width cards; each pins via `position: sticky` at a small incremental top offset and the next card slides up over it, scaling down to ~0.92 and dimming as it gets buried. 3-6 cards is the sweet spot. Works for feature lists, services, case studies.

**Why it sells:** Zero asset requirements, works with any content a buyer drops in, demos instantly in a marketplace preview scroll.

**Example sites:** Sticky Overlap (Framer component, $12) — framer.com/marketplace/components/sticky-overlap/ · Parallax Image Stack (Framer, $12) · Sticky Projects (Framer, free) · Adidas Annual Report 2024 — report.adidas-group.com/2024/en/

**Webflow build (shippable):** Each card `position: sticky` inside a `position: relative` parent, top offsets stepped 2rem/4rem/6rem. IX2 "While scrolling in view" scales the card to 0.92 and drops opacity as the next card enters. No code. GSAP ScrollTrigger pin+scrub is the smoother upgrade path (now free in Webflow).

**Framer build (shippable):** Set each card's Position to Sticky within its section with staggered pin distances; add a Scroll Transform effect (scale 1→0.92 + opacity) tied to scroll progress. Native, no code.

**Performance note:** Pure CSS sticky + transform — cheapest recipe on this list, no measurable perf cost, safe at any card count up to ~6 before scroll length gets tedious.

---

## 2. Scroll-scrubbed text reveal (line/word/char) — sellability 10

**What it looks like:** Headlines split into lines/words/characters that animate in tied to scroll — staggered rise from clip-masks, or a "scrub fill" where grey text fills to full color word-by-word as you scroll a pinned paragraph.

**Why it sells:** Typography is the one asset every buyer already has; char/word reveals make plain text feel expensive and animate identically regardless of content.

**Example sites:** YesNo — yesnowww.com · Blux Studio — bluxstudio.com · GSAP Text Animations (Timothy Ricks cloneable) — webflow.com/made-in-webflow/gsapscrolltrigger · Sticky Text Reveal (Framer, $10)

**Webflow build:** IX2 alone only animates whole blocks. Per-line/word/char needs GSAP SplitText + ScrollTrigger — now free in Webflow after the GSAP acquisition, and Webflow Interactions become natively GSAP-powered for Marketplace templates from May 1, 2026 (native text-splitting, stagger, timelines — no embed). Ship any needed script in page settings so buyers never touch it.

**Framer build:** Native for appear-style reveals — Text effects animate per line/word/character on scroll into view. Scrub-fill (progress-linked color fill) needs a code component using `useScroll` + `useTransform` over split spans — sellable as an included component.

**Performance note:** Char-splitting on long headlines multiplies DOM nodes (one span per character) — keep it to H1/H2-length copy, not body paragraphs, or layout thrash on resize gets expensive.

---

## 3. Pinned section with content swap (scrollytelling feature tour) — sellability 9

**What it looks like:** A section pins for 2-4 viewport heights while content swaps in steps — a phone/dashboard mockup stays fixed while screenshots change as text scrolls past, or numbered feature steps light up sequentially.

**Why it sells:** Highest perceived-value block in a SaaS template — buyers see their own product tour in it.

**Example sites:** Quoti — getquoti.ai · BMW Group Report 2025 — bmwgroup.com/en/report/2025/index.html · Switch Content on Scroll (Timothy Ricks cloneable) · Shopify Editions Winter '26

**Webflow build (shippable):** Sticky media column beside a scrolling text column; IX2 "scroll into view" triggers on each text step cross-fade the corresponding image (opacity/z-index). GSAP ScrollTrigger pin:true + timeline is the smoother pro version, still one embed, content stays CMS-editable.

**Framer build (shippable):** Sticky position on the media frame within a tall section; Scroll Variant triggers (Appear/Scroll Section transitions) swap image variants as text blocks pass. No code.

**Performance note:** Keep swapped media to opacity/z-index cross-fades, not simultaneous video autoplay per step — stacking multiple background videos in one pinned section is the actual perf risk, not the pin itself.

---

## 4. Horizontal scroll section driven by vertical scroll — sellability 8

**What it looks like:** A 300-500vh tall track pins a viewport-height container and translates a row of panels on the X-axis as the user scrolls vertically. Used for project galleries, timelines, product lineups.

**Why it sells:** Breaks vertical monotony at exactly one moment — the one thing juries and preview-scrollers both notice.

**Example sites:** Theo — theo.be · Canals Amsterdam — canals-amsterdam.com · Nikola Radeski — nikolaradeski.com · Home Société — homesociete.ca/en/

**Webflow build (shippable):** Outer wrapper 300-500vh, inner sticky div 100vh + overflow hidden, horizontal flex track inside; IX2 "While page is scrolling" maps 0-100% of wrapper scroll to translateX of the track. GSAP ScrollTrigger (scrub + containerAnimation for nested triggers, free in Webflow) is the smoother option.

**Framer build (cloneable-only concept, but code allowed on Framer marketplace):** Not clean native — Framer's scroll effects don't remap vertical scroll to X translation across a pinned track. Use a code component/override with `useScroll` + `useTransform([0,1],['0%','-75%'])` on a sticky container. Several marketplace horizontal-scroll components exist to include.

**Performance note:** The tall wrapper (300-500vh) inflates page height/scrollbar feel — test on mobile where horizontal-scroll-via-vertical-scroll frequently needs a simplified (non-pinned, native horizontal swipe) fallback below ~768px.

---

## 5. Multi-layer parallax hero — sellability 8

**What it looks like:** 3-6 stacked layers (background, midground subject, foreground texture, headline) moving at different scroll speeds to fake depth — the Firewatch pattern. Modern versions add progressive darkening or a gradient fade blending into the next section.

**Why it sells:** The most recognized "premium" scroll effect among non-designer buyers — sells depth with plain PNGs, every layer is just a swappable image.

**Example sites:** Firewatch parallax (Webflow cloneable) — fire-watch-parallax.webflow.io · Cloudz — cloudz.webflow.io · Every Last Drop — everylastdrop.co.uk · OODOS — oodos.life

**Webflow build (shippable):** IX2 "While page is scrolling" with different move-Y amounts per layer (background 0-10%, foreground 30-50%); add a fixed gradient overlay animating opacity for the fade-out. No code — the most-cloned Webflow interaction pattern.

**Framer build (shippable):** Native Scroll Transform "Parallax"/speed effect per layer directly on canvas — Framer's own blog documents building it no-code. Fastest recipe to reproduce in Framer.

**Performance note:** The OODOS "gradient fade exit" trick (a translucent gradient overlay blending the parallax hero into the next section) solves the hard-edge problem that kills most parallax heroes cheaply — one more div, no JS.

---

## 6. Zoom-scrub media hero (framed → full-bleed) — sellability 9

**What it looks like:** An image or muted video starts framed mid-viewport and, while its section is pinned, scales up to full-bleed (or the inverse) scrubbed to scroll position. Apple-style product-page energy.

**Why it sells:** Massive wow-per-effort: one media element + one scale transform reads as cinematic; buyers only replace one image.

**Example sites:** Sticky Zooming (Framer, $14) · Apple October 2020 remake (Webflow cloneable) — apple-october-2020.webflow.io · Chanel J12 Watch — chanel.com/us/watches/the-j12-watch/ · GlobalLeathers — global-leathers-digitalbutlers.webflow.io

**Webflow build (shippable):** Sticky inner container in a 200-300vh wrapper; IX2 "While scrolling in view" maps scroll progress to scale (0.6→1) and border-radius (24px→0). GSAP ScrollTrigger scrub gives the frame-perfect version.

**Framer build (shippable):** Sticky position + Scroll Transform scale/border-radius tied to section progress. One of the few "expensive-looking" effects Framer does entirely no-code.

**Performance note:** One media element scaling is cheap; if the "media" is background video, ensure a poster frame for mobile since autoplay can be blocked there.

---

## 7. Scroll-scrubbed video / image-sequence — sellability 7

**What it looks like:** A pinned full-screen video or pre-rendered image sequence whose playhead binds to scroll position — scroll forward, product rotates/explodes; scroll back, reverses. Flagship luxury product scrollytelling pattern.

**Why it sells:** Highest wow-factor on this beat — how Chanel, Ray-Ban and top SOTD sites present hardware.

**Example sites:** Singula Team - Chizzy — chizzy.singula.team/3/ · Ray-Ban Meta · Chanel J12 Watch · iCoMat — icomat.co.uk

**Webflow build (cloneable-only):** IX2 cannot scrub video. Custom code only: GSAP ScrollTrigger driving `video.currentTime` (unreliable on iOS) or the robust way — a `<canvas>` image sequence (100-150 JPG/WebP frames) drawn per scroll progress. Ship the script + a documented frames folder. Not marketplace-legal as-is; sell as a cloneable.

**Framer build (shippable):** Not native. Requires a code component using `useScroll` to drive canvas frame drawing or video `currentTime`. Legal and sellable on Framer marketplace, but flag the asset burden (100+ frames) for buyers.

**Performance note:** 100-150 JPG/WebP frames is real asset weight (often 5-20MB+ per sequence) — always preload progressively and provide a static-image fallback for slow connections/reduced-motion users.

---

## 8. Section wipes / curtain overlaps — sellability 9

**What it looks like:** Each full-height section pins as the next slides over it (dark wipes over light, footer revealed from "under" the page), sometimes with the buried section scaling down or a "portal" window scrolling slower than its content.

**Why it sells:** Cinematic rhythm across an entire multi-section page with pure CSS — no assets, no code — instantly differentiates from flat-card competitors in a preview scroll.

**Example sites:** Petralithe — petralithe.com/en · Unseen 2025 Annual Report — 2025.unseen.co · GlobalLeathers (sticky-frame portal) · Melvin Winkeler — melvinwinkeler.com

**Webflow build (shippable):** Sections `position: sticky; top: 0` with ascending z-index; next section naturally slides over. Reveal-footer variant: body `margin-bottom` = footer height, footer fixed behind it. Optional IX2 scale-down on the buried section.

**Framer build (shippable):** Sticky sections stacking with z-index, add Scroll Transform scale/opacity on the outgoing section. No code.

**Performance note:** Pure sticky/z-index — no JS, no measurable cost. The reveal-footer variant needs the body margin set precisely to footer height or you get a gap/overlap glitch; test at multiple footer content lengths (CMS-driven footers can vary height).

---

## 9. Lenis-style smooth scroll + inertia feel — sellability 8

**What it looks like:** Normalized, eased scrolling (lerp ~0.1) that makes every other scroll effect feel "liquid," sometimes paired with velocity-based skew/distortion on images. Invisible in screenshots but the #1 thing separating award sites from flat templates once you actually scroll.

**Why it sells:** The texture of the entire page — every reviewer touches the scrollbar within one second; buyers describe it as "the expensive feel" without knowing why.

**Example sites:** Cuberto — cuberto.com · Dogstudio — dogstudio.co · Blux Studio · Made With Gsap — madewithgsap.com

**Webflow build (cloneable-only... but see exception):** Custom code embed: Lenis (~3KB) initialized site-wide in footer code, synced with GSAP ScrollTrigger via `lenis.on('scroll', ScrollTrigger.update)`. GSAP ScrollSmoother is free in Webflow now and is an alternative. Both are still embeds — not shippable on marketplace as-is; document "position:fixed elements must live outside the smooth wrapper" for buyers regardless of channel.

**Framer build (cloneable-only concept, shippable as code component):** No global native toggle — use a Lenis override/code component applied at page level (community overrides exist). Framer's built-in scroll effects still work on top. Verify anchor-link behavior after adding it.

**Performance note:** Smooth-scroll libraries intercept the native scroll event — always test anchor links, focus-jump accessibility, and any `position: fixed` elements after adding it; these are the most common regressions buyers report.

---

## 10. Scroll marquee / velocity-reactive ticker — sellability 9

**What it looks like:** Infinite horizontal text or logo strip whose direction/speed responds to scroll velocity — scroll faster, it accelerates; scroll up, it reverses. Often doubles as a section divider with giant outlined display type.

**Why it sells:** Cheap, content-agnostic motion filling dead zones between sections; reads as "designed" in a 3-second preview.

**Example sites:** Scroll Marquee (Timothy Ricks cloneable) · Made With Gsap · Brandin — designbybrandin.com · Zajno Motion — motion.zajno.com

**Webflow build:** Basic loop is native IX2 (looping move animation on a duplicated track) — shippable. Velocity-reactive version needs a GSAP embed (ScrollTrigger + ObserverPlugin, or the classic velocity → timeScale snippet) — cloneable-only on marketplace.

**Framer build (shippable):** Native — Framer ships a built-in Ticker/Marquee component; speed-on-scroll reactivity needs a small override reading scroll velocity from Framer Motion's `useVelocity`.

**Performance note:** The constant-speed native version has zero perf cost; ship that as the marketplace default and offer velocity-reactivity as a documented "upgrade with this embed" add-on, not the baseline.

---

## 11. Staggered grid/image reveal on scroll into view — sellability 8

**What it looks like:** Cards, grid images, or list rows animate in with a 50-100ms stagger (y-rise + fade from a clipped mask) the first time they enter the viewport. The baseline "everything animates in" polish layer across an entire template.

**Why it sells:** Lowest-effort, highest-coverage pattern — upgrades every section at once and never breaks regardless of buyer content. Its absence is what makes templates feel dead.

**Example sites:** scroll-animation-image-grid (Skylar Kitchen cloneable) · Snowhouse Studio Year in Review 2024 · Hadaka — hadaka.jp · Four Pillars Studio — fourpillars.studio

**Webflow build (shippable):** IX2 "Scroll into view" trigger on a parent with child stagger, applying opacity/translateY/clip. Build it once as a class-based interaction so buyers get it on any element they tag with that class.

**Framer build (shippable):** Native Appear effects with per-child stagger and layout transitions — Framer's core strength, zero code.

**Performance note:** Apply the stagger class broadly (it's cheap per-element), but cap simultaneous animating children in one viewport to ~12-15 or the stagger reads as a delay rather than a ripple on large grids.

---

## 12. Scroll-linked theme/background color morph — sellability 8

**What it looks like:** Page background, text color, and navbar smoothly cross-fade between color themes as sections scroll into view (light hero → dark features → colored CTA), keeping nav legible throughout.

**Why it sells:** Makes one page feel like multiple "chapters" — the cheapest scrollytelling signal there is; demos strongly in preview videos.

**Example sites:** Navbar Color Change + Color Scroll (Timothy Ricks cloneables) · Hadaka · Un Verano Sin Ti — unveranosinti.tilda.ws · Frequency Breathwork — frequencybreathwork.com

**Webflow build (shippable):** IX2 "Scroll into view" triggers per section changing background-color/text color on body and navbar with a 0.6s ease; or one GSAP snippet reading `data-theme` attributes per section (cleaner for buyers — they just tag sections, but that variant is cloneable-only).

**Framer build:** Scroll Variant switching on the navbar component per section, plus section background transitions — native. A tiny override on data-attributes makes it fully automatic (code, still shippable on Framer).

**Performance note:** Keep the transition to background-color/color only (both cheap, compositor-friendly properties) — avoid animating box-shadow or filter on the same trigger, which is where this pattern starts to jank on lower-end devices.
