---
name: react-native-skia
description: React Native Skia — hardware-accelerated 2D canvas for React Native and Expo. Use for shaders, particles, generative textures, custom blur, gradients, path drawing, and any visual that plain views cannot express. Triggers: "skia", "shader", "particles", "custom canvas", "generative", "blur effect", "draw a path", "glow", "noise texture", "runtime shader" in a React Native or Expo context.
version: 1.0.0
author: Karim
tags: [react-native, expo, animation, graphics, skia, shader, mobile]
---

# React Native Skia

Google's Skia graphics engine exposed to React Native. This is the escape hatch for anything the view system cannot draw: shaders, particle fields, custom blurs, generative art, precise path work.

Authority: vault note `reference_mobile_motion_guide.md`. Companion skills: `reanimated` (drives Skia values), `shader-dev` (GLSL/SkSL authoring), `webgl-effect-recipes` (**web only — do not port its DOM code into RN**).

## Cost check before reaching for it

Skia is **high setup complexity, excellent runtime performance**. It is the right tool for shaders and particles and the wrong tool for a button press. Escalate deliberately:

1. Plain view + `moti` → micro-interactions
2. `reanimated` shared values → gesture and scroll motion
3. `lottie` / `rive` → designer-authored illustration and state machines
4. **Skia** → only when none of the above can draw it

## Setup

```bash
npx expo install @shopify/react-native-skia
```

Requires a development build for some native paths — Expo Go covers most of the API but not all. If a Skia import crashes only in Expo Go, build a dev client (`expo-dev-client`) before assuming the code is wrong. Verify Fabric/New Architecture compatibility on the installed version.

## Core model

Everything renders inside `<Canvas>`. Children are declarative drawing primitives, not views — they have no layout, no touch targets, no accessibility tree of their own.

```tsx
import { Canvas, Circle, Fill } from '@shopify/react-native-skia';

<Canvas style={{ flex: 1 }}>
  <Fill color="#26232C" />
  <Circle cx={128} cy={128} r={64} color="#FF7A21" />
</Canvas>
```

Primitives worth knowing: `Fill`, `Rect`, `RoundedRect`, `Circle`, `Path`, `Group`, `Image`, `Text`, `LinearGradient`, `RadialGradient`, `Blur`, `Shadow`, `BackdropFilter`.

## Animating Skia

Skia reads Reanimated shared values directly — no bridge, no re-render:

```tsx
const r = useSharedValue(20);
r.value = withRepeat(withTiming(80, { duration: 1200 }), -1, true);

<Canvas style={{ flex: 1 }}>
  <Circle cx={128} cy={128} r={r} color="#215CFF" />
</Canvas>
```

Pass the shared value itself, not `r.value`. Passing `.value` reads it once at render and freezes the animation — the most common Skia animation bug.

For per-frame logic use `useClock()` / `useComputedValue` rather than a JS timer.

## Shaders

Skia runs **SkSL**, close to GLSL but not identical:

```tsx
const source = Skia.RuntimeEffect.Make(`
uniform float2 resolution;
uniform float time;
half4 main(float2 xy) {
  float2 uv = xy / resolution;
  return half4(uv.x, uv.y, abs(sin(time)), 1.0);
}`)!;

<Canvas style={{ flex: 1 }}>
  <Fill>
    <Shader source={source} uniforms={{ resolution: [w, h], time: clock }} />
  </Fill>
</Canvas>
```

Do not paste GLSL from Shadertoy unchanged — SkSL uses `half4`/`float2`, requires `main(float2)`, and has no `iTime`/`iResolution` globals. Declare uniforms explicitly.

## Rules

- Canvas children are drawings, not views: no `onPress`. Put a `Pressable` over the canvas, or use Gesture Handler and hit-test yourself.
- Size the canvas explicitly. A `<Canvas>` with no dimensions draws nothing.
- Cap particle counts and test on a real mid-range Android — Skia will happily let you write something that renders at 12fps.
- Keep images decoded once (`useImage`) rather than per frame.
- Provide a static fallback when `useReducedMotion()` is true; a shader that pulses forever is exactly what that setting exists to stop.
- Nothing inside a canvas is readable by a screen reader. Anything conveying meaning needs an accessible label on a wrapping view.

Docs: https://shopify.github.io/react-native-skia/
