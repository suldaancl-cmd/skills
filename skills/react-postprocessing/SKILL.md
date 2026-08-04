---
name: react-postprocessing
description: Cinematic screen-space post-processing for React Three Fiber via @react-three/postprocessing (the postprocessing library's EffectComposer). Fire this whenever building or polishing an R3F / Three.js / WebGL scene that needs the "glow" — Bloom, DepthOfField, ChromaticAberration, Vignette, Noise/Grain, ToneMapping/ACESFilmic, SMAA, N8AO/SSAO, selective bloom, Glitch/Scanline/Pixelation, or a custom GLSL Effect. Triggers on "postprocessing", "post processing", "EffectComposer", "bloom", "depth of field", "chromatic aberration", "screen-space FX", "make it glow", "cinematic", and immersive / award / Awwwards / scroll-driven / 3D / WebGL site work where the signature Igloo/Lusion/Unseen look is the goal.
---

# React Postprocessing

`@react-three/postprocessing` is the React Three Fiber binding for pmndrs `postprocessing`. It replaces Three's stock `EffectComposer` with a merged-shader pipeline: effects are batched into as few full-screen passes as possible, so a five-effect stack still runs close to a single pass. That merging is why it outperforms hand-wiring `ShaderPass` chains, and it is the standard behind the glow-heavy R3F sites people screenshot.

The mental model: `<EffectComposer>` takes effect components as **children, and child order is pipeline order**. Effects render top-to-bottom, each reading the previous result. Order changes the picture — grain before bloom gets bloomed; grain after bloom stays crisp; tone mapping almost always goes last.

## Quick start

```bash
npm install @react-three/postprocessing postprocessing
# peers you already have in an R3F app: three @react-three/fiber react react-dom
```

```jsx
import { Canvas } from '@react-three/fiber'
import { EffectComposer, Bloom, DepthOfField, Noise, Vignette } from '@react-three/postprocessing'

export default function Scene() {
  return (
    <Canvas>
      {/* your meshes/lights */}
      <EffectComposer>
        <DepthOfField focusDistance={0} focalLength={0.02} bokehScale={2} height={480} />
        <Bloom luminanceThreshold={0} luminanceSmoothing={0.9} height={300} />
        <Noise opacity={0.02} />
        <Vignette eskil={false} offset={0.1} darkness={1.1} />
      </EffectComposer>
    </Canvas>
  )
}
```

`EffectComposer` defaults to `multisampling={8}` (WebGL2 MSAA antialiasing) and `frameBufferType={HalfFloatType}` (16-bit float buffers), which is what keeps bloom from banding in dark scenes. Keep those defaults unless profiling says otherwise.

## The award glow: Bloom done right

Bloom is the single effect that reads as "expensive." The look comes from three knobs, not from cranking intensity:

- `mipmapBlur` — enable it. It blurs across a mip pyramid, giving a soft wide falloff instead of a hard ring. This is the difference between "cinematic" and "2012 lens flare."
- `luminanceThreshold` — the brightness cutoff for what blooms. At `0` everything blooms (dreamy, low-contrast). Raise toward `0.9+` so only genuinely bright pixels (emissive materials, light sources, specular hits) glow. This is the taste dial.
- `intensity` — scales the added light. With `mipmapBlur` on you rarely need more than ~1–2.

```jsx
import { EffectComposer, Bloom } from '@react-three/postprocessing'

<EffectComposer>
  <Bloom
    mipmapBlur
    intensity={1.2}
    luminanceThreshold={0.9}
    luminanceSmoothing={0.3}
    radius={0.8}
  />
</EffectComposer>
```

For a mesh to actually cross that threshold, push its material's emissive past 1.0 (values above 1 are HDR and only visible because the composer uses a float buffer):

```jsx
<mesh>
  <sphereGeometry />
  <meshStandardMaterial emissive="#ff5533" emissiveIntensity={4} toneMapped={false} />
</mesh>
```

`toneMapped={false}` on the emissive material stops tone mapping from clamping the color before it blooms — a common reason "my bloom looks dull."

## Selective bloom: only chosen meshes glow

Threshold-based bloom glows anything bright. When you want *specific* objects to glow regardless of scene brightness, wrap the scene in `<Selection>` and tag meshes with `<Select enabled>`. `Bloom` then blooms only the selection.

```jsx
import { EffectComposer, Bloom, Selection, Select } from '@react-three/postprocessing'

export default function Scene() {
  return (
    <Canvas>
      <Selection>
        <Select enabled>
          <mesh>
            <torusKnotGeometry />
            <meshStandardMaterial emissive="#48f" emissiveIntensity={3} toneMapped={false} />
          </mesh>
        </Select>

        {/* not selected -> never blooms, even if bright */}
        <mesh position={[3, 0, 0]}>
          <boxGeometry />
          <meshStandardMaterial color="white" />
        </mesh>

        <EffectComposer>
          <Bloom mipmapBlur luminanceThreshold={0} intensity={1.5} />
        </EffectComposer>
      </Selection>
    </Canvas>
  )
}
```

`Select`'s `enabled` prop is reactive — drive it from hover/click/scroll state to make objects light up on interaction. Note the `EffectComposer` lives *inside* `<Selection>` so it can read the selection context. There is also a standalone `SelectiveBloom` effect (takes explicit `selection` and `lights` refs) for cases where you manage refs manually; the `Selection`/`Select` approach is the ergonomic default.

## Full cinematic stack

The Igloo/Lusion-tier look is a layered stack in the right order. Tone mapping resolves HDR to display range and belongs last:

```jsx
import { NoToneMapping } from 'three'
import { Canvas } from '@react-three/fiber'
import {
  EffectComposer, Bloom, DepthOfField, ChromaticAberration, Vignette, Noise, SMAA, ToneMapping,
} from '@react-three/postprocessing'
import { ToneMappingMode } from 'postprocessing'

export default function Cinematic() {
  return (
    <Canvas gl={{ toneMapping: NoToneMapping }}>
      {/* scene */}
      <EffectComposer multisampling={0}>
        <DepthOfField focusDistance={0.01} focalLength={0.05} bokehScale={3} />
        <Bloom mipmapBlur intensity={1.1} luminanceThreshold={0.85} />
        <ChromaticAberration offset={[0.0008, 0.0008]} radialModulation modulationOffset={0.4} />
        <Noise opacity={0.035} />
        <Vignette offset={0.3} darkness={0.7} />
        <ToneMapping mode={ToneMappingMode.ACES_FILMIC} />
        <SMAA />
      </EffectComposer>
    </Canvas>
  )
}
```

Two coupled choices here:

- **Tone mapping ownership.** Either let Three tone-map (its default `ACESFilmicToneMapping` on the renderer) *or* add a `ToneMapping` effect and set the renderer to `NoToneMapping`. Doing both double-applies the curve and washes everything out. If you add the effect, turn the renderer off as shown.
- **Antialiasing ownership.** `EffectComposer` MSAA (`multisampling`) and the `SMAA` effect both antialias. Pick one. Using `SMAA` (shader-based, cheaper on some GPUs) means dropping `multisampling` to `0` so you don't pay for both.

## Stylized passes

For non-photoreal / retro / glitchy looks, the same composer takes `Glitch`, `Scanline`, `Pixelation`, `DotScreen`, `HueSaturation`, `Sepia`, `ColorDepth`, `ASCII`. Example — a datamosh title treatment:

```jsx
import { EffectComposer, Glitch, Scanline, Pixelation } from '@react-three/postprocessing'
import { GlitchMode } from 'postprocessing'
import { Vector2 } from 'three'

<EffectComposer>
  <Glitch delay={[1.5, 3.5]} duration={[0.2, 0.4]} strength={[0.2, 0.5]} mode={GlitchMode.SPORADIC} />
  <Scanline density={1.5} opacity={0.15} />
  <Pixelation granularity={6} />
</EffectComposer>
```

## Ambient occlusion (N8AO / SSAO)

Contact shadows in crevices add the grounded, "rendered not gamey" feel. `N8AO` is the higher-quality choice — it is a full render pass, so unlike the merged effects it goes as a direct child and manages its own pass. Common props: `aoRadius`, `distanceFalloff`, `intensity`, `color`, `quality` (`'performance' | 'low' | 'medium' | 'high' | 'ultra'`), `halfRes`.

```jsx
import { EffectComposer, N8AO, Bloom } from '@react-three/postprocessing'

<EffectComposer>
  <N8AO aoRadius={2} distanceFalloff={1} intensity={2} halfRes />
  <Bloom mipmapBlur luminanceThreshold={0.9} />
</EffectComposer>
```

`halfRes` roughly halves AO cost for a large quality win on mid GPUs. The library also exposes a classic `SSAO` effect if you need the merged-pass variant.

## Custom GLSL effect

When no built-in fits, subclass `postprocessing`'s `Effect` with a fragment shader and lift it into React with `wrapEffect`. Minimal tint-by-uniform effect:

```jsx
import { Effect } from 'postprocessing'
import { wrapEffect } from '@react-three/postprocessing'
import { Uniform, Color } from 'three'

const fragment = /* glsl */ `
  uniform vec3 uTint;
  void mainImage(const in vec4 inputColor, const in vec2 uv, out vec4 outputColor) {
    outputColor = vec4(inputColor.rgb * uTint, inputColor.a);
  }
`

class TintEffectImpl extends Effect {
  constructor({ tint = new Color('#88aaff') } = {}) {
    super('TintEffect', fragment, { uniforms: new Map([['uTint', new Uniform(tint)]]) })
  }
}

// wrapEffect(effectClass, defaults?) -> a React component whose props feed the constructor
export const Tint = wrapEffect(TintEffectImpl)

// usage: <EffectComposer><Tint tint={new Color('#ffccaa')} /></EffectComposer>
```

The `mainImage(inputColor, uv, outputColor)` signature is fixed by the postprocessing convention — write to `outputColor`. For blend modes, animated `uTime` uniforms, and depth-aware effects, see [references/advanced.md](references/advanced.md).

## Framework integration (React / Next.js)

R3F unmounts the `EffectComposer` with the `Canvas`, so effects need no manual disposal in normal use — the composer disposes its render targets on unmount. Two integration facts matter:

- **Next.js / SSR.** WebGL has no server DOM. Render the whole 3D scene client-only:

  ```jsx
  import dynamic from 'next/dynamic'
  const Scene = dynamic(() => import('../components/Scene'), { ssr: false })
  ```

- **Conditional composer.** Toggling the entire `<EffectComposer>` on/off (for a low-power path, see below) is safe — it tears down and rebuilds the pipeline cleanly. Prefer swapping the whole composer over conditionally rendering individual effect children, which is also supported but re-links the pipeline on each change.

## Performance

Post-processing is fill-rate bound: cost scales with pixels, not scene complexity. Levers, cheapest wins first:

- **`frameBufferType={HalfFloatType}`** (the default) is what makes HDR bloom clean; keep it. Only drop to `UnsignedByteType` if you have no HDR content and want the memory back.
- **`resolutionScale`** on `EffectComposer` (and per-effect `resolution`/`height` on blur-heavy effects like `Bloom`, `DepthOfField`) renders the effect at a fraction of screen size then upscales. Halving DoF/Bloom resolution is usually invisible and a big saving.
- **Cap DPR**: `<Canvas dpr={[1, 2]}>` — retina at native DPR quadruples post cost for little gain.
- **Pick one antialiaser** (MSAA `multisampling` *or* `SMAA`), never both.
- **`N8AO halfRes`** and lower `quality` tiers before cutting the effect entirely.
- **Disable on weak hardware / mobile.** Gate the composer behind a capability check and render the raw scene otherwise.

## Accessibility

Postprocessing motion (animated glitch, chromatic pulsing, heavy grain, DoF racking) can trigger vestibular discomfort. Respect `prefers-reduced-motion` — drop to a calm or empty pipeline:

```jsx
import { useMemo } from 'react'
import { EffectComposer, Bloom, ChromaticAberration, Glitch } from '@react-three/postprocessing'

function usePrefersReducedMotion() {
  return useMemo(
    () => typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches,
    []
  )
}

function Effects() {
  const reduce = usePrefersReducedMotion()
  if (reduce) {
    return (
      <EffectComposer>
        <Bloom mipmapBlur luminanceThreshold={0.9} intensity={0.6} />
      </EffectComposer>
    )
  }
  return (
    <EffectComposer>
      <Bloom mipmapBlur luminanceThreshold={0.85} intensity={1.2} />
      <ChromaticAberration offset={[0.001, 0.001]} />
      <Glitch delay={[2, 5]} duration={[0.2, 0.4]} />
    </EffectComposer>
  )
}
```

Keep the static, information-bearing frame intact for reduced-motion users; only strip the moving/pulsing effects.

## Pitfalls

- **Transparent canvas + Bloom.** With `<Canvas gl={{ alpha: true }}>` or a CSS-transparent canvas, bloom can smear over or darken transparent regions because it adds light into an unpremultiplied alpha buffer. Render 3D onto an opaque background, or composite the bloom layer separately, when you need page content to show through.
- **Effect order is the picture.** Grain/noise before `Bloom` gets bloomed into mush; after `Bloom` it stays crisp film grain. `ToneMapping` before other effects tone-maps intermediate HDR and clips highlights early — put it last.
- **Double tone mapping.** Renderer tone mapping *and* a `ToneMapping` effect both applied = washed out. Set the renderer to `NoToneMapping` when you use the effect.
- **Blown highlights.** `luminanceThreshold={0}` blooms everything and quickly clips to white. Raise the threshold and lean on emissive HDR materials for controlled glow instead of raw intensity.
- **Bloom looks flat / grey.** Usually the emissive material is being tone-mapped/clamped before it blooms — set `toneMapped={false}` and push `emissiveIntensity` above 1.
- **Everything is soft/aliased at once.** You're paying for MSAA and SMAA together, or rendering at full DPR with a resolution-scaled composer fighting it. Own antialiasing in one place.

## References

Ground truth for exact prop names and any effect not covered above:

- react-postprocessing docs: https://react-postprocessing.docs.pmnd.rs/
- react-postprocessing repo (README + `src/effects/`): https://github.com/pmndrs/react-postprocessing
- postprocessing library (effect internals, `Effect` class, `BlendFunction`, `ToneMappingMode`, `GlitchMode`): https://github.com/pmndrs/postprocessing
- Advanced custom effects, blend modes, animated uniforms, full option tables: [references/advanced.md](references/advanced.md)
