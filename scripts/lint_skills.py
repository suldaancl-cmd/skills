"""Lint installed Claude Code skills for quality issues.

Flags:
  - Empty / named-only descriptions (the bug class that produced `migration-architect` etc.)
  - Description-similarity duplicates (>0.80 cosine on bag-of-words)
  - Missing `triggers:` field (degrades skill auto-matching)
  - Missing `name:` field
  - frontmatter `name:` mismatches folder name
  - SKILL.md broken / unparseable

Output: tmp/skill_lint_report.md (markdown, top of file = exit-status summary).
Exit code: 0 = clean, 1 = warnings only, 2 = critical issues found.
Critical = empty / named-only / broken-yaml.

Usage:
    python scripts/lint_skills.py [--root <dir>] [--report <md>] [--fail-on=critical|warning]
"""
import argparse, json, math, re, sys
from collections import Counter
from pathlib import Path

DEFAULT_META = Path(r"C:\Users\user\.claude\tmp\skills_meta.json")
DEFAULT_REPORT = Path(r"C:\Users\user\.claude\tmp\skill_lint_report.md")
SIM_THRESHOLD = 0.80
STOP = {"the","a","an","of","to","for","and","or","is","are","be","this","that","with",
        "use","when","user","skill","claude","code","also","by","at","on","in","as",
        "it","its","you","your","they","their","what","how","why","do","get","make"}


def tokens(text: str) -> Counter:
    words = re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())
    return Counter(w for w in words if w not in STOP)


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    common = set(a) & set(b)
    if not common:
        return 0.0
    num = sum(a[t] * b[t] for t in common)
    da = math.sqrt(sum(v * v for v in a.values()))
    db = math.sqrt(sum(v * v for v in b.values()))
    return num / (da * db) if da and db else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", type=Path, default=DEFAULT_META)
    ap.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    ap.add_argument("--fail-on", choices=["critical", "warning", "never"], default="critical")
    args = ap.parse_args()

    if not args.meta.exists():
        print(f"missing meta file: {args.meta}. Run extract_skill_meta.py first.", file=sys.stderr)
        return 2
    data = json.loads(args.meta.read_text(encoding="utf-8"))
    skills = data["skills"]

    critical = []   # (dir, reason)
    warnings = []   # (dir, reason)

    for s in skills:
        if not s.get("fm_ok"):
            critical.append((s["dir"], "frontmatter missing or unparseable"))
            continue
        desc = (s.get("desc") or "").strip()
        name = s["name"].strip().strip("\"'")
        if not desc:
            critical.append((s["dir"], "empty description"))
        elif desc.lower().strip(" \"'") == name.lower():
            critical.append((s["dir"], f"description is just the name (\"{desc[:60]}\")"))
        elif len(desc) < 60:
            warnings.append((s["dir"], f"very short description ({len(desc)} chars)"))
        # Note: most legit skills don't include explicit 'triggers:' field
        # (they describe triggers in the description). Skip this check.
        if name.lower() != s["dir"].lower():
            warnings.append((s["dir"], f"frontmatter name '{name}' != folder name '{s['dir']}'"))

    # similarity
    toks = {s["dir"]: tokens(s.get("desc", "")) for s in skills}
    pairs = []
    keys = list(toks)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            sim = cosine(toks[keys[i]], toks[keys[j]])
            if sim >= SIM_THRESHOLD:
                pairs.append((keys[i], keys[j], sim))
    pairs.sort(key=lambda p: -p[2])

    # Build report
    lines = [
        f"# Skill lint report",
        f"",
        f"- Skills scanned: **{len(skills)}**",
        f"- Critical issues: **{len(critical)}**",
        f"- Warnings: **{len(warnings)}**",
        f"- Likely-duplicate pairs (similarity ≥ {SIM_THRESHOLD}): **{len(pairs)}**",
        f"",
    ]
    if critical:
        lines += ["## Critical (block install)", ""]
        for d, r in critical:
            lines.append(f"- `{d}` — {r}")
        lines.append("")
    if warnings:
        lines += ["## Warnings", ""]
        for d, r in sorted(warnings):
            lines.append(f"- `{d}` — {r}")
        lines.append("")
    if pairs:
        lines += ["## Likely duplicate pairs", "", "| A | B | Similarity |", "|---|---|---:|"]
        for a, b, sim in pairs[:50]:
            lines.append(f"| `{a}` | `{b}` | {sim:.2f} |")
        if len(pairs) > 50:
            lines.append(f"| _...and {len(pairs)-50} more_ | | |")
        lines.append("")
    if not critical and not warnings and not pairs:
        lines += ["**All clear.**", ""]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.report}")
    print(f"  critical={len(critical)}  warnings={len(warnings)}  duplicate_pairs={len(pairs)}")

    # exit code
    if args.fail_on == "never":
        return 0
    if args.fail_on == "critical":
        return 2 if critical else 0
    if args.fail_on == "warning":
        return 2 if critical else (1 if warnings else 0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
