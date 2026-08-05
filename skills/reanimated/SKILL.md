---
name: reanimated
description: React Native Reanimated 3 and 4 — UI-thread animation with worklets, shared values, springs, layout and shared-element transitions, and scroll/gesture-driven motion. Use whenever animating a React Native or Expo screen, or when a build janks, a worklet throws, or the babel plugin is misconfigured. Triggers: "reanimated", "worklet", "shared value", "useAnimatedStyle", "withSpring", "layout animation", "scroll parallax", "animate this screen", "animation janks on Android".
version: 1.0.0
author: Karim
tags: [react-native, expo, animation, motion, reanimated, mobile]
---

# Reanimated 3

The default animation engine for React Native and Expo. Everything runs on the **UI thread** via worklets, so animation keeps running when JavaScript is busy — which is the entire reason it exists.

Authority for the rules below: vault note `reference_mobile_motion_guide.md`. Companion skills: `moti` (declarative wrapper), `react-native-skia` (canvas/shaders), `gesture-patterns`, `react-native-motion`.

## Setup — get this wrong and nothing works

**1. The babel plugin must be LAST — and in v4 it moved.**

Reanimated 4 extracted worklets into a separate `react-native-worklets` package. `react-native-worklets/plugin` is the canonical path; `react-native-reanimated/plugin` still resolves but is only a re-export shim (verified in 4.5.1: `node_modules/react-native-reanimated/plugin/index.js` is four lines re-exporting it).

```javascript
// babel.config.js
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: [
      // ...every other plugin first
      'react-native-worklets/plugin', // MUST BE LAST (v4+; v3 used react-native-reanimated/plugin)
    ],
  };
};
```

**`babel-preset-expo` is not hoisted to the project root on SDK 57.** A fresh `create-expo-app` bundles fine until you add a custom `babel.config.js`, then Metro dies with `Cannot find module 'babel-preset-expo'`. Fix: `npx expo install babel-preset-expo`. (Verified on SDK 57.0.10.)

**2. Metro caches babel output.** After any babel change:

```bash
npx expo start --clear
```

Skipping this is the single most common cause of "I added the plugin and it still says worklets aren't supported."

**3. Gesture Handler needs a root** (required as soon as you add gestures):

```tsx
import { GestureHandlerRootView } from 'react-native-gesture-handler';

export default function App() {
  return <GestureHandlerRootView style={{ flex: 1 }}>{/* app */}</GestureHandlerRootView>;
}
```

Install: `npx expo install react-native-reanimated react-native-gesture-handler`

Version reality (verified 2026-08-04): **SDK 57 installs Reanimated 4.5.1 + react-native-worklets 0.10.3**, not the 3.x that older guides assume. Reanimated 4 requires the New Architecture. Gesture Handler 2.x.

## Core model

A **shared value** lives on the UI thread. A **worklet** is a function marked to run there. `useAnimatedStyle` returns a style object recomputed on the UI thread every frame — no React re-render, no `setState`.

```tsx
import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';

const offset = useSharedValue(0);
const style = useAnimatedStyle(() => ({ transform: [{ translateX: offset.value }] }));

// drive it
offset.value = withSpring(100, { damping: 15, stiffness: 150 });
```

Animate with `withTiming`, `withSpring`, `withDelay`, `withSequence`, `withRepeat`. Compose them — `withRepeat(withSequence(withTiming(1), withTiming(0)), -1)` loops forever.

## The worklet rules

- A worklet cannot call arbitrary JS. To reach back into React, wrap it: `runOnJS(setCount)(next)`.
- To go the other way, `runOnUI(fn)()`.
- Reading `.value` during render is undefined behaviour — read it inside `useAnimatedStyle` / `useDerivedValue`.
- Keep worklets cheap. They run every frame; heavy work there *is* the jank.

## Layout and shared-element transitions

```tsx
import Animated, { FadeIn, FadeOut, LinearTransition } from 'react-native-reanimated';

<Animated.View entering={FadeIn} exiting={FadeOut} layout={LinearTransition} />
```

Prefer these over animating shared values by hand for mount/unmount — less code and the measurement is done for you.

Shared-element transitions use `sharedTransitionTag` and **require a native-stack navigator**. They will silently do nothing on a JS stack.

## Scroll and gesture driven

```tsx
const scrollY = useSharedValue(0);
const onScroll = useAnimatedScrollHandler((e) => { scrollY.value = e.contentOffset.y; });

<Animated.ScrollView onScroll={onScroll} scrollEventThrottle={16} />
```

`interpolate(scrollY.value, [0, 200], [0, -60], Extrapolation.CLAMP)` is the workhorse for parallax headers. Always clamp — unclamped extrapolation flies off-screen.

## Performance rules

1. UI thread only. If you are calling `setState` per frame, you have already lost.
2. Animate `transform` and `opacity` first. Layout properties (`width`, `height`, `top`) force re-layout.
3. Shared values for anything scroll- or gesture-driven — never React state.
4. **Test on a real mid-range Android.** The iOS simulator hides jank; it does not exist there.
5. Honour `useReducedMotion()` and skip or shorten motion when it returns true. This is an accessibility requirement, not a nicety.
6. Clean up scroll handlers and cancel animations on unmount.

## Common failures

| Symptom | Cause |
|---|---|
| "Reanimated 2 failed to create a worklet" | babel plugin missing, not last, or Metro cache stale — add it, then `--clear` |
| `Cannot find module 'babel-preset-expo'` | not hoisted on SDK 57 — `npx expo install babel-preset-expo` |
| Animation stutters only on Android | JS-thread work per frame, or you tested only on the iOS simulator |
| `sharedTransitionTag` does nothing | not on a native-stack navigator |
| Value jumps instead of animating | assigned a raw number instead of `withTiming`/`withSpring` |
| Crash calling a setter in a worklet | needs `runOnJS` |
| Style never updates | reading `.value` outside `useAnimatedStyle`/`useDerivedValue` |

## Do not reach for

`LayoutAnimation` (deprecated, inconsistent) and the legacy `Animated` API (JS thread, janks when JS is busy). GSAP has no DOM to render into here — but it *can* still drive shared values as a tween engine, so it is banned as a renderer, not as a maths library.

Docs: https://docs.swmansion.com/react-native-reanimated/
