# Repeated sprint scores

Last checked: 2026-10-07

## What it measures

A repeated sprint test is a set of short maximal sprints with short recoveries between them. Its scores show how well an athlete holds sprint times across the set. The main scores are the best time, the mean time, and the percent decrement: how much slower the set was than if every sprint had matched the best one.

## Formula

Use these formulas for one set of sprints:

```text
best time (s)          = fastest sprint time in the set
mean time (s)          = total time / n
total time (s)         = sum of all sprint times
percent decrement (%)  = (total time / (n × best time) − 1) × 100
fatigue index (%)      = (slowest time − best time) / best time × 100
```

Define every term in the formula:

- `n`: the number of sprints completed in the set.
- `best time`: the fastest sprint in the set, in seconds. It need not be the first sprint.
- `n × best time`: the ideal total, if every sprint matched the best one.
- `slowest time`: the slowest sprint in the set, in seconds.

Report percent decrement as the main fatigue score. Glaister et al. (2008) compared 8 fatigue formulas across two protocols and found percent decrement the most valid and reliable. It uses every sprint in the set. Their formula reads `(100 × (total sprint time ÷ ideal sprint time)) − 100`, which is the same calculation.

Report the fatigue index, the slowest-to-fastest version, only for comparison with sources that use it. Glaister et al. (2008) noted that formulas built on the extreme sprints are pushed up by measurement noise. An athlete with no fatigue still varies from sprint to sprint.

Always report best time and mean time next to the percent decrement. Oliver (2009) argues that any fatigue score calculated from a small drop-off in performance is unreliable, so its use may be questioned. The measured times let the reader see what drove the score. Reporting them is this skill's choice.

Fix the protocol before you compare any two scores: sprint distance, number of sprints, recovery, and whether recovery is passive or active. Glaister et al. (2008) ran 12 × 30 m sprints, starting every 35 s in one protocol and every 65 s in the other. Mean percent decrement was 4.43 ± 1.79% with the shorter cycle and 1.97 ± 0.86% with the longer one. Note whether the protocol states the rest between sprints or the time from one start to the next. The two are not the same.

### Calculate it in a spreadsheet

Put one athlete per row, with the sprint times in seconds in `B2:G2` for a 6-sprint set. Use these formulas. They return a blank when a sprint is missing:

```text
Best time (s), H2:          =IF(COUNT(B2:G2)<6,"",MIN(B2:G2))
Mean time (s), I2:          =IF(COUNT(B2:G2)<6,"",AVERAGE(B2:G2))
Total time (s), J2:         =IF(COUNT(B2:G2)<6,"",SUM(B2:G2))
Percent decrement (%), K2:  =IF(COUNT(B2:G2)<6,"",(SUM(B2:G2)/(COUNT(B2:G2)*MIN(B2:G2))-1)*100)
Fatigue index (%), L2:      =IF(COUNT(B2:G2)<6,"",(MAX(B2:G2)-MIN(B2:G2))/MIN(B2:G2)*100)
```

Change the range and the count of 6 to match the protocol. Do not compute a score for a set with a missing sprint. A set with one sprint dropped gives a different score from the full set.

### Calculate it in Power BI and Tableau

Both versions assume one row per athlete, date, session, and sprint in a `measures` table. The sprint time is `measure_name` `rsa_sprint_time` in `s`, and `trial_number` is the sprint number in the set. Show one athlete, date, and session per row, without `trial_number` in the visual.

In Power BI, use these DAX measures:

```text
RSA sprints counted =
CALCULATE ( COUNTROWS ( measures ), measures[measure_name] = "rsa_sprint_time",
    measures[unit] = "s", measures[status] = "ok" )

RSA best time (s) =
CALCULATE ( MIN ( measures[value] ), measures[measure_name] = "rsa_sprint_time",
    measures[unit] = "s", measures[status] = "ok" )

RSA mean time (s) =
CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "rsa_sprint_time",
    measures[unit] = "s", measures[status] = "ok" )

RSA percent decrement (%) =
VAR n = [RSA sprints counted]
VAR total =
    CALCULATE ( SUM ( measures[value] ), measures[measure_name] = "rsa_sprint_time",
        measures[unit] = "s", measures[status] = "ok" )
VAR best = [RSA best time (s)]
RETURN IF ( n >= 2 && best > 0, ( total / ( n * best ) - 1 ) * 100 )
```

Show `RSA sprints counted` in the same visual, so a set with a missing sprint is visible.

In Tableau, put `athlete_id`, `measure_date`, and `session_id` on the view. Use these aggregate calculations:

```text
RSA sprints counted:
COUNT(IF [measure_name] = "rsa_sprint_time" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

RSA best time (s):
MIN(IF [measure_name] = "rsa_sprint_time" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

RSA total time (s):
SUM(IF [measure_name] = "rsa_sprint_time" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

RSA percent decrement (%):
IF [RSA sprints counted] < 2 OR ISNULL([RSA best time (s)]) OR [RSA best time (s)] <= 0 THEN NULL
ELSE ([RSA total time (s)] / ([RSA sprints counted] * [RSA best time (s)]) - 1) * 100
END
```

Blanks behave this way in each tool:

- Power BI: a sprint with no row is not counted, so the count shows it. The decrement is blank with fewer than 2 sprints.
- Tableau: `COUNT` skips nulls, so a missing sprint lowers the count. The decrement is null with fewer than 2 sprints.

### Calculate it in Python

Use this Python code. It uses the standard library only:

```python
def repeated_sprint(times_s, expected_n):
    if len(times_s) != expected_n:
        raise ValueError(f"expected {expected_n} sprints, got {len(times_s)}")
    n, total, best, worst = len(times_s), sum(times_s), min(times_s), max(times_s)
    return {"best_s": best, "mean_s": total / n, "total_s": total,
            "decrement_pct": (total / (n * best) - 1) * 100,
            "fatigue_index_pct": (worst - best) / best * 100}
```

## Calculate the metric

Follow these steps to calculate the scores from raw inputs:

1. Record the protocol: sprint distance, number of sprints, recovery time, and recovery type.
2. Record whether the recovery time is the rest between sprints or the time from one start to the next.
3. Convert every sprint time to seconds.
4. Check that the set has the expected number of sprints.
5. Stop and tell the user if a sprint is missing or marked invalid.
6. Find the best time, the fastest sprint in the set.
7. Add all sprint times to get the total time.
8. Divide the total time by the number of sprints to get the mean time.
9. Calculate the percent decrement.
10. Calculate the fatigue index only if the user needs it for comparison.
11. Report best time, mean time, and percent decrement together, with the protocol.

## Worked example

This example uses one made-up athlete in a 6 × 30 m set. Every number below came from running the calculation in Python.

| Sprint | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Time (s) | 4.31 | 4.28 | 4.36 | 4.42 | 4.47 | 4.51 |

Step 1. Best time = 4.28 s, from sprint 2.

Step 2. Total time = 26.35 s. Mean time = 26.35 / 6 = 4.3917 s.

Step 3. Ideal total = 6 × 4.28 = 25.68 s.

Step 4. Percent decrement = (26.35 / 25.68 − 1) × 100 = 2.609%.

Step 5. Fatigue index = (4.51 − 4.28) / 4.28 × 100 = 5.374%.

Result: best time 4.28 s, mean time 4.39 s, and percent decrement 2.61%.

## What changes the number

These choices change the result even when the athlete's sprinting does not change:

- Protocol. Recovery length changed mean percent decrement from 4.43% to 1.97% in the same athletes (Glaister et al., 2008). Distance and number of sprints change it too.
- Best sprint choice. Using sprint 1 as the best in the worked example, instead of the fastest sprint, gives 1.895% instead of 2.609%. Glaister et al. (2008) found the fastest sprint was sprint 1 in 70% of cases with the shorter cycle and 50% with the longer one.
- Formula. In the worked example, percent decrement is 2.609%, the slowest-to-fastest fatigue index is 5.374%, and the first-to-last version is 4.640%. Never mix formulas in one trend.
- A missing sprint. Dropping sprint 4 from the worked example gives 2.477%. Do not score an incomplete set.
- Start and timing. Use the same start and gate layout for every sprint and every test.
- Surface, footwear, and warm-up. Keep them the same at every test.

## Units and typical range

Report best and mean time in seconds, and percent decrement in percent, with the protocol.

| Population | Typical range | Source |
|---|---|---|
| Physically active men (n = 10), 12 × 30 m, one sprint every 35 s | Percent decrement 4.43 ± 1.79% (mean ± SD) | Glaister et al., 2008 |
| Same athletes, 12 × 30 m, one sprint every 65 s | Percent decrement 1.97 ± 0.86% | Glaister et al., 2008 |

Use these ranges to check that data are plausible, not to rate athletes. Values from another protocol are not comparable.

Use this test variability to judge a change in one athlete. Between two trials at least 48 hours apart, the coefficient of variation of percent decrement was 31.7% with the 35 s cycle and 37.4% with the 65 s cycle (Glaister et al., 2008). With a CV near a third, a change in percent decrement of a third of its value can be noise. Measure your own typical error, as the `monitoring-statistics` skill describes.

Protocols vary. Of 30 elite soccer practitioners who tested repeated sprints, the most common protocol was 7 × 30 m with 20 s rest, used by 10 of them (Asimakidis et al., 2024).

## Data you need

Collect this data:

- Source: timing gates, or another timer that records each sprint in the set.
- Protocol: sprint distance, number of sprints, recovery time and type, and start method.
- Minimum data: one complete set. Judge change only against a typical error measured with the same protocol.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using sprint 1 as the best time. Use the fastest sprint in the set.
- Dividing by the slowest time, or by the mean, instead of n × best time.
- Comparing scores from different protocols or recovery times.
- Scoring a set with a missing or invalid sprint.
- Reporting percent decrement alone. Show best time and mean time beside it.
- Calling a change real when it is inside the test's noise. The decrement is noisy.
- Reading percent decrement as a measure of fitness for match play or as an injury signal. It describes this test only.

## Example request

> We did 6 × 30 m with 20 seconds' rest. Can you work out each player's fatigue score in Excel from these sprint times?

## Check the result

Run these checks:

- Recompute one value by hand: (26.35 / (6 × 4.28) − 1) × 100 = 2.61%.
- Check that percent decrement is not negative. It cannot be, because the best time is the minimum.
- Check that the count of sprints matches the protocol for every athlete.
- Check that the best time is the fastest sprint, not sprint 1.
- Check that every value used the same protocol.

## Sources

This file draws on these sources:

- Glaister M, Howatson G, Pattison JR, McInnes G. The reliability and validity of fatigue measures during multiple-sprint work: an issue revisited. Journal of Strength and Conditioning Research. 2008;22(5):1597-1601. https://doi.org/10.1519/JSC.0b013e318181ab80 (author manuscript at https://research.stmarys.ac.uk/id/eprint/107/, accessed 2026-10-07; the decrements and CVs were read in Tables 1 and 2, Formula 4, of the author manuscript)
- Oliver JL. Is a fatigue index a worthwhile measure of repeated sprint ability? Journal of Science and Medicine in Sport. 2009;12(1):20-23. https://doi.org/10.1016/j.jsams.2007.10.010 (abstract, accessed 2026-10-07)
- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
