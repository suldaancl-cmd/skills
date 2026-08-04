# Arabic typography implementation

Read this reference when the request includes HTML/CSS, a web app, an RTL audit, font loading, or production QA.

## Semantic direction and language

Set direction and language on the highest correct container:

```html
<html lang="ar" dir="rtl">
```

For mixed-language content, isolate complete runs rather than forcing a whole page into one direction:

```html
<p lang="ar" dir="rtl">
  السعر <bdi lang="en">Pro 2</bdi> هو <span dir="ltr">$49.00</span>
</p>
```

Use `<bdi>` for unknown or user-generated inline direction. Use `dir="ltr"` for known LTR tokens such as URLs, code, and Latin product names.

## Font stack and tokens

Use explicit Arabic and Latin tokens so each script can be tuned without scattering overrides:

```css
:root {
  --font-arabic-ui: "IBM Plex Sans Arabic", "Noto Sans Arabic", sans-serif;
  --font-arabic-display: "Reem Kufi", "Noto Kufi Arabic", sans-serif;
  --font-latin-ui: "IBM Plex Sans", system-ui, sans-serif;
}

:lang(ar) {
  font-family: var(--font-arabic-ui);
}

.display:lang(ar) {
  font-family: var(--font-arabic-display);
  line-height: 1.25;
}

.body-copy:lang(ar) {
  line-height: 1.65;
  letter-spacing: normal;
}
```

Treat these values as starting points. Inspect diacritics, ascenders, x-height-equivalent perception, and line collisions in the selected family before finalizing tokens.

## Font loading

Follow the project’s existing loading pattern. If self-hosting, declare only required files and weights, use WOFF2 where available, and keep the family’s license with the source distribution.

```css
@font-face {
  font-family: "Project Arabic";
  src: url("/fonts/project-arabic-regular.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}
```

Preload only a critical above-the-fold file. Too many Arabic subsets or weights can erase the performance benefit.

When privacy rules, content-security policy, offline use, or regional network reliability matter, prefer properly licensed self-hosting over a third-party font request. A remote font host can expose visitor metadata and become a rendering dependency.

## Layout

Prefer logical properties so the same component works in both directions:

```css
.card {
  padding-inline: 1rem;
  margin-inline-start: auto;
  border-inline-start: 3px solid currentColor;
  text-align: start;
}
```

Do not reverse logos, nondirectional icons, numerals, or media merely because the page is RTL. Mirror arrows and directional navigation only when their meaning changes with direction.

## Shaping safeguards

- Keep text as Unicode Arabic characters; do not paste presentation-form glyphs to “fix” shaping.
- Use a renderer with Arabic shaping and bidirectional support.
- Avoid splitting a connected word into per-letter spans for animation.
- Avoid arbitrary letter-spacing on connected text.
- Do not depend on `font-style: italic` unless the Arabic family includes a designed style that was tested.
- Preserve combining marks and test stacked diacritics after minification, copy/paste, PDF export, and video rendering.
- Use `font-variant-ligatures: normal` unless a tested design requirement says otherwise.

## Vertical and seal compositions

For the screenshot’s vertical composition presets, do not imitate Latin vertical type by rotating or stacking isolated Arabic letters. Build the treatment from complete connected words or short lines, preserve RTL reading order, and balance them optically. For a seal, create a dedicated SVG/vector composition after the wording is approved.

## QA matrix

Test at least:

| Surface | Check |
|---|---|
| Chrome/Edge/Firefox/Safari as relevant | Shaping, fallback, variable axes, layout width |
| iOS and Android as relevant | Fallback differences, clipping and line-height |
| PDF/print export | Embedded font, diacritics, outlines, selectable text |
| Figma/Adobe/office tools | Correct family version, shaping engine and editable delivery |
| Social/video renderer | Small counters, rasterization, motion per-word rather than per-letter |
| Mixed content | URLs, phone numbers, prices, dates, Latin brands and punctuation |

## Accessibility

- Keep meaningful Arabic text as text whenever possible.
- Provide an accessible text equivalent for outlined logo lettering.
- Do not use decorative calligraphy for long instructions or critical controls.
- Validate contrast and legibility at the delivered size, especially for thin strokes and dense Diwani/Nastaliq forms.

## Primary reference

- [W3C Arabic & Persian Layout Requirements](https://www.w3.org/TR/alreq/) — direction, bidirectional text, context-based shaping, baselines, ligatures, diacritics, and layout requirements.
