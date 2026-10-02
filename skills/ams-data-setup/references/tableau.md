# Set up the data model in Tableau

Last checked: 2026-10-02

Not tested in Power BI or Tableau. No step or calculation in this file was run in Tableau.

## What it covers

This file shows how to load the athlete, session, and measure tables from the table layout reference into Tableau Desktop. It covers import, missing values, athlete and calendar tables, relationships and joins, units, refresh, and the traps that give a wrong number with no warning.

## Method

Build the data source in three parts:

- Field types: set every type on the Data Source page, so `NA` becomes a true null and dates are dates.
- The data model: relate `athletes` and `sessions` to `measures`, and use a left join from a calendar scaffold where every day must have a mark.
- Named calculations: one calculated field for each result, with its unit and its null rule. Never let a view add up the `value` field on its own.

### Import the measures table

Follow these steps for the `measures` table:

1. Select **Connect**, then **Text file**, and pick the CSV.
2. On the Data Source page, set the type of each field. Tableau guesses types from the first 1,024 rows of a CSV and the first 10,000 rows of an Excel sheet, so a later `NA` or a later date format can be read wrongly.
3. Set `athlete_id`, `session_id`, `measure_name`, `side`, `unit`, `status`, `source`, and `source_record_id` to **String**. An ID read as a number loses leading zeros.
4. Set `measure_date` and `imported_on` to **Date**, not **Date & Time**.
5. Set `trial_number` to **Number (whole)**.
6. Set `value` to **Number (decimal)**. Tableau shows text it cannot convert, such as `NA`, as null.
7. Change types before you create an extract.

Step 6 also turns any other text in `value`, such as a typo, into null with no warning. Add this check calculation and confirm its sum is 0:

```text
ok row with no number (row-level):
IIF([status] = "ok" AND ISNULL([value]), 1, 0)
```

Load the `athletes` and `sessions` tables the same way. Set `start_date` and `end_date` to **Date**. An `NA` in `end_date` becomes null, so an active athlete has a null end date.

### Relate the tables

Drag `measures` to the canvas, then drag `athletes` and `sessions` next to it. Tableau draws a relationship. Set these fields:

- `athletes`: `athlete_id` equals `athlete_id`.
- `sessions`: `session_id` equals `session_id`. Add a `none` row to `sessions` for values with no session.

A relationship keeps the tables separate and aggregates each table at its own level of detail before it combines them. Athlete fields then do not repeat once per measure row, and you do not need FIXED expressions to undo duplicates.

Use a join in the physical layer instead in these two cases. Double-click a logical table to open the join canvas:

- A row-level calculation needs a field from the other table on every row, such as an athlete's HRmax on every heart rate sample. Join `athletes` to the samples on `athlete_id`. Each sample gets one athlete row, so nothing is duplicated when `athlete_id` is unique in `athletes`.
- Every athlete or every day must stay in the view, even with no data. Use a left join with the roster or the scaffold on the left. A left join keeps every row of the left table.

### Build a calendar scaffold

Tableau has no date table. Table calculations, such as a rolling baseline, count marks, not calendar days. Make a scaffold so every athlete has a mark on every day:

1. Make a CSV with one row for every athlete and every calendar date: `athlete_id` and `date`. Start it at least one baseline window before the first day you score.
2. Add it as the left table in a left join with `measures`, on `athlete_id` and on `date` equal to `measure_date`.
3. Use the scaffold's `athlete_id` and `date` in views. A day with no row then has a mark with null values.

For a quick check, right-click a date header and select **Show Missing Values**. Tableau then adds marks for missing dates. Check that the added dates cover the whole baseline window before the first day you score.

### Keep the unit with every value

Name the unit in every calculation, and filter on it inside the calculation:

```text
CMJ height (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" THEN [value] END)
```

A row in another unit then gives null, not a wrong number. Put `measure_name` on Rows and `COUNTD([unit])` on Text. Every row must read 1.

### Stop implicit sums

Tableau aggregates a measure with `SUM` by default when you drop it in a view. For `value`, that adds trials, adds different measures, and adds days. Right-click `value`, select **Default Properties**, then **Aggregation**, and choose **Maximum** or **Average** to make the default less harmful. Then hide `value`, so only named calculations reach a view.

### Average at the right grain

A plain `AVG([value])` averages rows. An athlete with 3 trials counts 3 times. Summarize each athlete first with an INCLUDE expression, then average the athletes:

```text
Squad mean CMJ, one value per athlete (cm):
AVG({ INCLUDE [athlete_id] : MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" THEN [value] END) })

Athletes with a CMJ value:
COUNTD(IF [measure_name] = "cmj_jump_height" AND [status] = "ok" AND NOT ISNULL([value]) THEN [athlete_id] END)
```

Do not average a FIXED expression over rows. A FIXED value repeats on every row of that athlete, so `AVG` weights it by the number of rows again.

### Pivot for analysis

Tableau Desktop pivots columns to rows, not rows to columns. When a formula needs two measures on one row, such as session RPE and minutes, use one of these:

- A rows-to-columns pivot in Tableau Prep. The pivot aggregates values, so check that each key has one row first.
- An aggregate calculation with the key fields on the view, such as `MAX(IF [measure_name] = "rpe_cr10" THEN [value] END)`.

### Handle dates and time zones

Store `measure_date` as the local date of the session before import, as the joining reference says. Do the time zone conversion in the AMS sheet, Python, or R, with a zone name such as `America/Chicago`. `DATEPARSE` reads time zone symbols in a date string, but only on some connectors.

On Tableau Cloud, the site time zone for extracts is UTC by default. `TODAY()` and `NOW()` then follow UTC, so "today" can be tomorrow's date during an evening session. Use dates from the data, or set the site time zone.

### Refresh the data

Select **Data**, then **Refresh**, in Tableau Desktop after each new import. For a published data source:

- On Tableau Server, an administrator sets refresh schedules. A full refresh is the default.
- On Tableau Cloud, a CSV or Excel file on a computer refreshes through Tableau Bridge. Bridge supports extracts of those files, not live connections.
- A workbook uploaded from a browser with a flat file inside cannot refresh that file.

After each refresh, check the row count and the `ok row with no number` count.

## Common mistakes

These are the mistakes AI tools and Tableau users make most often with athlete data:

- Dropping `value` into a view. Tableau sums it, so trials, days, and measures add up into a number that means nothing.
- Averaging rows instead of athletes. Use `AVG({ INCLUDE [athlete_id] : ... })`, and report the number of athletes.
- Wrapping a value in `ZN` or `IFNULL(x, 0)` for display. A missing value then looks like a real 0. Keep it null.
- Counting a rolling window in marks when days are missing. Table calculations see only the marks in the view. With no row for a rest day or a missing day, a 28-mark window spans more than 28 calendar days. Use the scaffold.
- Filtering dates with a dimension filter in a view with a rolling window. The filter runs before table calculations and removes the earlier days from the window. Use a table calculation filter to show a shorter range.
- Leaving a table calculation on its default direction. The default can run across the wrong field. For a rolling window over time, set **Compute Using** to **Specific Dimensions**, with the date checked and `athlete_id` unchecked. For a summary across athletes, such as TE or the SWC, compute using `athlete_id`.
- Using `WINDOW_STDEV` or `WINDOW_AVG` on views with null marks without checking. Tableau Help does not state how they treat nulls. Build the mean and SD from `WINDOW_SUM` of non-null values, or check one row by hand.
- Dividing without a test. Tableau Help does not state what division by zero returns. Test the divisor first.
- Filtering `measure_name` or a date on the Filters shelf in a view built on a left join from the roster. The filter removes the athletes with no row. Put the condition inside the calculation.
- Reading a time zone into a date. Evening sessions land on the next day.

## Example request

> I have my measures table as a CSV with athlete_id, measure_date, measure_name, value, unit, and status. Set it up in Tableau so I can see each athlete's wellness z-score against the last 28 days.

Status: not tested.

## Check the result

Run these checks after you build the data source:

- Compare the row count of `measures` in Tableau with the row count of the source file.
- Confirm `ok row with no number` sums to 0.
- Confirm `COUNTD([unit])` is 1 for every `measure_name`.
- Confirm `value` has a default aggregation other than `SUM` and is hidden.
- Recompute one athlete's 28-day baseline by hand. Confirm the count of baseline days, the mean, and the SD match the table calculations.
- Pick one athlete with no row on a test day. Confirm the athlete shows as missing, not as 0, and not as absent from the view.
- Pick one evening session. Confirm its `measure_date` is the local date of the session.

## Sources

These Tableau Help pages support the steps in this file. Each was read on 2026-10-02:

- Data types, type guessing from the first rows, and text that becomes null on conversion: https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm
- Relationships, native level of detail, and the logical and physical layers: https://help.tableau.com/current/pro/desktop/en-us/datasource_datamodel.htm
- How relationships differ from joins: https://help.tableau.com/current/pro/desktop/en-us/datasource_relationships_learnmorepage.htm
- Joins and the left join: https://help.tableau.com/current/pro/desktop/en-us/joining_tables.htm
- Show Missing Values: https://help.tableau.com/current/pro/desktop/en-us/missing_values.htm
- Default aggregation and Default Properties: https://help.tableau.com/current/pro/desktop/en-us/datafields_fieldproperties.htm and https://help.tableau.com/current/pro/desktop/en-us/calculations_aggregation.htm
- LOD expressions, FIXED and INCLUDE: https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm
- Table calculations, Compute Using, and marks in the view: https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm
- Table calculation functions: https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm
- Order of operations: https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm
- Aggregate functions ignore nulls; full function list: https://help.tableau.com/current/pro/desktop/en-us/functions_all_categories.htm
- `ZN`, `IFNULL`, `ISNULL`, `IIF`: https://help.tableau.com/current/pro/desktop/en-us/functions_functions_logical.htm
- `DATEPARSE` connector support: https://help.tableau.com/current/pro/desktop/en-us/functions_functions_date.htm
- Tableau Prep pivots: https://help.tableau.com/current/prep/en-us/prep_pivot.htm
- Extract time zone on Tableau Cloud: https://help.tableau.com/current/online/en-us/tz_for_extracts.htm
- Refresh schedules on Tableau Server and Tableau Cloud: https://help.tableau.com/current/server/en-us/schedule_add.htm and https://help.tableau.com/current/online/en-us/schedule_add.htm
- Tableau Bridge and local files: https://help.tableau.com/current/online/en-us/to_sync_local_data.htm
