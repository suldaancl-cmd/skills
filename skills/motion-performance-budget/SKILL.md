---
name: motion-performance-budget
description: Use when a heavily animated website — WebGL hero, pinned scroll sequences, shader backgrounds, smooth scroll, cinematic page transitions — has to hit real Core Web Vitals on real devices instead of only looking good on a fast laptop. Covers the LCP, INP, and CLS budget for premium motion sites, which animated properties are free versus which force layout, how smooth-scroll libraries and scroll-linked effects damage INP, asset budgets for video and image sequences and 3D, the reduced-motion and low-end-device fallback ladder, and how to profile and prove the numbers. Reach for this before shipping any award-tier build, since a premium site that scores badly loses both search ranking and the client.
---

# Motion Performance Budget

The gap between an award-shortlisted site and an unshippable one is almost never the idea. It is that the cinematic version runs at 12 fps on a three-year-old Android and scores in the red on Core Web Vitals. This skill is the budget and the proof.

**Companion skills.** Scroll narrative design → `choreograph-scroll-stories`. GSAP and Lenis implementation → `premium-motion-cookbook`, `gsap-scrolltrigger`. Library selection → `web-motion-library-map`. Launch audit → `awwwards-launch-qa`.

## The three metrics that decide the outcome

| Metric | What it measures | Motion-site failure mode |
|---|---|---|
| **LCP** — Largest Contentful Paint | When the main content appears | A WebGL or video hero delays the largest paint until after the scene compiles |
| **INP** — Interaction to Next Paint | Responsiveness to every interaction | Scroll-linked effects and long tasks make taps feel dead |
| **CLS** — Cumulative Layout Shift | Unexpected movement | Fonts, images without dimensions, and entrance animations that move layout |

**INP is the one that punishes motion sites hardest.** It replaced First Input Delay and it measures the *full* path from interaction to the next painted frame, across the whole session — not just the first interaction. Heavy scroll handlers, large JS bundles, and main-thread shader work all show up here.

Set the budget before design is locked, not after the build.

## The budget

Targets to hold on a **mid-tier mobile device on a throttled connection**, not on the build machine:

| Item | Budget |
|---|---|
| LCP | Under 2.5 s |
| INP | Under 200 ms |
| CLS | Under 0.1 |
| JS shipped before interaction | As small as the design allows; every kilobyte of parse is main-thread time |
| Hero media | Poster image first, heavy scene lazily after |
| Sustained frame rate during scroll | 60 fps, no sustained drops |
| Long tasks | None over 50 ms during interaction |

If the concept cannot fit the budget, the concept changes. Shipping a beautiful site that fails LCP is not a win — it loses ranking and it loses the next client.

## Which properties are free

This is the single highest-leverage technical fact in motion work.

| Animate | Cost | Notes |
|---|---|---|
| `transform` | **Free** — compositor only | translate, scale, rotate, skew |
| `opacity` | **Free** — compositor only | The other safe one |
| `filter` | Moderate — GPU | Blur is expensive at large radii |
| `clip-path` | Moderate | Fine for reveals; watch complex paths |
| `width`, `height`, `top`, `left`, `margin`, `padding` | **Expensive** — forces layout | Never animate these |
| `box-shadow` | **Expensive** — forces paint | Animate a pseudo-element opacity instead |
| `background-position` | Expensive — forces paint | Use transform on a child |

Rule: **animate `transform` and `opacity`. Everything else needs a justification.** A reveal that animates height can almost always be rebuilt with `transform: scaleY` or `clip-path`.

`will-change` promotes an element to its own layer — use it sparingly and remove it after the animation. Applied broadly it exhausts GPU memory and makes things slower, which is the opposite of the intent.

## Where premium motion sites lose INP

1. **Smooth-scroll libraries.** Lenis and equivalents hijack scroll and drive it from JS. This is a real INP cost. Mitigate by keeping the ticker doing nothing but interpolation, never layout reads or DOM writes.
2. **Layout thrash in scroll handlers.** Reading a layout property (`offsetTop`, `getBoundingClientRect`) after writing a style forces a synchronous reflow, every frame. Batch all reads, then all writes.
3. **Too many ScrollTrigger instances.** Dozens of independent triggers each doing work per frame adds up. Consolidate into one timeline with a single progress value where possible.
4. **Shader compilation on the main thread.** First render of a complex shader can block for hundreds of milliseconds. Compile early behind the loader, not on scroll.
5. **Oversized textures and 3D assets.** A 4K texture decoded on the main thread stalls everything.
6. **Font loading.** A late webfont swap causes both CLS and a visible reflow. Preload the critical face and set `font-display` deliberately.
7. **Third-party scripts.** Analytics and chat widgets compete for the same main thread as the animation.

## Asset budgets

| Asset | Guidance |
|---|---|
| **Hero video** | Never autoplay a large file as LCP. Show a poster, load video after. Use modern codecs, mute, `playsinline` |
| **Image sequences** (scroll-scrub) | The heaviest common technique. Reduce frame count aggressively, compress hard, preload in chunks, decode off the main thread. Consider a video with scrubbing instead |
| **3D models** | Compress geometry, keep draw calls low, budget textures. Draco-compressed assets need their decoder loaded correctly, and decoding costs time |
| **Fonts** | Subset to the characters actually used. Preload only the critical face. Arabic and Latin subsets are separate — do not ship the full family for both |
| **Images** | Modern formats, explicit width and height on every image to prevent CLS, responsive sources |

## The fallback ladder

A premium site should degrade in defined steps, not collapse.

1. **Full experience** — capable device, good network, motion allowed.
2. **Reduced effects** — lower particle counts, simpler shaders, fewer simultaneous timelines, on mid or low-end devices.
3. **Static-plus** — no WebGL. Poster images, CSS transitions only, layout and content identical.
4. **Reduced motion** — `prefers-reduced-motion: reduce` honoured. Replace movement with fades, keep all content reachable. This is an accessibility requirement, not an option.

Decide the tier from a capability check at load, and make every tier a genuinely complete experience. A fallback that shows a blank hero is a broken site, not a fallback.

Also handle the case where WebGL fails or is unavailable — it does happen, and an unguarded canvas becomes an empty rectangle.

## Profiling

1. **Field data first.** Lab tools measure your machine; field data measures users. Real-user metrics decide whether the budget is actually met.
2. **Lab profiling with throttling on.** Profile with CPU and network throttling, not at full speed — an unthrottled profile of a motion site is close to meaningless.
3. **Performance timeline** to find long tasks. Anything over 50 ms during interaction is an INP risk.
4. **Frame rendering stats** during the actual scroll interaction, not while idle.
5. **Test on a real mid-range Android phone.** The single most informative test. A desktop throttle simulator does not reproduce mobile GPU and thermal behaviour.
6. **Test on a throttled network** with an empty cache, which is how a first-time visitor arrives.

## Ship checklist

1. Budget written down before build, and design signed off against it.
2. Only `transform` and `opacity` animated, with documented exceptions.
3. No layout reads inside per-frame handlers.
4. Hero LCP element is a fast image, not the heavy scene.
5. Every image and video has explicit dimensions.
6. Fonts subset and preloaded; `font-display` set deliberately.
7. `prefers-reduced-motion` implemented and verified by toggling it.
8. WebGL failure path and low-end tier both verified by forcing them.
9. Profiled on a real mid-range Android with throttling.
10. Third-party scripts deferred.
11. Core Web Vitals measured on the deployed URL, not localhost.

## Verification

Before reporting a motion site as shipped, point to:

- a Core Web Vitals report for the **deployed** URL showing LCP, INP and CLS against the budget
- a throttled performance profile showing no long tasks during scroll
- a screen recording from a **real mid-range Android** device
- confirmation that reduced-motion and the no-WebGL fallback were each forced and observed

A Lighthouse score from an unthrottled desktop run is not evidence. If the site was only tested on the build machine, say so and label the result unverified.
