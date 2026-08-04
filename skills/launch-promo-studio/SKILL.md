---
name: launch-promo-studio
description: >-
  Build OpenAI / Anthropic-tier product launch & promo motion-graphics videos — kinetic
  typography, product-UI-in-frame demos, social proof, logo outros — fully in code
  (Remotion / GSAP / React-Three-Fiber + ffmpeg) with pro sound design. Use this WHENEVER
  the user wants a launch video, promo video, announcement film, product teaser/sizzle/hero
  reel, "a motion graphic like OpenAI / Anthropic / Linear / Vercel / Stripe", a kinetic
  typography video, or to design / produce / edit any branded short-form motion-graphics
  video — even if they don't say the words "motion graphics". Covers the whole pipeline:
  brief → script → scene archetypes → build → render → sound → master → social derivatives,
  plus one-object brand-kit reskinning. Pairs with the `motion-sound-design` skill for audio.
---

# Launch Promo Studio

Produce launch/promo motion-graphics videos at the standard set by OpenAI (Codex), Anthropic
(Claude / Claude Code), Linear, Vercel, Stripe, and Apple — **in code**, so every video is
reproducible, re-editable, and re-skinnable to any brand.

This skill is the **director**. It tells you the rules, the pipeline, the scene archetypes,
the exact motion values, and which tool builds each shot. For audio, hand off to the
**`motion-sound-design`** skill. For the deep research behind every claim here, the full
"director's cut" lives in the studio workspace (below).

## Studio workspace

The production workspace on this machine is:

```
C:\Users\user\motion-graphics-studio\
├── README.md            # master playbook + production runbook (read this to produce a video)
├── research/            # the 5 deep-research pillars (tooling, motion, sound, post, teardown)
├── brand-kits/          # one JSON per brand — swap to re-skin any template (see below)
├── templates/scene-archetypes/INDEX.md   # machine-usable archetype registry
├── assets/{music,sfx,fonts,logos}/
├── projects/<slug>/     # one folder per video you make
├── reference-frames/    # extracted frames from the 4 anchor reference videos
└── exports/
```

Create each new video under `projects/<slug>/`. The render engine is Remotion (already
installed at `C:\Users\user\aistudiotoday-promo` and `C:\Users\user\aistudiotoday-outros`;
reuse one or `npx create-video@latest` a fresh one per project).

## The standard (5 non-negotiable rules)

These five rules, drawn from teardown of OpenAI + Anthropic + whop launch films, are what
separate "expensive" from "AI-slop". Break them and the video reads cheap.

1. **One accent color, under ~15% of any frame.** Spend the accent only on a bracket glyph,
   the logo mark, or a single headline word. A second accent collapses the hierarchy. (OpenAI
   = purple only on `[brackets]`; whop = red only on the wordmark + one number.)
2. **Mask-reveal type at 480ms, expo-out.** Canonical word entrance: clip-path wipe from
   bottom + translate `y:24px → 0`, `cubic-bezier(0.16, 1, 0.3, 1)`, 480ms, stagger 45–55ms
   per word. This one token covers ~80% of all headline animation.
3. **Let scenes settle before cutting — minimum 1.2s dwell.** Cutting while motion is still
   moving reads as panic. Reach the settled state, hold 1.2–1.5s, then cut. Hold = confidence;
   cut = momentum.
4. **Own exactly one background texture.** Pure white (OpenAI), sage-green linen-noise
   (Claude Code), antique paper grain (Claude brand film), deep cinematic dark (whop). The
   texture surrounds every frame and does more brand work than the logo. Pick it first.
5. **Never show a raw screenshot — always frame product UI.** macOS browser chrome, a terminal
   window, or a glass panel, with 40–60px inner padding, `border-radius:12–16px`, and a shadow
   tuned to the background. The frame says "curated reality, not a screengrab."

Full motion-token table (every gesture's duration + easing + spring) →
`references/motion-tokens.md`.

## The 9 scene archetypes

Every launch promo is assembled from these. Full props-level specs and the build recipe for
each are in `references/scene-archetypes.md` (and the studio's `research/05-*.md`).

| ID | Slug | Purpose | Dur | Best tool |
|----|------|---------|-----|-----------|
| A1 | cold-open-hook | Pattern interrupt, one kinetic element, no brand yet | 3s | Remotion/GSAP |
| A2 | brand-wordmark | Logo + product name, held 1s for weight | 2s | Remotion/GSAP |
| A3 | kinetic-type | The claim in ~4 words: anchor (neutral) + accent word | 4s | Remotion/GSAP |
| A4 | product-ui-demo | Framed interface, typewriter/cursor interaction | 8s | Remotion/HyperFrames |
| A5 | feature-montage | Capability grid / chip-swarm to show breadth | 5s | Remotion/R3F |
| A6 | collage-texture | Narrative b-roll (archival/artistic) — brand films only | 10s | Remotion/GSAP |
| A7 | social-proof | Floating glass testimonial cards over a dashboard | 5s | Remotion/GSAP |
| A8 | stat-reveal | One number counts up to land a proof point | 2s | Remotion |
| A9 | logo-outro | Brand lockup, spring in, hold dead still | 2–3s | Remotion/GSAP |

**Sequence rules:** A1 always opens, A9 always closes. A3 may repeat up to 3×. A4 must appear
in any promo > 15s. A5 (dev/B2B) and A7 (consumer/commerce) are mutually exclusive proof
beats. A6 only when the brand has non-product creative assets.

## The pipeline (how to actually produce one)

Follow the full runbook in `references/production-runbook.md`. The short version:

1. **Brief** — audience, the ONE message, brand, length, platforms. (If missing, ask.)
2. **Script** — 65–75 words for 30s. One idea per beat. Write the accent words.
3. **Beat sheet** — map words to archetypes on the 30s master timeline (see below).
4. **Brand kit** — pick or create `brand-kits/<kit>.json` (12 keys — color, font, logo,
   texture, fps, motionStyle). This is the ONLY thing you change to re-skin.
5. **Build** — implement each beat as a Remotion `<Sequence>` (or HyperFrames scene). Use the
   motion tokens verbatim. Frame all UI.
6. **Render** — `remotion render ... out.mp4`, 4K (or 1080p) master, ProRes or high-bitrate H.264.
7. **Sound** — invoke **`motion-sound-design`**: music bed + SFX synced to cuts, duck, master
   to −14 LUFS / −1.5 dBTP.
8. **Master + derive** — mux audio, then derive 9:16 / 1:1 / 4:5 social cuts via ffmpeg
   (master once, never re-render per format). Specs → `references/export-specs.md`.
9. **QA** — run the pre-ship checklist in `references/export-specs.md`.

### Master 30s beat sheet

```
0:00–0:03  A1  Cold-open hook        (bgAlt, one sweep/slam, no brand)
0:03–0:05  A2  Brand wordmark        (logo + product name, spring in)
0:05–0:09  A3  Kinetic type #1       (primary value prop)
0:09–0:17  A4  Product-UI demo       (8s framed interaction — the longest beat)
0:17–0:21  A3  Kinetic type #2       (second claim)
0:21–0:26  A5 or A7  Proof           (montage for dev tools / social proof for consumer)
0:26–0:28  A3  Kinetic type #3       (CTA phrase, e.g. "Start building")
0:28–0:30  A9  Logo outro            (spring in, hold dead still)
```

15s = drop A2/A5, single A3, 3s A4. 60s = add a second A4 + an A6 collage + A8 stat. Duration
table → `templates/scene-archetypes/INDEX.md`.

## Tooling

Primary path (replicates ~80% of studio-tier looks at ~zero license cost):
**Remotion** (render engine) → **GSAP** (2D motion + SplitText kinetic type) → **R3F/Three.js**
(3D + particles) → **ffmpeg** (mux, derive, master) → **Blender** (free, 3D assets) →
**DaVinci Resolve** (free, color finish). Use AI video (Higgsfield/Kling/Nano Banana) ONLY for
atmospheric b-roll — never for the clean typographic core; it can't hold that aesthetic.
Rationale + studio attributions → `research/01-tooling-software-stack.md`.

## Brand-kit reskinning

One template, any brand, by swapping a single JSON object. Pre-built kits in `brand-kits/`:
`kit-openai-codex`, `kit-anthropic-claude-code`, `kit-anthropic-brand-film`, `kit-whop`,
plus `kit-ai-studio-today` (Karim's own). Keys: `bg, bgAlt, accent, text, textOnDark,
fontDisplay, fontMono, logoSrc, productName, motionStyle (snap|spring|ease), fps, bgTexture,
mascotSrc`. To make a new brand, copy a kit, change the values, point the template at it.

## Default assumptions (state, don't silently pick)

- If brand/length/platform are unspecified: default to **30s, 16:9 4K master**, derive
  9:16 + 1:1, and **ask** which brand kit (or offer to build one). Don't invent a brand.
- Engineering/dev-tool brands → snappy/staccato motion, no bounce, A5 proof.
  Consumer/commerce → springy motion, A7 social-proof.
- Always produce a master + social derivatives, not a single aspect ratio.

## What success looks like

A rendered MP4 that obeys the 5 rules, lands every cut on a sonic event, masters at
−14 LUFS, and re-skins to a new brand by editing one JSON file. If you can't point to those,
it's not done.
