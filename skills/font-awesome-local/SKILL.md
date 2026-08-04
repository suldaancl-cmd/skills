---
name: font-awesome-local
description: Use this for Font Awesome icon lookup, React/web icon implementation, SVG/icon font usage, category search, unicode shims, webfonts, and local Font Awesome metadata from FortAwesome/Font-Awesome.
---

# Font Awesome Local

Original clone: `C:\tmp\Font-Awesome`

References:

- Icon index: `references/font-awesome-icon-index.md`
- Raw icon metadata: `references/metadata/icons.json`
- Categories: `references/metadata/categories.yml`
- Shims: `references/metadata/shims.json`

Workflow:

1. Search the icon index by semantic terms, label, or icon id.
2. Check raw metadata when exact styles, aliases, unicode, SVG, or version details matter.
3. Prefer SVG/React component usage for modern apps; use webfonts only when the project already relies on icon fonts.
4. Verify the requested style exists before naming an import or CSS class.
5. Keep accessibility in mind: decorative icons should be hidden from assistive tech; semantic icons need labels.
