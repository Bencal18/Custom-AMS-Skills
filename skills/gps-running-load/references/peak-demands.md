# Peak demands

Last checked: 2026-10-07

## What it measures

Peak demands are the highest amount of a measure an athlete produced in any window of a set length, such as 1, 3, 5, or 10 minutes. Studies also call them the most demanding passages, the most demanding scenarios, worst-case scenarios, or peak match demands. This file uses "peak demands".

This file covers three measures: distance, high-speed running distance, and acceleration efforts. It also covers two uses: a drill as a percent of each player's own match peak, and comparisons between positions.

The data come from a GPS (global positioning system) unit worn by the athlete, a local positioning system (radio tracking installed in a venue), or video tracking. Speed is in m/s (metres per second). Sampling rate is in Hz (hertz, samples per second).

## Formula

Add the measure over every window of `n` consecutive samples, and keep the highest sum. Divide by the window length in minutes to get a rate per minute:

```text
x[i]               = the measure in sample i (see the list below)
n                  = window_s × hz
window_sum[i]      = Σ x[j] for j = i − n + 1 to i
peak               = max of window_sum over every valid window
peak_per_min       = peak ÷ (window_s ÷ 60)
drill_pct_of_peak  = drill_per_min ÷ match_peak_per_min × 100
```

Define every term in the formula:

- `x[i]`: the value of the measure in one sample. For distance, it is `speed_m_s ÷ hz`, the metres covered in that sample. For high-speed running, it is `speed_m_s ÷ hz` when speed is at or above the threshold, and 0 otherwise. For acceleration efforts, it is 1 on the first sample of each counted effort, and 0 otherwise.
- `hz`: the sampling rate in samples per second. At 10 Hz, one sample is 0.1 s.
- `window_s`: the window length in seconds, such as 60, 180, 300, or 600
- `n`: the number of samples in one window. A 60 s window at 10 Hz is 600 samples.
- `window_sum[i]`: the total of the measure in the window that ends at sample `i`, in metres or a count
- `peak`: the highest `window_sum` in the period, in metres or a count
- `peak_per_min`: the peak as a rate, in m/min or efforts per minute
- `drill_per_min`: the drill's total for the measure divided by the drill's duration in minutes
- `match_peak_per_min`: the player's match peak per minute for the same measure, window length, and window type. See [Express a drill as a percent of the match peak](#express-a-drill-as-a-percent-of-the-match-peak).

A valid window has every sample present and lies inside one period of play, such as one half. A window that crosses half time, a substitution, or a gap in the data is not valid. The time from the first to the last sample in a valid window is `(n − 1) ÷ hz`.

This file counts an acceleration effort in the window that holds its first sample. An effort that starts in one window and ends in the next counts once, in the first. This is this file's choice, not a published rule. Find the efforts with the method in [accelerations-decelerations.md](accelerations-decelerations.md), and use the same threshold, minimum duration, and boundary rule as there. For high-speed running, use the threshold and boundary rule in [high-speed-running.md](high-speed-running.md).

### Use rolling windows, and state the type

[total-distance.md](total-distance.md#formula) already sets the rule for distance: state the window length and whether it is rolling or fixed, and never compare a rolling value with a fixed value. A rolling window starts at every sample. A fixed window starts only at set times, such as every 5 minutes.

Apply the same rule to high-speed running and acceleration efforts. In soccer, fixed windows underestimated rolling values by about 12% to 25% for distance above 5.5 m/s (Fereday et al., 2020), more than for total distance. A systematic review of the football codes found moving averages, meaning rolling windows, the most common method (63% of studies). They identified higher peak demands than other methods (Whitehead et al., 2018).

### Choose the window lengths

This file uses 1, 3, 5, and 10 minutes. Whitehead et al. (2018) summarized peak 1, 5, and 10 minute relative distances across the football codes. In basketball, the windows most often analyzed ran from 15 s to 10 minutes, and 30 s, 1, 2, and 5 minute windows were named the most practical (Pérez-Chao et al., 2023). These are study settings. Ask the user which windows they use.

A window longer than the time an athlete played gives no peak. Whitehead et al. (2018) note that for players on the field for less than 10 minutes, shorter windows matter more.

Pérez-Chao et al. (2023) describe one data rule for basketball: start the rolling windows at the beginning of each quarter and stop them at its end. Apply the same rule to each period in any sport.

### Use this spreadsheet method

Put one period of play for one athlete on its own sheet, with one row per sample. Use these columns and cells:

- Column `A`: `time_s`, the time of each sample in seconds
- Column `B`: `speed_m_s`, speed in m/s. Leave a dropped sample blank.
- Column `C`: the measure per sample, `x`
- Column `D`: the running total of `x`
- Column `E`: the running count of dropped samples
- Column `F`: the window sum that ends at that row
- Cell `K1`: the sampling rate in Hz. Cell `K2`: the window length in seconds. Cell `K3`: the high-speed threshold in m/s. Cell `K4`: the number of samples in a window.

Enter these formulas in row 2, and fill them down. For distance, use the first formula for column `C`. For high-speed running, use the second. For acceleration efforts, put 1 on the first sample of each counted effort, 0 on every other sample, and leave a dropped sample blank instead:

```text
K4:  =ROUND(K2*K1,0)
C2:  =IF(ISNUMBER(B2),B2/$K$1,"")
C2:  =IF(ISNUMBER(B2),IF(ROUND(B2,6)>=ROUND($K$3,6),B2/$K$1,0),"")
D2:  =N(C2)                          D3: =D2+N(C3)
E2:  =IF(ISNUMBER(C2),0,1)           E3: =E2+IF(ISNUMBER(C3),0,1)
F2:  =IF(ROW()-1<$K$4,"",
       IF(OR(E2-IF(ROW()-1=$K$4,0,INDEX(E:E,ROW()-$K$4))>0,
             ROUND(A2-INDEX(A:A,ROW()-$K$4+1),3)<>ROUND(($K$4-1)/$K$1,3)),"",
          D2-IF(ROW()-1=$K$4,0,INDEX(D:D,ROW()-$K$4))))
```

Fill `D3` and `E3` down from row 3. Then find the peak and the rate per minute:

```text
Peak:            =IF(COUNT(F:F)=0,"",MAX(F:F))
Peak per minute: =IF(COUNT(F:F)=0,"",MAX(F:F)/($K$2/60))
```

The formulas work this way:

- The running total turns each window sum into one subtraction: the total at the last sample minus the total just before the first sample. A long file stays fast.
- Column `F` is blank when a window holds a dropped sample, or when the time across the window is not `(n − 1) ÷ hz`. The time test catches a gap or a jump in the clock.
- A blank `F` stays out of `MAX`. A period shorter than the window gives a blank peak, not 0.

Repeat the sheet for each period, and keep the higher period peak as the session peak. The same formulas work in Excel and Google Sheets.

Use this Python code for raw samples. It returns one row per athlete, session, period, window, and measure. `acc_start` is a column with 1 on the first sample of each counted acceleration effort, 0 on other samples, and blank where speed is blank:

```python
import numpy as np
import pandas as pd

hz, windows_s, thr = 10, [60, 180, 300, 600], 5.5   # ask the user for all three
g = ["athlete_id", "session_id", "period"]
df = df.sort_values(g + ["time_s"])
v = df["speed_m_s"].round(6)
df["distance_m"] = v / hz
df["hsr_m"] = (v / hz).where(v.isna() | (v >= round(thr, 6)), 0.0)   # blank stays blank
rows = []
for key, s in df.groupby(g):
    t = s["time_s"].to_numpy()
    for w in windows_s:
        n = int(round(w * hz))
        if len(s) < n:
            continue                                   # period shorter than the window
        ok = np.round(t[n - 1:] - t[: len(t) - n + 1], 3) == round((n - 1) / hz, 3)
        for col in ["distance_m", "hsr_m", "acc_start"]:
            x = s[col].to_numpy(dtype=float)
            sums = np.convolve(np.nan_to_num(x), np.ones(n), "valid")
            drops = np.convolve(np.isnan(x), np.ones(n), "valid") > 0
            sums = np.where(ok & ~drops, sums, np.nan)
            if not np.isnan(sums).all():
                peak = np.nanmax(sums)
                rows.append((*key, w, col, peak, peak / (w / 60)))
peaks = pd.DataFrame(rows, columns=g + ["window_s", "measure", "peak", "peak_per_min"])
session_peaks = peaks.groupby(["athlete_id", "session_id", "window_s", "measure"],
                              as_index=False)[["peak", "peak_per_min"]].max()
```

Use this function to make `acc_start` from raw speed. It follows the `efforts` function in [accelerations-decelerations.md](accelerations-decelerations.md):

```python
def effort_starts(speed_m_s, hz, thr, min_s, k=1):
    v = np.asarray(speed_m_s, dtype=float)
    a = np.full(len(v), np.nan)
    a[k:] = np.round((v[k:] - v[:-k]) * hz / k, 6)
    hit = a >= thr
    flag, i = np.zeros(len(v)), 0
    while i < len(v):
        if not hit[i]:
            i += 1
            continue
        j = i
        while j < len(v) and hit[j]:
            j += 1
        if (j - i) / hz >= min_s - 1e-9:               # run = samples × time step
            flag[i] = 1                                # count at the first sample
        i = j
    return flag

df["acc_start"] = df.groupby(g)["speed_m_s"].transform(
    lambda s: effort_starts(s, hz, thr=2.5, min_s=0.2))   # ask the user
df["acc_start"] = df["acc_start"].where(df["speed_m_s"].notna())   # blank on drops
```

### Calculate it in Power BI and Tableau

These versions follow the Python code. They use rolling windows, skip any window with a dropped sample or a time gap, and keep the highest window. They return a blank when a period is shorter than the window.

Both versions assume a `gps_samples` table with one row per sample: `athlete_id`, `session_id`, `period`, `sample_index` as a whole number, `time_s`, `speed_m_s`, and `acc_start`. Convert speed to m/s before import. Keep a row with a blank speed for each dropped sample. Set the settings once at the top: Hz, the window lengths, and the high-speed threshold. Label each result with them, the window type, and the acceleration settings that made `acc_start`.

In Power BI, find the peaks in Power Query. Each window needs the samples before it in order, and Power Query reads each period's samples once, at data refresh. The result is a static table that does not change with slicers. Select **New Source**, then **Blank Query**, open **Advanced Editor**, and paste this query. Name the query `peaks`:

```text
let
    hz = 10,
    windows = {60, 180, 300, 600},
    thr = 5.5,
    Peak = (t as list, x as list, w as number) as nullable number =>
        let
            n = Number.Round(w * hz),
            cnt = List.Count(x),
            cum = List.Buffer(
                List.Generate(
                    () => [i = 0, c = 0, d = 0],
                    each [i] <= cnt,
                    each [
                        i = [i] + 1,
                        c = [c] + (if x{[i]} = null then 0 else x{[i]}),
                        d = [d] + (if x{[i]} = null then 1 else 0)
                    ],
                    each [[c], [d]]
                )
            ),
            sums = List.Transform(
                List.Numbers(n - 1, List.Max({cnt - n + 1, 0})),
                each
                    if cum{_ + 1}[d] - cum{_ + 1 - n}[d] = 0
                        and Number.Round(t{_} - t{_ - n + 1}, 3) = Number.Round((n - 1) / hz, 3)
                    then cum{_ + 1}[c] - cum{_ + 1 - n}[c]
                    else null
            )
        in
            List.Max(List.RemoveNulls(sums)),
    Measures = (s as table) as table =>
        let
            sorted = Table.Sort(s, {{"sample_index", Order.Ascending}}),
            t = List.Buffer(sorted[time_s]),
            v = List.Buffer(sorted[speed_m_s]),
            dist = List.Buffer(List.Transform(v, each if _ = null then null else _ / hz)),
            hsr = List.Buffer(
                List.Transform(
                    v,
                    each if _ = null then null
                         else if Number.Round(_, 6) >= Number.Round(thr, 6) then _ / hz
                         else 0
                )
            ),
            acc = List.Buffer(List.Transform(List.Zip({v, sorted[acc_start]}), each if _{0} = null then null else _{1})),
            mins = List.Count(v) / hz / 60,
            sets = {{"distance_m", dist}, {"hsr_m", hsr}, {"acc_efforts", acc}},
            rows = List.TransformMany(
                windows,
                each sets,
                (w, m) => [
                    window_s = w,
                    measure = m{0},
                    peak = Peak(t, m{1}, w),
                    period_total = List.Sum(m{1}),
                    period_min = mins
                ]
            )
        in
            Table.FromRecords(rows),
    Grouped = Table.Group(
        gps_samples,
        {"athlete_id", "session_id", "period"},
        {{"rows", each Measures(_), type table}}
    ),
    Expanded = Table.ExpandTableColumn(
        Grouped, "rows", {"window_s", "measure", "peak", "period_total", "period_min"}
    ),
    peaks = Table.TransformColumnTypes(
        Expanded,
        {
            {"window_s", Int64.Type}, {"measure", type text}, {"peak", type number},
            {"period_total", type number}, {"period_min", type number}
        }
    )
in
    peaks
```

The query works this way:

- `cum` holds the running total and the running count of dropped samples. Position `i` holds the totals of the first `i` samples, so a window sum is one subtraction.
- `List.Numbers(n - 1, ...)` lists the last sample of every full window. A period shorter than the window gives an empty list, and `List.Max` of an empty list returns null (https://learn.microsoft.com/en-us/powerquery-m/list-max).
- `period_total` and `period_min` give the drill average when a period is one drill. `period_min` counts samples, including dropped ones, so check it against the drill time.
- `Table.TransformColumnTypes` sets the types. Without it, the expanded columns have the type `any`, and Power BI loads them as text (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types).

Relate `athletes[athlete_id]` to `peaks[athlete_id]` and `sessions[session_id]` to `peaks[session_id]`, one to many, single direction. The `sessions` table needs a `session_type` column with `match` or `training`. Put `peaks[measure]` and `peaks[window_s]` in slicers, and pick one of each. Use these DAX measures:

```text
Peak per minute =
VAR w = SELECTEDVALUE ( peaks[window_s] )
VAR p = MAX ( peaks[peak] )
RETURN
    IF (
        HASONEVALUE ( peaks[measure] ) && NOT ISBLANK ( w ) && NOT ISBLANK ( p ),
        p / ( w / 60 )
    )

Match peak reference (per min) =
CALCULATE (
    AVERAGEX ( VALUES ( sessions[session_id] ), [Peak per minute] ),
    REMOVEFILTERS ( sessions ),
    REMOVEFILTERS ( peaks[period] ),
    sessions[session_type] = "match"
)

Drill per minute =
VAR tot = MAX ( peaks[period_total] )
VAR mins = MAX ( peaks[period_min] )
RETURN
    IF (
        HASONEVALUE ( peaks[measure] ) && HASONEVALUE ( peaks[period] ) && mins > 0,
        tot / mins
    )

Drill % of match peak =
VAR d = [Drill per minute]
VAR r = [Match peak reference (per min)]
RETURN IF ( NOT ISBLANK ( d ) && r > 0, d / r * 100 )
```

The measures work this way:

- `MAX ( peaks[peak] )` over a session's periods gives the session peak. The match reference is the mean of the athlete's match session peaks for the chosen measure and window.
- To apply a minimum-minutes rule to matches, keep only qualifying matches in `peaks`, for example with a filter step in Power Query.
- Put `athletes[athlete_id]`, `sessions[session_id]`, and `peaks[period]` in the visual for drill rows.

In Tableau, put `athlete_id`, `session_id`, and `period` on Rows and `sample_index` on Detail as a discrete dimension, sorted ascending. Filter to one session at a time, because the view has one mark per sample. Never filter `sample_index`, because that cuts windows. Make these parameters: `Hz` as a float set to 10, `Window (s)` as a float set to 60, and `Threshold (m/s)` set to 5.5. Use these calculations, with the value per sample for the measure you want:

```text
Window samples:
ROUND([Window (s)] * [Hz], 0)

Value per sample, distance (aggregate):
MIN([speed_m_s]) / [Hz]

Value per sample, high-speed running (aggregate):
IF ISNULL(MIN([speed_m_s])) THEN NULL
ELSEIF ROUND(MIN([speed_m_s]), 6) >= ROUND([Threshold (m/s)], 6) THEN MIN([speed_m_s]) / [Hz]
ELSE 0
END

Value per sample, acceleration efforts (aggregate):
IF ISNULL(MIN([speed_m_s])) THEN NULL ELSE MIN([acc_start]) END

Running value (table calculation):
RUNNING_SUM(ZN([Value per sample]))

Running drops (table calculation):
RUNNING_SUM(IIF(ISNULL([Value per sample]), 1, 0))

Window sum (table calculation):
IF INDEX() < [Window samples] THEN NULL
ELSEIF [Running drops] - ZN(LOOKUP([Running drops], -[Window samples])) > 0 THEN NULL
ELSEIF ROUND(MIN([time_s]) - LOOKUP(MIN([time_s]), -([Window samples] - 1)), 3)
       <> ROUND(([Window samples] - 1) / [Hz], 3) THEN NULL
ELSE [Running value] - ZN(LOOKUP([Running value], -[Window samples]))
END

Peak (table calculation):
WINDOW_MAX([Window sum])

Peak per minute (table calculation):
[Peak] / ([Window (s)] / 60)
```

Point `[Value per sample]` at one of the three versions. Set **Compute Using** for every table calculation, including those used inside another one, to **Specific Dimensions**, with `sample_index` checked and `athlete_id`, `session_id`, and `period` unchecked. Each period is then its own partition (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm).

The calculations work this way:

- `INDEX()` counts samples from 1, so the first full window ends at sample `n`. There, `LOOKUP` reaches outside the period and returns null, and `ZN` makes it 0 (https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm).
- `WINDOW_MAX` ignores the null windows. To show one row per period, add a table calculation filter `FIRST() = 0`, as [accelerations-decelerations.md](accelerations-decelerations.md) does.

For drills as a percent of the match peak in Tableau, export `session_peaks` from the Python code or `peaks` from Power Query. Use one row per athlete, session, window, and measure, with `session_type` and `peak_per_min`. Make a `drills` table with `athlete_id`, `measure`, `drill`, and `drill_per_min`. Relate the two tables on `athlete_id` and `measure`. Put `drills` fields on the view, and use these calculations:

```text
Match peak reference (per min):
AVG(IF [session_type] = "match" AND [window_s] = [Window (s)] THEN [peak_per_min] END)

Drill % of match peak:
IF ISNULL([Match peak reference (per min)]) OR [Match peak reference (per min)] <= 0 THEN NULL
ELSE SUM([drill_per_min]) / [Match peak reference (per min)] * 100
END
```

Blanks behave this way in each tool:

- Power BI and Tableau: a window with a dropped sample or a time gap gives no value, and stays out of the peak. A period shorter than the window gives a blank peak.
- Both: a session with samples but no high-speed running or no efforts gives a peak of 0. That is a real 0.
- Both: a player with no match peaks gives a blank reference and a blank percent.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Find the speed column, and convert it to m/s.
2. Find the sampling rate in Hz, and check it against the timestamps.
3. Split each session into periods of play, such as halves, quarters, or drills.
4. Ask which windows to use, such as 1, 3, 5, and 10 minutes, and confirm they are rolling.
5. Ask for the high-speed threshold, and the acceleration threshold, minimum duration, and boundary rule.
6. Make the measure per sample: distance, high-speed distance, or acceleration effort starts.
7. Flag dropped samples and time gaps.
8. Sum the measure over every window that lies inside one period and holds no dropped sample.
9. Keep the highest window sum in each period.
10. Keep the highest period peak as the session peak.
11. Divide by the window length in minutes to get the rate per minute.
12. Label each result with the measure, window length, window type, threshold, and sampling rate.

## Express a drill as a percent of the match peak

A drill as a percent of the match peak compares a drill's intensity with the athlete's own most intense match passage of the same measure. Whitehead et al. (2018) describe peak match demands as one reference for the intensity of conditioning drills. The coach decides what to do with the percent.

Choose these settings, and state each one with the result:

- Match reference: the mean of the athlete's match peaks over the matches the user picks, or the highest one. Baptista et al. (2020) used the mean of 15 matches as 100%. Name which you used and how many matches it holds.
- Qualifying matches: a minimum time on the field and the same position. Baptista et al. (2020) used matches where players completed at least 60 minutes in one position. Ask for the user's rule.
- Window: match the window to the drill. Compute the match peak at the drill's own length when you have raw match data. Otherwise use the nearest window and say so. This is this file's choice, not a published rule.
- Comparison: the drill's average per minute against the match peak, or the drill's own peak window against the match peak of the same window. Baptista et al. (2020) used the second, with 5 minute peaks.

Show the measure, the window, and the reference next to every percent. Never compare a rolling match peak with a fixed one.

## Compare positions

Peak demands differ by position, and the differences depend on the measure (Whitehead et al., 2018). In basketball, position results depend on the team, the role, and the individual, so they should not be carried over to other teams (Pérez-Chao et al., 2023).

Follow these rules when you compare positions:

- Compare each athlete with their own match peak first. Group results by position only after that.
- Report a position group as the median and the number of athletes. A small group gives an unstable summary.
- Use the same measure, window, threshold, and window type for every position.
- Do not express one position's drill values against another position's match peak, or against a squad mean. The worked example shows how a squad reference hides the difference.

## Worked example

This example uses 12 minutes of one player's match data. To keep it short enough to follow by hand, the data are summed into 30 s blocks, and the windows step by one block. Real data step by one sample. Every value below came from running the calculation in Python.

| Block (30 s each) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Distance, m | 48 | 52 | 55 | 60 | 58 | 96 | 104 | 90 | 50 | 49 | 51 | 47 |
| High-speed distance, m | 0 | 0 | 5 | 4 | 3 | 30 | 36 | 24 | 0 | 0 | 0 | 0 |
| Acceleration effort starts | 0 | 1 | 0 | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |

| Block (30 s each) | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Distance, m | 50 | 53 | 49 | 52 | 58 | 62 | 92 | 98 | 57 | 50 | 46 | 50 |
| High-speed distance, m | 0 | 2 | 0 | 0 | 6 | 8 | 26 | 30 | 3 | 0 | 0 | 0 |
| Acceleration effort starts | 0 | 0 | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 0 | 1 | 0 |

The 12 minutes hold 1,477 m, so the average is 123.1 m/min.

Follow these steps for the 1 minute distance peak:

1. A 1 minute window is 2 blocks.
2. The running totals of distance for blocks 1 to 8 are 48, 100, 155, 215, 273, 369, 473, and 563 m.
3. The 2-block window ending at block 7 is 473 − 273 = 200 m. It covers blocks 6 and 7.
4. No other 2-block window is higher, so the rolling 1 minute peak is 200 m, or 200 m/min.
5. Fixed 1 minute windows start at blocks 1, 3, 5, 7, and so on. Blocks 6 and 7 fall in two different fixed windows. The highest fixed window is blocks 7 and 8: 104 + 90 = 194 m/min, 3.0% below the rolling peak.

The same blocks give these peaks:

| Measure | Window | Rolling peak | Per minute | Fixed peak | Per minute | Fixed below rolling |
|---|---|---|---|---|---|---|
| Distance | 1 min | 200 m | 200.0 m/min | 194 m | 194.0 m/min | 3.0% |
| Distance | 3 min | 463 m | 154.3 m/min | 393 m | 131.0 m/min | 15.1% |
| Distance | 5 min | 665 m | 133.0 m/min | 662 m | 132.4 m/min | 0.5% |
| Distance | 10 min | 1,283 m | 128.3 m/min | 1,274 m | 127.4 m/min | 0.7% |
| High-speed distance | 1 min | 66 m | 66.0 m/min | 60 m | 60.0 m/min | 9.1% |
| High-speed distance | 3 min | 102 m | 34.0 m/min | 60 m | 20.0 m/min | 41.2% |
| High-speed distance | 5 min | 102 m | 20.4 m/min | 102 m | 20.4 m/min | 0.0% |
| Acceleration efforts | 1 min | 3 | 3.00 per min | 3 | 3.00 per min | 0.0% |
| Acceleration efforts | 3 min | 6 | 2.00 per min | 5 | 1.67 per min | 16.7% |
| Acceleration efforts | 5 min | 7 | 1.40 per min | 7 | 1.40 per min | 0.0% |

The player did not change. The fixed 3 minute high-speed peak is 41.2% below the rolling one, because the intense passage crosses a fixed boundary.

The player then does a 4 minute small-sided game: 560 m, 20 m of high-speed distance, and 8 acceleration efforts. That is 140.0 m/min, 5.0 m/min, and 2.00 efforts per minute. Against this one match as the reference, the drill is this percent of the rolling match peak:

| Measure | Against the 3 min peak | Against the 4 min peak | Against the 5 min peak |
|---|---|---|---|
| Distance | 90.7% | 99.1% | 105.3% |
| High-speed distance | 14.7% | 19.6% | 24.5% |
| Acceleration efforts | 100.0% | 133.3% | 142.9% |

The 4 minute peak matches the drill length: 141.25 m/min for distance. The same drill reads 90.7% or 105.3% of match peak distance, depending on the window. State the window with every percent.

For positions, four players do the same 3 minute drill. Each player's reference is the mean of their 3 minute rolling match peaks over three matches:

| Player | Position | Match peak reference | Drill | Percent of own peak | Percent of squad mean (156.0 m/min) |
|---|---|---|---|---|---|
| W1 | Wide | 168.0 m/min | 132.0 m/min | 78.6% | 84.6% |
| W2 | Wide | 160.0 m/min | 128.0 m/min | 80.0% | 82.1% |
| C1 | Central | 150.0 m/min | 138.0 m/min | 92.0% | 88.5% |
| C2 | Central | 146.0 m/min | 140.0 m/min | 95.9% | 89.7% |

The wide players' median is 79.3% of their own peak. The central players' median is 93.9%. Against one squad mean, the two group medians look closer: 83.3% and 89.1%. Two players per group is too few for a stable summary. The example only shows the method.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Rolling or fixed windows. In the worked example, the fixed 3 minute high-speed peak is 41.2% below the rolling peak. In soccer, fixed windows underestimated rolling values by about 7% to 10% for total distance and about 12% to 25% for distance above 5.5 m/s (Fereday et al., 2020).
- Window length. A shorter window gives a higher rate per minute. In the worked example, the distance peak is 200.0 m/min over 1 minute and 128.3 m/min over 10 minutes.
- Window step. Stepping by sample gives a peak at least as high as stepping by 1 s or by 30 s blocks. The worked example steps by 30 s to stay short.
- Window for the drill comparison. In the worked example, the same drill reads 90.7%, 99.1%, or 105.3% of match peak distance.
- Match reference. The mean of several match peaks, the highest one, and the latest one give different percents. So do different minimum-minutes rules.
- Periods. A window that crosses half time or a substitution mixes playing and resting time. Restart the windows at each period.
- Thresholds and settings. The high-speed threshold and the acceleration threshold, minimum duration, and filter change the per-sample values. See [high-speed-running.md](high-speed-running.md) and [accelerations-decelerations.md](accelerations-decelerations.md).
- Where an effort counts. This file counts an effort in the window holding its first sample. Counting it where it ends, or splitting it, changes window counts.
- Sampling rate, device type, unit, and software. These change the per-sample values as they change total distance and high-speed running. See [total-distance.md](total-distance.md#what-changes-the-number).
- Matches against training. In basketball, most 1 minute peaks were higher in official matches than in training, in the one study that compared them (Pérez-Chao et al., 2023). Do not use a training peak as a match peak.

## Units and typical range

Peak demands depend on sport, level, position, window, and method. Compare each athlete with their own match peaks on the same device and settings.

| Population | Value | Source |
|---|---|---|
| Professional soccer, rolling windows, 10 Hz | 190.1 ± 20.4 m/min over 60 s; 120.9 ± 13.1 m/min over 600 s (mean ± standard deviation) | Fereday et al., 2020 |
| Football codes, method use | Moving averages in 63% of 27 studies | Whitehead et al., 2018 |
| Elite soccer, local positioning, training week 5 minute peaks as a percent of the match mean | Acceleration peaks 102% to 124%. Deceleration peaks 88% to 115%. Sprint distance peaks 64% for wing-backs, 107% for centre-backs, 100% for centre midfielders, and 107% for centre forwards. | Baptista et al., 2020 |
| Basketball, windows in use | 15 s to 10 minutes. 30 s, 1, 2, and 5 minutes named the most practical. | Pérez-Chao et al., 2023 |

Baptista et al. (2020) set high-intensity running at 19.8 km/h or more and sprinting at 25.2 km/h or more. These are study findings from one team, not targets.

## Data you need

Collect this data:

- Source: raw speed samples from GPS, local positioning, or optical tracking. A summary export with only session totals cannot give peaks.
- Sampling: 10 Hz or faster for GPS. Record the rate with every file.
- Periods: the start and end time of each half, quarter, drill, and substitution.
- Settings record: window lengths, window type, high-speed threshold, acceleration settings, and software version.
- Minimum data: one period gives one peak. A match reference needs several qualifying matches for that athlete on the same device and settings. Ask the user how many.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing rolling and fixed peaks. Fixed windows give lower peaks (Fereday et al., 2020; Varley et al., 2012). State the window type, and never compare the two.
- Using vendor peak values without asking how they are calculated. Ask for the window type, the step, and the window length.
- Letting a window cross half time or a substitution. Restart the windows at each period.
- Filling dropped samples with 0. A window with a gap looks less intense than it was. Skip windows with gaps.
- Comparing a drill with a match peak of a different window length without saying so. The percent changes with the window.
- Using a squad mean as every player's reference. Use each player's own match peak.
- Comparing peaks across devices, software versions, or thresholds. Compare within one system and one set of settings.
- Reading a percent above 100% as a problem, or below 100% as a gap. Report the value and the reference. The coach decides what it means.

## Example request

> I have 10 Hz GPS files from our last five league matches and Tuesday's training. Give me each player's rolling 1, 3, and 5 minute peaks for distance and distance above 5.5 m/s in the matches. Then show Tuesday's 4 minute small-sided game as a percent of each player's own match peak.

## Check the result

Run these checks:

- Confirm the peak per minute falls as the window gets longer, in most cases. A longer window with a higher rate usually means an error in the window length or the units.
- Confirm the 1 minute peak per minute is well above the whole-session average per minute. A lower value usually means an error in the window or the units.
- Confirm a rolling peak is at least the fixed peak for the same window.
- Recalculate one window by hand from the running totals.
- Confirm no window crosses a period boundary or a time gap.
- State the window type, window length, threshold, and match reference next to every result.

## Sources

These sources support the figures and methods in this file:

- Whitehead S, Till K, Weaving D, Jones B. The use of microtechnology to quantify the peak match demands of the football codes: a systematic review. Sports Med. 2018;48(11):2549-2575. https://doi.org/10.1007/s40279-018-0965-6 (accessed 2026-10-07)
- Fereday K, Hills SP, Russell M, Smith J, Cunningham DJ, Shearer D, McNarry M, Kilduff LP. A comparison of rolling averages versus discrete time epochs for assessing the worst-case scenario locomotor demands of professional soccer match-play. J Sci Med Sport. 2020;23(8):764-769. https://doi.org/10.1016/j.jsams.2020.01.002
- Varley MC, Elias GP, Aughey RJ. Current match-analysis techniques' underestimation of intense periods of high-velocity running. Int J Sports Physiol Perform. 2012;7(2):183-185. https://doi.org/10.1123/ijspp.7.2.183
- Baptista I, Johansen D, Figueiredo P, Rebelo A, Pettersen SA. Positional differences in peak- and accumulated- training load relative to match load in elite football. Sports. 2020;8(1):1. Published online 2019-12-23. https://doi.org/10.3390/sports8010001 (accessed 2026-10-07)
- Pérez-Chao EA, Portes R, Gómez MÁ, Parmar N, Lorenzo A, Jiménez-Sáiz SL. A narrative review of the most demanding scenarios in basketball: current trends and future directions. J Hum Kinet. 2023;89:231-245. https://doi.org/10.5114/jhk/170838 (accessed 2026-10-07)
