# 3D on the web — Three.js, R3F, Spline, WebGL, WebGPU

3D is not a decoration pass. It's a commitment: it changes performance budgets, accessibility, asset pipelines, and fallbacks. Use only when it carries the story.

## When 3D is worth it

- **Product configuration** — rotate, customize (cars, furniture, wearables).
- **Data visualization** — networks, geospatial, molecular.
- **Brand storytelling** — Apple product pages, cinematic agency portfolios, game sites.
- **Immersive experiences** — virtual tours, WebXR.

## When 3D is NOT worth it

- You want "a cool floating logo" — do it with CSS 3D or a looping GIF.
- You need text animation — SplitText + GSAP beats WebGL text every time.
- The audience is primarily mobile — 3D mobile budgets are brutal.
- You can achieve the same feel with parallax, clip-path, and scroll effects. See `aesthetics.md` → Epic Cinematic 2.5D.

## The stack decision tree

```
Is the 3D content dynamic/interactive?
├── No (hero loop, decorative) → exported video (MP4/WebM) or Lottie
├── Yes, simple (rotating product) → Spline (no-code) or basic Three.js
└── Yes, complex (product config, data viz, game)
    ├── React app → React Three Fiber (R3F)
    ├── Vanilla → Three.js
    └── Need cutting-edge perf → WebGPU / TresJS / Babylon
```

## Three.js core concepts

Minimum viable scene:
```js
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));  // cap DPR for perf
document.body.appendChild(renderer.domElement);

const geometry = new THREE.IcosahedronGeometry(1, 4);
const material = new THREE.MeshStandardMaterial({ color: 0xD4A853, roughness: 0.3, metalness: 0.7 });
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);

const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light, new THREE.AmbientLight(0xffffff, 0.3));

function tick() {
  mesh.rotation.y += 0.005;
  renderer.render(scene, camera);
  requestAnimationFrame(tick);
}
tick();

window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## React Three Fiber (R3F) — the React way

```bash
npm install three @react-three/fiber @react-three/drei
```

```jsx
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment, Float } from "@react-three/drei";

function Scene() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 50 }} dpr={[1, 2]}>
      <Environment preset="studio" />
      <Float speed={2} rotationIntensity={0.5} floatIntensity={0.5}>
        <mesh>
          <icosahedronGeometry args={[1, 4]} />
          <meshStandardMaterial color="#D4A853" roughness={0.3} metalness={0.7} />
        </mesh>
      </Float>
      <OrbitControls enableZoom={false} />
    </Canvas>
  );
}
```

**drei** is the utility library you'll use constantly: `OrbitControls`, `Environment` (HDRIs), `useGLTF` (model loading), `Text`, `Html`, `Float`, `ContactShadows`, `MeshReflectorMaterial`, `shaderMaterial`, `useScroll`.

### R3F + scroll
```jsx
import { ScrollControls, useScroll } from "@react-three/drei";

function ScrollScene() {
  const scroll = useScroll();
  useFrame(() => {
    mesh.current.rotation.y = scroll.offset * Math.PI * 2;
  });
}

<Canvas>
  <ScrollControls pages={3} damping={0.1}>
    <ScrollScene />
  </ScrollControls>
</Canvas>
```

### R3F + GSAP
```jsx
import { useFrame } from "@react-three/fiber";
import { useRef } from "react";
import { gsap } from "gsap";

function AnimatedMesh() {
  const meshRef = useRef();
  useGSAP(() => {
    gsap.to(meshRef.current.rotation, { y: Math.PI * 2, duration: 4, repeat: -1, ease: "none" });
  });
  return <mesh ref={meshRef}>{/* ... */}</mesh>;
}
```

## Spline — no-code 3D for designers

- **When:** You need a slick 3D hero, the scene is somewhat static or lightly interactive, and you don't want to hand-code Three.js.
- **Export:** Embed via `<spline-viewer>` web component, or export to GLTF/React component.
- **Trade-off:** Bundle size is heavier than hand-rolled Three.js. Harder to customize deeply.
- **Mobile:** Spline scenes can be heavy — test early. Often worth a lightweight fallback.

Embed:
```html
<script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.82/build/spline-viewer.js"></script>
<spline-viewer url="https://prod.spline.design/your-scene/scene.splinecode"></spline-viewer>
```

React:
```jsx
import Spline from "@splinetool/react-spline";
<Spline scene="https://prod.spline.design/your-scene/scene.splinecode" />
```

## Performance — 3D mobile budgets

Target: **60fps on a $250 Android phone**, not your M3 Mac.

- **Triangle count:** < 100k for hero scenes. < 30k for secondary. Low-poly + clever materials beats high-poly + default shader.
- **Texture resolution:** Max 2048×2048 for hero assets; 512–1024 elsewhere. Use KTX2 / Basis compression.
- **DPR cap:** `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`. Retina at 3× kills mobile.
- **Shadows:** Off or baked. Real-time shadows are expensive; use `ContactShadows` or baked AO in the texture.
- **Post-processing:** Each pass costs. Bloom, DoF, SSR — pick one, not all.
- **Lazy load:** Don't load 3D assets before first paint. Use IntersectionObserver or defer below-the-fold scenes.
- **Suspense + fallback:** R3F + `<Suspense fallback={<Loader />}>` for any async asset.
- **Dispose on unmount:** Call `.dispose()` on geometries, materials, textures, renderers. R3F handles most of this automatically; vanilla Three.js does not.

## Lighting — the single biggest quality multiplier

Three lights in a scene is usually enough. The default cheap look comes from:
- Single light source, often from the camera's angle (flattens depth).
- No ambient bounce — use a low `AmbientLight` or HDRI.
- No rim light — makes objects look pasted on.

**Studio setup:**
1. **Key light** (main, ~60° from front, bright)
2. **Fill light** (opposite side, 30% brightness, cooler temp)
3. **Rim light** (behind object, bright, creates edge highlight)

Or skip the manual setup and use `<Environment preset="studio" />` or an HDRI. HDRIs are the single biggest quality jump over manual lighting.

## Materials — the second biggest

- **`MeshStandardMaterial`** or **`MeshPhysicalMaterial`** for PBR (physically-based rendering). These react correctly to lighting.
- **`roughness: 0.3, metalness: 0.7`** is a good starting point for "premium object".
- **`clearcoat: 1, clearcoatRoughness: 0.1`** for lacquered/car-paint look.
- **`transmission: 1, thickness: 0.5, ior: 1.5`** for glass.
- Avoid `MeshBasicMaterial` for anything hero — it ignores lighting, looks flat.

## WebGPU — the next step

WebGPU is production-ready in Chrome / Edge / Safari 18+, still flagged in Firefox as of April 2026. It's faster than WebGL and enables compute shaders (particles, simulations, ML on GPU).

- **Three.js WebGPURenderer** is stable now.
- **TresJS** (Vue) and **Threlte** (Svelte) support it.
- **Use case:** High particle counts (millions), fluid sims, complex post-processing, GPU-based physics.
- **Fallback:** Always have a WebGL fallback for Firefox and older browsers.

```js
import WebGPURenderer from "three/addons/renderers/webgpu/WebGPURenderer.js";
const renderer = new WebGPURenderer({ antialias: true });
```

## Accessibility

3D is inherently visual. For users who can't / don't want 3D:
- Always provide a 2D fallback (image, video, or CSS-only version).
- Honor `prefers-reduced-motion` — disable auto-rotating/floating, make interactions opt-in.
- Keyboard-accessible interactions — `OrbitControls` supports this but test it.
- Provide text descriptions of what's being visualized for screen readers.
- Consider battery — auto-pause when tab is hidden (`document.hidden`).

## Common 3D mistakes

- Loading a 50MB GLB for a hero section. Compress with Draco + KTX2. Aim for < 3MB initial.
- Running three.js on the main thread alongside heavy JS — use workers for data prep.
- No loading state — users see a blank hero for 5 seconds.
- Mobile not tested until launch day. Test continuously.
- OrbitControls with pan enabled — users accidentally pan off the subject.
- Camera too close — subtle FOV changes read as amateur. Use 35–50mm equivalent.
- No shadows AND no HDRI — objects float in space with no grounding.

## The test

A 3D scene is working when removing it would demonstrably weaken the story. If you could replace it with a static image and nothing would be lost — do that, and keep the bundle size.
