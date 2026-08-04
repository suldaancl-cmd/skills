# Studio Stacks & Budget Tiers (2026 deep-research expansion)

Companion to `tool-catalog-2026.md`. Two things builders ask: *"what do the famous studios actually run?"* and *"what stack does this budget buy?"* Sources in `sources.md`.

---

## Canonical production stacks of top interactive studios

| Studio | Framework layer | 3D / WebGL | Animation + scroll | Notes |
|---|---|---|---|---|
| **Immersive Garden** | **Vue.js + Nuxt** (not React) | Three.js | **GSAP + Lenis** | Asset pipeline: Blender + Houdini + ZBrush; KTX compression + gltf-transform. (Awwwards case study, 2025) |
| **Active Theory** | custom in-house (historically their own framework/tooling) | WebGL/Three.js, WebGPU-forward | custom | "The story of technology built at Active Theory" — bespoke engine culture |
| **basement.studio** | **Next.js** | Three.js / R3F | **GSAP** (documented "GSAP + Next.js the bsmnt way") | React-first agency |
| **Locomotive** (Montréal) | — | Three.js when needed | Lenis (their lineage) + GSAP | Authored the Locomotive Scroll → Lenis lineage; Olivier Larose's effect tier-list |
| **Resn** | — | **Three.js** (custom "Jelly" pipeline) | GSAP | Awwwards WebGL trophy entry |
| **Unseen Studio** | (unconfirmed) | **Three.js** (per-page Scene instances) | GSAP + Lenis | Awwwards SOTM Feb 2023 |
| **Aristide Benoist** | vanilla (no framework confirmed) | **vanilla WebGL** (no Three.js wrapper) | GSAP | his WebGL portfolio |
| **Dogstudio** | **Nuxt** + Node + Sanity | **Three.js** | GSAP | StackShare — authored Highway.js → Taxi.js |
| **Merci-Michel** | (framework unconfirmed) | **Three.js** shaders | GSAP + Lenis | Coastal World case study |
| **Cuberto** | — | WebGL (unconfirmed) | **GSAP** (open-source Jelly Scroll lib) | their published GSAP libs |

**Convergent finding:** the **GSAP + Lenis + Three.js** triad is the near-universal premium-agency motion core. The framework layer varies (Next.js most common, Nuxt/Vue at Immersive Garden, vanilla at some). React adds **R3F + drei + @react-three/postprocessing**.

### Representative individual builds (real, from the research)
- **Roman Jean-Elie 2025 portfolio** — Next.js/React + Three.js + R3F + **GSAP** (incl. **MorphSVG** rect→text), Mixamo characters, `text-to-svg` → canvas.
- **Shader.se** — Three.js + R3F declarative scenes.
- **R3F creative carousel (2025-26)** — R3F + Three.js + drei, Vite + TS, **Lenis**-fed GLSL distortion, **Leva** controls.
- **AthenaHQ** — deferred 3D bundle + **OffscreenCanvas** worker shader-compile + mobile static fallback → INP <100 ms (the perf-correct way to ship Three.js).

---

## Stack tiers by budget

The same effect ladder, priced. SAR ranges carried over from the calaf premium-web ladder (`web-animation-effects` skill); confirm against live quotes.

### 🟢 Modern — ~$10k (SAR 12–22k)
- **Build:** Framer or Webflow, hand-tuned. Or Next.js + Tailwind.
- **Motion:** GSAP + ScrollTrigger, Lenis (or native CSS scroll), CSS.
- **Effects:** Mask split-text, masks/clip-path reveals, text scramble, animated gradients, sticky footer, text-row project lists. *High-margin: read premium, cheap to build.*
- **No WebGL.**

### 🟡 Premium — ~$30k (SAR 30–55k)
- **Build:** Next.js / Nuxt + headless CMS.
- **Motion:** GSAP ScrollTrigger + Lenis (synced to ticker) as the spine.
- **+ Light WebGL:** PixiJS or Curtains.js / OGL for image distortion, WebGL gallery, scroll-scrub video, stacked cards, pixel transitions.
- **One hero effect**, not many.

### 🔴 Award — $50k+ (SAR 90–180k+)
- **Build:** Next.js (App Router) / Nuxt + React/TS + CMS.
- **Full WebGL:** Three.js / R3F + drei + @react-three/postprocessing, GLSL/**TSL** shaders, **Lygia**, Theatre.js for cinematic 3D timelines, Rapier/cannon-es for 3D physics, PavelDoGreat fluid base.
- **Effects:** fluid shader, 3D scroll-through scenes, 3D perspective/WebGL galleries, mouse pixel-shaders.
- **Mandatory perf budget:** defer 3D bundle, OffscreenCanvas shader compile, KTX + gltf-transform assets, mobile static fallback, `prefers-reduced-motion`. Without this the Lighthouse score craters (Three.js ~600 KB base; full stack >3 MB).

---

## The opinionated default (unchanged from core SKILL.md, now evidence-backed)
**GSAP + Lenis + Barba** = ~70% of luxury web motion with no WebGL pain. Add **Three/R3F/OGL/Pixi** only when the visual idea genuinely needs canvas/WebGL. The research strongly corroborates this: GSAP+Lenis is the universal core, and WebGL is reserved for one deliberate hero moment, never sprayed everywhere ("uniform/generic motion everywhere" is the #1 failure mode of animated sites).
