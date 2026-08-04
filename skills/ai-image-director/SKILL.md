---
name: ai-image-director
description: >-
  Director-grade guide for generating consistent, cinematic AI images with GPT-Image
  (GPT Image 2 / gpt-image-1) and Nano Banana Pro (Gemini 3 Pro Image). Use this
  WHENEVER generating or editing an image for an AI film, ad, product shot, character
  sheet, keyframe, background plate, logo/text image, or ANY image that must stay
  consistent across multiple generations — even if the user only says "make an image",
  "generate a character", "product photo", "keyframe", "make a poster", or names GPT
  Image / Nano Banana / DALL-E / Midjourney / Seedream. This skill locks character,
  prop and location identity, camera, lighting, composition, and text rendering, and
  prevents the usual AI-image mistakes (warped hands, plastic skin, identity drift,
  garbled text, AI sheen). Pair it with ai-video-director when the image becomes a
  video keyframe.
---

# AI Image Director

You are directing an image, not "asking for a picture." A still is the **foundation of all downstream consistency** — in an AI film, the image IS the character. Get the still right and the video inherits it; get it wrong and every shot drifts. This skill makes every image deliberate, repeatable, and mistake-free.

## The one rule that governs everything: STILL-FIRST

The single biggest quality jump in 2026 AI production is this workflow switch: **never text-to-video a character from scratch.** Generate a locked still **keyframe** first, perfect it here, then hand it to `ai-video-director` to animate. The image is your continuity anchor. Treat every important image as a reusable asset, not a throwaway.

## Step 0 — Pick the model (they are not interchangeable)

| Use | Model | Why |
|---|---|---|
| Exact text, logos, infographics, UI, diagrams, "ad-grade" polish, conversational edits | **GPT Image 2** | Plans composition with reasoning, best text rendering + instruction-following; thinking mode holds a character across up to 8 frames in one go |
| Character/brand consistency from references, photoreal skin, multi-image fusion, fast iteration | **Nano Banana Pro** (Gemini 3 Pro Image) | Accepts **up to 14 reference images** for strict identity lock; strong world-knowledge realism |
| Painterly / concept-art / cinematic illustration | Midjourney-class | Aesthetic ceiling for stylized art |

Default for AI-film keyframes: **Nano Banana Pro** (reference-image identity lock). Default for anything with **on-image text** or precise layout: **GPT Image 2**. You can chain them (build identity in Nano Banana → typeset text in GPT Image).

## The universal prompt structure (use this order, every time)

Both top models reward the **same ordered template**. Order matters — it sets the "mode" before details land:

```
1. SCENE / ENVIRONMENT  — where we are, time of day, weather, mood
2. SUBJECT              — who/what, with the locked identity description
3. KEY DETAILS          — wardrobe, expression, pose, props, action
4. CAMERA / STYLE       — shot size, angle, lens, film stock / render look
5. LIGHTING             — named source + direction + quality
6. USE CASE             — "this is a film keyframe" / "TikTok ad" / "UI mock"
7. CONSTRAINTS          — aspect ratio, what to avoid, what to preserve
```

State the **use case** explicitly — it tells the model the polish level. Write **visual facts, not praise**: "wet cobblestone reflecting neon" beats "a beautiful street." Drop the spam — `4k, masterpiece, trending on artstation` is dead weight in 2026; these models read natural language.

## Consistency system (this is the whole game)

Identity drift is the #1 failure. Defeat it with three artifacts you build ONCE and reuse:

1. **Character Sheet** — a single description block you paste into every prompt, plus 1–3 locked reference images (front, 3/4, profile). Pin the *unchangeable* traits: face shape, eye color, hair, age markers, skin texture, a signature wardrobe item.
2. **Location Sheet** — reference image + fixed description for each recurring set (same wall color, furniture, window light).
3. **Anchor Prop** — one specific object that recurs (a collar, a watch, a phone case). It silently tells the viewer "same world, same character" across time-jumps and is the cheapest continuity trick that exists.

**Reference-image rules:** feed Nano Banana up to 14 refs for hard locks; feed GPT Image 2 your reference + use thinking mode for multi-frame sets. More clean references > more adjectives.

**Editing rule — split every edit into CHANGE + PRESERVE.** Never say only "make her smile." Say: *"Change: expression to a warm half-smile. Preserve: identical face, hairstyle, wardrobe, lighting, and background."* This stops the model from silently redrawing the whole image.

**One variable per iteration.** Treat the prompt box like a conversation, not a slot machine. Lighting boring? Add one lighting line. Composition cluttered? Add "minimalist." Change one thing, compare, keep or revert. Changing five things at once means you learn nothing.

## Camera & lens in stills

Direct the lens even for a still — it decides emotion:
- **Shot size:** extreme close-up (emotion) · close-up · medium · wide / establishing (context) · over-the-shoulder.
- **Angle:** eye-level (neutral) · low-angle (power/hero) · high-angle (vulnerability) · top-down.
- **Lens cues:** "85mm portrait, shallow depth of field, creamy bokeh" · "24mm wide, slight distortion" · "macro" — these reshape the whole image.

## Lighting — always name the source

Vague brightness = flat, warped renders. **Name where light comes from and how it behaves.** "Soft window light from frame-left with warm lamp fill" beats "well lit." A named physical source gives the model lighting logic, which stabilizes faces and shadows. Define a **palette** per scene (e.g. rainy-grey exterior / warm amber interior / cold blue hospital) and keep it consistent across the set.

## Text rendering (GPT Image 2's superpower)

Don't say "add text." Specify exact string + style + placement: *Write the text "SELLING OUT" in bold condensed sans, lower third, white with subtle drop shadow.* Quote the literal characters. For Arabic text, state the language and let GPT Image 2 handle the script; verify glyphs in the output (this is where most models fail).

## Mistake-prevention pre-flight (run BEFORE you hit generate)

- [ ] Did I follow the 7-part order (scene→subject→details→camera→light→use case→constraints)?
- [ ] Is the identity locked via a pasted character-sheet block AND a reference image?
- [ ] Did I name the light source and the aspect ratio?
- [ ] For an edit: did I write CHANGE + PRESERVE explicitly?
- [ ] Did I remove quality-spam adjectives and replace praise with visual facts?
- [ ] Am I changing only ONE variable from the last good version?
- [ ] If this is a film keyframe: is it framed so the video model has room to move (don't crop the action)?

## Common AI tells → fixes

| Tell | Fix |
|---|---|
| Plastic / waxy skin | "natural skin texture, visible pores, no retouching"; avoid "perfect/flawless" |
| Warped hands / extra fingers | keep hands partly out of frame or holding a defined object; in the negative: "no extra fingers, no malformed hands" |
| Garbled text | switch to GPT Image 2; quote exact characters; fewer words |
| Identity drift across frames | reuse the SAME reference image + character-sheet block; don't re-describe from scratch |
| "AI sheen" / over-symmetry | add "candid, imperfect framing, slight asymmetry, documentary feel" |

## Ready-to-paste templates

**Character sheet (build once):**
```
SUBJECT: [name], [age], [gender]. Face: [shape, eyes, brows, nose, lips]. Hair: [color/cut].
Skin: [tone, texture, marks]. Signature wardrobe: [item]. Build: [height/frame].
Keep these traits identical in every image. Reference image attached.
```

**Film keyframe:**
```
SCENE: [location, time, weather, mood]. SUBJECT: [paste character sheet]. DETAILS: [pose, expression, action, anchor prop]. CAMERA: [shot size + angle + lens]. LIGHTING: [named source + direction + quality]. USE CASE: cinematic film keyframe, 9:16 (or 16:9). CONSTRAINTS: photoreal, natural skin texture, leave headroom for motion; no text, no warping.
```

**Product shot (UGC/ad):**
```
SCENE: [real setting — kitchen counter / bathroom shelf]. SUBJECT: [PRODUCT], label facing camera, accurate logo. DETAILS: [in-use context]. CAMERA: macro/close-up, eye-level. LIGHTING: soft natural window light. USE CASE: TikTok Shop ad still, 9:16. CONSTRAINTS: keep label sharp and undistorted; no extra text.
```

**Background / location plate:**
```
SCENE: [environment] — empty, no people. STYLE: [palette + film look]. CAMERA: wide establishing, [lens]. LIGHTING: [named source]. USE CASE: reusable location plate for a film set. CONSTRAINTS: 16:9, consistent for multiple shots, no text.
```

## Hand-off to video

When the still is locked, pass it to **`ai-video-director`** as the first frame. Carry the SAME character sheet + anchor prop into the video prompt so identity survives the animation. The image you perfected here is the seed of every consistent shot that follows.
