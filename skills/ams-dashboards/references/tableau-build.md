# Build the AMS screens in Tableau

Last checked: 2026-10-05

## What it covers

This file shows how to build the core AMS screens in Tableau: the data sources, the lookup fields, each dashboard, row-level security for the athlete view, publishing, and refresh. It builds on the Tableau data model reference in the `ams-data-setup` skill, which covers import, types, nulls, and the calendar scaffold.

The [`dashboards`](https://github.com/Bencal18/Custom-AMS-Skills/tree/main/dashboards) folder of the Custom AMS Skills repository builds a starting version of the core screens from [core-screens.md](core-screens.md) as Tableau workbooks. It reads the same tables as this file. Its Tableau screens are simpler than its Power BI pages. The folder's README lists the differences.

## Method

### Know what Tableau needs

Check these points before you start:

- Tableau Desktop runs on Windows and macOS. The free Tableau Desktop Public Edition can save workbooks on your computer.
- Never publish athlete data to Tableau Public. Tableau states that workbooks and data published to a Tableau Public profile are not private and are freely accessible to anyone.
- Sharing with staff and athletes, and row-level security, need Tableau Server or Tableau Cloud under an organization account. Check the license cost on Tableau's own pricing page.

### Load the metric layer, not the raw data

Point Tableau at the files the metric layer writes. Keep the calculations in the metric layer. Tableau filters, sorts, and draws.

1. Connect to each metric file with **Text file**. Set every field type on the Data Source page. See the Tableau reference in the `ams-data-setup` skill.
2. Give each fact file the athlete's `name`, `group`, and `email` columns in the metric layer, so each data source can show and secure rows without a join.
3. Change the default aggregation of every numeric field away from **Sum**, so a view never adds trials, days, or athletes together.

### Use lookup fields, not calculation fields

Each calculated field filters or looks up a value the metric layer already calculated. Use these patterns:

```text
Latest day (boolean):
[date] = {FIXED : MAX([date])}

Athlete picked (boolean), for the staff profile with a parameter called Athlete:
[athlete_id] = [Athlete]
```

Put `Latest day` on the Filters shelf set to `True` for the squad board. For the staff profile, use a string parameter that lists athlete IDs, with each athlete's name as the display alias. A parameter works across every data source, so one control sets the athlete on every chart of the profile. Keep this parameter out of every workbook athletes can open, because its list shows every athlete's name.

For a chart with several lines, such as daily load with acute and chronic load, read a long table from the metric layer with one row for each athlete, date, series, and value. Put `series` on **Color**. This avoids dual axes and Measure Names.

### Build each dashboard

Use these sheets for the core screens:

| Screen | Sheet | Shelves |
|---|---|---|
| Squad board | Text table, filtered to the latest day, sorted by jump change divided by the noise band | Rows: athlete, group, availability, form, wellness, load, latest jump and its state |
| Athlete profile | Three line charts from the long table, with the athlete parameter | Columns: date. Use a discrete day for load and wellness, with a row for every calendar day, so a missing day stays a gap. Use a continuous day for jump height, so the line joins test days. Rows: value. Color: series |
| Load | Text table | Rows: athlete. Columns: week start. Text: a label such as `2,150 AU, 7 of 7 days` |
| Wellness | Square marks, filtered to the last 28 days | Rows: athlete. Columns: date (discrete day). Color and Text: total z-score |
| Testing | Bar chart, filtered to the latest test day | Rows: athlete, sorted by change divided by the noise band. Columns: change. Color: state wording |
| Availability | Stacked bars | Columns: date. Rows: count of athletes. Color: availability |
| Data health | Line chart and text table | Form completion by day; the import log |
| My data | Text and line charts | The athlete's latest jump sentence; jump height with the noise band; wellness total |

Follow these rules:

- Use a diverging color for z-scores, and keep the number on the mark. Tableau applies a diverging palette to a field with negative and positive values by default. Check that it reads in both directions for a color-blind viewer. See the `athlete-data-visualization` skill.
- Put a text object with the ACWR sentence directly under each sheet that shows ACWR.
- Put the condition inside the calculated field, not on the Filters shelf, when athletes with no row must stay visible. See the Tableau reference in the `ams-data-setup` skill.

### Show athletes only their own data

Use a data source filter built on user functions. A quick filter is not security, because the viewer can change it.

1. Create a calculated field: `IFNULL(ISMEMBEROF("AMS staff"), TRUE) OR LOWER([email]) = LOWER(USERNAME())`.
2. Add it as a data source filter set to `True`, on every data source that holds athlete rows.
3. Create a group called `AMS staff` on Tableau Server or Tableau Cloud, and add the staff.
4. Store each athlete's sign-in name in `email`, exactly as `USERNAME()` returns it on your site.
5. Publish the data source with the filter. Connect every athlete-facing workbook to that published data source, not to an embedded copy.
6. Deny athletes the permissions to download the workbook, save a copy, download full data, and edit on the web, on every workbook and data source they can open.
7. Sign in as a test athlete. Confirm the athlete sees only their own rows.

Tableau states that `ISMEMBEROF` returns `NULL` when nobody is signed in, and that `USERNAME` returns the local or network user name in Tableau Desktop. The `IFNULL` in step 1 shows every row when nobody is signed in, so staff can build in Desktop. Use it only together with steps 5 and 6. Row-level security takes effect only after you publish to Tableau Server or Tableau Cloud.

Put staff dashboards and athlete dashboards in separate workbooks, so athletes never open a squad dashboard or the athlete list.

### Refresh the data

Select **Data**, then **Refresh**, in Tableau Desktop after the metric layer runs. On Tableau Cloud, files on a computer refresh through Tableau Bridge. See the Tableau reference in the `ams-data-setup` skill for refresh schedules and the time zone of extracts.

## Common mistakes

These are the mistakes AI tools and staff make most often when they build AMS dashboards in Tableau:

- Publishing athlete data to Tableau Public.
- Calculating z-scores or rolling loads with table calculations and again in the metric layer, with two answers.
- Using a quick filter as the athlete view instead of a data source filter with user functions.
- Leaving `ISMEMBEROF` without `IFNULL`, so the workbook shows no rows in Desktop.
- Storing an email that does not match what `USERNAME()` returns, so an athlete sees no data.
- Leaving the default `SUM` aggregation on a numeric field.
- Building a profile from several data sources with separate quick filters, so the charts show different athletes.
- Putting the athlete parameter, with every athlete's name, in a workbook that athletes can open.

## Example request

> Build me a Tableau version of our squad readiness board and an athlete profile from the AMS metric files. Athletes should see only their own page when we publish to Tableau Cloud.

## Check the result

Run these checks before staff or athletes use the workbook:

- Pick one athlete and one day. Confirm every number on the squad board matches the metric layer file.
- Change the athlete parameter. Confirm every chart on the profile changes to the same athlete.
- Confirm no numeric field uses the `SUM` aggregation in a view.
- Sign in to Tableau Server or Tableau Cloud as a test athlete. Confirm the athlete sees only their own rows.
- Confirm the workbook is not saved to Tableau Public.

## Sources

These Tableau pages support the steps in this file. Each was read on 2026-10-05:

- User functions: https://help.tableau.com/current/pro/desktop/en-us/functions_functions_user.htm. `USERNAME()` returns the signed-in user on Tableau Server and Tableau Cloud, and the local or network user name in Desktop. `ISMEMBEROF()` returns `NULL` when nobody is signed in.
- Restrict data access with user filters and row-level security: https://help.tableau.com/current/pro/desktop/en-us/publish_userfilters.htm. Calculated fields map users to data values, and a filtered data source can serve several workbooks after you publish it.
- Save workbooks to Tableau Public: https://help.tableau.com/current/pro/desktop/en-us/publish_workbooks_tableaupublic.htm. Workbooks and data published to Tableau Public are freely accessible to anyone. Tableau Desktop Public Edition can save workbooks locally.
- Download and install Tableau Desktop: https://help.tableau.com/current/desktopdeploy/en-us/desktop_deploy_download_and_install.htm. Install steps for Windows and Mac.
- Color palettes and the diverging default: https://help.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties_color.htm

The dashboard layouts and the lookup-field pattern are practical guidance from the authors of this repository.
