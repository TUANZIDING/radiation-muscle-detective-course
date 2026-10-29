#!/usr/bin/env python3
"""After the Beam render engine v0.2: supersampled glowing diagrams, animated push-in, crossfades
and scale-in transitions, styled bilingual subtitles. Frames piped to ffmpeg.
usage: render-video-v0.2.py <ep> <datafile> <part> <nparts>   -> /tmp/ep<ep>-part<part>.mp4"""
import sys, os, json, math, importlib.util, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

EP, DATA, PART, NPARTS = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('d', DATA); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
import diagrams as DG
_epf = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"diagrams-ep{EP}-v0.1.py")
if os.path.exists(_epf):
    _s = importlib.util.spec_from_file_location('epd', _epf); _E = importlib.util.module_from_spec(_s); _s.loader.exec_module(_E); DG.SCENES.update(_E.SCENES)
TL = json.load(open(f"{ROOT}/audio/ep{EP}-timeline-v0.1.json"))
FD = f"{ROOT}/assets/fonts"; W, H, FPS, SS = 1920, 1080, 25, 2
TAIL = 10.0

_fc = {}
def F(name, size):
    k = (name, int(size))
    if k not in _fc:
        p = {'sans': 'NotoSansSC.ttf', 'serif': 'NotoSerifSC.ttf', 'title': 'PlayfairDisplay.ttf', 'gar': 'EBGaramond.ttf', 'gari': 'EBGaramond-Italic.ttf'}[name]
        f = ImageFont.truetype(f"{FD}/{p}", int(size))
        if name in ('sans', 'serif'):
            try: f.set_variation_by_axes([460])
            except Exception: pass
        _fc[k] = f
    return _fc[k]
WT = {}

# ---------- supersampling draw proxy ----------
def sc(v):
    if isinstance(v, (int, float)): return v * SS
    if isinstance(v, tuple): return tuple(sc(x) for x in v)
    if isinstance(v, list): return [sc(x) for x in v]
    return v
class SDraw:
    def __init__(self, d): self.d = d
    def _w(self, kw):
        if 'width' in kw: kw['width'] = max(1, int(kw['width'] * SS))
        return kw
    def line(self, xy, **kw): self.d.line(sc(list(xy)), **self._w(kw))
    def ellipse(self, xy, **kw): self.d.ellipse(sc(list(xy)), **self._w(kw))
    def rectangle(self, xy, **kw): self.d.rectangle(sc(list(xy)), **self._w(kw))
    def polygon(self, xy, **kw): self.d.polygon(sc(list(xy)), **self._w(kw))
    def rounded_rectangle(self, xy, r=0, **kw): self.d.rounded_rectangle(sc(list(xy)), r * SS, **self._w(kw))
    def text(self, xy, s, **kw): self.d.text(sc(tuple(xy)), s, **kw)
    def textlength(self, s, font): return self.d.textlength(s, font=font) / SS
def FS(name, size): return F(name, size * SS)

# ---------- background ----------
def make_bg():
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    t = y / H
    base = np.stack([10 + 10 * t, 18 + 12 * t, 34 + 18 * t], -1)
    r = np.sqrt(((x - W * 0.5) / W) ** 2 + ((y - H * 0.38) / H) ** 2)
    glow = np.clip(1 - r * 1.6, 0, 1)[..., None] * np.array([22, 30, 48], np.float32)
    img = base + glow
    vign = np.clip(1 - (r - 0.45) * 0.9, 0.55, 1)[..., None]
    img = img * vign
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    # faint grid + soft bokeh
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for gx in range(0, W, 80): d.line([(gx, 0), (gx, H)], fill=(120, 150, 200, 9))
    for gy in range(0, H, 80): d.line([(0, gy), (W, gy)], fill=(120, 150, 200, 9))
    rnd = np.random.default_rng(7)
    for _ in range(18):
        cx, cy, rr = rnd.integers(0, W), rnd.integers(0, H), rnd.integers(30, 120)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(90, 140, 220, 10))
    ov = ov.filter(ImageFilter.GaussianBlur(6))
    im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
    return np.asarray(im).astype(np.uint16)
BG = make_bg()

# ---------- diagram layer ----------
def diagram_layer(key, step, sec='', secz=''):
    big = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
    d = SDraw(ImageDraw.Draw(big, 'RGBA'))
    if key == 'section': DG.draw_section(d, FS, sec, secz)
    else: DG.draw(key, step, big, d, FS, M)
    lay = big.resize((W, H), Image.LANCZOS)
    glow = lay.filter(ImageFilter.GaussianBlur(9))
    a = np.asarray(glow).copy(); a[..., 3] = (a[..., 3] * 0.55).astype(np.uint8)
    comp = Image.alpha_composite(Image.fromarray(a), lay)
    return np.asarray(comp)

# ---------- overlay (header, tag, ref, subtitles) ----------
TAGC = {'FACT': ((46, 160, 90), 'FACT 事实'), 'ASSOCIATION': ((214, 150, 40), 'ASSOCIATION 关联'),
        'HYPOTHESIS': ((200, 70, 60), 'HYPOTHESIS 假说'), 'BENCH': ((70, 120, 200), 'BENCH NOTE 实验台笔记')}
def wrap_en(d, s, f, mw):
    out, cur = [], ''
    for w in s.split(' '):
        t = (cur + ' ' + w) if cur else w
        if d.textlength(t, font=f) <= mw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out
def wrap_zh(d, s, f, mw):
    out, cur = [], ''
    for ch in s:
        if d.textlength(cur + ch, font=f) <= mw: cur += ch
        elif ch in '，。、；：？！）”' and cur: cur += ch; out.append(cur); cur = ''
        else: out.append(cur); cur = ch
    if cur: out.append(cur)
    return out

def overlay(slot):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im, 'RGBA')
    key = slot.get('v') or 'title'; plain = key in ('title', 'refs', 'section')
    d.text((60, 36), f"AFTER THE BEAM  ·  EPISODE {EP}", font=F('title', 24), fill=(190, 200, 215, 230))
    if slot.get('sec') and not plain:
        d.text((60, 70), f"{slot['sec']}   {slot.get('secz','')}", font=F('sans', 23), fill=(140, 160, 185, 230))
    tag = slot.get('e')
    if tag in TAGC and not plain:
        c, lab = TAGC[tag]; f = F('sans', 23); tw = d.textlength(lab, font=f)
        d.rounded_rectangle([W - 70 - tw - 46, 34, W - 70, 78], 22, fill=c + (230,))
        d.ellipse([W - 70 - tw - 32, 50, W - 70 - tw - 20, 62], fill=(255, 255, 255, 230))
        d.text((W - 70 - tw - 12, 38), lab, font=f, fill=(255, 255, 255))
    ref = slot.get('r')
    if ref and not plain:
        f = F('sans', 21); lab = ref; tw = min(d.textlength(lab, font=f), 1150)
        x0 = W - 70 - tw - 84
        d.rounded_rectangle([x0, 698, W - 70, 742], 12, fill=(14, 24, 40, 200), outline=(244, 210, 130, 150), width=2)
        d.text((x0 + 14, 704), "REF", font=F('sans', 21), fill=(244, 210, 130))
        d.text((x0 + 66, 704), lab, font=f, fill=(225, 230, 240))
    en, zh = slot.get('en'), slot.get('zh')
    if en:
        fe, fz = F('sans', 40), F('sans', 37)
        le = wrap_en(d, en, fe, 1640); lz = wrap_zh(d, zh, fz, 1640)
        hgt = len(le) * 52 + len(lz) * 50 + 14
        y0 = H - 46 - hgt
        widest = max([d.textlength(l, font=fe) for l in le] + [d.textlength(l, font=fz) for l in lz])
        bx0, bx1 = (W - widest) / 2 - 44, (W + widest) / 2 + 44
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([bx0, y0 - 22, bx1, H - 26], 26, fill=(0, 0, 0, 120))
        im = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)), im); d = ImageDraw.Draw(im, 'RGBA')
        d.rounded_rectangle([bx0, y0 - 22, bx1, H - 26], 26, fill=(6, 12, 22, 200), outline=(255, 255, 255, 28), width=1)
        y = y0
        for l in le:
            tw = d.textlength(l, font=fe); d.text(((W - tw) / 2 + 2, y + 2), l, font=fe, fill=(0, 0, 0, 160)); d.text(((W - tw) / 2, y), l, font=fe, fill=(250, 250, 252)); y += 52
        y += 6
        for l in lz:
            tw = d.textlength(l, font=fz); d.text(((W - tw) / 2 + 2, y + 2), l, font=fz, fill=(0, 0, 0, 160)); d.text(((W - tw) / 2, y), l, font=fz, fill=(244, 212, 135)); y += 50
    a = np.asarray(im)
    rows = np.where(a[..., 3].max(1) > 0)[0]
    bands = []
    if len(rows):
        start = prev = rows[0]
        for r in rows[1:]:
            if r != prev + 1: bands.append((start, prev + 1)); start = r
            prev = r
        bands.append((start, prev + 1))
    return a, bands

# ---------- slots ----------
lines = TL['lines']; slots = [(0.0, lines[0]['start'], dict(v='title', step=0))]
for i, L in enumerate(lines):
    nxt = lines[i + 1]['start'] if i + 1 < len(lines) else TL['total'] + TAIL
    if i + 1 < len(lines) and lines[i + 1]['sec'] != L['sec']:
        slots.append((L['start'], L['end'] + 0.3, L))
        slots.append((L['end'] + 0.3, nxt, dict(v='section', step=0, sec=lines[i + 1]['sec'], secz=lines[i + 1]['secz'])))
    else:
        slots.append((L['start'], nxt, L))
def skey(s):
    return ('section', s.get('sec')) if s.get('v') == 'section' else (s.get('v') or 'title', s.get('step', 0))
# state segments
segs = []
for a, b, s in slots:
    k = skey(s)
    if segs and segs[-1]['k'] == k: segs[-1]['b'] = b
    else: segs.append(dict(k=k, a=a, b=b, s=s))
TOTAL = slots[-1][1]

XF = 0.7
def zoom_of(seg, t):
    u = (t - seg['a']) / max(seg['b'] - seg['a'], 1e-3)
    return 1.0 + 0.035 * min(max(u, 0), 1)
def warp(layer, z, cx=W / 2, cy=H * 0.36):
    Mx = np.array([[z, 0, (1 - z) * cx], [0, z, (1 - z) * cy]], np.float32)
    return cv2.warpAffine(layer, Mx, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
def blend(base, rgba, gain=1.0, y0=0, y1=H):
    a = rgba[y0:y1, :, 3:4].astype(np.uint16)
    if gain < 1: a = (a * int(gain * 256)) >> 8
    base[y0:y1] = (base[y0:y1] * (255 - a) + rgba[y0:y1, :, :3].astype(np.uint16) * a) // 255

layer_cache = {}
def get_layer(seg):
    k = seg['k']
    if k not in layer_cache:
        if len(layer_cache) > 4: layer_cache.pop(next(iter(layer_cache)))
        s = seg['s']
        layer_cache[k] = diagram_layer(k[0], k[1], s.get('sec', ''), s.get('secz', ''))
    return layer_cache[k]
ov_cache = {}
def get_ov(i):
    if i not in ov_cache:
        if len(ov_cache) > 3: ov_cache.pop(next(iter(ov_cache)))
        ov_cache[i] = overlay(slots[i][2])
    return ov_cache[i]

nf = int(round(TOTAL * FPS)); per = math.ceil(nf / NPARTS)
f0, f1 = PART * per, min(nf, (PART + 1) * per)
out = f"/tmp/ep{EP}-part{PART}.mp4"
ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-preset", "faster", "-crf", "21", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
si = 0; gi = 0
for fi in range(f0, f1):
    t = fi / FPS
    while si + 1 < len(slots) and slots[si + 1][0] <= t: si += 1
    while gi + 1 < len(segs) and segs[gi + 1]['a'] <= t: gi += 1
    while gi > 0 and segs[gi]['a'] > t: gi -= 1
    frame = BG.copy()
    seg = segs[gi]; dt = t - seg['a']
    if dt < XF and gi > 0:
        u = dt / XF; e = u * u * (3 - 2 * u)
        prev = segs[gi - 1]
        blend(frame, warp(get_layer(prev), zoom_of(prev, seg['a'])), 1 - e)
        newkey = prev['k'][0] != seg['k'][0]
        z = (0.975 + 0.025 * e) if newkey else zoom_of(seg, t)
        blend(frame, warp(get_layer(seg), z), e)
    else:
        blend(frame, warp(get_layer(seg), zoom_of(seg, t)))
    ov, bands = get_ov(si)
    for y0, y1 in bands: blend(frame, ov, 1.0, y0, y1)
    if fi < 12: frame = (frame * fi // 12)
    if fi > nf - 25: frame = (frame * max(nf - fi, 0) // 25)
    ff.stdin.write(frame.astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print("part", PART, "frames", f0, f1, "of", nf, "->", out)
