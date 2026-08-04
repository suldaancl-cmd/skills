# Symbol cleanup report

# Symbol-Cleanup Plan — Skill Library Design Output

## What this is
Karim rejects "developer-looking" decoration in **rendered design output** — the visible HTML/CSS a client sees. The tells: `// SECTION` comment-style labels used as on-page eyebrows, `-----` / `=====` ASCII rules, box-drawing frames (`┌─┐ │ └─┘`), bracket-framed labels (`[ DELIVERY SYSTEMS ]`, `< RE-IND >`), directional slash runs (`>>>`, `///`, `\\\`), and ASCII dot-matrix decoration. These read as unrendered code, not premium typography. They are the same family as the already-banned `// 01 — THE MISSION` dev-comment-label pattern (see `feedback_default_fonts_ban.md`).

## What was found (10 hits across 5 skill families)
- **`3d-animation-web-designer`** (P0 — Karim's active cinematic-web skill): two offenders. Line 91 instructs prefixing section labels with `// `; lines 170-173 use a box-drawing ASCII nav diagram.
- **`brutalist-skill`** (taste pack): lines 77-78 codify bracket-framed labels and `>>> /// \\\` directional slashes as the house "syntax decoration" style.
- **`deck-swiss-international`**: lines 49/57/80 instruct ASCII "呼吸点阵 / 点阵 / 矩阵" (breathing dot-matrix) decoration in rendered slides.
- **`od-tpl-html-ppt-obsidian-claude-gradient`**: line 3 specs a three-stop rainbow gradient heading (`#a855f7→#60a5fa→#34d399`) — purple→blue→teal reads as cheap neon, not the GitHub-dark premium it claims. (Adjacent symbol-aesthetic offense, same "looks like a dev tool but cheaply" failure.)
- **`od-tpl-clinical-case-report`** and **`od-release-notes-one-pager`**: CSS comment dividers with trailing `─────` runs inside `<style>` blocks. **Borderline** — see safety rule below.

## CRITICAL SAFETY RULE — do NOT blind-replace
This cleanup targets **decorative output only**. The following are NOT offenders and a find-and-replace that touches them will break working code:

1. **`//` in JavaScript / TypeScript / JSX** is a real line comment. `// eslint-disable`, `// TODO`, `// @ts-ignore`, URL schemes (`https://`), and JSX prop math are all legitimate. Never strip `//` outside of a string/text node destined for the rendered DOM.
2. **`---` as YAML frontmatter delimiters** (the opening/closing `---` of every `SKILL.md`) and **`---` / `***` as Markdown horizontal rules** are structural. Stripping them corrupts the skill loader and the docs.
3. **`/* ... */` CSS comments that organize a token block** (e.g. `/* tokens */`, `/* Document Header */`) are acceptable code organization — they live in `<style>`, not in visible content. Only the **trailing decorative dash-run** (`/* tokens ─────────── */`) is noise. Reduce to `/* tokens */`; do not delete the comment.
4. **`<kbd>`, `<samp>`, `<code>` content** legitimately contains brackets and slashes in a monospace face. A literal `[Esc]` inside `<kbd>` is correct; a `[ SECTION ]` eyebrow in a heading is not.

The distinction is **rendered visible content vs. source mechanics**. Fix the former by hand, per file. Never run a repo-wide blind regex.

## Replacement philosophy
Premium labelling earns hierarchy from **typography and space**, not ASCII characters. The five canonical replacements:
- **Whitespace rhythm** — let margin/padding separate sections instead of a `-----` rule.
- **Hairline border token** — a single `1px solid var(--hairline)` (or `border-left: 2px solid var(--accent)`) replaces every ASCII rule, bracket frame, and box-drawing line.
- **Uppercase eyebrow micro-label** — `font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent)` replaces `// SECTION` and `[ SECTION ]`. The styling signals the role; no prefix glyph needed.
- **Kicker** — a short lead-in phrase above a heading for editorial labelling where an eyebrow is too terse.
- **Numbered chip** — `01 / 02 / 03` set in the body face (or a small `<Badge>`) replaces `>>>` and decorative-slash directional cues.

Apply surgically: edit the specific line, match surrounding style, change nothing adjacent.

## Scale of the problem

- **Decorative-output offenders found:** 9 (across 16 corpus slices).
- **Code comments / YAML frontmatter / markdown rules correctly LEFT ALONE:** 477+ occurrences.
- Verdict: the decorative-symbol problem is **small and surgical**, not systemic. The earlier ban largely held. The fix is a handful of targeted edits plus a standing law (Section A of design-system-recommendations.md).

## Decorative-output offenders (raw findings)

| Slice | File | Kind | Snippet | Premium replacement |
|---|---|---|---|---|
| output-templates | `od-tpl-html-ppt-obsidian-claude-gradient/SKILL.md:3` | other | 三色渐变标题（#a855f7→#60a5fa→#34d399） | Use a single-stop accent color on the headline (e.g. #a855f7 alone) or a two-stop same-family gradient (purple→indigo). Three-stop rainbow gradients on headings |
| zhangzara-ppt-decks | `deck-swiss-international/SKILL.md:49,57,80` | box_drawing | ASCII 呼吸点阵 … ASCII 点阵 … ASCII 矩阵 | Replace ASCII dot-matrix decoration instructions with CSS grid dots (`background-image: radial-gradient(circle, currentColor 1px, transparent 1px); background-s |
| karim-web-build-skills | `3d-animation-web-designer/SKILL.md:91` | comment_label | Section labels: `0.65-0.75rem`, uppercase, `letter-spacing: 3px`, accent color,  | Use an uppercase <eyebrow> micro-label element (e.g. <span class="label">Services</span>) with a CSS border-left: 2px solid var(--accent) hairline, or a numbere |
| taste-packs | `brutalist-skill/SKILL.md:77` | box_drawing | [ DELIVERY SYSTEMS ], < RE-IND > | Uppercase eyebrow micro-label in <span class="eyebrow"> or a small pill chip (e.g. <Badge>DELIVERY SYSTEMS</Badge>) — no bracket framing. Reserve literal ASCII  |
| taste-packs | `brutalist-skill/SKILL.md:78` | decorative_slash | >>>, ///, \\ | Single 1px solid border-right or a CSS counter (content: counter(section)) for directional hierarchy. If motion is intended, use a CSS transform translateX arro |
| existing-rules-and-feedback | `3d-animation-web-designer/SKILL.md:91` | decorative_slash | Section labels: `0.65-0.75rem`, uppercase, `letter-spacing: 3px`, accent color,  | Remove the `// ` prefix instruction entirely. Replace with: uppercase eyebrow micro-label using `font-size: 0.65rem; letter-spacing: 0.2em; color: var(--accent) |
| existing-rules-and-feedback | `3d-animation-web-designer/SKILL.md:170-173` | box_drawing | ┌────────────────────────────────────────────────┐
│ ≡ MENU    │    BRAND NAME   | Replace box-drawing ASCII nav diagram with a prose description or an actual HTML/CSS snippet. If a visual diagram is needed in the skill doc, use a fenced code  |
| existing-rules-and-feedback | `od-tpl-clinical-case-report/examples/example-stemi.html:21-178` | ascii_divider | /* ── Document Header ───────────────────────────────────────────── */ | These are CSS comment dividers inside a <style> block — borderline acceptable as code organization. However the trailing ─── run after the section name is pure  |
| existing-rules-and-feedback | `od-release-notes-one-pager/assets/template.html:21-196` | ascii_divider | /* ─── tokens ───────────────────────────────────────────────────────── | Same pattern — CSS comment aesthetic decoration with ─── runs. Simplify to `/* tokens */` or use a blank line between CSS sections. The decorative dash-runs add |

## Ranked files to surgically fix

| Priority | File | Why | Fix |
|---|---|---|---|
| **P0** | `C:\Users\user\.claude\skills\3d-animation-web-designer\SKILL.md` | P0 — one of Karim's actively-invoked cinematic-web skills (in the design killer-combo routing table). Line 91 literally instructs prefixing section labels with `// `, the exact dev-comment-label pattern already banned in feedback_default_fonts_ban.md. This skill seeds real client output. | Line 91: remove the `prefix with // ` instruction. Replace with: uppercase eyebrow micro-label `font-size:0.65rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent)` — no prefix glyph. Lines 170-173: replace the ┌─┐ box-drawing nav diagram with a prose description or an HTML/CSS snippet. |
| **P0** | `C:\Users\user\.claude\skills\brutalist-skill\SKILL.md` | P0 — installed taste pack reachable for any brutalist brief; lines 77-78 codify `[ ... ]` bracket framing and `>>> /// \\` slash runs as the house style, so it actively teaches the banned aesthetic. Brutalist legitimately uses some industrial glyphs, so this needs a careful edit, not deletion. | Line 77: keep ASCII framing ONLY inside `<kbd>/<samp>/<code>` monospace contexts; for heading-level labels use an uppercase eyebrow or pill chip. Line 78: replace `>>> /// \\` directional decoration with a CSS counter or 1px border-right; reserve raw slashes for code/sample elements. |
| **P1** | `C:\Users\user\.claude\skills\deck-swiss-international\SKILL.md` | P1 — a deck template Karim may reach for in slide work; lines 49/57/80 instruct ASCII dot-matrix decoration (点阵/矩阵) in rendered slides. Line 80 already says use CSS/inline SVG for geometry, so the ASCII instruction contradicts the file's own rule. | Lines 49, 57: replace 'ASCII 呼吸点阵 / 点阵' with a CSS dot grid (`radial-gradient(circle, currentColor 1px, transparent 1px); background-size:8px 8px`) or inline SVG `<pattern>`. Align with the existing line-80 directive (pure CSS / inline SVG only). |
| **P1** | `C:\Users\user\.claude\skills\od-tpl-html-ppt-obsidian-claude-gradient\SKILL.md` | P1 — high-traffic od-tpl deck family; line 3 specs a three-stop rainbow heading gradient (#a855f7→#60a5fa→#34d399) that reads as cheap neon, undermining the premium GitHub-dark look it claims. Same 'looks dev but cheap' failure as the symbol decoration. | Line 3: change '三色渐变标题（#a855f7→#60a5fa→#34d399）' to a single-stop accent headline (#a855f7) or a two-stop same-family gradient (purple→indigo). Move any multi-stop gradient onto a thin pill/tag accent element, not the heading. |
| **P2** | `C:\Users\user\.claude\skills\od-tpl-clinical-case-report\examples\example-stemi.html` | P2 — borderline: these are CSS comment dividers inside a <style> block (acceptable code organization), but the trailing ─────── runs after section names are pure decoration that reinforces the AI-slop pattern in an example file. | Reduce `/* ── Document Header ──────── */` to `/* Document Header */`. Keep the comment (it organizes the stylesheet); strip only the box-drawing/dash decoration. Do NOT touch the CSS itself. |
| **P2** | `C:\Users\user\.claude\skills\od-release-notes-one-pager\assets\template.html` | P2 — same borderline CSS-comment-divider pattern (line 21: `/* ─── tokens ───── */`). Organizational comment is fine; the ─── decoration runs are noise. Example/asset file, lower blast radius than the SKILL docs above. | Reduce `/* ─── tokens ───────── */` to `/* tokens */` (or a blank line between CSS sections). Preserve the comment text and all token declarations beneath it untouched. |

_P0 = a skill Karim actively invokes for web builds._
