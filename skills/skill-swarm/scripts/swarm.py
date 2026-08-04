"""Exhaustive skill coverage for one topic.

Ranks every skill in the library against the topic, then splits the matches into three
tiers so ALL of them reach the answer without loading all of them whole:
  tier 1 -> invoke via the Skill tool (full SKILL.md, carries procedure)
  tier 2 -> digested here (headings + hard rules only, ~10 lines each)
  tier 3 -> named only, pulled on demand

Usage:
  python swarm.py --topic "immersive web design" [--out path/SWARM.md] [--tier1 8] [--tier2 40]
  python swarm.py --selftest
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.expanduser("~"), ".claude", "scripts"))
from topic_workspace import SKILL_ROOTS, load_skills, match_domains, rank_skills, words

# Lines worth carrying from a skill we are NOT invoking: the shape (headings) + the constraints.
RULE = re.compile(r"\b(NEVER|ALWAYS|MUST|DO NOT|DON'T|BANNED|FORBIDDEN|REQUIRED|RULE)\b")
HEADING = re.compile(r"^#{2,3}\s+(\S.*)$")


def skill_paths():
    """{skill_name: path_to_SKILL.md}. First root wins, matching load_skills()."""
    out = {}
    for root, _label in SKILL_ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirs, files in os.walk(root):
            if "SKILL.md" in files:
                out.setdefault(os.path.basename(dirpath), os.path.join(dirpath, "SKILL.md"))
    return out


def digest(path, max_headings=4, max_rules=5):
    """(headings, rules) — the actionable core of a skill we won't load whole."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            text = fh.read(12000)
    except OSError:
        return [], []
    headings, rules = [], []
    for line in text.splitlines():
        s = line.strip()
        h = HEADING.match(s)
        if h and len(headings) < max_headings:
            headings.append(h.group(1).strip())
        elif RULE.search(s) and len(s) < 300 and len(rules) < max_rules:
            rules.append(re.sub(r"^[-*>#\s]+", "", s))
        if len(headings) >= max_headings and len(rules) >= max_rules:
            break
    return headings, rules


def tiers(ranked, n1, n2):
    """Split the ranked matches into three exhaustive, non-overlapping tiers."""
    return ranked[:n1], ranked[n1:n1 + n2], ranked[n1 + n2:]


def est_tokens(paths):
    total = 0
    for p in paths:
        try:
            total += os.path.getsize(p)
        except OSError:
            pass
    return total // 4  # ponytail: chars/4 heuristic, swap for a tokenizer if it ever matters


def apply_floor(ranked, pinned, frac):
    """Drop the long tail of incidental one-word hits, keeping pinned skills unconditionally.
    The floor is relative to the best unpinned score, so it adapts per topic instead of
    hard-coding a number that is wrong for every topic but one."""
    if not ranked or frac <= 0:
        return ranked, 0
    pins = set(pinned)
    unpinned = [s for s, n, _d, _l in ranked if n not in pins]
    if not unpinned:
        return ranked, 0
    cut = frac * max(unpinned)
    kept = [r for r in ranked if r[0] >= cut or r[1] in pins]
    return kept, len(ranked) - len(kept)


def build(topic, n1, n2, frac=0.15):
    tw = words(topic)
    domains = match_domains(tw)
    pinned = [s for d in domains for s in d.get("skills", [])]
    library = load_skills()
    ranked, dropped = apply_floor(rank_skills(tw, library, pinned), pinned, frac)
    paths = skill_paths()
    t1, t2, t3 = tiers(ranked, n1, n2)

    out = [f"# Skill swarm — {topic}", "",
           f"**{len(ranked)} relevant of {len(library)} skills scanned** "
           f"({dropped} incidental one-word hits dropped below the {frac:g} relevance floor). "
           f"All {len(ranked)} are accounted for below: {len(t1)} invoked, {len(t2)} digested, "
           f"{len(t3)} named. Domains: {', '.join(d['name'] for d in domains) or 'none'}.", ""]

    t1_tokens = est_tokens([paths[n] for _s, n, _d, _l in t1 if n in paths])
    out += [f"## Tier 1 — invoke these via the Skill tool now ({len(t1)}, ~{t1_tokens} tokens)", ""]
    for s, n, d, lb in t1:
        out.append(f"- **{n}** ({s}){' `[' + lb + ']`' if lb else ''} — {d[:150]}")
    out.append("")

    out += [f"## Tier 2 — digested, do NOT invoke ({len(t2)})", "",
            "Headings are the procedure, rules are the constraints. Obey the rules; if two skills "
            "here contradict, say so and name both instead of silently picking one.", ""]
    for s, n, d, lb in t2:
        h, r = digest(paths.get(n, ""))
        out.append(f"### {n} ({s}){' `[' + lb + ']`' if lb else ''}")
        if d:
            out.append(f"_{d[:180]}_")
        if h:
            out.append("- steps: " + " · ".join(h))
        out += [f"- {x}" for x in r]
        out.append("")

    if t3:
        out += [f"## Tier 3 — named only ({len(t3)}), invoke on demand", "",
                ", ".join(f"`{n}`" for _s, n, _d, _l in t3), ""]

    out += ["## Coverage line — report this verbatim", "",
            f"`{len(ranked)} matched · {len(t1)} invoked · {len(t2)} digested · {len(t3)} named`", ""]
    return "\n".join(out) + "\n", len(ranked), len(library)


def selftest():
    import tempfile
    import textwrap
    d = tempfile.mkdtemp()
    p = os.path.join(d, "SKILL.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(textwrap.dedent("""\
            ---
            name: t
            description: test skill
            ---
            # Title
            ## Step one
            - NEVER use gold.
            ## Step two
            - just a plain line
            """))
    h, r = digest(p)
    assert h[:2] == ["Step one", "Step two"], h
    assert any("NEVER use gold" in x for x in r), r
    assert not any("plain line" in x for x in r), r

    # floor keeps pinned skills even below the cut, and drops incidental tail hits
    scored = [(20.0, "pinned-low", "", ""), (10.0, "strong", "", ""), (1.0, "incidental", "", "")]
    kept, dropped = apply_floor([(1.0, "pinned-low", "", ""), (10.0, "strong", "", ""),
                                 (1.0, "incidental", "", "")], ["pinned-low"], 0.15)
    names = [n for _s, n, _d, _l in kept]
    assert "pinned-low" in names and "strong" in names, names
    assert "incidental" not in names, names
    assert dropped == 1, dropped
    assert apply_floor(scored, [], 0)[0] == scored, "frac=0 must be a no-op"
    assert apply_floor([], [], 0.15) == ([], 0)

    ranked = [(i, f"s{i}", "", "") for i in range(20)]
    t1, t2, t3 = tiers(ranked, 3, 5)
    assert (len(t1), len(t2), len(t3)) == (3, 5, 12)
    assert len(t1) + len(t2) + len(t3) == len(ranked), "tiers must be exhaustive"
    assert not (set(n for _s, n, _d, _l in t1) & set(n for _s, n, _d, _l in t3)), "tiers must not overlap"

    t1, t2, t3 = tiers(ranked, 30, 30)  # over-wide tiers must not crash or duplicate
    assert len(t1) == 20 and not t2 and not t3
    print("selftest OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic")
    ap.add_argument("--out", help="write here instead of stdout (e.g. _projects/<slug>/SWARM.md)")
    ap.add_argument("--tier1", type=int, default=8)
    ap.add_argument("--tier2", type=int, default=40)
    ap.add_argument("--floor", type=float, default=0.15,
                    help="relevance floor as a fraction of the top unpinned score; 0 disables")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        selftest()
        return
    if not a.topic:
        ap.error("--topic is required")

    text, matched, scanned = build(a.topic, a.tier1, a.tier2, a.floor)
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"{a.out}\n{matched} matched of {scanned} scanned")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
