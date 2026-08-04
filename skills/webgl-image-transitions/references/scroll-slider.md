# Scroll-scrubbed slider, section crossfade, and image-trail

Extends the Quick Start / Recipe host in SKILL.md. All code original.

## Scroll-scrubbed slider (Lenis drives progress)

Instead of playing on a click, tie `uProgress` to normalized scroll so the
transition scrubs both ways. Lenis gives a smoothed scroll value; feed it in.

```bash
npm i lenis ogl
```

```js
import Lenis from 'lenis';

const lenis = new Lenis({ smoothWheel: true });
requestAnimationFrame(function raf(t) { lenis.raf(t); requestAnimationFrame(raf); });

// N slides means N-1 transitions across the scrollable height
const slides = ['/img/a.jpg', '/img/b.jpg', '/img/c.jpg'];
const textures = slides.map(loadTexture);        // loadTexture from SKILL.md
const segments = slides.length - 1;

lenis.on('scroll', ({ scroll, limit }) => {
  const p = limit > 0 ? scroll / limit : 0;      // 0..1 over the page
  const pos = p * segments;                       // e.g. 1.4 = between slide 1 and 2
  const i = Math.min(Math.floor(pos), segments - 1);
  const local = pos - i;                          // 0..1 within this segment

  program.uniforms.uFrom.value = textures[i];
  program.uniforms.uTo.value   = textures[i + 1];
  program.uniforms.uProgress.value = local;       // scrub, no tween
});
```

Render on scroll only (plus a first paint) rather than a permanent RAF loop, so
an idle page costs nothing:

```js
let dirty = true;
lenis.on('scroll', () => { dirty = true; });
requestAnimationFrame(function loop() {
  if (dirty) { renderer.render({ scene: mesh }); dirty = false; }
  requestAnimationFrame(loop);
});
```

## Scroll-linked crossfade between sections

Tie `progress` to how far a pinned section has entered the viewport. Works with
an `IntersectionObserver` for the enter/exit gate plus scroll for the ratio.

```js
const section = document.querySelector('#hero');

function onScroll() {
  const r = section.getBoundingClientRect();
  const vh = innerHeight;
  // 0 when the section top hits the bottom of the screen, 1 when it has scrolled one screen up
  const p = Math.min(Math.max((vh - r.top) / (vh + r.height), 0), 1);
  program.uniforms.uProgress.value = p;
  dirty = true;
}
addEventListener('scroll', onScroll, { passive: true });
```

## Full pointer image-trail (ring buffer)

Recipe 4 in SKILL.md distorts a single plane by velocity. A true trail stamps a
decaying copy of the image at each recent pointer position. Keep a fixed ring of
sprites, advance a head index per move, and fade each slot every frame.

```js
const TRAIL = 8;
const trail = Array.from({ length: TRAIL }, () => ({ x: 0, y: 0, alpha: 0 }));
let head = 0;

canvas.addEventListener('pointermove', (e) => {
  const rect = canvas.getBoundingClientRect();
  head = (head + 1) % TRAIL;
  trail[head].x = (e.clientX - rect.left) / rect.width;
  trail[head].y = (e.clientY - rect.top) / rect.height;
  trail[head].alpha = 1;                           // fresh stamp
});

function drawTrail() {
  for (const slot of trail) {
    slot.alpha *= 0.9;                             // decay
    if (slot.alpha < 0.01) continue;
    // set per-sprite uniforms and render one draw call per slot:
    // program.uniforms.uCenter.value = [slot.x, slot.y];
    // program.uniforms.uAlpha.value  = slot.alpha;
    // renderer.render({ scene: sprite });
  }
  requestAnimationFrame(drawTrail);
}
drawTrail();
```

Render sprites additively over a transparent canvas, or into a single render
target you composite once, to keep draw calls bounded. Cap `TRAIL` lower on
mobile and pause the loop when the pointer has been still (all alphas near zero).
