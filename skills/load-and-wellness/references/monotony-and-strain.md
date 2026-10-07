# Training monotony and strain

Last checked: 2026-10-07

## What it measures

Training monotony describes how evenly an athlete's load was spread across the days of one week. Training strain combines the week's total load with its monotony.

A week with the same hard session every day has high monotony. A week that mixes hard days, easy days, and rest days has low monotony. Strain is high when the weekly load is high and the days are alike.

Read these limits before you use them:

- Monotony and strain do not predict injury or illness. Foster (1998) followed 25 athletes. The abstract reports that a high share of their illnesses could be accounted for when athletes passed thresholds identified for each athlete, mostly thresholds of strain. That explains past illnesses in the same athletes. The abstract describes no test of whether strain predicts illness in new data.
- In the summary by Jones et al. (2017) of Foster (1998), spikes above each athlete's own threshold came before 77% of illnesses for monotony and 89% for strain. Yet 52% of the monotony spikes and 59% of the strain spikes were not followed by illness. A value that passes a threshold more often without illness than with it cannot sort athletes into those who will and will not fall ill.
- A systematic review found conflicting evidence for monotony and strain. It concluded that the literature does not support their role in monitoring and injury prevention (Jones et al., 2017). This file uses them only to describe a week.
- Training-load measures cannot tell you whether a change in load raises or lowers injury risk (Impellizzeri et al., 2020b). Rely on training principles and the athlete's response.

Use monotony and strain only to describe how a week's load was spread. Report the weekly load and the daily loads next to them.

Put this sentence directly under each monotony or strain table or chart, and in the same paragraph as each monotony or strain value in text, not once per answer:

> Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

A bare value such as "strain 6,000" reads like a warning level. No monotony or strain value has been shown to be safe or unsafe.

## Formula

Use the weekly form described by Haddad et al. (2017), from Foster (1998):

```text
weekly_load_au = sum of the 7 daily loads
monotony       = mean daily load over the 7 days ÷ SD of the 7 daily loads
strain_au      = weekly_load_au × monotony
```

Define every term in the formula:

- Daily load: the sum of all session loads on one calendar day, in the load's unit. For session RPE load this is AU (arbitrary units), from `rpe_cr10 × duration_min` for each session (Foster et al., 2001). See [session-rpe-load.md](session-rpe-load.md).
- `weekly_load_au`: the sum of the 7 daily loads, in AU.
- Mean daily load: `weekly_load_au ÷ 7`, in AU. Haddad et al. (2017) define it as the average daily load during the week.
- SD: standard deviation, how far the 7 daily loads spread around their mean, in AU. Haddad et al. (2017) define it as the SD of the daily load over the week.
- `monotony`: no unit, because AU divided by AU cancels. Monotony is 1 ÷ the coefficient of variation (CV), where CV = SD ÷ mean.
- `strain_au`: the weekly load multiplied by monotony (Haddad et al., 2017). Monotony has no unit, so strain keeps the unit of the load, AU for session RPE load.

The Foster (1998) abstract defines monotony as the daily mean divided by the SD, and strain as load multiplied by monotony. The abstract does not state the window, the type of SD, or how rest days were handled. We could not read the full text, so this file takes the weekly form from Haddad et al. (2017).

### Count rest days as zero

Count every day of the 7, with `0` AU on a rest day. A rest day is a real load of zero, as in [session-rpe-load.md](session-rpe-load.md). The sources we could read define the mean as the average daily load during the week, but none states the rest-day rule in words. This file's rule is to count all 7 days.

Leaving rest days out changes the result. In the worked example below, dropping the Sunday rest day raises monotony from 1.48 to 2.09.

### Choose the sample or population SD

Two SDs are in use. They give different monotony values from the same week:

- Sample SD: divides the sum of squared differences from the mean by n − 1, here 6. Excel `STDEV.S` and Google Sheets `STDEV` compute it. So do R `sd()`, Python `statistics.stdev()`, and pandas `.std()` by default.
- Population SD: divides by n, here 7. Excel `STDEV.P` and Google Sheets `STDEVP` compute it. So do Python `statistics.pstdev()` and NumPy `np.std()` by default.

The sources we could read do not say which SD Foster used. This file uses the sample SD as its default, labeled as this file's choice, because the default SD in most of these tools is the sample SD. The population SD is not wrong. Name the SD with every value, and use one SD for the whole series.

For a 7-day week, the population SD is always smaller, so monotony and strain from the population SD are always √(7 ÷ 6) = 1.080 times the values from the sample SD. That is 8.0% higher.

Watch for NumPy. `np.std()` gives the population SD unless you pass `ddof=1`. pandas `.std()` gives the sample SD unless you pass `ddof=0`.

### Handle a week with identical daily loads

If all 7 daily loads are the same, the SD is 0 and monotony is undefined, because you cannot divide by 0. Strain is undefined too. Report the weekly load and the status `no variation`. Do not report infinity, a very large number, or 0.

Monotony also grows without limit as the SD gets close to 0. A week of six days at 400 AU and one at 410 AU gives a sample SD of 3.78 AU and a monotony of 106.21. A week with no rest day can give a very large monotony from a tiny difference. Report the daily loads with it.

A week that has at least one rest day at 0 AU cannot have a monotony above 6 ÷ √7 = 2.27 with the sample SD, or √6 = 2.45 with the population SD. The highest value comes from one rest day and six equal days. These bounds come from the arithmetic of the formula.

### Choose calendar or rolling weeks

Two windows are in use. Name the window with every value:

- Calendar week: a fixed week, Monday to Sunday unless the user names another start day. Report one value per week, on its last day. This matches the weekly load in [session-rpe-load.md](session-rpe-load.md).
- Rolling week: the 7 days ending on each day. Report one value per day.

The rolling value on the last day of a calendar week equals the calendar value. On other days it differs, and it depends on which weekday the window ends. In the worked example, the rolling monotony on Friday 2026-08-14 is 1.75, while the two calendar weeks around it are 1.48 and 1.28. Compare rolling values on the same weekday. If the user has no preference, use calendar weeks and label that as this file's choice.

### Add sessions before you calculate

Add every session on a day into one daily load first. Then calculate the mean and SD across the 7 daily loads. Do not treat each session as its own value. In the worked example, using the 7 session loads plus the rest day as 8 values gives a monotony of 1.42 instead of 1.48.

### Keep missing days missing

A missing day is a day with training but no recorded load, such as a session with no RPE rating. It is not a rest day. Do not put `0` on it. Do not calculate monotony from the days you have.

Report monotony and strain as missing for any week, or any rolling window, that contains a missing day. Report the weekly load with the number of days it covers, such as 6 of 7 days, as [session-rpe-load.md](session-rpe-load.md) says. In the worked example, entering a missing Wednesday as 0 gives a monotony of 1.16 instead of 1.48, and the week looks lighter and more varied than it was.

If the `ams-data-setup` skill is installed, its missing data reference, in the section on averages and sums, covers zeros, missing codes, and coverage in more detail. Fill a missing day only when the user asks, and name the method.

### Calculate it in a spreadsheet

Use one row per athlete per calendar day, sorted by athlete and then date. Put `athlete_id` in column `A`, the date in column `B`, and the daily load in AU in column `C`. Put `0` on rest days. Leave a missing day blank, or write `NA`. Enter these formulas in row 8, which covers rows 2 to 8, and fill them down:

```text
Days recorded, D8: =COUNT(C2:C8)
Weekly load, E8:   =IF(AND(COUNTIF(A2:A8,A8)=7,B8-B2=6,COUNT(C2:C8)=7),SUM(C2:C8),"")
SD, F8:            =IF(E8="","",STDEV.S(C2:C8))
Monotony, G8:      =IF(OR(F8="",F8=0),"",AVERAGE(C2:C8)/F8)
Strain, H8:        =IF(G8="","",E8*G8)
Status, I8:        =IF(OR(COUNTIF(A2:A8,A8)<7,B8-B2<>6),"not 7 days of one athlete",IF(COUNT(C2:C8)<7,"missing day",IF(F8=0,"no variation","ok")))
Week end, J8:      =WEEKDAY(B8,2)=7
```

These formulas give a rolling week on every row. For Monday-to-Sunday calendar weeks, filter column `J` to `TRUE`. `WEEKDAY` with return type 2 numbers Monday as 1 and Sunday as 7.

The tests in the formulas work this way:

- `COUNTIF(A2:A8,A8)=7` checks that all 7 rows belong to one athlete.
- `B8-B2=6` checks that the 7 rows span 7 calendar days. A day with no row, or a date entered twice, fails this test.
- `COUNT` counts numbers only, so a blank, `NA`, or a number stored as text counts as a missing day. `STDEV.S` ignores empty cells and text in a range (Microsoft, STDEV.S function).

For the population SD, use `STDEV.P` in Excel. In Google Sheets, `STDEV` is the sample SD and `STDEVP` is the population SD.

A plain `=AVERAGE(C2:C8)/STDEV.S(C2:C8)` skips a blank day, so it calculates monotony from 6 days without warning. It also gives `#DIV/0!` on a week of identical loads.

### Calculate it in Python

Use this function for one athlete with one row per calendar day:

```python
import pandas as pd

def monotony_strain(load, ddof=1):
    """load: one athlete, one row per calendar day, DatetimeIndex, 0 on rest days, NaN if not recorded.
    ddof=1 gives the sample SD (n - 1). ddof=0 gives the population SD (n)."""
    load = load.sort_index()
    full = pd.date_range(load.index.min(), load.index.max(), freq="D")
    if load.index.has_duplicates or len(load) != len(full):
        raise ValueError("Need one row per calendar day. Add rest days as 0 first.")
    win = load.rolling(7, min_periods=7)      # any missing day in the window gives NaN
    weekly = win.sum()
    sd = win.std(ddof=ddof)
    monotony = (weekly / 7 / sd).where(sd.round(9) > 0)   # SD of 0: monotony undefined
    return pd.DataFrame({"load": load, "days_recorded": load.rolling(7, min_periods=1).count(),
                         "weekly_load": weekly, "sd": sd,
                         "monotony": monotony, "strain": weekly * monotony})
```

The result is a rolling week on every day. For Monday-to-Sunday calendar weeks, keep the Sundays: `out[out.index.dayofweek == 6]`.

The function stops if any calendar day has no row, because a missing rest-day row would turn a rest day into a missing day. It returns monotony and strain as missing for any window with a missing day, and for a window with an SD of 0. `round(9)` stops rounding error from hiding an SD of 0.

### Calculate it in Power BI and Tableau

These versions follow the spreadsheet and Python rules. They use a rolling 7-day window and the sample SD. A window with a missing day gives a blank. A window with an SD of 0 gives a blank monotony and strain.

Both versions use the same table setup as [acwr.md](acwr.md#calculate-it-in-power-bi-and-tableau): one `daily_load` row per athlete and calendar day in a `measures` table, with `unit` `au` and `status` `ok`. Use one load measure for every athlete and every day.

In Power BI, use the marked date table `dates` and the `Daily load (AU)` measure from [acwr.md](acwr.md#calculate-it-in-power-bi-and-tableau). Put `athletes[athlete_id]` and `dates[date]` in the visual. Use these DAX measures:

```text
Recorded days in last 7 =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
        DATESINPERIOD ( dates[date], today, -7, DAY )
    )
RETURN COUNTROWS ( FILTER ( days, NOT ISBLANK ( [@x] ) ) ) + 0

Weekly load, last 7 days (AU) =
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
        SUMX ( recorded, [@x] )
    )

SD of daily load, last 7 days (AU) =
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
        STDEVX.S ( recorded, [@x] )
    )

Monotony, last 7 days =
VAR w = [Weekly load, last 7 days (AU)]
VAR sd = [SD of daily load, last 7 days (AU)]
RETURN IF ( NOT ISBLANK ( w ) && NOT ISBLANK ( sd ) && ROUND ( sd, 9 ) > 0, ( w / 7 ) / sd )

Strain, last 7 days (AU) =
VAR w = [Weekly load, last 7 days (AU)]
VAR m = [Monotony, last 7 days]
RETURN IF ( NOT ISBLANK ( w ) && NOT ISBLANK ( m ), w * m )

Monotony status =
SWITCH (
    TRUE (),
    [Recorded days in last 7] < 7, "missing day in window",
    ROUND ( [SD of daily load, last 7 days (AU)], 9 ) = 0, "no variation",
    "ok"
)
```

For the population SD, use `STDEVX.P` instead of `STDEVX.S`. `STDEVX.S` divides by n − 1, skips blank rows, and returns an error with fewer than 2 rows (https://learn.microsoft.com/en-us/dax/stdevx-s-function-dax). The `= 7` test means it always gets 7 rows.

For calendar weeks, add a calculated column `is_week_end = WEEKDAY ( dates[date], 2 ) = 7` to `dates`, and filter the visual to `TRUE`. With return type 2, Monday is 1 and Sunday is 7 (https://learn.microsoft.com/en-us/dax/weekday-function-dax). The filter does not cut the window, because `DATESINPERIOD` reads the earlier days from the date table.

The Power BI measures in `acwr.md` do not include `Recorded days in last 7`, so the name does not clash. The misleading methods reference in the `monitoring-statistics` skill defines some measures with the same names as `acwr.md` in a different way. Use one file's set of measures in a model, not both.

In Tableau, use the scaffold table and the `Daily load (AU)` and `Recorded days in last 7` calculations from [acwr.md](acwr.md#calculate-it-in-power-bi-and-tableau). Use these calculations:

```text
Weekly load, last 7 days (AU) (table calculation):
IF [Recorded days in last 7] = 7 THEN WINDOW_SUM(ZN([Daily load (AU)]), -6, 0) END

SD of daily load, last 7 days (AU) (table calculation):
IF [Recorded days in last 7] = 7 THEN WINDOW_STDEV([Daily load (AU)], -6, 0) END

Monotony, last 7 days (table calculation):
IF NOT ISNULL([SD of daily load, last 7 days (AU)])
   AND ROUND([SD of daily load, last 7 days (AU)], 9) > 0
THEN ([Weekly load, last 7 days (AU)] / 7) / [SD of daily load, last 7 days (AU)]
END

Strain, last 7 days (AU) (table calculation):
IF NOT ISNULL([Monotony, last 7 days])
THEN [Weekly load, last 7 days (AU)] * [Monotony, last 7 days]
END

Monotony status (table calculation):
IF [Recorded days in last 7] < 7 THEN "missing day in window"
ELSEIF ROUND([SD of daily load, last 7 days (AU)], 9) = 0 THEN "no variation"
ELSE "ok"
END

Week end (table calculation, use as a filter set to True):
DATEDIFF('day', #2000-01-02#, LOOKUP(MIN([date]), 0)) % 7 = 0
```

`WINDOW_STDEV` returns the sample SD, and `WINDOW_STDEVP` returns the population SD (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm). Tableau Help does not say how they treat null marks. The `Recorded days in last 7` test means the window has no null when the SD is used.

2000-01-02 was a Sunday, so `Week end` is true on Sundays, for Monday-to-Sunday weeks. It is a table calculation filter on purpose. Tableau applies table calculation filters last, so the filter does not remove days from the 7-day window (https://help.tableau.com/current/pro/desktop/en-us/filtering.htm). A dimension filter on the weekday would remove the other six days from every window.

Set **Compute Using** for every table calculation, and for each nested one, to **Specific Dimensions**, with the scaffold `date` checked and `athlete_id` unchecked, as [acwr.md](acwr.md#calculate-it-in-power-bi-and-tableau) describes. The window then moves along the days and restarts for each athlete.

Show the results this way in both tools:

- Name the SD and the window, such as `sample SD, calendar week Monday to Sunday`.
- Put the weekly load next to monotony and strain.
- Put the monotony and strain caveat sentence directly under each table or chart.
- Do not add color bands, zone names, conditional formatting thresholds, or injury or illness labels.

Blanks behave this way in each tool:

- Power BI: a day with no row, or with no `ok` value, gives a blank daily load. It does not count as a recorded day, so every window that holds it gives a blank weekly load, SD, monotony, and strain. A rest day stored as 0 is a value, not a gap.
- Tableau: a null daily load counts as 0 in `Recorded days in last 7`, so the same windows return null.
- Both: two `daily_load` rows for one athlete-day give a blank daily load, so the day counts as missing. The Python function stops with an error instead. Fix the duplicate at the source.
- Both: an SD of 0 gives a blank monotony and strain, and the status `no variation`.

## Calculate monotony and strain

Follow these steps to calculate the metric from raw inputs:

1. Calculate each session's load, such as session RPE load in AU from `rpe_cr10 × duration_min`. Keep a session load missing if its rating or duration is missing.
2. Add session loads into one daily load per `athlete_id` and `date`. Mark the day as missing if any session that day has a missing load.
3. Build a full calendar for each athlete, one row per day.
4. Put `0` on rest days.
5. Leave days with training but no recorded load as missing.
6. Check that every calendar day has exactly one row. Stop and fix the data if it does not.
7. Ask the user for the window: calendar weeks, with the start day, or rolling 7-day weeks. Use Monday-to-Sunday calendar weeks if they have no preference, and label that as this file's choice.
8. Ask the user which SD to use. Use the sample SD (n − 1) if they have no preference, and label that as this file's choice.
9. For each week, check that all 7 days have a daily load. If any day is missing, report the weekly load with the number of days it covers, and report monotony and strain as missing.
10. Add the 7 daily loads to get the weekly load in AU.
11. Divide the weekly load by 7 to get the mean daily load in AU.
12. Calculate the SD of the 7 daily loads, with the SD the user chose.
13. If the SD is 0, report monotony and strain as undefined, with the status `no variation`.
14. Divide the mean daily load by the SD to get monotony.
15. Multiply the weekly load by the unrounded monotony to get strain in AU.
16. Report the weekly load, monotony, and strain together, with the SD type, the window, and the load measure. Give monotony to two decimals and strain to one decimal. Put the caveat sentence directly under the table.

## Worked example

One athlete's sessions for the calendar week from Monday 2026-08-03. Monday has a practice and a lift. Sunday is a rest day.

| Date | Session | `rpe_cr10` | `duration_min` | Session load (AU) | Daily load (AU) |
|---|---|---|---|---|---|
| 2026-08-03 | Practice | 6 | 75 | 450 | 630 |
| 2026-08-03 | Lift | 4 | 45 | 180 | |
| 2026-08-04 | Practice | 7 | 90 | 630 | 630 |
| 2026-08-05 | Practice | 5 | 60 | 300 | 300 |
| 2026-08-06 | Practice | 6 | 80 | 480 | 480 |
| 2026-08-07 | Walk-through | 3 | 40 | 120 | 120 |
| 2026-08-08 | Match | 8 | 90 | 720 | 720 |
| 2026-08-09 | Rest | | | | 0 |

Work out the week step by step:

- Daily loads: 630, 630, 300, 480, 120, 720, and 0 AU.
- Weekly load: 630 + 630 + 300 + 480 + 120 + 720 + 0 = 2,880 AU.
- Mean daily load: 2,880 ÷ 7 = 411.43 AU.
- Differences from the mean: 218.57, 218.57, −111.43, 68.57, −291.43, 308.57, and −411.43 AU.
- Sum of squared differences: 462,085.71 AU².
- Sample SD: √(462,085.71 ÷ 6) = √77,014.29 = 277.51 AU.
- Population SD: √(462,085.71 ÷ 7) = √66,012.24 = 256.93 AU.
- Monotony, sample SD: 411.43 ÷ 277.51 = 1.48.
- Monotony, population SD: 411.43 ÷ 256.93 = 1.60.
- Strain, sample SD: 2,880 × 1.4825 = 4,269.7 AU.
- Strain, population SD: 2,880 × 1.6013 = 4,611.8 AU.

| Week | Weekly load (AU) | SD | Monotony | Strain (AU) |
|---|---|---|---|---|
| 2026-08-03 to 2026-08-09 | 2,880 | Sample, 277.51 AU | 1.48 | 4,269.7 |
| 2026-08-03 to 2026-08-09 | 2,880 | Population, 256.93 AU | 1.60 | 4,611.8 |

Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

The next week, from Monday 2026-08-10, has daily loads of 500, 620, 320, 560, 280, 0, and 0 AU. Its weekly load is 2,280 AU, its monotony is 1.28, and its strain is 2,927.2 AU, all with the sample SD. Rolling 7-day values across the two weeks, with the sample SD:

| Window ends | Weekly load (AU) | Monotony | Strain (AU) |
|---|---|---|---|
| 2026-08-09 (Sunday, calendar week 1) | 2,880 | 1.48 | 4,269.7 |
| 2026-08-10 | 2,750 | 1.49 | 4,084.6 |
| 2026-08-11 | 2,740 | 1.49 | 4,077.6 |
| 2026-08-12 | 2,760 | 1.51 | 4,154.0 |
| 2026-08-13 | 2,840 | 1.51 | 4,299.2 |
| 2026-08-14 | 3,000 | 1.75 | 5,238.1 |
| 2026-08-15 | 2,280 | 1.28 | 2,927.2 |
| 2026-08-16 (Sunday, calendar week 2) | 2,280 | 1.28 | 2,927.2 |

Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

The rolling window ending Friday 2026-08-14 holds the match and only one rest day, so its monotony of 1.75 is higher than either calendar week. Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness.

## What changes the number

These choices change the result even when the athlete's training does not:

- SD type. The population SD gives monotony and strain 8.0% higher than the sample SD for a 7-day week: 1.60 against 1.48 in the worked example.
- Rest days. Dropping the Sunday rest day leaves 6 values and raises monotony from 1.48 to 2.09, and strain from 4,269.7 to 6,009.3 AU.
- Missing days entered as zero. Entering a missing Wednesday as 0 lowers the weekly load to 2,580 AU and monotony to 1.16.
- Sessions counted as days. Using the 7 session loads plus the rest day as 8 values gives a monotony of 1.42 instead of 1.48.
- Calendar or rolling weeks, and the weekday a rolling window ends. In the worked example, rolling monotony runs from 1.28 to 1.75 across one week.
- Rounding before strain. 2,880 × 1.48 = 4,262.4 AU, not 4,269.7 AU. Multiply by the unrounded monotony.
- Near-identical days. Six days at 400 AU and one at 410 AU give a monotony of 106.21. A small change to one day moves the value a lot when the SD is small.
- Load measure. Monotony from session RPE load and monotony from distance are different numbers. Strain takes the unit of the load, so strain from distance is in m, not AU. Do not mix measures.
- Injured, ill, or modified-training days. These change the load for reasons monotony cannot show. Mark them in an `availability` column, and report them with the week.

## Units and typical range

Monotony has no unit. Strain has the unit of the load, AU for session RPE load. Neither has a population range that applies across sports, ages, and training phases. Compare each athlete with their own history.

| Population | Possible range | Source |
|---|---|---|
| Any athlete, 7-day week with at least one training day | Monotony from 1 ÷ √7 = 0.38 (sample SD) or 1 ÷ √6 = 0.41 (population SD) upward. The lowest value comes from one training day and six rest days. | Arithmetic of the formula |
| Any athlete, 7-day week with at least one rest day at 0 AU | Monotony up to 6 ÷ √7 = 2.27 (sample SD) or √6 = 2.45 (population SD) | Arithmetic of the formula |
| Any athlete, 7-day week with no rest day | Monotony with no fixed ceiling. Undefined when all 7 days are equal. | Arithmetic of the formula |
| Any athlete | Strain from 0 upward, in the load's unit | Arithmetic of the formula |

## Data you need

Collect this data:

- Source: a daily load log, such as session RPE load from [session-rpe-load.md](session-rpe-load.md), or another daily load in one measure.
- Sampling: one total per athlete per calendar day, with `0` on rest days and a note on ill, unavailable, or modified-training days.
- Minimum data: 7 consecutive days with no missing day for one value.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Calling monotony or strain an injury or illness risk score, or labeling values safe or dangerous. Foster (1998) explained past illnesses with thresholds identified for each athlete, and most spikes above those thresholds were not followed by illness (Jones et al., 2017). Add the caveat sentence, and do not sort athletes into risk groups.
- Using a fixed cut-off, such as a monotony of 2.0. Jones et al. (2017) describe the spikes in Foster (1998) as monotony above 2.0. We could not read Foster's full text to confirm the figure, and the abstract describes thresholds for each athlete, not one cut-off. Do not use 2.0 or any other value as a threshold. If the user has their own cut-off, label it as their choice.
- Leaving rest days out. Monotony then comes from fewer than 7 values and reads higher. Put `0` on every rest day.
- Treating a missing day as a rest day. A missing rating is unknown, not zero load. Report the week as incomplete.
- Calculating monotony from the days that have data. A spreadsheet `AVERAGE` and `STDEV.S` skip blanks without warning. Check that all 7 days are present first.
- Treating each session as a day. Add sessions into daily loads first.
- Not naming the SD. The sample and population SD give values 8.0% apart. NumPy `np.std()` gives the population SD by default, and pandas `.std()` gives the sample SD.
- Reporting a huge monotony, infinity, or `#DIV/0!` for a week of identical loads. The SD is 0, so monotony is undefined. Report the weekly load and the status `no variation`.
- Mixing calendar and rolling weeks in one report. Pick one window and name it.
- Rounding monotony before you calculate strain. Use the unrounded value.
- Confusing Polar's "Strain" with this strain. The [Polar Team Pro device file](polar-team-pro.md#metric-meanings) describes Polar Strain as the 7-day average daily cardio load. It has no SD and no monotony in it. It is closer to the acute load in [acwr.md](acwr.md). Do not compare it with Foster's strain.
- Reading monotony as week-to-week change. Monotony describes the spread of days within one week. Use the weekly loads to describe change between weeks.

## Example request

> Our sports scientist left a sheet with daily sRPE loads. Add weekly monotony and strain for each player, and highlight anyone over 2 on monotony so we know who might get sick.

The correct answer calculates monotony and strain with rest days as 0, names the SD and the window, shows the weekly load beside them, adds the caveat sentence, and declines to flag players as likely to get sick. It explains that 2.0 is not a validated cut-off and asks whether the user wants to set their own rule, labeled as their choice.

## Check the result

Run these checks:

- Recalculate one week by hand: the weekly load, the mean, the SD, monotony, and strain. Show the arithmetic and confirm it matches.
- Confirm every week has exactly 7 calendar days, with `0` on rest days, and that no week with a missing day shows a monotony or strain.
- Confirm the SD type and the window appear with every value, and that one SD type is used for the whole series.
- Confirm that no week with a rest day at 0 AU shows a monotony above 2.27 (sample SD) or 2.45 (population SD). A higher value means a rest day was dropped or not entered as 0.
- Confirm that no monotony is below 0.38 (sample SD) or 0.41 (population SD). A lower value means the window holds more than 7 days or the formula is wrong.
- Confirm that strain equals the weekly load times the unrounded monotony.
- Confirm the caveat sentence sits directly under each monotony or strain table or chart, and in the same paragraph as each value in text.

## Sources

This file cites these sources:

- Foster C. Monitoring training in athletes with reference to overtraining syndrome. Med Sci Sports Exerc. 1998;30(7):1164-1168. https://doi.org/10.1097/00005768-199807000-00023 (accessed 2026-10-07). Abstract only. The full text was not available to us.
- Foster C, Florhaug JA, Franklin J, Gottschall L, Hrovatin LA, Parker S, Doleshal P, Dodge C. A new approach to monitoring exercise training. J Strength Cond Res. 2001;15(1):109-115. https://doi.org/10.1519/00124278-200102000-00019
- Haddad M, Stylianides G, Djaoui L, Dellal A, Chamari K. Session-RPE method for training load monitoring: validity, ecological usefulness, and influencing factors. Front Neurosci. 2017;11:612. https://doi.org/10.3389/fnins.2017.00612 (accessed 2026-10-07)
- Jones CM, Griffiths PC, Mellalieu SD. Training load and fatigue marker associations with injury and illness: a systematic review of longitudinal studies. Sports Med. 2017;47(5):943-974. https://doi.org/10.1007/s40279-016-0619-5 (accessed 2026-10-07)
- Impellizzeri FM, McCall A, Ward P, Bornn L, Coutts AJ. Training load and its role in injury prevention, part 2: conceptual and methodologic pitfalls. J Athl Train. 2020;55(9):893-901. https://doi.org/10.4085/1062-6050-501-19 (cited as 2020b; accessed 2026-10-07)
- Microsoft. STDEV.S function. https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23 (accessed 2026-10-07)
- Google. STDEV function. https://support.google.com/docs/answer/3094054 (accessed 2026-10-07)
- NumPy. numpy.std. https://numpy.org/doc/stable/reference/generated/numpy.std.html (accessed 2026-10-07)
- pandas. pandas.Series.std. https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html (accessed 2026-10-07)
- R Core Team. sd: Standard Deviation. https://stat.ethz.ch/R-manual/R-devel/library/stats/html/sd.html (accessed 2026-10-07)
- Python Software Foundation. statistics: Mathematical statistics functions. https://docs.python.org/3/library/statistics.html (accessed 2026-10-07)
