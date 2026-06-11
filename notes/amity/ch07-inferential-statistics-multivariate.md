---
date: 2026-06-11
book: "Amity Entrance: Master Syllabus (RCI / NIMHANS pattern)"
subject: "Amity Prep"
chapter: 7
tags: [amity, RCI, clinical-psychology, NIMHANS-pattern, entrance, MET2026]
---

# Ch 7: Inferential Statistics, Assumptions & Multivariate Modeling

This chapter takes you from the logic of hypothesis testing through every parametric and non-parametric test you will be asked about, then into correlation, regression, and the multivariate machinery (MANOVA, factor analysis) that NIMHANS-pattern and Amity papers love to probe. The recurring exam trick is the assumption layer: examiners test whether you know *which* test is valid *when*, so learn the diagnostics as carefully as the tests themselves.

## 1. The Logic of Inference: From Sample to Population

Inferential statistics let us reason from a **sample** to the **population** it was drawn from. The bridge is the **sampling distribution**: the theoretical distribution of a statistic (usually the mean) computed over infinitely many samples of fixed size N.

### Central Limit Theorem (CLT)
The **Central Limit Theorem** states that the sampling distribution of the mean approaches a **normal distribution** as N increases, *regardless of the shape of the parent population*, provided observations are independent and variance is finite. Its standard deviation is the **standard error of the mean**, SEM = sigma / sqrt(N). The practical rule of thumb is that for **N greater than or equal to 30** the sampling distribution is approximately normal even if the raw data are skewed. This is why large-sample z and t procedures stay valid on non-normal data: it is the *mean* that is normal, not the raw scores. The CLT is the single justification for most parametric inference, so exam items often ask "why can we use a t-test on skewed data with large N?" The answer is the CLT.

### Type I and Type II Error
Every decision risks two mistakes. A **Type I error** (false positive) is rejecting a true null hypothesis; its probability is **alpha**, the significance level set in advance, conventionally 0.05. A **Type II error** (false negative) is failing to reject a false null hypothesis; its probability is **beta**. The two trade off: lowering alpha (being more conservative) raises beta. Memorize the 2x2 decision grid below.

| | H0 actually true | H0 actually false |
|---|---|---|
| **Reject H0** | Type I error (alpha) | Correct (Power = 1 - beta) |
| **Fail to reject H0** | Correct (1 - alpha) | Type II error (beta) |

### Statistical Power
**Power** equals **1 - beta**, the probability of correctly detecting a real effect. Power rises with (a) larger **sample size N**, (b) larger **effect size**, (c) larger **alpha** (a more lenient criterion), and (d) lower error variance / more reliable measures. Conventionally researchers target **power of 0.80**. A **power analysis** computed before data collection ("a priori") tells you the N needed to detect an expected effect; this is what ethics boards and the RCI-style methodology questions want. Underpowered studies inflate false negatives and produce unreplicable findings.

## 2. Effect Size: How Big, Not Just Whether

A significant p-value tells you an effect probably exists; an **effect size** tells you how large it is, independent of N. This matters because with huge N even trivial differences reach significance.

- **Cohen's d** is the standardized mean difference for two groups: d = (M1 - M2) / SD_pooled, where the **pooled SD** combines both groups' variances. Benchmarks: **0.2 = small, 0.5 = medium, 0.8 = large**.
- **Eta-squared (eta^2)** is the proportion of total variance explained by a factor in ANOVA: SS_effect / SS_total. It is biased upward and inflates when multiple factors are present.
- **Partial eta-squared** isolates one effect by removing other effects from the denominator: SS_effect / (SS_effect + SS_error). SPSS reports this by default for factorial designs; values across factors can sum to more than 1.
- **Omega-squared (omega^2)** is a less biased, population-corrected alternative to eta-squared, preferred for small samples because it subtracts expected error variance.

## 3. Parametric Assumptions and Their Diagnostics

Parametric tests assume **normality of the distribution (of residuals/sampling distribution)**, **homogeneity of variance**, **interval/ratio data**, and **independence of observations**. Violations push you toward corrections or non-parametric alternatives.

### Testing Normality
- **Shapiro-Wilk test** is the most powerful normality test for **small samples (N < 50)**. A *non-significant* result (p > 0.05) means you fail to reject normality, which is what you want.
- **Kolmogorov-Smirnov test (with Lilliefors correction)** compares the sample's cumulative distribution to a reference distribution and is used for **larger samples (N >= 50)**.
- **Skewness** measures asymmetry (positive = long right tail; negative = long left tail). **Kurtosis** measures tail heaviness/peakedness (**leptokurtic** = heavy-tailed/peaked, positive excess; **platykurtic** = flat, negative excess; **mesokurtic** = normal). Values within roughly +/-1 (some texts +/-2) are treated as acceptable.

### Testing Homogeneity of Variance
- **Levene's test** checks equality of variances across groups and is **robust to non-normality** because it uses deviations from the group median/mean; a non-significant result supports the equal-variance assumption. It is the default for t-tests and ANOVA.
- **Bartlett's test** also tests homogeneity of variance but is **highly sensitive to departures from normality**, so it is used only when normality is well established.

### Repeated-Measures Specific: Sphericity
**Mauchly's test of sphericity** checks whether the variances of the *differences* between all pairs of within-subject conditions are equal, an assumption unique to **repeated-measures ANOVA**. If Mauchly's is significant (sphericity violated), you must correct the degrees of freedom. The **Greenhouse-Geisser** correction (more conservative) is used when the epsilon estimate is low (below about 0.75); the **Huynh-Feldt** correction is used when epsilon is higher (above 0.75) as it is less conservative. Both shrink the df, raising the critical F so the test is not falsely liberal.

### ANCOVA-Specific: Homogeneity of Regression Slopes
**ANCOVA** (analysis of covariance) additionally assumes **homogeneity of regression slopes**: the relationship between the covariate and the dependent variable is the same across all groups. Statistically you test the covariate-by-factor interaction; if it is *non-significant*, the assumption holds and ANCOVA is valid. A significant interaction means the covariate adjustment differs by group, invalidating standard ANCOVA.

### Regression-Specific: Multicollinearity
In multiple regression, **multicollinearity** is high intercorrelation among predictors, which inflates standard errors and destabilizes coefficients. The **Variance Inflation Factor (VIF)** quantifies it: VIF = 1 / (1 - R^2_j) for predictor j. A common cutoff is **VIF > 10** (some use 5) signaling a problem; **tolerance** (1/VIF) below 0.1 flags the same issue.

## 4. The t-Test Family

The **t-test** compares means using the **t-distribution** (heavier-tailed than normal, flattening as df grow toward the normal). Three forms:

- **One-sample t-test**: compares a sample mean to a known/hypothesized population value.
- **Independent-samples t-test**: compares means of two *unrelated* groups; assumes equal variances.
- **Paired (dependent) t-test**: compares two *related* scores (same subjects, pre/post or matched pairs); it analyzes the mean of the difference scores.
- **Welch's t-test**: an independent-samples variant that does **not** assume equal variances; it adjusts the degrees of freedom downward. Use it when Levene's test is significant. Many statisticians now recommend Welch as the default.

## 5. Analysis of Variance (ANOVA)

ANOVA compares **three or more** group means by partitioning variance, avoiding the inflated Type I error of running many t-tests. The core identity is:

**SS_total = SS_between + SS_within**

where SS_between captures variance due to the treatment (group differences) and SS_within is error (variability inside groups). The **F-ratio = MS_between / MS_within** (each MS = SS / its df). A large F means between-group variance dominates error, signaling real differences.

- **One-way ANOVA**: one factor, multiple levels.
- **Factorial ANOVA**: two or more factors, yielding **main effects** plus **interaction effects** (the effect of one factor depends on the level of another). The interaction is usually the most exam-relevant term.
- **Repeated-measures ANOVA**: the same subjects across conditions; more powerful because it removes between-subject variance, but requires **sphericity** (see Mauchly above).
- **ANCOVA**: ANOVA with a **covariate** statistically partialled out to reduce error variance and adjust group means (e.g., controlling for baseline IQ).

### MANOVA
**MANOVA** (multivariate ANOVA) handles **two or more dependent variables simultaneously**, testing whether groups differ on a *combination* of DVs while controlling the overall Type I error. Four multivariate test statistics appear in output:

| Statistic | Note |
|---|---|
| **Wilks' Lambda** | Most commonly reported; ranges 0-1, *smaller* = stronger effect (proportion of variance NOT explained) |
| **Pillai's Trace** | Most **robust** to assumption violations and unequal cell sizes; preferred when assumptions are shaky |
| **Hotelling's Trace** | Useful with two groups |
| **Roy's Largest Root** | Most powerful when DVs are strongly correlated but least robust |

### Post-Hoc Tests
A significant ANOVA says *some* means differ but not which; **post-hoc** tests do pairwise comparisons while controlling familywise error.

- **Tukey's HSD (Honestly Significant Difference)**: all pairwise comparisons, equal n, good balance of power and control. The standard choice.
- **Bonferroni correction**: divides alpha by the number of comparisons (alpha/k); simple but very **conservative** (low power) with many comparisons.
- **Scheffe's test**: the most conservative; allows *any* complex comparison (not just pairs), so use it for unplanned contrasts.
- **Dunnett's test**: compares every treatment group only against a single **control** group, gaining power by not testing all pairs.

## 6. Non-Parametric Tests

When normality, variance, or measurement-level assumptions fail (or data are ordinal), use distribution-free **non-parametric** tests, which typically work on **ranks**.

| Parametric test | Non-parametric equivalent | Use |
|---|---|---|
| Independent t-test | **Mann-Whitney U** | Two independent groups, ranked |
| Paired t-test | **Wilcoxon signed-rank** | Two related samples, ranked differences |
| One-way ANOVA | **Kruskal-Wallis H** | 3+ independent groups, ranked |
| Repeated-measures ANOVA | **Friedman test** | 3+ related conditions, ranked |

### Chi-Square and Categorical Tests
- **Chi-square test of independence** tests whether two categorical variables are associated, comparing **observed** vs **expected** frequencies. A core rule: **expected frequency in each cell should be >= 5**.
- **Chi-square goodness-of-fit** tests whether one categorical variable's distribution matches an expected/theoretical distribution.
- **Yates' continuity correction** is applied to a **2x2 chi-square** to reduce overestimation of significance with small samples (it subtracts 0.5 from each |O - E| before squaring).
- **Fisher's exact test** replaces chi-square when expected counts are too small (cells < 5) in a 2x2 table, giving an exact probability.
- **McNemar's test** is for **paired/related categorical data** (e.g., the same subjects before vs after), testing change in proportions on a 2x2 of discordant pairs.

## 7. Correlation: Measuring Association

A **correlation coefficient** ranges from **-1 to +1**, where 0 means no linear relationship. Choose the coefficient by the variables' measurement levels.

| Coefficient | When to use |
|---|---|
| **Pearson r** | Two continuous, linearly related, normally distributed variables |
| **Spearman rho** | Two ordinal (ranked) variables, or non-linear monotonic relationships |
| **Kendall's tau** | Ordinal data, especially small samples or many tied ranks (more robust than rho) |
| **Point-biserial** | One continuous + one *genuine* dichotomy (e.g., sex) |
| **Biserial** | One continuous + one *artificial* dichotomy (an underlying continuum forced into two categories) |
| **Phi coefficient** | Two genuine dichotomies (2x2) |
| **Tetrachoric** | Two artificial dichotomies, each assumed to mask an underlying normal continuum |

**Partial correlation** measures the association between two variables while removing the influence of a third variable from *both*. **Semi-partial (part) correlation** removes the third variable from only *one* of the two variables; it is the basis of the unique contribution of a predictor in regression.

## 8. Regression

**Ordinary Least Squares (OLS) regression** fits the line minimizing the sum of squared residuals, predicting a continuous outcome from one or more predictors. **R-squared** is the proportion of variance explained; **adjusted R-squared** penalizes for the number of predictors so it does not inflate as you add useless variables, making it the honest fit index for multiple regression.

### Variable Entry Methods
- **Stepwise regression** lets a statistical algorithm add/remove predictors based on significance; it is **data-driven**, atheoretical, and prone to capitalizing on chance (criticized for poor replication).
- **Hierarchical regression** enters predictors in **theory-driven blocks** specified by the researcher, examining the change in R-squared at each step. This is the methodologically preferred, hypothesis-testing approach.

### Logistic Regression
**Logistic regression** predicts a **binary (categorical) outcome** by modeling the log-odds (logit). Coefficients are interpreted as **odds ratios**: an OR > 1 means higher odds of the outcome per unit of the predictor, OR < 1 means lower odds, OR = 1 means no effect. The **Wald test** assesses whether each individual coefficient is significant. The **Hosmer-Lemeshow test** checks overall **goodness of fit**, and here you *want a non-significant* result (p > 0.05), meaning predicted and observed values agree.

## 9. Factor Analysis

Factor analysis reduces many observed variables to fewer underlying **latent factors**, central to test construction and validity questions.

### PCA vs PAF
- **Principal Component Analysis (PCA)** is technically a data-reduction technique that uses *total* variance (it puts 1s in the diagonal of the correlation matrix) to create components.
- **Principal Axis Factoring (PAF)**, a true common-factor model, analyzes only **shared (common) variance**, seeking the latent factors that cause the correlations. Use PAF/EFA when your goal is to identify underlying constructs, PCA when the goal is pure dimension reduction.

### Deciding How Many Factors
- **Kaiser criterion**: retain factors with **eigenvalue > 1** (each factor must explain more variance than a single variable). It tends to *over*-extract.
- **Scree plot**: plot eigenvalues in descending order and retain factors *above the elbow* where the curve levels off.
- **Parallel analysis** (Horn's method) is the most accurate: retain factors whose real eigenvalues exceed those from random data of the same size.

### Rotation
Rotation clarifies which variables load on which factor (simple structure).
- **Orthogonal rotation** keeps factors **uncorrelated**: **Varimax** (maximizes variance of loadings within factors, the most common) and **Quartimax** (simplifies variables across factors).
- **Oblique rotation** allows factors to **correlate** (realistic for psychological constructs): **Promax** and **Oblimin (Direct Oblimin)**.

### Reading the Output
A **factor loading** is the correlation between a variable and a factor; loadings above about **0.32** (roughly 10% shared variance) are usually interpreted as meaningful, with 0.40-0.50+ considered strong. **Communality (h^2)** is the proportion of a variable's variance accounted for by all retained factors (the sum of its squared loadings); low communality means the variable does not fit the factor solution.

## High-Yield Recap

- **CLT**: sampling distribution of the mean is normal for **N >= 30**, regardless of population shape; SEM = sigma/sqrt(N).
- **Type I = alpha** (false positive, reject true H0); **Type II = beta** (false negative); **Power = 1 - beta**, target **0.80**, rises with N, effect size, alpha.
- **Cohen's d**: 0.2/0.5/0.8 = small/medium/large; **partial eta-squared** = SS_effect/(SS_effect+SS_error); **omega-squared** less biased than eta-squared.
- **Shapiro-Wilk** for N<50, **Kolmogorov-Smirnov** for N>=50 normality; non-significant = normal.
- **Levene's** = robust homogeneity of variance (default); **Bartlett's** = normality-sensitive.
- **Mauchly's** tests sphericity in repeated-measures ANOVA; if violated correct df via **Greenhouse-Geisser** (epsilon < 0.75) or **Huynh-Feldt** (epsilon > 0.75).
- **ANCOVA** assumes **homogeneity of regression slopes** (non-significant covariate-by-factor interaction).
- **VIF > 10** flags multicollinearity (tolerance < 0.1).
- **Welch's t** when variances unequal; **Paired t** for related samples.
- ANOVA identity: **SS_total = SS_between + SS_within**; F = MS_between/MS_within.
- **MANOVA**: Wilks' Lambda (common, smaller=stronger), Pillai (most robust), Hotelling, Roy's.
- Post-hoc: **Tukey HSD** (standard), **Bonferroni** (conservative, alpha/k), **Scheffe** (most conservative, complex contrasts), **Dunnett** (vs one control).
- Non-parametric map: Mann-Whitney U / Wilcoxon signed-rank / Kruskal-Wallis H / Friedman.
- Chi-square needs **expected >= 5**; **Yates** correction for 2x2; **Fisher's exact** for tiny cells; **McNemar** for paired categorical.
- Correlations: Pearson (continuous), Spearman/Kendall (ordinal), point-biserial (true dichotomy), biserial (artificial), phi (2 true dichotomies), tetrachoric (2 artificial). **Partial** removes a third variable from both; **semi-partial** from one.
- **Adjusted R-squared** penalizes predictor count; **stepwise** = data-driven, **hierarchical** = theory-driven blocks.
- **Logistic regression**: odds ratios; **Wald** test per coefficient; **Hosmer-Lemeshow** non-significant = good fit.
- Factor analysis: **PCA** = total variance, **PAF** = common variance; retain factors with **eigenvalue > 1** (Kaiser), scree elbow, or parallel analysis; **Varimax/Quartimax** orthogonal, **Promax/Oblimin** oblique; meaningful **loading > 0.32**; **communality** = variance explained per variable.
