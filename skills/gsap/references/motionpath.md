# MotionPath plugin

Animate any object along a path — SVG `<path>`, an array of coordinates, or a Bezier curve.

## Registration
```js
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
gsap.registerPlugin(MotionPathPlugin);
```

## Along an SVG path
```js
gsap.to(".rocket", {
  duration: 5,
  ease: "none",
  motionPath: {
    path: "#flight-path",         // CSS selector for an SVG <path>
    align: "#flight-path",        // align coordinate spaces (important for HTML elements over SVG)
    alignOrigin: [0.5, 0.5],      // center the rocket on the path
    autoRotate: true,             // rotate to match path tangent
    start: 0,
    end: 1,
  },
});
```

## Along an array of points
```js
gsap.to(".ball", {
  duration: 3,
  motionPath: {
    path: [
      { x: 0,   y: 0 },
      { x: 200, y: -100 },
      { x: 400, y: 50 },
      { x: 600, y: 0 },
    ],
    curviness: 1.5,                // 0 = straight lines, 1+ = smooth bezier
    type: "cubic",                 // or "soft"
  },
});
```

## Convert SVG coordinates to element coordinates
If a `<path>` is in an SVG but you're animating an HTML div over it:
```js
MotionPathPlugin.convertToPath("#circle");   // convert circles/rects/lines/polys to paths
```

## Along a path on scroll
```js
gsap.to(".rocket", {
  ease: "none",
  motionPath: { path: "#flight-path", align: "#flight-path", autoRotate: true, alignOrigin: [0.5, 0.5] },
  scrollTrigger: { trigger: "#scene", start: "top top", end: "+=2000", scrub: 1, pin: true },
});
```

## Getting a point without animating
```js
const point = MotionPathPlugin.getPositionOnPath("#path", 0.5, true); // 0..1 along path, true for tangent
// point = { x, y, angle }
```
