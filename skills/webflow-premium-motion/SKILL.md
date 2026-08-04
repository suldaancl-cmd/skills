---
name: webflow-premium-motion
description: Use when adding premium custom-code motion (GSAP, ScrollTrigger, Lenis, WebGL) to a Webflow site without breaking the Designer-editable workflow. Covers where to inject scripts (Project vs Page Settings vs Embed), correct GSAP+ScrollTrigger+Lenis load order on top of Webflow's bundled jQuery, when to keep native IX2 vs take over with GSAP, a reusable per-site premium-motion.css/.js pattern with a window config object, fixed WebGL/Spline/canvas backgrounds, and the CDN/reduced-motion pitfalls that silently break Webflow builds.
---

# Webflow Premium Motion (GSAP · ScrollTrigger · Lenis · WebGL)

Add agency-tier motion to a Webflow site with custom code, **without** turning the
project into something only a developer can edit. Webflow already ships jQuery and
runs its own Interactions (IX2) engine, so the goal is to layer GSAP/Lenis *cooperatively*,
drive everything off `data-` attributes and combo-classes, and fail gracefully when a
CDN is down. Real production reference using exactly this stack (Webflow + jQuery 3.5.1
+ GSAP 3.11 + ScrollTrigger + lenis@1): **xshack.app**.

Docs: Webflow custom code https://help.webflow.com/hc/en-us/articles/33961356331923 ·
GSAP install https://gsap.com/docs/v3/Installation/ · ScrollTrigger
https://gsap.com/docs/v3/Plugins/ScrollTrigger/ · Lenis https://www.lenis.dev/ +
https://github.com/darkroomengineering/lenis

---

## 1. WHERE to inject code

Three placement surfaces, in order of scope:

| Surface | Path | Scope | Use for |
|---|---|---|---|
| **Project custom code** | Project Settings → Custom Code | Every page | Global CSS (`<head>`), library `<script>` + init (`</body>`) |
| **Page custom code** | Page Settings → (open page) → Custom Code | One page | Page-only effect (a single hero canvas, one scrolljack) |
| **Embed block** | Add element → Embed (≤ 50 000 chars) | One element/section | Inline markup the animation targets (`<canvas>`, SVG, a config snippet) |

Hard rules:

- **Scripts that touch the DOM go in the *Before `</body>`* slot**, never in `<head>`.
  At `</body>` the DOM and Webflow's own `webflow.js` are parsed, so `$` and your
  target elements exist. `<head>` is for `<style>`, fonts, and meta only.
- **CSS goes in the *Inside `<head>`* slot** (Project for site-wide, Page for one page),
  wrapped in `<style>…</style>`.
- Project-level custom code only renders on the **published** site (`*.webflow.io`
  staging or your domain), **not** in the Designer canvas or Preview. Always test on
  the published staging URL.
- Page custom code runs *after* project custom code — load libraries at Project level,
  then reference them in Page code.

---

## 2. GSAP + ScrollTrigger + Lenis on Webflow — load order & snippet

Webflow injects **jQuery 3.5.x** itself (served from CloudFront), so `$` is already
global — **do not add another jQuery**; you'll get conflicts. Just use `$`.

GSAP is free as of the Webflow/GreenSock acquisition — load from any CDN, no token.
Order matters: **gsap core → ScrollTrigger plugin → Lenis → your init**.

Put this in **Project Settings → Custom Code → Before `</body>`**:

```html
<!-- 1. GSAP core + ScrollTrigger (free; verified 200) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
<!-- 2. Lenis smooth scroll — note the package is `lenis`, NOT @studio-freight/lenis -->
<script src="https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js"></script>

<!-- 3. Init (jQuery `$` is already provided by Webflow) -->
<script>
  $(function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Guard: if any library failed to load, bail without throwing.
    if (typeof gsap === 'undefined') return;
    gsap.registerPlugin(ScrollTrigger);

    // Lenis (skip entirely for reduced-motion users)
    if (typeof Lenis !== 'undefined' && !reduce) {
      var lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
      window.__lenis = lenis; // expose for anchor links / pause-on-modal
    }

    // Drive animations off DATA-ATTRIBUTES + combo-classes so the site stays
    // editable: a content editor adds the class/attribute in the Designer,
    // no code change needed.
    gsap.utils.toArray('[data-anim="fade-up"]').forEach(function (el) {
      if (reduce) return;
      gsap.from(el, {
        opacity: 0,
        y: parseInt(el.getAttribute('data-anim-y') || 40, 10),
        duration: 0.9,
        ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 85%' }
      });
    });
  });
</script>
```

The `gsap.ticker.add(…lenis.raf(t*1000))` + `lagSmoothing(0)` pattern is the
**official Lenis↔GSAP sync** (https://www.lenis.dev/). Don't run a separate
`requestAnimationFrame` loop for Lenis when GSAP is present — driving Lenis from
GSAP's ticker keeps ScrollTrigger and the smooth scroll on one clock.

**Editability discipline:** never hard-code element selectors like `.hero-h1-wrapper-2`.
Target `[data-anim]` attributes or a stable combo-class (e.g. `.u-anim-stagger`) the
client can apply/remove in the Designer. Read tunables (`data-anim-y`, `data-anim-delay`,
`data-stagger`) off the element so non-devs adjust motion without touching JS.

Also turn **off** Webflow's native smooth-scroll when Lenis is on:
Project Settings → check the page interactions, and in Page Settings disable
"Smooth scrolling" — otherwise the two scroll systems fight.

---

## 3. Webflow IX2 vs GSAP — when to use which

Webflow's native **Interactions 2.0 (IX2)** is enough; reach for GSAP only when it isn't.

**Stay on native IX2 when:**
- Simple hover/tap states, dropdown/menu reveals, basic load fades.
- A single "while scrolling in view" parallax or opacity tween.
- The client must self-edit the interaction in the Designer with zero code.

**Take over with GSAP/ScrollTrigger when:**
- **Pinning + scrubbing** a section (horizontal scroll, sticky scrollytelling) — IX2
  has no real `pin`/`scrub` timeline.
- **Staggered timelines** with shared eases across many elements (`gsap.timeline()`).
- **Scrub-linked** WebGL/canvas/SVG values (IX2 can't drive arbitrary JS variables).
- You need `ScrollTrigger.matchMedia` / `gsap.matchMedia()` for responsive logic, or
  `lagSmoothing`, `FLIP`, `SplitText`, etc.

**Don't double-animate one element with both engines** — pick IX2 *or* GSAP per element.
If GSAP owns it, leave that element's IX2 panel empty. After GSAP mutates layout (e.g.
appended split-text spans), call `ScrollTrigger.refresh()` once on `window.load`.

---

## 4. Reusable multi-site pattern (config object + guards)

Ship the same two files to every Webflow client, customize per site via **one config
object** loaded *before* the script. Keeps each site identical in code, different in data.

**A. Per-site config — Project Settings → Custom Code → Before `</body>`, ABOVE the library block:**

```html
<script>
  // Per-site knobs. The shared premium-motion.js reads this; never edit the JS per site.
  window.__PREMIUM_MOTION_SITE = {
    slug: 'xshack',          // client identifier
    profile: 'cinematic',    // 'minimal' | 'editorial' | 'cinematic' — preset bundle
    effect: 'fixed-canvas'   // hero treatment: 'none' | 'fixed-canvas' | 'spline'
  };
</script>
```

**B. premium-motion.css** — `<head>` slot. Ship verbatim per site:

```html
<style>
  /* hide-then-reveal so GSAP-animated elements don't flash at full opacity (FOUC) */
  [data-anim] { will-change: transform, opacity; }
  .pm-prep [data-anim] { opacity: 0; }            /* class added by JS only if motion runs */
  @media (prefers-reduced-motion: reduce) {
    [data-anim] { opacity: 1 !important; transform: none !important; }
  }
  #pm-bg-canvas { position: fixed; inset: 0; z-index: -1; pointer-events: none; }
</style>
```

**C. premium-motion.js** — the shared init. Same on all sites; branches on the config.
Wrap **all** GSAP/Lenis usage in guards so a failed CDN never blanks the page (the
`[data-anim]` reveal CSS above guarantees content is visible if JS dies):

```html
<script>
  $(function () {
    var CFG = window.__PREMIUM_MOTION_SITE || { profile: 'minimal', effect: 'none' };
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var hasGSAP = typeof gsap !== 'undefined';

    if (!hasGSAP || reduce) return;            // graceful: native page stands on its own
    document.documentElement.classList.add('pm-prep');
    gsap.registerPlugin(ScrollTrigger);

    if (typeof Lenis !== 'undefined') {
      var lenis = new Lenis({ lerp: CFG.profile === 'cinematic' ? 0.08 : 0.12 });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
      window.__lenis = lenis;
    }

    // shared, attribute-driven animations (same across every site) …
    gsap.utils.toArray('[data-anim="fade-up"]').forEach(function (el) {
      gsap.from(el, { opacity: 0, y: 40, duration: 0.9, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 85%' } });
    });

    if (CFG.effect === 'fixed-canvas' && typeof initBgCanvas === 'function') initBgCanvas();
    if (CFG.effect === 'spline')      { /* lazy-load spline-viewer; see §5 */ }

    window.addEventListener('load', function () { ScrollTrigger.refresh(); });
  });
</script>
```

Per site you only change **the config object** (A) and which `effect` hook fires —
never the shared CSS/JS. New client = copy two files, set 3 config keys.

---

## 5. WebGL / Spline / canvas embeds

Pattern: a **fixed full-viewport canvas behind the content**, content layered above.

- Add a `<canvas id="pm-bg-canvas">` via an **Embed block** at the top of the page (or
  inject it from JS). CSS (from §4): `position:fixed; inset:0; z-index:-1; pointer-events:none;`
  so it sits behind everything and never eats clicks. Give your above-the-fold sections
  `position: relative; z-index: 1` in the Designer so they paint over it.
- **Three.js**: load `three.min.js` from a CDN in the `</body>` block *after* GSAP, then
  drive uniforms/camera from a ScrollTrigger `scrub` or `gsap.ticker`. Cap the pixel ratio
  (`renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`) and `pause` the RAF loop when
  the canvas is off-screen to protect mobile battery. (xshack.app does exactly this:
  Webflow + Three.js + GSAP + Lenis.)
- **Spline**: use the web component instead of hand-rolling WebGL —
  `<script type="module" src="https://unpkg.com/@splinetool/viewer@1/build/spline-viewer.js"></script>`
  then a `<spline-viewer url="…">` in an Embed. Lazy-load it (insert on `load` or via
  IntersectionObserver) so it doesn't block first paint. Same fixed-background CSS applies.
- Respect `prefers-reduced-motion`: skip starting the WebGL loop entirely for those users
  and show the static Webflow background/section instead.

---

## 6. PITFALLS

- **`@studio-freight/lenis` CDN 404.** The package was **renamed to `lenis`**. The old
  `@studio-freight/lenis@1` path can 404 on jsDelivr. Use
  `https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js` (resolves to 1.3.x) or pin an
  exact version, e.g. `https://unpkg.com/lenis@1.3.23/dist/lenis.min.js`.
- **Always include `prefers-reduced-motion`.** Gate every tween, the Lenis instance, and
  any WebGL loop on `matchMedia('(prefers-reduced-motion: reduce)').matches`. The CSS in
  §4 also force-resets `[data-anim]` to visible/no-transform for these users.
- **Verify CDN URLs return 200 before shipping.** A single broken `<script>` silently
  kills the whole init. Quick check: `curl -I https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js`
  (expect `200`). Verified-good as of writing: gsap@3 → 3.15.0, gsap@3 ScrollTrigger → 3.15.0,
  lenis@1 → 1.3.23. **Pin a major version (`@3`, `@1`)** so a future breaking release can't
  ambush a live client site — never load an unpinned `@latest`.
- **Don't add jQuery.** Webflow already loads it; a second copy breaks `$`. Just use `$`
  (or `window.Webflow.push(fn)`); if you prefer no jQuery, use plain
  `document.addEventListener('DOMContentLoaded', …)`.
- **Project code is invisible in Designer/Preview** — test on the published staging URL,
  not the canvas. Republish after every custom-code change (it only ships on publish).
- **ScrollTrigger positions wrong after async content** (web fonts, images, Spline, split
  text). Call `ScrollTrigger.refresh()` on `window.load` and after any layout-changing JS.
- **Lenis vs Webflow native smooth-scroll / anchor links.** Disable Webflow's smooth scroll
  when Lenis is active, and route in-page anchors through Lenis:
  `window.__lenis && window.__lenis.scrollTo(targetEl)`.
- **50 000-character Embed limit** and a per-site custom-code size budget — keep big logic
  in CDN-hosted files, not pasted inline.
