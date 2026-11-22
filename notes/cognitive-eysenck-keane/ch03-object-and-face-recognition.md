---
date: 2026-11-22
book: "Cognitive Psychology (Eysenck & Keane, 7th ed.)"
subject: Cognitive Psychology
chapter: 3
title: "Object and Face Recognition"
tags: [cognitive-psychology, pattern-recognition, gestalt, perceptual-organisation, object-recognition, recognition-by-components, face-recognition, prosopagnosia, fusiform-face-area, visual-imagery, clinical-psychology-entrance]
---

# Chapter 3: Object and Face Recognition

**What this chapter is really about.** You recognise thousands of things a day without noticing that you are doing anything at all: a cup, a friend's face across a room, the letter "g" in three different fonts. Because it feels effortless, it is easy to assume it is simple. The chapter's first job is to persuade you that it is not. No computer vision system yet matches more than a small fraction of what an ordinary sighted adult does, and the reasons are instructive: objects overlap and hide each other, members of one category (all the chairs in the world) look wildly different from one another, and the same object projects a different image every time you or it moves. A round plate seen at an angle is an ellipse on your retina, yet you never doubt that it is round.

The chapter's second job is to set up a single argument that runs from the first page to the last: **how much of recognition is driven by the stimulus (bottom-up), and how much by what you already know and expect (top-down)?** Each topic answers that question a little differently. Feature detectors and Biederman's geons are bottom-up stories. The Gestaltists insisted that grouping is innate and stimulus-driven, and the modern evidence keeps finding learning inside it. Fingerprint experts are shown to be pushed around by context. The orbitofrontal cortex turns out to guess what an object is before the temporal lobe has finished analysing it. Faces raise a related question: is there a dedicated face system, or are faces simply the category we have practised most? Imagery ends the chapter by turning the arrow round completely, because an image is perception run almost entirely from the top down.

**How to read this chapter.** Section 3.1 lays out why recognition is hard and what the chapter covers. Section 3.2 deals with two-dimensional patterns (letters, fingerprints) and the cells that detect features. Section 3.3 is perceptual organisation: the Gestalt laws, figure-ground segregation, and what modern experiments have done to them. Section 3.4 is the core of object recognition: spatial frequency and coarse-to-fine processing, Marr, Biederman's recognition-by-components theory, the viewpoint debate, the inferotemporal cortex and top-down effects. Section 3.5 treats faces separately: holistic processing, prosopagnosia, the fusiform face area, the expertise hypothesis, Bruce and Young's model and super-recognisers. Section 3.6 asks whether visual imagery is a weak form of seeing (Kosslyn) or something else that only feels like seeing (Pylyshyn). Depth perception, size constancy, colour and the two visual streams belong to Chapter 2; this chapter only borrows the ventral stream from there.

---

## 3.1 Introduction

### Why recognising objects is harder than it feels

Eysenck and Keane give three concrete reasons why object recognition is a genuine computational achievement rather than a trivial one.

1. **Segmentation.** In most scenes objects overlap. Before you can recognise anything, the visual system must decide where one object stops and the next begins. A mug partly hidden behind a laptop is two shapes in the image that must be assigned to two separate things.
2. **Category variability.** Many categories (chairs, trees, dogs) contain members that differ enormously in colour, size and shape. It is far from obvious what all chairs have in common visually that lets you put a beanbag and a dining chair in the same category.
3. **Orientation and viewpoint.** You recognise objects across a huge range of orientations. A plate is round, but most of the time its retinal image is an ellipse, and you still know it is a plate.

There is also more to recognition than naming. Once you have recognised an object you can usually say what it would look like from another side, and you know what it is for. Recognition connects a visual input to a body of stored knowledge.

### The chapter's route

The chapter starts with **two-dimensional patterns** (letters, digits, fingerprints), because they are the simplest case. It then asks how the visual system decides which bits of a scene **belong together** to form separate objects, which is an early and essential stage of recognising anything. Next come general **theories of three-dimensional object recognition**, tested against neuroimaging, behavioural experiments on healthy people and studies of brain-damaged patients. **Face recognition** gets its own section because faces seem to be processed differently from other objects. Finally the chapter asks whether **visual imagery** of objects uses the same processes as perceiving them.

> **Trap.** "Pattern recognition" in this chapter means recognising **two-dimensional** patterns (letters, fingerprints). "Object recognition" means recognising **three-dimensional** objects. Questions sometimes treat the terms as interchangeable; the book does not, and the theories differ (feature detectors for patterns; Marr and Biederman for objects).

---

## 3.2 Pattern Recognition

### What pattern recognition has to explain

**Pattern recognition** is the identification or categorisation of two-dimensional patterns. You do it constantly when you read. Much of the research has used **alphanumeric** patterns (letters and digits), and the central puzzle is flexibility: you recognise the letter "A" quickly and accurately whether it is large or small, upright or tilted, printed in a serif typeface or scrawled in someone's handwriting. Any theory has to explain how such different images all map onto one category.

### Classic background: template theories and why they fail

> **Classic background:** the oldest answer to the flexibility puzzle is **template matching**. On this view the mind stores a miniature copy (a template) of every pattern it knows, and an input is recognised by finding the template it overlaps with best. The idea works in highly constrained settings, such as machine-read characters printed in one standard font, but as a general theory of human recognition it collapses immediately: every change of size, slant, typeface or handwriting would need its own template, so the number of templates would be unmanageable, and a novel version of a familiar letter could never be recognised. Normalising the input first (rescaling and rotating it) only moves the problem, because the system would need to know what the pattern was in order to know how to normalise it. **Prototype** accounts loosen the idea by matching inputs to an idealised average of the category rather than to exact copies. The 7th edition does not discuss either account; it moves straight to features, which is where the evidence is.

### Feature theories

The approach the book adopts treats a pattern as a set of **features** or attributes (Jain & Duin, 2004). The letter "A", for example, can be described as two straight lines meeting at the top plus a connecting cross-bar. The big advantage is that features survive the transformations that defeat templates. Two oblique lines and a cross-bar are still present whether the "A" is tiny, huge, tilted or slightly irregular, so a feature description lets very different images count as the same pattern.

> **Classic background:** two pieces of evidence for feature analysis appear in most older textbooks. In **visual search** experiments (Neisser, 1964), people find a target letter such as Z faster among rounded letters (O, Q, G) than among angular letters that share its straight-line features (E, I, V), which is what you would expect if letters are compared feature by feature. And Selfridge's **Pandemonium** model (1959) described recognition as a hierarchy of feature detectors ("demons") whose outputs are pooled by letter detectors, with the most strongly activated letter winning. Both fit the neurophysiology described below.

### Global before local: Navon (1977)

Many feature theories assume a fixed order: first the specific features are processed, then a more global process puts them together. **Navon (1977)** showed that the order is often the reverse.

His stimuli were large letters made out of small letters, for example a big "H" built from small "S"s (Figure 3.1 shows the kind of display). On some trials observers had to say whether the **large** letter was an H or an S; on others, whether the **small** letters were Hs or Ss.

The result was asymmetric. When people judged the **small** letters, they were markedly slowed if the large letter was different (a big H made of little Ss slowed the "S" response). When they judged the **large** letter, the identity of the small letters made no difference at all. The global shape interfered with the local judgement, but the local shape did not interfere with the global one. In the book's metaphor, we usually see the **forest before the trees**. This is **global precedence**, and it fits a broader principle that the chapter returns to under spatial frequency: the visual system tends to process coarse, general information before fine detail.

Global precedence is not absolute.

- **Dalrymple et al. (2009)** reproduced Navon's result when the small letters were very small and tightly packed. When the small letters were made **larger and spaced out**, the pattern reversed: the small letters were processed faster than the large one, because the large letter was now harder to see as a whole.
- Where you **look** matters too. Which part of the display is fixated (attention allocation) also influences whether global processing comes first (Wagemans et al., 2012b).

> **Trap.** In the main text the 7th edition says **global processing often precedes local processing** (Navon, 1977). The end-of-chapter summary, however, states that feature processing "typically precedes" global processing, with exceptions. The two statements conflict. For an exam, go with the evidence the chapter actually presents: Navon found **global precedence** (global-to-local interference, not the reverse), and Dalrymple et al. (2009) showed that stimulus size and spacing can reverse it. If an option says "local features are always processed first", it is wrong either way.

### Feature detectors in the visual cortex: Hubel and Wiesel

If recognising a pattern begins with analysing its features, there should be cells in the brain that respond to those features. **Hubel and Wiesel (1962)** recorded from cells in the occipital cortex, the region at the back of the brain that handles the earliest cortical stages of vision. They found that some cells responded to a spot of light in two opposite ways, depending on which part of the cell's receptive field the spot fell on:

1. an **"on" response**, where firing rate goes **up** when the light comes on;
2. an **"off" response**, where the light makes firing rate go **down**.

In later work (e.g., Hubel & Wiesel, 1979) they distinguished types of neuron in **primary visual cortex**:

| Cell type | What drives it | Key properties |
|---|---|---|
| **Simple cells** | Bars or edges of a particular **orientation** | Separate rectangular "on" and "off" regions; respond best to a dark bar on a light background, a light bar on a dark background, or a straight light-dark edge; each cell is tuned to **one orientation** |
| **Complex cells** | Straight-line stimuli of a particular orientation, especially **moving** contours | **Large** receptive fields; each is driven by several simple cells that share an orientation preference and have closely overlapping receptive fields (Alonso & Martinez, 1998) |
| **End-stopped cells** | Lines of a particular **length** as well as orientation | Response depends on how long the stimulus is, so they can signal ends of lines and corners |

All three types look like **feature detectors**, so their discovery fitted feature theories of pattern recognition well.

> **Trap.** Keep the three cell types apart. **Simple** = orientation-tuned, small receptive field, separate on/off zones. **Complex** = orientation-tuned, **larger** receptive field, prefers **movement**, built from simple cells. **End-stopped** = sensitive to **length** as well as orientation. A common distractor gives complex cells the "on/off rectangular zones" description, which belongs to simple cells.

### Why feature detectors are not the whole story

The book warns against overstating what these cells achieve. Each one gives **ambiguous** information, because quite different stimuli can drive it equally. A cell might fire at the same rate to a horizontal line moving quickly and to a nearly horizontal line moving slowly. A single cell's output therefore cannot tell you which of those you are looking at; the ambiguity can only be resolved by **combining information across many neurons**.

The Hubel and Wiesel account also needs to be extended, because neurons in visual cortex differ in which **spatial frequencies** they respond to (fine versus coarse detail). That differential tuning explains several perceptual phenomena and is taken up in Section 3.4.

### In the real world: fingerprinting

Fingerprint identification is pattern recognition with very high stakes, and the 7th edition uses it to show how expert recognition can be distorted by top-down influences.

**How the process works.** A print recovered from a crime scene (the **latent print**) is compared with stored records by an **automatic fingerprint identification system (AFIS)**. The databases are huge; the FBI alone holds fingerprints from more than **60 million** people. AFIS produces a short list of candidate matches ranked by similarity, and human experts then decide which candidate, if any, actually matches.

AFIS works with features at two levels:

- **General patterns.** There are three basic fingerprint patterns: **loop**, **arch** and **whorl** (a circular pattern).
- **Specific features.** The skin of the fingers carries ridges and valleys called **friction ridges**. The most important specific features are **minutiae points**, places where a ridge stops abruptly or splits into two or more ridges.

Experts receive the minutiae-similarity information from AFIS but also inspect **microfeatures**, such as the width of particular ridges.

**The Madrid case.** After the Madrid train bombings of **11 March 2004**, four fingerprint experts concluded that a print from the scene belonged to **Brandon Mayfield**, an American lawyer, who was arrested. He was innocent. The print actually came from the bomber, **Ouhane Daoud**. Figure 3.2 (from Dror et al., 2006) shows the two prints side by side, and they look strikingly similar.

**Is this a rare exception?** Less rare than people assume.

- **Cole (2005)** reviewed **22** real cases of expert misidentification. In **more than half** of them, the original wrong identification had been **confirmed by one or more further experts**, so checking by a second expert did not reliably catch the error.
- **Dror et al. (2012)** had experts mark every minutia they could find on **ten** prints, then had them do the same prints again some months afterwards. The two lists for the same print agreed completely only **16%** of the time. Experts are not even fully consistent with themselves.

**Why errors happen.** Part of the problem is the prints themselves: latent prints are often smudged, partial and intrinsically complex. But top-down processing also plays a part, through **forensic confirmation bias**. Kassin et al. (2013) define it as the family of effects by which a person's prior beliefs, expectations, motives and situation shape how evidence is collected, perceived and interpreted.

- **Dror et al. (2006)** gave experts two prints and told them, falsely, that these were the prints the FBI had wrongly matched in the Madrid case. The experts did not know that they themselves had judged this very pair to be a clear and definite match several years before. Given the misleading context, **60%** of them now judged the prints to be definite **non-matches**. The prints had not changed; only the expectation had.
- **Langenburg et al. (2009)** manipulated context such as the supposed conclusion of an internationally respected expert. Both experts and non-experts were swayed by it, but **non-experts were swayed more**.

**What makes experts better? A signal-detection analysis.** Signal-detection theory (e.g., Phillips et al., 2001) separates two quite different reasons why experts might say "match" correctly more often than novices:

1. **Better discrimination**: they are genuinely better at telling matching pairs from non-matching pairs.
2. **A lenient response bias**: they simply say "match" more readily to everything.

The two explanations make opposite predictions about **false alarms**, saying "match" to a pair that is similar but does not match. Good discrimination produces a **low** false-alarm rate; a lenient bias produces a **high** one. So the false-alarm rate is the decisive measure.

**Thompson et al. (2014)** tested experts and novices on genuine crime-scene prints. On pairs that really matched, both groups said "match" on about **70%** of trials, so hit rates did not separate them. The false-alarm rates did: on similar but non-matching pairs, novices wrongly said "match" on **57%** of trials, experts on only **1.65%**. Experts therefore have **much better discrimination**, and they also adopt a **more conservative** criterion, meaning they are more reluctant to say "match" at all.

> **Trap.** In signal-detection terms, a high hit rate alone proves nothing, because it can come from a lenient bias. The diagnostic number is the **false-alarm rate**. Thompson et al. (2014): hits about **70% for both groups**; false alarms **57% (novices) vs 1.65% (experts)**. Experts show **better discrimination and a more conservative bias**, not a more lenient one. An option saying "experts are better because they are more willing to declare a match" reverses the finding.

> **Trap.** Forensic confirmation bias is a **top-down** effect on what experts perceive, not only on what they report. Expertise **reduces** susceptibility to context (Langenburg et al., 2009) but does **not remove** it (Dror et al., 2006). Keep the case in mind for the chapter's bottom-up versus top-down argument.

---

## 3.3 Perceptual Organisation

### The segregation problem

If every object in the world sat on its own with clear space around it, deciding which parts of the image belong together would be easy. Real scenes are not like that. Objects crowd together, overlap and partly hide one another, so the image arriving at the eye is a patchwork of fragments. Working out which fragments belong to the same object is called **perceptual segregation**, and it has to happen before recognition can.

### The Gestaltists and the law of Prägnanz

The first systematic research on this problem came from the **Gestaltists**. Its leading figures, **Koffka, Köhler and Wertheimer**, were German psychologists, and all of them left Germany for America in the interwar years. Their master principle was the **law of Prägnanz**: of all the ways the visual field could be organised, we tend to perceive the **simplest** one. Most of their other laws can be treated as special cases of it.

> **Classic background:** "Gestalt" is German for form or whole, and the school's slogan, that the whole is different from the sum of its parts, is the reason it rejected building perception up from isolated sensations. Wertheimer's 1923 paper on grouping is the usual source cited for the laws below. Older textbooks also list **common fate** (elements that move together are grouped together) among the original laws; the 7th edition mentions only its modern extension, generalised common fate (see the evaluation).

### The grouping laws

Figure 3.3 illustrates four laws. Since the figure is lost, here is what each panel shows and what the law says.

| Law | What it says | Typical demonstration |
|---|---|---|
| **Proximity** | Elements that are **close together** in space are grouped | Dots spaced closely in columns and widely between columns are seen as columns |
| **Similarity** | Elements that **look alike** are grouped | In a grid of open and filled dots, the filled dots are seen as rows or columns |
| **Good continuation** | We group the elements that need the **fewest changes or interruptions** to form straight or smoothly curving lines | Two lines crossing in an X are seen as two continuous lines, not as two Vs touching at their points |
| **Closure** | **Missing parts** of a figure are filled in to complete it | A circle with gaps in its outline is still seen as a circle |

It is tempting to treat these as party tricks. **Wagemans et al. (2012a)** argue the opposite: because the grouping principles decide which objects and parts you see at all, they shape almost every perceptual experience you have.

### Figure-ground segregation

The Gestaltists also emphasised **figure-ground segregation**: the visual field is organised into a **figure** (the object of interest) and a **ground** (the less important background). They made three claims about the difference:

1. The figure is seen as having a **definite shape**; the ground is relatively shapeless.
2. The figure is seen as lying **in front of** the ground.
3. The **contour** separating them is seen as **belonging to the figure**, not to the ground.

You can check all three in the **faces-goblet** figure (Figure 3.4), which can be seen as a white goblet or as two dark facing profiles. Whichever you see as figure takes on shape and seems to sit in front: when the goblet is the figure it stands out against a dark background, and when the faces are the figure they stand out against a light one. The shared contour switches owner as your interpretation switches.

> **Classic background:** this reversible figure is usually credited to the Danish psychologist **Edgar Rubin (1915)** and is often called **Rubin's vase**.

**Which region becomes the figure?** Regions that are **convex** (bulging outwards), **small**, **surrounded** by another region and **symmetrical** are more likely to be seen as figure (Wagemans et al., 2012a). **Fowlkes et al. (2007)** checked this with a large set of natural images on which observers made figure-ground judgements. Figure regions did tend to be **smaller and more convex** than ground regions, so the cues the Gestaltists identified in artificial displays also operate in real scenes.

### Findings: do the Gestalt laws hold up?

**Do the laws describe real contours?** A recurring complaint is that the Gestaltists worked mostly with artificial line drawings. **Geisler et al. (2001)** went to photographs of natural scenes (flowers, a river, trees and so on) and analysed object contours in detail. Contours could be recovered very well from two statistical regularities that are not the classic Gestalt laws:

1. **Neighbouring** segments of a contour almost always have **very similar** orientations.
2. Segments that are **further apart** along a contour usually have **somewhat different** orientations.

When observers had to say which of two complex patterns contained a winding contour, their performance was predicted very well by these two principles. The implication is that our contour decisions draw on **learned knowledge of how real object edges behave**, not only on innate rules.

**Elder and Goldberg (2002)**, also analysing the statistics of natural contours, found results broadly in line with the Gestalt laws. **Proximity** was by far the most powerful cue for deciding which contour fragments belonged to the same object; **similarity** and **good continuation** added only small contributions.

**Are the laws innate?** The Gestaltists held that grouping is intrinsic to the brain and played down learning. **Bhatt and Quinn (2011)** reviewed grouping in infancy. Some results look Gestalt-friendly: infants of only **three or four months** already group by **good continuation, proximity and connectedness**. But other principles, such as **closure**, appear only later in infancy, and infants make more use of grouping principles over a period of months. Taken together, the developmental evidence says that **learning plays an important role** in grouping.

**A principle the Gestaltists missed: uniform connectedness.** **Palmer and Rock (1994)** proposed **uniform connectedness**: any connected region with uniform visual properties (the same colour, texture or lightness) tends to be organised as a single perceptual unit. When they put it in conflict with proximity and similarity, **uniform connectedness won**. **Han and Humphreys (2003)** refined the picture: uniform connectedness produced faster grouping than proximity **only in displays containing several objects**, so its special advantage shows up when a scene holds many things at once.

> **Trap.** **Uniform connectedness is not a Gestalt law.** It was proposed by **Palmer and Rock (1994)**, decades after the Gestaltists, and it dominated proximity and similarity when they conflicted. Questions often list it among "the Gestalt laws" as a distractor, or credit it to Wertheimer.

**Does figure-ground segregation need attention?** The Gestaltists thought figure-ground segregation is fast and pre-attentive. **Vecera et al. (2004)** showed two adjacent regions and drew attention to one of them with a small cue rectangle. Whichever region was **attended** tended to be seen as the **figure**, so attention can steer figure-ground assignment. On the other hand, **Kimchi and Peterson (2008)** found that with relatively **simple** stimuli, figure-ground processing could happen **without attention**. Both can be true: attention matters when the display is ambiguous or complex.

**Does figure-ground segregation depend on experience?** The Gestaltists said no. **Barense et al. (2012)** tested patients with **amnesia** and healthy controls on displays in which one region contained parts of a familiar object (a guitar, a standing woman, a table lamp) and, in other displays, the same parts rearranged so they no longer made a recognisable object (Figure 3.5). Participants simply said which region was the figure.

- **Controls** chose the region containing the **familiar** object as figure more often than the region containing the rearranged parts.
- **Amnesic patients**, who had trouble identifying the objects, showed **no difference** between intact and rearranged versions.

So figure-ground assignment is not settled only by low-level cues such as convexity, symmetry and surroundedness. It also uses **object familiarity**, a product of past experience, and it is therefore **not entirely innate**. The amnesic group is the critical control: their low-level vision is intact, so the loss of the familiarity effect can be pinned on the loss of stored object knowledge.

**Border ownership in the brain.** The Gestaltists stressed that a border "belongs" to the figure. Recent neurophysiology has found **border-ownership neurons** in early visual cortex whose responses are tied directly to figure-ground segregation (Layton et al., 2012). They signal which side of an edge the figure is on, which is surprisingly high-level information for cells so early in the visual system.

### Evaluation of the Gestalt approach

**Strengths.**

1. The Gestaltists picked the **right problem**. Understanding how the visual field is organised into objects is fundamental to everything else in perception.
2. Almost all their **grouping laws**, and the concept of **figure-ground segregation**, have survived. Most apply to complex three-dimensional scenes as well as to drawings.
3. The idea that perceivers settle on the **simplest** organisation (the law of Prägnanz) has proved fruitful. Recent theory suggests that a drive towards simplicity may be central to accurate perception (Wagemans et al., 2012b).

**Limitations.**

1. **Learning was neglected.** The Gestaltists played down past experience and almost ignored how much perceptual organisation depends on knowing the regularities of the environment. Wagemans et al. (2012b) observe that the Gestaltists concentrated on processes inside the perceiver and took little interest in the environment itself.
2. **Description rather than explanation.** They catalogued phenomena well but did not explain them. Prägnanz could have been a powerful explanation, but they never developed it. Modern theorists have offered explanations, for example the **Bayesian approach** (Kersten et al., 2004), in which perception is a rational estimate of the scene that combines **how well an interpretation fits the image** with the perceiver's **prior knowledge and context**. On this approach we are sensitive to the **statistical regularities** of the world: we learn how often elements that are close together, or similar, actually belong to one object, and we use knowledge of objects to settle figure and ground.
3. **Two-dimensional evidence.** Their demonstrations were almost all flat drawings. Most of the principles carry over to real scenes, but real scenes are cluttered and full of occlusion, which makes perceiving them far harder than perceiving a tidy drawing.
4. **Incomplete list.** They did not find all the principles. Uniform connectedness is one omission; **generalised common fate** is another: elements that get brighter or darker together tend to be grouped (Wagemans et al., 2012a).
5. **Too inflexible.** They did not see that grouping and figure-ground segregation arise from **interactions between basic (possibly innate) processes and past experience**, or that they can happen **early or late** in processing depending on the stimulus and the task.

> **Trap.** "Which is NOT a limitation of the Gestalt approach?" Options that are genuine limitations: neglect of learning and experience; description without explanation; reliance on two-dimensional drawings; an incomplete set of principles; inflexibility about when grouping happens. Options that are **not** limitations (they are strengths): that the grouping laws have stood the test of time, and that the simplicity principle (Prägnanz) has proved fruitful. The book does **not** say the laws were wrong; it says they were under-explained and too nativist.

> **Trap.** Direction of the nativism argument: the Gestaltists said grouping and figure-ground segregation are **innate**; the modern evidence against them is **Bhatt and Quinn (2011)** (closure and other principles appear later in infancy and use increases with age), **Barense et al. (2012)** (familiarity affects figure assignment, absent in amnesia), **Geisler et al. (2001)** (learned contour statistics) and **Vecera et al. (2004)** (attention affects figure assignment). Infants grouping by proximity and good continuation at three to four months is the one result in this list that **supports** the Gestalt view.

---

## 3.4 Approaches to Object Recognition

**Object recognition**, identifying the objects in the visual field, is what lets you act sensibly in the world: you cannot pick up a cup you have not recognised as a cup. The section begins with a basic property of the visual system (spatial frequency tuning), then works through the major theories, the viewpoint debate, the neurophysiology of the inferotemporal cortex, and finally top-down influences.

### Spatial frequency

#### Coarse-to-fine processing

**Hegdé (2008)** stressed that visual perception **unfolds over time**, even though it feels instantaneous. In object recognition the unfolding typically runs **coarse-to-fine**: a rough, general analysis of the scene comes first and fine detail is filled in afterwards. The advantage of such a system is that it can deliver a quick gist of a scene and a detailed analysis, as the situation demands.

The mechanism lies in how cells in **primary visual cortex** are tuned. **Spatial frequency** refers to how rapidly light and dark alternate across an image. Many V1 cells respond to **high spatial frequencies**, which carry **fine detail** (sharp edges, texture, small features). Many others respond to **low spatial frequencies**, which carry **coarse** information (the overall layout and large blobs). Figure 3.6 shows a building filtered to keep only the high or only the low frequencies: the high-frequency version looks like a line sketch, the low-frequency version like a blurred photograph.

The timing difference comes from the two subcortical pathways described in Chapter 2. **Low spatial frequencies** reach higher brain areas quickly via the fast **magnocellular** pathway; **high spatial frequencies** travel more slowly via the **parvocellular** pathway. That speed difference is why coarse processing usually comes before fine processing.

| | Low spatial frequency | High spatial frequency |
|---|---|---|
| Carries | Coarse, global information | Fine detail |
| Pathway | **Magnocellular** (fast) | **Parvocellular** (slower) |
| Linked to | Global processing (Navon's large letter) | Local processing (Navon's small letters) |
| Dominates in | Peripheral vision | Central (foveal) vision |

> **Trap.** Direction errors are common here. **Low** spatial frequency = **coarse** = **magnocellular** = **fast**. **High** spatial frequency = **fine** = **parvocellular** = **slower**. Foveal vision is dominated by **higher** frequencies, the periphery by **lower** ones. If an option pairs high frequency with the fast magnocellular route, it is wrong.

#### Findings

**Musel et al. (2012)** tested the coarse-to-fine claim directly. Young adults saw very brief (**150 ms**) indoor and outdoor scenes that unfolded either from coarse to fine (low to high spatial frequency) or from fine to coarse, and had to decide quickly whether each scene was indoors or outdoors. Responses were **faster for the coarse-to-fine sequence**, which suggests that natural scene processing normally runs in that direction.

But the sequence is **not fixed**. **Flevaris et al. (2014)** used the Navon task with instructions to attend either to the global or to the local level. Global processing should benefit more from low spatial frequencies and local processing from high ones, and that is what the brain did: neurons responsive to **low** frequencies were more active during the **global** task, and neurons responsive to **high** frequencies were more active during the **local** task. The visual system adjusts which frequency channels it emphasises to suit the task.

#### In the gallery: why the Mona Lisa's smile disappears

**Livingstone (2000)** used spatial frequency to explain the famously elusive smile in Leonardo da Vinci's *Mona Lisa*. She produced very-low, low and high spatial frequency versions of the painting (Figure 3.7). The smile is much clearer in the two **low-frequency** versions than in the high-frequency one. Because central vision is dominated by high frequencies and peripheral vision by low ones, the smile is most visible when you look **away** from the mouth (at the eyes, say) and fades when you fixate the mouth itself. Livingstone summed it up by saying that the smile vanishes the moment you look straight at her mouth.

#### Conclusions on spatial frequency

The different tuning of cortical neurons to high and low spatial frequencies is central to understanding perception. It explains coarse-to-fine processing, but processing is flexible and task-dependent, so the coarse-to-fine order is **typical, not invariant**. Spatial frequency also matters for many other perceptual phenomena beyond those discussed here.

### Theories of object recognition: the ventral stream and beyond

Before the named theories, the book places object recognition in **Milner and Goodale's (1995, 2008) two-systems model** (covered in Chapter 2). They argued that object recognition and perception depend mainly on the **ventral stream**. That stream is organised as a **hierarchy**: information passes from the retina through the **lateral geniculate nucleus, V1, V2 and V4**, ending in the **inferotemporal cortex**. Moving along it, the stimuli that drive cells best become **progressively more complex**, and cells' **receptive fields grow progressively larger**.

The ventral stream is not the only player, though. The **dorsal stream** also contributes. According to **Thoma and Henson (2011)**, the ventral stream handles **analytic**, detailed processing that **requires attention**, while the dorsal stream handles **holistic** or global processing that does **not** depend on attention. **Farivar (2009)** reviewed research showing that many **three-dimensional shape cues** are processed **only within the dorsal stream**.

> **Trap.** The 7th edition uses Milner and Goodale's labels: the ventral stream is for **perception** ("what"), the dorsal stream for **action** ("how"). Older keys may still call the dorsal stream the "where" stream (the earlier Ungerleider and Mishkin wording). Do not conclude from that model that the dorsal stream plays no part in recognition: Thoma and Henson (2011) give it holistic, attention-free processing, and Farivar (2009) says many 3-D shape cues are handled there exclusively.

### Marr's computational approach

The most influential theorist of object recognition has probably been **David Marr (1982)**. His **computational** model argued that recognition is a sequence of processing stages and is far more complex than had been appreciated. (Mather, 2015, assesses Marr's long-term influence.)

Marr proposed that the observer builds a series of **representations** (descriptions), each more detailed than the last:

| Stage | What it describes | Frame of reference |
|---|---|---|
| **Primal sketch** | A **two-dimensional** description of the main changes in light intensity: **edges, contours and blobs** | Viewer-centred |
| **2½-D sketch** | The **depth and orientation of the visible surfaces**, computed from shading, texture, motion, binocular disparity and so on | **Viewer-centred** (viewpoint-dependent), like the primal sketch |
| **3-D model representation** | The **three-dimensional shapes** of objects and their relative positions, **independent of the observer's viewpoint** | **Object-centred** (viewpoint-invariant) |

> **Trap.** The **2½-D sketch is still viewer-centred**, even though it contains depth. Only the **3-D model** is viewpoint-invariant. A favourite wrong option says that "the 2½-D sketch provides an object-centred description".

**Why Marr mattered.**

1. He saw that object recognition is **much more complex** than earlier researchers had thought.
2. He built a **comprehensive computational model** of the processes involved, which inspired many later theorists to build their own computational models.
3. His distinction between **viewpoint-dependent** and **viewpoint-invariant** representations became the focus of a large body of research (below).

**Limitations.**

1. **Too bottom-up.** Marr did concede that top-down processing is sometimes used and needed, but in practice his model largely ignored the role of expectation and knowledge.
2. **Computationally implausible.** Many researchers now think that the computations needed to produce view-independent 3-D models are **too complex** (Mather, 2015). Supporting that view, **nobody has yet managed to generate 3-D models in the way Marr specified**.

### Biederman's recognition-by-components theory

#### Geons: an alphabet of shapes

**Irving Biederman (1987)** developed and extended Marr's ideas in his **recognition-by-components (RBC) theory**. The central assumption is that objects are made of basic shapes called **geons** ("geometric ions"): blocks, cylinders, spheres, arcs, wedges and so on. Biederman estimated that there are about **36** geons.

That number seems far too small to describe every object we can recognise. The book's answer is an analogy with speech. English has only about **44 phonemes**, yet those few sounds combine into an enormous vocabulary. Geons work the same way, because what matters is **how they are combined and related**. A **cup** is an arc attached to the **side** of a cylinder; a **pail** uses the same two geons with the arc attached to the **top**. The parts are identical; the relation between them makes the difference.

#### The stages of the theory (Figure 3.8)

Figure 3.8 is lost, but the text gives its sequence. Recognition runs roughly as follows:

1. **Edge extraction.** An early stage detects differences in surface characteristics (luminance, texture or colour) and produces something like a **line drawing** of the object.
2. **Parsing at concavities.** The object is segmented into its parts. Biederman argued that **concave regions** of the contour (where the outline bends inwards, as where a handle meets a mug) are especially useful for finding part boundaries. **Leek et al. (2012)** recorded eye movements during object recognition and found, as predicted, that fixations were directed most often to **internal concave regions**.
3. **Detection of non-accidental (invariant) properties.** The system identifies which properties of the edges stay the same across viewing angles. Biederman listed **five**:

   | Invariant property | Meaning |
   |---|---|
   | **Curvature** | Points lying on a curve |
   | **Parallel** | Sets of points running in parallel |
   | **Cotermination** | Edges ending at a common point |
   | **Symmetry** | Symmetry versus asymmetry |
   | **Collinearity** | Points lying along a common straight line |

4. **Determination of components.** Geons are built from these properties. A cylinder, for example, has **curved** edges at its ends joined by **two parallel** straight edges.
5. **Matching to stored object representations.** The geons and their **relations** are matched against **structural models** in long-term memory, which specify the relevant geons, their orientations, sizes and so on. The object is identified as whichever stored model fits best.

Biederman argued that these five properties are valuable because they do not change with orientation and can be recovered from just a few points on each edge, so a geon can be extracted despite large changes of viewpoint, partial occlusion and noise.

> **Trap.** Memorise the five invariant properties as a set: **curvature, parallel, cotermination, symmetry, collinearity**. Distractors include "convexity", "closure", "proximity" (Gestalt or figure-ground cues) and "colour" (which RBC explicitly treats as secondary to edges). Note also that RBC uses **concavities** to parse objects into parts, whereas **convexity** is a figure-ground cue in Section 3.3.

#### The key prediction: viewpoint invariance

Because recognition depends on identifying geons, and geons can be identified from almost any angle, RBC predicts that recognition is typically **viewpoint-invariant**: an object should be recognised about equally easily from nearly all viewpoints. Recognition from a particular angle should be hard only when that angle **hides one or more geons**. (Marr's 3-D model representation was also assumed to be viewpoint-invariant.)

#### The non-accidental principle

An important part of the theory is the **non-accidental principle**: regularities in the image are taken to reflect **real** regularities in the world, not accidents of the current viewpoint. If the image contains a two-dimensional symmetry, the visual system assumes the three-dimensional object is symmetrical. Usually this is a safe bet, but occasionally it misleads. A straight line in the image normally signals a straight edge in the world, but a **bicycle seen end-on** produces straight lines from curved wheels.

#### Recognition under poor conditions

How do we recognise an object when, for instance, something in front of it hides part of it? Biederman pointed to three factors:

- The invariant properties (curvature, parallel lines and so on) can still be detected when **only parts of the edges** are visible.
- If the **concavities** of a contour are visible, there are mechanisms that can **restore** the missing parts of the contour.
- Complex objects carry a lot of **redundant** information, so they can be recognised even when some geons are missing. A giraffe can be identified from its neck alone.

#### Findings

- **Neurons sensitive to geons.** **Vogels et al. (2001)** recorded from single neurons in **inferior temporal cortex** and compared responses to a **change in a geon** with responses to a **change in object size** that left the geon unchanged. Some neurons responded more to the geon change, which gives some support to the reality of geons.
- **Viewpoint invariance supported.** **Biederman and Gerhardstein (1993)** had people name objects that were preceded by a prime showing the same object. Naming was primed **as much when the two views differed by 135 degrees** as when they were identical, as RBC predicts.
- **Viewpoint dependence with novel objects.** Biederman and Gerhardstein used **familiar** objects, which people have usually seen from many viewpoints, and that makes viewpoint changes easier to cope with. **Tarr and Bülthoff (1995)** used **novel** objects and gave observers extensive practice with them from **particular** viewpoints. Recognition was then **viewpoint-dependent**: performance was better from the **familiar** viewpoints.
- **Edges are not enough.** RBC says recognition depends on **edges** rather than surface information such as colour. **Sanocki et al. (1998)** pointed out that edge extraction should struggle when objects appear **among other objects**, because it becomes hard to tell which edges belong to which object. They briefly showed objects as **line drawings** or **full-colour photographs**, either **in isolation** or **in context**. Recognition was **much worse for line drawings than for colour photographs**, especially **in context**. Biederman had therefore overstated the role of edge extraction.
- **Top-down effects are missing.** Figure 3.8 is entirely bottom-up, but expectation and knowledge often matter, particularly when recognition is difficult (Viggiano et al., 2008, below).

#### Evaluation of RBC

**Strengths.** The theory has been very influential. It offers an answer to a hard puzzle: how we identify objects despite large differences in shape, size and orientation among category members. The assumption that geons or geon-like components are involved is plausible, and **concavities and edges** clearly are important in recognition.

**Limitations.**

1. **Bottom-up bias.** It concentrates on processes triggered directly by the stimulus and underplays top-down processes based on expectation and knowledge.
2. **Coarse discriminations only.** It accounts for fairly unsubtle distinctions. It helps explain whether the animal in front of you is a dog or a cat, but not **which breed** of dog or cat it is.
3. **Viewpoint invariance overstated.** It assumes that recognition generally matches a viewpoint-independent representation of the stimulus with stored object information, and there are many exceptions (below).
4. **Too inflexible.** The idea that objects are made of a fixed set of invariant geons is too rigid. Hayward and Tarr (2005) make the point that you can put a working light bulb on top of almost any object and call it a lamp; in the right circumstances almost anything in the image can act as a feature.

> **Trap.** RBC versus view-based accounts. **RBC (Biederman, 1987)**: structural description from about **36 geons** and **five non-accidental properties**; predicts **viewpoint-invariant** recognition; supported by **Biederman and Gerhardstein (1993)** (135-degree priming). **View-based (viewer-centred) accounts**: objects stored as **particular views**; recognition is best from familiar views and slows with rotation; supported by **Tarr and Bülthoff (1995)** with **novel** objects. Classic background: Tarr and Bülthoff are the names most associated with the view-based side. The 7th-edition resolution is the categorisation versus identification distinction below.

### Does viewpoint influence object recognition?

Imagine a bicycle. You almost certainly pictured it **side-on**, both wheels visible. That is its **canonical** (typical) view. If one group of people sees a photograph of a bicycle from the side and another group sees the same bicycle **end-on** or from **above**, will the first group recognise it faster?

Two terms frame the question:

- Recognition is **viewpoint-invariant** if it is equally fast and easy from any viewing angle.
- Recognition is **viewer-centred** (viewpoint-dependent) if it is generally faster and easier from certain angles.

A second distinction turns out to be just as important:

- **Categorisation**: deciding what kind of thing it is (is it a dog?).
- **Identification**: a **within-category** discrimination (is it a poodle?).

#### Findings

**The behavioural pattern.** **Milivojevic (2012)** reviewed the behavioural evidence. When the task requires **categorisation**, orientation typically has **no** effect on recognition, so recognition looks largely **viewpoint-invariant**. When the task requires **identification**, recognition is **significantly slower** when the object is turned away from its canonical view, so recognition is **viewer-centred**.

**Hamm and McMullen (1998)** illustrate this neatly. Changing viewpoint did **not** affect recognition when people only had to categorise (decide that an object was a **car**), but it **did** affect recognition when they had to identify (decide whether it was a **taxi**).

**Reaction times can hide orientation effects.** Most studies of this issue (Biederman & Gerhardstein, 1993; Tarr & Bülthoff, 1995; Hamm & McMullen, 1998) used behavioural measures, mainly reaction time. But a small or absent effect on reaction time does not show that orientation had no effect on the internal processing. **Milivojevic et al. (2011)** showed letters or digits in several orientations and asked participants to categorise each as a letter or a digit. Orientation had only **small** effects on speed and accuracy, but **relatively large** effects on **event-related potentials (ERPs)**: early ERP components were **larger** when the character was **not upright**. These components seemed to reflect low-level feature processing and object classification. So viewer-centred processes were at work even though categorisation speed hardly depended on orientation.

**Neuroimaging.** In **categorisation** tasks, brain activation is mostly very similar whatever the object's orientation, but orientation does affect activity **early** in processing, so the initial processing is viewpoint-dependent (Milivojevic, 2012). In **identification** tasks, areas in the **inferior temporal cortex** are typically **more** active when an object is in a non-canonical orientation. That fits the heavy involvement of inferior temporal cortex in object recognition (Peissig & Tarr, 2007): identifying an object from an unusual angle seems to need extra processing, possibly a more detailed analysis of its features.

**Learning shifts recognition towards invariance.** Familiar faces are less affected by changes of view than unfamiliar ones. **Zimmermann and Eimer (2013)** presented unfamiliar faces over **640 trials**. During the **first half**, face recognition was **view-dependent**; later, as the faces became familiar, it became **more viewpoint-invariant**. Learning stored more information about each face in long-term memory, which allowed fast access to the face memory from any orientation.

**The verdict.** **Hayward (2012)** reviewed the evidence and concluded that it strongly indicates that the **ventral visual pathway**, the presumed basis of visual object understanding, builds **viewer-centred** representations of objects. The most likely reason is cost: building viewpoint-invariant representations is too expensive computationally, which echoes the criticism of Marr's 3-D models.

> **Trap.** The 7th-edition answer to "is object recognition viewpoint-invariant?" is **"it depends on the task"**: largely invariant for **categorisation** (car), viewer-centred for **identification** (taxi) (Milivojevic, 2012; Hamm & McMullen, 1998). Even when reaction times show no orientation effect, ERPs can (Milivojevic et al., 2011). The ventral stream's representations are best described as **viewer-centred** (Hayward, 2012). An older key that simply marks "object recognition is viewpoint-invariant (Biederman)" as correct reflects the 1987 theory, not the 7th edition's conclusion.

---

### Inferotemporal cortex

#### Why IT cortex is the end of the line for recognition

The **inferotemporal (IT) cortex**, especially its **anterior** part, is crucial for visual object recognition (Peissig & Tarr, 2007). Two lines of monkey research show this, first by correlation and then by causation.

**Correlation: binocular rivalry.** In **binocular rivalry**, each eye receives a different image and the observer consciously sees only one at a time, with the two alternating. Because the stimulus stays constant while the percept flips, rivalry lets you ask which neurons track **what is seen** rather than **what is shown**. **Leopold and Logothetis (1999)** and **Blake and Logothetis (2002)** trained macaques to report which of the two images they were perceiving while neurons were recorded at different stages of the visual system. The link between neural activity and perception grew stronger at later stages. Only about **20%** of neurons in **V1** had activity associated with the monkey's percept, compared with about **90%** in higher areas such as **inferotemporal cortex** and the **superior temporal sulcus**.

**Causation: microstimulation.** A correlation between IT activity and perception does not show that IT activity produces perception. **Afraz et al. (2006)** closed that gap. They trained **two** macaques to judge whether degraded images were **faces or non-faces**. On some trials they electrically **microstimulated face-selective neurons** in IT cortex. Stimulation **greatly increased the number of "face" decisions**. Driving those neurons made the monkeys see faces, which establishes a **causal** link between face-selective IT activity and face perception.

> **Trap.** Binocular rivalry studies (Leopold & Logothetis, 1999; Blake & Logothetis, 2002) are **correlational**: 20% of V1 neurons versus 90% in IT and STS track the percept. **Afraz et al. (2006)** is the **causal** study (microstimulation of face-selective IT neurons increased face judgements). If asked which study shows that IT activity *causes* a perceptual decision, the answer is Afraz.

#### Selectivity and invariance

Suppose you record IT neurons while showing many objects at different angles and sizes. Two dimensions describe the responses (Ison & Quiroga, 2008):

- **Selectivity**: a neuron that responds strongly to one object and weakly or not at all to others is **highly selective**.
- **Invariance (tolerance)**: a neuron that responds almost equally to a given object whatever its orientation, size and so on is **highly invariant**.

At first sight, highly invariant IT neurons support viewpoint-invariant theories and low-invariance neurons support viewpoint-dependent theories. Hayward (2012) urges caution: a neuron that responds to an object from every angle might be part of a genuinely **object-centred** representation, or it might simply receive excitatory input from **many view-specific neurons**, in which case it is really part of a **view-based** network. Invariance at the single-cell level does not settle the theoretical question.

**What the recordings show.**

- **Logothetis et al. (1995)**, a classic study, showed monkeys unfamiliar objects repeatedly. Many IT neurons were **viewpoint-dependent**, responding more to objects shown from a **familiar** viewpoint than from an unfamiliar one.
- **Booth and Rolls (1998)** first let monkeys **play with novel objects** in their cages, then showed photographs of the objects from different viewpoints while recording from the **superior temporal sulcus**. **49%** of neurons responded mainly to **specific views**; only **14%** gave **viewpoint-invariant** responses. Those few invariant neurons may matter more than their numbers suggest, because their pattern of activation carried enough information, in principle, to discriminate accurately among the objects.
- **Zoccolan et al. (2007)** made the first systematic attempt to relate the two dimensions and found a **moderate negative correlation** between selectivity and tolerance. Some neurons respond to many objects across many sizes and orientations; others respond mainly to one object in a narrow range of views. A plausible reason is that visual tasks range from very precise identification to very broad categorisation, and having neurons with very different response profiles supports both.

#### The "Jennifer Aniston neuron"

Some neurons show astonishing selectivity. Recording from **human** patients, **Quiroga et al. (2005)** came across a **medial temporal lobe** neuron with a striking preference: it fired vigorously to photographs of the *Friends* actress **Jennifer Aniston** and hardly at all to other famous faces or to objects. Oddly, it did **not** respond to pictures of Aniston **with Brad Pitt**. Other neurons responded selectively to other people (for example **Julia Roberts**) or to a famous building (the **Sydney Opera House**).

Does this mean each person you know is stored in a single cell, a so-called grandmother cell? The book says this is extremely unlikely. Quiroga et al. sampled a tiny number of neurons out of the roughly **one million** activated by any visual stimulus, so it is wildly improbable that they happened on the only Aniston-responsive neuron. And if knowledge of a person lived in one neuron, losing that cell would erase all knowledge of the person. Quiroga et al. (2013) suggest instead that a person is represented by a **relatively small population**, perhaps a few thousand neurons or fewer.

**A caveat about species.** Most of the studies in this section used monkeys, because the invasive recording methods can be used only in non-human animals (Quiroga's patients were an exception, recorded clinically). The assumption that basic visual processes are similar in humans and monkeys is widely made but may not be entirely correct.

### Top-down processes

#### Beyond the feedforward hierarchy

Until fairly recently, most theories of object recognition, Biederman's included, emphasised **bottom-up** processing. The hierarchical anatomy of the visual system seemed to justify that: higher up the hierarchy, neurons respond to more and more complex stimuli. Yardley et al. (2012) describe this traditional picture as a bottom-up stream that analyses an image element by element and passes the results forward, area by area, until the object's form and identity are established.

The anatomy, however, says this is a big oversimplification. Throughout most of the visual system there are roughly **equal numbers of forward-projecting and backward-projecting neurons** (Wyatte et al., 2012; Gilbert & Li, 2013). Backward projections are the hardware of **top-down** processing.

#### When do top-down effects happen?

There is an important question of **timing**:

- Top-down processes might act only **after** an object has been recognised, for example during semantic processing of what is already identified. This would be theoretically uninteresting.
- Or they might act **before** recognition, perhaps originating in the **prefrontal cortex**, and be **necessary** for recognition to happen at all. This is the more interesting possibility.

Top-down effects should be largest when bottom-up information is **poor**: degraded stimuli, very brief presentations and so on.

#### Findings

**Ambiguous figures.** **Goolkasian and Woodberry (2010)** showed ambiguous figures that each have two interpretations (for example one that can be seen as an Eskimo or as a Native American head, another as a liar or as a face), each immediately preceded by a **prime** related to one reading (for example a winter scene or a tomahawk). The primes **systematically biased** which interpretation people saw: a top-down effect on perception (Figure 3.9).

**The orbitofrontal cortex predicts the object.** **Bar et al. (2006)** briefly presented drawings of objects followed by a mask, making them hard to recognise. Activation in the **orbitofrontal cortex** (part of the prefrontal cortex) appeared **50 ms before** activation in recognition-related regions of the **temporal cortex**. The orbitofrontal activity **predicted successful recognition**, so it seemed important for recognition to happen. When recognition was easy (longer, unmasked presentation), the orbitofrontal cortex was **less** involved. Bar et al. concluded that top-down processes are more important when recognition is hard.

Their model, in a modified version by Yardley et al. (2012) shown in Figure 3.10, has **two routes**:

| Route | Pathway | Speed | Role |
|---|---|---|---|
| **Top-down** | Coarse information projected rapidly to the **orbitofrontal cortex** | **Fast** | Generates **predictions** (best guesses) about what the object might be |
| **Bottom-up** | The **ventral visual stream** | **Slower** | Detailed analysis of the input, constrained by the predictions |

> **Classic background:** in Bar's account the fast route is thought to carry **low spatial frequency** information, which links this model back to the magnocellular, coarse-to-fine story earlier in the section.

**Disrupting the prefrontal cortex with rTMS.** Bar et al. showed timing and correlation. **Viggiano et al. (2008)** went further by interfering with the prefrontal cortex. Their participants recognised photographs of objects (some living, some not), presented either **blurred** or sharp (**non-blurred**), in each of four conditions:

1. **repetitive transcranial magnetic stimulation (rTMS)** to the **left dorsolateral prefrontal cortex**;
2. rTMS to the **right dorsolateral prefrontal cortex**;
3. **sham** rTMS (the procedure without a magnetic field);
4. a **baseline** with no rTMS.

rTMS to **either** side of the dorsolateral prefrontal cortex **slowed** recognition of the **blurred** photographs, but it had **no effect** on recognition of **non-blurred** ones. So top-down prefrontal processes are **directly** involved in object recognition **when bottom-up information is limited**. The sham condition matters: it rules out the idea that the noise and sensation of the TMS procedure, rather than the magnetic disruption, slowed people down.

**Do words change what you see, or only what you say?** The book sets up the problem carefully. Suppose you show an object photograph to one eye while flashing high-contrast noise to the other eye to keep the object out of awareness, and you precede each photograph with a **valid** verbal cue (naming the object that will appear), an **invalid** cue (naming a different object) or **no** cue. If valid cues improve people's judgements of which object was shown, that may only mean the cue biased their **judgement**, not their **perception**.

A stronger design asks a pure **detection** question: on some trials a suppressed stimulus is present, on others there is none, and observers say whether anything was there. If valid cues improve **detection**, the label must have altered perception itself.

**Lupyan and Ward (2013)** ran this study. Observers were told the suppressed stimulus would be a **circle** or a **square**, or were given no cue. The stimulus was actually a circle, a square, a shape intermediate between the two, or nothing. Performance (both **hit rates** and **detection sensitivity**, Figure 3.11) was significantly **better with valid than with invalid cues**. Verbal labels activated shape knowledge that influenced **basic visual detection**.

> **Classic background:** the suppression technique described here, a static image to one eye with rapidly changing high-contrast patterns to the other, is generally known as **continuous flash suppression**.

#### Evaluation of top-down processing

Top-down processes often affect **perception and object recognition themselves**, not merely judgements made after perception. Yardley et al. (2012) put it strongly, saying that perception depends on existing knowledge as much as on incoming information. Their influence is **greater when stimuli are degraded**. The main open question is how bottom-up and top-down processes **interact**. The interactions probably occur at several levels of the visual system, but what determines whether and where they occur is still largely unknown.

> **Trap.** "Top-down" is not the same as "post-perceptual". The 7th edition's evidence (Bar et al., 2006: orbitofrontal activity **50 ms before** temporal recognition areas; Viggiano et al., 2008: rTMS to DLPFC slows recognition of **blurred** images only; Lupyan & Ward, 2013: labels improve **detection**) is that top-down processes can act **before and during** recognition, and are most important when the bottom-up input is **weak**. Contrast Marr and Biederman, whose models are predominantly **bottom-up**.

### Classic background: visual agnosia

> **Classic background:** the 7th-edition chapter mentions object agnosia only through patient **CK** (Section 3.5), but Indian papers regularly ask about the classic classification of the **visual agnosias**, a failure to recognise objects that is not explained by poor basic vision, language problems or general intellectual decline. Lissauer (1890) distinguished two broad types. In **apperceptive agnosia** the deficit is **perceptual**: the patient cannot form a coherent percept of the object's shape, so they cannot copy a drawing of it or match two views of it. In **associative agnosia**, perception is relatively intact (the patient can copy a drawing accurately and match shapes) but the percept **fails to make contact with stored knowledge**, so the patient cannot say what the object they have just copied actually is. **Prosopagnosia** is often described as a face-specific form of agnosia. Chapter 2's patient **DF** (visual form agnosia, with preserved visually guided action) is usually classed with the apperceptive group.

> **Trap.** **Apperceptive** = cannot **perceive** the form (fails at copying and shape matching). **Associative** = perceives the form (**can copy**) but cannot **give it meaning**. The test that separates them is **copying a drawing**. Do not confuse either with **visual form agnosia** versus **optic ataxia** (Chapter 2), which contrasts a ventral-stream perception deficit (DF) with a dorsal-stream deficit in visually guided reaching.

---

## 3.5 Face Recognition

### Why faces get their own section

The book gives three reasons for treating faces separately from other objects.

1. **Importance.** We usually identify people by their faces. Picture someone important to you: the image is almost certainly of their face and its distinctive features, not their build.
2. **Difference.** Face recognition seems to work differently from recognition of other objects, so general object-recognition theories (such as RBC) explain it only to a limited extent, and face-specific theories are needed.
3. **Depth of understanding.** Face recognition is now well understood, partly because the evidence comes from three converging sources: behavioural experiments, brain-damaged patients and neuroimaging.

### Face versus object recognition

#### Holistic processing

The key difference is that face recognition relies more on **holistic processing**: information from the **whole** face is tightly integrated, so that the **relationships among the features** (how far apart the eyes are, how the nose sits relative to the mouth) are processed along with the features themselves.

Holistic processing has two advantages over processing one feature at a time:

- **Speed.** The features are processed **in parallel** rather than serially. Familiar faces can usually be recognised in **under half a second** (Bruce & Young, 1986).
- **Reliability.** Individual features change: skin tone varies with a tan, mouth shape changes with expression. A representation of the whole configuration is more robust than any single feature.

> **Trap.** **Holistic** (configural) processing = the face is processed as an integrated whole, including the spatial relations between features. **Featural** (piecemeal, analytic) processing = parts are processed separately. The three standard markers of holistic processing are the **face inversion effect**, the **part-whole effect** and the **composite face effect**. Know what each measures; questions often describe one and name another.

#### The face inversion effect

The **face inversion effect** is the finding that faces are **much harder to identify upside down** than upright. Inversion disrupts the configuration on which holistic processing depends. For **non-face objects** the cost of inversion is usually **much smaller**, and it tends to **disappear quickly with practice** (McKone et al., 2007; Bruyer, 2011). That asymmetry is evidence that faces are processed more holistically than other objects.

The evidence is not all one way, because **expertise** complicates it:

- **Diamond and Carey (1986)** found that **dog experts** showed an inversion effect for photographs of **dog breeds** about **as large** as their inversion effect for faces.
- **Rossion and Curran (2010)** found that **car experts** showed a **much smaller** inversion effect for cars than for faces, but within the group, those with the **greatest** expertise showed a **larger** inversion effect for cars than those with less.

> **Classic background:** the **Thatcher illusion** (Thompson, 1980) dramatises the inversion effect. If the eyes and mouth of a face are cut out and turned upside down within an otherwise upright face, the result looks grotesque; turn the whole picture upside down and the oddity is hard to notice. Inverting the face disrupts the configural processing that would normally expose the wrongly oriented features.

#### The part-whole effect

The **part-whole effect** is the finding that a face part is recognised **more easily within a whole face** than on its own. **Farah (1994)** had participants learn names for drawings of **faces** and **houses**. They were then tested with either the whole face or house, or a **single feature** (a mouth, a front door). For **faces**, recognition of a part was **much better** when the **whole** face was shown. For **houses**, recognition was about the **same** whether the whole house or only the feature was shown. Face features are stored as parts of a whole; house features are stored more independently.

> **Classic background:** the part-whole paradigm is usually traced to **Tanaka and Farah (1993)**; the 7th edition cites Farah (1994). Either citation should be accepted for the effect itself.

#### The composite face effect

**Richler et al. (2011)** used **composite faces**: the top half of one face joined to the bottom half of the same or a different face. Participants judged whether the **top halves** of two successive composites were the same or different, and were told to ignore the bottom halves. Performance was **worse when the bottom halves differed**. People cannot help processing the bottom half along with the top half, so the halves fuse into a new-looking face. This **composite face effect** is further evidence that faces are processed holistically.

Richler et al. (2011) also found that people who showed **stronger holistic processing** had **better face recognition**, which is what you would expect if holistic processing is what face recognition depends on.

| Effect | Manipulation | Result | What it shows |
|---|---|---|---|
| **Inversion** | Turn the face upside down | Recognition drops sharply for faces, much less for objects | Faces rely on configural processing that inversion disrupts |
| **Part-whole** (Farah, 1994) | Test a feature alone or inside the whole | Face features recognised better in the whole; house features no different | Face parts are stored as parts of a whole |
| **Composite** (Richler et al., 2011) | Pair a top half with a different bottom half | Same/different judgements on the top half are impaired by a different bottom half | The two halves cannot be processed independently |

#### Special, or just practised?

The evidence so far suggests faces and objects are processed differently. The deeper question, which runs through the rest of the section, is **why**. Either there is something **special about faces** (an innate, dedicated system), or we simply have **far more expertise** with faces than with any other category. The prosopagnosia evidence, the fusiform face area and the expertise hypothesis all bear on that question.

### Prosopagnosia

#### The logic of the patient evidence

If every patient with severely impaired face processing also had severely impaired object processing, that would suggest a common mechanism. If faces are processed differently, there should be patients whose face recognition is badly damaged while object recognition is spared. Such patients exist. They have **prosopagnosia** (from Greek words meaning "face" and "without knowledge"), popularly called **face blindness**: a severe impairment of face recognition with much less impairment of object recognition, usually resulting from brain damage.

Prosopagnosia is **heterogeneous**: the exact pattern of face and object problems differs from patient to patient. One reason is that it has two origins:

- **Acquired prosopagnosia**, caused by brain damage.
- **Developmental prosopagnosia**, which occurs **without any obvious brain damage**.

There appear to be **few or no pure cases**: most patients have at least some difficulty beyond faces.

> **Trap.** **Acquired** prosopagnosia follows brain damage (for example to occipitotemporal face regions). **Developmental** prosopagnosia appears **without obvious brain damage** and is usually lifelong (Heather Sellers is the book's example). Do not equate developmental prosopagnosia with "prosopagnosia from brain damage in childhood". And note the book's caution that **pure** prosopagnosia is rare or non-existent.

#### Covert recognition

Many prosopagnosics show **covert recognition**: processing of faces without conscious awareness. **Simon et al. (2011)** showed familiar and unfamiliar faces to a prosopagnosic patient, **PS**, who could not consciously recognise the familiar faces. Yet PS's **fusiform face area** (see below) was **more active for familiar than for unfamiliar faces**. The brain was registering familiarity below the level of awareness.

> **Trap.** Covert recognition means the patient **denies** recognising a face while some **implicit** measure (here FFA activation, Simon et al., 2011) shows that the face has been processed as familiar. It parallels blindsight in Chapter 2 (processing without awareness), but blindsight concerns detection after V1 damage, while covert face recognition concerns familiarity in prosopagnosia.

#### In the real world: Heather Sellers

Prosopagnosia affects **up to 2%** of the population. The book illustrates what it means in daily life with **Heather Sellers**, an American woman with prosopagnosia who described her experiences in a **2010** book, *You Don't Look Like Anyone I Know*.

Key points of her case:

- As a child she was separated from her mother in a grocery store, and when staff brought them back together she **did not at first recognise her own mother**.
- Her **object recognition is essentially normal**; the problem is specific to faces.
- She struggles even with **her own face**. As a child she could barely find herself in school photographs. As an adult she has, on occasion, stepped aside for a woman in a mirrored lift before realising the woman was her own reflection. Experiences like these made her very anxious.
- She did not realise she had prosopagnosia until her **mid-thirties**. She had been getting by with other cues: **hairstyle, body type, clothing, voice and gait**.
- Those cues did not save her from frequent embarrassment. She has walked straight past friends, angering them, and has occasionally **failed to recognise her own husband**. She describes the condition as feeling like constant failure.

Her case shows why developmental prosopagnosia can go undetected for decades: people compensate with non-facial cues and assume everyone finds faces as hard as they do.

#### Two explanations for face-specific impairment

Why should someone have very poor face recognition but reasonable object recognition?

1. **Face-specific damage.** They have damage to a brain area **specialised for faces**.
2. **Difficulty.** Face recognition is simply **harder**. Recognising a face means distinguishing among members of **one** category (faces), whereas object recognition often only requires naming the **category** (cat, car). On this account, prosopagnosics should also fail whenever they must make **fine-grained** within-category distinctions among objects.

#### Findings

**Patient GG (Busigny et al., 2010b).** GG, a man with acquired prosopagnosia, was compared with healthy controls on five categories: **birds, boats, cars, chairs and faces**. On each trial a target from one category was followed by two items from the same category (the target and a distractor), and the participant had to pick the one seen before. GG was **as accurate as controls on every non-face category**, but much worse on faces: **67% versus 94%**. GG's impairment is **face-specific**, not a general problem with complex within-category stimuli. (Figure 3.12, which shows accuracy and speed for GG and controls, is credited in the book's caption to "Busigny et al. (2012b)", which appears to be a slip for 2010b.)

**Patient PS (Busigny et al., 2010a).** Busigny et al. (2010a) found earlier reports of at least **13** prosopagnosics with essentially normal object recognition despite very poor face recognition. They pointed out **two weaknesses** in that literature:

1. The **difficulty** of the object decisions had not been systematically manipulated, so it was hard to know whether the object tasks were as hard as the face tasks.
2. Only **accuracy** had been measured, not **speed**. A patient might reach normal accuracy on objects by working very slowly.

They fixed both problems in a study of **PS**, a woman with prosopagnosia. They varied the **similarity** between targets and distractors in an object-recognition task and recorded **reaction times** as well as errors. Making targets and distractors more similar raised error rates **to the same extent in PS as in controls**. On faces, by contrast, PS performed very poorly **even when the face task was very easy for controls**. That pattern rules out the difficulty explanation for PS: her face deficit is not just a matter of faces being hard.

**The reverse dissociation: patient CK (Moscovitch et al., 1997).** If faces and objects use partly different brain areas, there should also be patients with impaired **object** recognition but intact **face** recognition. **Moscovitch et al. (1997)** described **CK**, a man with **object agnosia**. His face recognition matched that of healthy controls whether faces were **photographs, caricatures or cartoons**, provided the face was **upright** and its **internal features were in the right places**. Together with GG and PS, CK gives a **double dissociation** between face and object recognition.

> **Trap.** A **single dissociation** (GG or PS: faces impaired, objects spared) is consistent with faces simply being harder. The **double dissociation** needs the reverse case too: **CK** (Moscovitch et al., 1997), with **object agnosia** but **normal** face recognition **as long as faces were upright with features in place**. That proviso is itself evidence for holistic face processing: CK's intact system is the configural face system, and it failed when the configuration was disrupted.

#### Why are prosopagnosics so poor at faces? Holistic processing

A popular explanation is that prosopagnosics have great difficulty with **holistic processing**. Busigny et al. (2010b) tested this in GG, who showed **neither** a face inversion effect **nor** a composite face effect. GG does not perceive individual faces holistically. Since holistic processing is needed to recognise individual faces but not individual objects, his object recognition survived.

**Van Belle et al. (2011)** tested GG in a condition where observers could see **only one part** of a face at a time (an eye, the mouth), which prevents holistic processing. In that condition GG performed **as well as controls**. When the **whole face** was visible and holistic processing was possible, GG was **much worse** than controls. Restricting everyone to piecemeal processing levelled the field, which shows that what GG lacks is precisely the holistic route.

> **Trap.** In Van Belle et al. (2011) GG was **normal** when viewing was restricted to one feature at a time and **impaired** with the whole face visible. Students often reverse this. The logic: controls lose their holistic advantage under restricted viewing; GG never had it, so the gap disappears.

### The fusiform face area

#### The case for a face area

If faces are processed differently, there may be **brain regions** specialised for them. The best-known candidate is the **fusiform face area (FFA)** in the **ventral temporal cortex** (Figure 3.13). Two lines of research support its role:

1. It is **often damaged** in patients with prosopagnosia (Kanwisher & Yovel, 2006).
2. Neuroimaging shows it is usually **more activated by faces** than by other objects. **Downing et al. (2006)** showed participants **faces, scenes and 18 object categories** (tools, fruits, vegetables and so on); the FFA responded **significantly more strongly to faces** than to any other category.

#### Complications

**Lesions.** Prosopagnosic patients often have damage to the **occipital face area (OFA)** as well as, or instead of, the FFA. **Gainotti and Marra (2011)** therefore argued that face processing depends on a **network** including both areas, not on the FFA alone.

**Imaging.** Neuroimaging has revealed **several** face-selective regions, not one (Figure 3.13 shows the **anterior face patch (AFP2)**, the **FFA** and the **OFA**, from Weiner & Grill-Spector, 2012). **Kanwisher et al. (1997)**, the study that named the area, found that only **80%** of participants showed greater FFA activation to faces than to other objects. Why, then, has the FFA been given such a central role? One reason, according to **Weiner and Grill-Spector (2012)**, is the use of **lenient criteria** for deciding whether face-related activation falls in the FFA. Individual brains may show several distinct face-responsive areas, but averaging data across people tends to blend them and exaggerate the FFA's role.

**Verdict.** The FFA is definitely involved in face processing and recognition for **most, but not all**, people. The claim that face processing is **localised** in the FFA is **incorrect**: face processing is far more likely to depend on a **network** that includes the FFA and the OFA (Atkinson & Adolphs, 2011). And the FFA is also activated by **many kinds of object other than faces**, which is why the book's key-term definition calls the name somewhat misleading.

> **Trap.** The 7th edition does **not** say the FFA is a face-only module. Its position: the FFA is **involved** in face processing in most people; face processing is a **network** (FFA, OFA and other patches; Gainotti & Marra, 2011; Atkinson & Adolphs, 2011); only **80%** of Kanwisher et al.'s (1997) participants showed the face preference; and the FFA responds to other objects too. An older key that marks "the FFA is the face-specific module" as correct reflects the strong modular claim the 7th edition rejects.

---

### The expertise hypothesis

#### The claim

**Gauthier and Tarr (2002)** argued that many findings that seem to show faces are special should be treated with suspicion, because we have vastly **more expertise** with faces than with telling apart individual members of any other category. Their **expertise hypothesis** states that the brain regions and processing mechanisms supposedly specific to faces are in fact used for recognising members of **any category in which we are expert**. On this view the FFA might better be called the **"fusiform expertise area"**.

Why should expertise matter? The plausible link is that expertise produces **holistic processing**. A chess expert takes in a whole board position as a meaningful pattern in an instant, because stored knowledge lets them see it as a configuration rather than as separate pieces (see Chapter 12 on chess expertise).

The hypothesis yields **four predictions**:

1. **Holistic (configural) processing** is not unique to faces; it should appear for **any object of expertise**.
2. The **FFA** should be strongly activated when people recognise members of **any category of expertise**.
3. **Young children**, having less face expertise, should show **less holistic face processing** than older children and adults.
4. If faces and objects of expertise use similar processes, objects of expertise should **interfere** with face processing.

#### Findings, prediction by prediction

**Prediction 1: holistic processing for objects of expertise.**

- **For.** **Wallis (2013)** took a model of object recognition and asked what it would predict after prolonged exposure to a single category. The model predicted that the hallmarks of face processing (holistic processing, the inversion effect) should emerge for **any** category of expertise: repeated co-occurrence of the same features (eyes, nose, mouth) gradually builds holistic processing. Wallis concluded that **one model can explain both object and face recognition**.
- **For.** **Kundel et al. (2007)** showed mammograms with or without breast cancer to doctors. The most expert doctors usually **fixated the cancer almost immediately**, which suggests fast, holistic processing.
- **Against.** **McKone et al. (2007)** reviewed studies of expertise with non-face objects and found that expertise **generally failed** to produce either the **inversion** effect or the **composite** effect, the two classic markers of holistic processing.
- **For again.** Other studies, including **Rossion and Curran (2010)** and **Diamond and Carey (1986)**, have found holistic processing associated with expertise for non-face objects. The evidence is mixed.

**Prediction 2: the FFA and expertise.**

- **Weak.** McKone et al. (2007) found only a **modest** tendency for the FFA to respond more to objects of expertise, and **larger** expertise effects **outside** the FFA than inside it.
- **Stronger.** **Bilalić et al. (2010)** had chess experts and novices do several tasks with chess pieces. Experts showed **more FFA activation than novices in every condition**. However, **faces** still activated the FFA **more than chess displays** did, for experts and novices alike.
- **Stronger.** **McGugin et al. (2012)** found that FFA activation to **cars** increased with participants' **car expertise**.
- **Developmental.** If the FFA is tied to expertise, it should **grow** through childhood and early adulthood as face expertise accumulates, and it does: FFA size increases substantially during development (Wallis, 2013).

**Prediction 3: holistic processing in children.** **Crookes and McKone (2009)** reviewed the developmental evidence. Most studies suggest that young children show some holistic face processing that **increases** with age. But Crookes and McKone noted that most studies had **not matched task difficulty across age groups**, so younger children may simply have found the tasks harder. When they **controlled** for this, children aged **7 or younger** showed **adult levels** of holistic processing. This result goes **against** the expertise hypothesis, since young children have far less face experience than adults.

**Prediction 4: interference.** **McKeeff et al. (2010)** had car experts and novices search for **face targets** among distractors that were either **cars and faces** or **watches and faces**. Car experts were **slower than novices when searching among cars**, but the two groups did **not differ when searching among watches**. Car expertise and face expertise seem to compete for the **same or similar** processes, as the hypothesis predicts.

> **Trap.** The four predictions are not all supported. Score them: (1) holistic processing for expertise, **mixed** (Wallis, Kundel, Diamond & Carey, Rossion & Curran for; McKone et al., 2007, against); (2) FFA activation by expertise, **partly** supported (Bilalić et al., 2010; McGugin et al., 2012; but faces still win, and McKone found bigger effects outside the FFA); (3) less holistic processing in young children, **not supported** once difficulty is matched (Crookes & McKone, 2009: adult-level by age 7 or less); (4) interference, **supported** (McKeeff et al., 2010). An option claiming "Crookes and McKone showed children lack holistic face processing" has the finding backwards.

#### Evaluation of the expertise hypothesis

There is **some** support for each of the four predictions, but how much remains disputed. A major reason is that **expertise is almost impossible to measure precisely or to control**. Many theorists have taken extreme positions, either that **all** the differences between face and object processing are due to expertise or that **none** are. A middle position is entirely possible: **many but not all** of the differences may reflect our greater expertise with faces. That would mean faces are special, but **less special than often assumed**.

> **Trap.** "Faces are special" (domain-specificity; the FFA as a face module; Kanwisher's tradition) versus the **expertise hypothesis** (Gauthier & Tarr, 2002: the "fusiform expertise area"). The 7th-edition verdict is a **compromise**, not a win for either: many, but not all, face-object differences are due to expertise. Questions offering "faces are processed by an entirely face-specific innate system" or "all face effects are due to expertise" are both overstatements.

### Theoretical approaches: Bruce and Young's model

#### The eight components

Of the many models of face recognition, **Bruce and Young's (1986)** has been by far the most influential. Figure 3.14 is lost, so here are its **eight** components and what each does:

| # | Component | Function |
|---|---|---|
| 1 | **Structural encoding** | Builds various descriptions (representations) of the face |
| 2 | **Expression analysis** | Infers the person's emotional state from the face |
| 3 | **Facial speech analysis** | Uses lip movements to help speech perception (lip-reading; Chapter 9) |
| 4 | **Directed visual processing** (printed "direct visual processing" in the 7th edition) | Selective processing of particular facial information |
| 5 | **Face recognition units (FRUs)** | Store structural information about **known** faces, emphasising the **less changeable** aspects at a fairly **abstract** level |
| 6 | **Person identity nodes (PINs)** | Hold information about the individual (occupation, interests and so on) |
| 7 | **Name generation** | Names are stored **separately** |
| 8 | **Cognitive system** | Holds additional knowledge (for example, that most actors have attractive faces) and influences which other components receive attention |

The flow for recognising a **familiar** face runs: structural encoding, then a match in the **face recognition unit** (a sense of familiarity), then the **person identity node** (who the person is and what you know about them), and only then **name generation**. Expression analysis, facial speech analysis and directed visual processing branch off from structural encoding as **separate** routes that do not depend on knowing who the person is. The cognitive system is connected to the whole arrangement.

#### Three predictions

1. **Familiar and unfamiliar faces are processed very differently.** FRUs, PINs and name generation are involved only for **familiar** faces, so familiar faces are much easier to recognise, especially from unusual angles or in unusual lighting.
2. **Identity and expression are processed by separate routes.** Facial **identity** (who is it?) depends on the relatively **unchanging** aspects of the face; **expression** (what are they feeling?) depends on the **changeable** aspects, handled by the **expression analysis** component.
3. **Information is accessed in a fixed order.** Familiarity (FRU) comes first, then personal information (PIN), then the name. So you can find a face familiar without remembering anything else about the person, or remember things about the person without their name, but a face should **never** produce a name without other personal information.

> **Trap.** In Bruce and Young (1986) the **name** comes **last**: FRU (familiarity) before PIN (semantic information such as occupation) before name generation. "Recalling a name while knowing nothing else about the person" is the error the model says should **never** happen. Do not confuse **face recognition units** (stored structural descriptions of known faces, giving familiarity) with **person identity nodes** (biographical knowledge).

#### Duchaine and Nakayama's simplified version

**Duchaine and Nakayama (2006)** produced a simplified version (Figure 3.15) with one addition: a **face detection** stage at the very start, where the observer decides whether the stimulus is a face at all. Detection is followed by structural encoding, which is then matched against **face memory**; the same perceptual representation also feeds **expression recognition** and **gender discrimination**. The detection stage is justified by a prosopagnosic called **Edward**: despite his very poor face recognition at later stages, he **detected faces as quickly as healthy people** (Duchaine & Nakayama, 2006). Face detection and face identification can therefore come apart.

#### Findings: prediction 1, familiar versus unfamiliar faces

The model offers several reasons why familiar faces are easier, but the most important is that we hold much more **structural information** about familiar faces (in the FRUs). That information concerns the relatively stable aspects of a face and builds up gradually as a face becomes familiar. The evidence suggests the familiar-unfamiliar difference is even **larger** than Bruce and Young assumed.

##### In the real world: recognising unfamiliar faces

**Jenkins et al. (2011)** gave British participants **40** face photographs and asked them to sort them into piles, one pile per person. Figure 3.16 shows a similar array. Most people looking at it think they see many different people.

- The participants produced on average **7.5** piles. In fact the 40 photographs showed only **two** people: **20** photographs each of **two Dutch celebrities** who are virtually unknown in Britain. People overestimated the number of individuals by a factor of **almost four**.
- When **Dutch** participants, to whom the celebrities were **familiar**, did exactly the same task, **nearly all of them sorted perfectly** into two piles of 20.
- In a third experiment, participants rated the attractiveness of **400** photographs (**20** photographs each of **20** unfamiliar people). Ratings varied **more within individuals than between individuals**: two photographs of the same person could differ in attractiveness more than photographs of two different people. (This is why celebrities can look surprisingly unattractive in unplanned photographs.)

What follows from this?

1. A single person's face produces **highly variable images**, which is why different photographs of an unfamiliar person can look like different people.
2. **Passport photographs** are of limited value for identification.
3. It helps explain why **eyewitnesses** find it hard to identify a stranger who committed a crime (Chapter 8).
4. We are good at seeing that different photographs show the **same familiar** person because we have **so much information** about that person.

**Improving unfamiliar face identification.** **Jenkins and Burton (2011)** proposed **image averaging**: combine several photographs of the same person into one average image. Averaging cancels out the aspects that vary from photograph to photograph (lighting, expression, angle) and keeps what is stable. As predicted, identification from average images became **more accurate as more photographs went into the average**.

#### Findings: prediction 2, separate routes for identity and expression

**Haxby et al. (2000)** agreed that the routes are separate and proposed that **changeable** aspects of faces, especially expressions, are processed mainly in the **superior temporal sulcus (STS)**. There is some support:

- **Fox et al. (2011)** reported a crossover. Patients whose lesions hit the face-recognition network could still read **expressions** but had trouble with **identity**; one patient whose lesion was in the **STS** showed the opposite, poor **expression** perception alongside fairly well preserved **identity** perception.

But the routes are **not fully independent**:

- **Schweinberger and Soukup (1998)** found that judgements of **expression** were strongly influenced by **irrelevant identity** information, whereas judgements of **identity** were **not** influenced by the emotion expressed. The interaction is **asymmetric**: identity affects expression processing, not the reverse.
- **Fitousi and Wenger (2013)** showed that independence depends on the task. In task (A) participants responded "yes" only if a face had a given identity **and** a given emotion (for example, a happy Keira Knightley). In task (B) they responded "yes" if the face had the identity **or** the emotion **or** both. There was evidence of **independent** processing in task **(B)** but **not** in task **(A)**.

The expression route is also **more complex** than the model assumed. Damage to certain regions affects some emotions more than others: **amygdala** damage produces bigger deficits in recognising **fear and anger** than other emotions, and similar emotion-specific patterns appear when the same patients try to recognise emotions from **voices** (Calder & Young, 2005). **Young and Bruce (2011)** admitted that they had not expected emotion-recognition deficits to be specific to particular emotions.

> **Trap.** Older keys present Bruce and Young's **separate identity and expression routes** as established fact. The 7th edition says this assumption is **oversimplified and often incorrect**: Fox et al. (2011) support some separation, but Schweinberger and Soukup (1998) show **identity influences expression judgements** (not the reverse), and Fitousi and Wenger (2013) show independence only for the **OR** task. The chapter summary states it directly: good support for the familiar/unfamiliar difference, not for the identity/expression separation.

#### Findings: prediction 3, the order of access

**Young et al. (1985)** asked people to keep a record of the problems they had recognising faces. Across **1,008** recorded incidents:

- People **never** reported putting a **name** to a face while knowing nothing else about the person, as the model predicts.
- On **190** occasions someone remembered a reasonable amount about a person but **not their name**, also as predicted.
- On **233** occasions a face produced a **feeling of familiarity** without any other information about the person, again as predicted.

But the strict order may be too rigid. **Calderwood and Burton (2006)** showed fans of the television series *Friends* pictures of the main characters and asked them to recall either the **name** or the **occupation**. Names came **faster** than occupations, which suggests that names can sometimes be retrieved before personal information. The book adds a caveat: other personal information (such as the character's role in *Friends*) might have been retrieved even faster than the name.

#### Evaluation of Bruce and Young's model

Young and Bruce (2011) themselves offered a useful evaluation.

**Strengths.**

1. A **broad perspective**: the model stresses the wide range of information that can be read from a face (identity, expression, speech, and so on).
2. It was **ahead of its time** in identifying the main processes and structures involved in face processing.
3. It made an excellent attempt to specify how processing of **familiar and unfamiliar** faces differs.

**Limitations.**

1. The idea that **expression is processed separately from identity** is oversimplified and often wrong.
2. **Expression analysis** is much more complex than the model assumed (emotion-specific deficits).
3. **Gaze perception** was wrongly left out, as Young and Bruce (2011) admitted. Gaze is very informative; for example, it tells us what another person is attending to.
4. The assumption that the **name** is always accessed **after** personal information may be too rigid.

### Individual differences: super-recognisers

Bruce and Young described general processes. A lot can also be learned from **individual differences**, as prosopagnosia already shows. At the other end of the scale, **Russell et al. (2009)** studied **four "super-recognisers"** with exceptionally good face recognition. They performed at a very high level on several face tasks, for example recognising famous people from photographs taken **many years before** they became famous.

What makes them so good? Russell et al. (2012) noted that face recognition depends **more** than object recognition on **surface reflectance** information (how a surface reflects and transmits light: skin tone, texture) and **less** on **shape**. Perhaps super-recognisers are especially good at using reflectance. In fact they were simply **better than other people at using both** reflectance and shape information.

**Genetics.** **Wilmer et al. (2010)** compared face recognition in **monozygotic** (identical) twins, who share **100%** of their genes, and **dizygotic** (fraternal) twins, who share about **50%**. Identical twins' scores were **much more similar** than fraternal twins', so face-recognition ability is partly **genetic**. The chapter summary adds that these genetic factors are **specific to faces**, which is part of why super-recognisers exist.

---

## 3.6 Visual Imagery

### Imagery as experience and as representation

Close your eyes and picture the face of someone close to you. Many people describe this as seeing with the mind's eye, which already assumes that imagery and perception are alike. Imagery is usually thought of as an **experience**, which ties it closely to **consciousness**. But it can also be treated as a **mental representation**, an internal symbol standing for some aspect of the outside world (e.g., Pylyshyn, 2002), and a representation need not be conscious. Despite its importance, whether imagery **necessarily** involves consciousness has received surprisingly little direct research (Thomas, 2009).

### If imagery is like seeing, why don't we confuse them?

Sometimes people **do** confuse them. Hallucinations are experiences of seeing in the absence of the relevant stimulus, and two clinical syndromes show the boundary between imagery and perception breaking down.

**Anton's syndrome** ("blindness denial"). Some blind people are **unaware that they are blind** and may take their visual imagery for real perception.

- **Goldenberg et al. (1995)** described a patient with almost all of **primary visual cortex destroyed** who nevertheless produced visual images vivid enough to be **mistaken for actual seeing**.
- For contrast, **Bridge et al. (2012)** studied **SBR**, a young man who also had **virtually no primary visual cortex** but did **not** have Anton's syndrome. He had **vivid imagery**, and his pattern of cortical activation during imagery was **very similar to that of healthy controls**. So imagery can be vivid and normal-looking in the brain without V1, and without any confusion with perception.

**Charles Bonnet syndrome.** Yacoub and Ferrucci (2011) define it as recurring or persistent **complex visual hallucinations** in people who are **visually impaired** but otherwise **cognitively intact**. One patient reported by Santhouse et al. (2000) described seeing heads of seventeenth-century men and women with elaborate hair (probably wigs), all of whom looked disapproving. Most patients, though not all, **know the hallucinations are not real**, so strictly speaking they are **pseudo-hallucinations**.

What happens in the brain?

- During hallucinations, patients show **increased activity in visual areas specialised for the relevant content** (ffytche et al., 1998). Hallucinations **in colour** went with increased activity in **colour-processing** areas.
- **Kazui et al. (2009)** proposed a mechanism. In normal perception, **bottom-up** input **inhibits** activity in parts of visual cortex (e.g., **BA37**). In Charles Bonnet syndrome the bottom-up input is impoverished by eye disease, so that inhibition is lifted and those areas become **spontaneously active**, producing hallucinations.

> **Trap.** **Anton's syndrome** = **cortical** blindness (V1 destroyed) with **denial** of blindness; imagery is mistaken for seeing. **Charles Bonnet syndrome** = **eye disease** (visual impairment) with **complex hallucinations** in a cognitively intact person, who usually **knows** they are not real (pseudo-hallucinations). The two differ in the cause of blindness (cortex versus eye) and in insight (absent versus usually present). **SBR** (Bridge et al., 2012) has almost no V1 but **no** Anton's syndrome and **normal-looking** imagery activation.

**How healthy people keep imagery and perception apart.** Anyone without eye disease who regularly hallucinated would not remain free for long, the book notes drily. Two things normally prevent confusion:

1. We usually **know we are deliberately constructing** an image, whereas perception just happens to us.
2. Images contain **much less detail** than percepts. **Harvey (1986)** found that people rated their images of faces as resembling photographs whose edges and borders had been **blurred** (sharpness removed).

### Why is visual imagery useful?

Moulton and Kosslyn (2009) argue that imagery lets us answer **"what if" questions**: it makes explicit the likely consequences of being in a certain situation or carrying out a certain action. A driver can imagine whether a manoeuvre will fit the gap before trying it; a top golfer can imagine how a particular shot will play out before hitting it. Imagery is a **simulation** tool.

### Imagery theories

#### Kosslyn's perceptual anticipation theory

**Kosslyn** (e.g., 1994, 2005) proposed a highly influential theory built on the assumption that **imagery resembles perception**. It is called **perceptual anticipation theory** because the mechanisms that generate images are the ones used to **anticipate** perceiving a stimulus.

Its main claims:

1. **Images are depictive representations.** Like pictures or drawings, they arrange objects and their parts **in space**. Information within an image is organised spatially, just as in a percept. An image of a desk with a computer on top and a cat asleep underneath has the computer at the **top** of the image and the cat at the **bottom**.
2. **Depictive representations are formed in early visual cortex.** Kosslyn located them in **primary visual cortex (BA17)** and **secondary visual cortex (BA18)**, in a **visual buffer**: a short-term store for visual information only. The same buffer is used in **perception** as well as in **imagery**.
3. **An attention window** selects part of the visual buffer and sends that information on to other brain areas for further processing.
4. **The sources differ.** In perception, the contents of the visual buffer come mainly from **external stimulation**. In imagery, they are generated from **non-pictorial** information in **long-term memory**: knowledge of **shapes** is stored in the **inferior temporal lobe**, and **spatial** representations in **posterior parietal cortex** (Figure 3.17, after Kosslyn & Thompson, 2003).
5. So, broadly, **perception is mostly bottom-up** and **imagery is top-down**.

| Component (Kosslyn) | Location | Role |
|---|---|---|
| **Visual buffer** | Early visual cortex, **BA17 and BA18** | Short-term visual store holding the depictive image (used in perception too) |
| **Attention window** | Operates on the buffer | Selects part of the buffer for further processing |
| **Shape memory** | **Inferior temporal lobe** | Non-pictorial long-term knowledge of object shapes |
| **Spatial memory** | **Posterior parietal cortex** | Long-term spatial representations |

#### Pylyshyn's propositional theory

**Pylyshyn** (e.g., 2002) argued that imagery is **much less like perception** than Kosslyn claimed. In his **propositional theory**, performance on imagery tasks does **not** use depictive or pictorial representations. It uses **tacit knowledge**: knowledge that is not accessible to consciousness. For Pylyshyn (2002), this is knowledge of what things would look like to people in the situations they are asked to imagine. When given an imagery task, then, participants draw on stored knowledge about the world rather than on anything picture-like.

Two features of the theory matter for evaluating it. First, Pylyshyn has not spelled out the nature of this tacit knowledge very explicitly, so the theory is hard to test precisely. Second, nothing in it gives any reason why **early visual cortex** should be active when people form images. That makes early visual cortex activation during imagery the key battleground.

> **Trap.** **Kosslyn**: imagery is **depictive** (picture-like, spatially organised), held in a **visual buffer in BA17 and BA18**, generated top-down from long-term memory; name = **perceptual anticipation theory**. **Pylyshyn**: imagery is **propositional** (description-like), performance reflects **tacit knowledge**, and there is no reason for early visual cortex to be involved (classic background: older texts describe Pylyshyn as treating the picture-like experience as **epiphenomenal**, a by-product that does no work). Swapping the two names, or calling Kosslyn's theory "propositional", is the standard trap. Note too that the visual buffer is a **short-term** store; the shape and spatial knowledge from which images are built is in **long-term** memory elsewhere (inferior temporal and posterior parietal).

#### Classic background: the imagery debate experiments

> **Classic background:** two older experiments are the usual exam entry point to the Kosslyn versus Pylyshyn "imagery debate", though the 7th edition does not describe them. In **mental rotation** (Shepard & Metzler, 1971), people judged whether two drawings of block figures showed the same object; the time taken increased **linearly with the angle** between them, as if one figure were being rotated in the mind at a steady rate. In **mental scanning** (Kosslyn, Ball & Reiser, 1978), people memorised a map of an island and then scanned mentally from one landmark to another; scanning time increased **linearly with the distance** between landmarks. Kosslyn took both as evidence that images preserve spatial properties (depictive representation). Pylyshyn replied that participants know, tacitly, that moving further or rotating more takes longer in the real world, and simply produce response times consistent with that knowledge, so the results reflect **tacit knowledge**, not a picture in the head. That reply is why the debate moved to brain evidence, which is where the 7th edition picks it up.

### Imagery resembles perception

If perception and imagery share processes, they should affect one another: **facilitation** when perception and imagery have the **same** content, **interference** when they differ.

**Facilitation: Pearson et al. (2008).** They used **binocular rivalry**, in which two different stimuli go one to each eye and only one is seen at any moment, alternating over time. If one of the two stimuli is shown on its own shortly beforehand, it is more likely to dominate when rivalry begins. Pearson et al. found this when observers first **perceived** a **green vertical** or **red horizontal** grating. The boost was greatest when the rivalry grating had the **same orientation** as the earlier one and smallest when the orientations differed a lot. Crucially, when the earlier grating was **imagined** rather than seen, the pattern of facilitation was **remarkably similar**. An image primed perception in the same way, and with the same orientation tuning, as a real stimulus.

**Interference: Baddeley and Andrade (2000).** Participants rated the **vividness** of **visual** or **auditory** images either with no other task or while doing a second task. The second task was either **visual/spatial** or **verbal** (counting aloud repeatedly from **1 to 10**). Visual images lost more vividness than auditory images when the concurrent task was visual/spatial, because that task competes for the **same mechanisms** that visual imagery uses.

**Early visual cortex in imagery.** According to Kosslyn (1994, 2005), much of the processing in visual imagery takes place in **early visual cortex (BA17 and BA18)**, though other areas are involved too. **Kosslyn and Thompson (2003)** surveyed many neuroimaging studies and found early visual cortex activation during imagery in **about half** of them. Activation was most often found when:

1. the task required inspecting **fine details** of the image;
2. the task concerned an object's **shape** rather than an object in motion;
3. **sensitive** imaging techniques were used.

**Overlap in brain activation.** **Ganis et al. (2004)** compared activation patterns for perception and imagery and found:

1. **Extensive overlap**, especially in **frontal and parietal** areas, perhaps because perception and imagery share **control** processes.
2. But imagery activated only **some** of the areas involved in perception. **Kosslyn (2005)** estimated that imagery tasks activate about **two-thirds** of the brain areas that perception activates.

### Imagery does not resemble perception

**Slezak's ambiguous figures.** Figure 3.18 shows outlines of three objects. If you form an image of one, close your eyes, mentally rotate it by **90 degrees clockwise** and ask what you now see, you will probably see nothing new. If you rotate the actual page, a different object jumps out. **Slezak (1991, 1995)** used very similar stimuli: **no** observer reported seeing the new objects in their rotated images. This was not a memory failure, because participants who **sketched** the image from memory and then rotated the **sketch** did see the new object. Information in an image cannot be **reinterpreted** as flexibly as information in a percept, which fits Pylyshyn's view better than Kosslyn's.

**Decoding imagined objects from brain activity: S.-H. Lee et al. (2012).** Participants either **viewed** or **imagined** common objects (a car, an umbrella and so on) while activity was measured in **early visual cortex** and in **object-selective** regions further along the ventral stream (the lateral occipital cortex and posterior fusiform sulcus; Figure 3.19). The researchers then tried to work out from the activation patterns which object was being perceived or imagined.

1. Activation in **every** region was **considerably greater** for perceived than for imagined objects.
2. Perceived and imagined objects could be identified at **above-chance** accuracy from activation patterns, **except imagined objects in primary visual cortex (V1)**.
3. For **perceived** objects, identification was **more successful from early visual areas** than from later ones. For **imagined** objects, it was the **reverse**: more successful from **later, object-selective** areas.

The conclusion is an important difference between imagery and perception. Early visual cortex is **crucial in perception** but plays only a **limited** role in **object imagery**, which depends mostly on **top-down** processes using **object knowledge**.

> **Trap.** Lee et al. (2012) is the 7th edition's main neuroimaging evidence **against** a strong Kosslyn view: imagined objects could **not** be decoded from **V1**, and imagery was decoded best from **later** object-selective areas, the opposite of perception. Do not confuse it with Pearson et al. (2008), which **supports** Kosslyn (imagery primes binocular rivalry like perception does).

### Brain damage

If perception and imagery used the same mechanisms, brain damage should affect both in the same way. Often it does, but there are many exceptions (Bartolomeo, 2002, 2008), and they run in **both directions**.

**Intact perception, impaired imagery.** **Moro et al. (2008)** described **two** patients whose brain damage had left **visual perception intact** while **visual imagery** was impaired. Both were very poor at **drawing objects from memory**, yet could **copy** the same objects when shown a drawing. These patients, and others with the same pattern, have damage to the **left temporal lobe**. Visual images are probably generated from conceptual knowledge, including knowledge about objects, stored in the **temporal lobes** (Patterson et al., 2007), and this generation process is not needed, or matters less, for perception.

**Intact imagery, impaired perception.** These patients typically have severe damage to **primary visual cortex**: **SBR** (Bridge et al., 2012), the Anton's syndrome patient of **Goldenberg et al. (1995)**, and another Anton's syndrome patient with **total** V1 damage reported by **Zago et al. (2010)**.

**Interpretation.** Perception is driven mainly **bottom-up** by the stimulus; imagery is driven mainly **top-down** from object knowledge. It is therefore unsurprising that **early visual areas** matter more for **perception**, and that areas storing **knowledge about objects** matter more for **imagery**.

| Pattern | Lesion | Example | Interpretation |
|---|---|---|---|
| Perception intact, imagery impaired | **Left temporal lobe** | Moro et al. (2008): two patients who copy well but cannot draw from memory | Image generation from stored concepts (Patterson et al., 2007) is damaged |
| Imagery intact, perception impaired | **Primary visual cortex** | SBR (Bridge et al., 2012); Goldenberg et al. (1995); Zago et al. (2010) | Bottom-up input is lost; top-down image generation survives |

> **Trap.** The two patient patterns form a **double dissociation** between imagery and perception, and the lesion sites go the **opposite** way to what a strong Kosslyn view predicts. If images lived in V1, V1 destruction should abolish imagery; instead SBR and the Anton's patients keep vivid imagery. Imagery loss goes with **left temporal** damage, not occipital damage. A common wrong option says "imagery deficits follow V1 damage".

### Evaluation

**Strengths of the "imagery resembles perception" position.** Much has been learned about the relationship between imagery and perception, and there is **strong evidence** that they share processes. They produce somewhat similar patterns of brain activity (Ganis et al., 2004; Kosslyn & Thompson, 2003), and the predicted **facilitation** (Pearson et al., 2008) and **interference** (Baddeley & Andrade, 2000) between imagery and perception tasks have been found. These findings fit **Kosslyn's theory better than Pylyshyn's**.

**Limitations.** Imagery and perception are **less similar** than Kosslyn assumed. The neuroimaging evidence of **S.-H. Lee et al. (2012)** and the frequent **dissociations** in brain-damaged patients show that. What is needed is a theory that explains the **differences** as well as the similarities. One piece of that theory is already clear: **bottom-up** processes dominate perception and **top-down** processes dominate imagery.

> **Trap.** "Who won the imagery debate?" Older keys tend to say Kosslyn, citing mental rotation, mental scanning and early visual cortex activation. The 7th-edition answer is more careful: the evidence is **more consistent with Kosslyn than with Pylyshyn** (overlap, facilitation, interference), but imagery is **less like perception** than Kosslyn claimed (Slezak's failed reinterpretation; Lee et al., 2012; double dissociations), because imagery relies far more on **top-down** object knowledge and far less on early visual cortex.

---

## How the chapter fits together

1. **Bottom-up versus top-down is the spine of the chapter.** Feature detectors (Hubel & Wiesel), Marr's stages and Biederman's geons are bottom-up accounts. Each section then finds top-down influence the older theory left out: context in fingerprint matching (Dror et al., 2006), familiarity in figure-ground assignment (Barense et al., 2012), orbitofrontal predictions before recognition (Bar et al., 2006), prefrontal rTMS effects on blurred objects (Viggiano et al., 2008), labels changing detection (Lupyan & Ward, 2013). Imagery is the limiting case: perception driven almost entirely from the top.
2. **Top-down effects grow when input is poor.** Blurred, masked, brief, degraded or suppressed stimuli are where expectation matters most. The same rule explains why fingerprint errors cluster on smudged latent prints and why Charles Bonnet hallucinations appear when eye disease starves the cortex of input.
3. **Coarse before fine, but flexibly.** Navon's global precedence, low spatial frequencies travelling on the fast magnocellular route, Musel et al.'s coarse-to-fine advantage and the Mona Lisa's peripheral smile are one idea. Flevaris et al. (2014) and Dalrymple et al. (2009) show the order can change with the task and the stimulus.
4. **Learning gets into processes once thought innate or fixed.** Gestalt grouping (Bhatt & Quinn, 2011), figure-ground (Barense et al., 2012), viewpoint invariance (Zimmermann & Eimer, 2013; Tarr & Bülthoff, 1995), holistic processing of non-face categories (the expertise hypothesis) and the gap between familiar and unfamiliar faces (Jenkins et al., 2011) all depend on experience.
5. **The task decides the answer.** Recognition is viewpoint-invariant for categorisation and viewer-centred for identification. Identity and expression look independent in an OR task and interact in an AND task. Figure-ground needs attention for complex displays but not for simple ones.
6. **Dissociations carry the theoretical weight.** GG and PS versus CK give a double dissociation between faces and objects. Moro et al.'s left-temporal patients versus SBR and the Anton's patients give a double dissociation between imagery and perception. Edward separates face detection from identification. In each case the controls (matched difficulty, reaction times as well as accuracy, sham rTMS, an amnesic group) are what make the conclusion stick.
7. **Networks, not centres.** The FFA turns out to be one node in a network with the OFA and anterior patches; Jennifer Aniston is coded by a small population, not one cell; imagery shares only about two-thirds of perception's areas. The 7th edition consistently replaces a single dedicated module with interacting systems.

---

## Worked example

*Mrs R, a 58-year-old retired schoolteacher, had a right-hemisphere occipitotemporal stroke. At her granddaughter's wedding three months later she walked straight past her own son, warmly greeted a stranger whose beard and turban resembled her brother's, and knew her husband only when he spoke to her. She names everyday objects without difficulty, reads normally and can still tell her neighbours' cars apart. When shown photographs of family members she sometimes says "I know this person, but I can't think who it is." Her 30-year-old daughter, who has had no neurological illness, says she has "always been hopeless with faces" and recognises colleagues by their walk. A trainee suggests that Mrs R's problem is simply that faces are harder to tell apart than objects, and that the daughter is "just not paying attention".*

**What is the most likely diagnosis, and does the daughter have the same thing?** Mrs R's pattern (severe face recognition failure, normal object naming and reading, onset after a stroke) is **acquired prosopagnosia**. Her daughter's lifelong difficulty with no brain injury fits **developmental prosopagnosia**, the form Heather Sellers has. Up to 2% of people may be affected, and like Sellers they often go undiagnosed for years because they compensate with hair, clothing, voice and gait. The daughter's reliance on gait is exactly that compensation, not inattention.

**Is the trainee right that faces are just harder?** This is the difficulty explanation, and it can be tested rather than assumed. Following **Busigny et al. (2010a, 2010b)**, give Mrs R object tasks with within-category items (cars, chairs, birds) whose **target-distractor similarity is varied**, and record **reaction times** as well as accuracy. If her errors rise with similarity exactly as controls' do, and she is not buying accuracy by going slowly, while she fails even easy face tasks, the impairment is face-specific (as for GG: 67% versus 94% on faces, normal on objects). Her intact car discrimination is already a hint in that direction.

**What is the underlying deficit likely to be?** Test for **holistic processing**. If Mrs R shows **no face inversion effect** and **no composite face effect**, as GG did, she has lost configural processing of faces. A restricted-viewing test of the **Van Belle et al. (2011)** type, where only one feature is visible at a time, should bring her close to controls, because it removes the holistic advantage that she no longer has.

**Where does the breakdown sit in Bruce and Young's model?** Work along the pathway. She **detects** faces (she knows a person is in front of her), so the face detection stage that Duchaine and Nakayama added is intact, as it was for Edward. Saying "I know this person but can't think who" on some photographs suggests that some **face recognition unit** activation survives but fails to reach the **person identity node**; Young et al.'s (1985) diary contained 233 such familiarity-only incidents in healthy people, so this is a recognised state, just pathologically frequent in her. Recognising her husband from his **voice** shows that the person identity nodes and name retrieval themselves are intact; the problem lies on the face route into them. Expression should be checked separately: if she reads emotions normally, her damage spares the STS route (Fox et al., 2011), but remember the 7th-edition caution that identity and expression are not fully independent.

**Could she recognise faces without knowing it?** Possibly. **Covert recognition** is common in prosopagnosia: in Simon et al. (2011), patient PS showed more fusiform face area activation for familiar than unfamiliar faces while denying any recognition. Covert familiarity is one reason why some patients feel uneasy or "warm" towards people they cannot name.

**What should the team expect from imaging?** Damage to the **fusiform face area**, the **occipital face area**, or both. The trainee should not assume that an intact FFA rules out prosopagnosia: Gainotti and Marra (2011) argue that face processing depends on a network including the OFA, and the FFA is not face-specific in every individual (only 80% in Kanwisher et al., 1997).

**What can be done?** No intervention in the chapter restores holistic processing, so management is compensatory: deliberate use of voice, gait, hairstyle and context, and asking family to say their names on arrival. Jenkins et al. (2011) adds a practical point: single photographs of a person vary so much that they are poor training material, and Jenkins and Burton (2011) found that **averaged images** support better identification than single ones, which is a reasonable idea (an inference, not a tested therapy) for building a family photo set.

---

## MCQ traps

1. **Navon (1977)**: large letter interferes with small-letter judgements, not vice versa = **global precedence**; **Dalrymple et al. (2009)** reversed it with larger, spaced-out small letters.
2. **Simple cells** = orientation, separate rectangular on/off zones; **complex cells** = larger fields, prefer **moving** contours, built from simple cells (Alonso & Martinez, 1998); **end-stopped** = length-sensitive.
3. **FBI AFIS**: over **60 million** prints; three general patterns **loop, arch, whorl**; **minutiae** = ridge endings and splits.
4. **Madrid bombing, 11 March 2004**: four experts matched the print to **Brandon Mayfield** (innocent); the bomber was **Ouhane Daoud**.
5. **Cole (2005)**: **22** misidentifications, over **half** confirmed by further experts; **Dror et al. (2012)**: same expert, same minutiae only **16%** of the time.
6. **Dror et al. (2006)**: misleading Madrid context made **60%** of experts call their own earlier definite match a **non-match**.
7. **Thompson et al. (2014)**: hits about **70%** for both groups; false alarms **57%** novices versus **1.65%** experts: better **discrimination** and **more conservative** bias.
8. **Law of Prägnanz** = simplest organisation; Gestaltists = **Koffka, Köhler, Wertheimer**.
9. **Uniform connectedness** = **Palmer and Rock (1994)**, not the Gestaltists; it beat proximity and similarity; Han and Humphreys (2003): faster than proximity only with **several** objects.
10. **Elder and Goldberg (2002)**: **proximity** strongest in natural contours; similarity and good continuation small.
11. **Bhatt and Quinn (2011)**: infants **3 to 4 months** group by good continuation, proximity, connectedness; **closure** later.
12. **Barense et al. (2012)**: **amnesic** patients lose the familiarity advantage in figure assignment, so figure-ground is **not entirely innate**.
13. **Low** spatial frequency = coarse = **magnocellular** = fast; **high** = fine = **parvocellular** = slower; **Musel et al. (2012)**: **150 ms** scenes, coarse-to-fine faster.
14. **Marr (1982)**: primal sketch, **2½-D sketch (still viewer-centred)**, 3-D model (**object-centred**).
15. **Biederman (1987)**: about **36 geons** (compare about **44 phonemes**); cup versus pail = same geons, different relations.
16. Five invariant properties: **curvature, parallel, cotermination, symmetry, collinearity**; parts are parsed at **concavities** (Leek et al., 2012: eye movements to internal concavities).
17. **Biederman and Gerhardstein (1993)**: equal priming at **135 degrees** (familiar objects); **Tarr and Bülthoff (1995)**: viewpoint-dependent with **novel** objects.
18. **Sanocki et al. (1998)**: line drawings much worse than **colour photographs**, especially **in context**, against RBC's edge emphasis.
19. **Hamm and McMullen (1998)**: viewpoint irrelevant for **car** (categorisation), matters for **taxi** (identification).
20. **Milivojevic et al. (2011)**: little orientation effect on RT but large effects on early **ERPs**; **Zimmermann and Eimer (2013)**: **640** trials, faces become view-invariant with learning.
21. Binocular rivalry: about **20%** of **V1** neurons versus about **90%** in **IT and STS** track the percept (Leopold & Logothetis, 1999; Blake & Logothetis, 2002).
22. **Afraz et al. (2006)**: microstimulating face-selective IT neurons in **two** macaques increased **face** decisions (causal).
23. **Booth and Rolls (1998)**: **49%** view-specific, **14%** view-invariant (STS); **Zoccolan et al. (2007)**: selectivity and tolerance **negatively** correlated.
24. **Quiroga et al. (2005)**: human **medial temporal lobe** "Jennifer Aniston" neuron, silent for Aniston with **Brad Pitt**; coding is sparse (thousands or fewer), not one cell.
25. **Bar et al. (2006)**: orbitofrontal activity **50 ms before** temporal recognition areas, more so when recognition is hard; **Viggiano et al. (2008)**: rTMS to left or right **DLPFC** slows recognition of **blurred** images only.
26. **Lupyan and Ward (2013)**: valid verbal cues improve **detection sensitivity** for suppressed shapes, so the effect is perceptual, not just a response bias.
27. **Farah (1994)** part-whole: faces yes, **houses no**; **Richler et al. (2011)**: composite effect, and stronger holistic processors recognise faces better.
28. **GG (Busigny et al., 2010b)**: faces **67% versus 94%**, normal on birds, boats, cars, chairs; no inversion or composite effects; **Van Belle et al. (2011)**: normal with one feature visible at a time.
29. **CK (Moscovitch et al., 1997)**: object agnosia, **normal faces** (photographs, caricatures, cartoons) only if **upright** with features in place.
30. **Kanwisher et al. (1997)**: only **80%** show the FFA face preference; **Downing et al. (2006)**: faces beat **18** object categories and scenes; **OFA** damage common (Gainotti & Marra, 2011).
31. **Expertise hypothesis (Gauthier & Tarr, 2002)** = "fusiform expertise area"; **Crookes and McKone (2009)**: adult-level holistic processing by **age 7 or less** (against prediction 3); **McKeeff et al. (2010)**: car experts slowed searching for faces among **cars**, not watches.
32. **Jenkins et al. (2011)**: **40** photos of **2** Dutch celebrities sorted into **7.5** piles by British participants; Dutch participants nearly perfect; attractiveness varies more **within** than between people.
33. **Young et al. (1985)**: **1,008** incidents; never name without other information; **190** information without name; **233** familiarity only; **Calderwood and Burton (2006)**: *Friends* names faster than occupations.
34. **Schweinberger and Soukup (1998)**: identity affects expression judgements, **not** the reverse; **Fitousi and Wenger (2013)**: independence in the **OR** task only; amygdala damage hits **fear and anger** (Calder & Young, 2005).
35. Bruce and Young's admitted omission = **gaze** perception; Duchaine and Nakayama's addition = **face detection** (patient **Edward**).
36. Super-recognisers: **Russell et al. (2009)**, **four** people; better at **both** reflectance and shape (Russell et al., 2012); **Wilmer et al. (2010)**: MZ more similar than DZ.
37. **Kosslyn**: perceptual anticipation theory, **depictive** images, **visual buffer in BA17/BA18**, shapes in **inferior temporal**, space in **posterior parietal**; **Pylyshyn**: propositional, **tacit knowledge**.
38. **Anton's syndrome** = cortical blindness with denial (Goldenberg et al., 1995; Zago et al., 2010); **Charles Bonnet** = eye disease, complex hallucinations, usually with insight; **SBR** (Bridge et al., 2012) = no V1, normal imagery, no Anton's.
39. **Kosslyn and Thompson (2003)**: early visual cortex active in **about half** of imagery studies; **Kosslyn (2005)**: imagery uses about **two-thirds** of perception's areas; **Ganis et al. (2004)**: overlap greatest in **frontal and parietal** areas.
40. **Slezak (1991, 1995)**: nobody saw the new object after mental rotation by **90 degrees**, but sketching then rotating worked; **Lee et al. (2012)**: imagined objects **not decodable from V1**.
41. **Moro et al. (2008)**: two patients, imagery impaired, perception intact, **left temporal** damage (copy fine, draw from memory poor); imagery spared with **V1** damage.

---

## Key terms

| Term | Definition |
|---|---|
| **Pattern recognition** | Identifying or categorising two-dimensional patterns such as letters, digits or fingerprints |
| **Template theory** (classic background) | Recognition by matching the input against stored exact copies; fails because every size, slant and style would need its own template |
| **Feature theory** | Recognition by detecting a pattern's component features (lines, angles, curves), which survive changes of size and orientation |
| **Global precedence** | The tendency to process the overall shape before local detail (Navon, 1977) |
| **Simple / complex / end-stopped cells** | V1 neurons tuned to oriented bars and edges (simple), to oriented and often moving contours over larger fields (complex), and to line length (end-stopped) |
| **Spatial frequency** | How rapidly light and dark alternate in an image; low frequencies carry coarse layout, high frequencies fine detail |
| **Coarse-to-fine processing** | The usual sequence in which a rough analysis of a scene precedes detailed analysis |
| **AFIS** | Automatic fingerprint identification system that ranks database prints by similarity to a crime-scene print |
| **Minutiae** | Points on a fingerprint where a friction ridge ends or splits |
| **Forensic confirmation bias** | Distortion of how forensic evidence is gathered, perceived and interpreted by prior beliefs, expectations and context |
| **False-alarm rate** | Proportion of non-matching (noise) trials on which a "match" (signal) response is given; separates discrimination from bias |
| **Law of Prägnanz** | Gestalt principle that the simplest available organisation of the visual field is the one perceived |
| **Proximity / similarity / good continuation / closure** | Gestalt grouping laws: near elements group; alike elements group; elements forming smooth lines group; gaps are filled to complete figures |
| **Figure-ground segregation** | Organisation of the visual field into a shaped object in front (figure) and a shapeless background (ground) |
| **Uniform connectedness** | A connected region with uniform colour, texture or lightness is perceived as one unit (Palmer & Rock, 1994) |
| **Generalised common fate** | Grouping of elements that change together, for example brightening or darkening at the same time |
| **Border-ownership neurons** | Early visual cortex cells whose responses signal which side of an edge belongs to the figure |
| **Bayesian approach** | Treating perception as the most probable interpretation, combining fit to the image with prior knowledge of scene statistics |
| **Primal sketch** | Marr's first stage: a 2-D description of intensity changes such as edges, contours and blobs |
| **2½-D sketch** | Marr's viewer-centred description of the depth and orientation of visible surfaces |
| **3-D model representation** | Marr's object-centred, viewpoint-invariant description of objects' 3-D shapes and arrangement |
| **Recognition-by-components** | Biederman's theory that objects are recognised from their component geons and the relations between them |
| **Geons** | About 36 basic 3-D shapes (cylinders, blocks, wedges, arcs and so on) from which object descriptions are built |
| **Non-accidental principle** | The assumption that regularities in the image (symmetry, straightness) reflect real regularities in the object, not the viewpoint |
| **Invariant properties** | Edge properties that survive viewpoint change: curvature, parallelism, cotermination, symmetry, collinearity |
| **Viewpoint-invariant** | Recognition equally easy from any viewing angle (object-centred) |
| **Viewer-centred (viewpoint-dependent)** | Recognition easier from some angles, typically the familiar or canonical view |
| **Canonical view** | The typical, most informative view of an object (a bicycle side-on) |
| **Categorisation versus identification** | Deciding the kind of object (a car) versus a within-category discrimination (a taxi) |
| **Selectivity** | A neuron's tendency to respond to one object and not others |
| **Invariance (tolerance)** | A neuron's tendency to respond to an object regardless of its size, position or orientation |
| **Binocular rivalry** | Different images to the two eyes produce alternating awareness of one image at a time |
| **Top-down processing** | Processing guided by knowledge, expectation and context rather than by the stimulus alone |
| **rTMS** | Repetitive transcranial magnetic stimulation; brief magnetic pulses that temporarily disrupt a cortical area |
| **Apperceptive / associative agnosia** (classic background) | Object recognition failure from defective perception of form (cannot copy) / from failure to link an adequate percept to meaning (can copy) |
| **Object agnosia** | Impaired recognition of objects not explained by basic sensory loss (patient CK) |
| **Holistic processing** | Processing a whole object, especially a face, as an integrated configuration including the relations among its parts |
| **Face inversion effect** | Faces are much harder to recognise upside down; the cost is smaller or absent for most other objects |
| **Part-whole effect** | A face part is recognised better inside a whole face than on its own |
| **Composite face effect** | Difficulty judging one half of a face when it is aligned with a different other half |
| **Prosopagnosia** | Severe impairment of face recognition with much less impairment of object recognition; face blindness |
| **Acquired versus developmental prosopagnosia** | Face blindness caused by brain damage versus face blindness with no obvious brain damage, usually lifelong |
| **Covert recognition** | Evidence of processing familiar faces (for example extra FFA activation) without conscious recognition |
| **Fusiform face area (FFA)** | Ventral temporal region more active for faces than other objects in most people, but also responsive to other categories |
| **Occipital face area (OFA)** | Face-selective region in occipital cortex, part of the face network and often damaged in prosopagnosia |
| **Expertise hypothesis** | Gauthier and Tarr's claim that "face-specific" mechanisms serve any category in which we are expert |
| **Face recognition units** | Bruce and Young's stores of abstract structural descriptions of known faces; their activation produces familiarity |
| **Person identity nodes** | Bruce and Young's stores of biographical knowledge about known people |
| **Super-recognisers** | People with exceptionally good face recognition (Russell et al., 2009) |
| **Surface reflectance** | How a surface reflects and transmits light (skin tone, texture), used more for faces than for objects |
| **Perceptual anticipation theory** | Kosslyn's theory that images are generated by the mechanisms used to anticipate perceiving, in shared visual areas |
| **Depictive representations** | Picture-like representations in which objects and parts are arranged spatially |
| **Visual buffer** | Kosslyn's short-term visual store in early visual cortex (BA17, BA18), used in both imagery and perception |
| **Attention window** | In Kosslyn's theory, the selector that passes part of the visual buffer on for further processing |
| **Propositional theory** | Pylyshyn's view that imagery tasks use description-like knowledge, not pictures |
| **Tacit knowledge** | Knowledge not available to awareness, here of how things would look in imagined situations |
| **Anton's syndrome** | Cortically blind patients who deny their blindness and take visual images for perception |
| **Charles Bonnet syndrome** | Vivid, complex visual hallucinations in visually impaired but cognitively intact people, usually recognised as unreal |
| **Pseudo-hallucination** | A hallucination that the person recognises as not real |

---

## Likely exam points

1. The three reasons object recognition is hard (overlap, category variability, orientation) and the pattern versus object recognition distinction.
2. Template versus feature theories; why templates fail; Navon (1977) global precedence and its limits (Dalrymple et al., 2009).
3. Hubel and Wiesel's simple, complex and end-stopped cells, and why single feature detectors are ambiguous.
4. Fingerprinting: AFIS, minutiae, the Madrid error, Cole (2005), Dror et al. (2006, 2012), and the signal-detection analysis of Thompson et al. (2014).
5. Forensic confirmation bias as a top-down effect on expert perception.
6. The Gestalt laws (Prägnanz, proximity, similarity, good continuation, closure) with diagrams.
7. Figure-ground segregation: the three Gestalt claims and the cues (convex, small, surrounded, symmetrical).
8. Modern tests of Gestalt claims: Geisler et al. (2001), Elder and Goldberg (2002), Bhatt and Quinn (2011), Vecera et al. (2004), Barense et al. (2012).
9. Uniform connectedness (Palmer & Rock, 1994) and generalised common fate as principles the Gestaltists missed.
10. Evaluation of the Gestalt approach: three strengths, five limitations, and the Bayesian alternative.
11. Spatial frequency, magnocellular versus parvocellular routes, coarse-to-fine processing (Musel et al., 2012) and its flexibility (Flevaris et al., 2014).
12. Livingstone's (2000) Mona Lisa explanation.
13. The ventral stream hierarchy and the dorsal stream's contribution (Thoma & Henson, 2011; Farivar, 2009).
14. Marr's three representations, which are viewer-centred, and the two main criticisms.
15. Biederman's RBC: geons, the five invariant properties, concavities, the non-accidental principle and recognition under degraded conditions.
16. Evidence for and against RBC: Vogels et al. (2001), Biederman and Gerhardstein (1993), Tarr and Bülthoff (1995), Sanocki et al. (1998); four limitations.
17. The viewpoint debate resolved by categorisation versus identification (Milivojevic, 2012; Hamm & McMullen, 1998); ERP evidence (Milivojevic et al., 2011); Hayward's (2012) viewer-centred conclusion.
18. IT cortex: binocular rivalry percentages, Afraz et al.'s causal evidence, selectivity versus invariance, Booth and Rolls, Zoccolan et al.
19. The Jennifer Aniston neuron and why it does not support grandmother cells.
20. Top-down processes in recognition: Bar et al. (2006) model, Viggiano et al. (2008) rTMS, Lupyan and Ward (2013).
21. Holistic processing in faces: inversion, part-whole and composite effects, and the expertise complications.
22. Prosopagnosia: acquired versus developmental, covert recognition, Heather Sellers, and the two explanations for face-specific deficits.
23. GG, PS and CK as a double dissociation; the holistic-processing account of prosopagnosia (Busigny et al., 2010b; Van Belle et al., 2011).
24. The FFA: evidence for its role and the 7th edition's network conclusion (OFA, AFP2, 80% figure, lenient criteria).
25. The expertise hypothesis: four predictions, the evidence for each, and the compromise verdict.
26. Bruce and Young (1986): eight components, three predictions, evidence for each, strengths and limitations (including gaze).
27. Familiar versus unfamiliar faces: Jenkins et al. (2011) and image averaging (Jenkins & Burton, 2011); implications for passports and eyewitnesses.
28. Super-recognisers and the genetic evidence (Russell et al., 2009, 2012; Wilmer et al., 2010).
29. Kosslyn's perceptual anticipation theory versus Pylyshyn's propositional theory.
30. Evidence that imagery resembles perception (Pearson et al., 2008; Baddeley & Andrade, 2000; Kosslyn & Thompson, 2003; Ganis et al., 2004).
31. Evidence that imagery differs from perception (Slezak, 1991, 1995; Lee et al., 2012).
32. Imagery-perception dissociations after brain damage (Moro et al., 2008 versus SBR and Anton's syndrome) and the bottom-up/top-down interpretation.
33. Anton's syndrome versus Charles Bonnet syndrome, and why healthy people do not confuse images with percepts.
