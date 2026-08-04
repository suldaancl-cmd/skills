# Motion — CSS, Motion (Framer Motion), GSAP

Motion is not decoration. Motion signals causality, hierarchy, and state. Every tween should teach the user something or it's noise.

**For deep GSAP work, load the full `gsap` skill** — it has the complete API, ScrollTrigger, Flip, SplitText, Draggable, and framework integration. This file is the higher-level "which tool and when".

## The hierarchy — pick the lightest tool that works

| Need | Tool |
|---|---|
| Simple hover, focus, state transition | CSS transition |
| Keyframe animation, looping, entry | CSS animation |
| Physics, gestures, drag (React) | Motion (fka Framer Motion) |
| Orchestration, sequencing, timelines | GSAP |
| Scroll-linked, pinned, scrubbed | GSAP ScrollTrigger |
| Path morphing, SVG effects, text splitting | GSAP + plugins |
| 3D / WebGL | Three.js / R3F + drei `useSpring` / GSAP |

Don't use GSAP for a single hover color change. Don't use CSS for a 12-step sequenced reveal across 30 elements.

## Easing — the single most important motion choice

Default `ease-in-out` is the hallmark of generic AI motion. Replace it.

**Custom cubic-beziers that feel expensive:**

```css
--ease-out-expo:   cubic-bezier(0.16, 1, 0.3, 1);        /* punchy deceleration */
--ease-out-quint:  cubic-bezier(0.22, 1, 0.36, 1);       /* softer than expo */
--ease-apple:      cubic-bezier(0.32, 0.72, 0, 1);       /* Apple's signature */
--ease-in-out-circ: cubic-bezier(0.85, 0, 0.15, 1);      /* dramatic two-sided */
--ease-spring:     cubic-bezier(0.175, 0.885, 0.32, 1.275); /* tiny overshoot */
```

**Rule of thumb:**
- UI state changes → `ease-out` variants (punchy, confident)
- Scroll-linked → `linear` / `"none"` (motion must match scroll 1:1)
- Two-sided transitions (modal open/close) → `ease-in-out` family, custom beziers only
- Playful overshoot → spring or `back.out(1.4)` in GSAP

## Duration — most AI motion is too fast

| Context | Range |
|---|---|
| UI micro-transition (hover, focus) | 150–250ms |
| UI state change (modal, drawer) | 250–400ms |
| Page transition | 400–700ms |
| Cinematic hero reveal | 800–1200ms |
| Pinned scroll scene | drives from scroll, 1500–4000px |

If your animation feels snappy but forgettable, it's too fast. Slow it down 30%; users perceive slower motion as more premium.

## CSS — when it's enough

### Transitions
```css
.button {
  transition: 
    transform 200ms var(--ease-out-expo),
    background-color 200ms var(--ease-out-expo),
    box-shadow 300ms var(--ease-out-expo);
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-lg);
}

.button:active {
  transform: translateY(0) scale(0.98);
  transition-duration: 75ms;  /* press feels instant */
}
```

### Staggered reveal via `animation-delay`
```css
@keyframes rise {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.reveal > * {
  opacity: 0;
  animation: rise 800ms var(--ease-out-expo) forwards;
}
.reveal > :nth-child(1) { animation-delay: 100ms; }
.reveal > :nth-child(2) { animation-delay: 200ms; }
.reveal > :nth-child(3) { animation-delay: 300ms; }
```

### Scroll-linked with CSS (modern)
```css
@supports (animation-timeline: scroll()) {
  .parallax {
    animation: rise linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 40%;
  }
}
```

Check browser support. Fall back to JS for older browsers.

## Motion (fka Framer Motion) — React

Best for: state-driven animation, gestures, layout animations, shared element transitions.

```jsx
import { motion, AnimatePresence } from "motion/react";

<motion.div
  initial={{ opacity: 0, y: 24 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -12 }}
  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
  whileHover={{ y: -2 }}
  whileTap={{ scale: 0.98 }}
/>
```

### `layout` prop — free layout animations
```jsx
<motion.div layout>{children}</motion.div>
```
Animates position/size changes for free when the element's layout changes (filter, sort, accordion expand).

### `AnimatePresence` for exit animations
Use for conditional rendering:
```jsx
<AnimatePresence mode="wait">
  {open && <motion.div key="modal" initial={...} exit={...} />}
</AnimatePresence>
```

### Gestures
- `whileHover`, `whileTap`, `whileFocus`, `whileInView`
- `drag`, `dragConstraints`, `dragElastic`, `dragTransition`

### When NOT to use Motion
- Long orchestrated sequences → use GSAP, Motion's API gets unwieldy.
- Scroll-scrubbed pinned scenes → use ScrollTrigger.
- Outside React → GSAP or CSS.

## GSAP — when motion is the product

Use when you need orchestration, scroll scrubbing, text splitting, or path morphing. **Load the full `gsap` skill for the complete API.**

Quick starter:
```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// Hero reveal
gsap.timeline({ defaults: { ease: "power3.out" } })
  .from(".hero-title", { y: 80, opacity: 0, duration: 1 })
  .from(".hero-sub",   { y: 40, opacity: 0, duration: 0.8 }, "-=0.5")
  .from(".hero-cta",   { scale: 0.9, opacity: 0, duration: 0.6 }, "-=0.3");

// Scroll reveal
gsap.utils.toArray(".fade-in").forEach(el => {
  gsap.from(el, {
    y: 40, opacity: 0, duration: 0.8,
    scrollTrigger: { trigger: el, start: "top 85%", once: true }
  });
});

// Pinned scrub
gsap.timeline({
  scrollTrigger: { trigger: ".hero", start: "top top", end: "+=1500", pin: true, scrub: 1 }
})
.to(".hero-title", { scale: 2, opacity: 0 })
.to(".hero-bg",    { yPercent: -30 }, 0);
```

In React, use `useGSAP` from `@gsap/react` for auto-cleanup. See the `gsap` skill → `references/frameworks.md`.

## Choreography — the composer's job

### Hero sequence rules
- **Start with structure**, then style, then detail. Eyebrow → headline → sub → CTA → product visual. Rarely reveal the product first.
- **Stagger ~80–150ms per element.** More feels drunk; less feels simultaneous.
- **Total duration ~1.2–1.8s.** Longer and users tap before it finishes.
- **First element should be visible at t=0** (no awkward empty frame).

### Scroll reveal rules
- **Single direction per section.** Mixing up/down/left/right feels chaotic.
- **Threshold at 85%, not 100%.** `start: "top 85%"` → element animates just before fully entering.
- **`once: true` unless it's genuinely a back-and-forth.** Re-animating on scroll-up is rarely desired.
- **For lists ≥ 20 items, use `ScrollTrigger.batch()`** — one trigger per item is expensive.

### Pinned scene rules
- **One big idea per pin.** 2–3 tweens max.
- **Linear ease** for anything scrubbed. Otherwise motion doesn't match scroll.
- **Pin duration in pixels, not time.** `end: "+=1500"` = 1500px of scroll.
- **Test with slow scroll.** Fast scrollers and slow scrollers must both feel right.

## Performance — non-negotiable

- **Animate only `transform` and `opacity` in hot paths.** Width, height, top, left trigger layout.
- **`will-change: transform`** only on actively animating elements. Remove after.
- **`filter: blur()` on large elements is expensive** — layer a pre-blurred element and fade it.
- **`backdrop-blur` only on fixed/sticky elements.** On scrolling containers it causes continuous repaints.
- **Test on a mid-range Android.** Chrome DevTools CPU throttle 4× is a good proxy.
- **Prefer one timeline over many independent tweens** — GSAP batches internally.
- **Lazy-register ScrollTriggers.** On long pages don't create 200 triggers at mount.

## Accessibility — motion safety

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

In JS:
```js
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (!reduceMotion) {
  gsap.from(".hero", { y: 80, opacity: 0, duration: 1 });
}
```

For users who opt in to motion: still provide pauseable autoplay, avoid flashing > 3Hz (seizure risk), and keep parallax subtle.

## Common motion mistakes

- Fade-in from opacity 0 without a transform — feels ghostly, not intentional. Always combine with a small transform.
- Animating on every scroll position update — use `scrub: 1` (smoothed) or threshold triggers.
- Hover animations without corresponding unhover — causes "stuck" states.
- Page transitions longer than 400ms — users feel trapped.
- Every element has motion — the distinctive moments lose meaning. Pick 2–3 hero moments per page.

## The test

Turn off the monitor, listen to someone describe the page. If the words "it feels alive" or "Apple-like" come up naturally, motion is doing its job. If they say "cool animations", it's too much.
