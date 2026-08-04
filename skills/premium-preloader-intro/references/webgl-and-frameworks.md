# WebGL preloading and fuller framework patterns

Advanced companions to the main skill. Read the SKILL.md recipes first; these
extend recipe 1 (real progress) to 3D assets and recipe 4/React integration to
the Next.js App Router.

## Preloading a Three.js / WebGL hero

A WebGL hero's real cost is GLTF meshes, textures, and shader compile — none of
which a DOM `img` loader sees. Track them with Three's own
`THREE.LoadingManager`, which reports real per-item progress, and fold that
fraction into the same counter.

```js
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

export function preloadScene({ models = [], textures = [], onProgress }) {
  const manager = new THREE.LoadingManager();

  // onProgress fires per finished item with real loaded/total counts
  manager.onProgress = (_url, loaded, total) => onProgress?.(loaded / total);

  const gltfLoader = new GLTFLoader(manager);
  const texLoader = new THREE.TextureLoader(manager);

  // loadAsync returns promises; the manager still tracks aggregate progress
  return Promise.all([
    ...models.map((url) => gltfLoader.loadAsync(url)),
    ...textures.map((url) => texLoader.loadAsync(url)),
  ]);
}
```

`manager.onProgress` gives honest counts, and `loadAsync` gives you the decoded
assets to add to the scene. Use both: the manager drives the counter, the
resolved promises populate the hero.

Two costs the manager does NOT cover, so account for them before you reveal:

- **Shader compile.** First render of a material can hitch. Warm it by rendering
  one hidden frame (`renderer.compile(scene, camera)`) inside the loader, so the
  reveal frame is already warm.
- **Draco/KTX2 decoders.** If you use `DRACOLoader` or `KTX2Loader`, their
  decoder wasm is itself an asset — set the decoder path and let it load before
  you count the GLTF as done.

## Weighted progress across mixed asset types

When one asset dwarfs the rest, equal weighting makes the counter crawl then
snap. Assign weights (rough byte estimates are fine) and sum weighted fractions.

```js
// each source: { load: () => Promise, weight: number }
export function weightedPreload(sources, onProgress) {
  const totalWeight = sources.reduce((s, x) => s + x.weight, 0);
  const progress = new Array(sources.length).fill(0);

  const report = () => {
    const done = progress.reduce((s, p, i) => s + p * sources[i].weight, 0);
    onProgress?.(done / totalWeight);
  };

  return Promise.all(
    sources.map((src, i) =>
      src.load((p01) => { progress[i] = p01; report(); }) // src reports 0..1
        .then(() => { progress[i] = 1; report(); })
    )
  );
}
```

For assets that can report sub-progress (XHR `onprogress`, `LoadingManager`),
feed the 0..1 through. For all-or-nothing assets, they simply jump 0 -> 1 when
resolved. Either way the aggregate is honest.

## Next.js App Router pattern

Keep the preloader a client island over server-rendered content. The hero is a
server component (good for LCP); the overlay is a sibling client component that
never blocks it.

```jsx
// app/page.jsx  (server component — hero renders on the server)
import Hero from "@/components/Hero";
import Preloader from "@/components/Preloader";

export default function Page() {
  return (
    <>
      <Hero />           {/* LCP element, server-rendered, painting underneath */}
      <Preloader />      {/* client island, fixed overlay on top */}
    </>
  );
}
```

```jsx
// components/Preloader.jsx
"use client";
import { useEffect, useRef, useState } from "react";
import { gsap } from "gsap";
import Lenis from "lenis";
import { preloadAssets } from "@/lib/preload";

const HERO_IMAGES = ["/hero.jpg", "/texture.webp"];

export default function Preloader() {
  const root = useRef(null);
  const [count, setCount] = useState(0);

  useEffect(() => {
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    const seen = sessionStorage.getItem("intro-seen");
    const lenis = new Lenis({ autoRaf: true });

    if (reduce || seen) {
      gsap.set(".preloader", { display: "none" });
      return () => lenis.destroy();
    }

    lenis.stop();
    document.documentElement.classList.add("is-loading");
    const started = performance.now();

    const ctx = gsap.context(() => {
      preloadAssets({
        images: HERO_IMAGES,
        onProgress: (p) => setCount(Math.round(p * 100)),
      }).then(async () => {
        const elapsed = performance.now() - started;
        if (elapsed < 900) await new Promise((r) => setTimeout(r, 900 - elapsed));
        sessionStorage.setItem("intro-seen", "1");
        gsap.timeline({
          onStart: () => {
            document.documentElement.classList.remove("is-loading");
            lenis.start();
          },
        }).to(".preloader", { clipPath: "inset(0 0 100% 0)", duration: 1.1, ease: "expo.inOut" });
      });
    }, root);

    return () => { ctx.revert(); lenis.destroy(); };
  }, []);

  return (
    <div ref={root} className="preloader" aria-hidden="true">
      <span className="preloader__count">{count}</span>
    </div>
  );
}
```

Notes specific to the App Router:

- Mark only the overlay `"use client"`. The hero stays a server component so its
  markup and LCP image ship in the initial HTML.
- `gsap.context(fn, root)` scopes selectors and, via `ctx.revert()`, tears down
  every tween on unmount — essential across client-side route changes, which do
  NOT reload the page.
- Route transitions do not remount the tree the way a hard load does. If you want
  the loader only on true first paint, `sessionStorage` is correct; for a
  per-route transition instead, use a route-change animation (a different tool)
  rather than this full-asset preloader.
- Never read `window` / `navigator` / `document` at module scope in a client
  component that Next may still evaluate during SSR — keep them inside
  `useEffect`.

## Verifying it is honest

The proof that the counter is real: throttle the network in DevTools (Slow 3G)
and watch the number climb gradually across the actual asset loads, then hit 100
exactly as the wipe starts. On a cached reload it should race to 100 fast and
the `MIN_MS` floor should still hold the overlay briefly. If the number moves
identically regardless of network throttling, it is a fake timer — fix it.
