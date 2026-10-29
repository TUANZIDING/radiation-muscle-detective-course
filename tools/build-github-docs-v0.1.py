#!/usr/bin/env python3
"""Build episode transcripts + study guides for the GitHub repo.
usage: build-github-docs-v0.1.py  (run from radiation-muscle/) -> github-repo/episodes/"""
import importlib.util, os, json, collections

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(R, 'github-repo', 'episodes')
EPS = [
    (1, 'ep1-data-v0.3.py', 'ep1-the-bullet-and-the-blueprint', 'after-the-beam-ep1-v0.2-small.mp4'),
    (2, 'ep2-data-v0.1.py', 'ep2-the-guardians', 'after-the-beam-ep2-v0.1-small.mp4'),
    (3, 'ep3-data-v0.1.py', 'ep3-the-neighbors-turn', 'after-the-beam-ep3-v0.1-small.mp4'),
    (4, 'ep4-data-v0.1.py', 'ep4-from-bench-to-bedside', 'after-the-beam-ep4-v0.1-small.mp4'),
]
TAG = {'FACT': '🟢 事实 FACT', 'ASSOCIATION': '🟠 关联 ASSOCIATION', 'HYPOTHESIS': '🔴 假说 HYPOTHESIS', 'BENCH': '🔵 实验台笔记 BENCH NOTE', '': ''}

GUIDE = {
1: dict(
 goal="弄清射线如何在 DNA 上留下损伤、细胞有哪几条修复路线、受损细胞的三种命运，以及为什么成熟肌纤维反而“扛得住”。",
 pre=["X 射线主要靠“直接打中”还是“间接作用”损伤 DNA？", "单链断裂和双链断裂，哪个更危险？为什么？", "一根已经融合、不再分裂的肌纤维，会不会因“分裂失败”而死？"],
 qa=[("同样总剂量，单次照射和分次照射效果为什么不同？用什么指标比较？", "分次之间细胞有时间修复；用生物有效剂量（BED）比较不同方案。"),
     ("NHEJ 和 HR 两条修复路线的关键差别？", "NHEJ 随时可用、快但可能留错；HR 需要姐妹染色单体做模板，只在复制后（S/G2）才可用，更精确。"),
     ("γH2AX 灶点在实验里说明什么？30 分钟和 24 小时各看什么？", "标记双链断裂位置；30 分钟看初始断裂，24 小时看残留未修复断裂，需配 53BP1 共定位与盲法计数。"),
     ("受损细胞的三种命运是什么？各用什么标志物判断？", "修复、死亡（凋亡 / 有丝分裂灾难：cleaved caspase-3、TUNEL）、冻结成衰老（SA-β-gal、p21/p16↑、Ki-67↓），需 2–3 个标志物互证。"),
     ("Latella 2004 发现成肌细胞和肌管照射后的差别是什么？", "体外 10 Gy：成肌细胞走 ATM→p53→凋亡；肌管同样出现 γH2AX，但 p53 通路被阻断，不凋亡——分化诱导的放射抵抗。")],
 feynman="用“子弹、蓝图、修理队”向一位本科生解释：为什么射线后肌纤维本身活下来，几年后肌肉却变细变硬——凶手可能在别处。",
 bench="设计一个 γH2AX 时间点实验：写出时间点、阳性/阴性对照、计数方法和至少一个互证标志物。"),
2: dict(
 goal="认识卫星细胞（PAX7+）：谁发现、怎么证明“非它不可”、静息状态的意义、隐藏储备，以及为什么生长中的肌肉更脆弱。",
 pre=["卫星细胞住在肌纤维的哪一层“夹缝”里？", "要证明一个细胞“必需”，实验上该怎么做？", "儿童肌肉和成人肌肉，面对射线时有什么不同？"],
 qa=[("1961 年 Mauro 用什么方法、在什么动物上首次描述卫星细胞？", "电镜，青蛙胫前肌；位于肌膜与基底膜之间。只是提出想法，不是证明。"),
     ("2011 年三项研究如何证明卫星细胞是再生所必需的？", "Pax7 驱动白喉毒素受体等方法特异清除 PAX7+ 细胞，再损伤肌肉，均不能再生。"),
     ("EdU 短脉冲和“长脉冲 + 追踪”各回答什么问题？", "短脉冲看谁正在复制；长脉冲加追踪找保留标记的、很少分裂的细胞。"),
     ("Heslop 2000 的 18 Gy 实验揭示了什么“隐藏储备”？", "照射后普通损伤下再生不明显，但 notexin 重损伤后仍能再生——存在抗辐射的储备细胞。"),
     ("为什么生长期肌肉可能更脆弱？这一条属于哪类证据？", "青春期前许多卫星细胞处于活跃分裂状态，分裂细胞对射线更敏感（Bachman 2020 提出）——标为假说。")],
 feynman="用“守护者住在城墙夹缝里”比喻，讲清楚静息、激活、自我更新三个词，并说明为什么“卫星细胞变多 ≠ 修复成功”。",
 bench="比较 Collao 2023（小鼠 4 周龄，16 Gy）与 Zeng 2022（大鼠，90 Gy）：列出物种、年龄、剂量、时间点四个差异，解释为何结论相反。"),
3: dict(
 goal="理解邻居细胞如何“变脸”：FAP 的两副面孔、巨噬细胞时序、TGF-β 之锁、血管与线粒体，并能画出晚期纤维化的工作模型。",
 pre=["FAP 在正常损伤修复里是帮手还是坏人？", "TNF 和 TGF-β 对 FAP 的作用方向一样吗？", "血管先倒还是干细胞先倒——你会怎样设计实验回答？"],
 qa=[("Joe 2010 与 Uezumi 2010 如何定义 FAP？流式分选的关键门控？", "小鼠 PDGFRα+ / Sca-1+，排除 CD45+（血细胞）与 CD31+（内皮）；人没有 Sca-1。"),
     ("Lemos 2015 中 TNF 与 TGF-β1 怎样决定 FAP 去留？", "急性损伤时巨噬细胞 TNF 促多余 FAP 凋亡；慢性损伤中 TGF-β1 让 FAP 存活并分泌基质 → 瘢痕。"),
     ("照射后（Collao 2023）FAP 发生了什么变化？", "第 56 天：FAP 更少但更趋衰老、更促纤维化，代谢转向糖酵解。"),
     ("单细胞测序推断的“巨噬 TGF-β → FAP”能当因果吗？", "不能。是 mRNA 与预测的配体-受体对话，属关联；需在照射肌肉中阻断 FAP 上的 TGF-β 受体验证。"),
     ("“血管先倒”的证据来自哪里？在肌肉里是什么级别？", "Paris 2001 小鼠肠道（阻断内皮死亡可保护肠干细胞）；在肌肉中仍是证据有限的假说。")],
 feynman="用“邻居变脸”讲完工作模型：射线 → 卫星细胞减少 → 衰老扩散 → TGF-β 让 FAP 产瘢痕 → 毛细血管变稀、线粒体漏电 → 互相加重。每一步说出它的证据标签。",
 bench="写一份 CD68/CD206 巨噬细胞染色方案：说明为什么“M1/M2”是简化、为什么要取多个时间点。"),
4: dict(
 goal="把机制带回病人：人体证据的强弱、研究模型与剂量换算、相互矛盾的线索如何调和、已有干预的边界，以及五个可以做成课题的悬案。",
 pre=["病例系列能告诉我们“有多常见”吗？", "90 Gy 单次和 3 × 8.2 Gy，能直接比较吗？", "如果两篇论文结论相反，第一步该检查什么？"],
 qa=[("Hutcheson 2012 的 29 例病人能说明什么、不能说明什么？", "说明晚期吞咽障碍真实存在且可在多年后进展；转诊样本，不能说明发生率。"),
     ("St. Jude 2021 中颅脑放疗与肌少症的 OR 是多少？证据类型？", "OR 1.84；横断面关联，不能证明因果（包括 mtDNA 拷贝数）。"),
     ("剂量方案不同时怎么比较？举 Hardee 的例子。", "用 BED：4 × 4 Gy 约 BED 37；16 Gy 单次约 100；极端单次大剂量时公式可靠性下降。"),
     ("“卫星细胞激活 vs 耗竭”的矛盾如何调和？", "物种、剂量、年龄、时间点都不同；激活是早期的爆发，耗竭是之后的残局——仍是假说，需同物种、配剂量、多时间点并排实验。"),
     ("PTX + 维生素 E 的证据适用于深部肌肉吗？", "2003 年 24 例乳腺癌 RCT 主要针对浅表（皮肤/皮下）纤维化，样本小；2020 年加氯膦酸治疗神经丛病变无获益——不能外推到深部肌肉。")],
 feynman="用一段“结案陈词”说明：为什么结论不是单一凶手，而是“失去的守护者 + 变脸的邻居 + 断掉的补给线 + 也许来自肿瘤的信使”的合谋。",
 bench="从五个悬案（衰老清除、巨噬时序、血管 vs 干细胞、心脏毒素/BaCl2 再损伤、工程化 EV）中选一个，写一页课题设计：物种、年龄、剂量、时间点、终点（含肌力）。"),
}

def load(f):
    s = importlib.util.spec_from_file_location('m', os.path.join(R, 'script', f))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def dur(ep):
    try:
        return json.load(open(os.path.join(R, 'audio', f'ep{ep}-timeline-v0.1.json')))['total']
    except Exception:
        return None

index = []
for ep, f, slug, video in EPS:
    m = load(f); d = os.path.join(OUT, slug); os.makedirs(d, exist_ok=True)
    tags = collections.Counter(); cur = ''; ref = ''; words = 0
    L = [f"# 第 {ep} 集 · {m.TITLE_ZH} · {m.TITLE_EN}\n",
         f"> 双语逐句文稿，由 `tools/ep{ep}-data-*.py` 自动生成。每段标注证据等级与参考文献。\n",
         "> 🟢 事实 = 有直接实验支持；🟠 关联 = 同时出现，不等于因果；🔴 假说 = 待检验；🔵 实验台笔记 = 动手做实验时的要点。\n"]
    last_tag = None; last_ref = None
    for t in m.D:
        k = t[0]
        if k == 'sec':
            L.append(f"\n## {t[1].strip()} · {t[2].strip()}\n"); last_tag = last_ref = None
        elif k == 'e':
            cur = t[1]
        elif k == 'r':
            ref = t[1]
        elif k == 's':
            tags[cur] += 1; words += len(t[1].split())
            head = []
            if cur != last_tag and cur:
                head.append(f"**{TAG[cur]}**")
            if ref != last_ref and ref:
                head.append(f"<sub>参考：{ref}</sub>")
            if head:
                L.append("\n" + " · ".join(head) + "\n")
            last_tag, last_ref = cur, ref
            L.append(f"- {t[1]}  \n  {t[2]}")
    refs = getattr(m, 'REFS', [])
    if refs:
        L.append("\n## 参考文献 · References\n")
        L += [f"{i}. {r}" for i, r in enumerate(refs, 1)]
    open(os.path.join(d, 'transcript-v0.1.md'), 'w').write("\n".join(L) + "\n")

    g = GUIDE[ep]; sec = [t for t in m.D if t[0] == 'sec']
    S = [f"# 第 {ep} 集学习单 · {m.TITLE_ZH} · {m.TITLE_EN}\n",
         f"**本集目标**：{g['goal']}\n",
         "## 学习节奏（约 60 分钟）\n",
         "| 步骤 | 时间 | 做什么 |", "| --- | --- | --- |",
         "| ① 预测 | 5 分钟 | 不看视频，先写下下面三个问题的答案（猜错没关系，猜过才记得牢） |",
         "| ② 观看 | 20 分钟 | 看视频；遇到 🟠/🔴 标签时暂停，问自己“这条证据为什么不是事实？” |",
         "| ③ 闭卷回忆 | 10 分钟 | 合上一切材料，回答“提取练习”五题，再展开答案对照 |",
         "| ④ 费曼输出 | 10 分钟 | 用自己的话讲一遍（可录音），卡住的地方回到文稿 |",
         "| ⑤ 实验台任务 | 15 分钟 | 完成一个小设计任务，把机制变成可以做的实验 |",
         "| ⑥ 间隔复习 | 1 天 / 3 天 / 7 天后 | 只重做提取练习，不重看视频 |\n",
         "## 本集结构\n"] + [f"- {t[1].strip()} · {t[2].strip()}" for t in sec] + [
         "\n## ① 观看前预测\n"] + [f"{i}. {q}" for i, q in enumerate(g['pre'], 1)] + [
         "\n## ③ 提取练习（先答再看）\n"]
    for i, (q, a) in enumerate(g['qa'], 1):
        S.append(f"**{i}. {q}**\n\n<details><summary>参考答案</summary>\n\n{a}\n\n</details>\n")
    S += ["## ④ 费曼一段话\n", g['feynman'] + "\n",
          "## ⑤ 实验台任务\n", g['bench'] + "\n",
          "## 本集证据构成\n",
          "| 标签 | 句数 |", "| --- | --- |"] + [f"| {TAG[k]} | {v} |" for k, v in tags.items() if k] + [
          "\n## 相关文件\n",
          f"- [双语逐句文稿](transcript-v0.1.md)",
          f"- [双语字幕 SRT](../../subtitles/ep{ep}-bilingual-v0.1.srt)",
          f"- [观看本集视频（720p）](../../videos/{video})"]
    open(os.path.join(d, 'study-guide-v0.1.md'), 'w').write("\n".join(S) + "\n")
    index.append((ep, m.TITLE_EN, m.TITLE_ZH, slug, dur(ep), words, dict(tags), len(refs)))
    print(ep, m.TITLE_EN, words, dict(tags), len(refs))
json.dump(index, open(os.path.join(OUT, 'index-v0.1.json'), 'w'), ensure_ascii=False, indent=1)
