# Mean concentric velocity

Last checked: 2026-10-02

## What it measures

Mean concentric velocity is the average speed of the bar, or the body, during the lifting part of a rep.

The concentric phase is the lifting part, such as standing up from a squat or pressing the bar off the chest. The eccentric phase is the lowering part. This file also covers two related measures, mean propulsive velocity and peak velocity, and the load-velocity profile built from them.

## Formula

Three velocity measures are in common use. They give different numbers for the same rep:

```text
mean concentric velocity (MV)  = concentric displacement_m ÷ concentric duration_s
mean propulsive velocity (MPV) = mean of velocity from the start of the concentric phase
                                 until acceleration first drops below −9.81 m/s²
peak velocity (PV)             = highest velocity sample in the concentric phase
```

Define every term in the formula:

- `concentric displacement_m`: how far the bar travels upward during the concentric phase, in metres
- `concentric duration_s`: how long the concentric phase lasts, in seconds
- `MV`: mean concentric velocity, also written MCV, in metres per second (m/s). With samples at a fixed rate, it equals the average of the velocity samples in the concentric phase.
- `MPV`: mean propulsive velocity, in m/s. The propulsive phase ends when the bar decelerates faster than gravity (−9.81 m/s²). The part after that is the braking phase (Weakley et al., 2021a; Sanchez-Medina et al., 2010). When acceleration never drops below −9.81 m/s², the whole concentric phase is propulsive and MPV equals MV.
- `PV`: peak velocity, in m/s. The single highest instant in the concentric phase.

Prefer the device's own per-rep MV, MPV, and PV. A value you recalculate from a velocity trace depends on these conventions:

- Phase start and end: which sample starts the concentric phase, and which ends it
- Acceleration: this file uses a forward difference, `(v[i+1] − v[i]) ÷ dt`, so braking starts after sample i.
- The phase-ending sample: whether the sample immediately before braking is in the propulsive phase
- Averaging: the mean of the samples, or the time integral of velocity (displacement) divided by the phase duration

In the worked example, these choices move MV by 0.114 m/s for one rep. That is more than the published smallest detectable difference for MV. Label any recalculated value "recalculated", state the conventions, and never compare it with device values or published tables.

Use each measure for these purposes:

- Mean velocity: Weakley et al. (2021a) prefer it to estimate 1RM, the one-repetition maximum, which is the heaviest load the athlete can lift once. It is more reliable than MPV with light loads, varies less between devices than PV, and gives a more linear load-velocity relationship (Weakley et al., 2021a). Weakley et al. (2021a) consider all three measures usable for velocity loss and for feedback during training.
- Mean propulsive velocity: use it when the user's device or published table reports MPV. Above about 70% of 1RM, MV and MPV give virtually the same information (Weakley et al., 2021a). In the bench press, the braking phase disappeared at 76.1 ± 7.4% of 1RM (Sanchez-Medina et al., 2010).
- Peak velocity: Weakley et al. (2021a) recommend it for testing ballistic lifts, such as a jump or a bench press throw, where the bar or body leaves contact, because MV and MPV include the flight phase. García-Ramos et al. (2018) found the opposite for relative load in the Smith machine bench press throw: MV predicted percent of 1RM best, with a standard error of the estimate of 3.80% to 4.76% of 1RM, while PV was the most repeatable. The sources conflict. Ask which measure the user's program uses, and do not present either one as the rule.

A load-velocity profile is a straight line fitted through each athlete's velocity at several loads in one exercise. Use these formulas for the line and the 1RM estimate:

```text
velocity_m_s = intercept + slope × load_kg
estimated_1rm_kg = (v1rm_m_s − intercept) ÷ slope
```

Define every term in these formulas:

- `load_kg`: the load lifted, in kilograms. Percent of 1RM also works.
- `slope`: change in velocity per kilogram, in m/s per kg. It is negative.
- `intercept`: the velocity the line predicts at zero load, in m/s
- `v1rm_m_s`: the velocity at 1RM, also called the minimum velocity threshold. It is the mean velocity of a successful 1RM lift, in m/s.

Weakley et al. (2021a) describe the individual profile: record mean velocity at about 5 submaximal loads, fit a linear regression, and read off the load at the 1RM velocity. A 2-point method at about 45% and 85% of 1RM is a shorter option. Weakley et al. (2021a) report it confirmed only for the bench pull, bench press, lat pull-down, and seated cable row.

Estimate 1RM from velocity only for a lift with both a published 1RM velocity and a published validation. Weakley et al. (2021a) report accurate estimates only during some upper-body exercises, and state that velocity recordings cannot give an accurate 1RM estimate in lower-body lifts such as the squat or deadlift.

In this file, that leaves the bench press and the prone bench pull. Name the equipment behind the 1RM velocity you use. A squat profile can still describe velocity at each load, but do not report a squat 1RM from it.

Use these spreadsheet formulas, with load in `A2:A6`, mean velocity in `B2:B6`, and the 1RM velocity in `D1`:

```text
slope:          =SLOPE(B2:B6,A2:A6)
intercept:      =INTERCEPT(B2:B6,A2:A6)
estimated 1RM:  =(D1-INTERCEPT(B2:B6,A2:A6))/SLOPE(B2:B6,A2:A6)
```

Use this Python code for a Smith machine bench press profile:

```python
import numpy as np
load_kg = np.array([40, 50, 60, 70, 80])
mv = np.array([1.01, 0.84, 0.70, 0.56, 0.39])   # fastest rep at each load
slope, intercept = np.polyfit(load_kg, mv, 1)
v1rm = 0.17                                      # ask the user; see the table below
est_1rm = (v1rm - intercept) / slope
```

### Calculate it in Power BI and Tableau

These versions use only points with both a load and a velocity. The slope and intercept are blank with fewer than 2 different loads. The 1RM estimate is blank when the slope is 0 or above, or when the 1RM velocity is missing. A flat or rising line has no 1RM. Estimate 1RM only for a lift with a published 1RM velocity and a published validation, as this file says.

Both versions assume a `lv_points` table with one row per athlete, date, exercise, and load: `athlete_id`, `measure_date`, `exercise`, `load_kg`, and `mv_m_s`, the mean velocity of the fastest rep at that load. The 1RM velocity comes from the user, in an `exercises` table column `v1rm_m_s` or in a parameter. Show the results with one athlete, date, and exercise per row. In Power BI, relate `exercises[exercise]` to `lv_points[exercise]`, one to many, single direction, and put `exercises[exercise]` in the visual.

In Power BI, use these DAX measures. They are measures because each one fits a line through several rows:

```text
LV slope (m/s per kg) =
VAR pts = FILTER ( lv_points, NOT ISBLANK ( lv_points[load_kg] ) && NOT ISBLANK ( lv_points[mv_m_s] ) )
VAR loads = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( pts, "@load", lv_points[load_kg] ) ) ) + 0
RETURN
    IF ( loads >= 2, ROUND ( MAXX ( LINESTX ( pts, lv_points[mv_m_s], lv_points[load_kg] ), [Slope1] ), 9 ) )

LV intercept (m/s) =
VAR pts = FILTER ( lv_points, NOT ISBLANK ( lv_points[load_kg] ) && NOT ISBLANK ( lv_points[mv_m_s] ) )
VAR loads = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( pts, "@load", lv_points[load_kg] ) ) ) + 0
RETURN
    IF ( loads >= 2, MAXX ( LINESTX ( pts, lv_points[mv_m_s], lv_points[load_kg] ), [Intercept] ) )

Estimated 1RM (kg) =
VAR s = [LV slope (m/s per kg)]
VAR i = [LV intercept (m/s)]
VAR v = SELECTEDVALUE ( exercises[v1rm_m_s] )
RETURN IF ( NOT ISBLANK ( s ) && s < 0 && NOT ISBLANK ( v ), ( v - i ) / s )
```

In Tableau, put `athlete_id`, `measure_date`, and `exercise` on the view. Make a parameter `1RM velocity (m/s)`. Use these calculations. They build the least-squares line from sums, which Tableau aggregates over non-null values:

```text
Load in pair (row-level):
IF NOT ISNULL([mv_m_s]) THEN [load_kg] END

Velocity in pair (row-level):
IF NOT ISNULL([load_kg]) THEN [mv_m_s] END

LV slope (m/s per kg) (aggregate):
IF COUNTD([Load in pair]) < 2 THEN NULL
ELSE ROUND(
     (COUNT([Load in pair]) * SUM([Load in pair] * [Velocity in pair]) - SUM([Load in pair]) * SUM([Velocity in pair]))
   / (COUNT([Load in pair]) * SUM([Load in pair] * [Load in pair]) - SUM([Load in pair]) * SUM([Load in pair])), 9)
END

LV intercept (m/s) (aggregate):
IF ISNULL([LV slope (m/s per kg)]) THEN NULL
ELSE (SUM([Velocity in pair]) - [LV slope (m/s per kg)] * SUM([Load in pair])) / COUNT([Load in pair])
END

Estimated 1RM (kg) (aggregate):
IF ISNULL([LV slope (m/s per kg)]) OR [LV slope (m/s per kg)] >= 0 THEN NULL
ELSE ([1RM velocity (m/s)] - [LV intercept (m/s)]) / [LV slope (m/s per kg)]
END
```

Both slopes are rounded to 9 decimals, so rounding error in a flat profile reads as 0, not as a tiny negative slope that gives a huge 1RM. To check the slope and intercept, add a linear trend line to a scatter plot of the same points and compare with **Describe Trend Model**.

Blanks behave this way in each tool:

- Power BI: rows with a blank load or velocity are filtered out before the fit. With fewer than 2 different loads, the measures return a blank, where the spreadsheet gives `#DIV/0!`.
- Tableau: the two pair fields are null unless both values exist, so `SUM`, `COUNT`, and `COUNTD` use the same points. A null slope gives a null 1RM.
- Both: a slope of 0 gives a blank 1RM, where the spreadsheet gives `#DIV/0!`.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the velocity columns and their units.
2. Convert cm/s to m/s by dividing by 100, and ft/s by multiplying by 0.3048.
3. Identify which measure each column holds: mean velocity, mean propulsive velocity, or peak velocity.
4. Use the device's per-rep values if they exist. Recalculate only if the user has a velocity-time trace and no per-rep values.
5. To recalculate, find the start and end of the concentric phase. A common practice, not a published rule, is to start when upward velocity begins and end when it returns to zero.
6. State the rule you used for the start and end of the concentric phase.
7. For mean velocity, divide the concentric displacement in metres by the concentric duration in seconds.
8. State whether you used the sample mean or the time integral.
9. For mean propulsive velocity, calculate acceleration between samples with a forward difference.
10. Find the first value below −9.81 m/s². If no value drops below −9.81 m/s², MPV equals MV.
11. Average the velocity samples up to and including the sample before that first value.
12. For peak velocity, take the highest velocity sample in the concentric phase.
13. For a load-velocity profile, keep the fastest rep at each load.
14. Fit a straight line of velocity against load for each athlete, exercise, and equipment.
15. To estimate 1RM, confirm the lift has a published 1RM velocity and validation. Do not estimate 1RM for the squat or deadlift.
16. Ask which 1RM velocity to use.
17. Solve the line for the load at that velocity.
18. Label every result with the measure, the device, the exercise variant, the equipment, and the units.
19. Label recalculated values "recalculated".

## Worked example

This example uses one back squat rep recorded at 20 Hz (20 samples per second, one every 0.05 s), and one athlete's Smith machine bench press load-velocity profile. Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Concentric velocity samples, m/s | 0.10, 0.35, 0.60, 0.80, 0.95, 1.05, 1.12, 1.16, 1.18, 1.15, 1.05, 0.55, 0.05 |
| Sampling rate | 20 Hz, so 0.05 s per sample |
| Smith machine bench press profile loads, kg | 40, 50, 60, 70, 80 |
| Fastest-rep mean velocity at each load, m/s | 1.01, 0.84, 0.70, 0.56, 0.39 |

Follow these steps for the single rep, treating each sample as one 0.05 s time step:

1. Concentric duration: 13 samples × 0.05 s = 0.65 s.
2. Displacement: sum of velocities 10.11 m/s × 0.05 s = 0.5055 m.
3. Mean concentric velocity: 0.5055 m ÷ 0.65 s = 0.778 m/s.
4. Peak velocity: 1.18 m/s.
5. Acceleration between samples, m/s²: 5.0, 5.0, 4.0, 3.0, 2.0, 1.4, 0.8, 0.4, −0.6, −2.0, −10.0, −10.0.
6. The first value below −9.81 m/s² comes after sample 11. The propulsive phase is samples 1 to 11, lasting 0.55 s, with a velocity sum of 9.51 m/s.
7. Mean propulsive velocity: 9.51 ÷ 11 = 0.865 m/s.

The same rep is 0.778 m/s (MV), 0.865 m/s (MPV), or 1.18 m/s (PV).

Recalculate the same 13 samples with other conventions to get these results:

| Convention | MV, m/s | MPV, m/s |
|---|---|---|
| Each sample counts as one 0.05 s step (sample mean), sample 11 in the propulsive phase | 0.778 | 0.865 |
| Same, sample 11 left out of the propulsive phase | 0.778 | 0.846 |
| Time integral by trapezoid, first to last sample | 0.836 | 0.894 |
| Zero-velocity sample added at each end, trapezoid from zero to zero | 0.722 | 0.817 |

The MV values span 0.114 m/s for one rep. The rep did not change. This spread is larger than the smallest detectable difference of 0.06 to 0.08 m/s in the table below. In a second trace that slows more gently, acceleration never drops below −9.81 m/s², so MPV equals MV (0.747 m/s).

Follow these steps for the bench press profile:

1. Fit the line: velocity = 1.612 − 0.0152 × load, with a correlation of −0.9992.
2. Estimate 1RM with the group 1RM velocity of 0.17 m/s: (0.17 − 1.612) ÷ −0.0152 = 94.9 kg.
3. Check the loads: 40 kg is 42.2% and 80 kg is 84.3% of that estimate, close to the 45% and 85% the 2-point method uses. The heaviest load is 14.9 kg below the estimate.
4. Estimate 1RM with a 1RM velocity of 0.10 m/s, the free-weight bench press value in the table below: 99.5 kg.
5. Use only the 40 kg and 80 kg points (2-point method): the line is velocity = 1.63 − 0.0155 × load, and the estimate at 0.17 m/s is 94.2 kg.

The same five lifts give estimates 4.6 kg apart, depending only on which 1RM velocity you choose.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Velocity measure. In the worked example, one rep is 0.778, 0.865, or 1.18 m/s depending on the measure. Never compare MV with MPV or PV.
- Calculation conventions. In the worked example, recalculated MV ranges from 0.722 to 0.836 m/s for one rep. Never compare recalculated values with device values.
- Load. In the bench press, the braking phase was present at lighter loads and disappeared near 76% of 1RM, so MV and MPV differ most at light loads (Sanchez-Medina et al., 2010).
- Device. Linear position transducers, which measure bar movement through a cable attached to the bar, showed greater accuracy and reliability than other device types in a systematic review (Weakley et al., 2021b). The relationship between velocity and percent of 1RM also depends on the device (Weakley et al., 2021a).
- Exercise and technique. The load-velocity relationship differs by exercise, by technique, and by sex (Weakley et al., 2021a). Technique includes concentric-only lifts, which start from a dead stop, and eccentric-concentric lifts, which lower the bar first. A Smith machine squat profile does not apply to a free-weight squat. A Smith machine guides the bar on fixed rails.
- Range of motion. Partial reps move the bar a shorter distance and change velocity. Keep depth and range the same. This is common practice, not a cited finding.
- 1RM velocity. In the worked example, 0.17 m/s and 0.10 m/s give bench press estimates 4.6 kg apart. The individual 1RM velocity in the free-weight back squat was unreliable between days, with a coefficient of variation (day-to-day variation as a percentage of the mean) of 22.5% (Banyard et al., 2017).
- Which rep at each load. Weakley et al. (2021a) record the fastest rep at each load. Using the first or the average rep gives a different line.
- Effort. Ask whether athletes were cued to lift as fast as possible. Comparing velocity only across reps lifted with maximal intent is common practice, not a cited finding.
- Rep detection. A device can miss a rep or count one rep twice. Check the rep count per set against the training log. This is common practice, not a cited finding.

## Units and typical range

Velocity is in metres per second (m/s). The first rows give velocity at 1RM, the slowest end of the profile. The last rows give target velocities and measurement error.

| Population | Value | Source |
|---|---|---|
| Smith machine bench press, velocity at 1RM in a study built on mean propulsive velocity, 120 trained men | 0.16 ± 0.04 m/s (mean ± standard deviation). Weakley et al. (2021a) list it as MPV on a Smith machine. | González-Badillo and Sánchez-Medina, 2010 |
| Bench press, mean velocity at 1RM, across 4 studies | 0.10 to 0.17 m/s, with 0.17 m/s suggested as a group value. Three studies used a Smith machine. The one free-weight study gave 0.10 m/s. | Weakley et al., 2021a |
| Squat, mean velocity at 1RM, across 4 studies (2 Smith machine, 2 free-weight) | 0.23 to 0.32 m/s, with 0.30 m/s suggested as a group value. The free-weight studies gave the lower values (0.23 and 0.24 m/s). | Weakley et al., 2021a |
| Free-weight back squat, mean velocity at 1RM, 17 trained men | 0.24 ± 0.06 m/s, coefficient of variation 22.5% between days | Banyard et al., 2017 |
| Deadlift, mean velocity at 1RM, 3 studies listed, 2 reporting values | 0.14 to 0.16 m/s, with 0.15 m/s suggested as a group value. Equipment not stated here. No validated 1RM estimate. | Weakley et al., 2021a |
| Prone bench pull, mean velocity at 1RM, across 3 studies | 0.48 to 0.52 m/s, with 0.50 m/s suggested as a group value. Equipment not stated here. Ask before you apply it. | Weakley et al., 2021a |
| Smith machine full squat, target mean propulsive velocity of the first rep, young men | 0.82 m/s at about 70%, 0.75 at about 75%, 0.68 at about 80%, 0.60 at about 85% of 1RM | Pareja-Blanco et al., 2017 |
| Between-day variation at a given percent of 1RM, Smith machine bench press throw, 30 men | PV 3.50% to 3.87%, MV 4.05% to 4.93%, MPV 5.11% to 6.03% (coefficient of variation) | García-Ramos et al., 2018 |
| Smallest detectable difference, free-weight back squat | MV 0.06 to 0.08 m/s. PV 0.11 to 0.19 m/s. MPV 0.08 to 0.11 m/s. | Weakley et al., 2021a |

The coefficient of variation is the typical day-to-day variation expressed as a percentage of the mean. A lower value means a more repeatable measure. The smallest detectable difference is a study value: the smallest change that exceeded measurement noise in that study's sample. It is not a rule for flagging one athlete's change.

The smallest detectable difference applies only to the same exercise, equipment, device, and velocity measure. For your own athletes, judge a change with the typical error and noise band rules in SKILL.md (Hopkins, 2000; Swinton et al., 2018).

García-Ramos et al. (2018) found PV the most repeatable but MV the best for estimating relative load in a bench press throw on a Smith machine.

## Data you need

Collect this data:

- Source: a bar speed device, such as a linear position transducer, an accelerometer, or a camera system, with its export
- Sampling: per-rep values from the device, or a velocity-time trace if you need to calculate MV, MPV, or PV yourself. Record the device and sampling rate.
- Minimum data: one rep gives one value. A load-velocity profile needs at least 2 loads with the 2-point method, and about 5 loads with the standard method (Weakley et al., 2021a). A trend at a fixed load needs several sessions with the same exercise, device, and setup.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing velocity measures. An app may export MV, MPV, and PV side by side. Comparing an athlete's MPV from one session with their MV from another session shows a false change. Confirm the column before any calculation.
- Using a published velocity table from another measure or exercise. A table built from MPV in a Smith machine squat does not apply to MV in a free-weight squat (Weakley et al., 2021a). Name the measure, exercise, and device behind any table.
- Using cm/s or ft/s as m/s. A value of 78 is cm/s, not m/s. A value of 2.6 may be ft/s, which is 0.79 m/s. Convert first: cm/s ÷ 100, ft/s × 0.3048.
- Comparing recalculated values with device values or published tables. Phase rules and averaging change MV by more than its smallest detectable difference. Label recalculated values and keep them in their own trend.
- Trusting the device's rep count. A missed or double-counted rep changes the fastest and last reps. Check reps per set against the training log.
- Averaging all reps in a set and calling it the athlete's velocity at that load. For a load-velocity profile, use the fastest rep at each load (Weakley et al., 2021a).
- Fitting one profile across exercises, devices, or variants. Fit each athlete, exercise, and device separately.
- Presenting an estimated 1RM as measured. Show it as an estimate with its 1RM velocity.
- Estimating a squat or deadlift 1RM from velocity. All predicted 1RM values differed from the measured 1RM in the free-weight back squat (Banyard et al., 2017), and velocity cannot give an accurate 1RM in lower-body lifts (Weakley et al., 2021a). Decline, and explain why.
- Using a Smith machine 1RM velocity for a free-weight lift. Most bench press values come from Smith machine studies. Name the equipment behind the value you use.
- Extrapolating far beyond the loads tested. A line fitted from 30 to 40 kg says little about 90 kg. Say how far beyond the heaviest load the estimate reaches.
- Stating one measure as the rule for a jump or throw. Weakley et al. (2021a) recommend peak velocity for ballistic lifts, but García-Ramos et al. (2018) found mean velocity best for relative load in the Smith machine bench press throw. Name the measure, and say the sources differ.
- Reading a small change as real, or using the SD of the athlete's own sessions as noise. Use a typical error from a short-term test-retest with the same exercise, equipment, device, and measure, and the noise band rules in SKILL.md. The band for two single values is about 2.77 × the typical error.

## Example request

> I have an export from our bar speed device for bench press. Each row is one rep with athlete, date, load in kg, mean velocity, and peak velocity. Build each athlete's load-velocity profile from Monday's warm-up sets and estimate their bench press 1RM.

## Check the result

Run these checks:

- Confirm mean velocity is lower than peak velocity for every rep.
- Confirm the load-velocity slope is negative. Heavier loads must move slower.
- Recalculate one estimate by hand: (1RM velocity − intercept) ÷ slope. Confirm the 1RM velocity and its source are named.

## Sources

These sources support the figures and methods in this file:

- Weakley J, Mann B, Banyard H, McLaren S, Scott T, Garcia-Ramos A. Velocity-based training: from theory to application. Strength Cond J. 2021;43(2):31-49. https://doi.org/10.1519/SSC.0000000000000560 Cited as Weakley et al., 2021a.
- Sanchez-Medina L, Perez CE, Gonzalez-Badillo JJ. Importance of the propulsive phase in strength assessment. Int J Sports Med. 2010;31(2):123-129. https://doi.org/10.1055/s-0029-1242815
- González-Badillo JJ, Sánchez-Medina L. Movement velocity as a measure of loading intensity in resistance training. Int J Sports Med. 2010;31(5):347-352. https://doi.org/10.1055/s-0030-1248333
- García-Ramos A, Pestaña-Melero FL, Pérez-Castilla A, Rojas FJ, Haff GG. Mean velocity vs. mean propulsive velocity vs. peak velocity: which variable determines bench press relative load with higher reliability? J Strength Cond Res. 2018;32(5):1273-1279. https://doi.org/10.1519/JSC.0000000000001998
- Banyard HG, Nosaka K, Haff GG. Reliability and validity of the load-velocity relationship to predict the 1RM back squat. J Strength Cond Res. 2017;31(7):1897-1904. https://doi.org/10.1519/JSC.0000000000001657
- Weakley J, Morrison M, García-Ramos A, Johnston R, James L, Cole MH. The validity and reliability of commercially available resistance training monitoring devices: a systematic review. Sports Med. 2021;51(3):443-502. https://doi.org/10.1007/s40279-020-01382-w Cited as Weakley et al., 2021b.
- Pareja-Blanco F, Rodríguez-Rosell D, Sánchez-Medina L, Sanchis-Moysi J, Dorado C, Mora-Custodio R, Yáñez-García JM, Morales-Alamo D, Pérez-Suárez I, Calbet JAL, González-Badillo JJ. Effects of velocity loss during resistance training on athletic performance, strength gains and muscle adaptations. Scand J Med Sci Sports. 2017;27(7):724-735. https://doi.org/10.1111/sms.12678
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
