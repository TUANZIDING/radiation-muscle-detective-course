"""Mechanism diagrams for 'After the Beam'. draw(key, step, im, d, F, M). Drawing area y 110..690."""
import math, random

W = 1920
WHITE = (240, 242, 246); GREY = (150, 160, 175); DIM = (90, 100, 118)
BLUE = (90, 160, 230); ORANGE = (240, 150, 70); RED = (230, 80, 70); GREEN = (90, 220, 120)
GOLD = (244, 210, 130); PINK = (226, 120, 150); MAG = (220, 70, 140); TEAL = (70, 200, 190)

def T(d, F, xy, s, size=30, fill=WHITE, anchor='mm', font='sans'):
    d.text(xy, s, font=F(font, size), fill=fill, anchor=anchor)

def arrow(d, a, b, fill=WHITE, w=5, head=18):
    d.line([a, b], fill=fill, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p1 = (b[0] - head * math.cos(ang - 0.45), b[1] - head * math.sin(ang - 0.45))
    p2 = (b[0] - head * math.cos(ang + 0.45), b[1] - head * math.sin(ang + 0.45))
    d.polygon([b, p1, p2], fill=fill)

def box(d, F, x0, y0, x1, y1, title, sub=None, col=BLUE, size=30):
    d.rounded_rectangle([x0, y0, x1, y1], 18, fill=col + (55,), outline=col + (255,), width=3)
    cy = (y0 + y1) / 2
    if sub:
        T(d, F, ((x0 + x1) / 2, cy - 20), title, size)
        T(d, F, ((x0 + x1) / 2, cy + 22), sub, size - 6, GREY)
    else:
        T(d, F, ((x0 + x1) / 2, cy), title, size)

def helix(d, x0, x1, yc, amp=40, breaks=(), single=(), col1=BLUE, col2=ORANGE, w=6):
    n = int((x1 - x0) / 4)
    pts1, pts2 = [], []
    for i in range(n + 1):
        x = x0 + i * 4; ph = (x - x0) / 70
        pts1.append((x, yc + amp * math.sin(ph))); pts2.append((x, yc - amp * math.sin(ph)))
    def gaps(x):
        return any(abs(x - b) < 14 for b in breaks)
    def gap1(x):
        return gaps(x) or any(abs(x - b) < 14 for b in single)
    # rungs
    for i in range(0, n, 6):
        x = x0 + i * 4
        if gaps(x): continue
        d.line([pts1[i], pts2[i]], fill=(120, 130, 150), width=2)
    for pts, g in ((pts1, gap1), (pts2, gaps)):
        seg = []
        for p in pts:
            if g(p[0]):
                if len(seg) > 1: d.line(seg, fill=col1 if pts is pts1 else col2, width=w)
                seg = []
            else: seg.append(p)
        if len(seg) > 1: d.line(seg, fill=col1 if pts is pts1 else col2, width=w)

def cell(d, c, r, fill=(60, 90, 130), nuc=True, outline=(150, 180, 220), nucfill=(40, 55, 90)):
    x, y = c
    d.ellipse([x - r, y - r, x + r, y + r], fill=fill + (210,), outline=outline, width=3)
    for k in range(1, 9):  # soft radial highlight
        rr = r * (1 - k / 10); ox, oy = -r * 0.18 * k / 9, -r * 0.22 * k / 9
        lift = tuple(min(255, int(v + 9 * k)) for v in fill)
        d.ellipse([x + ox - rr, y + oy - rr, x + ox + rr, y + oy + rr], fill=lift + (60,))
    if nuc:
        d.ellipse([x - r * .45, y - r * .45, x + r * .45, y + r * .45], fill=nucfill + (235,), outline=(130, 150, 200), width=2)
        d.ellipse([x - r * .30, y - r * .32, x + r * .10, y - r * .05], fill=(255, 255, 255, 18))

def foci(d, c, r, n, seed=1, col=GREEN, size=7):
    rnd = random.Random(seed)
    for _ in range(n):
        a = rnd.uniform(0, 6.283); rr = r * math.sqrt(rnd.uniform(0, 1))
        x, y = c[0] + rr * math.cos(a), c[1] + rr * math.sin(a)
        d.ellipse([x - size, y - size, x + size, y + size], fill=col)

def fiber(d, F, y, x0=180, x1=1740, h=120, nuclei=True, sat=False, satglow=False):
    d.rounded_rectangle([x0, y - h / 2, x1, y + h / 2], 60, fill=(150, 60, 70, 170), outline=(220, 120, 130), width=3)
    for x in range(x0 + 40, x1 - 20, 26):
        d.line([(x, y - h / 2 + 12), (x, y + h / 2 - 12)], fill=(190, 90, 100, 120), width=2)
    if nuclei:
        for x in range(x0 + 110, x1 - 60, 150):
            d.ellipse([x - 26, y - 12, x + 26, y + 12], fill=(70, 70, 150), outline=(160, 160, 230), width=2)
    if sat:
        sx, sy = (x0 + x1) / 2 + 60, y - h / 2 - 22
        if satglow: d.ellipse([sx - 70, sy - 50, sx + 70, sy + 50], fill=(230, 60, 120, 60))
        d.ellipse([sx - 46, sy - 24, sx + 46, sy + 24], fill=MAG + (230,), outline=(255, 180, 210), width=3)
        d.ellipse([sx - 18, sy - 12, sx + 18, sy + 12], fill=(120, 30, 80))

# ---------------- scenes ----------------
def s_title(st, im, d, F, M):
    T(d, F, (W / 2, 300), "AFTER THE BEAM", 110, WHITE, font='title')
    T(d, F, (W / 2, 400), "射线之后 · 辐射致骨骼肌损伤的侦探故事", 44, GOLD)
    T(d, F, (W / 2, 500), f"Episode {M.EP}: {M.TITLE_EN}", 48, (210, 215, 225), font='gari')
    T(d, F, (W / 2, 565), f"第{['一','二','三','四'][M.EP-1]}集  {M.TITLE_ZH}", 40, GREY)
    d.line([(W / 2 - 300, 440), (W / 2 + 300, 440)], fill=GOLD, width=2)

def s_section(st, im, d, F, M, sec='', secz=''):
    pass

def s_case(st, im, d, F, M):
    # stylized leg + beam + timeline
    x = 620
    d.rounded_rectangle([x - 110, 160, x + 110, 640], 100, fill=(70, 80, 100), outline=(150, 160, 180), width=3)
    T(d, F, (x, 680), "示意病例  Composite case", 24, GREY)
    if st >= 0:
        d.ellipse([x - 50, 330, x + 50, 430], fill=(160, 60, 60) if st < 1 else (90, 60, 60), outline=(220, 120, 120), width=3)
        T(d, F, (x + 190, 380), "tumor 肿瘤" if st < 1 else "tumor gone 肿瘤消失", 28, (230, 160, 160), 'lm')
    if st == 0:
        for k in range(-3, 4):
            d.line([(x - 420, 380 + k * 14), (x - 60, 380 + k * 4)], fill=(255, 230, 120, 120), width=4)
        T(d, F, (x - 420, 300), "radiotherapy 放疗", 30, GOLD, 'lm')
    if st >= 2:
        d.rounded_rectangle([x - 80, 250, x + 80, 520], 60, fill=(120, 90, 80, 160), outline=(200, 160, 120), width=4)
        T(d, F, (x + 190, 450), "thin + stiff 变细·变硬", 30, ORANGE, 'lm')
        # stairs
        for i in range(5):
            d.rectangle([1200 + i * 90, 600 - i * 80, 1290 + i * 90, 640], fill=(80, 90, 110), outline=(140, 150, 170))
        T(d, F, (1420, 180), "5 years later  五年后", 34, WHITE)
    if st >= 3:
        T(d, F, (1340, 250), "Why?", 60, GOLD, font='title'); T(d, F, (1530, 255), "为什么？", 50, GOLD)

def s_tags(st, im, d, F, M):
    items = [((46, 160, 90), "FACT  事实", "direct experiment 直接实验证明"),
             ((214, 150, 40), "ASSOCIATION  关联", "travel together, cause unproven 共同出现，因果未证"),
             ((200, 70, 60), "HYPOTHESIS  假说", "awaiting its day in court 有待检验")]
    for i, (c, a, b) in enumerate(items):
        y = 220 + i * 150
        d.rounded_rectangle([360, y, 820, y + 80], 40, fill=c + (235,))
        T(d, F, (590, y + 40), a, 36)
        T(d, F, (880, y + 40), b, 32, WHITE, 'lm')

def s_photon(st, im, d, F, M):
    d.rectangle([700, 150, 1700, 660], fill=(150, 70, 80, 40), outline=(200, 120, 130, 120), width=2)
    T(d, F, (1200, 640), "tissue 组织", 26, GREY)
    # wavy photon
    pts = [(160 + i * 6, 400 + 18 * math.sin(i * 0.5)) for i in range(0, 95)]
    d.line(pts, fill=GOLD, width=5); arrow(d, pts[-1], (760, 400), GOLD)
    T(d, F, (380, 330), "X-ray photon  X 射线光子", 32, GOLD)
    rnd = random.Random(3)
    atoms = [(rnd.randint(780, 1650), rnd.randint(190, 610)) for _ in range(22)]
    for i, (x, y) in enumerate(atoms):
        d.ellipse([x - 16, y - 16, x + 16, y + 16], outline=(170, 190, 220), width=3)
        if st >= 1 and i % 3 == 0:
            d.text((x - 8, y - 18), "+", font=F('sans', 30), fill=RED)
            arrow(d, (x + 18, y), (x + 90, y - 50), TEAL, 3, 12)
            d.ellipse([x + 88, y - 58, x + 100, y - 46], fill=TEAL)
    if st >= 1:
        T(d, F, (1200, 120 + 0), "ionization: electrons knocked out  电离：电子被撞出", 30, TEAL)

def s_water(st, im, d, F, M):
    def h2o(x, y, s=1):
        d.ellipse([x - 26 * s, y - 26 * s, x + 26 * s, y + 26 * s], fill=(200, 60, 60))
        for dx in (-34, 34):
            d.ellipse([x + dx * s - 14 * s, y + 20 * s - 14 * s, x + dx * s + 14 * s, y + 20 * s + 14 * s], fill=(230, 230, 240))
    h2o(330, 360); T(d, F, (330, 450), "H2O  水 (~70%)", 30)
    if st >= 1:
        arrow(d, (420, 380), (620, 380), GOLD); T(d, F, (520, 340), "radiation", 26, GOLD)
        d.ellipse([680, 340, 760, 420], fill=(230, 60, 50)); d.ellipse([700, 300, 740, 340], fill=(230, 230, 240))
        T(d, F, (720, 470), "•OH  羟自由基", 36, RED)
        T(d, F, (720, 520), "lives ~ns, travels a few nm", 24, GREY)
        T(d, F, (720, 552), "寿命极短，只走几纳米", 24, GREY)
    helix(d, 950, 1750, 380, 70, breaks=(1300,) if st >= 2 else ())
    T(d, F, (1350, 520), "DNA", 34, BLUE)
    if st >= 2:
        arrow(d, (780, 380), (1260, 380), RED, 5)
        for k in range(8):
            a = k * 0.785; d.line([(1300, 380), (1300 + 50 * math.cos(a), 380 + 50 * math.sin(a))], fill=RED, width=3)

def s_direct(st, im, d, F, M):
    T(d, F, (500, 160), "Direct action  直接作用", 36, GOLD)
    helix(d, 220, 780, 420, 55, breaks=(500,))
    pts = [(300 + i * 6, 220 + i * 5 + 10 * math.sin(i * .6)) for i in range(32)]
    d.line(pts, fill=GOLD, width=4); arrow(d, pts[-1], (495, 400), GOLD)
    if st >= 1:
        T(d, F, (1400, 160), "Indirect action  间接作用", 36, RED)
        helix(d, 1120, 1680, 420, 55, breaks=(1450,))
        pts = [(1150 + i * 6, 260 + 8 * math.sin(i * .6)) for i in range(25)]
        d.line(pts, fill=GOLD, width=4)
        d.ellipse([1300 - 24, 260 - 24, 1300 + 24, 260 + 24], fill=(200, 60, 60)); T(d, F, (1240, 260), "H2O", 24, WHITE, 'rm')
        arrow(d, (1320, 285), (1440, 395), RED); T(d, F, (1460, 320), "•OH", 32, RED, 'lm')
        T(d, F, (1400, 580), "X-rays: most damage  X 射线的主要途径", 28, WHITE)
        T(d, F, (1400, 625), "O2 'fixes' damage  氧气固定损伤", 26, GREY)

def s_dose(st, im, d, F, M):
    T(d, F, (W / 2, 160), "1 Gy = 1 J / kg", 54, GOLD, font='title')
    marks = [(0.05, "0.01–0.1 Gy", "CT-scan range CT 量级"), (2, "2 Gy", "one clinical fraction 单次放疗"),
             (16, "16 Gy", "single dose, mouse 小鼠单次"), (60, "60 Gy", "total course, patient 病人总量"), (90, "90 Gy", "single dose, rat 大鼠单次")]
    x0, x1, y = 200, 1720, 420
    d.line([(x0, y), (x1, y)], fill=WHITE, width=4)
    for i, (v, a, b) in enumerate(marks):
        x = x0 + (math.log10(v * 100) / math.log10(9000)) * (x1 - x0)
        d.line([(x, y - 20), (x, y + 20)], fill=GOLD, width=4)
        up = 60 + (50 if i == 4 else 0); dn = 60 + (45 if i in (2, 4) else 0)
        T(d, F, (x, y - up), a, 30, GOLD); T(d, F, (x, y + dn), b, 24, GREY)
    T(d, F, (W / 2, 560), "log scale 对数刻度", 22, DIM)
    if st >= 1:
        T(d, F, (W / 2, 630), "Dose makes the poison  剂量决定毒性", 44, RED, font='sans')

def s_fraction(st, im, d, F, M):
    T(d, F, (480, 170), "one blow  一次给完", 32)
    d.rectangle([420, 560 - 360, 540, 560], fill=RED + (200,))
    if st >= 1:
        T(d, F, (1260, 170), "fractions: ~2 Gy × 30  分次：约 2 Gy × 30", 32)
        for i in range(30):
            x = 800 + i * 31; d.rectangle([x, 520, x + 20, 560], fill=GOLD)
        T(d, F, (1260, 610), "repair between visits  两次之间可修复", 28, GREEN)
    if st >= 2:
        T(d, F, (W / 2, 660), "same total ≠ same effect → compare by BED  同总量≠同效应，用 BED 比较", 30, TEAL)
    d.line([(380, 560), (1760, 560)], fill=GREY, width=2)

def s_dna(st, im, d, F, M):
    br = () ; sg = ()
    if st >= 1: sg = (700,)
    if st >= 2: br = (1250,)
    helix(d, 200, 1720, 380, 80, breaks=br, single=sg)
    T(d, F, (W / 2, 180), "DNA: two strands, mirror copies  两条互为副本的链", 34)
    if st >= 1:
        T(d, F, (700, 540), "single-strand break 单链断裂", 30, GOLD)
        T(d, F, (700, 585), "easy: copy from the other strand 照另一条链补", 24, GREEN)
    if st >= 2:
        T(d, F, (1250, 540), "double-strand break 双链断裂", 30, RED)
    if st >= 3:
        T(d, F, (1250, 585), "no template at that spot 原位无副本", 24, RED)

def s_cluster(st, im, d, F, M):
    helix(d, 200, 1720, 380, 80, breaks=(980,) if st >= 1 else (), single=(560, 1400) if st == 0 else (900, 1060, 940))
    T(d, F, (W / 2, 180), "Ward 1990: SSB far more common; DSB tied to cell death", 30)
    T(d, F, (W / 2, 225), "单链断裂多得多；双链断裂与细胞死亡最相关", 28, GOLD)
    if st >= 1:
        d.ellipse([860, 260, 1100, 500], outline=RED, width=4)
        T(d, F, (980, 560), "clustered damage = a volley of shot  成簇损伤，像一阵霰弹", 30, RED)

def s_h2ax(st, im, d, F, M):
    c = (700, 400)
    cell(d, c, 220, fill=(40, 60, 90), nuc=False)
    d.ellipse([c[0] - 150, c[1] - 130, c[0] + 150, c[1] + 130], fill=(30, 40, 80), outline=(100, 120, 180), width=3)
    T(d, F, (700, 660), "nucleus 细胞核", 24, GREY)
    if st >= 1:
        T(d, F, (1340, 250), "H2AX  →  γH2AX (Ser139-P)", 38, GREEN)
        T(d, F, (1340, 300), "histone 'spool' tagged within minutes", 26, GREY)
        T(d, F, (1340, 335), "断口附近的组蛋白几分钟内被磷酸化", 26, GREY)
    if st >= 2:
        foci(d, c, 120, 18 if st == 2 else 4, seed=5)
        T(d, F, (1340, 440), "1 dot ≈ 1 break   一个亮点≈一个断口", 32, GREEN)
    if st >= 3:
        T(d, F, (1340, 520), "dots fade = repair  亮点消退 = 修复", 32, GOLD)
        for i, (lab, n) in enumerate([("30 min", 18), ("4 h", 9), ("24 h", 3)]):
            x = 1150 + i * 190; cc = (x, 610)
            d.ellipse([x - 55, 560, x + 55, 660], fill=(30, 40, 80), outline=(100, 120, 180), width=2)
            foci(d, cc, 38, n, seed=i + 9, size=5)
            T(d, F, (x, 680), lab, 22, GREY)

def s_bench(st, im, d, F, M):
    titles = ["γH2AX foci: timing & controls  γH2AX 灶：时间点与对照",
              "Which crew? block it  哪支修复队？拦住它",
              "Which fate? several witnesses  哪种命运？多个证人",
              "In vivo: shielded control leg  活体：遮挡对侧腿作对照"]
    rows = [[("30 min", "initial breaks 初始断口"), ("24 h", "residual foci 残余灶"), ("+ 53BP1", "co-localize 共定位"), ("blind count", "盲法计数")],
            [("DNA-PKcs inhibitor", "NHEJ slowed? 焊工变慢？"), ("ATM inhibitor", "alarm test 检验警报"), ("knockdown", "second proof 第二种证明"), ("", "")],
            [("cleaved caspase-3 / TUNEL", "apoptosis 凋亡"), ("SA-β-gal", "senescence 衰老"), ("p21 / p16 ↑ · Ki-67 ↓", "senescence 衰老"), ("≥ 2–3 markers", "多标记一致")],
            [("irradiate one leg", "照射一侧"), ("shield the other", "遮挡对侧"), ("PAX7 per 100 fibers", "每百根纤维干细胞数"), ("CSA · fibrosis · force", "纤维粗细·纤维化·肌力")]]
    d.rounded_rectangle([160, 140, 1760, 680], 24, fill=(230, 225, 205, 22), outline=(200, 190, 150), width=2)
    T(d, F, (W / 2, 195), titles[st], 36, GOLD)
    for i, (a, b) in enumerate(rows[st]):
        if not a: continue
        y = 280 + i * 95
        d.ellipse([240, y - 14, 268, y + 14], fill=(70, 120, 200))
        T(d, F, (300, y), a, 32, WHITE, 'lm'); T(d, F, (1000, y), b, 30, GREY, 'lm')

def s_atm(st, im, d, F, M):
    helix(d, 160, 900, 400, 60, breaks=(530,))
    T(d, F, (530, 560), "DSB", 30, RED)
    if st >= 1:
        d.ellipse([470, 220, 590, 340], fill=(80, 140, 230), outline=WHITE, width=3); T(d, F, (530, 280), "ATM", 32)
        T(d, F, (530, 190), "sentry 哨兵", 26, GREY)
        T(d, F, (530, 630), "marks H2AX, p53 …  标记 H2AX、p53", 24, GREY)
    if st >= 2:
        outs = [("checkpoint: stop the cycle", "检查点：细胞周期暂停", 230, BLUE), ("call repair crews", "召来修复队", 400, GREEN), ("die or stop for good", "死亡或永久停工", 570, RED)]
        for a, b, y, c in outs:
            arrow(d, (620, 280), (1080, y), c, 4)
            box(d, F, 1090, y - 55, 1760, y + 55, a, b, c, 30)

def s_repair(st, im, d, F, M):
    T(d, F, (W / 2, 150), "Two repair crews  两支修复队", 38)
    if st >= 1:
        box(d, F, 140, 200, 920, 300, "NHEJ: the fast welder", "非同源末端连接：快手焊工", GOLD)
        helix(d, 200, 860, 430, 40, breaks=(530,))
        for x in (505, 555):
            d.ellipse([x - 22, 405, x + 22, 455], outline=GOLD, width=6)
        T(d, F, (530, 500), "Ku ring grabs ends · DNA-PKcs", 24, GOLD)
        T(d, F, (530, 545), "any time · may lose letters  随时可用·接缝可能丢字母", 24, GREY)
    if st >= 2:
        box(d, F, 1000, 200, 1780, 300, "HR: the careful scribe", "同源重组：细心的抄写员", TEAL)
        helix(d, 1060, 1720, 410, 30, breaks=(1390,))
        helix(d, 1060, 1720, 500, 30, col1=(120, 200, 190), col2=(120, 200, 190), w=4)
        arrow(d, (1390, 480), (1390, 430), TEAL, 3, 10)
        T(d, F, (1390, 570), "needs sister copy → only cells preparing to divide", 24, TEAL)
        T(d, F, (1390, 605), "需要姐妹副本：只有准备分裂的细胞能用", 24, GREY)
    if st >= 3:
        T(d, F, (W / 2, 660), "resting cell → welder only   静息细胞只能靠焊工", 34, GOLD)

def s_vahidi(st, im, d, F, M):
    T(d, F, (W / 2, 160), "Vahidi Ferdousi 2014 · repair after IR (qualitative)  照射后修复（示意）", 30)
    cats = [("quiescent MuSC", "静息肌干细胞", 0.9, GREEN), ("committed progeny", "定向子代细胞", 0.55, GOLD), ("myonuclei", "成熟肌核", 0.25, RED)]
    for i, (a, b, v, c) in enumerate(cats):
        if st == 0 and i > 0: break
        if st == 1 and i > 1: break
        y = 260 + i * 140
        T(d, F, (520, y + 30), a, 30, WHITE, 'rm'); T(d, F, (520, y + 68), b, 24, GREY, 'rm')
        d.rounded_rectangle([560, y + 10, 560 + 1100 * v, y + 80], 12, fill=c + (220,))
    T(d, F, (1100, 680), "repair speed & accuracy (DNA-PKcs-dependent NHEJ)  修复速度与准确度", 24, GREY)

def s_fates(st, im, d, F, M):
    cell(d, (360, 400), 80, fill=(70, 90, 130)); T(d, F, (360, 520), "damaged cell 受损细胞", 26, GREY)
    roads = [("REPAIR  修好", "carries on 继续生活", 220, GREEN), ("DIE  死亡", "apoptosis / mitotic catastrophe 凋亡/有丝分裂灾难", 400, RED), ("FREEZE  冻结", "senescence (p53 → p21) 衰老", 580, TEAL)]
    for i, (a, b, y, c) in enumerate(roads):
        on = st >= i + 1
        col = c if on else DIM
        arrow(d, (450, 400), (900, y), col, 5)
        d.rounded_rectangle([910, y - 55, 1780, y + 55], 18, fill=col + (50,), outline=col, width=3)
        T(d, F, (940, y - 18), a, 32, WHITE if on else DIM, 'lm'); T(d, F, (940, y + 24), b, 24, GREY if on else DIM, 'lm')

def s_sasp(st, im, d, F, M):
    c = (900, 400)
    if st >= 1:
        for r in (130, 190, 250):
            d.ellipse([c[0] - r, c[1] - r * .8, c[0] + r, c[1] + r * .8], outline=(240, 160, 80, 140), width=3)
    cell(d, c, 80, fill=(90, 110, 120), nucfill=(60, 70, 80))
    T(d, F, (900, 540 if st < 1 else 640), "senescent cell 衰老细胞", 26, GREY)
    if st >= 1:
        T(d, F, (1500, 260), "SASP", 60, ORANGE, font='title')
        T(d, F, (1500, 330), "inflammatory signals + enzymes", 26)
        T(d, F, (1500, 365), "炎症因子与各种酶", 26, GREY)
    if st >= 2:
        for k, (x, y) in enumerate([(560, 230), (520, 520), (1240, 560), (1250, 220), (700, 640)]):
            cell(d, (x, y), 46, fill=(150, 100, 60), nuc=True)
        T(d, F, (1500, 470), "rumor mill → neighbors change", 28, ORANGE)
        T(d, F, (1500, 505), "谣言工厂：邻居被改变", 28, GREY)

def s_timeline(st, im, d, F, M):
    x0, x1, y = 200, 1720, 420
    d.line([(x0, y), (x1, y)], fill=WHITE, width=4)
    for x, lab in [(200, "RT 放疗"), (520, "weeks 周"), (950, "months 月"), (1500, "years 年")]:
        d.line([(x, y - 14), (x, y + 14)], fill=WHITE, width=3); T(d, F, (x, y + 45), lab, 26, GREY)
    if st >= 1:
        d.rounded_rectangle([280, 250, 700, 360], 18, fill=GOLD + (50,), outline=GOLD, width=3)
        T(d, F, (490, 285), "early effects 早期效应", 28); T(d, F, (490, 325), "skin, gut lining 皮肤·肠黏膜", 22, GREY)
    if st >= 2:
        d.rounded_rectangle([900, 230, 1700, 360], 18, fill=RED + (50,), outline=RED, width=3)
        T(d, F, (1300, 270), "late effects 晚期效应", 30); T(d, F, (1300, 315), "fibrosis · stiffness · atrophy  纤维化·僵硬·萎缩", 24, GREY)
        T(d, F, (1300, 560), "active, ongoing process (Bentzen 2006)", 28, WHITE)
        T(d, F, (1300, 600), "持续进行的主动过程：细胞因子·促瘢痕信号·小血管损伤", 24, GREY)

def s_fiber(st, im, d, F, M):
    fiber(d, F, 400, sat=st >= 3, satglow=st >= 3)
    T(d, F, (W / 2, 180), "skeletal muscle fiber  骨骼肌纤维", 36)
    if st >= 1:
        T(d, F, (W / 2, 520), "one giant cell · hundreds of nuclei (fused precursors)", 28)
        T(d, F, (W / 2, 560), "一个巨大的细胞，数百个细胞核，由前体细胞融合而成", 26, GREY)
    if st >= 2:
        T(d, F, (W / 2, 630), "never divides again → no mitotic death  不再分裂 → 不会分裂失败而死", 28, GREEN)
    if st >= 3:
        T(d, F, (1100, 260), "?", 60, GOLD, font='title')

def s_latella(st, im, d, F, M):
    T(d, F, (W / 2, 150), "Latella 2004 · 10 Gy", 34)
    T(d, F, (500, 210), "myoblasts (divide) 成肌细胞（可分裂）", 30)
    for i, x in enumerate((360, 500, 640)): cell(d, (x, 340), 55, fill=(80, 100, 140))
    T(d, F, (1400, 210), "myotubes (fused) 肌管（已融合）", 30)
    d.rounded_rectangle([1100, 300, 1700, 380], 40, fill=(150, 60, 70, 180), outline=(220, 120, 130), width=3)
    for x in range(1160, 1680, 90): d.ellipse([x - 20, 330, x + 20, 350], fill=(70, 70, 150))
    if st >= 1:
        for x in (360, 500, 640): foci(d, (x, 340), 22, 4, seed=x, size=5)
        foci(d, (1400, 340), 30, 0)
        for x in range(1160, 1680, 90): d.ellipse([x - 6, 334, x + 6, 346], fill=GREEN)
        T(d, F, (W / 2, 440), "both: ATM on, γH2AX foci  两者都启动 ATM、出现 γH2AX", 28, GREEN)
    if st >= 2:
        T(d, F, (500, 520), "ATM → p53 → apoptosis", 30, RED); T(d, F, (500, 560), "易凋亡", 28, RED)
        T(d, F, (1400, 520), "ATM → p53 blocked · no apoptosis", 30, GREEN); T(d, F, (1400, 560), "信号被拦截，不凋亡", 28, GREEN)
        T(d, F, (W / 2, 640), "differentiation-induced radioresistance  分化诱导的放射抵抗", 30, GOLD)

def s_organoid(st, im, d, F, M):
    c = (720, 410)
    d.ellipse([c[0] - 250, c[1] - 220, c[0] + 250, c[1] + 220], fill=(150, 70, 80, 120), outline=(220, 130, 140), width=3)
    rnd = random.Random(4)
    pax = [(c[0] + rnd.randint(-190, 190), c[1] + rnd.randint(-160, 160)) for _ in range(9)]
    for p in pax:
        d.ellipse([p[0] - 22, p[1] - 22, p[0] + 22, p[1] + 22], fill=MAG + (230,))
        if st >= 1:
            foci(d, p, 12, 3 if st == 1 else 0, seed=p[0], size=5)
    T(d, F, (720, 670), "human muscle organoid (hPSC)  人肌肉类器官", 26, GREY)
    T(d, F, (1420, 260), "● PAX7+ stem cells  干细胞", 32, MAG)
    if st >= 1:
        T(d, F, (1420, 340), "2 Gy → γH2AX highest in PAX7+", 32, GREEN)
        T(d, F, (1420, 380), "PAX7+ 细胞的断口信号最强", 28, GREY)
    if st >= 2:
        T(d, F, (1420, 470), "72 h: foci fade (repair)", 32, GOLD)
        T(d, F, (1420, 510), "72 小时亮点消退", 28, GREY)

def s_evidence(st, im, d, F, M):
    d.rounded_rectangle([140, 140, 1780, 680], 20, fill=(120, 90, 60, 40), outline=(180, 150, 100), width=3)
    T(d, F, (W / 2 - 60, 190), "EVIDENCE BOARD", 40, GOLD, font='title'); T(d, F, (W / 2 + 170, 192), "证据板", 36, GOLD)
    if st >= 1:
        box(d, F, 200, 250, 900, 420, "fiber survives the beam", "肌纤维挺过射线", GREEN)
        box(d, F, 1020, 250, 1720, 420, "muscle thin & stiff years later", "多年后肌肉变细变硬", RED)
    if st >= 2:
        box(d, F, 560, 470, 1360, 620, "suspect: PAX7+ stem cells", "嫌疑人：PAX7+ 干细胞", MAG)
    if st >= 3:
        T(d, F, (1560, 545), "but they repair well…?", 28, GOLD)
        T(d, F, (1560, 585), "可它们擅长修复…？", 28, GOLD)

def s_refs(st, im, d, F, M):
    T(d, F, (W / 2 - 80, 140), "References", 44, GOLD, font='title'); T(d, F, (W / 2 + 120, 142), "参考文献", 40, GOLD)
    n = len(M.REFS); size = 26 if n <= 14 else 22
    for i, r in enumerate(M.REFS):
        y = 200 + i * (40 if n <= 14 else 33)
        d.text((180, y), f"{i+1:>2}. {r}", font=F('sans', size), fill=(225, 230, 240))

SCENES = {k[2:]: v for k, v in globals().items() if k.startswith('s_')}

def draw(key, step, im, d, F, M, **kw):
    if key == 'section':
        return
    SCENES[key](step, im, d, F, M)

def draw_section(d, F, sec, secz):
    T(d, F, (W / 2, 380), sec, 64, WHITE, font='title')
    T(d, F, (W / 2, 470), secz, 46, GOLD)

def s_photo(st, im, d, F, M):
    """Real micrograph card. M.PHOTOS[st] = (path, caption_en_zh, credit)."""
    from PIL import Image as _I, ImageDraw as _D
    path, cap, credit = M.PHOTOS[st]
    S = im.size[0] // 1920
    ph = _I.open(path).convert('RGB')
    bw, bh = 1180 * S, 470 * S
    r = min(bw / ph.width, bh / ph.height); ph = ph.resize((int(ph.width * r), int(ph.height * r)), _I.LANCZOS)
    x0 = (im.size[0] - ph.width) // 2; y0 = 140 * S + (bh - ph.height) // 2
    d.rounded_rectangle([x0 / S - 10, y0 / S - 10, (x0 + ph.width) / S + 10, (y0 + ph.height) / S + 10], 16, fill=(255, 255, 255, 30), outline=(244, 210, 130, 200), width=2)
    im.paste(ph, (x0, y0))
    T(d, F, (W / 2, (y0 + ph.height) / S + 40), cap, 28, WHITE)
    T(d, F, (W / 2, (y0 + ph.height) / S + 76), credit, 18, GREY)
SCENES['photo'] = s_photo

def s_refs(st, im, d, F, M):
    import prims
    prims.refs_two_col(d, F, M.REFS)
SCENES['refs'] = s_refs
