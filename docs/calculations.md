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
  - [Training monotony and strain](#training-monotony-and-strain)
  - [Wellness z-score](#wellness-z-score)
  - [Taper volume reduction](#taper-volume-reduction)
  - [Intensity distribution](#intensity-distribution)
  - [Recovery questionnaire scores](#recovery-questionnaire-scores)
  - [Estimated load](#estimated-load)
- [Running load](#running-load)
  - [Total distance and distance per minute](#total-distance-and-distance-per-minute)
  - [High-speed running distance](#high-speed-running-distance)
  - [Accelerations and decelerations](#accelerations-and-decelerations)
  - [Peak demands](#peak-demands)
  - [Match-day load](#match-day-load)
- [Force plate](#force-plate)
  - [Countermovement jump height](#countermovement-jump-height)
  - [Reactive strength index-modified](#reactive-strength-index-modified)
  - [CMJ strategy and fatigue metrics](#cmj-strategy-and-fatigue-metrics)
  - [Isometric mid-thigh pull peak force](#isometric-mid-thigh-pull-peak-force)
  - [Eccentric hamstring force](#eccentric-hamstring-force)
  - [Dynamic strength index and eccentric utilization ratio](#dynamic-strength-index-and-eccentric-utilization-ratio)
- [Velocity-based training](#velocity-based-training)
  - [Mean concentric velocity](#mean-concentric-velocity)
  - [Velocity loss](#velocity-loss)
- [Limb symmetry](#limb-symmetry)
  - [Limb symmetry index](#limb-symmetry-index)
- [Composites](#composites)
  - [Readiness composite](#readiness-composite)
- [Testing profiles](#testing-profiles)
  - [Squad and position group percentile](#squad-and-position-group-percentile)
  - [Norm percentile](#norm-percentile)
- [Sprint testing](#sprint-testing)
  - [Sprint profile](#sprint-profile)
  - [Change of direction deficit](#change-of-direction-deficit)
  - [Repeated sprint scores](#repeated-sprint-scores)
- [Conditioning speeds](#conditioning-speeds)
  - [Maximal aerobic speed](#maximal-aerobic-speed)
  - [Anaerobic speed reserve](#anaerobic-speed-reserve)
  - [Interval distances](#interval-distances)
- [Heart rate and sleep](#heart-rate-and-sleep)
  - [HRV trends](#hrv-trends)
  - [Submaximal heart rate and heart rate recovery](#submaximal-heart-rate-and-heart-rate-recovery)
  - [Sleep trends](#sleep-trends)
- [Strength training load](#strength-training-load)
  - [Volume load](#volume-load)
  - [Estimated 1RM](#estimated-1rm)
  - [Personal bests and relative strength](#personal-bests-and-relative-strength)
- [Sport-specific counts](#sport-specific-counts)
  - [Count totals](#count-totals)
  - [Pitch and throw counts](#pitch-and-throw-counts)
  - [Jump counts](#jump-counts)
  - [Swim volume](#swim-volume)
  - [Bowling volume](#bowling-volume)
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
- **Vendor equivalents**: the matching metric in the VALD, Hawkin Dynamics, Catapult, Kinexon, STATSports, Polar, Firstbeat, WHOOP, Oura, GymAware, EliteForm, or Perch device reference files, how the vendor calculates it, and any difference in method
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
- A TE overestimated by 20% gives 1.87% for two single tests. Error correlation of 0.5 between consecutive tests gives 0.56% for two single tests, or 4.59% against a baseline of 10.

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
- Baseline mean of n values: against a mean of 10 prior tests, the 95% band is 1.96 × 0.6284 × √(1 + 1/10) = 1.2918 cm.
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
- A baseline window k and a minimum count of values, chosen by the user. If the user has none, the file offers at least 10 prior values, labeled as its own practice default.
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

**Worked example.** One athlete did a CMJ every 3 days, from 2026-08-29 to 2026-09-25: 40.2, 40.7, 41.0, 39.8, 40.6, 40.9, 39.5, 40.3, 41.2, and 40.0 cm. Today, 2026-09-28, the athlete jumped 37.6 cm. Judge today against the 10 prior tests:

1. Sum of the 10 prior values = 404.20 cm, so the baseline mean = 40.4200 cm.
2. Sum of squared deviations = 2.7560 cm². Divide by 9 to get 0.3062 cm².
3. Baseline SD = √0.3062 = 0.5534 cm.
4. z = (37.6 − 40.4200) / 0.5534 = −5.10.
5. Change from the baseline mean = −2.8200 cm.
6. Noise band with TE = 0.6284 cm: 1.96 × 0.6284 × 1.0488 = 1.2918 cm.
7. The drop is beyond the band by 2.8200 − 1.2918 = 1.5282 cm. That is still beyond the SWC of 0.6185 cm.
8. The TE came from 6 athletes, so t(5) = 2.57 applies. The band becomes 2.5706 × 0.6284 × 1.0488 = 1.6942 cm. The drop is still beyond it by 1.1258 cm.

Result: today is 5.10 of the athlete's usual SDs below baseline (window 10 prior tests, n = 10, sample SD). The drop is larger than measurement error, and clearly larger than the SWC. Report it as a flag for the practitioner to review, not as a diagnosis.

**Variants.** Use these variants when they fit:

- Rolling window of tests: the previous k tests. Use it when tests are irregular, such as weekly jumps. This is the default.
- Rolling window of days: the previous k calendar days. Use it only for daily measures. Missing days shrink the real number of values, so report n.
- Fixed baseline: the mean and SD of a set period, such as the first weeks of preseason. It does not drift. State the dates.
- Control limits: Sands et al. (2019) show limits at 1.5 and 2.0 × the baseline SD around the baseline mean, equal to z = ±1.5 and z = ±2.0. They are examples from a published case, not validated thresholds. With a 10-value baseline and pure noise, |z| > 2 flags about 8.9% of tests and |z| > 1.5 flags about 18.6%.

**What changes the number.** These choices change the z-score for the same athlete on the same day:

- Including today in the baseline: the last 10 values with today included give a mean of 40.1600 cm, an SD of 1.0532 cm, and z = −2.43 instead of −5.10.
- Window length: with the 4 prior tests, z = −3.71. With 3 prior tests, z = −4.64. Short windows give unstable SDs.
- Population SD: `STDEV.P` gives an SD of 0.5250 cm and z = −5.37.
- Team SD instead of the athlete's SD: dividing by the between-athlete SD of 3.0927 cm gives z = −0.91. That answers a different question.
- Small n: Swinton et al. (2018) show that a 95% interval based on a TE from 5 individuals needs a multiplier of 2.78 instead of 1.96.
- Own SD in place of TE: the baseline SD also holds biological variation, so a band built on it is never a measurement-error band. With at least 10 stable values, it gives the usual-variation band, `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`, with two states only. Today is outside that band when |z| > t(n − 1) × √(1 + 1/n), which is 2.37 for 10 values. With fewer than 10 values, do not build that band. See [Shared rules for judging change](#shared-rules-for-judging-change).
- Trend in the baseline: a baseline should be stable, with low variability and no clear trend (Sands et al., 2019). In a 30-test example that falls 0.1 cm per test from test 11, the rolling z against the prior 10 tests never reaches −2; its lowest value is −1.87. Before test 30, the rolling mean has drifted to 38.5500 cm, with an SD of 0.5603 cm. Against the fixed baseline of tests 1 to 10 (mean 40.0000 cm), test 30 is 2.5000 cm lower, beyond the noise band of 1.2918 cm. Pair a rolling baseline with a fixed reference period or a trend line.
- Mixed conditions: a baseline that spans preseason and in-season, or an illness period, changes both the mean and the SD.

**Units and typical range.** The z-score has no units. The baseline mean and SD have the units of the measure. The file gives no typical z-score range or flag threshold. Thresholds are choices, not facts. Name the threshold and its source. No source used in the file sets a best window for an individual baseline. Weir (2005) states there is no consensus on the sample size needed for a stable SEM. Hopkins (2017) asks for at least 10 values for modest precision, and Swinton et al. (2018) say more than 10 to 20 tests may be needed. So the file offers at least 10 prior values as its practice default, and its code templates use a window of 10 and a minimum of 10. Report n with every z-score.

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

These metrics describe internal load, how recent load compares with longer-term load, how a wellness answer compares with the athlete's own usual answers, how much volume dropped in a taper, how training was spread across intensity zones, and recovery questionnaire scores.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Session RPE load | `session_rpe_load_au = rpe_cr10 × duration_min` | AU | [session-rpe-load.md](../skills/load-and-wellness/references/session-rpe-load.md) |
| Daily and weekly session RPE load | Sum of session loads in a day; sum of daily loads in a week | AU | [session-rpe-load.md](../skills/load-and-wellness/references/session-rpe-load.md) |
| %HRmax and %HRR | `%HRmax = HR ÷ HRmax × 100`, `%HRR = (HR − HRrest) ÷ (HRmax − HRrest) × 100` | % | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Edwards TRIMP | `(min in zone 1 × 1) + (min in zone 2 × 2) + (min in zone 3 × 3) + (min in zone 4 × 4) + (min in zone 5 × 5)` | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Banister TRIMP | `Σ (t_i × x_i × 0.64 × e^(1.92 × x_i))` (male weighting) or `Σ (t_i × x_i × 0.86 × e^(1.67 × x_i))` (female weighting), summed over samples. Session mean fallback: `duration_min × x × 0.64 × e^(1.92 × x)` (male weighting) or `duration_min × x × 0.86 × e^(1.67 × x)` (female weighting) | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| Lucia TRIMP | `(min below VT × 1) + (min from VT to RCP × 2) + (min above RCP × 3)` | AU | [heart-rate-load.md](../skills/load-and-wellness/references/heart-rate-load.md) |
| ACWR, rolling coupled | Mean daily load, last 7 days ÷ mean daily load, last 28 days | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| ACWR, rolling uncoupled | Mean daily load, last 7 days ÷ mean daily load, days 8 to 28 back | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| ACWR, EWMA | EWMA with N = 7 ÷ EWMA with N = 28, with λ = 2 ÷ (N + 1) | No unit | [acwr.md](../skills/load-and-wellness/references/acwr.md) |
| Training monotony | Mean daily load over 7 days ÷ SD of the 7 daily loads, with rest days as 0 | No unit | [monotony-and-strain.md](../skills/load-and-wellness/references/monotony-and-strain.md) |
| Training strain | Weekly load × monotony | Unit of the load (AU for session RPE load) | [monotony-and-strain.md](../skills/load-and-wellness/references/monotony-and-strain.md) |
| Wellness z-score | `z = (x_today − baseline_mean) ÷ baseline_sd` | No unit (SD units) | [wellness-z-score.md](../skills/load-and-wellness/references/wellness-z-score.md) |
| Taper volume reduction | `(baseline_weekly_volume − taper_weekly_volume) ÷ baseline_weekly_volume × 100` | % | [taper-and-distribution.md](../skills/load-and-wellness/references/taper-and-distribution.md) |
| Intensity distribution | Share of time or sessions in Z1, Z2, and Z3. Pyramidal: Z1 > Z2 > Z3. Polarized: Z1 > Z3 > Z2 and `PI = log10(Z1_share ÷ Z2_share × Z3_share × 100)` above 2.00 | Shares as fractions or %; PI no unit | [taper-and-distribution.md](../skills/load-and-wellness/references/taper-and-distribution.md) |
| Hooper index | `sleep + stress + fatigue + soreness`, each 1 to 7 | Points, 4 to 28 | [recovery-questionnaires.md](../skills/load-and-wellness/references/recovery-questionnaires.md) |
| Total Quality Recovery (TQR) | Single rating, 6 to 20 | Points | [recovery-questionnaires.md](../skills/load-and-wellness/references/recovery-questionnaires.md) |
| Perceived Recovery Status (PRS) | Single rating, 0 to 10 | Points | [recovery-questionnaires.md](../skills/load-and-wellness/references/recovery-questionnaires.md) |
| BAM total mood disturbance | Sum of five negative mood items + inverted vigour | Points, 0 to 24 or 6 to 30 by the form's numbering | [recovery-questionnaires.md](../skills/load-and-wellness/references/recovery-questionnaires.md) |
| Estimated load, athlete rate | `rate_athlete = Σ load_measured ÷ Σ playing_min_measured`, then `estimated_load = rate_athlete × playing_min_today` | Unit of the load it replaces | [estimated-load.md](../skills/load-and-wellness/references/estimated-load.md) |
| Held-out error of an estimate | `abs(estimate_without_game − load_measured) ÷ load_measured × 100` | % | [estimated-load.md](../skills/load-and-wellness/references/estimated-load.md) |

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
5. Add daily loads across each calendar week, Monday to Sunday unless the user names another start day, to get weekly load. Do this even when the user asked only for daily load. Report how many days had complete data and how many were marked ill, unavailable, or modified. Mark a week with any missing day as incomplete, and give its total with the number of days it covers, such as 6 of 7 days.

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

- Duration definition: adding a 15-minute warm-up to Monday's practice changes it from 450 AU to 6 × 90 = 540 AU. No consensus says whether duration includes the warm-up or the cool-down. Use one rule for each session type, such as training and matches, and record it. If the user has no rule, the file offers this default, labeled as its own choice: training time from the start of the team warm-up to the end of the last drill, without a separate cool-down. Pustina et al. (2017) defined training duration the same way: it includes the warm-up and recovery periods and excludes the cool-down. For matches, ask whether to use minutes played. In one study of college soccer, match loads from minutes played correlated with GPS distance more closely than loads from total match duration: r = 0.808 against 0.566 (Pustina et al., 2017). Under minutes played, an unused substitute's warm-up scores 0 AU. The cool-down can change the rating itself, not only the minutes (Rodríguez-Marroyo et al., 2021).
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
- For Banister TRIMP, the weighting (curve) the user chooses for each athlete. Never ask for the athlete's gender, and never infer the weighting from a name or roster data.

**Calculation.** Express intensity as %HRmax or %HRR, then apply a TRIMP (training impulse) method. Name the method, the HRmax source, and the HRrest value with every result:

```text
%HRmax = HR ÷ HRmax × 100
%HRR   = (HR − HRrest) ÷ (HRmax − HRrest) × 100

TRIMP_Edwards  = (min in zone 1 × 1) + (min in zone 2 × 2) + (min in zone 3 × 3)
               + (min in zone 4 × 4) + (min in zone 5 × 5)

x_i = (HR_i − HRrest) ÷ (HRmax − HRrest)
Male weighting:    TRIMP_Banister = Σ ( t_i × x_i × 0.64 × e^(1.92 × x_i) )
Female weighting:  TRIMP_Banister = Σ ( t_i × x_i × 0.86 × e^(1.67 × x_i) )

Session mean fallback, only when nothing finer than the session mean and duration exists:
x_mean = (HR_mean − HRrest) ÷ (HRmax − HRrest)
Male weighting:    TRIMP_Banister_mean = duration_min × x_mean × 0.64 × e^(1.92 × x_mean)
Female weighting:  TRIMP_Banister_mean = duration_min × x_mean × 0.86 × e^(1.67 × x_mean)

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
- `i`: one heart rate sample, or one phase of the session. `Σ` adds the terms for every sample or phase.
- `HR_i`: the heart rate of sample `i`, or the mean heart rate of phase `i`, in bpm
- `t_i`: the length of sample or phase `i`, in minutes. For 1 Hz data, each sample lasts 1 ÷ 60 min.
- `x_i`, `x_mean`: the delta heart rate ratio, %HRR as a fraction, from 0 at rest to 1 at HRmax (Banister et al., 1992)
- `HR_mean`: the mean heart rate of the whole session (Paulson et al., 2015; Hourcade et al., 2018)
- `duration_min`: session length in minutes
- `0.64 × e^(1.92 × x)` and `0.86 × e^(1.67 × x)`: weighting factors that give more credit to high-intensity time, based on the exponential rise of blood lactate with intensity (Banister et al., 1992). Banister (1991) prints both multiplier forms. The female form appears earlier, in Banister and Hamilton (1985). Use this multiplier form by default, and name it with every result.
- Banister default: add one term for each sample whenever second-by-second heart rate exists, or one term for each phase when only phase means exist. Banister scored each phase from its length and heart rate, recorded periods at different intensities separately, and added the phase scores to give the session total (Banister, 1991, pp. 406-409). Polar also computes its Banister TRIMP each second and adds the results (Polar, 2025). Use the session mean only as a fallback, and label it "session mean". Paulson et al. (2015), Hourcade et al. (2018), and Tomoto et al. (2026) used the session mean. It cannot see intervals: Hourcade et al. (2018) found it did not separate two sessions with almost equal mean heart rate (p = 0.420). The weighting curves upward, so the per-sample sum is larger than the session mean whenever heart rate varies. Never mix the two in one athlete's history.
- Spreadsheet guard: a plain `SUMPRODUCT` reads a blank sample as 0 bpm, which adds a negative term. The reference file's formula multiplies each term by `(B2:B1201<>"")`, so a blank sample adds nothing.
- `e`: the base of natural logarithms, about 2.718
- `VT`, `RCP`: the heart rates at the first and second breathing thresholds in a lab ramp test (Lucia et al., 2003). The multipliers 1, 2, and 3 are reported by Paulson et al. (2015).

Follow these steps from raw inputs:

1. Find the sampling interval from the timestamps, in seconds.
2. Find gaps, where timestamps jump or `hr_bpm` is 0 or blank. Remove those samples. Do not count them as 0 bpm.
3. Find artifacts the user or device flags. Remove them only with the user's agreement, and report how many there were.
4. Keep plausible values above HRmax. If HRmax is age-predicted, tell the user the setting is probably too low. If HRmax is a Yo-Yo intermittent recovery level 2 peak, label it "may be about 2 % below HRmax on average (Krustrup et al., 2006)", and apply no correction factor.
5. Calculate time in each zone in minutes: count samples in the zone, multiply by the sampling interval, and divide by 60.
6. Calculate the TRIMP the user asked for, in AU. For Banister TRIMP, use the per-sample sum, and use the session mean only when nothing finer exists.
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
- Banister per-sample sum, measured HRmax: each block adds minutes × x × weighting. With the male weighting, the blocks at 110, 140, 180, 150, and 120 bpm add 1.42, 3.23, 15.85, 8.20, and 1.27 AU, so TRIMP = 30.0 AU from the unrounded terms. The female weighting gives 33.8 AU.
- Banister per-sample sum, predicted HRmax: 36.1 AU male and 40.0 AU female at 194 bpm, and 32.5 AU and 36.4 AU at 200 bpm.
- Banister session mean fallback, measured HRmax: x = (148.5 − 55) ÷ (205 − 55) = 0.6233. Male weighting 0.64 × e^(1.92 × 0.6233) = 2.1181, so TRIMP = 20 × 0.6233 × 2.1181 = 26.4 AU. Female weighting 2.4355, so TRIMP = 30.4 AU.
- Banister session mean fallback, predicted HRmax 194 bpm: x = 0.6727, giving 31.3 AU male and 35.6 AU female. At 200 bpm, x = 0.6448, giving 28.5 AU and 32.6 AU.
- Lucia: 14 min below VT and 6 min above RCP, so 14 × 1 + 0 × 2 + 6 × 3 = 32.0 AU. HRmax does not change it.

The per-sample sum is 13.5 % higher than the session mean with the male weighting and 11.2 % higher with the female weighting. Mean %HRmax is 72.4 % with the measured HRmax and 76.5 % with 194 bpm. An HRmax 11 bpm too low raises every HRmax-based result: the per-sample Banister sum rose from 30.0 to 36.1 AU male and from 33.8 to 40.0 AU female.

A steady 20-minute session at the same mean of 148.5 bpm gives 26.4 AU male and 30.4 AU female by either Banister form, because heart rate is constant. It gives 60.0 AU Edwards and 20.0 AU Lucia. The session mean gives the interval session the same 26.4 AU, so it cannot tell the two sessions apart. The per-sample sum and time in zone can. These methods do not agree on which session was harder: the per-sample sum and Lucia TRIMP score the interval session higher, and Edwards TRIMP scores the steady session higher.

**Variants.** Know these variants before you compare numbers:

- %HRR, the Karvonen method (Karvonen et al., 1957): %HRR tracks the percentage of oxygen uptake reserve more closely than the percentage of maximal oxygen uptake (Swain et al., 1998). The same heart rate gives a different percentage under each method, so never mix them in one report. Edwards defined his zones on %HRmax.
- HRmax source: use a measured HRmax when one exists. Without a maximal test, label the highest artifact-checked value from a maximal intermittent field test as HRpeak, with the test name and date. In the Yo-Yo intermittent recovery level 1 test, peak heart rate in 17 men was 187 ± 2 bpm, against 189 ± 2 bpm on a treadmill to exhaustion (Krustrup et al., 2003). In the level 2 test, heart rate at exhaustion was 98 ± 1 % of HRmax in 13 men (Krustrup et al., 2006). Accept a level 2 peak as HRpeak, labeled "may be about 2 % below HRmax on average (Krustrup et al., 2006)", with no correction factor. In 20 team sport players, heart rate at exhaustion did not differ between the 30-15 Intermittent Fitness Test and a continuous incremental test (Buchheit et al., 2009). Take HRpeak as the highest 5-second rolling average of artifact-checked samples, as Paulson et al. (2015) did in a lab test. This window is a practice default of the file, not a published rule. State it with the result. When a later session gives a higher artifact-checked 5-second average, raise HRpeak to that value.
- Age-predicted HRmax: 220 − age underestimates HRmax in older adults (Tanaka et al., 2001). 208 − 0.7 × age comes from Tanaka et al. (2001). 211 − 0.64 × age had a standard error of the estimate (SEE) of 10.8 bpm in 3,320 healthy adults (Nes et al., 2013).
- Banister exponent-only form: the appendix of Banister et al. (1992) prints e^(1.92 × x) and e^(1.67 × x) without the 0.64 and 0.86 multipliers. Banister's 1985 and 1991 texts include the multipliers. The exponent-only form gives larger numbers and reverses which sex scores higher. Ask which form a tool uses, and whether it sums samples or uses the session mean.
- Banister session mean: the fallback form, for files with only the session mean heart rate and duration. It is the form used in the validation papers checked for the file (Paulson et al., 2015; Hourcade et al., 2018; Tomoto et al., 2026). The whole-session mean comes from these later papers, not from Banister. It treats the whole session as one phase, so it cannot see intervals. Label it "session mean", and keep it as a separate series. Never mix it with the per-sample sum in one athlete's history.
- Individualized TRIMP (iTRIMP): a weighting built from each athlete's own heart rate and blood lactate profile (Manzi et al., 2009). Use it only when each athlete has a lactate test.
- Mean heart rate and mean %HRmax: simple summaries that hide how intensity was spread. Hourcade et al. (2018) found the summated zone load differed between two sessions with almost equal mean heart rate (p = 0.007), while Banister TRIMP from the session mean did not (p = 0.420). Report time in zone next to any mean.

The published Banister weightings are labeled male and female. They come from blood lactate curves in trained men and women (Banister, 1991). They say nothing about an athlete's gender. No published guidance was found for athletes outside those categories. At a delta heart rate ratio from 0.3 to 1.0, the female weighting gives 5 to 25 % more load than the male weighting. Follow these steps to choose a weighting:

1. Offer Edwards, Lucia, or iTRIMP first. Edwards TRIMP has no sex term.
2. If the user wants Banister TRIMP, ask which curve to use for each athlete. Never ask for the athlete's gender, and never infer the weighting from a name or roster data. Use this wording: "Banister TRIMP has two published curves, labeled male and female, built from blood lactate in trained men and women. Which curve should I use for this athlete? If you are unsure, I can show both, or use Edwards TRIMP, which has no sex term."
3. If the user does not choose, show both results, each labeled with its weighting.
4. Store both results for every session.
5. Record the chosen weighting, and never switch weightings within one athlete's history.

**What changes the number.** These choices change the result when the athlete's effort does not change. Figures use the measured HRmax, the male weighting, and the per-sample Banister sum unless stated:

- HRmax source: an age formula 11 bpm low raised Edwards TRIMP from 53.0 to 64.0 AU and Banister TRIMP from 30.0 to 36.1 AU.
- HRrest: Banister TRIMP was 32.0 AU at 45 bpm, 30.0 AU at 55 bpm, and 27.8 AU at 65 bpm.
- Boundary rule: at HRmax 200 bpm, the rule alone moved Edwards TRIMP from 53.0 to 64.0 AU, a 20.8 % swing.
- Banister form: the exponent-only form scored 46.8 AU male and 39.2 AU female, against 30.0 AU and 33.8 AU with the multipliers, so the sex ordering reverses.
- Per-sample sum or session mean: the session mean fallback gave 26.4 AU male and 30.4 AU female, against 30.0 AU and 33.8 AU from the per-sample sum.
- Dropouts: a 60-second dropout at 180 bpm recorded as 0 bpm cut mean heart rate from 148.50 to 139.50 bpm and Banister TRIMP from 30.0 to 27.2 AU. Each zero adds a small negative term. Removing it instead gave 19 min, 146.84 bpm, and 27.3 AU. With the session mean fallback, zeros gave 21.3 AU and removal gave 24.1 AU, against 26.4 AU. Edwards TRIMP fell to 49.0 AU either way. Lucia TRIMP fell to 30.0 AU with zeros and 29.0 AU with removal. A chest strap agreed best with an electrocardiogram (Gillinov et al., 2017).
- Artifact spikes: a false 15-second spike to 230 bpm raised Edwards TRIMP from 53.0 to 53.5 AU and Banister TRIMP from 30.0 to 31.4 AU.
- Sampling and averaging: with 30-second transitions, Edwards TRIMP was 53.4 AU at 1 s, 53.3 AU from 5 s averages, and 54.0 AU from 60 s averages. Lucia TRIMP was 31.2, 31.1, and 29.0 AU.
- Cardiovascular drift: heart rate rises during prolonged exercise (Coyle & González-Alonso, 2001; Achten & Jeukendrup, 2003). An illustrative drift of 0.5 bpm per minute raised Edwards TRIMP from 53.0 to 59.0 AU and Banister TRIMP from 30.0 to 33.8 AU.
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
- Polar `cardio_load`: Banister TRIMP summed from per-second heart rate, using resting heart rate, maximum heart rate, and gender. A 60-minute session typically scores 70 to 130. Polar sums per-second terms, which matches the reference file's default per-sample sum. Polar does not publish the scaling of the sum.
- Polar `training_load`: an older load score with unpublished method. Do not compare it with `cardio_load` or with any TRIMP.
- Firstbeat `TRIMP`: Banister TRIMP, T x HRratio x 0.64 x e^(1.92 x HRratio), where HRratio = (HRex − HRrest) / (HRmax − HRrest). Firstbeat uses beat-to-beat heart rate and a lower intensity limit that is not published. A mean-heart-rate TRIMP from another system gives different numbers. The Firstbeat file maps it to no reference file.
- Firstbeat `TRIMP/min`: TRIMP divided by session duration. The period used for laps and sessions is not published. The Firstbeat file maps it to no reference file.
- Firstbeat `%HRmax` and time in heart rate zones: zone limits are set in %HRmax, and the default limits are not published. The API numbers zones from the top, so `zone1Time` is the highest zone. The Firstbeat file maps both to no reference file.
- Catapult: the 10 Hz sensor data carry `hr` in beats per minute. The Catapult file maps no heart rate load metric.
- STATSports heart rate metrics: average and maximum heart rate, and time in heart rate zones 1 to 6, with zones set as percentages of each player's maximum heart rate. There are six zones, not five.
- STATSports Heart Rate Exertion (HRE): each heart rate sample gets a weight that rises on a convex curve as heart rate nears the maximum, and weight times duration in seconds is summed. The weights are not published. It is not Edwards TRIMP, so do not mix the two.

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
- An `availability` column that marks ill, unavailable, or modified-training days

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

### Training monotony and strain

**What it measures.** Training monotony describes how evenly an athlete's load was spread across the days of one week. Training strain combines the week's total load with its monotony. Put this sentence directly under each monotony or strain table or chart, and in the same paragraph as each value in text: "Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness."

Read these limits before you use them:

- Foster (1998) followed 25 athletes. The abstract reports that a high share of their illnesses could be accounted for when athletes passed thresholds identified for each athlete, mostly thresholds of strain. That explains past illnesses in the same athletes. The abstract describes no test of whether strain predicts illness in new data.
- In the summary by Jones et al. (2017) of Foster (1998), spikes above each athlete's own threshold came before 77% of illnesses for monotony and 89% for strain. Yet 52% of the monotony spikes and 59% of the strain spikes were not followed by illness.
- A systematic review found conflicting evidence for monotony and strain, and concluded that the literature does not support their role in monitoring and injury prevention (Jones et al., 2017).
- Training-load measures cannot tell you whether a change in load raises or lowers injury risk (Impellizzeri et al., 2020b).
- Jones et al. (2017) describe the spikes in Foster (1998) as monotony above 2.0. The file could not confirm the figure in Foster's full text, and the abstract describes thresholds for each athlete. Do not use 2.0 or any other value as a threshold.

**Inputs.** The calculation needs these data:

- One daily load total per athlete per calendar day in one load measure, such as session RPE load in AU, with sessions on the same day added first
- `0` on rest days, and missing for days with training but no recorded load
- An `availability` column that marks ill, unavailable, or modified-training days

**Calculation.** Use the weekly form described by Haddad et al. (2017), from Foster (1998):

```text
weekly_load_au = sum of the 7 daily loads
monotony       = mean daily load over the 7 days ÷ SD of the 7 daily loads
strain_au      = weekly_load_au × monotony
```

The terms mean the following:

- Mean daily load: `weekly_load_au ÷ 7`, in AU. Haddad et al. (2017) define it as the average daily load during the week. The file counts all 7 days, with `0` AU on rest days. The sources the file could read do not state the rest-day rule in words.
- SD: standard deviation of the 7 daily loads, in AU. The sample SD divides by n − 1, here 6: Excel `STDEV.S`, Google Sheets `STDEV`, R `sd()`, Python `statistics.stdev()`, and pandas `.std()`. The population SD divides by n, here 7: Excel `STDEV.P`, Google Sheets `STDEVP`, Python `statistics.pstdev()`, and NumPy `np.std()` by default. The sources the file could read do not say which SD Foster used. The file uses the sample SD as its labeled default.
- `monotony`: no unit. It is 1 ÷ the coefficient of variation (CV).
- `strain_au`: weekly load × monotony (Haddad et al., 2017). It keeps the unit of the load.

The Foster (1998) abstract defines monotony as the daily mean divided by the SD, and strain as load multiplied by monotony. It does not state the window, the type of SD, or the rest-day rule.

Follow these steps from raw inputs:

1. Add session loads into one daily load per `athlete_id` and `date`. Mark the day as missing if any session that day has a missing load.
2. Build a full calendar for each athlete, one row per day. Put `0` on rest days. Leave days with training but no recorded load as missing.
3. Check that every calendar day has exactly one row. Stop and fix the data if it does not.
4. Ask the user for the window and the SD. Use Monday-to-Sunday calendar weeks and the sample SD if they have no preference, and label both as the file's choice.
5. For each week, check that all 7 days have a daily load. If any day is missing, report the weekly load with the number of days it covers, and report monotony and strain as missing.
6. Add the 7 daily loads to get the weekly load. Divide by 7 to get the mean daily load.
7. Calculate the SD of the 7 daily loads. If it is 0, report monotony and strain as undefined, with the status `no variation`.
8. Divide the mean daily load by the SD to get monotony. Multiply the weekly load by the unrounded monotony to get strain.
9. Report the weekly load, monotony, and strain together, with the SD type, the window, the load measure, and the caveat sentence.

**Worked example.** One athlete's calendar week from Monday 2026-08-03, in session RPE load. Monday has a practice (6 × 75 = 450 AU) and a lift (4 × 45 = 180 AU). Sunday is a rest day:

| Mon | Tue | Wed | Thu | Fri | Sat | Sun | Weekly load |
|---|---|---|---|---|---|---|---|
| 630 | 630 | 300 | 480 | 120 | 720 | 0 | 2,880 AU |

The mean daily load is 2,880 ÷ 7 = 411.43 AU. The sum of squared differences from the mean is 462,085.71 AU². The sample SD is √(462,085.71 ÷ 6) = 277.51 AU, and the population SD is √(462,085.71 ÷ 7) = 256.93 AU.

| SD | Monotony | Strain (AU) |
|---|---|---|
| Sample, 277.51 AU | 411.43 ÷ 277.51 = 1.48 | 2,880 × 1.4825 = 4,269.7 |
| Population, 256.93 AU | 411.43 ÷ 256.93 = 1.60 | 2,880 × 1.6013 = 4,611.8 |

Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

The next week has daily loads of 500, 620, 320, 560, 280, 0, and 0 AU: weekly load 2,280 AU, monotony 1.28, and strain 2,927.2 AU with the sample SD. The rolling 7-day window ending Friday 2026-08-14 gives a weekly load of 3,000 AU, monotony 1.75, and strain 5,238.1 AU, higher than either calendar week. Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

**Variants.** These variants are in use. Name the one you use with every value:

- Sample or population SD: for a 7-day week, the population SD gives monotony and strain √(7 ÷ 6) = 1.080 times the sample SD values, 8.0% higher.
- Calendar or rolling weeks: a calendar week gives one value per week, on its last day. A rolling week gives one value per day, from the 7 days ending that day. The rolling value on the last day of a calendar week equals the calendar value.

**What changes the number.** These choices change the result when the athlete's training does not change:

- SD type: 1.60 with the population SD against 1.48 with the sample SD in the worked example.
- Rest days: dropping the Sunday rest day leaves 6 values and raises monotony from 1.48 to 2.09, and strain from 4,269.7 to 6,009.3 AU.
- Missing days entered as zero: entering a missing Wednesday as 0 gives a weekly load of 2,580 AU and monotony of 1.16. Report a week with a missing day as incomplete instead.
- Sessions counted as days: using the 7 session loads plus the rest day as 8 values gives 1.42 instead of 1.48.
- Rolling window end day: in the worked example, rolling monotony runs from 1.28 to 1.75 across one week. Compare rolling values on the same weekday.
- Rounding before strain: 2,880 × 1.48 = 4,262.4 AU, not 4,269.7 AU.
- Identical or near-identical days: seven equal days give an SD of 0, so monotony is undefined. Six days at 400 AU and one at 410 AU give a monotony of 106.21.
- Load measure: monotony from session RPE load and from distance are different numbers. Strain from distance is in m.

**Units and typical range.** Monotony has no unit. Strain has the unit of the load. Neither has a population range that applies across sports, ages, and training phases. From the arithmetic of the formula, a 7-day week with at least one training day has a monotony of at least 1 ÷ √7 = 0.38 (sample SD) or 1 ÷ √6 = 0.41 (population SD). A week with at least one rest day at 0 AU has a monotony of at most 6 ÷ √7 = 2.27 (sample SD) or √6 = 2.45 (population SD). A week with no rest day has no fixed ceiling. Strain runs from 0 upward. Monotony and strain need 7 consecutive days with no missing day.

**Vendor equivalents.** None. The Polar Team Pro file describes Polar Strain as the 7-day average daily cardio load. It shares the name but is not Foster's strain: it has no SD and no monotony in it. It sits with the ACWR loads above.

**Reference file.** [monotony-and-strain.md](../skills/load-and-wellness/references/monotony-and-strain.md)

### Wellness z-score

**What it measures.** A wellness z-score shows how far today's wellness answer sits from that athlete's own usual answers, in units of that athlete's usual day-to-day spread. Self-reported measures tracked changes in training load more consistently than common objective measures in a systematic review (Saw et al., 2016). Most daily wellness forms use single questions, and the most used single items in sport have not been validated (Jeffries et al., 2020). A z-score describes an unusual answer. It does not explain the cause, and it does not identify illness, injury, or overtraining.

**Inputs.** The calculation needs these data:

- One row per athlete per day with `athlete_id`, `date`, and one column per item, such as `sleep`, `soreness`, `fatigue`, `stress`, and `mood`, in form points such as 1 to 5
- Each item's direction, confirmed with the user
- The baseline window and the minimum number of baseline days, chosen by the user. If the user has none, the file offers 14 answers inside a 28-day window, labeled as its own choice, and never fewer than 10 answers covering at least one full training week.
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
8. For a squad flag list, flag on the total z-score or on the practitioner's raw-answer rule, not on single-item z-scores. Beside each flagged athlete, show each item's raw answer and change in points, with the total z-score, status, baseline window, and baseline day count.
9. In the athlete detail view, report each item's raw answer, change in points, z-score labeled approximate, status, baseline window, and baseline day count.

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

- Total z-score: add the items into a daily total, then standardize the total against the athlete's baseline of totals. Use it by default to flag athletes across a squad. Beside each flagged athlete, show each item's raw answer and change in points.
- Item-level z-score: one z-score per question. Show it in the athlete detail view, labeled approximate, after the raw answer and the change in points. It keeps the reason for a change visible. Do not use it to build a squad flag list.
- Rolling baseline: the previous N calendar days, such as 28. It follows slow changes, but it also absorbs a slow decline.
- Fixed baseline: a set period, such as a stable block of normal training. It does not drift, but it ages.
- Raw-answer flag: a practitioner may also flag on the raw answer, such as any soreness of 1 or 2. That is their choice. It can replace or join the total z-score in a squad flag list. Label it as theirs.

Treat the numbers with these limits in mind:

- A one-direction cut-off of z = −2 flags 2.3% of ordinary days when the baseline mean and SD are known, and 3.8% with a 14-day baseline. Across 25 athletes flagged on the total, that is 0.57 or 0.94 flags a day by chance, and a 43.7% or 61.8% chance of at least one. With 7 baseline answers the rate for one athlete is 5.5%, with 10 it is 4.4%, and with 28 it is 3.0%. These figures come from the normal and t distributions. The real rate on a 1 to 5 scale can be higher or lower.
- A small baseline gives an unstable SD. The 95% confidence interval for the true SD runs from about 0.64 to 2.20 times the sample SD with 7 values, 0.69 to 1.83 times with 10, 0.72 to 1.61 times with 14, and 0.79 to 1.36 times with 28. With 14 baseline days, a z-score of −3.13 matches about −1.94 to −4.32 against the true SD, which is the z-score multiplied by 0.621 to 1.379.
- Today's distance from a mean of n days has a spread of baseline SD × √(1 + 1/n). This is the standard prediction interval for one new value against a mean of n values (NIST, Dataplot reference manual, after Hahn and Meeker, 1991). With n = 14, √(1 + 1/14) = 1.035, so the sleep z-score of −3.13 becomes −3.03 on that scale.
- The baseline SD is not a typical error. It mixes real day-to-day change with error. Do not use it as TE, and do not borrow a noise band built on TE for wellness answers.
- Daily answers are often autocorrelated, and answers on a short point scale are not normally distributed, so treat these factors as a rough guide only.
- On a short point scale, z-scores jump in steps. For a single item, report the raw answer and the change in points first, and the z-score second as approximate. In a simulation run for the file (stable athletes, 14-day baselines, independent days), the chance rate of z ≤ −2 on one item ranged from 3.3% to 5.6% depending on the usual answer, against 3.8% expected, and most flags were a one-point drop.
- Keep single-item z-scores out of squad flag lists. With 5 items and a 14-day baseline, about 17% to 20% of athletes get at least one item flagged on an ordinary day by chance, treating the items as independent. That is 4 or 5 of 25 athletes a day, against about 1 when you flag on the total. The 17.5% comes from the t distribution, 1 − (1 − 0.0377)^5, and a simulation of 1 to 5 answers run for the skill gave about 20% for a squad with mixed usual answers, and about 25% when every usual answer was 4.25. Flag the squad on the total or on the practitioner's raw-answer rule, and show each item's raw answer and change in points beside each flagged athlete. Keep item z-scores, labeled approximate, in the athlete detail view.
- We found no peer-reviewed source that sets a minimum number of baseline days. Ask the user, and report the number of baseline days with every z-score. If the user has no number, the file offers 14 baseline answers inside a 28-day window, labeled as its own choice, and never fewer than 10 answers covering at least one full training week. Ten matches the floor the monitoring-statistics skill offers for an individual baseline. A user's choice below 10 is applied and labeled as the user's choice. A baseline should be stable, with low variability and no clear trend (Sands et al., 2019). The file infers, as its own suggestion, that a baseline should cover at least one full training week.
- Report the number of flags expected by chance next to the number found. Recommend a repeat answer or a conversation with the athlete before anyone acts on a single flag (Barnett et al., 2005).

**What changes the number.** These choices change the result when the athlete has not changed:

- Baseline length: with the last 10 days as the baseline, today's sleep z-score is −3.35 (mean 3.90, SD 0.57) instead of −3.13 with 14 days.
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

### Taper volume reduction

**What it measures.** Taper volume reduction is how much weekly training volume dropped in a taper, as a percentage of normal training. A taper is a planned cut in training before a competition. It describes what was done. It does not say what should be done. A meta-analysis of 27 studies found the largest performance effect for a 2-week taper in which volume was reduced exponentially by 41% to 60%, with intensity and frequency kept the same (Bosquet et al., 2007). Its authors say this seems to be the most efficient strategy. The file presents that as a pooled study finding, not a target. In 14 team-sport studies, tapering improved maximal power, maximal oxygen uptake, repeated sprint ability, and change of direction speed, but too few studies compared taper strategies to support recommendations (Vachon et al., 2021). 91% of 58 strength and conditioning practitioners (Washif et al., 2025) and 99% of 146 weightlifters (Winwood et al., 2023) reported tapering.

**Inputs.** The calculation needs these data:

- Weekly totals per athlete for volume, training minutes, session count, and session RPE load, with a week holding any missing session value marked missing
- The baseline weeks and the taper weeks, chosen by the user. If the user has none, the file offers the 4 full calendar weeks before the taper, labeled as its own choice.
- The volume unit: minutes, distance, volume load, or session RPE load

**Calculation.** Use this formula:

```text
reduction_pct = (baseline_weekly_volume − taper_weekly_volume) ÷ baseline_weekly_volume × 100
frequency_change_pct = (taper_sessions_per_week − baseline_sessions_per_week) ÷ baseline_sessions_per_week × 100
intensity_au_per_min = weekly session RPE load ÷ weekly training minutes
```

The terms mean the following:

- `baseline_weekly_volume`: the mean weekly volume over the named baseline weeks. Missing if any baseline week is missing. A baseline of 0 or less gives no reduction in every tool.
- `taper_weekly_volume`: one taper week, or the mean of the taper weeks. Name which.
- `intensity_au_per_min`: the time-weighted mean session RPE, the file's own choice of intensity measure for session RPE data.

Session RPE load falls when sessions get shorter and when they feel easier, so the file measures volume in minutes, distance, or volume load when volume and intensity must stay apart.

Follow these steps from raw inputs:

1. Ask for the baseline weeks, the taper weeks, and the volume unit.
2. Add each athlete's sessions into weekly totals. Keep a week with any missing session value as missing.
3. Calculate the baseline mean. Report it as missing if any baseline week is missing.
4. Calculate the reduction for each taper week and for the taper mean.
5. Report the frequency change and the intensity measure beside each reduction.

**Worked example.** One athlete, 4 baseline weeks from 2026-08-03 and 2 taper weeks:

| Week | Phase | Minutes | Session RPE load (AU) | Sessions |
|---|---|---|---|---|
| 2026-08-03 to 2026-08-24 | Baseline, 4 weeks | 480, 510, 460, 500 | 3,120, 3,340, 2,980, 3,260 | 6 each |
| 2026-08-31 | Taper | 330 | 2,050 | 6 |
| 2026-09-07 | Taper | 240 | 1,560 | 5 |

The baseline is 487.5 min a week. Taper week 1 is a 32.3% cut, week 2 a 50.8% cut, and the taper mean of 285 min a 41.5% cut. In session RPE load, the cut is 43.1% (3,175 to 1,805 AU). Intensity fell 2.8%, from 6.51 to 6.33 AU per minute. Sessions went from 6 a week to 6, then 5.

**Variants.** These variants are in use. Name the one you use with every value:

- Volume unit: minutes, distance, volume load, or session RPE load.
- Taper weeks one by one, or as a mean.
- Against the baseline mean, or week on week.

**What changes the number.** These choices change the result when the training does not change:

- Baseline weeks: in session RPE load, the taper mean is a 43.1% cut against the 4-week mean, 44.6% against the last baseline week, and 46.0% against the peak week.
- Week on week: taper week 2 is a 50.9% cut against baseline but 23.9% against taper week 1, in session RPE load.
- Volume unit: 41.5% in minutes against 43.1% in session RPE load.

**Units and typical range.** Percent. A positive value is a cut. Bosquet et al. (2007), abstract: 2-week taper, effect size 0.59 ± 0.33; volume cut by 41% to 60%, 0.72 ± 0.36; intensity kept, 0.33 ± 0.14; frequency kept, 0.35 ± 0.17. Winwood et al. (2023), abstract: weightlifters reported a taper of 8.0 ± 4.4 days and a 43.1 ± 14.6% volume cut. Both are study findings, not targets.

**Vendor equivalents.** None.

**Reference file.** [taper-and-distribution.md](../skills/load-and-wellness/references/taper-and-distribution.md)

### Intensity distribution

**What it measures.** Intensity distribution is the share of a week's or a block's training in three zones: Z1 (low), Z2 (moderate), and Z3 (high), with a label for the pattern. Sperlich et al. (2023) describe the three-zone model as the one most used in research, state that no standard criteria separate the zones, and state that the distribution obtained depends heavily on the method. Their review covered elite endurance athletes. A label describes a week. It does not rank one distribution above another.

**Inputs.** The calculation needs these data:

- One of three inputs: heart rate minutes in each zone, session CR-10 ratings with minutes, or a session goal (low, moderate, or high) from the plan
- The grouping into three zones, chosen by the user. Lucia's three phases (below VT, VT to RCP, above RCP) already form three zones. For Edwards %HRmax zones, the file offers below 80% HRmax as Z1, 80% to 90% as Z2, and 90% and above as Z3, labeled as its own choice. For CR-10, it offers 0 to 4, 5 and 6, and 7 to 10, labeled as its own choice.
- The counting unit, minutes or sessions, and the window. The file offers Monday-to-Sunday weeks, labeled as its own choice.

**Calculation.** Use these formulas, with the shares as fractions from 0 to 1:

```text
Z1_share = Z1_time ÷ (Z1_time + Z2_time + Z3_time)     (the same for Z2 and Z3)
PI = log10(Z1_share ÷ Z2_share × Z3_share × 100)
```

The polarization index (PI) comes from Treff et al. (2019). If Z3 is 0, PI is 0. If Z3 is larger than Z1, every tool returns the text "not valid". If Z2 is 0 and Z3 is above 0, every tool returns the text "not defined", because Treff et al. print the formula for that case without clear brackets. Such a week is labeled other, not polarized. An incomplete week gives a blank, kept apart from both texts. In Power BI and Tableau, the text sits in a separate `PI status` measure, because one measure cannot mix numbers and text.

Label the pattern as Sperlich et al. (2023) did:

- No Z3: Z1 > Z2 and Z3 = 0. Sperlich et al. used it for two-zone models. The file checks it first, so a week with all time in Z1 is no Z3. That order is the file's choice.
- Pyramidal: Z1 > Z2 > Z3.
- Polarized: Z1 > Z3 > Z2 and PI above 2.00.
- Threshold: Z2 > Z1 > Z3, as in the methods. The abstract writes it as Z2 > Z1 = Z3.
- Z2 and Z3 even: Z2 = Z3, with both above 0.
- Other: any other pattern.

Follow these steps from raw inputs:

1. Ask for the input, the grouping, the counting unit, and the window.
2. Add each athlete's minutes, or sessions, in Z1, Z2, and Z3, from complete sessions only.
3. Calculate the shares and PI.
4. Apply the labels, and report them with the zone totals, the shares, the input, the grouping, the counting unit, and the window.

**Worked example.** One week of six sessions, 325 minutes in all:

| Input | Z1 | Z2 | Z3 | PI | Label |
|---|---|---|---|---|---|
| Heart rate minutes, Edwards zones grouped below 80% / 80% to 90% / 90% and above | 265 min (81.5%) | 40 min (12.3%) | 20 min (6.2%) | 1.61 | Pyramidal |
| CR-10 minutes, bands 0-4 / 5-6 / 7-10 | 210 min (64.6%) | 30 min (9.2%) | 85 min (26.2%) | 2.26 | Polarized |
| CR-10 session counts, same bands | 3 | 1 | 2 | 2.00 | Other |

The heart rate PI is log10(0.8154 ÷ 0.1231 × 0.0615 × 100) = 1.61. The session-count PI is exactly 2.00, which is not above 2.00, so that row is other, not polarized. One week gives three labels.

**Variants.** These variants are in use. Name the one you use with every value:

- Input: heart rate time in zone, session RPE, or session goal (Sperlich et al., 2023, list these among others).
- Counting unit: minutes or sessions.
- Grouping of the source zones into three.

**What changes the number.** These choices change the result when the training does not change:

- Input and counting unit: pyramidal, polarized, and other for the same week in the worked example.
- Zone grouping: moving Edwards zone 3 (70% to 80%) into Z2 changes the shares to 60.0%, 33.8%, and 6.2%, and PI from 1.61 to 1.04.
- Time below 50% HRmax: leaving it out of Z1 changes the shares to 78.9%, 14.0%, and 7.0%.
- Session goal: a plan of 4 low and 2 high sessions gives Z2 = 0, so PI is not defined and the label is other. A plan of 4 low, 1 moderate, and 1 high gives Z2 = Z3, labeled Z2 and Z3 even.
- Percentages instead of fractions in PI: Treff et al. (2019) give 80%, 5%, and 15% as a polarized example. As fractions, PI is 2.38. With percentages, it becomes 4.38.

**Units and typical range.** Shares in fractions or percent, PI with no unit, and a text label. Of 175 distributions from elite endurance athletes, 89 were pyramidal, 65 polarized, and 8 threshold, and the rest other patterns. In 91%, more than 60% of endurance training was low intensity (Sperlich et al., 2023).

**Vendor equivalents.** The Polar Team Pro file maps `Time in HR zone`, time in five heart rate zones. The Firstbeat Sports file maps zone times, and the API numbers its zones from the top, so `zone1Time` is the highest zone. The STATSports file maps time in heart rate zones 1 to 6, set as percentages of each player's maximum heart rate. Group the zones into three with the user's rule.

**Reference file.** [taper-and-distribution.md](../skills/load-and-wellness/references/taper-and-distribution.md)

### Recovery questionnaire scores

**What it measures.** A recovery questionnaire score turns athletes' answers about recovery, fatigue, or mood into a number. The file scores four named questionnaires: the Hooper index (Hooper and Mackinnon, 1995), Total Quality Recovery (Kenttä and Hassmén, 1998), Perceived Recovery Status (Laurent et al., 2011), and the Brief Assessment of Mood (Shearer et al., 2015). 68% of 41 high-level football clubs (Akenhead and Nassis, 2016) and 84% of respondents (55% of 100 invited) in a high performance survey (Taylor et al., 2012) reported using questionnaires. Neither abstract says which named questionnaires. The file could not read any of the four original papers in full, so it takes ranges and directions from later studies that cite them. It does not copy any full form, because no license statement for the item wording was found. It leaves out the RESTQ-Sport, which is documented in a commercial user manual (Kellmann and Kallus, 2025). A score is the athlete's report. It does not identify illness, injury, or a training problem.

**Inputs.** The calculation needs these data:

- One row per athlete per day, with one column per item
- The questionnaire, its version, each item's range, and which end is good, confirmed from the user's form
- For the BAM, whether the points are numbered 0 to 4 or 1 to 5

**Calculation.** Use these formulas:

```text
hooper_index    = sleep + stress + fatigue + soreness          (each 1 to 7)
tqr             = single rating, 6 to 20
prs             = single rating, 0 to 10
bam_tmd         = anxiety + depression + anger + fatigue + confusion + vigour_inverted
vigour_inverted = (lowest point + highest point) − vigour
```

The terms mean the following:

- Hooper index: stress, fatigue, and soreness run from 1, very, very low, to 7, very, very high. Sleep runs from 1, very, very good, to 7, very, very bad (Douchet et al., 2024; Juillard et al., 2024). Higher is worse. Some studies print sleep the other way and still add it (Perazzetti et al., 2025), and one study's text and table disagree (Silva et al., 2022). Flip a sleep item that runs from bad to good with `8 − sleep`.
- TQR: 6 is very, very poor recovery and 20 is very, very good recovery (Selmi et al., 2025; Dutra et al., 2026). Higher is better. A 0 to 10 version is also in use (Pino-Mulero et al., 2025).
- PRS: 0 is very poorly recovered and extremely tired, and 10 is very well recovered and highly energetic (Delp et al., 2023; de Sousa Neto et al., 2022). Higher is better. Some forms allow half points (Bauer et al., 2024).
- BAM: six items on a 5-point intensity scale. The total mood disturbance score adds the six items after inverting vigour (Lipinski et al., 2025). Higher is worse. The file could not confirm the numbering of the points, or the formula of the energy index reported by Shearer et al. (2015).

Follow these steps from raw answers:

1. Confirm the questionnaire, version, ranges, and good end of each item from the user's form.
2. Mark any blank, text, or out-of-range answer as missing.
3. Flip any Hooper item that runs from bad to good.
4. Calculate the score. Leave it missing if any item is missing.
5. Trend each athlete's score with the wellness z-score method, and state which sign means worse than usual.

**Worked example.** One athlete on 2026-09-15:

| Questionnaire | Answers | Score |
|---|---|---|
| Hooper index | Sleep 3, stress 2, fatigue 4, soreness 5 | 14 of 4 to 28 (higher is worse) |
| TQR | 12 | 12 of 6 to 20 (higher is better) |
| PRS | 6 | 6 of 0 to 10 (higher is better) |
| BAM, 0 to 4 form | Anxiety 1, depression 0, anger 0, fatigue 3, confusion 1, vigour 1 | 1 + 0 + 0 + 3 + 1 + (0 + 4 − 1) = 8 of 0 to 24 (higher is worse) |

Against 14 previous Hooper scores with mean 10.43 and SD 0.94, today's 14 is 3.57 points higher, z = (14 − 10.4286) ÷ 0.9376 = 3.81, or 3.81 SDs worse than usual.

**Variants.** These variants are in use. Name the one you use with every value:

- Hooper sleep item printed good to bad, or bad to good.
- TQR on 6 to 20, or on 0 to 10.
- PRS in whole or half points.
- BAM numbered 0 to 4 or 1 to 5. BAM+ is a different version. Apweiler et al. (2018) list 10 items on 100 mm visual analog scales, with sleep and confidence among them.

**What changes the number.** These choices change the result when the athlete feels the same:

- Hooper sleep direction: a reversed sleep item added without the flip turns 14 into 16.
- BAM numbering: the same answers give 8 on a 0 to 4 form and 14 on a 1 to 5 form.
- BAM vigour not inverted: 6 instead of 8.
- Blank items added as 0: a lower, better-looking Hooper index or BAM total.

**Units and typical range.** Points with no physical unit. Hooper index 4 to 28. TQR 6 to 20, or 0 to 10 for the short version. PRS 0 to 10. BAM total 0 to 24 or 6 to 30 by the form's numbering. No population norm or flag cut-off from these sources applies across sports.

**Vendor equivalents.** None.

**Reference file.** [recovery-questionnaires.md](../skills/load-and-wellness/references/recovery-questionnaires.md)

### Estimated load

**What it measures.** An estimated load is a stand-in value for an athlete who played but did not wear the device, built from their playing time and their own load in games they did wear it. It is not a measurement. No published study validates a model that predicts one athlete's game load from playing time alone, so every method here is unvalidated until it is checked on the user's own data.

**Inputs.** The calculation needs these data:

- One row per athlete per game with `athlete_id`, `game_id`, `load`, and `load_source` (`measured` or `estimated`)
- Playing time for every game from an official source, such as time on ice (TOI) from the league's game report, converted from `mm:ss` to decimal minutes

**Calculation.** Use the athlete's own load per playing minute:

```text
rate_athlete       = Σ load_measured ÷ Σ playing_min_measured
estimated_load     = rate_athlete × playing_min_today
held_out_error_pct = |estimate_without_game − load_measured| ÷ load_measured × 100
```

The terms mean the following:

- `load_measured`: the device's load in a game the athlete wore it, such as TRIMP or PlayerLoad, in AU
- `playing_min_measured`, `playing_min_today`: playing time in minutes, such as TOI. Use the same kind of minutes in the rate and in the estimate.
- `rate_athlete`: a ratio of totals in AU per playing minute, not the mean of each game's ratio
- `estimate_without_game`: the estimate for one measured game from the athlete's other measured games, a leave-one-game-out check

Follow these steps from raw inputs:

1. Ask whether the user has their own estimation formula. If so, convert playing time as in step 2, apply the formula as given, and go to step 6.
2. Convert every playing time to decimal minutes.
3. Keep measured games of the same type and season that the user chooses.
4. Divide the sum of measured load by the sum of measured playing minutes.
5. Multiply by today's playing minutes.
6. Leave out each measured game in turn, estimate it from the rest, and report the mean and largest error in percent. This needs at least 2 measured games.
7. Say whether today's playing time falls inside the measured range.
8. Store the result with `load_source` set to `estimated` and the method name.

**Worked example.** One forward wore a heart rate monitor in six games, with 529 AU of TRIMP over 101.33 minutes of TOI. The rate is 529 ÷ 101.33 = 5.220 AU per TOI minute. In game 7 the athlete played 18:30, or 18.50 minutes, so the estimate is 5.220 × 18.50 = 96.6 AU, reported as 97 AU. The leave-one-game-out errors were 5.6%, 5.7%, 3.3%, 8.7%, 10.1%, and 3.8%: a mean of 6.2% and a largest of 10.1%. Dividing by the 150-minute game recording instead of TOI gives 0.588 AU per minute and an estimate of 10.9 AU, about one ninth of the right value.

**Variants.** Use these when the athlete rate does not fit:

- The user's own formula: apply it as given, and still run the held-out check.
- Athlete line: `load = a + b × playing_min`, fitted by least squares. The file's choice is at least 10 measured games.
- Position rate: `Σ load ÷ Σ playing_min` across wearers in the same position, labeled as a group estimate. Individual models predicted session RPE from GPS data with less error than a group model in Australian football (Bartlett et al., 2017).
- Research imputation methods: multiple imputation with predictive mean matching was best in most simulated scenarios (Bache-Mathiesen et al., 2022). The daily team mean was the best method in one study (Griffin et al., 2021) and the worst in another (Epp-Stobbe et al., 2022). These studies filled random gaps, not whole games for a player who never wore a device.

**What changes the number.** These choices change the estimate when the athlete's game does not:

- Playing time: in elite ice hockey, players with more TOI had lower intensity per minute (r = −0.63 to −0.18) (Rago et al., 2022), so a constant rate can overestimate long games.
- Position: defensemen had lower load per minute than forwards (Allard et al., 2022). Do not share a rate across positions.
- Denominator: a rate per recording minute multiplied by playing minutes underestimates the load, as the worked example shows.
- Game type: a rate built on training sessions does not fit games.

**Units and typical range.** An estimate has the unit of the load it replaces and no range of its own. Game TRIMP in men's varsity hockey was 98 ± 59 AU (Bigg et al., 2022). TRIMP test-retest typical error in collegiate hockey practices was 12.2% (Ulmer et al., 2019). PlayerLoad test-retest CV ranged from 2.2% to 26.6% across hockey tasks (Van Iterson et al., 2017). The estimate's error adds to this measurement error.

**Vendor equivalents.** None. Firstbeat `TRIMP/min` divides by session duration, not playing time, so it is not a rate per playing minute.

**Reference file.** [estimated-load.md](../skills/load-and-wellness/references/estimated-load.md)

## Running load

These metrics come from GPS (global positioning system) units, local positioning systems, or video tracking. Speed is in km/h or m/s. Sampling rate is in Hz, samples per second.

Running thresholds and ranges do not apply to skating. For ice hockey tracking, wearable, and time-on-ice data, see [ice-hockey.md](../skills/gps-running-load/references/ice-hockey.md).

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
| Peak demands | `max of Σ x[j]` over every valid rolling window of `n = window_s × hz` samples | m, or a count | [peak-demands.md](../skills/gps-running-load/references/peak-demands.md) |
| Peak per minute | `peak ÷ (window_s ÷ 60)` | m/min, or count per min | [peak-demands.md](../skills/gps-running-load/references/peak-demands.md) |
| Drill as a percent of match peak | `drill_per_min ÷ match_peak_per_min × 100` | % | [peak-demands.md](../skills/gps-running-load/references/peak-demands.md) |
| Match-day label | `MD+days_since_last` if within the post-match days, else `MD-days_to_next` | Label | [match-day-load.md](../skills/gps-running-load/references/match-day-load.md) |
| Percent of match | `session_value ÷ match_reference × 100` | % | [match-day-load.md](../skills/gps-running-load/references/match-day-load.md) |
| Speed zone edge from test results | `q × mas_m_s` | m/s | [high-speed-running.md](../skills/gps-running-load/references/high-speed-running.md) |
| Top-speed exposure | Runs of samples at or above `pct ÷ 100 × mss_m_s` that last at least `min_duration_s`, and the distance at or above it | Count, m | [high-speed-running.md](../skills/gps-running-load/references/high-speed-running.md) |

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
- Unit to unit: two units of the same model disagree on the same movement (Johnston et al., 2014). Give each athlete the same unit every session.
- Software version and filter settings: processing choices change the output (Malone et al., 2017). Manufacturer software and raw processing also gave substantially different values (Thornton et al., 2019). The abstract does not report software versions or filter settings. Record the software version and the processing date.
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
- STATSports Total Distance: distance in m, km, miles, or yards. The filtering is not published. STATSports Distance Per Minute is the average distance in m covered each minute, and it depends on how drill edges are drawn.

**Reference file.** [total-distance.md](../skills/gps-running-load/references/total-distance.md)

### High-speed running distance

**What it measures.** High-speed running distance is the distance an athlete covers while moving faster than a chosen speed threshold. The number depends on the threshold as much as on the athlete. Treat the threshold as part of the metric's name. No standard threshold exists across sports. Speed zone definitions vary widely within and between sports (Cummins et al., 2013). The file also covers speed zones built from test results, and top-speed exposure: efforts and distance at or above a percent of each athlete's maximal sprint speed. Top-speed exposure describes the running done. It does not predict any outcome.

**Inputs.** The calculation needs these data:

- Raw speed samples, or a summary export with distance in speed zones
- The sampling rate, checked against the timestamps
- The threshold value, unit, type (absolute or individualized), and the date it was set. For individualized thresholds, the test that set them.
- The vendor's boundary rule, and the minimum effort duration if you count efforts
- For zones from test results: each athlete's maximal aerobic speed (MAS), the test, and its date
- For top-speed exposure: each athlete's maximal sprint speed (MSS), its source (sprint test or GPS), its date, the percents, and the week definition

**Calculation.** Add the distance of every sample at or above the threshold. For a band with an upper limit, count samples at or above the lower bound and below the upper bound:

```text
hsr_distance_m     = Σ (speed_m_s × dt_s)   for samples where speed_m_s ≥ threshold_m_s
band_distance_m    = Σ (speed_m_s × dt_s)   for samples where lower_m_s ≤ speed_m_s < upper_m_s
threshold_m_s      = threshold_km_h ÷ 3.6, or threshold_mph × 0.44704
edge_m_s           = f × mas_m_s
top_threshold_m_s  = pct ÷ 100 × mss_m_s
```

The terms mean the following:

- `speed_m_s`: speed in one sample, in m/s
- `dt_s`: the time between samples. At 10 Hz, it is 0.1 s.
- `threshold_m_s`: the speed threshold in m/s
- `lower_m_s`, `upper_m_s`: the bounds of a speed band, in m/s
- `hsr_distance_m`: the distance covered at or above the threshold, in metres
- `mas_m_s`: maximal aerobic speed in m/s. `f`: the fraction of MAS, such as 0.80. `mss_m_s`: maximal sprint speed in m/s.
- `pct`: the percent of MSS for top-speed exposure, such as 85, 90, or 95
- Effort: one continuous stretch at or above the threshold that lasts at least a minimum time, the minimum effort duration or dwell time. The file measures a run's length as samples × `dt_s`.

Follow these steps from raw inputs:

1. Convert speed to m/s, and convert the threshold to m/s.
2. For individualized thresholds, join each athlete's own threshold to their rows by athlete ID. For zones from test results, calculate each edge as f × MAS first.
3. Set `dt_s = 1 ÷ Hz`, and check it against the timestamps.
4. Mark each sample at or above the threshold, and below the upper bound for a band, unless the vendor's rule differs. Round speed and threshold to the same number of decimals first.
5. Multiply each marked sample's speed by `dt_s`, and add the marked distances for each athlete and session.
6. For effort counts, group consecutive marked samples into runs. Count a run as an effort only if it lasts at least the minimum effort duration.
7. For weekly top-speed exposure, add each session's efforts and distance by athlete and week.
8. Label each result with the threshold, its unit, the threshold type, the boundary rule, and the minimum effort duration. For top-speed exposure, add the percent and the MSS value, source, and date.

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

The same 30 samples with zones from test results give these band distances:

| Athlete | MAS | 80% MAS edge | 80% to 100% MAS | At or above MAS |
|---|---|---|---|---|
| A | 4.5 m/s | 0.80 × 4.5 = 3.600 m/s | 2.78 m | 11.22 m |
| B | 4.0 m/s | 0.80 × 4.0 = 3.200 m/s | 2.19 m | 12.48 m |

For top-speed exposure, 40 samples at 10 Hz with two sprints, a top speed of 8.60 m/s, and a 0.6 s minimum give these results:

| Percent of MSS | MSS 9.20 m/s from a sprint test | MSS 8.90 m/s from GPS |
|---|---|---|
| 80% | 2 efforts, 17.005 m | 2 efforts, 19.175 m |
| 85% | 1 effort, 13.195 m | 2 efforts, 16.265 m |
| 90% | 1 effort, 6.780 m | 1 effort, 10.820 m |
| 95% | 0 efforts, 0.000 m | 0 efforts, 3.430 m |

At 90% of the sprint test MSS, the threshold is 8.28 m/s, samples 6 to 13 reach it for 0.8 s, and their distance is 6.78 m. Six sessions with 0, 3, 2, 0, 1, and 4 efforts give a weekly count of 10.

**Variants.** These threshold variants are in use:

- Absolute threshold: one speed for every athlete. Published examples are 19.8 km/h (5.5 m/s), the default of one camera-based system (Abt & Lovell, 2009); 14.4 km/h (4.0 m/s) in youth soccer (Buchheit et al., 2014b); 14.0 to 19.99 km/h for high-speed running and above 20.0 km/h for very high-speed running (Johnston et al., 2014); and 4.17 m/s (15.0 km/h) for high-speed running and 7.00 m/s (25.2 km/h) for sprinting (Varley et al., 2017).
- Individualized threshold: a speed set per athlete. Abt and Lovell (2009) used each player's running speed at the second ventilatory threshold. Reardon et al. (2015) used 60% of each player's maximum speed from a season of training and match data.
- Zones from test results: edges built as a fraction of MAS. Rago et al. (2019) used 80% to 99.9% of MAS for moderate-speed running, with high-speed running starting at 100% of MAS. The sources do not write out how edges above MAS are built from the anaerobic speed reserve, so the file gives no such edge. These are study settings.
- Top-speed exposure: thresholds at a percent of each athlete's MSS. Dillon et al. (2024) counted weekly exposures at or above 80%, 85%, 90%, and 95%. Shah et al. (2022) counted weekly efforts above 90% and 95% with a 0.6 s minimum duration, cited for the method only.

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
- Test results for zones: a lower MAS puts 3 more samples above MAS in the worked example.
- MSS source for top-speed exposure: at 85%, the sprint test MSS gives 1 effort and the GPS MSS gives 2 in the worked example. Weekly counts differed most at 80% and 85% and least at 90% and 95% (Dillon et al., 2024).
- A new MSS lowers every later count at the same percent.

**Units and typical range.** High-speed running distance is in metres. Report a range only with its threshold. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Professional soccer, match, camera tracking, threshold 19.8 km/h | 845 ± 296 m (mean ± SD) | Abt & Lovell, 2009 |
| Same players, individualized threshold (median 15 km/h, range 14 to 16 km/h) | 2,258 ± 707 m | Abt & Lovell, 2009 |
| Elite rugby union, match, 10 Hz GPS, 60% of maximum speed | Forwards 354.72 ± 99.22 m. Backs 570.02 ± 171.14 m. | Reardon et al., 2015 |
| English Premier League, camera tracking, match-to-match variation | CV 16.2% for high-speed running, 30.8% for sprint distance | Gregson et al., 2010 |
| Measurement error, high-speed distance, any tracking technology | Above 40% deviation from a reference system | Linke et al., 2018 |
| Measurement error, 10 Hz and 15 Hz units, as speed rises | Typical error 0.8% to 19.9% | Johnston et al., 2014 |
| Italian Serie B soccer, 13 players, test results used for zones | MAS 17.7 ± 0.6 km/h. MSS 31.1 ± 0.9 km/h, the highest GPS speed. | Rago et al., 2019 |
| Professional Australian football, 47 players, MSS from in-season GPS against a pre-season sprint test | Weekly counts lower by 1.26 at 80%, 0.78 at 85%, 0.42 at 90%, and 0.09 at 95% | Dillon et al., 2024 |
| Elite youth soccer, 12 players, 40 m sprints, 10 Hz GPS against a 100 Hz laser | 8.75 ± 0.32 m/s against 8.79 ± 0.33 m/s, mean difference 0.04 m/s | Kyprianou et al., 2019 |

The error rows compare units or systems. They are not the test-retest error of one athlete on one unit.

**Vendor equivalents.** The device files map these metrics:

- Catapult HS Distance: distance in velocity bands 5 and 6, by default above 5.5 m/s. Catapult Sprint Distance: distance in band 6, by default above 7 m/s. The default bands are band 1 0 to 0.2 m/s, band 2 0.2 to 2, band 3 2 to 4, band 4 4 to 5.5, band 5 5.5 to 7, and band 6 above 7. Those are Vector Core defaults. OpenField allows up to eight bands, and the public OpenField Bands page publishes no defaults. Bands can be absolute speeds or a percentage of each athlete's maximum, and they change by account and season. New bands apply only to future sessions unless someone reprocesses old sessions. Catapult does not publish its boundary rule. Catapult `max_vel` is the highest speed in the selected time.
- Kinexon Max. Speed: in km/h and mph. Kinexon publishes no formula. LPS and GPS Pro measure position. An IMU can only estimate speed, and how an IMU reports Max. Speed is not published. Smoothing is not published, and no source supports a cross-vendor comparison of the number. The column names for speed zones are not confirmed. Published studies that used Kinexon set high-speed running at 4.4 m/s or more in a handball study (Carton-Llorente et al., 2023). A handball LPS study names 5.5 to 7 m/s high-intensity running (Bassek et al., 2023). One study set sprints at 18.72 km/h (5.2 m/s) with a 1.0 s minimum. These are study settings, not Kinexon defaults.
- Polar `speed_zones_kmh` and Distance in speed zone: distance in five speed bands set in the sport profile, in m with limits in km/h. The defaults are not published, and the limits change when a coach edits them. Polar `speed_max_kmh` is top speed. The default Polar sprint rule is an acceleration test, not a speed test.
- STATSports High Speed Running (HSR): distance in speed zones 5 and 6, by default above 5.5 m/s, reported as HSR (Absolute) and HSR (Relative). STATSports has six speed zones, and the distance in each is a separate field, such as `Zone 4 Distance`. Max Speed is the highest speed in the session or drill, and its smoothing is not published. STATSports Sprints count a run above an entry speed, by default 19.8 km/h, held for a minimum time, by default 1 s. That is not the same as zone 6 distance.

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
- Manufacturer and processing: manufacturers differed substantially, particularly for threshold-based acceleration and deceleration variables (Thornton et al., 2019).
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
| Between-unit variation, 27 units, three 10 Hz brands, on a sled, range across movement variables | Coefficient of variation 0.2% to 78.2% | Thornton et al., 2019 |

A between-unit figure applies only when the athlete changed to another unit of the same model. No figure in the reference files can serve as one athlete's noise when the athlete changes device type or vendor. For an athlete on one unit, use a typical error from a short-term retest on that unit and the shared noise band rules.

**Vendor equivalents.** The device files map these metrics:

- Catapult Acceleration Efforts and Deceleration Efforts: a default threshold above 2 m/s². In the `Gen2Acceleration` band set, bands 1 to 3 are decelerations and bands 6 to 8 are accelerations. Bands 4 and 5, near zero, cannot be reported. The Gen2 effort rules exclude movements shorter than 0.9 s, from a public Catapult page. The fuller Gen2 rules need a Catapult sign-in.
- Catapult Acceleration load: the sum of absolute acceleration values from smoothed 10 Hz speed. It is a different quantity from PlayerLoad and from effort counts. The Catapult file maps it to no reference file.
- Kinexon Mechanical Load: accelerations and decelerations grouped by intensity, multiplied by proprietary weights, and summed. Mechanical Load is Accel Load plus Decel Load. The weights and bands are not published. Mechanical Intensity is Mechanical Load divided by time. The Kinexon file maps both to no reference file, and no source supports a Catapult equivalent. Published studies that used Kinexon set accelerations at 1.5 m/s² with a 0.5 s minimum in one study, and 2 m/s² in another.
- Polar `sprint_counter` and Sprints: each acceleration above 2.8 m/s² counts once, whatever its length. The coach can switch to a speed threshold in km/h.
- Polar `acceleration_zones_ms2` and Number of accelerations: counts in four acceleration and four deceleration bands. The default thresholds, the effort definition, and the minimum duration are not published.
- STATSports Accelerations and Decelerations: counts by zone, such as `Zone 5 Accelerations`. A 2020 STATSports article states at least 2.0 m/s² for at least 0.5 s for zones 3 to 6. The bounds of zones 4 and 6 are not confirmed, so count only the zones the user names. Maximum Acceleration and Maximum Deceleration are the largest values in the session. Relative zones are a percentage of a stored maximum, so record the maximum used.

**Reference file.** [accelerations-decelerations.md](../skills/gps-running-load/references/accelerations-decelerations.md)

### Peak demands

**What it measures.** Peak demands are the highest amount of a measure an athlete produced in any window of a set length, such as 1, 3, 5, or 10 minutes. Studies also call them the most demanding passages or worst-case scenarios. The file covers distance, high-speed running distance, and acceleration efforts, a drill as a percent of each player's match peak, and position comparisons. The coach decides what to do with any percent.

**Inputs.** The calculation needs these data:

- Raw speed samples with `time_s`. A summary export with session totals cannot give peaks.
- The sampling rate, checked against the timestamps
- Period boundaries: halves, quarters, drills, and substitutions
- The window lengths and window type, the high-speed threshold, and the acceleration threshold, minimum duration, and boundary rule
- For drills, each player's match reference rule and the drill duration

**Calculation.** Sum the measure over every rolling window that lies inside one period and holds no dropped sample, and keep the highest:

```text
n                  = window_s × hz
window_sum[i]      = Σ x[j] for j = i − n + 1 to i
peak               = max of window_sum over every valid window
peak_per_min       = peak ÷ (window_s ÷ 60)
drill_pct_of_peak  = drill_per_min ÷ match_peak_per_min × 100
```

The terms mean the following:

- `x[i]`: the measure in one sample. Distance is `speed_m_s ÷ hz`. High-speed running is `speed_m_s ÷ hz` at or above the threshold, else 0. Acceleration efforts are 1 on the first sample of each counted effort, else 0.
- `window_s`: the window length in seconds
- `n`: samples per window. A 60 s window at 10 Hz is 600 samples.
- `peak`: the highest window sum in the period, in m or a count
- `drill_per_min`: the drill total divided by the drill duration in minutes
- `match_peak_per_min`: the player's match peak per minute for the same measure, window length, and window type

A valid window lies inside one period, holds every sample, and spans `(n − 1) ÷ hz` seconds. The file counts an acceleration effort in the window that holds its first sample. That is the file's choice.

Follow these steps from raw inputs:

1. Convert speed to m/s, and check the sampling rate against the timestamps.
2. Split each session into periods.
3. Make the measure per sample.
4. Flag dropped samples and time gaps.
5. Sum the measure over every valid rolling window, using a running total so each window is one subtraction.
6. Keep the highest window in each period, then the highest period as the session peak.
7. Divide by the window length in minutes.
8. Label each result with the measure, window length, window type, threshold, and sampling rate.

**Worked example.** Twelve minutes of one player's match data, summed into 30 s blocks so it can be followed by hand. The windows step by one block. Real data step by one sample.

| Blocks | Distance, m |
|---|---|
| 1 to 12 | 48, 52, 55, 60, 58, 96, 104, 90, 50, 49, 51, 47 |
| 13 to 24 | 50, 53, 49, 52, 58, 62, 92, 98, 57, 50, 46, 50 |

The calculation gives these results:

- Average: 1,477 m over 12 minutes is 123.1 m/min.
- Rolling 1 minute peak: the running totals at blocks 5 and 7 are 273 and 473 m, so blocks 6 and 7 hold 200 m, or 200.0 m/min. The highest fixed 1 minute window is blocks 7 and 8: 194.0 m/min, 3.0% lower.
- Rolling distance peaks: 154.3 m/min over 3 minutes, 133.0 m/min over 5 minutes, and 128.3 m/min over 10 minutes.
- The fixed 3 minute high-speed peak is 41.2% below the rolling one, because the intense passage crosses a fixed boundary.
- A 4 minute drill of 560 m is 140.0 m/min. Against this match, it is 90.7% of the 3 minute peak, 99.1% of the 4 minute peak, and 105.3% of the 5 minute peak.
- Four players in a 3 minute drill: the wide players' median is 79.3% of their own match peak and the central players' median is 93.9%. Against one squad mean of 156.0 m/min, the group medians move closer: 83.3% and 89.1%.

**Variants.** These choices give different results:

- Rolling windows start at every sample. Fixed windows start at set times. Never compare the two. The rule in total-distance.md extends to every measure here.
- Drill average against the match peak of the same length, or the drill's own peak window against the match peak of the same window. Baptista et al. (2020) used the second, with 5 minute peaks.
- Match reference: the mean of the player's match peaks, or the highest one. Baptista et al. (2020) used the mean of 15 matches as 100%, from matches with at least 60 minutes in one position.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Rolling or fixed: in soccer, fixed windows underestimated rolling values by about 7% to 10% for total distance and about 12% to 25% for distance above 5.5 m/s (Fereday et al., 2020). Moving averages identified higher peaks than other methods (Whitehead et al., 2018).
- Window length: 200.0 m/min over 1 minute against 128.3 m/min over 10 minutes in the worked example.
- Window step: stepping by sample gives a peak at least as high as stepping by 1 s or 30 s.
- Window for the drill comparison: 90.7%, 99.1%, or 105.3% for the same drill.
- Match reference rule and minimum minutes.
- Periods: a window that crosses half time or a substitution mixes playing and resting time.
- Where an effort counts in a window.
- Thresholds, sampling rate, device type, unit, and software, as for total distance, high-speed running, and accelerations.
- Matches against training: in basketball, most 1 minute peaks were higher in official matches than in training, in the one study that compared them (Pérez-Chao et al., 2023).

**Units and typical range.** Peaks are in m, or a count. Rates are per minute. Compare each athlete with their own match peaks on the same device and settings. The file gives these values:

| Population | Value | Source |
|---|---|---|
| Professional soccer, rolling windows, 10 Hz | 190.1 ± 20.4 m/min over 60 s; 120.9 ± 13.1 m/min over 600 s | Fereday et al., 2020 |
| Football codes, method use | Moving averages in 63% of 27 studies | Whitehead et al., 2018 |
| Elite soccer, local positioning, training week 5 minute peaks as a percent of the match mean | Accelerations 102% to 124%. Decelerations 88% to 115%. Sprint distance 64% for wing-backs, 107% for centre-backs, 100% for centre midfielders, and 107% for centre forwards. | Baptista et al., 2020 |
| Basketball, windows in use | 15 s to 10 minutes. 30 s, 1, 2, and 5 minutes named the most practical. | Pérez-Chao et al., 2023 |

These are study findings from single teams, not targets.

**Vendor equivalents.** One device file maps this metric:

- STATSports Max Intensity Period (MIP): the highest moving average of a chosen metric over a window the user sets, with a default of 3 minutes. The type of moving average and the step are not published.

Ask how any other vendor's peak value is calculated before you use it: window type, step, and length.

**Reference file.** [peak-demands.md](../skills/gps-running-load/references/peak-demands.md)

### Match-day load

**What it measures.** Match-day load labels each training session by its days to or from a match, and expresses the session's load as a percent of the player's own match value for the same measure. It describes the training week. It does not say what the week should be.

**Inputs.** The calculation needs these data:

- The fixture list, with every match date the user counts
- Minutes played and position for every player and match, from the official match report
- One value per player per session for each measure, from the same device and settings in training and matches
- The number of post-match days the coach labels as MD+, the match reference rule, and a minimum reference below which no percent is shown

**Calculation.** Label each session, then divide by the player's match reference:

```text
days_to_next     = next_match_date − session_date
days_since_last  = session_date − last_match_date
label            = "MD" on a match date
                 = "MD+" & days_since_last   if days_since_last ≤ post_match_days
                 = "MD-" & days_to_next      otherwise
pct_of_match     = session_value ÷ match_reference × 100
week_pct         = Σ session values in the microcycle ÷ match_reference × 100
```

The terms mean the following:

- `post_match_days`: how many days after a match are labeled MD+, set by the coach
- `match_reference`: the mean of the player's qualifying match values for the measure
- Microcycle: the training days between two matches

Follow these steps from raw inputs:

1. Calculate `days_to_next` and `days_since_last` for every session, and store both.
2. Label each session with the coach's post-match rule.
3. Record the days between matches for each microcycle.
4. Choose the match reference rule: full matches, a minimum number of minutes, extrapolation to 90 minutes, or a position reference. A position reference is the mean of the match references of every qualifying player in the position, including this player when they qualify.
5. Calculate each player's reference, and count the matches in it.
6. Divide each session value by the reference, and multiply by 100. Give no percent when the reference is below the user's minimum.
7. Label each result with the measure, the reference rule, the number of matches, and the microcycle length.

**Worked example.** Matches on 2026-09-05, 2026-09-12, 2026-09-16, and 2026-09-19, with 1 post-match day:

- Labels for the 6-day week: MD+1, MD-5, MD-4, MD-3, MD-2, MD-1. The congested week after 2026-09-12 has MD+1, MD-2, MD-1, MD, MD+1, MD-1, with no MD-3 or MD-4.
- Player A's three full matches give a total distance reference of 10,450 m. MD-3 at 5,900 m is 5,900 ÷ 10,450 × 100 = 56.5%. MD-4 at 6,100 m is 58.4%. The five training sessions total 22,500 m, or 215.3%.
- Player B ran 5,900 m on MD-3. Against matches of at least 60 minutes (9,950 m), that is 59.3%. Against a 30 minute appearance of 3,900 m extrapolated to 90 minutes (11,700 m), it is 50.4%. Against a position reference, the mean of Player A's and Player B's references ((10,450 + 9,950) ÷ 2 = 10,200 m), it is 57.8%.
- A goalkeeper's high-speed reference is 14 m. Sessions of 9 m and 19 m read 64.3% and 135.7%. Show these values raw.

**Variants.** The studies calculated the percent in two ways:

- Group ratio: mean training session value × 100 ÷ mean match value, for the squad or a position (Martín-García et al., 2018).
- Player reference: the average of each variable across tracked matches set as 100% (Baptista et al., 2020).

The file uses a reference per player. A group ratio and the mean of player percents are different numbers.

**What changes the number.** These choices change the result when the athlete's training does not change:

- Match reference rule: 50.4% to 59.3% for Player B's same session.
- Number of matches in the reference: in English Premier League players, match-to-match coefficient of variation was 16.2% for high-speed running and 30.8% for sprint distance (Gregson et al., 2010).
- Labeling rule and week shape: the number of post-match days and a congested week change which labels exist. Both cited studies analyzed only weeks with 6 days between matches.
- Group ratio or player percent.
- Measure and threshold.
- Device, software, and settings in training and matches.
- Goalkeepers: a small match value makes the percent swing. Both cited studies left goalkeepers out.

**Units and typical range.** The percent has no unit. The file gives these findings from single teams, not targets:

| Population | Finding | Source |
|---|---|---|
| Spanish La Liga reserve team, 24 outfield players, 10 Hz GPS, 6-day weeks | MD-3: total distance 57%, high-speed running above 19.8 km/h 37%, sprint above 25.2 km/h 29%. MD-4: high-speed running 43%, sprint 45%. | Martín-García et al., 2018 |
| Same team, accelerations and decelerations above 3 m/s² | MD+1 compensatory 80% to 86%, MD-4 71% to 72%, MD-3 62% to 69%, MD-2 56% to 61% | Martín-García et al., 2018 |
| Same team, MD+1 compensatory, players with less than 60 minutes | Total distance 53% | Martín-García et al., 2018 |
| Norwegian elite team, local positioning, four sessions in a typical week | Accelerations 131% to 166%, decelerations 108% to 134%, sprint distance 36% to 61%, high-intensity running 57% to 71% | Baptista et al., 2020 |

**Vendor equivalents.** None. No device reference file maps a match-day label or a percent of match.

**Reference file.** [match-day-load.md](../skills/gps-running-load/references/match-day-load.md)

## Force plate

These metrics come from a force plate, or from a Nordic hamstring device with a force sensor at each ankle. Force is in newtons (N).

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| CMJ jump height, takeoff velocity method | `takeoff velocity^2 / (2 x 9.81)` | m | [cmj-jump-height.md](../skills/force-plate/references/cmj-jump-height.md) |
| CMJ jump height, flight time method | `9.81 x flight time^2 / 8` | m | [cmj-jump-height.md](../skills/force-plate/references/cmj-jump-height.md) |
| Reactive strength index-modified (RSImod) | `jump height (m) / time to takeoff (s)` | m/s | [rsi-modified.md](../skills/force-plate/references/rsi-modified.md) |
| Flight time to contraction time ratio (FT:CT) | `flight time (s) / time to takeoff (s)` | No unit | [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md) |
| CMJ time to takeoff | `takeoff time - onset time` | s | [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md) |
| CMJ braking or propulsive net impulse | `sum of (force - body weight) x time step` over the phase, or `gross impulse - body weight x phase duration` | N·s | [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md) |
| CMJ relative net impulse | `net impulse / body mass` | N·s/kg | [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md) |
| CMJ countermovement depth | Lowest center of mass displacement between onset and takeoff | m | [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md) |
| IMTP gross peak force | Highest vertical force during the pull | N | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP net peak force | `gross peak force - body weight` | N | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP relative peak force | `peak force / body mass` | N/kg | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP allometric peak force | `peak force / body mass^0.67` | N/kg^0.67 | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| IMTP rate of force development (RFD) | `(force at X ms after onset - force at onset) / (X / 1000)` | N/s | [imtp-peak-force.md](../skills/force-plate/references/imtp-peak-force.md) |
| Eccentric hamstring peak force, per leg | Highest force on that leg's sensor in the best repetition | N | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring relative force, per leg | `peak force / body mass` | N/kg | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring two-limb average | `(left peak force + right peak force) / 2` | N | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Eccentric hamstring between-limb imbalance | `(stronger leg - weaker leg) / stronger leg x 100`, with the weaker side named | % | [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md) |
| Dynamic strength index (DSI), gross | `CMJ peak propulsive force (gross) / IMTP peak force (gross)` | No unit | [strength-ratios.md](../skills/force-plate/references/strength-ratios.md) |
| Dynamic strength index (DSI), net | `(CMJ peak propulsive force - CMJ body weight) / (IMTP peak force - IMTP body weight)` | No unit | [strength-ratios.md](../skills/force-plate/references/strength-ratios.md) |
| Eccentric utilization ratio (EUR), height | `CMJ height / SJ height` | No unit | [strength-ratios.md](../skills/force-plate/references/strength-ratios.md) |
| Eccentric utilization ratio (EUR), peak power | `CMJ peak power / SJ peak power` | No unit | [strength-ratios.md](../skills/force-plate/references/strength-ratios.md) |

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
| NCAA Division I men (n = 76), no arm swing (light bar across the shoulders), flight time method, 10 Hz low-pass filter, mean of 2 trials | 0.36 ± 0.07 m (mean ± SD) | Sole et al., 2018 |
| NCAA Division I women (n = 75), no arm swing (light bar across the shoulders), flight time method, 10 Hz low-pass filter, mean of 2 trials | 0.27 ± 0.06 m (mean ± SD) | Sole et al., 2018 |
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
- Arm swing and jump type: RSImod differs between jump types (Ebben & Petushek, 2010). The ranges below come from jumps without arm swing: a light bar across the shoulders (Sole et al., 2018) or hands on hips (McMahon et al., 2018b). In basketball players, arm swing raised RSImod by 20 to 24% (Heishman et al., 2019a).
- Trial summary: the mean of trial RSImod values differs from mean jump height divided by mean time to takeoff.

**Units and typical range.** Report RSImod in m/s and name the jump height method. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I men, CMJ without arm swing (light bar across the shoulders), flight time jump height, 10 N threshold, 10 Hz low-pass filter | 0.424 ± 0.102 m/s (mean ± SD); observed range 0.208 to 0.704 m/s | Sole et al., 2018 |
| NCAA Division I women, CMJ without arm swing (light bar across the shoulders), flight time jump height, 10 N threshold, 10 Hz low-pass filter | 0.314 ± 0.089 m/s (mean ± SD); observed range 0.135 to 0.553 m/s | Sole et al., 2018 |
| Professional male rugby league, CMJ without arm swing (hands on hips), takeoff velocity jump height, lowest and highest groups | 0.36 ± 0.03 and 0.53 ± 0.05 m/s (mean ± SD) | McMahon et al., 2018b |

Sole et al. (2018) used a 10 N threshold for both onset and takeoff, not the 5 standard deviation rule, and a 10 Hz low-pass Butterworth filter. Values from another threshold, filter, or jump height method are not directly comparable with these ranges. Time to takeoff averaged 0.868 ± 0.105 s for men and 0.870 ± 0.114 s for women (Sole et al., 2018), and 0.707 to 0.881 s across the rugby league groups (McMahon et al., 2018b). In a separate-day retest of adolescent cricket and netball athletes (n = 17, mean of 3 trials, 1 week apart), the coefficient of variation of RSImod was 6.11% and the standard error of measurement was 0.03 m/s (Thomas et al., 2017).

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

### CMJ strategy and fatigue metrics

**What it measures.** Strategy metrics show how an athlete produces a countermovement jump, not only how high the athlete jumps. Jump height is the outcome. Time to takeoff, the flight time to contraction time ratio (FT:CT), braking and propulsive net impulse, and countermovement depth describe the strategy. Strategy can change when jump height does not (Gathercole et al., 2015). These metrics are decision support for healthy athletes. A change is not a diagnosis, and it does not decide whether an athlete trains.

**Inputs.** The calculation needs these data:

- Flight time and time to takeoff in s, with the onset and takeoff rules named
- Braking and propulsive impulse in N·s, net or gross, with the phase windows named, and body weight in N
- Phase durations in s, when the export gives gross impulse
- Countermovement depth in m, with its sign rule named
- A force plate at 1000 Hz or more, at least 1 s of still standing before each jump, and at least 3 trials per session (McMahon et al., 2018a)

**Calculation.** Use these formulas:

```text
time to takeoff (s)               = takeoff time - onset time
FT:CT (no unit)                   = flight time (s) / time to takeoff (s)
braking net impulse (N·s)         = sum of (force - body weight) x time step, over the braking phase
propulsive net impulse (N·s)      = sum of (force - body weight) x time step, over the propulsion phase
net impulse from a gross value    = gross impulse (N·s) - body weight (N) x phase duration (s)
relative net impulse (N·s/kg)     = net impulse (N·s) / body mass (kg)
countermovement depth (m)         = lowest center of mass displacement between onset and takeoff
```

The terms and phases mean the following (McMahon et al., 2018a):

- `onset`: first instant force drops below body weight by more than 5 standard deviations of quiet standing force
- `unweighting phase`: onset to peak negative velocity, when force rises back to body weight
- `braking phase`: peak negative velocity to zero velocity, the lowest point of the center of mass
- `propulsion phase`: zero velocity to takeoff
- `net impulse`: force above body weight added up over time. It equals the change in momentum. Relative propulsive net impulse equals takeoff velocity.
- `gross impulse`: total force added up over time, with body weight included

Follow these steps from raw inputs:

1. Name the onset rule, takeoff rule, and phase windows from the device file.
2. Convert times to s, depth to m, impulse to N·s, and body weight to N.
3. Subtract body weight × phase duration from any gross impulse.
4. Divide flight time by time to takeoff for each trial.
5. Divide each net impulse by body mass, body weight / 9.81.
6. Take the absolute value of depth, so a deeper dip is a larger number.
7. Summarize trials with one rule for every session. Use the mean of trials, this repository's default, based on the studies in the reference file. Average each trial's ratio.
8. Judge a change with the noise band, using a typical error for the same trial summary.

**Worked example.** One made-up athlete, body weight 785.0 N (80.0204 kg), 3 trials in each of 2 sessions:

1. Session 1, trial 1: time to takeoff = 0.300 + 0.200 + 0.250 = 0.750 s. FT:CT = 0.548 / 0.750 = 0.7307.
2. Braking net impulse = 245.0 - 785.0 × 0.200 = 88.00 N·s, or 1.0997 N·s/kg. Propulsive net impulse = 408.3 - 785.0 × 0.250 = 212.05 N·s, or 2.6499 N·s/kg, which gives a jump height of 0.3579 m.
3. Mean of 3: time to takeoff 0.7483 s and 0.8367 s, FT:CT 0.7347 and 0.6503, jump height 0.3598 m and 0.3517 m, depth 0.300 m and 0.340 m.
4. Best trial (highest jump, trial 2 both days): FT:CT 0.7697 and 0.6882.
5. With made-up typical errors of 0.020 (FT:CT, mean of 3), 0.030 (FT:CT, best trial), 0.025 s (time to takeoff), and 0.012 m (jump height), the band for two single tests is 2.7719 × TE.

Result: FT:CT fell by 0.0845 against a band of ±0.0554, and time to takeoff rose by 0.0883 s against ±0.0693 s. Jump height changed by -0.0080 m against ±0.0333 m, inside the band. The best-trial FT:CT changed by -0.0815 against a wider band of ±0.0832, inside the band.

**Variants.** Phase definitions differ across software and studies. A scoping review of 30 studies found 90 different metrics across the 18 studies that used the CMJ. Phase names were mixed across all tests in the review. For drop jump contact time, one study used 5 standard deviations of quiet standing force and another a fixed 10 N for onset and takeoff (Badby et al., 2025). These variants are in use:

| Item | This page | Other definitions in use |
|---|---|---|
| Onset | 5 standard deviations below body weight | A 30 ms step back from that instant (McMahon et al., 2018a); a fixed 20 N offset (Heishman et al., 2019a); a trace back to the last sample at body weight |
| Braking start | Peak negative velocity | Minimum force; peak negative force (Huebner et al., 2025) |
| Propulsion start | Zero velocity | A 0.01 m/s velocity threshold (McMahon et al., 2018a) |
| Impulse | Net | Gross, with body weight included |
| Depth | Positive, in m | Negative, in m or cm; scaled to standing height (Bishop et al., 2022) |
| Trial summary | Mean of 3 | Best trial, by highest jump height |

FT:CT is not RSImod and not drop-jump RSI. Some software calls it "RSI". RSImod is jump height divided by time to takeoff. Track jump height and time to takeoff beside it, and use depth to help explain a change in time to takeoff (Bishop et al., 2022).

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Onset rule: finding onset 30 ms earlier in the example gives 0.780 s and an FT:CT of 0.7026. Finding it 30 ms later gives 0.720 s and 0.7611. Onset errors affect time-based metrics most (McMahon et al., 2018a).
- Takeoff and landing thresholds: they move flight time and time to takeoff together.
- Braking window: a braking phase that starts at minimum force is longer and includes force below body weight.
- Gross or net impulse: in the example, the gross braking impulse is 2.784 times the net value.
- Body weight: every net impulse, velocity, and displacement depends on it.
- Arm swing: FT:CT was higher with arm swing in basketball players (Heishman et al., 2019a).
- Cueing: a cue to jump fast shortens braking and raises braking force (McMahon et al., 2018a).
- Trial summary: the mean of 3 had a lower between-day coefficient of variation than the single highest jump for all 86 variables in professional rugby union players (Howarth et al., 2022). Mean CMJ height was more sensitive than the highest jump to fatigue and to gains after training across 151 studies (Claudino et al., 2017).

**Units and typical range.** Report time to takeoff in s, FT:CT with no unit, impulse in N·s or N·s/kg, and depth in m or cm. Use these ranges to check that data are plausible:

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I basketball players (14 men, 8 women), CMJ without arm swing, mean of 3, 1000 Hz, 20 N onset and takeoff offsets | FT:CT 0.672 ± 0.13 (mean ± SD) | Heishman et al., 2019a |
| Same players, CMJ with arm swing | FT:CT 0.773 ± 0.19 (mean ± SD) | Heishman et al., 2019a |

No range is given for impulse or depth. Relative propulsive net impulse squared / 19.62 must match the takeoff velocity jump height from the same trial. Between-day coefficients of variation for the mean of 3 ranged from 2 to 11% for concentric variables and 1 to 45% for eccentric variables in professional rugby union players (Howarth et al., 2022). Eccentric metrics often needed more than 3 jumps for a reliability coefficient of 0.80 in NCAA Division I men (Huebner et al., 2025). After an Australian football match, FT:CT fell in 22 elite players (effect size -0.65 ± 0.28) (Cormack et al., 2008). That is a group result, not a threshold for one athlete.

**Vendor equivalents.** The device files and vendor metric pages map these metrics:

- VALD ForceDecks `Contraction Time` and Hawkin `Time To Takeoff(s)`: time to takeoff. VALD reports ms with a 20 N start rule. Hawkin reports s and traces the start back to system weight.
- VALD ForceDecks `Flight Time:Contraction Time`: FT:CT. Hawkin CMJ `RSI` is the same ratio, flight time divided by time to takeoff. It is not RSImod.
- Hawkin `Braking Net Impulse` and VALD `Eccentric Deceleration Impulse`: braking net impulse from peak negative velocity to zero velocity. VALD `Eccentric Braking Impulse` starts at minimum force, so it covers a different window. Hawkin `Braking Impulse` is gross. See the [Hawkin and VALD name collisions](vendor-metrics/hawkin-dynamics/README.md#hawkin-and-vald-name-collisions).
- Hawkin `Propulsive Net Impulse` and VALD `Concentric Impulse`: propulsive net impulse from zero velocity to takeoff. Hawkin `Propulsive Impulse` is gross. Hawkin `Relative Propulsive Net Impulse` is per kg.
- Hawkin `Countermovement Depth(m)`: lowest center of mass position, as a negative value in m. VALD `Countermovement Depth`: largest displacement from start of movement to takeoff, in cm.

**Reference file.** [cmj-strategy-metrics.md](../skills/force-plate/references/cmj-strategy-metrics.md)

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
2. For each athlete, date, and side, keep the highest `peak_force_n` among the valid repetitions: those with `status` `ok` that you did not flag in step 1.
3. Divide each leg's peak by `body_mass_kg` from the same day.
4. Average the left and right peaks.
5. Calculate the imbalance, and record which side is weaker.
6. For each earlier test the user cites, subtract the earlier value from the new value for each leg. Compare each change with the noise band, 1.96 × TE × √(1 + 1/n), where n is the number of tests in the baseline mean.
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
6. Left-right difference = 35 N. With SE = TE = 21.7 N for each leg, the band is 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the stronger leg. The 35 N difference is inside the band. This TE comes from a separate-day retest, so label the band as likely wider than needed for a same-session difference.

Result: neither the 25 N change nor the 35 N difference can be told apart from measurement noise with these data. This does not show that the legs are equal or that nothing changed.

**Variants.** The imbalance formula above is one of several:

- Log ratio: 100 × ln(right / left). Injury studies on this test did not use the imbalance formula above. They used a left-to-right ratio (Opar et al., 2015; Bourne et al., 2015). Opar et al. (2015) log-transformed the ratio only to calculate group means. Neither paper prints an equation for one athlete. Offer the log ratio as an option, because it gives the same size whichever leg is stronger. Do not say it matches the injury studies.
- Other asymmetry formulas give different numbers from the same legs (Bishop et al., 2018). Never compare an imbalance value with a published value calculated another way.
- For the SE in the asymmetry band, use SE = TE for single or best repetitions. For a mean of k repetitions, use a pooled squad coefficient of variation × the leg's value / √k. Take TE or the coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own repetitions or from the same repetitions you are judging.
- For a left-right difference from one session, use a within-session TE when such a study exists. If only a separate-day TE exists, such as Opar et al. (2013), use it, and label the band as likely wider than needed. Day-to-day changes that affect both legs alike cancel out of a same-session difference. In 22 collegiate basketball players, across 16 force measures from a two-plate CMJ with and without arm swing, within-session TE was a median 0.90 times the separate-day TE, with a range of 0.77 to 0.99 (Heishman et al., 2019b).

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
- Do not call low Nordic strength a training target. Training choices stay with the coach.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- When a difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal."

**Vendor equivalents.** The device files map these metrics:

- VALD NordBord `leftMaxForce`, `rightMaxForce`: peak force at the ankle hook for each leg. VALD states the unit as N, which is not confirmed in the API. It is force at the ankle, not hamstring muscle force.
- VALD NordBord `leftAvgForce`, `rightAvgForce`: in the NordBord app, the average of the peaks of all repetitions in the test. Whether the API field uses the same rule is not confirmed.
- VALD NordBord `leftMaxForcePerKg`, `rightMaxForcePerKg`: peak force divided by body mass, in N/kg. Body weight is entered in the NordBord app or pulled from VALD Hub. Check which body weight was entered or pulled.
- VALD NordBord `leftTorque`, `rightTorque`: force multiplied by the lever arm from the knee to the ankle hook, which the device estimates from the knee position setting, in N·m as VALD states it, not confirmed in the API. Report it as given, labeled as the device's value. It depends on the knee position setting.
- VALD NordBord imbalance (in the app only): described as the percentage difference between left and right maximums, with a second imbalance from left and right averages. VALD does not publish the formula. A VALD research summary used `|L − R| / (L + R)` for hamstring asymmetry, which differs from the ForceDecks glossary formula, and VALD does not say which one the app uses. The API has no imbalance field. Compute imbalance yourself with a stated formula.

**Reference file.** [eccentric-hamstring-force.md](../skills/force-plate/references/eccentric-hamstring-force.md)

### Dynamic strength index and eccentric utilization ratio

**What it measures.** The dynamic strength index (DSI) shows how much of an athlete's isometric mid-thigh pull (IMTP) peak force the athlete also produces in a jump. The eccentric utilization ratio (EUR) shows how much a countermovement helps the athlete jump, by comparing a countermovement jump (CMJ) with a squat jump (SJ), which starts from a held squat with no dip. Each ratio has no unit and changes when either test changes. The reference file found no survey that reports how many practitioners use either ratio. In one survey of elite male soccer practitioners, 35% of those who tested strength used the IMTP, and 45% of those who tested power used the squat jump (Asimakidis et al., 2024). Published DSI bands are study settings, not recommendations. The coach makes every training decision.

**Inputs.** The calculation needs these data:

- An export with a test type column, so each trial is labeled CMJ, SJ, or IMTP
- For the DSI: CMJ peak propulsive force and IMTP peak force in N, both gross or both net
- For the EUR: CMJ and SJ jump height in m from the same method, or peak power in W, from the same session
- Body weight in N from each trial's quiet period, for the net DSI
- The same sampling rate, filter, and trial rule for every test

**Calculation.** Use these formulas:

```text
DSI, gross (no unit)       = CMJ peak propulsive force, gross (N) / IMTP peak force, gross (N)
DSI, net (no unit)         = (CMJ peak propulsive force - CMJ body weight) / (IMTP peak force - IMTP body weight)
DSI, SJ version (no unit)  = SJ peak force (N) / IMTP peak force (N)
EUR, height (no unit)      = CMJ height (m) / SJ height (m)
EUR, peak power (no unit)  = CMJ peak power (W) / SJ peak power (W)
```

The terms mean the following:

- `CMJ peak propulsive force`: the highest vertical force in the propulsion phase, from zero velocity or 0.01 m/s to takeoff (McMahon et al., 2017; Ripley et al., 2025)
- `gross`: force that includes body weight. The papers do not use the words gross or net. McMahon et al. (2017) report CMJ propulsion peak force of about 25 N/kg and IMTP peak force of 31 to 47 N/kg and do not describe subtracting body weight, so the reference file assumes gross over gross. That default is the repository's choice.
- `net`: force minus the same trial's quiet period body weight
- `IMTP peak force`: the highest vertical force in the pull, as in the IMTP breakdown
- `CMJ height` and `SJ height`: jump height from one method for both jumps, preferably takeoff velocity

Follow these steps:

1. Keep the CMJ and IMTP trials for each athlete. For the EUR, keep the CMJ and SJ trials from one session.
2. Confirm each peak force is gross or net, and its phase window. Convert net to gross by adding that trial's body weight.
3. Check every SJ trial's force trace for a drop in force before the push. Flag a drop of 10% of body weight or more, the threshold Sheppard and Doyle (2008) used, or name a stricter rule.
4. Apply one trial rule, the mean of trials or the best trial, to every test.
5. Report the ratio with its version, both test values, and relative IMTP peak force.
6. Beside every DSI, state that force-based and impulse-based DSI agreed on training emphasis for 45.9% to 56.8% of athletes in one study, depending on the impulse method (Ripley et al., 2025).

**Worked example.** One made-up athlete, one session, all forces gross. CMJ body weight is 822 N, and IMTP body weight is 820 N:

| Test | Trials | Mean |
|---|---|---|
| IMTP peak force | 2690, 2720, 2700 N | 2703.33 N |
| CMJ peak propulsive force | 1905, 1935, 1920 N | 1920.00 N |
| CMJ height | 0.352, 0.361, 0.346 m | 0.3530 m |
| SJ height | 0.318, 0.324, 0.309 m | 0.3170 m |

The calculation runs this way:

1. DSI, gross = 1920.00 / 2703.33 = 0.7102. With the best trial, 1935 / 2720 = 0.7114.
2. DSI, net = (1920.00 - 822) / (2703.33 - 820) = 1098.00 / 1883.33 = 0.5830.
3. EUR, height = 0.3530 / 0.3170 = 1.1136.
4. Four weeks later, the means are 2830.00 N for the IMTP and 1938.33 N for the CMJ. DSI, gross = 0.6849, a change of -0.0253.
5. With made-up squad coefficients of variation (CV) of 3.0% for the CMJ and 3.5% for the IMTP, the approximate CV of the ratio is √(3.0² + 3.5²) = 4.61%. The approximate typical error (TE) is 0.0327, and the noise band for two single tests is ±0.0908.

Result: the gross DSI of 0.710 falls in the 0.60 to 0.80 band the studies used, and the net DSI of 0.583 falls below 0.60, for the same tests. The change of -0.0253 is inside the noise band.

**Variants.** These versions are in use:

- CMJ or SJ version. Use the CMJ version. The DSI from the CMJ had an intraclass correlation coefficient (ICC) of 0.920 to 0.952 and a CV of 3.80 to 4.57% within session. The SJ version had an ICC of 0.419 and a CV of 15.91% in the first session (Comfort et al., 2018a).
- Force or impulse. The fixed impulse DSI divides CMJ propulsive impulse by IMTP impulse from onset to 250 ms. The matched impulse DSI uses an IMTP window as long as the CMJ propulsion phase. Both had unacceptable absolute reliability. The force-based and matched impulse DSI agreed on training emphasis for 17 of 37 athletes (45.9%), and the force-based and fixed impulse DSI for 21 (56.8%) (Ripley et al., 2025). These are the figures in the body of the paper. Its abstract reports slightly different values: 44.7%, 55.3%, and 84.2%.
- EUR from height or from peak power. They gave significantly different values in some preseason tests (McGuigan et al., 2006).
- Published DSI bands: the studies used below 0.60 to describe a ballistic emphasis, 0.60 to 0.80 a mixed emphasis, and above 0.80 a maximal strength emphasis (Comfort et al., 2018b; Ripley et al., 2025). Comfort et al. (2018b) attribute them to Sheppard et al. (2011). They are study settings, not recommendations.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Gross or net force: 0.710 against 0.583 in the worked example
- The CMJ phase window: a whole-jump peak can come from the braking phase
- Jump strategy: a deeper countermovement can lower CMJ peak propulsive force (McMahon et al., 2017)
- SJ start depth: published knee angles ranged from 45° to 110° (McMahon et al., 2017)
- A dip in the squat jump: in 125 trials, researchers saw one in 69 (55.2%), and force data showed one in 43 of the 56 others (Sheppard and Doyle, 2008)
- Jump height method, arm swing, trial rule, sampling rate, and filtering

**Units and typical range.** Both ratios have no unit. The reference file gives these published DSI values: 0.84 ± 0.15 (CMJ) and 0.82 ± 0.18 (SJ) in 27 male youth soccer and rugby league players (Comfort et al., 2018a); 0.82 ± 0.12 in 37 team sport athletes (Ripley et al., 2025), as the abstract reports, while Table 1 prints 0.79 ± 0.03 for the force-based DSI; 0.55 ± 0.10 and 0.92 ± 0.11 in the lowest and highest 20 of 53 male college athletes (McMahon et al., 2017), which are extreme groups and not for a range check; and 0.78 ± 0.19 for the SJ version in 19 male college athletes (Thomas et al., 2015). It gives no EUR range. A countermovement raised jump height in 18 men (Harman et al., 1990), so an EUR below 1.00 is a reason to check the trials. A ratio carries the error of both tests. The SJ version had a separate-day TE of 0.03 and a CV of 4.6% (Thomas et al., 2015). Combining two test CVs as √(CV₁² + CV₂²) is the reference file's approximation, not a published rule. For the net DSI, use CVs of net force, because gross-force CVs understate the noise. It assumes independent errors and can overstate the noise when both tests come from one session.

**Vendor equivalents.** No device file maps a DSI, an EUR, or a CMJ peak propulsive force. VALD ForceDecks `Peak Net Take-off Force / BM` is net force per kg, with no phase window stated in the device file. Hawkin `Jump Height(m)` covers the CMJ and the squat jump with the takeoff velocity method. Hawkin `Peak Force(N)` (isometric test) is gross IMTP peak force. Use VALD `Test Type` or Hawkin `testType_name` to label each trial.

**Reference file.** [strength-ratios.md](../skills/force-plate/references/strength-ratios.md)

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
- EliteForm rep `avgVelocity`: average bar velocity of one rep, measured by a camera. The phase and the rep start and end rules are not published. It is not mean propulsive velocity. EliteForm rep `peakVelocity` is the highest velocity of one rep, and its sampling window and smoothing are not published.
- EliteForm set `avgVelocity` and `peakVelocity`: the mean of the reps' `avgVelocity` and the mean of the reps' `peakVelocity`. The first is the mean over all tracked reps, not the best rep, and the second is not the highest peak in the set.
- EliteForm Predictive 1RM (beta): a load-velocity profile extended to a minimum velocity threshold for each lift. EliteForm advises loads of about 50% to 85% of the current 1RM, maximal concentric intent, and several distinct loads. The thresholds, the fit, and the exact rep selection rule are not published. EliteForm says it is validated for the squat, bench press, and deadlift. The reference file does not accept a velocity 1RM for the squat or deadlift, so call those values device estimates.
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
- EliteForm velocity loss: no vendor field. Compute it from the rep `avgVelocity` values in `/reps`, and name the reference rep.
- Perch `% Drop` goal: a rep is flagged when it falls more than the set percentage below the first rep or the best rep. The choices are 5%, 10%, 15%, 20%, or manual. The velocity measure is not stated, and whether `% Drop` appears in exports is not published.

**Reference file.** [velocity-loss.md](../skills/velocity-based-training/references/velocity-loss.md)

## Limb symmetry

These metrics compare one limb's test result with the other limb's result. The name "limb symmetry index" covers many different formulas, and studies use the same name for formulas that give different numbers (Bishop et al., 2016; Parkinson et al., 2021). Always name the formula.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| LSI (symmetry) | `nondominant limb / dominant limb x 100` | % | [limb-symmetry-index.md](../skills/limb-symmetry/references/limb-symmetry-index.md) |
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
- A reference limb definition for each athlete: dominant and nondominant, or larger value (stronger and weaker). The user names the dominant limb for any LSI.
- About three trials per limb (Bishop et al., 2018), with one trial summary for both limbs
- A TE or pooled squad coefficient of variation for the test, from a squad reliability study, or from a published reliability study of the same test, device, and population

**Calculation.** These are the formula variants you will meet most often:

```text
LSI (symmetry, %)                       = nondominant limb / dominant limb x 100
Percentage difference, signed (%)       = (right - left) / max(right, left) x 100
Dominant-referenced asymmetry (%)       = (dominant - nondominant) / dominant x 100
Bilateral asymmetry index, BAI-1 (%)    = (dominant - nondominant) / (dominant + nondominant) x 100
Mean-referenced asymmetry index (%)     = (dominant - nondominant) / ((dominant + nondominant) / 2) x 100
Log ratio (%)                           = 100 x ln(right / left)
Symmetry angle (%)                      = (45 - arctan(left / right) in degrees) / 90 x 100
Noise band for the left-right difference = 1.96 × √(SE_left² + SE_right²)
```

The terms mean the following:

- `dominant limb`: the limb the athlete prefers, often the kicking leg. Define it once per athlete and do not change it.
- `right`, `left`: the athlete's own right and left
- `max(right, left)`: the larger of the two values on that day
- Reference limb: the limb in the denominator of a formula
- `SE_left`, `SE_right`: the standard error of each limb's value, in the units of the measure. Use TE for single or best trials. For a mean of k trials, use a pooled squad coefficient of variation × the limb's value / √k. For a same-session difference, prefer a within-session TE.

Follow the reference-limb rule:

- Name the reference limb in every result, and keep the same definition across every session for that athlete.
- Report both raw limb values next to the percentage.
- Only percentage difference against the larger limb, BAI-1, the mean-referenced index, the log ratio, and the symmetry angle keep the same size whichever limb is stronger.
- Never infer the dominant limb from the data. If the user does not name it, do not calculate an LSI.
- An index can change because either limb changed. Track each limb's own value over time.

Follow these steps from raw inputs:

1. Confirm the side labels against the device file, so left and right are not swapped.
2. Choose one trial summary, the best trial or the mean of trials, and use it for both limbs.
3. Choose the formula. Use the one the user names. If the user names none, use percentage difference for unilateral tests and BAI-1 for bilateral tests (Bishop et al., 2018), and say so. For the Nordic hamstring test, a two-leg task, use percentage difference against the stronger leg, because Nordic studies express imbalance on a one-leg scale (Opar et al., 2015; Bourne et al., 2015). Offer the log ratio, because it gives the same size whichever leg is stronger. Do not say it matches the Nordic studies.
4. Calculate the value and its sign. State which side is larger.
5. Get an SE for each limb and state its source. Take TE or the coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own trials or from the same trials you are judging.
6. For a left-right difference from one session, use a within-session TE when such a study exists. If only a separate-day TE exists, use it, and label the band as likely wider than needed. State the retest interval of the TE.
7. Compare the difference between the raw limb values, in units, with the noise band. Use this one rule whatever formula you report. When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study.
8. If the difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal."
9. Report the raw values for both limbs, the formula, the reference limb, the result, the SE and its source, and the band.
10. For a bilateral test, add the device's own asymmetry formula next to BAI-1 only where the device documents it. Recompute it from the left and right values, never from the vendor column, and label it with the device name and the larger side. See "Vendor equivalents" below.

**Worked example.** One pair of values, right 25 cm and left 20 cm, run through every formula. It reproduces the example in Bishop et al. (2016). In Case A, the right limb is dominant:

| Formula | Calculation | Result |
|---|---|---|
| LSI, nondominant / dominant × 100 | 20 / 25 × 100 | 80.00% symmetry |
| Percentage difference, (right - left) / max × 100 | 5 / 25 × 100 | 20.00% |
| Dominant-referenced, (D - ND) / D × 100 | 5 / 25 × 100 | 20.00% |
| BAI-1, (D - ND) / (D + ND) × 100 | 5 / 45 × 100 | 11.11% |
| Mean-referenced asymmetry index, (D - ND) / mean × 100 | 5 / 22.5 × 100 | 22.22% |
| Symmetry angle | (45 - 38.66) / 90 × 100 | 7.04% |

The asymmetry formulas range from 7.04% to 22.22%, a spread of 15.18 percentage points, and the largest is 3.15 times the smallest. In Case B, the left limb is dominant, so the dominant limb is the weaker one. The dominant-referenced value becomes −25.00%, BAI-1 −11.11%, and the mean-referenced index −22.22%. The range becomes 7.04% to 25.00% in size, a spread of 17.96 points, with the largest 3.55 times the smallest. The LSI becomes 125.00%, because the nondominant limb is the stronger one. The log ratio gives 22.31%, and −22.31% with the limbs swapped.

The noise band example uses Nordic values of left 325 N and right 360 N, best repetition per leg, a difference of 35 N:

1. Option A, SE = 21.7 N per leg, the lowest typical error Opar et al. (2013) reported: band = 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the larger leg. The 35 N difference is inside the band. This TE comes from a separate-day retest, so label the band as likely wider than needed for a same-session difference.
2. Option B, mean of 3 repetitions (317.7 N and 353.0 N) with an assumed pooled squad coefficient of variation of 5%: SE = 5% × 317.7 / √3 = 9.17 N and 5% × 353.0 / √3 = 10.19 N. Band = 1.96 × √(9.17² + 10.19²) = 26.9 N. The mean-of-3 difference, 35.3 N, is outside the band.

Result: one pair of values gave 7.04%, 11.11%, 20.00%, 22.22%, 25.00%, 80.00%, and 125.00%, depending on the formula and reference limb. For the Nordic legs, the percentage difference is 9.72%, the log ratio is 10.23%, and BAI-1 is 5.11%. The SE decides whether the difference is larger than noise.

**Variants.** Use each variant this way:

- LSI: the most used index in the literature (Parkinson et al., 2021). Use it only when the user names each athlete's dominant limb. The weaker limb as a percentage of the stronger limb equals 100% minus the size of the percentage difference, and it never exceeds 100%. Name which version you report.
- Percentage difference: the same size of result whichever limb is stronger. Recommended for unilateral tests (Bishop et al., 2018). The signed version is positive when the right limb is larger (Bishop et al., 2021).
- Dominant-referenced asymmetry: a larger size of result when the dominant limb is the weaker one. Use it only when the user asks for it.
- BAI-1: recommended for bilateral tests, because each limb's force is part of the total (Bishop et al., 2018). It gives smaller values than the other formulas (Parkinson et al., 2021). With no dominant limb named, calculate (right - left) / (right + left) × 100 and say so.
- Mean-referenced asymmetry index: Bishop et al. (2018) list the same calculation as LSI-3, the asymmetry index, and the bilateral asymmetry index 2 (BAI-2).
- Log ratio: changes sign, but not size, when you swap the limbs, so it gives the same size whichever limb is stronger. That is the reason to offer it. It does not match the published Nordic studies. Opar et al. (2015) used a left-to-right ratio and log-transformed it only to calculate group means, not a value for each athlete.
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
- Retest interval of the TE: a separate-day TE includes day-to-day changes. Changes that affect both limbs alike cancel out of a same-session left-right difference, so a separate-day TE gives a wider band than needed. In 22 collegiate basketball players, across 16 force measures from a two-plate CMJ with and without arm swing, within-session TE was a median 0.90 times the separate-day TE, with a range of 0.77 to 0.99 (Heishman et al., 2019b).
- Vendor formula and sign: the VALD ForceDecks Technical Glossary V2.0 uses (left - right) / max(left, right) × 100, where a positive value means the left limb is larger. Never read the sign of a vendor value. Recompute from the left and right values.

**Units and typical range.** Report every value in % with the formula name, the reference limb, and the larger side. Use these ranges to check that data are plausible. They are not cut-offs:

| Population | Typical range | Source |
|---|---|---|
| Male soccer players (n = 313), bilateral jump force test, (stronger - weaker) / stronger × 100, positive when the right leg is stronger | 2.5th to 97.5th percentile of that sample: −15% to 15% | Impellizzeri et al., 2007 |
| Recreational sport athletes (n = 28), unilateral isometric squat and single-leg jumps, percentage difference | Mean asymmetry 5.3% or less; some individuals 20 to 30% | Bishop et al., 2021 |

Keep these limits:

- Many studies apply a fixed threshold, most often between 10 and 15%, to label asymmetry as abnormal. That threshold was not always supported by appropriate evidence (Parkinson et al., 2021). Prospective evidence that a fixed threshold marks higher injury risk is scarce (Bishop et al., 2018). Do not use any of these figures as a cut-off.
- Never apply a threshold as a pass or fail, a clearance, or a return-to-sport rule.
- If the user asks about a 90% LSI or any other clearance or return-to-sport criterion, state that symmetry is not a clearance criterion. Do not say whether the athlete meets it.

**Vendor equivalents.** The device files map these metrics:

- VALD ForceDecks asymmetry (any metric with the `Asym` limb): the Technical Glossary gives (Left − Right) ÷ max(Left, Right) × 100. VALD sources disagree on the sign. VALD does not publish the Hub CSV column list. A public parser for Hub exports shows asymmetry as text, such as `12.3 L` or `8.1 R`, where the letter names the side with the larger value. The `valdr` function `export_forcedecks_csv()` drops the limb columns. Recompute from the left and right values with one stated formula. Because VALD documents this formula, you may show it next to BAI-1 for a bilateral test. Recompute it from the left and right values, never from the vendor column. Label it with the device name and the larger side. For example, left 920 N and right 1000 N give "BAI-1: 4.17%, right larger" and "VALD ForceDecks formula: −8.00%, right larger".
- VALD NordBord imbalance (in the app only): described as the percentage difference between left and right maximums, with a second imbalance from left and right averages. VALD does not publish the formula. A VALD research summary used `|L − R| / (L + R)` for hamstring asymmetry, and VALD does not say which formula the app uses. The API has no imbalance field. Say the app formula is unpublished, and show no device value.
- Hawkin `L|R ...(%)` metrics, such as `L|R Avg. Braking Force(%)` and `L|R Peak Force(%)`: Hawkin does not publish the formula. The asymmetry report shows left-dominant values as positive. Recompute from the `Left ...` and `Right ...` columns. Say the Hawkin formula is unpublished, and show no device value. Hawkin `Force at Peak` columns give each plate's force at the instant of combined peak force, not each plate's own peak.
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
- Training-load measures cannot tell you whether a change raises or lowers injury risk (Impellizzeri et al., 2020b). Load is the dose, and wellness and test results are the response. Self-reported well-being worsened with acute rises in load and improved with acute reductions (Saw et al., 2016), so a composite that holds both counts a dose and its response together. Keep load measures out of the composite by default, and show them beside it. Do not include the ACWR as an input (Impellizzeri et al., 2020a).
- The user may still add a load measure, with its direction and reason, labeled as the user's choice.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team. A routine soreness rating on a wellness form is an input. A reported injury, pain, or symptom is not.

**Inputs.** The calculation needs these data:

- One row per `athlete_id` and `date`, with one column per input in its own unit, such as `sleep` (1 to 5) and `cmj_cm` (cm)
- Each input's direction, written down with the user
- The baseline window and the minimum number of baseline days for each input. If the user has none, offer at least 10 prior values, labeled as a practice default.
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

1. Join the inputs by athlete and date. Keep load measures out of the composite, and show them beside it.
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

## Testing profiles

These metrics show where one athlete's test result sits against the squad, the position group, or a matched published norm. Each one is a position, not a rating. The skill never ranks athletes, numbers them, or combines tests into one score.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Squad or group percentile, definition C | `100 x (m + 0.5 x k) / N` | 0 to 100, no unit | [squad-position.md](../skills/testing-profiles/references/squad-position.md) |
| Step size | `100 / N` | Percentile points | [squad-position.md](../skills/testing-profiles/references/squad-position.md) |
| SD units from the group mean | `(x - group mean) / group SD` | No unit | [squad-position.md](../skills/testing-profiles/references/squad-position.md) |
| Measurement error range | `x ± 1.96 x TE`, carried into percentiles and SD units | Units of the test | [squad-position.md](../skills/testing-profiles/references/squad-position.md) |
| Norm percentile, t method | `100 x T.DIST((x - mean) / (SD x √((n + 1) / n)), n - 1, TRUE)` | 0 to 100, no unit | [published-norms.md](../skills/testing-profiles/references/published-norms.md) |
| Interval on a norm percentile | Non-central t limits, or Clopper-Pearson limits for raw norm values | 0 to 100, no unit | [published-norms.md](../skills/testing-profiles/references/published-norms.md) |

### Squad and position group percentile

**What it measures.** The percentage of the squad or position group with a lower result on the same test day, with ties split in half. It describes where one result sits. It does not rate the athlete or order the squad.

**Inputs.** The calculation needs these data:

- One result per athlete for one test, from the same test day, protocol, device, method, and trial summary
- A list of athletes in the group with no result
- The typical error (TE) of the test, on the same protocol and trial summary

**Calculation.** Use definition C, the percentage below plus half the ties (Crawford et al., 2009). Definition C is this skill's choice among the three definitions:

```text
percentile = 100 x (m + 0.5 x k) / N
step       = 100 / N
SD units   = (x - group mean) / group SD
```

The terms mean the following:

- `m`: athletes in the group with a lower result
- `k`: athletes with the same result, counting this athlete
- `N`: athletes in the group with a result on this test day
- `group SD`: the sample SD of the group's results, with this athlete included

Follow these steps from raw inputs:

1. Keep results from one test day, protocol, device, method, and trial summary.
2. List athletes with no result, and leave them out of `N`.
3. Count `m` and `k`, and calculate the percentile and the step.
4. Calculate the group mean, the sample SD, and SD units.
5. Calculate the error range, `x ± 1.96 x TE` (Swinton et al., 2018).
6. Recalculate the percentile at each end of the error range, with teammates fixed. This range is the skill's method, not a published one.
7. Calculate the SD units range, `SD units ± 1.96 x TE / group SD`.
8. For a timed test, count athletes with a higher time, and multiply SD units by -1. Label it "percent of squad slower". In the error range step, also remove the athlete's own value from the count of higher times. In the spreadsheet, flip `(B8<D8)` to `(B8>D8)` along with `"<"&` to `">"&`. In Power BI, flip `[@v] < x` and `[@v] < limit` to `>`. In Tableau, use `'desc'` in place of `'asc'`. For A07's 10 m sprint of 1.76 s, TE 0.03 s, the percentile is 79.2 and the range is 45.8 to 95.8. Without the flip of `(B8<D8)`, the low end gives 104.2.

**Worked example.** A made-up squad of 12 tested a CMJ, best of 3, with TE 1.4 cm. One athlete did not test. Athlete A07 jumped 37.4 cm:

1. `N` = 12, step = 8.3 points.
2. `m` = 6 and `k` = 2, because one teammate also jumped 37.4 cm. Percentile = 100 x (6 + 0.5 x 2) / 12 = 58.3.
3. Squad mean = 37.14 cm, SD = 3.29 cm. SD units = 0.08.
4. Error range = 34.66 to 40.14 cm. Percentile range = 20.8 to 79.2. SD units range = -0.76 to 0.91.
5. Within the backs, a group of 5: percentile 70, step 20, percentile range 50 to 70.

Result: 58th percentile of 12 squad athletes, with measurement error 21st to 79th. Seven of 11 teammates sit inside her error range.

**Variants.** Three percentile definitions are in use: below (A), at or below (B), and below plus half the ties (C) (Crawford et al., 2009). For A07, they give 50, 66.7, and 58.3. Excel `PERCENTRANK.INC` and Tableau `RANK_PERCENTILE` use other definitions. On (6, 9, 9, 14), `RANK_PERCENTILE` gives 0.67 for 9, and definition C gives 50.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- Percentile definition, especially with ties
- Group size: one place is 8.3 points in a group of 12 and 20 points in a group of 5
- Who tested, and who is in the group
- Trial summary, test day, method, and device
- TE and the confidence level, for the error ranges

**Units and typical range.** Percentiles have no unit. With definition C and the athlete in the group, they run from `50 / N` to `100 - 50 / N`: 4.2 to 95.8 for 12 athletes. SD units have no unit and no published range. A gap of 0.2 SD units equals the default smallest worthwhile change.

**Vendor equivalents.** None.

**Reference file.** [squad-position.md](../skills/testing-profiles/references/squad-position.md)

### Norm percentile

**What it measures.** The estimated percentage of a published or local norm population below the athlete's result, with an interval for the norm's sample size and an error range for the athlete's score. A norm is a reference, never a pass mark, target, or rating.

**Inputs.** The calculation needs these data:

- A norm that matches the athlete on population, protocol, device and processing, trial summary, and units, and states its `n`
- The norm as a mean and SD, as raw values, or as a percentile table
- The athlete's result and the test's TE

**Calculation.** For a norm given as a mean and SD, use the t method of Crawford and Howell (1998):

```text
t          = (x - norm mean) / (norm SD x √((n + 1) / n))
percentile = 100 x T.DIST(t, n - 1, TRUE)
```

The terms mean the following:

- `x`: the athlete's result, in the norm's units
- `norm mean`, `norm SD`, and `n`: the norm's mean, sample SD, and sample size
- `T.DIST(t, n - 1, TRUE)`: the share of a t distribution on `n - 1` degrees of freedom below `t`

Follow these steps from raw inputs:

1. Check every item in the match table. Stop and name any item that does not match.
2. Convert the athlete's result to the norm's units.
3. Calculate `t` and the percentile.
4. Calculate the 95% interval with non-central t distributions (Crawford & Garthwaite, 2002), in Python or the authors' programs.
5. For raw norm values, use definition C with `m` and `k` from the norm sample, and the Clopper-Pearson interval `BETA.INV(0.025, x, N - x + 1)` to `BETA.INV(0.975, x + 1, N - x)`, with `x = m + 0.5 x k` (Crawford et al., 2009; Thulin, 2014).
6. For a percentile table, report the two rows the result sits between.
7. Read the norm at both ends of the error range, `x ± 1.96 x TE`.

**Worked example.** A made-up matched norm reports 40.0 ± 4.5 cm from 18 athletes. A07 jumped 37.4 cm, with TE 1.4 cm:

1. t = (37.4 - 40.0) / (4.5 x 1.0274) = -0.562.
2. Percentile = 100 x T.DIST(-0.562, 17, TRUE) = 29.1. The normal curve would give 28.2.
3. 95% interval on the percentile = 14.2 to 47.2.
4. Error range 34.66 to 40.14 cm gives 13.2 to 51.2.
5. A made-up local norm of 40 athletes, with 11 below and none tied, gives 27.5, with a Clopper-Pearson interval of 14.6 to 43.9.

Result: about the 29th percentile of the norm, with a norm interval of 14th to 47th, and 13th to 51st with measurement error.

**Variants.** The standard method reads `z = (x - mean) / SD` from the normal curve. Crawford and Howell (1998) suggest the t method when the norm sample is under 50. Raw norm values use definition C with a Clopper-Pearson interval. Percentile tables give a bracket only.

**What changes the number.** These choices change the result when the athlete's performance does not change:

- A norm from another population, protocol, device, method, or trial summary
- The norm's `n`: the same mean and SD give an interval of 23.4 to 33.5 from 200 athletes, and 9.4 to 57.7 from 8
- The method: normal curve or t method
- The definition behind a percentile table, which is often not stated
- A skewed norm, since both methods assume a normal distribution

**Units and typical range.** Percentiles from 0 to 100, no unit. In the worked example, 18 athletes give a norm interval 33 points wide.

**Vendor equivalents.** None. Vendor normative reports are not mapped in any device reference file.

**Reference file.** [published-norms.md](../skills/testing-profiles/references/published-norms.md)

## Sprint testing

These metrics come from timing gates, a radar or laser gun, or GPS. Time is in seconds (s), distance in meters (m), and speed in m/s.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Maximal sprinting speed (MSS) and tau (τ) | Least squares fit of `d(t) = MSS x (t + τ x e^(-t/τ)) - MSS x τ` to split times | m/s, s | [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md) |
| Maximal acceleration (MAC) | `MSS / τ` | m/s² | [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md) |
| Theoretical maximal horizontal force (F0) and velocity (V0) | Intercepts of the straight line fitted to `F_H = m x a(t) + k x (v - v_wind)^2` against `v` | N or N/kg, m/s | [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md) |
| Maximal horizontal power (Pmax) | `F0 x V0 / 4` | W or W/kg | [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md) |
| Ratio of force (RF) and its decrease (DRF) | `100 x F_H / sqrt(F_H^2 + (m x 9.81)^2)`; DRF is the slope of RF against `v` for `t > 0.3 s` | %, %·s/m | [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md) |
| Change of direction (COD) deficit, per side | `505 time - 10 m sprint time` | s | [change-of-direction-deficit.md](../skills/sprint-testing/references/change-of-direction-deficit.md) |
| COD deficit asymmetry | `(faster side deficit - slower side deficit) / faster side deficit x 100`, with the faster side named | % | [change-of-direction-deficit.md](../skills/sprint-testing/references/change-of-direction-deficit.md) |
| Repeated sprint percent decrement | `(total time / (n x best time) - 1) x 100` | % | [repeated-sprint.md](../skills/sprint-testing/references/repeated-sprint.md) |
| Repeated sprint fatigue index | `(slowest time - best time) / best time x 100` | % | [repeated-sprint.md](../skills/sprint-testing/references/repeated-sprint.md) |

### Sprint profile

**What it measures.** A sprint profile describes how fast an athlete gets up to speed and how fast they can run, from one maximal sprint. The acceleration-velocity layer (MSS, τ, MAC) comes from the timing data. The force-velocity layer (F0, V0, Pmax, RF, DRF) adds body mass, height, and air resistance (Samozino et al., 2016). Force-velocity values are model estimates for the center of mass, averaged over whole steps, not measured forces.

**Inputs.** The calculation needs these data:

- Split times in s and split distances in m, at least 3 splits (4 for an estimated time correction), or a radar, laser, or GPS speed trace of one maximal sprint
- The start stance, the distance from the front foot to the first gate, and what started the clock
- Body mass in kg and height in m from the test day, for the force-velocity layer
- Air temperature, barometric pressure, and wind for an outdoor test

**Calculation.** Use these formulas (Samozino et al., 2016, eq. 1 to 13):

```text
v(t)   = MSS x (1 - e^(-t/τ))
d(t)   = MSS x (t + τ x e^(-t/τ)) - MSS x τ
a(t)   = (MSS / τ) x e^(-t/τ)
MAC    = MSS / τ
F_H(t) = m x a(t) + k x (v(t) - v_wind)^2
k      = 0.5 x ρ x A_f x 0.9
ρ      = 1.293 x (P_b / 760) x 273 / (273 + T)
A_f    = 0.2025 x h^0.725 x m^0.425 x 0.266
RF(t)  = 100 x F_H / sqrt(F_H^2 + (m x 9.81)^2)
F0, SFV = intercept and slope of F_H against v
V0     = -F0 / SFV
Pmax   = F0 x V0 / 4
DRF    = slope of RF against v, for t > 0.3 s
```

The terms mean the following:

- `t`: time since the first push, in s
- `MSS`: maximal sprinting speed, in m/s
- `τ`: time constant, the time to reach 63.2% of MSS, in s (Jovanović & Vescovi, 2022)
- `m`, `h`: body mass in kg and height in m
- `v_wind`: wind in m/s, positive for a tailwind
- `ρ`, `P_b`, `T`: air density in kg/m³, pressure in Torr, and temperature in °C
- `A_f`: frontal area in m²; `k`: air resistance coefficient in kg/m
- `F_H`: net horizontal force in N; `RF`: ratio of force in %
- `SFV`: slope of the force-velocity line, in N·s/m

Follow these steps from raw inputs:

1. Convert splits to m and s, and record the start and trigger.
2. Add the chosen time correction (none, fixed, or estimated) to every split.
3. Fit MSS and τ by least squares on distance, with Excel Solver, a τ scan in a spreadsheet, R (`shorts`), or Python.
4. Compute MAC and the residual at each split.
5. Build a table from 0 s to the last split time in 0.1 s steps, with speed, acceleration, air resistance, horizontal force, power, and RF.
6. Fit a straight line to horizontal force against speed for F0, SFV, and V0. Compute Pmax.
7. Fit a straight line to RF against speed for `t > 0.3 s` for DRF. RFmax is the highest RF after 0.3 s.

**Worked example.** A made-up 40 m sprint with splits of 1.38, 2.11, 3.40, 4.62, and 5.79 s at 5, 10, 20, 30, and 40 m, body mass 78.0 kg, height 1.80 m, 20 °C, 760 Torr, no wind, and no time correction:

1. The fit gives MSS = 8.523 m/s and τ = 1.107 s. MAC = 7.696 m/s².
2. Residuals are −0.038, 0.051, 0.023, −0.082, and 0.042 m.
3. ρ = 1.2047 kg/m³, A_f = 0.5254 m², and k = 0.2849 kg/m.
4. F0 = 595.0 N (7.63 N/kg), V0 = 8.81 m/s, and Pmax = 1310.9 W (16.81 W/kg).
5. RFmax = 48.13% at 0.4 s, and DRF = −7.94 %·s/m.

Result: MSS 8.52 m/s, τ 1.107 s, MAC 7.70 m/s², F0 7.63 N/kg, V0 8.81 m/s, and Pmax 16.81 W/kg.

**Variants.** These variants are in use:

- Acceleration-velocity profile only: MSS, τ, and MAC, with no body mass or height.
- Force-velocity profile without air resistance: `F0 = m x MSS / τ`, `V0 = MSS`, and `Pmax = m x MSS x MAC / 4`. In the worked example, this gives 7.70 N/kg, 8.52 m/s, and 16.40 W/kg. Use it only for values computed in a BI tool, and label it.
- Fit to time instead of distance: the `shorts` R package treats time as the outcome (Jovanović & Vescovi, 2022). Samozino et al. (2016) fitted distance. The two can give slightly different MSS and τ.
- Speed trace fit: for radar, laser, or GPS, fit `v(t)` with a start time `t0`. A GPS acceleration-speed profile in situ (Clavel et al., 2023) gives A0 and S0, which are not the same numbers as MAC and MSS.

**What changes the number.** These choices change the result when the athlete has not changed:

- Time correction: the same model athlete starting 0.5 m behind the first gate gives MAC 13.50 m/s² and Pmax 27.94 W/kg with no correction, 7.89 and 17.17 with +0.3 s, 6.00 and 13.76 with +0.5 s, and 8.31 and 17.95 with an estimated 0.266 s. The true values were 7.73 m/s² and 16.83 W/kg. No single fixed correction suits every case (Jovanović & Vescovi, 2022).
- Start trigger: over 40 m, hand-release, start-line photocell, and foot-release starts were 0.17, 0.27, and 0.69 s faster than a block start reacting to a gun (Haugen et al., 2012).
- Body mass: 83 kg instead of 78 kg raises F0 from 595.0 to 633.3 N. Per-kilogram values barely change.
- Wind: a 2 m/s headwind with the same splits raises Pmax from 16.81 to 17.16 W/kg.
- RF start time: starting RF at 0.5 s instead of after 0.3 s gives RFmax 44.94% instead of 48.13%.
- Gate height, surface, footwear, sprint length, and number of splits.

**Units and typical range.** Report MSS and V0 in m/s, τ in s, MAC in m/s², F0 in N/kg, Pmax in W/kg, and DRF in %·s/m. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Typical range | Source |
|---|---|---|
| Elite or sub-elite male sprinters (n = 9), block start, trigger delay added | MSS 10.05 ± 0.66 m/s; τ 1.24 ± 0.14 s; F0 638 ± 84 N; V0 10.51 ± 0.74 m/s; Pmax 1680 ± 280 W; body mass 76.4 ± 7.1 kg | Samozino et al., 2016 |
| High-level female soccer players (n = 116), estimated time correction | MSS 7.77 ± 0.43 m/s; τ 1.10 ± 0.16 s; F0 7.1 ± 0.9 N/kg; V0 8.03 ± 0.48 m/s; Pmax 14.2 ± 1.8 W/kg; RFmax 48 ± 3% | Vescovi & Jovanović, 2021 |

No published reliability figure for the sprint profile is given. Measure your own typical error.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [sprint-profile.md](../skills/sprint-testing/references/sprint-profile.md)

### Change of direction deficit

**What it measures.** Change of direction deficit is the extra time an athlete needs to turn 180° in the 505 test, compared with running 10 m in a straight line. It isolates turning more than the 505 time does (Nimphius et al., 2016).

**Inputs.** The calculation needs these data:

- 505 times in s for each side, labeled by the plant foot
- 10 m sprint times in s from the same session
- The same start for both tests: stance, distance behind the first gate, and trigger

**Calculation.** Use this formula for each side:

```text
COD deficit_side (s) = 505 time_side (s) - 10 m sprint time (s)
deficit asymmetry (%) = (D deficit - ND deficit) / D deficit x 100
```

The terms mean the following:

- `505 time_side`: the timed 10 m around the turn, from the gate 10 m from the start, to the turn at 15 m, and back through the gate (Roso-Moliner et al., 2023), as the mean of trials (Nimphius et al., 2016) or the best trial (Dos'Santos et al., 2019)
- `10 m sprint time`: time over the first 10 m of a straight sprint, with the same trial summary
- `D`, `ND`: the faster side, with the shorter deficit, and the slower side (Dos'Santos et al., 2019)

Follow these steps from raw inputs:

1. Check that both tests used the same start in the same session.
2. Summarize the 10 m trials and each side's 505 trials with the same rule, mean or best.
3. Subtract the 10 m value from each side's 505 value.
4. Name the faster side and calculate the asymmetry.

**Worked example.** A made-up athlete with 10 m times of 1.92, 1.97, and 1.95 s, left 505 times of 2.45, 2.51, and 2.48 s, and right 505 times of 2.40, 2.41, and 2.45 s:

1. Mean 10 m time = 1.9467 s. Mean 505 time = 2.4800 s left and 2.4200 s right.
2. Deficit = 0.5333 s left and 0.4733 s right.
3. Asymmetry = (0.4733 − 0.5333) / 0.4733 × 100 = −12.68%, right side faster.
4. The 505 time asymmetry is only −2.48%.

Result: deficit 0.533 s left and 0.473 s right, with a −12.7% asymmetry toward the right.

**Variants.** These variants are in use:

- Mean of trials (Nimphius et al., 2016; Dos'Santos et al., 2018) or best trial (Dos'Santos et al., 2019). The best trial gives −10.42% in the worked example.
- Pro-agility (5-10-5) deficits: some studies compute one with a time formula (Yamashita et al., 2024) or a velocity formula over equal distances (Freitas et al., 2018). No validated pro-agility deficit was found.

**What changes the number.** These choices change the result when the athlete has not changed:

- Trial summary: mean versus best changes the asymmetry from −12.68% to −10.42% in the worked example.
- Start type: a 10 m time 0.05 s faster from a different start raises each deficit by 0.05 s, about 10.6% of the right deficit.
- Timing resolution: 0.01 s is about 2% of a 0.47 s deficit.
- Gate height, surface, footwear, side labels, and trial order.

**Units and typical range.** Report each side's deficit in s, and the asymmetry in % with the faster side named. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Typical range, mean of 3 trials | Source |
|---|---|---|
| Male soccer players (n = 16) | 0.493 ± 0.097 s left, 0.469 ± 0.117 s right; asymmetry −18.5 ± 12.2% | Dos'Santos et al., 2018 |
| Female soccer players (n = 15) | 0.533 ± 0.106 s left, 0.529 ± 0.170 s right; asymmetry −24.0 ± 18.4% | Dos'Santos et al., 2018 |

Within one session, the coefficient of variation of the deficit was 4.9% to 15.5%, against 1.1% to 3.3% for the 505 time (Dos'Santos et al., 2018). The −14.5% asymmetry line in Dos'Santos et al. (2019) came from their own sample and is a study setting, not a cut-off.

**Vendor equivalents.** None. No device reference file maps this metric.

**Reference file.** [change-of-direction-deficit.md](../skills/sprint-testing/references/change-of-direction-deficit.md)

### Repeated sprint scores

**What it measures.** A repeated sprint test is a set of short maximal sprints with short recoveries. Its scores show how well an athlete holds sprint times across the set: best time, mean time, and percent decrement.

**Inputs.** The calculation needs these data:

- Every sprint time in the set, in s
- The protocol: distance, number of sprints, recovery time, and recovery type

**Calculation.** Use these formulas:

```text
percent decrement (%) = (total time / (n x best time) - 1) x 100
fatigue index (%)     = (slowest time - best time) / best time x 100
```

The terms mean the following:

- `n`: the number of sprints in the set
- `best time`: the fastest sprint in the set, not necessarily sprint 1
- `total time`: the sum of all sprint times

Follow these steps from raw inputs:

1. Record the protocol, and check that the set has the expected number of sprints.
2. Find the best time, the total time, and the mean time.
3. Calculate the percent decrement.
4. Report best time, mean time, and percent decrement together.

**Worked example.** A made-up 6 × 30 m set with times of 4.31, 4.28, 4.36, 4.42, 4.47, and 4.51 s:

1. Best time = 4.28 s. Total time = 26.35 s. Mean time = 4.3917 s.
2. Ideal total = 6 × 4.28 = 25.68 s.
3. Percent decrement = (26.35 / 25.68 − 1) × 100 = 2.609%.
4. Fatigue index = (4.51 − 4.28) / 4.28 × 100 = 5.374%.

Result: best time 4.28 s, mean time 4.39 s, and percent decrement 2.61%.

**Variants.** Glaister et al. (2008) compared 8 fatigue formulas and found percent decrement the most valid and reliable. The fatigue index from the slowest and fastest sprints is pushed up by measurement noise. Oliver (2009) argues that any fatigue score from a small drop-off in performance is unreliable, so the skill reports best and mean time beside it.

**What changes the number.** These choices change the result when the athlete has not changed:

- Protocol: 12 × 30 m every 35 s gave 4.43 ± 1.79%, and every 65 s gave 1.97 ± 0.86%, in the same athletes (Glaister et al., 2008).
- Best sprint choice: using sprint 1 instead of the fastest sprint gives 1.895% instead of 2.609% in the worked example.
- Formula: the first-to-last version gives 4.640% in the worked example.
- A missing sprint: dropping sprint 4 gives 2.477%.

**Units and typical range.** Report times in s and percent decrement in %. In 10 physically active men, percent decrement was 4.43 ± 1.79% with a 35 s cycle and 1.97 ± 0.86% with a 65 s cycle, for 12 × 30 m. Between trials at least 48 hours apart, its coefficient of variation was 31.7% and 37.4% (Glaister et al., 2008). Use these values to check that data are plausible, not to rate athletes. Of 30 elite soccer practitioners who tested repeated sprints, 10 used 7 × 30 m with 20 s rest (Asimakidis et al., 2024).

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [repeated-sprint.md](../skills/sprint-testing/references/repeated-sprint.md)

## Conditioning speeds

These metrics turn running field tests into reference speeds and interval distances. Speed is in metres per second (m/s) or km/h. Maximal aerobic speed (MAS) is the lowest speed at which an athlete reaches maximal oxygen uptake. Each field test gives a different speed, so every speed carries its test name. The coach chooses every percentage, work time, and group boundary. No number here is a training recommendation.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| MAS, set-distance time trial | `distance_m / time_s` | m/s | [maximal-aerobic-speed.md](../skills/conditioning-speeds/references/maximal-aerobic-speed.md) |
| MAS, set-time run | `distance_m / set_time_s` | m/s | [maximal-aerobic-speed.md](../skills/conditioning-speeds/references/maximal-aerobic-speed.md) |
| 30-15 IFT final speed (VIFT) | Speed of the last completed stage. Not MAS. | km/h | [maximal-aerobic-speed.md](../skills/conditioning-speeds/references/maximal-aerobic-speed.md) |
| Anaerobic speed reserve (ASR) | `MSS - MAS` | m/s | [anaerobic-speed-reserve.md](../skills/conditioning-speeds/references/anaerobic-speed-reserve.md) |
| Speed reserve ratio (SRR) | `MSS / MAS` | none | [anaerobic-speed-reserve.md](../skills/conditioning-speeds/references/anaerobic-speed-reserve.md) |
| Speed at a chosen % of ASR | `MAS + (q / 100) x ASR` | m/s | [anaerobic-speed-reserve.md](../skills/conditioning-speeds/references/anaerobic-speed-reserve.md) |
| Interval distance | `reference speed x p / 100 x work time` | m | [interval-distances.md](../skills/conditioning-speeds/references/interval-distances.md) |
| Target time for a set distance | `set distance / (reference speed x p / 100)` | s | [interval-distances.md](../skills/conditioning-speeds/references/interval-distances.md) |

### Maximal aerobic speed

**What it measures.** Maximal aerobic speed (MAS) is the lowest running speed at which an athlete reaches maximal oxygen uptake (VO2max), also called vVO2max (Buchheit & Laursen, 2013b; Sandford et al., 2021). Field tests estimate it, and each test gives a different speed. The 30-15 Intermittent Fitness Test (30-15 IFT) final speed and Yo-Yo results are not MAS. Of 102 elite male soccer practitioners, 82% assessed aerobic capacity. Of the 78 who did, 29% used the 30-15 IFT, 24% the Yo-Yo IR2, and 22% the Yo-Yo IR1 (Asimakidis et al., 2024).

**Inputs.** The calculation needs these data:

- The test name, the result, its unit, the test date, and the surface
- For a set-distance trial, the time in s. For a set-time run, the distance in m.
- For the 30-15 IFT, the speed of the last completed stage in km/h

**Calculation.** Use the formula for the test:

```text
Set-distance time trial:  MAS_est (m/s) = distance (m) / time (s)
Set-time run:             MAS_est (m/s) = distance (m) / time (s)
30-15 IFT:                VIFT (km/h) = speed of the last completed stage. VIFT is not MAS.
Yo-Yo IR1 or IR2:         distance (m) or level. No verified conversion to MAS.
```

The terms mean the following:

- `MAS_est`: estimated MAS in m/s, labeled with its test
- `distance`: the set distance, or the distance covered in a set time, in m
- `time`: the time taken, or the set time, in s
- `VIFT`: the 30-15 IFT speed at the last completed stage (Haydar et al., 2011)

Follow these steps from raw inputs:

1. Name the test for each result.
2. Convert mm:ss to seconds.
3. Divide distance in m by time in s.
4. For the 30-15 IFT, record VIFT and divide by 3.6 for m/s. Label it VIFT.
5. For a Yo-Yo test, record the distance or level. Do not compute a speed.
6. Keep each test's speeds in their own column.

**Worked example.** One made-up athlete, tested in one month:

1. 2,000 m in 7:30 = 450 s. MAS = 2000 / 450 = 4.444 m/s (16.00 km/h).
2. 1,500 m in 5:20 = 320 s. Speed = 4.688 m/s (16.88 km/h).
3. 5-minute run of 1,350 m. Speed = 1350 / 300 = 4.500 m/s (16.20 km/h).
4. 30-15 IFT last completed stage 20.0 km/h. VIFT = 5.556 m/s, 1.25 times the 2,000 m MAS.

Result: MAS from the 2,000 m time trial is 4.444 m/s. The other three speeds are correct for their own tests and cannot replace it.

**Variants.** The tests differ in these ways:

- Set-distance trials: in 28 male Australian Rules football players, 1,200 m and 1,400 m speeds were above laboratory MAS, 1,600 to 2,200 m speeds did not differ, and 2,000 m agreed best (Bellenger et al., 2015). In 33 female players, 1,400 m agreed best, with equality estimated at 1.4 to 1.5 km (Lundquist et al., 2021).
- 5-minute run: 17.1 ± 2.2 km/h against 16.9 ± 2.6 km/h on a treadmill in 48 men, r = 0.94 (Berthon et al., 1997a).
- 1,500 m race in 12 elite middle-distance runners: `vVO2max (km/h) = (1,500 m speed (km/h) - 14.921) / 0.4266`. Race speed was 2.06 ± 1.03 km/h above vVO2max (Sandford et al., 2019b). Do not apply it to other athletes. For a 16.875 km/h 1,500 m it returns 4.58 km/h.
- 30-15 IFT: 30 s shuttle runs over 40 m with 15 s of passive rest, starting at 8 km/h and rising 0.5 km/h each stage (Haydar et al., 2011). In 26 male academy soccer players, 6-minute and 1,800 m trial speeds were 77 ± 3% and 79 ± 3% of VIFT. Their equations were `6-min speed = 3.24 + 0.61 x VIFT` and `1,800 m speed = -0.93 + 0.84 x VIFT`, in km/h. An estimate of 87% of VIFT was 0.57 and 0.45 m/s higher than the two trials (Smith et al., 2025). Buchheit (2008) set intermittent run distances from VIFT directly.
- Yo-Yo IR1 focuses on the aerobic system, and IR2 has a high anaerobic contribution (Bangsbo et al., 2008). No conversion to MAS is given.

**What changes the number.** These choices change the result when fitness does not change:

- Test type: one athlete gives 16.00, 16.20, 16.88, and 20.0 km/h on four tests.
- Time trial distance: shorter trials give faster speeds (Bellenger et al., 2015).
- Continuous or intermittent format: VIFT is higher than continuous test speeds (Smith et al., 2025).
- Surface: Yo-Yo IR1 distance was 2,370 ± 662 m on grass and 1,441 ± 463 m on artificial turf in male collegiate soccer players (Ferigne et al., 2025).
- Stage rule: VIFT is the last completed stage (Haydar et al., 2011).

**Units and typical range.** Report MAS in m/s or km/h with the test name. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Test | Typical range | Source |
|---|---|---|---|
| 48 men of mixed fitness | 5-minute run | 17.1 ± 2.2 km/h | Berthon et al., 1997a |
| Sub-elite runners (n = 18) | 5-minute run | 19.5 ± 0.9 km/h | Berthon et al., 1997b |
| Athletes from other sports (n = 23) | 5-minute run | 15.9 ± 1.2 km/h | Berthon et al., 1997b |
| Male academy soccer players (n = 26) | 6-minute trial; 1,800 m trial; VIFT | 4.39 ± 0.24 m/s; 4.49 ± 0.26 m/s; 20.46 ± 0.89 km/h | Smith et al., 2025 |
| Female collegiate soccer players (n = 24) | VIFT | 17.52 km/h (mean) | Paulsen et al., 2023 |

The 5-minute run had a standard error of measurement of 0.15 to 0.34 km/h, retested within 3 weeks (Dabonneville et al., 2003). Across 10 study groups, the coefficient of variation of VIFT was 1.5% to 6.0% (Grgic et al., 2021). VIFT moves in 0.5 km/h steps.

**Vendor equivalents.** None.

**Reference file.** [maximal-aerobic-speed.md](../skills/conditioning-speeds/references/maximal-aerobic-speed.md)

### Anaerobic speed reserve

**What it measures.** Anaerobic speed reserve (ASR) is the range of speeds between maximal aerobic speed (MAS) and maximal sprint speed (MSS) (Sandford et al., 2019a; Sandford et al., 2021). Two athletes with the same MAS can have different reserves, so the same percentage of MAS can use different shares of each reserve.

**Inputs.** The calculation needs these data:

- MAS in m/s from a continuous test, not VIFT or a Yo-Yo result
- MSS in m/s from one source: a sprint test, or the highest valid GPS speed
- The date of each test

**Calculation.** Use these formulas:

```text
ASR (m/s)                 = MSS (m/s) - MAS (m/s)
SRR                       = MSS (m/s) / MAS (m/s)
Speed at q% of ASR (m/s)  = MAS (m/s) + (q / 100) x ASR (m/s)
Percent of ASR at a speed = (speed - MAS) / ASR x 100
```

The terms mean the following:

- `MSS`: maximal sprint speed in m/s. Bundle et al. (2003) took it as the fastest speed over 8 steps, about 3 s or less.
- `SRR`: speed reserve ratio, with no unit (Sandford et al., 2019a)
- `q`: the percentage of ASR the coach chooses. Blondel et al. (2001) expressed speed as a percentage of the range between maximal speed and vVO2max.

Follow these steps from raw inputs:

1. Get MAS in m/s with its test and date.
2. Get MSS in m/s with its source and date.
3. Confirm MSS is above MAS.
4. Subtract MAS from MSS.
5. Show the days between the two tests.

**Worked example.** Two made-up athletes with MAS from a 2,000 m time trial in 450 s, 4.444 m/s:

1. Athlete 1 MSS 8.00 m/s: ASR = 3.556 m/s, SRR = 8.00 / (2000 / 450) = 1.800.
2. Athlete 2 MSS 9.40 m/s: ASR = 4.956 m/s, SRR = 9.40 / (2000 / 450) = 2.115.
3. At 120% of MAS, 5.333 m/s, athlete 1 uses 25.0% of ASR and athlete 2 uses 17.9%.
4. At 20% of ASR, athlete 1 runs 5.156 m/s and athlete 2 runs 5.436 m/s.

**Variants.** SRR is MSS / MAS. Percent of ASR describes a speed above MAS as a share of the reserve. In 10 participants, time to exhaustion at 120% and 140% of vVO2max correlated most closely with speed as a percentage of this reserve (r = −0.83 and −0.94) (Blondel et al., 2001).

**What changes the number.** These choices change the result when the athlete does not change:

- MSS source: with MAS 4.444 m/s, a radar MSS of 8.90 m/s gives ASR 4.456 m/s, and a GPS top speed of 8.60 m/s gives 4.156 m/s.
- MAS test: VIFT in place of MAS shrinks ASR.
- Timing gate split: an average split speed is lower than the peak inside it.
- Time between tests: Sandford et al. (2019b) set their laboratory test within 6 weeks of the race, a study setting.

**Units and typical range.** Report ASR in m/s or km/h with the MAS test and MSS source. In 19 elite 800 m and 1,500 m runners, SRR ran from 1.36 to 1.58 or more across 3 subgroups (Sandford et al., 2019a). No team-sport ASR range is verified.

**Vendor equivalents.** None.

**Reference file.** [anaerobic-speed-reserve.md](../skills/conditioning-speeds/references/anaerobic-speed-reserve.md)

### Interval distances

**What it measures.** An interval distance is how far an athlete covers in a work period at a percentage of a reference speed. The coach chooses the reference test, the percentage, the work time, and any group boundaries. Every distance is a straight-line distance.

**Inputs.** The calculation needs these data:

- A test table with athlete ID, test code, result, and date
- The coach's reference test, percentage, and work time
- Optional: MSS and a percentage of ASR, a set distance, or group boundaries

**Calculation.** Use these formulas:

```text
target speed (m/s)    = reference speed (m/s) x p / 100
distance (m)          = target speed (m/s) x work time (s)
target time (s)       = set distance (m) / target speed (m/s)
ASR-based speed (m/s) = MAS (m/s) + (q / 100) x ASR (m/s)
group                 = 1 + number of coach-set boundaries at or below the athlete's speed
```

Follow these steps from raw inputs:

1. Ask the coach for the reference test, percentage, and work time.
2. Take each athlete's latest result on that test, and convert it to m/s.
3. Multiply by the percentage divided by 100, then by the work time.
4. Label each distance with the test, date, percentage, work time, and "straight-line".
5. Sort or group only if the coach asks.

**Worked example.** The coach chose a 2,000 m time trial, 105%, and 30 s, with group boundaries at 4.3 and 4.5 m/s:

1. A0001, 450 s: MAS 4.444 m/s, distance 140.0 m, group 2.
2. A0002, latest of two trials, 470 s: MAS 4.255 m/s, distance 134.0 m, group 1.
3. A0003, 435 s: MAS 4.598 m/s, distance 144.8 m, group 3.
4. A0004 has only a 30-15 IFT result, so the row is blank and listed as missing.
5. Target time for 100 m at 105% of A0001's MAS = 100 / (4.444 x 1.05) = 21.43 s.

**Variants.** These study settings are examples, not recommendations:

- 15 s work and 15 s rest to exhaustion at 120% of MAS, 20% of ASR, or 95% of VIFT, in 17 male junior Australian Rules football players (Collison et al., 2022)
- Constant-speed runs to exhaustion at 90%, 100%, 120%, and 140% of vVO2max, lasting 839, 357, 122, and 65 s on average (Blondel et al., 2001)
- Intermittent run distances set from VIFT in 59 young intermittent sport players (Buchheit, 2008)
- Interval speeds from 95% of vVO2max up to 100% of maximal sprint speed (Buchheit & Laursen, 2013b)

Interval design involves up to 9 variables, including work and rest intensity and duration, repetitions, and series (Buchheit & Laursen, 2013a).

**What changes the number.** These choices change the result when the athlete does not change:

- Reference test: 105% for 30 s gives 140.0 m from a 4.444 m/s MAS and 175.0 m from a 5.556 m/s VIFT.
- Which result counts: latest, best, or mean.
- Turns: at 60% of vVO2max, oxygen uptake was 37 ± 5 mL/kg/min over 20 m shuttles and 33 ± 6 mL/kg/min in a straight line (Buchheit et al., 2011). No verified distance correction exists in the reference file.
- Rounding to 5 m or 10 m.

**Units and typical range.** Distances in m, speeds in m/s or km/h, times in s. Distances have no range of their own. Check the reference speed instead.

**Vendor equivalents.** None.

**Reference file.** [interval-distances.md](../skills/conditioning-speeds/references/interval-distances.md)

## Heart rate and sleep

These metrics trend morning heart rate variability (HRV), submaximal heart rate tests, and sleep for each athlete against their own baseline. HRV is the beat-to-beat change in the time between heartbeats. Every value is compared only with the same athlete on the same device and protocol. No number here diagnoses anything, screens for a sleep disorder, or says an athlete is ready, fatigued, ill, or at risk. If a value suggests a health problem, the skill stops and tells the user to involve the medical team.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| ln rMSSD | `LN(rMSSD in ms)` | none | [hrv-trends.md](../skills/heart-rate-and-sleep/references/hrv-trends.md) |
| ln rMSSD 7-day mean | Mean of valid daily ln rMSSD in the 7 days ending today, with at least 3 readings | none | [hrv-trends.md](../skills/heart-rate-and-sleep/references/hrv-trends.md) |
| ln rMSSD 7-day CV | `7-day SD / 7-day mean x 100` | % | [hrv-trends.md](../skills/heart-rate-and-sleep/references/hrv-trends.md) |
| Submaximal exercise heart rate (HRex) | `mean HR over the last 60 s of the stage / HRmax x 100` | % HRmax | [submaximal-heart-rate.md](../skills/heart-rate-and-sleep/references/submaximal-heart-rate.md) |
| Heart rate recovery (HRR60) | `HR at stage end - HR 60 s later` | bpm | [submaximal-heart-rate.md](../skills/heart-rate-and-sleep/references/submaximal-heart-rate.md) |
| Total sleep time (TST) | Device or diary TST | h or min | [sleep-trends.md](../skills/heart-rate-and-sleep/references/sleep-trends.md) |
| Sleep efficiency | `TST / time in bed x 100` | % | [sleep-trends.md](../skills/heart-rate-and-sleep/references/sleep-trends.md) |
| Sleep midpoint | `onset + (final wake - onset) / 2`, in minutes since noon | clock time | [sleep-trends.md](../skills/heart-rate-and-sleep/references/sleep-trends.md) |
| Midpoint regularity | Sample SD of the midpoint over 14 nights, with at least 8 nights | min | [sleep-trends.md](../skills/heart-rate-and-sleep/references/sleep-trends.md) |

### HRV trends

**What it measures.** ln rMSSD is the natural log of the root mean square of successive differences between heartbeat intervals, from a short morning reading. It reflects vagal activity (Plews et al., 2012). The skill trends a 7-day rolling mean and the day-to-day spread around it. Weekly and 7-day rolling means have shown better methodological validity than single-day values (Plews et al., 2013). HRV is decision support only.

**Inputs.** The calculation needs these data:

- One valid rMSSD per athlete per day, in ms, from one device
- The reading conditions: time after waking, position, recording length, and the part analysed
- A full calendar of days, with days without a valid reading left blank

**Calculation.** Use these formulas:

```text
rMSSD (ms)    = √( mean of (RR(i+1) − RR(i))² )
ln rMSSD      = LN(rMSSD)
7-day mean    = mean of the valid ln rMSSD values in the 7 days ending today
7-day SD      = sample SD of the same values
7-day CV (%)  = 7-day SD / 7-day mean × 100
weekly mean   = mean of the valid ln rMSSD values from Monday to Sunday
band          = baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n), from prior weekly means
```

The terms mean the following:

- `RR(i)`: the time between two heartbeats, in ms
- `valid`: a reading under the athlete's standard conditions that passed the artifact check, as set with the user. This definition is the repository's choice.
- `n`: the number of prior weekly means in the baseline. The offered default is at least 10, from the `monitoring-statistics` skill.

Follow these steps from raw inputs:

1. Keep one valid rMSSD per athlete per day.
2. Take the natural log of each day.
3. Count the valid values in the 7 days ending each day.
4. Leave the 7-day mean, SD, and CV blank with fewer than 3 readings. Plews et al. (2014) concluded that practitioners should use a minimum of 3 valid data points per week. Applying it to a rolling window is the repository's choice.
5. Compute the 7-day mean, SD, and CV.
6. Compute Monday-to-Sunday weekly means with at least 3 readings.
7. Build the usual-variation band from the prior weekly means. Using weekly means, not overlapping rolling means, is the repository's choice.
8. Compare the current 7-day mean with the band. Show the single-day value as context only, with no band.

**Worked example.** One made-up athlete with 5 valid readings in a week:

1. rMSSD 72, none, 65, 81, none, 58, and 69 ms give ln rMSSD 4.2767, none, 4.1744, 4.3944, none, 4.0604, and 4.2341.
2. Day 3 has 2 readings, so the 7-day mean is blank. Day 4 has 3, and the mean is 4.2818.
3. Day 7: mean 4.2280, SD 0.1236, CV 2.922%.
4. Ten prior weekly means: mean 4.2960, SD 0.0438. Multiplier t(9) × √1.1 = 2.3726. Band 4.1922 to 4.3998.
5. The week's mean is inside the band (z = −1.553). The single reading on day 6, 4.0604, is shown as context only. The band does not apply to one reading.

Result: 7-day mean ln rMSSD 4.228, CV 2.92%, 5 readings, inside the athlete's usual-variation band.

**Variants.** These forms are in use:

- Plews band: baseline mean ± 0.5 × baseline SD, from the first two weeks of daily values (Plews et al., 2012). It is that study's worthwhile-change setting, not a noise band and not a recommendation. The skill shows it only on request. In the worked example, a 14-day baseline (mean 4.2993, SD 0.1189) gives 4.2399 to 4.3587, and the week's mean sits below it.
- Overnight HRV from a wearable is a different measure from a morning reading. Never mix the two in one trend.

**What changes the number.** These choices change the result when the athlete has not changed:

- Log then mean, or mean then log: 4.2280 against 4.2341 in the worked example.
- Single day or 7-day mean.
- Band type: the usual-variation band and the Plews band disagree on the same week.
- Position, recording length, and device. Short (5 to 10 min) recordings on waking are described as best practice for athletes (Buchheit, 2014).
- Heat acclimatization and plasma volume increases tend to raise HRV without clear changes in fatigue or fitness (Buchheit, 2014).

**Units and typical range.** ln rMSSD has no unit. No population range rates an athlete. In two elite triathletes, morning supine rMSSD was 211.2 ± 29.7 ms and 130.8 ± 44.6 ms across days (Plews et al., 2012). Buchheit (2014) gives a typical error, as a CV, of about 12% for resting ln rMSSD and an SWC of about +3%. Of 137 top-division European soccer clubs, 36% used HRV, with 24 procedures identified (Rave et al., 2018).

**Vendor equivalents.** These device references list related fields:

- Firstbeat (`load-and-wellness`): `RMSSD`, `RMSSD Awake`, and `RMSSD Sleep` in ms, and the Quick Recovery Test, a 3-minute rest test scored against the athlete's history by a method Firstbeat does not publish.
- Polar Team Pro (`gps-running-load`): `rmssd` from a session. Polar's Recovery Pro uses resting tests, so a session value is not comparable.
- WHOOP `hrv_rmssd_milli`: RMSSD in ms, measured only during sleep. How WHOOP weights or windows the night is not confirmed, because the WHOOP support pages were not readable by an automated check on 2026-10-07. It is a sleep value from a wrist sensor, not a timed morning reading. WHOOP `resting_heart_rate` is also a sleep value, by an unpublished method. Leave out days where `user_calibrating` is true. WHOOP Recovery is proprietary and maps to no reference file.
- Oura `average_hrv`: the mean of 5-minute samples while asleep, in ms. The Oura app's Moment feature reports rMSSD, as the Oura reference file cites, but the API field does not name the statistic. Oura `lowest_heart_rate` and `average_heart_rate` come from 30-second samples, and the app shows 5-minute values, so the two can differ. Oura Readiness and its `hrv_balance` rating are proprietary ratings and map to no reference file.
- Never mix an overnight value from WHOOP or Oura with a morning reading from another device in one trend.

**Reference file.** [hrv-trends.md](../skills/heart-rate-and-sleep/references/hrv-trends.md)

### Submaximal heart rate and heart rate recovery

**What it measures.** Exercise heart rate (HRex) is the mean heart rate at the end of a fixed submaximal stage, as a percentage of maximal heart rate (HRmax). Heart rate recovery (HRR60) is the drop in heart rate in the 60 s after the stage. Heart rate indices appear sensitive to positive endurance training effects, and their use to infer short-term negative effects is questionable in team sports (Shushan et al., 2022).

**Inputs.** The calculation needs these data:

- 1 Hz heart rate from the stage start to 60 s after it ends
- The second at which the stage ends
- HRmax and its source
- The `test_drill` code, warm-up, time of day, temperature, and recovery position

**Calculation.** Use these formulas:

```text
HRex (bpm)      = mean heart rate over the last 60 s of the stage
HRex (% HRmax)  = HRex / HRmax × 100
HRR60 (bpm)     = HR at the end of the stage − HR 60 s after the end
```

The terms mean the following:

- `stage`: at least 3 to 4 min at a fixed speed or drill, so heart rate reaches a steady state (Buchheit, 2014; Shushan et al., 2022)
- `last 60 s`: Buchheit (2014) states the last 30 to 60 s is generally used. The 60 s default is the repository's choice.
- `HR at the end` and `HR 60 s after`: single 1 s samples. Using single samples is the repository's choice.

Follow these steps from raw inputs:

1. Record the conditions and the `test_drill` code.
2. Check the last 60 s of the stage for gaps. Stop if any sample is missing.
3. Average the 60 samples and divide by HRmax.
4. Subtract the sample 60 s after the end from the sample at the end.
5. Flag any test with a different drill or changed conditions. Compare only tests with the same drill.

**Worked example.** One made-up athlete, HRmax 198 bpm, 4 min run:

1. Last 60 s in 10 s blocks: 169, 170, 171, 170, 172, and 172 bpm. HRex = 170.67 bpm = 86.195% HRmax.
2. HR at the end 172 bpm, 60 s later 141 bpm. HRR60 = 31 bpm.
3. Previous test 88.0% HRmax: change −1.805 points. TE 3% of 86.195 = 2.586. Noise band 2.7719 × 2.586 = 7.168. Inside the band.
4. Previous HRR60 26 bpm: change +5 bpm. TE 25% = 7.75 bpm, band 21.48 bpm. With TE 2.8% to 13.8%, the band is 2.41 to 11.86 bpm.

Result: HRex 86.2% HRmax and HRR60 31 bpm. Neither change is beyond the noise band with the figures from Buchheit (2014).

**Variants.** These forms are in use:

- HRex in bpm, or as % of heart rate reserve (Shushan et al., 2022)
- HRR as an absolute or relative difference between exercise heart rate and heart rate 10 to 180 s after the test (Shushan et al., 2022)
- The largest drop in any rolling window, reported by some devices

**What changes the number.** These choices change the result when fitness has not changed:

- Window: the last 30 s give 86.532% and the last 60 s give 86.195% HRmax in the worked example.
- HRmax: 205 bpm in place of 198 bpm gives 83.252% HRmax.
- Drill, speed, and course.
- Temperature, sleep, diet, time of day, and stress (Shushan et al., 2022).
- HRR method and recovery position.

**Units and typical range.** HRex in bpm and % HRmax, HRR60 in bpm. No population range rates an athlete. Test variability: HRex about 3% CV and SWC about −1%, HRR60 about 25% CV and SWC about +7% (Buchheit, 2014). Across team-sport studies, HRex 1.0% to 3.5% and HRR 2.8% to 13.8% CV (Shushan et al., 2022). Of 41 high-level football clubs, 41% used submaximal protocols (Akenhead and Nassis, 2016). Of 74 protocols from 66 practitioners, 61 (82%) collected cardiorespiratory or metabolic outcomes, mostly heart rate indices (Shushan et al., 2023).

**Vendor equivalents.** The device files map these metrics:

- Firstbeat (`load-and-wellness`) `HR Recovery`: the largest drop in heart rate over a rolling window of 15 to 120 s, not a drop from a marked stop time. It is not the same as HRR60.
- WHOOP workout `average_heart_rate` and `max_heart_rate`: the method is not published. Use them only when the workout is the standard test and its start and end match the test stages. WHOOP gives no second-by-second series, so the last 60 s of a stage cannot be averaged. WHOOP `percent_recorded` is a data quality flag. WHOOP's body `max_heart_rate` may be an estimate, and the estimation method is not confirmed, so ask whether the HRmax was measured.
- Oura `bpm`: samples in 5-minute increments, with a `source` of awake, rest, sleep, workout, live, or session. That is too coarse for a test stage unless the sample rate during a workout is finer. Check the timestamps.

**Reference file.** [submaximal-heart-rate.md](../skills/heart-rate-and-sleep/references/submaximal-heart-rate.md)

### Sleep trends

**What it measures.** Total sleep time (TST), sleep efficiency, the sleep midpoint, and the night-to-night SD of the midpoint, each against the athlete's own baseline. A one-size-fits-all sleep target is unlikely to be ideal (Walsh et al., 2021). Wearable outputs come from proprietary algorithms, so values are compared within one device only (Chinoy et al., 2021).

**Inputs.** The calculation needs these data:

- One row per athlete and night: into bed, sleep onset, final wake, out of bed, and TST of the main sleep, plus nap time in minutes when a nap happened
- The device and app version, or diary

**Calculation.** Use these formulas:

```text
time in bed (min)          = out of bed − into bed
sleep efficiency (%)       = TST / time in bed × 100
sleep midpoint             = onset + (final wake − onset) / 2
midpoint regularity (min)  = sample SD of midpoints over 14 nights, at least 8 nights
```

The terms mean the following:

- `TST`: total time asleep in the main sleep, in minutes (Chinoy et al., 2021)
- `nap time`: minutes asleep in naps, reported in its own column beside TST and never added to it
- `night date`: the date of the into-bed time minus 12 hours, so a bedtime after midnight keeps the night it belongs to.
- All times are converted to minutes since 12:00 noon on the night date first, so times across midnight sort correctly.
- The 14-night window and 8-night minimum are the repository's choice. The SD needed more than a week of data for an unbiased estimate (Fischer et al., 2021).

Follow these steps from raw inputs:

1. Keep one row per night, with missing nights blank.
2. Set each night date, and convert times to minutes since noon on that date.
3. Compute time in bed, efficiency, and midpoint.
4. Compute the 14-night midpoint SD where at least 8 nights exist.
5. Build the usual-variation band for TST and efficiency from at least 10 prior nights, and compare each night with it.
6. Report nap time in its own column beside TST. Never add it to TST.

**Worked example.** One made-up athlete, 7 nights:

1. Night 1: into bed 22:50 (650), onset 23:10 (670), final wake 07:05 (1145), out of bed 07:15 (1155), TST 441 min.
2. Time in bed 505 min. Efficiency 87.33%. Midpoint 907.5 min since noon, 03:07:30.
3. Midpoint SD over the 7 nights: 22.07 min.
4. Ten prior nights of TST: mean 437.8, SD 12.23 min. Band 408.8 to 466.8 min.
5. Night 5, into bed at 00:20 on 2026-09-12, has a night date of 2026-09-11 and a midpoint of 962.5 min since noon. Its TST of 371 min is below the band (z = −5.46). The 7-night mean, 423.71 min, is shown as context only, because the band is built from single nights.

Result: one night below the athlete's usual range, on a night with a later bedtime. The week's mean TST was 423.71 min.

**Variants.** Midpoint regularity can use another sleep timing, such as onset or offset, or another regularity metric (Fischer et al., 2021).

**What changes the number.** These choices change the result when sleep has not changed:

- Plain clock minutes since midnight: the midpoint SD becomes 254.0 min instead of 22.07 min.
- Device: mean TST bias against polysomnography ranged from −0.3 to +46.8 min across 7 consumer devices (Chinoy et al., 2021).
- Computing TST as final wake minus onset.
- Window length and missing nights.
- Adding nap time into TST. This skill reports it in its own column.

**Units and typical range.** TST in h or min, efficiency in %, midpoint as a clock time, regularity in min. No population range rates an athlete. Of 145 practitioners, 61% had monitored sleep in the previous year, mostly by questionnaire (37%) or diary (26%) (Hough et al., 2021).

**Vendor equivalents.** These device references list related fields:

- Firstbeat (`load-and-wellness`): `Sleep duration`, detected sleep time from a neural network on heartbeat, respiration, and movement data.
- WHOOP: total sleep time is the sum of `total_light_sleep_time_milli`, `total_slow_wave_sleep_time_milli`, and `total_rem_sleep_time_milli`, because WHOOP returns no single total. `total_in_bed_time_milli` is time in bed. `sleep_efficiency_percentage` is time asleep divided by time in bed. WHOOP `sleep_consistency_percentage` compares sleep and wake times with the day before. It is proprietary, so report it as given. It is not the SD of the midpoint. `sleep_performance_percentage` is also proprietary.
- Oura: `total_sleep_duration` and `time_in_bed` are in seconds. Oura `efficiency` is a rating from 1 to 100 with an unpublished formula, and it is not confirmed to be time asleep divided by time in bed. The `sleep_regularity` contributor and the Sleep Score are proprietary ratings and map to no reference file. Stages from `sleep_algorithm_version` `v1` and `v2` are not directly comparable.
- Use the main overnight sleep from either vendor. Report nap time in its own column. Never add a nap into TST, and never average a nap into the night.

**Reference file.** [sleep-trends.md](../skills/heart-rate-and-sleep/references/sleep-trends.md)

## Strength training load

These metrics come from a weight room training log with one row per set. Load is in kilograms (kg). Convert pounds with lb × 0.45359237 before any sum. Every estimated 1RM is an estimate, not a test. The coach chooses the formula and the 1RM used to set loads.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Volume load | Sum over work sets of `reps x load`; exercise, session, and week totals | kg | [volume-load.md](../skills/strength-training-load/references/volume-load.md) |
| Relative load | `load / chosen 1RM x 100` | %1RM | [volume-load.md](../skills/strength-training-load/references/volume-load.md) |
| Estimated 1RM, Epley | `load x (1 + 0.0333 x reps to failure)`; the load itself at 1 rep | kg | [estimated-1rm.md](../skills/strength-training-load/references/estimated-1rm.md) |
| Estimated 1RM, Brzycki | `load / (1.0278 - 0.0278 x reps to failure)` | kg | [estimated-1rm.md](../skills/strength-training-load/references/estimated-1rm.md) |
| Reps to failure | `reps + RIR`, with `RIR = 10 - RPE` on the RIR-based scale | reps | [estimated-1rm.md](../skills/strength-training-load/references/estimated-1rm.md) |
| Best tested and best estimated 1RM | Running maximum to date, kept in separate columns | kg | [personal-bests.md](../skills/strength-training-load/references/personal-bests.md) |
| Relative strength | `load / body mass`, or `load / body mass^0.67` | kg/kg, kg/kg^0.67 | [personal-bests.md](../skills/strength-training-load/references/personal-bests.md) |

### Volume load

**What it measures.** Volume load is the total load lifted: reps multiplied by load, added up over sets. In a survey of 58 practitioners from 9 Southeast and East Asian countries, 81% quantified training load with volume load (Washif et al., 2025). It counts work done, not intensity or closeness to failure.

**Inputs.** The calculation needs these data:

- One row per set with athlete, date, session, exercise, set type, side, reps completed, load, and unit
- The load type of each set: external, bodyweight, timed, or band and chain
- Body mass in kg, only for the system mass variant

**Calculation.** Use these formulas:

```text
set volume load (kg)     = reps x load (kg)
exercise volume load     = sum of set volume load over work sets
session volume load      = sum of exercise volume load
weekly volume load       = sum of session volume load, Monday to Sunday
```

The terms mean the following:

- `reps`: reps completed, not planned
- `load`: external load in kg (McBride et al., 2009). McBride et al. compared four volume methods across three squat protocols, one of them a jump squat with no external load (0% of 1RM), and the methods gave different answers.
- `work sets`: sets the coach counts; leaving out warm-ups is the skill's default choice

Follow these steps from raw inputs:

1. Reshape the log to one row per set and convert loads to kg. Keep only rows with a `status` of `ok`.
2. Label set type and load type.
3. Apply the user's rule for bodyweight, single-leg and single-arm, timed, and band or chain sets. By default, the skill counts external loads, the bar and plates of band and chain sets, and the added load of weighted bodyweight sets. Each default is the skill's choice.
4. Multiply reps by load and add up by exercise, session, and week.
5. Report bodyweight reps and time under load apart from volume load.

**Worked example.** A made-up athlete of 82.0 kg did a back squat of 5 × 120, 5 × 120, 5 × 125, and 4 × 125 kg, a Romanian deadlift of 3 × 8 × 90 kg, a split squat of 3 × 8 per side with 2 × 20 kg dumbbells, 3 × 6 pull-ups, and 3 × 30 s planks:

1. Back squat = 600 + 600 + 625 + 500 = 2325 kg.
2. Romanian deadlift = 2160 kg. Split squat = 960 kg per side, 1920 kg both sides.
3. Session = 2325 + 2160 + 1920 = 6405 kg. Pull-ups: 18 reps. Plank: 90 s.
4. A second session of 3720 kg gives a week of 10125 kg.

Result: session volume load 6405 kg and weekly volume load 10125 kg, with bodyweight and timed sets reported apart.

**Variants.** These variants are in use:

- System mass volume load: `reps x (body mass + added load)` for exercises where the whole body moves. McBride et al. (2009) added body mass minus shank mass for a squat. The worked example's pull-ups give 1476 kg. Report it apart from external volume load.
- Per side or both sides for single-leg and single-arm exercises.
- Time under load, `sets x duration`, for isometric holds and timed sets, which have no volume load.
- A reps × %1RM total: no source defines it; label it as the skill's variant if the user asks.

**What changes the number.** These choices change the result when the training has not changed:

- Warm-up sets: counting one raises the session from 6405 to 6705 kg.
- Per side or both sides: the split squat adds 960 or 1920 kg.
- Units: a load in lb read as kg is 2.2 times too large.
- Dumbbell recording, planned versus completed reps, week start, and exercise mix.

**Units and typical range.** Report volume load in kg. The reference file gives no typical range, because it depends on the exercise and program. Compare an athlete with their own history in the same exercise.

**Vendor equivalents.** One device file maps these fields:

- EliteForm `/sets` `repsCompleted` and `actualWeight`: reps done and weight lifted, in the exercise's `weightUnit`. Convert lb with lb × 0.45359237. `repsAssigned`, `weight`, and `loadFactor` are the prescription, not the load lifted. `/sets` lists every set on the card, so keep only rows with `hasResults` set to true. `isBodyweight` marks a bodyweight set, and how `actualWeight` is recorded on one is not published.

**Reference file.** [volume-load.md](../skills/strength-training-load/references/volume-load.md)

### Estimated 1RM

**What it measures.** An estimated 1RM predicts the heaviest load an athlete could lift once from a set of several reps. It is an estimate, not a test. The `velocity-based-training` skill estimates 1RM from bar speed instead. Keep the two apart.

**Inputs.** The calculation needs these data:

- Load in kg and reps completed for each set
- Reps in reserve (RIR), RIR-based RPE, or a note that the set went to failure
- The coach's formula and rep limit

**Calculation.** Use these formulas:

```text
reps to failure = reps + RIR,  RIR = 10 - RPE
Epley:   e1RM = load x (1 + 0.0333 x reps to failure)
Brzycki: e1RM = load / (1.0278 - 0.0278 x reps to failure)
```

The terms mean the following:

- `RPE`: rating of perceived exertion on the RIR-based scale, where RPE 10 means 0 RIR (Zourdos et al., 2016)
- `reps to failure`: reps the athlete could have done in that set (Helms et al., 2016)
- Epley as written by Macarilla et al. (2022), citing DiStasio (2014); Brzycki as listed by Beia et al. (2024) and, in the form `load x 36 / (37 - reps)`, by Oberhofer et al. (2021). The two Brzycki forms are nearly equal within 1 to 10 reps, but not identical

Follow these steps from raw inputs:

1. Find RIR for each set, from the RIR column or 10 − RPE. Use RIR 0 only for a set to failure.
2. Add RIR to reps.
3. Leave out sets above the rep limit, 10 by default, and count them. The limit is the skill's choice and was not tested for Epley or Brzycki. It draws on the study settings of Reynolds et al. (2006), who concluded that linear equations for the chest press and leg press should use no more than 10 reps, and Roberts et al. (2025), whose modified equations used 4 to 10 reps.
4. Apply the chosen formula. Return the load itself for Epley at 1 rep, as the skill's choice.
5. Label each estimate with the formula, reps to failure, and rep limit.

**Worked example.** A made-up back squat set of 100 kg × 5 to failure, and a set of 100 kg × 5 at RPE 8:

1. Epley at 5 reps: 100 × 1.1665 = 116.65 kg. Brzycki: 100 / 0.8888 = 112.51 kg.
2. At RPE 8, reps to failure = 7. Epley 123.31 kg, Brzycki 120.02 kg.
3. One rep of RIR error (8 reps to failure) gives Epley 126.64 kg.
4. At 70 kg × 15, above the default limit, Epley gives 104.97 kg and Brzycki 114.60 kg.

Result: 116.65 kg (Epley) or 112.51 kg (Brzycki) from 5 reps to failure, rep limit 10.

**Variants.** These variants are in use:

- Other rep formulas: Lander, Mayhew et al., O'Conner et al., Wathen, and Kemmler et al. (Beia et al., 2024). Use one only with its formula and source.
- RIR-based estimates: no study was found that checked them against a tested 1RM.
- Bar speed estimates: see the `velocity-based-training` skill.

**What changes the number.** These choices change the result when strength has not changed:

- Formula: 116.65 or 112.51 kg from the same set.
- RIR judgment: people underpredicted reps to failure by 0.95 reps on average (Halperin et al., 2022). Predictions closer to failure were only slightly improved, and the 95% CI of that effect crossed zero.
- Rep count: at 100 kg, Epley minus Brzycki is 3.80 kg at 2 reps, 4.14 kg at 5, 2.48 kg at 8, and −0.07 kg at 10. They nearly agree near 10 reps and differ more away from it, most above 10.
- Exercise: at 80% of 1RM, about 8.8 reps in the bench press and 13.1 in the leg press (Nuzzo et al., 2024). Every formula underestimated the deadlift in LeSuer et al. (1997).
- Failure: a set stopped short of failure, with no RIR, gives an estimate that is too low.

**Units and typical range.** Report the estimate in kg. The reference file gives no typical range. These published figures describe the error of estimates and the spread of reps and RPE:

| Method | Finding | Source |
|---|---|---|
| Seven rep formulas, 67 untrained college students | r > 0.95; mean differences significantly different from zero for 5 of 7 formulas in the bench press and 6 of 7 in the squat; all underestimated the deadlift | LeSuer et al., 1997 |
| Regression from 5RM, 70 adults | Standard error of the estimate 2.98 kg chest press, 16.16 kg leg press | Reynolds et al., 2006 |
| Mayhew and Wathen, lat pull-down and seated row, 23 adults | Underestimated by 2.14 to 6.65 kg | Pérez-Castilla et al., 2021 |
| Between-individual SD of reps to failure, 7289 people | 2.51 reps at 80% and 4.36 reps at 60% of 1RM | Nuzzo et al., 2024 |
| RPE at tested 1RM, 15 powerlifters | 9.6 to 9.7 | Helms et al., 2017 |

**Vendor equivalents.** One device file maps these fields:

- EliteForm `/one-rms` `result`: the athlete's current 1RM for one exercise. A coach enters it, or EliteForm predicts it when `isPredicted` is true. Keep predicted and coach-entered values in separate columns.
- EliteForm Predictive 1RM (beta): an estimate from bar speed, from a load-velocity profile extended to a minimum velocity threshold for each lift. EliteForm advises loads of about 50% to 85% of the current 1RM, maximal concentric intent, and several distinct loads. The thresholds, the fit, and the exact rep selection rule are not published. This is not a rep-based formula such as Epley or Brzycki. Call it a device estimate that this repository has not validated. See the `velocity-based-training` skill.

**Reference file.** [estimated-1rm.md](../skills/strength-training-load/references/estimated-1rm.md)

### Personal bests and relative strength

**What it measures.** A personal best is the heaviest load lifted, or the highest 1RM estimated, in one exercise up to a date. Tested and estimated bests stay in separate columns. Relative strength divides the load by body mass.

**Inputs.** The calculation needs these data:

- One row per set with test sets labeled and missed attempts removed
- Estimated 1RMs from one formula
- Body mass in kg with its date

**Calculation.** Use these formulas:

```text
best tested 1RM      = running maximum of successful test singles
best estimated 1RM   = running maximum of estimates, one formula
relative strength    = load / body mass
allometric strength  = load / body mass^0.67
```

The terms mean the following:

- `body mass`: same day, or the nearest weigh-in before it, as the skill's choice
- `0.67`: the power Jaric (2002) recommended for muscle force; using it for a lifted load is the skill's choice

Follow these steps from raw inputs:

1. Sort each athlete's sets by date within each exercise.
2. Take the running maximum of test singles, and separately of estimates.
3. Divide by body mass for relative strength.
4. Judge a new best against the noise band.

**Worked example.** A made-up back squat history: test singles of 140.0 kg (2026-03-02, 84.0 kg body mass) and 147.5 kg (2026-06-01, 85.5 kg), and Epley estimates of 143.98 kg (2026-04-13) and 151.65 kg (2026-08-17):

1. Best tested rises from 140.0 to 147.5 kg. The estimates do not change it.
2. Relative strength is 1.667 then 1.725 kg/kg. Allometric is 7.19 then 7.49 kg/kg^0.67.
3. With a made-up typical error of 3.0 kg, the noise band is 1.96 × √2 × 3.0 = 8.32 kg. The 7.5 kg gain is inside it.

Result: best tested 147.5 kg (1.725 kg/kg) and best estimated 151.65 kg (Epley), reported apart.

**Variants.** These variants are in use:

- Rep max bests, such as best 3RM or 5RM, one rep count at a time.
- Ratio or allometric relative strength. Never compare the two.
- The `force-plate` skill reports relative isometric mid-thigh pull force in N/kg, which is not comparable with kg/kg.

**What changes the number.** These choices change the result when strength has not changed:

- Formula for the estimated best: 151.65 kg with Epley or 146.26 kg with Brzycki for the 2026-08-17 set.
- Body mass date, scaling method, what counts as a test, technique standard, and exercise variant.

**Units and typical range.** Report bests in kg with date and kind, and relative strength in kg/kg or kg/kg^0.67. No typical range is given. In 32 studies with 1595 participants, the test-retest coefficient of variation of 1RM ranged from 0.5% to 12.1%, median 4.2% (Grgic et al., 2020). Measure your own typical error.

**Vendor equivalents.** One device file maps these fields:

- EliteForm gold screen and leaderboards: they show new best results. How EliteForm defines a best, and which metrics it can rank, are not published. The API has no personal best endpoint.
- EliteForm `/weigh-ins` `weight`: body mass from the EliteForm scale. It is always in lb, unlike lift weights, which use each exercise's `weightUnit`. Convert before you divide.

**Reference file.** [personal-bests.md](../skills/strength-training-load/references/personal-bests.md)

## Sport-specific counts

These metrics count actions instead of distance run: pitches and throws, jumps, balls bowled, and swim distance. Counts are whole numbers. Swim distance is in meters (m), and jump height is in meters. Every total names its count type, its source, and its window. No count, total, or change in this section judges injury risk or sets a limit. A limit is compared only when the coach supplies it.

| Metric | Formula | Units | Reference file |
|---|---|---|---|
| Daily, weekly, and rolling totals | Sum of daily totals over the calendar day, the Monday-to-Sunday week, or the 7 or 28 calendar days ending today; complete only when every day is recorded | count or m | [count-totals.md](../skills/sport-specific-counts/references/count-totals.md) |
| All logged throws | `game pitches + bullpen pitches + warm-up throws + between-innings throws + practice throws` | count | [throwing-counts.md](../skills/sport-specific-counts/references/throwing-counts.md) |
| Game share of logged throws | `game pitches / all logged throws x 100` | % | [throwing-counts.md](../skills/sport-specific-counts/references/throwing-counts.md) |
| Difference from a coach's limit | `count - limit the coach supplied` | count | [throwing-counts.md](../skills/sport-specific-counts/references/throwing-counts.md) |
| Jump height sum | Sum of single-jump heights, or `jump count x mean jump height` per session | m | [jump-counts.md](../skills/sport-specific-counts/references/jump-counts.md) |
| Sensor recall and precision against video | `matched / video jumps`; `matched / sensor jumps` | ratio | [jump-counts.md](../skills/sport-specific-counts/references/jump-counts.md) |
| Swim distance and zone share | Sum of set distances, with `yd x 0.9144`; `zone distance / swim distance x 100` | m, % | [swim-and-bowling-volume.md](../skills/sport-specific-counts/references/swim-and-bowling-volume.md) |
| Valid balls | `whole overs x 6 + part-over balls` | count | [swim-and-bowling-volume.md](../skills/sport-specific-counts/references/swim-and-bowling-volume.md) |

### Count totals

**What it measures.** Count totals add up how many times an athlete did one action over a day, a calendar week, or a rolling window. A total is complete only when every day in its window is recorded. The weeks and windows are the skill's choice: Monday to Sunday, and 7 and 28 days.

**Inputs.** The calculation needs these data:

- One row per athlete, calendar day, and count type
- `0` on rest days, and a blank on days with activity but no count, or without the sensor

**Calculation.** Use these formulas:

```text
daily total           = sum of the count across every session that calendar day
weekly total          = sum of the 7 daily totals, Monday to Sunday
rolling 7-day total   = sum of the daily totals for the 7 calendar days ending today
rolling 28-day total  = sum of the daily totals for the 28 calendar days ending today
recorded days         = days in the window with a daily total, including 0
```

Follow these steps from raw inputs:

1. Keep each count type separate.
2. Add the sessions for each athlete, day, and count type. Mark a day missing if any session count is blank.
3. Add a `0` row for each rest day and a blank row for each unrecorded day.
4. Add the days in each week and each rolling window. Show a total only when every day is recorded. Otherwise, show the partial total with its recorded days.

**Worked example.** A made-up athlete's 14 days of throws from Monday 2026-08-03, with Thursday 2026-08-06 not recorded:

1. Week 1: 45 + 60 + 0 + 70 + 95 + 0 = 270 throws, 6 of 7 days.
2. Week 2: 50 + 65 + 0 + 55 + 80 + 110 + 0 = 360 throws, 7 of 7 days.
3. First complete rolling 7-day total, on 2026-08-13: 335 throws.

Result: week 1 is incomplete at 270 throws, and week 2 is 360 throws.

**Variants.** The `load-and-wellness` skill uses the same 7-day and 28-day windows for acute and chronic load.

**What changes the number.** These choices change the result when the athlete has not changed:

- Zero versus missing: writing 0 on the missing Thursday makes week 1 look complete.
- Rows versus days: rolling over the last 7 rows on 2026-08-15, with no rows for rest days, spans 9 calendar days and gives 525 instead of 360 throws.
- Week start and window length.

**Units and typical range.** Report whole-number counts, or meters for swim distance. Counts have no population range. Compare each athlete with their own history from the same source and count type.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [count-totals.md](../skills/sport-specific-counts/references/count-totals.md)

### Pitch and throw counts

**What it measures.** Pitch and throw counts show how many times an athlete threw, split by type and source. The grouping into all logged throws and the game share are the skill's choices. Game pitch counts miss warm-up throws, plyometric ball work, long toss, bullpens, flat-ground throws, and pitches between innings (Dowling et al., 2020). Pitch count limits by age exist as injury-prevention guidelines (Dowling et al., 2020). The skill compares a count with a limit only when the coach supplies the limit, and does not interpret injury risk. A systematic review found little agreement on the scientific basis for many pitch count recommendations (Bakshi et al., 2020).

**Inputs.** The calculation needs these data:

- Daily counts for each type: game pitches, bullpen pitches, warm-up throws, between-innings throws, and practice throws
- Sensor throws, kept as a separate count type
- The coach's limit, if the coach wants a comparison

**Calculation.** Use these formulas:

```text
all logged throws      = game + bullpen + warm-up + between-innings + practice
game share (%)         = game pitches / all logged throws x 100
difference from limit  = count - limit the coach supplied
```

Follow these steps from raw inputs:

1. Put each count type in its own column, and label self-reported counts.
2. Add the logged types. Keep sensor throws apart.
3. Calculate the game share.
4. Build totals as in Count totals.
5. Compare only the matching count type with the coach's limit, and report the difference in plain words.

**Worked example.** A made-up pitcher's week from Monday 2026-08-03:

1. Weekly totals: warm-up 105, practice 90, bullpen 30, between innings 24, and game 78.
2. All logged throws: 327, 7 of 7 days.
3. Game share: 78 / 327 x 100 = 23.9%.
4. Sensor throws: 290, 6 of 7 days, because the sensor was not worn on Thursday.
5. Limit comparison: 78 game pitches, 7 below the coach's limit of 85.

Result: the game pitch count shows 78 of 327 logged throws. Adding sensor and logged throws, 617, counts most throws twice.

**Variants.** Arm sensors also give a value per throw, such as an elbow torque estimate or a workload score. These values change with sensor placement: for fastballs, peak resultant acceleration was 160.5 ± 113.4 m/s² at the trunk, 1046.6 ± 184.0 m/s² at the upper arm, and 1288.7 ± 184.1 m/s² at the forearm (Agresta et al., 2022). One arm-sleeve sensor's elbow varus torque differed from motion capture by 9.4 ± 12.0 N·m (Camp et al., 2021). Lizzio et al. (2020) write that reliability depends almost entirely on a consistent sensor location. Never compare these values across placements or devices.

**What changes the number.** These choices change the result when the athlete has not changed:

- Count type: 78 game pitches or 327 logged throws in the worked example.
- Source: self-reported throws had a mean relative error of 24.76 ± 16.04%, and only 22% of players were within 10% of the observed count (Hoyne et al., 2022).
- Sensor placement and intensity grouping.

**Units and typical range.** Report whole-number counts. In youth players aged 11 and 12 over one season, the official pitch count was 168.1 ± 122.4 per player, against 1666.2 ± 642.2 sensor-recorded total throws (Wahl et al., 2020). In players aged 10 and 11, game pitches were 36 ± 18 of 158 ± 106 total throws on pitching days (Freehill et al., 2023). These figures show what a pitch count can miss. They are not ranges to judge an athlete.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [throwing-counts.md](../skills/sport-specific-counts/references/throwing-counts.md)

### Jump counts

**What it measures.** A jump count shows how many times an athlete jumped, from a sensor or video. The jump height sum adds the height of each jump, where the sensor gives it. The jump height sum is the skill's choice. Charlton et al. (2017) proposed a related index, jump count times average kinetic energy.

**Inputs.** The calculation needs these data:

- Single jumps with heights in m, or a session count and mean height
- For a video check: matched jumps, video jumps, and sensor jumps

**Calculation.** Use these formulas:

```text
jump height sum (m)  = sum of single-jump heights, or jump count x mean jump height
mean jump height (m) = jump height sum / jump count
recall               = matched jumps / video jumps
precision            = matched jumps / sensor jumps
```

Follow these steps from raw inputs:

1. Convert heights to m.
2. Count the jumps in each session, and add their heights.
3. Mark sessions without the sensor as missing.
4. For a week, divide the weekly height sum by the weekly count to get the mean height.

**Worked example.** A made-up volleyball player's week from Monday 2026-08-03:

1. Sessions: 118 jumps at 0.48 m, 142 at 0.46 m, and 96 at 0.55 m. Thursday is missing.
2. Height sums: 56.64, 65.32, and 52.80 m.
3. Week: 356 jumps and 174.76 m, 6 of 7 days. Mean height 174.76 / 356 = 0.4909 m.
4. Video check: 126 matched of 150 video jumps and 128 sensor jumps. Recall 0.84, precision 0.984.

Result: averaging the session means gives 0.4967 m instead of 0.4909 m.

**Variants.** Charlton et al. (2017) load index: jump count times average kinetic energy.

**What changes the number.** These choices change the result when the athlete has not changed:

- Device bias: a device that reads 5.5 cm high on every jump adds 142 x 0.055 = 7.81 m to one session's height sum.
- Recall: at 0.814, a sensor would record about 122 of 150 real jumps.
- Jump definition for video coding, and missing days.

**Units and typical range.** Report counts as whole numbers and heights in m. In professional men's volleyball, one device counted 99.3% of 3637 jumps, overestimated height by 5.5 cm on average, and had a minimal detectable change of 9.7 cm (Skazalski et al., 2018). In junior elite men's volleyball, precision was 0.995 to 1.000, recall 0.814 to 0.930, and height bias 3.57 to 4.28 cm (Charlton et al., 2017). Both studies were in volleyball, with one device.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [jump-counts.md](../skills/sport-specific-counts/references/jump-counts.md)

### Swim volume

**What it measures.** Swim volume is the distance swum, split by stroke and intensity zone when the log holds them. In an international survey of 31 people in competitive swimming, 84% used training load monitoring, and swim volume (96%) and session RPE (92%) were used most often (Barry et al., 2022).

**Inputs.** The calculation needs these data:

- One row per set: distance, unit (`yd` or `m`), stroke, and zone
- The coach's zone system

**Calculation.** Use these formulas:

```text
set distance (m) = set distance (yd) x 0.9144
swim distance (m) = sum of set distances in m
zone share (%)    = distance in one zone / swim distance x 100
```

Follow these steps from raw inputs:

1. Convert every set to m.
2. Add the sets for each session, then build totals as in Count totals.
3. Report distance by zone and by stroke. Compute each zone share against the total at the level of the view, such as athlete and day for a daily view.

**Worked example.** A made-up 5000 yd session:

1. Total: 5000 x 0.9144 = 4572.0 m.
2. Zones: zone 1 22.0%, zone 2 52.0%, zone 3 16.0%, and zone 4 10.0%.

Result: 4572.0 m. Adding it to a 5000 m session as 10000 m is wrong. The true total is 9572.0 m.

**Variants.** None.

**What changes the number.** These choices change the result when the athlete has not changed:

- Pool unit: yards or meters.
- Zone system.

**Units and typical range.** Report m, with the pool unit named. Swim distance has no population range.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [swim-and-bowling-volume.md](../skills/sport-specific-counts/references/swim-and-bowling-volume.md)

### Bowling volume

**What it measures.** Bowling volume is the number of balls a cricket bowler delivered in matches and training. An over is 6 valid balls, and a wide or a no ball does not count as one of them (MCC Law 17). Bowling frequency is usually measured as balls bowled or in a logbook, and both have been shown to be unreliable, mainly because of adherence issues in reporting (Constable et al., 2021).

**Inputs.** The calculation needs these data:

- Overs as whole overs and part-over balls for each spell
- Training balls from a coach or observer tally, as a separate count type

**Calculation.** Use these formulas:

```text
valid balls = whole overs x 6 + part-over balls
```

Follow these steps from raw inputs:

1. Ask how overs are written, and split a value such as `4.3` into 4 overs and 3 balls.
2. Calculate valid balls.
3. Keep match and training balls separate, then build totals as in Count totals.

**Worked example.** A made-up day: a match spell of `4.3` overs, then 36 net balls:

1. Valid balls: 4 x 6 + 3 = 27.
2. Day total: 27 + 36 = 63 balls.

Result: 63 balls. Reading `4.3` as a decimal gives 25.8 balls. The scorecard alone misses 36 of the 63 balls.

**Variants.** None.

**What changes the number.** These choices change the result when the athlete has not changed:

- Overs notation.
- Including training balls.

**Units and typical range.** Report whole-number balls, with overs beside them. Bowling counts have no population range.

**Vendor equivalents.** None. No device reference file maps these metrics.

**Reference file.** [swim-and-bowling-volume.md](../skills/sport-specific-counts/references/swim-and-bowling-volume.md)

## Vendor metric pages

Every exportable metric each vendor publishes is broken down on its page. The pages paraphrase vendor definitions and link to the vendor sources. The [vendor metrics index](vendor-metrics/README.md) lists every page:

| Vendor | Products | Page |
|---|---|---|
| VALD | ForceDecks and NordBord | [VALD ForceDecks and NordBord metrics](vendor-metrics/vald-forcedecks-nordbord/README.md) |
| VALD | ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware | [VALD other products](vendor-metrics/vald-other-products/README.md) |
| Hawkin Dynamics | Force plates and TruStrength | [Hawkin Dynamics metrics](vendor-metrics/hawkin-dynamics/README.md) |
| Catapult | Vector, Catapult One, and Perch | [Catapult metrics](vendor-metrics/catapult.md) |
| Kinexon | Kinexon | [Kinexon metrics](vendor-metrics/kinexon.md) |
| STATSports | Apex, Sonra, and Sonra Lite | [STATSports metrics](vendor-metrics/statsports.md) |
| Polar | Polar Team Pro | [Polar Team Pro metrics](vendor-metrics/polar-team-pro.md) |
| Firstbeat | Firstbeat Sports | [Firstbeat Sports metrics](vendor-metrics/firstbeat-sports.md) |
| WHOOP | WHOOP strap | [WHOOP metrics](vendor-metrics/whoop.md) |
| Oura | Oura Ring | [Oura metrics](vendor-metrics/oura.md) |
| EliteForm | PowerTracker, Strength Planner, and Lift Tracker | [EliteForm metrics](vendor-metrics/eliteform.md) |

## Sources

This page cites these sources, as the reference files list them. Fifteen sources have no DOI, and the entry says so:

- Abt G, Lovell R. The use of individualized speed and intensity thresholds for determining the distance run at high-intensity in professional soccer. J Sports Sci. 2009;27(9):893-898. https://doi.org/10.1080/02640410902998239
- Achten J, Jeukendrup AE. Heart rate monitoring: applications and limitations. Sports Med. 2003;33(7):517-538. https://doi.org/10.2165/00007256-200333070-00004
- Agresta C, Freehill MT, Zendler J, Giblin G, Cain S. Sensor location matters when estimating player workload for baseball pitching. Sensors (Basel). 2022;22(22):9008. https://doi.org/10.3390/s22229008
- Akenhead R, Nassis GP. Training load and player monitoring in high-level football: current practice and perceptions. Int J Sports Physiol Perform. 2016;11(5):587-593. https://doi.org/10.1123/ijspp.2015-0331 Read as an abstract only.
- Allard P, Martinez R, Deguire S, Tremblay J. In-season session training load relative to match load in professional ice hockey. J Strength Cond Res. 2022;36(2):486-492. https://doi.org/10.1519/JSC.0000000000003490
- Apweiler E, Wallace D, Stansfield S, Allerton DM, Brown MA, Stevenson EJ, Clifford T. Pre-bed casein protein supplementation does not enhance acute functional recovery in physically active males and females when exercise is performed in the morning. Sports. 2018;7(1):5. https://doi.org/10.3390/sports7010005
- Ardern CL, Glasgow P, Schneiders A, Witvrouw E, Clarsen B, Cools A, et al. 2016 Consensus statement on return to sport from the First World Congress in Sports Physical Therapy, Bern. Br J Sports Med. 2016;50(14):853-864. https://doi.org/10.1136/bjsports-2016-096278
- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Front Physiol. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047
- Atkinson G, Nevill AM. Statistical methods for assessing measurement error (reliability) in variables relevant to sports medicine. Sports Med. 1998;26(4):217-238. https://doi.org/10.2165/00007256-199826040-00002
- Bache-Mathiesen LK, Andersen TE, Clarsen B, Fagerland MW. Handling and reporting missing data in training load and injury risk research. Science and Medicine in Football. 2022;6(4):452-464. https://doi.org/10.1080/24733938.2021.1998587
- Badby AJ, Ripley NJ, McMahon JJ, Mundy PD, Comfort P. Scoping review of methods of monitoring acute changes in lower body neuromuscular function via force plates. PLoS One. 2025;20(5):e0322820. https://doi.org/10.1371/journal.pone.0322820
- Bakshi NK, Inclan PM, Kirsch JM, Bedi A, Agresta C, Freehill MT. Current workload recommendations in baseball pitchers: a systematic review. Am J Sports Med. 2020;48(1):229-241. https://doi.org/10.1177/0363546519831010 Read as an abstract only.
- Bangsbo J, Iaia FM, Krustrup P. The Yo-Yo intermittent recovery test: a useful tool for evaluation of physical performance in intermittent sports. Sports Med. 2008;38(1):37-51. https://doi.org/10.2165/00007256-200838010-00004
- Banister EW. Modeling elite athletic performance. In: MacDougall JD, Wenger HA, Green HJ, editors. Physiological Testing of the High-Performance Athlete. 2nd ed. Champaign (IL): Human Kinetics Books; 1991:403-424. ISBN 0873223004. Book chapter, not peer reviewed, no DOI. Read through the Internet Archive full-text search: https://archive.org/details/physiologicaltes0000unse (accessed 2026-10-02).
- Banister EW, Hamilton CL. Variations in iron status with fatigue modelled from training in female distance runners. Eur J Appl Physiol Occup Physiol. 1985;54(1):16-23. https://doi.org/10.1007/BF00426292
- Banister EW, Morton RH, Fitz-Clarke J. Dose/response effects of exercise modeled from training: physical and biochemical measures. Ann Physiol Anthropol. 1992;11(3):345-356. https://doi.org/10.2114/ahs1983.11.345
- Banyard HG, Nosaka K, Haff GG. Reliability and validity of the load-velocity relationship to predict the 1RM back squat. J Strength Cond Res. 2017;31(7):1897-1904. https://doi.org/10.1519/JSC.0000000000001657
- Baptista I, Johansen D, Figueiredo P, Rebelo A, Pettersen SA. Positional differences in peak- and accumulated- training load relative to match load in elite football. Sports. 2020;8(1):1. Published online 2019-12-23. https://doi.org/10.3390/sports8010001
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-220. https://doi.org/10.1093/ije/dyh299
- Barry L, Lyons M, McCreesh K, Powell C, Comyns T. International survey of training load monitoring practices in competitive swimming: how, what and why not? Phys Ther Sport. 2022;53:51-59. https://doi.org/10.1016/j.ptsp.2021.11.005 Read as an abstract only.
- Bartlett JD, O'Connor F, Pitchford N, Torres-Ronda L, Robertson SJ. Relationships between internal and external training load in team-sport athletes: evidence for an individualized approach. Int J Sports Physiol Perform. 2017;12(2):230-234. https://doi.org/10.1123/ijspp.2015-0791
- Bassek M, Raabe D, Memmert D, Rein R. Analysis of motion characteristics and metabolic power in elite male handball players. J Sports Sci Med. 2023;22(2):310-316. https://doi.org/10.52082/jssm.2023.310
- Batterham AM, Hopkins WG. Making meaningful inferences about magnitudes. Int J Sports Physiol Perform. 2006;1(1):50-57. https://doi.org/10.1123/ijspp.1.1.50
- Bauer J, Muehlbauer T, Geiger S, Gruber M. Interaction between the leg recovery test and subjective measures of fatigue in handball players: short-, mid-, and long-term assessment. Front Sports Act Living. 2024;6:1474385. https://doi.org/10.3389/fspor.2024.1474385
- Beia R, Wassermann A, Raps S, Mayhew J, Uder M, Kemmler W. Developing accurate repetition prediction equations for trained older adults with osteopenia. Sports (Basel). 2024;12(9):233. https://doi.org/10.3390/sports12090233
- Bellenger CR, Fuller JT, Nelson MJ, Hartland M, Buckley JD, Debenedictis TA. Predicting maximal aerobic speed through set distance time-trials. Eur J Appl Physiol. 2015;115(12):2593-2598. https://doi.org/10.1007/s00421-015-3233-6
- Berthon P, Dabonneville M, Fellmann N, Bedu M, Chamoux A. Maximal aerobic velocity measured by the 5-min running field test on two different fitness level groups. Arch Physiol Biochem. 1997;105(7):633-639. https://doi.org/10.1076/apab.105.7.633.11394
- Berthon P, Fellmann N, Bedu M, Beaune B, Dabonneville M, Coudert J, Chamoux A. A 5-min running field test as a measurement of maximal aerobic velocity. Eur J Appl Physiol Occup Physiol. 1997;75(3):233-238. https://doi.org/10.1007/s004210050153
- Bigg JL, Gamble ASD, Spriet LL. Internal load of male varsity ice hockey players during training and games throughout an entire season. Int J Sports Physiol Perform. 2022;17(2):286-295. https://doi.org/10.1123/ijspp.2021-0089
- Bishop C, Read P, Chavda S, Turner A. Asymmetries of the lower limb: the calculation conundrum in strength training and conditioning. Strength Cond J. 2016;38(6):27-32. https://doi.org/10.1519/SSC.0000000000000264
- Bishop C, Read P, Lake J, Chavda S, Turner A. Interlimb asymmetries: understanding how to calculate differences from bilateral and unilateral tests. Strength Cond J. 2018;40(4):1-6. https://doi.org/10.1519/SSC.0000000000000371
- Bishop C, Lake J, Loturco I, Papadopoulos K, Turner A, Read P. Interlimb asymmetries: the need for an individual approach to data analysis. J Strength Cond Res. 2021;35(3):695-701. https://doi.org/10.1519/JSC.0000000000002729
- Bishop C, Turner A, Jordan M, Harry J, Loturco I, Lake J, Comfort P. A framework to guide practitioners for selecting metrics during the countermovement and drop jump tests. Strength Cond J. 2022;44(4):95-103. https://doi.org/10.1519/SSC.0000000000000677
- Blondel N, Berthoin S, Billat V, Lensel G. Relationship between run times to exhaustion at 90, 100, 120, and 140% of vVO2max and velocity expressed relatively to critical velocity and maximal velocity. Int J Sports Med. 2001;22(1):27-33. https://doi.org/10.1055/s-2001-11357
- Borg GA. Psychophysical bases of perceived exertion. Med Sci Sports Exerc. 1982;14(5):377-381. https://doi.org/10.1249/00005768-198205000-00012
- Borg E, Kaijser L. A comparison between three rating scales for perceived exertion and two different work tests. Scand J Med Sci Sports. 2006;16(1):57-69. https://doi.org/10.1111/j.1600-0838.2005.00448.x
- Bosquet L, Montpetit J, Arvisais D, Mujika I. Effects of tapering on performance: a meta-analysis. Med Sci Sports Exerc. 2007;39(8):1358-1365. https://doi.org/10.1249/mss.0b013e31806010e0 Read as an abstract only.
- Bourne MN, Opar DA, Williams MD, Shield AJ. Eccentric knee flexor strength and risk of hamstring injuries in rugby union: a prospective study. Am J Sports Med. 2015;43(11):2663-2670. https://doi.org/10.1177/0363546515599633
- Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? Front Physiol. 2014;5:73. https://doi.org/10.3389/fphys.2014.00073
- Buchheit M. The 30-15 intermittent fitness test: accuracy for individualizing interval training of young intermittent sport players. J Strength Cond Res. 2008;22(2):365-374. https://doi.org/10.1519/JSC.0b013e3181635b2e
- Buchheit M, Al Haddad H, Millet GP, Lepretre PM, Newton M, Ahmaidi S. Cardiorespiratory and cardiac autonomic responses to 30-15 intermittent fitness test in team sport players. J Strength Cond Res. 2009;23(1):93-100. https://doi.org/10.1519/JSC.0b013e31818b9721
- Buchheit M, Al Haddad H, Simpson BM, Palazzi D, Bourdon PC, Di Salvo V, Mendez-Villanueva A. Monitoring accelerations with GPS in football: time to slow down? Int J Sports Physiol Perform. 2014;9(3):442-445. https://doi.org/10.1123/ijspp.2013-0187 (cited as Buchheit et al., 2014a)
- Buchheit M, Allen A, Poon TK, Modonutti M, Gregson W, Di Salvo V. Integrating different tracking systems in football: multiple camera semi-automatic system, local position measurement and GPS technologies. J Sports Sci. 2014;32(20):1844-1857. https://doi.org/10.1080/02640414.2014.942687 (cited as Buchheit et al., 2014b)
- Buchheit M, Haydar B, Hader K, Ufland P, Ahmaidi S. Assessing running economy during field running with changes of direction: application to 20 m shuttle runs. Int J Sports Physiol Perform. 2011;6(3):380-395. https://doi.org/10.1123/ijspp.6.3.380
- Buchheit M, Laursen PB. High-intensity interval training, solutions to the programming puzzle: Part I: cardiopulmonary emphasis. Sports Med. 2013;43(5):313-338. https://doi.org/10.1007/s40279-013-0029-x
- Buchheit M, Laursen PB. High-intensity interval training, solutions to the programming puzzle. Part II: anaerobic energy, neuromuscular load and practical applications. Sports Med. 2013;43(10):927-954. https://doi.org/10.1007/s40279-013-0066-5
- Bundle MW, Hoyt RW, Weyand PG. High-speed running performance: a new approach to assessment and prediction. J Appl Physiol. 2003;95(5):1955-1962. https://doi.org/10.1152/japplphysiol.00921.2002
- Camp CL, Loushin S, Nezlek S, Fiegen AP, Christoffer D, Kaufman K. Are wearable sensors valid and reliable for studying the baseball pitching motion? An independent comparison with marker-based motion capture. Am J Sports Med. 2021;49(11):3094-3101. https://doi.org/10.1177/03635465211029017 Read as an abstract only.
- Carton-Llorente A, Lozano D, Gilart Iglesias V, Marcos Jorquera D, Manchado C. Worst-case scenario analysis of physical demands in elite men handball players by playing position through big data analytics. Biol Sport. 2023;40(4):1219-1227. https://doi.org/10.5114/biolsport.2023.126665
- Charlton PC, Kenneally-Dabrowski C, Sheppard J, Spratford W. A simple method for quantifying jump loads in volleyball athletes. J Sci Med Sport. 2017;20(3):241-245. https://doi.org/10.1016/j.jsams.2016.07.007 Read as an abstract only.
- Chinoy ED, Cuellar JA, Huwa KE, Jameson JT, Watson CH, Bessman SC, Hirsch DA, Cooper AD, Drummond SPA, Markwald RR. Performance of seven consumer sleep-tracking devices compared with polysomnography. Sleep. 2021;44(5):zsaa291. https://doi.org/10.1093/sleep/zsaa291
- Claudino JG, Cronin J, Mezêncio B, McMaster DT, McGuigan M, Tricoli V, Amadio AC, Serrão JC. The countermovement jump to monitor neuromuscular status: a meta-analysis. J Sci Med Sport. 2017;20(4):397-402. https://doi.org/10.1016/j.jsams.2016.08.011
- Clavel P, Leduc C, Morin JB, Buchheit M, Lacome M. Reliability of individual acceleration-speed profile in-situ in elite youth soccer players. J Biomech. 2023;153:111602. https://doi.org/10.1016/j.jbiomech.2023.111602
- Collison J, Debenedictis T, Fuller JT, Gerschwitz R, Ling T, Gotch L, et al. Supramaximal interval running prescription in Australian Rules Football players: a comparison between maximal aerobic speed, anaerobic speed reserve, and the 30-15 Intermittent Fitness Test. J Strength Cond Res. 2022;36(12):3409-3414. https://doi.org/10.1519/JSC.0000000000004103
- Comfort P, Dos'Santos T, Beckham GK, Stone MH, Guppy SN, Haff GG. Standardization and methodological considerations for the isometric midthigh pull. Strength Cond J. 2019;41(2):57-79. https://doi.org/10.1519/SSC.0000000000000433
- Comfort P, Thomas C, Dos'Santos T, Jones PA, Suchomel TJ, McMahon JJ. Comparison of methods of calculating dynamic strength index. Int J Sports Physiol Perform. 2018;13(3):320-325. https://doi.org/10.1123/ijspp.2017-0255 Read as an abstract only.
- Comfort P, Thomas C, Dos'Santos T, Suchomel TJ, Jones PA, McMahon JJ. Changes in dynamic strength index in response to strength training. Sports. 2018;6(4):176. https://doi.org/10.3390/sports6040176
- Constable M, Wundersitz D, Bini R, Kingsley M. Quantification of the demands of cricket bowling and the relationship to injury risk: a systematic review. BMC Sports Sci Med Rehabil. 2021;13(1):109. https://doi.org/10.1186/s13102-021-00335-8
- Cormack SJ, Newton RU, McGuigan MR. Neuromuscular and endocrine responses of elite players to an Australian rules football match. Int J Sports Physiol Perform. 2008;3(3):359-374. https://doi.org/10.1123/ijspp.3.3.359
- Coyle EF, González-Alonso J. Cardiovascular drift during prolonged exercise: new perspectives. Exerc Sport Sci Rev. 2001;29(2):88-92. https://doi.org/10.1097/00003677-200104000-00009
- Coyne JOC, Nimphius S, Newton RU, Haff GG. Does mathematical coupling matter to the acute to chronic workload ratio? A case study from elite sport. Int J Sports Physiol Perform. 2019;14(10):1447-1454. https://doi.org/10.1123/ijspp.2018-0874
- Crawford JR, Garthwaite PH. Investigation of the single case in neuropsychology: confidence limits on the abnormality of test scores and test score differences. Neuropsychologia. 2002;40:1196-1208. https://doi.org/10.1016/S0028-3932(01)00224-X
- Crawford JR, Garthwaite PH, Slick DJ. On percentile norms in neuropsychology: proposed reporting standards and methods for quantifying the uncertainty over the percentile ranks of test scores. The Clinical Neuropsychologist. 2009;23(7):1173-1195. https://doi.org/10.1080/13854040902795018
- Crawford JR, Howell DC. Comparing an individual's test score against norms derived from small samples. The Clinical Neuropsychologist. 1998;12(4):482-486. https://doi.org/10.1076/clin.12.4.482.7241
- Cummins C, Orr R, O'Connor H, West C. Global positioning systems (GPS) and microtechnology sensors in team sports: a systematic review. Sports Med. 2013;43(10):1025-1042. https://doi.org/10.1007/s40279-013-0069-2
- Dabonneville M, Berthon P, Vaslin P, Fellmann N. The 5 min running field test: test and retest reliability on trained men and women. Eur J Appl Physiol. 2003;88(4-5):353-360. https://doi.org/10.1007/s00421-002-0617-1
- de Sousa Neto IV, de Sousa NMF, Neto FR, Falk Neto JH, Tibana RA. Time course of recovery following CrossFit Karen benchmark workout in trained men. Front Physiol. 2022;13:899652. https://doi.org/10.3389/fphys.2022.899652
- de Vet HC, Terwee CB, Ostelo RW, Beckerman H, Knol DL, Bouter LM. Minimal changes in health status questionnaires: distinction between minimally detectable change and minimally important change. Health Qual Life Outcomes. 2006;4:54. https://doi.org/10.1186/1477-7525-4-54
- Delp M, Chesbro GA, Pribble BA, Miller RM, Pereira HM, Black CD, Larson RD. Higher rating of perceived exertion and lower perceived recovery following a graded exercise test during menses compared to non-bleeding days in untrained females. Front Physiol. 2023;14:1297242. https://doi.org/10.3389/fphys.2023.1297242
- Dillon P, Lovell R, Joyce D, Norris D. Maximum speed exposures in Australian rules football: do methods matter? Sci Med Footb. 2024;8(3):287-290. https://doi.org/10.1080/24733938.2023.2211048 Read as an abstract only.
- Dos'Santos T, Jones PA, Comfort P, Thomas C. Effect of different onset thresholds on isometric midthigh pull force-time variables. J Strength Cond Res. 2017;31(12):3463-3473. https://doi.org/10.1519/JSC.0000000000001765
- Dos'Santos T, Thomas C, Comfort P, Jones PA. Comparison of change of direction speed performance and asymmetries between team-sport athletes: application of change of direction deficit. Sports. 2018;6(4):174. https://doi.org/10.3390/sports6040174
- Dos'Santos T, Thomas C, Jones PA, Comfort P. Assessing asymmetries in change of direction speed performance: application of change of direction deficit. J Strength Cond Res. 2019;33(11):2953-2961. https://doi.org/10.1519/JSC.0000000000002438
- Douchet T, Paizis C, Carling C, Babault N. Influence of a modified versus a typical microcycle periodization on the weekly external loads and match day readiness in elite academy soccer players. J Hum Kinet. 2024;93:133-144. https://doi.org/10.5114/jhk/182984
- Dowling B, McNally MP, Chaudhari AMW, Oñate JA. A review of workload-monitoring considerations for baseball pitchers. J Athl Train. 2020;55(9):911-917. https://doi.org/10.4085/1062-6050-0511-19
- Dutra YM, Mendonça PT, Goodall S, Zagatto AM. Neuromuscular fatigue and perceived fatigability in the hours following a high-intensity endurance running depend on the exercise protocol. Eur J Sport Sci. 2026;26(8):e70176. https://doi.org/10.1002/ejsc.70176
- Ebben WP, Petushek EJ. Using the reactive strength index modified to evaluate plyometric performance. J Strength Cond Res. 2010;24(8):1983-1987. https://doi.org/10.1519/JSC.0b013e3181e72466
- Edwards S. The Heart Rate Monitor Book. Sacramento (CA): Fleet Feet Press; Port Washington (NY): Polar CIC; 1993. Third printing, October 1993. The Library of Congress catalogs the book (ISBN 0963463306, LCCN 92062064) as c1992. Book, not peer reviewed, no DOI. The five zones are listed on p. 56 of the third printing. A text search of that printing found Chapter 12 on pp. 113-123, but no zone weights on those pages. The search covered text only, so a figure could still hold them. The zone weights come from Paulson et al. (2015) and Hourcade et al. (2018).
- Epp-Stobbe A, Tsai M-C, Klimstra MD. Comparison of imputation methods for missing rate of perceived exertion data in rugby. Mach Learn Knowl Extr. 2022;4(4):827-838. https://doi.org/10.3390/make4040041
- Exell TA, Irwin G, Gittoes MJR, Kerwin DG. Implications of intra-limb variability on asymmetry analyses. J Sports Sci. 2012;30(4):403-409. https://doi.org/10.1080/02640414.2011.647047
- Fanchini M, Ferraresi I, Modena R, Schena F, Coutts AJ, Impellizzeri FM. Use of the CR100 scale for session rating of perceived exertion in soccer and its interchangeability with the CR10. Int J Sports Physiol Perform. 2016;11(3):388-392. https://doi.org/10.1123/ijspp.2015-0273
- Fereday K, Hills SP, Russell M, Smith J, Cunningham DJ, Shearer D, McNarry M, Kilduff LP. A comparison of rolling averages versus discrete time epochs for assessing the worst-case scenario locomotor demands of professional soccer match-play. J Sci Med Sport. 2020;23(8):764-769. https://doi.org/10.1016/j.jsams.2020.01.002
- Ferigne G, Martin K, Ottinger C, Biscardi L. Playing surface impacts Yo-Yo intermittent recovery test (level 1) performance and validity of indirect VO2max estimation. Int J Exerc Sci. 2025;18(8):1142-1150. https://doi.org/10.70252/pgpl8156
- Fischer D, Klerman EB, Phillips AJK. Measuring sleep regularity: theoretical properties and practical usage of existing metrics. Sleep. 2021;44(10):zsab103. https://doi.org/10.1093/sleep/zsab103
- Foster C. Monitoring training in athletes with reference to overtraining syndrome. Med Sci Sports Exerc. 1998;30(7):1164-1168. https://doi.org/10.1097/00005768-199807000-00023 (accessed 2026-10-07). Abstract only.
- Foster C, Florhaug JA, Franklin J, Gottschall L, Hrovatin LA, Parker S, Doleshal P, Dodge C. A new approach to monitoring exercise training. J Strength Cond Res. 2001;15(1):109-115. https://doi.org/10.1519/00124278-200102000-00019
- Freehill MT, Rose MJ, McCollum KA, Agresta C, Cain SM. Game-day pitch and throw count feasibility using a single sensor to quantify workload in youth baseball players. Orthop J Sports Med. 2023;11(3):23259671231151450. https://doi.org/10.1177/23259671231151450 Read as an abstract only.
- Freitas TT, Alcaraz PE, Bishop C, Calleja-González J, Arruda AFS, Guerriero A, Reis VP, Pereira LA, Loturco I. Change of direction deficit in national team rugby union players: is there an influence of playing position? Sports. 2018;7(1):2. https://doi.org/10.3390/sports7010002
- Furlan L, Sterr A. The applicability of standard error of measurement and minimal detectable change to motor learning research: a behavioral study. Front Hum Neurosci. 2018;12:95. https://doi.org/10.3389/fnhum.2018.00095
- Gabbett TJ. The training-injury prevention paradox: should athletes be training smarter and harder? Br J Sports Med. 2016;50(5):273-280. https://doi.org/10.1136/bjsports-2015-095788
- Gabbett TJ, Hulin B, Blanch P, Chapman P, Bailey D. To couple or not to couple? For acute:chronic workload ratios and injury risk, does it really matter? Int J Sports Med. 2019;40(9):597-600. https://doi.org/10.1055/a-0955-5589
- García-Ramos A, Pestaña-Melero FL, Pérez-Castilla A, Rojas FJ, Haff GG. Mean velocity vs. mean propulsive velocity vs. peak velocity: which variable determines bench press relative load with higher reliability? J Strength Cond Res. 2018;32(5):1273-1279. https://doi.org/10.1519/JSC.0000000000001998
- García-Ramos A, Weakley J, Janicijevic D, Jukic I. Number of repetitions performed before and after reaching velocity loss thresholds: first repetition versus fastest repetition, mean velocity versus peak velocity. Int J Sports Physiol Perform. 2021;16(7):950-957. https://doi.org/10.1123/ijspp.2020-0629
- Gathercole R, Sporer B, Stellingwerff T, Sleivert G. Alternative countermovement-jump analysis to quantify acute neuromuscular fatigue. Int J Sports Physiol Perform. 2015;10(1):84-92. https://doi.org/10.1123/ijspp.2013-0413
- Gillinov S, Etiwy M, Wang R, Blackburn G, Phelan D, Gillinov AM, Houghtaling P, Javadikasgari H, Desai MY. Variable accuracy of wearable heart rate monitors during aerobic exercise. Med Sci Sports Exerc. 2017;49(8):1697-1703. https://doi.org/10.1249/MSS.0000000000001284
- Glaister M, Gissane C. Caffeine and physiological responses to submaximal exercise: a meta-analysis. Int J Sports Physiol Perform. 2018;13(4):402-411. https://doi.org/10.1123/ijspp.2017-0312
- Glaister M, Howatson G, Pattison JR, McInnes G. The reliability and validity of fatigue measures during multiple-sprint work: an issue revisited. J Strength Cond Res. 2008;22(5):1597-1601. https://doi.org/10.1519/JSC.0b013e318181ab80
- Godhe M, Bergman S, Petré H. Between-session reliability of portable isometric mid-thigh pull and countermovement jump tests in elite male ice hockey players from the Swedish Hockey League. Sports. 2025;13(12):456. https://doi.org/10.3390/sports13120456
- González-Badillo JJ, Sánchez-Medina L. Movement velocity as a measure of loading intensity in resistance training. Int J Sports Med. 2010;31(5):347-352. https://doi.org/10.1055/s-0030-1248333
- González-Badillo JJ, Yañez-García JM, Mora-Custodio R, Rodríguez-Rosell D. Velocity loss as a variable for monitoring resistance exercise. Int J Sports Med. 2017;38(3):217-225. https://doi.org/10.1055/s-0042-120324
- Google. WEEKDAY (Google Sheets). https://support.google.com/docs/answer/3092985 (accessed 2026-10-07) No DOI.
- Gregson W, Drust B, Atkinson G, Di Salvo V. Match-to-match variability of high-speed activities in premier league soccer. Int J Sports Med. 2010;31(4):237-242. https://doi.org/10.1055/s-0030-1247546
- Grgic J, Lazinica B, Pedisic Z. Test-retest reliability of the 30-15 Intermittent Fitness Test: a systematic review. J Sport Health Sci. 2021;10(4):413-418. https://doi.org/10.1016/j.jshs.2020.04.010
- Grgic J, Lazinica B, Schoenfeld BJ, Pedisic Z. Test-retest reliability of the one-repetition maximum (1RM) strength assessment: a systematic review. Sports Med Open. 2020;6(1):31. https://doi.org/10.1186/s40798-020-00260-z Read as an abstract only.
- Griffin A, Kenny IC, Comyns TM, Purtill H, Tiernan C, O'Shaughnessy E, Lyons M. Training load monitoring in team sports: a practical approach to addressing missing data. J Sports Sci. 2021;39(19):2161-2171. https://doi.org/10.1080/02640414.2021.1923205
- Gualtieri A, Rampinini E, Dello Iacono A, Beato M. High-speed running and sprinting in professional adult soccer: current thresholds definition, match demands and training strategies. A systematic review. Front Sports Act Living. 2023;5:1116293. https://doi.org/10.3389/fspor.2023.1116293
- Haddad M, Stylianides G, Djaoui L, Dellal A, Chamari K. Session-RPE method for training load monitoring: validity, ecological usefulness, and influencing factors. Front Neurosci. 2017;11:612. https://doi.org/10.3389/fnins.2017.00612
- Haff GG, Ruben RP, Lider J, Twine C, Cormie P. A comparison of methods for determining the rate of force development during isometric midthigh clean pulls. J Strength Cond Res. 2015;29(2):386-395. https://doi.org/10.1519/JSC.0000000000000705
- Halperin I, Malleron T, Har-Nir I, Androulakis-Korakakis P, Wolf M, Fisher J, Steele J. Accuracy in predicting repetitions to task failure in resistance exercise: a scoping review and exploratory meta-analysis. Sports Med. 2022;52(2):377-390. https://doi.org/10.1007/s40279-021-01559-x Read as an abstract only.
- Harman EA, Rosenstein MT, Frykman PN, Rosenstein RM. The effects of arms and countermovement on vertical jumping. Med Sci Sports Exerc. 1990;22(6):825-833. https://doi.org/10.1249/00005768-199012000-00015
- Harper DJ, Carling C, Kiely J. High-intensity acceleration and deceleration demands in elite team sports competitive match play: a systematic review and meta-analysis of observational studies. Sports Med. 2019;49(12):1923-1947. https://doi.org/10.1007/s40279-019-01170-1
- Haugen TA, Tønnessen E, Seiler SK. The difference is in the start: impact of timing and start procedure on sprint running performance. J Strength Cond Res. 2012;26(2):473-479. https://doi.org/10.1519/JSC.0b013e318226030b
- Haydar B, Al Haddad H, Ahmaidi S, Buchheit M. Assessing inter-effort recovery and change of direction abilities with the 30-15 Intermittent Fitness Test. J Sports Sci Med. 2011;10(2):346-354. No DOI. https://pmc.ncbi.nlm.nih.gov/articles/PMC3761847/ (accessed 2026-10-07)
- Healy R, Kenny IC, Harrison AJ. Reactive strength index: a poor indicator of reactive strength? Int J Sports Physiol Perform. 2018;13(6):802-809. https://doi.org/10.1123/ijspp.2017-0511
- Heishman A, Brown B, Daub B, Miller R, Freitas E, Bemben M. The influence of countermovement jump protocol on reactive strength index modified and flight time: contraction time in collegiate basketball players. Sports. 2019;7(2):37. https://doi.org/10.3390/sports7020037 (cited as Heishman et al., 2019a)
- Heishman A, Daub B, Miller R, Brown B, Freitas E, Bemben M. Countermovement jump inter-limb asymmetries in collegiate basketball players. Sports. 2019;7(5):103. https://doi.org/10.3390/sports7050103 (cited as Heishman et al., 2019b). The 0.90 ratio and its range were calculated from the typical errors in the paper's within-session and separate-day reliability tables.
- Helms ER, Cronin J, Storey A, Zourdos MC. Application of the repetitions in reserve-based rating of perceived exertion scale for resistance training. Strength Cond J. 2016;38(4):42-49. https://doi.org/10.1519/SSC.0000000000000218
- Helms ER, Storey A, Cross MR, Brown SR, Lenetsky S, Ramsay H, Dillen C, Zourdos MC. RPE and velocity relationships for the back squat, bench press, and deadlift in powerlifters. J Strength Cond Res. 2017;31(2):292-297. https://doi.org/10.1519/JSC.0000000000001517 Read as an abstract only.
- Herzog W, Nigg BM, Read LJ, Olsson E. Asymmetries in ground reaction force patterns in normal human gait. Med Sci Sports Exerc. 1989;21(1):110-114. https://doi.org/10.1249/00005768-198902000-00020
- Hooper SL, Mackinnon LT. Monitoring overtraining in athletes. Recommendations. Sports Med. 1995;20(5):321-327. https://doi.org/10.2165/00007256-199520050-00003 Not read: neither the full text nor an abstract was available. Scale details come from later studies that cite it.
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02). No DOI. The skills use only its error formula, not its magnitude-based inference.
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. Med Sci Sports Exerc. 2009;41(1):3-13. https://doi.org/10.1249/MSS.0b013e31818cb278
- Hough PA, North JS, Patterson SD, Pedlar CR. Monitoring athletes sleep: a survey of current trends amongst practitioners. J Sport Exerc Sci. 2021;5(4):277-284. https://doi.org/10.36905/jses.2021.04.06
- Hourcade JC, Noirez P, Sidney M, Toussaint JF, Desgorces F. Effects of intensity distribution changes on performance and on training loads quantification. Biol Sport. 2018;35(1):67-74. https://doi.org/10.5114/biolsport.2018.70753
- Howarth DJ, Cohen DD, McLean BD, Coutts AJ. Establishing the noise: interday ecological reliability of countermovement jump variables in professional rugby union players. J Strength Cond Res. 2022;36(11):3159-3166. https://doi.org/10.1519/JSC.0000000000004037
- Hoyne ZG, Cripps AJ, Mosler AB, Joyce C, Chivers PT, Chipchase R, Murphy MC. Self-reported throwing volumes are not a valid tool for monitoring throwing loads in elite Australian cricket players: an observational cohort study. J Sci Med Sport. 2022;25(10):845-849. https://doi.org/10.1016/j.jsams.2022.06.008 Read as an abstract only.
- Huebner A, Lever JR, Clark TW, Suchomel TJ, Metoyer CJ, Hauenstein JD, Wagle JP. Novel use of generalizability theory to optimize countermovement jump data collection. Sports. 2025;13(3):85. https://doi.org/10.3390/sports13030085
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
- Jones CM, Griffiths PC, Mellalieu SD. Training load and fatigue marker associations with injury and illness: a systematic review of longitudinal studies. Sports Med. 2017;47(5):943-974. https://doi.org/10.1007/s40279-016-0619-5 (accessed 2026-10-07)
- Jovanović M, Vescovi JD. {shorts}: An R package for modeling short sprints. Int J Strength Cond. 2022;2(1). https://doi.org/10.47206/ijsc.v2i1.74
- Juillard E, Douchet T, Paizis C, Babault N. Impact of the menstrual cycle on physical performance and subjective ratings in elite academy women soccer players. Sports. 2024;12(1):16. https://doi.org/10.3390/sports12010016
- Karjalainen J, Viitasalo M. Fever and cardiac rhythm. Arch Intern Med. 1986;146(6):1169-1171. https://doi.org/10.1001/archinte.1986.00360180179026
- Karvonen MJ, Kentala E, Mustala O. The effects of training on heart rate; a longitudinal study. Ann Med Exp Biol Fenn. 1957;35(3):307-315. PMID: 13470504. No DOI.
- Kellmann M, Kallus KW, editors. The Recovery-Stress Questionnaires: A User Manual. 1st ed. Routledge; 2025. Book, not peer reviewed, no DOI. https://routledge.com/The-Recovery-Stress-Questionnaires-A-User-Manual/Kellmann-Kallus/p/book/9781032620503 (accessed 2026-10-07)
- Kenttä G, Hassmén P. Overtraining and recovery. A conceptual model. Sports Med. 1998;26(1):1-16. https://doi.org/10.2165/00007256-199826010-00001 Read as an abstract only.
- Kraska JM, Ramsey MW, Haff GG, Fethke N, Sands WA, Stone ME, Stone MH. Relationship between strength characteristics and unweighted and weighted vertical jump height. Int J Sports Physiol Perform. 2009;4(4):461-473. https://doi.org/10.1123/ijspp.4.4.461
- Krustrup P, Mohr M, Amstrup T, Rysgaard T, Johansen J, Steensberg A, Pedersen PK, Bangsbo J. The Yo-Yo intermittent recovery test: physiological response, reliability, and validity. Med Sci Sports Exerc. 2003;35(4):697-705. https://doi.org/10.1249/01.MSS.0000058441.94520.32
- Krustrup P, Mohr M, Nybo L, Jensen JM, Nielsen JJ, Bangsbo J. The Yo-Yo IR2 test: physiological response, reliability, and application to elite soccer. Med Sci Sports Exerc. 2006;38(9):1666-1673. https://doi.org/10.1249/01.mss.0000227538.20799.08
- Kyprianou E, Lolli L, Al Haddad H, Di Salvo V, Varley MC, Mendez-Villanueva A, Gregson W, Weston M. A novel approach to assessing validity in sports performance research: integrating expert practitioner opinion into the statistical analysis. Sci Med Footb. 2019;3(4):333-338. https://doi.org/10.1080/24733938.2019.1617433 Read as an abstract only.
- Laurent CM, Green JM, Bishop PA, Sjökvist J, Schumacker RE, Richardson MT, Curtner-Smith M. A practical approach to monitoring recovery: development of a perceived recovery status scale. J Strength Cond Res. 2011;25(3):620-628. https://doi.org/10.1519/jsc.0b013e3181c69ec6 Read as an abstract only.
- LeSuer DA, McCormick JH, Mayhew JL, Wasserstein RL, Arnold MD. The accuracy of prediction equations for estimating 1-RM performance in the bench press, squat, and deadlift. J Strength Cond Res. 1997;11(4):211-213. https://doi.org/10.1519/00124278-199711000-00001 Read as an abstract only.
- Linke D, Link D, Lames M. Validation of electronic performance and tracking systems EPTS under field conditions. PLoS One. 2018;13(7):e0199519. https://doi.org/10.1371/journal.pone.0199519
- Linthorne NP. Analysis of standing vertical jumps using a force platform. Am J Phys. 2001;69(11):1198-1204. https://doi.org/10.1119/1.1397460
- Lipinski D, Whelan JP, Stiglets BE, Andersland MD, Ginley MK, Pfund RA. The influence of winning and losing gambling experience on mood state and alcohol cravings. J Gambl Stud. 2025;41(2):841-855. https://doi.org/10.1007/s10899-024-10367-7
- Lizzio VA, Cross AG, Guo EW, Makhni EC. Using wearable technology to evaluate the kinetics and kinematics of the overhead throwing motion in baseball players. Arthrosc Tech. 2020;9(9):e1429-e1431. https://doi.org/10.1016/j.eats.2020.06.003
- Lolli L, Batterham AM, Hawkins R, Kelly DM, Strudwick AJ, Thorpe R, Gregson W, Atkinson G. Mathematical coupling causes spurious correlation within the conventional acute-to-chronic workload ratio calculations. Br J Sports Med. 2019;53(15):921-922. https://doi.org/10.1136/bjsports-2017-098110. Editorial, first published online 2017-11-03.
- Lucia A, Hoyos J, Santalla A, Earnest C, Chicharro JL. Tour de France versus Vuelta a España: which is harder? Med Sci Sports Exerc. 2003;35(5):872-878. https://doi.org/10.1249/01.MSS.0000064999.82036.B4
- Lundquist M, Nelson MJ, Debenedictis T, Gollan S, Fuller JT, Larwood T, Bellenger CR. Set distance time trials for predicting maximal aerobic speed in female Australian Rules Footballers. J Sci Med Sport. 2021;24(4):391-396. https://doi.org/10.1016/j.jsams.2020.10.002
- Macarilla CT, Sautter NM, Robinson ZP, Juber MC, Hickmott LM, Cerminaro RM, Benitez B, Carzoli JP, Bazyler CD, Zoeller RF, Whitehurst M, Zourdos MC. Accuracy of predicting one-repetition maximum from submaximal velocity in the barbell back squat and bench press. J Hum Kinet. 2022;82:201-212. https://doi.org/10.2478/hukin-2022-0046
- Maffiuletti NA, Aagaard P, Blazevich AJ, Folland J, Tillin N, Duchateau J. Rate of force development: physiological and methodological considerations. Eur J Appl Physiol. 2016;116(6):1091-1116. https://doi.org/10.1007/s00421-016-3346-6
- Malone JJ, Lovell R, Varley MC, Coutts AJ. Unpacking the black box: applications and considerations for using GPS devices in sport. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-18-S2-26. https://doi.org/10.1123/ijspp.2016-0236
- Manzi V, Castagna C, Padua E, Lombardo M, D’Ottavio S, Massaro M, Volterrani M, Iellamo F. Dose-response relationship of autonomic nervous system responses to individualized training impulse in marathon runners. Am J Physiol Heart Circ Physiol. 2009;296(6):H1733-H1740. https://doi.org/10.1152/ajpheart.00054.2009
- Martín-García A, Gómez Díaz A, Bradley PS, Morera F, Casamichana D. Quantification of a professional football team's external load using a microcycle structure. J Strength Cond Res. 2018;32(12):3511-3518. https://doi.org/10.1519/JSC.0000000000002816
- Marylebone Cricket Club. The Laws of Cricket. Law 17: The over. Governing body rules, not peer reviewed, no DOI. https://lawsofcricket.lords.org/laws-of-cricket/the-over-scoring-runs-dead-ball-and-extras/the-over (accessed 2026-10-07)
- McBride JM, McCaulley GO, Cormie P, Nuzzo JL, Cavill MJ, Triplett NT. Comparison of methods to quantify volume during resistance exercise. J Strength Cond Res. 2009;23(1):106-110. https://doi.org/10.1519/JSC.0b013e31818efdfe Read as an abstract only.
- McGuigan MR, Doyle TL, Newton M, Edwards DJ, Nimphius S, Newton RU. Eccentric utilization ratio: effect of sport and phase of training. J Strength Cond Res. 2006;20(4):992-995. https://doi.org/10.1519/R-19165.1 Read as an abstract only.
- McMahon JJ, Jones PA, Dos'Santos T, Comfort P. Influence of dynamic strength index on countermovement jump force-, power-, velocity-, and displacement-time curves. Sports. 2017;5(4):72. https://doi.org/10.3390/sports5040072
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength Cond J. 2018;40(4):96-106. https://doi.org/10.1519/SSC.0000000000000375 (cited as McMahon et al., 2018a)
- McMahon JJ, Jones PA, Suchomel TJ, Lake J, Comfort P. Influence of the reactive strength index modified on force- and power-time curves. Int J Sports Physiol Perform. 2018;13(2):220-227. https://doi.org/10.1123/ijspp.2017-0056 (cited as McMahon et al., 2018b)
- Merrigan JJ, Stone JD, Galster SM, Hagen JA. Analyzing force-time curves: comparison of commercially available automated software and custom MATLAB analyses. J Strength Cond Res. 2022;36(9):2387-2402. https://doi.org/10.1519/JSC.0000000000004275
- Microsoft. WEEKDAY function (DAX), WEEKDAY function (Excel), and DATESINPERIOD function (DAX). https://learn.microsoft.com/en-us/dax/weekday-function-dax, https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a, and https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax (accessed 2026-10-07). No DOI.
- Morán-Navarro R, Martínez-Cava A, Sánchez-Medina L, Mora-Rodríguez R, González-Badillo JJ, Pallarés JG. Movement velocity as a measure of level of effort during resistance exercise. J Strength Cond Res. 2019;33(6):1496-1504. https://doi.org/10.1519/JSC.0000000000002017
- Nes BM, Janszky I, Wisløff U, Støylen A, Karlsen T. Age-predicted maximal heart rate in healthy subjects: the HUNT fitness study. Scand J Med Sci Sports. 2013;23(6):697-704. https://doi.org/10.1111/j.1600-0838.2012.01445.x
- National Institute of Standards and Technology. Dataplot reference manual: prediction limits. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/predlimi.htm (accessed 2026-10-02). No DOI.
- Nimphius S, Callaghan SJ, Spiteri T, Lockie RG. Change of direction deficit: a more isolated measure of change of direction performance than total 505 time. J Strength Cond Res. 2016;30(11):3024-3032. https://doi.org/10.1519/JSC.0000000000001421
- Nuzzo JL, Pinto MD, Nosaka K, Steele J. Maximal number of repetitions at percentages of the one repetition maximum: a meta-regression and moderator analysis of sex, age, training status, and exercise. Sports Med. 2024;54(2):303-321. https://doi.org/10.1007/s40279-023-01937-7
- Oberhofer K, Erni R, Sayers M, Huber D, Lüthy F, Lorenzetti S. Validation of a smartwatch-based workout analysis application in exercise recognition, repetition count and prediction of 1RM in the strength training-specific setting. Sports (Basel). 2021;9(9):118. https://doi.org/10.3390/sports9090118
- Oliver JL. Is a fatigue index a worthwhile measure of repeated sprint ability? J Sci Med Sport. 2009;12(1):20-23. https://doi.org/10.1016/j.jsams.2007.10.010
- Opar DA, Piatkowski T, Williams MD, Shield AJ. A novel device using the Nordic hamstring exercise to assess eccentric knee flexor strength: a reliability and retrospective injury study. J Orthop Sports Phys Ther. 2013;43(9):636-640. https://doi.org/10.2519/jospt.2013.4837
- Opar DA, Williams MD, Timmins RG, Hickey J, Duhig SJ, Shield AJ. Eccentric hamstring strength and hamstring injury risk in Australian footballers. Med Sci Sports Exerc. 2015;47(4):857-865. https://doi.org/10.1249/MSS.0000000000000465
- Opar DA, Timmins RG, Behan FP, Hickey JT, van Dyk N, Price K, Maniar N. Is pre-season eccentric strength testing during the Nordic hamstring exercise associated with future hamstring strain injury? A systematic review and meta-analysis. Sports Med. 2021;51(9):1935-1945. https://doi.org/10.1007/s40279-021-01474-1. Read in abstract form only.
- Owen NJ, Watkins J, Kilduff LP, Bevan HR, Bennett MA. Development of a criterion method to determine peak mechanical power output in a countermovement jump. J Strength Cond Res. 2014;28(6):1552-1558. https://doi.org/10.1519/JSC.0000000000000311
- Pareja-Blanco F, Rodríguez-Rosell D, Sánchez-Medina L, Sanchis-Moysi J, Dorado C, Mora-Custodio R, Yáñez-García JM, Morales-Alamo D, Pérez-Suárez I, Calbet JAL, González-Badillo JJ. Effects of velocity loss during resistance training on athletic performance, strength gains and muscle adaptations. Scand J Med Sci Sports. 2017;27(7):724-735. https://doi.org/10.1111/sms.12678
- Parkinson AO, Apps CL, Morris JG, Barnett CT, Lewis MGC. The calculation, thresholds and reporting of inter-limb strength asymmetry: a systematic review. J Sports Sci Med. 2021;20(4):594-617. https://doi.org/10.52082/jssm.2021.594
- Paulsen KM, McDermott BP, Myers AJ, Gray M, Lo WJ, Ganio MS. Reliability and validity of the 30-15 Intermittent Field Test with and without a soccer ball. Res Q Exerc Sport. 2023;94(4):1001-1010. https://doi.org/10.1080/02701367.2022.2098230
- Paulson TA, Mason B, Rhodes J, Goosey-Tolfrey VL. Individualized internal and external training load relationships in elite wheelchair rugby players. Front Physiol. 2015;6:388. https://doi.org/10.3389/fphys.2015.00388
- Pearson M, García-Ramos A, Morrison M, Ramirez-Lopez C, Dalton-Barron N, Weakley J. Velocity loss thresholds reliably control kinetic and kinematic outputs during free weight resistance training. Int J Environ Res Public Health. 2020;17(18):6509. https://doi.org/10.3390/ijerph17186509
- Perazzetti A, Kaçurri A, Gjaka M, Pernigoni M, Lupo C, Tessitore A. Impact of a congested match schedule on internal load, recovery, well-being, and enjoyment in U16 youth water polo players. Sports. 2025;13(9):286. https://doi.org/10.3390/sports13090286
- Pérez-Castilla A, Suzovic D, Domanovic A, Fernandes JFT, García-Ramos A. Validity of different velocity-based methods and repetitions-to-failure equations for predicting the 1 repetition maximum during 2 upper-body pulling exercises. J Strength Cond Res. 2021;35(7):1800-1808. https://doi.org/10.1519/JSC.0000000000003076 Read as an abstract only.
- Pérez-Chao EA, Portes R, Gómez MÁ, Parmar N, Lorenzo A, Jiménez-Sáiz SL. A narrative review of the most demanding scenarios in basketball: current trends and future directions. J Hum Kinet. 2023;89:231-245. https://doi.org/10.5114/jhk/170838
- Pino-Mulero V, Soriano MA, Giuliano F, González-García J. Effects of a priming session with heavy sled pushes on neuromuscular performance and perceived recovery in soccer players: a crossover design study during competitive microcycles. Biol Sport. 2025;42(1):59-66. https://doi.org/10.5114/biolsport.2025.139082
- Plews DJ, Laursen PB, Kilding AE, Buchheit M. Heart rate variability in elite triathletes, is variation in variability the key to effective training? A case comparison. Eur J Appl Physiol. 2012;112(11):3729-3741. https://doi.org/10.1007/s00421-012-2354-4
- Plews DJ, Laursen PB, Le Meur Y, Hausswirth C, Kilding AE, Buchheit M. Monitoring training with heart rate-variability: how much compliance is needed for valid assessment? Int J Sports Physiol Perform. 2014;9(5):783-790. https://doi.org/10.1123/ijspp.2013-0455 Read as an abstract only.
- Plews DJ, Laursen PB, Stanley J, Kilding AE, Buchheit M. Training adaptation and heart rate variability in elite endurance athletes: opening the door to effective monitoring. Sports Med. 2013;43(9):773-781. https://doi.org/10.1007/s40279-013-0071-8
- Polar Electro Oy. Polar Training Load Pro white paper. November 12, 2019; revised March 2025. https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf (accessed 2026-10-02). No DOI. Cited as Polar, 2025.
- Polar Electro Oy. Polar Team Pro API reference, sport profile zone fields `lower_limit` (inclusive) and `higher_limit` (exclusive). https://www.polar.com/teampro-api/ (accessed 2026-10-02). No DOI.
- Pustina AA, Sato K, Liu C, Kavanaugh AA, Sams ML, Liu J, Uptmore KD, Stone MH. Establishing a duration standard for the calculation of session rating of perceived exertion in NCAA Division I men's soccer. J Trainol. 2017;6(1):26-30. https://doi.org/10.17338/trainology.6.1_26
- Rago V, Brito J, Figueiredo P, Krustrup P, Rebelo A. Relationship between external load and perceptual responses to training in professional football: effects of quantification method. Sports. 2019;7(3):68. https://doi.org/10.3390/sports7030068
- Rago V, Muschinsky A, Deylami K, Vigh-Larsen JF, Mohr M. Game demands of a professional ice hockey team with special emphasis on fatigue development and playing position. J Hum Kinet. 2022;84:195-205. https://doi.org/10.2478/hukin-2022-000078
- Rave G, Fortrat JO, Dawson B, Carre F, Dupont G, Saeidi A, Boullosa D, Zouhal H. Heart rate recovery and heart rate variability: use and relevance in European professional soccer. Int J Perform Anal Sport. 2018;18(1):168-183. https://doi.org/10.1080/24748668.2018.1460053 Read as an abstract only.
- Reardon C, Tobin DP, Delahunt E. Application of individualized speed thresholds to interpret position specific running demands in elite professional rugby union: a GPS study. PLoS One. 2015;10(7):e0133410. https://doi.org/10.1371/journal.pone.0133410
- Reynolds JM, Gordon TJ, Robergs RA. Prediction of one repetition maximum strength from multiple repetition maximum testing and anthropometry. J Strength Cond Res. 2006;20(3):584-592. https://doi.org/10.1519/R-15304.1 Read as an abstract only.
- Ripley NJ, Fahey J, Guppy S, Comfort P. Comparisons between different methods of calculating dynamic strength index: effect on training recommendations. PLoS One. 2025;20(9):e0331519. https://doi.org/10.1371/journal.pone.0331519
- Roberts TD, Smith RW, Arnett JE, Ortega DG, Schmidt RJ, Housh TJ. Cross-validation of equations for estimating 1 repetition maximum from repetitions to failure for the bench press and leg extension. J Strength Cond Res. 2025;39(2):e96-e105. https://doi.org/10.1519/JSC.0000000000004987 Read as an abstract only.
- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-73-S2-79. https://doi.org/10.1123/ijspp.2016-0541
- Rodríguez-Marroyo JA, González B, Foster C, Carballo-Leyenda AB, Villa JG. Effect of the cooldown type on session rating of perceived exertion. Int J Sports Physiol Perform. 2021;16(4):573-577. https://doi.org/10.1123/ijspp.2020-0225
- Roso-Moliner A, Lozano D, Nobari H, Bishop C, Carton-Llorente A, Mainer-Pardos E. Horizontal jump asymmetries are associated with reduced range of motion and vertical jump performance in female soccer players. BMC Sports Sci Med Rehabil. 2023;15:80. https://doi.org/10.1186/s13102-023-00697-1
- Samozino P, Rabita G, Dorel S, Slawinski J, Peyrot N, Saez de Villarreal E, Morin JB. A simple method for measuring power, force, velocity properties, and mechanical effectiveness in sprint running. Scand J Med Sci Sports. 2016;26(6):648-658. https://doi.org/10.1111/sms.12490
- Sanchez-Medina L, Perez CE, Gonzalez-Badillo JJ. Importance of the propulsive phase in strength assessment. Int J Sports Med. 2010;31(2):123-129. https://doi.org/10.1055/s-0029-1242815
- Sánchez-Medina L, González-Badillo JJ. Velocity loss as an indicator of neuromuscular fatigue during resistance training. Med Sci Sports Exerc. 2011;43(9):1725-1734. https://doi.org/10.1249/MSS.0b013e318213f880
- Sandford GN, Allen SV, Kilding AE, Ross A, Laursen PB. Anaerobic speed reserve: a key component of elite male 800-m running. Int J Sports Physiol Perform. 2019;14(4):501-508. https://doi.org/10.1123/ijspp.2018-0163
- Sandford GN, Laursen PB, Buchheit M. Anaerobic speed/power reserve and sport performance: scientific basis, current applications and future directions. Sports Med. 2021;51(10):2017-2028. https://doi.org/10.1007/s40279-021-01523-9
- Sandford GN, Rogers SA, Sharma AP, Kilding AE, Ross A, Laursen PB. Implementing anaerobic speed reserve testing in the field: validation of vVO2max prediction from 1500-m race performance in elite middle-distance runners. Int J Sports Physiol Perform. 2019;14(8):1147-1150. https://doi.org/10.1123/ijspp.2018-0553
- Sands WA, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone MH. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. Br J Sports Med. 2016;50(5):281-291. https://doi.org/10.1136/bjsports-2015-094758
- Scott MTU, Scott TJ, Kelly VG. The validity and reliability of global positioning systems in team sport: a brief review. J Strength Cond Res. 2016;30(5):1470-1490. https://doi.org/10.1519/JSC.0000000000001221
- Selmi O, Rahmoune MA, Bouassida A, Marsigliante S, Muscella A. Comparative analysis of morning and evening training on performance and well-being in elite soccer players. Physiol Rep. 2025;13(15):e70510. https://doi.org/10.14814/phy2.70510
- Shah S, Collins K, Macgregor LJ. The influence of weekly sprint volume and maximal velocity exposures on eccentric hamstring strength in professional football players. Sports. 2022;10(8):125. https://doi.org/10.3390/sports10080125 Cited for its counting method only.
- Shearer DA, Kilduff LP, Finn C, Jones RM, Bracken RM, Mellalieu SD, Owen N, Crewther BT, Cook CJ. Measuring recovery in elite rugby players: the Brief Assessment of Mood, endocrine changes, and power. Res Q Exerc Sport. 2015;86(4):379-386. https://doi.org/10.1080/02701367.2015.1066927 Read as an abstract only.
- Sheppard JM, Doyle TL. Increasing compliance to instructions in the squat jump. J Strength Cond Res. 2008;22(2):648-651. https://doi.org/10.1519/JSC.0b013e31816602d4 Read as an abstract only.
- Shrier I. Strategic Assessment of Risk and Risk Tolerance (StARRT) framework for return-to-play decision-making. Br J Sports Med. 2015;49(20):1311-1315. https://doi.org/10.1136/bjsports-2014-094569
- Shushan T, McLaren SJ, Buchheit M, Scott TJ, Barrett S, Lovell R. Submaximal fitness tests in team sports: a theoretical framework for evaluating physiological state. Sports Med. 2022;52(11):2605-2626. https://doi.org/10.1007/s40279-022-01712-0
- Shushan T, Norris D, McLaren SJ, Buchheit M, Scott TJ, Barrett S, Dello Iacono A, Lovell R. A worldwide survey on the practices and perceptions of submaximal fitness tests in team sports. Int J Sports Physiol Perform. 2023;18(7):765-779. https://doi.org/10.1123/ijspp.2023-0004 Read as an abstract only.
- Silva RM, Clemente FM, González-Fernández FT, Nobari H, Oliveira R, Silva AF, Cancela-Carral JM. Relationships between internal training intensity and well-being changes in youth football players. Healthcare. 2022;10(10):1814. https://doi.org/10.3390/healthcare10101814
- Skazalski C, Whiteley R, Hansen C, Bahr R. A valid and reliable method to measure jump-specific training and competition load in elite volleyball players. Scand J Med Sci Sports. 2018;28(5):1578-1585. https://doi.org/10.1111/sms.13052 Read as an abstract only.
- Smith K, Wright MD, Chesterton P, Taylor JM. Estimating maximal aerobic speed in academy soccer players: a comparison between time trial methods and the 30-15 Intermittent Fitness Test. Eur J Sport Sci. 2025;25(6):e12315. https://doi.org/10.1002/ejsc.12315
- Sole CJ, Suchomel TJ, Stone MH. Preliminary scale of reference values for evaluating reactive strength index-modified in male and female NCAA Division I athletes. Sports. 2018;6(4):133. https://doi.org/10.3390/sports6040133
- Song MK, Lin FC, Ward SE, Fine JP. Composite variables: when and how. Nurs Res. 2013;62(1):45-49. https://doi.org/10.1097/NNR.0b013e3182741948
- Sperlich B, Matzka M, Holmberg HC. The proportional distribution of training by elite endurance athletes at different intensities during different phases of the season. Front Sports Act Living. 2023;5:1258585. https://doi.org/10.3389/fspor.2023.1258585
- Stone JD, Merrigan JJ, Ramadan J, Brown RS, Cheng GT, Hornsby WG, Smith H, Galster SM, Hagen JA. Simplifying external load data in NCAA Division-I men's basketball competitions: a principal component analysis. Front Sports Act Living. 2022;4:795897. https://doi.org/10.3389/fspor.2022.795897
- Swain DP, Leutholtz BC, King ME, Haas LA, Branch JD. Relationship between % heart rate reserve and % VO2 reserve in treadmill exercise. Med Sci Sports Exerc. 1998;30(2):318-321. https://doi.org/10.1097/00005768-199802000-00022
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Tableau. Date functions, Join your data, and Table calculations. https://help.tableau.com/current/pro/desktop/en-us/functions_functions_date.htm, https://help.tableau.com/current/pro/desktop/en-us/joining_tables.htm, and https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm (accessed 2026-10-07) No DOI.
- Tanaka H, Monahan KD, Seals DR. Age-predicted maximal heart rate revisited. J Am Coll Cardiol. 2001;37(1):153-156. https://doi.org/10.1016/S0735-1097(00)01054-8
- Taylor KL, Chapman DW, Cronin JB, Newton MJ, Gill N. Fatigue monitoring in high performance sport: a survey of current trends. J Aust Strength Cond. 2012;20(1):12-23. No DOI. https://lida.sport-iat.de/twm/Record/4024682 (accessed 2026-10-07) Read as an abstract only.
- Thomas C, Dos'Santos T, Comfort P, Jones PA. Between-session reliability of common strength- and power-related measures in adolescent athletes. Sports. 2017;5(1):15. https://doi.org/10.3390/sports5010015
- Thomas C, Jones PA, Comfort P. Reliability of the dynamic strength index in college athletes. Int J Sports Physiol Perform. 2015;10(5):542-545. https://doi.org/10.1123/ijspp.2014-0255 Read as an abstract only.
- Thornton HR, Nelson AR, Delaney JA, Serpiello FR, Duthie GM. Interunit reliability and effect of data-processing methods of global positioning systems. Int J Sports Physiol Perform. 2019;14(4):432-438. https://doi.org/10.1123/ijspp.2018-0273 Read as an abstract only, 2026-10-05. The full text is paywalled.
- Thulin M. The cost of using exact confidence intervals for a binomial proportion. Electronic Journal of Statistics. 2014;8(1):817-840. https://doi.org/10.1214/14-EJS909
- Timmins RG, Bourne MN, Shield AJ, Williams MD, Lorenzen C, Opar DA. Short biceps femoris fascicles and eccentric knee flexor weakness increase the risk of hamstring injury in elite football (soccer): a prospective cohort study. Br J Sports Med. 2016;50(24):1524-1535. https://doi.org/10.1136/bjsports-2015-095362
- Tomoto T, Tarumi T, Sugawara J. Associations among dynamic cerebral autoregulation, baroreflex sensitivity, and carotid distensibility in young healthy adults: insight from endurance training. Eur J Appl Physiol. 2026;126(6):3201-3220. https://doi.org/10.1007/s00421-026-06155-3
- Treff G, Winkert K, Sareban M, Steinacker JM, Sperlich B. The polarization-index: a simple calculation to distinguish polarized from non-polarized training intensity distributions. Front Physiol. 2019;10:707. https://doi.org/10.3389/fphys.2019.00707
- Ulmer JG, Tomkinson GR, Short S, Short M, Fitzgerald JS. Test-retest reliability of TRIMP in collegiate ice hockey players. Biol Sport. 2019;36(2):191-194. https://doi.org/10.5114/biolsport.2019.84670
- Vachon A, Berryman N, Mujika I, Paquet JB, Arvisais D, Bosquet L. Effects of tapering on neuromuscular and metabolic fitness in team sports: a systematic review and meta-analysis. Eur J Sport Sci. 2021;21(3):300-311. https://doi.org/10.1080/17461391.2020.1736183 Read as an abstract only.
- VALD. ForceDecks Technical Glossary V2.0. March 2024. https://support.vald.com/hc/en-au/article_attachments/31552911571353 (accessed 2026-10-02). No DOI.
- van Dyk N, Bahr R, Burnett AF, Whiteley R, Bakken A, Mosler A, Farooq A, Witvrouw E. A comprehensive strength testing protocol offers no clinical value in predicting risk of hamstring injury: a prospective cohort study of 413 professional football players. Br J Sports Med. 2017;51(23):1695-1702. https://doi.org/10.1136/bjsports-2017-097754
- Van Iterson EH, Fitzgerald JS, Dietz CC, Snyder EM, Peterson BJ. Reliability of triaxial accelerometry for measuring load in men's collegiate ice hockey. J Strength Cond Res. 2017;31(5):1305-1312. https://doi.org/10.1519/JSC.0000000000001611
- Varley MC, Elias GP, Aughey RJ. Current match-analysis techniques' underestimation of intense periods of high-velocity running. Int J Sports Physiol Perform. 2012;7(2):183-185. https://doi.org/10.1123/ijspp.7.2.183 (cited as Varley et al., 2012a)
- Varley MC, Fairweather IH, Aughey RJ. Validity and reliability of GPS for measuring instantaneous velocity during acceleration, deceleration, and constant motion. J Sports Sci. 2012;30(2):121-127. https://doi.org/10.1080/02640414.2011.627941 (cited as Varley et al., 2012b)
- Varley MC, Gabbett T, Aughey RJ. Activity profiles of professional soccer, rugby league and Australian football match play. J Sports Sci. 2014;32(20):1858-1866. https://doi.org/10.1080/02640414.2013.823227
- Varley MC, Jaspers A, Helsen WF, Malone JJ. Methodological considerations when quantifying high-intensity efforts in team sport using global positioning system technology. Int J Sports Physiol Perform. 2017;12(8):1059-1068. https://doi.org/10.1123/ijspp.2016-0534
- Vaverka F, Jandačka D, Zahradník D, Uchytil J, Farana R, Supej M, Vodičar J. Effect of an arm swing on countermovement vertical jump performance in elite volleyball players. J Hum Kinet. 2016;53:41-50. https://doi.org/10.1515/hukin-2016-0009
- Vescovi JD, Jovanović M. Sprint mechanical characteristics of female soccer players: a retrospective pilot study to examine a novel approach for correction of timing gate starts. Front Sports Act Living. 2021;3:629694. https://doi.org/10.3389/fspor.2021.629694
- Wahl EP, Pidgeon TS, Richard MJ. Youth baseball pitch counts vastly underestimate high-effort throws throughout a season. J Pediatr Orthop. 2020;40(7):e609-e615. https://doi.org/10.1097/BPO.0000000000001520 Read as an abstract only.
- Walsh NP, Halson SL, Sargent C, et al. Sleep and the athlete: narrative review and 2021 expert consensus recommendations. Br J Sports Med. 2021;55(7):356-368. https://doi.org/10.1136/bjsports-2020-102025 Read as an abstract only.
- Wang C, Vargas JT, Stokes T, Steele R, Shrier I. Analyzing activity and injury: lessons learned from the acute:chronic workload ratio. Sports Med. 2020;50(7):1243-1254. https://doi.org/10.1007/s40279-020-01280-1
- Washif JA, James C, Pagaduan J, Lim J, Lum D, Raja Azidin RMF, Mujika I, Beaven CM. Current periodization, testing, and monitoring practices of strength and conditioning coaches. Int J Sports Physiol Perform. 2025;20(9):1239-1252. https://doi.org/10.1123/ijspp.2025-0051 Read as an abstract only.
- Wasserstein RL, Lazar NA. The ASA statement on p-values: context, process, and purpose. Am Stat. 2016;70(2):129-133. https://doi.org/10.1080/00031305.2016.1154108
- Weakley J, Mann B, Banyard H, McLaren S, Scott T, Garcia-Ramos A. Velocity-based training: from theory to application. Strength Cond J. 2021;43(2):31-49. https://doi.org/10.1519/SSC.0000000000000560 (cited as Weakley et al., 2021a)
- Weakley J, Morrison M, García-Ramos A, Johnston R, James L, Cole MH. The validity and reliability of commercially available resistance training monitoring devices: a systematic review. Sports Med. 2021;51(3):443-502. https://doi.org/10.1007/s40279-020-01382-w (cited as Weakley et al., 2021b)
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. J Strength Cond Res. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- Whitehead S, Till K, Weaving D, Jones B. The use of microtechnology to quantify the peak match demands of the football codes: a systematic review. Sports Med. 2018;48(11):2549-2575. https://doi.org/10.1007/s40279-018-0965-6
- Wiesinger HP, Gressenbauer C, Kösters A, Scharinger M, Müller E. Device and method matter: a critical evaluation of eccentric hamstring muscle strength assessments. Scand J Med Sci Sports. 2020;30(2):217-226. https://doi.org/10.1111/sms.13569
- Williams S, West S, Cross MJ, Stokes KA. Better way to determine the acute:chronic workload ratio? Br J Sports Med. 2017;51(3):209-210. https://doi.org/10.1136/bjsports-2016-096589. Accepted manuscript: https://purehost.bath.ac.uk/ws/files/147466466/BJSM_correspondence_alternative_to_rolling_averages_r1.pdf (accessed 2026-10-02)
- Windt J, Gabbett TJ. Is it all for naught? What does mathematical coupling mean for acute:chronic workload ratios? Br J Sports Med. 2019;53(16):988-990. https://doi.org/10.1136/bjsports-2017-098925
- Winwood PW, Keogh JWL, Travis SK, Pritchard HJ. The tapering practices of competitive weightlifters. J Strength Cond Res. 2023;37(4):829-839. https://doi.org/10.1519/jsc.0000000000004324 Read as an abstract only.
- Yamashita N, Sato D, Mishima T. Jump height ingenerated by countermovement and arm swing better correlates with proagility shuttle run tests but not with change of direction deficits in collegiate female athletes. J Sports Med Phys Fitness. 2024;64(8):749-757. https://doi.org/10.23736/S0022-4707.24.15691-5
- Zifchock RA, Davis I, Higginson J, Royer T. The symmetry angle: a novel, robust method of quantifying asymmetry. Gait Posture. 2008;27(4):622-627. https://doi.org/10.1016/j.gaitpost.2007.08.006
- Zourdos MC, Klemp A, Dolan C, Quiles JM, Schau KA, Jo E, Helms E, Esgro B, Duncan S, Garcia Merino S, Blanco R. Novel resistance training-specific rating of perceived exertion scale measuring repetitions in reserve. J Strength Cond Res. 2016;30(1):267-275. https://doi.org/10.1519/JSC.0000000000001049 Read as an abstract only.
