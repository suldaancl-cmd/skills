---
name: lottie-runtime
description: Use when shipping After-Effects-quality vector animations to web/mobile — loading .json or .lottie files exported via Bodymovin, playing them, controlling playback (scrub, segment, loop), or syncing to scroll/state. Triggers — "Lottie", "Bodymovin", ".lottie file", "After Effects animation on web", "lottiefiles", "play AE animation in browser", "JSON animation", "vector animation web".
---

# Lottie — After Effects animations on the web

Lottie is Airbnb's open format (and runtime ecosystem) for shipping vector animations exported from After Effects (via the **Bodymovin** plugin) or Figma (via LottieFiles plugin). The animation is a JSON file the browser renders as SVG, Canvas, or HTML — pixel-perfect, infinitely scalable, ~5-50KB per animation, hardware-accelerated.

**Key fact (keep current):** The newer **`.lottie` format (dotLottie)** is a zipped bundle containing one or more JSON animations + assets. ~80% smaller than raw `.json`. Use it when you can — `@lottiefiles/dotlottie-web` (vanilla) or `@lottiefiles/dotlottie-react` (React) are the modern runtimes.

## When to reach for Lottie

Use Lottie when:
- A designer hands you an After Effects animation that must look identical on web/iOS/Android
- Hero illustrations, empty states, onboarding flows, loading spinners with personality
- Marketing pages where a brand mascot or product reveal needs to feel hand-crafted
- You need to scrub an animation to scroll position (still cheaper than a video)

**Do NOT use** Lottie for:
- Simple CSS-doable animations (a pulsing dot, a fade-in) — wasted runtime
- Photoreal video — Lottie is vector-only. Use `<video>` or a hero MP4
- Complex 3D — Lottie has no z-axis. Use Three.js / Spline
- High-frequency state-driven animations (button presses, hover) — use CSS / Motion / GSAP, much lower overhead

## Install

### Classic JSON workflow (`lottie-web`)

```bash
npm install lottie-web
```

```js
import lottie from 'lottie-web';
const anim = lottie.loadAnimation({
  container: document.getElementById('lottie'),
  renderer: 'svg',          // 'svg' | 'canvas' | 'html'
  loop: true,
  autoplay: true,
  path: '/animations/hero.json',  // or `animationData: jsonObject`
});
```

### Modern dotLottie workflow (recommended)

```bash
npm install @lottiefiles/dotlottie-web
# or React:
npm install @lottiefiles/dotlottie-react
```

```jsx
import { DotLottieReact } from '@lottiefiles/dotlottie-react';

<DotLottieReact
  src="https://lottie.host/.../hero.lottie"
  loop
  autoplay
  speed={1}
/>
```

dotLottie supports **multi-animation files** (state machines, theme variants) and is dramatically smaller. Prefer it for any new work.

## Renderer choice

| Renderer | Quality | Performance | When |
|---|---|---|---|
| `svg` | Crispest, scales infinitely | Higher CPU on complex animations | Default. Logos, illustrations, sharp icons |
| `canvas` | Good, rasterized at render size | Best perf for many concurrent | Lists of animations, mobile, complex shapes |
| `html` | DOM-driven, scales fine | Slower | Rare. Use when you need DOM-level styling/CSS hooks |

Rule of thumb: SVG for one large hero animation, canvas if you have 10+ animations on screen simultaneously.

## Core API (lottie-web)

```js
const anim = lottie.loadAnimation({ container, renderer, loop, autoplay, animationData });

anim.play();
anim.pause();
anim.stop();
anim.goToAndPlay(0, true);       // frame, true=isFrame (false=isMs)
anim.goToAndStop(60, true);
anim.setSpeed(1.5);
anim.setDirection(-1);            // -1 = reverse
anim.playSegments([0, 60], true); // play frames 0-60
anim.addEventListener('complete', () => {});
anim.destroy();                   // critical — call on unmount
```

## Scroll-linked Lottie (the most-requested pattern)

```js
import lottie from 'lottie-web';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

const anim = lottie.loadAnimation({
  container: el, renderer: 'svg', loop: false, autoplay: false,
  path: '/scroll-anim.json',
});

anim.addEventListener('data_ready', () => {
  const totalFrames = anim.totalFrames;
  ScrollTrigger.create({
    trigger: '.hero', start: 'top top', end: '+=2000', scrub: true,
    onUpdate: (self) => anim.goToAndStop(self.progress * totalFrames, true),
  });
});
```

This scrubs the animation 1:1 with scroll — the "exploded technical drawing reveal" effect.

## React patterns

### Classic `lottie-react` (simpler, JSON)
```bash
npm install lottie-react
```
```jsx
import Lottie from 'lottie-react';
import animationData from './hero.json';

<Lottie animationData={animationData} loop autoplay style={{ height: 400 }} />
```

### dotLottie React (recommended)
```jsx
import { DotLottieReact } from '@lottiefiles/dotlottie-react';
import { useState } from 'react';

function Hero() {
  const [dotLottie, setDotLottie] = useState(null);
  return (
    <>
      <DotLottieReact
        src="/hero.lottie"
        dotLottieRefCallback={setDotLottie}
        autoplay
      />
      <button onClick={() => dotLottie?.play()}>Play</button>
    </>
  );
}
```

## Sourcing animations

- **LottieFiles** (lottiefiles.com) — largest library, mostly free CC0 / paid premium
- **IconScout** — paid, business-friendly licensing
- **Bodymovin** plugin for After Effects — export your designer's AE files
- **LottieFiles plugin for Figma** — convert Figma smart animate to Lottie

For Karim's UGC business: stock Lottie celebrations/loading states cost $0-5 each — much cheaper than rendering custom video. Use for client landing pages.

## Performance tips

1. **Strip unused features in the export** — Bodymovin "Export Modes" → "Standard" not "Demo". Disable expressions if you don't need them
2. **Compress with dotLottie or LottieFiles' "Optimize"** — typical 70-90% size reduction
3. **Lazy-load below-the-fold animations** — `<DotLottieReact intersectionObserverRoot />` or manual IntersectionObserver + `loadAnimation` on intersect
4. **Reuse the same animation across instances** — load JSON once, pass via `animationData` not `path`
5. **Set `progressiveLoad: true`** for big animations on slow connections
6. **Watch DOM node count** — SVG renderer creates one `<path>` per AE shape. Animations with 500+ shapes can lag

## Gotchas

1. **CORS** — loading `.json` from a different origin needs CORS headers. Self-host or use LottieFiles CDN
2. **Hidden tabs pause RAF** — Lottie animations stop animating when tab is backgrounded. Resume on `visibilitychange` if state matters
3. **Server-side rendering** — Lottie touches DOM. SSR-safe only with `lottie-react`'s lazy mode or `dynamic import` in Next.js
4. **AE expressions** — most expressions are NOT supported. Designer must "bake" complex expressions to keyframes before export
5. **Text in animations** — AE text doesn't always export cleanly. Outline text in AE before exporting
6. **`destroy()` is mandatory in React** — without it, leaving and re-entering a page leaks memory + leaves running RAF loops

## Quick decision guide

| Need | Reach for |
|---|---|
| Hero illustration animation | dotLottie + autoplay |
| Loading spinner | Lottie JSON, lottie-web, `loop: true` |
| Onboarding flow with steps | dotLottie with multiple animations |
| Scroll-scrubbed reveal | lottie-web + ScrollTrigger pattern |
| Hover state animation | Don't use Lottie — Motion `whileHover` is cheaper |
| Many simultaneous animations | Canvas renderer |
| Logo morph between routes | Lottie + `playSegments` triggered by state |

## Related

`gsap` (for scroll-scrubbing the lottie + orchestrating around it), `motion-dev` (for UI state animations that complement Lottie hero pieces), `senior-frontend` (React lifecycle patterns for cleanup).
