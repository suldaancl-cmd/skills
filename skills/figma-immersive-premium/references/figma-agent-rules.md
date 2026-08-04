# Karim — Figma Agent Skill (paste into Figma)

This is a **portable rules file** for Figma's canvas agent (Config 2026 "Skills" feature) and for Dev Mode's `create_design_system_rules`. It forces Figma's own agents to follow the same premium-design laws Claude follows, so work stays on-brand whether it's authored in Figma or in code.

**How to install it in Figma (one-time):**
1. Figma → the canvas agent panel → **Skills** → add a new Skill → paste everything below the line.
2. In Dev Mode, also run the MCP tool `create_design_system_rules` to generate the repo-specific rules file, and merge these laws into it.
3. Re-paste whenever these laws change (they mirror `premium-design-laws`).

Claude reads this same file via the `figma-immersive-premium` router, so both sides share one source of truth.

---

## Design laws (Karim, premium bar)

You are designing at a **$20K–$50K agency bar. Cinematic, never flat cards.** Tidy card-on-dark-panel grids are rejected on sight.

**Process — deck first.**
- Before building any UI, propose **3–4 distinct colour + font directions** and wait for a pick. No screens, no components, no code until one is chosen.
- Lock the chosen direction as Figma **variables** (tokens) and build everything from them.

**Typography.**
- **Banned default fonts:** Cormorant, Outfit, JetBrains Mono, Noto Kufi — never reach for these as a default.
- Use a real modular scale as number variables. Explicit line-height and letter-spacing. Negative tracking on display sizes. Strict display / body / meta separation — never one uniform weight.
- Arabic is first-class: Arabic-safe pairings, proper RTL, correct numerals. Never mix LTR and RTL in one text block.

**Colour & gradient.**
- One disciplined accent system. Semantic variables (`bg / surface / border / text / accent / cta / state`) in **light + dark modes**.
- Gradients must be **earned** — same-family stops or a real reference image. Never a rainbow or lazy 3-stop gradient on a heading.
- CTA contrast meets WCAG.

**Depth & surface (the flat-card cure).**
- Layered elevation, tinted (not pure-black) shadows, lit edges, glass where it belongs. Give every surface a reason to have depth.
- Use shader **fills** for rich hero/section backgrounds (aurora/mesh/noise in accent stops), and shader **effects** (grain, subtle aberration, glow) as a finishing pass — one signature fill + at most one or two effects per surface. If you can't name why an effect is there, remove it.

**Motion.**
- Ease everything (no linear). Motivate every move — entrance, focus, or feedback — never motion for motion's sake.
- Stagger reveals via timeline cohorts. Respect reduced-motion.

**Symbol hygiene (on-canvas text).**
- No `//`-style section labels, no `-----` / `=====` ASCII rules, no box-drawing, no decorative slash / pipe / dot separators.
- Use whitespace rhythm, a 1px hairline border variable, or an uppercase eyebrow micro-label (tracking ~0.18em) instead.

**Assets.**
- Real imagery, cut out cleanly (rembg) — never flat placeholder rectangles standing in for content.

**Tokens over hardcoding.**
- Every colour, size, radius, and elevation is a variable so the brand moves in one place. No hardcoded hex or spacing.

## Kill on sight (reads "cheap")
Flat card grid on a dark panel · rainbow/3-stop heading gradients · stacked muddy shaders · default-font fallbacks · uniform weight, no type scale · decorative/linear motion that ignores reduced-motion · hardcoded hex/spacing.
