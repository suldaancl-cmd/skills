# Implementation plan — premium design system

Audit → propose → implement, safest high-impact first. Nothing destructive runs without explicit go-ahead.

**STATUS (2026-06-22): APPROVED & EXECUTED.** All 6 surgical fixes applied and validated (0 box-drawing/decorative chars remain in the fixed files; YAML frontmatter and code comments intact). The CLAUDE.md pointer block below was merged into the global config as design reach-order "step 0".

## Phase 0 — Land the law (additive, zero risk) ✅ done by this run
- [x] Write the canonical law to `premium-design-laws/audit/design-system-recommendations.md`.
- [x] Write curated token sets (`typography-options.json`, `color-gradient-options.json`).
- [x] Write `SKILL.md` so the law loads via the Skill tool on any design turn.

## Phase 1 — Wire it into the session ✅ done
- [x] Merged the pointer block into global `CLAUDE.md` "Design / frontend stack" section as reach-order "step 0", so the law loads every design turn (2026-06-22).

## Phase 2 — Surgical symbol fixes ✅ all 6 applied & validated (P0 first — skills Karim actually uses)
**P0**
- [ ] `C:\Users\user\.claude\skills\3d-animation-web-designer\SKILL.md` — Line 91: remove the `prefix with // ` instruction. Replace with: uppercase eyebrow micro-label `font-size:0.65rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent)` — no prefix glyph. Lines 170-173: replace the ┌─┐ box-drawing nav diagram with a prose description or an HTML/CSS snippet.
- [ ] `C:\Users\user\.claude\skills\brutalist-skill\SKILL.md` — Line 77: keep ASCII framing ONLY inside `<kbd>/<samp>/<code>` monospace contexts; for heading-level labels use an uppercase eyebrow or pill chip. Line 78: replace `>>> /// \\` directional decoration with a CSS counter or 1px border-right; reserve raw slashes for code/sample elements.

**P1**
- [ ] `C:\Users\user\.claude\skills\deck-swiss-international\SKILL.md` — Lines 49, 57: replace 'ASCII 呼吸点阵 / 点阵' with a CSS dot grid (`radial-gradient(circle, currentColor 1px, transparent 1px); background-size:8px 8px`) or inline SVG `<pattern>`. Align with the existing line-80 directive (pure CSS / inline SVG only).
- [ ] `C:\Users\user\.claude\skills\od-tpl-html-ppt-obsidian-claude-gradient\SKILL.md` — Line 3: change '三色渐变标题（#a855f7→#60a5fa→#34d399）' to a single-stop accent headline (#a855f7) or a two-stop same-family gradient (purple→indigo). Move any multi-stop gradient onto a thin pill/tag accent element, not the heading.

**P2**
- [ ] `C:\Users\user\.claude\skills\od-tpl-clinical-case-report\examples\example-stemi.html` — Reduce `/* ── Document Header ──────── */` to `/* Document Header */`. Keep the comment (it organizes the stylesheet); strip only the box-drawing/dash decoration. Do NOT touch the CSS itself.
- [ ] `C:\Users\user\.claude\skills\od-release-notes-one-pager\assets\template.html` — Reduce `/* ─── tokens ───────── */` to `/* tokens */` (or a blank line between CSS sections). Preserve the comment text and all token declarations beneath it untouched.

_Each fix is a targeted edit to decorative output only. Re-grep after each to confirm no `//`-comment / frontmatter / markdown rule was touched._

## Phase 3 — Validate ✅ symbol-grep passed (0 decorative chars; frontmatter/code intact); vmi mirror via Syncthing
- [ ] Re-run the decorative-symbol grep across the fixed files (expect 0 decorative hits, code comments untouched).
- [ ] Spot-render one P0 template to confirm it still works and looks cleaner.
- [ ] Mirror changes to vmi per the standing sync rule.

## Remaining risks
- A blind find-replace of `//` or `---` would break code examples and frontmatter — the law's Section A safety rule exists precisely to prevent that. All fixes stay manual/surgical.
- Token sets are curated (not 1000). If a future brief needs more range in one category, extend that category — do not pad.

---

## CLAUDE.md merge block (APPLIED 2026-06-22)

```markdown
## Premium design law (source of truth — added by symbol/typography audit)

Before any web/app/design build, load the `premium-design-laws` skill — it is the standing law for typography, color, gradients, and symbol hygiene. It EXTENDS (never replaces) the "Default fonts ban" and "Colors & Fonts deck FIRST" rules. Hard rules: no `//`-comment section labels, no `-----`/`=====` ASCII rules, no box-drawing or decorative slash/pipe/dot separators in rendered output (these are valid only as real code comments / YAML frontmatter / markdown). Use the curated token sets in `premium-design-laws/audit/`, not ad-hoc fonts/colors.
```
