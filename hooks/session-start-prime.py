"""SessionStart hook: prime new sessions with vault state.

Injects via hookSpecificOutput.additionalContext:
- Today's UTC date
- MEMORY.md content (truncated if >200 lines)
- 3 most-recent feedback_*.md titles
- Latest precompact_*.md (skip if >7 days old)
- Brief MCP / hook health line
- Staged-drafts count if any waiting in ~/.claude/snapshots/staged_writes/

Token budget cap: ~3000 chars total. Always exits 0; never blocks startup.
"""
import datetime
import glob
import json
import os
import sys


VAULT = r"C:/Users/user/.claude/projects/C--Users-user--claude-skills/memory"
SNAPSHOTS = r"C:/Users/user/.claude/snapshots"
STAGED = os.path.join(SNAPSHOTS, "staged_writes")
SETTINGS = r"C:/Users/user/.claude/settings.json"
MCP = r"C:/Users/user/.claude/.mcp.json"
MAX_TOTAL_CHARS = 3000


def safe_read(path: str, max_lines: int | None = None) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            if max_lines is None:
                return fh.read()
            lines = []
            for i, ln in enumerate(fh):
                if i >= max_lines:
                    lines.append(f"... [truncated at {max_lines} lines]")
                    break
                lines.append(ln.rstrip("\n"))
            return "\n".join(lines)
    except Exception:
        return ""


def title_of(path: str) -> str:
    txt = safe_read(path, max_lines=40)
    lines = txt.splitlines()
    in_frontmatter = False
    saw_frontmatter_open = False
    for ln in lines:
        s = ln.strip()
        if s == "---":
            if not saw_frontmatter_open:
                saw_frontmatter_open = True
                in_frontmatter = True
                continue
            else:
                in_frontmatter = False
                continue
        if in_frontmatter:
            continue
        if s.startswith("#"):
            return s.lstrip("#").strip()
        if s:
            return s[:80]
    return os.path.basename(path)


def latest_precompact() -> tuple[str, float] | None:
    pattern = os.path.join(SNAPSHOTS, "precompact_*.md")
    files = glob.glob(pattern)
    if not files:
        return None
    files.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    p = files[0]
    age_days = (datetime.datetime.now().timestamp() - os.path.getmtime(p)) / 86400
    if age_days > 7:
        return None
    return (p, age_days)


def recent_feedback_titles(limit: int = 3) -> list[str]:
    pattern = os.path.join(VAULT, "feedback_*.md")
    files = glob.glob(pattern)
    files.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return [title_of(p) for p in files[:limit]]


def hook_event_names() -> list[str]:
    try:
        with open(SETTINGS, encoding="utf-8") as fh:
            d = json.load(fh)
        return list(d.get("hooks", {}).keys())
    except Exception:
        return []


def mcp_server_names() -> list[str]:
    try:
        with open(MCP, encoding="utf-8") as fh:
            d = json.load(fh)
        return list(d.get("mcpServers", {}).keys())
    except Exception:
        return []


def staged_count() -> int:
    if not os.path.isdir(STAGED):
        return 0
    n = 0
    for _root, _dirs, files in os.walk(STAGED):
        n += sum(1 for f in files if f.endswith(".md"))
    return n


def routing_system_health() -> str:
    """Self-check the skill-routing system; returns '' when healthy."""
    problems = []
    routes_path = r"C:/Users/user/.claude/skill-routes.json"
    router_path = r"C:/Users/user/.claude/hooks/skill-router.py"
    agents_path = r"C:/Users/user/.claude/AGENTS.md"
    try:
        with open(routes_path, encoding="utf-8") as fh:
            table = json.load(fh)
        if not table.get("domains"):
            problems.append("skill-routes.json has no domains")
    except Exception as e:
        problems.append(f"skill-routes.json unreadable/invalid ({type(e).__name__})")
    if not os.path.exists(router_path):
        problems.append("hooks/skill-router.py missing")
    if not os.path.exists(agents_path):
        problems.append("AGENTS.md (step-gate system) missing")
    if not problems:
        return ""
    return (
        "🚨 ROUTING SYSTEM BROKEN: " + "; ".join(problems)
        + ". Restore from git (`git -C C:/Users/user/.claude checkout -- <file>`) "
        "or re-run system-maintain BEFORE doing other work. Until fixed, manually "
        "obey AGENTS.md gates: route skills, read vault playbooks, verify with proof."
    )


def build_context() -> str:
    parts: list[str] = []

    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    parts.append(f"# Session prime — {today}")

    health = routing_system_health()
    if health:
        parts.append(health)

    mcps = mcp_server_names()
    hooks = hook_event_names()
    parts.append(
        f"MCPs: {', '.join(mcps) or '(none)'}  |  Hooks: {', '.join(hooks) or '(none)'}"
    )

    n_staged = staged_count()
    if n_staged:
        parts.append(
            f"⚠ {n_staged} staged draft(s) from prior sessions in ~/.claude/snapshots/staged_writes/ — "
            f"say `review staged drafts` to promote/discard."
        )

    fb = recent_feedback_titles(3)
    if fb:
        parts.append("Most recent user feedback notes:")
        for t in fb:
            parts.append(f"  - {t}")

    parts.append("\n## MEMORY.md (vault index)")
    mem = safe_read(os.path.join(VAULT, "MEMORY.md"), max_lines=200)
    parts.append(mem if mem else "(MEMORY.md not found or empty)")

    pc = latest_precompact()
    if pc:
        path, age_days = pc
        parts.append(f"\n## Last session snapshot ({age_days:.1f}d ago) — {os.path.basename(path)}")
        snap = safe_read(path)
        parts.append(snap)

    out = "\n".join(parts)
    if len(out) > MAX_TOTAL_CHARS:
        out = out[:MAX_TOTAL_CHARS] + f"\n... [truncated at {MAX_TOTAL_CHARS} chars]"
    return out


def safe_main() -> None:
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    ctx = build_context()
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": ctx,
        }
    }
    print(json.dumps(out))


def main() -> None:
    try:
        safe_main()
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
