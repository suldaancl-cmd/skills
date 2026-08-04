---
name: awwwards-winner-playbook
description: Use when planning, building, auditing, or submitting a website that aims for Awwwards / FWA / CSS Design Awards recognition — or just "award-tier" quality. Maps the official Awwwards judging rubric (Design 40% / Usability 30% / Creativity 20% / Content 10%) to a concrete build checklist and ROUTES each criterion to the right specialist skill in this library. Covers award categories, score thresholds (6.5 Honorable Mention, 7+ Developer Award, 75/100 Mobile Excellence), the jury/submission process, the tech-stack layers, and the non-motion trends (typography, color, brutalism, sound, CMS) a motion-only stack misses. This is the ORCHESTRATOR — it tells you which other skills to invoke for each part of an award build.
---

# Awwwards Winner Playbook

**The one thing to internalize: motion is 20% of the score. Win the other 80%.** A flawless GSAP/WebGL hero on a site with weak typography, muddy IA, or thin copy does not win. This playbook routes each scored criterion to the specialist skill that handles it.

Source for the rubric, thresholds, and process: [awwwards.com/about-evaluation](https://www.awwwards.com/about-evaluation/) · [awwwards.com/about-judging](https://www.awwwards.com/about-judging/) (fetched & verified 2026-06-15).

## The official rubric

| Criterion | Weight | What the jury grades |
|---|---|---|
| **Design** | **40%** | Visual quality, typographic system, color, layout, craft, consistency |
| **Usability** | **30%** | Navigation, IA, responsiveness, forms, states, speed, ease of use |
| **Creativity** | **20%** | Originality, concept, innovation — where motion/WebGL lives |
| **Content** | **10%** | Quality & relevance of copy, imagery, media |

Min. **18 jurors** score each submission; statistical outliers are auto-removed. Score is out of 10.

## Awards & thresholds (what to aim for)

- **Site of the Day (SOTD)** — highest jury score that day. **Honorable Mention** — score ≥ **6.5** but not top-of-day.
- **Site of the Month / Year (SOTM / SOTY)**, **Agency of the Year**, **E-Commerce SOTY**, **Developer SOTY** — escalating tracks.
- **Developer Award** — every SOTD is re-judged by a developer jury; score > **7** earns the badge. Graded on code quality, semantics, **accessibility**, performance, cross-device. *(A site can win SOTD and still fail this.)*
- **Mobile Excellence** (with Google) — judged on **Google's mobile rubric, threshold 75/100** — a *separate* scoring system, not motion.

## Criterion → action → which skill to invoke (the keystone)

### Before scoring — reference and concept gate
- Verify recent winners and extract transferable mechanisms → `mine-award-site-patterns`
- Turn brand meaning into one original central metaphor → `direct-immersive-concepts`
- Do not choose GSAP/WebGL effects until both the reference intelligence and concept direction are complete.

### Design — 40% (spend the most here)
- Visual hierarchy, scale, contrast → `visual-hierarchy`, `refactor-ui-01-establish-visual-hierarchy`
- Typographic system → `typography-scale`, `font-pairing-local`, `variable-fonts-local`; for typography that moves as an interface → `direct-kinetic-typography`
- Color/palette → `color-system`, `color-expert`; mine source-cited award-site tokens with `immersive-web-token-vault`; for color, light, texture, and atmosphere that evolve by scene → `direct-immersive-color-light`
- Layout & grid, spacing → `layout-grid`, `spacing-system`, `responsive-design`
- Overall craft / anti-AI-slop execution → `frontend-design`, `ui-ux-pro-max`, `impeccable` (audit pass)
- Aesthetic direction → `brutalist-skill` / `minimalist-skill` / `soft-skill` / `high-end-visual-design` (match the brief)
- **Karim's bar:** cinematic, not flat cards. Colors & Fonts deck FIRST, ban default-luxury fonts (see your feedback memories).

### Usability — 30% (most-missed by "creative" builds)
- IA & navigation → `information-architecture`, `navigation-patterns`, `search-ux`
- Forms, errors, loading, empty states → `form-design`, `error-handling-ux`, `loading-states`
- Responsive / cross-device → `responsive-design`, `apple-hig`
- Heuristics & general rules → `web-design-guidelines`, `heuristic-evaluation`, `aesthetic-usability`
- **Accessibility (Developer-Award gate)** → `a11y-audit`, `accessibility-audit`, `design:accessibility-review` — semantic HTML, ARIA, keyboard, `prefers-reduced-motion`.

### Creativity — 20% (the motion layer — already built)
- Library/effect selection → `web-motion-library-map` (the map)
- Narrative pacing and scene/state choreography → `choreograph-scroll-stories`
- Implementation → `premium-motion-cookbook`, `webgl-effect-recipes`, `cursor-interaction-recipes`
- 3D / shaders → `3d-animation-web-designer`, `three`, `shader-dev`, `react-three-fiber`
- Lightweight shader/image work → `ogl-webgl`, `webgl-image-transitions`
- R3F production helpers and cinematic finishing → `react-three-drei`, `react-postprocessing`
- Physics and interruptible spring behavior → `matter-js`, `react-spring`
- Honest asset loader and loader-to-hero handoff → `premium-preloader-intro`
- Optional consent-based interactive sound → `design-web-sonic-experiences`
- **One hero effect, not many** (motion's own rule).

### Content — 10%
- Microcopy / UX writing → `ux-writing`, `design:ux-copy`
- Narrative / marketing copy → `copywriting`, `content-strategy`

## Tech-stack layers of an award build (plan all four)

1. **Framework:** Next.js / Nuxt / **Astro** / **SvelteKit** (Awwwards tags all four on winners).
2. **CMS (headless):** Sanity / Storyblok / Prismic / Craft / Contentful / DatoCMS / Payload → `headless-cms-stack`; plan content structure from day one.
3. **Motion:** the `web-motion-library-map` stack (GSAP + Lenis + Three/R3F/OGL).
4. **No-code (legit at award tier):** Webflow / Framer → `webflow-premium-motion`.

## Non-motion trends Awwwards curates (2025–26, verified)

- **Hero / variable typography** as the centerpiece (named "Hero Typographies" collection).
- **Brutalism** — raw, system-font, web-safe-color, irreverent (dedicated collection: [awwwards.com/brutalism-brutalist-websites.html](https://www.awwwards.com/brutalism-brutalist-websites.html)).
- **Color-first** palettes & gradients (Color Exploration collection; Pantone tie-ins).
- **Bento grids / layout systems** (industry-dominant pattern).
- **AI-native UX** (AI-Powered Web Projects collection).
- **Sound design** — audio hover, ambience, scroll-velocity response, and audio-reactive worlds → `design-web-sonic-experiences`.
- **Scrollytelling / storytelling** (Storytelling Websites collection).
- **Microcopy / UX writing** (dedicated collection).

## Pre-submission gate

Before you submit, run **`awwwards-launch-qa`** (performance/INP, WebGL budget, a11y, motion, ship-verification). Then sanity-check against the rubric weights:
- [ ] Design (40%): type system, color, grid, craft all deliberate — not just "has animation".
- [ ] Usability (30%): IA clear, forms/states handled, responsive, fast (INP < 200ms).
- [ ] Accessibility passes (Developer-Award gate): keyboard, semantics, `prefers-reduced-motion`.
- [ ] Creativity (20%): one strong, original hero idea — not effect soup.
- [ ] Content (10%): copy is sharp, microcopy intentional, media high-quality.
- [ ] Mobile: real-device tested against Google's 75/100 bar.

## Selection rule
If the build is weak on Design or Usability, **fix those before adding motion** — they're 70% of the score and the most common reason creative sites lose. Motion is the finish, not the foundation.

## Default orchestration order

1. `mine-award-site-patterns`
2. `direct-immersive-concepts`
3. `direct-immersive-color-light` + `direct-kinetic-typography` (Colors & Fonts deck first)
4. `choreograph-scroll-stories`
5. implementation specialists: GSAP / Lenis / Three.js / OGL / R3F / WebGL / physics / Rive / Lottie as required
6. `design-web-sonic-experiences` only when sound strengthens the concept
7. `a11y-audit` + `awwwards-launch-qa`

## Sources
- Rubric & weights, jury process, thresholds: https://www.awwwards.com/about-evaluation/ · https://www.awwwards.com/about-judging/
- Developer Award: https://www.awwwards.com/developer-award/
- Mobile Excellence (Google): https://www.awwwards.com/google-and-awwwards-present-the-mobile-excellence-award.html
- Collections (color/type/AI/tools/brutalism): https://www.awwwards.com/collections/ · https://www.awwwards.com/brutalism-brutalist-websites.html
- Companion skills: `mine-award-site-patterns`, `immersive-web-token-vault`, `direct-immersive-concepts`, `direct-immersive-color-light`, `direct-kinetic-typography`, `choreograph-scroll-stories`, `design-web-sonic-experiences`, `premium-preloader-intro`, `ogl-webgl`, `webgl-image-transitions`, `react-three-drei`, `react-postprocessing`, `matter-js`, `react-spring`, `web-motion-library-map`, `awwwards-launch-qa`, and the premium-web-motion skills.
