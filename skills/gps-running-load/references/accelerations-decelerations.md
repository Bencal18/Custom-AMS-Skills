# Accelerations and decelerations

Last checked: 2026-10-02

## What it measures

Acceleration and deceleration counts are how many times an athlete speeds up or slows down harder than a chosen rate, for at least a minimum time. Acceleration and deceleration distance is how far the athlete traveled during those efforts.

Of the common running load metrics from GPS, accelerations and decelerations show the most variability (Buchheit et al., 2014a). Read the "What changes the number" section before you compare any two values.

The data come from a GPS (global positioning system) unit worn by the athlete, a local positioning system (radio tracking installed in a venue), or video tracking. Speed is in km/h (kilometres per hour) or m/s (metres per second). Sampling rate is in Hz (hertz, samples per second).

## Formula

Calculate acceleration from the change in speed, then count efforts above the threshold:

```text
accel_m_s2[i] = (speed_m_s[i] − speed_m_s[i − k]) ÷ (k × Δt_s)
acceleration effort = a run of consecutive samples with accel_m_s2 ≥ threshold_m_s2,
                      lasting at least min_duration_s
deceleration effort = a run of consecutive samples with accel_m_s2 ≤ −threshold_m_s2,
                      lasting at least min_duration_s
effort_distance_m   = Σ (speed_m_s × Δt_s) over the samples in counted efforts
```

Define every term in the formula:

- `speed_m_s`: speed in metres per second (m/s). Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 before you calculate acceleration.
- `Δt_s`: the time between samples, in seconds. At 10 Hz, `Δt_s` is 0.1 s.
- `k`: how many samples back you look to calculate the change in speed. With `k = 1` at 10 Hz, the interval is 0.1 s. With `k = 2`, it is 0.2 s. Varley et al. (2017) compared 0.2 s and 0.3 s intervals.
- `accel_m_s2`: acceleration in metres per second squared (m/s²). Positive values are accelerations. Negative values are decelerations. If acceleration is in ft/s², multiply by 0.3048.
- `threshold_m_s2`: the acceleration threshold. See the list below.
- `min_duration_s`: the minimum effort duration, also called dwell time. It is the shortest time the athlete must stay beyond the threshold for the run to count. Measure a run as the number of samples × `Δt_s`. Harper et al. (2019) report 0.2 to 1 s across the studies that stated it: 4 of 19 studies in their results, 8 in their discussion.
- `effort_distance_m`: distance covered during counted efforts, in metres

This file uses one boundary rule: a sample counts when its absolute acceleration is at or above the lower bound and below the upper bound, if a band has one. Varley et al. (2017) used ≥ 2.78 m/s². Harper et al. (2019) wrote their thresholds as strictly above (> 2.5 m/s²).

The two rules differ only for samples exactly on the bound. Ask for the vendor's rule first, because vendors do not always publish it. State the rule you used.

These thresholds appear in published studies and device material:

- Above 2.5 m/s² for high intensity and above 3.5 m/s² for very high intensity, the thresholds Harper et al. (2019) pooled. The most common start threshold in their review was 3 m/s², used in 11 of 19 studies.
- 2.78 m/s² or more (Varley et al., 2017)
- 1.5 m/s² with a 0.5 s minimum duration, in a basketball study with wearable tags sampled at 20 Hz (Stone et al., 2022)
- Above 2 m/s², in a handball study with wearable tags (Carton-Llorente et al., 2023)
- Above 2 m/s², the default of one GPS vendor. The device files list vendor defaults.

There are two output variants:

- Count: the number of efforts. Use it for the number of hard speed changes.
- Distance or time: metres or seconds spent beyond the threshold. Harper et al. (2019) note, from earlier studies, that counts can be reliably obtained at 10 Hz, while distance and time variables are less reliable.

Use the software's counts when you only have a summary export. Record the threshold, minimum duration, and software version with them. Recalculate from raw speed only if the user asks, and never mix recalculated values with software values in one trend.

Use this Python code for raw speed samples:

```python
import numpy as np
def efforts(speed_m_s, hz, thr, min_s, k=1, sign=1, upper=np.inf):
    v = np.asarray(speed_m_s, dtype=float)          # accepts a list or a column
    a = np.full(len(v), np.nan)
    a[k:] = np.round((v[k:] - v[:-k]) * hz / k, 6)
    hit = (sign * a >= thr) & (sign * a < upper)     # at or above, below upper
    count, dist, run = 0, 0.0, []
    for i, h in enumerate(np.append(hit, False)):
        if h: run.append(i); continue
        if run and len(run) / hz >= min_s - 1e-9:    # run = samples × time step
            count += 1; dist += v[run].sum() / hz
        run = []
    return count, round(float(dist), 3)   # sign=-1 for decelerations
```

The snippet rounds acceleration to 6 decimals. Without rounding, floating-point noise in the computer's arithmetic can push a value that sits exactly on the threshold to either side.

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They follow the `efforts` function above. They take the change in speed over `k` samples, round acceleration to 6 decimals, and count a sample at or above the threshold and below the upper bound. They keep runs that last at least the minimum duration, and add speed × `Δt_s` over the samples in each kept run. A blank speed gives a blank acceleration, which ends a run, as `NaN` does in Python. A session with samples but no efforts gives 0, not a blank.

Both versions assume a `speed_samples` table with one row per sample: `athlete_id`, `session_id`, `sample_index` as a whole number, and `speed_m_s`. Convert speed to m/s before import. Keep one row for every sample, with a blank speed for a dropped sample. Like the Python function, both versions read samples by position, so a missing row joins the samples on either side as if they were 1 sample apart. Set the five settings once at the top: Hz, `k`, threshold, upper bound, and minimum duration. Use the same settings for every session in a trend, and label each result with them, the boundary rule, the filter, and the software version.

In Power BI, find the efforts in Power Query, not in DAX. Each acceleration needs the sample `k` places before it, and each run needs every sample before it in that run. Power Query works through each session's samples in order, once, at data refresh. The result is a static table, like a calculated column: it does not change with filters or slicers (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options). Select **New Source**, then **Blank Query**, open **Advanced Editor**, and paste this query. Name the query `efforts`:

```text
let
    hz = 10,
    k = 1,
    thr = 2.5,
    upper = #infinity,
    min_s = 0.2,
    Runs = (t as table) as table =>
        let
            sorted = Table.Sort(t, {{"sample_index", Order.Ascending}}),
            v = List.Buffer(sorted[speed_m_s]),
            a = List.Transform(
                List.Positions(v),
                each if _ < k or v{_} = null or v{_ - k} = null then null
                     else Number.Round((v{_} - v{_ - k}) * hz / k, 6)
            ),
            state = List.Transform(
                a,
                each if _ = null then "none"
                     else if _ >= thr and _ < upper then "accel"
                     else if -_ >= thr and -_ < upper then "decel"
                     else "none"
            ),
            runs = Table.Group(
                Table.FromColumns({state, v}, {"state", "speed_m_s"}),
                {"state"},
                {
                    {"samples", each Table.RowCount(_), Int64.Type},
                    {"distance_m", each List.Sum([speed_m_s]) / hz, type number}
                },
                GroupKind.Local
            )
        in
            Table.AddColumn(
                runs,
                "counted",
                each [state] <> "none" and [samples] / hz >= min_s - 0.000000001,
                type logical
            ),
    Grouped = Table.Group(speed_samples, {"athlete_id", "session_id"}, {{"runs", each Runs(_), type table}}),
    Expanded = Table.ExpandTableColumn(Grouped, "runs", {"state", "samples", "distance_m", "counted"}),
    efforts = Table.TransformColumnTypes(
        Expanded,
        {{"state", type text}, {"samples", Int64.Type}, {"distance_m", type number}, {"counted", type logical}}
    )
in
    efforts
```

The query works this way:

- `upper = #infinity` means no upper bound. For a band, set it to the upper bound in m/s².
- `_ < k or ...` stops the lookup before the first `k` samples. M evaluates the right side of `or` only when the left side is not true, and a negative list position raises an error (https://learn.microsoft.com/en-us/powerquery-m/m-spec-operators).
- `Number.Round` breaks ties to the even digit, as `np.round` does (https://learn.microsoft.com/en-us/powerquery-m/number-round).
- `GroupKind.Local` makes one group from each run of consecutive rows with the same state. Two runs with the same state stay separate groups (https://learn.microsoft.com/en-us/powerquery-m/groupkind-type and https://learn.microsoft.com/en-us/powerquery-m/table-group).
- `counted` marks the runs that last at least the minimum duration. The tiny allowance matches `- 1e-9` in Python, so a run of exactly 0.2 s counts.
- `Table.TransformColumnTypes` sets the four expanded columns to text, whole number, decimal number, and true/false (https://learn.microsoft.com/en-us/powerquery-m/table-transformcolumntypes). Without it, they have the type `any`. Power BI loads a column of type `any` as text (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types), so the DAX measures below cannot test `counted` or add `distance_m`.

The `efforts` table has one row per run, including runs with state `none`, so every session with samples has rows. Relate `athletes[athlete_id]` to `efforts[athlete_id]`, one to many, single direction. Relate `sessions[session_id]` to `efforts[session_id]` the same way, as the Power BI setup reference in the `ams-data-setup` skill does for `measures`. Put `sessions[session_date]` on the axis to trend the efforts by date. Show the results with one athlete and one session per row. Use these DAX measures. They are measures because they add the effort rows for the athlete and session in the visual:

```text
Accelerations =
IF (
    COUNTROWS ( efforts ) > 0,
    CALCULATE ( COUNTROWS ( efforts ), efforts[state] = "accel", efforts[counted] = TRUE () ) + 0
)

Acceleration distance (m) =
IF (
    COUNTROWS ( efforts ) > 0,
    CALCULATE ( SUM ( efforts[distance_m] ), efforts[state] = "accel", efforts[counted] = TRUE () ) + 0
)

Decelerations =
IF (
    COUNTROWS ( efforts ) > 0,
    CALCULATE ( COUNTROWS ( efforts ), efforts[state] = "decel", efforts[counted] = TRUE () ) + 0
)

Deceleration distance (m) =
IF (
    COUNTROWS ( efforts ) > 0,
    CALCULATE ( SUM ( efforts[distance_m] ), efforts[state] = "decel", efforts[counted] = TRUE () ) + 0
)
```

The `+ 0` turns no efforts into 0 only for a session that has samples. A session with no samples has no rows, so the result stays blank. Format the distances to 3 decimals, as the Python function rounds them.

In Tableau, put `athlete_id` and `session_id` on Rows and `sample_index` on Detail as a discrete dimension, sorted ascending. Filter to one session at a time with a filter on `session_id`, because the view has one mark per sample. A 90-minute session at 10 Hz has 54,000 marks. Never filter `sample_index`, because that cuts runs. Make these parameters: `Hz` as a float set to 10, `k` as an integer set to 1, `Threshold (m/s²)` set to 2.5, `Upper bound (m/s²)` set to 999 for no upper bound, and `Minimum duration (s)` set to 0.2. Use these calculations:

```text
Speed (m/s) (aggregate):
MIN([speed_m_s])

Acceleration (m/s²) (table calculation):
IF ISNULL([Speed (m/s)]) OR ISNULL(LOOKUP([Speed (m/s)], -[k])) THEN NULL
ELSE ROUND(([Speed (m/s)] - LOOKUP([Speed (m/s)], -[k])) * [Hz] / [k], 6)
END

Accel sample (table calculation):
IF NOT ISNULL([Acceleration (m/s²)]) AND [Acceleration (m/s²)] >= [Threshold (m/s²)]
   AND [Acceleration (m/s²)] < [Upper bound (m/s²)]
THEN 1 ELSE 0 END

Accel run samples (table calculation):
IF [Accel sample] = 1 THEN PREVIOUS_VALUE(0) + 1 ELSE 0 END

Accel run speed (table calculation):
IF [Accel sample] = 1 THEN PREVIOUS_VALUE(0) + [Speed (m/s)] ELSE 0 END

Accel effort ends here (table calculation):
IF [Accel run samples] > 0 AND ZN(LOOKUP([Accel sample], 1)) = 0
   AND [Accel run samples] / [Hz] >= [Minimum duration (s)] - 0.000000001
THEN 1 ELSE 0 END

Accelerations (table calculation):
WINDOW_SUM([Accel effort ends here])

Acceleration distance (m) (table calculation):
WINDOW_SUM(IIF([Accel effort ends here] = 1, [Accel run speed], 0)) / [Hz]

Decel sample (table calculation):
IF NOT ISNULL([Acceleration (m/s²)]) AND -[Acceleration (m/s²)] >= [Threshold (m/s²)]
   AND -[Acceleration (m/s²)] < [Upper bound (m/s²)]
THEN 1 ELSE 0 END
```

For decelerations, copy the five calculations after `Accel sample`, and replace `Accel` with `Decel` in each name and field.

The calculations work this way:

- `LOOKUP` returns null when the target sample is outside the session, so the first `k` samples have no acceleration, as in Python (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm).
- `PREVIOUS_VALUE(0)` returns the value of the same calculation on the previous sample, and 0 on the first sample of the session (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm). `Accel run samples` therefore counts the samples in the current run, and `Accel run speed` adds their speeds.
- `Accel effort ends here` is 1 on the last sample of a run that lasts at least the minimum duration. On the last sample of the session, `LOOKUP` returns null and `ZN` makes it 0, so a run that reaches the end still counts, as in Python.
- `WINDOW_SUM` with no offsets adds over the whole session.

Set **Compute Using** for every table calculation, including those used inside another one, to **Specific Dimensions**, with `sample_index` checked and `athlete_id` and `session_id` unchecked. Each session is then its own partition, and the calculations run along the samples in order (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm). Tableau lets you set **Compute Using** for each nested table calculation on its own, so set each one (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations_custom.htm).

The session totals repeat on every sample. To show one row per session, add a table calculation `First sample` with the formula `FIRST() = 0`, put it on Filters, and keep `True`. Tableau applies table calculation filters after the table calculations, so the totals still use every sample (https://help.tableau.com/current/pro/desktop/en-us/filtering.htm).

Blanks behave this way in each tool:

- Power BI: a null speed gives a null acceleration on that sample and on the sample `k` places after it. Their state is `none`, so the run splits there, as in Python.
- Tableau: a null speed gives a null acceleration on the same two samples, so `Accel sample` is 0 there and the run splits.
- Both: a text speed becomes null on import and counts as a dropped sample.
- Both: a session with no efforts gives 0 efforts and 0 m. A session with no samples gives a blank in Power BI and no row in Tableau.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the speed column and its unit.
2. Convert km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048 to get m/s.
3. Find the sampling rate in Hz and set `Δt_s = 1 ÷ Hz`.
4. Ask which interval to use for the change in speed (`k × Δt_s`) and whether a filter is applied first. Use the same choice for every file.
5. Calculate acceleration for each sample in m/s².
6. Ask for the threshold in m/s², and the vendor's boundary rule.
7. If the rule is not known, count a value equal to the threshold.
8. Mark samples at or above the threshold as acceleration samples.
9. Mark samples at or below the negative threshold as deceleration samples.
10. For a band, also stop at the upper bound.
11. Group consecutive marked samples into runs.
12. Ask for the minimum effort duration in seconds.
13. Measure each run as samples × `Δt_s`.
14. Keep runs that last at least the minimum effort duration. Each kept run is one effort.
15. Count the efforts.
16. For distance, add speed × `Δt_s` over the samples in each kept run.
17. Label each result with the threshold, boundary rule, minimum duration, interval, filter, and software version.

## Worked example

This example uses three seconds of one athlete's speed at 10 Hz (30 samples). The athlete starts a short sprint, brakes, and has one noisy sample. Every value below came from running the calculation in Python.

| Input | Value |
|---|---|
| Speed, m/s, samples 1 to 10 | 1.00, 1.30, 1.65, 2.00, 2.35, 2.62, 2.85, 3.05, 3.20, 3.30 |
| Speed, m/s, samples 11 to 20 | 3.38, 3.42, 3.44, 3.45, 3.20, 2.85, 2.50, 2.20, 2.00, 1.95 |
| Speed, m/s, samples 21 to 30 | 1.93, 2.20, 2.15, 2.10, 2.05, 2.00, 1.98, 1.97, 1.96, 1.95 |
| Sampling rate | 10 Hz, so `Δt_s` = 0.1 s |
| Interval for the change in speed | 0.1 s (`k` = 1) |
| Threshold | at or above 2.5 m/s² |
| Minimum effort duration | 0.2 s |

Follow these steps:

1. Calculate acceleration for each sample. For sample 2: (1.30 − 1.00) ÷ 0.1 = 3.0 m/s².
2. Samples at or above 2.5 m/s²:
   - Samples 2 to 6: 3.0, 3.5, 3.5, 3.5, 2.7 m/s². This run is 5 samples, so it lasts 0.5 s.
   - Sample 22: 2.7 m/s². This run lasts 0.1 s. It is a single noisy jump in speed from 1.93 to 2.20 m/s.
3. Samples at or below −2.5 m/s²:
   - Samples 15 to 18: −2.5, −3.5, −3.5, −3.0 m/s². This run lasts 0.4 s. Sample 15 sits exactly on the threshold and counts under the "at or above" rule.
4. Apply the 0.2 s minimum duration. The 0.5 s acceleration run counts. The 0.1 s run does not. The 0.4 s deceleration run counts.
5. Result: 1 acceleration and 1 deceleration.
6. Acceleration distance: speeds at samples 2 to 6 are 1.30, 1.65, 2.00, 2.35, 2.62 m/s. Each × 0.1 s gives 0.13, 0.165, 0.2, 0.235, 0.262 m. Total 0.992 m.
7. Deceleration distance: speeds at samples 15 to 18 are 3.20, 2.85, 2.50, 2.20 m/s. Each × 0.1 s gives 0.32, 0.285, 0.25, 0.22 m. Total 1.075 m.

Run the same 30 samples with one setting changed at a time to get these results:

| Setting changed | Accelerations | Acceleration distance | Decelerations | Deceleration distance |
|---|---|---|---|---|
| None (at or above 2.5 m/s², 0.2 s, 0.1 s interval) | 1 | 0.992 m | 1 | 1.075 m |
| Minimum duration 0.1 s | 2 | 1.212 m | 1 | 1.075 m |
| Minimum duration 0.5 s | 1 | 0.992 m | 0 | 0 m |
| Threshold at or above 3.5 m/s² | 1 | 0.600 m | 1 | 0.535 m |
| Interval 0.2 s (`k` = 2) | 1 | 1.147 m | 1 | 0.955 m |
| Strictly above 2.5 m/s² (`>`) | 1 | 0.992 m | 1 | 0.755 m |

The athlete did not change. Deceleration counts ranged from 0 to 1 and acceleration counts from 1 to 2 across these settings, and deceleration distance from 0 to 1.075 m. Distances are given to 3 decimals because several fall exactly halfway between 2-decimal values.

With a 0.2 s interval, the noisy sample 22 no longer reaches 2.5 m/s² (it becomes 1.25 m/s²).

## What changes the number

These choices change the result even when the athlete's performance does not:

- Threshold. In the worked example, at or above 3.5 m/s² keeps 1 acceleration but cuts its distance from 0.992 m to 0.600 m, because the peak was exactly 3.5 m/s². Under a strictly-above rule, 3.5 m/s² would count nothing.
- Minimum effort duration. In the worked example, 0.1 s counts a noise spike as a second acceleration, and 0.5 s drops the deceleration. Even 0.1 s changes in minimum duration can make substantial differences in effort counts (Harper et al., 2019). Effort counts decline steeply as minimum duration rises, with the largest declines for accelerations (Varley et al., 2017).
- Filtering and the interval used to calculate acceleration. In the worked example, a 0.2 s interval removes the noise spike. Different filters gave small to very large differences in acceleration counts when minimum duration was under 0.7 s (Varley et al., 2017).
- Software version. One manufacturer software update produced large decreases in acceleration counts with the same units (Buchheit et al., 2014a). Reprocessing old files with new software can change stored values. Record the software version and the processing date.
- Unit to unit. Between-unit variation, meaning how much two devices disagree on the same movement, reached 56% for decelerations above 4 m/s². Some units recorded 2 to 6 times more accelerations and decelerations than others of the same brand. That study used 50 units of one brand, from two 15 Hz models (15 and 35 units), on a towed sled (Buchheit et al., 2014a). Give each athlete the same unit every session.
- Model to model. The two models of the same brand differed substantially, for example a standardized difference of 2.1 for the number of accelerations above 4 m/s² (Buchheit et al., 2014a).
- Manufacturer and processing. Threshold-based acceleration and deceleration variables differed most between manufacturers. Software-derived and raw-processed data also differed for a range of movement variables (Thornton et al., 2019).
- Device type. In one comparison with youth soccer players aged 14 to 17, acceleration values were greater by small to very large amounts with local positioning than with camera or GPS tracking (Buchheit et al., 2014b).
- Sampling rate. In straight-line running, 10 Hz GPS measured instantaneous speed two to three times more accurately than 5 Hz during acceleration, deceleration, and constant speed (Varley et al., 2012). That study measured speed, not effort counts.
- End-of-effort rule. Some methods end an effort when acceleration falls below 0 m/s² or below a second threshold. No study in a 19-study meta-analysis reported this rule (Harper et al., 2019).
- Boundary rule. In the worked example, counting −2.5 m/s² as a deceleration sample gives 1.075 m of deceleration distance. A strictly-above rule gives 0.755 m.

## Units and typical range

Counts depend on the settings above, so no published count range transfers to another system. Compare each athlete with their own history on the same device, software version, and settings.

| Population | Value | Source |
|---|---|---|
| Common thresholds in elite team sport research | High intensity above 2.5 m/s². Very high intensity above 3.5 m/s². | Harper et al., 2019 |
| Minimum effort durations used in studies | 0.2 to 1 s, from the few studies that reported it: 4 of 19 in the results, 8 in the discussion | Harper et al., 2019 |
| High-intensity acceleration distance per full match | Australian football 194 m, soccer 178 m, rugby union 94 m | Harper et al., 2019 |
| High-intensity deceleration distance per full match | Soccer 162 m, Australian football 149 m, rugby union 54 m | Harper et al., 2019 |
| Match play in elite team sport, accelerations versus decelerations | More high and very high intensity decelerations than accelerations in every sport studied except American football | Harper et al., 2019 |
| Between-unit variation, 50 units of one brand, two 15 Hz models | Up to 56% for decelerations above 4 m/s² | Buchheit et al., 2014a |
| Between-unit variation, range across movement variables | Coefficient of variation 0.2% to 78.2% | Thornton et al., 2019 |

The coefficient of variation is the typical measurement error expressed as a percentage of the mean. Between-unit variation is how much two devices disagree when they record the same movement. It is not the test-retest error of one athlete on one unit.

## Data you need

Collect this data:

- Source: GPS, local positioning, or optical tracking. Raw speed samples if you need to recalculate. A summary export if you use the software's counts.
- Sampling: 10 Hz or faster for GPS. A 5 Hz rate is less reliable than 10 Hz for these metrics (Harper et al., 2019).
- Settings record: threshold, minimum effort duration, filter, interval for the change in speed, and software version for every file
- Minimum data: one session gives one value. A trend needs several sessions of the same type for that athlete with identical settings.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Comparing counts across devices, brands, or software versions. Some units counted 2 to 6 times more efforts than other units of the same brand (Buchheit et al., 2014a), and counts differed substantially between manufacturers (Thornton et al., 2019). Compare within one system and one software version.
- Recalculating counts from raw speed and joining them to the software's counts. Software-derived and raw-processed data differed substantially for a range of movement variables (Thornton et al., 2019). Use one method for the whole trend.
- Leaving out the minimum effort duration. A count without its minimum duration cannot be checked or compared. Report it with every count.
- Calculating acceleration from raw, unfiltered speed at 0.1 s intervals and calling every spike an effort. Noise creates false efforts, as sample 22 does in the worked example. Ask which filter or interval to use.
- Using the wrong units. Acceleration is in m/s². Convert speed in km/h or mph to m/s before you calculate acceleration. A change of 1 km/h over 0.1 s is 2.78 m/s², not 10. A change of 1 mph over 0.1 s is 4.47 m/s².
- Using a different boundary rule from the vendor. A value exactly on the threshold counts under `≥` and not under `>`. Ask for the vendor's rule, and state yours.
- Mixing threshold bands. "Above 2.5 m/s²" and "between 2.5 and 3.5 m/s²" are different metrics. Ask whether a band has an upper limit.
- Treating decelerations as negative accelerations in one total. Report accelerations and decelerations separately. Harper et al. (2019) found more high-intensity decelerations than accelerations in most team sports.
- Reporting distance or time beyond the threshold as if it were as reliable as counts. Distance and time variables are less reliable (Harper et al., 2019).
- Using a between-unit figure as one athlete's noise. The 56% between-unit variation (Buchheit et al., 2014a) applies only when the athlete changed to another unit of the same model. For an athlete on one unit, use a typical error from a short-term retest on that unit, in the same session type, and the noise band rules in SKILL.md (Hopkins, 2000; Swinton et al., 2018). The band for two single values is about 2.77 × the typical error, not 1 × it.

## Example request

> My GPS export has one row per player per session with columns for accelerations and decelerations above 3 m/s². We updated the software in March. Can you chart each player's decelerations per session for the season and flag big changes?

Status: not tested.

## Check the result

Run these checks:

- Confirm the threshold, minimum duration, and software version are the same for every value in a trend. If the software changed, split the trend at that date.
- Recalculate one effort by hand from the raw speed: change in speed ÷ interval, then check the run length against the minimum duration.
- Look for single-sample spikes in acceleration, like sample 22 in the worked example. Short spikes can come from measurement error and inflate counts when the minimum duration is short (Harper et al., 2019).

## Sources

These sources support the figures and methods in this file:

- Harper DJ, Carling C, Kiely J. High-intensity acceleration and deceleration demands in elite team sports competitive match play: a systematic review and meta-analysis of observational studies. Sports Med. 2019;49(12):1923-1947. https://doi.org/10.1007/s40279-019-01170-1
- Varley MC, Jaspers A, Helsen WF, Malone JJ. Methodological considerations when quantifying high-intensity efforts in team sport using global positioning system technology. Int J Sports Physiol Perform. 2017;12(8):1059-1068. https://doi.org/10.1123/ijspp.2016-0534
- Buchheit M, Al Haddad H, Simpson BM, Palazzi D, Bourdon PC, Di Salvo V, Mendez-Villanueva A. Monitoring accelerations with GPS in football: time to slow down? Int J Sports Physiol Perform. 2014;9(3):442-445. https://doi.org/10.1123/ijspp.2013-0187 Cited as Buchheit et al., 2014a.
- Thornton HR, Nelson AR, Delaney JA, Serpiello FR, Duthie GM. Interunit reliability and effect of data-processing methods of global positioning systems. Int J Sports Physiol Perform. 2019;14(4):432-438. https://doi.org/10.1123/ijspp.2018-0273
- Buchheit M, Allen A, Poon TK, Modonutti M, Gregson W, Di Salvo V. Integrating different tracking systems in football: multiple camera semi-automatic system, local position measurement and GPS technologies. J Sports Sci. 2014;32(20):1844-1857. https://doi.org/10.1080/02640414.2014.942687 Cited as Buchheit et al., 2014b.
- Varley MC, Fairweather IH, Aughey RJ. Validity and reliability of GPS for measuring instantaneous velocity during acceleration, deceleration, and constant motion. J Sports Sci. 2012;30(2):121-127. https://doi.org/10.1080/02640414.2011.627941
- Stone JD, Merrigan JJ, Ramadan J, Brown RS, Cheng GT, Hornsby WG, Smith H, Galster SM, Hagen JA. Simplifying external load data in NCAA Division-I men's basketball competitions: a principal component analysis. Front Sports Act Living. 2022;4:795897. https://doi.org/10.3389/fspor.2022.795897
- Carton-Llorente A, Lozano D, Gilart Iglesias V, Marcos Jorquera D, Manchado C. Worst-case scenario analysis of physical demands in elite men handball players by playing position through big data analytics. Biol Sport. 2023;40(4):1219-1227. https://doi.org/10.5114/biolsport.2023.126665
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Front Nutr. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
