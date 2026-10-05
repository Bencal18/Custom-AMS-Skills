# Total distance and distance per minute

Last checked: 2026-10-02

## What it measures

Total distance is how far an athlete traveled in a session or match. Distance per minute, also called relative distance, is that distance divided by the time it took, so you can compare sessions of different lengths.

The data come from a GPS (global positioning system) unit worn by the athlete, a local positioning system (radio tracking installed in a venue), or video tracking. Speed is in km/h (kilometres per hour) or m/s (metres per second). Sampling rate is in Hz (hertz, samples per second).

## Formula

Use total distance as reported by the device software when the file holds one summary row per athlete per session. When the file holds raw speed samples, add the distance covered in each sample. When it holds raw positions, add the straight-line distance between consecutive positions:

```text
from speed:      total_distance_m = Σ (speed_m_s × dt_s)
from positions:  total_distance_m = Σ √((x[i] − x[i−1])² + (y[i] − y[i−1])²)
distance_per_min = total_distance_m ÷ duration_min
```

Define every term in the formula:

- `speed_m_s`: the athlete's speed in one sample, in metres per second (m/s). Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 first.
- `dt_s`: the time between samples, in seconds. Take it from the timestamp differences. At 10 Hz (10 samples per second), it is 0.1 s.
- `x`, `y`: the athlete's position in metres on the field or court axes
- `total_distance_m`: distance in metres (m)
- `duration_min`: the time you divide by, in minutes. Choose one rule and keep it: whole session, time on the field, or drill time only.
- `distance_per_min`: relative distance in metres per minute (m/min)

The three distance methods do not give the same number. Position noise adds small sideways steps, so summed positions overestimate distance unless the positions are filtered.

A distance you recalculate will not match the vendor total or the odometer. Software-derived and raw-processed data differed substantially for a range of movement variables (Thornton et al., 2019). Use one method for the whole trend.

There are two variants of distance per minute:

- Whole-session average: total distance divided by the full duration. Use this to compare sessions or matches of different lengths.
- Peak period: the highest distance per minute in any window of a set length, such as 1 or 5 minutes. This answers a different question, the most intense passage of play. Do not mix it with the whole-session average.

A peak period can use rolling or fixed windows. A rolling window starts at every sample. A fixed window starts only at set times, such as every 5 minutes.

Fixed 5-minute periods underestimated peak high-velocity running distance by up to 25% compared with rolling periods (Varley et al., 2012). Over 60 s to 600 s windows, fixed epochs underestimated rolling averages by about 7% to 10% for total distance and about 12% to 25% for distance above 5.5 m/s (Fereday et al., 2020).

Always state the window length and whether it is rolling or fixed. Never compare a rolling value with a fixed value.

Use this spreadsheet formula, with total distance in metres in column `C` and minutes in column `D`. It returns a blank when either input is blank or not a number, instead of 0 m/min for a blank distance:

```text
=IF(COUNT(C2,D2)<2,"",C2/D2)
```

Use this Python code for raw speed samples with a `time_s` column. The duration comes from the user's duration rule, in a table `durations` with one row per athlete and session:

```python
hz = 10                                        # ask the user; check it against the timestamps
g = ["athlete_id", "session_id"]
df = df.sort_values(g + ["time_s"])
df["speed_m_s"] = df["speed_kmh"] / 3.6
df["dt_s"] = df.groupby(g)["time_s"].diff().fillna(1 / hz)   # first sample: one step
df["gap"] = df["dt_s"] > 1.5 / hz              # snippet choice: a step over 1.5 × expected
df["dist_m"] = (df["speed_m_s"] * df["dt_s"]).where(~df["gap"], 0)
summary = df.groupby(g).agg(total_distance_m=("dist_m", "sum"), gaps=("gap", "sum"))
summary = summary.join(durations.set_index(g)["duration_min"])
summary["m_per_min"] = summary["total_distance_m"] / summary["duration_min"]
```

The snippet leaves out distance across a gap and counts the gaps. Report any session with gaps. The 1.5 × factor is a choice in this snippet, not a published rule.

### Calculate it in Power BI and Tableau

These versions return a blank when distance or duration is missing or duration is 0. They read only distance in metres and duration in minutes.

Both versions assume one row per athlete, session, and measure in a `measures` table. Total distance is `measure_name` `total_distance` in `m`. Duration is `duration_min` in `min`, under the one duration rule the user chose. Convert km to m on import. A distance in km gives a value 1,000 times too small.

In Power BI, use this DAX measure. It is a measure because distance and duration sit on two rows:

```text
Distance per minute (m/min) =
VAR dist =
    CALCULATE (
        SUM ( measures[value] ),
        measures[measure_name] = "total_distance",
        measures[unit] = "m",
        measures[status] = "ok"
    )
VAR mins =
    CALCULATE (
        SUM ( measures[value] ),
        measures[measure_name] = "duration_min",
        measures[unit] = "min",
        measures[status] = "ok"
    )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( measures[session_id] )
            && NOT ISBLANK ( dist ) && NOT ISBLANK ( mins ) && mins > 0,
        dist / mins
    )
```

The `HASONEVALUE` tests keep the result to one athlete and one session. Over a week, total distance divided by total minutes is a different number from the mean of each session's m/min. Choose one, and name it.

In Tableau, put `athlete_id` and `session_id` on the view. Use these aggregate calculations:

```text
Total distance (m):
SUM(IF [measure_name] = "total_distance" AND [unit] = "m" AND [status] = "ok" THEN [value] END)

Duration (min):
SUM(IF [measure_name] = "duration_min" AND [unit] = "min" AND [status] = "ok" THEN [value] END)

Distance per minute (m/min):
IF ISNULL([Total distance (m)]) OR ISNULL([Duration (min)]) THEN NULL
ELSEIF [Duration (min)] <= 0 THEN NULL
ELSE [Total distance (m)] / [Duration (min)]
END
```

Blanks behave this way in each tool:

- Power BI: a missing distance or duration gives a blank, and the `IF` returns blank, as the spreadsheet formula does.
- Tableau: `SUM` of no matching rows is null, so the `ISNULL` test is true and the result is null. The `<= 0` test stops a division by 0.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the distance column and its unit.
2. Convert kilometres to metres by multiplying by 1,000, and yards to metres by multiplying by 0.9144.
3. If the file holds raw samples instead of a distance column, find the speed column and its unit.
4. Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 to get m/s.
5. Find the sampling rate in Hz.
6. Take `dt_s` for each sample from the timestamp differences.
7. Flag any step longer than expected as a gap.
8. Multiply each speed sample by its `dt_s` to get the distance for that sample, in metres.
9. Add the sample distances for each athlete and session to get `total_distance_m`.
10. If the file holds positions only, add the straight-line distance between consecutive positions instead.
11. Label the result as recalculated from positions.
12. Choose the duration rule: whole session, time on the field, or drill time.
13. Convert the duration to minutes. A value of `hh:mm:ss` becomes `hh × 60 + mm + ss ÷ 60`.
14. Divide `total_distance_m` by `duration_min` to get `distance_per_min` in m/min.
15. Label each result with the distance method, the duration rule, the sampling rate, and the device type.

## Worked example

This example uses one player's summary row, one second of raw speed samples, and one second of raw positions. Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Total distance in the export | 6.42 km |
| Whole session duration | 01:15:30 |
| Time on the field | 62.0 min |
| Raw speed samples, 10 Hz, km/h | 18.0, 18.4, 18.9, 19.3, 19.8, 20.2, 20.5, 20.9, 21.2, 21.6 |
| Raw positions, 10 Hz, x in m | 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 |
| Raw positions, 10 Hz, y in m, with ±0.1 m noise | 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1, −0.1, 0.1 |

Follow these steps for the summary row:

1. Distance: 6.42 km × 1,000 = 6,420 m.
2. Whole session duration: 1 × 60 + 15 + 30 ÷ 60 = 75.5 min.
3. Distance per minute, whole session: 6,420 ÷ 75.5 = 85.0 m/min.
4. Distance per minute, time on the field: 6,420 ÷ 62.0 = 103.5 m/min.

The same player gives 85.0 m/min or 103.5 m/min depending on the duration rule. Neither is wrong. Label which one you used.

Follow these steps for the raw speed samples:

1. Convert to m/s by dividing by 3.6: 5.000, 5.111, 5.250, 5.361, 5.500, 5.611, 5.694, 5.806, 5.889, 6.000.
2. Multiply each by `dt_s` = 0.1 s and add: 5.52 m in one second.

Follow these steps for the raw positions:

1. The athlete runs in a straight line at 5 m/s, so the true distance is 5.0 m.
2. With noise, each step is √(0.5² + 0.2²) = 0.5385 m. Ten steps give 5.39 m.
3. The noise adds 7.7% to the distance, though the athlete ran no farther.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Duration rule. In the worked example, whole session time gives 85.0 m/min and time on the field gives 103.5 m/min for the same distance.
- Assumed sampling interval. Treating the 10 Hz samples in the worked example as 5 Hz (`dt_s` = 0.2 s) doubles the distance from 5.52 m to 11.04 m.
- Speed unit. Adding km/h values as if they were m/s gives 19.88 instead of 5.52 for the same second, 3.6 times too large.
- Distance method. Vendor totals, speed × time, odometer differences, and summed positions differ. In the worked example, ±0.1 m of position noise adds 7.7%.
- Sampling rate of the device. 5 Hz units were more valid than 1 Hz units (Jennings et al., 2010), and 10 Hz units were the most valid and reliable (Scott et al., 2016). Errors are largest for short, fast, or turning movements.
- Device type. GPS, local positioning, and video tracking measure the same movement differently. Total distance differences between systems were trivial to small in youth soccer players (Buchheit et al., 2014). In small-sided games, errors against a reference system were 2.2% to 4.0% (Linke et al., 2018).
- Unit to unit. Two units of the same model disagree on the same movement (Johnston et al., 2014; Thornton et al., 2019). Give each athlete the same unit every session, and record the unit ID.
- Software version and filter settings. Processing choices change the output, and manufacturer software differs from raw processing (Malone et al., 2017; Thornton et al., 2019). Reprocessing old files with new software or settings can change stored values. Record the software version and the processing date.
- Signal quality. Satellite count, signal dropouts, and device fit affect GPS output (Malone et al., 2017). GPS needs a view of the sky, so indoor venues and stadium roofs can weaken or block the signal. That last point is common practice guidance, not a study finding.
- Whole-session or peak-period distance per minute. A peak window is always at least as high as the session average. A rolling window gives a value at least as high as a fixed window of the same length.

## Units and typical range

Total distance depends on the sport, position, session type, and duration. No single range applies across them. Compare each athlete with their own history in the same session type.

| Population | Value | Source |
|---|---|---|
| Elite Australian football, match, 5 Hz GPS | 129 ± 17 m/min (mean ± standard deviation) | Varley et al., 2014 |
| Elite rugby league, match, 5 Hz GPS | 97 ± 16 m/min | Varley et al., 2014 |
| Elite soccer, match, 5 Hz GPS | 104 ± 10 m/min | Varley et al., 2014 |
| Professional soccer, worst-case relative total distance, rolling windows, 10 Hz | 190.1 ± 20.4 m/min over 60 s; 120.9 ± 13.1 m/min over 600 s | Fereday et al., 2020 |
| Measurement error, total distance, running circuit for team sport | Coefficient of variation (CV) 3.6%. The abstract does not say which sampling rate gave it. | Jennings et al., 2010 |
| Measurement error, total distance, 10 Hz units | Typical error 1.3% between units | Johnston et al., 2014 |
| Error against a reference system, small-sided games | 2.2% to 4.0% across GPS, local positioning, and video tracking | Linke et al., 2018 |

The coefficient of variation is the typical error expressed as a percentage of the mean. The error rows come from circuits and from units compared with each other. They are not the test-retest error of one athlete on one unit, so do not use them as that athlete's noise.

For illustration only: if 3.6% were the right typical error, the noise band would be ±9.98% for two single sessions and ±7.73% against a 5-session baseline mean. A typical error of 1.3% gives ±3.60% and ±2.79%. The SKILL.md file gives the formulas.

## Data you need

Collect this data:

- Source: a GPS unit, a local positioning system (indoor or stadium radio tracking), or optical tracking, with its export or API output
- Sampling: 10 Hz GPS gives more valid and reliable distance than 1 Hz or 5 Hz. Units at 15 Hz gave no added benefit over 10 Hz (Scott et al., 2016). Record the sampling rate with every file.
- Quality record: the unit ID, software version, and the signal quality fields the export provides. Malone et al. (2017) advise researchers to report satellite number and horizontal dilution of precision (HDOP), a measure of how satellite geometry affects position accuracy. No study cut-off for these fields is given here. Ask the user for their rule.
- Minimum data: one session gives one value. A trend needs several sessions of the same type for that athlete, on the same device type and software settings.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing units. Some exports report kilometres, yards, mph, or km/h. Convert to metres and m/s before you add or compare. A total in kilometres added to a total in metres is off by a factor of 1,000.
- Dividing by the wrong duration. Whole-session time, time on the field, and drill time give different metres per minute. State the rule, and use one rule for every row.
- Mixing whole-session and peak-period distance per minute. A peak 1-minute value is at least as high as the session average. Label which one you report.
- Comparing rolling and fixed peak periods. Fixed windows give lower peaks (Varley et al., 2012; Fereday et al., 2020). State the window length and type.
- Assuming the sampling interval. Do not assume 10 Hz. A 5 Hz file processed with `dt = 0.1 s` gives half the true distance. Take the time step from the timestamps.
- Ignoring gaps. A fixed time step hides dropouts. Flag every step longer than expected, and report the gap time.
- Mixing distance methods. Summed positions, speed × time, odometer differences, and vendor totals differ. Use one method for the whole trend (Thornton et al., 2019).
- Comparing values across device types as if they were the same. GPS, local positioning, and video tracking give different values for the same movement (Linke et al., 2018; Buchheit et al., 2014). Between-system differences in total distance were trivial to small, but they exist. Keep device type in the table and flag cross-system comparisons.
- Comparing values from different sampling rates. Lower sampling rates are less valid, most of all during fast running and changes of direction (Jennings et al., 2010; Scott et al., 2016). Johnston et al. (2014) advise against comparing 10 Hz and 15 Hz units.
- Ignoring software and setting changes. Filter settings and software versions change the output (Malone et al., 2017; Thornton et al., 2019). Record the software version with each export.
- Counting time with no signal as zero distance. A dropout makes total distance look low. Keep a quality flag per session, such as satellite count or signal quality where the export provides it (Malone et al., 2017).
- Using a between-unit or circuit error as one athlete's noise, or treating any change under a few percent as noise. Use the typical error and noise band rules in SKILL.md (Hopkins, 2000; Swinton et al., 2018). The band for two single values is about 2.77 × the typical error, not 1 × it.

## Example request

> I exported last week's GPS data to a spreadsheet. Each row is one player in one session, with total distance in kilometres and session duration as `hh:mm:ss`. Give me metres per minute for each row and a weekly total distance per player.

## Check the result

Run these checks:

- Recalculate two rows by hand: distance in metres divided by minutes. Confirm the result is in m/min.
- Confirm no session has negative distance, and that the duration is in minutes, not hours or a time-of-day value.
- Compare a full match or full session with the figures in the table for that sport. A value several times higher or lower usually means a unit or duration error.

## Sources

These sources support the figures and methods in this file:

- Varley MC, Gabbett T, Aughey RJ. Activity profiles of professional soccer, rugby league and Australian football match play. J Sports Sci. 2014;32(20):1858-1866. https://doi.org/10.1080/02640414.2013.823227
- Varley MC, Elias GP, Aughey RJ. Current match-analysis techniques' underestimation of intense periods of high-velocity running. Int J Sports Physiol Perform. 2012;7(2):183-185. https://doi.org/10.1123/ijspp.7.2.183
- Fereday K, Hills SP, Russell M, Smith J, Cunningham DJ, Shearer D, McNarry M, Kilduff LP. A comparison of rolling averages versus discrete time epochs for assessing the worst-case scenario locomotor demands of professional soccer match-play. J Sci Med Sport. 2020;23(8):764-769. https://doi.org/10.1016/j.jsams.2020.01.002
- Jennings D, Cormack S, Coutts AJ, Boyd L, Aughey RJ. The validity and reliability of GPS units for measuring distance in team sport specific running patterns. Int J Sports Physiol Perform. 2010;5(3):328-341. https://doi.org/10.1123/ijspp.5.3.328
- Johnston RJ, Watsford ML, Kelly SJ, Pine MJ, Spurrs RW. Validity and interunit reliability of 10 Hz and 15 Hz GPS units for assessing athlete movement demands. J Strength Cond Res. 2014;28(6):1649-1655. https://doi.org/10.1519/JSC.0000000000000323
- Scott MTU, Scott TJ, Kelly VG. The validity and reliability of global positioning systems in team sport: a brief review. J Strength Cond Res. 2016;30(5):1470-1490. https://doi.org/10.1519/JSC.0000000000001221
- Linke D, Link D, Lames M. Validation of electronic performance and tracking systems EPTS under field conditions. PLoS One. 2018;13(7):e0199519. https://doi.org/10.1371/journal.pone.0199519
- Buchheit M, Allen A, Poon TK, Modonutti M, Gregson W, Di Salvo V. Integrating different tracking systems in football: multiple camera semi-automatic system, local position measurement and GPS technologies. J Sports Sci. 2014;32(20):1844-1857. https://doi.org/10.1080/02640414.2014.942687
- Malone JJ, Lovell R, Varley MC, Coutts AJ. Unpacking the black box: applications and considerations for using GPS devices in sport. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-18-S2-26. https://doi.org/10.1123/ijspp.2016-0236
- Thornton HR, Nelson AR, Delaney JA, Serpiello FR, Duthie GM. Interunit reliability and effect of data-processing methods of global positioning systems. Int J Sports Physiol Perform. 2019;14(4):432-438. https://doi.org/10.1123/ijspp.2018-0273
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
