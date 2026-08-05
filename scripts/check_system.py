"""Health check for the intake stack: generator, router, stop hook, second brain.

Run: python ~/.claude/scripts/check_system.py
Exits 1 if anything fails, so it can gate a cron/maintenance run.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

CLAUDE = r"C:/Users/user/.claude"
VAULT = os.path.join(CLAUDE, "projects", "C--Users-user--claude-skills", "memory")
SLUG = "_healthcheck"
WS = os.path.join(CLAUDE, "_projects", SLUG)
TOPIC = "scrape competitor websites and research their pricing"
WANT = ["AGENTS.md", "BRAIN.md", "CLAUDE.md", "NOTES.md", "README.md",
        "SKILLS.md", "TOOLS.md", "sources"]
results = []


def check(name, passed, detail=""):
    results.append((bool(passed), name, str(detail)))


def load_consts(path, cut):
    """Exec the header of a script to read its resolved constants."""
    src = open(path, encoding="utf-8").read().split(cut)[0]
    ns = {}
    exec(compile(src, path, "exec"), ns)
    return ns


def main():
    os.chdir(CLAUDE)

    for f in ("scripts/topic_workspace.py", "scripts/build_second_brain.py",
              "hooks/skill-router.py", "hooks/skill-stop-check.py",
              "skills/session-intake/SKILL.md", "skill-routes.json"):
        check(f"exists: {f}", os.path.exists(f))

    # generator — run twice, must be identical and complete
    runs = []
    for _ in range(2):
        shutil.rmtree(WS, ignore_errors=True)
        runs.append(subprocess.run(
            [sys.executable, "scripts/topic_workspace.py", "--topic", TOPIC,
             "--slug", SLUG, "--kind", "study"],
            capture_output=True, text=True).stdout)
    check("generator deterministic", runs[0] == runs[1], runs[0].strip().split("\n")[-1][:64])
    got = sorted(os.listdir(WS)) if os.path.isdir(WS) else []
    check("workspace emits 8 artifacts", got == WANT, got)
    for f in ("BRAIN.md", "SKILLS.md", "TOOLS.md"):
        p = os.path.join(WS, f)
        n = len(open(p, encoding="utf-8").read()) if os.path.exists(p) else 0
        check(f"{f} non-empty", n > 200, f"{n} chars")
    ag = os.path.join(WS, "AGENTS.md")
    g0 = next((l for l in open(ag, encoding="utf-8") if l.startswith("G0 ROUTE")), "")
    check("dispatch block carries G0 chain", "firecrawl" in g0, g0.strip()[:80])

    # router
    out = subprocess.run([sys.executable, "hooks/skill-router.py"],
                         input='{"prompt":"build me a landing page for a saas"}',
                         capture_output=True, text=True).stdout
    ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    check("router injects intake + domain",
          "INTAKE" in ctx and "BRAIN.md" in ctx and "web-design" in ctx)
    check("router advertises long tail", "skill_find.py" in ctx and "skill-swarm" in ctx)

    # escalation must fire by rule, not by judgment
    def esc(prompt):
        o = subprocess.run([sys.executable, "hooks/skill-router.py"],
                           input=json.dumps({"prompt": prompt}), capture_output=True, text=True).stdout
        c = json.loads(o)["hookSpecificOutput"]["additionalContext"]
        return next((l for l in c.splitlines() if l.startswith("ESCALATE")), "")
    check("escalate: explicit 'all skills'", "skill-swarm" in esc("use all the skills for this build"))
    check("escalate: unmatched substantial work",
          "skill_find.py" in esc("explain how the annealing scheduler in this repo picks priority"))
    check("no escalate: short follow-up", not esc("give me the link"))
    check("no escalate: normal match", not esc("build me a landing page for a saas product"))

    # stop hook — the exemption matrix
    def verdict(blocks):
        fd, path = tempfile.mkstemp(suffix=".jsonl")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"type": "user",
                                 "message": {"content": "please do the substantive thing now"}}) + "\n")
            fh.write(json.dumps({"type": "assistant", "message": {"content": blocks}}) + "\n")
        o = subprocess.run([sys.executable, "hooks/skill-stop-check.py"],
                           input=json.dumps({"transcript_path": path, "session_id": "healthcheck"}),
                           capture_output=True, text=True).stdout
        os.unlink(path)
        return "BLOCK" if '"block"' in o else "allow"

    tool = lambda n: {"type": "tool_use", "name": n, "input": {}}
    long_text = {"type": "text", "text": "x" * 400}
    matrix = [
        ("2 tools + long text", [tool("Bash"), tool("Edit"), long_text], "allow"),
        ("no tools + long text", [long_text], "BLOCK"),
        ("Skill invoked", [{"type": "tool_use", "name": "Skill", "input": {"skill": "x"}}, long_text], "allow"),
        # one grounded command + an answer citing it is legitimate work, not recall
        ("1 tool + long text", [tool("Bash"), long_text], "allow"),
        ("no tools + short text", [{"type": "text", "text": "done"}], "allow"),
    ]
    for label, blocks, want in matrix:
        check(f"stop hook: {label}", verdict(blocks) == want, want)

    # second brain — resolved roots, not a text grep (the bug in the last run's assertion)
    roots = load_consts(os.path.join(CLAUDE, "scripts/build_second_brain.py"), "# ---------- 1. SKILLS")["SKILL_ROOTS"]
    check("brain scans all skill roots", len(roots) >= 3 and all(os.path.isdir(r) for r in roots),
          f"{len(roots)} roots, {sum(os.path.isdir(r) for r in roots)} exist")
    cat = os.path.join(VAULT, "Brain", "Skills", "CATALOG.md")
    check("brain catalog current", os.path.exists(cat) and "firecrawl" in open(cat, encoding="utf-8").read())

    cm = open(os.path.join(CLAUDE, "CLAUDE.md"), encoding="utf-8").read()
    check("CLAUDE.md wired", all(x in cm for x in ("Chat intake", "BRAIN.md", "topic_workspace.py")))

    # drift: routing table names that no longer exist on disk
    spec = importlib.util.spec_from_file_location("tw", os.path.join(CLAUDE, "scripts/topic_workspace.py"))
    tw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tw)
    lib = tw.load_skills()
    table = json.load(open(os.path.join(CLAUDE, "skill-routes.json"), encoding="utf-8"))
    # Namespaced skills (`plugin:name`) and command skills have no folder on disk but are
    # still invocable — only unqualified names missing from every skill root are real drift.
    virtual = {"vmi"}
    drift = sorted({s for d in table["domains"] for s in d.get("skills", [])
                    if s not in lib and ":" not in s and s not in virtual})
    check("routing table has no drift", not drift, drift or f"{len(lib)} skills on disk")

    shutil.rmtree(WS, ignore_errors=True)

    for passed, name, detail in results:
        print(f"{'PASS' if passed else 'FAIL'}  {name:38} {detail}")
    bad = [n for p, n, _ in results if not p]
    print(f"\n{len(results) - len(bad)}/{len(results)} passed" + (f" — FAILING: {bad}" if bad else " — ALL PASS"))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
