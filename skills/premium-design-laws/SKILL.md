---
name: premium-design-laws
description: Standing law for premium typography, color, gradients, and symbol hygiene on ANY web / app / landing / UI / slide / design build. Load this BEFORE writing CSS or picking fonts/colors. Bans developer-looking decoration (// section labels, ----- / ===== ASCII rules, box-drawing, decorative slash/pipe/dot separators) in rendered output, and locks a curated premium type + color token system. Extends the default-fonts ban and colors-fonts-deck-first rules.
---

# Premium design laws

Operational rules. Full rationale + token tables in `audit/design-system-recommendations.md`; machine-readable sets in `audit/typography-options.json` and `audit/color-gradient-options.json`.

## 1. Symbol hygiene (rendered output only)

Do **not** emit, in visible design output:
- `//` used as a section LABEL (`// 01 — THE MISSION`, `// FEATURES`)
- ASCII rules: `-----`, `=====`, `~~~~~`
- box-drawing runs: `────`, `━━━`, `═══`
- decorative slashes / pipes / dots as separators in headings or labels

Replace with: vertical whitespace rhythm · a 1px hairline border token · a small uppercase eyebrow micro-label (tracking ~0.18em) · a kicker line · a numbered chip.

**Never blind-replace:** `//` in JS/TS/CSS is a real comment, `---` at the top of a SKILL.md is YAML frontmatter, `---`/`|` in markdown are valid. Leave those.

## 2. Typography

- Honor the default-fonts ban: do **not** default to Cormorant, Outfit, JetBrains Mono, or Noto Kufi Arabic. (They are allowed only for a deliberate, named role — e.g. mono for code/meta — never as a lazy fallback.)
- Use a real modular scale, a defined weight system, and explicit line-height + letter-spacing. Display tracking negative (~-0.02 to -0.03em); mono eyebrows positive (~0.18em).
- Strict role separation: display / body / meta are different families with different jobs.
- Pick a pairing from `audit/typography-options.json` by brief type; Arabic-first work uses the Arabic-safe options.

## 3. Color & gradient

- One disciplined accent system. No rainbow 3-stop gradients on headings (reads cheap). Gradients must be earned — same-family stops, or motivated by a real reference.
- Dark + light foundations with semantic tokens (bg / surface / border / text / accent / cta / states).
- WCAG-aware CTA contrast. No muddy colors, no low contrast, no accent bloat.
- Pick from `audit/color-gradient-options.json`.

## 4. Workflow

Deck first (3–4 color/font options) → lock via `ui-ux-pro-max` → build with `frontend-design` → polish with `impeccable`. This law governs all four steps.
