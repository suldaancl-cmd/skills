---
name: web-animation-effects
description: >-
  Catalog of 22 production web animations ranked by build difficulty (God → Beginner) plus 5 current 2024 trends,
  each with its technique, library, a real example site, and which installed calaf skill
  builds it — PLUS a recommender that picks the right animations for a given web project.
  Use this whenever planning, scoping, quoting, or building animations for a website,
  landing page, portfolio, or product page; whenever the user asks "which animation/effect
  should I use", "what animation fits this project", mentions scroll effects, page
  transitions, WebGL, shaders, GSAP, Three.js, Awwwards-style/award-winning sites, or
  starts any calaf web build. Reach for it even if the user doesn't say the word
  "animation" but is choosing visual effects for a site.
---

# Web Animation Effects — Catalog + Project Recommender

A working reference of 22 web animations ranked by **difficulty to build** — plus 5 current 2024 trends (bottom) — with the
technique, library, a real example site, and the installed skill that builds each one.
Source: Olivier Larose's difficulty tier-list (Locomotive, Montréal) —
https://www.youtube.com/watch?v=u8YujK0jTSM

Use it two ways:
1. **Starting a project?** Jump to the **Recommender** — match the project to an archetype, get the effects that fit and the budget tier they imply.
2. **Building a specific effect?** Jump to the **Catalog** — get the technique, library, an example site to study, and the calaf skill to build it with.

---

## Recommender — which animations per project

Match the project to the closest archetype, then use those effects. The budget tier
sets pricing expectations (see Pricing).

| Project archetype | Recommended effects | Tier / budget |
|---|---|---|
| **Luxury product / e-commerce** | Video on Scroll · Masks · WebGL Gallery · Image Pixel Effect | Premium → Award |
| **Creative portfolio / agency** | 3D Perspective Gallery · WebGL Gallery · Parallel Page Transitions · Image Gallery with Mouse | Premium → Award |
| **SaaS / startup landing** | Stacked Cards · Mask Split Text · Gradients · Text Scramble | Modern → Premium |
| **Editorial / brand / storytelling** | Text Gradient · Masks · Image Pixel Effect · Mask Split Text | Modern → Premium |
| **Fast modern site (tight budget)** | Pixel Transition · Stairs Transition · Text Scramble · Mask Split Text | Modern |
| **Flagship / award bid (max budget)** | Fluid Shader · 3D Timelines · 3D Perspective Gallery · Gradients | Award |
| **Playful / interactive (events, fun brands)** | 2D Physics · Gooey Effect · Text Scramble | Premium |
| **Immersive / 3D product or story** | 3D Timelines · 3D DOM Positioning · 3D Physics · WebGL Gallery | Award |

**Selection rules of thumb:**
- Lead with **high-payoff / low-effort** effects (Mask Split Text, Masks, Text Scramble) — they read premium but are cheap, so they protect margin.
- Use **one** God/Advanced "hero" effect per site, not many — Olivier's own warning: don't slap a fluid sim on everything.
- Match effect to content: scroll-scrub video for products, WebGL galleries for visual portfolios, split-text for storytelling.

---

## Catalog — the 22 effects (hardest → easiest)

Each entry: **what it is** · **technique/library** · **example site** · **build with**.

### 🔴 God tier — only for flagship/award budgets

1. **Fluid Shader** — mouse-reactive liquid/smoke. GLSL shader on fluid-dynamics math (Pavel Dobryakov, open-source), usually via a library. Ex: https://lusion.co · build with `papaya-smoke-hero`.
2. **3D Timelines** — a 3D scene you move through on scroll, like a game inside the site. `Three.js` scene + camera on a scroll-linked path. Ex: https://hatom.com , https://igloo.inc · build with `three` / `3d-animation-web-designer`.

### 🟠 Advanced — Premium/Award scope

3. **3D Perspective Gallery** — infinite 3D gallery, images warp on pass (hardest non-god effect). Infinite scroll + vertex shader + perspective. Ex: https://unseen.co · build with `three`.
4. **Gradients** — live gradient reacting to mouse/scroll (not CSS). Custom shader. Ex: https://federicopian.com · build with `three` / `shader-dev`.
5. **3D Physics** — real 3D collisions/falling objects. `cannon.js` over `Three.js`. Ex: https://lusion.co · build with `three`.
6. **WebGL Gallery** — images stretch/distort by scroll speed inside WebGL. Infinite scroll + vertex distortion. Ex: https://guillaumecolombel.fr · build with `three`.
7. **3D DOM Positioning** — a 3D object snaps precisely onto a normal HTML element. Math to map 3D→DOM, updated on scroll/resize. Ex: https://kanaknaturals.com · build with `three`.
8. **Pixel Shader** — mouse breaks an image into distorting pixels. Shader + image-array knowledge + mouse. Ex: https://teletech.events , https://zajno.com · build with `three` / `shader-dev`.
9. **Parallel Page Transitions** — both pages visible during the transition. Hijacks native scroll (no scrollbar), rethinks site structure. Ex: https://exoape.com · build with `lenis-smooth-scroll` + `gsap`.
10. **Video on Scroll** — video scrubs forward/back with scroll; great for product reveals. Controlled video or image sequence (watch browser/battery/weight). Ex: https://scoutmotors.com , https://locomotive.ca · build with `gsap-scrolltrigger`.
11. **Gooey Effect** — shapes merge like liquid. Gaussian blur + matrix/render-target to cut the shape (SVG or WebGL). Ex: https://broedutrecht.nl · build with `shader-dev` / SVG.

### 🟡 Intermediate — Premium scope

12. **2D Physics** — draggable/colliding/swinging elements. `matter.js` in canvas. Ex: https://nodcoding.com · build with `frontend-design` + matter.js.
13. **Infinite Scroll** — endless looping content. Track each item's position, reorder on scroll. Ex: https://perspectives.mappmtl.com , https://locomotive.ca · build with `gsap-scrolltrigger` + `lenis-smooth-scroll`.
14. **Image Pixel Effect** — image starts pixelated, sharpens. Canvas + image-array structure (do before Pixel Shader). Ex: https://thibaud.film · build with `frontend-design`.
15. **Stacked Cards** — cards stack on scroll then release. `GSAP ScrollTrigger` + card/window-size math (not just sticky). Ex: https://serious.business · build with `gsap-scrolltrigger`.

### 🟢 Junior — Modern scope, high margin

16. **Image Gallery with Mouse** — images trail and fade behind the cursor. Track mouse, place images, fade, prune the DOM. Ex: https://locomotive.ca · build with `gsap`.
17. **Mask Split Text** — text splits (word/line/char) and reveals via a moving mask. `GSAP SplitText` + clip-path. Trap: re-split on resize, wait for font load. Ex: https://curbcph.tv , https://dothingsnyc.com · build with `gsap` (SplitText).
18. **Text Gradient** — text fades in word-by-word on enter (storytelling). Split text + opacity. Ex: https://pilot-republic.space · build with `gsap`.
19. **Masks** — simple mask reveals an image/section on scroll. clip-path/overflow + animating the 4 corners with different ease/duration. Ex: https://masaigon.space , https://zentry.com · build with `gsap`.

### 🔵 Beginner — Modern scope, fast wins

20. **Text Scramble** — text scrambles then resolves on hover. `GSAP ScrambleText` or vanilla — minutes. Ex: https://thibaud.film · build with `gsap` (ScrambleText).
21. **Pixel Transition** — page transition via pixel squares. divs animated with `GSAP Stagger`. Ex: InkFish , Locomotive's websoft project (named in the video) · build with `gsap`.
22. **Stairs Transition** — panels drop one-by-one between pages. Four divs animated on page change. Ex: https://sonder-mr.com , https://k72.ca · build with `gsap`.

---

## 2024 trend additions (Olivier's "Top 10 Web Animation Trends of 2024")

Current trends, not difficulty-ranked in the source. No example sites (that video was fullscreen — no address bars shown).

23. **Line Mask (Text Line Mask)** — text revealed line-by-line via a mask on scroll/enter; the single most common effect on award-winning sites. `GSAP SplitText` (lines) + clip-path/overflow + ScrollTrigger; add `ARIA` for screen readers. ≈ Junior · build with `gsap`.
24. **Fixed Image** — a fixed image revealed by a clip-path mask on scroll; strong storytelling, easy to ship. `clip-path` + `GSAP ScrollTrigger`. ≈ Intermediate · build with `gsap-scrolltrigger`.
25. **Panel Transition** — a colored panel slides across during a page transition (watch panel↔content contrast). `GSAP` + route transition (kin to Pixel/Stairs). ≈ Beginner · build with `gsap`.
26. **Sticky Footer** — footer pinned/revealed as you scroll past content; now standard on ~80% of award sites. CSS `position: sticky` (often + `GSAP ScrollTrigger`). ≈ Beginner · build with CSS.
27. **Text-Based Project Gallery** — project list as plain text rows with hover/scroll animation (often an image preview on hover). `GSAP` + hover/ScrollTrigger. ≈ Junior · build with `gsap`.

---

## Tooling map by tier

- **Beginner/Junior:** `GSAP` (+ SplitText · ScrambleText · Stagger), clip-path/CSS.
- **Intermediate:** `GSAP ScrollTrigger`, `matter.js`, canvas.
- **Advanced:** `Three.js`, WebGL, GLSL shaders, `Lenis` smooth scroll, `cannon.js`.
- **God:** advanced `Three.js` + heavy shader math (fluid sim) → `papaya-smoke-hero`.

## Pricing tie-in (SAR)

- **Modern (Beginner/Junior):** 12–22k · **Premium (Intermediate/Advanced):** 30–55k · **Award (God + hardest Advanced):** 90–180k+.
- Numbers are starting points from the calaf premium-web ladder — confirm against live pricing before any quote.

## Source & verification

- Definitions/rankings: from Olivier Larose's video directly.
- Example URLs: read from the browser address bar in the video's frames — none invented. Where he didn't name a site clearly, that's noted.
