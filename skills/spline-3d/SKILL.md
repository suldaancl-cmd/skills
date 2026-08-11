---
name: spline-3d
description: Use when embedding 3D scenes designed in Spline (app.spline.design) into a web page — drag-and-drop 3D without writing Three.js boilerplate, designer-driven 3D heroes, interactive objects with state, or React-friendly 3D where the designer iterates without touching code. Triggers — "Spline", "Spline 3D", "@splinetool", "spline.design", "embed 3D scene", "3D hero without three.js", "interactive 3D object on website", "react-spline", "no-code 3D web".
---

# Spline — designer-friendly 3D scenes on the web

Spline (spline.design) is a Figma-for-3D: designers build scenes in a browser-based editor, then export them to a runtime that renders in any web page. It's the "no-code Three.js" — you trade some performance and control for massive iteration speed.

**Mental model:**
- **Three.js / R3F** = code-first. Full control. Steep learning curve. Best perf.
- **Spline** = designer-first. Drag, drop, light, camera. Adequate perf. Iteration time is hours not days.

For Karim's stack: pair Spline with `hyliox-landing` / `3d-animation-web-designer` when the designer can ship a `.splinecode` URL faster than a developer can write R3F.

## When to reach for Spline

Use Spline when:
- A designer hands you a published scene URL (`https://prod.spline.design/.../scene.splinecode`)
- You need a 3D hero element on a marketing page but don't have a Three.js engineer
- The scene needs designer iteration during the project — they edit, you don't redeploy
- Interactive 3D objects with simple state machines (hover, click → trigger event in scene)
- Showcase pages where a product floats / spins — perfect Spline use case

**Do NOT use** Spline when:
- You need <100KB bundle — Spline runtime is ~600KB gzipped, scenes are 200KB-5MB
- High-perf real-time rendering, post-processing, custom shaders — go raw Three.js / R3F
- The 3D is data-driven (e.g., a CMS-fed product configurator) — Three.js gives you the JS hooks
- Tight art direction control via code (programmatic camera moves, shader variants) — use Three.js

## Install

### React (canonical)
```bash
npm install @splinetool/react-spline @splinetool/runtime
```
```jsx
import Spline from '@splinetool/react-spline';

export default function Hero() {
  return (
    <Spline scene="https://prod.spline.design/abc123/scene.splinecode" />
  );
}
```

That's it. The scene loads, lights, cameras, materials all in one URL.

### Next.js App Router
Two entries, two rules — mixing them renders NOTHING (verified 2026-08-11):

```jsx
// Server Component (no 'use client') — SSR + auto blur placeholder, but NO event props
import Spline from '@splinetool/react-spline/next';

// Client Component ('use client') — needed for onLoad/onSpline* events
import Spline from '@splinetool/react-spline';
```

**Gotcha:** the `/next` entry is an async Server Component. Putting it inside a
`'use client'` file fails silently — empty scene, console says
"is an async Client Component. Only Server Components can be async". If you need
`onLoad` (e.g. reduced-motion `app.stop()`), use the classic entry in a client
component and accept losing the SSR blur placeholder.

### Vanilla JS
```bash
npm install @splinetool/runtime
```
```js
import { Application } from '@splinetool/runtime';

const canvas = document.getElementById('canvas');
const app = new Application(canvas);
await app.load('https://prod.spline.design/.../scene.splinecode');
```

## Loading states & code-splitting

A 1-2MB scene is normal. Lazy-load it:

```jsx
import { Suspense, lazy } from 'react';
const Spline = lazy(() => import('@splinetool/react-spline'));

<Suspense fallback={<HeroSkeleton />}>
  <Spline scene="..." onLoad={() => console.log('loaded')} />
</Suspense>
```

For below-the-fold scenes, use IntersectionObserver + `loading="lazy"` pattern — only fetch when in viewport.

## Interactive scenes — events from Spline → React

In the Spline editor, the designer adds **Events** to objects (e.g., "on click, change state to Hovered"). The React runtime exposes these:

```jsx
function App() {
  function onLoad(splineApp) {
    const cube = splineApp.findObjectByName('Cube');
    cube.emitEvent('mouseHover');                // trigger a Spline event by name
  }

  function onMouseDown(e) {
    if (e.target.name === 'Cube') {
      // user clicked the Cube object
    }
  }

  return <Spline scene="..." onLoad={onLoad} onSplineMouseDown={onMouseDown} />;
}
```

Available events: `onSplineMouseDown`, `onSplineMouseUp`, `onSplineMouseHover`, `onSplineKeyDown`, `onSplineKeyUp`, `onSplineStart`, `onSplineLookAt`, `onSplineFollow`, `onSplineScroll`.

## Manipulating objects from code

```jsx
function App() {
  const splineRef = useRef();

  const onLoad = (app) => {
    splineRef.current = app;
  };

  const handleClick = () => {
    const obj = splineRef.current.findObjectByName('Sphere');
    obj.position.x += 100;
    obj.rotation.y += Math.PI / 4;
    obj.scale.set(1.5, 1.5, 1.5);
    obj.visible = false;
  };

  return <><Spline scene="..." onLoad={onLoad} /><button onClick={handleClick}>Move</button></>;
}
```

Position, rotation, scale, visibility, and material color are all mutable. The scene's animations still play unless you pause them.

## Variables — scene-level state from code

In the Spline editor, designers can expose **Variables** (numbers, booleans, colors). Read/write from code:

```js
splineApp.setVariable('mouseX', e.clientX);
const intensity = splineApp.getVariable('lightIntensity');
```

This is the cleanest way to make a Spline scene react to scroll / cursor / app state.

## Scroll-driven Spline

```jsx
const onLoad = (app) => {
  window.addEventListener('scroll', () => {
    const progress = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    app.setVariable('scrollProgress', progress * 100);   // designer wires this to camera/object
  });
};
```

Pair with Lenis for buttery scroll → variable updates.

## Performance — the only thing that matters with Spline

1. **Compress textures in the editor** — biggest single win. Spline's "Export → Optimize" reduces scenes 60-80%
2. **Lower poly counts** — anything > 50K polys is a smell. Spline's Performance panel shows the budget
3. **Disable physics if not used** — Spline includes a physics engine; turn it off per-object when unused
4. **Use baked lighting** — real-time lighting on multiple objects tanks FPS. Bake to texture in the editor
5. **Set `renderOnDemand`** — only re-render when something changes (camera moves, hover). Static scenes don't need 60fps RAF
6. **Cap pixel ratio** — `<Spline renderOnDemand pixelRatio={Math.min(2, window.devicePixelRatio)} />` saves ~50% on Retina

## Spline + Three.js coexistence

Spline scenes are NOT directly importable into Three.js. The runtime is its own renderer. If you need Three.js integration:
- Export the scene **as GLB/GLTF** from Spline (under File → Export → GLB)
- Then import into Three.js / R3F with `useGLTF` from `@react-three/drei`
- This loses Spline events/variables but gives you full Three.js control

## Quick decision guide

| Need | Reach for |
|---|---|
| 3D hero from a designer in 1 day | Spline `@splinetool/react-spline` |
| Interactive 3D button on a page | Spline + `onSplineMouseDown` |
| Scroll-following 3D object | Spline + `setVariable('scrollProgress', ...)` |
| Product configurator (data-driven) | Three.js / R3F (not Spline) |
| Custom shader / post-processing | Three.js / R3F |
| 60fps competitive game UI | Three.js / R3F |
| Designer needs to iterate without dev | Spline |

## Gotchas

1. **Scene URL is public** — anyone can copy your `.splinecode` URL and embed it. For exclusive scenes, self-host the export
2. **No code import** — designer changes ship via Spline's CDN, not your repo. Versioning lives in Spline. Test before deploying client-facing
3. **Mobile performance varies wildly** — test on a mid-range Android. Spline's editor doesn't show real mobile FPS
4. **`Application.load()` is one-shot** — to swap scenes, dispose and recreate. Don't try to `.load()` twice on one instance
5. **SSR + Spline** — strictly client-only. Use Next's `'use client'` + the `/next` entry point
6. **Touch events** — Spline supports touch but you may need to disable default touch-pan if the scene uses one-finger drag
7. **Bundle size** — ~600KB just for the runtime. Lazy-load. Don't put Spline in critical above-the-fold bundle

## Sourcing scenes

- **Spline Community** (spline.design/community) — free + paid public scenes
- **Hire a Spline designer** — Twitter/Threads has an active scene; rates $50-500/scene
- **Build it yourself** — the editor's onboarding is excellent. A polished hero takes 2-4 hours to learn

For Karim: a single "floating product" Spline scene reused across UGC client landings is a $0 marginal cost. Worth investing one week into Spline editor fluency.

## Related

`three` (Three.js / R3F for full control when Spline runs out of room), `hyliox-landing` and `3d-animation-web-designer` (compatible cinematic landing aesthetics), `senior-frontend` (React Suspense + lazy-loading patterns for big scenes).
