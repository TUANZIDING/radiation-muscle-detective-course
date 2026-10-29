from prims import *
# Episode 4 scenes for 'After the Beam' (From Bench to Bedside).
# Each scene f(st, im, d, F, M) draws step st; steps build progressively.
# Diagram area y 120..690; REF card at right x>1150, y 698..742; subtitles below 760.

AMBER = SCOL['ASSOCIATION']; FGREEN = SCOL['FACT']; HRED = SCOL['HYPOTHESIS']; BBLUE = SCOL['BENCH']
CREAM = (238, 230, 205); INK = (40, 40, 52); INK2 = (95, 85, 72)
PANEL = (34, 46, 72)


# ---------------- helpers ----------------
def tw(d, F, s, size, font='sans'):
    return d.textlength(s, F(font, size))

def TT(d, F, xy, s, size=26, col=WHITE, anchor='mm', maxw=None, font='sans', minsize=20):
    """Text that shrinks to fit maxw (never below minsize)."""
    if maxw:
        while size > minsize and tw(d, F, s, size, font) > maxw: size -= 1
    T(d, F, xy, s, size, col, anchor, font)
    return size

def bil(d, F, xy, en, zh=None, size=26, col=WHITE, zcol=GREY, anchor='mm', maxw=None, gap=None):
    """EN line with ZH line beneath (both shrink-to-fit)."""
    g = gap or size * 0.66
    if zh:
        TT(d, F, (xy[0], xy[1] - g), en, size, col, anchor, maxw)
        TT(d, F, (xy[0], xy[1] + g), zh, int(size * .88), zcol, anchor, maxw)
    else:
        TT(d, F, xy, en, size, col, anchor, maxw)

def wrap(d, F, s, size, maxw):
    cjk = any('\u4e00' <= ch <= '\u9fff' for ch in s) and ' ' not in s
    out, cur = [], ''
    toks = list(s) if cjk else s.split(' ')
    for t in toks:
        nxt = (cur + t) if cjk else ((cur + ' ' + t) if cur else t)
        if tw(d, F, nxt, size) <= maxw or not cur: cur = nxt
        else: out.append(cur); cur = t
    if cur: out.append(cur)
    return out

def para(d, F, xy, s, size, col, maxw, lh=None, anchor='mm'):
    lines = wrap(d, F, s, size, maxw); lh = lh or int(size * 1.3)
    y = xy[1] - (len(lines) - 1) * lh / 2
    for ln in lines:
        T(d, F, (xy[0], y), ln, size, col, anchor); y += lh
    return len(lines) * lh

def panel(d, bx, col=PANEL, a=150, outline=None, r=22, w=2):
    d.rounded_rectangle(bx, r, fill=col + (a,), outline=(outline + (200,)) if outline else None, width=w)

def chip(d, F, c, text, col=BLUE, size=24, txt=WHITE):
    w_ = tw(d, F, text, size)
    d.rounded_rectangle([c[0] - w_ / 2 - 20, c[1] - size * .9, c[0] + w_ / 2 + 20, c[1] + size * .9], size * .9, fill=col + (70,), outline=col + (230,), width=2)
    T(d, F, c, text, size, txt)
    return w_ + 40

def chips_row(d, F, cy, items, size=23, gap=26, cx=W / 2):
    ws = [tw(d, F, t, size) + 40 for t, _ in items]; x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    for (t, c), w_ in zip(items, ws):
        chip(d, F, (x + w_ / 2, cy), t, c, size); x += w_ + gap

def bolt(d, c, s=1.0, col=GOLD):
    x, y = c
    pts = [(x + 8 * s, y - 40 * s), (x - 16 * s, y + 4 * s), (x + 2 * s, y + 4 * s), (x - 8 * s, y + 40 * s), (x + 18 * s, y - 8 * s), (x, y - 8 * s)]
    d.polygon(pts, fill=col + (235,), outline=(255, 245, 210))

def pin(d, c, col=RED):
    d.ellipse([c[0] - 11, c[1] - 11, c[0] + 11, c[1] + 11], fill=col, outline=(255, 190, 180), width=2)
    d.ellipse([c[0] - 4, c[1] - 6, c[0] + 1, c[1] - 1], fill=(255, 230, 230))

def fiberseg(d, x0, x1, y, h=40, col=ROSE, nuclei=True):
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], h / 2, fill=col + (215,), outline=(240, 150, 160), width=2)
    for x in range(int(x0) + 14, int(x1) - 8, 12):
        d.line([(x, y - h / 2 + 6), (x, y + h / 2 - 6)], fill=(235, 130, 140, 110), width=1)
    if nuclei:
        for x in range(int(x0) + 40, int(x1) - 20, 70):
            d.ellipse([x - 11, y - 5, x + 11, y + 5], fill=(70, 70, 150))

def shieldicon(d, c, s=1.0, col=(150, 200, 255)):
    x, y = c
    pts = [(x, y - 30 * s), (x + 24 * s, y - 20 * s), (x + 22 * s, y + 6 * s), (x, y + 30 * s), (x - 22 * s, y + 6 * s), (x - 24 * s, y - 20 * s)]
    d.polygon(pts, fill=col + (110,), outline=col)
    check(d, (x, y - 2 * s), 10 * s, WHITE, max(2, int(4 * s)))

def door(d, F, c, h=320):
    x, y = c; w_ = h * .5
    d.rectangle([x - w_ / 2 - 14, y - h / 2 - 14, x + w_ / 2 + 14, y + h / 2], fill=(90, 70, 50, 200))
    d.rectangle([x - w_ / 2, y - h / 2, x + w_ / 2, y + h / 2], fill=(160, 120, 80, 235), outline=(220, 180, 130), width=3)
    for yy in (y - h / 2 + 20, y + 10):
        d.rectangle([x - w_ / 2 + 18, yy, x + w_ / 2 - 18, yy + h * .36], outline=(210, 170, 120), width=2)
    d.ellipse([x + w_ / 2 - 34, y - 6, x + w_ / 2 - 20, y + 8], fill=GOLD)

def drop(d, c, s=1.0, col=RED):
    x, y = c
    pts = [(x, y - 50 * s)]
    for i in range(0, 21):
        a = math.pi * (1 + i / 20)
        pts.append((x + 34 * s * math.cos(a + math.pi), y + 10 * s - 34 * s * math.sin(a + math.pi)))
    d.polygon([(x, y - 54 * s), (x + 30 * s, y - 2 * s)] + [(x + 32 * s * math.cos(t / 20 * math.pi), y + 12 * s + 32 * s * math.sin(t / 20 * math.pi)) for t in range(21)] + [(x - 30 * s, y - 2 * s)], fill=col + (200,), outline=(255, 150, 140))

def pill_capsule(d, c, L=150, h=56, c1=ORANGE, c2=(240, 240, 240), angle=0):
    x, y = c
    d.rounded_rectangle([x - L / 2, y - h / 2, x, y + h / 2], h / 2, fill=c1 + (240,))
    d.rectangle([x - h / 2, y - h / 2, x, y + h / 2], fill=c1 + (240,))
    d.rounded_rectangle([x, y - h / 2, x + L / 2, y + h / 2], h / 2, fill=c2 + (240,))
    d.rectangle([x, y - h / 2, x + h / 2, y + h / 2], fill=c2 + (240,))
    d.rounded_rectangle([x - L / 2 + 10, y - h / 2 + 8, x + L / 2 - 10, y - h / 2 + 18], 5, fill=(255, 255, 255, 70))

def softgel(d, c, rx=60, ry=38, col=(240, 200, 70)):
    x, y = c
    d.ellipse([x - rx, y - ry, x + rx, y + ry], fill=col + (225,), outline=(255, 235, 160), width=3)
    d.ellipse([x - rx * .6, y - ry * .7, x - rx * .05, y - ry * .3], fill=(255, 255, 230, 120))

def person(d, c, s=1.0, col=(120, 135, 160)):
    x, y = c
    d.ellipse([x - 6 * s, y - 16 * s, x + 6 * s, y - 4 * s], fill=col)
    d.rounded_rectangle([x - 9 * s, y - 2 * s, x + 9 * s, y + 16 * s], 6 * s, fill=col)

def stampc(d, F, c, text, key, size=24):
    stamp(d, F, c, text, SCOL[key], size)


# ---------------- cold open ----------------
def s_case4(st, im, d, F, M):
    d.rounded_rectangle([110, 140, 1450, 682], 26, fill=(86, 64, 44, 70), outline=(170, 140, 100), width=3)
    cards = [(150, 590), (590, 1030), (1030, 1410)]
    pins = []
    for i, (x0, x1) in enumerate(cards):
        if st < i: continue
        x0b, x1b = x0 + 12, x1 - 12; cx = (x0b + x1b) / 2
        d.rounded_rectangle([x0b, 196, x1b, 600], 16, fill=(28, 38, 60, 235), outline=(214, 196, 150), width=2)
        pins.append((cx, 200))
        if i == 0:
            helix(d, cx - 160, cx + 160, 270, 26, breaks=(cx + 10,), w=5)
            for k in range(6):
                a = k * 1.047; d.line([(cx + 10, 270), (cx + 10 + 26 * math.cos(a), 270 + 26 * math.sin(a))], fill=GOLD, width=3)
            fiberseg(d, cx - 150, cx + 70, 390, 46)
            shieldicon(d, (cx + 130, 390), 1.2)
            bil(d, F, (cx, 480), "Beam → DNA breaks", "射线 → DNA断裂", 27, WHITE, maxw=380)
            bil(d, F, (cx, 556), "fiber survives", "纤维存活", 24, GREEN, GREY, maxw=380)
        if i == 1:
            fiberseg(d, cx - 170, cx + 40, 330, 50)
            sat_cell(d, (cx - 110, 293), .5); sat_cell(d, (cx - 20, 293), .5, col=(60, 120, 80)); sat_cell(d, (cx + 10, 367), .5, dead=True)
            T(d, F, (cx - 65, 250), "PAX7", 20, GREEN)
            child(d, (cx + 130, 340), .9)
            T(d, F, (cx + 130, 430), "lifelong 终生", 20, GOLD)
            bil(d, F, (cx, 506), "Satellite cells lost", "卫星细胞丢失", 27, WHITE, maxw=380)
        if i == 2:
            fap(d, (cx - 120, 272), .55, angle=.3)
            arrow(d, (cx - 60, 272), (cx + 10, 272), ORANGE, 4, 14)
            collagen(d, (cx + 20, 248, cx + 170, 300), 5, col=ICE)
            T(d, F, (cx - 30, 240), "TGF-β", 20, ORANGE)
            bil(d, F, (cx, 352), "FAPs senescent → scar", "FAPs衰老 → 瘢痕", 26, WHITE, maxw=360)
            capillary(d, (cx - 90, 450), 22, cut=True); capillary(d, (cx - 130, 450), 13)
            mito(d, (cx + 75, 450), 110, 56)
            T(d, F, (cx - 105, 512), "vessels thin", 20, (240, 140, 130)); T(d, F, (cx - 105, 540), "血管变稀", 20, GREY)
            T(d, F, (cx + 75, 512), "mitochondria falter", 20, (240, 160, 120)); T(d, F, (cx + 75, 540), "线粒体失灵", 20, GREY)
    if len(pins) > 1:
        for a, b in zip(pins, pins[1:]):
            d.line([a, ((a[0] + b[0]) / 2, a[1] + 26), b], fill=(210, 60, 60), width=4, joint='curve')
    if st >= 3:
        door(d, F, (1640, 400), 330)
        T(d, F, (1640, 186), "Clinic  诊室", 30, WHITE)
        T(d, F, (1640, 396), "?", 84, GOLD)
        d.line([pins[-1], (1500, 230), (1570, 300)], fill=(210, 60, 60), width=4, joint='curve')
        T(d, F, (780, 644), "working model, built in mice  ·  工作模型，来自小鼠", 26, GOLD)
    for p in pins: pin(d, p)


# ---------------- 1 human cases ----------------
def bust(d, x=520):
    col = (70, 82, 104); oc = (150, 165, 190)
    d.polygon([(x - 280, 690), (x - 270, 520), (x - 200, 462), (x - 60, 432), (x + 60, 432), (x + 200, 462), (x + 270, 520), (x + 280, 690)], fill=col + (235,), outline=oc)
    d.rounded_rectangle([x - 58, 330, x + 58, 450], 30, fill=col + (255,))
    d.ellipse([x - 92, 150, x + 92, 360], fill=col + (255,), outline=oc, width=3)
    d.line([(x - 58, 360), (x - 58, 440)], fill=oc, width=3); d.line([(x + 58, 360), (x + 58, 440)], fill=oc, width=3)
    for sx in (-1, 1): d.ellipse([x + sx * 36 - 9, 232, x + sx * 36 + 9, 246], fill=(40, 48, 66))
    d.line([(x - 26, 314), (x + 26, 314)], fill=(40, 48, 66), width=4)
    d.line([(x - 60, 330), (x, 356), (x + 60, 330)], fill=(110, 122, 146), width=2, joint='curve')

def s_rfs(st, im, d, F, M):
    x = 520
    bust(d, x)
    d.rounded_rectangle([x - 130, 362, x + 130, 476], 16, fill=GOLD + (40,), outline=GOLD + (190,), width=3)
    T(d, F, (x - 140, 420), "RT field 照射野", 22, GOLD, 'rm')
    bil(d, F, (1290, 200), "Radiation fibrosis syndrome", "放射纤维化综合征", 38, WHITE, (220, 200, 160), gap=28)
    bil(d, F, (1290, 300), "progressive tissue hardening", "进行性组织硬化", 26, (200, 215, 235), GREY)
    if st >= 1:
        # anatomy on the bust: cord, roots, plexus, nerve, muscle
        d.line([(x, 372), (x, 640)], fill=GOLD, width=7)
        for s_ in (-1, 1):
            d.line([(x, 410), (x + s_ * 80, 470), (x + s_ * 170, 500), (x + s_ * 240, 600)], fill=(250, 230, 150), width=4)
            d.ellipse([x + s_ * 170 - 9, 491, x + s_ * 170 + 9, 509], fill=GOLD)
            d.polygon([(x + s_ * 70, 445), (x + s_ * 230, 500), (x + s_ * 200, 540), (x + s_ * 70, 485)], fill=ROSE + (130,))
        labs = [("myelo", "脊髓"), ("radiculo", "神经根"), ("plexo", "神经丛"), ("neuro", "神经"), ("myopathy", "肌病")]
        x0, step_ = 920, 190
        for i, (a, b) in enumerate(labs):
            cx = x0 + i * step_
            col = ROSE if i == 4 else GOLD
            d.rounded_rectangle([cx - 82, 385, cx + 82, 475], 16, fill=col + (45,), outline=col, width=3)
            bil(d, F, (cx, 430), a, b, 24, WHITE, GREY, maxw=150, gap=17)
            if i < 4:
                d.line([(cx + 82, 430), (cx + 108, 430)], fill=GOLD, width=4)
        bil(d, F, (1300, 560), "weak = muscle?  nerve?  both?", "无力：肌肉？神经？两者？", 30, (255, 220, 150), GREY, gap=22)
    if st >= 2:
        # trismus: jaw with blocked opening arrow
        d.line([(x, 290), (x, 318)], fill=RED, width=5); inhibit(d, (x, 296), (x, 324), RED, 5)
        arrow(d, (x, 300), (x, 282), RED, 4, 12)
        bil(d, F, (x - 130, 290), "trismus", "牙关紧闭", 26, (255, 170, 160), GREY, 'rm', gap=18)
        d.line([(x - 124, 300), (x - 34, 312)], fill=(255, 170, 160, 170), width=2)
        curved(d, (x + 70, 440), (x + 92, 330), -46, (255, 170, 160), 5, 16)
        bil(d, F, (x + 140, 236), "cervical dystonia", "颈部肌张力障碍", 26, (255, 170, 160), GREY, 'lm', gap=18)
        d.line([(x + 136, 256), (x + 96, 322)], fill=(255, 170, 160, 170), width=2)


def s_swallow(st, im, d, F, M):
    bil(d, F, (W / 2, 168), "n = 29 survivors  ·  ≥ 5 y after RT  ·  median 9 y", "29位幸存者 · 放疗后≥5年 · 中位9年", 32, WHITE, GREY, gap=22)
    # sagittal schematic (facing left)
    oc = (150, 165, 190); fillc = (70, 82, 104)
    head = [(330, 250), (420, 228), (540, 232), (630, 262), (680, 320), (690, 400), (680, 620), (470, 620), (455, 500), (420, 470), (350, 462), (318, 440), (312, 420), (296, 410), (300, 396), (290, 382), (296, 368), (284, 350), (256, 330), (276, 310), (300, 298), (312, 270)]
    d.polygon(head, fill=fillc + (210,), outline=oc)
    # oral cavity + pharynx air path
    d.rounded_rectangle([300, 360, 580, 394], 17, fill=(20, 26, 40, 255))
    d.rounded_rectangle([526, 360, 592, 524], 30, fill=(20, 26, 40, 255))
    d.polygon([(330, 396), (430, 388), (524, 396), (536, 450), (470, 462), (370, 446)], fill=ROSE + (230,))  # tongue
    T(d, F, (440, 425), "tongue 舌", 20, WHITE)
    d.ellipse([340, 290, 372, 306], fill=(40, 48, 66))
    # trachea (front) and oesophagus (back)
    d.rectangle([505, 520, 550, 618], fill=ICE + (110,), outline=ICE, width=2)
    for yy in range(530, 615, 16): d.line([(507, yy), (548, yy)], fill=ICE, width=2)
    d.rectangle([566, 520, 606, 618], fill=ROSE + (150,), outline=(240, 150, 160), width=2)
    d.polygon([(518, 500), (540, 468), (548, 474), (530, 506)], fill=(240, 200, 120))  # epiglottis
    T(d, F, (495, 596), "trachea 气管", 20, ICE, 'rm'); T(d, F, (618, 596), "oesophagus 食管", 20, (240, 160, 170), 'lm')
    T(d, F, (604, 440), "pharynx 咽", 20, GREY, 'lm')
    if st == 0:
        d.ellipse([318, 362, 360, 392], fill=GOLD + (235,))
    if st >= 1:
        for (bx, by, r) in [(545, 470, 13), (570, 498, 10), (552, 510, 8)]:
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=GOLD + (235,))
        d.ellipse([518, 552, 536, 572], fill=RED); arrow(d, (527, 512), (527, 548), RED, 4, 12)
    cards = [((870, 250, 1310, 410), "100%", "residue + aspiration", "残留 + 误吸：全部", RED, 1),
             ((1350, 250, 1790, 410), "38%", "trismus", "牙关紧闭", GOLD, 1),
             ((870, 430, 1310, 590), "86%", "pneumonia (half hospitalised)", "肺炎（半数住院）", ORANGE, 2),
             ((1350, 430, 1790, 590), "66%", "gastrostomy-dependent", "依赖胃造瘘", (200, 150, 230), 2)]
    for bx, num, en, zh, col, s0 in cards:
        if st < s0: continue
        panel(d, bx, col, 40, col)
        cx = (bx[0] + bx[2]) / 2
        T(d, F, (cx, bx[1] + 48), num, 46, col)
        bil(d, F, (cx, bx[1] + 118), en, zh, 26, WHITE, GREY, maxw=400, gap=19)
    if st >= 3:
        ax, ay = 900, 650
        arrow(d, (ax, ay), (1770, ay), (200, 210, 225), 4, 16)
        for x_, a, b in [(940, "RT", "放疗"), (1200, "years", "数年"), (1450, "dysphagia appears / worsens", "吞咽困难出现或加重")]:
            d.ellipse([x_ - 8, ay - 8, x_ + 8, ay + 8], fill=GOLD)
            T(d, F, (x_ + 16, ay - 18), a, 22, WHITE, 'lm'); T(d, F, (x_ + 16, ay + 16), b, 20, GREY, 'lm')
        stamp(d, F, (470, 662), "referred case series, not prevalence  转诊病例，非患病率", AMBER, 20)


def s_survivor(st, im, d, F, M):
    bil(d, F, (W / 2, 166), "St. Jude Lifetime  ·  n = 1,762  ·  median age 29  ·  ~20 y after diagnosis", "1762人 · 中位29岁 · 诊断后约20年", 30, WHITE, GREY, gap=22)
    rnd = random.Random(27); amber = set(rnd.sample(range(100), 27))
    gx, gy, sx, sy = 170, 262, 44, 35
    for i in range(100):
        r_, c_ = divmod(i, 10)
        person(d, (gx + c_ * sx, gy + r_ * sy), .78, AMBER if i in amber else (105, 120, 148))
    T(d, F, (gx + 4.5 * sx, 628), "sarcopenia 27%  肌少症", 32, AMBER)
    T(d, F, (gx + 4.5 * sx, 670), "low lean mass or weak grip  肌肉量低或握力弱", 21, GREY)
    if st >= 1:
        panel(d, (700, 236, 1790, 470), AMBER, 22, AMBER)
        # odds ratio mini forest plot
        x1, x2, y = 760, 1120, 330
        d.line([(x1, y), (x2, y)], fill=GREY, width=2)
        xr = x1 + 90; d.line([(xr, y - 30), (xr, y + 30)], fill=GREY, width=2)
        xo = x1 + 90 + 0.84 * 300
        d.line([(xr, y), (xo, y)], fill=AMBER, width=8); d.rectangle([xo - 11, y - 11, xo + 11, y + 11], fill=AMBER)
        T(d, F, (940, 278), "cranial RT  ·  OR 1.84", 26, WHITE)
        T(d, F, (940, 384), "头颅放疗 → 几率更高", 22, GREY)
        # blood drop with mtDNA rings
        dx = 1230; drop(d, (dx, 340), 1.25, RED)
        for (ox, oy) in [(-12, 344), (12, 356), (0, 322)]:
            d.ellipse([dx + ox - 8, oy - 8, dx + ox + 8, oy + 8], outline=(255, 235, 235), width=3)
        T(d, F, (1290, 300), "lower mtDNA copy number", 25, WHITE, 'lm')
        T(d, F, (1290, 336), "↔ sarcopenia", 25, AMBER, 'lm')
        T(d, F, (1290, 376), "mtDNA拷贝数低 ↔ 肌少症", 22, GREY, 'lm')
        stamp(d, F, (1245, 432), "ASSOCIATION · cross-sectional  关联·横断面", AMBER, 21)
    if st >= 2:
        human(d, (760, 586), .9, (150, 160, 180))
        d.line([(812, 600), (830, 676)], fill=(190, 170, 130), width=6)
        bil(d, F, (850, 546), "frailty in young survivors", "年轻幸存者衰弱", 25, WHITE, GREY, 'lm', gap=18)
        T(d, F, (850, 604), "Ness 2015", 20, GREY, 'lm')
        for k, (a, b) in enumerate([("senescence", "衰老"), ("sterile inflammation", "无菌炎症"), ("mitochondria", "线粒体")]):
            y = 520 + k * 58
            d.rounded_rectangle([1170, y - 24, 1520, y + 24], 12, fill=CREAM + (230,))
            T(d, F, (1190, y), a, 23, INK, 'lm'); T(d, F, (1500, y), b, 21, INK2, 'rm')
        stamp(d, F, (1662, 578), "HYPOTHESIS 假说", HRED, 24)


def slide(d, x, y, w_=14, h=96, tissue=True):
    d.rectangle([x - w_ / 2, y - h / 2, x + w_ / 2, y + h / 2], fill=(210, 230, 245, 170), outline=(235, 245, 255))
    if tissue: d.rectangle([x - w_ / 2 + 2, y - 10, x + w_ / 2 - 2, y + 14], fill=(220, 110, 150))

def slidebox(d, x0, y0, x1, y1, n_slides, lid=False, fill_all=False):
    d.rounded_rectangle([x0, y0, x1, y1], 10, fill=(110, 80, 55, 235), outline=(190, 150, 110), width=3)
    d.rectangle([x0 + 16, y0 + 16, x1 - 16, y1 - 16], fill=(40, 30, 24, 255))
    n = int((x1 - x0 - 50) / 22)
    for i in range(n):
        x = x0 + 30 + i * 22
        d.line([(x, y0 + 20), (x, y0 + 30)], fill=(150, 115, 80), width=2); d.line([(x, y1 - 30), (x, y1 - 20)], fill=(150, 115, 80), width=2)
    idx = list(range(n)) if fill_all else [n // 3, n // 3 + 1][:n_slides]
    for i in idx:
        slide(d, x0 + 30 + i * 22 + 11, (y0 + y1) / 2, 14, (y1 - y0) - 60)
    if lid:
        d.polygon([(x0, y0), (x1, y0), (x1 + 40, y0 - 120), (x0 + 40, y0 - 120)], fill=(130, 95, 65, 235), outline=(200, 160, 120))

def s_biopsy(st, im, d, F, M):
    bil(d, F, (520, 186), "Human muscle biopsies after RT", "放疗后人体肌肉活检", 32, WHITE, GREY, gap=24)
    if st == 0:
        slidebox(d, 220, 380, 820, 620, 0)
        d.rectangle([236, 396, 804, 604], fill=(30, 22, 18, 255))
        d.polygon([(220, 380), (820, 380), (860, 262), (260, 262)], fill=(130, 95, 65, 235), outline=(200, 160, 120))
        T(d, F, (560, 322), "?", 54, GOLD, font='title')
    else:
        slidebox(d, 220, 380, 820, 620, 2)
        d.polygon([(220, 380), (820, 380), (860, 262), (260, 262)], fill=(130, 95, 65, 160), outline=(200, 160, 120))
        # sticky note
        d.polygon([(640, 520), (900, 506), (912, 640), (652, 654)], fill=(250, 225, 110, 245))
        T(d, F, (776, 566), "few good series found", 22, INK); T(d, F, (778, 604), "未找到像样的系列", 21, INK2)
        arrow(d, (930, 450), (1110, 450), GOLD, 6, 22)
        for bx0, lab, zh, icon in [(1150, "mice", "小鼠", 'm'), (1490, "dishes", "培养皿", 'd')]:
            slidebox(d, bx0, 380, bx0 + 300, 560, 0, fill_all=True)
            if icon == 'm': mouse(d, (bx0 + 170, 320), .55)
            else: dish(d, F, (bx0 + 150, 330), 70)
            bil(d, F, (bx0 + 150, 604), lab, zh, 26, WHITE, GREY, gap=19)
        bil(d, F, (1470, 196), "gap = invitation", "空白 = 邀请", 36, GOLD, (230, 210, 160), gap=26)


# ---------------- 2 detective's toolkit ----------------
def s_models(st, im, d, F, M):
    T(d, F, (W / 2, 152), "Choose your model  ·  选择模型", 34, GOLD)
    boxes = [(130, 190, 945, 432), (975, 190, 1790, 432), (130, 450, 945, 690), (975, 450, 1790, 690)]
    titles = [("single dose  vs  fractionated", "单次 vs 分次"), ("juvenile  vs  adult", "幼年 vs 成年"),
              ("mouse  vs  rat", "小鼠 vs 大鼠"), ("in vitro: cells & human organoids", "体外：细胞与人类类器官")]
    show = [1, 1, 2, 3]
    for i, bx in enumerate(boxes):
        if st >= show[i]:
            panel(d, bx, PANEL, 170, (120, 150, 200))
            T(d, F, ((bx[0] + bx[2]) / 2, bx[1] + 34), titles[i][0] + "   " + titles[i][1], 27, WHITE)
        else:
            d.rounded_rectangle(bx, 22, outline=(90, 105, 130), width=2)
            T(d, F, ((bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2), "ABCD"[i], 54, (70, 85, 110), font='title')
    if st >= 1:
        x0, y0 = 130, 190
        bolt(d, (x0 + 230, y0 + 128), 1.25)
        for k in range(3): bolt(d, (x0 + 520 + k * 70, y0 + 150), .8)
        T(d, F, (x0 + 230, y0 + 212), "strong, quick  强而快", 22, GREY)
        T(d, F, (x0 + 590, y0 + 212), "closer to clinic  更接近临床", 22, GREY)
        x0 = 975
        mouse(d, (x0 + 250, y0 + 150), .55); mouse(d, (x0 + 580, y0 + 145), .95)
        T(d, F, (x0 + 230, y0 + 212), "childhood cancer  儿童肿瘤", 22, GREY)
        T(d, F, (x0 + 570, y0 + 212), "adult patient  成年病人", 22, GREY)
    if st >= 2:
        x0, y0 = 130, 450
        mouse(d, (x0 + 110, y0 + 120), .5)
        bil(d, F, (x0 + 190, y0 + 120), "genetics · scRNA-seq", "遗传工具 · 单细胞", 22, WHITE, GREY, 'lm', gap=17)
        rat(d, (x0 + 535, y0 + 120), .45)
        T(d, F, (x0 + 605, y0 + 96), "very high-dose", 22, WHITE, 'lm'); T(d, F, (x0 + 605, y0 + 122), "fibrosis", 22, WHITE, 'lm')
        T(d, F, (x0 + 605, y0 + 150), "超高剂量纤维化", 20, GREY, 'lm')
        d.ellipse([x0 + 175, y0 + 186, x0 + 205, y0 + 216], fill=(170, 90, 200), outline=(220, 170, 240), width=2)
        T(d, F, (x0 + 220, y0 + 201), "+ tumour: juvenile RMS + RT  幼年横纹肌肉瘤+放疗", 22, (220, 180, 240), 'lm')
    if st >= 3:
        x0, y0 = 975, 450
        dish(d, F, (x0 + 150, y0 + 130), 100)
        for k, (ox, oy) in enumerate([(-50, -6), (-20, 10), (40, -8), (60, 12)]):
            cell(d, (x0 + 150 + ox, y0 + 130 + oy), 9, fill=(170, 80, 95), nuc=False)
        d.ellipse([x0 + 128, y0 + 100, x0 + 172, y0 + 144], fill=(200, 100, 120, 220), outline=(250, 170, 180), width=2)
        items = [("no vessels", "无血管"), ("no immune cells", "无免疫"), ("no years", "无长期")]
        for k, (a, b) in enumerate(items):
            cx = x0 + 380 + k * 150; cy = y0 + 112
            if k == 0: capillary(d, (cx, cy), 22)
            elif k == 1: macrophage(d, (cx, cy), .5)
            else: clock(d, (cx, cy), 24)
            xmark(d, (cx, cy), 22, RED, 5)
            T(d, F, (cx, cy + 50), a, 20, WHITE); T(d, F, (cx, cy + 78), b, 20, GREY)


def s_doses(st, im, d, F, M):
    def ylog(v): return 670 - 260 * math.log10(v)
    xl, xr = 360, 440
    d.line([(xl, 150), (xl, 676)], fill=(170, 180, 200), width=5); d.line([(xr, 150), (xr, 676)], fill=(170, 180, 200), width=5)
    for v in (1, 10, 100):
        T(d, F, (xl - 22, ylog(v)), f"{v} Gy", 22, GREY, 'rm')
    for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        d.line([(xl, ylog(v)), (xr, ylog(v))], fill=(80, 92, 115), width=2 if v in (1, 10, 100) else 1)
    T(d, F, (300, 520), "log scale", 20, DIM, 'rm'); T(d, F, (300, 548), "对数刻度", 20, DIM, 'rm')
    rungs = [(2, "2 Gy  ·  human organoid (Jiang 2024)", "人类类器官", TEAL, 'org', 0),
             (8.2, "3 × 8.2 Gy  ·  juvenile mouse (Rochester)", "幼年小鼠 分3次", GREEN, 'jm3', 1),
             (16, "16 Gy single  ·  juvenile mouse (Collao 2023)", "幼年小鼠 单次", GREEN, 'jm', 1),
             (50, "50 Gy single  ·  adult mouse (Gans 2021)", "成年小鼠 单次", ORANGE, 'am', 2),
             (90, "90 Gy single  ·  rat (Zhou 2018, Zeng 2022)", "大鼠 单次", RED, 'rat', 3)]
    for v, en, zh, col, icon, s0 in rungs:
        if st < s0: continue
        y = ylog(v)
        d.line([(xl - 4, y), (xr + 4, y)], fill=col, width=8)
        d.ellipse([xr + 14, y - 6, xr + 26, y + 6], fill=col)
        ix = 560
        if icon == 'org':
            d.ellipse([ix - 24, y - 24, ix + 24, y + 24], fill=(200, 100, 120, 220), outline=(250, 170, 180), width=2)
        elif icon == 'jm3':
            mouse(d, (ix, y + 6), .32)
        elif icon == 'jm': mouse(d, (ix, y + 6), .32)
        elif icon == 'am': mouse(d, (ix, y + 6), .45)
        else: rat(d, (ix, y + 6), .34)
        T(d, F, (660, y - 13), en, 26, WHITE, 'lm'); T(d, F, (660, y + 19), zh, 21, col, 'lm')
    if st >= 3:
        bx = 1350; y1, y2 = ylog(90), ylog(2)
        d.line([(bx, y1), (bx + 24, y1), (bx + 24, y2), (bx, y2)], fill=GOLD, width=4)
        d.line([(bx + 24, (y1 + y2) / 2), (bx + 48, (y1 + y2) / 2)], fill=GOLD, width=4)
        ym = (y1 + y2) / 2
        T(d, F, (bx + 70, ym - 66), "45×", 60, GOLD, 'lm')
        T(d, F, (bx + 70, ym + 4), "different worlds", 30, WHITE, 'lm')
        T(d, F, (bx + 70, ym + 44), "相差45倍 —— 不同的世界", 24, GREY, 'lm')


def s_readouts(st, im, d, F, M):
    P = [(130, 128, 945, 400), (975, 128, 1790, 400), (975, 416, 1790, 688), (130, 416, 945, 688)]
    heads = [("Scar", "瘢痕"), ("Atrophy · guardians · damage", "萎缩·守护者·损伤"), ("Neighbours", "邻居细胞"), ("Function", "功能")]
    for i in range(min(st + 1, 4)):
        bx = P[i]; hi = (i == 3)
        panel(d, bx, PANEL, 170, GOLD if hi else (110, 135, 180), w=4 if hi else 2)
        T(d, F, (bx[0] + 26, bx[1] + 32), heads[i][0] + "   " + heads[i][1], 24, GOLD if hi else (190, 205, 230), 'lm')
    # 0: Masson trichrome
    x0, y0 = P[0][:2]; c = (x0 + 190, y0 + 150); R = 88
    d.ellipse([c[0] - R, c[1] - R, c[0] + R, c[1] + R], fill=(60, 100, 205, 235), outline=(150, 180, 240), width=2)
    sp = 33
    for row in range(-3, 4):
        for col in range(-3, 4):
            px = c[0] + (col + (row % 2) * .5) * sp; py = c[1] + row * sp * .87
            if math.dist((px, py), c) < R - 16:
                d.ellipse([px - 14, py - 14, px + 14, py + 14], fill=(205, 60, 75))
    T(d, F, (c[0], y0 + 254), "Masson trichrome", 20, GREY)
    bil(d, F, (x0 + 580, y0 + 128), "% blue area = fibrosis", "蓝色面积% = 纤维化", 28, WHITE, GREY, gap=20)
    d.rounded_rectangle([x0 + 440, y0 + 190, x0 + 720, y0 + 214], 12, fill=(60, 70, 90))
    d.rounded_rectangle([x0 + 440, y0 + 190, x0 + 540, y0 + 214], 12, fill=(70, 110, 210))
    if st >= 1:
        x0, y0 = P[1][:2]; cy = y0 + 128
        xs = [x0 + 110, x0 + 310, x0 + 510, x0 + 710]
        d.ellipse([xs[0] - 40, cy - 40, xs[0] + 40, cy + 40], fill=ROSE + (230,), outline=(240, 150, 160), width=3)
        d.line([(xs[0] - 40, cy + 56), (xs[0] + 40, cy + 56)], fill=GOLD, width=3)
        for k in range(5): d.line([(xs[0] - 40 + k * 20, cy + 48), (xs[0] - 40 + k * 20, cy + 56)], fill=GOLD, width=2)
        x = xs[1]; d.polygon([(x - 56, cy + 50), (x + 56, cy + 50), (x + 44, cy + 14), (x - 44, cy + 14)], fill=(150, 160, 180))
        d.rounded_rectangle([x - 40, cy - 34, x + 40, cy + 14], 20, fill=ROSE + (230,))
        x = xs[2]; fiberseg(d, x - 70, x + 70, cy + 14, 44, nuclei=False)
        for ox in (-36, 30): sat_cell(d, (x + ox, cy - 18), .45)
        x = xs[3]; d.ellipse([x - 46, cy - 40, x + 46, cy + 40], fill=(30, 40, 80), outline=(100, 120, 180), width=3)
        foci(d, (x, cy), 30, 8, seed=4, size=5)
        labs = [("CSA", "横截面积"), ("muscle mass", "肌重"), ("PAX7 count", "卫星细胞计数"), ("γH2AX", "DNA损伤")]
        for x, (a_, b_) in zip(xs, labs):
            T(d, F, (x, y0 + 210), a_, 22, WHITE); T(d, F, (x, y0 + 240), b_, 20, GREY)
    if st >= 2:
        x0, y0 = P[2][:2]
        ax0, ay0, ax1, ay1 = x0 + 60, y0 + 62, x0 + 340, y0 + 200
        d.line([(ax0, ay0), (ax0, ay1), (ax1, ay1)], fill=GREY, width=2)
        rnd = random.Random(8)
        for cx, cy, col in [(ax0 + 70, ay0 + 95, ORANGE), (ax0 + 200, ay0 + 40, RED), (ax0 + 210, ay0 + 105, PURPLE)]:
            for _ in range(24):
                px, py = cx + rnd.gauss(0, 16), cy + rnd.gauss(0, 11)
                d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=col + (220,))
            d.ellipse([cx - 38, cy - 27, cx + 38, cy + 27], outline=col, width=2)
        T(d, F, ((ax0 + ax1) / 2, y0 + 224), "flow: FAPs · ECs · immune", 21, WHITE)
        T(d, F, ((ax0 + ax1) / 2, y0 + 251), "流式：FAPs · 内皮 · 免疫", 20, GREY)
        umap(d, F, [(x0 + 560, y0 + 130, 46, GREEN, None, 28), (x0 + 655, y0 + 104, 42, ORANGE, None, 28), (x0 + 625, y0 + 180, 38, PURPLE, None, 24), (x0 + 715, y0 + 170, 30, RED, None, 20)])
        T(d, F, (x0 + 630, y0 + 224), "single-cell sequencing", 21, WHITE)
        T(d, F, (x0 + 630, y0 + 251), "单细胞测序", 20, GREY)
    if st >= 3:
        x0, y0 = P[3][:2]
        ax0, ay0, ax1, ay1 = x0 + 50, y0 + 80, x0 + 430, y0 + 240
        d.line([(ax0, ay0), (ax0, ay1), (ax1, ay1)], fill=GREY, width=2)
        def trace(h, col):
            pts = []
            for k in range(81):
                t = k / 80
                v = (1 - math.exp(-t * 12)) * (1 if t < .7 else math.exp(-(t - .7) * 18))
                pts.append((ax0 + 10 + t * (ax1 - ax0 - 20), ay1 - 6 - v * h))
            d.line(pts, fill=col, width=5)
        trace(140, (150, 165, 190)); trace(140 * .73, ROSE)
        d.line([(x0 + 290, y0 + 32), (x0 + 320, y0 + 32)], fill=(150, 165, 190), width=5); T(d, F, (x0 + 328, y0 + 32), "control 对照", 20, (170, 180, 200), 'lm')
        d.line([(x0 + 470, y0 + 32), (x0 + 500, y0 + 32)], fill=ROSE, width=5); T(d, F, (x0 + 508, y0 + 32), "irradiated 照射", 20, ROSE, 'lm')
        T(d, F, (x0 + 630, y0 + 104), "−27%", 54, ROSE)
        bil(d, F, (x0 + 630, y0 + 170), "specific force (EDL)", "比肌力 · O'Connor 2022", 22, WHITE, GREY, gap=16)
        chip(d, F, (x0 + 615, y0 + 232), "most patient-relevant  最贴近病人", GOLD, 20)


def topmouse(d, c, s=1.0, col=(200, 200, 210)):
    x, y = c
    d.line([(x, y + 120 * s), (x + 30 * s, y + 190 * s), (x - 10 * s, y + 240 * s)], fill=(230, 180, 190), width=int(6 * s))
    for sgn in (-1, 1):
        d.line([(x + sgn * 40 * s, y - 40 * s), (x + sgn * 80 * s, y - 70 * s)], fill=col, width=int(14 * s))
    d.ellipse([x - 62 * s, y - 80 * s, x + 62 * s, y + 130 * s], fill=col + (235,))
    d.polygon([(x - 40 * s, y - 70 * s), (x, y - 150 * s), (x + 40 * s, y - 70 * s)], fill=col)
    for sgn in (-1, 1):
        d.ellipse([x + sgn * 34 * s - 16 * s, y - 112 * s, x + sgn * 34 * s + 16 * s, y - 80 * s], fill=(230, 180, 190))

def s_timeline4(st, im, d, F, M):
    mx, my = 600, 290
    # hind legs and tail first, body on top
    L = (mx - 115, my + 170); R = (mx + 115, my + 170)
    for p0, p in (((mx - 40, my + 95), L), ((mx + 40, my + 95), R)):
        d.line([p0, p], fill=(200, 200, 210), width=22)
        d.ellipse([p[0] - 18, p[1] - 14, p[0] + 18, p[1] + 14], fill=(230, 180, 190))
    topmouse(d, (mx, my), .95)
    beam(d, (mx + 360, my - 120), (R[0] + 22, R[1] - 26), GOLD, 8)
    T(d, F, (mx + 380, my - 150), "irradiated leg  照射侧", 24, GOLD)
    d.rounded_rectangle([L[0] - 48, L[1] - 52, L[0] + 48, L[1] + 52], 12, fill=(120, 125, 135, 215), outline=(200, 205, 215), width=3)
    for k in range(int(L[1] - 40), int(L[1] + 50), 18): d.line([(L[0] - 40, k), (L[0] + 40, k - 12)], fill=(160, 165, 175), width=2)
    bil(d, F, (L[0] - 70, L[1]), "shielded contralateral control", "遮挡对侧对照", 23, (210, 215, 230), GREY, 'rm', gap=17)
    curved(d, (mx - 30, my + 40), (L[0] + 10, L[1] - 60), 40, (255, 140, 140), 3, 12)
    T(d, F, (mx - 120, my - 40), "? circulating signals", 22, (255, 150, 150), 'rm')
    T(d, F, (mx - 120, my - 10), "？循环信号", 21, GREY, 'rm')
    cx0, cy0 = 1240, 170
    d.rounded_rectangle([cx0, cy0, cx0 + 360, cy0 + 220], 14, fill=(40, 55, 80, 160), outline=(170, 185, 210), width=3)
    for x in range(cx0 + 30, cx0 + 360, 34): d.line([(x, cy0 + 6), (x, cy0 + 214)], fill=(150, 165, 190, 120), width=2)
    mouse(d, (cx0 + 200, cy0 + 150), .55)
    bil(d, F, (cx0 + 180, cy0 + 262), "unirradiated control", "未照射对照", 24, WHITE, GREY, gap=18)
    ay = 600
    if st >= 1:
        d.line([(200, ay), (1120 if st < 2 else 1180, ay)], fill=WHITE, width=4)
        if st < 2: arrow(d, (1100, ay), (1140, ay), WHITE, 4, 16)
        for x, lab in [(240, "24 h"), (420, "d3"), (560, "d7"), (700, "d14"), (980, "d56")]:
            d.line([(x, ay - 12), (x, ay + 12)], fill=WHITE, width=3); T(d, F, (x, ay - 34), lab, 24, WHITE)
        T(d, F, (610, ay + 42), "Collao 2023 / 2025", 20, GREY) if st < 2 else None
    if st >= 2:
        for k in (0, 1):
            d.line([(1192 + k * 18, ay - 16), (1204 + k * 18, ay + 16)], fill=WHITE, width=4)
        arrow(d, (1230, ay), (1780, ay), WHITE, 4, 16)
        d.line([(1520, ay - 12), (1520, ay + 12)], fill=GOLD, width=4)
        T(d, F, (1520, ay - 34), "14 months (Rochester)  14个月", 24, GOLD)
        d.rounded_rectangle([210, ay + 24, 1010, ay + 76], 14, fill=GOLD + (45,), outline=GOLD + (180,), width=2)
        T(d, F, (610, ay + 50), "early = injury   早期 = 损伤", 24, GOLD)
        d.rounded_rectangle([1240, ay + 24, 1780, ay + 76], 14, fill=RED + (45,), outline=RED + (180,), width=2)
        T(d, F, (1510, ay + 50), "late = disease   晚期 = 疾病", 24, (255, 150, 140))


BENCH = {
    0: ("Study design checklist  ·  研究设计清单",
        [("question + primary outcome + timepoint", "问题 + 主要结局 + 时间点"), ("randomize; record strain, sex, age, weight", "随机分组；记录品系、性别、年龄、体重"),
         ("shielded leg + unirradiated + vehicle", "遮挡腿 + 未照射 + 溶媒对照"), ("age matters: 4 wk vs 12 wk", "年龄很关键：4周 vs 12周")]),
    1: ("Dose reporting & BED  ·  剂量报告与BED",
        [("machine, energy, dose rate, field, shielding", "机器、能量、剂量率、照射野、遮挡"), ("verify dose (dosimetry)", "剂量核实"),
         ("4 × 4 Gy → BED 37;  16 Gy → BED ~100", "4×4 Gy → BED 37；16 Gy → 约100"), ("extreme single doses: formula less reliable", "极端单次剂量：公式不可靠")]),
    2: ("Blinding & sample size  ·  盲法与样本量",
        [("blind slide scoring", "盲法读片"), ("power calculation before start", "事先计算样本量"),
         ("n = 6–7 per group: fragile", "每组6–7只：脆弱"), ("report every animal lost (3/10)", "报告每只损失动物（3/10）")]),
    3: ("Force & timepoints  ·  肌力与时间点",
        [("in vivo or ex vivo force", "在体或离体测力"), ("specific force = force ÷ CSA", "比肌力 = 力 ÷ 横截面积"),
         ("early: damage, death", "早期：损伤、死亡"), ("weeks: remodeling;  months: lasting deficit", "几周：重塑；几个月：持久缺陷")]),
}

def s_bench4(st, im, d, F, M):
    title, rows = BENCH[st]
    bench_card(d, F, title, rows)


# ---------------- 3 conflicting clues ----------------
def podium(d, F, x0, x1, lines, col):
    d.polygon([(x0, 330), (x1, 330), (x1 - 20, 610), (x0 + 20, 610)], fill=(70, 55, 45, 220), outline=(170, 140, 110))
    d.rectangle([x0 - 10, 318, x1 + 10, 336], fill=(120, 95, 70), outline=(180, 150, 115))
    y = 368
    for txt, size, c in lines:
        T(d, F, ((x0 + x1) / 2, y), txt, size, c); y += size + (18 if size >= 24 else 14)

def scale_icon(d, c, tilt=0.0):
    x, y = c
    d.line([(x, y), (x, y + 110)], fill=GOLD, width=6); d.polygon([(x - 50, y + 124), (x + 50, y + 124), (x + 30, y + 106), (x - 30, y + 106)], fill=GOLD)
    a = tilt; dx, dy = 130 * math.cos(a), 130 * math.sin(a)
    l, r = (x - dx, y - dy), (x + dx, y + dy)
    d.line([l, r], fill=GOLD, width=6); d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=GOLD)
    for p in (l, r):
        d.line([p, (p[0] - 34, p[1] + 50)], fill=GOLD, width=2); d.line([p, (p[0] + 34, p[1] + 50)], fill=GOLD, width=2)
        d.chord([p[0] - 40, p[1] + 30, p[0] + 40, p[1] + 70], 0, 180, fill=GOLD + (200,)) if hasattr(d, 'chord') else d.ellipse([p[0] - 40, p[1] + 44, p[0] + 40, p[1] + 60], fill=GOLD + (200,))

def s_conflict(st, im, d, F, M):
    rat(d, (360, 250), .62)
    podium(d, F, 160, 580, [("rat  ·  90 Gy single", 26, GOLD), ("SCs ↑ activated", 28, GREEN), ("Zeng 2022", 20, GREY),
                             ("Pax7 / MyoD ↑ ~wk 4", 26, GREEN), ("Zhou 2018", 20, GREY), ("90 Gy · 卫星细胞↑", 22, (200, 210, 225))], GOLD)
    if st >= 1:
        mouse(d, (1570, 262), .7, facing=-1)
        podium(d, F, 1340, 1760, [("juvenile mouse", 26, GOLD), ("SCs ↓ 45%", 28, RED), ("Kallenbach 2022", 20, GREY),
                                   ("↓ day 3 & day 56", 26, RED), ("Collao 2023", 20, GREY), ("幼年 · 卫星细胞↓", 22, (200, 210, 225))], GOLD)
    scale_icon(d, (960, 170), -0.16 if st == 0 else 0.0)
    if st >= 1:
        T(d, F, (1130, 166), "?", 56, GOLD); T(d, F, (790, 166), "?", 56, GOLD)
    if st >= 2:
        rows = [("species 物种", "rat 大鼠", "mouse 小鼠"), ("dose 剂量", "90 Gy", "16 or 3×8.2 Gy"), ("age 年龄", "not juvenile 非幼年", "4 wk 4周")]
        for i, (mid, l, r) in enumerate(rows):
            y = 345 + i * 56
            chip(d, F, (960, y), mid, BLUE, 22)
            T(d, F, (870 - 30, y), l, 23, WHITE, 'rm'); T(d, F, (1050 + 30, y), r, 23, WHITE, 'lm')
    if st >= 3:
        y = 556; chip(d, F, (700, y), "time 时间", BLUE, 22)
        x0, x1, yb = 790, 1150, 588
        d.line([(x0, yb), (x1, yb)], fill=GREY, width=2)
        pts = [(x0 + t * (x1 - x0), yb - 62 * (math.exp(-((t - .22) / .12) ** 2)) - 24 * (1 - t) + 0) for t in [k / 60 for k in range(61)]]
        pts = [(px, min(py, yb - 2)) for px, py in pts]
        d.line(pts, fill=GOLD, width=5)
        T(d, F, (x0 + .22 * (x1 - x0) + 34, yb - 80), "activation 激活", 22, GREEN, 'lm')
        T(d, F, (x1 + 12, yb - 16), "depletion 耗竭", 22, RED, 'lm')
        stamp(d, F, (960, 632), "HYPOTHESIS 假说: same story, different snapshots  同一故事，不同快照", HRED, 21)
        T(d, F, (960, 676), "test: same species, matched dose, many timepoints  ·  检验：同物种、匹配剂量、多时间点", 20, GREY)


def cancer_cell(d, c, r=120):
    x, y = c; rnd = random.Random(11); pts = []
    for i in range(22):
        a = i / 22 * 6.283; rr = r * (1 + rnd.uniform(-.08, .08))
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    d.polygon(pts, fill=(120, 80, 150, 210), outline=(200, 160, 230))
    d.ellipse([x - r * .38, y - r * .34, x + r * .3, y + r * .36], fill=(70, 40, 100), outline=(170, 130, 210), width=2)

def ev(d, c, r=11, col=(250, 200, 120)):
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=col + (90,), outline=col, width=3)
    d.ellipse([c[0] - 3, c[1] - 3, c[0] + 3, c[1] + 3], fill=col)

def s_tumorev(st, im, d, F, M):
    tc = (350, 360); mc = (1560, 340)
    cancer_cell(d, tc, 120)
    T(d, F, (tc[0] - 150, 500), "tumour 肿瘤", 24, (210, 180, 240))
    # muscle bundle
    for k, yy in enumerate((280, 340, 400)):
        fiberseg(d, 1360, 1760, yy, 50, (150, 120, 130) if st >= 2 else ROSE)
    if st >= 2:
        collagen(d, (1360, 254, 1760, 426), 9, col=ICE, w=4)
    T(d, F, (1560, 456), "muscle 肌肉", 24, (240, 160, 170))
    # vessel path
    vy = 610
    d.line([(tc[0], 482), (tc[0], vy), (1700, vy), (1700, 430)], fill=RED + (120,), width=34, joint='curve')
    d.line([(tc[0], 482), (tc[0], vy), (1700, vy), (1700, 430)], fill=RED + (230,), width=4, joint='curve')
    T(d, F, (1120, vy - 36), "bloodstream 血液循环", 21, (230, 140, 130))
    beam(d, (1560, 135), (1560, 248), GOLD, 8)
    if st == 0:
        bil(d, F, (960, 200), "assumed: local crime", "原假设：现场作案", 32, WHITE, GREY, gap=24)
    else:
        bil(d, F, (960, 186), "assumed: local crime", "原假设：现场作案", 24, DIM, DIM, gap=18)
        d.line([(830, 176), (1090, 176)], fill=(200, 90, 90), width=3)
        beam(d, (350, 135), (350, 232), GOLD, 8)
        T(d, F, (530, 280), "arachidonic acid ↑", 26, GOLD, 'lm'); T(d, F, (530, 314), "花生四烯酸↑", 22, GREY, 'lm')
        arrow(d, (620, 336), (620, 372), WHITE, 3, 12)
        T(d, F, (530, 400), "SRM packed into small EVs", 26, (250, 200, 120), 'lm'); T(d, F, (530, 434), "亚精胺合酶装入小囊泡", 22, GREY, 'lm')
        for p in [(392, 330), (310, 400), (395, 410)]: ev(d, p, 10)
    if st >= 2:
        evc = (250, 200, 120) if st == 2 else (120, 110, 100)
        for x in range(470, 1700, 120):
            ev(d, (x, vy), 13, evc)
        ev(d, (tc[0], 560), 13)
        chain = [("spermidine ↑", "亚精胺↑"), ("eIF5A", None), ("type I collagen", "I型胶原")]
        ys = [270, 360, 450]
        for (a, b), y in zip(chain, ys):
            T(d, F, (1150, y - (12 if b else 0)), a, 26, ICE); 
            if b: T(d, F, (1150, y + 20), b, 21, GREY)
        arrow(d, (1150, 310), (1150, 336), ICE, 3, 10); arrow(d, (1150, 382), (1150, 412), ICE, 3, 10)
        T(d, F, (1560, 500), "fibers stiffen 纤维变硬", 22, ICE)
    if st >= 3:
        pc = (520, 540)
        pill_capsule(d, pc, 110, 40, (90, 170, 230), (235, 240, 245))
        xmark(d, (tc[0], 560), 24, RED, 7)
        inhibit(d, (pc[0] - 60, pc[1] + 4), (tc[0] + 34, 558), RED, 4)
        T(d, F, (600, 528), "losartan blocks SRM export (mouse)", 23, WHITE, 'lm')
        T(d, F, (600, 560), "氯沙坦阻断外送（小鼠）", 21, GREY, 'lm')
        chip(d, F, (1040, 668), "Zhang 2025 Cell Metab  ·  awaits human data  待人体验证", AMBER, 20)


# ---------------- 4 picking the lock ----------------
def s_ptx(st, im, d, F, M):
    padlock(d, (200, 196), 1.0)
    bil(d, F, (260, 196), "Picking the lock", "撬锁", 32, WHITE, GOLD, 'lm', gap=22)
    pill_capsule(d, (840, 196), 160, 58, (230, 150, 70), (245, 240, 230))
    T(d, F, (1040, 196), "+", 50, WHITE)
    softgel(d, (1220, 196), 62, 38)
    T(d, F, (840, 258), "pentoxifylline 己酮可可碱", 23, WHITE); T(d, F, (1220, 258), "vitamin E 维生素E", 23, WHITE)
    if st >= 1:
        bil(d, F, (525, 330), "2003 RCT · 24 women · breast RT · 6 months", "双盲安慰剂对照 · 乳腺放疗后纤维化", 24, WHITE, GREY, gap=18)
        T(d, F, (190, 388), "fibrosis area shrank  纤维化面积缩小", 20, GREY, 'lm')
        bars(d, F, (180, 400, 580, 590), [("PTX + Vit E", "联合", 60, FGREEN, "60%"), ("placebo", "双安慰剂", 43, (130, 140, 160), "43%")], maxv=60, size=22)
        for k, (cx, kind) in enumerate([(680, 'c'), (800, 's')]):
            if kind == 'c': pill_capsule(d, (cx, 470), 80, 30, (230, 150, 70), (245, 240, 230))
            else: softgel(d, (cx, 470), 34, 22)
            xmark(d, (cx, 470), 20, RED, 5)
        T(d, F, (740, 530), "either alone:", 22, WHITE); T(d, F, (740, 560), "ineffective 单用无效", 22, (255, 150, 140))
    if st >= 2:
        T(d, F, (525, 676), "superficial fibrosis, not deep muscle  ·  浅表纤维化，非深部肌肉", 23, ORANGE)
        panel(d, (990, 300, 1780, 612), PANEL, 170, (120, 140, 180))
        bil(d, F, (1385, 350), "2020 RCT · + clodronate · plexopathy · 18 mo", "加氯膦酸盐 · 放射性神经丛病 · 18个月", 23, WHITE, GREY, gap=18)
        bars(d, F, (1130, 440, 1640, 548), [("treated", "治疗组", 50, (130, 140, 160), None), ("placebo", "安慰剂", 50, (130, 140, 160), None)], maxv=60, size=22)
        T(d, F, (1385, 418), "no benefit  无获益", 28, RED)
        chip(d, F, (1385, 656), "mixed evidence  证据混合", AMBER, 26)


def switch_icon(d, F, c, down=True):
    x, y = c
    d.rounded_rectangle([x - 70, y - 90, x + 70, y + 90], 22, fill=(40, 52, 78, 230), outline=(170, 185, 210), width=3)
    d.rounded_rectangle([x - 16, y - 66, x + 16, y + 66], 16, fill=(20, 28, 44))
    ky = y + 40 if down else y - 40
    d.rounded_rectangle([x - 40, ky - 22, x + 40, ky + 22], 12, fill=ORANGE + (240,), outline=(255, 210, 160), width=2)
    T(d, F, (x, y - 118), "TGF-β", 28, ORANGE)
    T(d, F, (x - 86, y - 56), "on", 20, GREY, 'rm'); T(d, F, (x - 86, y + 56), "off", 20, GREY, 'rm')

def s_tgfb(st, im, d, F, M):
    mx, my, ms = 420, 320, 1.6
    mouse(d, (mx, my), ms)
    hx, hy = mx - 40 * ms, my + 42 * ms
    d.ellipse([hx - 44, hy - 40, hx + 44, hy + 40], outline=GOLD, width=4)
    beam(d, (hx - 170, 140), (hx - 30, hy - 40), GOLD, 7)
    T(d, F, (hx + 10, hy + 70), "right hindlimb 右后肢", 22, GOLD)
    switch_icon(d, F, (690, 520), down=True)
    arrow(d, (800, 450), (800, 580), ORANGE, 4, 14)
    T(d, F, (1340, 166), "50 Gy single  ·  right hindlimb  ·  12-wk C57BL/6", 25, WHITE)
    T(d, F, (1340, 206), "→ daily TGF-β inhibitor × 8 wk", 25, ORANGE)
    T(d, F, (1340, 244), "50 Gy单次 → 每日抑制剂 × 8周", 22, GREY)
    if st >= 1:
        panel(d, (900, 290, 1780, 616), PANEL, 160, (120, 140, 180))
        T(d, F, (1340, 324), "quadriceps fibrosis at 9 months  ·  9个月 股四头肌纤维化", 23, (200, 215, 235))
        bars(d, F, (980, 360, 1700, 536), [("RT only", "仅照射", 1.2, ROSE, "1.2%"), ("RT + inhibitor", "照射+抑制剂", 0.14, GREEN, "0.14%"),
                                            ("no RT", "未照射", 0.05, (140, 150, 170), "0.05%")], maxv=1.2, size=23)
    if st >= 2:
        chips_row(d, F, 664, [("preliminary 初步", GOLD), ("scar, not strength  测瘢痕未测肌力", AMBER), ("TGF-β has normal jobs  TGF-β有正常功能", HRED)], 22, cx=1150)


def s_cells(st, im, d, F, M):
    rx, ry, rs = 640, 380, 1.2
    rat(d, (rx, ry), rs, facing=1)
    k = rs * 1.45; hx, hy = rx - 40 * k, ry + 40 * k
    d.ellipse([hx - 50, hy - 40, hx + 50, hy + 40], outline=GOLD, width=4)
    T(d, F, (750, 530), "90 Gy rat model   90 Gy大鼠模型", 24, GOLD)
    sy = hy + 4; sx = hx - 52 - 170 * 1.3
    syringe(d, (sx, sy), 1.3)
    for j in range(6): d.ellipse([sx + 12 + j * 26, sy - 10, sx + 30 + j * 26, sy + 10], fill=(250, 220, 120))
    bil(d, F, (sx + 50, sy + 76), "ADSCs · adipose-derived stem cells", "脂肪来源干细胞", 22, (250, 220, 120), GREY, gap=17)
    arrow(d, (830, 340), (930, 270), WHITE, 4, 16); arrow(d, (830, 390), (930, 440), WHITE, 4, 16)
    panel(d, (950, 205, 1500, 315), ICE, 30, ICE)
    collagen(d, (975, 230, 1065, 290), 4, col=ICE)
    bil(d, F, (1090, 260), "fibrosis ↓ over time", "纤维化随时间减轻", 27, WHITE, GREY, 'lm', gap=19)
    panel(d, (950, 385, 1500, 495), GREEN, 30, GREEN)
    sat_cell(d, (1020, 440), .7)
    bil(d, F, (1090, 440), "SC activation ↑", "卫星细胞激活↑", 27, WHITE, GREY, 'lm', gap=19)
    T(d, F, (1225, 528), "Li 2025", 20, GREY)
    if st >= 1:
        d.rounded_rectangle([560, 580, 1360, 660], 16, fill=CREAM + (235,))
        T(d, F, (960, 604), "one group  ·  one model  ·  n = 6 per group", 25, INK)
        T(d, F, (960, 638), "一个团队 · 一个模型 · 每组6只", 22, INK2)
        chip(d, F, (1600, 620), "promising, early  有希望，尚早", GOLD, 23)


def s_exercise(st, im, d, F, M):
    wc = (330, 380); R = 170
    d.ellipse([wc[0] - R, wc[1] - R, wc[0] + R, wc[1] + R], outline=(170, 185, 210), width=8)
    d.ellipse([wc[0] - R + 16, wc[1] - R + 16, wc[0] + R - 16, wc[1] + R - 16], outline=(110, 125, 150), width=2)
    for k in range(12):
        a = k * math.pi / 6; d.line([wc, (wc[0] + (R - 8) * math.cos(a), wc[1] + (R - 8) * math.sin(a))], fill=(110, 125, 150), width=2)
    d.ellipse([wc[0] - 14, wc[1] - 14, wc[0] + 14, wc[1] + 14], fill=(170, 185, 210))
    d.line([wc, (wc[0], 640)], fill=(170, 185, 210), width=8); d.line([(wc[0] - 80, 640), (wc[0] + 80, 640)], fill=(170, 185, 210), width=8)
    mouse(d, (wc[0], wc[1] + R - 62), .62)
    T(d, F, (wc[0], 675), "juvenile irradiated mice  幼年受照小鼠", 21, GREY)
    for k, (num, en, zh, col, y) in enumerate([("+37%", "specific force (EDL)", "比肌力", GREEN, 270), ("−50%", "mito ROS", "线粒体活性氧", GOLD, 470)]):
        panel(d, (560, y - 80, 910, y + 80), col, 30, col)
        T(d, F, (735, y - 32), num, 48, col)
        bil(d, F, (735, y + 42), en, zh, 23, WHITE, GREY, gap=17)
    T(d, F, (735, 576), "O'Connor 2022", 20, GREY)
    if st >= 1:
        panel(d, (980, 140, 1790, 690), PANEL, 160, (120, 140, 180))
        bil(d, F, (1385, 186), "RMS + chemo-RT model", "横纹肌肉瘤 + 放化疗模型", 28, WHITE, GREY, gap=21)
        # dumbbell
        dx, dy = 1200, 276
        d.line([(dx - 60, dy), (dx + 60, dy)], fill=(190, 200, 215), width=10)
        for s_ in (-1, 1): d.rounded_rectangle([dx + s_ * 60 - 16, dy - 32, dx + s_ * 60 + 16, dy + 32], 6, fill=(150, 160, 180))
        # treadmill
        tx, ty = 1560, 290
        d.rounded_rectangle([tx - 110, ty, tx + 110, ty + 18], 9, fill=(150, 160, 180))
        d.line([(tx + 90, ty), (tx + 120, ty - 70)], fill=(150, 160, 180), width=6)
        mouse(d, (tx - 10, ty - 22), .32)
        T(d, F, (1200, 334), "resistance 抗阻", 20, GREY); T(d, F, (1560, 334), "endurance 耐力", 20, GREY)
        rows = [("muscle mass preserved", "肌量保住"), ("inflammatory / fibrotic genes calmed", "炎症/纤维化基因平息"), ("more endothelial cells", "内皮细胞更多")]
        for k, (a, b) in enumerate(rows):
            y = 400 + k * 70
            check(d, (1040, y), 18, GREEN, 6)
            T(d, F, (1080, y - 12), a, 24, WHITE, 'lm'); T(d, F, (1080, y + 18), b, 21, GREY, 'lm')
    if st >= 2:
        y = 610
        xmark(d, (1040, y), 16, RED, 6)
        T(d, F, (1080, y - 12), "fibrosis not prevented", 24, (255, 150, 140), 'lm'); T(d, F, (1080, y + 18), "纤维化未被阻止", 21, GREY, 'lm')
        T(d, F, (735, 630), "mouse data —", 22, GOLD); T(d, F, (735, 662), "test in survivors 需在幸存者中检验", 21, GOLD)


# ---------------- 5 cold cases & summation ----------------
def folder(d, F, y, en, zh, icon, h=84):
    x0, x1 = 470, 1800
    d.polygon([(x0, y - h / 2), (x0 + 30, y - h / 2 - 16), (x0 + 170, y - h / 2 - 16), (x0 + 190, y - h / 2)], fill=(214, 186, 120))
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], 10, fill=(214, 186, 120, 240), outline=(240, 215, 160), width=2)
    ix = x0 + 70
    d.ellipse([ix - 40, y - 38, ix + 40, y + 38], fill=(30, 38, 58, 235))
    icon(ix, y)
    T(d, F, (x0 + 132, y - 16), en, 24, INK, 'lm'); T(d, F, (x0 + 132, y + 18), zh, 21, INK2, 'lm')
    stamp(d, F, (x1 - 110, y), "OPEN 未结", HRED, 22)

def s_coldcases(st, im, d, F, M):
    # filing cabinet
    d.rounded_rectangle([140, 200, 410, 660], 12, fill=(80, 92, 115, 235), outline=(160, 175, 200), width=3)
    for k in range(3):
        y0 = 220 + k * 146
        d.rounded_rectangle([160, y0, 390, y0 + 126], 8, fill=(100, 112, 135), outline=(170, 185, 210), width=2)
        d.rounded_rectangle([245, y0 + 20, 305, y0 + 36], 6, fill=(200, 205, 215))
    d.rounded_rectangle([160, 220, 390, 346], 8, fill=(60, 70, 92))
    T(d, F, (275, 168), "Cold cases  悬案", 28, GOLD)
    def ic_sen(x, y):
        cell(d, (x - 8, y + 8), 21, fill=(130, 130, 140), nucfill=(80, 80, 92)); T(d, F, (x + 16, y - 18), "p21", 20, GOLD)
    def ic_tl(x, y):
        d.line([(x - 30, y), (x + 30, y)], fill=WHITE, width=3)
        for k in range(5): d.line([(x - 30 + k * 15, y - 8), (x - 30 + k * 15, y + 8)], fill=WHITE, width=2)
        T(d, F, (x, y - 22), "?", 22, PURPLE)
    def ic_race(x, y):
        capillary(d, (x - 16, y), 14); sat_cell(d, (x + 18, y + 2), .32)
    def ic_inj(x, y):
        syringe(d, (x - 22, y), .28); T(d, F, (x, y + 22), "CTX", 20, (200, 220, 240))
    def ic_ev(x, y):
        for p in [(x - 14, y - 8), (x + 12, y - 12), (x, y + 14)]: ev(d, p, 9)
    items = [(0, "Senolytics in irradiated muscle — untested in vivo", "受照肌肉中的衰老清除剂——尚无活体研究", ic_sen),
             (1, "Macrophage time course after RT — unmapped", "照射后巨噬细胞时程——未绘制", ic_tl),
             (2, "Vessels or stem cells first?  (vessel-first shown in intestine)", "血管还是干细胞先倒下？（血管先行见于肠道）", ic_race),
             (3, "CTX / BaCl2 injury after RT — not confirmed", "照射后CTX/BaCl2损伤——未确认", ic_inj),
             (3, "EV therapy in irradiated muscle — none", "受照肌肉囊泡治疗——空白", ic_ev)]
    for i, (s0, en, zh, ic) in enumerate(items):
        if st >= s0:
            folder(d, F, 178 + i * 106, en, zh, ic)
    if st >= 3:
        T(d, F, (1135, 674), "each = a thesis   每份 = 一篇论文", 26, GOLD)


def stiff_muscle(d, c):
    x, y = c
    for k, yy in enumerate((y - 34, y, y + 34)):
        fiberseg(d, x - 70, x + 70, yy, 30, (150, 120, 130), nuclei=False)
    collagen(d, (x - 70, y - 50, x + 70, y + 50), 6, col=ICE, w=3)

def s_verdict(st, im, d, F, M):
    T(d, F, (W / 2 - 110, 150), "Summation", 40, GOLD, font='title'); T(d, F, (W / 2 + 110, 152), "结案陈词", 36, GOLD)
    cy = 400
    bolt(d, (175, cy), 1.5); T(d, F, (175, cy + 84), "beam 射线", 22, GOLD)
    stiff_muscle(d, (1740, cy)); T(d, F, (1740, cy + 84), "stiff muscle", 22, ICE); T(d, F, (1740, cy + 112), "僵硬肌肉", 20, GREY)
    xs = [345 + i * 238 for i in range(6)]; cw = 214; top, bot = 220, 576
    links = [
        (1, "DNA breaks", "DNA断裂", [("FACT", FGREEN)], 'dna'),
        (1, "fiber survives, precursors vulnerable", "纤维存活，前体脆弱", [("FACT · cells", FGREEN)], 'fib'),
        (1, "SC loss → small fibers for life", "卫星细胞丢失→终生偏小", [("FACT · mice", FGREEN)], 'sc'),
        (2, "FAPs senescent, fibrogenic", "FAPs衰老、促纤维化", [("FACT · mice", FGREEN), ("macrophage TGF-β: inferred", AMBER)], 'fap'),
        (2, "vessels ↓  mitochondria ↓", "血管↓  线粒体↓", [("FACT · animals", FGREEN), ("order: HYPOTHESIS", HRED)], 'ves'),
        (3, "late weakness, dysphagia, sarcopenia", "人体晚期无力、吞咽困难、肌少症", [("ASSOCIATION", AMBER)], 'hum'),
    ]
    d.line([(225, cy), (1660, cy)], fill=(120, 110, 80), width=3)
    for i, (s0, en, zh, tags, ic) in enumerate(links):
        x = xs[i]
        if st < s0:
            d.rounded_rectangle([x - cw / 2, top, x + cw / 2, bot], 18, fill=(16, 26, 46, 255), outline=(80, 92, 115), width=2)
            continue
        col = tags[0][1]
        d.rounded_rectangle([x - cw / 2, top, x + cw / 2, bot], 18, fill=(26, 38, 62, 250), outline=col, width=3)
        y = top + 38
        for ln in wrap(d, F, en, 23, cw - 26): T(d, F, (x, y), ln, 23, WHITE); y += 30
        y += 4
        for ln in wrap(d, F, zh, 20, cw - 26): T(d, F, (x, y), ln, 20, GREY); y += 27
        # tags stacked upward from the card bottom
        tl_all = [(t, c, wrap(d, F, t, 20, cw - 44)) for t, c in tags]
        yb = bot - 12
        for t, c, tl in reversed(tl_all):
            hh = 16 + 25 * len(tl)
            d.rounded_rectangle([x - cw / 2 + 12, yb - hh, x + cw / 2 - 12, yb], 10, fill=c + (50,), outline=c, width=2)
            yy = yb - hh / 2 - (len(tl) - 1) * 12.5
            for ln in tl: T(d, F, (x, yy), ln, 20, WHITE); yy += 25
            yb -= hh + 8
        iy = (y + yb) / 2
        if ic == 'dna':
            helix(d, x - 70, x + 70, iy, 18, breaks=(x,), w=4)
        elif ic == 'fib':
            fiberseg(d, x - 80, x + 30, iy, 34, nuclei=False); shieldicon(d, (x + 62, iy), .9)
        elif ic == 'sc':
            fiberseg(d, x - 80, x + 80, iy + 10, 30, nuclei=False); sat_cell(d, (x - 30, iy - 14), .4, dead=True); sat_cell(d, (x + 30, iy - 14), .4, dead=True)
        elif ic == 'fap':
            fap(d, (x - 40, iy), .45, grey=True); collagen(d, (x + 4, iy - 18, x + 84, iy + 18), 3, col=ICE)
        elif ic == 'ves':
            capillary(d, (x - 40, iy), 18, cut=True); mito(d, (x + 40, iy), 74, 36)
        else:
            human(d, (x, iy + 14), .42, (200, 205, 215))
    for i in range(5):
        a = xs[i] + cw / 2; b = xs[i + 1] - cw / 2; m = (a + b) / 2
        on = st >= links[i + 1][0]
        d.ellipse([m - 20, cy - 11, m + 20, cy + 11], outline=GOLD if on else (90, 100, 118), width=4)
    if st >= 3:
        tx, ty = 1560, 640
        cancer_cell(d, (tx, ty), 28)
        darrow(d, (tx + 28, ty - 26), (1712, cy + 134), (210, 180, 240), 3, 12, 12)
        T(d, F, (tx - 44, ty - 14), "tumour EVs?", 22, (210, 180, 240), 'rm'); T(d, F, (tx - 44, ty + 16), "肿瘤囊泡？", 20, GREY, 'rm')
        d.rounded_rectangle([330, 604, 1290, 682], 20, fill=GOLD + (40,), outline=GOLD, width=3)
        T(d, F, (810, 627), "not one culprit — a conspiracy", 30, GOLD)
        T(d, F, (810, 662), "不是单一罪犯 —— 是合谋", 24, (230, 215, 170))


def microscope(d, c, s=1.0, col=(170, 185, 210)):
    x, y = c
    d.rounded_rectangle([x - 66 * s, y - 20 * s, x + 66 * s, y], 8, fill=col)
    d.line([(x + 40 * s, y - 20 * s), (x + 40 * s, y - 112 * s), (x + 8 * s, y - 148 * s)], fill=col, width=int(24 * s), joint='curve')
    d.rectangle([x - 56 * s, y - 84 * s, x + 44 * s, y - 72 * s], fill=col)
    d.line([(x - 8 * s, y - 92 * s), (x - 8 * s, y - 128 * s)], fill=col, width=int(16 * s))
    d.line([(x - 8 * s, y - 124 * s), (x - 32 * s, y - 186 * s)], fill=col, width=int(30 * s))
    d.line([(x - 32 * s, y - 182 * s), (x - 44 * s, y - 214 * s)], fill=(200, 212, 230), width=int(18 * s))

def s_sendoff(st, im, d, F, M):
    # dawn window (gradient sky inside the frame only)
    wx0, wy0, wx1, wy1 = 170, 150, 610, 470
    sky = [(40, 42, 78), (70, 56, 92), (120, 74, 98), (176, 98, 92), (226, 136, 84), (246, 176, 100)]
    n = 16
    for k in range(n):
        t = k / (n - 1); i0 = min(int(t * (len(sky) - 1)), len(sky) - 2); f = t * (len(sky) - 1) - i0
        c = tuple(int(sky[i0][j] + (sky[i0 + 1][j] - sky[i0][j]) * f) for j in range(3))
        d.rectangle([wx0, wy0 + k * (wy1 - wy0) / n, wx1, wy0 + (k + 1) * (wy1 - wy0) / n + 1], fill=c + (230,))
    def half(r, col):
        d.polygon([(390 + r * math.cos(math.pi + k * math.pi / 40), wy1 + r * math.sin(math.pi + k * math.pi / 40)) for k in range(41)], fill=col)
    half(130, (238, 158, 96, 235)); half(92, (248, 186, 112, 240)); half(60, (255, 222, 150, 255))
    d.rounded_rectangle([wx0, wy0, wx1, wy1], 6, outline=(150, 140, 160), width=6)
    d.line([(390, wy0), (390, wy1)], fill=(150, 140, 160), width=5); d.line([(wx0, 310), (wx1, 310)], fill=(150, 140, 160), width=5)
    d.rectangle([wx0 - 20, wy1, wx1 + 20, wy1 + 12], fill=(150, 140, 160))
    # researcher behind the bench
    human(d, (820, 446), 1.2, (150, 165, 190))
    # bench
    d.rectangle([140, 556, 1780, 580], fill=(120, 95, 70), outline=(180, 150, 115))
    d.rectangle([180, 580, 210, 688], fill=(100, 80, 60)); d.rectangle([1710, 580, 1740, 688], fill=(100, 80, 60))
    microscope(d, (620, 556), 1.0)
    for k in range(3):
        d.rounded_rectangle([300 + k * 6, 528 - k * 14, 450 + k * 6, 554 - k * 14], 4, fill=(214, 186, 120), outline=(240, 215, 160))
        d.polygon([(300 + k * 6, 528 - k * 14), (312 + k * 6, 520 - k * 14), (360 + k * 6, 520 - k * 14), (368 + k * 6, 528 - k * 14)], fill=(214, 186, 120))
    T(d, F, (380, 584 + 28), "cold cases 悬案", 20, GREY)
    # notebook (single page)
    nb = (1000, 170, 1720, 548)
    d.rounded_rectangle(nb, 10, fill=CREAM + (245,))
    for k in range(9): d.ellipse([988, 196 + k * 40, 1012, 212 + k * 40], outline=(130, 120, 100), width=3)
    for yy in range(250, 540, 72): d.line([(1040, yy), (1690, yy)], fill=(200, 190, 160), width=1)
    if st >= 1:
        items = [("dose · animal · duration", "剂量 · 动物 · 时长"), ("shield the leg", "遮挡对侧"), ("blind the count", "盲法计数"), ("measure force · tag evidence", "测肌力 · 标证据")]
        for k, (a, b) in enumerate(items):
            y = 210 + k * 72
            check(d, (1060, y + 10), 13, (46, 140, 80), 5)
            T(d, F, (1092, y), a, 24, INK, 'lm'); T(d, F, (1460, y), b, 22, INK2, 'lm')
        T(d, F, (1360, 506), "handed to you   交给你", 32, (150, 50, 50))
        d.line([(1180, 530), (1540, 530)], fill=(150, 50, 50, 160), width=2)
    T(d, F, (W / 2 - 110, 640), "The case is open", 40, GOLD, font='title'); T(d, F, (W / 2 + 175, 642), "案子仍未结", 34, GOLD)


SCENES = {
    'case4': s_case4, 'rfs': s_rfs, 'swallow': s_swallow, 'survivor': s_survivor, 'biopsy': s_biopsy,
    'models': s_models, 'doses': s_doses, 'readouts': s_readouts, 'timeline4': s_timeline4, 'bench': s_bench4,
    'conflict': s_conflict, 'tumorev': s_tumorev, 'ptx': s_ptx, 'tgfb': s_tgfb, 'cells': s_cells, 'exercise': s_exercise,
    'coldcases': s_coldcases, 'verdict': s_verdict, 'sendoff': s_sendoff,
}
