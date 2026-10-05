# Table layout for a home-built AMS

Last checked: 2026-10-02

## What it covers

This file shows how to lay out athlete data in tables so formulas, pivot tables, and code give correct results. It covers the athlete, session, and measure tables, athlete IDs, codes in key columns, units, and duplicate rows.

## Method

Give each kind of thing you observe its own table: athletes, sessions, and measures. Wickham (2014) sets this rule for tidy data: each type of observational unit forms a table.

Store the measures in a long storage format. Each row holds one value for one athlete, date, session, measure, side, and trial. The `measure_name` column names the measure, and the `value` column holds the number.

Choose this format for practical reasons: a new measure needs no new column, and every row carries its own unit, status, and source.

This long table is not tidy in Wickham's sense. In tidy data, each variable is a column. A column such as `measure_name` stores the names of variables, and Wickham (2014) calls that arrangement messy, though useful for storage.

Before you analyze, pivot the measures you need to one column for each measure, with one row for each athlete and date.

Apply these spreadsheet rules from Broman and Woo (2018) to every table:

- Be consistent.
- Write dates as `YYYY-MM-DD`.
- Put one value in each cell.
- Keep each table as one rectangle with one header row.
- Do not put calculations in the raw data.
- Do not use cell color as data.
- Keep a data dictionary.

### Build the athletes table

Use one row for each athlete. Add these columns:

- `athlete_id`: a short code such as `A0001`. It carries no meaning. Never reuse it. Never change it.
- `name`: the athlete's name. Remove this column before you paste data into an AI tool.
- `group`: team, squad, or position group. Use one spelling for each group.
- `start_date` and `end_date`: the first and last date the athlete is on the roster. Leave `end_date` as `NA` while the athlete is active.
- `status`: `active`, `inactive`, or a code you define.

### Build the source ID table

Use one row for each athlete in each source. This table maps the names and IDs that devices and forms use to your `athlete_id`. Add these columns:

- `athlete_id`: the ID from your athletes table.
- `source`: the device, form, or file, for example `gps_unit` or `wellness_form`.
- `source_athlete_id`: the ID the source uses. Store it as text.
- `source_name`: the name the source shows, spelled as the source spells it.
- `valid_from` and `valid_to`: the dates the mapping applies. Use these when a device or ID is reassigned.

### Build the sessions table

Use one row for each session: a practice, match, gym block, or test day. Add these columns:

- `session_id`: a unique code for the session.
- `session_date`: the local date at the place of the session.
- `start_time_local`: the local start time, if known.
- `time_zone`: the time zone name, for example `America/Chicago`.
- `session_type`: `practice`, `match`, `gym`, `test`, or a code you define.
- `group`: who the session is for.

### Build the measures table

Use one row for each athlete, date, session, measure, side, and trial. Add these columns:

- `athlete_id`: the ID from your athletes table.
- `measure_date`: the local date the value describes.
- `session_id`: the session the value belongs to. Write `none` when the value has no session, such as a daily form.
- `measure_name`: a lowercase name with underscores, for example `cmj_jump_height`.
- `side`: `left`, `right`, or `bilateral`. Use `bilateral` for a value taken on both sides together or with no side, such as jump height or a wellness score.
- `trial_number`: `1`, `2`, `3`, and so on. Use `1` when there is one trial.
- `value`: the number, or `NA` if missing.
- `unit`: the unit of `value`, for example `cm`, `N`, `s`, or `au`.
- `status`: `ok`, `held` while a duplicate question is open, `pain_reported` when the athlete or tester noted pain during that trial, or a reason code when the value is missing or removed. Keep a `pain_reported` row, and leave it out of best-trial values, means, baselines, z-scores, change, and left-right comparisons. Pass the pain report to the medical team.
- `source`: the device, form, or file.
- `source_record_id`: the source's own row or test ID. Write `NA` when the source gives none.
- `imported_on`: the date you imported the row.

Example rows:

```text
athlete_id,measure_date,session_id,measure_name,side,trial_number,value,unit,status,source,source_record_id,imported_on
A0001,2026-10-02,S0101,cmj_jump_height,bilateral,1,41.2,cm,ok,force_plate,T-88231,2026-10-03
A0001,2026-10-02,S0101,cmj_jump_height,bilateral,2,42.0,cm,ok,force_plate,T-88232,2026-10-03
A0002,2026-10-02,S0101,cmj_jump_height,bilateral,1,NA,cm,device_failure,force_plate,NA,2026-10-03
A0003,2026-10-02,S0101,nordic_peak_force,left,2,298,N,pain_reported,nordic_device,NA,2026-10-03
A0001,2026-10-02,none,wellness_score,bilateral,1,4,au,ok,wellness_form,NA,2026-10-03
```

### Keep missing values out of key columns

A key column is one you group, join, or dedupe on: `athlete_id`, `measure_date`, `session_id`, `measure_name`, `side`, `trial_number`, and `source`. Never write `NA` in a key column. Use an explicit code, such as `bilateral` for `side` and `none` for `session_id`.

Tools read `NA` as missing. In pandas, `groupby` drops every row whose key is missing, unless you pass `dropna=False`. With `side` set to `NA`, a group mean of jump height by athlete, measure, and side returns no rows at all.

pandas also reads `None`, `NULL`, and a blank cell as missing, so write `none` in lowercase.

Use `NA` only in columns that hold a value, such as `value`, `end_date`, or `source_record_id`.

### Keep a measure dictionary

Use one row for each `measure_name`. Add these columns: `measure_name`, `unit`, `definition`, `formula_variant`, `source`, `measure_date_rule`, and `status_codes`. The AI reads this table to learn what each measure means. Do not let the AI guess.

### Use stable athlete IDs

Never use names as keys. Names change, are spelled in several ways, and can match two athletes. A name key also breaks the join without a warning.

Keep the file that links names to IDs in a separate, protected place. Share only `athlete_id` with other people and with AI tools.

### Store the unit on every row

Use one unit for each `measure_name`. Convert before you import, and write the conversion in the dictionary. A mixed column, such as jump height in both `cm` and `in`, gives a wrong average with no error message.

### Handle duplicate rows

Define the key that makes a row unique before you import. For the measures table, use `athlete_id`, `measure_date`, `session_id`, `measure_name`, `side`, `trial_number`, and `source`.

The `session_id` keeps a test before and after practice on the same day apart. The `source` keeps two sources with the same `measure_name` apart.

Treat these cases differently:

- The same `source_record_id` appears twice, and it is not `NA`: the file was imported twice. Keep one row.
- Two rows both have `NA` in `source_record_id`: this alone does not make them duplicates. Compare the full key.
- The same key appears with two different values: the data conflicts. Do not pick one. Ask the user which is correct. Until the user answers, keep both rows with `status` set to `held`, show that athlete's summary as pending, and list each candidate value.
- Two trials of one test have the same value: these are two real trials. Keep both.

Never remove a row because its `source_record_id` matches a missing value. Do not remove duplicates by matching values. Two athletes can have the same value, and one athlete can repeat a value.

### Keep every trial and summarize in a separate table

Store every trial in the measures table. Make the summary, such as the best or mean trial, in a separate table. Name the rule in the summary, for example `best_of_3`. Do not drop trials on import.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often when they structure athlete data:

- Joining or looking up on the athlete's name. Use `athlete_id`.
- Putting each measure in its own column in the raw table, then adding a column for every new measure. Store the long format, and pivot for analysis.
- Analyzing the long table as it is when the question needs one column for each measure, such as a correlation between two measures. Pivot first.
- Writing `NA` in a key column such as `side` or `session_id`. A `groupby` then drops those rows, and a dedupe on `NA` IDs can remove real rows.
- Putting a unit in the column heading only, for example `jump_cm`, then merging a source in inches. Use a `unit` column and one unit for each `measure_name`.
- Letting the spreadsheet app change values on import. Zeeberg and colleagues (2004) found that default date and number conversions in Excel changed gene names irreversibly. Format ID and date columns as text before you import, or declare column types in code.
- Reading `03/04/2026` as 4 March in one file and 3 April in another. Write `YYYY-MM-DD`.
- Using a text ID such as `00123` as a number. The app drops the leading zeros, and the ID no longer matches. Store IDs as text.
- Calculating inside the raw data sheet. Do calculations in a separate sheet so the raw data stays unchanged.
- Dropping duplicates by value, or by date and name only. Use the full key.
- Averaging all trials when the test calls for the best trial, or the reverse. Name the rule.
- Showing the athlete's name in the data you send to an AI tool. Replace it with `athlete_id`.

## Example request

> I have wellness form exports, GPS files, and jump tests in separate spreadsheets. Set up one workbook where I can see all of it by athlete and date.

## Check the result

Run these checks on the finished tables:

- Pick one athlete and one date. Find that athlete's values in each source file, then in the measures table. Confirm they match, including the unit.
- Count the rows in each source file. Add them. Confirm the total matches the measures table, or list each row that you removed and why.
- Count the missing values in each key column. Confirm the count is zero.
- Run a duplicate count on the full key. Confirm it returns zero conflicts.

## Sources

These sources support the rules in this file:

- Wickham H. Tidy data. *Journal of Statistical Software*. 2014;59(10). doi:10.18637/jss.v059.i10. Defines tidy data: each variable is a column, each observation is a row, and each type of observational unit is a table. Calls a molten table, where one column stores the names of variables, messy, though useful for storage.
- Broman KW, Woo KH. Data organization in spreadsheets. *The American Statistician*. 2018;72(1):2-10. doi:10.1080/00031305.2017.1375989. Source of the spreadsheet rules: consistency, `YYYY-MM-DD` dates, one value in each cell, one rectangle, a data dictionary, and no calculations in raw data.
- Zeeberg BR, Riss J, Kane DW, et al. Mistaken identifiers: gene name errors can be introduced inadvertently when using Excel in bioinformatics. *BMC Bioinformatics*. 2004;5:80. doi:10.1186/1471-2105-5-80. Shows that default date and number conversions in Excel changed identifiers irreversibly.
