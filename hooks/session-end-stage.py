"""SessionEnd hook: stage candidate memory notes from the session transcript.

Walks the transcript looking for:
  - "remember X" / "don't X" / "always X" patterns in user messages → feedback_*.md draft
  - new infra installed (Edit/Write into ~/.claude/{skills,agents,hooks}/, .mcp.json, settings.json) → reference_*.md draft
  - "playbook for X" / "the workflow is" → playbook_*.md draft (best-effort, low signal)

Writes drafts to ~/.claude/snapshots/staged_writes/<session-id>/.
NEVER writes to the vault — that's gated by the `review-staged-drafts` skill.
Never blocks SessionEnd; all errors swallowed.
"""
import datetime
import json
import os
import re
import sys


STAGED_ROOT = r"C:/Users/user/.claude/snapshots/staged_writes"
CLAUDE_DIR = r"C:/Users/user/.claude"

REMEMBER_PATTERNS = [
    r"\bremember (?:this|that)?\b[:,]?\s*(.{8,200})",
    r"\bsave (?:this|that) (?:as|to) (?:memory|feedback|reference|a note)\b[:,]?\s*(.{0,200})",
    r"\bsave reference for\b[:,]?\s*(.{8,200})",
]
RULE_PATTERNS = [
    r"\b(?:never|don't|do not|stop) (.{8,200}?)(?:[.!?\n]|$)",
    r"\balways (.{8,200}?)(?:[.!?\n]|$)",
    r"\bfrom now on,? (.{8,200}?)(?:[.!?\n]|$)",
]
PLAYBOOK_PATTERNS = [
    r"\bplaybook (?:for|to) (.{8,200}?)(?:[.!?\n]|$)",
    r"\bnext time (.{8,200}?)(?:[.!?\n]|$)",
    r"\bthe workflow (?:is|should be) (.{8,200}?)(?:[.!?\n]|$)",
]


def slugify(s: str, max_len: int = 40) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s[:max_len] or "unnamed"


def safe_extract_user_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            c.get("text", "")
            for c in content
            if isinstance(c, dict) and c.get("type") == "text"
        )
    return ""


def walk_transcript(path: str):
    """Yield (kind, payload) tuples. kind ∈ {user_text, tool_use}."""
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                except Exception:
                    continue
                etype = entry.get("type")
                msg = entry.get("message", {}) or {}
                content = msg.get("content")
                if etype == "user":
                    # Skip tool_result echoes — Skill/Agent/mcp outputs come back as user-role.
                    if isinstance(content, list) and any(
                        isinstance(b, dict) and b.get("type") == "tool_result"
                        for b in content
                    ):
                        continue
                    text = safe_extract_user_text(content).strip()
                    if text:
                        yield ("user_text", text)
                elif etype == "assistant":
                    blocks = content if isinstance(content, list) else []
                    for b in blocks:
                        if isinstance(b, dict) and b.get("type") == "tool_use":
                            yield (
                                "tool_use",
                                {"name": b.get("name", ""), "input": b.get("input", {}) or {}},
                            )
    except Exception:
        return


def collect_feedback_candidates(user_texts: list[str]) -> list[tuple[str, str]]:
    """Return list of (slug, rule_text) tuples — deduplicated."""
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for text in user_texts:
        for pat in REMEMBER_PATTERNS + RULE_PATTERNS:
            for m in re.finditer(pat, text, flags=re.IGNORECASE):
                rule = m.group(1).strip().rstrip(".,!?")
                if not rule or len(rule) < 8:
                    continue
                slug = slugify(rule, max_len=40)
                if slug in seen:
                    continue
                seen.add(slug)
                out.append((slug, rule))
    return out


def collect_playbook_candidates(user_texts: list[str]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for text in user_texts:
        for pat in PLAYBOOK_PATTERNS:
            for m in re.finditer(pat, text, flags=re.IGNORECASE):
                topic = m.group(1).strip().rstrip(".,!?")
                slug = slugify(topic, max_len=40)
                if slug in seen:
                    continue
                seen.add(slug)
                out.append((slug, topic))
    return out


def collect_infra_changes(tool_uses: list[dict]) -> dict[str, list[str]]:
    """Group new-infra paths by category."""
    groups = {"skills": [], "agents": [], "hooks": [], "mcp": [], "settings": [], "other": []}
    seen: set[str] = set()
    for t in tool_uses:
        name = t.get("name", "")
        if name not in ("Edit", "Write"):
            continue
        fp = (t.get("input", {}) or {}).get("file_path", "")
        if not fp or fp in seen:
            continue
        seen.add(fp)
        norm = fp.replace("\\", "/").lower()
        if "/.claude/skills/" in norm:
            groups["skills"].append(fp)
        elif "/.claude/agents/" in norm:
            groups["agents"].append(fp)
        elif "/.claude/hooks/" in norm:
            groups["hooks"].append(fp)
        elif norm.endswith("/.mcp.json"):
            groups["mcp"].append(fp)
        elif norm.endswith("/settings.json") and "/.claude/" in norm:
            groups["settings"].append(fp)
    return groups


def write_draft(out_dir: str, name: str, body: str) -> str:
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return path


def safe_main() -> None:
    inp = json.load(sys.stdin)
    session_id = inp.get("session_id", f"unknown_{int(datetime.datetime.now().timestamp())}")
    transcript_path = inp.get("transcript_path", "")

    if not transcript_path or not os.path.exists(transcript_path):
        return

    user_texts: list[str] = []
    tool_uses: list[dict] = []
    for kind, payload in walk_transcript(transcript_path):
        if kind == "user_text":
            user_texts.append(payload)
        elif kind == "tool_use":
            tool_uses.append(payload)

    feedback = collect_feedback_candidates(user_texts)
    playbooks = collect_playbook_candidates(user_texts)
    infra = collect_infra_changes(tool_uses)

    if not feedback and not playbooks and not any(infra.values()):
        return

    out_dir = os.path.join(STAGED_ROOT, session_id)
    os.makedirs(out_dir, exist_ok=True)
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    written: list[str] = []

    for slug, rule in feedback[:20]:
        body = (
            f"---\n"
            f"name: {slug}\n"
            f"description: Candidate user-rule extracted from session on {today}\n"
            f"type: feedback\n"
            f"---\n\n"
            f"# Candidate feedback — {slug}\n\n"
            f"Extracted user instruction: **{rule}**\n\n"
            f"**Why:** (verify with user — heuristic extraction may miss context)\n"
            f"**How to apply:** (verify with user)\n\n"
            f"Source: session {session_id}, captured {today}.\n"
        )
        written.append(write_draft(out_dir, f"feedback_{slug}.md", body))

    for slug, topic in playbooks[:10]:
        body = (
            f"---\n"
            f"name: {slug}\n"
            f"description: Candidate playbook extracted from session on {today}\n"
            f"type: playbook\n"
            f"---\n\n"
            f"# Candidate playbook — {slug}\n\n"
            f"User mentioned procedure: **{topic}**\n\n"
            f"Steps: (verify with user — heuristic extraction; the actual procedure is in the session transcript)\n\n"
            f"Source: session {session_id}, captured {today}.\n"
        )
        written.append(write_draft(out_dir, f"playbook_{slug}.md", body))

    for category, paths in infra.items():
        if not paths:
            continue
        slug = f"session_{session_id[:8]}_{category}"
        body = (
            f"---\n"
            f"name: {slug}\n"
            f"description: New {category} files written/edited during session on {today}\n"
            f"type: reference\n"
            f"---\n\n"
            f"# New {category} infra — {today}\n\n"
            f"Files touched in this session:\n\n"
        )
        for p in paths[:30]:
            body += f"- `{p}`\n"
        body += f"\nSource: session {session_id}, captured {today}.\n"
        written.append(write_draft(out_dir, f"reference_{slug}.md", body))

    summary = os.path.join(out_dir, "_INDEX.md")
    with open(summary, "w", encoding="utf-8") as fh:
        fh.write(f"# Staged drafts — session {session_id}\n\n")
        fh.write(f"Captured {today} ({len(written)} drafts).\n\n")
        for w in written:
            fh.write(f"- {os.path.basename(w)}\n")
        fh.write(
            "\nReview with: say `review staged drafts` (invokes the consent-gate skill).\n"
        )


def main() -> None:
    try:
        safe_main()
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
