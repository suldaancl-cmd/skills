---
name: expo-3d-ar
description: 3D and AR inside Expo / React Native — three.js and React Three Fiber running on the expo-gl canvas, expo-three, drei helpers, GLB/Draco loading, model viewers, and AR Quick Look with USDZ. Use whenever a mobile app needs a 3D object, product viewer, or AR preview. Triggers: "3d in my app", "3d model viewer", "expo-gl", "expo-three", "react three fiber native", "GLB in react native", "AR", "AR Quick Look", "USDZ", "product in 3D", "rotate a model", "three.js on mobile".
version: 1.0.0
author: Karim
tags: [expo, react-native, 3d, ar, three, webgl, mobile]
---

# 3D & AR in Expo

**three.js and React Three Fiber do run in React Native** — through the `expo-gl` canvas, not a DOM one. This is worth stating plainly because "no DOM in RN" gets over-generalised into "no 3D", which is wrong and blocks legitimate work.

Verified from the npm registry (2026-08-06): `@react-three/fiber@9.7.0` declares peer dependencies on **`expo >=43`, `expo-gl >=11`, `expo-asset >=8.4`, `expo-file-system >=11`, `react-native >=0.78`**. `expo-gl@57.0.2` and `expo-three@8.0.0` are current.

Related: `react-native-skia` (2D canvas/shaders — cheaper, use it first if 2D suffices), `img2threejs` (build the model from an image), `three` / `react-three-fiber` (**web** guidance — read for API, ignore all DOM plumbing).

## What changes vs the web

| Web | Expo / RN |
|---|---|
| `<canvas>` element | `GLView` from `expo-gl` |
| `import { Canvas } from '@react-three/fiber'` | `from '@react-three/fiber/native'` |
| `window` / `document` / resize listeners | **do not exist** — use `useWindowDimensions()` |
| `fetch` a `.glb` by URL | `expo-asset` `Asset.fromModule()` then load the local URI |
| DOM events / raycasting on pointer | gesture-handler → shared values → camera |
| drei `Html`, `useCursor`, DOM-bound helpers | unavailable; geometry/material helpers are fine |

The API surface of three.js itself is identical. Everything that breaks is plumbing, not rendering.

## Install

```bash
npx expo install expo-gl expo-three expo-asset expo-file-system
npm i three @react-three/fiber @react-three/drei
```

`expo-gl` must come through `npx expo install` (native module, SDK-pinned). `three`, R3F and drei are plain npm.

## Minimal R3F scene

```tsx
import { Canvas } from '@react-three/fiber/native';   // NOTE: /native
import { useGLTF } from '@react-three/drei/native';    // NOTE: /native

function Model() {
  const { scene } = useGLTF(require('./assets/product.glb'));
  return <primitive object={scene} scale={1.4} />;
}

export function Viewer() {
  return (
    <Canvas camera={{ position: [0, 0, 4], fov: 45 }}>
      <ambientLight intensity={0.6} />
      <directionalLight position={[3, 4, 2]} intensity={1.2} />
      <Model />
    </Canvas>
  );
}
```

**Both `/native` entry points are mandatory.** Importing from the bare package pulls the DOM build and fails at runtime with a `document is not defined`-class error, often only on device.

## Raw expo-gl (no R3F)

When you want three.js directly:

```tsx
import { GLView } from 'expo-gl';
import { Renderer } from 'expo-three';

<GLView style={{ flex: 1 }} onContextCreate={async (gl) => {
  const renderer = new Renderer({ gl });
  renderer.setSize(gl.drawingBufferWidth, gl.drawingBufferHeight);
  // ...scene, camera, mesh...
  const loop = () => {
    requestAnimationFrame(loop);
    renderer.render(scene, camera);
    gl.endFrameEXP();          // REQUIRED every frame or nothing paints
  };
  loop();
}} />
```

`gl.endFrameEXP()` is the one line everyone forgets. Without it the scene renders to a buffer that is never presented — black screen, no error.

## Gesture-driven camera

No pointer events. Drive from gesture-handler into shared values:

```tsx
const rotY = useSharedValue(0);
const pan = Gesture.Pan().onChange((e) => { rotY.value += e.changeX * 0.01; });

// inside the scene
useFrame(() => { meshRef.current.rotation.y = rotY.value; });
```

Reading a shared value inside `useFrame` is fine — R3F's loop already runs per frame.

## Getting a model in — img2threejs and Spline

**`img2threejs` output runs in RN unchanged.** It emits `TypeScript + plain Three.js` — a `Group` factory (`src/createObjectModel.ts`) with no DOM, no loader, no asset file. That makes it the *best* model source for mobile, better than it is for web:

```tsx
import { createObjectModel } from './createObjectModel';   // generated, plain three.js
function Product() {
  const group = useMemo(() => createObjectModel(), []);
  return <primitive object={group} />;
}
```

Zero download weight, zero Draco step, diffable in git. Prefer it over a GLB whenever the object is hard-surface enough for the pipeline to reach fidelity. Its "can't reach fidelity from this image" stop is a valid outcome — fall back to a GLB then.

**Spline — export GLB, don't embed the player.**

| Package | Version | RN? |
|---|---|---|
| `@splinetool/react-spline` | 4.1.0 | **No** — peers include `react-dom` |
| `@splinetool/runtime` | 1.12.98 | **No** — web canvas runtime |
| `@splinetool/r3f-spline` | 1.0.2 | **Maybe** — peers are `@react-three/fiber` + `@splinetool/loader`, no `react-dom`. Untested here; verify on device before committing to it |

The reliable route is **export the scene as GLB from Spline** and load it with `useGLTF` like any other model. You lose Spline's interactivity/state machine, which is the point of Spline for web — so if the interactivity is the reason you chose Spline, reconsider whether Rive (a real RN runtime) fits better.

## Assets and budget

- **Draco-compress every GLB.** `npx gltf-transform optimize in.glb out.glb --compress draco`. A 12 MB model is a 12 MB app download and a several-second stall on mid-range Android.
- Bundle models with `require()` via `expo-asset`, not a remote fetch, unless they're genuinely optional content.
- Budget: **under 100k triangles**, textures **≤2048px**, one skinned mesh at most. Mobile GPUs are not desktop GPUs.
- Kill the render loop when the screen blurs — a spinning model in a background screen drains battery and users notice heat before they notice the 3D.

## AR — use the platform, don't build it

For "see it in your room", do **not** write an AR renderer. Both platforms ship a system viewer:

- **iOS — AR Quick Look:** host a `.usdz` and open it. The OS handles placement, lighting, scale.
- **Android — Scene Viewer:** host a `.glb` and open an `intent://arvr.google.com/scene-viewer/1.0?file=<glb-url>` link.

```tsx
import * as Linking from 'expo-linking';
Platform.OS === 'ios'
  ? Linking.openURL('https://cdn.example.com/chair.usdz')
  : Linking.openURL('intent://arvr.google.com/scene-viewer/1.0?file=https://cdn.example.com/chair.glb#Intent;scheme=https;package=com.google.ar.core;end;');
```

You need **both** formats — USDZ for iOS, GLB for Android. Convert with `usdzconvert` or Reality Converter.

Full ARKit/ARCore (plane detection, persistent anchors) needs a dev client and a native module; treat it as a separate project, not a feature.

## Guardrails

- Always test on device. `expo-gl` does not work the same in Expo Go for every path — build a dev client when a GL feature misbehaves.
- Provide a **static image fallback**. Low-end devices and `useReducedMotion()` users should get a rendered still, not a stalled canvas.
- 3D has no accessibility tree. Anything meaningful needs a labelled wrapper and a non-3D path to the same information.
- Prefer `react-native-skia` when the effect is genuinely 2D — it is dramatically cheaper than standing up a GL context.

## Failure table

| Symptom | Cause |
|---|---|
| `document is not defined` / crash on device | imported from `@react-three/fiber` instead of `/native` |
| Black canvas, no error | missing `gl.endFrameEXP()` in the raw expo-gl loop |
| Model invisible but no error | no light in the scene, or camera inside the mesh |
| Multi-second stall on open | uncompressed GLB — Draco it |
| Works in Expo Go, breaks in a build | native GL path needs a dev client |
| Battery drain / device heat | render loop never paused on blur |
| drei helper crashes | DOM-bound helper (`Html`, `useCursor`) — unavailable in RN |
