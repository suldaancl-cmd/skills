#!/usr/bin/env python3
"""Build a portable skill index that works on ANY Claude surface.

Claude Code reads ~/.claude/skills directly. claude.ai chat and Cowork cannot --
they only see skills uploaded to the account. This builds ONE small skill whose
body is a catalogue of the whole library, using progressive disclosure so the
always-on cost stays tiny and the per-domain detail loads only when needed.

Re-run it whenever skills change:
    python ~/.claude/scripts/build_portable_index.py

Output: _projects/skills-marketplace/portable/karim-skill-index/
        plus karim-skill-index.zip ready to upload.
"""
import json
import os
import re
import sys
import zipfile

HOME = os.path.expanduser("~")
CLAUDE = os.path.join(HOME, ".claude")
sys.path.insert(0, os.path.join(CLAUDE, "scripts"))
import topic_workspace as tw  # noqa: E402

OUT = os.path.join(CLAUDE, "_projects", "skills-marketplace", "portable",
                   "karim-skill-index")
REPO = "https://raw.githubusercontent.com/suldaancl-cmd/skills/main"

# Roots whose skills are committed to the public repo, so any surface can fetch
# the body over https. Anything else is local-only and marked as such.
FETCHABLE = {"": "skills", "extra": "skills-extra", "archived": "skills-archive"}


def load_rows():
    """(name, description, label) for every skill on disk, plus plugin skills."""
    rows = [(n, (d or ""), lb) for n, (d, lb) in tw.load_skills().items()]
    import glob
    seen = set()
    pats = ["plugins/marketplaces/*/plugins/*/skills/*/SKILL.md",
            "plugins/marketplaces/*/skills/*/SKILL.md",
            "skills-extra/*/plugins/*/skills/*/SKILL.md"]
    for pat in pats:
        for p in glob.glob(os.path.join(CLAUDE, pat)):
            parts = p.replace(os.sep, "/").split("/")
            mkt = parts[parts.index("marketplaces") + 1] if "marketplaces" in parts else parts[-5]
            if mkt.startswith("temp_"):
                continue
            name = parts[-2]
            if (mkt, name) in seen:
                continue
            seen.add((mkt, name))
            try:
                head = open(p, encoding="utf-8", errors="ignore").read(2500)
            except OSError:
                continue
            rows.append((name, tw.parse_description(head), "plugin:" + mkt))
    return rows


def assign_domains(rows, domains):
    """Best-matching routing domain per skill, by keyword overlap."""
    kw = [(d["name"], set(w.lower() for w in d.get("keywords", []))) for d in domains]
    out = {}
    for name, desc, label in rows:
        text = set(re.findall(r"[a-z0-9]{3,}", (name + " " + desc).lower()))
        best, score = "other", 0
        for dname, words in kw:
            s = len(text & words)
            if s > score:
                best, score = dname, s
        out.setdefault(best, []).append((name, desc, label))
    return out


def fetch_hint(label, name):
    if label in FETCHABLE:
        return "%s/%s/%s/SKILL.md" % (REPO, FETCHABLE[label], name)
    return ""


def main():
    refs = os.path.join(OUT, "references")
    os.makedirs(refs, exist_ok=True)
    # Clear our own previous output. Chunk names shift as the library grows, so
    # stale files would otherwise linger and be indexed as if current.
    for stale in os.listdir(refs):
        if stale.endswith(".md"):
            os.remove(os.path.join(refs, stale))
    routes = json.load(open(os.path.join(CLAUDE, "skill-routes.json"), encoding="utf-8"))
    rows = load_rows()
    buckets = assign_domains(rows, routes["domains"])

    # Per-domain reference files -- loaded only when that domain is in play.
    # A domain wider than CHUNK is split alphabetically; one 650-entry file
    # would cost more to load than the whole point of splitting by domain.
    CHUNK = 150
    files = {}  # domain -> [(reference filename, count)]
    for dom, items in sorted(buckets.items()):
        items.sort()
        parts = [items[i:i + CHUNK] for i in range(0, len(items), CHUNK)] or [[]]
        for idx, part in enumerate(parts):
            suffix = "" if len(parts) == 1 else "-%d" % (idx + 1)
            fname = "%s%s.md" % (dom, suffix)
            span = ""
            if part and len(parts) > 1:
                span = " (%s to %s)" % (part[0][0], part[-1][0])
            lines = ["# %s -- %d skills%s\n" % (dom, len(part), span)]
            for name, desc, label in part:
                url = fetch_hint(label, name)
                src = label or "skills"
                loc = "[body](%s)" % url if url else "_local only (%s)_" % src
                lines.append("- **%s** (%s) %s\n  %s" % (name, src, loc, desc[:200]))
            with open(os.path.join(OUT, "references", fname), "w",
                      encoding="utf-8") as fh:
                fh.write("\n".join(lines) + "\n")
            files.setdefault(dom, []).append((fname, len(part), span))

    # Flat name list for exact-match lookup.
    allnames = sorted(n for n, _d, _l in rows)
    with open(os.path.join(OUT, "references", "all-names.md"), "w",
              encoding="utf-8") as fh:
        fh.write("# Every skill name (%d)\n\n" % len(allnames))
        fh.write("\n".join("- " + n for n in allnames) + "\n")

    counts = sorted(((d, len(v)) for d, v in buckets.items()), key=lambda x: -x[1])
    table = "\n".join(
        "| `%s` | %d | %s |" % (
            d, n,
            " ".join("`references/%s`%s" % (f, sp) for f, _c, sp in files[d]))
        for d, n in counts)

    skill = """---
name: karim-skill-index
description: >-
  Karim's full skill library as a searchable catalogue -- %d skills across %d
  domains, spanning the local Claude Code library and every installed plugin.
  Use this on any Claude surface (claude.ai chat, Cowork, Claude Code) whenever
  you need to find which of Karim's skills applies to a task, or to fetch a
  skill's full body. Trigger on "which skill", "find a skill", "do I have a
  skill for", "search my skills", or any task where a specialised skill from
  the library would beat answering from general knowledge.
---

# Karim's skill index

%d skills. This file is the map; the detail lives in `references/` and loads
only when a domain is actually in play.

## How to use it

1. Match the task to a domain in the table below.
2. Read that domain's reference file. Each entry gives the skill name, where it
   lives, a one-line description, and a link to its full body.
3. Fetch the body from the link and follow it. Links point at the public repo,
   so they work from any surface with web access.
4. No domain fits -- read `references/all-names.md` and match by name.

On **Claude Code** prefer invoking the skill directly with the Skill tool; this
index is the fallback for surfaces that cannot see the local library.

## Domains

| Domain | Skills | Reference |
|---|---|---|
%s

## Coverage and limits

- Skills under `skills/`, `skills-extra/` and `skills-archive/` are committed to
  the public repo, so their bodies are fetchable over https from anywhere.
- Skills under `~/.agents/skills` are **local only** -- they are listed here for
  discovery but their bodies are not fetchable remotely. They are marked
  `local only` in the reference files.
- Plugin-provided skills are marked with their marketplace.

Regenerate with `python ~/.claude/scripts/build_portable_index.py`.
""" % (len(rows), len(buckets), len(rows), table)

    with open(os.path.join(OUT, "SKILL.md"), "w", encoding="utf-8") as fh:
        fh.write(skill)

    zpath = os.path.join(os.path.dirname(OUT), "karim-skill-index.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _dirs, files in os.walk(OUT):
            for f in files:
                full = os.path.join(dirpath, f)
                z.write(full, os.path.join("karim-skill-index",
                                           os.path.relpath(full, OUT)))

    if "--quiet" in sys.argv:
        return
    print("skills indexed : %d" % len(rows))
    print("domains        : %d" % len(buckets))
    print("SKILL.md       : %.1f KB" % (os.path.getsize(os.path.join(OUT, "SKILL.md")) / 1024))
    ref = sum(os.path.getsize(os.path.join(OUT, "references", f))
              for f in os.listdir(os.path.join(OUT, "references")))
    print("references     : %.0f KB across %d files"
          % (ref / 1024, len(os.listdir(os.path.join(OUT, "references")))))
    print("upload zip     : %s (%.0f KB)" % (zpath, os.path.getsize(zpath) / 1024))


if __name__ == "__main__":
    main()
