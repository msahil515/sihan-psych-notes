---
date: 2026-05-28
book: "Tests, Measurements & Research Methods (A.K. Singh)"
subject: Research Methods & Statistics
chapter: 5
title: "Statistics for Behavioural Sciences"
tags: [research-methods, statistics, correlation, t-test, ANOVA, chi-square, hypothesis-testing, non-parametric, MET-2026, clinical-psychology-entrance]
---

# Ch 5: Statistics for Behavioural Sciences

**Overview:** Statistics is the science of collecting, organising, summarising, and interpreting numerical data. In behavioural sciences, statistics serves two functions: **descriptive statistics** (summarise and describe data) and **inferential statistics** (draw conclusions about populations from samples). This chapter covers the full canonical treatment tested at NIMHANS and MET entrances, aligned with Coolican's *Research Methods and Statistics in Psychology*.

---

## PART ONE: DESCRIPTIVE STATISTICS

## 5.1 Frequency Distributions

- A **frequency distribution** organises raw scores into a table showing each score (or class interval) and its frequency of occurrence.
- **Relative frequency**: proportion of cases in each class (f / N).
- **Cumulative frequency**: running total of frequencies from lowest to highest.
- **Histogram**: bar graph of a frequency distribution (bars touch; area proportional to frequency).
- **Frequency polygon**: line graph connecting midpoint tops of histogram bars.
- **Ogive**: S-shaped curve of cumulative frequency; used to read off percentile ranks.
- **Class interval width** (i): N < 100 → i = 5; N > 100 → i = 10 (rule of thumb, 10-20 intervals).

> **Key Point:** Always check whether a distribution is **grouped** (class intervals) or **ungrouped** (individual scores) before computing statistics.

---

## 5.2 Measures of Central Tendency

| Measure | Formula / Computation | Level of Measurement | When to Use |
|---------|----------------------|----------------------|-------------|
| **Mode (Mo)** | Most frequently occurring score | Nominal | Categorical data; bimodal distributions |
| **Median (Mdn)** | Middle score when ranked; Mdn = L + [(N/2 − cf) / f] × i | Ordinal | Skewed distributions; ordinal data; outliers present |
| **Mean (M or X̄)** | X̄ = ΣX / N | Interval / Ratio | Normal (symmetric) distributions; further statistical computation |

- **Unimodal, symmetric distribution**: Mean = Median = Mode.
- **Positively skewed** (tail right): Mode < Median < Mean (mean is pulled toward the tail).
- **Negatively skewed** (tail left): Mean < Median < Mode.
- **Relationship (Pearson's empirical rule)**: Mode ≈ Mean − 3(Mean − Median).
- **Weighted mean**: X̄w = Σ(w × X) / Σw; used when subgroups have different sizes.

> **Key Point:** The **mean** is the most stable (least sampling error) but most affected by extreme scores. The **median** is the best measure of central tendency for skewed distributions (e.g., income, reaction time).

---

## 5.3 Measures of Dispersion

| Measure | Formula | Properties |
|---------|---------|------------|
| **Range (R)** | X_max − X_min | Simplest; unstable; uses only two scores |
| **Quartile Deviation (Q)** | Q = (Q3 − Q1) / 2 | Semi-interquartile range; resistant to outliers; used with Median |
| **Mean Deviation (MD)** | MD = Σ\|X − X̄\| / N | Uses all scores; absolute values; rarely used now |
| **Variance (σ² or s²)** | Population: σ² = Σ(X − μ)² / N; Sample: s² = Σ(X − X̄)² / (N − 1) | Foundation for inferential statistics |
| **Standard Deviation (σ or s)** | σ = √[Σ(X − μ)² / N]; s = √[Σ(X − X̄)² / (N − 1)] | Most used; same units as original data |

- **Why N − 1 for sample variance?** Using N−1 makes s² an **unbiased estimator** of σ²; N−1 is the **degrees of freedom**.
- **Coefficient of Variation (CV)**: CV = (s / X̄) × 100; compares dispersion across different units/scales.
- **Standard Deviation is preferred** because it uses all data points and yields to algebraic manipulation.

> **Key Point:** For a normal distribution, approximately **68%** of scores fall within ±1 SD, **95%** within ±2 SD, and **99.7%** within ±3 SD of the mean (the **68-95-99.7 rule**).

---

## 5.4 The Normal Distribution

- **Normal (Gaussian) distribution**: bell-shaped, perfectly symmetric, unimodal; described by two parameters: **μ** (mean) and **σ** (SD).
- Properties:
  1. **Symmetrical** about the mean.
  2. **Mean = Median = Mode** (all at the centre).
  3. **Asymptotic**: tails never touch the x-axis.
  4. **Unimodal**: one peak.
  5. Area under the curve = **1.00** (100%).
  6. Completely described by μ and σ.

| Range | % of Scores |
|-------|------------|
| μ ± 1σ | **68.26%** |
| μ ± 2σ | **95.44%** |
| μ ± 3σ | **99.73%** |

- **Standard Normal Distribution**: μ = 0, σ = 1; areas tabulated in z-tables.

---

## 5.5 Skewness and Kurtosis

### Skewness
- **Skewness**: degree of asymmetry of a distribution.
- **Positive skew**: tail extends to the right; most scores pile up on the left; mean > median > mode. Example: income.
- **Negative skew**: tail extends to the left; mean < median < mode. Example: easy test scores.
- **Pearson's coefficient of skewness**: Sk = 3(Mean − Median) / SD; range: −3 to +3; 0 = symmetric.

### Kurtosis
- **Kurtosis**: degree of peakedness/flatness of a distribution relative to normal.

| Type | Description | Peak | Tails |
|------|-------------|------|-------|
| **Mesokurtic** | Normal distribution | Moderate | Moderate |
| **Leptokurtic** | Taller and more peaked than normal | High | Heavy (fat) tails |
| **Platykurtic** | Flatter than normal | Low | Thin tails |

> **Key Point:** **Lepto** = thin (Greek) - a leptokurtic distribution is thin and tall. **Platy** = flat/broad. Kurtosis value for a normal curve = **3** (or **excess kurtosis = 0**).

---

## 5.6 Standard Scores (z-scores)

- **z-score**: expresses how many standard deviations a score is from the mean.
  - Formula: **z = (X − μ) / σ**
- Properties:
  - Mean of all z-scores = **0**.
  - SD of all z-scores = **1**.
  - z-scores are dimensionless (unit-free).
  - Converting to z-scores is called **standardisation**.
- **Uses**: compare scores from different distributions; find percentile ranks using z-tables; identify outliers (|z| > 3).
- **T-scores**: T = 10z + 50; mean = 50, SD = 10; always positive; used in personality tests (e.g., MMPI).
- **Stanines**: range 1-9; mean = 5, SD ≈ 2; used in educational testing.

| z | Percentile (approx.) |
|---|----------------------|
| −2.0 | 2.28% |
| −1.0 | 15.87% |
| 0 | 50.00% |
| +1.0 | 84.13% |
| +2.0 | 97.72% |

---

## PART TWO: CORRELATION AND REGRESSION

## 5.7 Correlation: Meaning and Basics

- **Correlation**: statistical relationship between two variables; indicates direction and magnitude.
- Depicted by a **scatterplot** (each dot = one participant; X = predictor, Y = criterion).
- **Direction**: positive (both variables increase together) or negative (one increases as the other decreases).
- **Magnitude**: strength from 0 (no relationship) to ±1.00 (perfect relationship).
- **Correlation coefficient (r)**: single number summarising direction and magnitude.

| r value | Interpretation |
|---------|---------------|
| ±0.90 to ±1.00 | Very high |
| ±0.70 to ±0.89 | High |
| ±0.50 to ±0.69 | Moderate |
| ±0.30 to ±0.49 | Low |
| ±0.00 to ±0.29 | Negligible |

> **Key Point:** Correlation does NOT imply causation. A third variable (**confound**) may explain both variables; the relationship may be coincidental (**spurious correlation**).

---

## 5.8 Pearson Product-Moment Correlation (r)

- **Assumptions**: both variables are measured at **interval/ratio** scale; both are **normally distributed**; the relationship is **linear**; **homoscedasticity** (equal variance of Y across levels of X).
- **Formula**:

  r = Σ[(X − X̄)(Y − Ȳ)] / √[Σ(X − X̄)² × Σ(Y − Ȳ)²]

  Equivalent raw-score formula: r = [NΣ XY − (ΣX)(ΣY)] / √{[NΣX² − (ΣX)²][NΣY² − (ΣY)²]}

- **Coefficient of determination (r²)**: proportion of variance in Y explained by X. If r = 0.70, r² = 0.49; X accounts for **49%** of variance in Y.
- **Significance test for r**: t = r√(N − 2) / √(1 − r²); df = N − 2.

---

## 5.9 Spearman Rank-Order Correlation (rho / ρ)

- Used when data are **ordinal** or when Pearson assumptions are violated (non-normal, outliers, small N).
- **Formula**: ρ = 1 − [6ΣD² / N(N² − 1)], where D = difference between ranks of paired scores.
- ρ ranges from −1.00 to +1.00; interpreted identically to Pearson r.
- Also called **rank-difference correlation**.

---

## 5.10 Other Correlation Coefficients

| Coefficient | When Used | Nature of Variables |
|-------------|-----------|---------------------|
| **Pearson r** | Both continuous, normal, linear | Interval/Ratio × Interval/Ratio |
| **Spearman rho (ρ)** | Both ordinal; or non-normal continuous | Ordinal × Ordinal |
| **Point-biserial (r_pb)** | One continuous (normal), one true dichotomy | Interval/Ratio × True dichotomy (e.g., pass/fail) |
| **Biserial (r_b)** | One continuous, one artificial dichotomy | Interval/Ratio × Artificial dichotomy (e.g., pass/fail when underlying trait is continuous) |
| **Phi coefficient (φ)** | Both true dichotomies | True dichotomy × True dichotomy |
| **Tetrachoric (r_t)** | Both artificial dichotomies | Artificial dichotomy × Artificial dichotomy |
| **Kendall's tau (τ)** | Both ordinal; preferred over rho for small N with many ties | Ordinal × Ordinal |

> **Key Point:** A **true dichotomy** is naturally binary (sex: male/female; alive/dead). An **artificial dichotomy** is a continuous variable cut at a point (e.g., pass/fail on an exam, high/low anxiety). Choosing the wrong coefficient underestimates the true correlation.

---

## 5.11 Partial and Multiple Correlation

- **Partial correlation (r_12.3)**: correlation between two variables after statistically removing the influence of a third variable. Used to rule out **confounds**.
- **Multiple correlation (R)**: correlation between one criterion variable and a **linear combination** of two or more predictor variables; R ranges from 0 to +1.00.
- **Multiple R²** (coefficient of multiple determination): proportion of criterion variance explained by all predictors together.

---

## 5.12 Regression

- **Regression**: predicts the value of one variable (Y, criterion/dependent) from another (X, predictor/independent).
- **Line of best fit (regression line)**: minimises the sum of squared vertical deviations (least-squares criterion).
- **Simple regression equation**: **Y' = a + bX**
  - b = slope = r × (s_Y / s_X)
  - a = Y-intercept = Ȳ − b X̄
- **Standard error of estimate (S_est)**: average prediction error; S_est = s_Y × √(1 − r²). If r = ±1, S_est = 0 (perfect prediction); if r = 0, S_est = s_Y (no better than guessing the mean).
- **Multiple regression**: Y' = a + b₁X₁ + b₂X₂ + … + b_kX_k; each b is a **partial regression coefficient**.

> **Key Point:** The closer r² is to 1.00, the more accurate the prediction. **Regression to the mean**: extreme scores on a first test tend to be less extreme on a second test (Francis Galton's observation).

---

## PART THREE: PROBABILITY AND SAMPLING DISTRIBUTIONS

## 5.13 Basic Probability

- **Probability (p)**: p(A) = number of favourable outcomes / total possible outcomes; ranges 0 to 1.
- **Addition rule**: p(A or B) = p(A) + p(B) − p(A and B); for mutually exclusive events: p(A or B) = p(A) + p(B).
- **Multiplication rule**: p(A and B) = p(A) × p(B|A); for independent events: p(A and B) = p(A) × p(B).
- **Complement rule**: p(not A) = 1 − p(A).
- In hypothesis testing, probability of a result given the null hypothesis is true is the **p-value**.

---

## 5.14 Sampling Distribution of the Mean and the Central Limit Theorem

- **Sampling distribution of the mean**: the theoretical frequency distribution of sample means (X̄) from all possible samples of size N drawn from the same population.
- Properties:
  1. Mean of the sampling distribution = **μ** (population mean).
  2. Standard deviation of sampling distribution = **Standard Error of the Mean (SEM or σ_X̄)**: σ_X̄ = σ / √N.
  3. Shape approaches **normal** as N increases regardless of population shape (**Central Limit Theorem**).
- **Central Limit Theorem (CLT)**: for large N (N ≥ 30 rule of thumb), the sampling distribution of the mean is approximately normal even when the population is not.
- **Standard Error of the Mean (SEM)**: σ_X̄ = s / √N (when σ unknown, use s). SEM decreases as N increases; larger samples → more precise estimates.

> **Key Point:** The CLT is the theoretical foundation of all parametric significance tests. It justifies using z and t distributions even when the population is not perfectly normal, provided N is sufficient.

---

## PART FOUR: HYPOTHESIS TESTING

## 5.15 Logic of Significance Testing

1. State the **null hypothesis (H₀)**: assumes no effect, no difference, no relationship (e.g., μ₁ = μ₂).
2. State the **alternative hypothesis (H₁ or Hₐ)**: what the researcher predicts (e.g., μ₁ ≠ μ₂).
3. Choose **significance level (α)**: the probability threshold for rejecting H₀ (typically α = 0.05 or 0.01).
4. Calculate the **test statistic** and find its **p-value**.
5. If p ≤ α, **reject H₀** (result is statistically significant); if p > α, **fail to reject H₀**.

- **One-tailed test** (directional): H₁ specifies direction (e.g., μ₁ > μ₂); critical region is in one tail; more powerful but only justified if direction is predicted a priori.
- **Two-tailed test** (non-directional): H₁ is μ₁ ≠ μ₂; critical region split between both tails; more conservative; default choice.

---

## 5.16 Type I and Type II Errors

| | **H₀ is Actually True** | **H₀ is Actually False** |
|---|---|---|
| **Reject H₀** | **Type I Error (α)** - False Positive | Correct (Power = 1 − β) |
| **Fail to Reject H₀** | Correct (Confidence = 1 − α) | **Type II Error (β)** - False Negative |

- **Type I error (α)**: reject a true null hypothesis; probability = level of significance.
- **Type II error (β)**: fail to reject a false null hypothesis; probability = β.
- **Power (1 − β)**: probability of correctly rejecting a false H₀; increased by larger N, larger effect size, higher α, one-tailed tests, reducing measurement error.
- **Relationship**: reducing α increases β (trade-off); increasing N reduces both errors simultaneously.

> **Key Point:** In clinical psychology, a Type I error might mean treating someone who has no disorder; a Type II error might mean missing a real disorder. Context determines which error is more costly.

---

## 5.17 Degrees of Freedom and Confidence Intervals

- **Degrees of freedom (df)**: number of values free to vary once constraints are applied; typically df = N − 1 (one-sample) or N − 2 (correlation); affects the shape of t, F, and chi-square distributions.
- **Confidence interval (CI)**: range of values likely to contain the population parameter with a given probability.
  - 95% CI for a mean: X̄ ± t_(α/2, df) × (s / √N)
  - If the 95% CI does not include 0 (for a difference), the result is significant at α = 0.05.
- **Effect size (Cohen's d)**: d = (X̄₁ − X̄₂) / s_pooled; measures practical significance independent of N.
  - Small: d = 0.2; Medium: d = 0.5; Large: d = 0.8 (Cohen, 1988).
  - For correlations: r = 0.10 (small), 0.30 (medium), 0.50 (large).

> **Key Point:** A statistically significant result is **not** the same as a practically significant result. With very large N, tiny effects become significant. Always report **effect size** alongside p-values.

---

## PART FIVE: PARAMETRIC TESTS

## 5.18 Assumptions of Parametric Tests

1. Data are measured at **interval or ratio** scale.
2. The population is (approximately) **normally distributed**.
3. **Homogeneity of variance**: populations have equal variances (for between-group tests; tested with Levene's test).
4. **Independence of observations** (unless paired/repeated).
5. Parametric tests are **robust** to mild violations of normality when N is large (CLT).

---

## 5.19 The z-test

- Used when: σ (population SD) is **known**; N is large.
- Formula: **z = (X̄ − μ) / (σ / √N)**
- Critical values: z = ±1.96 (two-tailed, α = 0.05); z = ±2.58 (α = 0.01); z = 1.645 (one-tailed, α = 0.05).
- Rarely used in practice (σ seldom known); replaced by t-test.

---

## 5.20 The t-test

Used when σ is unknown and N is small; uses t-distribution (heavier tails than normal; approaches normal as df → ∞).

### One-sample t-test
- Compares a sample mean to a known/hypothesised population mean (μ₀).
- **t = (X̄ − μ₀) / (s / √N)**; df = N − 1.

### Independent-samples t-test (unpaired)
- Compares means of **two independent groups**.
- **t = (X̄₁ − X̄₂) / S_p√(1/n₁ + 1/n₂)**
  - Pooled SD: S_p = √[((n₁−1)s₁² + (n₂−1)s₂²) / (n₁ + n₂ − 2)]
- df = n₁ + n₂ − 2.
- If variances are unequal (Levene's p < 0.05): use **Welch's t-test** (corrected df).

### Paired-samples t-test (correlated / repeated measures)
- Compares two related means (pre-post, matched pairs, same participants in both conditions).
- **t = D̄ / (s_D / √N)**; where D = difference score for each pair; df = N − 1.
- More **powerful** than independent t-test (removes between-subjects variance).

> **Key Point:** Paired t-test requires the assumption that **difference scores** are normally distributed, not the raw scores. Use when the same or matched participants appear in both conditions.

---

## 5.21 Analysis of Variance (ANOVA)

- **Purpose**: compare means of **three or more groups** simultaneously; avoids inflating Type I error from multiple t-tests.
- **F-ratio**: F = MS_between / MS_within = (variance due to treatment + error) / (variance due to error alone).
- When H₀ is true, F ≈ 1; when H₀ is false, F > 1.

### One-Way ANOVA (single factor, k groups)

| Source | SS | df | MS | F |
|--------|----|----|-----|---|
| Between (Treatment) | SS_B | k − 1 | SS_B / (k−1) | MS_B / MS_W |
| Within (Error) | SS_W | N − k | SS_W / (N−k) | - |
| Total | SS_T | N − 1 | - | - |

- **SS_T = SS_B + SS_W**; N = total subjects; k = number of groups.
- Significant F indicates at least one group mean differs; does NOT identify which pairs differ.

### Post-Hoc Tests (after significant one-way ANOVA)

| Test | Controls for | Use When |
|------|-------------|----------|
| **Tukey's HSD** | Familywise α | Equal n, all pairwise comparisons; most common |
| **Bonferroni correction** | Familywise α | Small number of planned comparisons |
| **Scheffé** | Familywise α | Unequal n; most conservative; complex comparisons |
| **LSD (Fisher)** | Individual comparison | Most liberal; risk of Type I error |
| **Newman-Keuls** | Stepwise | Intermediate power |

### Two-Way (Factorial) ANOVA
- Two independent variables (factors); tests three effects: **main effect of A**, **main effect of B**, and **A × B interaction**.
- **Interaction**: effect of one factor depends on the level of the other; most theoretically important finding.

### Repeated-Measures ANOVA
- Same participants measured across all levels (within-subjects design); removes individual differences from error term; more powerful than between-subjects ANOVA.
- Assumption of **sphericity** (equal variances of difference scores); tested with **Mauchly's test**; correction: **Greenhouse-Geisser** or **Huynh-Feldt epsilon**.

### ANCOVA (Analysis of Covariance)
- Adds a **covariate** (continuous variable correlated with DV) to ANOVA to reduce error variance and equate groups on a preexisting variable (e.g., pre-test scores, IQ).
- Increases statistical power and controls for confounds.

> **Key Point:** F is always positive (ratio of variances). A significant F only tells you that groups differ somewhere; always follow up with planned contrasts or post-hoc tests.

---

## PART SIX: NON-PARAMETRIC TESTS

## 5.22 When to Use Non-Parametric Tests

Non-parametric tests (also called **distribution-free tests**) make NO assumption about population distribution. Use when:
1. Data are **nominal or ordinal** (categorical or ranked).
2. The population is severely **non-normal** and N is small.
3. There are extreme **outliers** that distort parametric results.
4. **Assumptions of parametric tests are clearly violated**.

Trade-off: non-parametric tests are generally **less powerful** than their parametric equivalents when parametric assumptions ARE met.

---

## 5.23 Chi-Square Tests (χ²)

### Goodness-of-Fit Test (one variable)
- Tests whether observed frequencies match an expected (theoretical) distribution.
- **χ² = Σ [(O − E)² / E]**; where O = observed frequency, E = expected frequency.
- df = k − 1 (k = number of categories).
- Example: testing whether a die is fair (6 categories → df = 5).

### Test of Independence (two variables, contingency table)
- Tests whether two categorical variables are independent.
- **χ² = Σ [(O − E)² / E]**; E_ij = (Row total_i × Column total_j) / Grand total N.
- df = (r − 1)(c − 1); r = rows, c = columns.
- Critical assumption: **expected frequency ≥ 5 in each cell** (if violated, use Fisher's Exact Test for 2×2).
- **Cramer's V**: effect size for chi-square; V = √(χ² / N × min(r−1, c−1)).

> **Key Point:** Chi-square is sensitive to **sample size**; large N makes even trivial associations significant. Always report Cramer's V or phi alongside χ².

---

## 5.24 Non-Parametric Tests: Full Table

| Parametric Equivalent | Non-Parametric Test | Design | Data Type |
|-----------------------|---------------------|--------|-----------|
| One-sample t-test | **Wilcoxon signed-rank test** (one-sample version) / **Sign test** | One group vs. hypothesised value | Ordinal |
| Independent t-test | **Mann-Whitney U test** | Two independent groups | Ordinal |
| Paired t-test | **Wilcoxon signed-rank test** | Two related groups / repeated measures | Ordinal |
| Paired t-test (signs only) | **Sign test** | Two related groups; minimal assumptions | Ordinal (direction only) |
| One-way ANOVA | **Kruskal-Wallis H test** | Three+ independent groups | Ordinal |
| Repeated-measures ANOVA | **Friedman test** | Three+ related groups / repeated measures | Ordinal |
| Pearson r | **Spearman rho (ρ)** | Association between two variables | Ordinal |
| Chi-square for 2×2 with small N | **Fisher's Exact Test** | Two independent dichotomies | Nominal |

### Mann-Whitney U Test
- Ranks all scores from both groups combined; U = n₁n₂ + n₁(n₁+1)/2 − R₁ (where R₁ = sum of ranks for group 1).
- Tests whether one group's ranks tend to be higher; large U (or small U) → significant.

### Wilcoxon Signed-Rank Test
- Ranks the **absolute differences** between paired scores; sums ranks of positive and negative differences separately; W = smaller of the two sums.

### Kruskal-Wallis H Test
- Ranks all N scores across k groups; H = [12 / N(N+1)] × Σ(R_j² / n_j) − 3(N+1); df = k − 1.
- Significant H → at least one group distribution differs; follow up with pairwise Mann-Whitney U tests.

### Friedman Test
- Ranks scores within each participant (block) across k conditions; χ²_r = [12 / Nk(k+1)] × ΣR_j² − 3N(k+1); df = k − 1.

### Sign Test
- Simplest non-parametric test; only uses direction (+ or −) of differences, not magnitude; very low power but assumption-minimal.

---

## PART SEVEN: CHOOSING THE RIGHT TEST

## 5.25 Statistical Test Decision Table

| Research Question | Number of Groups | Design | Data Type | Recommended Test |
|-------------------|-----------------|--------|-----------|-----------------|
| Compare sample mean to population | 1 group | Single sample | Interval/Ratio | **One-sample t-test** (or z if σ known) |
| Compare two groups | 2 | Independent | Interval/Ratio | **Independent t-test** |
| Compare two groups | 2 | Independent | Ordinal/Non-normal | **Mann-Whitney U** |
| Compare two groups | 2 | Independent | Nominal | **Chi-square** (or Fisher's Exact) |
| Compare pre-post (or matched) | 2 | Related/paired | Interval/Ratio | **Paired t-test** |
| Compare pre-post (or matched) | 2 | Related/paired | Ordinal | **Wilcoxon signed-rank** |
| Compare three or more groups | 3+ | Independent | Interval/Ratio | **One-way ANOVA** + post-hoc |
| Compare three or more groups | 3+ | Independent | Ordinal | **Kruskal-Wallis** |
| Compare three or more conditions | 3+ | Repeated measures | Interval/Ratio | **Repeated-measures ANOVA** |
| Compare three or more conditions | 3+ | Repeated measures | Ordinal | **Friedman test** |
| Association between two variables | - | Correlational | Interval/Ratio | **Pearson r** |
| Association between two variables | - | Correlational | Ordinal | **Spearman rho** |
| Association: two dichotomies | - | Correlational | Nominal/Dichotomous | **Phi coefficient / Chi-square** |
| Predict Y from one X | - | Regression | Interval/Ratio | **Simple linear regression** |
| Predict Y from multiple X | - | Regression | Interval/Ratio | **Multiple regression** |
| Two factors; one DV | 2 factors | Between-subjects | Interval/Ratio | **Two-way ANOVA** |
| Control a covariate | Any | Any | Interval/Ratio | **ANCOVA** |

> **Key Point:** The critical decision tree: (1) What is the **level of measurement** of the DV? (2) How many **groups/conditions**? (3) Is the design **independent or related**? (4) Are parametric **assumptions met**?

---

## Key Terms

| Term | Definition |
|------|-----------|
| **Descriptive statistics** | Methods that summarise and describe data |
| **Inferential statistics** | Methods for drawing conclusions about populations from samples |
| **Frequency distribution** | Table showing each score and its frequency |
| **Mean (X̄)** | Sum of scores divided by N; best measure for interval/ratio, normal data |
| **Median** | Middle score; best for skewed distributions or ordinal data |
| **Mode** | Most frequent score; only measure for nominal data |
| **Range** | Difference between highest and lowest score |
| **Variance (s²)** | Mean of squared deviations from the mean |
| **Standard deviation (s)** | Square root of variance; most common dispersion measure |
| **Normal distribution** | Symmetric, bell-shaped curve; mean = median = mode |
| **68-95-99.7 rule** | Percentage of scores within 1, 2, 3 SDs of the mean in a normal distribution |
| **Positive skew** | Tail to the right; mean > median > mode |
| **Negative skew** | Tail to the left; mean < median < mode |
| **Leptokurtic** | More peaked than normal; heavier tails |
| **Platykurtic** | Flatter than normal; thinner tails |
| **Mesokurtic** | Normal kurtosis |
| **z-score** | (X − μ) / σ; number of SDs from the mean |
| **T-score** | 10z + 50; mean = 50, SD = 10 |
| **Correlation coefficient (r)** | Index of direction and strength of linear relationship; −1 to +1 |
| **Pearson r** | Correlation for interval/ratio data; assumes normality and linearity |
| **Spearman rho (ρ)** | Non-parametric correlation; uses ranks |
| **Point-biserial (r_pb)** | Correlation: continuous × true dichotomy |
| **Phi coefficient (φ)** | Correlation: two true dichotomies |
| **Coefficient of determination (r²)** | Proportion of shared variance; r² × 100 = % variance explained |
| **Partial correlation** | Correlation between two variables controlling for a third |
| **Regression equation** | Y' = a + bX; predicts criterion from predictor |
| **Standard error of estimate** | s_Y × √(1 − r²); average error in prediction |
| **Sampling distribution of the mean** | Distribution of all possible sample means of size N |
| **Standard error of the mean (SEM)** | σ / √N; SD of the sampling distribution |
| **Central Limit Theorem** | Sampling distribution of mean approaches normal as N increases |
| **Null hypothesis (H₀)** | Hypothesis of no effect or difference |
| **Alternative hypothesis (H₁)** | Research hypothesis; predicts an effect or difference |
| **Type I error (α)** | Rejecting a true H₀; false positive |
| **Type II error (β)** | Failing to reject a false H₀; false negative |
| **Statistical power (1 − β)** | Probability of correctly rejecting a false H₀ |
| **Degrees of freedom (df)** | Number of values free to vary; N − 1 for one sample |
| **Confidence interval** | Range likely to contain the population parameter |
| **Effect size (Cohen's d)** | Magnitude of difference in SD units; d = 0.2/0.5/0.8 = small/medium/large |
| **z-test** | Tests mean against population with known σ |
| **Independent t-test** | Compares means of two independent groups |
| **Paired t-test** | Compares two related means (pre-post or matched) |
| **F-ratio** | MS_between / MS_within; foundation of ANOVA |
| **One-way ANOVA** | Compares three or more independent group means |
| **Post-hoc tests** | Pairwise comparisons after significant ANOVA (Tukey, Bonferroni, Scheffé) |
| **Factorial ANOVA** | ANOVA with two or more independent variables |
| **Interaction** | Effect of one factor depends on level of another factor |
| **ANCOVA** | ANOVA with a covariate; reduces error, controls confounds |
| **Chi-square (χ²)** | Non-parametric test for categorical data; goodness-of-fit or independence |
| **Mann-Whitney U** | Non-parametric equivalent of independent t-test |
| **Wilcoxon signed-rank** | Non-parametric equivalent of paired t-test |
| **Kruskal-Wallis H** | Non-parametric equivalent of one-way ANOVA |
| **Friedman test** | Non-parametric equivalent of repeated-measures ANOVA |
| **Sign test** | Simplest non-parametric test; uses direction only |
| **Homoscedasticity** | Equal variance of Y across levels of X; assumption of regression and ANOVA |
| **Levene's test** | Tests homogeneity of variance assumption |
| **Sphericity** | Assumption of repeated-measures ANOVA; equal variances of difference scores |
| **Greenhouse-Geisser** | Correction for violations of sphericity |

---

## Likely Exam Points

1. **Mean, median, mode in skewed distributions**: positive skew → Mode < Median < Mean; negative skew → Mean < Median < Mode. The mean is pulled toward the tail.

2. **68-95-99.7 rule**: μ ± 1σ = 68.26%; μ ± 2σ = 95.44%; μ ± 3σ = 99.73%. These values are commonly tested directly.

3. **z-score formula**: z = (X − μ) / σ. A z-score of +1.96 cuts off the top 2.5% of a normal distribution (α = 0.05, two-tailed).

4. **Pearson r assumptions**: interval/ratio data, linear relationship, normality, homoscedasticity. Violation → use Spearman rho.

5. **r² (coefficient of determination)**: if r = 0.80, then r² = 0.64 means 64% of variance in Y is explained by X.

6. **Point-biserial vs. biserial vs. phi vs. tetrachoric**: the key is whether the dichotomy is TRUE (natural binary) or ARTIFICIAL (continuous variable dichotomised). True × True = phi; Artificial × Artificial = tetrachoric.

7. **Type I vs. Type II errors**: setting α = 0.01 reduces Type I error but increases Type II error. Increasing N reduces BOTH error types simultaneously.

8. **Statistical power** is increased by: larger N, larger effect size, higher α, one-tailed tests, reducing measurement error, using repeated-measures designs.

9. **Cohen's d benchmarks**: 0.2 = small; 0.5 = medium; 0.8 = large. For r: 0.10/0.30/0.50.

10. **Independent t-test formula** uses pooled variance; df = n₁ + n₂ − 2. **Paired t-test** uses difference scores; df = N − 1 (number of pairs minus 1).

11. **One-way ANOVA**: F = MS_between / MS_within; df_between = k − 1; df_within = N − k. Significant F alone does NOT tell you which groups differ; post-hoc tests are required.

12. **Tukey's HSD** is the most commonly tested post-hoc test; used for equal n and all pairwise comparisons. Scheffé is most conservative.

13. **Interaction in factorial ANOVA**: when the effect of Factor A is different at different levels of Factor B, an interaction is present. Always plot and interpret interactions before main effects.

14. **Chi-square formula**: χ² = Σ[(O − E)²/E]; df for independence = (r−1)(c−1); expected frequency assumption: E ≥ 5 in each cell.

15. **Non-parametric equivalents**: Mann-Whitney U = independent t-test; Wilcoxon signed-rank = paired t-test; Kruskal-Wallis = one-way ANOVA; Friedman = repeated-measures ANOVA.

16. **Central Limit Theorem**: even if the population is non-normal, the sampling distribution of the mean becomes approximately normal when N ≥ 30. This justifies parametric tests.

17. **Standard error of the mean (SEM)**: SEM = s / √N. Larger N → smaller SEM → more precise estimate of μ. Confidence interval width is proportional to SEM.

18. **Partial correlation** removes the influence of a third variable; used to test whether a correlation is spurious or genuine after controlling for a confound.

19. **Regression line**: always passes through the point (X̄, Ȳ); slope b = r × (s_Y / s_X); Y-intercept a = Ȳ − bX̄.

20. **Kurtosis**: normal curve kurtosis = 3 (or excess kurtosis = 0). Leptokurtic > 3 (tall, heavy tails); platykurtic < 3 (flat, thin tails).

---
*Source: Statistics for Behavioural Sciences (standard canonical treatment; complements A.K. Singh Part Three and Coolican). Part of [[INDEX]].*
