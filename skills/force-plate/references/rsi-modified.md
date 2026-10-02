# Reactive strength index-modified

Last checked: 2026-10-02

## What it measures

Reactive strength index-modified (RSI-modified, or RSImod) shows how high an athlete jumps relative to how long the countermovement jump takes to produce.

## Formula

Use this formula for the countermovement jump (CMJ):

```text
RSImod (m/s) = jump height (m) / time to takeoff (s)
```

Define every term in the formula:

- `jump height`: CMJ height in meters. Name the method, takeoff velocity or flight time. See `cmj-jump-height.md`.
- `time to takeoff`: time from the onset of movement (the start of the countermovement) to the instant the athlete leaves the plate, in seconds. It covers the unweighting phase (the dip, when force falls below body weight), the braking phase, and the propulsion phase (McMahon et al., 2018a; Sole et al., 2018).

RSImod was introduced as a version of the reactive strength index (RSI) that works for any vertical jump, not only the drop jump (Ebben and Petushek, 2010). The two are different metrics:

| Metric | Test | Formula |
|---|---|---|
| RSI-modified | Countermovement jump, from standing | jump height / time to takeoff |
| Drop-jump RSI | Drop jump (also called depth jump): step off a box, land, and rebound | jump height / ground contact time |
| Reactive strength ratio | Drop jump | flight time / ground contact time, with no units |

Some protocols compute a drop-jump value as flight time divided by contact time. Healy et al. (2018) call it the reactive strength ratio, to keep it apart from RSI. Check which one a drop-jump value uses before you compare it.

Ground contact time in a drop jump is the time on the ground between landing and rebound. It is a different time interval from time to takeoff. Never compare an RSImod value with a drop-jump RSI value or range. RSImod also differs between jump types, so compare CMJ with CMJ only (Ebben and Petushek, 2010).

Use this spreadsheet formula, with jump height in meters in `B2` and time to takeoff in seconds in `C2`. It returns a blank when either input is blank or not a number:

```text
=IF(COUNT(B2,C2)<2,"",B2/C2)
```

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They divide jump height and time to takeoff from the same trial. They return a blank when either value is missing or time to takeoff is 0.

Both versions assume one row per athlete, date, session, measure, and trial in a `measures` table. Jump height is `measure_name` `cmj_jump_height` in `m`. Time to takeoff is `cmj_time_to_takeoff` in `s`. Convert cm to m and ms to s on import. A height in cm gives a value 100 times too large.

In Power BI, use this DAX measure. It is a measure because height and time sit on two rows. It works one trial at a time, so a height from one trial is never divided by a time from another:

```text
RSImod (m/s) =
MAXX (
    VALUES ( measures[trial_number] ),
    VAR h =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "cmj_jump_height",
            measures[unit] = "m",
            measures[status] = "ok"
        )
    VAR t =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "cmj_time_to_takeoff",
            measures[unit] = "s",
            measures[status] = "ok"
        )
    RETURN IF ( NOT ISBLANK ( h ) && NOT ISBLANK ( t ) && t > 0, h / t )
)
```

With `trial_number` in the visual, the measure gives that trial. Without it, the measure gives the highest trial value that day. If the user picks the best trial by jump height instead, change the rule and name it.

In Tableau, put `athlete_id`, `measure_date`, `session_id`, and `trial_number` on the view. Use these aggregate calculations:

```text
Jump height (m):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)

Time to takeoff (s):
MAX(IF [measure_name] = "cmj_time_to_takeoff" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

RSImod (m/s):
IF ISNULL([Jump height (m)]) OR ISNULL([Time to takeoff (s)]) THEN NULL
ELSEIF [Time to takeoff (s)] <= 0 THEN NULL
ELSE [Jump height (m)] / [Time to takeoff (s)]
END
```

For one value per day without `trial_number` on the view, use this LOD expression, then take its `MAX`:

```text
RSImod per trial (m/s):
{ FIXED [athlete_id], [measure_date], [session_id], [trial_number] :
  IF MAX(IF [measure_name] = "cmj_time_to_takeoff" AND [unit] = "s" AND [status] = "ok" THEN [value] END) > 0
  THEN MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)
     / MAX(IF [measure_name] = "cmj_time_to_takeoff" AND [unit] = "s" AND [status] = "ok" THEN [value] END)
  END }
```

Blanks behave this way in each tool:

- Power BI: the `IF` returns a blank when either value is blank or time is 0. `MAXX` skips the blank trials.
- Tableau: a null height or time gives a null result. A null time makes the `> 0` test null, so the LOD version returns null too.

## Calculate the metric

Follow these steps to calculate RSImod from a raw trace or a summary export:

1. Find the jump height column and its unit.
2. Convert jump height to meters as `jump_height_m`.
3. Note the method, takeoff velocity or flight time.
4. Find the time to takeoff column. Exports may use another name for it.
5. Convert time to takeoff to seconds as `ttt_s`.
6. Check in the device file that time to takeoff runs from the onset of movement to takeoff.
7. If you have only the raw trace, find the onset of movement and takeoff as in `cmj-jump-height.md`.
8. Subtract the two times to get `ttt_s`.
9. Divide `jump_height_m` by `ttt_s` to get RSImod in m/s.
10. Choose one way to summarize trials, either the best trial or the mean of trials, and use it for every session.

## Worked example

This example uses the same synthetic jump as the worked example in `cmj-jump-height.md`.

| Input | Value |
|---|---|
| Onset of movement | 1.000 s |
| Takeoff | 1.650 s |
| Jump height, takeoff velocity method | 0.2866 m |
| Jump height, flight time method | 0.2965 m |

Step 1. Time to takeoff = 1.650 - 1.000 = 0.650 s.

Step 2. RSImod with the takeoff velocity height = 0.2866 / 0.650 = 0.4409 m/s.

Step 3. RSImod with the flight time height = 0.2965 / 0.650 = 0.4562 m/s.

Step 4. If jump height is left in centimeters, 28.66 / 0.650 = 44.09. That value is 100 times too large.

Result: RSImod is 0.4409 m/s with the takeoff velocity method. The same jump gives 0.4562 m/s with the flight time method.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Jump height method. In the worked example, switching to flight time raises RSImod from 0.4409 to 0.4562 m/s.
- Onset of movement. In the worked example, finding onset 30 ms earlier gives a time to takeoff of 0.680 s and RSImod of 0.4215 m/s. Finding it 30 ms later gives 0.620 s and 0.4622 m/s. Onset errors affect time-based measures such as RSImod more than they affect jump height (McMahon et al., 2018a).
- Onset threshold. Some protocols step back 30 ms from the 5 standard deviation threshold (Owen et al., 2014). Use the same rule at every test.
- Takeoff threshold. It changes both jump height and time to takeoff (McMahon et al., 2018a).
- Arm swing and jump type. RSImod differs between jump types (Ebben and Petushek, 2010). The ranges below come from jumps without arm swing: a light bar across the shoulders (Sole et al., 2018) or hands on hips (McMahon et al., 2018b). In basketball players, arm swing raised RSImod by 20 to 24% (Heishman et al., 2019).
- Trial summary. The mean of trial RSImod values differs from mean jump height divided by mean time to takeoff.

## Units and typical range

Report RSImod in m/s. Name the jump height method used.

| Population | Typical range | Source |
|---|---|---|
| NCAA Division I men, CMJ without arm swing (light bar across the shoulders), jump height from flight time, 10 N threshold | 0.424 ± 0.102 m/s (mean ± SD); observed range 0.208 to 0.704 m/s | Sole et al., 2018 |
| NCAA Division I women, CMJ without arm swing (light bar across the shoulders), jump height from flight time, 10 N threshold | 0.314 ± 0.089 m/s (mean ± SD); observed range 0.135 to 0.553 m/s | Sole et al., 2018 |
| Professional male rugby league, CMJ without arm swing (hands on hips), jump height from takeoff velocity, lowest and highest groups | 0.36 ± 0.03 and 0.53 ± 0.05 m/s (mean ± SD) | McMahon et al., 2018b |

Sole et al. (2018) used a 10 N threshold to find both the onset of movement and takeoff, not the 5 standard deviation rule in `cmj-jump-height.md`. McMahon et al. (2018b) took jump height from the velocity at takeoff. Values from another threshold or jump height method are not directly comparable with these ranges.

Time to takeoff in these samples averaged 0.868 ± 0.105 s for men and 0.870 ± 0.114 s for women (Sole et al., 2018), and 0.707 to 0.881 s across the rugby league groups (McMahon et al., 2018b).

Use these ranges to check that data are plausible, not to rate athletes.

Use this test variability from a retest on a separate day to judge a change in one athlete. In adolescent cricket and netball athletes (n = 17), the coefficient of variation of RSImod was 6.11% and the standard error of measurement was 0.03 m/s (Thomas et al., 2017). The protocol was CMJ with hands on hips, mean of 3 trials, retested 1 week later.

Use it only when your protocol and athletes match. Otherwise, measure your own typical error from a short-term retest in which no true change is expected. A separate-day retest counts day-to-day variation as noise and gives a larger typical error than a same-day retest. Judge a change with the noise band, 1.96 × TE × √(1 + 1/n) for a baseline mean of n tests, as the `force-plate` skill describes.

## Data you need

Collect this data:

- Source: a force plate, so you can find the onset of movement and takeoff. A contact mat cannot give time to takeoff.
- Sampling: at least 1000 Hz (McMahon et al., 2018a; Sole et al., 2018)
- Minimum data: at least 1 s of still standing before each jump, so the onset of movement can be found (McMahon et al., 2018a)

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using jump height in centimeters. This makes RSImod 100 times too large, for example 42 instead of 0.42. Convert to meters first.
- Using time to takeoff in milliseconds. Convert to seconds first.
- Dividing by flight time or contact time instead of time to takeoff
- Measuring time to takeoff from the start of the recording instead of the onset of movement
- Changing the onset threshold between sessions. A shift in the onset of movement likely has a larger effect on time-based measures, such as time to takeoff and RSImod, than on jump height (McMahon et al., 2018a). Use one threshold for all trials, sessions, and athletes.
- Mixing jump height methods. RSImod from flight time and RSImod from takeoff velocity are not comparable.
- Comparing RSImod with drop-jump RSI ranges, or calling both "RSI" in one table
- Averaging differently across sessions. The mean of trial RSImod values is not the same as mean jump height divided by mean time to takeoff. Pick one and say which.

## Example request

> Our force plate export has jump height in cm and contraction time in ms for every CMJ. Can you add an RSI-modified column in Google Sheets and flag any values that look like data errors?

Status: not tested.

## Check the result

Run these checks:

- Recompute one value by hand: 0.36 m / 0.868 s = 0.4147 m/s.
- Check the size of the value. Values in the published ranges sit well below 1 m/s. A value of 10 or more almost always means jump height in centimeters.
- Check time to takeoff on its own. Compare it with the ranges above and with the other rows from the same session. A value far outside both usually means the onset of movement or takeoff was found in the wrong place.

## Sources

This file cites these sources:

- Ebben WP, Petushek EJ. Using the reactive strength index modified to evaluate plyometric performance. Journal of Strength and Conditioning Research. 2010;24(8):1983-1987. https://doi.org/10.1519/JSC.0b013e3181e72466
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength and Conditioning Journal. 2018;40(4):96-106. https://doi.org/10.1519/SSC.0000000000000375 (cited as McMahon et al., 2018a)
- McMahon JJ, Jones PA, Suchomel TJ, Lake J, Comfort P. Influence of the reactive strength index modified on force- and power-time curves. International Journal of Sports Physiology and Performance. 2018;13(2):220-227. https://doi.org/10.1123/ijspp.2017-0056 (cited as McMahon et al., 2018b)
- Owen NJ, Watkins J, Kilduff LP, Bevan HR, Bennett MA. Development of a criterion method to determine peak mechanical power output in a countermovement jump. Journal of Strength and Conditioning Research. 2014;28(6):1552-1558. https://doi.org/10.1519/JSC.0000000000000311
- Healy R, Kenny IC, Harrison AJ. Reactive strength index: a poor indicator of reactive strength? International Journal of Sports Physiology and Performance. 2018;13(6):802-809. https://doi.org/10.1123/ijspp.2017-0511
- Thomas C, Dos'Santos T, Comfort P, Jones PA. Between-session reliability of common strength- and power-related measures in adolescent athletes. Sports. 2017;5(1):15. https://doi.org/10.3390/sports5010015
- Sole CJ, Suchomel TJ, Stone MH. Preliminary scale of reference values for evaluating reactive strength index-modified in male and female NCAA Division I athletes. Sports. 2018;6(4):133. https://doi.org/10.3390/sports6040133
- Heishman A, Brown B, Daub B, Miller R, Freitas E, Bemben M. The influence of countermovement jump protocol on reactive strength index modified and flight time: contraction time in collegiate basketball players. Sports. 2019;7(2):37. https://doi.org/10.3390/sports7020037 (accessed 2026-10-02)
