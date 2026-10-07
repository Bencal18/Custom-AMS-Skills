# Volume load

Last checked: 2026-10-07

## What it measures

Volume load is the total load an athlete lifted in a set, exercise, session, or week: reps multiplied by load, added up over sets.

Strength and conditioning coaches use it often. In an online survey of 58 practitioners from 9 Southeast and East Asian countries, 81% quantified training load with volume load and 72% with session rating of perceived exertion (Washif et al., 2025). Scott et al. (2016) describe volume load as one of several methods that give useful information about resistance training.

Volume load counts how much was lifted. It does not show how hard the sets were, how close to failure they went, or how fast the bar moved. Scott et al. (2016) note that resistance training has many variables, and that there is no consensus on how best to combine the methods that measure it.

## Formula

Use this formula for each set, then add up the sets:

```text
set volume load (kg)      = reps × load (kg)
exercise volume load (kg) = sum of set volume load over the work sets of one exercise
session volume load (kg)  = sum of exercise volume load over the session
weekly volume load (kg)   = sum of session volume load over the week
```

When every set of an exercise has the same reps and load, the exercise volume load is sets × reps × load.

Define every term in the formula:

- `reps`: reps completed in the set, not reps planned
- `load`: the external load lifted, in kilograms. For a barbell, the bar plus plates. For dumbbells and kettlebells, see the rules below.
- `work sets`: sets the coach counts as training. Leaving out warm-up sets unless the user asks for them is this skill's default choice. Say which you used.
- `week`: Monday to Sunday by default. That is this skill's choice. Use the user's training week if it differs.

McBride et al. (2009) defined volume load as repetitions × external load. They compared it with three other methods: a version that adds body mass to the external load, time under tension, and total work (force × displacement). They applied the four methods to three squat protocols: two with external loads and a jump squat with no external load (0% of 1RM). The four methods gave different answers for the same protocols. Name the method you use.

### Absolute and relative load

Load can be written two ways:

- Absolute load: the load in kg. Volume load in this file uses absolute load.
- Relative load: the load as a percentage of the athlete's 1RM, the heaviest load they can lift once. Relative load (%1RM) = load (kg) ÷ 1RM (kg) × 100.

Relative load depends on which 1RM you divide by: a tested 1RM, an estimated 1RM, or a 1RM from bar speed. The coach chooses it. Name it next to every %1RM value.

Scott et al. (2016) note that %1RM alone does not capture the effects of rest between sets, rep speed, or the number of reps done at that load.

Some coaches want a volume load in %1RM units, reps × %1RM summed over sets. This skill found no source that defines it. Compute it only if the user asks, and label it as this skill's variant.

### Special cases

Each special case needs a rule. Ask the user which one to use, and use it for every athlete and session. The rules below are this skill's choices unless a source is named:

- Bodyweight exercises, such as push-ups, pull-ups, and dips: by default, count reps, and keep them out of volume load. That is this skill's choice. McBride et al. (2009) added body mass, minus the shank (lower leg) mass, to the external load for a squat. That method needs a share of body mass for each exercise, and this skill found no published shares for push-ups, dips, or pull-ups. If the user wants body mass included, use reps × (body mass + added load) for exercises where the whole body moves, such as a pull-up or dip. Label it "system mass volume load", and never add it to external volume load.
- Weighted bodyweight exercises, such as a pull-up with a 20 kg belt: by default, count the added load only, and label it. That is this skill's choice.
- Single-leg and single-arm exercises, such as split squats and single-arm rows: record each side as its own row. Report volume load per side, or the total of both sides, and label which. A total of both sides is twice the per-side value when both sides match.
- Dumbbells and kettlebells: for a two-implement lift, such as a dumbbell bench press with two 30 kg dumbbells, the load is 60 kg. For a one-implement lift on one side, the load is the one implement. Check how the log records it.
- Isometric holds and timed sets, such as planks and wall sits: these have no reps, so they have no volume load. Report time under load in seconds (sets × duration), separately. McBride et al. (2009) treated time under tension as its own method.
- Bands and chains: the load changes through the rep, and the log usually records only the bar and plates. By default, count the bar and plates only, and flag the set as `band_chain`. That is this skill's choice. Do not add an estimated band tension unless the user gives a measured value.
- Machine lifts: use the load the machine shows. A machine's displayed load is not comparable with a free-weight load, so keep machine lifts as their own exercise.

### Calculate it in a spreadsheet

Every version below follows this skill's default rules for the special cases, which are this skill's choices, not rules from a source. Each version counts external sets, the bar and plates of band and chain sets, and the added load of weighted bodyweight sets. It leaves out bodyweight sets with no added load, and timed sets. If the user picks another rule, change the filter and label the result. Report weighted bodyweight and band or chain sets on their own lines when the coach wants them apart.

Put one set per row, with reps in `H2`, load in `I2`, `load_unit` in `J2`, `load_type` in `K2`, and `status` in `M2`. Use this formula for the set volume load in `L2`. It returns a blank unless the status is `ok`, reps and load are numbers, the load is above 0, the unit is kg, and the set is not timed:

```text
=IF(AND(ISNUMBER(H2),ISNUMBER(I2),J2="kg",K2<>"timed",M2="ok"),IF(I2>0,H2*I2,""),"")
```

For a session total, put the athlete ID in `A`, the session ID in `C`, the exercise in `D`, and `set_type` in `F`. Use this formula, with the athlete in `N2` and the session in `O2`:

```text
=SUMIFS(L:L,A:A,N2,C:C,O2,F:F,"work")
```

Add `D:D,P2` to the `SUMIFS` for one exercise. For a week, add the date in `B` with `B:B,">="&Q2,B:B,"<"&Q2+7`, where `Q2` is the Monday. The `<` test keeps Sunday rows that carry a time of day.

### Calculate it in Power BI and Tableau

Both versions assume the `sets` table in `training-log-exports.md`, with one row per set and loads already in kg.

In Power BI, use this DAX measure. It works at any level the visual shows: set, exercise, session, or week. Put `side` in the visual for per-side values. Without `side`, single-leg and single-arm exercises give the total of both sides:

```text
Volume load (kg) =
SUMX (
    FILTER (
        sets,
        sets[status] = "ok"
            && sets[set_type] = "work"
            && sets[load_unit] = "kg"
            && sets[load_type] <> "timed"
            && NOT ISBLANK ( sets[reps] )
            && NOT ISBLANK ( sets[load] )
            && sets[load] > 0
    ),
    sets[reps] * sets[load]
)
```

For weeks, add a date table marked as a date table, with a week start column such as `Week start = 'Date'[Date] - WEEKDAY ( 'Date'[Date], 3 )`. `WEEKDAY` with return type 3 counts Monday as 0, so this gives the Monday of each week.

In Tableau, use this aggregate calculation. Put `athlete_id` and `session_id`, or `exercise`, on the view:

```text
Volume load (kg):
SUM(IF [status] = "ok" AND [set_type] = "work" AND [load_unit] = "kg"
       AND [load_type] <> "timed" AND NOT ISNULL([reps]) AND [load] > 0
    THEN [reps] * [load] END)
```

For weeks, put `DATETRUNC('week', [session_date], 'monday')` on the view.

Blanks behave this way in each tool:

- Power BI: rows with a blank reps or load are filtered out, so they add nothing. A session with no counted rows gives a blank, not 0.
- Tableau: rows that fail the test give null, and `SUM` skips nulls. A session with no counted rows gives null.

Report how many rows each tool left out. A blank total is not a rest day.

### Calculate it in Python or R

Use this Python code. It uses the standard library only:

```python
from collections import defaultdict

def volume_load(rows, by=("athlete_id", "session_id", "exercise")):
    totals, skipped = defaultdict(float), 0
    for r in rows:
        ok = (r["status"] == "ok" and r["set_type"] == "work"
              and r["load_unit"] == "kg" and r["load_type"] != "timed"
              and r["reps"] is not None and r["load"] is not None
              and r["load"] > 0)
        if not ok:
            skipped += 1
            continue
        totals[tuple(r[k] for k in by)] += r["reps"] * r["load"]
    return dict(totals), skipped
```

Use this R code with dplyr:

```r
library(dplyr)
volume <- sets |>
  filter(status == "ok", set_type == "work", load_unit == "kg",
         load_type != "timed", !is.na(reps), !is.na(load), load > 0) |>
  group_by(athlete_id, session_id, exercise) |>
  summarise(volume_load_kg = sum(reps * load), .groups = "drop")
```

## Calculate the metric

Follow these steps to calculate volume load from a training log:

1. Reshape the log to one row per set, as `training-log-exports.md` describes.
2. Convert every load to kg.
3. Label each set `warmup`, `work`, or `test`.
4. Label each set's `load_type`: `external`, `bodyweight`, `timed`, or `band_chain`.
5. Apply the user's rule for each special case above.
6. Multiply reps by load for each counted set.
7. Add up the sets by exercise.
8. Add up the exercises by session, and label the total as a sum across exercises.
9. Add up the sessions by week.
10. Report bodyweight reps and time under load next to volume load, not inside it.
11. Report how many rows you left out, and why.

## Worked example

This example uses one made-up athlete with a body mass of 82.0 kg and two sessions in one week. Every number below came from running the calculation in Python.

Session 1 had these sets:

| Exercise | Sets | Volume load |
|---|---|---|
| Back squat, warm-up | 1 × 5 at 60 kg | 300 kg, left out |
| Back squat | 5 at 120, 5 at 120, 5 at 125, 4 at 125 kg | 600 + 600 + 625 + 500 = 2325 kg |
| Romanian deadlift | 3 × 8 at 90 kg | 2160 kg |
| Split squat, 2 × 20 kg dumbbells | 3 × 8 per side at 40 kg | 960 kg per side, 1920 kg both sides |
| Pull-up, body mass only | 3 × 6 | 18 reps, no volume load |
| Plank | 3 × 30 s | 90 s under load, no volume load |

Step 1. Session 1 volume load, work sets, both sides of the split squat = 2325 + 2160 + 1920 = 6405 kg.

Step 2. With the warm-up set counted, it is 6705 kg.

Step 3. With the split squat counted per side, it is 2325 + 2160 + 960 = 5445 kg.

Step 4. If the user chooses system mass volume load for the pull-up: 18 × 82.0 = 1476 kg. Report it on its own line, not in the 6405 kg.

Step 5. Session 2 had a bench press of 4 × 6 at 80 kg (1920 kg) and a row of 3 × 10 at 60 kg (1800 kg), for 3720 kg.

Step 6. Weekly volume load = 6405 + 3720 = 10125 kg.

Step 7. Relative load: if the coach's chosen squat 1RM is 150 kg, the 125 kg sets were 125 ÷ 150 × 100 = 83.3% of 1RM.

Step 8. If the Romanian deadlift had been logged as 200 lb and read as kg, its volume load would show 4800 kg. Converted, 200 lb is 90.72 kg, and the volume load is 2177.2 kg.

Result: session 1 volume load is 6405 kg, counting work sets with external load and both sides of the split squat. The week is 10125 kg. The pull-up and plank are reported as 18 reps and 90 s.

## What changes the number

These choices change the result even when the training does not:

- Warm-up sets. In the worked example, counting one warm-up set raises session 1 from 6405 to 6705 kg.
- Per side or both sides. In the worked example, the split squat adds 960 or 1920 kg.
- Bodyweight rule. Counting the pull-up as system mass adds 1476 kg.
- Units. A load in lb read as kg makes that exercise 2.2 times too large.
- Dumbbell recording. One implement or both changes the load by a factor of 2.
- Planned or completed reps. A log that stores the plan gives the plan's volume load.
- Week boundaries. A Sunday session falls in a different week with a Sunday or Monday week start.
- Exercise mix. A session of deadlifts and a session of curls can have the same reps and very different volume loads. Compare volume load within one exercise.

## Units and typical range

Report volume load in kg. Report bodyweight reps as a count, and time under load in s.

This skill found no published typical range for volume load. It depends on the exercise, the program, and the athlete. Compare an athlete's volume load with their own history for the same exercise.

## Data you need

Collect this data:

- Source: a training log with one row per set, or one that can be reshaped to it.
- Fields: athlete, date, session, exercise, set, reps completed, load, and unit. Add set type, side, and load type when the log has them.
- Body mass: only for system mass volume load or relative strength.
- Minimum data: one session for a session total. Several weeks of the same exercises before you compare weeks.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing kg and lb in one sum. Convert to kg first.
- Using planned reps or planned loads instead of completed ones.
- Counting a single-leg exercise once when the log has one row per side, or twice when the log has one row for both sides.
- Adding bodyweight reps to external volume load as if the load were 0 or the full body mass.
- Giving a plank or wall sit a volume load.
- Adding up volume load across very different exercises and reading the total as one measure of effort.
- Reading a blank week as a week of 0 load.
- Treating volume load as a measure of intensity or fatigue. It counts work done. Pair it with RPE or another measure if the coach wants intensity.

## Example request

> Our training log export has one row per set with athlete, date, exercise, reps, and load in pounds. Can you give me volume load per athlete per week in kg, and tell me what you did with the pull-ups and planks?

## Check the result

Run these checks:

- Recompute one set by hand: 5 × 125 = 625 kg.
- Check that the session total equals the sum of the exercise totals.
- Check that bodyweight and timed sets are reported apart from volume load.
- Check the unit of every load column before you sum.
- Check that each single-leg or single-arm total is labeled per side or both sides.

## Sources

This file draws on these sources:

- Washif JA, James C, Pagaduan J, Lim J, Lum D, Raja Azidin RMF, Mujika I, Beaven CM. Current periodization, testing, and monitoring practices of strength and conditioning coaches. International Journal of Sports Physiology and Performance. 2025;20(9):1239-1252. https://doi.org/10.1123/ijspp.2025-0051 (abstract, accessed 2026-10-07)
- Scott BR, Duthie GM, Thornton HR, Dascombe BJ. Training monitoring for resistance exercise: theory and applications. Sports Medicine. 2016;46(5):687-698. https://doi.org/10.1007/s40279-015-0454-0 (abstract, accessed 2026-10-07)
- McBride JM, McCaulley GO, Cormie P, Nuzzo JL, Cavill MJ, Triplett NT. Comparison of methods to quantify volume during resistance exercise. Journal of Strength and Conditioning Research. 2009;23(1):106-110. https://doi.org/10.1519/JSC.0b013e31818efdfe (abstract, accessed 2026-10-07)
