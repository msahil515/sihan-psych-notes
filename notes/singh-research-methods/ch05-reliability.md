---
date: 2026-05-29
book: "Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh)"
subject: "Research Methodology, Statistics & Psychological Testing"
chapter: 5
tags: [reliability, psychometrics, classical-test-theory, generalizability-theory, KR20, coefficient-alpha, standard-error-of-measurement, MET-2026]
---

# Reliability

Chapter 5 covers the theoretical foundations and practical methods of estimating the reliability of psychological test scores. It moves from classical test theory (CTT) and domain sampling through the four main reliability methods, then treats standard error of measurement, speed-test reliability, factors that affect reliability, and derived statistics (index of reliability, true-score estimation, difference-score reliability, composite-score reliability).

---

## History and Theory of Reliability

### Why Measurement Error Matters

Psychologists measure complex, unobservable human characteristics (intelligence, aggressiveness, beauty) for which no rigid yardstick exists. This absence of fixed standards allows **measurement error** to enter scores, sometimes inflating them and sometimes depressing them (Nunnally and Bernstein, 1994). The central question in test theory is: how much do scores differ from one another because of error rather than because of true differences in the characteristic?

### Foundational Contributors

| Scholar | Contribution | Year |
|---|---|---|
| **Charles Spearman** | Theorized about measurement error; published the foundational paper on reliability, "Measuring the Nature of Association Between Test Scores" | 1904 |
| **Karl Pearson** | Developed the **product-moment method of correlation**, the statistical bedrock of reliability coefficients | 1896 |
| **Kuder and Richardson** | Derived K-R20 and K-R21 formulas for internal consistency | 1937 |
| **Cronbach et al.** | Formulated **Generalizability Theory** and Coefficient Alpha | 1951 / 1972 |
| **Lord and Novick** | Extended classical theory of reliability | 1968 |
| **Feldt and Brennan** | Further developed domain sampling reliability | 1989 |

Reliability theory integrates two core ideas: **sampling error** and **correlation**. Spearman's 1904 paper provided the mathematical proof that the association between test scores could be used to measure reliability.

---

### Classical Test Theory (CTT)

**Classical Test Theory (CTT)**, premised on the **true score model** (Feldt, 1984), is the dominant framework. It was introduced by Spearman approximately 100 years before the text was written.

#### The Fundamental Equation

$$x = T + e \quad \text{...(5.1)}$$

- **x** = obtained (observed) score
- **T** = true score (score free from all error)
- **e** = error score

**True score** is defined as the score we would obtain if there were no errors of measurement; operationally it is the mean of scores from an unlimited number of repeated testings of the same person on the same test.

#### Core Assumptions of CTT

1. **True scores and errors are uncorrelated** (r between T and e = 0)
2. **Errors on different measures are uncorrelated** (r between e on test 1 and e on test 2 = 0)
3. **Errors of measurement are random** (not systematic): they are equally likely to be positive or negative and average to zero over many measurements.

Because errors are random, the mean of repeated measurements of the same person converges to the true score.

#### Variance Partition

Since x = T + e and correlations among components are zero:

$$\sigma^2_o = \sigma^2_t + \sigma^2_e \quad \text{...(5.2)}$$

- **σ²_o** = total (obtained) score variance
- **σ²_t** = true score variance
- **σ²_e** = error score variance

#### Logical Definition of the Reliability Coefficient

$$r_{tt} = \frac{\sigma^2_t}{\sigma^2_o} \quad \text{...(5.3)}$$

Reliability is the **proportion of total variance that is true variance**. Equivalently:

$$r_{tt} = 1 - \frac{\sigma^2_e}{\sigma^2_o} \quad \text{...(5.4)}$$

**Worked example from Table 5.2:** True variance = 43,191; Total variance = 58,369  
r_tt = 43,191 / 58,369 = **0.74** (74% of obtained variance is true variance)

#### Types of Error Scores

| Type | Description | Effect on Mean |
|---|---|---|
| **Random (chance) error** | Fluctuates unpredictably; positive sometimes, negative sometimes | Mean of errors → 0 in long run |
| **Systematic (constant) error** | Consistently biases in one direction (e.g., defective scale always reads high) | Mean of errors ≠ 0; does not cancel out |

Systematic errors threaten **validity** more than reliability; random errors threaten **reliability** directly.

---

### Domain Sampling Model

The **domain sampling model** addresses the problem of using a limited number of items to represent an unlimited domain of possible items.

- If a person spelled every word in the English language correctly, the percentage correct would be the **universe score** (true score for the domain).
- Because administering the entire domain is impossible, a researcher selects a sample of items. The **reliability** under this model is the ratio of observed-score variance to universe-score variance (Feldt and Brennan, 1989).
- As the number of items drawn from the domain **increases**, observed scores approach true scores and **reliability increases**.
- The model assumes items randomly drawn from a domain should each correlate more highly with the total score than with one another.

---

### Generalizability Theory

**Generalizability Theory** (G-Theory) was presented by **Cronbach et al. (1972)** as an alternative to CTT.

Key distinctions from CTT:

| Feature | CTT | Generalizability Theory |
|---|---|---|
| Nature of error | Single, undifferentiated, always random | Multiple, specific, some systematic |
| Focus | Is the test reliable? | Over what conditions can scores be generalized? |
| Analytic tool | Correlation | Analysis of Variance (ANOVA) |

CTT's most serious weakness (per Cronbach) is treating measurement error as a single entity. G-Theory identifies **both systematic and random sources of inconsistency** and asks: "What are the conditions over which one can generalize?" Factors such as time of testing, rater, and setting can each be isolated as distinct variance components using ANOVA.

Lord and Novick (1968) and Cronbach et al. (1972) showed that CTT is a **special case** of G-Theory.

Practical illustration (Table 5.1): Three psychologists each scored the same individual three times. Scores varied across psychologists (systematic difference) but were stable across time. G-Theory allows the researcher to identify which source of variance (psychologist vs. time) limits generalizability.

---

## Meaning of Reliability

**Reliability** refers to the **precision or consistency** of measurement. A reliable test produces the same or nearly the same results for an examinee on different occasions (Anastasi and Urbina, 1997, p. 88).

Formal definition: "Reliability refers to the consistency of scores obtained by the same individual when re-examined with the same test on different occasions, or with different but equivalent tests, or under other variable examining conditions."

### Two Dimensions of Consistency

| Term | Definition |
|---|---|
| **Temporal stability** | Consistency of scores over time (test-retest) |
| **Internal consistency** | Consistency of scores across items or equivalent forms of a single administration |

### Three Critical Clarifications

1. **Reliability is of test scores, not of the test itself.** A test may yield different reliability estimates for different groups or situations. We cannot speak of "the reliability of a test" as a fixed property.

2. **Reliability is necessary but not sufficient for validity.** A test can be highly reliable yet measure the wrong construct. Low reliability guarantees low validity; high reliability does not guarantee high validity.

3. **Reliability is always specific to a particular type of consistency.** A test can be temporally stable but internally inconsistent, or vice versa.

### Logical/Technical Meaning

If measurement were completely error-free, the reliability coefficient would equal **+1.00** (perfect). In practice, every measurement contains some error, so reliability is always less than perfect. The reliability coefficient is interpreted as the proportion of true variance in total variance (Equations 5.3 and 5.4 above).

Reliability is **not all-or-none**; it is always a matter of degree.

---

## Methods (Types) of Reliability

There are **four main methods** of estimating the reliability coefficient:

| Method | Also Called | Type |
|---|---|---|
| Test-Retest | Coefficient of stability | Temporal stability |
| Internal Consistency | Split-half, K-R, alpha | Homogeneity |
| Alternate-Forms | Parallel-forms, equivalence, comparable-forms | Equivalence |
| Scorer (Rater) Reliability | Inter-rater reliability | Consistency across scorers |

Test-retest and alternate-forms are **not** internal consistency procedures; they compare results across two independent processes.

---

## Test-Retest Reliability

### Definition and Procedure

**Test-retest reliability** is estimated by administering the same test twice to the same sample with a reasonable time gap and correlating the two sets of scores.

The resulting coefficient is the **temporal stability coefficient** (also called **coefficient of stability**). A high coefficient indicates that examinees retain their relative ranks across administrations.

### Optimal Time Interval

- **Too short**: Inflates reliability due to **practice effects** and **carryover** (memory of previous answers).
- **Too long**: Deflates reliability due to genuine changes in the examinee.
- The text recommends a **fortnight (two weeks)** as the most convenient gap.

### Advantages

- The most appropriate method for both **speed tests** and **power tests**.
- Most appropriate for **homogeneous tests**.

### Sources of Error Variance in Test-Retest

| Source | Effect |
|---|---|
| Physical/health/emotional changes in examinee | Lower reliability |
| Environmental changes across administrations | Lower reliability |
| Maturational effects (especially in young examinees) | Lower reliability |
| Practice and skill acquisition | Can inflate reliability (increases true variance) |
| Memory of first-administration answers | Can inflate reliability |

---

## Internal Consistency Reliability

**Internal consistency reliability** indicates the **homogeneity** of a test: the degree to which all items measure the same construct. A high internal consistency means a high inter-item correlation.

### Split-Half Method

The **split-half method** divides the test into two equal (or nearly equal) halves and correlates scores on the two halves. The correlation gives reliability of the **half-test**, which is then corrected to estimate reliability of the whole test.

**Best practice for splitting:** Odd-even (odd-numbered items vs. even-numbered items), because a simple first-half vs. second-half split confounds difficulty level (easier items tend to be at the beginning).

Each examinee receives two scores: score on odd items and score on even items. These are correlated to get r_hh (reliability of the half test).

#### Spearman-Brown Prophecy Formula (for split-half)

$$r_{tt} = \frac{2 \cdot r_{hh}}{1 + r_{hh}} \quad \text{...(5.5)}$$

- **r_tt** = reliability of the whole test
- **r_hh** = reliability of the half test

**Example:** If r_hh = 0.70:

$$r_{tt} = \frac{2 \times 0.70}{1 + 0.70} = \frac{1.40}{1.70} = 0.823$$

#### Advantages of Split-Half

- All data collected in a **single administration**; no second-testing variability.
- Eliminates between-session environmental effects.

#### Disadvantages of Split-Half

- Temporary conditions during the one session affect both halves in the same direction, leading to **overestimation or underestimation**.
- Different methods of splitting yield different reliability coefficients.
- **Must not be used with speed tests** (spuriously inflated results — see "Reliability of Speed Tests" section).

---

### Rulon Formula

Proposed by **Rulon**, this formula estimates internal consistency without needing a step-up (Spearman-Brown) correction.

**Requirement:** Test divided into two halves (odd-even or random assignment).

$$r_{tt} = 1 - \frac{\sigma^2_d}{\sigma^2_t} \quad \text{...(Rulon)}$$

- **σ²_d** = variance of the difference scores (odd score minus even score for each examinee)
- **σ²_t** = variance of the total test scores

The difference between the two half-scores is treated as the **error score** for each examinee.

**Example (Table 3.8 data):**  
σ²_d = 0.25; σ²_t = 1.65  
r_tt = 1 - (0.25/1.65) = 1 - 0.1519 = **0.85**

**Advantage over Spearman-Brown:** Does not require computing the half-test reliability coefficient first.

---

### Flanagan Formula

Proposed by **Flanagan**, this formula is similar to Rulon's but uses the variances of each half separately rather than the variance of difference scores.

$$r_{tt} = 2\left[1 - \frac{\sigma^2_1 + \sigma^2_2}{\sigma^2_t}\right] \quad \text{...(Flanagan)}$$

- **σ²_1** = variance of scores on the first (odd) half
- **σ²_2** = variance of scores on the second (even) half
- **σ²_t** = variance of total scores

**Example (same data):** σ²_1 = 2.00; σ²_2 = 2.25; σ²_t = 1.65 (scaled)  
Yields r_tt ≈ **0.85** (same result as Rulon — this serves as a computation check)

Both Rulon and Flanagan formulas apply to the **full-test reliability** directly and are preferred for inter-item consistency testing.

---

### Kuder-Richardson Formulas (K-R20 and K-R21)

**Kuder and Richardson (1937)** developed these formulas to overcome limitations of split-half methods. K-R20 and K-R21 are the most widely used; mathematically, the K-R reliability coefficient is the **mean of all possible split-half coefficients** (Cronbach, 1951).

#### Requirements for K-R Formulas

1. All items must be **homogeneous** (measuring the same factor in the same proportion; test should be unifactorial).
2. Items scored **dichotomously** (0 = wrong, 1 = correct).
3. For K-R20: items should **not vary greatly in difficulty**. For K-R21: items must be of **equal difficulty**.

#### K-R20 Formula

$$KR_{20} = \frac{n}{n-1} \left[\frac{s_t^2 - \sum pq}{s_t^2}\right] \quad \text{...(5.8)}$$

- **n** = number of items
- **s²_t** = variance of total test scores
- **p** = proportion of examinees answering each item correctly
- **q** = 1 - p (proportion answering incorrectly)
- **Σpq** = sum of p×q products across all items

K-R20 requires a **complete item-analysis worksheet** (knowing p for every item). It is the **basic formula** for internal consistency.

#### K-R21 Formula

K-R21 is a simplification of K-R20, assuming all items have the same difficulty value:

$$KR_{21} = \frac{n}{n-1} \left[\frac{s_t^2 - n\bar{p}\bar{q}}{s_t^2}\right] \quad \text{...(5.9)}$$

Where:  
- **p̄** = M/n (mean difficulty; M = mean total score, n = number of items)  
- **q̄** = (n - M)/n = 1 - p̄

Simplified further:

$$r_{tt} = \frac{nM(n-M)}{s_t^2(n-1)} \quad \text{...(5.10)}$$

K-R21 uses only **total score statistics** (mean and SD), making it useful for estimating reliability in advance. K-R21 **always underestimates** the coefficient when items differ in difficulty (because the equal-difficulty assumption is violated).

**Comparison K-R20 vs K-R21:**
- K-R20 requires item-level p values; K-R21 requires only M and s²_t.
- K-R21 underestimates K-R20 when item difficulty is heterogeneous.
- Both underestimate split-half reliability when item difficulties differ widely.

#### Modifications to K-R Formulas

| Scholar | Year | Modification |
|---|---|---|
| **Dressel** | 1940 | Extended K-R for items with **differential scoring weights** (e.g., +2, +1, 0): r = (n/n-1)[1 - ΣW²pq/σ²_x] |
| **Ferguson** | 1951 | Extended K-R for items with **more than two score levels** (e.g., +1, 0, -1) |
| **Tucker** | 1949 | Modified K-R20 with an additional term for variance of item difficulty proportions: r_n = (n/n-1)[(σ²_x - Σpq)/σ²_x - nσ²_c] |

#### Limitations of K-R Formulas

- Underestimate reliability of **heterogeneous tests** (measuring multiple traits).
- Underestimate reliability when **items differ widely in difficulty**.
- Must **not be used with speed tests**.

---

### Coefficient Alpha (Cronbach's Alpha)

**Coefficient alpha (α)**, formulated by **Cronbach (1951)** (also Kaiser and Michael, 1975), is the generalization of K-R20 to tests where items are **not scored dichotomously** (0/1). Examples: essay exams, Likert-type scales (Always/Sometimes/Rarely/Never).

$$c\alpha = \frac{n}{n-1} \left[1 - \frac{\sum \sigma^2_i}{\sigma^2_x}\right] \quad \text{...(5.14)}$$

- **n** = number of items
- **Σσ²_i** = sum of variances of individual item scores across all examinees
- **σ²_x** = variance of total test scores

The key difference from K-R20: **Σpq** (dichotomous item variance) is replaced by **Σσ²_i** (continuous item variance).

#### Properties of Coefficient Alpha

| Property | Detail |
|---|---|
| Range | 0 (no internal consistency) to 1 (perfect internal consistency) |
| Relation to split-half | Alpha is the **smallest** of all consistency estimates; it gives lower estimates than split-half with highs |
| Relation to K-R20 | Alpha is mathematically the **weighted average of all possible split-half reliability coefficients** |
| Accepted threshold | α ≥ **0.70** (minimum acceptable); α ≥ **0.80** (preferred) in psychological/educational research |
| Negative alpha | Indicates something wrong with test construction or an inappropriate reliability model |
| Sources of error variance | Content sampling and content heterogeneity |

Cronbach's alpha is currently regarded as the **most general method** of estimating internal consistency.

---

## Alternate-Forms Reliability

**Alternate-forms reliability** (also called **parallel-forms reliability**, **equivalence reliability**, or **comparable-forms reliability**) requires constructing **two equivalent forms** of the test and administering both to the same sample.

### Administration Variants

| Variant | Procedure | Coefficient Name |
|---|---|---|
| **Immediate** | Both forms given same day | Coefficient of equivalence |
| **Delayed** | Forms given with time gap (typically a fortnight) | Alternate-form delayed reliability (combines equivalence + stability) |

The correlation (Pearson's r) between the two sets of scores is the reliability estimate.

### Criteria for Parallel (Equivalent) Forms (Freeman, 1962, p. 72)

1. The **number of items** in both forms must be the same.
2. Items must be similar in **content, difficulty range, and adequacy of sampling**.
3. **Distribution of item difficulty** must be similar across forms.
4. Items must have **equal degree of homogeneity** (shown by inter-item correlations or item-total correlations).
5. **Means and standard deviations** of both forms must be equal or nearly so.
6. **Mode of administration** must be the same or similar.

Gulliksen (1950) defined parallel tests as having: equal expected scores, equal true variance, equal error variance, and equal inter-item correlations.

### Advantages

- Reduces **practice effects** (examinees cannot recall specific item answers).
- Most appropriate when constructing a **speed test**.
- Can be applied to power tests as well.

### Disadvantages and Sources of Error

- Extremely **labour-intensive**: all items must be written twice.
- Achieving complete equivalence is rarely, if ever, possible.
- Error variance sources: **content sampling** (two forms sample different content from the domain) and **time interval**.

---

## Scorer (Rater) Reliability

**Scorer reliability** (also called **rater reliability** or **inter-rater reliability**) measures the **consistency between two or more scorers**, or the same scorer on two different occasions, when scoring subjectively.

Used specifically for tests with subjective scoring: **projective tests**, **creativity tests**, **essay examinations**.

**Procedure:** Two scorers independently score the same set of responses; the correlation between their scores is the scorer reliability coefficient.

**Source of error variance:** Inter-rater differences.

---

## Satisfactory Size for the Reliability Coefficient

Guilford (1956) provided guidance based on the **purpose** of the test:

| Purpose of Test | Minimum Acceptable Reliability |
|---|---|
| Individual diagnosis (intelligence, aptitude, achievement tests) | **0.90 or above** |
| Comparing group means or sub-group trends | As low as **0.65** |

### When High Reliability is Essential

- Tests used for **final decisions** about individuals (e.g., military placement, clinical diagnosis).
- Decisions made on the basis of relatively **small individual differences**.

### When Lower Reliability is Acceptable

- Tests used for **preliminary decisions** only.
- Tests assessing **group trends** rather than individual differences.

### Bandwidth-Fidelity Dilemma

Coined from communication theory by **Shannon and Weaver (1949)** and applied to testing by **Cronbach and Gleser (1965)**:

- **Bandwidth** = the breadth of information a test covers (how many traits/domains it samples).
- **Fidelity** = the accuracy/precision with which information is transmitted (reliability).

The dilemma: **the greater the bandwidth, the lower the fidelity** (and vice versa). A broad test sampling many domains sacrifices precision (reliability), while a narrow, focused test can be highly reliable but limited in coverage. This represents a fundamental conflict between **breadth** and **precision** in measurement. Practically, researchers must decide the balance based on the purpose of the test.

---

## Standard Error of Measurement

### Definition

The **standard error of measurement (SE_meas)** is defined as the **standard deviation of the errors of measurement** of a test. It is the standard deviation of an individual's hypothetical score distribution across repeated testings.

Unlike the reliability coefficient, **SE_meas is not influenced by the variability or range of scores** in the group tested. This makes it more useful for interpreting individual scores.

### Formula

$$SE_{meas} = S_t\sqrt{1 - r_{tt}} \quad \text{...(5.16)}$$

- **SE_meas** = standard error of measurement
- **S_t** = standard deviation of test scores
- **r_tt** = reliability coefficient

**Example:** r_tt = 0.90, S_t = 10.0  
SE_meas = 10.0√(1 - 0.90) = 10.0 × 0.316 = **3.16**

### Using SE_meas for Confidence Intervals

The true score is treated as the mean of repeated measurements. Confidence intervals around an obtained score are:

| Confidence Level | Formula | Meaning |
|---|---|---|
| 68% | Obtained score ± 1 SE_meas | True score within this range 68% of the time |
| 95% | Obtained score ± 2 SE_meas | True score within this range 95% of the time |
| 99% | Obtained score ± 3 SE_meas | True score within this range 99% of the time |

**Example:** Obtained score = 21, SE_meas = 3.16  
95% CI = 21 ± 6.32 (i.e., 14.68 to 27.32)  
99% CI = 21 ± 9.48 (i.e., 11.52 to 30.48)

### Boundary Values

| Reliability | SE_meas |
|---|---|
| r_tt = 1.00 (error-free) | SE_meas = 0 |
| r_tt = 0.00 (entirely error) | SE_meas = S_t |

The **smaller** the SE_meas, the **more reliable** the test. SE_meas is independent of any particular category of test scores.

---

## Reliability of Speed Tests

### Distinction Between Speed and Power Tests

- **Power test**: measures the level of difficulty a person can reach; no strict time limit; nearly all items attempted.
- **Speed test**: measures rate of performance; items are easy but many; differences in scores reflect differences in speed.

In practice, most tests combine both elements.

### Problem with Split-Trial Methods on Speed Tests

**Split-half, K-R, and Cronbach's alpha are inapplicable to pure speed tests.** They yield **spuriously inflated** (artifactually perfect or near-perfect) reliability coefficients.

Explanation: In a pure speed test, every examinee gets all attempted items correct. If individual A completes 30 items, their odd score = 15, even score = 15. Individual B completes 50, odd = 25, even = 25. The odd-even correlation will be **1.00**, suggesting perfect reliability — which is entirely spurious (it only reflects that people answered consistently within what they attempted, not across different occasions or forms).

### Acceptable Alternatives for Speed Test Reliability

1. **Test-retest method**: administer the same test twice.
2. **Alternate-forms method**: administer two equivalent forms.
3. **Split-half by time rather than content**: divide total time into two halves, administer each half separately, correlate the two sets of scores.
4. **Separately timed halves**: print test on separate pages; administer each half with half the total time limit; correlate.
5. **Quarter method**: divide total time into four quarters; combine scores from quarters 1 and 4 as one half-score, quarters 2 and 3 as the other half-score; apply Rulon's formula. This balances practice, fatigue, and other cumulative effects. Most satisfactory when item difficulty is uniform.

---

## Factors Influencing Reliability of Test Scores

Factors fall into two categories: **extrinsic** (outside the test) and **intrinsic** (within the test).

### Extrinsic Factors

#### 1. Group Variability

- **Homogeneous group** (narrow ability range): **lowers** reliability coefficient (when all scores cluster, the correlation shrinks; if all examinees score identically, variance = 0 and correlation is undefined/zero).
- **Heterogeneous group** (wide ability range): **raises** reliability coefficient.

Rule: Reliability coefficients are partially artefacts of the variance in the sample; always interpret reliability in the context of sample variability.

#### 2. Guessing

Guessing introduces error into scores (examinee's true position on the construct is obscured). It lowers reliability.

- True-false/two-alternative items: 50% probability of guessing correctly.
- Multiple-choice (4 options): 25% probability.
- **Second-guessing** (test-wiseness, using clues) creates systematic differences in guessing accuracy across examinees, further reducing reliability.

#### 3. Environmental Conditions

Non-uniform testing environments (different lighting, noise, temperature, time of day across administrations) introduce variance unrelated to the construct, reducing reliability.

#### 4. Motivation of Examinees

Low motivation (fatigue, anxiety, interfering events) introduces random error. Variability in examinee effort across occasions lowers consistency.

---

### Intrinsic Factors

#### 1. Length of Test

A **longer test** yields higher reliability (samples more of the domain; reduces the proportional weight of any single item's error). This is quantified by the **Spearman-Brown formula for lengthening**:

$$r_{nn} = \frac{n \cdot r_{11}}{1 + (n-1) r_{11}} \quad \text{...(5.17)}$$

- **r_nn** = reliability of the lengthened test
- **n** = factor by which test length is increased
- **r_11** = reliability of the original test

**Example:** Original test: 200 items, r_11 = 0.80. Doubled to 400 items (n = 2):

$$r_{nn} = \frac{2 \times 0.80}{1 + (2-1)(0.80)} = \frac{1.60}{1.80} = 0.89$$

Conversely, **shortening** a test reduces reliability (n < 1).

**Spearman-Brown formula for determining the required lengthening factor** to achieve a target reliability:

$$n = \frac{r_n(1 - r_{11})}{r_{11}(1 - r_n)} \quad \text{...(5.18)}$$

- **n** = factor by which the test must be lengthened
- **r_n** = desired (target) reliability
- **r_11** = current reliability

**Example:** Current reliability = 0.60; desired reliability = 0.90:

$$n = \frac{0.90(1-0.60)}{0.60(1-0.90)} = \frac{0.90 \times 0.40}{0.60 \times 0.10} = \frac{0.36}{0.06} = 6$$

The test must be **lengthened 6 times** to achieve r = 0.90.

#### Key Values for Spearman-Brown Doubling

| Initial Reliability | After Doubling Length |
|---|---|
| 0.50 | 0.67 |
| 0.67 | 0.80 |
| 0.80 | 0.89 |

**Assumptions for adding items:** (a) New items must measure the same trait as the original items (same average difficulty and inter-item correlation). (b) Additional items must not adversely affect examinee motivation.

#### 2. Range of Total Scores

High variability in total scores (large SD) → high reliability. When all scores cluster near the same value, the reliability coefficient collapses toward zero (no variance to correlate).

#### 3. Homogeneity of Items

**Homogeneity** = all items measure the same construct (high inter-item correlation). A homogeneous test yields high reliability. Heterogeneous items (measuring different traits) produce low or zero reliability.

#### 4. Difficulty of Items

Items of **moderate difficulty** (p = 0.50, ideally in the range 0.40-0.60) yield the highest reliability. Very easy items (p close to 1.0) or very hard items (p close to 0.0) reduce variance and contribute nothing to reliability.

#### 5. Discrimination

Highly **discriminating items** (high item-total correlation) increase reliability. Non-discriminating items (near-zero item-total correlation) contribute error and lower reliability.

#### 6. Score (Rater) Reliability

If scorers do not agree, inter-rater inconsistency adds error variance, lowering overall reliability.

---

## How to Improve Reliability of Test Scores

### General Recommendations

1. Use a **heterogeneous group** of examinees.
2. Use **homogeneous items** (all measuring the same trait).
3. Make the **test sufficiently long**.
4. Set item difficulty in the range **0.40-0.50-0.60**.

### Three Systematic Approaches

#### Approach 1: Increase Test Length

Use Equation 5.17 or 5.18 (Spearman-Brown) to determine how many items to add. New items must measure the same property and have comparable difficulty and inter-item correlations.

#### Approach 2: Discard Low-Reliability Items

Conduct **item analysis**: compute the correlation between each item and the total test score. Items with low item-total correlation are probably measuring something different; discarding them raises the overall reliability. Also apply factor analysis to confirm unifactorial structure.

- High inter-factor correlation but low item-total correlation: item measures a different construct.
- Zero item-total correlation: no one differs in response to it; contribute nothing.

#### Approach 3: Correction for Attenuation

(Covered in Chapter 6.) This formula corrects validity coefficients for the attenuating effect of unreliability, allowing estimation of the correlation that would be obtained if both measures were perfectly reliable.

---

## Estimation of True Scores

Since the true score is the mean of unlimited measurements (impossible to obtain directly), it is estimated via regression:

$$\hat{X}_i = \bar{X}_t + r_1(X_o - \bar{X}_o) \quad \text{...(5.19)}$$

- **X̂_i** = estimated true score
- **X̄_t** = mean of true scores (≈ mean of obtained scores)
- **r_1** = reliability coefficient of the test
- **X_o** = obtained score of the examinee
- **X̄_o** = mean of obtained scores

The **standard error of the estimated true score**:

$$SE_e = \sigma\sqrt{r_1 - r_1^2} \quad \text{...(5.20)}$$

- **σ** = standard deviation of obtained scores

**Worked Example:**  
Mohan's obtained score = 50; test M = 100; SD = 10; r_tt = 0.80.

Estimated true score:  
X̂ = 100 + 0.80(50 - 100) = 100 + (-40) = **60**

SE of estimated true score:  
SE_e = 10√(0.80 - 0.64) = 10√(0.16) = 10 × 0.4 = **4**

95% CI for true score: 60 ± (1.96 × 4) = 60 ± 7.84 → [52.16, 67.84]  
99% CI: 60 ± (2.58 × 4) = 60 ± 10.32 → [49.68, 70.32]

Note: High reliability (0.80) reduces measurement error, but true score estimation via this method is not highly satisfactory for final decisions.

---

## Index of Reliability

The **index of reliability** is defined as the correlation between obtained scores and true scores. It is the square root of the reliability coefficient:

$$r_{xt} = \sqrt{r_{xx}} \quad \text{...(5.21)}$$

- **r_xt** = index of reliability (correlation between obtained and true scores)
- **r_xx** = reliability coefficient

This statistic provides the **maximum possible correlation** between a test and any external criterion (i.e., the ceiling on validity).

**Example:** r_xx = 0.64 → r_xt = √0.64 = **0.80**

This means the test can correlate with a criterion at most 0.80, regardless of how valid the criterion is.

---

## Reliability of Difference Score

Researchers frequently compare two sets of scores (e.g., pre-test vs. post-test; mathematics vs. verbal score). The reliability of the **difference** between scores on X and Y is:

$$r_{dd} = \frac{\frac{r_{xx} + r_{yy}}{2} - r_{xy}}{1 - r_{xy}} \quad \text{...(5.22)}$$

- **r_dd** = reliability of the difference score
- **r_xx** = reliability of measure X
- **r_yy** = reliability of measure Y
- **r_xy** = correlation between X and Y

### Key Principle

**The higher the correlation between X and Y, the lower the reliability of their difference score.** When X and Y are highly correlated, examinees' true scores on both measures are similar, so differences largely reflect measurement error rather than true differences. The difference score is thus unstable and unreliable.

This is why researchers must be cautious when interpreting difference scores derived from highly correlated measures (e.g., change scores in pre/post designs).

---

## Reliability of Composite Score

A **composite score** is the sum of scores across several different tests. The reliability of such a composite is generally **higher** than the reliability of any single component test.

$$r_{cc} = \frac{k\bar{r}}{1 + (k-1)\bar{r}_{ij}} \quad \text{...(5.23)}$$

- **r_cc** = reliability of the composite score
- **k** = number of tests combined
- **r̄** = average reliability of the individual tests
- **r̄_ij** = average inter-correlation among the tests

### Key Principles

- The more tests combined, the higher the composite reliability (analogous to lengthening a test).
- Higher inter-correlations among component tests → higher composite reliability.
- Combining a small number of **highly interrelated tests** achieves the same effect as adding correlated items to a single test.
- The principle parallels the **domain sampling model**: more samples from the same domain = more reliable estimate.

---

## Key Terms

| Term | Definition |
|---|---|
| **Reliability** | Consistency or precision of test scores; formally, the proportion of total score variance that is true score variance |
| **True score (T)** | Hypothetical error-free score; mean of an infinite number of measurements of the same person on the same test |
| **Error score (e)** | Difference between obtained score and true score (x - T) |
| **Obtained score (x)** | Actual score recorded; equals T + e |
| **Random error** | Unsystematic, unpredictable error that averages to zero over many measurements |
| **Systematic error** | Constant, directional bias that does not cancel out; threatens validity more than reliability |
| **True score variance (σ²_t)** | Variance attributable to genuine differences in the measured construct |
| **Error variance (σ²_e)** | Variance attributable to measurement error |
| **Reliability coefficient (r_tt)** | Ratio of true score variance to total score variance; ranges from 0 to 1 |
| **Temporal stability** | Consistency of scores across time; measured by test-retest reliability |
| **Internal consistency** | Consistency of scores across items within a single administration |
| **Coefficient of stability** | Another name for test-retest reliability coefficient |
| **Coefficient of equivalence** | Correlation between two parallel forms given simultaneously |
| **Split-half reliability** | Internal consistency estimated by dividing a test into two halves and correlating scores |
| **Spearman-Brown formula** | Formula for estimating whole-test reliability from half-test reliability, or for predicting reliability after lengthening |
| **Rulon formula** | Internal consistency formula using variance of difference scores: r_tt = 1 - σ²_d/σ²_t |
| **Flanagan formula** | Internal consistency formula using variance of each half: r_tt = 2[1 - (σ²_1 + σ²_2)/σ²_t] |
| **K-R20** | Kuder-Richardson formula for internal consistency of dichotomously scored items; requires item-level p values |
| **K-R21** | Simplified K-R20 assuming equal item difficulty; requires only mean and SD of total scores |
| **Coefficient alpha (Cronbach's α)** | Most general internal consistency estimate; extends K-R20 to non-dichotomous scoring |
| **Scorer reliability** | Reliability measuring agreement between two or more raters scoring the same responses |
| **Standard error of measurement (SE_meas)** | Standard deviation of measurement errors; SE_meas = S_t√(1 - r_tt) |
| **Index of reliability** | Square root of reliability coefficient; maximum possible validity coefficient r_xt = √r_xx |
| **Domain sampling model** | Conceptualizes reliability as ratio of observed-score variance to universe-score variance; error = sampling from a limited domain |
| **Generalizability theory** | Cronbach's framework identifying multiple, specific sources of error variance using ANOVA; CTT is a special case |
| **Bandwidth-fidelity dilemma** | Conflict between breadth of measurement (bandwidth) and precision/reliability (fidelity); more bandwidth = less fidelity |
| **Universe score** | True score under the domain sampling model; score if all items in the domain were administered |
| **Reliability of difference score (r_dd)** | Reliability of the difference between two correlated measures; decreases as correlation between measures increases |
| **Reliability of composite score (r_cc)** | Reliability of a sum of multiple test scores; generally higher than any individual test's reliability |
| **Correction for attenuation** | Statistical correction that removes the attenuating effect of unreliability on a validity coefficient |
| **Item homogeneity** | Degree to which all items measure the same underlying construct; high homogeneity → high internal consistency |
| **Bandwidth** | Breadth/range of information or traits a test covers |
| **Fidelity** | Accuracy/precision of measurement; analogous to reliability |
| **Power test** | Test measuring depth/difficulty of performance; no strict time limit |
| **Speed test** | Test measuring rate of performance; all items easy but many |

---

## Key People / Tests

| Name | Year | Contribution |
|---|---|---|
| **Charles Spearman** | 1904 | Foundational paper on reliability theory; classical test theory; true score concept |
| **Karl Pearson** | 1896 | Product-moment correlation (r); statistical basis for reliability coefficients |
| **Kuder and Richardson** | 1937 | K-R20 and K-R21 formulas for internal consistency reliability |
| **Lee J. Cronbach** | 1951 | Coefficient alpha; generalizability theory (1972); bandwidth-fidelity application |
| **Cronbach, Gleser** | 1965 | Applied bandwidth-fidelity dilemma to psychological testing |
| **Shannon and Weaver** | 1949 | Information theory; original bandwidth-fidelity framework |
| **Lord and Novick** | 1968 | Extended classical reliability theory; established CTT as special case of G-theory |
| **Feldt and Brennan** | 1989 | Domain sampling model; reliability as ratio of observed to universe-score variance |
| **Guilford** | 1956 | Guidelines for satisfactory size of reliability coefficients (0.90 for individual diagnosis; 0.65 for group comparisons) |
| **Guilford and Fruchter** | 1973 | Described split-half reliability; classic psychometrics text |
| **Gulliksen** | 1950 | Formal definition of parallel tests (equal expected scores, true variance, error variance, inter-item correlations) |
| **Freeman** | 1962 | Six criteria for judging whether two test forms are parallel |
| **Dressel** | 1940 | Modified K-R formula for differentially weighted item scores |
| **Ferguson** | 1951 | Extended K-R formulas to polytomous item scoring |
| **Tucker** | 1949 | Modified K-R20 formula with item-difficulty variance term |
| **Anastasi and Urbina** | 1997 | Standard definition of reliability cited in text (p. 88) |
| **Nunnally and Bernstein** | 1994 | Measurement error theory; recommendation that all items correlate with total score |
| **Novick and Lewis** | 1967 | Clarified that K-R coefficient = mean of all split-half Rulon coefficients |
| **Kaiser and Michael** | 1975 | Contributed to the formulation/interpretation of Coefficient alpha |
| **Rulon** | — | Rulon formula for internal consistency using difference-score variance |
| **Flanagan** | — | Flanagan formula for internal consistency using separate half-variances |

---

## Likely Exam Points

1. **The fundamental CTT equation is x = T + e.** Obtained score = True score + Error score. The core assumptions are: (a) T and e are uncorrelated; (b) errors across different tests are uncorrelated; (c) errors are random.

2. **Reliability coefficient formula:** r_tt = σ²_t / σ²_o. Equivalently, r_tt = 1 - (σ²_e / σ²_o). Reliability is the proportion of total variance that is true variance.

3. **Spearman-Brown formula for split-half:** r_tt = 2r_hh / (1 + r_hh). The whole-test reliability when r_hh (half-test reliability) is known.

4. **Spearman-Brown formula for lengthening a test:** r_nn = n·r_11 / [1 + (n-1)r_11]. To find required lengthening factor: n = r_n(1 - r_11) / [r_11(1 - r_n)].

5. **K-R20 requires item-level p values (item difficulty); K-R21 requires only M and SD.** K-R21 always underestimates K-R20 when item difficulties are unequal. Both are inapplicable to speed tests.

6. **Coefficient alpha (Cronbach's α) is the most general internal consistency method.** Applicable to non-dichotomous items (Likert scales, essay scores). Formula replaces Σpq with Σσ²_i. Acceptable threshold: α ≥ 0.70; preferred: α ≥ 0.80. A negative alpha signals a test construction problem. Alpha is the mean of all possible split-half Rulon coefficients.

7. **Standard error of measurement:** SE_meas = S_t√(1 - r_tt). Unlike r_tt, SE_meas is NOT affected by the range of scores. When r_tt = 1, SE_meas = 0; when r_tt = 0, SE_meas = S_t. Confidence intervals: ±1 SE = 68%, ±2 SE = 95%, ±3 SE = 99%.

8. **Split-half and K-R methods are INAPPROPRIATE for speed tests** because they yield spuriously inflated (artifactually perfect) reliability coefficients. Correct alternatives: test-retest, alternate forms, or split-by-time methods.

9. **Guilford's (1956) benchmarks:** r_tt ≥ 0.90 for individual diagnosis; r_tt as low as 0.65 acceptable for group comparisons.

10. **Index of reliability:** r_xt = √r_xx. This is the maximum correlation a test can have with any criterion (upper bound on validity). Example: r_xx = 0.64 → r_xt = 0.80.

11. **Generalizability Theory (Cronbach et al., 1972):** Identifies both systematic and random error sources using ANOVA. CTT is a special case of G-theory. Key question: "Over what conditions can scores be generalized?"

12. **Reliability of difference scores (r_dd):** The higher the correlation between X and Y (r_xy), the lower the reliability of their difference. Difference scores from highly correlated measures are dominated by measurement error, not true differences.

13. **Bandwidth-Fidelity dilemma (Cronbach and Gleser, 1965; Shannon and Weaver, 1949):** Broader tests (higher bandwidth) have lower reliability (lower fidelity). Narrow tests are more reliable but less comprehensive. A fundamental tension in test construction.

14. **Factors that increase reliability:** Longer test, heterogeneous examinees, homogeneous items, moderate item difficulty (0.40-0.60), high item discrimination, consistent scoring.

15. **Domain sampling model (Feldt and Brennan, 1989):** Reliability = ratio of observed-score variance to universe-score variance. Increasing the number of items brings observed scores closer to universe scores and increases reliability.

---
*Source: Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh), Chapter 5: Reliability (vision-transcribed). Part of [[INDEX]].*
