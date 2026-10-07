# Daily, weekly, and rolling count totals

Last checked: 2026-10-07

## What it measures

Count totals add up how many times an athlete did one action, such as throws, jumps, or balls bowled, over a day, a calendar week, or a rolling window of days. Swim distance uses the same totals, in meters instead of a count.

This file holds the totals method that every count in this skill shares. The sport files hold what each count includes and misses:

- [throwing-counts.md](throwing-counts.md): pitches, throws, and arm-sensor values.
- [jump-counts.md](jump-counts.md): jump counts and jump height sums.
- [swim-and-bowling-volume.md](swim-and-bowling-volume.md): swim distance, and balls and overs bowled.

## Formula

Use these formulas for one athlete and one count type:

```text
daily total            = sum of the count across every session that calendar day
weekly total           = sum of the 7 daily totals, Monday to Sunday
rolling 7-day total    = sum of the daily totals for the 7 calendar days ending today
rolling 28-day total   = sum of the daily totals for the 28 calendar days ending today
recorded days          = number of days in the window with a daily total, including 0
```

Define every term in the formula:

- `count type`: one kind of action from one source, such as `game_pitches` from the official scorebook or `sensor_throws` from an arm sensor. Keep each count type in its own column or `measure_name`.
- `daily total`: a whole number of actions, or meters for swim distance. It is `0` on a day with no activity. It is missing on a day when activity happened but the count was not recorded, or when the sensor was not worn.
- `calendar day`: a date, not a row. A window of 7 days covers 7 dates whether or not each date has a row.
- `recorded days`: the days in the window that hold a number. A `0` counts as recorded. A missing day does not.

A weekly or rolling total is complete only when every day in the window is recorded. Report an incomplete total with the days it covers, such as "270 throws, 6 of 7 days". Never present an incomplete total as a complete one.

These choices are this skill's, not published rules. Name them when you use them:

- Weeks run Monday to Sunday, unless the user names another start day.
- The rolling windows are 7 and 28 days, unless the user names others. They match the acute and chronic windows in the `load-and-wellness` skill.

### Log zeros and missing days

Follow these rules for every count type:

- Give every athlete one row per calendar day for each count type, including rest days.
- Write `0` on a day with no activity of that type. A rest day is a real 0.
- Leave the value blank on a day when the athlete was active but nobody recorded the count. Do not write 0.
- Leave the value blank when a sensor was not worn, ran out of battery, or did not sync. A sensor total of 0 on a day the athlete threw or jumped is a missing day, not a rest day.
- Record why a day is missing in a separate column, such as `day_status`, with values such as `rest`, `not_recorded`, and `sensor_not_worn`.
- Record ill, unavailable, or modified-training days in that column too, so a low total from an absence does not read as a planned easy week.

### Calculate it in a spreadsheet

Use one sheet with one row per athlete per calendar day, sorted by athlete and then by date. Put `athlete_id` in column `A`, the date in `B`, and the daily total in `C`. Leave `C` blank on a missing day.

Use these formulas in row 8, then fill down. They work in Excel and Google Sheets:

```text
Recorded days in last 7, D8:   =COUNT(C2:C8)
Rolling 7-day total, E8:       =IF(OR(COUNTIF(A2:A8,A8)<7,B8-B2<>6,COUNT(C2:C8)<7),"",SUM(C2:C8))
Partial 7-day total, F8:       =IF(OR(COUNTIF(A2:A8,A8)<7,B8-B2<>6),"",SUM(C2:C8)&" ("&COUNT(C2:C8)&" of 7 days)")
Week start (Monday), G2:       =B2-WEEKDAY(B2,3)
```

`COUNTIF(A2:A8,A8)<7` keeps the window inside one athlete. `B8-B2<>6` returns a blank when a date row is missing, so the window always covers 7 calendar days. `WEEKDAY(B2,3)` numbers Monday as 0 in Excel and Google Sheets, so `G2` is the Monday of that week. For a 28-day window, change the ranges to 28 rows and the date test to `B29-B2<>27`.

For a weekly table, list each athlete and week start once. With `athlete_id` in `I2` and the week start in `J2`, use:

```text
Recorded days in week, K2:   =COUNTIFS($A:$A,I2,$G:$G,J2,$C:$C,">=0")
Weekly total, L2:            =IF(K2<7,"",SUMIFS($C:$C,$A:$A,I2,$G:$G,J2))
Partial weekly total, M2:    =SUMIFS($C:$C,$A:$A,I2,$G:$G,J2)&" ("&K2&" of 7 days)"
```

`">=0"` counts only cells that hold a number, so a blank day is not counted as recorded. A plain `SUM` treats a blank as 0, which is why the formulas test the count first.

To build daily totals from a session log, use `SUMIFS` on the log for the athlete, date, and count type. Check each day with `COUNTIFS` for a blank count before you trust the total. `SUMIFS` returns 0 for a day with no session rows, so set those days from `day_status`, not from the formula.

### Calculate it in Power BI and Tableau

Both versions assume one row per athlete and calendar day in a `measures` table, with the daily total as its own `measure_name`, such as `daily_throws`, with `unit` `count`. For swim distance, use a name such as `daily_swim_distance` with `unit` `m`. Build the daily totals before import, in the spreadsheet, Python, or R. Write 0 on a rest day. Leave a day with an unrecorded count missing. A day with no row, or with a row whose `status` is not `ok`, is a missing day. Use one `measure_name` per count type.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Add a calculated column `week_start` to `dates`:

```text
week_start = dates[date] - WEEKDAY ( dates[date], 3 )
```

`WEEKDAY` with return type 3 numbers Monday as 0 (https://learn.microsoft.com/en-us/dax/weekday-function-dax). Put `athletes[athlete_id]` and `dates[date]` in the visual. Use these measures:

```text
Daily count =
IF (
    CALCULATE ( COUNTROWS ( measures ), measures[measure_name] = "daily_throws" ) = 1,
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "daily_throws",
        measures[unit] = "count",
        measures[status] = "ok"
    )
)

Recorded days in last 7 =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily count] ),
        DATESINPERIOD ( dates[date], today, -7, DAY )
    )
RETURN COUNTROWS ( FILTER ( days, NOT ISBLANK ( [@x] ) ) ) + 0

Rolling 7-day total =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily count] ),
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

Partial 7-day total =
VAR today = MAX ( dates[date] )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] ),
        SUMX (
            CALCULATETABLE (
                ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily count] ),
                DATESINPERIOD ( dates[date], today, -7, DAY )
            ),
            [@x]
        )
    )
```

For 28 days, copy the two window measures and change `-7` to `-28` and `= 7` to `= 28`. `DATESINPERIOD` returns calendar dates from the date table, not rows, so a day with no row still counts as a day in the window (https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax). Show `Recorded days in last 7` next to every partial total.

For calendar weeks, put `athletes[athlete_id]` and `dates[week_start]` in the visual, and use these measures:

```text
Recorded days in week =
COUNTROWS (
    FILTER ( ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily count] ), NOT ISBLANK ( [@x] ) )
) + 0

Weekly total =
VAR days = ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily count] )
VAR recorded = FILTER ( days, NOT ISBLANK ( [@x] ) )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[week_start] )
            && COUNTROWS ( days ) = 7 && COUNTROWS ( recorded ) = 7,
        SUMX ( recorded, [@x] )
    )
```

In Tableau, make a scaffold table with one row for every athlete and every calendar date. Left join `measures` to it on `athlete_id` and on scaffold `date` equal to `measure_date`, so a day with no row still has a mark (https://help.tableau.com/current/pro/desktop/en-us/joining_tables.htm). Put the scaffold's `athlete_id` on Rows and the scaffold `date` as an exact day on Columns. Use these calculations:

```text
Daily count (aggregate):
IF COUNT(IF [measure_name] = "daily_throws" THEN 1 END) = 1
THEN MIN(IF [measure_name] = "daily_throws" AND [unit] = "count" AND [status] = "ok" THEN [value] END)
END

Recorded days in last 7 (table calculation):
WINDOW_SUM(IIF(ISNULL([Daily count]), 0, 1), -6, 0)

Rolling 7-day total (table calculation):
IF [Recorded days in last 7] = 7 THEN WINDOW_SUM(ZN([Daily count]), -6, 0) END

Partial 7-day total (table calculation):
WINDOW_SUM(ZN([Daily count]), -6, 0)

Week start (row-level):
DATETRUNC('week', [date], 'monday')
```

The third argument of `DATETRUNC` sets the first day of the week (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_date.htm).

Set **Compute Using** for every table calculation to **Specific Dimensions**, with `date` checked and `athlete_id` unchecked. Set it the same way for the count inside `Rolling 7-day total`. The window then moves along the days and restarts for each athlete (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm). For 28 days, change `-6` to `-27` and `= 7` to `= 28`.

For calendar weeks, put `athlete_id` and `Week start` on the view, and use these calculations:

```text
Daily value (row-level):
IF [measure_name] = "daily_throws" AND [unit] = "count" AND [status] = "ok" THEN [value] END

Recorded days in week (aggregate):
COUNTD(IF NOT ISNULL([Daily value]) THEN [date] END)

Weekly total (aggregate):
IF [Recorded days in week] = 7 AND COUNT([Daily value]) = 7 THEN SUM([Daily value]) END
```

`COUNT([Daily value]) = 7` blocks a week in which one day has two rows, which would add that day twice.

Blanks behave this way in each tool:

- Spreadsheet: `SUM` and `SUMIFS` treat a blank as 0, so the formulas test the number of recorded days first.
- Power BI: `SUMX` skips blank days, so `Rolling 7-day total` tests the recorded days first. A day with two rows gives a blank `Daily count`.
- Tableau: `ZN` turns a null into 0 only inside a window that the recorded-days count has already tested.

### Calculate it in Python

```python
import pandas as pd

def count_totals(daily, value="count", window=7):
    """daily: one row per athlete_id and calendar date, value NaN when missing."""
    out = []
    for athlete, d in daily.groupby("athlete_id"):
        d = d.set_index("date").sort_index()
        full = pd.date_range(d.index.min(), d.index.max(), freq="D")
        if len(full) != len(d):
            raise ValueError(f"{athlete}: a calendar day has no row. Add it as 0 or missing.")
        x = d[value]
        recorded = x.notna().astype(int).rolling(window, min_periods=1).sum()
        partial = x.fillna(0).rolling(window, min_periods=1).sum()
        rolling = partial.where(recorded == window)
        week_start = x.index - pd.to_timedelta(x.index.weekday, unit="D")
        out.append(pd.DataFrame({"athlete_id": athlete, value: x,
                                 f"recorded_{window}d": recorded,
                                 f"partial_{window}d": partial,
                                 f"rolling_{window}d": rolling,
                                 "week_start": week_start}))
    return pd.concat(out).reset_index(names="date")
```

The `partial_` column holds the sum of the recorded days, including the first days before a full window exists. Show it only with its `recorded_` column. The function stops when a calendar day has no row, because a missing rest-day row would stretch the window. For weekly totals, group by `athlete_id` and `week_start`, take `sum(min_count=7)` for the complete total, and `count()` for the recorded days.

## Calculate the totals

Follow these steps to calculate the totals from raw inputs:

1. Load one row per athlete per session with the date, the count type, and the count.
2. Keep each count type separate. Do not add a sensor total to a logged count of the same throws or jumps.
3. Add the sessions for each athlete, date, and count type to get the daily total. If any session that day has a blank count, mark the day missing.
4. Add a row with `0` for each rest day, and a blank row for each day with activity but no count.
5. Confirm that each athlete has one row per calendar day from the first to the last date.
6. Add the daily totals for each Monday-to-Sunday week. Report the recorded days with every weekly total.
7. Add the daily totals for each rolling 7-day and 28-day window. Show a rolling total only when every day in the window is recorded. Show the partial total with its recorded days otherwise.
8. Report the first complete rolling 7-day total on day 7 or later, and the first complete 28-day total on day 28 or later.

## Worked example

One athlete has 14 days of daily throw totals, starting Monday 2026-08-03. Wednesday and Sunday are rest days. The count was not recorded on Thursday 2026-08-06.

| Date | Day | Daily total | Recorded days in last 7 | Rolling 7-day total |
|---|---|---|---|---|
| 2026-08-03 | Mon | 45 | 1 | blank |
| 2026-08-04 | Tue | 60 | 2 | blank |
| 2026-08-05 | Wed | 0 | 3 | blank |
| 2026-08-06 | Thu | missing | 3 | blank |
| 2026-08-07 | Fri | 70 | 4 | blank |
| 2026-08-08 | Sat | 95 | 5 | blank |
| 2026-08-09 | Sun | 0 | 6 | blank, partial 270 (6 of 7 days) |
| 2026-08-10 | Mon | 50 | 6 | blank, partial 275 (6 of 7 days) |
| 2026-08-11 | Tue | 65 | 6 | blank, partial 280 (6 of 7 days) |
| 2026-08-12 | Wed | 0 | 6 | blank, partial 280 (6 of 7 days) |
| 2026-08-13 | Thu | 55 | 7 | 335 |
| 2026-08-14 | Fri | 80 | 7 | 345 |
| 2026-08-15 | Sat | 110 | 7 | 360 |
| 2026-08-16 | Sun | 0 | 7 | 360 |

Work through the totals:

- Week of 2026-08-03: 45 + 60 + 0 + 70 + 95 + 0 = 270 throws, 6 of 7 days. Report it as incomplete.
- Week of 2026-08-10: 50 + 65 + 0 + 55 + 80 + 110 + 0 = 360 throws, 7 of 7 days.
- Rolling 7-day total on 2026-08-13: the window runs 2026-08-07 to 2026-08-13. It holds 70 + 95 + 0 + 50 + 65 + 0 + 55 = 335 throws. It is the first complete total, because the missing Thursday has left the window.

The wrong method writes 0 on the missing Thursday. Week 1 then shows 270 throws as if it were complete, and the rolling 7-day total shows from 2026-08-09, 4 days early.

A second wrong method enters no rows for rest days or the missing day, and rolls over 7 rows instead of 7 days. On 2026-08-15, the last 7 rows run from 2026-08-07 to 2026-08-15, which is 9 calendar days, and add to 525 throws instead of 360.

## What changes the number

These choices change the result even when the athlete's work does not:

- Zero versus missing. In the worked example, writing 0 on the missing Thursday makes week 1 look complete.
- Rows versus days. Rolling over rows instead of calendar days gave 525 instead of 360 throws in the worked example.
- Week start. A Sunday-to-Saturday week groups different days from a Monday-to-Sunday week.
- Window length. A 7-day and a 28-day total answer different questions. Name the window with every total.
- Count type. A total of game pitches and a total of all logged throws for the same days can differ several-fold. See [throwing-counts.md](throwing-counts.md).
- Source. A sensor count, an observer's count, and a self-reported count of the same session differ. See the sport files.

## Units and typical range

Report throws, pitches, jumps, and balls as whole-number counts, and swim distance in meters. Name the count type, the source, and the window with every total.

Counts have no population range that applies across sports, ages, positions, and training phases. Compare each athlete with their own history, from the same source and count type. The sport files give published counts from specific studies as context, not as ranges to judge an athlete.

## Data you need

Collect this data:

- Source: a session log, an observer's tally, a scorebook, video, or a sensor export.
- Sampling: one count per athlete, session, and count type, and one `day_status` per athlete per day.
- Minimum data: 7 recorded days for the first rolling 7-day total, and 28 for the first 28-day total. A trend needs weeks of complete data from one source.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with count totals:

- Writing 0 on a day with no record. A 0 means no activity. Leave the day blank and report the recorded days.
- Leaving rest days out of the table. A rolling window over rows then covers more than 7 calendar days.
- Adding a sensor total to a logged count of the same actions. The sensor already counts them, so the sum counts them twice.
- Mixing count types in one column, such as game pitches on game days and sensor throws on practice days.
- Averaging daily totals across a week and calling it a weekly total. A mean of 7 days is a seventh of the weekly total.
- Showing an incomplete week as complete. Give the recorded days with every partial total.

## Example request

> I log every pitcher's bullpen, game, and long toss throws in a Google Sheet, one row per session. Give me daily, weekly, and rolling 7-day totals per pitcher, and show which weeks have gaps.

## Check the result

Run these checks:

- Recompute one weekly total and one rolling total by hand.
- Confirm that each athlete has one row per calendar day, and that no rolling total appears before day 7 or day 28.
- Confirm that every partial total shows its recorded days.
- Confirm that no blank day became 0.

## Sources

This file draws on these sources:

- Microsoft. WEEKDAY function (DAX). https://learn.microsoft.com/en-us/dax/weekday-function-dax (accessed 2026-10-07)
- Microsoft. DATESINPERIOD function (DAX). https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax (accessed 2026-10-07)
- Tableau. Date functions. https://help.tableau.com/current/pro/desktop/en-us/functions_functions_date.htm (accessed 2026-10-07)
- Microsoft. WEEKDAY function (Excel). https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a (accessed 2026-10-07)
- Google. WEEKDAY (Google Sheets). https://support.google.com/docs/answer/3092985 (accessed 2026-10-07)
- Tableau. Join your data. https://help.tableau.com/current/pro/desktop/en-us/joining_tables.htm (accessed 2026-10-07)
- Tableau. Table calculations. https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm (accessed 2026-10-07)
