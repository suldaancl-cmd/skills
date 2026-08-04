---
name: google-fonts-family-lookup
description: Use this for looking up Google Fonts family slugs, license buckets, metadata paths, language/script coverage hints, and local google/fonts sparse-clone paths.
---

# Google Fonts Family Lookup

Use these local references:

- `../google-fonts-local/references/google-fonts-family-index.md`

Workflow:

1. Search the family index for a slug or likely normalized family name.
2. Use the listed bucket/path to inspect metadata with `git -C C:\tmp\google-fonts show HEAD:<bucket>/<family>/METADATA.pb` when details matter.
3. Check style/weight/script needs before recommending implementation.
4. Remember the clone is sparse and intentionally avoids binary font checkout.
