---
name: font-awesome-icon-lookup
description: Use this for searching Font Awesome icons by semantic term, label, unicode, style, category, alias, shim, or SVG metadata.
---

# Font Awesome Icon Lookup

Use these local references:

- `../font-awesome-local/references/font-awesome-icon-index.md`
- `../font-awesome-local/references/metadata/icons.json`
- `../font-awesome-local/references/metadata/categories.yml`
- `../font-awesome-local/references/metadata/shims.json`

Workflow:

1. Search the index by user meaning first.
2. Confirm exact icon id and styles in raw metadata.
3. Use shims only when migrating old icon names.
4. Return the icon id, available style, and implementation hint.
