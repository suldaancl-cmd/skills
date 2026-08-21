"""What the second brain already knows about a skill topic, before you write the skill.

Usage:
  python skill_brief.py "<what the skill should do>" [--detail 20] [--all-rules]

Prints a markdown briefing to stdout. Four sections:
  1. Standing rules  — every feedback_*.md note, unconditionally. These bind EVERY skill.
  2. Topic knowledge — vault notes that match, curated ones content-scanned, bulk dirs by filename.
  3. Existing skills — across live / .agents / archive / cold store, so you extend instead of
                       duplicating something that is already on disk (or parked and restorable).
  4. Router domain   — where the finished skill gets wired into skill-routes.json.

Read every file it lists before writing anything. The brain outranks general knowledge;
when they disagree, say so out loud rather than silently picking one.

Scoring reuses topic_workspace.py's IDF weighting: "design" appears in half the corpus and
carries no signal, "paywall" appears in a dozen files and carries all of it. Weighting words
equally buries the real hits under everything that merely mentions a common noun.
"""
import argparse
import math
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from topic_workspace import (  # noqa: E402  - sibling script, not a package
    CLAUDE, VAULT_DIR, load_skills, match_domains, parse_description, words,
)

COLDSTORE = os.path.join(CLAUDE, "_skills-coldstore")
VAULT_REL = "~/.claude/projects/C--Users-user--claude-skills/memory"

# Curated knowledge is worth reading in full; Sessions/Notion/Intel-Runs are machine-generated
# bulk where a filename match is all the signal there is.
CONTENT_DIRS = ["", "Brain", "app-building-kit"]
BULK_SECTIONS = [
    ("Sessions", "Past chats"),
    ("Intel-Runs", "Intel runs"),
    ("Notion", "Notion"),
    ("Hermes-Knowledge", "Hermes knowledge"),
    ("Fleet-Output", "Fleet output"),
]


def vault_files(sub, recursive):
    root = os.path.join(VAULT_DIR, sub) if sub else VAULT_DIR
    if not os.path.isdir(root):
        return
    if not recursive:
        for f in sorted(os.listdir(root)):
            if f.endswith(".md"):
                yield os.path.join(root, f)
        return
    for dirpath, _dirs, files in os.walk(root):
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def read(path, limit=60000):
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def rel(path):
    return os.path.relpath(path, VAULT_DIR).replace("\\", "/")


def scan_content(topic):
    """[(score, relpath, description)] for the curated notes, IDF-weighted."""
    docs = []
    for sub in CONTENT_DIRS:
        for path in vault_files(sub, recursive=bool(sub)):
            docs.append((path, read(path)))
    n = len(docs) or 1
    idf = {}
    for w in set(topic):
        df = sum(1 for p, body in docs if w in os.path.basename(p).lower() or w in body.lower())
        idf[w] = math.log(n / df) if df else math.log(n)
    hits = []
    for path, body in docs:
        name, low = os.path.basename(path)[:-3].lower(), body.lower()
        s = sum(3 * idf[w] for w in topic if w in name)
        s += sum(min(low.count(w), 5) * 0.4 * idf[w] for w in topic if w in low)
        if s:
            hits.append((round(s, 1), rel(path), parse_description(body[:2000])))
    hits.sort(key=lambda x: (-x[0], x[1]))
    # Almost every note mentions "app" or "design" somewhere, so a bare non-zero score matches
    # ~90% of the vault and the headline count becomes a lie. Keep only what is in the same
    # league as the best hit.
    floor = hits[0][0] * 0.15 if hits else 0
    return [h for h in hits if h[0] >= floor], len(docs)


def scan_filenames(sub, topic):
    hits = []
    for path in vault_files(sub, recursive=True):
        s = sum(2 for w in topic if w in os.path.basename(path)[:-3].lower())
        if s:
            hits.append((s, rel(path)))
    hits.sort(key=lambda x: (-x[0], x[1]))
    # Bulk dirs are machine-generated and huge; a one-word filename brush ("app") matches
    # hundreds of irrelevant files. Keep only the files that matched the most topic words, and
    # drop the section entirely when even the best of them is a single-word coincidence.
    return [h for h in hits if h[0] == hits[0][0]] if hits and hits[0][0] >= 4 else []


def load_parked():
    """{name: description} for skills in the cold store — restorable, not gone."""
    out = {}
    if not os.path.isdir(COLDSTORE):
        return out
    for dirpath, _dirs, files in os.walk(COLDSTORE):
        if "SKILL.md" in files:
            out[os.path.basename(dirpath)] = parse_description(
                read(os.path.join(dirpath, "SKILL.md"), 2000))
    return out


def rank_skills(topic, skills):
    n = len(skills) or 1
    idf = {}
    for w in set(topic):
        df = sum(1 for nm, (d, _l) in skills.items() if w in nm.lower() or w in d.lower())
        idf[w] = math.log(n / df) if df else math.log(n)
    ranked = []
    for name, (desc, label) in skills.items():
        s = (sum(3 * idf[w] for w in topic if w in name.lower())
             + sum(1 * idf[w] for w in topic if w in desc.lower()))
        if s:
            ranked.append((round(s, 1), name, desc, label))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    floor = ranked[0][0] * 0.35 if ranked else 0  # same reason as the vault floor, harsher:
    return [r for r in ranked if r[0] >= floor]   # 1654 skills means more incidental matches


def selftest():
    """python skill_brief.py --selftest — fails loudly if the brief has gone blind."""
    rules = [p for p in vault_files("", recursive=False)
             if os.path.basename(p).startswith("feedback_")]
    assert len(rules) >= 20, f"standing rules vanished: found {len(rules)}, expected 20+"

    topic = words("paywall design and pricing for a mobile app")
    hits, scanned = scan_content(topic)
    assert scanned > 150, f"content scan only saw {scanned} notes"
    assert any("paywall" in r for _s, r, _d in hits[:5]), "paywall notes not in the top 5"
    assert len(hits) < scanned * 0.6, f"floor not pruning: {len(hits)}/{scanned} matched"

    ranked = rank_skills(topic, dict(load_skills(), **{k: (v, "PARKED")
                                                       for k, v in load_parked().items()}))
    assert ranked and ranked[0][1].startswith("paywall"), f"top skill was {ranked[:1]}"
    assert len(ranked) < 60, f"skill floor not pruning: {len(ranked)} matched"

    assert scan_filenames("Notion", words("xyzzy nonexistent")) == [], "empty topic returned hits"
    print(f"selftest OK — {len(rules)} rules, {len(hits)}/{scanned} notes, {len(ranked)} skills")


def main():
    # Vault notes are full of arrows and Arabic; Windows stdout defaults to cp1252 and dies on them.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--selftest" in sys.argv:
        return selftest()
    ap = argparse.ArgumentParser()
    ap.add_argument("topic", help="what the skill should do, in plain words")
    ap.add_argument("--detail", type=int, default=20)
    ap.add_argument("--all-rules", action="store_true",
                    help="print every standing rule even when there are many")
    a = ap.parse_args()

    topic = words(a.topic)
    if not topic:
        sys.exit("topic reduced to zero searchable words — describe the skill in more detail")

    out = [f"# Skill brief: {a.topic}", ""]

    # 1 -------------------------------------------------------------- standing rules
    rules = [(rel(p), parse_description(read(p, 2000)))
             for p in vault_files("", recursive=False)
             if os.path.basename(p).startswith("feedback_")]
    out += [f"## 1. Standing rules ({len(rules)}) — these bind EVERY skill, read them all", "",
            "The skill you write has to obey these, not just its own topic. Encode the ones it "
            "can actually violate directly into its SKILL.md body.", ""]
    for r, d in rules:
        out.append(f"- `{VAULT_REL}/{r}`{' — ' + d[:150] if d else ''}")
    out.append("")

    # 2 ---------------------------------------------------------------- topic knowledge
    hits, scanned = scan_content(topic)
    out += [f"## 2. Topic knowledge — {len(hits)} of {scanned} curated notes matched", "",
            "The brain outranks your general knowledge. If a note contradicts what you were "
            "about to write, the note wins and you say so.", ""]
    if hits:
        for s, r, d in hits[: a.detail]:
            out.append(f"- **{s}** `{VAULT_REL}/{r}`{' — ' + d[:140] if d else ''}")
        if len(hits) > a.detail:
            out.append(f"- _...{len(hits) - a.detail} more, lower-scoring — "
                       f"rerun with `--detail {len(hits)}` to see them._")
    else:
        out.append("- _nothing matched. Say so plainly — a brand-new domain means the skill is "
                   "built from general knowledge, which is worth flagging to Karim._")
    out.append("")

    for sub, title in BULK_SECTIONS:
        bulk = scan_filenames(sub, topic)
        if bulk:
            out += [f"### {title} — {len(bulk)} filename matches (top 8)", ""]
            out += [f"- `{VAULT_REL}/{r}`" for _s, r in bulk[:8]]
            out.append("")

    # 3 ------------------------------------------------------------------ existing skills
    live, parked = load_skills(), load_parked()
    merged = dict(live)
    for name, desc in parked.items():
        merged.setdefault(name, (desc, "PARKED"))
    ranked = rank_skills(topic, merged)
    out += [f"## 3. Skills that already exist — {len(ranked)} of {len(merged)} matched", "",
            "Extend or fix the closest one before adding another. `[archived]` and `[PARKED]` are "
            "on disk and restorable — a new skill that duplicates one of them is pure bloat.", ""]
    if ranked:
        for s, n, d, lb in ranked[: a.detail]:
            tag = f" `[{lb}]`" if lb else ""
            out.append(f"- **{n}** ({s}){tag} — {d[:150]}")
        if len(ranked) > a.detail:
            out.append(f"- _...{len(ranked) - a.detail} more._")
    else:
        out.append("- _no existing skill matched — a genuine gap._")
    out += ["", "Restore a parked skill: `python ~/.claude/scripts/skill_park.py --restore <name>`",
            "Archived: see `~/.claude/skills-archive/MANIFEST-*.txt`.", ""]

    # 4 -------------------------------------------------------------------- router domain
    domains = match_domains(topic)
    out += ["## 4. Router domain — wire the finished skill in here", ""]
    if domains:
        for d in domains:
            chain = " -> ".join(d.get("skills", [])) or "(no chain)"
            out += [f"- **{d['name']}** — chain: {chain}"]
            if d.get("rule"):
                out.append(f"  - hard rule: {d['rule']}")
            for p in d.get("playbooks", []):
                out.append(f"  - playbook: `{VAULT_REL}/{p}`")
    else:
        out.append("- _no domain matched in `skill-routes.json`. Either add the skill to the "
                   "closest existing domain or propose a new one via `skill-router-tune`._")
    out += ["", "Edit `~/.claude/skill-routes.json` so the router surfaces this skill "
                "automatically on every future matching prompt.", "",
            f"_Generated {date.today().isoformat()} by `skill_brief.py`._"]

    print("\n".join(out))


if __name__ == "__main__":
    main()
