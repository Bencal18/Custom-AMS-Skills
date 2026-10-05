# High-speed running distance

Last checked: 2026-10-02

## What it measures

High-speed running distance is the distance an athlete covers while moving faster than a chosen speed threshold.

The number depends on the threshold as much as on the athlete. Treat the threshold as part of the metric's name.

The data come from a GPS (global positioning system) unit worn by the athlete, a local positioning system (radio tracking installed in a venue), or video tracking. Speed is in km/h (kilometres per hour) or m/s (metres per second). Sampling rate is in Hz (hertz, samples per second).

## Formula

Add the distance of every sample at or above the speed threshold. For a band with an upper limit, count samples at or above the lower bound and below the upper bound:

```text
hsr_distance_m = Σ (speed_m_s × dt_s)   for samples where speed_m_s ≥ threshold_m_s
band_distance_m = Σ (speed_m_s × dt_s)  for samples where lower_m_s ≤ speed_m_s < upper_m_s
threshold_m_s  = threshold_km_h ÷ 3.6, or threshold_mph × 0.44704
```

Define every term in the formula:

- `speed_m_s`: the athlete's speed in one sample, in metres per second (m/s)
- `dt_s`: the time between samples, in seconds. At 10 Hz, `dt_s` is 0.1 s.
- `threshold_m_s`: the speed threshold in m/s. Thresholds are often published in km/h. Divide by 3.6 to convert. Multiply mph by 0.44704, or ft/s by 0.3048.
- `lower_m_s`, `upper_m_s`: the lower and upper bounds of a speed band, in m/s
- `hsr_distance_m`: the distance covered at or above the threshold, in metres (m)

This file uses one boundary rule: a sample counts when it is at or above the lower bound and below the upper bound. Varley et al. (2017) used ≥ 4.17 m/s and ≥ 7.00 m/s. Half-open bands count each sample in exactly one band.

Ask for the vendor's rule first, because vendors do not always publish it. Round speed and threshold to the same number of decimals before you compare them, so floating-point noise does not move a sample across the line.

There are two threshold variants:

- Absolute threshold: one speed for every athlete, such as 19.8 km/h. Use it to compare athletes against one fixed line, and to compare with published data that used the same line.
- Individualized threshold: a speed set per athlete. Use it when you want each athlete's distance above their own hard-running speed. Two methods appear in the studies cited here:
  - Ventilatory threshold. Abt and Lovell (2009) used each player's running speed at the second ventilatory threshold, a breathing-based marker of hard effort measured on a treadmill test.
  - Percentage of maximum speed. Reardon et al. (2015) set high-speed running at 60% of each player's maximum speed, taken from all training and match data over a season.

These absolute thresholds appear in published studies:

- 19.8 km/h (5.5 m/s): the default high-intensity threshold of one camera-based match analysis system (Abt and Lovell, 2009)
- 14.4 km/h (4.0 m/s): high-intensity running in a comparison of tracking systems with youth soccer players aged 14 to 17 (Buchheit et al., 2014)
- 14.0 to 19.99 km/h for high-speed running, and above 20.0 km/h for very high-speed running (Johnston et al., 2014)
- 4.17 m/s (15.0 km/h) for high-speed running, and 7.00 m/s (25.2 km/h) for sprinting (Varley et al., 2017)

No standard threshold exists across sports. A systematic review found speed zone definitions varied widely within and between sports (Cummins et al., 2013).

High-speed running can also be counted as efforts. An effort is one continuous stretch at or above the threshold that lasts at least a minimum time, often called the minimum effort duration or dwell time. Effort counts change with filtering and dwell time (Varley et al., 2017).

This file measures a run's length as the number of samples × `dt_s`. Some software measures from the first to the last sample, (n − 1) × `dt_s`. The two rules give different effort counts, so ask which one the software uses.

Use this spreadsheet formula, with speed in km/h in column `B`, the threshold in km/h in cell `F1`, and 10 Hz data. It returns a blank when the threshold is blank or not a number, when column `B` holds no speeds, or when any speed cell holds text, such as a dropout code:

```text
=IF(OR(NOT(ISNUMBER(F1)),COUNT(B2:B5001)=0,COUNTA(B2:B5001)>COUNT(B2:B5001)),"",SUMPRODUCT((B2:B5001>=F1)*(B2:B5001/3.6)*0.1))
```

Adjust the range `B2:B5001` to the rows in your file.

Use this Python code, with a `time_s` column. Run length is the number of samples × `dt_s`:

```python
hz, threshold_kmh, min_s = 10, 19.8, 0.5          # ask the user for all three
g = ["athlete_id", "session_id"]
df = df.sort_values(g + ["time_s"])
df["speed_m_s"] = (df["speed_kmh"] / 3.6).round(6)
thr = round(threshold_kmh / 3.6, 6)                # round both before comparing
df["above"] = df["speed_m_s"] >= thr
df["hsr_m"] = df["speed_m_s"].where(df["above"], 0) / hz
hsr = df.groupby(g)["hsr_m"].sum()
df["run"] = (df["above"] != df.groupby(g)["above"].shift()).cumsum()
run_s = df[df["above"]].groupby(g + ["run"]).size() / hz
efforts = (run_s >= min_s - 1e-9).groupby(level=g).sum().reindex(hsr.index, fill_value=0)
```

### Calculate it in Power BI and Tableau

These versions follow the boundary rule in this file: a sample counts when it is at or above the threshold. They round speed and threshold to 6 decimals in m/s before comparing, as the Python code does. They return a blank when an individualized threshold is missing. A what-if parameter in Power BI and a parameter in Tableau always hold a value, so set it on purpose and print it with the result.

Both versions assume a `gps_samples` table with one row per sample: `athlete_id`, `session_id`, `time_s`, and `speed_kmh`. Ask the user for the sampling rate. The code below uses 10 Hz. Show the result with one athlete and one session per row.

The threshold comes from one of two places. For an absolute threshold, use a numeric what-if parameter in Power BI, or a parameter in Tableau. For an individualized threshold, use a column `hsr_threshold_kmh` in the `athletes` table. In Power BI, relate `athletes[athlete_id]` to `gps_samples[athlete_id]`, one to many, single direction, and put `athletes[athlete_id]` in the visual.

In Power BI, use this DAX measure. It is a measure, not a calculated column, because the threshold can change with a slicer, and a calculated column only changes on refresh:

```text
HSR distance (m) =
VAR thr = [HSR threshold (km/h)]
VAR hz = 10
VAR thr_ms = ROUND ( thr / 3.6, 6 )
VAR samples = COUNT ( gps_samples[speed_kmh] )
RETURN
    IF (
        NOT ISBLANK ( thr ) && samples > 0,
        SUMX (
            FILTER (
                gps_samples,
                NOT ISBLANK ( gps_samples[speed_kmh] )
                    && ROUND ( gps_samples[speed_kmh] / 3.6, 6 ) >= thr_ms
            ),
            gps_samples[speed_kmh] / 3.6 / hz
        ) + 0
    )
```

`[HSR threshold (km/h)]` is the what-if parameter value, or `SELECTEDVALUE ( athletes[hsr_threshold_kmh] )` for an individualized threshold. The `+ 0` reports 0 m when the session has samples but none above the threshold. That is a real 0.

In Tableau, make a parameter `Sample rate (Hz)` set to 10. For an individualized threshold, join `athletes` to `gps_samples` on `athlete_id` in the physical layer, so each sample row carries the threshold. Use this row-level calculation, then `SUM` it with `athlete_id` and `session_id` on the view:

```text
HSR distance per sample (m):
IF ISNULL([hsr_threshold_kmh]) OR ISNULL([speed_kmh]) THEN NULL
ELSEIF ROUND([speed_kmh] / 3.6, 6) >= ROUND([hsr_threshold_kmh] / 3.6, 6)
THEN [speed_kmh] / 3.6 / [Sample rate (Hz)]
ELSE 0
END
```

Replace `[hsr_threshold_kmh]` with a parameter for an absolute threshold.

Blanks behave this way in each tool:

- Power BI: a blank threshold returns a blank result. A blank speed sample adds nothing. Without the `NOT ISBLANK` test, a blank speed compares as 0, which is below any threshold, so it also adds nothing. The test keeps the intent visible.
- Tableau: a null threshold makes every row null, and `SUM` of only nulls is null. A null speed sample is null and `SUM` ignores it.
- Both: a text dropout code in the speed column becomes null on import, so it adds nothing. The spreadsheet formula returns a blank for the whole session instead. Count the dropout samples, because a dropout silently shortens the distance.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the speed column and its unit.
2. Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 to get m/s.
3. Ask for the threshold and its unit.
4. Convert the threshold to m/s.
5. Ask whether the threshold is absolute or individualized.
6. For individualized thresholds, join each athlete's own threshold to their rows by athlete ID.
7. Find the sampling rate in Hz and set `dt_s = 1 ÷ Hz`.
8. Check the sampling rate against the timestamps.
9. Ask for the vendor's boundary rule.
10. If the rule is not known, mark each sample at or above the threshold, and below the upper bound for a band.
11. Multiply each marked sample's speed by `dt_s` to get its distance in metres.
12. Add the marked distances for each athlete and session.
13. If the user wants effort counts, group consecutive marked samples into runs.
14. Measure each run as samples × `dt_s`.
15. Count a run as an effort only if it lasts at least the minimum effort duration in seconds.
16. Label each result with the threshold, its unit, the threshold type, the boundary rule, and the minimum effort duration.

## Worked example

This example uses three seconds of one athlete's speed at 10 Hz (30 samples). Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Speed, km/h, samples 1 to 10 | 14.0, 15.5, 17.0, 18.5, 19.6, 20.4, 21.0, 21.3, 21.1, 20.6 |
| Speed, km/h, samples 11 to 20 | 19.9, 19.0, 18.2, 17.6, 17.9, 18.8, 19.9, 20.3, 20.1, 19.7 |
| Speed, km/h, samples 21 to 30 | 18.9, 17.8, 16.4, 15.2, 14.6, 14.1, 13.5, 13.0, 12.4, 11.8 |
| Sampling rate | 10 Hz, so `dt_s` = 0.1 s |
| Threshold | 19.8 km/h = 5.5 m/s |
| Minimum effort duration | 0.5 s |

Follow these steps:

1. Convert to m/s. The samples at or above 5.5 m/s are:
   - Samples 6 to 11: 5.667, 5.833, 5.917, 5.861, 5.722, 5.528 m/s
   - Samples 17 to 19: 5.528, 5.639, 5.583 m/s
2. Multiply each by 0.1 s and add. Samples 6 to 11 give 3.45 m. Samples 17 to 19 give 1.68 m.
3. High-speed running distance: 3.45 + 1.68 = 5.13 m.
4. The first run lasts 6 samples × 0.1 s = 0.6 s. The second lasts 3 samples × 0.1 s = 0.3 s.
5. With a 0.5 s minimum effort duration, only the first run counts: 1 effort.

Run the same 30 samples with other settings to get these results:

| Threshold | Minimum effort duration | Distance above threshold | Runs above threshold | Efforts |
|---|---|---|---|---|
| 19.8 km/h (5.5 m/s) | 0.5 s | 5.13 m | 0.6 s and 0.3 s | 1 |
| 19.8 km/h (5.5 m/s) | 0.3 s | 5.13 m | 0.6 s and 0.3 s | 2 |
| 15.0 km/h (4.167 m/s) | 0.5 s | 12.08 m | 2.3 s | 1 |
| 14.4 km/h (4.0 m/s) | 0.5 s | 12.48 m | 2.4 s | 1 |
| 60% of a 9.0 m/s maximum speed: 5.4 m/s (19.44 km/h) | 0.5 s | 6.22 m | 0.7 s and 0.4 s | 1 |
| 19.8 km/h, run length as (n − 1) × `dt_s` | 0.3 s | 5.13 m | 0.5 s and 0.2 s | 1 |

The athlete did not change. The distance more than doubled when the threshold dropped from 19.8 to 14.4 km/h. The effort count doubled when the minimum duration dropped from 0.5 to 0.3 s. With a 0.3 s minimum, the run length rule alone changes the count from 2 to 1.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Threshold speed. In the worked example, 19.8 km/h gives 5.13 m and 14.4 km/h gives 12.48 m from the same three seconds. In a match study, the same players covered 845 m above the default 19.8 km/h threshold and 2,258 m above their individualized threshold (Abt and Lovell, 2009).
- Threshold unit. A km/h threshold applied to m/s data catches almost nothing. In the worked example, 19.8 applied to m/s data selects 0 of 30 samples. A m/s threshold applied to km/h data selects everything: 5.5 applied to km/h data selects 30 of 30 samples. A threshold of 19.8 km/h is 12.3 mph.
- Absolute or individualized threshold. Individualized thresholds move each athlete's line, so the ranking of athletes can change. With an individualized threshold, forwards in elite rugby union covered more high-speed distance, and backs less, than with an absolute threshold (Reardon et al., 2015).
- Run length rule. Counting a run as n × `dt_s` or (n − 1) × `dt_s` changes effort counts, as the worked example shows.
- Minimum effort duration. It changes effort counts but not distance. In the worked example, 0.5 s gives 1 effort and 0.3 s gives 2. Effort counts drop as minimum duration rises (Varley et al., 2017).
- Speed filtering. Different velocity filters changed high-speed running effort counts when minimum duration was under 0.5 s (Varley et al., 2017).
- Sampling rate. Error grows as speed rises, and 10 Hz units are more valid than 1 Hz or 5 Hz units (Jennings et al., 2010; Scott et al., 2016; Johnston et al., 2014).
- Device type. All tracking technologies showed deviations above 40% from a reference system for high-speed distance (Linke et al., 2018). Camera tracking gave more distance above 14.4 km/h than local positioning or GPS in one comparison (Buchheit et al., 2014).
- Unit to unit. Typical error between 10 Hz and 15 Hz units grew with speed (Johnston et al., 2014). Give each athlete the same unit every session.
- Software reprocessing. Reprocessing old files with new software or new bands can change stored values. Record the software version and processing date.
- Boundary rule. A sample exactly on the threshold counts with `≥` and does not count with `>`. Use the vendor's rule when it is known. Otherwise use at or above the lower bound and below the upper bound, and state it.
- Match-to-match variation. The athlete's own running changes from match to match, apart from any device error. In English Premier League players tracked by a camera system, match-to-match CV was 16.2% for high-speed running and 30.8% for sprint distance (Gregson et al., 2010).

## Units and typical range

High-speed running varies with sport, position, session, and threshold. Report a range only with its threshold.

| Population | Value | Source |
|---|---|---|
| Professional soccer, match, camera tracking, threshold 19.8 km/h | 845 ± 296 m (mean ± standard deviation) | Abt and Lovell, 2009 |
| Same players, camera tracking, individualized threshold (median 15 km/h, range 14 to 16 km/h) | 2,258 ± 707 m | Abt and Lovell, 2009 |
| Elite rugby union, match, 10 Hz GPS, 60% of maximum speed | Forwards 354.72 ± 99.22 m. Backs 570.02 ± 171.14 m. | Reardon et al., 2015 |
| English Premier League, camera tracking, match-to-match variation | CV 16.2% for high-speed running, 30.8% for sprint distance | Gregson et al., 2010 |
| Measurement error, high-speed distance, any tracking technology | Above 40% deviation from a reference system | Linke et al., 2018 |
| Measurement error, 10 Hz and 15 Hz units, as speed rises | Typical error 0.8% to 19.9% | Johnston et al., 2014 |

Typical error is the measurement noise between two devices or two trials, expressed here as a percentage of the mean. The error rows compare units or systems. They are not the test-retest error of one athlete on one unit. Judge any change with the rules in SKILL.md.

## Data you need

Collect this data:

- Source: GPS, local positioning, or optical tracking, as raw speed samples or a summary export with distance in speed zones.
- Sampling: 10 Hz or faster for GPS. 15 Hz gave no added benefit over 10 Hz (Scott et al., 2016).
- Minimum data: one session gives one value. A trend needs several sessions of the same type for that athlete, on the same device type, settings, and threshold.
- Threshold record: the threshold value, unit, type, and the date it was set. For individualized thresholds, the test that set them.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Comparing values that used different thresholds. Distance above 14.4 km/h and distance above 19.8 km/h are different metrics. Confirm the thresholds match before you compare players, teams, seasons, or published data.
- Mixing km/h and m/s. A threshold of 5.5 is m/s. A threshold of 19.8 is km/h. Convert the threshold to the data's unit, or convert both to m/s.
- Assuming the export's "high-speed running" column uses the user's threshold. Speed zone definitions are not standardized within or between sports (Cummins et al., 2013). Ask what the zone boundaries are.
- Changing the threshold mid-season without marking it. A new threshold creates a step change that looks like a change in the athlete. Record the threshold and its date for every session.
- Comparing across systems. GPS, local positioning, and video give different high-speed distances for the same running (Buchheit et al., 2014; Linke et al., 2018). Do not join data from two systems into one trend without flagging it.
- Treating effort counts as stable. Counts change with filtering and minimum duration (Varley et al., 2017). Report the minimum duration with every count.
- Using an individualized threshold from an old test. Fitness changes. Record the test date, and ask before you use an old threshold. The "one training phase" cut-off some practitioners use is common practice, not a published rule.
- Mixing mph, km/h, and m/s. A threshold of 12.3 mph is 19.8 km/h and 5.5 m/s. Convert everything to m/s first.
- Reading a match-to-match change as a change in the athlete. High-speed running varies widely between matches for reasons other than fitness (Gregson et al., 2010). Use the noise band rules in SKILL.md, with a typical error from the same session type.
- Calling high-speed running distance "sprint distance". Sprint thresholds are higher. Use the user's labels and state the threshold.

## Example request

> I have 10 Hz GPS files for 22 players from Saturday's match. Speed is in km/h. Give me each player's distance above 19.8 km/h and above 25.2 km/h, and the number of efforts above 25.2 km/h that last at least 1 second.

## Check the result

Run these checks:

- Confirm high-speed running distance is no more than total distance for every athlete and session.
- Confirm distance above a higher threshold is no more than distance above a lower threshold for the same session.
- Recalculate one short run of samples by hand: speed in m/s × 0.1 s at 10 Hz, added over the samples at or above the threshold.

## Sources

These sources support the figures and methods in this file:

- Abt G, Lovell R. The use of individualized speed and intensity thresholds for determining the distance run at high-intensity in professional soccer. J Sports Sci. 2009;27(9):893-898. https://doi.org/10.1080/02640410902998239
- Buchheit M, Allen A, Poon TK, Modonutti M, Gregson W, Di Salvo V. Integrating different tracking systems in football: multiple camera semi-automatic system, local position measurement and GPS technologies. J Sports Sci. 2014;32(20):1844-1857. https://doi.org/10.1080/02640414.2014.942687
- Johnston RJ, Watsford ML, Kelly SJ, Pine MJ, Spurrs RW. Validity and interunit reliability of 10 Hz and 15 Hz GPS units for assessing athlete movement demands. J Strength Cond Res. 2014;28(6):1649-1655. https://doi.org/10.1519/JSC.0000000000000323
- Varley MC, Jaspers A, Helsen WF, Malone JJ. Methodological considerations when quantifying high-intensity efforts in team sport using global positioning system technology. Int J Sports Physiol Perform. 2017;12(8):1059-1068. https://doi.org/10.1123/ijspp.2016-0534
- Cummins C, Orr R, O'Connor H, West C. Global positioning systems (GPS) and microtechnology sensors in team sports: a systematic review. Sports Med. 2013;43(10):1025-1042. https://doi.org/10.1007/s40279-013-0069-2
- Jennings D, Cormack S, Coutts AJ, Boyd L, Aughey RJ. The validity and reliability of GPS units for measuring distance in team sport specific running patterns. Int J Sports Physiol Perform. 2010;5(3):328-341. https://doi.org/10.1123/ijspp.5.3.328
- Scott MTU, Scott TJ, Kelly VG. The validity and reliability of global positioning systems in team sport: a brief review. J Strength Cond Res. 2016;30(5):1470-1490. https://doi.org/10.1519/JSC.0000000000001221
- Linke D, Link D, Lames M. Validation of electronic performance and tracking systems EPTS under field conditions. PLoS One. 2018;13(7):e0199519. https://doi.org/10.1371/journal.pone.0199519
- Reardon C, Tobin DP, Delahunt E. Application of individualized speed thresholds to interpret position specific running demands in elite professional rugby union: a GPS study. PLoS One. 2015;10(7):e0133410. https://doi.org/10.1371/journal.pone.0133410
- Gregson W, Drust B, Atkinson G, Di Salvo V. Match-to-match variability of high-speed activities in premier league soccer. Int J Sports Med. 2010;31(4):237-242. https://doi.org/10.1055/s-0030-1247546
