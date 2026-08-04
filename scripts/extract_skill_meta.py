"""Extract metadata for every skill folder under SKILLS_DIR.

Handles YAML pipe (`|`) and folded (`>`) multiline scalars correctly — that's
the bug that caused the false-positive "stub" deletions on 2026-05-03.

Usage:
    python scripts/extract_skill_meta.py [--root <dir>] [--out <json>]

Output: JSON with shape {"skills": [...], "no_skill_md": [...], "diagnostics": {...}}
Each skill record has dir, name, desc, fm_ok, has_triggers, size, multiline_desc.
"""
import argparse, json, re, sys
from pathlib import Path

DEFAULT_ROOT = Path(r"C:\Users\user\.claude\skills")
DEFAULT_OUT = Path(r"C:\Users\user\.claude\tmp\skills_meta.json")


def parse_frontmatter(text: str) -> tuple[dict, bool]:
    """Return (parsed_fields, has_frontmatter). Hand-rolled YAML — covers:
       - simple `key: value`
       - quoted `key: "value"` / `key: 'value'`
       - pipe block `key: |` (literal — newlines kept)
       - folded block `key: >` (folded — newlines become spaces).
    """
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}, False

    body = m.group(1)
    lines = body.splitlines()
    out = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        km = re.match(r"^([A-Za-z][\w-]*)\s*:\s*(.*)$", line)
        if not km:
            i += 1
            continue
        key, val = km.group(1).lower(), km.group(2).rstrip()
        if val in ("|", ">", "|-", ">-", "|+", ">+"):
            # multiline scalar — collect indented lines that follow
            scalar_style = val[0]
            collected = []
            i += 1
            base_indent = None
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    collected.append("")
                    i += 1
                    continue
                indent = len(nxt) - len(nxt.lstrip())
                if base_indent is None:
                    if indent == 0:
                        break
                    base_indent = indent
                if indent < base_indent:
                    break
                collected.append(nxt[base_indent:])
                i += 1
            joined = "\n".join(collected).rstrip()
            if scalar_style == ">":
                # folded: collapse internal single newlines into spaces
                joined = re.sub(r"(?<!\n)\n(?!\n)", " ", joined)
                joined = re.sub(r"\n\n+", "\n", joined)
            out[key] = joined
        else:
            # strip surrounding quotes if matched pair
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            out[key] = val
            i += 1
    return out, True


def extract_one(skill_dir: Path) -> dict | None:
    sk = skill_dir / "SKILL.md"
    if not sk.exists():
        return None
    try:
        text = sk.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {"dir": skill_dir.name, "name": skill_dir.name, "desc": "(read error)",
                "fm_ok": False, "has_triggers": False, "size": 0, "multiline_desc": False}
    fm, fm_ok = parse_frontmatter(text)
    name = fm.get("name") or skill_dir.name
    desc = fm.get("description") or ""
    multiline = "\n" in desc
    desc_one = desc.replace("\n", " ").strip()
    if not desc_one:
        # fallback to first non-heading paragraph in body
        body = re.sub(r"^---.*?---\n?", "", text, count=1, flags=re.S)
        for line in body.splitlines():
            line = line.strip()
            if line and not line.startswith(("#", "<!--", "```")):
                desc_one = line[:300]
                break
    return {
        "dir": skill_dir.name,
        "name": name,
        "desc": desc_one[:500],
        "fm_ok": fm_ok,
        "has_triggers": bool(fm.get("triggers")),
        "size": sk.stat().st_size,
        "multiline_desc": multiline,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    skills = []
    no_skill_md = []
    for d in sorted(args.root.iterdir()):
        if not d.is_dir():
            continue
        rec = extract_one(d)
        if rec is None:
            no_skill_md.append(d.name)
        else:
            skills.append(rec)

    diag = {
        "total_folders": len(skills) + len(no_skill_md),
        "with_skill_md": len(skills),
        "without_skill_md": len(no_skill_md),
        "named_only_desc": sum(1 for s in skills if s["desc"].lower().strip(' "\'') == s["name"].lower()),
        "empty_desc": sum(1 for s in skills if not s["desc"]),
        "broken_frontmatter": sum(1 for s in skills if not s["fm_ok"]),
        "multiline_desc_count": sum(1 for s in skills if s["multiline_desc"]),
        "missing_triggers": sum(1 for s in skills if not s["has_triggers"]),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps({"skills": skills, "no_skill_md": no_skill_md, "diagnostics": diag}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"wrote {args.out}")
    for k, v in diag.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
