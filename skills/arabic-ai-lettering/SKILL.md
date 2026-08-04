---
name: arabic-ai-lettering
description: Produce Arabic text and calligraphy in AI-generated images and video without shipping gibberish. Use whenever Arabic words must appear inside a generated image, poster, thumbnail, ad, logo mock, reel, or video frame — Nano Banana, Seedream/Seedance, Ideogram, Flux, Midjourney, GPT Image, Qwen Image, fal, Higgsfield, Kling, Sora — or when a user asks for "Arabic calligraphy" from an image model, an Arabic headline in an ad creative, خط عربي في صورة, or is building a product that turns user-typed Arabic into artwork. Fires even when the user just says "put this Arabic text on it."
---

# Arabic lettering in AI-generated media

Image models render Arabic as **believable-but-wrong**: shapes that read as Arabic at a glance and are nonsense to anyone who actually reads it. Latin text degrades visibly (a wrong letter looks wrong); Arabic degrades invisibly to a non-reader, which is why this ships broken so often.

Arabic is unusually hostile to diffusion because four things stack: letters change shape by position (initial/medial/final/isolated), they connect along a baseline, the script runs right-to-left, and dots plus diacritics carry meaning at tiny scale. A model that nails an English poster will still drop a dot and turn نُور into بُور.

## The rule that prevents almost every failure

**Generate the picture, not the letters. Composite real text from a real font on top.**

The letters come from a shaping engine (browser, Figma, Illustrator, Pillow/HarfBuzz, SVG). The model supplies background, texture, lighting, ornament, and mood. This is not a workaround — it is how professional Arabic work is produced, and it makes the text editable, correct, accessible, and legally clean.

Ask the model for letters only when a wrong glyph is genuinely harmless (mood boards, style exploration, background texture that nobody will read) or when a fluent reader verifies the output before it ships.

## What you actually want → how to get it

| The ask | Do this | Not this |
|---|---|---|
| Arabic headline on an ad/poster | Model generates the scene with **empty space**; set the text in a real font over it | Prompting the headline into the image |
| Arabic logo / wordmark | Real font or commissioned calligrapher, vectorized | Any image model |
| Authentic Thuluth / Diwani composition | A calligrapher, or a licensed specialist face; AI output is reference only | Treating a generation as a deliverable |
| Ornament, arabesque, geometric pattern, background | Model — it's genuinely good at this | — |
| Texture on existing lettering (ink, foil, relief, gold) | Render text first, then img2img / inpaint the texture onto it | Text-to-image from scratch |
| Style exploration before committing | Model, freely — label the output "mood, not copy" | Showing a client AI Arabic as final |
| A product that renders user-typed Arabic | Font-render pipeline + effects. See below | An image model in the hot path |

## Prompting when you do generate

- **Suppress accidental text.** Models sprinkle fake Arabic into "Middle Eastern" scenes unprompted. Add `no text, no lettering, no calligraphy, no writing, no signage` when you plan to composite. This is the highest-value prompt line in this skill.
- **Reserve the space.** Ask for negative space where the text will land: "large empty dark area in the upper third for a title."
- **Name the tradition in English** (Thuluth, Diwani, Kufic, Naskh, Nastaliq) — the training data is labeled in English far more than in Arabic.
- **Short beats long.** One or two words survive; a sentence never does.
- **Give the model the letters as pixels, not as a prompt.** Render the word correctly, then use img2img / ControlNet / inpainting with that render as the structural input. This is the only reliable way to get styled *correct* Arabic out of a model.
- **Never paste Arabic Presentation Forms** (U+FB50–FEFC) into a prompt to "fix" shaping. Use normal Unicode.

## Model selection

Treat every claim here as a starting point and re-test on your exact words — text rendering changes with each release, and no model is dependable for Arabic.

- Models marketed as strong at text (Ideogram, Nano Banana Pro, GPT Image, Qwen Image) are stronger at **Latin and CJK** than at Arabic. "Good at text" in a launch post rarely means "good at cursive RTL."
- Non-Latin scripts are the documented weak spot across the field: large glyph sets and contextual shaping with far less clean training data, so output is plausible-looking and wrong.
- Video models (Seedance, Kling, Sora, Higgsfield) are worse than image models — letters drift and re-form between frames. For video, composite text in the edit (Remotion, After Effects, CSS) over generated footage, never inside the generation.

## The verification gate — non-negotiable

Never ship AI-generated Arabic you have not read back.

1. Zoom to 100% and read the words aloud. Do they say the intended thing?
2. Check every dot: ب ت ث ن ي and ج ح خ differ only by dots. Count them.
3. Check joining — letters must connect along the baseline; look for hairline breaks mid-word.
4. Check reading order: the first letter belongs on the **right**.
5. Check ا د ذ ر ز و — these never connect to the following letter. A model that joined them invented a letterform.
6. If tashkeel is present, confirm each mark sits on the correct letter, or remove tashkeel entirely.

If you cannot read Arabic, you cannot clear this gate — composite real text instead, or get a reader. Saying "the Arabic is unverified" is correct and cheap; shipping a nonsense word onto a client's poster is not.

## Building a product that generates Arabic designs

If the app takes user-typed Arabic and returns artwork, an image model must not be what draws the letters — the user's own words would come back mangled, and that is an unfixable trust bug.

The pipeline that works:

1. **Shape and render the text** with a real font through a proper shaping engine (HarfBuzz, or headless browser / SVG / Canvas). Output vector or high-res raster.
2. **Compose** — apply the style preset (seal, vertical stack, ink, foil, foliated ornament) as layout plus effects on that render.
3. **Use AI for everything that isn't a letter** — background, arabesque frames, paper texture, lighting.
4. **Keep the text layer separate and editable** to the last step so corrections don't require regeneration.

Style presets in a picker (seal, hand-drawn, balanced vertical, antique) are **compositions and treatments**, not fonts — see the `arabic-typography` skill's style taxonomy before wiring a picker, so the UI doesn't promise a "font" it cannot deliver. For which real families back each style, and for licensing when the app renders user text commercially, see `arabic-font-licensing` — server-side rendering into a paid product is a specific right that most font licenses withhold.

## Cultural care

Quranic verses, hadith, divine names, and sacred formulas must never be AI-generated. A dropped dot changes the word, and the result is offensive rather than merely wrong. Set these with a verified font, from a verified source text, and have a reader confirm — or decline the request.
