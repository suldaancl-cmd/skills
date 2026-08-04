---
name: design-audit
description: >-
  Run a single, complete design audit that pushes a design through the full battery of
  design-rule, UX-law, and critique skills in one pass and returns ONE scored report. Use
  this whenever the user wants to review, critique, grade, QA, score, or "check" a design,
  UI, screen, landing page, component, flow, or design system — from any source: a live web
  URL or local dev server, a screenshot/image, React/HTML/CSS code in a repo, or a Figma
  file. Trigger on phrases like "design audit", "run the design rules on this", "review this
  UI", "critique this page", "is this design good", "grade this screen", "design QA", "check
  my landing page", "run all the design skills on X", or "what's wrong with this design" —
  even when the user names no specific rule or skill. This is the meta-runner: prefer it over
  invoking individual critique-* / refactor-ui-* / *-law skills one at a time.
---

# Design Audit — the one-pass runner

## Why this exists
The design rules in this library are scattered across many skills: the **measures**
(`refactor-ui-*`, `typography-scale`, `spacing-system`, `layout-grid`, `readable-measure`,
`color-system`, `visual-hierarchy`), the **laws** (`fitts-law`, `hicks-law`, `millers-law`,
`doherty-threshold`, `law-of-proximity`, `law-of-common-region`, `von-restorff-effect`,
`aesthetic-usability`), the **critiques** (`critique-typography`, `critique-visual-hierarchy`,
`critique-composition`, `critique-brand-consistency`), the **checklists**
(`design-qa-checklist`, `heuristic-evaluation`), and the **accessibility** pass
(`a11y-audit`). Running them one by one is slow and the outputs don't add up to a verdict.

This skill runs the whole battery in one go and merges it into a single graded report, so the
rules actually get *applied* instead of just existing. The substance of every sub-skill is
captured below as a scored dimension — you do **not** have to invoke each one. Reach for an
individual sub-skill (or `ui-ux-pro-max` for cited WCAG/HIG/Material detail) only when a
dimension needs a deeper look. The deliverable is always: coverage + one report.

For exact numeric thresholds and the full skill→dimension map, read
`references/measures.md` when you need the precise number behind a check.

## Step 0 — Identify the source and capture real evidence
An audit is only as good as its evidence. Never grade from memory or imagination — capture
something inspectable first, then measure against it. Pick the row that matches the source.

| Source | How to capture evidence | What you can measure |
|---|---|---|
| **Live URL / dev server** | `preview_start` then `preview_screenshot` (desktop + mobile via `preview_resize`), `preview_snapshot` for structure, `preview_inspect` for **computed CSS** (px, colors, font sizes, contrast). Chrome MCP is the fallback. | Everything — real pixels, real contrast ratios, real type scale, real spacing. Strongest audit. |
| **Screenshot / image** | `Read` the image directly. If multiple breakpoints exist, ask for or read each. | Visual hierarchy, composition, type *relationships*, color harmony, clutter, brand. Estimate spacing/contrast and **say it's estimated** — you can't read exact px from a raster. |
| **React / HTML / CSS in repo** | `Read`/`Grep` the components, the CSS/Tailwind config, the design tokens. If a dev server is available, also do the Live-URL capture above. | Token discipline, spacing-scale adherence, hardcoded magic numbers, font usage, repeated-pattern drift, state coverage (empty/loading/error). |
| **Figma file** | Figma MCP: `get_screenshot`, `get_metadata` (structure), `get_variable_defs` (tokens), `get_design_context`. | Token/variable discipline, component structure, spacing, type styles, contrast from defined colors. |

If the user gives no source, ask which one — do not invent a design to grade.

## Step 1 — Score the dimensions
Score each dimension **1–5** (see scale at the bottom). For every dimension, capture the
*measure* (the number/observation), then the *issues* it surfaces. Cite the rule each issue
comes from — that's what turns "I feel like" into "fails X."

1. **Visual hierarchy** — `refactor-ui-01`, `visual-hierarchy`, `von-restorff-effect`.
   Does the eye land on the most important thing first? Is there one clear primary action per
   view? Emphasis built with size/weight/color/spacing, not just bold-everything.

2. **Typography & measure** — `typography-scale`, `critique-typography`, `readable-measure`.
   Consistent modular scale (e.g. 1.2–1.333 ratio), limited steps, body line-height ~1.4–1.6,
   line length **45–75 characters**, ≤2 type families, restrained weight set.

3. **Color & contrast** — `refactor-ui-03`, `refactor-ui-09`, `color-system`.
   Disciplined palette (neutrals + 1 accent done well beats a rainbow), accent reserved for
   action, body text **≥4.5:1** contrast, large text/UI **≥3:1** (WCAG AA).

4. **Spacing & layout** — `refactor-ui-04`, `spacing-system`, `layout-grid`,
   `law-of-common-region`. Spacing from a fixed scale (4/8pt), consistent rhythm, real
   alignment to a grid, generous-enough white space, sane density.

5. **Buttons & affordance** — `refactor-ui-05`, `fitts-law`. Clear primary/secondary/tertiary
   tiers, only one primary competing per view, touch/click targets **≥44×44px**, important
   targets bigger/closer.

6. **Clutter & grouping** — `refactor-ui-06`, `refactor-ui-10`, `law-of-proximity`.
   Related things grouped by proximity, not boxed in borders unnecessarily; high
   signal-to-noise; nothing fighting for attention that shouldn't.

7. **Cognitive load & UX laws** — `hicks-law`, `millers-law`, `doherty-threshold`,
   `aesthetic-usability`. Few enough choices per step, options chunked (~5–7), system feedback
   under ~400ms (or a perceived-performance treatment), overall "feels effortless."

8. **States & feedback** — `refactor-ui-07`, `loading-states`, `error-handling-ux`,
   `feedback-patterns`. Empty, loading, error, and success states designed — not just the
   happy path. (For code/Figma sources this is often where the real gaps hide.)

9. **Consistency & system adherence** — `design-system-governance`, `design-token-audit`,
   `pattern-library`. Same component looks/behaves the same everywhere; tokens used instead of
   hardcoded values; no near-duplicate one-off variants.

10. **Brand & composition** — `critique-brand-consistency`, `critique-composition`.
    On-brand voice/color/type; balanced, intentional composition; imagery quality (no obvious
    stock-photo filler on a premium build).

## Step 2 — Accessibility pass (the most measurable rules)
Run `a11y-audit`'s essentials regardless of source: text contrast ratios, visible focus
states, target sizes, semantic structure / heading order, alt text, keyboard operability,
and motion-reduction respect. Accessibility findings are usually **blockers**, not nits —
they're pass/fail against WCAG, not taste.

## Step 3 — House rules (Karim-specific)
These are non-negotiable checks for Karim's builds. Flag any hit as a **blocker** or **high**.
- **Banned default-font autopicks**: Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic used
  *as the default/lazy pick*. Flag and propose a brief-appropriate alternative. (See
  `feedback_default_fonts_ban`.)
- **Banned decoration**: dev-comment-label motifs like `// 01 — THE MISSION` used as visual
  decoration.
- **RTL / Arabic correctness** (if any Arabic): direction, mirroring, numerals, font that
  actually supports Arabic, no mid-sentence EN/AR mixing in body. (See `rtl-arabic-i18n`.)
- **Premium-web standard** (for serious builds): motion is purposeful and restrained (GSAP
  ScrollTrigger + Lenis-class smoothness, not gratuitous), real content over lorem, fast load.
  Don't *require* animation — flag both "none where it'd elevate" and "too much / janky."

## Scoring
- **Per dimension:** 5 = exemplary · 4 = solid, minor nits · 3 = works but clearly improvable
  · 2 = real problems · 1 = broken/absent.
- **Overall = (sum of 10 dimensions) × 2**, giving a `/100` score. Then apply a cap: **any
  unresolved accessibility or house-rule blocker caps Overall at 69/100** — a design that
  fails WCAG or a hard house rule cannot be called "good" no matter how pretty.
- Pair the number with a one-line verdict. The number orients; the **ranked fixes** are the
  real value.

## Report structure
ALWAYS output exactly this template:

```
# Design Audit — <target name>
**Source:** <url / file path / image / figma node>  ·  **Evidence:** <what you captured>
**Viewports:** <e.g. 1440px + 390px, or "single image">
**Overall: <N>/100 — <one-line verdict>**   <note any blocker cap applied>

## Scorecard
| # | Dimension | Score | One-line verdict |
|---|-----------|-------|------------------|
| 1 | Visual hierarchy        | x/5 | ... |
| 2 | Typography & measure    | x/5 | ... |
| 3 | Color & contrast        | x/5 | ... |
| 4 | Spacing & layout        | x/5 | ... |
| 5 | Buttons & affordance    | x/5 | ... |
| 6 | Clutter & grouping      | x/5 | ... |
| 7 | Cognitive load / UX laws| x/5 | ... |
| 8 | States & feedback       | x/5 | ... |
| 9 | Consistency / system    | x/5 | ... |
| 10| Brand & composition     | x/5 | ... |
| A | Accessibility           | pass / warn / fail | ... |
| H | House rules             | pass / fail | ... |

## 🔴 Blockers (fix before ship)
1. **<issue>** — *<rule cited, e.g. WCAG 1.4.3 / Hick's Law / refactor-ui-04>* — <the fix>

## 🟠 High  /  🟡 Medium  /  ⚪ Low
- **[dimension]** <issue> — *<rule>* — <fix>

## ✅ What's working
- <keep-doing items — say what's already strong, briefly>

## Top 5 fixes, in priority order
1. <highest-leverage change first>
...
```

Keep each issue specific and tied to evidence ("body copy runs 110ch at 1440px — over the
45–75ch readable range" beats "typography could be better"). Severity = how much it hurts the
user or the goal, not how easy it is to fix.

## When to go deeper
If the user wants more than the one-pass report on a given dimension, *then* invoke the
specific source skill — e.g. `ui-ux-pro-max` to lock a corrected design system with citations,
`critique-typography` for a full type teardown, or `a11y-audit` for an exhaustive WCAG sweep.
The audit names the problem; those skills go deep on the fix.
