---
name: font-resources
description: One-stop reference for fonts, icons, and typography when building UIs — covers Google Fonts (use @fontsource npm, NOT clone 5GB google/fonts repo), Font Awesome (npm @fortawesome or CDN), Nerd Fonts (terminal/code use only, download from nerdfonts.com), plus a curated 213-line awesome-fonts list (typography tools, free fonts, emojis, iconic fonts, programming fonts, JS libs). Use when picking fonts for a project, adding Font Awesome icons, sourcing free fonts beyond Google Fonts, finding emoji libraries, picking a programming font, or when the user mentions Google Fonts / Font Awesome / Nerd Fonts / typography / font pairing. Pairs with ui-ux-pro-max (57 font pairings) and impeccable (typography polish).
---

# font-resources

Curated typography + icon resources. **No binaries cloned** — every font/icon source below has an npm or CDN install path that beats a multi-GB git clone.

## When to use

- Picking a font for a landing page, deck, or app
- Adding Font Awesome / Nerd Fonts / Google Fonts to a project
- Looking for free font alternatives to premium families
- Sourcing emoji libraries / iconic font packs
- Need a programming font (Inter, JetBrains Mono, Fira Code, Monaspace, Martian Mono, etc.)
- User mentions: "Google Fonts", "Font Awesome", "Nerd Fonts", "font pairing", "typography"

## Top-tier install patterns (use these, not git clone)

### Google Fonts → `@fontsource` npm (best for React/Next.js)

```bash
npm i @fontsource/inter @fontsource/dm-sans @fontsource-variable/space-grotesk
```

```js
import "@fontsource/inter/400.css"
import "@fontsource/inter/700.css"
import "@fontsource-variable/space-grotesk"
```

Why: per-weight tree-shaking, no FOIT, self-hosted (better Core Web Vitals than `fonts.googleapis.com`), no Google tracking.

**Alternative CDN** (faster for prototypes):
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
```

**Do NOT clone `github.com/google/fonts`** — it's 5+ GB of TTF binaries. Use `@fontsource` instead.

### Font Awesome → npm or CDN

```bash
npm i @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome
```

```jsx
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'
<FontAwesomeIcon icon={faArrowRight} />
```

**CDN:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<i class="fa-solid fa-arrow-right"></i>
```

**Do NOT clone `github.com/FortAwesome/Font-Awesome`** — the npm package gives you what you need, tree-shakable.

### Nerd Fonts → direct download per family (terminal/IDE use)

```
https://www.nerdfonts.com/font-downloads
```

Pick one family (JetBrainsMono Nerd Font, FiraCode Nerd Font, Hack Nerd Font, etc.) and download the ~10MB zip. NOT a web font — these are for terminals, VSCode, Neovim with extra glyphs (powerline, devicons, file icons).

**Do NOT clone `github.com/ryanoasis/nerd-fonts`** — 8+ GB. The web "font-downloads" page is the right entry point.

## Curated awesome-fonts list (213 lines, source: brabadu/awesome-fonts)

See `awesome-fonts.md` in this skill folder. Covers:

- **General typography tools**: Fontjoy (deep-learning pairing), Typewolf, Fonts In Use, FontAlternatives
- **Free font collections**: Apple Fonts, Fontshare, Font Squirrel, League of Moveable Type, IBM Plex, Mozilla Zilla Slab
- **Individual fonts worth knowing**: Inter, Monaspace (github), Martian Mono (evil martians), Barlow, Urbanist, Optician Sans, Redacted (wireframes)
- **Emoji libs**: twemoji, emojione, emojilib, node-emoji, vim-emoji
- **Iconic font packs**: Font Awesome, ionicons, octicons (GitHub), material-design-icons, Iconic, fontello
- **Programming fonts**: covered separately in awesome-fonts (Fira Code, Hack, Source Code Pro, etc.)
- **JS libs for runtime font work**: opentype.js, fontkit, fonteditor-core

Read `awesome-fonts.md` directly when picking; it's faster than reinventing categories.

## Banned defaults (per [[feedback_default_fonts_ban]])

When generating CSS / picking fonts, do NOT default to:
- ❌ Cormorant (overused for "luxury")
- ❌ Outfit (autopick for SaaS)
- ❌ JetBrains Mono (autopick for code blocks)
- ❌ Noto Kufi Arabic (autopick for Arabic)

Pull from the variation pool by brief type. Always do a ban check before writing CSS.

## Cross-references

- [[ui-ux-pro-max]] — 57 font pairings catalog (different layer; this skill is sources, that one is pairings)
- [[impeccable]] — typography polish/audit
- [[feedback_default_fonts_ban]] — what NOT to pick by default
- [[playbook_award_winning_web_design_2026]] — design playbook that often needs font picks
