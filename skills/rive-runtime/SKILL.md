---
name: rive-runtime
description: Use when building INTERACTIVE animations with state machines, inputs (numbers/booleans/triggers), or character rigs that respond to user input — different from playback-only Lottie. Triggers — "Rive", ".riv file", "state machine animation", "interactive vector animation", "Rive runtime", "rive-app", "animation with inputs", "responsive character animation", "rive.app".
---

# Rive — interactive runtime animations

Rive is **Lottie's interactive cousin**. Same vector-export-to-web idea, but Rive adds a **state machine** layer: animations have named inputs (booleans, numbers, triggers) that the runtime drives. The same `.riv` file can be a button that morphs on hover, an avatar that follows the cursor, a loader that switches state based on API response, or a character with conditional poses.

**Mental model:**
- **Lottie** = movie file. You play, pause, scrub. Output is the same every time.
- **Rive** = interactive component. You set inputs; the state machine decides what plays.

If the animation needs to respond to user/app state, choose Rive. If it just needs to play, choose Lottie.

## When to reach for Rive

- Interactive buttons (Rive's killer demo — the "twirling submit button" you've seen everywhere)
- Onboarding mascots that react to clicks/scroll
- Loading states that morph success/error/loading without manually swapping files
- Game-like UI: a meter that fills, a character that runs faster as a number increases
- Avatars that follow cursor / look at clicks
- Any animation where "play frame X to Y" is too rigid

**Don't use Rive** when:
- The animation is play-once or playback-only — Lottie is simpler and ecosystem is larger
- The designer doesn't know Rive (the editor at rive.app is the bottleneck — there's no "Bodymovin → Rive" exporter)
- You need photorealistic textures — Rive is vector

## Install

### Vanilla / framework-agnostic
```bash
npm install @rive-app/canvas
```
```js
import { Rive } from '@rive-app/canvas';

const r = new Rive({
  src: '/button.riv',
  canvas: document.getElementById('canvas'),
  autoplay: true,
  stateMachines: 'Button',  // name from the .riv file
  onLoad: () => r.resizeDrawingSurfaceToCanvas(),
});
```

### React
```bash
npm install @rive-app/react-canvas
```
```jsx
import { useRive, useStateMachineInput } from '@rive-app/react-canvas';

function FancyButton() {
  const { rive, RiveComponent } = useRive({
    src: '/button.riv',
    stateMachines: 'Button',
    autoplay: true,
  });
  const hover = useStateMachineInput(rive, 'Button', 'hover');
  const click = useStateMachineInput(rive, 'Button', 'click');

  return (
    <RiveComponent
      onMouseEnter={() => hover && (hover.value = true)}
      onMouseLeave={() => hover && (hover.value = false)}
      onClick={() => click?.fire()}
      style={{ width: 200, height: 60 }}
    />
  );
}
```

## State machines — the core concept

In the Rive editor, the designer creates:
1. **Animations** (timeline keyframes)
2. **State machine** — nodes (states) + transitions (edges) gated by **input conditions**
3. **Inputs**:
   - **Boolean** — true/false (hover, isOpen, isError)
   - **Number** — float (progress, speed, mood)
   - **Trigger** — one-shot fire (click, submit, retry)

In code, you read/write these inputs. The runtime handles all blending, transitions, and timing.

```js
const speedInput = useStateMachineInput(rive, 'Character', 'speed');
speedInput.value = 5;          // character animation speeds up

const submitTrigger = useStateMachineInput(rive, 'Form', 'submit');
submitTrigger.fire();          // plays the submit success animation
```

## Common patterns

### Hover/click button
```jsx
const { rive, RiveComponent } = useRive({ src: '/like.riv', stateMachines: 'Like' });
const isLiked = useStateMachineInput(rive, 'Like', 'liked');

<RiveComponent onClick={() => (isLiked.value = !isLiked.value)} />
```

### Loader that morphs success/error
```jsx
const state = useStateMachineInput(rive, 'Loader', 'state'); // number: 0=loading, 1=success, 2=error

useEffect(() => {
  fetch(...).then(() => state.value = 1).catch(() => state.value = 2);
}, []);
```

### Cursor-following avatar
```jsx
const cursorX = useStateMachineInput(rive, 'Avatar', 'cursorX');
const cursorY = useStateMachineInput(rive, 'Avatar', 'cursorY');

useEffect(() => {
  const onMove = (e) => {
    cursorX.value = (e.clientX / window.innerWidth) * 100;
    cursorY.value = (e.clientY / window.innerHeight) * 100;
  };
  window.addEventListener('mousemove', onMove);
  return () => window.removeEventListener('mousemove', onMove);
}, []);
```

### Scroll-driven Rive
```jsx
const progress = useStateMachineInput(rive, 'Scene', 'progress');

useEffect(() => {
  const onScroll = () => {
    const p = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    progress.value = p * 100;
  };
  window.addEventListener('scroll', onScroll);
  return () => window.removeEventListener('scroll', onScroll);
}, []);
```

For smoothness, pair with **Lenis** so `scrollY` is lerped, or use **GSAP ScrollTrigger**'s `onUpdate` to drive the input.

## Sizing & responsive

```js
const r = new Rive({
  src: '/anim.riv',
  canvas,
  layout: new Layout({
    fit: Fit.Contain,        // Contain | Cover | Fill | FitWidth | FitHeight | ScaleDown | None
    alignment: Alignment.Center,
  }),
  onLoad: () => r.resizeDrawingSurfaceToCanvas(),
});

window.addEventListener('resize', () => r.resizeDrawingSurfaceToCanvas());
```

In React, the `<RiveComponent>` handles this — just give it a CSS width/height.

## Multiple artboards / animations per file

A `.riv` file can contain multiple artboards (separate scenes). Specify which to load:

```js
new Rive({ src: '/scenes.riv', artboard: 'HeroScene', stateMachines: 'Idle' });
```

This is how Rive ships **theme variants** in one file — light/dark mode, brand-A/brand-B mascots.

## Sourcing Rive files

- **Rive Marketplace** (rive.app/marketplace) — free + paid community files
- **Hire a Rive designer** — niche skill, but the editor is approachable. Many Lottie designers cross over
- **Make it yourself** — rive.app editor is free, web-based. Learn in 1-2 days for simple cases

For Karim's UGC business: a `.riv` like-button or loader can be reused across every client landing page — one-time $0-50 asset, infinite reuse.

## Performance

1. **Canvas-only runtime** — Rive uses HTML canvas. Lighter than Lottie SVG for complex scenes
2. **WASM under the hood** — Rive ships a small WebAssembly runtime (~150KB gzipped). One-time cost; then animations are tiny (~5-30KB each)
3. **Pause when off-screen** — use IntersectionObserver to pause hidden Rive instances
4. **`resizeDrawingSurfaceToCanvas()` on resize only** — not on every frame
5. **WebGL renderer (newer)** — `@rive-app/webgl` exists for GPU-accelerated rendering. Use for 10+ concurrent Rive instances

## Gotchas

1. **State machine names are exact strings** — typo = silent failure. Always check the .riv file's state machine names in the Rive editor before coding
2. **Inputs are nullable** — `useStateMachineInput` returns null until the .riv loads. Always guard: `input && (input.value = x)` or `input?.fire()`
3. **`useRive` re-renders** — pass stable props. Wrap `src` in `useMemo` if it's an inline string
4. **`@rive-app/canvas` is one of THREE packages** — there's also `@rive-app/webgl` and `@rive-app/canvas-advanced`. Default to `canvas` unless you have >10 instances
5. **SSR** — Rive uses canvas + WASM. Client-side only. Next.js: `dynamic(() => import('...'), { ssr: false })`
6. **Cleanup** — `useRive` handles unmount in React. In vanilla, call `rive.cleanup()` when removing

## Quick decision guide

| Need | Reach for |
|---|---|
| Static playback animation | Lottie (simpler, more designers) |
| Hover/click responsive button | Rive — its sweet spot |
| Multi-state loader (loading/success/error) | Rive state machine |
| Cursor-following mascot | Rive with cursor inputs |
| Scroll-driven scene with branching | Rive + Lenis/ScrollTrigger |
| Form submission animation that branches | Rive triggers |
| Many concurrent instances | `@rive-app/webgl` |

## Related

`lottie-runtime` (sibling — pick by interactivity need), `motion-dev` (React state plumbing around Rive inputs), `gsap-scrolltrigger` (drive Rive inputs from scroll progress).
