#!/usr/bin/env python3
"""TTS each subtitle line, assemble narration wav with pauses, write timeline json.
usage: build-audio-v0.1.py <ep> <datafile>"""
import hashlib, sys, os, json, asyncio, subprocess, importlib.util, wave
import numpy as np
import edge_tts

EP = sys.argv[1]; DATA = sys.argv[2]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('d', DATA); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
SEG = f"{ROOT}/audio/ep{EP}-seg"; os.makedirs(SEG, exist_ok=True)
VOICE, RATE, PITCH = "en-US-ChristopherNeural", "-12%", "-4Hz"
SR = 48000
GAP, SEC_GAP, LEAD = 0.65, 3.0, 1.5

lines = [x for x in m.D if x[0] == 's']

async def one(i, txt, sem):
    out = f"{SEG}/{hashlib.md5(txt.encode()).hexdigest()[:12]}.mp3"
    if os.path.exists(out) and os.path.getsize(out) > 1000: return
    async with sem:
        for a in range(4):
            try:
                await edge_tts.Communicate(txt, VOICE, rate=RATE, pitch=PITCH).save(out); return
            except Exception as e:
                await asyncio.sleep(2 + a * 3)
        raise RuntimeError(f"tts fail {i}")

async def main():
    sem = asyncio.Semaphore(6)
    await asyncio.gather(*[one(i, l[1], sem) for i, l in enumerate(lines)])
asyncio.run(main())

def load(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True)
    a = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768
    # trim leading/trailing silence
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz): a = a[max(0, nz[0] - 480): nz[-1] + 2400]
    return a

parts = [np.zeros(int(LEAD * SR), np.float32)]; t = LEAD; tl = []; li = 0
state = dict(v=None, step=0, r='', e='', sec=None, secz=None)
first = True
for x in m.D:
    k = x[0]
    if k == 'sec':
        if not first:
            parts.append(np.zeros(int(SEC_GAP * SR), np.float32)); t += SEC_GAP
        state['sec'], state['secz'] = x[1], x[2]; first = False
    elif k == 'v': state['v'], state['step'] = x[1], x[2]
    elif k == 'r': state['r'] = x[1]
    elif k == 'e': state['e'] = x[1]
    elif k == 's':
        a = load(f"{SEG}/{hashlib.md5(x[1].encode()).hexdigest()[:12]}.mp3"); d = len(a) / SR
        tl.append(dict(i=li, start=round(t, 3), end=round(t + d, 3), en=x[1], zh=x[2], **state))
        parts.append(a); t += d
        parts.append(np.zeros(int(GAP * SR), np.float32)); t += GAP
        li += 1
parts.append(np.zeros(int(3.0 * SR), np.float32)); t += 3.0
audio = np.concatenate(parts)
os.makedirs(f"{ROOT}/audio", exist_ok=True)
with wave.open(f"{ROOT}/audio/ep{EP}-narration-v0.1.wav", 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes())
json.dump(dict(total=round(t, 3), lines=tl), open(f"{ROOT}/audio/ep{EP}-timeline-v0.1.json", 'w'), ensure_ascii=False, indent=1)
print("total", round(t, 1), "s", len(tl), "lines")
