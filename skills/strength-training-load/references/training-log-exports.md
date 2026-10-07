# Training log exports

Last checked: 2026-10-07

## What it covers

This file explains how to read a weight room training log export and turn it into one row per set. Every calculation in this skill starts from that layout. It is vendor-neutral. The column names below are this skill's names, not any app's names.

## Use one row per set

Reshape every log to this table before you calculate. Call it `sets`:

| Column | Meaning | Example |
|---|---|---|
| `athlete_id` | The athlete's ID, not their name | `A014` |
| `session_date` | Date of the session, as `YYYY-MM-DD` | `2026-09-14` |
| `session_id` | One ID per session, so two sessions on one day stay apart | `2026-09-14-am` |
| `exercise` | Exercise, variant, and equipment, written the same way every time | `back squat, free weight` |
| `set_number` | Order of the set within the exercise | `3` |
| `set_type` | `warmup`, `work`, or `test` | `work` |
| `side` | `bilateral`, `left`, or `right` | `bilateral` |
| `reps` | Reps completed, not reps planned | `5` |
| `load` | Load lifted, as a number | `125` |
| `load_unit` | `kg` after conversion | `kg` |
| `load_type` | `external`, `bodyweight`, `timed`, or `band_chain` | `external` |
| `duration_s` | Time in seconds, for timed sets only | `30` |
| `rpe` | RIR-based RPE, if recorded | `8` |
| `rir` | Reps in reserve, if recorded | `2` |
| `body_mass_kg` | Body mass from the same day, or the nearest weigh-in before it | `82.0` |
| `status` | `ok`, or a reason code when the row is missing or removed | `ok` |

This table and its column names are this skill's choice, not a published standard. They follow the same rule as the `ams-data-setup` skill: every row carries its own unit and status.

## Reshape other layouts

Exports come in several shapes. Follow these steps to turn each one into one row per set:

1. Find the planned columns and the completed columns. Keep the completed reps and loads. Planned values describe the program, not what the athlete lifted.
2. If the export has one row per exercise with a text field such as `4x5 @ 120`, split it into 4 rows of 5 reps at 120. Ask the user before you split a field you have not seen before.
3. If the export has one row per exercise with sets as columns, such as `set1_reps`, `set1_load`, and `set2_reps`, stack the columns into one row per set.
4. If a set says `x8 each` or `8/side`, make one row for `left` and one for `right`, each with 8 reps.
5. If a load says `BW`, set `load_type` to `bodyweight` and leave `load` blank. If it says `BW+20`, set `load_type` to `bodyweight` and `load` to 20.
6. If a load says a percentage, such as `75%`, it is a prescription. Ask for the load actually lifted. Do not compute load from the percentage unless the user asks and names the 1RM to use.
7. If an RPE field holds a value such as `@8`, strip the `@` and keep the number.
8. Keep each row's `status`. Do not drop a row without saying so.

## Convert units

Convert every load to kilograms before any sum:

```text
load_kg = load_lb × 0.45359237
```

Check each export's unit setting. Some logs store the unit once per athlete or per team, not per row. A squad with some athletes in lb and some in kg will give a sum that is wrong for every athlete in lb.

Do not round loads before you sum. Round only the final result.

## Check the export

Run these checks after you reshape the data:

- Row check: the number of sets per exercise matches the log.
- Reps check: every work set has a whole number of reps, 1 or more. A blank reps field is missing data, not 0.
- Load check: every external load is a number above 0 for barbell, dumbbell, kettlebell, and machine lifts.
- Unit check: `load_unit` is `kg` on every row.
- Name check: one exercise is not spelled two ways, such as `Back Squat` and `back squat`.
- Duplicate check: the same athlete, session, exercise, set number, and side does not appear twice.
- Implement check: dumbbell and kettlebell loads are recorded the same way on every row, one implement or both.

## Example request

> Here is a CSV from our training app. Each row is one exercise, with a column like "4x5 @ 120" and a unit setting at the top. Can you turn it into one row per set in kg so I can calculate volume load?
