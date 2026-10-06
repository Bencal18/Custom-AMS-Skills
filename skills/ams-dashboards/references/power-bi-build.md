# Build the AMS screens in Power BI

Last checked: 2026-10-05

## What it covers

This file shows how to build the core AMS screens in Power BI: the model, the lookup measures, each page, row-level security for the athlete view, publishing, licensing, and refresh. It builds on the Power BI data model reference in the `ams-data-setup` skill, which covers import, types, blanks, and the date table.

The [`dashboards`](https://github.com/Bencal18/Custom-AMS-Skills/tree/main/dashboards) folder of the Custom AMS Skills repository builds a starting version of the core screens from [core-screens.md](core-screens.md) as a Power BI project. It reads the same tables as this file. It leaves out some parts of core-screens.md, such as the availability strip on the profile and the list of athletes at or below the review value.

## Method

### Know what Power BI needs

Check these points before you start:

- Power BI Desktop needs Windows 10 or later. Microsoft also supports it in Azure Virtual Desktop and Windows 365. On a Mac, use one of those, or a Windows computer your IT staff approve. You can view and edit published reports in the Power BI service in a browser.
- A Power BI project (PBIP) is a folder of text files instead of one `.pbix` file. It works with version control, so you can see every change to a measure or a page. Microsoft lists the enhanced report format (PBIR) as generally available and as the default report format.
- Sharing a report needs a paid license for each viewer, unless the workspace sits on a large enough capacity. See [Plan the licenses](#plan-the-licenses).

### Load the metric layer, not the raw data

Point Power BI at the files the metric layer writes, one table for each file. Keep the calculations in the metric layer. Power BI looks values up, filters, and draws.

1. Create a text parameter, such as `DataFolder`, that holds the folder of the metric files.
2. Load each file with **Text/CSV**.
3. In Power Query, select the columns you need.
4. Replace empty cells and `NA` with `null`.
5. Set every column type. See the Power BI reference in the `ams-data-setup` skill.
6. Load a date table from the metric layer, with one row for each day, and mark it as the date table.
7. Relate each athlete-level table to `athletes` on `athlete_id`, and to the date table on its date column. Use one-to-many relationships that filter in one direction.
8. Set **Summarization** to **Don't summarize** on every numeric column.

### Write lookup measures, not calculation measures

Each measure returns a value that the metric layer already calculated. Use three patterns:

The day shown on the squad board is the day picked in the date slicer, or the latest day when nothing is picked:

```text
As of date =
IF (
    HASONEVALUE ( dates[date] ),
    VALUES ( dates[date] ),
    CALCULATE ( MAX ( athlete_day[date] ), REMOVEFILTERS () )
)
```

A value for each athlete on that day:

```text
Wellness z =
VAR d = [As of date]
RETURN
    CALCULATE ( SELECTEDVALUE ( athlete_day[wellness_total_z] ), REMOVEFILTERS ( dates ), athlete_day[date] = d )
```

A value for one athlete on each day of a chart, and blank when more than one athlete is in view, so the chart never adds athletes together:

```text
Daily load (AU) =
IF ( HASONEVALUE ( athletes[athlete_id] ), SELECTEDVALUE ( athlete_day[srpe_load_au] ) )
```

`SELECTEDVALUE` returns blank when there is no row or more than one row. A blank shows as a gap, not as 0.

### Build each page

Use these visuals for the core screens:

| Screen | Visual | Fields |
|---|---|---|
| Squad board | Table, sorted by jump change divided by the noise band, ascending | Athlete, group, and the lookup measures for availability, form, wellness, load, and the latest jump |
| Squad board | Cards | Availability counts, forms received, jump results beyond the band next to the number expected by chance, last successful import |
| Athlete profile | Line and clustered column chart | Date; daily load as columns; acute and chronic load as lines |
| Athlete profile | Line chart | Date; jump height, noise band low, noise band high |
| Athlete profile | Matrix with a visual filter on the last 28 days | Wellness item by date; the raw answer |
| Load | Matrix | Athlete by week; a text label such as `2,150 AU, 7 of 7 days` |
| Wellness | Matrix with background color | Athlete by date; total z-score, with a diverging color scale and the number in each cell |
| Testing | Clustered bar chart and table | Athlete; change from baseline, noise band, and state wording |
| Availability | Stacked column chart and table | Date; counts of full, modified, and out |
| Data health | Table, line chart, and column chart | Import log; completion by day; device failure rows |
| My data | Line charts and a card | The athlete's own jump height with the noise band; wellness total; one plain sentence |

Follow these rules:

- Put dates on a categorical axis, or turn on **Show items with no data**, where a missing day must stay visible. See the Power BI reference in the `ams-data-setup` skill.
- Put a text box with the ACWR sentence directly under each visual that shows ACWR.
- Use a color-blind-safe palette, such as blue and orange, and keep the number in the cell. See the `athlete-data-visualization` skill.

### Show athletes only their own data

Use row-level security (RLS). A slicer or a page filter is not security, because the viewer can clear it.

1. In the `athletes` table, keep an `email` column that holds each athlete's sign-in name. Power BI compares it with `USERPRINCIPALNAME()`, which in the service returns the user principal name. That is usually, but not always, the email address.
2. Create a role, such as `Athlete`, with this filter on `athletes`: `[email] = USERPRINCIPALNAME()`. The relationships carry the filter to every fact table.
3. In the same role, block squad-level tables, such as the data quality and import log tables, with the filter `FALSE()`.
4. Create a second role, such as `Staff`, with no filter.
5. Publish the report to a workspace your organization owns.
6. In the Power BI service, add members to each role. You cannot assign members in Power BI Desktop.
7. Give athletes the **Viewer** role on the workspace, or share an app with them. RLS applies only to viewers. It does not apply to workspace Admin, Member, or Contributor roles.
8. Sign in as a test athlete. For a rule built on `USERPRINCIPALNAME()`, **Test as role** evaluates your own identity, so it cannot show what an athlete sees.

Put the athlete pages in a separate report or app audience from the staff pages, so athletes do not open a squad page and see an empty table.

### Plan the licenses

Check the current licensing rules with your IT staff and Microsoft's licensing page. As of 2026-10-05, Microsoft states these rules:

- Creating and sharing reports in any workspace other than **My workspace** needs a Pro or Premium Per User (PPU) license.
- In a Pro workspace, each person who views a report needs a Pro or PPU license. In a PPU workspace, each viewer needs a PPU license.
- On a Fabric capacity smaller than F64, each viewer needs a Pro or PPU license.
- On a Fabric capacity of F64 or larger, or a Power BI Premium (P) capacity, a person with a free license and the **Viewer** role can view reports.

Count every coach and athlete who will view a report. Do not quote prices from memory. Check Microsoft's own pricing page.

### Never publish athlete data to the web

**Publish to web** makes a report public. Microsoft states that anyone on the internet can view it with no sign-in, including the detailed data the report summarizes. Never use it for athlete data. Share inside your organization's workspace or app.

### Refresh the data

Power BI Desktop refreshes from files on your computer. In the Power BI service, files on a computer need an on-premises data gateway. Check the data source list and the refresh limits in the Power BI reference of the `ams-data-setup` skill before you rely on a schedule. Run the metric layer before each refresh, and check the last import date on the data health page after it.

## Common mistakes

These are the mistakes AI tools and staff make most often when they build AMS pages in Power BI:

- Calculating z-scores, rolling loads, or noise bands in DAX and again in the metric layer, with two answers.
- Dropping a numeric column into a visual, so Power BI adds trials, days, or athletes together.
- Using a slicer as the athlete view instead of RLS.
- Giving athletes the Member or Contributor role, so RLS does not apply to them.
- Storing an email alias that does not match `USERPRINCIPALNAME()`, so an athlete sees no data.
- Using **Publish to web** for a quick share.
- Forgetting that every viewer may need a paid license.
- Joining points across missing days on a continuous date axis.

## Example request

> I have the metric files from my AMS. Build me a Power BI squad board for this morning, an athlete profile, and a page each athlete can see with only their own jump and wellness data.

## Check the result

Run these checks before staff or athletes use the report:

- Pick one athlete and one day. Confirm every number on the squad board matches the metric layer file.
- Clear the date slicer. Confirm the squad board shows the latest day.
- Pick two athletes on the profile page. Confirm the charts go blank instead of adding the two athletes.
- Confirm no numeric column is summarized in any visual.
- Sign in as a test athlete in the Power BI service. Confirm the athlete sees only their own rows, and no squad table.
- Confirm **Publish to web** is not used for this report.

## Sources

These Microsoft pages support the steps in this file. Each was read on 2026-10-05:

- Power BI Desktop projects (PBIP): https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview
- Power BI project report folder and PBIR: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report
- Row-level security with Power BI: https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security. Roles use DAX filters such as `[UserEmail] = USERPRINCIPALNAME()`. Members are added in the service. RLS restricts only users with **Viewer** permissions. **Test as role** uses your own identity for dynamic RLS.
- Microsoft Fabric licenses and capacity: https://learn.microsoft.com/en-us/fabric/enterprise/licenses. Viewing rules for Pro, Premium Per User, capacities smaller than F64, and F64 or larger.
- Publish to web from Power BI: https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web. Anyone on the internet can view a report published to the web, with no sign-in.
- Download Power BI Desktop: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop. Minimum requirement Windows 10 or Windows Server 2016. Supported in Azure Virtual Desktop and Windows 365.

The page layouts and the lookup-measure pattern are practical guidance from the authors of this repository.
