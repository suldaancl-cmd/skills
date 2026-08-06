#!/usr/bin/env python3
"""Website mirror pipeline: fingerprint -> seeds -> crawl -> repair.

The repair step is the reason this exists. wget's --page-requisites only
follows asset references it can see as src/href on known tags, which on a
modern framework misses most of the payload: modulepreload hints, chunk names
built at runtime, srcset variants, and @font-face URLs inside JS bundles.
Repair scans, fetches, and rescans until a round finds nothing new.

Usage:
  mirror.py fingerprint <url>
  mirror.py seeds <url> [--out seeds.txt] [--limit N]
  mirror.py crawl --seeds <file> --out <dir> [--domains a,b,c]
  mirror.py repair <mirror-dir> --origin <url> [--rounds N]
"""
import argparse
import os
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
HEADERS = {"User-Agent": UA}

WGET = r"C:\Users\user\AppData\Local\Microsoft\WinGet\Links\wget.exe"

# Framework signature -> (label, notes key in references/stacks.md)
STACKS = [
    (r"_nuxt|__NUXT__", "Nuxt"),
    (r"/_next/|__NEXT_DATA__", "Next.js"),
    (r"framerusercontent|data-framer", "Framer"),
    (r"website-files\.com|webflow", "Webflow"),
    (r"wp-content|wp-includes", "WordPress"),
    (r"astro-|_astro/", "Astro"),
    (r"cdn\.shopify", "Shopify"),
    (r"gatsby", "Gatsby"),
]

# Routes that are archive/index noise rather than design surface.
ARCHIVE = re.compile(
    r"^/(blog|glossary|guides|resources|docs|customers|ebooks|webinars|"
    r"podcast|news|press|events?/\d|tag|category|author|search|\d{4})/", re.I)

# Every extension a page can request. Keep this list greedy: an extension that
# is missing here is an asset the repair loop silently declines to fetch, and
# the mirror then looks complete while a whole subsystem is gone. mont-fort.com
# lost its entire WebGL layer (13 .glb models, an .exr envmap, the Basis .wasm
# transcoder) to an allowlist that stopped at images and fonts.
ASSET_EXT = (r"(?:woff2?|ttf|otf|eot|css|m?js|wasm|png|svg|jpe?g|webp|avif|gif|"
             r"ico|mp4|webm|mov|mp3|wav|ogg|m4a|glb|gltf|bin|ktx2|basis|exr|hdr|"
             r"dds|json|vtt|srt|xml|txt|pdf)")

# Path chars include non-ASCII: real sites ship filenames with accented and
# non-Latin characters written literally, not percent-encoded, in the source.
# An ASCII-only class silently skips them and they 404 only in a browser.
PATH_CHARS = r"[^\s\"'()<>\\{}|^`\[\]]+?"


def say(*parts):
    """Print without dying on the Windows cp1252 console (non-ASCII filenames)."""
    line = " ".join(str(p) for p in parts)
    enc = sys.stdout.encoding or "utf-8"
    sys.stdout.write(line.encode(enc, errors="replace").decode(enc) + "\n")


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, timeout=timeout).read()


def cmd_fingerprint(args):
    url = args.url.rstrip("/")
    host = re.sub(r"^https?://", "", url).split("/")[0]
    try:
        html = fetch(url).decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"FAILED to fetch {url}: {e}")
        return 1

    found = [label for pat, label in STACKS if re.search(pat, html, re.I)]
    hosts = Counter(re.findall(r"https?://([a-zA-Z0-9.-]+\.[a-z]{2,})", html))
    # Consent, analytics and edge-telemetry hosts must NEVER be recommended as
    # asset CDNs: spanning the crawl to them mirrors a third-party script that
    # is correct to leave remote, and verify.mjs then counts it as a first-party
    # leak. mont-fort.com surfaced cookiebot + cloudflareinsights as "CDNs".
    third_party = re.compile(
        r"google|gtag|gtm|facebook|linkedin|twitter|youtube|hubspot|segment|"
        r"intercom|hotjar|clarity|marketo|w3\.org|schema\.org|cookiebot|"
        r"cloudflareinsights|cdn-cgi|onetrust|usercentrics|termly|iubenda|"
        r"sentry|datadog|newrelic|doubleclick|adobedtm|typekit|recaptcha", re.I)
    cdns = [(h, n) for h, n in hosts.most_common(12)
            if h != host and not third_party.search(h)]

    try:
        robots = fetch(f"{url}/robots.txt").decode("utf-8", errors="ignore")
        disallow = re.findall(r"^Disallow:\s*(\S+)", robots, re.M)
        blanket = "/" in disallow
    except Exception:
        disallow, blanket = [], False

    print(f"host      : {host}")
    print(f"stack     : {', '.join(found) or 'static / undetected'}")
    print(f"asset CDNs: {', '.join(h for h, _ in cdns[:4]) or 'same-origin only'}")
    print(f"robots    : {'Disallow: / (needs -e robots=off)' if blanket else f'{len(disallow)} specific rules, crawlable'}")

    domains = ",".join([host] + [h for h, _ in cdns[:3]])
    print(f"\nrecommended --domains: {domains}")
    if found:
        print(f"read references/stacks.md section: {found[0]}")
    if "Nuxt" in found or "Next.js" in found:
        print("NOTE: modulepreload chunks will NOT be crawled. Repair is mandatory.")
    return 0


def cmd_seeds(args):
    url = args.url.rstrip("/")
    html = fetch(url).decode("utf-8", errors="ignore")
    paths = set(re.findall(r'href="(/[a-z0-9][a-z0-9/_-]*)"', html, re.I))
    keep = sorted(p for p in paths if not ARCHIVE.match(p + "/"))
    keep = keep[: args.limit]
    lines = [url + "/"] + [f"{url}{p.rstrip('/')}/" for p in keep]

    out = pathlib.Path(args.out)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    dropped = len(paths) - len(keep)
    print(f"wrote {len(lines)} seeds -> {out}")
    print(f"dropped {dropped} archive/index routes (blog, docs, tags, dated)")
    print("REVIEW this list before crawling; tell the user what was scoped out.")
    return 0


def cmd_crawl(args):
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    log = out / "_wget.log"

    cmd = [
        WGET, "--no-check-certificate", "-p", "-k",
        "--adjust-extension", "--restrict-file-names=windows", "--ignore-case",
        "--user-agent=" + UA, "--tries=3", "--timeout=25", "--waitretry=2",
        "-i", str(args.seeds), "-P", str(out), "-o", str(log),
    ]
    if args.robots_off:
        cmd.insert(1, "-e")
        cmd.insert(2, "robots=off")
    if args.domains:
        cmd += ["--span-hosts", "--domains=" + args.domains]

    rc = subprocess.call(cmd)
    files = sum(1 for _ in out.rglob("*") if _.is_file())
    note = {0: "clean", 8: "clean (exit 8 = a 4xx seen mid-crawl, normal)",
            3: "FILE WRITE ERROR - likely a >260-char Windows path"}.get(rc, "check log")
    print(f"wget exit {rc} — {note}")
    print(f"{files} files in {out}")
    print(f"log: {log}")
    return 0


def _origin_for(prefix, origin, host):
    """Assets under a CDN-named dir come from that CDN, not the site origin."""
    return f"https://{prefix}" if "." in prefix else origin


def cmd_repair(args):
    root = pathlib.Path(args.mirror)
    origin = args.origin.rstrip("/")
    host = re.sub(r"^https?://", "", origin).split("/")[0]

    # The web root is the host folder inside the mirror.
    web = root / host if (root / host).is_dir() else root

    # Move sibling CDN dirs inside the web root — served from the host folder,
    # "../cdn.example.com/" resolves above the root and can never load.
    moved = []
    for d in list(root.iterdir()):
        if d.is_dir() and d.name != host and "." in d.name and not d.name.startswith("_"):
            dst = web / d.name
            if not dst.exists():
                shutil.move(str(d), str(dst))
                moved.append(d.name)
    if moved:
        print(f"moved into web root: {', '.join(moved)}")

    cdn_dirs = [p.name for p in web.iterdir() if p.is_dir() and "." in p.name]
    local_dirs = [p.name for p in web.iterdir()
                  if p.is_dir() and p.name.startswith("_")] + ["static", "assets"]
    prefixes = [p for p in set(cdn_dirs + local_dirs) if (web / p).exists() or p in cdn_dirs]

    def text_files():
        return [p for p in web.rglob("*")
                if p.is_file() and p.suffix.lower() in (".html", ".css", ".js", ".mjs")]

    # ── rewrite pass: make every reference root-absolute (idempotent) ────────
    pats = []
    for p in set(cdn_dirs):
        e = re.escape(p)
        pats.append((re.compile(rf"(?:\.\./)+{e}"), f"/{p}"))
        pats.append((re.compile(rf"https?://{e}"), f"/{p}"))
    if prefixes:
        alt = "|".join(re.escape(p) for p in set(prefixes))
        pats.append((re.compile(rf"https?://{re.escape(host)}/({alt})/"), r"/\1/"))

    def rewrite():
        n = 0
        for f in text_files():
            t = orig = f.read_text(encoding="utf-8", errors="ignore")
            for rx, rep in pats:
                t = rx.sub(rep, t)
            if t != orig:
                f.write_text(t, encoding="utf-8")
                n += 1
        return n

    # ── fetch loop: scan -> fetch -> rescan, because fetched files ref more ──
    scan = re.compile(r"/(" + "|".join(re.escape(p) for p in set(prefixes)) +
                      r")/(" + PATH_CHARS + r"\." + ASSET_EXT + r")") if prefixes else None

    # Bare filename literals, for assets whose path is built at runtime
    # (`${base}name.svg`). A static scan can only see the tail, so resolve it
    # against directories where sibling assets already landed.
    bare = re.compile(r"[`'\"]([A-Za-z0-9][A-Za-z0-9_.-]*\." + ASSET_EXT + r")[`'\"]")

    def resolve_runtime_refs():
        """Recover assets whose path is built at runtime (`${base}name.svg`).

        A static scan sees only the filename tail. Rather than guessing the base
        by trying every directory (slow, and mostly 404s), use a SIBLING: these
        literals appear in clusters that share one base, so if `pricing-main.svg`
        is already on disk, its directory IS the base for
        `pricing-main-mobile.svg`. One fetch per file instead of dozens.
        """
        names = set()
        for f in text_files():
            if f.suffix.lower() in (".js", ".mjs"):
                names |= set(bare.findall(f.read_text(encoding="utf-8", errors="ignore")))
        by_name = {}
        for p in web.rglob("*"):
            if p.is_file():
                by_name.setdefault(p.name, p.parent)
        missing = sorted(n for n in names if n not in by_name)
        if not missing:
            return 0

        def sibling_dir(name):
            """Longest shared prefix with a filename already on disk."""
            stem = name.rsplit(".", 1)[0]
            best, best_len = None, 3   # require a real overlap, not one letter
            for known, parent in by_name.items():
                if not known.endswith(name.rsplit(".", 1)[-1]):
                    continue
                k = known.rsplit(".", 1)[0]
                n = len(os.path.commonprefix([stem, k]))
                if n > best_len:
                    best, best_len = parent, n
            return best

        got = 0
        bases = base_dirs()
        for name in missing:
            d = sibling_dir(name)
            if d is None:
                # No sibling to derive the base from. Fall back to the directory
                # literals the source itself declares — bounded (a handful of
                # bases), and it is the exact mechanism a loader uses at runtime:
                # setTranscoderPath("/libs/basis/") + loadAsync("x.wasm").
                for base in bases:
                    url = f"{origin}{base}{name}"
                    if url in dead_urls:
                        continue
                    dest = web / base.strip("/") / name
                    try:
                        body = fetch(url, timeout=30)   # fetch before mkdir
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(body)
                        by_name[name] = dest.parent
                        got += 1
                        break
                    except Exception:
                        dead_urls.add(url)
                continue
            rel = d.relative_to(web).as_posix()
            prefix = rel.split("/")[0]
            src = _origin_for(prefix, origin, host)
            sub = "/".join(rel.split("/")[1:])
            url = f"{src}/{sub}/{name}" if "." in prefix else f"{src}/{rel}/{name}"
            if url in dead_urls:
                continue
            try:
                (d / name).write_bytes(fetch(url, timeout=15))
                got += 1
                by_name[name] = d
            except Exception:
                dead_urls.add(url)
        return got

    # Relative ES-module specifiers: `import "./chunk.js"`, `from "./lib/x.mjs"`.
    #
    # Deliberately `./` only, never `../`. A bundler emits its chunks as
    # siblings, so every real runtime import is same-dir-or-below. What lives
    # above is Vite's `import.meta.glob` map — `{"../Chapters/Capital/Hero.js":
    # qS, ...}` — whose keys are BUILD-TIME source paths already inlined into
    # the bundle. They are never fetched, they 404 upstream, and following them
    # once cost 57 dead requests and 57 empty directories per repair run.
    # The trailing `(?!\s*:)` drops same-dir glob keys too: `Object.assign({
    # "./Pages/Capital.js": _T, ...})` is a map of already-bundled functions, and
    # a specifier followed by a colon is an object key, never a live import.
    module_import = re.compile(
        r"""["'](\./[A-Za-z0-9_.$/-]+\.m?js)["'](?!\s*:)""")

    def resolve_module_imports():
        """Fetch ES-module chunks that JS already on disk imports relatively.

        --page-requisites cannot see these: an `import` specifier is not an
        attribute on a tag it recognises. Miss one and the entry module 404s,
        the whole module graph dies with no console error, and the page sits at
        whatever opacity its reveal script was supposed to clear. On
        mont-fort.com that was five chunks and a blank white homepage.

        Resolution is exact — each specifier against its own importer's
        directory — so unlike the runtime-literal resolver there is nothing to
        guess. Loops internally because each recovered chunk imports more.
        """
        got = 0
        pending = True
        while pending:
            pending = False
            for f in [p for p in web.rglob("*")
                      if p.is_file() and p.suffix.lower() in (".js", ".mjs")]:
                text = f.read_text(encoding="utf-8", errors="ignore")
                for spec in sorted(set(module_import.findall(text))):
                    dest = (f.parent / spec).resolve()
                    if dest.exists() or web.resolve() not in dest.parents:
                        continue        # already have it, or it escapes the root
                    rel = dest.relative_to(web.resolve()).as_posix()
                    prefix = rel.split("/")[0]
                    src = _origin_for(prefix, origin, host)
                    url = f"{src}/{rel.split('/', 1)[1]}" if "." in prefix else f"{src}/{rel}"
                    if url in dead_urls:
                        continue
                    try:
                        # Fetch BEFORE mkdir: creating the directory first leaves
                        # an empty tree behind for every ref that 404s, which
                        # then reads as real site structure in the mirror.
                        body = fetch(url)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(body)
                        got += 1
                        pending = True  # the chunk just landed imports more
                    except Exception:
                        dead_urls.add(url)
        return got

    # Root-absolute DIRECTORY literals, e.g. setTranscoderPath("/libs/basis/").
    # These are the base half of a base+filename pair whose joined path never
    # appears as one string anywhere, so no path scan can ever see it. Collect
    # the bases and the runtime resolver can pair them with the bare filenames.
    dir_literal = re.compile(r"""["'](/[A-Za-z0-9_][A-Za-z0-9_./-]*/)["']""")

    def base_dirs():
        found = set()
        for f in text_files():
            if f.suffix.lower() in (".js", ".mjs"):
                found |= set(dir_literal.findall(
                    f.read_text(encoding="utf-8", errors="ignore")))
        return sorted(d for d in found if "." not in d.split("/")[1])

    total_got = 0
    dead_urls = set()   # unique, not per-round: the same dead ref fails every round
    for rnd in range(1, args.rounds + 1):
        changed = rewrite()
        if not scan:
            break
        refs = set()
        for f in text_files():
            refs |= set(scan.findall(f.read_text(encoding="utf-8", errors="ignore")))

        got = 0
        for prefix, tail in sorted(refs):
            # Check against the DECODED name: that is what we save under and
            # what the static server resolves. Checking the encoded form would
            # miss the file every run and destroy idempotency.
            dest = web / prefix / urllib.parse.unquote(tail)
            if dest.exists():
                continue
            src = _origin_for(prefix, origin, host)
            raw = f"{src}/{tail}" if "." in prefix else f"{src}/{prefix}/{tail}"
            # Source may hold the literal character; the browser requests it
            # percent-encoded. Fetch encoded, save under the decoded name so the
            # static server resolves what the page actually asks for.
            url = urllib.parse.quote(raw, safe=":/?&=%#")
            if url in dead_urls:
                continue        # already known dead; don't refetch every round
            dest = web / prefix / urllib.parse.unquote(tail)
            try:
                body = fetch(url)   # fetch before mkdir: a 404 must leave no dir
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(body)
                got += 1
            except Exception:
                dead_urls.add(url)

        # Modules first: a recovered chunk is what reveals the asset paths that
        # the next two passes then find. Run in the wrong order and a single
        # repair invocation leaves work behind that a second run would pick up.
        module_got = resolve_module_imports()
        runtime_got = resolve_runtime_refs()
        got += module_got + runtime_got
        total_got += got
        extra = ", ".join(
            f"{n} {label}" for n, label in
            ((module_got, "es-module"), (runtime_got, "runtime-constructed")) if n)
        say(f"round {rnd}: rewrote {changed} files, fetched {got}"
            f"{' (' + extra + ')' if extra else ''}, "
            f"{len(dead_urls)} unavailable so far")
        if got == 0:
            break

    print(f"\nrepair done - {total_got} assets recovered, "
          f"{len(dead_urls)} unavailable upstream")
    print(f"web root for serving: {web}")
    print("Verify with: node scripts/verify.mjs <mirror-dir> --port <fresh-port>")
    if dead_urls:
        print("Before reporting the unavailable ones as gaps, curl them on the LIVE "
              "site - most are dead links the site itself emits. Sample:")
        for u in sorted(dead_urls)[:3]:
            print(f"  {u}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fingerprint"); f.add_argument("url"); f.set_defaults(fn=cmd_fingerprint)

    s = sub.add_parser("seeds"); s.add_argument("url")
    s.add_argument("--out", default="seeds.txt"); s.add_argument("--limit", type=int, default=35)
    s.set_defaults(fn=cmd_seeds)

    c = sub.add_parser("crawl"); c.add_argument("--seeds", required=True)
    c.add_argument("--out", required=True); c.add_argument("--domains", default="")
    c.add_argument("--robots-off", action="store_true"); c.set_defaults(fn=cmd_crawl)

    r = sub.add_parser("repair"); r.add_argument("mirror")
    r.add_argument("--origin", required=True); r.add_argument("--rounds", type=int, default=4)
    r.set_defaults(fn=cmd_repair)

    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
