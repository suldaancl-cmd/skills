# Arabic style taxonomy

Use this reference when identifying a style, translating the screenshot labels into standard terminology, or deciding whether a request needs a font or custom lettering.

## Source taxonomy from the supplied screenshots

The screenshots show twelve labels. Six are script-oriented categories, two are historical or mood descriptions, and four are primarily treatments or compositions. The classification below preserves the user-facing Arabic labels while preventing category mistakes.

| Screenshot label | Working English name | Kind | Recognition cues | Best suited to | Important caution |
|---|---|---|---|---|---|
| خط النسخ | Naskh | Established cursive tradition | Open, balanced letterforms; clear word rhythm; strong legibility; familiar book texture | Body text, books, education, editorial and formal reading | “Naskh” covers many interpretations; compare proportions and diacritics before identifying a specific family |
| خط الثلث | Thuluth | Established cursive tradition | Tall ascenders, sweeping curves, pronounced contrast, layered or interlaced composition | Ceremonial headings, architectural inscriptions, religious or monumental display | Authentic results often require a calligrapher or specialist display face; not appropriate for body copy |
| خط الديواني | Diwani | Established cursive tradition | Dense flowing texture, rising/curving baselines, compact counters, ornamental connections | Invitations, luxury identities, certificates, formal decorative display | High density reduces small-size legibility; ordinary script fonts are poor substitutes |
| خط الرقعة | Ruqʿah / Ruqaa | Established handwriting tradition | Compact words, simplified shapes, short strokes, handwritten speed and firmness | Informal headings, notes, human brand accents, short phrases | Use for short text; very small counters and compressed rhythm can hinder body reading |
| التعليق الفارسي | Persian Nastaliq / Taʿlīq family | Established Persianate tradition | Diagonal descending word groups, suspended rhythm, strong thick–thin contrast, cascading lines | Persian/Urdu poetry, cultural/editorial display, elegant short text | Arabic support alone does not guarantee Persian/Urdu quality or conventions; test the exact language |
| الفاطمي المورق | Foliated Fatimid-style Kufi | Historical/decorative Kufi description | Angular skeleton combined with leaf, vine, or vegetal terminals and dense ornament | Heritage identities, museum graphics, architectural or exhibition display | Usually custom lettering/illustration, not a single standard font family; verify the intended historical reference |
| الكوفي الحديث | Modern Kufi | Contemporary Kufi-oriented category | Geometric construction, straighter strokes, modular counters, reduced ornament | Logos, UI display, wayfinding, packaging, technology and architecture | “Modern Kufi” is broad; distinguish text Kufi from highly geometric display designs |
| عتيق | Antique / heritage treatment | Mood or app preset | Aged, manuscript-like, distressed, archival, or deliberately irregular texture | Heritage campaigns, packaging, historical mood boards | Not a canonical script. Ask which historical period or base tradition is intended |
| خط اليد | Hand-drawn Arabic | Treatment/category | Natural irregularity, pen/brush variation, personal baseline and spacing | Personal brands, social graphics, signatures, informal storytelling | A hand-drawn look may be a font, lettering, or raster effect; identify the production requirement |
| خط الخاتم | Seal composition | Composition | Circular, square, emblematic, or interlocked arrangement optimized as a mark | Stamps, badges, monograms, seals and avatar-scale identities | The layout is the defining feature. The underlying letters may be Kufi, Thuluth, or custom forms |
| متوازن عمودي | Balanced vertical composition | Composition preset | Centered/stacked lines, controlled widths, stable vertical mass | Posters, titles, covers and narrow formats | Manual line breaks and optical balancing matter more than the font name |
| إنسيابي عمودي | Flowing vertical composition | Composition preset | Stacked text with more movement, curves, overlap, or changing line widths | Expressive posters, reels, motion titles and editorial display | Preserve reading order and joining; never stack isolated letters merely to mimic Latin vertical type |

## Broad recognition families

UNESCO describes a useful first division between geometric/angular calligraphy and curved/flowing calligraphy. Use it only as a first pass:

- **Angular/geometric:** early and decorative Kufi, modern Kufi, many seal constructions.
- **Curved/flowing:** Naskh, Thuluth, Ruqʿah, Diwani, Taʿlīq/Nastaliq.

Then narrow the classification using baseline, proportions, density, and intended function.

## Discriminating close styles

### Naskh vs Thuluth

- Naskh prioritizes repeatable reading rhythm and moderate proportions.
- Thuluth emphasizes monumental verticals, sweeping curves, and composed display impact.

### Ruqʿah vs Diwani

- Ruqʿah looks quicker, simpler, firmer, and more handwritten.
- Diwani looks more ornamental, compressed, interwoven, and ceremonially flowing.

### Naskh vs Nastaliq

- Naskh usually maintains a steadier reading line.
- Nastaliq creates diagonal, descending, suspended word groups.

### Historical Kufi vs modern Kufi

- Historical/decorative Kufi depends on period-specific structures and may include knots, leaves, or architectural ornament.
- Modern Kufi simplifies geometry for contemporary identity and display use.

## Confidence language

Use `high` only when multiple structural cues agree. Use `medium` when the image is stylized or low resolution. Use `low` when a logo modifies the letters so heavily that the base tradition is uncertain.

Example:

```text
Most likely: modern Kufi (الكوفي الحديث) — medium confidence.
Cues: modular square counters and a predominantly horizontal/vertical skeleton.
Closest alternative: a custom seal composition based on Kufi.
```

## References

- [UNESCO Silk Roads: Manuscript](https://en.unesco.org/silkroad/silk-road-themes/mouvable-heritage-and-museums/manuscript) — broad geometric/angular and curved/flowing categories.
- [W3C Arabic & Persian Layout Requirements](https://www.w3.org/TR/alreq/) — Arabic-script styles, shaping, direction, baselines, ligatures, and diacritics.
