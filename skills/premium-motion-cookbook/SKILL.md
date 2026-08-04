---
name: premium-motion-cookbook
description: Use when implementing premium scroll/text/timeline motion with GSAP, ScrollTrigger and Lenis — copy-paste code recipes for the correct Lenis+GSAP ticker wiring, single-progress shader uniforms, SplitText reveals (chars/lines/scramble/clip-path), pinned scrubbed sections with responsive matchMedia, prefers-reduced-motion guards, and React/Next useGSAP setup. GSAP 3.13+ is 100% free (incl. SplitText/MorphSVG/DrawSVG) since the Webflow acquisition — register plugins, no membership token needed.
---

# Premium Motion Cookbook (GSAP 3.13+ · ScrollTrigger · Lenis 1.3+)

Working snippets. GSAP 3.13+ is free including SplitText/MorphSVG/DrawSVG — just `registerPlugin`.
Docs: https://gsap.com/docs/v3/ · https://gsap.com/blog/3-13/ · https://lenis.dev · https://github.com/darkroomengineering/lenis

## 0. Install / load

```bash
npm i gsap lenis            # React/Vite/Next also: npm i @gsap/react
```
```html
<!-- CDN — the OLD @studio-freight/lenis CDN 404s. Use these. -->
<script src="https://unpkg.com/gsap@3/dist/gsap.min.js"></script>
<script src="https://unpkg.com/gsap@3/dist/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/gsap@3/dist/SplitText.min.js"></script>
<script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>  <!-- global: Lenis -->
```

## 1. Lenis + GSAP — correct wiring (do this once, app-wide)

Drive Lenis from GSAP's ticker (one RAF loop, no jitter). Do NOT also pass `autoRaf` — let GSAP own the loop.
Source: Lenis README "GSAP ScrollTrigger" — https://github.com/darkroomengineering/lenis#gsap-scrolltrigger

```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Lenis from 'lenis';            // NOT '@studio-freight/lenis'
import 'lenis/dist/lenis.css';        // optional base styles

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({ autoRaf: false });           // GSAP drives RAF, so disable Lenis' own
lenis.on('scroll', ScrollTrigger.update);              // keep triggers in sync with smooth scroll
gsap.ticker.add((time) => lenis.raf(time * 1000));     // GSAP time is seconds → Lenis wants ms
gsap.ticker.lagSmoothing(0);                           // no catch-up jumps after tab refocus
```

CSS Lenis expects (prevents double scrollbars):
```css
html.lenis, html.lenis body { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto !important; }
.lenis.lenis-stopped { overflow: hidden; }
```

## 2. Single-progress → shader uniform

One GSAP tween of a plain `{ v: 0 }` object is the source of truth; copy `obj.v` into a uniform every frame.
Avoids fighting between GSAP and your render loop.

```js
const u = { uProgress: { value: 0 } };  // pass into THREE.ShaderMaterial uniforms

const driver = { v: 0 };
gsap.to(driver, {
  v: 1,
  ease: 'none',
  scrollTrigger: { trigger: '#hero', start: 'top top', end: '+=1500', scrub: 1 },
  onUpdate: () => { u.uProgress.value = driver.v; }  // single value, copied each frame
});
// In your rAF/RenderLoop: material.uniforms.uProgress already updated — just renderer.render(...)
```

Scroll *velocity* into a uniform (cheap "speed lines"/RGB-split):
```js
const vel = { value: 0 };
const st = ScrollTrigger.create({ trigger: '#hero', start: 'top top', end: 'bottom top' });
gsap.ticker.add(() => { vel.value = gsap.utils.clamp(-1, 1, st.getVelocity() / 2000); });
```

## 3. Text reveal — SplitText (lines/chars) + scramble + clip-path wipe

Re-splits on resize via `autoSplit`+`onSplit`; the returned tween is auto-reverted/re-created. Always wait for fonts.
Docs: https://gsap.com/docs/v3/Plugins/SplitText/ · https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/

```js
import { SplitText } from 'gsap/SplitText';
import { ScrambleTextPlugin } from 'gsap/ScrambleTextPlugin';
gsap.registerPlugin(SplitText, ScrambleTextPlugin);

document.fonts.ready.then(() => {                 // MUST wait — splitting pre-font causes reflow/mis-measured lines
  SplitText.create('.headline', {
    type: 'lines, chars',
    mask: 'lines',                                // wraps each line in an overflow:hidden mask (built-in clip-path wipe)
    autoSplit: true,                              // re-split automatically on resize/font-load
    onSplit(self) {                               // return a tween → saved & reverted on each re-split
      return gsap.from(self.lines, {
        yPercent: 110, opacity: 0, duration: 0.9, ease: 'power4.out', stagger: 0.08,
        scrollTrigger: { trigger: '.headline', start: 'top 80%' }
      });
    }
  });
});

// Char scramble-in (decode effect)
document.fonts.ready.then(() => {
  const s = SplitText.create('.scramble', { type: 'chars' });
  gsap.to(s.chars, {
    duration: 1, ease: 'none', stagger: 0.02,
    scrambleText: { text: '{original}', chars: 'upperCase', speed: 0.4 },
    scrollTrigger: { trigger: '.scramble', start: 'top 85%' }
  });
});
```

Manual clip-path wipe (no mask option) — animate the CSS variable:
```css
.wipe { clip-path: inset(0 0 0 var(--w, 100%)); }
```
```js
gsap.to('.wipe', { '--w': '0%', duration: 1, ease: 'power3.inOut',
  scrollTrigger: { trigger: '.wipe', start: 'top 80%' } });
```

## 4. Pinned + scrubbed panels — responsive via matchMedia()

`gsap.matchMedia()` auto-reverts/rebuilds when the query flips. Put ALL ScrollTriggers inside it.
Docs: https://gsap.com/docs/v3/GSAP/Plugins/matchMedia()/ · .../ScrollTrigger/

```js
const mm = gsap.matchMedia();

mm.add(
  { isDesktop: '(min-width: 768px)', isMobile: '(max-width: 767px)', reduce: '(prefers-reduced-motion: reduce)' },
  (ctx) => {
    const { isDesktop, reduce } = ctx.conditions;
    if (reduce) return;                            // see §5 — no pinning for reduced-motion users

    const panels = gsap.utils.toArray('.panel');
    gsap.to(panels, {
      xPercent: -100 * (panels.length - 1),
      ease: 'none',
      scrollTrigger: {
        trigger: '#track',
        pin: true,                                 // lock section while it scrubs
        scrub: 1,                                  // 1s catch-up smoothing
        snap: 1 / (panels.length - 1),             // settle on each panel
        end: () => '+=' + document.querySelector('#track').offsetWidth,
        invalidateOnRefresh: true                  // recompute on resize/orientation
      }
    });
  }
);   // mm.revert() to tear everything down (route change, etc.)
```

## 5. prefers-reduced-motion guard (always ship this)

Kill motion and jump tweens to their end state so layout/content still resolves.

```js
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

function applyMotion() {
  if (reduce.matches) {
    gsap.globalTimeline.timeScale(200);            // fast-forward anything queued
    ScrollTrigger.getAll().forEach((t) => t.kill(false));  // drop pin/scrub, keep elements in place
    gsap.set('[data-animate]', { clearProps: 'all', opacity: 1 }); // static fallback = final state
    return;
  }
  // ...build your animations (call §3/§4 here)...
}
applyMotion();
reduce.addEventListener('change', () => location.reload()); // simplest correct re-eval
```

## 6. React / Next.js — useGSAP() (client-only)

`useGSAP` is a `useLayoutEffect` drop-in that scopes selectors and auto-reverts every tween/ScrollTrigger/SplitText on unmount. Register plugins client-side only (they touch `window`). In Next App Router the file needs `"use client"`.
Docs: https://gsap.com/resources/React/ · https://gsap.com/docs/v3/GSAP/UI/useGSAP/

```jsx
'use client';
import { useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';
import { useGSAP } from '@gsap/react';
import Lenis from 'lenis';

gsap.registerPlugin(useGSAP, ScrollTrigger, SplitText);  // client module — never runs during SSR

export default function Hero() {
  const root = useRef(null);

  useGSAP(() => {
    const lenis = new Lenis({ autoRaf: false });
    lenis.on('scroll', ScrollTrigger.update);
    const tick = (t) => lenis.raf(t * 1000);
    gsap.ticker.add(tick);
    gsap.ticker.lagSmoothing(0);

    const mm = gsap.matchMedia();
    mm.add('(prefers-reduced-motion: no-preference)', () => {
      gsap.from('.title', { yPercent: 40, opacity: 0, duration: 1, ease: 'power3.out',
        scrollTrigger: { trigger: '.title', start: 'top 80%' } });
    });

    return () => { gsap.ticker.remove(tick); lenis.destroy(); };  // cleanup; useGSAP reverts the rest
  }, { scope: root });

  // event-handler tweens created later must be contextSafe:
  const { contextSafe } = useGSAP({ scope: root });
  const onEnter = contextSafe(() => gsap.to('.cta', { scale: 1.05, duration: 0.3 }));

  return (
    <section ref={root}>
      <h1 className="title">Premium motion</h1>
      <button className="cta" onMouseEnter={onEnter}>Get started</button>
    </section>
  );
}
```

## Gotchas
- Plugins are tree-shaken unless `registerPlugin`-ed — register even if "unused" in the bundle.
- After dynamically loading content/images, call `ScrollTrigger.refresh()` (or set `invalidateOnRefresh: true`).
- One Lenis instance per app; one ticker wiring. Don't combine `autoRaf:true` with `gsap.ticker.add` — pick the ticker.
- SplitText needs `document.fonts.ready`; without it lines mis-measure on custom fonts.
- Next.js: anything importing GSAP plugins or Lenis must be a `"use client"` component.
