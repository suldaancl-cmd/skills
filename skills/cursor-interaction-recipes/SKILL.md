---
name: cursor-interaction-recipes
description: Use when building premium pointer interactions — custom cursor, magnetic buttons, image-trail, hover distortion, or cursor state changes on a marketing/portfolio site. Copy-paste vanilla-JS recipes (with React/GSAP variants) covering lerp cursor followers, mix-blend-mode invert cursors, magnetic CTAs with elastic release, fading image trails that prune DOM nodes, and data-attribute cursor states. Always ships the mandatory guards: disabled on touch (pointer:coarse / hover:none), respects prefers-reduced-motion, and never traps keyboard users.
---

# Cursor Interaction Recipes

Premium pointer interactions, 2026-current. Every recipe is a working vanilla-JS snippet with a brief React/GSAP note. **Read GUARDS first — they are mandatory, not optional.** A custom cursor that fires on a phone or ignores `prefers-reduced-motion` is a bug, not a flourish.

Sources: [Codrops — Custom Cursor Effects](https://tympanus.net/codrops/2019/01/31/custom-cursor-effects/), [Codrops — Image Trail Effects](https://tympanus.net/codrops/2019/08/07/image-trail-effects/), [GSAP `quickTo` custom cursor](https://codepen.io/GreenSock/pen/dyjywaZ), [Olivier Larose — Magnetic Buttons](https://blog.olivierlarose.com/tutorials/magnetic-button).

---

## 0. GUARDS (mandatory — gate every recipe behind this)

Run this once. If `cursorFxAllowed()` returns `false`, do not initialise any recipe below — the native cursor stays, the site stays usable.

```js
function cursorFxAllowed() {
  // Touch / no-hover devices: a follower cursor is invisible or laggy noise.
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  // Vestibular safety: honour the OS "reduce motion" switch.
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  return finePointer && !reduceMotion;
}

function enableCursorFx(init) {
  if (!cursorFxAllowed()) return false;
  init();
  // Re-evaluate if the user plugs in a mouse or flips reduce-motion live.
  window.matchMedia('(prefers-reduced-motion: reduce)')
    .addEventListener('change', e => { if (e.matches) location.reload(); });
  return true;
}
```

**Keyboard rule:** never set `cursor: none` on `:focus-visible` flows, never hijack `Tab`/`Enter`, and keep all hover affordances reachable by keyboard. A custom cursor is a *visual layer over* normal interaction — it must never *replace* it. Keep `cursor: none` scoped to `body` only when the custom cursor is active, and restore it in your reduce-motion fallback.

---

## 1. Custom cursor follower (lerp / easing)

The follower chases the mouse by adding a fraction of the remaining distance each frame (`pos += (target - pos) * ease`) inside `requestAnimationFrame`. Lower `ease` = laggier, more premium drift. Animate `transform`, never `left/top` (GPU-composited, no layout). Confirmed pattern per [Codrops](https://tympanus.net/codrops/2019/01/31/custom-cursor-effects/).

```html
<div class="cursor" aria-hidden="true"></div>
```
```css
.cursor {
  position: fixed; top: 0; left: 0; width: 24px; height: 24px;
  margin: -12px 0 0 -12px;              /* centre on the hotspot */
  border-radius: 50%; background: #fff;
  pointer-events: none; z-index: 9999; will-change: transform;
}
@media (hover: hover) and (pointer: fine) { body.has-cursor { cursor: none; } }
```
```js
enableCursorFx(() => {
  document.body.classList.add('has-cursor');
  const el = document.querySelector('.cursor');
  const mouse = { x: innerWidth / 2, y: innerHeight / 2 };
  const pos = { ...mouse };
  const ease = 0.15;                    // 0.1 slow & luxe · 0.3 snappy

  addEventListener('mousemove', e => { mouse.x = e.clientX; mouse.y = e.clientY; });

  (function raf() {
    pos.x += (mouse.x - pos.x) * ease;
    pos.y += (mouse.y - pos.y) * ease;
    el.style.transform = `translate(${pos.x}px, ${pos.y}px)`;
    requestAnimationFrame(raf);
  })();
});
```

**`mix-blend-mode: difference` variant** — the cursor inverts whatever is under it (white text → black hole, etc.). Just add to `.cursor`:
```css
.cursor { background: #fff; mix-blend-mode: difference; }
```
The element must be opaque white and sit above content for the invert to read.

**GSAP variant** — drop the RAF loop; `quickTo` does the easing and is the [official GreenSock approach](https://codepen.io/GreenSock/pen/dyjywaZ):
```js
const xTo = gsap.quickTo('.cursor', 'x', { duration: 0.3, ease: 'power3' });
const yTo = gsap.quickTo('.cursor', 'y', { duration: 0.3, ease: 'power3' });
addEventListener('mousemove', e => { xTo(e.clientX); yTo(e.clientY); });
```

**React:** put `mouse`/`pos` in `useRef`, run the RAF loop in `useEffect`, and **return a cleanup** that `cancelAnimationFrame`s and removes listeners.

---

## 2. Magnetic buttons (pull toward cursor, elastic release)

Inside the element's hover radius, translate it toward the cursor by the offset from its centre; on leave, snap home with an elastic ease. Math and easing verified against [Olivier Larose](https://blog.olivierlarose.com/tutorials/magnetic-button) (`elastic.out(1, 0.3)`).

```html
<button class="magnetic">Get started</button>
```
```js
enableCursorFx(() => {
  document.querySelectorAll('.magnetic').forEach(el => {
    const strength = 0.4;               // 0.2 subtle · 0.6 aggressive
    let raf, cur = { x: 0, y: 0 }, tgt = { x: 0, y: 0 };

    el.addEventListener('mousemove', e => {
      const r = el.getBoundingClientRect();
      tgt.x = (e.clientX - (r.left + r.width  / 2)) * strength;
      tgt.y = (e.clientY - (r.top  + r.height / 2)) * strength;
      if (!raf) loop();
    });
    el.addEventListener('mouseleave', () => { tgt.x = tgt.y = 0; });

    function loop() {
      cur.x += (tgt.x - cur.x) * 0.2;
      cur.y += (tgt.y - cur.y) * 0.2;
      el.style.transform = `translate(${cur.x}px, ${cur.y}px)`;
      raf = (Math.abs(cur.x) > 0.1 || Math.abs(cur.y) > 0.1 || tgt.x || tgt.y)
        ? requestAnimationFrame(loop) : null;
    }
  });
});
```

**GSAP variant** (real elastic bounce, the agency standard):
```js
const xTo = gsap.quickTo(el, 'x', { duration: 1, ease: 'elastic.out(1, 0.3)' });
const yTo = gsap.quickTo(el, 'y', { duration: 1, ease: 'elastic.out(1, 0.3)' });
el.addEventListener('mousemove', e => {
  const r = el.getBoundingClientRect();
  xTo((e.clientX - (r.left + r.width / 2)) * 0.4);
  yTo((e.clientY - (r.top + r.height / 2)) * 0.4);
});
el.addEventListener('mouseleave', () => { xTo(0); yTo(0); });  // elastic snap home
```
**React/Framer Motion:** `<motion.button animate={{ x, y }} transition={{ type:'spring', stiffness:150, damping:15, mass:0.1 }} />`, driving `x/y` from `onMouseMove` and resetting to `0` on `onMouseLeave`.

---

## 3. Image-trail / mouse-trail (spawn + fade, prune DOM nodes)

On mouse move (throttled by distance, not time), spawn an `<img>` at the cursor, fade+scale it out, and **remove it from the DOM on transition end** so nodes never accumulate. Concept from [Codrops Image Trail Effects](https://tympanus.net/codrops/2019/08/07/image-trail-effects/).

```css
.trail-img {
  position: fixed; width: 180px; pointer-events: none; z-index: 9990;
  transform: translate(-50%, -50%) scale(0.6); opacity: 0;
  transition: opacity .5s, transform .5s; will-change: transform, opacity;
}
.trail-img.in { opacity: 1; transform: translate(-50%, -50%) scale(1); }
```
```js
enableCursorFx(() => {
  const imgs = ['/t1.jpg', '/t2.jpg', '/t3.jpg'];
  const threshold = 100;                // px the mouse must travel to spawn the next
  let last = { x: 0, y: 0 }, i = 0;

  addEventListener('mousemove', e => {
    if (Math.hypot(e.clientX - last.x, e.clientY - last.y) < threshold) return;
    last = { x: e.clientX, y: e.clientY };

    const img = document.createElement('img');
    img.src = imgs[i++ % imgs.length];
    img.className = 'trail-img';
    img.style.left = e.clientX + 'px';
    img.style.top  = e.clientY + 'px';
    document.body.appendChild(img);

    requestAnimationFrame(() => img.classList.add('in'));   // fade in
    setTimeout(() => img.classList.remove('in'), 200);      // then fade out
    img.addEventListener('transitionend', () => {           // prune
      if (!img.classList.contains('in')) img.remove();
    });
  });
});
```
**Pruning is the load-bearing part:** without `img.remove()` the DOM grows unbounded and the page leaks memory on long sessions. For high-density trails (every few px) prefer a single `<canvas>` overlay drawing shrinking sprites — see [Codrops mouse trails with OGL](https://tympanus.net/codrops/2019/09/24/crafting-stylised-mouse-trails-with-ogl/).

**GSAP variant:** replace the CSS transition with `gsap.fromTo(img, {scale:.6, opacity:0}, {scale:1, opacity:0, duration:.8, ease:'power2.out', onComplete:() => img.remove()})`.

---

## 4. Cursor state changes on hover targets (grow / label)

Drive cursor states declaratively with `data-cursor` attributes — no per-element JS. Delegate one `mouseover`/`mouseout` pair on `document`. This scales cleanly across a whole site.

```html
<a href="#" data-cursor="view">Project</a>
<button data-cursor="grow">Play</button>
```
```css
.cursor { transition: width .3s, height .3s, background .3s; }
.cursor[data-state="grow"] { width: 64px; height: 64px; background: rgba(255,255,255,.2); }
.cursor[data-state="view"]::after {
  content: attr(data-label); position: absolute; inset: 0;
  display: grid; place-items: center; font: 600 11px/1 sans-serif; color: #000;
}
```
```js
// add inside the recipe-1 enableCursorFx block, after `el` is defined:
document.addEventListener('mouseover', e => {
  const t = e.target.closest('[data-cursor]');
  if (!t) return;
  el.dataset.state = t.dataset.cursor;
  if (t.dataset.cursor === 'view') el.dataset.label = t.dataset.label || 'View';
});
document.addEventListener('mouseout', e => {
  if (e.target.closest('[data-cursor]')) { el.dataset.state = ''; el.dataset.label = ''; }
});
```
Event delegation means dynamically-injected elements get the behaviour for free. **React:** expose a `setCursor(state)` from context and call it in `onMouseEnter`/`onMouseLeave`, or keep the same `data-cursor` + delegated listener in a top-level `useEffect`.

---

## 5. Hover image distortion (entry point)

A cursor-driven **WebGL displacement/RGB-shift on hover** (the liquid "gooey" image warp) is a shader effect, not a DOM trick — it needs a fragment shader sampling a displacement map against mouse velocity. **Do not hand-roll it here.**

→ Use the companion **`webgl-effect-recipes`** skill for the shader, the displacement-map setup, and the velocity uniform. If that skill is unavailable, the canonical standalone reference is [Codrops — Motion Hover Effects with Image Distortions (Three.js)](https://tympanus.net/codrops/2019/10/21/how-to-create-motion-hover-effects-with-image-distortions-using-three-js/) and [Making Gooey Image Hover Effects](https://tympanus.net/codrops/2019/10/23/making-gooey-image-hover-effects-with-three-js/). Wire its mouse-velocity input to the same `mousemove` source you already have from recipe 1, and keep it behind the same GUARDS.

---

## Ship checklist
- [ ] Everything gated behind `enableCursorFx()` — verified on a phone (native cursor, zero JS cost) and with OS reduce-motion ON.
- [ ] Only `transform`/`opacity` animated; `will-change` set; no `left/top` tweens.
- [ ] Trail nodes pruned (`.remove()` on transition/animation end) — no DOM growth over a 5-min session.
- [ ] `cursor: none` scoped to `body` and never applied when guards fail.
- [ ] Keyboard nav unaffected: `Tab` order intact, focus-visible rings present, no trapped focus.
- [ ] React recipes return cleanup (`cancelAnimationFrame` + `removeEventListener`).
