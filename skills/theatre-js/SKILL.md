---
name: theatre-js
description: Use when you need a VISUAL keyframe editor for web animations — drag keyframes on a timeline in the browser, then ship them to production. Best for orchestrating React Three Fiber scenes, marketing pages with cinematic camera moves, or any animation a designer wants to author without writing tween code. Triggers — "Theatre.js", "@theatre/core", "@theatre/studio", "Theatre R3F", "visual animation editor for web", "keyframe editor browser", "After Effects for code", "in-browser timeline editor".
---

# Theatre.js — visual animation editor in the browser

Theatre.js gives you an After-Effects-style timeline editor that runs **inside your dev environment**. You drag keyframes on a timeline, scrub, tweak easing, then **save the state to a JSON file**. In production you ship only the runtime + the saved state — the editor disappears.

**Mental model:**
- **GSAP timeline** — code-only. You write `.to(x, {...}, position)`. Power but slow iteration.
- **Motion** — declarative, React-state-driven. No timeline.
- **Theatre.js** — visual timeline. Drag keyframes. Production runtime reads the saved state. Closest thing to AE on the web.

For Karim: pair Theatre with **R3F** for cinematic Three.js camera/lights moves, or with **DOM** for marketing hero sequences a designer can refine without dev round-trips.

## When to reach for Theatre

- A 3D scene needs cinematic camera moves — pan, dolly, focus pulls — and you want to scrub them
- Marketing page hero with synchronized DOM + 3D animation where timing must be perfect
- A designer wants to "tweak the bounce" or "delay the title 200ms" without a code change
- You're producing a one-off agency page where iteration speed > runtime efficiency
- You want a single editable source of truth for an animation that drives multiple elements

**Do NOT use** Theatre when:
- The animation is reactive to runtime state (use Motion / GSAP)
- You need 1000+ keyframes (Theatre is fine for tens, not thousands)
- The team doesn't have a designer/animator who wants visual control — code is faster for devs
- You want zero-overhead bundle — Theatre adds ~50KB even just the runtime

## Install

```bash
npm install @theatre/core @theatre/studio
```

For React Three Fiber integration:
```bash
npm install @theatre/r3f
```

## Core concepts

1. **Project** — top-level container. One per app
2. **Sheet** — a timeline. Like an After Effects composition
3. **Object** — something on the sheet you animate. Has named props
4. **Studio** — the editor UI overlay (dev only)
5. **State** — the JSON your project gets saved into

## Minimal vanilla example

```js
import { getProject, types } from '@theatre/core';
import studio from '@theatre/studio';

studio.initialize();   // ONLY in dev — gate behind import.meta.env.DEV

const project = getProject('My Project');
const sheet = project.sheet('Hero Animation');
const obj = sheet.object('Title', {
  x: types.number(0, { range: [-500, 500] }),
  opacity: types.number(1, { range: [0, 1] }),
  rotation: 0,
});

obj.onValuesChange(({ x, opacity, rotation }) => {
  titleEl.style.transform = `translateX(${x}px) rotate(${rotation}deg)`;
  titleEl.style.opacity = opacity;
});

sheet.sequence.play({ iterationCount: Infinity });
```

The Studio panel appears as an overlay. Drag the playhead, change values — keyframes record. Click "Save" → exports `state.json`.

## Production deploy — strip Studio, load state

After saving the JSON from Studio:

```js
import { getProject } from '@theatre/core';
import projectState from './state.json';

const project = getProject('My Project', { state: projectState });
const sheet = project.sheet('Hero Animation');
const obj = sheet.object('Title', { x: 0, opacity: 1, rotation: 0 });

obj.onValuesChange(values => { /* apply to DOM */ });
sheet.sequence.play();
```

No Studio import in prod. The state file is the source of truth.

```js
// Recommended dev/prod split
if (import.meta.env.DEV) {
  const studio = (await import('@theatre/studio')).default;
  studio.initialize();
}
```

## React Three Fiber integration (the killer use case)

```bash
npm install @theatre/core @theatre/studio @theatre/r3f
```

```jsx
import { Canvas } from '@react-three/fiber';
import { editable as e, SheetProvider, PerspectiveCamera } from '@theatre/r3f';
import { getProject } from '@theatre/core';
import studio from '@theatre/studio';
import extension from '@theatre/r3f/dist/extension';
import state from './state.json';

if (import.meta.env.DEV) {
  studio.initialize();
  studio.extend(extension);   // adds 3D gizmos to Studio
}

const sheet = getProject('Demo', { state }).sheet('Scene');

export default function App() {
  return (
    <Canvas>
      <SheetProvider sheet={sheet}>
        <PerspectiveCamera theatreKey="Camera" makeDefault position={[0, 0, 5]} />
        <e.mesh theatreKey="Cube">
          <boxGeometry />
          <meshStandardMaterial color="hotpink" />
        </e.mesh>
        <e.directionalLight theatreKey="Light" position={[5, 5, 5]} />
      </SheetProvider>
    </Canvas>
  );
}
```

`editable as e` wraps R3F components and exposes their props in Theatre. Open Studio → drag camera in 3D viewport → keyframes record. Zero R3F animation code written.

## Common patterns

### Scrub by scroll instead of play()
```js
window.addEventListener('scroll', () => {
  const progress = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  sheet.sequence.position = progress * sheet.sequence.length;
});
```

Pair with Lenis for lerped scrubbing.

### Multi-stage timeline with markers
In Studio, add markers at named times. In code:
```js
sheet.sequence.play({ range: [0, 3], iterationCount: 1 });    // play 0–3s
sheet.sequence.position = sheet.sequence.markers['intro-end'].time;
```

### Drive Motion / GSAP from Theatre values
```js
obj.onValuesChange(({ progress }) => {
  motionApi.set(progress);    // bridge to other animation systems
});
```

Theatre is the orchestrator; downstream libs render.

## Versioning the state file

`state.json` lives in your repo. Commit it. Designers edit via Studio → "Save" → commit. Code reviews show keyframe changes as JSON diffs (readable enough — keyframe times + values).

**This is huge for client work:** designer iterates in browser, commits, you deploy. No Figma → Lottie → re-export loop.

## Types & props

```js
const obj = sheet.object('Hero', {
  position: types.compound({
    x: types.number(0, { range: [-100, 100] }),
    y: types.number(0, { range: [-100, 100] }),
  }),
  color: types.rgba({ r: 1, g: 0, b: 0, a: 1 }),
  visible: types.boolean(true),
  label: types.string('Hello'),
  mode: types.stringLiteral('idle', { idle: 'Idle', active: 'Active' }),
});
```

Studio shows the right control per type (slider, color picker, dropdown, toggle).

## Performance

1. **Studio is dev-only** — never ship it. Gate behind env check or dynamic import
2. **Runtime is lean** — only `@theatre/core` + state.json. ~50KB
3. **`onValuesChange` fires every frame** — keep handlers cheap. Apply to refs, not React state
4. **Sequence playback uses RAF internally** — don't add another RAF on top
5. **Many small objects > one big one** — Theatre tracks dirty props efficiently per object

## Gotchas

1. **State JSON path** — Theatre warns "state out of date" loudly if your code defines different props than the saved state. Match exactly
2. **Hot reload** — Theatre handles HMR but new Studio instances can leak. If Studio doubles up, hard-refresh
3. **Bundle size** — Studio adds ~300KB. Always tree-shake out of prod
4. **R3F deps** — `@theatre/r3f` peer-depends on specific R3F versions. Pin them or expect drift
5. **Mobile keyboards** — Studio's keyboard shortcuts (space=play, arrows=scrub) conflict with text inputs on focus. Studio handles it but watch for edge cases
6. **`sheet.object()` is idempotent** — calling it twice with the same name returns the same object. Don't try to create variants by re-calling

## Quick decision guide

| Need | Reach for |
|---|---|
| Cinematic R3F camera moves | Theatre + `@theatre/r3f` |
| Designer needs to tweak timing | Theatre Studio |
| Reactive UI motion (hover, state) | Motion (not Theatre) |
| Sub-frame timeline orchestration | GSAP timeline |
| Scroll-scrubbed video-like sequence | Theatre + scroll-to-sequence-position |
| One-off bespoke agency hero | Theatre (iteration speed wins) |
| Repeatable component animations | Motion variants (not Theatre) |

## Workflow recommendation for Karim

For UGC client landing pages with 3D hero:
1. Engineer scaffolds R3F scene + Theatre + `@theatre/r3f`
2. Designer opens dev URL → tweaks camera path, lighting, timing in Studio
3. Designer "Save" → commits `state.json`
4. Engineer deploys. Zero animation code touched after scaffolding

This collapses the design-dev round-trip on cinematic moments from days to hours.

## Related

`three` (the R3F / Three.js scenes Theatre orchestrates), `gsap-timeline` (alternative orchestration for code-first projects), `motion-dev` (component-level motion that pairs with Theatre's scene-level orchestration), `lenis-smooth-scroll` (drives scroll position into Theatre sequences).
