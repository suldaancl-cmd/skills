# Scene Archetypes (build specs)

Nine archetypes assemble every launch promo. Each entry: purpose · duration · visual recipe ·
motion recipe · props · best tool. Motion values reference `motion-tokens.md`. The full
director's-cut teardown is in the studio's `research/05-reference-teardown-blueprint.md`; the
machine-usable registry is `motion-graphics-studio/templates/scene-archetypes/INDEX.md`.

---

## A1 — cold-open-hook (3s)
**Purpose:** Pattern interrupt in the first 3s. No brand yet — one kinetic element that earns
the next 10 seconds. (65% of viewers who survive 3s watch 10+s.)
**Visual:** `bgAlt` (often inverted from main bg — dark if film is light). One bold word or a
single sweeping shape/light-streak. Max contrast.
**Motion:** One slam or sweep. Hero display appear (600ms expo) OR a fast wipe. No settle time —
momentum straight into A2.
**Props:** `bg, hookWord, accentColor, duration`
**Tool:** Remotion / GSAP

## A2 — brand-wordmark (2s)
**Purpose:** Logo + product name. The "this is who" beat.
**Visual:** Centered logo mark + product name in `fontDisplay`. Clean `bg`.
**Motion:** Logo spring-in (800ms, stiffness 200 / damping 18, 85%→100% overshoot). Hold 1s
dead still — the stillness is the weight.
**Props:** `logoSrc, productName, bg, textColor, font`
**Tool:** Remotion / GSAP

## A3 — kinetic-type (4s) — repeatable up to 3×
**Purpose:** The claim in ~4 words. The signature beat. Pattern: neutral **anchor** word +
**accent** word in brand color. Optional code-syntax styling (`[brackets]`/`(parens)` in accent,
à la OpenAI Codex).
**Visual:** Big `fontDisplay` on `bg`. Text fills ~60% width, generous margins. Accent word/glyph
is the only color.
**Motion:** Per-word mask reveal (clip-path wipe up + `y:24→0`, 480ms, expo-out
`cubic-bezier(0.16,1,0.3,1)`, stagger 45–55ms). Accent word does a 150ms clip wipe (snaps, never
fades). Settle 1.2s, cut.
**Props:** `anchorText, accentText, accentColor, bg, font`
**Tool:** Remotion / GSAP (SplitText)

## A4 — product-ui-demo (8s) — the longest beat, mandatory >15s
**Purpose:** Show the product doing the thing, in a curated frame. Most persuasive beat.
**Visual:** macOS browser chrome / terminal window / glass app panel. 40–60px inner padding,
`border-radius:12–16px`, shadow `0 40px 80px rgba(0,0,0,0.12)`. Real UI, never a raw screenshot.
**Motion:** Frame enters (700ms back-ease overshoot, scale 0.92→1). Idle float (±8px Y, 4s loop,
±1.5° tilt). Inside: cursor lerp (300ms move, 80ms click pulse) + terminal typing sim
(35–55ms/char ±10ms jitter) + scroll sim (easeInOutQuart 800–1200ms).
**Props:** `frameStyle (browser|terminal|glass), terminalLines[] or screenshot, bg, duration`
**Tool:** Remotion / HyperFrames (HTML is ideal here — real DOM UI)

## A5 — feature-montage (5s) — proof beat for dev/B2B (excludes A7)
**Purpose:** Show breadth — many capabilities fast.
**Visual:** Grid of cards / chip-swarm / tiled outputs in `accentColor` + neutrals.
**Motion:** Stagger in (70ms/card). Optional 3D depth (R3F) for chip-swarm.
**Props:** `variant (grid|swarm|tiles), items[], accentColor, bg`
**Tool:** Remotion / R3F

## A6 — collage-texture (10s) — brand films only
**Purpose:** Emotion/narrative via archival or artistic b-roll (Anthropic's butterflies→"C").
Skip for SaaS/dev-tool promos.
**Visual:** `images[]` on textured `bg`, slow pan/parallax (0.15× rate).
**Motion:** Organic flutter (irregular keyframes, ease-in-out + randomization). Elements can
morph/arrange into a letterform (staggered 80ms). Cuts land on beats (`cutOnBeat[]`).
**Props:** `images[], bg, cutOnBeat[], duration`
**Tool:** Remotion / GSAP

## A7 — social-proof (5s) — proof beat for consumer/commerce (excludes A5)
**Purpose:** Trust via testimonials + a metric.
**Visual:** Glassmorphism testimonial cards (avatar, name, ⭐⭐⭐⭐⭐, quote) floating over a
dashboard with a live metric. Soft gradient bg.
**Motion:** Cards stagger in (70ms) with parallax-float depth. Metric can run A8 count-up.
**Props:** `testimonials[], dashboardBg, metricValue`
**Tool:** Remotion / GSAP

## A8 — stat-reveal (2s) — standalone or embedded in A7
**Purpose:** One number lands a quantified proof point.
**Visual:** Huge number in `fontDisplay`, small unit + label.
**Motion:** Count-up from `countFrom` to `value` (≈1s, ease-out), accent flash on the unit.
**Props:** `value, unit, label, countFrom, bg`
**Tool:** Remotion

## A9 — logo-outro (2–3s) — always closes
**Purpose:** Final brand lockup + (optional) CTA.
**Visual:** Logo + product name (and CTA line) on solid `bg`/`bgAlt`. Often a soft accent glow.
**Motion:** Logo spring settle (800ms, 200/18, 85%→100%). Then hold DEAD STILL ≥2s. The hold is
mandatory — it's the signature of a confident outro.
**Props:** `logoSrc, productName, bg, holdFrames, ctaText?`
**Tool:** Remotion / GSAP

---

## Existing skills/templates that build these fast

- A3 kinetic type, A1 hook: `gsap` + `gsap-timeline` + `vfx-text-cursor`, `frame-glitch-title`
- A4 product UI: `frame-macos-notification`, HyperFrames (`hyperframes`, `hyperframes-cli`)
- A6 collage / liquid bg: `frame-light-leak-cinema`, `frame-liquid-bg-hero`
- A7/A8 dashboard + chart: `frame-data-chart-nyt`
- A9 logo outro: `frame-logo-outro`
- 3D (A5 swarm, A2 dimensional logo): `react-three-fiber`, `three`, `spline-3d`
- Whole-film engine: `remotion`, `hyperframes`, `premium-motion-cookbook`, `web-motion-library-map`
