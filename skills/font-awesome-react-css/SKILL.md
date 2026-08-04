---
name: font-awesome-react-css
description: Use this for implementing Font Awesome in React, HTML, CSS, SVG sprites, webfonts, accessibility labels, and migration from old fa class names.
---

# Font Awesome React And CSS

Use these local references:

- `../font-awesome-local/references/metadata/icons.json`
- Original clone: `C:\tmp\Font-Awesome`

Workflow:

1. Check whether the project already uses Font Awesome packages, CSS classes, webfonts, or inline SVG.
2. Match the existing implementation path before adding a new dependency.
3. Verify icon style availability before importing.
4. Use accessible labels for semantic icons and `aria-hidden` for decoration.
5. For migration, consult shim metadata before renaming icons.
