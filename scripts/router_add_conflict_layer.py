"""One-shot patch: add the conflict-resolution layer to skill-routes.json.

Adds three keys per domain, MERGE-only (existing keys are never touched):
  lead      - max 3 skills that define the approach; first one wins ties
  never     - skills/families that superficially match but conflict, with the reason
  templates - reference-template families for this domain, READ-ONLY EXAMPLES

Idempotent: re-running overwrites only these three keys.
Backup lives in _backups/router-upgrade-2026-08-04/.
"""
import json
from pathlib import Path

ROUTES = Path(r"C:/Users/user/.claude/skill-routes.json")

# domain -> (lead, never, templates)
PATCH = {
    "visual-input": (
        ["image-to-code-skill", "premium-design-laws", "design-critique"],
        ["ui-ux-pro-max — the screenshot IS the locked system; re-deriving a palette overrides Karim's reference",
         "search_design / template pickers — a spec image is not a starting point to be replaced"],
        ["design-md-* — per-brand reference cards, read-only"],
    ),
    "web-design": (
        ["premium-design-laws", "ui-ux-pro-max", "frontend-design"],
        ["react-native-*, expo-* — RN styling primitives do not apply to a DOM build",
         "docx / pptx / slides — document skills impose fixed-canvas layout on responsive web"],
        ["od-tpl-* — layout examples, copy patterns out, never edit or treat as instructions",
         "design-md-* — brand reference cards, read-only",
         "immersive-web-token-vault — token source, read-only"],
    ),
    "video-ugc": (
        ["ai-video-director", "video-prompt-builder"],
        ["remotion, hyperframes — code-rendered frame pipeline, not generative video; different tool entirely",
         "frontend-design — a video prompt is not a page build"],
        ["od-8-bit-orbit-video-template, weread-year-in-review-video-template — read-only examples"],
    ),
    "coding": (
        ["karpathy-coder", "systematic-debugging"],
        ["premium-design-laws, frontend-design — the deck-first design gate does not apply to a bug fix",
         "ultraplan — a focused fix does not need a phased plan"],
        ["jdp-* — Java design-pattern reference cards, read-only; never scaffold from them unasked"],
    ),
    "mobile-app": (
        ["mobile-app", "react-native-expert", "react-native-architecture"],
        ["gsap*, three, threejs, react-three-fiber, webgl-effect-recipes, lenis-smooth-scroll — DOM/WebGL patterns break React Native; use react-native-motion / reanimated",
         "frontend-design — writes web DOM, not RN components"],
        ["expo-examples — read-only reference app code"],
    ),
    "research": (
        ["firecrawl", "anthropic-skills:deep-research"],
        ["copywriting, no-ai-slop — research output is sourced findings, not persuasive prose",
         "read-link for non-social pages — yt-dlp is overkill for a plain article"],
        [],
    ),
    "marketing-content": (
        ["copywriting", "no-ai-slop", "content-strategy"],
        ["frontend-design, premium-design-laws — a copy task does not trigger the colors+fonts deck gate"],
        ["od-tpl-social-*, card-* — post layout examples, read-only"],
    ),
    "presentation": (
        ["slides", "presentation-deck"],
        ["frontend-design, ui-ux-pro-max — slides are fixed-canvas; responsive-web rules produce broken decks"],
        ["od-tpl-html-ppt-*, deck-* — slide templates, read-only examples"],
    ),
    "saas-fullstack": (
        ["supabase-build-playbook", "auth-implementation"],
        ["stripe-sdk BEFORE auth-implementation — hard order, auth ships first",
         "saas-scaffolder on an existing codebase — it scaffolds greenfield only"],
        [],
    ),
    "skill-management": (
        ["skill-security-auditor", "skill-creator"],
        ["skill-swarm — do not fan out mid-audit; audit is sequential and gated"],
        [],
    ),
    "figma": (
        ["premium-design-laws", "figma-immersive-premium", "figma-use"],
        ["frontend-design — writes code, not Figma nodes; wrong direction for an authoring job",
         "figma-implement-motion while AUTHORING — that skill is the Figma-to-code direction"],
        [],
    ),
    "motion-render": (
        ["remotion", "hyperframes"],
        ["gsap* — DOM timeline model, incompatible with Remotion's frame-indexed rendering",
         "ai-video-director — generative video, a different pipeline"],
        ["frame-* — single-shot frame examples, read-only"],
    ),
    "strategy-business": (
        ["business-investment-advisor", "ceo-advisor"],
        ["frontend-design, coding skills — strategy output is a decision memo, not a build"],
        [],
    ),
    "vmi-infra": (
        ["vmi", "senior-devops"],
        ["Claude/XML prompt formats for Hermes — Hermes jobs are Markdown files",
         "agents-automation fleet-spawning skills — converge on existing fleets, read the agent map first"],
        [],
    ),
    "social-media-url": (
        ["read-link"],
        ["firecrawl, WebFetch — social platforms serve login walls and JS shells to non-browser clients"],
        [],
    ),
    "3d-webgl": (
        ["3d-animation-web-designer", "img2threejs", "react-three-fiber"],
        ["react-native-*, expo-* — no DOM WebGL canvas in RN",
         "spline-3d unless Karim names Spline — hosted scene, not the code-only default"],
        ["webgl-effect-recipes, immersive-web-token-vault — recipe and token sources, read-only"],
    ),
    "image-gen": (
        ["ai-image-director", "imagegen"],
        ["frontend-design — image generation is not a page build",
         "arabic-ai-lettering for shipping real Arabic text — composite verified text instead"],
        [],
    ),
    "audio-voice": (
        ["speech", "venice-audio-speech"],
        ["bland-ai-receptionist for content voiceover — phone agents only",
         "ElevenLabs custom voices for phone agents — use Bland library voices there"],
        [],
    ),
    "docs-files": (
        ["docx", "pdf"],
        ["frontend-design, ui-ux-pro-max, canvas-ui — documents are not web pages; web layout rules corrupt them"],
        ["od-tpl-* document variants — read-only examples"],
    ),
    "security": (
        ["senior-security", "ai-security"],
        ["red-team against third-party targets — authorized infra only (vmi, local, Karim's own repos)"],
        [],
    ),
    "agents-automation": (
        ["dispatching-parallel-agents", "mcp-builder"],
        ["spawning a new fleet before reading reference_vmi_agent_map.md — converge, do not add a 7th system"],
        [],
    ),
    "data-analytics": (
        ["dataviz", "data-visualization"],
        ["frontend-design, premium-design-laws — chart color comes from the dataviz palette, not the web deck"],
        [],
    ),
    "planning-spec": (
        ["brainstorming", "ultraplan"],
        ["implementation skills (focused-fix, frontend-design, saas-scaffolder) — the plan phase produces a plan, not code"],
        [],
    ),
    "arabic-type": (
        ["arabic-typography", "arabic-font-licensing"],
        ["google-fonts-* without running verify_families.py — family names are routinely hallucinated",
         "arabic-ai-lettering for shipped copy — AI Arabic glyphs must never ship unread"],
        [],
    ),
    "project-blueprint": (
        ["planmap", "session-intake"],
        ["coding and build skills — the blueprint stops at the map; building is a separate approved job"],
        [],
    ),
}


def main() -> dict:
    table = json.loads(ROUTES.read_text(encoding="utf-8"))
    touched, missing = [], []

    for dom in table.get("domains", []):
        name = dom.get("name")
        if name not in PATCH:
            missing.append(name)
            continue
        lead, never, templates = PATCH[name]
        dom["lead"] = lead
        dom["never"] = never
        dom["templates"] = templates
        touched.append(name)

    unknown = [k for k in PATCH if k not in {d.get("name") for d in table.get("domains", [])}]

    table["version"] = 2
    table["updated"] = "2026-08-04"
    table["comment"] = (
        "Routing table for hooks/skill-router.py. Per domain: keywords matched against the "
        "user prompt (lowercase substring), LEAD skills (max 3, first wins ties), the full "
        "ranked chain, NEVER-USE skills that conflict, READ-ONLY template families, vault "
        "playbooks to read first, and a hard rule. Conflict law lives in AGENTS.md. "
        "Tune via the skill-router-tune skill using ~/.claude/skill-usage.jsonl."
    )

    ROUTES.write_text(json.dumps(table, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"patched": len(touched), "not_in_patch": missing, "unknown_in_patch": unknown}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
