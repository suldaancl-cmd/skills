"""Build a single self-contained HTML viewer that looks like Claude Code's sidebar."""
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\user\Downloads\claude-sessions")
OUT = ROOT / "viewer.html"

def first_h1(p: Path) -> str:
    with p.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("# "):
                return line[2:].strip()
    return p.stem

def parse_dt(name: str) -> str:
    m = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{2})(\d{2})", name)
    return f"{m.group(1)} {m.group(2)}:{m.group(3)}" if m else ""

sessions = []
for md in sorted(ROOT.rglob("*.md"), reverse=True):
    if md.name == "INDEX.md":
        continue
    sessions.append({
        "id": md.relative_to(ROOT).as_posix(),
        "title": first_h1(md),
        "project": md.parent.name,
        "datetime": parse_dt(md.name),
        "content": md.read_text(encoding="utf-8", errors="replace"),
    })

print(f"{len(sessions)} sessions, total content {sum(len(s['content']) for s in sessions)/1024:.0f} KB")

DATA_JSON = json.dumps(sessions, ensure_ascii=False)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Claude Code — Session Archive</title>
<style>
  :root {
    --bg: #faf9f7;
    --sidebar: #f5f3ee;
    --border: #e8e4dc;
    --text: #2c2c2c;
    --muted: #8a857c;
    --accent: #c89b3c;
    --hover: #ebe7df;
    --selected: #e2ddd3;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
    font-size: 14px;
    color: var(--text);
    background: var(--bg);
    height: 100vh;
    display: flex;
    overflow: hidden;
  }
  .sidebar {
    width: 320px;
    background: var(--sidebar);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
  }
  .top {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
  }
  .top-item {
    display: flex; align-items: center; gap: 10px;
    padding: 6px 8px; border-radius: 6px;
    color: var(--text); font-size: 14px;
    cursor: default; user-select: none;
  }
  .top-item .icon { width: 16px; text-align: center; color: var(--muted); }
  .search {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
  }
  .search input {
    width: 100%; padding: 7px 10px;
    border: 1px solid var(--border);
    border-radius: 6px; background: white;
    font-size: 13px; outline: none;
  }
  .search input:focus { border-color: var(--accent); }
  .section {
    padding: 10px 14px 4px;
    color: var(--muted);
    font-size: 12px;
    text-transform: lowercase;
    letter-spacing: 0.02em;
  }
  .list {
    flex: 1; overflow-y: auto;
    padding: 0 8px 16px;
  }
  .item {
    display: flex; align-items: center; gap: 10px;
    padding: 7px 10px; border-radius: 6px;
    cursor: pointer;
    font-size: 13.5px;
    color: var(--text);
    line-height: 1.3;
  }
  .item:hover { background: var(--hover); }
  .item.selected { background: var(--selected); }
  .item .dot {
    width: 8px; height: 8px; border-radius: 50%;
    border: 1.5px solid var(--muted);
    flex-shrink: 0;
  }
  .item.recent .dot { background: var(--accent); border-color: var(--accent); }
  .item .title {
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    flex: 1;
  }
  .main {
    flex: 1; overflow-y: auto;
    padding: 28px 40px;
    background: var(--bg);
  }
  .empty {
    color: var(--muted);
    font-size: 14px;
    margin-top: 80px;
    text-align: center;
  }
  .meta {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 14px;
  }
  .markdown { max-width: 760px; line-height: 1.55; }
  .markdown h1 { font-size: 22px; margin: 0 0 18px; }
  .markdown h2 {
    font-size: 14px;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
    padding-bottom: 4px;
    margin-top: 28px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-weight: 500;
  }
  .markdown h2.user { color: #6b4f12; }
  .markdown h2.assistant { color: #2c5e3f; }
  .markdown code {
    background: #efebe2;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 12.5px;
    font-family: "Cascadia Code", Consolas, monospace;
  }
  .markdown pre {
    background: #efebe2;
    padding: 10px 14px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 12.5px;
  }
  .markdown p { margin: 8px 0; white-space: pre-wrap; }
  .markdown em { color: var(--muted); }
  .project-tag {
    font-size: 10px; color: var(--muted);
    background: var(--hover);
    padding: 1px 5px;
    border-radius: 3px;
    margin-left: 6px;
  }
  ::-webkit-scrollbar { width: 8px; }
  ::-webkit-scrollbar-thumb { background: #d6d1c6; border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: #b8b2a4; }
</style>
</head>
<body>
<div class="sidebar">
  <div class="top">
    <div class="top-item"><span class="icon">+</span> New session</div>
    <div class="top-item"><span class="icon">⚡</span> Routines</div>
    <div class="top-item"><span class="icon">⚙</span> Customize</div>
    <div class="top-item"><span class="icon">▾</span> More</div>
  </div>
  <div class="search">
    <input id="q" type="text" placeholder="Search __COUNT__ chats…" autofocus>
  </div>
  <div class="section">Recents</div>
  <div class="list" id="list"></div>
</div>
<div class="main" id="main">
  <div class="empty">Select a chat from the sidebar.</div>
</div>

<script>
const SESSIONS = __DATA__;
const list = document.getElementById('list');
const main = document.getElementById('main');
const q = document.getElementById('q');
let selected = null;

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function renderMarkdown(md) {
  const lines = md.split('\\n');
  let html = ''; let inCode = false;
  for (let raw of lines) {
    if (raw.startsWith('```')) {
      html += inCode ? '</pre>' : '<pre>';
      inCode = !inCode; continue;
    }
    if (inCode) { html += escapeHtml(raw) + '\\n'; continue; }
    if (raw.startsWith('# ')) { html += '<h1>' + escapeHtml(raw.slice(2)) + '</h1>'; continue; }
    if (raw.startsWith('## ')) {
      const txt = raw.slice(3);
      const cls = txt.startsWith('User') ? 'user' : txt.startsWith('Assistant') ? 'assistant' : '';
      html += '<h2 class="' + cls + '">' + escapeHtml(txt) + '</h2>'; continue;
    }
    let line = escapeHtml(raw)
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>')
      .replace(/_([^_]+)_/g, '<em>$1</em>');
    html += line ? '<p>' + line + '</p>' : '';
  }
  return html;
}

function render(filter='') {
  const f = filter.toLowerCase();
  list.innerHTML = '';
  let count = 0;
  SESSIONS.forEach((s, i) => {
    if (f && !s.title.toLowerCase().includes(f)
          && !s.project.toLowerCase().includes(f)
          && !s.content.toLowerCase().includes(f)) return;
    count++;
    const div = document.createElement('div');
    div.className = 'item' + (i < 3 ? ' recent' : '') + (selected === i ? ' selected' : '');
    div.innerHTML = '<span class="dot"></span><span class="title">'
      + escapeHtml(s.title) + '</span>';
    div.title = s.project + '  ·  ' + s.datetime;
    div.onclick = () => { selected = i; show(s); render(filter); };
    list.appendChild(div);
  });
  if (count === 0) {
    list.innerHTML = '<div style="padding:14px;color:var(--muted);font-size:12px">No matches.</div>';
  }
}

function show(s) {
  main.innerHTML = '<div class="meta">' + escapeHtml(s.datetime) + '  ·  '
    + escapeHtml(s.project) + '</div><div class="markdown">'
    + renderMarkdown(s.content) + '</div>';
  main.scrollTop = 0;
}

q.addEventListener('input', e => render(e.target.value));
render();
</script>
</body>
</html>
"""

html = HTML.replace("__DATA__", DATA_JSON).replace("__COUNT__", str(len(sessions)))
OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT}  ({OUT.stat().st_size/1024/1024:.2f} MB)")
