"""Build INDEX.md for exported Claude Code sessions."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Users\user\Downloads\claude-sessions")

def first_h1(p: Path) -> str:
    with p.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("# "):
                return line[2:].strip()
    return p.stem

def parse_date(name: str):
    m = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{4})", name)
    return (m.group(1), m.group(2)) if m else ("", "")

by_project = defaultdict(list)
for md in ROOT.rglob("*.md"):
    if md.name == "INDEX.md":
        continue
    proj = md.parent.name
    title = first_h1(md)
    date, time = parse_date(md.name)
    rel = md.relative_to(ROOT).as_posix()
    by_project[proj].append((date, time, title, rel))

lines = ["# Claude Code session index", ""]
total = sum(len(v) for v in by_project.values())
lines.append(f"_{total} sessions across {len(by_project)} projects._")
lines.append("")

for proj in sorted(by_project):
    items = sorted(by_project[proj], reverse=True)  # newest first
    lines.append(f"## {proj}  _({len(items)})_")
    lines.append("")
    for date, time, title, rel in items:
        ts = f"{date} {time[:2]}:{time[2:]}" if date else "—"
        title_clean = title.replace("|", "\\|")
        lines.append(f"- `{ts}` [{title_clean}]({rel})")
    lines.append("")

(ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {ROOT / 'INDEX.md'} — {total} entries")
