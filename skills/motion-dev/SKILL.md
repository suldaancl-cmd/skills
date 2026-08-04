---
name: motion-dev
description: Use when building React/Vue/JS animations with a declarative API — variants, gesture handling, layout animations, AnimatePresence (enter/exit), scroll-linked motion, drag/pan, spring physics, or shared-element transitions. Triggers — "Framer Motion", "framer-motion", "motion library", "AnimatePresence", "layoutId", "useScroll", "useTransform", "drag and drop animation", "spring animation in React", "exit animation", "page transition".
---

# Motion — declarative animation for React/JS

Motion (formerly **Framer Motion**) is the leading declarative animation library for React. It's an alternative philosophy to GSAP — GSAP is imperative (you call `gsap.to()`), Motion is declarative (you write `<motion.div animate={{ x: 100 }} />` and React decides when to fire it). Both are excellent; pick by paradigm.

**Key fact (keep current):** The library was renamed in 2024 from `framer-motion` to **`motion`** by the original author Matt Perry. Old projects still import from `framer-motion`. New projects should use `motion`. The React API is now under `motion/react`. There's also a vanilla JS slice `motion` for non-React.

```bash
# Old (still works, identical API)
npm install framer-motion

# New canonical
npm install motion
```

```jsx
// New canonical React import
import { motion, AnimatePresence } from 'motion/react';

// Vanilla (no React)
import { animate } from 'motion';
```

## When to reach for Motion

Pick Motion over GSAP when:
- The project is **React** (or Vue/Svelte via wrappers) and you want animations co-located with components
- You need **layout animations** — `layoutId` for shared-element transitions, `layout` prop for FLIP without writing FLIP logic
- You need **enter/exit animations** — `AnimatePresence` handles unmount-then-animate properly (React's killer pain)
- You need **gestures** — drag, pan, hover, tap, focus all built-in with constraints and inertia
- The animations are **simple-to-medium complexity** — Motion shines at 80% of UI motion needs

Pick **GSAP** instead when:
- You need precise sub-frame timeline orchestration with many overlapping tweens
- Scroll-scrubbed cinematic heroes (ScrollTrigger > useScroll for complex cases)
- SVG path morphing, drawSVG, MotionPath
- Non-React project where the imperative API is cleaner

For Karim's stack: GSAP for cinematic landing pages (`hyliox-landing`, `epic-design`), Motion for app/dashboard component motion + page transitions.

## Core pattern — the `motion` component

Every HTML/SVG element has a `motion.*` counterpart that accepts animation props:

```jsx
import { motion } from 'motion/react';

<motion.div
  initial={{ opacity: 0, y: 50 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -20 }}
  transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
>
  Hello
</motion.div>
```

Three props do all the work:
- `initial` — start state (or `false` to skip enter)
- `animate` — target state (and re-runs whenever it changes)
- `exit` — required for unmount animation (needs `<AnimatePresence>` wrapper)

## Variants — orchestration

```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.2 }
  }
};
const item = {
  hidden: { y: 20, opacity: 0 },
  show: { y: 0, opacity: 1 }
};

<motion.ul variants={container} initial="hidden" animate="show">
  {items.map(i => <motion.li key={i} variants={item}>{i}</motion.li>)}
</motion.ul>
```

Variants cascade to children automatically — set state once on the parent, all descendants animate. This is Motion's answer to GSAP timelines and it's elegant.

## AnimatePresence — exit animations

React's biggest animation pain: unmounted components disappear instantly. AnimatePresence keeps them mounted long enough to play the `exit` animation.

```jsx
import { AnimatePresence, motion } from 'motion/react';

<AnimatePresence mode="wait">
  {isOpen && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
    />
  )}
</AnimatePresence>
```

`mode`: `"wait"` (default for page transitions — exit fully before enter), `"sync"` (overlap), `"popLayout"` (let layout collapse during exit).

## Layout animations — FLIP for free

The `layout` prop animates ANY layout change automatically — grid reorder, expanded card, removed item.

```jsx
<motion.div layout>...</motion.div>

// Shared element across components
<motion.div layoutId="hero-image" />
// ... navigate to detail page ...
<motion.img layoutId="hero-image" />  // SAME ID = animated transition
```

`layoutId` is the magic — match IDs across mount/unmount and Motion morphs one into the other. This is how Apple-style "tap card → expand to fullscreen" works.

## Gestures — drag, hover, tap, pan

```jsx
<motion.div
  drag                                 // enable drag
  dragConstraints={{ left: 0, right: 200 }}
  dragElastic={0.2}
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  onDragEnd={(e, { offset, velocity }) => { ... }}
/>
```

`whileHover` / `whileTap` / `whileFocus` / `whileInView` are inline state overrides that revert when the gesture ends. Zero state-management code.

## Scroll-linked motion

```jsx
import { motion, useScroll, useTransform } from 'motion/react';

function Hero() {
  const { scrollYProgress } = useScroll();         // 0 → 1 over page
  const y = useTransform(scrollYProgress, [0, 1], [0, -300]);
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0]);
  return <motion.div style={{ y, opacity }} />;
}
```

For pinned sections, use `useScroll({ target: ref, offset: ['start end', 'end start'] })`. For heavy scrubbed timelines, prefer GSAP ScrollTrigger — Motion's `useScroll` excels at parallax and reveal, not at orchestrated multi-element scrubbing.

## Spring physics

```jsx
<motion.div animate={{ x: 100 }} transition={{ type: 'spring', stiffness: 200, damping: 20 }} />
```

Spring is the default for `layoutId` and `drag` snap-back. Specify `stiffness` (300 = snappy, 100 = lazy), `damping` (10 = bouncy, 30 = critically damped), `mass` (default 1).

For deterministic timing, use `tween`: `transition={{ type: 'tween', duration: 0.5, ease: [0.22, 1, 0.36, 1] }}`.

## Common cubic-beziers (better than `easeInOut`)

```js
const easeOutExpo = [0.16, 1, 0.3, 1];
const easeOutQuart = [0.25, 1, 0.5, 1];
const easeOutBack = [0.34, 1.56, 0.64, 1];   // slight overshoot
const easeInOutCirc = [0.85, 0, 0.15, 1];    // dramatic mid-curve
```

## Performance

1. **Animate transforms and opacity only** — `x`, `y`, `scale`, `rotate`, `opacity` are GPU-accelerated. `width`, `height`, `top`, `left`, `margin` trigger layout. Use `layout` prop to let Motion FLIP layout changes for free.
2. **`layout` prop is expensive** — measures DOM on every render. Don't slap it on every component. Use it where you need it.
3. **`AnimatePresence` with many children** — provide stable `key` props. Without keys, React reuses DOM and exit animations break.
4. **Reduce-motion** — Motion respects `prefers-reduced-motion` automatically when you wrap your app in `<MotionConfig reducedMotion="user">`.

## Next.js App Router setup

```jsx
'use client';
import { motion } from 'motion/react';
// All motion components must be in client components
```

For page transitions in App Router, wrap the layout's `{children}` in `<AnimatePresence mode="wait">` keyed on `pathname`.

## Quick decision guide

| Need | Reach for |
|---|---|
| Hover/tap micro-interactions | `whileHover` / `whileTap` |
| Modal/drawer enter-exit | `AnimatePresence` + variants |
| Page transitions | `AnimatePresence mode="wait"` on route |
| Shared-element morph | `layoutId` |
| Stagger reveal | container variants + `staggerChildren` |
| Drag-and-drop | `drag` + `dragConstraints` + `onDragEnd` |
| Scroll parallax | `useScroll` + `useTransform` |
| Heavy scroll-scrubbed hero | GSAP ScrollTrigger (not Motion) |
| Sub-frame orchestration | GSAP timeline (not Motion) |
| Animate 1000 elements | GSAP (not Motion — React reconciliation cost) |

## Gotchas

1. **Renamed package** — `motion` is the new name, `framer-motion` still works identically. Pick one per project; don't mix.
2. **`layoutId` across routes** — needs both elements rendered simultaneously briefly, which React Router/Next don't do by default. Use `view-transition` API or keep both mounted during transition.
3. **`AnimatePresence` + key** — every conditional child needs a stable `key`. Without it, exit animations silently break.
4. **SSR + `layout`** — server-rendered layout differs from client. Motion handles it, but expect a one-frame layout shift on hydration.
5. **`useScroll` and `transform`** — putting `transform` directly on a `motion` component breaks Motion's internal `x`/`y`. Use the `x`/`y` props instead.
6. **Drag + scrolling** — vertical drag inside a vertically-scrolling page fights touch. Use `dragDirectionLock` or explicit `drag="x"`.

## Related

`gsap` — imperative counterpart, better for cinematic. `web-designer/references/motion.md` — broader library-choice context. `senior-frontend` — React patterns around component-driven animation.
