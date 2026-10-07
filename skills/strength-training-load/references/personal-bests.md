# Personal bests

Last checked: 2026-10-07

## What it measures

A personal best is the heaviest load an athlete has lifted, or the highest 1RM estimated for them, in one exercise up to a given date. Relative strength divides that load by the athlete's body mass, so athletes of different size can be shown on one scale.

## Formula

Track three kinds of best in separate columns. Never merge them:

```text
best tested 1RM (kg)       = highest load of a successful single in a test set, up to the date
best rep max, n reps (kg)  = highest load lifted for exactly n reps to failure, up to the date
best estimated 1RM (kg)    = highest estimated 1RM, one formula, up to the date
```

Use these formulas for relative strength:

```text
relative strength (kg/kg)                  = load (kg) ÷ body mass (kg)
allometric relative strength (kg/kg^0.67)  = load (kg) ÷ body mass (kg)^0.67
```

Define every term in the formula:

- `successful single`: one rep at a load, completed with the technique the coach accepts, in a set labeled `test`.
- `rep max`: the heaviest load lifted for a given number of reps to failure, such as a 3RM or 5RM. Compare only rep maxes with the same rep count.
- `estimated 1RM`: from `estimated-1rm.md`, with one formula, one rep limit, and the same RIR rule for every session.
- `up to the date`: the best of every value on or before that date. This is called a running maximum.
- `body mass`: in kg, from the same day as the lift, or the nearest weigh-in before it. That rule is this skill's choice. Show the date of the weigh-in next to the result.
- `allometric relative strength`: load divided by body mass raised to a power. Jaric (2002) recommended a power of 0.67 for muscle force measured with a dynamometer. Using it for a lifted load is this skill's choice. Always state the power.

Jaric (2002) reported that most studies presented strength data without normalizing for body size, with methods that were not appropriate, or with several methods on the same data. Name the method in every result.

The `force-plate` skill also reports relative strength, as isometric mid-thigh pull peak force per kilogram of body mass, in N/kg. That is a force from a force plate, not a lifted load. Do not compare N/kg with kg/kg.

### Keep tested and estimated values apart

Follow these rules:

- A tested 1RM changes only when the athlete lifts a heavier single in a test set.
- A higher estimate does not change the tested best.
- Estimates from different formulas go in different columns.
- Estimates from bar speed, from the `velocity-based-training` skill, go in their own column.
- Show the date of each best and the session it came from.

### Calculate it in a spreadsheet

Put one set per row. These column letters are for this file only, so remap them to the user's sheet. Put athlete ID in `A`, date in `B`, exercise in `D`, set type in `F`, load in kg in `I`, reps in `H`, and the chosen estimated 1RM in `G`. Body mass in kg goes in `M`. Use these formulas in row 2:

```text
Best tested 1RM to date (kg), N2:
=IFERROR(1/(1/MAXIFS(I:I,A:A,A2,D:D,D2,F:F,"test",H:H,1,B:B,"<="&B2)),"")

Best estimated 1RM to date (kg), O2:
=IFERROR(1/(1/MAXIFS(G:G,A:A,A2,D:D,D2,B:B,"<="&B2)),"")

Relative strength, tested (kg/kg), P2:
=IF(AND(F2="test",H2=1,ISNUMBER(I2),ISNUMBER(M2),M2>0),I2/M2,"")
```

`MAXIFS` returns 0 when nothing matches. The `1/(1/…)` wrapper turns that 0 into an error, and `IFERROR` turns it into a blank. Add `,status_range,"ok"` to each `MAXIFS` if the sheet has a status column.

### Calculate it in Power BI and Tableau

Both versions assume the `sets` table in `training-log-exports.md`, the `e1RM Epley (kg)` column from `estimated-1rm.md`, and a date table related to `sets[session_date]`.

In Power BI, use these DAX measures. Put `athlete_id`, `exercise`, and the date in the visual:

```text
Best tested 1RM to date (kg) =
VAR d = MAX ( 'Date'[Date] )
RETURN
    CALCULATE (
        MAX ( sets[load] ),
        sets[set_type] = "test",
        sets[reps] = 1,
        sets[status] = "ok",
        sets[load_unit] = "kg",
        'Date'[Date] <= d,
        REMOVEFILTERS ( 'Date' )
    )

Best e1RM Epley to date (kg) =
VAR d = MAX ( 'Date'[Date] )
RETURN
    CALCULATE ( MAX ( sets[e1RM Epley (kg)] ), 'Date'[Date] <= d, REMOVEFILTERS ( 'Date' ) )

Relative strength, tested (kg/kg) =
VAR best = [Best tested 1RM to date (kg)]
VAR d = MAX ( 'Date'[Date] )
VAR bmDate =
    CALCULATE ( MAX ( sets[session_date] ), NOT ISBLANK ( sets[body_mass_kg] ),
        'Date'[Date] <= d, REMOVEFILTERS ( 'Date' ), REMOVEFILTERS ( sets[exercise] ) )
VAR bm =
    CALCULATE ( MAX ( sets[body_mass_kg] ), sets[session_date] = bmDate,
        REMOVEFILTERS ( 'Date' ), REMOVEFILTERS ( sets[exercise] ) )
RETURN IF ( NOT ISBLANK ( best ) && bm > 0, DIVIDE ( best, bm ) )
```

The relative strength measure divides the best tested 1RM to date by the latest body mass on or before the date. To divide by body mass on the day of the best lift instead, compute relative strength per row and take its maximum. Say which you used.

In Tableau, put `athlete_id`, `exercise`, and `session_date` on the view, sorted by date. Use these calculations, and set each table calculation to compute along `session_date`:

```text
Tested 1RM (kg):
MAX(IF [set_type] = "test" AND [reps] = 1 AND [status] = "ok" AND [load_unit] = "kg"
    THEN [load] END)

Best tested 1RM to date (kg):
RUNNING_MAX([Tested 1RM (kg)])

Best e1RM Epley to date (kg):
RUNNING_MAX(MAX([e1RM Epley (kg)]))

Relative strength, tested (kg/kg):
IF MAX([body_mass_kg]) > 0 THEN [Best tested 1RM to date (kg)] / MAX([body_mass_kg]) END
```

Blanks behave this way in each tool:

- Power BI: a date with no test before it gives a blank best. A blank body mass gives a blank relative strength.
- Tableau: `RUNNING_MAX` skips nulls, so a session with no test carries the earlier best forward. Relative strength uses the body mass of the session on that row. A session with no body mass gives a null relative strength.

### Calculate it in Python or R

Use this Python code. It uses the standard library only. Each row is a dict with `date`, `set_type`, `reps`, `load`, and `e1rm`, for one athlete and exercise:

```python
def running_bests(rows):
    best_tested = best_est = None
    out = []
    for r in sorted(rows, key=lambda r: r["date"]):
        if r.get("status", "ok") != "ok":
            continue
        if r["set_type"] == "test" and r["reps"] == 1 and r["load"] is not None:
            best_tested = r["load"] if best_tested is None else max(best_tested, r["load"])
        if r.get("e1rm") is not None:
            best_est = r["e1rm"] if best_est is None else max(best_est, r["e1rm"])
        out.append({**r, "best_tested_kg": best_tested, "best_e1rm_kg": best_est})
    return out
```

Use this R code with dplyr. It assumes an `e1rm_epley_kg` column from `estimated-1rm.md`:

```r
library(dplyr)
bests <- sets |>
  filter(status == "ok") |>
  arrange(athlete_id, exercise, session_date) |>
  group_by(athlete_id, exercise) |>
  mutate(
    tested = if_else(set_type == "test" & reps == 1, load, NA_real_),
    best_tested_kg = cummax(coalesce(tested, -Inf)),
    best_e1rm_kg = cummax(coalesce(e1rm_epley_kg, -Inf)),
    best_tested_kg = na_if(best_tested_kg, -Inf),
    best_e1rm_kg = na_if(best_e1rm_kg, -Inf)
  ) |>
  ungroup()
```

## Calculate the metric

Follow these steps to track personal bests:

1. Reshape the log to one row per set, in kg, as `training-log-exports.md` describes.
2. Confirm which rows are test sets. Ask the user if the log does not label them.
3. Confirm that each test single was successful. Leave out missed attempts.
4. Compute estimated 1RMs with one formula, as `estimated-1rm.md` describes.
5. Sort each athlete's rows by date, within each exercise.
6. Take the running maximum of tested singles for the best tested 1RM.
7. Take the running maximum of estimates for the best estimated 1RM.
8. For rep maxes, take the running maximum for each rep count separately.
9. Find the body mass for each best, from the same day or the nearest weigh-in before it.
10. Divide the best load by body mass for relative strength.
11. Report each best with its date, its session, and its kind: tested, rep max, or estimated with the formula named.
12. Judge any new best with the noise rules below.

## Worked example

This example uses one made-up athlete's back squat over six months. The estimates use Epley with a 10-rep limit. Every number below came from running the calculation in Python.

| Date | Set | Body mass | Estimated 1RM | Best tested to date | Best estimated to date |
|---|---|---|---|---|---|
| 2026-03-02 | Test single, 140.0 kg | 84.0 kg | none | 140.0 kg | none |
| 2026-04-13 | 120.0 kg × 5, RIR 1 | 84.4 kg | 143.98 kg | 140.0 kg | 143.98 kg |
| 2026-06-01 | Test single, 147.5 kg | 85.5 kg | none | 147.5 kg | 143.98 kg |
| 2026-08-17 | 130.0 kg × 5, RIR 0 | 85.0 kg | 151.65 kg | 147.5 kg | 151.65 kg |

Step 1. The 2026-04-13 estimate is 120.0 × (1 + 0.0333 × 6) = 143.98 kg. It is higher than the tested 140.0 kg, but the best tested stays 140.0 kg.

Step 2. The 2026-06-01 test raises the best tested to 147.5 kg. The change from 140.0 kg is 7.5 kg, or 5.36%.

Step 3. Relative strength at each test is 140.0 ÷ 84.0 = 1.667 kg/kg, then 147.5 ÷ 85.5 = 1.725 kg/kg.

Step 4. Allometric relative strength is 140.0 ÷ 84.0^0.67 = 7.19 kg/kg^0.67, then 147.5 ÷ 85.5^0.67 = 7.49 kg/kg^0.67.

Step 5. Suppose the coach measured this athlete's typical error for the back squat 1RM at 3.0 kg, from a short retest. That TE is made up for this example. The noise band for two single tests is 1.96 × √2 × 3.0 = 8.32 kg. The 7.5 kg change is inside it, so it cannot be told apart from test noise.

Step 6. On 2026-08-17, the best estimated 1RM rises to 151.65 kg. The best tested stays 147.5 kg. With Brzycki, the same set gives 146.26 kg.

Result: on 2026-08-17, the best tested back squat 1RM is 147.5 kg (2026-06-01), or 1.725 kg/kg. The best estimated 1RM is 151.65 kg (Epley, 5 reps to failure, 2026-08-17). Report both, labeled, and do not call 151.65 kg a 1RM.

## What changes the number

These choices change the result even when the athlete's strength does not:

- Formula. In the worked example, the 2026-08-17 set gives a best estimate of 151.65 kg with Epley and 146.26 kg with Brzycki.
- Body mass date. Relative strength changes with the body mass you divide by. Use the same rule every time.
- Scaling. Ratio and allometric relative strength are on different scales. Never compare them.
- What counts as a test. A heavy single in training, labeled as a work set, is not in the tested best unless the coach says so.
- Technique standard. Depth, pause, and lockout rules change the load an athlete can lift. Keep them the same.
- Exercise variant and equipment. A safety bar squat best is not a back squat best.
- Units. A best in lb read as kg is 2.2 times too large.

## Units and typical range

Report bests in kg, with the date and kind. Report relative strength in kg/kg, or kg/kg^0.67 for the allometric form.

This skill does not give a typical range for 1RM or relative strength. They depend on the exercise, the athlete, and the technique standard. Use the athlete's own history.

Use this test variability to judge a change in a tested 1RM. A systematic review of 32 studies with 1595 participants found test-retest coefficients of variation from 0.5% to 12.1%, with a median of 4.2% (Grgic et al., 2020). The coefficient of variation is the typical retest error as a percentage of the mean. The same review found a median intraclass correlation of 0.97. The intraclass correlation shows how well athletes keep their rank order between tests, from 0 to 1. The spread is wide, so measure your own typical error with your athletes, exercise, and protocol. Use the noise band 1.96 × √2 × TE for two single tests, as the `monitoring-statistics` skill describes.

## Data you need

Collect this data:

- Source: a training log with one row per set, and test sets labeled.
- Fields: athlete, date, exercise, set type, reps, and load in kg.
- Body mass: in kg, with its date, for relative strength.
- Minimum data: one test or one estimate per exercise for a best. Two tests and a typical error before you judge a change.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Putting the highest estimate in the tested 1RM column.
- Taking the best across exercise variants, such as back squat and safety bar squat.
- Counting a missed attempt as a tested single.
- Mixing formulas in the best estimated column.
- Dividing a best from one date by body mass from a much later date, without saying so.
- Comparing relative strength in kg/kg with relative force in N/kg from a force plate.
- Calling every new best a real gain. Check it against the noise band.
- Letting a `MAXIFS` 0 show as a best when nothing matched.

## Example request

> I want a table of every athlete's best back squat, bench, and trap bar deadlift, tested and estimated, with the date and relative to body weight. Our log has test days marked. Can you build it in Excel?

## Check the result

Run these checks:

- Recompute one value by hand: 147.5 ÷ 85.5 = 1.725 kg/kg.
- Check that the best tested never goes down over time.
- Check that every tested best comes from a successful single in a test set.
- Check that every estimated best names its formula.
- Check that each best has a date and a session.

## Sources

This file draws on these sources:

- Jaric S. Muscle strength testing: use of normalisation for body size. Sports Medicine. 2002;32(10):615-631. https://doi.org/10.2165/00007256-200232100-00002 (abstract, accessed 2026-10-07)
- Grgic J, Lazinica B, Schoenfeld BJ, Pedisic Z. Test-retest reliability of the one-repetition maximum (1RM) strength assessment: a systematic review. Sports Medicine - Open. 2020;6(1):31. https://doi.org/10.1186/s40798-020-00260-z (abstract, accessed 2026-10-07)
