# CMJ strategy and fatigue metrics

Last checked: 2026-10-07

## What it measures

Strategy metrics show how an athlete produces a countermovement jump (CMJ), not only how high the athlete jumps. Jump height is the outcome. Time, impulse, and depth describe the strategy behind it.

This file covers these metrics:

- **Flight time to contraction time ratio (FT:CT):** time in the air divided by the time the jump took to produce.
- **Time to takeoff:** time from the onset of movement to takeoff. Some software calls it contraction time.
- **Braking net impulse:** the push above body weight that stops the downward movement.
- **Propulsive net impulse:** the push above body weight that drives the athlete up to takeoff.
- **Countermovement depth:** how far the center of mass drops before the athlete pushes up.
- **Trial summary:** the mean of trials or the best trial, for monitoring over time.

The CMJ is the most common power test in elite soccer. In a 2024 survey, 68 of the 74 practitioners who tested power or reactive strength used it (92%) (Asimakidis et al., 2024). Force plate exports already hold the metrics in this file.

Strategy can change when jump height does not. In 11 college athletes, mean power, peak velocity, and flight time changed more than the test's noise in most athletes right after intense running. At 72 h, time-related CMJ variables showed small increases (Gathercole et al., 2015). Gathercole et al. advise tracking variables that reflect the strategy the athlete used, as well as the usual outcome measures.

Use these metrics as decision support for healthy athletes. A change in strategy is not a diagnosis, and it does not tell you whether an athlete may train. Leave that decision to the practitioner.

## Name the phase definitions

Software and studies define the CMJ phases in different ways. A scoping review of 30 studies found 90 different metrics across the 18 studies that used the CMJ. Phase names were not uniform. Across all tests in the review, it counted "braking" 15 times, "eccentric" 13, "propulsive" 10, and "concentric" 19. Event rules also differed. For drop jump contact time, one study used 5 standard deviations of quiet standing force for contact and takeoff. Another used a fixed 10 N for movement onset and takeoff (Badby et al., 2025). Two values with the same name may cover different windows.

Use these definitions, which follow McMahon et al. (2018a):

| Event or phase | Definition used in this file | Other definitions in use |
|---|---|---|
| Onset of movement | First instant force drops below body weight by more than 5 standard deviations of quiet standing force. See `cmj-jump-height.md`. | A step back of 30 ms from that instant (McMahon et al., 2018a). A fixed offset below body weight, such as 20 N (Heishman et al., 2019a). A trace back to the last sample at body weight. |
| Takeoff | First instant force falls below the takeoff threshold. See `cmj-jump-height.md`. | Fixed thresholds such as 10 N or 20 N. Some software also requires the force to stay low for a set time. |
| Unweighting phase | Onset of movement to peak negative velocity, the instant force rises back to body weight | Some sources end it at minimum force. |
| Braking phase | Peak negative velocity to zero velocity, the lowest point of the center of mass | Some software starts it at minimum force, so it is longer and includes force below body weight. Some studies start it at peak negative force. Older studies call it the eccentric or stretching phase. |
| Propulsion phase | Zero velocity to takeoff | A velocity threshold of 0.01 m/s for the start (McMahon et al., 2018a). Also called the concentric or push-off phase. |
| Time to takeoff | Onset of movement to takeoff | Also called contraction time. It moves with the onset rule. |

Follow these rules:

- Before you compare two values, check that both use the same onset rule, takeoff rule, and phase window.
- Read the device file for each column's window. If the device file does not list a column, find the vendor's definition before you use it.
- Do not join a braking value from one device with a braking value from another unless both start at the same event.
- Record the rule in your data table, next to the value.

## Formula

Use these formulas:

```text
time to takeoff (s)               = takeoff time - onset time
FT:CT (no unit)                   = flight time (s) / time to takeoff (s)
braking net impulse (N·s)         = sum of (force - body weight) x time step, over the braking phase
propulsive net impulse (N·s)      = sum of (force - body weight) x time step, over the propulsion phase
net impulse from a gross value    = gross impulse (N·s) - body weight (N) x phase duration (s)
relative net impulse (N·s/kg)     = net impulse (N·s) / body mass (kg)
body mass (kg)                    = body weight (N) / 9.81
countermovement depth (m)         = lowest center of mass displacement between onset and takeoff
```

Define every term in the formula:

- `flight time`: time from takeoff to touchdown, in s.
- `time to takeoff`: time from the onset of movement to takeoff, in s. It covers the unweighting, braking, and propulsion phases.
- `body weight`: mean vertical force during quiet standing, in N. Use the same trial's quiet standing, as in `cmj-jump-height.md`.
- `time step`: time between samples, in s. At 1000 Hz it is 0.001 s.
- `net impulse`: force above body weight added up over time, in N·s. It removes body weight from the impulse. It equals the change in momentum over the phase (McMahon et al., 2018a).
- `gross impulse`: total force added up over time, with body weight included, in N·s. Some exports give this value.
- `phase duration`: length of the phase, in s.
- `relative net impulse`: net impulse per kilogram, in N·s/kg. The unit equals m/s. Relative propulsive net impulse equals takeoff velocity. Relative braking net impulse equals the peak downward speed.
- `center of mass displacement`: how far the center of mass has moved from standing height, in m. It comes from integrating velocity over time. It is 0 while the athlete stands still, and negative below standing height.

These points explain how the metrics relate:

- The braking net impulse equals the unweighting net impulse in size, because braking must stop the downward speed that unweighting created (McMahon et al., 2018a). This holds only when braking starts at peak negative velocity.
- An athlete who shortens the braking phase must produce a larger braking force to stop the same downward speed (McMahon et al., 2018a).
- Propulsive net impulse divided by body mass gives takeoff velocity, so it sets jump height. See `cmj-jump-height.md`.
- RSImod, from `rsi-modified.md`, is jump height divided by time to takeoff. Track jump height and time to takeoff beside it, because a change in RSImod can come from either part. Countermovement depth can help explain a change in time to takeoff (Bishop et al., 2022).
- FT:CT divides flight time, not jump height, by time to takeoff. It is not RSImod, and it is not drop-jump RSI. Some software calls it "RSI". See `rsi-modified.md`.

### Write the spreadsheet formulas

These formulas work in Excel and Google Sheets. Each returns a blank when an input is blank or not a number. Convert ms to s and cm to m before you use them.

Use this layout, one row per athlete, session, and trial:

| Column | Content | Unit |
|---|---|---|
| A | `athlete_id` | text |
| B | `session_id` | text |
| C | `trial_number` | number |
| D | jump height, takeoff velocity method | m |
| E | flight time | s |
| F | time to takeoff | s |
| G | FT:CT | no unit |
| H | body weight | N |
| I | gross propulsive impulse | N·s |
| J | propulsion phase duration | s |
| K | propulsive net impulse | N·s |
| L | relative propulsive net impulse | N·s/kg |
| M | countermovement depth as exported | m |
| N | countermovement depth, positive | m |

Use these formulas in row 2, then fill down:

```text
FT:CT (G2):                          =IF(COUNT(E2,F2)<2,"",IF(F2<=0,"",E2/F2))
Propulsive net impulse (K2):         =IF(COUNT(H2,I2,J2)<3,"",I2-H2*J2)
Relative propulsive net impulse (L2): =IF(COUNT(H2,K2)<2,"",K2/(H2/9.81))
Depth, positive (N2):                =IF(ISNUMBER(M2),ABS(M2),"")
```

Use the net impulse formula only when the export gives gross impulse. If the export already gives net impulse, use it as it is. Use the same formulas for the braking phase, with the gross braking impulse and the braking phase duration.

If the export gives event times instead of time to takeoff, use `=IF(COUNT(P2,Q2)<2,"",Q2-P2)`, with onset time in `P2` and takeoff time in `Q2`, both in s.

For a session summary, put the athlete in `R2` and the session in `S2`. Use these formulas for the mean of trials and the best trial. `FILTER` needs Excel 2021, Excel for Microsoft 365, or Google Sheets:

```text
Mean of trials, FT:CT:
=IFERROR(AVERAGEIFS($G$2:$G$500,$A$2:$A$500,R2,$B$2:$B$500,S2),"")

Best trial, FT:CT from the trial with the highest jump height:
=IFERROR(INDEX(FILTER($G$2:$G$500,($A$2:$A$500=R2)*($B$2:$B$500=S2)),
  MATCH(MAXIFS($D$2:$D$500,$A$2:$A$500,R2,$B$2:$B$500,S2),
  FILTER($D$2:$D$500,($A$2:$A$500=R2)*($B$2:$B$500=S2)),0)),"")
```

`AVERAGEIFS` skips blank results. If two trials tie on jump height, the best-trial formula takes the first one.

### Calculate it in Power BI

These versions assume one row per athlete, date, session, measure, and trial in a `measures` table. Store flight time as `measure_name` `cmj_flight_time` in `s`, time to takeoff as `cmj_time_to_takeoff` in `s`, jump height as `cmj_jump_height` in `m`, propulsive net impulse as `cmj_propulsive_net_impulse` in `N.s`, and body weight as `cmj_body_weight` in `N`. Convert units on import.

Use these DAX measures. Each one works one trial at a time, so a flight time from one trial is never divided by a time from another:

```text
FT:CT per trial =
VAR ft =
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "cmj_flight_time",
        measures[unit] = "s",
        measures[status] = "ok"
    )
VAR ct =
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "cmj_time_to_takeoff",
        measures[unit] = "s",
        measures[status] = "ok"
    )
RETURN IF ( NOT ISBLANK ( ft ) && NOT ISBLANK ( ct ) && ct > 0, ft / ct )

FT:CT mean of trials =
AVERAGEX ( VALUES ( measures[trial_number] ), [FT:CT per trial] )

FT:CT best trial =
VAR best =
    TOPN (
        1,
        VALUES ( measures[trial_number] ),
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "cmj_jump_height",
            measures[unit] = "m",
            measures[status] = "ok"
        ),
        DESC
    )
RETURN AVERAGEX ( best, [FT:CT per trial] )

Relative propulsive net impulse (N.s/kg) =
AVERAGEX (
    VALUES ( measures[trial_number] ),
    VAR imp =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "cmj_propulsive_net_impulse",
            measures[unit] = "N.s",
            measures[status] = "ok"
        )
    VAR bw =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "cmj_body_weight",
            measures[unit] = "N",
            measures[status] = "ok"
        )
    RETURN IF ( NOT ISBLANK ( imp ) && NOT ISBLANK ( bw ) && bw > 0, imp / ( bw / 9.81 ) )
)
```

With `trial_number` in the visual, each measure gives that trial. Without it, the mean measures give the mean of trials. `AVERAGEX` skips blank trials. `TOPN` returns every trial that ties for the highest jump, and the best-trial measure then averages them. Say so if it happens.

### Calculate it in Tableau

Put `athlete_id`, `measure_date`, and `session_id` on the view. Use these calculations:

```text
FT:CT per trial (LOD):
{ FIXED [athlete_id], [measure_date], [session_id], [trial_number] :
  IF MAX(IF [measure_name] = "cmj_time_to_takeoff" AND [unit] = "s" AND [status] = "ok" THEN [value] END) > 0
  THEN MAX(IF [measure_name] = "cmj_flight_time" AND [unit] = "s" AND [status] = "ok" THEN [value] END)
     / MAX(IF [measure_name] = "cmj_time_to_takeoff" AND [unit] = "s" AND [status] = "ok" THEN [value] END)
  END }

Jump height per trial (LOD):
{ FIXED [athlete_id], [measure_date], [session_id], [trial_number] :
  MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END) }

Best jump height in session (LOD):
{ FIXED [athlete_id], [measure_date], [session_id] : MAX([Jump height per trial (LOD)]) }

FT:CT mean of trials:
{ FIXED [athlete_id], [measure_date], [session_id] :
  AVG(IF [measure_name] = "cmj_flight_time" AND [unit] = "s" AND [status] = "ok"
      THEN [FT:CT per trial (LOD)] END) }

FT:CT best trial:
{ FIXED [athlete_id], [measure_date], [session_id] :
  MAX(IF [Jump height per trial (LOD)] = [Best jump height in session (LOD)]
      THEN [FT:CT per trial (LOD)] END) }
```

The mean of trials reads only the flight time rows, so each trial counts once. Blanks behave this way: a null flight time or time to takeoff gives a null trial value, and `AVG` and `MAX` skip it. If two trials tie on jump height, the best-trial calculation takes the higher FT:CT. Say so if it happens.

### Calculate it in Python

Use this Python sketch for a raw force trace. It follows the phase definitions above. Set the takeoff threshold to your device's rule:

```python
import numpy as np

def cmj_strategy(force_n, fs_hz, takeoff_threshold_n, quiet_s=1.0, g=9.81):
    """force_n: summed vertical force in N, starting with at least quiet_s of still standing.
    takeoff_threshold_n: the force below which the athlete is in the air. Use your device's rule."""
    f = np.asarray(force_n, dtype=float)
    dt = 1.0 / fs_hz
    n_quiet = int(quiet_s * fs_hz)
    bw = f[:n_quiet].mean()
    sd = f[:n_quiet].std(ddof=1)
    mass = bw / g
    onset = int(np.argmax(f < bw - 5 * sd))                  # first sample below body weight - 5 SD
    takeoff = onset + int(np.argmax(f[onset:] < takeoff_threshold_n))
    landing = takeoff + int(np.argmax(f[takeoff:] >= takeoff_threshold_n))
    net = f[:takeoff] - bw
    vel = np.cumsum(net / mass) * dt                         # velocity from the start of quiet standing
    disp = np.cumsum(vel) * dt                               # displacement, 0 while standing still
    # vel[i] is the velocity at the end of sample i, so each phase starts one sample after the event
    b0 = onset + int(np.argmin(vel[onset:])) + 1             # braking starts after peak negative velocity
    p0 = b0 + int(np.argmax(vel[b0:] >= 0)) + 1              # propulsion starts after zero velocity
    return {
        "body_weight_n": bw,
        "time_to_takeoff_s": (takeoff - onset) * dt,
        "flight_time_s": (landing - takeoff) * dt,
        "ft_ct": (landing - takeoff) / (takeoff - onset),
        "unweighting_s": (b0 - onset) * dt,
        "braking_s": (p0 - b0) * dt,
        "propulsion_s": (takeoff - p0) * dt,
        "braking_net_impulse_ns": net[b0:p0].sum() * dt,
        "propulsive_net_impulse_ns": net[p0:takeoff].sum() * dt,
        "rel_braking_net_impulse_ns_per_kg": net[b0:p0].sum() * dt / mass,
        "rel_propulsive_net_impulse_ns_per_kg": net[p0:takeoff].sum() * dt / mass,
        "countermovement_depth_m": disp[onset:takeoff].min(),
    }
```

On the synthetic jump in `cmj-jump-height.md`, with 0.492 s of flight added, this sketch gives a time to takeoff of 0.650 s and an FT:CT of 0.7569. The braking net impulse is 96.525 N·s, against an unweighting net impulse of -96.25 N·s. The gap is one sample on a step-shaped trace.

Use this sketch to summarize trials from an export:

```python
import pandas as pd

# one row per athlete, session, and trial, with SI units
trials["ft_ct"] = trials["flight_time_s"] / trials["time_to_takeoff_s"]
keys = ["athlete_id", "session_id"]

# Mean of trials: average each trial's ratio, not the ratio of the averages
mean3 = trials.groupby(keys)[["time_to_takeoff_s", "ft_ct", "jump_height_m"]].mean()

# Best trial: the single trial with the highest jump height; take every metric from it
best = trials.loc[trials.groupby(keys)["jump_height_m"].idxmax()].set_index(keys)
```

## Calculate the metric

Follow these steps to calculate the metrics from a summary export:

1. Find the columns for flight time, time to takeoff, jump height, body weight, impulses, phase durations, and countermovement depth.
2. Read the device file for each column's window, onset rule, and takeoff rule.
3. Record those rules next to the data.
4. Convert times to s, depth to m, impulse to N·s, and body weight to N.
5. Check whether each impulse is net or gross. If it is gross, subtract body weight × phase duration.
6. Divide flight time by time to takeoff to get FT:CT for each trial.
7. Divide each net impulse by body mass to get relative net impulse in N·s/kg.
8. Take the absolute value of countermovement depth, so a deeper dip is a larger number. Keep one sign rule for all data.
9. Summarize trials with one rule for every session: the mean of trials or the best trial. See the next section.
10. Judge a change with the noise band in the `force-plate` skill.

Follow these steps to calculate the metrics from a raw trace:

1. Find body weight, the onset of movement, and takeoff, as in `cmj-jump-height.md`.
2. Integrate net force divided by body mass to get velocity, as in `cmj-jump-height.md`.
3. Find peak negative velocity, the end of unweighting.
4. Find the first sample after it where velocity reaches 0. This is the end of braking and the lowest point.
5. Integrate velocity to get displacement. The lowest value before takeoff is countermovement depth.
6. Add up net force × time step over the braking phase, then over the propulsion phase.
7. Find touchdown, and subtract takeoff time to get flight time.
8. Calculate time to takeoff and FT:CT.

## Choose the mean of trials or the best trial

Use the mean of trials for monitoring. This is this repository's default, based on these studies:

- In a meta-analysis of 151 studies, mean CMJ height was more sensitive than the highest CMJ height to fatigue and to gains after training (Claudino et al., 2017). Most studies, 85.4%, used the highest jump.
- In 36 professional rugby union players, the mean of 3 jumps had a lower between-day coefficient of variation than the single highest jump for all 86 CMJ variables tested (Howarth et al., 2022).
- In a 2024 survey of elite soccer practitioners, 44% used a mix of best and mean scores, and 42% used the best score. Only 38% considered measurement error (Asimakidis et al., 2024).

If the user wants the best trial, define it as the single trial with the highest jump height. Take every metric from that trial. Do not take the shortest time to takeoff from one trial and the highest jump from another, because the result describes no real jump.

Average each trial's ratio. The mean of trial FT:CT values differs from mean flight time divided by mean time to takeoff. Use one rule and name it.

Take the typical error from the same trial summary as the values you compare. A typical error for the mean of 3 does not fit a best-trial value.

Some metrics need more than three trials to be stable. In 300 NCAA Division I men, a reliability coefficient of 0.80 or more needed 8 jumps for eccentric duration and 5 for countermovement depth in football players. Braking impulse needed 7 jumps in baseball players. That study defined braking impulse from peak negative force to zero velocity (Huebner et al., 2025). If the user tracks braking or depth metrics, tell them to check reliability in their own squad first.

## Worked example

This example uses made-up data for one athlete. Body weight is 785.0 N, so body mass is 785.0 / 9.81 = 80.0204 kg. Session 1 is a normal training day. Session 2 is the morning after a match. The export gives phase durations, flight time, gross impulses, and depth.

| Session | Trial | Unweighting (s) | Braking (s) | Propulsion (s) | Flight time (s) | Gross braking impulse (N·s) | Gross propulsive impulse (N·s) | Depth (m) |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0.300 | 0.200 | 0.250 | 0.548 | 245.0 | 408.3 | -0.30 |
| 1 | 2 | 0.290 | 0.190 | 0.245 | 0.558 | 238.8 | 408.4 | -0.29 |
| 1 | 3 | 0.310 | 0.205 | 0.255 | 0.542 | 247.3 | 409.8 | -0.31 |
| 2 | 1 | 0.340 | 0.230 | 0.270 | 0.542 | 264.6 | 421.6 | -0.34 |
| 2 | 2 | 0.320 | 0.220 | 0.265 | 0.554 | 258.3 | 422.5 | -0.33 |
| 2 | 3 | 0.350 | 0.240 | 0.275 | 0.534 | 270.0 | 422.3 | -0.35 |

Step 1. Calculate time to takeoff and FT:CT for session 1, trial 1:

- Time to takeoff = 0.300 + 0.200 + 0.250 = 0.750 s.
- FT:CT = 0.548 / 0.750 = 0.7307.

Step 2. Calculate the net impulses for session 1, trial 1:

- Braking net impulse = 245.0 - 785.0 × 0.200 = 88.00 N·s. Relative: 88.00 / 80.0204 = 1.0997 N·s/kg.
- Propulsive net impulse = 408.3 - 785.0 × 0.250 = 212.05 N·s. Relative: 212.05 / 80.0204 = 2.6499 N·s/kg.
- Jump height from takeoff velocity = 2.6499² / (2 × 9.81) = 0.3579 m.

Step 3. Repeat for every trial:

| Session | Trial | Time to takeoff (s) | FT:CT | Relative braking net impulse (N·s/kg) | Relative propulsive net impulse (N·s/kg) | Jump height (m) |
|---|---|---|---|---|---|---|
| 1 | 1 | 0.750 | 0.7307 | 1.0997 | 2.6499 | 0.3579 |
| 1 | 2 | 0.725 | 0.7697 | 1.1203 | 2.7002 | 0.3716 |
| 1 | 3 | 0.770 | 0.7039 | 1.0794 | 2.6196 | 0.3498 |
| 2 | 1 | 0.840 | 0.6452 | 1.0504 | 2.6200 | 0.3499 |
| 2 | 2 | 0.805 | 0.6882 | 1.0697 | 2.6803 | 0.3661 |
| 2 | 3 | 0.865 | 0.6173 | 1.0197 | 2.5797 | 0.3392 |

Step 4. Summarize each session both ways:

| Summary | Session 1 | Session 2 |
|---|---|---|
| Mean of 3, time to takeoff | 0.7483 s | 0.8367 s |
| Mean of 3, FT:CT | 0.7347 | 0.6503 |
| Mean of 3, jump height | 0.3598 m | 0.3517 m |
| Mean of 3, depth | 0.300 m | 0.340 m |
| Best trial (trial 2 both days), FT:CT | 0.7697 | 0.6882 |

Mean flight time divided by mean time to takeoff gives 0.7341 in session 1, not 0.7347. The difference is small here, but use one rule.

Step 5. Judge each change against noise. This example uses made-up typical errors (TE) from the squad's own retest: 0.020 for FT:CT as a mean of 3, 0.030 for FT:CT from the best trial, 0.025 s for time to takeoff as a mean of 3, and 0.012 m for jump height as a mean of 3. For two single tests, the noise band is 1.96 × √2 × TE, or 2.7719 × TE:

| Metric | Change | Noise band | Result |
|---|---|---|---|
| FT:CT, mean of 3 | -0.0845 | ±0.0554 | Larger than measurement error |
| FT:CT, best trial | -0.0815 | ±0.0832 | Inside the noise band |
| Time to takeoff, mean of 3 | +0.0883 s | ±0.0693 s | Larger than measurement error |
| Jump height, mean of 3 | -0.0080 m | ±0.0333 m | Inside the noise band |

Result: jump height did not change beyond noise. Time to takeoff rose and FT:CT fell, both beyond the noise band for the mean of 3. The dip was 4 cm deeper, which may explain part of the longer time to takeoff. The best-trial FT:CT changed by a similar amount but stayed inside its wider band. Report the change and its band. A repeat test would show whether the change holds. Leave training decisions to the practitioner.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Onset rule. In the worked example, finding onset 30 ms earlier in session 1, trial 1 gives a time to takeoff of 0.780 s and an FT:CT of 0.7026. Finding it 30 ms later gives 0.720 s and 0.7611. Onset errors affect time-based metrics more than velocity and displacement (McMahon et al., 2018a).
- Takeoff and landing thresholds. They change flight time and time to takeoff together.
- Braking window. A braking phase that starts at minimum force is longer than one that starts at peak negative velocity. Its impulse includes force below body weight, and its sign rule may differ.
- Propulsion start. Zero velocity and a 0.01 m/s threshold give slightly different windows (McMahon et al., 2018a).
- Gross or net impulse. In the worked example, the gross braking impulse of 245.0 N·s is 2.784 times the net value of 88.00 N·s.
- Body weight. Every net impulse, velocity, and displacement depends on it. See `cmj-jump-height.md`.
- Body mass scaling. Relative impulse in N·s/kg removes body mass. Absolute impulse in N·s rises when the athlete gains mass.
- Depth sign and unit. Software reports depth as a negative or a positive number, in m or cm. Bishop et al. (2022) suggest scaling depth to standing height for youth athletes, or in sports with large differences in body size, such as basketball.
- Arm swing. FT:CT was higher with arm swing than without in basketball players (Heishman et al., 2019a). Keep one arm condition.
- Cueing. A cue to jump fast shortens braking and raises braking force (McMahon et al., 2018a). Use the same cue at every test.
- Trial summary. The mean of 3 and the best trial give different values and different noise.

## Units and typical range

Report time to takeoff in s, FT:CT with no unit, impulse in N·s or N·s/kg, and depth in m or cm. Name the onset rule, the phase windows, and the trial summary.

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I basketball players (14 men, 8 women), CMJ without arm swing, mean of 3 trials, 1000 Hz, onset and takeoff at 20 N below body weight | FT:CT 0.672 ± 0.13 (mean ± SD), session 1 | Heishman et al., 2019a |
| Same players, CMJ with arm swing | FT:CT 0.773 ± 0.19 (mean ± SD), session 1 | Heishman et al., 2019a |

Use these ranges to check that data are plausible. For a published norm used as a reference point, see the `force-plate` skill limits. For time to takeoff ranges, see `rsi-modified.md`.

No range is given for impulse or depth. Check them this way instead:

- Relative propulsive net impulse equals takeoff velocity. Its square divided by 19.62 must match the takeoff velocity jump height from the same trial.
- Compare depth with the athlete's own other trials from the same session.

Use these reliability findings when you plan testing:

| Population and protocol | Finding | Source |
|---|---|---|
| Professional rugby union men (n = 36), 3 CMJs on 4 days over 8 days, between-day | Coefficient of variation across variables, mean of 3: concentric 2 to 11%, eccentric 1 to 45%, landing 4 to 32%. Single highest jump: 2 to 13%, 1 to 107%, and 6 to 45%. | Howarth et al., 2022 |
| Male college team-sport athletes (n = 11), 6 CMJs per visit | Most of 22 variables had within-day and between-day coefficients of variation under 10% | Gathercole et al., 2015 |
| NCAA Division I men (n = 300), within one session | Eccentric metrics often needed more than 3 jumps for a reliability coefficient of 0.80 | Huebner et al., 2025 |

These figures cover ranges of variables, not one value per metric. Measure your own typical error for each metric you track, from a short-term retest in which no true change is expected (Howarth et al., 2022). Judge a change with the noise band, 1.96 × TE × √(1 + 1/n) for a baseline mean of n tests, as the `force-plate` skill describes.

After an Australian football match, FT:CT fell in 22 elite players (effect size -0.65 ± 0.28). From 24 h after the match onward, it was lower than 48 h before the match (effect size -0.32 ± 0.26) (Cormack et al., 2008). That is a group result from one study. Do not use it as a threshold for one athlete.

## Data you need

Collect this data:

- Source: a force plate. A contact mat gives flight time, but not time to takeoff, impulse, or depth.
- Sampling: at least 1000 Hz (McMahon et al., 2018a).
- Minimum data: at least 1 s of still standing before each jump (McMahon et al., 2018a). Collect at least 3 trials per session. Eccentric and depth metrics may need more (Huebner et al., 2025).
- Baseline: enough repeated tests to measure typical error for each metric, with the same trial summary.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with these metrics:

- Comparing braking values from software with different braking windows. Check the start event first.
- Calling FT:CT "RSI" or comparing it with RSImod. They are different metrics.
- Dividing flight time in s by time to takeoff in ms. This gives 0.000731 instead of 0.7307. Convert both to s.
- Treating a gross impulse as net. Subtract body weight × phase duration.
- Mixing positive and negative depth values, or m and cm, in one trend.
- Building a "best" value from the best metric in each trial. Take every metric from one trial.
- Switching between the mean of trials and the best trial across sessions.
- Judging a change against the spread of trials within one session. Use the noise band with a typical error from repeated tests.
- Calling a strategy change fatigue, or saying an athlete is not ready. Report the change and its band, and leave the decision to the practitioner.

## Example request

> Our force plate export has flight time, contraction time, braking impulse, and depth for 3 CMJs per player. Can you add FT:CT in Google Sheets, compare the mean of 3 with the best jump, and tell me which players changed since Monday?

## Check the result

Run these checks:

- Recompute one value by hand: 0.548 s / 0.750 s = 0.7307.
- Confirm time to takeoff equals unweighting + braking + propulsion when the export gives all three.
- Confirm relative propulsive net impulse squared / 19.62 matches the takeoff velocity jump height from the same trial.
- From a raw trace, confirm the braking and unweighting net impulses match in size, within a sample or two.
- Confirm FT:CT is of the same size as the range above. A value near 1000 or 0.001 means flight time and time to takeoff are in different units.
- Confirm every value in a trend uses the same onset rule, braking window, and trial summary.

## Sources

This file cites these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
- Badby AJ, Ripley NJ, McMahon JJ, Mundy PD, Comfort P. Scoping review of methods of monitoring acute changes in lower body neuromuscular function via force plates. PLoS ONE. 2025;20(5):e0322820. https://doi.org/10.1371/journal.pone.0322820 (accessed 2026-10-07)
- Bishop C, Turner A, Jordan M, Harry J, Loturco I, Lake J, Comfort P. A framework to guide practitioners for selecting metrics during the countermovement and drop jump tests. Strength and Conditioning Journal. 2022;44(4):95-103. https://doi.org/10.1519/SSC.0000000000000677 (accessed 2026-10-07, accepted manuscript)
- Claudino JG, Cronin J, Mezêncio B, McMaster DT, McGuigan M, Tricoli V, Amadio AC, Serrão JC. The countermovement jump to monitor neuromuscular status: a meta-analysis. Journal of Science and Medicine in Sport. 2017;20(4):397-402. https://doi.org/10.1016/j.jsams.2016.08.011 (accessed 2026-10-07, abstract only)
- Cormack SJ, Newton RU, McGuigan MR. Neuromuscular and endocrine responses of elite players to an Australian rules football match. International Journal of Sports Physiology and Performance. 2008;3(3):359-374. https://doi.org/10.1123/ijspp.3.3.359 (accessed 2026-10-07, abstract only)
- Gathercole R, Sporer B, Stellingwerff T, Sleivert G. Alternative countermovement-jump analysis to quantify acute neuromuscular fatigue. International Journal of Sports Physiology and Performance. 2015;10(1):84-92. https://doi.org/10.1123/ijspp.2013-0413 (accessed 2026-10-07, abstract only)
- Heishman A, Brown B, Daub B, Miller R, Freitas E, Bemben M. The influence of countermovement jump protocol on reactive strength index modified and flight time: contraction time in collegiate basketball players. Sports. 2019;7(2):37. https://doi.org/10.3390/sports7020037 (accessed 2026-10-07). Cited as Heishman et al., 2019a, as in `rsi-modified.md`.
- Howarth DJ, Cohen DD, McLean BD, Coutts AJ. Establishing the noise: interday ecological reliability of countermovement jump variables in professional rugby union players. Journal of Strength and Conditioning Research. 2022;36(11):3159-3166. https://doi.org/10.1519/JSC.0000000000004037 (accessed 2026-10-07, abstract only)
- Huebner A, Lever JR, Clark TW, Suchomel TJ, Metoyer CJ, Hauenstein JD, Wagle JP. Novel use of generalizability theory to optimize countermovement jump data collection. Sports. 2025;13(3):85. https://doi.org/10.3390/sports13030085 (accessed 2026-10-07)
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength and Conditioning Journal. 2018;40(4):96-106. https://doi.org/10.1519/SSC.0000000000000375 (accessed 2026-10-07, accepted manuscript). Cited as McMahon et al., 2018a, as in `cmj-jump-height.md`.
