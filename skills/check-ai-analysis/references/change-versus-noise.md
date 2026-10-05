# Change versus noise

Last checked: 2026-10-02

## What it covers

This file shows how to tell a real change in an athlete's result from random measurement error. It defines typical error and the smallest worthwhile change, gives the formulas to compare a change to both, and lists the assumptions behind them.

## Formula

Every test gives a slightly different number each time, even when nothing has changed. The size of that random variation is the typical error (TE). It is the standard deviation of one athlete's repeated measurements (Hopkins, 2000).

Use these quantities:

```text
change     = new value - baseline mean
TE         = SD of the differences between two tests / sqrt(2)
noise band = 1.96 x TE x sqrt(1 + 1/n)
SWC        = 0.2 x between-athlete SD
```

Define every term in the formulas:

- `new value`: the athlete's result from the test you are judging, in the unit of the measure
- `baseline mean`: the mean of `n` earlier values of that athlete. Do not include the new value.
- `n`: the number of values in the baseline mean. For two single tests, `n = 1`.
- `SD of the differences`: the standard deviation of the test-to-test differences across athletes, in the unit of the measure
- `TE`: typical error, in the unit of the measure. If you express it as a percent of the value, it is a coefficient of variation.
- `noise band`: when nothing has changed, error alone gives a change smaller than this about 95 percent of the time, if the assumptions below hold
- `SWC`: the smallest worthwhile change, the smallest change that matters in practice. The common default is 0.2 times the standard deviation between athletes at baseline, taken from the same group and the same test (Swinton et al., 2018). Hopkins and colleagues (2009) list 0.2 as the threshold for a small standardized difference.
- `between-athlete SD`: the standard deviation of the athletes' scores on the test, in the unit of the measure

For two single tests, `n = 1`, and the noise band is `1.96 x sqrt(2) x TE`, about 2.77 times TE. Swinton and colleagues (2018) give this as the 95 percent range for an observed change, and state that the standard deviation of change scores equals TE times the square root of 2. Weir (2005) also shows how to use the standard error of measurement, another name for TE, to find the minimal difference needed to be confident that one person's true score changed.

For a baseline that is the mean of `n` tests, the variance of the new value (TE squared) and the variance of the baseline mean (TE squared divided by `n`) add.

This gives `sqrt(1 + 1/n)` in place of `sqrt(2)`.

Adding variances gives this band. Hopkins (2017) uses this error, TE x sqrt(1 + 1/n), for a change from the mean of several reference tests in his monitoring spreadsheet. The same sqrt(1 + 1/n) factor appears in the standard prediction interval for one new value against a mean of n values (NIST, Dataplot reference manual). The 95 percent level with 1.96 is this skill's choice.

Use this spreadsheet formula for TE, with the differences in `D2:D31`:

```text
=STDEV.S(D2:D31)/SQRT(2)
```

Use this Python snippet for two single tests. These ten differences have an SD of 1.106 cm:

```python
import numpy as np
diff = np.array([1.2, -0.8, 0.5, -1.5, 2.0, 0.3, -0.4, 1.1, -1.0, 0.6])  # test 2 minus test 1
te = diff.std(ddof=1) / np.sqrt(2)
noise_band = 1.96 * np.sqrt(2) * te
print(round(te, 2), round(noise_band, 2))   # 0.78 2.17
```

### List the assumptions beside the band

Write these assumptions next to every noise band you report:

- The athlete's true value stayed the same across the baseline and the new test, apart from the change you want to detect.
- Errors are independent from test to test. A swing that lasts several days, such as a poor week of sleep, violates this.
- TE is the same for every athlete and at every size of value.
- TE is known. Use 1.96 when TE comes from a large reliability study. When TE comes from few athletes, use a t multiplier. See the table below.
- TE comes from a short-term retest in which no true change is expected. Swinton and colleagues (2018) describe test-retest data from a group over time periods where true scores are not expected to change. TE uses the same summary as the values you compare: a single trial, the best of 3, or the mean of 3.

Optional: retest on separate days, so that normal day-to-day variation counts as noise. This is a practice choice of this skill, not a published rule. It gives a larger TE than a same-day retest, and so a wider band.

With all assumptions met, about 5 percent of unchanged results fall outside the band when you look in both directions, or 2.5 percent in one direction.

When assumptions fail, the real rate can be higher or lower than 5 percent. It is higher when TE is too small, comes from few athletes, or varies between athletes. It can be lower when TE is overestimated, or when errors are positively correlated over time.

### Use a t multiplier when TE is estimated

When you estimate TE from few athletes, use a larger multiplier than 1.96. Swinton and colleagues (2018) give adjusted multiples by the number of people in the test-retest study, for example 2.26 for a TE from 10 participants.

The values below come from the t distribution. Take the degrees of freedom from the TE study, not from the baseline: the number of athletes minus 1 for two trials, or (athletes minus 1) x (trials minus 1) for the method with three or more trials below. In a spreadsheet, use `=T.INV.2T(0.05, df)`. The table also shows the share of unchanged results that a 1.96 band flags, instead of 5 percent:

| Degrees of freedom | Example | 95 percent multiplier | Share flagged with 1.96 |
|---|---|---|---|
| 5 | TE from 6 athletes, two tests | 2.57 | 10.7 percent |
| 9 | TE from 10 athletes, two tests | 2.26 | 8.2 percent |
| 19 | TE from 20 athletes, two tests | 2.09 | 6.5 percent |
| 49 | TE from 50 athletes, two tests | 2.01 | 5.6 percent |

### Calculate TE and the t multiplier in Power BI and Tableau

These versions use only athletes with both tests, and they return a blank, not 0 or an error, when fewer than 2 athletes qualify.

Both versions assume one row per athlete, test, and trial in a `measures` table, with the retest stored as `trial_number` 1 and 2 in one retest session. The session filter keeps trials from other dates out. Replace `S0101` with the retest session. For a measure taken on each side, replace `bilateral` with `left` or `right` and compute each side separately. If your retest uses two sessions instead, filter test 1 and test 2 on their two `session_id` values in place of `trial_number`.

In Power BI, use these DAX measures. They are measures because TE is a summary across athletes, not a value on one row:

```text
Test 1 (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[session_id] = "S0101",
    measures[trial_number] = 1,
    measures[status] = "ok",
    measures[side] = "bilateral"
)

Test 2 (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[session_id] = "S0101",
    measures[trial_number] = 2,
    measures[status] = "ok",
    measures[side] = "bilateral"
)

TE (cm) =
VAR pairs =
    FILTER (
        ADDCOLUMNS (
            VALUES ( athletes[athlete_id] ),
            "@t1", [Test 1 (cm)],
            "@t2", [Test 2 (cm)]
        ),
        NOT ISBLANK ( [@t1] ) && NOT ISBLANK ( [@t2] )
    )
RETURN
    IF ( COUNTROWS ( pairs ) >= 2, STDEVX.S ( pairs, [@t2] - [@t1] ) / SQRT ( 2 ) )

t multiplier (95%) =
VAR df = LOOKUPVALUE ( reliability[te_df], reliability[measure_name], "cmj_jump_height" )
RETURN IF ( NOT ISBLANK ( df ) && df >= 1, T.INV.2T ( 0.05, df ) )
```

`reliability` is a small table with one row per measure: `measure_name`, `te`, `te_df`, and `te_source`. Take `te_df` from the TE study: athletes minus 1 for two trials, or (athletes minus 1) x (trials minus 1) for three or more trials.

In Tableau, put `athlete_id` on Rows. Use these calculated fields:

```text
Test 1 (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [session_id] = "S0101" AND [trial_number] = 1 AND [status] = "ok" AND [side] = "bilateral" THEN [value] END)

Test 2 (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [session_id] = "S0101" AND [trial_number] = 2 AND [status] = "ok" AND [side] = "bilateral" THEN [value] END)

Difference (cm) (aggregate):
IF ISNULL([Test 1 (cm)]) OR ISNULL([Test 2 (cm)]) THEN NULL ELSE [Test 2 (cm)] - [Test 1 (cm)] END

Pairs (table calculation):
WINDOW_SUM(IIF(ISNULL([Difference (cm)]), 0, 1))

TE (cm) (table calculation):
IF [Pairs] < 2 THEN NULL
ELSE SQRT(MAX(0, ROUND(
    (WINDOW_SUM(ZN([Difference (cm)]) * ZN([Difference (cm)]))
     - WINDOW_SUM(ZN([Difference (cm)])) * WINDOW_SUM(ZN([Difference (cm)])) / [Pairs])
    / ([Pairs] - 1), 9))) / SQRT(2)
END
```

Set **Compute Using** to `athlete_id` for `Pairs` and `TE (cm)`. The TE then covers every athlete in the view. The formula builds the SD from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks. `ROUND(..., 9)` and `MAX(0, ...)` stop rounding error from turning a zero spread into a tiny or negative variance.

Tableau has no function for the t-distribution inverse. Use one of these workarounds:

- Fill the `multiplier` column of the `reliability` table with the t multiplier, computed in Python with `scipy.stats.t.ppf(0.975, df)` or in R with `qt(0.975, df)`. Both equal `T.INV.2T(0.05, df)`.
- Relate a lookup table of `df` and `t95` to `reliability` on `df`.
- If an R analytics extension is set up, use the table calculation `SCRIPT_REAL("qt(0.975, .arg1)", MIN([te_df]))`.

Blanks behave this way in each tool:

- Power BI: `STDEVX.S` skips blanks, but it returns an error, not a blank, with fewer than 2 values. The `COUNTROWS ( pairs ) >= 2` test stops that. A `T.INV.2T` with `df` below 1 is not called.
- Tableau: an athlete missing a test gets a null difference, and the indicator in `Pairs` leaves that athlete out.

### Compute TE from three or more trials

With three or more retests for each athlete, remove each athlete's mean and each trial's mean, then pool the remainder. This removes a shift in the mean from trial to trial, such as learning or fatigue, which Hopkins (2000) says must not count as error.

With two trials, it gives the same TE as the SD of the differences divided by `sqrt(2)`. Look at the mean change between consecutive trials first. A large shift means the protocol needs more familiarization.

```python
import pandas as pd
# one row per athlete and trial, from a short-term retest with no true change expected
d = pd.DataFrame({"athlete_id": ["A1"] * 3 + ["A2"] * 3 + ["A3"] * 3 + ["A4"] * 3,
                  "trial": [1, 2, 3] * 4,
                  "value": [40.1, 41.0, 40.6, 35.2, 36.1, 35.0, 45.3, 44.8, 46.0, 38.0, 39.2, 38.9]})
w = d.pivot(index="athlete_id", columns="trial", values="value")
print(w.diff(axis=1).mean().dropna().round(2).tolist())  # mean change between consecutive trials
r = w.sub(w.mean(axis=1), axis=0).sub(w.mean(axis=0), axis=1) + w.stack().mean()
k, t = w.shape
te = ((r ** 2).to_numpy().sum() / ((k - 1) * (t - 1))) ** 0.5
print(round(te, 2))  # 0.54, with (k - 1) x (t - 1) = 6 degrees of freedom
```

This prints `[0.62, -0.15]` and `0.54`.

### Calculate TE from three or more trials in Power BI and Tableau

These versions follow the Python above. They give the mean change between consecutive trials, the TE, and its degrees of freedom, (athletes minus 1) x (trials minus 1).

They treat missing data as the Python does:

- An athlete with no row for a trial, or with a blank value, gives a blank TE and a blank degrees of freedom. The Python gives a `nan` TE in the same case. The model needs every athlete in every trial.
- Fewer than 2 athletes or fewer than 2 trials give a blank TE.
- The mean change between two consecutive trials uses only athletes with a value in both trials, as the Python `mean` does. It is blank for the first trial.

To get a TE when an athlete misses a trial, leave that athlete out of the retest and say so with the result. In Power BI, filter out the athlete on `athletes[athlete_id]` in the **Filters** pane.

Both versions assume one row per athlete, measure, and trial in a `measures` table, with the retest stored as `trial_number` 1, 2, 3, and so on in one retest session. Replace `S0101` with the retest session. A second row for the same athlete and trial gives a blank TE. The mean change then uses the larger value. The Python stops with an error in that case. For a measure taken on each side, replace `bilateral` with `left` or `right` and compute each side separately.

In Power BI, use these DAX measures. They are measures, not calculated columns, because each one summarizes all athletes in the retest:

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

Mean change from previous trial (cm) =
VAR j = SELECTEDVALUE ( measures[trial_number] )
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
VAR prev = MAXX ( FILTER ( retest, [@trial] < j ), [@trial] )
VAR pairs =
    FILTER (
        ADDCOLUMNS (
            DISTINCT ( SELECTCOLUMNS ( retest, "@a", [@athlete] ) ),
            "@now", VAR a = [@a] RETURN MAXX ( FILTER ( retest, [@athlete] = a && [@trial] = j ), [@value] ),
            "@before", VAR a = [@a] RETURN MAXX ( FILTER ( retest, [@athlete] = a && [@trial] = prev ), [@value] )
        ),
        NOT ISBLANK ( [@now] ) && NOT ISBLANK ( [@before] )
    )
RETURN IF ( NOT ISBLANK ( prev ) && COUNTROWS ( pairs ) >= 1, AVERAGEX ( pairs, [@now] - [@before] ) )
```

Show `TE two-way (cm)` and `TE df (two-way)` in two cards. In a row for one athlete they are blank, because one athlete is fewer than 2. A date or session slicer on the page also filters the retest. Keep the cards on a page without one. Put `measures[trial_number]` on the rows of a table visual to show `Mean change from previous trial (cm)`. The previous trial is the next lower trial number in the retest, as in the Python. `REMOVEFILTERS ( measures[trial_number] )` lets each measure see every trial from that row. Store the degrees of freedom as `te_df` in the `reliability` table, so the `t multiplier (95%)` measure above uses it.

In Tableau, use these calculated fields. The TE uses FIXED level of detail (LOD) expressions, not table calculations, so it needs no addressing ([Tableau Help, level of detail expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)):

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

For the mean change between consecutive trials, put `athlete_id` on Rows and add these fields. Set **Compute Using** to `athlete_id` for each table calculation. For each later trial, add a `Trial N (cm)` field, a change field, and a mean change field. Pair each trial with the next lower trial number in the retest. With trials 1, 2, and 4, use `Change 2 to 4 (cm)`.

```text
Trial 1 (cm) (aggregate):
MAX(IF [trial_number] = 1 THEN [Retest value (cm)] END)

Trial 2 (cm) (aggregate):
MAX(IF [trial_number] = 2 THEN [Retest value (cm)] END)

Change 1 to 2 (cm) (aggregate):
IF ISNULL([Trial 1 (cm)]) OR ISNULL([Trial 2 (cm)]) THEN NULL ELSE [Trial 2 (cm)] - [Trial 1 (cm)] END

Mean change 1 to 2 (cm) (table calculation):
IF WINDOW_SUM(IIF(ISNULL([Change 1 to 2 (cm)]), 0, 1)) > 0
THEN WINDOW_SUM(ZN([Change 1 to 2 (cm)])) / WINDOW_SUM(IIF(ISNULL([Change 1 to 2 (cm)]), 0, 1))
END
```

Missing values behave this way in each tool:

- Power BI: DAX treats a blank as 0 in addition, so `BLANK + 5` returns 5 ([Microsoft Learn, blanks, empty strings, and zero values](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types#blanks-empty-strings-and-zero-values)). The `complete` test returns a blank before a blank value can enter the residuals as 0.
- Power BI: `SELECTCOLUMNS` returns as many rows as its input table ([Microsoft Learn, SELECTCOLUMNS](https://learn.microsoft.com/en-us/dax/selectcolumns-function-dax)). `COUNTROWS ( retest )` therefore counts a second row for the same athlete and trial.
- Tableau: `AVG`, `SUM`, and `COUNTD` ignore nulls ([Tableau Help, aggregate functions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm)). A null value gives a null residual, and the `Filled cells` test then gives a null TE.
- Tableau: FIXED expressions are computed before dimension filters ([Tableau Help, order of operations](https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm)). They do use context filters ([Tableau Help, level of detail expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)). To leave an athlete out of the TE, filter on `athlete_id`, then right-click the filter on the **Filters** shelf and select **Add to Context** ([Tableau Help, context filters](https://help.tableau.com/current/pro/desktop/en-us/filtering_context.htm)).

## Units and typical range

Both TE and SWC are in the unit of the measure, or in percent. There is no universal TE or SWC for a test. Each depends on the test, the protocol, the device, and the athletes.

Do not use a TE or SWC from a paper unless the test, the device, and the population match the user's. Use the user's own repeated tests.

| Quantity | Where it comes from | Source |
|---|---|---|
| TE | The user's short-term retest with no true change expected, same protocol and summary | Hopkins, 2000; Swinton et al., 2018 |
| Noise band | 1.96 x TE x sqrt(1 + 1/n); for n = 1, 1.96 x sqrt(2) x TE | Swinton et al., 2018, for n = 1; Hopkins, 2017, for the error against a mean of n tests |
| SWC | 0.2 x between-athlete SD | Swinton et al., 2018; Hopkins et al., 2009 |

### Know the limits of the SWC

Treat 0.2 times the between-athlete SD as a convention, with these limits:

- It depends on how alike the athletes are. A squad of similar athletes has a small SD, and so a small SWC.
- It is imprecise in a small squad, because an SD from few athletes is imprecise.
- The observed between-athlete SD includes measurement error. The SD of the athletes' true scores is `sqrt(SD^2 - TE^2)`. This follows from adding the variances, and is derived.
- It is a rule for test scores. For a top athlete's competition time or distance, Hopkins and colleagues (2009) give thresholds of 0.3, 0.9, 1.6, 2.5, and 4.0 times the athlete's within-athlete variation between competitions, not multiples of the between-athlete SD.

## Data you need

Collect this data before you judge a change:

- Source: the user's own repeated measurements of the same test, with the same protocol, in athletes who were not trying to change
- Timing: a short-term retest in which no true change is expected (Swinton et al., 2018). Tests weeks apart in training let real change into the differences. Optional: retest on separate days, as a practice choice that gives a larger TE.
- Summary: the same summary as the values you compare, such as a single trial, the best of 3, or the mean of 3
- Sampling: at least two tests for each athlete. Three or more is better.
- Minimum data: Hopkins (2000) states that reasonable precision for a reliability estimate needs about 50 participants and at least 3 trials. With fewer, say that the TE is a rough estimate, and use the t multiplier.

## Interpret the result

Compare each change to the noise band, and then to the SWC in the direction the user cares about. The likely range of the true change is the change plus or minus the noise band.

Use a 95 percent band unless the user chooses another level. This is a choice, and it matches the common practice of reporting the minimal detectable change at 95 percent (MDC95). Give each result one of these labels:

| Label | Rule | What to say |
|---|---|---|
| Within error | The change is inside the noise band. | The change cannot be separated from measurement error. |
| Larger than error | The change is beyond the noise band, and the change minus the band is not beyond the SWC. | Larger than measurement error; may or may not be worthwhile. |
| Beyond the SWC | The change minus the noise band is beyond the SWC. For a rise, change minus band is above the SWC. For a drop, change plus band is below minus the SWC. | Larger than measurement error, and its likely range lies beyond the smallest worthwhile change. |
| Not enough data | The new value, the baseline, or the TE is missing. | Not enough data to judge the change. |

If a change lies beyond the band in the direction the user did not choose, report it with its direction, and do not compare it to the SWC unless the user asks.

This interval rule follows Swinton and colleagues (2018), who classify a change by whether the confidence interval for the true change lies in a pre-defined region, such as beyond the SWC. A change whose likely range spans both worthwhile and trivial values is unclear.

Batterham and Hopkins (2006) describe a related method based on probabilities. It is not the source of this rule.

If the noise band is larger than the SWC, the test can detect a large change. It cannot resolve a change near the size of the SWC in one athlete from two single tests.

Swinton and colleagues (2018) note that TE must not be so large that an athlete would need an unrealistic change to pass the SWC. Say this, and suggest a baseline of several tests or a less noisy test.

### Worked example

These numbers are made up for illustration. Ten athletes jump twice, a short time apart, when no true change is expected. The differences give an SD of 1.1 cm, so TE is 0.78 cm and the noise band for two single tests is 2.16 cm (1.96 x 1.1 cm).

The between-athlete SD is 4.5 cm, so the SWC is 0.9 cm.

Treat TE as known here. With TE from only 10 athletes, a stricter band uses 2.26 in place of 1.96, which gives 2.49 cm.

Three athletes gain height on the next test:

- A gain of 1.5 cm is inside the noise band. It cannot be separated from error, even though it is larger than the SWC.
- A gain of 2.5 cm is beyond the band. The change minus the band is 0.34 cm, which is below the SWC. Say it is larger than measurement error and may or may not be worthwhile.
- A gain of 3.5 cm is beyond the band. The change minus the band is 1.34 cm, which is above the SWC. Say its likely range lies beyond the smallest worthwhile change.

The noise band (2.16 cm) is larger than the SWC (0.9 cm). The test detects the 3.5 cm gain, but it cannot resolve a 0.9 cm change in one athlete from two single tests.

### Treat wellness scales with care

Wellness items scored 1 to 5 are ordinal. The steps are ranks, not equal amounts. A mean, an SD, a TE, and a noise band all assume values on a continuous scale. These problems follow:

- A single answer moves in whole steps. Against a baseline mean of 3.4, an answer of 1, 2, 3, 4, or 5 gives a change of -2.4, -1.4, -0.4, 0.6, or 1.6. A band of 1.3 points then flags every answer except 3 and 4, and the 95 percent figure does not hold.
- An athlete who always answers 5 cannot rise. Floor and ceiling effects shrink the SD and the TE.
- A sum of several items is closer to continuous, but the items may not be equal steps either.

Show the raw answers and the number of days at each answer next to any band. Call a band on a 1 to 5 item a rough guide. Apart from 2 studies of reliability and responsiveness, a systematic review found no validation studies of the single items most used in sport (Jeffries et al., 2020). So do not assume a published TE exists for a wellness item. A retest minutes apart cannot show day-to-day noise, and wellness states change from day to day. This is a practice judgment of this skill. For wellness answers, compare each answer with the athlete's own usual variation, as the wellness z-score in the `load-and-wellness` skill does. Label it as usual variation, not measurement error.

### Check z-scores

A z-score is the distance of a value from a mean, in units of an SD. Check each z-score for these problems:

- A rolling z-score whose SD includes the new value. An extreme value then widens its own SD and shrinks its own z-score.
- An SD from few values. It is imprecise, so a z-score built on it swings widely.
- A squad z-score read as individual change. It shows where an athlete sits in the squad, not how the athlete changed.
- A cut point such as plus or minus 1.5 or plus or minus 2 with no source. Ask where it came from.

### Check rolling baselines

A rolling baseline, such as the mean of the last 4 weeks, moves with the athlete. A slow, steady decline drags the baseline down with it, so each new value looks normal and never flags. Compare to a fixed baseline from a stable period as well, and show the trend.

### Check whether error differs between athletes

One TE for the whole squad assumes every athlete is equally consistent. Some athletes vary more than others.

A pooled TE then flags too often for the less consistent athletes and too rarely for the more consistent ones.

Error can also grow with the size of the value. If it does, use percent and log values (Atkinson and Nevill, 1998).

### Read repeated flags with care

Flags in consecutive weeks against the same baseline are not independent. They share the baseline, and a swing can last more than a week. Two flags in a row are not two separate confirmations.

A chance count of 5 percent assumes independent results.

### Report chance flags across a squad

Across a squad, report the number of flags expected by chance next to the number found. Multiply the number of results checked by 5 percent, or by 2.5 percent for one direction. For example, 25 athletes checked in one direction give 0.625 expected false flags a week, and a 46.9 percent chance of at least one.

Recommend a repeat test before anyone acts on a single flag. An athlete picked for an extreme value tends to be closer to average at the next test, without any real change (Barnett et al., 2005).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often when they judge change:

- Reporting a change with no comparison to TE, so the reader cannot tell a real change from noise
- Calling a change larger than the SWC because the observed change passes the SWC. The change minus the noise band must pass the SWC.
- Using the standard deviation of one athlete's own baseline values as TE. It is not TE: it mixes real change with error. It is also imprecise when it comes from few values. By the t distribution, a 1.96 band built on an SD from 5 stable values flags about 12 percent of unchanged values, not 5 percent. Get TE from a test-retest study instead.
- Using an athlete's own baseline SD without the usual-variation rules. When no TE exists, that SD may give a usual-variation band: `baseline mean ± t(n - 1) x baseline SD x sqrt(1 + 1/n)`, from at least 10 stable values (Hopkins, 2017). This is the standard prediction interval for one new value (NIST, Dataplot reference manual). Check that it uses t with n - 1 degrees of freedom, not 1.96: with 10 values, 1.96 lets 8.2 percent of unchanged values fall outside, against 5.0 percent with t(9). Check that it gives two states only, within or outside usual variation, with no smallest worthwhile change tier, and that it never calls the band measurement error.
- Using the between-athlete SD as TE. It is much larger, because athletes differ from each other.
- Using the standard error of the mean as the SWC or the noise
- Taking TE from a paper for a different test, device, or population
- Taking TE from retests far enough apart for real change to occur, such as tests weeks apart in training. Real change then inflates TE.
- Building the t multiplier from the baseline `n`. Take its degrees of freedom from the TE study.
- Taking TE from single trials, then judging the best of 3, or the reverse
- Computing TE from tests where the mean shifted between trials, for example from learning or fatigue. A shift that differs between athletes inflates TE. A shift the same for every athlete moves every change score by that amount. Check the mean change between trials first, and remove trials with learning or fatigue effects (Hopkins, 2000; Weir, 2005).
- Calling a change "significant" because `p < 0.05` in a group test, then applying it to one athlete
- Using the noise band of two single tests when the baseline is an average, or the reverse
- Applying a percent TE to raw values when error is a fixed number of units, or the reverse. Check whether error grows with the size of the value. If it does, use percent and log values (Atkinson and Nevill, 1998).
- Ignoring regression to the mean. An athlete picked for an extreme value will usually look closer to average at the next test, without any real change (Barnett et al., 2005).

## Example request

> Here are two rounds of jump tests, a week apart, for the squad. Which athletes changed by more than noise?

## Check the result

Run these checks on the result:

- Recompute TE by hand from the first three athletes' differences and the full SD. Confirm it equals the SD divided by 1.414.
- Confirm the unit of TE, the noise band, and the SWC is the unit of the measure, or percent.
- Confirm the band uses `sqrt(1 + 1/n)` with the right `n`, and that the assumptions are listed beside it.
- Count the changes beyond the noise band when nothing was done. With all assumptions met, expect about 5 percent when you look in both directions, or 2.5 percent in one direction. A result labeled Beyond the SWC is rarer by chance. A much larger share suggests the TE is too small or an assumption fails. It can also reflect a real change across the squad, for example after a block of matches.

## Sources

These sources support the formulas and rules in this file:

- Hopkins WG. Measures of reliability in sports medicine and science. *Sports Medicine*. 2000;30(1):1-15. doi:10.2165/00007256-200030010-00001. Defines the typical error as the standard deviation of an individual's repeated measurements, states that systematic changes in the mean between consecutive trials, such as learning or fatigue, must be removed from it, and states that reasonable precision needs about 50 participants and at least 3 trials.
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. *Frontiers in Nutrition*. 2018;5:41. doi:10.3389/fnut.2018.00041. Source of the rule to estimate TE from test-retest data over periods where true scores are not expected to change, the 95 percent range for a change (1.96 x TE x sqrt(2)), the statement that the SD of change scores is TE x sqrt(2), larger multiples when TE comes from a small sample, the 0.2 x between-athlete SD smallest worthwhile change, and the rule to classify a change by whether the confidence interval for the true change lies in a pre-defined region.
- Jeffries AC, Wallace L, Coutts AJ, McLaren SJ, McCall A, Impellizzeri FM. Athlete-reported outcome measures for monitoring training responses: a systematic review of risk of bias and measurement property quality according to the COSMIN guidelines. *International Journal of Sports Physiology and Performance*. 2020;15(9):1203-1215. doi:10.1123/ijspp.2020-0386. Accessed 2026-10-02. Found measurement error inadequate for multiple-item measures. Apart from 2 studies of reliability and responsiveness, it found no validation studies of the single items most used in sport.
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. *Sportscience*. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm. Accessed 2026-10-02. Its monitoring spreadsheet computes the error of a change from the mean of several reference tests as TE x sqrt(1 + 1/n), with t at the typical error's degrees of freedom. The skills use only its error formula, not its magnitude-based inference.
- National Institute of Standards and Technology. Dataplot reference manual: prediction limits. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/predlimi.htm. Accessed 2026-10-02. Gives the prediction interval for the mean of m new values as mean ± t x s x sqrt(1/n + 1/m), after Hahn and Meeker (1991), *Statistical Intervals*, pages 61-62. With m = 1, the factor is sqrt(1 + 1/n).
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. *Medicine and Science in Sports and Exercise*. 2009;41(1):3-13. doi:10.1249/MSS.0b013e31818cb278. Lists 0.2 as the small standardized difference, gives thresholds of 0.3, 0.9, 1.6, 2.5, and 4.0 of the within-athlete variation between competitions for a top athlete's competition time or distance, and advises judging magnitude by precision and not by null-hypothesis tests.
- Batterham AM, Hopkins WG. Making meaningful inferences about magnitudes. *International Journal of Sports Physiology and Performance*. 2006;1(1):50-57. doi:10.1123/ijspp.1.1.50. Describes a related, probability-based method of inference from confidence limits compared with beneficial and harmful values.
- Atkinson G, Nevill AM. Statistical methods for assessing measurement error (reliability) in variables relevant to sports medicine. *Sports Medicine*. 1998;26(4):217-238. doi:10.2165/00007256-199826040-00002. Advises a logarithmic transformation and ratios when error grows with the size of the value.
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. *Journal of Strength and Conditioning Research*. 2005;19(1):231-240. doi:10.1519/15184.1. Advises removing trials with learning or fatigue effects, and shows how to use the standard error of measurement to find the minimal difference needed to be confident that one person's true score changed.
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. *International Journal of Epidemiology*. 2005;34(1):215-220. doi:10.1093/ije/dyh299. Explains regression to the mean.
