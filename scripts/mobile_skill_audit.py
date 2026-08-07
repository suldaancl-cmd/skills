"""Audit: which installed skills serve building a mobile app, bucketed by stage.

Scans every skill root, reads name + description from frontmatter, and assigns each
skill to at most ONE bucket (first match wins, buckets ordered most-specific first)
so the totals never double-count.

Run: python ~/.claude/scripts/mobile_skill_audit.py
"""
import os, re, json, collections

ROOTS = [
    r"C:\Users\user\.claude\skills",
    r"C:\Users\user\.agents\skills",
]

# (bucket, [regexes]) — ordered: first match wins.
BUCKETS = [
    ("Motion & animation", [
        r"\breanimated\b", r"\bmoti\b", r"\bskia\b", r"rn-screen-transitions",
        r"expo-splash-launch", r"rn-component-motion", r"rn-icon-motion", r"expo-3d-ar",
        r"react-native-motion", r"gesture-patterns", r"micro-interaction",
        r"animation-principles", r"motion-system", r"motion-sound-design",
        r"swiftui-animation", r"flutter-animating", r"\blottie\b", r"\brive\b",
        r"mobbin-motion", r"premium-app-craft", r"figma-motion-pipeline",
    ]),
    ("Core RN / Expo build", [
        # NOTE: anchors don't work here — we match against "<folder> <name>", two tokens.
        r"(^|\s)mobile-app(\s|$)", r"react-native", r"expo-", r"\bexpo\b",
        r"maestro-mobile", r"perfetto", r"jetpack-compose", r"kotlin-specialist",
        r"swiftui-design", r"figma-swiftui", r"app-intents", r"sentry-flutter",
    ]),
    ("Ship / release / store", [
        r"eas-", r"app-store", r"appstore", r"aso-", r"app-launch", r"app-rejection",
        r"metadata-optimization", r"screenshots-marketing", r"screenshot-optimization",
        r"app-icon", r"release-manager", r"release-notes", r"local-build",
    ]),
    ("Monetization & growth", [
        r"paywall", r"pricing-strategy", r"app-growth", r"apple-search-ads",
        r"stripe", r"churn", r"referral", r"onboarding-cro", r"signup-flow-cro",
    ]),
    ("Design & UI for apps", [
        r"apple-hig", r"ui-ux-pro-max", r"design-system", r"design-token",
        r"icon-system", r"onboarding-design", r"loading-states", r"navigation-patterns",
        r"form-design", r"error-handling-ux", r"dark-mode", r"responsive-design",
        r"accessibility", r"a11y", r"wcag", r"gesture", r"visual-hierarchy",
        r"typography-scale", r"spacing-system", r"color-system", r"layout-grid",
        r"rtl-arabic", r"localization-design", r"state-machine",
        r"mobbin-design-research", r"imagegen-frontend-mobile",
        r"od-tpl-mobile-app", r"od-tpl-mobile-onboarding",
    ]),
    ("Backend & data", [
        r"supabase", r"auth-implementation", r"database-designer", r"sql-",
        r"rag-architect", r"mmkv", r"headless-cms",
    ]),
    ("Plan / spec / QA", [
        r"planmap", r"phased-plan", r"ultraplan", r"writing-plans", r"senior-architect",
        r"product-strategist", r"user-flow", r"wireframe", r"prototype",
        r"test-driven", r"senior-qa", r"webapp-testing", r"playwright",
        r"code-review", r"karpathy", r"verification-before",
    ]),
]

def frontmatter(path):
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read(1400)
    except Exception:
        return None, ""
    n = re.search(r"^name:\s*(.+)$", txt, re.M)
    d = re.search(r"^description:\s*(.+)$", txt, re.M)
    return (n.group(1).strip().strip('"\'') if n else None,
            d.group(1).strip() if d else "")

def main():
    seen, skills = set(), {}
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for d in os.listdir(root):
            f = os.path.join(root, d, "SKILL.md")
            if not os.path.isfile(f):
                continue
            real = os.path.realpath(f).lower()
            if real in seen:          # symlink/mirror — count once
                continue
            seen.add(real)
            name, desc = frontmatter(f)
            skills[d] = (name or d, desc)

    # Bucket on IDENTITY (folder + frontmatter name) only. Matching descriptions
    # drags in unrelated skills ("derive" matched rive, etc.) and inflates the count.
    buckets = collections.OrderedDict((b, []) for b, _ in BUCKETS)
    for folder, (name, desc) in sorted(skills.items()):
        hay = f"{folder} {name}".lower()
        for bucket, pats in BUCKETS:
            if any(re.search(p, hay) for p in pats):
                buckets[bucket].append(folder)
                break

    # Separate, broader signal: skills that *mention* mobile work in their description
    # but aren't named for it. Reported, not counted in the core total.
    core = {f for v in buckets.values() for f in v}
    MENTION = re.compile(r"\b(react native|expo|ios app|android app|mobile app|app store|swiftui)\b")
    adjacent = sorted(f for f, (n, d) in skills.items()
                      if f not in core and MENTION.search(f"{n} {d}".lower()))

    total_lib = len(skills)
    total_mobile = sum(len(v) for v in buckets.values())
    print(f"TOTAL DISTINCT SKILLS ON DISK: {total_lib}")
    print(f"NAMED FOR MOBILE APP WORK:     {total_mobile}"
          f"  ({total_mobile*100//total_lib}%)")
    print(f"ADJACENT (description only):   {len(adjacent)}\n")
    for b, items in buckets.items():
        print(f"{b}  —  {len(items)}")
        for i in items:
            print(f"    {i}")
        print()
    print(f"ADJACENT — mobile in description, not in name ({len(adjacent)}):")
    print("    " + ", ".join(adjacent))
    return {"total": total_lib, "mobile": total_mobile,
            "by_bucket": {k: len(v) for k, v in buckets.items()}}

if __name__ == "__main__":
    main()
