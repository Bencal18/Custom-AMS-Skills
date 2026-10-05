# Smallest worthwhile change

Last checked: 2026-10-02

## What it measures

The smallest worthwhile change (SWC) is the smallest change in a measure that matters in practice. It answers "is this change big enough to care about?", not "is this change real?" (Swinton et al., 2018).

## Formula

Use the between-athlete variant by default:

```text
SWC = 0.2 × SD_between
```

Define every term in the formula:

- `SD_between`: the sample standard deviation of the measure across athletes in the group at baseline, in the units of the measure (Swinton et al., 2018)
- `0.2`: the threshold for a small standardized effect (Hopkins, 2000; Hopkins et al., 2009)
- `SWC`: the smallest worthwhile change, in the units of the measure

Use these variants when they fit the question:

- **Between-athlete variant, 0.2 × SD.** Use it for fitness tests, jump tests, strength tests, and most team monitoring. This is the default (Hopkins, 2000; Swinton et al., 2018).
- **True-score variant.** The observed SD holds some measurement noise. To remove it, use `SWC = 0.2 × √(SD_between² − TE²)` (Hopkins, 2000). It gives a slightly smaller SWC. Name it if you use it.
- **Competition performance variant.** For a top athlete's competition time or distance, use 0.3 × the athlete's typical variation between competitions (Hopkins et al., 2009). Use it only for real competition results, not training tests. On this scale, the thresholds for small, moderate, large, very large, and extremely large are 0.3, 0.9, 1.6, 2.5, and 4.0 × within-athlete variation (Hopkins et al., 2009). Do not mix them with the 0.2, 0.6, 1.2, 2.0, and 4.0 × SD scale below.
- **Practitioner variant.** The coach or practitioner sets the SWC from experience with similar athletes (Swinton et al., 2018). Record the value and who chose it.
- **Larger thresholds.** For moderate, large, very large, and extremely large changes, use 0.6, 1.2, 2.0, and 4.0 × SD_between (Hopkins et al., 2009).

Treat 0.2 × SD as a convention, not a law. These caveats apply:

- It depends on how alike the squad is. A more varied squad gives a larger SWC for the same test.
- It is imprecise in small squads, because an SD from a few athletes is itself uncertain. Report the number of athletes.
- The observed SD between athletes includes measurement error. The corrected SD is `√(SD² − TE²)`, which gives the true-score variant above (Hopkins, 2000).

To judge one athlete's change, compare it with both the noise and the SWC (Buchheit, 2014). Build an interval around the change:

```text
interval = change ± z × √2 × TE          (two single tests)
interval = change ± z × TE × √(1 + 1/n)  (a new value against a baseline mean of n values)
```

The half-width is the noise band. Error alone gives a change smaller than this about 95 percent of the time at z = 1.96. For two single tests, n = 1, and the band is 1.96 × √2 × TE, about 2.77 × TE.

The second form adds variances. Hopkins (2017) uses the same error for a change from the mean of several tests. The individual baselines and z-scores reference explains this form and its assumptions.

Define every term in the interval:

- `change`: new value minus baseline value, in the units of the measure
- `TE`: typical error of the test, in the units of the measure. See the typical error reference.
- `z`: 1.96 for 95% confidence, or 1.645 for 90% confidence (Swinton et al., 2018; Weir, 2005). This skill uses 95% as its default when the user has no preference. That default is a choice that matches common MDC95 reporting, not a published rule for monitoring.
- `n`: the number of values in the baseline mean. Use n = 1 when the baseline is one test.

With z = 1.96, error alone pushes a change past the band in either direction about 5% of the time. When only one direction matters, such as a drop, the chance rate of a false flag is 2.5%, not 5%.

Label the change with the first row that fits:

| Interval result | Label |
|---|---|
| The interval includes zero. | Unclear: inside measurement noise. |
| The interval is entirely beyond the SWC, in one direction. | Real, and at least as large as the SWC. |
| The interval excludes zero but stays inside ±SWC. | Real, but smaller than the SWC. |
| The interval excludes zero and crosses the SWC. | Real, possibly as large as the SWC. |

This follows the rule that a change counts as worthwhile when its interval lies beyond the SWC (Swinton et al., 2018). Batterham and Hopkins (2006) describe a related probability method. A change is clearly larger than the SWC only when the change minus the noise band is beyond the SWC, in the chosen direction.

Write "larger than measurement error; may or may not be worthwhile" for a change beyond the noise band but not clearly beyond the SWC. Name the rule and the confidence level you used.

If TE comes from few athletes, replace z with t. Take the degrees of freedom from the TE study: athletes − 1 for two trials, or (athletes − 1) × (trials − 1) for the two-way model.

TE from 6 athletes gives t(5) = 2.57. TE from 10 athletes gives t(9) = 2.26 (Swinton et al., 2018).

## Calculate the SWC and label a change

Follow these steps to calculate the SWC and label each change:

1. Pick the baseline test date and the comparison group, such as the same sex, level, and position group.
2. Collect one baseline value per athlete in a column such as `baseline_value`, in the units of the measure.
3. Compute the sample SD of `baseline_value`, dividing by n − 1.
4. Multiply the SD by 0.2. The result is the SWC, in the units of the measure.
5. For each athlete, compute `change = new_value − baseline_value`.
6. Get the typical error (TE) for the test, in the same units.
7. Compute the half-width `z × √2 × TE` for the chosen confidence level. If the baseline is a mean of n values, use `z × TE × √(1 + 1/n)`.
8. Compute the interval: `change − half-width` to `change + half-width`.
9. Label the change with the table above.

Spreadsheet version, with baseline values in `B2:B21`, new values in `C2:C21`, TE in `F1`, and SWC in `F2`. The change, half-width, and limits return a blank when an input they need is blank or not a number, so a blank TE never collapses the band to 0:

```text
SWC (F2):         =0.2*STDEV.S(B2:B21)
Change (D2):      =IF(COUNT(B2,C2)<2,"",C2-B2)
Half-width (F3):  =IF(ISNUMBER(F1),1.96*SQRT(2)*F1,"")
Lower (E2):       =IF(OR(D2="",$F$3=""),"",D2-$F$3)
Upper (G2):       =IF(OR(D2="",$F$3=""),"",D2+$F$3)
```

Python version:

```python
import math

Z = {0.90: 1.645, 0.95: 1.960}

def classify_change(change, te, swc, level=0.95):
    half = Z[level] * math.sqrt(2) * te
    lo, hi = change - half, change + half
    if lo <= 0 <= hi:
        return lo, hi, "unclear: inside measurement noise"
    if min(abs(lo), abs(hi)) >= swc:
        return lo, hi, "real, and at least as large as the SWC"
    if max(abs(lo), abs(hi)) < swc:
        return lo, hi, "real, but smaller than the SWC"
    return lo, hi, "real, possibly as large as the SWC"

print(classify_change(2.6, te=0.6284, swc=0.6185))
```

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. The SWC uses only athletes with a baseline value, and it is blank with fewer than 2 of them. A missing baseline or new value gives a blank change. A missing TE gives a blank half-width, never a band of 0.

Both versions assume one row per athlete, date, measure, and trial in a `measures` table, and a `reliability` table with one row per measure: `measure_name`, `te`, `te_df`, and `te_source`. The user picks the baseline and the new test dates. Show the results with one athlete per row. The SWC uses every athlete the filters and slicers leave in the view, so set the comparison group with those filters.

In Power BI, add two single-select date slicers on two tables that are not related to anything, `baseline_pick` and `new_pick`, each with one `date` column. Use these DAX measures. They are measures because they combine dates chosen in slicers and, for the SWC, all athletes in the group:

```text
Test value (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)

Baseline value (cm) =
VAR d = SELECTEDVALUE ( baseline_pick[date] )
RETURN
    IF ( NOT ISBLANK ( d ), CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ), dates[date] = d ) )

New value (cm) =
VAR d = SELECTEDVALUE ( new_pick[date] )
RETURN
    IF ( NOT ISBLANK ( d ), CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ), dates[date] = d ) )

SWC (cm) =
VAR vals =
    FILTER (
        ADDCOLUMNS ( ALLSELECTED ( athletes[athlete_id] ), "@b", [Baseline value (cm)] ),
        NOT ISBLANK ( [@b] )
    )
RETURN IF ( COUNTROWS ( vals ) >= 2, 0.2 * STDEVX.S ( vals, [@b] ) )

Change (cm) =
VAR b = [Baseline value (cm)]
VAR n = [New value (cm)]
RETURN IF ( NOT ISBLANK ( b ) && NOT ISBLANK ( n ), n - b )

Half-width (cm) =
VAR te = LOOKUPVALUE ( reliability[te], reliability[measure_name], "cmj_jump_height" )
RETURN IF ( NOT ISBLANK ( te ) && te > 0, 1.96 * SQRT ( 2 ) * te )

Lower (cm) =
VAR c = [Change (cm)]
VAR h = [Half-width (cm)]
RETURN IF ( NOT ISBLANK ( c ) && NOT ISBLANK ( h ), c - h )

Upper (cm) =
VAR c = [Change (cm)]
VAR h = [Half-width (cm)]
RETURN IF ( NOT ISBLANK ( c ) && NOT ISBLANK ( h ), c + h )
```

For a baseline that is a mean of n values, replace `SQRT ( 2 )` with `SQRT ( 1 + 1 / n )`.

In Tableau, relate `reliability` to `measures` on `measure_name`. The half-width picks the CMJ row of `reliability` itself, because the view does not filter `measure_name`. Make two date parameters, `Baseline date` and `New date`. Put `athlete_id` on Rows. Use these calculations:

```text
Baseline value (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" AND [measure_date] = [Baseline date] THEN [value] END)

New value (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" AND [measure_date] = [New date] THEN [value] END)

Baseline count (table calculation):
WINDOW_SUM(IIF(ISNULL([Baseline value (cm)]), 0, 1))

SWC (cm) (table calculation):
IF [Baseline count] < 2 THEN NULL
ELSE 0.2 * SQRT(MAX(0, ROUND(
    (WINDOW_SUM(ZN([Baseline value (cm)]) * ZN([Baseline value (cm)]))
     - WINDOW_SUM(ZN([Baseline value (cm)])) * WINDOW_SUM(ZN([Baseline value (cm)])) / [Baseline count])
    / ([Baseline count] - 1), 9)))
END

Change (cm) (aggregate):
IF ISNULL([Baseline value (cm)]) OR ISNULL([New value (cm)]) THEN NULL
ELSE [New value (cm)] - [Baseline value (cm)]
END

TE (cm) (aggregate of a FIXED LOD):
MIN({ FIXED : MIN(IF [measure_name (reliability)] = "cmj_jump_height" THEN [te] END) })

Half-width (cm) (aggregate):
IF ISNULL([TE (cm)]) OR [TE (cm)] <= 0 THEN NULL ELSE 1.96 * SQRT(2) * [TE (cm)] END

Lower (cm) (aggregate):
IF ISNULL([Change (cm)]) OR ISNULL([Half-width (cm)]) THEN NULL ELSE [Change (cm)] - [Half-width (cm)] END

Upper (cm) (aggregate):
IF ISNULL([Change (cm)]) OR ISNULL([Half-width (cm)]) THEN NULL ELSE [Change (cm)] + [Half-width (cm)] END
```

Set **Compute Using** for `Baseline count` and `SWC (cm)` to `athlete_id`. The SWC then uses every athlete in the view, which is the comparison group. The SD is built from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks.

Blanks behave this way in each tool:

- Power BI: `STDEVX.S` skips blank baselines, but it returns an error with fewer than 2 values. The `>= 2` test stops that. A blank TE gives a blank half-width, so lower and upper are blank too.
- Tableau: an athlete with no baseline gets a null value, and `Baseline count` leaves that athlete out of the SWC. A null TE gives a null half-width.
- Both: text in the baseline column becomes null on import, so the SWC uses the remaining athletes, as `STDEV.S` skips text in the spreadsheet.

## Worked example

Eight athletes did a preseason countermovement jump (CMJ). The test's TE is 0.6284 cm, from the worked example in the typical error reference. These are made-up numbers for illustration.

| Input | Value |
|---|---|
| Baseline CMJ (cm) | 36.4, 41.2, 38.9, 44.0, 35.1, 40.3, 42.7, 37.6 |
| TE | 0.6284 cm |
| Confidence level | 95%, z = 1.96 (default) |

Work through the SWC:

1. Baseline mean = 39.5250 cm.
2. Sample SD between athletes = 3.0927 cm.
3. SWC = 0.2 × 3.0927 = 0.6185 cm.
4. Half-width = 1.96 × 1.4142 × 0.6284 = 1.7418 cm.

Label four athletes' changes:

| Athlete | Change (cm) | Interval (cm) | Label |
|---|---|---|---|
| A | −0.9 | −2.6418 to 0.8418 | Unclear: inside measurement noise |
| B | +2.6 | 0.8582 to 4.3418 | Real, and at least as large as the SWC |
| C | +2.1 | 0.3582 to 3.8418 | Real, possibly as large as the SWC |
| D | +1.3 | −0.4418 to 3.0418 | Unclear: inside measurement noise |

Athlete B is clearly larger than the SWC: 2.6 − 1.7418 = 0.8582 cm, which is beyond 0.6185 cm. Athlete C is larger than measurement error, but 2.1 − 1.7418 = 0.3582 cm is not beyond the SWC, so C may or may not be worthwhile.

Athlete D's change of 1.3 cm is twice the SWC, but it sits inside the noise. Here TE is about the same size as the SWC, so this test only detects changes well above the SWC.

The TE came from 6 athletes, so t(5) = 2.5706 strictly applies. The half-width becomes 2.2845 cm.

Athlete B's interval becomes 0.3155 to 4.8845 cm, "real, possibly as large as the SWC". Athlete C's interval becomes −0.1845 to 4.3845 cm, inside the noise. A TE from more athletes would narrow the band.

## What changes the number

These choices change the result even when the athletes do not change:

- **Population SD instead of sample SD.** In the worked example, `STDEV.P` gives an SD of 2.8930 cm and an SWC of 0.5786 cm instead of 0.6185 cm.
- **Mixing populations.** Adding two higher-jumping athletes at 52.5 cm and 55.0 cm raises the SD to 6.6151 cm and the SWC to 1.3230 cm, more than double.
- **True-score variant.** Removing the noise gives 0.2 × √(3.0927² − 0.6284²) = 0.6056 cm.
- **Confidence level.** At 90%, the half-width shrinks from 1.7418 cm to 1.4619 cm. Athlete C's interval becomes 0.6381 to 3.5619 cm, and the label changes to "real, and at least as large as the SWC".
- **Baseline date.** A baseline taken after a training block, or a different set of athletes, gives a different SD. Fix the baseline and state it.
- **Which TE you use.** A TE from a different protocol, or from tests weeks apart, changes every interval.

## Units and typical range

SWC has the same units as the measure. If you work in percent, express both the change and the SWC in percent.

This file gives no typical SWC values. The SWC depends on how varied your group is. Compute it from your own baseline data and report the group it came from.

## Data you need

You need these data to compute the SWC:

- Source: one baseline value per athlete for the same test and protocol
- Group: athletes comparable to the athlete you judge, such as the same sex, level, and position group
- Minimum data: the sources for this file publish no minimum number of athletes. Report the number of athletes the SD came from.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with the SWC:

- Treating the SWC as the noise threshold. The SWC says whether a change matters. Typical error says whether it is real. Check both.
- Using the SD of change scores. Use the SD of baseline values between athletes.
- Using one athlete's own day-to-day SD. That gives a z-score, not an SWC. See the individual baselines and z-scores reference.
- Mixing populations. An SD from a mixed squad of men and women, or starters and academy players, inflates the SWC. Use a comparable group.
- Using the population SD. Use `STDEV.S`, not `STDEV.P`.
- Recomputing the SWC every week from new data. The threshold then drifts. Fix the baseline period and state it.
- Mixing units. Do not compare a change in percent with an SWC in centimeters.
- Calling a change worthwhile because it exceeds the SWC while its interval includes zero. Check noise first.
- Using one athlete's own baseline SD as the TE. That SD mixes biological variation with measurement error, and from a few values it needs a t multiplier. Use a TE from test-retest data.

## Example request

> Here are preseason sprint times for 22 players and their times today. Which players changed by more than the smallest worthwhile change, and which changes are only noise? Our 10 m sprint typical error is 0.03 s.

## Check the result

Run these checks on the result:

- Confirm the SWC is 0.2 × the baseline SD, and the SD came from the stated group and date.
- Confirm each label matches its interval. Recompute one athlete by hand.
- Confirm you reported TE, SWC, the confidence level, and the units next to each label.

## Sources

- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. Medicine and Science in Sports and Exercise. 2009;41(1):3-13. https://doi.org/10.1249/MSS.0b013e31818cb278
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02)
- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. Journal of Strength and Conditioning Research. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- Batterham AM, Hopkins WG. Making meaningful inferences about magnitudes. International Journal of Sports Physiology and Performance. 2006;1(1):50-57. https://doi.org/10.1123/ijspp.1.1.50
- Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? Frontiers in Physiology. 2014;5:73. https://doi.org/10.3389/fphys.2014.00073
