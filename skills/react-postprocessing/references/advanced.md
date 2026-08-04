# Advanced react-postprocessing

Deeper material split out of SKILL.md. All component/util names below are from `@react-three/postprocessing` `src/`; effect internals are from the `postprocessing` library.

## Custom Effect with animated uniforms and a blend mode

`wrapEffect(effectClass, defaults?)` turns a `postprocessing` `Effect` subclass into an R3F component. Props passed to the component are forwarded to the effect's constructor; `blendFunction` and `opacity` are understood by the base `Effect`.

```jsx
import { forwardRef, useMemo } from 'react'
import { useFrame } from '@react-three/fiber'
import { Effect, BlendFunction } from 'postprocessing'
import { Uniform } from 'three'

const fragment = /* glsl */ `
  uniform float uTime;
  uniform float uAmount;
  void mainImage(const in vec4 inputColor, const in vec2 uv, out vec4 outputColor) {
    // scrolling scanline wobble driven by uTime
    float wobble = sin(uv.y * 200.0 + uTime * 4.0) * uAmount;
    vec2 shifted = vec2(uv.x + wobble, uv.y);
    // note: sampling the input buffer is via the auto-provided inputBuffer in real effects;
    // for a pure color op, operate on inputColor directly:
    outputColor = vec4(inputColor.rgb + wobble, inputColor.a);
  }
`

class WobbleImpl extends Effect {
  constructor({ amount = 0.01, blendFunction = BlendFunction.NORMAL } = {}) {
    super('WobbleEffect', fragment, {
      blendFunction,
      uniforms: new Map([
        ['uTime', new Uniform(0)],
        ['uAmount', new Uniform(amount)],
      ]),
    })
  }
  update(_renderer, _inputBuffer, deltaTime) {
    this.uniforms.get('uTime').value += deltaTime
  }
}
```

The base `Effect.update(renderer, inputBuffer, deltaTime)` hook is called every frame by the composer — use it for time, not a React `useFrame`, so the value tracks the render loop exactly.

Bridging to React with a ref so you can tweak uniforms from outside:

```jsx
import { wrapEffect } from '@react-three/postprocessing'
export const Wobble = wrapEffect(WobbleImpl)

// <EffectComposer><Wobble amount={0.02} blendFunction={BlendFunction.SCREEN} /></EffectComposer>
```

If you need `Vector2`/`Vector3` props (e.g. an offset) coerced from array literals like `offset={[0.001, 0.002]}`, the library's `useVector2(props, key)` helper (exported from the package util) does that conversion inside a hand-rolled wrapper component.

## Blend functions

Every effect accepts a `blendFunction` (from `postprocessing`'s `BlendFunction`) controlling how its output combines with the buffer beneath it. Common values: `NORMAL`, `ADD` (Bloom's default — additive light), `SCREEN`, `MULTIPLY`, `OVERLAY`, `SOFT_LIGHT`, `DARKEN`, `LIGHTEN`, `AVERAGE`. Switching a color effect to `SCREEN` vs `ADD` vs `OVERLAY` is a fast way to retune a look without touching the shader.

## EffectComposer props (verified from src/EffectComposer.tsx)

| Prop | Type | Note |
|---|---|---|
| `enabled` | `boolean` | Toggle the whole pipeline. |
| `depthBuffer` | `boolean` | Allocate a depth buffer (needed by depth-aware effects like DoF). |
| `enableNormalPass` | `boolean` | Render a normal pass (some effects need it). |
| `stencilBuffer` | `boolean` | Allocate a stencil buffer. |
| `autoClear` | `boolean` | Composer auto-clear behavior. |
| `resolutionScale` | `number` | Render the whole pipeline at a fraction of screen size. |
| `multisampling` | `number` | MSAA sample count. Default `8`. Set `0` to disable (e.g. when using `SMAA`). |
| `frameBufferType` | `TextureDataType` | Default `HalfFloatType` — keep for HDR/bloom fidelity. |
| `renderPriority` | `number` | R3F render loop priority. |
| `camera` / `scene` | `Camera` / `Scene` | Override the composed camera/scene. |

`EffectComposerContext` is exported (`composer`, `normalPass`, `downSamplingPass`, `camera`, `scene`, `resolutionScale`) — consume it when a custom effect needs the live composer or passes.

## Exported effects (verified from src/index)

`Bloom`, `DepthOfField`, `Autofocus`, `LensFlare`, `ChromaticAberration`, `Vignette`, `Noise`, `Glitch`, `Scanline` (`ScanlineEffect`), `Pixelation`, `DotScreen`, `Grid`, `GodRays`, `Outline`, `SelectiveBloom`, `SMAA`, `FXAA`, `SSAO`, `N8AO`, `ToneMapping`, `HueSaturation`, `BrightnessContrast`, `ColorAverage`, `ColorDepth`, `Sepia`, `Ramp`, `Texture`, `LUT`, `TiltShift`, `TiltShift2`, `ASCII`, `Water`, `Depth`, `ShockWave`. Plus `Selection` / `Select` (context) and utils `wrapEffect`, `useVector2`.

Effects created with `wrapEffect` (like `Bloom`, `ToneMapping`) forward their props straight to the underlying `postprocessing` effect constructor, so the authoritative prop list for each is that effect's class in the `postprocessing` repo (`Bloom` -> `BloomEffect`: `intensity`, `luminanceThreshold`, `luminanceSmoothing`, `mipmapBlur`, `radius`, `levels`; `ToneMapping` -> `ToneMappingEffect`: `mode` via `ToneMappingMode`, plus adaptive-luminance params).

## N8AO props (verified from src/effects/N8AO.tsx)

`aoRadius` (default 5), `distanceFalloff` (1), `intensity` (1), `color`, `quality` (`'performance' | 'low' | 'medium' | 'high' | 'ultra'`), `aoSamples` (16), `denoiseSamples` (4), `denoiseRadius` (12), `halfRes`. It is a full render pass (not a merged effect), applied via `applyProps(effect.configuration, ...)`.

## When to reach outside this binding

If you need many chained custom passes, ping-pong buffers, or a pass that must run at a different cadence, you're past what the declarative composer is for — drop to the `postprocessing` library's imperative `EffectComposer`/`RenderPass` directly inside a `useFrame`, or a raw Three `WebGLRenderTarget` setup. The React binding optimizes for the common declarative stack, not arbitrary multi-pass graphs.
