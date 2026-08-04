---
name: html-everything
version: "0.1.0"
description: "Convert any blob — Markdown, JSON, plain text, or a URL to a doc — into a single self-contained editorial HTML page with clickable links. Lightweight, no deps, no API keys."
argument-hint: 'html-everything <file-path> | html-everything <url> | html-everything (then paste)'
allowed-tools: Bash, Read, Write, WebFetch
homepage: https://github.com/iharnoor/html-everything
repository: https://github.com/iharnoor/html-everything
author: iharnoor
license: MIT
user-invocable: true
---

# /html-everything

You take any input — a file path, a URL, or pasted content — and produce one self-contained HTML file in editorial-scorecard register. Every URL in the input becomes a clickable `<a href>` in the output. No external assets beyond Google Fonts.

This skill is a **recipe**, not a parser binary. You (Claude) do the conversion in-context.

## Step 1 — Resolve input

The user's `<argument>` is one of:

| Pattern | Action |
|---|---|
| `^https?://` | `WebFetch` the URL, ask for the raw text content |
| existing file path | `Read` the file |
| anything else | treat as inline content |
| empty | ask the user to paste content, wait |

After resolution, you have a string `CONTENT`. Set:
- `OUT_DIR` = `${HTMLE_OUTPUT_DIR:-$HOME/Documents/html-everything}` and `mkdir -p`
- `SLUG` = short kebab-case from the first non-empty heading/line of `CONTENT` (max 50 chars)
- `OUT_PATH` = `$OUT_DIR/$SLUG.html`

## Step 2 — Detect content type

Cheap heuristics, top to bottom:

| Signal | Type |
|---|---|
| First non-whitespace char is `{` or `[`, content parses as JSON | `json` |
| Contains `# ` headings, `**bold**`, `- ` bullets, or `[text](url)` links | `markdown` |
| Contains JSON-like `key: value` lines without markdown markers | `key-value` |
| Otherwise | `prose` |

## Step 3 — Pick a mood (lightweight per-run pick)

Scan the content for topic signal. Pick ONE mood word — derive palette from it. Do not delegate to other skills.

| Topic signal | Mood | Ground | Accent | Notes |
|---|---|---|---|---|
| AI / dev / tech / agents / coding | **editorial** | `#FFFFFF` | `#0029FF` cobalt | Default. Swiss-print magazine cover. |
| finance / markets / earnings / portfolio | **bookish** | `#F5F0E6` plaster | `#1A1A2E` ink | Book-jacket sobriety. |
| sports / playoffs / brackets | **signage** | `#FFFFFF` | `#FFB300` chrome yellow | Highway-sign bold. |
| politics / policy / regulation | **mineral** | `#EDEAE3` limestone | `#5C4033` weathered slate | Gravitas without preaching. |
| product launch / consumer | **highlighter** | `#FFFFFF` | `#FFEA00` fluorescent yellow | Buzzy without screaming. |
| nightlife / music / entertainment | **nocturnal** | `#1A1A1A` wet asphalt | `#FF1493` hot pink | Dark mode flips on. |
| science / research / data | **alpine** | `#F8FAFC` snow | `#0F4C5C` evergreen | Cold, clear, factual. |
| nothing fits | **editorial** (fall back) | `#FFFFFF` | `#0029FF` cobalt | Don't agonize. |

The mood word goes in the eyebrow line of the rendered page (`Mood · {mood}`). It signals intentionality — the page wasn't templated, it was tuned.

## Step 4 — Generate HTML

Write one self-contained file to `$OUT_PATH`. Use the canonical template below. Substitute `{TOKENS}`.

### Canonical template (single file)

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{TITLE} · /html-everything</title>
<meta name="description" content="{DESCRIPTION}" />
<meta name="generator" content="/html-everything · https://github.com/iharnoor/html-everything" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" />
<style>
  :root {
    --ground: {GROUND};
    --ink: {INK};
    --accent: {ACCENT};
    --mute: {MUTE};
    --hair: {HAIR};
    --panel: {PANEL};
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--ground); color: var(--ink); }
  body { font-family: 'Inter Tight', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
  a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
  a:hover { text-decoration-thickness: 2px; }
  .wrap { max-width: 1100px; margin: 0 auto; padding: 80px 64px; display: flex; flex-direction: column; gap: 56px; }
  .eyebrow { display: flex; align-items: center; gap: 12px; font-weight: 500; font-size: 11px; letter-spacing: 0.2em; color: var(--mute); text-transform: uppercase; }
  .eyebrow .dot { width: 7px; height: 7px; background: var(--accent); border-radius: 50%; display: inline-block; }
  h1.display { font-family: 'Archivo Black', system-ui, sans-serif; font-size: 96px; line-height: 92px; letter-spacing: -0.03em; margin: 0; max-width: 18ch; }
  h2 { font-family: 'Archivo Black', system-ui, sans-serif; font-size: 36px; line-height: 42px; letter-spacing: -0.02em; margin: 0 0 16px 0; }
  h3 { font-family: 'Archivo Black', system-ui, sans-serif; font-size: 22px; line-height: 26px; letter-spacing: -0.01em; margin: 0 0 8px 0; }
  p { font-size: 16px; line-height: 24px; margin: 0 0 16px 0; max-width: 70ch; }
  ul, ol { padding-left: 24px; }
  li { font-size: 16px; line-height: 24px; margin-bottom: 8px; }
  code, .mono { font-family: 'JetBrains Mono', monospace; font-size: 14px; }
  pre { background: var(--panel); padding: 16px 20px; overflow-x: auto; font-size: 13px; line-height: 20px; }
  blockquote { border-left: 4px solid var(--accent); padding: 4px 20px; margin: 16px 0; color: var(--mute); font-style: normal; }
  .thesis { display: flex; gap: 0; }
  .thesis .strip { width: 6px; background: var(--accent); flex-shrink: 0; }
  .thesis .body { padding: 20px 28px; flex: 1; }
  .section { padding-top: 24px; border-top: 1px solid var(--hair); }
  .card { padding: 24px 0; border-top: 1px solid var(--ink); display: flex; flex-direction: column; gap: 12px; }
  .meta-row { display: flex; gap: 24px; align-items: baseline; flex-wrap: wrap; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--mute); }
  .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }
  footer { padding-top: 32px; border-top: 2px solid var(--ink); font-size: 13px; color: var(--mute); display: flex; justify-content: space-between; align-items: baseline; gap: 16px; }
  @media (max-width: 640px) { .wrap { padding: 40px 24px; gap: 32px; } h1.display { font-size: 56px; line-height: 56px; } .grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<main class="wrap">

  <div class="eyebrow">
    <span class="dot"></span>
    <span>{EYEBROW}</span>
    <span style="margin-left:auto;color:var(--mute);">Mood · {MOOD}</span>
  </div>

  <h1 class="display">{HEADLINE}</h1>

  <!-- Optional thesis block if the input has a clear one-line argument -->
  {THESIS_BLOCK}

  <!-- Body sections — one per heading group in the source -->
  {BODY_SECTIONS}

  <footer>
    <span>Generated by <a href="https://github.com/iharnoor/html-everything">/html-everything</a> · {DATE}</span>
    <span class="mono">{SOURCE_HINT}</span>
  </footer>

</main>
</body>
</html>
```

### Rendering rules by content type

**`markdown`:**
- `# H1` → `<h1 class="display">` (first one becomes the page headline; subsequent become `<h2>`)
- `## H2` → `<h2>` inside a `.section`
- `### H3` → `<h3>` inside a `.card`
- `- item` / `* item` lists → `<ul>` / `<ol>`
- `**bold**` → `<b>` (used for headline phrases in lead-in paragraphs)
- `[text](url)` → `<a href="url">text</a>` (preserve exactly)
- Raw URLs (lines that ARE just a URL) → wrap in `<a>` and use the domain as link text
- `> quote` → `<blockquote>`
- Code blocks → `<pre>`
- Inline `` `code` `` → `<code>`

**`json`:**
- Look for common shapes: `{title, items: [...]}`, `{headline, sections: [...]}`, `{topic, top: [...], clusters: [...]}`
- `title` / `headline` / `topic` → `<h1 class="display">`
- `items[]` with `{title, url, snippet, stats?}` → render as cards in a `.grid` or vertical stack
- `sections[]` with `{name, body}` → render as `.section` blocks
- Unknown keys: emit as `<dl>` definition list under a "Data" section
- Always linkify URL values

**`key-value` / `prose`:**
- First non-empty line → `<h1 class="display">`
- Subsequent paragraphs → `<p>`
- Bullet-shaped lines → `<ul>`
- URLs anywhere → wrap as `<a>`

### Link rule (every type)

Anything that matches `https?://[^\s)<>"']+` becomes a clickable link. Never emit a bare URL. If the link is in a sentence, link only the URL substring; if the line IS just a URL, replace it with `<a href="<URL>">domain-and-path-shortened</a>` (drop protocol, drop `www.`, keep ~50 chars).

## Step 5 — Save + open

```bash
# Write the HTML to OUT_PATH (via Write tool, not echo)
# Then:
open "$OUT_PATH" 2>/dev/null || xdg-open "$OUT_PATH" 2>/dev/null || echo "Wrote: $OUT_PATH"
```

If the user passed `--no-open` (anywhere in the argument), skip the `open`.

## Step 6 — Reply

Reply with under 150 words:

```
Rendered → <OUT_PATH>
Mood: <mood>  ·  Type: <markdown|json|prose|key-value>
Sections: <N>
Links: <count of <a href> in output>
```

If links count is zero on input that clearly had URLs, that's a regression — regenerate.

## Lightweight rules (non-negotiable)

- Never delegate to `frontend-design`, `ui-ux-pro-max`, or other heavy skills. The template is the design.
- Never install packages. No `npm install`, no `pip install`.
- Never write a parser script — you (Claude) parse inline.
- One HTML file out per run. No CSS files, no JS files, no images saved separately.
- Don't show the user the raw HTML in chat unless they ask. Just the path + summary.

## Secret hygiene

- If `CONTENT` contains anything matching API key shapes (`sk_…`, `xai-…`, `gho_…`, `AKIA…`, `AIza…`, `-----BEGIN … PRIVATE KEY-----`), refuse to render and warn the user. Their input may contain secrets they didn't mean to share.
- Never include `.env` content in output.

## Companion skill

If the input is a `/last30days` or `/last72hours` raw `.md` scrape, this skill produces the same shape as `iharnoor/last72hours-skill/examples/ai-coding-agents-72h-radar.html`. Pipe scrape → render → share.
