#!/usr/bin/env python3
"""usage: make-srt-v0.1.py <ep> -> subs/ep<ep>-bilingual-v0.1.srt (EN line, ZH line)"""
import json, os, sys
EP = sys.argv[1]; R = os.environ.get('RM_ROOT', '.')
L = json.load(open(f'{R}/audio/ep{EP}-timeline-v0.1.json'))['lines']
def ts(t): h, m = int(t // 3600), int(t % 3600 // 60); s = t % 60; return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"
out = []
for i, l in enumerate(L):
    end = l['end'] + 0.2
    if i + 1 < len(L): end = min(end, L[i + 1]['start'] - 0.05)
    out.append(f"{i+1}\n{ts(l['start'])} --> {ts(end)}\n{l['en']}\n{l['zh']}\n")
open(f'{R}/subs/ep{EP}-bilingual-v0.1.srt', 'w').write('\n'.join(out)); print(len(L), 'cues')
