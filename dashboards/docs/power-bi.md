# Open the template in Power BI

This guide shows you how to open the Power BI version of the template, point it at your data, and share it safely.

## Check what you need

You need these things:

- Power BI Desktop on Windows 10 or later. Microsoft also supports Azure Virtual Desktop and Windows 365. Power BI Desktop does not run on macOS.
- A copy of this repository on that computer.
- To share the report: a Power BI Pro or Premium Per User license, and a workspace your organization owns. Viewers need a license too, unless the workspace sits on an F64 or larger capacity. Check with your IT staff.

## Open the project

Follow these steps:

1. Copy the repository to the computer, for example to `C:\Custom-AMS-Skills`.
2. In Power BI Desktop, select **File**, then **Open**, and open `powerbi\CustomAMS.pbip`.
3. Select **Transform data**, then **Edit parameters**.
4. Set **DataFolder** to the full path of the `dashboards\data\metrics` folder, ending with a backslash, for example `C:\Custom-AMS-Skills\dashboards\data\metrics\`.
5. Select **Apply changes**. Power BI loads the 11 tables.
6. Optional: select **View**, then **Themes**, then **Browse for themes**, and pick `powerbi\CustomAMS-theme.json`. It sets a color-blind-safe palette.
7. Open the **Data health** page first. Confirm the last import date and the completion figures look right.

If Power BI shows an error when it opens the project, note the message and the file it names, and [open an issue](../CONTRIBUTING.md).

## Find your way around the model

The model has these tables:

| Table | One row for each | Used by |
|---|---|---|
| `athletes` | Athlete | Every page, and the athlete security role |
| `dates` | Calendar day | Date slicers and axes |
| `athlete_day` | Athlete and day on the roster | Squad board, profile, wellness grid, availability, my data |
| `wellness_scores` | Athlete, day, and wellness item | Profile |
| `test_results` | Athlete and jump test day | Profile, testing, my data |
| `weekly_load` | Athlete and week | Load |
| `test_day_summary` | Test day | Squad board, testing |
| `reliability` | Tested measure | Testing |
| `data_quality` | Day | Squad board, wellness, data health |
| `import_log` | Import | Data health |
| `settings` | Setting the staff choose | Wellness |

Every measure looks up a value that the metric layer calculated. For example, `Wellness z` returns the total wellness z-score for the day on the squad board. No measure calculates a z-score, a rolling load, or a noise band. To change a formula, change `pipeline/build_metrics.py` and run it again.

## Show athletes only their own data

The model has two security roles:

- `Staff`: sees every row.
- `Athlete`: sees only the rows where `athletes[email]` matches the signed-in user, and no squad tables.

Follow these steps after you publish:

1. In the `athletes` file, put each athlete's Power BI sign-in name in the `email` column. Use the value `USERPRINCIPALNAME()` returns. It is usually, but not always, the email address.
2. Publish the report to a workspace your organization owns.
3. In the Power BI service, open the semantic model's **Security** settings. Add staff to `Staff` and athletes to `Athlete`.
4. Give athletes the **Viewer** role, or share an app with them. Row-level security does not apply to Admin, Member, or Contributor roles.
5. Share only the **My data** page with athletes, for example through a separate app audience.
6. Sign in as a test athlete. Confirm the athlete sees only their own data.

Never use **Publish to web** for this report. Anyone on the internet can view a report published to the web.

## Refresh the data

Run the metric layer, then select **Refresh** in Power BI Desktop. In the Power BI service, files on a computer need an on-premises data gateway, or the files must live in a location the service can reach. Ask your IT staff which they approve.
