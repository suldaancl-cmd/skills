---
name: premium-preloader-intro
description: >-
  Build a real award-site preloader and the loader-to-hero reveal handoff:
  a genuine 0-to-100 counter driven by ACTUAL asset loading (Promise.all over
  images/fonts/GLTF, document.fonts.ready, image decode) — never a fake
  setTimeout — plus scroll-lock during load, minimum-display-time, first-visit
  vs repeat via sessionStorage, and ONE GSAP timeline that wipes the loader and
  hands off into the hero entrance. Fire this whenever building a preloader,
  loading screen, loader, intro / opening animation, page reveal, splash, or
  curtain / mask / clip-path wipe — especially on immersive, cinematic,
  awwwards / award-style, scroll-driven, GSAP, Lenis, or Three.js / WebGL / 3D
  sites, and on Next.js / SSR apps that must avoid FOUC and protect LCP and
  Core Web Vitals.
---

# Premium preloader + intro choreography

Every award-winning site opens the same way: a loader that tracks *real* work,
then a choreographed reveal that hands the viewer straight into the hero. The
whole trick is honesty. The counter must count actual bytes, the reveal must
start the frame loading finishes, and the hero must already be composed
underneath so the wipe uncovers a live page, not a second load.

This skill codifies that handoff with GSAP (timelines + SplitText) and Lenis
(scroll lock). GSAP core and every plugin, including SplitText and
ScrollTrigger, are free on public npm as of v3.13, so no auth token is needed.

## When to reach for this

- The brief says preloader, loading screen, splash, intro, opening, reveal,
  curtain, or "make the entrance feel premium."
- The site has heavy hero assets (large images, a video poster, a webfont
  headline, a Three.js/WebGL scene) that would otherwise pop in ugly.
- You caught yourself about to write `setTimeout(() => hideLoader(), 2500)`.
  Stop. That is the anti-pattern this skill exists to kill.

## Quick start

```bash
npm install gsap lenis
```

```js
import { gsap } from "gsap";
import Lenis from "lenis";

// Minimal honest loader: count real image loads, then reveal.
const imgs = [...document.querySelectorAll("img")];
let loaded = 0;

Promise.all(
  imgs.map(async (img) => {
    // decode() resolves only once the bitmap is ready to paint, not just fetched
    if (img.complete && img.naturalWidth) { /* already cached */ }
    else await new Promise((r) => (img.onload = img.onerror = r));
    try { await img.decode(); } catch {}
    loaded++;
    counterEl.textContent = Math.round((loaded / imgs.length) * 100);
  })
).then(reveal); // reveal() runs a single GSAP timeline — see recipe 2
```

The counter moves because `loaded` moves. Nothing is faked.

## The mental model

Four things run in order. Keep them as four separate, testable pieces:

1. **Track** real progress (recipe 1). A promise per asset; a fraction resolved.
2. **Lock** the scroll while the loader is up (recipe 3), so the page can't be
   scrolled behind the overlay.
3. **Reveal** on one GSAP timeline (recipe 2): finish the counter, wipe the
   overlay, and start the hero entrance as overlapping steps of the *same*
   timeline so there is no seam.
4. **Gate** first-visit vs repeat and honor reduced-motion / slow links
   (recipes 4 and 5), so returning users and constrained devices skip the show.

## Recipe 1: A counter that tells the truth

Progress is the fraction of real work done. Weight assets if some dominate (a
5MB GLTF should not count the same as a favicon), but never invent numbers.

```js
// preload.js
export function preloadAssets({ images = [], fonts = true, onProgress }) {
  const tasks = [];

  // Images: wait for load, then decode so the first paint can't stutter.
  for (const src of images) {
    tasks.push(() => new Promise((resolve) => {
      const img = new Image();
      img.onload = () => img.decode().then(resolve, resolve);
      img.onerror = resolve; // a failed asset must not hang the loader forever
      img.src = src;
    }));
  }

  // Fonts: document.fonts.ready resolves when all @font-face loads settle.
  if (fonts) tasks.push(() => document.fonts.ready);

  const total = tasks.length;
  let done = 0;
  return Promise.all(
    tasks.map((run) =>
      run().then(() => {
        done++;
        onProgress?.(done / total); // 0..1, monotonic
      })
    )
  );
}
```

```js
// usage: a real 0 -> 100
preloadAssets({
  images: ["/hero.jpg", "/texture.webp", "/logo.png"],
  onProgress: (p) => {
    // ease the *display* toward the true value so it never jumps or reverses
    gsap.to(state, {
      value: p * 100,
      duration: 0.4,
      ease: "power2.out",
      onUpdate: () => (counterEl.textContent = Math.round(state.value)),
    });
  },
}).then(reveal);
```

Easing the *display* toward the real value (rather than snapping) is the one
honest smoothing allowed: the target is always the true fraction, so the number
can lag by a few hundred ms but can never lie or run backward.

Why `decode()`: `onload` fires when bytes arrive, but the browser may still owe
you a decode before it can paint. Awaiting `img.decode()` moves that cost inside
the loader, so the hero reveal is jank-free. See
[MDN: HTMLImageElement.decode()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decode).

## Recipe 2: One timeline for the whole reveal

Put the counter finish, the loader wipe, and the hero entrance on a single
`gsap.timeline()`. Overlap them with the position parameter (`"-=0.4"`,
`"<"`) so the eye reads one continuous move, not three cuts.

```js
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(SplitText);

function reveal() {
  // Compose the hero split BEFORE the wipe so lines are ready to animate in.
  const split = new SplitText(".hero__title", { type: "lines", linesClass: "line" });

  const tl = gsap.timeline({
    defaults: { ease: "expo.inOut" },
    onComplete: () => split.revert(), // restore clean DOM for a11y + resize
  });

  tl
    // 1. let the counter land on 100 and hold a beat
    .to(state, { value: 100, duration: 0.3, onUpdate: () => (counterEl.textContent = 100) })
    // 2. curtain wipe: reveal the page by shrinking the overlay's clip-path
    .to(".preloader", {
      clipPath: "inset(0 0 100% 0)", // wipe upward; page shows through
      duration: 1.1,
    }, "+=0.15")
    .set(".preloader", { pointerEvents: "none" })
    // 3. hero entrance overlaps the tail of the wipe — no seam
    .from(split.lines, {
      yPercent: 120,
      opacity: 0,
      duration: 1,
      stagger: 0.08,
      ease: "power4.out",
    }, "-=0.6")
    .from(".hero__media", { scale: 1.15, duration: 1.4, ease: "power3.out" }, "<");

  return tl;
}
```

```css
.preloader {
  position: fixed;
  inset: 0;
  z-index: 9999;
  clip-path: inset(0 0 0 0); /* fully covering at start */
}
.hero__title .line { overflow: hidden; } /* mask the yPercent slide */
```

Alternative wipes, same one-timeline rule: a **curtain split** (two halves
sliding opposite ways via `xPercent`), a **scale-out** (`scale: 0` on a masked
panel), or an **SVG/clip mask** wipe. Codrops documents mask-based reveals in
depth (see References). Pick one; do not stack three.

## Recipe 3: Lock the scroll, then release it

While the overlay is up the page must not scroll. Lock at both layers: Lenis
(so its rAF loop stops advancing) and the body (so native scroll can't leak).

```js
import Lenis from "lenis";

const lenis = new Lenis({ autoRaf: true });
lenis.stop();                          // pause smooth scroll during load
document.documentElement.classList.add("is-loading");

// ...after the reveal timeline STARTS releasing (not before), let scroll back:
function releaseScroll() {
  document.documentElement.classList.remove("is-loading");
  lenis.start();
}
```

```css
html.is-loading,
html.is-loading body { overflow: hidden; height: 100%; }
```

Call `releaseScroll()` from the reveal timeline — e.g. add it as a callback
partway through the wipe with `tl.add(releaseScroll, "-=0.8")` so scrolling
returns exactly as the hero appears, not a moment early.

If you drive ScrollTrigger with Lenis, wire them once (per Lenis docs):

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000)); // if you drive raf via gsap, set autoRaf:false
gsap.ticker.lagSmoothing(0);
```

Use `autoRaf: true` for the standalone loop, OR drive `lenis.raf` from
`gsap.ticker` with `autoRaf: false` — not both, or you run two loops.

## Recipe 4: First visit vs repeat, and minimum display time

Show the full choreography once. On repeat visits within the session, skip
straight to the page. And never let a fast connection make the loader flash for
80ms — hold a floor so it reads.

```js
const KEY = "intro-seen";
const MIN_MS = 900; // floor so a cached load still registers as intentional

async function boot() {
  const firstVisit = !sessionStorage.getItem(KEY);
  if (!firstVisit) { skipIntro(); return; } // no overlay, no lock

  lenis.stop();
  const startedAt = performance.now();

  await preloadAssets({ images: HERO_IMAGES, onProgress: paintCounter });

  // hold the floor: real load may finish before MIN_MS
  const elapsed = performance.now() - startedAt;
  if (elapsed < MIN_MS) await new Promise((r) => setTimeout(r, MIN_MS - elapsed));

  sessionStorage.setItem(KEY, "1");
  reveal().add(releaseScroll, "-=0.8");
}
```

The `setTimeout` here is a *floor on a real load*, not a substitute for one —
that distinction is the whole point. `sessionStorage` (not `localStorage`) is
usually right: fresh tab gets the show, in-session navigations do not. Swap to
`localStorage` only if the client wants once-per-device.

## Recipe 5: Respect reduced motion and slow connections

A preloader is motion and it delays content, so it is exactly what
`prefers-reduced-motion` and constrained networks should short-circuit.

```js
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

// navigator.connection is Chromium-only and experimental — feature-detect it.
const conn = navigator.connection;
const slow = conn && (conn.saveData || /2g/.test(conn.effectiveType || ""));

if (reduce || slow) {
  skipIntro();     // remove overlay, unlock scroll, no wipe, no counter theatrics
} else {
  boot();
}

function skipIntro() {
  gsap.set(".preloader", { display: "none" });
  document.documentElement.classList.remove("is-loading");
  lenis.start();
}
```

Under reduced motion, prefer an instant cut or a plain opacity fade over any
transform-based wipe. `navigator.connection` / `effectiveType` / `saveData` are
experimental and absent in Safari and Firefox, so the `&&` guard is load-bearing
(see [MDN: NetworkInformation](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation)).

## React / Next.js integration

A preloader touches `window`, `document.fonts`, and layout — all client-only.
Mount it after hydration and clean up GSAP on unmount so timelines don't leak
across route changes.

```jsx
"use client";
import { useEffect, useRef } from "react";
import { gsap } from "gsap";
import Lenis from "lenis";

export default function Preloader() {
  const root = useRef(null);

  useEffect(() => {
    const lenis = new Lenis({ autoRaf: true });
    lenis.stop();

    // gsap.context scopes selectors to this subtree and reverts on cleanup
    const ctx = gsap.context(() => {
      boot(lenis); // your recipe-4 flow, scoped
    }, root);

    return () => {
      ctx.revert();   // kills every tween/timeline created in the context
      lenis.destroy();
    };
  }, []);

  return <div ref={root} className="preloader" aria-hidden="true" />;
}
```

SSR cautions that keep LCP and CLS clean:

- Render the hero markup on the server. The overlay sits *on top* via
  `position: fixed`, so the LCP element is already in the DOM and painting
  underneath — the loader must not block or replace it.
- Keep the overlay's initial covered state in CSS (`.preloader{clip-path:inset(0)}`),
  not in a JS `useEffect`, or there is a flash of the page before JS runs (FOUC).
- Reserve space for hero media with width/height or aspect-ratio so revealing it
  causes zero layout shift.
- Guard `window` / `navigator` access behind `useEffect` or `typeof window`;
  they do not exist during server render.
- Do not `stop()` Lenis on the server; instantiate it inside `useEffect`.

## Performance

- Preload only above-the-fold, LCP-critical assets. Counting every image on the
  page just makes users wait for things they can't see yet.
- Do heavy decode work off the paint path: `img.decode()` and
  `createImageBitmap()` keep bitmap prep off the main thread's critical moment.
- One rAF loop, one timeline. Two competing loops (Lenis `autoRaf` plus a manual
  `gsap.ticker` feed) double the work and desync.
- A fake timer loader is a measurable Core Web Vitals regression: it delays LCP
  by design and adds nothing. Real progress that finishes early is strictly
  better for the user and the metric.

## Accessibility

- `aria-hidden="true"` on the overlay; it is decoration, not content.
- Honor `prefers-reduced-motion` (recipe 5) with a cut or fade, never a big
  transform.
- Move focus to a real landmark after reveal, and ensure the released page is
  keyboard-scrollable (the body unlock in recipe 3 handles this).
- Revert SplitText (`split.revert()`) after the entrance so screen readers and
  copy/paste see intact text, not per-line spans.

## Pitfalls

- **The fake `setTimeout` loader.** It lies about progress, delays LCP on
  purpose, and users learn to distrust it. A real counter that hits 100 in 300ms
  is a feature, not a bug.
- **A counter that jumps to 100 then waits.** Means the number was never tied to
  load state. Bind it to the resolved fraction (recipe 1).
- **Blocking the main thread during load.** Synchronous decode/parse of a big
  asset freezes the counter animation itself. Await `decode()`; keep parsing async.
- **FOUC before the loader mounts.** The covered state must be in server-rendered
  CSS, not applied by JS after hydration.
- **Layout shift on reveal.** Un-reserved hero media shoves content when it
  appears. Reserve dimensions.
- **Two rAF loops.** `autoRaf: true` and a `gsap.ticker` feed at once. Choose one.
- **Loader on every navigation.** Gate with `sessionStorage` (recipe 4) so
  returning users are not punished.
- **A hang on a failed asset.** Every promise needs an `onerror`/`.catch` that
  still resolves, or one 404 freezes the loader forever.

## Going further

Advanced material — preloading a Three.js / WebGL hero (GLTF, textures,
`THREE.LoadingManager`), weighted progress across mixed asset types, and a
fuller Next.js App Router pattern — lives in
[references/webgl-and-frameworks.md](references/webgl-and-frameworks.md).

## References

Grounded in the official docs fetched while authoring this skill:

- GSAP install, imports, `registerPlugin`, and the 3.13 free-for-all:
  https://gsap.com/docs/v3/Installation
- GSAP v3 docs hub (Timeline, Tween, plugins): https://gsap.com/docs/v3/
- Lenis README (options, `raf`, `stop()`/`start()`, `scrollTo`, ScrollTrigger
  wiring): https://github.com/darkroomengineering/lenis
- Codrops preloader tag and mask-reveal tutorials:
  https://tympanus.net/codrops/tag/preloader/ and
  https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/
- MDN, `HTMLImageElement.decode()`:
  https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decode
- MDN, `document.fonts` / FontFaceSet `ready`:
  https://developer.mozilla.org/en-US/docs/Web/API/Document/fonts
- MDN, NetworkInformation (`effectiveType`, `saveData`):
  https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation
