"""PreCompact hook: snapshot active session state before compaction wipes it.

Reads stdin PreCompact payload, walks the JSONL transcript, extracts:
- last 10 user prompts (truncated)
- latest TodoWrite state
- recent file modifications (Edit/Write file_paths)
- recent Bash commands (truncated)
- "current task" header from last user prompt + first 200 chars of last assistant text

Writes to ~/.claude/snapshots/precompact_<session_id>.md (overwrites per session).
NEVER blocks compaction — all errors swallowed, always exits 0.
"""
import datetime
import json
import os
import sys


def safe_main() -> None:
    inp = json.load(sys.stdin)
    session_id = inp.get("session_id", "unknown")
    transcript_path = inp.get("transcript_path", "")
    trigger = inp.get("trigger", "unknown")
    cwd = inp.get("cwd", "")

    if not transcript_path or not os.path.exists(transcript_path):
        return

    with open(transcript_path, encoding="utf-8") as fh:
        lines = fh.readlines()

    user_prompts: list[str] = []
    file_paths: list[str] = []
    bash_cmds: list[str] = []
    latest_todos = None
    last_assistant_text = ""
    last_user_text = ""

    for line in lines:
        try:
            entry = json.loads(line)
        except Exception:
            continue
        etype = entry.get("type")
        msg = entry.get("message", {}) or {}
        content = msg.get("content")

        if etype == "user":
            # Skip tool_result echoes — Skill/Agent/mcp outputs come back as user-role.
            # Without this, "Last 10 user prompts" gets polluted with skill outputs.
            if isinstance(content, list) and any(
                isinstance(b, dict) and b.get("type") == "tool_result"
                for b in content
            ):
                continue
            text = ""
            if isinstance(content, str):
                text = content
            elif isinstance(content, list):
                text = " ".join(
                    c.get("text", "")
                    for c in content
                    if isinstance(c, dict) and c.get("type") == "text"
                )
            text = text.strip()
            if text:
                user_prompts.append(text[:300])
                last_user_text = text

        elif etype == "assistant":
            blocks = content if isinstance(content, list) else []
            text_chunks: list[str] = []
            for b in blocks:
                if not isinstance(b, dict):
                    continue
                btype = b.get("type")
                if btype == "text":
                    text_chunks.append(b.get("text", "") or "")
                elif btype == "tool_use":
                    name = b.get("name", "") or ""
                    tool_input = b.get("input", {}) or {}
                    if name == "TodoWrite":
                        todos = tool_input.get("todos")
                        if isinstance(todos, list):
                            latest_todos = todos
                    elif name in ("Edit", "Write"):
                        fp = tool_input.get("file_path", "")
                        if fp:
                            file_paths.append(fp)
                    elif name == "Bash":
                        cmd = (tool_input.get("command", "") or "")[:200]
                        if cmd:
                            bash_cmds.append(cmd)
            if text_chunks:
                last_assistant_text = " ".join(text_chunks).strip()

    last_10_prompts = user_prompts[-10:]
    seen: set[str] = set()
    distinct_files: list[str] = []
    for fp in reversed(file_paths):
        if fp not in seen:
            seen.add(fp)
            distinct_files.append(fp)
        if len(distinct_files) >= 30:
            break
    distinct_files.reverse()
    last_files = distinct_files[-30:]

    last_bash = bash_cmds[-10:]

    snapshots_dir = r"C:/Users/user/.claude/snapshots"
    os.makedirs(snapshots_dir, exist_ok=True)
    out_path = os.path.join(snapshots_dir, f"precompact_{session_id}.md")

    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    out_lines = [
        f"# Pre-compact snapshot — {now} ({trigger})",
        f"Session: `{session_id}`  CWD: `{cwd}`",
        "",
        "## Current task",
        f"> {last_user_text[:500] if last_user_text else '(none)'}",
        "",
        "Last assistant action (first 200 chars):",
        last_assistant_text[:200] if last_assistant_text else "(none)",
        "",
        "## Active todos",
    ]
    if latest_todos:
        for t in latest_todos:
            if not isinstance(t, dict):
                continue
            status = t.get("status", "pending")
            content_val = t.get("content", "") or t.get("activeForm", "")
            mark = {"completed": "x", "in_progress": "~"}.get(status, " ")
            out_lines.append(f"- [{mark}] {content_val}")
    else:
        out_lines.append("(no TodoWrite found in transcript)")
    out_lines.append("")

    out_lines.append("## Recent files touched")
    if last_files:
        for fp in last_files:
            out_lines.append(f"- {fp}")
    else:
        out_lines.append("(no Edit/Write tool calls found)")
    out_lines.append("")

    out_lines.append("## Recent bash")
    if last_bash:
        for cmd in last_bash:
            short = cmd.replace("\n", " ⏎ ")
            out_lines.append(f"- `{short}`")
    else:
        out_lines.append("(no Bash tool calls found)")
    out_lines.append("")

    out_lines.append("## Last 10 user prompts")
    if last_10_prompts:
        for i, p in enumerate(last_10_prompts, 1):
            short = p.replace("\n", " ⏎ ")
            out_lines.append(f"{i}. {short}")
    else:
        out_lines.append("(no user prompts found)")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out_lines) + "\n")


def main() -> None:
    try:
        safe_main()
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
