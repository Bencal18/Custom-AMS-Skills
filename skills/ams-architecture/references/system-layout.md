# Lay out the system in layers

Last checked: 2026-10-05

## What it covers

This file shows how to split an AMS into raw, clean, metric, and report layers. It covers the folder layout for a spreadsheet or low-code setup, the schema layout for a database, the reference tables, the import log, and how to change a formula safely.

## Method

### Use four layers

Keep each layer in its own place. Each layer reads only from the layer before it:

| Layer | What it holds | Who or what writes to it | Rule |
|---|---|---|---|
| Raw | Each export, API response, or form download, exactly as received | The import step only | Never edit. Never overwrite. Only add. |
| Clean | The measures table in one layout, with one unit for each measure, keyed to the reference tables | A repeatable step, such as Power Query or a script, that reads the raw layer | Rebuild from raw at any time |
| Metrics | Calculated values, such as weekly load, z-scores, or limb symmetry | One defined calculation for each metric | Each metric is calculated in one place only |
| Reports | Charts, tables, and flags for staff and athletes | The report tool, reading the metric layer | Show values. Do not calculate them. |

Wilson and colleagues (2017) recommend that you save raw data as it was first generated, and record every step used to process it. Broman and Woo (2018) recommend keeping calculations out of raw data.

Test the layout with one question: if you delete the clean and metric layers, can you rebuild them from the raw layer and the reference tables alone? If not, some data or step lives only in a layer that is meant to be rebuilt. Move it.

### Keep the reference tables separate

Reference tables are the small tables that staff edit by hand. Keep them in their own place, and record each change:

- `athletes`: one row for each athlete, with `athlete_id` and the athlete's name.
- `source_ids`: maps each device's or form's athlete ID to `athlete_id`.
- `sessions`: one row for each session.
- `measure_dictionary`: one row for each measure, with its unit, definition, formula variant, and the date that variant took effect.
- `corrections`: one row for each manual fix, with the athlete, date, measure, old value, new value, reason, who, and when.

Apply manual fixes through the `corrections` table during the clean step. Never type a fix into the clean layer. A fix typed into the clean layer disappears at the next rebuild.

The `ams-data-setup` skill describes the athlete, session, measure, and source ID tables in detail.

### Lay out folders in a spreadsheet or low-code setup

Use one shared folder, owned by an organization account, with this layout:

```text
ams/
  README.md                     What the system does and how to run it
  raw/
    gps/2026-10-05_gps_session.csv
    force_plate/2026-10-05_force_plate_cmj.csv
    wellness/2026-10-05_wellness_form.csv
  reference/
    athletes.xlsx
    source_ids.xlsx
    sessions.xlsx
    measure_dictionary.xlsx
    corrections.xlsx
  clean/
    measures.xlsx               Built by Power Query from raw/ and reference/. Load to the Data Model when it nears the worksheet row limit.
  metrics/
    metrics.xlsx                Built from clean/
  reports/
    weekly_report.pbix
  logs/
    import_log.xlsx
```

Name each raw file `YYYY-MM-DD_<source>_<export>.<ext>`, with the date the data describes. Do not rename or edit a raw file after you save it.

Names appear in three places: the raw layer, because exports arrive with names, and the `athletes` and `source_ids` tables. Give `raw/`, `reference/athletes.xlsx`, and `reference/source_ids.xlsx` the tightest sharing. Keep names out of the clean and metric layers. Join names back in only in reports for staff who may see them.

Do not share the `reports/weekly_report.pbix` file itself. A Power BI file that imports data holds a copy of all of it. Publish the report to a workspace with access rules instead.

### Lay out schemas in a database

Use one schema for each layer:

```text
raw.gps_session_export        One table for each source, columns as received, plus import_id
raw.force_plate_cmj_export
raw.wellness_form_export
ref.athletes                  Names, with ref.source_ids and the raw schema
ref.source_ids
ref.sessions
ref.measure_dictionary
ref.corrections
clean.measures                Built from raw and ref by a script or view
metrics.weekly_load           One table or view for each metric group
metrics.limb_symmetry
log.imports
```

Give the `raw` schema, `ref.athletes`, and `ref.source_ids` the tightest access. Give report users read access to the `metrics` schema only. Give the import script write access to the `raw` and `log` schemas only. See [access-and-privacy.md](access-and-privacy.md).

### Keep an import log

Add one row to the import log for each import, with these columns:

- `import_id`: a unique code for the import.
- `source`: the device, form, or file.
- `file_or_request`: the raw file name, or the API request with dates.
- `imported_at`: the date and time, with the time zone.
- `rows_read`, `rows_added`, `rows_held`, and `rows_rejected`: the counts.
- `import_status`: `ok`, `failed`, `partial`, or `rejected`.
- `notes`: what went wrong, and who fixed it.

Store `import_id` on every raw row, and carry it into the clean measures table as an extra column. You can then trace every value to its import.

To undo one bad import, do not delete its raw rows. Set its `import_status` to `rejected` in the import log. The clean step skips rejected imports at the next rebuild.

Make each import safe to run twice. Before you add rows, check the import log and the source's own record ID. Running the same file twice must not double any rows.

### Change a formula safely

Follow these steps when you change how a metric is calculated:

1. Record the new formula, its variant name, and the date it takes effect in the `measure_dictionary`.
2. Build the new calculation next to the old one.
3. Compare the old and new values for a few athletes. Explain every difference.
4. Recalculate the full history with the new formula, so every value in the history uses the same formula.
5. Record the change, its date, and the reason in the system's change log.
6. Tell the staff who read the report.

Do not mix values from two formulas in one trend line.

## Common mistakes

These are the mistakes AI tools and staff make most often with system layout:

- Pasting each new export over the last one. The raw history is lost, and an error cannot be traced.
- Typing a fix into a clean or report sheet. The next refresh removes it.
- Building calculations inside the report tool and inside the workbook. The two disagree.
- Keeping athlete names in every table. Every file then needs the tightest sharing.
- Running an import twice and doubling a week of data.
- Changing a formula partway through a season without recalculating the history. The trend shows a jump that is not real.

## Example request

> My workbook has grown to 30 tabs and nobody else understands it. Help me reorganize it so it's easier to maintain and hand over.

## Check the result

Run these checks on the layout:

- Delete a copy of the clean and metric layers, rebuild them, and confirm the values match.
- Import the same raw file twice into a test copy. Confirm the row count does not change on the second import.
- Pick one metric. Confirm it is calculated in exactly one place.
- Confirm names appear only in the raw layer, the `athletes` and `source_ids` tables, and reports for staff who may see them.

## Sources

These sources support the method in this file:

- Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK. Good enough practices in scientific computing. *PLOS Computational Biology*. 2017;13(6):e1005510. doi:10.1371/journal.pcbi.1005510. Recommends saving raw data as originally generated, recording every processing step, writing scripts for each stage of processing, and naming files to reflect their content.
- Broman KW, Woo KH. Data organization in spreadsheets. *The American Statistician*. 2018;72(1):2-10. doi:10.1080/00031305.2017.1375989. Recommends no calculations in raw data files, consistent names, and `YYYY-MM-DD` dates.

The four layers, the corrections table, the import log, and the steps to change a formula are practical guidance from the authors of this repository.
