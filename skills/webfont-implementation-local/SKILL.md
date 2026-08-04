---
name: webfont-implementation-local
description: Use this for implementing web fonts with CSS, @font-face, Google Fonts CSS, self-hosting, preload, font-display, fallback stacks, variable fonts, and performance-aware typography.
---

# Webfont Implementation Local

Use these local references:

- `../google-fonts-local/references/google-fonts-family-index.md`
- `../awesome-fonts-local/references/awesome-fonts.md`

Workflow:

1. Check the project's framework and existing font loading pattern.
2. Prefer `font-display: swap` or an established local convention.
3. Use `@font-face` for self-hosting and Google Fonts CSS when network loading is acceptable.
4. Preload only critical above-the-fold font files.
5. Define fallback stacks that preserve metrics reasonably.
6. Keep edits scoped to typography files, theme tokens, or layout surfaces that actually need the font.
