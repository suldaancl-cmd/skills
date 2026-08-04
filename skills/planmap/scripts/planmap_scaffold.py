"""Scaffold a planmap workspace.

Wraps ~/.claude/scripts/topic_workspace.py (which already writes README/CLAUDE/AGENTS/
BRAIN/SKILLS/TOOLS/NOTES + sources/) and adds the planmap-specific files.

Usage:
  python planmap_scaffold.py --project "Zefaf B2B platform" [--slug zefaf-b2b]
                             [--prompt "<Karim's exact message>"]

Never overwrites. Prints the workspace path and the fill-in checklist.
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
TEMPLATES = os.path.join(SKILL, "templates")
CLAUDE = os.path.join(os.path.expanduser("~"), ".claude")
WORKSPACE = os.path.join(CLAUDE, "scripts", "topic_workspace.py")

# (template file, destination name)
FILES = [
    ("PLANMAP.template.md", "PLANMAP.md"),
    ("MANUAL-SETUP.template.md", "MANUAL-SETUP.md"),
]

CODEX = """# {slug} — Codex / ChatGPT entry point

Same workspace, different runner. Read these in order before producing anything:

1. `BRAIN.md` — matching second-brain files. Outranks your general knowledge.
2. `SKILLS.md` — the ranked skill chain for this topic.
3. `CLAUDE.md` — purpose and the hard rules in force.
4. `PLANMAP.md` — the plan you are filling in.
5. `MANUAL-SETUP.md` — the human-only list you are counting.

The full workflow lives in `~/.claude/skills/planmap/SKILL.md`. If you cannot read that path,
use `~/.claude/skills/planmap/portable/PROMPT.md`, which is the same workflow inlined.

Gates that bind you here (they are not inherited automatically):
G1 KNOW — the brain first. G2 THINK — simplest thing that works, state assumptions.
G3 ACT — work inside this folder, MERGE never replace, confirm destructive ops.
G4 VERIFY — point to the artifact that proves each claim; unproven means say "unverified".
G5 LEARN — append findings to `NOTES.md`.
"""


def run_topic_workspace(topic, slug, prompt):
    if not os.path.isfile(WORKSPACE):
        sys.exit(f"missing {WORKSPACE} — planmap reuses it, it is not optional")
    cmd = [sys.executable, WORKSPACE, "--topic", topic, "--kind", "build"]
    if slug:
        cmd += ["--slug", slug]
    if prompt:
        cmd += ["--prompt", prompt]
    # topic_workspace picks _projects relative to cwd unless cwd is under ~/.claude
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=CLAUDE)
    if res.returncode != 0:
        sys.exit(f"topic_workspace failed:\n{res.stderr or res.stdout}")
    out = res.stdout.strip().splitlines()
    return out[0], "\n".join(out[1:])


def write(path, text):
    if os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True, help="project name / one-line description")
    ap.add_argument("--slug")
    ap.add_argument("--prompt", default="")
    a = ap.parse_args()

    slug = a.slug or re.sub(r"[^a-z0-9]+", "-", a.project.lower()).strip("-")[:48]
    root, stats = run_topic_workspace(a.project, slug, a.prompt)
    today = date.today().isoformat()

    created, skipped = [], []
    for src, dst in FILES:
        srcp = os.path.join(TEMPLATES, src)
        if not os.path.isfile(srcp):
            sys.exit(f"missing template {srcp}")
        with open(srcp, encoding="utf-8") as fh:
            body = fh.read()
        body = body.replace("{{PROJECT}}", a.project).replace("{{SLUG}}", slug).replace("{{DATE}}", today)
        (created if write(os.path.join(root, dst), body) else skipped).append(dst)

    (created if write(os.path.join(root, "codex.md"), CODEX.format(slug=slug)) else skipped).append("codex.md")

    for sub in ("refs/mobbin", "figma"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)

    print(root)
    print(stats)
    print(f"created: {', '.join(created) or 'none'}")
    if skipped:
        print(f"kept existing: {', '.join(skipped)}")
    # ASCII only: the Windows console is cp1252 and mangles em dashes in stdout.
    print("""
NEXT (the script only scaffolds - you fill these in):
  1. read BRAIN.md and SKILLS.md
  2. INTERVIEW Karim - batches of 3-6 multiple-choice questions, one topic per batch,
     one option marked (recommended). Keep going until a batch yields no new decision.
     Mandatory: "what does V1 done mean?" and "what is explicitly OUT of V1?"
     Question bank: skills/planmap/references/interview-questions.md
  3. hand him MANUAL-SETUP.md early, as soon as the stack is decided - he sets up
     accounts and keys while you keep interviewing
  4. fill PLANMAP.md   - sitemap, backend, AI layer, integrations, task list
  5. Mobbin refs -> refs/mobbin/   |   FigJam diagrams -> figma/
  6. finalise MANUAL-SETUP.md with real counts + the launch gate
  7. merge templates/AGENTS.template.md into AGENTS.md
  8. export PLANMAP.md to Google Docs, log decisions to NOTES.md""")


if __name__ == "__main__":
    main()
