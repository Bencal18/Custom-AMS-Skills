# Open the template in Tableau

This guide shows you how to open the Tableau version of the template, point it at your data, and share it safely.

## Check what you need

You need these things:

- Tableau Desktop 2026.1 or later, on Windows or macOS. The free Tableau Desktop Public Edition opens the workbooks and saves them on your computer.
- A copy of this repository.
- To share the workbooks: Tableau Server or Tableau Cloud under your organization's account.

Never save or publish these workbooks to Tableau Public once they hold athlete data. Workbooks and data on Tableau Public are open to anyone.

## Open the workbooks

The template has two workbooks:

- `tableau/CustomAMS-staff.twb`: the squad board, athlete profile, load, wellness, testing, availability, and data health dashboards. Staff only.
- `tableau/CustomAMS-athlete.twb`: the **My data** dashboard. It holds no athlete list and no squad sheet.

Follow these steps for each workbook:

1. Open the workbook in Tableau Desktop.
2. If Tableau asks where a file is, browse to the `data/metrics` folder inside the `dashboards` folder of your copy of the repository, and pick the file it names.
3. In the staff workbook, open the **Data health** dashboard first. Confirm the import log and completion figures look right.

In Tableau Desktop nobody signs in, so the athlete workbook shows every athlete, one row each. Once published with row security, each athlete sees only their own row.

If Tableau shows an error when it opens a workbook, note the message, and [open an issue](../CONTRIBUTING.md).

## Find your way around the workbooks

The staff workbook has one data source for each metric file:

| Data source | One row for each | Used by |
|---|---|---|
| `athlete_day` | Athlete and day on the roster | Squad board, wellness grid, availability |
| `test_results` | Athlete and jump test day | Testing |
| `profile_series` | Athlete, day, and chart line | Athlete profile |
| `weekly_load` | Athlete and week | Load |
| `data_quality` | Day | Wellness, data health |
| `import_log` | Import | Data health |

The athlete workbook uses `test_results` and `profile_series` only.

The athlete profile uses a parameter called **Athlete**, so one control sets every chart. It lists athlete IDs and shows each athlete's name. The list holds the sample athletes. When you use your own data, edit the parameter, select **Add values from**, and pick `athlete_id`. Then set each name as the alias. The parameter list shows every athlete's name, so keep the staff workbook away from athletes.

Calculated fields only filter or look values up. No field calculates a z-score, a rolling load, or a noise band. To change a formula, change `pipeline/build_metrics.py` and run it again.

## Show athletes only their own data

Each data source with athlete rows has a data source filter called **Row security**:

```text
IFNULL(ISMEMBEROF("AMS staff"), TRUE) OR LOWER([email]) = LOWER(USERNAME())
```

The `IFNULL` shows every row when nobody is signed in, so staff can work in Tableau Desktop. It is safe only with steps 4 and 5.

Follow these steps after you publish:

1. In the `athletes` file, put each athlete's Tableau sign-in name in the `email` column, as `USERNAME()` returns it on your site. On Tableau Cloud that is usually an email address. On Tableau Server it can be a user name. Run the metric layer again.
2. On Tableau Server or Tableau Cloud, create a group called `AMS staff`, and add every staff member who builds or reads the staff workbook. A signed-in author who is not in the group sees empty sheets.
3. Publish the `test_results` and `profile_series` data sources with the filter.
4. Connect the athlete workbook to those published data sources, not to embedded copies, and publish it to a project only athletes and staff can open.
5. Deny athletes the permissions to download the workbook, save a copy, download full data, and edit on the web.
6. Publish the staff workbook to a project athletes cannot open.
7. Sign in as a test athlete. Confirm the athlete sees only their own data.

## Refresh the data

Run the metric layer, then select **Data**, then **Refresh**. On Tableau Cloud, files on a computer refresh through Tableau Bridge.
