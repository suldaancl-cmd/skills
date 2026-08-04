---
name: webgl-image-transitions
description: >-
  Build the award-studio displacement / RGB-split image-to-image transition and
  WebGL slider — the signature effect from Exo Ape, Unseen, Locomotive, and
  funkhaus. Fire this whenever the ask involves a WebGL image transition,
  displacement map / dispersion / RGB-split / distortion crossfade, an animated
  image slider or carousel, hover image-trail, scroll-scrubbed gallery, or
  gl-transitions (glsl transitions) shaders driven by GSAP/Lenis in OGL, Three.js,
  or curtains.js — including any immersive / cinematic / awwwards / scroll / 3D
  context where two images morph into each other. Not for plain CSS crossfades.
---

# WebGL image transitions — the studio signature slider

The recurring high-end effect is one shader: two textures, a `progress` uniform
from 0 to 1, and a grayscale displacement map that warps the pixels as they
crossfade. Add a per-channel offset (RGB split) that peaks mid-transition and you
have the "dispersion" look every award studio ships. Everything else in this
skill is a variation on that one idea: change the warp function (wave, curl,
slices, zoom-blur) or change what drives `progress` (a click, scroll position,
or mouse velocity).

Keep the real `<img>` in the DOM and paint the WebGL canvas on top. That way the
page is crawlable, works with motion reduced, and degrades to a plain crossfade
when WebGL is unavailable. This is the accessibility spine of the whole
technique, not an afterthought.

## The technique family

- **Displacement transition** — warp both images along a displacement texture while crossfading. The base effect.
- **RGB split / dispersion** — offset R and B channels; strongest mid-transition. Layers on top of any warp.
- **Wave / ripple** — displacement driven by a `sin` field instead of a texture.
- **Curl** — rotate the sample point around a center as progress advances.
- **Slices** — quantize UVs into bands that slide at staggered offsets.
- **Zoom-blur** — sample along the vector toward center, accumulate, for a punch-in dissolve.

Wave, curl, slices, and zoom-blur GLSL live in `references/shader-variants.md`.

## Core contract (gl-transitions compatible)

The [gl-transitions](https://github.com/gl-transitions/gl-transitions) collection
is the reference format, and matching it means any of its shaders drop straight
into your renderer. A transition is a GLSL function:

```glsl
vec4 transition(vec2 uv);
```

Inside it you get three contextual variables and two functions, supplied by the
host program:

- `progress` (float) — moves 0.0 to 1.0 over the transition.
- `ratio` (float) — viewport aspect, `width / height`.
- `uv` (vec2) — the pixel coordinate.
- `getFromColor(vec2 uv)` — samples the outgoing image.
- `getToColor(vec2 uv)` — samples the incoming image.

At `progress == 0.0` only the `from` image shows; at `1.0` only `to`. Parameters
are plain uniforms with a comment default, e.g. `uniform float intensity; // = 0.6`.
Provide those five names and you can paste any gl-transitions shader body
verbatim (Recipe 2).

## Quick start (OGL)

OGL is the smallest renderer that does this well. Install it, mount a fullscreen
triangle, and drive one uniform with GSAP.

```bash
npm i ogl gsap
```

```js
import { Renderer, Program, Mesh, Triangle, Texture } from 'ogl';
import gsap from 'gsap';

const canvas = document.querySelector('#gl');
const renderer = new Renderer({ canvas, dpr: Math.min(devicePixelRatio, 2) });
const gl = renderer.gl;

function fit() {
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
}
addEventListener('resize', fit);
fit();

// grayscale displacement map (clouds/ridged noise works well)
function loadTexture(src) {
  const texture = new Texture(gl);
  const img = new Image();
  img.crossOrigin = 'anonymous';
  img.onload = () => (texture.image = img);
  img.src = src;
  return texture;
}

const uFrom = loadTexture('/img/a.jpg');
const uTo   = loadTexture('/img/b.jpg');
const uDisp = loadTexture('/img/disp.jpg');

const vertex = /* glsl */ `
  attribute vec2 uv;
  attribute vec2 position;
  varying vec2 vUv;
  void main() { vUv = uv; gl_Position = vec4(position, 0.0, 1.0); }
`;

const fragment = /* glsl */ `
  precision highp float;
  uniform sampler2D uFrom, uTo, uDisp;
  uniform float uProgress, uStrength;
  varying vec2 vUv;

  void main() {
    float d = texture2D(uDisp, vUv).r;
    // push the two images opposite ways along the displacement
    vec2 fromUv = vUv + vec2(d * uProgress * uStrength, 0.0);
    vec2 toUv   = vUv - vec2(d * (1.0 - uProgress) * uStrength, 0.0);

    // RGB split peaks at progress = 0.5, zero at both ends
    float split = uStrength * sin(uProgress * 3.14159265) * 0.04;
    vec4 fromC = vec4(
      texture2D(uFrom, fromUv + vec2(split, 0.0)).r,
      texture2D(uFrom, fromUv).g,
      texture2D(uFrom, fromUv - vec2(split, 0.0)).b, 1.0);
    vec4 toC = vec4(
      texture2D(uTo, toUv + vec2(split, 0.0)).r,
      texture2D(uTo, toUv).g,
      texture2D(uTo, toUv - vec2(split, 0.0)).b, 1.0);

    gl_FragColor = mix(fromC, toC, uProgress);
  }
`;

const program = new Program(gl, {
  vertex, fragment,
  uniforms: {
    uFrom: { value: uFrom }, uTo: { value: uTo }, uDisp: { value: uDisp },
    uProgress: { value: 0 }, uStrength: { value: 0.6 },
  },
});

const mesh = new Mesh(gl, { geometry: new Triangle(gl), program });

renderer.render({ scene: mesh });
let raf = requestAnimationFrame(function loop() {
  renderer.render({ scene: mesh });
  raf = requestAnimationFrame(loop);
});

// trigger the transition
document.querySelector('#next').addEventListener('click', () => {
  gsap.fromTo(program.uniforms.uProgress,
    { value: 0 }, { value: 1, duration: 1.2, ease: 'power2.inOut' });
});
```

To go from A to B to C, swap `uFrom.value = uTo.value; uTo.value = loadTexture(next)`
and reset `uProgress` to 0 before the next tween.

## Recipe 1: Cover-fit UVs (do this before shipping)

Images are rarely the canvas aspect. Without correction the picture stretches.
Compute a scale from image aspect vs. plane aspect and remap `uv` so the texture
behaves like CSS `object-fit: cover`.

```glsl
// pass uImageSize (px) and uPlaneSize (px) as uniform vec2
vec2 coverUv(vec2 uv, vec2 image, vec2 plane) {
  vec2 s = plane / image;                 // scale each axis to fill
  float scale = max(s.x, s.y);            // cover = the larger scale
  vec2 size = image * scale;              // rendered size in px
  vec2 offset = (plane - size) * 0.5 / size; // center it
  return uv * (plane / size) - offset;
}
// in main(): vec2 uv = coverUv(vUv, uImageSize, uPlaneSize);
```

Sample `getFromColor`/`getToColor` (or `texture2D`) with the corrected `uv`, not
the raw `vUv`. Update `uPlaneSize` on resize; set `uImageSize` per texture once
the image loads.

## Recipe 2: Drop in a gl-transitions shader

Because the host program below defines the five contextual names, you can paste
any transition body from the gl-transitions collection between the markers. The
sample transition here is original — replace it with the `.glsl` you want.

```glsl
precision highp float;
uniform sampler2D uFrom, uTo;
uniform float progress;   // gl-transitions reads `progress`
uniform float ratio;      // width / height

varying vec2 vUv;

vec4 getFromColor(vec2 uv) { return texture2D(uFrom, uv); }
vec4 getToColor(vec2 uv)   { return texture2D(uTo, uv); }

// ---- paste a gl-transitions body below (keep its own uniforms) ----
uniform float intensity; // = 0.3
vec4 transition(vec2 uv) {
  vec2 dir = uv - vec2(0.5);
  vec2 p = uv + dir * sin(progress * 3.14159) * intensity;
  return mix(getFromColor(p), getToColor(p), progress);
}
// ---- end paste ----

void main() { gl_FragColor = transition(vUv); }
```

Set `progress` and `ratio` from JS exactly as `uProgress`/uniforms in the Quick
Start. A transition object in the `gl-transitions` npm package carries `glsl`,
`name`, `author`, `defaultParams`, and `paramsTypes` — read `defaultParams` to
seed each pasted transition's uniforms.

If you prefer the official loader over hand-wrapping, the `gl-transition` runtime
package exposes `createTransition(gl, transition)`, which returns an object with
`draw(progress, from, to, width, height, params)` and `dispose()`. It wants a raw
WebGL context and its own texture wrappers, so hand-wrapping (above) is usually
the lighter path inside an existing OGL/Three scene.

## Recipe 3: Three.js mount

Same shader, Three.js host. Fullscreen plane, orthographic camera, explicit
disposal.

```js
import * as THREE from 'three';

const canvas = document.querySelector('#gl');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));

const scene = new THREE.Scene();
const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

const loader = new THREE.TextureLoader();
const uniforms = {
  uFrom: { value: loader.load('/img/a.jpg') },
  uTo:   { value: loader.load('/img/b.jpg') },
  uDisp: { value: loader.load('/img/disp.jpg') },
  uProgress: { value: 0 },
  uStrength: { value: 0.6 },
};

const material = new THREE.ShaderMaterial({
  uniforms,
  vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position, 1.0); }`,
  fragmentShader: /* paste the Quick Start fragment (uses vUv) */ FRAGMENT,
});

const quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
scene.add(quad);

function resize() {
  renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
}
addEventListener('resize', resize);
resize();

renderer.setAnimationLoop(() => renderer.render(scene, camera));

// cleanup when the component unmounts
function destroy() {
  renderer.setAnimationLoop(null);
  quad.geometry.dispose();
  material.dispose();
  Object.values(uniforms).forEach(u => u.value?.isTexture && u.value.dispose());
  renderer.dispose();
}
```

## Recipe 4: Hover image-trail (velocity to distortion)

Map pointer speed to `uStrength` and let it decay each frame, so the image
distorts only while the cursor is moving fast over it.

```js
let px = 0, py = 0, target = 0;
const el = canvas; // the WebGL surface

el.addEventListener('pointermove', (e) => {
  const dx = e.clientX - px, dy = e.clientY - py;
  px = e.clientX; py = e.clientY;
  const speed = Math.min(Math.hypot(dx, dy) / 40, 1); // normalize
  target = Math.max(target, speed);                    // spike on fast moves
});

function loop() {
  target *= 0.92;                                       // decay toward rest
  const u = program.uniforms; // OGL; for Three use `uniforms`
  u.uStrength.value += (target * 0.9 - u.uStrength.value) * 0.1; // smooth
  renderer.render({ scene: mesh });
  requestAnimationFrame(loop);
}
loop();
```

For a true multi-image trail (each pointer move stamps a decaying copy), keep a
ring buffer of recent positions and draw a sprite per slot with falling alpha;
the full pattern is in `references/scroll-slider.md`.

## Scroll-scrubbed slider and section crossfade

A WebGL carousel maps scroll position (via Lenis) to `uProgress`, so the
transition scrubs instead of playing on a timer; a section crossfade does the
same but ties `progress` to how far a section has entered the viewport. Both
patterns, including the Lenis wiring, are in `references/scroll-slider.md`.

## React / Next mount and cleanup

Create the renderer once in an effect, tear everything down on unmount, and let
React own only the trigger state. In Next, gate on the client because WebGL has
no server render.

```jsx
'use client';
import { useEffect, useRef } from 'react';

export function Transition({ from, to, disp }) {
  const canvasRef = useRef(null);
  const apiRef = useRef(null);

  useEffect(() => {
    const api = initTransition(canvasRef.current, { from, to, disp }); // your setup, returns { play, destroy }
    apiRef.current = api;
    return () => api.destroy(); // dispose textures, program, cancel RAF, remove listeners
  }, [from, to, disp]);

  return (
    <div>
      {/* real images stay in the DOM for SEO and no-JS fallback */}
      <img src={from} alt="" hidden aria-hidden="true" />
      <canvas ref={canvasRef} />
      <button onClick={() => apiRef.current?.play()}>Next</button>
    </div>
  );
}
```

Guard React Strict Mode's double-invoke by making `destroy()` idempotent, and
never recreate the renderer on every render — only inside the effect.

## Performance

- **Cap texture size.** Downscale source images to the largest size they display at (often <= 2048 px). Oversized textures are the top cause of jank and memory spikes.
- **Reuse one program.** Compile the shader once and swap the `uFrom`/`uTo` texture references between slides rather than rebuilding materials.
- **Clamp DPR** to `Math.min(devicePixelRatio, 2)`; retina at 3x quadruples fragment work for no visible gain.
- **Pause when offscreen.** Stop the RAF loop with an `IntersectionObserver` or `document.hidden` check so an idle slider costs nothing.
- **Only render when animating.** If `progress` isn't tweening and nothing else moves, skip the frame; render on demand instead of a permanent loop.
- **Dispose on unmount.** Every texture, geometry, program, and the renderer itself leak GPU memory if not released between route changes.

## Accessibility

- **Keep the real `<img>` in the DOM.** The WebGL canvas is decorative; the image element carries the `alt` text, feeds SEO, and is what shows if WebGL fails.
- **Honor `prefers-reduced-motion`.** When reduced, skip the shader entirely and cross-fade with CSS `opacity`, or jump-cut. Detect once and never build the GPU pipeline for those users.

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduce) {
  mountPlainCrossfade(); // opacity transition on the <img> elements
} else {
  mountWebglTransition();
}
```

- **Keyboard and focus.** Slider controls must be real `<button>`s reachable by tab, with visible focus and `aria-label`s; the effect is progressive enhancement over working controls.
- **Provide a still fallback** for `WebGLRenderingContext` being null (blocked/old GPU): show the current image and wire buttons to a plain swap.

## Pitfalls

- **Black or flipped textures.** WebGL samples with the Y axis inverted from HTML images. Flip on upload (OGL `Texture({ flipY: true })`, Three sets `flipY` true by default) or `1.0 - uv.y` in the shader — pick one, not both.
- **CORS taint.** Cross-origin images without `crossOrigin = 'anonymous'` (and a permissive server) silently fail to upload. Set it before `img.src`.
- **NPOT wrap warnings.** Non-power-of-two textures can't use `REPEAT` wrapping or mipmaps in WebGL1; use `CLAMP_TO_EDGE` and `LINEAR`, or resize to a power of two.
- **Stretched images.** Not applying cover-fit UVs (Recipe 1) stretches every non-square image; correct per texture and on resize.
- **Transition never completes visually.** If `mix` uses a warped `progress` but the final frame still samples the `from` image, the last pixels look wrong — ensure at `progress == 1.0` the math resolves to exactly `getToColor`.
- **Leak on route change.** Forgetting `dispose()` in SPA navigation grows GPU memory until the tab crashes; always tear down in cleanup.
- **Displacement too strong.** `uStrength` above ~1.0 tears the image into unreadable smears; the tasteful range is roughly 0.3 to 0.8.

## References

- gl-transitions collection and authoring spec: https://github.com/gl-transitions/gl-transitions
- gl-transitions gallery: https://gl-transitions.com/
- `gl-transition` runtime package (createTransition / draw / dispose): https://www.npmjs.com/package/gl-transition
- OGL: https://github.com/oframe/ogl
- Three.js ShaderMaterial: https://threejs.org/docs/#api/en/materials/ShaderMaterial
- Scroll slider, section crossfade, full image-trail: `references/scroll-slider.md`
- Wave, curl, slices, zoom-blur GLSL: `references/shader-variants.md`
