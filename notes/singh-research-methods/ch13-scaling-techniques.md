---
date: 2026-05-29
book: "Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh)"
subject: "Research Methodology, Statistics & Psychological Testing"
chapter: 13
tags: [scaling, psychophysics, psychophysical-methods, psychological-scaling, attitude-scales, MET2026, MCQ-prep]
---

# Scaling Techniques

Scaling methods are procedures by which stimuli or individuals are ordered according to specified attributes, yielding a psychological continuum. Chapter 13 distinguishes two broad families: **psychophysical scaling methods** (stimuli have a known physical referent) and **psychological scaling methods** (stimuli possess only psychological attributes with no physical referent). Classical psychophysical methods, Weber's and Fechner's laws, Stevens' Power Law, and attitude-scale construction techniques (Thurstone, Likert, Guttman) are all covered.

---

## Distinction Between Psychophysical and Psychological Scaling Methods

### Psychophysical Scaling Methods

**Psychophysical scaling methods** are methods in which the stimuli presented have a **physical referent** — they can be objectively described by a known physical scale (e.g., grams, decibels, centimeters, minutes). The purpose is to establish the quantitative relationship between the subjective measurement of stimuli (as rated by a subject) and their objective measurement on a physical scale.

- The physical ordering of objects is called the **physical continuum**.
- The ordering of the same objects based on subjects' judgements is called the **psychological continuum**.
- The field is named **psychophysics**, a term coined by **G.T. Fechner (1801–1887)**, who defined it as *"the exact science of the functional relations of dependency between body and mind."*

### Psychological Scaling Methods

**Psychological scaling methods** deal with stimuli that **cannot be described by a known physical scale** — stimuli possessing only psychological attributes (e.g., sense of humor, quality of beauty, honesty, aggressiveness, pleasantness).

- **Torgerson (1958)**, in *Theory and Methods of Scaling*: *"Psychological scaling methods are procedures for constructing scales for the measurement of psychological attributes."*
- These methods rely on the **judgemental process** of individuals.

---

## Core Concepts in Psychophysical Measurement

### Threshold (Limen)

The concept of **threshold** was first introduced by **Johann Herbart in 1824** ("threshold of consciousness"). The Latin equivalent is **limen**.

**Threshold**: That boundary value on a stimulus dimension separating the stimulus that produces a response from one that makes no response (or a different response).

#### 1. Absolute Threshold (RL — Reiz Limen)

**Absolute threshold** (abbreviated **RL** from the German *Reiz Limen*): The minimal stimulus value that produces a response **50% of the time**.

- **Andreas (1960)**: "A boundary point in sensation, separating sensory experience from no such experience when physical stimulus values reach a particular point."
- RL varies across individuals and situations; statistically defined as the **mean RL over several trials** by the same subject.

#### 2. Difference Threshold (DL — Differenz Limen) / Just Noticeable Difference (JND)

**Difference threshold** (abbreviated **DL** from the German *Differenz Limen*): The difference between two stimuli that can be perceived **50% of the time**.

- Also called **just noticeable difference (JND)**: The smallest detectable difference between two stimuli.
- Two stimuli: **standard stimulus (S)** (constant) and **comparable stimulus (C)** (varied).
- **Lower difference threshold**: C increased from below until it becomes indistinguishable from S.
- **Upper difference threshold**: C decreased from above until it becomes indistinguishable from S.
- **Interval of uncertainty (IU)**: The span between upper and lower thresholds.

**Formula:**
> DL = (Upper threshold − Lower threshold) / 2 = IU / 2

**Key distinction:** RL is a **point** on a stimulus dimension (detected 50% of the time); DL is a **span/range** (amount of change detected 50% of the time).

### Point of Subjective Equality (PSE) and Point of Objective Equality (POE)

- **PSE**: The value of C judged equal to S on average by the subject.
- **POE**: The exact physical value of S.
- In illusions, PSE rarely equals S/POE.

### Constant Error (CE)

**Constant error (CE)**: The systematic tendency to consistently over- or under-judge a comparison stimulus.

**Formula (Woodworth & Schlosberg, 1954):**
> CE = PSE − S  ...(13.1)

- **Negative CE** = underjudgement (subject perceives standard as smaller).
- **Positive CE** = overjudgement (subject perceives standard as larger).

*Example:* Standard = 50 mm, mean setting = 45.5 mm → CE = −4.5 mm (underjudgement).

### Variable Error (VE)

**Variable error**: Unsystematic error from unknown sources (motivation fluctuations, attention, etc.) working in both directions, tending to cancel out. Indexed by the **standard deviation (SD)** of judgements.

### Constant Errors Specific to Method of Limits

| Error | Definition | Effect on Series Means |
|---|---|---|
| **Error of habituation** (perseverance) | Tendency to keep responding "Yes"/"No" after stimulus has changed | Inflates **ascending** series mean over descending |
| **Error of anticipation** (expectation) | Tendency to change response before stimulus change is apparent | Inflates **descending** series mean over ascending |

- These errors work in **opposite directions**; alternating ascending and descending series cancels them.
- Both cannot exist simultaneously in the same subject.

---

## Classical Psychophysical Methods

### 1. Method of Limits

**Other names:** Method of Just Noticeable Difference, **Method of Minimal Changes** (Guilford, 1954 preferred), Method of Serial Exploration.

**Named by: Kraepelin in 1891** — a series ends when the subject reaches the **limit** where they change their judgement.

**Procedure:**
- **Ascending series**: Stimuli increase from below threshold.
- **Descending series**: Stimuli decrease from above threshold.
- For **DL**: Subject reports C as smaller (−), equal (=), or larger (+) than S.
- For **RL**: Subject reports presence or absence of stimulus.
- Experimenter deliberately **varies the starting point** of each series to prevent habitual guessing.

**Computation of RL:**
- Threshold for each series = midpoint between the last value producing one response and the first producing the changed response = **transition point**.
- Mean of all individual thresholds = **mean absolute threshold (RL)**.
- SD of individual thresholds = index of variable error.

*Worked example:* MAT = 8.3, MDT = 7.5 → RL = (8.3 + 7.5)/2 = **7.9**; SD = 0.92. Because MAT > MDT → subject committed **error of habituation** (magnitude = 0.8).

**Computation of DL (weightlifting, S = 105 g):**
> Mean upper threshold = 106.4; Mean lower threshold = 104.5
> IU = 1.9; DL = 0.95
> PSE = 105.45; CE = +0.45 (overestimation)

**Practice and fatigue effects**: Compare mean of first half vs. second half of series. Guilford (1954) recommended **ANOVA** for better analysis.

---

### 2. Method of Constant Stimuli

**Other names:** Method of Right and Wrong Cases (almost obsolete), Method of Frequency.

**Procedure:**
- Fixed constant stimuli presented **multiple times (50–200 each) in random order** (order predetermined but unknown to subject).
- For **RL**: Subject reports perception or non-perception each time.
- For **DL** (**method of constant stimuli differences**): S and C presented in succession; subject reports "greater" or "less." S presented first in half the trials, second in the other half (controls **time error**).

**Key difference from Method of Limits:** Smaller C values may abruptly follow larger C values — no regular progression.

**Two-category vs. Three-category judgement:**
- **Two-category** (yes/no, heavier/lighter): More reliable (Davidson and Cross, 1941). Forces subject to commit; removes ambiguous neutral category; automatically removes "doubtful" responses.
- **Three-category** (heavier/equal/lighter): More natural but less reliable; meaning of neutral category is vague.
- **Proportional division**: When equal/doubtful responses exist in a two-category task, they are divided between the two categories proportionally.

**Cannot control** error of habituation and expectation (unlike Method of Limits) because presentations are random.

#### Methods for Calculating RL

**a) Graphical method**: Plot stimuli vs. % heard; find 50% point; drop perpendicular to x-axis. RL = point on x-axis. (Rough.)

**b) Linear interpolation method**: Find the median by interpolation between the two stimulus values bracketing 50%.

*Criticisms:*
1. Assumes linear relationship between two values (controversial).
2. Uses only two data points.
3. No correct estimate of dispersion.

*SD estimation from interpolation data:* Find Q1 (p = 0.25) and Q3 (p = 0.75); compute Q = (Q3 − Q1)/2; then **SD = 1.4833 × Q**.

**c) Summation method:**
> M = S₁ − 0.5i − i(Σp)   ...(13.2)
> M = S₂ + 0.5i + i(Σd)   ...(13.3)
> SD = i√[Σp − (Σp)²/n]   ...(13.4)
> SD = i√[Σcf − (Σcf)²/n]  ...(13.5)

Where: i = unit stimulus interval; p = proportion of higher-category judgements; d = 1−p; Σp = cumulated proportions.

**DL computation (three-category judgement):**
- Draw two **psychometric functions**: one for "heavier," one for "lighter."
- Upper threshold (U) = stimulus value where "heavier" curve crosses 50%.
- Lower threshold (L) = stimulus value where "lighter" curve crosses 50%.
- DL = (U − L)/2; PSE = (U + L)/2

**DL computation (two-category judgement):**
- Q1 = lower difference threshold; Q3 = upper difference threshold.
- DL = (Q3 − Q1)/2; PSE = (Q1 + Q3)/2

---

### 3. Method of Average Error

**Other names:** Method of Adjustment, Method of Reproduction, Method of Equivalent Stimuli.

**The oldest psychophysical method**; described as "a gift to psychophysics and astronomy."

**Procedure:**
- Subject adjusts C until it appears equivalent to S.
- **Subject controls the stimulus** (not the experimenter — key distinction from Limits and Constant Stimuli).
- Mean of all adjustments = **PSE**; CE = PSE − S.

**Specific constant errors:**

| Error | Definition | Control |
|---|---|---|
| **Movement error** | Bias for moving C inward vs. outward | Counterbalance: set C above S in half the trials (inward movement), below S in other half (outward movement) |
| **Space error** | Bias for left vs. right spatial position | Counterbalance: present C to right of S in half the trials, to left in other half |

- **Extraneous cues**: Random changes in initial value of C prevent subjects from using cues.

**Muller-Lyer Illusion** example:
- Proposed by **Franz Carl Muller-Lyer (1857–1916)**, German neurologist-psychiatrist.
- Standard = arrow-headed line; comparable = feather-headed line.
- Outward movement: subject extends feather-headed line (set shorter than standard).
- Inward movement: subject shortens feather-headed line (set longer than standard).
- Hypothetical data: PSE = 46.90, S = 50 mm → CE = −3.10 (underestimation). Space error = 1.095; Movement error = 0.405.

---

## Weber's Law and Fechner's Law

### Weber's Law

**E.H. Weber** = **"father of psychophysical experimentation."**

**Discovery:** JND is NOT a fixed value. It increases with the size of the standard stimulus **linearly** — the larger S, the larger the DL needed for discrimination.

**Weber's Law:**
> ΔR / R = K   ...(13.6)

Or equivalently:
> ΔR / standard stimulus = constant   ...(13.7)

- ΔR = DL; R = standard stimulus; K = **Weber's constant** (the **Weber fraction** or **Weber proportion**)
- Weber fraction = the constant dimensionless ratio indicating the proportion by which S must increase to produce a JND.

**Weber fractions for different modalities:**
| Modality | Weber Fraction |
|---|---|
| Heaviness | 0.020 |
| Line length | 0.010 |
| Brightness | 0.079 |
| Finger span | 0.023 |
| Electric shock | 0.014 |
| Salty taste | 0.084 |

**Advantage of Weber fraction:** Directly comparable across modalities (dimensionless).

**Limitation:** Precision is lost at extremely weak or extremely strong standard stimuli. Also influenced by order of presentation (Ohse, 1979): S followed by C gives maximum precision.

---

### Fechner's Law

Fechner derived his law from Weber's Law. **Key insight:** While stimulus intensity increases in **geometrical progression**, psychological sensation increases in **arithmetical progression** — a **logarithmic relationship**.

**Fechner's Law:**
> R = K log S   ...(13.8)

- R = magnitude of sensation; K = Weber's constant; S = physical stimulus magnitude

**Two core assumptions:**
1. The JND is a **unit of psychological sensation equal at all intensity levels** (all JNDs are psychologically equivalent).
2. Psychological sensation = the **sum of all JND steps** that preceded it.

**Historical significance:** First showed that mind-body relationship could be expressed mathematically; extremely influential in early psychology.

*Illustration:* Weber fraction = 0.25, starting at S = 20:
Step 1: 20 → 25 (+5); Step 2: 25 → 31.25 (+6.25); Step 3: 31.25 → 39.06 (+7.81)
Physical: geometric (multiply by 5/4); Psychological: arithmetic (each step = 1 JND).

---

## Stevens' Power Law

**S.S. Stevens** challenged Fechner, arguing sensory magnitude can be assessed **directly**.

**Two major findings of Stevens:**

a) Subjects readily judge subjective ratios and assign proportional numbers — a direct ratio scale is achievable.

b) The function relating direct scale to physical intensity is a **power function**, not a logarithm:

> S = A × I^N   (Stevens' Power Law)

- S = subjective magnitude; I = stimulus intensity; A = scaling constant; N = exponent

**Effect of exponent N:**
| N | Curve shape | Example | Meaning |
|---|---|---|---|
| N < 1 (e.g., **0.33**) | Negatively accelerated | **Loudness** | Sensation grows slower than intensity; wide range of stimuli compressed into small subjective range |
| N = 1 | Linear | **Apparent length** | Subjective = physical; no compression or expansion |
| N > 1 (e.g., **3.5**) | Concave upward | **Electric shock** | Sensation grows faster than intensity; small physical change → large subjective change |

**Direct vs. Indirect scaling:**
- **Direct scaling**: Experimenter directly obtains quantitative ratios from the subject.
- **Indirect scaling**: Uses assumed equal-appearing intervals and derives scales indirectly (e.g., Thurstone's law of comparative judgement).

---

## Newer Psychophysical Methods

### Method of Category Scaling

**Definition:** Stimuli are grouped into a **predetermined number of categories** based on perceived strength along a dimension; a direct method.

- **First demonstrated by Sanford**: Subjects sorted envelopes of different weights into **5 categories** (1 = lightest, 5 = heaviest) with subjectively equal intervals between category boundaries. Therefore also called **equal-interval scaling**.
- Extended by **Stevens & Galanter (1957)**: Frequently used **7 categories**.

**Procedure:** Subjects sort stimuli → mean ratings per stimulus across subjects → reflects an **interval scale**.

**Advantages:** Mean ratings form interval scale; absolute level and relative distances between stimuli are interpretable.

**Disadvantages:** Stimuli can only be placed within a category; similar but discriminably different stimuli may land in the same category.

---

### Method of Magnitude Estimation

**Developed by Stevens (1956).**

The **most direct approach to scaling**. Originally psychophysical; also applied to psychological dimensions.

**Procedure:**
- Subject is presented with a **standard stimulus** and told its **modulus** (numerical value).
- Subject assigns numbers to all subsequent stimuli proportional to their apparent magnitude relative to the standard.
- *Example:* Standard tone = 100 (modulus); next tone sounds twice as loud → assign 200; half as loud → 50.

**Properties:**
- Task involves judging stimuli as n times the standard → resultant scale is a **ratio scale**.
- This method was the basis for **Stevens' Power Law**.

**Cross-modality matching** (variation): No numbers used. Subject judges stimuli on one dimension by producing responses on a **different dimension** (e.g., judge line length by adjusting tone loudness).

---

## Psychological Scaling Methods

### Method of Rank Order

**Other name:** Order of Merit Method.

**Developed from works of Cattell (1903) and Spearman (1904)** on ranks in correlation computation.

**Procedure:**
- All stimuli presented **simultaneously**; subject ranks from high (rank 1 = best) to low.
- Best suited for a **small number of stimuli**.
- No sequence-of-presentation problem (unlike paired comparisons).

**Scale produced:** **Ordinal scale**.

**Computation:**

| Step | Formula | Notes |
|---|---|---|
| Choice score | C = n − r  ...(13.9) | n = total objects, r = rank assigned |
| Mean rank | Mr = Σr / N  ...(13.10) | N = number of judges |
| Mean choice score | Mc = n − Mr  ...(13.11) | |
| p value | p = Mc / (n−1)  ...(13.12) | |
| z value | from normal deviates table | Woodworth & Schlosberg, 1954 |

**Checks:** Average Mr = (n+1)/2; average p = 0.50.

**Guilford's C Scale (1954):** Normalized transformation of ranks; **mean = 5, SD = 2**. Converts ordinal data to interval-level data, enabling parametric statistics.

**Advantages over rating scales:**
1. Forces use of all parts of the scale.
2. Eliminates **error of central tendency**.
3. Forces discrimination between every pair of items.

**Serious limitation:** Does not quantify the magnitude of differences between adjacent ranks (not an interval scale by itself).

---

### Method of Successive Categories

**Other name:** Method of Successive Intervals.

**Origin:** Developed by **Thurstone**, published by **Safir (1937)** in a comparative study of pair comparisons, rank order, and successive categories.

**Key difference from equal-appearing intervals:** No assumption of **psychological equality** of interval widths (equal-appearing intervals does assume this).

**Procedure:**
- Subjects sort stimuli into 9 ordered categories:

```
1    2    3    4    5    6    7    8    9
Unfavourable          Neutral          Favourable
```

- For each item, frequencies → cumulative frequencies (Cf) → cumulative proportions (Cp) → **normal deviates (z_ij)**.
- p_ij values < 0.02 or > 0.98 are **ignored** (extreme categories 1 and 9 generally not scalable; normal deviates would be infinite).
- **Width of each interval (w_ij)** = successive subtractions of z values within rows.
- **Scale values** determined from mean/median of cumulative proportions.

**Key notations:**
- **p_ij**: proportion of judges placing statement i below upper limit of category j
- **z_ij**: normal deviate corresponding to p_ij
- **w_ij**: width of jth interval estimated from statement i

**Assumptions:**
1. Categories in correct rank order; boundaries are stable.
2. Responses follow a **normal distribution** along the psychological continuum.
3. Momentary judgements perfectly correlated with momentary positions on the psychological continuum.

---

## Methods of Attitude Scales

### Method of Equal-Appearing Intervals (Thurstone's Method)

**Developed by L.L. Thurstone.**

- Judges sort attitude statements into categories assumed to be **psychologically equal in width**.
- **Assumes** equal interval widths (unlike successive categories, which does not).
- Scale value of each statement = the **median** of the judges' sortings.

---

### Method of Summated Ratings (Likert Scale)

**Developed by Rensis Likert.**

- Subjects respond to each item on a **typically 5-point scale** (Strongly Agree to Strongly Disagree).
- Item scores **summed (or averaged)** to yield a total attitude score.
- High score always = favourable attitude; negative items are reverse-scored.
- Typically treated as an **interval scale** (technically ordinal).

**Advantages over Thurstone:** Easier to construct; generally more reliable.

---

### Guttman's Cumulative Scale (Scalogram)

**Developed by Louis Guttman.**

**Core principle:** Items form a **cumulative hierarchy** — endorsing a more extreme item implies endorsing all less extreme items.

**Coefficient of Reproducibility (CR):**
> CR = 1 − (Number of errors / Number of responses)

- Acceptable CR: **≥ 0.90** (Guttman's criterion).
- CR ≥ 0.90 indicates **unidimensionality**.

**Advantages:** Unidimensionality verified empirically; total score allows perfect prediction of response pattern.

**Limitation:** Hard to find real items forming a perfect Guttman scale.

---

## Method of Pair Comparisons

Every stimulus is paired with every other stimulus; subject judges which has more of the attribute.

**Number of pairs:** n(n−1)/2

**Thurstone's Law of Comparative Judgement (1927):** Basis for scaling from pair comparison data; assumes psychological values are normally distributed. Case V (simplified):
> S_A − S_B = z_AB

**Advantages:** Produces reliable interval scale; relatively free from rater bias.

**Disadvantages:** Time-consuming for large n (n = 20 → 190 pairs); all stimuli must be available simultaneously.

---

## Comparison of Psychological Scaling Methods

| Feature | Rank Order | Pair Comparisons | Successive Categories |
|---|---|---|---|
| Scale type | Ordinal (upgradeable) | Interval | Interval |
| Practicality with large n | Poor | Very poor | Good |
| Simultaneous presentation | Required | Required per pair | Not required |
| Assumptions | Minimal | Normal distribution | Normal distribution |
| Developed by | Cattell/Spearman | Thurstone (1927) | Thurstone/Safir (1937) |

---

## Key Terms

| Term | Definition |
|---|---|
| **Scaling methods** | Methods for sorting stimuli/individuals along a continuum based on specified attributes |
| **Psychophysical scaling** | Scaling methods where stimuli have a known physical referent |
| **Psychological scaling** | Scaling methods for stimuli lacking a physical referent; uses judgemental processes |
| **Psychophysics** | Field studying functional relations between physical stimuli and sensations; coined by Fechner |
| **Physical continuum** | Ordering of objects based on measured physical values |
| **Psychological continuum** | Ordering of objects based on subjects' judgements |
| **Limen** | Latin for threshold |
| **Absolute threshold (RL)** | Minimum stimulus detected 50% of the time; from Reiz Limen |
| **Difference threshold (DL)** | Minimum detectable difference 50% of the time; from Differenz Limen |
| **JND** | Just Noticeable Difference; smallest detectable stimulus change; = DL |
| **Standard stimulus (S)** | The constant reference stimulus in psychophysical experiments |
| **Comparable stimulus (C)** | The variable stimulus compared against the standard |
| **Interval of uncertainty (IU)** | Span between upper and lower thresholds; IU = 2 × DL |
| **PSE** | Point of Subjective Equality; value of C judged equal to S on average |
| **POE** | Point of Objective Equality; the exact physical value of S |
| **Constant error (CE)** | Systematic over- or under-judgement; CE = PSE − S |
| **Variable error** | Unsystematic error from unknown sources; indexed by SD |
| **Error of habituation** | Persistence in response after stimulus changed; also error of perseverance |
| **Error of anticipation** | Premature response change; also error of expectation |
| **Movement error** | Bias for inward vs. outward movement of C (Method of Average Error) |
| **Space error** | Bias for spatial position (left vs. right) of C (Method of Average Error) |
| **Weber fraction** | K = DL/S; the proportion by which S must increase to produce a JND |
| **Fechner's Law** | R = K log S; sensation grows as the logarithm of stimulus intensity |
| **Stevens' Power Law** | S = AI^N; sensation grows as a power function of stimulus intensity |
| **Modulus** | In magnitude estimation: numerical value assigned to the standard stimulus |
| **Cross-modality matching** | Variation of magnitude estimation using a different response dimension |
| **Choice score** | In rank order: C = n − r |
| **Ordinal scale** | Scale produced by rank order method; shows relative ordering only |
| **Equal-appearing intervals** | Thurstone's method; assumes psychologically equal interval widths |
| **Summated ratings** | Likert's method; items scored and summed for total score |
| **Cumulative scale** | Guttman's scalogram; endorsing extreme item implies endorsing all less extreme |
| **Coefficient of Reproducibility (CR)** | CR = 1 − errors/responses; ≥ 0.90 = unidimensional (Guttman) |
| **Method of successive categories** | Scaling method using ordered categories; no equal-width assumption (Thurstone/Safir, 1937) |
| **Psychometric function** | Curve relating stimulus values to proportions of a specific response category |
| **C scale** | Guilford's normalized rank transformation; mean = 5, SD = 2; converts ordinal to interval |
| **p_ij** | Proportion of judges placing statement i below upper limit of category j |
| **z_ij** | Normal deviate corresponding to p_ij |
| **w_ij** | Width of jth interval estimated from item i; by successive z subtraction |
| **SD = 1.4833 × Q** | SD estimated from semi-interquartile range in linear interpolation method |

---

## Key People / Tests

| Name | Contribution |
|---|---|
| **G.T. Fechner (1801–1887)** | Coined "psychophysics"; developed the three classical psychophysical methods; formulated Fechner's Law (R = K log S) |
| **Johann Herbart (1824)** | First introduced the concept of "threshold of consciousness" |
| **E.H. Weber** | Father of psychophysical experimentation; discovered Weber's Law (DL/R = K) |
| **Kraepelin (1891)** | Named the Method of Limits |
| **J.P. Guilford (1954)** | Preferred "Method of Minimal Changes"; recommended ANOVA for practice/fatigue effects; proposed C scale transformation |
| **S.S. Stevens (1956)** | Developed Method of Magnitude Estimation; formulated Stevens' Power Law (S = AI^N) |
| **Stevens & Galanter (1957)** | Extended category scaling; used 7 categories |
| **L.L. Thurstone** | Method of Equal-Appearing Intervals; Method of Successive Categories; Law of Comparative Judgement (1927) |
| **Safir (1937)** | Published comparative study of pair comparisons, rank order, and successive categories |
| **Rensis Likert** | Method of Summated Ratings (Likert scale) |
| **Louis Guttman** | Cumulative Scale (Scalogram); Coefficient of Reproducibility |
| **Cattell (1903)** | Ranks in computation of correlation; contributed to rank order method |
| **Spearman (1904)** | Ranks in computation of correlation; contributed to rank order method |
| **Sanford** | First demonstrated category scaling; used 5 categories for weight judgements |
| **Torgerson (1958)** | *Theory and Methods of Scaling*; defined psychological scaling methods |
| **Franz Carl Muller-Lyer (1857–1916)** | German neurologist-psychiatrist; propounded the Muller-Lyer illusion |
| **Woodworth & Schlosberg (1954)** | p-to-z conversion tables; CE formula; summation method reference |
| **Davidson and Cross (1941)** | Demonstrated two-category judgements are more reliable than three-category |
| **Andreas (1960)** | Defined absolute threshold as "a boundary point in sensation..." |
| **Ohse (1979)** | Showed Weber fraction is influenced by manner of stimulus presentation |

---

## Likely Exam Points

1. **"Psychophysics" coined by:** G.T. Fechner (1801–1887). Definition: *"the exact science of the functional relations of dependency between body and mind."*

2. **Who first introduced threshold?** Johann Herbart, **1824** ("threshold of consciousness").

3. **Who named Method of Limits?** Kraepelin, **1891**. Guilford prefers "Method of Minimal Changes."

4. **RL vs DL:** RL is a **point** (detected 50% of time); DL is a **span/range** (amount of change detected 50% of time).

5. **Constant Error formula:** CE = PSE − S. Negative = underjudgement; Positive = overjudgement.

6. **DL formula:** DL = (Upper − Lower threshold) / 2 = IU / 2.

7. **Weber's Law:** ΔR/R = K. Key fractions: heaviness = 0.020; line length = 0.010; brightness = 0.079.

8. **Fechner's Law:** R = K log S. Two assumptions: (1) all JNDs are equal psychological units; (2) sensation = sum of preceding JND steps.

9. **Stevens' Power Law:** S = AI^N. Loudness: N = **0.33** (negatively accelerated); Apparent length: N = **1** (linear); Electric shock: N = **3.5** (concave upward).

10. **Method of Average Error** = oldest psychophysical method. Also called Method of Adjustment, Method of Reproduction, Method of Equivalent Stimuli. **Subject** controls the stimulus (not the experimenter).

11. **Errors in Method of Average Error:** Movement error (inward/outward bias) and Space error (left/right bias). Both controlled by **counterbalancing**.

12. **Error of habituation** inflates **ascending** series mean; **error of anticipation** inflates **descending** series mean. Cancellation by alternating series.

13. **Method of Successive Categories:** Developed by Thurstone, published by Safir **(1937)**. Does **NOT** assume equal psychological intervals. p_ij < 0.02 or > 0.98 is **ignored** in z-conversion.

14. **Guttman's CR:** CR = 1 − (errors/responses). Acceptable: **CR ≥ 0.90** (unidimensionality).

15. **Guilford's C Scale:** Normalized rank transformation; mean = **5**, SD = **2**. Formula from interpolation data: SD = **1.4833 × Q**.

16. **Two-category judgements more reliable** than three-category (Davidson & Cross, 1941): neutral "equal" category is vague; binary forces commitment.

17. **Category scaling (equal-interval scaling):** First by **Sanford** (5 categories); extended by **Stevens & Galanter (1957)** (7 categories). Mean ratings reflect an **interval scale**.

18. **Magnitude estimation** (Stevens, 1956): modulus is the standard's assigned number; resultant scale is a **ratio scale**. **Cross-modality matching** uses a different response dimension.

---
*Source: Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh), Chapter 13: Scaling Techniques (vision-transcribed). Part of [[INDEX]].*
