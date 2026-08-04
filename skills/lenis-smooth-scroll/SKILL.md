---
name: lenis-smooth-scroll
description: Use when adding smooth/inertial scroll to a website, normalizing wheel/trackpad/touch input across browsers, building a scroll-driven hero, or pairing with GSAP ScrollTrigger for buttery scroll. Triggers — "smooth scroll", "scroll feels janky", "Lenis", "smooth scrolling library", "scroll lerp", "inertia scroll", "@studio-freight/lenis".
---

# Lenis — smooth scroll library

Lenis (by Darkroom Engineering, formerly Studio Freight) is a tiny (~3KB), framework-agnostic library that turns the browser's native scroll into a buttery, lerped, RAF-driven scroll. It preserves accessibility (real `scrollTop`, links and anchors still work) while fixing the trackpad/wheel inconsistency that makes scroll-driven sites feel cheap.

**Key fact (keep current):** Studio Freight rebranded to **Darkroom Engineering** in 2024 and **renamed the package from `@studio-freight/lenis` → `lenis`** (v1.0, late 2024). Old docs reference the legacy path. Use `lenis`, not the scoped name.

## When to reach for Lenis

Use Lenis when:
- The hero is scroll-driven and the default browser scroll feels stuttery on Mac trackpads vs Windows wheels
- You need a **single normalized scroll value** to drive ScrollTrigger, IntersectionObserver, or custom animations
- The user wants the "agency website" feel — momentum + slight lerp, not just CSS `scroll-behavior: smooth`
- You're building a horizontal-scroll page or pinned cinematic section

**Do NOT use** when:
- GSAP `ScrollSmoother` (free since 3.13) is already in the project — pick one, not both
- The site is content-heavy and accessibility-first (reading-flow sites): default scroll is fine and respects user preferences
- The user has `prefers-reduced-motion: reduce` — disable Lenis, fall back to native

## Install

```bash
npm install lenis
```

CDN (prototypes):
```html
<script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>
```

## Core pattern (vanilla)

```js
import Lenis from 'lenis';

const lenis = new Lenis({
  duration: 1.2,            // smoothness — higher = more lerp (default 1.2)
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),  // expo.out
  smoothWheel: true,
  smoothTouch: false,       // KEEP FALSE — mobile native scroll is better
  wheelMultiplier: 1,
  touchMultiplier: 2,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
```

That's the entire setup. Everything else is configuration.

## Pair with GSAP ScrollTrigger (the killer combo)

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis();
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

This hands the RAF loop to GSAP's ticker and feeds every Lenis scroll event to ScrollTrigger. Now every `scrollTrigger: { scrub: true }` tween follows Lenis's lerped scroll — perfectly synced.

## React pattern

```bash
npm install lenis
```

```jsx
'use client';
import { useEffect } from 'react';
import Lenis from 'lenis';

export default function SmoothScroll({ children }) {
  useEffect(() => {
    const lenis = new Lenis();
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    return () => lenis.destroy();
  }, []);
  return children;
}
```

Wrap your `<body>` content in `<SmoothScroll>` at the root. Next.js App Router: client component only.

There's also an official wrapper: `npm install lenis @studio-freight/react-lenis` (still under old scope; Darkroom hasn't migrated this yet) — provides `<ReactLenis root>` and `useLenis()` hook. Cleaner for big React apps.

## API quick reference

| Method | What it does |
|---|---|
| `lenis.scrollTo(target, opts)` | Scroll to selector / element / number. `opts: { offset, duration, easing, lock, force, onComplete }` |
| `lenis.start()` / `lenis.stop()` | Pause/resume smooth scrolling (e.g., during a modal) |
| `lenis.on('scroll', cb)` | Subscribe — receives `{ scroll, limit, velocity, direction, progress }` |
| `lenis.raf(time)` | Tick the loop — must be called every frame |
| `lenis.destroy()` | Cleanup — call on unmount |

## Configuration cheat-sheet

```js
new Lenis({
  duration: 1.2,        // scroll lerp duration (s). 0.6 = snappy, 1.5 = floaty
  easing: t => ...,     // custom easing function
  smoothWheel: true,    // smooth desktop wheel (always true for the effect)
  smoothTouch: false,   // touch — false is correct 99% of cases
  wheelMultiplier: 1,   // wheel sensitivity
  touchMultiplier: 2,
  orientation: 'vertical',  // 'horizontal' for sideways pages
  gestureOrientation: 'vertical',
  lerp: 0.1,            // alternative to duration — linear interpolation factor
  infinite: false,      // loop scroll (rare)
  autoResize: true,
});
```

## Common patterns

### Anchor links (still work natively, but with lerp)
```js
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    lenis.scrollTo(a.getAttribute('href'), { offset: -80 });
  });
});
```

### Pause Lenis during a modal
```js
openModal.addEventListener('click', () => lenis.stop());
closeModal.addEventListener('click', () => lenis.start());
```

### Respect reduced-motion
```js
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const lenis = new Lenis({ smoothWheel: !reduced, smoothTouch: false });
```

### Horizontal scroll
```js
new Lenis({ orientation: 'horizontal', gestureOrientation: 'horizontal' });
```

## Gotchas

1. **`position: fixed` + Lenis** — fixed elements work fine, but `position: sticky` inside a Lenis page needs no special handling. Lenis touches only `scrollTop`, not transforms.
2. **`smoothTouch: true` is wrong** — iOS Safari's inertia is hand-tuned; replacing it with Lenis lerp feels worse, not better. Leave touch native.
3. **Hash links on page load** — Lenis won't auto-scroll to `#section` on initial load. Manually call `lenis.scrollTo(window.location.hash, { immediate: true })` after init.
4. **`scrollIntoView()` doesn't work** — bypass Lenis. Always use `lenis.scrollTo()`.
5. **iframes / nested scroll** — Lenis hijacks the root scroll. Internally-scrollable elements (`overflow: auto`) still work, but you can't smooth them too without a separate Lenis instance with `wrapper`/`content` options.
6. **SSR (Next.js App Router)** — Lenis touches `window`. Run only in `useEffect` / `'use client'`.
7. **GSAP ScrollSmoother conflict** — both lerp the page. Pick one. ScrollSmoother is now free (GSAP 3.13) and integrates tighter with ScrollTrigger; Lenis is smaller and more flexible. For pure GSAP projects, ScrollSmoother wins. For React-heavy or mixed-animation projects, Lenis wins.

## Quick decision guide

| Need | Reach for |
|---|---|
| Add inertia to a marketing site | Lenis vanilla setup |
| GSAP-driven cinematic page | Lenis + ScrollTrigger pattern above |
| Already using ScrollSmoother | Stay with ScrollSmoother, don't add Lenis |
| Horizontal hero | `orientation: 'horizontal'` |
| Just need anchor links smooth | Native `scroll-behavior: smooth` — don't pull in a library |

## Related

See also: `gsap-scrolltrigger` (the canonical scroll-trigger toolkit), `web-designer/references/motion.md` (broader motion-library decision guide), `three` (for scroll-driven 3D scenes — pair Lenis + R3F + `useScroll`).
