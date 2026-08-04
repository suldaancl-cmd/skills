---
name: google-fonts-webfont-implementation
description: Use this for implementing Google Fonts in web apps, Next.js, CSS imports, self-hosting, font-display, preload strategy, fallback stacks, and performance tradeoffs.
---

# Google Fonts Webfont Implementation

Use these local references:

- `../google-fonts-local/references/google-fonts-family-index.md`
- `../google-fonts-local/references/google-fonts-readme.md`

Workflow:

1. Check the framework's preferred font loading path first.
2. For Next.js, prefer the project's established `next/font` pattern if present.
3. For plain CSS, use `@import` or `<link>` only when external loading is acceptable.
4. For self-hosting, define `@font-face`, `font-display`, weights, styles, and fallbacks explicitly.
5. Avoid loading unused weights, italics, or scripts.
