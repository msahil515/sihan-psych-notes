---
date: 2026-05-28
book: "Tests, Measurements & Research Methods (A.K. Singh)"
subject: Research Methods & Statistics
chapter: 2
title: "Reliability, Validity & Norms"
tags: [research-methods, psychometrics, reliability, validity, norms, standard-scores, cronbach-alpha, MET-2026, clinical-psychology-entrance]
---

# Ch 2: Reliability, Validity & Norms

**Overview:** Core psychometrics from Part One of Singh (Chapters 5-8). Covers classical true-score theory, all reliability methods (with formulas), validity types (content/criterion/construct), convergent and discriminant validation (MTMM matrix), norm-referenced vs criterion-referenced interpretation, standard score systems, and response sets. Every formula is as stated by Singh; every taxonomy follows his exact terminology.

---

## PART A: RELIABILITY (Singh Ch. 5)

### A.1 History and Classical True Score Theory

- **Spearman (1904)**: "The Proof and Measurement of Association between Two Things" -- founder of reliability theory.
- **Thorndike (1904)**: *An Introduction to the Theory of Mental and Social Measurements*.
- **Kuder & Richardson (1937)**: introduced KR-20 and KR-21.
- **Cronbach (1951, 1972)**: coefficient alpha; generalizability theory.

**Classical test theory (CTT)** assumes:

> **X = T + E** (obtained score = true score + error score)

Where:
- **X** = obtained (observed) score
- **T** (or x_t) = **true score** -- the mean of an infinite number of administrations; free from chance errors
- **E** (or x_e) = **error score** -- random or systematic

**Assumptions of CTT:**
- Mean error of measurement = 0
- True scores and errors are uncorrelated (r = 0)
- Errors on different measures are uncorrelated

**Variance partition:**

> **σ²_x = σ²_t + σ²_e**

(Total variance = True variance + Error variance)

**Reliability coefficient (logical definition):**

> **r_tt = σ²_t / σ²_x** = proportion of true variance in total variance

Equivalently: r_tt = 1 - (σ²_e / σ²_x)

> **Key Point:** Reliability is the property of **test scores**, not the test itself. It always refers to a particular type of consistency (over time, over raters, over item samples).

**Error score types:**
- **Random (chance) errors**: inflate or depress score randomly; mean = 0 over many trials
- **Systematic (constant) errors**: always in one direction; mean ≠ 0; do NOT affect reliability but do affect validity

**Domain sampling model**: reliability = ratio of observed-score variance on a shorter test to true-score variance; more items = better representation = higher reliability.

**Generalizability theory (Cronbach et al. 1972)**: identifies both systematic and random inconsistency sources; classical theory is a special case. Question: "Under what conditions can scores be generalized?"

---

### A.2 Methods (Types) of Reliability

Singh lists **four** main methods. Test-retest and parallel-forms are **external consistency** procedures; split-half and KR/alpha are **internal consistency** procedures.

| Method | Also Called | Procedure | Error Source | When to Use |
|--------|-------------|-----------|--------------|-------------|
| **Test-retest** | Temporal stability / Coefficient of stability | Same test, same sample, two occasions (fortnight gap recommended) | Time sampling; maturation; practice/memory effects | Speed tests, power tests, heterogeneous tests |
| **Parallel forms (immediate)** | Alternate/equivalent/comparable forms; Coefficient of equivalence | Two equivalent forms, same day | Content sampling | Speed test construction |
| **Parallel forms (delayed)** | Alternate forms delayed | Two equivalent forms, ~fortnight gap | Time sampling + content sampling + content heterogeneity | Power tests |
| **Split-half** | On-the-spot reliability (Guilford & Fruchter 1973) | Single test split into two halves (odd-even preferred); PM correlation of halves; then Spearman-Brown | Content/item sampling | Power tests only (NOT speed tests) |
| **KR-20 / KR-21** | Kuder-Richardson formulas | Single administration; requires item p and q values | Content sampling | Dichotomous items (0/1); homogeneous tests |
| **Coefficient alpha (Cronbach's alpha)** | Alpha coefficient | Single administration; uses item variances | Content sampling + content heterogeneity | Polytomously scored items; most general |
| **Scorer reliability** | Inter-rater reliability | Two or more independent scorers rate same responses | Inter-scorer differences | Subjective/projective tests |

> **Key Point:** Split-half, KR formulas, and coefficient alpha should **NOT** be used with speed tests -- reliability will be spuriously inflated (perfect odd-even split due to speed alone).

**Criteria for parallel/equivalent forms (Freeman 1962):**
1. Same number of items
2. Uniformity in content, range of difficulty, adequacy of sampling
3. Similar distribution of difficulty indices
4. Item-total correlations equal
5. Equal (or nearly equal) means and SDs
6. Uniform mode of administration and scoring

---

### A.3 Key Formulas

**Spearman-Brown Prophecy Formula (half to whole):**

> r_tt = **2 r_(x1x2) / (1 + r_(x1x2))**

Where r_(x1x2) = PM correlation between two half-scores.

Example: r_half = 0.70 → r_whole = 2(0.70)/1.70 = **0.82**

**Spearman-Brown (lengthening by n times):**

> r_nn = **n r_tt / (1 + (n-1) r_tt)**

Example: r_tt = 0.80, n = 4 → r_nn = 4(0.80)/(1+3×0.80) = 3.20/3.40 = **0.94**

**Spearman-Brown (finding n required for desired r):**

> n = **r_desired (1 - r_tt) / r_tt (1 - r_desired)**

Example: r_tt = 0.60, desired = 0.90 → n = 0.90(0.40)/0.60(0.10) = 0.36/0.06 = **6**

(Doubling test length from r=0.50 gives r=0.67; again doubling gives r=0.80.)

**Rulon Formula:**

> r_tt = **1 - (σ²_d / σ²_t)**

Where σ²_d = variance of difference between two half-scores; σ²_t = variance of total score.

**Flanagan Formula:**

> r_tt = **2[1 - (σ²_1 + σ²_2) / σ²_t]**

Where σ²_1, σ²_2 = variances of the two half-scores; σ²_t = variance of total score.
*(Advantage over Spearman-Brown: no need to compute r of half-tests first.)*

**KR-20:**

> KR_20 = **(n / n-1) × (σ²_t - Σpq) / σ²_t**

Where n = number of items; σ²_t = total score variance; p = proportion correct per item; q = 1-p.

**KR-21:**

> KR_21 = **(n / n-1) × (σ²_t - nPQ) / σ²_t**

Simplified form: **(nσ²_t - M_t(n - M_t)) / σ²_t(n-1)**

Where M_t = mean total score; P = average proportion correct = M_t/n; Q = 1-P.

KR-21 **underestimates** KR-20 when item difficulty values vary widely. KR-20 is the basic formula; KR-21 is its simplification (assumes all items same difficulty).

**Requirements for KR formulas:**
1. All items homogeneous (unifactor test)
2. Items scored 0 or 1 (dichotomous)
3. For KR-21: all items equal difficulty; for KR-20: values of p/q per item needed

**Coefficient Alpha (Cronbach, 1951):**

> α = **(n / n-1) × (σ²_t - Σσ²_i) / σ²_t**

Where Σσ²_i = sum of variances of individual item scores.

- Differs from KR-20 in that Σpq is replaced by Σσ²_i (sum of item variances)
- Applicable when items have **multiple score values** (not just 0/1)
- Most general internal consistency method
- Alpha = average of all possible split-half coefficients (Cronbach 1951)
- Range: 0 (zero internal consistency) to 1 (perfect)
- Negative alpha = items negatively correlated or inappropriate model
- Acceptable: ≥ 0.60; preferred: closer to 0.90
- Error sources: content sampling + **content heterogeneity**

**Hoyt's ANOVA Formula:**

> r_tt = **1 - (V_e / V_p)**

Where V_e = error variance; V_p = variance among examinees. Yields same result as KR-20.

> **Key Point:** KR is mathematically the mean of all split-half coefficients (Cronbach 1951) -- strictly true when halves are estimated by Rulon formula (not by Spearman-Brown).

---

### A.4 Satisfactory Size of Reliability Coefficient

| Purpose | Acceptable r_tt |
|---------|----------------|
| Individual diagnosis (intelligence, aptitude, achievement tests) | **0.90 or higher** |
| Comparing group means (narrow range) | 0.50-0.60 sufficient |
| Preliminary (not final) decisions | Lower levels acceptable |
| Gross individual differences | Lower levels acceptable |

**Bandwidth-Fidelity Dilemma (Cronbach & Gleser 1965; Shannon & Weaver 1949):**
- **Bandwidth** = breadth of information in the test
- **Fidelity** = accuracy of measurement
- Broader bandwidth → lower fidelity (lower reliability)
- Narrower bandwidth → higher fidelity (higher reliability)
- Conflict is inherent: measuring a specific trait with high accuracy vs. measuring a broad trait less accurately

---

### A.5 Standard Error of Measurement (SEM)

**Definition:** Standard deviation of error scores (or of a sample of obtained scores around the true score). Not influenced by range of scores (unlike the reliability coefficient).

**Formula:**

> **SE_meas = σ √(1 - r_tt)**

Where σ = SD of test scores; r_tt = reliability coefficient.

**Interpretation:**
- If r_tt = 0.90, σ = 10: SE_meas = 10√(1-0.81) = 10√0.19 ≈ **4.35**
- Obtained score 60: 95% interval = 60 ± 1.96(4.35) = [51.47, 68.53]
- Obtained score 60: 99% interval = 60 ± 2.58(4.35) = [48.78, 71.22]
- If r_tt = 1.00: SE_meas = 0 (perfect reliability, no error)
- **Smaller SE_meas = more reliable test**

**True score estimation (regression equation):**

> X_t_hat = r_tt × X_o + (1 - r_tt) × M_t

Where X_t_hat = estimated true score; X_o = obtained score; M_t = mean.

Standard error of estimated true score:

> SE_t = σ √(r_tt - r²_tt)

---

### A.6 Reliability of Speed Tests

- Single-trial methods (odd-even, KR formulas) are **inapplicable** to speed tests -- produce spuriously inflated coefficients (pure speed → perfect odd-even correlation)
- **Appropriate methods:**
  - Test-retest
  - Equivalent-form reliability
  - Split by **time** (not items): separately timed halves; apply Spearman-Brown
  - Quarter method: combine 1st+4th quarter vs 2nd+3rd quarter scores

---

### A.7 Factors Influencing Reliability

**Extrinsic Factors (outside the test):**

| Factor | Effect on Reliability |
|--------|----------------------|
| **Group variability/heterogeneity** | Heterogeneous group → higher r_tt; homogeneous group → lower r_tt (if SD=0, r=0) |
| **Guessing** | Raises total score; increases error variance → lowers reliability |
| **Environmental conditions** | Non-uniform conditions → lower r_tt |
| **Momentary fluctuations** | Anxiety, distraction, health → error variance → lower r_tt |

**Intrinsic Factors (within the test):**

| Factor | Effect on Reliability |
|--------|----------------------|
| **Length of test** | Longer test → higher r_tt (Spearman-Brown principle) |
| **Range of total scores** | Wider range (high SD) → higher r_tt |
| **Item homogeneity** | All items measuring same trait → higher inter-item r → higher r_tt |
| **Item difficulty** | Items near p = 0.5 (range 0.40-0.60) → highest reliability; extreme p → low r_tt |
| **Item discrimination** | High discriminating items → high item-total r → higher r_tt |
| **Scorer reliability** | Poor inter-rater agreement → lower r_tt |

---

### A.8 How to Improve Reliability

1. Use **heterogeneous** group of examinees
2. Use **homogeneous items** (unifactor test)
3. Make the test **longer**
4. Use items with **moderate difficulty** (p = 0.40-0.60)
5. Use **discriminating items**

**Three main approaches:**
- **Lengthen the test**: use Spearman-Brown (Eq. 5.17/5.18)
- **Discard low-reliability items**: factor analysis (unidimensional) or item analysis (discriminability analysis -- remove items with low item-total r)
- **Correction for attenuation** (see Validity section)

---

### A.9 Index of Reliability

**Definition:** Correlation between obtained scores and true scores. Indicates the maximum correlation the test can yield.

> **r_ot = √r_tt**

Example: r_tt = 0.65 → index of reliability = √0.65 = **0.81**

This is the **maximum** validity coefficient the test can attain in its present form.

---

### A.10 Reliability of Difference Scores and Composite Scores

**Reliability of difference score (X minus Y):**

> r_DD = **(r_xx + r_yy)/2 - r_xy) / (1 - r_xy)**

Key insight: higher correlation between X and Y → **lower** reliability of difference score (true scores overlap; difference = mostly error).

**Reliability of composite score:**

> r_composite = **k r_ii / (1 + (k-1) r_ij)**

Where k = number of tests; r_ii = average test reliability; r_ij = average inter-test correlation. Composite scores are typically **more** reliable than individual components.

---

## PART B: VALIDITY (Singh Ch. 6)

### B.1 Meaning of Validity

**Validity** = the degree to which a test measures what it claims to measure. It is the correlation with some **outside independent criterion**, not the self-correlation of the test.

- **Lindquist (1951)**: "accuracy with which it measures what it is intended to measure"
- **Kaplan & Saccuzzo (2001)**: "agreement between a test score and the quantity it is believed to measure"
- **Standards (AERA, APA & NCME 1999)**: "A test is valid to the extent that inferences made from it are appropriate, meaningful, and useful"
- **Cronbach (1989)**: "All validation is one and in a sense, all is construct validation"

> **Key Point:** Validity is the property of **score-based inferences**, not the test itself. The 1999 Standards no longer recognizes separate categories of validity -- only different categories of **evidence** for validity.

**Validity is never higher than the index of reliability.** A test must be reliable to be valid, but high reliability does not guarantee high validity.

---

### B.2 Aspects (Types) of Validity

Three purposes of testing → three main types of validity (APA 1966 Standards monograph):

| Type | Also Called | What It Measures | Method | Applicable Tests |
|------|-------------|-----------------|--------|-----------------|
| **Content validity** | Intrinsic/curricular/representativeness validity | Adequacy of item sampling from content domain | Expert judgement; statistical internal consistency | Achievement/proficiency tests |
| **Criterion-related: Predictive** | Empirical/statistical validity | Correlation with future criterion | PM r between test scores and future criterion scores | Aptitude, selection, vocational tests |
| **Criterion-related: Concurrent** | Concurrent empirical validity | Correlation with present criterion | PM r between test and current criterion/established test | Diagnostic tests |
| **Construct validity** | Factorial/trait validity | Measurement of a hypothetical construct | Programme of research (correlations, factor analysis, group differences, experimental manipulation) | Personality, intelligence tests; when no criterion/content universe is adequate |
| **Face validity** | (not a technical type) | Appearance of validity to examinees | Subjective inspection | All tests (for rapport/cooperation) |

> **Key Point:** Face validity is **not** a technical form of validity. It is a matter of **social acceptability**, not objective measurement. Do not confuse with content validity.

**Content validity requires two sub-types:**
- **Item validity**: each item represents the intended content area
- **Sampling validity**: test adequately samples the total content area

**Content validity threats (Standards 1999):**
- **Construct under-representation**: fails to include important construct components
- **Construct-irrelevant variance**: scores influenced by factors irrelevant to construct (e.g., test anxiety)

---

### B.3 Criterion-Related Validity

**Criterion** = external, independent measure of the same variable.

**Qualities of a good criterion (four):**

| Quality | Description |
|---------|-------------|
| **Relevance** | Closely corresponds to the ultimate behaviours of interest |
| **Freedom from bias** | Equal opportunity to score high/low regardless of group membership |
| **Reliability** | Criterion scores must be stable/reproducible |
| **Availability** | Practically accessible; not too costly or time-consuming |

**Predictive vs Concurrent:**
- Predictive validity is typically **lower** than concurrent validity (association between test and criterion decreases over time)
- Concurrent: discrimination method -- does the test discriminate between those with vs without a characteristic?

**Correction for attenuation (full -- both test and criterion):**

> r_xy_corrected = **r_xy / √(r_xx × r_yy)**

Where r_xy = obtained validity coefficient; r_xx = reliability of test; r_yy = reliability of criterion.

**One-way correction (criterion only -- more common):**

> r_xy_corrected = **r_xy / √r_yy**

> **Key Point:** Correction for attenuation **increases** the validity coefficient. The denominator sets the upper limit of correlation between test and criterion.

---

### B.4 Construct Validity

**Cronbach & Meehl (1955)**: construct validity is used "when no criterion or universe of content is accepted as entirely adequate to define the quality to be measured."

**A construct** = nonobservable trait (e.g., intelligence, anxiety, neuroticism) that explains behaviour. Nunnally (1970): indicates "a variety of behaviours will correlate with each other in studies of individual differences."

**Three steps in construct validation:**
1. Specify possible measures of the construct (define it; list referents)
2. Determine correlations among all measures empirically
3. Determine whether measures behave as expected relative to other variables

**Evidence for construct validity (Gregory 2005):**
- Test is **homogeneous** (measures a single construct)
- Correlates more with related tests than with unrelated tests
- Shows expected **developmental changes** over time/age
- **Group differences** are theory-consistent
- **Intervention effects** produce theory-consistent score changes
- **Factor analysis** produces theory-consistent structure

> **Key Point:** Construct-related evidence subsumes all other validity evidence. Today many psychologists consider construct validity as the only fundamental form of validity.

---

### B.5 Convergent and Discriminant Validation (MTMM)

**Campbell & Fiske (1959)**: proposed the **Multitrait-Multimethod Matrix (MTMM)** to study both convergent and discriminant validity simultaneously.

- **Convergent validity**: test correlates highly with other measures of the **same construct** (measures "go together")
- **Discriminant validity**: test correlates **poorly** with measures of **different constructs** (confirms what the test does NOT measure)

**MTMM design**: ≥2 traits measured by ≥2 methods. Matrix contains:
- **Reliability diagonals** (monotrait-monomethod): values in parentheses; should be highest
- **Validity diagonals** (monotrait-heteromethod): bold/italics; should be high and significant
- **Heterotrait-monomethod triangles**: solid-line triangles; correlations between different traits by same method
- **Heterotrait-heteromethod triangles**: broken-line triangles; correlations between different traits by different methods

**Four criteria for satisfactory construct validity from MTMM:**

| Criterion | Requirement | Evidence For |
|-----------|-------------|-------------|
| 1 | Validity diagonal values are **large and significant** | Convergent validity |
| 2 | Validity diagonal values > heterotrait-heteromethod triangles | Discriminant validity |
| 3 | Validity diagonal values > heterotrait-monomethod triangles (if opposite, method bias present) | Discriminant validity |
| 4 | Both heterotrait triangles show same pattern of trait intercorrelations | Discriminant validity |

> **Key Point:** Requirements 1, 2, and 3 must be met at minimum for satisfactory construct validity.

---

### B.6 Factors Influencing Validity

| Factor | Effect |
|--------|--------|
| **Length of test** (homogeneous lengthening) | Increases both reliability and validity |
| **Range of ability** (sample heterogeneity) | Restricted range → lower validity coefficient |
| **Ambiguous directions** | Differential interpretation + guessing → lower validity |
| **Socio-cultural differences** | Test developed in one culture may not be valid in another |
| **Addition of inappropriate items** | Lowers both reliability and validity |
| **Unreliability of criterion** | Attenuates validity coefficient (apply correction for attenuation) |

**Formula for validity after lengthening n times:**

> r_c(n) = **n r_cx / √(n + n(n-1) r_tt)**

**Maximum validity when lengthened indefinitely:**

> r_max = **r_cx / √r_tt** = validity coefficient / index of reliability

---

### B.7 Cross-Validation

**Cross-validation** = revalidating a completed test on a **new sample** from the same population (different from standardization sample).

**Why necessary?** Validity on original sample is **spuriously high** because:
- Items selected to maximize group differences capitalize on chance factors
- Random sampling errors of the original sample inflate the coefficient

**Validity shrinkage** = phenomenon where validity predicts criterion less accurately in new sample than in original sample.

**Shrinkage is greater when:**
- Initial item pool is large and proportion retained is small
- Sample sizes are small
- Items assembled without previously formulated rationale

**Classic demonstration (Kurtz 1948, Rorschach)**: r = 1.00 on original sample → r = .02 on new sample of 41 managers.

**Messick's expanded theory of validity:** validity must go beyond score meaning to include:
- Relevance and utility of test scores
- Value implications of score interpretation
- Consequences of test use (actual and potential)

---

### B.8 Relation of Validity to Reliability

**Key relationships:**
- Validity = correlation with outside criterion; Reliability = self-correlation
- A test that does not correlate with itself cannot correlate with outside criteria
- **Reliability is a necessary but not sufficient condition for validity** (for homogeneous tests)
- For **heterogeneous tests**: validity may be high even with low internal consistency (each part measures independent function)

**Maximum validity:**

> **r_max = √(r_11 × r_22)**

Where r_11 = reliability of test; r_22 = reliability of criterion.

Example: r_11 = 0.80, r_22 = 1.00 → r_max = √0.80 = **0.89**

> **Key Point:** Validity cannot exceed the **index of reliability** (√r_tt). Reliability is a ceiling on validity.

**Tucker (1946) compromise:** inter-item correlations ranging from **0.10 to 0.60** allow satisfactory levels of both reliability and validity. High reliability requires equal difficulty + high inter-item r; high validity requires different difficulty + lower inter-item r -- these goals are in tension (working at cross purposes).

---

## PART C: NORMS AND TEST SCALES (Singh Ch. 7)

### C.1 Norm-Referenced vs Criterion-Referenced Tests

| Feature | **Norm-Referenced Test (NRT)** | **Criterion-Referenced Test (CRT)** |
|---------|-------------------------------|-------------------------------------|
| Purpose | Compare examinee to a norm group | Compare examinee to a predetermined standard/criterion |
| Items | Broad domain; vary widely in difficulty for maximal discrimination | Narrow, real-world domain; similar difficulty level |
| Score expression | Standard scores, percentiles, grade equivalents | Percentage; predetermined pass level |
| Reference | Other examinees | Predetermined cut-off |
| Focus | Relative position | Mastery of specific competencies |
| Possible result | Must have spread (some fail) | All can pass if all meet standard |

**Norms** = average performance on a test by a standardization sample; interpretive framework for converting raw scores to meaningful derived scores.

---

### C.2 Steps in Developing Norms (Singh's three steps)

1. **Define the target population** (normative group): determined by intended use of the test
2. **Select a representative sample** from the target population: cross-sectional representation of all subgroups; cluster sampling generally used (random sampling impractical); larger sample preferred
3. **Standardize conditions** for test administration: sound, lighting, timing, test security, adherence to manual

---

### C.3 Types of Norms and Test Scales

**Four types of derived scores (Lyman 1963):** age scores, grade scores, percentile scores, standard scores. Each corresponds to a type of norm.

#### Age-Equivalent Norms (Age Norms)
- Average performance of a representative sample of a given **age level** on a trait
- Most suitable for traits that **increase systematically with age** (physical traits; cognitive abilities in childhood/adolescence)

**Limitations:**
1. Units are **not equal** throughout growth (growth at age 3-4 ≠ growth at 14-15; decelerates after 16-17)
2. Growth rates of different traits **not comparable** (maze learning stops at adolescence; vocabulary grows lifelong)
3. Traits with no progressive age change (e.g., visual acuity; many personality traits) cannot use age norms

#### Grade-Equivalent Norms (Grade Norms)
- Average performance of a representative sample of a given **grade or class**
- Used for achievement tests, educational tests, intelligence tests

**Limitations:**
1. Grade equivalents in different subjects **not comparable** (social studies vs. arithmetic)
2. Assumes similar curriculum experiences across grade -- may not hold for higher grades
3. Not suited when growth is rapid in early grades but plateaus later (spelling, arithmetic)

#### Percentile Norms (Percentile-Rank Norms)

**Key terms:**
- **Percentile rank (PR)**: percentage of cases in a distribution at or **below** a given score
- **Percentile**: the score corresponding to a given percentile rank (a score, not a percentage)
- **Centile**: equivalent to percentile (C_30 = 30th percentile)
- **Decile**: divides distribution into 10 parts (D_7 = 70th centile)
- **Quartile**: divides into 4 parts; Q_1 = 25th centile, Q_2 = 50th centile, Q_3 = 75th centile

> Do NOT confuse **percentile** (a derived score expressed as percentage of persons) with **percentage score** (a raw score expressed as percentage of items correctly answered).

**Most popular and common type of norm** in psychological and educational tests.

**Advantages:** Easy to construct; easy to understand; usable by untrained persons.

**Limitations:**
1. Laymen confuse percentile with percentage score
2. **Inequality of units**: same raw-score difference produces large PR change near median but small change at extremes (nonlinear transformation); units are **systematically unequal**
3. Indicates only relative position; conveys nothing about the amount of actual difference

#### Standard Score Norms

**Standard scores** = derived scores with fixed mean and SD. Units are **equal** throughout the scale (solves percentile inequality problem).

**Two transformation types:**
- **Linear transformation**: retains all properties of original distribution (shape unchanged)
- **Normalized transformation**: adjusts to produce normal distribution regardless of original shape

| Score Type | Mean | SD | Distribution | Formula/Notes |
|-----------|------|----|-------------|--------------|
| **z-score** (sigma score) | 0 | 1 | Same as original (linear) | z = (X - M) / σ |
| **T-score** | 50 | 10 | Normal (normalized) | T = 10z + 50; range typically 20-80; devised by McCall (1922), named after Thorndike |
| **Stanine** | 5 | ~2 | Normal (normalized) | 9-point scale (1-9); developed by US Air Force in WWII; contraction of "Standard nine" |
| **Sten** | 5.5 | 2 | Normal | 10-point scale proposed by Canfield (1951); variant of stanine |
| **Deviation IQ** | 100 | 15 or 16 | Normal (normalized) | NOT ratio IQ; first used by Wechsler (mean=100, SD=15) |

**z-score formula:**

> **z = (X - M) / σ**

Example: X = 60, M = 30, σ = 15 → z = (60-30)/15 = **+2.0**

**T-score formula:**

> **T = 10z + 50**

**Standard score (general linear transformation):**

> **New SS = z(new SD) + new mean**

**Stanine distribution** (percentages per stanine):

| Stanine | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---------|---|---|---|---|---|---|---|---|---|
| % of cases | 4 | 7 | 12 | 17 | 20 | 17 | 12 | 7 | 4 |

**Deviation IQ:**
- SD varies: 12-18, but 15 or 16 is standard
- Not the same as ratio IQ (MA/CA × 100)
- Example (SD=16): deviation IQ of 132 = 2 SD above mean; deviation IQ of 84 = -1 SD

**Normalized vs linear standard scores:** Use normalized when original distribution is skewed and comparison across distributions is needed.

#### Local and Subgroup Norms
- **Local norms**: from local rather than national sample (e.g., Hindi-speaking people of Bihar only)
- **Subgroup norms**: scores from an identified subgroup (by sex, ethnic background, geographic region, SES, etc.)

---

### C.4 Criteria of Good Test Norms

| Criterion | Description |
|-----------|-------------|
| **Representative** | True representative of the group with which comparison is desired; must include all subgroups (sex, rural/urban, SES, caste, school size, etc.) |
| **Relevant** | Meaningful for the concerned group; national vs local norms chosen based on purpose |
| **Up to date** | Must reflect current population performance; old norms produce inflated percentile ranks |
| **Comparable** | Norms of different tests based on same population for direct score comparisons (e.g., profile comparisons of aptitude and achievement) |
| **Adequately described** | Provide information about: (i) sampling method, (ii) number/distribution of cases, (iii) characteristics of norm group (age, sex, SES, geography, education, caste), (iv) standardization conditions |

---

## PART D: RESPONSE SETS (Singh Ch. 8)

### D.1 Meaning

**Response bias**: when a response to a test item is altered in a way that indicates something other than what the test intends to measure (Guilford 1954).

**Response set**: a kind of response bias occurring from the examinee **assuming certain mental sets** (Cronbach 1946): "the tendency causing a person to give different responses to items than he would when the same content is presented in a different form."

> **Cronbach (1950):** "Response sets are the enemy of validity."

Response sets are common in ability tests, personality tests, interest inventories, and attitude scales.

**Response styles**: response sets considered as durable, consistent personality traits worth measuring in their own right (Wiggins 1962; Jackson & Messick 1962). Distinction from response sets is not accepted by all.

---

### D.2 Types of Response Sets

| Response Set | Description | Common In |
|-------------|-------------|-----------|
| **Deviation set** (Berg 1961) | Tendency to give very unusual/uncommon responses | Nonverbal tests (Rorschach, TAT) |
| **Acquiescence set** | Tendency to systematically mark only "Yes/True/Agree" (yes-saying) or "No/False/Disagree" (no-saying) | Personality inventories, interest inventories |
| **Social desirability (faking-good)** | Tendency to give answers creating a favourable self-impression; Edwards (1957): a "facade effect" / "put oneself in good front"; related to need for social approval (Crowne & Marlowe 1964) | Personality tests, service selection tests |
| **Faking-bad (social undesirability)** | Tendency to give unfavourable/maladjusted-appearing responses; related to need for sympathy/attention | Clinical settings (psychotherapy admission, malingering) |
| **Semantics (semantic confusion)** | Confusion in interpreting vague frequency words ("often," "seldom," "sometimes") | Likert/rating-scale items |
| **Evasiveness** | Tendency to mark "?", "Uncertain," "Indifferent" rather than fixed alternatives | Tests with three-option (Y/N/?) format |
| **Tendency to work speedily** | Response for speed over accuracy; ignoring true content | Long temperament tests (300+ items); ego-oriented examinees |
| **Tendency to guess when uncertain** | Guessing on difficult or multiple-choice items | Ability and special ability tests |
| **Cautiousness** | Tendency to leave difficult items unanswered (opposite of guessing) | Ability tests |
| **Extremeness** | Tendency to mark only extreme points on rating scales | Rating scales |

> **Key Point:** Social desirability research (Edwards 1957): faking-good is mostly **unconscious** -- examinees are unaware they are doing it.

---

### D.3 Implications of Response Sets

1. Reduce the **range of individual differences** in test scores
2. Contribute to **error (irrelevant) variance** -- dilute test with factors not part of the content; **reduce validity**
3. More obvious when items are **difficult, ambiguous, or unstructured**
4. Response sets are **consistent** across administrations and tests -- raise reliability (via true variance), but this contribution is small compared to error variance contribution
5. When consistent, response sets become **response styles** (treated as durable personality traits)

---

### D.4 Methods to Eliminate/Control Response Sets

| Method | Targets | Details |
|--------|---------|---------|
| **Design of test items** | Acquiescence, evasiveness | Use 5-, 7-, or 10-point scales instead of Yes-No/?; increases reliability and validity; use forced-choice items for social desirability (EPPS: 2-term forced choice; Gordon Personal Inventory: multi-term) |
| **Forced-choice items** | Social desirability / faking-good | Examinees choose between equally attractive/unattractive options; EPPS and GPI examples; not fully effective per subsequent research |
| **Independent SD scale** (Meehl & Hathaway 1946) | Social desirability | Correlate items with SD scale (e.g., MMPI K scale); drop/reformulate high-r items; MMPI-2 uses: ? (Question), L (Lie), F (Validity), K (Correction) scales + Fb, VRIN, TRIN |
| **Neutral items** (Wiener 1948; Hanley 1956; Edwards 1957) | Social desirability | Use items with SD scale values 4-6 (neutral on Edwards' 9-point scale: 1=extremely undesirable to 9=extremely desirable) |
| **Adapting test difficulty** | General response sets | Match item difficulty to examinee ability level |
| **Modifying directions** | Acquiescence, guessing, evasiveness | Explicitly state ~50% items are false (controls acquiescence); warn of negative marking (controls guessing); discourage marking "?" (controls evasiveness) |
| **Good/appropriate scoring formulas** | General | Weighted scoring; factor-analyze to optimally weight correct, incorrect, and unattempted responses (Guilford 1954) |
| **Easy multiple-choice items** | Guessing | 2-alternative items: 50% guess probability; multi-choice items reduce guessing; randomize position of correct answers (Mosier & Price 1945) |

**MMPI validity scales:**
- **? score**: number of unanswered/double-answered items (evasiveness)
- **L (Lie) score**: naive attempts to appear virtuous
- **F (Validity) score**: infrequent responses (faking-bad, confusion, carelessness)
- **K (Correction) score**: suppressor variable; high K = faking-good; low K = self-criticism; added to subscale raw scores
- **MMPI-2 additional scales**: Fb (Back F), VRIN (Variable Response Inconsistency), TRIN (True Response Inconsistency)

---

## Key Terms

| Term | Definition |
|------|-----------|
| **True score (T)** | Mean of infinite administrations; score free from error; theoretical construct |
| **Error score (E)** | Difference between obtained and true score; X - T = E |
| **Reliability** | Proportion of true variance in total variance; self-correlation of test; consistency of scores |
| **Coefficient of stability** | r_tt from test-retest method; indicates temporal stability |
| **Coefficient of equivalence** | r from parallel-forms method |
| **Coefficient of internal consistency** | r from split-half, KR, or alpha methods; alpha coefficient |
| **Spearman-Brown prophecy formula** | Estimates whole-test r from half-test r; also for lengthening |
| **KR-20** | Basic internal consistency formula; requires item p and q; for 0/1 scored items |
| **KR-21** | Simplified KR-20; assumes all items equal difficulty; uses mean and SD only |
| **Coefficient alpha** | Most general internal consistency method; for polytomous items; mean of all split-half r's |
| **SE_meas** | σ√(1-r_tt); SD of error distribution; direct index of score accuracy; not affected by score range |
| **Index of reliability** | √r_tt; maximum validity the test can achieve; correlation between obtained and true scores |
| **Bandwidth-fidelity dilemma** | Conflict between measuring broadly (bandwidth) and measuring accurately (fidelity) |
| **Validity** | Degree to which test measures what it claims; correlation with outside criterion |
| **Content validity** | Adequacy of item sampling from content domain; non-statistical; for achievement tests |
| **Face validity** | Appearance of validity to examinees; not a technical form; social acceptability |
| **Criterion-related validity** | Correlation of test with external criterion (present or future) |
| **Predictive validity** | Criterion obtained in future; empirical/statistical validity |
| **Concurrent validity** | Criterion available at present; diagnostic use |
| **Construct validity** | Measurement of a theoretical construct; factorial/trait validity |
| **Convergent validity** | Test correlates with measures of the same construct |
| **Discriminant validity** | Test has low correlation with unrelated construct measures |
| **MTMM** | Multitrait-Multimethod Matrix (Campbell & Fiske 1959); evaluates convergent and discriminant validity |
| **Correction for attenuation** | Corrects validity coefficient for unreliability in test and/or criterion |
| **Cross-validation** | Revalidating test on a new sample; corrects for spuriously high validity |
| **Validity shrinkage** | Reduction in validity coefficient when applied to new sample |
| **Norm-referenced test** | Compares examinee to norm group |
| **Criterion-referenced test** | Compares examinee to predetermined performance standard |
| **Norms** | Average performance on a test by a standardization sample |
| **Age norms** | Average performance of a given age level |
| **Grade norms** | Average performance of a given grade/class level |
| **Percentile rank (PR)** | % of cases at or below a given score |
| **Percentile** | Score corresponding to a given PR (a score value, not a %) |
| **z-score** | (X-M)/σ; linear standard score; mean=0, SD=1 |
| **T-score** | 10z+50; normalized standard score; mean=50, SD=10; devised by McCall (1922) |
| **Stanine** | Standard nine; 9-point normalized scale; mean=5, SD≈2; WWII Air Force |
| **Sten** | Standard ten; 10-point scale; Canfield (1951) |
| **Deviation IQ** | Normalized standard score; mean=100, SD=15 or 16; NOT ratio IQ |
| **Response bias** | Alteration of response in a way reflecting something other than what the test measures |
| **Response set** | Response bias from assuming certain mental sets (Cronbach 1946) |
| **Response style** | Consistent response set treated as a durable personality trait |
| **Acquiescence set** | Systematic yes-saying or no-saying |
| **Social desirability (faking-good)** | Tendency to create a favourable self-impression |
| **Deviation set** | Tendency to give unusual/uncommon responses (Berg 1961) |
| **Evasiveness** | Tendency to mark "?/uncertain/indifferent" |

---

## Likely Exam Points

1. **Classical true score equation**: X = T + E; variance partition: σ²_x = σ²_t + σ²_e; reliability = σ²_t/σ²_x. Random errors: mean = 0; uncorrelated with T. Systematic errors affect validity, not reliability.

2. **Four types of reliability** per Singh: test-retest, internal consistency (split-half, KR, alpha), parallel forms, scorer reliability. Test-retest and parallel forms are **external consistency** methods.

3. **Spearman-Brown formula**: 2r/(1+r) for half-to-whole; nrtt/(1+(n-1)rtt) for lengthening; Doubling r=0.50 → r=0.67; doubling again → r=0.80 (know these benchmarks).

4. **KR-20 vs KR-21 vs alpha**: KR-20 requires item p and q; KR-21 assumes equal difficulty (underestimates KR-20 when difficulty varies); alpha for polytomous items; all are mean of all possible split-half coefficients.

5. **Speed tests**: split-half and KR formulas are **inappropriate** (spuriously inflated). Use test-retest, alternate forms, or time-based split.

6. **SEM formula**: SE_meas = σ√(1-r_tt). Smaller SEM = more reliable. Unaffected by score range. r_tt = 1.00 → SEM = 0.

7. **Satisfactory reliability**: ≥0.90 for individual diagnosis; 0.50-0.60 for group comparison. Bandwidth-Fidelity dilemma (Cronbach & Gleser 1965).

8. **Index of reliability** = √r_tt = maximum correlation test can yield = maximum validity. Validity ≤ index of reliability ≤ 1.0.

9. **Three types of validity**: content (non-statistical, achievement tests; expert judgment), criterion-related (predictive: future criterion; concurrent: present criterion), construct (hypothetical traits; when no criterion/content universe adequate).

10. **Face validity** is NOT a technical form of validity. It is social acceptability, not objective measurement.

11. **Four qualities of a good criterion**: relevance, freedom from bias, reliability, availability.

12. **Correction for attenuation**: r_corrected = r_xy/√(r_xx × r_yy) (full); r_xy/√r_yy (one-way/criterion only). Increases the validity coefficient.

13. **MTMM (Campbell & Fiske 1959)**: convergent = same trait, different methods correlate; discriminant = different traits, same method do NOT correlate highly. Validity diagonal > heterotrait triangles.

14. **Validity-reliability relation**: validity cannot exceed index of reliability (√r_tt); reliability is necessary but not sufficient for validity; heterogeneous tests can have high validity with low internal consistency reliability.

15. **Cross-validation**: validity on standardization sample is spuriously high; apply to new sample; Kurtz (1948) Rorschach -- r dropped from 1.00 to .02.

16. **Maximum validity formula**: r_max = r_xy/√r_tt; also r_max = √(r_11 × r_22).

17. **Norm-referenced vs criterion-referenced**: NRT = compare to norm group; CRT = compare to predetermined standard; CRT items same difficulty vs NRT items vary in difficulty.

18. **Three steps in developing norms** (Singh): (1) define target population, (2) select representative sample, (3) standardize conditions.

19. **Standard score conversions**: z = (X-M)/σ; T = 10z+50; Stanine: 9 points (4-7-12-17-20-17-12-7-4%); Deviation IQ = mean 100, SD 15.

20. **Stanine history**: developed by US Air Force in WWII; "standard nine"; mean=5, SD≈2; 9-point scale (1-9).

21. **Percentile limitation**: unequal units (nonlinear transformation); large raw-score change at median = large PR change; large raw-score change at extremes = small PR change.

22. **Five criteria of good norms** (Singh): representative, relevant, up to date, comparable, adequately described.

23. **Response sets**: Cronbach (1950) called them "enemy of validity." Acquiescence (yes/no-saying), social desirability (faking-good, usually unconscious per Edwards 1957), faking-bad, deviation set (Berg 1961), evasiveness, cautiousness, extremeness.

24. **Control methods for response sets**: forced-choice items (EPPS), SD scale (MMPI K scale), neutral items (Edwards 9-point scale 4-6), modify directions, multiple-choice items, appropriate scoring formulas.

25. **Implications of response sets**: reduce individual differences range; add error variance; reduce validity; consistent across administrations (can raise reliability slightly); if treated as personality traits = response styles.

---

*Source: A.K. Singh, Tests, Measurements and Research Methods in Behavioural Sciences, Part One: Principles of Test Construction -- Ch. 5 Reliability (pp. 79-103), Ch. 6 Validity (pp. 104-124), Ch. 7 Norms and Test Scales (pp. 125-139), Ch. 8 Response Set in Test Scores (pp. 140-146). Part of [[INDEX]].*
