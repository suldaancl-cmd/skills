# Framework integration

The unifying rule: **animations are side effects**. Create them after mount, clean them up on unmount, scope selectors to the component, and never animate React/Vue/Svelte state through GSAP — animate the DOM directly.

## React — use `@gsap/react`

```bash
npm install gsap @gsap/react
```

`useGSAP` is a drop-in hook that handles:
- StrictMode double-mount (no duplicate tweens in dev)
- Cleanup on unmount (`.revert()` — removes all animations and restores original styles)
- Scoped selectors so `"."` selectors only match inside this component

```jsx
"use client";
import { useRef } from "react";
import { useGSAP } from "@gsap/react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(useGSAP, ScrollTrigger);

export function Hero() {
  const container = useRef(null);

  useGSAP(() => {
    // Selectors here are scoped to `container`
    gsap.from(".title", { y: 100, opacity: 0, duration: 1, ease: "power3.out" });

    gsap.from(".card", {
      y: 40, opacity: 0, stagger: 0.1,
      scrollTrigger: { trigger: ".cards", start: "top 80%" },
    });
  }, { scope: container });   // scope limits queries and auto-reverts on unmount

  return (
    <section ref={container}>
      <h1 className="title">Hi</h1>
      <div className="cards">
        <div className="card" />
        <div className="card" />
      </div>
    </section>
  );
}
```

### useGSAP with dependencies (re-run on change)
```jsx
useGSAP(() => {
  gsap.to(".bar", { width: `${progress}%`, duration: 0.4 });
}, { scope: container, dependencies: [progress] });
```

### Getting a context for manual control
```jsx
const { context, contextSafe } = useGSAP({ scope: container });

const onClick = contextSafe(() => {      // ensures cleanup tracking
  gsap.to(".box", { x: 200 });
});

return <button onClick={onClick}>Go</button>;
```

### Next.js App Router specifics
- Mark the component `"use client"` — GSAP touches the DOM.
- Register plugins once at the top of the file (idempotent).
- For route-change cleanup on a long-lived layout, inside `useGSAP` you rarely need to do more — `revert()` runs on unmount.
- `ScrollTrigger.refresh()` after route changes if you have pinned sections elsewhere: call from a `usePathname()` effect.

## Vue 3 — Composition API

```vue
<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

const root = ref(null);
let ctx;

onMounted(() => {
  ctx = gsap.context(() => {
    gsap.from(".title", { y: 80, opacity: 0, duration: 1 });
    gsap.from(".card", {
      y: 40, opacity: 0, stagger: 0.1,
      scrollTrigger: { trigger: ".cards", start: "top 80%" },
    });
  }, root.value);   // scope
});

onUnmounted(() => ctx?.revert());
</script>

<template>
  <section ref="root">
    <h1 class="title">Hi</h1>
    <div class="cards"><div class="card" /><div class="card" /></div>
  </section>
</template>
```

`gsap.context()` is the Vue/Svelte equivalent of `useGSAP` — scopes selectors and collects every animation for one-call cleanup.

## Svelte

```svelte
<script>
  import { onMount, onDestroy } from "svelte";
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  gsap.registerPlugin(ScrollTrigger);

  let root;
  let ctx;

  onMount(() => {
    ctx = gsap.context(() => {
      gsap.from(".title", { y: 80, opacity: 0 });
    }, root);
  });

  onDestroy(() => ctx?.revert());
</script>

<section bind:this={root}>
  <h1 class="title">Hi</h1>
</section>
```

## Vanilla JS

```js
document.addEventListener("DOMContentLoaded", () => {
  gsap.from(".title", { y: 80, opacity: 0, duration: 1 });
});
```

For multi-page sites, that's enough. If content loads via fetch/htmx later, run animations inside the insertion callback or use a `MutationObserver`.

## Animating component state vs DOM — important philosophy

Don't pipe GSAP updates back into React/Vue/Svelte state:

```jsx
// ❌ Don't — thrashes the framework
gsap.to({ v: 0 }, { v: 100, onUpdate() { setProgress(this.targets()[0].v); } });
```

```jsx
// ✅ Animate the DOM directly
gsap.to(barRef.current, { width: "100%", duration: 2 });
```

GSAP is already 60fps. Routing every frame through a framework reconciler undoes that.

## Cleanup, one more time

Unmounted components that still have running tweens = memory leaks, zombie ScrollTriggers, broken refs. Always:

- React → `useGSAP` hook, or `const ctx = gsap.context(() => {...}, scopeEl)` in a `useEffect` with `return () => ctx.revert()`.
- Vue/Svelte → `gsap.context()` + `ctx.revert()` on unmount.
- Vanilla dynamic content → store tween refs and call `.kill()` when the element is removed.

`.revert()` is stronger than `.kill()` — it restores all inline styles GSAP applied, which is usually what you want.
