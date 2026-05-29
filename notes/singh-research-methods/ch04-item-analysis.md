---
date: 2026-05-29
book: "Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh)"
subject: "Research Methodology, Statistics & Psychological Testing"
chapter: 4
tags: [item-analysis, psychometrics, MET-2026, MCQ-prep, item-difficulty, item-discrimination, IRT, distractor-analysis]
---

# Item Analysis

Chapter 4 covers the systematic procedures used after test items are written and edited to evaluate each item's effectiveness, difficulty, and discriminating power. The chapter walks through indices for power tests and speed tests, distractor analysis, correlational item-validity techniques, and ends with the modern framework of Item Response Theory (IRT) and the Item Characteristic Curve (ICC).

---

## Meaning and Purpose of Item Analysis

**Item analysis** is a set of procedures applied to determine the **indices of effectiveness (or validity)** of individual test items. It evaluates how well each item functions within the total test, selects valid and discriminating items, and identifies items to eliminate or modify.

The core logic: each item is "a test within a test"; the value of the whole test depends on the validity of individual items. Item performance by a group of examinees on a single item is compared to their performance on the whole test.

### Main Objectives of Item Analysis

1. Provides an **index of difficulty value** to each item (easy, moderately easy, moderately difficult, difficult).
2. Provides an **index of discrimination** — the ability of the item to separate superior from inferior examinees (also called **item validity**).
3. Indicates the **effectiveness of distractors** in multiple-choice items (distractor analysis).
4. Indicates why a particular item has not functioned effectively and how to modify it.

---

## Power Tests

A **power test** is one where the examinee is allowed sufficient time to answer all items. Emphasis is on measuring the examinee's **ability (power)**, not speed. Items are ideally arranged in increasing order of difficulty.

The two primary indices:
- **Index of difficulty value**
- **Index of discrimination value**

---

## Item Difficulty

### Definition

The **difficulty value (p)** (also called the **index of difficulty**) is defined as the **proportion or percentage of examinees who correctly answer the item**.

Key inverse relationship: higher p = **easier** item; lower p = **harder** item.

### Why p = 0.50 is Optimal

- Items at p = 1.0 or p = 0.0 have zero discriminating significance.
- Maximum discrimination occurs at p = 0.50.
- At p = 0.50, **variance is maximized**.
- **SD of a dichotomous item = √pq** where p = proportion passing, q = 1 − p.
- At p = q = 0.50: SD = √0.25 = 0.50; **Variance = p × q = 0.25** (maximum possible).
- At p = 0.75: Variance = 0.75 × 0.25 = 0.1875 (less than maximum).
- As p moves away from 0.50 in either direction, variance decreases and discriminating ability falls.

### Distribution of Difficulty in a Well-Constructed Test

| Position in Test | Recommended p Range |
|---|---|
| Beginning | ~100% to 60% (easy items) |
| Middle | 40% to 60% (moderate) |
| End | 10% to 40% (hardest items) |

A **peaked test** = test with items having D values in the range **0.4 to 0.6**. Produces symmetrical (near-normal) distributions and the largest standard deviations.

### Effect on Score Distribution

| D Value Range | Distribution Shape | SD |
|---|---|---|
| High D (easy) | Negatively skewed | Larger |
| Low D (difficult) | Positively skewed | Smaller |
| Moderate D (~0.5) | Symmetrical / normal | Largest |

### Effect on Reliability

- Extreme p values (0.1, 0.2, 0.8, 0.9) → items don't intercorrelate well → lower internal consistency.
- Moderate p values (~0.4–0.6) → moderate inter-item correlations → higher internal consistency.
- Item-total correlation is heavily influenced by inter-item correlations.

---

## Methods of Determining Item Difficulty

### 1. Method of Judgement

Difficulty estimated by **expert opinion** — experts rank items by difficulty. The test constructor synthesizes judgements. **Demerit:** not fully reliable or objective.

### 2. Empirical (Statistical) Method

Two variants:

#### 2a. All-Examinees Formula (Equation 4.1)

```
p = R / N
```

- **p** = index of difficulty
- **R** = number answering correctly
- **N** = total number of examinees

Items scored dichotomously: correct = 1, incorrect = 0.

#### 2b. Extreme Groups Method — Upper 27% and Lower 27%

Proposed and demonstrated by **Kelley (1939)**. Sort examinees by total score; select upper 27% (upper group) and lower 27% (lower group); discard middle 46%.

**Why 27%?** Kelley demonstrated that with a normal distribution, the critical ratio (difference between proportions / standard error of the difference) is maximized at exactly 27%. This maximizes variance captured for item analysis.

**Formula (Equation 4.2):**

```
p = (Ru + Rl) / (Nu + Nl)
```

- **Ru** = correct answers in upper group
- **Rl** = correct answers in lower group
- **Nu** = N of upper group
- **Nl** = N of lower group

**Shortcut:** Average the two group proportions:

```
p = (p_upper + p_lower) / 2
```

Example: p_upper = 0.75, p_lower = 0.25 → p = (0.75 + 0.25)/2 = 0.50.

**Advantage:** The same two groups can simultaneously yield both the difficulty index and the discrimination index, saving time and labor.

---

## Correction for Guessing (Chance Success)

Guessing inflates actual scores and raises p. Effect is greatest with fewer options (true-false = 50% guessing chance).

**Formula (Equation 4.3):**

```
S = R - W / (N - 1)
```

- **S** = corrected score
- **R** = number correct
- **W** = number incorrect
- **N** = number of response options

### Four Purposes of Correction for Guessing

1. To **discourage guessing**.
2. To give apparent advantage to examinees who **do not guess**.
3. To make scores **meaningful and dependable**.
4. To make items with **different numbers of distractors directly comparable**.

### Assumptions of the Guessing Formula

1. All wrong answers are due to **blind guessing** (no partial knowledge).
2. Each option is equally likely to be chosen by guessing.
3. Examinees exercise genuine effort.

### Limitations (Marshall & Hales, 1971; Thorndike & Hagen, 1977)

- Useful only when omissions clearly reflect lack of knowledge.
- Brighter examinees tend to attempt more items and answer more correctly, so the formula may not cleanly separate knowledge from guessing.
- **Thorndike & Hagen (1977):** if the test is sound, gives sufficient time, and suits examinees, guessing is automatically minimized — the formula is unnecessary.

---

## Optimal Difficulty Level for a Reliable Test

| Item Format | Optimal p (unadjusted) |
|---|---|
| Two-alternative (true-false, agree-disagree) | **0.85** |
| Four-alternative | **0.74** |
| Five-alternative | **0.69** |

For two-alternative items, ambiguous items may yield p near 0.5 but have **near-zero biserial/point-biserial correlations** — high p alone does not guarantee reliability. The recommendation: two-alternative items should have D value above **0.75** (unadjusted = 0.85 optimal).

---

## Index of Discrimination

### Definition

The **index of discrimination** (also called **item validity index**) = the degree to which a single item separates superior from inferior individuals on the continuum of the trait being measured.

Key citations:
- Exhaustively described by **Mosier & McQuitty (1940)**, **Johnson (1951)**, **Wood (1961)**.
- **Ebel (1965):** "The degree to which the single item separates the superior from the inferior individuals on the continuum of traits being measured."
- **Marshall & Hales (1971, p. 81):** "The discriminatory power or validity of a single test item is defined as the extent to which success and failure on that item indicate the possession of the trait or achievement the test measures."

### Types of Discriminating Items

| Type | Definition |
|---|---|
| **Positively discriminating** | Proportion correct is greater in the upper group |
| **Negatively discriminating** | Proportion correct is lower in the upper group |
| **Nondiscriminating** | Proportion correct is approximately equal in both groups |

Negatively discriminating and nondiscriminating items are **dropped** after item analysis.

---

## Methods of Determining the Index of Discrimination

### 1. Critical Ratio (Difference Between Two Proportions)

Divide examinees into upper 27% and lower 27% by total score. Apply critical ratio to test significance of the proportional difference.

**Demerit:** Only indicates WHETHER an item discriminates — not the AMOUNT of discrimination.

### 2. Chi-Square Method — Gulliksen (1945)

**Gulliksen (1945)** recommended chi-square when both extreme groups have equal N.

**Formula (Equation 4.4):**

```
χ² = N(Pu − PL)² / 4pq
```

- **N** = total examinees
- **Pu** = proportion passing in upper group
- **PL** = proportion passing in lower group
- **p** = arithmetic mean of Pu and PL
- **q** = 1 − p

**Limitation:** p value affects chi-square value; only tells whether item discriminates, not the degree.

### 3. Net D Index — Marshall & Hales (1972)

**Marshall & Hales (1972)** proposed the **"Net D index"** (abbreviated D or V = validity index).

**Definition:** Absolute difference in proportions correct between upper and lower groups.

**Formula (Equation 4.5):**

```
D = (Ku / Nu) − (KL / NL)
```

Or: D = p_upper − p_lower

- **Ku** = correct answers in upper group
- **KL** = correct answers in lower group
- **Nu, NL** = group sizes

**Net D Interpretation Table:**

| Net D | Interpretation | Action |
|---|---|---|
| Negative | Negative discrimination | Drop |
| 0.00–0.10 | Negligible discrimination | Drop or modify |
| 0.10–0.20 | Very little / marginal | Drop or modify |
| 0.20–0.40 | Good discrimination | Retain |
| Above 0.40 | Excellent discrimination | Retain |

**Example:** Nu = NL = 100; Ku = 80; KL = 70.
D = 80/100 − 70/100 = 0.80 − 0.70 = 0.10 → negligible → drop or modify.

---

## Correlational Techniques for Item Discrimination

**Item-total correlation** — each item correlated against total test score. Called **"internal-consistency item discrimination index"** by **Lindquist (1951)**.

**General rules:**
- Items with r ≥ **0.20** are satisfactory and selected for the final test.
- At least **75%** of all item-total correlations should be positive (preferably above 0.15).

### Five Correlational Measures

| Statistic | When to Use |
|---|---|
| **Product Moment (PM) / Pearson r** | Multipoint items (e.g., Likert scale) |
| **Biserial r** | Item has two response categories; total score continuous |
| **Point biserial r** | Item is true dichotomy; total score continuous |
| **Tetrachoric r** | Both item and total score artificially dichotomized |
| **Phi-coefficient (φ)** | Both item and total score are true dichotomies (0/1 scoring) |

**Flanagan's table:** Ready-reference chart giving biserial r directly from p_upper and p_lower. Criterion group N must be ≥ 100 (total N ≥ ~370).

**Nunnally (1978) item selection procedure:**
1. Rank all items from highest to lowest item-total correlation.
2. Select top items (e.g., 30 items).
3. Apply **KR-20** to check reliability.
4. If KR-20 ≥ 0.90 → accept; if KR-20 < 0.80 → add more items with next highest correlations and recompute.

### Scoring Reversal for Personality/Attitude Tests

When ~25% of items yield negative item-total correlations:
- Reverse the scoring key for those items (e.g., if "Yes" = +1 yielded negative r, recode so "No" = +1).
- Recalculate total scores; recompute item-total correlations.
- Repeat if still more negatives remain.

---

## A Simplified Item Analysis Form (Step-by-Step)

For a 30-item test with 375 examinees:

1. Score answer sheets by key (correct = 1 or weighted).
2. Compute total scores.
3. Arrange sheets from highest to lowest total score.
4. Per **Kelley (1939):** Select upper 27% (~100 cases) and lower 27% (~100 cases); discard middle 46%.
5. For each item: count correct responses in upper 27% group.
6. Count correct responses in lower 27% group.
7. Compute difference = Upper correct − Lower correct.
8. Divide by N of upper group → **Discrimination index D**.
9. Count correct responses in middle 46% group; add upper + middle + lower correct responses.
10. Divide total correct by total N (375) → **Difficulty value p**.

---

## Effectiveness of Distractors (Distractor Analysis)

### Definitions

| Distractor Type | Definition |
|---|---|
| **Good distractor** | Chosen by more lower-group examinees than upper-group; functions correctly |
| **Poor distractor** | Chosen by more upper-group examinees than lower-group; must be rewritten |
| **Nonfunctional distractor** | Attracts/repels neither group; drop or modify |

**Key rule:**
- **Correct response** → positive discrimination index.
- **Each distractor** → negative discrimination index.

### Expected Frequency Formula (Without Extreme Groups)

```
Expected number choosing a distractor = (N answering incorrectly) / (Number of distractors)
```

Example: 100 examinees, 3 distractors, 75 correct → 25 incorrect → expect 25/3 ≈ 8 per distractor. Wide deviation from expected → distractor functioning poorly.

### Effects of Poor Distractors

- Lower the difficulty value (item becomes too easy).
- Lower the discriminating power.

---

## Speed Tests

A **speed test** provides limited time; all items should be at **uniform difficulty level**. Standard item analysis cannot be applied directly because later items are not reached by many examinees due to time — not inherent difficulty.

---

## Index of Difficulty for Speed Tests

```
p = A / N
```

- **A** = number of correct answers
- **N** = number of examinees who actually **reached or attempted** the item (not total test N)

Example: Item 70 reached by 50 of 100 examinees; 20 correct → p = 20/50 = 0.40.

### Corrected Index of Difficulty for Speed Tests (Equation 4.6)

```
p_c = (A − R) / (N − R)
```

- **A** = correct answers
- **N** = examinees who reached the item
- **R** = number of chance-correct responses (estimated as N × 1/K, where K = number of options)

---

## Index of Discrimination for Speed Tests

Standard item-total correlation **cannot** be used because:
- Items arranged in ascending difficulty (not random).
- Time limit creates restriction of range in item scores.
- First items → many correct; last items → very few correct.
- Both extremes yield poor inter-item correlations and misleading item-total correlations.

**Alternative: Nunnally (1970) method** — select items based on difficulty index plus experimentally determined ideal time limit.

### Nunnally (1970) Method for Ideal Time Limit

1. Randomly select six equal-sized groups of parallel ability.
2. Give same test to each group with different time limits (e.g., 10, 12, 15, 18, 20, 25, 30 minutes).
3. Compute reliability (split-half) or use **standard deviation** as criterion.
4. The time limit producing the **largest standard deviation** → highest reliability → **ideal time limit**.

**Principle:** Larger SD = higher reliability.

---

## Factors Influencing Index of Difficulty and Index of Discrimination

### Factors Affecting Index of Difficulty

1. **Complexity/ambiguity of item stem** — lowers p.
2. **Previous learning/experience** — unfamiliarity lowers p.
3. **Nature of response alternatives** — homogeneous distractors lower p; obvious/heterogeneous distractors raise p.

### Factors Affecting Index of Discrimination

(All difficulty factors apply, plus:)
4. **Heterogeneity of the group** — more heterogeneous → better discrimination.
5. **Reliability of the total test** — higher reliability → better item discrimination.
6. **Clarity of the question** — vague questions lower discrimination.
7. **Effectiveness of distractors** — poor distractors reduce discriminating power.

---

## Problems of Item Analysis

### Problem 1: Overestimation of Item-Total Correlation

When total score is the criterion and the item being correlated is part of that total, the correlation is always an **overestimate**. More serious in homogeneous tests.

### Problem 2: Dichotomous Items in Personality Tests

If all agreements are scored +1 indiscriminately on personality scales, positive items will **correlate negatively** with negative items → average inter-item correlation approaches zero → all item-total correlations approach zero.

**Solution:** Change the scoring key to maximize total variance. Give +1 to positive items when agreed with, and +1 to negative items when disagreed with (reverse scoring).

### Problem 3: Content and Process Contamination

Items may measure more than one attribute (e.g., a math test item also requires reading comprehension). Factor contamination inflates certain item-total correlations misleadingly.

**Solution:** Correlate items with both the target factor and the unwanted factor; select items with high target correlation and low unwanted-factor correlation.

### Problem 4: Multiple Items with Identical Item-Total Correlations

Selection becomes arbitrary.

**Solution:** Start with more items than needed (e.g., 160 items for a final 50-item test). Correlate each item with both total score and unwanted factor. Select items with high target and low nuisance correlations.

### Problem 5: Guessing / Chance Success

Two-alternative items allow 50% guessing probability. Guessing formula can overcorrect when wrong answers reflect partial knowledge rather than pure chance.

**Solution:** Use correction formula (Eq 4.3); maximize distractors; warn against guessing; design plausible distractors; give ample time.

---

## Interactions Among Item Characteristics

### Distractors and Difficulty

- **Ridiculous distractors** → item too easy.
- **Plausible distractors** → item harder.
- Item difficulty can be easily changed by rewriting distractors.

**Classic example from text:**
- Item A: Wundt's lab year — options: 1849, 1279, 1879, 1959 → ridiculous → very easy.
- Item B: Wundt's lab year — options: 1865, 1868, 1876, 1879 → plausible → much harder.

### Distractors and Discrimination

Poor distractors make items too easy or too hard → directly limits discriminating power.

### Difficulty and Discrimination

- p = 1.0 or p = 0.0 → zero discrimination.
- **Items with p between 0.30 and 0.70** have maximum potential for discrimination.
- Average of 0.30–0.70 range → mean p = 0.50.
- A poor item with p = 0.50 is still a poor item — p alone does not guarantee good discrimination.

---

## The Item Characteristic Curve (ICC) and Item Response Theory

### Item Characteristic Curve (ICC)

The **ICC** is a **graphic representation** of the relationship between the **probability of a correct response** to an item and the **underlying ability/trait level** of the examinee. It is the foundation of IRT.

| ICC Feature | What It Indicates |
|---|---|
| **Steepness of slope** | Discriminating power |
| **Position on x-axis (left vs right)** | Item difficulty |
| Steep positive slope | High item-total correlation, high discrimination |
| Flat (near-zero) slope | Item-total correlation ≈ 0, no discrimination |
| ICC rises on right (high ability) | Difficult item |
| ICC rises on left (low ability) | Easy item |

**Fig. 4.1:** ICCs with different slopes but similar difficulty.
**Fig. 4.2:** ICCs with similar slopes but varying difficulty (Item A = easiest, Item C = hardest, Item B = moderate).

---

### Item Response Theory (IRT)

**Synonyms:** Latent trait theory | Item characteristics curve theory

**Core definition (Gorth & Hambleton, 1972):** The probability of a particular response to a test item is a **joint function of one or more parameters of the item and one or more parameters of the examinee**.

**IRT vs Classical Test Theory (CTT):**

| Feature | CTT | IRT |
|---|---|---|
| Score | Sum of responses | Probability modeled per item |
| Item calibration | Sample-dependent | Sample-invariant |
| Ability estimation | Sample-dependent | Sample-invariant |
| Tailored testing | Not possible | Possible (computer-adaptive) |
| Item format | Single total score | Independent ICC per item |

### IRT Assumptions (Murphy & Davidshofer, 1988)

1. The trait is **unidimensional** (one underlying dimension).
2. Local independence — examinee's ability and probability of correct response are **independent of specific items** used.
3. Item characteristics described by ICCs derived from data.

### IRT Parameters

Most models use two parameters:
1. **Difficulty (b parameter)**
2. **Discrimination (a parameter)**

Three-parameter models add:
3. **Pseudo-guessing (c parameter)** — probability that a very low-ability examinee guesses correctly.

### Advantages of IRT

1. **Sample-invariant measures** — item and ability estimates don't depend on the specific sample.
2. **Item-independent ability estimates** — ability estimates don't depend on specific items administered.
3. **Tailored/computer-adaptive testing** — items dynamically matched to examinee's estimated ability.
4. **50% more efficient** than paper-pencil tests — Weiss (1985) and Weiss & Yoes (1991).
5. Handles items in **different formats** within same test.
6. **Reveals item bias patterns**; reduces bias against slow test-takers.
7. Item analysis without a large, representative sample.

### IRT Applications

#### (a) Getting Information from Distractors (Trace Lines)

IRT constructs a **separate ICC ("trace line") for each response option** — both correct answer and each distractor.

**Fig. 4.3** shows trace lines for responses A, B, C, D, and "omit" (X) for one multiple-choice item:
- **Correct response (A):** Trace line increases with ability — chosen by most able examinees.
- **Good distractor (C):** Shows positive discriminating power at moderate ability — useful trap for able examinees.
- **Poor distractor (B):** Shows negative discriminating power — chosen more by low-ability examinees; still provides information.
- **Omit (X):** Separate trace line; declines as ability rises.

Any response (even incorrect) provides information about the examinee's ability level.

#### (b) Tailored Testing (Computer-Adaptive Testing)

- Computer selects items whose difficulty matches the examinee's **estimated ability level** after each response.
- All items calibrated on a **common scale**.
- Examinee not embarrassed by items far above ability, not bored by items far below.
- Each examinee gets a **different set of items** — hence "tailored testing."
- Most efficient and precise form of ability assessment.

#### (c) Item Analysis for Specialized Tests

Particularly useful for:
- **Criterion-keyed tests:** e.g., **MMPI (Minnesota Multiphasic Personality Inventory)** — personality test scored against known-group norms.
- **Screening tests:** Pass/fail decisions based on minimum competency.
- Standard norm-referenced procedures do not apply; IRT fills the gap.

---

## Key Terms

| Term | Definition |
|---|---|
| **Item analysis** | Procedures to determine effectiveness, difficulty, and discriminating validity of individual test items |
| **Index of difficulty (p)** | Proportion of examinees correctly answering an item; p = R/N |
| **Peaked test** | Test with item D values in the range 0.4–0.6; produces near-normal score distribution with largest SD |
| **Index of discrimination / Net D** | Extent to which an item separates superior from inferior examinees; D = p_upper − p_lower |
| **Item validity index** | Alternative name for the index of discrimination |
| **Positively discriminating item** | Proportion correct is higher in the upper group |
| **Negatively discriminating item** | Proportion correct is lower in the upper group |
| **Nondiscriminating item** | Proportion correct is approximately equal in both groups |
| **Distractor analysis** | Examination of how each incorrect option functions for upper and lower groups |
| **Good distractor** | Chosen by more lower-group examinees than upper-group examinees |
| **Power test** | Test with sufficient time for all items; measures ability, not speed |
| **Speed test** | Test with time pressure; items at uniform difficulty; emphasizes speed |
| **Tailored testing** | Computer-adaptive testing matching items to each examinee's estimated ability |
| **Item Characteristic Curve (ICC)** | Graph of probability of correct response versus ability/trait level |
| **Item Response Theory (IRT)** | Psychometric theory relating examinee ability to item response probability; also called latent trait theory |
| **Latent trait theory** | Alternative name for IRT |
| **Trace lines** | ICCs constructed separately for each response option (correct + each distractor) in IRT analysis |
| **Correction for guessing** | S = R − W/(N−1); adjusts raw score for chance success |
| **Internal-consistency item discrimination index** | Lindquist (1951) term for item-total correlation |
| **Biserial r** | Correlation: dichotomous item vs continuous total score (assumes underlying normality) |
| **Point biserial r** | Correlation: true dichotomy vs continuous total score |
| **Phi-coefficient (φ)** | Correlation: two true dichotomies |
| **Tetrachoric r** | Correlation: two artificially dichotomized continuous variables |
| **Dichotomous items** | Items scored 0 or 1 (correct/incorrect or agree/disagree) |
| **Item-total correlation** | Correlation of individual item score with total test score; primary discrimination index |
| **Variance of dichotomous item** | p × q; maximum = 0.25 when p = q = 0.50 |
| **KR-20 (Kuder-Richardson Formula 20)** | Internal consistency reliability formula used to validate selected item sets |
| **Computer-adaptive testing** | IRT-based tailored testing via computer; 50% more efficient than paper-pencil (Weiss, 1985) |

---

## Key People / Tests

| Name / Test | Contribution |
|---|---|
| **Kelley (1939)** | Demonstrated that using the upper and lower 27% of examinees maximizes the critical ratio; recommended 27% as standard for item analysis |
| **Mosier & McQuitty (1940)** | First to exhaustively describe the index of discrimination |
| **Johnson (1951)** | Further described the index of discrimination |
| **Wood (1961)** | Further described the index of discrimination |
| **Ebel (1965)** | Defined discrimination as the degree an item separates superior from inferior individuals on the trait continuum |
| **Lindquist (1951)** | Named item-total correlation the "internal-consistency item discrimination index" |
| **Flanagan** | Developed ready-reference chart for reading biserial r directly from proportions in upper 27% and lower 27% groups |
| **Gulliksen (1945)** | Recommended chi-square for discrimination with equal group sizes; formula: χ² = N(Pu − PL)²/4pq |
| **Marshall & Hales (1971)** | Defined discriminatory power; noted limitations of correction for guessing |
| **Marshall & Hales (1972)** | Proposed "Net D index of discrimination" — simple proportion difference between upper and lower groups |
| **Nunnally (1978)** | Procedure: rank items by item-total r, check with KR-20, add items until desired reliability achieved |
| **Nunnally (1970)** | Experimental method for determining ideal time limit in speed tests using SD as reliability criterion |
| **Gorth & Hambleton (1972)** | Defined IRT: probability of response is joint function of item parameters and examinee parameters |
| **Cascio (1987)** | Noted IRT makes extensive use of item analysis |
| **Steinberg & Thissen (1995)** | Applied IRT to item analysis |
| **Weiss (1985); Weiss & Yoes (1991)** | Demonstrated computer-adaptive testing is 50% more efficient than paper-pencil |
| **Murphy & Davidshofer (1988)** | Described unidimensional trait assumption of IRT |
| **Thorndike & Hagen (1977)** | Argued correction for guessing is unnecessary when the test is well-constructed, timed correctly, and appropriate for examinees |
| **MMPI** | Minnesota Multiphasic Personality Inventory; criterion-keyed personality test cited as example of specialized test analyzed with IRT |

---

## Likely Exam Points

1. **Item analysis** = set of procedures determining indices of effectiveness/validity of each item; selects valid, discriminating items.

2. **Index of difficulty (p):** p = R/N; inversely related to actual difficulty (higher p = easier item).

3. **Optimal p = 0.50:** Maximum variance = p × q = 0.25; SD = √pq = 0.50.

4. **Kelley (1939) — why 27%:** At 27% cut in a normal distribution, the critical ratio between upper and lower groups is maximized.

5. **Peaked test:** Items with D values 0.4–0.6; produces symmetrical distribution and largest SD.

6. **Optimal difficulty by format:** Two-alternative = 0.85; four-alternative = 0.74; five-alternative = 0.69.

7. **Correction for guessing:** S = R − W/(N−1), where N = number of options.

8. **Net D values:** Negative = drop; 0–0.10 = negligible (drop/modify); 0.10–0.20 = very little; 0.20–0.40 = good; >0.40 = excellent.

9. **Gulliksen (1945) chi-square:** χ² = N(Pu − PL)²/4pq; requires equal group sizes; tells whether (not how much) item discriminates.

10. **Five correlational measures:** PM (multipoint), biserial r, point biserial r (two-category), tetrachoric r (both dichotomized), phi (true dichotomies).

11. **Satisfactory item-total r threshold:** ≥ 0.20; at least 75% of items should yield positive correlations.

12. **Speed test difficulty:** p = A/N where N = examinees who reached (attempted) the item, NOT total N.

13. **IRT synonyms:** Item Response Theory = Latent Trait Theory = Item Characteristics Curve Theory.

14. **IRT vs CTT:** IRT yields sample-invariant item and ability estimates; enables tailored/computer-adaptive testing; 50% more efficient (Weiss, 1985; Weiss & Yoes, 1991).

15. **ICC interpretation:** Slope = discriminating power (steep = high discrimination, flat = none); position = difficulty (rises left = easy, rises right = difficult).
```

---

That is the complete Chapter 4 study note. It covers every section, all formulas (Equations 4.1 through 4.6), every researcher citation, all classification tables, and ends with the three summary tables and 15 high-yield exam points. Save it to your vault — it is ready to use as-is.

---
*Source: Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh), Chapter 4: Item Analysis (vision-transcribed). Part of [[INDEX]].*
