---
name: seedance-hypermotion-ads
description: Generate fast, kinetic "hyper-motion" PRODUCT ads for Instagram Reels and TikTok using Seedance (or Kling / Veo 3 as fallback). Use whenever the user wants a punchy short product video — speed-ramp push-ins, whip pans, 360-degree orbits, liquid/powder/spark bursts, macro product reveals, a glossy hero shot — especially at 9:16, 1080p, ~15s, or says "product ad", "hyper motion", "kinetic product video", "product reveal", or wants to turn a product photo into an ad. Carries the image-to-video discipline that stops the label from warping. Prefer this over generic video-prompt help for product ads.
---

# Seedance Hyper-Motion Product Ads

Turn a product (or a single product photo) into a punchy 9:16 hyper-motion ad for Reels/TikTok. The goal: a usable, on-brand, **non-warped** product reveal in one or two renders — not the tenth.

## The one rule that saves most renders

**Start from a locked product still and animate it (image-to-video). Never text-to-video.** Text-to-video re-invents the product every clip and melts the label. Animating a fixed first frame is the single biggest consistency upgrade — it's why this skill exists.

## Settings (every render)

`Aspect 9:16 · 1080p · 24fps · 15s = 3×5s shots · Model: Seedance 2.0 (native audio) or 1.0 Pro`

Seedance renders 5–10s clips, so a 15s ad = three 5s shots stitched together (or one multi-shot prompt on Seedance 2.0). Test short before you commit credits to long.

## Hyper-motion camera grammar (this is the "hyper" part)

One product — but motion does the selling. Pull from this vocabulary:
speed-ramp push-in → hard stop · whip-pan entry with motion blur · 360° orbit · snap focus · slow-mo burst (liquid splash / powder / spark / mist) that speed-ramps back to real time · hero landing on a pedestal with a quick dolly-out.

**One action + one camera move per clip.** Stacking actions or moves is the #1 cause of melting and warping. If you need two beats, that's two clips.

## The 6-layer prompt (so the model never has to guess)

`Subject → Action (one beat) → Environment → Camera (one size + one move) → Lighting (name the source) → Audio/SFX.` Target 50–100 words per clip. Naming the light source ("hard rim light from frame-left") stabilizes the render and kills warping.

## Template (fill the brackets)

```
[PRODUCT] hyper-motion ad, 9:16, 1080p.
Clip 1 (0–5s): macro extreme close-up of [PRODUCT] on [SURFACE]; fast speed-ramp push-in that snaps to a hard stop on the label. Whip-pan entry, motion blur, snap focus. Lighting: hard rim light + glossy specular highlights. SFX: deep whoosh + impact.
Clip 2 (5–10s): [PRODUCT] rotates mid-air, 360° orbit; [SIGNATURE ELEMENT — liquid splash / powder burst / smoke / spark] erupts around it in slow-mo, then speed-ramps back to real-time. Camera arcs around the product. Lighting: dramatic [COLOR] gel + backlight.
Clip 3 (10–15s): hero shot — [PRODUCT] lands center-frame on a clean pedestal, quick dolly-out, droplets/particles settle. Logo + tagline space holds steady, legible. Lighting: clean studio key.
Style: glossy commercial, high-contrast, kinetic, premium [BRAND COLOR] palette, crisp reflections, shallow depth of field. Keep product label sharp, readable, unchanged.
Negative: no warping, no melting label, no extra text, no watermark, no distortion.
```

## Negative prompt (paste into every render)

`no warping, no morphing, no melting label, no distorted product, no extra text, no watermark, no logo distortion, no camera glitches, no malformed reflections`

## Model fallback

| Need | Reach for |
|---|---|
| Best value, native audio, Arabic lip-sync | **Seedance 2.0** |
| Hardest physics — splashes, real motion, action | **Kling 2.x/3.0** (Character ID) |
| Synced SFX + first/last-frame keyframing | **Veo 3 / 3.1** |
| One-prompt UGC/product ad with avatars + presets | **Higgsfield Marketing Studio** |

## Five ready category prompts

For copy-paste prompts (perfume · skincare · sneaker · beverage · tech), read [references/example-prompts.md](references/example-prompts.md) and swap the product in.

## Pro tips

- **Test Clip 1 at 5s first** — it's the hook, ~80% of ad performance lives in the first 3 seconds.
- **Change ONE variable per regeneration**, not five — that's how you learn what actually moved the result.
- **Keep the product off-center** in the keyframe so the camera has room to move.
- **Arabic on-screen text:** render it into the keyframe (RTL, Arabic display font) or burn captions in post — don't mix Arabic + Latin in one frame.
- **Label it as AI** when posting — Meta and TikTok both require disclosure for realistic AI-generated content.
