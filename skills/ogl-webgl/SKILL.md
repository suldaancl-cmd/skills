---
name: ogl-webgl
description: >-
  Build studio-tier image-distortion heroes and shader galleries with OGL, the
  tiny raw-WebGL2 library (Exo Ape / Unseen / Awwwards aesthetic). Fire this
  whenever the work is a full-screen GLSL hero, animated gradient/noise
  background, hover image distortion (displacement + RGB split), flowmap or
  render-target post FX, or any lightweight WebGL/shader effect where Three.js /
  R3F is too heavy. Triggers: OGL, oframe/ogl, raw WebGL, GLSL shader hero,
  image distortion, displacement map, RGB split, fullscreen quad, curtains.js
  alternative, DOM-synced planes, immersive / award / scroll-driven WebGL.
---

# OGL — minimal WebGL for image distortion heroes

## What OGL is and why to reach for it

OGL is a small (about 29kb minzipped, zero dependencies) library over raw WebGL2. It gives you a handful of thin wrappers — `Renderer`, `Program`, `Mesh`, `Geometry`, `Texture` — and then gets out of your way. You write the GLSL yourself.

Reach for OGL when the deliverable is a *shader effect*, not a *3D scene*: a full-screen animated gradient, a hover-distorted image gallery, a flowmap trail, a scroll-driven displacement hero. This is the standard tool for the Exo Ape / Unseen Studio class of image-effect site, where Three.js would drag in a scene graph, materials, and lights you never use.

Stay with Three.js / React Three Fiber when you actually need a 3D scene: loaded GLTF models, real cameras and lights, physics, instancing, an ecosystem of loaders and helpers. OGL has a `Camera` and a `Transform` hierarchy too, but its sweet spot is 2D full-screen shader passes.

Reach for **curtains.js** instead only when the core need is planes that stay pinned to real DOM elements as the page scrolls — curtains was built around syncing WebGL planes to HTML bounding boxes. OGL can do the same with manual math, but curtains makes DOM-synced planes the happy path.

## Quick Start

```bash
npm i ogl
```

Minimal full-screen shader. The trick for a full-bleed quad is a single oversized triangle (three vertices covering the clip-space square) rather than two triangles — fewer vertices, no seam.

```js
import { Renderer, Geometry, Program, Mesh } from 'ogl';

const renderer = new Renderer({ width: innerWidth, height: innerHeight });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

// Oversized triangle: covers the whole clip-space square in 3 vertices.
const geometry = new Geometry(gl, {
  position: { size: 2, data: new Float32Array([-1, -1, 3, -1, -1, 3]) },
  uv:       { size: 2, data: new Float32Array([0, 0, 2, 0, 0, 2]) },
});

const program = new Program(gl, {
  vertex: /* glsl */ `
    attribute vec2 position;
    attribute vec2 uv;
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `,
  fragment: /* glsl */ `
    precision highp float;
    uniform float uTime;
    varying vec2 vUv;
    void main() {
      vec3 col = 0.5 + 0.5 * cos(uTime + vUv.xyx + vec3(0.0, 2.0, 4.0));
      gl_FragColor = vec4(col, 1.0);
    }
  `,
  uniforms: { uTime: { value: 0 } },
});

const mesh = new Mesh(gl, { geometry, program });

requestAnimationFrame(function loop(t) {
  requestAnimationFrame(loop);
  program.uniforms.uTime.value = t * 0.001;
  renderer.render({ scene: mesh });
});
```

Note `renderer.render({ scene })` takes a `camera` too, but a full-screen quad ignores it — the vertex shader writes clip space directly.

## Core objects

You will use a small subset of the API for image-effect work:

- `Renderer({ width, height, dpr, alpha, ... })` — owns the WebGL2 context. Read the context from `renderer.gl` and the canvas from `renderer.gl.canvas`. Resize with `renderer.setSize(w, h)`.
- `Geometry(gl, attributes)` — vertex buffers. Each attribute is `{ size, data: Float32Array }`. For full-screen work, the `Triangle` and `Plane` extras save you writing the vertices.
- `Program(gl, { vertex, fragment, uniforms })` — the shader pair plus uniforms. Each uniform is `{ value }`; mutate `program.uniforms.uName.value` at runtime.
- `Mesh(gl, { geometry, program })` — binds geometry to a program so the renderer can draw it.
- `Texture(gl, { image, flipY, generateMipmaps, ... })` — an image on the GPU. See Recipe 4 for correct loading.
- `Transform` / `Camera` — a scene-graph node and a camera, for when you move beyond a single flat quad.
- `Vec2`, `Vec3`, `Mat4` — the math types; `Vec2` is handy for mouse and resolution uniforms.

`Triangle` and `Plane` (from the extras bundle) are prebuilt geometries. `Triangle(gl)` is exactly the oversized full-screen triangle from Quick Start:

```js
import { Triangle } from 'ogl';
const geometry = new Triangle(gl); // provides `position` and `uv`, no manual arrays
```

## Recipe 1 — Full-screen animated gradient / noise hero

A living background: value noise scrolled over time, remapped into a two-color gradient. Drop the canvas behind your hero content with `position: fixed; inset: 0; z-index: -1`.

```js
import { Renderer, Triangle, Program, Mesh, Vec2 } from 'ogl';

const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

const program = new Program(gl, {
  vertex: /* glsl */ `
    attribute vec2 position;
    attribute vec2 uv;
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `,
  fragment: /* glsl */ `
    precision highp float;
    uniform float uTime;
    uniform vec2 uResolution;
    uniform vec3 uColorA;
    uniform vec3 uColorB;
    varying vec2 vUv;

    // Cheap 2D value noise.
    float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float noise(vec2 p) {
      vec2 i = floor(p), f = fract(p);
      vec2 u = f * f * (3.0 - 2.0 * f);
      return mix(
        mix(hash(i + vec2(0.0, 0.0)), hash(i + vec2(1.0, 0.0)), u.x),
        mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);
    }

    void main() {
      vec2 aspect = vec2(uResolution.x / uResolution.y, 1.0);
      vec2 p = vUv * aspect * 3.0;
      float n = noise(p + uTime * 0.15);
      n += 0.5 * noise(p * 2.0 - uTime * 0.1);
      vec3 col = mix(uColorA, uColorB, smoothstep(0.2, 1.0, n));
      gl_FragColor = vec4(col, 1.0);
    }
  `,
  uniforms: {
    uTime: { value: 0 },
    uResolution: { value: new Vec2(innerWidth, innerHeight) },
    uColorA: { value: [0.05, 0.05, 0.1] },
    uColorB: { value: [0.5, 0.3, 0.9] },
  },
});

const mesh = new Mesh(gl, { geometry: new Triangle(gl), program });

function resize() {
  renderer.setSize(innerWidth, innerHeight);
  program.uniforms.uResolution.value.set(innerWidth, innerHeight);
}
addEventListener('resize', resize);
resize();

requestAnimationFrame(function loop(t) {
  requestAnimationFrame(loop);
  program.uniforms.uTime.value = t * 0.001;
  renderer.render({ scene: mesh });
});
```

## Recipe 2 — Image hover distortion (displacement + mouse + RGB split)

The signature studio effect. A displacement texture warps the image UVs, the amount driven by a smoothed mouse position, and the three color channels are sampled at slightly offset UVs for a chromatic-aberration edge.

Provide two images: your photo, and a grayscale displacement map (clouds, ridged noise, a liquid render — anything smooth). Both go into `Texture`.

```js
import { Renderer, Triangle, Program, Mesh, Texture, Vec2 } from 'ogl';

const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
const gl = renderer.gl;
const canvas = gl.canvas;
document.querySelector('.hero').appendChild(canvas);

function loadTexture(src) {
  const texture = new Texture(gl);
  const img = new Image();
  img.crossOrigin = 'anonymous';
  img.onload = () => (texture.image = img); // flipY defaults true for TEXTURE_2D
  img.src = src;
  return texture;
}

const program = new Program(gl, {
  vertex: /* glsl */ `
    attribute vec2 position;
    attribute vec2 uv;
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `,
  fragment: /* glsl */ `
    precision highp float;
    uniform sampler2D tImage;
    uniform sampler2D tDisp;
    uniform float uHover;   // 0 at rest, 1 on hover
    uniform vec2 uMouse;    // 0..1 smoothed pointer
    varying vec2 vUv;

    void main() {
      float disp = texture2D(tDisp, vUv).r;
      // Push UVs toward the cursor, scaled by displacement and hover amount.
      vec2 dir = (uMouse - vUv);
      vec2 offset = dir * disp * uHover * 0.25;

      // Sample each channel at a widening offset -> RGB split on the edges.
      float split = disp * uHover * 0.02;
      float r = texture2D(tImage, vUv + offset + split).r;
      float g = texture2D(tImage, vUv + offset).g;
      float b = texture2D(tImage, vUv + offset - split).b;
      gl_FragColor = vec4(r, g, b, 1.0);
    }
  `,
  uniforms: {
    tImage: { value: loadTexture('/hero.jpg') },
    tDisp:  { value: loadTexture('/displacement.jpg') },
    uHover: { value: 0 },
    uMouse: { value: new Vec2(0.5, 0.5) },
  },
});

const mesh = new Mesh(gl, { geometry: new Triangle(gl), program });

const target = new Vec2(0.5, 0.5);   // raw pointer
let hoverTarget = 0;

canvas.addEventListener('pointermove', (e) => {
  const r = canvas.getBoundingClientRect();
  target.set((e.clientX - r.left) / r.width, 1 - (e.clientY - r.top) / r.height);
});
canvas.addEventListener('pointerenter', () => (hoverTarget = 1));
canvas.addEventListener('pointerleave', () => (hoverTarget = 0));

function resize() {
  const r = canvas.parentElement.getBoundingClientRect();
  renderer.setSize(r.width, r.height);
}
addEventListener('resize', resize);
resize();

requestAnimationFrame(function loop() {
  requestAnimationFrame(loop);
  const u = program.uniforms;
  // Smooth (lerp) the mouse and hover so the distortion eases instead of snapping.
  u.uMouse.value.x += (target.x - u.uMouse.value.x) * 0.08;
  u.uMouse.value.y += (target.y - u.uMouse.value.y) * 0.08;
  u.uHover.value += (hoverTarget - u.uHover.value) * 0.08;
  renderer.render({ scene: mesh });
});
```

The lerp (`* 0.08`) is what makes it feel expensive — an instant uniform update reads as cheap. Tune the `0.25` push and `0.02` split to taste.

## Recipe 3 — Render-target post FX

Render your scene into an offscreen framebuffer, then run a shader over that texture. The extras bundle ships a `Post` helper that manages ping-pong render targets for you — use it unless you need manual control.

```js
import { Renderer, Camera, Transform, Box, Program, Mesh, Post } from 'ogl';

const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

const camera = new Camera(gl, { fov: 35 });
camera.position.set(0, 0, 5);
const scene = new Transform();
const cube = new Mesh(gl, {
  geometry: new Box(gl),
  program: new Program(gl, { vertex: sceneVert, fragment: sceneFrag }),
});
cube.setParent(scene);

const post = new Post(gl);

// Each pass is a fragment shader over the previous result, bound as `tMap`.
post.addPass({
  fragment: /* glsl */ `
    precision highp float;
    uniform sampler2D tMap;
    uniform float uTime;
    varying vec2 vUv;
    void main() {
      // Wobble the whole frame + slight vignette.
      vec2 uv = vUv + 0.003 * vec2(sin(uv.y * 40.0 + uTime), cos(uv.x * 40.0 + uTime));
      vec3 col = texture2D(tMap, uv).rgb;
      col *= smoothstep(1.1, 0.4, distance(vUv, vec2(0.5)));
      gl_FragColor = vec4(col, 1.0);
    }
  `,
  uniforms: { uTime: { value: 0 } },
});

function resize() {
  renderer.setSize(innerWidth, innerHeight);
  post.resize();
  camera.perspective({ aspect: gl.canvas.width / gl.canvas.height });
}
addEventListener('resize', resize);
resize();

requestAnimationFrame(function loop(t) {
  requestAnimationFrame(loop);
  cube.rotation.y += 0.01;
  post.passes[0].uniforms.uTime.value = t * 0.001;
  // post.render renders the scene to a target, then runs the passes to screen.
  post.render({ scene, camera });
});
```

`addPass` accepts `{ vertex, fragment, uniforms, textureUniform = 'tMap', enabled }` and returns the pass object (`{ mesh, program, uniforms, enabled, ... }`). Toggle a pass at runtime with `pass.enabled = false`. For manual control instead of `Post`, render into a `RenderTarget` and read its output texture — see [references/render-targets.md](references/render-targets.md).

## Recipe 4 — Loading an image texture correctly

```js
import { Texture } from 'ogl';

const texture = new Texture(gl, {
  generateMipmaps: true, // fine for power-of-two images on WebGL2
});

const img = new Image();
img.crossOrigin = 'anonymous';        // required for any cross-origin image
img.onload = () => (texture.image = img);
img.src = '/photo.jpg';
```

Two orientation and color facts worth knowing:

- **flipY** defaults to `true` for a 2D texture, which matches how HTML images are laid out top-down. If your image samples upside-down, you set `flipY` somewhere by hand — remove that, do not flip the UVs to compensate.
- OGL does **no automatic color management**. An image loads as raw sRGB bytes and your shader samples those bytes directly, so colors look correct for straightforward display. Only if you start doing lighting math do you need to linearize (`pow(color, vec3(2.2))`) and convert back.
- `texture.image = img` is deferred: the upload to the GPU happens on the next `renderer.render`, when the texture's `update()` runs. You do not await it.

For non-power-of-two images (most photos) the defaults are safe on WebGL2, where NPOT textures support mipmaps and the default `CLAMP_TO_EDGE` wrap. If you ever see a black texture, set `generateMipmaps: false`.

## Resize and devicePixelRatio

Two things must move together on resize: the drawing buffer (`renderer.setSize`) and any resolution uniform your shader reads. Cap `dpr` at 2 — retina phones report 3 or 4 and you rarely see the difference past 2, but you pay for every extra pixel.

```js
const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
function resize() {
  renderer.setSize(innerWidth, innerHeight);       // sets canvas.width = w * dpr internally
  program.uniforms.uResolution?.value.set(innerWidth, innerHeight);
}
addEventListener('resize', resize);
resize();
```

`renderer.setSize` takes CSS pixels and multiplies by `dpr` for the backing buffer, so pass logical sizes, not `* dpr` values.

## RAF loop and strict cleanup

A WebGL context is a heavy, finite resource — browsers cap how many can exist at once. A single-page app that mounts and unmounts effects will leak contexts and eventually kill the whole page unless you tear down completely.

```js
let raf;
function start() {
  raf = requestAnimationFrame(function loop(t) {
    raf = requestAnimationFrame(loop);
    program.uniforms.uTime.value = t * 0.001;
    renderer.render({ scene: mesh });
  });
}
function destroy() {
  cancelAnimationFrame(raf);                 // 1. stop the loop
  removeEventListener('resize', resize);     // 2. drop listeners
  gl.getExtension('WEBGL_lose_context')?.loseContext(); // 3. free the GPU context
  gl.canvas.remove();                        // 4. detach the canvas node
}
```

The order matters: stop the loop before you lose the context, or a queued frame renders into a dead context and throws.

## React / Next mount and cleanup

Own the whole lifecycle inside one `useEffect`. Create the renderer against a ref'd container, and return the teardown so React runs it on unmount. In Next.js this must be a client component (`'use client'`) because it touches `window` and the DOM.

```jsx
'use client';
import { useEffect, useRef } from 'react';
import { Renderer, Triangle, Program, Mesh } from 'ogl';

export default function ShaderHero() {
  const ref = useRef(null);

  useEffect(() => {
    const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
    const gl = renderer.gl;
    ref.current.appendChild(gl.canvas);

    const program = new Program(gl, { vertex, fragment, uniforms: { uTime: { value: 0 } } });
    const mesh = new Mesh(gl, { geometry: new Triangle(gl), program });

    const resize = () => {
      const { clientWidth: w, clientHeight: h } = ref.current;
      renderer.setSize(w, h);
    };
    addEventListener('resize', resize);
    resize();

    let raf;
    const loop = (t) => {
      raf = requestAnimationFrame(loop);
      program.uniforms.uTime.value = t * 0.001;
      renderer.render({ scene: mesh });
    };
    raf = requestAnimationFrame(loop);

    return () => {
      cancelAnimationFrame(raf);
      removeEventListener('resize', resize);
      gl.getExtension('WEBGL_lose_context')?.loseContext();
      gl.canvas.remove();
    };
  }, []);

  return <div ref={ref} style={{ position: 'fixed', inset: 0, zIndex: -1 }} />;
}
```

Under React 18 Strict Mode in dev, effects run twice on mount — the cleanup above makes that safe (the first context is lost and detached before the second is created).

## Performance

- Cap `dpr` at 2. This is the single biggest lever; fragment cost scales with pixel count.
- Keep the fragment shader lean — it runs once per pixel per frame. Move constant math to the vertex shader or to JS uniforms.
- Pause the loop when the canvas is offscreen. An `IntersectionObserver` that stops `requestAnimationFrame` when the hero scrolls away saves the whole GPU cost for free.
- Prefer one oversized `Triangle` over a two-triangle `Plane` for full-screen passes: fewer vertices and no diagonal seam where the two triangles meet.
- Reuse geometries and programs across meshes instead of recreating them.

## Accessibility — prefers-reduced-motion

Users who set reduced-motion should get a still image, not a frozen-then-animating surprise. Render exactly one frame and never start the loop.

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduce) {
  renderer.render({ scene: mesh }); // one static frame, no RAF
} else {
  requestAnimationFrame(loop);
}
```

For the distortion hero, also skip binding the pointer listeners under reduced motion so hover does nothing. A static first frame still needs its textures loaded, so render once inside the image's `onload`, not immediately.

## Pitfalls

- **Leaked contexts.** Not calling `loseContext()` on unmount is the top cause of a page that dies after navigating between a few effect-heavy routes. Always run the four-step teardown.
- **Resolution uniform out of sync.** Resizing the renderer but not updating `uResolution` warps the aspect ratio. Update both in the same `resize` handler.
- **Passing `* dpr` sizes to `setSize`.** `setSize` already multiplies by `dpr`; pass CSS pixels.
- **Awaiting textures.** `texture.image = img` uploads on the next render, not immediately — there is nothing to await. Just assign it in `onload`.
- **Cross-origin images.** Without `img.crossOrigin = 'anonymous'` (and CORS headers on the host), the texture taints the context and reads fail. Same-origin images are fine.
- **Fighting flipY with flipped UVs.** If an image is upside down, fix the `flipY` option, not the UVs — flipping UVs breaks the moment you swap the image source.
- **Recreating programs every frame.** Build `Program` and `Geometry` once outside the loop; only mutate `.value` on uniforms inside it.

## References

- OGL repository and README: https://github.com/oframe/ogl
- OGL examples (Triangle Screen Shader, Textures, Render to texture, Post FXAA, Post Bloom, Mouse Flowmap, Post Fluid Distortion): https://oframe.github.io/ogl/examples
- Manual render-target control (without the `Post` helper): [references/render-targets.md](references/render-targets.md)
