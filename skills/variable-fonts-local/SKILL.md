---
name: variable-fonts-local
description: Use this for variable font selection and implementation, CSS font-variation-settings, optical sizing, weight/width axes, Google Fonts variable families, and performance-aware variable typography.
---

# Variable Fonts Local

Use these local references:

- `../google-fonts-local/references/google-fonts-family-index.md`
- `../awesome-fonts-local/references/awesome-fonts.md`

Workflow:

1. Confirm the variable font supports the needed axes by inspecting metadata when required.
2. Use standard CSS properties such as `font-weight`, `font-stretch`, and `font-optical-sizing` when possible.
3. Use `font-variation-settings` only for custom axes or precise control.
4. Keep axis ranges restrained so UI text remains readable.
5. Weigh one variable file against multiple static files for performance.
