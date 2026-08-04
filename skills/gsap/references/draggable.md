# Draggable (+ InertiaPlugin)

Draggable makes elements draggable with physics-based throws when paired with InertiaPlugin (now free).

## Registration
```js
import { Draggable } from "gsap/Draggable";
import { InertiaPlugin } from "gsap/InertiaPlugin";
gsap.registerPlugin(Draggable, InertiaPlugin);
```

## Basic drag
```js
Draggable.create(".box", {
  type: "x,y",                  // or "x", "y", "rotation", "scrollLeft", "scrollTop"
  bounds: ".container",          // constrain inside this element (or object {top, left, width, height})
  inertia: true,                 // smooth throw after release
  edgeResistance: 0.65,          // 0..1, how much bounds resist (lower = springier)
  onDrag() { console.log(this.x, this.y); },
  onDragEnd() {},
  onThrowUpdate() {},
  onThrowComplete() {},
});
```

## Snap to grid
```js
Draggable.create(".card", {
  type: "x,y",
  inertia: true,
  snap: {
    x: value => Math.round(value / 100) * 100,    // snap to nearest 100
    y: value => Math.round(value / 100) * 100,
  },
});
```

## Rotate knob
```js
Draggable.create(".knob", {
  type: "rotation",
  inertia: true,
  snap: value => Math.round(value / 15) * 15,      // snap to 15° increments
});
```

## Carousel / slider
```js
Draggable.create(".track", {
  type: "x",
  inertia: true,
  bounds: { minX: -2000, maxX: 0 },
  snap: { x: gsap.utils.snap(200) },                // snap to every 200px
});
```

## Scrolling a custom container
```js
Draggable.create(".scroll-area", {
  type: "scrollTop",             // drag scrolls this element
  edgeResistance: 0.85,
  inertia: true,
});
```

## Useful instance properties/methods
- `draggable.x`, `draggable.y`, `draggable.rotation` — current values
- `draggable.startDrag(event)` — programmatically start
- `draggable.endDrag(event)`
- `draggable.disable()` / `.enable()`
- `draggable.applyBounds(newBounds)`
- `draggable.update()` — re-measure if target moved externally

## Gotchas
- Draggable sets `touch-action: none` on the element to prevent browser gestures from interfering. If you need touch scrolling on a parent, design accordingly.
- Inside a scroll container, combine with `dragClickables: false` to avoid hijacking clicks on interactive children.
- For knobs: set `transform-origin: center center` in CSS.
