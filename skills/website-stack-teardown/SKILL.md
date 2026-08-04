---
name: website-stack-teardown
description: Use when asked what a website is built with / to reverse-engineer or analyze a site's tech stack, framework, libraries, hosting, or analytics from the outside. Passive black-box fingerprinting from response headers + raw HTML + script srcs + runtime globals. Covers CMS/site-builders (Webflow, WordPress, Shopify, Framer, Wix), JS frameworks (Next.js, React), hosts/CDNs (Vercel, Netlify, Cloudflare, Fastly), animation libs (GSAP, Three.js, Lenis, Lottie, Spline), and analytics/CRM tags (GTM, GA4, Meta Pixel, HubSpot, Segment, GoHighLevel).
---

# Website Stack Teardown

Reverse-engineer any public website's tech stack from the outside — no source access, no login. The whole method is: pull the **response headers** and the **raw HTML**, then match both against the fingerprint tables below. Headers reveal host/CDN/CMS; HTML `<script src>` + runtime globals reveal libraries; inline tag snippets reveal analytics/CRM.

## Scope (read first)

Passive fingerprinting only — you fetch the same bytes a normal browser would. **Do not** scan ports, brute-force admin paths, probe for vulns, hit non-public endpoints, or send anything but ordinary GETs. This is observation, not intrusion. Report findings with a confidence note; never imply you accessed anything private.

A fingerprint can be spoofed or stripped (Cloudflare proxies hide the origin; CMSes let users remove `generator` tags). Treat single signals as *likely*, corroborated signals (header + HTML + CDN domain) as *confirmed*. Flag anything you inferred from one weak signal.

---

## STEP 1 — Fetch headers + HTML, save for grep

Get headers and body in two passes. Follow redirects (`-L`) and send a real User-Agent (some hosts serve a challenge page to default agents).

**bash / curl:**
```bash
URL="https://example.com"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# 1) Response headers only (note: -I uses HEAD; some sites differ on GET — use -sIL plus a GET fallback)
curl -sIL -A "$UA" "$URL"

# 2) Raw HTML saved to disk for repeated grepping
curl -sL -A "$UA" "$URL" -o /tmp/page.html

# If HEAD is blocked or thin, capture GET headers + body together:
curl -sL -D /tmp/headers.txt -A "$UA" "$URL" -o /tmp/page.html
```

**PowerShell (Windows):**
```powershell
$URL = "https://example.com"
$UA  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$r = Invoke-WebRequest -Uri $URL -UserAgent $UA -MaximumRedirection 5
$r.Headers                      # response headers (hashtable)
$r.Content | Out-File C:\Temp\page.html -Encoding utf8   # raw HTML for grep
```

Then grep the saved HTML (use the Grep tool, or `rg`/`Select-String`). Key things to pull: every `<script src=...>`, every `<link href=...>`, the `<meta name="generator">`, any `__NEXT_DATA__` / `window.__` globals, and inline analytics snippets.

```bash
rg -o 'src="[^"]+"' /tmp/page.html        # all script/asset sources
rg -i 'generator|gtm-|"G-|fbq|hs-scripts|webflow|wp-content|_next' /tmp/page.html
```

> Headers answer **host/CDN/CMS**. HTML `src` domains answer **libraries**. Inline `<script>` snippets answer **analytics/CRM**. Do all three.

---

## STEP 2 — Header fingerprints (host / CDN / CMS / framework)

Match against the response headers from Step 1. Header names are case-insensitive.

| Platform | Header / value signals | Notes |
|---|---|---|
| **Webflow** | `server` mentions Webflow; `<meta name="generator" content="Webflow">` in HTML; assets from `cdn.prod.website-files.com` (older: `assets.website-files.com`) | `x-wf-*` and a `surrogate-key` of `pageId:<id> wf-page:<id>` appear at the **Fastly origin layer** and are normally **stripped before the client** — you'll usually confirm Webflow via the `generator` meta + the `website-files.com` CDN, not the surrogate key. |
| **Next.js** | `x-powered-by: Next.js`; assets under `/_next/static/...`; `<script id="__NEXT_DATA__" type="application/json">` in HTML; `<div id="__next">` | `x-powered-by` is often disabled; `/_next/` + `__NEXT_DATA__` are the reliable tells. App Router omits `__NEXT_DATA__` — look for `self.__next_f` chunks instead. |
| **Vercel** (host) | `x-vercel-id`, `x-vercel-cache: HIT/MISS`, `server: Vercel` | Hosting layer. Frequently sits in front of Next.js but also hosts other frameworks. |
| **Netlify** (host) | `x-nf-request-id`, `server: Netlify` | Hosting/CDN layer. |
| **Cloudflare** (CDN) | `cf-ray`, `server: cloudflare`, `cf-cache-status` | A **proxy in front** of the real origin — it masks the true host. Presence ≠ the site is "built on" Cloudflare; note it as the CDN/edge only (unless `cf-ray` + Workers signals like `cf-worker`). |
| **Fastly** (CDN) | `x-served-by: cache-*`, `x-cache: HIT/MISS`, `via: ... varnish`, `x-fastly-request-id` | CDN layer; underlies Webflow, Shopify, and many others. |
| **WordPress** | `link: <...>; rel="https://api.w.org/"` header; HTML has `/wp-content/`, `/wp-includes/`, `<meta name="generator" content="WordPress x.y">`; REST at `/wp-json/` | `/wp-content/` paths are the strongest tell. `x-powered-by: PHP` corroborates. Check `/wp-json/` only as a normal GET. |
| **Shopify** | `x-shopify-stage: production`, `x-shopid`, `x-sorting-hat-podid`, `x-shardid`; HTML loads `cdn.shopify.com` and `Shopify.theme` / `window.Shopify` | Any `x-shopify-*` header confirms Shopify outright. |
| **Framer** | Assets from `framerusercontent.com` / `events.framer.com`; `<meta name="generator" content="Framer ...">`; HTML comment `<!-- ✨ Built with Framer -->`; `<body class="framer-body">`; `data-framer-hydrate-v2`, `__framer-badge-container` | `framerusercontent.com` is the most reliable signal; corroborate with the generator meta or `data-framer-*` attributes. |
| **Wix** | `server: Pepyaka` (Wix's server); `x-wix-request-id`; HTML loads `static.parastorage.com` and references `wixBiSession` / `wix-warmup-data` | `parastorage.com` + `x-wix-request-id` together = Wix. |

Layering tip: a real stack is usually **CDN → host → framework → CMS**. Report each layer separately, e.g. "Cloudflare (edge) → Vercel (host) → Next.js (framework)". Don't collapse them.

---

## STEP 3 — Library detection (JS / animation / 3D)

Two evidence sources: **(a)** `<script src>` filenames/CDN paths in the saved HTML, and **(b)** runtime globals on `window` (only verifiable if you can run the page in a headless browser; otherwise rely on `src`). For passive HTML-only analysis, the `src` patterns below are primary.

| Library | HTML `src` / markup signal | Runtime global (if browser available) |
|---|---|---|
| **jQuery** | `jquery[-.]<ver>.min.js`, `code.jquery.com`, `cdnjs.../jquery/` | `window.jQuery`, `window.$`, `jQuery.fn.jquery` (version) |
| **GSAP** | `gsap.min.js`, `cdn.jsdelivr.net/npm/gsap`, `cdnjs.../gsap/`, plus plugin files `ScrollTrigger.min.js`, `SplitText.min.js` | `window.gsap`, `gsap.version`, `window.ScrollTrigger` |
| **Three.js** | `three.min.js`, `three.module.js`, `cdn.jsdelivr.net/npm/three`, `unpkg.com/three` | `window.THREE`, `THREE.REVISION` (version number) |
| **Lenis** (smooth scroll) | `lenis.min.js`, `@studio-freight/lenis`, `studio-freight` in path; markup gets `class="lenis lenis-smooth"` on `<html>` | `window.Lenis` |
| **React** | bundled (rarely a named CDN src); markup has `data-reactroot` (legacy) or hydration containers; DevTools hook | `window.__REACT_DEVTOOLS_GLOBAL_HOOK__`, `React.version` if exposed |
| **Webflow IX2** (interactions) | `js/webflow.<hash>.js` (or `webflow.js`); interaction elements carry `data-w-id="..."`; `<html data-wf-page>` / `data-wf-site` | `window.Webflow`, `Webflow.require('ix2')` |
| **Spline** (3D) | `@splinetool/runtime`, `prod.spline.design`, a `<spline-viewer>` custom element or `<canvas>` fed by Spline | `window.SPLINE` / spline-viewer element present |
| **Lottie** | `lottie.min.js`, `lottie-web`, `dotlottie`, `<lottie-player>` / `<dotlottie-player>` web component | `window.lottie` |
| **SplitType / SplitText** | `split-type` (`SplitType.min.js`) or GSAP's `SplitText.min.js`; in DOM, text wrapped in `<div class="line"><div class="word"><div class="char">` style spans | `window.SplitType` |
| **PixiJS** | `pixi.min.js`, `pixi.js`, `cdn.jsdelivr.net/npm/pixi.js` | `window.PIXI` |
| **PavelDoGreat WebGL fluid sim** | A fullscreen `<canvas>` with a WebGL context; the sim is often **inlined/renamed** (not a stable filename) — recognize it by its distinctive identifiers in the JS: functions/vars like `splatStack`, `multipleSplats`, `curl`, `vorticity`, `SPLAT_RADIUS`, `densityDissipation`, GLSL `curlShader`/`vorticityShader` | n/a (self-contained; no global) — match the shader/uniform names |

When a library is bundled (Webpack/Vite output like `index-a1b2c3.js`), `src` won't name it. Say so: "bundled, library names not exposed in filenames — would need runtime inspection to confirm." Don't guess a framework from a hashed bundle alone.

---

## STEP 4 — Analytics / CRM / pixels

Grep the raw HTML for these inline-snippet tokens. Each maps to a vendor and usually carries the account ID right next to it.

| Tool | Signal in HTML | ID format |
|---|---|---|
| **Google Tag Manager** | `googletagmanager.com/gtm.js`, `(window,document,'script','dataLayer','GTM-...)` | container `GTM-XXXXXXX` |
| **Google Analytics 4** | `googletagmanager.com/gtag/js?id=G-...`, `gtag('config','G-...')` | measurement `G-XXXXXXXXXX` (older Universal Analytics: `UA-...`) |
| **Meta (Facebook) Pixel** | `connect.facebook.net/en_US/fbevents.js`, `fbq('init','<id>')`, `fbq('track','PageView')` | numeric pixel ID in `fbq('init', ...)` |
| **HubSpot** | `js.hs-scripts.com/<hubid>.js` (loader) + `js.hs-analytics.net` (tracking); `_hsq` queue | numeric Hub ID in the script filename |
| **Segment** | `cdn.segment.com/analytics.js`, `analytics.load("<writeKey>")`, `analytics.track(` | write key string in `analytics.load(...)` |
| **GoHighLevel** | scripts/iframes from `msgsndr.com` / `*.msgsndr.com`; `msgsndr` in inline JS; form action to a GHL/`leadconnector` domain | account/location id in the msgsndr URL |

Also worth noting if seen: Hotjar (`static.hotjar.com`, `hjid`), Plausible (`plausible.io/js/script.js`), Mixpanel (`cdn.mxpnl.com`), Intercom (`widget.intercom.io`, `window.intercomSettings`).

---

## Worked example — a GSAP-heavy Webflow site (the xshack.app pattern)

Goal: a motion-rich marketing site. Run Step 1, then read the evidence:

**Headers:**
```
server: cloudflare              → Cloudflare edge (proxy; true origin hidden)
cf-ray: 8a...                   → confirms Cloudflare
x-served-by: cache-...          → Fastly underneath (Webflow's CDN)
```

**HTML `<meta>` + asset domains:**
```
<meta name="generator" content="Webflow">                  → CMS = Webflow (confirmed)
<html data-wf-page="..." data-wf-site="...">                → Webflow page/site attrs
assets from cdn.prod.website-files.com                      → Webflow CDN
```

**`<script src>` grep:**
```
.../js/jquery-3.x.min.js          → jQuery (Webflow always ships it)
.../js/webflow.<hash>.js          → Webflow IX2 interactions runtime
gsap.min.js + ScrollTrigger.min.js→ GSAP + ScrollTrigger (scroll animation)
SplitText.min.js (or split-type)  → text split into line/word/char for staggered reveals
three.min.js                      → Three.js (WebGL scene)
```

**Inline JS / canvas inspection:**
```
a fullscreen <canvas> + JS containing splatStack / curl / vorticity / densityDissipation
   → PavelDoGreat WebGL fluid simulation used as an animated background
```

**Verdict to report:**
> **Hosting/edge:** Cloudflare in front of Webflow's Fastly CDN.
> **CMS / builder:** Webflow (confirmed via `generator` meta + `data-wf-*` + `website-files.com`).
> **Baseline JS:** jQuery + Webflow IX2 (both shipped by Webflow by default).
> **Animation:** GSAP with ScrollTrigger; SplitText/SplitType for kinetic typography.
> **3D / background:** Three.js scene, plus a PavelDoGreat WebGL fluid-sim canvas for the animated hero background.
> **Confidence:** high — every claim is backed by a `src` path, a header, or distinctive shader identifiers, not a single weak signal.

This pattern (Webflow shell + jQuery/IX2 baseline + GSAP/ScrollTrigger + SplitType + Three.js + a fluid-sim canvas) is extremely common for award-style agency landing pages — recognizing the cluster lets you call the whole stack at a glance.

---

## Reporting format

Lead with the **layered stack** (edge → host → CMS → framework → libraries → analytics), then a one-line **confidence** note per layer, then flag anything uncertain. Example skeleton:

```
Edge/CDN:    <e.g. Cloudflare → Fastly>
Host:        <e.g. Vercel / Netlify / origin unknown behind proxy>
CMS/Builder: <e.g. Webflow>            [confirmed: generator meta + CDN]
Framework:   <e.g. Next.js App Router> [likely: /_next/ chunks, no __NEXT_DATA__]
Libraries:   <jQuery, GSAP+ScrollTrigger, Three.js, Lenis, SplitType, Lottie...>
Analytics:   <GTM GTM-XXXX, GA4 G-XXXX, Meta Pixel 1234, HubSpot 567>
Unsure:      <bundled chunks hide framework X; header Y could be spoofed>
```

Keep claims tied to evidence. "I can't access that" is never the answer here — you can fetch the public bytes; if a signal is ambiguous, say *what* you saw and *why* it's ambiguous.
