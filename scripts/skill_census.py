"""Single source of truth for how many skills exist — generated, never typed.

  python ~/.claude/scripts/skill_census.py            # count, diff vs last run, write census
  python ~/.claude/scripts/skill_census.py --sync-docs # also rewrite the marker blocks in the docs
  python ~/.claude/scripts/skill_census.py --quiet     # one line, for the SessionStart hook

Writes skill-census.json (current counts + the full name list) and appends every
change to skill-census-log.jsonl, so "what did we add today" is answerable.

Reuses topic_workspace.load_skills() so this never disagrees with skill_find.py.
"""
import argparse
import datetime
import importlib.util
import json
import os
import re

CLAUDE = os.path.expanduser(r"~/.claude")
CENSUS = os.path.join(CLAUDE, "skill-census.json")
LOG = os.path.join(CLAUDE, "skill-census-log.jsonl")
COLD = os.path.join(CLAUDE, "_skills-coldstore")

START, END = "<!-- SKILL-CENSUS:START -->", "<!-- SKILL-CENSUS:END -->"


def _load_tw():
    path = os.path.join(CLAUDE, "scripts", "topic_workspace.py")
    spec = importlib.util.spec_from_file_location("topic_workspace", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _subdirs(root):
    if not os.path.isdir(root):
        return [], []
    dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    ok = [d for d in dirs if os.path.isfile(os.path.join(root, d, "SKILL.md"))]
    return ok, [d for d in dirs if d not in ok]


def measure():
    tw = _load_tw()
    listable, broken = _subdirs(os.path.join(CLAUDE, "skills"))
    cold, _ = _subdirs(COLD)
    searchable = tw.load_skills()
    return {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "listable": len(listable),          # what Claude Code puts in the system prompt
        "searchable": len(searchable),      # what skill_find.py / the router can reach
        "coldstore": len(cold),             # parked, restorable, not listed
        "broken": len(broken),              # dirs under skills/ with no SKILL.md
        "broken_names": sorted(broken),
        "names": sorted(listable),
        "cold_names": sorted(cold),
    }


def diff(now, prev):
    if not prev:
        return [], []
    a, b = set(prev.get("names", [])), set(now["names"])
    return sorted(b - a), sorted(a - b)


def sync_docs(now, added, removed):
    """Rewrite the census block in every doc that quotes a skill count."""
    lines = [
        START,
        f"**Skill library (generated {now['generated'][:10]} by "
        f"`scripts/skill_census.py` — do not hand-edit these numbers):** "
        f"**{now['listable']}** skills listed to Claude · **{now['searchable']}** reachable via "
        f"`skill_find.py` · **{now['coldstore']}** parked in `_skills-coldstore/` (restorable) · "
        f"**{now['broken']}** dirs without a `SKILL.md`.",
    ]
    # Karim asked to see what changed, not just the total. Cap the list so a bulk
    # install can't push the whole library into every doc.
    if added:
        shown = ", ".join(f"`{n}`" for n in added[:12])
        more = f" (+{len(added) - 12} more)" if len(added) > 12 else ""
        lines.append(f"**Added since the last census ({len(added)}):** {shown}{more}")
    if removed:
        lines.append(f"**Removed/parked since the last census:** {len(removed)}")
    lines.append(END)
    block = "\n".join(lines)
    touched = []
    for rel in ["CLAUDE.md",
                "projects/C--Users-user--claude-skills/memory/MEMORY.md",
                "SKILL_ROUTER.md"]:
        p = os.path.join(CLAUDE, rel)
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        if START in text:
            new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
        else:
            continue  # marker must be placed once by hand; never guess an insertion point
        if new != text:
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(new)
            touched.append(rel)
    return touched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync-docs", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    prev = None
    if os.path.isfile(CENSUS):
        try:
            with open(CENSUS, encoding="utf-8") as fh:
                prev = json.load(fh)
        except (OSError, ValueError):
            prev = None

    now = measure()
    added, removed = diff(now, prev)

    with open(CENSUS, "w", encoding="utf-8") as fh:
        json.dump(now, fh, indent=1)
    if added or removed or prev is None:
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": now["generated"], "listable": now["listable"],
                                 "added": added, "removed": removed}) + "\n")

    touched = sync_docs(now, added, removed) if a.sync_docs else []

    if a.quiet:
        delta = ""
        if added or removed:
            delta = f" | today: +{len(added)} -{len(removed)}"
        # ASCII only: the Windows console is cp1252 and mangles typographic separators.
        print(f"[skills] {now['listable']} listed | {now['searchable']} searchable | "
              f"{now['coldstore']} parked | {now['broken']} broken{delta}")
        return 0

    print(f"listable (in Claude's prompt) : {now['listable']}")
    print(f"searchable (skill_find.py)    : {now['searchable']}")
    print(f"parked in _skills-coldstore   : {now['coldstore']}")
    print(f"dirs without SKILL.md         : {now['broken']}  {now['broken_names']}")
    if prev is None:
        print("\nbaseline established — future runs will report added/removed")
    else:
        print(f"\nsince last census ({prev['generated'][:16]}):")
        print(f"  added   ({len(added)}): {', '.join(added) or '-'}")
        print(f"  removed ({len(removed)}): {', '.join(removed) or '-'}")
    if touched:
        print("\ndocs updated:", ", ".join(touched))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
