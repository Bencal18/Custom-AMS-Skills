# Submaximal heart rate and heart rate recovery

Last checked: 2026-10-07

## What it measures

A submaximal heart rate test is a fixed run or drill below maximal effort. Exercise heart rate (HRex) is the mean heart rate near the end of the stage. Heart rate recovery (HRR) is how far heart rate falls in the 60 s after the stage ends. Both show how hard the same fixed work was for the athlete on that day.

These tests track aerobic fitness over weeks better than short-term fatigue. Heart rate indices appear sensitive to positive endurance training effects. Their use to infer short-term negative effects is questionable in team sports (Shushan et al., 2022). Buchheit (2014) lists exercise heart rate as a marker of aerobic fitness, and states that a raised heart rate should not be used as a clear marker of fatigue.

## Formula

Use these formulas for one test:

```text
HRex (bpm)       = mean heart rate over the last 60 s of the stage
HRex (% HRmax)   = HRex (bpm) / HRmax (bpm) × 100
HRR60 (bpm)      = HR at the end of the stage − HR 60 s after the end
```

Define every term in the formula:

- `stage`: a fixed bout of 3 to 4 min or longer, at a fixed speed or in a fixed drill. Buchheit (2014) states that at least 3 to 4 min of exercise are generally needed for heart rate to reach a steady state. Shushan et al. (2022) recommend a minimum of 3 to 4 min to attain more stable heart rate.
- `last 60 s`: the averaging window. Buchheit (2014) states that the mean over the last 30 to 60 s is generally used. In the studies reviewed by Shushan et al. (2022), most used the last 10 to 60 s. The default of 60 s is this repository's choice within that range. Use one window for every test.
- `HRmax`: the athlete's maximal heart rate in bpm. Expressed as a percentage of HRmax, HRex gives a within-athlete marker of relative intensity (Buchheit, 2014). For how to set HRmax, see the HRmax section of the heart rate load reference in the `load-and-wellness` skill.
- `HR at the end of the stage`: the 1 s sample at the moment the stage ends.
- `HR 60 s after the end`: the 1 s sample 60 s later, with the athlete at rest in the same position every test.
- `HRR60`: heart rate recovery within 60 s (Buchheit, 2014). Shushan et al. (2022) describe HRR as an absolute or relative difference between exercise heart rate and heart rate between 10 and 180 s after the test. Report the absolute drop in bpm by default. Using the single samples at the end and at 60 s is this repository's choice. Name the method with every value.

A relative version, HRR60 as a percentage of the heart rate at the end, also appears in studies (Shushan et al., 2022). Do not mix it with the bpm version.

### Fix the test conditions

Heart rate responds to more than fitness. Shushan et al. (2022) name environmental factors such as temperature, habitual factors such as sleep and diet, the time of day, and psychological factors such as stress. They advise considering these or standardizing them where practical.

Keep these the same at every test, and record them in the data:

- `test_drill`: the drill, speed, distance, or course. Give each version its own code.
- Warm-up: its content and length.
- Time of day.
- Heat: the air temperature, and indoors or outdoors.
- The day of the training week, and the athlete's training in the 24 h before.
- The recovery position after the stage, and the device.

Flag any test whose `test_drill` differs from the athlete's reference test. Compare HRex and HRR only between tests with the same `test_drill`. Flag a change in any other condition as "conditions changed". Ask the user for each tolerance, such as how many minutes apart counts as the same time of day. No source in this file sets one, so this skill offers no default.

### Calculate it in a spreadsheet

Put one test per sheet with 1 Hz heart rate: elapsed time in whole seconds in column A and heart rate in bpm in column B. Leave dropouts blank. Put the second the stage ends in `F1` and the athlete's HRmax in `F2`. Use these formulas:

```text
HRex (bpm), F3:
=IF(COUNTIFS(A:A,">"&($F$1-60),A:A,"<="&$F$1,B:B,"<>")<60,"",
    AVERAGEIFS(B:B,A:A,">"&($F$1-60),A:A,"<="&$F$1))

HRex (% HRmax), F4:     =IF(OR(F3="",F2=""),"",F3/F2*100)

HR at stage end, F5:
=IFERROR(IF(INDEX(B:B,MATCH($F$1,A:A,0))="","",INDEX(B:B,MATCH($F$1,A:A,0))),"")

HR 60 s later, F6:
=IFERROR(IF(INDEX(B:B,MATCH($F$1+60,A:A,0))="","",INDEX(B:B,MATCH($F$1+60,A:A,0))),"")

HRR60 (bpm), F7:        =IF(OR(F5="",F6=""),"",F5-F6)
```

HRex is blank when the window has fewer than 60 samples. HRR60 is blank when either sample is missing. A plain `INDEX` returns 0 for a blank cell, which would give a false HRR.

Keep a test log with one row per test: date, athlete, `test_drill`, warm-up, start time, temperature, HRmax used, HRex (% HRmax), and HRR60. Put the athlete's reference test in row 2 and the drill in column C. Flag a different drill with this formula in a new column:

```text
=IF(C3<>$C$2,"different drill","")
```

### Calculate it in Power BI and Tableau

Both versions assume an `hr_samples` table with one row per second: `athlete_id`, `session_id`, `time_s` in whole seconds from the stage start, and `hr_bpm`. They also assume a `submax_tests` table with one row per test: `athlete_id`, `session_id`, `stage_end_s`, `test_drill`, `hr_max_bpm`, and the conditions. Store the HRmax used for each test in its row, so a later HRmax change does not rewrite past tests. This is this repository's choice.

In Power BI, add a column `test_key`, the athlete and session joined as text, to both tables. Relate `submax_tests[test_key]` to `hr_samples[test_key]`, one to many, single direction. Put `submax_tests[test_key]` and `submax_tests[test_drill]` in the visual. Use these DAX measures:

```text
HRex (bpm) =
VAR e = SELECTEDVALUE ( submax_tests[stage_end_s] )
VAR s =
    FILTER (
        hr_samples,
        hr_samples[time_s] > e - 60
            && hr_samples[time_s] <= e
            && NOT ISBLANK ( hr_samples[hr_bpm] )
    )
RETURN IF ( NOT ISBLANK ( e ) && COUNTROWS ( s ) = 60, AVERAGEX ( s, hr_samples[hr_bpm] ) )

HRex (% HRmax) =
VAR h = [HRex (bpm)]
VAR m = SELECTEDVALUE ( submax_tests[hr_max_bpm] )
RETURN IF ( NOT ISBLANK ( h ) && m > 0, h / m * 100 )

HRR60 (bpm) =
VAR e = SELECTEDVALUE ( submax_tests[stage_end_s] )
VAR h0 = CALCULATE ( MAX ( hr_samples[hr_bpm] ), hr_samples[time_s] = e )
VAR h1 = CALCULATE ( MAX ( hr_samples[hr_bpm] ), hr_samples[time_s] = e + 60 )
RETURN IF ( NOT ISBLANK ( e ) && NOT ISBLANK ( h0 ) && NOT ISBLANK ( h1 ), h0 - h1 )
```

In Tableau, join `submax_tests` to `hr_samples` on `athlete_id` and `session_id` in the physical layer. Put `athlete_id`, `session_id`, and `test_drill` on the view. Use these calculations:

```text
In HRex window (row-level):
[time_s] > [stage_end_s] - 60 AND [time_s] <= [stage_end_s] AND NOT ISNULL([hr_bpm])

HRex (bpm) (aggregate):
IF COUNT(IF [In HRex window] THEN [hr_bpm] END) = 60
THEN AVG(IF [In HRex window] THEN [hr_bpm] END) END

HRex (% HRmax) (aggregate):
IF MIN([hr_max_bpm]) > 0 THEN [HRex (bpm)] / MIN([hr_max_bpm]) * 100 END

HR at stage end (aggregate):
MIN(IF [time_s] = [stage_end_s] THEN [hr_bpm] END)

HR 60 s later (aggregate):
MIN(IF [time_s] = [stage_end_s] + 60 THEN [hr_bpm] END)

HRR60 (bpm) (aggregate):
[HR at stage end] - [HR 60 s later]
```

Blanks behave this way in each tool:

- Power BI: HRex is blank when the window has fewer than 60 samples. HRR60 is blank when either sample is missing.
- Tableau: HRex is null when the window has fewer than 60 samples. A null sample at either point makes HRR60 null.

### Calculate it in Python

Use this Python code. It uses the standard library only:

```python
def submax_hr(hr, stage_end_s, hr_max, window_s=60, recovery_s=60):
    """hr: dict of second -> bpm at 1 Hz, from the stage start (0) to after recovery.
    stage_end_s: second at which the stage ends. Returns HRex, %HRmax, and HRR."""
    last = [hr.get(t) for t in range(stage_end_s - window_s + 1, stage_end_s + 1)]
    if any(v is None for v in last):
        raise ValueError("gap in the HRex window")
    hr_ex = sum(last) / len(last)
    hr_end, hr_rec = hr.get(stage_end_s), hr.get(stage_end_s + recovery_s)
    hrr = None if hr_end is None or hr_rec is None else hr_end - hr_rec
    return {"hr_ex_bpm": hr_ex, "hr_ex_pct_max": hr_ex / hr_max * 100,
            "hrr60_bpm": hrr}
```

In R, take `mean()` of the samples in the window, and subtract the two recovery samples, with the same gap rules.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Record the test conditions and the `test_drill` code.
2. Load the heart rate samples at 1 Hz, with time from the stage start.
3. Find the second at which the stage ended.
4. Check the last 60 s of the stage for gaps and artifacts. Stop if any sample is missing.
5. Average the 60 samples to get HRex in bpm.
6. Divide by HRmax and multiply by 100. Name the HRmax source.
7. Take the samples at the stage end and 60 s later.
8. Subtract to get HRR60 in bpm.
9. Compare the conditions and the drill with the athlete's reference test. Flag any difference.
10. Compare the change with the noise band, as below.

## Worked example

This example uses one made-up athlete in a 4 min run at a fixed speed. Every number below came from running the calculation in Python. HRmax is 198 bpm, measured in a maximal test.

| Last 60 s, in 10 s blocks | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Mean heart rate (bpm) | 169 | 170 | 171 | 170 | 172 | 172 |

Step 1. HRex = mean of the 60 samples = 170.67 bpm.

Step 2. HRex = 170.67 / 198 × 100 = 86.195% HRmax.

Step 3. Heart rate at the stage end is 172 bpm. Heart rate 60 s later is 141 bpm. HRR60 = 172 − 141 = 31 bpm.

Step 4. The previous test, with the same drill and conditions, gave 88.0% HRmax. The change is −1.805 points.

Step 5. With a typical error (TE) of 3% of the value (Buchheit, 2014), TE = 0.03 × 86.195 = 2.586 points. The noise band for two single tests is 1.96 × √2 × TE = 2.7719 × 2.586 = 7.168 points. The change of −1.805 is inside it.

Step 6. The previous HRR60 was 26 bpm, so HRR60 rose by 5 bpm. With a TE of 25% (Buchheit, 2014), TE = 7.75 bpm and the noise band is 21.48 bpm. With the range of 2.8% to 13.8% from Shushan et al. (2022), the band runs from 2.41 to 11.86 bpm.

Result: HRex is 86.2% HRmax and HRR60 is 31 bpm. Neither change is beyond the noise band with Buchheit's figures. Which TE you choose decides whether the HRR change can be judged at all.

## What changes the number

These choices change the result even when the athlete's fitness does not change:

- Averaging window. In the worked example, the last 30 s give 86.532% HRmax and the last 60 s give 86.195%.
- HRmax. With an HRmax of 205 bpm in place of 198, HRex falls from 86.195% to 83.252% HRmax.
- Drill, speed, and course. A different drill is a different test.
- Heat, time of day, sleep, diet, and stress (Shushan et al., 2022). Increases in plasma volume after heat acclimatization also change heart rate measures (Buchheit, 2014).
- HRR method. A drop in bpm from a marked stop time, a percentage, and the largest drop in any rolling window give different numbers. Some devices report the rolling-window version. Check the device reference before you compare.
- Recovery position. Standing, sitting, or walking after the stage changes HRR.

## Units and typical range

Report HRex in bpm and % HRmax, and HRR60 in bpm. Name the drill, the window, and the HRmax source.

No population range in this file rates an athlete. HRex depends on the drill. Values at or above 100% HRmax in a submaximal stage point to a wrong HRmax or an artifact. This check is this repository's choice.

Use this test variability to judge a change, and state which figure you used:

| Measure | Typical error, as a CV | Smallest worthwhile change | Source |
|---|---|---|---|
| HRex | About 3% | About −1% | Buchheit, 2014 |
| HRex, team-sport studies | 1.0% to 3.5% | Not given | Shushan et al., 2022 |
| HRR60 | About 25% | About +7% | Buchheit, 2014 |
| HRR, team-sport studies | 2.8% to 13.8% | Not given | Shushan et al., 2022 |

The two sources differ for HRR. HRR is noisy either way, and its noise depends on the protocol and how HRR is expressed. Measure your own TE with your drill, as the `monitoring-statistics` skill describes. The SWC figures are study settings, not targets.

Practice varies. Of 41 high-level football clubs, 41% monitored players' responses with submaximal exercise protocols (Akenhead and Nassis, 2016). Of 74 protocols from 66 practitioners in 24 countries, 61 (82%) collected cardiorespiratory or metabolic outcomes, mostly heart rate indices (Shushan et al., 2023). Of 137 European soccer clubs, 50% used HRR, and the authors identified 28 HRR procedures (Rave et al., 2018).

## Data you need

Collect this data:

- Source: a chest strap or another heart rate sensor that records every second.
- Sampling: 1 Hz or faster, from the stage start to at least 60 s after it ends.
- Protocol: the `test_drill` code, warm-up, time of day, temperature, and recovery position.
- HRmax: a measured value or a labeled estimate, with its date.
- Minimum data: one complete test. Judge change only with a TE from the same drill.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Averaging the whole stage. Use the last 60 s, or the window the user set.
- Comparing tests from different drills or speeds.
- Ignoring heat, time of day, or the day of the training week.
- Using an age-predicted HRmax without saying so.
- Reading a single high HRex as fatigue. Heart rate indices track fitness better than short-term fatigue (Shushan et al., 2022).
- Treating a small HRR change as real. HRR is noisy.
- Reading 0 bpm from a dropout as a heart rate.
- Reading any heart rate value as a sign of a heart problem.

## Example request

> We run a 4-minute submax run every Monday. Here are the heart rate files. Can you give me HRex as % of max and 60-second recovery for each player, and flag anyone whose test conditions changed?

## Check the result

Run these checks:

- Recompute one value by hand: 170.67 / 198 × 100 = 86.2% HRmax.
- Check that HRex is below 100% HRmax.
- Check that HRR60 is positive. A negative value means the samples were swapped or the stage end is wrong.
- Check that every compared test has the same `test_drill`.
- Check that the window held 60 samples with no gap.
- Check that the HRmax for each test is the one in force on that date.

## Sources

This file draws on these sources:

- Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? Frontiers in Physiology. 2014;5:73. https://doi.org/10.3389/fphys.2014.00073 (accessed 2026-10-07)
- Shushan T, McLaren SJ, Buchheit M, Scott TJ, Barrett S, Lovell R. Submaximal fitness tests in team sports: a theoretical framework for evaluating physiological state. Sports Medicine. 2022;52(11):2605-2626. https://doi.org/10.1007/s40279-022-01712-0 (accessed 2026-10-07)
- Shushan T, Norris D, McLaren SJ, Buchheit M, Scott TJ, Barrett S, Dello Iacono A, Lovell R. A worldwide survey on the practices and perceptions of submaximal fitness tests in team sports. International Journal of Sports Physiology and Performance. 2023;18(7):765-779. https://doi.org/10.1123/ijspp.2023-0004 (abstract, accessed 2026-10-07)
- Akenhead R, Nassis GP. Training load and player monitoring in high-level football: current practice and perceptions. International Journal of Sports Physiology and Performance. 2016;11(5):587-593. https://doi.org/10.1123/ijspp.2015-0331 (abstract, accessed 2026-10-07)
- Rave G, Fortrat JO, Dawson B, Carre F, Dupont G, Saeidi A, Boullosa D, Zouhal H. Heart rate recovery and heart rate variability: use and relevance in European professional soccer. International Journal of Performance Analysis in Sport. 2018;18(1):168-183. https://doi.org/10.1080/24748668.2018.1460053 (abstract, accessed 2026-10-07)
