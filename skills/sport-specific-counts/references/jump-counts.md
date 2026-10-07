# Jump counts

Last checked: 2026-10-07

## What it measures

A jump count shows how many times an athlete jumped in a session, day, or week, from a wearable sensor or from video. Where the sensor also gives a height for each jump, the jump height sum adds those heights, so a session of high jumps reads larger than a session of low jumps with the same count.

## Formula

Use these formulas for one athlete and one session. Use the totals method in [count-totals.md](count-totals.md) for days, weeks, and rolling windows:

```text
jump count (count)          = number of jumps recorded in the session
jump height sum (m)         = sum of the height of every recorded jump
mean jump height (m)        = jump height sum / jump count
sensor recall               = jumps matched on video and sensor / jumps seen on video
sensor precision            = jumps matched on video and sensor / jumps the sensor recorded
```

Define every term in the formula:

- `jump`: one takeoff and landing that the sensor or the video coder counts as a jump. Each device and each coding rule has its own definition.
- `height of every jump`: the device's estimate for that jump, in meters. Convert cm to m before you add.
- `jumps matched`: jumps that the video coder and the sensor both recorded at the same time.
- `recall`: the share of real jumps the sensor caught. A recall below 1 means the sensor missed jumps.
- `precision`: the share of sensor jumps that were real jumps. A precision below 1 means the sensor counted things that were not jumps.

The jump height sum is this skill's choice of a count weighted by height. It equals jump count × mean jump height. Charlton et al. (2017) proposed a related load index, the product of the jump count and the average kinetic energy of the jumps. Use their index only if the user asks for it, and name it.

Always get the jump height sum from the heights of single jumps, or from each session's count × mean height. Never multiply a week's count by an average of session means.

### What each count misses

Each source sees only part of an athlete's jumping:

- **Sensor counts.** In 14 professional men's volleyball players over 3 practices and 2 matches, one waist-worn inertial jump sensor counted 99.3% of the 3637 jumps seen on video (Skazalski et al., 2018). In junior elite male volleyball players, the same device had a precision of 0.995 to 1.000 and a recall of 0.814 to 0.930 against video (Charlton et al., 2017). It rarely counted a jump that did not happen, but it missed some real jumps.
- **Sensor jump heights.** The device overestimated jump height by an average of 5.5 cm (95% CI 4.5 to 6.5 cm) across volleyball jumps, and its minimal detectable change was 9.7 cm (Skazalski et al., 2018). Against 3D motion analysis, its mean bias was 3.57 to 4.28 cm (Charlton et al., 2017).
- **Video counts.** Video was the reference in both studies, coded jump by jump after the session. It misses any jump off camera, and it needs a written rule for what counts as a jump.
- **Basketball and other sports.** Both validation studies were in volleyball, with one device. This file cites no validation in basketball. Before you trust a count in another sport or from another device, check it against video, as below.
- **Missing days.** A sensor counts only while worn and synced. A day without it is missing, not 0.

### Check a sensor against video

Follow these steps to check one device in your setting:

1. Film one full session for a few athletes.
2. Write a rule for what counts as a jump, and code every jump on video with its time.
3. Match each video jump with a sensor jump at the same time.
4. Count the matched jumps, the video jumps, and the sensor jumps.
5. Calculate recall and precision with the formulas above.
6. Report both values with the session type and the number of jumps.

### Calculate it in a spreadsheet

For single jumps, put one row per jump with the height in meters in column `D`, the athlete in `A`, the date in `B`, and the session in `C`. In a session summary with the athlete in `G2`, the date in `H2`, and the session in `I2`, use:

```text
Jump count, J2:         =COUNTIFS($A:$A,G2,$B:$B,H2,$C:$C,I2)
Heights filled, M2:     =COUNTIFS($A:$A,G2,$B:$B,H2,$C:$C,I2,$D:$D,">=0")
Jump height sum (m), K2: =IF(OR(J2=0,M2<J2),"",SUMIFS($D:$D,$A:$A,G2,$B:$B,H2,$C:$C,I2))
Mean jump height (m), L2: =IF(K2="","",K2/J2)
```

`K2` stays blank when any jump in the session has no height, so a blank height cannot lower the sum without warning.

For a session export with a count and a mean height, put the count in `B2` and the mean height in meters in `C2`:

```text
Jump height sum (m), D2: =IF(COUNT(B2,C2)<2,"",B2*C2)
```

For a video check, put the matched jumps in `B2`, the video jumps in `C2`, and the sensor jumps in `D2`:

```text
Recall, E2:     =IF(C2=0,"",B2/C2)
Precision, F2:  =IF(D2=0,"",B2/D2)
```

Recall and precision are single ratios from one video check. In Power BI, Tableau, or Python, divide the same three counts the same way.

### Calculate it in Power BI and Tableau

Both versions assume one row per session in the `measures` table, with `measure_name` `jump_count` in `count` and `mean_jump_height` in `m`. Convert cm to m on import. For days, weeks, and rolling windows, build `daily_jump_count` and `daily_jump_height_sum` as in [count-totals.md](count-totals.md).

In Power BI, put `athletes[athlete_id]`, `dates[date]`, and `measures[session_id]` in the visual. Use this measure. It works one session at a time, so a count from one session is never multiplied by a height from another:

```text
Jump height sum (m) =
SUMX (
    VALUES ( measures[session_id] ),
    VAR n =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "jump_count",
            measures[unit] = "count",
            measures[status] = "ok"
        )
    VAR h =
        CALCULATE (
            MAX ( measures[value] ),
            measures[measure_name] = "mean_jump_height",
            measures[unit] = "m",
            measures[status] = "ok"
        )
    RETURN IF ( NOT ISBLANK ( n ) && NOT ISBLANK ( h ), n * h )
)
```

Without `session_id` in the visual, the measure adds the sessions in view. A session with a blank count or height adds nothing, so show the session count beside the sum.

In Tableau, put `athlete_id`, `measure_date`, and `session_id` on the view. Use these aggregate calculations:

```text
Jump count:
MAX(IF [measure_name] = "jump_count" AND [unit] = "count" AND [status] = "ok" THEN [value] END)

Mean jump height (m):
MAX(IF [measure_name] = "mean_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)

Jump height sum (m):
IF ISNULL([Jump count]) OR ISNULL([Mean jump height (m)]) THEN NULL
ELSE [Jump count] * [Mean jump height (m)]
END
```

To add sessions into a day without `session_id` on the view, use this LOD expression, then take its `SUM`:

```text
Jump height sum per session (m):
{ FIXED [athlete_id], [measure_date], [session_id] :
  MAX(IF [measure_name] = "jump_count" AND [unit] = "count" AND [status] = "ok" THEN [value] END)
  * MAX(IF [measure_name] = "mean_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END) }
```

A null count or height gives a null session value, which `SUM` skips. Show the number of sessions next to the sum.

### Calculate it in Python

```python
# jumps: one row per jump, height_m NaN when the device gave no height.
s = (jumps.groupby(["athlete_id", "date", "session_id"])["height_m"]
          .agg(jump_count="size", heights_filled="count",
               jump_height_sum_m=lambda x: x.sum(min_count=len(x))))
s["mean_jump_height_m"] = s["jump_height_sum_m"] / s["jump_count"]
```

`min_count=len(x)` keeps the sum missing when any jump in the session has no height.

## Calculate the counts

Follow these steps to calculate jump counts from raw inputs:

1. Ask where the counts come from: a sensor, video coding, or a tally. Ask which device and which jump definition.
2. Convert every jump height to meters.
3. Count the jumps in each session.
4. If the sensor gives single-jump heights, add them to get the jump height sum. If it gives only a session mean, multiply the session count by the session mean.
5. Mark sessions with no sensor data as missing, not 0.
6. Build daily, weekly, and rolling totals for the count and the height sum with [count-totals.md](count-totals.md).
7. For a weekly mean jump height, divide the weekly height sum by the weekly count. Do not average the session means.
8. If the user has a video check, report recall and precision with the setting.

## Worked example

One volleyball player wears a jump sensor for a week starting Monday 2026-08-03. The sensor was not worn on Thursday. Tuesday, Saturday, and Sunday are rest days.

| Date | Session | Jump count | Mean jump height (m) | Jump height sum (m) |
|---|---|---|---|---|
| 2026-08-03 | Practice | 118 | 0.48 | 56.64 |
| 2026-08-04 | Rest | 0 | none | 0 |
| 2026-08-05 | Practice | 142 | 0.46 | 65.32 |
| 2026-08-06 | Practice | missing | missing | missing |
| 2026-08-07 | Match | 96 | 0.55 | 52.80 |
| 2026-08-08 | Rest | 0 | none | 0 |
| 2026-08-09 | Rest | 0 | none | 0 |

Work through the week:

- Monday: 118 × 0.48 = 56.64 m.
- Jump count: 118 + 142 + 96 = 356 jumps, 6 of 7 days. Report it as incomplete.
- Jump height sum: 56.64 + 65.32 + 52.80 = 174.76 m, 6 of 7 days.
- Mean jump height: 174.76 / 356 = 0.4909 m.
- The wrong method averages the session means: (0.48 + 0.46 + 0.55) / 3 = 0.4967 m. It gives the short match the same weight as the long practices.

For single jumps, a set of 5 jumps at 0.52, 0.49, 0.55, 0.47, and 0.50 m gives a height sum of 2.53 m. That equals 5 × the mean of 0.506 m.

A video check of one practice found 150 jumps on video and 128 on the sensor, with 126 matched. Recall is 126 / 150 = 0.84. Precision is 126 / 128 = 0.984. The sensor missed 24 jumps and counted 2 that the coder did not.

## What changes the number

These choices change the result even when the athlete's jumping does not:

- Device. A device that reads 5.5 cm high on every jump, as in Skazalski et al. (2018), adds 142 × 0.055 = 7.81 m to Wednesday's height sum.
- Recall. At the lowest recall Charlton et al. (2017) report, 0.814, a sensor would record about 122 of 150 real jumps. At their highest, 0.930, it would record about 140.
- Jump definition. A video coder who counts small hops or blocks without a full takeoff gets a different count from one who does not.
- Session means versus single jumps. Averaging session means gave 0.4967 m instead of 0.4909 m in the worked example.
- Missing days. Writing 0 on Thursday makes the week look complete.

## Units and typical range

Report jump count as a whole number, jump height sum in m, and mean jump height in m. Name the device, the jump definition, and the window with every value.

Jump counts have no population range that applies across sports, positions, and training phases. Compare each athlete with their own history from the same device. These figures describe the device studies, not athletes:

| Setting | Figure | Source |
|---|---|---|
| Professional men's volleyball, practice and matches, against video | 99.3% of 3637 jumps counted; height overestimated by 5.5 cm on average; minimal detectable change 9.7 cm | Skazalski et al., 2018 |
| Junior elite men's volleyball, training and matches, against video and 3D motion analysis | Precision 0.995 to 1.000; recall 0.814 to 0.930; height bias 3.57 to 4.28 cm | Charlton et al., 2017 |

To judge a change in mean jump height for one athlete, use the typical error and noise band rules in the `monitoring-statistics` skill. The minimal detectable change above applies only to that device and setting.

## Data you need

Collect this data:

- Source: a wearable jump sensor export with single jumps or session summaries, or video coded jump by jump.
- Sampling: every session, with the device worn the same way each time.
- Minimum data: one video check per device and setting before you trust the count, and several complete weeks before you read a trend.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with jump counts:

- Averaging session mean heights to get a weekly mean. Divide the weekly height sum by the weekly count.
- Adding heights in cm to heights in m.
- Writing 0 for a session without the sensor.
- Comparing counts or heights across devices, or with a video count, without saying so.
- Treating the sensor's jump height as a force plate jump height. The device's heights differed from the reference method in both studies.
- Using a volleyball validation as proof for basketball or another sport.

## Example request

> Our volleyball players wear jump sensors. Give me jumps per player per week and the total of their jump heights, and tell me how far I can trust the counts.

## Check the result

Run these checks:

- Recompute one session's height sum by hand: count × mean height.
- Confirm that the weekly mean height equals the weekly height sum divided by the weekly count.
- Confirm that every height is in meters.
- Confirm that missing sessions stayed missing.

## Sources

This file draws on these sources:

- Skazalski C, Whiteley R, Hansen C, Bahr R. A valid and reliable method to measure jump-specific training and competition load in elite volleyball players. Scandinavian Journal of Medicine and Science in Sports. 2018;28(5):1578-1585. https://doi.org/10.1111/sms.13052 (abstract, accessed 2026-10-07)
- Charlton PC, Kenneally-Dabrowski C, Sheppard J, Spratford W. A simple method for quantifying jump loads in volleyball athletes. Journal of Science and Medicine in Sport. 2017;20(3):241-245. https://doi.org/10.1016/j.jsams.2016.07.007 (abstract, accessed 2026-10-07)
