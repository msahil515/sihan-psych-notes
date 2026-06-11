---
date: 2026-06-11
book: "Amity Entrance: Master Syllabus (RCI / NIMHANS pattern)"
subject: "Amity Prep"
chapter: 6
tags: [amity, RCI, clinical-psychology, NIMHANS-pattern, entrance, MET2026]
---

# Ch 6: Experimental Designs, Path Modeling & Validity Threats

This chapter teaches how psychologists establish cause: how extraneous variables are controlled, how true and quasi and single-subject designs are built, how mediation and moderation decompose causal pathways, and the full Campbell and Stanley catalogue of internal and external validity threats. These topics are heavily tested on RCI and NIMHANS-pattern papers as direct definition items and as applied "which threat is this" vignettes.

## 1. Controlling Extraneous Variables

An **extraneous variable** is any variable other than the independent variable (IV) that could influence the dependent variable (DV). When an extraneous variable systematically co-varies with the IV, it becomes a **confound** and destroys internal validity. The experimenter has a toolbox of control techniques.

**Operationalization** is the first step: defining a fuzzy construct in terms of the concrete, measurable operations used to produce or measure it. "Anxiety" becomes "score on the Beck Anxiety Inventory" or "number of self-touches in 5 minutes." Good operational definitions are precise, replicable, and valid for the construct. Without them, variables cannot be controlled because they are not even pinned down.

**Elimination** removes the extraneous variable entirely from the situation. If noise might affect concentration, you soundproof the room so noise is zero for everyone. This is the cleanest control but is impossible for variables you cannot physically remove (you cannot eliminate participants' intelligence or age).

**Constancy** (holding conditions constant) keeps an extraneous variable at the same fixed level for all participants rather than removing it. The same time of day, same room temperature, same experimenter, same instructions for everyone. The variable still exists but no longer co-varies with the IV, so it cannot bias the comparison. Constancy is the workhorse of routine lab control.

**Matching** equates groups on a known nuisance variable before assigning conditions. In **precision matching**, participants are paired so each pair has near-identical scores on the matching variable (e.g., IQ), and one member of each pair goes to each condition. In **frequency-distribution (range) matching**, groups are made equivalent on the mean and spread of the variable without pairing individuals. Matching is powerful when the matching variable is strongly correlated with the DV, but it controls only the variables you thought to match on, and it can introduce statistical regression if groups are matched on an unreliable measure.

**Randomization** (random assignment) is the single most powerful control because it distributes ALL extraneous variables, known and unknown, probabilistically equally across conditions. With enough participants, groups become equivalent on age, motivation, prior history, and a thousand variables you never measured. Randomization does not guarantee equality in any one experiment, but it makes systematic bias unlikely and is the defining feature of a **true experiment**. Note the distinction: random *sampling* concerns external validity (who is in the study), random *assignment* concerns internal validity (who goes to which condition).

### 1.1 Counterbalancing and Latin Squares

In **within-subjects (repeated-measures) designs**, every participant experiences every condition, which controls individual differences perfectly but introduces **order effects**: practice, fatigue, carryover, and sensitization that depend on the sequence of conditions. **Counterbalancing** controls order effects by varying the order across participants.

**Complete counterbalancing** uses every possible order. With *k* conditions there are *k!* orders (3 conditions = 6 orders, 4 conditions = 24 orders), so it becomes impractical quickly. **Partial (incomplete) counterbalancing** uses a subset of orders.

A **Latin square** is a partial-counterbalancing scheme in which each condition appears exactly once in each ordinal position (first, second, third, etc.). For *k* conditions you need *k* sequences (a *k* × *k* square). A **balanced Latin square** additionally ensures each condition precedes and follows every other condition equally often, which controls first-order carryover effects, not just position. The standard balanced-square row generation order is 1, 2, *k*, 3, *k*-1, 4, and so on. Latin squares are efficient because they balance order with far fewer sequences than complete counterbalancing.

## 2. Mediation and Moderation (Path Modeling)

Both ask "what comes between X and Y," but they answer different questions and are tested as a classic contrast.

A **mediator** explains *how* or *why* X affects Y: it is an intervening variable on the causal chain X → M → Y. Example: stress (X) raises cortisol (M) which impairs memory (Y). A **moderator** specifies *when* or *for whom* X affects Y: it changes the strength or direction of the X → Y relationship. Example: the effect of therapy (X) on outcome (Y) is stronger for high-motivation clients (Z). Mnemonic: mediator = mechanism (in between), moderator = condition (it depends).

### 2.1 Mediation: Baron and Kenny

**Baron and Kenny (1986)** proposed the classic **causal-steps** approach. Label the paths: *a* = X → M, *b* = M → Y (controlling X), *c* = total X → Y, *c'* = X → Y controlling M (direct effect). The four conditions are:

1. X significantly predicts Y (path *c* is significant), there is an effect to mediate.
2. X significantly predicts M (path *a* is significant).
3. M significantly predicts Y controlling for X (path *b* is significant).
4. When M is added, the X → Y effect shrinks. If it drops to non-significance you have **full (complete) mediation**; if it shrinks but stays significant you have **partial mediation**.

The **indirect effect** is the product **a × b** (equivalently *c* − *c'* in simple models). This is the amount of X's effect on Y that travels through M.

The **Sobel test** tests whether the indirect effect a × b is significantly different from zero. Its statistic is z = (a × b) / SE, where the standard error SE = √(b²·sa² + a²·sb²), with sa and sb the standard errors of paths *a* and *b*. The Sobel test assumes the indirect effect is normally distributed, which is often false; modern practice prefers **bootstrapped confidence intervals** for a × b (e.g., the PROCESS macro), and a bias-corrected bootstrap CI that excludes zero indicates significant mediation. Note the exam point: contemporary thinking holds that a significant *c* is NOT strictly required (X can have no total effect yet still operate through suppressing indirect paths).

### 2.2 Moderation

Moderation is tested as a statistical **interaction**. In regression, you enter X, the moderator Z, and the **product term X × Z**: Y = b0 + b1·X + b2·Z + b3·(X × Z). A significant b3 means the slope of Y on X depends on Z (moderation present). Predictors are usually **mean-centered** before forming the product to reduce multicollinearity and make lower-order terms interpretable. Significant interactions are unpacked by plotting **simple slopes** of X → Y at low, mean, and high values of Z (often ±1 SD). When the moderator is categorical (e.g., gender, diagnosis), moderation is also tested via **multi-group SEM**, comparing a model where paths are forced equal across groups against one where they are freely estimated; a significant chi-square difference indicates the path differs by group (moderation). A variable can be both a **moderated mediator** (mediation strength depends on Z) or a **mediated moderator**.

## 3. Design Typologies

### 3.1 True (Factorial) Experiments

A **true experiment** has (a) manipulation of at least one IV and (b) random assignment to conditions. A **factorial design** crosses two or more IVs (factors), each with two or more levels, so every combination is tested. A 2 × 3 design has 2 factors with 2 and 3 levels = 6 cells. Factorial designs yield two kinds of effects:

- **Main effect**: the overall effect of one factor averaged across the levels of the other factor(s). A 2 × 2 design has two possible main effects.
- **Interaction effect**: the effect of one factor *differs depending on* the level of another factor. The 2 × 2 has one possible two-way interaction. An interaction appears as non-parallel lines on a graph. Interactions are usually more theoretically interesting than main effects because they reveal moderation. When an interaction is significant, main effects must be interpreted cautiously.

### 3.2 Quasi-Experimental Designs

A **quasi-experiment** manipulates an IV (or uses a naturally occurring treatment) but **lacks random assignment**. It is used when randomization is impossible or unethical (you cannot randomly assign people to trauma, school district, or diagnosis). Internal validity is therefore weaker. Key types:

- **Nonequivalent control group design**: a treatment group and a comparison group that were not randomly formed (e.g., two intact classrooms), both given a pretest and posttest. Because groups may differ at baseline, the chief threat is **selection** and **selection-maturation** interactions. The pretest lets you check baseline equivalence and statistically adjust.
- **Interrupted time-series design**: many repeated observations on a single group before and after an intervention (O O O O X O O O O). A treatment effect shows as a change in level or slope at the point of interruption. Many pre-observations let you rule out **maturation** and **regression**; the main remaining threat is **history** (some other event coinciding with the intervention). Adding a control series (multiple time-series) strengthens it.
- **Regression-discontinuity (RD) design**: assignment to treatment is determined by a **cutoff score on a continuous assignment variable** (e.g., students scoring below 40 get tutoring). The treatment effect is the **discontinuity (jump) in the regression line at the cutoff**. Because assignment is fully known and modeled, RD has internal validity approaching a randomized experiment near the cutoff, which is why it is highly regarded among quasi-designs.

### 3.3 Single-Subject (Single-Case) Designs

Single-subject designs study **one participant (or a few) intensively across many measurements**, used heavily in behavior analysis (ABA), clinical case work, and operant research. The participant serves as their own control; the logic is repeated demonstration of effect. Core terms: **A** = baseline phase (no treatment, measured to stability), **B** = treatment phase.

- **AB design**: baseline then treatment. Weakest, because a single A-to-B change is confounded with history/maturation.
- **ABA (reversal/withdrawal)**: baseline, treatment, return to baseline. If behavior reverses when treatment is withdrawn, the treatment is implicated. Ethically awkward because it ends in baseline (no treatment).
- **ABAB**: adds a second treatment phase, ending on treatment (better ethically) and providing two demonstrations of the effect, strengthening causal inference. Reversal logic only works for **reversible behaviors**; it fails for learning that does not un-learn.
- **Multiple-baseline design**: introduces the treatment in a staggered, sequential fashion and shows the behavior changes only when and where treatment is applied. Three variants: **across subjects** (same behavior, several people, treat one at a time), **across behaviors** (one person, several behaviors, treat one at a time), and **across settings** (one behavior, several settings, treat one setting at a time). This avoids withdrawal entirely, so it suits irreversible behaviors and is ethically preferable.

## 4. Internal Validity Threats (Campbell & Stanley)

**Internal validity** is the degree to which we can confidently conclude that the IV (not something else) caused the change in the DV. The classic threats:

| Threat | What it is |
|---|---|
| **History** | A specific external event (other than the IV) occurring between pretest and posttest that affects the DV (a news event during a study on attitudes). |
| **Maturation** | Internal changes in participants over time (growth, aging, fatigue, boredom, hunger) that are not due to the IV. |
| **Testing** | Taking a pretest changes performance on the posttest (practice effects, becoming test-wise). |
| **Instrumentation** | A change in the measuring instrument or in observers/raters over time (a scale drifts, raters get lenient or stricter). |
| **Statistical regression** (regression to the mean) | Participants selected for extreme scores tend to score closer to the mean on retest regardless of treatment, because extreme scores partly reflect measurement error. |
| **Selection** | Pre-existing differences between groups because they were not randomly assigned. |
| **Attrition / mortality** | Differential dropout of participants from groups, so the remaining groups are no longer comparable. |
| **Selection-maturation interaction** | Selected groups mature or change at different rates, mimicking a treatment effect. |

Other named threats include **diffusion of treatment** (control group learns and uses the treatment), **compensatory rivalry / resentful demoralization**, and **ambiguous temporal precedence** (unclear whether X preceded Y). Random assignment defends against selection-based threats; a control group defends against history, maturation, testing, instrumentation, and regression because those affect both groups equally.

## 5. External Validity Threats

**External validity** is the degree to which results **generalize** to other people, settings, times, and operations. Generalizing to a defined target population is sometimes called **population validity**; generalizing to other settings, **ecological validity**. The threats are usually framed as **interactions of the treatment effect with some factor**:

- **Selection × treatment interaction**: the treatment effect holds only for the particular kind of people sampled (e.g., works for college volunteers but not the general public). Limits generalization to other populations.
- **Setting × treatment interaction**: the effect holds only in the specific setting (the lab) and may not replicate in clinics, schools, or homes. This is the core of low ecological validity.
- **History × treatment (interaction of treatment with time)**: results are tied to a particular historical moment and may not generalize to other times.
- **Reactive arrangements / Hawthorne effect**: participants change behavior simply because they know they are being observed or are in a study; the **Hawthorne effect** (named from the Western Electric Hawthorne Works studies, 1920s-30s) is the classic case where productivity rose under almost any change because of the attention itself.
- **Demand characteristics** (Orne): cues in the experimental situation that signal what is expected, leading participants to guess the hypothesis and behave accordingly (the "good-subject" effect).
- **Experimenter / Rosenthal expectancy effect**: the experimenter's own expectations unintentionally bias participants' behavior or the recording of data. **Rosenthal and Jacobson's** "Pygmalion in the classroom" showed teachers' induced expectations raised the IQ of randomly labeled "bloomers." The defense is the **double-blind** procedure, where neither participant nor experimenter knows the condition assignment.
- **Reactive (pretest) sensitization**: taking the pretest makes participants more responsive to the treatment, so the effect would not appear in an unpretested population. The **Solomon four-group design** detects and controls this by crossing (pretest vs no pretest) with (treatment vs control).

There is often a **trade-off**: tight laboratory control maximizes internal validity but the artificial setting can reduce external validity, while naturalistic field studies maximize ecological validity at the cost of control.

## High-Yield Recap

- **Control techniques**: operationalization (define measurably), elimination (remove it), constancy (hold it fixed), matching (equate groups on a nuisance variable), randomization (distributes ALL variables, defines a true experiment). Random *assignment* = internal validity; random *sampling* = external validity.
- **Counterbalancing** controls order effects in within-subjects designs. Complete = *k*! orders. **Latin square** = *k* × *k*, each condition once per position; **balanced** Latin square also controls carryover.
- **Mediator** = mechanism (X → M → Y, *how/why*); **moderator** = condition (X × Z interaction, *when/for whom*).
- **Baron & Kenny (1986)** four steps: c significant, a significant, b significant, c' shrinks (full if to non-significance, partial if still significant). Indirect effect = **a × b**. **Sobel z = a·b / √(b²sa² + a²sb²)**; bootstrap CI preferred.
- **Moderation** = product term X × Z in regression (center predictors); categorical moderator tested via **multi-group SEM** chi-square difference.
- **Factorial** designs give **main effects** (one per factor) and **interaction** effects (non-parallel lines). A 2 × 3 = 6 cells.
- **Quasi (no random assignment)**: nonequivalent control group (threat = selection), interrupted time-series (threat = history), regression-discontinuity (cutoff on continuous variable, treatment = jump at cutoff, strongest quasi-design).
- **Single-subject**: AB (weak), ABA (reversal, ends in baseline), ABAB (two demonstrations, ends on treatment); reversal needs reversible behavior. **Multiple-baseline** across subjects / behaviors / settings (staggered, no withdrawal, good for irreversible behaviors).
- **Internal validity threats**: history, maturation, testing, instrumentation, statistical regression (to the mean, from extreme-score selection), selection, attrition/mortality, selection-maturation interaction.
- **External validity threats**: selection × treatment, setting × treatment, history × treatment, reactive arrangements / **Hawthorne effect**, **demand characteristics** (Orne, good-subject effect), **experimenter/Rosenthal expectancy** (Pygmalion; defended by double-blind), pretest sensitization (controlled by **Solomon four-group design**).
- Internal vs external validity is a **trade-off**: lab control raises internal validity, lowers ecological validity.
