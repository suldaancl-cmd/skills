# Marketplace publish — review list

Ownership audit of **1001 skill directories** in `skills/`. **Nothing is published.**
Approve or cut lines below, then I build the plugin tree and push.

## Why the other ~955 can't be published

| Signal | Count |
|---|---|
| Skill dirs scanned | 1001 |
| Declare `author: Karim` | 12 |
| Ship a third-party LICENSE file | 84 |
| Git submodules pointing at other people's repos | 9 |
| Vendored clones carrying their own `.git` | 12 |

Largest families with no signal at all are still clearly third-party:
`od-*` (75), `gstack-*` (44), `figma-*` (24), `expo-*` / `eas-*` (24), `bbg-*` (15),
`fal-*` (12), `firecrawl-*` (10), `gsap-*` (9), `layers-*` (9), `hyperframes-*` (8).

Declared authors found in frontmatter: **Alireza Rezvani (83)**, mahipal (14),
claudekit (10), refactoring-ui-expert (9), firecrawl (4).
Licence holders found: **Zara Zhang (33)**, GreenSock, hoainho, Next Level Builder,
VoltAgent, op7418, Matt Van Horn.

**Provenance caveat — read this.** The repo's first commit `00da091` imported
**8,813 files at once** ("scoped skill-library repo — 1471 skills"). Git history
therefore cannot distinguish *authored* from *vendored* for anything inside that
import. Tier C below rests on content evidence only, not proof.

---

## Tier A — explicit self-attribution (12)

*Evidence: `author: Karim` in SKILL.md frontmatter.* Safe to publish.

| Skill | What it is |
|---|---|
| `before-implementing` | Gate before writing any non-trivial code — new modules, schema changes, refactors |
| `expo-3d-ar` | 3D and AR inside Expo / RN — three.js and R3F on the expo-gl canvas |
| `expo-iap` | In-app purchases and subscriptions — RevenueCat, StoreKit 2, Google Play |
| `expo-splash-launch` | Animated splash and launch-to-first-screen continuity |
| `legal-asset-pipeline` | License-tracked asset pipeline for any site, app or landing build |
| `moti` | Declarative Framer-Motion-style animation for RN, built on Reanimated |
| `react-native-skia` | Hardware-accelerated 2D canvas — shaders, custom drawing |
| `reanimated` | Reanimated 3 and 4 — UI-thread animation, worklets, shared values, springs |
| `rn-component-motion` | Motion for components users touch — bottom sheets, swipeable rows, pull-to-refresh |
| `rn-icon-motion` | Animated icons across iOS, Android, RN — SF Symbols, Lottie |
| `rn-screen-transitions` | Screen and navigation transition choreography — expo-router / react-navigation |
| `supabase-stack` | Wire Supabase into an existing Vite/React project |

## Tier B — added in small authoring commits after the import (4)

*Evidence: own named commit, small file count — you wrote these in place.* Safe to publish.

| Skill | Commit evidence | What it is |
|---|---|---|
| `website-download` | `f7b36a2`, 7 files, "add website-download" | Download a whole site locally so it renders offline |
| `build-factory` | `064712b`, "rescue 7 skills that existed only on the vmi" | Delivery factory — turns ideas and offers into working assets |
| `project-context` | `8495829` | Scaffold and fill the nine project context files |
| `figma-first-app-pipeline` | `4238f8f` | Binding delivery contract for app UI and animated screen sequences |

## Tier C — your tooling, but unprovable from git (30)

*Evidence: references your own infra — vmi, vault paths, `skill-routes.json`,
AISTUDIOTODAY — but landed inside the 8,813-file import.* **These need your call.**

**Your system tooling** — almost certainly yours, they only make sense in your setup:
`skill-router-tune` · `system-maintain` · `session-intake` · `review-staged-drafts` ·
`skill-swarm` · `planmap` · `read-link` · `project-context` · `mobile-app`

**AISTUDIOTODAY / your business**:
`ai-studio-today-design` · `aistudiotoday-carousel` · `launch-promo-studio` ·
`app-growth-monetization` · `ai-receptionist-business`

**Design / motion / immersive**:
`immersive-web-token-vault` · `immersive-components` · `mine-award-site-patterns` ·
`awwwards-winner-playbook` · `design-audit` · `direct-immersive-color-light` ·
`direct-kinetic-typography` · `figma-depth-and-light` · `figma-immersive-premium` ·
`figma-motion-pipeline` · `figma-typography-systems` · `template-color-typography` ·
`web-motion-library-map` · `motion-sound-design` · `higgsfield-motion-design`

**Other**: `rtl-arabic-i18n` · `auth-implementation`

> Watch these two: `auth-implementation` and `higgsfield-motion-design` mention you
> but wrap third-party products. Confirm you wrote the SKILL.md itself, not just
> edited an imported one.

## Not proposed

Everything else — every skill whose SKILL.md you did not write, all 9 submodules,
all 12 vendored clones, all 84 carrying someone else's licence, and every
Anthropic-authored skill the Directory already lists under Anthropic's name
(`canvas-design`, `docx`, `pptx`, `pdf`, `mcp-builder`, `brand-guidelines`,
`theme-factory`, `web-artifacts-builder`, `slack-gif-creator`, `algorithmic-art`,
`learn`, `doc-coauthoring`, `internal-comms`, `skill-creator`, `xlsx`).

---

## What happens after you approve

1. Copy the approved skills into `plugins/<group>/skills/` under this folder
   (originals untouched — copy, never move).
2. Write `.claude-plugin/plugin.json` per group.
3. Commit the manifest to a public repo root.
4. Anyone installs with:
   `claude plugin marketplace add suldaancl-cmd/skills` then
   `claude plugin install <name>@karim-skills`

There is **no upload to the Anthropic Directory** — it has no submit API or CLI.
A marketplace is pulled from your repo, not pushed to a registry.
