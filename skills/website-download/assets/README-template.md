# {SITE} — design mirror

Downloaded {DATE}. Stack: **{STACK}**. Assets on {CDN_HOSTS}.

## Serve it

```bash
cd {HOST_FOLDER} && python -m http.server 8080
```

Open `http://localhost:8080/`. **Serve `{HOST_FOLDER}` as the web root** — the
router assumes base `/`, and every asset reference was rewritten root-absolute
against it. Serving from the parent folder breaks routing and all rewritten
paths.

## What's inside

| Path | Contents |
|---|---|
| `{HOST_FOLDER}/` | {N_PAGES} pages — {PAGE_LIST} |
| `{HOST_FOLDER}/{BUILD_DIR}/` | {N_JS} JS chunks, {N_CSS} CSS, font subsets |
| `{HOST_FOLDER}/{CDN_DIR}/` | Images, icons, video, stylesheets |
| `_design-system/` | skillui extraction — tokens, references, screenshots |

## Verified {DATE}

Headless Chromium over local HTTP:

| Width | Failed requests | Broken images | First-party remote |
|---|---|---|---|
| 1440 | {X} | {X} | {X} |
| 1280 | {X} | {X} | {X} |
| 1024 | {X} | {X} | {X} |
| 768 | {X} | {X} | {X} |
| 390 | {X} | {X} | {X} |

Fonts resolved: {FONTS}. Video playable from disk: {VIDEO}.

## Known limits

- **Third-party stays remote by design** — {THIRD_PARTY}. Analytics, CRM, and
  form endpoints, not design assets. The page renders without them; forms will
  not submit.
- {N_DEAD} referenced paths 404 upstream too — dead links the site itself
  emits, confirmed by curling production. Not mirror gaps.
- Only the {N_PAGES} seeded pages. {EXCLUDED} were not crawled.
- Lazy images need real scrolling in a real browser; scripted scroll only
  trips a handful.
- {STACK_LIMITS}

## Licensing

{SITE}'s copyrighted design, copy, and assets. Local reference and study only.
Do not republish, redistribute, or ship derivative pages that reuse their
brand assets, logos, imagery, or copy.
