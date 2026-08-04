---
name: matter-js
description: >-
  Matter.js — the 2D rigid-body physics engine for the web. Fire this whenever a build needs real physics in the browser: falling/stacking/colliding objects, draggable bodies, springs and ragdolls, gravity playgrounds, Newton's cradle, physics-driven hero sections, cursor-repel or click-to-drop interactions, or a physics layer feeding an award-style immersive/scroll/WebGL/Three.js/Pixi scene. Triggers on "matter.js", "matter-js", "2D physics", "physics engine", "rigidbody / rigid body", "gravity simulation", "collision detection", "draggable physics", "bouncing balls", plus any immersive/awwwards/Webflow/GSAP context that asks for objects that fall, bounce, collide, or respond to the pointer. Covers custom canvas/WebGL rendering (bypassing Matter.Render), React/Next mounting with strict cleanup, performance tuning, and a prefers-reduced-motion fallback.
---

# Matter.js — 2D physics for immersive web

Matter.js is a mature (MIT, `matter-js` on npm, current line 0.20.x) 2D rigid-body engine: it integrates forces, resolves collisions, and hands you each body's `position`, `angle`, and `vertices` every tick. It ships an optional debug renderer and an optional runner, but for production immersive work you almost always drive your own loop and draw the bodies yourself into a canvas, WebGL, or Three.js layer. The engine is the physics brain; the pixels are your job.

## When to reach for it

Use Matter.js when elements must obey physics: fall under gravity, stack, bounce, collide, get flung by the cursor, hang from springs, or settle into a pile. If you only need eased tween motion along a known path, use GSAP instead — physics is for emergent, reactive motion you do not want to hand-author.

## Quick start

Install:

```bash
npm install matter-js
```

Or from a CDN (UMD global `Matter`), pinning a version:

```html
<script src="https://cdn.jsdelivr.net/npm/matter-js@0.20.0/build/matter.min.js"></script>
```

Smallest thing that runs — the built-in renderer and runner, two boxes and a floor:

```javascript
const { Engine, Render, Runner, Bodies, Composite } = Matter;

const engine = Engine.create();                 // engine.world, engine.gravity live here
const render = Render.create({ element: document.body, engine });

const boxA = Bodies.rectangle(400, 200, 80, 80);
const boxB = Bodies.rectangle(450, 50, 80, 80);
const ground = Bodies.rectangle(400, 610, 810, 60, { isStatic: true });

Composite.add(engine.world, [boxA, boxB, ground]);

Render.run(render);
Runner.run(Runner.create(), engine);
```

`Matter.Render` is a debug view (wireframes, velocity vectors, bounds). Ship it for prototyping, then replace it with your own drawing — see [Custom rendering](#custom-rendering-the-production-path). With ES modules, `matter-js` ships UMD, so the reliable form is a default import you destructure:

```javascript
import Matter from 'matter-js';
const { Engine, Runner, Bodies, Composite, Body, Constraint, Events } = Matter;
```

## Core building blocks

**Engine** — `Engine.create([options])` returns an engine holding `world` (the root composite), `gravity` (`{ x: 0, y: 1, scale: 0.001 }` by default — set `gravity.y = 0` for zero-g, flip sign to float things up), and `timing`. Advance it with `Engine.update(engine, delta)` where `delta` is milliseconds (defaults near 16.666). `Engine.clear(engine)` tears down internal state.

**Runner** — the built-in fixed-timestep loop. `Runner.create()`, `Runner.run(runner, engine)`, `Runner.stop(runner)`. Convenient, but a custom `requestAnimationFrame` loop calling `Engine.update` gives you frame-synced control and is what you want when rendering yourself.

**Bodies** (factory) — every call takes a centre `(x, y)` and returns a body:
- `Bodies.rectangle(x, y, width, height, [options])`
- `Bodies.circle(x, y, radius, [options], [maxSides])`
- `Bodies.polygon(x, y, sides, radius, [options])`
- `Bodies.trapezoid(x, y, width, height, slope, [options])`
- `Bodies.fromVertices(x, y, vertexSets, [options])` — arbitrary shapes; concave shapes need the `poly-decomp` library registered via `Common.setDecomp(require('poly-decomp'))`, otherwise you get the convex hull.

**Body** (operate on an existing body) — `Body.applyForce(body, position, force)` (force at a world point; tiny numbers, e.g. `0.05`), `Body.setVelocity(body, {x, y})`, `Body.setStatic(body, bool)`, `Body.setPosition(body, {x, y})`, `Body.setAngle(body, radians)`, `Body.rotate`, `Body.scale`. Read from `body.position`, `body.angle` (radians), `body.vertices` (array of world-space `{x, y}` corners), `body.bounds` (`{ min, max }`), `body.velocity`, `body.isSleeping`, `body.label`.

**Body options / material defaults** (pass in the factory's options object): `restitution` (bounciness, 0 → dead, ~0.9 → very bouncy; default 0), `friction` (0.1), `frictionAir` (0.01 — air drag, raise it to make motion feel heavy/damped), `frictionStatic` (0.5), `density` (0.001 — mass is derived from density × area, set this rather than mass directly), `isStatic`, `isSensor`, `collisionFilter`, and `render` (only read by `Matter.Render`).

**Composite / World** — `Composite.add(composite, bodyOrArray)`, `Composite.remove`, `Composite.allBodies(composite)`, `Composite.clear(composite, keepStatic)`. `engine.world` is itself a composite; `World.add(engine.world, …)` is an alias for `Composite.add`.

**Constraint** — springs and pins. `Constraint.create({ bodyA, bodyB, pointA, pointB, length, stiffness, damping })`. `pointA`/`pointB` are offsets from each body's centre (or absolute if that side has no body — pin to a fixed world point by giving only `bodyB` + `pointA`). `stiffness` 0–1: near 1 is a rigid rod, low values are a loose spring. Omit `length` to keep the current distance.

**Composites** (prefab arrangements):
- `Composites.stack(xx, yy, columns, rows, columnGap, rowGap, callback)` — `callback(x, y, column, row, lastBody, i)` returns the body to place.
- `Composites.pyramid(xx, yy, columns, rows, columnGap, rowGap, callback)` — same callback, triangular packing.
- `Composites.newtonsCradle(xx, yy, number, size, length)` — returns a ready cradle composite.

**Events** — `Events.on(object, names, handler)` and `Events.off(object, names, handler)`. On the engine: `beforeUpdate`, `afterUpdate`, and the collision trio `collisionStart`, `collisionActive`, `collisionEnd`. Collision handlers receive `event.pairs`, each with `.bodyA` and `.bodyB`. Always pair every `on` with an `off` on teardown.

## Custom rendering (the production path)

Skip `Matter.Render` for anything shipping. Run your own loop, step the engine with a clamped delta, then read each body's geometry and draw it. This is what lets physics feed a branded canvas, a WebGL pass, or a Three.js scene.

```javascript
import Matter from 'matter-js';
const { Engine, Bodies, Composite } = Matter;

const canvas = document.querySelector('#stage');
const ctx = canvas.getContext('2d');

const engine = Engine.create();
const balls = Array.from({ length: 40 }, () =>
  Bodies.circle(Math.random() * canvas.width, Math.random() * 200, 12, { restitution: 0.8 })
);
const walls = [
  Bodies.rectangle(canvas.width / 2, canvas.height + 30, canvas.width, 60, { isStatic: true }),
  Bodies.rectangle(-30, canvas.height / 2, 60, canvas.height, { isStatic: true }),
  Bodies.rectangle(canvas.width + 30, canvas.height / 2, 60, canvas.height, { isStatic: true }),
];
Composite.add(engine.world, [...balls, ...walls]);

let last = performance.now();
let raf;
function frame(now) {
  const delta = Math.min(now - last, 1000 / 30); // clamp: never step more than a 30fps slice
  last = now;
  Engine.update(engine, delta);

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (const body of Composite.allBodies(engine.world)) {
    const v = body.vertices;                     // world-space corners, already rotated
    ctx.beginPath();
    ctx.moveTo(v[0].x, v[0].y);
    for (let i = 1; i < v.length; i++) ctx.lineTo(v[i].x, v[i].y);
    ctx.closePath();
    ctx.fillStyle = '#e8e2d6';
    ctx.fill();
  }
  raf = requestAnimationFrame(frame);
}
raf = requestAnimationFrame(frame);
// on teardown: cancelAnimationFrame(raf)
```

The engine works in the same pixel space as your canvas — `body.position` and `body.vertices` are already in world coordinates, so a body at `(400, 200)` draws at canvas `(400, 200)`. Because `vertices` are pre-rotated you rarely need `body.angle` directly; reach for it when you draw a sprite or a Three.js mesh that you rotate yourself. For a sprite: translate to `body.position`, `ctx.rotate(body.angle)`, draw the image centred, restore.

**Delta clamping is not optional.** When a tab is backgrounded, `requestAnimationFrame` pauses and the next `now - last` can be hundreds of ms. Feeding that straight into `Engine.update` makes bodies tunnel through walls and explode. Clamp it (as above), or use Matter's fixed-timestep runner which does this for you.

## Recipe: drag bodies with the pointer

`MouseConstraint` turns the cursor into a soft grabber. When you render into your own canvas, still create a `Mouse` on that canvas so screen coordinates map correctly.

```javascript
const { Mouse, MouseConstraint } = Matter;

const mouse = Mouse.create(canvas);
const mouseConstraint = MouseConstraint.create(engine, {
  mouse,
  constraint: { stiffness: 0.2, render: { visible: false } },
});
Composite.add(engine.world, mouseConstraint);

// if the canvas is CSS-scaled or on a HiDPI display, correct the pixel ratio:
mouse.pixelRatio = window.devicePixelRatio;
```

`stiffness` on the mouse constraint controls how snappily the grabbed body follows — lower feels elastic, higher feels glued. Static bodies are not grabbable.

## Recipe: springs and hanging chains

Constraints build springs, pendulums, and rope. Pin one end to a fixed point by giving the constraint only `bodyB` plus an absolute `pointA`.

```javascript
const { Bodies, Constraint, Composite } = Matter;

const anchor = { x: 400, y: 100 };
const bob = Bodies.circle(400, 300, 24, { frictionAir: 0.02 });

const spring = Constraint.create({
  pointA: anchor,          // fixed world point (no bodyA)
  bodyB: bob,
  stiffness: 0.02,         // low = springy; near 1 = rigid rod
  damping: 0.05,
  length: 150,
});
Composite.add(engine.world, [bob, spring]);
```

Chain several bodies with constraints between successive `bodyA`/`bodyB` pairs to get rope or a ragdoll. Raise `frictionAir` on the bodies so the chain settles instead of oscillating forever.

## Recipe: prefab stacks, pyramids, cradle

```javascript
const { Composites, Bodies, Composite } = Matter;

const boxes = Composites.stack(120, 0, 8, 5, 6, 6, (x, y) =>
  Bodies.rectangle(x, y, 40, 40, { restitution: 0.2 })
);

const cradle = Composites.newtonsCradle(300, 120, 5, 30, 200);

Composite.add(engine.world, [boxes, cradle]);
```

`stack`/`pyramid` call your callback per cell with the computed `(x, y)`; return any body. The cradle is self-contained — add it and it swings.

## Recipe: collisions, filters, and sensors

Listen for contacts, and use `collisionFilter` to control what hits what. Sensors detect overlap without pushing back — ideal for trigger zones.

```javascript
const { Events, Bodies, Body, Composite } = Matter;

// categories are single bits; a body collides with another only if each side's
// mask includes the other's category.
const WALL = 0x0001, PLAYER = 0x0002, PICKUP = 0x0004;

const player = Bodies.circle(200, 100, 20, {
  collisionFilter: { category: PLAYER, mask: WALL | PICKUP },
});
const coin = Bodies.circle(400, 100, 14, {
  isSensor: true,                                // overlaps, never blocks
  collisionFilter: { category: PICKUP, mask: PLAYER },
});
Composite.add(engine.world, [player, coin]);

Events.on(engine, 'collisionStart', (event) => {
  for (const { bodyA, bodyB } of event.pairs) {
    const pair = [bodyA, bodyB];
    if (pair.includes(player) && pair.includes(coin)) {
      Composite.remove(engine.world, coin);       // collect
    }
  }
});
```

`collisionFilter` also has `group`: two bodies with the same non-zero `group` always collide (positive) or never collide (negative), overriding category/mask — handy for "these ragdoll parts never self-collide". To boot a body across the scene, `Body.applyForce(player, player.position, { x: 0.05, y: -0.1 })` (forces are small) or set velocity directly with `Body.setVelocity`.

## React / Next mounting and strict cleanup

Physics state, a canvas, RAF handles, and event listeners all leak across React re-renders and hot reloads if you do not tear them down. Under React 18 Strict Mode the effect runs twice in development, so cleanup that fully reverses setup is the only thing that keeps you from stacking two engines. Create everything inside `useEffect`, keep handles in the closure, and undo each one.

```jsx
'use client';
import { useEffect, useRef } from 'react';
import Matter from 'matter-js';

export default function PhysicsStage() {
  const canvasRef = useRef(null);

  useEffect(() => {
    const { Engine, Runner, Render, Bodies, Composite, Mouse, MouseConstraint, Events } = Matter;
    const canvas = canvasRef.current;

    const engine = Engine.create();
    const render = Render.create({ canvas, engine, options: { wireframes: false, background: '#0d0d0f' } });
    const runner = Runner.create();

    const ground = Bodies.rectangle(200, 380, 420, 40, { isStatic: true });
    Composite.add(engine.world, [ground, Bodies.circle(200, 60, 24, { restitution: 0.7 })]);

    const mouse = Mouse.create(canvas);
    const mc = MouseConstraint.create(engine, { mouse, constraint: { stiffness: 0.2, render: { visible: false } } });
    Composite.add(engine.world, mc);

    const onTick = () => { /* per-frame logic */ };
    Events.on(engine, 'afterUpdate', onTick);

    Render.run(render);
    Runner.run(runner, engine);

    return () => {
      Events.off(engine, 'afterUpdate', onTick);   // drop listeners
      Render.stop(render);                         // stop the draw loop
      Runner.stop(runner);                         // stop stepping
      Composite.clear(engine.world, false);        // empty the world
      Engine.clear(engine);                        // free engine state
      render.canvas = null;                        // release the canvas ref Render held
      render.context = null;
      render.textures = {};
    };
  }, []);

  return <canvas ref={canvasRef} width={400} height={400} />;
}
```

If you render into your own loop instead of `Matter.Render`, the cleanup swaps `Render.stop` for `cancelAnimationFrame(rafRef.current)` and you skip the `render.*` nulling. Either way: stop the loop, remove events, clear the world, clear the engine. Never `new` a second engine without clearing the first.

## Performance

- **Clamp the delta** (shown above). One skipped frame with an unclamped step is the most common cause of bodies exploding or tunnelling through thin walls.
- **Iterations trade accuracy for cost.** `engine.positionIterations` (default 6) and `engine.velocityIterations` (default 4) can drop to 4/3 for large scenes that tolerate softer contacts, or rise for tall stacks that must not jitter. `engine.constraintIterations` (default 2) matters when you have many constraints.
- **`body.slop`** (default 0.05) is the allowed penetration before contacts resolve. Slightly higher slop settles stacks faster and cheaper; too high and bodies visibly sink into each other.
- **Enable sleeping** so settled bodies stop consuming solver time: `engine.enableSleeping = true`. Sleeping bodies wake on contact; watch the `sleepStart` / `sleepEnd` events if your render needs to react. Note that sleeping can make bodies ignore small forces until nudged.
- **Keep bodies simple.** Circles and boxes are cheapest; high-`sides` polygons and `fromVertices` shapes cost more per contact. Prefer a few primitives over one concave mesh.
- **Never ship the debug renderer.** If you keep `Matter.Render`, at least set `options.wireframes = false`; it defaults to a wireframe overlay that redraws every edge.
- **Cull off-screen bodies** with `body.bounds` versus your viewport when the world is larger than the view — remove or skip-draw what `Bounds.overlaps` says is out of frame.

## Accessibility: prefers-reduced-motion

Emergent physical motion is exactly what motion-sensitive users ask to suppress. Detect the preference and, instead of animating, compose a static settled layout: build the bodies, step the engine enough times to let them come to rest, draw one frame, and never start the loop.

```javascript
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (reduced) {
  for (let i = 0; i < 240; i++) Engine.update(engine, 1000 / 60); // settle silently
  drawOnce();                                                      // single static frame, no RAF, no runner
} else {
  startLoop();                                                     // your rAF loop or Runner.run
}
```

This preserves the composed look (a pile of shapes, a hung pendulum at rest) without any movement on screen. Also honour the preference for pointer-driven effects: skip the `MouseConstraint` or cursor-repel forces when `reduced` is true. Listen to the media query's `change` event if the user can toggle it mid-session.

## Pitfalls

- **Unclamped delta on tab refocus** — see Performance; clamp every step.
- **Mouse coordinates off on HiDPI or CSS-scaled canvas** — set `mouse.pixelRatio = window.devicePixelRatio`, and if the canvas is resized after creation, `Mouse.setElement` / recreate the mouse so offsets stay correct.
- **Concave `fromVertices` collapses to a convex hull** — that is the missing decomposition library. Register it with `Common.setDecomp(decomp)` (the `poly-decomp` package) before calling `fromVertices`.
- **Forces feel like nothing** — `Body.applyForce` uses tiny magnitudes because mass ≈ density(0.001) × area. Try values around `0.01`–`0.1`, not whole numbers, or set velocity directly.
- **Setting `body.mass` by hand** — mass derives from `density` and area; assign `density` in the options instead so the inertia stays consistent.
- **Mutating `body.position` directly** — bypasses the engine's bookkeeping; use `Body.setPosition` so bounds and vertices update.
- **Two engines after a re-render / hot reload** — always `Engine.clear` and stop the loop in cleanup; a leaked engine keeps stepping invisibly and tanks the frame rate.
- **Static bodies ignore forces and dragging** — flip with `Body.setStatic(body, false)` when you need them to react.

## References

Grounded in the official docs fetched for this skill:

- API reference — https://brm.io/matter-js/docs/
- Getting started (wiki) — https://github.com/liabru/matter-js/wiki/Getting-started
- Wiki (Rendering, Running, and more) — https://github.com/liabru/matter-js/wiki
- Source, examples, releases — https://github.com/liabru/matter-js
