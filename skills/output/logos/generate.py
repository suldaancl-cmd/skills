"""Obsidian Alchemy — 4 logo variations.

v2: per-face metallic lighting, sharper geometry, auto-fit wordmark.
The mark is an angular monogram that reads as K / IX: a vertical bar with
two sharp diagonals springing from the top and bottom of the bar and meeting
at a single vertex to the right — a closed chevron, not a floating K.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(r"C:/Users/user/.claude/skills/output/logos")
FONTS = Path(r"C:/Users/user/.claude/skills/canvas-design/canvas-fonts")

SIZE = 1024
SS = 2  # supersampling factor
W = SIZE * SS

# -- palette stops (top-highlight → deep copper) -------------------------------
STOPS = [
    (0.00, (255, 244, 208)),  # highlight
    (0.11, (248, 222, 142)),  # pale gold
    (0.28, (227, 182,  76)),  # gold
    (0.46, (194, 140,  50)),  # deep gold
    (0.62, (165, 100,  40)),  # amber
    (0.78, (124,  68,  30)),  # copper
    (0.90, ( 88,  48,  22)),  # oxidised
    (1.00, ( 52,  30,  16)),  # shadow
]
DARKER = [(t, (int(r*0.72), int(g*0.72), int(b*0.72))) for t, (r,g,b) in STOPS]
LIGHTER = [(t, (min(255,int(r*1.12+8)), min(255,int(g*1.10+8)), min(255,int(b*1.05+4))))
           for t, (r,g,b) in STOPS]


# ---------- gradient along an arbitrary axis ---------------------------------

def directional_gradient(w: int, h: int, angle_deg: float, stops=STOPS) -> Image.Image:
    """Gradient whose stops run along an axis at `angle_deg` (0 = top→bottom)."""
    a = math.radians(angle_deg)
    # project pixel coords onto the axis
    xs = np.arange(w)[None, :]
    ys = np.arange(h)[:, None]
    # axis direction: 0° points down (+y), 90° points right (+x)
    dx, dy = math.sin(a), math.cos(a)
    proj = xs * dx + ys * dy
    # normalise to 0..1
    lo = proj.min()
    hi = proj.max()
    t = (proj - lo) / max(1e-6, (hi - lo))
    # build lookup table
    lut = np.zeros((1024, 3), dtype=np.uint8)
    for i in range(1024):
        ti = i / 1023
        for j in range(len(stops) - 1):
            t0, c0 = stops[j]
            t1, c1 = stops[j + 1]
            if t0 <= ti <= t1:
                f = (ti - t0) / (t1 - t0)
                r = int(c0[0] + (c1[0] - c0[0]) * f)
                g = int(c0[1] + (c1[1] - c0[1]) * f)
                b = int(c0[2] + (c1[2] - c0[2]) * f)
                lut[i] = (r, g, b)
                break
    idx = np.clip((t * 1023).astype(np.int32), 0, 1023)
    arr = lut[idx]
    # add a crisp specular band — narrow highlight at t~0.22
    sheen_center = 0.22
    sheen_width = 0.035
    sheen = np.exp(-((t - sheen_center) ** 2) / (2 * sheen_width ** 2))
    arr = np.clip(arr.astype(np.int32) + (sheen[..., None] * np.array([50, 45, 30])).astype(np.int32), 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


# ---------- background --------------------------------------------------------

def dark_ground(w: int, h: int) -> Image.Image:
    cx, cy = w / 2, h / 2
    max_r = math.hypot(cx, cy)
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / max_r
    base = 19
    edge = 6
    v = (base - (base - edge) * np.clip(r, 0, 1)).astype(np.uint8)
    arr = np.stack([v, v, v], axis=-1)
    return Image.fromarray(arr)


# ---------- mark geometry -----------------------------------------------------

def mark_faces(
    w: int,
    h: int,
    height: int,
    bar_w: int,
    arm_reach: int,
    arm_thickness: int,
    x_center: int | None = None,
    y_center: int | None = None,
) -> dict[str, list[tuple[float, float]]]:
    """Return polygons for each face of the K/IX monogram.

    Faces:
      bar        — vertical rectangle
      arm_upper  — diagonal beam from top of bar down-right to vertex
      arm_lower  — diagonal beam from bottom of bar up-right to same vertex
    The vertex sits to the right of the bar, so arms form a rightward-pointing
    chevron grafted onto the bar.
    """
    if x_center is None:
        x_center = w // 2
    if y_center is None:
        y_center = h // 2

    top = y_center - height // 2
    bot = y_center + height // 2

    visual_w = bar_w + arm_reach
    left = x_center - visual_w // 2
    bar_x1 = left
    bar_x2 = left + bar_w

    bar = [(bar_x1, top), (bar_x2, top), (bar_x2, bot), (bar_x1, bot)]

    # vertex where arms meet — slightly right of the bar's right edge at mid
    vertex = (bar_x2 + arm_reach, y_center)

    def beam(p_start, p_end, thickness):
        dx, dy = p_end[0] - p_start[0], p_end[1] - p_start[1]
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        t = thickness / 2
        return [
            (p_start[0] - nx * t, p_start[1] - ny * t),
            (p_start[0] + nx * t, p_start[1] + ny * t),
            (p_end[0] + nx * t, p_end[1] + ny * t),
            (p_end[0] - nx * t, p_end[1] - ny * t),
        ]

    # arms originate from the inner-right corners of the bar top/bottom
    overlap = bar_w // 3
    arm_upper = beam(
        (bar_x2 - overlap, top + bar_w * 0.45),
        vertex,
        arm_thickness,
    )
    arm_lower = beam(
        (bar_x2 - overlap, bot - bar_w * 0.45),
        vertex,
        arm_thickness,
    )

    return {"bar": bar, "arm_upper": arm_upper, "arm_lower": arm_lower}


def paint_face(canvas: Image.Image, polygon, gradient: Image.Image) -> None:
    mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(mask).polygon(polygon, fill=255)
    canvas.paste(gradient, (0, 0), mask)


def hairline_outline(canvas: Image.Image, polygons, thickness_px: int, rgb=(232, 198, 118)) -> None:
    mask = Image.new("L", canvas.size, 0)
    d = ImageDraw.Draw(mask)
    for poly in polygons:
        d.polygon(poly, fill=255)
    edge = mask.filter(ImageFilter.FIND_EDGES)
    for _ in range(max(1, thickness_px - 1)):
        edge = edge.filter(ImageFilter.MaxFilter(3))
    layer = Image.new("RGB", canvas.size, rgb)
    canvas.paste(layer, (0, 0), edge)


def paint_mark(
    canvas: Image.Image,
    faces: dict,
    light_angle_deg: float = 12.0,
) -> None:
    """Paint each face with a gradient angled to suggest one consistent light source."""
    w, h = canvas.size
    # bar — gradient runs top→bottom (axis near vertical, slightly tilted)
    g_bar = directional_gradient(w, h, angle_deg=light_angle_deg, stops=STOPS)
    # upper arm — gradient runs roughly along its axis (down-right ≈ 135° from top)
    g_upper = directional_gradient(w, h, angle_deg=135, stops=LIGHTER)
    # lower arm — gradient runs roughly along its axis (up-right ≈ 45°)
    g_lower = directional_gradient(w, h, angle_deg=45, stops=DARKER)

    paint_face(canvas, faces["arm_lower"], g_lower)
    paint_face(canvas, faces["arm_upper"], g_upper)
    paint_face(canvas, faces["bar"], g_bar)


# ---------- typography --------------------------------------------------------

def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size=size)


def text_width_tracked(draw: ImageDraw.ImageDraw, text: str, font, tracking: int) -> int:
    total = 0
    for i, ch in enumerate(text):
        bb = draw.textbbox((0, 0), ch, font=font)
        total += bb[2] - bb[0]
        if i < len(text) - 1:
            total += tracking
    return total


def draw_tracked(layer, xy, text, font, color, tracking):
    d = ImageDraw.Draw(layer)
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=color)
        bb = d.textbbox((0, 0), ch, font=font)
        x += (bb[2] - bb[0]) + tracking


def fit_font(text: str, font_name: str, target_w: int, tracking_frac: float, max_size: int) -> tuple[ImageFont.FreeTypeFont, int]:
    """Binary-search for the largest font size whose tracked text fits target_w."""
    tmp = ImageDraw.Draw(Image.new("L", (4, 4)))
    lo, hi = 20, max_size
    best = (lo, int(lo * tracking_frac))
    while lo <= hi:
        mid = (lo + hi) // 2
        tracking = max(1, int(mid * tracking_frac))
        font = load_font(font_name, mid)
        w = text_width_tracked(tmp, text, font, tracking)
        if w <= target_w:
            best = (mid, tracking)
            lo = mid + 1
        else:
            hi = mid - 1
    return load_font(font_name, best[0]), best[1]


# ---------- composites --------------------------------------------------------

def logo_01_refined() -> Image.Image:
    bg = dark_ground(W, W)
    faces = mark_faces(
        W, W,
        height=520 * SS,
        bar_w=62 * SS,
        arm_reach=240 * SS,
        arm_thickness=60 * SS,
    )
    paint_mark(bg, faces)
    hairline_outline(bg, list(faces.values()), thickness_px=1 * SS)
    return bg


def logo_02_lockup() -> Image.Image:
    bg = dark_ground(W, W)

    # mark sits in a generous left column
    mark_h = 320 * SS
    mark_cx = int(W * 0.28)
    mark_cy = W // 2
    faces = mark_faces(
        W, W,
        height=mark_h,
        bar_w=44 * SS,
        arm_reach=160 * SS,
        arm_thickness=44 * SS,
        x_center=mark_cx,
        y_center=mark_cy,
    )
    paint_mark(bg, faces)

    # divider between mark and wordmark
    divider_layer = Image.new("L", bg.size, 0)
    d = ImageDraw.Draw(divider_layer)
    div_x = int(W * 0.40)
    div_top = mark_cy - int(mark_h * 0.30)
    div_bot = mark_cy + int(mark_h * 0.30)
    d.rectangle([(div_x, div_top), (div_x + 2 * SS, div_bot)], fill=150)
    g_div = directional_gradient(W, W, angle_deg=12.0, stops=STOPS)
    bg.paste(g_div, (0, 0), divider_layer)

    # wordmark — auto-fit within the right column
    right_margin = int(W * 0.06)
    word_left = int(W * 0.44)
    target_w = W - word_left - right_margin
    font, tracking = fit_font("NEXT LEVEL", "Outfit-Bold.ttf", target_w, 0.14, 120 * SS)

    tmp = ImageDraw.Draw(Image.new("L", (4, 4)))
    tw = text_width_tracked(tmp, "NEXT LEVEL", font, tracking)
    bb = tmp.textbbox((0, 0), "N", font=font)
    th = bb[3] - bb[1]
    tx = word_left + (target_w - tw) // 2
    ty = (W - th) // 2 - int(6 * SS)

    wordmark_layer = Image.new("L", bg.size, 0)
    draw_tracked(wordmark_layer, (tx, ty), "NEXT LEVEL", font, 255, tracking)
    g_word = directional_gradient(W, W, angle_deg=12.0, stops=STOPS)
    bg.paste(g_word, (0, 0), wordmark_layer)

    return bg


def fit_font_simple(text: str, font_name: str, target_w: int, tracking_frac: float, max_size: int):
    return fit_font(text, font_name, target_w, tracking_frac, max_size)


def logo_03_seal() -> Image.Image:
    bg = dark_ground(W, W)
    cx, cy = W // 2, W // 2

    # outer ring
    ring_layer = Image.new("L", bg.size, 0)
    rd = ImageDraw.Draw(ring_layer)
    r_outer = int(W * 0.42)
    rd.ellipse(
        [cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer],
        outline=255,
        width=3 * SS,
    )
    r_inner_ring = r_outer - int(22 * SS)
    rd.ellipse(
        [cx - r_inner_ring, cy - r_inner_ring, cx + r_inner_ring, cy + r_inner_ring],
        outline=165,
        width=2 * SS,
    )
    g_ring = directional_gradient(W, W, angle_deg=12.0, stops=STOPS)
    bg.paste(g_ring, (0, 0), ring_layer)

    # 12 tick marks
    ticks_layer = Image.new("L", bg.size, 0)
    td = ImageDraw.Draw(ticks_layer)
    t_in = r_inner_ring + 4 * SS
    t_out = r_outer - 4 * SS
    for i in range(12):
        a = math.radians(i * 30 - 90)
        x1 = cx + t_in * math.cos(a)
        y1 = cy + t_in * math.sin(a)
        x2 = cx + t_out * math.cos(a)
        y2 = cy + t_out * math.sin(a)
        w_tick = 4 * SS if i % 3 == 0 else 2 * SS
        td.line([(x1, y1), (x2, y2)], fill=215, width=w_tick)
    bg.paste(g_ring, (0, 0), ticks_layer)

    # centred mark
    faces = mark_faces(
        W, W,
        height=360 * SS,
        bar_w=40 * SS,
        arm_reach=160 * SS,
        arm_thickness=40 * SS,
    )
    paint_mark(bg, faces)
    return bg


def logo_04_stacked() -> Image.Image:
    bg = dark_ground(W, W)

    mark_cy = int(W * 0.43)
    faces = mark_faces(
        W, W,
        height=420 * SS,
        bar_w=52 * SS,
        arm_reach=200 * SS,
        arm_thickness=52 * SS,
        y_center=mark_cy,
    )
    paint_mark(bg, faces)

    g_word = directional_gradient(W, W, angle_deg=12.0, stops=STOPS)

    # rule between mark and tagline
    rule_layer = Image.new("L", bg.size, 0)
    rd = ImageDraw.Draw(rule_layer)
    rule_y = int(W * 0.72)
    rule_len = int(W * 0.22)
    rule_x1 = (W - rule_len) // 2
    rd.rectangle([(rule_x1, rule_y), (rule_x1 + rule_len, rule_y + 2 * SS)], fill=175)
    bg.paste(g_word, (0, 0), rule_layer)

    # tagline
    tag = "EST.   2026"
    font, tracking = fit_font_simple(tag, "GeistMono-Regular.ttf", int(W * 0.40), 0.30, 36 * SS)
    tmp = ImageDraw.Draw(Image.new("L", (4, 4)))
    tw = text_width_tracked(tmp, tag, font, tracking)
    bb = tmp.textbbox((0, 0), "E", font=font)
    th = bb[3] - bb[1]
    tx = (W - tw) // 2
    ty = int(W * 0.775)
    tag_layer = Image.new("L", bg.size, 0)
    draw_tracked(tag_layer, (tx, ty), tag, font, 210, tracking)
    bg.paste(g_word, (0, 0), tag_layer)

    return bg


# ---------- driver ------------------------------------------------------------

def render(generator, name: str) -> None:
    img_hi = generator()
    img = img_hi.resize((SIZE, SIZE), Image.LANCZOS)
    path = OUT / name
    img.save(path, format="PNG", optimize=True)
    print(f"  saved {path}  ({path.stat().st_size // 1024} KB)")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("Obsidian Alchemy — rendering 4 marks (v2)")
    render(logo_01_refined, "logo-01-refined.png")
    render(logo_02_lockup,  "logo-02-lockup.png")
    render(logo_03_seal,    "logo-03-seal.png")
    render(logo_04_stacked, "logo-04-stacked.png")
    print("done.")


if __name__ == "__main__":
    main()
