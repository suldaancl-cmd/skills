# Multi-site premium motion upgrade verification

Use this when applying one reusable motion system (GSAP + ScrollTrigger + Lenis + CSS effects) across many static sites or many HTML files.

## Durable lessons

- Treat motion as a shared asset pair: one `premium-motion.css` + one `premium-motion.js` copied into each site/folder, then inject references into every HTML page.
- Add a small per-site config object such as `window.__PREMIUM_MOTION_SITE = { slug, profile, effect }` before loading the shared script. This lets one engine vary tone/effects without maintaining 18 separate scripts.
- Keep the site renderable if libraries fail: guard all GSAP/Lenis/ScrollTrigger usage and return early instead of throwing.
- Always include `prefers-reduced-motion` checks in both CSS and JS.

## CDN pitfall: Lenis package rename

The old CDN path can 404:

```html
https://unpkg.com/@studio-freight/lenis@1.0.42/bundled/lenis.min.js
```

Use the current package path instead:

```html
https://unpkg.com/lenis@1/dist/lenis.min.js
```

Verify external dependencies with HTTP checks before browser QA:

- `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js`
- `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js`
- `https://unpkg.com/lenis@1/dist/lenis.min.js`

## File-level verification checklist

For every site/folder:

- `premium-motion.css` exists
- `premium-motion.js` exists
- every HTML file contains the CSS ref
- every HTML file contains the JS ref
- every HTML file contains the site config block
- no old Lenis URL remains
- `node --check premium-motion.js` exits `0`

## Live/browser verification checklist

Raw HTTP `200` is not enough. Run a browser pass and check:

- page status is `200`
- CSS and JS refs are present in the DOM
- `window.gsap` exists
- `window.ScrollTrigger` or registered ScrollTrigger exists
- `window.Lenis` exists when Lenis CDN is used
- a script-owned sentinel exists, e.g. `window.__premiumMotionUpgradeLoaded === true`
- console errors array is empty
- screenshots are captured for visual spot checks

Playwright is a good default for this multi-site verification because it can navigate each live port, collect console errors, evaluate the runtime state, and save screenshots in one deterministic pass.

## Reporting format

When claiming completion, report evidence, not vibes:

- number of sites upgraded
- number of HTML files injected
- syntax check result
- CDN HTTP statuses
- live HTTP statuses
- browser console error count
- screenshot path/pattern

Example: `18/18 sites upgraded, 108 HTML files updated, node --check exit 0, CDN URLs 200, live ports 8120–8137 HTTP 200, Playwright console errors []`.
