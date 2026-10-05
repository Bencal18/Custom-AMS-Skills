# Countermovement jump height

Last checked: 2026-10-02

## What it measures

Countermovement jump (CMJ) height is how high the athlete's center of mass rises after takeoff in a vertical jump that starts from standing with a quick dip before the push.

## Formula

Three methods exist. They give different numbers from the same jump, so never mix them in one table, trend, or comparison:

- Takeoff velocity method, also called the impulse-momentum method. Use it when you have the raw force-time trace. It is the recommended method (Linthorne, 2001; McMahon et al., 2018a).
- Flight time method. Use it only when flight time is all you have, for example from a contact mat or a summary export. It assumes the athlete lands in the same body position as at takeoff.
- Work-energy method, which uses the force-displacement curve. Some exports call it impulse-displacement. It integrates twice to get displacement, so errors compound, and it is often the least reliable of the three (Linthorne, 2001). Do not use it unless the user asks, and never mix it with the other two.

Use these equations for the takeoff velocity method:

```text
body weight (N)         = mean vertical force during quiet standing
body mass (kg)          = body weight / 9.81
acceleration (m/s^2)    = (vertical force - body weight) / body mass, at each sample
velocity (m/s)          = running integral of acceleration over time, up to takeoff
jump height (m)         = takeoff velocity^2 / (2 x 9.81)
```

Use this equation for the flight time method:

```text
jump height (m) = 9.81 x flight time^2 / 8
```

Define every term in the formula:

- `9.81`: acceleration due to gravity, in m/s²
- `vertical force`: the force the plate measures, in newtons (N). Sum both plates when the athlete stands on two.
- `quiet standing`: the still period before the jump starts. Use at least 1 s (McMahon et al., 2018a).
- `standard deviation`: how much the force values spread around their mean. A still athlete gives a small standard deviation.
- `onset of movement`: the first instant force drops below body weight by more than 5 standard deviations of the quiet standing force. Some protocols step back 30 ms from that instant (Owen et al., 2014; McMahon et al., 2018a).
- `takeoff`: the instant force falls below a set threshold. One published threshold is 5 standard deviations of the unloaded plate force, taken over 300 ms of the flight phase (McMahon et al., 2018a).
- `takeoff velocity`: vertical velocity of the center of mass at takeoff, in m/s
- `flight time`: time from takeoff to touchdown, in seconds
- `running integral`: add up acceleration × time step, sample by sample. Use the trapezoid rule, which averages each pair of neighboring samples before multiplying by the time step (McMahon et al., 2018a).

These points explain why the two methods differ:

- Athletes usually land with ankles, knees, and hips more bent than at takeoff. The center of mass is 1 to 4 cm lower at landing, so flight time is longer. With hands on hips, the flight time method overestimates height by 0.5 to 2 cm. Arm swing makes the gap larger (Linthorne, 2001).
- The takeoff velocity method depends on body weight. A 10 N error in body weight gives a 2 to 3 cm error in jump height (Linthorne, 2001).
- The takeoff velocity method also depends on finding takeoff. A 3 ms error in takeoff gives about a 0.9 cm error in jump height (McMahon et al., 2018a).

Use this spreadsheet formula for the flight time method, with flight time in seconds in `B2`. It returns a blank when `B2` is blank or not a number, instead of a jump height of 0:

```text
=IF(ISNUMBER(B2),9.81*B2^2/8,"")
```

Use this Python sketch for the takeoff velocity method:

```python
import numpy as np

def cmj_height_takeoff_velocity(force_n, fs_hz, takeoff_index, quiet_s=1.0, g=9.81):
    """force_n: summed vertical force in N, starting with quiet standing.
    takeoff_index: sample where force first falls below your takeoff threshold."""
    n_quiet = int(quiet_s * fs_hz)
    body_weight = force_n[:n_quiet].mean()
    mass = body_weight / g
    acc = (force_n[:takeoff_index] - body_weight) / mass
    vel = np.concatenate([[0.0], np.cumsum((acc[1:] + acc[:-1]) / 2) / fs_hz])
    return vel[-1] ** 2 / (2 * g)  # jump height in m
```

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They use the flight time method only. They return a blank, not 0 m, when flight time is missing, and they read only flight times stored in seconds.

Both versions assume one row per athlete, date, session, measure, and trial in a `measures` table, with flight time stored as `measure_name` `cmj_flight_time` and `unit` `s`. Convert milliseconds to seconds on import. A value in ms inside this formula gives a height about a million times too large.

In Power BI, use this DAX measure. It is a measure, not a calculated column, because the `value` column holds many measures, and one row cannot hold both the input and the result:

```text
CMJ height, flight time (m) =
VAR ft =
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "cmj_flight_time",
        measures[unit] = "s",
        measures[status] = "ok"
    )
RETURN
    IF ( NOT ISBLANK ( ft ) && ft > 0, 9.81 * ft * ft / 8 )
```

Put `trial_number` in the visual to see each trial. Without it, the measure returns the height of the longest flight that day, which is the best trial.

In Tableau, use this row-level calculation, then aggregate it with `MAX` for the best trial or show it with `trial_number` on the view:

```text
CMJ height, flight time (m):
IF [measure_name] = "cmj_flight_time" AND [unit] = "s" AND [status] = "ok" AND [value] > 0
THEN 9.81 * POWER([value], 2) / 8
END
```

Blanks behave this way in each tool:

- Power BI: a missing flight time gives a blank `ft`, and the `IF` returns blank. A flight time of 0 s, which no real jump gives, also returns blank. Check those rows.
- Tableau: a null `value` makes the test null. The `IF` has no `ELSE`, so it returns null. `MAX` ignores the null.

## Calculate the metric

Follow these steps to calculate jump height with the takeoff velocity method from a raw trace:

1. Load the vertical force column in N and the time column in s. If the export has one column per plate, add them into one `force_n` column.
2. Confirm the sampling rate from the time step. A step of 0.001 s means 1000 Hz.
3. In the first 1 s of the trace, while the athlete stands still, calculate the mean as `body_weight_n` and the standard deviation as `bw_sd_n`.
4. Divide `body_weight_n` by 9.81 to get `body_mass_kg`.
5. Find the onset of movement: the first sample where `force_n` is below `body_weight_n - 5 × bw_sd_n`. You need it for time to takeoff and to confirm the athlete was still before it.
6. Find takeoff: the first sample after the push where `force_n` falls below your takeoff threshold.
7. For every sample up to takeoff, calculate `net_force_n = force_n - body_weight_n`.
8. Multiply each `net_force_n` by the time step and add them up, from the first sample of quiet standing to takeoff, to get the net impulse in N·s. Use the trapezoid rule on real traces (McMahon et al., 2018a).
9. Divide the net impulse by `body_mass_kg` to get takeoff velocity in m/s.
10. Calculate jump height as takeoff velocity² / (2 × 9.81), in m.

Notes on the integration step: Starting at the beginning of a still quiet period has no meaningful effect on jump height when body weight is correct (McMahon et al., 2018a). When body weight is the mean of the window where integration starts, that window adds zero net impulse. In the worked example, integrating from the onset of movement instead gives the same 2.3713 m/s.

Follow these steps for the flight time method:

1. Find takeoff as in step 6 above.
2. Find touchdown: the first sample after takeoff where `force_n` rises above the same threshold.
3. Subtract the takeoff time from the touchdown time to get flight time in s.
4. Calculate jump height as 9.81 × flight time² / 8, in m.

## Worked example

This example uses a simplified synthetic jump sampled at 1000 Hz. Force is held constant inside each phase so you can follow it by hand.

| Input | Value |
|---|---|
| Quiet standing | 1.000 s (1000 samples), alternating 784 N and 786 N |
| Dip (unweighting) | 0.250 s (250 samples) at 400 N |
| Push (braking and propulsion) | 0.400 s (400 samples) at 1500 N |
| Landing | Center of mass 0.02 m lower than at takeoff |

Step 1. Calculate body weight and body mass:

- Mean quiet force = 785.00 N. Standard deviation = 1.0005 N.
- Body mass = 785.00 / 9.81 = 80.0204 kg.

Step 2. Find the onset of movement:

- Threshold = 785.00 - 5 × 1.0005 = 780.00 N.
- Force first drops below 780.00 N at sample 1000, which is 1.000 s.

Step 3. Calculate the net impulse, phase by phase:

- Dip: (400 - 785.00) × 0.250 = -96.25 N·s.
- Push: (1500 - 785.00) × 0.400 = 286.00 N·s.
- Total net impulse = -96.25 + 286.00 = 189.75 N·s.

Step 4. Calculate takeoff velocity and jump height:

- Takeoff velocity = 189.75 / 80.0204 = 2.3713 m/s.
- Jump height = 2.3713² / (2 × 9.81) = 0.2866 m.
- Summing all 1650 samples at 1 ms each gives the same values, 2.3713 m/s and 0.2866 m.
- The trapezoid rule on this step-shaped trace gives 2.3668 m/s and 0.2855 m, because it treats the last contact sample differently. On real traces, force falls smoothly to zero at takeoff.

Step 5. Apply the flight time method to the same jump:

- If the athlete landed in the takeoff posture, flight time would be 0.4834 s, which gives 0.2866 m. The two methods would agree.
- The athlete lands with the center of mass 0.02 m lower, so flight time is 0.4917 s.
- Jump height from flight time = 9.81 × 0.4917² / 8 = 0.2965 m.

Result: the takeoff velocity method gives 0.2866 m. The flight time method gives 0.2965 m for the same jump, 0.99 cm higher. This matches the 0.5 to 2 cm gap that Linthorne (2001) reports for jumps with hands on hips.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Method. Flight time reads higher than takeoff velocity when the athlete lands with bent joints. In the worked example the gap is 0.99 cm.
- Body weight. This error happens only when body weight comes from somewhere other than the quiet period you integrate, such as a scale or another trial. A body weight error is then added to every sample you integrate, so the error grows with the length of the integration.
- Size of a body weight error. In the worked example, a body weight 10 N too high gives 0.2329 m instead of 0.2866 m when you integrate from the start of quiet standing. It gives 0.2606 m when you integrate from the onset of movement. A body weight 10 N too low gives 0.3474 m and 0.3145 m. Linthorne (2001) reports a 2 to 3 cm error for a 10 N body weight error.
- Weighing window. Shorter or noisier quiet periods give a less accurate body weight. Use at least 1 s (McMahon et al., 2018a).
- Takeoff threshold. A 3 ms error in finding takeoff changes jump height by about 0.9 cm (McMahon et al., 2018a).
- Filtering. Filtered force data can underestimate CMJ height (McMahon et al., 2018a).
- Sampling and integration rate. Use at least 1000 Hz (McMahon et al., 2018a).
- Arm swing. Arm swing raises jump height and makes the flight time error larger (Linthorne, 2001). In 18 men it raised takeoff velocity by 10% and the rise after takeoff by 21% (Harman et al., 1990). In elite volleyball players the gain in height was 38% (Vaverka et al., 2016). Keep the same arm condition at every test.
- Trial selection. The best trial and the mean of trials give different values.

## Units and typical range

Report jump height in meters or centimeters. Name the method and whether arm swing was allowed.

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I men (n = 76), no arm swing (light bar across the shoulders), flight time method, mean of 2 trials | 0.36 ± 0.07 m (mean ± SD) | Sole et al., 2018 |
| NCAA Division I women (n = 75), no arm swing (light bar across the shoulders), flight time method, mean of 2 trials | 0.27 ± 0.06 m (mean ± SD) | Sole et al., 2018 |
| Professional male rugby league (n = 53), no arm swing (hands on hips), takeoff velocity method, mean of 3 trials | 0.35 ± 0.04 m (mean ± SD); lowest and highest RSI-modified groups (n = 20 each) 0.318 ± 0.032 m and 0.377 ± 0.039 m | McMahon et al., 2018b |

Use these ranges to check that data are plausible, not to rate athletes.

No takeoff velocity range is given, because jump height = takeoff velocity² / (2 × 9.81) carries the same information. If an export gives only takeoff velocity, convert it to height. Do not use peak velocity in its place. Velocity peaks about 0.03 s before takeoff and is 6 to 7% lower at takeoff (Harman et al., 1990), so peak velocity overstates height by about 13 to 16%.

Use this test variability from a retest on a separate day to judge a change in one athlete:

| Population and protocol | Typical error | Source |
|---|---|---|
| Elite male ice hockey players (n = 22), takeoff velocity method, hands on hips, best of 3 trials, retest 24 h later | 1.3 cm, coefficient of variation 3.1% | Godhe et al., 2025 |
| Adolescent cricket and netball athletes (n = 17), flight time method, hands on hips, mean of 3 trials, retest 1 week later | Coefficient of variation 2.63% | Thomas et al., 2017 |

These retests were on separate days, so they count day-to-day variation as noise and give a larger typical error than a same-day retest. Use them only when your method, trial summary, and athletes match. Otherwise, measure your own typical error from a short-term retest in which no true change is expected. Judge a change with the noise band, 1.96 × TE × √(1 + 1/n) for a baseline mean of n tests, as the `force-plate` skill describes.

## Data you need

Collect this data:

- Source: a force plate. For the takeoff velocity method you need the raw vertical force trace, not only the summary export.
- Sampling: at least 1000 Hz. Use unfiltered data, because filtering can underestimate CMJ height (McMahon et al., 2018a).
- Plate setup: zero the plate before each trial. McMahon et al. (2018a) call this essential to reduce signal noise.
- Minimum data: at least 1 s of still standing before each jump (McMahon et al., 2018a). Collect about three trials per session so you can estimate trial-to-trial variation (Bishop et al., 2018).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing methods. A flight time value and a takeoff velocity value are not comparable. Name the method in every column header and keep one method per trend.
- Using the wrong flight time formula, such as `g × t² / 2` or `g × t / 2`. Use `g × t² / 8`.
- Using flight time in milliseconds inside a formula that expects seconds. Convert first.
- Mixing centimeters, meters, and inches in one column. Convert everything to one unit before any calculation.
- Using a scale weight or an earlier body mass in the takeoff velocity method. Use the quiet standing force from the same trial. A device's test-level body weight field may have an unknown unit and source. Check the device file before you use it.
- Keeping a trial where the athlete moved during quiet standing. The velocity calculation assumes the athlete starts still. Flag the trial instead.
- Integrating total force without subtracting body weight. Subtract body weight first, then divide by body mass.
- Filtering or smoothing the force trace before integration. Use the raw trace, unless the plate is known to need filtering. Some plates register rapid changes in force poorly, and their data may need digital filtering (McMahon et al., 2018a). Then state the filter type and cutoff.
- Mixing jump heights from different takeoff thresholds. Thresholds of 6 N and 10 N above true zero overestimated jump height by 1% and 1.5% (McMahon et al., 2018a). Use one threshold and state it.
- Judging a change against the trial-to-trial variation within one session. Use the noise band with a typical error from repeated tests.
- Comparing an athlete's value with a published range from a different method or arm-swing condition
- Switching between the best trial and the mean of trials across sessions. Pick one and say which.

## Example request

> I exported raw force data from our CMJ testing at 1000 Hz. Can you write me a Python function that gives jump height for each trial, and tell me why it's lower than the number on the old jump mat?

## Check the result

Run these checks:

- Recompute one trial by hand. A flight time of 0.553 s gives 9.81 × 0.553² / 8 = 0.375 m. A takeoff velocity of 2.71 m/s gives 2.71² / 19.62 = 0.374 m.
- When you have both methods for the same jump, the flight time value is usually the higher one. If it is much lower, check the takeoff and body weight steps.
- Compare body mass from quiet standing with the athlete's scale mass. A large gap means the athlete moved or the plate was not zeroed.

## Sources

This file cites these sources:

- Linthorne NP. Analysis of standing vertical jumps using a force platform. American Journal of Physics. 2001;69(11):1198-1204. https://doi.org/10.1119/1.1397460
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength and Conditioning Journal. 2018;40(4):96-106. https://doi.org/10.1519/SSC.0000000000000375 (cited as McMahon et al., 2018a)
- McMahon JJ, Jones PA, Suchomel TJ, Lake J, Comfort P. Influence of the reactive strength index modified on force- and power-time curves. International Journal of Sports Physiology and Performance. 2018;13(2):220-227. https://doi.org/10.1123/ijspp.2017-0056 (cited as McMahon et al., 2018b)
- Owen NJ, Watkins J, Kilduff LP, Bevan HR, Bennett MA. Development of a criterion method to determine peak mechanical power output in a countermovement jump. Journal of Strength and Conditioning Research. 2014;28(6):1552-1558. https://doi.org/10.1519/JSC.0000000000000311
- Sole CJ, Suchomel TJ, Stone MH. Preliminary scale of reference values for evaluating reactive strength index-modified in male and female NCAA Division I athletes. Sports. 2018;6(4):133. https://doi.org/10.3390/sports6040133
- Godhe M, Bergman S, Petré H. Between-session reliability of portable isometric mid-thigh pull and countermovement jump tests in elite male ice hockey players from the Swedish Hockey League. Sports. 2025;13(12):456. https://doi.org/10.3390/sports13120456
- Thomas C, Dos'Santos T, Comfort P, Jones PA. Between-session reliability of common strength- and power-related measures in adolescent athletes. Sports. 2017;5(1):15. https://doi.org/10.3390/sports5010015
- Bishop C, Read P, Lake J, Chavda S, Turner A. Interlimb asymmetries: understanding how to calculate differences from bilateral and unilateral tests. Strength and Conditioning Journal. 2018;40(4):1-6. https://doi.org/10.1519/SSC.0000000000000371
- Harman EA, Rosenstein MT, Frykman PN, Rosenstein RM. The effects of arms and countermovement on vertical jumping. Medicine and Science in Sports and Exercise. 1990;22(6):825-833. https://doi.org/10.1249/00005768-199012000-00015 (accessed 2026-10-02)
- Vaverka F, Jandačka D, Zahradník D, Uchytil J, Farana R, Supej M, Vodičar J. Effect of an arm swing on countermovement vertical jump performance in elite volleyball players. Journal of Human Kinetics. 2016;53:41-50. https://doi.org/10.1515/hukin-2016-0009 (accessed 2026-10-02)
