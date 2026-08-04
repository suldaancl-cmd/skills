# /html-everything

A Claude Code skill that converts **any blob of content** — Markdown, JSON, plain text, a URL to a doc — into a single self-contained editorial HTML page with clickable links.

Lightweight: one SKILL.md, no dependencies, no API keys, no build step.

```
/html-everything ~/Documents/scrape.md
/html-everything '{"title": "Q1 picks", "items": [...]}'
/html-everything https://some-doc-url.com/report
/html-everything           ← then paste content inline
```

## What you get

A single `.html` file at `$HTMLE_OUTPUT_DIR` (defaults to `~/Documents/html-everything/`) — editorial scorecard layout, Archivo Black display type, Inter Tight body, JetBrains Mono numerics, every URL wrapped as `<a href>`, responsive, no external assets beyond Google Fonts.

Designed to be **shareable in Slack / email / DMs** where the links matter and PNGs don't.

## Install

```bash
git clone https://github.com/iharnoor/html-everything ~/Developer/html-everything
ln -s ~/Developer/html-everything/skills/html-everything ~/.claude/skills/html-everything
```

Then `/html-everything <input>` works in any session.

## Example

A 5-line markdown blob:

```markdown
# AI coding agents — what I noticed this week

- **Claude Code Agent View** — Anthropic shipped a dashboard for parallel agents · https://x.com/k1rallik/status/2053946261246459950
- **9router** — 40+ provider proxy with 40% token savings, 942★ in a day · https://x.com/conradlotz/status/2053973472150257811
- **r/AI_Agents** ran the contrarian thread of the week · https://www.reddit.com/r/AI_Agents/comments/1taei9m
```

Becomes a fully styled editorial HTML page with the same register as `examples/demo-output.html` in this repo.

## How it works

The skill is a **recipe**, not a binary. SKILL.md tells Claude:

1. Resolve the input (path / URL / inline)
2. Auto-detect content type (Markdown / JSON / plain text)
3. Pick a mood + palette based on content (editorial for tech, mineral for finance, signage for sports, etc.)
4. Generate a single HTML file with the editorial template baked in
5. Save and (optionally) open in browser

No external deps because Claude does the conversion in-context. The skill's value is the **opinionated editorial template + content-aware mood picking**, not the parser.

## Companion skill

Pairs naturally with [`/last72hours`](https://github.com/iharnoor/last72hours-skill) — pipe its raw `.md` scrape into `/html-everything` for a shareable HTML version of any scrape.

## License

MIT.
