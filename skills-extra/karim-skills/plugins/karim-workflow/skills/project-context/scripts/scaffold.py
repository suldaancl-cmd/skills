#!/usr/bin/env python3
"""Copy the nine context files into a project. Never overwrites — reports what it skipped.

Usage:  python scaffold.py <target-project-dir> [--force <file>]

Writes <target>/context/. A file that already exists is left alone, because a half-filled
context file is more valuable than a fresh blank one. Use --force to replace a named file.
"""
import shutil
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"


def main() -> int:
    args = [a for a in sys.argv[1:]]
    force = set()
    while "--force" in args:
        i = args.index("--force")
        if i + 1 >= len(args):
            print("--force needs a filename, e.g. --force 06-ui-tokens.md")
            return 2
        force.add(args[i + 1])
        del args[i : i + 2]

    if len(args) != 1:
        print(__doc__)
        return 2

    target = Path(args[0]).expanduser().resolve()
    if not target.is_dir():
        print(f"target is not a directory: {target}")
        return 1

    dest = target / "context"
    (dest / "designs").mkdir(parents=True, exist_ok=True)

    written, skipped = [], []
    for src in sorted(TEMPLATES.rglob("*.md")):
        rel = src.relative_to(TEMPLATES)
        out = dest / rel
        if out.exists() and rel.name not in force:
            skipped.append(str(rel))
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, out)
        written.append(str(rel))

    print(f"context/ -> {dest}")
    for f in written:
        print(f"  wrote   {f}")
    for f in skipped:
        print(f"  kept    {f}  (already existed, not touched)")
    print(f"\n{len(written)} written, {len(skipped)} kept")
    if skipped:
        print("Re-run with --force <filename> to replace a kept file.")
    return 0


def _selftest() -> None:
    """Run: python scaffold.py --selftest"""
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        sys.argv = ["scaffold.py", td]
        assert main() == 0
        ctx = Path(td) / "context"
        names = {p.name for p in ctx.rglob("*.md")}
        for n in ("01-project-overview.md", "09-progress-tracker.md", "README.md"):
            assert n in names, f"missing {n}"
        assert (ctx / "designs").is_dir(), "designs/ not created"

        # second run must not clobber edited content
        edited = ctx / "01-project-overview.md"
        edited.write_text("EDITED BY USER", encoding="utf-8")
        assert main() == 0
        assert edited.read_text(encoding="utf-8") == "EDITED BY USER", "clobbered an existing file"

        # --force must replace it
        sys.argv = ["scaffold.py", td, "--force", "01-project-overview.md"]
        assert main() == 0
        assert edited.read_text(encoding="utf-8") != "EDITED BY USER", "--force did not replace"
    print("\nselftest OK: scaffolds, never clobbers, --force replaces")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    else:
        sys.exit(main())
