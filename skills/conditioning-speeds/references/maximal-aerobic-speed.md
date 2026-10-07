# Maximal aerobic speed

Last checked: 2026-10-07

## What it measures

Maximal aerobic speed (MAS) is the lowest running speed at which an athlete reaches maximal oxygen uptake (VO2max), the most oxygen the body can use. It is also called vVO2max, the velocity at VO2max (Buchheit and Laursen, 2013b; Sandford et al., 2021).

A laboratory treadmill test with gas analysis measures it directly. Field tests estimate it. Each field test gives a different speed, because each test asks for a different kind of running. Keep the test name with every speed.

Aerobic fitness testing is common. In a survey of 102 elite male soccer practitioners, 82% assessed aerobic capacity. Of the 78 who did, 29% used the 30-15 Intermittent Fitness Test, 24% the Yo-Yo intermittent recovery test level 2, and 22% level 1 (Asimakidis et al., 2024).

## Formula

Use the formula for the test the athlete did:

```text
Set-distance time trial:  MAS_est (m/s) = distance (m) / time (s)
Set-time run:             MAS_est (m/s) = distance (m) / time (s)
30-15 IFT:                VIFT (km/h) = speed of the last completed stage. VIFT is not MAS.
Yo-Yo IR1 or IR2:         distance (m) or level. No verified conversion to MAS.
Speed in km/h:            speed (km/h) = speed (m/s) x 3.6
```

Define every term in the formula:

- `MAS_est`: estimated MAS, in m/s. Label it with the test, such as "MAS, 2,000 m time trial".
- `distance`: the set distance of a time trial, or the distance covered in a set-time run, in m.
- `time`: the time taken for a set distance, or the set time of a set-time run, in s. Convert mm:ss first: 7:30 is 7 × 60 + 30 = 450 s.
- `VIFT`: the final speed of the 30-15 IFT, recorded as the speed at the last completed stage (Haydar et al., 2011).

### Set-distance time trials

The athlete runs a set distance as fast as possible. Average speed is distance divided by time.

The distance changes the result. In 28 male Australian Rules football players, average speed over 1,200 m and 1,400 m was higher than laboratory MAS. Speeds over 1,600 to 2,200 m did not differ from MAS, and 2,000 m agreed best (Bellenger et al., 2015). In 33 female Australian Rules football players, 1,400 m agreed best. The authors estimated that time trial speed equals MAS at 1.4 to 1.5 km (Lundquist et al., 2021).

A shorter trial gives a faster speed. Bellenger et al. (2015) found the gap between time trial speed and MAS shrank as the distance grew.

### Set-time runs

The athlete runs as far as possible in a set time. Average speed is distance divided by the set time.

The 5-minute run was designed to estimate MAS. In 48 men, it gave 17.1 ± 2.2 km/h against 16.9 ± 2.6 km/h on a treadmill, with r = 0.94 (Berthon et al., 1997a). Smith et al. (2025) used a 6-minute distance trial.

### 1,500 m race times in elite middle-distance runners

In 12 elite middle-distance runners, average 1,500 m race speed was 2.06 ± 1.03 km/h faster than laboratory vVO2max. The authors derived this equation for that population (Sandford et al., 2019b):

```text
vVO2max (km/h) = (1,500 m race speed (km/h) - 14.921) / 0.4266
```

Do not apply it to other athletes. For a 1,500 m in 320 s (16.875 km/h), it returns 4.58 km/h, which is impossible. Use the plain time trial formula instead, and name the distance.

### The 30-15 Intermittent Fitness Test is not MAS

The 30-15 IFT is a set of 30 s shuttle runs over 40 m, with 15 s of passive rest between them. Speed starts at 8 km/h and rises 0.5 km/h at each stage. The test ends when the athlete cannot reach a 3 m zone near each line on the audio signal 3 times in a row (Haydar et al., 2011). VIFT is the speed at the last completed stage.

VIFT is faster than MAS from a continuous test. The runs are short, and the athlete rests between them. Smith et al. (2025) link the gap partly to the anaerobic demand of frequent deceleration, change of direction, and reacceleration in intermittent tests.

Use VIFT as its own reference speed. Buchheit (2008) set the distances of intermittent runs from VIFT, and heart rate during those runs varied less between players than when distances came from continuous tests.

If the user asks to convert VIFT to MAS, show this study and its limits. Do not apply it as a rule:

- Smith et al. (2025) tested 26 male academy soccer players. Mean VIFT was 20.46 ± 0.89 km/h.
- Speed in a 6-minute distance trial was 77 ± 3% of VIFT. Speed in an 1,800 m time trial was 79 ± 3% of VIFT.
- The authors gave these equations: 6-minute trial speed (km/h) = 3.24 + 0.61 × VIFT (km/h), and 1,800 m trial speed (km/h) = −0.93 + 0.84 × VIFT (km/h).
- Their MAS estimate of 87% of VIFT, a factor from earlier guidance, was 0.57 m/s higher than the 6-minute trial and 0.45 m/s higher than the 1,800 m trial.
- They concluded that each test gives a distinct estimate of MAS.

### The Yo-Yo intermittent recovery tests are not MAS

The Yo-Yo intermittent recovery tests are shuttle runs between lines 20 m apart, paced by audio signals at rising speed, with 10 s of active recovery between runs (Ferigne et al., 2025). Level 1 (IR1) focuses on the aerobic system. Level 2 (IR2) has a high anaerobic contribution (Bangsbo et al., 2008).

The result is a distance or a level, not a speed. This file gives no conversion from a Yo-Yo result to MAS, because no conversion was verified in a primary source. Some studies report a "maximal aerobic speed" from the Yo-Yo IR1 without saying how they derived it (Ferigne et al., 2025). Do not copy such a value into a MAS column.

If the user's only aerobic test is a Yo-Yo test, compute distances from it only if the user names a method and its source. Otherwise, say the skill cannot turn a Yo-Yo result into a running speed.

### Calculate it in a spreadsheet

Use this layout, which `interval-distances.md` uses for the full run sheet:

- Sheet `tests`: `A` athlete ID, `B` test code, `C` result, `D` test date as a real date, and `E` speed in m/s from the formula below.
- Sheet `test_info`: `A` test code, `B` result kind, `C` set distance in m, and `D` set time in s.

Fill `test_info` with one row for each test. Use these result kinds:

| Test code | Result kind | Set distance (m) | Set time (s) | Result in `tests!C` |
|---|---|---|---|---|
| `tt_2000m` | `time_s` | 2000 | | Time in s |
| `tt_1500m` | `time_s` | 1500 | | Time in s |
| `run_5min` | `distance_m` | | 300 | Distance in m |
| `ift_30_15` | `speed_kmh` | | | VIFT in km/h |
| `yoyo_ir1` | `no_speed` | | | Distance in m |
| `sprint_mss` | `speed_m_s` | | | Maximal sprint speed in m/s |
| `gps_max_speed` | `speed_m_s` | | | Highest valid GPS speed in m/s |

Put this formula in `tests!E2`, and fill it down. It works in Excel 2019 or later and in Google Sheets. It returns a blank when the result is blank, text, or 0, and for `no_speed` tests:

```text
=IF(NOT(ISNUMBER(C2)),"",IFERROR(SWITCH(VLOOKUP(B2,test_info!$A:$B,2,FALSE),"time_s",VLOOKUP(B2,test_info!$A:$C,3,FALSE)/C2,"distance_m",C2/VLOOKUP(B2,test_info!$A:$D,4,FALSE),"speed_kmh",C2/3.6,"speed_m_s",C2),""))
```

The column holds MAS only for `time_s` and `distance_m` rows. For `ift_30_15` rows it holds VIFT in m/s. Never average or chart `ift_30_15` rows with time trial rows.

For km/h, multiply by 3.6: `=IF(ISNUMBER(E2),E2*3.6,"")`.

### Calculate it in Power BI and Tableau

These versions assume one row per athlete, date, session, measure, and trial in a `measures` table, as in the `ams-data-setup` skill. A 2,000 m time trial is `measure_name` `tt_2000m_time` in `s`. Change the name and the 2000 for another distance. They use the latest test date for each athlete, and the fastest time on that date.

In Power BI, use this DAX measure:

```text
MAS 2000 m TT (m/s) =
VAR lastDate =
    CALCULATE (
        MAX ( measures[measure_date] ),
        measures[measure_name] = "tt_2000m_time",
        measures[unit] = "s",
        measures[status] = "ok"
    )
VAR t =
    CALCULATE (
        MIN ( measures[value] ),
        measures[measure_name] = "tt_2000m_time",
        measures[unit] = "s",
        measures[status] = "ok",
        measures[measure_date] = lastDate
    )
RETURN
    IF ( NOT ISBLANK ( t ) && t > 0, 2000 / t )
```

Put `athlete_id` in the visual. The measure returns a blank for an athlete with no valid time.

In Tableau, use these calculations. Put `athlete_id` on the view, and use `MIN` of the last one:

```text
Latest TT date:
{ FIXED [athlete_id] :
  MAX(IF [measure_name] = "tt_2000m_time" AND [unit] = "s" AND [status] = "ok"
      THEN [measure_date] END) }

Latest TT time (s):
{ FIXED [athlete_id] :
  MIN(IF [measure_name] = "tt_2000m_time" AND [unit] = "s" AND [status] = "ok"
      AND [measure_date] = [Latest TT date] THEN [value] END) }

MAS 2000 m TT (m/s):
IF [Latest TT time (s)] > 0 THEN 2000 / [Latest TT time (s)] END
```

A null or zero time gives a null MAS in both tools.

### Calculate it in Python

```python
import pandas as pd

SET_DISTANCE_M = {"tt_2000m": 2000, "tt_1500m": 1500}   # time_s tests
SET_TIME_S = {"run_5min": 300}                          # distance_m tests

def reference_speed_m_s(test, result):
    """Return the test's speed in m/s, or None. VIFT stays VIFT; Yo-Yo gives None."""
    if pd.isna(result) or result <= 0:
        return None
    if test in SET_DISTANCE_M:
        return SET_DISTANCE_M[test] / result
    if test in SET_TIME_S:
        return result / SET_TIME_S[test]
    if test == "ift_30_15":
        return result / 3.6        # VIFT in m/s, not MAS
    return None

tests["speed_m_s"] = [reference_speed_m_s(t, r) for t, r in zip(tests["test"], tests["result"])]
```

## Calculate the metric

Follow these steps to calculate a reference speed from a test result:

1. Find the test name for each result. Do not guess it from the size of the number.
2. Convert a time in mm:ss to seconds.
3. For a set-distance trial, divide the distance in m by the time in s.
4. For a set-time run, divide the distance in m by the set time in s.
5. For the 30-15 IFT, record the speed of the last completed stage in km/h, and divide by 3.6 for m/s. Label it VIFT.
6. For a Yo-Yo test, record the distance or level. Do not compute a speed.
7. Multiply any m/s value by 3.6 to show km/h.
8. Keep each test's speeds in their own column.

## Worked example

This example uses made-up results for one athlete, tested in one month.

| Input | Value |
|---|---|
| 2,000 m time trial | 7:30 |
| 1,500 m time trial | 5:20 |
| 5-minute run | 1,350 m |
| 30-15 IFT, last completed stage | 20.0 km/h |

Step 1. 2,000 m time = 7 × 60 + 30 = 450 s. MAS = 2000 / 450 = 4.444 m/s, or 16.00 km/h.

Step 2. 1,500 m time = 5 × 60 + 20 = 320 s. Speed = 1500 / 320 = 4.688 m/s, or 16.88 km/h.

Step 3. 5-minute run speed = 1350 / 300 = 4.500 m/s, or 16.20 km/h.

Step 4. VIFT = 20.0 / 3.6 = 5.556 m/s. This is not MAS.

Step 5. Compare the tests. The 1,500 m speed is 0.88 km/h faster than the 2,000 m speed. VIFT is 1.25 times the 2,000 m MAS.

Result: MAS from the 2,000 m time trial is 4.444 m/s (16.00 km/h). The same athlete has three other reference speeds from three other tests. Each is correct for its own test. None can replace another.

## What changes the number

These choices change the result even when the athlete's fitness does not:

- Test type. In the worked example, the four tests give 16.00, 16.20, 16.88, and 20.0 km/h for one athlete.
- Time trial distance. Shorter trials give faster speeds (Bellenger et al., 2015). Women and men may reach MAS at different distances (Lundquist et al., 2021).
- Continuous or intermittent format. Rest between runs and shorter runs raise VIFT above continuous test speeds (Smith et al., 2025).
- Surface. In male collegiate soccer players, Yo-Yo IR1 distance was 2,370 ± 662 m on natural grass and 1,441 ± 463 m on artificial turf (Ferigne et al., 2025). Use the same surface at every test.
- Stage rule. VIFT is the last completed stage, not the stage the athlete stopped in (Haydar et al., 2011). Use the same rule every time.
- Pacing and timing. A self-paced trial depends on pacing. Hand timing and electronic timing can differ. Record both the method and the conditions.

## Units and typical range

Report MAS in m/s or km/h, and name the test. Use these ranges to check that data are plausible, not to rate athletes:

| Population | Test | Typical range | Source |
|---|---|---|---|
| 48 men of mixed fitness | 5-minute run | 17.1 ± 2.2 km/h (mean ± SD) | Berthon et al., 1997a |
| 48 men of mixed fitness | Treadmill, last step | 16.9 ± 2.6 km/h (mean ± SD) | Berthon et al., 1997a |
| Sub-elite runners (n = 18) | 5-minute run | 19.5 ± 0.9 km/h (mean ± SD) | Berthon et al., 1997b |
| Athletes from other sports (n = 23) | 5-minute run | 15.9 ± 1.2 km/h (mean ± SD) | Berthon et al., 1997b |
| Male academy soccer players, aged 17 (n = 26) | 6-minute distance trial | 4.39 ± 0.24 m/s (mean ± SD) | Smith et al., 2025 |
| Male academy soccer players, aged 17 (n = 26) | 1,800 m time trial | 4.49 ± 0.26 m/s (mean ± SD) | Smith et al., 2025 |
| Male academy soccer players, aged 17 (n = 26) | 30-15 IFT, VIFT | 20.46 ± 0.89 km/h (mean ± SD) | Smith et al., 2025 |
| Female collegiate soccer players (n = 24) | 30-15 IFT, VIFT | 17.52 km/h (mean) | Paulsen et al., 2023 |

Use these figures to judge a change in one athlete:

- 5-minute run: the standard error of measurement (SEM) was 0.15 to 0.34 km/h across groups, retested within 3 weeks (Dabonneville et al., 2003). The noise band for two single tests, 2.77 × SEM, is 0.42 to 0.94 km/h.
- 30-15 IFT: across 10 study groups, the coefficient of variation of VIFT was 1.5% to 6.0% (Grgic et al., 2021). On a VIFT of 20.0 km/h, that is 0.3 to 1.2 km/h.

Use a published figure only when your test, surface, and athletes match. Otherwise, measure your own typical error from a short-term retest.

## Data you need

Collect this data:

- Source: the test name, the result, its unit, the test date, and the surface.
- Sampling: one result per athlete per test day. Record the timing method for a time trial.
- Minimum data: one valid test per athlete on the chosen test. To judge change, a typical error for that test.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Calling VIFT "MAS", or putting VIFT and time trial speeds in one column. Keep each test in its own column.
- Converting a Yo-Yo result to a speed with an unsourced rule. Do not convert it.
- Typing 7:30 as 7.30 and dividing. Convert mm:ss to seconds first.
- Reading km/h as m/s. A MAS of 16 m/s is a km/h value in the wrong column.
- Using the speed of the stage the athlete stopped in as VIFT. Use the last completed stage.
- Applying the elite 1,500 m race equation to team-sport athletes.
- Treating a switch from one test to another as a change in fitness.

## Example request

> Our squad ran a 2 km time trial in September. The times are in mm:ss in Google Sheets. Can you add MAS in m/s and km/h for each player, and tell me why it doesn't match their 30-15 scores?

## Check the result

Run these checks:

- Recompute one value by hand: 2000 m / 450 s = 4.444 m/s = 16.00 km/h.
- Check the size. Every mean in the table above sits between about 4 and 6 m/s, or 15 and 21 km/h. A value far outside that range needs a second look.
- Check that VIFT is higher than MAS from a continuous test for the same athlete.

## Sources

This file cites these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
- Bangsbo J, Iaia FM, Krustrup P. The Yo-Yo intermittent recovery test: a useful tool for evaluation of physical performance in intermittent sports. Sports Medicine. 2008;38(1):37-51. https://doi.org/10.2165/00007256-200838010-00004 (accessed 2026-10-07)
- Bellenger CR, Fuller JT, Nelson MJ, Hartland M, Buckley JD, Debenedictis TA. Predicting maximal aerobic speed through set distance time-trials. European Journal of Applied Physiology. 2015;115(12):2593-2598. https://doi.org/10.1007/s00421-015-3233-6 (accessed 2026-10-07)
- Berthon P, Fellmann N, Bedu M, Beaune B, Dabonneville M, Coudert J, Chamoux A. A 5-min running field test as a measurement of maximal aerobic velocity. European Journal of Applied Physiology and Occupational Physiology. 1997;75(3):233-238. https://doi.org/10.1007/s004210050153 (accessed 2026-10-07). Cited as Berthon et al., 1997a.
- Berthon P, Dabonneville M, Fellmann N, Bedu M, Chamoux A. Maximal aerobic velocity measured by the 5-min running field test on two different fitness level groups. Archives of Physiology and Biochemistry. 1997;105(7):633-639. https://doi.org/10.1076/apab.105.7.633.11394 (accessed 2026-10-07). Cited as Berthon et al., 1997b.
- Buchheit M. The 30-15 intermittent fitness test: accuracy for individualizing interval training of young intermittent sport players. Journal of Strength and Conditioning Research. 2008;22(2):365-374. https://doi.org/10.1519/JSC.0b013e3181635b2e (accessed 2026-10-07)
- Buchheit M, Laursen PB. High-intensity interval training, solutions to the programming puzzle. Part II: anaerobic energy, neuromuscular load and practical applications. Sports Medicine. 2013;43(10):927-954. https://doi.org/10.1007/s40279-013-0066-5 (accessed 2026-10-07). Cited as Buchheit and Laursen, 2013b.
- Dabonneville M, Berthon P, Vaslin P, Fellmann N. The 5 min running field test: test and retest reliability on trained men and women. European Journal of Applied Physiology. 2003;88(4-5):353-360. https://doi.org/10.1007/s00421-002-0617-1 (accessed 2026-10-07)
- Ferigne G, Martin K, Ottinger C, Biscardi L. Playing surface impacts Yo-Yo intermittent recovery test (level 1) performance and validity of indirect VO2max estimation. International Journal of Exercise Science. 2025;18(8):1142-1150. https://doi.org/10.70252/pgpl8156 (accessed 2026-10-07)
- Grgic J, Lazinica B, Pedisic Z. Test-retest reliability of the 30-15 Intermittent Fitness Test: a systematic review. Journal of Sport and Health Science. 2021;10(4):413-418. https://doi.org/10.1016/j.jshs.2020.04.010 (accessed 2026-10-07)
- Haydar B, Al Haddad H, Ahmaidi S, Buchheit M. Assessing inter-effort recovery and change of direction abilities with the 30-15 Intermittent Fitness Test. Journal of Sports Science and Medicine. 2011;10(2):346-354. https://pmc.ncbi.nlm.nih.gov/articles/PMC3761847/ (accessed 2026-10-07)
- Lundquist M, Nelson MJ, Debenedictis T, Gollan S, Fuller JT, Larwood T, Bellenger CR. Set distance time trials for predicting maximal aerobic speed in female Australian Rules Footballers. Journal of Science and Medicine in Sport. 2021;24(4):391-396. https://doi.org/10.1016/j.jsams.2020.10.002 (accessed 2026-10-07)
- Paulsen KM, McDermott BP, Myers AJ, Gray M, Lo WJ, Ganio MS. Reliability and validity of the 30-15 Intermittent Field Test with and without a soccer ball. Research Quarterly for Exercise and Sport. 2023;94(4):1001-1010. https://doi.org/10.1080/02701367.2022.2098230 (accessed 2026-10-07)
- Sandford GN, Rogers SA, Sharma AP, Kilding AE, Ross A, Laursen PB. Implementing anaerobic speed reserve testing in the field: validation of vVO2max prediction from 1500-m race performance in elite middle-distance runners. International Journal of Sports Physiology and Performance. 2019;14(8):1147-1150. https://doi.org/10.1123/ijspp.2018-0553 (accessed 2026-10-07). Cited as Sandford et al., 2019b.
- Sandford GN, Laursen PB, Buchheit M. Anaerobic speed/power reserve and sport performance: scientific basis, current applications and future directions. Sports Medicine. 2021;51(10):2017-2028. https://doi.org/10.1007/s40279-021-01523-9 (accessed 2026-10-07)
- Smith K, Wright MD, Chesterton P, Taylor JM. Estimating maximal aerobic speed in academy soccer players: a comparison between time trial methods and the 30-15 Intermittent Fitness Test. European Journal of Sport Science. 2025;25(6):e12315. https://doi.org/10.1002/ejsc.12315 (accessed 2026-10-07)
