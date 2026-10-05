# Velocity loss within a set

Last checked: 2026-10-02

## What it measures

Velocity loss is how much slower an athlete's reps get from the best rep of a set to the last rep, as a percentage of the best rep.

It serves as a sign of fatigue within the set and of how close the athlete came to failure. Failure is the point where the athlete cannot complete another rep.

Rep velocity comes from a bar speed device. This file uses these terms:

- Mean velocity: the average bar speed over the lifting part of a rep, in m/s
- Peak velocity: the highest instant of bar speed in the lifting part of a rep
- Mean propulsive velocity: the average bar speed before the bar slows faster than gravity
- 1RM: the one-repetition maximum, the heaviest load the athlete can lift once.
- Smith machine: a rack that guides the bar on fixed rails

In strength-trained men doing the bench press or squat, velocity loss was strongly correlated with peak blood lactate after exercise (correlation coefficient r = 0.93 to 0.97, where 1 is a perfect straight-line relationship). Velocity loss and loss of jump height after squat sessions were also highly correlated (r = 0.91 to 0.97) (Sánchez-Medina and González-Badillo, 2011).

These links support its use as a fatigue indicator. They do not make it a diagnosis of fatigue, overtraining, or injury risk.

Repetitions in reserve (RIR) is the number of reps the athlete could still have done before failure. Velocity loss also tracks how close a set went to failure.

In the bench press, velocity loss was closely related to the percent of possible reps completed. The link was tested at 50% to 85% of 1RM and was most similar across loads from 50% to 70% (González-Badillo et al., 2017). The abstract does not state the velocity measure or the equipment. Check the paper before you apply its equations.

A related approach uses absolute velocity, not velocity loss. The velocity at which a set stopped with 2, 4, 6, or 8 reps in reserve was similar across loads and reliable within each of four exercises: bench press, full squat, prone bench pull, and shoulder press (Morán-Navarro et al., 2019). The abstract does not state the velocity measure or the equipment.

Both findings are specific to the exercises tested. Do not apply them to another exercise without saying so.

## Formula

Calculate velocity loss as the percent drop from the reference rep to the last rep:

```text
velocity_loss_pct = (v_reference − v_last) ÷ v_reference × 100
```

Define every term in the formula:

- `v_reference`: the velocity of the reference rep, in metres per second (m/s). Use the fastest rep of the set by default.
- `v_last`: the velocity of the last completed rep of the set, in m/s
- `velocity_loss_pct`: the result, in percent (%)

Two reference variants exist:

- Fastest rep: the fastest rep in the set. Pareja-Blanco et al. (2017) define velocity loss as the percent loss from the fastest (usually first) rep to the slowest (last) rep. García-Ramos et al. (2021) recommend the fastest rep over the first rep, from 15 men in the Smith machine bench press. Use this by default.
- First rep: the first rep of the set. Use it only if the user's program or device defines velocity loss this way. It gives a smaller loss whenever a later rep is faster than the first.

When the fastest rep is not the first rep, report the first-rep loss beside the fastest-rep loss, and flag the set.

García-Ramos et al. (2021) recommend mean velocity over peak velocity for velocity loss. Weakley et al. (2021a) consider mean, mean propulsive, and peak velocity all usable. The sources differ, so name the measure. Use the same velocity measure for every rep in the set.

Published velocity loss figures come from different measures and equipment. Pareja-Blanco et al. (2017) report all velocities as mean propulsive velocity (MPV) in a Smith machine full squat. Pearson et al. (2020) used mean concentric velocity in a free-weight back squat. A figure from one does not transfer to the other without saying so.

To use velocity loss as a stopping rule during a set, calculate the stopping velocity before the set:

```text
stop_velocity_m_s = v_reference × (1 − threshold_pct ÷ 100)
```

Use these spreadsheet formulas, with one set's rep velocities in `B2:B20`, sorted by rep number, and blank cells after the last rep. The `LOOKUP(2,1/(B2:B20<>""),B2:B20)` part returns the last filled cell, so the formula works for any set length up to 19 reps:

```text
fastest rep:  =(MAX(B2:B20)-LOOKUP(2,1/(B2:B20<>""),B2:B20))/MAX(B2:B20)*100
first rep:    =(B2-LOOKUP(2,1/(B2:B20<>""),B2:B20))/B2*100
```

These work in Excel and LibreOffice. Google Sheets does not treat the `LOOKUP` part as an array on its own, so it returns the first cell instead of the last. In Google Sheets, wrap each formula in `ARRAYFORMULA`:

```text
fastest rep:  =ARRAYFORMULA((MAX(B2:B20)-LOOKUP(2,1/(B2:B20<>""),B2:B20))/MAX(B2:B20)*100)
first rep:    =ARRAYFORMULA((B2-LOOKUP(2,1/(B2:B20<>""),B2:B20))/B2*100)
```

Sort by a numeric rep column. If rep numbers are stored as text, convert them first with `=VALUE(A2)`, because text sorts "10" before "2".

Use this Python code:

```python
import pandas as pd
df["rep"] = pd.to_numeric(df["rep"])     # text rep numbers sort "10" before "2"
reps = df.sort_values("rep").groupby(["athlete_id", "date", "exercise", "set"])["mv_m_s"]
out = reps.agg(v_first="first", v_fastest="max", v_last="last", n="count")
out["vl_fastest_pct"] = (out.v_fastest - out.v_last) / out.v_fastest * 100
out["vl_first_pct"] = (out.v_first - out.v_last) / out.v_first * 100
out["fastest_not_first"] = out.v_fastest > out.v_first
out.loc[out.n < 2, ["vl_fastest_pct", "vl_first_pct"]] = float("nan")  # 1-rep sets
```

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They take the last completed rep as the highest rep number with a velocity, as the spreadsheet `LOOKUP` does, so a gap in the middle of the set is skipped. A set with fewer than 2 reps with a velocity gives a blank, as the Python version does. A rep stored as 0 m/s gives a blank and a flag, because a failed rep is not a completed rep. Leave failed reps out, or code them with a reason, and note them.

Both versions assume a `reps` table with one row per rep: `set_id` (one code per athlete, date, exercise, and set), `rep_number`, `mv_m_s`, and `status`. Show the results with one set per row.

Store `rep_number` as a whole number. Text sorts "10" before "2", so the wrong rep would count as the last one. In Power Query, set the column type to **Whole Number**. If a calculated column is needed instead, use `VALUE ( reps[rep_number_text] )`. In Tableau, change the field's data type to **Number (whole)**, or use `INT([rep_number])`.

In Power BI, use these DAX measures. They are measures because each one reads every rep in the set:

```text
Fastest rep (m/s) =
CALCULATE ( MAX ( reps[mv_m_s] ), reps[status] = "ok" )

Last rep (m/s) =
CALCULATE (
    LASTNONBLANKVALUE ( reps[rep_number], MAX ( reps[mv_m_s] ) ),
    reps[status] = "ok"
)

First rep (m/s) =
CALCULATE (
    FIRSTNONBLANKVALUE ( reps[rep_number], MAX ( reps[mv_m_s] ) ),
    reps[status] = "ok"
)

Reps at 0 m/s or below =
CALCULATE (
    COUNTROWS ( FILTER ( reps, NOT ISBLANK ( reps[mv_m_s] ) && reps[mv_m_s] <= 0 ) ),
    reps[status] = "ok"
) + 0

Velocity loss, fastest rep (%) =
VAR n = CALCULATE ( COUNT ( reps[mv_m_s] ), reps[status] = "ok" )
VAR f = [Fastest rep (m/s)]
VAR l = [Last rep (m/s)]
RETURN
    IF (
        HASONEVALUE ( reps[set_id] ) && n >= 2 && [Reps at 0 m/s or below] = 0 && f > 0,
        ( f - l ) / f * 100
    )

Velocity loss, first rep (%) =
VAR n = CALCULATE ( COUNT ( reps[mv_m_s] ), reps[status] = "ok" )
VAR v1 = [First rep (m/s)]
VAR l = [Last rep (m/s)]
RETURN
    IF (
        HASONEVALUE ( reps[set_id] ) && n >= 2 && [Reps at 0 m/s or below] = 0
            && NOT ISBLANK ( v1 ) && v1 > 0,
        ( v1 - l ) / v1 * 100
    )
```

In Tableau, put `set_id` on Rows. Use these calculations:

```text
Velocity ok (row-level):
IF [status] = "ok" THEN [mv_m_s] END

Last rep number (FIXED LOD):
{ FIXED [set_id] : MAX(IF NOT ISNULL([Velocity ok]) THEN [rep_number] END) }

First rep number (FIXED LOD):
{ FIXED [set_id] : MIN(IF NOT ISNULL([Velocity ok]) THEN [rep_number] END) }

Fastest rep (m/s) (aggregate):
MAX([Velocity ok])

Last rep (m/s) (aggregate):
MAX(IF [rep_number] = [Last rep number] THEN [Velocity ok] END)

First rep (m/s) (aggregate):
MAX(IF [rep_number] = [First rep number] THEN [Velocity ok] END)

Reps at 0 m/s or below (aggregate):
SUM(IIF([Velocity ok] <= 0, 1, 0, 0))

Velocity loss, fastest rep (%) (aggregate):
IF COUNT([Velocity ok]) < 2 OR [Reps at 0 m/s or below] > 0 THEN NULL
ELSEIF [Fastest rep (m/s)] <= 0 THEN NULL
ELSE ([Fastest rep (m/s)] - [Last rep (m/s)]) / [Fastest rep (m/s)] * 100
END

Velocity loss, first rep (%) (aggregate):
IF COUNT([Velocity ok]) < 2 OR [Reps at 0 m/s or below] > 0 OR ISNULL([First rep (m/s)]) THEN NULL
ELSEIF [First rep (m/s)] <= 0 THEN NULL
ELSE ([First rep (m/s)] - [Last rep (m/s)]) / [First rep (m/s)] * 100
END
```

When the fastest rep is not the first rep, report both losses and flag the set, as this file says.

Blanks behave this way in each tool:

- Power BI: a blank compares as 0, so `reps[mv_m_s] <= 0` alone would count blank reps as failed. The `NOT ISBLANK` test stops that. `LASTNONBLANKVALUE` skips reps with no velocity, so a gap in the set is skipped.
- Both: the first rep is the lowest rep number with a velocity, as the Python version takes the first value with `first`. The spreadsheet takes cell `B2` whether or not it holds a value.
- Tableau: a null velocity is skipped by `MAX` and `COUNT`. `IIF` returns its fourth argument, 0, for a null velocity in the count of failed reps.
- Both: a set with no reps gives a blank, where the spreadsheet gives `#N/A`.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the per-rep velocity column and its unit.
2. Convert cm/s to m/s by dividing by 100, and ft/s by multiplying by 0.3048.
3. Confirm the column is mean velocity. If it is mean propulsive or peak velocity, say so in the result.
4. Group the reps by athlete, date, exercise, and set.
5. Convert rep numbers to numbers.
6. Sort the reps within each set by rep number.
7. Check the rep count against the training log.
8. Find the reference rep. Take the fastest rep by default, or the first rep if the user asks.
9. If the fastest rep is not the first, also report the first-rep loss and flag the set.
10. Find the last completed rep. Leave out any failed rep with no recorded velocity.
11. Calculate `(v_reference − v_last) ÷ v_reference × 100`.
12. Label each result with the reference rep, the velocity measure, and the unit (%).

## Worked example

This example uses one set of 8 reps of back squat. Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Mean velocity per rep, m/s | 0.66, 0.70, 0.68, 0.65, 0.62, 0.59, 0.55, 0.53 |
| First rep | 0.66 m/s |
| Fastest rep | 0.70 m/s (rep 2) |
| Last rep | 0.53 m/s |

Follow these steps with the fastest rep as the reference:

1. Drop: 0.70 − 0.53 = 0.17 m/s.
2. Velocity loss: 0.17 ÷ 0.70 × 100 = 24.3%.

Follow these steps with the first rep as the reference:

1. Drop: 0.66 − 0.53 = 0.13 m/s.
2. Velocity loss: 0.13 ÷ 0.66 × 100 = 19.7%.

The same set is 24.3% or 19.7% depending on the reference rep. The fastest rep is rep 2, not rep 1, so report both values and flag the 4.6-point difference.

Apply a 20% velocity loss to the same reps, as an illustration of the arithmetic and not a recommendation, to get these results:

| Reference | Stopping velocity | Loss at each rep, % | Rep where 20% is first reached |
|---|---|---|---|
| Fastest rep (0.70 m/s) | 0.70 × 0.80 = 0.56 m/s | 5.7, 0.0, 2.9, 7.1, 11.4, 15.7, 21.4, 24.3 | Rep 7 |
| First rep (0.66 m/s) | 0.66 × 0.80 = 0.528 m/s | 0.0, −6.1, −3.0, 1.5, 6.1, 10.6, 16.7, 19.7 | Not reached in 8 reps |

With the fastest rep as reference, the set stops at rep 7. With the first rep, the athlete is still under 20% after rep 8.

Pearson et al. (2020) adjusted the free-weight back squat load until the fastest warm-up rep moved at 0.70 m/s (± 0.01) mean concentric velocity, then stopped sets at fixed velocities. Running the stopping formula gives the same values they report: 0.63 m/s for 10%, 0.56 m/s for 20%, and 0.49 m/s for 30% velocity loss. These show the arithmetic. They are study settings, not recommended thresholds.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Reference rep. In the worked example, the fastest rep gives 24.3% and the first rep gives 19.7% for the same set. The reference rep and velocity measure changed the number of reps performed before reaching velocity loss thresholds (García-Ramos et al., 2021).
- Velocity measure. Using peak velocity instead of mean velocity changed the number of reps performed before a velocity loss threshold was reached (García-Ramos et al., 2021).
- Denominator. Dividing by the last rep instead of the reference rep gives 32.1% instead of 24.3% for the worked example set. Always divide by the reference rep.
- Absolute or percent loss. A drop of 0.13 m/s is not 13%. Report velocity loss in percent.
- Exercise. For the same set and rep scheme, velocity loss was greater in the bench press than in the squat (Sánchez-Medina and González-Badillo, 2011). A threshold from one exercise does not transfer to another.
- Device and setup. The device and the exercise variant change the velocity values (Weakley et al., 2021a; Weakley et al., 2021b). Use the same device and setup for every set you compare.
- Effort. Ask whether every rep was lifted with maximal intent. Treating velocity loss as a fatigue sign only under maximal intent is common practice, not a cited finding.
- Rep detection. A missed or double-counted rep moves the fastest or last rep. Check reps per set against the training log. This is common practice, not a cited finding.
- A failed or partial rep. Including a failed rep as 0 m/s gives 100% loss. Leave failed reps out and note them.

## Units and typical range

Velocity loss is in percent. With the fastest-rep reference, it is 0% or more. A negative value means the last rep was faster than the reference rep, which is possible only with the first-rep reference.

| Population | Value | Source |
|---|---|---|
| Free-weight back squat, mean concentric velocity, 12 semi-professional athletes | 10%, 20%, and 30% thresholds tested for between-day reliability | Pearson et al., 2020 |
| Smith machine full squat, mean propulsive velocity, 8-week program, young men | 20% and 40% thresholds compared | Pareja-Blanco et al., 2017 |
| Smith machine full squat, mean propulsive velocity, 20% velocity loss | About half of the maximum possible reps in the set | Pareja-Blanco et al., 2017, citing Sánchez-Medina and González-Badillo, 2011 |
| Smith machine full squat, mean propulsive velocity, 40% velocity loss | Reps to failure, or nearly to failure, in most sets | Pareja-Blanco et al., 2017, citing Sánchez-Medina and González-Badillo, 2011 |
| Review authors' opinion, not a tested rule | 20% to 40% in the off-season. Below 20% in season. | Weakley et al., 2021a |

Every row is a study setting or an opinion, not a prescription. Do not repeat the last row as advice. Leave threshold choice to the coach.

The abstract of Sánchez-Medina and González-Badillo (2011) does not state the 20% and 40% figures, so cite them as Pareja-Blanco et al. (2017) citing that study.

## Data you need

Collect this data:

- Source: a bar speed device that reports a velocity for every rep, with its export
- Sampling: one velocity value per rep, using one velocity measure for the whole set
- Minimum data: one set of at least 2 reps gives one value. A trend needs several sessions with the same exercise, load, device, and reference rep.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using the first rep when it is not the fastest. In Smith machine bench press sets of more than 12 reps, the fastest mean velocity rep was the second rep (40.0% of sets) about as often as the first (37.1%) (García-Ramos et al., 2021). That study had 15 men. Use the fastest rep unless the user asks otherwise, and report the first-rep value beside it.
- Applying a threshold from another measure or equipment. Pareja-Blanco et al. (2017) used mean propulsive velocity on a Smith machine. Pearson et al. (2020) used mean concentric velocity with free weights. Name the measure and equipment behind any threshold.
- Hard-coding the last rep cell, such as `B9`. Sets differ in length. Find the last filled rep, as the spreadsheet formula above does.
- Sorting text rep numbers. Text sorts "10" before "2", so the last rep is wrong. Convert rep numbers to numbers first.
- Dividing by the last rep. The denominator is the reference rep. Dividing by the last rep inflates the loss.
- Reporting the drop in m/s as a percent. A 0.13 m/s drop on a 0.66 m/s first rep is 19.7%, not 13%.
- Using the slowest rep instead of the last rep without saying so. These are usually the same rep, but not always. Name which one you used.
- Mixing velocity measures within a set, such as mean velocity for one rep and peak velocity for another
- Comparing velocity loss across exercises. Bench press and squat lose velocity at different rates for the same rep scheme (Sánchez-Medina and González-Badillo, 2011).
- Reading a change in velocity loss between sessions as real without a noise estimate. Judge it with the typical error and noise band rules in SKILL.md (Hopkins, 2000; Swinton et al., 2018).
- Treating velocity loss across a whole session as the same metric. Loss across sets, or loss at a fixed load before and after a session, are different measures (Sánchez-Medina and González-Badillo, 2011). Name the one you report.
- Reading velocity loss as a direct count of repetitions in reserve. The published links are exercise-specific equations (González-Badillo et al., 2017; Morán-Navarro et al., 2019). Name the exercise and study behind any repetitions-in-reserve estimate.

## Example request

> Here is a CSV from our bar speed app for bench press. Each row is one rep with athlete, date, set number, rep number, load, and mean velocity. For every set, give me the velocity loss, and flag sets where it went past 25%.

## Check the result

Run these checks:

- Recalculate one set by hand: (fastest rep − last rep) ÷ fastest rep × 100.
- Confirm no value is negative with the fastest-rep reference. A negative value means the formula used the wrong rep.
- Confirm a set with only 1 rep has no velocity loss value, not 0%.

## Sources

These sources support the figures and methods in this file:

- Sánchez-Medina L, González-Badillo JJ. Velocity loss as an indicator of neuromuscular fatigue during resistance training. Med Sci Sports Exerc. 2011;43(9):1725-1734. https://doi.org/10.1249/MSS.0b013e318213f880
- Pareja-Blanco F, Rodríguez-Rosell D, Sánchez-Medina L, Sanchis-Moysi J, Dorado C, Mora-Custodio R, Yáñez-García JM, Morales-Alamo D, Pérez-Suárez I, Calbet JAL, González-Badillo JJ. Effects of velocity loss during resistance training on athletic performance, strength gains and muscle adaptations. Scand J Med Sci Sports. 2017;27(7):724-735. https://doi.org/10.1111/sms.12678
- García-Ramos A, Weakley J, Janicijevic D, Jukic I. Number of repetitions performed before and after reaching velocity loss thresholds: first repetition versus fastest repetition, mean velocity versus peak velocity. Int J Sports Physiol Perform. 2021;16(7):950-957. https://doi.org/10.1123/ijspp.2020-0629
- Pearson M, García-Ramos A, Morrison M, Ramirez-Lopez C, Dalton-Barron N, Weakley J. Velocity loss thresholds reliably control kinetic and kinematic outputs during free weight resistance training. Int J Environ Res Public Health. 2020;17(18):6509. https://doi.org/10.3390/ijerph17186509
- González-Badillo JJ, Yañez-García JM, Mora-Custodio R, Rodríguez-Rosell D. Velocity loss as a variable for monitoring resistance exercise. Int J Sports Med. 2017;38(3):217-225. https://doi.org/10.1055/s-0042-120324
- Morán-Navarro R, Martínez-Cava A, Sánchez-Medina L, Mora-Rodríguez R, González-Badillo JJ, Pallarés JG. Movement velocity as a measure of level of effort during resistance exercise. J Strength Cond Res. 2019;33(6):1496-1504. https://doi.org/10.1519/JSC.0000000000002017
- Weakley J, Mann B, Banyard H, McLaren S, Scott T, Garcia-Ramos A. Velocity-based training: from theory to application. Strength Cond J. 2021;43(2):31-49. https://doi.org/10.1519/SSC.0000000000000560 Cited as Weakley et al., 2021a.
- Weakley J, Morrison M, García-Ramos A, Johnston R, James L, Cole MH. The validity and reliability of commercially available resistance training monitoring devices: a systematic review. Sports Med. 2021;51(3):443-502. https://doi.org/10.1007/s40279-020-01382-w Cited as Weakley et al., 2021b.
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
