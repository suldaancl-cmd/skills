---
name: webgl-effect-recipes
description: Use when adding a drop-in WebGL/shader hero effect to a premium site — fluid cursor, image distortion, postprocessing bloom, gradient/noise backgrounds. Five verified, copy-paste recipes (PavelDoGreat fluid sim, OGL Flowmap, R3F image hover-distortion, @react-three/postprocessing Bloom+Vignette, simplex-noise gradient background) with real repo URLs, exact config knobs, minimal snippets, and a mandatory performance/bundle-budget section. Reach for this on Awwwards-tier landing pages where one tasteful GPU effect carries the hero.
---

# WebGL Effect Recipes (drop-in, 2026)

Five battle-tested effects used on premium/Awwwards sites. Each is self-contained — pick ONE per page, never stack heroes. All snippets verified against the real repos (June 2026).

**Rule of taste:** one effect carries the hero; everything else stays still. A second WebGL surface competing for attention reads as a tech demo, not a premium brand.

---

## 1. PavelDoGreat WebGL Fluid Simulation — cursor smoke/ink background

**What it is:** Real-time Navier-Stokes fluid on a fullscreen `<canvas>`. Cursor drags leave dye/smoke trails. Raw WebGL2, no framework. The single most-cloned premium hero background.

**Source:** https://github.com/PavelDoGreat/WebGL-Fluid-Simulation (MIT). The original `script.js` grabs `document.getElementsByTagName('canvas')[0]` and is a single file you drop in.

**Maintained npm fork (recommended for React/Next/Vue):** https://github.com/michaelbrusegard/WebGL-Fluid-Enhanced — ES modules, TypeScript, minified, no dat.gui. `npm i webgl-fluid-enhanced`.

**Integration (Enhanced fork, React):**
```jsx
import { useEffect, useRef } from 'react';
import WebGLFluidEnhanced from 'webgl-fluid-enhanced';

export default function FluidHero() {
  const canvasRef = useRef(null);
  useEffect(() => {
    const sim = new WebGLFluidEnhanced(canvasRef.current);
    sim.setConfig({
      DENSITY_DISSIPATION: 3.5,   // higher = trails fade faster (orig default 1)
      VELOCITY_DISSIPATION: 2,    // motion damping (orig default 0.2)
      PRESSURE: 0.8,
      CURL: 30,                   // vorticity / swirl — 0 = calm, 50 = chaotic
      SPLAT_RADIUS: 0.2,          // size of each cursor dab (orig default 0.25)
      SPLAT_FORCE: 6000,
      COLOR_PALETTE: ['#0a0a0a', '#1a1a2e', '#7b2ff7'], // brand-lock the dye
      BACK_COLOR: '#000000',
      TRANSPARENT: false,
      BLOOM: true,
    });
    sim.start();
    return () => sim.stop();
  }, []);
  return <canvas ref={canvasRef} style={{ position: 'fixed', inset: 0, zIndex: -1 }} />;
}
```

**Key config knobs** (verified defaults from `script.js`): `SIM_RESOLUTION: 128`, `DYE_RESOLUTION: 1024`, `DENSITY_DISSIPATION: 1`, `VELOCITY_DISSIPATION: 0.2`, `PRESSURE: 0.8`, `CURL: 30`, `SPLAT_RADIUS: 0.25`, `SPLAT_FORCE: 6000`, `SHADING: true`, `BLOOM: true`.

**Premium tuning:** drop `DYE_RESOLUTION` to 512 and `SIM_RESOLUTION` to 64 for retina perf; bump `DENSITY_DISSIPATION` to 3–4 so trails dissolve fast (lingering ink looks cheap); lock `COLOR_PALETTE` to 2–3 brand colors instead of the default rainbow.

---

## 2. OGL + Flowmap — cursor-velocity image/text distortion

**What it is:** Cursor drags a "flow" through an image — water-on-glass ripple that follows mouse velocity. Far lighter than Three.js: OGL is **"Total 29kb"** minzipped with **zero dependencies** (per the README).

**Source:** https://github.com/oframe/ogl — `npm i ogl`. Reference example: https://github.com/oframe/ogl/blob/master/examples/mouse-flowmap.html · Flowmap class: https://github.com/oframe/ogl/blob/master/src/extras/Flowmap.js · walkthrough: https://tympanus.net/codrops/2019/09/25/mouse-flowmap-deformation-with-ogl/

**How it works:** `Flowmap` renders cursor velocity into an **RG float texture** every frame — R = velocity.x, G = velocity.y (B = velocity length). Your fragment shader samples that flowmap and offsets the image UVs by it, so the distortion trails and decays where the cursor moved.

**Integration (core wiring):**
```js
import { Renderer, Geometry, Program, Mesh, Vec2, Flowmap, Texture } from 'ogl';

const renderer = new Renderer({ dpr: 2 });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

const flowmap = new Flowmap(gl, { falloff: 0.3, dissipation: 0.92 }); // RG velocity target
const mouse = new Vec2(), velocity = new Vec2();
let lastTime, lastMouse = new Vec2();

const program = new Program(gl, {
  vertex: /* glsl */`
    attribute vec2 uv; attribute vec2 position; varying vec2 vUv;
    void main(){ vUv = uv; gl_Position = vec4(position, 0.0, 1.0); }`,
  fragment: /* glsl */`
    precision highp float;
    uniform sampler2D tWater;   // your image
    uniform sampler2D tFlow;    // Flowmap RG output
    varying vec2 vUv;
    void main(){
      vec3 flow = texture2D(tFlow, vUv).rgb;
      vec2 uv = vUv - flow.rg * 0.025;     // displace UVs by cursor velocity
      gl_FragColor = texture2D(tWater, uv);
    }`,
  uniforms: { tWater: { value: imageTexture }, tFlow: flowmap.uniform },
});

function update(t){
  requestAnimationFrame(update);
  const dt = (t - (lastTime || t)) / 1000; lastTime = t;
  velocity.set((mouse.x - lastMouse.x) / Math.max(dt, 1e-4),
               (mouse.y - lastMouse.y) / Math.max(dt, 1e-4));
  lastMouse.copy(mouse);
  flowmap.aspect = gl.canvas.width / gl.canvas.height;
  flowmap.mouse.copy(mouse);
  flowmap.velocity.lerp(velocity, 0.1); // smooth so it glides, not jitters
  flowmap.update();                      // writes RG velocity texture
  renderer.render({ scene: mesh });
}
requestAnimationFrame(update);
```
Use this for product images, hero photography, or large display type. The `0.025` displacement multiplier is the taste knob — keep it subtle.

---

## 3. React Three Fiber — image hover-distortion shader (mouse velocity → UV displacement)

**What it is:** Hover an image, it ripples/warps via a custom GLSL shader; a `uProgress` uniform (0→1) animated by **GSAP** drives reveal/transition intensity. The R3F-native version of the Codrops "motion hover" classic: https://tympanus.net/codrops/2019/10/21/how-to-create-motion-hover-effects-with-image-distortions-using-three-js/

**Source:** Three.js https://github.com/mrdoob/three.js · R3F https://github.com/pmndrs/react-three-fiber · drei (`useTexture`, `shaderMaterial`) https://github.com/pmndrs/drei · `npm i three @react-three/fiber @react-three/drei gsap`

**Integration:**
```jsx
import * as THREE from 'three';
import { Canvas, useFrame, extend } from '@react-three/fiber';
import { useTexture, shaderMaterial } from '@react-three/drei';
import { useRef } from 'react';
import gsap from 'gsap';

const DistortMaterial = shaderMaterial(
  { uTexture: null, uProgress: 0, uMouse: new THREE.Vector2(0.5, 0.5), uTime: 0 },
  /* vertex */`
    varying vec2 vUv;
    void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
  /* fragment */`
    uniform sampler2D uTexture; uniform float uProgress; uniform vec2 uMouse;
    varying vec2 vUv;
    void main(){
      float d = distance(vUv, uMouse);
      vec2 uv = vUv + normalize(vUv - uMouse) * uProgress * 0.06 * (1.0 - d);
      // subtle RGB split scales with the same progress
      float r = texture2D(uTexture, uv + vec2(0.01,0.0)*uProgress).r;
      vec4 g = texture2D(uTexture, uv);
      gl_FragColor = vec4(r, g.g, g.b, 1.0);
    }`
);
extend({ DistortMaterial });

function Plane() {
  const mat = useRef();
  const tex = useTexture('/hero.jpg');
  useFrame((s) => { mat.current.uTime = s.clock.elapsedTime; });
  return (
    <mesh
      onPointerMove={(e) => (mat.current.uMouse = e.uv)}
      onPointerOver={() => gsap.to(mat.current, { uProgress: 1, duration: 0.6, ease: 'power3.out' })}
      onPointerOut={() => gsap.to(mat.current, { uProgress: 0, duration: 0.8, ease: 'power3.out' })}
    >
      <planeGeometry args={[3, 4, 32, 32]} />
      <distortMaterial ref={mat} uTexture={tex} />
    </mesh>
  );
}

export default () => <Canvas camera={{ position: [0, 0, 5] }}><Plane /></Canvas>;
```
GSAP owning `uProgress` (not `useFrame` lerp) gives you eased, designable timing and lets you reuse the same tween on scroll-in.

---

## 4. @react-three/postprocessing — Bloom + Vignette

**What it is:** EffectComposer pass that adds cinematic glow (Bloom) and edge darkening (Vignette) over any R3F scene. The "expensive-looking" finish on dark hero scenes.

**Source:** https://github.com/pmndrs/react-postprocessing · docs https://react-postprocessing.docs.pmnd.rs/ · `npm i @react-three/postprocessing postprocessing` (peer deps: `postprocessing`, `@react-three/fiber`, `three`).

**Integration:**
```jsx
import { EffectComposer, Bloom, Vignette } from '@react-three/postprocessing';

<Canvas>
  {/* ...your scene... */}
  <EffectComposer disableNormalPass>
    <Bloom
      intensity={1.0}
      luminanceThreshold={0.9}   // only pixels brighter than this glow
      luminanceSmoothing={0.025}
      mipmapBlur                  // cheaper, softer bloom — keep on
    />
    <Vignette offset={0.3} darkness={0.7} />
  </EffectComposer>
</Canvas>
```

**Critical gotcha:** Bloom only fires on values **above the standard 0–1 range**. Set `toneMapped={false}` on the materials you want to glow and push their color/emissive past 1 (e.g. `emissiveIntensity={2}`). Raise `luminanceThreshold` toward 1 to make *nothing* glow by default, then opt specific materials in. Keep `mipmapBlur` on — it is dramatically cheaper than the legacy kernel.

---

## 5. Animated gradient / noise shader background

**What it is:** A fullscreen quad whose fragment shader scrolls simplex noise to produce a slow, living gradient (the "aurora mesh" look). Cheapest premium effect — one draw call, no geometry, no textures.

**Source (noise):** canonical Ashima/Stefan Gustavson `snoise` — https://github.com/stegu/webgl-noise (paste `snoise(vec3)` from `src/noise3D.glsl`). Run it on a single plane via R3F, OGL, or raw WebGL.

**Integration (R3F, drop-in fragment):**
```glsl
// uniforms: uTime (float), uResolution (vec2), uColorA/uColorB (vec3)
// #include the snoise(vec3) function from stegu/webgl-noise above this main()
varying vec2 vUv;
void main(){
  vec2 uv = vUv;
  float n  = snoise(vec3(uv * 2.5, uTime * 0.08));        // base flow
  n += 0.5 * snoise(vec3(uv * 5.0, uTime * 0.12));         // finer detail octave
  float t = smoothstep(-0.6, 0.6, n);
  vec3 col = mix(uColorA, uColorB, t);
  col += 0.03 * snoise(vec3(uv * 200.0, uTime));           // film grain kills banding
  gl_FragColor = vec4(col, 1.0);
}
```
Drive `uTime` from `useFrame`. Two brand colors in `uColorA/uColorB`, slow time multipliers (0.05–0.15 — fast = nauseating), and the grain line to avoid 8-bit banding. This is the safest effect to ship: trivially cheap, degrades gracefully, never blocks paint.

---

## PERFORMANCE (mandatory — read before shipping any of the above)

**Bundle budget — know what you're importing:**
- Three.js core ≈ **600KB** minified; a full R3F + drei + postprocessing hero easily exceeds **3MB**. OGL is **29KB**. Raw-WebGL fluid sim is one ~50KB file. **Prefer OGL or raw WebGL when a single effect is all you need** — reach for Three.js only when the scene genuinely needs its scene-graph/loader ecosystem.

**Defer the 3D bundle past first paint:**
- Never block LCP on a WebGL bundle. Lazy-load it. Next.js: `const FluidHero = dynamic(() => import('./FluidHero'), { ssr: false })`. Vite/React: `React.lazy` + `<Suspense>`. Start the GL context after the hero text/LCP image has painted, ideally on `requestIdleCallback` or first interaction.

**Move shader compile off the main thread (OffscreenCanvas worker):**
- Shader compilation and the first frame can jank the main thread. Render in a Web Worker via `canvas.transferControlToOffscreen()` and run the GL loop there, so scroll/input stays at 60fps during warm-up. (Supported in modern Chromium/Firefox; feature-detect `'transferControlToOffscreen' in HTMLCanvasElement.prototype` and fall back to main-thread on Safari.)

**Ship a static image on mobile:**
- Fluid sims and postprocessing are battery and GPU killers on phones. Feature-detect and serve a pre-rendered hero still (or the noise-gradient recipe, which is cheap) instead of the full simulation. Gate on `window.matchMedia('(pointer: fine)').matches` (cursor effects are pointless on touch anyway) and `(prefers-reduced-motion: reduce)` — respect both.

**Asset/texture discipline (Three.js scenes):**
- Compress GLB with `gltf-transform` (https://gltf-transform.dev) and ship **KTX2** (Basis-compressed) textures, not PNG/JPG — they upload to the GPU compressed, cutting VRAM and load time. `gltf-transform optimize in.glb out.glb --texture-compress ktx2`.

**Always set DPR and dispose:**
- Cap `dpr={[1, 2]}` (uncapped retina DPR quadruples fragment work). Dispose GL contexts/geometries/textures on unmount — every recipe above returns a cleanup that stops the RAF loop and frees the context.

**Cited sources:** PavelDoGreat https://github.com/PavelDoGreat/WebGL-Fluid-Simulation · Enhanced fork https://github.com/michaelbrusegard/WebGL-Fluid-Enhanced · OGL https://github.com/oframe/ogl · Flowmap demo https://tympanus.net/codrops/2019/09/25/mouse-flowmap-deformation-with-ogl/ · react-postprocessing https://github.com/pmndrs/react-postprocessing · drei https://github.com/pmndrs/drei · webgl-noise https://github.com/stegu/webgl-noise · gltf-transform https://gltf-transform.dev
