# How every metric is calculated

This page shows how every metric in the skills is calculated, in one place, grouped by analysis type. It is written for coaches and sports scientists who want to check a number by hand, or compare it with a vendor export.

The skill reference files are the source of truth. This page condenses them and adds nothing to them. If this page and a reference file differ, follow the reference file and fix this page. Change this page in the same commit as any formula change in a reference file.

Every metric on this page is decision support only. No number here clears an athlete for training, competition, or return to sport. No number here predicts injury or makes a training decision. Each breakdown keeps the limits its reference file states.

## Contents

This page has these sections:

- [Monitoring statistics](#monitoring-statistics)
  - [Shared rules for judging change](#shared-rules-for-judging-change)
  - [Typical error](#typical-error)
  - [Smallest worthwhile change](#smallest-worthwhile-change)
  - [Minimal detectable change](#minimal-detectable-change)
  - [Individual baselines and z-scores](#individual-baselines-and-z-scores)
  - [Group p-values for individual athletes](#group-p-values-for-individual-athletes)
- [Load and wellness](#load-and-wellness)
  - [Session RPE load](#session-rpe-load)
  - [Heart rate load](#heart-rate-load)
  - [Acute to chronic workload ratio](#acute-to-chronic-workload-ratio)
  - [Wellness z-score](#wellness-z-score)
- [Running load](#running-load)
  - [Total distance and distance per minute](#total-distance-and-distance-per-minute)
  - [High-speed running distance](#high-speed-running-distance)
  - [Accelerations and decelerations](#accelerations-and-decelerations)
- [Force plate](#force-plate)
  - [Countermovement jump height](#countermovement-jump-height)
  - [Reactive strength index-modified](#reactive-strength-index-modified)
  - [Isometric mid-thigh pull peak force](#isometric-mid-thigh-pull-peak-force)
  - [Eccentric hamstring force](#eccentric-hamstring-force)
- [Velocity-based training](#velocity-based-training)
  - [Mean concentric velocity](#mean-concentric-velocity)
  - [Velocity loss](#velocity-loss)
- [Limb symmetry](#limb-symmetry)
  - [Limb symmetry index](#limb-symmetry-index)
- [Composites](#composites)
  - [Readiness composite](#readiness-composite)
- [Vendor metric pages](#vendor-metric-pages)
- [Sources](#sources)

## How to read this page

Each analysis type starts with a summary table of its metrics, formulas, units, and reference files. One breakdown per metric follows the table. Each breakdown has these parts:

- **What it measures**: the metric in plain words, with the limits the reference file states
- **Inputs**: the raw signals or columns the metric needs
- **Calculation**: the formula with every term defined, then numbered steps from raw inputs
- **Worked example**: the inputs and the result from the reference file, condensed, with the key intermediate values
- **Variants**: other formulas in use, and when each applies
- **What changes the number**: settings, thresholds, windows, and protocol choices that change the result when the athlete has not changed
- **Units and typical range**: the units, and the range the reference file gives, with its source
- **Vendor equivalents**: the matching metric in the VALD, Hawkin Dynamics, Catapult, Kinexon, Polar, Firstbeat, GymAware, or Perch device reference files, how the vendor calculates it, and any difference in method
- **Reference file**: a link to the full metric reference file

Read the page with these conventions in mind:

- Code font marks column names, field names, and vendor metric names.
- Worked examples use made-up numbers for illustration, as in the reference files.
- "None" under vendor equivalents means no device reference file maps that metric.
- Citations name the source the reference file gives. The full list with DOIs is in [Sources](#sources).

## Monitoring statistics

These metrics judge whether a change in one athlete is real, and whether it is big enough to matter. Every other analysis type on this page uses them.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Typical error (TE) | `TE = SD(diff) / √2` | Units of the measure | [typical-error.md](../skills/monitoring-statistics/references/typical-error.md) |
| Coefficient of variation (CV%) | `CV% = 100 × TE / grand mean` | % | [typical-error.md](../skills/monitoring-statistics/references/typical-error.md) |
| Smallest worthwhile change (SWC) | `SWC = 0.2 × SD_between` | Units of the measure | [smallest-worthwhile-change.md](../skills/monitoring-statistics/references/smallest-worthwhile-change.md) |
| Minimal detectable change (MDC) | `MDC95 = SEM × 1.96 × √2`, `MDC90 = SEM × 1.645 × √2` | Units of the measure | [minimal-detectable-change.md](../skills/monitoring-statistics/references/minimal-detectable-change.md) |
| Noise band against a baseline mean (derived) | `1.96 × TE × √(1 + 1/n)` | Units of the measure | [individual-baselines-z-scores.md](../skills/monitoring-statistics/references/individual-baselines-z-scores.md) |
| Usual-variation band, when no TE exists | `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)` | Units of the measure | [individual-baselines-z-scores.md](../skills/monitoring-statistics/references/individual-baselines-z-scores.md) |
| Individual z-score | `z = (today − baseline_mean) / baseline_SD` | No unit | [individual-baselines-z-scores.md](../skills/monitoring-statistics/references/individual-baselines-z-scores.md) |
| Group p-value | A paired t-test on change scores. The file gives no formula. | Probability from 0 to 1 | [misleading-methods.md](../skills/monitoring-statistics/references/misleading-methods.md) |

The file `misleading-methods.md` also covers the acute to chronic workload ratio (ACWR). This page breaks the ACWR down under [Load and wellness](#load-and-wellness), from `acwr.md`.

### Shared rules for judging change

Every skill that judges whether a change, a difference, or an asymmetry is real states these rules the same way. They come from the monitoring statistics reference files.

Take typical error from the right study:

- Take TE from a short-term test-retest study in which no true change is expected (Hopkins, 2000; Swinton et al., 2018). Hopkins (2000) states that this TE suits decisions about change in an individual over any time frame.
- Retesting on separate days is an optional practice choice, not a published rule. It counts normal day-to-day variation as noise and gives a larger TE than a same-day retest. Name the choice with the result.
- Compute TE on the same summary you compare: a single trial, the best of 3, or the mean of 3. The error of a mean of n independent trials is TE / √n (Hopkins, 2000).
- An SD from the athlete's own baseline values is not TE. It mixes biological variation with measurement error. Do not use it as TE.

When no TE exists, use the usual-variation band from `individual-baselines-z-scores.md` instead:

```text
Usual-variation band:   baseline mean ± t(n − 1) × baseline SD × √(1 + 1/n)
```

Apply these rules to it:

- Use at least 10 values from a stable period, with today left out. Hopkins (2017) says at least 10 tests are needed for even modest precision. His monitoring spreadsheet uses the athlete's own scatter about the trend line when no short-term TE is entered.
- Take t from n − 1 degrees of freedom. The band is the standard prediction interval for one new value (NIST, Dataplot reference manual, after Hahn and Meeker, 1991, pp. 61-62). With 10 values, the multiplier is t(9) × √(1 + 1/10) = 2.2622 × 1.0488 = 2.37.
- With 10 stable values, independent days, and normal data, 5.0% of values fall outside the band by chance with t(9), and 8.2% with 1.96. In a simulation run for the skill, a correlation of 0.3 or 0.5 between consecutive days raised the t(9) rate to 5.7% or 6.6%.
- Give two states only: within usual variation or outside usual variation. Add no smallest worthwhile change tier.
- Never call the band noise or measurement error. It holds real day-to-day change as well as error.

Use these noise band formulas:

```text
Two single tests:                    1.96 × √2 × TE  ≈ 2.77 × TE
New value against a baseline mean:   1.96 × TE × √(1 + 1/n)
```

Read the formulas this way:

- `n` is the number of values in the baseline mean. With n = 1, the second form equals the first.
- The second form adds the variance of the new test to the variance of the baseline mean, whose error is TE / √n (Hopkins, 2000). Hopkins (2017) uses the same error for a change from the mean of several tests in his monitoring spreadsheet. The 95% level is a choice.
- The band means this: error alone gives a change smaller than the band about 95 percent of the time.

The band rests on these assumptions:

- The athlete's true score stays constant over the baseline and the new test.
- Errors are independent.
- TE is the same across athletes and across the range of values.
- TE is known.

Choose the multiplier this way:

- Use z = 1.96 for 95% when TE comes from a large reliability study. Use 1.645 for 90%.
- When TE comes from few athletes, use t with the degrees of freedom of the TE study, not of the baseline. Use athletes − 1 for two trials, or (athletes − 1) × (trials − 1) for the two-way model. TE from 6 athletes gives t(5) = 2.57. TE from 10 athletes gives t(9) = 2.26 (Swinton et al., 2018).

Use 95% as the default confidence level when the user has no preference. That default is a choice that matches common MDC95 reporting, not a published rule for monitoring. Hopkins (2000) suggests an observed change of about 1.5 to 2.0 × TE as a practical threshold. Offer it with its cost: for two single tests and pure noise, 1.5 × TE flags 28.9% of changes (14.4% in one direction), and 2.0 × TE flags 15.7% (7.9%), against 5% at 2.77 × TE.

Apply the SWC interval rule to decide whether a change is worthwhile:

- A change is clearly beyond the SWC only when its interval lies beyond the SWC in the chosen direction (Swinton et al., 2018). Put another way, the change minus the noise band is still beyond the SWC.
- Batterham and Hopkins (2006) describe a related probability method. The interval rule comes from Swinton et al. (2018).
- A change beyond the noise band but not clearly beyond the SWC reads: "larger than measurement error; may or may not be worthwhile".

Know the false-flag rates:

- With all assumptions met, about 5% of pure-noise changes cross the band in either direction, or 2.5% when only one direction matters, such as a drop.
- When the assumptions fail, the real rate can be higher or lower than 5%. It is higher when TE is too small, comes from few athletes, or varies between athletes. It can be lower when TE is overestimated or errors are positively correlated over time. Never call 5% a lower bound.
- With TE from 6 athletes and 1.96, about 10.7% of pure-noise changes cross the band. With t(5), the rate is 5.0%.
- A TE overestimated by 20% gives 1.87% for two single tests. Error correlation of 0.5 between consecutive tests gives 0.56% for two single tests, or 4.38% against a baseline of 8.

Report flags expected across a squad:

- Expected flags = number of results × 5%, or × 2.5% for one direction.
- For 25 athletes checked for drops, 0.625 false flags are expected each week, and the chance of at least one is 46.9%.
- Flags in consecutive weeks against the same baseline are not independent.
- Recommend a repeat test before anyone acts on a single flag. A flagged value was picked for being extreme, and regression to the mean makes the next value likely to sit closer to the athlete's usual level (Barnett et al., 2005).

### Typical error

**What it measures.** Typical error (TE) is the noise in a test: how much one athlete's score moves between repeated tests when nothing real has changed (Hopkins, 2000). It is also called the standard error of measurement (SEM). Both names mean the standard deviation of one athlete's repeated measurements (Hopkins, 2000; Weir, 2005).

**Inputs.** The calculation needs these data:

- One row per athlete with `athlete_id`, `trial1`, and `trial2`, both in the units of the measure
- Repeated tests of the same athletes with the same protocol, device, and time of day, close enough together that no true change is expected
- The same trial summary you compare in monitoring: a single trial, the best of 3, or the mean of 3

**Calculation.** Use the difference-score method for two trials. This is the default:

```text
diff_i = trial2_i − trial1_i
TE     = SD(diff) / √2
CV%    = 100 × TE / grand mean
```

The terms mean the following:

- `diff_i`: the change for athlete `i` between trial 1 and trial 2, in the units of the measure
- `SD(diff)`: the sample standard deviation of the difference scores across athletes
- `√2`: the square root of 2. Each difference holds the error of two tests, so its variance is 2 × TE² (Hopkins, 2000; Swinton et al., 2018).
- `TE`: typical error, in the units of the measure
- `grand mean`: the mean of all values from both trials
- `CV%`: the coefficient of variation, which is TE as a percent of the mean (Hopkins, 2000; Swinton et al., 2018)

Follow these steps from raw inputs:

1. Drop any athlete who is missing either trial.
2. Compute `diff = trial2 − trial1` for each athlete.
3. Compute the mean of `diff`, and report it as the bias, the systematic change between trials.
4. Compute the sample SD of `diff`, dividing by n − 1.
5. Divide that SD by √2, about 1.4142, to get TE.
6. Compute the grand mean of all `trial1` and `trial2` values.
7. Compute `CV% = 100 × TE / grand mean`.
8. Optional: Repeat steps 2 to 5 on `100 × ln(trial)` to get `TE_log`, then convert with `CV% = 100 × (exp(TE_log / 100) − 1)`.

**Worked example.** Six athletes did a countermovement jump (CMJ) on two days, 2 days apart, with the same protocol and time of day and no change in training:

| Athlete | Trial 1 (cm) | Trial 2 (cm) | Difference (cm) |
|---|---|---|---|
| 1 | 38.2 | 39.0 | 0.8 |
| 2 | 41.5 | 40.8 | −0.7 |
| 3 | 35.0 | 36.1 | 1.1 |
| 4 | 44.1 | 44.9 | 0.8 |
| 5 | 39.7 | 38.9 | −0.8 |
| 6 | 36.8 | 37.9 | 1.1 |

The calculation gives these values:

- Bias: 2.3 / 6 = 0.383 cm
- Sum of squared deviations from the mean difference: 3.9483 cm²
- Sample SD of differences: √(3.9483 / 5) = 0.8886 cm
- TE: 0.8886 / 1.4142 = 0.6284 cm
- Grand mean of all 12 values: 39.4083 cm
- CV%: 100 × 0.6284 / 39.4083 = 1.59%
- Log method: the SD of `100 × ln` differences divided by √2 is 1.6268, so CV% = 100 × (exp(0.016268) − 1) = 1.64%

Result: TE = 0.63 cm, or 1.6% of the mean, from 6 athletes and 2 trials. Report the bias of 0.38 cm separately.

**Variants.** Use these variants when they fit the data:

- Log variant for CV%: use it when athletes with larger values show larger errors. Compute TE on `100 × ln(value)`. That TE is close to the CV% when it is under 5%. When it is larger, convert with the formula in step 8 (Hopkins, 2000; Atkinson & Nevill, 1998).
- Two-way model, three or more trials: `TE = √MSE`, the square root of the error mean square from a model with athletes and trials as effects. This is the preferred method (Hopkins, 2000; Weir, 2005).
- Pooled within-athlete SD, three or more trials: average each athlete's variance across trials, then take the square root. It counts changes in the trial means as error, so it reads high when there is learning. Average the variances, not the SDs (Hopkins, 2000).
- Consecutive pairs, three or more trials: compute TE for trials 1 and 2, trials 2 and 3, and so on, to check whether TE settles after practice trials (Hopkins, 2000).
- From a published intraclass correlation (ICC): `SEM = SD × √(1 − ICC)`, where `SD` is the SD of all scores. It is modestly affected by how varied the sample is. Prefer `√MSE` or the difference-score method (Weir, 2005).

**What changes the number.** These choices change TE when the athletes' true ability does not change:

- Population SD instead of sample SD: `STDEV.P` gives an SD of 0.8112 cm and a TE of 0.5736 cm, 8.7% smaller than the correct 0.6284 cm.
- Leaving out √2: reporting the SD of differences, 0.8886 cm, as TE is 41% too large.
- CV% denominator: dividing by the trial 1 mean gives 1.60% instead of 1.59%. The gap grows when the bias is large.
- Log transform: the log method gives 1.64% against 1.59% from the raw method. Use one method and name it.
- Time between tests: tests weeks apart let real change into the differences, which inflates TE.
- Same-day or separate-day retest: a separate-day retest gives a larger TE. This is a practice choice, not a published rule.
- Summary of trials: a TE for single trials does not fit values that are the best of 3 or the mean of 3.
- Method for 3 trials: with a third trial of 38.7, 41.6, 35.5, 44.3, 39.6, and 37.2 cm, the two-way `√MSE` is 0.4687 cm and the pooled within-athlete SD is 0.4708 cm. Averaging SDs gives 0.4666 cm. Consecutive pairs give 0.6284 cm for trials 1 and 2 and 0.4846 cm for trials 2 and 3, which suggests a practice effect in trial 1.
- Learning trials: a first, unfamiliar trial adds a systematic shift. Drop early trials that show learning (Weir, 2005).
- Who is in the sample: noise can differ between groups, such as junior and senior athletes. Compute TE separately when residuals differ between groups (Hopkins, 2000).

**Units and typical range.** TE has the units of the measure. CV% is a percent. The file gives no typical range, because TE depends on the test, the protocol, the device, and the athletes. Take it from your own test-retest data, or from a published reliability study that used the same protocol on similar athletes (Swinton et al., 2018). About 50 athletes and at least 3 trials give a reasonably precise estimate (Hopkins, 2000). Report the number of athletes and trials with the result.

**Vendor equivalents.** None.

**Reference file.** [typical-error.md](../skills/monitoring-statistics/references/typical-error.md)

### Smallest worthwhile change

**What it measures.** The smallest worthwhile change (SWC) is the smallest change in a measure that matters in practice. It answers "is this change big enough to care about?", not "is this change real?" (Swinton et al., 2018). To judge one athlete's change, compare it with both the noise and the SWC (Buchheit, 2014).

**Inputs.** The calculation needs these data:

- One baseline value per athlete for the same test and protocol, in a column such as `baseline_value`
- A comparison group of athletes like the athlete you judge, such as the same sex, level, and position group
- Each athlete's new value, in the same units
- The test's TE, in the same units

**Calculation.** Use the between-athlete variant by default, and build an interval around each change:

```text
SWC      = 0.2 × SD_between
interval = change ± z × √2 × TE          (two single tests)
interval = change ± z × TE × √(1 + 1/n)  (a new value against a baseline mean of n values)
```

The terms mean the following:

- `SD_between`: the sample SD of the measure across athletes in the group at baseline (Swinton et al., 2018)
- `0.2`: the threshold for a small standardized effect (Hopkins, 2000; Hopkins et al., 2009)
- `SWC`: the smallest worthwhile change, in the units of the measure
- `change`: new value minus baseline value
- `TE`: typical error of the test
- `z`: 1.96 for 95% confidence, or 1.645 for 90% confidence (Swinton et al., 2018; Weir, 2005)
- `n`: the number of values in the baseline mean. Use n = 1 when the baseline is one test.

Follow these steps from raw inputs:

1. Pick the baseline test date and the comparison group.
2. Collect one baseline value per athlete.
3. Compute the sample SD of `baseline_value`, dividing by n − 1.
4. Multiply the SD by 0.2 to get the SWC.
5. For each athlete, compute `change = new_value − baseline_value`.
6. Compute the half-width `z × √2 × TE`, or `z × TE × √(1 + 1/n)` for a baseline mean of n values.
7. Compute the interval from `change − half-width` to `change + half-width`.
8. Label the change with the first row of this table that fits.

| Interval result | Label |
|---|---|
| The interval includes zero. | Unclear: inside measurement noise. |
| The interval is entirely beyond the SWC, in one direction. | Real, and at least as large as the SWC. |
| The interval excludes zero but stays inside ±SWC. | Real, but smaller than the SWC. |
| The interval excludes zero and crosses the SWC. | Real, possibly as large as the SWC. |

**Worked example.** Eight athletes did a preseason CMJ of 36.4, 41.2, 38.9, 44.0, 35.1, 40.3, 42.7, and 37.6 cm. TE is 0.6284 cm, from the typical error example. The confidence level is the 95% default, z = 1.96. The SWC works out this way:

1. Baseline mean = 39.5250 cm.
2. Sample SD between athletes = 3.0927 cm.
3. SWC = 0.2 × 3.0927 = 0.6185 cm.
4. Half-width = 1.96 × 1.4142 × 0.6284 = 1.7418 cm.

Four athletes' changes get these labels:

| Athlete | Change (cm) | Interval (cm) | Label |
|---|---|---|---|
| A | −0.9 | −2.6418 to 0.8418 | Unclear: inside measurement noise |
| B | +2.6 | 0.8582 to 4.3418 | Real, and at least as large as the SWC |
| C | +2.1 | 0.3582 to 3.8418 | Real, possibly as large as the SWC |
| D | +1.3 | −0.4418 to 3.0418 | Unclear: inside measurement noise |

Athlete B is clearly larger than the SWC: 2.6 − 1.7418 = 0.8582 cm, still beyond 0.6185 cm. Athlete C is larger than measurement error, but 2.1 − 1.7418 = 0.3582 cm is not beyond the SWC. Athlete D's change of 1.3 cm is twice the SWC, but it sits inside the noise.

The TE came from 6 athletes, so t(5) = 2.5706 strictly applies. The half-width becomes 2.2845 cm. Athlete B's interval becomes 0.3155 to 4.8845 cm, "real, possibly as large as the SWC". Athlete C's interval becomes −0.1845 to 4.3845 cm, inside the noise.

**Variants.** Use these variants when they fit the question:

- Between-athlete variant, 0.2 × SD: for fitness tests, jump tests, strength tests, and most team monitoring. This is the default (Hopkins, 2000; Swinton et al., 2018).
- True-score variant: `SWC = 0.2 × √(SD_between² − TE²)` removes the measurement noise from the observed SD (Hopkins, 2000). It gives a slightly smaller SWC. Name it if you use it.
- Competition performance variant: for a top athlete's competition time or distance, 0.3 × the athlete's typical variation between competitions. On this scale, small, moderate, large, very large, and extremely large are 0.3, 0.9, 1.6, 2.5, and 4.0 × within-athlete variation (Hopkins et al., 2009). Use it only for real competition results.
- Practitioner variant: the coach sets the SWC from experience with similar athletes (Swinton et al., 2018). Record the value and who chose it.
- Larger thresholds: for moderate, large, very large, and extremely large changes, 0.6, 1.2, 2.0, and 4.0 × SD_between (Hopkins et al., 2009). Do not mix this scale with the competition scale.

Treat 0.2 × SD as a convention with these caveats:

- It depends on how alike the squad is. A more varied squad gives a larger SWC for the same test.
- It is imprecise in small squads, because an SD from a few athletes is itself uncertain. Report the number of athletes.
- The observed SD includes measurement error. The corrected SD is `√(SD² − TE²)`, which gives the true-score variant (Hopkins, 2000).

**What changes the number.** These choices change the result when the athletes do not change:

- Population SD instead of sample SD: `STDEV.P` gives an SD of 2.8930 cm and an SWC of 0.5786 cm instead of 0.6185 cm.
- Mixing populations: adding two higher-jumping athletes at 52.5 cm and 55.0 cm raises the SD to 6.6151 cm and the SWC to 1.3230 cm, more than double.
- True-score variant: 0.2 × √(3.0927² − 0.6284²) = 0.6056 cm.
- Confidence level: at 90%, the half-width shrinks from 1.7418 cm to 1.4619 cm. Athlete C's interval becomes 0.6381 to 3.5619 cm, labeled "real, and at least as large as the SWC".
- Baseline date: a baseline after a training block, or a different set of athletes, gives a different SD. Fix the baseline and state it.
- Which TE you use: a TE from a different protocol, or from tests weeks apart, changes every interval.

**Units and typical range.** The SWC has the units of the measure. If you work in percent, express both the change and the SWC in percent. The file gives no typical SWC values, because the SWC depends on how varied your group is. Compute it from your own baseline data and report the group it came from. No published minimum group size exists in the sources for the file.

**Vendor equivalents.** None.

**Reference file.** [smallest-worthwhile-change.md](../skills/monitoring-statistics/references/smallest-worthwhile-change.md)

### Minimal detectable change

**What it measures.** The minimal detectable change (MDC) is the smallest change in one athlete's score that is larger than measurement noise, at a stated confidence level (Weir, 2005; de Vet et al., 2006). Weir (2005) calls it the minimal difference. Other names are smallest detectable change and smallest real change (de Vet et al., 2006). The MDC shows detectability only. It does not show that a change is important (de Vet et al., 2006).

**Inputs.** The calculation needs these data:

- An SEM or TE for the test, from a short-term test-retest study with the same protocol
- The confidence level the user picks
- Two test results per athlete, from the columns that hold the old and new values

**Calculation.** Use the confidence level the user picks. If they have no preference, use MDC95 as the default and offer MDC90:

```text
MDC95 = SEM × 1.96 × √2
MDC90 = SEM × 1.645 × √2
MDCz  = SEM × z × √2
```

The terms mean the following:

- `SEM`: the standard error of measurement, in the units of the measure. With two trials, `SEM = SD(diff) / √2`, the same as typical error (Weir, 2005).
- `1.96`: the z value for a 95% confidence interval (Weir, 2005)
- `1.645`: the z value for a 90% confidence interval (Swinton et al., 2018)
- `√2`: a change involves two measurements, and each has error (Weir, 2005; de Vet et al., 2006)
- `MDC`: the minimal detectable change, in the units of the measure

Follow these steps from raw inputs:

1. Get the SEM for the test from a short-term test-retest study with the same protocol.
2. Pick the confidence level and its z value: 1.96 for 95%, the default, or 1.645 for 90%.
3. Multiply: `MDC = SEM × z × 1.4142`.
4. For each athlete, compute `change = new_value − old_value`.
5. Compare the size of the change with the MDC. A change larger than the MDC is larger than noise at that confidence level.
6. Report the MDC with its confidence level, the SEM source, and the units.

**Worked example.** The CMJ test has an SEM of 0.6284 cm, from the typical error example. One athlete jumped 40.3 cm last month and 41.9 cm today. The calculation runs this way:

1. SEM × √2 = 0.6284 × 1.4142 = 0.8887 cm.
2. MDC95 = 0.6284 × 1.96 × 1.4142 = 1.7418 cm.
3. MDC90 = 0.6284 × 1.645 × 1.4142 = 1.4619 cm.
4. Change = 41.9 − 40.3 = 1.6 cm.
5. 1.6 cm is larger than MDC90 but smaller than MDC95.

Result: at the default 95% level, the 1.6 cm change is inside the noise band. Report it as "not larger than measurement error at 95%". At 90%, the same change would count as larger than noise. Report the level with the result, and let the practitioner decide what to do with it.

**Variants.** Use these variants when they fit:

- MDC95: the common reporting standard (Weir, 2005; de Vet et al., 2006; Furlan & Sterr, 2018). It equals about 2.77 × SEM.
- MDC90: a less strict threshold. It equals about 2.33 × SEM.
- Practical threshold: Hopkins (2000) judges the 95% level too strict for monitoring one athlete and suggests about 1.5 to 2.0 × TE. The false-flag cost is in the shared rules.
- Against a baseline mean: `1.96 × SEM × √(1 + 1/n)`. This form adds variances, and Hopkins (2017) uses the same error. With n = 1 it equals MDC95.
- Regression-based version: Weir (2005) notes a more exact interval that uses the estimated true score and the standard error of prediction, `SEP = SD × √(1 − ICC²)`. Use it only if the user asks.
- Small TE study: replace 1.96 with t from the TE study's degrees of freedom. An SEM from 6 athletes gives t(5) = 2.57 (Swinton et al., 2018).

The MDC and the SWC answer different questions. The MDC asks whether the change is bigger than noise and is built from measurement error. The SWC asks whether the change is big enough to matter and is built from the spread between athletes. A change can exceed the MDC and still be too small to matter (de Vet et al., 2006). At the same confidence level, "the interval `change ± z × √2 × SEM` excludes zero" is the same test as "the size of the change is larger than the MDC".

**What changes the number.** These choices change the MDC when the athlete does not change:

- Confidence level: MDC95 is 1.7418 cm and MDC90 is 1.4619 cm. The same 1.6 cm change fails MDC95 and passes MDC90.
- Small TE study: the SEM of 0.6284 cm came from 6 athletes. With t(5) = 2.5706, the band is 2.5706 × 0.6284 × 1.4142 = 2.2845 cm, and the 1.6 cm change is still inside it.
- Baseline mean of n values: against a mean of 8 prior tests, the 95% band is 1.96 × 0.6284 × √(1 + 1/8) = 1.3064 cm.
- Practical threshold: 1.5 × TE and 2.0 × TE give 0.9426 cm and 1.2568 cm (Hopkins, 2000).
- Leaving out √2: `1.96 × SEM` gives 1.2317 cm, which is 29% too small and makes noise look like change.
- Which SEM: an SEM from a different protocol, from tests weeks apart, or from an ICC formula on a different group changes the MDC (Weir, 2005).
- Individual versus group: for the mean change of a group of 6, the 95% noise is `t × SEM × √2 / √n` = 2.5706 × 0.6284 × 1.4142 / 2.4495 = 0.9326 cm (Hopkins, 2000). Do not apply that to one athlete.

**Units and typical range.** The MDC has the units of the measure. If the SEM is a CV%, the MDC is a percent change. The file gives no typical MDC values, because the MDC depends on the test, the protocol, and the athletes. Compute it from your own reliability data or a published study that used the same protocol. Weir (2005) states there is no consensus on how many athletes give a stable SEM. Report the number of athletes and trials.

**Vendor equivalents.** None.

**Reference file.** [minimal-detectable-change.md](../skills/monitoring-statistics/references/minimal-detectable-change.md)

### Individual baselines and z-scores

**What it measures.** An individual baseline is an athlete's own normal for a measure, built from their prior values. A z-score says how far today's value sits from that normal, in units of the athlete's own usual variation. Using the athlete as their own control is the basis of single-athlete monitoring (Sands et al., 2019). A z-score says how unusual today is for this athlete. It does not say whether the change is larger than measurement error. For that, use the noise band with the test's TE.

**Inputs.** The calculation needs these data:

- A long table with one row per `athlete_id`, `date`, and value, such as `cmj_cm`, from one protocol
- A baseline window k and a minimum count of values, chosen by the user
- The test's TE, from test-retest data, for the noise band

**Calculation.** Use a rolling baseline of prior values only, by default:

```text
baseline_mean = mean of the athlete's previous k values (today excluded)
baseline_SD   = sample SD of the same k values
z             = (today − baseline_mean) / baseline_SD
noise band    = 1.96 × TE × √(1 + 1/n)
```

The terms mean the following:

- `today`: the athlete's value on the day you judge, in the units of the measure
- `k`: the baseline window, as a count of prior tests or a number of prior days. State it.
- `baseline_mean`: the mean of the window
- `baseline_SD`: the sample SD of the window, dividing by k − 1
- `z`: the z-score, with no units. A z of −2 means today is 2 of the athlete's usual SDs below their baseline mean.
- `TE`: the test's typical error
- `n`: the number of values in the baseline mean

Follow these steps from raw inputs:

1. Sort the rows by `athlete_id`, then by `date`.
2. Drop or mark rows from test days that broke protocol, as the user defines them. Do not fill missing values with zero.
3. For each row, take the previous k values for the same athlete. Do not include the row itself.
4. Count those values. If the count is below the minimum, leave the z-score blank and say why.
5. Compute the mean and the sample SD of the window.
6. If the SD is 0, leave the z-score blank and say why.
7. Compute `z = (today − baseline_mean) / baseline_SD`.
8. Compute the noise band from the test's TE, and compare the change from the baseline mean with it.
9. Report the z-score with the window k, the count n, the baseline mean, the baseline SD, and the units.

**Worked example.** One athlete did a CMJ every 3 days, from 2026-09-04 to 2026-09-25: 41.0, 39.8, 40.6, 40.9, 39.5, 40.3, 41.2, and 40.0 cm. Today, 2026-09-28, the athlete jumped 37.6 cm. Judge today against the 8 prior tests:

1. Sum of the 8 prior values = 323.30 cm, so the baseline mean = 40.4125 cm.
2. Sum of squared deviations = 2.6288 cm². Divide by 7 to get 0.3755 cm².
3. Baseline SD = √0.3755 = 0.6128 cm.
4. z = (37.6 − 40.4125) / 0.6128 = −4.59.
5. Change from the baseline mean = −2.8125 cm.
6. Noise band with TE = 0.6284 cm: 1.96 × 0.6284 × 1.0607 = 1.3064 cm.
7. The drop is beyond the band by 2.8125 − 1.3064 = 1.5061 cm. That is still beyond the SWC of 0.6185 cm.
8. The TE came from 6 athletes, so t(5) = 2.57 applies. The band becomes 2.5706 × 0.6284 × 1.0607 = 1.7133 cm. The drop is still beyond it by 1.0992 cm.

Result: today is 4.59 of the athlete's usual SDs below baseline (window 8 prior tests, n = 8, sample SD). The drop is larger than measurement error, and clearly larger than the SWC. Report it as a flag for the practitioner to review, not as a diagnosis.

**Variants.** Use these variants when they fit:

- Rolling window of tests: the previous k tests. Use it when tests are irregular, such as weekly jumps. This is the default.
- Rolling window of days: the previous k calendar days. Use it only for daily measures. Missing days shrink the real number of values, so report n.
- Fixed baseline: the mean and SD of a set period, such as the first weeks of preseason. It does not drift. State the dates.
- Control limits: Sands et al. (2019) show limits at 1.5 and 2.0 × the baseline SD around the baseline mean, equal to z = ±1.5 and z = ±2.0. They are examples from a published case, not validated thresholds. With an 8-value baseline and pure noise, |z| > 2 flags about 10.1% of tests and |z| > 1.5 flags about 20.0%.

**What changes the number.** These choices change the z-score for the same athlete on the same day:

- Including today in the baseline: the last 8 values with today included give a mean of 39.9875 cm, an SD of 1.1180 cm, and z = −2.14 instead of −4.59.
- Window length: with the 4 prior tests, z = −3.71. With 3 prior tests, z = −4.64. Short windows give unstable SDs.
- Population SD: `STDEV.P` gives an SD of 0.5732 cm and z = −4.91.
- Team SD instead of the athlete's SD: dividing by the between-athlete SD of 3.0927 cm gives z = −0.91. That answers a different question.
- Small n: Swinton et al. (2018) show that a 95% interval based on a TE from 5 individuals needs a multiplier of 2.78 instead of 1.96.
- Own SD in place of TE: the baseline SD also holds biological variation, so a band built on it is never a measurement-error band. With at least 10 stable values, it gives the usual-variation band, `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`, with two states only. Today is outside that band when |z| > t(n − 1) × √(1 + 1/n), which is 2.37 for 10 values. With fewer than 10 values, do not build that band. See [Shared rules for judging change](#shared-rules-for-judging-change).
- Trend in the baseline: a baseline should be stable, with low variability and no clear trend (Sands et al., 2019). In a 28-test example that falls 0.1 cm per test from test 9, the rolling z never reaches −2; its lowest value is −1.91. Before test 28, the rolling mean has drifted to 38.4500 cm, with an SD of 0.4440 cm. Against the fixed baseline of tests 1 to 8 (mean 40.0000 cm), test 28 is 2.4000 cm lower, beyond the noise band of 1.3064 cm. Pair a rolling baseline with a fixed reference period or a trend line.
- Mixed conditions: a baseline that spans preseason and in-season, or an illness period, changes both the mean and the SD.

**Units and typical range.** The z-score has no units. The baseline mean and SD have the units of the measure. The file gives no typical z-score range or flag threshold. Thresholds are choices, not facts. Name the threshold and its source. No source used in the file sets a minimum number of values or a best window for an individual baseline. Weir (2005) states there is no consensus on the sample size needed for a stable SEM. Report n with every z-score.

**Vendor equivalents.** One device file maps a z-score status:

- Perch Readiness: compares the most recent jump session with the previous session and the 30-day average, then gives a z-score status. Green is above 1. Yellow is between −1 and −2. Red is −2 or below. The published bands leave −1 to 1 unassigned. The Perch file maps it to no reference file and gives no SD source.

**Reference file.** [individual-baselines-z-scores.md](../skills/monitoring-statistics/references/individual-baselines-z-scores.md)

### Group p-values for individual athletes

**What it measures.** A p-value is the probability of data at least this extreme if there were no true effect and the model's assumptions hold (Wasserstein & Lazar, 2016). A group p-value does not tell you whether one athlete's change is real or important. It does not measure the size of an effect or its importance (Wasserstein & Lazar, 2016). A group can improve on average while some athletes get worse: Sands et al. (2019) show a group with p = 0.048 in which the three best jumpers declined.

**Inputs.** The individual view needs these data:

- One change score per athlete, in the units of the measure
- The test's TE and SWC, in the same units

**Calculation.** The file reports a paired t-test and gives no p-value formula. It sets out the individual view to report first, with this noise band for two single tests:

```text
noise band = 1.96 × √2 × TE
```

Follow these steps when the user asks whether a group change was "significant":

1. Report the group mean change with its units.
2. Label each athlete's change against TE and the SWC, with the interval rule from the SWC breakdown.
3. Report how many athletes improved, declined, or stayed inside the noise.
4. If you report a p-value, put it after the individual results, with the sample size.

**Worked example.** Ten athletes did a CMJ before and after a training block, with TE = 0.6284 cm and SWC = 0.6185 cm:

| Input | Value |
|---|---|
| Changes (cm) | +2.2, −0.3, +1.9, −0.8, +2.3, +0.7, −0.8, +2.3, +0.7, −0.5 |
| Mean change | 0.77 cm, SD of changes 1.3208 cm |
| Paired t-test, n = 10 | t = 1.8435, p = 0.0984 |

The individual view at the 95% default uses a noise band of 1.96 × √2 × 0.6284 = 1.7418 cm:

1. Four athletes (+2.2, +1.9, +2.3, +2.3) changed by more than measurement error.
2. None of the four is clearly larger than the SWC. For the largest, 2.3 − 1.7418 = 0.5582 cm, which is not beyond 0.6185 cm.
3. Six athletes are inside the noise. Four of the 10 changes are negative.
4. With t(5) = 2.5706, the band becomes 2.2845 cm, and only the two +2.3 cm changes stay beyond it.

A squad of 40 with the same 10 changes four times has the same mean change of 0.77 cm, but p = 0.000444. Result: the p-value moved with the sample size. It said nothing about which athletes changed.

**Variants.** The file gives no variants.

**What changes the number.** These choices change a p-value when the effect does not change:

- Sample size: the same changes gave p = 0.0984 at n = 10 and p = 0.000444 at n = 40.
- Measurement noise: more noise widens the spread of changes and raises p, for the same true effect (Batterham & Hopkins, 2006).

**Units and typical range.** A p-value is a probability between 0 and 1. Decisions should not rest only on whether p passes a threshold (Wasserstein & Lazar, 2016). Do not run a t-test on one athlete's daily values to call a change "significant". Use typical error, the MDC, and the SWC instead.

**Vendor equivalents.** None.

**Reference file.** [misleading-methods.md](../skills/monitoring-statistics/references/misleading-methods.md)

## Load and wellness

These metrics describe internal load, how recent load compares with longer-term load, and how a wellness answer compares with the athlete's own usual answers.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Session RPE load | `session_rpe_load_au = rpe_cr10 × duration_min` | AU | [session-rpe-load.md](../skills/load-and-wellness/references/session-rpe-load.md) |
| Daily and weekly session RPE load | Sum of session loads in a day; sum of daily loads in a week | AU | [session-rpe-load.md](../skills/load-and-wellness/references/session-rpe-load.md) |
| %HRmax and %HRR | `%HRmax = HR ÷ HRmax × 100`, `%HRR = (HR − HRrest) ÷ (HRmax − HRrest) × 100` | % | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Edwards TRIMP | `(min in zone 1 × 1) + (min in zone 2 × 2) + (min in zone 3 × 3) + (min in zone 4 × 4) + (min in zone 5 × 5)` | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Banister TRIMP | `duration_min × x × 0.64 × e^(1.92 × x)` (male weighting) or `duration_min × x × 0.86 × e^(1.67 × x)` (female weighting) | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Lucia TRIMP | `(min below VT × 1) + (min from VT to RCP × 2) + (min above RCP × 3)` | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| ACWR, rolling coupled | Mean daily load, last 7 days ÷ mean daily load, last 28 days | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| ACWR, rolling uncoupled | Mean daily load, last 7 days ÷ mean daily load, days 8 to 28 back | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| ACWR, EWMA | EWMA with N = 7 ÷ EWMA with N = 28, with λ = 2 ÷ (N + 1) | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| Wellness z-score | `z = (x_today − baseline_mean) ÷ baseline_sd` | No unit (SD units) | [wellness-z-score.md](../skills/load-and-wellness/references/wellness-z-score.md) |

### Session RPE load

**What it measures.** Session RPE load estimates how hard a whole session was for the athlete, by multiplying their effort rating by the session length (Foster et al., 2001). It is a measure of internal load, the athlete's response to the work. External load is the work itself, such as distance run (Impellizzeri et al., 2019). Session RPE load does not replace external load, and external load does not replace it.

**Inputs.** The calculation needs these columns:

- One row per athlete per session with `athlete_id`, `date`, `session`, `rpe_cr10` (0 to 10, no unit), and `duration_min` (minutes)
- One `availability` value per athlete per day, such as `full`, `modified`, or `out`

**Calculation.** Use the session RPE method from Foster et al. (2001):

```text
session_rpe_load_au = rpe_cr10 × duration_min
```

The terms mean the following:

- `rpe_cr10`: the athlete's rating of the whole session on the 0 to 10 category ratio scale (CR-10), where 0 is rest and 10 is maximal. No unit.
- `duration_min`: the session length in minutes (Foster et al., 2001; Impellizzeri et al., 2004)
- `session_rpe_load_au`: the result, in arbitrary units (AU) (Haddad et al., 2017). AU is not a physical unit. Compare AU only for the same athlete, scale, and method.

Collect the rating about 30 minutes after the session ends, so a very hard or very easy final drill does not dominate it (Foster et al., 2001). Keep the delay the same every day.

Follow these steps from raw inputs:

1. Confirm every `rpe_cr10` value is between 0 and 10. Ask the user about any value above 10 before you call it an error. It may come from a CR100 form.
2. Convert any duration in hours or `hh:mm` text to minutes.
3. Multiply `rpe_cr10` by `duration_min` for each session, and store it in `srpe_load_au`. Keep the result missing if either input is missing.
4. Add `srpe_load_au` across sessions for each `athlete_id` and `date` to get daily load. If any session that day has a missing rating, mark the day as missing.
5. Add daily loads across each calendar week, Monday to Sunday unless the user names another start day, to get weekly load. Do this even when the user asked only for daily load. Report how many days had complete data and how many were marked injured, ill, or modified. Mark a week with any missing day as incomplete, and give its total with the number of days it covers, such as 6 of 7 days.

**Worked example.** One athlete trains three days. Monday, 2026-08-03, has a practice and a lift:

| Date | Session | `rpe_cr10` | `duration_min` | Load (AU) |
|---|---|---|---|---|
| 2026-08-03 | Practice | 6 | 75 | 6 × 75 = 450 |
| 2026-08-03 | Lift | 4 | 45 | 4 × 45 = 180 |
| 2026-08-04 | Practice | 7 | 90 | 7 × 90 = 630 |
| 2026-08-05 | Practice | 5 | 60 | 5 × 60 = 300 |

The daily loads are 450 + 180 = 630 AU, 630 AU, and 300 AU. The three-day total is 1,560 AU. The wrong method averages Monday's RPE and multiplies by Monday's total minutes: 5 × 120 = 600 AU, which is 30 AU short of the correct 630 AU.

**Variants.** Check which rating scale the form used:

- CR-10: the scale the file assumes. Ratings run from 0 to 10.
- Borg CR100, also called centiMax (Borg & Kaijser, 2006): a category ratio scale with a wider number range. It is valid for session RPE in soccer and can be used interchangeably with CR-10 (Fanchini et al., 2016). Do not mix CR100 and CR-10 loads in one series without a conversion the user names.
- Ratings above 10 on a CR-10 form: treat the claim that CR-10 allows them as unverified. Ask the user before you call one an error.
- The 6 to 20 RPE scale: a different scale (Borg, 1982). Its product with minutes is not session RPE load.

For more than one session in a day, calculate each session's load, then add them. Record a day with no activity as `0` AU, with the reason in `availability`. Keep a day with activity but no rating as missing.

**What changes the number.** These choices change the result when the athlete's effort does not change:

- Duration definition: adding a 15-minute warm-up to Monday's practice changes it from 450 AU to 6 × 90 = 540 AU. No consensus says whether duration includes the warm-up or the cool-down. Use one rule for every session, and record it. If the user has no rule, the file offers this default, labeled as its own choice: training time from the start of the team warm-up to the end of the last drill, without a separate cool-down. Pustina et al. (2017) used that rule for training. For matches, ask whether to use minutes played. In one study of college soccer, match loads from minutes played matched GPS distance more closely than loads from the whole match period: r = 0.81 against 0.57 (Pustina et al., 2017). The cool-down can change the rating itself, not only the minutes (Rodríguez-Marroyo et al., 2021).
- Duration unit: entering Monday's practice as 1.25 hours gives 6 × 1.25 = 7.5 AU instead of 450 AU.
- Rating timing: if an immediate rating changed Monday's 6 to a 7, the practice would read 7 × 75 = 525 AU (Foster et al., 2001).
- Rating scale: a 6 to 20 rating or a CR100 rating is on a different range from a CR-10 rating. Name the scale with every load.
- Splitting or merging sessions: rating a practice and a lift separately gives a different number from one rating of the whole day.
- How the question is asked: use the same scale, labels, and wording every time. Haddad et al. (2017) list many factors that can alter RPE.

**Units and typical range.** Session RPE load is in AU. It has no population range that applies across sports, ages, and training phases. Compare each athlete with their own history. For any CR-10 session, the possible range is 0 to 10 × `duration_min` AU (Foster et al., 2001, scale bounds). Haddad et al. (2017) give an example: an 87-minute session at RPE 4 gives 87 × 4 = 348 AU.

**Vendor equivalents.** None. The Perch file lists `RPE` as an exercise variable, with units not published, but maps it to no reference file.

**Reference file.** [session-rpe-load.md](../skills/load-and-wellness/references/session-rpe-load.md)

### Heart rate load

**What it measures.** Heart rate load estimates the cardiovascular response to a session by combining time with heart rate intensity. It is a measure of internal load. It describes the response to one session. It does not diagnose illness or overtraining, and it does not predict injury or performance. Heart rate load and session RPE load agree in direction but not in size. Do not convert one into the other.

**Inputs.** The calculation needs these data:

- One row per heart rate sample with `athlete_id`, `session_id`, `timestamp`, and `hr_bpm`
- Each athlete's maximal heart rate (HRmax), with how it was set: a maximal test, a peak from a maximal field test, or an age formula
- Each athlete's resting heart rate (HRrest), with how it was measured
- For Lucia TRIMP, the heart rate at the ventilatory threshold (VT) and the respiratory compensation point (RCP) from a lab ramp test
- For Banister TRIMP, the weighting the user names for each athlete. Never infer it from a name or roster data.

**Calculation.** Express intensity as %HRmax or %HRR, then apply a TRIMP (training impulse) method. Name the method, the HRmax source, and the HRrest value with every result:

```text
%HRmax = HR ÷ HRmax × 100
%HRR   = (HR − HRrest) ÷ (HRmax − HRrest) × 100

TRIMP_Edwards  = (min in zone 1 × 1) + (min in zone 2 × 2) + (min in zone 3 × 3)
               + (min in zone 4 × 4) + (min in zone 5 × 5)

x = (HR_mean − HRrest) ÷ (HRmax − HRrest)
Male weighting:    TRIMP_Banister = duration_min × x × 0.64 × e^(1.92 × x)
Female weighting:  TRIMP_Banister = duration_min × x × 0.86 × e^(1.67 × x)

TRIMP_Lucia = (min below VT × 1) + (min from VT to RCP × 2) + (min above RCP × 3)
```

The Edwards zones use %HRmax (Edwards, 1993, as described by Paulson et al., 2015 and Hourcade et al., 2018):

| Zone | % HRmax | Weight in Edwards TRIMP |
|---|---|---|
| Below zone 1 | Below 50 % | 0 |
| 1 | 50 to 60 % | 1 |
| 2 | 60 to 70 % | 2 |
| 3 | 70 to 80 % | 3 |
| 4 | 80 to 90 % | 4 |
| 5 | 90 to 100 % | 5 |

The terms mean the following:

- `HRmax`, `HRrest`: maximal and resting heart rate, in bpm. Heart rate reserve (HRR) is HRmax − HRrest.
- Zone boundary rule: include the lower bound and exclude the upper bound, on the unrounded %HRmax. A value of exactly 60.0 % counts in zone 2. Values at or above 100 % HRmax count in zone 5. Use the same rule for Lucia zones. Neither Edwards nor Lucia et al. (2003) say which zone gets a value on a boundary. The rule matches the Polar Team Pro API. It is a practice convention, not a published part of either method.
- `x`: the delta heart rate ratio, %HRR as a fraction, from 0 at rest to 1 at HRmax (Banister et al., 1992)
- `HR_mean`: the mean heart rate of the session (Paulson et al., 2015; Hourcade et al., 2018)
- `duration_min`: session length in minutes
- `0.64 × e^(1.92 × x)` and `0.86 × e^(1.67 × x)`: weighting factors that give more credit to high-intensity time, based on the exponential rise of blood lactate with intensity (Banister et al., 1992). Banister (1991) prints both multiplier forms. The female form appears earlier, in Banister and Hamilton (1985). Use this multiplier form by default, and name it with every result.
- `e`: the base of natural logarithms, about 2.718
- `VT`, `RCP`: the heart rates at the first and second breathing thresholds in a lab ramp test (Lucia et al., 2003). The multipliers 1, 2, and 3 are reported by Paulson et al. (2015).

Follow these steps from raw inputs:

1. Find the sampling interval from the timestamps, in seconds.
2. Find gaps, where timestamps jump or `hr_bpm` is 0 or blank. Remove those samples. Do not count them as 0 bpm.
3. Find artifacts the user or device flags. Remove them only with the user's agreement, and report how many there were.
4. Keep plausible values above HRmax. If HRmax is age-predicted, tell the user the setting is probably too low.
5. Calculate time in each zone in minutes: count samples in the zone, multiply by the sampling interval, and divide by 60.
6. Calculate the TRIMP the user asked for, in AU.
7. Report recorded minutes next to planned session minutes.
8. Report the method, the zone boundaries and boundary rule, HRmax and its source, HRrest, and the weighting with each result.

**Worked example.** One synthetic 20-minute interval session, recorded at 1 Hz (1,200 samples), for an athlete aged 20:

| Input | Value |
|---|---|
| Session | 3 min at 110 bpm, 3 min at 140 bpm, then 2 min at 180 bpm and 2 min at 150 bpm, three times, then 2 min at 120 bpm |
| Mean heart rate | 148.50 bpm |
| Measured HRmax | 205 bpm |
| Age-predicted HRmax | 194 bpm (208 − 0.7 × age), 200 bpm (220 − age) |
| HRrest | 55 bpm |
| Lab heart rate at VT and RCP | 160 bpm and 178 bpm |

Time in zone differs with the HRmax:

| Zone | Minutes, measured HRmax 205 bpm | Minutes, predicted HRmax 194 bpm |
|---|---|---|
| Below 50 % | 0 | 0 |
| 1 | 5 | 3 |
| 2 | 3 | 2 |
| 3 | 6 | 9 |
| 4 | 6 | 0 |
| 5 | 0 | 6 |

The TRIMP methods give these results:

- Edwards, measured HRmax: 5 × 1 + 3 × 2 + 6 × 3 + 6 × 4 = 53.0 AU.
- Edwards, predicted HRmax 194 bpm: 3 × 1 + 2 × 2 + 9 × 3 + 0 × 4 + 6 × 5 = 64.0 AU.
- Edwards, predicted HRmax 200 bpm: 120, 140, and 180 bpm sit exactly on boundaries. The result is 64.0 AU with boundaries in the higher zone and 53.0 AU with boundaries in the lower zone.
- Banister, measured HRmax: x = (148.5 − 55) ÷ (205 − 55) = 0.6233. Male weighting 0.64 × e^(1.92 × 0.6233) = 2.1181, so TRIMP = 20 × 0.6233 × 2.1181 = 26.4 AU. Female weighting 2.4355, so TRIMP = 30.4 AU.
- Banister, predicted HRmax 194 bpm: x = 0.6727, giving 31.3 AU male and 35.6 AU female. At 200 bpm, x = 0.6448, giving 28.5 AU and 32.6 AU.
- Lucia: 14 min below VT and 6 min above RCP, so 14 × 1 + 0 × 2 + 6 × 3 = 32.0 AU. HRmax does not change it.

Mean %HRmax is 72.4 % with the measured HRmax and 76.5 % with 194 bpm. An HRmax 11 bpm too low raises every HRmax-based result. A steady 20-minute session at the same mean of 148.5 bpm gives the same Banister TRIMP, 26.4 AU male and 30.4 AU female, but 60.0 AU Edwards and 20.0 AU Lucia. Banister TRIMP from the mean cannot tell the two sessions apart. Time in zone can.

**Variants.** Know these variants before you compare numbers:

- %HRR, the Karvonen method (Karvonen et al., 1957): %HRR tracks the percentage of oxygen uptake reserve more closely than the percentage of maximal oxygen uptake (Swain et al., 1998). The same heart rate gives a different percentage under each method, so never mix them in one report. Edwards defined his zones on %HRmax.
- HRmax source: use a measured HRmax when one exists. Without a maximal test, label the highest artifact-checked value from a maximal intermittent field test as HRpeak, with the test name and date. In the Yo-Yo intermittent recovery level 1 test, peak heart rate in 17 men was 187 ± 2 bpm, against 189 ± 2 bpm on a treadmill to exhaustion (Krustrup et al., 2003). In the level 2 test, heart rate at exhaustion was 98 ± 1 % of HRmax in 13 men (Krustrup et al., 2006). In 20 team sport players, heart rate at exhaustion did not differ between the 30-15 Intermittent Fitness Test and a continuous incremental test (Buchheit et al., 2009). Take HRpeak as the highest 5-second rolling average of artifact-checked samples, as Paulson et al. (2015) did in a lab test. This window is a practice default of the file, not a published rule. State it with the result.
- Age-predicted HRmax: 220 − age underestimates HRmax in older adults (Tanaka et al., 2001). 208 − 0.7 × age comes from Tanaka et al. (2001). 211 − 0.64 × age had a standard error of the estimate (SEE) of 10.8 bpm in 3,320 healthy adults (Nes et al., 2013).
- Banister exponent-only form: the appendix of Banister et al. (1992) prints e^(1.92 × x) and e^(1.67 × x) without the 0.64 and 0.86 multipliers. Banister's 1985 and 1991 texts include the multipliers. The exponent-only form gives larger numbers and reverses which sex scores higher. Ask which form a tool uses.
- Banister phase-sum or per-sample form: Banister scored each phase of a session from its duration and mean heart rate, then added the phases (Banister & Hamilton, 1985; Banister, 1991). Applying the formula to each sample and adding the results is the same rule with one-sample phases. Polar computes its Banister TRIMP each second and adds the results (Polar, 2025). It gives a larger number than the mean form whenever heart rate varies. Use the session mean by default. It is the form used in the validation papers checked for the file (Paulson et al., 2015; Hourcade et al., 2018; Tomoto et al., 2026). The whole-session mean comes from these later papers, not from Banister. It treats the whole session as one phase, so it cannot see intervals. Offer the phase-sum or per-sample form as a labeled option. Never mix the two in one athlete's history.
- Individualized TRIMP (iTRIMP): a weighting built from each athlete's own heart rate and blood lactate profile (Manzi et al., 2009). Use it only when each athlete has a lactate test.
- Mean heart rate and mean %HRmax: simple summaries that hide how intensity was spread. Hourcade et al. (2018) found the summated zone load differed between two sessions with almost equal mean heart rate (p = 0.007), while Banister TRIMP did not (p = 0.420). Report time in zone next to any mean.

The published Banister weightings are male and female only. They come from blood lactate curves in trained male and female subjects (Banister, 1991). No published guidance was found for athletes outside those categories. For those athletes, prefer Edwards, Lucia, or iTRIMP. At a delta heart rate ratio from 0.3 to 1.0, the female weighting gives 5 to 25 % more load than the male weighting.

**What changes the number.** These choices change the result when the athlete's effort does not change. Figures use the measured HRmax and the male weighting unless stated:

- HRmax source: an age formula 11 bpm low raised Edwards TRIMP from 53.0 to 64.0 AU and Banister TRIMP from 26.4 to 31.3 AU.
- HRrest: Banister TRIMP was 28.7 AU at 45 bpm, 26.4 AU at 55 bpm, and 24.0 AU at 65 bpm.
- Boundary rule: at HRmax 200 bpm, the rule alone moved Edwards TRIMP from 53.0 to 64.0 AU, a 20.8 % swing.
- Banister form: the exponent-only form scored 41.3 AU male and 35.3 AU female, so the sex ordering reverses.
- Mean or per-sample: the per-sample form gave 30.0 AU male and 33.8 AU female.
- Dropouts: a 60-second dropout at 180 bpm recorded as 0 bpm cut mean heart rate from 148.50 to 139.50 bpm and Banister TRIMP from 26.4 to 21.3 AU. Removing it instead gave 19 min, 146.84 bpm, and 24.1 AU. Edwards TRIMP fell to 49.0 AU either way. Lucia TRIMP fell to 30.0 AU with zeros and 29.0 AU with removal. A chest strap agreed best with an electrocardiogram (Gillinov et al., 2017).
- Artifact spikes: a false 15-second spike to 230 bpm raised Edwards TRIMP from 53.0 to 53.5 AU and per-sample Banister TRIMP from 30.0 to 31.4 AU.
- Sampling and averaging: with 30-second transitions, Edwards TRIMP was 53.4 AU at 1 s, 53.3 AU from 5 s averages, and 54.0 AU from 60 s averages. Lucia TRIMP was 31.2, 31.1, and 29.0 AU.
- Cardiovascular drift: heart rate rises during prolonged exercise (Coyle & González-Alonso, 2001; Achten & Jeukendrup, 2003). An illustrative drift of 0.5 bpm per minute raised Edwards TRIMP from 53.0 to 59.0 AU and Banister TRIMP from 26.4 to 29.7 AU.
- Heat and hydration: dehydration and air temperature can change the relationship between heart rate and oxygen uptake a great deal (Achten & Jeukendrup, 2003).
- Caffeine: 3 to 6 mg per kg body mass did not change heart rate during submaximal exercise but lowered RPE (Glaister & Gissane, 2018).
- Illness and fever: 24-hour heart rate rose by about 8.5 bpm for each 1 °C in 27 young men with an acute febrile infection (Karjalainen & Viitasalo, 1986). Do not infer illness from heart rate. Refer health questions to medical staff.
- Day-to-day variation: heart rate shows a small day-to-day variability (Achten & Jeukendrup, 2003). Do not call a change real without a typical error.

**Units and typical range.** Time in zone is in minutes. TRIMP is in AU. No population range for TRIMP applies across sports, session lengths, and methods. Compare each athlete with their own history on the same method and settings. The file gives these bounds:

| Population | Typical range | Source |
|---|---|---|
| Any session, Edwards TRIMP | 0 to 5 × `duration_min` AU | Arithmetic of the formula (Paulson et al., 2015) |
| Any session, Lucia TRIMP | 1 to 3 × `duration_min` AU | Arithmetic of the formula (Paulson et al., 2015) |
| Any session, Banister TRIMP with 0.64 or 0.86 multiplier | 0 to 4.365 × `duration_min` AU (male), 0 to 4.568 × `duration_min` AU (female), at x = 1 | Arithmetic of the formula |
| Healthy adults, age-predicted HRmax | SEE 10.8 bpm around 211 − 0.64 × age | Nes et al., 2013 |

The file gives no typical error for session TRIMP. Do not call a change between sessions real unless the user supplies a TE and the change exceeds the noise band, 1.96 × √2 × TE, about 2.77 × TE.

**Vendor equivalents.** The device files map these metrics:

- Polar `heart_rate_zones` and Time in HR zone: five bands of the player's own HRmax, with defaults of 50 to 60, 60 to 70, 70 to 80, 80 to 90, and 90 to 100 percent. A band includes its lower limit and excludes its upper limit, as in the reference file. The coach can edit the bands. Polar does not state how it treats a value at or above 100 percent of HRmax.
- Polar `heart_rate_avg_percent`, with max and min versions: heart rate relative to the player's HRmax, which defaults to 220 minus age. The API does not return HRmax, so name the HRmax source yourself.
- Polar `cardio_load`: Banister TRIMP summed from per-second heart rate, using resting heart rate, maximum heart rate, and gender. A 60-minute session typically scores 70 to 130. The reference file's default Banister form uses the session mean heart rate. Polar sums per-second terms, which matches the reference file's labeled per-sample option. Polar does not publish the scaling of the sum.
- Polar `training_load`: an older load score with unpublished method. Do not compare it with `cardio_load` or with any TRIMP.
- Firstbeat `TRIMP`: Banister TRIMP, T x HRratio x 0.64 x e^(1.92 x HRratio), where HRratio = (HRex − HRrest) / (HRmax − HRrest). Firstbeat uses beat-to-beat heart rate and a lower intensity limit that is not published. A mean-heart-rate TRIMP from another system gives different numbers. The Firstbeat file maps it to no reference file.
- Firstbeat `TRIMP/min`: TRIMP divided by session duration. The period used for laps and sessions is not published. The Firstbeat file maps it to no reference file.
- Firstbeat `%HRmax` and time in heart rate zones: zone limits are set in %HRmax, and the default limits are not published. The API numbers zones from the top, so `zone1Time` is the highest zone. The Firstbeat file maps both to no reference file.
- Catapult: the 10 Hz sensor data carry `hr` in beats per minute. The Catapult file maps no heart rate load metric.

**Reference file.** [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md)

### Acute to chronic workload ratio

**What it measures.** The acute to chronic workload ratio (ACWR) divides an athlete's recent load (acute load) by their longer-term average load (chronic load). It describes how recent load compares with what the athlete has been doing. Put this sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text: "ACWR describes how recent load compares with longer-term load. It does not predict injury."

Read these limits before you use it:

- No study has properly estimated whether changing ACWR changes injury rates, and the ratio adds noise and statistical artifacts (Impellizzeri et al., 2020a).
- A reanalysis found that ACWR gave no meaningful predictive advantage over a model with no predictor. Dividing acute load by made-up chronic values produced similar injury associations to the real ratio (Impellizzeri et al., 2021).
- The ratio does not remove the effect of acute load, even when the windows do not overlap (Impellizzeri et al., 2020a; Impellizzeri et al., 2020b).
- The window lengths are a convention. Studies have used 1 to 2 weeks for acute load and 1 to 8 weeks for chronic load without justification (Impellizzeri et al., 2020b).
- Training-load measures cannot tell you whether a change raises or lowers injury risk (Impellizzeri et al., 2020b).
- A "sweet spot" of 0.8 to 1.3 and a "danger zone" of 1.5 or higher were proposed by Gabbett (2016). Later work found no evidence to support ACWR for reducing injury risk (Impellizzeri et al., 2020a; Impellizzeri et al., 2021). Do not use these bands as thresholds.

**Inputs.** The calculation needs these data:

- One daily load total per athlete per calendar day in one load measure, such as `srpe_load_au` (AU) or `distance_m` (m)
- `0` on rest days, and missing for days with training but no recorded load
- An `availability` column that marks injured, ill, or modified-training days

**Calculation.** Three variants are in use. They give different numbers from the same data, so name the variant every time:

```text
Rolling average, coupled:    ACWR = mean daily load, last 7 days ÷ mean daily load, last 28 days
Rolling average, uncoupled:  ACWR = mean daily load, last 7 days ÷ mean daily load, days 8 to 28 back
EWMA:                        EWMA_today = load_today × λ + (1 − λ) × EWMA_yesterday
                             λ = 2 ÷ (N + 1)
                             ACWR = EWMA with N = 7 ÷ EWMA with N = 28
```

The terms mean the following:

- `load`: daily load in one measure. Both loads in the ratio must use the same measure.
- Acute load: the recent window, by convention 7 days. Hulin et al. (2014) used 1 week acute and a 4-week rolling average chronic load.
- Chronic load: the longer window, by convention 28 days.
- Coupled: the acute week is inside the chronic window. This is the traditional form (Windt & Gabbett, 2019).
- Uncoupled: the chronic window excludes the acute week, so it uses the 3 weeks before it (Gabbett et al., 2019; Windt & Gabbett, 2019).
- Mathematical coupling: in coupled ACWR, the same numbers sit in the top and bottom of the ratio. This creates a spurious correlation of about 0.50 between acute and chronic load: r = 0.52 in simulated data of 1,000 athletes (Lolli et al., 2019, as reported by Windt & Gabbett, 2019). With four unrelated weeks of equal spread, the arithmetic gives exactly 0.5. Real loads also correlate for reasons other than coupling. In real basketball and weightlifting data, acute load correlated with uncoupled chronic load at r = 0.17 to 0.53 (Coyne et al., 2019).
- EWMA: exponentially weighted moving average. It gives older days less weight instead of dropping them at the window edge. `λ` is the decay value. `N` is the time decay constant in days, typically 7 and 28 (Williams et al., 2017).
- `N` sets the span, not a hard memory limit. The 28-day EWMA still puts 13.5% of its weight on days older than 28 days, because (1 − 2/29)^28 = 0.135.
- EWMA start: the file sets the first EWMA value to the day 1 load. Williams et al. (2017) started both EWMAs at the day 1 load, as their figure legend states in the authors' accepted manuscript. Early values depend on the start value, which Wang et al. (2020) call the initial load problem. With λ = 2/29, the start value still carries 14.5% of the 28-day EWMA on day 28, 2.0% on day 56, and 0.3% on day 84. It carries 0.04% of the 7-day EWMA on day 28.

Follow these steps from raw inputs:

1. Add sessions into one daily total per `athlete_id` and `date`.
2. Build a full calendar for each athlete, one row per day. Put `0` on rest days. Leave days with training but no recorded load as missing.
3. Check that every calendar day has exactly one row. Stop and fix the data if it does not.
4. Ask the user for the variant and the windows. Use 7 and 28 days if they have no preference. Say the windows are a convention, even when the user chose them.
5. For rolling coupled ACWR, divide the mean daily load of the last 7 days by the mean daily load of the last 28 days.
6. For rolling uncoupled ACWR, divide the mean daily load of the last 7 days by the mean daily load of days 8 to 28 back.
7. For EWMA ACWR, set both EWMA values to the day 1 load. Update each day with λ = 0.25 for N = 7 and λ = 2 ÷ 29 for N = 28. On a missing day, keep each EWMA at the previous day's value. Divide the 7-day EWMA by the 28-day EWMA.
8. Report no rolling ratio before day 28 and no EWMA ratio before day 56. Report a ratio as missing on a missing day and the 27 days after it. Keep showing the acute load when its own 7 days have no missing day.
9. Report the acute and chronic loads next to each ratio, with the variant name, the windows, and the sentence that ACWR does not predict injury. Give the acute and chronic loads to two decimals. When the user will check another tool against your values, start the table on the last day with no ratio, so the first blank ratio shows.

**Worked example.** One athlete's daily session RPE load in AU, from 2026-08-03. Week 5 is a preseason camp:

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Week total |
|---|---|---|---|---|---|---|---|---|
| 1 | 450 | 600 | 300 | 550 | 250 | 0 | 0 | 2,150 |
| 2 | 500 | 620 | 320 | 560 | 280 | 0 | 0 | 2,280 |
| 3 | 480 | 650 | 300 | 600 | 260 | 0 | 0 | 2,290 |
| 4 | 520 | 640 | 350 | 580 | 300 | 0 | 0 | 2,390 |
| 5 | 700 | 800 | 500 | 750 | 600 | 400 | 0 | 3,750 |

The rolling ratios on day 35 (2026-09-06) come from the weekly totals:

- Acute weekly load: 3,750 AU.
- Coupled chronic weekly load: (2,280 + 2,290 + 2,390 + 3,750) ÷ 4 = 2,677.5 AU.
- Uncoupled chronic weekly load: (2,280 + 2,290 + 2,390) ÷ 3 = 2,320.0 AU.
- Coupled ACWR: 3,750 ÷ 2,677.5 = 1.40.
- Uncoupled ACWR: 3,750 ÷ 2,320.0 = 1.62.

The EWMA uses λ = 0.25 and λ = 0.069, both started at the day 1 load of 450 AU. On day 2 the 7-day and 28-day EWMAs are 487.5 and 460.3 AU. On day 3 they are 440.6 and 449.3 AU. On day 35, the mean daily loads are 535.71 AU (7 days), 382.50 AU (28 days), and 331.43 AU (days 8 to 28). The 7-day and 28-day EWMAs are 386.06 and 394.62 AU, which gives an EWMA start-up value of 0.98. Starting both EWMAs at the week 1 mean of 307.1 AU gives 1.01 instead. These EWMA values fall before day 56, so they are shown only to compare the variants.

Result: on day 35 the same athlete has a coupled ACWR of 1.40, an uncoupled ACWR of 1.62, and an EWMA start-up value of 0.98 or 1.01. The variants disagree by 0.64, the largest gap in the week. ACWR describes how recent load compares with longer-term load. It does not predict injury.

**Variants.** The three variants above are the ones in use. The weekly-sum form gives the same coupled value: acute weekly sum ÷ (28-day sum ÷ 4). Weekly sums and daily means give the same rolling ratio only when every window has the full number of days. The uncoupled variant removes the shared week, but the ratio still fails to normalize acute load (Impellizzeri et al., 2020a). EWMA is a poor fit when athletes taper (Wang et al., 2020).

**What changes the number.** These choices change the result when the athlete's training does not change:

- Variant: on day 35, the same load gives 1.40 coupled, 1.62 uncoupled, and 0.98 EWMA (start-up value).
- Window lengths: a 7:21 coupled ratio on day 35 gives 1.33 instead of 1.40.
- Day of the week: EWMA ACWR drops on rest days. It moved from 1.21 on Saturday to 0.98 on Sunday. Compare values on the same weekday.
- EWMA start value: starting at the week 1 mean (307.1 AU) instead of the day 1 load (450 AU) changes day 28 from 0.68 to 0.73 in the worked example. Early EWMA values depend on the start value (Wang et al., 2020).
- Rest days versus missing days: treating a missing day as `0` lowers both loads. Dropping rest-day rows makes a 7-row window span more than 7 days.
- Injured, ill, or modified-training days: these lower the load for reasons the ratio cannot show. Mark them.
- Load measure: a ratio built on session RPE load and one built on distance are different numbers.
- A chronic load near zero: after a break, injury, or illness, a small chronic load makes the ratio very large. Report the loads instead.

**Units and typical range.** ACWR has no unit. A value of 1.0 means acute and chronic load are equal. No ACWR range has been shown to be safe or to lower injury risk (Impellizzeri et al., 2020a). The rolling coupled 7:28 ratio runs from 0 to 4.0, because the acute week is a quarter of the chronic window. The uncoupled and EWMA ratios run from 0 upward with no fixed ceiling. Both bounds come from the arithmetic of the formulas. The rolling ratios need 28 days with no gaps, and the EWMA ratio needs 56 days.

**Vendor equivalents.** The device files map these metrics:

- Polar Strain, Tolerance, and Cardio load status (web only): Strain is the 7-day average daily cardio load, Tolerance is the 28-day average, and Status is Strain divided by Tolerance. This matches the coupled rolling ACWR in form. The bands are below 0.8, 0.8 to 1.0, 1.0 to 1.3, and above 1.3. Polar attaches injury and illness wording to the bands. Report the ratio without that wording. Whether rest days count as zero is not published.
- Polar `cardio_load_interpretation`: session load divided by the 90-day session average, with bands below 0.5, 0.5 to 0.75, 0.75 to 1.25, 1.25 to 2, and 2 or more. It needs three sessions. Polar says the bands come from customer data, not firm scientific evidence. The Polar file maps it to no reference file.
- Firstbeat `Acute Training Load`: the sum of daily TRIMP over 7 days. It is a sum, not a daily mean.
- Firstbeat `Chronic Training Load`: the sum of daily TRIMP over 28 days, divided by 4. It is a weekly amount, and the 28 days appear to include the acute week.
- Firstbeat `ACWR`: acute load divided by chronic load, the coupled rolling-sum form. The gauge color limits are not published. Firstbeat says a high ACWR raises injury risk. The ACWR reference file does not support that claim. The API lacks values for days with no measurement.

**Reference file.** [acwr.md](../skills/load-and-wellness/references/acwr.md)

### Wellness z-score

**What it measures.** A wellness z-score shows how far today's wellness answer sits from that athlete's own usual answers, in units of that athlete's usual day-to-day spread. Self-reported measures tracked changes in training load more consistently than common objective measures in a systematic review (Saw et al., 2016). Most daily wellness forms use single questions, and the most used single items in sport have not been validated (Jeffries et al., 2020). A z-score describes an unusual answer. It does not explain the cause, and it does not identify illness, injury, or overtraining.

**Inputs.** The calculation needs these data:

- One row per athlete per day with `athlete_id`, `date`, and one column per item, such as `sleep`, `soreness`, `fatigue`, `stress`, and `mood`, in form points such as 1 to 5
- Each item's direction, confirmed with the user
- The baseline window and the minimum number of baseline days, chosen by the user. If the user has none, the file offers 14 answers inside a 28-day window, labeled as its own choice, and never fewer than 7 answers covering one full training week.
- Whether the practitioner also flags on the raw answer, and at what level

**Calculation.** Calculate each athlete and each item separately:

```text
z = (x_today − baseline_mean) ÷ baseline_sd
change_points = x_today − baseline_mean
```

The terms mean the following:

- `x_today`: today's answer for one item, or today's total score
- `baseline_mean`: the mean of that athlete's previous answers for the same item over the baseline window. Exclude today.
- `baseline_sd`: the sample SD of the same baseline answers
- `z`: the result, in SD units, with no unit
- `change_points`: the change from the baseline mean in the form's own points. Show it, and the raw answer, beside every z-score.

Follow these steps from raw inputs:

1. Flip any item where a high number is bad, so a high number is good for every item. On a 1 to 5 scale, flipped = 6 − answer.
2. For each athlete, item, and day, take the answers from the baseline window before that day. Exclude the day being scored.
3. Count the baseline answers. If the count is below the minimum, report "baseline too short" with the count.
4. Calculate the baseline mean, the change in points, and the sample SD.
5. If the SD is 0, report "no variation in baseline" and the change in points.
6. Calculate z = (today's answer − baseline mean) ÷ baseline SD.
7. For a total z-score, add the flipped items into a daily total first, then repeat steps 2 to 6 on the totals.
8. Report each item's raw answer, change in points, z-score, status, baseline window, and baseline day count. Show the total z-score only next to the item z-scores.

**Worked example.** One athlete answers a 1 to 5 form each morning, where 5 is best for every item. The baseline is the 14 mornings before today:

| Item | Baseline answers, 14 days | Today | Baseline mean | Change (points) | Baseline SD | z |
|---|---|---|---|---|---|---|
| Sleep | 4, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 3, 4, 4 | 2 | 3.93 | −1.93 | 0.62 | −3.13 |
| Soreness | 3, 4, 4, 3, 4, 3, 3, 4, 3, 4, 4, 3, 3, 4 | 3 | 3.50 | −0.50 | 0.52 | −0.96 |
| Fatigue | 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3 | 4 | 3.64 | 0.36 | 0.50 | 0.72 |
| Stress | 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4 | 4 | 3.86 | 0.14 | 0.36 | 0.39 |
| Mood | 4, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4 | 4 | 4.14 | −0.14 | 0.36 | −0.39 |

Sleep z = (2 − 3.9286) ÷ 0.6157 = −3.13, from the unrounded mean and SD. The rounded values in the table give −3.11. For the total, the baseline daily totals are 19, 19, 19, 19, 20, 19, 18, 19, 19, 21, 19, 18, 19, and 19, with a mean of 19.07 and an SD of 0.73. Today's total is 2 + 3 + 4 + 4 + 4 = 17, so the total z = (17 − 19.0714) ÷ 0.7300 = −2.84. The item z-scores show that the low total comes from sleep, with a smaller drop in soreness.

**Variants.** Choose and name the variant:

- Item-level z-score: one z-score per question. Use this by default. It keeps the reason for a change visible.
- Total z-score: add the items into a daily total, then standardize the total against the athlete's baseline of totals. Show the item z-scores next to it.
- Rolling baseline: the previous N calendar days, such as 28. It follows slow changes, but it also absorbs a slow decline.
- Fixed baseline: a set period, such as a stable block of normal training. It does not drift, but it ages.
- Raw-answer flag: a practitioner may also flag on the raw answer, such as any soreness of 1 or 2. That is their choice. Label it as theirs.

Treat the numbers with these limits in mind:

- A one-direction cut-off of z = −2 flags 2.3% of ordinary days when the baseline mean and SD are known, and 3.8% with a 14-day baseline. Across 25 athletes on one item, that is 0.57 or 0.94 flags a day by chance, and a 43.7% or 61.8% chance of at least one. With 7 baseline answers the rate for one athlete is 5.5%, and with 28 it is 3.0%. These figures come from the normal and t distributions. The real rate on a 1 to 5 scale can be higher or lower.
- A small baseline gives an unstable SD. The 95% confidence interval for the true SD runs from about 0.64 to 2.20 times the sample SD with 7 values, 0.72 to 1.61 times with 14, and 0.79 to 1.36 times with 28. With 14 baseline days, a z-score of −3.13 matches about −1.94 to −4.32 against the true SD, which is the z-score multiplied by 0.621 to 1.379.
- Today's distance from a mean of n days has a spread of baseline SD × √(1 + 1/n). This is the standard prediction interval for one new value against a mean of n values (NIST, Dataplot reference manual, after Hahn and Meeker, 1991). With n = 14, √(1 + 1/14) = 1.035, so the sleep z-score of −3.13 becomes −3.03 on that scale.
- The baseline SD is not a typical error. It mixes real day-to-day change with error. Do not use it as TE, and do not borrow a noise band built on TE for wellness answers.
- Daily answers are often autocorrelated, and answers on a short point scale are not normally distributed, so treat these factors as a rough guide only.
- On a short point scale, z-scores jump in steps. For a single item, report the raw answer and the change in points first, and the z-score second as approximate. In a simulation run for the file (stable athletes, 14-day baselines, independent days), the chance rate of z ≤ −2 on one item ranged from 3.3% to 5.6% depending on the usual answer, against 3.8% expected, and most flags were a one-point drop.
- We found no peer-reviewed source that sets a minimum number of baseline days. Ask the user, and report the number of baseline days with every z-score. If the user has no number, the file offers 14 baseline answers inside a 28-day window, labeled as its own choice, and never fewer than 7 answers covering one full training week. A baseline should be stable, with low variability and no clear trend (Sands et al., 2019). The file infers, as its own suggestion, that a baseline should cover at least one full training week.
- Report the number of flags expected by chance next to the number found. Recommend a repeat answer or a conversation with the athlete before anyone acts on a single flag (Barnett et al., 2005).

**What changes the number.** These choices change the result when the athlete has not changed:

- Baseline length: with the last 7 days as the baseline, today's sleep z-score is −3.46 (mean 4.00, SD 0.58) instead of −3.13 with 14 days.
- Including today in the baseline: the sleep z-score shrinks from −3.13 to −2.32.
- Item versus total: the total z-score is −2.84. The plain mean of the five item z-scores is −0.68.
- Size of the baseline SD: an answer of 3 gives z = −2.36 on stress (mean 3.86, SD 0.36) but −0.96 on soreness (mean 3.50, SD 0.52).
- Rolling versus fixed baseline: a slow decline lowers the rolling mean, so later answers look less unusual.
- Chronic problems: an athlete whose 14 soreness answers were mostly 1 and 2 (mean 1.29, SD 0.47) gets z = −0.61 for a 1, the worst answer on the form.
- Scale direction: an item that runs the other way and is not flipped gives the wrong sign and a wrong total.
- Zero spread: an athlete who answered 4 on all 14 stress mornings has an SD of 0, so the z-score is undefined. A 3 still shows as −1.0 point.
- Blank answers: a spreadsheet formula without a blank check turns a missing answer into 0, which gives a sleep z-score of (0 − 3.9286) ÷ 0.6157 = −6.38.
- Form changes: a new question wording or scale starts a new baseline.

**Units and typical range.** A z-score has no unit. Zero means today equals the athlete's baseline mean. The file gives no validated flag cut-off, because the most used single wellness items have no validation studies (Jeffries et al., 2020). Use the cut-off the practitioner chose, and label it as their choice.

**Vendor equivalents.** None.

**Reference file.** [wellness-z-score.md](../skills/load-and-wellness/references/wellness-z-score.md)

## Running load

These metrics come from GPS (global positioning system) units, local positioning systems, or video tracking. Speed is in km/h or m/s. Sampling rate is in Hz, samples per second.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Total distance, from speed | `Σ (speed_m_s × dt_s)` | m | [total-distance.md](../skills/gps-running-load/references/total-distance.md) |
| Total distance, from positions | `Σ √((x[i] − x[i−1])² + (y[i] − y[i−1])²)` | m | [total-distance.md](../skills/gps-running-load/references/total-distance.md) |
| Distance per minute | `total_distance_m ÷ duration_min` | m/min | [total-distance.md](../skills/gps-running-load/references/total-distance.md) |
| High-speed running distance | `Σ (speed_m_s × dt_s)` for samples where `speed_m_s ≥ threshold_m_s` | m | [high-speed-running.md](../skills/gps-running-load/references/high-speed-running.md) |
| Speed band distance | `Σ (speed_m_s × dt_s)` for samples where `lower_m_s ≤ speed_m_s < upper_m_s` | m | [high-speed-running.md](../skills/gps-running-load/references/high-speed-running.md) |
| Acceleration | `(speed_m_s[i] − speed_m_s[i − k]) ÷ (k × dt_s)` | m/s² | [accelerations-decelerations.md](../skills/gps-running-load/references/accelerations-decelerations.md) |
| Acceleration and deceleration efforts | Runs of samples beyond ± the threshold that last at least `min_duration_s` | Count | [accelerations-decelerations.md](../skills/gps-running-load/references/accelerations-decelerations.md) |
| Effort distance | `Σ (speed_m_s × dt_s)` over the samples in counted efforts | m | [accelerations-decelerations.md](../skills/gps-running-load/references/accelerations-decelerations.md) |

### Total distance and distance per minute

**What it measures.** Total distance is how far an athlete traveled in a session or match. Distance per minute, also called relative distance, is that distance divided by the time it took, so you can compare sessions of different lengths.

**Inputs.** The calculation needs one of these data sources:

- A summary export with one row per athlete per session and a total distance column
- Raw speed samples with a `time_s` column, from which you take `dt_s`
- Raw positions `x` and `y` in metres on the field or court axes
- A duration in minutes under one rule: whole session, time on the field, or drill time only

**Calculation.** Use the device's total distance when the file holds one summary row per athlete per session. Otherwise, add the distance in each sample:

```text
from speed:      total_distance_m = Σ (speed_m_s × dt_s)
from positions:  total_distance_m = Σ √((x[i] − x[i−1])² + (y[i] − y[i−1])²)
distance_per_min = total_distance_m ÷ duration_min
```

The terms mean the following:

- `speed_m_s`: speed in one sample, in m/s. Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 first.
- `dt_s`: the time between samples, in seconds, from the timestamp differences. At 10 Hz it is 0.1 s.
- `x`, `y`: the athlete's position in metres
- `total_distance_m`: distance in metres
- `duration_min`: the time you divide by, in minutes, under one stated rule
- `distance_per_min`: relative distance in m/min

Follow these steps from raw inputs:

1. Find the distance column and its unit. Convert kilometres × 1,000 and yards × 0.9144 to metres.
2. For raw samples, find the speed column and convert it to m/s.
3. Take `dt_s` for each sample from the timestamp differences. Flag any step longer than expected as a gap.
4. Multiply each speed sample by its `dt_s`, then add the sample distances for each athlete and session.
5. If the file holds positions only, add the straight-line distances between consecutive positions. Label the result as recalculated from positions.
6. Convert the duration to minutes. A value of `hh:mm:ss` becomes `hh × 60 + mm + ss ÷ 60`.
7. Divide `total_distance_m` by `duration_min`.
8. Label each result with the distance method, the duration rule, the sampling rate, and the device type.

**Worked example.** One player's summary row, one second of raw speed samples at 10 Hz, and one second of raw positions:

| Input | Value |
|---|---|
| Total distance in the export | 6.42 km |
| Whole session duration | 01:15:30 |
| Time on the field | 62.0 min |
| Raw speed samples, km/h | 18.0, 18.4, 18.9, 19.3, 19.8, 20.2, 20.5, 20.9, 21.2, 21.6 |
| Raw positions, x in m | 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 |
| Raw positions, y in m, with ±0.1 m noise | 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1 |

The calculation gives these results:

- Summary row: 6.42 km × 1,000 = 6,420 m. The whole session is 1 × 60 + 15 + 30 ÷ 60 = 75.5 min, so 6,420 ÷ 75.5 = 85.0 m/min. Time on the field gives 6,420 ÷ 62.0 = 103.5 m/min. Neither is wrong. Label which one you used.
- Raw speed: the samples in m/s are 5.000, 5.111, 5.250, 5.361, 5.500, 5.611, 5.694, 5.806, 5.889, and 6.000. Each × 0.1 s, added, gives 5.52 m in one second.
- Raw positions: the athlete runs straight at 5 m/s, so the true distance is 5.0 m. With noise, each step is √(0.5² + 0.2²) = 0.5385 m, and ten steps give 5.39 m. The noise adds 7.7%.

**Variants.** The three distance methods do not give the same number. Position noise adds small sideways steps, so summed positions overestimate distance unless the positions are filtered. Software-derived and raw-processed data differed substantially for a range of movement variables (Thornton et al., 2019). Use one method for the whole trend.

Distance per minute has two variants:

- Whole-session average: total distance divided by the full duration. Use it to compare sessions or matches of different lengths.
- Peak period: the highest distance per minute in any window of a set length, such as 1 or 5 minutes. A rolling window starts at every sample. A fixed window starts only at set times. Fixed 5-minute periods underestimated peak high-velocity running distance by up to 25% compared with rolling periods (Varley et al., 2012a). Over 60 s to 600 s windows, fixed epochs underestimated rolling averages by about 7% to 10% for total distance and about 12% to 25% for distance above 5.5 m/s (Fereday et al., 2020). State the window length and type, and never compare a rolling value with a fixed value.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Duration rule: 85.0 m/min for the whole session against 103.5 m/min for time on the field.
- Assumed sampling interval: treating the 10 Hz samples as 5 Hz (`dt_s` = 0.2 s) doubles the distance from 5.52 m to 11.04 m.
- Speed unit: adding km/h values as if they were m/s gives 19.88 instead of 5.52 for the same second, 3.6 times too large.
- Distance method: ±0.1 m of position noise adds 7.7%.
- Sampling rate: 5 Hz units were more valid than 1 Hz units (Jennings et al., 2010), and 10 Hz units were the most valid and reliable (Scott et al., 2016).
- Device type: total distance differences between systems were trivial to small in youth soccer players (Buchheit et al., 2014b). In small-sided games, errors against a reference system were 2.2% to 4.0% (Linke et al., 2018).
- Unit to unit: two units of the same model disagree on the same movement (Johnston et al., 2014; Thornton et al., 2019). Give each athlete the same unit every session.
- Software version and filter settings: processing choices change the output (Malone et al., 2017; Thornton et al., 2019). Record the software version and the processing date.
- Signal quality: satellite count, signal dropouts, and device fit affect GPS output (Malone et al., 2017).
- Whole-session or peak-period: a peak window is always at least as high as the session average.

**Units and typical range.** Total distance depends on the sport, position, session type, and duration. Compare each athlete with their own history in the same session type. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Elite Australian football, match, 5 Hz GPS | 129 ± 17 m/min (mean ± SD) | Varley et al., 2014 |
| Elite rugby league, match, 5 Hz GPS | 97 ± 16 m/min | Varley et al., 2014 |
| Elite soccer, match, 5 Hz GPS | 104 ± 10 m/min | Varley et al., 2014 |
| Professional soccer, worst-case relative total distance, rolling windows, 10 Hz | 190.1 ± 20.4 m/min over 60 s; 120.9 ± 13.1 m/min over 600 s | Fereday et al., 2020 |
| Measurement error, total distance, team sport running circuit | Coefficient of variation 3.6%, sampling rate not stated in the abstract | Jennings et al., 2010 |
| Measurement error, total distance, 10 Hz units | Typical error 1.3% between units | Johnston et al., 2014 |
| Error against a reference system, small-sided games | 2.2% to 4.0% across GPS, local positioning, and video tracking | Linke et al., 2018 |

The error rows come from circuits and from units compared with each other. They are not the test-retest error of one athlete on one unit. For illustration only, a typical error of 3.6% would give a noise band of ±9.98% for two single sessions and ±7.73% against a 5-session baseline mean. A typical error of 1.3% gives ±3.60% and ±2.79%.

**Vendor equivalents.** The device files map these metrics:

- Catapult Total Distance (`total_distance`): the sum over the selected periods, in m, with no difference in method. For 10 Hz data, compute distance as the last odometer (`o`) value minus the first, not as a sum of odometer values. Periods can nest, so check period sums against the session total.
- Kinexon Total Distance: in m. Kinexon publishes no formula. LPS and GPS Pro measure position. An IMU can only estimate distance, so IMU values are estimates, not measured distance. Kinexon's own pages contradict each other on whether an IMU uses position data.
- Polar `distance_meters` and Total distance: from GNSS at 10 Hz outdoors and the inertial sensor indoors. Polar reports a distance error of 1 percent or less on a 100 m straight path and 2 percent or less on a 120 m multi-directional path, from a study its white paper cites. Polar `Distance / Min` has no published definition.
- Firstbeat `Distance`: passed through from a Garmin recording, when present, in m or mi.

**Reference file.** [total-distance.md](../skills/gps-running-load/references/total-distance.md)

### High-speed running distance

**What it measures.** High-speed running distance is the distance an athlete covers while moving faster than a chosen speed threshold. The number depends on the threshold as much as on the athlete. Treat the threshold as part of the metric's name. No standard threshold exists across sports. Speed zone definitions vary widely within and between sports (Cummins et al., 2013).

**Inputs.** The calculation needs these data:

- Raw speed samples, or a summary export with distance in speed zones
- The sampling rate, checked against the timestamps
- The threshold value, unit, type (absolute or individualized), and the date it was set. For individualized thresholds, the test that set them.
- The vendor's boundary rule, and the minimum effort duration if you count efforts

**Calculation.** Add the distance of every sample at or above the threshold. For a band with an upper limit, count samples at or above the lower bound and below the upper bound:

```text
hsr_distance_m  = Σ (speed_m_s × dt_s)   for samples where speed_m_s ≥ threshold_m_s
band_distance_m = Σ (speed_m_s × dt_s)   for samples where lower_m_s ≤ speed_m_s < upper_m_s
threshold_m_s   = threshold_km_h ÷ 3.6, or threshold_mph × 0.44704
```

The terms mean the following:

- `speed_m_s`: speed in one sample, in m/s
- `dt_s`: the time between samples. At 10 Hz, it is 0.1 s.
- `threshold_m_s`: the speed threshold in m/s
- `lower_m_s`, `upper_m_s`: the bounds of a speed band, in m/s
- `hsr_distance_m`: the distance covered at or above the threshold, in metres
- Effort: one continuous stretch at or above the threshold that lasts at least a minimum time, the minimum effort duration or dwell time. The file measures a run's length as samples × `dt_s`.

Follow these steps from raw inputs:

1. Convert speed to m/s, and convert the threshold to m/s.
2. For individualized thresholds, join each athlete's own threshold to their rows by athlete ID.
3. Set `dt_s = 1 ÷ Hz`, and check it against the timestamps.
4. Mark each sample at or above the threshold, and below the upper bound for a band, unless the vendor's rule differs. Round speed and threshold to the same number of decimals first.
5. Multiply each marked sample's speed by `dt_s`, and add the marked distances for each athlete and session.
6. For effort counts, group consecutive marked samples into runs. Count a run as an effort only if it lasts at least the minimum effort duration.
7. Label each result with the threshold, its unit, the threshold type, the boundary rule, and the minimum effort duration.

**Worked example.** Three seconds of one athlete's speed at 10 Hz (30 samples), with a threshold of 19.8 km/h (5.5 m/s) and a minimum effort duration of 0.5 s:

| Samples | Speed, km/h |
|---|---|
| 1 to 10 | 14.0, 15.5, 17.0, 18.5, 19.6, 20.4, 21.0, 21.3, 21.1, 20.6 |
| 11 to 20 | 19.9, 19.0, 18.2, 17.6, 17.9, 18.8, 19.9, 20.3, 20.1, 19.7 |
| 21 to 30 | 18.9, 17.8, 16.4, 15.2, 14.6, 14.1, 13.5, 13.0, 12.4, 11.8 |

The calculation runs this way:

1. The samples at or above 5.5 m/s are samples 6 to 11 (5.667, 5.833, 5.917, 5.861, 5.722, 5.528 m/s) and samples 17 to 19 (5.528, 5.639, 5.583 m/s).
2. Each × 0.1 s, added, gives 3.45 m and 1.68 m.
3. High-speed running distance: 3.45 + 1.68 = 5.13 m.
4. The first run lasts 6 samples × 0.1 s = 0.6 s. The second lasts 0.3 s.
5. With a 0.5 s minimum, only the first run counts: 1 effort.

The same 30 samples give these results under other settings:

| Threshold | Minimum effort duration | Distance above threshold | Runs above threshold | Efforts |
|---|---|---|---|---|
| 19.8 km/h (5.5 m/s) | 0.5 s | 5.13 m | 0.6 s and 0.3 s | 1 |
| 19.8 km/h (5.5 m/s) | 0.3 s | 5.13 m | 0.6 s and 0.3 s | 2 |
| 15.0 km/h (4.167 m/s) | 0.5 s | 12.08 m | 2.3 s | 1 |
| 14.4 km/h (4.0 m/s) | 0.5 s | 12.48 m | 2.4 s | 1 |
| 60% of a 9.0 m/s maximum speed: 5.4 m/s (19.44 km/h) | 0.5 s | 6.22 m | 0.7 s and 0.4 s | 1 |
| 19.8 km/h, run length as (n − 1) × `dt_s` | 0.3 s | 5.13 m | 0.5 s and 0.2 s | 1 |

The athlete did not change. The distance more than doubled when the threshold dropped from 19.8 to 14.4 km/h.

**Variants.** Two threshold variants are in use:

- Absolute threshold: one speed for every athlete. Published examples are 19.8 km/h (5.5 m/s), the default of one camera-based system (Abt & Lovell, 2009); 14.4 km/h (4.0 m/s) in youth soccer (Buchheit et al., 2014b); 14.0 to 19.99 km/h for high-speed running and above 20.0 km/h for very high-speed running (Johnston et al., 2014); and 4.17 m/s (15.0 km/h) for high-speed running and 7.00 m/s (25.2 km/h) for sprinting (Varley et al., 2017).
- Individualized threshold: a speed set per athlete. Abt and Lovell (2009) used each player's running speed at the second ventilatory threshold. Reardon et al. (2015) used 60% of each player's maximum speed from a season of training and match data.

Some software measures a run from the first to the last sample, (n − 1) × `dt_s`, instead of samples × `dt_s`. Ask which rule the software uses.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Threshold speed: in a match study, the same players covered 845 m above 19.8 km/h and 2,258 m above their individualized threshold (Abt & Lovell, 2009).
- Threshold unit: 19.8 applied to m/s data selects 0 of 30 samples. 5.5 applied to km/h data selects 30 of 30. A threshold of 19.8 km/h is 12.3 mph.
- Absolute or individualized threshold: with an individualized threshold, forwards in elite rugby union covered more high-speed distance, and backs less, than with an absolute threshold (Reardon et al., 2015).
- Run length rule: with a 0.3 s minimum, it changes the count from 2 to 1.
- Minimum effort duration: it changes effort counts but not distance. Counts drop as the minimum rises (Varley et al., 2017).
- Speed filtering: different velocity filters changed effort counts when the minimum duration was under 0.5 s (Varley et al., 2017).
- Sampling rate: error grows as speed rises, and 10 Hz units are more valid than 1 Hz or 5 Hz units (Jennings et al., 2010; Scott et al., 2016; Johnston et al., 2014).
- Device type: all tracking technologies showed deviations above 40% from a reference system for high-speed distance (Linke et al., 2018).
- Boundary rule: a sample exactly on the threshold counts with `≥` and not with `>`.
- Match-to-match variation: in English Premier League players, match-to-match CV was 16.2% for high-speed running and 30.8% for sprint distance (Gregson et al., 2010).

**Units and typical range.** High-speed running distance is in metres. Report a range only with its threshold. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Professional soccer, match, camera tracking, threshold 19.8 km/h | 845 ± 296 m (mean ± SD) | Abt & Lovell, 2009 |
| Same players, individualized threshold (median 15 km/h, range 14 to 16 km/h) | 2,258 ± 707 m | Abt & Lovell, 2009 |
| Elite rugby union, match, 10 Hz GPS, 60% of maximum speed | Forwards 354.72 ± 99.22 m. Backs 570.02 ± 171.14 m. | Reardon et al., 2015 |
| English Premier League, camera tracking, match-to-match variation | CV 16.2% for high-speed running, 30.8% for sprint distance | Gregson et al., 2010 |
| Measurement error, high-speed distance, any tracking technology | Above 40% deviation from a reference system | Linke et al., 2018 |
| Measurement error, 10 Hz and 15 Hz units, as speed rises | Typical error 0.8% to 19.9% | Johnston et al., 2014 |

The error rows compare units or systems. They are not the test-retest error of one athlete on one unit.

**Vendor equivalents.** The device files map these metrics:

- Catapult HS Distance: distance in velocity bands 5 and 6, by default above 5.5 m/s. Catapult Sprint Distance: distance in band 6, by default above 7 m/s. The default bands are band 1 0 to 0.2 m/s, band 2 0.2 to 2, band 3 2 to 4, band 4 4 to 5.5, band 5 5.5 to 7, and band 6 above 7. Those are Vector Core defaults. OpenField allows up to eight bands, and the public OpenField Bands page publishes no defaults. Bands can be absolute speeds or a percentage of each athlete's maximum, and they change by account and season. New bands apply only to future sessions unless someone reprocesses old sessions. Catapult does not publish its boundary rule. Catapult `max_vel` is the highest speed in the selected time.
- Kinexon Max. Speed: in km/h and mph. Kinexon publishes no formula. LPS and GPS Pro measure position. An IMU can only estimate speed, and how an IMU reports Max. Speed is not published. Smoothing is not published, and no source supports a cross-vendor comparison of the number. The column names for speed zones are not confirmed. Published studies that used Kinexon set high-speed running at 4.4 m/s or more in a handball study (Carton-Llorente et al., 2023). A handball LPS study names 5.5 to 7 m/s high-intensity running (Bassek et al., 2023). One study set sprints at 18.72 km/h (5.2 m/s) with a 1.0 s minimum. These are study settings, not Kinexon defaults.
- Polar `speed_zones_kmh` and Distance in speed zone: distance in five speed bands set in the sport profile, in m with limits in km/h. The defaults are not published, and the limits change when a coach edits them. Polar `speed_max_kmh` is top speed. The default Polar sprint rule is an acceleration test, not a speed test.

**Reference file.** [high-speed-running.md](../skills/gps-running-load/references/high-speed-running.md)

### Accelerations and decelerations

**What it measures.** Acceleration and deceleration counts are how many times an athlete speeds up or slows down harder than a chosen rate, for at least a minimum time. Acceleration and deceleration distance is how far the athlete traveled during those efforts. These metrics show the most variability of common GPS running load metrics (Buchheit et al., 2014a).

**Inputs.** The calculation needs these data:

- Raw speed samples to recalculate, or a summary export to use the software's counts
- The sampling rate, the interval for the change in speed, and any filter
- The threshold in m/s², the boundary rule, the minimum effort duration, and the software version

**Calculation.** Work out acceleration from the change in speed, then count efforts beyond the threshold:

```text
accel_m_s2[i] = (speed_m_s[i] − speed_m_s[i − k]) ÷ (k × dt_s)
acceleration effort = a run of consecutive samples with accel_m_s2 ≥ threshold_m_s2,
                      lasting at least min_duration_s
deceleration effort = a run of consecutive samples with accel_m_s2 ≤ −threshold_m_s2,
                      lasting at least min_duration_s
effort_distance_m   = Σ (speed_m_s × dt_s) over the samples in counted efforts
```

The terms mean the following:

- `speed_m_s`: speed in m/s. Convert before you work out acceleration.
- `dt_s`: the time between samples, 0.1 s at 10 Hz
- `k`: how many samples back you look. With `k = 1` at 10 Hz the interval is 0.1 s, and with `k = 2` it is 0.2 s. Varley et al. (2017) compared 0.2 s and 0.3 s intervals.
- `accel_m_s2`: acceleration in m/s². Positive values are accelerations and negative values are decelerations. Multiply ft/s² by 0.3048.
- `threshold_m_s2`: the acceleration threshold
- `min_duration_s`: the minimum effort duration, or dwell time, measured as samples × `dt_s`. Harper et al. (2019) report 0.2 to 1 s across the studies that stated it.
- `effort_distance_m`: distance covered during counted efforts

The file's boundary rule counts a sample when its absolute acceleration is at or above the lower bound and below any upper bound. Varley et al. (2017) used ≥ 2.78 m/s². Harper et al. (2019) wrote their thresholds as strictly above.

Follow these steps from raw inputs:

1. Convert speed to m/s, and set `dt_s = 1 ÷ Hz`.
2. Ask which interval and filter to use, and use the same choice for every file.
3. Calculate acceleration for each sample.
4. Mark samples at or above the threshold as acceleration samples, and samples at or below the negative threshold as deceleration samples.
5. Group consecutive marked samples into runs. Keep runs that last at least the minimum effort duration. Each kept run is one effort.
6. Count the efforts. For distance, add speed × `dt_s` over the samples in each kept run.
7. Label each result with the threshold, boundary rule, minimum duration, interval, filter, and software version.

**Worked example.** Three seconds of one athlete's speed at 10 Hz (30 samples), with an interval of 0.1 s (`k` = 1), a threshold at or above 2.5 m/s², and a minimum effort duration of 0.2 s:

| Samples | Speed, m/s |
|---|---|
| 1 to 10 | 1.00, 1.30, 1.65, 2.00, 2.35, 2.62, 2.85, 3.05, 3.20, 3.30 |
| 11 to 20 | 3.38, 3.42, 3.44, 3.45, 3.20, 2.85, 2.50, 2.20, 2.00, 1.95 |
| 21 to 30 | 1.93, 2.20, 2.15, 2.10, 2.05, 2.00, 1.98, 1.97, 1.96, 1.95 |

The calculation runs this way:

1. Sample 2: (1.30 − 1.00) ÷ 0.1 = 3.0 m/s².
2. Samples 2 to 6 reach 3.0, 3.5, 3.5, 3.5, and 2.7 m/s², a 0.5 s run. Sample 22 reaches 2.7 m/s², a 0.1 s run from a single noisy jump from 1.93 to 2.20 m/s.
3. Samples 15 to 18 reach −2.5, −3.5, −3.5, and −3.0 m/s², a 0.4 s run. Sample 15 sits exactly on the threshold and counts under the "at or above" rule.
4. With the 0.2 s minimum, the 0.5 s acceleration run and the 0.4 s deceleration run count. The 0.1 s run does not.
5. Result: 1 acceleration and 1 deceleration.
6. Acceleration distance: 0.13 + 0.165 + 0.2 + 0.235 + 0.262 = 0.992 m.
7. Deceleration distance: 0.32 + 0.285 + 0.25 + 0.22 = 1.075 m.

The same 30 samples give these results with one setting changed at a time:

| Setting changed | Accelerations | Acceleration distance | Decelerations | Deceleration distance |
|---|---|---|---|---|
| None (at or above 2.5 m/s², 0.2 s, 0.1 s interval) | 1 | 0.992 m | 1 | 1.075 m |
| Minimum duration 0.1 s | 2 | 1.212 m | 1 | 1.075 m |
| Minimum duration 0.5 s | 1 | 0.992 m | 0 | 0 m |
| Threshold at or above 3.5 m/s² | 1 | 0.600 m | 1 | 0.535 m |
| Interval 0.2 s (`k` = 2) | 1 | 1.147 m | 1 | 0.955 m |
| Strictly above 2.5 m/s² (`>`) | 1 | 0.992 m | 1 | 0.755 m |

With a 0.2 s interval, the noisy sample 22 no longer reaches 2.5 m/s². It becomes 1.25 m/s².

**Variants.** These thresholds appear in published studies and device material:

- Above 2.5 m/s² for high intensity and above 3.5 m/s² for very high intensity, the thresholds Harper et al. (2019) pooled. The most common start threshold in their review was 3 m/s², used in 11 of 19 studies.
- 2.78 m/s² or more (Varley et al., 2017).
- 1.5 m/s² with a 0.5 s minimum, in a basketball study with wearable tags at 20 Hz (Stone et al., 2022).
- Above 2 m/s², in a handball study with wearable tags (Carton-Llorente et al., 2023), and as the default of one GPS vendor.

Two output variants exist. The count is the number of efforts. Distance or time is metres or seconds beyond the threshold. Counts can be reliably obtained at 10 Hz, while distance and time variables are less reliable (Harper et al., 2019). Use the software's counts when you only have a summary export, and never mix recalculated values with software values in one trend.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Threshold: at or above 3.5 m/s² keeps 1 acceleration but cuts its distance from 0.992 m to 0.600 m, because the peak was exactly 3.5 m/s².
- Minimum effort duration: 0.1 s counts a noise spike as a second acceleration, and 0.5 s drops the deceleration. Even 0.1 s changes can make substantial differences in effort counts (Harper et al., 2019).
- Filtering and interval: a 0.2 s interval removes the noise spike. Different filters gave small to very large differences in acceleration counts when the minimum duration was under 0.7 s (Varley et al., 2017).
- Software version: one software update produced large decreases in acceleration counts with the same units (Buchheit et al., 2014a).
- Unit to unit: between-unit variation reached 56% for decelerations above 4 m/s², and some units recorded 2 to 6 times more efforts than others of the same brand (Buchheit et al., 2014a).
- Model to model: two models of the same brand differed by a standardized difference of 2.1 for accelerations above 4 m/s² (Buchheit et al., 2014a).
- Manufacturer and processing: threshold-based acceleration and deceleration variables differed most between manufacturers (Thornton et al., 2019).
- Device type: acceleration values were small to very largely greater with local positioning than with camera or GPS tracking in youth soccer players (Buchheit et al., 2014b).
- Sampling rate: 10 Hz GPS measured instantaneous speed two to three times more accurately than 5 Hz (Varley et al., 2012b).
- Boundary rule: counting −2.5 m/s² as a deceleration sample gives 1.075 m of deceleration distance. A strictly-above rule gives 0.755 m.

**Units and typical range.** Counts depend on the settings above, so no published count range transfers to another system. Compare each athlete with their own history on the same device, software version, and settings. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Common thresholds in elite team sport research | High intensity above 2.5 m/s². Very high intensity above 3.5 m/s². | Harper et al., 2019 |
| Minimum effort durations used in studies | 0.2 to 1 s, from the few studies that reported it: 4 of 19 in the results, 8 in the discussion | Harper et al., 2019 |
| High-intensity acceleration distance per full match | Australian football 194 m, soccer 178 m, rugby union 94 m | Harper et al., 2019 |
| High-intensity deceleration distance per full match | Soccer 162 m, Australian football 149 m, rugby union 54 m | Harper et al., 2019 |
| Accelerations versus decelerations in match play | More high and very high intensity decelerations than accelerations in every sport studied except American football | Harper et al., 2019 |
| Between-unit variation, 50 units of one brand, two 15 Hz models | Up to 56% for decelerations above 4 m/s² | Buchheit et al., 2014a |
| Between-unit variation, range across movement variables | Coefficient of variation 0.2% to 78.2% | Thornton et al., 2019 |

A between-unit figure applies only when the athlete changed to another unit of the same model. No figure in the reference files can serve as one athlete's noise when the athlete changes device type or vendor. For an athlete on one unit, use a typical error from a short-term retest on that unit and the shared noise band rules.

**Vendor equivalents.** The device files map these metrics:

- Catapult Acceleration Efforts and Deceleration Efforts: a default threshold above 2 m/s². In the `Gen2Acceleration` band set, bands 1 to 3 are decelerations and bands 6 to 8 are accelerations. Bands 4 and 5, near zero, cannot be reported. The Gen2 effort rules exclude movements shorter than 0.9 s, from a public Catapult page. The fuller Gen2 rules need a Catapult sign-in.
- Catapult Acceleration load: the sum of absolute acceleration values from smoothed 10 Hz speed. It is a different quantity from PlayerLoad and from effort counts. The Catapult file maps it to no reference file.
- Kinexon Mechanical Load: accelerations and decelerations grouped by intensity, multiplied by proprietary weights, and summed. Mechanical Load is Accel Load plus Decel Load. The weights and bands are not published. Mechanical Intensity is Mechanical Load divided by time. The Kinexon file maps both to no reference file, and no source supports a Catapult equivalent. Published studies that used Kinexon set accelerations at 1.5 m/s² with a 0.5 s minimum in one study, and 2 m/s² in another.
- Polar `sprint_counter` and Sprints: each acceleration above 2.8 m/s² counts once, whatever its length. The coach can switch to a speed threshold in km/h.
- Polar `acceleration_zones_ms2` and Number of accelerations: counts in four acceleration and four deceleration bands. The default thresholds, the effort definition, and the minimum duration are not published.

**Reference file.** [accelerations-decelerations.md](../skills/gps-running-load/references/accelerations-decelerations.md)

## Force plate

These metrics come from a force plate, or from a Nordic hamstring device with a force sensor at each ankle. Force is in newtons (N).

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| CMJ jump height, takeoff velocity method | `takeoff velocity^2 / (2 x 9.81)` | m | [cmj-jump-height.md](../skills/force-plate/references/cmj-jump-height.md) |
| CMJ jump height, flight time method | `9.81 x flight time^2 / 8` | m | [cmj-jump-height.md](../skills/force-plate/references/cmj-jump-height.md) |
| Reactive strength index-modified (RSImod) | `jump height (m) / time to takeoff (s)` | m/s | [rsi-modified.md](../skills/force-plate/references/rsi-modified.md) |
| IMTP gross peak force | Highest vertical force during the pull | N | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP net peak force | `gross peak force - body weight` | N | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP relative peak force | `peak force / body mass` | N/kg | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP allometric peak force | `peak force / body mass^0.67` | N/kg^0.67 | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP rate of force development (RFD) | `(force at X ms after onset - force at onset) / (X / 1000)` | N/s | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| Eccentric hamstring peak force, per leg | Highest force on that leg's sensor in the best repetition | N | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring relative force, per leg | `peak force / body mass` | N/kg | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring two-limb average | `(left peak force + right peak force) / 2` | N | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring between-limb imbalance | `(stronger leg - weaker leg) / stronger leg x 100`, with the weaker side named | % | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |

### Countermovement jump height

**What it measures.** Countermovement jump (CMJ) height is how high the athlete's center of mass rises after takeoff in a vertical jump that starts from standing with a quick dip before the push.

**Inputs.** The calculation needs these data:

- For the takeoff velocity method, the raw vertical force trace in N with a time column in s, summed across both plates, at least 1000 Hz and unfiltered (McMahon et al., 2018a)
- At least 1 s of still standing before each jump (McMahon et al., 2018a)
- For the flight time method, flight time in seconds, such as from a contact mat or a summary export
- About three trials per session (Bishop et al., 2018)

**Calculation.** Three methods exist. They give different numbers from the same jump, so never mix them in one table, trend, or comparison. The takeoff velocity method, also called the impulse-momentum method, is the recommended method when you have the raw trace (Linthorne, 2001; McMahon et al., 2018a):

```text
Takeoff velocity method:
body weight (N)         = mean vertical force during quiet standing
body mass (kg)          = body weight / 9.81
acceleration (m/s^2)    = (vertical force - body weight) / body mass, at each sample
velocity (m/s)          = running integral of acceleration over time, up to takeoff
jump height (m)         = takeoff velocity^2 / (2 x 9.81)

Flight time method:
jump height (m) = 9.81 x flight time^2 / 8
```

The terms mean the following:

- `9.81`: acceleration due to gravity, in m/s²
- `vertical force`: the force the plate measures, in N. Sum both plates when the athlete stands on two.
- `quiet standing`: the still period before the jump starts, at least 1 s (McMahon et al., 2018a)
- `onset of movement`: the first instant force drops below body weight by more than 5 standard deviations of the quiet standing force. Some protocols step back 30 ms from that instant (Owen et al., 2014; McMahon et al., 2018a).
- `takeoff`: the instant force falls below a set threshold. One published threshold is 5 standard deviations of the unloaded plate force, taken over 300 ms of the flight phase (McMahon et al., 2018a).
- `takeoff velocity`: vertical velocity of the center of mass at takeoff, in m/s
- `flight time`: time from takeoff to touchdown, in seconds
- `running integral`: acceleration × time step, added sample by sample. Use the trapezoid rule, which averages each pair of neighboring samples before multiplying by the time step (McMahon et al., 2018a).

Follow these steps for the takeoff velocity method:

1. Add the plate columns into one `force_n` column, and confirm the sampling rate from the time step. A step of 0.001 s means 1000 Hz.
2. Take the first 1 s of the trace. Calculate its mean as `body_weight_n` and its standard deviation as `bw_sd_n`.
3. Divide `body_weight_n` by 9.81 to get `body_mass_kg`.
4. Find the onset of movement: the first sample where `force_n` is below `body_weight_n - 5 × bw_sd_n`.
5. Find takeoff: the first sample after the push where `force_n` falls below your takeoff threshold.
6. For every sample up to takeoff, calculate `net_force_n = force_n - body_weight_n`.
7. Multiply each `net_force_n` by the time step and add them, from the first sample of quiet standing to takeoff, to get the net impulse in N·s. When body weight is the mean of the window where integration starts, that window adds zero net impulse.
8. Divide the net impulse by `body_mass_kg` to get takeoff velocity in m/s.
9. Calculate jump height as takeoff velocity² / (2 × 9.81).

For the flight time method, find takeoff and touchdown with the same threshold, subtract to get flight time in s, and calculate 9.81 × flight time² / 8.

**Worked example.** A simplified synthetic jump sampled at 1000 Hz, with force held constant inside each phase:

| Input | Value |
|---|---|
| Quiet standing | 1.000 s (1000 samples), alternating 784 N and 786 N |
| Dip (unweighting) | 0.250 s (250 samples) at 400 N |
| Push (braking and propulsion) | 0.400 s (400 samples) at 1500 N |
| Landing | Center of mass 0.02 m lower than at takeoff |

The calculation runs this way:

1. Mean quiet force = 785.00 N, standard deviation = 1.0005 N. Body mass = 785.00 / 9.81 = 80.0204 kg.
2. Onset threshold = 785.00 - 5 × 1.0005 = 780.00 N. Force first drops below it at sample 1000, which is 1.000 s.
3. Net impulse: dip (400 - 785.00) × 0.250 = -96.25 N·s, push (1500 - 785.00) × 0.400 = 286.00 N·s, total 189.75 N·s.
4. Takeoff velocity = 189.75 / 80.0204 = 2.3713 m/s.
5. Jump height = 2.3713² / (2 × 9.81) = 0.2866 m. The trapezoid rule on this step-shaped trace gives 2.3668 m/s and 0.2855 m.
6. Flight time method: had the athlete landed in the takeoff posture, flight time would be 0.4834 s, giving 0.2866 m. Landing 0.02 m lower makes it 0.4917 s, so 9.81 × 0.4917² / 8 = 0.2965 m.

Result: the takeoff velocity method gives 0.2866 m. The flight time method gives 0.2965 m for the same jump, 0.99 cm higher. This matches the 0.5 to 2 cm gap that Linthorne (2001) reports for jumps with hands on hips.

**Variants.** Use each method only where it fits:

- Takeoff velocity method: use it when you have the raw force-time trace. It depends on body weight and on finding takeoff.
- Flight time method: use it only when flight time is all you have. It assumes the athlete lands in the same body position as at takeoff. Athletes usually land with the center of mass 1 to 4 cm lower, so flight time reads high. With hands on hips, it overestimates height by 0.5 to 2 cm, and arm swing makes the gap larger (Linthorne, 2001).
- Work-energy method, also called impulse-displacement in some exports: it integrates twice to get displacement, so errors compound, and it is often the least reliable of the three (Linthorne, 2001). Do not use it unless the user asks, and never mix it with the other two.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Method: flight time reads 0.99 cm higher in the worked example.
- Body weight from another source, such as a scale or another trial: a body weight 10 N too high gives 0.2329 m instead of 0.2866 m when you integrate from the start of quiet standing, and 0.2606 m from the onset of movement. A body weight 10 N too low gives 0.3474 m and 0.3145 m. Linthorne (2001) reports a 2 to 3 cm error for a 10 N body weight error.
- Weighing window: shorter or noisier quiet periods give a less accurate body weight.
- Takeoff threshold: a 3 ms error in finding takeoff changes jump height by about 0.9 cm (McMahon et al., 2018a). Thresholds of 6 N and 10 N above true zero overestimated jump height by 1% and 1.5% (McMahon et al., 2018a).
- Filtering: filtered force data can underestimate CMJ height (McMahon et al., 2018a).
- Sampling rate: use at least 1000 Hz (McMahon et al., 2018a).
- Arm swing: arm swing raises jump height and makes the flight time error larger (Linthorne, 2001). In 18 men it raised takeoff velocity by 10% and the rise after takeoff by 21% (Harman et al., 1990). In elite volleyball players the gain in height was 38% (Vaverka et al., 2016). Keep the same arm condition at every test.
- Trial selection: the best trial and the mean of trials give different values.

**Units and typical range.** Report jump height in m or cm. Name the method and whether arm swing was allowed. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I men (n = 76), no arm swing (light bar across the shoulders), flight time method, mean of 2 trials | 0.36 ± 0.07 m (mean ± SD) | Sole et al., 2018 |
| NCAA Division I women (n = 75), no arm swing (light bar across the shoulders), flight time method, mean of 2 trials | 0.27 ± 0.06 m (mean ± SD) | Sole et al., 2018 |
| Professional male rugby league (n = 53), no arm swing (hands on hips), takeoff velocity method, mean of 3 trials | 0.35 ± 0.04 m (mean ± SD); lowest and highest RSI-modified groups (n = 20 each) 0.318 ± 0.032 m and 0.377 ± 0.039 m | McMahon et al., 2018b |

No takeoff velocity range is given, because jump height = takeoff velocity² / (2 × 9.81) carries the same information. If an export gives only takeoff velocity, convert it to height. Do not use peak velocity in its place. Velocity peaks about 0.03 s before takeoff and is 6 to 7% lower at takeoff (Harman et al., 1990), so peak velocity overstates height by about 13 to 16%.

Test variability from a separate-day retest, for judging a change in one athlete:

| Population and protocol | Typical error | Source |
|---|---|---|
| Elite male ice hockey players (n = 22), takeoff velocity method, hands on hips, best of 3 trials, retest 24 h later | 1.3 cm, coefficient of variation 3.1% | Godhe et al., 2025 |
| Adolescent cricket and netball athletes (n = 17), flight time method, hands on hips, mean of 3 trials, retest 1 week later | Coefficient of variation 2.63% | Thomas et al., 2017 |

These separate-day retests give a larger typical error than a same-day retest. Use them only when your method, trial summary, and athletes match. Otherwise, measure your own TE and judge a change with the shared noise band rules.

**Vendor equivalents.** The device files map these metrics:

- VALD ForceDecks `Jump Height (Imp-Mom)`: jump height from center of mass velocity at take-off and body mass, in cm. It is the same method. Take-off thresholds may differ, so values may differ slightly. VALD sources disagree on the take-off and landing threshold: the Technical Glossary V2.0 and the User Guide say 20 N, and the knowledge base pages say 30 N.
- VALD ForceDecks `Jump Height (Flight Time)`: jump height from flight time, in cm. It matches the flight time method and gives different values from `Jump Height (Imp-Mom)`.
- VALD ForceDecks `Jump Height (Imp-Dis)`: maximum center of mass displacement between take-off and landing, in cm. It is a third method. Do not mix it with the other two.
- VALD ForceDecks `Flight Time`: take-off to landing, in ms. Convert to seconds before you use the flight time formula.
- Hawkin `Jump Height(m)`: take-off velocity squared divided by 2 × 9.81, in m. It matches the takeoff velocity method. Integration starts at the traced-back start of movement: Hawkin finds the start when force falls 5 standard deviations of the weighing force below system weight, then traces back to the last sample at system weight. The reference method integrates from the start of quiet standing.
- Hawkin `System Weight(N)`: the lowest 1 s average of force in the weighing phase, found by an optimization loop that is not published. The reference method uses the mean of the first 1 s.
- Hawkin `Takeoff Velocity(m/s)`: net force divided by system mass, summed sample by sample from the start of movement.
- Hawkin `Flight Time(s)`: Hawkin does not turn it into a jump height. Multi rebound jump heights use the flight time method, so do not compare them with takeoff velocity jump heights. Merrigan et al. (2022) report Hawkin's take-off as force below 25 N for 30 ms.
- Perch `Jump Height`: apex head height minus standing head height, from camera head tracking. It measures head displacement, not center of mass displacement, and no comparison with force plates is published. Units are not published. The Perch file maps it to no reference file.

**Reference file.** [cmj-jump-height.md](../skills/force-plate/references/cmj-jump-height.md)

### Reactive strength index-modified

**What it measures.** Reactive strength index-modified (RSImod) shows how high an athlete jumps relative to how long the countermovement jump takes to produce. It was introduced as a version of the reactive strength index (RSI) that works for any vertical jump, not only the drop jump (Ebben & Petushek, 2010).

**Inputs.** The calculation needs these data:

- CMJ jump height in m, with its method named
- Time to takeoff in s, from the onset of movement to takeoff
- A force plate at least 1000 Hz, so the onset of movement can be found. A contact mat cannot give time to takeoff.

**Calculation.** Use this formula for the CMJ:

```text
RSImod (m/s) = jump height (m) / time to takeoff (s)
```

The terms mean the following:

- `jump height`: CMJ height in m, by the takeoff velocity or flight time method
- `time to takeoff`: time from the onset of movement to the instant the athlete leaves the plate, in s. It covers the unweighting, braking, and propulsion phases (McMahon et al., 2018a; Sole et al., 2018).

Follow these steps from raw inputs:

1. Convert jump height to meters as `jump_height_m`, and note the method.
2. Convert time to takeoff to seconds as `ttt_s`. Check that it runs from the onset of movement to takeoff.
3. From a raw trace, find the onset of movement and takeoff as in the CMJ breakdown, and subtract the two times.
4. Divide `jump_height_m` by `ttt_s`.
5. Use one trial summary, the best trial or the mean of trials, for every session.

**Worked example.** The same synthetic jump as the CMJ example, with onset of movement at 1.000 s and takeoff at 1.650 s:

1. Time to takeoff = 1.650 - 1.000 = 0.650 s.
2. RSImod with the takeoff velocity height = 0.2866 / 0.650 = 0.4409 m/s.
3. RSImod with the flight time height = 0.2965 / 0.650 = 0.4562 m/s.
4. Jump height left in centimeters gives 28.66 / 0.650 = 44.09, which is 100 times too large.

Result: RSImod is 0.4409 m/s with the takeoff velocity method and 0.4562 m/s with the flight time method.

**Variants.** RSImod and drop-jump measures are different metrics:

| Metric | Test | Formula |
|---|---|---|
| RSI-modified | Countermovement jump, from standing | jump height / time to takeoff |
| Drop-jump RSI | Drop jump: step off a box, land, and rebound | jump height / ground contact time |
| Reactive strength ratio | Drop jump | flight time / ground contact time, with no units |

Healy et al. (2018) call flight time divided by contact time the reactive strength ratio, to keep it apart from RSI. Never compare an RSImod value with a drop-jump RSI value or range. RSImod also differs between jump types, so compare CMJ with CMJ only (Ebben & Petushek, 2010).

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Jump height method: switching to flight time raises RSImod from 0.4409 to 0.4562 m/s.
- Onset of movement: finding onset 30 ms earlier gives 0.680 s and 0.4215 m/s. Finding it 30 ms later gives 0.620 s and 0.4622 m/s. Onset errors affect time-based measures more than jump height (McMahon et al., 2018a).
- Onset threshold: some protocols step back 30 ms from the 5 standard deviation threshold (Owen et al., 2014). Use the same rule at every test.
- Takeoff threshold: it changes both jump height and time to takeoff (McMahon et al., 2018a).
- Arm swing and jump type: RSImod differs between jump types (Ebben & Petushek, 2010). The ranges below come from jumps without arm swing: a light bar across the shoulders (Sole et al., 2018) or hands on hips (McMahon et al., 2018b). In basketball players, arm swing raised RSImod by 20 to 24% (Heishman et al., 2019).
- Trial summary: the mean of trial RSImod values differs from mean jump height divided by mean time to takeoff.

**Units and typical range.** Report RSImod in m/s and name the jump height method. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I men, CMJ without arm swing (light bar across the shoulders), flight time jump height, 10 N threshold | 0.424 ± 0.102 m/s (mean ± SD); observed range 0.208 to 0.704 m/s | Sole et al., 2018 |
| NCAA Division I women, CMJ without arm swing (light bar across the shoulders), flight time jump height, 10 N threshold | 0.314 ± 0.089 m/s (mean ± SD); observed range 0.135 to 0.553 m/s | Sole et al., 2018 |
| Professional male rugby league, CMJ without arm swing (hands on hips), takeoff velocity jump height, lowest and highest groups | 0.36 ± 0.03 and 0.53 ± 0.05 m/s (mean ± SD) | McMahon et al., 2018b |

Sole et al. (2018) used a 10 N threshold for both onset and takeoff, not the 5 standard deviation rule. Time to takeoff averaged 0.868 ± 0.105 s for men and 0.870 ± 0.114 s for women (Sole et al., 2018), and 0.707 to 0.881 s across the rugby league groups (McMahon et al., 2018b). In a separate-day retest of adolescent cricket and netball athletes (n = 17, mean of 3 trials, 1 week apart), the coefficient of variation of RSImod was 6.11% and the standard error of measurement was 0.03 m/s (Thomas et al., 2017).

**Vendor equivalents.** The device files map these metrics:

- VALD ForceDecks `Contraction Time`: start of movement to take-off, in ms. It equals time to takeoff.
- VALD ForceDecks `RSI-modified`: `Jump Height (Flight Time)` divided by `Contraction Time`, in m/s. It uses flight time jump height.
- VALD ForceDecks `RSI-modified (Imp-Mom)`: `Jump Height (Imp-Mom)` divided by `Contraction Time`, in m/s. It is not interchangeable with `RSI-modified`.
- Hawkin `mRSI` (CMJ) and `CMJ Modified RSI`: `Jump Height` divided by `Time To Takeoff`. It matches RSImod with takeoff velocity jump height, so it matches VALD `RSI-modified (Imp-Mom)`, not VALD `RSI-modified`.
- Hawkin `Time To Takeoff(s)`: take-off time minus start time, in s. The start is traced back to system weight, with no fixed 30 ms step. In the drop jump, `Time To Takeoff` is contact time.
- Hawkin `RSI` (CMJ): `Flight Time` divided by `Time To Takeoff`, with no unit. It is neither RSImod nor drop-jump RSI. VALD calls it `Flight Time:Contraction Time`.
- Hawkin `mRSI` (drop jump): takeoff velocity jump height divided by contact time. This is drop-jump RSI, not RSImod. Hawkin `RSI` (drop jump) is flight time divided by contact time, the reactive strength ratio.
- Perch `RSIMod`: `Jump Height ÷ Time To Takeoff`, with no unit by Perch's choice, for CMJ (Arms Fixed), CMJ (Arms Swing), and Continuous Jumps. Perch `Time To Takeoff` runs from the start of unweighting to takeoff, when the head returns to standing height. Both come from head tracking. The Perch file maps them to no reference file.
- GymAware RSI: `Jump Height / Ground Contact Time` for drop jumps and rebound jumps, in m/s. That is the drop-jump RSI form, not RSImod. Landing and takeoff detection is not published.

**Reference file.** [rsi-modified.md](../skills/force-plate/references/rsi-modified.md)

### Isometric mid-thigh pull peak force

**What it measures.** Isometric mid-thigh pull (IMTP) peak force is the highest vertical force an athlete produces while pulling as hard and fast as possible on a fixed bar at mid-thigh height. "Isometric" means the bar does not move.

**Inputs.** The calculation needs these data:

- The vertical force trace in N with a time column in s, summed across both plates
- A quiet period of at least 1 s with the athlete in the pull position and strapped to the bar
- At least two clean trials, with more until peak forces are within 250 N of each other (Comfort et al., 2019)
- The knee angle, hip angle, and bar height, kept the same at every test

**Calculation.** Four versions are in use. Name the version in every result, because they differ by hundreds of newtons or by a factor of 9.81:

```text
gross peak force (N)               = highest vertical force during the pull
net peak force (N)                 = gross peak force - body weight
relative peak force (N/kg)         = peak force / body mass
allometric peak force (N/kg^0.67)  = peak force / body mass^0.67
RFD 0-X ms (N/s)                   = (force at X ms after onset - force at onset) / (X / 1000)
```

The terms mean the following:

- `vertical force`: the force the plate measures, in N. Sum both plates.
- `body weight`: mean vertical force during the quiet period before the pull, in the pull position and strapped to the bar, in N (Comfort et al., 2019)
- `gross peak force`: peak force that includes body weight
- `net peak force`: peak force with body weight removed (Comfort et al., 2019). Neither net nor gross is agreed to be better. Always report which one you used.
- `body mass`: body weight in N divided by 9.81, in kg
- `relative peak force`: peak force divided by body mass, also called ratio scaling. State net or gross.
- `allometric peak force`: peak force divided by body mass raised to a power. The power 0.67 is recommended for force (Jaric, 2002) and has been used for IMTP force (Kraska et al., 2009). Always state the power.
- Onset of the pull: the first sample above body weight + 5 standard deviations of body weight, from a 1 s quiet period (Comfort et al., 2019; Dos'Santos et al., 2017)

Follow these steps from a raw trace:

1. Take the 1 s quiet period. Calculate its mean as `body_weight_n` and its standard deviation as `bw_sd_n`.
2. If force changes by more than 50 N during the quiet period, reject the trial (Comfort et al., 2019).
3. Divide `body_weight_n` by 9.81 to get `body_mass_kg`.
4. Find the onset: the first sample where `force_n` is above `body_weight_n + 5 × bw_sd_n`.
5. Find the highest `force_n` between onset and the end of the pull. This is gross peak force.
6. Subtract `body_weight_n` to get net peak force.
7. Repeat for each trial. Apply your trial rule, the best trial or the mean of trials, and state it.
8. Divide by `body_mass_kg` for relative peak force, or by `body_mass_kg` raised to 0.67 for allometric peak force. Name net or gross.
9. For RFD, read force at onset and at each fixed time after onset, then apply the RFD formula.

**Worked example.** A simplified synthetic pull sampled at 1000 Hz:

| Input | Value |
|---|---|
| Quiet period | 1.000 s, alternating 832 N and 836 N |
| Gross peak force, trials 1 to 3 | 2905 N, 2610 N, 2840 N |
| Force at onset | 846 N |
| Force at 50, 100, 150, 200, 250 ms after onset | 1120, 1490, 1820, 2080, 2260 N |

The calculation runs this way:

1. Mean quiet force = 834.00 N, standard deviation = 2.0010 N. Body mass = 834.00 / 9.81 = 85.0153 kg. Onset threshold = 834.00 + 5 × 2.0010 = 844.01 N.
2. The three trials span 295 N, more than 250 N. The two highest, 2905 N and 2840 N, are 65 N apart, so no more trials are needed. With the best-trial rule, report 2905 N.
3. Gross peak force = 2905.0 N. Net peak force = 2905.0 - 834.0 = 2071.0 N.
4. Relative gross = 2905.0 / 85.0153 = 34.17 N/kg. Relative net = 2071.0 / 85.0153 = 24.36 N/kg.
5. Allometric gross = 2905.0 / 85.0153^0.67 = 148.0 N/kg^0.67. Allometric net = 105.5 N/kg^0.67.
6. RFD 0-50 ms = (1120 - 846) / 0.050 = 5480 N/s. RFD 0-100, 0-150, 0-200, and 0-250 ms are 6440, 6493, 6170, and 5656 N/s.

Result: the same pull is 2905.0 N gross, 2071.0 N net, 34.17 or 24.36 N/kg relative, and 148.0 or 105.5 N/kg^0.67 allometric. Each label is needed to read the number.

**Variants.** The four peak force versions above are the variants. For rate of force development, follow these rules:

- Use fixed time windows from onset, such as 0-50, 0-100, 0-150, 0-200, and 0-250 ms. These were reliable (Haff et al., 2015; Comfort et al., 2019).
- Do not use average RFD, peak force divided by time to peak force. It failed reliability standards (Haff et al., 2015).
- If you report peak RFD, name the sampling window. Published methods used windows from 2 to 50 ms. Only peak RFD from a 20 ms moving window was reliable (Comfort et al., 2019, citing Haff et al., 2015).
- Expect RFD to be less reliable than peak force (Maffiuletti et al., 2016).

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Net or gross force: the gap is the full body weight, 834.0 N.
- Scaling: ratio scaling and allometric scaling give different values (Comfort et al., 2019).
- Dividing by body weight in N instead of body mass in kg: this gives 3.483 with no units, instead of 34.17 N/kg.
- Onset threshold: fixed thresholds such as 75 N or 10% of body weight above body weight move the onset later than 5 standard deviations, and change time-specific force and RFD (Dos'Santos et al., 2017). In a second synthetic pull, a threshold 75 N above body weight moved onset 4 ms later and raised force at 100 ms from 2012.4 N to 2041.7 N.
- Posture: knee and hip angles change force output (Comfort et al., 2019).
- Sampling rate and filtering: these change early force-time measures most (Comfort et al., 2019).
- RFD method: fixed windows, peak RFD, and average RFD give different values with different reliability (Haff et al., 2015).
- Pre-tension: pulling on the bar before the start changes the measured body weight and the onset (Comfort et al., 2019).

**Units and typical range.** Report peak force in N, relative force in N/kg, and allometric force in N/kg^0.67. Name net or gross, and the knee and hip angles. The file gives no published range, because peak force depends on body mass, sex, training, posture, and whether body weight is included. Run these internal checks instead:

- Net peak force is smaller than gross by exactly one body weight: 2905.0 - 2071.0 = 834.0 N.
- Gross peak force is above body weight.
- The trials you used are within 250 N of each other (Comfort et al., 2019).
- A relative value is not 9.81 times too small.

The file sets these protocol figures: knee angle of 125 to 145° and hip angle of 140 to 150°; IMTP data can be collected accurately at 500 Hz, with at least 1000 Hz for early force-time measures (Comfort et al., 2019). In a separate-day retest of elite male ice hockey players (n = 21 for this test, hip and knee angles of about 145°, best of 3 trials, 24 h apart), the standard error of measurement of peak force was 104 N, a coefficient of variation of 3.1% (Godhe et al., 2025).

**Vendor equivalents.** The device files map these metrics:

- VALD ForceDecks `Peak Vertical Force [N]` (IMTP test): the highest force in the pull. VALD does not publish whether it includes body weight, so confirm gross or net before you compare with published values. VALD also reports `Peak Vertical Force / BM [N/kg]`, `Peak Vertical Force [N] Asymmetry`, and `Start Time to 80% Peak Force`.
- Hawkin `Peak Force(N)` (isometric test): the highest combined force, including body weight. It is gross peak force.
- Hawkin `Net Peak Force(N)`: `Peak Force` minus `System Weight`. It is net peak force. System weight includes any pretension on the bar (Merrigan et al., 2022).
- Hawkin `Relative Peak Force(%)`: peak force divided by this trial's system weight, as a percentage. It is not N/kg. N/kg = % × 9.81 / 100 when the same weight is used.
- Hawkin `Relative Peak Force (BW)(N/kg)`: peak force divided by the athlete's last known body weight, a stored weight, not this trial's.
- Hawkin `RFD 0-50 ms(N/s)` to `RFD 0-250 ms(N/s)`, `Force at 50 ms(N)` to `Force at 250 ms(N)`, and `Time to Peak Force(s)`: the average slope from 0 ms to the window end. Fixed windows match the reference method. Merrigan et al. (2022) report a start-of-pull rule of 5 standard deviations above body weight, which Hawkin's own pages do not state. The API dictionary reports `Initiation Threshold`, 3 standard deviations of the quiet period, as a quality check.

**Reference file.** [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md)

### Eccentric hamstring force

**What it measures.** Eccentric hamstring force is the peak force each leg produces at the ankle while the athlete resists falling forward during the Nordic hamstring exercise. "Eccentric" means the muscle is producing force while it lengthens. The athlete kneels with both ankles held in place and lowers the upper body forward as slowly as possible, and a sensor at each ankle records force (Opar et al., 2013; Bourne et al., 2015). The value is a force at the ankle in N, not a hamstring muscle force and not a knee torque. Do not calculate knee torque or muscle force from it.

**Inputs.** The calculation needs these data:

- One row per repetition with `athlete_id`, `test_date`, `side` (left or right), and `peak_force_n`, with side labels checked against the device file
- `body_mass_kg` measured on the test day
- A warm-up set, then three maximal repetitions (Bourne et al., 2015)

**Calculation.** Calculate each leg separately:

```text
peak force, per leg (N)          = highest force on that leg's sensor in the best repetition
relative force, per leg (N/kg)   = peak force / body mass
two-limb average (N)             = (left peak force + right peak force) / 2
between-limb imbalance (%)       = (stronger leg - weaker leg) / stronger leg x 100, with the weaker side named
```

The terms mean the following:

- `peak force`: the highest force in N from one leg's sensor during one repetition. The best of three repetitions has been used (Bourne et al., 2015). Opar et al. (2015) used the mean of the three peaks.
- `body mass`: the athlete's mass in kg on the test day
- `two-limb average`: the mean of left and right peak force (Bourne et al., 2015)
- `stronger leg`, `weaker leg`: the legs with the higher and lower peak force on that day
- `between-limb imbalance`: the percentage by which the weaker leg falls short of the stronger leg. It equals the size of the signed percentage difference in the limb symmetry breakdown.

Follow these steps from repetition-level data:

1. Flag repetitions that did not reach a clear peak followed by a fast drop in force (Bourne et al., 2015).
2. For each athlete, date, and side, keep the highest `peak_force_n` among the valid repetitions.
3. Divide each leg's peak by `body_mass_kg` from the same day.
4. Average the left and right peaks.
5. Calculate the imbalance, and record which side is weaker.
6. For each earlier test the user cites, including a pre-injury baseline, subtract the earlier value from the new value for each leg. Compare each change with the noise band, 1.96 × TE × √(1 + 1/n), where n is the number of tests in the baseline mean.
7. To judge the imbalance, compare the left-right difference in N with the asymmetry band, 1.96 × √(SE_left² + SE_right²).

**Worked example.** One athlete's Nordic test:

| Input | Value |
|---|---|
| Left leg, repetitions 1 to 3 | 310 N, 325 N, 318 N |
| Right leg, repetitions 1 to 3 | 352 N, 360 N, 347 N |
| Body mass on the test day | 82 kg |
| Left leg best at the previous test | 300 N |

The calculation runs this way:

1. Best repetition per leg: left 325 N, right 360 N.
2. Relative force: left 325 / 82 = 3.96 N/kg, right 360 / 82 = 4.39 N/kg.
3. Two-limb average = (325 + 360) / 2 = 342.5 N, which is 4.18 N/kg.
4. Imbalance = (360 - 325) / 360 × 100 = 9.72%, with the left leg weaker.
5. Change in the left leg = 325 - 300 = 25 N. With TE = 21.7 N, the lowest value Opar et al. (2013) reported, and one earlier test, the band is 1.96 × 21.7 × √2 = 60.1 N. With TE = 27.5 N, it is 76.2 N. These equal the minimal detectable change values Opar et al. (2013) reported. The 25 N change is inside both bands.
6. Left-right difference = 35 N. With SE = TE = 21.7 N for each leg, the band is 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the stronger leg. The 35 N difference is inside the band.

Result: neither the 25 N change nor the 35 N difference can be told apart from measurement noise with these data. This does not show that the legs are equal or that nothing changed.

**Variants.** The imbalance formula above is one of several:

- Log ratio: 100 × ln(right / left). Injury studies on this test did not use the imbalance formula above. They used a left-to-right ratio, log-transformed and back-transformed to a percentage (Opar et al., 2015; Bourne et al., 2015). Neither paper prints the equation for one athlete. The log ratio keeps the same size whichever leg is stronger. Offer it as an option.
- Other asymmetry formulas give different numbers from the same legs (Bishop et al., 2018). Never compare an imbalance value with a published value calculated another way.
- For the SE in the asymmetry band, use SE = TE for single or best repetitions. For a mean of k repetitions, use a pooled squad coefficient of variation × the leg's value / √k. Take TE or the coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own repetitions or from the same repetitions you are judging.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Imbalance formula: the formula above gives 9.72%. Dividing by the left leg gives 10.77%. Dividing by the sum of both legs gives 5.11%. The log ratio gives 10.23%. The left-to-right ratio is 0.903.
- Noise estimate: with the mean of 3 repetitions (317.7 N and 353.0 N) and an assumed pooled squad coefficient of variation of 5%, each leg's SE is 9.17 N and 10.19 N. The asymmetry band shrinks to 26.9 N, and the 35.3 N difference is outside it. The choice of SE decides the answer, so state it.
- Multiplier: Opar et al. (2013) had 30 athletes. Using t with 29 degrees of freedom, 2.045, raises the change band from 60.1 N to 62.8 N.
- Best repetition or mean of repetitions: with the mean, the imbalance is 10.01%.
- Body mass: the same 325 N is 4.06 N/kg at 80 kg and 3.96 N/kg at 82 kg.
- Summing legs: adding both legs gives 685 N, which is not a per-leg value.
- Device: a Nordic device and an isokinetic dynamometer give different values and side-to-side ratios for the same athlete (Wiesinger et al., 2020).
- Repetition quality: repetitions without a clear peak, or with a broken position, lower or raise the peak.

**Units and typical range.** Report peak force in N per leg, relative force in N/kg, and imbalance in % with the weaker side named. In recreationally active men with no history of hamstring strain, peak force was left 344.7 ± 61.1 N and right 361.2 ± 65.1 N (mean ± SD) (Opar et al., 2013). In that sample, 30 men completed the test on 2 separate occasions. Typical error was 21.7 to 27.5 N, 5.8 to 8.5% as a coefficient of variation, and the minimal detectable change at 95% confidence was 60.1 to 76.2 N (Opar et al., 2013). Side-to-side strength ratios from this test had low reliability (Wiesinger et al., 2020), so treat a single imbalance value with caution.

Keep these limits:

- Do not use published injury studies to predict injury for one athlete. Those studies report group-level associations in specific cohorts, and their findings on imbalance disagree (Opar et al., 2015; Bourne et al., 2015).
- Do not quote injury-study cut-offs, such as force or imbalance cut-offs from Opar et al. (2015) or Bourne et al. (2015), as targets or flags for one athlete. The cut-offs did not replicate. Later cohorts found a different force cut-off, 337 N in soccer (Timmins et al., 2016), or no link with Nordic strength (van Dyk et al., 2017). A meta-analysis of six cohorts (1100 players) found no difference in pre-season Nordic strength or imbalance between players who later had a hamstring injury and those who did not (Opar et al., 2021).
- When a difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal or that the athlete has recovered."

**Vendor equivalents.** The device files map these metrics:

- VALD NordBord `leftMaxForce`, `rightMaxForce`: peak force at the ankle hook for each leg. VALD states the unit as N, which is not confirmed in the API. It is force at the ankle, not hamstring muscle force.
- VALD NordBord `leftAvgForce`, `rightAvgForce`: in the NordBord app, the average of the peaks of all repetitions in the test. Whether the API field uses the same rule is not confirmed.
- VALD NordBord `leftMaxForcePerKg`, `rightMaxForcePerKg`: peak force divided by body mass, in N/kg. Body weight is entered in the NordBord app or pulled from VALD Hub. Check which body weight was entered or pulled.
- VALD NordBord `leftTorque`, `rightTorque`: force multiplied by the lever arm from the knee to the ankle hook, which the device estimates from the knee position setting, in N·m as VALD states it, not confirmed in the API. Report it as given, labeled as the device's value. It depends on the knee position setting.
- VALD NordBord imbalance (in the app only): described as the percentage difference between left and right maximums, with a second imbalance from left and right averages. VALD does not publish the formula. A VALD research summary used `|L − R| / (L + R)` for hamstring asymmetry, which differs from the ForceDecks glossary formula, and VALD does not say which one the app uses. The API has no imbalance field. Compute imbalance yourself with a stated formula.

**Reference file.** [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md)

## Velocity-based training

These metrics come from a bar speed device, such as a linear position transducer, an accelerometer, or a camera system. Velocity is in metres per second (m/s). The concentric phase is the lifting part of a rep. The eccentric phase is the lowering part. 1RM is the one-repetition maximum, the heaviest load the athlete can lift once.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Mean concentric velocity (MV) | `concentric displacement_m ÷ concentric duration_s` | m/s | [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md) |
| Mean propulsive velocity (MPV) | Mean of velocity from the start of the concentric phase until acceleration first drops below −9.81 m/s² | m/s | [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md) |
| Peak velocity (PV) | Highest velocity sample in the concentric phase | m/s | [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md) |
| Load-velocity profile | `velocity_m_s = intercept + slope × load_kg` | m/s | [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md) |
| Estimated 1RM | `estimated_1rm_kg = (v1rm_m_s − intercept) ÷ slope` | kg | [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md) |
| Velocity loss | `velocity_loss_pct = (v_reference − v_last) ÷ v_reference × 100` | % | [velocity-loss.md](../skills/velocity-based-training/references/velocity-loss.md) |
| Stopping velocity | `stop_velocity_m_s = v_reference × (1 − threshold_pct ÷ 100)` | m/s | [velocity-loss.md](../skills/velocity-based-training/references/velocity-loss.md) |

### Mean concentric velocity

**What it measures.** Mean concentric velocity is the average speed of the bar, or the body, during the lifting part of a rep. The reference file also covers two related measures, mean propulsive velocity and peak velocity, and the load-velocity profile built from them.

**Inputs.** The calculation needs these data:

- The device's per-rep MV, MPV, or PV, or a velocity-time trace if no per-rep values exist
- The unit of each velocity column. Convert cm/s ÷ 100 and ft/s × 0.3048 to m/s.
- For a load-velocity profile, the load in kg and the fastest rep at each load, per athlete, exercise, and equipment
- For a 1RM estimate, a published 1RM velocity for the same lift and equipment

**Calculation.** Three velocity measures are in common use. They give different numbers for the same rep:

```text
mean concentric velocity (MV)  = concentric displacement_m ÷ concentric duration_s
mean propulsive velocity (MPV) = mean of velocity from the start of the concentric phase
                                 until acceleration first drops below −9.81 m/s²
peak velocity (PV)             = highest velocity sample in the concentric phase
velocity_m_s     = intercept + slope × load_kg
estimated_1rm_kg = (v1rm_m_s − intercept) ÷ slope
```

The terms mean the following:

- `concentric displacement_m`: how far the bar travels upward during the concentric phase, in metres
- `concentric duration_s`: how long the concentric phase lasts, in seconds
- `MV`: also written MCV. With samples at a fixed rate, it equals the average of the velocity samples in the concentric phase.
- `MPV`: the propulsive phase ends when the bar decelerates faster than gravity (−9.81 m/s²). The part after that is the braking phase (Weakley et al., 2021a; Sanchez-Medina et al., 2010). When acceleration never drops below −9.81 m/s², MPV equals MV.
- `PV`: the single highest instant in the concentric phase
- `load_kg`: the load lifted. Percent of 1RM also works.
- `slope`: change in velocity per kilogram, in m/s per kg. It is negative.
- `intercept`: the velocity the line predicts at zero load
- `v1rm_m_s`: the velocity at 1RM, also called the minimum velocity threshold, the mean velocity of a successful 1RM lift

A value you recalculate from a trace depends on the phase start and end, the acceleration rule (the file uses a forward difference, `(v[i+1] − v[i]) ÷ dt`), whether the sample before braking is in the propulsive phase, and whether you average the samples or integrate over time. Label any recalculated value "recalculated", state the conventions, and never compare it with device values or published tables.

Follow these steps from raw inputs:

1. Identify which measure each column holds: MV, MPV, or PV. Use the device's per-rep values if they exist.
2. To recalculate, find the start and end of the concentric phase. Starting when upward velocity begins and ending when it returns to zero is common practice, not a published rule. State the rule.
3. For MV, divide the concentric displacement by the concentric duration.
4. For MPV, work out acceleration with a forward difference. Find the first value below −9.81 m/s². Average the velocity samples up to and including the sample before it.
5. For PV, take the highest velocity sample in the concentric phase.
6. For a load-velocity profile, keep the fastest rep at each load, and fit a straight line of velocity against load.
7. To estimate 1RM, confirm the lift has a published 1RM velocity and validation, and solve the line for the load at that velocity. Do not estimate 1RM for the squat or deadlift.
8. Label every result with the measure, the device, the exercise variant, the equipment, and the units.

**Worked example.** One back squat rep recorded at 20 Hz (one sample every 0.05 s), with concentric velocity samples of 0.10, 0.35, 0.60, 0.80, 0.95, 1.05, 1.12, 1.16, 1.18, 1.15, 1.05, 0.55, and 0.05 m/s. Treating each sample as one 0.05 s step:

1. Concentric duration: 13 samples × 0.05 s = 0.65 s.
2. Displacement: velocity sum 10.11 m/s × 0.05 s = 0.5055 m.
3. MV: 0.5055 m ÷ 0.65 s = 0.778 m/s.
4. PV: 1.18 m/s.
5. Acceleration between samples, m/s²: 5.0, 5.0, 4.0, 3.0, 2.0, 1.4, 0.8, 0.4, −0.6, −2.0, −10.0, −10.0. The first value below −9.81 m/s² comes after sample 11.
6. The propulsive phase is samples 1 to 11, lasting 0.55 s, with a velocity sum of 9.51 m/s. MPV: 9.51 ÷ 11 = 0.865 m/s.

The same 13 samples give these values under other conventions:

| Convention | MV, m/s | MPV, m/s |
|---|---|---|
| Sample mean, sample 11 in the propulsive phase | 0.778 | 0.865 |
| Same, sample 11 left out of the propulsive phase | 0.778 | 0.846 |
| Time integral by trapezoid, first to last sample | 0.836 | 0.894 |
| Zero-velocity sample added at each end, trapezoid from zero to zero | 0.722 | 0.817 |

The MV values span 0.114 m/s for one rep, more than the smallest detectable difference of 0.06 to 0.08 m/s. In a second trace that slows more gently, MPV equals MV (0.747 m/s).

One athlete's Smith machine bench press profile used loads of 40, 50, 60, 70, and 80 kg, with fastest-rep MV of 1.01, 0.84, 0.70, 0.56, and 0.39 m/s:

1. The fitted line is velocity = 1.612 − 0.0152 × load, with a correlation of −0.9992.
2. With the group 1RM velocity of 0.17 m/s: (0.17 − 1.612) ÷ −0.0152 = 94.9 kg. The loads were 42.2% and 84.3% of that estimate, and the heaviest load is 14.9 kg below it.
3. With a 1RM velocity of 0.10 m/s, the free-weight bench press value: 99.5 kg.
4. With only the 40 kg and 80 kg points (2-point method): velocity = 1.63 − 0.0155 × load, and the estimate at 0.17 m/s is 94.2 kg.

Result: the same rep is 0.778 m/s (MV), 0.865 m/s (MPV), or 1.18 m/s (PV). The same five lifts give 1RM estimates 4.6 kg apart, depending only on the 1RM velocity.

**Variants.** Use each measure for these purposes:

- Mean velocity: Weakley et al. (2021a) prefer it to estimate 1RM. It is more reliable than MPV with light loads, varies less between devices than PV, and gives a more linear load-velocity relationship.
- Mean propulsive velocity: use it when the device or a published table reports MPV. Above about 70% of 1RM, MV and MPV give virtually the same information (Weakley et al., 2021a). In the bench press, the braking phase disappeared at 76.1 ± 7.4% of 1RM (Sanchez-Medina et al., 2010).
- Peak velocity: Weakley et al. (2021a) recommend it for ballistic lifts, where the bar or body leaves contact. García-Ramos et al. (2018) found MV predicted relative load best in the Smith machine bench press throw, with a standard error of the estimate of 3.80% to 4.76% of 1RM, while PV was the most repeatable. The sources conflict. Ask which measure the program uses.
- Load-velocity profile: record mean velocity at about 5 submaximal loads and fit a linear regression (Weakley et al., 2021a). A 2-point method at about 45% and 85% of 1RM is a shorter option, confirmed only for the bench pull, bench press, lat pull-down, and seated cable row.
- 1RM estimate: use only for a lift with a published 1RM velocity and validation. Weakley et al. (2021a) state that velocity cannot give an accurate 1RM estimate in lower-body lifts such as the squat or deadlift. In the file, that leaves the bench press and the prone bench pull. Name the equipment behind the 1RM velocity.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Velocity measure: one rep is 0.778, 0.865, or 1.18 m/s. Never compare MV with MPV or PV.
- Calculation conventions: recalculated MV ranges from 0.722 to 0.836 m/s for one rep.
- Load: MV and MPV differ most at light loads, because the braking phase disappears near 76% of 1RM (Sanchez-Medina et al., 2010).
- Device: linear position transducers showed greater accuracy and reliability than other device types (Weakley et al., 2021b).
- Exercise and technique: the load-velocity relationship differs by exercise, by technique, and by sex (Weakley et al., 2021a). A Smith machine squat profile does not apply to a free-weight squat.
- Range of motion: partial reps change velocity. This is common practice, not a cited finding.
- 1RM velocity: 0.17 m/s and 0.10 m/s give bench press estimates 4.6 kg apart. The individual 1RM velocity in the free-weight back squat was unreliable between days, with a coefficient of variation of 22.5% (Banyard et al., 2017).
- Which rep at each load: Weakley et al. (2021a) record the fastest rep. The first or the average rep gives a different line.
- Effort and rep detection: compare velocity only across reps lifted with maximal intent, and check the rep count against the training log. Both are common practice, not cited findings.

**Units and typical range.** Velocity is in m/s. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Smith machine bench press, velocity at 1RM, mean propulsive velocity, 120 trained men | 0.16 ± 0.04 m/s (mean ± SD) | González-Badillo & Sánchez-Medina, 2010 |
| Bench press, mean velocity at 1RM, across 4 studies | 0.10 to 0.17 m/s, with 0.17 m/s as a group value. Three studies used a Smith machine. The one free-weight study gave 0.10 m/s. | Weakley et al., 2021a |
| Squat, mean velocity at 1RM, across 4 studies | 0.23 to 0.32 m/s, with 0.30 m/s as a group value. The free-weight studies gave 0.23 and 0.24 m/s. | Weakley et al., 2021a |
| Free-weight back squat, mean velocity at 1RM, 17 trained men | 0.24 ± 0.06 m/s, coefficient of variation 22.5% between days | Banyard et al., 2017 |
| Deadlift, mean velocity at 1RM | 0.14 to 0.16 m/s, with 0.15 m/s as a group value. No validated 1RM estimate. | Weakley et al., 2021a |
| Prone bench pull, mean velocity at 1RM, across 3 studies | 0.48 to 0.52 m/s, with 0.50 m/s as a group value | Weakley et al., 2021a |
| Smith machine full squat, target MPV of the first rep, young men | 0.82 m/s at about 70%, 0.75 at about 75%, 0.68 at about 80%, 0.60 at about 85% of 1RM | Pareja-Blanco et al., 2017 |
| Between-day variation, Smith machine bench press throw, 30 men | PV 3.50% to 3.87%, MV 4.05% to 4.93%, MPV 5.11% to 6.03% (coefficient of variation) | García-Ramos et al., 2018 |
| Smallest detectable difference, free-weight back squat | MV 0.06 to 0.08 m/s. PV 0.11 to 0.19 m/s. MPV 0.08 to 0.11 m/s. | Weakley et al., 2021a |

The smallest detectable difference is a study value, not a rule for flagging one athlete's change. For your own athletes, judge a change with a typical error from the same exercise, equipment, device, and measure, and the shared noise band rules.

**Vendor equivalents.** The device files map these metrics:

- GymAware `meanVelocity` (set, best rep) and Conc Mean Velocity (rep): the sum of point velocities divided by the number of concentric points, with v = (d2 - d1) / (t2 - t1), in m/s. The phase starts "where the displacement rapidly changes", not at the lowest point, and runs to the top of the bar path. Olympic lift catches are excluded. It is mean velocity, not mean propulsive velocity. The set field comes from the best rep, not the set average or necessarily the fastest rep. GymAware samples at a variable rate, down-sampled to at most 50 points per second.
- GymAware `peakVelocity` (set, "peak rep") and Conc Peak Velocity (rep): an instantaneous value over a sample period of about 20 ms. The reference takes the highest velocity sample. The set field can come from a different rep than `meanVelocity`.
- GymAware mean propulsive velocity: not provided. Do not label GymAware mean velocity as MPV.
- GymAware 1RM estimate: a linear load-velocity line. The bench press example uses a minimum velocity threshold of 0.16 m/s. No API field carries the estimate.
- Perch `Mean Velocity`: displacement on the Z axis from the bottom of the rep to the top, divided by the time between those two points, in m/s. The form matches the reference, but the path comes from a camera. For Olympic lifts, only the propulsive phase is used.
- Perch `Mean Propulsive Velocity`: `MPV = (P1 - P0) / (t1 - t0)` over the propulsive phase. Perch does not publish how it finds the end of the phase, so do not assume it matches the −9.81 m/s² rule.
- Perch `Peak Velocity`: the largest velocity between any two consecutive coordinates, from the lowest to the highest point. It is a single-frame difference, sensitive to noise. The frame rate and any smoothing are not published.
- Perch Estimated 1RM (e1RM) and MVT: a load-velocity line fitted through set history, read at the minimum velocity threshold. Every tracked exercise has a default MVT, and the default values are not published. A higher MVT lowers e1RM. Perch can show an e1RM for a squat or deadlift, which the reference file says not to report from velocity. Which rep Perch uses at each load is not stated. Perch pages disagree on when a profile starts: two loads more than 30 lb apart on one page, and 40 lb or more across multiple sessions on another.

**Reference file.** [mean-concentric-velocity.md](../skills/velocity-based-training/references/mean-concentric-velocity.md)

### Velocity loss

**What it measures.** Velocity loss is how much slower an athlete's reps get from the best rep of a set to the last rep, as a percentage of the best rep. It is used as a sign of fatigue within the set and of how close the athlete came to failure. In strength-trained men, velocity loss correlated with peak blood lactate (r = 0.93 to 0.97) and with loss of jump height after squat sessions (r = 0.91 to 0.97) (Sánchez-Medina & González-Badillo, 2011). These links support its use as a fatigue indicator. They do not make it a diagnosis of fatigue, overtraining, or injury risk.

**Inputs.** The calculation needs these data:

- One velocity value per rep, with one velocity measure for the whole set
- Rep numbers stored as numbers, grouped by athlete, date, exercise, and set
- At least 2 reps in the set

**Calculation.** Calculate velocity loss as the percent drop from the reference rep to the last rep:

```text
velocity_loss_pct = (v_reference − v_last) ÷ v_reference × 100
stop_velocity_m_s = v_reference × (1 − threshold_pct ÷ 100)
```

The terms mean the following:

- `v_reference`: the velocity of the reference rep, in m/s. Use the fastest rep of the set by default.
- `v_last`: the velocity of the last completed rep of the set, in m/s
- `velocity_loss_pct`: the result, in percent
- `stop_velocity_m_s`: the velocity at which a set reaches a chosen threshold, worked out before the set

Follow these steps from raw inputs:

1. Convert the velocity column to m/s, and confirm which measure it holds.
2. Group the reps by athlete, date, exercise, and set.
3. Convert rep numbers to numbers, then sort the reps by rep number. Text sorts "10" before "2".
4. Find the reference rep, the fastest by default. If the fastest rep is not the first, also report the first-rep loss and flag the set.
5. Find the last completed rep. Leave out any failed rep with no recorded velocity.
6. Calculate `(v_reference − v_last) ÷ v_reference × 100`.
7. Label each result with the reference rep, the velocity measure, and the unit.

**Worked example.** One set of 8 back squat reps, with mean velocity of 0.66, 0.70, 0.68, 0.65, 0.62, 0.59, 0.55, and 0.53 m/s:

1. With the fastest rep (0.70 m/s, rep 2): 0.70 − 0.53 = 0.17 m/s, and 0.17 ÷ 0.70 × 100 = 24.3%.
2. With the first rep (0.66 m/s): 0.66 − 0.53 = 0.13 m/s, and 0.13 ÷ 0.66 × 100 = 19.7%.

The same set is 24.3% or 19.7%, a 4.6-point difference. A 20% velocity loss, applied as an illustration of the arithmetic and not as a recommendation, gives these results:

| Reference | Stopping velocity | Loss at each rep, % | Rep where 20% is first reached |
|---|---|---|---|
| Fastest rep (0.70 m/s) | 0.70 × 0.80 = 0.56 m/s | 5.7, 0.0, 2.9, 7.1, 11.4, 15.7, 21.4, 24.3 | Rep 7 |
| First rep (0.66 m/s) | 0.66 × 0.80 = 0.528 m/s | 0.0, −6.1, −3.0, 1.5, 6.1, 10.6, 16.7, 19.7 | Not reached in 8 reps |

Pearson et al. (2020) adjusted the free-weight back squat load until the fastest warm-up rep moved at 0.70 m/s (± 0.01) mean concentric velocity. The stopping formula gives the values they report: 0.63 m/s for 10%, 0.56 m/s for 20%, and 0.49 m/s for 30% velocity loss. These are study settings, not recommended thresholds.

**Variants.** Two reference variants exist:

- Fastest rep: the percent loss from the fastest, usually first, rep to the slowest, last, rep (Pareja-Blanco et al., 2017). García-Ramos et al. (2021) recommend the fastest rep over the first rep, from 15 men in the Smith machine bench press. Use this by default.
- First rep: use it only if the program or device defines velocity loss this way. It gives a smaller loss whenever a later rep is faster than the first.

The velocity measure matters too. García-Ramos et al. (2021) recommend mean velocity over peak velocity. Weakley et al. (2021a) consider mean, mean propulsive, and peak velocity all usable. Name the measure. Pareja-Blanco et al. (2017) report mean propulsive velocity in a Smith machine full squat, and Pearson et al. (2020) used mean concentric velocity in a free-weight back squat. A figure from one does not transfer to the other.

A related approach uses absolute velocity. The velocity at which a set stopped with 2, 4, 6, or 8 reps in reserve was similar across loads within each of four exercises (Morán-Navarro et al., 2019). In the bench press, velocity loss was closely related to the percent of possible reps completed at 50% to 85% of 1RM (González-Badillo et al., 2017). Both findings are specific to the exercises tested.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Reference rep: 24.3% against 19.7% for the same set. The reference rep and velocity measure changed the number of reps performed before reaching thresholds (García-Ramos et al., 2021).
- Velocity measure: peak velocity instead of mean velocity changed the reps performed before a threshold was reached (García-Ramos et al., 2021).
- Denominator: dividing by the last rep gives 32.1% instead of 24.3%.
- Absolute or percent loss: a drop of 0.13 m/s is not 13%.
- Exercise: for the same set and rep scheme, velocity loss was greater in the bench press than in the squat (Sánchez-Medina & González-Badillo, 2011).
- Device and setup: the device and the exercise variant change the velocity values (Weakley et al., 2021a; Weakley et al., 2021b).
- A failed or partial rep: including a failed rep as 0 m/s gives 100% loss.
- Effort and rep detection: maximal intent and a correct rep count are common practice, not cited findings.

In Smith machine bench press sets of more than 12 reps, the fastest rep was the second rep (40.0% of sets) about as often as the first (37.1%) (García-Ramos et al., 2021).

**Units and typical range.** Velocity loss is in percent. With the fastest-rep reference, it is 0% or more. A negative value is possible only with the first-rep reference. Every row below is a study setting or an opinion, not a prescription. Leave threshold choice to the coach:

| Population | Value | Source |
|---|---|---|
| Free-weight back squat, mean concentric velocity, 12 semi-professional athletes | 10%, 20%, and 30% thresholds tested for between-day reliability | Pearson et al., 2020 |
| Smith machine full squat, mean propulsive velocity, 8-week program, young men | 20% and 40% thresholds compared | Pareja-Blanco et al., 2017 |
| Smith machine full squat, mean propulsive velocity, 20% velocity loss | About half of the maximum possible reps in the set | Pareja-Blanco et al., 2017, citing Sánchez-Medina & González-Badillo, 2011 |
| Smith machine full squat, mean propulsive velocity, 40% velocity loss | Reps to or very close to failure in most sets | Pareja-Blanco et al., 2017, citing Sánchez-Medina & González-Badillo, 2011 |
| Review authors' opinion, not a tested rule | 20% to 40% in the off-season. Below 20% in season. | Weakley et al., 2021a |

**Vendor equivalents.** The device files map these metrics:

- GymAware velocity loss, velocity drop-off, or fatigue target: no API field and no published formula. GymAware's worked examples use the first rep as the reference. VALD's article compares the fastest rep with later reps. In the GymAware file's made-up example set, where rep 2 is fastest, the last rep shows 23.7% against the first rep and 27.6% against the fastest rep. Compute velocity loss yourself from the rep mean velocities in `/reps`.
- Perch `% Drop` goal: a rep is flagged when it falls more than the set percentage below the first rep or the best rep. The choices are 5%, 10%, 15%, 20%, or manual. The velocity measure is not stated, and whether `% Drop` appears in exports is not published.

**Reference file.** [velocity-loss.md](../skills/velocity-based-training/references/velocity-loss.md)

## Limb symmetry

These metrics compare one limb's test result with the other limb's result. The name "limb symmetry index" covers many different formulas, and studies use the same name for formulas that give different numbers (Bishop et al., 2016; Parkinson et al., 2021). Always name the formula.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| LSI (symmetry) | `involved limb / uninvolved limb x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Percentage difference, signed | `(right - left) / max(right, left) x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Dominant-referenced asymmetry | `(dominant - nondominant) / dominant x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Bilateral asymmetry index (BAI-1) | `(dominant - nondominant) / (dominant + nondominant) x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Mean-referenced asymmetry index | `(dominant - nondominant) / ((dominant + nondominant) / 2) x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Log ratio | `100 x ln(right / left)` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Symmetry angle | `(45 - arctan(left / right) in degrees) / 90 x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
| Asymmetry noise band | `1.96 × √(SE_left² + SE_right²)` | Units of the measure | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |

### Limb symmetry index

**What it measures.** A limb symmetry index compares one limb's test result with the other limb's result, as a percentage. LSI reports symmetry, where 100% means equal. The other formulas report asymmetry, where 0% means equal. An index never shows on its own that an athlete is "at risk", "cleared", or "ready".

**Inputs.** The calculation needs these data:

- One row per limb per trial with `athlete_id`, `test_date`, `test_name`, `side` (left or right), and the measure with its unit, such as `jump_height_m` or `peak_force_n`
- Whether the test is unilateral (each limb tested on its own) or bilateral (both limbs at once, one value per limb)
- A reference limb definition for each athlete: involved and uninvolved, dominant and nondominant, or larger value. The user names the involved limb for any LSI.
- About three trials per limb (Bishop et al., 2018), with one trial summary for both limbs
- A TE or pooled squad coefficient of variation for the test, from a squad reliability study, or from a published reliability study of the same test, device, and population

**Calculation.** These are the formula variants you will meet most often:

```text
LSI (symmetry, %)                       = involved limb / uninvolved limb x 100
Percentage difference, signed (%)       = (right - left) / max(right, left) x 100
Dominant-referenced asymmetry (%)       = (dominant - nondominant) / dominant x 100
Bilateral asymmetry index, BAI-1 (%)    = (dominant - nondominant) / (dominant + nondominant) x 100
Mean-referenced asymmetry index (%)     = (dominant - nondominant) / ((dominant + nondominant) / 2) x 100
Log ratio (%)                           = 100 x ln(right / left)
Symmetry angle (%)                      = (45 - arctan(left / right) in degrees) / 90 x 100
Noise band for the left-right difference = 1.96 × √(SE_left² + SE_right²)
```

The terms mean the following:

- `involved limb`: the injured or operated limb. `uninvolved limb`: the other limb.
- `dominant limb`: the limb the athlete prefers, often the kicking leg. Define it once per athlete and do not change it.
- `right`, `left`: the athlete's own right and left
- `max(right, left)`: the larger of the two values on that day
- Reference limb: the limb in the denominator of a formula
- `SE_left`, `SE_right`: the standard error of each limb's value, in the units of the measure. Use TE for single or best trials. For a mean of k trials, use a pooled squad coefficient of variation × the limb's value / √k.

Follow the reference-limb rule:

- Name the reference limb in every result, and keep the same definition across every session for that athlete.
- Report both raw limb values next to the percentage.
- Only percentage difference against the larger limb, BAI-1, the mean-referenced index, the log ratio, and the symmetry angle keep the same size whichever limb is stronger.
- Never infer the involved limb from the data. If the user does not name it, do not calculate an LSI.
- An LSI can look better because the uninvolved limb got weaker. After ACL reconstruction, LSIs often overestimated knee function compared with an index that used the uninvolved limb's values from before surgery (Wellsandt et al., 2017). Track each limb's own value over time.

Follow these steps from raw inputs:

1. Confirm the side labels against the device file, so left and right are not swapped.
2. Choose one trial summary, the best trial or the mean of trials, and use it for both limbs.
3. Choose the formula. Use the one the user names. If the user names none, use percentage difference for unilateral tests and BAI-1 for bilateral tests (Bishop et al., 2018), and say so. For the Nordic hamstring test, a two-leg task, use percentage difference, because Nordic studies express imbalance on a one-leg scale: a left-to-right ratio, log-transformed and back-transformed to a percentage (Opar et al., 2015; Bourne et al., 2015). Offer the log ratio.
4. Calculate the value and its sign. State which side is larger.
5. Get an SE for each limb and state its source. Take TE or the coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own trials or from the same trials you are judging.
6. Compare the difference between the raw limb values, in units, with the noise band. Use this one rule whatever formula you report. When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study.
7. If the difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal or that the athlete has recovered."
8. Report the raw values for both limbs, the formula, the reference limb, the result, the SE and its source, and the band.

**Worked example.** One pair of values, right 25 cm and left 20 cm, run through every formula. It reproduces the example in Bishop et al. (2016). In Case A, the right limb is dominant and the left limb is involved:

| Formula | Calculation | Result |
|---|---|---|
| LSI, involved / uninvolved × 100 | 20 / 25 × 100 | 80.00% symmetry |
| Percentage difference, (right - left) / max × 100 | 5 / 25 × 100 | 20.00% |
| Dominant-referenced, (D - ND) / D × 100 | 5 / 25 × 100 | 20.00% |
| BAI-1, (D - ND) / (D + ND) × 100 | 5 / 45 × 100 | 11.11% |
| Mean-referenced asymmetry index, (D - ND) / mean × 100 | 5 / 22.5 × 100 | 22.22% |
| Symmetry angle | (45 - 38.66) / 90 × 100 | 7.04% |

The asymmetry formulas range from 7.04% to 22.22%, a spread of 15.18 percentage points, and the largest is 3.15 times the smallest. In Case B, the left limb is dominant, so the dominant limb is the weaker one. The dominant-referenced value becomes −25.00%, BAI-1 −11.11%, and the mean-referenced index −22.22%. The range becomes 7.04% to 25.00% in size, a spread of 17.96 points, with the largest 3.55 times the smallest. In Case C, the right limb is involved, and LSI becomes 125.00%. The log ratio gives 22.31%, and −22.31% with the limbs swapped.

The noise band example uses Nordic values of left 325 N and right 360 N, best repetition per leg, a difference of 35 N:

1. Option A, SE = 21.7 N per leg, the lowest typical error Opar et al. (2013) reported: band = 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the larger leg. The 35 N difference is inside the band.
2. Option B, mean of 3 repetitions (317.7 N and 353.0 N) with an assumed pooled squad coefficient of variation of 5%: SE = 5% × 317.7 / √3 = 9.17 N and 5% × 353.0 / √3 = 10.19 N. Band = 1.96 × √(9.17² + 10.19²) = 26.9 N. The mean-of-3 difference, 35.3 N, is outside the band.

Result: one pair of values gave 7.04%, 11.11%, 20.00%, 22.22%, 25.00%, 80.00%, and 125.00%, depending on the formula and reference limb. For the Nordic legs, the percentage difference is 9.72%, the log ratio is 10.23%, and BAI-1 is 5.11%. The SE decides whether the difference is larger than noise.

**Variants.** Use each variant this way:

- LSI: the most used index in the literature (Parkinson et al., 2021). Use it only in a rehab setting when the user names the involved limb.
- Percentage difference: the same size of result whichever limb is stronger. Recommended for unilateral tests (Bishop et al., 2018). The signed version is positive when the right limb is larger (Bishop et al., 2021).
- Dominant-referenced asymmetry: a larger size of result when the dominant limb is the weaker one. Use it only when the user asks for it.
- BAI-1: recommended for bilateral tests, because each limb's force is part of the total (Bishop et al., 2018). It gives smaller values than the other formulas (Parkinson et al., 2021). With no dominant limb named, calculate (right - left) / (right + left) × 100 and say so.
- Mean-referenced asymmetry index: Bishop et al. (2018) list the same calculation as LSI-3, the asymmetry index, and the bilateral asymmetry index 2 (BAI-2).
- Log ratio: changes sign, but not size, when you swap the limbs. Nordic studies have used a log-transformed left-to-right ratio, back-transformed to a percentage (Bourne et al., 2015).
- Symmetry angle: needs no reference limb and gives small values (Zifchock et al., 2008; Bishop et al., 2016). Use it only when both values are above zero. The result then stays between −50% and 50%.

Bishop et al. (2021) describe an optional lenient screen. They computed group coefficients of variation for each test, metric, and limb from three trials within a session, and drew one line per metric at the largest of those values. Use it only if the user asks, cite it, and call it a lenient screen. It flags more differences than the noise band. Never compute the coefficient of variation from one athlete's own three trials. An estimate from three values is unstable, so a symmetric athlete is often flagged by chance. With single trials and a coefficient of variation of 5%, the noise band on the difference is about 1.96 × √2 × 5% = 13.9% of the limb value, while the screen's line is 5%.

**What changes the number.** These choices change the result when the athlete has not changed:

- Formula: the same limbs give asymmetry values from 7.04% to 25.00%.
- Reference limb: changing the dominant limb from right to left changes the dominant-referenced value from 20.00% to −25.00%.
- Denominator: dividing the same 5 cm difference by the larger limb, the smaller limb, the sum, or the mean gives 20.00%, 25.00%, 11.11%, or 22.22%.
- Symmetry or asymmetry: an 80% LSI and a 20% asymmetry describe the same data.
- Values near zero: symmetry indexes in normal walking ranged up to more than 13,000% for variables near zero (Herzog et al., 1989).
- Test and metric: asymmetry rarely favored the same limb across tests (Bishop et al., 2021).
- Trial selection: the best trial and the mean of trials give different values.
- Intra-limb variability: a between-limb difference can come from trial-to-trial noise within each limb (Exell et al., 2012).
- Vendor formula and sign: at least one device glossary uses (left - right) / max(left, right) × 100, where a positive value means the left limb is larger. Never read the sign of a vendor value. Recompute from the left and right values.

**Units and typical range.** Report every value in % with the formula name, the reference limb, and the larger side. Use these ranges to check that data are plausible. They are not cut-offs:

| Population | Typical range | Source |
|---|---|---|
| Male soccer players (n = 313), bilateral jump force test, (stronger - weaker) / stronger × 100, positive when the right leg is stronger | 2.5th to 97.5th percentile of that sample: −15% to 15% | Impellizzeri et al., 2007 |
| Recreational sport athletes (n = 28), unilateral isometric squat and single-leg jumps, percentage difference | Mean asymmetry 5.3% or less; some individuals 20 to 30% | Bishop et al., 2021 |

Keep these limits:

- Many studies apply a fixed threshold, most often between 10 and 15%, to label asymmetry as abnormal. That threshold was not always supported by appropriate evidence (Parkinson et al., 2021). Prospective evidence that a fixed threshold marks higher injury risk is scarce (Bishop et al., 2018). Do not use any of these figures as a cut-off.
- Never apply a threshold as a pass or fail, a clearance, or a return-to-sport rule.
- A 90% LSI or any other return-to-sport criterion belongs to a clinician-run test battery. After ACL reconstruction, 57.1% of patients reached 90% LSIs on all tests, but only 28.6% reached 90% of estimated pre-injury capacity (Wellsandt et al., 2017). The 90% cut-off rests on consensus and expert opinion, not on outcome data. In 233 athletes, LSI cut-offs did not separate those who returned without a second ACL injury from those who did not (Simonsson et al., 2025). In a meta-analysis, only 23% of patients passed a return-to-sport test battery. Passing lowered the risk of graft rupture but raised the risk of an ACL injury in the other knee, and did not lower the risk of any second ACL injury (Webster & Hewett, 2019). Do not say whether the athlete meets the criterion.

**Vendor equivalents.** The device files map these metrics:

- VALD ForceDecks asymmetry (any metric with the `Asym` limb): the Technical Glossary gives (Left − Right) ÷ max(Left, Right) × 100. VALD sources disagree on the sign. VALD does not publish the Hub CSV column list. A public parser for Hub exports shows asymmetry as text, such as `12.3 L` or `8.1 R`, where the letter names the side with the larger value. The `valdr` function `export_forcedecks_csv()` drops the limb columns. Recompute from the left and right values with one stated formula.
- VALD NordBord imbalance (in the app only): described as the percentage difference between left and right maximums, with a second imbalance from left and right averages. VALD does not publish the formula. A VALD research summary used `|L − R| / (L + R)` for hamstring asymmetry, and VALD does not say which formula the app uses. The API has no imbalance field.
- Hawkin `L|R ...(%)` metrics, such as `L|R Avg. Braking Force(%)` and `L|R Peak Force(%)`: Hawkin does not publish the formula. The asymmetry report shows left-dominant values as positive. Recompute from the `Left ...` and `Right ...` columns. Hawkin `Force at Peak` columns give each plate's force at the instant of combined peak force, not each plate's own peak.
- GymAware: no endpoint has a side field. Side appears only in exercise names, such as `Landmine Press - Left`. No GymAware asymmetry formula is published.
- Perch: rep-level Train Sets exports show left-right asymmetry for lower-body unilateral exercises. The field names and the formula are not published.

**Reference file.** [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md)

## Composites

A composite combines several monitoring measures into one number. The reference file labels the output "composite distance from baseline", not "readiness score".

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Input z-score | `z_i = (x_i − baseline_mean_i) ÷ baseline_sd_i` | No unit | [readiness-composites.md](../skills/readiness-composites/references/readiness-composites.md) |
| Aligned z-score | `z_i' = z_i × d_i` | No unit | [readiness-composites.md](../skills/readiness-composites/references/readiness-composites.md) |
| Composite | `Σ (w_i × z_i') ÷ Σ w_i` | No unit | [readiness-composites.md](../skills/readiness-composites/references/readiness-composites.md) |
| Composite z (optional) | `(composite − mean of past composites) ÷ SD of past composites` | No unit | [readiness-composites.md](../skills/readiness-composites/references/readiness-composites.md) |

### Readiness composite

**What it measures.** A readiness composite combines several monitoring measures, such as wellness answers and test results, into one number that shows how far an athlete sits from their own usual values overall. It measures nothing directly. It is a weighted summary of its inputs, so it can only be as sound as those inputs and their weights.

Read these limits before you build one:

- A composite is decision support. It is never clearance for training, competition, or return to sport. Return to sport is a shared decision across a continuum, made by clinicians, athletes, and coaches (Ardern et al., 2016). Frameworks for that decision combine many kinds of information and the decision-maker's risk tolerance (Shrier, 2015).
- Combining variables into one loses information and makes the result harder to interpret (Song et al., 2013). A single score hides which input changed. Song et al. (2013) discuss composites for research analyses, so their points carry over to one athlete's daily score by reasoning, not by direct evidence.
- Traffic-light monitoring systems lack a standard way of being set up (Robertson et al., 2017). A composite's colors are a local choice.
- Training-load measures cannot tell you whether a change raises or lowers injury risk (Impellizzeri et al., 2020b). Keep load measures out of the composite by default, and show them beside it. Do not include the ACWR as an input (Impellizzeri et al., 2020a).
- For a rehab athlete, never put pain, swelling or effusion, loss of motion, giving way, locking, wound problems, calf pain or swelling, new numbness or weakness, or systemic symptoms such as fever into a composite. Show each one raw, and tell the user to pass any report to the medical team. A pain z-score of −2 with a CMJ z-score of +1, a sleep z-score of +1, and a fatigue z-score of 0 gives a composite of 0.0.
- A return of the composite to the pre-injury baseline is not a return-to-sport criterion. Published criteria, such as those in Grindem et al. (2016), are batteries of tests in which passing meant a score above 90 on all tests. A composite lets a good score on one input hide a failed one.

**Inputs.** The calculation needs these data:

- One row per `athlete_id` and `date`, with one column per input in its own unit, such as `sleep` (1 to 5) and `cmj_cm` (cm)
- Each input's direction, written down with the user
- The baseline window and the minimum number of baseline days for each input
- The weights, with their source, or equal weights
- Load measures, such as `load_prev_day_au`, in their own columns beside the composite

**Calculation.** Build a composite in four steps, with an optional fifth:

```text
1. z_i  = (x_i − baseline_mean_i) ÷ baseline_sd_i        for each input i, per athlete
2. z_i' = z_i × d_i                                      d_i = +1 if higher is better, −1 if higher is worse
3. composite = Σ (w_i × z_i') ÷ Σ w_i                    weighted mean of the aligned z-scores
4. Report every z_i', raw value, and change in raw units next to the composite
5. Optional: composite_z = (composite − mean of past composites) ÷ SD of past composites
```

The terms mean the following:

- `x_i`: the athlete's value for input `i` on the day scored, in that input's own unit
- `baseline_mean_i`, `baseline_sd_i`: the mean and sample SD of that athlete's previous values for input `i` over the baseline window, excluding the day scored
- `z_i`: the input's z-score, in SD units
- `d_i`: the direction sign, so a positive `z_i'` means "better than usual" for every input
- `w_i`: the weight for input `i`. Equal weights give a simple average.
- `composite`: a weighted mean of z-scores, not itself a z-score
- `composite_z`: the composite standardized against the athlete's own baseline of composite values. Song et al. (2013) describe re-standardizing a composite. Use it only if the user asks, and name it.

Follow these steps from raw inputs:

1. Join the inputs by athlete and date. Keep load measures and rehab warning signs out of the composite, and show them raw.
2. For each athlete, input, and day, calculate the baseline mean and sample SD from the window before that day.
3. Mark an input as missing for that day if its baseline is too short or its SD is 0.
4. Calculate each input's z-score, then multiply it by its direction sign.
5. Use the user's weights, or equal weights if they have none. Say what share each construct gets.
6. If any input is missing that day, mark the composite as incomplete and do not calculate it, unless the user chose another rule.
7. Calculate the composite as the sum of weight × aligned z-score, divided by the sum of the weights.
8. Report the composite with every input's raw value, change in raw units, baseline mean, baseline SD, and aligned z-score, and the load columns beside it.

**Worked example.** One athlete has four inputs, with baselines from the previous 28 days. Wellness items use a 1 to 5 scale where 5 is best, so a 5 for soreness means not sore. All directions are +1:

| Input | Baseline mean | Baseline SD | Day A raw | Day A aligned z | Day B raw | Day B aligned z |
|---|---|---|---|---|---|---|
| Sleep (1 to 5) | 4.0 | 0.5 | 3 | −2.0 | 4 | 0.0 |
| Soreness (1 to 5) | 4.0 | 1.0 | 4 | 0.0 | 3 | −1.0 |
| Fatigue (1 to 5) | 4.0 | 0.5 | 4 | 0.0 | 4 | 0.0 |
| CMJ jump height (cm) | 38.0 | 1.2 | 38.0 cm | 0.0 | 36.8 cm | −1.0 |
| Previous-day load, beside the composite | | | 690 AU (+240 AU) | not in composite | 450 AU (0 AU) | not in composite |

Each aligned z-score is (raw − mean) ÷ SD × direction. Day A sleep is (3 − 4.0) ÷ 0.5 × (+1) = −2.0. Day B jump height is (36.8 − 38.0) ÷ 1.2 × (+1) = −1.0. With equal weights:

- Day A composite: (−2.0 + 0.0 + 0.0 + 0.0) ÷ 4 = −0.5.
- Day B composite: (0.0 − 1.0 + 0.0 − 1.0) ÷ 4 = −0.5.

Result: both days read −0.5. On Day A, one poor night of sleep drives the score. On Day B, more soreness and a lower jump drive it. Only the sub-scores show the difference.

**Variants.** The file describes these choices:

- Weights from a prior study or from a statistical method such as principal components analysis (Song et al., 2013). No published weights exist for a general readiness composite. Use equal weights unless the user supplies weights and their source.
- Grouping: average related items into one group score first, then combine the groups. Equal weights per input are not equal weights per construct. With three wellness items and one jump test, wellness carries 75% of the weight.
- Composite z: the optional fifth step, used only on request.

The composite is not a z-score. A mean of k unrelated z-scores has an SD of 1 ÷ √k, which is 0.50 for 4 inputs and 0.447 for 5. For 4 inputs that each correlate at r = 0.5, the SD is 0.79. The spread of a composite depends on the variances and covariances of its inputs (Song et al., 2013). In a simulation of 4 unrelated inputs, 2.3% of days fell below a composite of −1, against 15.9% for a single z-score. Across 25 athletes at that cut-off, that is 0.57 flags a day by chance, with a 43.7% chance of at least one. Report the expected number next to the number found, and recommend a repeat measurement or a conversation before anyone acts on a single flag (Barnett et al., 2005).

**What changes the number.** These choices change the result when the athlete has not changed:

- Weights: doubling the weight on jump height gives Day A −0.4 and Day B −0.6. Doubling the weight on sleep gives Day A −0.8 and Day B −0.4. The order of the two days flips.
- Grouping: averaging the three wellness items first, then averaging with jump height, gives Day A −0.33 and Day B −0.67.
- Direction of an input: soreness entered with a direction of −1 by mistake makes Day B read 0.0 instead of −0.5.
- Adding load: previous-day load on Day A (690 AU, z = +2.0) gives −0.8 with a direction of −1 and 0.0 with +1. No published rule sets that direction (Impellizzeri et al., 2020b).
- Missing inputs: with no jump test on Day B, filling the gap with 0 gives −0.25, and averaging the three inputs present gives −0.33. Both differ from the complete −0.5. Mark the day as incomplete.
- Number of inputs, baseline window, and team versus athlete baseline: each changes every z-score or the composite's spread.
- Rescaling: converting to a 0 to 100 scale changes how it reads, not what it measures. It is not "% ready".

**Units and typical range.** The composite has no unit. Zero means the weighted inputs average out at the athlete's baseline. It is not a z-score, a percentage, a probability, or a risk. No validated range or cut-off exists for a general readiness composite (Robertson et al., 2017). Use cut-offs the practitioner chose, and label them as their choice. A baseline should be stable, with low variability and no clear trend (Sands et al., 2019).

**Vendor equivalents.** The device files describe these vendor composites. None maps to the reference file:

- Firstbeat `Training Status`: a 0 to 100 score that combines acute load, ACWR, and the last three Quick Recovery Tests. The weights are not published. Above 70 is well balanced, 30 to 70 is moderate, and below 30 is out of balance. It needs at least 3 tests in 14 days to include recovery. It includes load and ACWR, which the reference file keeps out of a composite.
- Firstbeat `Overnight Recovery (%)` and `24h Stress & Recovery Balance`: proprietary composites with unpublished methods.
- Perch Readiness: compares the most recent jump session with the previous session and the 30-day average, then gives a z-score status. The published bands leave −1 to 1 unassigned.
- Perch Total Performance Score: weights Speed Score and Strength Score equally. Both are z-scores of load-velocity profile intercepts against a group, not against the athlete's own baseline. The reference group, and whether the total is a mean or a sum, are not published.

**Reference file.** [readiness-composites.md](../skills/readiness-composites/references/readiness-composites.md)

## Vendor metric pages

Every exportable metric each vendor publishes is broken down on its page. The pages paraphrase vendor definitions and link to the vendor sources. The [vendor metrics index](vendor-metrics/README.md) lists every page:

| Vendor | Products | Page |
|---|---|---|
| VALD | ForceDecks and NordBord | [VALD ForceDecks and NordBord metrics](vendor-metrics/vald-forcedecks-nordbord/README.md) |
| VALD | ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware | [VALD other products](vendor-metrics/vald-other-products/README.md) |
| Hawkin Dynamics | Force plates and TruStrength | [Hawkin Dynamics metrics](vendor-metrics/hawkin-dynamics/README.md) |
| Catapult | Vector, Catapult One, and Perch | [Catapult metrics](vendor-metrics/catapult.md) |
| Kinexon | Kinexon | [Kinexon metrics](vendor-metrics/kinexon.md) |
| Polar | Polar Team Pro | [Polar Team Pro metrics](vendor-metrics/polar-team-pro.md) |
| Firstbeat | Firstbeat Sports | [Firstbeat Sports metrics](vendor-metrics/firstbeat-sports.md) |

## Sources

This page cites these sources, as the reference files list them. Seven sources have no DOI, and the entry says so:

- Abt G, Lovell R. The use of individualized speed and intensity thresholds for determining the distance run at high-intensity in professional soccer. J Sports Sci. 2009;27(9):893-898. https://doi.org/10.1080/02640410902998239
- Achten J, Jeukendrup AE. Heart rate monitoring: applications and limitations. Sports Med. 2003;33(7):517-538. https://doi.org/10.2165/00007256-200333070-00004
- Ardern CL, Glasgow P, Schneiders A, Witvrouw E, Clarsen B, Cools A, et al. 2016 Consensus statement on return to sport from the First World Congress in Sports Physical Therapy, Bern. Br J Sports Med. 2016;50(14):853-864. https://doi.org/10.1136/bjsports-2016-096278
- Atkinson G, Nevill AM. Statistical methods for assessing measurement error (reliability) in variables relevant to sports medicine. Sports Med. 1998;26(4):217-238. https://doi.org/10.2165/00007256-199826040-00002
- Banister EW. Modeling elite athletic performance. In: MacDougall JD, Wenger HA, Green HJ, editors. Physiological Testing of the High-Performance Athlete. 2nd ed. Champaign (IL): Human Kinetics Books; 1991:403-424. ISBN 0873223004. Book chapter, not peer reviewed, no DOI. Read through the Internet Archive full-text search: https://archive.org/details/physiologicaltes0000unse (accessed 2026-10-02).
- Banister EW, Hamilton CL. Variations in iron status with fatigue modelled from training in female distance runners. Eur J Appl Physiol Occup Physiol. 1985;54(1):16-23. https://doi.org/10.1007/BF00426292
- Banister EW, Morton RH, Fitz-Clarke J. Dose/response effects of exercise modeled from training: physical and biochemical measures. Ann Physiol Anthropol. 1992;11(3):345-356. https://doi.org/10.2114/ahs1983.11.345
- Banyard HG, Nosaka K, Haff GG. Reliability and validity of the load-velocity relationship to predict the 1RM back squat. J Strength Cond Res. 2017;31(7):1897-1904. https://doi.org/10.1519/JSC.0000000000001657
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-220. https://doi.org/10.1093/ije/dyh299
- Bassek M, Raabe D, Memmert D, Rein R. Analysis of motion characteristics and metabolic power in elite male handball players. J Sports Sci Med. 2023;22(2):310-316. https://doi.org/10.52082/jssm.2023.310
- Batterham AM, Hopkins WG. Making meaningful inferences about magnitudes. Int J Sports Physiol Perform. 2006;1(1):50-57. https://doi.org/10.1123/ijspp.1.1.50
- Bishop C, Read P, Chavda S, Turner A. Asymmetries of the lower limb: the calculation conundrum in strength training and conditioning. Strength Cond J. 2016;38(6):27-32. https://doi.org/10.1519/SSC.0000000000000264
- Bishop C, Read P, Lake J, Chavda S, Turner A. Interlimb asymmetries: understanding how to calculate differences from bilateral and unilateral tests. Strength Cond J. 2018;40(4):1-6. https://doi.org/10.1519/SSC.0000000000000371
- Bishop C, Lake J, Loturco I, Papadopoulos K, Turner A, Read P. Interlimb asymmetries: the need for an individual approach to data analysis. J Strength Cond Res. 2021;35(3):695-701. https://doi.org/10.1519/JSC.0000000000002729
- Borg GA. Psychophysical bases of perceived exertion. Med Sci Sports Exerc. 1982;14(5):377-381. https://doi.org/10.1249/00005768-198205000-00012
- Borg E, Kaijser L. A comparison between three rating scales for perceived exertion and two different work tests. Scand J Med Sci Sports. 2006;16(1):57-69. https://doi.org/10.1111/j.1600-0838.2005.00448.x
- Bourne MN, Opar DA, Williams MD, Shield AJ. Eccentric knee flexor strength and risk of hamstring injuries in rugby union: a prospective study. Am J Sports Med. 2015;43(11):2663-2670. https://doi.org/10.1177/0363546515599633
- Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? Front Physiol. 2014;5:73. https://doi.org/10.3389/fphys.2014.00073
- Buchheit M, Al Haddad H, Millet GP, Lepretre PM, Newton M, Ahmaidi S. Cardiorespiratory and cardiac autonomic responses to 30-15 intermittent fitness test in team sport players. J Strength Cond Res. 2009;23(1):93-100. https://doi.org/10.1519/JSC.0b013e31818b9721
- Buchheit M, Al Haddad H, Simpson BM, Palazzi D, Bourdon PC, Di Salvo V, Mendez-Villanueva A. Monitoring accelerations with GPS in football: time to slow down? Int J Sports Physiol Perform. 2014;9(3):442-445. https://doi.org/10.1123/ijspp.2013-0187 (cited as Buchheit et al., 2014a)
- Buchheit M, Allen A, Poon TK, Modonutti M, Gregson W, Di Salvo V. Integrating different tracking systems in football: multiple camera semi-automatic system, local position measurement and GPS technologies. J Sports Sci. 2014;32(20):1844-1857. https://doi.org/10.1080/02640414.2014.942687 (cited as Buchheit et al., 2014b)
- Carton-Llorente A, Lozano D, Gilart Iglesias V, Marcos Jorquera D, Manchado C. Worst-case scenario analysis of physical demands in elite men handball players by playing position through big data analytics. Biol Sport. 2023;40(4):1219-1227. https://doi.org/10.5114/biolsport.2023.126665
- Comfort P, Dos'Santos T, Beckham GK, Stone MH, Guppy SN, Haff GG. Standardization and methodological considerations for the isometric midthigh pull. Strength Cond J. 2019;41(2):57-79. https://doi.org/10.1519/SSC.0000000000000433
- Coyle EF, González-Alonso J. Cardiovascular drift during prolonged exercise: new perspectives. Exerc Sport Sci Rev. 2001;29(2):88-92. https://doi.org/10.1097/00003677-200104000-00009
- Coyne JOC, Nimphius S, Newton RU, Haff GG. Does mathematical coupling matter to the acute to chronic workload ratio? A case study from elite sport. Int J Sports Physiol Perform. 2019;14(10):1447-1454. https://doi.org/10.1123/ijspp.2018-0874
- Cummins C, Orr R, O'Connor H, West C. Global positioning systems (GPS) and microtechnology sensors in team sports: a systematic review. Sports Med. 2013;43(10):1025-1042. https://doi.org/10.1007/s40279-013-0069-2
- de Vet HC, Terwee CB, Ostelo RW, Beckerman H, Knol DL, Bouter LM. Minimal changes in health status questionnaires: distinction between minimally detectable change and minimally important change. Health Qual Life Outcomes. 2006;4:54. https://doi.org/10.1186/1477-7525-4-54
- Dos'Santos T, Jones PA, Comfort P, Thomas C. Effect of different onset thresholds on isometric midthigh pull force-time variables. J Strength Cond Res. 2017;31(12):3463-3473. https://doi.org/10.1519/JSC.0000000000001765
- Ebben WP, Petushek EJ. Using the reactive strength index modified to evaluate plyometric performance. J Strength Cond Res. 2010;24(8):1983-1987. https://doi.org/10.1519/JSC.0b013e3181e72466
- Edwards S. High performance training and racing. In: The Heart Rate Monitor Book. Sacramento (CA): Fleet Feet Press; Port Washington (NY): Polar CIC; 1993:113-123. Third printing, October 1993. The Library of Congress catalogs the book (ISBN 0963463306, LCCN 92062064) as c1992. Book, not peer reviewed, no DOI. Zone weights are taken from Paulson et al. (2015) and Hourcade et al. (2018).
- Exell TA, Irwin G, Gittoes MJR, Kerwin DG. Implications of intra-limb variability on asymmetry analyses. J Sports Sci. 2012;30(4):403-409. https://doi.org/10.1080/02640414.2011.647047
- Fanchini M, Ferraresi I, Modena R, Schena F, Coutts AJ, Impellizzeri FM. Use of the CR100 scale for session rating of perceived exertion in soccer and its interchangeability with the CR10. Int J Sports Physiol Perform. 2016;11(3):388-392. https://doi.org/10.1123/ijspp.2015-0273
- Fereday K, Hills SP, Russell M, Smith J, Cunningham DJ, Shearer D, McNarry M, Kilduff LP. A comparison of rolling averages versus discrete time epochs for assessing the worst-case scenario locomotor demands of professional soccer match-play. J Sci Med Sport. 2020;23(8):764-769. https://doi.org/10.1016/j.jsams.2020.01.002
- Foster C, Florhaug JA, Franklin J, Gottschall L, Hrovatin LA, Parker S, Doleshal P, Dodge C. A new approach to monitoring exercise training. J Strength Cond Res. 2001;15(1):109-115. https://doi.org/10.1519/00124278-200102000-00019
- Furlan L, Sterr A. The applicability of standard error of measurement and minimal detectable change to motor learning research: a behavioral study. Front Hum Neurosci. 2018;12:95. https://doi.org/10.3389/fnhum.2018.00095
- Gabbett TJ. The training-injury prevention paradox: should athletes be training smarter and harder? Br J Sports Med. 2016;50(5):273-280. https://doi.org/10.1136/bjsports-2015-095788
- Gabbett TJ, Hulin B, Blanch P, Chapman P, Bailey D. To couple or not to couple? For acute:chronic workload ratios and injury risk, does it really matter? Int J Sports Med. 2019;40(9):597-600. https://doi.org/10.1055/a-0955-5589
- García-Ramos A, Pestaña-Melero FL, Pérez-Castilla A, Rojas FJ, Haff GG. Mean velocity vs. mean propulsive velocity vs. peak velocity: which variable determines bench press relative load with higher reliability? J Strength Cond Res. 2018;32(5):1273-1279. https://doi.org/10.1519/JSC.0000000000001998
- García-Ramos A, Weakley J, Janicijevic D, Jukic I. Number of repetitions performed before and after reaching velocity loss thresholds: first repetition versus fastest repetition, mean velocity versus peak velocity. Int J Sports Physiol Perform. 2021;16(7):950-957. https://doi.org/10.1123/ijspp.2020-0629
- Gillinov S, Etiwy M, Wang R, Blackburn G, Phelan D, Gillinov AM, Houghtaling P, Javadikasgari H, Desai MY. Variable accuracy of wearable heart rate monitors during aerobic exercise. Med Sci Sports Exerc. 2017;49(8):1697-1703. https://doi.org/10.1249/MSS.0000000000001284
- Glaister M, Gissane C. Caffeine and physiological responses to submaximal exercise: a meta-analysis. Int J Sports Physiol Perform. 2018;13(4):402-411. https://doi.org/10.1123/ijspp.2017-0312
- Godhe M, Bergman S, Petré H. Between-session reliability of portable isometric mid-thigh pull and countermovement jump tests in elite male ice hockey players from the Swedish Hockey League. Sports. 2025;13(12):456. https://doi.org/10.3390/sports13120456
- González-Badillo JJ, Sánchez-Medina L. Movement velocity as a measure of loading intensity in resistance training. Int J Sports Med. 2010;31(5):347-352. https://doi.org/10.1055/s-0030-1248333
- González-Badillo JJ, Yañez-García JM, Mora-Custodio R, Rodríguez-Rosell D. Velocity loss as a variable for monitoring resistance exercise. Int J Sports Med. 2017;38(3):217-225. https://doi.org/10.1055/s-0042-120324
- Gregson W, Drust B, Atkinson G, Di Salvo V. Match-to-match variability of high-speed activities in premier league soccer. Int J Sports Med. 2010;31(4):237-242. https://doi.org/10.1055/s-0030-1247546
- Grindem H, Snyder-Mackler L, Moksnes H, Engebretsen L, Risberg MA. Simple decision rules can reduce reinjury risk by 84% after ACL reconstruction: the Delaware-Oslo ACL cohort study. Br J Sports Med. 2016;50(13):804-808. https://doi.org/10.1136/bjsports-2016-096031
- Haddad M, Stylianides G, Djaoui L, Dellal A, Chamari K. Session-RPE method for training load monitoring: validity, ecological usefulness, and influencing factors. Front Neurosci. 2017;11:612. https://doi.org/10.3389/fnins.2017.00612
- Haff GG, Ruben RP, Lider J, Twine C, Cormie P. A comparison of methods for determining the rate of force development during isometric midthigh clean pulls. J Strength Cond Res. 2015;29(2):386-395. https://doi.org/10.1519/JSC.0000000000000705
- Harman EA, Rosenstein MT, Frykman PN, Rosenstein RM. The effects of arms and countermovement on vertical jumping. Med Sci Sports Exerc. 1990;22(6):825-833. https://doi.org/10.1249/00005768-199012000-00015
- Harper DJ, Carling C, Kiely J. High-intensity acceleration and deceleration demands in elite team sports competitive match play: a systematic review and meta-analysis of observational studies. Sports Med. 2019;49(12):1923-1947. https://doi.org/10.1007/s40279-019-01170-1
- Healy R, Kenny IC, Harrison AJ. Reactive strength index: a poor indicator of reactive strength? Int J Sports Physiol Perform. 2018;13(6):802-809. https://doi.org/10.1123/ijspp.2017-0511
- Heishman A, Brown B, Daub B, Miller R, Freitas E, Bemben M. The influence of countermovement jump protocol on reactive strength index modified and flight time: contraction time in collegiate basketball players. Sports. 2019;7(2):37. https://doi.org/10.3390/sports7020037
- Herzog W, Nigg BM, Read LJ, Olsson E. Asymmetries in ground reaction force patterns in normal human gait. Med Sci Sports Exerc. 1989;21(1):110-114. https://doi.org/10.1249/00005768-198902000-00020
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02). No DOI.
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. Med Sci Sports Exerc. 2009;41(1):3-13. https://doi.org/10.1249/MSS.0b013e31818cb278
- Hourcade JC, Noirez P, Sidney M, Toussaint JF, Desgorces F. Effects of intensity distribution changes on performance and on training loads quantification. Biol Sport. 2018;35(1):67-74. https://doi.org/10.5114/biolsport.2018.70753
- Hulin BT, Gabbett TJ, Blanch P, Chapman P, Bailey D, Orchard JW. Spikes in acute workload are associated with increased injury risk in elite cricket fast bowlers. Br J Sports Med. 2014;48(8):708-712. https://doi.org/10.1136/bjsports-2013-092524
- Impellizzeri FM, Rampinini E, Coutts AJ, Sassi A, Marcora SM. Use of RPE-based training load in soccer. Med Sci Sports Exerc. 2004;36(6):1042-1047. https://doi.org/10.1249/01.MSS.0000128199.23901.2F
- Impellizzeri FM, Rampinini E, Maffiuletti N, Marcora SM. A vertical jump force test for assessing bilateral strength asymmetry in athletes. Med Sci Sports Exerc. 2007;39(11):2044-2050. https://doi.org/10.1249/mss.0b013e31814fb55c
- Impellizzeri FM, Marcora SM, Coutts AJ. Internal and external training load: 15 years on. Int J Sports Physiol Perform. 2019;14(2):270-273. https://doi.org/10.1123/ijspp.2018-0935
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. Int J Sports Physiol Perform. 2020;15(6):907-913. https://doi.org/10.1123/ijspp.2019-0864 (cited as Impellizzeri et al., 2020a)
- Impellizzeri FM, McCall A, Ward P, Bornn L, Coutts AJ. Training load and its role in injury prevention, part 2: conceptual and methodologic pitfalls. J Athl Train. 2020;55(9):893-901. https://doi.org/10.4085/1062-6050-501-19 (cited as Impellizzeri et al., 2020b)
- Impellizzeri FM, Woodcock S, Coutts AJ, Fanchini M, McCall A, Vigotsky AD. What role do chronic workloads play in the acute to chronic workload ratio? Time to dismiss ACWR and its underlying theory. Sports Med. 2021;51(3):581-592. https://doi.org/10.1007/s40279-020-01378-6
- Jaric S. Muscle strength testing: use of normalisation for body size. Sports Med. 2002;32(10):615-631. https://doi.org/10.2165/00007256-200232100-00002
- Jeffries AC, Wallace L, Coutts AJ, McLaren SJ, McCall A, Impellizzeri FM. Athlete-reported outcome measures for monitoring training responses: a systematic review of risk of bias and measurement property quality according to the COSMIN guidelines. Int J Sports Physiol Perform. 2020;15(9):1203-1215. https://doi.org/10.1123/ijspp.2020-0386
- Jennings D, Cormack S, Coutts AJ, Boyd L, Aughey RJ. The validity and reliability of GPS units for measuring distance in team sport specific running patterns. Int J Sports Physiol Perform. 2010;5(3):328-341. https://doi.org/10.1123/ijspp.5.3.328
- Johnston RJ, Watsford ML, Kelly SJ, Pine MJ, Spurrs RW. Validity and interunit reliability of 10 Hz and 15 Hz GPS units for assessing athlete movement demands. J Strength Cond Res. 2014;28(6):1649-1655. https://doi.org/10.1519/JSC.0000000000000323
- Karjalainen J, Viitasalo M. Fever and cardiac rhythm. Arch Intern Med. 1986;146(6):1169-1171. https://doi.org/10.1001/archinte.1986.00360180179026
- Karvonen MJ, Kentala E, Mustala O. The effects of training on heart rate; a longitudinal study. Ann Med Exp Biol Fenn. 1957;35(3):307-315. PMID: 13470504. No DOI.
- Kraska JM, Ramsey MW, Haff GG, Fethke N, Sands WA, Stone ME, Stone MH. Relationship between strength characteristics and unweighted and weighted vertical jump height. Int J Sports Physiol Perform. 2009;4(4):461-473. https://doi.org/10.1123/ijspp.4.4.461
- Krustrup P, Mohr M, Amstrup T, Rysgaard T, Johansen J, Steensberg A, Pedersen PK, Bangsbo J. The Yo-Yo intermittent recovery test: physiological response, reliability, and validity. Med Sci Sports Exerc. 2003;35(4):697-705. https://doi.org/10.1249/01.MSS.0000058441.94520.32
- Krustrup P, Mohr M, Nybo L, Jensen JM, Nielsen JJ, Bangsbo J. The Yo-Yo IR2 test: physiological response, reliability, and application to elite soccer. Med Sci Sports Exerc. 2006;38(9):1666-1673. https://doi.org/10.1249/01.mss.0000227538.20799.08
- Linke D, Link D, Lames M. Validation of electronic performance and tracking systems EPTS under field conditions. PLoS One. 2018;13(7):e0199519. https://doi.org/10.1371/journal.pone.0199519
- Linthorne NP. Analysis of standing vertical jumps using a force platform. Am J Phys. 2001;69(11):1198-1204. https://doi.org/10.1119/1.1397460
- Lolli L, Batterham AM, Hawkins R, Kelly DM, Strudwick AJ, Thorpe R, Gregson W, Atkinson G. Mathematical coupling causes spurious correlation within the conventional acute-to-chronic workload ratio calculations. Br J Sports Med. 2019;53(15):921-922. https://doi.org/10.1136/bjsports-2017-098110. Editorial, first published online 2017-11-03.
- Lucia A, Hoyos J, Santalla A, Earnest C, Chicharro JL. Tour de France versus Vuelta a España: which is harder? Med Sci Sports Exerc. 2003;35(5):872-878. https://doi.org/10.1249/01.MSS.0000064999.82036.B4
- Maffiuletti NA, Aagaard P, Blazevich AJ, Folland J, Tillin N, Duchateau J. Rate of force development: physiological and methodological considerations. Eur J Appl Physiol. 2016;116(6):1091-1116. https://doi.org/10.1007/s00421-016-3346-6
- Malone JJ, Lovell R, Varley MC, Coutts AJ. Unpacking the black box: applications and considerations for using GPS devices in sport. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-18-S2-26. https://doi.org/10.1123/ijspp.2016-0236
- Manzi V, Castagna C, Padua E, Lombardo M, D’Ottavio S, Massaro M, Volterrani M, Iellamo F. Dose-response relationship of autonomic nervous system responses to individualized training impulse in marathon runners. Am J Physiol Heart Circ Physiol. 2009;296(6):H1733-H1740. https://doi.org/10.1152/ajpheart.00054.2009
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength Cond J. 2018;40(4):96-106. https://doi.org/10.1519/SSC.0000000000000375 (cited as McMahon et al., 2018a)
- McMahon JJ, Jones PA, Suchomel TJ, Lake J, Comfort P. Influence of the reactive strength index modified on force- and power-time curves. Int J Sports Physiol Perform. 2018;13(2):220-227. https://doi.org/10.1123/ijspp.2017-0056 (cited as McMahon et al., 2018b)
- Merrigan JJ, Stone JD, Galster SM, Hagen JA. Analyzing force-time curves: comparison of commercially available automated software and custom MATLAB analyses. J Strength Cond Res. 2022;36(9):2387-2402. https://doi.org/10.1519/JSC.0000000000004275
- Morán-Navarro R, Martínez-Cava A, Sánchez-Medina L, Mora-Rodríguez R, González-Badillo JJ, Pallarés JG. Movement velocity as a measure of level of effort during resistance exercise. J Strength Cond Res. 2019;33(6):1496-1504. https://doi.org/10.1519/JSC.0000000000002017
- Nes BM, Janszky I, Wisløff U, Støylen A, Karlsen T. Age-predicted maximal heart rate in healthy subjects: the HUNT fitness study. Scand J Med Sci Sports. 2013;23(6):697-704. https://doi.org/10.1111/j.1600-0838.2012.01445.x
- National Institute of Standards and Technology. Dataplot reference manual: prediction limits. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/predlimi.htm (accessed 2026-10-02). No DOI.
- Opar DA, Piatkowski T, Williams MD, Shield AJ. A novel device using the Nordic hamstring exercise to assess eccentric knee flexor strength: a reliability and retrospective injury study. J Orthop Sports Phys Ther. 2013;43(9):636-640. https://doi.org/10.2519/jospt.2013.4837
- Opar DA, Williams MD, Timmins RG, Hickey J, Duhig SJ, Shield AJ. Eccentric hamstring strength and hamstring injury risk in Australian footballers. Med Sci Sports Exerc. 2015;47(4):857-865. https://doi.org/10.1249/MSS.0000000000000465
- Opar DA, Timmins RG, Behan FP, Hickey JT, van Dyk N, Price K, Maniar N. Is pre-season eccentric strength testing during the Nordic hamstring exercise associated with future hamstring strain injury? A systematic review and meta-analysis. Sports Med. 2021;51(9):1935-1945. https://doi.org/10.1007/s40279-021-01474-1
- Owen NJ, Watkins J, Kilduff LP, Bevan HR, Bennett MA. Development of a criterion method to determine peak mechanical power output in a countermovement jump. J Strength Cond Res. 2014;28(6):1552-1558. https://doi.org/10.1519/JSC.0000000000000311
- Pareja-Blanco F, Rodríguez-Rosell D, Sánchez-Medina L, Sanchis-Moysi J, Dorado C, Mora-Custodio R, Yáñez-García JM, Morales-Alamo D, Pérez-Suárez I, Calbet JAL, González-Badillo JJ. Effects of velocity loss during resistance training on athletic performance, strength gains and muscle adaptations. Scand J Med Sci Sports. 2017;27(7):724-735. https://doi.org/10.1111/sms.12678
- Parkinson AO, Apps CL, Morris JG, Barnett CT, Lewis MGC. The calculation, thresholds and reporting of inter-limb strength asymmetry: a systematic review. J Sports Sci Med. 2021;20(4):594-617. https://doi.org/10.52082/jssm.2021.594
- Paulson TA, Mason B, Rhodes J, Goosey-Tolfrey VL. Individualized internal and external training load relationships in elite wheelchair rugby players. Front Physiol. 2015;6:388. https://doi.org/10.3389/fphys.2015.00388
- Pearson M, García-Ramos A, Morrison M, Ramirez-Lopez C, Dalton-Barron N, Weakley J. Velocity loss thresholds reliably control kinetic and kinematic outputs during free weight resistance training. Int J Environ Res Public Health. 2020;17(18):6509. https://doi.org/10.3390/ijerph17186509
- Polar Electro Oy. Polar Training Load Pro white paper. November 12, 2019; revised March 2025. https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf (accessed 2026-10-02). No DOI. Cited as Polar, 2025.
- Polar Electro Oy. Polar Team Pro API reference, sport profile zone fields `lower_limit` (inclusive) and `higher_limit` (exclusive). https://www.polar.com/teampro-api/ (accessed 2026-10-02). No DOI.
- Pustina AA, Sato K, Liu C, Kavanaugh AA, Sams ML, Liu J, Uptmore KD, Stone MH. Establishing a duration standard for the calculation of session rating of perceived exertion in NCAA Division I men's soccer. J Trainol. 2017;6(1):26-30. https://doi.org/10.17338/trainology.6.1_26
- Reardon C, Tobin DP, Delahunt E. Application of individualized speed thresholds to interpret position specific running demands in elite professional rugby union: a GPS study. PLoS One. 2015;10(7):e0133410. https://doi.org/10.1371/journal.pone.0133410
- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-73-S2-79. https://doi.org/10.1123/ijspp.2016-0541
- Rodríguez-Marroyo JA, González B, Foster C, Carballo-Leyenda AB, Villa JG. Effect of the cooldown type on session rating of perceived exertion. Int J Sports Physiol Perform. 2021;16(4):573-577. https://doi.org/10.1123/ijspp.2020-0225
- Sanchez-Medina L, Perez CE, Gonzalez-Badillo JJ. Importance of the propulsive phase in strength assessment. Int J Sports Med. 2010;31(2):123-129. https://doi.org/10.1055/s-0029-1242815
- Sánchez-Medina L, González-Badillo JJ. Velocity loss as an indicator of neuromuscular fatigue during resistance training. Med Sci Sports Exerc. 2011;43(9):1725-1734. https://doi.org/10.1249/MSS.0b013e318213f880
- Sands WA, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone MH. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. Br J Sports Med. 2016;50(5):281-291. https://doi.org/10.1136/bjsports-2015-094758
- Scott MTU, Scott TJ, Kelly VG. The validity and reliability of global positioning systems in team sport: a brief review. J Strength Cond Res. 2016;30(5):1470-1490. https://doi.org/10.1519/JSC.0000000000001221
- Shrier I. Strategic Assessment of Risk and Risk Tolerance (StARRT) framework for return-to-play decision-making. Br J Sports Med. 2015;49(20):1311-1315. https://doi.org/10.1136/bjsports-2014-094569
- Simonsson R, Sundberg A, Piussi R, Högberg J, Senorski C, Thomeé R, Samuelsson K, Della Villa F, Hamrin Senorski E. Questioning the rules of engagement: a critical analysis of the use of limb symmetry index for safe return to sport after anterior cruciate ligament reconstruction. Br J Sports Med. 2025;59(6):376-384. https://doi.org/10.1136/bjsports-2024-108079
- Sole CJ, Suchomel TJ, Stone MH. Preliminary scale of reference values for evaluating reactive strength index-modified in male and female NCAA Division I athletes. Sports. 2018;6(4):133. https://doi.org/10.3390/sports6040133
- Song MK, Lin FC, Ward SE, Fine JP. Composite variables: when and how. Nurs Res. 2013;62(1):45-49. https://doi.org/10.1097/NNR.0b013e3182741948
- Stone JD, Merrigan JJ, Ramadan J, Brown RS, Cheng GT, Hornsby WG, Smith H, Galster SM, Hagen JA. Simplifying external load data in NCAA Division-I men's basketball competitions: a principal component analysis. Front Sports Act Living. 2022;4:795897. https://doi.org/10.3389/fspor.2022.795897
- Swain DP, Leutholtz BC, King ME, Haas LA, Branch JD. Relationship between % heart rate reserve and % VO2 reserve in treadmill exercise. Med Sci Sports Exerc. 1998;30(2):318-321. https://doi.org/10.1097/00005768-199802000-00022
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Tanaka H, Monahan KD, Seals DR. Age-predicted maximal heart rate revisited. J Am Coll Cardiol. 2001;37(1):153-156. https://doi.org/10.1016/S0735-1097(00)01054-8
- Thomas C, Dos'Santos T, Comfort P, Jones PA. Between-session reliability of common strength- and power-related measures in adolescent athletes. Sports. 2017;5(1):15. https://doi.org/10.3390/sports5010015
- Thornton HR, Nelson AR, Delaney JA, Serpiello FR, Duthie GM. Interunit reliability and effect of data-processing methods of global positioning systems. Int J Sports Physiol Perform. 2019;14(4):432-438. https://doi.org/10.1123/ijspp.2018-0273
- Timmins RG, Bourne MN, Shield AJ, Williams MD, Lorenzen C, Opar DA. Short biceps femoris fascicles and eccentric knee flexor weakness increase the risk of hamstring injury in elite football (soccer): a prospective cohort study. Br J Sports Med. 2016;50(24):1524-1535. https://doi.org/10.1136/bjsports-2015-095362
- Tomoto T, Tarumi T, Sugawara J. Associations among dynamic cerebral autoregulation, baroreflex sensitivity, and carotid distensibility in young healthy adults: insight from endurance training. Eur J Appl Physiol. 2026;126(6):3201-3220. https://doi.org/10.1007/s00421-026-06155-3
- van Dyk N, Bahr R, Burnett AF, Whiteley R, Bakken A, Mosler A, Farooq A, Witvrouw E. A comprehensive strength testing protocol offers no clinical value in predicting risk of hamstring injury: a prospective cohort study of 413 professional football players. Br J Sports Med. 2017;51(23):1695-1702. https://doi.org/10.1136/bjsports-2017-097754
- Varley MC, Elias GP, Aughey RJ. Current match-analysis techniques' underestimation of intense periods of high-velocity running. Int J Sports Physiol Perform. 2012;7(2):183-185. https://doi.org/10.1123/ijspp.7.2.183 (cited as Varley et al., 2012a)
- Varley MC, Fairweather IH, Aughey RJ. Validity and reliability of GPS for measuring instantaneous velocity during acceleration, deceleration, and constant motion. J Sports Sci. 2012;30(2):121-127. https://doi.org/10.1080/02640414.2011.627941 (cited as Varley et al., 2012b)
- Varley MC, Gabbett T, Aughey RJ. Activity profiles of professional soccer, rugby league and Australian football match play. J Sports Sci. 2014;32(20):1858-1866. https://doi.org/10.1080/02640414.2013.823227
- Varley MC, Jaspers A, Helsen WF, Malone JJ. Methodological considerations when quantifying high-intensity efforts in team sport using global positioning system technology. Int J Sports Physiol Perform. 2017;12(8):1059-1068. https://doi.org/10.1123/ijspp.2016-0534
- Vaverka F, Jandačka D, Zahradník D, Uchytil J, Farana R, Supej M, Vodičar J. Effect of an arm swing on countermovement vertical jump performance in elite volleyball players. J Hum Kinet. 2016;53:41-50. https://doi.org/10.1515/hukin-2016-0009
- Wang C, Vargas JT, Stokes T, Steele R, Shrier I. Analyzing activity and injury: lessons learned from the acute:chronic workload ratio. Sports Med. 2020;50(7):1243-1254. https://doi.org/10.1007/s40279-020-01280-1
- Wasserstein RL, Lazar NA. The ASA statement on p-values: context, process, and purpose. Am Stat. 2016;70(2):129-133. https://doi.org/10.1080/00031305.2016.1154108
- Weakley J, Mann B, Banyard H, McLaren S, Scott T, Garcia-Ramos A. Velocity-based training: from theory to application. Strength Cond J. 2021;43(2):31-49. https://doi.org/10.1519/SSC.0000000000000560 (cited as Weakley et al., 2021a)
- Weakley J, Morrison M, García-Ramos A, Johnston R, James L, Cole MH. The validity and reliability of commercially available resistance training monitoring devices: a systematic review. Sports Med. 2021;51(3):443-502. https://doi.org/10.1007/s40279-020-01382-w (cited as Weakley et al., 2021b)
- Webster KE, Hewett TE. What is the evidence for and validity of return-to-sport testing after anterior cruciate ligament reconstruction surgery? A systematic review and meta-analysis. Sports Med. 2019;49(6):917-929. https://doi.org/10.1007/s40279-019-01093-x
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. J Strength Cond Res. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- Wellsandt E, Failla MJ, Snyder-Mackler L. Limb symmetry indexes can overestimate knee function after anterior cruciate ligament injury. J Orthop Sports Phys Ther. 2017;47(5):334-338. https://doi.org/10.2519/jospt.2017.7285
- Wiesinger HP, Gressenbauer C, Kösters A, Scharinger M, Müller E. Device and method matter: a critical evaluation of eccentric hamstring muscle strength assessments. Scand J Med Sci Sports. 2020;30(2):217-226. https://doi.org/10.1111/sms.13569
- Williams S, West S, Cross MJ, Stokes KA. Better way to determine the acute:chronic workload ratio? Br J Sports Med. 2017;51(3):209-210. https://doi.org/10.1136/bjsports-2016-096589. Accepted manuscript: https://purehost.bath.ac.uk/ws/files/147466466/BJSM_correspondence_alternative_to_rolling_averages_r1.pdf (accessed 2026-10-02)
- Windt J, Gabbett TJ. Is it all for naught? What does mathematical coupling mean for acute:chronic workload ratios? Br J Sports Med. 2019;53(16):988-990. https://doi.org/10.1136/bjsports-2017-098925
- Zifchock RA, Davis I, Higginson J, Royer T. The symmetry angle: a novel, robust method of quantifying asymmetry. Gait Posture. 2008;27(4):622-627. https://doi.org/10.1016/j.gaitpost.2007.08.006
