# Design Audit — exact measures & skill map

Load this when you need the precise number behind a check, or want to cite the underlying
skill by name. Thresholds are sane defaults — a brief can justify deviating, but say so.

## Numeric thresholds

### Typography
- **Modular scale ratio:** 1.2 (minor third) to 1.333 (perfect fourth) is the common,
  safe range; larger ratios (1.5+) only for expressive/editorial.
- **Type steps:** keep the distinct sizes few (≈5–7 across the whole UI). More = no hierarchy.
- **Line length (measure):** 45–75 characters for body; ~66 is the classic target. Under ~35
  or over ~90 hurts reading. This is the `readable-measure` rule.
- **Line height:** body ~1.4–1.6; headings tighter (~1.05–1.25). Long measure → more leading.
- **Font families:** ≤2 (a display/heading + a text face). 3 needs a reason.
- **Weights:** a small intentional set (e.g. 400/500/700), not every weight the font ships.

### Color & contrast (WCAG 2.x AA)
- **Body text contrast:** ≥ 4.5:1 against its background.
- **Large text (≥24px, or ≥18.66px bold):** ≥ 3:1.
- **Non-text UI (icons, borders that carry meaning, focus rings):** ≥ 3:1.
- **Palette discipline:** neutrals carry the UI; 1 (maybe 2) accent(s) reserved for primary
  action and key emphasis. Many competing saturated colors = a smell.

### Spacing & layout
- **Spacing scale:** multiples of 4 (or 8). Values off the scale (e.g. 13px, 27px) are
  magic-number smells unless deliberate.
- **Alignment:** elements share edges/baselines; check for "almost aligned" (1–3px off).
- **Grid:** consistent column structure and gutters; content max-width set for readability.
- **Density:** related content close, unrelated content far (proximity); enough breathing room.

### Targets & interaction (Fitts / Doherty)
- **Touch targets:** ≥ 44×44px (Apple HIG) / 48dp (Material). Spacing between adjacent targets.
- **Primary action size & placement:** large, reachable, one per view.
- **System response:** feedback within ~400ms (Doherty); beyond that show progress/skeleton.

### Cognitive load (Hick / Miller)
- **Choices per step:** fewer is faster; collapse/defer secondary options.
- **Chunking:** group into ~5–7 items; paginate/segment long lists.

### States
- Every data-driven view needs **empty**, **loading**, **error**, and **success** states
  designed — not just the populated happy path.

## Severity guide
- **🔴 Blocker:** fails WCAG, breaks a flow, violates a hard house rule, or makes the primary
  goal unachievable. Caps Overall at 69/100.
- **🟠 High:** clearly hurts usability/conversion or credibility; fix this sprint.
- **🟡 Medium:** noticeable, worth fixing, not urgent.
- **⚪ Low:** polish / nice-to-have.

## Dimension → source-skill map
Use these names when you want to cite or go deeper.

| Dimension | Primary skills | Laws / standards |
|---|---|---|
| Visual hierarchy | `refactor-ui-01-establish-visual-hierarchy`, `visual-hierarchy` | von Restorff |
| Typography & measure | `typography-scale`, `critique-typography`, `readable-measure`, `refactor-ui-02` | — |
| Color & contrast | `refactor-ui-03-build-color-palette`, `refactor-ui-09-manage-color-contrast`, `color-system`, `color-expert` | WCAG 1.4.3 / 1.4.11 |
| Spacing & layout | `refactor-ui-04-apply-consistent-spacing`, `spacing-system`, `layout-grid` | Law of Common Region |
| Buttons & affordance | `refactor-ui-05-design-button-hierarchy` | Fitts's Law |
| Clutter & grouping | `refactor-ui-06-eliminate-visual-clutter`, `refactor-ui-10-group-related-elements` | Law of Proximity |
| Cognitive load / UX laws | `hicks-law`, `millers-law`, `doherty-threshold`, `aesthetic-usability` | — |
| States & feedback | `refactor-ui-07-design-empty-states`, `loading-states`, `error-handling-ux`, `feedback-patterns` | — |
| Consistency / system | `design-system-governance`, `design-token-audit`, `pattern-library`, `design-system-adoption` | — |
| Brand & composition | `critique-brand-consistency`, `critique-composition` | — |
| Accessibility | `a11y-audit`, `accessibility-audit` | WCAG 2.x AA |
| Shadows / depth (optional 11th) | `refactor-ui-08-use-shadows-appropriately` | — |
| Deep system lock (on request) | `ui-ux-pro-max` | WCAG / Apple HIG / Material (cited) |

## Capture-tool cheat-sheet
- **Live/URL:** `preview_start` → `preview_screenshot` (+ `preview_resize` for 390px/768px/1440px)
  → `preview_snapshot` (structure) → `preview_inspect` (computed CSS: px, color, contrast).
- **Image:** `Read` the file; state which measures are estimated vs measured.
- **Code:** `Read`/`Grep` components + token/Tailwind config; check hardcoded values vs tokens.
- **Figma:** `get_screenshot`, `get_metadata`, `get_variable_defs`, `get_design_context`.
