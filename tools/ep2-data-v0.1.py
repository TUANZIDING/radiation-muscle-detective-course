# Episode 2 data v0.1: "The Guardians" (satellite cells). Same tuple format as ep1-data-v0.2.py.
# ('sec', en_title, zh_title)   section header (adds pause, sets label)
# ('v', key, step)              visual state
# ('r', 'ref1; ref2')           reference card for following lines
# ('e', 'FACT'|'ASSOCIATION'|'HYPOTHESIS'|'BENCH'|'')  evidence tag
# ('s', en, zh)                 one narrated subtitle line
# VIS (end of file): illustrator brief for every visual key, step by step.
EP = 2
TITLE_EN = "The Guardians"
TITLE_ZH = "守护者"

D = [
('sec', "Cold open", "序幕"),
('v', 'recap', 0), ('r', ''), ('e', ''),
('s', "My friends, when we parted last time, I left you standing beside a muscle fiber that refused to die.", "朋友们，上次分别时，我把你们留在一根不肯死去的肌纤维旁边。"),
('s', "The beam had struck it. The alarm had sounded. And the fiber, armored by its own maturity, survived.", "射线击中了它，警报拉响了。而这根纤维，靠着自身成熟带来的盔甲，活了下来。"),
('v', 'recap', 1),
('s', "Yet years later, the muscle still grew thin and stiff.", "可是多年以后，这块肌肉还是变细了、变硬了。"),
('s', "So we turned our suspicion to the small cells that rebuild muscle, the ones that wear the PAX7 badge.", "于是我们把怀疑转向那些负责重建肌肉、佩戴 PAX7 徽章的小细胞。"),
('v', 'recap', 2),
('s', "And we found a puzzle. Those resting cells repair broken DNA faster and more accurately than their own offspring.", "我们还发现了一道谜题：这些静息的细胞修复断裂 DNA，比它们自己的子代更快、更准。"),
('s', "If they are such good mechanics, how could radiation empty their ranks?", "既然它们是这么好的修理工，射线又怎么能让它们的队伍空掉？"),
('v', 'title', 0),
('s', "Tonight we meet those cells face to face. Scientists call them satellite cells. I will call them the guardians.", "今晚，我们和这些细胞面对面。科学家叫它们卫星细胞，我叫它们守护者。"),
('s', "We will ask who found them, how we know they matter, and where they hide when there is no work to do.", "我们要问：是谁发现了它们？我们凭什么知道它们重要？没活干的时候，它们藏在哪里？"),
('s', "And before the evening is over, I will offer you an answer to our puzzle, piece by piece, each piece honestly labeled.", "今晚结束之前，我会给出这道谜题的答案，一块一块地拼，每一块都老实贴上标签。"),

('sec', "1  The cell on the edge", "一  边缘上的细胞"),
('v', 'em', 0), ('r', 'Mauro 1961 J Biophys Biochem Cytol'), ('e', 'FACT'),
('s', "Our story begins in 1961, at the Rockefeller Institute in New York.", "故事从 1961 年开始，地点是纽约的洛克菲勒研究所。"),
('s', "A scientist named Alexander Mauro was studying the outer edge of muscle fibers with an electron microscope.", "一位名叫 Alexander Mauro 的科学家，正用电子显微镜研究肌纤维的外缘。"),
('s', "His samples came from the leg of a frog, a muscle called the tibialis anticus.", "他的样本来自青蛙的腿，一块叫胫前肌的肌肉。"),
('v', 'em', 1),
('s', "Look closely at the border of the fiber. There, a small cell lies flattened against it.", "仔细看纤维的边缘：那里有一个小细胞，扁扁地贴在上面。"),
('s', "It has a large nucleus and very little cytoplasm, as if it had packed only what it truly needed.", "它的细胞核很大，细胞质却很少，好像只带上了真正必需的行李。"),
('v', 'niche', 0),
('s', "What struck Mauro most was where it sat.", "最让 Mauro 惊讶的，是它待的位置。"),
('s', "Every muscle fiber is wrapped in a thin sheet of protein, a kind of sleeve, called the basement membrane, or basal lamina.", "每根肌纤维外面都包着一层薄薄的蛋白膜，像一只袖套，叫基底膜，也叫基板。"),
('v', 'niche', 1),
('s', "Beneath that sleeve lies the fiber's own cell membrane.", "袖套下面，是纤维自己的细胞膜。"),
('s', "Mauro's cell was wedged between the two: inside the sleeve, yet outside the fiber.", "Mauro 看到的细胞，就楔在这两层之间：在袖套里面，却在纤维外面。"),
('v', 'niche', 2),
('s', "It was not part of the fiber, yet it shared the fiber's coat, like a sentry standing just inside the castle wall.", "它不属于纤维，却和纤维穿同一件外衣，就像一名哨兵站在城墙内侧。"),
('s', "Mauro chose to call these satellite cells, for the way they clung to the fiber.", "因为它们紧紧依附着纤维，Mauro 给它们取名为卫星细胞。"),
('s', "His paper was barely three pages long. He offered an idea, not a proof.", "他的论文只有短短三页。他提出的是一个想法，而不是证明。"),
('s', "He wrote that these cells might be pertinent to what he called the vexing problem of skeletal muscle regeneration.", "他写道，这些细胞也许和他所说的“骨骼肌再生这个恼人的难题”有关。"),
('r', 'Mauro 1961; Relaix & Zammit 2012 Development'),
('s', "Perhaps, as later reviewers summed it up, they were dormant myoblasts, held in reserve until the muscle needed repair.", "后来的综述者这样概括：也许它们是休眠的成肌细胞，被留作后备，等肌肉需要修复时再出场。"),
('v', 'niche', 3),
('s', "Today we recognize them by a protein in their nucleus called PAX7, a master switch that controls other genes.", "今天，我们靠它们细胞核里一种叫 PAX7 的蛋白认出它们，它是一个调控其他基因的总开关。"),
('s', "It is the badge we met in the last episode, and it is how nearly every study tonight finds and counts them.", "这就是上一集我们见过的那枚徽章；今晚几乎每一项研究，都是靠它来找到并清点它们的。"),
('v', 'bench', 0), ('r', 'Relaix & Zammit 2012; Lepper 2011'), ('e', 'BENCH'),
('s', "A note from the bench. When you count satellite cells in a muscle section, PAX7 alone is not quite enough.", "一段实验台笔记：在肌肉切片上数卫星细胞时，光靠 PAX7 还不太够。"),
('s', "Stain laminin as well, which outlines the basal lamina, and a DNA dye such as DAPI, which marks every nucleus.", "还要同时染层粘连蛋白，它能勾出基底膜的轮廓；再加一种 DNA 染料，比如 DAPI，标出所有细胞核。"),
('s', "A true satellite cell is a PAX7-positive nucleus sitting under the laminin sleeve, right where Mauro found it.", "真正的卫星细胞，是一个 PAX7 阳性的细胞核，坐在层粘连蛋白袖套之下，正是 Mauro 发现它的位置。"),
('s', "Count them per hundred fibers, or per square millimeter, across many fields, and stay blind to which leg is which.", "按每一百根纤维或每平方毫米来计数，多数几个视野，并且不要知道哪条腿是哪组。"),

('sec', "2  Proof of necessity", "二  必要性的证明"),
('v', 'ablation', 0), ('r', 'Relaix & Zammit 2012 Development; Lepper 2011 Development'), ('e', 'FACT'),
('s', "For fifty years, the satellite cell was the leading suspect in muscle repair. But a suspect is not yet a proven culprit.", "五十年来，卫星细胞一直是肌肉修复的头号嫌疑人。但嫌疑人还不等于被证实的那个人。"),
('s', "Over those years, cells from other origins were also reported to join muscle fibers after they were transplanted.", "这些年里，也有报道说，来自其他来源的细胞移植后同样能加入肌纤维。"),
('s', "So a fair question lingered. Were satellite cells truly required, or were they one helper among many?", "于是一个合理的问题一直悬着：卫星细胞真的不可缺少吗？还是只是众多帮手之一？"),
('v', 'ablation', 1), ('r', 'Lepper 2011; Sambasivan 2011; Murphy 2011 Development'),
('s', "There is only one honest way to settle such a question. Remove the suspect, and see whether the work still gets done.", "要回答这种问题，只有一个老实办法：把嫌疑人拿走，看看活儿还能不能干成。"),
('s', "In September 2011, three independent teams did exactly that, and their papers appeared side by side in the same issue of the journal Development.", "2011 年 9 月，三个独立团队正是这么做的，他们的论文并排登在同一期《Development》上。"),
('v', 'three', 0),
('s', "Christoph Lepper, Terence Partridge and Chen-Ming Fan engineered mice in which cells expressing Pax7 could be genetically eliminated.", "Christoph Lepper、Terence Partridge 和 Chen-Ming Fan 构建了一种小鼠，可以从基因层面清除表达 Pax7 的细胞。"),
('s', "Then they injured the tibialis anterior muscle.", "然后，他们损伤了小鼠的胫骨前肌。"),
('s', "Without Pax7-positive cells, regenerative muscle formation was completely blocked.", "没有了 Pax7 阳性细胞，肌肉的再生性生成被完全阻断。"),
('s', "The same was true when they transplanted a small muscle into another mouse and asked it to rebuild itself.", "他们把一小块肌肉移植到另一只小鼠体内、让它自我重建时，结果也一样。"),
('v', 'three', 1),
('s', "In Paris, Ramkumar Sambasivan, Shahragim Tajbakhsh and their colleagues used a different weapon.", "在巴黎，Ramkumar Sambasivan、Shahragim Tajbakhsh 和同事用了另一种武器。"),
('s', "They placed a human receptor for diphtheria toxin under control of the Pax7 gene, so an injection of toxin struck only the satellite cells.", "他们把人的白喉毒素受体放到 Pax7 基因的控制之下，这样注射毒素时，只有卫星细胞会被击中。"),
('s', "The muscle lost tissue and failed to regenerate, and it filled with inflammatory cells and fat.", "肌肉组织明显丢失、无法再生，还被炎症细胞和脂肪占满。"),
('s', "No other cell type stepped in. But when they transplanted adult Pax7-positive satellite cells, regeneration was rescued.", "没有别的细胞类型顶上来。可当他们移植进成年的 Pax7 阳性卫星细胞时，再生就被挽救了。"),
('v', 'three', 2),
('s', "In Utah, Malea Murphy, Gabrielle Kardon and their colleagues removed satellite cells with yet another genetic switch.", "在犹他，Malea Murphy、Gabrielle Kardon 和同事用又一种基因开关清除了卫星细胞。"),
('s', "Regenerated muscle was lost entirely, and connective tissue increased dramatically.", "再生的肌肉完全消失，结缔组织则急剧增多。"),
('s', "But they also removed a second cell, the connective tissue fibroblast, and repair suffered then, too.", "他们还清除了另一种细胞，也就是结缔组织成纤维细胞，结果修复同样受损。"),
('s', "Without fibroblasts, satellite cells differentiated too early, their early pool was depleted, and the new fibers came out smaller.", "没有成纤维细胞，卫星细胞分化得太早，早期细胞池被耗尽，新长出的纤维也更细。"),
('v', 'ablation', 2),
('s', "Three teams, three methods, one verdict. After acute injury, there is no muscle regeneration without satellite cells.", "三个团队，三种方法，一个判决：急性损伤之后，没有卫星细胞，就没有肌肉再生。"),
('s', "A review the following year put it plainly: skeletal muscle does not regenerate without them.", "第二年的一篇综述说得很直白：没有它们，骨骼肌不会再生。"),
('v', 'ablation', 3),
('s', "But notice the detail in those papers. The guardian needs its neighbors, and when the guardian is gone, scar and fat move in.", "但请留意这些论文里的细节：守护者需要邻居；而守护者一旦不在，瘢痕和脂肪就会搬进来。"),
('s', "File that away. It will matter a great deal in the next episode.", "把这一点存档。下一集，它会非常重要。"),
('v', 'bench', 1), ('r', 'Murphy 2011; Lepper 2011'), ('e', 'BENCH'),
('s', "A note from the bench, because these switches are tools you may soon use yourself.", "一段实验台笔记，因为这些开关很可能就是你马上要用的工具。"),
('s', "A common design pairs Pax7-CreER with a gene in the Rosa26 locus that stays silent until Cre removes a stop signal in front of it.", "常见的设计是把 Pax7-CreER 和放在 Rosa26 位点上的一个基因配对，这个基因一直沉默，直到 Cre 剪掉它前面的终止信号。"),
('s', "Cre is a pair of molecular scissors. In CreER, the scissors stay locked outside the nucleus until the drug tamoxifen opens the door.", "Cre 是一把分子剪刀。在 CreER 里，剪刀被锁在细胞核外，直到他莫昔芬这种药把门打开。"),
('s', "If the silent gene is a toxin, such as diphtheria toxin A, the Pax7 cells die. If it is a fluorescent reporter, they and all their descendants glow.", "如果沉默的基因是毒素，比如白喉毒素 A，Pax7 细胞就会死亡；如果是荧光报告基因，它们和所有后代都会发光。"),
('s', "One switch, two experiments. Ablation asks whether a cell is needed. Tracing asks what it becomes.", "一个开关，两种实验：清除，问的是这个细胞是否必需；示踪，问的是它会变成什么。"),

('sec', "3  Quiescence is not sleep", "三  静止不是沉睡"),
('v', 'cycle', 0), ('r', 'Cheung & Rando 2013 Nat Rev Mol Cell Biol'), ('e', 'FACT'),
('s', "Now, what do the guardians do when nothing is wrong?", "那么，天下太平的时候，守护者在做什么？"),
('s', "In an adult muscle at rest, most satellite cells are not dividing. Biologists call this state quiescence.", "在静息的成年肌肉里，大多数卫星细胞并不分裂。生物学家把这种状态叫做静止。"),
('s', "For a long time it was pictured as dormancy, a cell asleep in its bunk, doing as little as possible.", "很长一段时间里，人们把它想象成休眠：细胞躺在铺位上睡觉，尽量什么都不做。"),
('v', 'quiescence', 0),
('s', "In 2013, Tom Cheung and Thomas Rando reviewed the evidence for a different picture.", "2013 年，Tom Cheung 和 Thomas Rando 综述了支持另一幅图景的证据。"),
('s', "Quiescence, they argued, is actively maintained. Signaling pathways and gene controls hold the cell in a poised state.", "他们认为，静止是被主动维持的：信号通路和基因调控把细胞保持在一种蓄势待发的状态。"),
('v', 'quiescence', 1),
('s', "Think of a fire crew at the station. The engine is not racing, but the boots are standing by the door.", "想想消防站里的消防队：发动机没在轰鸣，但靴子就摆在门口。"),
('s', "That readiness allows rapid activation when the alarm comes, and the state can be reversed.", "这种准备就绪，让警报一响就能迅速激活；而且这种状态是可逆的。"),
('v', 'cycle', 1),
('s', "When the muscle is injured, the guardian wakes. It leaves quiescence and begins to divide.", "肌肉一受伤，守护者就醒来，离开静止状态，开始分裂。"),
('v', 'cycle', 2),
('s', "Its daughters multiply into a crowd of myoblasts, which fuse to repair damaged fibers or to build new ones.", "它的子代繁殖成一大群成肌细胞，它们融合起来，修补受损的纤维，或者造出新的纤维。"),
('v', 'cycle', 3),
('s', "And here is what makes it a stem cell. Some daughters do not fuse. They return to the niche and go quiet again.", "而让它称得上干细胞的，是这一点：有些子代并不融合，而是回到微环境里，重新安静下来。"),
('s', "This is called self-renewal. Every repair must leave behind guardians for the next one.", "这叫自我更新。每一次修复，都必须为下一次留下守护者。"),
('v', 'paradox', 0), ('r', 'Vahidi Ferdousi 2014 Stem Cell Res; Caiozzo 2010 Radiat Res'), ('e', 'FACT'),
('s', "Now hold that cycle up beside our puzzle.", "现在，把这个循环和我们的谜题放在一起看。"),
('s', "Vahidi Ferdousi and her colleagues showed that quiescent satellite cells repair radiation breaks well, using the welder's tool, DNA-PKcs.", "Vahidi Ferdousi 和同事证明，静止的卫星细胞能很好地修复辐射造成的断裂，用的是焊工的工具 DNA-PKcs。"),
('v', 'paradox', 1),
('s', "But in 2010, Vincent Caiozzo, Charles Limoli and their colleagues irradiated satellite cells growing in culture, where they divide.", "可是在 2010 年，Vincent Caiozzo、Charles Limoli 和同事照射了在培养皿里生长、正在分裂的卫星细胞。"),
('s', "Doses of five grays or more reduced their numbers by at least seventy percent.", "5 Gy 及以上的剂量，让细胞数量减少了至少七成。"),
('s', "Part of the loss came from apoptosis, and part from cells stalling in the cell cycle.", "一部分损失来自凋亡，一部分来自细胞周期停滞。"),
('s', "Radiation also kept reactive oxygen and nitrogen species high, while nitric oxide, which these cells need to proliferate, fell.", "辐射还让活性氧和活性氮持续升高，而这些细胞增殖所需要的一氧化氮却下降了。"),
('v', 'paradox', 2),
('s', "So the same family of cells looks sturdy at rest and fragile when it is busy dividing.", "所以，同一家族的细胞，静息时看起来很结实，忙着分裂时却很脆弱。"),
('s', "Keep that contrast in mind. It is the hinge on which our answer will turn.", "请记住这个对比。我们的答案，就要绕着这根门轴转。"),
('v', 'bench', 2), ('r', 'Cheung & Rando 2013'), ('e', 'BENCH'),
('s', "A note from the bench. How do you know whether a cell has been dividing?", "一段实验台笔记：怎么知道一个细胞有没有分裂过？"),
('s', "Give the animal EdU, a modified building block of DNA. Any cell that copies its DNA while EdU is present takes it in.", "给动物注射 EdU，一种经过修饰的 DNA 原料。凡是在 EdU 存在期间复制 DNA 的细胞，都会把它掺进去。"),
('s', "A quick chemical reaction then makes the EdU glow, so a short pulse shows who was copying DNA during that window.", "随后一个简便的化学反应让 EdU 发光，所以短时间给药，就能看出谁在那段时间里复制了 DNA。"),
('s', "Give it longer, then wait for weeks. Cells that divide dilute the label, so the ones still glowing are called label-retaining cells.", "给药时间长一些，再等上几周。分裂的细胞会把标记稀释掉，所以仍在发光的，叫做标记滞留细胞。"),
('s', "Use the lowest dose that works, since EdU sits inside the DNA itself, and always co-stain PAX7 to know whose nucleus you are counting.", "用能起效的最低剂量，因为 EdU 是嵌在 DNA 里面的；并且一定要同时染 PAX7，才知道你数的是谁的细胞核。"),

('sec', "4  The hidden reserve", "四  隐藏的储备"),
('v', 'heslop', 0), ('r', 'Heslop 2000 J Cell Sci'), ('e', 'FACT'),
('s', "Now we bring radiation into the room.", "现在，让射线登场。"),
('s', "In 2000, Heslop, Jennifer Morgan and Terence Partridge irradiated mouse muscle with eighteen grays.", "2000 年，Heslop、Jennifer Morgan 和 Terence Partridge 用 18 Gy 照射了小鼠肌肉。"),
('s', "They studied normal mice, and also mdx mice, a model of Duchenne muscular dystrophy.", "他们研究了正常小鼠，也研究了 mdx 小鼠，一种杜氏肌营养不良的模型。"),
('v', 'heslop', 1),
('s', "After irradiation alone, neither normal nor dystrophic muscle regenerated to any significant extent.", "单纯照射之后，无论正常肌肉还是营养不良的肌肉，都没有明显再生。"),
('s', "Single fibers lifted out of that muscle released very few precursor cells, and those barely divided.", "从这些肌肉里取出的单根纤维，只释放出极少的前体细胞，而且它们几乎不分裂。"),
('v', 'heslop', 2),
('s', "Then the team injected notexin, a snake venom toxin that severely damages muscle.", "接着，团队注射了 notexin，一种严重破坏肌肉的蛇毒毒素。"),
('s', "To their surprise, the irradiated muscles regenerated.", "出乎他们意料，受过照射的肌肉再生了。"),
('s', "Some single fibers now produced rapidly dividing precursor cells, more often from normal muscle than from dystrophic muscle.", "有些单根纤维这时能产生快速分裂的前体细胞，而且正常肌肉比营养不良肌肉更常见。"),
('v', 'heslop', 3),
('s', "Even after twenty-five grays, notexin evoked some new muscle, though no dividing precursor cells remained on the fibers.", "即使照射 25 Gy，notexin 仍能唤起一些新肌肉，只是纤维上已经没有能分裂的前体细胞了。"),
('s', "Their conclusion: muscle holds distinct populations of myogenic cells. Most are radiation sensitive, but some survive and wait for an extreme emergency.", "他们的结论是：肌肉里有几类功能不同的成肌细胞。大多数对辐射敏感，但有一些能活下来，等待极端的紧急情况。"),
('s', "And in dystrophic muscle, that hidden reserve was markedly diminished, as if a long war had already spent it.", "而在营养不良的肌肉里，这支隐藏的储备明显减少了，好像一场漫长的战争早已把它耗光。"),
('v', 'transplant', 0), ('r', 'Wernig 2000 J Physiol; Boldrin 2012 Stem Cells'),
('s', "Scientists soon turned this weakness into a tool.", "科学家很快把这个弱点变成了工具。"),
('s', "In 2000, Anton Wernig and his colleagues gave sixteen grays of X-rays to the mouse soleus before injecting donor myoblasts.", "2000 年，Anton Wernig 和同事先用 16 Gy 的 X 射线照射小鼠比目鱼肌，再注射供体成肌细胞。"),
('v', 'transplant', 1),
('s', "Irradiation alone left those muscles about eighteen percent lighter and weaker. The donor cells abolished those deficits.", "单纯照射让这些肌肉的重量和力量都下降了约 18%，而供体细胞消除了这些缺陷。"),
('s', "The authors concluded that irradiation is an effective way to prepare a muscle for transplanted cells.", "作者的结论是：照射是为细胞移植预先处理肌肉的有效办法。"),
('v', 'transplant', 2),
('s', "In 2012, Luisa Boldrin, Jennifer Morgan and their colleagues sharpened the rule.", "2012 年，Luisa Boldrin、Jennifer Morgan 和同事把这条规律说得更精确。"),
('s', "Donor satellite cells engrafted best when the host's own satellite cells were incapacitated, but the niche itself was preserved.", "当宿主自己的卫星细胞失去能力、而微环境本身被保留时，供体卫星细胞植入得最好。"),
('s', "If the niche was destroyed, or still filled with competent host cells, engraftment was poor. The empty house must still be standing.", "如果微环境被毁，或者仍被有能力的宿主细胞占着，植入就很差。空房子，得是还立着的房子。"),
('v', 'reserve', 0), ('r', 'Scaramozza 2019 Cell Stem Cell'), ('e', 'FACT'),
('s', "But who exactly were Heslop's survivors? For nearly twenty years, they had no name.", "可是，Heslop 看到的幸存者究竟是谁？将近二十年里，它们都没有名字。"),
('s', "In 2019, Annarita Scaramozza, Andrew Brack and their colleagues used lineage tracing to look.", "2019 年，Annarita Scaramozza、Andrew Brack 和同事用谱系示踪去找它们。"),
('v', 'reserve', 1),
('s', "A genetic switch called Mx1-Cre permanently marked a small subset of Pax7-positive satellite cells.", "一个叫 Mx1-Cre 的基因开关，永久标记了 Pax7 阳性卫星细胞中的一小群。"),
('s', "These marked cells were enriched for a related gene, Pax3, and carried lower levels of reactive oxygen species.", "这些被标记的细胞富含一个近亲基因 Pax3，体内活性氧水平也更低。"),
('v', 'reserve', 2),
('s', "In ordinary repair they contributed little, simply because there were so few of them.", "在普通的修复里，它们贡献很小，只因为数量太少。"),
('s', "But under the pressure of radiation, they expanded dramatically, clone by clone, rebuilding muscle and repopulating the niche.", "可在辐射的压力下，它们一个克隆接一个克隆地大规模扩增，重建肌肉，重新填满微环境。"),
('v', 'reserve', 3),
('s', "When the team removed Pax3 from these reserve cells, their reactive oxygen rose, and their survival and stress tolerance fell.", "当团队从这些储备细胞里去掉 Pax3，它们的活性氧升高，存活能力和抗压能力都下降了。"),
('s', "So the guardians are not one uniform regiment. Some are a reserve, built to outlast the storm.", "所以，守护者并不是清一色的一个团。其中有一部分是预备队，生来就是为了熬过风暴。"),
('v', 'bench', 3), ('r', 'Heslop 2000; Scaramozza 2019'), ('e', 'BENCH'),
('s', "A note from the bench. Heslop's method is still a favorite: the single-fiber culture.", "一段实验台笔记：Heslop 用的方法至今仍很受欢迎，那就是单纤维培养。"),
('s', "Digest the muscle gently with collagenase, and single fibers come free with their satellite cells still under the sleeve.", "用胶原酶温和地消化肌肉，单根纤维就会游离出来，卫星细胞仍留在袖套下面。"),
('s', "Float the fibers in medium, and you can watch the guardians wake, divide, and crawl away, fiber by fiber.", "把纤维漂在培养液里，你就能一根一根地看着守护者醒来、分裂、爬走。"),
('s', "To collect satellite cells in bulk, labs sort them by flow cytometry, for example keeping alpha-7 integrin positive cells and excluding blood and vessel cells.", "要大批收集卫星细胞，实验室会用流式细胞术分选，比如保留 α7 整合素阳性的细胞，排除血细胞和血管细胞。"),
('s', "But remember, digestion and sorting themselves begin to wake the cells. A freshly isolated guardian is no longer quite at rest.", "但要记住，消化和分选本身就会开始唤醒细胞。刚分离出来的守护者，已经不完全处于静息了。"),

('sec', "5  The children", "五  孩子们"),
('v', 'growth', 0), ('r', 'Bachman 2020 iScience'), ('e', 'FACT'),
('s', "Now we come to the most painful part of tonight's story.", "现在，我们来到今晚故事里最让人心痛的部分。"),
('s', "In a child, muscle is not merely being maintained. It is being built.", "在孩子身上，肌肉不只是在维持，而是在建造。"),
('v', 'growth', 1),
('s', "Before puberty, satellite cells actively contribute to fiber growth, and some of them are busy at that age.", "青春期之前，卫星细胞积极参与纤维的生长，其中一些在这个年纪正忙着干活。"),
('s', "In 2020, Bachman, Joe Chakkalakal and their colleagues asked what radiation does to them at that age.", "2020 年，Bachman、Joe Chakkalakal 和同事追问：在这个年纪，射线会对它们做什么？"),
('s', "Using a small animal radiation research platform, they gave prepubertal mice a local, fractionated course of radiation.", "他们用一台小动物放射研究平台，给青春期前的小鼠做了局部、分次的照射。"),
('v', 'growth', 2),
('s', "Right after treatment, satellite cell numbers fell. The survivors worked less well, though some myogenic potential remained.", "照射一结束，卫星细胞数量就下降了。幸存者功能变差，但仍保留了一些成肌潜能。"),
('v', 'growth', 3),
('s', "Fourteen months later, fibers were smaller and held fewer nuclei, in both fast and slow muscles.", "十四个月后，无论快肌还是慢肌，纤维都更细，细胞核也更少。"),
('s', "And when the team depleted satellite cells genetically before puberty, with no radiation at all, the same lifelong deficits appeared.", "而当团队在青春期前用基因手段清除卫星细胞、完全不照射时，同样的终身缺陷也出现了。"),
('s', "That second experiment matters most. It points directly at the guardians.", "第二个实验最关键，它直接指向了守护者。"),
('v', 'kallenbach', 0), ('r', 'Kallenbach 2022 J Cachexia Sarcopenia Muscle; Paris 2020 Sci Rep'),
('s', "In 2022, Kallenbach and the same group gave three doses of eight point two grays to the hindlimbs of four-week-old mice.", "2022 年，Kallenbach 和同一团队给四周龄小鼠的后肢照射了三次，每次 8.2 Gy。"),
('s', "Some of those mice carried a childhood muscle cancer, rhabdomyosarcoma, which the radiation eliminated.", "其中一些小鼠身上长着一种儿童肌肉肿瘤，横纹肌肉瘤，照射把它消灭了。"),
('v', 'kallenbach', 1),
('s', "With radiation alone, by eight weeks of age, muscle mass was down seventeen percent, and muscle function twenty-five.", "单纯照射，到八周龄时，肌肉质量下降 17%，肌肉功能下降 25%。"),
('s', "Satellite cells were down forty-five percent, and fiber cross-sectional area thirty percent.", "卫星细胞减少 45%，纤维横截面积减少 30%。"),
('v', 'kallenbach', 2),
('s', "At sixteen months, middle age for a mouse, the fibers were still shrunken, nuclei were still missing, and the fibrosis was lifelong.", "到十六个月，也就是小鼠的中年，纤维依然萎缩，细胞核依然缺失，纤维化终身存在。"),
('s', "A related study found that blocked fiber growth is a consistent feature of pediatric cancer treatment in these models.", "一项相关研究发现，在这些模型里，纤维生长受阻是儿童肿瘤治疗的一个一贯特征。"),
('v', 'species', 0), ('r', 'Collao 2023 J Cachexia Sarcopenia Muscle; Zeng 2022 Radiat Res'),
('s', "But a careful detective checks whether every witness tells the same story.", "可细心的侦探要核对：每个证人讲的是不是同一个故事。"),
('s', "Collao, De Lisio and their colleagues gave a single dose of sixteen grays to one hindlimb of four-week-old mice, shielding the other.", "Collao、De Lisio 和同事给四周龄小鼠的一侧后肢单次照射 16 Gy，另一侧遮挡。"),
('s', "They found fewer satellite cells at three days, and again at fifty-six days.", "他们发现，第 3 天卫星细胞变少，第 56 天又一次变少。"),
('v', 'species', 1),
('s', "Yet in rats given ninety grays in one shot, a team led by Zeng counted more satellite cells, not fewer, across twenty-four weeks.", "可是在一次照射 90 Gy 的大鼠里，Zeng 领衔的团队在 24 周里数到的卫星细胞反而更多，而不是更少。"),
('s', "A different species, a far higher single dose, and a different clock.", "物种不同，单次剂量高得多，时间线也不同。"),
('s', "And more satellite cells is not the same as successful repair. Fibrosis rose in those rats all the same.", "而且，卫星细胞多，不等于修复成功。那些大鼠的纤维化照样在加重。"),
('v', 'species', 2),
('s', "So we cannot fold these results into one tidy story. Species, age, dose, and time all change what the guardians do.", "所以，我们不能把这些结果揉成一个整齐的故事。物种、年龄、剂量和时间，都会改变守护者的表现。"),
('v', 'verdict', 0), ('r', 'Vahidi Ferdousi 2014; Bachman 2020; Kallenbach 2022; Collao 2023'), ('e', 'FACT'),
('s', "So let us return to our puzzle and build an answer, one piece at a time, each with its honest label.", "那就回到我们的谜题，一块一块地拼出答案，每一块都贴上老实的标签。"),
('s', "First, the facts. Quiescent satellite cells repair DNA breaks well. And in irradiated young mice, their numbers still fall.", "先摆事实：静止的卫星细胞修复 DNA 断裂的能力很强；可在受照的幼鼠里，它们的数量仍然下降。"),
('s', "These two facts do not contradict each other, because mending a break is not the same as surviving everything that comes after it.", "这两个事实并不矛盾，因为修好一处断口，不等于能熬过随后的一切。"),
('v', 'verdict', 1), ('r', 'Bachman 2020; Caiozzo 2010'), ('e', 'HYPOTHESIS'),
('s', "Here is the first piece of the answer, and it is a hypothesis. In growing muscle, many guardians are not resting. They are at work.", "答案的第一块是一个假说：在生长中的肌肉里，很多守护者并不在静息，而是在干活。"),
('s', "Bachman's team proposed exactly this: because some satellite cells are active before puberty, they may be especially susceptible.", "Bachman 团队正是这样提出的：因为青春期前有些卫星细胞处于活跃状态，它们可能格外容易受伤。"),
('s', "And dividing satellite cells in a dish die or stall after a few grays, just as we saw.", "而正如我们看到的，培养皿里正在分裂的卫星细胞，挨上几 Gy 就会死亡或停滞。"),
('v', 'verdict', 2), ('r', 'Heslop 2000; Bachman 2020; Collao 2025 Am J Physiol Cell Physiol'), ('e', 'FACT'),
('s', "The second piece is firmer. Survivors often fail to perform. Heslop's fibers released few cells, and Bachman's survivors worked less well.", "第二块更扎实：幸存者常常不能履职。Heslop 的纤维只放出很少的细胞，Bachman 的幸存者功能也变差了。"),
('s', "A guardian that is alive but cannot answer the alarm is, to the muscle, nearly as good as gone.", "一个活着却应不了警报的守护者，对肌肉来说，几乎等于不在了。"),
('e', 'ASSOCIATION'),
('s', "The third piece is an association. Collao's single-cell study found a senescence signature, the p21 gene, in every type of resident muscle cell after radiation.", "第三块是一个关联：Collao 的单细胞研究发现，照射后，肌肉里每一类常驻细胞都带着衰老印记，也就是 p21 基因。"),
('s', "It also found a long-term relative loss of the most deeply quiescent satellite cells, the kind of reserve that Heslop and Scaramozza described.", "它还发现，处于最深静止状态的卫星细胞长期相对减少，那正是 Heslop 和 Scaramozza 描述的那种储备。"),
('s', "A gene signature is a witness, not a confession. It tells us senescence travels with the damage, not yet that it causes it.", "基因印记是证人，不是供词。它告诉我们衰老与损伤同行，却还没证明是衰老造成了损伤。"),
('v', 'verdict', 3), ('r', 'Collao 2023; Murphy 2011'), ('e', 'HYPOTHESIS'),
('s', "The last piece points beyond the guardians. In Collao's 2023 study, signals from irradiated neighbor cells impaired satellite cell differentiation and fusion in a dish.", "最后一块指向了守护者之外：在 Collao 2023 年的研究里，受照邻居细胞释放的信号，在培养皿里损害了卫星细胞的分化和融合。"),
('s', "Whether a hostile neighborhood is what silences the guardians inside a living muscle is still a hypothesis.", "在活体肌肉里，究竟是不是一个充满敌意的街区让守护者沉默，目前仍是假说。"),
('v', 'growth', 3), ('r', 'Bachman 2020; Kallenbach 2022'), ('e', ''),
('s', "So here is where tonight leaves us.", "今晚，我们就停在这里。"),
('s', "Fewer guardians helps explain why the muscle grows thin. A child's fibers stay small because builders were lost while the house was still going up.", "守护者变少，能帮助解释肌肉为什么变细：孩子的纤维一直偏细，是因为房子还在盖，工匠就没了。"),
('s', "But it does not explain why the muscle grows hard.", "但它解释不了，肌肉为什么会变硬。"),
('v', 'ablation', 3), ('r', 'Sambasivan 2011; Murphy 2011'),
('s', "Remember the mice of 2011. When the guardians vanished, connective tissue, fat, and inflammatory cells moved in.", "还记得 2011 年的那些小鼠吗？守护者一消失，结缔组织、脂肪和炎症细胞就搬了进来。"),
('s', "Somebody laid that scar. And the guardians were never alone in the niche.", "那道瘢痕，是有人铺下的。而守护者在微环境里，从来不是孤身一人。"),
('v', 'recap', 3), ('r', ''),
('s', "They live beside fibroblast-like builders, immune clean-up crews, the small vessels that feed them, and the power plants inside every fiber.", "它们身边有像成纤维细胞那样的建筑工、负责清扫的免疫细胞、给它们供给养分的小血管，还有每根纤维里的发电厂。"),
('s', "In the next episode, the neighbors turn.", "下一集，邻居变脸。"),
('s', "We will meet the fibro-adipogenic progenitors, the macrophages, a signal called TGF-beta, the vessels, and the mitochondria.", "我们会见到成纤维-成脂祖细胞、巨噬细胞、一种叫 TGF-β 的信号、血管，还有线粒体。"),
('s', "Until then, my friends, remember that a missing witness is evidence too.", "在那之前，朋友们，请记住：缺席的证人，本身也是证据。"),
('v', 'refs', 0), ('r', ''), ('e', ''),
('s', "The references for tonight's episode are on the screen.", "本集的参考文献，都在屏幕上。"),
]

REFS = [
"Mauro A. J Biophys Biochem Cytol 1961;9:493-495. doi:10.1083/jcb.9.2.493",
"Relaix F, Zammit PS. Development 2012;139:2845-2856. doi:10.1242/dev.069088",
"Lepper C, et al. Development 2011;138:3639-3646. doi:10.1242/dev.067595",
"Sambasivan R, et al. Development 2011;138:3647-3656. doi:10.1242/dev.067587",
"Murphy MM, et al. Development 2011;138:3625-3637. doi:10.1242/dev.064162",
"Cheung TH, Rando TA. Nat Rev Mol Cell Biol 2013;14:329-340. doi:10.1038/nrm3591",
"Vahidi Ferdousi L, et al. Stem Cell Res 2014;13:492-507. doi:10.1016/j.scr.2014.08.005",
"Caiozzo VJ, et al. Radiat Res 2010;174:582-589. doi:10.1667/RR2190.1",
"Heslop L, et al. J Cell Sci 2000;113:2299-2308. doi:10.1242/jcs.113.12.2299",
"Wernig A, et al. J Physiol 2000;522:333-345. doi:10.1111/j.1469-7793.2000.t01-2-00333.x",
"Boldrin L, et al. Stem Cells 2012;30:1971-1984. doi:10.1002/stem.1158",
"Scaramozza A, et al. Cell Stem Cell 2019;24:944-957.e5. doi:10.1016/j.stem.2019.03.020",
"Bachman JF, et al. iScience 2020;23:101760. doi:10.1016/j.isci.2020.101760",
"Kallenbach JG, et al. J Cachexia Sarcopenia Muscle 2022;13:296-310. doi:10.1002/jcsm.12902",
"Paris ND, et al. Sci Rep 2020;10:19501. doi:10.1038/s41598-020-75913-w",
"Collao N, et al. J Cachexia Sarcopenia Muscle 2023;14:2335-2349. doi:10.1002/jcsm.13320",
"Zeng X, et al. Radiat Res 2022;197:638-649. doi:10.1667/RADE-21-00183.1",
"Collao N, et al. Am J Physiol Cell Physiol 2025;328:C1995-C2012. doi:10.1152/ajpcell.00115.2025",
]

# Illustrator brief. Dark navy background as in Ep1; EN label first, short ZH under/after it.
# Steps build progressively: each step keeps everything from the previous step and adds the new element.
VIS = {
'recap': (
    "Step 0: Ep1 callback. A long horizontal muscle fiber (pale red cylinder, row of myonuclei like street lamps) with a gold armor sheen; "
    "a faint beam (thin white diagonal line) has just passed through it. Label 'Fiber survives 纤维存活'. "
    "Step 1: Below the fiber, a cross-section icon of the same muscle years later: thinner and greyed, with a leathery texture. Label 'Years later: thin + stiff 多年后：变细、变硬'. "
    "Step 2: Small round cells along the fiber edge light up, each with a blue 'PAX7' badge; a big question mark between a wrench icon "
    "('repair well 修复好') and an emptying row of badges ('ranks empty? 队伍为何空了？'). "
    "Step 3 (cliffhanger): Same fiber with only one or two PAX7 cells left; around it, shadowy silhouettes step forward in the niche: "
    "a spindly fibroblast-like cell ('FAP'), a macrophage blob ('macrophage 巨噬细胞'), a capillary tube ('vessel 血管'), a mitochondrion icon inside the fiber ('mitochondria 线粒体'), "
    "and a faint 'TGF-β' cloud. Caption 'The neighbors turn 邻居变脸 → Ep3'."),
'title': "Step 0: Series and episode title card. 'After the Beam 射线之后' small on top; large 'Episode 2 · The Guardians'; below '第二集 · 守护者'. "
         "Background motif: a single satellite cell silhouette tucked against a fiber edge, gold rim light.",
'em': (
    "photo: transmission electron micrograph of a skeletal muscle satellite cell between sarcolemma and basal lamina (CC-licensed, e.g. Wikimedia Commons). "
    "Fallback drawing if no photo: grayscale EM-style cross-section. "
    "Step 0: Grainy grey EM field showing the edge of a large muscle fiber (striated myofibrils inside). Caption 'Mauro 1961 · frog tibialis anticus 青蛙胫前肌 · electron microscope 电子显微镜'. "
    "Step 1: Zoom/circle highlight on a small flattened cell at the fiber border: large dark nucleus, thin rim of cytoplasm. Arrows: 'large nucleus 核大', 'little cytoplasm 胞质少'."),
'niche': (
    "Schematic of the satellite-cell niche (longitudinal cut through the fiber edge). "
    "Step 0: Fiber drawn as a wide pink band; around it a thin green outer line labelled 'basal lamina / basement membrane 基底膜（基板）' — draw it as a sleeve. "
    "Step 1: Just inside, a second thin line hugging the fiber: 'sarcolemma (fiber membrane) 肌膜'. "
    "Step 2: A small lens-shaped cell wedged between the two lines, glowing softly; label 'satellite cell 卫星细胞', with a tiny sentry/shield icon. "
    "Small text: 'inside the sleeve, outside the fiber 袖套之内，纤维之外'. "
    "Step 3: The cell's nucleus turns blue with a 'PAX7' tag; side caption 'PAX7 = master gene switch 总开关 · the badge 徽章'."),
'ablation': (
    "Logic diagram for a necessity test. "
    "Step 0: Courtroom-style card: 'Suspect 嫌疑人: satellite cell' vs 'Other candidates 其他候选: cells from other origins 其他来源细胞' with a scale balanced and a question mark 'Required? 是否必需？'. "
    "Step 1: Experiment logic in three boxes left→right: 'Remove Pax7+ cells 清除 Pax7+ 细胞' → 'Injure muscle 损伤肌肉' → 'Regeneration? 再生？'. "
    "Step 2: Result: control muscle cross-section full of new fibers with central nuclei ('control 对照: regenerates 再生') vs ablated muscle empty ('ablated 清除后: no regeneration 不再生'). "
    "Banner 'Three teams · three methods · one verdict 三个团队·三种方法·一个判决'. "
    "Step 3: In the ablated muscle, fill the empty space with yellow fat droplets, purple inflammatory cells and grey-green scar fibres; labels 'fat 脂肪', 'inflammatory cells 炎症细胞', 'connective tissue 结缔组织'. "
    "Small note: 'fibroblasts needed too 成纤维细胞也必需 (Murphy 2011)'."),
'three': (
    "Three journal-style cards side by side, header 'Development, Sept 2011 · same issue 同一期'. Each step highlights one card (others dimmed). "
    "Step 0: Card 1 'Lepper, Partridge & Fan' — icon: genetic ablation of Pax7+ cells; bullets 'TA injury → regeneration blocked 再生被阻断' and 'EDL graft → no rebuilding 移植肌也不重建'. "
    "Step 1: Card 2 'Sambasivan, Tajbakhsh et al. (Paris)' — icon: syringe 'diphtheria toxin 白喉毒素' + receptor on Pax7 cell 'Pax7-DTR'; bullets 'tissue loss, fat + inflammation 组织丢失、脂肪与炎症', "
    "'rescued by Pax7+ cell transplant 移植 Pax7+ 细胞可挽救' (green check). "
    "Step 2: Card 3 'Murphy, Kardon et al. (Utah)' — icon: 'Pax7-CreERT2 × R26R-DTA' and 'Tcf4-CreERT2 × R26R-DTA'; bullets 'SC ablation → no regenerated muscle, more connective tissue 无再生肌、结缔组织增多', "
    "'fibroblast ablation → early differentiation, smaller fibers 成纤维细胞清除→过早分化、纤维更细'."),
'cycle': (
    "The satellite-cell life cycle as a circular diagram. "
    "Step 0: One quiet cell under the basal lamina, labelled 'quiescent (G0) 静止'. Adult muscle at rest; 'most SCs not dividing 大多不分裂'. "
    "Step 1: Lightning bolt 'injury 损伤' → cell enlarges 'activated 激活' and starts dividing (two cells). "
    "Step 2: Arrow to a cluster of many small cells 'myoblasts 成肌细胞' → arrow to them fusing into a fiber 'fuse: repair / new fibers 融合：修复/新纤维'. "
    "Step 3: A curved return arrow from the cluster back to the niche: one cell goes quiet again, label 'self-renewal 自我更新 · leave guardians for next time 为下次留下守护者'. Circle closes."),
'quiescence': (
    "Analogy panel. "
    "Step 0: Left: old view — cell in a bunk bed with 'Zzz', crossed out lightly, 'dormant? 休眠？'. Right: new view — cell with small signal arrows inside (pathways) and a dial at 'poised 蓄势待发'; "
    "caption 'quiescence is actively maintained 静止是被主动维持的 (Cheung & Rando 2013)'. "
    "Step 1: Fire station illustration: engine parked (not running), boots and helmet by the door; alarm bell icon; labels 'ready 待命', 'rapid activation 快速激活', 'reversible 可逆'."),
'paradox': (
    "Two-column comparison, same cell family. "
    "Step 0: Left column 'At rest 静息': quiescent SC with a welder/wrench icon 'DNA-PKcs (NHEJ)'; caption 'repairs breaks well 修复好 (Vahidi Ferdousi 2014)'. "
    "Step 1: Right column 'Dividing in culture 培养中分裂': petri dish of SCs; bar dropping '≥5 Gy → numbers −≥70% 数量减少至少七成'; small icons 'apoptosis 凋亡', 'cycle arrest 周期停滞', "
    "'ROS/RNS ↑ 活性氧/氮升高', 'NO ↓ 一氧化氮下降' (Caiozzo 2010, in vitro). "
    "Step 2: A hinge icon between columns; caption 'sturdy at rest, fragile when dividing 静息时结实，分裂时脆弱'."),
'heslop': (
    "Experiment timeline, mouse hindlimb muscle (normal C57Bl/10 and mdx). "
    "Step 0: Mouse leg icon with a beam '18 Gy'; two groups labelled 'normal 正常' and 'mdx (Duchenne model 杜氏模型)'. "
    "Step 1: Result of IR alone: muscle section with no new fibers 'no significant regeneration 无明显再生'; single-fiber dish with only 1–2 cells 'few precursors, barely divide 前体少、几乎不分裂'. "
    "Step 2: Add snake icon / syringe 'notexin (snake venom toxin 蛇毒毒素)'. Now new fibers appear; single fiber with a growing cluster 'rapidly dividing precursors 快速分裂的前体'; "
    "small bar: normal > mdx. "
    "Step 3: Third lane '25 Gy + notexin': 'some new muscle 少量新肌' but 'no dividing precursors on fibers 纤维上无可分裂前体'. Summary box: "
    "'most myogenic cells radiosensitive 大多对辐射敏感 · a reserve survives 18 Gy 少数储备存活 · reserve diminished in mdx mdx 中储备减少'."),
'transplant': (
    "Transplant-host diagram. "
    "Step 0: Mouse soleus with beam '16 Gy X-ray' then syringe 'donor myoblasts 供体成肌细胞' (Wernig 2000). "
    "Step 1: Two bars: 'IR + sham 照射+假注射: mass & force ≈ −18% 质量和力量约降 18%' vs 'IR + donor cells 照射+供体细胞: deficits abolished 缺陷消除'. "
    "Step 2: Three small house icons (Boldrin 2012): (a) house standing, host residents removed, donor cells moving in → green check 'host SCs incapacitated + niche preserved 宿主卫星细胞失能+微环境保留'; "
    "(b) house destroyed → red X 'niche destroyed 微环境被毁'; (c) house full of competent residents → red X 'niche occupied 微环境被占'. "
    "Note on screen: no irradiation label on Boldrin panel (method not stated in the abstract)."),
'reserve': (
    "Lineage-tracing panel (Scaramozza 2019). "
    "Step 0: Fiber with ~12 PAX7 cells (blue). Title 'Who survived? 幸存者是谁？'. "
    "Step 1: 1–2 of them turn magenta, labelled 'Mx1-Cre marked 被标记 · Pax3-high Pax3 高 · low ROS 低活性氧'. "
    "Step 2: Two scenarios: 'ordinary injury 普通损伤' — magenta cells contribute a tiny share; 'radiation stress 辐射压力' — blue cells fade, magenta cells expand into large clones "
    "that fill fibers and repopulate the niche ('clonal expansion 克隆扩增'). "
    "Step 3: Inset: 'Pax3 removed 去掉 Pax3' → ROS ↑, survival ↓, stress tolerance ↓. Caption 'a radiotolerant reserve 耐辐射储备'."),
'growth': (
    "Juvenile growth panel (Bachman 2020). "
    "Step 0: Child silhouette beside a growing muscle fiber; caption 'built, not just maintained 是在建造，不只是维持'. "
    "Step 1: SCs fusing into the fiber, adding nuclei as it lengthens/thickens; label 'prepubertal SCs add nuclei 青春期前卫星细胞添加细胞核'; small beam 'local fractionated IR (SARRP) 局部分次照射'. "
    "Step 2: Immediately after: fewer SCs; survivors drawn dimmer 'fewer + weaker 更少、功能更差' with a small spark 'some myogenic potential remains 仍有部分潜能'. "
    "Step 3: Timeline arrow '14 months later 14 个月后': adult fiber thinner with fewer nuclei vs control; side box 'genetic SC depletion before puberty (no IR) → same deficits 青春期前基因清除（不照射）→相同缺陷'."),
'kallenbach': (
    "Bar chart, juvenile mice 3 × 8.2 Gy at 4 weeks old (Kallenbach 2022). "
    "Step 0: Protocol strip: '3 wk: RMS tumor cells (some mice) 部分小鼠种入横纹肌肉瘤' → '4 wk: 3 × 8.2 Gy hindlimb 后肢' → 'tumor eliminated 肿瘤消除'. "
    "Step 1: Horizontal bars, radiation-only vs control at 8 weeks of age: mass −17% 质量, function −25% 功能, satellite cells −45% 卫星细胞, fiber CSA −30% 横截面积. "
    "Step 2: Second timepoint '16 months (middle age) 16 月龄（中年）': fiber atrophy −20%, myonuclei −18%, 'lifelong fibrosis 终身纤维化'. Footnote 'Paris 2020: blocked hypertrophic growth 肥大生长受阻'."),
'species': (
    "Comparison table of conflicting witnesses. "
    "Step 0: Row 1 'Mouse, 4-week-old, single 16 Gy, contralateral leg shielded 小鼠4周龄·单次16 Gy·对侧遮挡' → 'SCs ↓ at day 3 and day 56 第3、56天减少' (Collao 2023). "
    "Step 1: Row 2 'Rat (SD), single 90 Gy groin 大鼠·单次90 Gy' → 'SCs ↑ over 1–24 weeks 数量增加; fibrosis ↑ anyway 纤维化仍加重' (Zeng 2022). Red 'vs' between rows. "
    "Step 2: Four dials beneath: 'species 物种', 'age 年龄', 'dose 剂量', 'time 时间'; caption 'more SCs ≠ successful repair 卫星细胞多≠修复成功'."),
'verdict': (
    "Evidence board answering the Ep1 puzzle; each card carries its colored tag. "
    "Step 0: Two green FACT cards pinned: 'quiescent SCs repair DSBs well 静止时修复好' and 'SC numbers fall after juvenile IR 幼年照射后数量下降'; string between them "
    "with note 'repair ≠ survival 修复≠存活'. "
    "Step 1: Red HYPOTHESIS card: 'growing muscle: many SCs active → more vulnerable 生长中肌肉：许多卫星细胞活跃→更易受伤' (Bachman 2020 authors' proposal; Caiozzo 2010 in vitro support). "
    "Step 2: Green FACT card 'survivors fail to perform 幸存者功能受损 (Heslop 2000; Bachman 2020)' + amber ASSOCIATION card "
    "'p21 (Cdkn1a) senescence signature in all resident cells; deep-quiescent SCs relatively depleted 所有常驻细胞 p21 印记；深静止卫星细胞相对减少 (Collao 2025)'. "
    "Step 3: Red HYPOTHESIS card 'hostile niche silences guardians 敌意微环境让守护者沉默' with small FACT sub-note 'irradiated neighbor-cell secretome impairs SC differentiation/fusion in vitro 体外：受照邻居细胞分泌物损害分化/融合 (Collao 2023)'; "
    "arrow off the board toward Ep3."),
'bench': (
    "Same bench card layout as Ep1 (title in gold + up to 4 bullet rows, EN left / ZH right). "
    "Step 0 title: 'Counting satellite cells  数卫星细胞'. Rows: "
    "('PAX7 antibody', '核内 PAX7'); ('+ laminin', '勾出基底膜'); ('+ DAPI', '所有细胞核'); ('per 100 fibers · blind', '每百根纤维·盲法'). "
    "Step 1 title: 'One switch, two experiments  一个开关，两种实验'. Rows: "
    "('Pax7-CreER + tamoxifen', '他莫昔芬开锁'); ('R26-stop-DTA', '清除：是否必需'); ('R26-stop-reporter', '示踪：变成什么'); ('Cre removes stop', 'Cre 剪掉终止信号'). "
    "Step 2 title: 'Who has divided?  谁分裂过？'. Rows: "
    "('EdU short pulse', '短时给药：谁在复制'); ('long pulse + chase', '长给药+等待'); ('label-retaining cells', '标记滞留细胞'); ('lowest dose · + PAX7', '最低剂量·共染 PAX7'). "
    "Step 3 title: 'Single fibers & sorting  单纤维与分选'. Rows: "
    "('collagenase digest', '胶原酶消化'); ('single-fiber culture', '单纤维培养'); ('FACS: α7-integrin+, lineage−', '流式：α7整合素+，排除血/血管细胞'); ('isolation activates cells', '分离本身会激活细胞')."),
'refs': "Step 0: Reference list screen, same layout as Ep1 (18 entries, smaller font).",
}
