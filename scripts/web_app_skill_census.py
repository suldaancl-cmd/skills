"""Census: how much of the skill library serves WEB vs APP, and what they share.

A skill can serve both (ui-ux-pro-max, supabase, karpathy-coder), so this reports
three sets — web-only, app-only, shared — instead of forcing a single bucket.
The app patterns are the flattened BUCKETS from mobile_skill_audit.py, so the
app total here matches that script by construction.

Bulk reference families (antd-*, design-md-*, jdp-*, od-tpl-*) are counted but
reported separately: 120 Ant Design component cards is not 120 skills' worth of
capability, and folding them into the headline makes web look 3x richer than it is.

Run: python ~/.claude/scripts/web_app_skill_census.py
"""
import os, re, collections, importlib.util

ROOTS = [r"C:\Users\user\.claude\skills", r"C:\Users\user\.agents\skills"]

_spec = importlib.util.spec_from_file_location(
    "mobile_audit", os.path.join(os.path.dirname(__file__), "mobile_skill_audit.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
APP_PATTERNS = [p for _, pats in _m.BUCKETS for p in pats]

WEB_STAGES = [
    ("Design & UI (web)", [
        r"^design-md", r"frontend-design", r"web-design", r"landing-page", r"^tailwind$",
        r"shadcn", r"aceternity", r"magic-ui", r"cult-ui", r"reactbits", r"antalik-ui",
        r"canvas-ui", r"^antd-", r"ant-design", r"premium-design-laws", r"ui-ux-pro-max",
        r"refactor-ui", r"minimalist-ui", r"industrial-brutalist", r"high-end-visual",
        r"design-taste-frontend", r"awesome-design-md", r"web-design-guidelines",
    ]),
    ("Motion & animation (web)", [
        r"^gsap", r"lenis", r"barba", r"animejs", r"motion-dev", r"motion-primitives",
        r"waapi", r"css-animations", r"web-animation-effects", r"theatre-js",
        r"react-spring", r"choreograph-scroll", r"template-scroll-animation",
        r"premium-motion-cookbook", r"webflow-premium-motion", r"cursor-interaction",
        r"premium-preloader", r"web-motion-library-map", r"^lottie$", r"^rive-runtime$",
    ]),
    ("3D / WebGL", [
        r"^three$", r"^threejs$", r"react-three", r"react-postprocessing", r"webgpu",
        r"ogl-webgl", r"babylonjs", r"pixijs", r"shader-dev", r"webgl-", r"matter-js",
        r"spline-3d", r"img2threejs", r"3d-animation-web", r"papaya-smoke", r"hyliox",
        r"immersive-components", r"immersive-web-token", r"figma-shader",
    ]),
    ("Build / framework / stack", [
        r"senior-frontend", r"senior-fullstack", r"frontend-dev", r"frontend-skill",
        r"saas-scaffolder", r"headless-cms", r"supabase", r"auth-implementation",
        r"^stripe", r"webflow", r"framer-template", r"^wix", r"^vercel", r"netlify",
        r"website-download", r"website-stack-teardown", r"web-artifacts-builder",
        r"artifacts-builder", r"html-everything", r"theming", r"theme-factory",
    ]),
    ("Growth / SEO / CRO", [
        r"seo-audit", r"ai-seo", r"programmatic-seo", r"keyword-research",
        r"schema-markup", r"site-architecture", r"-cro$", r"^page-cro", r"^form-cro",
        r"free-tool-strategy", r"link-in-bio", r"competitor-alternatives",
    ]),
    ("Plan / QA / audit (web)", [
        r"awwwards", r"design-review", r"design-audit", r"design-critique",
        r"^impeccable", r"no-ai-slop", r"playwright", r"webapp-testing",
        r"a11y-audit", r"accessibility-audit", r"wcag", r"full-page-screenshot",
    ]),
]
WEB_PATTERNS = [p for _, pats in WEB_STAGES for p in pats]

BULK = [("antd-*", r"^antd-"), ("design-md-*", r"^design-md-"),
        ("od-tpl-* / od-*", r"^od-"), ("jdp-*", r"^jdp-")]


def load():
    skills = {}
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for d in os.listdir(root):
            f = os.path.join(root, d, "SKILL.md")
            if not os.path.isfile(f) or d in skills:
                continue
            name, _ = _m.frontmatter(f)
            skills[d] = (name or d, root)
    return skills


def main():
    skills = load()
    web, app = set(), set()
    stage_hits = collections.OrderedDict((s, []) for s, _ in WEB_STAGES)

    for folder, (name, _root) in skills.items():
        hay = f"{folder} {name}".lower()
        if any(re.search(p, hay) for p in APP_PATTERNS):
            app.add(folder)
        for stage, pats in WEB_STAGES:
            if any(re.search(p, hay) for p in pats):
                web.add(folder)
                stage_hits[stage].append(folder)
                break

    both = web & app
    print(f"LIBRARY (distinct, both roots): {len(skills)}\n")
    print(f"{'WEB total':22s} {len(web):5d}   (web-only {len(web - app)})")
    print(f"{'APP total':22s} {len(app):5d}   (app-only {len(app - web)})")
    print(f"{'SHARED both':22s} {len(both):5d}")
    print(f"{'Neither':22s} {len(skills) - len(web | app):5d}\n")

    print("WEB by stage")
    for s, items in stage_hits.items():
        print(f"  {s:28s} {len(items):5d}")

    print("\nBULK REFERENCE FAMILIES (counted above, but they are cards not capability)")
    total_bulk = 0
    for label, pat in BULK:
        n = len([f for f in skills if re.search(pat, f)])
        nw = len([f for f in web if re.search(pat, f)])
        total_bulk += nw
        print(f"  {label:16s} {n:5d} on disk   {nw:5d} counted as web")
    print(f"  {'':16s} {'':5s}             {total_bulk:5d} total")
    print(f"\nWEB minus bulk families: {len(web) - total_bulk}")
    print(f"Shared web+app skills:   {sorted(both)}")
    return {"web": len(web), "app": len(app), "both": len(both)}


if __name__ == "__main__":
    main()
