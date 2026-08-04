# Framer Marketplace submission and pricing

## How review actually works

Framer publishes templates **instantly with no manual review**, but enforces published quality/originality standards after the fact. That changes the workflow: you can ship fast, but you must self-audit against framer.com/template-requirements before and after every edit, because that same checklist is also what earns "featured" placement — there is no reviewer to catch omissions for you.

## Self-audit checklist (from framer.com/template-requirements)

- Shared Text Styles and Color Styles are used throughout — no one-off font/color overrides on individual layers (see `component-architecture.md`).
- A custom 404 page exists (not the Framer default).
- No lorem ipsum or placeholder copy anywhere in the shipped file.
- CMS collections and fields use clear, human-readable naming; empty/placeholder CMS entries are removed before submission.
- Real `mailto:` and `tel:` links on contact info, not dead `#` links or plain text.
- Images have alt text set.

Treat this as a pre-submission gate, and re-run it after every editing pass — it is easy to reintroduce a broken link or an empty CMS row while polishing motion.

## Revenue model and pricing bands

- Framer creators keep **100% of paid-template revenue**.
- Free templates earn roughly **50% affiliate commission** on the Framer signups they drive.
- The top of the live leaderboard (selected.site) is almost all free templates — a free flagship (for reach/rank) + a paid niche catalog (for revenue) is the proven portfolio shape, not "everything paid."

Observed pricing bands across bestseller lists:

| Band | Positioning |
|---|---|
| Free | Rank-farming / affiliate commission play |
| $39-$49 | Personal / portfolio templates |
| $79-$99 | Niche pro (fintech, architecture, wellness) |
| $129-$149 | Flagship agency/SaaS template with one signature animation |

Jet ($149, the priciest in Velox's top-25) justifies the top band specifically by shipping a "customizable hero animation" — a code component with property controls buyers can tune without touching code (see `component-architecture.md`). Vectura ($99) and Saalix (#2 weekly on selected.site) sit in the niche-pro band on the strength of one over-designed section (pricing page) rather than a signature hero.

## Listing craft (half the sale)

- Use an animated preview capture over a static thumbnail.
- Write a descriptive byline and pick accurate categories — buyers filter by category before they ever open a preview.
- The grid thumbnail is one image: pick the most distinctive hero screenshot, since a distinctive hero is what wins the click in a marketplace grid (this is exactly why "one signature hero effect" patterns exist — see `patterns.md`).
- Track selected.site as free, live competitive intelligence: it's a daily leaderboard of marketplace rankings with weekly/monthly winners, useful for spotting category and pricing gaps before building.

## What separates a bestseller from a rejected/ignored template, per the research

- **Bestsellers** (Nakula, Xtract, Vectura, Mugen, Jet) each lead with one clearly named, easy-to-screenshot feature: a preloader, native appear animations, a pricing page, advanced CMS, a customizable hero. Buyers are shown to shop by naming ONE reason, not a feature list.
- **CMS discipline is graded, not optional** — clear field naming and no empty entries are on Framer's own published checklist, meaning a template can look polished and still under-deliver on this specific, checkable criterion.
- **Ecommerce is a gap, not a native feature.** Framer has no native store; DTC templates integrate Shopify via Frameship and sell the integration itself as the headline feature (Essentia). If building for that niche, budget for the integration, not just the design.
- **Code-component-dependent effects are Framer's real differentiator vs. Webflow.** Anything that needs custom code (Unicorn Studio WebGL, Rive, magnetic buttons, drag physics, horizontal-scroll-from-vertical-scroll) is legal and expected in a Framer template, and is exactly the class of effect Webflow's marketplace bans outright from templates. Lean into this rather than under-using it out of habit from Webflow-style caution.

## Related skills in this library

- `template-marketplace-strategy` — deeper business-layer guidance on niche selection, pricing strategy, and marketplace choice (Webflow vs. Framer vs. others).
- `template-color-typography` — palette archetypes and font-pairing choices for the style-guide page these templates need.
- `webflow-template-builder` — the Webflow-side equivalent of this skill, useful for porting a pattern between builders or understanding what's legal on each marketplace.
