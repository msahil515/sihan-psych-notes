---
date: 2026-06-11
book: "Amity Entrance: Master Syllabus (RCI / NIMHANS pattern)"
subject: "Amity Prep"
chapter: 5
tags: [amity, RCI, clinical-psychology, NIMHANS-pattern, entrance, MET2026]
---

# Ch 5: Advanced Psychometrics & Scale Construction

This chapter teaches the mathematical machinery behind psychological tests: how Classical Test Theory models a score, how reliability and validity are estimated, how individual items are analyzed and selected, and how modern Item Response Theory replaced the test-level view with an item-level, latent-trait view. Every formula, criterion, and key figure here is high-yield for RCI and NIMHANS-pattern entrances, where psychometrics is reliably worth several objective questions.

## 1. Classical Test Theory (CTT): The True Score Model

Classical Test Theory, often credited to **Charles Spearman** and formalized by **Lord and Novick (1968)**, rests on one deceptively simple equation:

**X = T + E**

Here **X** is the **observed score** (what the test actually gives), **T** is the **true score** (the score the person would get averaged over infinitely many parallel testings, i.e. the expected value of the observed score), and **E** is the **error score** (random measurement error). The true score is defined operationally, not philosophically: **T = E(X)**, the long-run average of a person's observed scores. Error is whatever pushes the observed score away from the true score on any given occasion.

### Core assumptions of CTT

CTT makes four assumptions that let the model do work:

- **E(E) = 0**: across many testings, random errors average to zero. Errors are equally likely to inflate or deflate a score, so the mean error is nil. This is why the true score equals the expected observed score.
- **rho_TE = 0**: the correlation between true scores and error scores is zero. How much error you get does not depend on how high your true ability is. Error is genuinely random with respect to ability.
- **rho_E1E2 = 0**: errors on two different tests (or two administrations) are uncorrelated with each other. The error you make today is independent of the error you make tomorrow.
- A fourth implied assumption is that **error is uncorrelated with the true score on a different test** (rho_E1T2 = 0).

A key consequence: because true and error variance are independent, **observed-score variance partitions additively**: **sigma^2_X = sigma^2_T + sigma^2_E**. Total observed variance is true variance plus error variance. This decomposition is the foundation of reliability.

### Reliability defined

**Reliability (rxx)** is the proportion of observed-score variance that is true-score variance:

**rxx = sigma^2_T / sigma^2_X = sigma^2_T / (sigma^2_T + sigma^2_E)**

Reliability ranges from 0 to 1. A reliability of 0.80 means 80% of the variance in scores reflects true individual differences and 20% reflects measurement error. Equivalently, reliability is the squared correlation between observed and true scores, and the correlation between observed and true score (the **reliability index**) equals the square root of reliability, **sqrt(rxx)**.

### Standard Error of Measurement (SEM)

The **Standard Error of Measurement** quantifies, in raw score units, how much an individual's observed score is expected to fluctuate around the true score due to error:

**SEM = SD * sqrt(1 - rxx)**

where SD is the standard deviation of the test scores and rxx is the reliability. Notice the logic: if reliability is perfect (rxx = 1), SEM = 0 (no error). If reliability is zero, SEM equals the full SD (the score is all noise). The SEM is used to build a **confidence interval around an observed score**: roughly 68% of the time the true score lies within +/- 1 SEM, and about 95% within +/- 1.96 SEM. Clinically, SEM tells you how seriously to take a single IQ or symptom score. Example: SD = 15, rxx = 0.91, then SEM = 15 * sqrt(0.09) = 15 * 0.3 = 4.5 points.

## 2. Reliability: Estimation Methods and Corrections

### Types of reliability (what kind of error each captures)

| Method | Procedure | Error source assessed | Key statistic |
|---|---|---|---|
| **Test-retest** | Same test, same people, two occasions | Temporal stability (time sampling) | Correlation = **coefficient of stability** |
| **Parallel / alternate forms** | Two equivalent forms, same people | Item/content sampling (and time if delayed) | Correlation = **coefficient of equivalence** |
| **Internal consistency** | One test, one administration, split or item-level | Item/content homogeneity | Split-half, Cronbach's alpha, KR-20 |
| **Inter-rater (inter-scorer)** | Two or more raters score same responses | Scorer variance | % agreement, **Cohen's kappa**, ICC |

Test-retest is vulnerable to **carryover and practice effects**; parallel forms solve practice effects but require building two genuinely equivalent tests. Inter-rater reliability matters wherever judgment is involved (projective tests, behavioral coding, clinical ratings); **Cohen's kappa** corrects percent agreement for chance agreement.

### Spearman-Brown prophecy formula

When you split a test in half and correlate the halves, you get the reliability of a **half-length** test, which underestimates the full test's reliability (shorter tests are less reliable). The **Spearman-Brown prophecy formula** corrects (prophesies) the reliability of the full or lengthened test:

**r_full = (n * r) / (1 + (n - 1) * r)**

where r is the observed reliability and n is the factor by which length is changed. For the classic split-half case, n = 2 (you are doubling the half-test back to full length):

**r_full = (2 * r_half) / (1 + r_half)**

Example: split-half correlation of 0.60 gives full-test reliability of (2 * 0.6)/(1.6) = 0.75. The formula also answers "how many items do I need to reach a target reliability," making it central to scale construction. A limitation of split-half is that the answer depends on **how you split** the test (odd-even vs first-half/second-half give different values).

### Cronbach's alpha

**Cronbach's alpha (1951)** generalizes split-half: it is the **mean of all possible split-half reliabilities** and is the most widely reported index of internal consistency. It estimates reliability from the average inter-item covariance and the number of items:

**alpha = (k / (k - 1)) * (1 - (sum of item variances / total test variance))**

where k is the number of items. Alpha rises with (a) more items and (b) higher average inter-item correlation. Conventional benchmarks: **>= 0.70 acceptable**, **>= 0.80 good**, **>= 0.90 excellent** (but very high alpha, > 0.95, can signal redundant items). Crucially, alpha assumes **tau-equivalence** (items measure the same construct with equal true-score weights) and is a **lower-bound estimate** of reliability. Alpha is for **continuous / multi-point (e.g. Likert) items**.

### Kuder-Richardson formulas (KR-20 and KR-21)

KR formulas are the special case of internal consistency for **dichotomously scored items** (right/wrong, yes/no, 1/0).

**KR-20** is the dichotomous analogue of alpha:

**KR-20 = (k / (k - 1)) * (1 - (sum of p*q) / sigma^2_total)**

where p is the proportion passing an item, q = 1 - p, and p*q is that item's variance. **KR-21** is a simplified approximation that assumes **all items are equal in difficulty**, using only the test mean (M) and variance:

**KR-21 = (k / (k - 1)) * (1 - (M * (k - M)) / (k * sigma^2_total))**

KR-21 is easier to compute but, because real items differ in difficulty, **KR-21 <= KR-20 <= true reliability** (KR-21 is the most conservative).

### Correction for attenuation

Measurement error **attenuates** (shrinks) the observed correlation between two variables below their true correlation. The **correction for attenuation** estimates what the correlation would be if both measures were perfectly reliable:

**r_true = r_xy / sqrt(rxx * ryy)**

where r_xy is the observed correlation and rxx, ryy are the two reliabilities. Example: observed r = 0.45 with reliabilities 0.81 and 0.64 gives 0.45 / sqrt(0.5184) = 0.45 / 0.72 = 0.625. This shows validity coefficients are capped by reliability, which is why reliability is a **necessary but not sufficient** condition for validity.

## 3. Item Analysis (Classical)

After piloting a test you evaluate each item to decide which to keep, revise, or drop.

### Item difficulty (p)

**Item difficulty** is simply the **proportion of examinees who answer the item correctly**: **p = (number correct) / (total examinees)**. Counterintuitively, higher p means an **easier** item (more people passed). p ranges 0 to 1. For maximizing discrimination on a norm-referenced test, **p around 0.50** is ideal because it produces maximum item variance (p*q peaks at p = 0.50). In practice item writers aim for an average p of about 0.50, adjusting upward to roughly the midpoint between chance and 1.0 for guessing-prone multiple-choice items (e.g. for 4-option items, around 0.625).

### Item discrimination index (d)

The **discrimination index d** measures how well an item separates high scorers from low scorers. The classic **upper-lower 27% method** (Kelley's optimal cut): rank examinees by total score, take the **top 27%** and the **bottom 27%**, then:

**d = (number correct in upper group - number correct in lower group) / (number in one group)**

d ranges from -1 to +1. Interpretation benchmarks (**Ebel**): **>= 0.40 very good**, **0.30 to 0.39 reasonably good**, **0.20 to 0.29 marginal (revise)**, **< 0.20 poor (discard)**. A **negative d** is a red flag: low scorers got it right more than high scorers, suggesting a miskeyed item or a misleading distractor. The 27% figure is used because it best balances having extreme, contrasting groups against having enough people in each group.

### Point-biserial correlation

The **point-biserial correlation (r_pb)** is a continuous index of discrimination: the correlation between the **dichotomous item score (0/1)** and the **continuous total test score**. A high positive r_pb means people who got the item right scored higher overall, i.e. the item is consistent with the rest of the test. It is preferred over the upper-lower d because it uses the full sample, not just the extremes. Items with low or negative r_pb are candidates for removal. (Note: total-score should ideally exclude the item being analyzed to avoid spurious inflation.)

## 4. Item Response Theory (IRT) / Latent Trait Theory

IRT (also called **latent trait theory**) shifts the unit of analysis from the test to the **individual item**, modeling the probability of a correct response as a function of an unobservable trait. Its great advantages over CTT: item parameters are **sample-invariant** (do not depend on the particular group tested), person ability is **test-invariant** (does not depend on the particular items used), and measurement precision can vary along the trait. IRT underlies modern **computerized adaptive testing (CAT)**.

### The latent trait (theta)

**Theta (θ)** is the **latent trait** or ability being measured (e.g. depression severity, mathematical ability), conventionally scaled with mean 0 and SD 1, typically ranging from about -3 to +3. The **Item Characteristic Curve (ICC)** plots the probability of a correct/endorsed response against theta and is S-shaped (logistic ogive).

### The 1PL / Rasch model (b parameter)

The **one-parameter logistic (1PL)** model, when the discrimination is fixed at 1, is the **Rasch model** (Georg Rasch). The single estimated parameter is **b, the difficulty (location) parameter**: the point on the theta scale where a person has a **50% probability** of answering correctly. Higher b = harder item (it takes more ability to reach 50% success). On the ICC, b is the theta value at the inflection point. The Rasch model assumes all items discriminate equally and has elegant measurement properties (specific objectivity).

### The 2PL model (a parameter)

The **two-parameter logistic (2PL)** model adds **a, the discrimination parameter**, which is proportional to the **slope of the ICC at its inflection point**. A high a means the item sharply distinguishes people just below from just above b (a steep curve); a low a means a flat, weakly discriminating item. The 2PL allows items to differ in both difficulty (b) and discrimination (a).

### The 3PL model (c parameter)

The **three-parameter logistic (3PL)** model adds **c, the pseudo-guessing parameter**: the **lower asymptote** of the ICC, the probability that a very low-ability examinee still gets the item right by guessing. For a 4-option multiple-choice item, c is theoretically around 0.25. With guessing, the curve does not drop to zero probability at low theta; it flattens out at c.

| Model | Parameters estimated | What each captures |
|---|---|---|
| **1PL / Rasch** | b | difficulty only (a fixed = 1) |
| **2PL** | a, b | discrimination + difficulty |
| **3PL** | a, b, c | discrimination + difficulty + guessing |

### Information functions

In IRT, **reliability is replaced by information**. The **Item Information Function** shows how much measurement precision an item provides at each level of theta; an item gives **maximum information near its b value** and more discriminating (high a) items provide more information. The **Test Information Function (TIF)** is the **sum of all item information functions** and shows where on the trait the whole test measures most precisely. The **standard error of measurement in IRT is the inverse square root of information**: **SE(theta) = 1 / sqrt(I(theta))**, so more information means less error, and error can differ across the trait range (unlike CTT's single SEM).

### Differential Item Functioning (DIF)

**Differential Item Functioning** occurs when examinees from **different groups (e.g. gender, ethnicity) who have the same level of the latent trait (matched on theta) have different probabilities of answering an item correctly**. DIF signals potential **item bias** and threatens fairness. It is detected with methods such as the **Mantel-Haenszel** procedure or IRT-based comparisons of ICCs across groups. **Uniform DIF** means one group is favored consistently across all theta levels (ICCs differ in b); **non-uniform DIF** means the advantage reverses across theta (ICCs differ in a, curves cross). DIF is essential to documenting test fairness for high-stakes assessment.

## 5. Validity and Construct Validation

**Validity** is the degree to which evidence and theory support the interpretations of test scores for proposed uses (it is a property of inferences, not of the test itself).

### Types of validity

- **Content validity**: the degree to which test items adequately and representatively **sample the content domain** the test claims to measure. Judged by expert review, not statistics. **Face validity** (whether the test merely *appears* relevant to test-takers) is the weakest, superficial cousin and is not true validity.
- **Criterion validity**: how well scores predict or relate to an external criterion. **Concurrent validity** correlates test scores with a criterion measured at the **same time**; **predictive validity** correlates with a criterion measured in the **future** (e.g. entrance test predicting later GPA). The correlation is the **validity coefficient**.
- **Construct validity**: the degree to which a test measures the **theoretical construct** it intends to. It is the overarching, umbrella form of validity and is established by accumulating evidence, including **convergent** and **discriminant** validity.
  - **Convergent validity**: the measure correlates **highly** with other measures of the **same construct**.
  - **Discriminant (divergent) validity**: the measure correlates **low** with measures of **different/unrelated constructs**.

### Lawshe's Content Validity Ratio (CVR)

**C. H. Lawshe (1975)** quantified content validity. A panel of experts rates whether each item is "Essential," "Useful but not essential," or "Not necessary." The **Content Validity Ratio** is:

**CVR = (n_e - N/2) / (N/2)**

where n_e is the number of experts rating the item "Essential" and N is the total number of experts. CVR ranges from **-1 to +1**. CVR = 0 means exactly half called it essential; CVR > 0 means a majority did. Items are retained if CVR exceeds the **critical value tabled for the panel size** (the cutoff falls as N rises: e.g. about 0.99 for 5 raters, 0.62 for 10, 0.49 for 15, 0.29 for 40). Averaging the retained items' CVRs gives the **Content Validity Index (CVI)**.

### Standard error of estimate

When a regression predicts a criterion (Y) from test scores (X), the **standard error of estimate (SEest)** is the standard deviation of the prediction errors (residuals), i.e. how far actual criterion values typically fall from the predicted regression line:

**SEest = SD_y * sqrt(1 - r^2_xy)**

where r_xy is the validity coefficient. The stronger the validity (higher r), the smaller the SEest and the tighter the prediction. It is the validity analogue of SEM.

### Multitrait-Multimethod Matrix (Campbell & Fiske, 1959)

**Donald Campbell and Donald Fiske (1959)** introduced the **Multitrait-Multimethod (MTMM) matrix** to evaluate construct validity by measuring **several traits, each by several methods**, then examining the correlation matrix. The diagonals and blocks each carry meaning:

- **Reliability diagonal (monotrait-monomethod)**: same trait, same method (the test's reliability). These should be the **highest** values in the matrix.
- **Validity diagonal (monotrait-heteromethod)**: **same trait measured by different methods**. These show **convergent validity** and should be **high** (a trait should correlate with itself even across methods).
- **Heterotrait-monomethod triangle**: **different traits measured by the same method**. These index **method variance / common-method bias**; they should be **low** (and lower than the validity diagonals).
- **Heterotrait-heteromethod triangle**: **different traits, different methods**. These should be the **lowest** values.

Campbell and Fiske's criteria for good construct validity: (1) validity (monotrait-heteromethod) values are significantly **> 0** and high (convergence), (2) validity values **> heterotrait-heteromethod** values, (3) validity values **> heterotrait-monomethod** values (discriminant), and (4) the same pattern of trait inter-correlations holds across all method blocks.

### Nomological networks

**Cronbach and Meehl (1955)** proposed the **nomological network**: the interlocking system of theoretical laws and observable relationships that defines a construct. A construct gains validity when its measure relates to other constructs **exactly as theory predicts** (e.g. a new anxiety scale should correlate positively with stress and negatively with calmness if the theory of anxiety is correct). Construct validation is thus the process of confirming the measure's place within this lawful network of relationships.

## High-Yield Recap

- **CTT: X = T + E**; assumptions **E(E) = 0, rho_TE = 0, rho_E1E2 = 0**; variance splits as **sigma^2_X = sigma^2_T + sigma^2_E**.
- **Reliability rxx = sigma^2_T / sigma^2_X**; reliability index = **sqrt(rxx)**.
- **SEM = SD * sqrt(1 - rxx)**; +/- 1 SEM ~ 68% CI, +/- 1.96 SEM ~ 95% CI.
- **Spearman-Brown (split-half): r_full = 2r / (1 + r)**; lengthening a test raises reliability.
- **Cronbach's alpha** = mean of all split-halves, for **multi-point** items; **>= 0.70** acceptable; lower-bound estimate.
- **KR-20** for **dichotomous** items; **KR-21** assumes equal item difficulty and is the most conservative (**KR-21 <= KR-20**).
- **Correction for attenuation: r_true = r_xy / sqrt(rxx * ryy)**; reliability caps validity.
- **Item difficulty p** = proportion correct (higher = easier); ideal **p ~ 0.50** for max variance.
- **Discrimination d** = upper 27% minus lower 27% (Ebel: **>= 0.40 very good, < 0.20 discard**); negative d = miskeyed. **Point-biserial** = item-total correlation.
- **IRT/latent trait (theta)**: **1PL/Rasch = b (difficulty, 50% point)**; **2PL adds a (discrimination/slope)**; **3PL adds c (guessing, lower asymptote ~0.25 for 4-option)**.
- **Information functions** replace reliability; **TIF = sum of item info**; **SE(theta) = 1/sqrt(I(theta))**.
- **DIF** = equal-theta groups differ in p(correct) = item bias; detected via **Mantel-Haenszel**; uniform vs non-uniform.
- **Validity types**: content (face = weakest), criterion (concurrent vs predictive), construct (convergent high, discriminant low).
- **Lawshe CVR = (n_e - N/2) / (N/2)**, range -1 to +1; retain above tabled critical value; average = CVI.
- **SEest = SD_y * sqrt(1 - r^2)**.
- **MTMM (Campbell & Fiske 1959)**: reliability diagonal highest; **validity (monotrait-heteromethod) = convergent, should be high**; **heterotrait-monomethod = method bias, should be low**; heterotrait-heteromethod lowest.
- **Nomological network (Cronbach & Meehl 1955)** = lawful web of relationships defining a construct.
