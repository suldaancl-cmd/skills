---
name: font-icons-local
description: Use this for icon fonts and glyph systems, including Font Awesome, Nerd Fonts, SVG icons, unicode glyphs, icon accessibility, and choosing between icon fonts and SVG components.
---

# Font Icons Local

Use these local references:

- `../font-awesome-local/references/font-awesome-icon-index.md`
- `../font-awesome-local/references/metadata/icons.json`
- `../nerd-fonts-local/references/fonts.json`

Workflow:

1. Prefer SVG icons for web UI unless the project already uses icon fonts.
2. Use Font Awesome for product UI icons and Nerd Fonts for terminal/editor glyphs.
3. Check exact icon id, style, unicode, and availability before implementation.
4. Add accessible names only when icons communicate meaning; hide decorative icons.
5. Avoid mixing icon sets unless visual style remains coherent.
