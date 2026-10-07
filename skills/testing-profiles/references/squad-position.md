# Position within the squad and position group

Last checked: 2026-10-07

## What it measures

Position within the squad shows where one athlete's result on one test sits among the squad's results from the same test day, as a percentile and in SD units, with measurement error beside each value.

Coaches often make these comparisons. In a survey of elite male soccer practitioners, 73 answered the data analysis questions. Of those, 68% compared results with normative data or benchmarks, and 52% used position-specific comparisons. Only 38% took any form of measurement error into account (Asimakidis et al., 2024).

It describes where the athlete sits. It does not rate the athlete, rank the squad, or make a training decision. Keep the rules in the [`testing-profiles` skill](../SKILL.md#decline-a-ranking-request): no ordered list, no rank numbers, and no composite score across tests.

## Formula

Use two numbers for each athlete and test. Show both, with measurement error beside each.

### Percentile, definition C

A percentile rank is the percentage of scores in a group that sit below a given score. Three definitions are in use. Definition A counts scores below. Definition B counts scores at or below. Definition C counts scores below plus half of the scores equal to it (Crawford et al., 2009). Crawford et al. (2009) recommend definition C and give this formula, which they credit to Ley (1972):

```text
percentile = 100 × (m + 0.5 × k) / N
```

Define every term in the formula:

- `m`: the number of athletes in the group with a lower score than this athlete.
- `k`: the number of athletes in the group with the same score, counting this athlete.
- `N`: the number of athletes in the group with a result on this test day. Athletes who did not test are not in `N`.
- `percentile`: the percentage of the group below this athlete, with ties split in half, from 0 to 100.

Definition C is this skill's choice among the three, based on that recommendation. This skill uses definition C for every group. The athlete belongs to the squad, so the athlete counts in `k` and `N`. With these counts, no athlete in the group gets 0 or 100.

Built-in functions use other definitions, so they give other numbers for the same data:

- Excel `PERCENTRANK.INC` returns a value from 0 to 1 inclusive and keeps 3 digits by default. In Microsoft's example data (13, 12, 11, 8, 4, 3, 2, 1, 1, 1), it returns 0.333 for the value 2 (Microsoft, `PERCENTRANK.INC`). Definition C gives 100 × (3 + 0.5 × 1) / 10 = 35.
- Tableau `RANK_PERCENTILE` ranks the values (6, 9, 9, 14) as 0.00, 0.67, 0.67, and 1.00 (Tableau, table calculation functions). Definition C gives 12.5, 50, 50, and 87.5.

Do not use these built-in functions. Use the `COUNTIF` formulas below, and name definition C next to every percentile.

### Step size

```text
step = 100 / N
```

The step is the smallest gap between two possible percentiles. With 12 athletes, one place in the squad moves the percentile by 8.3 points. With 5 athletes, it moves it by 20 points. Print the step next to every percentile.

### SD units

```text
SD units = (x − group mean) / group SD
```

Define every term in the formula:

- `x`: the athlete's result, in the units of the test.
- `group mean`: the mean of the group's results on this test day, with this athlete included.
- `group SD`: the sample standard deviation (SD) of the same results, with `n − 1` in the denominator.
- `SD units`: how far the athlete sits from the group mean, in units of the group's spread. 0 is the group mean.

These are the same SD units as the profile dot plot in the relationships reference of the `athlete-data-visualization` skill. They are not the z-score against the athlete's own baseline in the individual baselines reference of the `monitoring-statistics` skill. Do not call them z-scores in a coach report. Say "SD units from the squad mean".

A gap of 0.2 SD units from the group mean equals the default smallest worthwhile change (SWC), 0.2 × the between-athlete SD. Use the SWC rules and caveats in the smallest worthwhile change reference of the `monitoring-statistics` skill to judge whether a gap is worth attention.

### Measurement error beside each value

Typical error (TE) is the noise in a test: the SD of one athlete's repeated scores when nothing real changed. Take it from the typical error reference of the `monitoring-statistics` skill, on the same protocol and trial summary as the squad values.

Put an approximate 95% range for the athlete's true score around the observed value. Swinton et al. (2018) build this range as the observed score plus and minus a multiple of TE:

```text
error range = x ± 1.96 × TE
```

Carry the range into each scale:

```text
SD units range   = SD units ± 1.96 × TE / group SD
percentile range = percentile the athlete would have at x − 1.96 × TE, and at x + 1.96 × TE
```

For the percentile range, keep every teammate's value fixed. Move only this athlete's value to each end of the error range, and apply definition C again.

The range for SD units follows from dividing the error range by the group SD. The percentile range is this skill's method, built from the Swinton et al. (2018) range. It is not a published method. The 95% level is a choice. When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study, as the `monitoring-statistics` skill describes.

The range covers only this athlete's error. Teammates' values hold error too, so the true order inside the squad is less certain than the range shows. To say whether two athletes differ beyond noise, follow the section on ranking that reads as judgment in the squad views reference of the `athlete-data-visualization` skill. Do not restate that rule as a ranking.

### Direction for timed tests

For a test where a lower value is a better score, such as a sprint time, count athletes with a higher value instead of a lower one. The percentile then reads as "percent of the squad slower". Multiply SD units by −1, so a positive value means faster than the mean. Say so in the row label, for example `10 m sprint, percent of squad slower`. The profile dot plot flips timed tests the same way.

### Use a spreadsheet

These formulas work in Excel and Google Sheets. Put one row per athlete for one test day: `athlete_id` in column `A`, the result in `B` (blank when the athlete did not test), the position group in `C`, and TE in cell `$F$1`. Rows 2 to 13 hold the squad. Each formula below is for the athlete in row 8:

```text
Squad n:                 =COUNT($B$2:$B$13)
Step:                    =100/COUNT($B$2:$B$13)
Squad percentile (C):    =IF(B8="","",100*(COUNTIF($B$2:$B$13,"<"&B8)+0.5*COUNTIF($B$2:$B$13,B8))/COUNT($B$2:$B$13))
SD units:                =IF(B8="","",(B8-AVERAGE($B$2:$B$13))/STDEV.S($B$2:$B$13))
SD units error (±):      =1.96*$F$1/STDEV.S($B$2:$B$13)
Error range, low:        =B8-1.96*$F$1
Error range, high:       =B8+1.96*$F$1
```

For the percentile at each end of the error range, put the low end in `D8` and the high end in `E8`. Then use this formula, with `D8` replaced by `E8` for the high end. The parts `(B8<D8)` and `(B8=D8)` remove the athlete's own value from the teammate counts, and the `+1` puts the athlete back at the new value:

```text
=100*(COUNTIF($B$2:$B$13,"<"&D8)-(B8<D8)+0.5*(COUNTIF($B$2:$B$13,D8)-(B8=D8)+1))/COUNT($B$2:$B$13)
```

For the position group, count only rows with the same group in column `C`. `FILTER` works in Excel 365 and Google Sheets:

```text
Group n:                 =SUMPRODUCT(($C$2:$C$13=C8)*ISNUMBER($B$2:$B$13))
Group percentile (C):    =IF(B8="","",100*(COUNTIFS($C$2:$C$13,C8,$B$2:$B$13,"<"&B8)+0.5*COUNTIFS($C$2:$C$13,C8,$B$2:$B$13,B8))/SUMPRODUCT(($C$2:$C$13=C8)*ISNUMBER($B$2:$B$13)))
Group SD units:          =IF(B8="","",(B8-AVERAGE(FILTER($B$2:$B$13,($C$2:$C$13=C8)*ISNUMBER($B$2:$B$13))))/STDEV.S(FILTER($B$2:$B$13,($C$2:$C$13=C8)*ISNUMBER($B$2:$B$13))))
```

For a timed test, make these changes:

- Replace `"<"&` with `">"&` in every percentile formula.
- In the error range formula, also replace `(B8<D8)` with `(B8>D8)`. Otherwise the athlete counts as a slower teammate at their own value.
- Use `(AVERAGE(...)-B8)` in place of `(B8-AVERAGE(...))` for SD units.

Check the timed version on A07's sprint in the worked example below. At the low end, 1.701 s, the formula gives 100 × (12 − 1 + 0.5 × (0 − 0 + 1)) / 12 = 95.8. Without the change to `(B8>D8)`, it gives 104.2, which is above 100. At the high end, 1.819 s, it gives 100 × (5 − 0 + 0.5) / 12 = 45.8.

Keep the rows in roster or position order. Do not sort the sheet by the result or the percentile.

### Calculate it in Power BI and Tableau

These versions assume one row per athlete, date, session, measure, and trial in a `measures` table, and an `athletes` table with `athlete_id` and `group`, as in the table layout reference of the `ams-data-setup` skill. The test is `cmj_jump_height` in `cm`, and the trial summary is the best trial. Use the same summary as the test's TE. Filter the report to one test day.

In Power BI, use these DAX measures. Put `athletes[athlete_id]` in the visual, not `measures[athlete_id]`. The squad table removes the filter on athletes, so every teammate counts even when the visual shows one athlete:

```text
Test value (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)

Squad percentile (C) =
VAR x = [Test value (cm)]
VAR squad =
    CALCULATETABLE (
        FILTER (
            ADDCOLUMNS ( VALUES ( athletes[athlete_id] ), "@v", [Test value (cm)] ),
            NOT ISBLANK ( [@v] )
        ),
        REMOVEFILTERS ( athletes )
    )
VAR n = COUNTROWS ( squad )
VAR below = COUNTROWS ( FILTER ( squad, [@v] < x ) )
VAR equal = COUNTROWS ( FILTER ( squad, [@v] = x ) )
RETURN
    IF ( HASONEVALUE ( athletes[athlete_id] ) && NOT ISBLANK ( x ), 100 * ( below + 0.5 * equal ) / n )

Squad SD units =
VAR x = [Test value (cm)]
VAR squad =
    CALCULATETABLE (
        FILTER (
            ADDCOLUMNS ( VALUES ( athletes[athlete_id] ), "@v", [Test value (cm)] ),
            NOT ISBLANK ( [@v] )
        ),
        REMOVEFILTERS ( athletes )
    )
VAR sd = STDEVX.S ( squad, [@v] )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && NOT ISBLANK ( x ) && COUNTROWS ( squad ) >= 2 && sd > 0,
        ( x - AVERAGEX ( squad, [@v] ) ) / sd
    )

Squad percentile at low error limit =
VAR te = 1.4
VAR id = SELECTEDVALUE ( athletes[athlete_id] )
VAR x = [Test value (cm)]
VAR limit = x - 1.96 * te
VAR squad =
    CALCULATETABLE (
        FILTER (
            ADDCOLUMNS ( VALUES ( athletes[athlete_id] ), "@v", [Test value (cm)] ),
            NOT ISBLANK ( [@v] )
        ),
        REMOVEFILTERS ( athletes )
    )
VAR others = FILTER ( squad, athletes[athlete_id] <> id )
VAR below = COUNTROWS ( FILTER ( others, [@v] < limit ) )
VAR equal = COUNTROWS ( FILTER ( others, [@v] = limit ) )
RETURN
    IF ( NOT ISBLANK ( id ) && NOT ISBLANK ( x ), 100 * ( below + 0.5 * ( equal + 1 ) ) / COUNTROWS ( squad ) )
```

Set `te` to the test's TE in the units of the test. For the high limit, copy the last measure and use `x + 1.96 * te`. For the position group, add `VAR grp = SELECTEDVALUE ( athletes[group] )` at the top, and add `athletes[group] = grp` as a filter inside each `CALCULATETABLE`, after `REMOVEFILTERS ( athletes )`.

For a timed test, make these changes in the DAX:

- In `Squad percentile (C)`, replace `[@v] < x` with `[@v] > x`.
- In each error limit measure, replace `[@v] < limit` with `[@v] > limit`.
- In `Squad SD units`, use `( AVERAGEX ( squad, [@v] ) - x ) / sd`.

In Tableau, put `athlete_id` on the view and filter to one test day. Use these calculations. Set each table calculation to compute using `athlete_id`. For the position group, add `group` to the view, so each group is its own partition:

```text
Test value (cm):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" THEN [value] END)

Squad percentile (C):
IF ISNULL([Test value (cm)]) THEN NULL
ELSE 100 * ((RANK([Test value (cm)], 'asc') - 1)
     + 0.5 * (RANK_MODIFIED([Test value (cm)], 'asc') - (RANK([Test value (cm)], 'asc') - 1)))
     / WINDOW_COUNT([Test value (cm)])
END

Squad SD units:
([Test value (cm)] - WINDOW_AVG([Test value (cm)])) / WINDOW_STDEV([Test value (cm)])

SD units error (±):
1.96 * [TE (cm)] / WINDOW_STDEV([Test value (cm)])
```

`[TE (cm)]` is a parameter that holds the test's TE. The percentile works because, in ascending order, `RANK` gives 1 plus the number of lower values, and `RANK_MODIFIED` gives the number of values at or below (Tableau, table calculation functions). On (6, 9, 9, 14), this calculation gives 12.5, 50, 50, and 87.5. Use the rank functions only inside this calculation. Do not show them, and do not sort the view by them.

For a timed test, replace every `'asc'` with `'desc'` in `Squad percentile (C)`. In descending order, `RANK` gives 1 plus the number of higher values, and `RANK_MODIFIED` gives the number of values at or above. For A07's sprint in the worked example below, this gives 79.2. Also use `(WINDOW_AVG([Test value (s)]) - [Test value (s)]) / WINDOW_STDEV([Test value (s)])` for SD units.

Follow these Tableau rules:

- Ranking functions ignore nulls, so an athlete with no test does not count (Tableau, table calculation functions). List that athlete in a note.
- Table calculations run after dimension filters. To show one athlete, do not filter `athlete_id`. That removes teammates before the calculation. Use a table calculation filter instead, such as `LOOKUP(ATTR([athlete_id]), 0) = [Selected athlete]`.
- Table calculations cannot count teammates below a value that is not in the data. Compute the percentile range in the spreadsheet, Power BI, or Python. In Tableau, show the SD units range instead.

### Use Python

This standard-library Python code reads one row per athlete and returns the profile for one athlete and test:

```python
import csv, statistics

def percentile_c(values, own, at=None):
    """Definition C percentile of `at` (default: own value) in a group that holds `own`."""
    at = own if at is None else at
    others = list(values)
    others.remove(own)
    below = sum(v < at for v in others)
    equal = sum(v == at for v in others) + 1      # the athlete counts at `at`
    return 100 * (below + 0.5 * equal) / len(values)

def profile(rows, athlete, col, te, lower_is_better=False):
    sign = -1 if lower_is_better else 1
    group = [sign * float(r[col]) for r in rows if r[col] != ""]
    own = sign * float(next(r[col] for r in rows if r["athlete_id"] == athlete))
    mean, sd = statistics.mean(group), statistics.stdev(group)   # sample SD
    return {
        "n": len(group),
        "step": 100 / len(group),
        "percentile": percentile_c(group, own),
        "error_percentiles": (percentile_c(group, own, own - 1.96 * te),
                              percentile_c(group, own, own + 1.96 * te)),
        "sd_units": (own - mean) / sd,
        "sd_units_error": 1.96 * te / sd,
    }

rows = list(csv.DictReader(open("squad.csv")))   # athlete_id, group, cmj_cm, sprint10_s
print([r["athlete_id"] for r in rows if r["cmj_cm"] == ""])          # no test
print(profile(rows, "A07", "cmj_cm", te=1.4))
print(profile([r for r in rows if r["group"] == "backs"], "A07", "cmj_cm", te=1.4))
print(profile(rows, "A07", "sprint10_s", te=0.03, lower_is_better=True))
```

## Calculate the metric

Follow these steps for each test:

1. Pick one test day or one short test window for the whole group.
2. Keep only results from the same protocol, device, method, and trial summary.
3. List every athlete in the group who has no result. Do not fill a missing result.
4. Count `N`, the athletes with a result.
5. Work out the step, `100 / N`.
6. Count `m`, the athletes with a lower result than this athlete. For a timed test, count athletes with a higher result.
7. Count `k`, the athletes with the same result, including this athlete.
8. Calculate the percentile, `100 × (m + 0.5 × k) / N`.
9. Calculate the group mean and the sample SD.
10. Calculate SD units, `(x − mean) / SD`. Multiply by −1 for a timed test.
11. Calculate the error range, `x ± 1.96 × TE`.
12. Calculate the percentile at each end of the error range, with teammates fixed.
13. Calculate the SD units range, `SD units ± 1.96 × TE / SD`.
14. Repeat steps 3 to 13 within the athlete's position group.
15. Show each number with its group, `N`, step, definition, TE source, and units.

## Worked example

The squad has 13 athletes. Twelve did a countermovement jump (CMJ) and a 10 m sprint on the same test day. Athlete A13 did not test. The CMJ result is the best of 3 trials. The sprint result is the fastest of 3 trials. All numbers are made up. The squad's own same-day retest gave TE = 1.4 cm for the CMJ and 0.03 s for the sprint, on the same trial summaries.

| Athlete | Group | CMJ height (cm) | 10 m sprint (s) |
|---|---|---|---|
| A01 | forwards | 41.3 | 1.78 |
| A02 | backs | 34.8 | 1.74 |
| A03 | forwards | 38.6 | 1.82 |
| A04 | backs | 31.2 | 1.80 |
| A05 | forwards | 36.9 | 1.86 |
| A06 | backs | 43.0 | 1.71 |
| A07 | backs | 37.4 | 1.76 |
| A08 | forwards | 35.6 | 1.84 |
| A09 | forwards | 39.9 | 1.79 |
| A10 | forwards | 37.4 | 1.88 |
| A11 | backs | 33.5 | 1.77 |
| A12 | forwards | 36.1 | 1.83 |
| A13 | forwards | no test | no test |

The table is in roster order. Keep it that way in any output.

Work out A07's CMJ against the squad:

1. `N` = 12. A13 is listed as no test. Step = 100 / 12 = 8.3 points.
2. `m` = 6 athletes jumped lower than 37.4 cm.
3. `k` = 2: A07 and A10 both jumped 37.4 cm.
4. Percentile = 100 × (6 + 0.5 × 2) / 12 = 58.3.
5. Squad mean = 37.14 cm. Squad SD = 3.29 cm.
6. SD units = (37.4 − 37.14) / 3.29 = 0.08.
7. Error range = 37.4 ± 1.96 × 1.4 = 37.4 ± 2.74 = 34.66 to 40.14 cm.
8. At 34.66 cm, 2 teammates sit lower. Percentile = 100 × (2 + 0.5) / 12 = 20.8.
9. At 40.14 cm, 9 teammates sit lower. Percentile = 100 × (9 + 0.5) / 12 = 79.2.
10. SD units range = 0.08 ± 2.74 / 3.29 = 0.08 ± 0.83 = −0.76 to 0.91.

Seven of A07's 11 teammates sit inside her error range.

Work out A07's CMJ against the backs, a group of 5:

1. Step = 100 / 5 = 20 points.
2. `m` = 3, `k` = 1. Percentile = 100 × (3 + 0.5) / 5 = 70.
3. Backs mean = 35.98 cm. Backs SD = 4.52 cm. SD units = 0.31.
4. At 34.66 cm, the percentile is 50. At 40.14 cm, it is still 70, because no back sits between 37.4 and 40.14 cm.
5. SD units range = 0.31 ± 0.61 = −0.29 to 0.92.

Work out A07's 10 m sprint against the squad, as percent of squad slower:

1. Nine teammates ran slower than 1.76 s, and no one tied. Percentile = 100 × (9 + 0.5) / 12 = 79.2.
2. Squad mean = 1.798 s. Squad SD = 0.050 s. SD units = (1.798 − 1.76) / 0.050 = 0.77 faster than the mean.
3. Error range = 1.76 ± 0.059 = 1.701 to 1.819 s.
4. At 1.819 s, 5 teammates are slower: percentile 45.8. At 1.701 s, all 11 are slower: percentile 95.8.
5. SD units range = 0.77 ± 1.17 = −0.41 to 1.94.

Result: write A07's profile in plain words, one test per line:

- CMJ: 58th percentile of 12 squad athletes (definition C, steps of 8.3). With measurement error, 21st to 79th. In SD units, 0.08 from the squad mean (−0.76 to 0.91). This is inside ±0.2 SD units, the default SWC, so it is at the squad mean for practical purposes.
- CMJ within the backs: 70th percentile of 5 (steps of 20). With measurement error, 50th to 70th.
- 10 m sprint: faster than 79% of 12 squad athletes. With measurement error, 46% to 96%. The sprint TE is large next to the squad's spread, so the range covers about half the squad.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Percentile definition. For A07's CMJ, definition A (scores below) gives 50, definition B (at or below) gives 66.7, and definition C gives 58.3. Ties make the gap larger.
- Group size. One place in a squad of 12 is 8.3 points. One place in a group of 5 is 20 points.
- Who is in the group. Adding or removing one athlete changes every percentile. Athletes who did not test change `N`.
- Trial summary. Best of 3 and mean of 3 give different values and a different TE. Use one summary for every athlete, as step 9 of the `force-plate` skill asks.
- Test day. Results from different days mix real change with position.
- Method and device. A jump height from flight time and one from takeoff velocity are not comparable.
- TE and the confidence level. A larger TE or a higher level widens every range.

## Units and typical range

Percentiles run from 0 to 100 and have no unit. With definition C and the athlete in the group, the lowest possible value is `50 / N` and the highest is `100 − 50 / N`. With 12 athletes, that is 4.2 to 95.8.

SD units have no unit. No published range applies to a squad, because the squad sets its own mean and SD.

## Data you need

Collect this data:

- Source: one result per athlete per test, from the same test day, protocol, device, method, and trial summary.
- Sampling: one test day or one short test window for the whole group.
- Minimum data: no published minimum group size exists for a squad percentile. Show `N` and the step with every percentile, and let the coach judge. For a group of 5 or fewer, also show the group's values as a dot plot, so the coach sees every value. The cut at 5 is this skill's practice default, not a published rule.
- TE for each test, on the same protocol and trial summary, from the typical error reference of the `monitoring-statistics` skill.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with squad position:

- Using `PERCENTRANK.INC` or `RANK_PERCENTILE` without saying which definition it uses. Use definition C, and name it.
- Showing a percentile with no `N` and no step. A 70th percentile of 5 athletes is not a 70th percentile of 200.
- Showing a percentile with no measurement error beside it.
- Dropping athletes who did not test without listing them.
- Mixing trial summaries, methods, or test days in one group.
- Treating a higher percentile as better for a timed test without flipping it. Say "percent of squad slower".
- Calling SD units a z-score, which in these skills means a z-score against the athlete's own baseline.
- Sorting the table by percentile, numbering athletes, or adding a total across tests. That is a ranking. See [Decline a ranking request](../SKILL.md#decline-a-ranking-request).
- Rating words such as "elite", "poor", or "below standard" next to a percentile.

## Example request

> Here are our preseason CMJ and 10 m sprint results for 12 players. Where does A07 sit against the squad and against the other backs?

## Check the result

Run these checks:

- Recompute one percentile by hand: count `m` and `k`, and confirm `100 × (m + 0.5 × k) / N`.
- Confirm the percentile lies between `50 / N` and `100 − 50 / N`.
- Confirm the athlete's percentile sits inside the athlete's percentile range.
- Confirm the SD units use the sample SD (`STDEV.S`, `statistics.stdev`, or `STDEVX.S`).
- Confirm timed tests are flipped and labeled.
- Confirm the output lists every athlete with no result, and is in roster or position order.

## Sources

This file cites these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07). Source of the share of practitioners who compare with norms, use position groups, and account for measurement error.
- Crawford JR, Garthwaite PH, Slick DJ. On percentile norms in neuropsychology: proposed reporting standards and methods for quantifying the uncertainty over the percentile ranks of test scores. The Clinical Neuropsychologist. 2009;23(7):1173-1195. https://doi.org/10.1080/13854040902795018 (accessed 2026-10-07). Source of the three percentile definitions, the recommendation of definition C, and its formula, which the paper credits to Ley (1972).
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041 (accessed 2026-10-07). Source of the range for a true score as the observed score plus and minus a multiple of TE.
- Microsoft. PERCENTRANK.INC function. https://support.microsoft.com/en-us/office/percentrank-inc-function-149592c9-00c0-49ba-86c1-c1f45b80463a (accessed 2026-10-07).
- Tableau. Table calculation functions: RANK, RANK_MODIFIED, RANK_PERCENTILE, and WINDOW_COUNT. https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm (accessed 2026-10-07).
