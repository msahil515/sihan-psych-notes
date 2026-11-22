---
date: 2026-11-21
book: "Biopsychology (Pinel & Barnes, 11th ed.)"
subject: Biopsychology
chapter: 5
title: "The Research Methods of Biopsychology"
tags: [biopsychology, research-methods, neuroimaging, CT, MRI, PET, fMRI, BOLD, DTI, TMS, tES, EEG, ERP, P300, MEG, psychophysiology, lesions, stereotaxic-surgery, psychopharmacology, genetic-methods, optogenetics, neuropsychological-testing, WAIS, cognitive-neuroscience, animal-paradigms, MET2026, clinical-psychology, MCQ-prep]
---

# Chapter 5: The Research Methods of Biopsychology

**What this chapter is really about.** Every claim in the rest of the book ("the hippocampus is needed for spatial memory", "dopamine neurons fire to unexpected reward", "the left hemisphere is dominant for language") rests on a method, and every method has a blind spot. This chapter is the toolkit. It has two halves that mirror the two halves of the word *biopsychology*. Part One covers the ways of looking at, recording from and manipulating the **nervous system**: brain imaging, transcranial stimulation, recording from the surface of the body, surgery inside the brain, chemicals and genes. Part Two covers the ways of measuring **behaviour**: neuropsychological tests for patients, the behavioural logic of brain-imaging experiments, and the standard behavioural set-ups used with laboratory rats.

The single idea that ties the chapter together is that no method is clean. A lesion damages more than its target; an fMRI image shows blood, not neurons; a skin conductance change could mean fear, excitement or simply a warm room; a knockout mouse grew up without its gene and may have compensated. Pinel and Barnes end the chapter by naming the solution, **converging operations**: a question is settled only when several methods with different weaknesses point to the same answer. If you read each method asking "what does it actually measure, and what could fool it?", the chapter becomes a set of contrasts rather than a list, and the contrasts are exactly what entrance papers test (CT versus MRI, PET versus fMRI, EEG versus MEG, SCL versus SCR, aspiration versus radio-frequency versus reversible lesions, knockout versus knockin, immunocytochemistry versus in situ hybridisation).

**How to read this chapter.** The 11th edition has eight modules, numbered here 5.1 to 5.8. Part One: 5.1 imaging and stimulating the living human brain; 5.2 psychophysiological recording (brain, somatic and autonomic measures); 5.3 invasive methods in animals (stereotaxic surgery, lesions, stimulation, recording); 5.4 pharmacological methods; 5.5 genetic methods. Part Two: 5.6 neuropsychological testing; 5.7 behavioural methods of cognitive neuroscience; 5.8 behavioural paradigms for animals, ending with converging operations. For each method, fix four things: what it measures, how it physically works, what it is good and bad at (spatial and temporal resolution, invasiveness, cost), and which method it is most often confused with. The comparison tables at the ends of 5.1 and 5.2 are worth learning as tables.

---

## The Ironic Case of Professor P.

The chapter opens with a biopsychologist who becomes a patient. Professor P. had a tumour growing on his **right auditory-vestibular cranial nerve (cranial nerve VIII)**, the nerve that carries both hearing and balance information from the inner ear, and it had to be surgically removed. Two weeks before the operation he went to the hospital for a day of tests, and what struck him was that almost every test was a procedure he knew from his own research.

The tests, in order:

| Test | What was done | What it assessed |
|---|---|---|
| Audiological testing | Detecting tones that varied in loudness and pitch | Hearing in each ear |
| Auditory evoked potentials | Clicks played into the right ear while the EEG response of the auditory cortex was recorded from the scalp | Whether the auditory pathway from the right ear was conducting normally |
| Vestibular (caloric) test | Water of decreasing temperature flushed into the ear | Function of the vestibular part of nerve VIII |
| Somatosensory evoked potentials | The right cheek lightly pricked while somatosensory cortex responses were recorded from the scalp | A baseline for monitoring the facial nerve during surgery |

The vestibular test is the memorable one. Cold water in the ear canal normally disturbs the fluid of the balance organ and produces strong dizziness and nausea. In Professor P. the water was made colder and colder with almost no effect, and only the coldest flush gave him a mild sense that the bed was tilting. The technician remarked that most people would have been violently sick at those temperatures. The results confirmed the damage: hearing in his right ear was poor and his right vestibular nerve was barely working. That was bad news for Professor P., but it simplified the surgery, because the surgeon no longer needed to try to preserve the nerve; it could simply be cut.

The last test explains a clever piece of surgical monitoring. The main danger when removing a tumour from nerve VIII is damage to the neighbouring **facial nerve (cranial nerve VII)**, which would leave the right side of the face drooping. So during the operation, electrodes in the cheek would deliver small electrical pulses, the resulting responses of the somatosensory cortex would be recorded and fed to a loudspeaker, and the surgeon would *hear* any change in the signal the moment the scalpel began to stray towards the facial nerve. The pre-operative recording provided the normal baseline against which those changes would be judged.

Driving home, Professor P. reflected that each of the three hospital labs he had visited employed people who had started their careers as biopsychologists. On the day of surgery, a nurse who had once been his student inserted a large needle into his face as part of the preparation. He was barely conscious, and he did not yet know that he would not regain consciousness for several days, and that when he did he would be unable to speak, eat or even breathe on his own. The book returns to him in **Chapter 10**.

### Why the case opens a methods chapter

The point is not the tumour. It is that the research methods of biopsychology are also **clinical methods**. Evoked potentials, vestibular testing, EEG monitoring and brain imaging are used both to answer scientific questions and to diagnose and treat patients, and many of the technicians and scientists who run them are trained biopsychologists. This is the book's **clinical implications** theme, and the chapter's closing "Themes revisited" section points back to Professor P. for exactly that reason.

> **Trap.** Professor P.'s tumour was on cranial nerve **VIII (auditory-vestibular, also called vestibulocochlear)**; the nerve at risk during surgery was cranial nerve **VII (facial)**. Questions sometimes swap them. The cheek-pricking test monitored the facial nerve indirectly, through the somatosensory cortex response, not by recording from the nerve itself.

---

## Part One: Methods of Studying the Nervous System

Part One is about getting information out of, or changing the state of, the nervous system itself. The methods are extremely varied, from multimillion-rupee scanners to a hand-held glass pipette, but they share one purpose: neural activity is invisible, so every method in Part One is a way of making the invisible observable. Module 5.1 deals with the living human brain, which can only be studied non-invasively; modules 5.3 to 5.5 move to the more direct methods that are mostly limited to laboratory animals.

## 5.1 Methods of Visualising and Stimulating the Living Human Brain

The module covers four families of imaging methods, classified by the physical signal they use: **X-ray-based** (contrast X-rays, CT), **radioactivity-based** (PET), **magnetic-field-based** (MRI, diffusion tensor MRI, fMRI) and **ultrasound-based** (functional ultrasound). It then covers three ways of non-invasively **stimulating** the human brain: transcranial magnetic, electrical and ultrasound stimulation. Before the early 1970s, none of the imaging methods except contrast X-rays existed, and biopsychology was badly hampered by being unable to see the organ it cared most about.

A distinction to fix before anything else: a **structural** image shows what the brain looks like (anatomy, tumours, lesions, tracts), while a **functional** image shows what the brain is doing (where activity, metabolism or blood flow is changing during a task). CT, MRI and diffusion tensor MRI are structural. PET, fMRI and fUS are functional.

### Why ordinary X-rays fail

An X-ray photograph works by shining a beam through an object onto a photographic plate. Every molecule in the path absorbs a little of the radiation, so the plate records only what got through. That is ideal when the thing you want to see absorbs X-rays very differently from what surrounds it, such as bone inside flesh or a metal object in a bag of clothes. The brain is the opposite case. It is made of many overlapping structures that differ only slightly in how much X-radiation they absorb, so by the time the beam has passed through all of them it carries almost no usable information about any one of them. A plain skull X-ray shows the skull well and the brain hardly at all.

### Contrast X-rays and cerebral angiography

The fix is to create the difference in absorption artificially. In **contrast X-ray techniques**, a substance that absorbs X-rays either *more* or *less* than the surrounding tissue is injected into one compartment of the body, which heightens the contrast between that compartment and everything around it.

The contrast technique the book describes is **cerebral angiography**: a **radio-opaque dye** is infused into a **cerebral artery**, and X-ray photographs then show the cerebral circulation. Angiograms are most useful for locating **vascular damage** (blocked, narrowed or ballooning vessels), but they can also locate a **tumour** indirectly, because a growing mass pushes blood vessels out of their normal positions.

A historical note from the chapter's journal prompt: cerebral angiography was pioneered by **Egas Moniz**, the Portuguese neurologist who also introduced the prefrontal lobotomy and received a Nobel Prize for it. Some have argued that the prize should be revoked; others reply that his angiography work alone would have earned it.

> **Trap.** Moniz is linked to **two** things: cerebral angiography and the lobotomy (prefrontal leucotomy). His Nobel Prize (1949, a date from outside the chapter) was awarded for the lobotomy, not for angiography. Older editions of Pinel and many Indian guidebooks also mention **pneumoencephalography** (air injected into the ventricles) as a contrast X-ray method; the 11th edition does not describe it, and cerebral angiography is now its only worked example.

<div class="fig">
<a class="figzoom" href="figs/f_5_1.jpg" target="_blank" rel="noopener"><img src="figs/f_5_1.jpg" loading="lazy" alt="Pinel Fig 5.1: cerebral angiogram showing the brain&#x27;s arteries made visible by radio-opaque dye"></a>
<p class="cap"><b>A cerebral angiogram of a healthy human.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.1</p>
</div>

### Computed tomography (CT)

**Computed tomography (CT)**, introduced in the **early 1970s**, was the first method that let researchers and clinicians see the living brain itself, and it revolutionised the field. It is a **computer-assisted X-ray procedure**.

How it works:

1. The patient lies with the head in the centre of a large cylinder.
2. On one side of the cylinder is an **X-ray tube**; directly opposite is an **X-ray detector**. The beam passes through the head from tube to detector.
3. Tube and detector **rotate rapidly around the head at one level** of the brain, taking a large number of individual X-ray readings from different angles.
4. Each single reading is nearly useless on its own, for the reason given above. A computer combines all of them to reconstruct an image of **one horizontal section** of the brain.
5. Tube and detector are then moved along the length of the body to the next level, and the process repeats. Typically **eight or nine horizontal sections** are taken, and together they give a **three-dimensional** representation of the brain.

The trick, in other words, is not a better X-ray but better arithmetic. Many weak, ambiguous measurements taken from different directions can be combined to recover what each point inside the head is like. (Godfrey Hounsfield and Allan Cormack shared the 1979 Nobel Prize in medicine for developing CT; the chapter does not mention them.)

<div class="fig">
<a class="figzoom" href="figs/f_5_2.jpg" target="_blank" rel="noopener"><img src="figs/f_5_2.jpg" loading="lazy" alt="Pinel Fig 5.2: CT scanner with rotating X-ray source and detector, horizontal CT sections and a 3-D reconstruction"></a>
<p class="cap"><b>Computed tomography uses X-rays to create a brain scan.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.2</p>
</div>

### Positron emission tomography (PET)

**Positron emission tomography (PET)** was the **first** brain-imaging technique to produce images of brain **activity** (functional images) rather than brain **structure**.

In the version the book describes, radioactive **fluorodeoxyglucose (FDG)** is injected into the patient's **carotid artery**, the neck artery that supplies the cerebral hemisphere on the same side. The logic runs in four steps:

1. Glucose is the brain's main metabolic fuel, and active (energy-consuming) cells take up more of it.
2. FDG is similar enough to glucose that active cells take it up rapidly.
3. Unlike glucose, FDG **cannot be metabolised**, so it is trapped and **accumulates** in active neurons and astrocytes until it is slowly broken down.
4. The amount of radioactivity in each region therefore reflects how active that region was while the FDG was being taken up.

So if a volunteer reads for about **30 seconds** after the FDG injection, the PET scan shows which parts of that brain level were most active during those 30 seconds. Each scan represents one **horizontal** level, with radioactivity colour-coded (in Figure 5.3, reds and yellows mark high activity, and the visual cortex of the occipital lobe lights up when the eyes are open but not when they are closed).

Look at what a PET scan actually is. It is **not a picture of the brain**. It is a colour-coded map of the amount of radioactivity in each of the tiny cubes, called **voxels** (volume pixels), that make up the scan. Which brain structure a given voxel corresponds to can only be estimated by **superimposing** the PET scan on a structural image such as an MRI.

(The physics behind the name, standard but not spelled out in the chapter: the radioactive label emits positrons; each positron travels a millimetre or so, meets an electron, and the two annihilate into a pair of gamma rays flying off in opposite directions. Detectors around the head register these pairs, and a computer works back to where they originated.)

> **Trap.** Older editions of Pinel (and the old version of this note) said that PET uses radioactive **2-deoxyglucose (2-DG)**. The 11th edition says **fluorodeoxyglucose (FDG)**, the radioactive glucose analogue actually used in clinical PET. **2-DG** in the 11th edition belongs to the **2-deoxyglucose technique** of module 5.4, an *animal* method in which the brain is removed and sliced for autoradiography. If an option says "2-DG autoradiography is used in living human volunteers", it is wrong; if an old key says "PET uses 2-DG", recognise it as old-edition wording for the same principle.

<div class="fig">
<a class="figzoom" href="figs/f_5_3.jpg" target="_blank" rel="noopener"><img src="figs/f_5_3.jpg" loading="lazy" alt="Pinel Fig 5.3: two horizontal PET scans; occipital visual cortex shows high (red-yellow) activity with eyes open, not with eyes closed"></a>
<p class="cap"><b>A pair of PET scans with the eyes open and closed.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.3</p>
</div>

### PET with ligands: mapping molecules

According to the 11th edition, the **most significant current application** of PET is not measuring activity at all but mapping where particular **molecules**, such as neurotransmitters, receptors and transporters, are located in the living brain (Camardese et al., 2014). Volunteers are injected with radioactively labelled **ligands**, ions or molecules that bind to other molecules (for example, a drug that binds to a particular dopamine receptor). The PET scan then shows where the radioactivity, and hence the binding target, is concentrated. This is the living-human counterpart of the receptor-locating methods for animal tissue in module 5.4.

> **Trap.** "PET's main use is measuring regional glucose metabolism" is what most students write. The 11th edition says its **most significant current** use is **ligand imaging** of neurotransmitters, receptors and transporters. Both uses are real; read the question's wording.

### Magnetic resonance imaging (MRI)

**Magnetic resonance imaging (MRI)** is a **structural** imaging procedure. High-resolution images are built from measurements of the **radio-frequency waves** that **hydrogen atoms** emit as they align with a powerful **magnetic field**.

Why this produces a picture of the brain, in three links:

1. Water (H₂O) contains two hydrogen atoms per molecule.
2. Different brain structures contain different amounts of water, so they contain different numbers of hydrogen atoms.
3. The radio-frequency signal coming from one structure therefore differs from that of its neighbours, and the differences can be turned into an image.

(The fuller standard account: in the strong field, hydrogen nuclei line up; a pulse of radio waves knocks them out of alignment, and as they relax back they emit radio-frequency energy whose strength and timing depend on the local tissue.)

MRI gives **clearer images of the brain than CT** (Lerch et al., 2017). It also has relatively high **spatial resolution**, which the book defines as the ability to detect and represent differences in spatial location, and it can produce images in **three dimensions** (Figure 5.5 shows a growing tumour, coloured red, in a 3-D MRI). Figure 5.4 is a two-dimensional MRI of the **midsagittal** plane.

<div class="fig">
<a class="figzoom" href="figs/f_5_4.jpg" target="_blank" rel="noopener"><img src="figs/f_5_4.jpg" loading="lazy" alt="Pinel Fig 5.4: two-dimensional MRI of the midsagittal plane of the human head and brain"></a>
<p class="cap"><b>A colour-enhanced midsagittal MRI scan.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.4</p>
</div>

<div class="fig">
<a class="figzoom" href="figs/f_5_5.jpg" target="_blank" rel="noopener"><img src="figs/f_5_5.jpg" loading="lazy" alt="Pinel Fig 5.5: three-dimensional MRI reconstruction of a brain with a tumour shown in red"></a>
<p class="cap"><b>MRI of a growing tumour, coloured red.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.5</p>
</div>

### CT versus MRI

These two are the commonest structural-imaging pairing in MCQs.

| | CT | MRI |
|---|---|---|
| Physical basis | X-rays (computer-assisted) | Magnetic field plus radio-frequency waves from hydrogen atoms |
| Ionising radiation | Yes | No |
| What creates contrast | Differences in X-ray absorption | Differences in water (hydrogen) content |
| Image quality for brain | Good | Clearer, higher spatial resolution |
| Slices | Horizontal sections, typically 8 or 9, combined into 3-D | Any plane (e.g. midsagittal) and 3-D |
| Type | Structural | Structural (fMRI and DTI are variants) |

The radiation row comes from general knowledge rather than the chapter, but it follows directly from the physics: CT is an X-ray method and MRI is not. The practical consequence often tested in clinical papers is that CT is faster and better for detecting fresh bleeding and bone injury, while MRI shows soft-tissue detail far better.

### Diffusion tensor MRI and the connectome

Many variants of MRI have been developed. The book singles out **diffusion tensor MRI (DTI)** as perhaps the most innovative. It identifies the pathways along which **water molecules diffuse rapidly**. In the brain, water moves most freely *along* bundles of axons (tracts) rather than across them, so DTI produces an image of the brain's **major tracts** (Figure 5.6).

Why that matters: most brain research has concentrated on structures, but understanding how the brain works requires knowing how the structures are **connected**. The complete map of neural connections is called the **connectome**. Complete connectomes already exist for some organisms, including the nematode **C. elegans** and the **mouse** (Oh et al., 2014), and the **Human Connectome Project** is well under way. DTI is a central tool of that effort, which is why diffusion tensor images have become a research focus.

> **Trap.** DTI is a **structural** MRI method that images **white-matter tracts**, inferred from the direction of water diffusion. It does not image activity, and it does not image grey-matter nuclei particularly well. "Functional connectivity" (module 5.7) is a different thing entirely: it is inferred from correlated *activity* over time, not from anatomy.

<div class="fig">
<a class="figzoom" href="figs/f_5_6.jpg" target="_blank" rel="noopener"><img src="figs/f_5_6.jpg" loading="lazy" alt="Pinel Fig 5.6: three-dimensional diffusion tensor image showing the major white-matter tracts in colour"></a>
<p class="cap"><b>Diffusion tensor MRI of the brain's major tracts.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.6</p>
</div>

### Functional MRI and the BOLD signal

MRI technology has also been adapted to produce functional images, and **functional MRI (fMRI)** has become the **most influential tool of cognitive neuroscience**. It is used clinically to judge whether a brain is functioning abnormally, and in research for surprisingly varied purposes, including inferring the content of a person's **dreams** (Horikawa et al., 2013).

fMRI produces images of the **increase in oxygenated blood flow** to active areas of the brain. It depends on two properties of oxygenated blood:

1. **Active brain areas take up more oxygenated blood than their energy needs require**, so oxygenated blood accumulates in active areas (Hillman, 2014). The blood supply overshoots the demand.
2. **Oxygenated blood has different magnetic properties from deoxygenated blood**, and this difference changes the radio-frequency waves that hydrogen atoms emit in the scanner.

Put these together: an active area becomes relatively richer in oxygenated blood, which changes the local MRI signal. The signal recorded by fMRI is called the **BOLD signal** (**blood-oxygen-level-dependent** signal). It indicates which brain areas are active or inactive during a cognitive or behavioural task, and therefore suggests what kinds of analysis the brain is carrying out.

The crucial caution: because the BOLD signal is produced by **blood flow**, it is **not a direct measure of the brain's electrical activity**.

### fMRI versus PET

fMRI has **three advantages over PET**, a list that is examined directly:

1. **Nothing has to be injected** into the volunteer (no radioactive tracer).
2. It provides **structural and functional information in the same image**.
3. Its **spatial resolution is better**.

Figure 5.7 is an fMRI from Kiehl and colleagues (1999). Volunteers looked at strings of letters and had to decide which strings were real words (a lexical decision task); in the control condition they looked at strings of asterisks. The figure shows the cortical surface areas that became more active in the word task than in the asterisk task, an early taste of the subtraction logic that module 5.7 develops.

| | PET | fMRI |
|---|---|---|
| Signal | Radioactivity from an injected tracer (FDG, or a labelled ligand) | BOLD signal (oxygenated versus deoxygenated blood) |
| Injection needed | Yes, radioactive | No |
| Structure in the same image | No, must be superimposed on a structural scan | Yes |
| Spatial resolution | Poorer | Better |
| Unique strength | Can map specific molecules (receptors, transporters) via ligands | Repeatable, no radiation, most-used tool in cognitive neuroscience |
| Historical status | First functional imaging method | Later, now dominant |

> **Trap.** "fMRI measures neural firing" is wrong. It measures the **BOLD signal**, a consequence of blood flow and oxygenation, whose relation to neural activity is **complex**. Equally, "PET measures blood oxygen" is wrong; FDG-PET measures **accumulated radioactive glucose analogue**, an index of metabolic activity.

<div class="fig">
<a class="figzoom" href="figs/f_5_7.jpg" target="_blank" rel="noopener"><img src="figs/f_5_7.jpg" loading="lazy" alt="Pinel Fig 5.7: fMRI of cortical areas more active when deciding which letter strings are words than when viewing asterisks (Kiehl et al., 1999)"></a>
<p class="cap"><b>Functional MRI of cortical activity during a word-recognition task.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.7</p>
</div>

### Reading fMRI images critically: temporal resolution

Pinel and Barnes warn against being dazzled by fMRI. Popular articles and introductory textbooks present the coloured images as if they were photographs of neurons at work. They are images of the BOLD signal, and the relationship between that signal and neural activity is complex.

The second limitation is **temporal resolution**, the ability to specify *when* neural events happen. fMRI is poor at it. It takes **2 or 3 seconds** to measure the BOLD signal, whereas many neural events, action potentials for example, unfold within **milliseconds**. An fMRI study can therefore tell you fairly precisely *where* something happened, but only roughly *when*. Keep this in mind for 5.2, where the EEG-based methods have the opposite profile.

### Functional ultrasound imaging (fUS)

**Functional ultrasound imaging (fUS)** is a new technique that uses **ultrasound** (sound waves above the range of human hearing) to measure changes in **blood volume** in particular brain regions. When a region becomes active its blood volume rises, and that alters how ultrasound passes through it.

It has **three key advantages over PET and fMRI** (Deffieux et al., 2018):

1. It is **cheap**.
2. It is **highly portable**.
3. It can image people who cannot undergo PET or fMRI, such as **human infants**.

Like fMRI, it measures a blood-related signal (blood *volume* here, blood *oxygenation* in fMRI), so it is also an indirect index of neural activity.

### Why imaging cannot prove causation

PET, fMRI and fUS let cognitive neuroscientists image brain activity while people perform particular cognitive tasks. Impressive as these studies are, they share one built-in weakness: they can show that brain activity and a cognitive activity are **correlated**, but not that the brain activity **caused** the cognitive activity (Sack, 2006).

The book's illustration: suppose imaging shows that the **cingulate cortex** becomes active when people view disturbing photographs. That does not prove the cingulate activity produces the emotional experience; the activity could be a by-product, a consequence, or a response to some other feature of the task. Two strategies would strengthen the causal claim:

- **Remove the area and see whether the function goes.** Test emotional experience in people without a working cingulate cortex, either patients with cingulate damage or healthy people whose cingulate cortex has been temporarily "turned off". TMS can do the turning off.
- **Activate the area and see whether the function appears.** Test emotional experience after the cingulate cortex has been "turned on". Transcranial electrical stimulation and transcranial ultrasound stimulation can do the turning on.

This is the same logic as lesion and stimulation studies in animals (module 5.3), applied non-invasively to humans.

### Transcranial magnetic stimulation (TMS)

**Transcranial magnetic stimulation (TMS)** creates a **magnetic field under a coil held next to the skull**. The field temporarily **turns off** (disrupts) an area of cortex while the effects on cognition and behaviour are measured (Candidi et al., 2015). In effect, it produces a brief, reversible "lesion" in a healthy volunteer.

TMS is widely used precisely to get around the causation problem of imaging. However, the book notes that there are still **fundamental open questions** about its **safety**, its **depth of effect**, and the **mechanisms** by which it disrupts neural activity. And with **different stimulation parameters**, TMS can also be used to **turn on** an area of cortex (Rossini et al., 2015).

(Standard background, not in the chapter: the rapidly changing magnetic field induces electrical currents in the cortex beneath the coil; repeated pulses are called **rTMS**, which is approved in many countries as a treatment for depression.)

### Transcranial electrical stimulation (tES)

**Transcranial electrical stimulation (tES)** **turns on** an area of cortex by passing an electrical current between **two electrodes placed directly on the scalp**. The stimulation temporarily **increases** activity in that part of the brain while its effects on cognition and behaviour are measured.

tES has become popular for its supposed cognitive-enhancing effects, and relatively cheap kits can be bought online (Bourzac, 2016). The evidence is mixed: some studies report benefits, others no effect, and some even report **detrimental** effects on cognition. Differences in stimulation protocols may explain part of the inconsistency (Sellers et al., 2015).

> **Trap.** The 11th edition uses the umbrella term **tES**. The best-known form in the wider literature is **tDCS** (transcranial *direct current* stimulation), in which a weak constant current flows from an anode to a cathode; anodal stimulation is generally described as raising cortical excitability and cathodal as lowering it. If a paper asks about tDCS, it is asking about the tES family. Also note the asymmetry the book draws: **TMS is presented mainly as a way to turn cortex off** (though it can turn it on), whereas **tES and tUS are presented as ways to turn it on**.

### Transcranial ultrasound stimulation (tUS)

**Transcranial ultrasound stimulation (tUS)** can also activate brain structures, but with a decisive advantage: **TMS and tES can only stimulate cortical structures, whereas tUS can also reach subcortical structures**.

How it gets deep without affecting everything in between: **several sources of low-amplitude ultrasound** are placed around the head and each is aimed at the same target. Along each individual path the sound is too weak to do anything, but where the beams **converge at the target, their waves sum**, and the combined amplitude there is large enough to stimulate the cells (Tyler, Lani, & Hwang, 2018).

The same procedure with **larger-amplitude** sources produces a summed wave strong enough to make a small **permanent lesion**, about the size of a grain of rice. This tUS lesion method has been used therapeutically, for example to destroy a **thalamic nucleus** to treat **essential tremor**, and it requires **no incision**. The book says it is revolutionising neurosurgery (Landhuis, 2017).

### The imaging and stimulation methods side by side

| Method | Physical basis | Structural or functional | Key strength | Key limitation |
|---|---|---|---|---|
| Cerebral angiography | Radio-opaque dye in a cerebral artery, X-rays | Structural (vessels) | Shows vascular damage; tumours by vessel displacement | Invasive injection; shows vessels, not brain tissue |
| CT | Rotating X-ray tube and detector, computer reconstruction | Structural | First view of the living brain (early 1970s) | Less clear than MRI |
| PET | Radioactive FDG or labelled ligand | Functional (first functional method) | Maps specific molecules via ligands | Radioactive injection; poorer spatial resolution; voxels must be overlaid on anatomy |
| MRI | Radio-frequency waves from hydrogen atoms in a magnetic field | Structural | Clear, high spatial resolution, 3-D | Expensive scanner |
| DTI | Direction of water diffusion | Structural (tracts) | Images major axon tracts; connectome research | Tracts only |
| fMRI | BOLD signal | Functional, plus structure in same image | No injection; better spatial resolution than PET | Poor temporal resolution (2 to 3 s); BOLD is not electrical activity |
| fUS | Ultrasound changes with blood volume | Functional | Cheap, portable, usable with infants | Indirect (blood volume) |
| TMS | Magnetic field from a coil | Stimulation (mainly turns cortex off) | Tests causation in healthy people | Cortex only; safety, depth and mechanism questions |
| tES | Current between two scalp electrodes | Stimulation (turns cortex on) | Cheap | Cortex only; conflicting evidence on cognition |
| tUS | Converging low-amplitude ultrasound beams | Stimulation (on), or lesion at high amplitude | Reaches subcortical structures; no incision | New |

---

## 5.2 Recording Human Psychophysiological Activity

Module 5.1 dealt with imaging. This module deals with **psychophysiological recording**: methods that record physiological activity from the **surface of the human body**, without opening it. The book describes **six** widely studied measures, arranged as three pairs:

| System | Measure 1 | Measure 2 |
|---|---|---|
| Brain activity | Scalp EEG | Magnetoencephalography (MEG) |
| Somatic nervous system | Muscle tension (EMG) | Eye movement (EOG) |
| Autonomic nervous system | Skin conductance (SCL, SCR) | Cardiovascular activity (heart rate, blood pressure, blood volume) |

Learn the grid. A favourite question asks which of a list is a measure of *autonomic* activity, and the answer is skin conductance or cardiovascular activity, never EMG or EOG (which reflect the somatic system's control of skeletal and eye muscles).

### Scalp electroencephalography (EEG)

The **electroencephalogram (EEG)** is a measure of the **gross electrical activity of the brain**. Three words to keep apart: the *record* is the electroencephalogram, the *machine* is the electroencephalograph, and the *technique* is **electroencephalography**. In human studies, each channel of EEG is usually recorded through a disc-shaped electrode, roughly half the size of a small coin, attached to the scalp.

What the scalp EEG picks up is the **sum of all electrical events in the head**. That includes the brain's action potentials and postsynaptic potentials, but also electrical signals from the **skin, muscles, blood and eyes**. So the EEG is not a clear window onto neural activity. Its value as a research and diagnostic tool lies elsewhere: certain **EEG wave forms reliably accompany particular states of consciousness or particular kinds of brain pathology**, such as **epilepsy**.

### EEG wave forms and what they signal

The one wave form the book defines is the **alpha wave**: regular, **8 to 12 per second**, **high-amplitude** waves associated with **relaxed wakefulness**. Figure 5.8 shows four characteristic EEGs. The **aroused** EEG is low-amplitude and fast; the **relaxed** EEG shows bursts of alpha waves; the **asleep** EEG is slower and more irregular; and the **deep sleep** EEG consists of slow, large waves, only a few per second.

The general rule visible in the figure: as arousal falls, EEG waves become **slower and larger**; as arousal rises, they become **faster and smaller** (more "desynchronised").

| Rhythm (standard bands, not all named in this chapter) | Frequency | Typical state |
|---|---|---|
| Beta | above about 13 Hz, low amplitude | Alert, aroused, active thinking |
| **Alpha** | **8 to 12 Hz**, high amplitude, regular | **Relaxed wakefulness**, typically eyes closed |
| Theta | about 4 to 7 Hz | Drowsiness, light sleep |
| Delta | below about 4 Hz, very large | Deep (slow-wave) sleep |

Only alpha is defined in this chapter; the other bands come from Chapter 14 and standard texts and are included because examiners ask for them together.

**Localising the source.** EEG signals **weaken as they spread** from where they originate. So comparing the strength of a wave at many scalp sites can sometimes indicate where it comes from (Cohen, 2017), which is why EEG is normally recorded from **many sites at once**.

> **Trap.** Alpha is **8 to 12 Hz** and goes with **relaxed** wakefulness, not with alert concentration (that is beta) and not with sleep. Opening the eyes or starting to concentrate typically blocks alpha. The 11th-edition figure labels its traces by state (aroused, relaxed, asleep, deep sleep) rather than by band name; older editions included a theta example from a memory task, which has been dropped.

<div class="fig">
<a class="figzoom" href="figs/f_5_8.jpg" target="_blank" rel="noopener"><img src="figs/f_5_8.jpg" loading="lazy" alt="Pinel Fig 5.8: EEG traces for aroused, relaxed (alpha waves), asleep and deep-sleep states, with a 1-second scale"></a>
<p class="cap"><b>Typical electroencephalograms and their psychological correlates.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.8</p>
</div>

### Event-related potentials and the signal-to-noise problem

Psychophysiologists are often less interested in the ongoing background EEG than in the brief EEG changes that accompany specific psychological events. These are called **event-related potentials (ERPs)**. A common type is the **sensory evoked potential**: the change in the cortical EEG produced by the brief presentation of a sensory stimulus such as a click or a flash.

The difficulty is that any EEG recorded after a stimulus contains two things mixed together:

- the **signal**, the part of a recording you are interested in (here, the response to the stimulus); and
- the **noise**, everything else (here, the ongoing background EEG).

The background EEG is usually so large compared with the evoked response that the response is completely hidden in any single trial. Picking it out is like trying to hear one quiet voice in a crowded, noisy hall.

### Signal averaging, step by step

The solution is **signal averaging**, and it is worth understanding exactly how it works, because the same idea returns in module 5.7 as the mean difference image.

1. Present the same stimulus, say a click, many times, for example **1,000 times**, and record the EEG after each one.
2. Line up all 1,000 traces so that each starts at the moment of the click.
3. At the **0-millisecond** point, take the voltage of every trace and compute the mean.
4. Do the same at **1 msec** after the click, then 2 msec, 3 msec, and so on along the whole trace.
5. Plot the means.

Why it works: the response to the click occurs at the **same delay** after every click, so it is the same on every trace and survives averaging. The background EEG is **random** relative to the click; at any given delay it is positive on some trials and negative on others, so averaging over many trials drives it towards zero. Averaging therefore **raises the signal-to-noise ratio**. Figure 5.9 shows both sides of this: averaging stretches of background EEG alone gives a nearly flat line, while averaging stretches that each contain an evoked potential reveals a clear, repeatable wave form.

The product is an **average evoked potential (AEP)**.

<div class="fig">
<a class="figzoom" href="figs/f_5_9.jpg" target="_blank" rel="noopener"><img src="figs/f_5_9.jpg" loading="lazy" alt="Pinel Fig 5.9: averaging 1-second EEG segments gives a flat line for background EEG but a clear average evoked potential after clicks"></a>
<p class="cap"><b>Signal averaging of background EEG and of auditory evoked potentials.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.9</p>
</div>

### Reading an average evoked potential: P300 and far-field potentials

An AEP is analysed wave by wave, and each wave is described by two properties: its **direction** (positive or negative) and its **latency** (the delay after the stimulus). The names encode both: **P300** is a **positive** wave occurring about **300 milliseconds** after the stimulus.

The **P300 wave** appears only after a momentary stimulus that **has meaning for the participant**, for instance a stimulus to which the participant must respond. In Figure 5.10 the click signals that a reward is about to arrive, so it is meaningful and a P300 follows it. The P300 is therefore a marker of cognitive processing (attention to and evaluation of a stimulus), not of simple sensation.

At the other end of the trace are the waves recorded in the **first few milliseconds** after the stimulus. Whether the stimulus matters to the participant makes **no difference** to them. They are known as **far-field potentials**: the electrodes sit on the scalp, but the generators lie a long way off, in the **sensory nuclei of the brain stem**. Early waves therefore reflect the sensory pathway; late waves such as P300 reflect cognition.

A convention that catches people: in EEG and ERP figures, **positive waves are drawn as downward deflections**. So in Figure 5.10 the P300 points *down*.

> **Trap.** Three facts in one item: P300 is **positive** (despite being drawn **downward** by convention), occurs **about 300 msec** after the stimulus, and depends on the stimulus being **meaningful**. Far-field potentials are the **earliest** components (first few msec), originate in the **brain stem** sensory nuclei, and are **unaffected by meaning**. A question that says "far-field potentials reflect the significance of the stimulus" has the two reversed.

<div class="fig">
<a class="figzoom" href="figs/f_5_10.jpg" target="_blank" rel="noopener"><img src="figs/f_5_10.jpg" loading="lazy" alt="Pinel Fig 5.10: average evoked potential to a meaningful click, with early far-field potentials and a P300 drawn downward (positive)"></a>
<p class="cap"><b>An average auditory evoked potential and the P300.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.10</p>
</div>

### Magnetoencephalography (MEG)

**Magnetoencephalography (MEG)** also monitors brain activity from the scalp, but it measures **changes in magnetic fields** on the scalp surface rather than electrical potentials. Every electrical current produces a magnetic field, so changing patterns of neural activity produce tiny changing magnetic fields. These fields are extremely weak, so only those generated **near the surface of the brain** can be picked up from the scalp (Hari & Parkkonen, 2015).

MEG has **two major advantages over EEG**:

1. **Much better spatial resolution**: it can localise changes in cortical electrical activity more precisely.
2. It can localise **subcortical** activity **more reliably** than EEG (Baillet, 2017).

Its **downsides**: it is **expensive**, the machines are **very large** (Figure 5.11), and participants must stay **very still** during recording (Baillet, 2017), although newer designs are trying to relax that requirement (Boto et al., 2018).

(Background, not in the chapter: the magnetic fields are so weak, billions of times weaker than the Earth's field, that they are detected with supercooled sensors called **SQUIDs** inside a magnetically shielded room.)

<div class="fig">
<a class="figzoom" href="figs/f_5_11.jpg" target="_blank" rel="noopener"><img src="figs/f_5_11.jpg" loading="lazy" alt="Pinel Fig 5.11: a participant seated with the head inside the large helmet of an MEG machine"></a>
<p class="cap"><b>A magnetoencephalography (MEG) machine.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.11</p>
</div>

### EEG versus MEG

| | Scalp EEG | MEG |
|---|---|---|
| What is measured | Electrical potentials on the scalp | Magnetic fields on the scalp |
| Signal contamination | Sum of all electrical events in the head (skin, muscle, blood, eyes as well as brain) | Mainly near-surface neural sources |
| Spatial resolution | Poorer (signals are smeared by skull and scalp) | Much better |
| Subcortical localisation | Less reliable | More reliable |
| Temporal resolution | Excellent (milliseconds) | Excellent (milliseconds) |
| Cost and practicality | Cheap, portable | Expensive, huge machine, subject must keep still |

Both EEG and MEG have the **millisecond temporal resolution** that fMRI lacks, because they record the electromagnetic consequences of neural activity directly rather than a slow blood-flow response. That is the deep contrast across 5.1 and 5.2: **fMRI is good at where and poor at when; EEG and MEG are good at when**, with MEG better than EEG at where.

> **Trap.** The 11th edition says MEG beats EEG on **spatial** resolution and on **subcortical** localisation. It does *not* say MEG has better temporal resolution than EEG; both are fast. Note the apparent tension in the book's own account: MEG picks up mainly near-surface activity, yet localises subcortical activity more reliably than EEG. Answer whichever claim the question asks about in the book's terms.

### Muscle tension: electromyography (EMG)

Each skeletal muscle consists of millions of threadlike **muscle fibres**. A fibre contracts in an **all-or-none** fashion when its motor neuron activates it. In a resting muscle, a few fibres are contracting at any moment, which maintains the muscle's overall **tone** (tension); **movement** happens when a large number of fibres contract together.

Everyday language calls anxious people "tense", and the description is physiologically accurate: anxious or otherwise aroused people typically have **high resting muscle tension**. That is why psychophysiologists measure it: muscle tension is an **index of psychological arousal**.

The usual procedure is **electromyography**, and the record is the **electromyogram (EMG)**. It is normally recorded between **two electrodes taped to the skin** over the muscle of interest. The main correlate of stronger contraction is a larger **amplitude** of the raw EMG signal, and the amplitude reflects **how many fibres are contracting** at once.

Raw EMG is a dense burst of spikes and is awkward to work with, so most researchers **integrate** it. A computer adds up the total EMG activity in successive short intervals (for example, every **0.1 second**) and plots the totals. The result is a **smooth curve** whose height is a simple, continuous measure of muscle tension. Figure 5.12 shows a raw and an integrated EMG from a volunteer who tensed a muscle and then gradually relaxed it.

<div class="fig">
<a class="figzoom" href="figs/f_5_12.jpg" target="_blank" rel="noopener"><img src="figs/f_5_12.jpg" loading="lazy" alt="Pinel Fig 5.12: raw EMG spikes and the smooth integrated EMG curve as a volunteer tensed and then gradually relaxed a muscle"></a>
<p class="cap"><b>A raw EMG signal and its integrated version.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.12</p>
</div>

### Eye movement: electrooculography (EOG)

The technique for recording eye movements electrically is **electrooculography**, and the record is the **electrooculogram (EOG)**. It depends on a simple fact: there is a **steady potential difference** across the eyeball, with the **front positive** and the **back negative**. The eye is therefore like a small battery. When it rotates, the positive and negative poles move relative to electrodes placed around it, and the voltage between the electrodes changes.

The standard placement (Figure 5.13):

- **Horizontal** movements: one electrode on **each side** of the eye.
- **Vertical** movements: one electrode **above** and one **below** the eye.

The two traces together describe the eye's path; in the figure they were recorded while the volunteer's gaze traced a circle. EOG is used, for example, to detect the rapid eye movements of REM sleep (Chapter 14).

> **Trap.** The cornea (front) is **positive** and the retina (back) is **negative**. EOG and EMG are both **somatic** measures; neither tells you about autonomic activity. And EMG amplitude reflects the **number of fibres** contracting, not the strength of contraction of individual fibres, because each fibre contracts all-or-none.

<div class="fig">
<a class="figzoom" href="figs/f_5_13.jpg" target="_blank" rel="noopener"><img src="figs/f_5_13.jpg" loading="lazy" alt="Pinel Fig 5.13: electrodes beside and above/below the eye, with horizontal and vertical EOG traces recorded while scanning a circle"></a>
<p class="cap"><b>Electrode placement for electrooculography.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.13</p>
</div>

### Skin conductance: SCL and SCR

Emotional thoughts and experiences are accompanied by **increases in the skin's ability to conduct electricity**. The two most commonly used indices of this **electrodermal activity** are:

- the **skin conductance level (SCL)**: the **background, tonic level** of skin conductance associated with a particular **situation**; and
- the **skin conductance response (SCR)**: the **transient, phasic changes** in conductance associated with **discrete experiences** (a sudden noise, a significant word, a picture).

A good way to fix the difference: SCL is like the water level in a lake over an afternoon; SCR is a wave produced by throwing in a stone.

The physiological basis is not fully understood, but the evidence points strongly to the **sweat glands** (Green et al., 2014). Their main job is to cool the body, but they also tend to become active in emotional situations, and the sweat they release raises the skin's conductivity. Sweat glands cover most of the body, but those of the **hands, feet, armpits and forehead** are especially responsive to emotional stimuli, which is why electrodes are usually placed on the fingers or palm.

> **Trap.** **SCL = level = background, situation-linked; SCR = response = transient, event-linked.** Older texts and many Indian papers use the term **galvanic skin response (GSR)**, which corresponds to the SCR; the 11th edition does not use "GSR". Skin conductance is an **autonomic** (sympathetic) measure, which is why it appears in lie-detection (polygraph) discussions in Chapter 17.

### Cardiovascular activity: heart rate

Phrases like "white with fear" and "blushing bride" show that the link between the **cardiovascular system** and emotion was noticed long before psychophysiology. The cardiovascular system has two parts, the **blood vessels** and the **heart**, and it distributes oxygen and nutrients, removes metabolic wastes, and carries chemical messages. Psychophysiological research commonly uses **three** cardiovascular measures: **heart rate, arterial blood pressure and local blood volume**.

**Heart rate.** The electrical signal produced by each heartbeat can be recorded through **electrodes on the chest**. The record is the **electrocardiogram**, abbreviated **ECG** or **EKG** (the K comes from the original German spelling). The average resting heart rate of a healthy adult is about **70 beats per minute**, and it jumps abruptly at the sound, or even the thought, of something unpleasant such as a dentist's drill.

### Blood pressure

Arterial blood pressure requires **two separate measurements**:

- the **peak** pressure during the periods of heart contraction, the **systoles**; and
- the **minimum** pressure during the periods of relaxation, the **diastoles**.

It is expressed as **systolic over diastolic**, in **millimetres of mercury (mmHg)**. The book gives normal adult resting blood pressure as about **130/70 mmHg**, and defines **hypertension** as a **chronic** blood pressure above **140/90 mmHg**, a serious health hazard.

The familiar clinical device is the **sphygmomanometer**: an inflatable hollow cuff, a rubber bulb to pump it up, and a gauge to read the cuff pressure (*sphygmos* is Greek for "pulse"). The book calls it crude; research uses more reliable, fully automated methods.

> **Trap.** The numbers are the book's: normal about **130/70**, hypertension **above 140/90** (chronic). Current clinical guidelines in some countries define hypertension at a lower threshold (130/80), but an MCQ built on Pinel expects **140/90**. Systolic is the **higher** number (contraction); diastolic is the **lower** (relaxation).

### Blood volume: plethysmography

Changes in the **volume of blood** in particular parts of the body accompany psychological events. The best-known example is **genital engorgement** during sexual arousal, in both males and females. **Plethysmography** is the general name for techniques that measure changes in the blood volume of a body part (*plethysmos* means "an enlargement").

Two methods:

1. **Strain gauge.** Wrap a strain gauge around the target tissue and record changes in its volume. Useful for fingers and similarly shaped organs, but limited in where it can be applied.
2. **Light absorption.** Shine a light through the tissue and measure how much is absorbed. The more blood a structure contains, the more light it absorbs.

---|---|---|---|---|
| Scalp EEG | Electroencephalogram | Brain | States of consciousness, pathology such as epilepsy; ERPs | Disc electrodes on scalp, many sites |
| MEG | Magnetoencephalogram | Brain | Near-surface cortical activity with good spatial localisation | Large magnetic-sensing machine |
| Muscle tension | EMG (raw, then integrated) | Somatic | Arousal (resting tension) | Two skin electrodes over the muscle |
| Eye movement | EOG | Somatic | Eye position and movement | Electrodes beside, above and below the eye |
| Skin conductance | SCL (tonic), SCR (phasic) | Autonomic | Emotional arousal | Electrodes on skin, usually hand |
| Cardiovascular | ECG/EKG; BP; plethysmogram | Autonomic | Heart rate; systolic/diastolic pressure; local blood volume | Chest electrodes; cuff; strain gauge or light |

---

## 5.3 Invasive Physiological Research Methods

Modules 5.1 and 5.2 were non-invasive and mostly human. This module turns to the **direct** methods used mainly with **laboratory animals**. Most of them fall into three categories: **lesion methods**, **electrical stimulation methods** and **invasive recording methods**. All three usually require putting something into a precise location deep in the brain, so the module begins with the procedure that makes that possible.

### Stereotaxic surgery: the atlas and the instrument

**Stereotaxic surgery** is the first step in many biopsychological experiments. It is the means by which an experimental device (an electrode, a cannula, a knife) is positioned precisely in the depths of the brain, which the surgeon cannot see. It needs two things: an **atlas** that gives directions to the target, and an **instrument** that gets the device there.

**The stereotaxic atlas.** It works like a road atlas, with one difference: the Earth's surface has two dimensions and the brain has three. So the brain is represented as a **series of maps, one per page**, each showing a single two-dimensional **frontal (coronal) slice**. Every distance in the atlas is given in **millimetres from a reference point**. In most rat atlases the reference point is **bregma**, the point on top of the skull where two of the major **sutures** (the seams between skull bones) cross.

**The stereotaxic instrument** (Figure 5.14, a rodent model) has two parts:

- a **head holder**, which clamps the animal's head in a fixed, standard position and orientation; and
- an **electrode holder**, which carries the device to be inserted and can be moved by precision gears in **three dimensions**: **anterior-posterior, dorsal-ventral and lateral-medial**.

Figure 5.15 walks through implanting an electrode in the **rat amygdala**:

1. The atlas page showing the amygdala is the one for a frontal section **2.8 mm posterior to bregma**, and the target's lateral and depth coordinates are read off that page.
2. A hole is drilled **2.8 mm posterior** and **4.5 mm lateral** to bregma. The electrode holder is positioned over the hole and the electrode lowered **8.5 mm** (that is, 8.5 mm ventral).
3. To keep the electrode fixed for later testing, a few **stainless steel screws** are set into the skull and **dental acrylic** is moulded around them and the electrode's connector; once it hardens, the whole assembly is cemented in place.

The idea to take away: because all rats of a given strain, age and size have nearly the same brain geometry relative to bregma, three numbers from an atlas let a surgeon reach a structure a few millimetres across without ever seeing it.

<div class="fig">
<a class="figzoom" href="figs/f_5_14.jpg" target="_blank" rel="noopener"><img src="figs/f_5_14.jpg" loading="lazy" alt="Pinel Fig 5.14: a rodent stereotaxic instrument with head holder and electrode holder on precision rails"></a>
<p class="cap"><b>A stereotaxic instrument for rodent surgery.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.14</p>
</div>

<div class="fig">
<a class="figzoom" href="figs/f_5_15.jpg" target="_blank" rel="noopener"><img src="figs/f_5_15.jpg" loading="lazy" alt="Pinel Fig 5.15: atlas page 2.8 mm posterior to bregma, hole drilled 4.5 mm lateral, electrode lowered 8.5 mm and fixed with screws and dental acrylic"></a>
<p class="cap"><b>Stereotaxic surgery: implanting an electrode in the rat amygdala.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.15</p>
</div>

### Lesion methods: the logic

In the **lesion methods**, part of the brain is damaged, destroyed or inactivated, and the animal's behaviour is then carefully assessed to infer what the lesioned structure did. The book discusses four types: **aspiration lesions, radio-frequency lesions, knife cuts and reversible lesions**.

### Aspiration lesions

When the target is **cortical tissue that the surgeon can see and reach**, **aspiration** is often the method of choice. The tissue is sucked away through a **fine-tipped, hand-held glass pipette**. Because the underlying **white matter is slightly more resistant to suction** than the cortical grey matter, a skilled surgeon can peel away the cortex layer by layer while leaving the white matter and the major blood vessels intact.

### Radio-frequency lesions

For small **subcortical** targets, the usual method is to lower an electrode stereotaxically until its **tip** sits in the target, then pass **radio-frequency** (high-frequency) **current** out of it. The current **heats** and kills the surrounding tissue. Three variables control how big the lesion is and what shape it takes: how **long** the current flows, how **strong** it is, and the **shape of the electrode tip**.

### Knife cuts

**Sectioning** (cutting) is used to stop conduction in a **nerve or tract**. A tiny, well-placed cut can do this unambiguously without much damage to surrounding tissue. The obvious problem is how to put a knife into the depths of the brain without wrecking everything above the target. One solution (Figure 5.16) is a device that is lowered stereotaxically with its blade retracted; once in position, the blade swings out to make the cut. In the figure, the **anterior commissure** is being sectioned.

<div class="fig">
<a class="figzoom" href="figs/f_5_16.jpg" target="_blank" rel="noopener"><img src="figs/f_5_16.jpg" loading="lazy" alt="Pinel Fig 5.16: a stereotaxically lowered knife whose blade swings out to section the anterior commissure"></a>
<p class="cap"><b>A device for making subcortical knife cuts.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.16</p>
</div>

### Reversible lesions

**Reversible lesions** temporarily eliminate the activity of a brain area while tests are carried out. Their great advantage is methodological: **the same animal can be tested repeatedly in both the lesion and the control conditions**, so each subject serves as its own control. The two commonest ways of producing one are:

- **cooling** the target structure; and
- injecting a local **anaesthetic** such as **lidocaine** into it.

> **Trap.** Older editions called the cooling method **cryogenic blockade** (a cryoprobe chills the neurons below the temperature at which they can fire), and older keys may use that term. The 11th edition simply lists cooling and lidocaine as the two common ways of making a **reversible lesion**. Match each lesion type to its target: **aspiration = visible cortex**; **radio-frequency = small subcortical**; **knife cut = a nerve or tract**; **reversible = any site, temporary**.

| Lesion type | How | Typical target | Main feature |
|---|---|---|---|
| Aspiration | Suction through a glass pipette | Accessible cortex | Spares underlying white matter and major vessels |
| Radio-frequency | Heat from high-frequency current at an electrode tip | Small subcortical structures | Size set by current duration, intensity, tip shape |
| Knife cut | Stereotaxically placed swinging blade | Nerves and tracts | Stops conduction with little collateral damage |
| Reversible | Cooling or lidocaine | Any area | Same animal tested in lesion and control states |
| Selective neurotoxic (module 5.4) | Kainic or ibotenic acid; 6-OHDA | Cell bodies; NE/DA neurons | Spares fibres of passage or non-target neurons |

### Interpreting lesion effects

Pinel and Barnes stress that **lesion effects are deceptively hard to interpret**. Brain structures are small, folded and tightly packed, so even an excellent surgeon cannot destroy one completely without also damaging its neighbours. Researchers nonetheless tend to forget this. A lesion that spares much of the amygdala and damages several nearby structures ends up being called, in shorthand, an "amygdala lesion".

That harmless-looking shorthand misleads in two opposite directions:

1. If you assume "amygdala lesions" damage **nothing else**, you may wrongly credit the amygdala with **every** behavioural effect of the lesion, including effects actually caused by damage to neighbouring structures.
2. If you assume "amygdala lesions" destroy **the whole amygdala**, you may wrongly conclude that the amygdala plays **no part** in behaviours the lesion left unchanged, when the spared portion may be doing that job.

The first error over-attributes function; the second under-attributes it. Chapter 12's VMH story (where the "satiety centre" effect turned out partly to reflect damage to nearby paraventricular fibres) is a textbook instance of the first.

### Bilateral and unilateral lesions

As a general rule, with several notable exceptions, **unilateral** lesions (restricted to one side of the brain) produce **much milder** behavioural effects than **symmetrical bilateral** lesions (involving both sides), especially in non-human species. The effects of some unilateral lesions are hard to detect at all, because the intact homologous structure on the other side can largely carry the load. For that reason, **most experimental lesion studies use bilateral lesions**.

> **Trap.** "Unilateral lesions usually have effects as large as bilateral ones" is false. The well-known **exceptions** come from the lateralised human cortex: a unilateral left-hemisphere lesion can devastate language (Chapter 16). The rule is stated for non-human animals especially.

### Electrical stimulation

Clues to a structure's function can also be obtained by **stimulating** it electrically. Brain stimulation is usually delivered across the two tips of a **bipolar electrode**: two insulated wires wound tightly together and cut at the end, so current flows between the two bare tips. **Weak pulses** of current produce an **immediate increase in firing** of the neurons near the tip.

Why it is useful:

- It often has behavioural effects, and these are usually **opposite** to the effects of a **lesion** at the same site. Lesion and stimulation results at one site therefore check each other.
- It can elicit whole **behavioural sequences**, including **eating, drinking, attacking, copulating and sleeping**.

Which behaviour appears depends on **three** things: the **location of the electrode tip**, the **parameters of the current** (intensity, frequency, duration), and the **test environment** in which stimulation is given (stimulation that elicits eating in a rat with food available may elicit something else when no food is present).

Because it is invasive, brain stimulation is usually limited to non-human subjects, but the brains of **conscious human patients** are sometimes stimulated for **therapeutic** reasons (Jonas et al., 2014). (The most familiar example from later chapters is deep brain stimulation for Parkinson's disease.)

### Invasive electrophysiological recording: four methods

The book describes **four** invasive recording methods, which differ in how much of the nervous system each electrode "hears" and what kind of signal results. They go from the smallest scale to the largest (Figure 5.17).

#### Intracellular unit recording

**Intracellular unit recording** gives a **moment-by-moment record of the graded fluctuations in one neuron's membrane potential**: the postsynaptic potentials as well as the action potentials (Chapter 4). The microelectrode tip sits **inside** the neuron.

Its limitation is mechanical. Keeping a microelectrode tip inside a single neuron is very difficult if the animal moves, so most such experiments use **chemically immobilised** animals (Long & Lee, 2012). Special electrodes now being developed allow intracellular recording in **freely moving** animals (Lee & Brecht, 2018).

#### Extracellular unit recording

In **extracellular unit recording**, the microelectrode tip sits in the **extracellular fluid next to** a neuron. Each time the neuron fires, the electrical disturbance registers as a **blip** at the tip. So this method records **when the neuron fires** but tells you **nothing about its membrane potential** (no PSPs, no resting potential).

Recording from one neuron in a freely moving animal is hard because the tip tends to drift away, but **special flexible microelectrodes** that move slightly with the brain make it possible. Originally neurons were recorded one at a time, each at the tip of its own electrode. Now, by analysing the **correlations among the signals picked up by several electrodes** implanted in the same general area, researchers can record extracellular signals from **up to about 1,000 neurons** simultaneously (Callaway & Garg, 2017; Jun et al., 2017).

#### Multiple-unit recording

In **multiple-unit recording**, the electrode tip is **much larger** than a microelectrode, so it picks up signals from **many neurons**, and small movements of the animal barely affect the overall signal. The many action potentials picked up are fed into an **integrating circuit** that adds them together. The record is a graph of the **total number of action potentials per unit of time** (for example, per 0.1 second). Compare the integrated EMG of 5.2: same idea, applied to neurons instead of muscle fibres.

#### Invasive EEG recording

EEG can also be recorded through **implanted electrodes** instead of scalp electrodes, in non-human animals and sometimes in human patients (Fox et al., 2018). In animals, **cortical** EEG is often recorded through **stainless steel skull screws**, and **subcortical** EEG through **implanted wire electrodes**. A large electrode picks up general changes in electrical activity, and, as Figure 5.17 notes, the EEG signal **bears no obvious relation to the firing of individual neurons**.

| Method | Electrode | What is recorded | Scale | Key limitation |
|---|---|---|---|---|
| Intracellular unit | Microelectrode **inside** one neuron | Graded membrane potential (PSPs and APs) | One neuron, millivolts | Usually needs an immobilised animal |
| Extracellular unit | Microelectrode **beside** one neuron | Firing (blips) only, no membrane potential | One neuron (or up to ~1,000 with arrays) | Tip may drift in moving animals |
| Multiple-unit | Larger electrode | Summed action potentials per unit time | Many nearby neurons | Loses individual-neuron identity |
| Invasive EEG | Large electrode, skull screw or implanted wire | Gross electrical activity | Large populations, microvolts | Not obviously related to neural firing |

> **Trap.** Only **intracellular** recording shows the **membrane potential**; extracellular recording shows **only firing**. A question asking which method would reveal an IPSP that did not trigger an action potential has one right answer: intracellular unit recording.

---

<div class="fig">
<a class="figzoom" href="figs/f_5_17.jpg" target="_blank" rel="noopener"><img src="figs/f_5_17.jpg" loading="lazy" alt="Pinel Fig 5.17: intracellular, extracellular, multiple-unit and invasive EEG recordings compared, from one neuron to large populations"></a>
<p class="cap"><b>Four ways of recording electrical activity of the nervous system.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.17</p>
</div>

## 5.4 Pharmacological Research Methods

Module 5.3 manipulated and recorded from the brain surgically and electrically. This module does it **chemically**. The central strategy of **psychopharmacology** is to give drugs that **increase or decrease the effects of particular neurotransmitters** and observe what happens to behaviour. The module covers four topics: how drugs are given, how chemicals can make selective lesions, how the brain's chemical activity is measured, and how particular neurotransmitters and receptors are located.

### Routes of drug administration

In most psychopharmacological experiments, drugs reach the subject in one of three general ways:

1. **Fed** to the subject (oral).
2. Delivered through a tube into the **stomach** (**intragastrically**).
3. **Injected hypodermically**, by one of four routes:

| Route | Abbreviation | Into |
|---|---|---|
| Intraperitoneal | **IP** | The **peritoneal cavity** of the abdomen |
| Intramuscular | **IM** | A large **muscle** |
| Subcutaneous | **SC** | The **fatty tissue beneath the skin** |
| Intravenous | **IV** | A large **surface vein** |

The problem with all of these **peripheral** routes is that many drugs **do not readily cross the blood-brain barrier**. The solution is to deliver tiny amounts **directly into the brain** through a **cannula**, a fine hollow tube **implanted stereotaxically**. This also allows the drug to be confined to one structure.

> **Trap.** "Subcutaneous" means into the **fat beneath the skin**, not into a vein (IV) or muscle (IM). IP (into the abdominal cavity) is the workhorse route for rats and mice. A **cannula** is the implanted tube for central administration; do not confuse it with the dialysis probe below, which *collects* chemicals rather than delivering them.

### Selective chemical lesions: neurotoxins

Surgical, radio-frequency and reversible lesions share a problem: they affect **all** neurons in the target area, which makes their effects hard to interpret. **Neurotoxins** (neural poisons) with an affinity for particular components of the nervous system allow more **selective** lesions. There are many; the book names three:

- **Kainic acid** and **ibotenic acid**: when **microinjected**, they are taken up preferentially by **cell bodies** at the tip of the cannula and destroy those neurons, while largely sparing neurons whose **axons merely pass through** the area. That solves a classic lesion problem: an electrolytic or radio-frequency lesion at a site destroys the "fibres of passage" from distant neurons as well as the local cells, so a behavioural change could come from either.
- **6-hydroxydopamine (6-OHDA)**: taken up **only by neurons that release norepinephrine or dopamine**, leaving other neurons at the injection site unharmed. It is the standard way of making an animal model of Parkinson's disease by destroying dopamine neurons.

> **Trap.** Kainic and ibotenic acid are selective by **cell part** (cell bodies, sparing fibres of passage). 6-OHDA is selective by **neurotransmitter** (noradrenergic and dopaminergic neurons only). An option claiming 6-OHDA destroys serotonergic neurons, or that kainic acid destroys axons of passage, is wrong.

### The 2-deoxyglucose technique

The book highlights two methods for measuring the brain's chemical activity, and the first is the **2-deoxyglucose (2-DG) technique**. It is the animal ancestor of FDG-PET and rests on the same trick.

1. Inject the animal with **radioactive 2-DG**.
2. Place it in a test situation where it engages in the activity of interest.
3. Because 2-DG resembles glucose, the brain's main energy source, **active neurons absorb it at a high rate**, but they **cannot metabolise it**, so it accumulates in them.
4. **Kill the animal**, remove the brain and slice it.
5. Subject the slices to **autoradiography**: coat them with photographic emulsion, store them in the dark for a few days, and develop them much as film is developed. Areas that absorbed a lot of radioactive 2-DG show up as **black spots**.
6. The density of the spots in different regions can then be **colour-coded**.

Figure 5.18 shows the result in a **Richardson's ground squirrel** that, after 2-DG injection, viewed brightly lit black and white stripes for **45 minutes** through its **left eye** with the **right eye covered**. In this species almost all visual fibres cross to the opposite side, so the label piled up mainly in the visual structures of the **right hemisphere**, the side opposite the open eye.

> **Trap.** 2-DG with autoradiography requires the animal to be **killed**, so it gives one snapshot of activity per animal. FDG-PET applies the same principle to **living humans**, scanning the radioactivity in place. And in the ground squirrel figure, the uncovered eye is the **left**, so the labelled hemisphere is the **right**.

<div class="fig">
<a class="figzoom" href="figs/f_5_18.jpg" target="_blank" rel="noopener"><img src="figs/f_5_18.jpg" loading="lazy" alt="Pinel Fig 5.18: three frontal sections of a Richardson&#x27;s ground squirrel brain with 2-DG radioactivity concentrated in right-hemisphere visual structures"></a>
<p class="cap"><b>The 2-deoxyglucose technique in the ground squirrel.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.18</p>
</div>

### Cerebral dialysis

The second method, **cerebral dialysis** (better known in the wider literature as **microdialysis**), measures the **extracellular concentration of specific neurochemicals in behaving animals**. That is its distinctive advantage: most other neurochemical measures require **killing** the animal to extract tissue.

How it works: a fine tube with a short **semipermeable** section is implanted so that the semipermeable section lies in the structure of interest. Extracellular chemicals from that structure **diffuse into the tube** across the membrane. From there they can be collected for **freezing, storage and later analysis**, or carried in solution directly to a **chromatograph**, a device that measures the chemical constituents of liquids or gases.

So a researcher can, for example, sample dopamine levels in the nucleus accumbens every few minutes while a rat self-administers a drug, and relate the chemical changes to the behaviour as it happens.

| | 2-DG technique | Cerebral dialysis |
|---|---|---|
| Measures | Which areas were metabolically active during a test | Extracellular concentration of specific chemicals |
| Animal state | Killed after the test | Alive and behaving throughout |
| Time course | One snapshot per animal | Repeated samples over time |
| Read-out | Autoradiography (black spots), colour-coded | Chromatography |

### Locating neurotransmitters and receptors

A key step in understanding what a particular neurotransmitter or receptor does psychologically is finding out **where in the brain it is**. The book describes two techniques. Both expose **brain slices** to a **labelled ligand** of the molecule being studied (a ligand of a molecule is another molecule that binds to it), and both show where the label ends up. They differ in **what** the label binds to.

### Immunocytochemistry

**Immunocytochemistry** exploits the immune system. When a foreign protein (an **antigen**) enters an animal, the body makes **antibodies** that bind to it and help remove or destroy it; this is the **immune reaction**. Neurochemists have produced stocks of antibodies against the brain's **peptide neurotransmitters (neuropeptides)** and their **receptors**.

The procedure: label the antibodies with a **dye** or a **radioactive element**, expose brain slices to them, and look for where the dye or radioactivity accumulates. Those regions contain the target **neuroprotein**.

Immunocytochemistry only binds **proteins**, so how can it locate a non-peptide transmitter such as dopamine or norepinephrine? Indirectly, through the transmitter's **synthetic enzymes**. All enzymes are proteins, and only neurons that release a particular neurotransmitter are likely to contain **all** the enzymes needed to make it. So a labelled antibody against one of those enzymes marks the neurons that use the transmitter. Figure 5.19 shows a section through a rat's **pons** in which **noradrenergic neurons** have bound the antibody to **dopamine-beta-hydroxylase**, the enzyme that converts **dopamine to norepinephrine**. Dopaminergic neurons lack that enzyme, so the stain picks out noradrenergic cells specifically.

<div class="fig">
<a class="figzoom" href="figs/f_5_19.jpg" target="_blank" rel="noopener"><img src="figs/f_5_19.jpg" loading="lazy" alt="Pinel Fig 5.19: rat pons section with noradrenergic neurons labelled by the antibody to dopamine-beta-hydroxylase"></a>
<p class="cap"><b>Immunocytochemistry of noradrenergic neurons in the rat pons.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.19</p>
</div>

### In situ hybridisation

**In situ hybridisation** is another way of locating **peptides and other proteins**, but it targets an earlier step in their production. Every peptide and protein is made from instructions carried on strands of **messenger RNA (mRNA)**. The nucleotide base sequences of the mRNAs that direct the synthesis of many neuroproteins are known, and **hybrid RNA strands** with the **complementary** base sequence can be made artificially.

The steps:

1. Obtain hybrid RNA strands whose base sequence is complementary to the mRNA for the target neuroprotein.
2. Label the hybrid strands with a **dye or radioactive element**.
3. Expose brain slices to the labelled strands. They bind to the complementary mRNA, marking the neurons that are **making** (and so releasing) the target neuroprotein.

### Which chemical method answers which question

| Question | Method | Binds to / measures | Living or dead tissue |
|---|---|---|---|
| Which brain areas were active during a behaviour (animal)? | 2-DG + autoradiography | Accumulated radioactive glucose analogue | Dead (sliced) |
| Which areas are active (human)? | FDG-PET | Accumulated radioactive glucose analogue | Living |
| What is the extracellular level of a chemical during behaviour? | Cerebral dialysis | Chemicals diffusing across a membrane | Living, behaving |
| Where is a neuropeptide, receptor or enzyme (the protein itself)? | Immunocytochemistry | **Protein**, via labelled **antibody** | Slices |
| Which neurons are making a given protein? | In situ hybridisation | **mRNA**, via labelled complementary **RNA** | Slices |
| Where are receptors or transporters in a living human? | PET with labelled ligand | Target molecule | Living |

> **Trap.** **Immunocytochemistry = antibody binds protein. In situ hybridisation = complementary RNA binds mRNA.** Swapping these is the commonest error on this topic. Note also that immunocytochemistry locates small-molecule transmitters **indirectly**, through the **enzymes** that synthesise them.

---

## 5.5 Genetic Methods

Genetics has advanced so fast that methods routine in biopsychology labs today would have sounded like science fiction a few decades ago. These methods let researchers **add, remove and alter specific genes**. The book groups them into three categories: **(1) gene knockout techniques, (2) gene knockin techniques and (3) gene editing techniques**, and then adds two tools that grew out of genetic engineering: **fluorescent proteins** (GFP and the brainbow) and **optogenetics**.

### Gene knockout techniques: the melanopsin mice

**Gene knockout techniques** create organisms that **lack a particular gene** (e.g. Gingras et al., 2014). Mice, the favoured mammals of genetic research, produced this way are called **knockout mice**.

The book's worked example concerns circadian rhythms (Chapter 14). **Melanopsin** is a protein found in some neurons of the mammalian **retina**, and it had been implicated in how light controls **circadian** (about 24-hour) rhythms such as the daily cycles of sleep, eating and body temperature. **Ruby and colleagues (2002)** and **Hattar and colleagues (2003)** studied **melanopsin knockout mice**, in which the gene for making melanopsin had been deleted.

The result: knocking out the gene **impaired, but did not eliminate**, the mice's ability to adjust their circadian rhythms to changes in the light-dark cycle. The inference: melanopsin **contributes** to the control of circadian rhythms by light, but it is **not the only factor**; other photoreceptive mechanisms must also be feeding light information to the circadian clock.

Pinel and Barnes say this outcome is **typical** of gene knockout studies of behaviour. Many genes have been found that contribute to particular behaviours, but other mechanisms are invariably involved too. It is tempting to think in terms of "a gene for" each behaviour, but every behaviour depends on **many genes interacting with one another and with experience**, through **epigenetic mechanisms** (Chapter 2).

> **Trap.** The melanopsin knockout result was **partial impairment**, not abolition. An option saying "melanopsin knockout mice could not entrain to light" is wrong. And note the general caution behind it: a knockout animal develops from conception without the gene, so other systems may **compensate**, and the effect of losing the gene in development can differ from the effect of losing it in adulthood. That is one reason the 11th edition emphasises gene editing at chosen times (below).

### Gene knockin techniques and transgenic mice

It is now possible to **replace one gene with another** or to **add a gene that the organism does not normally have**. These are **gene knockin techniques**. One application is to insert **pathological human genes** into other animals, usually mice. Mice that carry genetic material from another species are called **transgenic mice**.

The book's example comes from **Shen and colleagues (2008)**. A **Scottish family** with an unusually high rate of **schizophrenia** had been found to carry a **defective gene**, and the team inserted the human version of that faulty gene into mice. (The gene, not named in the chapter, is *DISC1*, "disrupted in schizophrenia 1".) The transgenic mice showed a range of **cerebral abnormalities**, including a **reduced cerebral cortex** and **enlarged ventricles**, together with atypical behaviours reminiscent of human schizophrenia. Enlarged ventricles are one of the best-replicated structural findings in human schizophrenia (Chapter 18), which is what makes the model persuasive.

The longer-term therapeutic hope, **replacing faulty genes** in patients with genetic disorders, is described as exciting but **not yet realised**.

| | Knockout | Knockin |
|---|---|---|
| What is done | A gene is deleted or inactivated | A gene is replaced, or a new (often foreign) gene is added |
| Typical product | Knockout mouse | Transgenic mouse (if the added gene is from another species) |
| Book's example | Melanopsin knockout mice (Ruby et al., 2002; Hattar et al., 2003) | Human schizophrenia-linked gene in mice (Shen et al., 2008) |
| Finding | Circadian light adjustment impaired, not abolished | Reduced cortex, enlarged ventricles, schizophrenia-like behaviour |

### Gene editing: CRISPR/Cas9

Because behaviour reflects many genes interacting with experience over development, researchers want to change a gene **at a particular time** in development rather than for the animal's whole life. Modern **gene editing techniques** allow exactly that (Heidenreich & Zhang, 2016), and so help control for the interaction of genes with experience.

Of the many available, the **CRISPR/Cas9 method** is generating the most excitement. In its most widely used version:

1. **Cas9**, a protein, is linked to a strand of RNA called the **guide-RNA**.
2. The guide-RNA consists of a nucleotide base sequence **complementary** to one or more stretches of **DNA**; it is the "address" that tells Cas9 where to act.
3. The guide-RNA/Cas9 combination is packaged into a **virus**.
4. The virus is injected either **peripherally**, to edit the genome of the **whole organism**, or **intracranially into a specific brain region**, to study the **local** effects of editing a gene only in cells of that region.
5. Inside a cell, the guide-RNA lines up with its complementary DNA, and **Cas9 can then inhibit or activate** the gene through various mechanisms.

Two further capabilities matter. Cas9 activity can itself be **regulated**, so a researcher can alter a gene's expression **reversibly** in a chosen brain region and watch the effect on behaviour. And Cas9 can be used to alter an organism's **epigenome** (Gomez, Beitnere, & Segal, 2019), not just its DNA sequence, which is why the chapter's "thinking about epigenetics" theme appears here.

> **Trap.** The learning objective in the 11th edition misprints the method as "CRISP-Cas9"; the correct name is **CRISPR/Cas9**. Know the division of labour: the **guide-RNA finds the target** (by complementary base pairing with DNA), **Cas9 acts on it**, and a **virus delivers** the package. Unlike a classic knockout, CRISPR/Cas9 editing can be done **at a chosen time**, **in a chosen region**, and **reversibly**.

### Green fluorescent protein

**Green fluorescent protein (GFP)** glows bright green when exposed to **blue light**. Its source is a **jellyfish** that lives in Pacific waters off **western North America**, from which **Shimomura, Johnson and Saiga (1962)** first purified it. **Martin Chalfie, Osamu Shimomura and Roger Tsien** shared the **2008 Nobel Prize in Chemistry** for its discovery and development.

For three decades GFP remained a curiosity; it became a research tool only once its **gene had been identified and cloned, in the early 1990s**. The idea is then to make the GFP gene active **only in the particular cells under study**, so those cells, and only those, glow. There are two ways to do this:

- insert the GFP gene **only into the target cells**; or
- introduce it into **all cells** but arrange for it to be **expressed only in the target cells**.

**Chalfie and colleagues (1994)** were the **first to use GFP to visualise neurons**. They inserted the GFP gene into the small, transparent roundworm ***Caenorhabditis elegans***, into a region of its chromosomes that controls the development of **touch receptor neurons**, so those neurons glowed green (Figure 5.20). GFP has since been expressed in many plant and animal species, **including humans**.

The evolutionary-perspective theme surfaces here: a protein that evolved in a jellyfish turned out to be one of the most useful tools in neuroscience.

<div class="fig">
<a class="figzoom" href="figs/f_5_20.jpg" target="_blank" rel="noopener"><img src="figs/f_5_20.jpg" loading="lazy" alt="Pinel Fig 5.20: the transparent roundworm Caenorhabditis elegans with its touch receptor neurons glowing green (Chalfie et al., 1994)"></a>
<p class="cap"><b>Touch receptor neurons of C. elegans labelled with GFP.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.20</p>
</div>

### Brainbow

**Livet and colleagues (2007)** took GFP a large step further. First, **Tsien (1998)** had found that small alterations to the GFP gene produced proteins that **fluoresce in different colours**. Livet's team then introduced genes for three such colour variants (the book lists cyan, yellow and blue fluorescent proteins) into the genomes of developing mice in a way that made them **expressed in developing neurons**.

The key is that **each neuron made different amounts of the three proteins**. Just as a printer can produce any colour from three inks mixed in different proportions, each neuron ended up with its own **distinctive colour**. Because neighbouring neurons were now distinguishable, an individual axon could be **followed to its destination** through the dense tangle of other cells. The technique is called the **brainbow** (Figure 5.21).

> **Trap.** GFP fluoresces **green** under **blue** light. It came from a **jellyfish**, not a roundworm; **C. elegans** was the **first animal whose neurons were visualised** with it (Chalfie et al., 1994). The **brainbow** (Livet et al., 2007) depends on **colour variants** of GFP developed by **Tsien (1998)**, mixed in different proportions in each neuron, and its purpose is **tracing axons**.

<div class="fig">
<a class="figzoom" href="figs/f_5_21.jpg" target="_blank" rel="noopener"><img src="figs/f_5_21.jpg" loading="lazy" alt="Pinel Fig 5.21: brainbow-labelled neurons, each a distinct colour, allowing individual axons to be traced"></a>
<p class="cap"><b>The brainbow: each neuron labelled with a different colour.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.21</p>
</div>

### Other uses of fluorescent proteins

Beyond brainbows, fluorescent proteins have allowed researchers to:

1. **label specific neurotransmitters**, so that their activity can be watched;
2. **label synaptic vesicle proteins**, so that the **fusion of vesicles with the presynaptic membrane** (exocytosis) can be observed;
3. **visualise postsynaptic potentials**, using fluorescent proteins that light up when the membrane depolarises or hyperpolarises; and
4. **observe neurotransmitter-receptor binding**, using engineered receptors that light up when they bind their transmitter.

The common principle: a fluorescent protein is attached to, or built into, a molecule whose activity you want to see, so that a chemical or electrical event becomes a visible flash.

### Optogenetics: a neural light switch

**Opsins** are **light-sensitive ion channels** found in the cell membranes of certain **bacteria and algae**. When light falls on them they open and let ions into the cell. Depending on the particular opsin, light either **depolarises** or **hyperpolarises** the membrane they sit in.

Opsins could not be used in neuroscience until their **gene was identified and rendered expressible in a mammalian cell**, first achieved in **2003**. Soon afterwards, neuroscientists began using genetic engineering to insert opsin genes, or variants of them, into **particular types of neurons**. Once a type of neuron carries an opsin, light can switch it on (depolarise) or off (hyperpolarise). This method is **optogenetics**, and it is revolutionising how the brain is studied.

How it is done in a living animal:

1. Inject the animal with a **virus carrying an opsin gene** designed to be expressed only in one **type** of neuron (for example, **dopaminergic** neurons; Chang et al., 2016).
2. Implant an **optical fibre** in the relevant brain region.
3. Shine light through the fibre to open the opsin channels, so that **only the targeted neurons** increase or decrease their activity.
4. Recent developments use **wireless** technology so that optogenetics can be used in **freely moving** animals (Gutruf & Rogers, 2018).

Why it is such a leap: electrical stimulation (5.3) activates **every** neuron near the electrode tip, of every type, and lesions destroy every neuron in an area. Optogenetics can switch **one genetically defined type** of neuron on or off, **reversibly**, with **millisecond** timing, in a behaving animal. It combines the specificity of genetic targeting with the speed of light.

(Background beyond the chapter: the opsin most used to excite neurons is **channelrhodopsin-2**, which responds to blue light by letting positive ions in; the classic inhibitory tool is **halorhodopsin**, which responds to yellow light by moving chloride ions into the cell.)

> **Trap.** Opsins in optogenetics come from **bacteria and algae**, not from the human retina (the retina's photopigments are a different family, even though melanopsin is also an opsin-type protein). And optogenetics manipulates activity; **GFP** merely **labels** cells. A question that credits GFP with turning neurons on is wrong.

### Abbreviations from Part One

Pinel and Barnes joke that biopsychologists suffer from a fear of leaving any term unabbreviated, and they test Part One with a list of abbreviations. Indian papers love the same kind of item, so here is the full list, with the extra abbreviations used in this note.

| Abbreviation | Full term |
|---|---|
| CT | Computed tomography |
| MRI | Magnetic resonance imaging |
| PET | Positron emission tomography |
| 2-DG | 2-deoxyglucose |
| fMRI | Functional MRI |
| MEG | Magnetoencephalography |
| TMS | Transcranial magnetic stimulation |
| EEG | Electroencephalogram |
| ERP | Event-related potential |
| AEP | Average evoked potential |
| EMG | Electromyogram |
| EOG | Electrooculogram |
| SCL | Skin conductance level |
| SCR | Skin conductance response |
| ECG / EKG | Electrocardiogram |
| IP | Intraperitoneal |
| IM | Intramuscular |
| IV | Intravenous |
| SC | Subcutaneous |
| 6-OHDA | 6-hydroxydopamine |
| GFP | Green fluorescent protein |
| fUS | Functional ultrasound imaging |
| tES | Transcranial electrical stimulation |
| tUS | Transcranial ultrasound stimulation |
| DTI | Diffusion tensor imaging |
| BOLD | Blood-oxygen-level-dependent |
| FDG | Fluorodeoxyglucose |

---

## Part Two: Behavioural Research Methods of Biopsychology

Part Two moves from the brain side of biopsychology to the behaviour side. The contrast in aims is worth stating precisely. Neural activity is inherently invisible, so the **nervous-system methods** of Part One exist to **make the unobservable observable**. Behaviour, by contrast, is visible but messy, so the **behavioural methods** exist to **control, simplify and objectify** it.

A single set of procedures developed to study one behavioural phenomenon is called a **behavioural paradigm**. Each paradigm normally has two components: a method for **producing** the behaviour under study, and a method for **measuring** it objectively. Keep this two-part definition in mind; the paradigms of 5.8 (the elevated plus maze, the Morris water maze and so on) are all instances of it.

## 5.6 Neuropsychological Testing

### Why neuropsychological testing matters

A patient suspected of nervous system dysfunction is normally sent first to a **neurologist**, who assesses **simple sensory and motor** functions. **Subtler** changes in **perceptual, emotional, motivational or cognitive** function are the province of the **neuropsychologist**.

Neuropsychological testing is very **time-consuming**, so only a small fraction of brain-damaged patients receive it. The book regards that as unfortunate, because testing helps patients in **three** ways:

1. It helps **diagnose** neural disorders, particularly when **brain imaging, EEG and neurological testing have been equivocal**.
2. It provides a basis for **counselling and caring** for the patient (what the patient can and cannot do, what support is needed).
3. It provides an **objective** way of evaluating how well a **treatment** works and how serious its **side effects** are.

### Three approaches to neuropsychological testing

The field has changed radically since the 1950s, passing through three distinct phases. Learn them in order, with their dates, goals and failures, because each phase arose from the failure of the one before.

#### The single-test approach

**Before the 1950s**, the few neuropsychological tests that existed were designed to answer one question: does this patient have brain damage? More specifically, their aim was to separate patients whose psychological problems arose from **structural** brain damage from those whose problems arose from **functional** (not structural) changes in the brain, roughly the old "organic versus functional" distinction.

It failed, mainly because **no single test could be sensitive to the whole variety of symptoms** that brain damage can produce. Damage to different areas produces different deficits, so any one test misses many damaged patients.

#### The standardised-test-battery approach

The next approach grew directly out of that failure and became predominant in **North America by the 1960s**. The **goal stayed the same**, identifying brain-damaged patients, but instead of one test, patients took a standardised **battery** (set) of tests.

The most widely used was the **Halstead-Reitan Neuropsychological Test Battery**: a set of tests on which brain-damaged patients tend to do poorly relative to other patients or healthy controls. Scores on the individual tests are **added into a single aggregate score**, and an aggregate **below a designated cutoff** leads to a diagnosis of brain damage.

The approach was only **marginally successful**. Standardised batteries separate **neurological patients from healthy people** well, but they are much worse at separating **neurological patients from psychiatric patients**, which was often the clinically important question.

#### The customised-test-battery approach

The **customised-test-battery approach** was developed largely by **Luria** and other neuropsychologists of the **Soviet Union** (Luria & Majovski, 1977; Ardila, 1992). It began to be used routinely in a few **American** research institutions in the **1960s**, proved highly successful in research, spread to clinical practice, and now **predominates in both the research laboratory and the neurological ward**.

The crucial change is in the **goal**. Modern testing does not merely ask *whether* a patient has brain damage; it aims to **characterise the nature of each patient's psychological deficits**.

How it works, in two stages:

1. **A common battery for everyone.** All patients start with the same battery of general tests, chosen by the neuropsychologist to show the broad nature of the symptoms.
2. **A customised follow-up.** Depending on those results, the neuropsychologist selects further tests **tailored to that patient** to characterise the general problems in detail. A patient whose common battery suggests a memory problem would next receive tests designed to pin down exactly what kind of memory problem it is.

The tests of the customised approach differ from earlier ones in **three** respects:

1. **They are designed around modern theory.** They measure aspects of psychological function that current theories and data have highlighted. For example, modern evidence indicates that short-term and long-term memory depend on entirely different mechanisms, so patients with memory problems are virtually always tested on **both**.
2. **They look at strategy, not only score.** Interpretation often depends on **how** the patient performs, the **cognitive strategy** used, not just on how well.
3. **They demand more of the examiner.** The neuropsychologist needs more skill and knowledge, both to pick the right tests for a particular patient and to recognise **qualitative** differences in strategy.

| Approach | Era | Goal | Method | Outcome |
|---|---|---|---|---|
| Single-test | Before the 1950s | Detect brain damage; structural versus functional | One test | Failed: no single test sensitive to all symptoms |
| Standardised-test-battery | Predominant in North America by the 1960s | Detect brain damage | Fixed battery (Halstead-Reitan); aggregate score versus cutoff | Marginal: separates patients from healthy people, not from psychiatric patients |
| Customised-test-battery | Luria and Soviet colleagues; in a few US institutions from the 1960s; now dominant | **Characterise** each patient's deficits | Common battery, then patient-specific tests | Highly successful in research and clinic |

> **Trap.** The **Halstead-Reitan** is the emblem of the **standardised** battery approach, not the customised one. The **customised** approach is associated with **Luria**. Note also that the standardised batteries were good at separating neurological patients from **healthy controls**; their weakness was separating them from **psychiatric** patients. (The separate **Luria-Nebraska Neuropsychological Battery** is a later standardised battery built from Luria's items; it is not mentioned in the 11th edition, so do not confuse it with Luria's own customised approach.)

### The common test battery: intelligence (WAIS)

Because the customised approach has two phases, the book describes tests in two groups: those often included in the **initial common battery**, and those used afterwards to study **specific** functions.

Overall **IQ is a weak indicator of brain damage**, yet a general intelligence test is almost always included in the common battery anyway. Many assessments begin with the **Wechsler Adult Intelligence Scale (WAIS)**. The facts the book gives:

- first published in **1955**;
- standardised in **1981** on a sample of **1,880 U.S. citizens** aged **16 to 71**;
- composed of **many subtests**.

Why give it first? Two reasons. Knowing a patient's **IQ helps interpret the results of later tests** (a below-average score on a memory test means something different in someone of high and low general ability). And a skilled neuropsychologist can sometimes infer something about the patient's dysfunction from the **pattern of scores across subtests**. For example, **low scores on the verbal comprehension subtests** tend to be associated with **left-hemisphere damage**.

> **Trap.** The 1981 standardisation on 1,880 people aged 16 to 71 is, historically, the **WAIS-R** (the revised edition); the book attributes it to "the WAIS". The current version, outside the chapter, is the **WAIS-IV** (2008), whose index scores are Verbal Comprehension, Perceptual Reasoning, Working Memory and Processing Speed. For a Pinel-based MCQ, give the book's numbers: **1955, 1981, 1,880, 16 to 71**. Older Pinel editions and older keys also say low *performance* scores suggest right-hemisphere damage; the 11th edition mentions only the verbal comprehension/left-hemisphere link.

### The common test battery: memory

A weakness of the WAIS is that it **often fails to detect memory deficits**, even though some subtests test memory. Two examples:

- The **information subtest** tests memory for **general knowledge** (facts about well-known people and the world).
- The **digit span** subtest, the **most widely used test of short-term memory**, is defined as the **longest string of random digits the patient gets right on half (50 percent) of attempts**. For most people that figure is **7**.

The problem is that these two kinds of memory are among the **least likely to be disrupted by brain damage**. Patients with severe memory disturbances frequently score normally on both. In practice, however, memory problems rarely go unnoticed, because the patient or the family usually report them.

> **Trap.** Digit span is defined by the **50 percent** criterion, and normal span is **7**. A normal digit span **does not** rule out serious amnesia; H.M. (Chapter 11) had a normal digit span. If a question asks why the WAIS misses memory problems, the answer is that its memory subtests (information, digit span) tap forms of memory that brain damage **rarely** disrupts.

### The common test battery: language and the token test

If the patient has taken the WAIS, a language deficit can be inferred from a **low aggregate score on the verbal subtests**. If not, a quick screen is the **token test**.

The materials: **20 tokens** made by crossing **two shapes** (squares and circles), **two sizes** (large and small) and **five colours** (white, black, yellow, green and red). Check the arithmetic: 2 × 2 × 5 = 20, one token for each combination.

The procedure runs from easy to hard:

1. The examiner reads out **simple** instructions involving one token, of the "touch a particular coloured shape" kind.
2. The instructions become more **complex**, specifying size, colour and shape for two tokens in sequence.
3. Finally, the patient **reads the instructions aloud** and then carries them out.

Because the tokens and actions are trivial, failure points to difficulty **understanding** (and, in the last stage, reading) language rather than to motor or perceptual problems.

### The common test battery: language lateralisation

Usually one hemisphere participates more than the other in language. In most people the **left** hemisphere is dominant; in some it is the **right**. A test of **language lateralisation** is often part of the common battery because knowing which hemisphere is dominant helps interpret the other results. It is **virtually always** given before any surgery that might encroach on the cortical language areas, so that the surgeon can plan to avoid them.

There are two widely used tests: the **sodium amytal test (Wada, 1949)** and the **dichotic listening test (Kimura, 1973)**.

#### The sodium amytal (Wada) test

The anaesthetic **sodium amytal** is injected into the **left or right carotid artery** in the neck. This temporarily anaesthetises the **ipsilateral** (same-side) hemisphere, leaving the **contralateral** hemisphere largely unaffected. Several language tests are given quickly while the drug acts; later the procedure is repeated on the other side.

The result is clear-cut. If the injection is on the **language-dominant** side, the patient becomes **completely mute for about 2 minutes**. If it is on the non-dominant side, there are only **a few minor speech problems**.

Because it is **invasive**, the test can be given only for **medical reasons**, usually to identify the dominant hemisphere before brain surgery.

#### The dichotic listening test

The dichotic listening test is **non-invasive**, so it can be given to anyone. In the standard version, the participant wears stereo headphones and hears **three digits in one ear at the same time as three different digits in the other ear**, then reports as many of the **six** digits as possible.

**Kimura (1973)** found that people report **more of the digits heard by the ear contralateral to their language-dominant hemisphere**, as determined independently by the sodium amytal test. So most people, being left-dominant, show a **right-ear advantage** for digits. The reason (developed in Chapter 16) is that the auditory pathways from each ear to the opposite hemisphere are stronger than the same-side pathways, so the right ear has the more direct route to a left-hemisphere language system.

> **Trap.** Wada = **sodium amytal**, **1949**, **carotid artery**, anaesthetises the **ipsilateral** hemisphere, dominant side = **mute about 2 minutes**, **invasive**. Kimura = **dichotic listening**, **1973**, **3 + 3 digits**, advantage for the ear **contralateral** to the dominant hemisphere (usually the **right ear**). Do not reverse ipsilateral and contralateral: the injected side's hemisphere is put to sleep; the ear that wins is on the side opposite the dominant hemisphere.

### Tests of specific function: memory

After the common battery, the neuropsychologist chooses from **thousands** of possible tests to clarify the general problems it exposed. The book gives examples for memory and language.

Once a memory impairment has been found, at least **four fundamental questions** must be answered (Chapter 11):

1. Does it affect **short-term** memory, **long-term** memory, or both?
2. Are the long-term deficits **anterograde** (affecting things learned **after** the damage), **retrograde** (affecting things learned **before** the damage), or both?
3. Do the long-term deficits involve **semantic** memory (knowledge of the world) or **episodic** memory (personal experiences)?
4. Are they deficits of **explicit** memory (memories the patient is aware of and can express verbally), **implicit** memory (shown by improved performance without conscious awareness), or both?

Many amnesic patients have **severe explicit memory deficits with no implicit memory deficit at all** (Squire & Dede, 2015). **Repetition priming tests** have been central to demonstrating this. The procedure:

1. The patient is shown a list of words and asked to **study** them, but not told to remember them.
2. Later, the patient is asked to **complete word fragments**, many of which come from words on the original list (a fragment with some letters missing, such as one built from "purple").
3. Amnesic patients often complete the fragments **as accurately as healthy controls**.
4. Yet they often have **no conscious memory** of the words, or even of having seen a list.

That is the dissociation: good **implicit** memory for an experience with no **explicit** memory of it.

### Tests of specific function: language and reading

If the common battery reveals a **language** problem, a complex series of tests follows. A **speech** problem can be one of **three fundamentally different** kinds:

| Component | Meaning |
|---|---|
| **Phonology** | The rules governing the **sounds** of the language |
| **Syntax** | The **grammar** of the language |
| **Semantics** | The **meaning** of the language |

Because a brain-damaged patient may have one of these problems without the others, **every** patient with a speech problem must be tested on all three.

**Reading aloud** can also break down in different ways, and follow-up tests must tell the patterns apart. The book describes two kinds of **dyslexic** patient (patients with reading problems):

- Some still know the **rules of pronunciation** but cannot pronounce **irregular** words whose pronunciation must simply be remembered, such as *come* and *tongue*.
- Others can pronounce **simple familiar words from memory** but have **lost the ability to apply pronunciation rules**, so they cannot read aloud **nonwords** such as *trapple* or *fleeming*.

These are the two patterns Chapter 16 names **surface dyslexia** (rules intact, irregular words fail) and **deep dyslexia** (rules lost, nonwords fail). This chapter describes them without the labels.

> **Trap.** **Irregular-word failure with rules intact = surface dyslexia; nonword failure with memorised familiar words intact = deep (phonological) dyslexia.** The examples given in the chapter, *come/tongue* versus *trapple/fleeming*, map onto them in that order. Students often reverse them because "deep" sounds more severe.

---

## 5.7 Behavioural Methods of Cognitive Neuroscience

### The Case of the Vegetative Patient

The module opens with a question that sounds philosophical but turned out to be testable: could a patient diagnosed as being in a **vegetative state** actually be **conscious**, but simply unable to produce any observable response? **Owen and colleagues (2014)** set out to test it with fMRI.

The design, described in outline:

1. **Establishing a code.** In healthy controls, imagining **playing tennis** and imagining **walking from room to room through one's own home** were already known to activate two **distinct** sets of brain regions (broadly, motor-planning areas for tennis and spatial-navigation areas for the house).
2. **Testing the patient.** Inside the scanner, a woman diagnosed as vegetative was asked to imagine each activity in turn. Her fMRI activation patterns were strikingly similar to those of the controls. She was following the instructions.
3. **Turning imagery into answers.** The researchers then asked her to imagine **tennis to mean "yes"** and **moving around her home to mean "no"**, and put to her questions whose answers they already knew, such as the name of her father. Her brain activity gave the **correct answer to every question**.

The case shows what functional imaging can do that no behavioural test could: it detected awareness, and even established two-way communication, in a person whose outward behaviour suggested none. It also raises the stakes of everything that follows in this module, because conclusions like these depend entirely on the logic used to turn brain images into statements about cognition.

> **Trap.** The 11th edition cites this work as **Owen and colleagues (2014)** and describes a **female** patient. The original landmark report of tennis versus house imagery in a vegetative patient was **Owen and colleagues (2006, Science)**, and the yes/no communication method was published by **Monti and colleagues (2010)**, with Owen as a co-author; a paper may cite either. The two imagery tasks are **tennis (yes)** and **navigating the home (no)**. Do not confuse the "vegetative state" (eyes open, sleep-wake cycles, no apparent awareness) with coma (eyes closed, unrousable) or with locked-in syndrome (fully conscious but almost totally paralysed, often communicating with eye movements).

**Cognitive neuroscience** is the division of biopsychology that focuses on understanding **cognition**, and fMRI is its main tool. Pinel and Barnes repeat their earlier warning here: because fMRI images are so persuasive, it is especially important to be an informed consumer of them (Raz, 2012), which means understanding the assumptions and methods behind them.

### Two assumptions of cognitive neuroscience

Cognitive neuroscience rests on two key assumptions:

1. **Each complex cognitive process is built from simpler ones**, called **constituent cognitive processes**. Reading a word aloud, for example, involves seeing the letters, recognising the word, retrieving its sound and producing speech.
2. **Each constituent cognitive process is mediated by neural activity in a particular brain region or set of regions** (Sporns & Betzel, 2016).

Put together, these define the field's **main goal**: to identify the parts of the brain that mediate the various constituent cognitive processes.

### Paired-image subtraction technique

Because PET and fMRI are so central to cognitive neuroscience, the **paired-image subtraction technique** has become one of its key behavioural methods (Posner & Raichle, 1994; Kriegeskorte, 2010). It was devised to solve a simple but serious problem.

**The problem.** Suppose you want to find the brain areas that let a person form a **word association** (respond to a printed word by saying a related word). The naive approach is to scan someone doing a word-association task. But most of the activity recorded will have nothing to do with association itself; it will reflect **looking at** the screen, **seeing** and **reading** the words, and **speaking**. The process you care about is buried among the ones you do not.

**The solution.** Scan the person during **several** tasks, designed so that **pairs of tasks differ in only one constituent process**. Then **subtract** the image from one task of a pair from the image from the other. Everything common to both tasks cancels out, and what remains, the **difference image**, estimates the activity specific to the one process that differs.

**The classic example: Petersen and colleagues (1988).** This **PET** study of single-word processing is the standard illustration.

- **Task A:** volunteers spent a minute **reading aloud printed nouns** as they appeared on a screen.
- **Task B:** they saw the **same nouns** but responded to each by saying aloud an **associated verb** (for a noun naming a vehicle, a verb for what you do with it).
- **Subtraction:** image B minus image A. Both tasks involve fixating the screen, seeing nouns, and saying a word aloud, so all of that cancels. What survives is the activity associated with **forming the word association** itself.

Figure 5.7's lexical-decision fMRI (letters versus asterisks; Kiehl et al., 1999) uses the same logic with a simpler control.

> **Trap.** Petersen and colleagues (1988) used **PET**, not fMRI. The comparison was **reading nouns aloud** versus **generating an associated verb** for each noun, and the subtraction isolates **word association**. The logic depends on the assumption that the two tasks differ in **only one** constituent process; if they differ in more (say, the verb task is also harder and demands more attention), the difference image includes those differences too. That assumption, called "pure insertion" in the methods literature, is the technique's weak point.

### Default mode network

Interpreting difference images is complicated by a discovery that at first seems odd: the brain is **substantially active when a person sits quietly and lets the mind wander**. This level of activity has been called the brain's **default mode** (Raichle, 2010). The brain structures that are typically **active in the default mode but less active during cognitive or behavioural tasks** are collectively the **default mode network**, and their pattern of activity is recorded as **resting state-fMRI (R-fMRI)**.

The default mode network includes many structures (Fox et al., 2015), among them **four cortical areas** (Figure 5.22):

1. **Medial parietal cortex**
2. **Lateral parietal cortex**
3. **Medial prefrontal cortex**
4. **Lateral temporal cortex**

Why it complicates subtraction: the "baseline" or "control" condition of an imaging experiment is not neural silence. If the control task allows the mind to wander, default mode areas will be *more* active in the control than in the task, and a subtraction will show them as "deactivated" by the task. A difference image is always relative to whatever the comparison condition was doing.

> **Trap.** The default mode network is **more** active at **rest** (mind-wandering) and **less** active during **tasks**, the reverse of what most people expect. Its four cortical areas in the book are **medial parietal, lateral parietal, medial prefrontal and lateral temporal**. "Dorsolateral prefrontal cortex" is not on the list; it belongs to the task-engaged networks. (Standard sources often name the medial parietal component as the posterior cingulate cortex and precuneus.)

<div class="fig">
<a class="figzoom" href="figs/f_5_22.jpg" target="_blank" rel="noopener"><img src="figs/f_5_22.jpg" loading="lazy" alt="Pinel Fig 5.22: medial and lateral views of the right hemisphere marking medial parietal, lateral parietal, medial prefrontal and lateral temporal cortex"></a>
<p class="cap"><b>The default mode network.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.22</p>
</div>

### Mean difference images

A second difficulty is **noise**. During any test, random mental events produce brain activity that has nothing to do with the task: a sudden pang of hunger, noticing something moving on the screen, wondering how much longer the session will last (Mason et al., 2007). A single difference image is contaminated by such events.

The fix is the same as for evoked potentials in 5.2: **signal averaging**. Averaging the difference images from **repetitions** of the same tests greatly increases the signal-to-noise ratio. It is also **standard practice to average across several volunteers**. The result is a **mean difference image**, which **emphasises** activity that is **common to many volunteers** and **de-emphasises** activity **peculiar to a few**.

But averaging across people creates at least **two serious problems**:

1. **Individual differences.** If two volunteers each had a specific but **different** pattern of cortical activity, the average of the two reveals little about either. People differ substantially in the cortical localisation of their cognitive abilities (Braver, Cole, & Yarkoni, 2010; Kanai & Rees, 2011), so this is a real problem, not a theoretical one. The average may describe a brain that nobody actually has.
2. **Neuroplasticity.** The cortical area that controls an ability may **change within an individual as a result of experience**, so even one person's map may not be stable over time.

This is the point at which the book's **neuroplasticity** theme appears in the chapter: experience reorganises the brain, and that complicates the interpretation of averaged functional images.

### Functional connectivity

Cognitive neuroscientists want to know not only **which** areas are active during a task but how **networks** of areas work together. This is the study of **functional connectivity (FC)**. To measure it, the researcher looks for brain regions whose activity shows **parallel patterns over time**: regions that rise and fall together are taken to be functionally connected.

Two kinds:

- **Extrinsic FC**: changes in functional connectivity when a **stimulus is presented** or during the **performance of a task**.
- **Intrinsic FC**: functional connectivity present **at rest**, during the **R-fMRI** (Kelly & Castellanos, 2014).

The overall project of characterising the FC associated with each behaviour and cognitive process is the study of the **functional connectome** (Matthews & Hampshire, 2016).

| Term | What it is | How it is obtained |
|---|---|---|
| Connectome | The brain's map of anatomical connections | Structural methods, especially DTI (5.1) |
| Functional connectivity | Regions whose activity rises and falls together | Correlated activity over time in functional images |
| Extrinsic FC | FC during a stimulus or task | Task fMRI |
| Intrinsic FC | FC at rest | R-fMRI |
| Functional connectome | The FC associated with every behaviour and cognitive process | Accumulated FC studies |

> **Trap.** **Connectome** (anatomical wiring, DTI) is not the **functional connectome** (correlated activity). Two regions can be functionally connected without a direct anatomical tract, because they may be coordinated through a third region. And **extrinsic = task/stimulus**, **intrinsic = rest**; the words are easy to swap.

---

## 5.8 Biopsychological Paradigms of Animal Behaviour

The book groups the animal paradigms under three headings: **(1) paradigms for assessing species-common behaviours, (2) traditional conditioning paradigms and (3) seminatural animal learning paradigms**. In each case the focus is on the **laboratory rat**, one of the commonest subjects of biopsychological research.

### Species-common behaviours

**Species-common behaviours** are those shown by virtually **all members of a species**, or at least by all members of the same **age and sex**. Commonly studied examples include **grooming, swimming, eating, drinking, copulating, fighting and nest building**. The book describes three paradigms: the open-field test, tests of aggressive and defensive behaviour, and tests of sexual behaviour.

### Open-field test

In the **open-field test**, the animal is placed in a **large, barren chamber** and its **activity** is recorded (Brooks & Dunnett, 2009). It is also common to count the number of **boluses** (pieces of excrement) the animal drops during the test.

Interpretation:

- **Low activity and high bolus counts** are often used as indicators of **fearfulness**.
- Fearful rats are also highly **thigmotaxic**: they **stay close to the walls** of the chamber and rarely venture into the open centre, and they rarely **rear** or **groom**.
- Rats are often fearful the first time they are placed in an unfamiliar open field, but the fearfulness usually **declines with repeated exposure** to the same field.

The logic is ecological: for a rat, open ground is where predators strike, so staying by walls and freezing are sensible defensive strategies, and their intensity indexes fear.

### Tests of aggressive and defensive behaviour

The **colony-intruder paradigm** (Blanchard & Blanchard, 1988) lets researchers observe and measure typical aggressive and defensive behaviour. A **smaller male intruder** is placed into an established colony, and the encounter between it and the colony's **dominant male** (the **alpha male**) is recorded. The dominant male's behaviour is classed as **aggressive** and the intruder's as **defensive**.

What each animal does:

- **The alpha male** approaches **sideways** with its **hair erect**, then tries to push the intruder off balance and bite its **back and flanks**.
- **The intruder** protects its back and flanks by **rearing up on its hind legs** and fending off the attacker with its forepaws, or by **rolling onto its back**.

So the markers are:

| Aggression (attacker) | Defence (intruder) |
|---|---|
| **Piloerection** (hair standing on end) | **Freezing** |
| **Lateral approach** | **Boxing** (rearing and pushing away) |
| **Flank- and back-biting** | **Rolling over** |

Some tests of defensiveness measure reactions to the **experimenter** rather than to another rat. A common one is to rate how much a rat **resists being picked up**, from no resistance (lowest) to biting (highest).

> **Trap.** Piloerection and lateral approach belong to the **aggressor**; boxing belongs to the **defender**. Students see "boxing" and assume attack. Also, rat aggression is aimed at the **back and flanks**, which is why the defender's postures (rearing, rolling over) protect exactly those areas.

### Elevated plus maze

The **elevated plus maze** is a test of **defensiveness** widely used to study the **anxiolytic** (anxiety-reducing) effects of drugs. It is a four-armed, plus-sign-shaped maze, typically mounted **50 centimetres** above the floor. **Two arms have sides (closed arms)** and **two do not (open arms)**.

The measure of defensiveness, or anxiety, is the **proportion of time the rat spends in the protected closed arms rather than on the exposed open arms**. Many established anxiolytic drugs significantly **increase** the proportion of time on the **open arms**, and new drugs that reduce rats' defensiveness on the maze often prove effective against human anxiety. This is one of the places the chapter's **clinical implications** theme reappears.

> **Trap.** Anxiolytics **increase open-arm time**. More closed-arm time means **more** anxiety. An option saying "an effective anxiolytic increases time in the closed arms" has the direction reversed.

### Tests of sexual behaviour

Most research on the physiological bases of rat sexual behaviour has focused on the **copulatory act** itself. The sequence:

1. The male **mounts** the female from behind and clasps her hindquarters.
2. If the female is receptive, she adopts **lordosis**: hindquarters raised, back bent into a U shape, tail deflected to one side.
3. On some mounts, the male inserts his penis into the female's vagina; this is **intromission**. He then **dismounts by jumping backward** and returns a few seconds later to mount and intromit again.
4. After about **10** cycles of mounting, intromitting and dismounting, the male mounts, intromits and **ejaculates** (ejects his sperm).

The measures:

- **Male** (three common measures): the number of **mounts needed to achieve intromission**; the number of **intromissions needed to achieve ejaculation**; and the **interval between ejaculation and the start of mounting again** (the post-ejaculatory interval).
- **Female** (the most common measure): the **lordosis quotient**, the **proportion of mounts that elicit lordosis**.

> **Trap.** **Lordosis** is the **female** receptive posture; **intromission** is penile insertion, not ejaculation. It takes **about 10** intromissions before ejaculation in the rat. The **lordosis quotient** is a **proportion of mounts**, not a count of lordosis episodes per hour.

### Traditional conditioning paradigms

Learning paradigms are central to biopsychological research for **three** reasons:

1. **Learning is a phenomenon of primary interest** to psychologists in its own right.
2. Learning paradigms provide an effective **technology for producing and controlling animal behaviour**. Animals cannot follow verbal instructions, so they often have to be **trained** to behave in a way that serves the experiment.
3. An animal's ability to learn and perform responses allows researchers to **infer** a lot about its **sensory, motor, motivational and cognitive** state (whether a lesioned rat can learn a visual discrimination tells you whether it can see).

The two classic paradigms:

- **Pavlovian conditioning paradigm.** The experimenter pairs an initially neutral **conditional stimulus** (a tone or light) with an **unconditional stimulus** (meat powder) that elicits an **unconditional** (reflexive) **response** (salivation). After repeated pairings, the conditional stimulus alone comes to elicit a **conditional response** (salivation), which is often, but **not always**, similar to the unconditional response.
- **Operant conditioning paradigm.** The animal emits a **voluntary** response, for example **pressing a lever**, and its consequences change how often it does so: **reinforcement raises** the response rate and **punishment lowers** it.

One widely used operant paradigm in biopsychology is the **self-stimulation paradigm**: each lever press sends a pulse of current through an electrode implanted in the animal's **own brain**, so the animal is delivering **electrical brain stimulation** to itself. Structures that support self-stimulation have often been called **pleasure centres**. (The phenomenon was discovered by Olds and Milner in 1954, a detail from Chapter 15 rather than this chapter.)

> **Trap.** Pinel uses **"conditional"** and **"unconditional"** stimulus and response, Pavlov's original sense (conditional on pairing), where most Indian textbooks say "conditioned" and "unconditioned". They mean the same thing; do not mark an option wrong for the wording. Note too that the conditional response is **not always** the same as the unconditional response (in drug tolerance, Chapter 15, it is often the **opposite**).

### Seminatural animal learning paradigms

Besides the traditional paradigms, biopsychologists use learning paradigms designed to **mimic situations an animal might meet in its natural environment**. The rationale is a reasonable assumption: forms of learning that help an animal survive in the wild are likely to be **more highly developed** and **more directly tied to innate neural mechanisms** than arbitrary lever-pressing. This rationale is where the book's **evolutionary perspective** theme appears.

Four such paradigms are described: **taste-aversion conditioning, the radial arm maze, the Morris water maze and conditioned defensive burying**.

### Conditioned taste aversion

When eating a food is followed by illness, animals come to **avoid its taste**; that learned avoidance is a **conditioned taste aversion** (Garcia & Koelling, 1966; Lin, Arthurs, & Reilly, 2014). In the standard experiment, rats eat a food with an **unfamiliar** taste and are then given an **emetic** (a nausea-inducing drug). After that **single** pairing, they avoid the taste.

The survival value is obvious: in the wild, nothing screens potential foods for poison, so a rat that can learn from one bad experience lives longer. Rats and many other animals are also **neophobic** (afraid of new things), so when they meet a new food they eat only a **small** amount; if they then become ill, they never eat it again. Aversions can also develop to **familiar** tastes, but these usually need **more than one** trial.

Humans develop them too. **Cancer patients** have been reported to develop aversions to foods eaten before **nausea-inducing chemotherapy** (Bernstein & Webster, 1980). (Pinel adds a personal anecdote about a lasting aversion to a particular red laboratory punch.)

**Why the discovery mattered.** Conditioned taste aversion challenged **three** widely accepted principles of learning that had come out of traditional operant and Pavlovian research (Revusky & Garcia, 1970):

1. **That conditioning is always gradual.** Robust taste aversions form in a **single trial**.
2. **That temporal contiguity is essential.** Rats acquire taste aversions even when illness comes **several hours** after eating, whereas classical conditioning was supposed to need the stimuli close together in time.
3. **The principle of equipotentiality**, the idea that conditioning proceeds in basically the same way whatever the stimuli and responses. Rats learn **taste-illness** associations readily, but only with great difficulty learn relations between the **colour of food and nausea**, or between **taste and footshock**. They appear to have **evolved** a readiness to connect tastes with illness specifically.

> **Trap.** Three principles challenged, in a fixed set: **gradual acquisition, temporal contiguity, equipotentiality**. The third is the one Garcia and Koelling (1966) demonstrated most directly: taste goes with illness, not with shock; audiovisual cues go with shock, not with illness. Note that the 11th edition cites **Revusky and Garcia (1970)** for the three challenged principles and **Bernstein and Webster (1980)** for chemotherapy aversions in humans.

### Radial arm maze

The **radial arm maze** taps the rat's well-developed **spatial abilities**. A wild rat's survival depends on navigating quickly and accurately and learning which places are likely to have food and water. That is harder for a rodent than for a supermarket shopper whose food sources are constantly restocked. A foraging rat must remember not only **where food is likely to be** but also **which of those places it has recently emptied**, so it does not waste time going back too soon.

**Olton and Samuelson (1976)** built the radial arm maze (Figure 5.23) for exactly this purpose. Picture a hub with spokes: a **central start platform** with arms, **typically eight or more**, leading off it, and a **food cup at the far end of every arm**, which the experimenter baits or leaves empty according to the design.

In one version, rats are placed in the maze each day with the **same arms baited each day**. After a few days they:

- **rarely visit unbaited arms at all** (they remember where food is; a long-term, reference-type memory); and
- **rarely visit a baited arm more than once in the same day** (they remember where they have already been today; a short-term, working-type memory).

They do this even when **control procedures** make it impossible to use **odour trails** from earlier visits or to follow a **fixed systematic sequence** of arms (such as always turning right). Since all the arms are identical, the rats must orient using **external room cues**, and their performance is disrupted if the maze is **rotated** or the **room's appearance is changed**.

<div class="fig">
<a class="figzoom" href="figs/f_5_23.jpg" target="_blank" rel="noopener"><img src="figs/f_5_23.jpg" loading="lazy" alt="Pinel Fig 5.23: a radial arm maze with arms radiating from a central platform and food cups at the arm ends"></a>
<p class="cap"><b>A radial arm maze.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.23</p>
</div>

### Morris water maze

The **Morris water maze** (**Morris, 1981**) is another seminatural test of spatial ability. Rats are placed in a **circular, featureless pool of cool, milky water** and must swim until they find an **escape platform** hidden **just beneath the surface**, invisible because the water is opaque. They are allowed to rest on the platform before the next trial.

The rat is released from a **different point** on each trial, yet within **a few trials** it heads **straight** for the platform, apparently steering by **landmarks around the room**. Because the start position changes, they cannot simply learn a fixed sequence of swimming movements; they must know where the platform is in the room. The maze is widely used to assess the **navigational skills of brain-lesioned or drugged animals** (hippocampal damage is the classic impairing lesion; Chapter 11).

| | Radial arm maze | Morris water maze |
|---|---|---|
| Designer | Olton & Samuelson (1976) | Morris (1981) |
| Apparatus | Usually 8 or more arms around a central start, food cups at ends | Circular pool of cool milky water, hidden platform just below surface |
| Motivation | Food | Escape from water |
| What is learned | Which arms are baited; which have been visited today | Location of the hidden platform |
| Cues used | External room cues (odour and sequences controlled) | External room cues (start point varied) |
| Disrupted by | Rotating the maze or changing the room | Lesions, drugs; changes in room cues |

> **Trap.** Neither maze can be solved by smell or by a learned sequence of turns, because the designs control for both; both depend on **distal room cues**. The water is **milky** so the platform is **invisible**; a visible-platform version is a *control* for visual or motor problems, not the spatial test itself.

### Conditioned defensive burying

The fourth seminatural paradigm, **conditioned defensive burying**, comes from Pinel's own laboratory (**Pinel & Treit, 1978**; **Pinel & Mana, 1989**). A rat receives a **single** aversive stimulus (for example, a **shock**, an **air blast** or a **noxious odour**) from an object mounted on the wall of the test chamber just above a floor covered with **bedding material**. After that **single trial**, almost every rat treats the object as a threat and responds by **flinging bedding at it with its head and forepaws**, eventually burying it (Figure 5.24).

**Antianxiety drugs reduce conditioned defensive burying**, so the paradigm is used to study the **neurochemistry of anxiety** (Steimer, 2011).

> **Trap.** Conditioned defensive burying is learned in **one trial**, the response is **burying** the source of the aversive stimulus with **bedding** (not fleeing or freezing), and **anxiolytics reduce** it. It and the elevated plus maze are the chapter's two anxiety-screening paradigms; conditioned taste aversion is about **illness**, not anxiety.

<div class="fig">
<a class="figzoom" href="figs/f_5_24.jpg" target="_blank" rel="noopener"><img src="figs/f_5_24.jpg" loading="lazy" alt="Pinel Fig 5.24: four photographs of a rat flinging bedding with its forepaws to bury a wall-mounted shock prod"></a>
<p class="cap"><b>A rat burying a test object after a single mild shock.</b> Pinel &amp; Barnes, 11th ed. &middot; Fig 5.24</p>
</div>

### Thinking creatively: converging operations

The chapter ends with a principle that applies to everything in it. **Multiple research methods are almost always needed to answer a question**; an important biopsychological issue is seldom, if ever, settled by a single method.

The reason is that **no method is perfectly selective**, on either side:

- There is **no way of manipulating the brain that changes only one aspect of brain function**. A lesion damages neighbouring structures and fibres of passage; electrical stimulation activates every neuron near the tip; a drug acts at receptors all over the brain; a knockout gene is missing throughout development.
- There is **no measure of behaviour that reflects only one psychological process**. Open-arm time on the plus maze could reflect anxiety, but also activity level or vision; a deficit on the water maze could reflect spatial memory, but also motivation, swimming ability or eyesight.

So a line of research built on **one** method can usually be **interpreted in more than one way**, and cannot give unequivocal support to any single interpretation. Important questions are typically resolved only when **several methods, with different weaknesses, are brought to bear on the same problem** and their results agree. This approach, first introduced in Chapter 1, is called **converging operations**.

A concrete illustration using this chapter's toolkit: to establish that a structure is needed for spatial memory, you might show that **lesions** of it (and, more selectively, **neurotoxic** lesions that spare fibres of passage) impair the **Morris water maze** and **radial arm maze**, that **reversible** inactivation impairs them only while it lasts, that **extracellular unit recording** finds neurons in it that fire at particular locations, that **optogenetic** silencing of its principal neurons impairs navigation, and that **fMRI** shows it active when humans navigate a virtual environment. Each method alone is open to an alternative explanation; together, the alternatives are excluded.

---

## How the chapter fits together

Eight threads run through the whole chapter. If you can follow each one across the modules, the methods stop being a list and become a system.

1. **Structure versus function.** CT, MRI and DTI show what the brain is; PET, fMRI and fUS show what it is doing. PET was the first functional method; fMRI gives structure and function in one image. In animals the same split appears as anatomical tracing (brainbow) versus activity measures (2-DG, unit recording, dialysis).
2. **Where versus when.** Every recording method trades spatial against temporal resolution. fMRI is good at *where* and poor at *when* (2 to 3 seconds against millisecond neural events); EEG and MEG are excellent at *when*, with MEG better than EEG at *where*. In animals, unit recording gets both, at the price of invasiveness.
3. **Correlation versus causation.** Imaging and recording show what activity accompanies a function; only manipulation shows what activity is necessary or sufficient. The manipulations come in matched pairs: turning off (TMS, lesions, reversible lesions, neurotoxins, knockouts, inhibitory opsins) and turning on (tES, tUS, electrical stimulation, excitatory opsins). Lesion and stimulation effects at one site are usually opposite, which is what makes them a useful cross-check.
4. **Signal versus noise.** The same arithmetic recurs: signal averaging pulls the evoked potential out of the background EEG; integration turns raw EMG and multiple-unit spikes into smooth curves; mean difference images average out stray thoughts in imaging studies. Averaging across people has a cost, though: it can erase genuine individual differences.
5. **Direct versus indirect measures.** The BOLD signal measures blood, not neurons; skin conductance measures sweat-gland activity, not emotion as such; PET scans are voxel maps of radioactivity, not pictures. Each method has to be read as what it actually measures.
6. **The march towards selectivity.** Aspiration and radio-frequency lesions destroy everything in an area; neurotoxins pick out cell bodies (kainic, ibotenic acid) or a transmitter system (6-OHDA); knockouts remove one gene everywhere for life; CRISPR/Cas9 edits one gene in one region at a chosen time, reversibly; optogenetics turns one genetically defined neuron type on or off in milliseconds. Each step answers the interpretive problem of the step before it.
7. **Research methods are clinical methods.** Professor P.'s evoked potentials and caloric test, the Wada test before surgery, neuropsychological batteries, the elevated plus maze and defensive burying as anxiolytic screens, tUS lesions for essential tremor, fMRI communication with a vegetative patient.
8. **Converging operations.** Because no manipulation is perfectly selective and no behavioural measure reflects a single process, an answer is trusted only when several methods with different weaknesses agree.

---

## Worked example

*A 29-year-old right-handed man has had focal seizures since adolescence, starting with an odd rising feeling in the stomach. Drugs no longer control them, and the team is considering removing part of his left temporal lobe. You are asked which methods from this chapter will be used in his work-up, what each contributes, and what each cannot tell you.*

**Is there a structural lesion?** Start with **MRI** rather than CT. Both are structural, but MRI gives clearer images and higher spatial resolution, and a small scar in the hippocampus is exactly the kind of soft-tissue detail CT tends to miss. **DTI** could show how the main tracts run near the planned resection.

**Where do the seizures start?** **Scalp EEG** is the first-line tool, because some wave forms are characteristic of epilepsy and recording from many sites at once lets the team compare amplitudes to estimate the source. Its limitation is that it sums everything electrical in the head, so localisation is coarse. **MEG** localises cortical sources much more precisely, at the cost of an expensive, immobile machine and a patient who must keep very still. If uncertainty remains, **invasive EEG** through implanted electrodes may be recorded before surgery, the human use of an animal method from module 5.3.

**Which hemisphere handles his language?** He is right-handed, so the left is likely, but likely is not enough before cutting the left temporal lobe. The **dichotic listening test** is non-invasive and would be expected to show a right-ear advantage if the left is dominant. The decisive test is the **sodium amytal (Wada) test**: injected into the left carotid artery, it anaesthetises the left hemisphere; if he is completely mute for about 2 minutes, the left hemisphere is dominant for language. Because it is invasive, it is justified here only because surgery is planned. **fMRI** with a paired-image subtraction design (for example, generating verbs minus reading nouns aloud, as in Petersen and colleagues' 1988 PET study) can map the language areas themselves. Remember what that map is: a BOLD difference image, slow, indirect, and, if averaged across people, possibly unlike his own brain, since individuals differ in cortical localisation.

**What are his current cognitive strengths and weaknesses?** A **customised-test-battery** approach. The common battery begins with the **WAIS** (published 1955), whose IQ helps interpret everything that follows and whose verbal comprehension subtests may hint at left-hemisphere dysfunction. A **normal digit span** (about 7) would *not* reassure you about memory, because short-term span and general knowledge are rarely damaged; the follow-up battery must ask the four memory questions: short- versus long-term, anterograde versus retrograde, semantic versus episodic, explicit versus implicit. A **repetition priming** test could reveal preserved implicit memory alongside explicit deficits. Language follow-up must test phonology, syntax and semantics separately, and reading tests should distinguish irregular-word errors from nonword errors.

**Why test before and after?** The second benefit of neuropsychological testing the book lists is planning care and counselling; the third is evaluating the treatment objectively. The pre-operative profile is the baseline against which post-operative memory and language are judged, the same logic as Professor P.'s pre-surgery somatosensory baseline.

**What would a researcher add?** Suppose a lab wants to know whether the structure he will lose is needed for spatial memory. No single method will settle it. Bilateral **neurotoxic** lesions (kainic or ibotenic acid, sparing fibres of passage) in rats tested on the **Morris water maze** and **radial arm maze**; **reversible** inactivation with lidocaine to show the deficit lasts only while the area is off; **extracellular unit recording** to find place-related firing; **optogenetic** silencing of a specific cell type; and human **fMRI** during virtual navigation. Each has an alternative explanation on its own (damage to neighbours, motor or visual problems, correlation without causation); together they are **converging operations**.

---

## MCQ traps

1. **Structural vs functional imaging.** CT, MRI and DTI are **structural**; PET, fMRI and fUS are **functional**; **PET was the first functional** method.
2. **Plain X-rays fail** because the brain's overlapping structures differ only slightly in X-ray absorption; **contrast X-rays** inject a substance absorbing more or less than surrounding tissue.
3. **Cerebral angiography** (radio-opaque dye in a cerebral artery) is best for **vascular damage** and finds tumours by **vessel displacement**; pioneered by **Egas Moniz**, also of lobotomy fame.
4. **CT**: computer-assisted X-ray, **early 1970s**, rotating tube and detector, typically **8 or 9 horizontal sections** combined into 3-D.
5. **The 11th-edition PET tracer is FDG**, injected into the **carotid artery**; older editions said 2-DG. FDG cannot be metabolised, so it is trapped in active cells.
6. **A PET scan is a voxel map of radioactivity**, not a picture of the brain; its **most significant current use** is **ligand** mapping of transmitters, receptors and transporters.
7. **MRI** uses radio-frequency waves from **hydrogen atoms** aligning in a magnetic field; it works because water content differs between structures; it is **clearer than CT**.
8. **DTI** images **tracts** from fast **water diffusion** along axons; complete connectomes exist for **C. elegans** and the **mouse**.
9. **BOLD = blood-oxygen-level-dependent**: active areas take up **more oxygenated blood than they need**, and oxygenated and deoxygenated blood differ **magnetically**. BOLD is **not** electrical activity.
10. **fMRI beats PET** three ways (no injection; structure and function in one image; better spatial resolution) but has poor **temporal resolution (2 to 3 s)**.
11. **fUS** measures **blood volume**; it is **cheap, portable and usable with infants**.
12. **Imaging is correlational** (Sack, 2006). **TMS mainly turns cortex off**; **tES and tUS turn it on**; only **tUS reaches subcortical** structures and, at high amplitude, makes **rice-grain lesions** (thalamus, essential tremor) **without incision**. tES evidence is conflicting, even **detrimental**.
13. **EEG** sums every electrical event in the head (brain, skin, muscles, blood, eyes); its value lies in wave forms tied to **states of consciousness** and **epilepsy**.
14. **Alpha waves: 8 to 12 per second, high amplitude, relaxed wakefulness.**
15. **Signal averaging** (e.g. 1,000 trials, mean at each millisecond) cancels random background EEG and raises the **signal-to-noise ratio**, giving the **AEP**.
16. **P300**: **positive**, about **300 msec**, only after a **meaningful** stimulus. **Far-field potentials**: first few msec, from **brain-stem sensory nuclei**, **unaffected by meaning**. Positive waves are drawn **downward**.
17. **MEG beats EEG** on **spatial resolution** and **subcortical localisation**, not on temporal resolution; drawbacks are **cost, size, and the need to keep still**.
18. **EMG and EOG are somatic; SCL/SCR and cardiovascular measures are autonomic.**
19. **EMG amplitude reflects how many fibres contract** (each is all-or-none); the **integrated** EMG totals activity per interval (e.g. 0.1 s).
20. **EOG**: the eye is **front-positive, back-negative**; electrodes **beside** the eye for horizontal and **above and below** for vertical movement.
21. **SCL = tonic, situation-linked level; SCR = transient, event-linked change.** GSR is the older name for SCR. Hands, feet, armpits and forehead are most responsive.
22. **Cardiovascular numbers**: about **70 bpm** resting; normal BP about **130/70 mmHg**; **hypertension = chronic BP above 140/90**; ECG/EKG (K from German); **plethysmography** = blood volume (strain gauge or light absorption).
23. **Stereotaxic atlas**: one **frontal section per page**, distances in mm from **bregma** (where two major sutures meet); the instrument is a **head holder plus electrode holder** moving in three axes.
24. **Lesion targets**: **aspiration** = visible cortex (white matter resists suction); **radio-frequency** = small subcortical (heat); **knife cut** = tract or nerve; **reversible** = cooling or **lidocaine**, same animal in both conditions.
25. **The "amygdala lesion" error runs both ways**: assuming nothing else was damaged over-attributes function; assuming the whole structure was destroyed under-attributes it.
26. **Unilateral lesions are usually much milder than bilateral ones**, so most lesion studies are bilateral.
27. **Electrical stimulation** (bipolar electrode) usually has effects **opposite** to a lesion at the same site; the behaviour depends on **site, current parameters and test environment**.
28. **Only intracellular recording shows the membrane potential**; extracellular shows firing only (up to about **1,000** neurons now); multiple-unit sums many neurons; invasive EEG bears no obvious relation to firing.
29. **Kainic and ibotenic acid** kill **cell bodies** and spare **axons of passage**; **6-OHDA** kills only **noradrenergic and dopaminergic** neurons.
30. **2-DG** needs the animal **killed** and **autoradiography**; **cerebral dialysis** samples extracellular chemicals in **behaving** animals, analysed by **chromatograph**.
31. **Immunocytochemistry = labelled antibody binds protein** (small-molecule transmitters found via their **enzymes**, e.g. dopamine-beta-hydroxylase). **In situ hybridisation = labelled complementary RNA binds mRNA.**
32. **Melanopsin knockout** (Ruby et al., 2002; Hattar et al., 2003): circadian light adjustment **impaired, not eliminated**. **Knockin**: Shen et al. (2008), Scottish-family schizophrenia gene in mice, **reduced cortex and enlarged ventricles**.
33. **CRISPR/Cas9**: **guide-RNA** finds the DNA, **Cas9** inhibits or activates, a **virus** delivers; editing can be **timed, regional and reversible**, and can alter the **epigenome**.
34. **GFP**: jellyfish, green under **blue** light; Shimomura et al. (1962); **Chalfie et al. (1994)** first visualised neurons (C. elegans); **2008 Nobel in Chemistry**. **Brainbow**: Livet et al. (2007), Tsien's (1998) colour variants, for **axon tracing**.
35. **Opsins** come from **bacteria and algae**, were first expressed in mammalian cells in **2003**, and are delivered by **virus** and activated through an **optical fibre** (now wireless).
36. **Testing history**: single test (before 1950s) failed; **Halstead-Reitan** standardised battery (1960s) separates patients from healthy people but **not from psychiatric patients**; **Luria's customised battery** now dominates and **characterises** deficits.
37. **WAIS**: **1955**; standardised **1981** on **1,880** U.S. citizens aged **16 to 71**; low verbal comprehension suggests **left** damage. **Digit span**: **50 percent** criterion, normal **7**, rarely disrupted. **Token test**: **20 tokens** (2 × 2 × 5).
38. **Wada (1949)**: sodium amytal in one carotid artery anaesthetises the **ipsilateral** hemisphere; dominant side gives **mutism for about 2 minutes**. **Kimura (1973)**: dichotic listening, advantage for the ear **contralateral** to the dominant hemisphere.
39. **Petersen et al. (1988) used PET**, subtracting reading nouns aloud from generating verbs to isolate **word association**.
40. **Default mode network**: active at **rest**, less active in tasks; **medial parietal, lateral parietal, medial prefrontal, lateral temporal** cortex; recorded as **R-fMRI**. **Intrinsic FC** = rest; **extrinsic FC** = task.
41. **Mean difference images** can mislead because of **individual differences** in localisation and **experience-driven change**.
42. **Open field**: low activity, many **boluses** and **thigmotaxis** mean fear. **Colony-intruder**: **piloerection, lateral approach, flank and back bites** = aggression; **freezing, boxing, rolling over** = defence.
43. **Elevated plus maze** (about **50 cm** high): anxiolytics **increase open-arm** time. **Defensive burying** (Pinel & Treit, 1978): one trial, **reduced by anxiolytics**.
44. **Rat copulation**: about **10** mount-intromission cycles before ejaculation; **lordosis quotient** = proportion of mounts eliciting lordosis.
45. **Conditioned taste aversion** (Garcia & Koelling, 1966) challenged **gradual learning, temporal contiguity and equipotentiality** (Revusky & Garcia, 1970); chemotherapy aversions: Bernstein & Webster (1980).
46. **Radial arm maze = Olton & Samuelson (1976)**, usually 8 or more arms; **Morris water maze = Morris (1981)**, hidden platform; both rely on **room cues**. Pinel's "conditional/unconditional" = conditioned/unconditioned.

---

## Key terms

| Term | Definition |
|---|---|
| **Contrast X-ray techniques** | X-ray methods that inject a substance absorbing X-rays more or less than surrounding tissue, to heighten contrast |
| **Cerebral angiography** | Contrast X-ray of the cerebral circulation using a radio-opaque dye infused into a cerebral artery |
| **Computed tomography (CT)** | Computer-assisted X-ray procedure building horizontal brain sections from many rotating X-ray readings |
| **Positron emission tomography (PET)** | First functional imaging method; maps accumulated radioactivity from an injected tracer or ligand |
| **Fluorodeoxyglucose (FDG)** | Radioactive glucose analogue taken up but not metabolised by active cells; the PET tracer |
| **Voxel** | Volume pixel; the tiny cube whose radioactivity or signal a functional scan represents |
| **Ligand** | An ion or molecule that binds to another molecule; labelled ligands map receptors and transmitters |
| **Magnetic resonance imaging (MRI)** | Structural imaging from radio-frequency waves emitted by hydrogen atoms aligning in a strong magnetic field |
| **Spatial resolution** | Ability to detect and represent differences in spatial location |
| **Diffusion tensor MRI (DTI)** | MRI method identifying pathways of rapid water diffusion, hence major tracts |
| **Connectome** | The complete map of connections among brain structures |
| **Functional MRI (fMRI)** | MRI-based functional imaging of increased oxygenated blood flow to active areas |
| **BOLD signal** | Blood-oxygen-level-dependent signal recorded by fMRI; reflects blood oxygenation, not electrical activity directly |
| **Temporal resolution** | Ability to specify the timing of neural events |
| **Functional ultrasound imaging (fUS)** | Ultrasound measurement of regional blood-volume change; cheap, portable, usable with infants |
| **Transcranial magnetic stimulation (TMS)** | Magnetic field from a coil beside the skull that temporarily disrupts (or, with other parameters, activates) cortex |
| **Transcranial electrical stimulation (tES)** | Current passed between two scalp electrodes to increase cortical activity |
| **Transcranial ultrasound stimulation (tUS)** | Converging low-amplitude ultrasound beams that activate cortical or subcortical targets; lesions at high amplitude |
| **Psychophysiological recording** | Recording physiological activity from the surface of the human body |
| **Electroencephalography (EEG)** | Recording of the gross electrical activity of the brain through scalp (or implanted) electrodes |
| **Alpha waves** | Regular 8 to 12 per second, high-amplitude EEG waves of relaxed wakefulness |
| **Event-related potentials (ERPs)** | EEG waves accompanying particular psychological events |
| **Sensory evoked potential** | Change in cortical EEG produced by a momentary sensory stimulus |
| **Signal averaging** | Averaging many stimulus-locked recordings to cancel random noise and reveal the signal |
| **Average evoked potential (AEP)** | The averaged evoked response produced by signal averaging |
| **P300 wave** | Positive AEP wave about 300 msec after a stimulus that has meaning for the participant |
| **Far-field potentials** | Earliest evoked-potential waves (first few msec), originating in brain-stem sensory nuclei, unaffected by meaning |
| **Magnetoencephalography (MEG)** | Recording of scalp magnetic-field changes produced by neural activity; better spatial resolution than EEG |
| **Electromyography (EMG)** | Recording of muscle electrical activity, an index of muscle tension and arousal |
| **Electrooculography (EOG)** | Recording of eye movements from the eyeball's steady front-positive, back-negative potential |
| **Skin conductance level (SCL)** | Background (tonic) skin conductance associated with a situation |
| **Skin conductance response (SCR)** | Transient (phasic) change in skin conductance associated with a discrete experience |
| **Electrocardiogram (ECG or EKG)** | Recording of the heart's electrical signals from chest electrodes |
| **Systole / diastole** | Period of heart contraction (peak pressure) / period of relaxation (minimum pressure) |
| **Hypertension** | Chronic blood pressure above 140/90 mmHg |
| **Sphygmomanometer** | Cuff, bulb and gauge for measuring blood pressure |
| **Plethysmography** | Techniques for measuring changes in the blood volume of a body part |
| **Stereotaxic surgery** | Procedure for positioning devices precisely in the depths of the brain |
| **Stereotaxic atlas** | Series of frontal-section maps giving coordinates in mm from a reference point |
| **Bregma** | Skull reference point where two major sutures intersect; zero point of most rat atlases |
| **Stereotaxic instrument** | Head holder plus electrode holder movable in three dimensions |
| **Aspiration** | Removal of accessible cortical tissue by suction through a glass pipette |
| **Radio-frequency lesion** | Subcortical lesion made by heat from high-frequency current at an electrode tip |
| **Knife cut** | Sectioning of a nerve or tract with a stereotaxically placed blade |
| **Reversible lesions** | Temporary inactivation of an area by cooling or local anaesthetic (lidocaine) |
| **Unilateral / bilateral lesions** | Lesions on one side / symmetrically on both sides of the brain |
| **Bipolar electrode** | Two insulated wires wound together and cut at the end, used for brain stimulation |
| **Intracellular unit recording** | Microelectrode inside a neuron recording its graded membrane potential |
| **Extracellular unit recording** | Microelectrode beside a neuron recording its firing but not its membrane potential |
| **Multiple-unit recording** | Larger electrode recording integrated action potentials of many neurons per unit time |
| **Invasive EEG recording** | EEG through implanted electrodes (skull screws for cortex, wires for subcortex) |
| **Psychopharmacology** | Study of drug effects on the nervous system and behaviour |
| **Intraperitoneal / intramuscular / subcutaneous / intravenous** | Injection into the abdominal cavity / a large muscle / fat beneath the skin / a surface vein |
| **Cannula** | Fine hollow tube implanted stereotaxically for delivering drugs into the brain |
| **Neurotoxins** | Neural poisons; selective ones make lesions limited to particular cell types or parts |
| **Kainic acid / ibotenic acid** | Neurotoxins destroying cell bodies at the injection site while sparing axons of passage |
| **6-hydroxydopamine (6-OHDA)** | Neurotoxin taken up only by noradrenergic and dopaminergic neurons |
| **2-deoxyglucose (2-DG) technique** | Radioactive 2-DG accumulates in active neurons; brain sliced and autoradiographed |
| **Autoradiography** | Coating slices with photographic emulsion so that radioactive regions appear as dark spots |
| **Cerebral dialysis** | Semipermeable implanted tube sampling extracellular chemicals in behaving animals (microdialysis) |
| **Chromatograph** | Device measuring the chemical constituents of liquids or gases |
| **Immunocytochemistry** | Locating neuroproteins with labelled antibodies |
| **Antigen / antibody** | Foreign protein / immune protein that binds it |
| **In situ hybridisation** | Locating neurons making a protein with labelled RNA complementary to its mRNA |
| **Gene knockout techniques** | Creating organisms lacking a particular gene |
| **Gene knockin techniques** | Replacing one gene with another or adding a gene the organism lacks |
| **Transgenic mice** | Mice containing genetic material from another species |
| **Gene editing techniques** | Methods for editing genes at a particular time in development |
| **CRISPR/Cas9 method** | Guide-RNA linked to Cas9, delivered by virus, to inhibit or activate targeted genes |
| **Guide-RNA** | RNA strand complementary to the target DNA that directs Cas9 |
| **Green fluorescent protein (GFP)** | Jellyfish protein fluorescing green under blue light; used to make target cells visible |
| **Brainbow** | Labelling each neuron with a distinct colour by mixing GFP colour variants, for tracing axons |
| **Opsins** | Light-sensitive ion channels from bacteria and algae that depolarise or hyperpolarise membranes |
| **Optogenetics** | Using light to switch genetically targeted, opsin-expressing neurons on or off |
| **Behavioural paradigm** | A set of procedures for producing and objectively measuring a behavioural phenomenon |
| **Neuropsychologist vs neurologist** | Assesses subtle perceptual, emotional, motivational, cognitive changes vs simple sensory and motor functions |
| **Single-test approach** | Pre-1950s use of one test to detect brain damage |
| **Standardised-test-battery approach** | Fixed battery with aggregate score and cutoff (Halstead-Reitan) |
| **Halstead-Reitan Neuropsychological Test Battery** | Most widely used standardised battery; poor at separating neurological from psychiatric patients |
| **Customised-test-battery approach** | Luria's approach: common battery then patient-specific tests to characterise deficits |
| **Wechsler Adult Intelligence Scale (WAIS)** | Intelligence test with many subtests; 1955, standardised 1981 on 1,880 people aged 16 to 71 |
| **Digit span** | Longest random-digit sequence repeated correctly 50 percent of the time; normal about 7 |
| **Token test** | Language comprehension screen with 20 tokens (2 shapes, 2 sizes, 5 colours) |
| **Sodium amytal test** | Wada (1949): carotid injection anaesthetising one hemisphere to identify language dominance |
| **Dichotic listening test** | Kimura (1973): simultaneous different digits to each ear; advantage for ear contralateral to dominant hemisphere |
| **Repetition priming tests** | Word-fragment completion revealing implicit memory without explicit memory |
| **Anterograde / retrograde amnesia** | Loss of memory for events after / before the damage |
| **Semantic / episodic memory** | Memory for knowledge of the world / for personal experiences |
| **Explicit / implicit memory** | Conscious, verbally expressible memory / memory shown only by improved performance |
| **Phonology / syntax / semantics** | Sound rules / grammar / meaning of a language |
| **Cognitive neuroscience** | Division of biopsychology focused on understanding cognition, chiefly through functional imaging |
| **Constituent cognitive processes** | Simple processes combining to produce a complex cognitive process |
| **Paired-image subtraction technique** | Subtracting images from tasks differing in one constituent process to isolate it |
| **Difference image** | The result of subtracting one functional image from another |
| **Default mode** | The substantial brain activity present when the mind wanders at rest |
| **Default mode network** | Structures active in the default mode and less active during tasks |
| **Resting state-fMRI (R-fMRI)** | Activity pattern of the default mode network recorded at rest |
| **Mean difference image** | Difference image averaged over repetitions and volunteers |
| **Functional connectivity (FC)** | Network relationship inferred from regions with parallel activity over time |
| **Extrinsic / intrinsic FC** | FC during a task or stimulus / FC at rest |
| **Functional connectome** | The FC associated with each behaviour and cognitive process |
| **Species-common behaviours** | Behaviours shown by virtually all members of a species, or all of one age and sex |
| **Open-field test** | Activity and boluses recorded in a large barren chamber; index of fearfulness |
| **Thigmotaxic** | Tending to stay close to walls; a sign of fearfulness in rats |
| **Colony-intruder paradigm** | Encounter between a colony's alpha male and a smaller male intruder to measure aggression and defence |
| **Elevated plus maze** | Raised plus-shaped maze with two open and two closed arms; anxiety measured by closed-arm time |
| **Anxiolytic** | Anxiety-reducing |
| **Lordosis** | Female rat receptive posture: hindquarters raised, back arched, tail to one side |
| **Intromission** | Insertion of the penis into the vagina |
| **Ejaculate** | Eject sperm |
| **Lordosis quotient** | Proportion of mounts that elicit lordosis |
| **Pavlovian conditioning paradigm** | Pairing a conditional stimulus with an unconditional stimulus until the former elicits a conditional response |
| **Operant conditioning paradigm** | Changing the rate of a voluntary response by reinforcement or punishment |
| **Self-stimulation paradigm** | Animals press a lever to stimulate sites in their own brains ("pleasure centres") |
| **Conditioned taste aversion** | Avoidance of a taste whose consumption was followed by illness; often one-trial |
| **Neophobic** | Afraid of new things |
| **Emetic** | Nausea-inducing drug |
| **Equipotentiality** | Discredited principle that conditioning works the same way for any stimuli and responses |
| **Radial arm maze** | Olton and Samuelson's (1976) maze of 8 or more arms radiating from a centre, for spatial memory |
| **Morris water maze** | Morris's (1981) pool of milky water with a hidden platform, for spatial navigation |
| **Conditioned defensive burying** | One-trial learning to bury an object that delivered an aversive stimulus; reduced by anxiolytics |
| **Converging operations** | Using several methods with different weaknesses to answer one question |

---

## Likely exam points

1. **Professor P.:** tumour on right **cranial nerve VIII**; tests included auditory evoked potentials, caloric vestibular test, somatosensory evoked potentials as a baseline to protect **cranial nerve VII**; shows research methods are clinical methods.
2. **Four imaging families:** X-ray (contrast X-rays, CT), radioactivity (PET), magnetic (MRI, DTI, fMRI), ultrasound (fUS); **three stimulation** methods (TMS, tES, tUS).
3. **Cerebral angiography** and Moniz; why plain X-rays fail.
4. **CT procedure:** early 1970s, rotating tube and detector, 8 or 9 horizontal sections.
5. **PET:** first functional imaging; FDG into the carotid artery; trapped in active cells; voxels; about 30 seconds of activity; main current use = ligand mapping.
6. **MRI principle:** hydrogen atoms, water content; clearer than CT; spatial resolution defined.
7. **DTI and the connectome:** tracts via water diffusion; C. elegans and mouse connectomes; Human Connectome Project.
8. **fMRI and BOLD:** two properties of oxygenated blood; three advantages over PET; poor temporal resolution (2 to 3 s); BOLD is not electrical activity.
9. **fUS:** blood volume; cheap, portable, infants.
10. **Correlation versus causation** (Sack, 2006) and the cingulate example; TMS off, tES and tUS on; tUS subcortical and lesioning (essential tremor).
11. **Six psychophysiological measures** in three pairs (brain, somatic, autonomic).
12. **EEG** contents and value; **alpha 8 to 12 Hz relaxed wakefulness**; multi-site recording for localisation.
13. **Signal averaging** procedure and the **AEP**; signal versus noise.
14. **P300** (positive, about 300 msec, meaningful stimulus) versus **far-field potentials** (first msec, brain stem, meaning-independent); positive drawn downward.
15. **MEG versus EEG:** better spatial resolution and subcortical localisation; cost, size, stillness.
16. **EMG** (fibres all-or-none, amplitude = number of fibres, integration per 0.1 s) and **EOG** (front positive, electrode placement).
17. **SCL versus SCR**; sweat glands; responsive sites.
18. **Cardiovascular:** ECG/EKG, 70 bpm; systolic/diastolic, 130/70, hypertension above 140/90, sphygmomanometer; plethysmography (strain gauge, light absorption).
19. **Stereotaxic surgery:** atlas (frontal maps, mm from bregma), instrument (head holder, electrode holder, three axes); the amygdala example (2.8 mm posterior, 4.5 mm lateral, 8.5 mm ventral).
20. **Four lesion methods** with their targets, and the two-way "amygdala lesion" interpretive error; bilateral versus unilateral.
21. **Electrical stimulation:** bipolar electrode; opposite to lesion effects; behaviours elicited; three determinants.
22. **Four invasive recording methods** and what each can and cannot show.
23. **Routes of administration** (oral, intragastric, IP, IM, SC, IV, cannula) and the blood-brain barrier.
24. **Selective neurotoxins:** kainic and ibotenic acid (cell bodies) versus 6-OHDA (NE and DA neurons).
25. **2-DG autoradiography** (ground squirrel, left eye, right hemisphere) versus **cerebral dialysis** (behaving animals, chromatograph).
26. **Immunocytochemistry** (antibody to protein, enzyme trick, dopamine-beta-hydroxylase) versus **in situ hybridisation** (complementary RNA to mRNA).
27. **Genetic methods:** knockout (melanopsin, partial effect, many genes plus experience), knockin/transgenic (Shen et al., 2008), CRISPR/Cas9 (guide-RNA, Cas9, virus, timed and reversible, epigenome).
28. **GFP and brainbow:** Shimomura (1962), Chalfie (1994), Tsien (1998), Livet (2007), Nobel 2008.
29. **Optogenetics:** opsins from bacteria and algae; mammalian expression 2003; virus, optical fibre, wireless; cell-type specificity.
30. **Three approaches to neuropsychological testing** with dates, goals and outcomes; three ways the customised tests differ; three ways testing helps patients.
31. **Common battery:** WAIS (1955; 1981; 1,880; 16 to 71), information and digit span (7, 50 percent), token test (20 tokens), language lateralisation (Wada 1949, mute about 2 minutes; Kimura 1973 dichotic listening).
32. **Specific tests:** four memory questions; repetition priming; phonology, syntax, semantics; two dyslexic patterns (irregular words versus nonwords).
33. **Cognitive neuroscience:** vegetative patient (Owen and colleagues; tennis = yes, home = no); constituent processes; paired-image subtraction (Petersen et al., 1988, PET); default mode network and its four areas; mean difference images and their two problems; extrinsic versus intrinsic functional connectivity.
34. **Animal paradigms:** open field, colony-intruder, elevated plus maze, copulatory measures and lordosis quotient; Pavlovian, operant and self-stimulation; CTA and the three principles it challenged; radial arm maze, Morris water maze, conditioned defensive burying.
35. **Converging operations:** why no single method suffices.

---
*Rewritten 2026-11-21 from Pinel & Barnes, Biopsychology, Global Edition, 11th ed., Chapter 5 "The Research Methods of Biopsychology" (pp. 121-150), at full explanatory depth. Figures are the real textbook figures. Part of [[INDEX]].*
