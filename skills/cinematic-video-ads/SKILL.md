---
name: cinematic-video-ads
description: >-
  Engine for producing cinematic, lead-generating video ads with AI. Use this whenever the
  user wants to make, plan, script, storyboard, produce, or critique a video ad — a product
  ad, real-estate/property promo, app/SaaS ad, UGC ad, brand film, or a Reels/TikTok/Shorts
  ad — even if they don't say the word "cinematic." Turns a brief into: chosen ad structure,
  a scroll-stopping hook, an emotional shot list, ready-to-paste AI generation prompts, a
  captions/audio assembly plan, and ONE lead-gen CTA. Pulls in `ai-video-director` for the
  shot-by-shot generation mechanics. Reach for it the moment a video advertisement is the goal.
---

# Cinematic Video Ads

A cinematic ad that doesn't convert is a showreel. A converting ad that isn't cinematic gets scrolled past. This skill builds the rare thing that is **both** — and produces it with AI, cheaply, at scale.

## The core equation

> **Cinematic craft** (stops the scroll, builds emotion) × **Conversion structure** (hook → escalate → payoff → one CTA) = **leads.**

Most ads have exactly one half. The reference STAROOT real-estate film was pure craft — gorgeous, 86s, *zero* hook text, *zero* CTA, no contact → it generated admiration, not enquiries. Never ship one half without the other. This is the discipline the whole skill enforces.

## What this is (and what it isn't)

This is a **general engine** for any vertical (real estate, e-com, app, local service, personal brand). It owns the **ad craft + conversion + assembly** layer. It does **not** re-teach AI shot generation — that lives in **`ai-video-director`** (image-to-video, one-action-one-camera-move, the 6-layer prompt, model consistency). Use both together: this skill decides *what ad to make*; `ai-video-director` executes *each shot*.

Four reference files carry the depth — load the one you need, when you need it:
- `references/conversion-rules.md` — the data: hook-rate benchmarks, retention, silent-first, CTA mechanics, hook + CTA templates.
- `references/craft-patterns.md` — the cinematic grammar: 12 named patterns + mini-frameworks (Guinness/Nike/Apple-grade).
- `references/vertical-templates.md` — 8 ad structures + copyable shot-by-shot templates per vertical + benchmarks + mistakes.
- `references/ai-production.md` — the 2026 tool matrix, consistency rules, end-to-end assembly, cost discipline.

## The workflow

Run these in order. Don't skip to generation — the expensive mistake is always a skipped brief or a missing hook, not a bad render.

**0 — Lock the brief.** You cannot design an ad you can't describe. Fill the Brief block below. If the user hasn't given audience / goal / offer / CTA destination, ask in one shot.

**1 — Pick the structure.** Match goal + category to one structure (table below; full beat-sequences in `vertical-templates.md`). One structure per ad. For lead-gen, default to PAS or AIDA short; for high-ticket/brand, Three-Act.

**2 — Engineer the hook (first 1–3s).** This is 80% of the result — hook rate is the first auction filter. Write 3–5 hook variants (templates in `conversion-rules.md`). The hook is a *visual* + a *line of on-screen text*, decided together. No logo, no slow drone build, no brand super in the first 3s.

**3 — Design the emotional arc + shot list.** Lay 6–8 beats on the chosen structure. Apply cinematic patterns from `craft-patterns.md` (shot-scale cascade, deferred brand reveal, tension→plateau→release, kinetic-rhyme cuts). Each beat = one shot = shot-size + one action + on-screen text. This becomes the `ai-video-director` shot list.

**4 — Write the ONE CTA.** Lead-gen converts on conversation, not clicks. Default to comment-to-DM, click-to-WhatsApp, or book-a-call (templates in `conversion-rules.md`). State it twice — spoken (if VO) **and** on-screen — in the last 3–5s.

**5 — Generate each shot.** Hand the shot list to **`ai-video-director`**. Image-to-video only: lock a keyframe per shot (`ai-image-director`), then animate. Pick the model from the matrix in `ai-production.md`. Test every shot at **5s draft** before committing to Quality.

**6 — Assemble.** Captions (non-negotiable — silent-first), voiceover (ElevenLabs for Arabic/clone), music bed (Suno/Udio), edit in CapCut/Descript. Steps in `ai-production.md`.

**7 — QA + variants.** Run the pre-flight checklist. Then ship **3–5 hook variants** over the same body+CTA — hooks fatigue at ~day 7; rotate the opener, keep the engine.

## Decision tables

### Structure by goal × category
| Goal / category | Structure | Length |
|---|---|---|
| Lead-gen, high-pain (clinic, finance, service) | **PAS** | 15–30s |
| Lead-gen, cold mass-market (e-com, app) | **AIDA short** | 15–30s |
| High-ticket / prestige (real estate, luxury, coaching) | **Three-Act** | 30–60s |
| Visible-result (beauty, fitness, renovation) | **Before/After** | 20–28s |
| New / skeptical brand, trust-building | **Founder/Origin** | 40–50s |
| Aesthetic hero product | **Product-Hero reveal** | 20–28s |
| Retargeting, proof-led | **Testimonial** | 22–28s |

### Model by need (full matrix + prices in `ai-production.md`)
| Need | Reach for |
|---|---|
| Budget social hooks, product motion, in-frame text | **Kling 3.0** |
| Native synced audio + multi-shot in one pass, UGC | **Seedance 2.0** |
| Cinematic + ambient audio/dialogue baked in | **Veo 3.1** |
| Post-generation in-video edits, agency control | **Runway Gen-4.5** |
| One-prompt product-ad factory + avatars (your MCP) | **Higgsfield Marketing Studio** |
| Long hero clip (15–25s), physics — sparingly | **Sora 2** |

### Platform rules (don't fight them)
| | Meta (Reels/Feed) | TikTok | YouTube Shorts |
|---|---|---|---|
| Sound | **Silent-first** (85% muted) — captions carry it | **Sound-ON** — sound drives conversion | Captioned, sound-aware |
| Aspect | 9:16 / 4:5 | 9:16 | 9:16 |
| Feel | Native > polished | "Real, not polished" | Native |
| CTA | Comment-to-DM / WhatsApp / link | DM / instant form → WhatsApp | Link / comment |

## The brief (lock before generating)
```
PRODUCT / SUBJECT:
ONE-SENTENCE PROMISE:        (what changes in the customer's life)
AUDIENCE + their pain:
PLATFORM + aspect:           (Reels 9:16 / TikTok 9:16 / Shorts …)
GOAL:                        lead-gen (DM / WhatsApp / booking / link)
STRUCTURE:                   (from the table)
HOOK (visual + text line):
CTA (the one action):
SPOKEN LANGUAGE:             (e.g. Arabic VO via ElevenLabs)
PALETTE / TONE:              (3 colours; cinematic look)
DURATION:                    (15–45s)
```

## Hook engineering — the first 1–3 seconds

The hook is a **visual pattern-interrupt** + a **text line**, designed together:
- Visual: open mid-motion, unexpected scale/texture, or a before-state. Sharp foreground vs blurred background. (See "Sensory Pre-Interrupt", "In Medias Res" in `craft-patterns.md`.)
- Text: a curiosity gap, bold claim, pain mirror, or audience callout (templates in `conversion-rules.md`).
- Benchmarks: aim for a Reels hook rate ≥25% (≥40% is elite). Below 15% the ad dies in the auction.
- **Never** open on a logo or a slow establishing drone shot with no text — that was the STAROOT mistake.

## Captions are the script, not a subtitle

On Meta, ~85% watch muted — the on-screen text *is* the message. Big branded font (not default subtitles), kinetic emphasis on key phrases, reposition through the frame, step indicators / curiosity builders. Test the whole ad on mute: if it doesn't sell silent, it doesn't sell.

## The ONE CTA (lead-gen)

One action, last 3–5s, stated spoken + on-screen. Prefer conversation over clicks:
- **Comment-to-DM:** "Comment 'PLAN' and I'll DM you the price list."
- **Click-to-WhatsApp:** "Tap to message me on WhatsApp — I reply personally." (WhatsApp ads see 45–60% link CTR vs 2–5% email.)
- **Book-a-call / register:** "Register → free floor plan." Add real scarcity only if true.

## Pre-flight (clear before you spend credits)
- [ ] Brief fully locked (audience, goal, CTA destination)?
- [ ] Hook is a visual + text line in the first 1–3s — no logo, no slow build?
- [ ] One structure, 6–8 beats, one action per shot?
- [ ] Image-to-video with a locked keyframe per shot (not text-to-video)?
- [ ] Exactly ONE CTA, shown + spoken, in the last 3–5s?
- [ ] Captions designed for mute (Meta) / sound designed-in (TikTok)?
- [ ] Correct aspect ratio for the platform?
- [ ] Testing each shot at 5s draft before Quality? One variable per regen?
- [ ] 3–5 hook variants planned for rotation?

## Cost discipline (from `ai-production.md`)
A 30s ad ≈ 5–8 clips. At Kling rates ≈ $4–12 raw. Storyboard-first cuts ~70%. Reserve Sora 2 / Veo Quality for 1–2 hero shots only. Test at 5s Fast/draft; change one variable per iteration; batch a campaign in one session.

## Anti-patterns (the ad-killers)
Logo-first opening · cinematic build with no hook payload · feature dumping · sound-on design for Meta · wrong aspect ratio · CTA after the drop-off · talking to everyone · over-polishing away authenticity · "story" with no product moment · no friction-reducer at the CTA.

## Related
- **`ai-video-director`** — generate each shot (mechanics, models, consistency). Always pair.
- **`ai-image-director`** — lock the keyframe before animating.
- **`video-content-strategist`** — channel/repurposing strategy around the ads.
- **`ad-creative`** — platform-constrained ad *copy* (RSA/Meta headlines) when you also need text ads.
