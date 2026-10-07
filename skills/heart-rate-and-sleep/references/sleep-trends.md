# Sleep trends

Last checked: 2026-10-07

## What it measures

This file trends four sleep measures for each athlete against their own baseline: total sleep time, sleep efficiency, the sleep midpoint, and how much the midpoint moves from night to night. It also reports nap time in a separate column. It works with a wearable, a bedside device, or a sleep diary, one source per athlete.

It describes sleep timing and amount for a healthy athlete. It does not screen for sleep disorders or judge health.

## Formula

Use these formulas for one night:

```text
total sleep time (h)     = TST (min) / 60
time in bed (min)        = out of bed − into bed
sleep efficiency (%)     = TST (min) / time in bed (min) × 100
sleep midpoint           = sleep onset + (final wake − sleep onset) / 2
midpoint regularity (min) = sample SD of the midpoints over the last 14 nights
```

Define every term in the formula:

- `TST`: total sleep time, the total time spent asleep in the night, in minutes (Chinoy et al., 2021). Take it from the device or diary. Do not compute it as wake time minus bedtime, because that includes time awake.
- `time in bed`: from getting into bed to getting out of bed, in minutes.
- `nap time`: the minutes asleep in naps on the night date, reported in its own column beside TST. Never add it to TST. TST, efficiency, the midpoint, and every band use the main sleep only.
- `sleep efficiency`: TST as a percentage of time in bed (Chinoy et al., 2021).
- `sleep onset`: the clock time of falling asleep. `final wake`: the clock time of the last waking.
- `sleep midpoint`: the time halfway through the main sleep. With sleep from 00:00 to 08:00, the midpoint is 04:00 (Fischer et al., 2021).
- `midpoint regularity`: the intra-individual SD of the midpoint. A lower number means a more regular pattern (Fischer et al., 2021). The SD can be applied to sleep onset, sleep offset, midsleep, or sleep duration (Fischer et al., 2021). This skill uses the midpoint.

Fischer et al. (2021) found that this SD needed more than a week of sleep data for an unbiased estimate. This skill uses a 14-night window and needs at least 8 valid nights in it. Both numbers are this repository's choice.

### Handle clock times across midnight

Give each night a night date: the date of the into-bed time minus 12 hours. A bedtime of 23:30 on 2026-09-11 and a bedtime of 00:20 on 2026-09-12 both give a night date of 2026-09-11. Use full date and time values for this, not clock times alone.

Convert every time to minutes since 12:00 noon on the night date before you average or subtract. Then 23:30 is 690 and 00:40 is 760, and they sort in the right order. Plain clock minutes put 00:40 before 23:30, and the midpoint lands in the afternoon. A night dated by the calendar date of a bedtime after midnight gets the next day's date. Its midpoint, counted from noon on that date, is negative.

This conversion assumes the main sleep starts between noon and the next noon. For an athlete who sleeps in the day, such as after a night match or a long flight, choose another anchor with the user.

### Compare with the athlete's baseline

Compare each measure with the athlete's own history, not with a fixed target. Walsh et al. (2021) state that a one-size-fits-all approach to sleep recommendations, such as 7 to 9 hours a night, is unlikely to be ideal. They recommend an individualized approach that considers the athlete's perceived sleep need.

Build the band with the rules in the `monitoring-statistics` skill. If it is installed, use its individual baseline and z-score reference. Follow these rules:

- Use the prior nights only. Keep tonight out of its own baseline.
- Use the usual-variation band: `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`. Never call it noise or measurement error.
- Offer at least 10 prior valid nights as the minimum, as the `monitoring-statistics` skill does.
- Compare each night with the band. Show a 7-night mean beside it as context, with the number of nights it holds. Do not compare the 7-night mean with this band. A mean of 7 nights varies less than one night, so the band is too wide for it.
- For midpoint regularity, show the trend of the 14-night SD. Do not build a band for it.

### Compare devices and scores with care

Wearable sleep outputs come from proprietary algorithms. Device makers update their models, apps, and sleep algorithms, so results apply best to the version tested (Chinoy et al., 2021). In 34 healthy young adults, mean TST bias against laboratory polysomnography ranged from −0.3 to +46.8 min across 7 consumer devices. Research actigraphy overestimated TST by 23.9 min. Sleep stage assessments by the devices were inconsistent (Chinoy et al., 2021).

Follow these rules:

- Compare an athlete only with their own data from the same device and app.
- Start a new baseline when the device changes. Note app or firmware updates in the data.
- Do not compare TST between athletes who use different devices.
- Report sleep stages (light, deep, REM) only as the device's output. Do not trend them or interpret them.
- Treat recovery, readiness, and sleep scores as vendor composites. Vendors do not publish their full formulas. See the WHOOP and Oura device references in this skill. Do not combine scores from two vendors, and do not treat a score as a measurement.

### Calculate it in a spreadsheet

Put one athlete per sheet with one row per night, in date order. Store each time as a full date and time, such as `2026-09-12 00:20`. Put into bed in column B, sleep onset in C, final wake in D, out of bed in E, and TST in minutes in F. Put the night date in column A. Put nap time in minutes in column N, and leave it blank when the athlete took no nap. For a recorded night, use `=INT(B2-0.5)`, the date of into bed minus 12 hours. For a missing night, type the date, leave B to F blank, and keep the row. Use these formulas:

```text
Night date, A2:                 =INT(B2-0.5)
TST (h), G2:                    =IF(F2="","",F2/60)
Time in bed (min), H2:          =IF(OR(B2="",E2=""),"",(E2-B2)*1440)
Efficiency (%), I2:             =IF(OR(F2="",H2=""),"",F2/H2*100)
Midpoint (min since noon), J2:  =IF(OR(A2="",C2="",D2=""),"",((C2+D2)/2-(A2+0.5))*1440)
Midpoint (clock), K2:           =IF(J2="","",MOD(J2/1440+0.5,1))
```

Format `A2` as a date and `K2` as `hh:mm`. `A2 + 0.5` is 12:00 noon on the night date. Column N is typed, and no formula adds it to F or G.

For midpoint regularity from row 15 down, so each window holds 14 nights:

```text
Nights in window, L15:          =COUNT(J2:J15)
Midpoint SD (min), M15:         =IF(L15<8,"",STDEV.S(J2:J15))
```

For the baseline band and z-score of TST and efficiency, use the spreadsheet formulas in the `monitoring-statistics` skill on columns F and I.

### Calculate it in Power BI and Tableau

Both versions assume one row per athlete, night, and measure in a `measures` table. Build three rows per night before import, from full date and time values, not clock times alone:

- `sleep_tst` in `min`
- `sleep_time_in_bed` in `min`
- `sleep_midpoint` in `min_since_noon`, counted from 12:00 on the night date
- `sleep_nap` in `min`, the nap time on that night date, only for nights with a nap

Set `measure_date` to the night date, the date of the into-bed time minus 12 hours, and `status` to `ok` for a valid night. A bedtime of 00:20 on 2026-09-12 then belongs to the night of 2026-09-11, and its midpoint stays positive.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Put `athletes[athlete_id]` and `dates[date]` in the visual. Use these DAX measures:

```text
TST (h) =
VAR t =
    CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sleep_tst",
        measures[unit] = "min", measures[status] = "ok" )
RETURN IF ( NOT ISBLANK ( t ), t / 60 )

Sleep efficiency (%) =
VAR t =
    CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sleep_tst",
        measures[unit] = "min", measures[status] = "ok" )
VAR b =
    CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sleep_time_in_bed",
        measures[unit] = "min", measures[status] = "ok" )
RETURN IF ( NOT ISBLANK ( t ) && b > 0, t / b * 100 )

Nap time (min) =
CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sleep_nap",
    measures[unit] = "min", measures[status] = "ok" )

Sleep midpoint (min since noon) =
CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sleep_midpoint",
    measures[unit] = "min_since_noon", measures[status] = "ok" )

Midpoint SD, 14 nights (min) =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Sleep midpoint (min since noon)] ),
            DATESINPERIOD ( dates[date], today, -14, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && COUNTROWS ( recorded ) >= 8,
        STDEVX.S ( recorded, [@x] )
    )
```

In Tableau, make a scaffold table with one row for every athlete and every calendar date. Left join `measures` to it on `athlete_id`, and on scaffold `date` equal to `measure_date`. Put `athlete_id` and `date` on the view, and compute the table calculations along `date` for each athlete. Use these calculations:

```text
TST (h) (aggregate):
MIN(IF [measure_name] = "sleep_tst" AND [unit] = "min" AND [status] = "ok" THEN [value] END) / 60

Nap time (min) (aggregate):
MIN(IF [measure_name] = "sleep_nap" AND [unit] = "min" AND [status] = "ok" THEN [value] END)

Time in bed (min) (aggregate):
MIN(IF [measure_name] = "sleep_time_in_bed" AND [unit] = "min" AND [status] = "ok" THEN [value] END)

Sleep efficiency (%) (aggregate):
IF [Time in bed (min)] > 0 THEN [TST (h)] * 60 / [Time in bed (min)] * 100 END

Sleep midpoint (min since noon) (aggregate):
MIN(IF [measure_name] = "sleep_midpoint" AND [unit] = "min_since_noon" AND [status] = "ok"
    THEN [value] END)

Nights in last 14 (table calculation):
WINDOW_SUM(IIF(ISNULL([Sleep midpoint (min since noon)]), 0, 1), -13, 0)

Midpoint SD, 14 nights (min) (table calculation):
IF [Nights in last 14] >= 8 THEN WINDOW_STDEV([Sleep midpoint (min since noon)], -13, 0) END
```

Blanks behave this way in each tool:

- Power BI: a missing night gives blank values. The 14-night window counts calendar dates, so it does not stretch.
- Tableau: `WINDOW_STDEV` skips nulls. The count makes the minimum visible.

For the baseline band and z-score of TST and efficiency, use the measures in the `monitoring-statistics` skill.

### Calculate it in Python

Use this Python code. The regularity function needs pandas. The other three use the standard library only:

```python
from datetime import datetime, time, timedelta
import pandas as pd

def night_date(in_bed):
    """The date of into bed minus 12 hours, so 00:20 on 2026-09-12 gives 2026-09-11."""
    return (in_bed - timedelta(hours=12)).date()

def mins_since_noon(t, night):
    """Minutes from 12:00 on the night date, so 23:30 = 690 and 00:40 next day = 760."""
    return (t - datetime.combine(night, time(12))).total_seconds() / 60

def sleep_night(in_bed, onset, final_wake, out_of_bed, tst_min, nap_min=None):
    """Times as 'YYYY-MM-DD HH:MM'. nap_min is reported beside TST, never added to it."""
    b, on, wk, out = (datetime.strptime(x, "%Y-%m-%d %H:%M")
                      for x in (in_bed, onset, final_wake, out_of_bed))
    night = night_date(b)
    tib = (out - b).total_seconds() / 60
    return {"night_date": night, "tst_h": tst_min / 60, "tib_min": tib, "nap_min": nap_min,
            "efficiency_pct": tst_min / tib * 100,
            "midpoint_min_since_noon": mins_since_noon(on + (wk - on) / 2, night)}

REG_WINDOW, REG_MIN = 14, 8   # nights, valid nights: this repository's choice

def add_regularity(d):
    """d: one athlete, one row per calendar night, midpoint NaN when missing."""
    roll = d["midpoint_min_since_noon"].rolling(REG_WINDOW, min_periods=REG_MIN)
    return d.assign(midpoint_sd_min=roll.std())
```

In R, set the night date and convert times the same way, then use `sd()` over a 14-night window with `zoo::rollapply()`.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Confirm the source for each athlete: device and app version, or diary.
2. Load one row per athlete and night, with into bed, sleep onset, final wake, out of bed, TST of the main sleep, and nap time.
3. Keep missing nights as blank rows.
4. Set each night date to the date of into bed minus 12 hours. Convert every time to minutes since noon on that date.
5. Compute TST in hours, time in bed, and efficiency. Report nap time in its own column beside TST. Do not add it to TST.
6. Compute the sleep midpoint.
7. Compute the 14-night SD of the midpoint where at least 8 nights are present.
8. Build the usual-variation band for TST and efficiency from prior nights.
9. Compare tonight with the band. Show the 7-night mean as context. Report n.
10. Name the device, and say that its outputs are not comparable with another device.

## Worked example

This example uses one made-up athlete over 7 nights from one wearable. Every number below came from running the calculation in Python.

| Night | Night date | Into bed | Onset | Final wake | Out of bed | TST (min) |
|---|---|---|---|---|---|---|
| 1 | 2026-09-07 | 22:50 | 23:10 | 07:05 | 07:15 | 441 |
| 2 | 2026-09-08 | 23:05 | 23:20 | 07:00 | 07:10 | 428 |
| 3 | 2026-09-09 | 23:30 | 23:55 | 07:20 | 07:30 | 412 |
| 4 | 2026-09-10 | 22:45 | 23:05 | 06:55 | 07:05 | 446 |
| 5 | 2026-09-11 | 00:20 (2026-09-12) | 00:40 | 07:25 | 07:35 | 371 |
| 6 | 2026-09-12 | 23:10 | 23:30 | 07:10 | 07:20 | 431 |
| 7 | 2026-09-13 | 23:00 | 23:15 | 07:00 | 07:10 | 437 |

Step 1. Night 1 in minutes since noon on 2026-09-07: into bed 650, onset 670, final wake 1145, out of bed 1155.

Step 2. Time in bed = 1155 − 650 = 505 min. Efficiency = 441 / 505 × 100 = 87.33%.

Step 3. Midpoint = 670 + (1145 − 670) / 2 = 907.5 min since noon, which is 03:07:30.

Step 4. Night 5: into bed at 00:20 on 2026-09-12, so the night date is 2026-09-11. Time in bed 435 min, efficiency 85.29%, midpoint 962.5 min since noon on 2026-09-11, which is 04:02:30. Dated by the calendar date of the bedtime, night 5 would share 2026-09-12 with night 6, and its midpoint would be −477.5 min.

Step 5. The 7 midpoints are 907.5, 910.0, 937.5, 900.0, 962.5, 920.0, and 907.5. Their SD is 22.07 min. This window has only 7 nights, so it is shown here to illustrate the arithmetic. The skill reports it only from 8 nights in a 14-night window.

Step 6. Mean TST over the 7 nights is 423.71 min, or 7.06 h.

Step 7. The 10 prior nights of TST are 436, 452, 419, 441, 428, 447, 433, 425, 458, and 439 min. Their mean is 437.8 min and their SD is 12.23 min.

Step 8. The usual-variation band is 437.8 ± 2.3726 × 12.23 = 408.8 to 466.8 min. Night 5, at 371 min, sits below it, with a z-score of −5.46. The 7-night mean of 423.71 min is shown as context only.

Result: TST on night 5 was below the athlete's usual range, on a night with a later bedtime. The week's mean was 423.71 min. Midpoint SD over the week was 22.07 min.

## What changes the number

These choices change the result even when the athlete's sleep does not change:

- Clock arithmetic. With plain clock minutes, the midpoints in the worked example include 907.5 (15:07) and 242.5 (04:02), and the SD becomes 254.0 min instead of 22.07 min.
- Device and algorithm. Mean TST bias ranged from −0.3 to +46.8 min across devices (Chinoy et al., 2021).
- TST source. Final wake minus onset counts time awake as sleep.
- Window length. Fewer nights give a less stable SD. The SD needed more than a week of data (Fischer et al., 2021).
- Missing nights. A rolling count of rows in place of calendar nights stretches the window.
- Main sleep or naps. Adding naps into TST raises TST, and it changes efficiency and the midpoint. This skill trends the main sleep only and reports nap time in a separate column.

## Units and typical range

Report TST in h or min, nap time in min in its own column, time in bed in min, efficiency in percent, the midpoint as a clock time, and regularity in min.

No population range in this file rates an athlete. Efficiency above 100% or TST longer than time in bed means a data error. This check is this repository's choice.

Practice varies. Of 145 practitioners working with high-performance athletes, 88% rated sleep extremely important for recovery, and 61% had monitored athletes' sleep in the previous year. The methods used were a sleep questionnaire (37%), a sleep diary (26%), wrist actigraphy (19%), a phone app (15%), and a finger-worn device (2%) (Hough et al., 2021).

## Data you need

Collect this data:

- Source: one wearable, bedside device, or diary per athlete, with the app version.
- Sampling: one row per night, with into bed, sleep onset, final wake, out of bed, and TST of the main sleep, plus nap time in minutes when a nap happened.
- Minimum data: 8 valid nights in 14 for regularity, and at least 10 prior nights for a baseline band. Both are this repository's choices.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Averaging clock times across midnight. Convert to minutes since noon on the night date first.
- Dating a night by the calendar date of a bedtime after midnight. Use the date of into bed minus 12 hours.
- Computing TST as wake time minus bedtime.
- Adding nap time into TST. Report it in its own column.
- Comparing athletes who use different devices, or one athlete across a device change.
- Treating a readiness or sleep score as a measurement, or averaging scores from two vendors.
- Trending deep or REM sleep from a wearable.
- Judging an athlete against a fixed number of hours.
- Reading a sleep value as a sign of a sleep disorder or illness.

## Example request

> I have two weeks of sleep data from our players' rings. Can you work out average sleep, sleep efficiency, and how regular their bedtimes are, and show who slept less than usual this week?

## Check the result

Run these checks:

- Recompute one value by hand: 441 / 505 × 100 = 87.33%.
- Check that TST is not longer than time in bed, and efficiency is not above 100%.
- Check that TST holds the main sleep only, and that nap time sits in its own column and is in no total.
- Check that every midpoint falls in the night. A midpoint in the afternoon points to clock arithmetic across midnight.
- Check that every athlete's data come from one device.
- Check that tonight is not in its own baseline.
- Check the night count in every window.

## Sources

This file draws on these sources:

- Chinoy ED, Cuellar JA, Huwa KE, Jameson JT, Watson CH, Bessman SC, Hirsch DA, Cooper AD, Drummond SPA, Markwald RR. Performance of seven consumer sleep-tracking devices compared with polysomnography. Sleep. 2021;44(5):zsaa291. https://doi.org/10.1093/sleep/zsaa291 (accessed 2026-10-07)
- Fischer D, Klerman EB, Phillips AJK. Measuring sleep regularity: theoretical properties and practical usage of existing metrics. Sleep. 2021;44(10):zsab103. https://doi.org/10.1093/sleep/zsab103 (accessed 2026-10-07)
- Walsh NP, Halson SL, Sargent C, Roach GD, Nédélec M, Gupta L, Leeder J, Fullagar HH, Coutts AJ, Edwards BJ, Pullinger SA, Robertson CM, Burniston JG, Lastella M, Le Meur Y, Hausswirth C, Bender AM, Grandner MA, Samuels CH. Sleep and the athlete: narrative review and 2021 expert consensus recommendations. British Journal of Sports Medicine. 2021;55(7):356-368. https://doi.org/10.1136/bjsports-2020-102025 (abstract, accessed 2026-10-07)
- Hough PA, North JS, Patterson SD, Pedlar CR. Monitoring athletes sleep: a survey of current trends amongst practitioners. The Journal of Sport and Exercise Science. 2021;5(4):277-284. https://doi.org/10.36905/jses.2021.04.06 (full text at https://research.stmarys.ac.uk/id/eprint/5176/, accessed 2026-10-07)
