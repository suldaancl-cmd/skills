# ScrollTrigger

ScrollTrigger links animations to scroll position. It's the most-used GSAP plugin and also the most misused — read this before writing anything non-trivial.

## Registration
```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
```

## The mental model

A ScrollTrigger is a marker that watches one element (`trigger`) and fires events (or scrubs an animation) as that element crosses defined scroll positions. You attach it either:

1. **To a tween/timeline** via the `scrollTrigger` vars object, or
2. **Standalone** via `ScrollTrigger.create({...})` for pure side effects (pinning, callbacks, pure scroll tracking).

## Core options

```js
ScrollTrigger.create({
  trigger: ".panel",       // element whose position we watch
  start: "top 80%",        // "trigger-position viewport-position" — trigger's top hits 80% down the viewport
  end: "bottom 20%",       // default: start + 100 pixels
  scrub: true,             // true = linked to scroll; number = smoothing delay in seconds (1 is nice)
  pin: true,               // pin the trigger while scrolling between start and end
  pinSpacing: true,        // default; inserts padding so layout doesn't collapse
  markers: true,           // DEV ONLY — visual start/end markers
  toggleActions: "play none none reverse", // onEnter onLeave onEnterBack onLeaveBack
  once: true,              // fire only the first time (overrides toggleActions)
  snap: { snapTo: 1/4, duration: 0.3, ease: "power1.inOut" },
  onEnter: () => {},
  onLeave: () => {},
  onUpdate: (self) => { console.log(self.progress, self.direction, self.velocity); },
  invalidateOnRefresh: true, // recompute tween start/end values on resize
});
```

### Position syntax
- `"top center"` — element's top reaches viewport center
- `"top 80%"` — element's top reaches 80% down the viewport
- `"+=500"` after a start → end is 500px of scroll later
- `"bottom top"` — element's bottom reaches viewport top (common end for "until off screen")
- Callback form: `start: (self) => self.previous()?.end ?? 0`

### toggleActions
A string of four keywords for `[onEnter, onLeave, onEnterBack, onLeaveBack]`.  
Options: `play | pause | resume | reverse | restart | complete | reset | none`.

Defaults: `"play none none none"` — plays forward on enter, does nothing else.  
Common: `"play none none reverse"` — plays forward, reverses when scrolling back up.

## Scrub vs toggleActions — pick one

- **Use `scrub`** when animation progress should match scroll progress (parallax, pinned scenes, reveals tied to scroll amount). Use `ease: "none"` on the tween.
- **Use `toggleActions`** when the element should animate on its own clock once it enters view (a card fades up at its normal duration).

Don't set both.

## Pinning

```js
ScrollTrigger.create({
  trigger: ".section",
  start: "top top",
  end: "+=2000",          // pin for 2000px of scroll
  pin: true,
});
```

Inside a pinned section, other ScrollTriggers can scrub animations — that's how you get the classic "pinned hero with scroll-scrubbed reveals" pattern.

**Pin gotchas:**
- The pinned element gets wrapped in a `.pin-spacer`. CSS like `section:nth-child(...)` may break — style using classes.
- If content is taller than viewport, avoid pinning or set `pinType: "transform"` explicitly.
- On iOS, `pinType: "fixed"` sometimes causes jank; GSAP picks `"transform"` automatically on touch devices, which is usually what you want.

## Responsive: `gsap.matchMedia`

This is the modern way. Don't use the deprecated `ScrollTrigger.matchMedia`.

```js
const mm = gsap.matchMedia();

mm.add("(min-width: 768px)", () => {
  gsap.to(".panel", {
    xPercent: -300,
    scrollTrigger: { trigger: ".wrap", pin: true, scrub: 1, end: "+=3000" }
  });
  // return cleanup optional — matchMedia auto-reverts
});

mm.add("(max-width: 767px)", () => {
  gsap.from(".panel", { opacity: 0, stagger: 0.2,
    scrollTrigger: { trigger: ".panel", start: "top 85%" }
  });
});
```

All tweens/ScrollTriggers created inside the callback are automatically reverted when the media query no longer matches.

## Batch — performance for long lists

Instead of creating one ScrollTrigger per card in a 200-item feed:
```js
ScrollTrigger.batch(".card", {
  onEnter: els => gsap.from(els, { y: 40, opacity: 0, stagger: 0.1, overwrite: true }),
  start: "top 85%",
});
```

Batch groups elements entering the viewport in the same frame — much cheaper.

## Horizontal scroll

```js
const sections = gsap.utils.toArray(".panel");
gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: "none",
  scrollTrigger: {
    trigger: ".wrapper",
    pin: true,
    scrub: 1,
    snap: 1 / (sections.length - 1),
    end: () => "+=" + document.querySelector(".wrapper").offsetWidth,
  },
});
```

## Refreshing

Call `ScrollTrigger.refresh()` after:
- Dynamic content loads that changes layout
- Fonts finish loading (causes reflow): `document.fonts.ready.then(() => ScrollTrigger.refresh())`
- Route changes in SPAs (also kill old ones: `ScrollTrigger.getAll().forEach(t => t.kill())`)

## Debug workflow

1. Add `markers: true` to see start/end lines.
2. Use `onUpdate: self => console.log(self.progress)` to verify the range is right.
3. If animation doesn't run: check that the plugin is **registered**, the trigger element **exists** at the time of creation (not null from SSR), and there's actual scrollable content above/below.
4. Common bug: creating ScrollTriggers inside a component before the DOM is measured — layouts based on images without dimensions shift, `start`/`end` compute wrong. Use `imagesLoaded` or `document.fonts.ready`, then `ScrollTrigger.refresh()`.

## ScrollSmoother (also now free)

For butter-smooth native-feel scrolling with parallax:
```js
import { ScrollSmoother } from "gsap/ScrollSmoother";
gsap.registerPlugin(ScrollSmoother);

ScrollSmoother.create({
  wrapper: "#smooth-wrapper",
  content: "#smooth-content",
  smooth: 1.5,
  effects: true,           // enables data-speed / data-lag attributes
});
```

HTML:
```html
<div id="smooth-wrapper">
  <div id="smooth-content">
    <img data-speed="0.8" src="..." />       <!-- moves slower (parallax) -->
    <h1 data-speed="1.2">Title</h1>           <!-- moves faster -->
  </div>
</div>
```

Don't use ScrollSmoother alongside Lenis, Locomotive, or CSS `scroll-behavior: smooth` — pick one.
