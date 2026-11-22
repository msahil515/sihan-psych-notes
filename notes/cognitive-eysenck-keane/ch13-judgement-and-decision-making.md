---
date: 2026-11-22
book: "Cognitive Psychology (Eysenck & Keane, 7th ed.)"
subject: Cognitive Psychology
chapter: 13
title: "Judgement and decision making"
tags: [cognitive-psychology, judgement, decision-making, heuristics-and-biases, base-rate-neglect, prospect-theory, dual-process-theory, bounded-rationality, neuroeconomics, clinical-psychology-entrance]
---

# Chapter 13: Judgement and Decision Making

**What this chapter is really about.** Chapter 12 asked how people solve problems; this chapter asks how they estimate what is likely and then choose what to do. Part IV of the book (Thinking and reasoning) treats problem solving, judgement, decision making and reasoning as different faces of one cognitive system, and its opening box separates two terms you must keep apart: **judgement** is the estimation of how likely various events are, and its yardstick is accuracy; **decision making** is the selection of one option from several, and the decision has personal consequences. Judgement usually feeds into decision making as an early stage. The chapter's running argument is about rationality. Normative theories (Bayes' theorem for judgement, expected utility theory for decisions) say how an ideal reasoner *should* proceed. Kahneman and Tversky showed, problem after problem, that people deviate from those norms in systematic, predictable ways, and they explained the deviations with **heuristics** (rules of thumb) and with **prospect theory**. Most of the rest of the chapter is the reply: Gigerenzer arguing that heuristics are often smart rather than dumb, De Neys arguing that "intuitive" people are processing more than they appear to, emotion and social researchers showing that the "errors" often have motivational and social roots, and naturalistic researchers showing how experts actually decide under time pressure.

For a clinical psychology student this is not abstract. Almost every bias in the chapter has a version in the clinic: a doctor who misses a heart attack because the patient looks healthy, an emergency physician who misdiagnoses because of the last three weeks of cases, a parent who refuses vaccination because harm from acting feels worse than harm from not acting, a patient whose choice flips depending on whether a treatment is described in terms of survival or death.

**How to read this chapter.** 13.1 fixes the definitions. 13.2 is the empirical core of judgement research (Bayes, base-rate neglect, representativeness, availability, and when base rates *are* used). 13.3 gives the theories: support theory, fast-and-frugal heuristics, natural frequencies, and the System 1 and System 2 account with De Neys's revision. 13.4 turns to risky choice and prospect theory, 13.5 adds emotion and social accountability, and 13.6 covers complex real-life and expert decisions. Keep two questions running throughout: *does this theory describe what people do or prescribe what they should do?* and *does this finding show irrationality, or an unfair task?*

---

## 13.1 Introduction

### Judgement versus decision making

The two areas overlap, but they are evaluated in different ways, and an exam can test that difference directly.

| | Judgement | Decision making |
|---|---|---|
| Core task | Estimating the probability of events from incomplete information | Choosing one option from several possibilities |
| Example | Using your past exam marks to estimate your chance of passing the next exam | Choosing which university to attend or which course to study |
| Criterion of quality | **Accuracy** | **Consequences** (are you happy with the outcome?) |
| Relation | Often an early component of decision making | Requires judgement whenever full information is unavailable |

The car-buying example shows the relation. Before you choose a car (the decision), you make a set of judgements: how much each model is likely to cost to run, how reliable each is likely to be, how much you would enjoy owning it. The decision then integrates those judgements.

Decisions also vary hugely in weight. Choosing between two soft drinks is quick and nearly effortless; choosing a career path is slow, involves many attributes, and unfolds over months. That spread is why the chapter moves from simple laboratory gambles (13.4) to complex real-life choices (13.6).

### A good decision can have a bad outcome

We normally judge decisions by their consequences, but the book warns that this is sometimes unfair. The surgeon's grim joke (the operation succeeded, the patient died) makes the point: a decision can be the right one given the information available when it was made, even if things later go badly. In clinical terms, a psychiatrist who chooses the treatment with the best evidence for a given patient has made a good decision even if that patient happens not to respond. Judging the decision by the outcome alone is called outcome bias in the wider literature.

> **Trap.** Judgement is evaluated by **accuracy**, decision making by **consequences**. Do not swap them. And "a good decision" does not mean "a decision that turned out well": quality is assessed on the information available at the time of choosing.

### The rationality question

Underneath the whole chapter is the question of what this research tells us about human rationality. The book treats that broader debate (including bounded rationality and the dual-process view of reasoning) in Chapter 14, so here the focus is on the specific findings. Remember, though, that each "bias" in this chapter is defined *relative to a normative standard*: Bayes' theorem for probability judgements, expected utility for risky choices, multi-attribute utility for complex choices. A bias is a systematic departure from that standard.

---

## 13.2 Judgement Research

### Updating beliefs: Bayes' theorem

In daily life we constantly revise how likely we think something is. Suppose you are 90% sure a friend has lied to you, and then a second person independently confirms the friend's story; your confidence that you were lied to might fall to 60%. New information strengthens or weakens beliefs all the time. The question for judgement research is whether people revise their beliefs by the *right amount*.

The Reverend **Thomas Bayes** (an eighteenth-century clergyman and mathematician) supplied the normative answer for the case of two competing hypotheses, call them H<sub>A</sub> and H<sub>B</sub> (for example, "X is lying" versus "X is not lying"). Two ingredients are needed:

1. **Prior odds**: how likely each hypothesis was *before* the new data arrived, expressed as a ratio, p(H<sub>A</sub>) / p(H<sub>B</sub>).
2. **Likelihood ratio**: how probable the observed data (D) would be if each hypothesis were true, p(D/H<sub>A</sub>) / p(D/H<sub>B</sub>). The notation p(D/H<sub>A</sub>) means "the probability of the data given that H<sub>A</sub> is true".

Bayes' theorem in its odds form then says:

**Posterior odds = prior odds × likelihood ratio**

p(H<sub>A</sub>/D) / p(H<sub>B</sub>/D) = [p(H<sub>A</sub>) / p(H<sub>B</sub>)] × [p(D/H<sub>A</sub>) / p(D/H<sub>B</sub>)]

The left side is what we want: the relative probability of the two hypotheses *after* seeing the data. The right side multiplies what we believed beforehand by how strongly the data favour one hypothesis over the other. The book reassures the reader that the formula looks harder than it is, and it does: it is one multiplication.

#### Worked through: the taxi-cab problem (Kahneman & Tversky, 1972)

The classic test case comes from **Kahneman and Tversky (1972)**. One night a cab was involved in an accident. In the city, **85%** of cabs belong to the Green company and **15%** to the Blue company. A witness said the cab was Blue. When her ability to tell the colours apart under similar night-time conditions was tested, she was wrong **20%** of the time. What is the probability the cab really was Blue?

Set it up:

| Quantity | Value | Why |
|---|---|---|
| H<sub>A</sub> | cab was Blue | |
| H<sub>B</sub> | cab was Green | |
| Prior p(H<sub>A</sub>) | 0.15 | 15% of cabs are Blue (the base rate) |
| Prior p(H<sub>B</sub>) | 0.85 | 85% are Green |
| p(D/H<sub>A</sub>) | 0.80 | she says "Blue" when it is Blue 80% of the time |
| p(D/H<sub>B</sub>) | 0.20 | she says "Blue" when it is Green 20% of the time |

Posterior odds = (0.15 / 0.85) × (0.80 / 0.20) = 0.12 / 0.17, that is **odds of 12:17** in favour of Green. Converting odds to a probability: 12 / (12 + 17) = 12/29, which is about **41%**. So, despite the eyewitness, the cab was more likely Green than Blue.

The intuition behind the number: Green cabs are so common that even a 20% misidentification rate produces many "Blue" reports about Green cabs. Out of 100 cabs, 15 are Blue and the witness correctly calls 12 of them Blue; 85 are Green and she wrongly calls 17 of them Blue. Of the 29 "Blue" reports, only 12 are genuine.

> **Trap.** Two numbers in one problem. The **odds** are 12:17; the **probability** is 12/29 = 41%. An option offering "12/17" or "71%" as the probability has confused odds with probability. The popular wrong answer is **80%** (the witness's accuracy alone).

### Neglecting base rates

**Base-rate information** is the relative frequency with which an event occurs in the relevant population (here, 15% Blue cabs). Bayes' theorem says it must be combined with the specific evidence. In fact people often ignore it or give it too little weight. In the taxi-cab problem most participants attended only to the witness's reliability and answered that the probability of Blue was **80%**. This systematic failure is **base-rate neglect**.

#### The lawyer-engineer problem (Kahneman & Tversky, 1973)

**Kahneman and Tversky (1973)** gave a second, now famous, demonstration. Participants read a brief personality sketch of "Jack", a 45-year-old married father of four described as conservative, careful and ambitious, uninterested in politics and social issues, who spends his spare time on hobbies such as carpentry, sailing and mathematical puzzles. They were told the sketch had been drawn at random from 100 descriptions. The manipulation was the base rate: half the participants were told the 100 comprised **70 engineers and 30 lawyers**, the other half **70 lawyers and 30 engineers**.

Bayesian reasoning says the base rate should shift the answer substantially between the two groups. It did not. On average, both groups judged the probability that Jack was an engineer to be about **0.90**, regardless of whether engineers made up 70% or 30% of the pool. The 70:30 base rate had effectively no influence.

### Heuristics: what they are and why we use them

**Amos Tversky and Daniel Kahneman** (for example in their 1974 paper) argued that most people tackle judgement problems with **heuristics**, rules of thumb that cut the computation short. Two later definitions, both quoted in the book, emphasise different things, and you should know which author says which:

- **Gigerenzer and Gaissmaier (2011)** define heuristics as strategies that deliberately ignore part of the available information so that decisions can be made faster, more frugally and/or *more accurately* than with more complex methods. Note the claim that ignoring information can increase accuracy; that is the Gigerenzer position you will meet in 13.3.
- **Shah and Oppenheimer (2008)** put the function more modestly: heuristics primarily serve to reduce the effort a task requires.

> **Trap.** Kahneman and Tversky's programme is the **heuristics-and-biases** approach: heuristics are useful but lead to systematic errors. Gigerenzer's programme is the **fast-and-frugal** (adaptive toolbox) approach: heuristics are often accurate and can beat complex methods. Questions that ask "who argued heuristics can be more accurate than complex strategies?" want Gigerenzer, not Kahneman.

### The representativeness heuristic

Why did participants ignore the 70:30 split? Kahneman and Tversky's answer is the **representativeness heuristic**: we judge that an object or person belongs to a category because it looks *typical* (representative) of that category. Jack's sketch reads like a stereotypical engineer, so participants judged by resemblance and ignored how many engineers were actually in the pool. Representativeness is a judgement of *similarity*; the base rate is a matter of *frequency*; the heuristic substitutes the first for the second.

#### The conjunction fallacy: the Linda problem (Tversky & Kahneman, 1983)

**Tversky and Kahneman (1983)** used representativeness to explain a second error, the **conjunction fallacy**: the mistaken belief that a conjunction of two events (A *and* B) is more likely than one of those events alone.

Participants read about "Linda", a 31-year-old single woman, very bright and outspoken, who majored in philosophy and who as a student was deeply concerned about discrimination and social justice and took part in anti-nuclear protests. They were asked which is more probable: that Linda is a bank teller, or that Linda is a bank teller *and* active in the feminist movement. Most people choose the second.

That answer breaks a basic law of probability. Every feminist bank teller is a bank teller, so the set "feminist bank tellers" is contained within the set "bank tellers"; the probability of the conjunction can never exceed the probability of either component. People nonetheless choose it because the sketch *resembles* a feminist activist far more than a bank teller, and representativeness overrides set logic.

**A misinterpretation objection, and why it does not rescue people.** Many participants read "Linda is a bank teller" as implying "and she is *not* a feminist" (Manktelow, 2012). On that reading the second option is not a conjunction at all. But **Sides et al. (2002)** did almost everything possible to make the intended reading clear, and the conjunction fallacy still appeared. So misinterpretation is part of the story, not all of it.

**Tentori et al. (2013): what kind of representativeness?** Standard accounts, including the representativeness explanation, say the fallacy depends on how *probable* the added detail ("feminist activist") seems given the description. Tentori et al. proposed a subtly different account: what matters is how strongly the description *supports* (confirms) the added hypothesis. To separate the two, they added a comparison conjunction: Linda is a bank teller *and owns a pair of black shoes*. Owning black shoes is objectively more probable than being a feminist activist, so the standard account predicts that this conjunction should be rated likelier. But nothing in Linda's description *supports* the black-shoes hypothesis, so the confirmation account predicts the reverse. The results favoured the **confirmation (support) explanation**. The implication the book draws is that the conjunction fallacy is harder to explain than is usually assumed.

> **Trap.** **Base-rate neglect** and the **conjunction fallacy** are different errors, though both are attributed to representativeness. Base-rate neglect = ignoring the prior frequency of a category (taxi-cab, lawyer-engineer). Conjunction fallacy = rating P(A and B) above P(A) (Linda). The lawyer-engineer problem is Kahneman and Tversky **1973**; Linda is Tversky and Kahneman **1983**; the taxi-cab problem is Kahneman and Tversky **1972** in this edition. Some other textbooks cite the cab problem from Tversky and Kahneman's later papers (around 1980 to 1982), so if an older key gives a later date it is the same problem.

#### In the real world: representativeness in medical diagnosis

The heuristic would matter much more if experts also fell for it in real decisions, and **Groopman (2007)** described a case in which one did. **Evan McKinley**, a slim, very fit forest ranger in his early forties, developed severe chest pain, worse on breathing, while hiking. The emergency physician **Pat Croskerry** found that he had never smoked, was not under stress, and had normal blood pressure, a normal electrocardiogram and a normal chest X-ray. Croskerry reassured him that the problem was almost certainly a strained muscle from overexertion and that a cardiac cause was very unlikely. Soon afterwards it emerged that McKinley had in fact had a heart attack. Croskerry later acknowledged that he had been swayed by how healthy the man looked and by the absence of risk factors.

The analysis: McKinley looked highly *representative* of the category "healthy man at negligible risk of heart attack", so that category was assigned and the possibility of a cardiac event was dismissed. A judgement by resemblance replaced a proper estimate of probability.

### Heeding base rates: when people do use them

The picture so far makes people look hopeless at base rates. The book then shows that base-rate use depends heavily on how the problem is presented and on motivation.

#### Causal knowledge (Krynski & Tenenbaum, 2007)

**Krynski and Tenenbaum (2007)** argued that in everyday life we usually have *causal* knowledge that lets us use base rates sensibly, whereas laboratory problems often strip that knowledge away.

They gave one group the **false positive scenario**: among 60-year-old women attending routine mammogram screening, **2%** have breast cancer at the time of screening and most of them will get a positive result; a woman *without* cancer has a **6%** chance of a positive result. A 60-year-old woman tests positive; with no other information, how likely is it that she has cancer? Many participants neglected the 2% base rate here. One plausible reason is that cancer is the only cause of a positive mammogram that the problem mentions, so a positive result "means" cancer.

The second group got the **benign cyst scenario**, in which only the wording of the 6% statement changed: 6% of women without cancer have a dense but harmless cyst that looks like a tumour and produces a positive mammogram. Now there is an explicit alternative *cause* of positive results. Participants given this version were far more likely to use the base rate fully (Figure 13.1 in the book shows the distribution of correct answers and of the various wrong answers, such as base-rate neglect and base-rate overuse, for the two scenarios). Krynski and Tenenbaum argued that the benign cyst version supplies a fairly complete causal picture, which corresponds to how such information is encountered in real life.

They then applied the same idea to the taxi-cab problem, which they argued is hard because its causal structure is opaque: *why* would the witness be wrong? Their **faded paint** version gave a reason: when a sample of cabs was examined, only 80% of each company's cabs actually looked their own colour, because faded paint made 20% of Blue cabs look green and 20% of Green cabs look blue.

| Measure | Standard version | Faded paint version |
|---|---|---|
| Base-rate neglect | 43% | 8% |
| Correct answers | 8% | 46% |

The conclusion: many people do use base rates once they understand the causal mechanism that generates the data.

#### Motivation (Ditto et al., 1998)

People also use base rates when it suits them. **Ditto et al. (1998)** had participants put saliva on a test strip. They were told that if it turned blue, they had an enzyme deficiency signalling a health problem, but that there was a **1 in 10** chance the test would give a misleading result. When the strip turned blue (bad news), most participants seized on the 1/10 base rate to argue that the test was unreliable. When other participants were told that blue meant they were *healthy*, they regarded the same test as accurate and ignored the 1/10 figure.

> **High-yield.** Two conditions make base-rate use more likely: (1) **causal knowledge** about how the data arise (Krynski & Tenenbaum, 2007: benign cyst, faded paint), and (2) **motivation**, when the base rate favours the conclusion you want (Ditto et al., 1998). Base rates are used when advantageous and ignored when disadvantageous: this is motivated reasoning, not neutral Bayesian updating.

### The availability heuristic

The second heuristic Tversky and Kahneman (1974) identified is the **availability heuristic**: we estimate how frequent or probable an event is by how easily instances of it come to mind from long-term memory. Ease of retrieval is often a reasonable proxy for frequency (common things are usually easier to recall), which is why the heuristic exists. It misleads whenever something other than true frequency makes events memorable: vividness, recency, emotional impact or media coverage.

#### Causes of death (Lichtenstein et al., 1978)

**Lichtenstein et al. (1978)** asked people to judge the relative likelihood of different causes of death. Causes that receive heavy publicity, such as **murder**, were judged more likely than less publicised causes, such as **suicide**, even when the true frequencies ran the other way. Publicity makes instances easy to retrieve, and ease of retrieval was read as frequency.

#### Three ways of explaining frequency judgements (Pachur et al., 2012)

**Pachur et al. (2012)** asked *which* kind of availability, or something else entirely, actually drives these judgements. They compared three candidate accounts:

1. **Availability by recall of direct experience**: people judge a cause of death common to the extent that they can recall cases from their own lives (relatives, acquaintances).
2. **Availability by total experience**: people draw on direct experience *plus* media coverage.
3. **The affect heuristic**: people gauge how much *dread* each risk evokes and infer that the more dreaded risk is the more prevalent one. (More generally, the affect heuristic is the use of one's emotional reactions to drive rapid judgements or decisions.)

The results (Figure 13.2 in the book plots the percentage of correct predictions for each model): availability based on **recall of direct experience** was the **best** predictor of people's judged frequencies; the **affect heuristic** also predicted judged risk; and availability based on **media coverage** was the **least** successful predictor.

> **Trap.** It is tempting to assume media coverage is the main driver, because Lichtenstein et al.'s murder versus suicide result is usually explained that way. In Pachur et al. (2012) the *media-inclusive* availability account did **worst**, and *personal direct experience* did **best**. Do not let the classic study overwrite the modern one.

#### When availability is overridden (Oppenheimer, 2004; Oppenheimer & Monin, 2009)

The heuristic is not applied blindly. **Oppenheimer (2004)** showed American participants pairs of surnames, one belonging to a famous person and one not, and asked which surname was more common in the United States. Availability predicts the famous name, because it comes to mind easily. In fact participants mostly picked the **non-famous** names, which was correct, since those names were slightly more common. Participants seem to have recognised *why* the famous name felt familiar (it belonged to a celebrity) and discounted that feeling by deliberate thought.

That interpretation predicts that disabling deliberate thought should bring the heuristic back, and it does. When **Oppenheimer and Monin (2009)** had participants make the same judgement **under cognitive load**, they fell back on availability and chose the famous name **80%** of the time. Availability is the default; deliberate thought can override it when resources allow.

#### In the real world: availability in medical diagnosis

**Groopman (2007)** also described a diagnostic error driven by availability. **Dr Harrison Alter**, working in an Arizona emergency department, had seen dozens of patients with **viral pneumonia** over a three-week period. **Blanche Begaye**, a Navajo woman, then arrived with breathing difficulty; she had taken some aspirin and was breathing at nearly twice the normal rate. Alter diagnosed viral pneumonia, although she lacked the white streaks on the lungs and the harsh lung sounds (rhonchi) characteristic of that disease. Her blood had become slightly acidic, which can happen in a major infection. Within minutes an internist correctly identified **aspirin toxicity** (an aspirin overdose). Alter later admitted she had been a textbook case of it, rapid breathing and electrolyte shift included, and that he had missed it.

The analysis: the many recent pneumonia cases made that diagnosis spring to mind, and its high availability crowded out the correct, rarer diagnosis.

> **Trap.** Croskerry/McKinley is **representativeness** (the patient *looked like* a member of the low-risk category). Alter/Begaye is **availability** (a diagnosis was *easy to retrieve* because of many recent cases). Both are from **Groopman (2007)**. Exam questions describe the scenario and ask you to name the heuristic, so attach each case to its mechanism, not just to "medical error".

**Classic background: anchoring and adjustment.** The third heuristic in Tversky and Kahneman's 1974 paper, not treated in this chapter, is **anchoring and adjustment**: people start from an initial value (an anchor, even an arbitrary one) and adjust insufficiently away from it. In their best-known demonstration, a number produced by a spun wheel of fortune influenced estimates of the percentage of African countries in the United Nations. Older Indian keys list "representativeness, availability, and anchoring" as *the* three heuristics, so know all three.

### Overall evaluation of the heuristics-and-biases approach

**Strengths.**

- Kahneman and Tversky showed that a small number of general heuristics (representativeness, availability) underlie judgements across very different contexts. They were instrumental in founding judgement research as a field.
- Their influence extends well beyond psychology, into economics and philosophy.
- There is abundant evidence that most people prefer to keep cognitive demands low by using heuristics (for example **Kool et al., 2010**; **Fiedler & von Sydow, 2015**).
- The errors are not simply a feature of less able people. It might seem that these biases would afflict less intelligent people more, but intelligence or cognitive ability is almost unrelated to performance on most judgement tasks such as the Linda and lawyer-engineer problems (**Stanovich, 2012**; see Chapter 14).

**Limitations.** The book lists four.

1. **The heuristics are vaguely defined.** Fiedler and von Sydow (2015) argue that one-word labels such as "representativeness" act as stand-ins for theories without placing any testable constraint on the cognitive process. A label that can be stretched to fit any result explains nothing.
2. **Theorising has been limited.** Fiedler and von Sydow express disappointment at how little theoretical precision and progress the approach has achieved. In particular, Kahneman and Tversky did not specify the exact conditions that trigger each heuristic or how the heuristics relate to one another. (The book notes that later theories, in 13.3, partly answer this.)
3. **It is sometimes unfair to call judgements biased.** Most people think skin cancer kills more people than cancer of the mouth and throat, whereas the reverse is true (**Hertwig et al., 2004**). But the "error" arises because skin cancer has received a great deal of media attention. The problem lies in the *information* people have been given, not in how they process it (**Juslin et al., 2007**; **Le Mens & Denrell, 2011**). A perfectly rational processor fed a biased sample will produce biased estimates.
4. **Much research is detached from everyday reality.** Emotional and motivational factors shape real-world judgements but were rarely studied in the laboratory until fairly recently (see Chapter 15). For example, fearful individuals estimated the probability of future terrorist attacks as higher than did individuals who were sad or angry (**Lerner et al., 2003**).

> **Trap.** "Which is NOT a limitation of the heuristics-and-biases approach?" Typical distractor: "the biases are confined to people of low intelligence." The book says the opposite: intelligence is almost **unrelated** to performance on these tasks (Stanovich, 2012). Another distractor: "it ignores the quality of the information people receive" *is* a limitation (Juslin et al., 2007), so do not reject it.

---

## 13.3 Judgement Theories

Kahneman and Tversky's early work contained theoretical ideas, but mostly in the form of labels. Since then they and others have tried to specify the processes behind judgement and its biases. The book takes four theories in turn: support theory, fast-and-frugal heuristics, the natural frequency hypothesis, and Kahneman's dual-process theory (with De Neys's alternative).

### Support theory (Tversky & Koehler, 1994)

**The core idea.** **Tversky and Koehler (1994)** built **support theory** partly on the availability heuristic. Its key assumption is that the subjective probability of an event depends on **how the event is described**, not only on the event itself. So we must distinguish between events and *descriptions* of events. The same event, described in more explicit detail, will seem more probable.

The book's illustration: you probably think it very unlikely that you will die on your next summer holiday. But if you are asked how likely it is that you will die on holiday *from a disease, a car crash, a plane crash, or any other cause*, the probability feels higher, even though the event (dying on holiday) is identical.

**Why explicit descriptions boost probability.** Support theory gives two reasons:

1. An explicit description draws attention to parts of the event that are less obvious in the bare description (you were not thinking about car crashes until they were named).
2. Memory limitations mean people may fail to retrieve all the relevant possibilities unless they are supplied.

Both are availability-style mechanisms: naming the components makes them available, and available components add "support" to the hypothesis.

#### Findings for support theory

**Mandel (2005): terrorist attacks.** Some participants estimated the risk of a terrorist attack in the next six months. Others estimated the probability of an attack *plotted by al-Qaeda* and of an attack *not plotted by al-Qaeda*.

| Description | Mean estimated probability |
|---|---|
| Terrorist attack (unpacked: no) | 0.30 |
| Attack plotted by al-Qaeda | 0.30 |
| Attack not plotted by al-Qaeda | 0.18 |

The two explicit components sum to **0.48** (0.30 + 0.18), well above the **0.30** given to the undivided event. Logically the whole must equal the sum of its exclusive parts, so this is exactly the "unpacking" effect support theory predicts.

**Redelmeier et al. (1995): expert doctors are not immune.** You might expect experts to fill in missing possibilities from their own knowledge, so explicitness should not matter to them. **Redelmeier et al. (1995)** gave expert doctors a description of a woman with abdominal pain. Half assigned probabilities to **two** named diagnoses (gastroenteritis and ectopic pregnancy) plus a residual "everything else" category. The other half assigned probabilities to **five** named diagnoses (including those two) plus "everything else". The key comparison is the probability given to *all diagnoses other than gastroenteritis and ectopic pregnancy*: **0.50** when those other possibilities were lumped together (non-explicit), but **0.69** when three of them were spelled out (explicit). Even experts' probabilities rose with explicitness.

#### Findings against support theory

**Sloman et al. (2004): explicitness can lower probability.** Participants estimated the probability that a randomly chosen American would die of disease rather than some other cause.

| Condition | Mean estimate |
|---|---|
| No examples of diseases given | 0.55 |
| Three *typical* diseases named (heart disease, cancer, stroke) | about the same as 0.55 |
| Three *atypical* diseases named (pneumonia, diabetes, cirrhosis) | 0.40 |

This is the direct opposite of the support theory prediction. Naming low-probability causes focused attention on them and *reduced* the judged probability of the whole category.

**Redden and Frederick (2011): explicitness can make a problem harder.** Some participants judged the likelihood of throwing an **even number** with a die; others judged the likelihood of throwing **a 2, 4 or 6**. The second description is more explicit but was given a *lower* likelihood, because working out the answer from the listed numbers took more effort. Explicitness that increases processing difficulty can reduce subjective probability.

#### Evaluation of support theory

**Strengths.** Its main predictions have generally been supported. It shows concretely how availability can lead to judgement errors. And it is impressive, and somewhat surprising, that even experts are swayed by how explicitly the possibilities are described (Redelmeier et al., 1995).

**Limitations.**

1. The precise reasons *why* explicit descriptions usually raise subjective probability remain unclear.
2. Explicit descriptions can **reduce** subjective probability when they draw attention to low-probability causes (Sloman et al., 2004).
3. They can also reduce it when they make the event harder to comprehend (Redden & Frederick, 2011).
4. The theory is oversimplified. It assumes that the support evidence gives one hypothesis is independent of the rival hypotheses. In practice people compare hypotheses against each other, so the independence assumption is wrong (**Pleskac, 2012**).

> **Trap.** Support theory predicts that **unpacking** an event into explicit components **increases** its judged probability (sum of parts exceeds the whole). Sloman et al. (2004) and Redden and Frederick (2011) are the two exceptions where explicitness *decreased* probability: one through attention to atypical causes, the other through processing difficulty. Do not mix up which exception is which.

### Fast-and-frugal heuristics (Gigerenzer)

**The motivating question.** If our judgements are riddled with heuristic-driven errors, how do we manage so well in the real world? The philosopher **Glymour (2001)** put the puzzle memorably: "If we're so dumb, how come we're so smart?" **Gigerenzer** and his colleagues (for example **Gigerenzer & Gaissmaier, 2011**) answer that heuristics are often genuinely valuable. Their focus is on **fast-and-frugal heuristics**, which process small amounts of information quickly. We are said to possess an **"adaptive toolbox"** of such heuristics, and these heuristics are claimed to be surprisingly accurate, sometimes more accurate than complex strategies.

#### The take-the-best heuristic

The central example is **take-the-best**, summarised as "take the best, ignore the rest". Suppose you must decide which of two German cities, **Cologne** or **Herne**, has the larger population. You might first use the most valid cue you have: cities whose names you recognise tend to be bigger than cities you have never heard of. But suppose you recognise both. You move to the next valid cue, for example that cities with a cathedral tend to be larger. You know Cologne has a cathedral and are unsure about Herne, so you answer "Cologne", and you stop there.

Take-the-best has **three components**:

1. **Search rule**: look through cues in order of their validity (recognition first, then cathedral, and so on).
2. **Stopping rule**: stop as soon as you find a **discriminating** cue, one that applies to only one of the two options.
3. **Decision rule**: choose the option that the discriminating cue favours.

Notice what is missing: there is no weighting and adding of all cues. One good cue settles the matter.

#### The recognition heuristic

The most researched instance of take-the-best is the **recognition heuristic**: if you recognise one of two objects and not the other, choose the recognised one. If you recognise Cologne but not Herne, you infer (correctly) that Cologne is larger and ignore everything else. **Goldstein and Gigerenzer (2002)** made the controversial claim that when one object is recognised and the other is not, **no other information** influences the judgement. Recognition is non-compensatory: other cues cannot outweigh it.

**How is a heuristic chosen?** **Kruglanski and Gigerenzer (2011)** proposed a **two-step** process. First, the nature of the task and the individual's memory limit which heuristics are available. Second, the person selects one of these based on its likely outcome and its processing demands.

#### Findings for fast-and-frugal heuristics

**Goldstein and Gigerenzer (2002), study 1.** American students judged which of two German cities was larger. When they recognised only one of the pair, they apparently used the recognition heuristic **90%** of the time. The book flags a methodological catch that applies to much of this research: choosing the recognised city does not prove the recognition heuristic was used, because the city could have been chosen for other reasons (for example, other knowledge about it).

**Goldstein and Gigerenzer (2002), study 2.** Participants were taught that German cities with football teams tend to be larger. They then compared a *recognised* city that had *no* football team with an unrecognised city. They still chose the recognised city **92%** of the time, largely ignoring the conflicting football cue, as the non-compensatory claim predicts.

> **Trap.** **90%** is recognition-heuristic use in the basic comparison; **92%** is use *despite conflicting information* (the recognised city lacked a football team). Some summaries attach 92% to "when recognition is valid"; that is not what this edition says.

**Recognition is used selectively (Pachur et al., 2012).** The heuristic would be silly for some questions: if asked which of two foreign cities lies further north, recognising one tells you nothing. In fact people use recognition much more when it is valid than when it is not. A **meta-analysis by Pachur et al. (2012)** found a correlation of **+0.64** between how often the recognition heuristic was used and how valid it was for the task.

**Less can be more (Wübben & van Wangenheim, 2008).** That simple heuristics work moderately well is unsurprising. The surprise is that they sometimes beat complex calculations. **Wübben and van Wangenheim (2008)** studied how managers of clothing shops classify customers as **active** (likely to buy again) or inactive. The **hiatus heuristic** says simply: a customer who has bought something fairly recently is active; otherwise not. The alternative was a complex statistical model using all available information.

| Method | Customers correctly classified |
|---|---|
| Hiatus heuristic (recency only) | **83%** |
| Complex model (all information) | **75%** |

This is a **less-is-more effect**: the approach using less information performed better.

#### Findings against, or complicating, fast-and-frugal heuristics

**Recognition is not used when other cues conflict strongly (Richter & Späth, 2006).** German students judged which of two American cities was larger. For some recognised cities they were told the city had an international airport; for others that it did not. The recognised city was chosen **98%** of the time when it had an airport, but only **82%** when it did not. Participants believed airport status was a valid cue, and conflicting information reduced use of recognition, contrary to the claim that nothing else matters.

**Take-the-best is used less than predicted (Newell et al., 2003).** Participants chose between shares in two fictitious companies using various cues. Only **33%** of participants followed all three components of take-the-best. It was least likely to be used when information was cheap to obtain and cue validities were unknown; then people searched more thoroughly than take-the-best allows.

**Individual differences (Bröder, 2003).** On a share-choice task, more intelligent participants were more likely than less intelligent ones to use take-the-best *when it was the best strategy to use*. Strategy use is therefore adaptive, and adaptive skill varies across people.

**Information redundancy (Dieckmann & Rieskamp, 2007).** Redundancy is **high** when different cues carry similar information and **low** when they carry different information. Dieckmann and Rieskamp predicted that simple heuristics like take-the-best work better, and so should be used more, when redundancy is high: if all the cues say much the same thing, checking one is enough. After a learning phase, participants entered a decision phase in which they had to **pay** for information. As predicted (Figure 13.3 in the book shows the proportions of trials), take-the-best was used more than a complex continued-search strategy under **high** redundancy, and the reverse held under **low** redundancy. Put crudely: simple strategies work best, and are chosen more, when the information environment is simple.

#### Evaluation of fast-and-frugal heuristics

**Strengths.** People do often use fast-and-frugal heuristics such as recognition and take-the-best, and these can be surprisingly effective despite their simplicity. It is striking that people with *less* knowledge can sometimes outperform people with more (the less-is-more effect). Progress has been made on what determines strategy selection (Dieckmann & Rieskamp, 2007; Kruglanski & Gigerenzer, 2011).

**Limitations.**

1. **The biggest problem**, as **Evans and Over (2010)** put it, is that the suggestion we are always better off following intuition and gut feeling is an extraordinary claim; if logical reasoning had no value, why would we have the capacity for it?
2. **Recognition-heuristic use is more complex than claimed.** Gigerenzer originally said it was used whenever one of two objects was recognised. In fact people usually consider *why* they recognise an object before deciding whether to rely on recognition (**Newell, 2011**). (Compare Oppenheimer's famous-name result in 13.2.)
3. **Take-the-best is also more complex than claimed.** It requires the cues to be ranked by validity, but we often do not know the cue validities well enough to rank them.
4. **It de-emphasises the importance of the decision.** Stopping at the first discriminating cue may be fine for guessing city sizes, but for a momentous choice, such as which of two people to marry, most people want to weigh all the relevant evidence.

> **Trap.** Gigerenzer's **recognition heuristic** (choose the recognised object) is not the same as Kahneman and Tversky's **availability heuristic** (judge frequency by ease of retrieval), though both rest on memory. Recognition is a binary "know it or not" cue used for *comparison*; availability is a graded ease-of-retrieval cue used for *frequency estimation*. The **hiatus heuristic** is Wübben and van Wangenheim (2008), not Gigerenzer himself.

### The natural frequency hypothesis (Gigerenzer & Hoffrage, 1999)

**The argument.** **Gigerenzer and Hoffrage (1999)** pointed out that in everyday life people are almost never handed summary statistics such as "the base rate is 1%". What we actually experience is **natural sampling**: meeting instances of a population one after another and, in effect, keeping a running count. Their evolutionary argument follows. Our evolutionary history has equipped us to track the **frequencies** of different kinds of events, but not to manipulate fractions, percentages and single-event probabilities, which are recent cultural inventions. That is why people do so badly on base-rate problems stated as percentages. The central prediction: performance on such problems should improve greatly if the information is presented as **natural frequencies**.

To see why the format could matter, take the **Fiedler et al. (2000)** mammogram figures discussed below (base rate 1%, 80% of women with cancer test positive, 9.6% of women without cancer test positive) and restate them as natural frequencies:

- Imagine **1,000** women. **10** have breast cancer; **990** do not.
- Of the 10 with cancer, **8** test positive.
- Of the 990 without cancer, about **95** test positive (9.6% of 990).
- So about **103** women test positive, and only **8** of them have cancer: 8/103 is about **7.8%**.

In frequency form the base rate is built into the counts, so the Bayesian computation collapses into "how many of the positives are real?". That is the intuition behind the hypothesis.

**Two conceptual problems** the book raises before the findings:

1. The theory stresses "natural" or objective frequencies, but in real life we only ever encounter a *sample*, and the frequencies in our sample can differ substantially from the population's. A university student, for example, meets highly intelligent and less intelligent people in proportions very unlike those in the general population.
2. Natural frequencies are not the same as the word problems used in research. In most studies participants are simply *given* frequency information; they never have to do any natural sampling themselves.

#### Findings for frequency formats

**Fiedler (1988): the Linda problem.** Comparing standard and frequency versions of the Linda problem, the percentage of participants committing the conjunction fallacy fell by **two-thirds** in the frequency version.

**Hoffrage et al. (2000): experts benefit too.** Advanced medical students worked through **four** realistic diagnostic tasks in probability or frequency versions. They performed much better, and made much more use of base-rate information, with the **frequency** versions.

**Lesage et al. (2013): frequencies still need resources.** Base-rate problems were given in probability or frequency versions, with the information expressed either in simple absolute terms (natural frequencies) or in more complex relative terms. Correct answers that fully used the base rate were far more common with frequency versions. But even the frequency versions demanded cognitive resources: participants of **higher cognitive ability** did better on them than those of lower ability. Frequencies help, but they do not make the problem effortless.

#### Findings against the natural frequency explanation

**Evans et al. (2000): the confound.** Frequency versions of problems usually make the problem's underlying **structure** much more obvious (as the 1,000-women breakdown above illustrates, the set relations are laid out). When **Evans et al. (2000)** removed this confound, performance on frequency versions was typically **no better** than on probability versions. They also found a new bias: participants given frequency versions were *more* likely to focus exclusively on the base rate and ignore the specific diagnostic information.

**Fiedler et al. (2000): let people sample, and they sample badly.** This study tested whether actual frequency *sampling* increases base-rate use. The problem: an **80%** chance that a woman with breast cancer has a positive mammogram, **9.6%** for a woman without, and a base rate of **1%**. Participants had to judge how likely a woman with a positive mammogram is to have cancer, and they gathered information by drawing cards from files sorted into "women with breast cancer" and "women without". Their sampling was heavily skewed towards the cancer file, because they wrongly believed it was more informative. The result was an average estimate of **63%** that a positive-testing woman has cancer, against the correct answer of **7.8%**.

**Fiedler (2008): natural sampling on a decision task.** When participants used natural sampling in a decision-making task, they often ended up with too little information about **infrequent** categories, and their decisions were biased as a result. Rare categories are, by definition, rarely encountered.

#### Evaluation of the natural frequency hypothesis

**Strengths.**

1. It is plausible that natural or objective sampling could improve the accuracy of many everyday judgements.
2. Judgements based on frequency information are often better than those based on probability information.

**Limitations.**

1. Once steps are taken to stop the frequency version making the problem structure more obvious, it is generally **not** easier than the probability version (Evans et al., 2000; Manktelow, 2012). So the frequency advantage probably does **not** arise because humans are naturally equipped to think in frequencies.
2. There is a wide gap between people's real sampling behaviour and the tidy frequency data supplied in laboratory experiments (Fiedler et al., 2000).
3. Truly natural sampling may be impossible, because at any moment information about different objects is not equally available (**Fiedler, 2008**).
4. Thinking in frequencies is sometimes *harder* than thinking in probabilities, because tracking frequencies in the real world places heavy demands on memory (**Amitani, 2008**).

> **Trap.** Two different claims hide under "frequency formats help". The **empirical** claim (frequency versions are often solved better) is well supported. The **theoretical** claim (they help because evolution tuned us to frequencies) is what Evans et al. (2000) undermine: the benefit largely comes from making the **set structure transparent**. An option saying "Evans et al. showed frequency formats never help" overstates them; they showed the benefit vanishes when transparency is equated. And the mammogram numbers belong to **Fiedler et al. (2000)** (1%, 80%, 9.6%; answer 7.8%, estimate 63%), whereas the **Krynski and Tenenbaum (2007)** mammogram used 2% and 6%.

### Dual-process theory: Kahneman (2003)

**Why two processes?** Most of the time people judge by heuristics because heuristics are quick and nearly effortless. But sometimes people clearly use slower, more complex processes. This led several theorists (for example **Kahneman, 2003**; **De Neys, 2012**) to propose **dual-process models**. The same family of models is applied to reasoning in Chapter 14.

According to **Kahneman (2003)**, probability judgements depend on processing in two systems:

| Feature | System 1 | System 2 |
|---|---|---|
| Speed | Fast | Slower |
| Mode | Automatic | Serial (one operation at a time) |
| Effort | Effortless | Effortful |
| Awareness | Implicit: not open to introspection | More likely to be consciously monitored |
| Control | Hard to control or modify | Deliberately controlled |
| Emotion | Often emotionally charged | Not described as emotionally charged |
| Flexibility | Relatively rigid | Relatively flexible, potentially rule-governed |

**How the systems relate.** In Kahneman's account the processing is **serial**. System 1 rapidly produces an intuitive answer (for example, by representativeness). System 2 then monitors or evaluates that answer and may correct it. So a judgement always starts with System 1 and is *sometimes* followed by System 2. Errors arise when System 2 fails to step in.

**Classic background.** The labels "System 1" and "System 2" were introduced by **Stanovich and West (2000)** and were popularised by Kahneman, especially in *Thinking, Fast and Slow* (2011). Exam keys sometimes credit the terms to Kahneman alone; the theory discussed here is Kahneman's (2003) version.

#### Findings for the theory

**De Neys (2006): System 2 is slower.** Participants solved the Linda problem and a very similar problem. Those who gave the correct answers (presumably using System 2) took almost **40%** longer than those who apparently used only System 1.

**De Neys (2006): System 2 needs the central executive.** The same problems were solved alone or alongside a demanding secondary task that loaded the **central executive** (the attention-controlling component of working memory). Accuracy fell from **17%** correct without the secondary task to **9.5%** with it, as predicted if the correct answer requires effortful System 2 processing.

#### Findings that complicate the theory

**De Neys et al. (2011): intuitive responders still register the base rate.** On standard base-rate problems, participants gave incorrect, base-rate-neglecting intuitive answers on **80%** of trials, which looks like complete neglect. But they were **less confident** when giving those incorrect intuitive answers than when giving correct answers. So the base rate was being processed to some degree even when it did not change the response. Other research suggests this processing happens **below conscious awareness** (**De Neys & Glumicic, 2008**).

**De Neys et al. (2008): the brain detects the conflict.** Focusing on people whose answers were heuristic and who apparently ignored the base rate, De Neys et al. argued that these people had nonetheless processed the base rate and detected a **conflict** between it and their answer. They measured activity in the **anterior cingulate cortex** (ACC), a region associated with conflict detection, and found increased activation, as predicted.

**Pennycook and Thompson (2012): base rates in the first, fast answer.** Pennycook and Thompson used problems modelled on the lawyer-engineer task. In one, 1,000 people took part in a study, of whom **995 were nurses and 5 were doctors**; "Paul", chosen at random, is described as a 34-year-old who lives in a fine house in an affluent suburb, speaks well, is keenly interested in politics and is heavily invested in his career. What is the probability Paul is a nurse? The base rate says almost certainly a nurse; the description sounds like a doctor. Participants answered each problem **twice**: first with whatever came to mind, then with a deliberate answer.

Kahneman's theory makes two predictions: (1) initial answers should rarely reflect the base rate and should mostly be driven by representativeness; (2) the base rate should be used much more in the deliberate answers. **Neither was supported.**

- About **half** of the initial answers were based mainly on the base rate.
- Among participants who changed their answer, **30%** gave *more* weight to the base rate in the deliberate answer, but an almost equal **23%** gave it *less*.

So the assumption that base-rate answers require System 2 and description-based answers come from System 1 is wrong; processing is more flexible.

**Chun and Kruglanski (2006): format, not content.** Using versions of the lawyer-engineer problem, they presented one type of information (base rate or personality description) **briefly** and the other **at length**, and manipulated **cognitive load**. Dual-process theory predicts that load reduces System 2 and therefore reduces base-rate use, whatever the format. Instead, load increased reliance on **whichever information was presented briefly**, whether that was the base rate or the personality description. What determined "System 1-like" versus "System 2-like" use was how easy the information was to process, not whether it was base-rate or individuating content.

#### Evaluation of Kahneman's dual-process theory

**Strengths.** There is reasonable support for two distinct kinds of processing, and System 2 processing is clearly more demanding and effortful than System 1. The idea that judgements are usually driven by System 1 fits most findings. Similar two-process theories have been fairly successful for decision making (this chapter) and reasoning (Chapter 14).

**Limitations.** The book lists five.

1. It assumes people often rely almost entirely on System 1 and so *totally* ignore base rates. Rapid, non-conscious processing of base rates (De Neys & Glumicic, 2008; De Neys et al., 2008, 2011) shows this is an oversimplification.
2. It is tempting to equate errors with System 1 and accuracy with System 2. But people can show strong biases even when using effortful, conscious, controlled strategies of the System 2 kind (**Le Mens & Denrell, 2011**).
3. It assumes base rates influence judgement only when conditions favour effortful System 2 processing. That increasingly looks wrong or oversimplified (Chun & Kruglanski, 2006; Pennycook & Thompson, 2012).
4. **The serial-processing puzzle** (De Neys, 2012): if System 2 has not yet been engaged, how can the person rapidly detect that System 1's answer is wrong and needs correcting? Something must flag the conflict *before* System 2 runs.
5. Dividing processes neatly into heuristic and controlled is too tidy (**Keren & Schul, 2009**). Fiedler and von Sydow (2015) note that the two systems are claimed to differ on too many attributes at once (automaticity, capacity limits, awareness, rule use, effort), and there is very little evidence that these attributes actually go together as tightly as the theory assumes.

> **Trap.** The **anterior cingulate cortex** finding (De Neys et al., 2008) is evidence **against** the simple Kahneman view: it shows conflict detection in people whose *answers* looked purely heuristic. It is not evidence that those people "used System 2". Likewise De Neys (2006) (40% longer; 17% versus 9.5% under load) **supports** Kahneman; De Neys et al. (2008, 2011) and Pennycook and Thompson (2012) **challenge** him. Same author, opposite directions.

### The way forward: De Neys's logical intuition model (2012)

To accommodate these findings, **De Neys (2012)** proposed the **logical intuition model** (the book develops it further in Chapter 14, with Figure 14.6). The key change is that intuitive, fast processing is not only heuristic. In the initial phase there is rapid intuitive processing of the **heuristic** information (System 1 in the usual sense) **and** rapid intuitive **logical** processing, for example of base rates. This initial processing is *sometimes* followed by deliberate System 2 processing.

| Advantage over Kahneman (2003) | Evidence |
|---|---|
| Heuristic and base-rate information can both be accessed quickly and intuitively | Pennycook & Thompson (2012): about half of first answers used the base rate |
| Easily processed base-rate information should be used *more* under load | Chun & Kruglanski (2006) |
| Conflict between heuristic and base-rate information can be detected rapidly, because both are present in the intuitive phase | De Neys et al. (2008, 2011): ACC activation, reduced confidence |

> **High-yield.** Kahneman (2003): **serial**, default-interventionist; System 1 answers, System 2 may override. De Neys (2012): **logical intuitions** run in parallel with heuristic intuitions at the fast stage, which explains conflict detection and fast base-rate use. "Which finding is consistent with De Neys's model but not with Kahneman's?" Answer: greater use of easily processed base-rate information under cognitive load (Chun & Kruglanski, 2006).

---

## 13.4 Decision Making under Risk

### From normative to descriptive theories

Everyday life is a stream of choices: which film to see, whom to date, whom to share a flat with next year. For a long time it was assumed that people behave rationally most of the time and so usually pick the best option. That assumption was built into **normative theories**, which describe how people *should* decide rather than how they *actually* do. Psychology's contribution has been **descriptive** theories, and prospect theory is the most important of them.

#### Expected utility theory (von Neumann & Morgenstern, 1944)

**Von Neumann and Morgenstern (1944)** proposed **utility theory**. It was not intended as a psychological theory, but it assumes we try to maximise **utility**, the subjective value we place on an outcome. For a simple choice, each option's expected utility is:

**Expected utility = (probability of an outcome) × (utility of that outcome)**

and the rational chooser picks the option with the highest expected utility. One of their key contributions was to treat decisions *as if they were gambles*, each option being a set of outcomes with attached probabilities.

As **Manktelow (2012)** notes, this approach was later combined with **Savage's (1954)** mathematical method, which uses people's preferences to combine **subjective** utilities with **subjective** probabilities. The result is **subjective expected utility (SEU) theory**.

In real choices, each option has several attributes. One holiday may be in a more interesting area with better weather, but cost more and involve more travel. On the expected utility view, people work out the utility or disutility (cost) of each factor and combine them into an overall value for each option. In fact, choices are often determined by factors other than utility, as the rest of the chapter shows.

> **Trap.** Expected utility theory (von Neumann & Morgenstern, **1944**) and SEU theory (building on **Savage, 1954**) are **normative**. Prospect theory (Kahneman & Tversky, **1979**, 1984) is **descriptive**. Questions that ask "which is a descriptive theory of decision making under risk?" want prospect theory.

### Losses and gains: three puzzling choices

The book opens with three decisions where most people do not choose what expected value recommends.

| Problem | Options | Expected values | What most people do |
|---|---|---|---|
| 1. Coin toss (**Tversky & Shafir, 1992**) | Win $200 on heads, lose $100 on tails, or decline | Accepting gives an average gain of **$50** per toss | **Two-thirds refuse** the bet |
| 2. Gains (**Kahneman & Tversky, 1984**) | Sure gain of $800, or 85% chance of $1,000 and 15% chance of nothing | $800 versus **$850** | Most take the **sure $800** (smaller expected gain) |
| 3. Losses (**Kahneman & Tversky, 1984**) | Sure loss of $800, or 85% chance of losing $1,000 and 15% chance of losing nothing | $800 versus **$850** expected loss | Most take the **gamble** (larger expected loss) |

Problems 2 and 3 are mirror images. In the domain of gains people are **risk averse** (they take the certain option); in the domain of losses they are **risk seeking** (they gamble to avoid a certain loss). Expected value theory cannot explain why the direction flips.

#### In the real world: Nik Wallenda's decision making under risk

People differ enormously in their appetite for risk. The American tightrope walker **Nik Wallenda**, known as "the King of the Wire" (discussed by **Newell, 2015**), crossed the Grand Canyon on **23 June 2013** on a wire about **1,500 feet** up, with **no safety harness and no net**, in winds he said were far worse than he had expected. He made it across in **22 minutes and 54 seconds**. How can such a choice be understood? Wallenda emphasised the gains (walking the wire is what he loves and, in his words, his life), and his strong **Christian faith** minimised the perceived potential loss, since he said he was not afraid of dying and was sure of where he would go. The book uses the case later to make the point that prospect theory **de-emphasises individual differences**.

### Prospect theory (Kahneman & Tversky, 1979, 1984)

**Kahneman and Tversky (1979, 1984)** developed **prospect theory** to explain these apparently paradoxical findings. Two main assumptions:

1. **A reference point.** People evaluate outcomes not as final states of wealth but as **gains or losses relative to a reference point**, usually their current state.
2. **Loss aversion.** People are much more sensitive to potential losses than to equivalent potential gains. That is why most people refuse a 50:50 bet unless the potential win is roughly **twice** the potential loss (**Kahneman, 2003**).

#### The value function (Figure 13.4)

The book's Figure 13.4 (a hypothetical value function from Kahneman and Tversky, 1984) is lost from the PDF, so here is its shape in words:

- The horizontal axis runs from **losses** (left) to **gains** (right); the vertical axis is subjective **value**. The **reference point** is where the axes cross.
- **On the gains side**, value rises but **ever more slowly** (the curve is concave). So winning £2,000 instead of £1,000 does not double the subjective value of the win.
- **On the losses side**, value falls **more steeply** than it rises for gains, so a loss of a given size hurts more than an equal gain pleases. (The losses curve also flattens with size, which is why a further loss on top of a large loss matters relatively little.)
- The result is an asymmetric S-shape, steeper below the reference point than above it.

#### How prospect theory explains the three puzzles

- **Refusing the coin toss**: the potential $100 loss is weighted more heavily than the $200 gain, because the loss limb is steep.
- **Taking the sure $800 gain**: on the concave gains limb, a certain $800 has more subjective value than an 85% shot at $1,000, so people are **risk averse for gains**.
- **Gambling on the losses problem**: a certain loss is especially painful, and the gamble offers a chance of avoiding loss altogether, so people are **risk seeking for losses**.

So the theory does not predict that people always avoid risk. When risk offers a way out of a loss, people take it, *because* they are so loss averse.

#### Overweighting rare events

Prospect theory also assumes people **overweight low-probability events**: rare events receive more decision weight than their actual probability justifies. This helps explain why people buy tickets for the National Lottery, where the chance of the jackpot is about **1 in 14 million**.

> **Trap.** **Loss aversion** (losses loom larger than equal gains) is not the same as **risk aversion** (preferring a certain outcome to a gamble of equal or higher expected value). Prospect theory predicts **risk aversion for gains** but **risk seeking for losses**, and loss aversion is the reason for the risk seeking. If an option says "loss aversion makes people avoid all risks", it is wrong.

### Findings: the framing effect

A **framing effect** occurs when decisions are swayed by aspects of the situation that should be irrelevant to a good decision, such as the wording of a problem. The classic demonstration is the **Asian disease problem** of **Tversky and Kahneman (1981)**.

Participants were told that the United States was preparing for an unusual Asian disease expected to kill **600** people, and that two programmes to combat it had been proposed, with exact scientific estimates of their consequences.

**Gain frame** (outcomes described as lives saved):

- Programme **A**: 200 people will be saved.
- Programme **B**: one-third probability that all 600 are saved, two-thirds probability that nobody is saved.
- Result: **72%** chose A, the **certain** option, although on average both programmes save 200 lives.

**Loss frame** (the same outcomes described as deaths):

- Programme **C**: 400 people will die.
- Programme **D**: one-third probability that nobody dies, two-thirds probability that all 600 die.
- Result: **78%** chose D, the **risky** option, driven by loss aversion, although again both programmes have the same average effect.

A and C describe exactly the same outcome (200 live, 400 die), as do B and D. Changing only the wording reverses the majority preference: risk aversion when the outcome is framed as gains, risk seeking when it is framed as losses.

#### Problems with the framing evidence

**Mandel and Vartanian (2011): ambiguity.** The certain option is always more ambiguous than its risky partner. Some participants probably read programme A as "*at least* 200 saved" and programme C as "*at least* 400 die", which would make A look better and C look worse for reasons unrelated to loss aversion. Consistent with this, when **all** programmes were described completely (or all incompletely), the framing effect **disappeared**.

**Wang (1996): social and moral factors.** Wang argued that prospect theory ignores social and moral considerations. Participants chose between a **deterministic** option (two-thirds of the patients definitely survive) and a **probabilistic** option (one-third chance all survive, two-thirds chance none survive). The deterministic option saves, on average, **twice** as many patients, but the probabilistic option seems **fairer** because everyone shares the same fate. When the patients were **six strangers**, participants strongly preferred the deterministic option. When they were **six close relatives**, participants preferred the probabilistic option, because fairness mattered most when family was involved.

**Almashat et al. (2008): framing can be eliminated.** Using medical scenarios about cancer treatment, they found that the framing effect disappeared when participants **listed the advantages and disadvantages** of each option and **justified** their decision. Careful, deliberate consideration of the options can remove the effect.

**Classic background.** A well-known medical framing study often cited in Indian papers is **McNeil et al. (1982)**: patients, doctors and students preferred surgery over radiation for lung cancer more often when outcomes were described in terms of survival than in terms of mortality. It is not in this chapter but illustrates the same effect.

### Findings: the sunk-cost effect

The **sunk-cost effect** resembles loss aversion: it is the tendency to keep pursuing a course of action that has turned out badly *because* resources have already been invested in it (the definition the book takes from **Braverman & Blumenthal-Barby, 2012**). Everyday shorthand: throwing good money after bad. Rationally, money already spent and unrecoverable should not influence a forward-looking choice.

**Dawes (1988)** discussed a study in which two people had paid a **non-refundable $100 deposit** for a weekend at a resort. On the way, both felt slightly unwell and thought they would probably enjoy themselves more at home. Many participants said they should carry on to the resort so as not to "waste" the $100. But the $100 is gone either way; going adds further costs (money spent at the resort) and produces the less preferred outcome.

How can the effect be overcome?

- **Complete information (Baliga & Ely, 2011).** They argued that people with full memory of all the relevant information should be immune, because they would not fixate on the costs already incurred. As predicted, **MBA students** given an investment problem with full access to the information showed the **opposite** of the sunk-cost effect.
- **Expertise (Braverman & Blumenthal-Barby, 2012).** **Expert healthcare providers** making treatment recommendations for clinical scenarios showed **no overall** sunk-cost effect.

### Findings: overweighting rare events, and the description-experience gap

Several studies support prospect theory's prediction that rare events are overweighted. But in most of them participants received a neat **description** of the outcomes and their probabilities. In real life we often decide from limited personal **experience** instead.

**Hertwig et al. (2004)** compared the two. When decisions were based on **descriptions**, participants **overweighted** rare events, as prospect theory predicts. When decisions were based on **experience**, gained by sampling outcomes one at a time (sequential sampling), participants **underweighted** rare events, largely because in a short sample they often never encountered the rare event at all. This reversal is known in the wider literature as the **description-experience gap**.

**Hilbig and Glöckner (2011)** asked whether rare events could be weighted *accurately*. They proposed **open sampling**: rapidly presenting participants with a large amount of detailed outcome information. They also ran description and sequential sampling conditions. As in earlier work, descriptions produced **overweighting** and sequential sampling produced **underweighting** (Figure 13.5 in the book plots the probability of choosing the rare-event gamble against its value in euros for each format). As predicted, **open sampling** produced **accurate** weighting.

Two conclusions follow: the weighting of rare events depends on exactly how information is provided, and the sequential and open sampling results are inconsistent with prospect theory, which assumes overweighting.

> **Trap.** Direction matters. **Description → overweighting** of rare events (prospect theory's prediction). **Sequential experience → underweighting** (Hertwig et al., 2004). **Open sampling → accurate weighting** (Hilbig & Glöckner, 2011).

### In the real world: risk taking by experts

Because most prospect-theory research is done in the laboratory, it is fair to wonder whether experts, whose income depends on good decisions, would have learned to suppress loss aversion. Three real-world studies say they have not, or only partly.

**Professional golfers (Pope & Schweitzer, 2011).** In golf, a **birdie** (one under par) is a gain and a **bogey** (one over par) is a loss relative to the par reference point. A par putt, if missed, produces a bogey, so loss aversion predicts players will putt *more aggressively* for par and more cautiously for birdie. Pope and Schweitzer analysed about **2.5 million** putts by professionals. **Par putts were less likely than birdie putts of the same length to stop short of the hole**, the signature of loss aversion, and **94%** of golfers, **Tiger Woods** included, showed evidence of it.

**Poker players (Smith et al., 2009).** Experienced poker players (many of them professionals) were studied in high-stakes games; **half** of the players won or lost more than **$200,000**. They typically played more **aggressively** (betting and raising more often) after a **big loss**, as loss aversion predicts: after a loss, risk seeking increases in an attempt to get back to the reference point.

**Financial professionals (Abdellaoui et al., 2013).** Professionals who each handled about **£200 million** on average were, as prospect theory predicts, **risk averse for gains** and **risk seeking for losses** on a money task. Their risk aversion for gains was similar to that of students, but they were **less loss averse** than students (Figure 13.6).

The upshot: even experts whose livelihood depends on accurate decisions show loss aversion, so prospect theory applies outside the laboratory, though experts may be somewhat less loss averse than non-experts.

### Loss neutrality (Yechiam & Hochman, 2013)

Consider a choice between (1) a 50% chance to win £1 and a 50% chance to lose £1, and (2) a 50% chance to win £5 and a 50% chance to lose £5. Prospect theory predicts that loss-averse people will prefer (1) because it limits possible losses. In fact, across several studies with choices like these, the usual result is **loss neutrality**: participants do not favour either option, unless the stakes are high (**Yechiam & Hochman, 2013**). This repeated finding contradicts prospect theory.

Why loss neutrality here but loss aversion elsewhere? Yechiam and Hochman proposed an **attentional model**. Losses cause a brief rise in **arousal**, which directs attention to the task and makes the person more sensitive to its outcomes, both losses and gains. When potential gains and losses are presented **together**, this heightened sensitivity applies to both and produces loss neutrality. Loss aversion appears on tasks where attention is directed to gains **or** losses rather than both at once.

### Findings: individual differences

Prospect theory says little about individual differences (recall Wallenda).

- **Deal or No Deal (Brooks et al., 2009).** On this television game of chance, where contestants can win or lose large sums, most were **risk averse**, especially with high stakes, as the theory predicts. But individual differences in willingness to take risks were large, even at very high stakes.
- **Self-esteem (Josephs et al., 1992).** People high in self-esteem were more likely to prefer risky gambles than people low in self-esteem, because a strong self-protective system helps them maintain self-esteem when threatened by a loss.
- **Narcissism (Foster et al., 2011).** Narcissism is related to self-esteem but involves excessive self-regard. People high in narcissism made **riskier stock-market investments**, because they are highly sensitive to reward but have low sensitivity to punishment.

### Evaluation of prospect theory

**Strengths.** Prospect theory accounts for decision making far better than earlier approaches such as subjective expected utility theory. Its value function, especially the greater weight on losses than gains, explains many phenomena: loss aversion, the sunk-cost effect and framing effects. Loss aversion in professional golfers, experienced poker players and financiers demonstrates that it applies widely in the real world.

**Limitations.** The book lists six.

1. **No detailed rationale for the value function.** Kahneman and Tversky did not explain *why* it has its shape. Its origins may lie in evolutionary history (**McDermott et al., 2008**): risky behaviour may be the best strategy for someone facing starvation, whereas minimising risk is sensible when resources are plentiful.
2. **Oversimplification of the reference point.** The theory treats the reference point as the current state, but its meaning depends on context. Winning nothing would feel far worse if you had been given a **90%** chance of winning **$1 million** than if your chance had been one in a million (**Newell, 2015**). Expectations, not just current wealth, set the reference point.
3. **The predicted overweighting of rare events sometimes fails**, especially when people learn about events through sequential sampling (Hertwig et al., 2004).
4. **Loss aversion is found less often than the theory predicts**; **loss neutrality** appears, especially when gains and losses are presented together (Yechiam & Hochman, 2013).
5. **Individual differences are de-emphasised**, although everyday experience shows people vary enormously in willingness to take risks.
6. **Social and emotional factors receive little attention** (for example **Wang, 1996**), despite much research on them (13.5).

> **Trap.** "Which is NOT a limitation of prospect theory?" A distractor might say "it cannot explain the framing effect" or "it does not apply to experts". Both are false: framing is one of its main successes, and golfers, poker players and financiers all show loss aversion. The genuine limitations are the six above (no rationale for the value function, oversimplified reference point, rare-event weighting failures, loss neutrality, individual differences, social and emotional factors).

---

## 13.5 Decision Making: Emotional and Social Factors

Prospect theory's last two limitations open this section. Winning and losing have emotional consequences, so emotion should shape risky choice: a person who is more strongly affected by winning than by losing should take more risks than someone with the opposite tendency (the narcissism result of Foster et al., 2011, already fits this). And while laboratory decisions are usually made in private, real decisions often have to be **justified to other people**.

The book's illustration of the social point: a contestant on *Who Wants to Be a Millionaire?* faces a question with two possible answers. A correct answer gains **£75,000**; a wrong answer loses **£25,000**. On a 50:50 guess the expected financial value favours answering. But if her family is poor and the money already won would transform their lives, the social context says she should take the money and stop. Pure expected value misses what matters to the decision maker.

### Emotional factors

Anticipated or actual losses can trigger negative emotions such as anxiety, and those emotions may be what produces loss aversion. Much of the relevant research falls within **neuroeconomics**, the use of cognitive neuroscience to understand economic decision making.

#### Impact bias (Kermer et al., 2006)

**Kermer et al. (2006)** showed that people exaggerate how bad a loss will feel. Participants were first given **$5**, then predicted how they would feel if a coin toss made them **win $5** or **lose $3**. They predicted that losing $3 would affect their happiness more than winning $5, both immediately and **ten minutes** later, which looks like loss aversion.

What actually happened: participants who lost felt **happier than they had predicted** at both time points, and the actual effect on happiness of losing $3 was **no greater** than that of winning $5. Overestimating the intensity and duration of negative emotional reactions to loss is called **impact bias**. Kermer et al. noted that it also appears in predictions about major losses, such as losing a job or a romantic partner.

The implication is important: part of loss aversion may rest on a *forecasting error*. We avoid losses because we expect them to hurt more than they really do.

> **Trap.** **Impact bias** is an error in *predicting* emotion (affective forecasting): the forecast loss is worse than the experienced loss. **Loss aversion** is a property of *choice*: losses weigh more than equal gains. Kermer et al. (2006) suggest the first partly causes the second. The amounts are **win $5 / lose $3**, after being given **$5**.

#### Anticipated versus immediate emotions (Schlösser et al., 2013)

Two kinds of emotion can be distinguished. **Anticipated emotions** are those a person predicts will follow the possible outcomes of a decision. **Immediate emotions** are those actually felt just before deciding. **Schlösser et al. (2013)** found that the riskiness of decisions was predicted by **both**.

#### Regret, disappointment, rejoicing and elation (Giorgetta et al., 2013)

Emotional effects are more intricate than "losses feel bad". **Giorgetta et al. (2013)** used a gambling task in which the choices were made either by the **participant** or by a **computer**. The same outcome produced different emotions depending on who chose:

| Outcome | Participant chose (personal agency) | Computer chose (no agency) |
|---|---|---|
| Loss | **Regret** | **Disappointment** |
| Win | **Rejoicing** | **Elation** |

The behavioural consequences (Figure 13.7 in the book shows the percentage of risky choices after each emotion):

- **Regret** was followed by **riskier** choices than **disappointment**.
- **Elation** was followed by **riskier** choices than **rejoicing**.

Overall, the findings fitted prospect theory better in the conditions with personal agency (regret and rejoicing).

> **Trap.** Regret and rejoicing require **personal agency** (you chose); disappointment and elation follow **computer** choices. After losses, **regret** (not disappointment) produced the riskier choices; after wins, **elation** (not rejoicing) did. Students often assume "positive emotion means more risk" across the board; the comparison is within each outcome type.

#### Which brain areas? The amygdala and the ventromedial prefrontal cortex

Several brain regions are involved in emotional processing during decision making, but most research has focused on two: the **amygdala**, a limbic-system structure associated with several emotional states including fear and anxiety, and the **ventromedial prefrontal cortex** (vmPFC). (The book points to its figures in Chapter 15 for their location.)

**Weller et al. (2007): lesion patterns differ.**

| Damage | Risk seeking for potential gains | Risk seeking for potential losses |
|---|---|---|
| Ventromedial prefrontal cortex | **Elevated** | **Elevated** |
| Amygdala | **Elevated** | **Not** elevated |

The vmPFC patients' risk seeking was especially marked when the probability of success was **low**.

**De Martino et al. (2010): no amygdala, no loss aversion.** Two women, **SP and AP**, with severe amygdala damage showed **no evidence of loss aversion**. De Martino et al. described the amygdala as acting like a "cautionary brake" on risky choice.

**Sokol-Hessner et al. (2013): regulating emotion reduces loss aversion.** When participants making risky financial decisions were instructed to use **emotion regulation** (reducing their emotional involvement in the task), they showed **reduced loss aversion**, and other findings suggested this happened because regulation **decreased amygdala responses to losses**.

**Koscik and Tranel (2013): vmPFC and social attribution.** Participants invested money with hypothetical investors whose success was described either as **dispositional** (earned through their own efforts, for instance being highly motivated and ambitious) or **situational** (owed to favourable circumstances, such as economic growth in China). Healthy people tend to make **dispositional attributions** for others' behaviour in most circumstances, so they read even situational success as reflecting the person, and invested comparable amounts with both investors. Patients with **vmPFC damage**, by contrast, invested **more** with investors who had succeeded by their own efforts. The interpretation: the bias towards dispositional attribution depends on social-information processing in the vmPFC, so it disappears when that region is damaged. Intriguingly, the patients' investments were the more financially sensible ones, since it makes more sense to back someone who earned their success than someone who got lucky.

**Classic background: the somatic marker hypothesis.** Older textbooks and Indian keys explain the vmPFC's role through **Damasio's (1994) somatic marker hypothesis**: bodily emotional signals tag options as good or bad, and vmPFC patients who lack them choose badly in real life (tested with the **Iowa Gambling Task**, Bechara et al., 1994). This chapter does not use that framework. Note the tension with Shiv et al. below: there, reduced emotion *improves* a particular gambling decision. Both can hold, because the tasks reward different things.

#### In the real world: can brain damage improve decision making? (Shiv et al., 2005a, 2005b)

**Shiv et al. (2005a, b)** argued that emotions can make us excessively cautious and loss averse. That led to a counterintuitive prediction: patients whose brain damage **reduced emotional experience** should outperform healthy people on a suitable gambling task.

**Groups.** (1) Patients with damage to emotion-related areas (**amygdala, orbitofrontal cortex, insula or somatosensory cortex**); (2) patients with brain damage elsewhere; (3) healthy controls.

**Task.** Each participant started with **$20**. On each of **20 rounds** they decided whether to invest **$1**. If they invested, a coin toss determined the outcome: heads, they **lost the $1**; tails, they **won $1.50**. Investing gave an average gain of **25 cents** per round compared with keeping the dollar, so the most profitable strategy was to **invest on every round**.

**Results.**

| Group | Rounds invested |
|---|---|
| Damage to emotion regions | **84%** |
| Damage to other regions | **61%** |
| Healthy controls | **58%** |

The emotion-damaged patients did best. The key pattern (Figure 13.8): the other two groups were much **less likely to invest after a loss** on the previous round than after a gain, whereas the emotion-damaged patients' decisions were **completely unaffected** by the previous outcome.

**Conclusion.** An emotion such as anxiety can stop us maximising profit by making us overly concerned about losses and too afraid of risk.

**But emotion is not simply harmful (Seo & Barrett, 2007).** In an internet-based stock investment simulation, investors who experienced **more intense** feelings made **better** decisions than those with less intense feelings. The best performers understood their emotions well and kept them from directly driving their choices. What matters is how emotion is understood and regulated, not merely how much of it there is.

### Omission bias and status quo bias

Emotion also shows up as a preference for not acting.

#### Omission bias

**Omission bias** is a preference for risking harm through **inaction** over risking harm through **action**. Harm that follows from something we did feels worse, and more blameworthy, than equal or greater harm that follows from something we failed to do.

- **Vaccination (Brown et al., 2010).** British parents answering questions about vaccinating their children against various diseases were willing to accept a **higher risk** of their child getting the **disease** than of their child suffering an **adverse reaction to the vaccine**.
- **Anticipated regret (Wroe et al., 2005).** In a similar study, parents said they would expect to feel more responsibility and regret if they vaccinated and something went wrong than if they did not vaccinate.
- **Experts too (Aberegg et al., 2005).** **Pulmonologists** (lung-disease specialists) were given scenarios about evaluating **pulmonary embolism** and treating **septic shock**. When "do nothing" was available as an option, they chose the best management strategy **less** often than when it was not available: **40% versus 59%**. That is strong omission bias in experts.
- **Not universal (Baron & Ritov, 2004).** In a vaccination study, **58%** of participants showed omission bias, but **22%** showed the opposite, **action bias**, guided by a rule along the lines of "don't just sit there, do something".

#### Status quo bias

**Status quo bias** is a preference for keeping the current state of affairs rather than changing a decision. **Samuelson and Zeckhauser (1988)** found that many people kept the **same allocation of their retirement funds** year after year, even when changing would have cost them nothing.

**Nicolle et al. (2011)** found status quo bias on a difficult **perceptual** decision task. Mistakenly **rejecting** the status quo produced stronger **regret** than mistakenly **accepting** it, and mistaken rejection was associated with greater activation in regret-related regions, the **medial prefrontal cortex** and **insula**.

#### Anderson's rational-emotional model (2003)

**Anderson (2003)** proposed a **rational-emotional model** of **decision avoidance**, covering both omission bias and status quo bias. Both biases are explained by **regret** and **fear**. Regret matters for the reasons above: an action that turns out badly is more regrettable than inaction. Fear matters because postponing or avoiding a decision reduces fear for the time being.

**Problems with the model.**

1. In the **short term** people often feel more regret for errors of **action** than of inaction, but in the **long term** the reverse is frequently true (**Leach & Plaks, 2009**): we come to regret the things we did not do. The model struggles to explain this reversal.
2. Status quo bias appears even for **trivial** decisions, such as whether to switch television channels (**Esteves-Sorenson & Perretti, 2012**). It is hard to believe regret or fear explains staying on the same channel.

> **Trap.** Three look-alike biases. **Sunk-cost effect**: continuing because of what has already been *invested* (Dawes, 1988, the $100 resort deposit). **Omission bias**: preferring *inaction* when both acting and not acting carry risk (vaccination; Aberegg's pulmonologists 40% versus 59%). **Status quo bias**: preferring to *keep the current state* (Samuelson & Zeckhauser, 1988, retirement funds). Anderson's (2003) model covers omission and status quo bias (decision avoidance), not sunk cost. The opposite of omission bias is **action bias** (Baron & Ritov, 2004: 58% omission, 22% action).

### Social factors

#### Tetlock's social functionalist approach (2002)

**Tetlock (2002)** stressed social factors. In his **social functionalist approach**, people often act like **intuitive politicians**: they are accountable to various constituencies, and their long-term success at managing impressions depends on anticipating the objections others are likely to raise to alternative courses of action. Decisions are shaped by the need to be able to **justify** them.

**Accountability strengthens the sunk-cost effect (Simonson & Staw, 1992).** In a sunk-cost study, some participants were told their decisions would be shared with other students and instructors (**high accountability**); others were told their decisions would be confidential (**low accountability**). The high-accountability participants were **more** likely to stick with their previously unsuccessful course of action, showing a **stronger** sunk-cost effect, because they felt a greater need to justify their earlier decisions.

**Accountability affects experts (Schwartz et al., 2004).** Medical experts chose a treatment for a patient with **osteoarthritis**. Their decisions were **more biased** when they were made accountable, by having to write an explanation and agreeing to be contacted later to discuss it.

**Limitations of the social functionalist approach.**

1. It de-emphasises **individual differences** in how strongly people feel the need to justify themselves.
2. Most of the research uses laboratory tasks that make no real demands on social responsibility.

> **Trap.** Intuition says accountability should make decisions *better*. In these studies it made them **worse**: stronger sunk-cost effect (Simonson & Staw, 1992) and more biased treatment choices by doctors (Schwartz et al., 2004). "Intuitive politicians" is **Tetlock (2002)**, the social functionalist approach.

---

## 13.6 Complex Decision Making

### Why the laboratory is not enough

So far the decisions have been simple: a coin toss, two programmes, a pair of cities. Real life also brings important, complex decisions, such as a doctor's diagnostic decision (which can be a matter of life or death; see Chapter 12) or whether to marry a particular person or emigrate. The book notes **two important differences** between laboratory and real-world decision making:

1. Real-world decisions usually have **far more serious consequences**.
2. Laboratory participants typically make a **single** decision, whereas in real life we make a **series** of decisions over time in pursuit of long-term goals, such as building a career.

The focus here is on the **strategies** people use for complex decisions, starting with an approximation to the ideal.

### Multi-attribute utility theory (Wright, 1984)

According to **multi-attribute utility theory** (MAUT; **Wright, 1984**), a decision maker should go through **five stages**:

1. **Identify** the attributes relevant to the decision.
2. **Weight** those attributes by importance.
3. **List** all the options under consideration.
4. **Rate** each option on each attribute.
5. **Compute** a total utility for each option (its subjective desirability, obtained by summing its weighted attribute ratings) and choose the option with the highest total.

Applied to renting a flat: identify the relevant attributes (number of rooms, location, weekly rent), work out how much each matters, then compare the flats on total weighted utility and take the highest scorer. Because every attribute contributes to the total, a weakness on one attribute can be offset by a strength on another; in the wider literature this is called a **compensatory** strategy (and the weighted sum is often called the **weighted additive** or weighted averaging rule).

MAUT will often yield the best decision, **provided all options are listed and the criteria are independent of each other**. But people rarely use it in real life, for three reasons:

1. It can be **very complex**.
2. The full set of relevant dimensions **cannot always be identified**.
3. The dimensions may **not be clearly separable** from one another.

### Bounded rationality and satisficing (Simon, 1957)

**Herbert Simon (1957)** offered a far more realistic account. Decision-making ability is limited by **processing limitations**, such as the small capacity of short-term memory. Hence **bounded rationality**: decision making is "bounded" by **environmental constraints** (for example, the cost of obtaining information) and by **cognitive constraints** (for example, limited attention). In short, we are as rational as the environment and our limited minds allow. Chapter 14 discusses the concept more fully.

In practice, bounded rationality leads to **satisficing**, a word Simon formed by blending *satisfactory* and *sufficing*. Satisficing means choosing the **first option that meets your minimum requirements**, rather than searching for the best possible option. It does not guarantee the best decision, but it is especially useful when options appear **at different times**, so they cannot all be compared at once, as with potential romantic partners.

**Classic background.** Some keys date bounded rationality and satisficing to Simon's 1955 or 1956 papers; this edition cites **Simon (1957)**.

#### Satisficers versus maximisers (Schwartz et al., 2002; Roets et al., 2012)

**Schwartz et al. (2002)** distinguished **satisficers** (content with reasonably good decisions) from **maximisers** (perfectionists who seek the best). Satisficers came out ahead on well-being: they were **happier** and **more optimistic**, had **greater life satisfaction**, and experienced **less regret and self-blame**.

But that study sampled only **Americans**, and the advantage does not travel. **Roets et al. (2012)** found **no well-being difference** between maximisers and satisficers in **China**. Their explanation is cultural: the pressure to pick the optimal option is weaker in Chinese than in American society, so falling short of the best choice carries less psychological cost.

> **Trap.** **Bounded rationality** and **satisficing** are **Simon (1957)**. **Elimination by aspects** is **Tversky (1972)**. **Multi-attribute utility theory** is attributed to **Wright (1984)** in this chapter. The **satisficer versus maximiser** distinction is **Schwartz et al. (2002)**, and its cultural limit is **Roets et al. (2012)**. Do not let "Schwartz" slide into Simon.

### Elimination by aspects (Tversky, 1972)

**Tversky (1972)** proposed a theory similar in spirit to Simon's. According to **elimination-by-aspects** theory, decision makers eliminate options by considering **one relevant attribute (aspect) at a time**. A house buyer might first consider location and eliminate every house outside a chosen area, then consider price and eliminate every remaining property above a certain figure, and so on, attribute by attribute, until **only one option remains**. Unlike MAUT, this is non-compensatory: a house that fails on location is gone, however cheap or beautiful it is.

**The main problem**: the option finally chosen depends on the **order** in which attributes are considered, so the choice may not be the best one. A superb house just outside the first-considered area never gets a hearing.

#### Kaplan et al.'s two-stage theory (2011)

**Kaplan et al. (2011)** modified Tversky's theory into a **two-stage theory**:

1. **Stage 1**, resembling elimination by aspects: only options meeting certain criteria are retained, cutting the set down to a **manageable number**.
2. **Stage 2**: detailed comparison of the **patterns of attributes** of the retained options. Such detailed comparisons are only feasible for a small number of options, which is why stage 1 is needed.

#### Findings on strategy use

**Payne (1976): strategy changes as the set shrinks.** Students chose among flats using information about attributes such as rent and distance from campus. With **many** flats, they typically began with a **simple** strategy such as **satisficing or elimination by aspects**. When only a **few** flats remained, they often switched to a **more complex** strategy resembling **MAUT**.

**Kaplan et al. (2011): support for two stages.** Students chose an apartment after searching information on **600** apartments. In the first stage, the three most popular criteria for keeping or dropping apartments were **location**, **walking time to the university** and **rental price**. In the second stage, participants made more complex calculations: the importance they gave to low rent depended on other factors. Low rent mattered most for participants who had **little price knowledge**, went to the university **frequently**, and had **often searched** for apartments in recent years.

**Lenton and Stewart (2008): online dating.** Single women chose from a real dating website with **4, 24 or 64** potential mates. As the number of options rose, the women shifted from complex to simple strategies.

| Strategy | With 4 potential mates | With 64 potential mates |
|---|---|---|
| Weighted averaging (MAUT-like) | **81%** | **41%** |
| Elimination by aspects | **39%** | **69%** |
| Satisficing | **6%** | **16%** |

The percentages in each column add to more than 100% because many women used more than one strategy.

**Lenton and Francesconi (2010): speed dating.** At **large** speed-dating events, decisions were driven mostly by **easily assessed** attributes (age, height, weight) rather than harder-to-assess ones (occupation, academic achievements). At **small** events, the reverse held. The likely reason is the greater **cognitive load** at large events.

#### Evaluation of elimination by aspects

Elimination by aspects works reasonably well when people must choose among **many** options. With **few** options, people often switch to a MAUT-like approach. So elimination by aspects is best seen as a useful **early filter**, less valuable at later stages. A further limitation is that it ignores our preference for options that **share many attributes with other options**; **Won (2012)** showed that adding this preference to the model improves its predictions.

> **High-yield.** The consistent pattern across Payne (1976), Kaplan et al. (2011), Lenton and Stewart (2008) and Lenton and Francesconi (2010): **many options or high load → simple, non-compensatory strategies** (elimination by aspects, satisficing, easily assessed attributes); **few options → complex, compensatory strategies** (MAUT-like weighted averaging). People are adaptive strategy switchers.

### Changing preferences and facts

Most theories assume that a person's assessment of the utility of an attribute (its desirability multiplied by its importance) stays **constant** during a decision. **Simon et al. (2004)** tested this. (Note: this is **Dan Simon** and colleagues, not Herbert Simon.) Participants chose between job offers from two department store chains on the basis of **four** attributes, such as salary and commuting time. After they had rated their preferences, they were told one job had a much better **location**, which often led them to choose that job. When they then **re-rated** their preferences, ratings of the chosen job's desirable attributes had **increased** and ratings of its undesirable attributes had **decreased**. Preferences shift to fit the decision, contrary to the constancy assumption.

Decisions can even distort memory for **facts**. **Svenson et al. (2009)** had advanced **nursing students** decide whether a male or a female patient should get surgery, when resources allowed only one operation. Afterwards, their memory for objective facts (such as life expectancy without surgery and the probability of surviving surgery) was **distorted in the direction that increased support** for the decision they had made.

### Selective exposure

**Selective exposure** is the tendency to prefer information that is **consistent** with one's existing beliefs and to avoid information that conflicts with them. It is an important source of poor decisions.

**Fischer and Greitemeyer's (2010) model** (Figure 13.9) specifies when it increases or decreases:

| Motivation | Effect on selective exposure |
|---|---|
| **High defence motivation** (a need to defend one's own position) | **Increases** selective exposure |
| **High accuracy motivation**, but only a **restricted** amount of information may be accessed | **Increases** selective exposure |
| **High accuracy motivation** produced by instructions to make the **best choice** | **Reduces** selective exposure |

All of these effects were reported in a **meta-analysis by Hart et al. (2009)**.

> **Trap.** Accuracy motivation cuts **both ways** in this model. When it is triggered by the goal of making the optimal *decision*, it **reduces** selective exposure; when it operates during an information *search* that is restricted, it **increases** selective exposure. Defence motivation always increases it. Selective exposure (preferring belief-consistent information while choosing) is closely related to **confirmation bias** in reasoning (Chapter 14), but the term used in this chapter is selective exposure.

### Naturalistic decision making

Because so much laboratory research is artificial, there has been strong interest in **naturalistic decision making**, the study of the processes involved in real-life decisions.

#### Galotti's five-phase theory (2002)

**Galotti (2002)** proposed that naturalistic decisions involve **five phases**:

1. **Setting goals**
2. **Gathering information**
3. **Structuring the decision** (listing the options and the criteria for choosing among them)
4. **Making a final choice**
5. **Evaluating the decision**

The book's Figure 13.10 (lost from the PDF) emphasises that the **order is flexible**: many decision makers loop back to earlier phases when they are struggling. It is not a rigid one-way sequence.

#### Galotti (2007): what real decision structuring looks like

The key phase is **decision structuring**. **Galotti (2007)** reviewed **five studies** of important real-life decisions (for example, students choosing a college and college students choosing their main subject). The findings:

1. Decision makers limited the information they considered, focusing on **two to five options (mean four)** at any one time.
2. The number of options considered **decreased** over time.
3. They considered **three to nine attributes (mean six)** at any one time.
4. The number of attributes did **not** decrease over time, and sometimes **increased**.
5. People of **higher ability and/or more education** considered **more attributes**.
6. Most of the real-life decisions were judged to be **good** ones.

**What it shows.** The most striking result is that people consistently **limited** the information (options and attributes) they considered. That is **inconsistent with MAUT**, which requires considering everything, but **consistent with Simon's bounded rationality**. In addition, the number of options **fell by 18%** over several months; Tversky's elimination-by-aspects theory predicts a reduction, but a **larger** one than Galotti found.

**Galotti and Tinkelenberg (2009): parents choosing a school.** Parents choosing a first-grade school placement for their child focused on a restricted set of options, typically **three** out of **eight or more** available, and usually considered only about **five** criteria at a time. But their decision making was **dynamic**: over a **six-month** period, on average **one-third** of the options and **over half** of the criteria changed.

#### Individual differences in search (Crossley & Highhouse, 2005)

People differ markedly in their naturalistic strategies. **Crossley and Highhouse (2005)** studied how people searched for and chose a job, and identified **three** information-search strategies:

1. **Focused search**: concentrating on a small number of carefully selected potential employers.
2. **Exploratory search**: considering several job options and using several sources of information (friends, employment centres and so on).
3. **Haphazard search**: an unsystematic, trial-and-error approach.

**Focused search** correlated **positively** with satisfaction with the job-search process and with job satisfaction. **Haphazard search** correlated **negatively** with both.

### Expert decision making: Klein's recognition-primed decision model

How do experts make decisions at work, especially when decisions must be fast (a forest fire, a battlefield)? The influential answer is **Klein's recognition-primed decision (RPD) model** (for example **Klein, 1998, 2008**). The book's Figure 13.11 (from Patterson et al., 2009) is lost, so here is the model as a flow:

1. **Is the situation perceived as familiar or typical?**
2. **If yes:** the expert matches the situation to learned patterns in long-term memory by **pattern recognition**. This fast, automatic process usually retrieves a **single option**, and the situation confirms the expert's expectancies.
3. The expert runs a **mental simulation**: imagining what would happen if that option were carried out.
4. If the imagined outcome is **satisfactory** (as it usually is for experts), the option is **implemented** at once. If not, it is modified or another option is retrieved.
5. **If the situation is not typical, or expectancies are violated:** the expert **diagnoses** the situation further, for example by **story building** and **collecting more data**, before deciding.

**Support.** **Klein (1998)** analysed **over 600** decisions by various experts (for example fire commanders and military commanders). They generally considered only **one option at a time**. Even with a novel situation, experts typically categorised it quickly as an instance of a familiar type and then simply retrieved the appropriate action from long-term memory. There is no weighing of alternatives in the MAUT sense.

**Mixed support (Turpin & Marais, 2004).** In interviews with **six** prominent decision makers, **three** relied heavily on intuition, consistent with the model. The other three were less consistent with it: they preferred a reasonable decision today over a better decision later, which looks more like **satisficing**.

**Reconciling Klein and Kahneman (Kahneman & Klein, 2009).** The RPD model emphasises how **accurate** human judgement and decision making can be, whereas Kahneman's heuristics-and-biases approach emphasises **error**. **Kahneman and Klein (2009)** pointed out that the difference arises largely because the RPD model applies to **experts** and the heuristics-and-biases approach does not. On average, experts make better decisions than non-experts.

**Limitations of the RPD model.**

1. It was explicitly designed for **experts in crisis situations under severe time pressure**, which helps explain why it failed to predict the behaviour of some of Turpin and Marais's decision makers.
2. It gives a **general outline** with few specific details. For example, when a crisis seems unfamiliar, experts are said to clarify and diagnose, but the actual processing will vary greatly with the type of crisis and with the expert's personality and knowledge.

> **Trap.** In the RPD model the expert typically considers **one option at a time** and evaluates it by **mental simulation**, not by comparing several options side by side. An option describing "generating and comparing several alternatives on weighted attributes" describes **MAUT**, not Klein. Kahneman and Klein (2009) is a **reconciliation** paper, not a refutation of either side.

### Unconscious thought theory (Dijksterhuis & Nordgren, 2006)

**The claim.** Most people assume conscious thinking is best for complex decisions and that unconscious thinking, if it helps at all, helps with simple ones. **Dijksterhuis and Nordgren (2006)** argued the **opposite** in their **unconscious thought theory**. Conscious thought is constrained by the **limited capacity of consciousness**, so **unconscious thought is better at integrating large amounts of information**. But only conscious thought can follow **strict rules**, so conscious thought is best for **rule-based** problems such as mathematics.

#### Findings

**Dijksterhuis et al. (2006): the car study.** All participants read information about **four** hypothetical cars. In the **simple** condition each car was described on **4** attributes; in the **complex** condition, on **12**. Participants then either thought about the cars for **four minutes** (conscious thought) or spent four minutes solving **anagrams** before choosing (unconscious thought, since attention was occupied elsewhere). As predicted, choices were **better after unconscious thought when the decision was complex**, but **better after conscious thought when it was simple**.

**Nieuwenstein and van Rijn (2012): weak replication.** Reviewing similar studies, they found that unconscious thought beat conscious thought in only **45%** of experiments.

**Nordgren et al. (2011): combine the two.** Participants chose the best of **12** apartments.

| Condition | Chose one of the best apartments |
|---|---|
| Conscious thought only | **26%** |
| Unconscious thought only | **28%** |
| Conscious thought followed by unconscious thought | **57%** |

As predicted, combining the two produced much better decisions.

#### Doubts about unconscious thought (Newell & Shanks, 2014)

**Newell and Shanks (2014)** questioned whether the positive findings really show unconscious thought is superior. In most studies, participants in the conscious condition had to think for several minutes while relying on their **fragmentary memory** of information presented earlier. That procedure probably **underestimates** the value of conscious thought.

**Payne et al. (2008): forced long deliberation is the problem.** Some participants engaged in conscious thought for a fixed **four minutes**; others decided for themselves how long to think (**self-paced**). Self-paced participants, who spent about **20 seconds** on average, **outperformed** the four-minute conscious group and did **as well as** the unconscious thought group. So forcing people to deliberate for a long time impairs their decisions; it is not that conscious thought is inherently worse.

**Mamede et al. (2010): experts do better with conscious thought.** Most of this research uses non-experts. **Mamede et al. (2010)** asked **medical experts** to diagnose **simple** and **complex** cases either immediately, after conscious thought, or after unconscious thought (deliberation-without-attention, involving distraction). With **simple** cases, accuracy did not differ across conditions. With **complex** cases, accuracy was **best after conscious thought** (Figure 13.12), the **opposite** of what unconscious thought theory predicts. Mamede et al. argued that experts possess extensive, well-organised knowledge that they can search effectively by deliberate, conscious retrieval from long-term memory.

#### Evaluation of unconscious thought theory

**Strengths.** The theory has focused attention on the strengths and limitations of both conscious and unconscious thought. Unconscious thought sometimes does produce better decisions than conscious thought, and decisions can be best of all when the two are combined (Nordgren et al., 2011).

**Limitations.**

1. The findings are **inconsistent** (Nieuwenstein & van Rijn, 2012: only 45% of experiments).
2. Forcing participants to spend several minutes in conscious thought probably **reduces** its value (Payne et al., 2008).
3. Conscious thought can be **much more useful** than unconscious thought when **experts** make complex decisions (Mamede et al., 2010).
4. The theory assumes unconscious-thought participants rely heavily on intuitive processes, but such participants say they rely mostly on **conscious memory** (**Aczel et al., 2011**).


---

## How the chapter fits together

1. **Norms versus behaviour.** Every "bias" is a gap between a normative standard and what people do: Bayes' theorem (base-rate neglect, conjunction fallacy), expected utility (loss aversion, framing, sunk cost), MAUT (satisficing, elimination by aspects). Always ask which norm a finding is measured against.
2. **Is it the mind or the task?** Apparent irrationality shrinks when the task changes: causal structure (Krynski & Tenenbaum), frequency formats (Fiedler; Hoffrage), complete descriptions (Mandel & Vartanian), full information (Baliga & Ely), open sampling (Hilbig & Glöckner). Biased input, not biased processing, explains many "errors" (Juslin et al.; Le Mens & Denrell).
3. **Heuristics are double-edged.** Kahneman and Tversky stress the errors, Gigerenzer the accuracy (hiatus heuristic 83% versus 75%), Klein the power of expert pattern recognition; Kahneman and Klein (2009) reconcile them by noting that the RPD model is about experts.
4. **Two kinds of processing, but not two tidy systems.** System 1 versus System 2, unconscious versus conscious thought, recognition-primed versus deliberate diagnosis. Each clean split breaks down: base rates are processed intuitively (De Neys; Pennycook & Thompson), conscious thought helps experts (Mamede), and combining modes works best (Nordgren et al.).
5. **Emotion is not noise.** Loss aversion may rest on impact bias; the amygdala brakes risky choice; regret drives omission and status quo bias; reduced emotion helped on one gambling task (Shiv) while well-understood intense emotion helped investors (Seo & Barrett).
6. **Decisions are social and dynamic.** People justify choices to others (Tetlock), accountability can worsen bias, preferences and remembered facts reshape themselves after a choice (Simon et al.; Svenson et al.), and real decisions unfold over months (Galotti).

---

## Worked example

*A 52-year-old schoolteacher is referred to a hospital psychiatry OPD with "?panic disorder": three months of sudden episodes of pounding heartbeat, breathlessness and a sense of doom lasting several minutes. He is slim, active and a non-smoker, with a normal ECG last year. The clinical psychology trainee who sees him has assessed many young adults with panic disorder in the past fortnight. He also screens positive on the ward's brief depression questionnaire. Later the team debates continuing a medication that has not helped in twelve weeks, and he is reluctant to try a new drug because of a rare side effect.*

**What threatens the diagnosis?** Both Groopman patterns. **Availability**: a fortnight of panic cases makes "panic" spring to mind, as weeks of pneumonia did for Dr Alter. **Representativeness**: he looks fit and low-risk, as McKinley did for Dr Croskerry, so a cardiac cause is dismissed by resemblance. The corrective is to ask about **base rates**: how often does panic first appear in the early fifties, compared with arrhythmia, thyroid disease or other medical causes of these symptoms at his age? (Clinically, late first onset of panic is a recognised red flag.)

**Using support theory on purpose.** Spelling out alternatives raises the probability doctors give them (Redelmeier et al., 1995: 0.50 to 0.69). Writing an explicit differential (arrhythmia, hyperthyroidism, hypoglycaemia, caffeine or substance effects, other) stops the residual category being underweighted.

**What does the positive screen mean?** With illustrative numbers (not from the book): the screen detects 80% of depressed patients, gives false positives in 20% of others, and 10% of the ward is depressed. A colleague's "80% likely" is the **taxi-cab error**. In natural frequencies: of 1,000 patients, 100 are depressed and 80 screen positive; of 900 others, 180 screen positive; so 80 of 260 positives, about **31%**, are depressed. In odds form: 1:9 × 4 = 4:9, that is 4/13, the same answer. The frequency version is easier largely because it lays out the set structure (Evans et al., 2000).

**Why continue the failed drug?** The **sunk-cost effect**, possibly strengthened by **accountability** at a case conference (Simonson & Staw, 1992; Schwartz et al., 2004). Remedies: re-decide with full information on current costs and benefits (Baliga & Ely, 2011) and lean on expertise (Braverman & Blumenthal-Barby, 2012).

**Why does the patient refuse the new drug?** **Omission bias** and anticipated regret for action (Brown et al., 2010; Wroe et al., 2005); **status quo bias**; **overweighting a rare event** presented as a description (Hertwig et al., 2004); **impact bias** about how bad the side effect would feel (Kermer et al., 2006); and, as an anxious man, heightened loss aversion (Shiv et al., 2005). Present both frames ("90 of 100 improve" and "10 of 100 do not"), use natural frequencies, and have him list pros and cons and justify his choice, which removed framing in Almashat et al. (2008).

**The consultant's "I know this pattern".** Klein's recognition-primed process suits typical cases, but late onset **violates expectancies**, which in the RPD model is the cue to diagnose further. For complex cases, doctors were most accurate after **conscious** deliberation (Mamede et al., 2010), so think it through rather than "sleep on it".

---

## MCQ traps

1. **Judgement = accuracy; decision making = consequences**; a good decision can still have a bad outcome.
2. **Taxi-cab (Kahneman & Tversky, 1972):** 85% Green, 15% Blue, witness wrong 20%; odds **12:17**, probability **41%**; popular answer **80%**.
3. **Lawyer-engineer (Kahneman & Tversky, 1973):** 70:30 versus 30:70; Jack rated **0.90** engineer either way (base-rate neglect).
4. **Linda (Tversky & Kahneman, 1983)** is the **conjunction fallacy**; survives careful wording (**Sides et al., 2002**); **Tentori et al. (2013)** black shoes favour a confirmation account.
5. **Croskerry/McKinley = representativeness; Alter/Begaye (aspirin toxicity read as viral pneumonia) = availability**; both **Groopman (2007)**.
6. **Krynski & Tenenbaum (2007):** faded paint cut base-rate neglect **43% → 8%** and raised correct answers **8% → 46%**; their mammogram is **2% / 6%**.
7. **Ditto et al. (1998):** the **1 in 10** misleading-test rate was invoked only for bad news.
8. **Lichtenstein et al. (1978):** **murder** judged likelier than **suicide**. **Pachur et al. (2012):** **direct experience** best predictor, **media** worst.
9. **Oppenheimer & Monin (2009):** under load the famous surname was picked **80%** of the time.
10. **Intelligence is almost unrelated** to Linda and lawyer-engineer performance (**Stanovich, 2012**).
11. **Lerner et al. (2003):** **fear** (not sadness or anger) raised terrorism-risk estimates.
12. **Support theory (Tversky & Koehler, 1994):** unpacking **raises** probability: **Mandel (2005)** 0.30 versus 0.30 + 0.18; **Redelmeier et al. (1995)** **0.50 → 0.69** in doctors.
13. **Exceptions:** **Sloman et al. (2004)** atypical diseases **0.55 → 0.40**; **Redden & Frederick (2011)** "2, 4 or 6" felt less likely than "even".
14. **"If we're so dumb, how come we're so smart?"** is **Glymour (2001)**.
15. **Take-the-best:** search by validity, **stop at the first discriminating cue**, decide (Cologne versus Herne).
16. **Goldstein & Gigerenzer (2002):** recognition used **90%**; **92%** despite a conflicting football cue. Use tracks validity, **r = +0.64** (Pachur et al., 2012).
17. **Hiatus heuristic (Wübben & van Wangenheim, 2008):** **83%** versus **75%** = less-is-more.
18. **Richter & Späth (2006):** **98%** with airport, **82%** without. **Newell et al. (2003):** only **33%** used full take-the-best. **Dieckmann & Rieskamp (2007):** take-the-best under **high** redundancy.
19. **Fiedler (1988):** frequency Linda cut the fallacy by **two-thirds**; **Hoffrage et al. (2000):** **four** tasks, advanced medical students.
20. **Fiedler et al. (2000):** 1%, 80%, 9.6%; estimate **63%**, correct **7.8%**. **Evans et al. (2000):** advantage vanishes when structure is equally clear.
21. **De Neys (2006):** correct answers almost **40% slower**; load **17% → 9.5%** (supports Kahneman). **De Neys et al. (2008):** **ACC** conflict signal (challenges him).
22. **Pennycook & Thompson (2012):** **995 nurses, 5 doctors**; about **half** of first answers used the base rate; **30%** versus **23%** shifts.
23. **Chun & Kruglanski (2006):** load increased use of the **briefly presented** information, whatever its content; fits **De Neys's (2012) logical intuition model**.
24. **Expected utility (von Neumann & Morgenstern, 1944)**, **SEU (Savage, 1954)** = normative; **prospect theory (1979, 1984)** = descriptive.
25. **Tversky & Shafir (1992):** +$200 / −$100 coin toss refused by **two-thirds**. A 50:50 bet needs a win about **twice** the loss (**Kahneman, 2003**).
26. **Risk averse for gains, risk seeking for losses**; loss aversion is not the same as risk aversion.
27. **Asian disease (Tversky & Kahneman, 1981):** 600 at risk; **72%** certain A (gain frame), **78%** risky D (loss frame).
28. **Mandel & Vartanian (2011):** framing vanishes when all options are fully described; **Almashat et al. (2008):** pros-and-cons listing removed it; **Wang (1996):** strangers versus close relatives.
29. **Sunk cost:** **Dawes (1988)** $100 deposit; MBA students with full information showed the **opposite** (Baliga & Ely, 2011).
30. **Description → overweighting; experience → underweighting** (Hertwig et al., 2004); **open sampling → accurate** (Hilbig & Glöckner, 2011). Jackpot **1 in 14 million**.
31. **Pope & Schweitzer (2011):** **2.5 million** putts, **94%** loss averse, par putts less often short. Financiers **less loss averse** than students (Abdellaoui et al., 2013).
32. **Loss neutrality (Yechiam & Hochman, 2013):** ±£1 versus ±£5; attentional model.
33. **Kermer et al. (2006) impact bias:** win $5 / lose $3; the loss hurt **less** than forecast.
34. **Giorgetta et al. (2013):** regret (own loss) riskier than disappointment; **elation** (computer win) riskier than rejoicing.
35. **Weller et al. (2007):** vmPFC → risk seeking for **gains and losses**; amygdala → **gains only**. **SP and AP** (De Martino et al., 2010): no loss aversion.
36. **Shiv et al. (2005):** invested **84% / 61% / 58%** (emotion damage / other damage / controls).
37. **Aberegg et al. (2005):** pulmonologists **40% versus 59%**; **Baron & Ritov (2004):** **58%** omission, **22%** action bias.
38. **Simonson & Staw (1992):** accountability **strengthened** sunk cost; "intuitive politicians" = **Tetlock (2002)**.
39. **MAUT = Wright (1984); bounded rationality and satisficing = Simon (1957); elimination by aspects = Tversky (1972).** Lenton & Stewart (2008): weighted averaging **81% → 41%** from 4 to 64 mates.
40. **Galotti (2007):** options **2 to 5 (mean 4)**, attributes **3 to 9 (mean 6)**, options fell **18%**. **Klein (1998):** over **600** decisions, one option at a time. **Dijksterhuis et al. (2006):** 4 versus 12 attributes; replicated in only **45%** (Nieuwenstein & van Rijn, 2012); **Nordgren et al. (2011):** **26% / 28% / 57%**; **Payne et al. (2008):** self-paced about **20 s**.

---

## Key terms

| Term | Definition |
|---|---|
| **Judgement** | Estimating how probable an event is from incomplete information |
| **Decision making** | Choosing among options; needs judgement whenever information is incomplete |
| **Base-rate information** | How often an event or category occurs in the relevant population |
| **Bayes' theorem** | Posterior odds equal prior odds multiplied by the likelihood ratio |
| **Heuristic** | A rule of thumb that uses part of the information to save effort |
| **Representativeness heuristic** | Assigning something to a category because it looks typical of it |
| **Conjunction fallacy** | Judging two events together as likelier than one of them alone |
| **Availability heuristic** | Estimating frequency from how easily instances come to mind |
| **Affect heuristic** | Letting an emotional reaction, such as dread, drive a quick judgement |
| **Support theory** | Judged probability depends on how explicitly an event is described (Tversky & Koehler, 1994) |
| **Take-the-best** | Check cues in order of validity and decide on the first that discriminates |
| **Recognition heuristic** | If only one of two objects is recognised, judge it the higher on the criterion |
| **Hiatus heuristic** | Customers count as active only if they bought something fairly recently |
| **Natural sampling** | Meeting instances one at a time and keeping counts, rather than receiving summary statistics |
| **System 1 / System 2** | Fast, automatic, implicit processing / slow, serial, effortful, controlled processing |
| **Prospect theory** | Outcomes coded as gains or losses from a reference point, losses weighted more |
| **Loss aversion** | Greater sensitivity to a potential loss than to an equal potential gain |
| **Framing effect** | A choice changing with irrelevant features of presentation such as wording |
| **Sunk-cost effect** | Adding resources to a failing course of action to justify past investment |
| **Loss neutrality** | No preference between options with symmetrical gains and losses of different sizes |
| **Neuroeconomics** | Studying economic decisions with the tools of cognitive neuroscience |
| **Impact bias** | Overestimating how intense and lasting the distress from a loss will be |
| **Omission bias** | Preferring to risk harm through inaction rather than through action |
| **Status quo bias** | Preferring to keep the present state rather than change a decision |
| **Social functionalist approach** | Tetlock's view of people as intuitive politicians who must justify their choices |
| **Multi-attribute utility theory** | Weight attributes, rate every option on each, sum, and pick the highest total |
| **Bounded rationality** | Rationality limited by the environment and by limited processing capacity |
| **Satisficing** | Taking the first option that meets one's minimum requirements |
| **Elimination by aspects** | Discarding options one attribute at a time until one remains |
| **Selective exposure** | Favouring information that supports existing views and avoiding conflicting information |
| **Recognition-primed decision model** | Klein: experts recognise the situation, retrieve one option, and test it by mental simulation |
| **Unconscious thought theory** | Unconscious thought integrates complex information better than conscious thought (Dijksterhuis & Nordgren, 2006) |

---

## Likely exam points

1. Judgement (accuracy) versus decision making (consequences).
2. Bayes' theorem in odds form; taxi-cab answer 41%.
3. Base-rate neglect: taxi-cab (1972), lawyer-engineer (1973).
4. Representativeness and the Linda conjunction fallacy (1983); Sides et al. (2002); Tentori et al. (2013).
5. Conditions for base-rate use: causal knowledge (Krynski & Tenenbaum, 2007) and motivation (Ditto et al., 1998).
6. Availability: Lichtenstein et al. (1978); Pachur et al. (2012); Oppenheimer (2004) and Oppenheimer and Monin (2009).
7. Groopman's (2007) two medical cases and the heuristic behind each.
8. Four limitations of the heuristics-and-biases approach; intelligence nearly unrelated (Stanovich, 2012).
9. Support theory, its supporting studies and its two exceptions.
10. Take-the-best's three rules and the recognition heuristic (90%, 92%, +0.64).
11. Less-is-more: hiatus heuristic 83% versus 75%.
12. Limits of fast-and-frugal heuristics (Richter & Späth; Newell et al.; Bröder; Dieckmann & Rieskamp; Evans & Over).
13. Natural frequency hypothesis, its support and the Evans et al. (2000) confound.
14. Fiedler et al. (2000): 63% versus 7.8%.
15. Kahneman's System 1 and System 2 and the serial relation.
16. Evidence against simple dual-process theory and its five limitations.
17. De Neys's logical intuition model and its three advantages.
18. Expected utility and SEU as normative theories.
19. Prospect theory: reference point, loss aversion, value function, rare-event overweighting.
20. Asian disease problem (72% / 78%) and the three critiques.
21. Sunk-cost effect and its remedies.
22. Description-experience gap and open sampling.
23. Loss aversion in golfers, poker players and financiers.
24. Loss neutrality and the six limitations of prospect theory.
25. Impact bias; regret versus disappointment; rejoicing versus elation.
26. Amygdala and vmPFC lesion findings; Shiv et al. (2005) and Seo and Barrett (2007).
27. Omission and status quo bias; Anderson's (2003) model and its two problems.
28. Tetlock's social functionalist approach and accountability effects.
29. MAUT versus satisficing, elimination by aspects and the two-stage theory; strategy shifts with set size.
30. Post-decision changes, selective exposure, Galotti's naturalistic findings, Klein's RPD model, and unconscious thought theory with its critics.
