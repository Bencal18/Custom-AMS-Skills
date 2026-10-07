# High-speed running distance

Last checked: 2026-10-07

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

## Build speed zones from test results

Individualized zones can come from a running test instead of a speed record. This section shows how to build zone edges from maximal aerobic speed. For how to calculate it from a field test, use the `conditioning-speeds` skill, if it is installed. A threshold as a percent of maximum speed is covered above, under the threshold variants.

Maximal aerobic speed (MAS) is the lowest running speed at which the athlete reaches their maximal oxygen uptake, in m/s. It comes from a running test. Build each zone edge as a fraction of MAS:

```text
edge_m_s = f × mas_m_s
```

Define every term in the formula:

- `mas_m_s`: maximal aerobic speed in m/s. Convert km/h ÷ 3.6.
- `f`: the fraction of MAS, such as 0.80 for "80% MAS" or 1.00 for MAS itself
- `edge_m_s`: one zone edge in m/s

This zone scheme appears in a published study. It is a study setting, not a recommendation:

- Moderate-speed running from 80% to 99.9% of MAS, with high-speed running starting at 100% of MAS. MAS was estimated from the distance in the Yo-Yo intermittent recovery test level 1 (Rago et al., 2019).

Some studies and vendors also set edges above MAS from the anaerobic speed reserve (ASR), the difference between maximal sprint speed and MAS (Rago et al., 2019; Gualtieri et al., 2023). The sources cited here do not write out how those edges are calculated, so this file gives no ASR-based edge. If the user follows such a scheme, ask for the exact formula, and show it next to every result.

Gualtieri et al. (2023) note that thresholds built from continuous running tests do not reflect the repeated accelerations of soccer. Treat zones from test results as one option. Ask the user which one they use.

Use this spreadsheet method. Put each athlete's test results on a sheet named `athletes`: `athlete_id` in column `A`, MAS in m/s in column `B`, and the test date in column `C`. Put `f` for the lower edge in cell `H1`. Then add these columns:

```text
D2 (lower edge, m/s):   =IF(ISNUMBER(B2),$H$1*B2,"")
E2 (MAS edge, m/s):     =IF(ISNUMBER(B2),B2,"")
```

Look up each athlete's edges next to their speed samples with `XLOOKUP` or `VLOOKUP`. Then use the band formula in this file with the athlete's own lower and upper edges. A blank test result gives a blank edge, and the band formula then returns a blank.

Use this Python code, after the HSR code above. `athletes` has `athlete_id` and `mas_m_s`:

```python
f = 0.80                                              # ask the user
athletes["edge_f"] = f * athletes["mas_m_s"]
athletes["edge_mas"] = athletes["mas_m_s"]
df = df.merge(athletes[["athlete_id", "edge_f", "edge_mas"]], on="athlete_id", how="left")
v = (df["speed_kmh"] / 3.6).round(6)
lf, lo = df["edge_f"].round(6), df["edge_mas"].round(6)
df["band_f_mas_m"] = (v / hz).where((v >= lf) & (v < lo), 0).where(lf.notna())
df["band_above_mas_m"] = (v / hz).where(v >= lo, 0).where(lo.notna())
zones = df.groupby(g)[["band_f_mas_m", "band_above_mas_m"]].sum(min_count=1)
```

`min_count=1` keeps a blank result for an athlete with no test, instead of 0 m.

In Power BI, add the edges as calculated columns in the `athletes` table, from column `mas_m_s`. Then point the threshold in the HSR distance measure above at the edge. Use these columns:

```text
Edge MAS (km/h) =
IF ( NOT ISBLANK ( athletes[mas_m_s] ), athletes[mas_m_s] * 3.6 )

Edge 80% MAS (km/h) =
VAR f = 0.80
RETURN IF ( NOT ISBLANK ( athletes[mas_m_s] ), f * athletes[mas_m_s] * 3.6 )
```

Use `SELECTEDVALUE ( athletes[Edge MAS (km/h)] )` as `[HSR threshold (km/h)]`. For a band, use the lower edge as the threshold and add the test `< upper edge` to the `FILTER`. The edges are columns, not measures, because they change only when a new test result arrives.

In Tableau, with `athletes` joined to `gps_samples` as above, use these calculations, and use `[Edge MAS (km/h)]` in place of `[hsr_threshold_kmh]`:

```text
Edge MAS (km/h):
IF ISNULL([mas_m_s]) THEN NULL ELSE [mas_m_s] * 3.6 END

Edge MAS fraction (km/h):
IF ISNULL([mas_m_s]) THEN NULL ELSE [MAS f] * [mas_m_s] * 3.6 END
```

`[MAS f]` is a parameter set to 0.80. A null MAS gives a null edge, and the distance calculation returns null.

This example applies MAS zones to the 30 samples in the worked example above. Every value below came from running the calculation in Python.

| Athlete | MAS | 80% MAS edge | MAS edge |
|---|---|---|---|
| A | 4.5 m/s | 3.600 m/s (12.96 km/h) | 4.500 m/s (16.20 km/h) |
| B | 4.0 m/s | 3.200 m/s (11.52 km/h) | 4.000 m/s (14.40 km/h) |

For athlete A: the lower edge = 0.80 × 4.5 = 3.6 m/s.

The same 30 samples give these band distances:

| Athlete | 80% to 100% MAS | At or above MAS |
|---|---|---|
| A | 7 samples, 2.78 m | 21 samples, 11.22 m |
| B | 6 samples, 2.19 m | 24 samples, 12.48 m |

The running did not change. Athlete B's lower MAS moves 3 more samples above MAS.

## Count top-speed exposure

Top-speed exposure is how often, and how far, an athlete runs close to their own maximal sprint speed. Count it per session and per week. It describes the running done. It does not predict any outcome.

Count efforts and distance at or above a percent of each athlete's MSS:

```text
threshold_m_s      = pct ÷ 100 × mss_m_s
top_speed_efforts  = runs of samples with speed_m_s ≥ threshold_m_s
                     lasting at least min_duration_s
top_speed_dist_m   = Σ (speed_m_s × dt_s) for samples where speed_m_s ≥ threshold_m_s
weekly_efforts     = Σ top_speed_efforts over the sessions in the week
```

Define every term in the formula:

- `pct`: the percent of MSS, such as 85, 90, or 95
- `mss_m_s`: the athlete's maximal sprint speed in m/s, from the source and date the user chose
- `min_duration_s`: the minimum effort duration in seconds. Measure a run as samples × `dt_s`, as above.
- `top_speed_dist_m`: distance at or above the threshold, from every sample at or above it, as for high-speed running distance above. Distance inside counted efforts only is a different number. Name which one you report.
- Week: the 7 days or the microcycle the user chose. State which.

These settings appear in published studies. They are study settings, not recommendations:

- Weekly counts at or above 80%, 85%, 90%, and 95% of each player's maximum, at 10 Hz (Dillon et al., 2024).
- Weekly efforts above 90% and above 95% of each player's maximum velocity, at 10 Hz, with a minimum effort duration (dwell time) of 0.6 s (Shah et al., 2022). Cite this study for its counting method only.
- Sprint entry at 80% to 85% of peak velocity from a sprint test, or above 80%, 85%, or 90% of the highest velocity from training or matches, as summarized by Gualtieri et al. (2023).

Shah et al. (2022) wrote their thresholds as strictly above (`>`). Dillon et al. (2024) wrote them as at or above (`≥`). Use the vendor's rule when known, and state it.

### Choose the maximal sprint speed

The MSS source changes the counts. Practitioners derive MSS from tests, training, and matches, in combination (Kyprianou et al., 2019). Choose one of these sources:

- A sprint test. Gualtieri et al. (2023) describe an all-out 30 to 40 m sprint after a standardized warm-up, measured with GPS, as a time-efficient method. Record the test date, distance, and device.
- The highest valid GPS value from training and matches. Players do not always reach their maximum in matches, because of the game and their position (Gualtieri et al., 2023). Rago et al. (2019) used the highest GPS speed over the study period.

In one study of 47 professional Australian football players, weekly counts were lower with MSS from in-season GPS monitoring than with MSS from a pre-season 3 × 50 m sprint test. The mean differences were 1.26 efforts per week at 80%, 0.78 at 85%, 0.42 at 90%, and 0.09 at 95%. The authors judged the effect meaningful at 80% and 85%, and somewhat trivial at 90% and 95% (Dillon et al., 2024). The direction of the difference depends on which MSS is higher. A lower MSS gives a lower threshold and more counts, as in the example below.

Follow these rules for the MSS value:

- Check a GPS maximum before you use it. Look at the speed trace around it, and reject a single-sample spike. Ask the user for their validity rule.
- Store the MSS value, its source, and its date with every count. A new maximum lowers every later count at the same percent.
- Do not recalculate old counts with a new MSS unless the user asks. If they do, show both versions.
- Use the same device type for MSS and for the sessions you count. In 12 elite youth soccer players, 10 Hz GPS gave a mean maximal sprinting speed of 8.75 m/s against 8.79 m/s from a laser, a mean difference of 0.04 m/s (Kyprianou et al., 2019).

Use this spreadsheet method on one session's samples, with speed in m/s in column `B`, the athlete's MSS in m/s in cell `K1`, the percent in `K2`, the sampling rate in `K3`, and the minimum duration in seconds in `K4`. Columns `C` to `F` mark the samples, count each run's length, mark counted efforts, and hold each sample's distance:

```text
K5 (threshold, m/s):  =IF(COUNT(K1,K2)<2,"",ROUND(K2/100*K1,6))
C2 (at or above):     =IF(OR($K$5="",NOT(ISNUMBER(B2))),0,IF(ROUND(B2,6)>=$K$5,1,0))
D2 (run length):      =IF(C2=1,N(D1)+1,0)
E2 (effort ends):     =IF(AND(C2=1,N(C3)=0,D2/$K$3>=$K$4-0.000000001),1,0)
F2 (distance, m):     =IF(C2=1,B2/$K$3,0)
K6 (efforts):         =IF($K$5="","",SUM(E:E))
K7 (distance, m):     =IF($K$5="","",SUM(F:F))
```

`D2` counts the samples in the current run. `N(D1)` treats the header as 0. `E2` marks the last sample of a run long enough to count. Fill `C2` to `F2` down to the last sample. A dropped sample ends a run. Add each session's count into a weekly total by athlete and week.

Use this Python code, after the HSR code above. `mss` has `athlete_id`, `mss_m_s`, `mss_source`, and `mss_date`. Use the same session rows as the HSR code:

```python
import pandas as pd

pcts, min_s = [85, 90, 95], 0.6                        # ask the user
df = df.merge(mss[["athlete_id", "mss_m_s"]], on="athlete_id", how="left")
v = (df["speed_kmh"] / 3.6).round(6)
out = []
for pct in pcts:
    thr = (pct / 100 * df["mss_m_s"]).round(6)
    above = (v >= thr) & thr.notna()
    run = (above != above.groupby([df[c] for c in g]).shift()).cumsum()
    runs = above[above].groupby([df[c] for c in g] + [run[above]]).size() / hz
    eff = (runs >= min_s - 1e-9).groupby(level=g).sum()
    dist = (v / hz).where(above, 0).groupby([df[c] for c in g]).sum()
    res = pd.DataFrame({"efforts": eff.reindex(dist.index, fill_value=0), "dist_m": dist})
    res.loc[df.groupby(g)["mss_m_s"].first().isna(), ["efforts", "dist_m"]] = None
    out.append(res.assign(pct=pct))
top = pd.concat(out).reset_index()
```

An athlete with no MSS gets a blank result, not 0. Join a week label to `top`, and add `efforts` and `dist_m` by athlete, week, and `pct`.

In Power BI, add `mss_m_s` to the `athletes` table. Make the threshold a measure from a what-if parameter `[Top speed %]`, and use it in the HSR distance measure above:

```text
Top speed threshold (km/h) =
VAR mss = SELECTEDVALUE ( athletes[mss_m_s] )
RETURN IF ( NOT ISBLANK ( mss ), [Top speed %] / 100 * mss * 3.6 )
```

Use `[Top speed threshold (km/h)]` as `[HSR threshold (km/h)]` to get distance at or above the threshold. For effort counts, use the Power Query `efforts` method in [accelerations-decelerations.md](accelerations-decelerations.md), with speed in place of acceleration: mark a sample when `speed_kmh ÷ 3.6` is at or above the athlete's threshold, group runs with `GroupKind.Local`, and keep runs that last at least the minimum duration. Store the percent and the MSS used with each row.

In Tableau, add `mss_m_s` to `athletes`, and make a parameter `Top speed %` set to 90. Use this calculation in place of `[hsr_threshold_kmh]` for distance:

```text
Top speed threshold (km/h):
IF ISNULL([mss_m_s]) THEN NULL ELSE [Top speed %] / 100 * [mss_m_s] * 3.6 END
```

For effort counts in Tableau, use the table calculations for `Accel sample`, `Accel run samples`, and `Accel effort ends here` in [accelerations-decelerations.md](accelerations-decelerations.md). Replace the acceleration test with `ROUND(MIN([speed_kmh]) / 3.6, 6) >= ROUND([Top speed %] / 100 * MIN([mss_m_s]), 6)`.

This example uses four seconds of one athlete's speed at 10 Hz (40 samples), with two sprints. Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Speed, m/s, samples 1 to 10 | 6.80, 7.20, 7.60, 7.90, 8.10, 8.30, 8.45, 8.55, 8.60, 8.60 |
| Speed, m/s, samples 11 to 20 | 8.55, 8.45, 8.30, 8.10, 7.80, 7.40, 7.00, 6.50, 6.00, 5.50 |
| Speed, m/s, samples 21 to 30 | 5.60, 6.20, 6.80, 7.30, 7.70, 7.95, 8.05, 8.10, 8.05, 7.90 |
| Speed, m/s, samples 31 to 40 | 7.60, 7.20, 6.80, 6.30, 5.80, 5.40, 5.00, 4.80, 4.60, 4.50 |
| MSS from a sprint test | 9.20 m/s |
| MSS from the highest valid GPS value | 8.90 m/s |
| Minimum effort duration | 0.6 s |

Follow these steps for 90% of the sprint test MSS:

1. Threshold: 0.90 × 9.20 = 8.28 m/s.
2. Samples 6 to 13 are at or above 8.28 m/s. The run lasts 8 × 0.1 = 0.8 s, so it counts as 1 effort.
3. No sample in the second sprint reaches 8.28 m/s. Its top speed is 8.10 m/s.
4. Distance at or above the threshold: the 8 speeds × 0.1 s, added, give 6.78 m.

The same 40 samples give these results:

| Percent of MSS | MSS from the sprint test | MSS from GPS |
|---|---|---|
| 80% | 7.360 m/s: 2 efforts, 17.005 m | 7.120 m/s: 2 efforts, 19.175 m |
| 85% | 7.820 m/s: 1 effort, 13.195 m | 7.565 m/s: 2 efforts, 16.265 m |
| 90% | 8.280 m/s: 1 effort, 6.780 m | 8.010 m/s: 1 effort, 10.820 m |
| 95% | 8.740 m/s: 0 efforts, 0.000 m | 8.455 m/s: 0 efforts, 3.430 m |

Distances are given to 3 decimals because several fall exactly halfway between 2-decimal values. The athlete did not change. At 85%, the MSS source alone changes the count from 1 to 2. At 95% with the GPS MSS, samples 8 to 11 reach the threshold for 0.4 s. That is too short for the 0.6 s minimum, so it adds 3.43 m but no effort. The example shows how the settings act. It does not show the size of the difference in a squad.

If the athlete's six sessions in a week give 0, 3, 2, 0, 1, and 4 efforts at 90%, the weekly count is 10. Report it with the percent, the MSS value and source, the minimum duration, and the week definition.

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
- Test results for MAS zones. A new test moves every edge. In the MAS example, a lower MAS puts 3 more samples above MAS for the same running.
- MSS source for top-speed exposure. In the top-speed example, the sprint test MSS gives 1 effort at 85% and the GPS MSS gives 2. Weekly counts differed most at 80% and 85% and least at 90% and 95% (Dillon et al., 2024).
- A new MSS. A higher maximum lowers every later count at the same percent. Record the MSS and its date with every count.
- Minimum effort duration for top-speed efforts. Near the top of an athlete's speed, runs are short. In the top-speed example, a 0.4 s run at 95% adds distance but no effort under a 0.6 s minimum.

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
| Italian Serie B soccer, 13 players, test results used for zones | MAS 17.7 ± 0.6 km/h from Yo-Yo intermittent recovery test level 1. MSS 31.1 ± 0.9 km/h, the highest GPS speed. | Rago et al., 2019 |
| Professional Australian football, 47 players, 10 Hz GPS, MSS from in-season monitoring against a pre-season sprint test | Weekly counts lower by 1.26 at 80%, 0.78 at 85%, 0.42 at 90%, and 0.09 at 95% of MSS | Dillon et al., 2024 |
| Elite youth soccer, 12 players, 40 m sprints, MSS from 10 Hz GPS against a 100 Hz laser | 8.75 ± 0.32 m/s against 8.79 ± 0.33 m/s. Mean difference 0.04 m/s (90% confidence interval −0.03 to 0.11). | Kyprianou et al., 2019 |

Typical error is the measurement noise between two devices or two trials, expressed here as a percentage of the mean. The error rows compare units or systems. They are not the test-retest error of one athlete on one unit. Judge any change with the rules in SKILL.md.

## Data you need

Collect this data:

- Source: GPS, local positioning, or optical tracking, as raw speed samples or a summary export with distance in speed zones.
- Sampling: 10 Hz or faster for GPS. 15 Hz gave no added benefit over 10 Hz (Scott et al., 2016).
- Minimum data: one session gives one value. A trend needs several sessions of the same type for that athlete, on the same device type, settings, and threshold.
- Threshold record: the threshold value, unit, type, and the date it was set. For individualized thresholds, the test that set them.
- Test record for MAS zones: each athlete's MAS, the test that gave it, and its date.
- MSS record for top-speed exposure: the value, its source (sprint test or GPS), its date, and the validity check used for a GPS value.
- Week definition: calendar week or microcycle, for weekly top-speed counts.

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
- Using an MSS from a single-sample GPS spike. Check the speed trace before you use a GPS maximum.
- Updating MSS without marking the date. Every later top-speed count shifts. Store the MSS and its date with each count.
- Comparing top-speed counts at different percents, or with MSS from different sources, as one trend.
- Describing top-speed exposure as a risk or a safe level. Report the count, the percent, and the MSS. The coach decides what it means.

## Example request

> I have 10 Hz GPS files for 22 players from Saturday's match. Speed is in km/h. Give me each player's distance above 19.8 km/h and above 25.2 km/h, and the number of efforts above 25.2 km/h that last at least 1 second.

## Check the result

Run these checks:

- Confirm high-speed running distance is no more than total distance for every athlete and session.
- Confirm distance above a higher threshold is no more than distance above a lower threshold for the same session.
- Recalculate one short run of samples by hand: speed in m/s × 0.1 s at 10 Hz, added over the samples at or above the threshold.
- For MAS zones, recalculate one athlete's edges by hand: f × MAS. Confirm the edges rise from band to band.
- For top-speed exposure, confirm the count at 95% is no more than the count at 90%, and so on down. Confirm the MSS value, source, and date appear with the result.

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
- Rago V, Brito J, Figueiredo P, Krustrup P, Rebelo A. Relationship between external load and perceptual responses to training in professional football: effects of quantification method. Sports. 2019;7(3):68. https://doi.org/10.3390/sports7030068 (accessed 2026-10-07)
- Gualtieri A, Rampinini E, Dello Iacono A, Beato M. High-speed running and sprinting in professional adult soccer: current thresholds definition, match demands and training strategies. A systematic review. Front Sports Act Living. 2023;5:1116293. https://doi.org/10.3389/fspor.2023.1116293 (accessed 2026-10-07)
- Dillon P, Lovell R, Joyce D, Norris D. Maximum speed exposures in Australian rules football: do methods matter? Sci Med Footb. 2024;8(3):287-290. https://doi.org/10.1080/24733938.2023.2211048 Read as an abstract only. The full text is paywalled. (accessed 2026-10-07)
- Shah S, Collins K, Macgregor LJ. The influence of weekly sprint volume and maximal velocity exposures on eccentric hamstring strength in professional football players. Sports. 2022;10(8):125. https://doi.org/10.3390/sports10080125 Cited for its counting method only. (accessed 2026-10-07)
- Kyprianou E, Lolli L, Al Haddad H, Di Salvo V, Varley MC, Mendez-Villanueva A, Gregson W, Weston M. A novel approach to assessing validity in sports performance research: integrating expert practitioner opinion into the statistical analysis. Sci Med Footb. 2019;3(4):333-338. https://doi.org/10.1080/24733938.2019.1617433 Read as an abstract only. (accessed 2026-10-07)

