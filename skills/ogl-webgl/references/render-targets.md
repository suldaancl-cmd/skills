# Manual render targets in OGL

The `Post` helper (Recipe 3 in SKILL.md) covers most post-processing. Drop to a raw `RenderTarget` when you need control `Post` does not give you: multiple inputs to one pass, feedback loops (ping-pong buffers that read last frame), or rendering a scene into a texture you then map onto other geometry.

## Rendering a scene into a texture

Pass a `target` to `renderer.render` and it draws into that framebuffer instead of the screen. The result lives on `renderTarget.texture`.

```js
import { Renderer, Camera, Transform, Box, Program, Mesh, RenderTarget, Triangle } from 'ogl';

const renderer = new Renderer({ dpr: Math.min(devicePixelRatio, 2) });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

// Offscreen buffer. Defaults: width/height = canvas size, RGBA, depth on.
const target = new RenderTarget(gl, {
  width: gl.canvas.width,
  height: gl.canvas.height,
});

// A normal 3D scene we will capture.
const camera = new Camera(gl, { fov: 35 });
camera.position.set(0, 0, 5);
const scene = new Transform();
const cube = new Mesh(gl, {
  geometry: new Box(gl),
  program: new Program(gl, { vertex: sceneVert, fragment: sceneFrag }),
});
cube.setParent(scene);

// A full-screen pass that reads the captured texture as tMap.
const screen = new Mesh(gl, {
  geometry: new Triangle(gl),
  program: new Program(gl, {
    vertex: /* glsl */ `
      attribute vec2 position;
      attribute vec2 uv;
      varying vec2 vUv;
      void main() { vUv = uv; gl_Position = vec4(position, 0.0, 1.0); }
    `,
    fragment: /* glsl */ `
      precision highp float;
      uniform sampler2D tMap;
      varying vec2 vUv;
      void main() {
        vec3 col = texture2D(tMap, vUv).rgb;
        col = 1.0 - col;            // invert, as a stand-in effect
        gl_FragColor = vec4(col, 1.0);
      }
    `,
    uniforms: { tMap: { value: target.texture } },
  }),
});

function resize() {
  renderer.setSize(innerWidth, innerHeight);
  target.setSize?.(gl.canvas.width, gl.canvas.height);
  camera.perspective({ aspect: gl.canvas.width / gl.canvas.height });
}
addEventListener('resize', resize);
resize();

requestAnimationFrame(function loop() {
  requestAnimationFrame(loop);
  cube.rotation.y += 0.01;

  // Pass 1: render the 3D scene into the offscreen target.
  renderer.render({ scene, camera, target });

  // Pass 2: render the full-screen mesh to the screen (target = null default).
  renderer.render({ scene: screen });
});
```

The two-pass structure is the whole idea: draw into `target`, then draw a quad that samples `target.texture`.

## Ping-pong for feedback effects

Effects that read the previous frame (trails, flowmaps, reaction-diffusion) need two targets you swap each frame — you cannot read and write the same texture in one pass.

```js
let read = new RenderTarget(gl);
let write = new RenderTarget(gl);

function frame() {
  program.uniforms.tPrev.value = read.texture; // sample last frame
  renderer.render({ scene: sim, target: write }); // write this frame
  [read, write] = [write, read];                  // swap

  screen.program.uniforms.tMap.value = read.texture;
  renderer.render({ scene: screen });             // show it
}
```

The Mouse Flowmap and Post Fluid Distortion examples on the OGL site are built on this pattern — study them before writing your own fluid sim.

## RenderTarget options worth knowing

The constructor is `new RenderTarget(gl, { ... })` with these defaults:

- `width`, `height` — default to the canvas size.
- `color` — number of color attachments, default 1. Access extras via `target.textures[i]`; `target.texture` aliases `textures[0]`.
- `depth` — depth buffer, default `true`. Turn off for pure 2D image passes to save memory.
- `stencil` — default `false`.
- `depthTexture` — default `false`; enable to sample depth in a shader.
- `wrapS` / `wrapT` — default `CLAMP_TO_EDGE`.
- `minFilter` / `magFilter` — default `LINEAR`.
- `type`, `format`, `internalFormat` — default `UNSIGNED_BYTE` / `RGBA`. For HDR / float accumulation you raise `type` to a float type, which needs the matching WebGL2 extension enabled on the context.

## References

- RenderTarget source: https://github.com/oframe/ogl/blob/master/src/core/RenderTarget.js
- Post source: https://github.com/oframe/ogl/blob/master/src/extras/Post.js
- Mouse Flowmap and Post examples: https://oframe.github.io/ogl/examples
