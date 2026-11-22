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
    'ch04-chapter-4-neural-conduction-and-synaptic-transmiss.md': [
        ('## 4.2 Generation, Conduction, and Integration of Postsynaptic Potentials', [('f_4_1.jpg', 'Three factors that influence the distribution of Na+ and K+ ions across the membrane of a resting neuron.', 'Pinel Fig 4.1: concentration gradients push Na+ in and K+ out, the negative interior pulls both in, and sodium-potassium pumps move 3 Na+ out for every 2 K+ in')]),
        ('### Integration: adding up the PSPs', [('f_4_2.jpg', 'An EPSP, an IPSP, and an EPSP followed by an action potential.', 'Pinel Fig 4.2: membrane potential traces showing a small depolarising EPSP, a small hyperpolarising IPSP, and an EPSP crossing threshold to trigger an AP peaking near +50 mV')]),
        ('### Temporal summation', [('f_4_3.jpg', 'The three possible combinations of spatial summation.', 'Pinel Fig 4.3: simultaneous EPSPs sum to a larger EPSP, simultaneous IPSPs sum to a larger IPSP, and a simultaneous EPSP and IPSP cancel out')]),
        ('### Ripples on a pond: summation is continuous', [('f_4_4.jpg', 'The two possible combinations of temporal summation.', 'Pinel Fig 4.4: two EPSPs, or two IPSPs, elicited in rapid succession at the same synapse sum to a larger PSP')]),
        ('### Why one action potential barely changes the ion concentrations', [('f_4_5.jpg', 'Opening and closing of voltage-gated sodium and potassium channels across the three phases of the action potential.', 'Pinel Fig 4.5: Na+ channels open at threshold (rising phase), close at about 1 ms (repolarisation by K+ efflux), and K+ channels close gradually (hyperpolarisation)')]),
        ('### Conduction in myelinated axons: saltatory conduction', [('f_4_6.jpg', 'The usual direction of signals conducted through a multipolar neuron (orthodromic conduction).', 'Pinel Fig 4.6: five steps from PSPs on dendrites and soma, decremental spread to the axon initial segment, AP at threshold, nondecremental conduction, to exocytosis at the terminal button')]),
        ('### Other kinds of synapse: dendrodendritic, axoaxonic and axomyelenic', [('f_4_7.jpg', 'Anatomy of a typical synapse.', 'Pinel Fig 4.7: an axodendritic synapse onto a dendritic spine, showing button, synaptic vesicles of two sizes, Golgi complex, mitochondrion, microtubules, synaptic cleft and astrocytic processes')]),
        ('### Directed and nondirected synapses', [('f_4_8.jpg', 'Presynaptic facilitation and inhibition.', "Pinel Fig 4.8: neuron A forms an axoaxonic synapse on the terminal button of neuron B, increasing or decreasing B's effect on neuron C")]),
        ('### Synthesis, packaging and transport of neurotransmitter molecules', [('f_4_9.jpg', 'Nondirected neurotransmitter release from varicosities along an axon and its branches.', 'Pinel Fig 4.9: a string-of-beads axon releasing neurotransmitter molecules diffusely from varicosities')]),
        ('### Small-molecule versus neuropeptide release', [('f_4_10.jpg', 'Schematic illustration of exocytosis.', 'Pinel Fig 4.10: electron micrograph and drawing of synaptic vesicles fusing with the presynaptic membrane and emptying neurotransmitter towards the postsynaptic membrane')]),
        ('### Epigenetics and receptor structure', [('f_4_11.jpg', 'Ionotropic and metabotropic receptors.', 'Pinel Fig 4.11: an ionotropic receptor on an ion channel that opens when transmitter binds, and a metabotropic receptor on a signal protein whose G protein subunit breaks away')]),
        ('### Glia, gap junctions and synaptic transmission', [('f_4_12.jpg', 'The two mechanisms for terminating neurotransmitter action in the synapse.', 'Pinel Fig 4.12: reuptake of transmitter by presynaptic transporters versus enzymatic degradation by a deactivating enzyme in the cleft')]),
        ('### How astrocytes and gap junctions are distributed', [('f_4_13.jpg', 'Gap junctions connect the cytoplasm of two adjacent cells.', 'Pinel Fig 4.13: connexin channels bridging the prejunction and postjunction membranes, forming pores that join the cytoplasm of two cells')]),
        ('### Catecholamines and their synthesis', [('f_4_14.jpg', 'String-of-beads noradrenergic nerve fibres.', 'Pinel Fig 4.14: fluorescence image of beaded noradrenergic axons, the bright beads being sites where norepinephrine is stored and released')]),
        ('### Serotonin, an indolamine, and the naming of adrenergic neurons', [('f_4_15.jpg', 'The steps in the synthesis of catecholamines from tyrosine.', 'Pinel Fig 4.15: tyrosine to L-dopa to dopamine to norepinephrine to epinephrine')]),
        ('## 4.6 Pharmacology of Synaptic Transmission and Behaviour', [('f_4_16.jpg', 'The classes of neurotransmitters.', 'Pinel Fig 4.16: small-molecule classes (amino acids, monoamines, acetylcholine, unconventional) and the large-molecule neuropeptides, with the members of each')]),
        ('### Agonistic and antagonistic mechanisms', [('f_4_17.jpg', 'Seven steps in neurotransmitter action.', 'Pinel Fig 4.17: synthesis, storage in vesicles, breakdown of leaked transmitter, exocytosis, autoreceptor feedback, postsynaptic receptor activation, and deactivation')]),
        ('### The three lines of research', [('f_4_18.jpg', 'Some mechanisms of agonistic and antagonistic drug effects.', 'Pinel Fig 4.18: six agonistic and five antagonistic drug actions at synthesis, leakage, release, autoreceptors, postsynaptic receptors and deactivation')]),
        ('### Pleasure and pain: discovery of endogenous opioids', [('f_4_19.jpg', 'Receiving cosmetic Botox injections.', 'Pinel Fig 4.19: a person receiving cosmetic Botox injections to reduce facial wrinkles')]),
    ],
    'ch14-chapter-14-sleep-dreaming-and-circadian-rhythms.md': [
        ('### Three stages of sleep EEG', [('f_14_1.jpg', 'A participant wired for EEG, EOG and EMG in a sleep experiment.', 'Pinel Fig 14.1: a volunteer asleep in a laboratory bed with electrodes on the scalp and face wired to a recording unit')]),
        ('### The sleep cycle across a night: initial versus emergent stage 1', [('f_14_2.jpg', 'The EEG of alert wakefulness, of sleep onset, and of the three stages of sleep.', 'Pinel Fig 14.2: EEG traces for alert wakefulness, alpha waves before sleep, stage 1, stage 2 with K complex and sleep spindle, and stage 3 delta waves')]),
        ('### REM, NREM and slow-wave sleep: getting the terms straight', [('f_14_3.jpg', 'EEG stages across a typical night, with REM periods and loss of core-muscle tone.', 'Pinel Fig 14.3: hypnogram of about 90-minute cycles over 9 hours, stage 3 concentrated early, REM and core-muscle atonia coinciding with emergent stage 1')]),
        ('## 14.3 Why Do We Sleep, and Why Do We Sleep When We Do?', [('f_14_4.jpg', 'Brain areas implicated in dreaming and in the visual imagery of dreams.', 'Pinel Fig 14.4: medial prefrontal cortex and temporo-parieto junction (dreaming) and medial occipital lobe (visual imagery in dreams)')]),
        ('## 14.4 Effects of Sleep Deprivation', [('f_14_5.jpg', 'African lions sleep almost continuously for 2 or 3 days after gorging on a kill.', 'Pinel Fig 14.5: a lion sprawled asleep on its back in the open after feeding')]),
        ('### REM-sleep deprivation', [('f_14_6.jpg', 'The carousel apparatus for sleep-depriving an experimental rat alongside a yoked control.', 'Pinel Fig 14.6: two rats on a shared rotating disk over water; the disk turns whenever the experimental rat shows sleep EEG')]),
        ('### REM sleep and memory', [('f_14_7.jpg', 'The two effects of REM-sleep deprivation.', 'Pinel Fig 14.7: awakenings needed rise across 7 nights of REM deprivation, and REM percentage rebounds above baseline after deprivation')]),
        ('### Internal desynchronisation', [('f_14_8.jpg', 'A free-running sleep-wake cycle of 25.3 hours with no time cues.', 'Pinel Fig 14.8: actogram over 30 days in which sleep onset drifts about 1.3 hours later each day')]),
        ('### The SCN transplant experiment (Ralph and colleagues, 1990)', [('f_14_9.jpg', 'Location of the suprachiasmatic nuclei.', 'Pinel Fig 14.9: the suprachiasmatic nuclei in the medial hypothalamus just above the optic chiasm')]),
        ('### Genetics of circadian rhythms', [('f_14_10.jpg', 'The discovery of the retinohypothalamic tracts.', 'Pinel Fig 14.10: cutting the optic nerve abolishes light entrainment, cutting the optic tract does not; retinohypothalamic tracts leave the chiasm for both SCN')]),
        ('### Reticular formation and sleep', [('f_14_11.jpg', 'Two hypothalamic regions involved in sleep and wakefulness.', 'Pinel Fig 14.11: anterior hypothalamus and basal forebrain (sleep) versus posterior hypothalamus and midbrain (wakefulness)')]),
        ('### Reticular REM-sleep nuclei', [('f_14_12.jpg', 'Four pieces of evidence that the reticular formation is involved in sleep.', 'Pinel Fig 14.12: cerveau isolé and reticular-core lesions give continuous slow-wave EEG; encéphale isolé is normal; reticular stimulation wakes cats')]),
        ('### Why there is no single REM-sleep centre', [('f_14_13.jpg', 'Brain-stem areas of the cat that control the separate indices of REM sleep.', 'Pinel Fig 14.13: caudal reticular sites for PGO spikes, EEG desynchronisation, hippocampal theta, limb twitches, REMs, core-muscle relaxation and cardiorespiratory changes')]),
        ('### Does melatonin improve sleep? Soporific versus chronobiotic', [('f_14_14.jpg', 'The location of the pineal gland, the source of melatonin.', 'Pinel Fig 14.14: the pineal gland on the midline just ventral to the rear of the corpus callosum')]),
        ('### Long-term sleep reduction: a personal case study', [('f_14_15.jpg', 'Mortality associated with different sleep durations in 2,200,425 volunteers followed for about 12 years.', 'Pinel Fig 14.15: mortality relative to 7 hours (100%): 105, 106, 105 percent at 4 to 6 hours, 104 at 8, rising to 115, 125 and 138 percent at 9, 10 and 11 hours')]),
        ('## How the chapter fits together', [('f_14_16.jpg', "Pinel's sleep record during his 4-week sleep-reduction programme.", 'Pinel Fig 14.16: nightly sleep bars over about 28 days clustered between the target bedtime of 23:00 and waking time of 04:00')]),
        ('### Other physiological correlates of REM sleep', [('t_14_1.jpg', 'Summary of the various sleep-stage terms.', 'Pinel Table 14.1: REM sleep = emergent stage 1; NREM = initial stage 1, stage 2, stage 3 (NREM 1 to 3); slow-wave sleep = stage 3')]),
        ('### Four conclusions from the comparative evidence', [('t_14_2.jpg', 'Average hours slept per day by various mammalian species.', 'Pinel Table 14.2: from giant sloth 20 hours, cat 14, human 8, down to roe deer, horse and zebra 2 hours')]),
        ('## 14.8 Sleep Disorders', [('t_14_3.jpg', 'Summary of the drugs that affect sleep.', 'Pinel Table 14.3: hypnotic (benzodiazepines, imidazopyridines, 5-HTP), antihypnotic (cocaine- and amphetamine-derived stimulants, tricyclic antidepressants), chronobiotic (melatonin)')]),
    ],
    'ch15-chapter-15-drug-addiction-and-the-brain-s-reward-c.md': [
        ('### Three things to know about the specificity of tolerance', [('f_15_1.jpg', 'Drug tolerance is a shift in the dose-response curve to the right.', 'Pinel Fig 15.1: initial and post-exposure dose-response curves; after exposure the same dose has less effect and a greater dose is needed for the same effect')]),
        ('### Drug addiction: what is it?', [('f_15_2.jpg', 'The same adaptive neural changes produce tolerance during drug exposure and withdrawal effects after it.', 'Pinel Fig 15.2: adaptive neural changes grow during drug exposure, counteracting the drug (tolerance), then produce opposite withdrawal effects that fade after the drug is removed')]),
        ('### Conditioned drug tolerance: Crowell, Hinson and Siegel (1981)', [('f_15_3.jpg', 'Contingent tolerance to the anticonvulsant effect of alcohol (Pinel, Mana, &amp; Kim, 1989).', 'Pinel Fig 15.3: convulsion duration across baseline, treatment and test trials; rats given alcohol before each stimulation became tolerant, rats given it after did not')]),
        ("### Siegel's overdose hypothesis", [('f_15_4.jpg', 'Situational specificity of tolerance to the hypothermic effect of alcohol (Crowell, Hinson, &amp; Siegel, 1981).', 'Pinel Fig 15.4: after 20 alcohol injections, rats tested in the same environment showed no temperature drop, while rats tested in a different environment dropped about 1.31 degrees')]),
        ('## 15.5 Early Biopsychological Research on Addiction', [('f_15_5.jpg', 'Global prevalence of addiction to six commonly used psychoactive drugs.', 'Pinel Fig 15.5: drug-dependent people worldwide in millions: tobacco 933, alcohol 100, opioids 27, marijuana 22, cocaine 6, amphetamine 5')]),
        ('### The mesotelencephalic dopamine system', [('f_15_6.jpg', 'A rat pressing a lever to obtain rewarding brain stimulation.', 'Pinel Fig 15.6: intracranial self-stimulation apparatus in which a lever press activates a stimulator that delivers current through an implanted electrode')]),
        ('### Four lines of evidence linking the mesocorticolimbic pathway to self-stimulation', [('f_15_7.jpg', 'The mesotelencephalic dopamine system: nigrostriatal and mesocorticolimbic pathways.', 'Pinel Fig 15.7: dopamine projections from the substantia nigra to the dorsal striatum (nigrostriatal) and from the ventral tegmental area to prefrontal and limbic cortex, nucleus accumbens, amygdala, septum and olfactory tubercle (mesocorticolimbic)')]),
        ('### Early evidence that dopamine mediates drug reward', [('f_15_8.jpg', 'The drug self-administration and conditioned place-preference paradigms.', "Pinel Fig 15.8: a rat lever-pressing to self-inject a drug from an infusion pump, and a two-compartment box in which a drug-free rat's preference for the drug-paired compartment is measured")]),
        ('### Three stages in the development of an addiction', [('f_15_9.jpg', 'Historic influences that shaped current thinking about the brain mechanisms of addiction.', 'Pinel Fig 15.9: two lines from 1950s tolerance and dependence research, one through physical-dependence and positive-incentive theories to the mesocorticolimbic reward pathway, the other through conditioned responses in tolerance to conditioned responses in craving and relapse')]),
        ('### Stage 1: Initial drug taking', [('f_15_10.jpg', 'The three stages in the development of an addiction.', 'Pinel Fig 15.10: initial drug taking, then habitual drug taking, then drug craving and repeated relapse')]),
        ('### Enrichment and non-drug reinforcers protect against relapse', [('f_15_11.jpg', 'Incubation of cocaine craving in rats after withdrawal.', 'Pinel Fig 15.11: cue-elicited lever presses rise from under 50 one day after cocaine withdrawal to over 200 at 60 days')]),
    ],
    'ch17-chapter-17-biopsychology-of-emotion-stress-and-hea.md': [
        ('## 17.1 Biopsychology of Emotion: Introduction', [('f_17_1.jpg', "A reconstruction of Phineas Gage's brain injury, centred on the medial prefrontal lobes.", "Pinel Fig 17.1: computer reconstruction of the tamping iron's path through Gage's skull, damaging both medial prefrontal lobes")]),
        ('#### James-Lange and Cannon-Bard theories', [('f_17_2.jpg', "Darwin's woodcuts of aggressive and submissive dogs illustrating the principle of antithesis.", "Pinel Fig 17.2: Darwin's 1872 woodcuts, aggressive dog (ears forward, back up, hair up, tail up) versus submissive dog (ears back, back down, hair down, tail down)")]),
        ('#### Sham rage (Bard, 1929)', [('f_17_3.jpg', 'Four ways of relating perception of a stimulus, bodily reaction and feeling: commonsense, James-Lange, Cannon-Bard and modern views.', 'Pinel Fig 17.3: perception of a bear, physiological reactions and feeling of fear linked by different arrows in the commonsense, James-Lange, Cannon-Bard and modern biopsychological views')]),
        ('#### Klüver-Bucy syndrome (1939)', [('f_17_4.jpg', 'The structures Papez proposed control emotional expression.', 'Pinel Fig 17.4: amygdala, mammillary body, hippocampus, fornix, cingulate cortex, septum, olfactory bulb and hypothalamus ringing the thalamus')]),
        ('#### The facial feedback hypothesis', [('f_17_5.jpg', "Ekman's six primary facial expressions of emotion.", 'Pinel Fig 17.5: faces showing surprise, anger, sadness, disgust, fear and happiness')]),
        ('#### Voluntary control of facial expression', [('f_17_6.jpg', 'The effect of facial expression on emotional experience (Rutledge &amp; Hupka, 1985).', 'Pinel Fig 17.6: participants felt happier and less angry while making happy faces, and angrier and less happy while making angry faces, for both anger- and happiness-inducing slides')]),
        ('#### Facial expressions: current perspectives', [('f_17_7.jpg', 'A fake smile: the orbicularis oculi component of a genuine (Duchenne) smile is missing.', 'Pinel Fig 17.7: a posed smile with zygomaticus major contraction but little orbicularis oculi contraction around the eyes')]),
        ('## 17.2 Fear, Defence, and Aggression', [('f_17_8.jpg', 'An expression of pride, conveyed by body posture as well as the face.', 'Pinel Fig 17.8: a woman showing pride with a small smile, head tilted slightly back and hands on hips')]),
        ('### Contextual fear conditioning and the hippocampus', [('f_17_9.jpg', 'The circuit mediating sympathetic and behavioural responses conditioned to a threatening sound.', 'Pinel Fig 17.9: threatening sound to medial geniculate nucleus of the thalamus, then to the amygdala directly or via auditory cortex, and from the amygdala to the PAG (behavioural response) and hypothalamus (sympathetic response)')]),
        ('### The amygdala and human emotion', [('f_17_10.jpg', 'Motor and premotor cortex activity when volunteers watched, and when they made, facial expressions of emotion.', 'Pinel Fig 17.10: horizontal, sagittal and coronal fMRI images showing activity in primary motor cortex (M1) and premotor cortex (PMC) during observation of emotional expressions (Carr et al., 2003)')]),
        ('### Neural mechanisms of human emotion: current perspectives', [('f_17_11.jpg', 'The asymmetry of facial expressions, more obvious on the left side of the face.', 'Pinel Fig 17.11: the Mona Lisa and Albert Einstein, whose expressions are more pronounced on the left side of the face')]),
        ('#### Is there one stress response?', [('f_17_12.jpg', 'The two-system view of the stress response.', 'Pinel Fig 17.12: stressor acting on the brain, via anterior pituitary and adrenal cortex (glucocorticoids) and via sympathetic nervous system and adrenal medulla (epinephrine and norepinephrine)')]),
        ('#### The adaptive immune system', [('f_17_13.jpg', 'Phagocytosis: a phagocyte about to ingest and destroy bacteria.', 'Pinel Fig 17.13: coloured micrograph of a phagocyte extending toward bacteria (red blobs)')]),
        ('### Emotions and the autonomic nervous system', [('t_17_1.jpg', 'Biopsychological investigation of emotion: six early landmarks.', 'Pinel Table 17.1: Gage 1848, Darwin 1872, James-Lange and Cannon-Bard about 1900, sham rage 1929, Klüver-Bucy syndrome 1939, limbic system theory 1952')]),
        ('#### The target-site concept', [('t_17_2.jpg', 'Categories of aggressive and defensive behaviours in rats.', 'Pinel Table 17.2: predatory and social aggression; intraspecific defence, defensive attacks, freezing and flight, maternal defence, risk assessment and defensive burying')]),
    ],
    'ch18-chapter-18-biopsychology-of-psychiatric-disorders.md': [
        ("#### Snyder's binding studies: the D2 revision", [('f_18_1.jpg', 'Chlorpromazine as a receptor blocker at dopamine synapses.', 'Pinel Fig 18.1: chlorpromazine binds postsynaptic dopamine receptors without activating them; feedback raises dopamine release, which is broken down into metabolites')]),
        ('#### The limits of the D2 theory and the current version', [('f_18_2.jpg', 'Antipsychotic potency plotted against D2 binding: the correlation behind the D2 version of the dopamine theory.', 'Pinel Fig 18.2: positive correlation between D2-binding potency and antipsychotic potency, with chlorpromazine low, haloperidol high and spiroperidol highest')]),
        ('#### Atypical antidepressants', [('f_18_3.jpg', 'How fluoxetine (Prozac) blocks serotonin reuptake.', 'Pinel Fig 18.3: fluoxetine blocks reuptake of serotonin into the presynaptic neuron, increasing activation of serotonin receptors')]),
        ('### Theories of Depression', [('f_18_4.jpg', 'Bilateral anterior cingulate electrodes and an implanted stimulator for chronic deep brain stimulation in depression.', 'Pinel Fig 18.4: bilateral electrodes in the brain connected by leads under the skin to a stimulator implanted in the upper chest'), ('f_18_5.jpg', 'The anterior cingulate site where chronic stimulation of subcortical white matter relieved treatment-resistant depression (Lozano et al., 2008).', 'Pinel Fig 18.5: medial view of the brain showing the anterior cingulate gyrus and the stimulation site in white matter just beneath the genu of the corpus callosum')]),
        ("### Pharmacological Treatment of Tourette's Disorder", [('f_18_6.jpg', "No rebound above baseline after periods of tic suppression in children with Tourette's disorder (Himle &amp; Woods, 2005).", 'Pinel Fig 18.6: percentage of 10-second periods with a tic across five 5-minute periods; baseline about 50 percent, suppression about 20 percent, post-suppression below baseline')]),
        ('### Controversial Aspects of Clinical Trials', [('t_18_1.jpg', 'Phases of drug development, from basic research through three phases of clinical trials to sale (after Zivin, 2000).', 'Pinel Table 18.1: basic research, application to begin trials, phase 1 safety and maximum safe dose, phase 2 doses and schedules, phase 3 demonstration of therapeutic effect, application to market, selling to the public')]),
        ('#### 5. Targets of psychopharmacology', [('f_18_7.jpg', 'The probability that a drug qualifying for human testing reaches each phase and is approved: only 22 percent gain approval.', 'Pinel Fig 18.7: line falling from 100 percent at phase I through phases II and III to about 22 percent at approval')]),
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
