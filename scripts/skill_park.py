"""Park skills out of the listing without deleting them.

  python ~/.claude/scripts/skill_park.py --plan            # show what would move, change nothing
  python ~/.claude/scripts/skill_park.py --apply           # move into _skills-coldstore/
  python ~/.claude/scripts/skill_park.py --restore NAME    # bring one back

_skills-coldstore/ sits outside every SKILL_ROOT, so parked skills leave Claude's
prompt listing AND skill_find.py, but the bytes stay on disk and in the manifest.
Nothing is ever deleted.
"""
import argparse
import datetime
import json
import os
import re
import shutil

CLAUDE = os.path.expanduser(r"~/.claude")
SKILLS = os.path.join(CLAUDE, "skills")
COLD = os.path.join(CLAUDE, "_skills-coldstore")
MANIFEST = os.path.join(COLD, "MANIFEST.json")

# Bulk families Karim does not work in — verified against skill-usage.jsonl (0 uses each).
FAMILIES = ["jdp-", "antd-", "design-md-"]


def listable():
    return [d for d in os.listdir(SKILLS)
            if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md"))]


def alias_pairs(names):
    """(alias, canonical) for the od- / -od import duplicates only."""
    have = set(names)
    pairs = []
    for n in names:
        canon = None
        if n.startswith("od-"):
            canon = n[3:]
        elif n.endswith("-od"):
            canon = n[:-3]
        if canon and canon in have:
            pairs.append((n, canon))
    return pairs


def plan():
    names = listable()
    fam = sorted(n for n in names if any(n.startswith(p) for p in FAMILIES))
    pairs = alias_pairs(names)
    aliases = sorted(a for a, _c in pairs)
    return fam, pairs, sorted(set(fam) | set(aliases))


def apply(targets, reason_of):
    os.makedirs(COLD, exist_ok=True)
    man = {"parked": {}}
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as fh:
            man = json.load(fh)
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    moved = []
    for n in targets:
        src, dst = os.path.join(SKILLS, n), os.path.join(COLD, n)
        if not os.path.isdir(src) or os.path.exists(dst):
            continue
        shutil.move(src, dst)
        man["parked"][n] = {"parked_at": stamp, "from": "skills/", "reason": reason_of[n]}
        moved.append(n)
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=1, sort_keys=True)
    return moved


def restore(name):
    src, dst = os.path.join(COLD, name), os.path.join(SKILLS, name)
    if not os.path.isdir(src):
        return f"not parked: {name}"
    if os.path.exists(dst):
        return f"already present in skills/: {name}"
    shutil.move(src, dst)
    with open(MANIFEST, encoding="utf-8") as fh:
        man = json.load(fh)
    man["parked"].pop(name, None)
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=1, sort_keys=True)
    return f"restored: {name}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--restore")
    a = ap.parse_args()

    if a.restore:
        print(restore(a.restore))
        return 0

    fam, pairs, targets = plan()
    reason = {n: f"bulk family {next(p for p in FAMILIES if n.startswith(p))}*" for n in fam}
    for alias, canon in pairs:
        reason[alias] = f"duplicate of {canon}"

    print(f"bulk-family skills : {len(fam)}")
    for p in FAMILIES:
        print(f"    {p}* : {sum(1 for n in fam if n.startswith(p))}")
    print(f"import duplicates  : {len(pairs)}")
    for alias, canon in pairs[:6]:
        print(f"    {alias}  ->  keeping {canon}")
    if len(pairs) > 6:
        print(f"    ... and {len(pairs) - 6} more")
    print(f"TOTAL to park      : {len(targets)}")

    if a.apply:
        moved = apply(targets, reason)
        print(f"\nparked {len(moved)} skills into _skills-coldstore/")
        print(f"manifest: {MANIFEST}")
        print("restore any with: python scripts/skill_park.py --restore <name>")
    else:
        print("\n(plan only — rerun with --apply to move)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
