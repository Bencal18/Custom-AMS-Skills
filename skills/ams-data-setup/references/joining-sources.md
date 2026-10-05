# Join sources by athlete and date

Last checked: 2026-10-02

## What it covers

This file shows how to combine data from several devices, forms, and files by athlete and date. It covers join keys, row counts, dates, time zones, and duplicate rows.

## Method

Follow these steps in order:

1. Ask the user for the device or form name and a sample of each export.
2. Ask for the column headings, the units, the time zone of any timestamps, and whether each row is a trial, a session, an athlete-day, or a sample.
3. Convert each source to the long format from the measures table. Use one script or sheet for each source, so you can rerun it.
4. Map each source's athlete name or ID to `athlete_id` with the source ID table.
5. List every source row that has no match, and stop.
6. Ask the user to resolve each unmatched row.
7. Convert every timestamp to a local session date. Use the time zone of the place of the session.
8. Check that the join key is unique on the side that should have one row.
9. Count rows for each key.
10. Join with a left join from the table that defines what you expect, such as the roster for a date. A left join keeps athletes who have no data, so gaps stay visible.
11. Compare the row counts before and after the join.
12. Explain every difference.

### Choose the join key

Join on `athlete_id` and the local date. Add `session_id` when both sources have it. Add `side` and `trial_number` when you join trial-level data.

Do not join on name. Do not join on date alone. If an athlete has two sessions on one day, a date-only join pairs each row with both sessions and doubles the data.

Keep missing values out of every key column. Tools treat a missing key in different ways, all without a warning.

A SQL join never matches a missing key, so the row drops out. A pandas `merge` matches a missing key to any other missing key, so unrelated rows pair up. A pandas `groupby` drops the row unless you pass `dropna=False`.

Use explicit codes, such as `bilateral` for `side` and `none` for `session_id`. See the table layout reference.

### Know what each join does to the row count

A join of one row per athlete-day onto one row per athlete-day returns the same number of rows. A join of one row per athlete-day onto many rows per athlete-day, such as several trials, returns more rows. That is correct only when you expect it.

Write down the expected relation before you run the join: one-to-one, one-to-many, or many-to-one. Make the tool test it. In pandas, use `validate="many_to_one"` and `indicator=True`.

```python
import pandas as pd
m = pd.read_csv("measures.csv", dtype={"athlete_id": str}, parse_dates=["measure_date"])
a = pd.read_csv("athletes.csv", dtype={"athlete_id": str})
j = m.merge(a, on="athlete_id", how="left", validate="many_to_one", indicator=True)
print(len(m), len(j))                 # the two counts must match
print((j["_merge"] != "both").sum())  # rows with an unknown athlete_id
```

### Handle dates

Write every date as `YYYY-MM-DD` (Broman and Woo, 2018). Store the date as a date type, not as text with a day and month in either order.

Decide what date each measure describes, and write it in the dictionary. A morning wellness form often asks about the night before, such as sleep.

Read the form's questions to decide. A GPS session belongs to the date of the session. Keep `recorded_at` if you need the time the value was entered, and use `measure_date` for joins.

### Handle time zones

A device may record in UTC, in the phone's time zone, or in the club's time zone. Ask the user which one. Convert to the time zone of the place of the session, then take the date.

A 21:00 session in `America/Chicago` on 2026-10-02 is 02:00 on 2026-10-03 in UTC. A UTC date puts the session on the wrong day.

Store and report the time zone by its name, such as `America/Chicago`, not as a fixed offset such as `-05:00`. Name it next to the joined result. A name keeps the correct offset when clocks change.

```python
import pandas as pd
s = pd.Series(["2026-10-03T02:00:00Z"])
local = pd.to_datetime(s, utc=True).dt.tz_convert("America/Chicago")
print(local.dt.date.iloc[0])  # 2026-10-02
```

For travel, use the time zone of the place of the session, not the athlete's home zone. Mark the time zone in the `sessions` table.

### Handle duplicate rows from several sources

The same session can appear in two sources, for example a GPS file and a team log. Do not keep both as separate measures. Give each measure its own `measure_name`, or its own `source`, and keep the `source` column. Then choose one source for each analysis and say which.

Keep `source_record_id`. When you import a file again, remove a new row only when its `source_record_id` is not `NA` and is in the table. Never dedupe on a missing `source_record_id`.

For a new row with no ID, compare the full key from the table layout reference. If the key is in the table, show the row to the user and ask. Until the user answers, keep the row in the table with `status` set to `held`, leave it out of summaries, and count it as held, not removed. If its value differs from the row in the table, show that athlete's summary as pending and list both values, as the table layout reference says.

```python
import pandas as pd
old = pd.read_csv("measures.csv", dtype=str)
new = pd.read_csv("new_import.csv", dtype=str)
key = ["athlete_id", "measure_date", "session_id", "measure_name", "side", "trial_number", "source"]
has_id = new["source_record_id"].notna().to_numpy()
seen = has_id & new["source_record_id"].isin(old["source_record_id"].dropna()).to_numpy()
in_old = new[key].merge(old[key].drop_duplicates(), how="left", indicator=True)["_merge"].eq("both").to_numpy()
hold = ~has_id & in_old  # no ID, and the key is already in the table: ask the user
held = new[hold].assign(status="held")  # status "held": keep in the table, out of summaries
add = new[~seen & ~hold]
table = pd.concat([old, add, held], ignore_index=True)
print(f"{len(new)} new rows: {seen.sum()} already imported, {hold.sum()} to ask about, {len(add)} to add")
```

Take a table of 7 rows, 2 of them with no ID. Take a new file that repeats those 7 rows and adds 1 new row with no ID. For this data, the snippet prints `8 new rows: 5 already imported, 2 to ask about, 1 to add`.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often when they join sources:

- Joining on the athlete's name. Spelling, order, and nicknames differ between sources. Use `athlete_id`.
- Joining on date only. A second session or a second trial on the same date multiplies rows.
- Using an inner join, which drops athletes who have no data in one source. Use a left join from the roster or the session list.
- Skipping the row count before and after the join. A join can silently double or drop rows.
- Taking the date from a UTC timestamp. Evening sessions land on the next day.
- Using a fixed UTC offset. The offset changes when clocks change.
- Letting the spreadsheet read `02/10/2026` as 10 February or 2 October. Write `YYYY-MM-DD`.
- Leaving out the fourth argument of `VLOOKUP`. Approximate match is then the default. On data sorted by the key, it returns the row with the largest key less than or equal to the lookup value, with no error when the key is missing. Set the fourth argument to `FALSE` for exact match, or use `XLOOKUP` with a not-found value of `NA`.
- Removing new rows whose `source_record_id` is `NA` because the table holds a row with `NA` there. In pandas, `isin` matches a missing value to a missing value.
- Joining a daily value, such as a wellness score, to every row of a session. This repeats the value and weights it by the number of rows when you average.

## Example request

> I export GPS data from my units every week and my athletes fill in a wellness form each morning. Join them by athlete and day so I can see load next to wellness.

## Check the result

Run these checks on the joined table:

- Count the athlete-days in each source. After a left join from the roster, confirm the athlete-day count equals the sum, over all dates, of the athletes on the roster on that date. An athlete is on the roster from `start_date` to `end_date`.
- Pick three athlete-days. Find the values in the original files and in the joined table. Confirm they match.
- List the athletes who have data in one source but not the other. Ask whether that is expected.

## Sources

These sources support the rules in this file:

- Broman KW, Woo KH. Data organization in spreadsheets. *The American Statistician*. 2018;72(1):2-10. doi:10.1080/00031305.2017.1375989. Source of the `YYYY-MM-DD` date rule and the consistency rule for identifiers and codes.
- Wickham H. Tidy data. *Journal of Statistical Software*. 2014;59(10). doi:10.18637/jss.v059.i10. Source of the one-table-for-each-observational-unit rule used for the tables that you join.
