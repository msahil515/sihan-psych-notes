---
date: 2026-06-11
book: "Amity Entrance: Master Syllabus (RCI / NIMHANS pattern)"
subject: "Amity Prep"
chapter: 2
tags: [amity, RCI, clinical-psychology, NIMHANS-pattern, entrance, MET2026]
---

# Ch 2: Synaptic Transmission & Vesicular Trafficking

This chapter walks through how one neuron talks to the next at the chemical synapse: how the arriving action potential triggers calcium entry, how synaptic vesicles dock and fuse to release transmitter, how the membrane is recycled, how the receiving cell decodes the signal through ionotropic and metabotropic receptors, and how thousands of these tiny signals are summed at the axon hillock to decide whether the postsynaptic neuron fires. Synaptic transmission is the single most exam-tested topic in the biological-bases section of RCI and NIMHANS-pattern papers, so master the named proteins, the second messengers, and the summation rules precisely.

## 1. The Chemical Synapse: Orientation

A **chemical synapse** has three parts: the **presynaptic terminal** (the bouton of the sending axon), the **synaptic cleft** (a gap of roughly 20 to 40 nanometres), and the **postsynaptic membrane** (a dendrite, soma, or another axon). Unlike the **electrical synapse** (gap junctions made of **connexons**, which allow near-instant bidirectional ionic flow), the chemical synapse is slower (a **synaptic delay** of about 0.5 to 1 millisecond), unidirectional, and crucially it can amplify, integrate, and modulate signals. That synaptic delay is almost entirely the time taken for calcium to enter and trigger vesicle fusion.

Transmission proceeds as a fixed sequence: action potential reaches the terminal, voltage-gated calcium channels open, calcium triggers vesicle fusion and transmitter release, transmitter diffuses across the cleft, transmitter binds postsynaptic receptors, the postsynaptic membrane changes its potential, and finally the transmitter is cleared and the membrane is recycled. We take each stage in turn.

## 2. Presynaptic Exocytosis and Calcium Microdomains

### 2.1 Voltage-Gated Calcium Channels (VGCCs)

When the action potential depolarises the terminal, it opens **voltage-gated calcium channels (VGCCs)**. Calcium is the trigger ion for release because the extracellular calcium concentration (about 1 to 2 mM) hugely exceeds the resting intracellular concentration (about 100 nM, a roughly 10,000-fold to 20,000-fold gradient), so when channels open calcium rushes inward steeply. The main subtypes tested are:

| Channel type | Gene/name | Where it matters | Pharmacology |
|---|---|---|---|
| **L-type** | Ca_v1.x | Cell body, dendrites, muscle; long-lasting, high-threshold | Blocked by dihydropyridines (nifedipine) |
| **N-type** | Ca_v2.2 | Presynaptic terminals (CNS + PNS), neurotransmitter release | Blocked by omega-conotoxin |
| **P/Q-type** | Ca_v2.1 | Dominant at fast central + neuromuscular release sites | Blocked by omega-agatoxin |
| **T-type** | Ca_v3.x | Thalamic rhythmic bursting (low-threshold, transient) | Distinct from the above |

For exam purposes: **N-type** and **P/Q-type** channels are the ones physically coupled to the release machinery at most synapses, **L-type** is the classic long-lasting high-threshold channel of the soma and muscle, and **T-type** ("T" for transient, low-threshold) drives thalamic burst firing. **Lambert-Eaton myasthenic syndrome** is the classic clinical pointer here: autoantibodies attack presynaptic **P/Q-type** VGCCs, reducing calcium entry and therefore transmitter release, producing muscle weakness that paradoxically improves with repeated effort.

### 2.2 Calcium Microdomains

Calcium does not flood the whole terminal uniformly. Instead, VGCCs cluster within nanometres of the docked vesicles, so when they open a brief, intense, highly localised spike of calcium concentration forms right at the release site: this is the **calcium microdomain** (or **nanodomain** when a single channel sits beside a vesicle). Inside a microdomain the local calcium can transiently reach tens of micromolar, far above the bulk cytosolic level, which is exactly what the low-affinity calcium sensor on the vesicle needs. Because calcium is buffered and pumped away within microseconds to milliseconds, the signal is sharp and spatially confined, which is why release is fast and tightly tied to the action potential.

## 3. The SNARE Core Complex and Vesicle Fusion

### 3.1 The SNARE Proteins

Vesicle fusion is driven by **SNARE proteins** (Soluble NSF Attachment protein REceptors). Two families are distinguished:

- **v-SNARE** (vesicle SNARE): **synaptobrevin** (also called **VAMP**, vesicle-associated membrane protein), sitting on the synaptic vesicle membrane.
- **t-SNAREs** (target/plasma-membrane SNAREs): **syntaxin-1** and **SNAP-25** (synaptosomal-associated protein of 25 kDa), sitting on the presynaptic plasma membrane.

These three wind together into an extremely stable four-helix bundle called the **SNARE core complex** (synaptobrevin contributes one helix, syntaxin one, and SNAP-25 two). The zippering of this complex from the membrane-distal end toward the membrane pulls the vesicle and plasma membranes into close apposition, providing the mechanical force that overcomes the energy barrier to fusion. The clinical/pharmacology hook: **botulinum toxin** cleaves SNARE proteins (different serotypes cleave SNAP-25, syntaxin, or synaptobrevin), blocking acetylcholine release and causing flaccid paralysis; **tetanus toxin** cleaves synaptobrevin in inhibitory spinal interneurons, removing inhibition and causing spastic paralysis.

### 3.2 Synaptotagmin: the Calcium Sensor

**Synaptotagmin-1** is the vesicle protein that acts as the **calcium sensor** for fast synchronous release. It has two cytoplasmic **C2 domains (C2A and C2B)** that bind calcium ions. When the calcium microdomain forms, calcium binds synaptotagmin's C2 domains, which then insert into the plasma membrane and clamp onto the assembled SNARE complex, triggering the final fusion step within a fraction of a millisecond. In the resting state, **complexin** clamps the partly-zippered SNARE complex and holds it ready; calcium-bound synaptotagmin displaces this clamp to release the brake. This is why release is so steeply calcium-dependent (release rate rises roughly with the third to fourth power of calcium concentration, reflecting multiple calcium ions binding the sensor).

### 3.3 Docking, Priming, Fusion

The vesicle cycle near the membrane has three named steps. Know these terms exactly:

1. **Docking:** the vesicle is tethered at the **active zone** (the specialised release-ready region of presynaptic membrane), with SNAREs beginning to associate. The pool of docked, fusion-ready vesicles is the **readily releasable pool (RRP)**.
2. **Priming:** ATP-dependent maturation makes the docked vesicle competent to fuse. Priming proteins **Munc18** and **Munc13** organise syntaxin and catalyse SNARE assembly; the SNARE complex partially zippers. **RIM** proteins help recruit calcium channels close to the vesicle (building the microdomain).
3. **Fusion:** calcium entry and synaptotagmin action drive full SNARE zippering and membrane merger, opening a **fusion pore** through which transmitter escapes into the cleft. Release is **quantal**: one vesicle is one **quantum**, producing a **miniature end-plate potential (MEPP)** when it fuses spontaneously, a key piece of evidence from Katz's quantal hypothesis.

After fusion, **NSF** (an ATPase) plus its cofactor **alpha-SNAP** pry the tightly bound SNARE complex apart so the proteins can be reused. This recycling of the SNARE proteins is distinct from recycling of the vesicle membrane, covered next.

## 4. Endocytosis and Vesicle Recycling

A terminal contains only a finite number of vesicles, so the membrane and proteins added by fusion must be retrieved and rebuilt into new vesicles. The dominant pathway is **clathrin-mediated endocytosis**:

- **Clathrin** molecules (three-legged **triskelions**) assemble into a polyhedral lattice (a basket) on the cytoplasmic face of the membrane, forming a **clathrin-coated pit** that curves inward. Adaptor protein **AP-2** links clathrin to the membrane cargo.
- **Dynamin**, a GTPase, assembles as a collar around the **neck** of the deeply invaginated pit and, using GTP hydrolysis, constricts and pinches it off: this is **dynamin-mediated neck fission**, releasing a coated vesicle into the cytoplasm.
- The clathrin coat is then shed (uncoated, with help from **Hsc70** and **auxilin**), and the bare vesicle either refills with transmitter directly or first fuses with an **early endosome** for sorting and quality control before regenerating new synaptic vesicles. This **endosomal sorting** route lets damaged proteins be replaced.

Faster, clathrin-independent routes also exist (**kiss-and-run**, where the fusion pore opens briefly and reseals without full collapse, and bulk endocytosis during very intense activity), but clathrin-mediated retrieval with dynamin-driven fission is the canonical, exam-default pathway. The clinical pointer: certain forms of epilepsy and the action of drugs targeting **dynamin** trace back to this recycling step.

## 5. Postsynaptic Signal Transduction

Once transmitter crosses the cleft it binds receptors. There are two great receptor families, and distinguishing them is heavily tested.

### 5.1 Ionotropic vs Metabotropic Receptors

| Feature | **Ionotropic (ligand-gated ion channels)** | **Metabotropic (GPCRs)** |
|---|---|---|
| Structure | Receptor IS the ion channel | Receptor is separate from any channel; 7 transmembrane domains |
| Speed | Fast (milliseconds) | Slow (hundreds of ms to seconds/minutes) |
| Mechanism | Ligand binding opens the pore directly | Ligand activates a G-protein → second messengers |
| Duration | Brief | Prolonged, amplifying, modulatory |
| Examples | Nicotinic ACh, GABA-A (Cl-), AMPA/NMDA/kainate (glutamate), glycine | Muscarinic ACh, GABA-B, metabotropic glutamate (mGluR), all monoamine receptors |

**Ionotropic receptors** mediate fast point-to-point transmission. Nicotinic and AMPA receptors pass cations (depolarising, excitatory); GABA-A passes chloride and glycine receptors also pass chloride (usually hyperpolarising, inhibitory). The **NMDA receptor** is a special excitatory glutamate receptor that is both ligand-gated and voltage-dependent (blocked by Mg2+ at rest) and is permeable to calcium, making it central to learning and **long-term potentiation**.

**Metabotropic receptors** are **G-protein-coupled receptors (GPCRs)**: a single polypeptide threading the membrane seven times. They do not open a pore themselves; instead they recruit intracellular machinery, producing slower but amplified and longer-lasting effects.

### 5.2 The Heterotrimeric G-Protein Cycle

A **heterotrimeric G-protein** has three subunits: **alpha (Gα)**, **beta (Gβ)**, and **gamma (Gγ)**; beta and gamma act as a functional **Gβγ dimer**. The cycle:

1. At rest the Gα subunit holds **GDP** and the trimer sits intact, associated with the receptor.
2. Ligand binding changes the receptor's shape so it acts as a **guanine nucleotide exchange factor (GEF)**, prompting Gα to swap **GDP for GTP**.
3. GTP-bound Gα dissociates from the Gβγ dimer. **Both** the free Gα-GTP and the free Gβγ can now regulate effector enzymes and ion channels.
4. Gα has intrinsic **GTPase** activity: it hydrolyses GTP back to GDP (accelerated by **RGS** proteins), then reassociates with Gβγ, ending the signal. This built-in timer is why metabotropic signalling self-terminates.

G-proteins come in families named by their Gα: **Gs** stimulates adenylate cyclase (raises cAMP), **Gi** inhibits adenylate cyclase (lowers cAMP), and **Gq** activates phospholipase C. Cholera toxin locks Gs "on" (constant cAMP); pertussis toxin locks Gi "off."

### 5.3 Effector Enzymes and Second Messengers

- **Adenylate cyclase (adenylyl cyclase):** activated by Gs, inhibited by Gi. It converts ATP into the **second messenger cyclic AMP (cAMP)**. cAMP's main target is **Protein Kinase A (PKA)**.
- **Phospholipase C (PLC):** activated by Gq. It cleaves the membrane lipid **PIP2** into two second messengers at once: **IP3 (inositol trisphosphate)** and **DAG (diacylglycerol)**.
  - **IP3** diffuses to the endoplasmic reticulum and opens IP3 receptors, releasing stored **calcium (Ca2+)** into the cytosol. Calcium is itself a major second messenger.
  - **DAG** stays in the membrane and, together with calcium, activates **Protein Kinase C (PKC)**.

So the four classic second messengers to name are **cAMP, IP3, DAG, and Ca2+** (with cGMP as a fifth in some systems). The logic: Gs/Gi → cAMP → PKA; Gq → PLC → IP3 + DAG → Ca2+ + PKC.

### 5.4 The Protein Kinases

Second messengers act by switching on **protein kinases**, enzymes that phosphorylate target proteins (adding a phosphate from ATP) to change their activity. The three tested by name:

- **PKA (Protein Kinase A):** activated by **cAMP**. It phosphorylates ion channels, metabolic enzymes, and the transcription factor **CREB**, which switches on genes for long-term changes. This cAMP–PKA–CREB pathway underlies long-term memory (famously in Kandel's Aplysia work).
- **PKC (Protein Kinase C):** activated by **DAG + Ca2+**. Involved in growth, plasticity, and the action of phorbol esters (which mimic DAG).
- **CaMKII (Calcium/calmodulin-dependent protein kinase II):** activated by **Ca2+ bound to calmodulin**. It is enriched at the postsynaptic density, autophosphorylates so it stays active after calcium falls (a molecular "memory switch"), and is essential for **long-term potentiation (LTP)** and learning. CaMKII phosphorylates and inserts AMPA receptors, strengthening the synapse.

Note the recurring amplification logic: one transmitter molecule can activate a GPCR, which activates many G-proteins, each effector makes many second-messenger molecules, each kinase phosphorylates many substrates. This **signal amplification cascade** is the defining advantage of metabotropic over ionotropic signalling.

## 6. Postsynaptic Potentials and Signal Integration

### 6.1 EPSPs and IPSPs

Receptor activation changes the postsynaptic membrane potential, producing a **postsynaptic potential (PSP)**, which is **graded** (variable in size) and **decremental** (fades with distance), unlike the all-or-none action potential.

- An **excitatory postsynaptic potential (EPSP)** is a **depolarisation** (membrane moves toward threshold, e.g. from -70 mV toward -55 mV), typically from opening cation channels that let Na+ (and sometimes Ca2+) in. Glutamate via AMPA/NMDA is the main excitatory driver.
- An **inhibitory postsynaptic potential (IPSP)** is a **hyperpolarisation** (membrane moves away from threshold, more negative), typically from opening Cl- channels (GABA-A, glycine) letting chloride in, or opening K+ channels letting potassium out. GABA is the main inhibitory transmitter in the brain, glycine in the spinal cord.

A single EPSP is usually far too small to fire the cell; thousands must combine.

### 6.2 Spatial and Temporal Summation

The neuron adds up its incoming PSPs. Two modes, both heavily tested:

- **Spatial summation:** PSPs arriving at the **same time from different locations** (different synapses) on the neuron add together. Many simultaneous EPSPs from across the dendritic tree can sum to reach threshold. EPSPs and IPSPs can also cancel each other in space.
- **Temporal summation:** PSPs arriving at the **same location in rapid succession** (close together in time, before the first has decayed) add on top of one another. A high-frequency train from one synapse can build up to threshold.

### 6.3 The Axon Hillock and the Decision to Fire

All these summed potentials spread passively to the **axon hillock** (the **initial segment**, the cone-shaped junction of soma and axon). The hillock is the integration point because it has the **highest density of voltage-gated sodium channels** and therefore the **lowest threshold** in the neuron. If the net summed depolarisation at the hillock reaches **threshold (about -55 mV, roughly 15 mV above the -70 mV resting potential)**, an **all-or-none action potential** is triggered and propagates down the axon. If summation falls short, no spike fires. This is why the axon hillock is described as the neuron's **decision-making zone** or trigger zone: it weighs the total excitatory and inhibitory input from thousands of synapses and converts a graded analogue signal into a digital all-or-none output.

## High-Yield Recap

- **Synaptic delay** ~0.5 to 1 ms; **cleft** ~20 to 40 nm; chemical synapses are unidirectional and modulatory, electrical synapses (connexons) are fast and bidirectional.
- **VGCCs:** N-type (Ca_v2.2) and P/Q-type (Ca_v2.1) drive release; L-type (Ca_v1) = long-lasting somatic/muscle; T-type (Ca_v3) = transient thalamic bursting. **Lambert-Eaton** = anti-P/Q antibodies.
- **Calcium microdomain/nanodomain:** sharp, local, transient high-calcium zone at the active zone right beside docked vesicles.
- **SNARE core complex:** v-SNARE **synaptobrevin (VAMP)** + t-SNAREs **syntaxin-1** and **SNAP-25** form a 4-helix bundle; **synaptotagmin-1** (two C2 domains) is the Ca2+ sensor; **complexin** clamps; **NSF + alpha-SNAP** disassemble afterward.
- **Botulinum toxin** cleaves SNAREs → flaccid paralysis; **tetanus toxin** cleaves synaptobrevin in inhibitory neurons → spastic paralysis.
- **Three steps:** Docking (RRP at active zone) → Priming (Munc13/Munc18, ATP) → Fusion (Ca2+ + synaptotagmin, fusion pore). Release is **quantal** (1 vesicle = 1 quantum = MEPP).
- **Recycling:** clathrin (triskelions) + AP-2 coated pit → **dynamin** GTPase pinches the neck (fission) → uncoating (Hsc70) → endosomal sorting; alternatives = kiss-and-run, bulk endocytosis.
- **Ionotropic** = receptor is the channel, fast (nicotinic, GABA-A/Cl-, AMPA/NMDA, glycine). **Metabotropic** = 7-TM **GPCR**, slow, amplifying (muscarinic, GABA-B, mGluR, monoamines). NMDA = ligand- + voltage-gated, Mg2+ block, Ca2+ permeable, LTP.
- **G-protein cycle:** receptor = GEF, Gα swaps GDP→GTP, Gα-GTP and Gβγ both signal, intrinsic GTPase (+ RGS) ends it. **Gs** ↑adenylate cyclase, **Gi** ↓it, **Gq** → PLC.
- **Second messengers:** adenylate cyclase → **cAMP** → **PKA** (→ CREB → genes); PLC cleaves PIP2 → **IP3** (releases ER **Ca2+**) + **DAG** (with Ca2+ → **PKC**); **CaMKII** (Ca2+/calmodulin) drives **LTP** and autophosphorylates.
- **EPSP** = depolarisation (Na+ in), **IPSP** = hyperpolarisation (Cl- in / K+ out); PSPs are graded and decremental.
- **Spatial summation** = different sites, same time; **temporal summation** = same site, rapid succession.
- **Axon hillock / initial segment** = highest Na+ channel density, lowest threshold; fires all-or-none AP when summed input reaches **threshold ~-55 mV** (resting ~-70 mV).
