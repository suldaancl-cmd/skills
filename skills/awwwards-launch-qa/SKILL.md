---
name: awwwards-launch-qa
description: Use before launching a premium / animation-heavy / WebGL website — a performance, accessibility, and motion QA checklist that catches the failures that tank Core Web Vitals, break keyboard users, and trigger motion sickness on otherwise beautiful builds. Verified against 2026 web.dev CWV thresholds (LCP/INP/CLS), Three.js bundle budgets, and Lenis/GSAP smooth-scroll guidance. Invoke when work is "done" but not yet shipped, when a site uses scroll-jacking / parallax / 3D, or when an Awwwards-tier build needs an evidence-not-vibes sign-off.
---

# Awwwards Launch QA

Beautiful sites fail launch on three things judges and users both punish: a slow/janky first interaction, a keyboard trap, and motion that makes people sick. This is the pre-flight checklist. Work top to bottom. Every box is either checked with **evidence** (a number, a screenshot, a passing command) or it is not done.

**Rule: evidence, not vibes.** "Feels smooth" is not a pass. A p75 INP number from a real device is. If you cannot produce the evidence for a box, it stays unchecked and ships as a known risk — written down, not hand-waved.

Create a TodoWrite item per section so nothing is skipped under launch pressure.

---

## 1. PERFORMANCE budget

Core Web Vitals are measured at the **75th percentile** of real field traffic, segmented mobile/desktop. Lab numbers (Lighthouse) are a proxy — the field is the verdict. Source: [web.dev/articles/inp](https://web.dev/articles/inp), [web.dev — defining CWV thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds).

### Core Web Vitals targets (2026)
- [ ] **LCP (Largest Contentful Paint) ≤ 2.5 s** (good). 2.5–4.0 s = needs improvement, > 4.0 s = poor.
- [ ] **INP (Interaction to Next Paint) ≤ 200 ms** (good). 200–500 ms = needs improvement, > 500 ms = poor. INP **replaced FID** as a Core Web Vital on **2024-03-12** — it measures *every* interaction's full lifecycle (input delay + processing + presentation), not just the first input. It is the most-failed CWV in 2026, so treat it as the headline metric for animation-heavy sites.
- [ ] **CLS (Cumulative Layout Shift) ≤ 0.1** (good). 0.1–0.25 = needs improvement, > 0.25 = poor.
- [ ] LCP image: explicit `width`/`height` (or `aspect-ratio`), `fetchpriority="high"`, preloaded, served as AVIF/WebP. No lazy-load on the LCP element.
- [ ] Fonts: `font-display: swap` (or `optional`), self-hosted/preloaded, `size-adjust` to kill the swap-induced CLS.
- [ ] Reserve space for every async element (images, embeds, ads, injected banners) so nothing reflows after paint → protects CLS.

### WebGL / 3D budget
Three.js core ships **~600 KB minified** before any scene, model, or texture — and it is **not meaningfully tree-shakeable**. A full stack (loaders + controls + postprocessing + draco/ktx2 decoders) routinely exceeds **3 MB**. Source: [utsubo — 100 Three.js tips (2026)](https://www.utsubo.com/blog/threejs-best-practices-100-tips), [Evil Martians — OffscreenCanvas + workers](https://evilmartians.com/chronicles/faster-webgl-three-js-3d-graphics-with-offscreencanvas-and-web-workers).

- [ ] **Defer the 3D bundle past first paint** — dynamic `import()` the Three.js chunk; it must NOT block LCP. The hero text/image paints first; the canvas hydrates after.
- [ ] **Below-the-fold 3D is lazy-loaded** via `IntersectionObserver` — don't init a scene the user may never scroll to.
- [ ] **Move shader compile + parsing off the main thread**: render in a **Web Worker via `OffscreenCanvas`** (`transferControlToOffscreen()`). Shader linking is the single biggest main-thread stall on init; on a 1080p display a fragment shader runs ~2M times/frame (8M at 4K), so a blocking compile spikes INP hard.
- [ ] **Textures: KTX2 (Basis Universal)** — stays GPU-compressed, ~10× less VRAM than PNG/JPG. Run assets through **`gltf-transform`** (KTX2 + Draco/meshopt + dedupe + prune) before shipping. No raw 4K PNGs in a `.glb`.
- [ ] **Draw-call budget: < 100 desktop, < 50 mobile.** Merge geometry / use instancing to stay under.
- [ ] **Mobile gets a static fallback** — a poster image or CSS-only version, not the full WebGL scene. Gate on device capability / `navigator.hardwareConcurrency` / reduced-motion, not just viewport width.
- [ ] Dispose discipline: `geometry.dispose()`, `material.dispose()`, `texture.dispose()`, `renderer.dispose()` on unmount/route-change — no leaked GPU memory across SPA navigations.
- [ ] Cap `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))` — never render at full DPR on a 3× phone.

---

## 2. SCROLL / MOTION risk

JS smooth-scroll (Lenis, Locomotive) **hijacks the native scroll** and re-drives it on the main thread every frame. Done wrong it is a top source of poor **INP**; done right it has no measurable LCP/CLS cost and can even *improve* INP by replacing janky native behavior. Source: [Lenis (darkroom.engineering)](https://github.com/darkroomengineering/lenis), [orchestrating-gsap-lenis](https://skills.rest/skill/orchestrating-gsap-lenis).

- [ ] **Sync Lenis to one RAF loop, not two.** Set Lenis `autoRaf: false` and drive it from `gsap.ticker` (`gsap.ticker.add((t) => lenis.raf(t * 1000))`, then `gsap.ticker.lagSmoothing(0)`). Two separate `requestAnimationFrame` loops make ScrollTrigger read a 1–2-frame-stale scroll value → jitter + mis-fired triggers.
- [ ] **Keep active ScrollTriggers under ~30.** Each is a scroll-time read; a few hundred turns every scroll frame into a long task → INP > 200 ms.
- [ ] **Prefer scroll-*position* triggers over scroll-*jacking*.** Reveal/pin on position is cheap and accessible. Forcing the user through a fixed timeline (full-page scrolljacking) degrades INP *and* measurably hurts conversion — users fight the page. If you must jack, scope it to one section, never the whole document.
- [ ] No layout thrash in scroll callbacks — read all geometry, then write. Never read `offsetTop`/`getBoundingClientRect` and mutate styles in the same handler.
- [ ] `ScrollTrigger.refresh()` after fonts/images load and on resize, so trigger positions aren't computed against a pre-layout DOM.
- [ ] Throttle/rAF any custom `scroll`/`pointermove` handlers; passive listeners (`{ passive: true }`) where you don't `preventDefault`.

---

## 3. ACCESSIBILITY

For users with vestibular disorders, reducing motion is a **medical necessity** — parallax, large slide-ins, and zoom transitions can cause dizziness, nausea, and migraines. This is not a nice-to-have. Source: [web.dev — prefers-reduced-motion](https://web.dev/articles/prefers-reduced-motion), [motion.dev — accessibility](https://motion.dev/docs/react-accessibility).

### Reduced motion (CSS **and** JS)
- [ ] **CSS**: a global `@media (prefers-reduced-motion: reduce)` block that kills/shortens animations, removes parallax, stops auto-playing carousels/loops, and disables scroll-driven transforms. Keep small opacity fades (< 200 ms), focus-ring transitions, and progress indicators — don't nuke *all* motion, reduce the vestibular-triggering kind.
- [ ] **JS**: read `window.matchMedia('(prefers-reduced-motion: reduce)')` before building GSAP timelines / starting Lenis / initializing WebGL camera moves. CSS alone does NOT stop JS-driven animation. Use `gsap.matchMedia()` to branch reduced vs full. Lenis: don't smooth-scroll (or drop to instant) when reduced is set.
- [ ] Listen for live changes (`mql.addEventListener('change', …)`) — users toggle the OS setting mid-session.

### Keyboard & focus with hijacked scroll
Scroll-jacked / pinned sections can "hang" the viewport when tabbing, and focus can land **behind** an animated element. Source: [GSAP forums — ScrollTrigger & tabindex accessibility](https://gsap.com/community/forums/topic/29639-gsap-scrolltrigger-and-accessibility-via-tabindex/).

- [ ] **Tab through the entire page with the mouse untouched.** Focus order is logical, nothing is skipped, the viewport follows focus into pinned/jacked sections (no dead hang).
- [ ] Off-screen / not-yet-revealed content that animates in is **not focusable early** — set `tabindex="-1"` (or `inert`) while hidden, restore when revealed.
- [ ] When scroll is hijacked, **manually `element.focus()`** the target section/heading on navigation so keyboard + screen-reader users land where sighted users do. Pair with `scroll-margin-top` for anchor targets under sticky headers.
- [ ] Visible focus indicator on every interactive element — never `outline: none` without a replacement. Survives the dark/cinematic theme (check contrast of the ring itself).
- [ ] A **"skip to content"** link, and skip links past any long scroll-driven intro.

### Contrast & safe animation properties
- [ ] Text contrast ≥ **4.5:1** (normal) / **3:1** (large ≥ 24px or 18.66px bold); UI/icon contrast ≥ 3:1. Re-check text sitting over video/3D/gradient heroes — the worst frame, not the best.
- [ ] **Only animate compositor-friendly properties: `transform`, `opacity`, `filter`, `clip-path`.** Never animate layout props (`width`, `height`, `top`, `left`, `margin`) — they trigger layout + paint every frame → jank + INP cost. Use `transform: translate/scale` instead.
- [ ] `will-change` used sparingly (a handful of elements, removed after the animation) — not slapped on everything.
- [ ] No flashing > 3×/second (seizure risk, WCAG 2.3.1).

---

## 4. CROSS-DEVICE

The phone is where CWV is judged and where the GPU is weakest. The desktop hero is not the product — the mobile experience is.

- [ ] **Motion downgrade on mobile**: fewer/disabled parallax layers, shorter timelines, simpler easing. A scroll story that sings on a trackpad can be nauseating and janky on a thumb-scrolled phone.
- [ ] **WebGL downgrade on mobile**: lower DPR (`min(devicePixelRatio, 1.5–2)`), fewer particles, smaller render targets, reduced shader resolution / disabled postprocessing, lower poly LODs.
- [ ] Real-device test (or throttled DevTools: 4× CPU + Slow 4G) on a **mid-tier Android**, not just the latest iPhone — that's where the 75th-percentile user lives.
- [ ] Touch targets ≥ 44×44 px; hover-only affordances have a tap/visible equivalent.
- [ ] Test landscape, small-height viewports, and the iOS dynamic toolbar (`100svh`/`100dvh`, not `100vh`).
- [ ] No horizontal scroll / overflow at 320 px width; safe-area insets respected on notched devices.

---

## 5. SHIP VERIFICATION

The proof-of-work gate. Each line produces an artifact you can paste into the report. No artifact → not shipped.

- [ ] **Every external asset returns HTTP 200.** CDN scripts (GSAP, Lenis, Three.js, fonts), model/texture URLs, OG image. Check each:
      `curl -sI <url> | findstr /R "HTTP"` (PowerShell) — confirm `200`, no `403`/`404`/`canceled`.
- [ ] **`node --check` passes on every authored JS/MJS file** — no syntax errors reach the browser. Loop the bundle/source files; zero non-zero exits.
- [ ] **Playwright smoke run is green** with these explicit assertions:
  - [ ] `page.on('console')` collected array is **`[]`** — zero console errors/warnings on load and after a full scroll-through.
  - [ ] `await page.evaluate(() => !!window.gsap)` is **true** (and `!!window.ScrollTrigger` if used).
  - [ ] Lenis present — `window.lenis` (or your exposed instance) is defined; smooth scroll actually advances `scrollY` on wheel.
  - [ ] No unhandled `pageerror` events.
  - [ ] **Screenshots captured** at hero, mid-scroll, and footer — desktop **and** mobile viewport — and eyeballed for broken layout / missing 3D / FOUC.
  - [ ] A `prefers-reduced-motion` run (`browser.newContext({ reducedMotion: 'reduce' })`) loads with motion suppressed and **no console errors**.
- [ ] **Field/lab CWV captured**: a Lighthouse (mobile preset) or PageSpeed Insights run attached, with LCP/INP/CLS numbers recorded against the §1 targets. Note any metric in needs-improvement/poor as a tracked risk.

### Evidence-not-vibes report format
Close every QA pass with this block — it is the launch sign-off:

```
## Launch QA — <site> — <date>
PERFORMANCE   LCP <x.x s>  INP <x ms>  CLS <x.xx>     [pass / risk]
WEBGL         3D bundle <x KB deferred: y/n>  draw calls <n>  mobile fallback <y/n>
MOTION        active ScrollTriggers <n>  Lenis↔ticker synced <y/n>  scrolljack scope <none/section/page>
A11Y          reduced-motion CSS+JS <y/n>  keyboard tab-through <pass/fail>  min contrast <ratio>
CROSS-DEVICE  mid-Android tested <y/n>  mobile motion+DPR downgraded <y/n>
SHIP          CDN 200s <n/n>  node --check <pass>  Playwright <pass>  console errors <[]>
SCREENSHOTS   <paths — desktop + mobile>
KNOWN RISKS   <bullets, or "none">
VERDICT       SHIP / HOLD
```

A box left unchecked is allowed — lying that it's checked is not. List it under KNOWN RISKS and let a human decide SHIP/HOLD.
