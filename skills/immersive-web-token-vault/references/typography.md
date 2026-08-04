# Typography — pairings extracted from award-winning sites

Source: `skillui` static analysis of shipped CSS, 2026-07-13. Font *names* are what the sites declare in their `font-family` stacks. Most are **commercial** — see licensing + free equivalents at the bottom.

## Extracted pairings (real)

| Site | Display / headings | Body / UI | Mono / labels | Move |
|---|---|---|---|---|
| Exo Ape | **Lausanne-300** | Times New Roman | — | Neo-grotesk heads over system serif body — quiet-luxury |
| Unseen Studio | **Saol Display** | Neue Montreal | — | Editorial serif + clean grotesk (the classic award pairing) |
| funkhaus | **Saol Display** | Matter | SFMono | Serif display + grotesk body + mono accent |
| Lusion | **Aeonik** | Aeonik | IBM Plex Mono | One grotesk, weights do the work + mono for tech labels |
| Serious Business | **Nib Pro** | PP Mori | — | Characterful serif + neutral grotesk |
| Studiogusto | **Matter** | Matter | — | Single-family, expressive weights |
| Scout Motors | **scout-sans-medium** | scout-sans-regular | scout-ibm-plex-mono | Custom brand grotesk + Plex Mono |
| Clear Street | **Reyhan** | Reyhan | — | Single serif system, unusual for fintech |
| Design Embraced | **exodus-sans** | exodus-sans | modern-era-mono | Grotesk + mono, greyscale editorial |
| Umault | **FFF Acid Grotesk** | Open Sans | — | Statement grotesk head + neutral body |
| Hatom | **OCMikola** | OCMikola | — | Single distinctive face, neon context |
| X-Shack | **Oswald** | Inter | — | Condensed display + neutral body |
| Igloo Inc | **Times New Roman** | Times New Roman | — | System serif only — the ironic-luxury move on an SOTY winner |
| Zajno | (unresolved sans) | — | — | Font hidden behind JS; couldn't resolve the real family |

## The four patterns that recur

1. **Editorial serif + neutral grotesk.** Saol Display × Neue Montreal (Unseen), Nib Pro × PP Mori (Serious Business). This is *the* award-site signature — a characterful display serif for oversized heroes, a quiet grotesk for everything else.
2. **One statement grotesk, weights only.** Aeonik (Lusion), Matter (Studiogusto). No pairing — a single strong face carrying the whole site through weight/size contrast. Simpler to license, harder to make interesting (the motion has to carry it).
3. **Mono as the technical accent.** IBM Plex Mono, SFMono, modern-era-mono appear as *labels, timestamps, coordinates, nav* — never body. A tiny amount of mono reads as "engineered."
4. **System serif on purpose.** Exo Ape and Igloo ship **Times New Roman** deliberately. When the WebGL/motion is the spectacle, a "boring" system serif becomes a confident, cost-free flex. Zero webfont load.

## Licensing + free equivalents

Most of the display faces above are paid. If you can't license them, these free faces get you the same *feel* — and they are premium-grade, not the banned defaults (no Cormorant / Outfit / JetBrains Mono / Noto Kufi as a lazy default). **Fontshare** (Indian Type Foundry) is the go-to: free for commercial use, foundry-quality.

| Commercial face (extracted) | Foundry | Closest free substitute |
|---|---|---|
| Lausanne | Weltkern | **Switzer** (Fontshare) or General Sans |
| Saol Display | Schick Toben | **Fraunces** (Google, variable) or Newsreader |
| Neue Montreal | Pangram Pangram | **Switzer** (Fontshare) |
| Aeonik | CoType | **General Sans** (Fontshare) or Space Grotesk |
| Matter | Displaay | **General Sans** (Fontshare) |
| PP Mori | Pangram Pangram | **General Sans** (Fontshare) |
| Nib Pro | — | **Fraunces** |
| Reyhan | — | **Newsreader** or Fraunces |
| FFF Acid Grotesk | Fff | **Space Grotesk** (display) |
| OCMikola | — | **Clash Display** (Fontshare) |
| Free already | — | Oswald, Inter, Open Sans, IBM Plex Mono (all Google/OFL); Times New Roman & SFMono are system |

## Applying this (checklist)

- Heading face carries the brand; pick ONE and commit. Serif for editorial/luxury, statement grotesk for modern/technical.
- Body face disappears — Switzer / General Sans / Neue-Montreal-class grotesk. Never let the body face compete with the display.
- Add mono only for functional micro-copy (labels, indices, timestamps). A little goes far.
- Two families max on screen (the extracted sites average ~2). Weights create hierarchy, not more fonts.
- For **Arabic/English** builds, pair the Latin face with a matched Arabic face and set direction per block — see `direct-kinetic-typography` for bilingual motion; never mix scripts mid-line.
- Self-host the woff2 and preload the display face to avoid FOUC (see `premium-preloader-intro`).
