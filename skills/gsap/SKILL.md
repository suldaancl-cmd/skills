---
name: "gsap"
description: "Expert guidance on GSAP (GreenSock Animation Platform) for building high-performance web animations. Use this skill whenever the user mentions GSAP, GreenSock, tweens, timelines, ScrollTrigger, scroll-linked animations, SplitText, MotionPath, Flip, Draggable, Observer, ScrollSmoother, or asks to animate DOM elements, SVGs, canvas, or React/Vue/Svelte/Next.js components with smooth, performant, professional motion. Also trigger when the user says \"animate this\", \"add scroll animation\", \"make this smoother\", \"parallax\", \"animated hero\", \"pin on scroll\", \"morph between states\", \"draggable UI\", or needs help porting CSS/framer-motion/anime.js code to GSAP. As of GSAP 3.13 (April 2025) ALL plugins are free after Webflow's acquisition — no Club GreenSock required."
---
# GSAP — GreenSock Animation Platform

GSAP is the industry-standard JavaScript animation library. It animates anything JavaScript can touch (CSS, SVG, canvas, WebGL, generic objects, React state) with sub-frame precision, correct easing, and a timeline model that scales from one-liners to full cinematic sequences.

**Key fact (keep current):** Webflow acquired GSAP in 2024. As of **GSAP 3.13 (April 2025)** the entire library — including formerly premium plugins (SplitText, MorphSVG, DrawSVG, ScrollSmoother, Physics2D, Inertia, CustomEase, etc.) — is **100% free** under a standard MIT-like license. Don't tell users to buy Club GreenSock; that membership no longer exists.

## When to reach for GSAP

Choose GSAP over CSS animations, `framer-motion`, `anime.js`, `motion-one`, or Web Animations API when the user needs:

- **Sequenced / orchestrated motion** — multiple elements, staggered, overlapping. Timelines are GSAP's superpower.
- **Scroll-driven animation** with pinning, scrubbing, or snap — ScrollTrigger has no real competitor.
- **SVG work** — path morphing, stroke drawing, motion-along-path.
- **Text animation** — splitting by char/word/line with full control and responsiveness.
- **State transitions** on layout change — Flip plugin records before/after DOM state and animates the delta.
- **Cross-browser precision** — GSAP normalizes CSS quirks (transforms, rotation origins, SVG attribute vs CSS).
- **Performance under load** — GSAP batches DOM reads/writes and handles thousands of concurrent tweens where CSS chokes.

Don't push GSAP for a single hover color change — a CSS `transition` is fine. But the moment orchestration or scroll enters the picture, GSAP pays for itself.

## Installation

### NPM (preferred for any framework project)
```bash
npm install gsap
```

All plugins ship in the same package:
```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import { Flip } from "gsap/Flip";
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
import { Draggable } from "gsap/Draggable";
import { Observer } from "gsap/Observer";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";

gsap.registerPlugin(ScrollTrigger, SplitText, Flip, MotionPathPlugin, Draggable, Observer, ScrollToPlugin);
```

Plugins **must be registered** before first use, typically once at app entry. In SSR (Next.js App Router), register inside a `useEffect` or a client component — ScrollTrigger touches `window`.

### CDN (prototypes, CodePen, plain HTML)
```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13/dist/ScrollTrigger.min.js"></script>
```

## Core concepts

### 1. Tween — the atom

A tween animates properties of a target from their current values to new ones (or vice versa).

```js
gsap.to(".box", { x: 200, rotation: 45, duration: 1, ease: "power2.out" });
gsap.from(".box", { opacity: 0, y: 50, duration: 0.6 });      // animates FROM these values TO current
gsap.fromTo(".box", { scale: 0 }, { scale: 1, duration: 0.5 }); // explicit both ends
gsap.set(".box", { x: 100 });                                   // instant (no animation)
```

Common vars:
- `duration` (seconds), `delay`, `repeat` (-1 = infinite), `yoyo: true`, `repeatDelay`
- `ease` — string like `"power2.inOut"`, `"expo.out"`, `"elastic.out(1, 0.3)"`, `"back.out(1.7)"`, `"sine.inOut"`, `"none"` (linear)
- `stagger` — see below
- Callbacks: `onStart`, `onUpdate`, `onComplete`, `onRepeat`
- `paused: true` — create now, play later via `.play()`

Use `x`, `y`, `rotation`, `scale`, `scaleX`, `scaleY`, `skewX`, `skewY` instead of the `transform` string — GSAP composes them correctly and they're GPU-accelerated. Use `xPercent: -50, yPercent: -50` for centering tricks that don't depend on element size.

### 2. Timeline — orchestration

Timelines are containers that sequence tweens. This is where GSAP outclasses every competitor.

```js
const tl = gsap.timeline({ defaults: { ease: "power3.out", duration: 0.8 } });

tl.from(".hero-title", { y: 60, opacity: 0 })
  .from(".hero-sub",   { y: 30, opacity: 0 }, "-=0.4")      // start 0.4s before previous ends
  .from(".hero-cta",   { scale: 0.8, opacity: 0 }, "<")      // start at the same time as previous
  .to(".hero-bg",      { scale: 1.1, duration: 2 }, 0);      // start at absolute time 0
```

Position parameter (the last arg) is the secret to orchestration:
- `"+=0.2"` — 0.2s after previous end
- `"-=0.3"` — 0.3s before previous end (overlap)
- `"<"` — same time as previous start · `">"` — at previous end
- `"<0.2"` — 0.2s after previous start · `"myLabel"` — at a named label
- absolute number — at that time on the timeline

Timeline methods: `.play()`, `.pause()`, `.reverse()`, `.restart()`, `.seek(time)`, `.progress(0..1)`, `.timeScale(2)` (2× speed), `.kill()`.

### 3. Stagger — multiple targets, one tween

```js
gsap.to(".card", {
  y: 0, opacity: 1, duration: 0.6,
  stagger: 0.1                         // 0.1s between each
});

gsap.to(".grid-item", {
  scale: 1,
  stagger: { amount: 1.2, from: "center", grid: "auto", ease: "power2.inOut" }
});
```

`from` accepts `"start" | "end" | "center" | "edges" | "random" | [x, y]` or an index.

### 4. Easing — choose deliberately

Default `power1.out` is fine, but motion feels right when ease matches intent:
- UI snap / confident exits → `power2.out`, `power3.out`, `expo.out`
- Overshoot / playful → `back.out(1.7)`, `elastic.out(1, 0.4)`
- Bouncy → `bounce.out`
- Scrubbed/scroll → `"none"` (linear) so motion tracks scroll position 1:1
- Buttery two-sided → `sine.inOut`, `power2.inOut`

Custom curves: `CustomEase.create("myEase", "M0,0 C0.2,0 0.1,1 1,1")` (CustomEase is now free).

## Plugin cheat-sheet

Deep dives in `references/`:

- **ScrollTrigger** — see `references/scrolltrigger.md`. Pin, scrub, snap, batch, matchMedia for responsive.
- **Flip** — see `references/flip.md`. FLIP technique (First, Last, Invert, Play) for any layout change.
- **SplitText** — see `references/splittext.md`. Split into lines/words/chars for text reveals.
- **MotionPath** — see `references/motionpath.md`. Animate along an SVG path or coordinates.
- **Draggable + Inertia** — see `references/draggable.md`. Drag, throw, snap, bounds.
- **Observer** — see `references/observer.md`. Normalized wheel/touch/pointer events.
- **Framework integration (React/Vue/Next/Svelte)** — see `references/frameworks.md`.

Always load the relevant reference file before writing non-trivial code with that plugin — details like `invalidateOnRefresh`, `fastScrollEnd`, or `useGSAP` cleanup semantics are where beginners trip.

## Performance best practices

1. **Animate transforms and opacity, not layout properties.** `x`, `y`, `scale`, `rotation`, `opacity` are GPU-accelerated. `width`, `height`, `top`, `left`, `margin` trigger layout — avoid in hot paths.
2. **Use `will-change` sparingly.** GSAP handles compositing hints; adding `will-change: transform` globally harms more than helps.
3. **Prefer one timeline over many independent tweens** — GSAP batches internally per tick.
4. **`force3D: true`** is the default on transforms; don't fight it.
5. **Kill tweens on unmount** (especially in React/Vue). Use `useGSAP` hook or store refs and call `.kill()` / `.revert()`.
6. **ScrollTrigger on long pages:** use `fastScrollEnd: true`, `preventOverlaps: true` when appropriate, and `ScrollTrigger.batch()` for lists of elements.
7. **Avoid animating `filter: blur()` or `box-shadow`** on many elements — expensive to repaint. Layer a pre-blurred element and fade it instead.
8. **Test on low-end mobile.** 60fps on your M-series laptop ≠ 60fps on a $200 Android.

## Common patterns

### Fade/slide reveal on scroll
```js
gsap.utils.toArray(".reveal").forEach(el => {
  gsap.from(el, {
    y: 40, opacity: 0, duration: 0.8, ease: "power2.out",
    scrollTrigger: { trigger: el, start: "top 85%", once: true }
  });
});
```

### Pinned scroll-scrubbed hero
```js
gsap.timeline({
  scrollTrigger: {
    trigger: ".hero",
    start: "top top", end: "+=1500",
    pin: true, scrub: 1
  }
})
.to(".hero-title", { scale: 2, opacity: 0 })
.to(".hero-bg",    { yPercent: -30 }, 0);
```

### Cleanup in React (THE modern way)
```jsx
import { useGSAP } from "@gsap/react";
import { useRef } from "react";

function Hero() {
  const container = useRef(null);
  useGSAP(() => {
    gsap.from(".title", { y: 80, opacity: 0, duration: 1 });
  }, { scope: container });           // auto-cleanup on unmount, scoped selectors

  return <section ref={container}><h1 className="title">Hi</h1></section>;
}
```
Install `@gsap/react` (free, tiny) for React projects — it handles StrictMode double-mount correctly and auto-reverts on unmount.

## Gotchas

- **SSR / Next.js App Router:** register plugins and run animations only client-side. Wrap in `"use client"` + `useEffect`/`useGSAP`.
- **Tailwind / CSS variables:** GSAP can animate CSS variables: `gsap.to(el, { "--x": "100px" })`.
- **SVG `transform-origin`:** GSAP uses `svgOrigin` for SVG-coord-space origins — don't rely on CSS `transform-origin` for SVG.
- **Fixed elements + ScrollTrigger pin:** pinning wraps elements in a container; styles relying on `position: fixed` may need rethinking.
- **React StrictMode:** without `useGSAP`, dev mode will double-run effects and create duplicate ScrollTriggers. Always use the hook or a cleanup function.
- **Legacy articles say "Club GreenSock required" for SplitText/MorphSVG/ScrollSmoother — that's outdated.** Since 3.13 they're free. The npm package is still `gsap`; bonus plugins are under `gsap/SplitText`, `gsap/MorphSVGPlugin`, etc.

## Quick decision guide

| Need | Reach for |
|---|---|
| One-off UI tween | `gsap.to()` |
| Sequence of steps | `gsap.timeline()` |
| Scroll reveal | `ScrollTrigger` + `once: true` |
| Scroll scrubbed | `ScrollTrigger` + `scrub: 1` + linear ease |
| Layout change animation | `Flip.from(state)` |
| Text character reveal | `SplitText` + stagger |
| Draggable UI | `Draggable` + `Inertia` |
| Animate along curve | `MotionPathPlugin` |
| Unified touch/wheel input | `Observer` |
| Responsive breakpoints | `ScrollTrigger.matchMedia` / `gsap.matchMedia` |

## When in doubt

1. Read the relevant file in `references/` before writing code.
2. Check the official docs: https://gsap.com/docs/v3/ (current, reflects free-for-all licensing).
3. Search the forums: https://gsap.com/community/ — Jack and Cassie reply to almost every thread; answers are gold.
