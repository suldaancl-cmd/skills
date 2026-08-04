---
name: react-native-motion
description: Immersive motion, animation, and gesture for Expo / React Native apps — the mobile equivalent of the GSAP/Motion web stack. Covers Reanimated (UI-thread animations, layout & shared-element transitions), Moti (declarative Framer-Motion-style API), Gesture Handler, React Native Skia (shaders/canvas), Lottie, Rive, and expo-haptics. Also the bridge that turns Figma Motion / get_motion_context output (which only emits web + SwiftUI code) into real Reanimated/Moti code. Use this whenever adding animation, transitions, micro-interactions, gestures, haptics, parallax, skeleton loaders, or immersive motion to a React Native / Expo app, or implementing Figma motion in a mobile app.
---

# React Native Motion

Immersive motion for Expo/React Native apps. On the web you reach for GSAP/Motion; on mobile the equivalent stack is **Reanimated + Moti + Gesture Handler + Skia**, and this skill is how you use them well — plus the bridge from Figma Motion into that stack, because neither Figma's export nor `figma-implement-motion` speaks React Native.

Motion is what separates a premium app from a flat one. But mobile motion runs on a real device with a 120Hz display and a battery — jank and dropped frames read as "cheap" instantly, so the golden rule is: **animate on the UI thread, never re-render per frame.**

## Pick the right tool

| Need | Reach for | Why |
|---|---|---|
| Any property animation (opacity, transform, color, layout) | **Reanimated** | Runs on the UI thread via worklets — smooth even when JS is busy |
| Declarative, Figma-Motion-style motion (`from`/`animate`/`exit`) | **Moti** | Thin layer over Reanimated; maps almost 1:1 to motion.dev / Figma Motion |
| Drag, pinch, swipe, long-press, fling | **Gesture Handler** | Native-thread gestures that drive Reanimated shared values directly |
| Shaders, custom canvas, blur, generative texture, particles | **React Native Skia** | The on-device answer to Figma's shader engine |
| Designer-authored vector animation (After Effects JSON) | **Lottie** (`lottie-react-native`) | Ship complex illustrated motion as data |
| Interactive, state-machine animation | **Rive** (`rive-react-native`) | Stateful characters/toggles that react to input |
| Physical feedback on interaction | **expo-haptics** | A light tap on press/success/error makes motion feel tactile |

Reanimated and Gesture Handler ship in the Expo SDK; Moti/Skia/Lottie/Rive install with `npx expo install`. See `references/stack-setup.md` for versions and the `babel.config.js` / `react-native-reanimated/plugin` gotcha (it must be **last** in the plugin list or worklets silently fail).

## Reanimated core (the 80%)

The mental model: a **shared value** lives on the UI thread; an **animated style** reads it; you drive it with a **timing/spring** function.

```tsx
const y = useSharedValue(0);
const style = useAnimatedStyle(() => ({ transform: [{ translateY: y.value }] }));
// trigger:
y.value = withSpring(-24, { damping: 14, stiffness: 180 });
```

- **Timing vs spring:** `withTiming(to, { duration, easing })` for precise, designer-specified motion; `withSpring(to, { damping, stiffness, mass })` for natural, interruptible motion. Prefer springs for anything the user can interrupt (drags, toggles).
- **Compose** with `withSequence`, `withDelay`, `withRepeat`. Stagger a list by mapping index → `withDelay(i * 40, …)`.
- **Layout animations** (`Entering`/`Exiting`/`Layout` props, e.g. `entering={FadeInDown.springify()}`) animate mount/unmount/reflow with zero shared-value wiring — use them for list items and screen sections.
- **Shared-element transitions** across screens: Reanimated `sharedTransitionTag` on the two elements, or `react-navigation` native-stack shared elements. This is the single most "premium" mobile move — a tapped card that morphs into its detail screen.
- **Easing:** `Easing.bezier(x1,y1,x2,y2)` matches any CSS cubic-bezier exactly — this is the hook for the Figma bridge below.

Load `references/reanimated-patterns.md` for scroll-driven headers/parallax, interpolate/`interpolateColor`, and the worklet rules (`'worklet'`, `runOnJS`, `runOnUI`).

## Moti (when you want it declarative)

Moti gives motion.dev's API on mobile — the fastest path from a Figma Motion spec to working code:

```tsx
<MotiView
  from={{ opacity: 0, translateY: 16 }}
  animate={{ opacity: 1, translateY: 0 }}
  transition={{ type: 'timing', duration: 320, easing: Easing.out(Easing.cubic) }}
/>
// AnimatePresence + exit={{...}} for mount/unmount, like Framer Motion.
```

Use Moti for declarative component motion and presence; drop to raw Reanimated for gesture-driven or scroll-linked motion where you need the shared value directly.

## The Figma → React Native bridge

`get_motion_context` returns **CSS `@keyframes` + motion.dev snippets** — web only. `figma-implement-motion` translates those to React-web and SwiftUI, **not** React Native. Here's the translation this skill owns:

1. **Get the data** exactly as `figma-implement-motion` describes: `get_design_context` for structure, `get_motion_context` for keyframes/easing/timing/cohorts. Match nodes by `data-node-id`. (Reuse that skill's node-merging rules — don't re-derive them.)
2. **motion.dev snippet → Moti.** `initial/animate/transition` map directly to Moti's `from`/`animate`/`transition`. Keep the exact durations, easing arrays, and offsets — fidelity is graded.
3. **CSS `@keyframes` → Reanimated.** Each keyframe stop becomes a `withTiming` in a `withSequence`, or use Reanimated's `Keyframe` API for multi-stop tracks. Convert `cubic-bezier(a,b,c,d)` → `Easing.bezier(a,b,c,d)`; convert a spring → `withSpring` config.
4. **`timelineCohorts` → shared timing.** Nodes sharing a cohort share one driver: one shared value or one staggered map, not independently-timed components — otherwise a coordinated animation drifts out of sync.
5. **Transforms:** RN has no `transform-origin`. For scale/rotate that pivots off-center, offset with translate before/after the transform (compose the transform array), or anchor with layout. Note this when a snippet relies on a non-center origin.
6. **`prefers-reduced-motion`:** use Reanimated's `useReducedMotion()` (or `AccessibilityInfo.isReduceMotionEnabled`) and render the resting state / near-zero duration when true. This is a default, not an opt-in — same rule as the web bridge.

`references/figma-bridge.md` has a worked example (a Figma stagger-in list → Moti) and the full easing/spring mapping table.

## Immersive patterns worth having

The moves that make an app feel crafted rather than templated — each maps to a stack tool above:

- **Gesture-driven sheets & cards** (drag-to-dismiss, snap points) — Gesture Handler + `withSpring`.
- **Scroll-linked headers, parallax, sticky-collapse** — `useAnimatedScrollHandler` + `interpolate`.
- **Shared-element hero transitions** between list and detail — the premium signature move.
- **Skeleton / shimmer loaders** — a Skia gradient sweep or a Moti `Skeleton`, never a blank spinner.
- **Haptics on meaningful moments** — `expo-haptics` on success, selection, and threshold-cross. Subtle; overuse is worse than none.
- **Skia for the "wow"** — animated mesh gradients, blur-on-scroll, generative brand texture: the on-device cousin of Figma's shader fills (`figma-shader-recipes`).

## Guardrails

- **60/120fps or it's broken.** Keep per-frame work in worklets on the UI thread; never `setState` per frame. Test on a real mid-range Android device, not just the iOS simulator — Android is where jank shows.
- **Honor reduced motion** everywhere (above).
- **Match the app's existing motion stack.** If the repo already uses Moti, don't introduce raw Reanimated boilerplate beside it (and vice-versa) — consistency reads as quality.
- **Prove it.** Motion can't be verified by reading code. Show a screen recording or sampled frames from the simulator/device before calling it done — "it should animate" is not evidence.
