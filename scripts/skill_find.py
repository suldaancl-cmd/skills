"""Search the whole skill library from one command — the long tail without a workspace.

  python ~/.claude/scripts/skill_find.py "arabic paywall onboarding" [-n 30] [--all]

Reuses topic_workspace's loader + ranker so search results and workspace SKILLS.md
never disagree. --all drops the score filter and prints every match, names only.
"""
import argparse
import importlib.util
import os
import sys

TW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "topic_workspace.py")
_spec = importlib.util.spec_from_file_location("topic_workspace", TW)
tw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", type=int, default=20)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()

    query = " ".join(a.query)
    words = tw.words(query)
    if not words:
        print("query too short after stopword removal", file=sys.stderr)
        return 2

    domains = tw.match_domains(words)
    pinned = [s for d in domains for s in d.get("skills", [])]
    ranked = tw.rank_skills(words, tw.load_skills(), pinned)

    print(f"{len(ranked)} skills match '{query}'"
          f"  |  routing domains: {', '.join(d['name'] for d in domains) or 'none'}")
    if pinned:
        print(f"chain: {' -> '.join(pinned)}")
    print()
    if a.all:
        print(", ".join(n for _s, n, _d, _l in ranked))
    else:
        for s, n, d, label in ranked[: a.n]:
            tag = f" [{label}]" if label and label != "skills" else ""
            print(f"{s:4}  {n}{tag}\n      {d[:150]}")
        if len(ranked) > a.n:
            print(f"\n... {len(ranked) - a.n} more — rerun with --all or -n {len(ranked)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
