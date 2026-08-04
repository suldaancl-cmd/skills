---
name: react-three-drei
description: >-
  The React Three Fiber helper toolkit (@react-three/drei). Fire this whenever
  you build or debug an R3F / react-three-fiber 3D scene and reach for drei
  helpers — OrbitControls, ScrollControls + useScroll, PresentationControls,
  CameraControls, Environment / Stage / ContactShadows / AccumulativeShadows /
  SoftShadows / Sky, useGLTF / useTexture / Clone / useAnimations,
  MeshTransmissionMaterial (glass) / MeshReflectorMaterial (floor) /
  MeshDistortMaterial / shaderMaterial, Text / Text3D / Html / Billboard,
  Instances / Merged / Detailed / PerformanceMonitor / AdaptiveDpr / Preload,
  Bounds / useBounds. Use it for scroll-driven 3D, immersive / award-tier /
  Awwwards WebGL sites, product configurators, hero canvases, and any
  "make the R3F scene shippable" task. Synonyms: drei, pmndrs helpers, R3F
  abstractions.
---

# React Three Drei

drei is the batteries-included helper library for React Three Fiber (R3F). R3F is
a React renderer for Three.js; drei is the hundred small abstractions that turn a
bare scene into a shippable one — controls, HDRI lighting, GLTF loading with
Suspense, glass and mirror materials, HTML overlays pinned to 3D space, instancing
for performance. Reach for a drei helper before hand-rolling the Three.js
equivalent; it already handles disposal, ref forwarding, and the render loop.

This skill assumes you already have an R3F `<Canvas>`. To wire up R3F itself
(Canvas, useFrame, useThree, the render loop), use the `react-three-fiber` skill
first, then come back here for the helpers.

## Quick start

drei is a peer of R3F and Three — install all three together, and pin drei to a
version built against your R3F/Three majors (see Pitfalls).

```bash
npm install three @react-three/fiber @react-three/drei
```

A minimal scene that shows the three helpers you will use most — orbit controls,
image-based lighting, and a Suspense-wrapped model loader:

```jsx
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Environment, useGLTF } from '@react-three/drei'
import { Suspense } from 'react'

function Model() {
  const { scene } = useGLTF('/model.glb')
  return <primitive object={scene} />
}

export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 45 }}>
      <Suspense fallback={null}>
        <Model />
        <Environment preset="studio" />
      </Suspense>
      <OrbitControls makeDefault />
    </Canvas>
  )
}

useGLTF.preload('/model.glb') // warm the cache before the component mounts
```

`Suspense` is not optional here: `useGLTF` and `useTexture` suspend while
loading, so an async helper without a Suspense boundary above it throws.

## What is in the box

drei ships a few hundred helpers; this skill covers the ones that matter for
production 3D sites, grouped by job:

- **Controls** — OrbitControls, ScrollControls + useScroll + Scroll, PresentationControls, CameraControls
- **Staging & lighting** — Environment (+ Lightformer), Stage, ContactShadows, AccumulativeShadows + RandomizedLight, SoftShadows, Sky
- **Loaders** — useGLTF (+ preload), useTexture, Clone, useAnimations
- **Materials** — MeshTransmissionMaterial (glass), MeshReflectorMaterial (floor), MeshDistortMaterial, shaderMaterial
- **Text & overlay** — Text (SDF), Text3D, Html (occlude/transform), Billboard
- **Performance** — Instances/Instance, Merged, Detailed (LOD), PerformanceMonitor, AdaptiveDpr, BakeShadows, Preload, meshBounds
- **Framing** — Bounds + useBounds

Full prop tables, transmission tuning, and instancing at scale live in
[references/advanced.md](references/advanced.md).

## Controls

`makeDefault` registers the control as the scene's default, so other helpers
(like Bounds) know which controls to drive and pause.

```jsx
import { OrbitControls } from '@react-three/drei'

<OrbitControls
  makeDefault
  enablePan={false}
  minPolarAngle={Math.PI / 3}
  maxPolarAngle={Math.PI / 2}
  minDistance={3}
  maxDistance={8}
/>
```

**PresentationControls** is the right control for a hero product shot: it springs
back to center instead of freely orbiting, so the model always faces the camera.

```jsx
import { PresentationControls } from '@react-three/drei'

<PresentationControls
  global                       // capture drags anywhere on the canvas
  snap                         // spring back to the resting rotation on release
  speed={1.5}
  zoom={0.8}
  polar={[-Math.PI / 4, Math.PI / 4]}
  azimuth={[-Math.PI / 4, Math.PI / 4]}
>
  <Model />
</PresentationControls>
```

**CameraControls** wraps yomotsu/camera-controls for smooth, imperative camera
moves (`dollyTo`, `setLookAt`, `fitToBox`) — reach for it when you need scripted
transitions between camera framings rather than free orbit.

## Scroll-driven 3D

This is the pattern behind most scroll-story R3F sites. `ScrollControls`
virtualizes `pages` worth of scroll height over the canvas; `useScroll` reads the
normalized scroll position inside `useFrame`; `Scroll` renders content that moves
with scroll (add `html` to overlay real DOM in sync with the 3D).

```jsx
import { Canvas, useFrame } from '@react-three/fiber'
import { ScrollControls, Scroll, useScroll } from '@react-three/drei'

function Rig() {
  const scroll = useScroll()
  useFrame((state) => {
    // offset is 0..1 across the whole scroll range
    state.camera.position.z = 5 - scroll.offset * 3
    // range(start, distance) returns 0..1 within a slice of the scroll
    const fade = scroll.range(0, 1 / 3)
    state.camera.rotation.y = fade * 0.4
  })
  return null
}

<Canvas>
  <ScrollControls pages={3} damping={0.25}>
    <Model />
    <Rig />
    <Scroll html>
      <h1 style={{ position: 'absolute', top: '100vh' }}>Section two</h1>
    </Scroll>
  </ScrollControls>
</Canvas>
```

Read `useScroll` values only inside `useFrame`, never in render — they mutate
every frame and reading them during render will not re-render the component.
`damping` smooths the scroll; higher = more lag. `useScroll` also exposes
`range(start, distance)` and `curve(start, distance)` for per-section easing and
`visible(start, distance)` for on/off ranges.

For a Lenis-based smooth-scroll page where the 3D reacts to real page scroll
instead of a virtualized canvas, use the `lenis-smooth-scroll` skill for the page
and drive the scene from its scroll value.

## Staging & lighting

Good lighting is what separates a toy scene from an award-tier one. Prefer
image-based lighting (`Environment`) over stacking point lights.

```jsx
import { Environment, ContactShadows } from '@react-three/drei'

<Environment preset="city" background blur={0.5} />
<ContactShadows position={[0, -0.5, 0]} opacity={0.6} scale={10} blur={2} far={4} />
```

`preset` pulls a curated HDRI (studio, city, sunset, dawn, night, warehouse,
forest, apartment, park, lobby). `background` also paints it behind the scene;
omit it to light only. For a fully custom studio, drop `Lightformer` children
inside `Environment` to place emissive panels — that is how product renders get
their signature soft reflections. See references/advanced.md for the Lightformer
setup.

**Stage** is the fastest path to a presentable single-object scene — it wires up
environment, shadows, and auto-centered framing in one component:

```jsx
import { Stage } from '@react-three/drei'

<Stage environment="city" intensity={0.5} shadows="contact" adjustCamera>
  <Model />
</Stage>
```

**ContactShadows** fakes a soft grounding shadow with a blurred shadow map —
cheap and almost always the right call. For physically accurate, baked-looking
shadows on a static hero, use **AccumulativeShadows** with **RandomizedLight**,
which accumulates many shadow samples over several frames:

```jsx
import { AccumulativeShadows, RandomizedLight } from '@react-three/drei'

<AccumulativeShadows temporal frames={100} alphaTest={0.9} scale={12} position={[0, -0.5, 0]}>
  <RandomizedLight amount={8} radius={4} ambient={0.5} position={[5, 5, -5]} />
</AccumulativeShadows>
```

`temporal` spreads the `frames` samples across real frames so the first paint is
cheap; the shadow crisps up over the next second. Because it accumulates, it fits
static scenes — a spinning object smears the shadow.

**SoftShadows** patches the shadow shader globally for percentage-closer soft
shadows (`size`, `samples`, `focus`) — call it once. **Sky** renders a physical
sky dome for outdoor scenes.

## Loaders

`useGLTF` loads and caches a GLTF/GLB and returns `{ scene, nodes, materials,
animations }`. Pass a Draco-compressed model's flag to decode it, and always
`preload` the URL at module scope so the fetch starts before React mounts the
component.

```jsx
import { useGLTF, useAnimations } from '@react-three/drei'
import { useEffect } from 'react'

function Avatar() {
  const { scene, animations } = useGLTF('/avatar-draco.glb', true) // true = Draco
  const { actions, names } = useAnimations(animations, scene)
  useEffect(() => {
    actions[names[0]]?.reset().fadeIn(0.3).play()
    return () => actions[names[0]]?.fadeOut(0.3)
  }, [actions, names])
  return <primitive object={scene} />
}

useGLTF.preload('/avatar-draco.glb', true)
```

Rendering the same `useGLTF` scene twice reuses one object graph, which breaks —
the second mount steals the first. Use **Clone** to render multiple independent
copies of a loaded scene:

```jsx
import { Clone } from '@react-three/drei'
const { scene } = useGLTF('/tree.glb')
// each Clone is an independent, mountable copy
<Clone object={scene} position={[0, 0, 0]} />
<Clone object={scene} position={[3, 0, 0]} />
```

**useTexture** loads one or many textures with the same Suspense caching:

```jsx
import { useTexture } from '@react-three/drei'
const props = useTexture({
  map: '/color.jpg',
  normalMap: '/normal.jpg',
  roughnessMap: '/roughness.jpg',
})
<meshStandardMaterial {...props} />
```

## Materials

drei ships the materials that make R3F sites look expensive. Quick reference —
full prop tables in references/advanced.md.

**MeshTransmissionMaterial** is production glass (refraction, thickness, chromatic
aberration). **MeshReflectorMaterial** is a blurred reflective floor.
**MeshDistortMaterial** wobbles vertices for organic blobs.

```jsx
import { MeshTransmissionMaterial } from '@react-three/drei'

<mesh>
  <sphereGeometry args={[1, 64, 64]} />
  <MeshTransmissionMaterial
    thickness={0.6}
    roughness={0.1}
    transmission={1}
    ior={1.5}
    chromaticAberration={0.05}
    backside
  />
</mesh>
```

For a custom GLSL material, **shaderMaterial** generates a
`THREE.ShaderMaterial` subclass with typed uniforms that you `extend()` into JSX,
then animate by mutating the uniform in `useFrame`. Full runnable recipe:
[references/advanced.md](references/advanced.md#shadermaterial-custom-glsl).

## Text & overlay

**Text** renders crisp SDF text on the GPU (troika) — cheap and scalable, the
default for any 3D-space label. **Text3D** extrudes a font into real geometry.
**Html** projects real DOM into the scene; `occlude` hides it behind meshes,
`transform` makes it live in 3D space, and `distanceFactor` scales it with
distance. **Billboard** keeps its children always facing the camera.

```jsx
import { Text, Html, Billboard } from '@react-three/drei'

<Text fontSize={0.5} color="white" anchorX="center" anchorY="middle">
  Hello 3D
</Text>

<Billboard>
  <Html occlude transform distanceFactor={4} position={[0, 1.5, 0]}>
    <div className="label">Buy now</div>
  </Html>
</Billboard>
```

`Html` with `transform` renders through a CSS3D layer that a browser cannot
composite with WebGL depth, so heavy overlays cost real layout — keep them small
and few. On the React Native (`native`) build, `Html` and `Loader` are not
exported.

## Performance

**Instances** draws thousands of the same geometry in one draw call. Wrap the
geometry+material once, then render lightweight `Instance` children:

```jsx
import { Instances, Instance } from '@react-three/drei'

<Instances limit={1000} range={1000}>
  <boxGeometry />
  <meshStandardMaterial />
  {positions.map((p, i) => (
    <Instance key={i} position={p} color="orange" />
  ))}
</Instances>
```

`limit` sets the allocated buffer size (the ceiling); `range` how many draw this
frame. **Merged** does the same for multiple distinct meshes from a loaded model.
**Detailed** is level-of-detail: pass distance thresholds and it swaps to cheaper
meshes as the camera pulls away.

**PerformanceMonitor** watches the framerate and lets you scale quality down on
weak devices — the single most impactful helper for shipping to real hardware:

```jsx
import { PerformanceMonitor, AdaptiveDpr } from '@react-three/drei'
import { useState } from 'react'

function Scene() {
  const [dpr, setDpr] = useState(1.5)
  return (
    <Canvas dpr={dpr}>
      <PerformanceMonitor
        onIncline={() => setDpr(2)}
        onDecline={() => setDpr(1)}
      />
      <AdaptiveDpr pixelated />
      {/* scene */}
    </Canvas>
  )
}
```

`AdaptiveDpr` drops resolution while the camera moves and restores it when still.
**BakeShadows** freezes the shadow map after one frame for fully static scenes.
**Preload** with `all` forces every asset onto the GPU during the Suspense
fallback so the first interactive frame never stutters. **meshBounds** is a
cheap bounding-sphere raycast for pointer events when precise hit-testing is
overkill.

## Framing with Bounds

**Bounds** auto-frames its children in the camera; **useBounds** exposes an
imperative API to refit on demand — the standard way to "zoom to the clicked
part" in a configurator.

```jsx
import { Bounds, useBounds } from '@react-three/drei'

function SelectToZoom({ children }) {
  const api = useBounds()
  return (
    <group onClick={(e) => (e.stopPropagation(), api.refresh(e.object).fit())}>
      {children}
    </group>
  )
}

<Bounds fit clip observe margin={1.2}>
  <SelectToZoom>
    <Model />
  </SelectToZoom>
</Bounds>
```

`fit` frames on mount, `clip` sets near/far to the content, `observe` refits on
resize, `margin` pads the framing. Bounds drives the default controls, so give
your controls `makeDefault`.

## React / Next.js integration

- Mount the `<Canvas>` in a client component. In Next.js App Router, put
  `'use client'` at the top of the file and load it with `next/dynamic` and
  `ssr: false` — WebGL has no server render, and SSR-ing the Canvas throws.

  ```jsx
  'use client'
  import dynamic from 'next/dynamic'
  const Scene = dynamic(() => import('./Scene'), { ssr: false })
  ```

- Cleanup is mostly automatic: R3F disposes geometries, materials, and textures
  it created when a component unmounts. What it does not own, you dispose — a
  texture or geometry you `new`-ed outside JSX, or an object added imperatively
  via `scene.add`. Call `.dispose()` in a `useEffect` cleanup for those.

- Keep GLB/HDRI assets in `public/` and reference them by absolute path
  (`/model.glb`), and `useGLTF.preload` at module scope so the fetch overlaps the
  route transition.

## Accessibility

WebGL canvases are invisible to assistive tech and heavy motion can trigger
vestibular discomfort — always honor reduced-motion.

```jsx
import { useReducedMotion } from 'framer-motion' // or a matchMedia hook
const reduce = useReducedMotion()

useFrame((state) => {
  if (reduce) return                 // freeze idle animation
  ref.current.rotation.y += 0.01
})
```

- Gate autoplaying spins, scroll parallax, and camera drifts behind
  `prefers-reduced-motion`; keep the scene static when it is set.
- The canvas is decorative to a screen reader. Provide the real content (product
  name, price, CTA) as normal DOM outside the Canvas, or in an `Html` overlay, so
  the page is usable without the 3D.
- Ensure any interaction available by dragging the model is also reachable with
  standard DOM controls (buttons, links) elsewhere on the page.

## Pitfalls

- **Suspense boundaries.** Every async helper (`useGLTF`, `useTexture`,
  `Environment` with `files`) suspends. Wrap them in `<Suspense>` or the app
  throws. One boundary around the whole scene is fine; nest more for staged
  reveals.
- **Version pinning.** drei tracks R3F and Three closely. A drei built for R3F v9
  / Three r160+ will break against older majors with cryptic errors. Pin all
  three to compatible versions and upgrade them together, not piecemeal.
- **three-stdlib, not three/examples.** drei pulls helpers from `three-stdlib`,
  so import controls and loaders from drei — do not mix in
  `three/examples/jsm` copies of the same class.
- **Reusing a loaded scene.** `useGLTF` returns one shared object graph. Render it
  once, or use `Clone` for copies. Rendering the raw `scene` twice makes the
  second mount steal it from the first.
- **Reading useScroll in render.** Its values mutate per frame; read them inside
  `useFrame`, never during render.
- **Html overlays are not free.** `transform` Html renders through CSS3D and
  cannot depth-composite with WebGL; many overlays tank layout performance. And
  it is not exported on the `native` build.
- **Dispose what you own.** R3F cleans up what it created; manually-added objects
  and out-of-JSX textures/geometries leak until you `.dispose()` them.

## References

Official sources this skill was written against:

- drei documentation — https://drei.docs.pmnd.rs/
- drei source, README, and full component list — https://github.com/pmndrs/drei
- React Three Fiber (the renderer drei extends) — https://r3f.docs.pmnd.rs/

Advanced material and performance reference (full prop tables, transmission
tuning, Lightformer studios, instancing at scale):
[references/advanced.md](references/advanced.md)
