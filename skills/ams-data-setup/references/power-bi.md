# Set up the data model in Power BI

Last checked: 2026-10-02

Not tested in Power BI or Tableau. No step or DAX formula in this file was run in Power BI.

## What it covers

This file shows how to load the athlete, session, and measure tables from the table layout reference into Power BI. It covers import, missing values, the athlete and date tables, relationships, units, refresh, and the traps that give a wrong number with no warning.

## Method

Build the model in three layers:

- Power Query: import the tables, set every column type, and turn the missing code `NA` into a true blank.
- The model: an `athletes` table and a `dates` table that filter the `measures` table, with one-to-many relationships.
- Explicit DAX measures: one named measure for each result, with its unit and its blank rule. Never let a visual add up the `value` column on its own.

### Import the measures table

Follow these steps for the `measures` table:

1. Select **Get data**, then **Text/CSV**, and pick the file. Select **Transform Data**, not **Load**.
2. In Power Query, delete the automatic **Changed Type** step. Power Query guesses types from the first 200 rows, so a later `NA` or a later date format can be read wrongly.
3. Set `athlete_id`, `session_id`, `measure_name`, `side`, `unit`, `status`, `source`, and `source_record_id` to **Text**. An ID read as a number loses leading zeros.
4. Set `measure_date` and `imported_on` to **Date**, not **Date/Time**. If a file writes dates as `02/10/2026`, use **Change type**, then **Using locale**, and pick the locale of the file.
5. Set `trial_number` to **Whole Number**.
6. Select `value`, then **Replace values**, and replace `NA` with `null`. Under **Advanced options**, select **Match entire cell contents**, so only whole `NA` cells change. Do this before the type change.
7. Set `value` to **Decimal Number**.
8. Select `value`, then **Keep rows**, then **Keep errors**, to list any cell that still failed to convert. Fix those cells at the source. Then delete the audit step.
9. Leave `source_record_id` as text, with `NA` kept as text. A missing ID is not a duplicate key.
10. Select **Close & Apply**.

Do not use **Replace errors** with 0. It turns every value Power Query could not read into a real 0.

Load the `athletes` and `sessions` tables the same way. Set `start_date` and `end_date` to **Date**, and replace `NA` in `end_date` with `null` first, so an active athlete has a blank end date.

### Build the date table

Time functions such as `DATESINPERIOD` need one row for every calendar day. Build the date table in DAX with **New table**:

```text
dates =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2026, 1, 1 ), DATE ( 2026, 12, 31 ) ),
    "week_start", [Date] - WEEKDAY ( [Date], 2 ) + 1
)
```

Set the first and last dates to cover all the data, plus the longest baseline window before the first day you score. Then select the table, select **Mark as date table**, and choose the `Date` column. Power BI checks that the dates are unique, have no blanks, and run without gaps. The formulas in the skill files write `dates[date]`. DAX names are not case-sensitive, so that matches the `Date` column.

Turn off **Auto date/time** under **File**, **Options and settings**, **Options**, in the **Time intelligence** setting. It builds a hidden date table for every date column. A marked date table replaces it.

### Relate the tables

Create these relationships in **Model view**:

- `athletes[athlete_id]` to `measures[athlete_id]`: one to many, single direction.
- `dates[Date]` to `measures[measure_date]`: one to many, single direction.
- `sessions[session_id]` to `measures[session_id]`: one to many, single direction. Add a `none` row to `sessions` for values with no session.

Put `athletes[athlete_id]` and `dates[Date]` in visuals and slicers, never `measures[athlete_id]` or `measures[measure_date]`. Hide those two `measures` columns. With single-direction relationships, a filter on a `measures` column does not reach `athletes` or `dates`. Measures that read `SELECTEDVALUE ( athletes[...] )` then return blank, and date windows built on `dates` ignore the filter.

Keep the cross filter direction single. Microsoft recommends both directions only when a report needs it, because it slows the model and can make filter paths ambiguous.

Keep small lookup tables unrelated and read them with `LOOKUPVALUE` or `SELECTEDVALUE`:

- `reliability`: one row per measure with `measure_name`, `te`, `te_df`, `te_source`, and `multiplier`. `multiplier` holds 1.96 for a TE from a large reliability study, or the t multiplier for `te_df`. The noise band and the change labels read TE and the multiplier from here.
- Date pick tables, such as `old_pick` and `new_pick`, each one column of dates for a single-select slicer.

### Keep the unit with every value

Name the unit in every measure, and filter on it:

```text
CMJ height (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)
```

A row in another unit then gives a blank, not a wrong number. Add this check measure and show it in a table with `measure_name`. Every row must read 1:

```text
Units per measure = DISTINCTCOUNT ( measures[unit] )
```

### Stop implicit sums

Power BI adds up a numeric column by default when you drop it in a visual. For `value`, that adds trials, adds different measures, and adds days. Select `measures[value]`, and on the **Column tools** tab set **Summarization** to **Don't summarize**. Then hide `value` from report view, so only named measures reach a visual.

### Average at the right grain

A plain `AVERAGE ( measures[value] )` averages rows. An athlete with 3 trials counts 3 times, and an athlete with 1 trial counts once. Summarize each athlete first, then average the athletes, and report `n`:

```text
Squad mean CMJ, one value per athlete (cm) =
AVERAGEX ( VALUES ( athletes[athlete_id] ), [CMJ height (cm)] )

Athletes with a CMJ value =
COUNTROWS ( FILTER ( VALUES ( athletes[athlete_id] ), NOT ISBLANK ( [CMJ height (cm)] ) ) ) + 0
```

`AVERAGEX` skips athletes with a blank value. Show the count next to the mean, for example `mean 38.4 cm, n = 18 of 24`.

### Pivot for analysis

Some formulas need two measures on one row, such as session RPE and minutes. Build those tables in Power Query:

1. Duplicate the `measures` query and filter it to the measure names you need.
2. Replace `value` with `null` on rows whose `status` is not `ok`.
3. Remove every column except the key columns, `measure_name`, and `value`.
4. Select `measure_name`, then **Transform**, then **Pivot column**, with `value` as the value column.
5. Under **Advanced**, choose **Don't aggregate**. The default is a sum, which would add two rows for one key with no warning. With **Don't aggregate**, a duplicate shows as an error in that cell.

### Handle dates and time zones

Store `measure_date` as the local date of the session before import, as the joining reference says. Power Query converts time zones by a fixed offset with `DateTimeZone.SwitchZone`, which does not follow clock changes. `DateTimeZone.ToLocal` converts to the local time zone of the machine that runs the query, which can differ between Power BI Desktop and a scheduled refresh in the service. Convert in the AMS sheet, Python, or R, or join a table of sessions with their offset on that date.

Keep `measure_date` as a **Date** column. A **Date/Time** column keeps its time in a relationship, so 2026-10-02 21:00 does not match the date table row for 2026-10-02. A **Date/Time/Timezone** column becomes **Date/Time** in the model, with no adjustment for the reader's time zone.

### Refresh the data

Select **Refresh** in Power BI Desktop after each new import. In the Power BI service, set a scheduled refresh on the semantic model:

- Some sources need an on-premises data gateway. Check the data source list before you publish a report that reads files on a computer.
- Pro allows 8 scheduled refreshes a day. Premium, Premium Per User, and Fabric capacity allow 48.
- The service pauses a schedule after 2 months with no report views, and turns it off after 4 failures in a row.

After each refresh, check the row count and the error count from the import steps.

## Common mistakes

These are the mistakes AI tools and Power BI users make most often with athlete data:

- Dropping `value` into a visual. Power BI sums it, so trials, days, and measures add up into a number that means nothing.
- Averaging rows instead of athletes. Athletes with more trials or more sessions weigh more. Summarize each athlete first with `AVERAGEX ( VALUES ( athletes[athlete_id] ), ... )`.
- Replacing errors or blanks with 0, with **Replace errors**, `COALESCE ( x, 0 )`, or `DIVIDE ( x, y, 0 )`. A missing value then looks like a real 0. Return a blank.
- Using DAX `MAX` or `MIN` with two values on data that can be blank. Both treat a blank as 0, so `MIN ( BLANK (), 325 )` is 0.
- Writing `x - y` or `( x + y ) / 2` where one side can be blank. A blank plus a number gives the number. Test each input with `ISBLANK` first.
- Calling `STDEV.S` or `STDEVX.S` on fewer than 2 values. Both return an error, not a blank. Test the count first.
- Counting a rolling window in rows. `WINDOW`, `OFFSET`, and `TOPN` work on the rows present. With no row for a missing day, a 28-row window spans more than 28 calendar days. Use `DATESINPERIOD` on the marked date table for a window of calendar days, and use a count of rows only for a window of tests.
- Plotting a line on a continuous date axis. Power BI connects points across missing days. Use a categorical axis with **Show items with no data**, so the gap stays visible.
- Leaving **Show items with no data** off where missing athletes matter. Athletes with no row then disappear from a table instead of showing as missing.
- Relating on a **Date/Time** column, or taking the date from a UTC timestamp. Evening sessions land on the next day or on no day.
- Setting relationships to filter in both directions by default. Filters then travel in ways the report does not show.

## Example request

> I have my measures table as a CSV with athlete_id, measure_date, measure_name, value, unit, and status. Set it up in Power BI so I can see each athlete's weekly jump height and how many athletes tested.

Status: not tested.

## Check the result

Run these checks after you build the model:

- Compare the row count of `measures` in Power Query with the row count of the source file.
- Confirm the **Keep errors** audit step returned no rows before you deleted it.
- Confirm `Units per measure` is 1 for every `measure_name`.
- Confirm `measures[value]` shows **Don't summarize** and is hidden.
- Recompute one athlete's weekly mean by hand from the source file. Confirm it matches the measure, and that `n` counts athletes, not rows.
- Pick one athlete with no row on a test day. Confirm the athlete shows as missing, not as 0, and not as absent from the table.
- Pick one evening session. Confirm its `measure_date` is the local date of the session.

## Sources

These Microsoft Learn pages support the steps in this file. Each was read on 2026-10-02:

- Power Query data types, type detection from the first 200 rows, and **Using locale**: https://learn.microsoft.com/en-us/power-query/data-types
- Power Query cell-level errors when text such as `NA` is changed to a number, and **Replace errors**: https://learn.microsoft.com/en-us/power-query/dealing-with-errors
- Power Query pivot, its default sum, and the **Don't aggregate** error for duplicates: https://learn.microsoft.com/en-us/power-query/pivot-columns
- Date table requirements, **Mark as date table**, and the effect on auto date tables: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables
- **Auto date/time**: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-auto-date-time
- Relationships, cardinality, cross filter direction, and Date/Time columns in relationships: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand
- Star schema, and implicit and explicit measures: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
- Default summarization of numeric fields: https://learn.microsoft.com/en-us/power-bi/create-reports/service-aggregates
- Blank arithmetic, comparison with blank, and Date/Time/Timezone in the model: https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types
- `MAX` and `MIN` with two values treat blank as 0: https://learn.microsoft.com/en-us/dax/max-function-dax and https://learn.microsoft.com/en-us/dax/min-function-dax
- `STDEV.S` and `STDEVX.S` return an error with fewer than 2 values: https://learn.microsoft.com/en-us/dax/stdev-s-function-dax and https://learn.microsoft.com/en-us/dax/stdevx-s-function-dax
- `AVERAGE` and `AVERAGEX` skip blanks: https://learn.microsoft.com/en-us/dax/average-function-dax and https://learn.microsoft.com/en-us/dax/averagex-function-dax
- `WINDOW` works on the rows present, not on calendar days: https://learn.microsoft.com/en-us/dax/window-function-dax
- `DATESINPERIOD`: https://learn.microsoft.com/en-us/dax/datesinperiod-function-dax
- Returning blank instead of 0 from measures: https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-converting-blank
- `DateTimeZone.SwitchZone` and `DateTimeZone.ToLocal`: https://learn.microsoft.com/en-us/powerquery-m/datetimezone-switchzone and https://learn.microsoft.com/en-us/powerquery-m/datetimezone-tolocal
- Line chart gaps on categorical and continuous axes: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart
- **Show items with no data**: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-show-items-no-data
- Scheduled refresh limits and gateways: https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh
