# Synthesis — verified findings (capstone)

The `deep-research` workflow extracted 129 claims from 31 sources, then ran 3-vote adversarial verification (2/3 refutes kill a claim). The background run was interrupted by session events before its synthesis agent fired, so this capstone is synthesized directly from the journal's completed verdicts. **Verification signal: 31 votes adjudicated → 29 upheld (all high-confidence), 2 refuted.** The upheld core is heavily primary-sourced (Codrops first-party build write-ups, official `darkroomengineering/lenis` and `oframe/ogl` repos, pmndrs).

## Executive summary
The premium/Awwwards web stack in 2026 has a stable spine and a variable shell. The spine is **GSAP + Lenis + Three.js (or OGL)**; the shell is the framework (Next.js most common; Immersive Garden runs Vue/Nuxt) and an optional WebGL hero. The dominant, verified production pattern is **one GSAP timeline as the single source of truth** — a 0→1 `progress` value tweened by GSAP and copied per-frame into a shader uniform — with **Lenis synced to `gsap.ticker`** so scroll, DOM, and GPU animate on one deterministic loop. WebGL is used surgically for a single hero moment, never sprayed everywhere, because un-budgeted Three.js wrecks Core Web Vitals. The biggest dissenting evidence is a strong performance/accessibility case *against* JS smooth-scroll and scrolljacking.

## High-confidence findings (verified, primary-sourced)

1. **GSAP owns the motion curve; the shader is stateless.** A single GSAP-tweened `progress` (0–1) copied each frame into a shader uniform is "the single pattern reused across every effect." Verified verbatim (Codrops 2026-05-06) + corroborated by Codrops' Oct-2025 "Animate WebGL Shaders with GSAP" and tutorials back to 2021. *This is THE technique to internalize.*
2. **Lenis synced to `gsap.ticker` = single source of truth.** Native scroll is too brittle for tightly-coupled ScrollTrigger; the official Lenis README prescribes `gsap.ticker.add(t => lenis.raf(t*1000))` + `lagSmoothing(0)`. Running separate rAF loops causes 1–2 frame ScrollTrigger desync jitter. Verified + multi-source.
3. **The text-reveal recipe:** GSAP **SplitText** (char/line) + **scramble** + a **clip-path wipe** layered on top (both run together, left-to-right), driven by a `ScrollTrigger` `scrub:1`. Verified verbatim from a first-party build.
4. **OGL is a real, deliberate Three.js replacement** for leaner bundle/API (~29 KB minzip), with a built-in **Flowmap** extra that writes cursor velocity into an off-screen RG texture for fading distortion. Verified against the author's post + `oframe/ogl/src/extras/Flowmap.js`. *(Correction from verification: Flowmap drives **hero images + text**, not "video carousels.")*
5. **R3F + Three.js + TSL is the canonical React WebGL stack.** Shader.se (founded 2021) composes scenes declaratively in R3F; **TSL** node materials compile to **both WebGL and WebGPU** (production WebGPU since Three r171, Sep 2025). R3F ~700k npm/wk, Three ~5M/wk. Verified + corroborated.
6. **pmndrs postprocessing** merges effects into the minimum GPU passes (beats Three's independent passes). **Leva** = standard R3F control panel; **@pmndrs/uikit** = in-canvas DOM-like UI.
7. **Immersive Garden** (Awwwards case study): Three.js + GSAP + Lenis on **Vue/Nuxt**; assets via Blender/Houdini/ZBrush + KTX + gltf-transform.

## Medium / contested findings (use with the hedge)

- **JS smooth-scroll & scrolljacking carry a real cost.** Multiple sources: JS scroll (Lenis/Locomotive) is main-thread and hurts **INP**; native CSS `scroll-behavior:smooth` is off-main-thread and faster (~95% support, Baseline Mar 2022); scrolljacking "tanks INP" and is "one of the most reliable ways to lose a B2B client." *Consistent but partisan (perf/UX advocates) — strong guidance, not absolute law. The premium-agency reality still ships Lenis; the resolution is: use it deliberately, sync to ticker, gate `prefers-reduced-motion`, prefer scroll-position triggers over physics override.*
- **WebGL must be budgeted.** Three.js ≈600 KB base; full stack >3 MB. Shader compile is synchronous (50–300 ms each). Fix (AthenaHQ, INP <100 ms): defer the 3D bundle, OffscreenCanvas worker for shader compile, static image on mobile, KTX + gltf-transform.

## Low-confidence / refuted

- **"Motion is 2.5×/6× faster than GSAP"** — vendor self-benchmark (motion.dev). Directional only; not independently verified. Do not quote as fact.
- "Award-tier" framing on several individual portfolios is the **authors' own aspiration** (benchmarking against Awwwards), not verified awards. The *techniques* are real and well-sourced; the "award-winning" label on those specific personal sites is not.

## Caveats
The verified sample skews toward the GSAP/Lenis/OGL/Codrops cluster (those votes completed first). Studio-stack claims (Immersive Garden, Active Theory, basement.studio) rest largely on single authoritative sources each. Fast-moving area — WebGPU/TSL adoption is climbing through 2026.

## Open questions
1. **Partly answered (June gap-fill):** Nuxt/Vue is a *pattern* at non-React award studios, not an outlier — both **Immersive Garden** and **Dogstudio** run Nuxt. And the very top tier sometimes drops Three.js entirely for a **bespoke/vanilla WebGL** engine (**Active Theory**'s in-house "Hydra"; **Aristide Benoist**'s raw WebGL). Still open: how common is the custom-engine route vs Three.js at SOTY level?
2. When does WebGPU/TSL become the default over WebGL/GLSL for new award builds?
3. What's the real conversion/SEO delta between a scrolljacked award site and a CWV-optimized one in B2B vs creative-portfolio contexts?
