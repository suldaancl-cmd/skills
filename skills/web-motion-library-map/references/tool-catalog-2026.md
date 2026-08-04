# Tool Catalog — Awwwards / $50k-tier stack (2026 deep-research expansion)

Expansion of the core `SKILL.md` map. Built from a fan-out + adversarially-verified deep-research pass (June 2026). Every non-obvious claim is traceable to `sources.md`. Use this when you need the *full* menu, not just the opinionated defaults.

Legend: **Use** = what to reach for it for · **Alt** = swap-ins · **Seen on** = real example site/studio from the research.

---

## 1. Core animation + scroll

| Tool | Use | Alt | Seen on / note |
|---|---|---|---|
| **GSAP** (3.x, now 100% free incl. all plugins) | The central animation orchestrator. Drives DOM tweens, timelines, **and** WebGL shader uniforms — a single GSAP-tweened `progress` 0→1 copied into a uniform each frame unifies DOM + shader motion under one timeline. | Motion, Anime.js | Universal on Awwwards/GSAP showcase; basement.studio's GSAP+Next.js setup |
| **GSAP ScrollTrigger** | Scroll-coupled animation; `scrub:1` drives scroll-linked morphing, pinning, parallax, count-ups. Built-in `prefers-reduced-motion` + async layout/media handling. | Scroll/View Timeline (native), Motion `scroll()` | The scroll workhorse on premium builds |
| **GSAP SplitText** | Split heading into char/line/word for staggered reveals; layer with scramble + clip-path wipe. (Official, now free — supersedes SplitType for new work.) | SplitType (MIT, framework-agnostic) | Portfolio text reveals |
| **GSAP MorphSVG** | Morph between SVG shapes (e.g. rectangle → complex text path). Often fed by `text-to-svg` → canvas for perf. | Flubber | Roman Jean-Elie 2025 WebGL portfolio |
| **GSAP Flip / Observer / DrawSVG / ScrambleText** | Flip = layout/FLIP transitions; Observer = unified input; DrawSVG = line draw; ScrambleText = decode text. | — | Standard premium toolkit |
| **Motion** (motion.dev, ex-Framer Motion) | Compositor-tier JS animation; benchmarks itself ~2.5× faster than GSAP on unknown-value tweens and 6× on unit conversion via "deferred keyframe resolution" (⚠ vendor benchmark — treat as directional). Has a performant `scroll()`. | GSAP, WAAPI | React-first teams |
| **Anime.js** | Lightweight timeline/SVG animation for simpler sites. | Motion, GSAP | Mid-tier |
| **Lenis** (darkroom.engineering) | The default smooth-scroll. Sync to GSAP `ticker` as single source of truth (native scroll is "too brittle" for tightly-coupled ScrollTrigger). Often **forked** to add page-snapping between scenes; provides scroll velocity that feeds WebGL distortion. | Locomotive Scroll | Immersive Garden; nearly every scroll-driven WebGL site |
| **Locomotive Scroll** | Older smooth-scroll, bundled detection of in-view. | Lenis (now preferred) | Locomotive's own work |

> ⚠ **Performance/accessibility caveat (well-sourced, see sources.md):** JS smooth-scroll (Lenis/Locomotive) runs on the main thread and measurably hurts **INP**; native CSS `scroll-behavior:smooth` is off-main-thread, ~95% supported (Baseline since Mar 2022), and faster. JS scroll also breaks keyboard focus (needs manual focus + `tabindex="-1"`) and can trigger motion sickness. **Scrolljacking tanks INP and Core Web Vitals** — one source calls it "one of the most reliable ways to lose a B2B client." Prefer **scroll-position-triggered** animation (Webflow IX2 style) over physics-overriding scroll, and always gate behind `prefers-reduced-motion`.

---

## 2. Page transitions

| Tool | Use | Alt | Note |
|---|---|---|---|
| **Barba.js** | Full-control SPA-style page transitions (both pages visible, app-like feel). Pair with GSAP. | Swup, Taxi.js, Highway | In real agency codebases GSAP ≫ Barba; adopt Barba **only** when cross-page transition UX is a genuine requirement |
| **Swup** | Lighter drop-in page transitions. | Barba, Taxi | Tighter-budget |
| **Native View Transitions API** | Native cross-document/SPA transitions; combine with GSAP clip-path morphs + `flushSync` to commit the route synchronously inside the VT callback. | Barba | Modern path, less JS |

---

## 3. 3D / WebGL

| Tool | Use | Alt | Seen on / note |
|---|---|---|---|
| **Three.js** | The core WebGL engine for premium 3D. ⚠ ~600 KB min before scene code; full stack (Three + drei + postprocessing + .glb) exceeds 3 MB. | Babylon.js, PlayCanvas, OGL | Immersive Garden, Active Theory, most Three.js agencies |
| **React Three Fiber (R3F)** | Declarative Three.js in React — the canonical combo for React/Next premium WebGL. | vanilla Three.js | Shader.se, Roman Jean-Elie, R3F carousels |
| **@react-three/drei** | Helper components (Html, controls, loaders) on top of R3F. | — | Standard with R3F |
| **@react-three/postprocessing** | R3F wrapper over **pmndrs postprocessing**; auto-merges effects into the minimum GPU passes (beats Three's independent passes which redundantly re-render depth/normals). Effects: Bloom, Vignette, DoF, Glitch. | raw EffectComposer | The canonical R3F post stack |
| **TSL (Three.js Shading Language)** | Node-based material authoring that compiles to **both WebGL and WebGPU** — the cross-renderer shader layer in modern award-tier pipelines. | raw GLSL | WebGPU-forward builds |
| **OGL** | Lightweight WebGL (~29 KB minzip); deliberate Three.js replacement for leaner bundle/API. Built-in **Flowmap** extra writes cursor velocity to an off-screen RG texture for fading distortion on **hero images + text**. | Three.js | Verified: Codrops author rewrote a portfolio Three→OGL "line by line" |
| **Babylon.js / PlayCanvas** | Full game-grade engines for heavy 3D/WebXR. | Three.js | Heavier interactive/3D product |
| **Curtains.js / gpu-curtains** | Bind DOM images/videos to WebGL planes for shader effects without a full 3D scene. gpu-curtains = WebGPU successor. | OGL, Three.js | DOM-image shader path |
| **Spline** | No-code/low-code 3D scenes embedded on the web. | Three.js (hand-built) | Designer-driven 3D |
| **Lygia** (lygia.xyz) | Reusable GLSL/WGSL shader function library (noise, blur, sdf…) you `#include` into shaders. | Shadertoy snippets | Shared shader building blocks |
| **Leva** | Standard optional GUI/tweak panel for R3F (live uniform controls). | lil-gui, dat.GUI, Tweakpane | R3F dev tooling |
| **@pmndrs/uikit** | DOM-like UI laid out **inside** the Three.js canvas (forkable for WebGPU). | drei Html | In-canvas UI, less common |
| **raw GLSL** | Hand-written vertex/fragment shaders remain the tool for bespoke effects (wavy displacement, day/night/cloud/atmosphere layers). Importing `.glsl` into Next/webpack needs `raw-loader -D`. | TSL, Lygia | Every bespoke WebGL look |

> ⚠ **WebGL perf (well-sourced):** shader compile is synchronous, 50–300 ms each; large texture decode 50–200 ms — main-thread. Unoptimized Three.js drops Lighthouse into the 30s, blows LCP, pegs INP. Pattern that worked (AthenaHQ, INP <100 ms): **defer the 3D bundle past first paint**, move shader compile to a Web Worker via **OffscreenCanvas** (`transferControlToOffscreen`), ship a **static image on mobile**.

---

## 4. 2D canvas / pixel

| Tool | Use | Alt |
|---|---|---|
| **PixiJS** | Fast 2D canvas/WebGL — image distortion, pixelation, filters, particle-heavy 2D. | OGL, Three.js |
| **p5.js / Paper.js / Two.js / Konva** | Creative-coding & vector canvas (p5 = generative art, Paper/Two = vector, Konva = interactive shapes). | canvas API |

---

## 5. Physics

| Tool | Use | Alt |
|---|---|---|
| **Matter.js** | Beginner-friendly 2D physics (draggable/colliding/swinging DOM-canvas). | Planck.js, Box2D |
| **Rapier / @react-three/rapier** | High-performance 2D/3D physics (Rust/WASM); the serious choice, R3F-native binding. | cannon-es |
| **cannon-es** | Maintained 3D physics; simpler than Rapier. | Rapier |

---

## 6. Motion-design runtimes

| Tool | Use | Alt |
|---|---|---|
| **Lottie** (lottie-web / dotLottie) | Ship After-Effects vector animations (icons, hero loops) as JSON. dotLottie = compressed/multi-anim. | Rive |
| **Rive** | Interactive, state-machine vector animation runtime (real-time, responds to input/state). | Lottie |
| **Theatre.js** | Cinematic timeline editor for sequencing 3D/DOM — pair with R3F + GSAP for "3D timelines / scroll-through-scene." | GSAP timelines |

---

## 7. Fluid / particle / post

| Tool | Use | Alt |
|---|---|---|
| **PavelDoGreat WebGL Fluid Simulation** | The open-source GPU fluid/smoke base (Navier-Stokes, curl/vorticity). Drop-in cursor smoke; integrate into Three/OGL/Curtains for production. | custom shader |
| **pmndrs postprocessing / EffectComposer** | Bloom, DoF, glitch, vignette as merged GPU passes (see §3). | raw passes |
| **tsParticles / particles.js** | Configurable particle backgrounds/links. | custom canvas |
| **Hydra** | Live-coded video/visual synth (generative, niche). | shaders |

---

## 8. Text

| Tool | Use | Alt |
|---|---|---|
| **GSAP SplitText** | Official, free, robust splitting + masking (re-splits on resize, waits for font load). | SplitType |
| **SplitType** | MIT, framework-agnostic splitter for char/word/line. | GSAP SplitText |
| **text-to-svg** | Generate text as SVG path (then morph via MorphSVG, render to canvas for perf). | — |
| **blotter.js** | GLSL text effects (liquid/distort) — older, niche. | custom shader |

---

## 9. No-code / visual builders at the high end

| Tool | Use | Note |
|---|---|---|
| **Webflow** | Visual builder; premium teams hand-code GSAP/Three on top (IX2 for scroll-position animation). | xshack.app, many Awwwards Webflow sites |
| **Framer** | Designer-driven production sites with built-in motion. | Faster modern builds |
| **Spline** | No-code 3D → web embed. | Designer 3D |
| **Unicorn Studio** (unicorn.studio) | No-code interactive WebGL/shader scenes for the web. | Designer WebGL |
| **Rive** | Interactive motion-design runtime (also a builder). | vs Lottie |
| **Jitter** | Quick motion-design for social/marketing exports. | — |

---

## Asset pipeline (for real 3D, from studio research)

- **Modeling/sim:** Blender, Houdini, ZBrush (Immersive Garden pipeline). Characters often from **Mixamo**.
- **Optimization:** **KTX** texture compression (server-side), **gltf-transform** for `.glb` slimming. Ship compressed, defer, fallback on mobile.
