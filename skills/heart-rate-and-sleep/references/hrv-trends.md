# HRV trends

Last checked: 2026-10-07

## What it measures

Heart rate variability (HRV) is the beat-to-beat change in the time between heartbeats. This file trends one HRV index, ln rMSSD, from a short morning reading. It compares a 7-day rolling mean, and the day-to-day spread around it, with the athlete's own baseline.

Use HRV trends as one input to a coach's decision about a healthy athlete. HRV does not diagnose anything. It does not say whether an athlete is ready, fatigued, ill, or at risk.

## Formula

Use these formulas for one athlete:

```text
rMSSD (ms)            = √( mean of (RR(i+1) − RR(i))² )
ln rMSSD              = LN(rMSSD in ms)
7-day mean            = mean of the valid ln rMSSD values in the 7 days ending today
7-day SD              = sample SD of the same values
7-day CV (%)          = 7-day SD / 7-day mean × 100
weekly mean           = mean of the valid ln rMSSD values from Monday to Sunday
```

Define every term in the formula:

- `RR(i)`: the time between two heartbeats, in milliseconds (ms). Also called the R-R interval.
- `rMSSD`: the root mean square of successive differences between RR intervals, in ms. It reflects the part of the nervous system that slows the heart (vagal activity) (Plews et al., 2012).
- `LN`: the natural logarithm. Plews et al. (2012) log-transformed rMSSD because HRV data are skewed. ln rMSSD has no unit.
- `valid`: a reading taken under the athlete's standard conditions that passed the device's artifact check. Set the rule with the user. This definition is this repository's choice.
- `7 days ending today`: today and the 6 calendar days before it, whether or not each day has a reading.
- `7-day CV`: the coefficient of variation (CV) of the daily ln rMSSD values in the window. It shows how much HRV moves from day to day. Plews et al. (2012) calculated a 7-day rolling CV of ln rMSSD.
- `weekly mean`: a mean over a fixed calendar week. Weekly means do not overlap, so they suit a baseline.

Leave a 7-day mean, SD, CV, or weekly mean blank when it has fewer than 3 valid readings. Plews et al. (2014) compared ln rMSSD averaged over 1 to 7 randomly chosen days in the week, in trained triathletes. They concluded that practitioners should use a minimum of 3 valid data points per week. Applying the same minimum to a rolling 7-day window is this repository's choice.

Take the log of each daily rMSSD first, then average. The log of the mean rMSSD is a different number.

### Read a single day against the rolling mean

Lead with the 7-day mean, not the single-day value. In two elite triathletes, Plews et al. (2012) set an individual band of 0.5 × the athlete's CV around their baseline. During normal training, single-day ln rMSSD values fell outside the band 63.6% of the time in the athlete who trained and performed well. In the athlete who later showed non-functional overreaching, single-day values fell outside the band 100% of the time during normal training. When averaged over 7 days, they fell outside it 20% of the time. Plews et al. (2013) state that weekly and 7-day rolling means have shown better methodological validity than single-day values.

Show the single-day value as context, labeled as one reading.

### Set the athlete's normal band

Build the band with the rules in the `monitoring-statistics` skill. If it is installed, use its individual baseline and z-score reference. Follow these rules:

- Use weekly means as the baseline values, not the overlapping 7-day rolling means. Rolling means share 6 of 7 days with the day before, so they are not independent values. This choice is this repository's.
- Keep the current week out of its own baseline.
- Use the usual-variation band from the `monitoring-statistics` skill: `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`, where n is the number of prior weekly means. Never call this band noise or measurement error. It holds real week-to-week change as well as error.
- Offer at least 10 prior weekly means as the minimum, as the `monitoring-statistics` skill does. If the user sets fewer, use their choice and say the band is imprecise.
- Compare the current week's mean, or today's 7-day mean, with the band. A 7-day mean built from 3 readings is less stable than one built from 7, so it crosses the band more often by chance. Show the count.
- Do not compare a single day with this band. Daily values vary more than weekly means, so the band is too narrow for one reading.
- Say that weekly means within a training block are often correlated with each other. Then more than 5% of weeks can fall outside the band by chance.

Show this published band beside it only when the user asks for the method in Plews et al. (2012). Label it as that study's setting:

```text
Plews band = baseline mean ± 0.5 × baseline SD
```

Plews et al. (2012) took the baseline from the first two weeks of daily ln rMSSD values. They set the smallest worthwhile change (SWC) at 0.5 of the athlete's CV. Here 0.5 × CV × mean gives 0.5 × SD. The band is a worthwhile-change line, not a noise line, and it is not a recommendation.

A falling 7-day CV is not a flag in this skill. In the study athlete who later showed non-functional overreaching, the 7-day CV fell steadily toward the race (Plews et al., 2012). That is one case. Report the CV trend as a description only.

### Measure under the same conditions every day

Standardize the reading. Buchheit (2014) described short (5 to 10 min) recordings on waking in the morning as best practice for athletes. Supine recordings are better tolerated by athletes in the field than standing ones, and seated recordings are also of interest for comfort (Buchheit, 2014). Plews et al. (2012) recorded on waking with a chest strap and analysed the last 5 min of a 6 min supine rest.

Record these with every reading:

- Time of the reading, relative to waking
- Position: supine, seated, or standing
- Recording length, and the part analysed
- Device, sensor, and app
- Breathing: free or paced

Keep each of these the same for one athlete. A change in position or device starts a new baseline. Overnight HRV from a ring, wristband, or watch is a different measure from a morning reading. Do not mix the two in one trend, and compare only within one device.

### Calculate it in a spreadsheet

Put one athlete per sheet with one row per calendar day, in date order. Put the date in column A and the valid rMSSD in ms in column B. Leave B blank on a day with no valid reading. Do not delete the row. Use these formulas from row 8 down, so each window holds 7 rows:

```text
ln rMSSD, C2 (fill down from row 2):  =IF(B2="","",LN(B2))
Readings in last 7 days, D8:          =COUNT(C2:C8)
7-day mean, E8:                       =IF(D8<3,"",AVERAGE(C2:C8))
7-day SD, F8:                         =IF(D8<3,"",STDEV.S(C2:C8))
7-day CV (%), G8:                     =IF(D8<3,"",F8/E8*100)
```

`COUNT`, `AVERAGE`, and `STDEV.S` skip the empty text that the formula in column C returns. The window covers 7 calendar days only when every date has a row. A missing row stretches the window.

For the weekly baseline, put one row per week on a second sheet: the week's mean in column B and its count in column C. Use `=IF(COUNT(range)<3,"",AVERAGE(range))` for the mean. Then build the band and z-score with the spreadsheet formulas in the `monitoring-statistics` skill.

### Calculate it in Power BI and Tableau

Both versions assume one row per athlete and reading in a `measures` table, with `measure_name` `hrv_rmssd_morning`, `unit` `ms`, and `status` `ok` for a valid reading. Use one reading per athlete per day. If an athlete has two readings on one day, choose one rule with the user, such as the first reading, and apply it before import.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Put `athletes[athlete_id]` and `dates[date]` in the visual. Use these DAX measures:

```text
ln rMSSD =
VAR r =
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "hrv_rmssd_morning",
        measures[unit] = "ms",
        measures[status] = "ok"
    )
RETURN IF ( NOT ISBLANK ( r ) && r > 0, LN ( r ) )

HRV readings in last 7 days =
VAR today = MAX ( dates[date] )
VAR days =
    CALCULATETABLE (
        ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [ln rMSSD] ),
        DATESINPERIOD ( dates[date], today, -7, DAY )
    )
RETURN COUNTROWS ( FILTER ( days, NOT ISBLANK ( [@x] ) ) ) + 0

ln rMSSD 7-day mean =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [ln rMSSD] ),
            DATESINPERIOD ( dates[date], today, -7, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && COUNTROWS ( recorded ) >= 3,
        AVERAGEX ( recorded, [@x] )
    )

ln rMSSD 7-day SD =
VAR today = MAX ( dates[date] )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [ln rMSSD] ),
            DATESINPERIOD ( dates[date], today, -7, DAY )
        ),
        NOT ISBLANK ( [@x] )
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && COUNTROWS ( recorded ) >= 3,
        STDEVX.S ( recorded, [@x] )
    )

ln rMSSD 7-day CV (%) =
VAR m = [ln rMSSD 7-day mean]
VAR s = [ln rMSSD 7-day SD]
RETURN IF ( NOT ISBLANK ( m ) && NOT ISBLANK ( s ) && m > 0, s / m * 100 )
```

The window counts calendar days through the date table, so a day with no reading does not stretch it. The count test runs before `STDEVX.S`, which returns an error with fewer than 2 values.

In Tableau, make a scaffold table with one row for every athlete and every calendar date. Left join `measures` to it on `athlete_id`, and on scaffold `date` equal to `measure_date`, so a day with no reading still has a mark. Put `athlete_id` and `date` on the view, and compute the table calculations along `date` for each athlete. Use these calculations:

```text
ln rMSSD (aggregate):
LN(MIN(IF [measure_name] = "hrv_rmssd_morning" AND [unit] = "ms" AND [status] = "ok"
          AND [value] > 0 THEN [value] END))

HRV readings in last 7 days (table calculation):
WINDOW_SUM(IIF(ISNULL([ln rMSSD]), 0, 1), -6, 0)

ln rMSSD 7-day mean (table calculation):
IF [HRV readings in last 7 days] >= 3 THEN WINDOW_AVG([ln rMSSD], -6, 0) END

ln rMSSD 7-day SD (table calculation):
IF [HRV readings in last 7 days] >= 3 THEN WINDOW_STDEV([ln rMSSD], -6, 0) END

ln rMSSD 7-day CV (%) (table calculation):
IF [ln rMSSD 7-day mean] > 0 THEN [ln rMSSD 7-day SD] / [ln rMSSD 7-day mean] * 100 END
```

Blanks behave this way in each tool:

- Power BI: a day with no valid reading gives a blank `ln rMSSD`. The window skips it and the count drops.
- Tableau: `WINDOW_AVG` and `WINDOW_STDEV` skip nulls. The count makes the minimum visible.

Build the weekly means and the band before import, in the spreadsheet or Python. Append the weekly means to `measures` as `hrv_ln_rmssd_week_mean`, and use the z-score measures in the `monitoring-statistics` skill.

### Calculate it in Python

Use this Python code with pandas and NumPy. It keeps one row per calendar day, so a missing reading does not stretch the window:

```python
import numpy as np
import pandas as pd

MIN_VALID = 3   # valid readings in a 7-day window (Plews et al., 2014)

def hrv_daily(d):
    """d: one athlete, columns date and rmssd_ms (NaN when no valid reading)."""
    d = d.set_index("date").asfreq("D")            # one row per calendar day
    d["ln_rmssd"] = np.log(d["rmssd_ms"].where(d["rmssd_ms"] > 0))
    win = d["ln_rmssd"].rolling(7, min_periods=1)  # today and the 6 days before
    d["n_7d"] = win.count()
    ok = d["n_7d"] >= MIN_VALID
    d["ln_rmssd_7d_mean"] = win.mean().where(ok)
    d["ln_rmssd_7d_sd"] = win.std().where(ok)      # sample SD
    d["ln_rmssd_7d_cv_pct"] = d["ln_rmssd_7d_sd"] / d["ln_rmssd_7d_mean"] * 100
    return d.reset_index()

def hrv_weekly(d):
    """d: output of hrv_daily, with the ln_rmssd column. Monday-to-Sunday means,
    blank with fewer than MIN_VALID readings."""
    w = d.set_index("date")["ln_rmssd"].resample("W-SUN").agg(["mean", "count"])
    w["mean"] = w["mean"].where(w["count"] >= MIN_VALID)
    return w.rename(columns={"mean": "ln_rmssd_week_mean", "count": "n_week"})
```

In R, use `log()` for ln rMSSD and `zoo::rollapply()` with `width = 7` on a complete daily calendar. Apply the same minimum of 3.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Confirm the reading conditions: time after waking, position, recording length, and device.
2. Mark each reading valid or not, with the rule set with the user.
3. Keep one valid rMSSD per athlete per day, in ms.
4. Build a full calendar of days for each athlete. Leave days with no valid reading blank.
5. Take the natural log of each daily rMSSD.
6. For each day, count the valid ln rMSSD values in the 7 days ending that day.
7. If the count is below 3, leave the 7-day mean, SD, and CV blank, and say why.
8. Compute the 7-day mean, the sample SD, and the CV.
9. Compute a mean for each Monday-to-Sunday week with at least 3 valid readings.
10. Build the usual-variation band from the prior weekly means, as above.
11. Compare the current 7-day mean with the band. Report n, the band, and its multiplier.
12. Show the single-day value as context only.

## Worked example

This example uses one made-up athlete. Every number below came from running the calculation in Python. Readings are supine, on waking, from the same chest strap.

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| rMSSD (ms) | 72 | none | 65 | 81 | none | 58 | 69 |
| ln rMSSD | 4.2767 | none | 4.1744 | 4.3944 | none | 4.0604 | 4.2341 |

Step 1. On day 3, the window holds 2 valid readings. The 7-day mean is blank.

Step 2. On day 4, the window holds 3 readings. The 7-day mean is 4.2818.

Step 3. On day 7, the window holds 5 readings. The 7-day mean is 4.2280, the SD is 0.1236, and the CV is 0.1236 / 4.2280 × 100 = 2.922%.

Step 4. This week is also a Monday-to-Sunday week, so the weekly mean is 4.2280, from 5 readings.

Step 5. The 10 prior weekly means are 4.31, 4.25, 4.36, 4.28, 4.33, 4.22, 4.30, 4.35, 4.27, and 4.29. Their mean is 4.2960 and their SD is 0.0438.

Step 6. The multiplier is t(9) × √(1 + 1/10) = 2.2622 × 1.0488 = 2.3726. The half-width is 2.3726 × 0.0438 = 0.1038. The usual-variation band runs from 4.1922 to 4.3998.

Step 7. The week's mean of 4.2280 is 0.068 below the baseline mean, a z-score of −1.553. It sits inside the band.

Step 8. The single reading on day 6, 4.0604, is the lowest of the week. Show it as context only. The band is built from weekly means, so it does not apply to one reading.

Step 9. Shown here because the user asked for the method in Plews et al. (2012): the 14 made-up baseline days are 4.41, 4.18, 4.30, 4.52, 4.12, 4.27, 4.36, 4.22, 4.45, 4.19, 4.33, 4.28, 4.40, and 4.16. Their mean is 4.2993 and their SD is 0.1189. The Plews band runs from 4.2399 to 4.3587. The week's mean sits below this band.

Result: the 7-day mean ln rMSSD is 4.228 (CV 2.92%, 5 readings). It is inside the athlete's usual-variation band from 10 prior weeks. It is below the study band of Plews et al. (2012), shown on request. The two bands answer different questions, so name the band with the result.

## What changes the number

These choices change the result even when the athlete has not changed:

- Order of log and mean. The mean of ln rMSSD in the worked example is 4.2280. The log of the mean rMSSD is 4.2341.
- Single day or rolling mean. In the worked example, day 6 is 0.168 below the 7-day mean.
- Band type. The usual-variation band and the Plews band disagree on the same week in the worked example.
- Minimum readings. Requiring 3 readings leaves day 3 blank. Requiring 1 would report a mean from 2 readings.
- Position, recording length, and the part of the recording analysed. Keep them the same (Buchheit, 2014).
- Device and app. Overnight wearable HRV and a morning chest-strap reading are different measures.
- Heat and hydration. Increases in plasma volume, usual after intense aerobic exercise and heat acclimatization, tend to raise beat-to-beat HRV without clear changes in fatigue or fitness (Buchheit, 2014).
- HRV index. Choose one index and keep it. Plews et al. (2013) recommend choosing one vagal HRV index and prefer ln rMSSD.

## Units and typical range

ln rMSSD has no unit. rMSSD is in ms. The CV is in percent.

| Population | Value | Source |
|---|---|---|
| Two elite triathletes, on waking, last 5 min of 6 min supine | rMSSD 211.2 ± 29.7 ms (man) and 130.8 ± 44.6 ms (woman), mean ± SD across days | Plews et al., 2012 |

No population range in this file rates an athlete. Use the athlete's own history. The values above show that rMSSD differs widely between athletes.

Use this test variability to judge a change, and state that it may not match your protocol:

- Buchheit (2014) gives a typical error, expressed as a CV, of about 12% for resting ln rMSSD, and an SWC of about +3%.
- Day-to-day changes in training load bring large daily changes in ln rMSSD, with a CV of 10% to 20% (Buchheit, 2014).
- These CVs are not the same quantity as the 7-day CV in this file, which is the CV of daily ln values. Do not apply 12% to ln values. Applied to an ln rMSSD of about 4.2, it would give ±0.5, far wider than the weekly SD of 0.04 in the worked example.

Measure your own typical error when you can, as the `monitoring-statistics` skill describes.

Practice varies widely. In a survey of 137 top-division European soccer clubs, 36% used HRV, and the authors identified 24 HRV procedures (Rave et al., 2018).

## Data you need

Collect this data:

- Source: a chest strap, a finger or camera app, or a wearable, with one device per athlete.
- Sampling: one reading per day, on waking, under fixed conditions.
- Minimum data: 3 valid readings in each 7-day window (Plews et al., 2014). For the band, at least 10 prior weekly means is the offered default from the `monitoring-statistics` skill.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Averaging rMSSD in ms, then taking the log. Take the log of each day first.
- Reacting to one low reading. Lead with the 7-day mean.
- Filling a missing day with 0 or with the previous day's value. Leave it blank and count it.
- Using a window of 7 rows when days are missing. Use 7 calendar days.
- Building the band from overlapping rolling means. Use weekly means.
- Mixing overnight wearable HRV with morning readings, or two devices, in one trend.
- Calling the Plews band a noise band, or applying 0.5 × SD as a recommendation.
- Calling a low HRV a sign of illness, overtraining, or injury risk.

## Example request

> Here are our players' morning HRV readings from the last 12 weeks. Can you add a 7-day rolling ln rMSSD and flag anyone outside their normal range in Google Sheets?

## Check the result

Run these checks:

- Recompute one value by hand: LN(65) = 4.1744.
- Check the size of ln rMSSD. Values between about 2 and 6 match rMSSD of about 7 to 400 ms. This range is this repository's plausibility choice, not a published range. A value near 65 means rMSSD was not logged. A negative value means rMSSD was in seconds.
- Check that no 7-day mean comes from fewer than 3 readings.
- Check that the window covers 7 calendar days, not 7 rows.
- Check that every reading in one trend used the same position and device.
- Check that the current week is not in its own baseline.

## Sources

This file draws on these sources:

- Plews DJ, Laursen PB, Kilding AE, Buchheit M. Heart rate variability in elite triathletes, is variation in variability the key to effective training? A case comparison. European Journal of Applied Physiology. 2012;112(11):3729-3741. https://doi.org/10.1007/s00421-012-2354-4 (full text read as Chapter Three of Plews DJ, The practical application of heart rate variability: monitoring training adaptation in world class athletes, doctoral thesis, Auckland University of Technology, 2014, https://hdl.handle.net/10292/7122, accessed 2026-10-07)
- Plews DJ, Laursen PB, Stanley J, Kilding AE, Buchheit M. Training adaptation and heart rate variability in elite endurance athletes: opening the door to effective monitoring. Sports Medicine. 2013;43(9):773-781. https://doi.org/10.1007/s40279-013-0071-8 (full text read as Chapter Six of the same thesis, accessed 2026-10-07)
- Plews DJ, Laursen PB, Le Meur Y, Hausswirth C, Kilding AE, Buchheit M. Monitoring training with heart rate-variability: how much compliance is needed for valid assessment? International Journal of Sports Physiology and Performance. 2014;9(5):783-790. https://doi.org/10.1123/ijspp.2013-0455 (abstract, accessed 2026-10-07)
- Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? Frontiers in Physiology. 2014;5:73. https://doi.org/10.3389/fphys.2014.00073 (accessed 2026-10-07)
- Rave G, Fortrat JO, Dawson B, Carre F, Dupont G, Saeidi A, Boullosa D, Zouhal H. Heart rate recovery and heart rate variability: use and relevance in European professional soccer. International Journal of Performance Analysis in Sport. 2018;18(1):168-183. https://doi.org/10.1080/24748668.2018.1460053 (abstract, accessed 2026-10-07)
