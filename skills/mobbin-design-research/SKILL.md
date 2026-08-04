---
name: mobbin-design-research
description: Search and analyze Mobbin iOS and web screens, website sections, and flows; cite canonical references; and export targeted JPEG batches with a manifest. Use for Mobbin design research, UI pattern comparisons, screen or flow inspiration, and permitted local reference downloads. Do not use for full-library mirroring, Android catalogs, or video extraction.
---

# Mobbin Design Research

Use Mobbin as a targeted reference source, not as a corpus to mirror.

## Boundaries

- Use the Mobbin MCP tools for discovery. Never scrape or bypass access controls.
- Treat `ios` and `web` as the only supported app platforms. If Android is requested, state that the connector rejects it; do not relabel iOS designs as Android.
- Treat flow results as ordered still frames. Do not claim they contain downloadable animation or video data.
- Do not create a standalone Mobbin repository or bulk mirror. Export only a user-relevant, query-scoped batch for internal reference.
- Preserve existing exports by creating a new timestamped folder.

## Research workflow

1. Convert the request into one concrete screen, section, or journey query. Avoid vague keyword lists and combined intents.
2. Choose the tool:
   - `search_screens`: iOS or web UI screens, maximum 30 results.
   - `search_sections`: website sections, maximum 30 results.
   - `search_flows`: iOS or web journeys, maximum 10 flows per page.
3. Use `standard` screen search for direct patterns and `deep` only when intent is nuanced.
4. Inspect every returned image used in the answer. Never describe a result from metadata alone.
5. Cite each mentioned screen or flow with its canonical `mobbin_url`.
6. Deduplicate exports by screen or section ID.

## Targeted export

Build a JSON manifest with an `assets` array. Give each asset:

- `id`: Mobbin screen or section ID.
- `image_url`: returned short-lived image URL.
- `mobbin_url`: canonical reference URL.
- `relative_path`: safe path such as `ios/screens/<id>.jpg`.

Run:

    python scripts/download_manifest.py manifest.json "D:\Mobbin\export_<timestamp>"

Use `--limit N` for a small sample and `--workers N` to lower concurrency after network errors. Keep `manifest.json` beside the downloaded images.

## Verification

- Confirm manifest asset count equals unique JPEG count.
- Validate JPEG magic bytes, not just file extensions.
- Report saved count, failed count, bytes, and absolute destination.
- If any download fails, retry only failed files with lower concurrency.

