---
name: arabic-font-licensing
description: Find Arabic typefaces and clear the licence before shipping them. Use whenever Arabic fonts must be sourced, downloaded, bought, bundled, self-hosted, embedded in an app or PDF, used in a logo delivered to a client, or rendered server-side by a product — and whenever someone asks "is this Arabic font free", "can I use this commercially", "where do I get a Thuluth/Diwani font", ترخيص خط, or wants to add an Arabic font to a website, app, video, or design tool. Fires before any Arabic font is downloaded or bundled, not after.
---

# Sourcing and licensing Arabic type

Arabic type has a worse piracy and licence-confusion problem than Latin type: the good display faces (Thuluth, Diwani, ornamental Kufi) are overwhelmingly commercial, and re-uploaded copies of them saturate free-font aggregators. "I found it on a free fonts site" is the most common way an Arabic project ends up shipping an unlicensed commercial face.

Clear the licence **before** downloading. Retrofitting a licence after a logo ships costs far more than picking a properly licensed face on day one.

## Four questions that determine which licence you need

1. **Where do the glyphs get drawn?** On the designer's machine (desktop), in the visitor's browser (webfont), inside an app binary (app/embedding), or **on your server** (server/SaaS)?
2. **Does the font file leave your control?** Handed to a client, bundled in a download, embedded in an editable PDF?
3. **Does the artwork become a trademark?** Logos and wordmarks are a separate right at most foundries.
4. **How much traffic?** Commercial webfont licences are usually capped by monthly pageviews and tied to one domain.

Most licence breaches come from question 1 and question 3 — a desktop licence used to render on a server, or a retail font outlined into a registered logo.

## Use case → what you need

| What you're doing | Licence bucket | Safe default |
|---|---|---|
| Comps, print, client artwork on your machine | Desktop | Any; OFL is free |
| Text on a public website | Webfont (self-host, pageview-capped, per-domain) | OFL |
| Font bundled in an iOS/Android/desktop app | App / embedding — usually a separate paid tier | OFL |
| Editable PDF / document handed off | Embedding rights | OFL |
| **Your server renders user text into images/PDFs** | **Server / SaaS — withheld by most retail licences** | **OFL only, unless you buy explicitly** |
| Logo or trademark | Extended / logo licence; often negotiated | OFL is fine; check foundry terms |
| Broadcast, film, out-of-home | Broadcast tier | OFL |

The bolded row is the one that catches product builders. A standard desktop or webfont licence covers *your* text on *your* pages — not a service that renders *other people's* text on demand. Any Arabic design generator, certificate maker, invitation builder, or thumbnail tool lives in that row.

## OFL — the safe default, and its two real constraints

Google Fonts' Arabic families are almost entirely SIL Open Font License 1.1 (a few older Noto files are Apache 2.0). Both permit commercial use, bundling, embedding, self-hosting, modification, and server-side rendering into a paid product. For a product that renders user text, **OFL is the answer** — it removes the hardest licence question entirely.

Two constraints that actually bite:

- **You cannot sell the font by itself.** You *can* sell software, a service, or artwork that includes it. Selling a "font pack" of OFL fonts as the product is the prohibited case.
- **Reserved Font Name.** If you modify the font — subsetting, renaming, hinting, adding glyphs — you must rename it. Shipping a modified "Cairo" as "Cairo" violates the RFN clause. Ship the `OFL.txt` alongside your distribution.

Apache 2.0 has no rename requirement; keep the notice.

## Where to source

**Trustworthy**

- **Google Fonts** — 40+ Arabic families, OFL, per-family licence file in the repo. Verified against the live API on 2026-08-02; run `arabic-typography/scripts/verify_families.py` to re-check any name before you cite it.
- **github.com/google/fonts** — the actual source files, metadata, and the licence file that governs each family.
- **SIL** (Scheherazade New, Lateef, Harmattan) — OFL, unusually deep Arabic-script coverage for scholarly and minority-language text.
- **Foundry direct** — the only correct place to buy commercial Arabic type.
- **Fontstand** — rent-to-own trials from real foundries when the budget is not there yet.
- **Adobe Fonts** — included with Creative Cloud, but check the terms per use; server rendering and app bundling are generally **not** included.

**Commercial Arabic foundries** — reach for these when the brief needs authentic Thuluth, Diwani, or a serious bilingual system:

| Foundry | Known for |
|---|---|
| 29LT (Pascal Zoghbi) | Bi-scriptual Arabic/Latin families; webfonts self-host only, pageview-capped, per-domain; app use requires the `-app` files |
| TPTQ Arabic (Kristyan Sarkis / Typotheque) | High-craft contemporary Arabic text and display |
| Boutros Fonts | Long-established Naskh and advertising faces |
| Arabetics, AlMohtaraf, Naghi | Specialist and calligraphic ranges |

Verify the current tier and price on the foundry's own site — published licence terms and pricing change, and the search snippets that describe them go stale.

**Avoid**

Free-font aggregators that mirror everything (onlinewebfonts, dafont-style sites, "download 1000 Arabic fonts" packs, Telegram/Drive collections). For Arabic these are heavily populated with re-uploads of commercial faces stripped of their licences. A file with no licence file is not free — it is unlicensed. "Free for personal use" is not a commercial licence.

## Before you ship — checklist

1. Open the licence file that shipped with the font. Not the download page, not the blog post, not a search result.
2. Confirm the bucket you actually need from the table above, especially server rendering and logo use.
3. If you modified anything, confirm the rename requirement and rename.
4. Keep the licence file in the repo next to the font files.
5. Record family, version, source URL, licence, and date in the project — the question always returns at handoff.
6. For commercial faces, keep the purchase receipt and the seat/pageview cap with the project.

## For an Arabic design-generator product

Build on OFL families and the hardest question disappears: you may render user text server-side, bundle the fonts, sell the output, and charge subscriptions. Ship each `OFL.txt`, rename anything you subset or modify, and never offer the raw font files as a downloadable asset — that is the one thing OFL forbids.

If a style genuinely needs a commercial face, licence it explicitly for **server-side rendering / SaaS** and expect it to be quoted separately from desktop and web. For authentic Thuluth, Diwani, and foliated Kufi, budget for a calligrapher or specialist face rather than assuming a free equivalent exists — see `arabic-typography` for which traditions have credible open-source options and which do not, and `arabic-ai-lettering` for why generating those letterforms with an image model is not a substitute.

This skill is not legal advice. For a trademark, a large commercial launch, or an enterprise contract, have the licence reviewed.
