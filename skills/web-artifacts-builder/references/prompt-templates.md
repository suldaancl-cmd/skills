# AI Video & 3D Web Animation Prompt Templates

Proven prompt structures for generating cinematic 3D content for web heroes and marketing videos.

---

## Table of Contents
1. [Seedance 2.0 — Cinematic Video Prompts](#seedance-20)
2. [Spline 3D — Web Hero Animation Prompts](#spline-3d)
3. [Prompt Engineering Rules](#prompt-rules)

---

## Seedance 2.0

Seedance 2.0 is a ByteDance AI cinematic video generator. Prompts must use **film director language**, not code or 3D terminology.

### Prompt Structure (7 Sections)

Every Seedance prompt should cover these areas:

1. **Scene Overview** — What is the scene? What mood? Duration? Loop?
2. **Architecture & Elements** — Describe every physical object in the frame
3. **Materials & Textures** — Surface finishes, glass types, metal finishes
4. **Camera Animation** — Movement type, speed, path, transitions
5. **Lighting Setup** — Light sources, color temps, shadows, time of day
6. **UI Text & Branding** — On-screen text, watermarks, branded elements
7. **Post-Processing** — Bloom, DOF, grain, vignette, color grading

### Template: Aerial Night Cityscape

```
Cinematic 4K aerial drone shot of [CITY] at night. [SPECIFIC SUBJECT]
at the center, surrounded by illuminated high-rise buildings with warm
golden window lights. Night sky with deep navy-black tones. City lights
reflecting off [wet asphalt / glass facades]. Ultra-realistic, 9:16
vertical, smooth slow camera [orbit / dolly / crane]. [BRAND] watermark.
Dramatic cinematic color grading with amber, teal, and deep blue tones.
No sun, no daylight.
```

### Template: Street-Level Establishing Shot

```
4K cinematic ground-level establishing shot of a premium [CITY]
neighborhood at night. Camera slowly pushes forward along a
[tree-lined avenue / commercial street] with [luxury towers / shops]
glowing with warm interior lights. Street lamps casting golden pools
of light. [Slight rain mist creating atmospheric halos / dry crisp
night air]. Deep shadows with subtle blue-teal fill light. No daylight.
Smooth dolly movement. 9:16 vertical. [BRAND] branded.
```

### Template: Interior/Exterior Transition

```
4K cinematic shot from inside a [luxury penthouse / office / showroom]
looking out through floor-to-ceiling windows at [CITY] skyline at night.
Camera slowly pans revealing [modern interior details]. Outside, the
city stretches with thousands of building lights. Reflection of interior
lights on glass. Atmospheric depth haze. Color palette: warm gold
interior, cool blue-teal exterior. No daylight. 9:16 vertical.
```

### Template: Construction / Development Site

```
Cinematic 4K aerial view of a cleared construction-ready urban lot
surrounded by illuminated buildings. Clean leveled dirt and gravel surface
with subtle ground markings. [Golden / amber] boundary lights marking
the plot perimeter. No structures, no cranes. Night sky. Traffic light
trails on surrounding streets. Deep cinematic color grading — navy blacks,
warm ambers, cool teals. 9:16 vertical. [BRAND] title card.
```

### Camera Movement Vocabulary

Use these director terms — Seedance understands film language:

| Term | Effect |
|------|--------|
| Slow orbit | Camera circles subject at constant distance |
| Dolly push | Camera moves forward toward subject |
| Crane up/down | Camera rises or descends vertically |
| Helicopter flyover | High altitude sweeping movement |
| Tracking shot | Camera moves parallel to subject |
| Rack focus | Shift focus from foreground to background |
| Steadicam walk | Smooth handheld-style forward movement |

### Lighting Vocabulary

| Term | Color Temp | Mood |
|------|-----------|------|
| Warm amber | 2700K | Luxury, comfort |
| Cool teal fill | 7500K | Cinematic depth |
| Golden hour (indoor) | 3200K | Premium warmth |
| Moonlight | 5500K blue | Night atmosphere |
| Neon accent | N/A | Urban energy |

---

## Spline 3D

Spline 3D prompts are for interactive web hero animations — they need technical 3D specifications alongside visual descriptions.

### Prompt Structure (7 Sections)

1. **Scene Overview** — Theme, mood, brand, duration, loop behavior
2. **Architecture & Scene Elements** — 3D objects with precise descriptions
3. **Materials & Textures** — IOR values, roughness, metalness, subsurface
4. **Camera Animation** — Path, easing, focal length, orbit speed
5. **Lighting Setup** — Light types, positions, color temperatures, intensity
6. **UI Text & Interactive** — Text overlays, buttons, hover states
7. **Post-Processing & FX** — Bloom, DOF, chromatic aberration, particles

### Key Spline-Specific Terms

- `backdrop-filter` material — for glassmorphism elements
- Subdivide + Voronoi modifier — for geometric facades
- IOR glass material — for transparent building surfaces
- Unreal bloom pass — for light glow effects
- WebGL Three.js compatible export — for web deployment

### Template: Agency Hero Scene

```
Scene Overview:
Create a cinematic, dark-luxury 3D hero animation for [BRAND].
Photorealistic night cityscape. Mood: aspirational, powerful.
15-second seamless loop.

Architecture:
[Describe 3-5 architectural elements with precise shapes, heights,
and materials]

Materials:
Dark green-black tinted glass (IOR 1.45), chrome structural ribs
(metalness 0.95, roughness 0.1), concrete base (roughness 0.8)

Camera:
Slow orbital at 0.3 RPM, 35mm lens, start facing hero tower,
sweep 120° clockwise over 15s, ease-in-out

Lighting:
Key: warm directional (2700K, intensity 0.8) from upper-right
Fill: cool ambient (7500K, intensity 0.3)
Rim: amber point lights on building edges

Post-FX:
Bloom threshold 0.85, radius 6, intensity 0.4
DOF: f/2.8 on hero tower
Film grain: 4% at 1080p
200 ambient dust particles, warm orange, 0.1 m/s upward drift
```

---

## Prompt Rules

1. **Be specific about what's NOT in the scene** — "No sun, no daylight, no cranes"
2. **Include color grading explicitly** — "amber, teal, deep navy" not just "cinematic"
3. **Specify aspect ratio** — 9:16 vertical for social, 16:9 for web heroes
4. **Name the brand** — Include watermark/title card instructions
5. **Reference real architecture** — "inspired by [Nairobi GTC towers / Dubai Marina]"
6. **Control motion speed** — "slow", "gentle", "0.3 RPM" — AI tends to move too fast
7. **Layer atmospheric effects** — fog, haze, rain mist, dust particles add realism
8. **End with technical specs** — resolution (4K), frame rate (60fps), export format
