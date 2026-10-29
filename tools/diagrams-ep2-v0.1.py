from prims import *
"""Episode 2 'The Guardians' scene drawings. Each scene f(st, im, d, F, M) draws step st (steps build).
Canvas: logical 1920x1080, diagram area y 120..690, REF card zone x>1150 y 698-742 kept clear."""
import math, random, re
from PIL import Image as _Img, ImageDraw as _IDraw
CUR = {'im': None}

BG = (16, 26, 46)
LAM = (110, 215, 200)          # basal lamina (laminin) line
PAXB = (70, 125, 235)          # PAX7 badge / nucleus blue
MYO = (150, 235, 165)          # myoblast (light green)
NUC = (80, 80, 175)            # myonucleus


# ---------------- helpers ----------------
def mu(c, k=0.42):
    """Mute colour c toward the background (k = share of original kept)."""
    return tuple(int(v * k + b * (1 - k)) for v, b in zip(c[:3], BG))


def L2(d, F, xy, en, zh=None, size=28, col=WHITE, zcol=GREY, anchor='mm', zs=None, gap=None):
    """EN line with ZH line under it; xy is the centre between them."""
    x, y = xy
    if not zh:
        T(d, F, xy, en, size, col, anchor); return
    zs = zs or int(size * 0.86)
    g = gap or (size + zs) * 0.6
    T(d, F, (x, y - g / 2), en, size, col, anchor)
    T(d, F, (x, y + g / 2), zh, zs, zcol, anchor)


def wrap(d, F, s, size, maxw):
    toks = re.findall(r'[\u2e80-\u9fff\uff00-\uffef\u3000-\u303f]|[^\s\u2e80-\u9fff\uff00-\uffef\u3000-\u303f]+|\s+', s)
    lines, cur = [], ''
    for t in toks:
        if t.isspace():
            if cur: cur += ' '
            continue
        tt = cur + t
        if d.textlength(tt.strip(), F('sans', size)) <= maxw or not cur.strip():
            cur = tt
        else:
            lines.append(cur.strip()); cur = t
    if cur.strip(): lines.append(cur.strip())
    return lines


def para(d, F, x, y, s, size, col, maxw, anchor='mm', lh=1.32):
    """Wrapped paragraph; first line centred at y. Returns y after last line."""
    for ln in wrap(d, F, s, size, maxw):
        T(d, F, (x, y), ln, size, col, anchor); y += size * lh
    return y


def blend(a, b, t):
    return tuple(int(x * (1 - t) + y * t) for x, y in zip(a[:3], b[:3]))


def soft(d, fn):
    """Draw fn(proxy) on a transparent layer and alpha-composite it (true translucency over shapes)."""
    im = CUR['im']
    if im is None:
        fn(d); return
    tmp = _Img.new('RGBA', im.size, (0, 0, 0, 0))
    fn(type(d)(_IDraw.Draw(tmp, 'RGBA')))
    im.alpha_composite(tmp)


def glow(d, c, r, col, a=50, n=5, sy=1.0):
    soft(d, lambda dd: _glow(dd, c, r, col, a, n, sy))


def _glow(d, c, r, col, a=50, n=5, sy=1.0):
    for k in range(n, 0, -1):
        rr = r * (0.5 + 0.5 * k / n)
        d.ellipse([c[0] - rr, c[1] - rr * sy, c[0] + rr, c[1] + rr * sy], fill=col + (int(a / n),))


def lfib(d, x0, x1, y, h, col=ROSE, nuclei=(), alpha=225, striate=True, outline=None, nuc_col=NUC, nuc_w=None):
    """Longitudinal muscle fiber (pill) with optional striations and myonuclei at x positions."""
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], h / 2, fill=col + (alpha,), outline=outline or tuple(min(255, v + 45) for v in col), width=3)
    if striate:
        for x in range(int(x0 + h * .45), int(x1 - h * .45), 18):
            d.line([(x, y - h / 2 + 7), (x, y + h / 2 - 7)], fill=blend(col, (70, 25, 40), .22), width=2)
    nw = nuc_w or max(14, h * .32)
    for x in nuclei:
        d.ellipse([x - nw, y - nw * .42, x + nw, y + nw * .42], fill=nuc_col + (235,), outline=(170, 170, 235), width=2)


def sc(d, F, c, s=1.0, pax=False, badge=False, glow_=False, dim=False, col=GREEN):
    """Satellite cell (green spindle). pax -> blue nucleus; badge -> 'PAX7' tag above."""
    x, y = c
    if glow_: glow(d, c, 70 * s, col, 70, 6, .55)
    cc = mu(col, .55) if dim else col
    w, h = 52 * s, 24 * s
    d.ellipse([x - w, y - h, x + w, y + h], fill=cc + (230,), outline=tuple(min(255, v + 70) for v in cc), width=3)
    nc = (PAXB if pax else (30, 90, 50))
    if dim: nc = mu(nc, .6)
    d.ellipse([x - w * .42, y - h * .52, x + w * .42, y + h * .52], fill=nc)
    if badge:
        pill(d, F, (x, y - h - 26), "PAX7", PAXB, 20, 12)


def rcell(d, c, r, fill=(60, 90, 130), nucfill=(40, 55, 90), outline=None, nuc=True):
    """Opaque round cell with soft highlight (no alpha punch-through)."""
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline or tuple(min(255, v + 70) for v in fill), width=3)
    for k in range(1, 7):
        rr = r * (1 - k / 8) - 2; ox, oy = -r * .16 * k / 6, -r * .2 * k / 6
        d.ellipse([x + ox - rr, y + oy - rr, x + ox + rr, y + oy + rr], fill=blend(fill, (255, 255, 255), .035 * k))
    if nuc:
        d.ellipse([x - r * .45, y - r * .45, x + r * .45, y + r * .45], fill=nucfill, outline=blend(nucfill, (255, 255, 255), .35), width=2)


def wrench(d, c, s=1.0, col=GOLD, ang=-0.7):
    x, y = c; ca, sa = math.cos(ang), math.sin(ang)
    a = (x - ca * 50 * s, y - sa * 50 * s); b = (x + ca * 40 * s, y + sa * 40 * s)
    d.line([a, b], fill=col, width=int(14 * s))
    hx, hy = b[0] + ca * 14 * s, b[1] + sa * 14 * s; r = 24 * s
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=col)
    px, py = -sa, ca; hw = 9 * s                       # open jaw slot
    p0 = (hx - ca * 2 * s, hy - sa * 2 * s); p1 = (hx + ca * 30 * s, hy + sa * 30 * s)
    d.polygon([(p0[0] + px * hw, p0[1] + py * hw), (p1[0] + px * hw, p1[1] + py * hw), (p1[0] - px * hw, p1[1] - py * hw), (p0[0] - px * hw, p0[1] - py * hw)], fill=BG + (255,))
    d.ellipse([p0[0] - hw, p0[1] - hw, p0[0] + hw, p0[1] + hw], fill=BG + (255,))
    d.ellipse([a[0] - 8 * s, a[1] - 8 * s, a[0] + 8 * s, a[1] + 8 * s], fill=col)


def bolt(d, c, s=1.0, col=GOLD):
    x, y = c
    pts = [(x + 6 * s, y - 34 * s), (x - 16 * s, y + 4 * s), (x - 2 * s, y + 4 * s), (x - 8 * s, y + 34 * s), (x + 16 * s, y - 6 * s), (x + 2 * s, y - 6 * s)]
    glow(d, c, 34 * s, col, 60, 4)
    d.polygon(pts, fill=col)


def star(d, c, r=12, col=GOLD):
    x, y = c
    d.polygon([(x, y - r), (x + r * .3, y - r * .3), (x + r, y), (x + r * .3, y + r * .3), (x, y + r), (x - r * .3, y + r * .3), (x - r, y), (x - r * .3, y - r * .3)], fill=col)


def xsec2(d, c, R=130, mode='regen', seed=7, step3=False):
    """Cross-section. mode: 'normal' | 'regen' (central nuclei) | 'empty' (failed regeneration)
    | 'pale' (no new fibers) | 'few' (sparse new fibers) | 'grey' (atrophic & stiff)."""
    rnd = random.Random(seed); x, y = c
    d.ellipse([x - R - 14, y - R - 14, x + R + 14, y + R + 14], fill=(60, 40, 50, 130), outline=(200, 160, 170), width=3)
    sp = R * 2 / 5.2; cents = []
    for row in range(-6, 7):
        for col in range(-6, 7):
            px = x + (col + (row % 2) * .5) * sp + rnd.uniform(-sp * .07, sp * .07); py = y + row * sp * .866 + rnd.uniform(-sp * .07, sp * .07)
            if math.dist((px, py), c) < R - sp * .45: cents.append((px, py))
    fr = sp * .45
    if mode == 'empty':
        d.ellipse([x - R, y - R, x + R, y + R], fill=(30, 26, 40, 200))
        for i, p in enumerate(cents):
            if i % 5 == 0:
                r = fr * .45; d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=mu(ROSE, .5) + (200,))
            elif i % 3 == 0:
                q = (p[0] + rnd.uniform(-8, 8), p[1] + rnd.uniform(-8, 8)); d.ellipse([q[0] - 3, q[1] - 3, q[0] + 3, q[1] + 3], fill=(140, 120, 130))
        if step3:
            rs = random.Random(seed + 3)
            for k in range(9):                       # connective tissue strands
                yy = y - R * .8 + k * R * .2; half = math.sqrt(max(0, R * R * .85 - (yy - y) ** 2))
                ph = rs.uniform(0, 6)
                pts = [(xx, yy + 5 * math.sin(ph + xx / 18)) for xx in range(int(x - half), int(x + half), 6)]
                if len(pts) > 1: d.line(pts, fill=ICE + (170,), width=3)
            fat(d, (x - R * .38, y - R * .32), 5, R * .2, seed=2)
            fat(d, (x + R * .42, y + R * .3), 5, R * .2, seed=5)
            fat(d, (x + R * .3, y - R * .5), 3, R * .12, seed=8)
            for k, (dx, dy) in enumerate([(-.45, .38), (.05, .05), (.55, -.1), (-.1, .6)]):
                macrophage(d, (x + dx * R, y + dy * R), .38, seed=k + 2)
        return cents
    if mode == 'grey':
        d.ellipse([x - R, y - R, x + R, y + R], fill=ICE + (110,))
    for i, p in enumerate(cents):
        if mode == 'pale':
            r = fr * .9; d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=mu(ROSE, .55) + (220,), outline=mu((240, 150, 160), .6), width=2)
            continue
        if mode == 'few' and i % 3:
            r = fr * .85; d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=mu(ROSE, .45) + (200,)); continue
        if mode == 'grey':
            r = fr * .62; d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(140, 125, 132, 235), outline=(190, 180, 190), width=2); continue
        r = fr * (rnd.uniform(.78, .98) if mode in ('regen', 'few') else .95)
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=ROSE + (235,), outline=(240, 150, 160), width=3)
        if mode in ('regen', 'few'):
            n = max(3, r * .26); d.ellipse([p[0] - n, p[1] - n, p[0] + n, p[1] + n], fill=(70, 70, 160))
        else:
            d.ellipse([p[0] + r * .5, p[1] - r * .2, p[0] + r * .8, p[1] + r * .1], fill=(70, 70, 150))
    return cents


def fiber_dish(d, c, w=230, cells=0, cluster=False, empty_x=False):
    """Single isolated fiber floating in a dish, with satellite-cell progeny."""
    x, y = c
    d.ellipse([x - w / 2, y - w * .2, x + w / 2, y + w * .2], fill=(180, 210, 230, 40), outline=(200, 225, 240), width=3)
    lfib(d, x - w * .36, x + w * .36, y, 18, striate=False, nuclei=[x - w * .2, x, x + w * .2], nuc_w=7)
    pos = [(x - w * .12, y - 22), (x + w * .16, y + 22)]
    for p in pos[:cells]:
        d.ellipse([p[0] - 9, p[1] - 9, p[0] + 9, p[1] + 9], fill=GREEN + (230,))
    if cluster:
        rnd = random.Random(5)
        for k in range(14):
            a = rnd.uniform(0, 6.28); r = rnd.uniform(0, 30)
            px, py = x + w * .08 + r * math.cos(a) * 1.6, y - 30 + r * math.sin(a) * .55
            d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=GREEN + (230,), outline=(190, 255, 200), width=1)


def house(d, c, s=1.0, col=(170, 180, 200), ruined=False):
    x, y = c
    if ruined:
        for (dx, dy, w_, h_, a) in [(-40, 30, 60, 18, .3), (10, 34, 70, 16, -.2), (-10, 12, 50, 14, .8), (34, 14, 30, 30, 0)]:
            ca, sa = math.cos(a), math.sin(a); cx, cy = x + dx * s, y + dy * s
            pts = [(-w_ / 2, -h_ / 2), (w_ / 2, -h_ / 2), (w_ / 2, h_ / 2), (-w_ / 2, h_ / 2)]
            d.polygon([(cx + (px * ca - py * sa) * s, cy + (px * sa + py * ca) * s) for px, py in pts], fill=mu(col, .7) + (230,), outline=col)
        d.line([(x - 55 * s, y + 45 * s), (x + 60 * s, y + 45 * s)], fill=GREY, width=3)
        return
    d.rectangle([x - 55 * s, y - 20 * s, x + 55 * s, y + 45 * s], fill=col + (60,), outline=col, width=3)
    d.polygon([(x - 70 * s, y - 18 * s), (x, y - 70 * s), (x + 70 * s, y - 18 * s)], fill=col + (90,), outline=col)
    d.rectangle([x - 14 * s, y + 8 * s, x + 14 * s, y + 45 * s], fill=BG + (255,), outline=col, width=2)


def dial(d, F, c, r=46, frac=0.5, col=GOLD):
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], fill=(24, 36, 60, 230), outline=col, width=4)
    for k in range(9):
        a = math.pi * (0.75 + 1.5 * k / 8)
        d.line([(x + r * .72 * math.cos(a), y + r * .72 * math.sin(a)), (x + r * .88 * math.cos(a), y + r * .88 * math.sin(a))], fill=col + (180,), width=2)
    a = math.pi * (0.75 + 1.5 * frac)
    d.line([(x, y), (x + r * .66 * math.cos(a), y + r * .66 * math.sin(a))], fill=WHITE, width=5)
    d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=col)


def tag(d, F, c, kind, size=20):
    names = {'FACT': 'FACT 事实', 'ASSOCIATION': 'ASSOCIATION 关联', 'HYPOTHESIS': 'HYPOTHESIS 假说'}
    t = names[kind]; col = SCOL[kind]
    tw = d.textlength(t, F('sans', size))
    d.rounded_rectangle([c[0], c[1] - size * .85, c[0] + tw + 28, c[1] + size * .85], size * .85, fill=col + (235,))
    T(d, F, (c[0] + 14, c[1]), t, size, WHITE, 'lm')


def ecard(d, F, bx, kind, en, zh, cite, en_size=22, zh_size=21):
    """Evidence-board card with coloured tag, EN text, ZH text and citation."""
    x0, y0, x1, y1 = bx; col = SCOL[kind]
    d.rounded_rectangle([x0 + 6, y0 + 8, x1 + 6, y1 + 8], 14, fill=(0, 0, 0, 70))
    d.rounded_rectangle(bx, 14, fill=(28, 38, 60, 245), outline=col + (230,), width=3)
    d.ellipse([(x0 + x1) / 2 - 9, y0 - 9, (x0 + x1) / 2 + 9, y0 + 9], fill=RED)
    tag(d, F, (x0 + 18, y0 + 34), kind)
    y = y0 + 78
    y = para(d, F, x0 + 20, y, en, en_size, WHITE, x1 - x0 - 36, 'lm', 1.28)
    y = para(d, F, x0 + 20, y + 2, zh, zh_size, GREY, x1 - x0 - 36, 'lm', 1.28)
    T(d, F, (x0 + 20, y1 - 24), cite, 20, (130, 145, 170), 'lm')


# ---------------- scenes ----------------
def s_recap(st, im, d, F, M):
    fy, fx0, fx1, fh = 290, 220, 1700, 130
    cells_x = [560, 820, 1080, 1340, 1600]
    # gold armour sheen + fiber
    d.rounded_rectangle([fx0 - 8, fy - fh / 2 - 8, fx1 + 8, fy + fh / 2 + 8], fh / 2 + 8, outline=GOLD + (120,), width=6)
    lfib(d, fx0, fx1, fy, fh, nuclei=range(330, 1650, 160), nuc_w=26, nuc_col=(120, 120, 215))
    d.line([(fx0 + 60, fy - fh / 2 + 14), (fx1 - 60, fy - fh / 2 + 14)], fill=blend(ROSE, (255, 230, 200), .35), width=4)
    soft(d, lambda dd: [_glow(dd, (x, fy), 40, (200, 200, 255), 90, 4, .55) for x in range(330, 1650, 160)])
    # faint beam already passed through
    soft(d, lambda dd: (dd.line([(640, 130), (960, 386)], fill=(255, 255, 255, 45), width=16), dd.line([(640, 130), (960, 386)], fill=(255, 255, 255, 170), width=3)))
    L2(d, F, (330, 160), "Fiber survives", "纤维存活", 30, GREEN, GREY)
    if st in (1, 2):
        darrow(d, (400, 368), (400, 438), GREY, 3, 12, 10)
        xsec2(d, (400, 565), 100, 'grey', seed=4)
        L2(d, F, (535, 560), "Years later: thin + stiff", "多年后：变细、变硬", 28, ORANGE, GREY, 'lm')
    if st == 2:
        for x in cells_x: sc(d, F, (x, 212), .8, pax=True, badge=True, glow_=True)
        wrench(d, (1180, 520), 1.0, GREEN)
        L2(d, F, (1180, 625), "repair well", "修复好", 24, GREEN, GREY)
        T(d, F, (1400, 530), "?", 110, GOLD, font='title')
        for i in range(5):
            x = 1555 + i * 42
            if i < 2: d.ellipse([x - 16, 510, x + 16, 542], fill=PAXB + (230,))
            else: d.ellipse([x - 16, 510, x + 16, 542], outline=PAXB + (int(200 - i * 45),), width=3)
        L2(d, F, (1640, 625), "ranks empty?", "队伍为何空了？", 24, PAXB, GREY)
    if st == 3:
        for x in (560, 1080): sc(d, F, (x, 212), .8, pax=True, badge=True)
        mito(d, (1420, 300), 150, 64, sparks=0)
        d.line([(1500, 182), (1450, 262)], fill=GREY, width=2)
        L2(d, F, (1570, 162), "mitochondria", "线粒体", 24, (240, 150, 110), GREY)
        # shadowy neighbours step forward
        for (c, r) in [((400, 500), 90), ((760, 500), 90), ((1150, 500), 140), ((1540, 500), 110)]:
            glow(d, c, r, (0, 0, 0), 90, 5, .7)
        fap(d, (400, 495), 1.4)
        L2(d, F, (400, 600), "FAP", "成纤维-成脂祖细胞", 26, ORANGE, GREY, zs=20)
        macrophage(d, (760, 495), 1.0, seed=3)
        L2(d, F, (760, 600), "macrophage", "巨噬细胞", 26, PURPLE, GREY)
        vessel(d, 1010, 1290, 495, 52)
        L2(d, F, (1150, 600), "vessel", "血管", 26, RED, GREY)
        rnd = random.Random(8)
        for k in range(9):
            a = k / 9 * 6.28; px, py = 1540 + 62 * math.cos(a), 495 + 34 * math.sin(a)
            r = 34 + rnd.uniform(-6, 8); d.ellipse([px - r, py - r * .8, px + r, py + r * .8], fill=ICE + (50,))
        d.ellipse([1470, 455, 1610, 535], fill=ICE + (60,))
        T(d, F, (1540, 495), "TGF-β", 30, ICE)
        T(d, F, (W / 2, 668), "The neighbors turn  邻居变脸  →  Ep3", 30, GOLD)


def _ytop(x):
    return 400 + 18 * math.sin((x - 260) / 160)


def s_em(st, im, d, F, M):
    """Illustrated EM view (no openly licensed EM of a satellite cell was found on Wikimedia Commons)."""
    X0, Y0, X1, Y1 = 260, 140, 1240, 600
    d.rectangle([X0, Y0, X1, Y1], fill=(66, 66, 70))
    cx, half = 720, 200
    def prof(x):
        u = (x - cx) / half; return max(0.0, 1 - u * u)
    def ft(x): return _ytop(x) + 10 * prof(x)
    top = [(x, ft(x)) for x in range(X0, X1 + 1, 6)]
    d.polygon(top + [(X1, Y1), (X0, Y1)], fill=(150, 150, 153))
    for x in range(X0 + 10, X1 - 36, 68):          # sarcomeres: A bands + Z lines
        d.rectangle([x, ft(x + 17) + 12, x + 34, Y1], fill=(122, 122, 126))
        if x + 52 < X1 - 4: d.line([(x + 52, ft(x + 52) + 12), (x + 52, Y1)], fill=(78, 78, 82), width=3)
    for y in range(470, Y1, 34):              # myofibril boundaries
        d.line([(X0, y), (X1, y)], fill=(168, 168, 171), width=2)
    # satellite cell: thin rim of cytoplasm, large heterochromatic nucleus
    lens_top = [(x, _ytop(x) - 64 * prof(x) ** 0.7) for x in range(cx - half, cx + half + 1, 5)]
    lens_bot = [(x, ft(x)) for x in range(cx + half, cx - half - 1, -5)]
    d.polygon(lens_top + lens_bot, fill=(184, 184, 186), outline=(212, 212, 215))
    nx, ny = cx - 6, _ytop(cx) - 24
    d.ellipse([nx - 118, ny - 30, nx + 118, ny + 30], fill=(42, 42, 46))
    d.ellipse([nx - 104, ny - 21, nx + 104, ny + 21], fill=(84, 84, 88))
    rnd = random.Random(3)
    for _ in range(24):
        a = rnd.uniform(0, 6.28); px, py = nx + 100 * math.cos(a), ny + 22 * math.sin(a)
        d.ellipse([px - 8, py - 5, px + 8, py + 5], fill=(38, 38, 42))
    for _ in range(9):
        px, py = nx + rnd.uniform(-70, 70), ny + rnd.uniform(-10, 10)
        d.ellipse([px - 5, py - 4, px + 5, py + 4], fill=(56, 56, 60))
    d.ellipse([nx + 24, ny - 8, nx + 42, ny + 8], fill=(30, 30, 32))
    # basal lamina over cell and fiber
    bl = [(x, (_ytop(x) - 64 * prof(x) ** 0.7 if abs(x - cx) < half else _ytop(x)) - 9) for x in range(X0, X1 + 1, 5)]
    d.line(bl, fill=(36, 36, 40), width=4)
    for _ in range(150):                      # collagen fibril cross-sections
        px, py = rnd.uniform(X0 + 8, X1 - 8), rnd.uniform(Y0 + 8, 320)
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(84, 84, 89))
    def grain(dd):
        g = random.Random(11)
        for _ in range(3000):
            px, py = g.uniform(X0, X1 - 2), g.uniform(Y0, Y1 - 2); v = g.choice([20, 200])
            dd.rectangle([px, py, px + 1.5, py + 1.5], fill=(v, v, v, 26))
    soft(d, grain)
    d.rounded_rectangle([X0 - 10, Y0 - 10, X1 + 10, Y1 + 10], 16, outline=GOLD + (200,), width=2)
    d.rounded_rectangle([X1 - 250, Y1 - 52, X1 - 14, Y1 - 14], 10, fill=(20, 24, 34))
    T(d, F, (X1 - 132, Y1 - 33), "muscle fiber  肌纤维", 22, WHITE)
    T(d, F, ((X0 + X1) / 2, 640), "Mauro 1961 · frog tibialis anticus  青蛙胫前肌", 26, WHITE)
    T(d, F, ((X0 + X1) / 2, 675), "electron microscope view, illustrated  电子显微镜视野（示意图）", 21, GREY)
    if st >= 1:
        d.ellipse([cx - 235, _ytop(cx) - 120, cx + 235, _ytop(cx) + 55], outline=GOLD, width=5)
        arrow(d, (1335, 280), (nx + 70, ny - 12), GOLD, 4, 16)
        L2(d, F, (1355, 280), "large nucleus", "核大", 30, WHITE, GOLD, 'lm')
        tx = cx + 165
        arrow(d, (1335, 470), (tx + 4, ft(tx) - 6), GOLD, 4, 16)
        L2(d, F, (1355, 470), "little cytoplasm", "胞质少", 30, WHITE, GOLD, 'lm')


def s_niche(st, im, d, F, M):
    ft, fb = 360, 580; cx = 960
    def p(x):
        if st < 2: return 0.0
        u = (x - cx) / 170; return max(0.0, 1 - u * u)
    xs = list(range(100, 1821, 8))
    top = [(x, ft + 12 * p(x)) for x in xs]
    # sleeve fill + fiber
    d.polygon([(x, ft - 20 - 48 * p(x)) for x in xs] + [(x, fb + 20) for x in reversed(xs)], fill=LAM + (28,))
    d.polygon(top + [(x, fb) for x in reversed(xs)], fill=ROSE + (215,))
    for x in range(130, 1800, 20):
        d.line([(x, ft + 12 * p(x) + 8), (x, fb - 8)], fill=(230, 120, 135, 60), width=2)
    for x in range(260, 1800, 260):
        if abs(x - cx) < 60: continue
        d.ellipse([x - 38, 470 - 15, x + 38, 470 + 15], fill=NUC + (235,), outline=(170, 170, 235), width=2)
    # basal lamina (outer sleeve)
    d.line([(x, ft - 20 - 48 * p(x)) for x in xs], fill=LAM, width=5)
    d.line([(x, fb + 20) for x in xs], fill=LAM, width=5)
    d.line([(420, 236), (420, 336)], fill=LAM, width=2); d.ellipse([413, 333, 427, 347], fill=LAM)
    L2(d, F, (420, 196), "basal lamina / basement membrane", "基底膜（基板）", 28, LAM, GREY)
    if st >= 1:
        d.line(top, fill=(255, 195, 205), width=4)
        d.line([(x, fb) for x in xs], fill=(255, 195, 205), width=4)
        d.line([(420, 584), (420, 622)], fill=(255, 195, 205), width=2); d.ellipse([413, 573, 427, 587], fill=(255, 195, 205))
        L2(d, F, (420, 650), "sarcolemma (fiber membrane)", "肌膜", 26, (255, 195, 205), GREY)
    if st >= 2:
        glow(d, (cx, 345), 200, GREEN, 70, 6, .35)
        lt = [(x, ft - 48 * p(x)) for x in range(cx - 170, cx + 171, 5)]
        lb = [(x, ft + 12 * p(x)) for x in range(cx + 170, cx - 171, -5)]
        d.polygon(lt + lb, fill=GREEN + (235,), outline=(170, 255, 190))
        nuc = PAXB if st >= 3 else (30, 90, 50)
        d.ellipse([cx - 80, 340 - 17, cx + 80, 340 + 17], fill=nuc)
        d.line([(x, ft - 20 - 48 * p(x)) for x in range(cx - 200, cx + 201, 6)], fill=LAM, width=5)
        # shield icon + label
        sx, sy = 770, 196
        d.polygon([(sx - 16, sy - 20), (sx + 16, sy - 20), (sx + 16, sy + 2), (sx, sy + 22), (sx - 16, sy + 2)], fill=GREEN + (90,), outline=GREEN)
        L2(d, F, (cx + 20, 196), "satellite cell", "卫星细胞", 32, GREEN, GREY)
        d.line([(cx, 240), (cx, 286)], fill=GREEN, width=2)
        L2(d, F, (1440, 650), "inside the sleeve, outside the fiber", "袖套之内，纤维之外", 26, WHITE, GREY)
    if st >= 3:
        pill(d, F, (cx + 205, 296), "PAX7", PAXB, 24, 14)
        L2(d, F, (1500, 196), "PAX7 = master gene switch", "总开关 · the badge 徽章", 28, PAXB, GREY)


def s_ablation(st, im, d, F, M):
    if st == 0:
        T(d, F, (W / 2, 170), "Required?   是否必需？", 42, GOLD)
        d.line([(960, 262), (960, 600)], fill=(170, 175, 190), width=10)
        d.polygon([(880, 630), (1040, 630), (1000, 600), (920, 600)], fill=(170, 175, 190))
        d.line([(560, 262), (1360, 262)], fill=(200, 205, 215), width=8)
        d.ellipse([946, 248, 974, 276], fill=GOLD)
        for x in (560, 1360):
            d.line([(x, 262), (x - 100, 400)], fill=GREY, width=2); d.line([(x, 262), (x + 100, 400)], fill=GREY, width=2)
            d.chord([x - 115, 360, x + 115, 440], 0, 180, fill=(170, 175, 190, 200)) if hasattr(d, 'chord') else d.ellipse([x - 115, 392, x + 115, 416], fill=(170, 175, 190, 220))
        sc(d, F, (560, 370), 1.1, pax=True, glow_=True)
        for (x, y, col) in [(1305, 372, (150, 150, 165)), (1362, 366, (175, 140, 140)), (1418, 374, (140, 160, 175))]:
            rcell(d, (x, y), 24, fill=col, nucfill=(70, 70, 85))
        L2(d, F, (560, 480), "Suspect  嫌疑人", "satellite cell 卫星细胞", 30, WHITE, GREEN, zs=24)
        L2(d, F, (1360, 480), "Other candidates  其他候选", "cells from other origins 其他来源细胞", 30, WHITE, GREY, zs=24)
        return
    # steps 1-3: logic boxes, results, aftermath
    bx = [(200, 640, "Remove Pax7+ cells", "清除 Pax7+ 细胞", GREEN), (740, 1180, "Injure muscle", "损伤肌肉", RED), (1280, 1720, "Regeneration?", "再生？", GOLD)]
    for i, (a, b, t, z, c) in enumerate(bx):
        box(d, F, a, 150, b, 250, t, z, c, 28)
        if i < 2: arrow(d, (b + 10, 200), (bx[i + 1][0] - 10, 200), WHITE, 4, 16)
    if st >= 2:
        xsec2(d, (520, 468), 128, 'regen', seed=3)
        L2(d, F, (520, 654), "control: regenerates", "对照：再生", 26, GREEN, GREY)
        xsec2(d, (1400, 468), 128, 'empty', seed=9, step3=(st >= 3))
        L2(d, F, (1400, 654), "ablated: no regeneration", "清除后：不再生", 26, RED, GREY)
        for i, (e, z) in enumerate([("Three teams", "三个团队"), ("three methods", "三种方法"), ("one verdict", "一个判决")]):
            L2(d, F, (960, 380 + i * 78), e, z, 30, GOLD, GREY, zs=24)
    if st >= 3:
        L2(d, F, (1570, 385), "fat", "脂肪", 26, YELLOW, GREY, 'lm')
        L2(d, F, (1570, 475), "inflammatory cells", "炎症细胞", 26, PURPLE, GREY, 'lm')
        L2(d, F, (1570, 565), "connective tissue", "结缔组织", 26, ICE, GREY, 'lm')
        L2(d, F, (960, 628), "fibroblasts needed too  成纤维细胞也必需", "(Murphy 2011)", 22, ORANGE, GREY, zs=20)


def s_three(st, im, d, F, M):
    T(d, F, (W / 2, 160), "Development · Sept 2011 · same issue  同一期", 30, GOLD)
    cols = [(165, 675), (715, 1225), (1265, 1775)]
    heads = [("Lepper, Partridge & Fan", "Pax7+ cell ablation  清除 Pax7+ 细胞"),
             ("Sambasivan, Tajbakhsh et al.", "Paris  巴黎"),
             ("Murphy, Kardon et al.", "Utah  犹他")]
    bullets = [[("TA injury → regeneration blocked", "胫骨前肌损伤 → 再生被阻断"), ("EDL graft → no rebuilding", "移植肌也不重建")],
               [("tissue loss, fat + inflammation", "组织丢失、脂肪与炎症"), ("rescued by Pax7+ cell transplant", "移植 Pax7+ 细胞可挽救")],
               [("SC ablation → no regenerated muscle, more connective tissue", "无再生肌、结缔组织增多"),
                ("fibroblast ablation → early differentiation, smaller fibers", "过早分化、纤维更细")]]
    for i, (x0, x1) in enumerate(cols):
        cx = (x0 + x1) / 2; on = (i == st); shown = i <= st
        k = 1.0 if on else .42
        oc = (GOLD if on else DIM)
        d.rounded_rectangle([x0, 200, x1, 675], 20, fill=(30, 42, 66, 235 if on else 150), outline=oc + (255,), width=4 if on else 2)
        T(d, F, (cx, 242), heads[i][0], 27, mu(WHITE, k) if shown else DIM)
        T(d, F, (cx, 280), heads[i][1], 21, mu(GREY, k) if shown else DIM)
        if not shown:
            T(d, F, (cx, 460), "?", 80, DIM, font='title'); continue
        # icons
        if i == 0:
            sc(d, F, (cx - 110, 360), 1.0, pax=True, dim=not on)
            arrow(d, (cx - 40, 360), (cx + 40, 360), mu(WHITE, k), 4, 14)
            sat_cell(d, (cx + 110, 360), 1.0, dead=True)
        elif i == 1:
            syringe(d, (cx - 190, 360), .85, mu((200, 220, 240), k))
            T(d, F, (cx - 120, 322), "diphtheria toxin  白喉毒素", 20, mu(GOLD, k))
            sc(d, F, (cx + 140, 362), .95, pax=True, dim=not on)
            for a in (-2.4, -1.57, -0.7):
                px, py = cx + 140 + 50 * math.cos(a), 362 + 24 * math.sin(a)
                qx, qy = cx + 140 + 64 * math.cos(a), 362 + 34 * math.sin(a)
                d.line([(px, py), (qx, qy)], fill=mu(GOLD, k), width=3)
                d.line([(qx, qy), (qx - 6, qy - 7)], fill=mu(GOLD, k), width=3); d.line([(qx, qy), (qx + 6, qy - 7)], fill=mu(GOLD, k), width=3)
            T(d, F, (cx + 140, 410), "Pax7-DTR", 20, mu(PAXB, k))
        else:
            sc(d, F, (x0 + 52, 335), .45, pax=True, dim=not on)
            fap(d, (x0 + 52, 387), .42, col=mu(ORANGE, k))
            T(d, F, (cx + 30, 335), "Pax7-CreERT2 × R26R-DTA", 22, mu(GREEN, k))
            T(d, F, (cx + 30, 387), "Tcf4-CreERT2 × R26R-DTA", 22, mu(ORANGE, k))
        y = 455
        for j, (e, z) in enumerate(bullets[i]):
            mark = (GREEN if (i == 1 and j == 1) else (RED if j == 0 else ORANGE))
            d.ellipse([x0 + 26, y - 8, x0 + 42, y + 8], fill=mu(mark, k))
            y = para(d, F, x0 + 58, y, e, 22, mu(WHITE, k), x1 - x0 - 80, 'lm', 1.28)
            y = para(d, F, x0 + 58, y + 2, z, 21, mu(GREY, k), x1 - x0 - 80, 'lm', 1.28) + 26


def s_cycle(st, im, d, F, M):
    # quiescent niche vignette
    qx, qy = 500, 440
    lfib(d, qx - 110, qx + 110, qy, 44, nuclei=[qx - 60, qx + 70], nuc_w=12)
    sc(d, F, (qx, qy - 38), .9, glow_=(st == 0))
    d.line([(qx - 115, qy - 26)] + [(qx + t, qy - 26 - 34 * max(0, 1 - (t / 70) ** 2)) for t in range(-70, 71, 6)] + [(qx + 115, qy - 26)], fill=LAM, width=4)
    L2(d, F, (372, 360), "quiescent (G0)", "静止", 30, GREEN, GREY, 'rm')
    L2(d, F, (372, 450), "most SCs not dividing", "大多不分裂", 22, WHITE, GREY, 'rm', zs=21)
    if st >= 1:
        curved(d, (560, 370), (850, 225), 60, WHITE, 4, 16)
        bolt(d, (705, 300), 1.0)
        L2(d, F, (672, 248), "injury", "损伤", 26, GOLD, GREY, 'rm')
        glow(d, (960, 215), 110, GREEN, 60, 5, .6)
        rcell(d, (918, 215), 44, fill=(60, 170, 90), nucfill=(30, 90, 50), outline=(170, 255, 190))
        rcell(d, (1004, 215), 44, fill=(60, 170, 90), nucfill=(30, 90, 50), outline=(170, 255, 190))
        L2(d, F, (1075, 215), "activated · dividing", "激活 · 分裂", 28, GREEN, GREY, 'lm')
    if st >= 2:
        curved(d, (1110, 270), (1350, 360), 50, WHITE, 4, 16)
        rnd = random.Random(2)
        for k in range(9):
            a = k / 9 * 6.28 + .3; r = 0 if k == 0 else 46
            px, py = 1430 + r * math.cos(a), 420 + r * math.sin(a) * .8
            d.ellipse([px - 22, py - 22, px + 22, py + 22], fill=MYO + (225,), outline=(210, 255, 215), width=2)
            d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=(40, 110, 60))
        L2(d, F, (1520, 420), "myoblasts", "成肌细胞", 28, MYO, GREY, 'lm')
        lfib(d, 760, 1170, 430, 70, nuclei=[820, 900, 980, 1060, 1120], nuc_w=18)
        for x in (980, 1060, 1120): glow(d, (x, 430), 26, GREEN, 70, 4, .6)
        arrow(d, (1365, 432), (1185, 432), WHITE, 4, 16)
        L2(d, F, (965, 505), "fuse: repair / new fibers", "融合：修复 / 新纤维", 26, WHITE, GREY)
    if st >= 3:
        curved(d, (1430, 490), (540, 485), -150, GREEN, 4, 18)
        sc(d, F, (985, 562), .55)
        L2(d, F, (W / 2, 640), "self-renewal · leave guardians for next time", "自我更新 · 为下次留下守护者", 28, GREEN, GREY, zs=23)


def s_quiescence(st, im, d, F, M):
    for x in (650, 1270): d.line([(x, 190), (x, 640)], fill=(90, 100, 118, 120), width=2)
    # old view
    T(d, F, (400, 168), "old view  旧观点", 26, GREY)
    c = mu((200, 205, 215), .6)
    d.rounded_rectangle([250, 375, 550, 405], 8, fill=c + (200,))
    d.line([(255, 300), (255, 470)], fill=c, width=8); d.line([(545, 340), (545, 470)], fill=c, width=8)
    d.rounded_rectangle([262, 340, 310, 372], 10, fill=mu((230, 230, 240), .5) + (220,))
    sc(d, F, (420, 352), 1.2, dim=True)
    T(d, F, (500, 290), "Z z z", 30, mu(GREY, .8))
    d.line([(255, 250), (545, 470)], fill=mu(RED, .7), width=4)
    L2(d, F, (400, 525), "dormant?", "休眠？", 30, mu(WHITE, .7), mu(GREY, .8))
    # new view
    T(d, F, (960, 168), "new view  新观点", 26, GOLD)
    rcell(d, (880, 335), 92, fill=(50, 140, 80), nucfill=(30, 90, 50), outline=(170, 255, 190))
    for (a, b, bend) in [((820, 290), (880, 255), 20), ((930, 280), (950, 345), 18), ((830, 390), (900, 410), -20), ((945, 380), (900, 405), 14)]:
        curved(d, a, b, bend, GOLD, 3, 11)
    dial(d, F, (1130, 320), 52, .72, GOLD)
    L2(d, F, (1130, 412), "poised", "蓄势待发", 24, GOLD, GREY)
    L2(d, F, (960, 530), "quiescence is actively maintained", "静止是被主动维持的", 26, WHITE, GREY)
    T(d, F, (960, 590), "(Cheung & Rando 2013)", 20, GREY)
    if st >= 1:
        T(d, F, (1520, 168), "like a fire station  像消防站", 26, ORANGE)
        bx0, bx1, by0, by1 = 1330, 1710, 260, 440
        d.polygon([(bx0 - 20, by0), (1520, 200), (bx1 + 20, by0)], fill=(150, 60, 55, 220), outline=(220, 120, 110))
        d.rectangle([bx0, by0, bx1, by1], fill=(120, 60, 60, 160), outline=(220, 120, 110), width=3)
        d.rectangle([1360, 300, 1600, by1], fill=(30, 30, 40, 230), outline=(200, 200, 210), width=2)
        # engine (parked)
        d.rounded_rectangle([1380, 352, 1560, 420], 10, fill=RED + (240,))
        d.rounded_rectangle([1510, 330, 1560, 370], 6, fill=RED + (240,))
        d.rectangle([1520, 336, 1552, 356], fill=(170, 210, 240))
        d.line([(1390, 345), (1500, 345)], fill=(220, 220, 230), width=4)
        for x in (1415, 1525): d.ellipse([x - 16, 410, x + 16, 442], fill=(30, 30, 30), outline=(150, 150, 160), width=3)
        # boots + helmet by the door
        for x in (1630, 1662):
            d.polygon([(x, 410), (x + 14, 410), (x + 14, 432), (x + 24, 440), (x, 440)], fill=GOLD)
        d.polygon([(1654 + 26 * math.cos(a), 398 - 24 * math.sin(a)) for a in [i * math.pi / 16 for i in range(17)]], fill=GOLD)
        d.rounded_rectangle([1618, 394, 1694, 404], 4, fill=GOLD)
        d.line([(1654, 376), (1654, 396)], fill=(150, 110, 40), width=3)
        # alarm bell
        d.polygon([(1505, 222), (1535, 222), (1542, 248), (1498, 248)], fill=GOLD); d.ellipse([1514, 246, 1526, 258], fill=GOLD)
        for i, (t, col) in enumerate([("ready  待命", GREEN), ("rapid activation  快速激活", ORANGE), ("reversible  可逆", BLUE)]):
            pill(d, F, (1520, 505 + i * 58), t, col, 23, 18)


def s_paradox(st, im, d, F, M):
    d.line([(960, 200), (960, 600)], fill=(90, 100, 118, 140), width=2)
    L2(d, F, (520, 175), "At rest", "静息", 34, GREEN, GREY)
    lfib(d, 270, 770, 345, 70, nuclei=[340, 460, 700], nuc_w=18)
    sc(d, F, (580, 296), 1.15, glow_=True)
    wrench(d, (420, 255), .9, GOLD, -0.5)
    T(d, F, (520, 440), "welder's tool  DNA-PKcs (NHEJ)", 26, GOLD)
    L2(d, F, (520, 510), "repairs breaks well", "修复好", 30, WHITE, GREY)
    T(d, F, (520, 590), "Vahidi Ferdousi 2014", 20, GREY)
    if st >= 1:
        L2(d, F, (1400, 175), "Dividing in culture", "培养中分裂", 34, ORANGE, GREY)
        x, y = 1215, 335
        d.ellipse([x - 150, y - 56, x + 150, y + 56], fill=(180, 210, 230, 45), outline=(200, 225, 240), width=3)
        d.ellipse([x - 132, y - 44, x + 132, y + 44], outline=(200, 225, 240, 110), width=2)
        for (px, py, pair) in [(-80, -8, 1), (-20, 14, 0), (40, -12, 1), (95, 10, 0), (-50, 24, 0), (10, -24, 0)]:
            if pair:
                for dx in (-11, 11): d.ellipse([x + px + dx - 12, y + py - 10, x + px + dx + 12, y + py + 10], fill=GREEN + (230,))
            else:
                d.ellipse([x + px - 13, y + py - 11, x + px + 13, y + py + 11], fill=GREEN + (230,))
        T(d, F, (x, 420), "satellite cells, dividing  分裂中的卫星细胞", 20, GREY)
        # bars: 0 Gy vs >=5 Gy
        base = 420; Hh = 170
        T(d, F, (1590, 222), "cell numbers  细胞数", 20, GREY)
        d.line([(1480, base), (1710, base)], fill=GREY, width=2)
        d.rounded_rectangle([1505, base - Hh, 1565, base], 8, fill=GREEN + (210,))
        d.rounded_rectangle([1625, base - Hh * .28, 1685, base], 8, fill=RED + (210,))
        T(d, F, (1655, base - Hh * .28 - 26), "≥70% fewer", 22, RED)
        T(d, F, (1535, base + 22), "0 Gy", 20, WHITE); T(d, F, (1655, base + 22), "≥5 Gy", 20, WHITE)
        for i, (t, col) in enumerate([("apoptosis  凋亡", RED), ("cycle arrest  周期停滞", ORANGE), ("ROS/RNS ↑  活性氧/氮↑", (200, 140, 40)), ("NO ↓  一氧化氮↓", BLUE)]):
            pill(d, F, (1225 + (i % 2) * 345, 495 + (i // 2) * 56), t, col, 21, 14)
        T(d, F, (1400, 590), "Caiozzo 2010 · in vitro  体外", 20, GREY)
    if st >= 2:
        d.rounded_rectangle([936, 330, 958, 430], 6, fill=(170, 175, 190))
        d.rounded_rectangle([962, 330, 984, 430], 6, fill=(170, 175, 190))
        for yy in (345, 380, 415): d.ellipse([951, yy - 9, 969, yy + 9], fill=GOLD)
        T(d, F, (W / 2, 655), "sturdy at rest, fragile when dividing   静息时结实，分裂时脆弱", 30, GOLD)


def s_heslop(st, im, d, F, M):
    # column A: protocol
    mouse(d, (310, 290), .85)
    beam(d, (215, 150), (270, 318), GOLD, 7)
    T(d, F, (300, 168), "18 Gy", 30, GOLD, 'lm')
    T(d, F, (300, 378), "normal 正常  ·  mdx", 24, WHITE)
    L2(d, F, (300, 425), "mdx = Duchenne model", "杜氏肌营养不良模型", 20, GREY, GREY, zs=20)
    if st >= 1:
        arrow(d, (455, 285), (505, 285), WHITE, 4, 14)
        T(d, F, (800, 165), "IR alone  单纯照射", 28, WHITE)
        xsec2(d, (640, 280), 75, 'pale', seed=5)
        L2(d, F, (640, 406), "no significant regeneration", "无明显再生", 22, WHITE, GREY, zs=20)
        fiber_dish(d, (965, 280), 230, cells=2)
        L2(d, F, (965, 406), "few precursors", "前体少、几乎不分裂", 22, WHITE, GREY, zs=20)
    if st >= 2:
        arrow(d, (1100, 285), (1150, 285), WHITE, 4, 14)
        syringe(d, (1200, 165), .6, (200, 220, 240))
        T(d, F, (1490, 165), "+ notexin  蛇毒毒素", 28, (200, 230, 160))
        xsec2(d, (1290, 280), 75, 'regen', seed=6)
        L2(d, F, (1290, 406), "regenerated", "再生了", 22, GREEN, GREY, zs=20)
        fiber_dish(d, (1555, 280), 230, cluster=True)
        L2(d, F, (1555, 406), "rapidly dividing precursors", "快速分裂的前体", 22, WHITE, GREY, zs=20)
        T(d, F, (1555, 452), "normal > mdx", 20, GOLD)
    if st >= 3:
        d.line([(160, 470), (1760, 470)], fill=(90, 100, 118, 160), width=2)
        pill(d, F, (300, 548), "25 Gy + notexin", (150, 120, 50), 24, 18)
        arrow(d, (440, 548), (500, 548), WHITE, 4, 14)
        xsec2(d, (575, 548), 52, 'few', seed=8)
        L2(d, F, (650, 548), "some new muscle", "少量新肌", 22, WHITE, GREY, 'lm', zs=20)
        fiber_dish(d, (1060, 548), 200, cells=0)
        L2(d, F, (1185, 548), "no dividing precursors on fibers", "纤维上无可分裂前体", 22, WHITE, GREY, 'lm', zs=20)
        for i, (t, col) in enumerate([("most radiosensitive  大多对辐射敏感", RED), ("a reserve survives  少数储备存活", GREEN), ("reserve ↓ in mdx   mdx 中储备减少", (200, 120, 40))]):
            pill(d, F, (400 + i * 560, 645), t, col, 22, 16)


def s_transplant(st, im, d, F, M):
    T(d, F, (440, 160), "Wernig 2000 · mouse soleus  小鼠比目鱼肌", 26, WHITE)
    mouse(d, (470, 300), .9)
    beam(d, (360, 190), (412, 322), GOLD, 7)
    T(d, F, (560, 215), "16 Gy X-ray", 26, GOLD, 'lm')
    syringe(d, (215, 350), .9)
    L2(d, F, (290, 410), "then donor myoblasts", "供体成肌细胞", 22, (200, 220, 240), GREY, zs=20)
    if st >= 1:
        T(d, F, (1300, 175), "soleus mass & force vs control  质量与力量（对比对照）", 22, GREY)
        x0, L = 1000, 600
        for yy in range(236, 392, 14): d.line([(x0 + L, yy), (x0 + L, yy + 7)], fill=WHITE, width=2)
        T(d, F, (x0 + L, 420), "control 对照", 20, WHITE)
        T(d, F, (x0, 228), "IR + sham  照射+假注射", 22, WHITE, 'lm')
        d.rounded_rectangle([x0, 248, x0 + L * .82, 292], 10, fill=RED + (210,))
        T(d, F, (x0 + L * .82 - 14, 270), "≈ −18%", 24, WHITE, 'rm')
        T(d, F, (x0, 328), "IR + donor cells  照射+供体细胞", 22, WHITE, 'lm')
        d.rounded_rectangle([x0, 348, x0 + L, 392], 10, fill=GREEN + (200,))
        T(d, F, (x0 + 18, 370), "deficits abolished  缺陷消除", 22, (10, 40, 20), 'lm')
    if st >= 2:
        T(d, F, (W / 2, 470), "Boldrin 2012 · when do donor SCs engraft best?  供体卫星细胞何时植入最好？", 24, GOLD)
        cols = [160, 700, 1240]
        # (a) house standing, host residents out, donors moving in
        hx = cols[0] + 140
        house(d, (hx, 580), 1.0, (170, 200, 180))
        sat_cell(d, (hx - 36, 580), .36, dead=True)
        for dx in (-128, -98):
            d.ellipse([hx + dx - 12, 628 - 10, hx + dx + 12, 628 + 10], fill=GREEN + (240,), outline=GOLD, width=2)
        arrow(d, (hx - 80, 628), (hx - 22, 618), GOLD, 3, 10)
        check(d, (hx + 62, 522), 20)
        L2(d, F, (cols[0] + 230, 560), "host SCs incapacitated", "+ niche preserved", 22, WHITE, WHITE, 'lm', zs=22)
        T(d, F, (cols[0] + 230, 615), "宿主失能 + 微环境保留", 20, GREY, 'lm')
        # (b) niche destroyed
        hx = cols[1] + 85
        house(d, (hx, 580), 1.0, (170, 160, 160), ruined=True)
        xmark(d, (hx + 60, 525), 16, RED, 6)
        L2(d, F, (cols[1] + 175, 575), "niche destroyed", "微环境被毁", 24, WHITE, GREY, 'lm')
        # (c) niche occupied
        hx = cols[2] + 85
        house(d, (hx, 580), 1.0, (170, 180, 200))
        for dx in (-30, 30): sat_cell(d, (hx + dx, 572), .35)
        xmark(d, (hx + 60, 525), 16, RED, 6)
        L2(d, F, (cols[2] + 175, 575), "niche occupied", "微环境被占", 24, WHITE, GREY, 'lm')


def s_reserve(st, im, d, F, M):
    T(d, F, (740, 150), "Who survived?  幸存者是谁？", 34, GOLD)
    lfib(d, 180, 1300, 275, 70, nuclei=range(250, 1260, 170), nuc_w=16)
    top = [(x, 229) for x in (260, 440, 620, 800, 980, 1160)]
    bot = [(x, 321) for x in (350, 530, 710, 890, 1070, 1250)]
    marked = {(1160, 229), (710, 321)}
    for p in top + bot:
        if st >= 1 and p in marked:
            sc(d, F, p, .75, glow_=True, col=MAG)
        else:
            sc(d, F, p, .75, pax=True)
    if st >= 1:
        d.line([(1352, 236), (1210, 230)], fill=MAG, width=2)
        T(d, F, (1365, 200), "Mx1-Cre marked  被标记", 26, MAG, 'lm')
        T(d, F, (1365, 242), "Pax3-high · low ROS", 24, WHITE, 'lm')
        T(d, F, (1365, 280), "Pax3 高 · 低活性氧", 22, GREY, 'lm')
    if st >= 2:
        for (x0, x1, head, hc) in [(160, 700, "ordinary injury  普通损伤", WHITE), (760, 1300, "radiation stress  辐射压力", GOLD)]:
            d.rounded_rectangle([x0, 405, x1, 685], 18, fill=(30, 42, 66, 160), outline=(90, 100, 118), width=2)
            T(d, F, ((x0 + x1) / 2, 440), head, 24, hc)
        lfib(d, 210, 650, 535, 50, nuclei=[260, 340, 420, 500, 580], nuc_w=12)
        for k, x in enumerate((240, 320, 400, 480, 560, 625)):
            sc(d, F, (x, 497), .5, pax=True)
        sc(d, F, (290, 573), .5, col=MAG)
        for k, x in enumerate((380, 470, 560)): sc(d, F, (x, 573), .5, pax=True)
        L2(d, F, (430, 640), "tiny share", "贡献很小（数量太少）", 24, WHITE, GREY, zs=20)
        lfib(d, 810, 1250, 535, 50, nuclei=[860, 940, 1020, 1100, 1180], nuc_w=12, nuc_col=(170, 60, 140))
        for x in (830, 1020, 1190): sat_cell(d, (x, 500), .45, dead=True)
        for (cx, cy, n) in [(925, 497, 3), (1100, 497, 2), (900, 573, 4), (1120, 573, 3)]:
            for j in range(n):
                sc(d, F, (cx + (j - (n - 1) / 2) * 40, cy), .42, col=MAG)
        L2(d, F, (1030, 640), "clonal expansion · refills niche", "克隆扩增 · 重建并回填", 24, MAG, GREY, zs=20)
    if st >= 3:
        d.rounded_rectangle([1360, 405, 1770, 685], 18, fill=RED + (30,), outline=RED + (200,), width=3)
        T(d, F, (1565, 445), "Pax3 removed  去掉 Pax3", 26, RED)
        for i, (t, up) in enumerate([("ROS  活性氧", True), ("survival  存活", False), ("stress tolerance  抗压", False)]):
            y = 500 + i * 46
            T(d, F, (1400, y), t, 24, WHITE, 'lm')
            T(d, F, (1730, y), "↑" if up else "↓", 30, RED, 'rm')
        T(d, F, (1565, 650), "a radiotolerant reserve  耐辐射储备", 20, GOLD)


def s_growth(st, im, d, F, M):
    child(d, (280, 440), 1.75)
    L2(d, F, (280, 630), "built, not just maintained", "是在建造，不只是维持", 24, WHITE, GREY, zs=22)
    fy = 270; xs = [640, 800, 960, 1100]
    nuclei = [560, 720, 880, 1040, 1180] if st == 0 else sorted([560, 720, 880, 1040, 1180] + xs)
    lfib(d, 520, 1240, fy, 80, nuclei=nuclei, nuc_w=18)
    if st >= 1:
        soft(d, lambda dd: [_glow(dd, (x, fy), 28, GREEN, 90, 4, .6) for x in xs])
    arrow(d, (510, fy), (455, fy), GREY, 4, 14); arrow(d, (1250, fy), (1305, fy), GREY, 4, 14)
    if st >= 1:
        for i, x in enumerate(xs):
            if st >= 2 and i in (0, 2):
                sat_cell(d, (x, 196), .65, dead=True); continue
            sc(d, F, (x, 196), .65, dim=(st >= 2))
            if st == 1: arrow(d, (x, 214), (x, 236), GREEN, 3, 10)
        L2(d, F, (760, 370), "prepubertal SCs add nuclei", "青春期前卫星细胞添加细胞核", 24, GREEN, GREY, zs=21)
        beam(d, (1480, 140), (1265, 232), GOLD, 7)
        L2(d, F, (1580, 300), "local, fractionated IR", "局部分次照射 (SARRP)", 22, GOLD, GREY, zs=20)
    if st >= 2:
        star(d, (xs[3] + 34, 175), 11, GOLD)
        star(d, (945, 431), 9, GOLD)
        L2(d, F, (1110, 370), "fewer + weaker", "更少、功能更差", 24, RED, GREY, zs=21)
        T(d, F, (960, 431), "some potential remains  仍有部分潜能", 20, GOLD, 'lm')
    if st >= 3:
        T(d, F, (930, 485), "14 months later · adult   14 个月后（成年）", 26, GOLD)
        lfib(d, 640, 1240, 548, 58, nuclei=range(690, 1220, 70), nuc_w=15)
        lfib(d, 640, 1240, 628, 32, nuclei=range(730, 1220, 140), nuc_w=11, col=mu(ROSE, .8))
        T(d, F, (620, 548), "control 对照", 22, WHITE, 'rm')
        T(d, F, (620, 628), "IR 照射", 22, WHITE, 'rm')
        d.rounded_rectangle([1320, 460, 1770, 682], 16, fill=(30, 42, 66, 200), outline=GREEN + (160,), width=2)
        T(d, F, (1545, 495), "genetic SC depletion", 22, WHITE)
        T(d, F, (1545, 530), "before puberty (no IR)", 22, WHITE)
        T(d, F, (1545, 566), "青春期前基因清除（不照射）", 20, GREY)
        T(d, F, (1545, 612), "→ same deficits", 26, RED)
        T(d, F, (1545, 650), "→ 相同缺陷", 22, GREY)


def s_kallenbach(st, im, d, F, M):
    bxs = [(160, 640, "3 wk · RMS cells (some mice)", "部分小鼠种入横纹肌肉瘤", (200, 120, 60)),
           (720, 1200, "4 wk · 3 × 8.2 Gy hindlimb", "4 周龄 · 后肢照射", GOLD),
           (1280, 1760, "tumor eliminated", "肿瘤消除", GREEN)]
    for i, (a, b, t, z, c) in enumerate(bxs):
        box(d, F, a, 150, b, 250, t, z, c, 26)
        if i < 2: arrow(d, (b + 10, 200), (bxs[i + 1][0] - 10, 200), WHITE, 4, 16)
    def hb(rows, x0, L, ctrl_y0, ctrl_y1):
        for yy in range(ctrl_y0, ctrl_y1, 14): d.line([(x0 + L, yy), (x0 + L, yy + 7)], fill=WHITE, width=2)
        for (lab, v, txt, col, y) in rows:
            T(d, F, (x0 - 18, y), lab, 22, WHITE, 'rm')
            d.rounded_rectangle([x0, y - 18, x0 + L * v, y + 18], 8, fill=col + (215,))
            T(d, F, (x0 + L * v - 12, y), txt, 22, WHITE, 'rm')
    if st >= 1:
        L2(d, F, (580, 318), "8 weeks old · IR only vs control", "8 周龄 · 单纯照射 vs 对照", 24, WHITE, GREY, zs=21)
        hb([("muscle mass 质量", .83, "−17%", (110, 130, 170), 400), ("function 功能", .75, "−25%", (110, 130, 170), 465),
            ("satellite cells 卫星细胞", .55, "−45%", GREEN, 530), ("fiber CSA 横截面积", .70, "−30%", ROSE, 595)], 470, 420, 372, 625)
        T(d, F, (890, 652), "control 对照", 20, WHITE)
        d.line([(1030, 300), (1030, 660)], fill=(90, 100, 118, 140), width=2)
    if st >= 2:
        L2(d, F, (1420, 318), "16 months · middle age", "16 月龄（中年）", 24, WHITE, GREY, zs=21)
        hb([("fiber atrophy 纤维萎缩", .80, "−20%", ROSE, 400), ("myonuclei 肌核", .82, "−18%", NUC, 465)], 1320, 380, 372, 490)
        T(d, F, (1700, 512), "control 对照", 20, WHITE)
        pill(d, F, (1420, 565), "lifelong fibrosis  终身纤维化", (90, 120, 150), 24, 20)
        L2(d, F, (1420, 640), "Paris 2020: blocked hypertrophic growth", "肥大生长受阻", 20, GREY, GREY, zs=20)


def s_species(st, im, d, F, M):
    def row(y, animal, desc, res, cite, rcol):
        d.rounded_rectangle([160, y - 62, 1760, y + 62], 18, fill=(30, 42, 66, 170), outline=(90, 100, 118), width=2)
        animal()
        T(d, F, (420, y - 34), desc[0], 26, WHITE, 'lm')
        T(d, F, (420, y + 2), desc[1], 22, GREY, 'lm')
        T(d, F, (420, y + 34), desc[2], 21, GREY, 'lm')
        arrow(d, (1040, y), (1110, y), WHITE, 4, 14)
        T(d, F, (1140, y - 34), res[0], 25, rcol, 'lm')
        T(d, F, (1140, y + 2), res[1], 22, res[2] if len(res) > 2 else GREY, 'lm')
        T(d, F, (1140, y + 34), cite, 20, (130, 145, 170), 'lm')
    row(210, lambda: mouse(d, (305, 218), .75),
        ("Mouse · 4 wk · single 16 Gy", "contralateral leg shielded", "小鼠 4 周龄 · 单次 16 Gy · 对侧遮挡"),
        ("satellite cells ↓ at day 3 & day 56", "第 3、56 天减少"), "Collao 2023", (240, 120, 110))
    if st >= 1:
        T(d, F, (W / 2, 305), "vs", 36, RED, font='title')
        row(400, lambda: rat(d, (318, 405), .64),
            ("Rat (SD) · single 90 Gy · groin", "a far higher single dose", "大鼠 · 单次 90 Gy"),
            ("satellite cells ↑ over 1–24 weeks", "fibrosis ↑ anyway  纤维化仍加重", ICE), "Zeng 2022", GREEN)
    if st >= 2:
        for i, (e, z, fr) in enumerate([("species", "物种", .25), ("age", "年龄", .6), ("dose", "剂量", .85), ("time", "时间", .45)]):
            x = 480 + i * 320
            dial(d, F, (x, 540), 46, fr)
            T(d, F, (x, 612), f"{e}  {z}", 24, WHITE)
        T(d, F, (W / 2, 664), "more SCs ≠ successful repair   卫星细胞多 ≠ 修复成功", 28, GOLD)


def s_verdict(st, im, d, F, M):
    d.rounded_rectangle([140, 128, 1780, 690], 20, fill=(120, 90, 60, 36), outline=(180, 150, 100, 200), width=3)
    C = [(165, 540), (565, 940), (970, 1345), (1375, 1755)]
    R1, R2 = (150, 392), (428, 670)
    # FACT A, note, FACT B
    ecard(d, F, (C[0][0], R1[0], C[0][1], R1[1]), 'FACT', "Quiescent SCs repair DNA breaks well", "静止时修复好", "Vahidi Ferdousi 2014")
    ecard(d, F, (C[2][0], R1[0], C[2][1], R1[1]), 'FACT', "SC numbers fall after juvenile IR", "幼年照射后数量下降", "Bachman 2020 · Kallenbach 2022")
    d.line([(C[0][1] - 10, 205), (750, 245), (C[2][0] + 10, 205)], fill=RED, width=3)
    d.rounded_rectangle([600, 225, 905, 335], 8, fill=(240, 230, 200, 240))
    d.ellipse([742, 215, 762, 235], fill=RED)
    T(d, F, (752, 266), "repair ≠ survival", 26, (40, 40, 50))
    T(d, F, (752, 302), "修复 ≠ 存活", 24, (90, 80, 70))
    if st >= 1:
        ecard(d, F, (C[3][0], R1[0], C[3][1], R1[1]), 'HYPOTHESIS', "Growing muscle: many SCs active → more vulnerable",
              "生长中肌肉：许多卫星细胞活跃 → 更易受伤", "Bachman 2020 · Caiozzo 2010")
    if st >= 2:
        ecard(d, F, (C[0][0], R2[0], C[0][1], R2[1]), 'FACT', "Survivors fail to perform", "幸存者功能受损", "Heslop 2000 · Bachman 2020")
        ecard(d, F, (C[1][0], R2[0], C[1][1], R2[1]), 'ASSOCIATION', "p21 signature in all resident cells; deep-quiescent SCs relatively depleted",
              "所有常驻细胞 p21 印记；深静止卫星细胞相对减少", "Collao 2025", 20, 20)
    if st >= 3:
        x0, x1, y0, y1 = C[2][0], C[3][1], R2[0], R2[1]
        d.rounded_rectangle([x0 + 6, y0 + 8, x1 + 6, y1 + 8], 14, fill=(0, 0, 0, 70))
        d.rounded_rectangle([x0, y0, x1, y1], 14, fill=(28, 38, 60, 245), outline=SCOL['HYPOTHESIS'] + (230,), width=3)
        d.ellipse([(x0 + x1) / 2 - 9, y0 - 9, (x0 + x1) / 2 + 9, y0 + 9], fill=RED)
        tag(d, F, (x0 + 18, y0 + 34), 'HYPOTHESIS')
        T(d, F, (x0 + 20, y0 + 82), "Hostile niche silences the guardians", 26, WHITE, 'lm')
        T(d, F, (x0 + 20, y0 + 116), "敌意微环境让守护者沉默", 22, GREY, 'lm')
        sx0, sy0 = x0 + 20, y0 + 145
        d.rounded_rectangle([sx0, sy0, x1 - 20, y1 - 14], 10, fill=SCOL['FACT'] + (30,), outline=SCOL['FACT'] + (180,), width=2)
        tag(d, F, (sx0 + 12, sy0 + 26), 'FACT', 20)
        T(d, F, (sx0 + 142, sy0 + 26), "in vitro: irradiated neighbor-cell secretome", 20, WHITE, 'lm')
        T(d, F, (sx0 + 12, sy0 + 58), "impairs SC differentiation / fusion · 受照邻居分泌物损害分化/融合", 20, WHITE, 'lm')
        T(d, F, (x1 - 34, sy0 + 26), "Collao 2023", 20, (130, 145, 170), 'rm')
        arrow(d, (x1 - 6, (y0 + y1) / 2 - 80), (1880, (y0 + y1) / 2 - 80), GOLD, 5, 18)
        T(d, F, (1840, (y0 + y1) / 2 - 116), "Ep3", 26, GOLD)


BENCH = [
    ("Counting satellite cells  数卫星细胞",
     [("PAX7 antibody", "核内 PAX7"), ("+ laminin", "勾出基底膜"), ("+ DAPI", "所有细胞核"), ("per 100 fibers · blind", "每百根纤维·盲法")]),
    ("One switch, two experiments  一个开关，两种实验",
     [("Pax7-CreER + tamoxifen", "他莫昔芬开锁"), ("R26-stop-DTA", "清除：是否必需"), ("R26-stop-reporter", "示踪：变成什么"), ("Cre removes stop", "Cre 剪掉终止信号")]),
    ("Who has divided?  谁分裂过？",
     [("EdU short pulse", "短时给药：谁在复制"), ("long pulse + chase", "长给药+等待"), ("label-retaining cells", "标记滞留细胞"), ("lowest dose · + PAX7", "最低剂量·共染 PAX7")]),
    ("Single fibers & sorting  单纤维与分选",
     [("collagenase digest", "胶原酶消化"), ("single-fiber culture", "单纤维培养"), ("FACS: α7-integrin+, lineage−", "流式：α7整合素+，排除血/血管细胞"), ("isolation activates cells", "分离本身会激活细胞")]),
]


def s_bench(st, im, d, F, M):
    t, rows = BENCH[st]
    bench_card(d, F, t, rows)


def _cur(f):
    def g(st, im, d, F, M):
        CUR['im'] = im
        try: return f(st, im, d, F, M)
        finally: CUR['im'] = None
    return g


SCENES = {
    'recap': s_recap, 'em': s_em, 'niche': s_niche, 'bench': s_bench, 'ablation': s_ablation, 'three': s_three,
    'cycle': s_cycle, 'quiescence': s_quiescence, 'paradox': s_paradox, 'heslop': s_heslop, 'transplant': s_transplant,
    'reserve': s_reserve, 'growth': s_growth, 'kallenbach': s_kallenbach, 'species': s_species, 'verdict': s_verdict,
}
SCENES = {k: _cur(v) for k, v in SCENES.items()}
