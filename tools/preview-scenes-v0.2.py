#!/usr/bin/env python3
"""Preview every (key, step) of an episode as a contact sheet, rendered exactly like the v0.2 engine diagram layer.
usage: preview-scenes-v0.2.py <ep> <datafile> [key ...]  -> /tmp/preview-ep<ep>/<key>-<step>.png + sheet.png"""
import sys, os, importlib.util
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
EP, DATA = sys.argv[1], sys.argv[2]; only = sys.argv[3:]
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
spec = importlib.util.spec_from_file_location('d', DATA); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
import diagrams as DG
epf = f"{HERE}/diagrams-ep{EP}-v0.1.py"
if os.path.exists(epf):
    s2 = importlib.util.spec_from_file_location('epd', epf); E = importlib.util.module_from_spec(s2); s2.loader.exec_module(E); DG.SCENES.update(E.SCENES)
W, H, SS = 1920, 1080, 2; FD = f"{ROOT}/assets/fonts"; _fc = {}
def F(name, size):
    k = (name, int(size))
    if k not in _fc:
        p = {'sans': 'NotoSansSC.ttf', 'serif': 'NotoSerifSC.ttf', 'title': 'PlayfairDisplay.ttf', 'gar': 'EBGaramond.ttf', 'gari': 'EBGaramond-Italic.ttf'}[name]
        f = ImageFont.truetype(f"{FD}/{p}", int(size))
        if name in ('sans', 'serif'): f.set_variation_by_axes([460])
        _fc[k] = f
    return _fc[k]
def sc(v):
    if isinstance(v, (int, float)): return v * SS
    if isinstance(v, (tuple, list)): return type(v)(sc(x) for x in v)
    return v
class SDraw:
    def __init__(s, d): s.d = d
    def _w(s, kw):
        if 'width' in kw: kw['width'] = max(1, int(kw['width'] * SS))
        return kw
    def line(s, xy, **kw): s.d.line(sc(list(xy)), **s._w(kw))
    def ellipse(s, xy, **kw): s.d.ellipse(sc(list(xy)), **s._w(kw))
    def rectangle(s, xy, **kw): s.d.rectangle(sc(list(xy)), **s._w(kw))
    def polygon(s, xy, **kw): s.d.polygon(sc(list(xy)), **s._w(kw))
    def rounded_rectangle(s, xy, r=0, **kw): s.d.rounded_rectangle(sc(list(xy)), r * SS, **s._w(kw))
    def text(s, xy, t, **kw): s.d.text(sc(tuple(xy)), t, **kw)
    def textlength(s, t, font): return s.d.textlength(t, font=font) / SS
def FS(n, s): return F(n, s * SS)
keys = []
for x in M.D:
    if x[0] == 'v' and (x[1], x[2]) not in keys and (not only or x[1] in only): keys.append((x[1], x[2]))
out = f"/tmp/preview-ep{EP}"; os.makedirs(out, exist_ok=True); thumbs = []
for k, st in keys:
    big = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0)); d = SDraw(ImageDraw.Draw(big, 'RGBA'))
    try: DG.draw(k, st, big, d, FS, M)
    except Exception as e: print('ERROR', k, st, repr(e)); continue
    lay = big.resize((W, H), Image.LANCZOS)
    bg = Image.new('RGBA', (W, H), (16, 26, 46, 255))
    g = lay.filter(ImageFilter.GaussianBlur(9)); a = np.asarray(g).copy(); a[..., 3] = (a[..., 3] * .55).astype(np.uint8)
    im = Image.alpha_composite(Image.alpha_composite(bg, Image.fromarray(a)), lay).convert('RGB')
    dd = ImageDraw.Draw(im); dd.rectangle([0, 760, W, H], fill=(40, 20, 20)); dd.text((60, 900), f"{k} step {st}  (subtitle zone)", font=F('sans', 40), fill=(200, 200, 200))
    safe = k.replace(':', '_').replace(' ', '-')[:40]
    im.save(f"{out}/{safe}-{st}.png"); thumbs.append(im.resize((480, 270)))
cols = 4; rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new('RGB', (cols * 480, max(1, rows) * 270))
for i, t in enumerate(thumbs): sheet.paste(t, ((i % cols) * 480, (i // cols) * 270))
sheet.save(f"{out}/sheet.png"); print(len(thumbs), "scenes ->", out)
