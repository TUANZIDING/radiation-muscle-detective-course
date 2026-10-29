# Radiation injury to skeletal muscle: literature check for the 4-episode story series (v0.1)

Checked 2026-10-28 against Crossref (api.crossref.org/works/{doi}) and PubMed E-utilities (esearch `{doi}[doi]` → PMID; efetch abstracts).
Every item below has a DOI that resolves in Crossref and a PMID that maps back to it.
The key findings come from the PubMed abstracts I read, unless marked *(full text)*, which means it is general knowledge to confirm in the full paper before narrating.

Abbreviations: SC/MuSC = satellite cell / muscle stem cell; FAP = fibro-adipogenic progenitor; IR = irradiation; DSB = double-strand break; DDR = DNA damage response; TA = tibialis anterior; EDL = extensor digitorum longus.

---

## Part A. The 12 references you gave me

| # | Verified citation | DOI | PMID | Status |
|---|---|---|---|---|
| 1 | Ward JF. The yield of DNA double-strand breaks produced intracellularly by ionizing radiation: a review. *Int J Radiat Biol* 1990;57(6):1141-1150 | 10.1080/09553009014551251 | 1971840 | ✅ OK |
| 2 | Jackson SP, Bartek J. The DNA-damage response in human biology and disease. *Nature* 2009;461:1071-1078 | 10.1038/nature08467 | 19847258 | ✅ OK |
| 3 | Heslop L, Morgan JE, Partridge TA. Evidence for a myogenic stem cell that is exhausted in dystrophic muscle. *J Cell Sci* 2000;113(12):2299-2308 | 10.1242/jcs.113.12.2299 | 10825301 | ✅ OK. Note: the title does not mention radiation, but the whole study uses 18 Gy and 25 Gy local IR plus notexin injury |
| 4 | Vahidi Ferdousi L, et al. More efficient repair of DNA double-strand breaks in skeletal muscle stem cells compared to their committed progeny. *Stem Cell Res* 2014;13(3 Pt A):492-507 | 10.1016/j.scr.2014.08.005 | 25262445 | ✅ OK |
| 5 | Boldrin L, Neal A, Zammit PS, Muntoni F, Morgan JE. Donor satellite cell engraftment is significantly augmented when the host niche is preserved and endogenous satellite cells are incapacitated. *Stem Cells* 2012;30(9):1971-1984 | 10.1002/stem.1158 | 22730231 | ✅ Metadata OK. The abstract says "incapacitation" of host SCs but does not name the method. Check in the full text that this was done by irradiation before saying so on air |
| 6 | Bachman JF, et al. Radiation-induced damage to prepubertal Pax7+ skeletal muscle stem cells drives lifelong deficits in myofiber size and nuclear number. *iScience* 2020;23(11):101760 | 10.1016/j.isci.2020.101760 | 33241204 | ✅ OK |
| 7 | Collao N, et al. Radiation induces long-term muscle fibrosis and promotes a fibrotic phenotype in fibro-adipogenic progenitors. *J Cachexia Sarcopenia Muscle* 2023;14(5):2335-2349 | 10.1002/jcsm.13320 | 37671686 | ✅ OK |
| 8 | Collao N, Johannsen EB, Just J, De Lisio M. Single-cell transcriptomic analysis reveals alterations to cellular dynamics and paracrine signaling in radiation-induced muscle pathology. *Am J Physiol Cell Physiol* 2025;328(6):C1995-C2012 | 10.1152/ajpcell.00115.2025 | 40316295 | ✅ OK |
| 9 | Martin M, Lefaix JL, Delanian S. TGF-β1 and radiation fibrosis: a master switch and a specific therapeutic target? *Int J Radiat Oncol Biol Phys* 2000;47(2):277-290 | 10.1016/s0360-3016(00)00435-1 | 10802350 | ✅ OK |
| 10 | Fijardo M, Kwan JYY, Bissey PA, Citrin DE, Yip KW, Liu FF. The clinical manifestations and molecular pathogenesis of radiation fibrosis. *EBioMedicine* 2024;**103**:105089 | 10.1016/j.ebiom.2024.105089 | 38579363 | ⚠️ **Mismatch: the volume is 103, not 102** (May 2024 issue). DOI and article number are correct |
| 11 | Bentzen SM. Preventing or reducing late side effects of radiation therapy: radiobiology meets molecular pathology. *Nat Rev Cancer* 2006;6(9):702-713 | 10.1038/nrc1950 | 16929324 | ✅ OK |
| 12 | Venkatesulu BP, et al. Radiation-induced endothelial vascular injury: a review of possible mechanisms. *JACC Basic Transl Sci* 2018;3(4):563-572 | 10.1016/j.jacbts.2018.01.014 | 30175280 | ✅ OK |

Key findings of the given papers that matter for the story:
- **Vahidi Ferdousi 2014**: quiescent SCs repair radiation-induced DSBs faster and more accurately than their committed progeny, using DNA-PKcs-dependent NHEJ. They also undergo less apoptosis. Post-mitotic myonuclei repair much less efficiently. Repair capacity tracks differentiation more than proliferation.
- **Heslop 2000** (mouse, 18 and 25 Gy): after IR, muscle does not regenerate. A radiation-resistant reserve of myogenic cells survives 18 Gy and can be "woken up" by severe notexin damage. That reserve is depleted in mdx muscle.
- **Bachman 2020** (juvenile mouse, fractionated local hindlimb IR on SARRP): immediate SC loss, then smaller fibres and fewer myonuclei 14 months later. Genetic SC depletion before puberty reproduces this.
- **Collao 2023** (4-week-old mice, single 16 Gy to one hindlimb, contralateral limb shielded as control; days 3/7/14/56): fibrosis by day 56; fewer SCs (days 3 and 56), endothelial cells and FAPs (day 56); FAPs become senescent, fibrogenic and glycolytic; their secretome impairs SC differentiation and fusion.
- **Collao 2025** (scRNA-seq at 24 h and 56 d post-IR): deep-quiescent MuSCs are relatively depleted long term. A senescence *Cdkn1a* (p21) signature appears in all resident cell types. FAPs are the main ECM source and the main target of monocyte/macrophage-derived TGF-β, acting via TGF-βR2.

---

## Part B. Added references (all DOI + PMID verified)

### B1. Episode 1: the bullet and the blueprint (physics → DSB → DDR → cell fate)
| Citation | DOI | PMID | Key finding (model) |
|---|---|---|---|
| Rogakou EP, et al. DNA double-stranded breaks induce histone H2AX phosphorylation on serine 139. *J Biol Chem* 1998;273(10):5858-5868 | 10.1074/jbc.273.10.5858 | 9488723 | Discovery of γH2AX, the "flare" marking each DSB. This is the foci readout used in almost every muscle IR paper *(full text)* |
| Lomax ME, Folkes LK, O'Neill P. Biological consequences of radiation-induced DNA damage: relevance to radiotherapy. *Clin Oncol* 2013;25(10):578-585 | 10.1016/j.clon.2013.06.007 | 23849504 | Review: direct vs indirect (hydroxyl radical) action, clustered/complex lesions. Good for the "water radiolysis" scene |
| Chang HHY, Pannunzio NR, Adachi N, Lieber MR. Non-homologous DNA end joining and alternative pathways to double-strand break repair. *Nat Rev Mol Cell Biol* 2017;18(8):495-506 | 10.1038/nrm.2017.48 | 28512351 | Review of NHEJ vs HR vs alt-EJ. Explains why non-dividing cells such as quiescent SCs and myonuclei rely on NHEJ |
| Coppé JP, et al. Senescence-associated secretory phenotypes reveal cell-nonautonomous functions of oncogenic RAS and the p53 tumor suppressor. *PLoS Biol* 2008;6(12):e301 | 10.1371/journal.pbio.0060301 | 19053174 | Defines the SASP: senescent cells secrete inflammatory factors that change their neighbours. Bridge from Ep1 cell fates to Ep3 |
| Latella L, Lukas J, Simone C, Puri PL, Bartek J. Differentiation-induced radioresistance in muscle cells. *Mol Cell Biol* 2004;24(14):6350-6361 | 10.1128/MCB.24.14.6350-6361.2004 | 15226436 | Mouse and human myoblasts vs myotubes, 10 Gy: both activate ATM, γH2AX and MRN, but myotubes block ATM→p53-Ser15/18 and do not undergo apoptosis. This explains why the fibre survives while its stem cells suffer |

### B2. Episode 2: the guardians (satellite cells)
| Citation | DOI | PMID | Key finding (model) |
|---|---|---|---|
| Mauro A. Satellite cell of skeletal muscle fibers. *J Biophys Biochem Cytol* 1961;9(2):493-495 | 10.1083/jcb.9.2.493 | 13768451 | The founding EM description of a mononuclear cell wedged between the fibre membrane and basal lamina. Frog muscle *(full text)* |
| Lepper C, Partridge TA, Fan CM. An absolute requirement for Pax7-positive satellite cells in acute injury-induced skeletal muscle regeneration. *Development* 2011;138(17):3639-3646 | 10.1242/dev.067595 | 21828092 | Genetic ablation of Pax7+ cells in mouse → regeneration fails after injury *(full text)* |
| Sambasivan R, et al. Pax7-expressing satellite cells are indispensable for adult skeletal muscle regeneration. *Development* 2011;138(17):3647-3656 | 10.1242/dev.067587 | 21828093 | Independent confirmation (diphtheria-toxin-receptor ablation) *(full text)* |
| Murphy MM, Lawson JA, Mathew SJ, Hutcheson DA, Kardon G. Satellite cells, connective tissue fibroblasts and their interactions are crucial for muscle regeneration. *Development* 2011;138(17):3625-3637 | 10.1242/dev.064162 | 21828091 | SC ablation abolishes regeneration. Fibroblast ablation also impairs it, which foreshadows the "neighbours" theme *(full text)* |
| Cheung TH, Rando TA. Molecular regulation of stem cell quiescence. *Nat Rev Mol Cell Biol* 2013;14(6):329-340 | 10.1038/nrm3591 | 23698583 | Review: quiescence is an actively maintained state, not sleep. Background for "deep quiescent" MuSCs |
| Caiozzo VJ, et al. The radiosensitivity of satellite cells: cell cycle regulation, apoptosis and oxidative stress. *Radiat Res* 2010;174(5):582-589 | 10.1667/RR2190.1 | 20726709 | γ-IR ≥5 Gy cut SC numbers by ≥70% (apoptosis plus cell-cycle block), with persistent ROS/RNS and reduced NO, which SC proliferation needs. Rat/mouse SC culture |
| Scaramozza A, et al. Lineage tracing reveals a subset of reserve muscle stem cells capable of clonal expansion under stress. *Cell Stem Cell* 2019;24(6):944-957.e5 | 10.1016/j.stem.2019.03.020 | 31006621 | Mx1-Cre lineage tracing (mouse): a rare Pax3-enriched, low-ROS, radiotolerant SC subset clonally expands and repopulates the niche after IR. A modern answer to Heslop's "reserve" |
| Kallenbach JG, et al. Muscle-specific functional deficits and lifelong fibrosis in response to paediatric radiotherapy and tumour elimination. *J Cachexia Sarcopenia Muscle* 2022;13(1):296-310 | 10.1002/jcsm.12902 | 34997696 | Juvenile mice, 3×8.2 Gy hindlimb (± rhabdomyosarcoma): at 8 weeks of age, −17% mass, −25% force, −45% SCs, −30% fibre CSA. At 16 months: lifelong fibrosis and atrophy, consistent with accelerated sarcopenia |

### B3. Episode 3: the neighbours turn (FAPs, macrophages, TGF-β, senescence, vessels, mitochondria)
| Citation | DOI | PMID | Key finding (model) |
|---|---|---|---|
| Joe AWB, et al. Muscle injury activates resident fibro/adipogenic progenitors that facilitate myogenesis. *Nat Cell Biol* 2010;12(2):153-163 | 10.1038/ncb2015 | 20081841 | Discovery of FAPs as helpful "builders" after injury (mouse) *(full text)* |
| Uezumi A, Fukada S, Yamamoto N, Takeda S, Tsuchida K. Mesenchymal progenitors distinct from satellite cells contribute to ectopic fat cell formation in skeletal muscle. *Nat Cell Biol* 2010;12(2):143-152 | 10.1038/ncb2014 | 20081842 | Same issue: PDGFRα+ mesenchymal progenitors are the source of fat in muscle, the "dark side" of FAPs *(full text)* |
| Arnold L, et al. Inflammatory monocytes recruited after skeletal muscle injury switch into antiinflammatory macrophages to support myogenesis. *J Exp Med* 2007;204(5):1057-1069 | 10.1084/jem.20070075 | 17485518 | Normal timeline: Ly6C+ inflammatory monocytes arrive, eat debris, then switch to anti-inflammatory macrophages that release TGF-β1 and drive differentiation. Depleting monocytes prevents regeneration (mouse, non-IR injury) |
| Lemos DR, et al. Nilotinib reduces muscle fibrosis in chronic muscle injury by promoting TNF-mediated apoptosis of fibro/adipogenic progenitors. *Nat Med* 2015;21(7):786-794 | 10.1038/nm.3869 | 26053624 | The "timing" rule: macrophage TNF normally kills surplus FAPs. When TGF-β1 dominates (chronic injury, mdx), FAPs survive and become matrix producers. Nilotinib reduced fibrosis (mouse, not IR) |
| Christov C, et al. Muscle satellite cells and endothelial cells: close neighbors and privileged partners. *Mol Biol Cell* 2007;18(4):1397-1409 | 10.1091/mbc.e06-08-0693 | 17287398 | SCs sit next to capillaries in mouse and human. Endothelial cells feed SC growth via IGF-1, HGF, bFGF, PDGF-BB and VEGF, so losing vessels means losing the niche |
| Paris F, et al. Endothelial apoptosis as the primary lesion initiating intestinal radiation damage in mice. *Science* 2001;293(5528):293-297 | 10.1126/science.1060191 | 11452123 | Classic "vessel-first" hypothesis: microvascular endothelial apoptosis (acid sphingomyelinase) precedes crypt stem-cell failure. **This is intestine, not muscle.** Use it as an analogy and a testable question |
| Zhou Y, et al. Radiation-induced muscle fibrosis rat model: establishment and valuation. *Radiat Oncol* 2018;13(1):160 | 10.1186/s13014-018-1104-0 | 30157899 | SD rats, single 65-90 Gy to the groin/rectus femoris: fibrosis and TGF-β1 rise over 1-8 weeks; EM shows swollen mitochondria, endothelial swelling, leaky vessels and perivascular fibrosis; a transient early myogenic gene rise (~week 4) |
| O'Connor TN, et al. Endurance exercise attenuates juvenile irradiation-induced skeletal muscle functional decline and mitochondrial stress. *Skelet Muscle* 2022;12(1):8 | 10.1186/s13395-022-00291-y | 35414122 | Juvenile mice, 3×8.2 Gy knee-to-foot: EDL specific force −27%, protein oxidation +73%, Ca²⁺ handling disrupted. Wheel running cut mitochondrial ROS by 50% and raised PGC-1α |
| Amorim NML, et al. Irradiation impairs mitochondrial function and skeletal muscle oxidative capacity: significance for metabolic complications in cancer survivors. *Metabolism* 2020;103:154025 | 10.1016/j.metabol.2019.154025 | 31765667 | Mice, 6 Gy (whole body): fewer oxidative fibres, lower mitochondrial enzyme activity, impaired fatty-acid oxidation and glucose uptake. Pax7-nGFP SCs keep the defect in culture. TBI-exposed childhood cancer survivors show a parallel lipid signature |

### B4. Episode 4: from bench to bedside (human evidence, methods, interventions)
| Citation | DOI | PMID | Key finding (model) |
|---|---|---|---|
| Stubblefield MD. Radiation fibrosis syndrome: neuromuscular and musculoskeletal complications in cancer survivors. *PM R* 2011;3(11):1041-1054 | 10.1016/j.pmrj.2011.08.535 | 22108231 | Clinical framework: "myelo-radiculo-plexo-neuro-myopathy"; trismus and cervical dystonia after head-neck RT. Review |
| Hutcheson KA, et al. Late dysphagia after radiotherapy-based treatment of head and neck cancer. *Cancer* 2012;118(23):5793-5799 | 10.1002/cncr.27631 | 23640737 | 29 head-neck survivors ≥5 years (median 9) after RT: aspiration in all, trismus 38%, pneumonia 86%, 66% gastrostomy-dependent. Shows the damage can appear or worsen years later |
| McCastlain K, et al. The association of mitochondrial copy number with sarcopenia in adult survivors of childhood cancer. *J Natl Cancer Inst* 2021;113(11):1570-1580 | 10.1093/jnci/djab084 | 33871611 | St. Jude Lifetime cohort, n=1762: sarcopenia prevalence 27%. Cranial RT OR 1.84. Lower blood mtDNA copy number is associated with sarcopenia (association only) |
| Gans I, El Abiad JM, James AW, Levin AS, Morris CD. Administration of TGF-ß inhibitor mitigates radiation-induced fibrosis in a mouse model. *Clin Orthop Relat Res* 2021;479(3):468-474 | 10.1097/CORR.0000000000001286 | 33252888 | C57BL/6, single 50 Gy right hindlimb, daily small-molecule TGF-β inhibitor for 8 weeks: quadriceps fibrosis 1.2% vs 0.14% at 9 months. Preliminary; Crossref dates the online version 2020 |
| Zhang X, et al. Arachidonic acid triggers spermidine synthase secretion from primary tumor to induce skeletal muscle weakness upon irradiation. *Cell Metab* 2025;37(8):1766-1782.e12 | 10.1016/j.cmet.2025.05.013 | 40541182 | 2025 plot twist: after IR, the *tumour* ships spermidine synthase in small EVs, which drives spermidine and type I collagen in muscle (eIF5A-dependent). Losartan blocks it (mouse). Muscle injury is not only local |
| Delanian S, Porcher R, Balla-Mekias S, Lefaix JL. Randomized, placebo-controlled trial of combined pentoxifylline and tocopherol for regression of superficial radiation-induced fibrosis. *J Clin Oncol* 2003;21(13):2545-2550 | 10.1200/JCO.2003.06.064 | 12829674 | Breast-cancer survivors (n=24, 2×2 factorial): PTX + vitamin E for 6 months gave 60% vs 43% regression of the fibrosis surface; either drug alone was ineffective |

---

## Part C. Supplementary verified references (optional depth, backup for Q&A)
| Citation | DOI | PMID | Use |
|---|---|---|---|
| Relaix F, Zammit PS. Satellite cells are essential for skeletal muscle regeneration: the cell on the edge returns centre stage. *Development* 2012;139(16):2845-2856 | 10.1242/dev.069088 | 22833472 | Beginner-friendly SC review (Ep2) |
| Paris ND, et al. Chemoradiation impairs myofiber hypertrophic growth in a pediatric tumor model. *Sci Rep* 2020;10:19501 | 10.1038/s41598-020-75913-w | 33177579 | Juvenile rhabdomyosarcoma mouse model, 3×8.2 Gy or 5×4.8 Gy + vincristine: hypertrophic growth blocked (Ep2/Ep4 model) |
| Hardee JP, et al. The effect of radiation dose on mouse skeletal muscle remodeling. *Radiol Oncol* 2014;48(3):247-256 | 10.2478/raon-2014-0025 | 25177239 | 4×4 Gy (BED 37) vs 16 Gy single dose (BED 100): dose and fractionation change remodelling, ECM and 4-HNE (oxidative marker). Good for explaining fractionation and BED (Ep1/Ep4) |
| Zeng X, et al. Satellite cells are activated in a rat model of radiation-induced muscle fibrosis. *Radiat Res* 2022;197(6):638-649 | 10.1667/RADE-21-00183.1 | 35294551 | 90 Gy rat, 1-24 weeks: rising fibrosis, apoptosis, autophagy, IL-1β; SC numbers *increase*. This contrasts with the mouse SC-loss data. Model and dose matter (Ep4 "conflicting clues") |
| King SN, et al. Cytokine and growth factor response in a rat model of radiation induced injury to the submental muscles. *Dysphagia* 2021;36(3):457-464 | 10.1007/s00455-020-10162-7 | 32734547 | 6×8 Gy to the rat mylohyoid: TGF-β1, MMP-2 and IL-6 up; TNF-α and IL-1β unchanged. A swallowing-muscle model for the head-neck link (Ep3/Ep4) |
| Li S, et al. Adipose-derived stem cells alleviate radiation-induced muscle fibrosis by promoting muscle regeneration. *Front Cell Dev Biol* 2025;13:1620998 | 10.3389/fcell.2025.1620998 | 41210252 | Rat 90 Gy model: ADSC transplantation reduced fibrosis and boosted SC activation (cell therapy, Ep4) |
| Jiang Y, et al. Unraveling radiation-induced skeletal muscle damage: insights from a 3D human skeletal muscle organoid model. *BBA Mol Cell Res* 2024;1871(7):119792 | 10.1016/j.bbamcr.2024.119792 | 38936620 | hPSC organoids, 2 Gy: γH2AX/53BP1 foci highest in PAX7+ cells, falling by 72 h (human method, Ep1/Ep4) |
| Ness KK, et al. Frailty in childhood cancer survivors. *Cancer* 2015;121(10):1540-1547 | 10.1002/cncr.29211 | 25529481 | Survivors are frail early; senescence, sterile inflammation and mitochondrial dysfunction are proposed causes (hypothesis) (Ep4) |
| Delanian SE, et al. Randomized, placebo-controlled clinical trial combining pentoxifylline-tocopherol and clodronate in the treatment of radiation-induced plexopathy. *Int J Radiat Oncol Biol Phys* 2020;107(1):154-162 | 10.1016/j.ijrobp.2020.01.002 | 31987975 | **Negative** RCT (n=58, 18 months) in nerve plexopathy. An honest counterweight to the 2003 trial (Ep4) |
| Collao N, et al. Resistance and endurance exercise training improves muscle mass and the inflammatory/fibrotic transcriptome in a rhabdomyosarcoma model of cancer survivorship. *J Cachexia Sarcopenia Muscle* 2023;14(2):781-793 | 10.1002/jcsm.13185 | 36797054 | Juvenile RMS + vincristine + 5×4.8 Gy: exercise preserved mass and inflammatory/fibrotic genes, but did *not* prevent fibrosis (Ep4) |
| De Lisio M, et al. Exercise training enhances the skeletal muscle response to radiation-induced oxidative stress. *Muscle Nerve* 2011;43(1):58-64 | 10.1002/mus.21797 | 21171096 | Exercise-trained mice raise SOD/MnSOD and mitochondrial enzymes after high-dose IR (Ep3/Ep4) |
| D'Souza D, et al. The late effects of radiation therapy on skeletal muscle morphology and progenitor cell content are influenced by diet-induced obesity and exercise training in male mice. *Sci Rep* 2019;9:6691 | 10.1038/s41598-019-43204-8 | 31040340 | Obesity worsened post-IR fibrosis; exercise improved fibre size and SC commitment (Ep4) |
| Wernig A, et al. Function of skeletal muscle tissue formed after myoblast transplantation into irradiated mouse muscles. *J Physiol* 2000;522(2):333-345 | 10.1111/j.1469-7793.2000.t01-2-00333.x | 10639108 | 16 Gy irradiated soleus loses ~18% mass and force; donor myoblasts rescue it. Shows the "irradiated host" as a classic transplantation tool (Ep2/Ep4 methods) |
| Siemionow M, et al. Effects of 8-Gy radiation on the microcirculation of muscle flaps in the rat. *Plast Reconstr Surg* 1999;104(5):1372-1378 | 10.1097/00006534-199910000-00020 | 10513920 | **Negative** finding: a single 8 Gy did not significantly change cremaster microcirculation or leukocyte-endothelial interactions over 12 weeks. Vascular injury is dose-dependent (Ep3) |
| Cemazar M, Jurdana M. Radiation-induced impairment of skeletal muscle regeneration. *Radiol Oncol* 2025;59(3):293-300 | 10.2478/raon-2025-0048 | 40959925 | Recent short review (oxidative stress, SCs, fibrosis, vessels, cytokines; melatonin and growth factors) |
| Sebastian S, et al. Effects of low-dose γ-radiation on skeletal muscle stem cells. *Int J Radiat Biol* 2026;102(11):1457-1466 | 10.1080/09553002.2026.2699713 | 42617041 | 10-100 mGy (CT-scan range) in C2C12 and human MuSC cultures: no harm, even a partial restoration of differentiation. Useful for "dose makes the poison" (Ep1/Ep4) |

**Totals:** 12 given + 28 core additions = **40 core references**, plus 16 supplementary = 56 verified in all.

---

## Part D. Gaps I could not fill with muscle-specific, verified evidence (say so honestly on air)
1. **Macrophage time course in irradiated muscle.** There is no dedicated time-course paper. The evidence is indirect: scRNA-seq shows monocyte/macrophage TGF-β signalling to FAPs (Collao 2025), and inflammatory gene expression rises (Kallenbach 2022). The normal timeline comes from non-IR injury (Arnold 2007; Lemos 2015). Frame it as "the detectives infer…".
2. **Senolytics in irradiated muscle.** I found no in-vivo muscle study. Senescence is documented (FAP senescence in Collao 2023, a p21 signature in Collao 2025), but clearance has not been tested in muscle. This is a strong "open question" for Ep4.
3. **Endothelial loss specifically in muscle.** It is supported by Collao 2023 (fewer ECs at 56 d) and Zhou 2018 (EM, 90 Gy rat). Siemionow 1999 found no change at 8 Gy. The "vessel-first" mechanism is shown only in intestine (Paris 2001).
4. **Cardiotoxin/BaCl₂ after IR.** The classic "IR then injury" design in my set uses notexin (Heslop 2000) or cryoinjury (Wernig 2000). I did not verify a CTX/BaCl₂-after-IR paper. Bachman 2020 tested regeneration after IR, but its injury agent is not in the abstract (check the full text).
5. **EV therapy in irradiated muscle.** There is no muscle-specific EV-therapy paper. The EV angle is covered from the other side: tumour-derived EVs drive muscle fibrosis (Zhang 2025).
6. **Human radiation myopathy histology.** No good biopsy series turned up quickly. The human evidence is clinical and functional (Hutcheson 2012; Stubblefield 2011; McCastlain 2021).
7. **Contradictions worth dramatizing.** Rat 90 Gy models show SC *activation* (Zeng 2022; Zhou 2018), while mouse fractionated and juvenile models show SC *loss* (Kallenbach 2022; Bachman 2020; Collao 2023). Species, dose, timing and age all differ.

---

## Part E. Suggested story arc: 4 episodes × ~20 min (~2,600 words each), detective/discovery frame

The series question: *"Why does a muscle that was 'only' near the tumour grow weak and stiff years after radiotherapy?"*
The detectives follow the clues from the moment of impact to the patient's clinic.

### Episode 1: The bullet and the blueprint
*Hook:* a muscle fibre survives the blast, and its stem cells do not. Why?
1. **The invisible bullet.** Photons, ionization, water radiolysis, hydroxyl radicals; direct vs indirect action; Gy, fractionation and BED in plain words. *Refs:* Lomax 2013; Ward 1990; Hardee 2014 (BED example); Sebastian 2026 (very low dose ≠ high dose).
2. **The broken blueprint.** SSB vs DSB and why the DSB is the lethal lesion; clustered damage; γH2AX as the "flare". *Refs:* Ward 1990; Rogakou 1998; Jackson & Bartek 2009.
3. **The repair crews.** ATM → checkpoint; NHEJ vs HR; why quiescent cells depend on NHEJ (DNA-PKcs). *Refs:* Jackson & Bartek 2009; Chang 2017; Vahidi Ferdousi 2014.
4. **Three fates: repair, die, or freeze.** Apoptosis, mitotic failure and senescence; the SASP as the "rumour mill" that sets up Ep3. *Refs:* Jackson & Bartek 2009; Coppé 2008; Bentzen 2006.
5. **First clue in muscle.** Myotubes and myonuclei resist death (blocked ATM→p53 signalling), but dividing precursors die; a human organoid shows foci concentrated in PAX7+ cells. *Cliff-hanger:* the fibre lives, so who pays? *Refs:* Latella 2004; Vahidi Ferdousi 2014; Jiang 2024.

### Episode 2: The guardians
*Hook:* in 1961, an electron microscope spots a cell hiding under the fibre's membrane.
1. **Discovery.** Mauro's "satellite" cell; for decades, did it matter? *Refs:* Mauro 1961; Relaix & Zammit 2012.
2. **Proof of necessity.** Three 2011 papers in the same issue: kill the Pax7+ cells and regeneration fails. *Refs:* Lepper 2011; Sambasivan 2011; Murphy 2011.
3. **Quiescence: alert but asleep.** Quiescence as an active state, and the paradox that quiet SCs repair DNA well, yet radiation still depletes them. *Refs:* Cheung & Rando 2013; Vahidi Ferdousi 2014; Caiozzo 2010.
4. **The radiation experiments.** Heslop's 18/25 Gy plus notexin reveals a hidden reserve; irradiation as a tool to "empty the niche" for transplants; modern lineage tracing finds radiotolerant reserve SCs. *Refs:* Heslop 2000; Boldrin 2012 (method to confirm); Wernig 2000; Scaramozza 2019.
5. **Children: growing muscle is most vulnerable.** Prepubertal SCs are actively building fibres; losing them means smaller fibres for life. *Cliff-hanger:* SCs alone don't explain the *stiffness*. *Refs:* Bachman 2020; Kallenbach 2022; Paris ND 2020.

### Episode 3: The neighbours turn
*Hook:* a crime scene with too much scar tissue and too few stem cells. Who laid the scar?
1. **Meet the FAPs.** The 2010 twin discovery: helpful builders that can become fat and scar producers. *Refs:* Joe 2010; Uezumi 2010; Murphy 2011.
2. **The clean-up crew and its timing.** Normal monocyte→macrophage switch; TNF normally culls FAPs, and if TGF-β dominates, FAPs persist and lay matrix. *Refs:* Arnold 2007; Lemos 2015.
3. **The TGF-β lock and senescent FAPs.** TGF-β1 as the "master switch"; after IR, FAPs turn senescent, fibrogenic and glycolytic; scRNA-seq shows a p21 signature everywhere, with FAPs receiving macrophage TGF-β via TGF-βR2. *Refs:* Martin 2000; Collao 2023; Collao 2025; Coppé 2008; Zhou 2018; King 2021.
4. **Losing the supply lines.** SCs live beside capillaries; IR reduces endothelial cells and causes perivascular fibrosis; the intestinal "vessel-first" analogy; a dose caveat. *Refs:* Christov 2007; Venkatesulu 2018; Collao 2023; Zhou 2018; Paris 2001; Siemionow 1999.
5. **The power plants falter.** ROS, swollen mitochondria, lost oxidative capacity, Ca²⁺ mishandling; exercise as a hint of reversibility. *Refs:* O'Connor 2022; Amorim 2020; Caiozzo 2010; De Lisio 2011; Hardee 2014.

### Episode 4: From bench to bedside
*Hook:* a head-neck cancer survivor who can't swallow nine years after "successful" treatment.
1. **The human cases.** Radiation fibrosis syndrome; late dysphagia and trismus; sarcopenia and frailty in childhood cancer survivors. *Refs:* Stubblefield 2011; Hutcheson 2012; McCastlain 2021; Ness 2015; Fijardo 2024; Bentzen 2006.
2. **The detective's toolkit (methods for beginners).** Local hindlimb IR with a shielded contralateral control (SARRP, fractionated vs single dose); rat high-dose fibrosis models; juvenile tumour-bearing models; injury-after-IR designs; lineage tracing; scRNA-seq; human organoids; core readouts (Masson, fibre CSA, Pax7 counts, γH2AX, ex vivo force). *Refs:* Collao 2023; Bachman 2020; Kallenbach 2022; Zhou 2018; Heslop 2000; Scaramozza 2019; Collao 2025; Jiang 2024; Hardee 2014.
3. **Conflicting clues.** SC activation in rat 90 Gy vs SC loss in mouse; a remote tumour-EV mechanism (the 2025 plot twist). *Refs:* Zeng 2022; Zhou 2018; Kallenbach 2022; Zhang 2025.
4. **Attempts to break the lock.** PTX + vitamin E (positive in 2003, negative in the 2020 plexopathy trial); TGF-β inhibition in mice; losartan blocking tumour SRM; ADSC cell therapy; exercise (helps mass, not fibrosis). *Refs:* Delanian 2003; Delanian 2020; Gans 2021; Zhang 2025; Li 2025; Collao 2023 (exercise); O'Connor 2022; D'Souza 2019; Martin 2000.
5. **Open cases.** Senolytics untested in irradiated muscle; macrophage time course after IR unmapped; whether vessels or stem cells go first; human biopsy data scarce; low-dose effects. *Refs:* Collao 2025; Ness 2015; Paris 2001; Sebastian 2026; Cemazar 2025.

**Arc adjustment I'd suggest:** keep your split. Mitochondria/ROS could open Ep1 as the "radical" mechanism instead, but the muscle-specific mitochondrial data are late and functional, so they fit Ep3 better as a slow-burn clue. Put the methods section in Ep4 (section 2) so beginners meet the tools right after the human stakes.

---

## Part F. Narration cautions
- Label evidence as **fact** (direct experiment), **association** (McCastlain mtDNA, survivor cohorts) or **hypothesis** (vessel-first in muscle, senescence as a driver of frailty).
- Doses differ widely (2 Gy organoid; 16 Gy single mouse; 3×8.2 Gy juvenile; 50 Gy mouse; 90 Gy rat). Don't merge them into one story without saying so.
- Before quoting Ward's per-Gy break numbers on air, check the exact figures in the full text.
