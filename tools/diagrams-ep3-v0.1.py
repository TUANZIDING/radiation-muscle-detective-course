"""Episode 3 'The Neighbors Turn' scene drawings for 'After the Beam'.
Each scene f(st, im, d, F, M) draws step st on the supersampled proxy d (logical 1920x1080).
Diagram area y 120..690; REF card at x>1150, y 698..742; subtitles below 760.
Colour identities: satellite cell GREEN, FAP ORANGE, macrophage PURPLE, capillary RED, fiber ROSE, scar ICE.
"""
from prims import *
import os, math, random
from diagrams import T, arrow, box, fiber, cell, foci, W

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(os.path.dirname(HERE), 'assets', 'img', 'trichrome-fibrosis-human-spinal-muscle-v0.1.jpg')
TGFC = (175, 228, 80)       # TGF-beta signal (lime, distinct from satellite-cell green)
MONO = (220, 95, 140)       # Ly6C+ inflammatory monocyte (red-tinted purple)
MACB = (110, 150, 235)      # anti-inflammatory macrophage (blue-tinted)
AMBER = SCOL['ASSOCIATION']; HYP = SCOL['HYPOTHESIS']
CREAM = (240, 230, 200); INK = (40, 40, 50); INK2 = (95, 85, 75)


# ---------------------------------------------------------------- helpers
def dline(d, a, b, col=GREY, w=3, dash=14):
    L = math.dist(a, b); n = max(2, int(L / dash))
    for i in range(0, n, 2):
        p = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
        q = (a[0] + (b[0] - a[0]) * min(n, i + 1) / n, a[1] + (b[1] - a[1]) * min(n, i + 1) / n)
        d.line([p, q], fill=col, width=w)

def dcircle(d, c, r, col=GOLD, n=28, s=3):
    for i in range(n):
        a = i / n * 6.283; x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
        d.ellipse([x - s, y - s, x + s, y + s], fill=col)

def drect(d, bx, col=GREY, w=3, dash=14):
    x0, y0, x1, y1 = bx
    for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        dline(d, a, b, col, w, dash)

def spark(d, c, s=12, col=GOLD):
    x, y = c
    d.polygon([(x, y - s), (x + s * .33, y - s * .25), (x + s, y), (x + s * .33, y + s * .25), (x, y + s),
               (x - s * .33, y + s * .25), (x - s, y), (x - s * .33, y - s * .25)], fill=col)

def updn(d, c, up=True, col=GREEN, s=1.0):
    """Solid block arrow icon (no glyph needed)."""
    x, y = c; h = 22 * s; w = 9 * s; hw = 18 * s
    if up:
        d.polygon([(x, y - h), (x + hw, y - h + hw), (x + w, y - h + hw), (x + w, y + h), (x - w, y + h), (x - w, y - h + hw), (x - hw, y - h + hw)], fill=col)
    else:
        d.polygon([(x, y + h), (x + hw, y + h - hw), (x + w, y + h - hw), (x + w, y - h), (x - w, y - h), (x - w, y + h - hw), (x - hw, y + h - hw)], fill=col)

def arcpts(c, rx, ry, a0, a1, n=40):
    return [(c[0] + rx * math.cos(a0 + (a1 - a0) * i / n), c[1] + ry * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]

def pacman(d, c, r, col, ang=0.0):
    d.polygon([c] + arcpts(c, r, r, ang + .55, ang + 6.283 - .55), fill=col + (230,), outline=tuple(min(255, v + 60) for v in col))
    d.ellipse([c[0] - r * .35 - 6, c[1] - r * .55, c[0] - r * .35 + 10, c[1] - r * .55 + 12], fill=(60, 30, 70))

def roundcell(d, c, r, col):
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=col + (225,), outline=tuple(min(255, v + 60) for v in col), width=3)
    d.ellipse([c[0] - r * .4, c[1] - r * .4, c[0] + r * .4, c[1] + r * .4], fill=tuple(int(v * .45) for v in col))

def tube(d, x0, x1, y, h=64, col=RED, rbc=()):
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], h / 2, fill=col + (55,), outline=col, width=4)
    for x in rbc:
        d.ellipse([x - 15, y - 8, x + 15, y + 8], fill=(235, 95, 90))

def debris(d, box_, n=14, seed=3, col=ROSE):
    rnd = random.Random(seed); x0, y0, x1, y1 = box_
    for _ in range(n):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1); s = rnd.uniform(8, 16)
        pts = [(x + s * math.cos(a) * rnd.uniform(.6, 1.1), y + s * math.sin(a) * rnd.uniform(.6, 1.1)) for a in [k * 1.257 for k in range(5)]]
        d.polygon(pts, fill=col + (190,))

def cap_glyph(d, c, col=CREAM):
    """Small capsule (drug pill) icon."""
    x, y = c
    d.rounded_rectangle([x - 34, y - 14, x + 34, y + 14], 14, fill=(240, 240, 245, 230))
    d.rounded_rectangle([x, y - 14, x + 34, y + 14], 14, fill=(230, 120, 100, 240))
    d.rectangle([x, y - 14, x + 10, y + 14], fill=(230, 120, 100, 240))

def two(d, F, xy, en, zh, size=26, col=WHITE, zcol=GREY, anchor='mm', gap=None, zsize=None):
    g = gap or size * .66
    T(d, F, (xy[0], xy[1] - g), en, size, col, anchor)
    T(d, F, (xy[0], xy[1] + g), zh, zsize or int(size * .88), zcol, anchor)

def panel(d, bx, col=(120, 140, 170), a=28):
    d.rounded_rectangle(bx, 22, fill=col + (a,), outline=col + (150,), width=2)

def half_disk(d, c, r, left=True, col=ORANGE, a=90):
    a0, a1 = (math.pi / 2, 3 * math.pi / 2) if left else (-math.pi / 2, math.pi / 2)
    d.polygon(arcpts(c, r, r, a0, a1, 60), fill=col + (a,))

def hexfibers(c, R, sp):
    out = []
    for row in range(-10, 11):
        for col in range(-10, 11):
            px = c[0] + (col + (row % 2) * .5) * sp; py = c[1] + row * sp * .866
            if math.dist((px, py), c) < R - sp * .5: out.append((px, py))
    return out

def flame(d, c, s=1.0):
    x, y = c
    d.polygon([(x, y - 30 * s), (x + 16 * s, y - 4 * s), (x + 12 * s, y + 14 * s), (x - 12 * s, y + 14 * s), (x - 16 * s, y - 4 * s)], fill=(245, 140, 50, 235))
    d.polygon([(x, y - 14 * s), (x + 8 * s, y + 2 * s), (x + 6 * s, y + 12 * s), (x - 6 * s, y + 12 * s), (x - 8 * s, y + 2 * s)], fill=(255, 225, 120))

def trowel(d, c, s=1.0, col=ICE):
    x, y = c
    d.polygon([(x - 34 * s, y + 18 * s), (x + 30 * s, y + 18 * s), (x - 2 * s, y - 26 * s)], fill=col + (230,))
    d.line([(x - 2 * s, y - 26 * s), (x + 12 * s, y - 46 * s)], fill=(170, 170, 180), width=int(6 * s))
    d.rounded_rectangle([x + 8 * s, y - 66 * s, x + 26 * s, y - 42 * s], 6, fill=(140, 90, 50))

def hammer(d, c, s=1.0):
    x, y = c
    d.line([(x - 30 * s, y + 34 * s), (x + 14 * s, y - 14 * s)], fill=(170, 115, 60), width=int(10 * s))
    d.polygon([(x - 6 * s, y - 34 * s), (x + 10 * s, y - 50 * s), (x + 44 * s, y - 16 * s), (x + 28 * s, y)], fill=(200, 205, 215))

def bulb(d, c, on=True):
    x, y = c
    if on:
        for r, a in ((70, 30), (52, 50)):
            d.ellipse([x - r, y - r, x + r, y + r], fill=YELLOW + (a,))
        for k in range(8):
            a = k * .785; d.line([(x + 46 * math.cos(a), y + 46 * math.sin(a)), (x + 60 * math.cos(a), y + 60 * math.sin(a))], fill=YELLOW, width=4)
    d.ellipse([x - 32, y - 34, x + 32, y + 30], fill=(YELLOW if on else (120, 120, 110)) + (240,))
    d.rectangle([x - 15, y + 26, x + 15, y + 46], fill=(170, 175, 185))
    d.line([(x - 15, y + 34), (x + 15, y + 34)], fill=(110, 110, 120), width=2)

def scissors(d, c, s=1.0, col=(220, 225, 235)):
    x, y = c
    d.line([(x - 40 * s, y - 30 * s), (x + 40 * s, y + 18 * s)], fill=col, width=int(7 * s))
    d.line([(x - 40 * s, y + 30 * s), (x + 40 * s, y - 18 * s)], fill=col, width=int(7 * s))
    for yy in (-30, 30):
        d.ellipse([x - 66 * s, y + yy * s - 14 * s, x - 38 * s, y + yy * s + 14 * s], outline=col, width=int(6 * s))


# ================================================================ cold open
def s_recap(st, im, d, F, M):
    c = (620, 410)
    scar = [0, 0, .45, .8][st]
    xsection(d, c, R=230, n=14, seed=11, scar=scar, caps=True, sats=8 if st >= 1 else 0, sat_dead=6)
    beam(d, (140, 250), (372, 372))
    rows = [("Ep1: the fiber survives", "第一集：纤维挺住了", GOLD),
            ("Ep2: guardians thinned", "第二集：守护者减少", GREEN),
            ("Weeks later: scar fills the gaps", "数周后：瘢痕填满缝隙", ICE)]
    for i, (en, zh, col) in enumerate(rows):
        if st < i: break
        y = 190 + i * 92
        d.ellipse([1062, y - 9, 1080, y + 9], fill=col)
        T(d, F, (1104, y - 16), en, 28, WHITE, 'lm'); T(d, F, (1104, y + 20), zh, 24, GREY, 'lm')
    if st >= 3:
        d.ellipse([606, 266, 774, 434], outline=GOLD, width=8); d.line([(750, 410), (830, 490)], fill=GOLD, width=14)
        T(d, F, (1400, 465), "Who laid the scar?", 44, GOLD, font='title')
        T(d, F, (1400, 517), "瘢痕是谁铺的？", 32, GOLD)
        fap(d, (1170, 600), .7)
        macrophage(d, (1400, 598), .72)
        tube(d, 1570, 1720, 600, 44, rbc=(1610, 1680))
        for x, lab in ((1170, "FAP"), (1400, "macrophage 巨噬"), (1645, "capillary 毛细血管")):
            T(d, F, (x, 668), lab, 21, GREY)


# ================================================================ 1  FAP two faces
def s_fap(st, im, d, F, M):
    if st <= 1:
        fiber(d, F, 205, 160, 1760, 100)
        fiber(d, F, 455, 160, 1760, 100)
        # satellite cell under the basal lamina of the upper fiber
        sat_cell(d, (330, 268), .8)
        d.line(arcpts((330, 262), 64, 30, 0, math.pi, 30), fill=(200, 210, 225), width=2)
        T(d, F, (330, 335), "satellite cell 卫星细胞", 21, GREEN)
        for x, a in ((660, .1), (1480, -.12)):
            fap(d, (x, 330), 1.15, angle=a)
        two(d, F, (1070, 330), "interstitial cells", "间质细胞", 28, ORANGE, GREY)
        if st >= 1:
            T(d, F, (W / 2, 548), "FAP  =  fibro-adipogenic progenitor    纤维-脂肪生成祖细胞", 30, ORANGE)
            for x0, en in ((380, "Joe et al. 2010 · Vancouver"), (1080, "Uezumi et al. 2010 · Japan")):
                d.rounded_rectangle([x0, 592, x0 + 460, 680], 10, fill=(230, 225, 205, 26), outline=GOLD + (180,), width=2)
                d.rectangle([x0, 592, x0 + 14, 680], fill=GOLD + (200,))
                T(d, F, (x0 + 237, 620), en, 24, WHITE); T(d, F, (x0 + 237, 654), "Nat Cell Biol 12(2)", 21, GREY)
            two(d, F, (960, 636), "same issue", "同一期", 21, GOLD, GOLD, gap=14, zsize=20)
        return
    # step 2: intact vs injury
    T(d, F, (540, 160), "intact muscle  完好肌肉", 30, WHITE)
    T(d, F, (1380, 160), "injury  损伤", 30, WHITE)
    dline(d, (960, 150), (960, 600), DIM, 3)
    fiber(d, F, 255, 200, 880, 80, nuclei=False); fiber(d, F, 475, 200, 880, 80, nuclei=False)
    for x in (330, 540, 750):
        fap(d, (x, 368), .6, angle=.05)
        T(d, F, (x + 52, 322), "z z", 22, GREY)
    T(d, F, (540, 560), "quiet 安静待命", 24, GREY)
    for y in (255, 475):
        d.rounded_rectangle([1040, y - 40, 1235, y + 40], 40, fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
        d.rounded_rectangle([1525, y - 40, 1720, y + 40], 40, fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
    for i in range(9):
        fap(d, (1290 + (i % 3) * 90, 290 + (i // 3) * 78), .45, angle=.3 * (i % 2))
    sat_cell(d, (1110, 368), .6); sat_cell(d, (1650, 368), .6)
    arrow(d, (1240, 368), (1160, 368), YELLOW, 4, 14); arrow(d, (1520, 368), (1600, 368), YELLOW, 4, 14)
    two(d, F, (1380, 565), "helps differentiation (dish)", "促进分化（培养皿）", 24, WHITE, GREY)
    stamp(d, F, (960, 648), "transient helper   暂时的帮手", GOLD, 28)


def _muscle_oval(d, c, fatty=False):
    x, y = c
    d.ellipse([x - 150, y - 82, x + 150, y + 82], fill=(150, 60, 70, 120), outline=(220, 130, 140), width=3)
    for dx, dy in ((-90, -20), (-30, -40), (40, -30), (100, 0), (-60, 35), (20, 30), (80, 45)):
        d.ellipse([x + dx - 22, y + dy - 18, x + dx + 22, y + dy + 18], fill=ROSE + (200,), outline=(240, 150, 160), width=2)
    if fatty:
        fat(d, (x - 5, y + 5), n=8, R=70, seed=7)


def s_fapexp(st, im, d, F, M):
    if st <= 1:
        dline(d, (960, 150), (960, 650), DIM, 3)
        T(d, F, (540, 160), "Joe 2010 · transplant  移植", 28, WHITE)
        syringe(d, (260, 245), 1.2)
        for k, x in enumerate(range(290, 410, 26)):
            d.ellipse([x - 9, 236, x + 9, 254], fill=ORANGE)
        T(d, F, (340, 206), "purified FAPs  纯化 FAP", 22, ORANGE)
        arrow(d, (468, 262), (380, 362), WHITE, 4, 14); arrow(d, (468, 262), (690, 362), WHITE, 4, 14)
        _muscle_oval(d, (330, 450), True); _muscle_oval(d, (750, 450), False)
        two(d, F, (330, 575), "fatty-infiltration model", "脂肪浸润模型 → 白色脂肪", 22, YELLOW, GREY, zsize=20)
        two(d, F, (750, 575), "healthy muscle", "健康肌肉 → 无脂肪", 22, WHITE, GREY, zsize=20)
        T(d, F, (540, 648), "same cell, different neighborhood   同一细胞，不同街区", 25, GOLD)
        if st >= 1:
            T(d, F, (1390, 160), "Uezumi 2010 · PDGFRα", 28, WHITE)
            ox, oy = 1060, 480
            d.line([(ox, 220), (ox, oy), (1330, oy)], fill=GREY, width=3)
            T(d, F, (1195, 506), "PDGFRα →", 20, GREY)
            rnd = random.Random(5)
            for _ in range(46):
                x, y = ox + 30 + rnd.gauss(70, 30), oy - 30 - rnd.gauss(60, 28)
                x, y = min(max(x, ox + 12), 1200), min(max(y, 330), oy - 10)
                d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(170, 180, 200, 200))
            for _ in range(26):
                x, y = 1265 + max(-40, min(40, rnd.gauss(0, 18))), 300 + max(-40, min(40, rnd.gauss(0, 20)))
                d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=ORANGE + (230,))
            d.rectangle([1215, 248, 1315, 352], outline=ORANGE, width=3)
            T(d, F, (1265, 232), "PDGFRα+", 21, ORANGE)
            arrow(d, (1325, 300), (1480, 300), ORANGE, 4, 16)
            arrow(d, (1205, 430), (1480, 470), GREY, 3, 14)
            dish(d, F, (1620, 300), 115)
            for k, x in enumerate((1565, 1620, 1675)):
                d.ellipse([x - 20, 282, x + 20, 318], fill=ORANGE + (220,))
                d.ellipse([x - 8, 290, x + 6, 304], fill=YELLOW); d.ellipse([x + 2, 300, x + 12, 310], fill=YELLOW)
            T(d, F, (1620, 366), "→ fat  成脂", 21, YELLOW)
            dish(d, F, (1620, 470), 115)
            for x in (1570, 1625, 1678):
                sat_cell(d, (x, 470), .38)
            T(d, F, (1620, 536), "other cells: lean  其他细胞不成脂", 21, GREY)
            two(d, F, (1380, 612), "only PDGFRα+ cells make fat efficiently", "只有 PDGFRα+ 细胞高效成脂", 25, WHITE, GREY, zsize=22)
        return
    # step 2: two faces
    c = (960, 355); r = 185
    half_disk(d, c, r, True, ORANGE, 70); half_disk(d, c, r, False, (140, 140, 150), 70)
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], outline=GOLD, width=4)
    d.line([(c[0], c[1] - r), (c[0], c[1] + r)], fill=GOLD, width=3)
    fap(d, (868, 290), .75); fap(d, (1052, 290), .75, grey=True)
    hammer(d, (870, 430), 1.0); trowel(d, (1040, 445), 1.0)
    fat(d, (1092, 385), n=3, R=12, seed=2)
    T(d, F, (730, 300), "builder", 34, ORANGE, 'rm'); T(d, F, (730, 344), "建造者", 28, ORANGE, 'rm')
    T(d, F, (730, 400), "beside healthy fibers", 22, GREY, 'rm'); T(d, F, (730, 430), "& busy stem cells", 22, GREY, 'rm')
    T(d, F, (730, 462), "在健康纤维与干细胞旁", 21, GREY, 'rm')
    T(d, F, (1190, 300), "fat & scar maker", 34, (200, 205, 215), 'lm'); T(d, F, (1190, 344), "脂肪/瘢痕制造者", 28, (200, 205, 215), 'lm')
    T(d, F, (1190, 400), "alone in damaged tissue", 22, GREY, 'lm'); T(d, F, (1190, 432), "独自留在受损组织里", 21, GREY, 'lm')
    fiber(d, F, 620, 470, 860, 60, nuclei=False)
    T(d, F, (665, 620), "healthy fiber", 21, WHITE)
    inhibit(d, (876, 620), (990, 620), RED, 6)
    fat(d, (1030, 620), n=4, R=18, seed=3)
    T(d, F, (1080, 620), "fibers inhibit adipogenesis   纤维抑制成脂", 24, WHITE, 'lm')


# ================================================================ bench notes
BENCH = [
    ("Bench note 1 · Catching FAPs by flow cytometry   流式分选 FAP",
     [("Digest muscle into single cells", "酶消化为单细胞"),
      ("Exclude CD45+ (blood), CD31+ (vessel)", "剔除 CD45+、CD31+ 细胞"),
      ("Mouse FAP: PDGFRα+ Sca-1+", "小鼠 FAP：PDGFRα+ Sca-1+"),
      ("Caveat: digestion stress; no human Sca-1", "注意：消化应激；人无 Sca-1")]),
    ("Bench note 2 · Staining macrophages   巨噬细胞染色",
     [("CD68 (mouse F4/80): all macrophages", "泛巨噬细胞标记"),
      ("CD206: repair-type, anti-inflammatory", "修复型 / 抗炎型"),
      ("Flow: Ly6C-high new · Ly6C-low converted", "Ly6C 高：新到 · 低：已转变"),
      ("M1/M2 is a simplification: sample many days", "M1/M2 是简化；多时间点取样")]),
    ("Bench note 3 · Measuring scar   测量瘢痕",
     [("Masson trichrome: collagen blue", "胶原染成蓝色"),
      ("Picrosirius red + polarized light", "天狼星红：偏振光下粗纤维发光"),
      ("Hydroxyproline: total collagen", "羟脯氨酸：总胶原量"),
      ("Preset threshold · score blind · whole muscle", "预设阈值 · 盲法 · 全肌取样")]),
    ("Bench note 4 · Counting capillaries   计数毛细血管",
     [("CD31 staining on cross-sections", "横切面 CD31 染色"),
      ("Report capillaries per fiber, not only per mm²", "报告每纤维毛细血管数"),
      ("Atrophy inflates per-area density", "萎缩会虚增单位面积密度"),
      ("Stained ≠ perfused: add a perfusion test", "染上 ≠ 有灌注：加灌注检测")]),
]

def s_bench(st, im, d, F, M):
    title, rows = BENCH[st]
    bench_card(d, F, title, rows)


# ================================================================ 2  macrophages
def s_macro(st, im, d, F, M):
    vy = 200
    tube(d, 160, 1000, vy, 70, rbc=(640, 860, 950))
    crew = (260, 380, 500)
    for x in crew:
        roundcell(d, (x, vy), 24, PURPLE if st < 3 else (120, 110, 140))
        if st >= 3: xmark(d, (x, vy), 22, RED, 6)
    T(d, F, (1060, 172), "cleanup crew  清理队", 30, PURPLE, 'lm')
    T(d, F, (1060, 214), "monocytes & macrophages  单核/巨噬细胞", 23, GREY, 'lm')
    # damaged fiber
    fy = 385
    d.rounded_rectangle([160, fy - 50, 720, fy + 50], 50, fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
    d.rounded_rectangle([1250, fy - 50, 1760, fy + 50], 50, fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
    for x in range(200, 700, 26): d.line([(x, fy - 38), (x, fy + 38)], fill=(190, 90, 100, 120), width=2)
    for x in range(1290, 1740, 26): d.line([(x, fy - 38), (x, fy + 38)], fill=(190, 90, 100, 120), width=2)
    if st in (0, 3): debris(d, (740, 335, 1230, 435), 18, 3)
    if st == 1: debris(d, (900, 335, 1230, 435), 11, 4)
    if st == 2: debris(d, (1080, 345, 1230, 425), 4, 5)
    # bottom timeline (steps 1-3)
    ty = 530
    if st >= 1:
        arrow(d, (200, ty), (1720, ty), GREY, 3, 16)
        d.line([(360, ty - 12), (360, ty + 12)], fill=GREY, width=3)
        T(d, F, (360, ty - 30), "day ~1", 21, GREY)
        T(d, F, (1745, ty), "", 20)
    if st in (1, 2):
        mc = [(780, 350), (850, 418), (930, 355)]
        dline(d, (760, vy + 36), (775, 318), MONO if st == 1 else MACB, 3)
        if st == 1:
            for (x, y), a in zip(mc, (0.2, -0.4, 0.1)): pacman(d, (x, y), 26, MONO, a)
            for x, y in ((1110, 370), (1150, 405)): sat_cell(d, (x, y), .42)
            T(d, F, (1130, 445), "", 20)
        else:
            for x, y in mc: roundcell(d, (x, y), 26, MACB)
            rnd = random.Random(8)
            for _ in range(14):
                a = rnd.uniform(0, 6.28); rr = rnd.uniform(40, 80)
                x, y = 855 + rr * math.cos(a) * 1.3, 385 + rr * math.sin(a) * .6
                d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=TGFC)
            d.rounded_rectangle([1020, 368, 1180, 404], 18, fill=GREEN + (210,), outline=(170, 255, 190), width=3)
            for x in (1050, 1100, 1150): d.ellipse([x - 9, 380, x + 9, 392], fill=(30, 90, 50))
            T(d, F, (870, 300), "TGF-β1", 22, TGFC)
        # phase labels
        c1 = MONO; T(d, F, (560, 578), "① Ly6C+ inflammatory monocytes", 24, c1)
        T(d, F, (560, 612), "Ly6C+ 炎症单核细胞", 21, GREY)
        T(d, F, (560, 650), "→ muscle cells multiply  增殖", 22, WHITE)
        if st >= 2:
            T(d, F, (1360, 578), "② anti-inflammatory macrophages", 24, MACB)
            T(d, F, (1360, 612), "抗炎巨噬细胞 · TGF-β1", 21, GREY)
            T(d, F, (1360, 650), "→ mature & fuse  分化融合", 22, WHITE)
            T(d, F, (960, 482), "eating debris flips the switch   吞噬碎片触发转换", 22, GOLD)
    if st >= 3:
        T(d, F, (580, 272), "depleted at injury  损伤时清除", 22, RED)
        stamp(d, F, (1440, 290), "not irradiated  非放射模型", RED, 22)
        T(d, F, (960, 590), "no regeneration   完全无再生", 36, RED)
        T(d, F, (960, 640), "Arnold 2007 · mouse", 22, GREY)


def s_balance(st, im, d, F, M):
    if st == 0:
        panel(d, (520, 165, 1400, 590))
        T(d, F, (960, 200), "same room  同一个房间", 26, GREY)
        macrophage(d, (960, 320), 1.0)
        for x, y in ((740, 480), (960, 505), (1180, 480)): fap(d, (x, y), .8)
        T(d, F, (960, 638), "Lemos 2015 · Nat Med · mouse", 26, WHITE)
        return
    if st <= 2:
        panel(d, (140, 160, 920, 640)); panel(d, (1000, 160, 1780, 640), a=28 if st >= 2 else 10)
        T(d, F, (530, 198), "acute injury  急性损伤", 28, WHITE)
        T(d, F, (1390, 198), "chronic injury (mdx)  慢性损伤", 28, WHITE if st >= 2 else DIM)
        macrophage(d, (320, 380), .95)
        for y in (300, 400, 500):
            arrow(d, (385, 380 + (y - 400) * .25), (600, y), RED, 4, 16)
        T(d, F, (470, 300), "TNF", 26, RED)
        fap(d, (720, 290), .7)
        for (x, y), s in (((720, 410), 3), ((720, 515), 7)):
            fap(d, (x, y), .7, grey=True)
            rnd = random.Random(s)
            for _ in range(6):
                a = rnd.uniform(0, 6.28); rr = rnd.uniform(44, 64)
                d.ellipse([x + rr * math.cos(a) - 6, y + rr * math.sin(a) * .7 - 6, x + rr * math.cos(a) + 6, y + rr * math.sin(a) * .7 + 6], fill=(150, 150, 160, 200))
        T(d, F, (840, 462), "apoptosis", 20, GREY); T(d, F, (840, 488), "凋亡", 20, GREY)
        two(d, F, (530, 594), "TNF culls surplus FAPs", "TNF 清除多余 FAP", 24, WHITE, GREY, zsize=21)
        if st >= 2:
            collagen(d, (1480, 250, 1750, 540), n=11, seed=4, w=3)
            macrophage(d, (1150, 380), .95)
            d.ellipse([1215, 315, 1435, 445], fill=TGFC + (60,), outline=TGFC + (160,), width=2)
            for k in range(10):
                a = k * .63; d.ellipse([1325 + 80 * math.cos(a) - 6, 380 + 45 * math.sin(a) - 6, 1325 + 80 * math.cos(a) + 6, 380 + 45 * math.sin(a) + 6], fill=TGFC)
            T(d, F, (1325, 380), "TGF-β1", 30, TGFC)
            for x, y in ((1590, 300), (1630, 410), (1570, 505)): fap(d, (x, y), .7)
            two(d, F, (1390, 594), "TGF-β1: FAPs survive → matrix", "FAP 存活 → 基质（瘢痕）", 24, WHITE, GREY, zsize=21)
        return
    # step 3: balance of timing
    clock(d, (960, 205), 46, GOLD, hour=4)
    T(d, F, (1030, 205), "timing  时机", 30, GOLD, 'lm')
    d.polygon([(900, 640), (1020, 640), (960, 575)], fill=(150, 160, 175))
    d.line([(960, 575), (960, 330)], fill=(150, 160, 175), width=8)
    L, R = (620, 300), (1300, 380)
    d.line([L, R], fill=(200, 205, 215), width=8)
    d.ellipse([950, 330, 970, 350], fill=GOLD)
    for (x, y), lab, zh, col in ((L, "TNF", "early 早期", RED), (R, "TGF-β", "later 晚期", TGFC)):
        py = y + 105
        d.line([(x, y), (x - 70, py)], fill=GREY, width=2); d.line([(x, y), (x + 70, py)], fill=GREY, width=2)
        d.polygon(arcpts((x, py), 90, 34, 0, math.pi, 30), fill=(150, 160, 175, 200))
        pill(d, F, (x, py - 26), lab, col if col != TGFC else (110, 160, 60), 26)
        T(d, F, (x, py + 62), zh, 24, col)
    collagen(d, (1450, 420, 1700, 520), n=7, seed=9, w=4)
    T(d, F, (1575, 548), "too early → scar wins", 22, ICE); T(d, F, (1575, 576), "时机错乱 → 瘢痕胜出", 21, GREY)
    cap_glyph(d, (240, 600))
    T(d, F, (295, 586), "nilotinib reduced fibrosis (mdx)", 22, WHITE, 'lm')
    T(d, F, (295, 618), "尼洛替尼减轻纤维化", 21, GREY, 'lm')
    stamp(d, F, (1580, 200), "not irradiated  非放射模型", RED, 22)


# ================================================================ 3  TGF-beta lock
def s_lock(st, im, d, F, M):
    if st <= 2:
        # col 1: skin / subcutis fibrosis
        beam(d, (230, 132), (318, 196), w=6)
        d.rectangle([200, 200, 660, 230], fill=(220, 165, 155, 230))
        d.rectangle([200, 230, 660, 420], fill=(110, 80, 95, 160))
        collagen(d, (205, 238, 655, 415), n=15, seed=3, w=4)
        d.rectangle([200, 420, 660, 520], fill=(90, 80, 70, 120))
        fat(d, (330, 470), n=5, R=40, seed=1); fat(d, (540, 470), n=5, R=40, seed=2)
        d.rectangle([200, 200, 660, 520], outline=(180, 170, 180), width=2)
        T(d, F, (430, 562), "radiation fibrosis  放射性纤维化", 26, ICE)
        T(d, F, (430, 600), "mostly skin & subcutis  主要为皮肤及皮下", 21, GREY)
        T(d, F, (430, 634), "Martin 2000 · review", 21, GREY)
    if 1 <= st <= 2:
        bulb(d, (1010, 215))
        myofibroblast(d, (1010, 375), 1.35)
        T(d, F, (1010, 470), "chronically activated", 24, WHITE)
        T(d, F, (1010, 502), "myofibroblasts", 24, WHITE)
        T(d, F, (1010, 538), "持续激活的肌成纤维细胞", 22, GREY)
    if st == 2:
        x, y = 1390, 300
        d.polygon([(x - 50, y - 8), (x - 10, y - 22), (x + 40, y - 10), (x + 50, y + 8), (x + 5, y + 22), (x - 45, y + 10)], fill=(180, 60, 60, 220))
        for k, rr in enumerate((70, 100, 130)):
            d.line(arcpts((x, y), rr, rr, -0.6, 0.6, 20), fill=GOLD + (220 - k * 50,), width=4)
            d.line(arcpts((x, y), rr, rr, math.pi - 0.6, math.pi + 0.6, 20), fill=GOLD + (220 - k * 50,), width=4)
        T(d, F, (x, 410), "repair signals 修复信号", 21, GOLD)
        sx, sy = 1620, 360
        d.rounded_rectangle([sx - 60, sy - 90, sx + 60, sy + 90], 14, fill=(50, 60, 80, 230), outline=(180, 190, 210), width=3)
        d.line([(sx, sy + 10), (sx + 4, sy - 70)], fill=GREEN, width=12)
        d.ellipse([sx - 14, sy - 84, sx + 22, sy - 50], fill=GREEN)
        T(d, F, (sx, sy + 58), "ON", 24, GREEN)
        padlock(d, (sx + 112, sy + 10), .75)
        T(d, F, (1560, 486), "TGF-β1 master switch", 24, WHITE); T(d, F, (1560, 518), "纤维化总开关", 22, GREY)
        T(d, F, (1270, 610), "“a wound where repair signals never stop”", 32, GOLD, font='gari')
        T(d, F, (1270, 652), "修复信号永不停歇的伤口", 24, GOLD)
        T(d, F, (1690, 625), "?", 64, GOLD, font='title')
    if st == 3:
        rat(d, (440, 400), 1.0)
        beam(d, (300, 150), (370, 345), w=8)
        T(d, F, (420, 175), "single 90 Gy  单次 90 Gy", 26, GOLD, 'lm')
        T(d, F, (440, 520), "SD rat · thigh (rectus femoris)", 22, WHITE); T(d, F, (440, 552), "大鼠大腿（股直肌）", 21, GREY)
        bx = (900, 250, 1700, 520)
        linechart(d, F, bx, [("", ICE, [.18, .38, .6, .86]), ("", TGFC, [.12, .3, .5, .72])], xt=("wk 1", "wk 2", "wk 4", "wk 8"), size=21)
        d.line([(930, 190), (980, 190)], fill=ICE, width=5); T(d, F, (995, 190), "fibrosis (Masson)  纤维化", 22, ICE, 'lm')
        d.line([(1360, 190), (1410, 190)], fill=TGFC, width=5); T(d, F, (1425, 190), "TGF-β1", 22, TGFC, 'lm')
        T(d, F, (1110, 615), "Zhou 2018 · SD rat · 90 Gy single dose", 24, WHITE)
        stamp(d, F, (1560, 615), "association  关联", AMBER, 24)


# ================================================================ Collao 2023
def _topmouse(d, F, c):
    x, y = c; col = (200, 200, 210)
    d.line([(x - 45, y + 110), (x - 95, y + 210)], fill=col, width=26)
    d.line([(x + 45, y + 110), (x + 95, y + 210)], fill=col, width=26)
    d.line([(x, y + 130), (x - 10, y + 190), (x + 12, y + 250)], fill=(230, 180, 190), width=6)
    d.ellipse([x - 80, y - 120, x + 80, y + 140], fill=col + (235,))
    d.ellipse([x - 48, y - 190, x + 48, y - 96], fill=col)
    for dx in (-44, 44): d.ellipse([x + dx - 22, y - 186, x + dx + 22, y - 142], fill=(230, 180, 190))
    for dx in (-18, 18): d.ellipse([x + dx - 5, y - 160, x + dx + 5, y - 150], fill=(30, 30, 30))
    d.line([(x - 50, y - 70), (x - 92, y - 10)], fill=col, width=16); d.line([(x + 50, y - 70), (x + 92, y - 10)], fill=col, width=16)


def s_collao(st, im, d, F, M):
    if st == 0:
        mx, my = 540, 360
        d.rounded_rectangle([mx + 50, my + 70, mx + 150, my + 260], 16, fill=GOLD + (60,))
        _topmouse(d, F, (mx, my))
        d.rounded_rectangle([mx + 50, my + 70, mx + 150, my + 260], 16, outline=GOLD, width=3)
        T(d, F, (mx + 172, my + 165), "16 Gy", 30, GOLD, 'lm')
        sx0, sx1 = mx - 150, mx - 40
        d.rounded_rectangle([sx0, my + 70, sx1, my + 260], 10, fill=(120, 125, 135, 235), outline=(200, 205, 215), width=3)
        for k in range(my + 84, my + 250, 22): d.line([(sx0 + 8, k + 10), (sx1 - 8, k - 10)], fill=(165, 170, 180), width=2)
        T(d, F, (sx0 - 18, my + 140), "lead shield", 22, GREY, 'rm'); T(d, F, (sx0 - 18, my + 172), "遮挡对照", 22, GREY, 'rm')
        T(d, F, (sx0 - 18, my + 204), "(control)", 21, GREY, 'rm')
        T(d, F, (mx, 668), "4-week-old male mouse   4 周龄雄性小鼠", 24, WHITE)
        T(d, F, (1360, 240), "single 16 Gy to one hind leg", 30, WHITE)
        T(d, F, (1360, 282), "单次 16 Gy 照射一侧后肢，对侧遮挡", 24, GREY)
        arrow(d, (1000, 430), (1740, 430), GREY, 3, 16)
        for x, lab in ((1060, "day 3"), (1180, "day 7"), (1330, "day 14"), (1620, "day 56")):
            d.ellipse([x - 9, 421, x + 9, 439], fill=GOLD)
            T(d, F, (x, 392), lab, 24, WHITE)
        T(d, F, (1360, 490), "tissue harvested at each time point  各时间点取材", 21, GREY)
        return
    # results list (steps 1-3)
    T(d, F, (430, 160), "day 56 · irradiated vs shielded", 26, WHITE)
    T(d, F, (430, 194), "第 56 天 · 受照腿 vs 遮挡腿", 22, GREY)
    rows = [("fibrosis", "纤维化", True, ICE), ("fiber size", "纤维变细", False, ROSE),
            ("satellite cells (d3, d56)", "卫星细胞", False, GREEN), ("endothelial cells", "内皮细胞", False, RED),
            ("FAPs", "FAP", False, ORANGE)]
    for i, (en, zh, up, col) in enumerate(rows):
        y = 262 + i * 84
        if i == 4:
            d.rounded_rectangle([160, y - 34, 700, y + 34], 16, fill=ORANGE + (40,), outline=ORANGE, width=3)
            T(d, F, (665, y), "?", 40, GOLD, font='title')
        updn(d, (200, y), up, col, .9)
        T(d, F, (240, y), en, 26, WHITE, 'lm')
        T(d, F, (240 + d.textlength(en, F('sans', 26)) + 16, y + 1), zh, 23, GREY, 'lm')
    fx, fy = 1000, 330
    if st == 1:
        fap(d, (fx, fy), 1.5)
        T(d, F, (fx + 110, fy - 100), "?", 56, GOLD, font='title')
        T(d, F, (fx, 470), "fewer FAPs …", 26, ORANGE); T(d, F, (fx, 504), "FAP 反而更少……", 22, GREY)
        return
    fap(d, (fx, fy), 1.5, grey=True)
    collagen(d, (1060, 400, 1190, 440), n=3, seed=2, w=4)
    clock(d, (820, 492), 28, GOLD, 3); trowel(d, (1000, 506), .75); flame(d, (1180, 494), 1.1)
    for x, en, zh in ((820, "senescent", "衰老"), (1000, "more fibrogenic", "更促纤维化"), (1180, "glycolytic", "糖酵解")):
        T(d, F, (x, 560), en, 22, WHITE); T(d, F, (x, 590), zh, 21, GREY)
    T(d, F, (1000, 648), "fewer FAPs, more scar   FAP 更少，瘢痕更多", 27, GOLD)
    if st >= 3:
        sasp(d, (1215, 320), n=12, R=70, seed=4)
        arrow(d, (1160, 300), (1340, 270), (230, 120, 160), 4, 16)
        T(d, F, (1250, 205), "secretome", 22, (230, 140, 175)); T(d, F, (1250, 233), "分泌组", 21, GREY)
        for x in (1430, 1560, 1690): sat_cell(d, (x, 255), .55)
        d.rounded_rectangle([1390, 410, 1730, 460], 25, outline=GREEN + (150,), width=3)
        for x in (1450, 1560, 1670): d.ellipse([x - 12, 428, x + 12, 442], outline=GREEN + (150,), width=2)
        for x in (1430, 1560, 1690): dline(d, (x, 285), (x, 400), GREEN + (150,), 3, 10)
        d.line([(1390, 345), (1730, 345)], fill=RED, width=7)
        xmark(d, (1560, 345), 18, RED, 6)
        T(d, F, (1560, 498), "impairs differentiation & fusion", 24, WHITE)
        T(d, F, (1560, 530), "削弱卫星细胞分化与融合", 22, GREY)
        stamp(d, F, (1560, 610), "rumor mill (SASP)  谣言工厂", ORANGE, 22)


# ================================================================ single-cell RNA-seq
UM = {'musc': (1060, 320), 'fap': (1360, 262), 'ec': (1625, 340), 'imm': (1300, 492)}
NET = {'musc': (1040, 340), 'fap': (1360, 262), 'ec': (1660, 370), 'imm': (1250, 528)}

def s_scrna(st, im, d, F, M):
    # left panel: dissociation -> droplets (steps 0-2)
    if st <= 2:
        for i, t in enumerate(("24 h", "56 d")): pill(d, F, (240 + i * 110, 165), t, (70, 90, 130), 22)
        T(d, F, (420, 165), "after IR  照射后", 22, GREY, 'lm')
        d.ellipse([170, 270, 330, 400], fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
        for dx, dy in ((-40, -20), (10, -30), (50, 5), (-20, 25), (25, 35)):
            d.ellipse([250 + dx - 16, 335 + dy - 13, 250 + dx + 16, 335 + dy + 13], fill=ROSE + (220,))
        arrow(d, (345, 335), (440, 335), WHITE, 4, 14)
        for i, col in enumerate((GREEN, ORANGE, RED, PURPLE)):
            y = 230 + i * 74
            d.ellipse([480, y - 30, 540, y + 30], fill=(180, 210, 230, 45), outline=(200, 225, 240), width=2)
            d.ellipse([498, y - 12, 522, y + 12], fill=col)
            for k, bw in enumerate((3, 6, 2, 5, 3, 4, 2, 6)):
                bx = 560 + k * 12; d.rectangle([bx, y - 18, bx + bw, y + 18], fill=(225, 230, 240))
        two(d, F, (420, 560), "single-cell RNA sequencing", "单细胞 RNA 测序：千万个各自的声音", 24, WHITE, GREY, zsize=21)
        T(d, F, (420, 625), "Collao 2025 · mouse", 22, GREY)
    if st <= 1:
        deep_r = 42 if st == 0 else 20
        umap(d, F, [(UM['musc'][0], UM['musc'][1], 85, GREEN, None, 60), (985, 262, deep_r, (40, 150, 75), None, 26 if st == 0 else 8),
                    (UM['fap'][0], UM['fap'][1], 110, ORANGE, None, 110), (UM['ec'][0], UM['ec'][1], 82, RED, None, 66),
                    (UM['imm'][0], UM['imm'][1], 98, PURPLE, None, 86)])
        T(d, F, (1060, 405), "MuSC 肌干细胞", 22, GREEN); T(d, F, (1360, 366), "FAP", 24, ORANGE)
        T(d, F, (1625, 422), "endothelial 内皮", 22, RED); T(d, F, (1300, 590), "monocyte / macrophage  单核/巨噬", 22, PURPLE)
        if st == 1:
            for (x, y) in ((1135, 262), (1455, 182), (1690, 280), (1395, 430)):
                pill(d, F, (x, y), "p21", (110, 115, 130), 20, 14)
            T(d, F, (870, 190), "deep-quiescent MuSCs ↓ (56 d)", 21, GREEN)
            T(d, F, (870, 218), "深度静息干细胞相对减少", 20, GREY)
            d.line([(930, 232), (972, 252)], fill=GREEN, width=2)
            T(d, F, (1300, 640), "p21 (Cdkn1a) senescence signature in every resident cell type", 22, WHITE)
            T(d, F, (1300, 670), "所有常驻细胞都出现衰老特征", 21, GREY)
        return
    # network (steps 2-3)
    dashed = st >= 3
    P = NET
    nodes = [('musc', 58, GREEN, "MuSC", None), ('fap', 74, ORANGE, "FAP", None), ('ec', 58, RED, "EC", "内皮"), ('imm', 64, PURPLE, "Mono/Mφ", "单核/巨噬")]
    for a_, b_ in (('musc', 'fap'), ('fap', 'ec'), ('musc', 'imm'), ('ec', 'imm')):
        if dashed: dline(d, P[a_], P[b_], (110, 120, 140), 2, 12)
        else: d.line([P[a_], P[b_]], fill=(110, 120, 140), width=2)
    fx, fy = P['fap']
    for k in range(9):
        a = math.pi * (1.05 + k * .11) if k < 5 else -math.pi * (.05 + (k - 5) * .11)
        r0, r1 = 82, 150
        pts = [(fx + (r0 + t) * math.cos(a) + 5 * math.sin(t / 9) * math.sin(a), fy + (r0 + t) * math.sin(a) * .8 - 5 * math.sin(t / 9) * math.cos(a)) for t in range(0, r1 - r0, 4)]
        d.line(pts, fill=ICE + (190,), width=4)
    T(d, F, (1090, 185), "main ECM source", 22, ICE); T(d, F, (1090, 213), "基质主要来源", 21, GREY)
    a, b = P['imm'], P['fap']
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p = (a[0] + 72 * math.cos(ang), a[1] + 72 * math.sin(ang)); q = (b[0] - 84 * math.cos(ang), b[1] - 84 * math.sin(ang))
    if dashed: darrow(d, p, q, PURPLE, 9, 30, 18)
    else: arrow(d, p, q, PURPLE, 10, 32)
    T(d, F, (1335, 425), "TGF-β → TGF-βR2", 23, TGFC, 'lm')
    for k, r, col, en, zh in nodes:
        node(d, F, P[k], r, col, en, zh, 22)
    if st == 2:
        T(d, F, (1360, 650), "who talks to whom (predicted)  谁在和谁说话", 22, WHITE)
    if st >= 3:
        stamp(d, F, (1360, 640), "predicted from mRNA — not yet proven by blocking", AMBER, 22)
        T(d, F, (1360, 678), "基于 mRNA 推断，尚未阻断验证", 20, AMBER)
        T(d, F, (460, 175), "trials still unheld  尚未开庭", 26, GOLD)
        for i, (en1, en2, zh) in enumerate((("block TGF-βR2 on FAPs", "in irradiated muscle?", "受照肌肉中阻断 FAP 的 TGF-βR2？"),
                                             ("clear senescent cells", "in vivo (senolytics)?", "体内清除衰老细胞？"))):
            y0 = 230 + i * 200
            drect(d, (170, y0, 760, y0 + 160), GOLD + (200,), 3, 14)
            d.rounded_rectangle([200, y0 + 52, 250, y0 + 102], 6, outline=GREY, width=3)
            T(d, F, (280, y0 + 42), en1, 24, WHITE, 'lm'); T(d, F, (280, y0 + 78), en2, 24, WHITE, 'lm')
            T(d, F, (280, y0 + 118), zh, 21, GREY, 'lm')


# ================================================================ real micrograph
def s_photo3(st, im, d, F, M):
    from PIL import Image as _I
    S = im.size[0] // 1920
    ph = _I.open(PHOTO).convert('RGBA')
    x0, y0, h = 220, 150, 490
    w = int(h * ph.width / ph.height)
    php = ph.resize((w * S, h * S), _I.LANCZOS)
    d.rounded_rectangle([x0 - 10, y0 - 10, x0 + w + 10, y0 + h + 10], 16, fill=(255, 255, 255, 30), outline=GOLD + (200,), width=2)
    im.paste(php, (x0 * S, y0 * S))
    k = h / ph.height
    pf = (x0 + 649 * k, y0 + 111 * k)      # a dark-red muscle fiber
    pc = (x0 + 422 * k, y0 + 255 * k)      # blue-green collagen between fibers
    lx = 1010
    for (px, py), y, en, zh, col in ((pf, 270, "muscle fibers", "肌纤维", (240, 120, 130)),
                                     (pc, 400, "collagen (scar)", "胶原（瘢痕）", (110, 210, 225))):
        d.line([(px, py), (lx - 20, y)], fill=(10, 16, 30), width=7); d.line([(px, py), (lx - 20, y)], fill=WHITE, width=3)
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=col, outline=WHITE, width=3)
        T(d, F, (lx, y - 18), en, 32, col, 'lm'); T(d, F, (lx, y + 22), zh, 26, GREY, 'lm')
    T(d, F, (lx, 520), "Trichrome stain: collagen stains blue-green", 24, WHITE, 'lm')
    T(d, F, (lx, 554), "三色染色：胶原呈蓝绿色，肌纤维呈暗红色", 22, GREY, 'lm')
    T(d, F, (lx, 600), "human back-muscle biopsy · illustrative, not from the cited studies", 21, GOLD, 'lm')
    T(d, F, (lx, 630), "人背部肌肉活检 · 示意图片，非所引研究", 21, GOLD, 'lm')
    T(d, F, (x0 + w / 2, 670), "Wikimedia Commons · Lenoir T, Guedj N, Boulu P, Guigui P, Benoist M · CC BY-SA 4.0", 20, GREY)


# ================================================================ 4  supply lines
NC = (560, 410); NR = 238; NSP = 94

def _niche_xs(d, st):
    cents = hexfibers(NC, NR, NSP)
    d.ellipse([NC[0] - NR - 12, NC[1] - NR - 12, NC[0] + NR + 12, NC[1] + NR + 12], fill=(60, 40, 50, 120), outline=(200, 160, 170), width=3)
    fr = NSP * .43
    for p in cents:
        d.ellipse([p[0] - fr, p[1] - fr, p[0] + fr, p[1] + fr], fill=ROSE + (225,), outline=(240, 150, 160), width=3)
    caps = []
    for p in cents:
        q = (p[0] + NSP / 2, p[1] + NSP * .2887)
        if math.dist(q, NC) < NR - 24: caps.append((q, p))
    hl = caps[len(caps) // 2 + 1]
    for i, (q, p) in enumerate(caps):
        capillary(d, q, 12, cut=(st >= 3 and q == hl[0]))
    if st >= 1:
        for i, (q, p) in enumerate(caps):
            if i % 3: continue
            ang = math.atan2(q[1] - p[1], q[0] - p[0])
            sc = (p[0] + (fr - 3) * math.cos(ang), p[1] + (fr - 3) * math.sin(ang))
            sat_cell(d, sc, .3, col=GREEN if not (st >= 3 and q == hl[0]) else (130, 135, 145))
            if st == 1: dcircle(d, ((q[0] + sc[0]) / 2, (q[1] + sc[1]) / 2), 26, GOLD, 22, 2)
    return hl


def s_niche(st, im, d, F, M):
    hl = _niche_xs(d, st)
    if st <= 1:
        T(d, F, (1390, 185), "supply lines = capillaries", 32, (240, 120, 110))
        T(d, F, (1390, 228), "补给线 = 毛细血管", 26, GREY)
    if st == 1:
        T(d, F, (1390, 300), "satellite cells sit beside capillaries", 26, GREEN)
        T(d, F, (1390, 336), "卫星细胞紧邻毛细血管", 24, GREY)
        T(d, F, (1390, 370), "mouse & human · Christov 2007", 21, GREY)
        panel(d, (1060, 420, 1720, 640))
        human(d, (1150, 545), .78)
        T(d, F, (1235, 480), "athletes: more capillaries", 24, WHITE, 'lm')
        T(d, F, (1235, 514), "→ more satellite cells", 24, GREEN, 'lm')
        T(d, F, (1235, 556), "运动员：毛细血管多，", 21, GREY, 'lm')
        T(d, F, (1235, 586), "卫星细胞也多", 21, GREY, 'lm')
        return
    if st >= 2:
        q = hl[0]
        d.ellipse([q[0] - 40, q[1] - 40, q[0] + 40, q[1] + 40], outline=GOLD, width=4)
        d.line([(q[0] + 30, q[1] - 28), (1000, 165)], fill=GOLD + (150,), width=2)
        d.line([(q[0] + 30, q[1] + 28), (1000, 640)], fill=GOLD + (150,), width=2)
        d.rounded_rectangle([1000, 165, 1780, 640], 22, fill=(20, 32, 55, 200), outline=GOLD + (200,), width=3)
        T(d, F, (1390, 198), "zoom  放大 · Christov 2007", 21, GREY)
        cx, cy = 1140, 370; sx, sy = 1630, 335
        if st == 2:
            capillary(d, (cx, cy), 62)
            sat_cell(d, (sx, sy), 1.1)
            d.line([(sx - 80, sy + 50), (sx - 80, sy - 25), (sx, sy - 75), (sx + 80, sy - 25), (sx + 80, sy + 50)], fill=GREEN + (170,), width=3)
            d.ellipse([sx - 75, 405, sx + 75, 437], fill=ROSE + (220,), outline=(240, 150, 160), width=2)
            arrow(d, (1215, 330), (1535, 330), GOLD, 5, 18)
            T(d, F, (1385, 262), "IGF-1 · HGF · bFGF", 22, GOLD); T(d, F, (1385, 294), "PDGF-BB · VEGF", 22, GOLD)
            arrow(d, (1545, 420), (1215, 410), (240, 120, 110), 4, 16)
            T(d, F, (1385, 372), "pro-angiogenic  促血管生成", 22, (240, 120, 110))
            T(d, F, (cx, 470), "endothelial cells", 22, WHITE); T(d, F, (cx, 498), "内皮细胞", 21, GREY)
            T(d, F, (sx, 470), "satellite cell → myocyte", 22, WHITE); T(d, F, (sx, 498), "卫星细胞 → 肌细胞", 21, GREY)
            T(d, F, (1390, 590), "two-way partnership   双向伙伴", 32, GOLD)
        else:
            capillary(d, (cx, cy), 62, cut=True)
            scissors(d, (cx + 10, cy - 105), .9)
            sat_cell(d, (sx, sy), 1.1, col=(130, 135, 145))
            for a_, b_ in (((sx - 100, 420), (sx - 30, 404)), ((sx - 15, 398), (sx + 50, 416)), ((sx + 60, 410), (sx + 105, 428)), ((sx - 70, 436), (sx + 20, 440))):
                d.line([a_, b_], fill=(130, 135, 145), width=3)
            T(d, F, (cx, 470), "vessel lost", 22, WHITE); T(d, F, (cx, 498), "血管消失", 21, GREY)
            T(d, F, (sx, 470), "niche collapses", 22, WHITE); T(d, F, (sx, 498), "龛塌陷", 21, GREY)
            T(d, F, (1390, 568), "lose the vessel, lose the niche", 32, (240, 110, 100))
            T(d, F, (1390, 606), "失去血管，失去龛", 24, GREY)


# ================================================================ vessel evidence board
def s_vesselev(st, im, d, F, M):
    d.rounded_rectangle([140, 140, 1780, 688], 20, fill=(120, 90, 60, 36), outline=(180, 150, 100), width=3)
    cols = [(420, "Body-wide (review)", "全身（综述）", WHITE), (960, "Muscle", "肌肉", ROSE), (1500, "Gut (analogy)", "肠道（类比）", GREY)]
    for cx, en, zh, col in cols:
        T(d, F, (cx, 178), en, 26, WHITE); T(d, F, (cx, 210), zh, 22, GREY)
    for x in (690, 1230): dline(d, (x, 165), (x, 665), (180, 150, 100, 160), 2, 12)
    # col 1
    d.rounded_rectangle([200, 280, 640, 400], 60, fill=RED + (60,), outline=RED, width=6)
    d.rounded_rectangle([200, 302, 640, 378], 38, fill=(70, 20, 30, 200))
    d.polygon([(370, 380), (400, 350), (450, 342), (500, 352), (530, 380)], fill=YELLOW + (230,))
    zz = [(260 + k * 18, 304 + (6 if k % 2 else 0)) for k in range(18)]
    d.line(zz, fill=(255, 170, 120), width=3)
    T(d, F, (420, 448), "radiation injures vessel lining,", 22, WHITE)
    T(d, F, (420, 478), "starts & speeds atherosclerosis", 22, WHITE)
    T(d, F, (420, 512), "损伤血管内壁，引发并加速动脉硬化", 20, GREY)
    T(d, F, (420, 546), "Venkatesulu 2018", 20, GREY)
    T(d, F, (420, 606), "A-bomb survivors: inflammation ↑", 21, GOLD)
    T(d, F, (420, 636), "原爆幸存者血液炎症信号增多", 20, GREY)
    if st >= 1:
        mouse(d, (790, 285), .45)
        T(d, F, (860, 266), "mouse 16 Gy · day 56", 22, WHITE, 'lm')
        T(d, F, (860, 298), "endothelial cells ↓  内皮细胞减少", 21, GREY, 'lm')
        vc = (790, 410)
        d.ellipse([vc[0] - 62, vc[1] - 62, vc[0] + 62, vc[1] + 62], fill=ICE + (70,), outline=ICE, width=2)
        d.ellipse([vc[0] - 44, vc[1] - 44, vc[0] + 44, vc[1] + 44], fill=(70, 20, 30, 230), outline=RED, width=4)
        for k in range(5):
            a = k * 1.257; d.ellipse([vc[0] + 30 * math.cos(a) - 14, vc[1] + 30 * math.sin(a) - 10, vc[0] + 30 * math.cos(a) + 14, vc[1] + 30 * math.sin(a) + 10], fill=(230, 120, 110, 230))
        for a in (0.4, 2.2, 4.0):
            d.ellipse([vc[0] + 74 * math.cos(a) - 5, vc[1] + 74 * math.sin(a) - 5, vc[0] + 74 * math.cos(a) + 5, vc[1] + 74 * math.sin(a) + 5], fill=(235, 95, 90))
        T(d, F, (870, 376), "rat 90 Gy · electron microscopy", 21, WHITE, 'lm')
        T(d, F, (870, 406), "swollen, leaky; scar around vessels", 20, GREY, 'lm')
        T(d, F, (870, 436), "内皮肿胀·渗漏·血管周围纤维化", 20, GREY, 'lm')
    if st >= 2:
        d.rounded_rectangle([715, 492, 1210, 600], 14, fill=(150, 155, 165, 45), outline=(170, 175, 185), width=2)
        T(d, F, (735, 516), "rat 8 Gy single · 12 weeks", 21, WHITE, 'lm')
        T(d, F, (735, 546), "no significant flow change", 21, WHITE, 'lm')
        T(d, F, (735, 576), "无显著变化 · Siemionow 1999", 20, GREY, 'lm')
        gc = (1150, 572)
        d.line(arcpts(gc, 40, 40, math.pi, 2 * math.pi, 24), fill=GREY, width=4)
        d.line([gc, (gc[0] - 34, gc[1] - 18)], fill=GOLD, width=4)
        T(d, F, (1150, 512), "dose", 20, GREY)
    if st >= 3:
        cx, top, by, r = 1500, 255, 375, 70
        R2 = r + 26
        loop = [(cx - R2, top - 10)] + [(cx - R2 * math.cos(k * math.pi / 30), by + R2 * math.sin(k * math.pi / 30)) for k in range(31)] + [(cx + R2, top - 10)]
        d.line(loop, fill=RED, width=5)
        cells = [(cx - r, top + k * 30) for k in range(4)] + [(cx - r * math.cos(k * math.pi / 6), by + r * math.sin(k * math.pi / 6)) for k in range(1, 6)] + [(cx + r, top + k * 30) for k in range(3, -1, -1)]
        for i, (x, y) in enumerate(cells):
            stem = 4 <= i <= 8
            d.ellipse([x - 16, y - 16, x + 16, y + 16], fill=(GREEN if stem else (220, 170, 170)) + (225,), outline=WHITE, width=2)
            if stem and i in (5, 7): xmark(d, (x, y), 10, RED, 4)
        xmark(d, (cx + r + 24, 320), 13, RED, 5); xmark(d, (cx - r - 24, 320), 13, RED, 5)
        T(d, F, (cx + r + 52, 300), "①", 22, RED); T(d, F, (cx - r - 56, by + 30), "②", 22, RED)
        T(d, F, (1500, 504), "① vessel lining dies first  内皮先死", 20, (240, 120, 110))
        T(d, F, (1500, 536), "② then crypt stem cells  再到干细胞", 20, WHITE)
        T(d, F, (1500, 572), "bFGF or ASMase knockout → spared", 20, GREEN)
        T(d, F, (1500, 602), "阻止内皮死亡 → 干细胞得以保全", 20, GREY)
        T(d, F, (1500, 636), "Paris 2001 · mouse gut", 20, GREY)
        stamp(d, F, (960, 628), "HYPOTHESIS: vessels first in muscle", HYP, 22)
        T(d, F, (960, 664), "肌肉中“血管先倒”= 假说（证据有限）", 20, (230, 110, 100))


# ================================================================ 5  mitochondria
def s_mito(st, im, d, F, M):
    if st <= 1:
        mc = (600, 390)
        d.rectangle([760, 175, 815, 290], fill=(120, 110, 110), outline=(170, 160, 160), width=2)
        for x, y, r in ((800, 158, 14), (835, 145, 18), (875, 138, 14)):
            d.ellipse([x - r, y - r, x + r, y + r], fill=(160, 165, 175, 120))
        mito(d, mc, w=560, h=240, sparks=0, swollen=False)
        sp0 = [(930, 300), (955, 470), (300, 510)]
        sp1 = [(250, 300), (330, 250), (900, 230), (980, 390), (880, 535), (420, 540)]
        for p in sp0 + (sp1 if st >= 1 else []): spark(d, p, 13)
        T(d, F, (215, 400), "ROS  活性氧", 26, GOLD)
        if st >= 1: T(d, F, (210, 230), "RNS", 26, (240, 120, 110), 'mm')
        two(d, F, (600, 622), "mitochondrion = power plant", "线粒体 = 发电厂", 28, WHITE, GREY)
        if st >= 1:
            panel(d, (1150, 165, 1760, 395))
            dish(d, F, (1260, 290), 80)
            for x in (1230, 1290): sat_cell(d, (x, 290), .35)
            for p in ((1225, 250), (1300, 252), (1330, 310)): spark(d, p, 9)
            T(d, F, (1360, 235), "satellite cells in culture", 22, WHITE, 'lm')
            T(d, F, (1360, 272), "≥5 Gy: ROS/RNS stay high", 22, GOLD, 'lm')
            T(d, F, (1360, 309), "持续升高 · Caiozzo 2010", 20, GREY, 'lm')
            panel(d, (1150, 420, 1760, 650))
            mito(d, (1265, 535), w=170, h=64, swollen=True)
            T(d, F, (1375, 495), "rat 90 Gy · electron microscopy", 21, WHITE, 'lm')
            T(d, F, (1375, 532), "swollen mitochondria", 22, (240, 150, 110), 'lm')
            T(d, F, (1375, 569), "线粒体肿胀 · Zhou 2018", 20, GREY, 'lm')
        return
    # steps 2-3: Amorim 2020
    dline(d, (960, 150), (960, 650), DIM, 3)
    T(d, F, (540, 160), "Amorim 2020 · mouse 6 Gy", 26, WHITE)
    for k, (cx, frac, lab) in enumerate(((340, .5, "control  对照"), (740, .2, "6 Gy"))):
        c = (cx, 322); rnd = random.Random(21)
        d.ellipse([cx - 128, 194, cx + 128, 450], fill=(60, 40, 50, 120), outline=(200, 160, 170), width=3)
        for p in hexfibers(c, 125, 46):
            dark = rnd.random() < frac
            d.ellipse([p[0] - 20, p[1] - 20, p[0] + 20, p[1] + 20], fill=((105, 35, 60) if dark else (235, 160, 170)) + (235,))
        T(d, F, (cx, 474), lab, 24, WHITE)
    T(d, F, (540, 508), "dark = oxidative fibers   深色 = 氧化型纤维", 20, GREY)
    for i, (en, zh) in enumerate((("mitochondrial enzyme activity", "线粒体酶活性"), ("fat oxidation", "脂肪氧化"), ("glucose uptake", "葡萄糖摄取"))):
        y = 552 + i * 44
        updn(d, (250, y), False, RED, .7)
        T(d, F, (285, y), en, 23, WHITE, 'lm')
        T(d, F, (285 + d.textlength(en, F('sans', 23)) + 16, y + 1), zh, 21, GREY, 'lm')
    if st >= 3:
        mouse(d, (1120, 280), .8)
        spark(d, (1080, 230), 12)
        arrow(d, (1215, 285), (1345, 285), WHITE, 4, 16)
        T(d, F, (1280, 252), "taken out  取出", 20, GREY)
        dish(d, F, (1480, 290), 105)
        for x in (1440, 1490, 1540): sat_cell(d, (x, 290), .35)
        for k in range(3): updn(d, (1625 + k * 36, 290), False, RED, .55)
        T(d, F, (1480, 375), "cells remember   细胞记住了", 30, GOLD)
        x, y = 1090, 520
        d.polygon([(x, y - 34), (x + 20, y - 2)] + arcpts((x, y + 8), 22, 22, -0.4, math.pi + 0.4, 16) + [(x - 20, y - 2)], fill=(210, 50, 60))
        T(d, F, (1135, 500), "total-body-irradiation survivors:", 21, WHITE, 'lm')
        T(d, F, (1135, 530), "parallel blood lipid signature", 21, WHITE, 'lm')
        T(d, F, (1135, 560), "全身照射幸存者：相似脂质特征", 20, GREY, 'lm')
        pill(d, F, (1215, 604), "association 关联", AMBER, 20, 14)
        fap(d, (1650, 525), .85); flame(d, (1722, 470), .9)
        T(d, F, (1660, 590), "FAPs glycolytic", 20, ORANGE); T(d, F, (1660, 618), "糖酵解 (Collao 2023)", 20, GREY)


# ================================================================ O'Connor 2022
def _wheel(d, c, r=88, locked=False):
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], outline=(190, 195, 205), width=6)
    for k in range(8):
        a = k * .785; d.line([(x, y), (x + r * math.cos(a), y + r * math.sin(a))], fill=(150, 155, 165), width=3)
    d.line([(x, y + r), (x - 30, y + r + 40)], fill=(150, 155, 165), width=5); d.line([(x, y + r), (x + 30, y + r + 40)], fill=(150, 155, 165), width=5)


def s_oconnor(st, im, d, F, M):
    if st == 0:
        mouse(d, (400, 400), 1.35)
        beam(d, (235, 150), (342, 448), w=8)
        T(d, F, (420, 190), "3 × 8.2 Gy", 32, GOLD, 'lm'); T(d, F, (420, 228), "knee → foot  膝至足", 22, GREY, 'lm')
        T(d, F, (400, 555), "juvenile male mouse  幼年雄性小鼠", 24, WHITE)
        arrow(d, (620, 400), (820, 400), WHITE, 4, 18)
        for x0, locked, en in ((880, True, "locked wheel  锁定跑轮"), (1360, False, "free wheel  自由跑轮")):
            d.rounded_rectangle([x0, 250, x0 + 360, 530], 16, outline=(150, 160, 175), width=3)
            for xx in range(x0 + 30, x0 + 360, 40): d.line([(xx, 252), (xx, 270)], fill=(150, 160, 175), width=2)
            c = (x0 + 180, 380); _wheel(d, c, 88, locked)
            if locked: padlock(d, (c[0], c[1] - 10), .8)
            else:
                for a0 in (-2.6, 0.55):
                    pts = arcpts(c, 106, 106, a0, a0 + 1.3, 20)
                    d.line(pts[:-1], fill=GREEN, width=5); arrow(d, pts[-3], pts[-1], GREEN, 5, 16)
            T(d, F, (x0 + 180, 572), en, 24, WHITE)
        pill(d, F, (1300, 640), "1 month   一个月", (70, 100, 150), 24)
        return
    by, k = 380, 3.6
    def vbar(x, v, col, lab_en, lab_zh, vt):
        h = abs(v) * k
        if v < 0:
            d.rounded_rectangle([x - 45, by, x + 45, by + h], 8, fill=col + (215,))
            T(d, F, (x, by + h + 26), vt, 28, WHITE)
            T(d, F, (x, by - 62), lab_en, 22, WHITE); T(d, F, (x, by - 32), lab_zh, 20, GREY)
        else:
            d.rounded_rectangle([x - 45, by - h, x + 45, by], 8, fill=col + (215,))
            T(d, F, (x, by - h - 26), vt, 28, WHITE)
            T(d, F, (x, by + 30), lab_en, 22, WHITE); T(d, F, (x, by + 60), lab_zh, 20, GREY)
    # left: irradiated sedentary vs non-irradiated
    T(d, F, (540, 160), "irradiated · sedentary vs non-irradiated", 24, WHITE)
    T(d, F, (540, 192), "受照久坐 vs 未照射", 21, GREY)
    d.line([(190, by), (560, by)], fill=GREY, width=2)
    vbar(290, -27, ROSE, "EDL force", "快肌比肌力", "−27%")
    vbar(470, -14, ROSE, "soleus force", "比目鱼肌", "−14%")
    for (y0, big, en, zh) in ((250, "+73%", "protein oxidation", "蛋白质氧化"), (400, "", "calcium handling", "disturbed  钙调控紊乱")):
        d.rounded_rectangle([620, y0, 900, y0 + 120], 16, fill=(214, 150, 40, 35), outline=(214, 150, 40, 200), width=2)
        if big:
            T(d, F, (760, y0 + 34), big, 34, GOLD); T(d, F, (760, y0 + 74), en, 22, WHITE); T(d, F, (760, y0 + 100), zh, 20, GREY)
        else:
            d.line([(660 + i * 8, y0 + 34 + 10 * math.sin(i * .9)) for i in range(26)], fill=GOLD, width=4)
            T(d, F, (760, y0 + 70), en, 22, WHITE); T(d, F, (760, y0 + 98), zh, 20, GREY)
    if st >= 2:
        dline(d, (960, 150), (960, 610), DIM, 3)
        T(d, F, (1390, 160), "+ free wheel vs sedentary (both irradiated)", 24, WHITE)
        T(d, F, (1390, 192), "跑轮 vs 久坐（均受照）", 21, GREY)
        d.line([(1020, by), (1740, by)], fill=GREY, width=2)
        vbar(1100, 37, GREEN, "EDL force", "比肌力", "+37%")
        vbar(1290, -50, GREEN, "mito ROS", "线粒体活性氧", "−50%")
        vbar(1480, -35, GREEN, "nitrosylation", "亚硝基化", "−35%")
        x = 1650
        updn(d, (x, by - 60), True, GREEN, 1.6)
        T(d, F, (x, by + 30), "PGC-1α ↑", 22, WHITE); T(d, F, (x, by + 60), "线粒体建造者", 20, GREY)
    if st >= 3:
        stamp(d, F, (1340, 650), "correlated with better function · association  关联", AMBER, 22)
        arrow(d, (1690, 650), (1780, 650), GOLD, 5, 18)
        T(d, F, (1730, 600), "reversible?", 21, GOLD); T(d, F, (1730, 626), "可逆？→ Ep4", 20, GOLD)


# ================================================================ working model
MN = {1: (390, 255), 2: (960, 255), 3: (1530, 255), 4: (1530, 545), 5: (960, 590), 6: (390, 545)}

def s_model(st, im, d, F, M):
    stamp(d, F, (960, 150), "WORKING MODEL · HYPOTHESIS   工作模型 · 假说", HYP, 24)
    data = {1: ("beam → fiber survives ✓", "satellite cells ↓  卫星细胞减少", GREEN),
            2: ("senescence (p21) spreads", "常驻细胞衰老 · SASP 谣言工厂", (170, 175, 190)),
            3: ("macrophage —TGF-β→ FAP", "经 TGF-βR2 接收", PURPLE),
            4: ("senescent FAP → matrix", "分泌组拖住干细胞  ⊣ stem cells", ORANGE),
            5: ("capillaries ↓ → niche lost", "毛细血管减少，失去龛", RED),
            6: ("mitochondria: ROS ↑ → force ↓", "线粒体活性氧↑，肌力↓", GOLD)}
    data[4] = ("senescent FAP → matrix (scar)", "secretome holds back stem cells", ORANGE)
    show = {0: [1], 1: [1, 2, 3], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6]}[st]
    order = [1, 2, 3, 4, 5, 6, 1]
    def edge(a, b):
        (ax, ay), (bx, by) = MN[a], MN[b]
        ang = math.atan2(by - ay, bx - ax)
        def off(cx, cy, ang):
            dx, dy = math.cos(ang), math.sin(ang)
            t = min(200 / abs(dx) if dx else 1e9, 58 / abs(dy) if dy else 1e9) + 12
            return (cx + dx * t, cy + dy * t)
        return off(ax, ay, ang), off(bx, by, ang + math.pi)
    for i in range(6):
        a, b = order[i], order[i + 1]
        if a in show and b in show and (i < 5 or st >= 3):
            p, q = edge(a, b)
            arrow(d, p, q, GOLD if st >= 3 else (170, 180, 200), 5 if st >= 3 else 4, 18)
    for n in show:
        x, y = MN[n]; en, zh, col = data[n]
        d.rounded_rectangle([x - 200, y - 58, x + 200, y + 58], 18, fill=col + (45,), outline=col, width=3)
        T(d, F, (x, y - 18), en, 24, WHITE); T(d, F, (x, y + 20), zh, 21, GREY)
        if n == 4:
            pass
    if 3 in show:
        x, y = MN[3]
        dline(d, (x - 50, y + 76), (x - 50, y + 116), (150, 150, 160), 3, 8)
        T(d, F, (x - 66, y + 96), "TNF cull?  untested 未检验", 20, (150, 155, 170), 'rm')
    if 4 in show:
        T(d, F, (MN[4][0], MN[4][1] + 80), "分泌组 → 干细胞受抑", 20, GREY)
    if st >= 3:
        T(d, F, (960, 395), "a wound where repair signals never stop", 28, GOLD, font='gari')
        T(d, F, (960, 432), "修复信号永不停歇的伤口", 24, GOLD)
        T(d, F, (960, 488), "→ weak 变弱 + stiff 变硬 · years later 多年后", 26, WHITE)


# ================================================================ open cases
def s_gaps(st, im, d, F, M):
    d.rounded_rectangle([160, 140, 1760, 590], 20, fill=(150, 110, 70, 70), outline=(190, 150, 100), width=3)
    T(d, F, (W / 2, 180), "Open cases   悬案", 34, GOLD)
    cards = [("Macrophage time course", "in irradiated muscle", "NOT MAPPED", "受照肌肉巨噬细胞时程", "未描绘"),
             ("Senolytics in irradiated", "muscle, in a living animal", "UNTESTED", "衰老清除剂", "未在体内验证"),
             ("Muscle vessel evidence thin:", "vessel or stem cell first?", "UNKNOWN", "肌肉血管证据有限", "谁先倒下？")]
    for i, (a, b, verdict, z1, z2) in enumerate(cards):
        x0 = 240 + i * 500; bx = (x0, 230, x0 + 440, 550)
        corkcard(d, F, bx)
        T(d, F, (x0 + 30, 262), f"#{i + 1}", 22, INK2, 'lm')
        if st >= (1 if i < 2 else 2):
            cx = x0 + 220
            T(d, F, (cx, 312), a, 24, INK); T(d, F, (cx, 346), b, 24, INK)
            tw = d.textlength(verdict, F('sans', 26))
            d.rounded_rectangle([cx - tw / 2 - 24, 384, cx + tw / 2 + 24, 436], 8, outline=(190, 50, 45), width=4)
            T(d, F, (cx, 410), verdict, 26, (190, 50, 45))
            T(d, F, (cx, 474), z1, 22, INK2); T(d, F, (cx, 506), z2, 22, INK2)
    if st >= 3:
        x0, x1, y = 200, 1340, 652
        d.line([(x0, y), (x1, y)], fill=GOLD, width=3)
        labs = ["mouse 6 Gy", "mouse 16 Gy", "juvenile 3×8.2 Gy", "rat 6×8 Gy", "rat 90 Gy"]
        for j, lab in enumerate(labs):
            x = x0 + 70 + j * (x1 - x0 - 140) / 4
            d.line([(x, y - 10), (x, y + 10)], fill=GOLD, width=3)
            T(d, F, (x, y - 30), lab, 21, WHITE)
        T(d, F, (1400, 628), "almost all rodents", 24, GOLD, 'lm'); T(d, F, (1400, 662), "几乎都是啮齿类", 22, GREY, 'lm')


SCENES = {
    'recap': s_recap,
    'fap': s_fap,
    'fapexp': s_fapexp,
    'bench': s_bench,
    'macro': s_macro,
    'balance': s_balance,
    'lock': s_lock,
    'collao': s_collao,
    'scrna': s_scrna,
    'photo:Masson trichrome stain skeletal muscle fibrosis': s_photo3,
    'niche': s_niche,
    'vesselev': s_vesselev,
    'mito': s_mito,
    'oconnor': s_oconnor,
    'model': s_model,
    'gaps': s_gaps,
}
