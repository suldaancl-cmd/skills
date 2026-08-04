---
name: arabic-typography
description: Select, identify, pair, audit, and implement Arabic fonts and calligraphic styles for brands, logos, headlines, editorial work, documents, social graphics, and RTL interfaces. Use whenever the user mentions Arabic fonts, Arabic typography, Arabic calligraphy, خط عربي, خطوط عربية, Naskh, Thuluth, Diwani, Ruqah, Kufi, Nastaliq, tashkeel, Arabic font pairing, an Arabic logo or headline, RTL type, or asks to identify an Arabic style from an image—even if they only ask for “a nice Arabic font.”
compatibility: Works with text-only requests; use image viewing for visual identification. Verify current font availability and license terms before production use.
---

# Arabic Typography

Choose Arabic type by script tradition, language, reading context, and implementation constraints. Treat the screenshots that inspired this skill as a useful style menu, not as proof that every label is a downloadable font family.

## Core distinction

Keep these three layers separate because confusing them produces weak recommendations:

1. **Calligraphic tradition** — Naskh, Thuluth, Diwani, Ruqʿah, Nastaliq, Kufi.
2. **Font family** — a specific digital implementation such as Amiri or Reem Kufi.
3. **Composition or treatment** — a seal, vertical stack, ink effect, hand drawing, or foliated ornament.

Say which layer you mean. Never present a composition preset such as “seal” or “balanced vertical” as a historical script or a downloadable font family.

## Workflow

### 1. Establish the brief

Infer what is already clear, then resolve only details that change the answer:

- Language and locale: Arabic, Persian, Urdu, or another Arabic-script language.
- Role: long-form body text, interface text, display heading, logo, packaging, religious/editorial work, or experimental art.
- Medium: web, app, print, slides, video, social graphic, or generated image.
- Exact text, including whether diacritics/tashkīl must appear.
- Desired tone: readable, formal, monumental, intimate, luxurious, historic, geometric, or expressive.
- License and delivery constraints: open-source, commercial permitted, self-hosted, editable text, or outlined artwork.

Arabic, Persian, and Urdu share a script but not identical glyph preferences or typographic conventions. Do not treat support for one as proof of high-quality support for all three.

### 2. Inspect visual evidence

When an image or screenshot is supplied, inspect it before naming the style. Compare stroke angle, baseline behavior, proportions, density, geometry, ligatures, ornament, and composition.

Read [references/style-taxonomy.md](references/style-taxonomy.md) for the recognition guide. If evidence is ambiguous, return the top two candidates and explain the discriminating feature instead of claiming certainty.

### 3. Choose the tradition before the family

Match purpose to tradition:

- Reading and editorial continuity → Naskh-oriented designs.
- Monumental or ceremonial display → Thuluth or custom display lettering.
- Ornamental elegance → Diwani or custom lettering.
- Fast, informal handwritten character → Ruqʿah.
- Persian/Urdu cascading texture → Nastaliq, after language testing.
- Geometric identity, architecture, or modern display → Kufi-oriented designs.

Some authentic Thuluth, Diwani, foliated Kufi, seal, and vertical compositions require custom lettering. Say so plainly; a convenient web font is not automatically an authentic substitute.

### 4. Shortlist actual families

Read [references/font-catalog.md](references/font-catalog.md). Return at most three strong candidates unless the user asks for a survey. For each candidate include:

- Exact family name.
- Closest tradition or design category.
- Recommended role and weight.
- Language/script coverage caveat.
- Source and license status, or a clear “verify before use” note.
- Why it fits the supplied words and medium.

Avoid recommending a family only because its name sounds Arabic. Confirm that it contains the required Arabic-script glyphs and shapes the exact sample correctly.

### 5. Test with the user’s real text

Use the exact text whenever it is available. Preserve Unicode characters; do not replace letters with Arabic Presentation Forms. Test at least:

```text
اللغة العربية — لآلئُ الخطِّ الجميل — مسؤولية — ١٢٣٤٥ / 12345
```

Check:

- Initial, medial, final, and isolated shaping.
- Lam–alef and common ligatures.
- Dots and stacked diacritics at intended sizes.
- Baseline rhythm and collisions.
- Arabic and Latin numerals.
- Mixed Arabic/Latin product names, URLs, and prices.
- All required weights in the actual browser, editor, or renderer.

Do not judge an Arabic family from a Latin-only specimen.

### 6. Implement or hand off appropriately

For web/app work, read [references/implementation.md](references/implementation.md). Set language and direction semantically, preserve shaping, and use logical layout properties. For logos or decorative compositions, keep the wording editable until approved, then outline a copy only for final artwork while retaining the editable source.

## Recommendation output

Use this compact structure unless the user requests a different deliverable:

```markdown
## Direction
[Chosen tradition/treatment and the reason]

## Shortlist
| Family or approach | Role | Why it fits | Source/license | Caveat |
|---|---|---|---|---|

## Type recipe
- Display:
- Body/UI:
- Latin companion:
- Size/weight/line-height:
- Fallback stack:

## Arabic QA
[Results for shaping, diacritics, mixed text, small sizes, and license]
```

For style identification, start with `Most likely: [style] ([Arabic label])`, give confidence as high/medium/low, cite two visual cues, and list the closest alternative.

## Quality rules

- Favor one Arabic family plus one compatible Latin companion. Add families only when roles genuinely differ.
- Use weight, size, spacing, and contrast to create hierarchy before adding another family.
- Avoid positive letter-spacing on connected Arabic body text; it can break texture and joining expectations. Use a better width, size, weight, or composition instead.
- Give Arabic body text enough vertical room for ascenders and diacritics; validate the actual font instead of applying one universal percentage.
- Do not synthesize fake italics for Arabic. Choose a designed alternate or another hierarchy cue.
- Do not use Nastaliq merely as an exotic Arabic accent; confirm the language, reading order, and glyph repertoire.
- Do not imitate sacred or historical calligraphy casually in contexts where cultural accuracy matters. Recommend a calligrapher or specialist review when authenticity is central.
- Treat font-repository license buckets as discovery metadata, not legal advice. Check the license file shipped with the chosen family before redistribution, embedding, or logo delivery.

## Source discipline

Use current primary sources for claims about availability, supported scripts, axes, and licenses. Prefer the font project’s repository or foundry page, the Google Fonts family metadata, W3C Arabic layout guidance, and Unicode/OpenType documentation. Flag approximations and unresolved uncertainty.

