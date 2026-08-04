---
name: nerd-fonts-local
description: Use this for Nerd Fonts terminal font selection, patched programming fonts, glyph/icon support, Powerline/devicons/fontawesome terminal rendering, font patching, and install guidance from ryanoasis/nerd-fonts.
---

# Nerd Fonts Local

Original sparse clone: `C:\tmp\nerd-fonts`

References:

- Patched font index: `references/nerd-fonts-index.md`
- Raw patched font metadata: `references/fonts.json`
- README and patcher: `C:\tmp\nerd-fonts\readme.md`, `C:\tmp\nerd-fonts\font-patcher`

Workflow:

1. Search the patched font index for the desired original or patched family.
2. Prefer Nerd Font Mono variants for terminals and editor glyph alignment.
3. For app UI typography, use Nerd Fonts only when glyph coverage is required; otherwise prefer normal text fonts plus SVG icons.
4. For patching, inspect `font-patcher` and the README first; do not assume cloning the full repo is necessary.
5. Mention install route by platform only when asked; avoid downloading binary font archives unless the user requests installation.
