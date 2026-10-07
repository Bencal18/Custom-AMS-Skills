# Audit a monitoring workbook

Last checked: 2026-10-07

## What it covers

This file shows how to audit a coach's monitoring workbook in Excel or Google Sheets. An audit is a planned check of every formula and input for errors that give a wrong number without a warning. The file covers the errors to look for, the tools that find each one, a season rollover procedure, when to fix the workbook in place and when to rebuild it as long tables, and a worked example.

## Method

Audit a copy, not the live file. Save a copy with the date in the file name, such as `monitoring_audit_2026-10-07.xlsx`. This step is this repository's choice. It keeps the live file safe while you test fixes.

Work in this order:

1. List each sheet, what it holds, and who edits it. Unhide every hidden sheet first.
2. Show the formulas, so you can see which cells hold formulas and which hold typed values.
3. Check each error type in the next section, one at a time.
4. Fix the copy. Recalculate one athlete's result by hand to confirm each fix.
5. Replace the live file only after the user agrees.

The order is this repository's choice.

### Know the errors to look for

Look for each of these errors:

- **Broken references:** a formula shows `#REF!`. Excel shows `#REF!` when a formula refers to a cell that is not valid, most often a cell that was deleted or pasted over.
- **Ranges that stop before new rows:** a fixed range such as `A2:A200` does not grow when you add row 201. The formula ignores the new rows and gives no warning.
- **Hard-coded numbers inside formulas:** a number typed into a formula, such as `=C2/45` where 45 is one athlete's baseline. A baseline is the athlete's reference value that later results are compared with. When the baseline changes, the formula keeps the old number.
- **Values pasted over formulas:** a cell in a formula column holds a typed number. It looks like a result, but it no longer updates.
- **Mixed units in one column:** a jump height column holds some values in cm and some in inches. The average is wrong, and no error appears. See [the unit rule in the table layout reference](table-layout.md#store-the-unit-on-every-row).
- **Text that looks like a number:** a cell holds `41.2` as text. `AVERAGE` and `SUM` skip text in a range, so the value drops out of the result.
- **Dates stored as text:** a date that the app reads as text does not sort, filter, or compare as a date. Excel left-aligns a text date by default.
- **Inconsistent athlete names:** `J. Smith`, `John Smith`, and `John Smith ` with a trailing space count as three athletes. Use `athlete_id`, as [the table layout reference](table-layout.md#use-stable-athlete-ids) explains.
- **Hidden rows or sheets that formulas still read:** hiding a row or a sheet changes what you see, not what a formula reads. An old test hidden in row 14 still counts in the average.
- **Volatile functions:** a volatile function recalculates every time the workbook recalculates. A rolling window is a summary of the last set number of days, such as the last 7 days. `TODAY` and `NOW` move a rolling window each day, so a report you open next week shows different numbers.
- **Lookups that return the wrong match:** `VLOOKUP` with its last argument left out uses approximate match. Approximate match returns the closest row it finds, not only an exact match. If the first column is not sorted, the result can be a wrong row, with no error.

### Use the tools that find each error

Use these tools in Excel:

| Error | Tool in Excel |
|---|---|
| Broken references | **Home**, **Find & Select**, **Find**, with **Look in** set to **Formulas**, and search for `#REF!`. Or use **Go To Special**, **Formulas**, with only **Errors** selected. |
| Ranges that stop before new rows | Select the formula cell, then **Formulas**, **Trace Precedents**. Arrows point to the cells the formula reads. For a range on another sheet, a black arrow points to a worksheet icon. Double-click it to list the reference in the **Go To** box. Error checking also flags **Formulas which omit cells in a region**. |
| Hard-coded numbers inside formulas | **Formulas**, **Show Formulas**, or press Ctrl+`. Read each formula for typed numbers. In Excel for Windows with Microsoft 365 Apps for enterprise, **Inquire**, **Workbook Analysis** lists formulas, cells, and warnings. |
| Values pasted over formulas | Select the formula column, then **Go To Special**, **Constants**. Any cell it selects is a typed value. Select only the data cells, not the header, because a header is also a constant. Or add a helper column with `=ISFORMULA(C2)`, which returns FALSE for a typed value. A helper column is a spare column that holds a check formula for each row. Error checking also flags **Formulas inconsistent with other formulas in the region**. |
| Mixed units | Add a conditional formatting rule with **Use a formula to determine which cells to format**. Highlight values outside the range the user expects for that measure, such as `=OR(C2<20,C2>70)` for jump height in cm. Ask the user for the range. |
| Text that looks like a number | `=ISTEXT(C2)` in a helper column, or `=SUMPRODUCT(ISTEXT(C2:C500)*1)` to count text cells in the column. Error checking flags **Numbers formatted as text or preceded by an apostrophe** with a green triangle. |
| Dates stored as text | `=ISTEXT(A2)` on the date column. Error checking flags **Cells containing years represented as 2 digits**. |
| Inconsistent athlete names | `=COUNTIF(source_ids[source_name],B2)=0` flags a name that is not in the source ID table. This form needs the source ID table set up as a table named `source_ids`. With a plain range, write the range instead, such as `ids!$C$2:$C$200`. `TRIM` removes extra spaces, but not the nonbreaking space. |
| Hidden rows or sheets | Right-click any sheet tab, then **Unhide**, to list hidden sheets. The list leaves out sheets that VBA code hid as very hidden. Ask the workbook owner about those. Select all, then unhide rows and columns. **Go To Special**, **Visible cells only** shows which cells a hidden row skips. |
| Volatile functions | Find, with **Look in** set to **Formulas**, for volatile functions such as `TODAY`, `NOW`, `OFFSET`, `INDIRECT`, `RAND`, and `RANDBETWEEN`. |
| Approximate-match lookups | Find, with **Look in** set to **Formulas**, for `VLOOKUP`. Read each one. A `VLOOKUP` with only 3 arguments, or with `TRUE` or `1` last, uses approximate match. Other lookup functions, such as `MATCH`, have their own match setting. Check each one. |

In Excel for Windows, open **Go To Special** from **Home**, **Find & Select**, **Go To**, **Special**, or press Ctrl+G, then **Special**.

Use these tools in Google Sheets:

| Error | Tool in Google Sheets |
|---|---|
| Broken references, volatile functions, and approximate-match lookups | **Edit**, **Find and replace**, with **Also search within formulas** selected. Search for `#REF!`, `TODAY`, `NOW`, `RAND`, or `VLOOKUP`. |
| Ranges that stop before new rows, hard-coded numbers, and values pasted over formulas | Press Ctrl+~ to show all formulas. Add a helper column with `=ISFORMULA(C2)`. |
| Mixed units, text numbers, and text dates | **Format**, **Conditional formatting**, with **Custom formula is**, such as `=ISTEXT(C2)` or `=OR(C2<20,C2>70)`. |
| Inconsistent athlete names | `COUNTIF` against the source ID table, and `TRIM`, as in Excel. |
| Hidden sheets | **View**, then the option to show each hidden sheet. Hiding a sheet does not protect it. Every editor can unhide it, and a viewer who makes a copy can unhide it there. |

In Google Sheets, `VLOOKUP` also uses approximate match when you leave out `is_sorted`. Google recommends `FALSE` for `is_sorted`.

### Fix each error

Apply these fixes:

- **Broken references:** find what the formula read before the delete. Rewrite the range, then check the result by hand.
- **Hard-coded numbers inside formulas:** move each number into its own labeled cell or a lookup table, such as a `baselines` table with `athlete_id`, `measure_name`, `baseline`, and `set_on`. Point the formula at that cell.
- **Values pasted over formulas:** copy the formula from the cell above, and confirm `ISFORMULA` returns TRUE.
- **Mixed units:** replace the value with the value from the source export in the column's unit. If you convert, write the conversion in the measure dictionary.
- **Text that looks like a number:** in Excel, select the cells and choose **Convert to Number** from the error indicator, or use `VALUE`. In Google Sheets, use `VALUE`. Then fix the import step that made the text.
- **Dates stored as text:** use `DATEVALUE`. Check the result. In Excel, `DATEVALUE` can vary with the computer's date settings. In Google Sheets, the formats it reads can depend on region and language settings. A text date such as `03/04/2026` can become 3 April or 4 March.
- **Inconsistent athlete names:** add each spelling to the source ID table, mapped to one `athlete_id`. Do not merge two names on your own. Ask the user to confirm each uncertain match.
- **Hidden rows or sheets:** delete rows that should not count, or move them to an archive sheet that no formula reads. If a summary must skip hidden rows, `SUBTOTAL` with codes 101 to 111 ignores hidden rows in both Excel and Google Sheets. Codes 1 to 11 include them. Both sets of codes ignore rows a filter hides.
- **Approximate-match lookups:** set the last argument to `FALSE`, such as `=VLOOKUP(A2,roster,2,FALSE)`. Look up on `athlete_id`, not on a name.

### Roll the workbook over to a new season

Follow these steps at the end of each season:

1. Save the old season's workbook under a name with the season, such as `monitoring_2025-26.xlsx`.
2. Make the archive read-only. In Excel, set a password to modify the file, so other people can open it only as read-only. A read-only recommended prompt alone does not stop changes. In Google Sheets, protect each sheet with **Data**, **Protect sheets and ranges**, and name a version in **Version history** so you can return to it.
3. Copy the workbook to make the new season's template.
4. Keep every `athlete_id`. Give a new athlete a new ID. Never reuse an ID from a past athlete. See [the athletes table rules](table-layout.md#build-the-athletes-table).
5. Clear the data rows in the new template. Keep the headers, the formulas, the source ID table, and the measure dictionary.
6. Decide, with the user, which baselines to reset and which to carry over. Do not reset a baseline by default.
7. Write each reset in a `baseline_log` sheet, with `athlete_id`, `measure_name`, the old baseline, the new baseline, the reset date, and the reason.
8. Paste last season's data into a test copy of the new template.
9. Compare the test copy's results with the archive for three athletes and three dates. The numbers must match to the decimals shown, except where a baseline reset explains the difference.
10. Run the audit in this file on the test copy.
11. Start the new season only after every check passes.

The procedure is this repository's choice. Steps 8 to 11 test the template before the first real data of the new season goes in.

### Decide whether to fix in place or rebuild

Fix the workbook in place when the errors are few and the layout stays the same each season.

Rebuild the data as long tables when one of these is true. A long table holds one value per row, as [the table layout reference](table-layout.md#build-the-measures-table) explains:

- The workbook adds a column for every new measure, test date, or week.
- The same error comes back after each fix, such as a range that stops before new rows.
- Two or more people edit the same sheet.
- You need to join a second device or form to the same athletes and dates.

These triggers are this repository's choice. The table layout reference explains the long tables, and [its common mistakes list](table-layout.md#common-mistakes) covers moving from one column per measure to a long table.

### Work through an example

This example uses made-up data. A coach keeps a `log` sheet with one row per jump test, and a `summary` sheet with each athlete's mean countermovement jump (CMJ) height. The `log` sheet has these rows:

```text
row  test_date   athlete_id  cmj_height_cm
2    2026-09-07  A0001       40.0
3    2026-09-07  A0002       35.0
4    2026-09-07  A0003       45.0
5    2026-09-14  A0001       42.0
6    2026-09-14  A0002       36.4
7    2026-09-14  A0003       44.0
8    2026-09-21  A0001       41.0
9    2026-09-21  A0002       15.0
10   2026-09-21  A0003       46.0
11   2026-09-28  A0001       43.0
12   2026-09-28  A0002       37.3
13   2026-09-28  A0003       47.0
```

The `summary` sheet has these cells:

```text
A2: A0001   B2: =AVERAGEIF(log!$B$2:$B$10,A2,log!$C$2:$C$10)    shows 41.0
A3: A0002   B3: =AVERAGEIF(log!$B$2:$B$10,A3,log!$C$2:$C$10)    shows 28.8
A4: A0003   B4: 44.5                                            shows 44.5
```

The workbook has three planted errors:

- The formulas in `B2` and `B3` read rows 2 to 10. The coach built them after three weeks. The fourth week, in rows 11 to 13, is missing.
- `B4` holds a typed 44.5 that someone pasted over the formula.
- `log!C9` holds 15.0, a value in inches typed into a cm column.

Find each error with these steps:

1. Press Ctrl+` in Excel, or Ctrl+~ in Google Sheets, on the `summary` sheet. `B4` shows `44.5`, not a formula. Add `=ISFORMULA(B4)` in a spare cell. It returns FALSE.
2. Select `B2`, then **Trace Precedents** in Excel. The arrow points to a worksheet icon. Double-click it. The **Go To** box lists `log!$B$2:$B$10` and `log!$C$2:$C$10` only. In Google Sheets, read the formula in the formula bar. Add `=COUNTIF(log!$B$2:$B$10,A2)` in a spare cell. It returns 3, but the `log` sheet has 4 tests for `A0001`.
3. Add a conditional formatting rule to `log!C2:C13` with the formula `=OR(C2<20,C2>70)`. The range 20 to 70 cm is an example the coach chose for this made-up squad. `C9` is highlighted.

Fix each error with these steps:

1. Set `B2` to `=AVERAGEIF(log!$B$2:$B$13,A2,log!$C$2:$C$13)`, and fill it down to `B4`. This covers all four weeks and restores the formula in `B4`.
2. Open the jump mat export for 2026-09-21. It shows 38.1 cm for `A0002`. Type 38.1 in `log!C9`.

These are the results before and after the fixes:

| athlete_id | Before | After | Values in the mean after the fix |
|---|---|---|---|
| A0001 | 41.0 | 41.5 | 40.0, 42.0, 41.0, 43.0 |
| A0002 | 28.8 | 36.7 | 35.0, 36.4, 38.1, 37.3 |
| A0003 | 44.5 | 45.5 | 45.0, 44.0, 46.0, 47.0 |

The errors moved the means by 0.5 cm to 7.9 cm, and none showed a warning.

## Common mistakes

These are common mistakes when you audit or extend a workbook:

- Fixing the live file without a copy. A wrong fix then has no way back except version history.
- Wrapping a formula in `IFERROR(x, 0)` to hide `#REF!` or `#N/A`. The error becomes a real-looking zero. See [the missing data reference](missing-data.md).
- Trusting a result because the cell shows no error. Pasted values, fixed ranges, text numbers, and mixed units give no error.
- Leaving out the last argument of `VLOOKUP`. Write `FALSE` every time.
- Hiding rows instead of deleting or archiving them. Formulas still read hidden rows.
- Resetting every baseline at the start of a season without a record. Later comparisons then mix two baselines with no note of when one changed.
- Changing an `athlete_id` at rollover. Last season's data then no longer joins to this season's.
- Merging two athlete names because they look alike. Ask the user.

## Example request

> My jump testing spreadsheet has been running for two seasons, and some of the averages look off. Check it for errors and set it up for next season.

## Check the result

Run these checks after the audit:

- Confirm Find, with formulas included, returns no `#REF!`.
- Confirm `ISFORMULA` returns TRUE for every cell in each formula column.
- Confirm a count of text cells in each number and date column returns 0.
- Confirm each measure has one unit, and no value falls outside the range the user set.
- Add a test row in a copy. Confirm every summary that should change does change.
- Recalculate one athlete's result by hand from the raw rows. Confirm it matches the workbook.
- Confirm every `VLOOKUP` ends in `FALSE`.
- Confirm the `baseline_log` lists every reset.

## Sources

These official help pages support the function behavior and tool steps in this file. Each was read on 2026-10-07:

- Excel `#REF!` errors and their causes: https://support.microsoft.com/en-us/office/how-to-correct-a-ref-error-822c8e46-e610-4d02-bf29-ec4b8c5ff4be
- Excel error checking rules, including formulas that omit cells, inconsistent formulas, numbers formatted as text, and 2-digit years: https://support.microsoft.com/en-us/office/detect-errors-in-formulas-3a8acca5-1d61-4702-80e0-99a36a2822c1
- Excel **Go To Special**, with **Constants**, **Formulas**, and **Visible cells only**: https://support.microsoft.com/en-us/office/find-and-select-cells-that-meet-specific-conditions-in-excel-2d686424-6150-4015-a8e4-a5990f4d7e3a
- Excel **Trace Precedents** and **Trace Dependents**: https://support.microsoft.com/en-us/office/display-the-relationships-between-formulas-and-cells-a59bef2b-3701-46bf-8ff1-d3518771d507
- Excel **Show Formulas** and Ctrl+`: https://support.microsoft.com/en-us/office/display-or-hide-formulas-f7f5ab4e-bf24-4efc-8fc9-0c1b77a5356f
- Excel **Inquire** and its availability: https://support.microsoft.com/en-us/office/analyze-a-workbook-with-spreadsheet-inquire-5991e8fa-f1c1-401a-ae3f-469384ae3e3b
- Excel Find with **Look in** set to **Formulas**: https://support.microsoft.com/en-us/office/find-or-replace-text-and-numbers-on-a-worksheet-0e304ca5-ecef-4808-b90f-fdb42f892e90
- Excel `ISFORMULA`: https://support.microsoft.com/en-us/office/isformula-function-e4d1355f-7121-4ef2-801e-3839bfd6b1e5
- Excel `ISTEXT` and the other IS functions: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Excel `AVERAGE` skips text in a range: https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6
- Excel `AVERAGEIF`: https://support.microsoft.com/en-us/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642
- Excel numbers stored as text and **Convert to Number**: https://support.microsoft.com/en-us/excel/convert-numbers-stored-as-text-to-numbers-in-excel
- Excel dates stored as text are left-aligned: https://support.microsoft.com/en-us/excel/convert-dates-stored-as-text-to-dates
- Excel `DATEVALUE` and the effect of the computer's date settings: https://support.microsoft.com/en-us/excel/functions/datevalue-function
- Excel `TRIM` and the nonbreaking space: https://support.microsoft.com/en-us/excel/functions/trim-function
- Excel conditional formatting with a formula: https://support.microsoft.com/en-us/excel/use-conditional-formatting-to-highlight-information-in-excel
- Excel hidden sheets can still be referenced, and very hidden sheets do not show in **Unhide**: https://support.microsoft.com/en-us/excel/hide-or-unhide-worksheets
- Excel `SUBTOTAL` codes 1 to 11 and 101 to 111, and hidden rows: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939
- Excel `VLOOKUP` approximate match is the default and needs a sorted first column: https://support.microsoft.com/en-us/excel/functions/vlookup-function
- Excel volatile functions, including `NOW`, `TODAY`, `RAND`, `OFFSET`, and `INDIRECT`: https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation
- Excel password to modify a file for read-only access: https://support.microsoft.com/en-us/office/protection-and-security-in-excel-be0b34db-8cb6-44dd-a673-0b3e3475ac2d
- Excel read-only recommended does not prevent changes: https://support.microsoft.com/en-us/office/prompt-to-open-a-workbook-as-read-only-f41e48ed-9561-4bdd-b33e-34b8ddc0beb5
- Excel `SUM` ignores text values: https://support.microsoft.com/en-us/excel/functions/sum-function
- Google Sheets `VLOOKUP`, the default `is_sorted`, and the advice to use `FALSE`: https://support.google.com/docs/answer/3093318
- Google Sheets `ISFORMULA`: https://support.google.com/docs/answer/6270316
- Google Sheets `ISTEXT`: https://support.google.com/docs/answer/3093297
- Google Sheets `AVERAGE` ignores text: https://support.google.com/docs/answer/3093615
- Google Sheets `SUBTOTAL` and hidden rows: https://support.google.com/docs/answer/3093649
- Google Sheets `TRIM`: https://support.google.com/docs/answer/3094140
- Google Sheets `VALUE`: https://support.google.com/docs/answer/3094220
- Google Sheets `DATEVALUE` and region and language settings: https://support.google.com/docs/answer/3093039
- Google Sheets Ctrl+~ to show all formulas: https://support.google.com/docs/answer/181110
- Google Sheets **Find and replace** with **Also search within formulas**: https://support.google.com/docs/answer/62754
- Google Sheets conditional formatting with **Custom formula is**: https://support.google.com/docs/answer/78413
- Google Sheets volatile functions and recalculation settings: https://support.google.com/docs/answer/58515
- Google Sheets hidden and protected sheets: https://support.google.com/docs/answer/1218656
- Google Sheets version history and named versions: https://support.google.com/docs/answer/190843
