---
name: react-spring
description: >-
  Physics-based UI + 3D animation for React with react-spring (a.k.a.
  @react-spring/web, @react-spring/three, react spring, pmndrs spring). Fire this
  whenever you animate React with spring physics instead of CSS transitions or
  keyframe/duration tweens: fade/slide/scale entrances, staggered lists
  (useTrail), mount/enter/leave and route/page transitions (useTransition),
  sequenced timelines (useChain), draggable cards / sliders / pull-to-dismiss
  via @use-gesture/react, and declarative react-three-fiber mesh/material
  animation via @react-spring/three. Reach for it for immersive, award-style,
  scroll-driven, gesture, WebGL/3D, and "make it feel premium / natural / bouncy"
  motion work in React and Next.js. Prefer this over hand-rolled requestAnimationFrame
  or CSS when the motion should respond to interruption and feel real.
---

# React Spring

React Spring is a spring-physics-first animation library for React. Instead of "animate over 300ms with an ease-out curve," you describe a target value and the physical properties of the spring that chases it. The result feels natural because real objects don't move on fixed timelines either.

## Why springs beat duration + easing

A duration/easing tween commits to a fixed path and a fixed end time. If the target changes mid-flight (the user clicks again, a new value arrives), you either wait for the tween to finish or hard-cut and restart, and the restart is visible as a stutter.

A spring has no set duration or curve. It always chases its current goal value from wherever it is, at whatever velocity it currently has. Change the goal mid-animation and it re-targets smoothly, carrying momentum. That interruptibility is what makes UI feel responsive and physical rather than scripted. Andy Matuschak's line, quoted in the docs, sums it up: "Animation APIs parameterized by duration and curve are fundamentally opposed to continuous, fluid interactivity."

Use `mass`, `tension`, and `friction` to shape feel. Reach for `duration` + `easing` only when you genuinely need a timed curve (steps, CSS-keyframe parity); mixing the two on one value is a smell.

## Quick start

```bash
npm install @react-spring/web
# 3D target:      npm install @react-spring/three @react-three/fiber three
# gestures:       npm install @use-gesture/react
```

Two things do all the work: the `useSpring` hook produces animated values, and the `animated.*` element applies them without re-rendering React on every frame.

```jsx
import { useSpring, animated } from '@react-spring/web'

function FadeIn({ children }) {
  const styles = useSpring({ from: { opacity: 0, y: 24 }, to: { opacity: 1, y: 0 } })
  return <animated.div style={styles}>{children}</animated.div>
}
```

`animated.div` writes the spring values straight to the DOM node each frame, so the component function runs once, not 60 times a second. Any host element works (`animated.div`, `animated.span`, `animated.path`, `animated.button`).

## The hooks, at a glance

| Hook | Use it for |
| --- | --- |
| `useSpring` | One set of animated values. The flagship hook. |
| `useSprings` | N independent springs sharing one imperative API. |
| `useTrail` | Same as `useSprings` but auto-staggered one after another. |
| `useTransition` | Animating items in/out of a list or the DOM (mount/enter/leave/update). |
| `useChain` | Sequencing whole hooks (e.g. a `useSpring` then a `useTransition`). |

Every hook takes the same config shape: `from`, `to`, `config`, `delay`, `loop`, `pause`, `reset`, `reverse`, `immediate`, `ref`, plus event callbacks.

## Static vs imperative form

Pass a **config object** and the hook animates on mount / whenever the object's values change with render. This is the declarative form.

Pass a **function returning the config** (plus a deps array) and you get back `[springs, api]`. The `api` is a `SpringRef` you drive imperatively with `api.start(...)`, without re-rendering React. Use the function form for anything event-driven (clicks, gestures, scroll), 3D, and performance-sensitive paths.

```jsx
// declarative: re-animates when `open` changes
const styles = useSpring({ height: open ? 200 : 0 })

// imperative: drive it from a handler, no state churn
const [styles, api] = useSpring(() => ({ height: 0 }), [])
api.start({ height: 200 })
```

## Recipe 1: imperative toggle with a SpringRef

`useSpringRef` gives you a stable handle to start/stop a spring from event handlers. `api.start` accepts a partial update and merges its `config`, so you can vary feel per interaction.

```jsx
import { useRef } from 'react'
import { useSpring, animated } from '@react-spring/web'

function ToggleBox() {
  const open = useRef(false)
  const [styles, api] = useSpring(() => ({ x: 0, config: { tension: 210, friction: 20 } }), [])

  const toggle = () => {
    api.start({
      x: open.current ? 0 : 200,
      config: { friction: open.current ? 20 : 10 }, // merged over the base config
      onRest: () => { open.current = !open.current },
    })
  }
  return <animated.div onClick={toggle} style={styles}>Click me</animated.div>
}
```

`SpringRef` methods (from the imperative API): `start`, `set` (jump without animating), `stop(cancel?, keys?)`, `pause(keys?)`, `resume(keys?)`, `update` (queue props), `add`, `delete`. `set` is the escape hatch when you want an instant value change.

## Recipe 2: interpolate values with to()

Springs animate raw numbers; `to()` maps them into transforms, colors, or any string. Interpolate on the `SpringValue` (the `.to` method) or with the standalone `to` import to combine several values.

```jsx
import { useSpring, animated, to } from '@react-spring/web'

function Spinner() {
  const { x } = useSpring({ from: { x: 0 }, to: { x: 1 }, loop: true })
  return (
    <animated.div
      style={{
        // range -> output, then format
        opacity: x.to([0, 1], [0.3, 1]),
        transform: to([x], v => `rotateZ(${v * 360}deg) scale(${1 + v * 0.2})`),
      }}
    />
  )
}
```

Interpolating a spring is cheaper than adding another spring: one physics simulation drives many derived values. Chain `.to(...).to(...)` to remap then format. Prefer animating `transform`/`opacity` over layout props (see Pitfalls).

## Recipe 3: staggered list with useTrail

`useTrail` shares `useSprings`' signature but orchestrates the springs so each lags the previous one, giving a cascade for free.

```jsx
import { useTrail, animated } from '@react-spring/web'

function List({ items }) {
  const trail = useTrail(items.length, {
    from: { opacity: 0, x: 20 },
    to:   { opacity: 1, x: 0 },
    config: { tension: 180, friction: 14 }, // wobbly-ish
  })
  return trail.map((style, i) => (
    <animated.div key={items[i].id} style={style}>{items[i].label}</animated.div>
  ))
}
```

## Recipe 4: mount / enter / leave with useTransition

`useTransition` animates items into and out of the DOM. It tracks each datum by key, holds leaving items on screen until their `leave` animation finishes, then unmounts them. The returned function is a render prop receiving `(style, item)`.

```jsx
import { useTransition, animated } from '@react-spring/web'

function Notifications({ items }) {
  const transitions = useTransition(items, {
    keys: item => item.id,          // stable keys matter (see Pitfalls)
    from:  { opacity: 0, height: 0 },
    enter: { opacity: 1, height: 60 },
    leave: { opacity: 0, height: 0 },
    trail: 80,                      // stagger between items
  })
  return transitions((style, item) => (
    <animated.div style={style}>{item.text}</animated.div>
  ))
}
```

Config keys: `from`, `enter`, `leave`, `update` (for items that stay but change), `initial` (first-mount override of `from`), `keys`, `sort`, `trail`, `exitBeforeEnter`, `expires`. For **route / page transitions**, drive it off a single-element array keyed by the current route, with `exitBeforeEnter` so the outgoing page finishes before the incoming one enters:

```jsx
const transitions = useTransition(location.pathname, {
  from:  { opacity: 0, y: 12 },
  enter: { opacity: 1, y: 0 },
  leave: { opacity: 0, y: -12 },
  exitBeforeEnter: true,
})
return transitions((style, path) => (
  <animated.main style={style}><Routes location={path}>{/* ... */}</Routes></animated.main>
))
```

## Recipe 5: sequence hooks with useChain

`useChain` runs whole hooks one after another. Give each hook a `useSpringRef`, wire it via the hook's `ref` prop, then pass the refs in order. By default the next hook starts when the previous comes to rest.

```jsx
import { useSpring, useTransition, useChain, useSpringRef, animated } from '@react-spring/web'

function Menu({ open, items }) {
  const boxRef = useSpringRef()
  const box = useSpring({ ref: boxRef, width: open ? 240 : 0 })

  const listRef = useSpringRef()
  const list = useTransition(open ? items : [], {
    ref: listRef,
    from: { opacity: 0, x: -10 }, enter: { opacity: 1, x: 0 }, leave: { opacity: 0 },
    trail: 60,
  })

  // container opens first, then items stagger in; reversed order on close
  useChain(open ? [boxRef, listRef] : [listRef, boxRef], [0, open ? 0.3 : 0.6])

  return (
    <animated.div style={{ width: box.width, overflow: 'hidden' }}>
      {list((style, item) => <animated.div style={style}>{item.label}</animated.div>)}
    </animated.div>
  )
}
```

The optional second arg is timesteps in `0..1`; each timestep times the timeframe (default 1000ms) becomes that ref's delay. `useChain` needs refs on hooks that have already been declared, so it must appear after them.

## Recipe 6: draggable card with @use-gesture

`@use-gesture/react` reads pointer/touch gestures; react-spring moves the element. The gesture hook only hands you data, so pipe `movement` into `api.start` and set `immediate: down` so the element tracks the finger 1:1 while held, then springs back on release.

```jsx
import { useSpring, animated } from '@react-spring/web'
import { useDrag } from '@use-gesture/react'

function DraggableCard() {
  const [{ x, y }, api] = useSpring(() => ({ x: 0, y: 0 }))
  const bind = useDrag(({ down, movement: [mx, my] }) => {
    api.start({ x: down ? mx : 0, y: down ? my : 0, immediate: down })
  })
  return <animated.div {...bind()} style={{ x, y, touchAction: 'none' }} />
}
```

`useDrag` returns a `bind` function; spreading `{...bind()}` attaches the pointer handlers. The same shape works for `usePinch` (`offset` scale), `useWheel`, and `useScroll` from the same package. Set `touchAction: 'none'` on draggable elements so the browser doesn't hijack the gesture for scrolling.

## Recipe 7: animate a 3D mesh with @react-spring/three

`@react-spring/three` registers `animated` versions of the react-three-fiber elements, so you animate mesh transforms and material props declaratively. Spring physics on `mass`/`tension`/`friction` reads as real motion in a 3D scene, and re-targeting mid-flight (a metal sphere reacting to a new force) stays seamless.

```jsx
import { useSpring, animated } from '@react-spring/three'
import { Canvas } from '@react-three/fiber'

function Box() {
  const [hovered, setHovered] = useState(false)
  const { scale, color } = useSpring({
    scale: hovered ? 1.4 : 1,
    color: hovered ? '#569AFF' : '#ff6d6d',
    config: { mass: 4, friction: 10 }, // bouncy
  })
  return (
    <animated.mesh scale={scale} onPointerOver={() => setHovered(true)} onPointerOut={() => setHovered(false)}>
      <boxGeometry />
      <animated.meshStandardMaterial color={color} />
    </animated.mesh>
  )
}

export default () => (
  <Canvas>
    <ambientLight intensity={0.8} />
    <pointLight position={[0, 6, 0]} />
    <Box />
  </Canvas>
)
```

To animate a third-party material, wrap it once: `const AnimatedMat = animated(MeshDistortMaterial)`. For per-frame follow-the-cursor motion drive the imperative `api.start` from pointer events instead of React state, so no render fires. Deeper R3F + gesture patterns live in [references/three-and-gestures.md](references/three-and-gestures.md).

## Config: presets and custom springs

Import the `config` presets or hand-tune the physics. Empty config falls back to the default `{ mass: 1, tension: 170, friction: 26 }`.

```jsx
import { useSpring, config } from '@react-spring/web'

useSpring({ x: 1, config: config.wobbly })     // named preset
useSpring({ x: 1, config: { mass: 5, tension: 120, friction: 120 } }) // custom
```

Verified presets:

| Preset | tension / friction | Feel |
| --- | --- | --- |
| `default` | 170 / 26 | balanced |
| `gentle` | 120 / 14 | soft, slow settle |
| `wobbly` | 180 / 12 | overshoots, playful |
| `stiff` | 210 / 20 | snappy |
| `slow` | 280 / 60 | heavy, deliberate |
| `molasses` | 280 / 120 | very heavy |

Other useful `config` props: `clamp: true` stops dead at the goal (kills overshoot), `precision` (default `0.01`) controls when a spring is considered at rest, `bounce`, `velocity`, `decay`. `config` can also be a function of the spring key, so one hook can give `opacity` a smooth feel and `scale` a bouncy one in the same call.

## Events

React to animation lifecycle with callbacks in the config. Each can be a single function or an object keyed by spring value.

```jsx
useSpring({
  x: 1,
  onStart:  (result, spring) => {},   // after the first tick (value is "dirty")
  onChange: (result, spring) => {},   // every frame
  onRest:   (result, spring) => {},   // settled at goal
})
```

Also available: `onPause`, `onResume`, `onResolve`, `onProps`, and (transitions only) `onDestroyed`. The `result` carries `{ value, finished, cancelled }`. In `useTransition` these callbacks receive the `item` as a third argument.

## React / Next.js integration

The hooks are ordinary client hooks, so in the Next.js App Router put animated components in files marked `'use client'`. There's nothing to clean up manually: unmounting a component disposes its springs, and `useTransition` handles the mount/unmount lifecycle of its own items. For imperative springs created with the function form, the deps array behaves like `useEffect` deps, so recreate the animation only when its inputs change. Passing `ref` targets to SSR is fine because animation only starts on the client after hydration.

## Performance

- Prefer the imperative `api.start` for anything firing rapidly (drag, scroll, pointer-move). It updates the animated node directly and skips React renders.
- Animate `transform` and `opacity`, which the compositor handles off the main thread. Animating `width`, `height`, `top`, or `left` forces layout every frame (see Pitfalls).
- One spring plus `to()` interpolations is cheaper than many springs. Derive multiple visual values from a single simulation.
- On 3D scenes, if animation appears to skip its final frames, lower `config.precision` (e.g. `0.0001`); the default `0.01` can settle visibly early for three.js values.

## Accessibility (prefers-reduced-motion)

Respect the OS "reduce motion" setting. `useReducedMotion` reads the preference and, called once near the app root, sets react-spring's global `skipAnimation` so every spring jumps straight to its goal instead of animating.

```jsx
import { useReducedMotion } from '@react-spring/web'

export default function App({ children }) {
  useReducedMotion() // wires prefers-reduced-motion -> Globals.skipAnimation
  return children
}
```

If you need to force it yourself (e.g. a "disable animations" toggle), assign the global directly. Set it back to `false` on cleanup so it doesn't leak across mounts:

```jsx
import { Globals } from '@react-spring/web'

useEffect(() => {
  Globals.assign({ skipAnimation: true })
  return () => Globals.assign({ skipAnimation: false })
}, [])
```

`skipAnimation` behaves like setting `immediate: true` on every spring: values still update, they just don't tween.

## Pitfalls

- **Animating layout props instead of transform.** `height`/`width`/`top`/`left` trigger reflow on every frame and stutter. Animate `transform` (`x`/`y`/`scale`) and `opacity` instead. When you truly must animate size (an accordion), expect the cost and consider `will-change` or a clip-based approach.
- **Unstable keys in useTransition.** The hook diffs items by key to decide enter vs leave. Array-index keys, or new object identities every render, make it think everything left and re-entered, so items flash or animate wrongly. Pass a stable `keys={item => item.id}`.
- **useChain refs declared out of order.** `useChain` only orchestrates hooks that already exist and carry a matching `ref`. Declare the `useSpring`/`useTransition` hooks (with their `useSpringRef`) *before* the `useChain` call, or the sequence silently does nothing.
- **Mixing spring physics with `duration`.** Setting `config.duration` switches that value to a timed easing and discards tension/friction. Pick one model per value; don't set both and expect them to blend.
- **Reading a spring value on the JS side directly.** Animated values live outside React state. To read the current number use `springValue.get()`; don't expect a plain number from `styles.x` in render.
- **Forgetting `touchAction: 'none'` on draggables.** Without it, mobile browsers claim the gesture for scrolling and the drag feels broken.

## References

Official docs fetched July 2026:

- Overview & hooks: https://www.react-spring.dev/docs
- useSpring: https://www.react-spring.dev/docs/components/use-spring
- useSprings: https://www.react-spring.dev/docs/components/use-springs
- useTrail: https://www.react-spring.dev/docs/components/use-trail
- useTransition: https://www.react-spring.dev/docs/components/use-transition
- useChain: https://www.react-spring.dev/docs/components/use-chain
- Interpolation / to(): https://www.react-spring.dev/docs/advanced/interpolation
- Spring configs & presets: https://www.react-spring.dev/docs/advanced/config
- Events: https://www.react-spring.dev/docs/advanced/events
- SpringRef (imperative API): https://www.react-spring.dev/docs/advanced/spring-ref
- useReducedMotion & skipAnimation: https://www.react-spring.dev/docs/utilities/use-reduced-motion
- react-three-fiber guide: https://www.react-spring.dev/docs/guides/react-three-fiber
- @use-gesture: https://use-gesture.netlify.app/docs/
- Repo: https://github.com/pmndrs/react-spring
