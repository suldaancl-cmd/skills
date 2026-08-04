"""Weekly digest of skill-library health for the Obsidian vault.

Runs the extractor + linter + usage-stats and writes one summary report to
~/.claude/projects/C--Users-user--claude-skills/memory/Reports/skills_weekly_<YYYY-WW>.md.

Designed to run as a vmi cron Sunday 09:00. The vault sync via LiveSync will
propagate it back to Windows automatically.

Usage:
    python scripts/weekly_skill_digest.py
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

CLAUDE = Path(r"C:\Users\user\.claude") if Path(r"C:\Users\user\.claude").exists() else Path("/root/.claude")
SCRIPTS = CLAUDE / "scripts"
META = CLAUDE / "tmp" / "skills_meta.json"
LINT_REPORT = CLAUDE / "tmp" / "skill_lint_report.md"
USAGE_DIR = CLAUDE / "projects" / "C--Users-user--claude-skills" / "memory" / "Sessions"
REPORTS_DIR = CLAUDE / "projects" / "C--Users-user--claude-skills" / "memory" / "Reports"


def run(cmd: list[str]):
    print(f"$ {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode not in (0, 1, 2):
        print(f"  FAIL ({r.returncode}): {r.stderr}", file=sys.stderr)
    if r.stdout:
        print(r.stdout.rstrip())
    return r


def main():
    today = dt.date.today()
    yyyy_ww = today.strftime("%G-W%V")  # ISO week

    # 1. extract
    run([sys.executable, str(SCRIPTS / "extract_skill_meta.py")])
    # 2. lint
    run([sys.executable, str(SCRIPTS / "lint_skills.py"), "--fail-on=never"])
    # 3. usage
    run([sys.executable, str(SCRIPTS / "skill_usage_stats.py")])

    # Synthesize digest
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"skills_weekly_{yyyy_ww}.md"

    diag = json.loads(META.read_text(encoding="utf-8"))["diagnostics"]
    lint_text = LINT_REPORT.read_text(encoding="utf-8") if LINT_REPORT.exists() else "(lint report missing)"
    usage_files = sorted(USAGE_DIR.glob("SKILL_USAGE_*.md"), reverse=True)
    latest_usage = usage_files[0].name if usage_files else "(none)"

    body = [
        "---",
        f"name: Skills weekly digest — {yyyy_ww}",
        f"description: Auto-generated weekly snapshot of skill-library health.",
        "type: digest",
        f"date: {today.isoformat()}",
        f"week: {yyyy_ww}",
        "---",
        "",
        f"# Skills weekly digest — {yyyy_ww}",
        "",
        "## Counts",
        "",
        f"- Skill folders scanned: **{diag['total_folders']}**",
        f"- With SKILL.md: **{diag['with_skill_md']}**",
        f"- Without SKILL.md (cleanup candidates): **{diag['without_skill_md']}**",
        f"- Multiline-description skills: **{diag.get('multiline_desc_count', 0)}**",
        f"- Empty descriptions: **{diag.get('empty_desc', 0)}**",
        f"- Named-only descriptions: **{diag.get('named_only_desc', 0)}**",
        f"- Broken frontmatter: **{diag.get('broken_frontmatter', 0)}**",
        "",
        "## Lint findings",
        "",
        lint_text,
        "",
        f"## Latest usage stats",
        "",
        f"See `[[Sessions/{latest_usage}]]` for the rank table.",
        "",
    ]
    out.write_text("\n".join(body), encoding="utf-8")
    print(f"\nwrote digest: {out}")


if __name__ == "__main__":
    main()
