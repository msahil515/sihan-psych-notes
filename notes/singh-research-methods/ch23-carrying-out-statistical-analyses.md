---
date: 2026-05-29
book: "Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh)"
subject: "Research Methodology, Statistics & Psychological Testing"
chapter: 23
tags: [statistics, parametric, nonparametric, ANOVA, t-test, normal-curve, skewness, kurtosis, standard-scores, MET-2026]
---

# Carrying Out Statistical Analyses

Chapter 23 covers the full pipeline of applied statistical analysis: the distinction between sample and population, the theoretical basis of the normal curve, measures of departure from normality (skewness and kurtosis), standard score transformations, and the logic, assumptions, and computation of the major parametric and nonparametric tests used in behavioural research. It concludes with post hoc procedures, ANCOVA, and MANOVA/MANCOVA.

---

## Sample and Population

A **population** is the totality of a particular group or set of individuals or objects (e.g., all arts graduates, all university employees). A **sample** is any selected subset drawn from a population according to some rule or plan.

- **Statistic**: a measure computed from a sample.
- **Parameter**: a measure computed from the entire population.
- A statistic is the estimate of the corresponding parameter.

### Types of Samples

| Type | Basis of Selection |
|---|---|
| **Probability sample** | Chance/random process; each individual has a known probability of selection |
| **Nonprobability sample** | Judgment-based; probability of individual selection is unknown |

### Hidden Population

A **hidden population** is a population of people who engage in clandestine, socially disapproved, or concealed activities and are very difficult to locate and study. Examples include populations relevant to AIDS research and deviant behaviour studies. Both probability and nonprobability sampling techniques are used for studying hidden populations.

### Central Limit Theorem

The **Central Limit Theorem** describes the nature of sample means and enables generalizations about a population with known probability. For samples usually greater than N = 50 drawn randomly from a population, it predicts three things:

1. The means of the samples will be **normally distributed**.
2. The **mean of the sample means** will be identical to the mean of the population.
3. The distribution of sample means will have its own standard deviation, called the **standard error of the mean**.

### Types of Statistics

| Type | Definition |
|---|---|
| **Descriptive statistics** | Used when dealing with an entire population; describes its characteristics |
| **Inferential (inductive/sampling) statistics** | Used when dealing with a sample; provides information about the population from which the sample was drawn |

---

## Normal Curve

### Historical Development

| Scholar | Period | Contribution |
|---|---|---|
| **De Moivre** | 1733 | First to develop the mathematical equation of the normal curve |
| **Gauss and Laplace** | Early 19th century | Independently rediscovered the normal curve; interested in distribution of errors in astronomy; called it "normal law of error" |
| **Quetelet** (Belgian) | Mid-19th century | Extended normal curve to anthropology, sociology, meteorology, and human affairs |
| **Galton** | Late 19th century | Systematically studied normal distribution; showed physical and psychological traits conform to the normal curve |

The normal curve is known by various names: **Gaussian Curve**, **De Moivre's Curve**, **bell-shaped curve**, **curve of error**.

### Definition

A **normal distribution** is one in which the majority of cases are located in the middle of the scale and only a small number at both extremes.

### Major Characteristics of a Normal Curve

1. Always **symmetrical**: right half is equivalent to left half in all respects.
2. **Unimodal**: mode at the centre. **Mean = Median = Mode**, all located at the centre.
3. **Asymptotic to the x-axis**: never touches the baseline, no matter how far extended.
4. Frequency is **highest at the centre**: all ordinates on both sides are smaller than the highest ordinate.
5. **Continuous**.

### Area under the Normal Curve

| Range | Area Included |
|---|---|
| ±1 SD from mean | 34.13% + 34.13% = **68.26%** (approximately 2/3 of cases) |
| ±2 SD from mean | 68.26% + 13.59% + 13.59% = **95.44%** |
| ±3 SD from mean | 95.44% + 2.15% + 2.15% = **99.74%** |
| Beyond ±3 SD | Only **0.26%** of total area |

**Practical Applications of the Normal Curve:**
1. Transforming raw scores into standard scores.
2. Calculating percentile rank of given scores.
3. Normalizing an obtained distribution.
4. Testing significance of obtained measures against a chance hypothesis.
5. Scaling data from attitude scales, ratings, or rankings via suitable numerical transformations.

**Reasons Researchers Prefer Normal Distributions:**
- (a) Useful mathematical features form the basis for several inferential statistics (e.g., the t-test assumes normality of the underlying population).
- (b) Mathematical precision allows accurate computation of area under different regions of the curve.
- (c) Normal distributions arise spontaneously in nature; important physical characteristics (birth weight, brain weight) and mental characteristics (intelligence) approximate the normal curve for large groups.

---

## Nonnormal Distributions: Skewness and Kurtosis

**Nonnormal distributions** deviate from the symmetric bell-shaped form. The two primary concerns in behavioural research are skewness and kurtosis.

---

### Skewness

**Skewness** is a condition in which a frequency distribution departs from a symmetrical shape.

| Type | Direction of Pile-up | Position of Mean Relative to Median |
|---|---|---|
| **Positive skewness** | Scores piled at low/left end; tail extends right | Mean lies **to the right** of the median |
| **Negative skewness** | Scores piled at high/right end; tail extends left | Mean lies **to the left** of the median |
| **Zero skewness** | Normal distribution (mean = median) | Mean = Median |

#### Formula 1: Skewness via Percentiles (Formula 23.1)

$$S_k = \frac{P_{90} + P_{10} - 2 \cdot Mdn}{P_{90} - P_{10}}$$

- $S_k$ = skewness; $Mdn$ = Median; $P_{90}$ = 90th percentile; $P_{10}$ = 10th percentile

#### Standard Error of Skewness (Formula 23.2)

$$SE_{Sk} = \frac{0.2425}{\sqrt{P_{90} - P_{10}}}$$

- If $S_k / SE_{Sk} \geq 1.96$: positive skewness is statistically significant.
- If $S_k / SE_{Sk} \leq -1.96$: negative skewness is statistically significant.
- If $-1.95 \leq S_k / SE_{Sk} \leq +1.95$: failed to prove skewness exists. **This does NOT mean the curve is symmetrical.**

#### Formula 2: Skewness via Mean, Median, and SD

$$S_k = \frac{\text{Mean} - \text{Median}}{\text{SD}} \qquad \text{or} \qquad S_k = \frac{\text{Mean} - \text{Mode}}{\text{SD}}$$

Standard error in this form: $S_{Sk} = \sqrt{6/N}$

#### Causes of Skewness (Four Situations)

| Situation | Direction |
|---|---|
| Natural restriction at the low end of scale (e.g., number of offspring, commission earned) | **Positive** skewness |
| Natural restriction at the high end of scale (e.g., maximum errors fittable in a box) | **Negative** skewness |
| Artificial restriction at the low end (e.g., extremely difficult test — most score near zero) | **Positive** skewness |
| Artificial restriction at the high end (e.g., extremely easy test — most score near maximum) | **Negative** skewness |

#### Interpretation of Skewness in Test Construction

- **Positive skewness** (scores concentrated at low end): test has **too few easy items**; cannot discriminate at lower end.
- **Negative skewness** (scores concentrated at high end): test has **too few hard items**; cannot discriminate at upper end.
- Remedy: add/modify items, or apply a statistical scale transformation to normalize the distribution.
- **Normalization** (making $S_k \approx 0.005$) is widely used in determining T scores.

**Square-root transformation** to reduce positive skewness: $X = 2 \rightarrow \sqrt{2} = 1.41$; $X = 3 \rightarrow \sqrt{3} = 1.73$. Increases small scores proportionally less and reduces spacing among larger scores.

---

### Kurtosis

**Kurtosis** refers to the peakedness or flatness of a frequency distribution compared with the normal distribution. It is the extent to which a curve is more or less peaked than a normal curve with the same standard deviation.

| Type | Description |
|---|---|
| **Leptokurtic** | More peaked than normal |
| **Mesokurtic** | Same peakedness as normal curve |
| **Platykurtic** | Flatter than normal |

In standard diagrams: **Curve A = leptokurtic, Curve B = mesokurtic, Curve C = platykurtic**.

---

## Measures of Relative Position: Standard Scores

A **standard score** is a derived score expressing the distance of a raw score from the mean in terms of standard deviations. Standard scores have a **fixed mean** and a **fixed standard deviation**.

---

### Linear Standard Scores

A **linear standard score** results from a linear transformation of original scores: subtracting the mean and dividing by the standard deviation. All characteristics of the original distribution are preserved.

**Formula for sigma score (z score):**

$$z = \frac{X - \bar{X}}{SD}$$

**Limitation of sigma (z) scores**: occurrence of negative values and decimal fractions.

#### Common Linear Standard Scores

| Scale | Mean | SD |
|---|---|---|
| **Sigma score (z score)** | 0 | 1 |
| **AGCT** (Army General Classification Test) | 100 | 20 |
| **CEEB** (College Entrance Examination Board) | 500 | 100 |
| **WISC/IQ** (Wechsler Intelligence Scale) | 100 | 15 |

Conversion: multiply z score by desired SD, then add desired mean.

**Note**: derived standard scores can be compared among themselves only when obtained from distributions with approximately similar shapes.

---

### Normalized Standard Scores (Nonlinear Standard Scores)

**Normalized standard scores** are expressed in a form where the distribution has been transformed to fit a normal curve via nonlinear transformations. Used when comparing scores from distributions of dissimilar shapes.

**Prerequisites for Using Normalized Standard Scores:**
1. The sample is **large**.
2. The sample is **representative**.
3. The non-normality of original scores is due to **defects in the test material**, not the nature of the trait being measured.

**Interpretation:**
- Score = 0: performance at the 50th percentile; excels over 50% of the group.
- Score = +2 SD: excels over approximately 98% of the group.
- Score = -2 SD: excels over only approximately 2% of the group.

**Common Examples:** **T scores** and **Stanine scores**.

If the original distribution is normal, linear and normalized standard scores give similar or identical results.

---

## Parametric and Nonparametric Statistical Tests

### Parametric Statistical Tests

A **parametric statistical test** specifies conditions about the parameters of the population from which a sample is taken. Generally more powerful than nonparametric tests.

**Assumptions of Parametric Tests:**
1. Observations must be **independent** (selection of one case must not depend on another).
2. Observations must be drawn from a **normally distributed population**.
3. Samples must have **equal variances** (principle of **homogeneity of variances**).
4. Data must be expressed in **interval or ratio scales** (nominal and ordinal measures do not qualify).
5. The variable under study must be **continuous**.

**Examples:** z test, t test, F test (ANOVA), Pearson r, MANOVA.

---

### Nonparametric Statistical Tests (Distribution-Free Statistics)

A **nonparametric statistical test** does not specify conditions about the parameters of the population. Also called **distribution-free statistics**.

**Advantages of Nonparametric Tests:**
1. Exact probability statements regardless of population distribution shape.
2. Applicable when data are in the form of ranks/order.
3. Can be applied to **nominal and ordinal data**.
4. Simpler computation; especially suited for small sample sizes.
5. Less restrictive assumptions.

**Disadvantages:**
1. Mosteller and Bush (1954) and Siegel and Castellan (1988): nonparametric statistics are **"wasteful of data"**.
2. Less efficient when parametric assumptions are met.
3. Tables scattered across different publications.

### Scale Level and Appropriate Statistic

| Level | Scale | Parametric Statistics | Nonparametric Statistics |
|---|---|---|---|
| 1 | Nominal | — | Mode, frequency distribution |
| 2 | Ordinal | — | Median, percentile, Rank-difference correlation (Rho), ANOVA by ranks |
| 3 | Interval | Mean, SD, Pearson r, t-test, F-test (ANOVA), MANOVA | — |
| 4 | Ratio | Mean, SD, Pearson r, t-test, F-test (ANOVA), MANOVA | — |

### Guidelines for Choosing

1. If assumptions are met, prefer parametric tests (consider amount of difference, not just order).
2. Central Limit Theorem ensures parametric benefit even near-normal distributions.
3. Non-normal data can be transformed to near-normal.
4. For N > 30, parametric tests can be safely used.
5. Very small samples: use nonparametric statistics.

---

## Parametric Statistics

The major parametric statistics are:
1. Student's t-test and z test
2. Analysis of Variance (F ratio/ANOVA)
3. Analysis of Covariance (ANCOVA)
4. Pearson r
5. Partial correlation and Multiple correlation

---

### 1. Student's t-Test and Z Test

Used to test the significance of the difference between two means. Computes a ratio of experimental variance (obtained mean difference) to error variance (standard error of the mean difference).

#### Key Distinction: t-Test vs Z Test

| Feature | t-Test (Student's t) | Z test |
|---|---|---|
| Sample size | Less than 30 (especially < 10) | Greater than 30 |
| SD used | Sample standard deviation (estimate when population SD is unknown) | Actual population SD |
| Table used | t-distribution table | Normal probability curve (z-table) |

**Historical note**: Concept developed in **1915** by **William Seely Gosset**, a statistician for Guinness Breweries in Dublin, Ireland. Published as **"Student"** due to the company's prohibition on publication under researcher's own name. Hence: **Student's t**.

As sample size increases, critical values of t approach z values of the normal probability table.

#### Assumptions of t-Test

1. Variances of the two samples are independent (**homogeneity of variances**).
2. Sample has been randomly selected.
3. Population distribution of scores is normal.

**Robustness**: The t-test is a **robust test** — inferences remain valid even with large departures from normality in large samples (N > 30). To address normality doubts, increase N as much as possible (Sibert, 1990).

#### General t-Ratio Formula (Formula 23.7)

$$t = \frac{M_1 - M_2}{SE_D}$$

- $M_1$ = mean of the first group; $M_2$ = mean of the second group; $SE_D$ = standard error of the difference between two sample means.

#### Three Types of t-Ratio Situations

1. **t ratio from independent groups**: no correlation between groups (e.g., separate groups of boys and girls).
2. **t ratio from correlated groups**: same group measured on two occasions (pre-test/post-test); correlation between scores is included.
3. **t ratio from matched groups**: groups matched in terms of means and SDs.

For **correlated groups**, the SE_D formula includes the correlation coefficient:

$$SE_D = \sqrt{\frac{N_1(SD_1^2 + SD_2^2 - 2r_{12} \cdot SD_1 \cdot SD_2)}{N(N-1)}}$$

Where $r_{12}$ = coefficient of correlation between the initial and final set of scores.

- df for correlated/matched groups: $df = N - 1$

---

### Key Concepts in Hypothesis Testing

#### Degree of Freedom (df)

**Degree of freedom** (df) means freedom to vary. It is the number of observations that are independent of each other and cannot be deduced from each other.

- Single sample: $df = N - 1$
- Paired scores: df = number of pairs - 1
- When the mean is computed, one df is used up (fixed), leaving $N - 1$ free to vary.

**Example**: 5 scores with mean = 10; $df = 5 - 1 = 4$ (four scores can be any value, but the fifth is determined by the constraint that the mean must equal 10).

#### Null Hypothesis (H₀)

The **null hypothesis** ($H_0$) is a **no-difference hypothesis** stating that observed differences between samples are due to chance, not true differences. Set up for the express purpose of being **rejected**.

The **alternative hypothesis ($H_1$)** is an operational statement of the researcher's research hypothesis. When $H_0$ is rejected, $H_1$ is accepted.

#### Level of Significance (Alpha Level)

| Alpha Level | Meaning |
|---|---|
| **0.05 (5%)** | 5% probability of rejecting a true H0; 95% confidence results are real |
| **0.01 (1%)** | 1% probability of rejecting a true H0; 99% confidence |
| **0.001** | 1 in 1000 replications would show results by chance; very stringent; uncommonly used |

#### Types of Errors in Hypothesis Testing

| Decision | H0 True | H0 False |
|---|---|---|
| **Fail to reject H0** | Correct decision | **Type II Error (Beta error)** |
| **Reject H0** | **Type I Error (Alpha error)** | Correct decision |

- **Type I Error (Alpha error)**: Rejecting a true null hypothesis. Risk = alpha level.
- **Type II Error (Beta error)**: Failing to reject a false null hypothesis (accepting H0 when it should be rejected).
- **Inverse relationship**: Reducing Type I error increases Type II error, and vice versa. To reduce **both**, increase N.

#### One-Tailed vs Two-Tailed Tests

| Feature | One-Tailed Test | Two-Tailed Test |
|---|---|---|
| Also called | Directional test | Nondirectional test |
| Hypothesis | Specifies direction: M1 > M2 OR M1 < M2 | Only states difference: M1 ≠ M2 |
| Critical region | All in one tail | Split equally in both tails |
| z cutoff at 0.05 | **1.64** | **1.96** |
| z cutoff at 0.01 | **2.33** | **2.58** |
| Terminology | Rejected at 5% or 1% **points** | Rejected at 5% or 1% **levels** |
| Preferred? | Less preferred (risks Type I error; misses effects in opposite direction) | More preferred and generally accepted |

**Problems with one-tailed tests:**
1. Makes it easier to reject H0 even when differences are small (greater Type I error risk).
2. Can only detect treatment effects in one direction; misses significant changes in the opposite direction.

#### Power of a Statistical Test

**Power** = the likelihood of rejecting H0 when, in fact, H1 is true. The probability of correctly rejecting a false H0.

$$\text{Power} = 1 - P(\text{Type II error})$$

**Factors Affecting Power:**

| Factor | Effect on Power |
|---|---|
| Larger alpha level | Increases power (easier to reject H0) |
| One-tailed test (vs two-tailed) | Increases power |
| Larger sample size (N) | Increases power (better representation of population) |

---

### 2. F Ratio and Analysis of Variance (ANOVA)

**ANOVA** (Analysis of Variance) was originally developed by **R.A. Fisher in the 1920s**.

**Advantages over multiple t-tests:**
1. Can compare more than two group means simultaneously.
2. Can account for interaction effects between independent variables.

#### Types of ANOVA

| Type | Description |
|---|---|
| **Simple (One-way) ANOVA** | One independent variable |
| **Two-way ANOVA** | Two independent variables |
| **MANOVA** | Multiple dependent variables |

#### Key Formulas and Concepts

**Partition of Variance:**

$$SS_{tot} = SS_{between} + SS_{within}$$

| Component | Also Called | Reflects |
|---|---|---|
| $SS_{between}$ | $SS_{treatment}$ | Effect of the independent variable; differences among group means |
| $SS_{within}$ | $SS_{error}$ | Sampling error and random factors within groups |
| $SS_{tot}$ | Total SS | Total variation of all scores about the grand mean |

**Correction Factor (CF):**

$$CF = \frac{(\Sigma X)^2}{N}$$

**Computation Formulas:**

$$SS_{tot} = \Sigma X^2 - CF$$

$$SS_{between} = \frac{(\Sigma X_1)^2}{n_1} + \frac{(\Sigma X_2)^2}{n_2} + \cdots - CF$$

$$SS_{within} = SS_{tot} - SS_{between}$$

**Degrees of Freedom:**

| Source | df |
|---|---|
| Between groups | $k - 1$ (k = number of groups) |
| Within groups | $N - k$ |
| Total | $N - 1$ |

**Mean Square (Variance Estimate):** $MS = SS / df$

**F Ratio:**

$$F = \frac{MS_{between}}{MS_{within}}$$

- Under H0: F ≈ 1. Under H1 (treatment effect present): F > 1.
- Compare obtained F with critical value from the **F table (Guilford and Fruchter, 1978)**: $df_1$ (between, numerator) on top; $df_2$ (within, denominator) on left side.

**Example with 3 groups, N=30:** $df_1 = 2$, $df_2 = 27$. Critical F at 0.05 level = 3.35; at 0.01 level = 5.49. If calculated F = 6.28, reject H0.

**Homogeneity of Variance: F-Max Test:**

$$F_{Max} = \frac{\text{Largest sample variance}}{\text{Smallest sample variance}}$$

If $F_{Max}$ is near 1, the assumption is not violated. Compare with critical values using k = number of groups and df = $n - 1$.

---

### Post Hoc Tests (A Posteriori Tests)

The F test only indicates an **overall** significant difference; it does not identify **which specific pairs** of means differ. Post hoc tests are used to locate exact pairwise differences after a significant F.

**Note**: a posteriori tests are generally **less powerful** than planned comparison (a priori) tests.

**Important post hoc tests:**
- **Newman-Keuls (NK) test**
- **Duncan's Multiple Range Test**
- **Tukey's Honestly Significant Difference (HSD) test** (most popular)
- **Scheffe test** (most popular; most conservative)

#### Tukey's HSD Test

Requires **equal n** in each group.

$$HSD = q\sqrt{\frac{MS_{within}}{n}}$$

- $MS_{within}$ = within-treatment variance
- $n$ = number of subjects per treatment group
- $q$ = **studentized range statistic** (from table by **Gravetter and Wallnau, 1987**)

**Decision rule:**
- Mean difference **> HSD**: significant difference between the two groups.
- Mean difference **< HSD**: no significant difference.

#### Scheffe Test

For each pair:

$$F = \frac{(M_1 - M_2)^2}{MS_w\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$

**Decision rule**: Compare obtained F with $(k-1) \times F_{critical}$. Only pairs where F exceeds this adjusted critical value are significant.

---

### 3. Analysis of Covariance (ANCOVA)

**ANCOVA** was developed by **R.A. Fisher**; first published example in **1932** from agricultural experimentation. A most widely used elaboration of ANOVA. May be regarded as a **partial correlation technique**.

ANCOVA employs **indirect statistical control** to enhance the precision of an experiment by statistically adjusting for a covariate.

**Key Terms:**
- **Covariate** (also called **concomitant variable**, designated **X**): the variable statistically controlled; measured **before** treatment to ensure independence from treatment.
- **Dependent variable (Y)**: the variable of experimental interest.
- Groups are compared on **adjusted Y scores** after variance due to X is removed.

**Assumptions of ANCOVA:**
1. X scores (covariate) are **not affected** by treatments.
2. Dependent variable is normally distributed in the population.
3. Regression coefficient of Y on X is the **same in all groups** (regression is **linear and consistent**; regression lines for all groups are **parallel**).
4. Treatment groups are randomly selected from the same population.
5. Within-group variances are approximately equal.

**ANCOVA degrees of freedom:**
- Within groups: $N - k - 1$ (one additional df lost for covariate estimation).
- Total: $N - 2$.

---

### MANOVA and MANCOVA

**MANOVA** (Multivariate Analysis of Variance): ANOVA with more than one dependent variable. Determines how groups differ on a **combination** of dependent variables. Different from running separate ANOVAs for each dependent variable.

**MANCOVA** (Multivariate Analysis of Covariance): ANCOVA with more than one dependent variable.

| Statistic | Dependent Variables | Independent Variables |
|---|---|---|
| ANOVA | 1 | 1 or more |
| MANOVA | 2 or more | 1 or more |
| ANCOVA | 1 | 1 or more + 1 covariate |
| MANCOVA | 2 or more | 1 or more + covariates |

---

## Key Terms

| Term | Definition |
|---|---|
| **Population** | Totality of a particular group or set of individuals/objects |
| **Sample** | Any selected subset drawn from a population |
| **Statistic** | A measure computed from a sample |
| **Parameter** | A measure computed from the entire population |
| **Hidden population** | Population engaging in clandestine/concealed activities; difficult to locate |
| **Central Limit Theorem** | For large random samples (N > 50), sample means are normally distributed, their mean = population mean, and they have a standard error of the mean |
| **Standard error of the mean** | Standard deviation of the distribution of sample means |
| **Descriptive statistics** | Statistics describing a whole population |
| **Inferential (inductive) statistics** | Statistics used to make inferences about a population from a sample |
| **Normal distribution** | Mean = median = mode; majority of cases in the middle, few at extremes |
| **Skewness** | Departure of a frequency distribution from symmetrical shape |
| **Positive skewness** | Scores piled at low end; tail extends right; mean > median |
| **Negative skewness** | Scores piled at high end; tail extends left; mean < median |
| **Kurtosis** | Peakedness or flatness of a distribution compared with normal |
| **Leptokurtic** | More peaked than normal |
| **Mesokurtic** | Same peakedness as normal |
| **Platykurtic** | Flatter than normal |
| **Standard score** | Score expressing distance from mean in SD units; fixed mean and SD |
| **Linear standard score** | From linear transformation; preserves all original distribution characteristics |
| **Normalized standard score** | From nonlinear transformation to fit a normal distribution |
| **Sigma score (z score)** | Linear standard score; mean = 0, SD = 1 |
| **T score** | Normalized standard score |
| **Stanine score** | Normalized standard score |
| **Parametric test** | Test specifying conditions about population parameters; requires normality, interval/ratio data, homogeneity of variance |
| **Nonparametric test (distribution-free)** | Test making no assumptions about population parameters or distribution shape |
| **Homogeneity of variances** | Assumption that samples have equal or nearly equal variances |
| **Null hypothesis (H0)** | No-difference hypothesis; set up to be rejected |
| **Alternative hypothesis (H1)** | Research hypothesis; accepted when H0 is rejected |
| **Level of significance (alpha level)** | Probability criterion for rejecting H0 |
| **Type I Error (Alpha error)** | Rejecting a true null hypothesis |
| **Type II Error (Beta error)** | Failing to reject a false null hypothesis |
| **Degree of freedom (df)** | Number of observations free to vary; typically N - 1 |
| **Student's t** | Parametric statistic for comparing two means; developed by Gosset (1915); robust; used when N < 30 |
| **Z test** | Parametric statistic for comparing two means; N > 30; uses population SD |
| **One-tailed test** | Directional test; critical region in one tail; rejected at "points" |
| **Two-tailed test** | Nondirectional test; critical region split in both tails; rejected at "levels" |
| **Power of a test** | Probability of correctly rejecting a false H0; = 1 - P(Type II error) |
| **ANOVA** | Analysis of Variance; tests differences among 3+ group means using F ratio; developed by R.A. Fisher (1920s) |
| **SS_between** | Between-groups sum of squares; reflects effect of independent variable |
| **SS_within** | Within-groups sum of squares; reflects error/random variation |
| **F ratio** | Ratio of between-groups MS to within-groups MS |
| **Post hoc tests (a posteriori tests)** | Tests used after significant F to locate specific pairwise differences |
| **Tukey's HSD** | Post hoc test using Honestly Significant Difference; requires equal n; uses studentized range statistic q |
| **Scheffe test** | Most conservative post hoc test; computes adjusted F ratios for each pair |
| **ANCOVA** | Analysis of Covariance; ANOVA with statistical control via a covariate; developed by R.A. Fisher (1932) |
| **Covariate (concomitant variable)** | Variable statistically controlled in ANCOVA; measured before treatment; must be unaffected by treatment |
| **MANOVA** | ANOVA with multiple dependent variables |
| **MANCOVA** | ANCOVA with multiple dependent variables |
| **Robust test** | A test whose inferences remain valid even with violations of assumptions |

---

## Key People / Tests

| Name | Contribution |
|---|---|
| **De Moivre (1733)** | First to develop the mathematical equation of the normal curve |
| **Gauss and Laplace (early 19th century)** | Independently rediscovered the normal curve; applied to astronomy/error distribution; coined "normal law of error" |
| **Quetelet (mid-19th century, Belgian)** | Extended normal curve to anthropology, sociology, meteorology, and human affairs |
| **Galton (late 19th century)** | Showed physical and psychological traits conform to the normal curve |
| **William Seely Gosset ("Student") (1915)** | Developed small-sample t-test at Guinness Breweries, Dublin; published under pen name "Student" |
| **R.A. Fisher (1920s; 1932)** | Developed ANOVA in 1920s; first published ANCOVA example in 1932 |
| **Mosteller and Bush (1954)** | Described nonparametric statistics as "wasteful of data" |
| **Siegel and Castellan (1988)** | Echoed the "wasteful of data" critique of nonparametric statistics |
| **Gravetter and Wallnau (1987)** | Provided table of Studentized Range Statistic (q) for Tukey's HSD |
| **Guilford and Fruchter (1978)** | Standard reference for the F table used in ANOVA |
| **Whitney (1948)** | Argued for nonparametric approaches for ordinal data |
| **AGCT** | Army General Classification Test; linear standard score; mean = 100, SD = 20 |
| **CEEB** | College Entrance Examination Board score; linear standard score; mean = 500, SD = 100 |
| **WISC** | Wechsler Intelligence Scale; linear standard score; mean = 100, SD = 15 |
| **Newman-Keuls (NK) Test** | Post hoc comparison after significant F |
| **Duncan's Multiple Range Test** | Post hoc comparison after significant F |
| **Tukey's HSD Test** | Most popular post hoc test; uses q statistic; requires equal n |
| **Scheffe Test** | Most popular post hoc test; most conservative; works for unequal n |

---

## Likely Exam Points

1. **De Moivre (1733)** was the first to develop the mathematical equation of the normal curve. Gauss and Laplace independently rediscovered it (for astronomy/errors). Quetelet extended it to social sciences. Galton applied it to physical and psychological traits.

2. **Area under the normal curve**: ±1 SD = **68.26%**; ±2 SD = **95.44%**; ±3 SD = **99.74%**; beyond ±3 SD = only **0.26%**.

3. In a normal distribution: **mean = median = mode**. In **positive skew**: mean is to the **RIGHT** of the median. In **negative skew**: mean is to the **LEFT** of the median.

4. **Positive skewness** = test **too difficult** (too few easy items; scores piled at low end). **Negative skewness** = test **too easy** (too few hard items; scores piled at high end).

5. **Student's t-test** was developed by **William Seely Gosset in 1915**, published under the pen name **"Student"** due to Guinness Breweries' prohibition on employees publishing under their real name.

6. **t-test** when N < 30 (uses sample SD); **z-test** when N > 30 (uses population SD). As N increases, t critical values approach z critical values.

7. **Type I Error (Alpha)** = rejecting a true H0. **Type II Error (Beta)** = failing to reject a false H0. Reducing Type I error **increases** Type II error. To reduce **both**, increase N.

8. **One-tailed**: z = 1.64 (0.05) or 2.33 (0.01); results stated at "**points**." **Two-tailed**: z = 1.96 (0.05) or 2.58 (0.01); results stated at "**levels**." Two-tailed tests are generally **preferred**.

9. **Power of a test = 1 - P(Type II error)**. Power **increases** with: larger alpha level, one-tailed tests, larger sample size.

10. **ANOVA** was developed by **R.A. Fisher in the 1920s**. F = MS_between / MS_within. df_between = k-1; df_within = N-k; df_total = N-1.

11. **ANCOVA** was also developed by **R.A. Fisher**; first published example in **1932**. The covariate (X) must be measured before treatment, must not be affected by treatment, and regression lines for all groups must be **parallel**.

12. **AGCT**: mean = 100, SD = 20. **CEEB**: mean = 500, SD = 100. **WISC/IQ**: mean = 100, SD = **15**. All are **linear standard scores**.

13. **Tukey's HSD** formula: $HSD = q \sqrt{MS_{within}/n}$. If mean difference > HSD, significant. Requires **equal** group sizes. $q$ value from Studentized Range Statistic table (Gravetter and Wallnau, 1987).

14. **Nonparametric tests** = **distribution-free statistics**; appropriate for nominal and ordinal data. Called "**wasteful of data**" by Mosteller and Bush (1954) and Siegel and Castellan (1988) when parametric assumptions can be met.

15. **Normalized standard scores** (T scores, Stanines) should only be used when: the sample is large and representative, AND non-normality is due to defects in the test itself, not the trait being measured.

---

The study note is ready. It covers every section in the chapter with full definitions, formulas, tables, researcher attributions, and 15 targeted exam points. You can copy this directly into your knowledge base or Obsidian vault.

---
*Source: Tests, Measurements and Research Methods in Behavioural Sciences (A.K. Singh), Chapter 23: Carrying Out Statistical Analyses (vision-transcribed). Part of [[INDEX]].*
