#!/usr/bin/env python3
"""Clean, soft solo-piano bed (additive synthesis, no noise, no drones, deterministic reverb).
usage: build-piano-v0.1.py <seconds> <out.wav> [seed]"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt

DUR = float(sys.argv[1]); OUT = sys.argv[2]; SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 1
SR = 48000
rng = np.random.default_rng(SEED)
N = int((DUR + 8) * SR)
L = np.zeros(N, np.float32); R = np.zeros(N, np.float32)

def midi(n): return 440.0 * 2 ** ((n - 69) / 12)

cache = {}
def tone(n, vel):
    key = n
    if key not in cache:
        f0 = midi(n); T = 6.0 if n < 60 else 4.5
        t = np.arange(int(T * SR)) / SR
        B = 0.00035
        s = np.zeros_like(t)
        for k in range(1, 9):
            fk = k * f0 * np.sqrt(1 + B * k * k)
            if fk > 6000: break
            amp = 1.0 / k ** 1.6
            dec = (2.8 if n < 60 else 2.0) / (1 + 0.45 * (k - 1))
            s += amp * np.sin(2 * np.pi * fk * t) * np.exp(-t / dec)
        att = np.minimum(1, t / 0.006)
        rel = np.ones_like(t); rel[-int(0.4 * SR):] = np.linspace(1, 0, int(0.4 * SR))
        s = s * att * rel
        cache[key] = (s / np.max(np.abs(s))).astype(np.float32)
    return cache[key] * vel

def place(n, t0, vel, pan=0.0):
    s = tone(n, vel); i = int(t0 * SR)
    if i >= N: return
    j = min(N, i + len(s)); s = s[: j - i]
    L[i:j] += s * (0.5 - pan * 0.35); R[i:j] += s * (0.5 + pan * 0.35)

# A minor / C major, gentle progression: Am F C G | Am Em F G
PROG = [
    (45, [57, 60, 64, 69]), (41, [57, 60, 65, 69]), (48, [55, 60, 64, 67]), (43, [55, 59, 62, 67]),
    (45, [57, 60, 64, 69]), (40, [55, 59, 64, 67]), (41, [57, 60, 65, 69]), (43, [55, 59, 62, 67]),
]
SCALE = [69, 71, 72, 74, 76, 79, 81]
BAR = 6.4  # seconds per chord, slow
t = 1.0; bi = 0
while t < DUR:
    bass, ch = PROG[bi % len(PROG)]
    place(bass, t, 0.30, -0.3)
    # broken chord, sparse
    pattern = [0, 1, 2, 3, 2, 1] if bi % 2 == 0 else [0, 2, 1, 3, 1, 2]
    step = BAR / 6
    for k, p in enumerate(pattern):
        place(ch[p], t + k * step + rng.uniform(0, 0.03), 0.16 + rng.uniform(0, 0.04), 0.1 * (p - 1.5))
    # occasional quiet melody note
    if bi % 2 == 1:
        place(int(rng.choice(SCALE)), t + BAR * 0.5, 0.13, 0.3)
    t += BAR; bi += 1

def reverb(x):
    out = np.zeros_like(x)
    for d, g in [(1557, .82), (1617, .81), (1491, .80), (1422, .79), (1277, .78), (1356, .77)]:
        y = x.copy()
        # feedback comb via block recursion
        for start in range(d, len(y), d):
            seg = y[start - d:start]; y[start:start + d] += g * seg[: len(y[start:start + d])]
        out += y
    out /= 6
    for d, g in [(225, .5), (556, .5)]:
        y = np.zeros_like(out); buf = out.copy()
        y[:d] = -g * buf[:d]
        for start in range(d, len(out), d):
            e = min(len(out), start + d)
            y[start:e] = -g * buf[start:e] + buf[start - d:e - d] + g * y[start - d:e - d]
        out = y
    return out

wetL = reverb(L); wetR = reverb(np.roll(R, 311))
L2 = 0.75 * L + 0.35 * wetL; R2 = 0.75 * R + 0.35 * wetR
hp = butter(4, 90, 'highpass', fs=SR, output='sos'); lp = butter(4, 5500, 'lowpass', fs=SR, output='sos')
L2 = sosfilt(lp, sosfilt(hp, L2)); R2 = sosfilt(lp, sosfilt(hp, R2))
st = np.stack([L2, R2], 1)[: int(DUR * SR)]
fade = int(4 * SR); env = np.ones(len(st)); env[:fade] = np.linspace(0, 1, fade); env[-fade:] = np.linspace(1, 0, fade)
st = st * env[:, None]
st = st / np.max(np.abs(st)) * 0.5
with wave.open(OUT, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
print("piano", DUR, "s ->", OUT)
