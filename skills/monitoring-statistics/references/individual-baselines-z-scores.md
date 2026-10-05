# Individual baselines and z-scores

Last checked: 2026-10-02

## What it measures

An individual baseline is an athlete's own normal for a measure, built from their prior values. A z-score says how far today's value sits from that normal, in units of the athlete's own usual variation.

Using the athlete as their own control is the basis of single-athlete monitoring (Sands et al., 2019). Individual reference ranges classified muscle recovery more accurately than group ranges for one blood marker in one study (Hecksteden et al., 2017).

## Formula

Use a rolling baseline of prior values only, by default:

```text
baseline_mean = mean of the athlete's previous k values (today excluded)
baseline_SD   = sample SD of the same k values
z             = (today − baseline_mean) / baseline_SD
```

Define every term in the formula:

- `today`: the athlete's value on the day you judge, in the units of the measure
- `k`: the baseline window, as a count of prior tests or a number of prior days. State it.
- `baseline_mean`: the mean of the window, in the units of the measure
- `baseline_SD`: the sample SD of the window, dividing by k − 1, in the units of the measure
- `z`: the z-score. It has no units. A z of −2 means today is 2 of the athlete's usual SDs below their baseline mean.

Use these variants when they fit:

- **Rolling window of tests.** The previous k tests. Use it when tests are irregular, such as weekly jumps. This is the default.
- **Rolling window of days.** The previous k calendar days. Use it only for daily measures. Missing days shrink the real number of values, so report n.
- **Fixed baseline.** The mean and SD of a set period, such as the first weeks of preseason. Use it when you want a stable reference that does not drift. State the dates.
- **Control limits.** Sands et al. (2019) show limits at 1.5 and 2.0 × the baseline SD around the baseline mean. These equal z = ±1.5 and z = ±2.0. They are examples from a published case, not validated thresholds. With a 10-value baseline and pure noise, |z| > 2 flags about 8.9% of tests and |z| > 1.5 flags about 18.6%. Let the practitioner choose, and cite the source of any cut point.

A z-score says how unusual today is for this athlete. It does not say whether the change is larger than measurement error. For that, use the noise band with the test's typical error (TE):

```text
noise band = 1.96 × TE × √(1 + 1/n)
```

- `TE`: typical error of the test, from test-retest data, in the units of the measure. See the typical error reference.
- `n`: the number of values in the baseline mean
- `1.96`: the z value for 95%. Error alone gives a change smaller than this band about 95 percent of the time.

The error of a mean of n independent tests is TE / √n (Hopkins, 2000). Adding the variances of the new test and the baseline mean gives an error of TE × √(1 + 1/n).

Hopkins (2017) uses the same error for a change from the mean of several reference tests in his monitoring spreadsheet. The 95% level is a choice. For two single tests, n = 1, and the band is 1.96 × √2 × TE, about 2.77 × TE (Weir, 2005).

The band rests on these assumptions:

- The athlete's true score stays constant over the baseline and the new test.
- Errors are independent.
- TE is the same across athletes and across the range of values.
- TE is known. If TE comes from few athletes, replace 1.96 with a t value whose degrees of freedom come from the TE study, not from the baseline. Use athletes − 1 for two trials, or (athletes − 1) × (trials − 1) for the two-way model. TE from 6 athletes gives t(5) = 2.57. TE from 10 athletes gives t(9) = 2.26 (Swinton et al., 2018).
- TE comes from a short-term retest with no true change expected (Hopkins, 2000; Swinton et al., 2018). It uses the same summary as the values you compare: a single trial, the best of 3, or the mean of 3.

With all assumptions met, about 5% of pure-noise changes cross the band, or 2.5% when only one direction matters, such as a drop.

When the assumptions fail, the real rate can be higher or lower than 5%. It is higher when TE is too small, comes from few athletes, or varies between athletes. It can be lower when TE is overestimated or errors are positively correlated over time.

Never call 5% a lower bound. For example, with TE from 6 athletes and 1.96, about 10.7% of pure-noise changes cross the band. With t(5), the rate is 5.0%.

A TE overestimated by 20% gives 1.87% for two single tests. Error correlation of 0.5 between consecutive tests gives 0.56% for two single tests, or 4.59% against a baseline of 10.

Across a squad, report the number of flags expected by chance next to the number found. Expected flags = number of results × 5%, or × 2.5% for one direction.

For 25 athletes checked for drops, you expect 0.625 false flags each week. The chance of at least one is 46.9%. Flags in consecutive weeks against the same baseline are not independent.

Recommend a repeat test before anyone acts on a single flag. A flagged value was picked for being extreme, and regression to the mean makes the next value likely to sit closer to the athlete's usual level (Barnett et al., 2005).

Do not use the athlete's own baseline SD as TE. It mixes biological variation with measurement error.

### Use usual variation when no TE exists

When no TE exists for the test, you can still compare today with the athlete's usual variation. Hopkins's (2017) monitoring spreadsheet takes a similar approach: if no short-term TE is entered, it uses the athlete's own scatter about the trend line. Build the band from the baseline SD:

```text
usual-variation band = baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)
```

The terms mean the following:

- `t(n − 1)`: the two-sided 95% t value with n − 1 degrees of freedom, because the SD comes from the n baseline values. In a spreadsheet, use `T.INV.2T(0.05, n − 1)`.
- `√(1 + 1/n)`: adds the spread of the new value to the uncertainty of the baseline mean.

This is the standard prediction interval for one new value from a normal distribution (NIST, after Hahn and Meeker, 1991, pp. 61-62). Today sits outside the band when |z| > t(n − 1) × √(1 + 1/n). With 10 values, that multiplier is 2.2622 × 1.0488 = 2.37.

Follow these rules:

- Use at least 10 values from a stable period: one protocol, no clear trend, no illness or injury, and today left out. Hopkins (2017) says at least 10 tests are needed for even modest precision.
- Use t, not 1.96. With 10 stable values, independent days, and normal data, 5.0% of values fall outside the band by chance with t(9), and 8.2% with 1.96.
- Give two states only: `Within usual variation` or `Outside usual variation`. Do not add a smallest worthwhile change tier.
- Never call the band noise or measurement error. It holds real day-to-day change as well as error.
- Say that day-to-day correlation raises the chance rate. In a simulation run for this skill, with 10 values and a correlation of 0.3 or 0.5 between consecutive days, 5.7% or 6.6% of values fell outside the t(9) band.

## Calculate a rolling z-score

Follow these steps to calculate a rolling z-score from raw inputs:

1. Arrange the data in long format: one row per `athlete_id`, `date`, and value, such as `cmj_cm`. If the `ams-data-setup` skill is installed, use its table layout.
2. Sort the rows by `athlete_id`, then by `date`.
3. Drop or mark rows from test days that broke protocol, as the user defines them. Do not fill missing values with zero.
4. For each row, take the previous k values for the same athlete. Do not include the row itself.
5. Count those values.
6. If the count is below the minimum you set, leave the z-score blank and say why.
7. Compute the mean and the sample SD of the window.
8. If the SD is 0, because every value in the window is the same, leave the z-score blank and say why.
9. Compute `z = (today − baseline_mean) / baseline_SD`.
10. Compute the noise band `1.96 × TE × √(1 + 1/n)` from the test's TE, and compare the change from the baseline mean with it.
11. Report the z-score with the window k, the count n, the baseline mean, the baseline SD, and the units.

Spreadsheet version, for one athlete with dates sorted in column A and values in column B, judging row 12 against the 10 rows before it. Put the minimum number of baseline values (2 or more), such as 10, in cell `H1`:

```text
Mean (C12): =AVERAGE(B2:B11)
SD (D12):   =STDEV.S(B2:B11)
n (E12):    =COUNT(B2:B11)
z (F12):    =IF(OR(B12="",E12<$H$1),"",IF(D12=0,"",(B12-C12)/D12))
```

The z-score is blank when today is blank, when the count is below `H1`, or when the SD is 0. A plain `=(B12-C12)/D12` turns a blank value today into a z-score.

Python version:

```python
import pandas as pd

WINDOW, MIN_N = 10, 10   # prior tests in baseline, minimum to report: the offered default

def add_z(d, col):
    prior = d[col].shift(1)                      # keep today out of its own baseline
    roll = prior.rolling(WINDOW, min_periods=MIN_N)
    sd = roll.std().replace(0, float("nan"))     # sample SD; an SD of 0 gives a blank z
    d = d.assign(base_mean=roll.mean(), base_sd=sd,
                 base_n=prior.rolling(WINDOW, min_periods=1).count())
    return d.assign(z=(d[col] - d["base_mean"]) / d["base_sd"])

# df: long table with columns athlete_id, date, cmj_cm
df = df.sort_values(["athlete_id", "date"])
out = pd.concat(add_z(d, "cmj_cm") for _, d in df.groupby("athlete_id"))
```

The settings `WINDOW = 10` and `MIN_N = 10` follow this skill's offered default of at least 10 prior values, from the section on choosing a window. They are not published standards. Swinton et al. (2018) say more than 10 to 20 tests may be needed. Set both to the user's choice. Label any value below 10 as the user's choice.

### Calculate it in Power BI and Tableau

These versions follow steps 4 to 9 above. The baseline is the previous k tests for the same athlete, with today left out. A baseline with fewer values than the minimum gives a blank z-score. A baseline SD of 0 gives a blank z-score. A missing test today gives a blank z-score, never a z-score for 0.

The window counts test dates that have a row for the measure, as the spreadsheet and Python versions count rows. A test date with only a reason-coded row takes a place in the window but adds no value, so n can be smaller than k.

Both versions assume one row per athlete, date, measure, and trial in a `measures` table, with the test in `measure_name`, such as `cmj_jump_height`. They use the best trial each day. Use the same summary as the test's TE. Show the results with one athlete and one test date per row. The settings k = 10 and minimum 10 below follow this skill's offered default of at least 10 prior values. They are not published standards.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Use these DAX measures, not calculated columns. Tell the user why: the table has one row per trial, but each result is for one athlete and one test date in the visual. A measure is evaluated in the filter context of the visual. A calculated column is computed once per row at data refresh and does not change with filters or slicers (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options):

```text
Test value (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)

Baseline n =
VAR k = 10
VAR today = MAX ( dates[date] )
VAR priorDates =
    CALCULATETABLE (
        VALUES ( measures[measure_date] ),
        measures[measure_name] = "cmj_jump_height",
        measures[measure_date] < today,
        REMOVEFILTERS ( dates )
    )
VAR lastK = TOPN ( k, priorDates, measures[measure_date], DESC )
VAR vals =
    FILTER (
        ADDCOLUMNS ( lastK, "@v", CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ) ) ),
        NOT ISBLANK ( [@v] )
    )
RETURN COUNTROWS ( vals )

Baseline mean (cm) =
VAR k = 10
VAR today = MAX ( dates[date] )
VAR priorDates =
    CALCULATETABLE (
        VALUES ( measures[measure_date] ),
        measures[measure_name] = "cmj_jump_height",
        measures[measure_date] < today,
        REMOVEFILTERS ( dates )
    )
VAR lastK = TOPN ( k, priorDates, measures[measure_date], DESC )
VAR vals =
    FILTER (
        ADDCOLUMNS ( lastK, "@v", CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ) ) ),
        NOT ISBLANK ( [@v] )
    )
RETURN AVERAGEX ( vals, [@v] )

Baseline SD (cm) =
VAR k = 10
VAR today = MAX ( dates[date] )
VAR priorDates =
    CALCULATETABLE (
        VALUES ( measures[measure_date] ),
        measures[measure_name] = "cmj_jump_height",
        measures[measure_date] < today,
        REMOVEFILTERS ( dates )
    )
VAR lastK = TOPN ( k, priorDates, measures[measure_date], DESC )
VAR vals =
    FILTER (
        ADDCOLUMNS ( lastK, "@v", CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ) ) ),
        NOT ISBLANK ( [@v] )
    )
RETURN IF ( COUNTROWS ( vals ) >= 2, STDEVX.S ( vals, [@v] ) )

z-score =
VAR minN = 10
VAR x = [Test value (cm)]
VAR n = [Baseline n]
VAR sd = [Baseline SD (cm)]
RETURN
    IF (
        HASONEVALUE ( dates[date] ) && NOT ISBLANK ( x ) && n >= minN && sd > 0,
        ( x - [Baseline mean (cm)] ) / sd
    )

z-score status =
VAR minN = 10
VAR rowsToday =
    CALCULATE ( COUNTROWS ( measures ), measures[measure_name] = "cmj_jump_height" )
RETURN
    IF (
        NOT ISBLANK ( rowsToday ),
        SWITCH (
            TRUE (),
            ISBLANK ( [Test value (cm)] ), "no test today",
            [Baseline n] < minN, "baseline too short",
            NOT ( [Baseline SD (cm)] > 0 ), "no variation in baseline",
            "ok"
        )
    )
```

The status is blank on dates with no row for the test, so a table does not list every calendar date. A blank `Baseline n` means no earlier value, and it compares as 0, so the status reads `baseline too short`. Keep the status measure even when the user asks to show nothing below the minimum, so a short baseline reads `baseline too short`, not a blank that looks like missing data. Tell the user that `Baseline SD (cm)` tests the count before it calls `STDEVX.S` because `STDEVX.S` returns an error, not a blank, with fewer than 2 values (https://learn.microsoft.com/en-us/dax/stdevx-s-function-dax).

In Tableau, filter `measure_name` to the test. That filter keeps every row of the test, including reason-coded rows, so each test date is one mark. Put `athlete_id` on Rows and `measure_date` as an exact date on Columns or Detail. Use these calculations:

```text
Test value (cm) (aggregate):
MAX(IF [status] = "ok" AND [unit] = "cm" THEN [value] END)

Has value (aggregate):
IIF(ISNULL([Test value (cm)]), 0, 1)

Baseline n (table calculation):
ZN(WINDOW_SUM([Has value], -10, -1))

Baseline sum (table calculation):
ZN(WINDOW_SUM(ZN([Test value (cm)]), -10, -1))

Baseline sum of squares (table calculation):
ZN(WINDOW_SUM(ZN([Test value (cm)]) * ZN([Test value (cm)]), -10, -1))

Baseline mean (cm) (table calculation):
IF [Baseline n] > 0 THEN [Baseline sum] / [Baseline n] END

Baseline SD (cm) (table calculation):
IF [Baseline n] >= 2
THEN SQRT(MAX(0, ROUND(([Baseline sum of squares] - [Baseline sum] * [Baseline sum] / [Baseline n]) / ([Baseline n] - 1), 9)))
END

z-score (table calculation):
IF ISNULL([Test value (cm)]) OR [Baseline n] < 10 THEN NULL
ELSEIF [Baseline SD (cm)] > 0 THEN ([Test value (cm)] - [Baseline mean (cm)]) / [Baseline SD (cm)]
END

z-score status (table calculation):
IF ISNULL([Test value (cm)]) THEN "no test today"
ELSEIF [Baseline n] < 10 THEN "baseline too short"
ELSEIF ISNULL([Baseline SD (cm)]) OR [Baseline SD (cm)] <= 0 THEN "no variation in baseline"
ELSE "ok"
END
```

For every table calculation, set **Compute Using** to **Specific Dimensions**, check `measure_date` only, and leave `athlete_id` unchecked. The window then moves along each athlete's tests and restarts for each athlete. Do not filter dates with a dimension filter, because it removes earlier tests from the window. Use a table calculation filter to show a shorter range.

At an athlete's first tests, the window reaches back past the first mark and holds fewer than 10 tests. Check one early row by hand: n must equal the number of earlier tests with a value.

Blanks behave this way in each tool:

- Power BI: `STDEVX.S` returns an error, not a blank, with fewer than 2 values. The `>= 2` test stops that. A blank SD compares as 0, so `sd > 0` is false for a blank SD and for a 0 SD.
- Power BI: `TOPN` works on the dates in the data, not on the calendar, so k counts tests, not days.
- Tableau: `ZN` turns missing values into 0 for the sums, and `Has value` counts only real values. The SD is built from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks.
- Both: a text value becomes null on import and is not counted, as `COUNT` skips text in the spreadsheet.

## Worked example

One athlete did a CMJ every 3 days. Judge the test on 2026-09-28 against the 10 tests before it. These are made-up numbers for illustration.

| Date | CMJ (cm) |
|---|---|
| 2026-08-29 | 40.2 |
| 2026-09-01 | 40.7 |
| 2026-09-04 | 41.0 |
| 2026-09-07 | 39.8 |
| 2026-09-10 | 40.6 |
| 2026-09-13 | 40.9 |
| 2026-09-16 | 39.5 |
| 2026-09-19 | 40.3 |
| 2026-09-22 | 41.2 |
| 2026-09-25 | 40.0 |
| 2026-09-28 (today) | 37.6 |

Work through the calculation:

1. Sum of the 10 prior values = 404.20 cm, so the baseline mean = 404.20 / 10 = 40.4200 cm.
2. Deviations from the mean: −0.2200, 0.2800, 0.5800, −0.6200, 0.1800, 0.4800, −0.9200, −0.1200, 0.7800, and −0.4200 cm.
3. Sum of squared deviations = 2.7560 cm². Divide by 9 to get 0.3062 cm².
4. Baseline SD = √0.3062 = 0.5534 cm.
5. z = (37.6 − 40.4200) / 0.5534 = −5.10.
6. Change from the baseline mean = 37.6 − 40.4200 = −2.8200 cm.
7. Noise band with TE = 0.6284 cm from the typical error reference: 1.96 × 0.6284 × √(1 + 1/10) = 1.96 × 0.6284 × 1.0488 = 1.2918 cm.
8. The drop of 2.8200 cm is beyond the band by 2.8200 − 1.2918 = 1.5282 cm. That margin is beyond the SWC of 0.6185 cm from the smallest worthwhile change reference.
9. The TE came from 6 athletes, so t(5) = 2.57 applies. The band becomes 2.5706 × 0.6284 × 1.0488 = 1.6942 cm. The drop is beyond it by 1.1258 cm, so the conclusion does not change.

The Python version above, with `WINDOW = 10` and `MIN_N = 10`, gives the same row for 2026-09-28: `base_n` = 10, `base_mean` = 40.42, `base_sd` = 0.5534, and `z` = −5.10. It leaves `z` blank for the 10 earlier tests, because each has fewer than 10 prior values.

Result: today is 5.10 of the athlete's usual SDs below baseline (window 10 prior tests, n = 10, sample SD). The drop is larger than measurement error, and clearly larger than the SWC. Report it as a flag for the practitioner to review, not as a diagnosis.

## What changes the number

These choices change the z-score for the same athlete on the same day:

- **Including today in the baseline.** Using the last 10 values, today included, gives a mean of 40.1600 cm, an SD of 1.0532 cm, and z = −2.43 instead of −5.10. Today's low value pulls the mean down and inflates the SD.
- **Window length.** With the 4 prior tests, z = −3.71. With 3 prior tests, z = −4.64. Short windows give unstable SDs.
- **Population SD.** `STDEV.P` gives an SD of 0.5250 cm and z = −5.37.
- **Team SD instead of the athlete's SD.** Dividing by the between-athlete SD of 3.0927 cm from the smallest worthwhile change reference gives z = −0.91. That answers a different question.
- **Small n.** An SD from few values is imprecise. Swinton et al. (2018) show that a 95% interval based on a TE from 5 individuals needs a multiplier of 2.78 instead of 1.96.
- **Own SD in place of TE.** The baseline SD also holds biological variation, so a band built on it is never a measurement-error band. With at least 10 stable values, it gives the usual-variation band, `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`, with two states only. With fewer than 10 values, do not build that band.
- **Trend in the baseline.** A baseline should be stable, with low variability and no clear trend (Sands et al., 2019). A rolling baseline that follows a slow decline can hide it. See the example below.
- **Mixed conditions.** A baseline that spans preseason and in-season, or an illness period, changes both the mean and the SD.

This example shows a slow decline that a rolling baseline never flags. One athlete tested 30 times.

Tests 1 to 10 alternate 40.5 and 39.5 cm around 40.0 cm. Tests 11 to 30 fall 0.1 cm per test with the same ±0.5 cm variation, ending at 37.5 cm. These are made-up numbers for illustration:

1. Rolling z against the prior 10 tests never reaches −2. The lowest value is −1.87.
2. Before test 30, the rolling baseline mean has drifted to 38.5500 cm, with an SD of 0.5603 cm.
3. Against the fixed baseline of tests 1 to 10 (mean 40.0000 cm), test 30 is 2.5000 cm lower.
4. That drop is beyond the noise band of 1.2918 cm for n = 10.

Pair a rolling baseline with a fixed reference period, or a trend line, so a slow decline shows up.

## Choose a window and a minimum

No source used in this file sets a best window for an individual baseline. Weir (2005) states there is no consensus on the sample size needed for a stable SEM. Two methods sources point to about 10 values as a floor when noise is estimated from one athlete's own values: Hopkins (2017) says at least 10 for modest precision, and Swinton et al. (2018) say more than 10 to 20 tests may be needed. With 5 values, the 95% interval for the true SD runs from 0.60 to 2.87 times the sample SD. With 10 values, it runs from 0.69 to 1.83 times, and with 28 values, from 0.79 to 1.36 times. These factors come from the chi-square distribution.

Follow these rules instead:

- Ask the user which window and minimum they want. If they have no preference, offer at least 10 prior values as the minimum. Say it is this skill's practice default, based on the two sources above, and state it in every result. If the user sets a window or minimum below 10, use it, label it as the user's choice, and say the two sources above point to about 10 values, so an SD and a z-score from fewer are imprecise.
- Count the window in tests, not days, when tests are irregular. Give the first and last date of each window. If the user gives a test schedule, name each scheduled date in the window with no test.
- Report n with every z-score, and say when n is small.
- Keep the same window for every athlete in one report.

## Units and typical range

The z-score has no units. The baseline mean and SD have the units of the measure.

This file gives no typical z-score range or flag threshold. Thresholds are choices, not facts. Name the threshold and its source.

## Data you need

You need these data to compute an individual baseline:

- Source: repeated values of one measure for one athlete, from the same protocol
- Sampling: a regular testing schedule. Record the date of every test.
- Minimum data: no published minimum exists in the sources for this file. If the user has no minimum, offer at least 10 prior values, as set out in the section on choosing a window. Report n, and treat a baseline built from few values as imprecise.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with baselines and z-scores:

- Including today in its own baseline. Use `shift(1)` in pandas, or a range that ends on the row above.
- Using the team SD, or a squad z-score, as if it were individual change. A squad z-score compares the athlete with teammates on one day. It says nothing about change within the athlete.
- Using the population SD. Use `STDEV.S` or pandas `.std()`.
- Using a window of calendar days with gaps, then calling it "28 days of data". Report the count of values.
- Filling missing days with zero. That drags the mean down and inflates the SD.
- Treating a large z-score as a real change and not checking noise. A z-score uses day-to-day variation, which mixes biological variation and measurement error. Compare the change with the noise band from TE too.
- Using the athlete's own baseline SD as the TE. It mixes biological variation with measurement error. Without a TE, use the usual-variation band.
- Computing an SD from few values. Report n, and use a t multiplier when you build a band from it.
- Applying ±1.5 or ±2 as flag cut points without a source. Name the source, or label the cut point as the user's choice. With a 10-value baseline and pure noise, these flag about 18.6% and 8.9% of tests.
- Reporting squad flags without the number expected by chance. Show results × 5%, or × 2.5% for one direction, next to the flags found.
- Relying only on a rolling baseline. It follows a slow decline and may never flag it. Add a fixed reference period or a trend line.
- Quoting 5% as the false flag rate when only drops matter. With one direction of interest, the chance rate is 2.5%.
- Ignoring direction. For some measures, such as soreness ratings, a higher value is worse. State which direction is a concern.
- Comparing z-scores between athletes as if they share one scale. Each athlete's SD differs.
- Treating ordinal 1 to 5 wellness items as continuous. Ratings are ordered categories, and many ties make the SD tiny and the z-score extreme. For a single item, lead with the raw rating and the change in points, and show any z-score second, labeled approximate. In a simulation run for this skill (stable athletes, 14-day baselines, independent days), the chance rate of z ≤ −2 on one item ranged from 3.3% to 5.6% depending on the athlete's usual answer, against 3.8% expected, and most flags were a one-point drop. A total of five items, or a 0 to 100 scale, came close to the expected rate. Keep single-item z-scores out of squad flag lists. With 5 items and a 14-day baseline, about 17% to 20% of athletes get at least one item flagged on an ordinary day by chance, treating the items as independent: 4 or 5 of 25 athletes, against about 1 on the total. Flag the squad on the total or on the practitioner's own raw-answer rule, and show each item's raw answer and change in points beside each flagged athlete. Keep item z-scores, labeled approximate, in the athlete detail view.

## Example request

> For each player, compare today's jump height with their own last 10 tests and flag anyone who is unusually low. Tell me what window you used.

## Check the result

Run these checks on the result:

- Recompute one athlete's z-score by hand from the window values.
- Confirm today's value is not in its own baseline.
- Confirm every z-score shows its window, n, baseline mean, baseline SD, and units.
- Confirm each change was compared with the noise band from TE, and the band's n, multiplier, and degrees of freedom are stated.
- Confirm squad reports show the flags expected by chance next to the flags found.

## Sources

- Sands W, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone M. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- Hecksteden A, Pitsch W, Julian R, Pfeiffer M, Kellmann M, Ferrauti A, Meyer T. A new method to individualize monitoring of muscle recovery in athletes. International Journal of Sports Physiology and Performance. 2017;12(9):1137-1142. https://doi.org/10.1123/ijspp.2016-0120
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02). The skills use only its error formula, not its magnitude-based inference.
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. International Journal of Epidemiology. 2005;34(1):215-220. https://doi.org/10.1093/ije/dyh299
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. Journal of Strength and Conditioning Research. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- National Institute of Standards and Technology. Dataplot reference manual: prediction limits. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/predlimi.htm (accessed 2026-10-05). Gives the prediction interval mean ± t(n − 1) × s × √(1/n + 1/m) for the mean of m new values, after Hahn GJ, Meeker WQ, Statistical Intervals: A Guide for Practitioners, Wiley, 1991, pp. 61-62. With m = 1, the factor is √(1 + 1/n).
