"""Illustration primitives for 'After the Beam' (v0.2 engine).
All functions take d (supersampled draw proxy, logical 1920x1080 coords) and F (font fn: F(name,size)).
Drawing area for diagrams: y 110..690 (subtitles below ~760, ref card at y 698-742 right side).
Colors: cell identities are fixed across the series:
  muscle fiber = rose/red; satellite cell (MuSC) = GREEN; FAP = ORANGE; macrophage = PURPLE;
  endothelium/capillary = RED; collagen/scar = ICE (pale blue-white); fat = YELLOW; ROS sparks = ORANGE/GOLD.
"""
import math, random
from diagrams import T, arrow, box, helix, cell, foci, fiber, W, WHITE, GREY, DIM, BLUE, ORANGE, RED, GREEN, GOLD, PINK, MAG, TEAL

PURPLE = (160, 110, 230); YELLOW = (250, 220, 90); ICE = (200, 225, 245); ROSE = (205, 85, 100)
SCOL = {'FACT': (46, 160, 90), 'ASSOCIATION': (214, 150, 40), 'HYPOTHESIS': (200, 70, 60), 'BENCH': (70, 120, 200)}

def label(d, F, xy, en, zh=None, size=28, col=WHITE, zcol=GREY, anchor='mm', gap=None):
    """Two-line bilingual label centred at xy (EN on top, ZH below)."""
    if zh:
        g = gap or size * 0.62
        T(d, F, (xy[0], xy[1] - g), en, size, col, anchor)
        T(d, F, (xy[0], xy[1] + g), zh, int(size * 0.9), zcol, anchor)
    else:
        T(d, F, xy, en, size, col, anchor)

def pill(d, F, c, text, col=BLUE, size=24, pad=22):
    tw = d.textlength(text, F('sans', size))
    d.rounded_rectangle([c[0] - tw / 2 - pad, c[1] - size * 0.85, c[0] + tw / 2 + pad, c[1] + size * 0.85], size, fill=col + (220,))
    T(d, F, c, text, size, (255, 255, 255))

def stamp(d, F, c, text, col=RED, size=26):
    """Rubber-stamp style evidence/warning label."""
    tw = d.textlength(text, F('sans', size))
    x0, y0, x1, y1 = c[0] - tw / 2 - 26, c[1] - size, c[0] + tw / 2 + 26, c[1] + size
    d.rounded_rectangle([x0, y0, x1, y1], 10, fill=col + (40,), outline=col + (255,), width=4)
    d.rounded_rectangle([x0 + 6, y0 + 6, x1 - 6, y1 - 6], 7, outline=col + (150,), width=1)
    T(d, F, c, text, size, col)

def card(d, F, bx, title=None, lines=(), col=BLUE, size=26, title_size=30):
    """Rounded info card. lines = list of str or (en, zh) tuples."""
    x0, y0, x1, y1 = bx
    d.rounded_rectangle(bx, 20, fill=col + (38,), outline=col + (220,), width=3)
    y = y0 + 36
    if title:
        T(d, F, ((x0 + x1) / 2, y), title, title_size, col if sum(col) > 300 else WHITE); y += title_size + 22
    for ln in lines:
        if isinstance(ln, tuple):
            T(d, F, ((x0 + x1) / 2, y), ln[0], size); T(d, F, ((x0 + x1) / 2, y + size + 6), ln[1], size - 3, GREY); y += size * 2 + 22
        else:
            T(d, F, ((x0 + x1) / 2, y), ln, size); y += size + 18

def darrow(d, a, b, fill=WHITE, w=4, head=16, dash=16):
    """Dashed arrow (predicted / untested link)."""
    L = math.dist(a, b); n = max(1, int(L / dash))
    for i in range(0, n - 1, 2):
        p = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
        q = (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n)
        d.line([p, q], fill=fill, width=w)
    arrow(d, (a[0] + (b[0] - a[0]) * (n - 1) / n, a[1] + (b[1] - a[1]) * (n - 1) / n), b, fill, w, head)

def inhibit(d, a, b, fill=RED, w=5):
    """Blunt-ended inhibition arrow  a --| b."""
    d.line([a, b], fill=fill, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0]); px, py = -math.sin(ang) * 18, math.cos(ang) * 18
    d.line([(b[0] - px, b[1] - py), (b[0] + px, b[1] + py)], fill=fill, width=w + 2)

def curved(d, a, b, bend=60, fill=WHITE, w=4, head=16):
    """Curved arrow via quadratic bezier."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    ang = math.atan2(b[1] - a[1], b[0] - a[0]); cx, cy = mx - math.sin(ang) * bend, my + math.cos(ang) * bend
    pts = [((1 - t) ** 2 * a[0] + 2 * (1 - t) * t * cx + t * t * b[0], (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * cy + t * t * b[1]) for t in [i / 30 for i in range(31)]]
    d.line(pts[:-2], fill=fill, width=w); arrow(d, pts[-3], pts[-1], fill, w, head)

def xmark(d, c, s=26, col=RED, w=7):
    d.line([(c[0] - s, c[1] - s), (c[0] + s, c[1] + s)], fill=col, width=w); d.line([(c[0] - s, c[1] + s), (c[0] + s, c[1] - s)], fill=col, width=w)

def check(d, c, s=26, col=GREEN, w=7):
    d.line([(c[0] - s, c[1]), (c[0] - s * 0.3, c[1] + s * 0.7), (c[0] + s, c[1] - s * 0.8)], fill=col, width=w)

def updown(d, F, c, up=True, col=None, size=34):
    T(d, F, c, '↑' if up else '↓', size, col or (GREEN if up else RED))

# ---------- cells ----------
def sat_cell(d, c, s=1.0, col=GREEN, dead=False):
    """Satellite cell: flattened green spindle with dark nucleus. dead=True -> grey outline + X."""
    x, y = c; w, h = 52 * s, 24 * s
    if dead:
        d.ellipse([x - w, y - h, x + w, y + h], outline=(130, 135, 145), width=3); xmark(d, c, 14 * s, (200, 80, 80), 5); return
    d.ellipse([x - w, y - h, x + w, y + h], fill=col + (225,), outline=tuple(min(255, v + 70) for v in col), width=3)
    d.ellipse([x - w * .4, y - h * .5, x + w * .4, y + h * .5], fill=(30, 90, 50))

def fap(d, c, s=1.0, col=ORANGE, angle=0.0, grey=False):
    """FAP: orange spindle/stellate cell with processes."""
    if grey: col = (140, 140, 150)
    x, y = c; L = 70 * s; ca, sa = math.cos(angle), math.sin(angle)
    tips = [(x + ca * L, y + sa * L), (x - ca * L, y - sa * L), (x - sa * 34 * s + ca * 20 * s, y + ca * 34 * s + sa * 20 * s)]
    for t in tips: d.line([(x, y), t], fill=col + (200,), width=int(6 * s) or 1)
    d.ellipse([x - 26 * s, y - 18 * s, x + 26 * s, y + 18 * s], fill=col + (230,), outline=tuple(min(255, v + 50) for v in col), width=2)
    d.ellipse([x - 11 * s, y - 8 * s, x + 11 * s, y + 8 * s], fill=(110, 60, 20))

def macrophage(d, c, s=1.0, col=PURPLE, seed=3):
    """Macrophage: irregular purple blob with pseudopods."""
    rnd = random.Random(seed); x, y = c; pts = []
    for i in range(16):
        a = i / 16 * 6.283; r = (44 + rnd.uniform(-8, 14) + (16 if i % 4 == 0 else 0)) * s
        pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    d.polygon(pts, fill=col + (215,), outline=tuple(min(255, v + 60) for v in col))
    d.ellipse([x - 18 * s, y - 14 * s, x + 14 * s, y + 16 * s], fill=(70, 40, 120))
    for k in range(3):
        a = rnd.uniform(0, 6.28); r = 26 * s
        d.ellipse([x + r * math.cos(a) - 5 * s, y + r * math.sin(a) - 5 * s, x + r * math.cos(a) + 5 * s, y + r * math.sin(a) + 5 * s], fill=(230, 210, 255, 180))

def capillary(d, c, r=22, col=RED, cut=False):
    """Capillary in cross-section: red ring with lumen and a red blood cell."""
    x, y = c
    if cut:
        d.ellipse([x - r, y - r, x + r, y + r], outline=(120, 90, 95), width=3); return
    d.ellipse([x - r, y - r, x + r, y + r], fill=col + (90,), outline=col, width=4)
    d.ellipse([x - r * .45, y - r * .3, x + r * .45, y + r * .3], fill=(240, 120, 110))

def vessel(d, x0, x1, y, h=60, col=RED, leaky=False):
    """Longitudinal blood vessel tube with flowing RBCs."""
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], h / 2, fill=col + (60,), outline=col, width=4)
    for i, x in enumerate(range(int(x0) + 40, int(x1) - 30, 70)):
        d.ellipse([x - 16, y - 9 + (i % 2) * 6 - 3, x + 16, y + 9 + (i % 2) * 6 - 3], fill=(235, 95, 90))
    if leaky:
        for x in range(int(x0) + 80, int(x1) - 40, 160):
            d.ellipse([x - 6, y + h / 2 + 10, x + 6, y + h / 2 + 22], fill=(235, 95, 90, 160))

def myofibroblast(d, c, s=1.0):
    x, y = c
    d.polygon([(x - 90 * s, y), (x - 20 * s, y - 28 * s), (x + 90 * s, y), (x - 20 * s, y + 28 * s)], fill=(200, 140, 90, 210), outline=(240, 190, 140))
    for k in (-14, 0, 14): d.line([(x - 60 * s, y + k * s * .7), (x + 60 * s, y + k * s * .7)], fill=(255, 220, 180, 170), width=2)
    d.ellipse([x - 26 * s, y - 12 * s, x + 6 * s, y + 12 * s], fill=(110, 60, 30))

def senescent(d, F, c, r=40, col=ORANGE):
    """Grey, enlarged, flattened cell with a clock badge and SASP puffs."""
    x, y = c
    cell(d, c, r, fill=(110, 110, 120), nucfill=(70, 70, 80))
    d.ellipse([x + r * .5, y - r * 1.1, x + r * 1.2, y - r * .4], fill=(40, 40, 50), outline=GOLD, width=2)
    d.line([(x + r * .85, y - r * .75), (x + r * .85, y - r * .95)], fill=GOLD, width=2); d.line([(x + r * .85, y - r * .75), (x + r, y - r * .75)], fill=GOLD, width=2)

def sasp(d, c, n=7, R=90, seed=5, col=(230, 120, 160)):
    rnd = random.Random(seed)
    for i in range(n):
        a = rnd.uniform(0, 6.28); r = rnd.uniform(R * .6, R)
        x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a); s = rnd.uniform(6, 13)
        d.ellipse([x - s, y - s, x + s, y + s], fill=col + (170,))

def mito(d, c, w=260, h=130, col=(230, 120, 80), sparks=0, swollen=False, seed=2):
    x, y = c
    if swollen: h *= 1.4
    d.ellipse([x - w / 2, y - h / 2, x + w / 2, y + h / 2], fill=col + (200,), outline=tuple(min(255, v + 40) for v in col), width=4)
    d.ellipse([x - w / 2 + 14, y - h / 2 + 14, x + w / 2 - 14, y + h / 2 - 14], fill=(120, 50, 40, 200))
    n = 6
    for i in range(n):
        cx = x - w / 2 + 40 + i * (w - 80) / (n - 1); top = i % 2 == 0
        if swollen and i % 2: continue
        d.line([(cx, y - h / 2 + 16 if top else y + h / 2 - 16), (cx, y + (8 if top else -8))], fill=(255, 170, 130), width=6)
    rnd = random.Random(seed)
    for _ in range(sparks):
        a = rnd.uniform(0, 6.28); r = rnd.uniform(w * .55, w * .85)
        sx, sy = x + r * math.cos(a), y + r * math.sin(a) * .6
        d.polygon([(sx, sy - 12), (sx + 4, sy - 3), (sx + 12, sy), (sx + 4, sy + 3), (sx, sy + 12), (sx - 4, sy + 3), (sx - 12, sy), (sx - 4, sy - 3)], fill=GOLD)

def fat(d, c, n=6, R=50, seed=4):
    rnd = random.Random(seed)
    for _ in range(n):
        a = rnd.uniform(0, 6.28); r = rnd.uniform(0, R); s = rnd.uniform(12, 26)
        x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
        d.ellipse([x - s, y - s, x + s, y + s], fill=YELLOW + (200,), outline=(255, 245, 190), width=2)

def collagen(d, box_, n=10, seed=6, col=ICE, w=3):
    """Wavy collagen strands filling a box (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box_; rnd = random.Random(seed)
    for i in range(n):
        yy = y0 + (y1 - y0) * (i + .5) / n; ph = rnd.uniform(0, 6); amp = rnd.uniform(4, 9)
        pts = [(x, yy + amp * math.sin(ph + (x - x0) / 22)) for x in range(int(x0), int(x1), 6)]
        if len(pts) > 1: d.line(pts, fill=col + (180,), width=w)

def xsection(d, c, R=230, n=14, seed=11, fib_col=ROSE, scar=0.0, caps=True, sats=0, sat_dead=0, faps=0, small=1.0):
    """Muscle cross-section: packed round/polygonal fibers in a fascia ring.
    scar 0..1 thickens ICE collagen between fibers; caps draws capillaries between fibers;
    sats = number of satellite cells at fiber edges (first sat_dead drawn dead); faps in interstitium.
    small<1 shrinks fibers (atrophy). Returns list of fiber centres."""
    rnd = random.Random(seed); x, y = c; cents = []
    d.ellipse([x - R - 14, y - R - 14, x + R + 14, y + R + 14], fill=(60, 40, 50, 120), outline=(200, 160, 170), width=3)
    if scar > 0:
        d.ellipse([x - R, y - R, x + R, y + R], fill=ICE + (int(40 + 120 * scar),))
    sp = R * 2 / max(3.0, math.sqrt(n) * 1.25)
    for row in range(-12, 13):
        for col in range(-12, 13):
            px = x + (col + (row % 2) * .5) * sp + rnd.uniform(-sp * .06, sp * .06); py = y + row * sp * .866 + rnd.uniform(-sp * .06, sp * .06)
            if math.dist((px, py), c) < R - sp * .5: cents.append((px, py))
    fr = sp * .46 * small * (1 - .25 * scar)
    for p in cents:
        d.ellipse([p[0] - fr, p[1] - fr, p[0] + fr, p[1] + fr], fill=fib_col + (230,), outline=(240, 150, 160), width=3)
        d.ellipse([p[0] + fr * .5, p[1] - fr * .2, p[0] + fr * .8, p[1] + fr * .1], fill=(70, 70, 150))
    if caps:
        for i, p in enumerate(cents):
            q = cents[(i + 1) % len(cents)]; m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
            if math.dist(m, c) < R * .9 and i % 2 == 0: capillary(d, m, 9)
    for i in range(min(sats, len(cents))):
        p = cents[i * 2 % len(cents)]; sp = (p[0], p[1] - fr - 4)
        sat_cell(d, sp, .45, dead=(i < sat_dead))
    for i in range(faps):
        p = cents[(i * 3 + 1) % len(cents)]; q = cents[(i * 3 + 2) % len(cents)]
        fap(d, ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2), .45, angle=i)
    return cents

def beam(d, a, b, col=GOLD, w=10):
    """Radiation beam: glowing zigzag bolt from a to b."""
    n = 7; pts = []
    for i in range(n + 1):
        t = i / n; px, py = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        off = (16 if i % 2 else -16) if 0 < i < n else 0
        ang = math.atan2(b[1] - a[1], b[0] - a[0]); pts.append((px - math.sin(ang) * off, py + math.cos(ang) * off))
    d.line(pts, fill=col + (90,), width=w * 3); d.line(pts, fill=col, width=w); d.line(pts, fill=(255, 255, 230), width=max(2, w // 3))
    arrow(d, pts[-2], pts[-1], col, w, 30)

def shield(d, F, c, h=160, text="shield 遮挡"):
    x, y = c
    d.rounded_rectangle([x - 22, y - h / 2, x + 22, y + h / 2], 8, fill=(120, 125, 135, 230), outline=(200, 205, 215), width=3)
    for k in range(int(y - h / 2) + 14, int(y + h / 2), 20): d.line([(x - 18, k), (x + 18, k - 10)], fill=(160, 165, 175), width=2)
    T(d, F, (x, y + h / 2 + 24), text, 20, GREY)

def mouse(d, c, s=1.0, col=(200, 200, 210), facing=1):
    """Lab mouse silhouette. facing=1 right, -1 left."""
    x, y = c; f = facing
    d.ellipse([x - 70 * s, y - 38 * s, x + 50 * s, y + 38 * s], fill=col + (230,))
    d.ellipse([x + f * 30 * s - 30 * s, y - 34 * s, x + f * 30 * s + 30 * s, y + 18 * s], fill=col + (230,))
    hx = x + f * 70 * s
    d.polygon([(x + f * 40 * s, y - 26 * s), (hx + f * 22 * s, y - 4 * s), (x + f * 40 * s, y + 14 * s)], fill=col)
    d.ellipse([x + f * 36 * s - 14 * s, y - 50 * s, x + f * 36 * s + 14 * s, y - 22 * s], fill=(230, 180, 190))
    d.ellipse([hx - 4 * s, y - 12 * s, hx + 4 * s, y - 4 * s], fill=(30, 30, 30))
    d.line([(x - f * 70 * s, y + 10 * s), (x - f * 120 * s, y - 20 * s), (x - f * 150 * s, y + 6 * s)], fill=(230, 180, 190), width=max(2, int(5 * s)))
    for lx in (-40, 20): d.line([(x + lx * s, y + 34 * s), (x + lx * s, y + 50 * s)], fill=col, width=max(2, int(8 * s)))

def rat(d, c, s=1.0, facing=1):
    mouse(d, c, s * 1.45, col=(185, 175, 165), facing=facing)

def dish(d, F, c, r=90, label_=None, content=None):
    x, y = c
    d.ellipse([x - r, y - r * .38, x + r, y + r * .38], fill=(180, 210, 230, 50), outline=(200, 225, 240), width=3)
    d.ellipse([x - r * .9, y - r * .3, x + r * .9, y + r * .3], outline=(200, 225, 240, 120), width=2)
    if label_: T(d, F, (x, y + r * .38 + 26), label_, 22, GREY)

def syringe(d, a, s=1.0, col=(200, 220, 240)):
    x, y = a
    d.rounded_rectangle([x, y - 14 * s, x + 130 * s, y + 14 * s], 6, fill=col + (90,), outline=col, width=3)
    d.rectangle([x + 130 * s, y - 4 * s, x + 170 * s, y + 4 * s], fill=col)
    d.rectangle([x - 30 * s, y - 4 * s, x, y + 4 * s], fill=col); d.rectangle([x - 36 * s, y - 18 * s, x - 30 * s, y + 18 * s], fill=col)

def magnifier(d, c, r=60, col=GOLD):
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 25), outline=col, width=8)
    d.line([(x + r * .7, y + r * .7), (x + r * 1.6, y + r * 1.6)], fill=col, width=14)

def padlock(d, c, s=1.0, col=GOLD):
    x, y = c
    d.rounded_rectangle([x - 34 * s, y - 6 * s, x + 34 * s, y + 46 * s], 8, fill=col + (230,))
    d.line([(x - 22 * s, y - 6 * s), (x - 22 * s, y - 30 * s), (x - 10 * s, y - 44 * s), (x + 10 * s, y - 44 * s), (x + 22 * s, y - 30 * s), (x + 22 * s, y - 6 * s)], fill=col, width=int(8 * s) or 1)
    d.ellipse([x - 7 * s, y + 10 * s, x + 7 * s, y + 24 * s], fill=(60, 50, 30))

def clock(d, c, r=40, col=GOLD, hour=2):
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], fill=(20, 30, 45, 200), outline=col, width=4)
    a = -math.pi / 2 + hour / 12 * 6.283
    d.line([(x, y), (x + r * .5 * math.cos(a), y + r * .5 * math.sin(a))], fill=col, width=4)
    d.line([(x, y), (x, y - r * .75)], fill=col, width=3)

def bars(d, F, bx, data, maxv=None, col=BLUE, size=22):
    """Bar chart. data = [(label_en, label_zh_or_None, value, color_or_None, value_text_or_None)]. No axis numbers."""
    x0, y0, x1, y1 = bx; n = len(data); maxv = maxv or max(abs(v[2]) for v in data) or 1
    bw = (x1 - x0) / n * .55
    d.line([(x0, y1), (x1, y1)], fill=GREY, width=2)
    for i, (le, lz, v, c, vt) in enumerate(data):
        cx = x0 + (x1 - x0) * (i + .5) / n; h = (y1 - y0 - 40) * abs(v) / maxv
        d.rounded_rectangle([cx - bw / 2, y1 - h, cx + bw / 2, y1], 8, fill=(c or col) + (210,))
        if vt: T(d, F, (cx, y1 - h - 20), vt, size, WHITE)
        T(d, F, (cx, y1 + 24), le, size - 2, WHITE)
        if lz: T(d, F, (cx, y1 + 50), lz, size - 4, GREY)

def linechart(d, F, bx, series, xt=(), size=20):
    """series = [(label, color, [y values 0..1])]; xt = x tick labels. No y numbers."""
    x0, y0, x1, y1 = bx
    d.line([(x0, y1), (x1, y1)], fill=GREY, width=2); d.line([(x0, y0), (x0, y1)], fill=GREY, width=2)
    for j, t in enumerate(xt): T(d, F, (x0 + (x1 - x0) * (j + .5) / len(xt), y1 + 22), t, size, GREY)
    for k, (lab, c, ys) in enumerate(series):
        pts = [(x0 + (x1 - x0) * (j + .5) / len(ys), y1 - (y1 - y0) * v) for j, v in enumerate(ys)]
        d.line(pts, fill=c, width=5)
        for p in pts: d.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=c)
        T(d, F, (pts[-1][0] + 16, pts[-1][1] - 4), lab, size, c, 'lm')

def umap(d, F, clusters, seed=9):
    """clusters = [(cx, cy, R, color, label, n_points)]."""
    rnd = random.Random(seed)
    for cx, cy, R, c, lab, n in clusters:
        for _ in range(n):
            a = rnd.uniform(0, 6.28); r = R * math.sqrt(rnd.uniform(0, 1))
            x, y = cx + r * math.cos(a), cy + r * math.sin(a) * .75
            d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=c + (200,))
        if lab: T(d, F, (cx, cy + R * .75 + 26), lab, 22, c)

def node(d, F, c, r, col, en, zh=None, size=24):
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=col + (70,), outline=col, width=4)
    label(d, F, c, en, zh, size)

def corkcard(d, F, bx, en=None, zh=None, col=(240, 230, 200), size=24, pin=RED):
    x0, y0, x1, y1 = bx
    d.rounded_rectangle(bx, 8, fill=col + (235,))
    d.ellipse([(x0 + x1) / 2 - 10, y0 - 6, (x0 + x1) / 2 + 10, y0 + 14], fill=pin)
    if en: T(d, F, ((x0 + x1) / 2, (y0 + y1) / 2 - (16 if zh else 0)), en, size, (40, 40, 50))
    if zh: T(d, F, ((x0 + x1) / 2, (y0 + y1) / 2 + 20), zh, size - 2, (90, 80, 70))

def human(d, c, s=1.0, col=(200, 205, 215)):
    x, y = c
    d.ellipse([x - 22 * s, y - 100 * s, x + 22 * s, y - 56 * s], fill=col)
    d.rounded_rectangle([x - 34 * s, y - 50 * s, x + 34 * s, y + 30 * s], 20, fill=col)
    d.line([(x - 16 * s, y + 30 * s), (x - 20 * s, y + 100 * s)], fill=col, width=int(16 * s)); d.line([(x + 16 * s, y + 30 * s), (x + 20 * s, y + 100 * s)], fill=col, width=int(16 * s))
    d.line([(x - 34 * s, y - 40 * s), (x - 56 * s, y + 20 * s)], fill=col, width=int(13 * s)); d.line([(x + 34 * s, y - 40 * s), (x + 56 * s, y + 20 * s)], fill=col, width=int(13 * s))

def child(d, c, s=1.0):
    human(d, c, s * .7, (215, 205, 190))

def bench_card(d, F, title, rows):
    """Lab-notebook card like Ep1. rows = [(en, zh)] up to 4."""
    d.rounded_rectangle([160, 140, 1760, 680], 24, fill=(230, 225, 205, 22), outline=(200, 190, 150), width=2)
    for yy in range(250, 670, 95): d.line([(200, yy + 46), (1720, yy + 46)], fill=(200, 190, 150, 40), width=1)
    T(d, F, (W / 2, 195), title, 36, GOLD)
    for i, (a, b) in enumerate(rows):
        if not a: continue
        y = 280 + i * 95
        d.ellipse([240, y - 14, 268, y + 14], fill=(70, 120, 200))
        T(d, F, (300, y), a, 30, WHITE, 'lm'); T(d, F, (1060, y), b, 28, GREY, 'lm')

def refs_two_col(d, F, refs, top=196, bottom=700):
    """Fit all references (wrapped) in one or two columns, auto-shrinking the font."""
    T(d, F, (W / 2 - 80, 140), "References", 44, GOLD, font='title'); T(d, F, (W / 2 + 120, 142), "参考文献", 40, GOLD)
    ncol = 2 if len(refs) > 10 else 1; colw = 820 if ncol == 2 else 1640
    def wrap(s, size):
        out, cur = [], ''
        for w in s.split(' '):
            tt = (cur + ' ' + w) if cur else w
            if d.textlength(tt, F('sans', size)) <= colw: cur = tt
            else: out.append(cur); cur = '   ' + w
        if cur: out.append(cur)
        return out
    for size in range(24, 11, -1):
        lh = int(size * 1.28); blocks = [wrap(f"{i+1}. {r}", size) for i, r in enumerate(refs)]
        tot = sum(len(b) * lh + 4 for b in blocks)
        if tot / ncol <= (bottom - top) * 0.97: break
    x, y, col = 110 if ncol == 2 else 140, top, 0; limit = tot / ncol
    used = 0
    for b in blocks:
        if ncol == 2 and col == 0 and used + len(b) * lh > limit + lh:
            col = 1; x = 110 + 870; y = top
        for ln in b:
            d.text((x, y), ln, font=F('sans', size), fill=(225, 230, 240)); y += lh; used += lh
        y += 4; used += 4
