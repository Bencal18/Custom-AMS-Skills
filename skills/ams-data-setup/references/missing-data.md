# Handle missing data

Last checked: 2026-10-02

## What it covers

This file shows how to record, count, and report values that are missing from athlete data. It covers zeros, missing codes, coverage, and what to do before you average or sum.

## Method

A missing value is one that you expected and do not have. Examples are a skipped wellness form, a device that failed, or a test an athlete missed. Zero is a real value. Never use zero for missing.

### Mark missing values

Follow these rules:

- Write one code for missing in the `value` column, such as `NA`. Do not leave the cell blank, and do not use `0` or `999`. Broman and Woo (2018) recommend one consistent code for missing values, and warn against a number such as `999`.
- Do not use `-` for missing either. This rule is specific to this skill: a hyphen can look like a minus sign. Broman and Woo (2018) allow `NA` or a hyphen.
- Add a row with `value` set to `NA` and a `status` only when you know why the value is missing. Examples: `excused`, `device_failure`, `not_measured`.
- If you do not know why, add no row. Coverage then counts the gap against the expected list.
- Do not remove rows to hide a gap. Do not carry the last value forward. Do not fill with the average.
- Never write `NA` in a key column such as `side` or `session_id`. Use an explicit code, such as `bilateral` or `none`. See the table layout reference.

Ask the user to define the list of `status` codes and write it in the measure dictionary.

### Know what is expected

You can only report a gap against a list of what you expected. Build the expected list from the athletes table (active athletes in the group on that date) and the sessions table (sessions that happened).

Keep excused athletes on the expected list, and report them as their own count. An athlete may be excused for a reason linked to the value you want, such as illness or injury.

Taking them off the list hides that gap. Report it as, for example, `18 of 24 athletes with a value, 2 excused, 4 with no row`.

### Report coverage

Coverage is the number of athletes with a usable value, divided by the number of athletes expected. Count athletes, not rows. A test with 3 trials has up to 3 rows for each athlete, so a count of rows can pass 100 percent.

```text
coverage = athletes with at least one value with status ok / athletes expected
```

An athlete whose only values are `held` is pending, not covered. Report settled, pending, and missing athletes as separate counts, for example 4 of 6 settled, 1 pending, and 1 with no value.

Report coverage for each measure and each week. Show the numbers, for example `18 of 24 athletes (75%)`. Put the date of each athlete's last value in the report.

In a spreadsheet, make a sheet with one row for each expected athlete, with `athlete_id` in column A and the date in `$D$1`. Count that athlete's `ok` rows in column B, and all rows in column C:

```text
B2: =COUNTIFS(measures[athlete_id],A2,measures[measure_name],"wellness_score",measures[measure_date],$D$1,measures[status],"ok")
C2: =COUNTIFS(measures[athlete_id],A2,measures[measure_name],"wellness_score",measures[measure_date],$D$1)
```

Then count athletes, with the expected athletes in rows 2 to 25:

```text
with a value:             =COUNTIF(B2:B25,">0")
with only a reason code:  =COUNTIFS(B2:B25,0,C2:C25,">0")
with no row:              =COUNTIF(C2:C25,0)
```

This Python snippet does the same count:

```python
import pandas as pd
m = pd.read_csv("measures.csv", dtype=str)
expected = set(pd.read_csv("expected.csv", dtype=str)["athlete_id"])  # athletes expected that day
day = m[(m["measure_name"] == "cmj_jump_height") & (m["measure_date"] == "2026-10-02")]
ok = set(day.loc[day["status"] == "ok", "athlete_id"]) & expected
coded = (set(day["athlete_id"]) & expected) - ok  # only reason-coded rows, such as device_failure
no_row = expected - ok - coded
print(f"{len(ok)} of {len(expected)} athletes with a value ({len(ok) / len(expected):.0%})")
print(f"{len(coded)} with a reason code, {len(no_row)} with no row")
```

Take 4 expected athletes. Of these, 2 have 3 trial rows each, and one of those has a failed trial. Of the rest, 1 has only a `device_failure` row and 1 has no row. For this data, the snippet prints `2 of 4 athletes with a value (50%)` and `1 with a reason code, 1 with no row`. A count of `ok` rows for the same data gives 5, more than the 4 athletes expected.

### Count coverage in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They count athletes, not rows, and they keep athletes with no row on the expected list.

Both versions assume the `measures` table and the `athletes` table from the table layout reference. They also assume that `NA` in `value` and in `end_date` became a true blank on import. See the `power-bi.md` and `tableau.md` references.

In Power BI, select one date in a slicer on the `dates` table. `OK rows` and `All rows` count only that date because `dates[Date]` filters `measures[measure_date]` through their relationship. Use these DAX measures. They are measures, not calculated columns, because the date comes from the slicer, and a calculated column cannot see a slicer:

```text
OK rows =
CALCULATE (
    COUNTROWS ( measures ),
    measures[measure_name] = "wellness_score",
    measures[status] = "ok"
)

All rows =
CALCULATE (
    COUNTROWS ( measures ),
    measures[measure_name] = "wellness_score"
)

Athletes expected =
VAR d = SELECTEDVALUE ( dates[date] )
RETURN
    IF (
        NOT ISBLANK ( d ),
        COUNTROWS (
            FILTER (
                athletes,
                athletes[start_date] <= d
                    && ( ISBLANK ( athletes[end_date] ) || athletes[end_date] >= d )
            )
        ) + 0
    )

Athletes with a value =
VAR d = SELECTEDVALUE ( dates[date] )
VAR expected =
    FILTER (
        athletes,
        athletes[start_date] <= d
            && ( ISBLANK ( athletes[end_date] ) || athletes[end_date] >= d )
    )
RETURN
    IF (
        NOT ISBLANK ( d ),
        COUNTROWS ( FILTER ( expected, COALESCE ( [OK rows], 0 ) > 0 ) ) + 0
    )

Athletes with only a reason code =
VAR d = SELECTEDVALUE ( dates[date] )
VAR expected =
    FILTER (
        athletes,
        athletes[start_date] <= d
            && ( ISBLANK ( athletes[end_date] ) || athletes[end_date] >= d )
    )
RETURN
    IF (
        NOT ISBLANK ( d ),
        COUNTROWS (
            FILTER ( expected, COALESCE ( [OK rows], 0 ) = 0 && COALESCE ( [All rows], 0 ) > 0 )
        ) + 0
    )

Athletes with no row =
VAR d = SELECTEDVALUE ( dates[date] )
VAR expected =
    FILTER (
        athletes,
        athletes[start_date] <= d
            && ( ISBLANK ( athletes[end_date] ) || athletes[end_date] >= d )
    )
RETURN
    IF (
        NOT ISBLANK ( d ),
        COUNTROWS ( FILTER ( expected, ISBLANK ( [All rows] ) ) ) + 0
    )
```

For the per-athlete check, put `athletes[athlete_id]`, `OK rows`, and `All rows` in a table visual. Turn on **Show items with no data** for `athlete_id`, so athletes with no row stay in the table.

In Tableau, make a date parameter named `Report date`. Double-click the `athletes` table on the data source canvas to open the physical layer. Join `measures` to it with a left join on `athlete_id`, with `athletes` on the left. A left join keeps every athlete, including athletes with no row. The join gives two `athlete_id` fields. Use the one from `athletes` everywhere below, written `[athlete_id (athletes)]` if Tableau renames it. The `measures` one is null for athletes with no row. Use these calculated fields:

```text
ok_row (row-level):
IIF([measure_name] = "wellness_score" AND [measure_date] = [Report date] AND [status] = "ok", 1, 0, 0)

any_row (row-level):
IIF([measure_name] = "wellness_score" AND [measure_date] = [Report date], 1, 0, 0)

Coverage group (row-level, built on FIXED LOD expressions):
IF { FIXED [athlete_id (athletes)] : SUM([ok_row]) } > 0 THEN "with a value"
ELSEIF { FIXED [athlete_id (athletes)] : SUM([any_row]) } > 0 THEN "with only a reason code"
ELSE "with no row"
END

Expected on report date (row-level, use as a filter set to True):
[start_date] <= [Report date] AND (ISNULL([end_date]) OR [end_date] >= [Report date])
```

Put `Coverage group` on Rows and `COUNTD([athlete_id (athletes)])` on Text. The three counts must add up to the number expected.

Put the measure name and the report date inside the calculations, as above. Do not filter `measure_name` or `measure_date` on the Filters shelf. That filter removes the rows of athletes with no row, so they drop out of the count.

Blanks behave this way in each tool:

- Power BI: `COUNTROWS` returns blank for an athlete with no rows, not 0. `COALESCE` turns that blank into 0 for the comparison only. The `+ 0` makes a count of no athletes print as 0, which is a real count here.
- Tableau: an athlete with no row has null in every `measures` field. `IIF` returns its fourth argument, 0, when the test is null. So that athlete gets 0 in both counts and lands in `with no row`.

### Handle averages and sums

`AVERAGE` and `AVERAGEIF` in spreadsheets ignore text such as `NA`. This gives the mean of the values you have. State the count next to the mean, for example `mean 38.4 cm, n = 18 of 24`.

`SUM` also ignores text. A weekly total with two missing days is lower than the true total, and it looks like a real drop. Do not compare a total with missing days to a total with none. Count the days that went into each total. Ask the user what share of days they need before they trust a total.

### Think about why the data is missing

Values are not always missing at random. An athlete who skips a test may be injured, sick, or tired, and that is the reason you want the data. The observed data alone cannot tell you whether values are missing at random or missing because of the value itself (Sterne et al., 2009).

Using only complete cases can bias the result and cost precision (Sterne et al., 2009). Say who is missing when you report a summary.

### Fill missing values only when the user asks

Do not fill, estimate, or impute missing values unless the user asks. If the user asks, explain the options, state the method you use, and show the results with and without the filled values. Mark each filled value in a column such as `value_filled`.

In simulations built on one men's football team's data, multiple imputation with predictive mean matching was the most accurate of five methods in most scenarios, for session rating of perceived exertion and GPS total distance (Bache-Mathiesen et al., 2022). It performed poorly when all GPS variables were missing on the same days. Multiple imputation does not fix values that are missing because of the value itself, such as high loads that go unreported. The study judged methods by how well a research model of load and injury risk was recovered, not by how well an athlete's daily values were filled. Do not assume the result holds for other measures or for filling one athlete's values. Ask a statistician before you impute.

Report missing data in every analysis. In a review of 108 training load and injury studies, only 37 reported whether training load had missing observations (Bache-Mathiesen et al., 2022).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with missing data:

- Filling missing values with `0`. This lowers every average and every total, and it looks like a real drop in load or a real low score.
- Using `IFERROR(x, 0)` or `fillna(0)`. These turn errors and gaps into zeros without a warning.
- Carrying the last value forward. The value then looks measured on a day it was not.
- Dropping rows with missing values before you count athletes. The count then hides who is missing.
- Counting rows instead of athletes for coverage. Trials and repeat rows push coverage past 100 percent.
- Taking excused athletes off the expected list without a separate count. The gap then disappears from the report.
- Reporting a mean without `n`. A mean of 6 athletes and a mean of 24 athletes look the same.
- Comparing a week with full data to a week with gaps, using sums.
- Treating a blank, `0`, and `NA` as the same thing. They mean different things.
- Filling gaps with the squad average. This pulls each athlete toward the group and hides individual change.

## Example request

> Some athletes skipped the wellness form on some days. Work out each athlete's weekly average wellness score and tell me how much data is missing.

## Check the result

Run these checks on the result:

- Count the `0` values in each measure. Confirm each zero is a real zero, such as a score of zero that the form allows, not a gap.
- Recompute one athlete's weekly average by hand from the raw values. Confirm it ignores missing days and that `n` is correct.
- Sort the expected athletes into three groups: athletes with at least one `ok` value, athletes with only reason-coded rows, and athletes with no row. Confirm the three counts add up to the number expected.

## Sources

These sources support the rules in this file:

- Broman KW, Woo KH. Data organization in spreadsheets. *The American Statistician*. 2018;72(1):2-10. doi:10.1080/00031305.2017.1375989. Source of the rule to use one consistent code for missing values and not to leave cells empty. Allows `NA` or a hyphen, and warns against a numeric code such as `999`.
- Sterne JAC, White IR, Carlin JB, et al. Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls. *BMJ*. 2009;338:b2393. doi:10.1136/bmj.b2393. Shows that complete case analysis can give biased results when data are missing at random but not completely at random, that observed data alone cannot separate missing at random from missing because of the value itself, and that many studies report missing data poorly.
- Bache-Mathiesen LK, Andersen TE, Clarsen B, Fagerland MW. Handling and reporting missing data in training load and injury risk research. *Science and Medicine in Football*. 2022;6(4):452-464. doi:10.1080/24733938.2021.1998587. Reports that 37 of 108 studies reported missing training load data, and that multiple imputation with predictive mean matching performed best in most simulated scenarios for session rating of perceived exertion and GPS total distance, but not when all GPS variables were missing together.
