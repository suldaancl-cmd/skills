# Sources — 2026 deep-research expansion

31 sources fetched and claim-extracted by the `deep-research` workflow (fan-out search → fetch → adversarial verification). Grouped by theme. Confidence notes are added where a claim is a vendor benchmark or single-source.

## Studio stacks & case studies
- Immersive Garden — Awwwards case study: https://www.awwwards.com/case-study-immersive-gardens-new-website.html
- Active Theory — "The story of technology built at Active Theory": https://medium.com/active-theory/the-story-of-technology-built-at-active-theory-5d17ae0e3fb4
- basement.studio — "GSAP and Next.js, the bsmnt way": https://basement.studio/post/gsap-and-nextjs-setup-the-bsmnt-way
- Utsubo — Top Three.js agencies: https://www.utsubo.com/blog/top-threejs-agencies
- Orpetron — 10 award-winning sites powered by GSAP: https://orpetron.com/blog/10-award-winning-websites-powered-by-gsap-magic/

## Codrops / Tympanus build tutorials (primary, hands-on)
- Wavy infinite carousels in R3F + GLSL (2025-11-26): https://tympanus.net/codrops/2025/11/26/creating-wavy-infinite-carousels-in-react-three-fiber-with-glsl-shaders/
- Creative process → WebGL portfolio (2025-11-27): https://tympanus.net/codrops/2025/11/27/letting-the-creative-process-shape-a-webgl-portfolio/
- Scroll-revealed WebGL gallery — GSAP + Three.js + Astro + Barba (2026-02-02): https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/
- Seamless 3D transitions — Webflow + GSAP + Three.js (2026-03-18): https://tympanus.net/codrops/2026/03/18/building-seamless-3d-transitions-with-webflow-gsap-and-three-js/
- Shader uniforms → clip-path wipes, GSAP-driven portfolio (2026-05-06): https://tympanus.net/codrops/2026/05/06/from-shader-uniforms-to-clip-path-wipes-how-gsap-drives-my-portfolio/
- Shader.se WebGPU scroll pipeline (2026-05-19): https://tympanus.net/codrops/2026/05/19/80s-business-tech-seamless-scene-transitions-inside-shader-ses-scroll-driven-webgpu-pipeline/

## 3D / WebGL references
- Three.js Journey — post-processing with R3F: https://threejs-journey.com/lessons/post-processing-with-r3f
- Lygia shader library: https://lygia.xyz/
- PavelDoGreat WebGL Fluid Simulation: https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- Curtains.js: https://www.curtainsjs.com/
- Unicorn Studio (no-code WebGL): https://www.unicorn.studio/
- particles.js: https://particles.js.org/
- Web Game Dev — physics: https://www.webgamedev.com/physics
- Utsubo — WebGL/Three.js SEO-rankable guide: https://www.utsubo.com/blog/webgl-three-js-site-seo-rankable-guide
- Award-winning 3D site w/ scroll (Next+Three+GSAP), dev.to: https://dev.to/robinzon100/build-an-award-winning-3d-website-with-scroll-based-animations-nextjs-threejs-gsap-3630

## Animation libraries & performance (⚠ read with the perf caveats)
- Motion — web animation performance tier-list (⚠ vendor; Motion-vs-GSAP benchmark is self-reported): https://motion.dev/magazine/web-animation-performance-tier-list
- GSAP + CSS + Barba.js: https://adigital.agency/blog/gsap-css-animations-barba-js
- noqode — GSAP tool overview: https://www.noqode.fr/en/outils/gsap
- CoreWebVitals — improve INP, ditch JS scrolling: https://www.corewebvitals.io/pagespeed/improve-inp-ditch-javascript-scrolling
- CSS-Tricks — smooth scrolling & accessibility: https://css-tricks.com/smooth-scrolling-accessibility/
- "Scrolljacking is evil" UX guide: https://www.get-started-int.com/en/post/scrolljacking-is-evil-ux-guide
- Utsubo — award-winning website design guide: https://www.utsubo.com/blog/award-winning-website-design-guide

## Pricing references (for the budget tiers)
- be-dev — 2025 website pricing (Framer/Webflow/custom): https://be-dev.pl/blog/eng/website-design-pricing-2025-framer-webflow-and-custom-dev
- Brix Templates — Framer website cost: https://brixtemplates.com/blog/how-much-does-a-framer-website-cost
- Webflow pricing: https://webflow.com/pricing
- Fiverr — interactive 3D site gig (Three/WebGL/GSAP/Webflow/Spline) as market signal: https://www.fiverr.com/xshopifylabs/interactive-3d-animated-website-threejs-webgl-gsap-webflow-spline-3d-shopify

---

### Verification status
Claims were extracted then run through 3-vote adversarial verification (2/3 refutes kill a claim). The library→use mappings are well-established and corroborated across multiple Codrops/studio sources. The spicier **performance claims** (JS scroll hurts INP, native CSS scroll superior, scrolljacking tanks Core Web Vitals) are consistently sourced but partisan — treat as strong guidance, not absolute law. The **Motion "2.5×/6× faster than GSAP"** figure is a vendor self-benchmark — directional only. The confidence-ranked capstone is in `synthesis.md` — note: the automated `deep-research` synthesis agent failed on a schema error, so the capstone was assembled by hand from the 29/31 completed adversarial verdicts.

## Gap-fill verification (single researcher agent, June 2026)

A focused agent pass (replacing the failed workflow) verified the thinner tools and studios — cite-or-flag, nothing invented:

**Tools confirmed (primary source each):** Babylon.js (babylonjs.com) · PlayCanvas (playcanvas.com) · p5.js (p5js.org) · Paper.js (paperjs.org) · Konva (konvajs.org) · two.js (two.js.org) · Box2D JS port (github.com/kripken/box2d.js) · Planck.js (github.com/piqnt/planck.js) · Hydra (hydra.ojack.xyz) · blotter.js (github.com/bradley/Blotter) · Jitter (jitter.video) · tsParticles (particles.js.org) · Spline (spline.design) · Rive (rive.app — used by Spotify/Duolingo/Disney) · Lottie (github.com/airbnb/lottie-web; LottieFiles dotlottie-web = Rust+WASM, WebGL2/WebGPU) · Curtains.js (curtainsjs.com) · gpu-curtains (github.com/martinlaxenaire/gpu-curtains) · Theatre.js (theatrejs.com) · Anime.js (animejs.com) · Swup (swup.js.org) · Taxi.js (taxi.js.org) · Highway.js (archived → Taxi.js).

**Studio stacks verified:** Resn = Three.js + GSAP ("Jelly" pipeline, Awwwards trophy entry) · Unseen Studio = Three.js per-page Scene instances (Awwwards SOTM Feb 2023) · Aristide Benoist = **vanilla WebGL, no Three.js wrapper** (LinkedIn portfolio post) · Dogstudio = Three.js + **Nuxt** + Node + Sanity (StackShare; authored Highway.js→Taxi.js) · Merci-Michel = Three.js shader work (Coastal World case study) · Active Theory = custom in-house **"Hydra" WebGL engine, not Three.js** (Active Theory Medium).

**Could not verify (flagged, not invented):** Cuberto's Three.js/WebGL (only their GSAP is confirmed) · Merci-Michel's JS framework layer · Unseen's framework layer · whether Aristide Benoist wraps his vanilla WebGL in a bundler/framework.
