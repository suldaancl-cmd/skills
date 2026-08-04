---
name: ig-tiktok-ad-playbook
description: The 2026 playbook for generating VIDEO and IMAGE ads for Instagram and TikTok. Use whenever the user is planning, scripting, or producing paid or organic ads for IG (Reels, Stories, feed, carousels) or TikTok (in-feed, Spark Ads, photo mode) — choosing which AI tool/model to use (Sora 2, Veo 3, Kling, Seedance, Higgsfield, HeyGen, Arcads, Nano Banana, Midjourney, FLUX, Ideogram), platform specs and safe zones, hook/retention creative patterns, the end-to-end generation workflow, or AI-content labeling rules. Reach for this on any "ad for IG/TikTok", "what tool should I use", "ad specs", "hook ideas", or "how do I make ads at scale" request, even if the user doesn't name a tool.
---

# IG / TikTok Ad Playbook (2026)

A decision layer for producing short-form video and image ads on Instagram and TikTok with an AI toolchain — written for a small AI-UGC creative operation (solo + AI agents, also serving Gulf/MENA clients).

> **Verify-before-quoting:** the specs, prices, and policy details below are a working snapshot from training knowledge (early 2026), not live-verified. Platform specs and tool pricing move fast — confirm volatile numbers against the official help center / pricing page before committing them to a client deliverable. When the toolchain matters tactically for a *product video*, hand off to the `seedance-hypermotion-ads` skill.

## 1. Platform specs & what the algorithm favors

**Instagram**
| Placement | Aspect / size | Duration | Notes |
|---|---|---|---|
| Reels (primary ad unit) | 9:16, 1080×1920 | hook <3s; 7–15s converts | keep text/CTA out of top ~250px & bottom ~500px (UI overlap) |
| Feed | 4:5 (1080×1350) | ≤60s | 4:5 wins more vertical space than 1:1 |
| Stories | 9:16 | ≤60s/card | full-bleed |
| Carousel | up to 20 cards, 4:5 | — | strong for swipe = dwell time |

**TikTok**
| Placement | Aspect / size | Duration | Notes |
|---|---|---|---|
| In-feed ad | 9:16, 1080×1920 | 9–15s sweet spot | respect right-rail icons + bottom caption safe zone |
| Spark Ads | boosts an organic post (yours or a creator's via auth code) | — | highest-trust format; keeps likes/comments |
| Photo / Carousel mode | static swipeable images | — | cheap CPMs, rising |
| TopView / Top Feed | premium first-impression | — | brand/reach budgets |

**Bias 2026:** vertical 9:16, caption-readable sound-off, hook <3s, native "posted not produced" look, watch-through % over raw length.

## 2. AI generation toolchain

**Video generation**
| Model | Best for |
|---|---|
| Kling 2.x/3.0 | realistic human motion, physics, Character ID consistency |
| Seedance 2.0 | multi-shot from one prompt, native audio, Arabic lip-sync — strong value |
| Veo 3 / 3.1 | synced dialogue/SFX, clean first+last-frame keyframing |
| Sora 2 | cinematic directing, dialogue scenes |
| Higgsfield Marketing Studio | one-prompt UGC/product ads with avatars + presets |
| Runway Gen-4 / Luma | references / fast cheap drafts |

**AI UGC / avatar ads** (talking-head spokesperson at scale): HeyGen, Arcads, Creatify, Captions AI.

**Image generation** (keyframes, product shots, carousels): Nano Banana / Gemini image (best editing + consistency), Midjourney v7 (aesthetics), FLUX (control/API), Ideogram (text-in-image), Seedream (Arabic text), Firefly (commercially safe).

**Edit/captions:** CapCut (auto-captions, native to TikTok), Descript (text-based edit).

## 3. Creative patterns that convert

- **Hook = first 1–3s.** Pattern interrupt, bold claim, or "you know that feeling…". ~80% of performance.
- **Native > polished** for direct-response — but lean into authenticity to beat "AI slop" fatigue (real faces, natural light, candid framing, handheld cue in the prompt).
- **Captions always** (sound-off default).
- **Hook → Retain → CTA.** Fast cuts, one idea per shot, one clear CTA.
- **Funnel-stage message:** cold = problem, warm = solution/mechanism, hot = proof + risk removal.
- **Volume is the strategy.** AI lets you ship 50–100 variants/month; test one variable at a time, kill losers fast.

## 4. End-to-end generation workflow

```
1. CONCEPT/SCRIPT  → angle + hook + one CTA
2. KEYFRAME (image)→ Nano Banana: lock product/character still, 9:16, on-brand palette
3. IMAGE→VIDEO     → animate the still (NOT text-to-video): Kling/Seedance/Veo
                     one action + one camera move per shot; same character-sheet each shot
4. EDIT/CAPTION    → CapCut: cut to <15s, burn captions, licensed sound
5. VARIANTS        → swap hook / first 3s / CTA → 5–20 versions
6. PUBLISH/TEST    → Spark Ads (TikTok) / Reels; read 3s-hold & watch-through; scale winners
```

## 5. Platform policy & AI labeling

- **Meta/Instagram:** disclose realistic AI-generated/altered content; Meta reads C2PA/IPTC metadata and auto-applies an "AI info" label. Mandatory disclosure for political/social-issue ads.
- **TikTok:** AIGC labeling is mandatory for realistic AI content; TikTok adopted C2PA Content Credentials and auto-labels "AI-generated". Label or risk takedown/reduced reach.
- **Spark Ads:** run creator content via the authorization code — keeps the social proof.

## Action layer for an AI-UGC business

1. Lock a Nano Banana keyframe (off-center product, on-brand palette, 9:16).
2. Animate it with Seedance (Arabic lip-sync) or Kling (hardest physics) — never text-to-video.
3. Keep ads <15s with a <3s hook and exactly one CTA.
4. Burn captions in CapCut; use licensed/commercial sound.
5. Generate 10+ hook variants per concept; test one variable at a time.
6. Ship via Spark Ads, label as AI, and scale by 3s-hold + watch-through, not vanity likes.
