# Practical Arabic font catalog

Use this as a shortlist generator, not as a substitute for testing. All listed families appeared in the local Google Fonts repository index under the OFL bucket when this skill was checked on 2026-08-02. Re-check the current family metadata and the bundled license file before production, redistribution, embedding, or logo delivery.

Every family named below was verified against the live Google Fonts API on 2026-08-02 — hosted, with real Arabic coverage. Before recommending any family **not** on this page, confirm it exists: `python scripts/verify_families.py "Family Name"`. Plausible-sounding names such as "Noto Serif Arabic", "Sofia Sans Arabic" and "Uthman Taha" are not hosted on Google Fonts. For sourcing beyond Google Fonts, commercial foundries, and the licence bucket needed when a product renders user text server-side, see the `arabic-font-licensing` skill.

## Strong open-source starting points

| Family | Closest design category | Good roles | Main caveat |
|---|---|---|---|
| Amiri | Classical Naskh-oriented serif | Books, long-form editorial, formal and literary work, diacritic-rich text | Traditional texture may feel too formal for dense product UI |
| Noto Naskh Arabic | Naskh | General reading, multilingual fallback, editorial and documents | Confirm the required weight range and platform rendering |
| Scheherazade New | Naskh-oriented literary face | Extended Arabic-script coverage, books, scholarship, text with diacritics | Generous forms need line-height and width testing |
| Lateef | Traditional Naskh-oriented text/display | Literary, cultural and friendly editorial work | Test at small UI sizes before adopting broadly |
| Aref Ruqaa | Ruqʿah | Short headings, quotes, invitations and human accents | Not a body/UI default |
| Aref Ruqaa Ink | Inked Ruqʿah treatment | Expressive headings and handcrafted graphics | Texture and compactness lose clarity at small sizes |
| Noto Nastaliq Urdu | Nastaliq | Urdu and Persianate display/editorial use | Cascading lines require generous vertical spacing; test Arabic/Persian/Urdu separately |
| Gulzar | Nastaliq | Urdu/Persian poetry, display, cultural editorial | Do not assume it is the best choice for Modern Standard Arabic body text |
| Noto Kufi Arabic | Text/display Kufi | Modern identity, headings, UI accents and multilingual fallback | Geometric tone can become rigid in long paragraphs |
| Reem Kufi | Contemporary Kufi display | Brand headings, posters, packaging and logos | Use restrained weights and test tight counters |
| Reem Kufi Ink | Inked Kufi treatment | Heritage-modern display, social graphics and expressive headlines | A treatment font, not an authentic substitute for every historic Kufi style |
| Kufam | Contemporary Kufi | Digital products, wayfinding, modern editorial and identity | Confirm its tone against the exact Arabic copy; it can feel technical |
| IBM Plex Sans Arabic | Contemporary Arabic sans | Product UI, dashboards, corporate systems and bilingual IBM Plex pairings | A modern sans, not a classical calligraphy style |
| Cairo | Contemporary Kufi-influenced sans | Interfaces, marketing, dashboards and broad web use | Familiarity can make distinctive brand work feel generic |
| Tajawal | Contemporary Arabic sans | Friendly marketing, mobile interfaces, labels and body text | Check very light weights and small-size contrast |
| Vazirmatn | Contemporary Persian/Arabic sans | Persian-first interfaces, multilingual products and data-heavy UI | Validate Arabic regional preferences when the product is Arabic-first |

## Map the screenshot categories to production approaches

| Requested category | Honest production approach | Starting points |
|---|---|---|
| Naskh | Use a tested text family | Amiri, Noto Naskh Arabic, Scheherazade New, Lateef |
| Thuluth | Prefer commissioned/custom lettering or a verified specialist family | Do not present a generic Google font as authentic Thuluth |
| Diwani | Prefer custom lettering or a properly licensed specialist family | Test ornament and readability; avoid false open-source equivalence |
| Ruqʿah | Use a Ruqʿah family for short display text | Aref Ruqaa, Aref Ruqaa Ink |
| Persian Nastaliq | Use a language-tested Nastaliq family | Noto Nastaliq Urdu, Gulzar |
| Foliated Fatimid | Construct custom Kufi lettering plus period-appropriate vegetal ornament | A Kufi family may provide a sketch base, but the ornament is custom |
| Modern Kufi | Use a geometric Kufi-oriented family | Reem Kufi, Noto Kufi Arabic, Kufam |
| Antique | Choose the base tradition first, then add a reversible print/ink texture | Amiri for manuscript tone; Reem Kufi Ink or Aref Ruqaa Ink for ink character |
| Hand-drawn | Decide whether editable type or unique lettering matters more | Aref Ruqaa Ink, Reem Kufi Ink, or commissioned lettering |
| Seal | Design a compact composition; the font is only raw material | Reem Kufi or Noto Kufi Arabic as a base, then optical customization |
| Balanced vertical | Stack complete words/lines and balance their visual widths | Kufi-oriented display families often adapt well |
| Flowing vertical | Compose complete connected words with controlled movement | Custom lettering or a flowing display tradition; protect reading order |

## Pairing recipes

### Modern bilingual product

- Arabic UI/body: IBM Plex Sans Arabic or Cairo.
- Latin UI/body: IBM Plex Sans or a metrics-compatible neutral sans.
- Arabic display: Reem Kufi only if the brand needs a separate display voice.
- Keep data, numerals, and labels visually aligned across scripts.

### Editorial and cultural

- Arabic body: Amiri, Noto Naskh Arabic, or Scheherazade New.
- Latin companion: a book serif with comparable seriousness and moderate contrast.
- Display: use the same Arabic family at a stronger size/weight before introducing calligraphy.

### Premium invitation or identity

- Arabic mark: custom Diwani, Thuluth, or Ruqʿah lettering according to tone.
- Supporting Arabic text: a restrained Naskh or contemporary sans.
- Latin companion: choose by formality and stroke contrast, not by superficial resemblance.

## Selection checklist

1. Does the family support the exact language and punctuation?
2. Do all required letters join correctly in the target software?
3. Are diacritics positioned cleanly at the final size and weight?
4. Are small counters still open after export, compression, or video rendering?
5. Do Arabic and Latin lines feel optically compatible rather than numerically identical?
6. Is the license suitable for web embedding, app bundling, editable client delivery, and logo use?
7. Does the family remain legible without relying on an image preview from another font version?

## Sources

- [Google Fonts repository](https://github.com/google/fonts) — family files, metadata, descriptions, and per-family license files.
- [W3C typeface styles and font fallback](https://www.w3.org/International/articles/typography/fontstyles.en.html) — script-specific style and fallback considerations.
