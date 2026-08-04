---
name: ai-video-director
description: >-
  Director-grade guide for generating consistent, cinematic AI VIDEO with Seedance 2.0,
  Kling 3.0, Veo 3.1, and Sora 2. Use this WHENEVER generating, animating, or planning
  any AI video, film, ad, reel, short, or multi-shot sequence — even if the user only
  says "make a video", "animate this", "turn this image into a clip", "AI ad", "shot
  list", or names Seedance / Kling / Veo / Sora / Higgsfield / Runway. This skill is the
  pre-flight checklist that stops you wasting credits on broken renders: it locks
  character/prop/location consistency, camera, lighting, place/background, and movement,
  enforces the image-to-video workflow, and prevents the classic mistakes (identity
  drift, warped hands, distorted product labels, melted faces, camera chaos, too many
  actions per shot). Pair with ai-image-director to build the keyframes first.
---

# AI Video Director

Video is where credits get burned and consistency dies. This skill is your **director + pre-flight gate**: do not hit "generate" until you've cleared the checklist below. The goal is a usable, on-model, non-warped shot on the first or second try — not the tenth.

## The two rules that prevent 80% of mistakes

1. **IMAGE-TO-VIDEO, not text-to-video.** Generate a locked still keyframe first (see `ai-image-director`), then animate it. Text-to-video reinvents the character every clip and guarantees drift. Animating a fixed first frame is the single biggest consistency upgrade in 2026.
2. **ONE action + ONE camera move per shot.** Stacking actions or camera moves is the #1 cause of melting, warping, and chaos. If you need two beats, that's two shots.

## Step 1 — Build the Production Design Guide (once per project)

Before any shot, write a one-page guide. This is the persistent-context artifact that real AI films use to stay consistent across 20+ shots. It is the difference between amateur and pro.

```
PRODUCTION DESIGN GUIDE — [title]
LOG LINE: [one sentence: story + emotion]
CHARACTERS (paste into every shot):
  - Lead (young): [age, hair, wardrobe, distinguishing features]
  - Lead (old):   [same person + ageing markers]
  - Companion / pet / co-star: [breed/colour/marking]
ANCHOR PROP: [one recurring object = the collar/watch/phone] ← continuity glue
LOCATIONS: [set A description + palette] / [set B] ...
PALETTE: [3 colours, e.g. rainy grey · warm amber · cold hospital blue]
AUDIO: [music mood / voice language]
```

## Step 2 — Write the Shot List

Break the story into shots. Each row = one render. Keep it 6–8 shots for a 20s piece; scale up only once the pipeline works.

```
# | SIZE (CU/MS/WS/ECU) | ANGLE | ONE ACTION (single beat) | KEYFRAME REF
1 | MS | eye-level | man finds puppy in rain        | img_01
2 | CU | low-angle | puppy looks up                  | img_02
...
```

## Step 3 — The universal video prompt (6 layers, in order)

Every model rewards the same six-layer structure. Missing a layer = the model guesses, and guessing = drift.

```
1. SUBJECT      — who, with the locked character-sheet description
2. ACTION       — ONE clear beat, described as physical motion
3. ENVIRONMENT  — the set + atmosphere (steam, rain, dust)
4. CAMERA       — ONE shot size + ONE move
5. LIGHTING     — named source + direction
6. AUDIO        — dialogue in quotes / SFX / music mood
```

Target **50–100 words**. Quality of structure beats quantity of adjectives.

### Camera vocabulary (be explicit)
- **Move (pick ONE):** static/locked · slow dolly in · dolly out · tracking · orbit · pan L/R · tilt · crane up/down · handheld.
- **Size:** ECU · CU · MS · MWS · WS/establishing.
- **Angle:** eye-level · low (power) · high (vulnerability) · POV.

### Movement (where realism is won or lost)
- Use **strong, specific motion verbs**: "drifts," "sprints," "uncaps and presses," not "moves."
- Chain cause→effect with **"and"**: "she swipes the stick across her cheek **and** the line softens." Models with physics engines (Kling especially) follow this causality and produce believable motion.
- Describe motion in **beats/counts** for control: "takes two steps, pauses, turns."

### Lighting — always name the source
"Soft morning window light from frame-left" stabilizes the render and kills warping. Never just "bright." Keep the palette from your Production Design Guide.

## Step 4 — Multi-shot & timeline syntax (2–4 shots MAX per render)

To get an edited feel in one render: `Clip 1 (0–3s): ... / Clip 2 (3–6s): ... / Clip 3 (6–8s): ...`. Assign seconds per clip and **repeat the style + character cues in every clip**. Past 4 clips, drift takes over — render separately and edit together instead.

## Step 5 — Audio & dialogue
- Dialogue in **quotes**, kept short to match clip length (a 4s shot fits ~1 line).
- Sounds as `SFX: rain on pavement`. Music as a mood line.
- **Seedance 2.0** = native audio-video + phoneme-level lip-sync in 8+ languages (incl. Arabic). **Veo 3.1** = synced dialogue/SFX from the prompt. Kling/Sora: add audio in post if needed.

## Consistency in video (carry the still forward)

| Model | Consistency mechanism | How to use it |
|---|---|---|
| **Kling 3.0** | **Character ID** — holds identity in ~90%+ of clips | Give a clean reference; avoid extreme angles, very dark light, or tiny-in-frame subjects (the failing 10%) |
| **Seedance 2.0** | Multimodal **@mentions**, up to ~12 reference files (image/video/audio) | Upload refs, cite `@Image 1` / `@Video 1`; great for multi-shot from one prompt |
| **Veo 3.1** | **First-frame + last-frame** keyframing + synced audio | Feed your Nano-Banana keyframe as first frame; reduces voice/identity breaks |
| **Sora 2** | Image-to-video locks the opening frame | Upload the still as frame 1; describe only the motion |

Golden rule: **the same keyframe + the same character-sheet text in every shot.** Don't re-describe the character from scratch per shot — paste the locked block.

## Step 6 — Model selection

| Need | Reach for |
|---|---|
| Realistic human body motion, action, physics | **Kling 3.0** |
| Native audio + multi-shot story from one prompt + non-English lip-sync | **Seedance 2.0** |
| Synced dialogue/SFX, multi-clip edited feel, clean keyframing | **Veo 3.1** |
| Filmic directing, dialogue scenes, cinematic language | **Sora 2** |
| One-prompt UGC/product ad with avatars + presets | **Higgsfield Marketing Studio** (your connected MCP) |

## MISTAKE-PREVENTION PRE-FLIGHT (clear ALL before generating)

- [ ] Am I **animating a keyframe** (image-to-video), not text-to-video from zero?
- [ ] Exactly **ONE action** and **ONE camera move** in this shot?
- [ ] Did I paste the **character-sheet block** and attach the **same reference**?
- [ ] Did I **name the light source** and set the **aspect ratio + duration**?
- [ ] Is the prompt **50–100 words**, six layers present, no adjective spam?
- [ ] For multi-shot: **≤4 clips**, seconds assigned, style cues repeated?
- [ ] Did I add a **negative** for the known failure of this shot (hands/label/text)?
- [ ] Am I starting at **5s** to test before extending to 10s+? (save credits)
- [ ] Will I change **one variable** per regeneration, not five?

## Common failure modes → fixes

| Failure | Cause | Fix |
|---|---|---|
| Face/identity drifts between shots | text-to-video; re-described character | image-to-video; reuse keyframe + Character ID / @refs |
| Hands warp / extra fingers | hands free + complex motion | keep hands on a defined object; negative "no malformed hands" |
| Product label melts/changes | no anchor on the label | "keep product label sharp, readable, unchanged"; close-up |
| Whole shot melts / morphs | too many actions or camera moves | one action + one move; shorten to 5s |
| Camera does random zooms | vague/contradictory camera cues | state exactly one move; "locked tripod shot" if static |
| Looks fake / "AI" | over-clean, studio feel | "handheld, candid, natural imperfections, documentary" |

## Negative prompt (Kling especially — keep a default)
`no warping, no morphing, no extra fingers, no distorted faces, no changing product label, no text artifacts, no sudden camera jumps`

## Ready-to-paste shot template (any model)
```
SUBJECT: [paste character sheet]. ACTION: [one physical beat]. ENVIRONMENT: [set + atmosphere]. CAMERA: [one size] + [one move]. LIGHTING: [named source + direction]. AUDIO: "[short line]" / SFX: [sound]. Style: cinematic, [palette], natural imperfect feel. First frame: [keyframe]. Duration 5s, 9:16.
Negative: no warping, no extra fingers, no label distortion, no camera jumps.
```

## Cost discipline
Each render costs credits and most "bad" outputs come from skipping the pre-flight. Lock the keyframe, test at 5s, change one variable, and only then scale duration or batch variants. A perfected keyframe + a disciplined prompt beats brute-force regeneration every time.
