# Typical error of measurement

Last checked: 2026-10-02

## What it measures

Typical error (TE) is the noise in a test: how much one athlete's score moves between repeated tests when nothing real has changed (Hopkins, 2000).

Typical error is also called the standard error of measurement (SEM). Both names mean the standard deviation of one athlete's repeated measurements (Hopkins, 2000; Weir, 2005).

## Formula

Use the difference-score method for two trials. This is the default:

```text
diff_i = trial2_i − trial1_i
TE     = SD(diff) / √2
CV%    = 100 × TE / grand mean
```

Define every term in the formula:

- `diff_i`: the change for athlete `i` between trial 1 and trial 2, in the units of the measure
- `SD(diff)`: the sample standard deviation of the difference scores across athletes, in the units of the measure
- `√2`: the square root of 2. Each difference holds the error of two tests. Its variance is 2 × TE² (Hopkins, 2000; Swinton et al., 2018).
- `TE`: typical error, in the units of the measure
- `grand mean`: the mean of all values from both trials, in the units of the measure
- `CV%`: the coefficient of variation. It is the typical error as a percent of the mean (Hopkins, 2000; Swinton et al., 2018).

Use these variants when they fit the data:

- **Log variant for CV%.** Use it when athletes with larger values show larger errors. Take `100 × ln(value)` for each trial, then compute TE on those values. That TE is close to the CV% when it is under 5%. When it is larger, use `CV% = 100 × (exp(TE_log / 100) − 1)` (Hopkins, 2000; Atkinson & Nevill, 1998).
- **Three or more trials, two-way model.** Use the residual error from a model with athletes and trials as effects: the square root of the error mean square, `TE = √MSE`. This is the preferred method (Hopkins, 2000; Weir, 2005).
- **Three or more trials, pooled within-athlete SD.** Compute each athlete's variance across the trials, average the variances, then take the square root. This equals a one-way ANOVA. It counts changes in the trial means as error, so it reads high when there is learning. Average the variances, not the SDs. Averaging SDs underestimates TE (Hopkins, 2000).
- **Three or more trials, consecutive pairs.** Compute TE separately for trials 1 and 2, trials 2 and 3, and each later pair of trials. Use it to check whether TE settles after practice trials. Pool the pairs with similar TE (Hopkins, 2000).
- **From a published intraclass correlation (ICC).** `SEM = SD × √(1 − ICC)`, where `SD` is the standard deviation of all scores. This version is modestly affected by how varied the sample is. Prefer `√MSE` or the difference-score method (Weir, 2005).

## Calculate typical error

Follow these steps to calculate typical error from raw inputs:

1. Arrange one row per athlete, with columns `athlete_id`, `trial1`, and `trial2`. Both trials use the same units, such as centimeters.
2. Drop any athlete who is missing either trial.
3. Compute `diff = trial2 − trial1` for each athlete, in the units of the measure.
4. Compute the mean of `diff`. Report it as the bias, which is the systematic change between trials.
5. Compute the sample SD of `diff`, dividing by n − 1.
6. Divide that SD by √2, about 1.4142. The result is TE, in the units of the measure.
7. Compute the grand mean of all `trial1` and `trial2` values.
8. Compute `CV% = 100 × TE / grand mean`.
9. Optional: Repeat steps 3 to 6 on `100 × ln(trial)` to get `TE_log`.
10. Optional: Convert with `CV% = 100 × (exp(TE_log / 100) − 1)` to get the log CV%.

Spreadsheet version, with trial 1 in column A, trial 2 in column B, the difference in column C, and the pair mean in column D, rows 2 to 21. The difference and pair mean return a blank when either trial is blank or not a number, so TE, CV%, and bias use only athletes with both trials:

```text
Difference (C2):  =IF(COUNT(A2:B2)<2,"",B2-A2)
Pair mean (D2):   =IF(COUNT(A2:B2)<2,"",(A2+B2)/2)
TE:               =STDEV.S(C2:C21)/SQRT(2)
CV%:              =100*STDEV.S(C2:C21)/SQRT(2)/AVERAGE(D2:D21)
Bias:             =AVERAGE(C2:C21)
```

Python version:

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({"trial1": [38.2, 41.5, 35.0, 44.1, 39.7, 36.8],
                   "trial2": [39.0, 40.8, 36.1, 44.9, 38.9, 37.9]})
diff = df["trial2"] - df["trial1"]
bias = diff.mean()                            # systematic change; report it separately
te = diff.std(ddof=1) / np.sqrt(2)            # ddof=1 gives the sample SD
cv_pct = 100 * te / df[["trial1", "trial2"]].to_numpy().mean()
d_log = 100 * (np.log(df["trial2"]) - np.log(df["trial1"]))
cv_log_pct = 100 * (np.exp(d_log.std(ddof=1) / np.sqrt(2) / 100) - 1)
print(f"bias {bias:.2f}, TE {te:.2f}, CV {cv_pct:.2f} %, CV log {cv_log_pct:.2f} %")
```

### Calculate it in Power BI and Tableau

These versions follow steps 2 to 8 above. Every result uses only athletes with both trials. TE and CV% are blank with fewer than 2 such athletes.

Both versions assume one row per athlete, measure, and trial in a `measures` table, with the retest stored as `trial_number` 1 and 2 in one retest session. The session filter keeps trials from other dates out. Replace `S0101` with the retest session. For a measure taken on each side, replace `bilateral` with `left` or `right` and compute each side separately. If the retest uses two sessions, filter trial 1 and trial 2 on their two `session_id` values in place of `trial_number`.

In Power BI, use these DAX measures. The difference is a measure, shown with one athlete per row. TE, CV%, and bias are measures because they summarize all athletes:

```text
Trial 1 (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[session_id] = "S0101",
    measures[trial_number] = 1,
    measures[status] = "ok",
    measures[side] = "bilateral"
)

Trial 2 (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[session_id] = "S0101",
    measures[trial_number] = 2,
    measures[status] = "ok",
    measures[side] = "bilateral"
)

Difference (cm) =
VAR t1 = [Trial 1 (cm)]
VAR t2 = [Trial 2 (cm)]
RETURN IF ( NOT ISBLANK ( t1 ) && NOT ISBLANK ( t2 ), t2 - t1 )

TE (cm) =
VAR pairs =
    FILTER (
        ADDCOLUMNS (
            VALUES ( athletes[athlete_id] ),
            "@t1", [Trial 1 (cm)],
            "@t2", [Trial 2 (cm)]
        ),
        NOT ISBLANK ( [@t1] ) && NOT ISBLANK ( [@t2] )
    )
RETURN IF ( COUNTROWS ( pairs ) >= 2, STDEVX.S ( pairs, [@t2] - [@t1] ) / SQRT ( 2 ) )

CV (%) =
VAR pairs =
    FILTER (
        ADDCOLUMNS (
            VALUES ( athletes[athlete_id] ),
            "@t1", [Trial 1 (cm)],
            "@t2", [Trial 2 (cm)]
        ),
        NOT ISBLANK ( [@t1] ) && NOT ISBLANK ( [@t2] )
    )
VAR te = IF ( COUNTROWS ( pairs ) >= 2, STDEVX.S ( pairs, [@t2] - [@t1] ) / SQRT ( 2 ) )
VAR grand = AVERAGEX ( pairs, ( [@t1] + [@t2] ) / 2 )
RETURN IF ( NOT ISBLANK ( te ) && grand <> 0, 100 * te / grand )

Bias (cm) =
VAR pairs =
    FILTER (
        ADDCOLUMNS (
            VALUES ( athletes[athlete_id] ),
            "@t1", [Trial 1 (cm)],
            "@t2", [Trial 2 (cm)]
        ),
        NOT ISBLANK ( [@t1] ) && NOT ISBLANK ( [@t2] )
    )
RETURN AVERAGEX ( pairs, [@t2] - [@t1] )
```

Because each athlete in `pairs` has both trials, the mean of the athlete means equals the mean of all trials, the grand mean.

In Tableau, put `athlete_id` on Rows. Use these calculations:

```text
Trial 1 (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [session_id] = "S0101" AND [trial_number] = 1 AND [status] = "ok" AND [side] = "bilateral" THEN [value] END)

Trial 2 (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [session_id] = "S0101" AND [trial_number] = 2 AND [status] = "ok" AND [side] = "bilateral" THEN [value] END)

Difference (cm) (aggregate):
IF ISNULL([Trial 1 (cm)]) OR ISNULL([Trial 2 (cm)]) THEN NULL ELSE [Trial 2 (cm)] - [Trial 1 (cm)] END

Pairs (table calculation):
WINDOW_SUM(IIF(ISNULL([Difference (cm)]), 0, 1))

TE (cm) (table calculation):
IF [Pairs] < 2 THEN NULL
ELSE SQRT(MAX(0, ROUND(
    (WINDOW_SUM(ZN([Difference (cm)]) * ZN([Difference (cm)]))
     - WINDOW_SUM(ZN([Difference (cm)])) * WINDOW_SUM(ZN([Difference (cm)])) / [Pairs])
    / ([Pairs] - 1), 9))) / SQRT(2)
END

Grand mean (cm) (table calculation):
IF [Pairs] > 0
THEN WINDOW_SUM(IIF(ISNULL([Difference (cm)]), 0, ([Trial 1 (cm)] + [Trial 2 (cm)]) / 2)) / [Pairs]
END

CV (%) (table calculation):
IF ISNULL([TE (cm)]) OR ISNULL([Grand mean (cm)]) OR [Grand mean (cm)] = 0 THEN NULL
ELSE 100 * [TE (cm)] / [Grand mean (cm)]
END

Bias (cm) (table calculation):
IF [Pairs] > 0 THEN WINDOW_SUM(ZN([Difference (cm)])) / [Pairs] END
```

Set **Compute Using** for every table calculation to `athlete_id`. The results then cover every athlete in the view. The SD is built from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks.

Blanks behave this way in each tool:

- Power BI: an athlete missing a trial is left out of `pairs`, so the TE, the grand mean, and the bias use the same athletes. `STDEVX.S` returns an error with fewer than 2 values. The `>= 2` test stops that.
- Tableau: an athlete missing a trial has a null difference. `Pairs` leaves that athlete out, and `IIF` gives 0 for that athlete in the sums.
- Both: a text trial becomes null on import, so that athlete drops out of the count. The spreadsheet formulas drop that athlete in the same way.

### Calculate the two-way TE in Power BI and Tableau

These versions compute `TE = √MSE` for three or more trials. They remove each athlete's mean and each trial's mean from every value, then add back the grand mean. They square and sum the remainders, divide by (athletes − 1) × (trials − 1), and take the square root. Report the degrees of freedom, (athletes − 1) × (trials − 1), with the TE.

They treat missing data this way:

- An athlete with no row for a trial, or with a blank value, gives a blank TE. The two-way model in this form needs every athlete in every trial.
- Fewer than 2 athletes or fewer than 2 trials give a blank TE.
- A second row for the same athlete and trial gives a blank TE.
- For a measure taken on each side, replace `bilateral` with `left` or `right` and compute each side separately.

To get a TE when an athlete misses a trial, leave that athlete out of the retest and say so with the result. In Power BI, filter out the athlete on `athletes[athlete_id]` in the **Filters** pane.

Both versions assume one row per athlete, measure, and trial in a `measures` table, with the retest stored as `trial_number` 1, 2, 3, and so on in one retest session. Replace `S0101` with the retest session. Check the result against the `√MSE` of 0.4687 cm for the three-trial data under **What changes the number**.

In Power BI, use these DAX measures. They are measures, not calculated columns, because they summarize all athletes. Show them in two cards. In a row for one athlete they are blank. A date or session slicer on the page also filters the retest. Keep the cards on a page without one.

```text
TE two-way (cm) =
VAR retest =
    CALCULATETABLE (
        SELECTCOLUMNS (
            measures,
            "@athlete", measures[athlete_id],
            "@trial", measures[trial_number],
            "@value", measures[value]
        ),
        measures[measure_name] = "cmj_jump_height",
        measures[unit] = "cm",
        measures[session_id] = "S0101",
        measures[status] = "ok",
        measures[side] = "bilateral",
        REMOVEFILTERS ( measures[trial_number] )
    )
VAR k = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( retest, "@a", [@athlete] ) ) )
VAR t = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( retest, "@j", [@trial] ) ) )
VAR filled =
    COUNTROWS (
        DISTINCT (
            SELECTCOLUMNS (
                FILTER ( retest, NOT ISBLANK ( [@value] ) ),
                "@a", [@athlete],
                "@j", [@trial]
            )
        )
    )
VAR complete = k >= 2 && t >= 2 && COUNTROWS ( retest ) = k * t && filled = k * t
VAR grand = AVERAGEX ( retest, [@value] )
VAR ss =
    SUMX (
        retest,
        VAR a = [@athlete]
        VAR j = [@trial]
        VAR athleteMean = AVERAGEX ( FILTER ( retest, [@athlete] = a ), [@value] )
        VAR trialMean = AVERAGEX ( FILTER ( retest, [@trial] = j ), [@value] )
        RETURN ( [@value] - athleteMean - trialMean + grand ) ^ 2
    )
RETURN IF ( complete, SQRT ( ss / ( ( k - 1 ) * ( t - 1 ) ) ) )

TE df (two-way) =
VAR retest =
    CALCULATETABLE (
        SELECTCOLUMNS (
            measures,
            "@athlete", measures[athlete_id],
            "@trial", measures[trial_number]
        ),
        measures[measure_name] = "cmj_jump_height",
        measures[unit] = "cm",
        measures[session_id] = "S0101",
        measures[status] = "ok",
        measures[side] = "bilateral",
        REMOVEFILTERS ( measures[trial_number] )
    )
VAR k = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( retest, "@a", [@athlete] ) ) )
VAR t = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( retest, "@j", [@trial] ) ) )
RETURN IF ( NOT ISBLANK ( [TE two-way (cm)] ), ( k - 1 ) * ( t - 1 ) )
```

In Tableau, use these calculated fields. The TE uses FIXED level of detail (LOD) expressions, not table calculations, so it needs no addressing ([Tableau Help, level of detail expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)). Show them in a sheet with no dimensions:

```text
Retest row (row level):
[measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [session_id] = "S0101" AND [status] = "ok" AND [side] = "bilateral"

Retest value (cm) (row level):
IF [Retest row] THEN [value] END

Athletes (LOD):
{FIXED : COUNTD(IF [Retest row] THEN [athlete_id] END)}

Trials (LOD):
{FIXED : COUNTD(IF [Retest row] THEN [trial_number] END)}

Retest rows (LOD):
{FIXED : SUM(IIF([Retest row], 1, 0))}

Filled cells (LOD):
{FIXED : COUNTD(IF NOT ISNULL([Retest value (cm)]) THEN [athlete_id] + "|" + STR([trial_number]) END)}

Athlete mean (cm) (LOD):
{FIXED [athlete_id] : AVG([Retest value (cm)])}

Trial mean (cm) (LOD):
{FIXED [trial_number] : AVG([Retest value (cm)])}

Retest grand mean (cm) (LOD):
{FIXED : AVG([Retest value (cm)])}

Residual (cm) (row level):
[Retest value (cm)] - [Athlete mean (cm)] - [Trial mean (cm)] + [Retest grand mean (cm)]

Residual SS (LOD):
{FIXED : SUM([Residual (cm)] * [Residual (cm)])}

TE two-way (cm) (aggregate):
IF MIN([Athletes]) >= 2 AND MIN([Trials]) >= 2
   AND MIN([Filled cells]) = MIN([Athletes]) * MIN([Trials])
   AND MIN([Retest rows]) = MIN([Athletes]) * MIN([Trials])
THEN SQRT(MIN([Residual SS]) / ((MIN([Athletes]) - 1) * (MIN([Trials]) - 1)))
END

TE df (two-way) (aggregate):
IF NOT ISNULL([TE two-way (cm)]) THEN (MIN([Athletes]) - 1) * (MIN([Trials]) - 1) END
```

Missing values behave this way in each tool:

- Power BI: DAX treats a blank as 0 in addition, so `BLANK + 5` returns 5 ([Microsoft Learn, blanks, empty strings, and zero values](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types#blanks-empty-strings-and-zero-values)). The `complete` test returns a blank before a blank value can enter the residuals as 0.
- Power BI: `SELECTCOLUMNS` returns as many rows as its input table ([Microsoft Learn, SELECTCOLUMNS](https://learn.microsoft.com/en-us/dax/selectcolumns-function-dax)). `COUNTROWS ( retest )` therefore counts a second row for the same athlete and trial.
- Tableau: `AVG`, `SUM`, and `COUNTD` ignore nulls ([Tableau Help, aggregate functions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm)). A null value gives a null residual, and the `Filled cells` test then gives a null TE.
- Tableau: FIXED expressions are computed before dimension filters ([Tableau Help, order of operations](https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm)). They do use context filters ([Tableau Help, level of detail expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)). To leave an athlete out of the TE, filter on `athlete_id`, then right-click the filter on the **Filters** shelf and select **Add to Context** ([Tableau Help, context filters](https://help.tableau.com/current/pro/desktop/en-us/filtering_context.htm)).

## Worked example

Six athletes did a countermovement jump (CMJ) on two days, 2 days apart, with the same protocol, time of day, and no change in training. These are made-up numbers for illustration.

| Athlete | Trial 1 (cm) | Trial 2 (cm) | Difference (cm) |
|---|---|---|---|
| 1 | 38.2 | 39.0 | 0.8 |
| 2 | 41.5 | 40.8 | −0.7 |
| 3 | 35.0 | 36.1 | 1.1 |
| 4 | 44.1 | 44.9 | 0.8 |
| 5 | 39.7 | 38.9 | −0.8 |
| 6 | 36.8 | 37.9 | 1.1 |

Work through the calculation:

1. Mean difference (bias) = 2.3 / 6 = 0.383 cm.
2. Sum of squared deviations from the mean difference = 3.9483 cm².
3. Sample SD of differences = √(3.9483 / 5) = 0.8886 cm.
4. TE = 0.8886 / 1.4142 = 0.6284 cm.
5. Grand mean of all 12 values = 39.4083 cm.
6. CV% = 100 × 0.6284 / 39.4083 = 1.59%.
7. Log method: the SD of `100 × ln` differences divided by √2 is 1.6268, so CV% = 100 × (exp(0.016268) − 1) = 1.64%.

Result: TE = 0.63 cm, or 1.6% of the mean, from 6 athletes and 2 trials. Report the bias of 0.38 cm separately.

## What changes the number

These choices change the result even when the athletes' true ability does not:

- **Population SD instead of sample SD.** In the worked example, `STDEV.P` gives an SD of 0.8112 cm and a TE of 0.5736 cm, 8.7% smaller than the correct 0.6284 cm.
- **Leaving out √2.** If you report the SD of differences, 0.8886 cm, as TE, it is 41% too large.
- **CV% denominator.** Dividing by the trial 1 mean, not the grand mean, gives 1.60% instead of 1.59%. The gap grows when the bias is large.
- **Log transform.** The log method gave 1.64% against 1.59% from the raw method. Use one method and name it.
- **Time between tests.** Take TE from a short-term retest in which no true change is expected. Hopkins (2000) states that this TE suits decisions about change in an individual over any time frame. Swinton et al. (2018) describe test-retest data "over time periods where true scores are not expected to change". Tests weeks apart let real change into the differences, which inflates TE.
- **Same-day or separate-day retest.** Retesting on separate days counts normal day-to-day variation as noise and gives a larger TE than a same-day retest. This skill offers it as a practice choice, not a published rule. Name the choice with the result.
- **Summary of trials.** A TE for single trials does not fit values that are the best of 3 or the mean of 3. The error of a mean of n independent trials is TE / √n (Hopkins, 2000). Compute TE on the same summary you compare.
- **Method for 3 trials.** Add a third trial for the same 6 athletes: 38.7, 41.6, 35.5, 44.3, 39.6, and 37.2 cm. The two-way `√MSE` is 0.4687 cm, and the pooled within-athlete SD is 0.4708 cm. Averaging SDs instead of variances gives 0.4666 cm. Consecutive pairs give 0.6284 cm for trials 1 and 2 and 0.4846 cm for trials 2 and 3. The drop suggests a practice effect in trial 1.
- **Learning trials.** Keeping a first, unfamiliar trial adds a systematic shift and can widen the spread of differences. Drop early trials that show learning (Weir, 2005).
- **Who is in the sample.** Noise can differ between groups, such as junior and senior athletes. Compute TE separately when residuals differ between groups (Hopkins, 2000).
- **ICC-based SEM.** `SD × √(1 − ICC)` is modestly affected by the spread of the sample (Weir, 2005).

## Units and typical range

TE has the same units as the measure. CV% is a percent.

This file gives no typical range. Typical error depends on the test, the protocol, the device, and the athletes. Take it from your own test-retest data, or from a published reliability study that used the same protocol on similar athletes (Swinton et al., 2018).

## Data you need

You need these data to compute typical error:

- Source: repeated tests of the same athletes, with the same protocol, device, and time of day
- Timing: a short-term retest, close enough together that no true change is expected (Hopkins, 2000; Swinton et al., 2018). A separate-day retest is an optional choice that gives a larger TE.
- Summary: the same summary you compare in monitoring, such as a single trial, the best of 3, or the mean of 3
- Minimum data: about 50 athletes and at least 3 trials give a reasonably precise estimate (Hopkins, 2000). A smaller squad gives an estimate, but a less precise one. Report the number of athletes and trials with the result.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with typical error:

- Forgetting to divide by √2. The SD of the differences is about 1.4 times the typical error. Divide by `SQRT(2)`.
- Using the SD of the raw scores. That is the spread between athletes, not the noise within one athlete. Use the SD of the difference scores.
- Using the population SD. `STDEV.P` in a spreadsheet and `np.std()` in Python divide by n. Use `STDEV.S`, `pandas .std()`, or `np.std(x, ddof=1)`.
- Ignoring the mean difference. A learning or fatigue effect between trials is a systematic change, not noise. Report the mean difference as bias. If it is large, add familiarization trials and drop the early ones (Hopkins, 2000; Weir, 2005).
- Reporting an ICC as the noise. An ICC is a ratio with no units. It rises when the athletes are more varied, even if the noise is the same (Atkinson & Nevill, 1998; Weir, 2005). Report TE or CV% in the units of the measure.
- Using a TE from a different protocol, device, or population. Noise differs between tests. Match the protocol (Swinton et al., 2018).
- Computing TE from tests weeks apart. Real change enters the difference. Use tests close together for the noise estimate (Hopkins, 2000).
- Dividing by the mean of one trial for CV%. Use the grand mean of both trials.
- Mixing absolute TE with a change in percent. Compare a change in centimeters with TE in centimeters, and a change in percent with CV%.

## Example request

> I had my 18 players do a countermovement jump on Monday and again on Wednesday, with no training change between. Column A is jump 1 and column B is jump 2, in centimeters. What is the typical error and the CV for this test?

## Check the result

Run these checks on the result:

- Confirm TE is smaller than the SD of the raw scores between athletes. In the worked example, TE is 0.63 cm and the SD of trial 1 scores is 3.28 cm. If TE is not smaller, the test cannot tell athletes apart.
- Confirm about 95% of the difference scores fall within ±2.77 × TE of the mean difference. These are the 95% limits of agreement (Hopkins, 2000).
- Confirm the CV% from the raw method and the log method are close. A large gap means the error grows with the size of the value. Use the log method then.

## Sources

- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. Journal of Strength and Conditioning Research. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- Atkinson G, Nevill AM. Statistical methods for assessing measurement error (reliability) in variables relevant to sports medicine. Sports Medicine. 1998;26(4):217-238. https://doi.org/10.2165/00007256-199826040-00002
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
