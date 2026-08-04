"""Verify that Arabic font families actually exist on Google Fonts.

Why this exists: family names are easy to hallucinate. "Noto Serif Arabic",
"Sofia Sans Arabic" and "Uthman Taha" all sound correct and none of them are
hosted on Google Fonts. Recommending a font that does not exist wastes the
user's time and is invisible until they try to load it.

Method: hit the css2 API per family. HTTP 200 with a U+06xx unicode-range
means the family is hosted AND ships real Arabic coverage. HTTP 400 means the
name is wrong or the family is not on Google Fonts.

A modern browser User-Agent is required: with an unrecognised UA the API
returns a legacy payload with no unicode-range and every family looks like it
lacks Arabic.

Usage:
    python verify_families.py                    # check the catalog defaults
    python verify_families.py "Cairo" "Amiri"    # check specific names
"""
import json
import sys
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# The families named in references/font-catalog.md, all verified 2026-08-02.
CATALOG = [
    "Amiri", "Noto Naskh Arabic", "Scheherazade New", "Lateef", "Aref Ruqaa",
    "Aref Ruqaa Ink", "Noto Nastaliq Urdu", "Gulzar", "Noto Kufi Arabic",
    "Reem Kufi", "Reem Kufi Ink", "Kufam", "IBM Plex Sans Arabic", "Cairo",
    "Tajawal", "Vazirmatn",
]


def check(family):
    """Return 'ARABIC', 'NO-ARABIC-RANGE', or 'MISSING(code)' for one family."""
    url = "https://fonts.googleapis.com/css2?family=" + urllib.parse.quote(family)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        css = urllib.request.urlopen(req, timeout=20).read().decode()
    except Exception as exc:
        return "MISSING(%s)" % getattr(exc, "code", type(exc).__name__)
    return "ARABIC" if "U+06" in css else "NO-ARABIC-RANGE"


def main(families):
    results = {fam: check(fam) for fam in families}
    for fam, status in sorted(results.items(), key=lambda kv: (kv[1], kv[0])):
        print(f"{status:18} {fam}")
    bad = [f for f, s in results.items() if s != "ARABIC"]
    if bad:
        print(f"\n{len(bad)} family name(s) failed — do not recommend these: {', '.join(bad)}")
    return results


def _self_check():
    """One runnable check: a real family passes, an invented one fails."""
    assert check("Cairo") == "ARABIC", "Cairo should be hosted with Arabic coverage"
    assert check("Noto Serif Arabic").startswith("MISSING"), \
        "Noto Serif Arabic does not exist; verifier should catch it"
    print("self-check OK")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if args and args[0] == "--self-check":
        _self_check()
    else:
        results = main(args or CATALOG)
        if not args:
            with open("gf_arabic_check.json", "w", encoding="utf-8") as fh:
                json.dump(results, fh, indent=1, ensure_ascii=False)
