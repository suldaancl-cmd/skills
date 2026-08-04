# AI Production Pipeline (2026)

How to actually produce the ad with AI. Model selection, consistency, end-to-end assembly, and cost discipline. Pairs with `ai-video-director` (shot-level prompting mechanics). Model specs/prices change fast — **verify before a paid run.**

## Tool-Selection Matrix

| Model | Best-for in ads | Consistency mechanism | Approx cost | 
|---|---|---|---|
| **Kling 3.0** (Kuaishou) | Social hooks, product motion, 4K, text legibility in-frame | Character ID (identity locked from refs, ~90%+); first/last-frame keyframing | ~$0.029/sec on fal.ai; consumer $6.99–$127.99/mo |
| **Seedance 2.0** (ByteDance) | Multi-shot narratives needing native synced audio + lipsync in one pass; UGC-style | Physics-aware motion + consistent characters baked in; no post-sync | ~$0.077/sec Fast → $0.20–0.30/sec Std; ~$0.76 per 5s clip |
| **Veo 3.1** (Google) | Cinematic quality + synced ambient audio/dialogue baked in; TV-spot finishing | Native audio locked to video; Scene Extension; 4K upscale | $0.075 → $0.60/video; ~$0.15/sec Fast |
| **Runway Gen-4.5** | Agency-grade multi-shot; post-generation in-video edits; camera control | Reference-image system (face/outfit/props persist); Aleph text-driven edits ("add rain") | from $12/mo; ~5 credits/sec @1080p |
| **Sora 2** (OpenAI) | Longer clips (15–25s), physics-accurate motion, product lifestyle | Improved temporal consistency; image-to-video first-frame anchor | $0.30/sec → $0.50/sec HD (API); ChatGPT Plus $20 / Pro $200 mo |
| **Higgsfield Marketing Studio** (your MCP) | End-to-end ad factory: product URL → UGC / TV-spot / CGI; 40+ avatars; one-prompt | Soul ID locks face+body across generations; Kling+Seedance underneath; avatar pinning | Starter $15 / Plus $34 / Ultra $84 / Business $49 seat |
| **fal.ai** (platform/API) | Programmatic batch over Kling/Seedance/Veo/Wan; no subscription lock-in | Depends on underlying model; pay-per-use | $0.05–$0.40/sec by model; 600+ models |

**Cost anchor:** a finished 30s ad ≈ 5–8 clips of 3–5s. At Kling ($0.029/sec) raw generation ≈ **$4–12/ad**. Veo 3.1 Quality with audio ≈ $3–5. Sora 2 HD ≈ $75–200 for the same batch → **hero shots only.** [devtk.ai]

**Arabic audio:** Kling/Runway do NOT natively produce Arabic audio. Seedance/Veo native-audio Arabic coverage is **unconfirmed — verify.** Production-safe route: layer **ElevenLabs** (Arabic + regional accents, voice cloning) in post. [elevenlabs.io]

## Image-to-Video & Consistency Rules
- **Keyframe-first is mandatory for ads.** Text-to-video reinvents characters/products per shot; image-to-video locks identity to your asset. Always anchor from a product photo / character still.
- **Source image quality = output ceiling.** Min 1024×1024, sharp, clean light, no motion blur. A blurry input → blurry video.
- **Frame-chaining for multi-shot consistency.** Export the last clean frame of each clip → use as the first-frame input of the next. Most reliable anti-drift method across a 5-shot ad.
- **Kling Character ID** for humans (2–3 reference angles → identity embedding survives lighting/location, ~90%+).
- **Runway Gen-4 reference system** strongest for outfits/props/product across angles (no fine-tuning).
- **Product hero shots:** render/photograph at high res, then drive motion (slow orbit, dolly-in). Text-to-video rarely matches brand assets.
- **Archviz / real estate:** render 2–3 hero stills traditionally (V-Ray/Corona/3ds Max) or with archviz AI, then drive AI video from those. Full AI-gen still struggles with material accuracy + geometric precision for top-tier work.
- **Labels/text in-frame:** Kling 3.0 leads on legibility (signs, price tags, logos).

## End-to-End Ad Assembly Workflow
1. **Brief lock** — subject, audience, format (9:16/1:1/16:9), duration (15–30s), tone, hook type, spoken language.
2. **Storyboard into 3–8 shots** — one sentence per shot (framing, action, mood). Never one mega-prompt. 3–5s/clip.
3. **Prepare source assets** — product at 1024px+ clean bg; avatar via Higgsfield Soul ID / Kling Character ID (2–3 angles); archviz hero stills.
4. **Generate clips (image-to-video).** Pick model: budget/social hooks → Kling; UGC + baked audio → Seedance; cinematic + ambient audio → Veo 3.1; post-edit control → Runway; long hero clips → Sora 2 (sparingly). Generate at **5s Fast/draft** first; approve composition before Quality.
5. **Frame-chain** — last clean frame → next first-frame.
6. **Voiceover** — ElevenLabs (Arabic/multilingual, clone brand voice) OR Higgsfield avatar lip-sync.
7. **Music bed** — Suno Pro / Udio (commercial rights, royalty-free); prompt tempo+mood+duration, no lyrics.
8. **Assemble + caption** — Descript or CapCut (auto-captions, text-based edit). Captions non-optional.
9. **QA** — shot-to-shot consistency, audio sync, caption accuracy (esp. brand names), platform-UI safe zones, color continuity.
10. **Export** — 9:16 TikTok/Reels/Shorts; 1:1/4:5 Meta feed; 16:9 YouTube/CTV. 1080p min; 4K upscale for hero.

## Cost Discipline
- **Test at 5s, Fast tier, draft** before Quality. Validate composition + character lock first.
- **Change one variable per iteration.** Never regenerate an approved shot to "try something."
- **Storyboard-first cuts cost ~70%** (~$1.50/clip vs ~$5 blind).
- **Reserve Sora 2 / Veo Quality for 1–2 hero shots** (10–20× the per-second cost of Kling/Wan).
- **Watch billing/expiry:** Higgsfield top-up credits expire in 90 days; verify monthly vs annual at checkout.
- **Batch a campaign in one session** while references are loaded; use **fal.ai** for 50+ ads/month programmatic.

## Sources
Higgsfield (official pricing, Marketing Studio, Soul ID) · imagine.art · flowith.io · invideo.io · atlascloud.ai (Kling, Seedance, image-to-video) · segmind · buildfastwithai · OpenRouter (Veo pricing) · veo3ai.io · runwayml.com/research · selfielab.me · aumiqx.com · aifreeapi.com · wavespeed.ai · buildmvpfast · devtk.ai · fal.ai (official) · fluxnote.io · magichour.ai · genra.ai · renderai.app · blog.chaos.com · medium.com/@paoloperrone · seowerkz.com · Suno (dynamoi, aivideobootcamp) · ElevenLabs (official) · imagine.art (AI editors)
