---
name: ams-data-setup
description: Set up a home-built athlete management system in a spreadsheet, tables, Power BI, or Tableau. Covers athlete IDs, long measure tables, joining devices by athlete and date, units, and missing data.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
  last-tested: "not tested"
---

# Set up data for an athlete management system

This skill helps you build the data structure of a home-built athlete management system (AMS) in a spreadsheet, a database, Power BI, Tableau, or code. A clean structure lets the AI calculate, trend, and chart athlete data without silent errors.

## When to use

Use this skill when the user asks to:

- Set up a spreadsheet, database, Power BI model, or Tableau data source to track athletes, sessions, and test results.
- Combine exports from several devices, forms, or files into one dataset.
- Clean messy athlete data, fix duplicate rows, or fix dates that look wrong.
- Decide how to store missing values, units, or athlete names.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| Athlete, session, and measure tables; IDs; key codes; units; duplicates | [references/table-layout.md](references/table-layout.md) |
| Joining sources by athlete and date; time zones; dates | [references/joining-sources.md](references/joining-sources.md) |
| Missing data, coverage, and zeros | [references/missing-data.md](references/missing-data.md) |
| Power BI: import, date table, relationships, units, refresh, and traps | [references/power-bi.md](references/power-bi.md) |
| Tableau: import, calendar scaffold, relationships and joins, units, refresh, and traps | [references/tableau.md](references/tableau.md) |

## Steps

Follow these steps in order:

1. Ask which devices, forms, or files the data comes from, if the user has not said.
2. For each source, ask for the file type, the column headings, the units, and one example row with names removed. Do not guess what a column means.
3. Ask where the user keeps the data: a spreadsheet app, a database, Power BI, Tableau, or code.
4. Write all formulas and code for that tool. For Power BI, load [references/power-bi.md](references/power-bi.md). For Tableau, load [references/tableau.md](references/tableau.md).
5. Load [references/table-layout.md](references/table-layout.md).
6. Design the tables before you import any data.
7. Give each athlete a stable `athlete_id`. Never use a name as a key.
8. Keep a list that maps each source's athlete ID or name to your `athlete_id`.
9. Store results in a long storage format: one row per athlete, date, session, measure, side, and trial.
10. Put the unit in a `unit` column on every row.
11. Pivot to one column for each measure before you analyze.
12. When the user combines two or more sources, load [references/joining-sources.md](references/joining-sources.md).
13. Join on `athlete_id` and the local session date.
14. Confirm the row counts before and after the join.
15. Load [references/missing-data.md](references/missing-data.md).
16. Mark a missing value as missing. Never fill it with zero.
17. Report coverage with every summary: how many athletes have a value, out of how many expected. Count athletes, not rows.
18. Show the join key, the dedupe rule, and the units next to each result.

## Core rules

Apply these rules to every table you design or edit:

- Use one table for each kind of thing: athletes, sessions, and measures. Do not mix them in one sheet.
- Keep raw imports unchanged. Do calculations in a separate sheet or table.
- Write dates as `YYYY-MM-DD`. Store times with a time zone name.
- Put one value in each cell. Do not use cell color or comments to store data.
- Use one consistent code for missing values in `value`, such as `NA`. Never use `0` or a blank for missing. This rule is specific to this skill: do not use `-` either.
- Never write `NA` in a key column. Write `side` as `left`, `right`, or `bilateral`, and write `session_id` as `none` when a value has no session.
- Never dedupe on a missing `source_record_id`. Two rows with `NA` there are not duplicates for that reason.
- Never remove a row with no `source_record_id` on your own, even when its full key and value repeat another row. Show the rows to the user and ask. Until the user answers, keep them with `status` set to `held`, leave them out of summaries, and count them as held, not removed. See [references/joining-sources.md](references/joining-sources.md).
- Keep one unit for each measure. Convert on import, and record the conversion.
- Keep names out of the data you paste into an AI tool. Use `athlete_id`.

## Checks before answering

Run these checks on your own work before you show it:

- Count the rows in each source and in the joined result. Explain every difference.
- Confirm the full key has no duplicates, and no key column has a missing value. Show the key you tested.
- Confirm every `athlete_id` in the measures table exists in the athletes table.
- Confirm each `measure_name` has exactly one `unit`.
- Confirm every date parses as a real date, falls in the expected range, and is not in the future.
- Confirm you did not turn a missing value into `0`, an empty string, or a carried-forward value.
- Report coverage for each measure and each week, as a count of athletes, not rows.
- Check that the spreadsheet app, Power BI, or Tableau did not change values on import, for example a date with the day and month swapped, a text ID read as a number, or `NA` turned into 0.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not merge two athletes into one by matching names. Ask the user to confirm each uncertain match.
- Do not delete, merge, or overwrite rows without telling the user which rows and why.
- Do not fill, estimate, or impute missing values unless the user asks. If the user asks, state the method and show results with and without the filled values.
- Do not invent a minimum coverage rule. Ask the user what share of expected data they need before they trust a summary.
- Do not guess a device export layout. Ask the user for the device name, the software version, and a sample of the export.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- Wellness forms can hold mood, stress, or free-text answers. If an answer suggests a mental-health or welfare concern, do not interpret it. Tell the user to follow their organization's referral process and involve appropriate staff.
- If any athletes are minors, remind the user to check the consent rules and the rules on parent or guardian access to the data.

## References

Load these files when needed:

- [references/table-layout.md](references/table-layout.md): the athlete, session, and measure tables, IDs, codes in key columns, units, and duplicates.
- [references/joining-sources.md](references/joining-sources.md): joining sources by athlete and date, and handling time zones.
- [references/missing-data.md](references/missing-data.md): marking, counting, and reporting missing data.
- [references/power-bi.md](references/power-bi.md): setting up the tables in Power BI, with the date table, relationships, units, refresh, and the traps that give a wrong number.
- [references/tableau.md](references/tableau.md): setting up the tables in Tableau, with the calendar scaffold, relationships and joins, units, refresh, and the traps that give a wrong number.

Device references are optional. Ask the user for the device and the export format, and use what they give you. A metric skill that covers that device may hold a device reference if it is installed. Do not rely on one being present.
