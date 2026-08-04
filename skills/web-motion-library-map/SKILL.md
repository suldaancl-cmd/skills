---
name: web-motion-library-map
description: Use when building or planning premium web/app interfaces with motion, animation, page transitions, scroll effects, WebGL galleries, shader effects, physics, text effects, or cinematic frontend interactions. This skill maps common high-end web effects to the right libraries and recommended stack so future web/app builds don't default to generic CSS or random libraries. Covers the verified 2026 Awwwards/$50k-tier stack — GSAP (now fully free) + Lenis + Three.js/OGL, R3F + postprocessing/TSL/WebGPU, OGL Flowmap cursor distortion, Lottie/Rive motion runtimes — and the canonical "single GSAP progress → shader uniform" + "Lenis synced to gsap.ticker" patterns. Pairs with premium-motion-cookbook, webgl-effect-recipes, and cursor-interaction-recipes for the copy-paste code.
---

# Web Motion Library Map

Use this as the default reference before choosing animation libraries for websites, landing pages, portfolios, dashboards, and app interfaces with premium motion.

> Origin: mirrored from the Hermes skill `/root/.hermes/skills/software-development/web-motion-library-map/SKILL.md`. The **Awwwards / $50k-tier expansion** (studio stacks, budget tiers, extended effect map) lives in `references/` and is merged in additively — the original map below is preserved verbatim.

## References (2026 deep-research expansion)

Load these for the full Awwwards/$50k-tier picture (source-cited, adversarially verified):
- **`references/tool-catalog-2026.md`** — every tool across 9 categories: use / alternatives / real example sites, + Motion, OGL+Flowmap, TSL, pmndrs postprocessing, Leva, @pmndrs/uikit, Lygia, Unicorn Studio, and the WebGL/scroll performance caveats.
- **`references/studio-stacks-and-tiers.md`** — what Immersive Garden / Active Theory / basement.studio actually run, + stack tiers by budget ($10k / $30k / $50k+).
- **`references/sources.md`** — 31 cited sources + verification status.
- **`references/synthesis.md`** — verified findings capstone: confidence-ranked, 29/31 votes upheld, with the canonical 2026 patterns to internalize.
- **`references/multi-site-motion-upgrade-verification.md`** — durable lessons for rolling one motion system across many sites/HTML files (shared `premium-motion.css/js`, per-site config, **Lenis CDN-rename pitfall** → `lenis@1/dist/lenis.min.js`, verification checklists). *(synced from the Hermes copy)*

**Three new headline findings to internalize:**
1. **GSAP + Lenis + Three.js is the universal premium-agency core.** Framework layer varies (Next.js most common; Immersive Garden runs Vue/Nuxt). In React, add R3F + drei + @react-three/postprocessing.
2. **Smooth-scroll / scrolljacking has a real cost.** JS scroll (Lenis/Locomotive) runs on the main thread and hurts INP; native CSS `scroll-behavior:smooth` is faster and off-main-thread. Reserve JS scroll for genuinely scroll-coupled WebGL, always gate behind `prefers-reduced-motion`, and prefer scroll-*position* triggers over physics override.
3. **WebGL must be budgeted.** Three.js ≈600 KB base (>3 MB full stack). Defer the 3D bundle, compile shaders in an OffscreenCanvas worker, ship a static image on mobile, compress with KTX + gltf-transform — or Lighthouse craters.

## Default opinionated stack

For most high-end web/app work, start here:

1. GSAP — core animation/timelines
   https://gsap.com/docs/v3/
2. ScrollTrigger — scroll-linked animation
   https://gsap.com/docs/v3/Plugins/ScrollTrigger/
3. Lenis — smooth scroll
   https://lenis.darkroom.engineering/
4. Barba.js or Swup — page transitions
   https://barba.js.org/
   https://swup.js.org/
5. Three.js / React Three Fiber / Drei — 3D + WebGL in React
   https://threejs.org/
   https://docs.pmnd.rs/react-three-fiber
   https://drei.docs.pmnd.rs/
6. PixiJS — performant 2D canvas/WebGL image and pixel effects
   https://pixijs.com/
7. OGL — lightweight shader/WebGL work
   https://github.com/oframe/ogl
8. Matter.js — 2D physics
   https://brm.io/matter-js/
9. Rapier / react-three-rapier — high-performance 2D/3D physics
   https://rapier.rs/docs/user_guides/javascript/getting_started_js
   https://github.com/pmndrs/react-three-rapier
10. Theatre.js — cinematic 3D timelines
    https://www.theatrejs.com/

Rule of thumb: GSAP + Lenis + Barba gives 70% of luxury web motion without WebGL pain. Add Three/R3F/Pixi/OGL only when the visual idea genuinely needs canvas/WebGL.

**The verified spine (2026):** GSAP + Lenis + Three.js (or OGL) is the universal premium-agency core; the framework is the variable shell (Next.js most common; Immersive Garden / Dogstudio run Nuxt/Vue). In React, add R3F + drei + @react-three/postprocessing. See `references/synthesis.md`.

**2026 stack additions** (verified — full menu in `references/tool-catalog-2026.md`):
- Motion (motion.dev, ex-Framer Motion) — React-first JS animation with a performant `scroll()`; https://motion.dev/
- @react-three/postprocessing — merged-pass Bloom / Vignette / DoF / Glitch for R3F; https://github.com/pmndrs/postprocessing
- TSL (Three.js Shading Language) — node materials that compile to WebGL **and** WebGPU (production since Three r171); https://threejs.org/
- OGL Flowmap — built-in cursor-velocity distortion for hero images/text; https://github.com/oframe/ogl
- Lottie + Rive — ship After-Effects (Lottie) or interactive state-machine (Rive) vector motion; https://lottiefiles.com/ · https://rive.app/
- Spline / Unicorn Studio — no-code 3D / WebGL scenes; https://spline.design/ · https://www.unicorn.studio/
- Lygia — `#include`-able GLSL/WGSL shader functions; https://lygia.xyz/ · Leva — R3F tweak panel; https://github.com/pmndrs/leva

## Core libraries

- GSAP: https://gsap.com/docs/v3/
- GSAP SplitText: https://gsap.com/docs/v3/Plugins/SplitText/
- GSAP ScrambleText: https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/
- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- GSAP Flip: https://gsap.com/docs/v3/Plugins/Flip/
- Lenis: https://lenis.darkroom.engineering/
- Barba.js: https://barba.js.org/
- Swup: https://swup.js.org/
- View Transitions API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- Three.js: https://threejs.org/
- React Three Fiber: https://docs.pmnd.rs/react-three-fiber
- Drei: https://drei.docs.pmnd.rs/
- PixiJS: https://pixijs.com/
- OGL: https://github.com/oframe/ogl
- Curtains.js: https://www.curtainsjs.com/
- gpu-curtains: https://github.com/martinlaxenaire/gpu-curtains
- Matter.js: https://brm.io/matter-js/
- Rapier.js: https://rapier.rs/docs/user_guides/javascript/getting_started_js
- react-three-rapier: https://github.com/pmndrs/react-three-rapier
- cannon-es: https://pmndrs.github.io/cannon-es/
- Theatre.js: https://www.theatrejs.com/
- PavelDoGreat WebGL Fluid Simulation: https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- CSS Mask: https://developer.mozilla.org/en-US/docs/Web/CSS/mask
- CSS clip-path: https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path
- CSS gradients: https://developer.mozilla.org/en-US/docs/Web/CSS/gradient
- SplitType: https://github.com/lukePeavey/SplitType
- Motion: https://motion.dev/
- Anime.js: https://animejs.com/

**2026 additions** (full catalog + citations in `references/tool-catalog-2026.md`):
- @react-three/postprocessing (wraps pmndrs postprocessing): https://github.com/pmndrs/postprocessing
- Leva (R3F control panel): https://github.com/pmndrs/leva
- Lygia (GLSL/WGSL shader includes): https://lygia.xyz/
- OGL Flowmap: https://github.com/oframe/ogl
- Lottie (lottie-web / dotLottie): https://lottiefiles.com/
- Rive: https://rive.app/
- Spline: https://spline.design/
- Unicorn Studio: https://www.unicorn.studio/
- Babylon.js: https://www.babylonjs.com/
- p5.js: https://p5js.org/
- tsParticles: https://particles.js.org/
- text-to-svg: https://github.com/shrhdk/text-to-svg

**2026 currency notes:** GSAP is now 100% free incl. all plugins (SplitText, MorphSVG, …) — for new work, official **SplitText supersedes SplitType**. Three.js WebGPU is production since **r171** (TSL compiles to both renderers). Lenis' CDN path was renamed → use `lenis@1/dist/lenis.min.js` (the old `@studio-freight/lenis` path 404s — see `references/multi-site-motion-upgrade-verification.md`).

## Effect-to-library map

### Beginner / General

**Stairs Transition**
- Best: GSAP + Barba.js
- Alternatives: Swup, View Transitions API
- Links: https://gsap.com/docs/v3/ · https://barba.js.org/ · https://swup.js.org/ · https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API

**Pixel Transition**
- Best 2D/image path: PixiJS
- Best shader path: Three.js or OGL
- Alternatives: Curtains.js
- Links: https://pixijs.com/ · https://threejs.org/ · https://github.com/oframe/ogl · https://www.curtainsjs.com/

**Text Scramble**
- Best: GSAP ScrambleText
- Links: https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/

### Junior

**Masks**
- Best: CSS mask / clip-path + GSAP
- Links: https://developer.mozilla.org/en-US/docs/Web/CSS/mask · https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path · https://gsap.com/docs/v3/

**Text Gradient**
- Best: CSS gradients
- Animated: GSAP animating CSS variables / background-position
- Links: https://developer.mozilla.org/en-US/docs/Web/CSS/gradient · https://gsap.com/docs/v3/

**Mask Split Text**
- Best: GSAP SplitText + mask wrapper
- Alternative: SplitType + GSAP
- Links: https://gsap.com/docs/v3/Plugins/SplitText/ · https://github.com/lukePeavey/SplitType

**Image Gallery with Mouse**
- DOM gallery: GSAP
- Distortion/displacement: Three.js or PixiJS
- React: React Three Fiber + Drei
- Links: https://gsap.com/docs/v3/ · https://threejs.org/ · https://pixijs.com/ · https://docs.pmnd.rs/react-three-fiber

### Intermediate

**Stacked Cards**
- Best: GSAP ScrollTrigger
- Layout transitions: GSAP Flip
- Alternative: Motion
- Links: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ · https://gsap.com/docs/v3/Plugins/Flip/ · https://motion.dev/

**Image Pixel Effect**
- Fast path: PixiJS filters
- Premium path: custom shader in Three.js/OGL
- Links: https://pixijs.com/ · https://threejs.org/ · https://github.com/oframe/ogl

**Infinite Scroll**
- Best: Lenis + GSAP
- Scroll animations: ScrollTrigger
- Links: https://lenis.darkroom.engineering/ · https://gsap.com/docs/v3/ · https://gsap.com/docs/v3/Plugins/ScrollTrigger/

**2D Physics**
- Beginner-friendly: Matter.js
- Performance: Rapier.js
- Links: https://brm.io/matter-js/ · https://rapier.rs/docs/user_guides/javascript/getting_started_js

### Advanced

**Gooey Effect**
- Best: SVG/CSS filter + GSAP
- React option: gooey-react
- Links: https://gsap.com/docs/v3/ · https://github.com/luukdv/gooey-react

**Video on Scroll**
- Best: GSAP ScrollTrigger + video frame scrubbing
- Smooth scroll: Lenis
- WebGL video: Three.js
- Links: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ · https://lenis.darkroom.engineering/ · https://threejs.org/

**Parallel Page Transitions**
- Best: Barba.js + GSAP
- Alternatives: Swup, View Transitions API
- Links: https://barba.js.org/ · https://gsap.com/docs/v3/ · https://swup.js.org/ · https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API

**Pixel Shader**
- Lightweight: OGL
- Ecosystem: Three.js
- DOM image/video shaders: Curtains.js / gpu-curtains
- Links: https://github.com/oframe/ogl · https://threejs.org/ · https://www.curtainsjs.com/ · https://github.com/martinlaxenaire/gpu-curtains

**WebGL Gallery**
- React/Next: React Three Fiber + Drei + GSAP
- DOM image shader path: Curtains.js
- Links: https://docs.pmnd.rs/react-three-fiber · https://drei.docs.pmnd.rs/ · https://gsap.com/docs/v3/ · https://www.curtainsjs.com/

**3D DOM Positioning**
- Best: R3F + Drei Html
- Links: https://docs.pmnd.rs/react-three-fiber · https://drei.docs.pmnd.rs/misc/html

**3D Physics**
- Best: react-three-rapier
- Alternative: cannon-es
- Links: https://github.com/pmndrs/react-three-rapier · https://pmndrs.github.io/cannon-es/

**Gradients**
- Simple: CSS gradients
- Premium animated: Three.js/OGL shader
- Links: https://developer.mozilla.org/en-US/docs/Web/CSS/gradient · https://threejs.org/ · https://github.com/oframe/ogl

**3D Perspective Gallery**
- Pseudo-3D DOM: CSS perspective + GSAP
- True 3D: R3F + Drei
- Links: https://gsap.com/docs/v3/ · https://docs.pmnd.rs/react-three-fiber · https://drei.docs.pmnd.rs/

### God Tier

**3D Timelines**
- Best: R3F + GSAP + Theatre.js
- Links: https://docs.pmnd.rs/react-three-fiber · https://gsap.com/docs/v3/ · https://www.theatrejs.com/

**Fluid Shader**
- Starting base: PavelDoGreat WebGL Fluid Simulation
- Production: Three.js/OGL/Curtains integration
- Links: https://github.com/PavelDoGreat/WebGL-Fluid-Simulation · https://threejs.org/ · https://github.com/oframe/ogl · https://www.curtainsjs.com/

### 2026 additions (deep-research)

**WebGL Scroll Text Reveal** (split heading + scramble + clip-path wipe on scroll)
- Best: GSAP SplitText + ScrambleText + clip-path, driven by ScrollTrigger `scrub:1`
- Code: `premium-motion-cookbook`
- Links: https://gsap.com/docs/v3/Plugins/SplitText/ · https://gsap.com/docs/v3/Plugins/ScrollTrigger/

**Cursor Flowmap Distortion** (hero image/text warps as the mouse moves)
- Best: OGL Flowmap (cursor velocity → off-screen RG texture → fading displacement)
- Alternative: custom Three.js shader
- Code: `webgl-effect-recipes`, `cursor-interaction-recipes`
- Links: https://github.com/oframe/ogl

**Bloom / Glow / Post FX**
- Best (React): @react-three/postprocessing — merged GPU passes (Bloom, Vignette, DoF, Glitch)
- Links: https://github.com/pmndrs/postprocessing

**Image → WebGL Plane** (DOM-bound shader without a full 3D scene)
- Best: Curtains.js / gpu-curtains (bind a DOM `<img>`/`<video>` to a shader plane)
- Alternatives: OGL, Three.js
- Links: https://www.curtainsjs.com/ · https://github.com/martinlaxenaire/gpu-curtains

**Vector Motion-Design Runtime** (icons, hero loops, interactive characters)
- Ship AE animations: Lottie (lottie-web / dotLottie)
- Interactive / state-machine: Rive
- Links: https://lottiefiles.com/ · https://rive.app/

**WebGPU / Cross-Renderer Shaders**
- Best: TSL node materials (compile to WebGL + WebGPU; production since Three r171)
- Shared functions: Lygia
- Links: https://threejs.org/ · https://lygia.xyz/

## Canonical 2026 patterns (verified)

Two techniques recur across nearly every premium build (primary-sourced in `references/synthesis.md`). Internalize both — the full copy-paste code lives in **`premium-motion-cookbook`**.

1. **One GSAP timeline is the single source of truth.** Tween a single `progress` value 0→1 with GSAP/ScrollTrigger, then copy it into a shader uniform each frame (`material.uniforms.uProgress.value = progress`). DOM motion and GPU motion stay on one deterministic curve — "the single pattern reused across every effect."
2. **Sync Lenis to `gsap.ticker`** so scroll, DOM, and WebGL run on one rAF loop — separate loops cause 1–2 frame ScrollTrigger desync:
   ```js
   const lenis = new Lenis({ autoRaf: false });
   lenis.on('scroll', ScrollTrigger.update);
   gsap.ticker.add((t) => lenis.raf(t * 1000));
   gsap.ticker.lagSmoothing(0);
   ```

## Selection rules

- If it is DOM text, layout, cards, page transitions, or scroll: use GSAP first.
- If it is smooth scrolling: use Lenis, then wire ScrollTrigger refresh/update correctly.
- If it is page transitions: use Barba.js + GSAP for full control; use View Transitions API for simpler native transitions.
- If it is image distortion, pixelation, or canvas-heavy 2D: use PixiJS.
- If it is real 3D or shaders: use Three.js/R3F. Use OGL when a tiny custom WebGL scene is enough.
- If it is DOM images/videos with shader effects: consider Curtains.js/gpu-curtains.
- If it is physics: Matter.js for simple 2D, Rapier/react-three-rapier for serious physics.
- If it is cinematic 3D sequencing: combine GSAP timelines with Theatre.js.

## Implementation guardrails

- Respect `prefers-reduced-motion`; provide static fallbacks.
- Animate transform and opacity before anything layout-affecting.
- Do not add WebGL just to look fancy; mediocre WebGL is worse than excellent 2D motion.
- Keep CDN dependencies optional or bundled. A site should still render if motion libraries fail.
- On mobile, reduce particle counts, shader resolution, DPR, and scroll-scrub complexity.
- For React/Next, register GSAP plugins only client-side and clean animations on unmount.
- **Budget WebGL.** Three.js ≈600 KB base (full stack >3 MB) and shader compile is synchronous (50–300 ms each). Defer the 3D bundle past first paint, compile in an OffscreenCanvas worker, ship a static image on mobile, compress with KTX + gltf-transform. Un-budgeted Three.js craters LCP/INP (see `references/synthesis.md`).
- **Smooth-scroll has an INP cost.** Lenis/Locomotive run on the main thread and hurt INP; reserve JS smooth-scroll for genuinely scroll-coupled WebGL, sync it to `gsap.ticker`, gate behind `prefers-reduced-motion`, and prefer scroll-*position* triggers over physics override. For simple cases, native CSS `scroll-behavior:smooth` is faster and off-main-thread.

## Learning order for Karim / AIStudioToday builds

1. GSAP
2. ScrollTrigger
3. Lenis
4. Barba.js
5. Three.js
6. React Three Fiber
7. PixiJS
8. Matter.js
9. Rapier / react-three-rapier
10. Theatre.js

This sequence supports premium agency websites first, then advanced interactive demos later.
