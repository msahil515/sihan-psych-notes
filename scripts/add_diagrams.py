#!/usr/bin/env python3
"""Insert the real Pinel & Barnes textbook figures into the biopsychology notes.

These are the actual figures cropped from Pinel & Barnes, Biopsychology (11th ed.),
NOT schematic redraws. Each is one contiguous <div class="fig"> ... </div> block with
NO internal blank lines, so python-markdown passes it through as raw HTML untouched.
Image files live in docs/figs/ (served by Pages, precached by the service worker).

Idempotent: strips any existing <div class="fig"> blocks first, then re-inserts, so
re-running (or running over the old inline-SVG diagrams) yields the same clean result.
"""
import pathlib, re, sys

PINEL = pathlib.Path(__file__).resolve().parent.parent / "notes" / "pinel-biopsychology"
ATTRIB = "Pinel &amp; Barnes, 11th ed."


def block(fig, title, alt):
    """One contiguous raw-HTML figure block (no blank lines) -> survives markdown."""
    num = fig.replace("f_", "").replace(".jpg", "").replace("_", ".")
    return (
        '<div class="fig">\n'
        f'<a class="figzoom" href="figs/{fig}" target="_blank" rel="noopener">'
        f'<img src="figs/{fig}" loading="lazy" alt="{alt}"></a>\n'
        f'<p class="cap"><b>{title}</b> {ATTRIB} &middot; Fig {num}</p>\n'
        '</div>'
    )


# chapter file -> list of (anchor heading, [figure blocks to insert before it])
PLAN = {
    "ch03-chapter-3-anatomy-of-the-nervous-system.md": [
        ("### Major Divisions", [
            ("f_3_2.jpg", "The major divisions of the nervous system.",
             "Pinel Fig 3.2: the major divisions of the nervous system")]),
        ("### External Anatomy", [
            ("f_3_5.jpg", "External features of a neuron.",
             "Pinel Fig 3.5: external features of a neuron")]),
        ("### Internal Anatomy", [
            ("f_3_6.jpg", "Internal features of a neuron.",
             "Pinel Fig 3.6: internal features of a neuron")]),
        ("### Classes of Neurons (by processes)", [
            ("f_3_8.jpg", "Unipolar, bipolar &amp; multipolar neurons and an interneuron.",
             "Pinel Fig 3.8: unipolar, bipolar and multipolar neurons and an interneuron")]),
        ("### Oligodendrocytes vs. Schwann Cells", [
            ("f_3_9.jpg", "Myelination: an oligodendrocyte (CNS) vs a Schwann cell (PNS).",
             "Pinel Fig 3.9: myelination by an oligodendrocyte versus a Schwann cell")]),
        ("### Planes of Section", [
            ("f_3_16.jpg", "Horizontal, frontal (coronal) and sagittal planes.",
             "Pinel Fig 3.16: horizontal, frontal and sagittal planes")]),
        ("## 3.9 Five Major Divisions of the Brain", [
            ("f_3_19.jpg", "The five divisions of the adult human brain.",
             "Pinel Fig 3.19: the five divisions of the adult human brain")]),
        ("#### Cerebral Cortex", [
            ("f_3_25.jpg", "The lobes of the cerebral hemisphere.",
             "Pinel Fig 3.25: the lobes of the cerebral hemisphere")]),
        ("### Limbic System", [
            ("f_3_27.jpg", "The limbic system.",
             "Pinel Fig 3.27: the limbic system")]),
        ("### Basal Ganglia", [
            ("f_3_28.jpg", "The basal ganglia.",
             "Pinel Fig 3.28: the basal ganglia")]),
    ],
    "ch04-chapter-4-neural-conduction-and-synaptic-transmiss.md": [
        ("### Refractory Periods", [
            ("f_4_5.jpg", "Na⁺ and K⁺ channels across the three phases of the action potential.",
             "Pinel Fig 4.5: sodium and potassium channels across the action potential")]),
        ("### Synthesis, Packaging, Transport", [
            ("f_4_7.jpg", "Anatomy of a typical synapse.",
             "Pinel Fig 4.7: anatomy of a typical synapse")]),
        ("### Amino Acid Neurotransmitters", [
            ("f_4_16.jpg", "The classes of neurotransmitters.",
             "Pinel Fig 4.16: the classes of neurotransmitters")]),
    ],
    "ch06-chapter-6-the-visual-system.md": [
        ("### Inside-Out Arrangement", [
            ("f_6_5.jpg", "The cellular structure of the retina.",
             "Pinel Fig 6.5: the cellular structure of the retina")]),
        ("### Retinotopic Organization", [
            ("f_6_13.jpg", "The retina-geniculate-striate pathway.",
             "Pinel Fig 6.13: the retina-geniculate-striate pathway")]),
    ],
    "ch07-chapter-7-mechanisms-of-perception-hearing-touch-s.md": [
        ("### From Ear to Primary Auditory Cortex", [
            ("f_7_4.jpg", "Anatomy of the ear.",
             "Pinel Fig 7.4: anatomy of the ear")]),
        ("### Cortical Areas of Somatosensation", [
            ("f_7_10.jpg", "The dorsal-column medial-lemniscus system.",
             "Pinel Fig 7.10: the dorsal-column medial-lemniscus system"),
            ("f_7_11.jpg", "The anterolateral system.",
             "Pinel Fig 7.11: the anterolateral system")]),
    ],
    "ch08-chapter-8-the-sensorimotor-system.md": [
        ("### General Model (Figure 8.1)", [
            ("f_8_1.jpg", "The sensorimotor system as a hierarchy.",
             "Pinel Fig 8.1: the sensorimotor system as a hierarchy")]),
        ("### Conventional View", [
            ("f_8_6.jpg", "The motor homunculus.",
             "Pinel Fig 8.6: the motor homunculus")]),
    ],
    "ch12-chapter-12-hunger-eating-and-health.md": [
        ("### Why the body stores most of its energy as fat", [
            ("f_12_1.jpg", "The gastrointestinal tract and the process of digestion.",
             "Pinel Fig 12.1: the gastrointestinal tract and the eight steps of digestion")]),
        ("### The three phases of energy metabolism", [
            ("f_12_2.jpg", "Distribution of stored energy in an average person.",
             "Pinel Fig 12.2: fat 85 percent, protein 14.5 percent, glycogen 0.5 percent")]),
        ("## 12.2 Two Theories of Hunger: Set Points versus Positive Incentives", [
            ("f_12_3.jpg", "The cephalic, absorptive and fasting phases, and what insulin and glucagon do in each.",
             "Pinel Fig 12.3: the three phases of energy metabolism")]),
        ("### The anatomy of any set-point system", [
            ("f_12_4.jpg", "The energy set-point view of hunger and eating.",
             "Pinel Fig 12.4: the energy set-point view of hunger and eating")]),
        ("### How much we eat: the appetizer effect, serving size, and social facilitation", [
            ("f_12_5.jpg", "The sham-eating preparation.",
             "Pinel Fig 12.5: the sham-eating preparation")]),
        ("### Why the VMH is not a satiety centre", [
            ("f_12_6.jpg", "The ventromedial and lateral hypothalamus in the rat brain.",
             "Pinel Fig 12.6: locations of the VMH and LH in the rat brain")]),
        ("### Koopmans's transplanted stomach", [
            ("f_12_7.jpg", "Cannon and Washburn's 1912 system for measuring stomach contractions.",
             "Pinel Fig 12.7: the Cannon and Washburn balloon apparatus and hunger pangs")]),
        ("### Hunger and satiety peptides", [
            ("f_12_8.jpg", "Transplantation of an extra stomach and length of intestine in a rat.",
             "Pinel Fig 12.8: Koopmans's transplanted stomach preparation")]),
        ("### The settling-point model and the leaky barrel", [
            ("f_12_9.jpg", "The diminishing effects on body weight of a low-calorie and a high-calorie diet.",
             "Pinel Fig 12.9: diets plateau at a new stable level")]),
        ("### Four facts of weight regulation, explained twice", [
            ("f_12_10.jpg", "The leaky-barrel model: a settling point, not a set point.",
             "Pinel Fig 12.10: the leaky-barrel model of body-weight homeostasis")]),
        ("### Leptin: the discovery", [
            ("f_12_11.jpg", "The five stages of a typical weight-loss program.",
             "Pinel Fig 12.11: the five stages of a typical weight-loss programme")]),
        ("### Leptin, insulin, and the arcuate melanocortin system", [
            ("f_12_12.jpg", "A control mouse and an ob/ob mouse.",
             "Pinel Fig 12.12: a control mouse beside a leptin-deficient ob/ob mouse")]),
        ("## 12.7 Anorexia Nervosa and Bulimia Nervosa", [
            ("f_12_13.jpg", "Gastric bypass and the adjustable gastric band.",
             "Pinel Fig 12.13: two surgical treatments, gastric bypass and adjustable gastric band")]),
    ],
    'ch09-chapter-9-development-of-the-nervous-system.md': [
        ('### How identical DNA produces different cells', [('f_9_1.jpg', 'Totipotent, pluripotent and multipotent stem cells, and asymmetric cell division.', 'Pinel Fig 9.1: a totipotent cell giving rise to pluripotent then multipotent cells and finally lung, pancreas, heart muscle, red blood, skin and neuron cells')]),
        ('### From neural plate to neural tube', [('f_9_2.jpg', 'Cross section of the ectoderm, mesoderm and endoderm in a developing embryo.', 'Pinel Fig 9.2: embryo cross section showing amniotic cavity, ectoderm, neural plate, mesoderm, notochord, endoderm and yolk sac')]),
        ('### Neural proliferation', [('f_9_3.jpg', 'How the neural plate becomes the neural tube in weeks 3 and 4.', 'Pinel Fig 9.3: neural plate at 18 days, neural groove at 21 days, and neural tube with neural crest and central canal at 24 days')]),
        ('### Migration: time, location and direction', [('f_9_4.jpg', 'Radial glial cells are the stem cells of the developing nervous system.', 'Pinel Fig 9.4: radial glial cells dividing asymmetrically over time to produce neurons, astrocytes, oligodendrocytes and ependymal cells')]),
        ('### Two mechanisms of migration', [('f_9_5.jpg', 'Radial and tangential migration.', 'Pinel Fig 9.5: neural tube cross section with radial migration outward from the centre and tangential migration parallel to the walls')]),
        ('### The inside-out pattern of cortical development', [('f_9_6.jpg', 'Somal translocation and radial-glia-mediated migration.', 'Pinel Fig 9.6: a soma moving along its own extended process, versus a neuron climbing a radial glial fibre')]),
        ("### Sperry's eye-rotation experiments", [('f_9_7.jpg', 'Growth cones and their filopodia.', 'Pinel Fig 9.7: fluorescent micrograph of growing axons tipped by growth cones with fingerlike filopodia')]),
        ('### The chemoaffinity hypothesis', [('f_9_8.jpg', "Sperry's classic study of eye rotation and regeneration.", 'Pinel Fig 9.8: normal frog strikes accurately; rotated eye with or without cut and regenerated optic nerve misdirects strikes by 180 degrees')]),
        ('### Synapse formation', [('f_9_9.jpg', 'Optic nerve regeneration after half the retina or half the tectum is destroyed.', 'Pinel Fig 9.9: half a retina projects over the whole optic tectum, and a whole retina compresses onto half a tectum, supporting the topographic gradient hypothesis')]),
        ('### Scan Your Brain: the stages in order', [('f_9_10.jpg', 'Synapse rearrangement increases the selectivity of transmission.', 'Pinel Fig 9.10: diffuse synaptic contacts early in development become focused on fewer cells after rearrangement')]),
        ('### Topographic sensory cortex maps', [('f_9_11.jpg', 'A few days of monocular deprivation reduces LGN axon branching in layer IV.', 'Pinel Fig 9.11: richly branched LGN axon from the nondeprived eye versus sparsely branched axon from the deprived eye in layer IV of primary visual cortex')]),
        ('### Where adult neurogenesis occurs', [('f_9_12.jpg', 'Adult neurogenesis in the dentate gyrus.', 'Pinel Fig 9.12: hippocampal dentate gyrus with neurons stained blue, glia green and new cells red; double-labelled cells are new neurons')]),
        ('### Elves, folktales and the epilogue', [('f_9_13.jpg', 'Cortical volume differences in Williams syndrome.', 'Pinel Fig 9.13: lateral brain with reduced volume at the parietal-occipital boundary and orbitofrontal cortex, and the superior temporal region marked in blue')]),
    ],
    'ch11-chapter-11-learning-memory-and-amnesia.md': [
        ('### Retrograde versus anterograde, short-term versus long-term', [('f_11_1.jpg', "Medial temporal lobectomy: the tissue removed from H.M.'s brain.", "Pinel Fig 11.1: inferior view of the brain with the medial temporal tissue excised in H.M.'s bilateral lobectomy shaded")]),
        ('### Test 4: The incomplete-pictures test', [('f_11_2.jpg', "H.M.'s learning and retention of the mirror-drawing task.", "Pinel Fig 11.2: mirror-drawing apparatus and H.M.'s errors falling across three days of ten trials")]),
        ('### Test 5: Pavlovian eyeblink conditioning', [('f_11_3.jpg', "The incomplete-pictures test and H.M.'s improvement on retest.", "Pinel Fig 11.3: fragmented drawings in sets 1 to 5 and H.M.'s fewer errors on retest one hour later")]),
        ('### Transient global amnesia', [('f_11_4.jpg', "The hippocampal subfields and R.B.'s CA1 damage.", 'Pinel Fig 11.4: coronal section showing dentate gyrus and CA1 to CA4 subfields, with the CA1 pyramidal cell layer marked')]),
        ("### Gradients of retrograde amnesia and Hebb's consolidation theory", [('f_11_5.jpg', 'Retrograde and anterograde amnesia after closed-head TBI.', 'Pinel Fig 11.5: timeline of normal function, retrograde amnesia, blow to head, coma, confusion with anterograde amnesia, recovery')]),
        ('### The current view: consolidation without end', [('f_11_6.jpg', 'A long gradient of ECS-produced retrograde amnesia.', 'Pinel Fig 11.6: recognition of one-season TV shows before and after ECS, with loss only for shows from the previous 3 years')]),
        ('### How the lesioned monkeys performed', [('f_11_7.jpg', 'A delayed nonmatching-to-sample trial.', 'Pinel Fig 11.7: four steps of a monkey trial, sample object, screened delay, choice, selection of the unfamiliar object')]),
        ('### The three major structures of the medial temporal lobe', [('f_11_8.jpg', 'Delayed nonmatching-to-sample deficits after medial temporal lobe lesions in monkeys.', 'Pinel Fig 11.8: percent correct of lesioned monkeys versus controls falling with longer retention delays')]),
        ('### Why the rat version mattered: hippocampal lesions in monkeys and rats', [('f_11_9.jpg', 'The three major medial temporal lobe structures in the monkey.', 'Pinel Fig 11.9: monkey brain showing hippocampus, amygdala and medial temporal cortex below the rhinal fissure')]),
        ('### The rat version: David Mumby and the Mumby box', [('f_11_10.jpg', 'Aspiration lesions of the hippocampus in monkeys and rats.', 'Pinel Fig 11.10: hippocampal aspiration removes medial temporal cortex in monkeys but only a little parietal neocortex in rats')]),
        ('### How well do intact rats perform?', [('f_11_11.jpg', 'The Mumby box and the rat delayed nonmatching-to-sample test.', 'Pinel Fig 11.11: step-by-step rat trial in the Mumby box with sample object, delay and choice of novel object')]),
        ('### Neuroanatomical basis of the object-recognition deficits', [('f_11_12.jpg', 'Intact monkeys and intact rats on delayed nonmatching-to-sample.', 'Pinel Fig 11.12: percent correct across delays for intact monkeys and intact rats, both near 90 percent at short delays')]),
        ('### The R.B. puzzle: why ischaemia misled', [('f_11_13.jpg', 'Medial temporal cortex versus hippocampus-plus-amygdala lesions in rats.', 'Pinel Fig 11.13: presurgery and postsurgery scores showing deficits after medial temporal cortex lesions but not hippocampus-plus-amygdala lesions')]),
        ('### The relationship between grid cells and place cells', [('f_11_14.jpg', 'Areas of human medial temporal cortex.', 'Pinel Fig 11.14: inferior brain view showing perirhinal, entorhinal and parahippocampal cortex')]),
        ('### Engram cells and optogenetics', [('f_11_15.jpg', 'Concept cells and a hypothetical Harry Potter neuron.', 'Pinel Fig 11.15: still of Harry Potter used to illustrate concept cells')]),
        ('### Inferotemporal cortex', [('f_11_16.jpg', 'Brain structures implicated in memory.', 'Pinel Fig 11.16: brain showing basal forebrain, mediodorsal nucleus, prefrontal cortex, amygdala, medial temporal cortex, hippocampus, inferotemporal cortex and cerebellum')]),
        ('### The classic LTP experiment in the dentate gyrus', [('f_11_17.jpg', 'The three hippocampal synapses where LTP is most studied.', 'Pinel Fig 11.17: rat hippocampal slice marking dentate granule cell, CA3 pyramidal and CA1 pyramidal synapses and the perforant path')]),
        ('### Why LTP became the favoured model of memory', [('f_11_18.jpg', 'LTP in the granule cell layer of the rat dentate gyrus.', 'Pinel Fig 11.18: stimulation of the perforant path and larger population spikes 1 day and 1 week after induction')]),
        ('### Other forms of LTP', [('f_11_19.jpg', 'The induction of NMDA-receptor-mediated LTP.', 'Pinel Fig 11.19: without postsynaptic depolarisation few calcium ions enter; with depolarisation many enter and LTP is induced')]),
    ],
    'ch16-chapter-16-lateralization-language-and-the-split-b.md': [
        ('## 16.1 Cerebral Lateralisation of Function: Introduction', [('f_16_1.jpg', 'The cerebral hemispheres and cerebral commissures.', 'Pinel Fig 16.1: frontal and midsagittal sections showing the corpus callosum, hippocampal, anterior and posterior commissures, massa intermedia and optic chiasm')]),
        ('### Hugo-Karl Liepmann: apraxia is also a left-hemisphere matter', [('f_16_2.jpg', "The location of Broca's area.", "Pinel Fig 16.2: Broca's area in the inferior left prefrontal cortex, just anterior to the face area of the primary motor cortex")]),
        ('### Myers and Sperry (1953): the results', [('f_16_3.jpg', 'Restricting visual information to one hemisphere in cats.', 'Pinel Fig 16.3: cat with transected corpus callosum, transected optic chiasm and one eye blindfolded, restricting visual input to the hemisphere ipsilateral to the open eye')]),
        ('### Confirmation in other species: split-brain monkeys', [('f_16_4.jpg', "Myers and Sperry's (1953) split-brain experiment.", 'Pinel Fig 16.4: control cats retain the discrimination when the patch is switched; experimental cats with chiasm and callosum cut drop to 50 percent and relearn with no savings')]),
        ('### Two brains, but not equal: "Right Hemisphere Ray" and "Left Hemisphere Logan"', [('f_16_5.jpg', 'Testing procedure for split-brain patients.', 'Pinel Fig 16.5: patient fixates a screen with SPOON flashed left and APPLE flashed right, hands under a ledge; each visual field and hand projects to the contralateral hemisphere')]),
        ('### A note on two terms you may meet elsewhere', [('f_16_6.jpg', 'The chimeric figures test.', 'Pinel Fig 16.6: a chimeric face made of two half-faces; the left hemisphere sees a completed version of the right half and the right hemisphere a completed version of the left half')]),
        ('### Why anatomical asymmetry has been hard to link to function', [('f_16_7.jpg', 'Three language areas studied for neuroanatomical asymmetry.', "Pinel Fig 16.7: lateral view showing the frontal operculum, Heschl's gyrus and the planum temporale along the lateral fissure")]),
        ('### How the model works: two circuits', [('f_16_8.jpg', 'The seven components of the Wernicke-Geschwind model.', "Pinel Fig 16.8: left hemisphere showing primary motor cortex, Broca's area, arcuate fasciculus, primary auditory cortex, Wernicke's area, angular gyrus and primary visual cortex")]),
        ('## 16.6 The Wernicke-Geschwind Model: The Evidence', [('f_16_9.jpg', 'How the Wernicke-Geschwind model works.', 'Pinel Fig 16.9: pink circuit for responding to a heard question and black circuit for reading aloud through the left-hemisphere language areas')]),
        ('### Evidence from surgical excisions', [('f_16_10.jpg', "Brain damage in one of Broca's original patients.", "Pinel Fig 16.10: diffuse area of damage extending well beyond Broca's area in one of Broca's two original patients")]),
        ('### Hécaen and Angelergues (1964): accidental and disease-related damage', [('f_16_11.jpg', 'No permanent language disruption after excision of the classic language areas.', 'Pinel Fig 16.11: six surgical cases (J.M., H.N., J.C., P.R., D.H., A.D.) with excisions of Wernicke-Geschwind areas and only transient or minor language problems')]),
        ('### Penfield and Roberts (1959) and Ojemann: scattered sites and a mosaic', [('f_16_12.jpg', "Responses of a patient's left hemisphere to electrical stimulation.", 'Pinel Fig 16.12: numbered cards on the exposed left hemisphere of a 37-year-old patient marking sites producing sensations, movements, speech arrest and naming difficulty')]),
        ('### Current status of the Wernicke-Geschwind model', [('f_16_13.jpg', 'Wide distribution of sites where stimulation blocked or disrupted speech.', 'Pinel Fig 16.13: left hemisphere dots for speech-arrest and speech-disruption sites scattered across frontal, temporal and parietal cortex')]),
        ("### Damasio's PET study of naming", [('f_16_14.jpg', "Reading-associated activity in Bavelier and colleagues' (1997) fMRI study.", 'Pinel Fig 16.14: averaged maps showing extensive active and very active regions in the left hemisphere and a small active region in the right during silent reading')]),
    ],
}


def main():
    for fname, anchors in PLAN.items():
        f = PINEL / fname
        text = f.read_text()
        # strip any existing fig blocks (old inline-SVG doodles or a previous run)
        text = re.sub(r'<div class="fig">.*?</div>\n*', '', text, flags=re.S)
        lines = text.splitlines(keepends=True)
        inserts = []
        for anchor, figs in anchors:
            idx = next((i for i, l in enumerate(lines)
                        if l.strip() == anchor or l.startswith(anchor)), None)
            if idx is None:
                print(f"!! anchor not found in {fname}: {anchor!r}")
                sys.exit(1)
            inserts.append((idx, figs))
        # insert from the bottom up so earlier line indices stay valid
        for idx, figs in sorted(inserts, reverse=True):
            blob = "".join(block(*fg) + "\n\n" for fg in figs)
            lines.insert(idx, blob)
        f.write_text("".join(lines))
        n = sum(len(figs) for _, figs in anchors)
        print(f"patched {fname}: +{n} real figures")


if __name__ == "__main__":
    main()
