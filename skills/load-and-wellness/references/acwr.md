# Acute to chronic workload ratio (ACWR)

Last checked: 2026-10-02

## What it measures

ACWR divides an athlete's recent load (acute load) by their longer-term average load (chronic load), so it describes how recent load compares with what the athlete has been doing.

Read these limits before you use it:

- ACWR does not predict injury. No study has properly estimated whether changing ACWR changes injury rates, and the ratio adds noise and statistical artifacts (Impellizzeri et al., 2020a).
- A reanalysis found that ACWR gave no meaningful predictive advantage over a model with no predictor at all. Dividing acute load by made-up chronic values produced similar injury associations to the real ratio (Impellizzeri et al., 2021). The authors recommend dismissing ACWR as a framework.
- The ratio does not remove the effect of acute load, even when the windows do not overlap (Impellizzeri et al., 2020a; Impellizzeri et al., 2020b).
- The window lengths are a convention, not a finding. Studies have used 1 to 2 weeks for acute load and 1 to 8 weeks for chronic load without justification (Impellizzeri et al., 2020b).
- Training-load measures cannot tell you whether a change raises or lowers injury risk. Rely on training principles and the athlete's response (Impellizzeri et al., 2020b).

Use ACWR only as a description of how load changed. Report the acute and chronic loads next to it.

Put this sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text, not once per answer:

> ACWR describes how recent load compares with longer-term load. It does not predict injury.

A bare value such as "uncoupled ACWR 1.62" reads like a published "danger zone". Impellizzeri et al. (2020a) found no evidence that supports ACWR for training recommendations aimed at reducing injury risk.

## Formula

Three variants are in use. They give different numbers from the same data. Name the variant every time.

```text
Rolling average, coupled:    ACWR = mean daily load, last 7 days ÷ mean daily load, last 28 days
Rolling average, uncoupled:  ACWR = mean daily load, last 7 days ÷ mean daily load, days 8 to 28 back
EWMA:                        EWMA_today = load_today × λ + (1 − λ) × EWMA_yesterday
                             λ = 2 ÷ (N + 1)
                             ACWR = EWMA with N = 7 ÷ EWMA with N = 28
```

Define every term in the formula:

- `load`: daily load in the athlete's own unit, for example session RPE load in AU or distance in m. Both loads in the ratio must use the same measure.
- Acute load: the recent window, by convention 7 days. Hulin et al. (2014) used 1 week for acute load and a 4-week rolling average for chronic load.
- Chronic load: the longer window, by convention 28 days.
- Coupled: the acute week is inside the chronic window. This is the traditional form (Windt and Gabbett, 2019).
- Uncoupled: the chronic window excludes the acute week, so it uses the 3 weeks before it (Gabbett et al., 2019; Windt and Gabbett, 2019).
- Mathematical coupling: the same numbers appear in the top and bottom of a ratio. In coupled ACWR this creates a spurious correlation of about 0.50 between acute and chronic load: r = 0.52 in simulated data of 1,000 athletes (Lolli et al., 2019, as reported by Windt and Gabbett, 2019). With four unrelated weeks of equal spread, the arithmetic gives exactly 0.5. Real loads also correlate for reasons other than coupling. In real basketball and weightlifting data, acute load correlated with uncoupled chronic load at r = 0.17 to 0.53 (Coyne et al., 2019).
- EWMA: exponentially weighted moving average. It gives older days less weight instead of dropping them at the window edge. `λ` (lambda) is the decay value between 0 and 1. `N` is the time decay constant in days, typically 7 and 28 (Williams et al., 2017).
- `N` sets the span, not a hard memory limit. The 28-day EWMA puts 13.5% of its weight on days older than 28 days, because (1 − 2/29)^28 = 0.135.
- EWMA start: this file sets the first EWMA value to the day 1 load. Williams et al. (2017) started both EWMAs at the day 1 load, as their figure legend states in the authors' accepted manuscript. Early values depend on the start value, which Wang et al. (2020) call the initial load problem.
- EWMA start-up period: with λ = 2/29, the start value carries 14.5% of the 28-day EWMA on day 28, 2.0% on day 56, and 0.3% on day 84. The 7-day EWMA settles fast: the start value carries 0.04% of it on day 28. Do not report EWMA ACWR before day 56, about two chronic windows. If the user needs earlier values, show each one next to the same value from a second start value, so the start effect is visible.

The weekly-sum form gives the same coupled value: acute weekly sum ÷ (28-day sum ÷ 4).

Use this Python function for one athlete with one row per calendar day:

```python
import pandas as pd

def acwr(load, acute=7, chronic=28, ewma_start=56):
    """load: one row per calendar day, DatetimeIndex, 0 on rest days, NaN if not recorded."""
    load = load.sort_index()
    full = pd.date_range(load.index.min(), load.index.max(), freq="D")
    if load.index.has_duplicates or len(load) != len(full):
        raise ValueError("Need one row per calendar day. Add rest days as 0 first.")
    a = load.rolling(acute).mean()
    coupled = a / load.rolling(chronic).mean()
    uncoupled = a / load.shift(acute).rolling(chronic - acute).mean()
    ewma = (load.ewm(alpha=2 / (acute + 1), adjust=False, ignore_na=True).mean()
            / load.ewm(alpha=2 / (chronic + 1), adjust=False, ignore_na=True).mean())
    day = pd.Series(range(1, len(load) + 1), index=load.index)
    gap = load.isna().astype(int).rolling(chronic, min_periods=1).max() == 1
    return pd.DataFrame({"load": load, "acute_mean": a, "chronic_mean": load.rolling(chronic).mean(),
                         "acwr_rolling_coupled": coupled,
                         "acwr_rolling_uncoupled": uncoupled,
                         "acwr_ewma": ewma.mask((day < ewma_start) | gap)})
```

The code stops if any calendar day has no row, because a missing rest-day row would turn a rest day into a missing day. It returns rolling ratios as missing for any window with a missing day.

On a missing day, each EWMA keeps the previous day's value and keeps reporting, so the code masks EWMA ACWR on the missing day and the 27 days after it. Keep `ignore_na=True`. With the pandas default, `ignore_na=False`, `ewm()` gives the first day after a gap extra weight. That matches the 28-day rolling rule. The missing day has a small effect after that, because EWMA never fully drops a day: a single day 28 days back carries 0.9% of the 28-day EWMA.

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They follow the `acwr` function and steps 10 to 17 in the next section. They give the 7-day mean, the 28-day mean, and the days 8 to 28 mean, with three ratios: rolling coupled, rolling uncoupled, and EWMA with λ = 2 ÷ (N + 1). They keep these rules from the Python function:

- A rolling ratio is blank until the 28 days ending that day all have a recorded load. It is also blank on a missing day and the 27 days after it.
- Each EWMA starts at the day 1 load. On a missing day, it keeps the previous day's value.
- The EWMA ratio is blank before day 56, on a missing day, and on the 27 days after it.
- The 7-day mean shows whenever its own 7 days have no missing day.
- A ratio is blank when its chronic load is 0. The Python function gives a missing value or infinity there.

Both versions count calendar days, not rows. A window of 7 or 28 rows spans more calendar days when a day has no row, so a missing day would silently stretch the window. Each window below takes a fixed run of calendar dates and counts how many of them have a load.

Both versions assume one row per athlete and calendar day in a `measures` table, with `measure_name` `daily_load` and `unit` `au`. Build the daily totals before import, in the AMS sheet, Python, or R. Add up each athlete's sessions for each calendar day. Write 0 on a rest day. Leave a day with an unrated session missing, with no value. Append the totals to `measures` with `measure_name` `daily_load`, `unit` `au`, and `status` `ok`. A day with no row, or with a row whose `status` is not `ok`, is a missing day. For distance, change the name and unit, for example to `daily_distance` in `m`. Use one load measure for every athlete and every day.

Day 1 is the athlete's first day with a daily load: exactly one `daily_load` row, with `status` `ok` and a value. The Python function counts from the first row of the calendar, so start that calendar on the first recorded day and the two agree.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Put `athletes[athlete_id]` and `dates[date]` in the visual. Use these DAX measures. They are measures, not calculated columns, because each value reads a window of earlier days for the athlete and date in the visual. A calculated column is computed once per row at data refresh and does not change with filters or slicers (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options):

```text
Daily load (AU) =
IF (
    CALCULATE ( COUNTROWS ( measures ), measures[measure_name] = "daily_load" ) = 1,
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "daily_load",
        measures[unit] = "au",
        measures[status] = "ok"
    )
)

Recorded days in last 28 =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
        DATESINPERIOD ( dates[date], today, -28, DAY )
    )
RETURN COUNTROWS ( FILTER ( days, NOT ISBLANK ( [@x] ) ) ) + 0

Acute load, 7-day mean (AU) =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESINPERIOD ( dates[date], today, -7, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && COUNTROWS ( recorded ) = 7,
        SUMX ( recorded, [@x] ) / 7
    )

Chronic load, 28-day mean (AU) =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESINPERIOD ( dates[date], today, -28, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && COUNTROWS ( recorded ) = 28,
        SUMX ( recorded, [@x] ) / 28
    )

Chronic load, days 8 to 28 mean (AU) =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESINPERIOD ( dates[date], today - 7, -21, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && COUNTROWS ( recorded ) = 21,
        SUMX ( recorded, [@x] ) / 21
    )

Rolling ACWR, coupled =
VAR a = [Acute load, 7-day mean (AU)]
VAR c = [Chronic load, 28-day mean (AU)]
RETURN IF ( NOT ISBLANK ( a ) && NOT ISBLANK ( c ) && c > 0, a / c )

Rolling ACWR, uncoupled =
VAR a = [Acute load, 7-day mean (AU)]
VAR c = [Chronic load, days 8 to 28 mean (AU)]
RETURN IF ( NOT ISBLANK ( a ) && NOT ISBLANK ( c ) && c > 0, a / c )

First load date =
MINX (
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            REMOVEFILTERS ( dates )
        ),
        NOT ISBLANK ( [@x] )
    ),
    dates[date]
)

Acute EWMA (AU) =
VAR n = 7
VAR lambda = 2 / ( n + 1 )
VAR today = MAX ( dates[date] )
VAR start = [First load date]
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESBETWEEN ( dates[date], start, today )
        ),
        NOT ISBLANK ( [@x] )
    )
VAR x0 = MAXX ( FILTER ( recorded, dates[date] = start ), [@x] )
VAR k = COUNTROWS ( recorded ) - 1
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && NOT ISBLANK ( x0 ) && today >= start,
        POWER ( 1 - lambda, k ) * x0
            + SUMX (
                FILTER ( recorded, dates[date] > start ),
                VAR d = dates[date]
                VAR later = COUNTROWS ( FILTER ( recorded, dates[date] > d ) )
                RETURN lambda * POWER ( 1 - lambda, later ) * [@x]
            )
    )

Chronic EWMA (AU) =
VAR n = 28
VAR lambda = 2 / ( n + 1 )
VAR today = MAX ( dates[date] )
VAR start = [First load date]
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESBETWEEN ( dates[date], start, today )
        ),
        NOT ISBLANK ( [@x] )
    )
VAR x0 = MAXX ( FILTER ( recorded, dates[date] = start ), [@x] )
VAR k = COUNTROWS ( recorded ) - 1
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && NOT ISBLANK ( x0 ) && today >= start,
        POWER ( 1 - lambda, k ) * x0
            + SUMX (
                FILTER ( recorded, dates[date] > start ),
                VAR d = dates[date]
                VAR later = COUNTROWS ( FILTER ( recorded, dates[date] > d ) )
                RETURN lambda * POWER ( 1 - lambda, later ) * [@x]
            )
    )

EWMA ACWR =
VAR start = [First load date]
VAR day_number = DATEDIFF ( start, MAX ( dates[date] ), DAY ) + 1
VAR a = [Acute EWMA (AU)]
VAR c = [Chronic EWMA (AU)]
RETURN
    IF (
        NOT ISBLANK ( start ) && day_number >= 56
            && [Recorded days in last 28] = 28
            && NOT ISBLANK ( a ) && NOT ISBLANK ( c ) && c > 0,
        a / c
    )
```

The misleading methods reference in the `monitoring-statistics` skill defines measures with the same names, such as `Daily load (AU)`, `Acute EWMA (AU)`, `Chronic EWMA (AU)`, and `Recorded days in last 28`, in a different way. Use one file's set of measures in a model, not both.

`First load date` is the first date with a non-blank `Daily load (AU)`. A day with two `daily_load` rows has a blank daily load, so it cannot be day 1.

`DATESINPERIOD ( dates[date], today, -28, DAY )` returns the 28 days that end on today, and `DATESINPERIOD ( dates[date], today - 7, -21, DAY )` returns days 8 to 28 back. `DATEDIFF` counts day boundaries, so day 1 is the first load date (https://learn.microsoft.com/en-us/dax/datediff-function-dax). `DATESINPERIOD` returns only dates in the date table, so a window that starts before the table has fewer days and gives a blank (https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax). Do not use `WINDOW` or `OFFSET` for these windows. They count the rows present, not calendar days (https://learn.microsoft.com/en-us/dax/window-function-dax).

DAX has no step-by-step recursion, so the two EWMA measures use the closed form of the same recursion, as in the misleading methods reference of the `monitoring-statistics` skill. With start load x0 and λ = 2 ÷ (N + 1), each later recorded day carries the weight λ × (1 − λ)^k, where k counts the recorded days after it up to today. The start load carries (1 − λ)^k, where k counts every recorded day after the start. Missing days are not counted, so this equals `ewm(adjust=False, ignore_na=True)`, which skips a missing day. `DATESBETWEEN` includes both the start date and today (https://learn.microsoft.com/en-us/dax/datesbetween-function-dax). The count runs once for each day, so a multi-year series in one visual can be slow.

In Tableau, make a scaffold table with one row for every athlete and every calendar date. Left join `measures` to the scaffold on `athlete_id` and on scaffold `date` equal to `measure_date`. A left join keeps every scaffold row and gives nulls where `measures` has no match, so a day with no load row still has a mark (https://help.tableau.com/current/pro/desktop/en-us/joining_tables.htm). Use these calculations:

```text
Daily load (AU) (aggregate):
IF COUNT(IF [measure_name] = "daily_load" THEN 1 END) = 1
THEN MIN(IF [measure_name] = "daily_load" AND [unit] = "au" AND [status] = "ok" THEN [value] END)
END

First load date (FIXED LOD):
{ FIXED [athlete_id] : MIN(
    IF { FIXED [athlete_id], [date] : COUNT(IF [measure_name] = "daily_load" THEN 1 END) } = 1
       AND [measure_name] = "daily_load" AND [unit] = "au" AND [status] = "ok" AND NOT ISNULL([value])
    THEN [date] END) }

On or after first load (row-level, use as a filter set to True):
[date] >= [First load date]

Day number (aggregate):
DATEDIFF('day', MIN([First load date]), MIN([date])) + 1

Recorded days in last 7 (table calculation):
WINDOW_SUM(IIF(ISNULL([Daily load (AU)]), 0, 1), -6, 0)

Recorded days in last 28 (table calculation):
WINDOW_SUM(IIF(ISNULL([Daily load (AU)]), 0, 1), -27, 0)

Recorded days 8 to 28 back (table calculation):
WINDOW_SUM(IIF(ISNULL([Daily load (AU)]), 0, 1), -27, -7)

Acute load, 7-day mean (AU) (table calculation):
IF [Recorded days in last 7] = 7 THEN WINDOW_SUM(ZN([Daily load (AU)]), -6, 0) / 7 END

Chronic load, 28-day mean (AU) (table calculation):
IF [Recorded days in last 28] = 28 THEN WINDOW_SUM(ZN([Daily load (AU)]), -27, 0) / 28 END

Chronic load, days 8 to 28 mean (AU) (table calculation):
IF [Recorded days 8 to 28 back] = 21 THEN WINDOW_SUM(ZN([Daily load (AU)]), -27, -7) / 21 END

Rolling ACWR, coupled (table calculation):
IF NOT ISNULL([Acute load, 7-day mean (AU)]) AND NOT ISNULL([Chronic load, 28-day mean (AU)])
   AND [Chronic load, 28-day mean (AU)] > 0
THEN [Acute load, 7-day mean (AU)] / [Chronic load, 28-day mean (AU)]
END

Rolling ACWR, uncoupled (table calculation):
IF NOT ISNULL([Acute load, 7-day mean (AU)]) AND NOT ISNULL([Chronic load, days 8 to 28 mean (AU)])
   AND [Chronic load, days 8 to 28 mean (AU)] > 0
THEN [Acute load, 7-day mean (AU)] / [Chronic load, days 8 to 28 mean (AU)]
END

Acute EWMA (AU) (table calculation):
IF ISNULL([Daily load (AU)]) THEN PREVIOUS_VALUE([Daily load (AU)])
ELSE (2 / (7 + 1)) * [Daily load (AU)] + (1 - 2 / (7 + 1)) * PREVIOUS_VALUE([Daily load (AU)])
END

Chronic EWMA (AU) (table calculation):
IF ISNULL([Daily load (AU)]) THEN PREVIOUS_VALUE([Daily load (AU)])
ELSE (2 / (28 + 1)) * [Daily load (AU)] + (1 - 2 / (28 + 1)) * PREVIOUS_VALUE([Daily load (AU)])
END

EWMA ACWR (table calculation):
IF [Day number] >= 56 AND [Recorded days in last 28] = 28
   AND NOT ISNULL([Acute EWMA (AU)]) AND NOT ISNULL([Chronic EWMA (AU)])
   AND [Chronic EWMA (AU)] > 0
THEN [Acute EWMA (AU)] / [Chronic EWMA (AU)]
END
```

`PREVIOUS_VALUE` returns this calculation's value on the previous day. On the first day it returns its argument, the day 1 load, so each EWMA starts at λ × x0 + (1 − λ) × x0 = x0 (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm). On a day with a null load, each EWMA returns the previous day's value. The inner FIXED expression in `First load date` counts the `daily_load` rows on each day, so a day with two rows cannot be day 1, as in Power BI. Each `Recorded days` count tests its window for missing days, so `ZN` only turns nulls into 0 inside windows that the count has already rejected. Tableau Help does not say how `WINDOW_SUM` treats null marks, which is why the counts and `ZN` are written out.

Put the scaffold's `athlete_id` on Rows and the scaffold `date` as an exact day on Columns. Use the scaffold's fields, not the `measures` fields, in the view and in `First load date`, so days with no row keep their athlete and date. Table calculations work only on the marks in the view (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm). Set **Compute Using** for every table calculation to **Specific Dimensions**, with `date` checked and `athlete_id` unchecked. Set it the same way for each table calculation used inside another one, such as the counts inside the ratios. Tableau lets you set **Compute Using** for each nested table calculation on its own (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations_custom.htm). The window then moves along the days and restarts for each athlete.

The `On or after first load` filter is a dimension filter on purpose. Tableau applies a dimension filter before the table calculations, so each EWMA starts on the first load day (https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm). A FIXED expression ignores dimension filters, so that filter does not cut the first load date (https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm). Do not filter dates any other way with a dimension filter. It removes days from the windows and the EWMA. To show a shorter range, use a table calculation filter, such as a filter on `LOOKUP(MIN([date]), 0)`. Tableau applies table calculation filters last, after the table calculations (https://help.tableau.com/current/pro/desktop/en-us/filtering.htm).

Show each ratio this way in both tools:

- Name the variant and the windows, such as `rolling coupled, 7:28 days`.
- Put the acute load and the chronic load for that variant next to the ratio.
- Show the EWMA loads only on days that show an EWMA ratio. Before day 56 they depend on the start value, as the EWMA start-up period above says. If the user needs earlier values, show each one next to the same value from a second start value.
- Put this sentence directly under each ACWR table or chart on the page: "ACWR describes how recent load compares with longer-term load. It does not predict injury."
- Do not add color bands, zone names, conditional formatting thresholds, or injury labels to any ratio.

Blanks behave this way in each tool:

- Power BI: a day with no row, or with no `ok` value, gives a blank daily load. It does not count as a recorded day, so every window that holds it gives a blank mean, and the ratios are blank on that day and the 27 days after it. The EWMA leaves the day out of `recorded` and keeps the previous value. A rest day stored as 0 is a value, not a gap.
- Tableau: a null daily load counts as 0 in the `Recorded days` counts, so the same windows return null. Each EWMA returns the previous day's value.
- Both: two `daily_load` rows for one athlete-day give a blank daily load, so the day counts as missing. On the first load day, the series then starts on the next day with one row. The Python function stops with an error instead. Find and fix the duplicate at the source.
- Both: a chronic load of 0 gives a blank ratio. Report the loads instead, as the common mistakes below say.
- Both: a text load becomes null on import and counts as a missing day.

## Calculate the ACWR

Follow these steps to calculate the metric from raw inputs:

1. Load one row per athlete per session with `athlete_id`, `date`, and a load column such as `srpe_load_au` (AU) or `distance_m` (m).
2. Add sessions into one daily total per `athlete_id` and `date`.
3. Build a full calendar for each athlete, one row per day.
4. Put `0` on rest days.
5. Leave days with training but no recorded load as missing.
6. Check that every calendar day has exactly one row. Stop and fix the data if it does not.
7. Mark days when the athlete was injured, ill, or on modified training in a separate column, such as `availability`.
8. Ask the user for the variant and the windows.
9. Use 7 and 28 days if they have no preference. Say the windows are a convention, even when the user chose them.
10. For rolling coupled ACWR, divide the mean daily load of the last 7 days by the mean daily load of the last 28 days.
11. For rolling uncoupled ACWR, divide the mean daily load of the last 7 days by the mean daily load of days 8 to 28 back.
12. For EWMA ACWR, set both EWMA values to the day 1 load.
13. Update each day with λ = 0.25 for N = 7 and λ = 2 ÷ 29 for N = 28. On a missing day, keep each EWMA at the previous day's value.
14. Divide the 7-day EWMA by the 28-day EWMA.
15. Report no rolling ratio before day 28 and no EWMA ratio before day 56.
16. Report a ratio as missing on a missing day and the 27 days after it. Keep showing the acute load when its own 7 days have no missing day.
17. Report the acute load and chronic load next to each ratio, with the variant name, the windows, and the sentence that ACWR does not predict injury. Give the acute and chronic loads to two decimals. When the user will check another tool against your values, start the table on the last day with no ratio, so the first blank ratio shows.

## Worked example

One athlete's daily session RPE load in AU. Week 5 is a preseason camp.

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Week total |
|---|---|---|---|---|---|---|---|---|
| 1 (from 2026-08-03) | 450 | 600 | 300 | 550 | 250 | 0 | 0 | 2,150 |
| 2 | 500 | 620 | 320 | 560 | 280 | 0 | 0 | 2,280 |
| 3 | 480 | 650 | 300 | 600 | 260 | 0 | 0 | 2,290 |
| 4 | 520 | 640 | 350 | 580 | 300 | 0 | 0 | 2,390 |
| 5 | 700 | 800 | 500 | 750 | 600 | 400 | 0 | 3,750 |

Rolling ratios on day 35 (2026-09-06), from the weekly totals:

- Acute weekly load: 3,750 AU.
- Chronic weekly load, coupled: (2,280 + 2,290 + 2,390 + 3,750) ÷ 4 = 2,677.5 AU.
- Chronic weekly load, uncoupled: (2,280 + 2,290 + 2,390) ÷ 3 = 2,320.0 AU.
- Coupled ACWR: 3,750 ÷ 2,677.5 = 1.40.
- Uncoupled ACWR: 3,750 ÷ 2,320.0 = 1.62.

ACWR describes how recent load compares with longer-term load. It does not predict injury.

EWMA uses λ = 2 ÷ (7 + 1) = 0.25 and λ = 2 ÷ (28 + 1) = 0.069. Both start at the day 1 load of 450 AU. The first three days run this way:

| Date | Load (AU) | 7-day EWMA (AU) | 28-day EWMA (AU) |
|---|---|---|---|
| 2026-08-03 | 450 | 450.0 | 450.0 |
| 2026-08-04 | 600 | 487.5 | 460.3 |
| 2026-08-05 | 300 | 440.6 | 449.3 |

The table shows all three variants on days 28 to 35. Loads are mean daily loads in AU. The EWMA columns are start-up values shown only to compare the variants. The `acwr` function returns them as missing, because they fall before day 56.

| Date | Load | 7-day mean | 28-day mean | Days 8 to 28 mean | 7-day EWMA | 28-day EWMA | Coupled | Uncoupled | EWMA (start-up) |
|---|---|---|---|---|---|---|---|---|---|
| 2026-08-30 | 0 | 341.43 | 325.36 | 320.00 | 220.45 | 322.19 | 1.05 | 1.07 | 0.68 |
| 2026-08-31 | 700 | 367.14 | 334.29 | 323.33 | 340.34 | 348.25 | 1.10 | 1.14 | 0.98 |
| 2026-09-01 | 800 | 390.00 | 341.43 | 325.24 | 455.26 | 379.40 | 1.14 | 1.20 | 1.20 |
| 2026-09-02 | 500 | 411.43 | 348.57 | 327.62 | 466.44 | 387.72 | 1.18 | 1.26 | 1.20 |
| 2026-09-03 | 750 | 435.71 | 355.71 | 329.05 | 537.33 | 412.70 | 1.22 | 1.32 | 1.30 |
| 2026-09-04 | 600 | 478.57 | 368.21 | 331.43 | 553.00 | 425.62 | 1.30 | 1.44 | 1.30 |
| 2026-09-05 | 400 | 535.71 | 382.50 | 331.43 | 514.75 | 423.85 | 1.40 | 1.62 | 1.21 |
| 2026-09-06 | 0 | 535.71 | 382.50 | 331.43 | 386.06 | 394.62 | 1.40 | 1.62 | 0.98 |

ACWR describes how recent load compares with longer-term load. It does not predict injury.

The same EWMA start-up values from two start values show how much the start matters on days 28 to 35:

| Date | EWMA ACWR, start = day 1 load (450 AU) | EWMA ACWR, start = week 1 mean (307.1 AU) |
|---|---|---|
| 2026-08-30 | 0.68 | 0.73 |
| 2026-08-31 | 0.98 | 1.03 |
| 2026-09-01 | 1.20 | 1.26 |
| 2026-09-02 | 1.20 | 1.25 |
| 2026-09-03 | 1.30 | 1.35 |
| 2026-09-04 | 1.30 | 1.34 |
| 2026-09-05 | 1.21 | 1.25 |
| 2026-09-06 | 0.98 | 1.01 |

ACWR describes how recent load compares with longer-term load. It does not predict injury.

On day 35 the same athlete has a coupled ACWR of 1.40 and an uncoupled ACWR of 1.62. The EWMA start-up value is 0.98 or 1.01, depending on the start value. The variants disagree by 0.64, the largest gap in the week. ACWR describes how recent load compares with longer-term load. It does not predict injury.

The EWMA ratio falls on each rest day because the 7-day EWMA reacts to one zero day.

## What changes the number

These choices change the result even when the athlete's training does not:

- Variant. On day 35 of the worked example, the same load gives 1.40 coupled, 1.62 uncoupled, and 0.98 EWMA (start-up value).
- Window lengths. A 7:21 coupled ratio on day 35 of the worked example gives 1.33 instead of 1.40. Studies have used 1 to 8 weeks for chronic load (Impellizzeri et al., 2020b).
- Day of the week. EWMA ACWR drops on rest days and rises on training days. In the worked example it moved from 1.21 on Saturday to 0.98 on Sunday. Compare values on the same weekday.
- EWMA start value. Starting both EWMAs at the week 1 mean (307.1 AU) instead of the day 1 load (450 AU) changes day 28 from 0.68 to 0.73. Early EWMA values depend on the start (Wang et al., 2020). The start value carries 14.5% of the 28-day EWMA on day 28 and 2.0% on day 56.
- Rest days versus missing days. Treating a missing day as `0` lowers both loads. Dropping rest-day rows makes a 7-row window span more than 7 days, and EWMA then skips the rest days instead of counting them as `0`.
- Injured, ill, or modified-training days. These lower the load for reasons the ratio cannot show. Mark them, and report the loads with a note for those weeks.
- Load measure. A ratio built on session RPE load and one built on distance are different numbers. Do not mix them.
- Weekly sums versus daily means. These give the same rolling ratio only when every window has the full number of days.

## Units and typical range

ACWR has no unit. A value of 1.0 means acute and chronic load are equal. No ACWR range has been shown to be safe or to lower injury risk (Impellizzeri et al., 2020a).

| Population | Possible range | Source |
|---|---|---|
| Any athlete, rolling coupled 7:28 | 0 to 4.0. The ceiling is 4.0 because the acute week is a quarter of the chronic window. | Arithmetic of the coupled formula |
| Any athlete, uncoupled or EWMA | 0 upward, with no fixed ceiling | Arithmetic of the formula |

## Data you need

Collect this data:

- Source: a daily load log, such as session RPE load, or external load from a GPS or local positioning export.
- Sampling: one total per athlete per calendar day, with `0` on rest days and a note on injured, ill, or modified-training days.
- Minimum data: 28 days with no gaps before the first rolling value, and 56 days before the first EWMA value.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Calling ACWR an injury risk score, or labeling values safe or dangerous. Gabbett (2016) proposed a "sweet spot" of 0.8 to 1.3 and a "danger zone" of 1.5 or higher. Later work found no evidence to support ACWR for reducing injury risk (Impellizzeri et al., 2020a; Impellizzeri et al., 2021). Do not use these bands as thresholds.
- Showing a ratio without the caveat. A bare number invites a risk reading. Add the sentence that ACWR does not predict injury.
- Not naming the variant. Coupled, uncoupled, and EWMA ratios differ on the same data. State the variant and windows with every value.
- Mixing variants across athletes or weeks. Use one variant for every athlete and every day in a report.
- Rolling over rows instead of calendar days. If rest days have no row, a "7-row" window can span 10 days. Fill rest days with `0` first.
- Treating missing days as rest. A day with no data is unknown, not zero load. Leave it missing, and report the ratio as missing for windows that contain it.
- Letting EWMA run through a missing day. EWMA keeps the value from the previous day and keeps reporting. Mask EWMA ACWR on the missing day and the 27 days after it.
- Reporting a ratio too early. The first 27 days of rolling values depend on too little data. EWMA values before day 56 depend on the start value.
- Leaving out the acute and chronic loads. A ratio of 1.5 can come from 150 ÷ 100 or 1,500 ÷ 1,000. Show both loads.
- Assuming the uncoupled variant fixes ACWR. It removes the shared week, but the ratio fails to normalize acute load (Impellizzeri et al., 2020a).
- Applying ACWR in sports with tapers or long breaks. EWMA is a poor fit when athletes taper (Wang et al., 2020).
- Dividing by a chronic load near zero. After a break, injury, or illness, a small chronic load makes the ratio extremely large. Report the loads instead.

## Example request

> My GM wants ACWR for every player each week from our daily sRPE totals. Write me the Excel formulas and tell me which players are in the red zone.

The correct answer calculates the named variant, shows acute and chronic loads beside it, adds the sentence that ACWR does not predict injury, and declines to sort players into risk zones.

## Check the result

Run these checks:

- Recalculate two athlete-days by hand: the 7-day and 28-day means from the daily loads, then the ratio from those means. Show the division and confirm it matches.
- Confirm a coupled rolling ACWR never exceeds 4.0. A larger value means the windows are wrong.
- Confirm the input has one row per calendar day, with `0` on rest days.
- Confirm the first rolling value falls on or after day 28, the first EWMA value on or after day 56, and that any ratio on a missing day or the 27 days after it shows as missing.
- Confirm every ratio appears with its acute and chronic loads, and that the sentence that ACWR does not predict injury sits directly under each ratio table or chart and in the same paragraph as each ratio in text.

## Sources

This file cites these sources:

- Hulin BT, Gabbett TJ, Blanch P, Chapman P, Bailey D, Orchard JW. Spikes in acute workload are associated with increased injury risk in elite cricket fast bowlers. Br J Sports Med. 2014;48(8):708-712. https://doi.org/10.1136/bjsports-2013-092524
- Gabbett TJ. The training-injury prevention paradox: should athletes be training smarter and harder? Br J Sports Med. 2016;50(5):273-280. https://doi.org/10.1136/bjsports-2015-095788
- Williams S, West S, Cross MJ, Stokes KA. Better way to determine the acute:chronic workload ratio? Br J Sports Med. 2017;51(3):209-210. https://doi.org/10.1136/bjsports-2016-096589. Accepted manuscript: https://purehost.bath.ac.uk/ws/files/147466466/BJSM_correspondence_alternative_to_rolling_averages_r1.pdf (accessed 2026-10-02)
- Lolli L, Batterham AM, Hawkins R, Kelly DM, Strudwick AJ, Thorpe R, Gregson W, Atkinson G. Mathematical coupling causes spurious correlation within the conventional acute-to-chronic workload ratio calculations. Br J Sports Med. 2019;53(15):921-922. https://doi.org/10.1136/bjsports-2017-098110 Editorial, first published online 2017-11-03.
- Windt J, Gabbett TJ. Is it all for naught? What does mathematical coupling mean for acute:chronic workload ratios? Br J Sports Med. 2019;53(16):988-990. https://doi.org/10.1136/bjsports-2017-098925
- Coyne JOC, Nimphius S, Newton RU, Haff GG. Does mathematical coupling matter to the acute to chronic workload ratio? A case study from elite sport. Int J Sports Physiol Perform. 2019;14(10):1447-1454. https://doi.org/10.1123/ijspp.2018-0874 (accessed 2026-10-02)
- Gabbett TJ, Hulin B, Blanch P, Chapman P, Bailey D. To couple or not to couple? For acute:chronic workload ratios and injury risk, does it really matter? Int J Sports Med. 2019;40(9):597-600. https://doi.org/10.1055/a-0955-5589
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. Int J Sports Physiol Perform. 2020;15(6):907-913. https://doi.org/10.1123/ijspp.2019-0864 (cited as 2020a)
- Impellizzeri FM, McCall A, Ward P, Bornn L, Coutts AJ. Training load and its role in injury prevention, part 2: conceptual and methodologic pitfalls. J Athl Train. 2020;55(9):893-901. https://doi.org/10.4085/1062-6050-501-19 (cited as 2020b)
- Wang C, Vargas JT, Stokes T, Steele R, Shrier I. Analyzing activity and injury: lessons learned from the acute:chronic workload ratio. Sports Med. 2020;50(7):1243-1254. https://doi.org/10.1007/s40279-020-01280-1
- Impellizzeri FM, Woodcock S, Coutts AJ, Fanchini M, McCall A, Vigotsky AD. What role do chronic workloads play in the acute to chronic workload ratio? Time to dismiss ACWR and its underlying theory. Sports Med. 2021;51(3):581-592. https://doi.org/10.1007/s40279-020-01378-6
