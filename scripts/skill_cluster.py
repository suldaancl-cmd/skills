import json, re
inv = json.load(open(r"C:\Users\user\.claude\skill_inventory.json", encoding="utf-8"))
DOM = [
 ("IMMERSIVE-WEB", r"three|webgl|gsap|scroll|particle|preload|shader|immersive|cinematic|3d|glass|lenis|barba|spline|pixi|ogl|babylon|matter-js|theatre|rive|lottie|motion|animation|anime|awwwards|papaya|hyliox|cursor|smoke|webgl"),
 ("STANDARD-WEB", r"landing|frontend|tailwind|shadcn|ui-ux|responsive|seo|page-cro|programmatic-seo|nextjs|react-best|web-design|design-md|antd|ant-design|aceternity|magic-ui|cult-ui|reactbits|wpds|webflow|wix|framer"),
 ("EXPO-MOBILE", r"expo|react-native|app-store|testflight|eas|swiftui|apple-hig|aso|ios|android|mobile|paywall|app-icon|app-launch|maestro|clerk-expo|flutter|kotlin"),
 ("DOCUMENTS", r"docx|pptx|pdf|xlsx|slides|deck|presentation|resume|invoice|report|doc-|minimax-|keynote"),
 ("DESIGN-ASSETS", r"figma|font|typography|color|icon|poster|banner|brand|illustration|imagegen|image-|logo|palette|spacing|layout-grid|design-token|design-system|canvas-design|theme"),
 ("VIDEO-AI", r"video|seedance|higgsfield|sora|kling|remotion|hyperframes|reel|ugc|veo|clip|youtube|tiktok|speech|audio|music|voice|fal-|venice"),
 ("RESEARCH-CONTENT", r"research|content|copywriting|writing|literature|summar|interview|persona|journey|survey|osint|keyword|read-link|notebooklm|firecrawl|seo-audit"),
 ("BUSINESS-OPS", r"advisor|ceo|cfo|cto|cmo|ciso|finance|pricing|sales|marketing|campaign|crm|email|legal|contract|compliance|hiring|hr|okr|board|launch-strategy|metrics|saas-metrics|ma-playbook"),
 ("ENGINEERING", r"code-review|debug|test|tdd|refactor|senior-|architect|docker|devops|security|auth|supabase|stripe|database|sql|api|mcp|agent|skill-|git|deploy|release|rag|llm|jdp-|bbg-|system-design"),
 ("TEMPLATE-LIBS", r"^tpl-|^od-|template|^design-md-|^antd-component-|^jdp-|^bbg-|^refactor-ui-"),
]
res = {d: [] for d,_ in DOM}
res["UNSORTED"] = []
for s in inv:
    key = (s["dir"] + " " + s["description"] + " " + s["h1"]).lower()
    hit = None
    for d, pat in DOM:
        if re.search(pat, key):
            hit = d; break
    res[hit or "UNSORTED"].append(s["dir"])
json.dump(res, open(r"C:\Users\user\.claude\skill_clusters.json","w",encoding="utf-8"), indent=0)
for k,v in res.items(): print(f"{k:18} {len(v)}")
