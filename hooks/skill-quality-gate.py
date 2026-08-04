"""SessionStart hook: emits a one-line health summary about the skill library.

Wires into Claude Code's SessionStart event. Reads the latest lint report (if
recent) and prints a short status line. If the lint report is older than 24h,
re-runs the extractor + linter first.

Output goes to stdout — Claude's session-start prime hook captures it.

Usage (registered in settings.json under hooks.SessionStart):
    python hooks/skill-quality-gate.py
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

CLAUDE = Path(r"C:\Users\user\.claude") if os.name == "nt" else Path("/root/.claude")
META = CLAUDE / "tmp" / "skills_meta.json"
REPORT = CLAUDE / "tmp" / "skill_lint_report.md"
EXTRACT = CLAUDE / "scripts" / "extract_skill_meta.py"
LINT = CLAUDE / "scripts" / "lint_skills.py"
MAX_AGE_SEC = 24 * 3600


def stale(p: Path) -> bool:
    if not p.exists():
        return True
    return (time.time() - p.stat().st_mtime) > MAX_AGE_SEC


def main():
    try:
        if stale(META) or stale(REPORT):
            subprocess.run([sys.executable, str(EXTRACT)], capture_output=True, timeout=60)
            subprocess.run([sys.executable, str(LINT), "--fail-on=never"], capture_output=True, timeout=60)
        if not META.exists():
            print("[skill-quality-gate] meta file missing — run extract_skill_meta.py")
            return 0

        diag = json.loads(META.read_text(encoding="utf-8")).get("diagnostics", {})
        critical = diag.get("named_only_desc", 0) + diag.get("empty_desc", 0) + diag.get("broken_frontmatter", 0)
        total = diag.get("with_skill_md", 0)

        if critical > 0:
            print(f"[skill-quality-gate] WARN: {critical} skills have critical issues (empty/named-only/broken frontmatter). Run: python scripts/lint_skills.py")
        else:
            print(f"[skill-quality-gate] OK: {total} skills loaded; no critical issues. {diag.get('without_skill_md', 0)} folders without SKILL.md.")
    except Exception as e:
        print(f"[skill-quality-gate] hook error: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
