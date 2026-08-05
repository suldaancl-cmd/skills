# Per-stack recipes and traps

The fingerprint step names the stack. Read only that section. Difficulty is
about how much repair work the crawl leaves behind, not download size.

## Contents

- [Webflow](#webflow) — easiest
- [Astro / static](#astro--static)
- [Framer](#framer)
- [Next.js](#nextjs)
- [Nuxt](#nuxt) — hardest
- [WordPress / WooCommerce](#wordpress--woocommerce)
- [Shopify headless](#shopify-headless)

---

## Webflow

Signature: assets on `cdn.prod.website-files.com`, `Server: cloudflare`.

Pure static HTML/CSS/JS with no hydration step, so the crawl mostly just
works. Span to `cdn.prod.website-files.com`, `cdn.jsdelivr.net`,
`cdnjs.cloudflare.com`, and the Google Fonts hosts.

**The one real trap: fonts.** Webflow loads its primary typeface through
`WebFont.load({google:{families:[...]}})` at runtime. `--page-requisites`
never sees it, so the mirror silently falls back to a system font — and a
Playfair-to-Times swap is obvious on sight. Fetch the Google Fonts v1 CSS
with a Chrome UA (an old UA returns TTF instead of WOFF2), pull each
`fonts.gstatic.com` WOFF2, rewrite `src` to the local copy, and inject the
stylesheet before `</head>`. Leave the dead `WebFont.load` call in place; the
local `@font-face` wins in both online and offline modes.

Verify fonts with `performance.getEntriesByType('resource')` showing zero
`gstatic` requests. `document.fonts.check()` lies — it returns false until the
text scrolls into view, so `await document.fonts.load(...)` first.

Award-style Webflow sites with bespoke GSAP + ScrollTrigger + Lenis + Three.js
scroll experiences download fine and render, but the pinned/horizontal/WebGL
runtime is best-effort offline. Headless verification is misleading here:
Lenis ignores `window.scrollTo` (drive it with dispatched `WheelEvent`s) and
the WebGL canvas can sit at height 0 until a real resize. Say so plainly and
tell the user to scroll it in a real browser rather than baking speculative
fixes.

## Astro / static

Signature: `astro-` class hashes, `_astro/` directory.

Mirrors cleanly. Standard recipe, no special handling.

## Framer

Signature: `Server: Framer`, thousands of `data-framer-*`, assets on
`framerusercontent.com`.

SSRs full content so the text and layout mirror well. Four traps:

1. **Navigation is JS, not `href="/..."`.** wget cannot discover pages by
   crawling. Seed it with every sitemap URL explicitly or you get one page.
2. Span to `framerusercontent.com` and `app.framerstatic.com`.
3. Framer lazy-imports 10–20 further `.mjs` chunks from inside its own
   `.mjs` (font loaders, icon modules). Grep the on-disk bundles for
   `[A-Za-z0-9_.-]+\.mjs`, diff against disk, fetch the gaps. Many candidates
   are minified tokens that 404 — that is fine and expected.
4. **Query-string image variants.** Framer requests
   `NAME.webp?scale-down-to=...` while `--restrict-file-names=windows` saved
   it as `NAME.webp@scale-down-to=...`. The hydrated `<img>` 404s on a file
   that is right there. Inject a script that strips the `@…`/`?…` suffix from
   every `framerusercontent.com/images/` src and removes its `srcset`, and
   copy the largest variant to the query-less base name.

Inter fonts under `framerusercontent.com/assets/*.woff2` are static string
literals in the font-loader chunk, so they localize cleanly with a prefix
swap. But `app.framerstatic.com/chunk-*.mjs` and `framerusercontent.com/
modules/*.js` icon components are built from base+hash **at runtime** — a
static scan finds zero and they cannot be rewritten. They stream from CDN
offline. Report that honestly; a service-worker shim is the only full fix and
is not worth baking speculatively.

Framer's entrance animation is flaky offline, leaving content stuck at
opacity 0. Inject:
`[data-framer-appear-id]{opacity:1!important;transform:none!important}`.

## Next.js

Signature: `/_next/`, `__NEXT_DATA__`.

**The big one: `<link rel="modulepreload">` is not followed by wget.** On a
real marketing site that is 40–180 JS chunks — nearly the whole bundle. The
page renders from SSR HTML and then fails to hydrate. `mirror.py repair`
handles this; do not skip it.

Images under `/_next/image?url=...&w=...` are query-string URLs saved with
`@` substitutions. Same fix pattern as Framer.

If media sits on `cdn.shopify.com`, see the Shopify section.

## Nuxt

Signature: `_nuxt` / `_nuxt4` directory, `__NUXT__` global. **Hardest stack.**

Everything in the Next.js section applies, plus:

1. **`robots.txt` is often `Disallow: /`** via nuxt-robots, so wget fetches
   nothing at all. Pass `-e robots=off` when the fingerprint reports a blanket
   disallow.
2. **CDN certificate failures.** Image hosts (notably `images.prismic.io`) can
   chain to a CA outside wget's bundle, silently failing every image. Use
   `--no-check-certificate` and span that host.
3. **Lazy route chunks.** Beyond the ~12 named in HTML, Nuxt loads ~10 more
   whose hashed names live inside JS strings. Also fetch the build manifest at
   `_nuxt/builds/meta/<buildhash>.json` — its 404 is a fatal
   "Cannot read properties of undefined (reading 'data')".
4. **`_payload.json?<hash>`** saved as `_payload.json@<hash>` while the app
   requests the `?query` form. Copy each to a plain `_payload.json` in its
   directory.
5. **Base-path trap.** The router base is `/`. Serving the mirror under
   `/site.com/` redirects to `/` and crashes. Serve the host folder as web
   root; repair's rewrite pass assumes this.

Do **not** try to "freeze" the SSR output by stripping `<script type=module>`.
Content sits at opacity 0 behind a JS preloader, so you get a blank page.
Restore hydration instead.

Worked example: chargebee.com (2026-08-04) — 49 of 50 chunks missing after
crawl, 180 recovered in repair, plus 158 more once CDN dirs moved in-root and
refs were rewritten. Final: 0 failed requests, 0 first-party remote.

## WordPress / WooCommerce

Signature: `wp-content`, `wp-includes`.

Respect robots.txt — it auto-skips add-to-cart traps. Then exclude the rest:

```
--reject-regex "(add-to-cart|orderby|replytocom|eventDisplay|eventDate|ical=|/feed|/embed|/comment-page-|/wp-json)"
--exclude-directories=/wp-admin,/cart,/checkout,/my-account
```

Usually large and slow. Run in background — the foreground 10-minute cap will
kill it mid-crawl.

Cart, checkout, forms, and client-fetched data will not function from a static
mirror. That is inherent, not a defect.

## Shopify headless

Media lives on `cdn.shopify.com`. Span to it so assets come local and get
link-converted.

AI-generated product filenames are frequently long enough to breach the
Windows 260-char path limit, which is what wget **exit 3** means. Re-fetch
that one file to a short name and patch its references.
