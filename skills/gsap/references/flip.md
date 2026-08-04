# Flip plugin

Flip animates between two layout states using the FLIP technique (First, Last, Invert, Play). Record positions before a DOM change, make the change, and Flip animates the difference.

## Registration
```js
import { Flip } from "gsap/Flip";
gsap.registerPlugin(Flip);
```

## Core workflow

```js
const state = Flip.getState(".card");      // 1. FIRST — snapshot current positions/sizes
reorderTheDOM();                             // 2. make any DOM/class/layout change
Flip.from(state, {                           // 3. LAST + INVERT + PLAY
  duration: 0.6,
  ease: "power2.inOut",
  stagger: 0.05,
  absolute: true,                            // takes elements out of flow during animation
  onEnter: els => gsap.from(els, { opacity: 0, scale: 0 }),
  onLeave: els => gsap.to(els, { opacity: 0, scale: 0 }),
});
```

## What Flip handles automatically
- Position changes (grid reordering, filtering, sorting)
- Size changes (expanding cards, masonry relayout)
- Parent changes (moving an element to a different container — tabs, lightbox open)
- Nested elements (`nested: true` option keeps children animating smoothly)

## Typical use cases

**Sort / filter a grid:**
```js
const state = Flip.getState(".item");
items.sort((a, b) => ...);
items.forEach(el => grid.appendChild(el));   // re-append in new order
Flip.from(state, { duration: 0.7, ease: "power3.inOut", stagger: 0.02 });
```

**Expand-to-detail (shared element transition):**
```js
const state = Flip.getState(".thumbnail");
thumbnail.classList.add("expanded");         // CSS changes size/position
Flip.from(state, { duration: 0.8, ease: "expo.out" });
```

**Tab content swap:**
```js
const state = Flip.getState(".tab-content", { props: "opacity" });
tabContent.textContent = newContent;
Flip.from(state, { duration: 0.4, absolute: true });
```

## Options worth knowing
- `absolute: true` — position elements absolutely during flight so layout doesn't reflow mid-animation (essential when reordering)
- `scale: true` — animate with `scale` instead of `width`/`height` (cheaper, but distorts children)
- `nested: true` — correctly handle nested flipping elements
- `props: "backgroundColor,borderRadius"` — also animate these CSS props between states
- `targets: ".item"` — if element references changed between states (rare, but matters for frameworks)
- `onEnter` / `onLeave` — callbacks for elements that weren't in the original state or aren't in the new one (React list diffs)

## React gotcha

When items come and go via React rendering, call `Flip.getState` in a `useLayoutEffect` **before** the state update, store the state in a ref, then in the next `useLayoutEffect` after render, call `Flip.from(stateRef.current, ...)`. Or use `useGSAP` with a dependency on the list — see `frameworks.md`.
