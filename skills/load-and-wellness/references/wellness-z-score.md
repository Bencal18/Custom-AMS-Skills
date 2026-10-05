# Wellness z-score

Last checked: 2026-10-02

## What it measures

A wellness z-score shows how far today's wellness answer is from that athlete's own usual answers, in units of that athlete's usual day-to-day spread.

In a systematic review, self-reported measures tracked changes in training load more consistently than common objective measures (Saw et al., 2016). Most of the self-reported measures in that review were multi-item questionnaires, such as the Profile of Mood States. Most daily wellness forms use single questions instead. The single items most used in sport have not been validated (Jeffries et al., 2020).

Wellness z-scores are used in team-sport research (Gallo et al., 2016; Govus et al., 2018). A z-score describes an unusual answer. It does not explain the cause.

## Formula

Calculate each athlete and each item separately:

```text
z = (x_today − baseline_mean) ÷ baseline_sd
change_points = x_today − baseline_mean
```

Define every term in the formula:

- `x_today`: today's answer for one item, or today's total score. No unit beyond the form's points.
- `baseline_mean`: the mean of that athlete's previous answers for the same item, over the baseline window. Exclude today.
- `baseline_sd`: the sample standard deviation (SD) of the same baseline answers. SD measures the usual spread around the mean.
- `z`: the result, in SD units. No unit.
- `change_points`: the change from the baseline mean in the form's own points. Show it, and the raw answer, beside every z-score.

Choose and name the variants:

- Total z-score: add the items into a daily total first, then standardize the total against the athlete's baseline of totals. Name it as a total. Use it by default to flag athletes across a squad. Beside each flagged athlete, show each item's raw answer and change in points.
- Item-level z-score: one z-score per question, such as sleep, soreness, fatigue, stress, and mood. Show it in the athlete detail view, labeled approximate, after the raw answer and the change in points. It keeps the reason for a change visible. Do not use it to build a squad flag list.
- Raw-answer flag: the practitioner's own rule on the raw answer, such as any soreness of 1 or 2. It can replace or join the total z-score in a squad flag list. Label it as theirs.
- Rolling baseline: the previous N calendar days, such as 28. It follows slow changes, but it also absorbs a slow decline.
- Fixed baseline: a set period, such as a stable block of normal training. It does not drift, but it becomes out of date.

Read these limits of scoring against the athlete's own baseline:

- A z-score only compares the athlete with themselves. An athlete who always reports high soreness has a z-score near 0 on a day with high soreness. A practitioner may also flag on the raw answer, such as any soreness of 1 or 2. That is their choice. Ask, and label it as theirs.
- A rolling baseline absorbs a slow decline. Each lower answer pulls the mean down, so later answers look normal.
- On a short point scale, z-scores jump in steps. For a single item, report the raw answer and the change in points first, and the z-score second as approximate. In a simulation run for this review (stable athletes, 14-day baselines, independent days), the chance rate of z ≤ −2 on one item ranged from 3.3% to 5.6% depending on the usual answer, against 3.8% expected, and most flags were a one-point drop. Answers can only move in whole points, and a small SD turns one point into a large z-score. In the worked example, a one-point drop on stress from 4 to 3 gives (3 − 3.8571) ÷ 0.3631 = −2.36.

Report chance flags when you flag across a squad:

- Flag the squad on the total z-score or on the practitioner's own raw-answer rule. Keep single-item z-scores out of squad flag lists. Beside each flagged athlete, show each item's raw answer and change in points, so the reason for the flag stays visible.
- Under the assumptions above, a one-direction cut-off of z = −2 flags 2.3% of ordinary days when the baseline mean and SD are known. With a 14-day baseline, the mean and SD are estimates, and the rate rises to 3.8%. These figures come from the normal and t distributions, and the real rate on a 1 to 5 scale can be higher or lower.
- Across 25 athletes flagged on the total, that is 0.57 flags a day by chance with a known baseline, or 0.94 with a 14-day baseline. The chance of at least one flag is 43.7% or 61.8%.
- Flags on single items add up. With 5 items and a 14-day baseline, about 17% to 20% of athletes get at least one item flagged on an ordinary day by chance, treating the items as independent. That is 4 or 5 of 25 athletes a day, against about 1 when you flag on the total. The 17.5% comes from the t distribution: 1 − (1 − 0.0377)^5. A simulation of 1 to 5 answers run for this skill (stable athletes, usual answers from 3 to 4.25, a day-to-day SD of 0.6 to 0.8 points, and independent items and days) gave about 20% for a squad with mixed usual answers. It rose to about 25% for athletes whose usual answer on every item was 4.25.
- Report the number of flags expected by chance next to the number found, for the user's own cut-off.
- Flags on consecutive days against the same baseline are not independent.
- Recommend a repeat answer or a conversation with the athlete before anyone acts on a single flag. An unusually low answer tends to be followed by one closer to the athlete's mean, which is called regression to the mean (Barnett et al., 2005).

Choose the minimum baseline length with the user:

- We found no peer-reviewed source that sets a minimum number of baseline days for wellness z-scores. Ask the user, apply it, and report the number of baseline days with every z-score. If the user has no number, offer 14 baseline answers inside a 28-day window, and label it as this skill's choice. Never offer fewer than 10 answers, and cover at least one full training week. Ten is the same floor the `monitoring-statistics` skill offers for a z-score built on an athlete's own SD. If the user chooses fewer than 10, apply it and label it as the user's choice.
- A baseline should be stable, with low variability and no clear trend (Sands et al., 2019).
- Sands et al. (2019) describe training load as cyclic, with hard and easy days and weekly patterns, and warn that stopping data collection early shows only part of a cycle. They make that point about trend analysis. From it, we infer that a baseline should cover at least one full training week, so hard and easy days are both in it. That is our inference, not their rule.
- A small baseline gives an unstable SD. For normally distributed answers, the 95% confidence interval for the true SD runs from about 0.64 to 2.20 times the sample SD with 7 values, 0.69 to 1.83 times with 10, 0.72 to 1.61 times with 14, and 0.79 to 1.36 times with 28. These factors come from the chi-square distribution.
- The SD factors apply to z. With 14 baseline days, a z-score of −3.13 matches a z-score of about −1.94 to −4.32 against the true SD. That is the z-score multiplied by 0.621 to 1.379.
- The baseline mean is uncertain too. If baseline days are independent and come from a stable baseline, today's distance from a mean of n days has a spread of baseline SD × √(1 + 1/n). This adds the variance of today's answer to the variance of the baseline mean. It is the standard prediction interval for one new value against a mean of n values (NIST, Dataplot reference manual, after Hahn and Meeker, 1991). With n = 14, √(1 + 1/14) = 1.035, so the sleep z-score of −3.13 becomes −3.03 on that scale.
- Short baselines raise the chance flag rate. For a one-direction cut-off of z = −2, an ordinary day is flagged 5.5% of the time with 7 baseline answers, 4.4% with 10, 3.8% with 14, and 3.0% with 28, against 2.3% with a known mean and SD. These figures come from the t distribution and assume normal, independent answers. The real rate can be higher or lower.
- The baseline SD is not a typical error (TE). TE comes from a short-term test-retest study in which no true change is expected, and it measures error only. The baseline SD mixes real day-to-day change with error. A z-score asks whether today is unusual for this athlete, not whether the change exceeds measurement error. Do not use the baseline SD as a TE, and do not borrow a noise band built on TE for wellness answers.
- These intervals assume independent days. Daily answers are often autocorrelated, which means one day's answer tends to resemble the day before. That makes the true intervals wider. Answers on a short point scale, such as 1 to 5, are not normally distributed either, so treat all of these factors as a rough guide only.

Use these spreadsheet formulas, with answers in column `B`, today in row 30, the previous 28 days in rows 2 to 29, and the minimum number of baseline days (2 or more) in cell `H1`. The rows equal 28 calendar days only when every day has its own row, with blank cells on days with no answer:

```text
Baseline count, C30:   =COUNT(B2:B29)
Change in points, D30: =IF(OR(NOT(ISNUMBER(B30)),COUNT(B2:B29)<$H$1),"",B30-AVERAGE(B2:B29))
z-score, E30:          =IF(OR(NOT(ISNUMBER(B30)),COUNT(B2:B29)<$H$1),"",IF(STDEV.S(B2:B29)=0,"",(B30-AVERAGE(B2:B29))/STDEV.S(B2:B29)))
Status, F30:           =IF(B30="","no answer",IF(NOT(ISNUMBER(B30)),"not a number",IF(COUNT(B2:B29)<$H$1,"baseline too short",IF(STDEV.S(B2:B29)=0,"no variation in baseline","ok"))))
```

A text answer today, such as `good` or a number stored as text, gives a blank change and z-score and the status `not a number`. Fix the entry at the source. Text in the baseline rows is not counted as a baseline answer.

A plain `=(B30-AVERAGE(B2:B29))/STDEV.S(B2:B29)` turns a blank answer today into 0. In the worked example that would give a sleep z-score of (0 − 3.9286) ÷ 0.6157 = −6.38 for an athlete who did not answer.

Use this Python function for one athlete and one item, indexed by date:

```python
import numpy as np
import pandas as pd

def wellness_z(item, window, min_baseline):
    """item: one athlete, one item, DatetimeIndex. window: such as "28D". min_baseline >= 2."""
    base = item.rolling(window, closed="left", min_periods=0)
    n, mean, sd = base.count(), base.mean(), base.std(ddof=1)
    short = n < min_baseline
    status = np.select([item.isna(), short, ~(sd > 0)],
                       ["no answer", "baseline too short", "no variation in baseline"], "ok")
    z = ((item - mean) / sd).where(status == "ok")
    return pd.DataFrame({"value": item, "baseline_n": n, "baseline_mean": mean,
                         "baseline_sd": sd, "change_points": (item - mean).mask(short),
                         "z": z, "status": status})
```

### Calculate it in Power BI and Tableau

These versions keep the rules of the spreadsheet formulas above. Today is left out of its own baseline. A blank answer today gives a blank change and z-score, not a z-score for 0 points. A baseline shorter than the minimum gives a blank. A baseline SD of 0 gives a blank z-score. The status says which rule applied.

Both versions use the previous 28 calendar days, not the previous 28 rows. A day with no answer counts as a day in the window but not as a baseline value.

Both versions assume one row per athlete, day, and item in a `measures` table, with the item in `measure_name`, such as `sleep`, and the answer in `value`. Show the results with one athlete and one date per row.

In Power BI, filter the visual to one item. Use a marked date table `dates` related to `measures[measure_date]`, and a whole-number what-if parameter `Min baseline days` with a minimum of 2. Use these DAX measures. They are measures because each one reads a window of earlier days, which a single row cannot hold:

```text
Answer (points) =
IF (
    CALCULATE ( COUNT ( measures[value] ), measures[status] = "ok" ) = 1,
    CALCULATE ( MAX ( measures[value] ), measures[status] = "ok" )
)

Baseline count =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@a", [Answer (points)] ),
        DATESINPERIOD ( dates[date], today - 1, -28, DAY )
    )
RETURN COUNTROWS ( FILTER ( days, NOT ISBLANK ( [@a] ) ) ) + 0

Baseline mean =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@a", [Answer (points)] ),
        DATESINPERIOD ( dates[date], today - 1, -28, DAY )
    )
RETURN AVERAGEX ( FILTER ( days, NOT ISBLANK ( [@a] ) ), [@a] )

Baseline SD =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@a", [Answer (points)] ),
        DATESINPERIOD ( dates[date], today - 1, -28, DAY )
    )
VAR answered = FILTER ( days, NOT ISBLANK ( [@a] ) )
RETURN IF ( COUNTROWS ( answered ) >= 2, STDEVX.S ( answered, [@a] ) )

Change in points =
VAR x = [Answer (points)]
RETURN
    IF (
        HASONEVALUE ( dates[date] ) && NOT ISBLANK ( x )
            && [Baseline count] >= [Min baseline days Value],
        x - [Baseline mean]
    )

z-score =
VAR x = [Answer (points)]
VAR sd = [Baseline SD]
RETURN
    IF (
        HASONEVALUE ( dates[date] ) && NOT ISBLANK ( x )
            && [Baseline count] >= [Min baseline days Value] && sd > 0,
        ( x - [Baseline mean] ) / sd
    )

Status =
SWITCH (
    TRUE (),
    ISBLANK ( [Answer (points)] ), "no answer",
    [Baseline count] < [Min baseline days Value], "baseline too short",
    NOT ( [Baseline SD] > 0 ), "no variation in baseline",
    "ok"
)
```

`Status` and `Baseline count` always return a value, so a table with them lists every date in `dates` for every athlete. Filter the page to the dates you report.

`DATESINPERIOD ( dates[date], today - 1, -28, DAY )` returns the 28 days that end the day before today. `Answer (points)` returns a blank when a day has two answers for the item. Find and fix duplicates at the source.

In Tableau, make a scaffold table with one row for every athlete and every calendar date, starting at least 28 days before the first day you score. Left join `measures` to the scaffold on `athlete_id` and on scaffold `date` equal to `measure_date`. Every day then has a mark, even with no answer. Set the item inside `Item value`, as below. Do not filter `measure_name` on the Filters shelf: that removes the days with no answer, and the window then counts rows, not days. Make an integer parameter `Min baseline days` with a minimum of 2. Use these calculations:

```text
Item value (row-level):
IF [measure_name] = "sleep" AND [status] = "ok" THEN [value] END

Answer (points) (aggregate):
IF COUNT([Item value]) = 1 THEN MIN([Item value]) END

Answered (aggregate):
IIF(ISNULL([Answer (points)]), 0, 1)

Baseline count (table calculation):
ZN(WINDOW_SUM([Answered], -28, -1))

Baseline sum (table calculation):
ZN(WINDOW_SUM(ZN([Answer (points)]), -28, -1))

Baseline sum of squares (table calculation):
ZN(WINDOW_SUM(ZN([Answer (points)]) * ZN([Answer (points)]), -28, -1))

Baseline mean (table calculation):
IF [Baseline count] > 0 THEN [Baseline sum] / [Baseline count] END

Baseline SD (table calculation):
IF [Baseline count] >= 2
THEN SQRT(MAX(0, ROUND(([Baseline sum of squares] - [Baseline sum] * [Baseline sum] / [Baseline count]) / ([Baseline count] - 1), 9)))
END

Change in points (table calculation):
IF ISNULL([Answer (points)]) OR [Baseline count] < [Min baseline days] THEN NULL
ELSE [Answer (points)] - [Baseline mean]
END

z-score (table calculation):
IF ISNULL([Answer (points)]) OR [Baseline count] < [Min baseline days] THEN NULL
ELSEIF [Baseline SD] > 0 THEN ([Answer (points)] - [Baseline mean]) / [Baseline SD]
END

Status (table calculation):
IF ISNULL([Answer (points)]) THEN "no answer"
ELSEIF [Baseline count] < [Min baseline days] THEN "baseline too short"
ELSEIF ISNULL([Baseline SD]) OR [Baseline SD] <= 0 THEN "no variation in baseline"
ELSE "ok"
END
```

Put `athlete_id` on Rows and the scaffold `date` as an exact day on Columns or Detail. For every table calculation, set **Compute Using** to **Specific Dimensions**, check `date` only, and leave `athlete_id` unchecked. The window then moves along the days and restarts for each athlete. In a nested calculation such as `z-score`, set the same Compute Using for each nested field in the dialog.

Do not filter dates with a dimension filter. It removes the earlier days from the window. To show a shorter date range, use a table calculation filter, such as a filter on `LOOKUP(MIN([date]), 0)`.

The SD is built from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks. `ROUND(..., 9)` and `MAX(0, ...)` stop rounding error from hiding a zero SD.

Blanks behave this way in each tool:

- Power BI: `STDEVX.S` returns an error, not a blank, with fewer than 2 values. The `>= 2` test stops that. A missing answer today gives a blank `x`, so the change in points and the z-score are blank, and the status reads `no answer`.
- Power BI: a blank compares as 0, so `NOT ( [Baseline SD] > 0 )` is true for a blank SD as well as a 0 SD. The baseline-length test comes first, so a blank SD from a short baseline reads `baseline too short`.
- Tableau: `ZN` turns the missing days into 0 for the sums, and `Answered` counts only the days with an answer. A null answer today gives a null change and z-score.
- Both: a text answer becomes null on import and counts as no answer. The spreadsheet also leaves the change and z-score blank for it, but its status reads `not a number`.

## Calculate the wellness z-score

Follow these steps to calculate the metric from raw inputs:

1. Load one row per athlete per day with `athlete_id`, `date`, and one column per item, such as `sleep`, `soreness`, `fatigue`, `stress`, and `mood` (form points, such as 1 to 5).
2. Confirm each item's direction with the user. Flip any item where a high number is bad, so that a high number is good for every item. On a 1 to 5 scale, flipped = 6 − answer.
3. Ask the user for the baseline window and the minimum number of baseline days.
4. Ask the user whether they also flag on the raw answer, and at what level.
5. For each athlete, item, and day, take the answers from the baseline window before that day. Exclude the day being scored.
6. Count the baseline answers. If the count is below the minimum, report "baseline too short" with the count, and stop for that day.
7. Calculate the baseline mean, the change in points, and the sample SD of the baseline answers.
8. If the SD is 0, report "no variation in baseline" and the change in points, and stop for that day.
9. Calculate z = (today's answer − baseline mean) ÷ baseline SD.
10. For a total z-score, add the flipped items into a daily total first, then repeat steps 5 to 9 on the totals.
11. For a squad flag list, flag on the total z-score or on the practitioner's raw-answer rule, not on single-item z-scores. Beside each flagged athlete, show each item's raw answer and change in points, with the total z-score, status, baseline window, and baseline day count.
12. In the athlete detail view, report each item's raw answer, change in points, z-score labeled approximate, status, baseline window, and baseline day count.

## Worked example

One athlete answers a 1 to 5 form each morning, where 5 is best for every item. The baseline is the 14 mornings before today.

| Item | Baseline answers, 14 days | Today |
|---|---|---|
| Sleep | 4, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 3, 4, 4 | 2 |
| Soreness | 3, 4, 4, 3, 4, 3, 3, 4, 3, 4, 4, 3, 3, 4 | 3 |
| Fatigue | 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3 | 4 |
| Stress | 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4 | 4 |
| Mood | 4, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4 | 4 |

Item z-scores:

| Item | Today | Baseline mean | Change (points) | Baseline SD | z |
|---|---|---|---|---|---|
| Sleep | 2 | 3.93 | −1.93 | 0.62 | −3.13 |
| Soreness | 3 | 3.50 | −0.50 | 0.52 | −0.96 |
| Fatigue | 4 | 3.64 | 0.36 | 0.50 | 0.72 |
| Stress | 4 | 3.86 | 0.14 | 0.36 | 0.39 |
| Mood | 4 | 4.14 | −0.14 | 0.36 | −0.39 |

Sleep z = (2 − 3.9286) ÷ 0.6157 = −3.13. Use the unrounded mean and SD. The rounded values in the table give −3.11. Today's sleep answer is about 2 points, or about 3 baseline SDs, below this athlete's usual answer.

Total z-score:

- Baseline daily totals: 19, 19, 19, 19, 20, 19, 18, 19, 19, 21, 19, 18, 19, 19.
- Baseline total mean: 19.07. Baseline total SD: 0.73.
- Today's total: 2 + 3 + 4 + 4 + 4 = 17.
- Total z = (17 − 19.0714) ÷ 0.7300 = −2.84.

The item z-scores show that the low total comes from sleep, with a smaller drop in soreness.

The Python snippet run on the sleep answers, dated 2026-09-01 to 2026-09-15, with a 14-day window and a minimum of 10 baseline days, gives these rows:

| Date | Value | `baseline_n` | `baseline_mean` | `change_points` | `z` | `status` |
|---|---|---|---|---|---|---|
| 2026-09-01 | 4 | 0 | missing | missing | missing | baseline too short |
| 2026-09-10 | 4 | 9 | 4.00 | missing | missing | baseline too short |
| 2026-09-11 | 4 | 10 | 4.00 | 0.00 | 0.00 | ok |
| 2026-09-12 | 3 | 11 | 4.00 | −1.00 | −1.58 | ok |
| 2026-09-15 | 2 | 14 | 3.93 | −1.93 | −3.13 | ok |

## What changes the number

These choices change the result even when the athlete has not changed:

- Baseline length. With the last 10 days as the baseline, today's sleep z-score is −3.35 (mean 3.90, SD 0.57) instead of −3.13 with 14 days.
- Including today in the baseline. Adding today's answer to the 14-day sleep baseline shrinks the z-score from −3.13 to −2.32.
- Item versus total. In the worked example, the total z-score is −2.84. The plain mean of the five item z-scores is −0.68. These are different variants. Name the one you report.
- Size of the baseline SD. An answer of 3 gives z = −2.36 on stress (mean 3.86, SD 0.36) but −0.96 on soreness (mean 3.50, SD 0.52). A small SD turns a small change in points into a large z-score.
- Rolling versus fixed baseline. A rolling baseline moves with the athlete. A slow decline lowers the baseline mean, so later answers look less unusual.
- Chronic problems. An athlete whose 14 soreness answers were mostly 1 and 2 (mean 1.29, SD 0.47) gets z = −0.61 for a 1, the worst answer on the form.
- Scale direction. If one item runs the other way and is not flipped, its z-score has the wrong sign and the total is wrong.
- Zero spread. An athlete who answered 4 on all 14 stress mornings has a baseline SD of 0, so any z-score for stress is undefined. The change in points shows: a 3 is −1.0 point.
- Form changes. A new question wording or scale starts a new baseline.

## Units and typical range

A z-score has no unit. Zero means today equals the athlete's baseline mean. The sign depends on the item's scale direction.

| Population | Typical range | Source |
|---|---|---|
| Any athlete | No validated flag cut-off. The most used single wellness items have no validation studies. Use the cut-off the practitioner chose, and label it as their choice. | Jeffries et al., 2020 |

## Data you need

Collect this data:

- Source: a daily wellness form or app, filled in before training.
- Sampling: one answer per item per athlete per day, at the same time of day.
- Minimum data: the minimum number of baseline days the user chose. If the user has none, offer 14 answers inside 28 days, and never fewer than 10 answers covering at least one full training week. This is the skill's choice, partly inferred from Sands et al. (2019), not their rule.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using the team mean and SD. A team baseline mixes athletes who use the scale differently. Use each athlete's own baseline.
- Including today in the baseline. Today's answer then pulls the mean toward itself and shrinks the z-score. Exclude today.
- Ignoring scale direction. Forms differ. In Gastin et al. (2013), 1 was the positive end. In Govus et al. (2018), a higher soreness score meant less sore. Confirm each item's direction, and flip items so that the sign means the same thing for every item.
- Adding items that run in opposite directions into one total. Flip them first, or do not total them.
- Reporting only the total. A good sleep score can cancel a bad soreness score. Show each item's raw answer and change in points beside the total.
- Building a squad flag list from single-item z-scores. With 5 items, about 17% to 20% of athletes get at least one item flagged on an ordinary day by chance, or 4 or 5 of 25. Flag the squad on the total or on the practitioner's raw-answer rule. Keep item z-scores, labeled approximate, in the athlete detail view.
- Reporting only the z-score. On a 1 to 5 scale, a z-score of −2.36 can be a one-point change. Show the raw answer and the change in points beside it.
- Relying only on the athlete's own baseline. An athlete who always reports high soreness never looks unusual. Ask whether the practitioner also flags on the raw answer.
- Treating the total as a validated scale. Most wellness forms use single-item questions. The most common single items in sport have not been validated, and modified versions are common (Jeffries et al., 2020; Duignan et al., 2020).
- Letting a blank answer become 0. A spreadsheet formula without a blank check turns a missing answer into a large negative z-score. Check for blanks first.
- Dividing by zero. An athlete who always answers 4 has an SD of 0, and the z-score is undefined. Report "no variation in baseline" instead of a number.
- Reporting z-scores before the minimum baseline is met. Show "baseline too short" and the number of days.
- Using a fixed cut-off, such as −1 or −1.5, as if it were validated. Ask the user which cut-off they use.
- Reporting squad flags without the chance count. With 25 athletes flagged on the total, a cut-off of −2 gives 0.57 to 0.94 flags a day by chance alone. Show the expected number next to the number found.
- Filling missing days with the athlete's mean. This shrinks the SD and inflates later z-scores. Leave them missing.
- Treating a low z-score as a diagnosis. It flags an answer to follow up with the athlete. It does not identify illness, injury, or overtraining.

## Example request

> Our players fill in a 1 to 5 wellness form every morning: sleep, soreness, fatigue, stress, and mood. Build me a sheet that flags anyone who is well below their own normal today.

## Check the result

Run these checks:

- Recalculate one athlete-item z-score by hand from the listed baseline values. Confirm today is not in the baseline.
- Confirm each z-score shows the raw answer, the change in points, the baseline window, the baseline day count, and a status.
- Confirm that blank answers, text answers, short baselines, and zero-SD baselines show as blank with a status, not as a number.
- Confirm that for every item a negative z-score means the same thing, worse or better, as stated in the output.

## Sources

This file cites these sources:

- Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. Br J Sports Med. 2016;50(5):281-291. https://doi.org/10.1136/bjsports-2015-094758
- Gastin PB, Meyer D, Robinson D. Perceptions of wellness to monitor adaptive responses to training and competition in elite Australian football. J Strength Cond Res. 2013;27(9):2518-2526. https://doi.org/10.1519/JSC.0b013e31827fd600
- Gallo TF, Cormack SJ, Gabbett TJ, Lorenzen CH. Pre-training perceived wellness impacts training output in Australian football players. J Sports Sci. 2016;34(15):1445-1451. https://doi.org/10.1080/02640414.2015.1119295
- Govus AD, Coutts A, Duffield R, Murray A, Fullagar H. Relationship between pretraining subjective wellness measures, player load, and rating-of-perceived-exertion training load in American college football. Int J Sports Physiol Perform. 2018;13(1):95-101. https://doi.org/10.1123/ijspp.2016-0714
- Jeffries AC, Wallace L, Coutts AJ, McLaren SJ, McCall A, Impellizzeri FM. Athlete-reported outcome measures for monitoring training responses: a systematic review of risk of bias and measurement property quality according to the COSMIN guidelines. Int J Sports Physiol Perform. 2020;15(9):1203-1215. https://doi.org/10.1123/ijspp.2020-0386
- Duignan C, Doherty C, Caulfield B, Blake C. Single-item self-report measures of team-sport athlete wellbeing and their relationship with training load: a systematic review. J Athl Train. 2020;55(9):944-953. https://doi.org/10.4085/1062-6050-0528.19
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-220. https://doi.org/10.1093/ije/dyh299
- Sands WA, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone MH. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- National Institute of Standards and Technology. Dataplot reference manual: prediction limits. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/predlimi.htm (accessed 2026-10-02). Gives the prediction interval for the mean of m new values as mean ± t × s × √(1/n + 1/m), after Hahn GJ, Meeker WQ, Statistical Intervals, Wiley, 1991, pages 61-62. With m = 1, the factor is √(1 + 1/n).
