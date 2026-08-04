"""Export all Claude Code .jsonl sessions to readable Markdown."""
import json, re, sys
from pathlib import Path
from datetime import datetime

SRC = Path(r"C:\Users\user\.claude\projects")
DST = Path(r"C:\Users\user\Downloads\claude-sessions")
DST.mkdir(parents=True, exist_ok=True)

SKIP_PREFIXES = ("<ide_opened_file>", "<system-reminder>", "<command-message>",
                 "<command-name>", "<command-args>", "<local-command-stdout>")

def slug(s, n=60):
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:n] or "untitled"

def block_to_md(block):
    t = block.get("type")
    if t == "text":
        text = block.get("text", "").strip()
        if any(text.startswith(p) for p in SKIP_PREFIXES):
            return None
        return text or None
    if t == "thinking":
        thought = block.get("thinking", "").strip()
        return f"_[thinking]_ {thought}" if thought else None
    if t == "tool_use":
        name = block.get("name", "tool")
        inp = block.get("input", {})
        # short summary of tool call
        if name == "Bash":
            return f"`$ {inp.get('command','')[:200]}`"
        if name in ("Read", "Edit", "Write"):
            return f"_[{name}]_ `{inp.get('file_path','')}`"
        if name in ("Grep", "Glob"):
            return f"_[{name}]_ `{inp.get('pattern','')}`"
        if name == "TodoWrite":
            return "_[TodoWrite]_"
        if name == "Task" or name == "Agent":
            return f"_[Agent: {inp.get('subagent_type','')}]_ {inp.get('description','')}"
        return f"_[{name}]_"
    if t == "tool_result":
        # skip — usually noisy
        return None
    if t == "image":
        return "_[image]_"
    return None

def message_to_md(d):
    msg = d.get("message", {})
    content = msg.get("content", "")
    parts = []
    if isinstance(content, str):
        if content.strip() and not any(content.startswith(p) for p in SKIP_PREFIXES):
            parts.append(content.strip())
    else:
        for b in content:
            md = block_to_md(b)
            if md:
                parts.append(md)
    return "\n\n".join(parts).strip()

def export_one(jsonl_path, project_name):
    title = None
    first_prompt = None
    first_ts = None
    turns = []
    with jsonl_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            t = d.get("type")
            if t == "ai-title":
                title = d.get("aiTitle")
            elif t in ("user", "assistant") and not d.get("isSidechain"):
                ts = d.get("timestamp")
                if not first_ts:
                    first_ts = ts
                body = message_to_md(d)
                if not body:
                    continue
                if t == "user" and not first_prompt:
                    first_prompt = body[:80]
                turns.append((t, ts, body))

    if not turns:
        return None

    # filename
    try:
        dt = datetime.fromisoformat(first_ts.replace("Z", "+00:00"))
        date_part = dt.strftime("%Y-%m-%d_%H%M")
    except Exception:
        date_part = "unknown-date"
    name_part = slug(title or first_prompt or jsonl_path.stem)
    out_dir = DST / project_name
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{date_part}_{name_part}.md"

    lines = [f"# {title or first_prompt or 'Untitled session'}",
             f"_Source: `{jsonl_path}`_", ""]
    for role, ts, body in turns:
        prefix = "## User" if role == "user" else "## Assistant"
        if ts:
            prefix += f"  _{ts}_"
        lines.append(prefix)
        lines.append("")
        lines.append(body)
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out

def main():
    count = 0
    skipped = 0
    for project_dir in sorted(SRC.iterdir()):
        if not project_dir.is_dir():
            continue
        for jsonl in project_dir.glob("*.jsonl"):
            res = export_one(jsonl, project_dir.name)
            if res:
                count += 1
            else:
                skipped += 1
    print(f"Exported: {count}    Skipped (empty): {skipped}    Output: {DST}")

if __name__ == "__main__":
    main()
