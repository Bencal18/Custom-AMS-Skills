# <Vendor and product> data

Checked against: <software or API version>, <YYYY-MM-DD>

This file describes the <vendor> API output and export format, what each metric means, and how to transform the data for analysis. <Vendor> is a trademark of its owner. This repository is not affiliated with or endorsed by <vendor>.

## Get the data

- Web export: <menu path, file type, and row level: one row per trial, test, session, period, or athlete>.
- API: <base URL or region, authentication method, and who can get access>.
- Date and time format: <format and time zone>.

## API output

| Endpoint | Returns | Key fields |
|---|---|---|
| `<GET /path>` | <What one response holds> | `<field>`, `<field>` |

Describe the nesting of the response, for example athlete, then test, then trial, then result. Describe paging and date filters.

## Export columns

| Column name | Meaning | Units |
|---|---|---|
| `<column>` | <meaning> | <units> |

## Metric meanings

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `<vendor metric>` | <plain-language meaning> | <calculation or default threshold> | <units> | [<metric>](<metric>.md) | <None, or the difference> |

## Transform the data

Follow these steps to turn the API output or export into the athlete, session, and measure tables from `ams-data-setup`:

1. <Step, such as joining athletes to tests by ID.>
2. <Step, such as reshaping to one row per athlete, test, trial, metric, and limb.>
3. <Step, such as converting units or time stamps.>
4. <Step, such as removing duplicate or excluded trials.>
5. <Step, such as picking the best or mean trial.>

## Common mistakes

These are the mistakes most often made with this data:

- <Mistake, and what to do instead.>

## Sources

This file draws on these sources:

- <Vendor documentation URL, accessed YYYY-MM-DD.>
