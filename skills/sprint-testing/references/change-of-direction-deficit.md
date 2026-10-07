# Change of direction deficit

Last checked: 2026-10-07

## What it measures

Change of direction (COD) deficit is the extra time an athlete needs to turn 180° in the 505 test, compared with running the same distance in a straight line. It removes most of the linear speed from the 505 time, so it isolates turning more than the 505 time does (Nimphius et al., 2016).

Practitioners test change of direction often. Of 49 elite soccer practitioners who tested it, 27 (55%) used the 505 (Asimakidis et al., 2024). In a survey of 170 soccer strength and conditioning coaches, 61% of first team coaches and 77% of academy coaches assessed change of direction (McQuilliam et al., 2023).

The 505 test times a 180° turn. In one common layout, the athlete sprints from a start line, passes a timing gate at 10 m, turns at a line 15 m from the start, and runs back through the gate. The 505 time runs from the first pass of the gate to the second, so it covers 5 m in, the turn, and 5 m out (Roso-Moliner et al., 2023). Each side is tested on its own. The side is the foot the athlete plants to turn.

## Formula

Calculate the deficit for each side:

```text
COD deficit_side (s) = 505 time_side (s) − 10 m sprint time (s)
```

Define every term in the formula:

- `505 time_side`: the 505 time when the athlete turns on that side, in seconds. Use the mean of trials (Nimphius et al., 2016; Dos'Santos et al., 2018) or the best trial (Dos'Santos et al., 2019). Use the same choice for both tests and every session.
- `10 m sprint time`: time over the first 10 m of a straight sprint, in seconds, with the same trial summary.
- `side`: `left` or `right`, the plant foot for the turn.

Use the same start for both tests: the same stance, the same distance behind the first gate, and the same trigger. Dos'Santos et al. (2019) started both tests 0.5 m behind the first gate from a two-point staggered stance. A 10 m time from a different start shifts every deficit by the full difference.

### Side-to-side difference

Dos'Santos et al. (2019) compared the two sides with this formula, where D is the faster side, with the shorter deficit, and ND is the slower side:

```text
deficit asymmetry (%) = (D deficit − ND deficit) / D deficit × 100
```

The result is negative by design, because D is the shorter time. Report which side is faster next to it. Dos'Santos et al. (2018) used the same formula. If the `limb-symmetry` skill is installed, name this formula as a separate variant and do not swap it for a limb symmetry index.

Asymmetry in the deficit is much larger than asymmetry in the 505 time. In 43 youth netball players, 2 athletes showed a 505 time asymmetry of 10% or more, and 21 showed a deficit asymmetry of 10% or more (Dos'Santos et al., 2019). A small difference in the 505 time is a large share of a deficit of about 0.5 s.

### The pro-agility test

This skill found no validated deficit for the pro-agility (5-10-5) test. Some studies compute one, with different formulas. Yamashita et al. (2024) paired the pro-agility test with 10 m and 20 m sprint times. Freitas et al. (2018) subtracted pro-agility velocity from 20 m sprint velocity over the same distance. The formulas differ, so their values are not comparable. Do not compute a pro-agility deficit unless the user asks. If they ask, name the formula and say that no validation was found.

### Calculate it in a spreadsheet

Put one athlete per row. Put the three 10 m times in `B2:D2`, the three left 505 times in `E2:G2`, and the three right 505 times in `H2:J2`, all in seconds. Use these formulas, which return a blank when a trial is missing:

```text
Left deficit (s), K2:   =IF(COUNT(B2:D2,E2:G2)<6,"",AVERAGE(E2:G2)-AVERAGE(B2:D2))
Right deficit (s), L2:  =IF(COUNT(B2:D2,H2:J2)<6,"",AVERAGE(H2:J2)-AVERAGE(B2:D2))
Faster side, M2:        =IF(COUNT(K2:L2)<2,"",IF(K2<L2,"left",IF(L2<K2,"right","equal")))
Asymmetry (%), N2:      =IF(COUNT(K2:L2)<2,"",IF(MIN(K2:L2)<=0,"check",(MIN(K2:L2)-MAX(K2:L2))/MIN(K2:L2)*100))
```

For the best-trial variant, replace `AVERAGE` with `MIN`. If your protocol has fewer trials, change the count of 6.

### Calculate it in Power BI and Tableau

Both versions assume one row per athlete, date, session, measure, side, and trial in a `measures` table. The 10 m time is `measure_name` `sprint_10m_time`, `side` `bilateral`, in `s`. The 505 time is `cod_505_time`, `side` `left` or `right`, in `s`. Both versions use the mean of trials. Use `MIN` instead of `AVERAGE` for the best-trial variant.

In Power BI, use these DAX measures. Put `side` in the visual for the deficit, and leave it out for the asymmetry:

```text
COD deficit (s) =
VAR s = SELECTEDVALUE ( measures[side] )
VAR t505 =
    CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "cod_505_time",
        measures[unit] = "s", measures[status] = "ok" )
VAR t10 =
    CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "sprint_10m_time",
        measures[side] = "bilateral", measures[unit] = "s", measures[status] = "ok" )
RETURN
    IF ( s IN { "left", "right" } && NOT ISBLANK ( t505 ) && NOT ISBLANK ( t10 ), t505 - t10 )

COD deficit asymmetry (%) =
VAR t10 =
    CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "sprint_10m_time",
        measures[side] = "bilateral", measures[unit] = "s", measures[status] = "ok" )
VAR l505 =
    CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "cod_505_time",
        measures[side] = "left", measures[unit] = "s", measures[status] = "ok" )
VAR r505 =
    CALCULATE ( AVERAGE ( measures[value] ), measures[measure_name] = "cod_505_time",
        measures[side] = "right", measures[unit] = "s", measures[status] = "ok" )
VAR dl = l505 - t10
VAR dr = r505 - t10
VAR d = MIN ( dl, dr )
VAR nd = MAX ( dl, dr )
RETURN
    IF ( NOT ISBLANK ( t10 ) && NOT ISBLANK ( l505 ) && NOT ISBLANK ( r505 ) && d > 0,
        ( d - nd ) / d * 100 )
```

The `measures[side] = "bilateral"` filter replaces the side in the visual, so the 10 m time is found on the left and right rows. The `ISBLANK` tests matter: in DAX, a blank minus a number gives the negative number, not a blank.

In Tableau, put `athlete_id`, `measure_date`, and `session_id` on the view, without `side`. Use these aggregate calculations:

```text
10 m time (s):
AVG(IF [measure_name] = "sprint_10m_time" AND [side] = "bilateral" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

505 left (s):
AVG(IF [measure_name] = "cod_505_time" AND [side] = "left" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

505 right (s):
AVG(IF [measure_name] = "cod_505_time" AND [side] = "right" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

COD deficit left (s):
[505 left (s)] - [10 m time (s)]

COD deficit right (s):
[505 right (s)] - [10 m time (s)]

COD deficit asymmetry (%):
IF ISNULL([COD deficit left (s)]) OR ISNULL([COD deficit right (s)]) THEN NULL
ELSEIF MIN([COD deficit left (s)], [COD deficit right (s)]) <= 0 THEN NULL
ELSE (MIN([COD deficit left (s)], [COD deficit right (s)]) - MAX([COD deficit left (s)], [COD deficit right (s)]))
     / MIN([COD deficit left (s)], [COD deficit right (s)]) * 100
END
```

Blanks behave this way in each tool:

- Power BI: a missing 10 m or 505 time gives a blank deficit and a blank asymmetry.
- Tableau: a null in either time gives a null deficit, and the asymmetry returns null.

### Calculate it in Python

Use this Python code. It uses the standard library only:

```python
from statistics import mean

def cod_deficit(sprint_10m_s, t505_left_s, t505_right_s, summary=mean):
    t10 = summary(sprint_10m_s)
    left = summary(t505_left_s) - t10
    right = summary(t505_right_s) - t10
    d, nd = min(left, right), max(left, right)
    faster = "left" if left < right else "right" if right < left else "equal"
    return {"left_s": left, "right_s": right, "faster_side": faster,
            "asymmetry_pct": (d - nd) / d * 100 if d > 0 else None}
```

Pass `summary=min` for the best-trial variant.

## Calculate the metric

Follow these steps to calculate the deficit from raw inputs:

1. Find the 10 m sprint times and the 505 times, and convert them to seconds.
2. Label each 505 trial `left` or `right` by the plant foot.
3. Check that both tests used the same start stance, distance behind the first gate, and trigger.
4. Stop and tell the user if the starts differ.
5. Choose the trial summary, the mean or the best, and use it for both tests.
6. Summarize the 10 m trials.
7. Summarize the 505 trials for each side.
8. Subtract the 10 m value from each side's 505 value.
9. Name the faster side, the one with the shorter deficit.
10. Calculate the asymmetry with the faster side as D.
11. Report each side's deficit, the faster side, the asymmetry, the trial summary, and the start.

## Worked example

This example uses one made-up athlete with three trials of each test. Both tests started 0.5 m behind the first gate from the same stance. Every number below came from running the calculation in Python.

| Input | Trials (s) |
|---|---|
| 10 m sprint | 1.92, 1.97, 1.95 |
| 505, left plant foot | 2.45, 2.51, 2.48 |
| 505, right plant foot | 2.40, 2.41, 2.45 |

Step 1. Mean 10 m time = 1.9467 s. Mean 505 time is 2.4800 s on the left and 2.4200 s on the right.

Step 2. Left deficit = 2.4800 − 1.9467 = 0.5333 s. Right deficit = 2.4200 − 1.9467 = 0.4733 s.

Step 3. The right side is faster. Asymmetry = (0.4733 − 0.5333) / 0.4733 × 100 = −12.68%.

Step 4. For comparison, the asymmetry in mean 505 time is (2.4200 − 2.4800) / 2.4200 × 100 = −2.48%.

Step 5. With the best trial instead, the deficits are 0.53 s left and 0.48 s right, and the asymmetry is −10.42%.

Result: with the mean of trials, the deficit is 0.533 s on the left and 0.473 s on the right. The right side is faster, with a deficit asymmetry of −12.7%.

## What changes the number

These choices change the result even when the athlete's turning does not change:

- Trial summary. In the worked example, the mean gives an asymmetry of −12.68% and the best trial gives −10.42%.
- Start type. A 10 m time 0.05 s faster, from a different start, raises each deficit by 0.05 s. For the right side in the worked example, that is about 10.6%.
- Timing resolution. One timing step of 0.01 s is about 2% of a 0.47 s deficit.
- Gate height. Dos'Santos et al. (2019) set gates at about hip height, so that one body part breaks the beam.
- Surface and footwear. Dos'Santos et al. (2018) ran both tests on the same surface. Keep both the same at every test.
- Side labels. A swap of left and right reverses the faster side.
- Order and rest. Dos'Santos et al. (2019) alternated sides with 2 minutes' rest between trials.

## Units and typical range

Report the deficit in seconds for each side, and the asymmetry in percent with the faster side named.

| Population | Typical range, mean of 3 trials | Source |
|---|---|---|
| Male soccer players (n = 16) | Deficit 0.493 ± 0.097 s left, 0.469 ± 0.117 s right; asymmetry −18.5 ± 12.2% | Dos'Santos et al., 2018 |
| Female soccer players (n = 15) | Deficit 0.533 ± 0.106 s left, 0.529 ± 0.170 s right; asymmetry −24.0 ± 18.4% | Dos'Santos et al., 2018 |
| Male cricket players (n = 23) | Deficit 0.575 ± 0.094 s left, 0.517 ± 0.148 s right; asymmetry −28.4 ± 26.5% | Dos'Santos et al., 2018 |
| Female netball players (n = 21) | Deficit 0.548 ± 0.071 s left, 0.530 ± 0.105 s right; asymmetry −11.0 ± 10.1% | Dos'Santos et al., 2018 |

All values are mean ± SD. Use them to check that data are plausible, not to rate athletes.

Use this test variability to judge a change in one athlete. Within one session, the coefficient of variation (CV) of the deficit ranged from 4.9% to 15.5% across the six groups in the study. The CV of the 505 time ranged from 1.1% to 3.3% (Dos'Santos et al., 2018). The deficit is noisier than the 505 time in relative terms, so it needs a larger change before you call it real. Measure your own typical error from a retest with your athletes, as the `monitoring-statistics` skill describes.

Dos'Santos et al. (2019) classed youth netball players as asymmetrical beyond a deficit asymmetry of −14.5%. They set that line from their own sample's mean and SD. It is a study setting, not a cut-off for your athletes.

## Data you need

Collect this data:

- Source: timing gates for a 10 m sprint and the 505 test, in the same session.
- Trials: Dos'Santos et al. (2018, 2019) used 3 trials of each test, with 3 for each side of the 505.
- Start: the same stance, distance behind the first gate, and trigger for both tests.
- Labels: the plant foot for every 505 trial.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using a 10 m time from a different start or a different session. Use the same start in the same session.
- Using the full 505 run, 15 m out and 5 m back, instead of the timed 10 m around the turn.
- Mixing the mean of trials for one test with the best trial for the other.
- Averaging the two sides into one deficit. Report each side.
- Calling the asymmetry positive. With the faster side as D, the formula gives a negative value.
- Computing a pro-agility deficit and comparing it with 505 deficit values.
- Reading the asymmetry as an injury signal. It shows turning time only.

## Example request

> We ran the 505 both ways and a 10 m sprint today, three trials each. Can you add change of direction deficit for each side and show which athletes are much slower turning one way?

## Check the result

Run these checks:

- Recompute one value by hand: 2.4200 − 1.9467 = 0.4733 s.
- Check that each deficit is positive. A negative deficit means the 505 time is shorter than the 10 m time, which points to a start, gate, or label problem.
- Check that the 10 m and 505 values came from the same session and the same start.
- Check that each side has the expected number of trials.
- Check the faster side against the raw 505 times.

## Sources

This file draws on these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
- McQuilliam SJ, Clark DR, Erskine RM, Brownlee TE. Physical testing and strength and conditioning practices differ between coaches working in academy and first team soccer. International Journal of Sports Science and Coaching. 2023;18(4):1045-1055. https://doi.org/10.1177/17479541231155108 (abstract, accessed 2026-10-07)
- Nimphius S, Callaghan SJ, Spiteri T, Lockie RG. Change of direction deficit: a more isolated measure of change of direction performance than total 505 time. Journal of Strength and Conditioning Research. 2016;30(11):3024-3032. https://doi.org/10.1519/JSC.0000000000001421 (abstract, accessed 2026-10-07)
- Dos'Santos T, Thomas C, Jones PA, Comfort P. Assessing asymmetries in change of direction speed performance: application of change of direction deficit. Journal of Strength and Conditioning Research. 2019;33(11):2953-2961. https://doi.org/10.1519/JSC.0000000000002438 (accessed 2026-10-07; the 0.5 m start and the −14.5% threshold were read in the accepted manuscript at https://repository.mmu.ac.uk/articles/journal_contribution/Assessing_Asymmetries_in_Change_of_Direction_Speed_Performance_Application_of_Change_of_Direction_Deficit/32545257)
- Dos'Santos T, Thomas C, Comfort P, Jones PA. Comparison of change of direction speed performance and asymmetries between team-sport athletes: application of change of direction deficit. Sports. 2018;6(4):174. https://doi.org/10.3390/sports6040174 (accessed 2026-10-07)
- Roso-Moliner A, Lozano D, Nobari H, Bishop C, Carton-Llorente A, Mainer-Pardos E. Horizontal jump asymmetries are associated with reduced range of motion and vertical jump performance in female soccer players. BMC Sports Science, Medicine and Rehabilitation. 2023;15:80. https://doi.org/10.1186/s13102-023-00697-1 (accessed 2026-10-07)
- Freitas TT, Alcaraz PE, Bishop C, Calleja-González J, Arruda AFS, Guerriero A, Reis VP, Pereira LA, Loturco I. Change of direction deficit in national team rugby union players: is there an influence of playing position? Sports. 2018;7(1):2. https://doi.org/10.3390/sports7010002 (accessed 2026-10-07)
- Yamashita N, Sato D, Mishima T. Jump height ingenerated by countermovement and arm swing better correlates with proagility shuttle run tests but not with change of direction deficits in collegiate female athletes. Journal of Sports Medicine and Physical Fitness. 2024;64(8):749-757. https://doi.org/10.23736/S0022-4707.24.15691-5 (abstract, accessed 2026-10-07)
