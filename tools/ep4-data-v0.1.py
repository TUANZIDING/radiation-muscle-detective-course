# Episode 4 data v0.1: finale, ~20 min. Same tuple format as ep1-data-v0.2.py.
# ('sec', en_title, zh_title)   section header (adds pause, sets label)
# ('v', key, step)              visual state
# ('r', 'ref1; ref2')           reference card for following lines
# ('e', 'FACT'|'ASSOCIATION'|'HYPOTHESIS'|'BENCH'|'')  evidence tag
# ('s', en, zh)                 one narrated subtitle line
# Every number below was checked against literature-v0.1.md and the PubMed abstracts
# (fetched 2026-10-29). Human clinical sections are tagged ASSOCIATION (observational).
EP = 4
TITLE_EN = "From Bench to Bedside"
TITLE_ZH = "从实验台到病床"

D = [
('sec', "Cold open", "序幕"),
('v', 'case4', 0), ('r', ''), ('e', ''),
('s', "My friends, for three nights we have followed a beam of light into the body. Tonight, we follow it home.", "朋友们，三个晚上，我们跟着一束光走进了身体。今晚，我们要跟着它回家。"),
('s', "Let me remind you how far we have come.", "让我先提醒你，我们已经走了多远。"),
('v', 'case4', 1),
('s', "The beam broke the blueprint of life, and the muscle fiber, armored by its own maturity, survived.", "射线撕裂了生命的蓝图，而肌纤维凭着自身成熟带来的盔甲，活了下来。"),
('s', "Its guardians, the satellite cells, paid the price, and in young muscle that price was paid for a lifetime.", "付出代价的是它的守护者——卫星细胞；而在年轻的肌肉里，这份代价要用一生去偿还。"),
('v', 'case4', 2),
('s', "Then the neighbors turned. The builders called FAPs froze into senescence and began laying scar, urged on by TGF-beta.", "接着，邻居变了脸。名叫 FAPs 的建筑工冻结成衰老状态，在 TGF-β 的催促下开始铺设瘢痕。"),
('s', "The supply lines thinned, and the power plants faltered.", "补给线变稀了，发电厂也开始失灵。"),
('v', 'case4', 3),
('s', "That is our working model. But a model built in mice is only a story until it meets a patient.", "这就是我们的工作模型。可一个在小鼠身上建起的模型，在遇见病人之前，只是一个故事。"),
('s', "So tonight we leave the laboratory, walk down the hall, and knock on the clinic door.", "所以今晚，我们离开实验室，穿过走廊，去敲诊室的门。"),
('v', 'title', 0),
('s', "This is our final episode: from the bench to the bedside.", "这是我们的最后一集：从实验台到病床。"),
('s', "We will weigh the human evidence, open the detective's toolkit, face the clues that contradict each other, and examine every attempt to pick the lock.", "我们要掂量人体证据，打开侦探的工具箱，直面互相矛盾的线索，再逐一检查每一次撬锁的尝试。"),
('s', "And at the end, I will sum up the whole case for you, as I would for a jury.", "最后，我会像面对陪审团那样，为你总结整个案子。"),

('sec', "1  The human cases", "一  人体证据"),
('v', 'rfs', 0), ('r', 'Stubblefield 2011 PM R; Fijardo 2024 EBioMedicine'), ('e', 'ASSOCIATION'),
('s', "Let us begin with the patients themselves.", "先从病人本身说起。"),
('s', "In 2011, Michael Stubblefield, a rehabilitation physician at Memorial Sloan Kettering, wrote a review describing what clinicians call radiation fibrosis syndrome.", "2011 年，纪念斯隆-凯特琳癌症中心的康复科医生 Michael Stubblefield 写了一篇综述，描述临床上所说的放射纤维化综合征。"),
('s', "It names the many clinical faces of a slow, progressive hardening of tissue, set in motion by radiotherapy.", "这个名字涵盖了由放疗启动的、缓慢而进行性的组织硬化所呈现的种种临床面貌。"),
('v', 'rfs', 1),
('s', "Its reach is long. It can touch the spinal cord, the nerve roots, the nerve plexus, the nerves, and the muscle itself.", "它波及很广：可以累及脊髓、神经根、神经丛、周围神经，以及肌肉本身。"),
('s', "Stubblefield wrote it as one long word: myelo-radiculo-plexo-neuro-myopathy.", "Stubblefield 把它写成一个长长的词：脊髓-神经根-神经丛-神经-肌病。"),
('s', "Notice what that means for us. When a survivor is weak, the victim may be the muscle, or the nerve that drives it, or both.", "请注意这对我们意味着什么：一位幸存者无力时，受害者可能是肌肉，也可能是支配它的神经，或者两者都是。"),
('v', 'rfs', 2),
('s', "In head and neck cancer survivors, he highlighted trismus, a jaw that will not open, and cervical dystonia, a neck pulled by muscles that will not relax.", "在头颈部肿瘤幸存者中，他特别指出了牙关紧闭——张不开的下颌，以及颈部肌张力障碍——被放松不下来的肌肉拉扯的脖子。"),
('s', "A 2024 review by Fijardo and colleagues gathers these clinical pictures together with their molecular roots.", "Fijardo 等人 2024 年的综述，把这些临床表现和它们的分子根源放在了一起。"),
('v', 'swallow', 0), ('r', 'Hutcheson 2012 Cancer'),
('s', "Now to the survivor who cannot swallow.", "现在来看那位无法吞咽的幸存者。"),
('s', "In 2012, Katherine Hutcheson and her colleagues at MD Anderson described twenty-nine head and neck cancer survivors with swallowing trouble, all at least five years past radiotherapy.", "2012 年，MD 安德森癌症中心的 Katherine Hutcheson 和同事报告了 29 位有吞咽困难的头颈部肿瘤幸存者，他们都已在放疗后至少五年。"),
('s', "The median time since treatment was nine years.", "距离治疗的中位时间是九年。"),
('v', 'swallow', 1),
('s', "X-ray swallowing studies showed food left behind in the throat, and food entering the airway, in every one of them.", "X 线吞咽造影显示：每一个人都有食物残留在咽部，也都有食物进入气道。"),
('s', "Trismus was found in thirty-eight percent.", "38% 的人有牙关紧闭。"),
('v', 'swallow', 2),
('s', "Eighty-six percent developed pneumonia, and half of those needed a hospital bed.", "86% 的人得过肺炎，其中一半需要住院。"),
('s', "In the end, sixty-six percent depended on a feeding tube.", "最终，66% 的人要依赖胃造瘘管进食。"),
('v', 'swallow', 3),
('s', "The authors' key point was this: severe dysphagia may develop or progress years after treatment.", "作者的核心观点是：严重的吞咽困难可能在治疗多年之后才出现或加重。"),
('s', "Remember, these were patients referred for testing, not a random sample. The study shows the problem is real, not how common it is.", "要记住，这些是被转诊来做检查的病人，不是随机样本。这项研究说明问题真实存在，却说明不了它有多常见。"),
('v', 'survivor', 0), ('r', 'McCastlain 2021 J Natl Cancer Inst; Ness 2015 Cancer'),
('s', "Next, the children who grew up.", "接下来，是那些已经长大的孩子。"),
('s', "In 2021, a St. Jude team studied 1,762 adult survivors of childhood cancer, a median of about twenty years after diagnosis.", "2021 年，圣裘德儿童研究医院的团队研究了 1762 位儿童肿瘤的成年幸存者，距诊断的中位时间约二十年。"),
('s', "Their median age was only twenty-nine. Yet twenty-seven percent had sarcopenia, meaning low muscle mass or a weak grip.", "他们的中位年龄只有 29 岁，却有 27% 患有肌少症，也就是肌肉量低或握力弱。"),
('v', 'survivor', 1),
('s', "Cranial radiation was linked to higher odds, with an odds ratio of 1.84.", "头颅放疗与更高的患病几率相关，比值比为 1.84。"),
('s', "And survivors with fewer copies of mitochondrial DNA in their blood were more likely to have sarcopenia.", "血液中线粒体 DNA 拷贝数越少的幸存者，越可能患肌少症。"),
('s', "But mark the tag. This is an association, measured at one point in time. It does not prove that mitochondria caused the weakness.", "但请看标签：这是关联，而且是在同一个时间点测得的。它不能证明是线粒体导致了无力。"),
('v', 'survivor', 2),
('s', "In 2015, Kirsten Ness and her colleagues warned that young adult survivors can be frail, a condition usually found in the elderly.", "2015 年，Kirsten Ness 和同事提醒：年轻的成年幸存者可能已经衰弱，而衰弱通常见于老年人。"),
('s', "They proposed early senescence, sterile inflammation, and failing mitochondria as causes. You know all three suspects. But they called it what it is: a hypothesis.", "他们提出，过早衰老、无菌性炎症和线粒体功能障碍可能是原因。这三个嫌疑人你都认识。但他们实事求是地称之为：假说。"),
('v', 'biopsy', 0), ('e', ''),
('s', "Now, an honest confession.", "现在，坦白一件事。"),
('s', "You might expect many human muscle biopsies, taken years after radiotherapy, showing exactly which cells are missing.", "你也许以为，会有很多放疗多年后取的人体肌肉活检，清楚地显示到底少了哪些细胞。"),
('v', 'biopsy', 1),
('s', "In preparing this series, I did not find a good biopsy series of that kind.", "在准备这个系列时，我没有找到那样像样的活检系列研究。"),
('s', "The human evidence is mostly clinical and functional. The cellular story we told comes almost entirely from animals and from dishes.", "人体证据大多是临床和功能层面的。我们讲的细胞故事，几乎全部来自动物和培养皿。"),
('s', "That gap is not a failure. It is an invitation.", "这个空白不是失败，而是一份邀请。"),

('sec', "2  The detective's toolkit", "二  侦探工具箱"),
('v', 'models', 0), ('r', 'Collao 2023 JCSM; Bachman 2020 iScience; Kallenbach 2022 JCSM; Zhou 2018 Radiat Oncol; Jiang 2024 BBA'), ('e', 'FACT'),
('s', "So how does a young detective work this case? Let us open the toolkit.", "那么，一位年轻的侦探该怎么办这个案子？我们打开工具箱。"),
('s', "The first choice is the model, and every model answers a slightly different question.", "第一个选择是模型，而每种模型回答的问题都略有不同。"),
('v', 'models', 1),
('s', "A single large dose is simple and gives strong effects quickly. A fractionated schedule of smaller doses looks more like the clinic.", "单次大剂量简单，效应强而快；分成几次的小剂量方案，更接近临床。"),
('s', "Juvenile animals model childhood cancer, when growing muscle is most vulnerable. Adult animals model the far more common adult patient.", "幼年动物模拟儿童肿瘤，那时生长中的肌肉最脆弱；成年动物模拟更常见的成年病人。"),
('v', 'models', 2),
('s', "Mice offer genetic tools: lineage tracing, gene knockouts, single-cell sequencing. Rats are larger, and have carried very high-dose fibrosis models.", "小鼠提供遗传学工具：谱系示踪、基因敲除、单细胞测序。大鼠体型更大，被用来建立超高剂量的纤维化模型。"),
('s', "Some teams add a tumor, such as a juvenile rhabdomyosarcoma, so that cancer and treatment travel together, as they do in patients.", "有些团队还会加上肿瘤，比如幼年横纹肌肉瘤，让肿瘤和治疗同时存在，就像在病人身上那样。"),
('v', 'models', 3),
('s', "And in the dish, we have muscle cells and human stem-cell organoids.", "在培养皿里，我们有肌肉细胞，也有用人类干细胞做的类器官。"),
('s', "They let us watch repair in human cells, but they have no blood vessels, no immune system, and no years to wait.", "它们让我们能在人类细胞里观察修复，但它们没有血管，没有免疫系统，也等不了好几年。"),
('v', 'doses', 0), ('r', 'Jiang 2024; Collao 2023; Kallenbach 2022; Gans 2021; Zeng 2022'),
('s', "Now look at the doses, because this is where beginners stumble.", "再看剂量，因为初学者最容易在这里摔跤。"),
('s', "The human organoid study used two grays.", "人类类器官研究用的是 2 Gy。"),
('v', 'doses', 1),
('s', "Collao's juvenile mice received a single sixteen grays to one hind leg. The Rochester group gave three fractions of eight point two grays.", "Collao 的幼年小鼠一侧后肢单次接受 16 Gy；罗切斯特团队则分三次给予，每次 8.2 Gy。"),
('s', "Notice the difference. Fractions give normal tissue time to repair, so a fractionated total is gentler than the same total given at once.", "注意其中的区别：分次给照让正常组织有时间修复，所以同样的总剂量，分次给比一次给更温和。"),
('v', 'doses', 2),
('s', "A mouse study of TGF-beta inhibition used fifty grays in a single fraction.", "一项 TGF-β 抑制的小鼠研究，用了单次 50 Gy。"),
('s', "A dose like that produces strong, measurable scarring in adult animals within months.", "这样的剂量能在几个月内，让成年动物出现明显、可测量的瘢痕。"),
('v', 'doses', 3),
('s', "And the rat fibrosis models used ninety grays in a single shot. That is not a typo.", "而大鼠纤维化模型用的是单次 90 Gy。这不是笔误。"),
('s', "These numbers span a forty-five-fold range. They are not one experiment repeated. They are different worlds, and we must never merge them without saying so.", "这些数字相差四十五倍。它们不是同一个实验的重复，而是不同的世界；绝不能不加说明就把它们混成一个故事。"),
('v', 'readouts', 0), ('r', "Collao 2023; Kallenbach 2022; O'Connor 2022 Skelet Muscle; Collao 2025"),
('s', "Next, the readouts. What do we actually measure?", "接下来是读数：我们到底测什么？"),
('s', "For scar, Masson's trichrome stain turns collagen blue, and we measure how much of the section is blue.", "看瘢痕，用 Masson 三色染色把胶原染成蓝色，再测切片里蓝色占多大比例。"),
('v', 'readouts', 1),
('s', "For atrophy, we weigh the muscle and measure fiber cross-sectional area.", "看萎缩，就称肌肉重量，测肌纤维横截面积。"),
('s', "For the guardians, we count PAX7 cells. For DNA damage, we count the gamma-H2AX flares you met in episode one.", "看守护者，就数 PAX7 细胞；看 DNA 损伤，就数第一集里认识的 γH2AX 信号弹。"),
('v', 'readouts', 2),
('s', "For the neighbors, flow cytometry counts FAPs, endothelial cells, and immune cells. Single-cell sequencing reads thousands of cells, one at a time.", "看邻居，流式细胞术可以计数 FAPs、内皮细胞和免疫细胞；单细胞测序可以一个一个地读取成千上万个细胞。"),
('s', "It can tell you not only who is present, but what each cell may be saying to its neighbors.", "它不仅能告诉你谁在场，还能提示每个细胞可能在对邻居说什么。"),
('v', 'readouts', 3),
('s', "And for function, the readout that matters most to a patient: force.", "而看功能，就是对病人最要紧的那个读数：肌力。"),
('s', "O'Connor and colleagues measured force in muscles removed from the body. Irradiation cut the specific force of a fast muscle by twenty-seven percent.", "O'Connor 等人在离体肌肉上测力：照射使一块快肌的比肌力下降了 27%。"),
('v', 'timeline4', 0), ('r', 'Collao 2023; Collao 2025; Kallenbach 2022; Bachman 2020'),
('s', "Then the controls. The most elegant is the shielded leg.", "然后是对照。最精巧的，是遮挡的那条腿。"),
('s', "Irradiate one hind limb, shield the other, and each animal carries its own control, with the same blood, diet, and age.", "照射一侧后肢，遮挡另一侧，每只动物就自带对照：同样的血液、同样的饮食、同样的年龄。"),
('s', "But the shielded leg may not be perfectly innocent. Signals in the blood can reach it, so an unirradiated animal is a wise second control.", "但被遮挡的腿未必完全清白。血液里的信号可能到达那里，所以再加一组未照射的动物作为第二对照，是明智之举。"),
('v', 'timeline4', 1),
('s', "Finally, timepoints. Collao's team examined muscle at three, seven, fourteen, and fifty-six days.", "最后是时间点。Collao 团队在第 3、7、14 和 56 天检查肌肉。"),
('s', "Their single-cell study read the muscle at twenty-four hours and at fifty-six days.", "他们的单细胞研究则在 24 小时和 56 天读取肌肉。"),
('v', 'timeline4', 2),
('s', "The Rochester group waited fourteen months, deep into middle age for a mouse.", "罗切斯特团队等了 14 个月，对小鼠来说已经步入中年。"),
('s', "Early timepoints show the injury. Late timepoints show the disease the patient will live with.", "早期时间点展示的是损伤；晚期时间点展示的，才是病人要与之共处的疾病。"),
('v', 'bench', 0), ('r', 'Collao 2023; Gans 2021 Clin Orthop'), ('e', 'BENCH'),
('s', "A note from the bench, for your first study design.", "一段实验台笔记，送给你的第一个研究设计。"),
('s', "Before you irradiate a single animal, write down your question, your primary outcome, and the timepoint where you expect to see it.", "在照射第一只动物之前，先写下你的问题、你的主要结局指标，以及你预期看到它的时间点。"),
('s', "Randomize animals to groups, and record strain, sex, age, and weight. Collao used four-week-old mice; Gans used twelve-week-old adults.", "把动物随机分组，记录品系、性别、年龄和体重。Collao 用的是 4 周龄小鼠，Gans 用的是 12 周龄的成年鼠。"),
('s', "Fix your controls in advance: a shielded leg, unirradiated animals, and when you test a drug, a vehicle group that gets the same injections.", "提前定好对照：遮挡腿、未照射动物；测试药物时，还要有一组注射同样溶媒的对照。"),
('v', 'bench', 1), ('r', 'Hardee 2014 Radiol Oncol'),
('s', "Another note from the bench, on dose.", "再来一段实验台笔记，关于剂量。"),
('s', "Report the machine, the energy, the dose rate, the field, the shielding, and how you verified the dose.", "要报告机器、能量、剂量率、照射野、遮挡方式，以及剂量如何核实。"),
('s', "A dose no one can reproduce is a rumor, not a fact.", "别人无法重复的剂量，只是传闻，不是事实。"),
('s', "When schedules differ, compare biologically effective doses. In Hardee's mouse study, four fractions of four grays had a BED of thirty-seven; a single sixteen grays, about one hundred.", "方案不同时，就比较生物有效剂量。在 Hardee 的小鼠研究里，4 次各 4 Gy 的 BED 是 37；单次 16 Gy 约为 100。"),
('s', "Same total dose, nearly three times the biological punch. And at extreme single doses, the usual formula becomes much less trustworthy.", "总剂量相同，生物学冲击却差了近三倍。而在极端的单次大剂量下，常用的公式就远没那么可靠了。"),

('sec', "3  Conflicting clues", "三  互相矛盾的线索"),
('v', 'conflict', 0), ('r', 'Zeng 2022 Radiat Res; Zhou 2018 Radiat Oncol'), ('e', 'FACT'),
('s', "Every good case has a witness who seems to tell a different story.", "每个好案子里，都有一个似乎讲着不同故事的证人。"),
('s', "In the rat model, with ninety grays to the groin, Zeng and colleagues reported in 2022 that satellite cells were activated, and their numbers increased.", "在腹股沟区照射 90 Gy 的大鼠模型里，Zeng 等人 2022 年报告：卫星细胞被激活了，数量还增加了。"),
('s', "Zhou's earlier work in the same model found myogenic genes, Pax7 and MyoD among them, rising around the fourth week.", "Zhou 早先在同一模型里发现，包括 Pax7 和 MyoD 在内的成肌基因，在第四周左右升高。"),
('v', 'conflict', 1), ('r', 'Kallenbach 2022; Bachman 2020; Collao 2023'),
('s', "Yet in juvenile mice, the guardians fell. Kallenbach's team found forty-five percent fewer satellite cells; Collao found fewer at three days and at fifty-six days.", "可在幼年小鼠里，守护者倒下了。Kallenbach 团队发现卫星细胞少了 45%；Collao 在第 3 天和第 56 天都发现它们变少。"),
('s', "So which witness is lying?", "那么，哪个证人在说谎？"),
('v', 'conflict', 2), ('e', 'HYPOTHESIS'),
('s', "Perhaps neither. Look at what differs.", "也许谁都没说谎。看看有哪些不同。"),
('s', "Species: rat versus mouse. Dose: ninety grays at once, versus sixteen, or three fractions of eight point two.", "物种：大鼠对小鼠。剂量：一次 90 Gy，对 16 Gy，或三次各 8.2 Gy。"),
('s', "Age: rats not described as juvenile, versus mice irradiated at four weeks, when the guardians are busy building growing fibers.", "年龄：没有被描述为幼年的大鼠，对 4 周龄就受照的小鼠——那时守护者正忙着建造生长中的纤维。"),
('v', 'conflict', 3),
('s', "And time. Activation is a burst of effort. Depletion is what remains after the effort is spent. One snapshot can catch the burst, another the exhaustion.", "还有时间。激活是一阵拼命，耗竭是拼命之后剩下的局面。一张快照可能拍到拼命，另一张拍到的是精疲力竭。"),
('s', "Zhou's own authors concluded that regeneration was set in motion only at an early stage.", "Zhou 的作者们自己也得出结论：再生过程只在早期被启动。"),
('s', "My reconciliation is a hypothesis, not a verdict. The experiment that would settle it is side by side: same species, matched doses, many timepoints.", "我的调和只是假说，不是判决。能一锤定音的实验，是并排比较：同一物种、匹配的剂量、多个时间点。"),
('v', 'tumorev', 0), ('r', 'Zhang 2025 Cell Metab'), ('e', 'FACT'),
('s', "And now, the plot twist of 2025.", "现在，来看 2025 年的剧情反转。"),
('s', "All along we assumed the crime happened at the scene: the beam strikes the muscle, and the muscle is injured.", "一直以来，我们都假定罪案发生在现场：射线击中肌肉，肌肉受伤。"),
('v', 'tumorev', 1),
('s', "Zhang and colleagues, writing in Cell Metabolism, found that after irradiation, the tumor itself sends something out.", "Zhang 等人在《细胞·代谢》上发表的研究发现：照射之后，肿瘤自己会往外送东西。"),
('s', "Radiation raised a fatty acid, arachidonic acid, in cancer cells, which then packed an enzyme, spermidine synthase, into small extracellular vesicles.", "照射使癌细胞里一种脂肪酸——花生四烯酸——增多，癌细胞随后把一种酶，亚精胺合酶，装进小细胞外囊泡。"),
('v', 'tumorev', 2),
('s', "These tiny parcels traveled in the circulation. In muscle, spermidine accumulated, and type one collagen was built, through a factor called eIF5A.", "这些小包裹随循环流动。在肌肉里，亚精胺累积，并通过一个叫 eIF5A 的因子，合成出 I 型胶原。"),
('s', "In other words, the stiffening signal arrived by mail, from the organ the beam was aimed at, to a muscle that was only nearby.", "换句话说，促使肌肉变硬的信号是“寄”来的：从射线瞄准的器官，寄到只是在旁边的肌肉。"),
('v', 'tumorev', 3),
('s', "Losartan, a common blood pressure drug, blocked the export of that enzyme in their mice.", "在他们的小鼠里，常用降压药氯沙坦阻断了这种酶的外送。"),
('s', "If this holds in patients, part of the muscle's injury may be ordered from a distance, by the tumor.", "如果这在病人身上成立，肌肉的一部分损伤可能是肿瘤从远处“下单”的。"),
('s', "For now, it is a mouse finding awaiting confirmation in people.", "目前，这仍是有待人体证实的小鼠发现。"),

('sec', "4  Attempts to pick the lock", "四  撬锁的尝试"),
('v', 'ptx', 0), ('r', 'Delanian 2003 J Clin Oncol; Delanian 2020 Int J Radiat Oncol Biol Phys'), ('e', 'FACT'),
('s', "So, can the lock be picked?", "那么，这把锁能撬开吗？"),
('s', "The oldest serious attempt is a pair of pills: pentoxifylline, an old drug for blood flow, and vitamin E, an antioxidant.", "最早的正式尝试是一对药片：己酮可可碱，一种改善血流的老药；以及维生素 E，一种抗氧化剂。"),
('v', 'ptx', 1),
('s', "In 2003, Sylvie Delanian and colleagues ran a double-blind, placebo-controlled trial in twenty-four women with fibrosis after breast radiotherapy.", "2003 年，Sylvie Delanian 和同事在 24 位乳腺癌放疗后出现纤维化的女性中，做了一项双盲、安慰剂对照试验。"),
('s', "After six months, the combination shrank the fibrotic area by sixty percent, against forty-three percent with double placebo. Either drug alone was ineffective.", "六个月后，联合用药使纤维化面积缩小 60%，双安慰剂组为 43%。单用任何一种都无效。"),
('v', 'ptx', 2),
('s', "But the trial was small, and the fibrosis was superficial, in skin and the tissue beneath it, not deep muscle.", "但这项试验很小，治疗的是浅表纤维化——皮肤和皮下组织，而不是深部肌肉。"),
('s', "In 2020, a trial adding clodronate treated radiation nerve plexopathy for eighteen months. It failed to show a benefit.", "2020 年，一项加用氯膦酸盐、治疗放射性神经丛病 18 个月的试验，未能显示获益。"),
('s', "So the evidence is mixed: promising for superficial fibrosis, unproven for deep muscle.", "所以证据是混合的：对浅表纤维化有希望，对深部肌肉尚未证实。"),
('v', 'tgfb', 0), ('r', 'Gans 2021 Clin Orthop Relat Res; Martin 2000 IJROBP'),
('s', "Next, the master switch itself, TGF-beta.", "接下来，是总开关本身：TGF-β。"),
('s', "Gans and colleagues gave adult mice fifty grays to one hind limb, then a daily TGF-beta inhibitor for eight weeks.", "Gans 等人给成年小鼠一侧后肢照射 50 Gy，随后连续八周每天注射 TGF-β 抑制剂。"),
('v', 'tgfb', 1),
('s', "Nine months after radiation, fibrosis covered 1.2 percent of the quadriceps section without treatment, and 0.14 percent with the inhibitor.", "照射九个月后，未治疗组股四头肌切片的纤维化面积为 1.2%，抑制剂组为 0.14%。"),
('s', "Unirradiated control mice showed 0.05 percent, so the inhibitor brought the scar most of the way back toward normal.", "未照射的对照小鼠为 0.05%，所以抑制剂让瘢痕大部分回落到接近正常的水平。"),
('v', 'tgfb', 2),
('s', "The authors called it preliminary. The abstract reports scar, not strength, and TGF-beta has many lawful jobs in the body.", "作者自己称之为初步结果。摘要报告的是瘢痕，不是肌力；而且 TGF-β 在体内还有许多正当的工作。"),
('s', "Shut that switch too hard, or for too long, and you may disturb healing elsewhere. Any human use would need careful testing.", "把这个开关关得太狠、太久，可能扰乱别处的愈合。任何人体应用都需要谨慎检验。"),
('v', 'cells', 0), ('r', 'Li 2025 Front Cell Dev Biol'),
('s', "Then cell therapy. In 2025, Li and colleagues transplanted adipose-derived stem cells into the ninety-gray rat model.", "然后是细胞治疗。2025 年，Li 等人把脂肪来源干细胞移植进 90 Gy 的大鼠模型。"),
('s', "Fibrosis eased over time, and satellite cell activation increased.", "纤维化随时间减轻，卫星细胞的激活增加。"),
('v', 'cells', 1),
('s', "It is one group, one model, and groups of six rats. Promising, but early.", "这只是一个团队、一个模型，每组六只大鼠。有希望，但还很早。"),
('s', "And remember the conflicting clue: this rat model already shows activated satellite cells, so it may not predict the depleted juvenile mouse.", "还要记住那条矛盾的线索：这个大鼠模型本身就显示卫星细胞被激活，所以它未必能预测干细胞耗竭的幼年小鼠。"),
('v', 'exercise', 0), ('r', "O'Connor 2022 Skelet Muscle; Collao 2023 JCSM 14:781"),
('s', "And finally, the oldest medicine of all: exercise.", "最后，是最古老的药：运动。"),
('s', "In juvenile irradiated mice, voluntary wheel running improved fast-muscle specific force by thirty-seven percent, and cut mitochondrial reactive oxygen species by half.", "在幼年受照小鼠里，自主跑轮使快肌的比肌力提高了 37%，并让线粒体活性氧减少了一半。"),
('v', 'exercise', 1),
('s', "In a model of childhood rhabdomyosarcoma treated with chemotherapy and radiation, resistance and endurance training preserved muscle mass, and calmed inflammatory and fibrotic genes.", "在接受放化疗的儿童横纹肌肉瘤模型里，抗阻加耐力训练保住了肌肉量，也平息了炎症和纤维化基因。"),
('s', "The trained limbs also held more endothelial cells, a hint that the supply lines were being rebuilt.", "训练过的受照肢体里内皮细胞也更多，这提示补给线可能正在被重建。"),
('v', 'exercise', 2),
('s', "But it did not prevent the fibrosis itself.", "但它没能阻止纤维化本身。"),
('s', "So exercise may rebuild the house without clearing the scar. These are mouse results: reasons to study exercise in survivors, not proof.", "所以运动也许能把房子重建起来，却清不掉瘢痕。这些是小鼠结果：是在幸存者中研究运动的理由，而不是证明。"),
('v', 'bench', 2), ('r', 'Gans 2021; Li 2025'), ('e', 'BENCH'),
('s', "A note from the bench, about trust.", "一段实验台笔记，关于可信度。"),
('s', "Gans's team scored fibrosis blinded. Copy that: whoever reads the slides should not know which group they came from.", "Gans 团队是盲法评估纤维化的。照着做：读片的人不应知道切片来自哪一组。"),
('s', "Small groups of six or seven animals can miss real effects and exaggerate lucky ones. Calculate your sample size before you begin, from a realistic effect.", "每组六七只动物，可能漏掉真实效应，也可能夸大侥幸结果。开始之前，就要按现实的效应量计算样本量。"),
('s', "And report every animal lost. In Gans's study, three of ten treated mice did not reach analysis, and the paper says so.", "还要报告每一只损失的动物。在 Gans 的研究里，治疗组十只中有三只没能进入分析，论文如实写明了。"),

('sec', "5  Cold cases and the summation", "五  悬案与结案陈词"),
('v', 'coldcases', 0), ('r', 'Collao 2023; Collao 2025 Am J Physiol Cell Physiol; Ness 2015'), ('e', 'HYPOTHESIS'),
('s', "Now to the cold cases, the files still open on my desk.", "现在来看悬案，那些仍摊在我桌上的卷宗。"),
('s', "First, senolytics, drugs designed to clear senescent cells.", "第一，衰老细胞清除剂，一类专门用来清除衰老细胞的药物。"),
('s', "We know senescence appears in irradiated muscle: senescent FAPs, and a p21 signature in every resident cell type.", "我们知道受照肌肉里出现了衰老：衰老的 FAPs，以及所有驻留细胞类型中都有的 p21 特征。"),
('s', "But I found no study that clears those cells in irradiated muscle of a living animal. That experiment is waiting for someone.", "但我没有找到任何在活体动物受照肌肉里清除这些细胞的研究。这个实验正在等人来做。"),
('v', 'coldcases', 1), ('r', 'Arnold 2007 J Exp Med; Collao 2025'),
('s', "Second, the macrophage time course.", "第二，巨噬细胞的时间进程。"),
('s', "In ordinary injury, inflammatory monocytes arrive first and then turn into healing macrophages. After radiation, I found no day-by-day map in muscle. We infer it from other injuries.", "在普通损伤里，炎性单核细胞先到，再转变为促修复的巨噬细胞。可在照射后的肌肉里，我没有找到逐日的时间图谱，只能从其他损伤去推断。"),
('v', 'coldcases', 2), ('r', 'Paris 2001 Science; Collao 2023'),
('s', "Third, who falls first, the vessels or the stem cells?", "第三，谁先倒下：血管，还是干细胞？"),
('s', "In the mouse intestine, Paris and colleagues argued that endothelial death comes first. In muscle, we see fewer endothelial cells at fifty-six days, but not which came first.", "在小鼠肠道里，Paris 等人认为内皮细胞死亡在先。在肌肉里，我们看到第 56 天内皮细胞减少，却看不出谁先谁后。"),
('v', 'coldcases', 3), ('r', 'Heslop 2000 J Cell Sci; Wernig 2000 J Physiol; Zhang 2025'),
('s', "Fourth, injuring irradiated muscle with cardiotoxin or barium chloride, today's standard test of regeneration.", "第四，用心脏毒素或氯化钡损伤受照肌肉——这是如今检验再生的标准方法。"),
('s', "Older work used notexin or freezing injury. For the modern version, I could not confirm a reliable report.", "早年的研究用的是诺蛇毒素或冷冻损伤；至于现代版本，我没能确认到可靠的报告。"),
('s', "And fifth, if tumor vesicles can carry harm to muscle, could engineered vesicles carry help? I found no such therapy tested in irradiated muscle.", "第五，既然肿瘤囊泡能把伤害送到肌肉，人工改造的囊泡能不能把帮助送过去？我没有找到在受照肌肉里测试过的此类疗法。"),
('s', "Five open files. Each one could be a thesis.", "五份未结的卷宗，每一份都可能成为一篇博士论文。"),
('v', 'bench', 3), ('r', "O'Connor 2022; Kallenbach 2022; Bachman 2020"), ('e', 'BENCH'),
('s', "A last note from the bench.", "最后一段实验台笔记。"),
('s', "Measure force whenever you can: in the living animal, or in an isolated muscle stimulated in a bath, dividing force by cross-sectional area to get specific force.", "只要能测，就测肌力：可以在活体动物上测，也可以把离体肌肉放在浴槽中电刺激，用力除以横截面积得到比肌力。"),
('s', "A muscle can look small yet be strong for its size, or look normal and be weak. Only force tells you which.", "一块肌肉可能看着小，按体积算却很有力；也可能看着正常，却很无力。只有肌力能告诉你是哪种。"),
('s', "And choose timepoints by biology: one early for damage and cell death, one at weeks for remodeling, and one months later for the lasting deficit.", "时间点要按生物学来选：早期一个看损伤和细胞死亡，几周一个看重塑，几个月后再一个看持久的缺陷。"),
('v', 'verdict', 0), ('r', 'Episodes 1-4 references'), ('e', ''),
('s', "My friends, it is time for the summation.", "朋友们，到了结案陈词的时候。"),
('s', "Here is the chain, from the beam to the stiff muscle, link by link, with its evidence.", "这是从射线到僵硬肌肉的证据链，一环接一环，各附证据。"),
('v', 'verdict', 1), ('e', 'FACT'),
('s', "Radiation breaks DNA. That is fact.", "射线打断 DNA。这是事实。"),
('s', "The mature fiber resists death, while its precursors are more vulnerable. Fact, in cells.", "成熟的纤维抵抗死亡，而它的前体细胞更脆弱。事实，在细胞层面。"),
('s', "Satellite cells are lost, especially in growing muscle, and fibers stay smaller for life. Fact, in mice.", "卫星细胞丢失，尤其在生长中的肌肉里，纤维终生偏小。事实，在小鼠身上。"),
('v', 'verdict', 2), ('e', 'HYPOTHESIS'),
('s', "FAPs turn senescent and fibrogenic. That is fact in mice. That macrophage TGF-beta drives them is inferred from sequencing.", "FAPs 变得衰老、促纤维化，这在小鼠中是事实；巨噬细胞的 TGF-β 驱动它们，则是从测序中推断的。"),
('s', "Vessels thin and mitochondria falter. Fact in animals. Whether they lead or follow is still hypothesis.", "血管变稀，线粒体失灵，这在动物中是事实；它们是带头者还是跟随者，仍是假说。"),
('v', 'verdict', 3), ('e', 'ASSOCIATION'),
('s', "And in people, late weakness, dysphagia, and sarcopenia follow radiotherapy. That is association, consistent, but not yet traced cell by cell.", "在人身上，晚期无力、吞咽困难和肌少症跟随放疗而来。这是关联，前后一致，却还没有一个细胞一个细胞地追查清楚。"),
('s', "So the verdict is not a single culprit.", "所以，判决不是一个单独的罪犯。"),
('s', "It is a conspiracy: a lost guardian, a turned neighbor, a broken supply line, and perhaps a message from the tumor itself.", "而是一场合谋：失去的守护者、变脸的邻居、断掉的补给线，也许还有肿瘤亲自发出的一封信。"),
('v', 'sendoff', 0), ('r', ''), ('e', ''),
('s', "Some of you watching are just beginning in the laboratory.", "看这个节目的你们，有些人刚刚走进实验室。"),
('s', "You may feel the big discoveries are already made. Look at the cold cases again. They are not.", "你也许觉得，重大的发现都已经被别人做完了。再看看那些悬案吧，并没有。"),
('v', 'sendoff', 1),
('s', "Ask what dose, in what animal, and over how long. Shield the leg, blind the count, measure the force, and tag your evidence honestly.", "问清多大剂量、什么动物、多长时间。遮挡对侧腿，盲法计数，测量肌力，诚实地给证据贴标签。"),
('s', "The patient who cannot climb the stairs, and the survivor who cannot swallow, are waiting for what you will find.", "那位爬不动楼梯的病人，那位咽不下饭的幸存者，都在等待你的发现。"),
('s', "The case is not closed. It is handed to you.", "这个案子没有结案。它交到了你的手里。"),
('s', "Thank you, my friends, for following the evidence with me.", "朋友们，谢谢你们和我一起追随证据。"),
('v', 'refs', 0), ('r', ''), ('e', ''),
('s', "The references for this episode are on the screen.", "本集的参考文献，都在屏幕上。"),
]

REFS = [
"Stubblefield MD. PM R 2011;3:1041-1054. doi:10.1016/j.pmrj.2011.08.535",
"Fijardo M, et al. EBioMedicine 2024;103:105089. doi:10.1016/j.ebiom.2024.105089",
"Hutcheson KA, et al. Cancer 2012;118:5793-5799. doi:10.1002/cncr.27631",
"McCastlain K, et al. J Natl Cancer Inst 2021;113:1570-1580. doi:10.1093/jnci/djab084",
"Ness KK, et al. Cancer 2015;121:1540-1547. doi:10.1002/cncr.29211",
"Jiang Y, et al. BBA Mol Cell Res 2024;1871:119792. doi:10.1016/j.bbamcr.2024.119792",
"Collao N, et al. J Cachexia Sarcopenia Muscle 2023;14:2335-2349. doi:10.1002/jcsm.13320",
"Kallenbach JG, et al. J Cachexia Sarcopenia Muscle 2022;13:296-310. doi:10.1002/jcsm.12902",
"Bachman JF, et al. iScience 2020;23:101760. doi:10.1016/j.isci.2020.101760",
"Collao N, et al. Am J Physiol Cell Physiol 2025;328:C1995-C2012. doi:10.1152/ajpcell.00115.2025",
"O'Connor TN, et al. Skelet Muscle 2022;12:8. doi:10.1186/s13395-022-00291-y",
"Hardee JP, et al. Radiol Oncol 2014;48:247-256. doi:10.2478/raon-2014-0025",
"Zhou Y, et al. Radiat Oncol 2018;13:160. doi:10.1186/s13014-018-1104-0",
"Zeng X, et al. Radiat Res 2022;197:638-649. doi:10.1667/RADE-21-00183.1",
"Zhang X, et al. Cell Metab 2025;37:1766-1782.e12. doi:10.1016/j.cmet.2025.05.013",
"Delanian S, et al. J Clin Oncol 2003;21:2545-2550. doi:10.1200/JCO.2003.06.064",
"Delanian SE, et al. Int J Radiat Oncol Biol Phys 2020;107:154-162. doi:10.1016/j.ijrobp.2020.01.002",
"Gans I, et al. Clin Orthop Relat Res 2021;479:468-474. doi:10.1097/CORR.0000000000001286",
"Martin M, et al. Int J Radiat Oncol Biol Phys 2000;47:277-290. doi:10.1016/s0360-3016(00)00435-1",
"Li S, et al. Front Cell Dev Biol 2025;13:1620998. doi:10.3389/fcell.2025.1620998",
"Collao N, et al. J Cachexia Sarcopenia Muscle 2023;14:781-793. doi:10.1002/jcsm.13185",
"Arnold L, et al. J Exp Med 2007;204:1057-1069. doi:10.1084/jem.20070075",
"Paris F, et al. Science 2001;293:293-297. doi:10.1126/science.1060191",
"Heslop L, et al. J Cell Sci 2000;113:2299-2308. doi:10.1242/jcs.113.12.2299",
"Wernig A, et al. J Physiol 2000;522:333-345. doi:10.1111/j.1469-7793.2000.t01-2-00333.x",
]

# What each diagram shows at each step. Steps build progressively (each step adds to the previous).
VIS = {
'title': "0: Series title card 'After the Beam / 射线之后', episode line 'Episode 4 · From Bench to Bedside / 第4集 · 从实验台到病床'; faint beam line ending at a hospital bed silhouette.",
'case4': (
    "Recap evidence board, four pinned cards joined by red string, left to right. "
    "0: card 1 'Beam → DNA breaks / 射线→DNA断裂' (broken helix icon); fiber icon with shield 'fiber survives / 纤维存活'. "
    "1: + card 2 'Satellite cells lost / 卫星细胞丢失' (fading PAX7 dots under a fiber; small child silhouette 'lifelong / 终生'). "
    "2: + card 3 'FAPs senescent → scar / FAPs衰老→瘢痕' (blue collagen strands, TGF-β arrow) and small icons 'vessels thin / 血管变稀', 'mitochondria falter / 线粒体失灵'. "
    "3: + string runs off-board to a door labelled 'Clinic / 诊室' with a question mark; caption 'working model, built in mice / 工作模型，来自小鼠'."),
'rfs': (
    "Body outline (front view, neck and shoulder emphasised) for radiation fibrosis syndrome. "
    "0: shaded RT field over neck; title 'Radiation fibrosis syndrome / 放射纤维化综合征'; caption 'progressive tissue hardening / 进行性组织硬化'. "
    "1: chain of five linked labels along the cord → nerve → muscle: 'myelo 脊髓 · radiculo 神经根 · plexo 神经丛 · neuro 神经 · myopathy 肌病'; note 'weak = muscle? nerve? both? / 无力：肌肉？神经？两者？'. "
    "2: + jaw with arrow blocked 'trismus / 牙关紧闭' and neck twisted 'cervical dystonia / 颈部肌张力障碍'; ref tag 'Stubblefield 2011 · Fijardo 2024'."),
'swallow': (
    "Sagittal head-and-neck schematic (tongue, pharynx, larynx, trachea, oesophagus) with bolus. "
    "0: header 'n = 29 survivors · ≥5 y after RT · median 9 y / 29位幸存者 · 放疗后≥5年 · 中位9年'; MD Anderson 2012. "
    "1: bolus residue in pharynx and a drop entering trachea, red: 'residue + aspiration: 100% / 残留+误吸：全部'; small jaw icon 'trismus 38% / 牙关紧闭 38%'. "
    "2: two bar/icon rows: lung icon 'pneumonia 86% (half hospitalised) / 肺炎 86%（半数住院）', feeding tube icon 'gastrostomy-dependent 66% / 依赖胃造瘘 66%'. "
    "3: timeline arrow 'RT → years → dysphagia may appear or worsen / 放疗→数年→吞咽困难出现或加重'; caveat stamp 'referred case series, not prevalence / 转诊病例系列，非患病率'."),
'survivor': (
    "Cohort graphic: grid of 100 small person icons. "
    "0: header 'St. Jude Lifetime · n = 1,762 · median age 29 · ~20 y after diagnosis / 1762人 · 中位29岁 · 诊断后约20年'; 27 of 100 icons coloured amber 'sarcopenia 27% / 肌少症 27%' (low lean mass or weak grip). "
    "1: + odds bar 'cranial RT OR 1.84 / 头颅放疗 OR 1.84'; blood drop with mtDNA circles 'lower mtDNA copy number ↔ sarcopenia / mtDNA拷贝数低↔肌少症'; amber tag 'ASSOCIATION, cross-sectional / 关联，横断面'. "
    "2: young adult silhouette with cane shadow 'frailty in young survivors / 年轻幸存者衰弱'; three suspect cards 'senescence 衰老 · sterile inflammation 无菌炎症 · mitochondria 线粒体' stamped red 'HYPOTHESIS / 假说' (Ness 2015)."),
'biopsy': (
    "0: microscope slide box labelled 'Human muscle biopsies after RT / 放疗后人体肌肉活检' with the lid opening. "
    "1: box is nearly empty (one or two slides), sticky note 'few good series found / 未找到像样的系列'; arrow to two full boxes 'mice 小鼠' and 'dishes 培养皿'; caption 'gap = invitation / 空白=邀请'."),
'models': (
    "Model 'zoo' as a 2×2 card grid that fills in. "
    "0: empty grid titled 'Choose your model / 选择模型'. "
    "1: card A 'single dose vs fractionated / 单次 vs 分次' (one big lightning bolt vs three small); card B 'juvenile vs adult / 幼年 vs 成年' (small vs large mouse). "
    "2: card C 'mouse vs rat / 小鼠 vs 大鼠' with icons 'genetics, scRNA-seq / 遗传工具、单细胞' vs 'very high-dose fibrosis / 超高剂量纤维化'; small tumour badge 'juvenile RMS + RT / 幼年横纹肌肉瘤+放疗'. "
    "3: card D 'in vitro: cells & human organoids / 体外：细胞与人类类器官' with crossed-out icons 'no vessels 无血管 · no immune cells 无免疫 · no years 无长期'."),
'doses': (
    "Vertical dose ladder on a log scale (1 to 100 Gy), rungs light up one by one with model icons. "
    "0: rung '2 Gy · human organoid (Jiang 2024) / 人类类器官'. "
    "1: + '16 Gy single · juvenile mouse (Collao 2023) / 幼年小鼠单次' and '3 × 8.2 Gy · juvenile mouse (Rochester) / 幼年小鼠分3次'. "
    "2: + '50 Gy single · adult mouse (Gans 2021) / 成年小鼠单次'. "
    "3: + '90 Gy single · rat (Zhou 2018, Zeng 2022) / 大鼠单次'; bracket '45× range — different worlds / 相差45倍——不同的世界'."),
'readouts': (
    "Four-panel readout dashboard filling clockwise. "
    "0: Masson trichrome cartoon section, blue collagen between red fibers, '% blue area = fibrosis / 蓝色面积%=纤维化'. "
    "1: + fiber cross-sections with ruler 'CSA 横截面积', scale 'muscle mass 肌重'; PAX7 green nuclei 'SC count 卫星细胞计数'; γH2AX dots 'DNA damage 损伤'. "
    "2: + flow-cytometry dot plot with gates 'FAPs · ECs · immune / FAPs·内皮·免疫'; scRNA-seq UMAP blob cluster 'single-cell 单细胞'. "
    "3: + force trace (twitch/tetanus curve) 'specific force −27% (EDL, O'Connor 2022) / 比肌力 −27%', marked 'most patient-relevant / 最贴近病人'."),
'timeline4': (
    "Mouse with two hind legs plus horizontal time axis. "
    "0: right leg in beam, left leg behind lead shield 'shielded contralateral control / 遮挡对侧对照'; faint dashed arrows from blood to the shielded leg '? circulating signals / ？循环信号'; extra cage 'unirradiated control / 未照射对照'. "
    "1: axis with ticks '24 h · d3 · d7 · d14 · d56 (Collao 2023/2025)'. "
    "2: axis extends with break to '14 months (Rochester) / 14个月'; bands 'early = injury / 早期=损伤' and 'late = disease / 晚期=疾病'."),
'bench': (
    "Lab-notebook card; title + up to 4 rows (EN | ZH). "
    "0: title 'Study design checklist / 研究设计清单'; rows: 'question + primary outcome + timepoint | 问题+主要结局+时间点'; 'randomize; record strain, sex, age, weight | 随机分组；记录品系、性别、年龄、体重'; 'shielded leg + unirradiated + vehicle | 遮挡腿+未照射+溶媒对照'; 'age matters: 4 wk vs 12 wk | 年龄很关键：4周 vs 12周'. "
    "1: title 'Dose reporting & BED / 剂量报告与BED'; rows: 'machine, energy, dose rate, field, shielding | 机器、能量、剂量率、照射野、遮挡'; 'verify dose (dosimetry) | 剂量核实'; '4×4 Gy → BED 37; 16 Gy → BED ~100 | 4×4 Gy→BED 37；16 Gy→约100'; 'extreme single doses: formula less reliable | 极端单次剂量：公式不可靠'. "
    "2: title 'Blinding & sample size / 盲法与样本量'; rows: 'blind slide scoring | 盲法读片'; 'power calculation before start | 事先计算样本量'; 'n = 6–7 per group: fragile | 每组6–7只：脆弱'; 'report every animal lost (3/10) | 报告每只损失动物（3/10）'. "
    "3: title 'Force & timepoints / 肌力与时间点'; rows: 'in vivo or ex vivo force | 在体或离体测力'; 'specific force = force ÷ CSA | 比肌力=力÷横截面积'; 'early: damage, death | 早期：损伤、死亡'; 'weeks: remodeling; months: lasting deficit | 几周：重塑；几个月：持久缺陷'."),
'conflict': (
    "Courtroom: two witness stands, rat on left, mouse on right, balance scale in the middle. "
    "0: rat stand '90 Gy single · SCs ↑ activated (Zeng 2022); Pax7/MyoD ↑ ~wk 4 (Zhou 2018) / 90 Gy · 卫星细胞↑'. "
    "1: + mouse stand 'juvenile · SCs ↓ 45% (Kallenbach 2022); ↓ d3 & d56 (Collao 2023) / 幼年 · 卫星细胞↓'; scale tips; '?' over judge. "
    "2: four comparison rows between stands: 'species 物种: rat 大鼠 | mouse 小鼠', 'dose 剂量: 90 Gy | 16 or 3×8.2 Gy', 'age 年龄: not juvenile 非幼年 | 4 wk 4周'. "
    "3: + row 'time 时间' drawn as a curve: early burst peak 'activation 激活' then decline 'depletion 耗竭'; red tag 'HYPOTHESIS: same story, different snapshots / 假说：同一故事，不同快照'; footnote 'test: same species, matched dose, many timepoints / 检验：同物种、匹配剂量、多时间点'."),
'tumorev': (
    "Two-organ map: tumour (left) — bloodstream — muscle (right). "
    "0: beam hits muscle only, caption 'assumed: local crime / 原假设：现场作案'. "
    "1: beam also hits tumour; inside cancer cell 'arachidonic acid ↑ / 花生四烯酸↑' → 'SRM (spermidine synthase) packed into small EVs / SRM装入小囊泡'. "
    "2: EV bubbles travel through vessel to muscle; in muscle 'spermidine ↑ → eIF5A → type I collagen / 亚精胺↑→eIF5A→I型胶原', fibers stiffen. "
    "3: losartan pill blocks EV export at tumour (red X) 'losartan blocks SRM export (mouse) / 氯沙坦阻断（小鼠）'; tag 'Zhang 2025 Cell Metab · awaits human data / 待人体验证'."),
'ptx': (
    "Lock icon at top 'Picking the lock / 撬锁'; trial bar chart below. "
    "0: two pills 'pentoxifylline 己酮可可碱' + 'vitamin E 维生素E'. "
    "1: bars for 2003 RCT (n = 24 women, breast RT, 6 months): 'PTX+VitE 60% regression' vs 'placebo 43%'; small greyed bars 'either alone: ineffective / 单用无效'. "
    "2: + label 'superficial fibrosis, not deep muscle / 浅表纤维化，非深部肌肉'; second panel '2020 RCT · + clodronate · plexopathy · 18 mo → no benefit / 2020 · 加氯膦酸盐 · 神经丛病 · 无获益' (flat bars); verdict chip 'mixed evidence / 证据混合'."),
'tgfb': (
    "Mouse hindlimb + master switch icon labelled 'TGF-β'. "
    "0: '50 Gy single, right hindlimb, 12-wk C57BL/6 → daily TGF-β inhibitor × 8 wk / 50 Gy单次 → 每日抑制剂×8周'; switch being turned down. "
    "1: bar chart at 9 months, quadriceps fibrosis: 'RT only 1.2%' vs 'RT + inhibitor 0.14%' vs 'no RT 0.05%'. "
    "2: caveat chips 'preliminary 初步', 'scar not strength / 测瘢痕未测肌力', 'TGF-β has normal jobs / TGF-β有正常功能'."),
'cells': (
    "0: syringe of 'adipose-derived stem cells (ADSCs) / 脂肪来源干细胞' into irradiated rat thigh '90 Gy rat model'; arrows 'fibrosis ↓ · SC activation ↑ / 纤维化↓ · 卫星细胞激活↑'. "
    "1: caveat card 'one group · one model · n = 6 / 一个团队 · 一个模型 · 每组6只'; chip 'promising, early / 有希望，尚早'."),
'exercise': (
    "Running wheel with mouse. "
    "0: juvenile irradiated mouse on wheel; gauges 'specific force +37% (EDL) / 比肌力 +37%' and 'mito ROS −50% / 线粒体ROS −50%' (O'Connor 2022). "
    "1: second panel: dumbbell + treadmill 'RMS + chemo-RT model' with ticks 'muscle mass ✓ 肌量', 'inflammatory/fibrotic genes ✓ 炎症/纤维化基因'. "
    "2: + red cross 'fibrosis not prevented ✗ / 纤维化未被阻止'; caption 'mouse data — test in survivors / 小鼠数据——需在幸存者中检验'."),
'coldcases': (
    "Filing cabinet with case folders pulled out one per step, each stamped 'OPEN / 未结'. "
    "0: folder 1 'Senolytics in irradiated muscle — untested in vivo / 受照肌肉中的衰老清除剂——尚无活体研究' (senescent FAP with p21 badge). "
    "1: + folder 2 'Macrophage time course after RT — unmapped / 照射后巨噬细胞时程——未绘制' (empty day-by-day timeline). "
    "2: + folder 3 'Vessels or stem cells first? / 血管还是干细胞先倒下？' (capillary and PAX7 cell racing; note 'vessel-first shown in intestine / 血管先行见于肠道'). "
    "3: + folder 4 'CTX / BaCl₂ injury after RT — not confirmed / 照射后CTX/BaCl₂损伤——未确认' and folder 5 'EV therapy in irradiated muscle — none / 受照肌肉囊泡治疗——空白'; caption 'each = a thesis / 每份=一篇论文'."),
'verdict': (
    "Final evidence chain, horizontal, links appear with coloured tags (green FACT, amber ASSOCIATION, red HYPOTHESIS). "
    "0: empty chain from beam icon to stiff muscle icon; title 'Summation / 结案陈词'. "
    "1: links 'DNA breaks 断裂 [FACT]', 'fiber survives, precursors vulnerable 纤维存活，前体脆弱 [FACT, cells]', 'SC loss → small fibers for life 卫星细胞丢失→终生偏小 [FACT, mice]'. "
    "2: + 'FAPs senescent, fibrogenic 衰老促纤维化 [FACT, mice]' with sub-tag 'macrophage TGF-β 巨噬细胞TGF-β [inferred, scRNA-seq]'; 'vessels ↓, mitochondria ↓ 血管↓线粒体↓ [FACT animals; order = HYPOTHESIS]'. "
    "3: + 'human late weakness, dysphagia, sarcopenia 人体晚期无力/吞咽困难/肌少症 [ASSOCIATION]'; dotted side-link from tumour 'tumour EVs? 肿瘤囊泡？'; banner 'not one culprit — a conspiracy / 不是单一罪犯——是合谋'."),
'sendoff': (
    "0: young researcher at a bench at dawn, open notebook, cold-case folders beside the microscope; caption 'The case is open / 案子仍未结'. "
    "1: four checklist lines appear on the notebook 'dose · animal · duration / 剂量·动物·时长', 'shield the leg / 遮挡对侧', 'blind the count / 盲法计数', 'measure force · tag evidence / 测肌力·标证据'; final line 'handed to you / 交给你'."),
'refs': "0: Reference list (REFS, 25 entries; may need two columns or smaller font).",
}
