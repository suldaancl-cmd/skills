---
name: google-fonts-local
description: Use this for Google Fonts family lookup, webfont selection, CSS font loading, open-source font licensing buckets, variable fonts, multilingual font coverage, and local google/fonts repo metadata.
---

# Google Fonts Local

Original sparse clone: `C:\tmp\google-fonts`

References:

- Family path index: `references/google-fonts-family-index.md`
- Repository README: `references/google-fonts-readme.md`

Workflow:

1. Search the family index for the family slug and license bucket.
2. For detailed metadata, inspect the sparse git object with `git -C C:\tmp\google-fonts show HEAD:<bucket>/<family>/METADATA.pb`.
3. Use Google Fonts CSS imports or self-hosted font files according to the user's project constraints.
4. Pair fonts by role: display, body, UI label, code, numeric/data, and fallback stack.
5. Check language/script needs before recommending a family.

The clone is sparse by design, so it does not check out every binary font file.
