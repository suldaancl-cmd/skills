---
name: moti
description: Moti — declarative Framer-Motion-style animation for React Native and Expo, built on Reanimated. Use for micro-interactions, mount/unmount transitions, AnimatePresence, skeleton loaders, and any animation expressible as from/animate props rather than hand-written worklets. Triggers: "moti", "MotiView", "AnimatePresence", "declarative animation", "fade in this component", "button press animation", "skeleton loader".
version: 1.0.0
author: Karim
tags: [react-native, expo, animation, motion, moti, mobile]
---

# Moti

A declarative layer over Reanimated with a Framer-Motion-shaped API. Reach for it when the animation can be described as *states* rather than *maths* — which covers most product UI.

Authority: vault note `reference_mobile_motion_guide.md`. Companion skills: `reanimated` (the engine underneath), `micro-interaction-spec`, `gesture-patterns`.

## When Moti vs raw Reanimated

| Use Moti | Use Reanimated directly |
|---|---|
| Fades, scales, slides on state change | Scroll-linked parallax |
| Mount/unmount via `AnimatePresence` | Gesture-driven drag physics |
| Button press / tap feedback | Anything needing `interpolate` over a continuous input |
| Skeleton loaders, pulsing placeholders | Custom worklet maths |
| Staggered list entrances | Frame-by-frame control |

Moti compiles down to Reanimated, so mixing them is fine — Moti for the simple 80%, worklets for the rest.

## Setup

```bash
npx expo install moti react-native-reanimated
```

Moti's version **must match** your Reanimated major. Reanimated's babel plugin must still be **last** in `babel.config.js`, and Metro still needs `npx expo start --clear` after that change — Moti does not remove those requirements, it inherits them.

## The API

```tsx
import { MotiView } from 'moti';

<MotiView
  from={{ opacity: 0, translateY: 12 }}
  animate={{ opacity: 1, translateY: 0 }}
  exit={{ opacity: 0 }}
  transition={{ type: 'timing', duration: 300 }}
/>
```

`from` is the mount state, `animate` the target, `exit` the unmount state. Change `animate` and it transitions automatically — no imperative call.

**Transitions:** `{ type: 'timing', duration }` or `{ type: 'spring', damping, stiffness }`. Spring is the default and usually the right feel on mobile. Per-key overrides work:

```tsx
transition={{ type: 'spring', opacity: { type: 'timing', duration: 150 } }}
```

**Press feedback — there is no `tap` prop.** Guides circulate a `tap={{ scale: 0.95 }}` example; it does not exist in Moti 0.30 and fails to typecheck (`Property 'tap' does not exist`). Verified 2026-08-04. Drive `animate` from state instead:

```tsx
const [pressed, setPressed] = useState(false);

<MotiView animate={{ scale: pressed ? 0.96 : 1 }} transition={{ type: 'timing', duration: 100 }}>
  <Pressable onPressIn={() => setPressed(true)} onPressOut={() => setPressed(false)}>
    <Text>Press Me</Text>
  </Pressable>
</MotiView>
```

Or use `MotiPressable` from `moti/interactions` when you want the press state managed for you.

**Unmount animations** need `AnimatePresence` — without it `exit` never runs, because the component is gone before it can animate:

```tsx
import { AnimatePresence, MotiView } from 'moti';

<AnimatePresence>
  {visible && <MotiView from={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} />}
</AnimatePresence>
```

**Stagger** a list by delaying per index:

```tsx
{items.map((item, i) => (
  <MotiView key={item.id} from={{ opacity: 0 }} animate={{ opacity: 1 }}
            transition={{ delay: i * 60 }} />
))}
```

**Skeletons** ship built in: `import { Skeleton } from 'moti/skeleton'`.

## Rules

- `MotiText`, `MotiImage`, `MotiScrollView` exist — use them instead of wrapping a plain component in `MotiView` when you need the text/image itself animated.
- Animate `opacity`, `scale`, `translateX/Y`, `rotate`. Animating `width`/`height` triggers layout and costs more; prefer `scale` where the visual allows.
- `exit` without `AnimatePresence` is a silent no-op — the most common Moti bug.
- Honour `useReducedMotion()` from Reanimated and collapse durations to 0 when it returns true.
- Do not drive `animate` from a value that changes every frame; that is a shared-value job.

## Figma bridge

Moti's `from`/`animate`/`transition` shape maps almost directly onto Figma Motion keyframes: start state → `from`, end state → `animate`, easing + duration → `transition`. This makes it the cheapest target when porting a Figma prototype into React Native. See `figma-motion-pipeline` for the routing.

Docs: https://moti.fyi/
