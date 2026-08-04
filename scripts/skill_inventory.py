import json, os, re

ROOTS = [
    (r"C:\Users\user\.claude\skills", "claude", False),
    (r"C:\Users\user\.agents\skills", "agents", False),
    (r"C:\Users\user\.claude\skills-archive", "archive", True),
]

def parse(path):
    try:
        t = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return None
    fm, body = {}, t
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if m:
        body = t[m.end():]
        for line in m.group(1).split("\n"):
            k = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
            if k:
                fm[k.group(1).lower()] = k.group(2).strip().strip('"\'')
    h = next((l.lstrip("# ").strip() for l in body.split("\n") if l.startswith("#")), "")
    return fm, h, len(t)

out, seen = [], {}
for root, tag, archived in ROOTS:
    if not os.path.isdir(root):
        continue
    for name in sorted(os.listdir(root)):
        f = os.path.join(root, name, "SKILL.md")
        if not os.path.isfile(f):
            continue
        p = parse(f)
        if not p:
            continue
        fm, h, size = p
        rec = {
            "slug": fm.get("name", name),
            "dir": name,
            "root": tag,
            "archived": archived,
            "description": fm.get("description", "")[:400],
            "when_to_use": (fm.get("when_to_use") or fm.get("whentouse") or "")[:300],
            "h1": h[:120],
            "bytes": size,
        }
        prev = seen.get(name)
        if prev is None:
            seen[name] = rec
            out.append(rec)
        else:
            # same skill dir in >1 root: keep the richest copy, note where else it lives
            prev.setdefault("also_in", []).append(tag)
            if size > prev["bytes"]:
                prev.update({k: rec[k] for k in ("description", "when_to_use", "h1", "bytes")})
                prev["root"] = tag
            if not archived:
                prev["archived"] = False

p = r"C:\Users\user\.claude\skill_inventory.json"
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
by_root = {}
for r in out:
    by_root[r["root"]] = by_root.get(r["root"], 0) + 1
print(f"{len(out)} unique skills -> {p}")
print("  primary root:", by_root)
print("  archived-only:", sum(1 for r in out if r["archived"]))
