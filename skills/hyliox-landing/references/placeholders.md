# Placeholders Reference

The hyliox mega-prompt defines 32 placeholders in §1. Fill every one before generating, or leave a clearly-marked `[TODO: {{NAME}}]` per anti-slop rule #5.

Group the questions to the user — don't dump all 32 at once. Suggested batches are documented in `SKILL.md` Phase 1.

## The 32 placeholders

| Placeholder | Type | Example | Default |
|---|---|---|---|
| `{{LANG}}` | BCP-47 code | `fr-CH` | `fr-CH` |
| `{{BRAND_NAME}}` | string | `ABP` | `Atelier` |
| `{{BRAND_TAGLINE}}` | 3-6 words | `Déménagement d'exception` | `Built for what's next` |
| `{{LOGO_PATH}}` | image path | `/logo.svg` | `/logo.svg` |
| `{{NAV_ITEMS}}` | array of `{label, href}` | `[{"label":"Services","href":"#services"}, ...]` | 4-5 items |
| `{{CTA_LABEL}}` | 1-3 words | `Devis gratuit` | `Get Started` |
| `{{CTA_HREF}}` | anchor/url | `#devis` | `#cta` |
| `{{FRAMES_PATH}}` | public path prefix | `/frames` | `/frames` |
| `{{FRAME_COUNT}}` | integer | `240` | `240` |
| `{{FRAME_EXT}}` | `jpg` or `webp` | `jpg` | `jpg` |
| `{{FPS}}` | integer | `30` | `30` |
| `{{HERO_HEADLINE}}` | 2-5 words (will be uppercased) | `Bouger, sans bruit.` | `Move, quietly.` |
| `{{HERO_SUB}}` | 1-2 sentences | `Du studio au penthouse. L'art du déménagement, signé {{BRAND_NAME}}.` | `One move. Zero friction.` |
| `{{HERO_CTA_PRIMARY}}` | 1-3 words | `Devis gratuit` | `Start now` |
| `{{HERO_CTA_SECONDARY}}` | 1-3 words | `Voir le film` | `Watch film` |
| `{{PARTNERS}}` | array of 5-6 strings | `["Christie's","Sotheby's","Piaget"]` | 5 brand names |
| `{{SERVICES}}` | array of 6 `{icon, title, body}` | see below | 6 entries |
| `{{REASONS}}` | array of 4 `{icon, title, body}` | see below | 4 entries |
| `{{PROCESS_STEPS}}` | array of 3-4 `{n, title, body}` | see below | 4 entries |
| `{{STATS}}` | array of exactly 4 `{value, label}` | `[{"value":"2500+","label":"déménagements"}, ...]` | 4 entries |
| `{{STATS_BG_VIDEO}}` | HLS or MP4 URL | `https://stream.mux.com/xxx.m3u8` | placeholder URL |
| `{{TESTIMONIALS}}` | array of ≥6 `{quote, name, role}` | see below | 6 entries |
| `{{FAQ_ITEMS}}` | array of 5-8 `{q, a}` | see below | 6 entries |
| `{{CTA_BG_VIDEO}}` | HLS or MP4 URL | `https://stream.mux.com/yyy.m3u8` | placeholder URL |
| `{{CTA_HEADLINE}}` | 4-7 words | `Prêts à partir ?` | `Ready to move?` |
| `{{CTA_SUB}}` | 1 sentence | `Un entretien. Un plan. Un déménagement.` | `One call. Done.` |
| `{{FOOTER_LINKS}}` | array of `{label, href}` | `[{"label":"Mentions","href":"/legal"}]` | 4 entries |
| `{{COPYRIGHT}}` | string | `© 2026 {{BRAND_NAME}} SA. Tous droits réservés.` | `© 2026 {{BRAND_NAME}}. All rights reserved.` |
| `{{COLOR_INK}}` | HSL triplet (no `hsl()` wrapper) | `20 15% 9%` | `20 15% 9%` |
| `{{COLOR_CREAM}}` | HSL triplet | `40 30% 90%` | `40 30% 90%` |
| `{{COLOR_OCHRE}}` | HSL triplet | `32 55% 65%` | `32 55% 65%` |
| `{{COLOR_TERRA}}` | HSL triplet | `14 55% 31%` | `14 55% 31%` |
| `{{FONT_DISPLAY}}` | Google Fonts family | `Oswald` | `Oswald` |
| `{{FONT_BODY}}` | Google Fonts family | `Inter` | `Inter` |

## Array shapes (verbatim from source)

### `{{SERVICES}}` — 6 entries

```js
[
  { icon: "Truck",       title: "Déménagement",  body: "..." },
  { icon: "Package",     title: "Emballage",     body: "..." },
  { icon: "Warehouse",   title: "Garde-meubles", body: "..." },
  { icon: "Globe",       title: "International", body: "..." },
  { icon: "Building2",   title: "Bureaux",       body: "..." },
  { icon: "Sparkles",    title: "Sur-mesure",    body: "..." },
]
```

### `{{REASONS}}` — 4 entries

```js
[
  { icon: "ShieldCheck", title: "Assuré intégralement",   body: "..." },
  { icon: "Clock",       title: "Ponctuels",              body: "..." },
  { icon: "Leaf",        title: "Éco-conscients",         body: "..." },
  { icon: "Award",       title: "Certifiés Swiss Moving", body: "..." },
]
```

### `{{PROCESS_STEPS}}` — 3-4 entries; `n` is `"01"`..`"04"`

```js
[
  { n: "01", title: "Brief",         body: "..." },
  { n: "02", title: "Devis",         body: "..." },
  { n: "03", title: "Coordination",  body: "..." },
  { n: "04", title: "Déménagement",  body: "..." },
]
```

### `{{STATS}}` — exactly 4 entries

```js
[
  { value: "2500+",  label: "Déménagements" },
  { value: "98%",    label: "Clients satisfaits" },
  { value: "24h",    label: "Délai de devis" },
  { value: "15 ans", label: "Métier" },
]
```

Numeric values are animated with a count-up motion span when in view (strip non-digits, preserve suffixes like `+`, `%`).

### `{{TESTIMONIALS}}` — ≥6 entries

```js
[
  { quote: "...", name: "Marie L.",     role: "Architecte d'intérieur" },
  { quote: "...", name: "Pierre M.",    role: "Galeriste" },
  // ... at least 6 total
]
```

The marquee duplicates the array to make the loop seamless. Real names + roles are non-negotiable per anti-slop rule #5.

### `{{FAQ_ITEMS}}` — 5-8 entries

```js
[
  { q: "Comment fonctionne le devis ?", a: "..." },
  { q: "Quelle est votre zone d'intervention ?", a: "..." },
  // ...
]
```

## Palette Defaults by Niche

The user can override any HSL triplet, but these niche-tuned defaults work as starting points:

### Warm luxury (default — moving, real estate, atelier brands)
```
COLOR_INK    = 20 15% 9%
COLOR_CREAM  = 40 30% 90%
COLOR_OCHRE  = 32 55% 65%
COLOR_TERRA  = 14 55% 31%
FONT_DISPLAY = Oswald
FONT_BODY    = Inter
```

### Cold editorial (fashion, gallery, design studio)
```
COLOR_INK    = 220 15% 8%
COLOR_CREAM  = 30 20% 92%
COLOR_OCHRE  = 0 0% 70%       (silver, not ochre — keeps the "cold" feel)
COLOR_TERRA  = 220 30% 18%
FONT_DISPLAY = Cormorant Garamond
FONT_BODY    = Inter
```

### Electric SaaS (B2B AI, dev tools — VOXR style)
```
COLOR_INK    = 250 30% 6%
COLOR_CREAM  = 0 0% 96%
COLOR_OCHRE  = 270 80% 65%    (electric violet primary)
COLOR_TERRA  = 280 50% 30%
FONT_DISPLAY = Space Grotesk
FONT_BODY    = Inter
```

### Earth retreat (wellness, hospitality, sustainability)
```
COLOR_INK    = 25 20% 12%
COLOR_CREAM  = 35 35% 88%
COLOR_OCHRE  = 30 45% 55%
COLOR_TERRA  = 20 35% 25%
FONT_DISPLAY = Fraunces
FONT_BODY    = Inter
```

## Common Mistakes

- **Forgetting the `hsl()` wrapper convention.** Triplets are stored bare (`20 15% 9%`) so Tailwind can do alpha math. Wrapping happens in `@theme` (`hsl(var(--ink))`).
- **Putting CSS variable colors in copy fields.** `{{HERO_HEADLINE}}` is plain text, not a color reference.
- **Mixing `BRAND_TAGLINE` (3-6 words) with `HERO_SUB` (1-2 sentences).** The tagline is the small chip in the navbar pill area; the sub is the paragraph under the headline.
- **Setting `FRAME_COUNT` before extraction.** Run `ffmpeg` first, then `ls public/frames | wc -l`, then update `constants.ts`.
- **Translating filled French placeholders to English when the user ran `LANG=fr-CH`.** Per anti-slop rule #13, leave them as-is.
