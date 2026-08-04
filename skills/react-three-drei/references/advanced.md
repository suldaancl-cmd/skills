# drei — advanced materials, staging & performance

Deep reference for the drei helpers whose full surface did not fit in SKILL.md.
Prop names below are drawn from the official docs and README
(https://github.com/pmndrs/drei, https://drei.docs.pmnd.rs/). Where a numeric
range matters it is a tuning starting point, not a hard rule — tune against your
own scene and hardware.

## MeshTransmissionMaterial — production glass

An extension of Three's `MeshPhysicalMaterial` transmission with extra controls
for thickness, roughness blur, and chromatic aberration. This is what makes glass,
gems, and frosted panels read as real.

```jsx
<MeshTransmissionMaterial
  transmission={1}          // 0..1 — how much light passes through (1 = full glass)
  thickness={0.5}           // volume thickness; drives refraction depth
  roughness={0.1}           // surface blur; higher = frosted
  ior={1.5}                 // index of refraction (glass ~1.5, water ~1.33, diamond ~2.4)
  chromaticAberration={0.05}// rainbow fringing at edges
  anisotropy={0.1}          // directional blur
  distortion={0.2}          // surface distortion strength
  distortionScale={0.3}
  temporalDistortion={0.1}  // animates distortion over time
  backside                  // render back faces first for convincing double refraction
  samples={10}              // resolution of the transmission buffer render
  resolution={256}          // buffer resolution; raise for sharper refraction, costs GPU
/>
```

Tuning notes:

- `backside` renders the object twice (back faces, then front) for real
  double-sided refraction — the single biggest quality lever, and the biggest
  cost. Turn it off on distant or many glass objects.
- `resolution` and `samples` are the perf knobs. Transmission renders the scene
  into a buffer every frame; drop these on mobile or when there are several glass
  meshes.
- Give the geometry enough segments (`sphereGeometry args={[1, 64, 64]}`) —
  refraction exposes low-poly faceting.

## MeshReflectorMaterial — reflective floor

A blurred, mip-mapped planar reflector for floors and water. Put it on a large
plane laid flat under the scene.

```jsx
<mesh rotation={[-Math.PI / 2, 0, 0]}>
  <planeGeometry args={[50, 50]} />
  <MeshReflectorMaterial
    resolution={1024}       // reflection buffer size; 512 mobile, 1024–2048 desktop
    blur={[400, 100]}       // [x, y] blur of the reflection
    mixBlur={1}             // how much blur mixes with sharp reflection
    mixStrength={0.8}       // reflection intensity
    depthScale={1}          // depth-based fade
    minDepthThreshold={0.4}
    maxDepthThreshold={1.4}
    roughness={1}
    mirror={0}              // 0 = environment-tinted, 1 = pure mirror
  />
</mesh>
```

`resolution` and `blur` dominate cost — a reflector renders the scene a second
time. One large reflector is fine; avoid several.

## MeshDistortMaterial — organic wobble

`MeshPhysicalMaterial` whose vertices are displaced by noise. For blobs, liquid
metal, and living surfaces.

```jsx
<mesh>
  <icosahedronGeometry args={[1, 32]} />  {/* needs dense geometry */}
  <MeshDistortMaterial distort={0.4} speed={2} roughness={0.2} color="#5a4fff" />
</mesh>
```

`distort` is amplitude, `speed` is animation rate. Distortion is per-vertex, so a
low-poly mesh distorts into a faceted mess — use a subdivided geometry.

## shaderMaterial — custom GLSL

`shaderMaterial(uniforms, vertexShader, fragmentShader)` returns a
`THREE.ShaderMaterial` subclass with each uniform exposed as a typed property.
`extend()` registers it as a JSX element (lowercased first letter), and you
animate it by mutating the uniform ref in `useFrame`.

```jsx
import * as THREE from 'three'
import { shaderMaterial } from '@react-three/drei'
import { extend, useFrame } from '@react-three/fiber'
import { useRef } from 'react'

const WaveMaterial = shaderMaterial(
  { uTime: 0, uColor: new THREE.Color('hotpink') },
  `varying vec2 vUv;
   void main() {
     vUv = uv;
     gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
   }`,
  `uniform float uTime;
   uniform vec3 uColor;
   varying vec2 vUv;
   void main() {
     gl_FragColor = vec4(uColor * (0.5 + 0.5 * sin(uTime + vUv.x * 10.0)), 1.0);
   }`
)
extend({ WaveMaterial })

function Wave() {
  const ref = useRef()
  useFrame((_, dt) => (ref.current.uTime += dt))
  return (
    <mesh>
      <planeGeometry args={[4, 4, 32, 32]} />
      <waveMaterial ref={ref} />
    </mesh>
  )
}
```

## Environment + Lightformer — a custom studio

`preset` is the quick path; a hand-built Lightformer rig is how product renders
get bespoke reflections. Lightformers are emissive planes/rings placed in the
environment map, visible in reflections but not lighting like scene lights.

```jsx
import { Environment, Lightformer } from '@react-three/drei'

<Environment resolution={512}>
  {/* key light overhead */}
  <Lightformer intensity={2} position={[0, 5, -5]} scale={[10, 5, 1]} />
  {/* rim strip along the side, visible as a highlight on glossy surfaces */}
  <Lightformer form="ring" intensity={1} position={[-5, 1, -1]} scale={2} />
  <Lightformer form="rect" intensity={1.5} position={[5, 3, 1]} scale={[3, 8, 1]} />
</Environment>
```

`form` is `rect` (default), `circle`, or `ring`. `files` on `Environment` loads a
custom HDRI/EXR instead of a preset. `ground` projects the environment onto a
floor plane for a grounded backdrop.

## AccumulativeShadows + RandomizedLight — full prop set

Progressive, baked-quality contact shadows for static scenes.

```jsx
<AccumulativeShadows
  temporal                  // spread frames over time; cheap first paint
  frames={100}              // samples to accumulate (Infinity keeps refining)
  alphaTest={0.9}           // shadow darkness cutoff
  opacity={1}
  scale={12}                // size of the shadow-catcher plane
  color="black"
  position={[0, -0.5, 0]}
>
  <RandomizedLight
    amount={8}              // number of jittered light samples
    radius={4}              // jitter radius — larger = softer penumbra
    ambient={0.5}           // ambient occlusion contribution
    intensity={1}
    position={[5, 5, -5]}
    bias={0.001}
  />
</AccumulativeShadows>
```

Because it accumulates, it only suits still scenes. Any movement of the caster or
lights smears the result. Pair with `frames={Infinity}` and no `temporal` for a
one-shot high-quality bake, or `temporal` + finite `frames` for a scene that
crisps up over the first second.

## SoftShadows — global PCSS

Patches Three's shadow shader for percentage-closer soft shadows. Call the
component once anywhere in the tree; it affects all shadow-casting lights.

```jsx
<SoftShadows size={25} samples={16} focus={0} />
```

`size` is penumbra width, `samples` is quality (higher = smoother, slower),
`focus` is the distance of sharpest shadow. It recompiles shaders, so toggling it
at runtime is expensive — set it once.

## Instances at scale

For thousands to millions of repeats, `Instances`/`Instance` collapse to one draw
call. Animate instances by mutating their refs in `useFrame`, not by re-rendering.

```jsx
import { Instances, Instance } from '@react-three/drei'
import { useRef } from 'react'
import { useFrame } from '@react-three/fiber'

function Field({ data }) {
  return (
    <Instances limit={data.length}>   {/* limit = buffer ceiling */}
      <sphereGeometry args={[0.1, 16, 16]} />
      <meshStandardMaterial />
      {data.map((d, i) => <Bit key={i} {...d} />)}
    </Instances>
  )
}

function Bit({ position, speed }) {
  const ref = useRef()
  useFrame((state) => {
    ref.current.position.y = position[1] + Math.sin(state.clock.elapsedTime * speed)
  })
  return <Instance ref={ref} position={position} />
}
```

`Merged` is the equivalent for a set of distinct meshes pulled from a loaded
model — it returns instanced components for each mesh so you can scatter a whole
kit (a decorated model, furniture set) cheaply.

## Detailed — level of detail

Swap to cheaper geometry as the camera recedes. Children are ordered
highest-detail first; the `distances` array sets the switch thresholds.

```jsx
import { Detailed } from '@react-three/drei'

<Detailed distances={[0, 10, 25]}>
  <mesh geometry={highPoly} />   {/* shown 0–10 units away */}
  <mesh geometry={midPoly} />    {/* 10–25 */}
  <mesh geometry={lowPoly} />    {/* 25+ */}
</Detailed>
```

## PerformanceMonitor — advanced flags

Beyond `onIncline`/`onDecline`, it exposes hysteresis and bounds so quality does
not oscillate:

```jsx
<PerformanceMonitor
  bounds={(refreshrate) => (refreshrate > 90 ? [50, 90] : [50, 60])}
  flipflops={3}                     // give up adapting after N direction flips
  onFallback={() => setDpr(1)}      // final floor when it stops adapting
  onIncline={() => setDpr(2)}
  onDecline={() => setDpr(1)}
  onChange={({ factor }) => {/* 0..1 headroom, drive any quality setting */}}
/>
```

Drive `dpr`, shadow map size, `Environment resolution`, post-processing passes, or
instance counts off the `factor` for graceful degradation on weak GPUs.

## Preload — force GPU upload

`useGLTF.preload(url)` warms the fetch/parse cache; `<Preload all />` inside the
Canvas forces every loaded object onto the GPU during the Suspense fallback, so
the first interactive frame does not hitch while textures compile.

```jsx
<Suspense fallback={<Loader />}>
  <Model />
  <Environment preset="city" />
  <Preload all />
</Suspense>
```
