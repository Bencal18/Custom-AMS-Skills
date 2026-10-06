# Use your own data

This guide shows you how to put your data into the template: lay out the clean tables, run the metric layer, and refresh the dashboards.

Keep athlete data inside storage your organization owns and approves. Never commit real athlete data to a public repository.

## Install Python once

The metric layer is a Python script. Install it once on the computer that runs it:

1. Install Python 3.9, 3.10, 3.11, or 3.12 from your organization's software catalog or from python.org.
2. Open a terminal in the `dashboards` folder.
3. Create an environment and install the packages. If `python3 --version` shows 3.13 or later, use `python3.12` in place of `python3`.

```bash
python3 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\pip` instead of `.venv/bin/pip`, and `.venv\Scripts\python` instead of `.venv/bin/python`.

## Lay out the clean tables

Put these five CSV files in one folder, such as `data/clean`. They follow the [table layout](../../skills/ams-data-setup/references/table-layout.md) in the `ams-data-setup` skill. Open the files in `data/sample` to see a full example of each.

| File | One row for each | Columns |
|---|---|---|
| `athletes.csv` | Athlete | `athlete_id`, `name`, `group`, `email`, `start_date`, `end_date` (`NA` while active), `status` |
| `measures.csv` | Athlete, date, session, measure, side, and trial | `athlete_id`, `measure_date`, `session_id`, `measure_name`, `side`, `trial_number`, `value`, `unit`, `status`, `source`, `source_record_id`, `imported_on` |
| `availability.csv` | Athlete and day | `athlete_id`, `date`, `availability` (`full`, `modified`, or `out`) |
| `settings.csv` | Choice the staff make | `setting`, `value`, `meaning` |
| `import_log.csv` | Import | `import_id`, `source`, `import_date`, `import_time_local`, `rows_imported`, `result` (`ok` or a reason) |

The metric layer reads these measure names from `measures.csv`:

| `measure_name` | Unit | Notes |
|---|---|---|
| `sleep_quality`, `fatigue`, `soreness`, `stress`, `mood` | `points` | 1 to 5, with 5 best on every item. One row for each answer. |
| `session_rpe_cr10` | `au` | CR-10 rating of the whole session |
| `session_duration` | `min` | Minutes the athlete took part |
| `total_distance`, `hsr_distance` | `m` | One row for each session |
| `cmj_jump_height` | `cm` | One row for each trial |

Write dates as `YYYY-MM-DD`. Use the local date of the session or form. Write `NA` for a missing value, and a reason in `status`, such as `device_failure`.

## Make your choices in settings.csv

The metric layer reads every choice from `settings.csv`. Copy the sample file and change the values:

| Setting | Sample value | What it controls |
|---|---|---|
| `acute_window_days`, `chronic_window_days` | `7`, `28` | Acute and chronic load windows. A convention, not a validated value. |
| `wellness_baseline_window_days` | `28` | Days the wellness baseline looks back |
| `wellness_min_baseline_answers` | `14` | Fewest answers before a z-score shows |
| `wellness_review_z` | `-2.0` | An example only. The total z-score at or below which staff review an athlete. No published cut point exists. Set your own. |
| `cmj_trial_summary` | `mean_of_3` | How trials become one value for each test day. `mean_of_N` takes the mean of the ok trials. A day with fewer than N ok trials gets no value. |
| `cmj_baseline_start`, `cmj_baseline_end` | Preseason dates | The fixed baseline period for jump height |
| `cmj_min_baseline_tests` | `3` | Fewest baseline test days before a change state shows |
| `cmj_direction` | `drop` | The direction of change that gets flagged: `drop` or `rise` |
| `retest_day_1`, `retest_day_2` | Two preseason days | The retest that gives the typical error. Test the same athletes twice, a short time apart, when no true change is expected. |

## Run the metric layer

Run this command from the `dashboards` folder:

```bash
.venv/bin/python pipeline/build_metrics.py --input data/clean --output data/metrics
```

It prints the number of rows it wrote to each file. Check the counts against what you expect.

## Refresh the dashboards

Refresh Power BI or Tableau. See [Open the template in Power BI](power-bi.md) and [Open the template in Tableau](tableau.md). Open the **Data health** page first.

Then pick one athlete and one day. Find each number on the squad board in `data/metrics/athlete_day.csv`, and confirm they match.

## Change a formula

Change the formula in `pipeline/build_metrics.py`, in one place only. Add or update a known-answer test in `pipeline/tests/test_metrics.py`. Install the developer packages, as [Check the template](check-the-template.md) describes. Then run the tests:

```bash
.venv/bin/python -m pytest pipeline/tests
```
