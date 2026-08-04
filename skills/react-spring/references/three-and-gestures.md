# React Spring: deeper 3D + gesture patterns

Extends the main SKILL. Everything here is grounded in the official react-three-fiber guide and the @use-gesture docs.

## Imperative R3F: move a mesh without React renders

Inside a `<Canvas>`, driving `api.start` from pointer events (not React state) means the scene graph updates every frame with zero React reconciliation. This is the pattern for cursor-follow, hover-scale, and physics-feel blobs.

Key moves in this example:

- Function form of `useSpring` returns `[springs, api]`.
- `config` is a **function of the spring key** so `scale` gets a bouncy spring while `position` gets a heavy, sticky one.
- Mouse position is a 2D vector but a mesh `position` is 3D, so a `to()` interpolation adapts the array.

```jsx
import { useRef, useEffect, useCallback } from 'react'
import { useSpring, animated } from '@react-spring/three'
import { Canvas, useThree } from '@react-three/fiber'
import { MeshDistortMaterial } from '@react-three/drei'

const AnimatedMeshDistortMaterial = animated(MeshDistortMaterial)

function Blob() {
  const isOver = useRef(false)
  const { width, height } = useThree(state => state.size)

  const [springs, api] = useSpring(() => ({
    scale: 1,
    position: [0, 0, 0],
    color: '#ff6d6d',
    config: key => {
      switch (key) {
        case 'scale':    return { mass: 4, friction: 10 }   // bouncy
        case 'position': return { mass: 4, friction: 220 }  // sticky/heavy
        default:         return {}
      }
    },
  }), [])

  const onMove = useCallback(e => {
    if (!isOver.current) return
    const x = (e.offsetX / width) * 2 - 1
    const y = (e.offsetY / height) * -2 + 1
    api.start({ position: [x * 5, y * 2, 0] })
  }, [api, width, height])

  useEffect(() => {
    const over = () => { isOver.current = true }
    const out  = () => { isOver.current = false; api.start({ position: [0, 0, 0] }) }
    window.addEventListener('pointerover', over)
    window.addEventListener('pointerout', out)
    window.addEventListener('pointermove', onMove)
    return () => {
      window.removeEventListener('pointerover', over)
      window.removeEventListener('pointerout', out)
      window.removeEventListener('pointermove', onMove)
    }
  }, [api, onMove])

  return (
    <animated.mesh
      scale={springs.scale}
      position={springs.position}
      onPointerEnter={() => api.start({ scale: 1.5 })}
      onPointerLeave={() => api.start({ scale: 1 })}
      onClick={() => api.start({ color: '#569AFF' })}
    >
      <sphereGeometry args={[1.5, 64, 32]} />
      <AnimatedMeshDistortMaterial speed={5} distort={0.5} color={springs.color} />
    </animated.mesh>
  )
}

export default function Scene() {
  return (
    <Canvas>
      <ambientLight intensity={0.8} />
      <pointLight intensity={1} position={[0, 6, 0]} />
      <Blob />
    </Canvas>
  )
}
```

Why springs here instead of `useFrame` + `THREE.Color.lerp`: react-spring animations are physically correct and interruptible, you don't hand-manage a `THREE.Color` instance or write easing, and re-targeting mid-flight stays seamless (objects don't stall when a new force arrives). If the tail of a 3D animation looks like it skips frames, drop `config.precision` to `0.0001` (default `0.01` settles visibly early for three.js values).

## Wrapping any third-party material or object

`animated()` upgrades any component/material to accept `SpringValue`s:

```jsx
const AnimatedMat = animated(MeshDistortMaterial)
// then <AnimatedMat color={springs.color} />
```

The same wrapper works for lights, groups, and imported objects. Built-in R3F elements (`mesh`, `group`, `meshStandardMaterial`, `pointLight`, …) already exist as `animated.mesh` etc. once you import from `@react-spring/three`.

## Gestures beyond drag

`@use-gesture/react` is platform-agnostic input; react-spring does the moving. All hooks return a `bind` you spread with `{...bind()}`.

Pinch to scale (offset carries absolute accumulated scale):

```jsx
import { useSpring, animated } from '@react-spring/web'
import { usePinch } from '@use-gesture/react'

function Pinchable() {
  const [{ scale }, api] = useSpring(() => ({ scale: 1 }))
  const bind = usePinch(({ offset: [s] }) => api.start({ scale: s }))
  return <animated.div {...bind()} style={{ scale, touchAction: 'none' }} />
}
```

Wheel / scroll drive the same way with `useWheel` and `useScroll` from the same package. Combine multiple gestures on one element with `useGesture({ onDrag, onPinch, onWheel })`.

Notes:

- `@use-gesture` never moves anything itself; it hands gesture data to your `api.start`. Keep that split clear.
- Use `movement` for delta-from-gesture-start and `offset` for absolute accumulated value across gestures.
- Set `immediate: down` (or `immediate: active`) so the element tracks the pointer 1:1 while held, then animates on release when `immediate` is false.
- Always set `touchAction: 'none'` on gesture targets so the browser doesn't steal the touch for scrolling.

## Vanilla / class-component driving

Outside hooks, construct the imperative pieces directly: `SpringRef()` for the ref and `new Controller({ ...values, ref })` for the animated state, then call `controller.start(...)` and render `controller.springs`. Useful in class components or non-React glue. Prefer the `useSpringRef` hook in function components.
