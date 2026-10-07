# Interval distances

Last checked: 2026-10-07

## What it measures

An interval distance is how far an athlete covers in a work period at a speed the coach sets as a percentage of the athlete's reference speed. This file computes the distance, or the target time for a set distance. The coach chooses the reference test, the percentage, the work time, and any groups.

## Formula

Use these formulas:

```text
target speed (m/s)   = reference speed (m/s) x p / 100
distance (m)         = target speed (m/s) x work time (s)
target time (s)      = set distance (m) / target speed (m/s)
ASR-based speed (m/s) = MAS (m/s) + (q / 100) x ASR (m/s)
```

Define every term in the formula:

- `reference speed`: the athlete's speed from one named test, in m/s. It is MAS from a continuous test, or VIFT from the 30-15 IFT. See `maximal-aerobic-speed.md`. Keep the test name with it.
- `p`: the percentage of the reference speed the coach chooses.
- `work time`: the length of one work period the coach chooses, in s.
- `set distance`: a distance the coach chooses, in m, when the coach wants a time instead of a distance.
- `q`: the percentage of anaerobic speed reserve (ASR) the coach chooses. See `anaerobic-speed-reserve.md`.

Every distance here is a straight-line distance. It does not account for turns.

### Shuttles and turns

Turns change the effort at the same average speed. In 10 male team-sport athletes running at 60% of vVO2max, oxygen uptake was 37 ± 5 mL/kg/min over 20 m shuttles and 33 ± 6 mL/kg/min in a straight line (Buchheit et al., 2011). That study gives no correction for distance.

This file gives no shuttle correction, because no verified source in it gives one. Do not invent one. Label a distance run as shuttles as "straight-line distance, run as shuttles". The 30-15 IFT is run over 40 m shuttles (Haydar et al., 2011), so VIFT already includes a turn every 40 m. Buchheit (2008) set intermittent run distances from VIFT.

### Study settings, not recommendations

These are settings from named studies. Show them only as examples when the user asks what others have used. They are not advice, and they do not fit every athlete, sport, or time of season:

| Study | Athletes | Setting |
|---|---|---|
| Collison et al., 2022 | 17 male junior Australian Rules football players | 15 s work and 15 s rest until exhaustion, at 120% of MAS, 20% of ASR, or 95% of VIFT |
| Blondel et al., 2001 | 10 participants | Constant-speed runs to exhaustion at 90%, 100%, 120%, and 140% of vVO2max. Mean times were 839, 357, 122, and 65 s. |
| Buchheit, 2008 | 59 young intermittent sport players, aged 16.2 ± 2.3 | 3 series of intermittent runs, with distances set from VIFT and from the end speeds of 2 continuous field tests |
| Buchheit and Laursen, 2013b | Review | High-intensity interval training used speeds from 95% of vVO2max up to 100% of maximal sprint speed |

Collison et al. (2022) found that time to exhaustion varied less between players at 20% of ASR than at 120% of MAS, but the confidence interval included no difference. Buchheit and Laursen (2013a) describe interval design as the choice of up to 9 variables, including work and rest intensity and duration, number of repetitions, and number of series. This skill computes only the speed and distance part.

### Build a per-athlete run sheet in a spreadsheet

These formulas work in Excel 2019 or later and in Google Sheets. They use 3 sheets and one helper sheet.

Sheet `tests` holds one row for each result. Use these columns:

- `A` athlete ID, as text
- `B` test code, such as `tt_2000m` or `sprint_mss`
- `C` result, in the unit `test_info` names
- `D` test date, as a real date, not text
- `E` speed in m/s, from the formula in `maximal-aerobic-speed.md`

Sheet `test_info` holds one row for each test code, as `maximal-aerobic-speed.md` shows.

Sheet `settings` holds the coach's choices. The skill fills none of them:

| Cell | Holds |
|---|---|
| `B1` | Reference test code, such as `tt_2000m` |
| `B2` | Percentage of the reference speed |
| `B3` | Work time in s |
| `B4` | Sprint test code, such as `sprint_mss` or `gps_max_speed` |
| `B5` | Optional: percentage of ASR |
| `B6:B7` | Optional: group boundaries in m/s |

Sheet `run_sheet` has one row for each athlete. Put athlete IDs in column `A`, typed or from `=UNIQUE(tests!A2:A1000)`. Put these formulas in row 2, and fill them down:

| Column | Holds | Formula |
|---|---|---|
| `B` | Latest reference test date | `=IF(MAXIFS(tests!$D:$D,tests!$A:$A,$A2,tests!$B:$B,settings!$B$1)=0,"",MAXIFS(tests!$D:$D,tests!$A:$A,$A2,tests!$B:$B,settings!$B$1))` |
| `C` | Rows on that date | `=IF(B2="","",COUNTIFS(tests!$A:$A,$A2,tests!$B:$B,settings!$B$1,tests!$D:$D,B2))` |
| `D` | Reference speed (m/s) | `=IF(B2="","",IF(C2>1,"check: "&C2&" rows",IFERROR(AVERAGEIFS(tests!$E:$E,tests!$A:$A,$A2,tests!$B:$B,settings!$B$1,tests!$D:$D,B2),"no valid result")))` |
| `E` | Reference speed (km/h) | `=IF(ISNUMBER(D2),D2*3.6,"")` |
| `F` | Distance (m) | `=IF(AND(ISNUMBER(D2),ISNUMBER(settings!$B$2),ISNUMBER(settings!$B$3)),D2*settings!$B$2/100*settings!$B$3,"")` |
| `G` | Latest sprint test date | `=IF(MAXIFS(tests!$D:$D,tests!$A:$A,$A2,tests!$B:$B,settings!$B$4)=0,"",MAXIFS(tests!$D:$D,tests!$A:$A,$A2,tests!$B:$B,settings!$B$4))` |
| `H` | MSS (m/s), best on that date | `=IF(G2="","",IF(MAXIFS(tests!$E:$E,tests!$A:$A,$A2,tests!$B:$B,settings!$B$4,tests!$D:$D,G2)=0,"no valid result",MAXIFS(tests!$E:$E,tests!$A:$A,$A2,tests!$B:$B,settings!$B$4,tests!$D:$D,G2)))` |
| `I` | ASR (m/s) | `=IF(AND(ISNUMBER(D2),ISNUMBER(H2)),H2-D2,"")` |
| `J` | Speed at chosen % ASR (m/s) | `=IF(AND(ISNUMBER(I2),ISNUMBER(settings!$B$5)),D2+settings!$B$5/100*I2,"")` |
| `K` | Days between the two tests | `=IF(AND(ISNUMBER(B2),ISNUMBER(G2)),ABS(G2-B2),"")` |
| `L` | Group | `=IF(AND(ISNUMBER(D2),COUNT(settings!$B$6:$B$7)>0),1+COUNTIF(settings!$B$6:$B$7,"<="&D2),"")` |

Read the run sheet this way:

- Column `D` shows "check" when one athlete has 2 or more rows for the chosen test on the same date. Resolve the duplicate before you use the row.
- Column `D` is blank for an athlete with no result for the chosen test. List those athletes for the coach.
- Column `F` stays blank until the coach enters a percentage and a work time.
- Column `I` is only a true ASR when the reference test is a continuous MAS test, not `ift_30_15`.
- Column `L` gives group 1 to the slowest band. Each boundary in `B6:B7` starts a new group at that speed. Add cells for more boundaries, and widen the range.
- Format columns `B` and `G` as dates.

For a target time over a set distance, put the distance in `settings!B8` and use `=IF(AND(ISNUMBER(D2),ISNUMBER(settings!$B$2),ISNUMBER(settings!$B$8)),settings!$B$8/(D2*settings!$B$2/100),"")`.

Rounding is the coach's choice. To round a distance to the nearest metre, use `=IF(ISNUMBER(F2),ROUND(F2,0),"")`. Show the unrounded value next to it.

### Sort athletes by speed

Sort only when the user asks. Use a sorted list to set up running groups, not to rank athletes. Do not number the rows or label anyone best or worst.

In Excel 365, use this formula on a new sheet. It drops athletes with no numeric speed and sorts by column `D`, fastest first:

```text
=SORT(FILTER(run_sheet!A2:L200,ISNUMBER(run_sheet!D2:D200)),4,-1)
```

In Google Sheets, the sort order argument differs:

```text
=SORT(FILTER(run_sheet!A2:L200,ISNUMBER(run_sheet!D2:D200)),4,FALSE)
```

### Calculate it in Power BI and Tableau

These versions use the `MAS 2000 m TT (m/s)` measure from `maximal-aerobic-speed.md`.

In Power BI, add two what-if parameters the coach sets: `Percent chosen` and `Work seconds`. Then add this DAX measure:

```text
Interval distance (m) =
VAR mas = [MAS 2000 m TT (m/s)]
VAR p = SELECTEDVALUE ( 'Percent chosen'[Percent chosen] )
VAR t = SELECTEDVALUE ( 'Work seconds'[Work seconds] )
RETURN
    IF ( NOT ISBLANK ( mas ) && NOT ISBLANK ( p ) && NOT ISBLANK ( t ), mas * p / 100 * t )
```

In Tableau, add two parameters the coach sets: `[Percent chosen]` and `[Work seconds]`. Then add this calculation, and use `MIN` of it with `athlete_id` on the view:

```text
Interval distance (m):
[MAS 2000 m TT (m/s)] * [Percent chosen] / 100 * [Work seconds]
```

A Tableau parameter always holds a value. Tell the coach to set both parameters before reading the result.

### Calculate it in Python

```python
def interval_distance_m(ref_speed_m_s, percent, work_s):
    """All three inputs come from the coach's test and choices."""
    if None in (ref_speed_m_s, percent, work_s):
        return None
    return ref_speed_m_s * percent / 100 * work_s

def target_time_s(set_distance_m, ref_speed_m_s, percent):
    return set_distance_m / (ref_speed_m_s * percent / 100)

def speed_group(speed_m_s, boundaries):
    """Group 1 is the slowest band. The coach supplies the boundaries."""
    return 1 + sum(1 for b in boundaries if b <= speed_m_s)
```

## Calculate the metric

Follow these steps to calculate interval distances:

1. Ask the coach for the reference test, the percentage, and the work time.
2. Get each athlete's latest reference speed from that test, in m/s.
3. Multiply the reference speed by the percentage divided by 100.
4. Multiply the result by the work time in s.
5. For a set distance, divide the distance by the target speed to get a target time.
6. Label each distance with the test, the test date, the percentage, the work time, and "straight-line".
7. Sort or group only if the coach asks, at boundaries the coach gives.

## Worked example

This example uses a made-up test table. The coach chose these settings: reference test `tt_2000m`, 105% of MAS, 30 s of work, sprint test `sprint_mss`, and group boundaries at 4.3 and 4.5 m/s.

| Athlete | Test | Result | Date |
|---|---|---|---|
| A0001 | `tt_2000m` | 450 s | 2026-09-01 |
| A0001 | `sprint_mss` | 8.90 m/s | 2026-09-03 |
| A0002 | `tt_2000m` | 480 s | 2026-09-01 |
| A0002 | `tt_2000m` | 470 s | 2026-09-29 |
| A0002 | `sprint_mss` | 8.50 m/s | 2026-09-03 |
| A0003 | `tt_2000m` | 435 s | 2026-09-01 |
| A0003 | `ift_30_15` | 20.5 km/h | 2026-09-15 |
| A0003 | `sprint_mss` | 9.10 m/s | 2026-09-03 |
| A0004 | `ift_30_15` | 19.0 km/h | 2026-09-15 |

Step 1. MAS for A0001 = 2000 / 450 = 4.444 m/s (16.00 km/h).

Step 2. A0002 has two 2,000 m trials. The latest is 2026-09-29: 2000 / 470 = 4.255 m/s (15.32 km/h).

Step 3. MAS for A0003 = 2000 / 435 = 4.598 m/s (16.55 km/h). The 30-15 IFT row is ignored, because the coach chose `tt_2000m`.

Step 4. A0004 has no 2,000 m result. The run sheet leaves the row blank, and the answer lists A0004 as missing.

Step 5. Distance for A0001 = 4.444 × 105 / 100 × 30 = 140.0 m. For A0002, 4.255 × 1.05 × 30 = 134.0 m. For A0003, 4.598 × 1.05 × 30 = 144.8 m.

Step 6. ASR for A0001 = 8.90 − 4.444 = 4.456 m/s. For A0002, 8.50 − 4.255 = 4.245 m/s, with 26 days between the tests. For A0003, 9.10 − 4.598 = 4.502 m/s.

Step 7. Groups at 4.3 and 4.5 m/s: A0002 (4.255 m/s) is in group 1, A0001 (4.444 m/s) in group 2, and A0003 (4.598 m/s) in group 3.

Step 8. Target time for 100 m at 105% of A0001's MAS = 100 / (4.444 × 1.05) = 21.43 s.

Result:

| Athlete | Test date | MAS (m/s) | MAS (km/h) | Distance, 105% for 30 s (m) | MSS (m/s) | ASR (m/s) | Days apart | Group |
|---|---|---|---|---|---|---|---|---|
| A0001 | 2026-09-01 | 4.444 | 16.00 | 140.0 | 8.90 | 4.456 | 2 | 2 |
| A0002 | 2026-09-29 | 4.255 | 15.32 | 134.0 | 8.50 | 4.245 | 26 | 1 |
| A0003 | 2026-09-01 | 4.598 | 16.55 | 144.8 | 9.10 | 4.502 | 2 | 3 |
| A0004 | none | | | | | | | |

All distances are straight-line distances.

## What changes the number

These choices change the result even when the athlete does not change:

- Reference test. For a made-up athlete with a 2,000 m MAS of 4.444 m/s and a VIFT of 20.0 km/h (5.556 m/s), 105% for 30 s gives 140.0 m from MAS and 175.0 m from VIFT.
- Which result counts. The run sheet uses the latest date. The best result or a mean of tests gives other distances. Say which rule you used.
- Turns. A distance run as shuttles is harder than the same distance in a straight line (Buchheit et al., 2011).
- Rounding. Rounding to 5 m or 10 m changes the true percentage for each athlete.
- Duplicate rows. Two trials on one date need a rule, such as the fastest or the mean. The run sheet stops and asks.

## Units and typical range

Report distances in m, speeds in m/s or km/h, and times in s. A distance has no typical range of its own. It follows from the reference speed, the percentage, and the work time. Check the reference speed against the ranges in `maximal-aerobic-speed.md` instead.

## Data you need

Collect this data:

- Source: a test table with athlete ID, test code, result, and date, plus the coach's choices.
- Sampling: one row per athlete per test per date. Store every trial, and name the rule for choosing one.
- Minimum data: one valid result on the chosen reference test per athlete.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this method:

- Choosing a percentage or work time for the coach. Ask for both.
- Presenting a study setting as the right setting. Name the study and its athletes.
- Mixing reference tests across athletes on one run sheet.
- Entering 105 where the formula expects 1.05, or the reverse. These formulas expect 105.
- Adding an unsourced shuttle correction.
- Using text dates. `MAXIFS` reads text dates as 0, and the athlete's row comes back blank.
- Numbering athletes in a sorted list, which turns a run sheet into a ranking.

## Example request

> Here is our test sheet with player, test, result, and date. Make me a run sheet in Google Sheets for 15 s runs at the percentage of 2 km MAS I type in, and split the squad at the speeds I give you.

## Check the result

Run these checks:

- Recompute one value by hand: 4.444 m/s × 1.05 × 30 s = 140.0 m.
- Check that a higher percentage or a longer work time gives a longer distance for every athlete.
- Check that every athlete in the input appears in the run sheet, with a blank and a note where the chosen test is missing.

## Sources

This file cites these sources:

- Blondel N, Berthoin S, Billat V, Lensel G. Relationship between run times to exhaustion at 90, 100, 120, and 140% of vVO2max and velocity expressed relatively to critical velocity and maximal velocity. International Journal of Sports Medicine. 2001;22(1):27-33. https://doi.org/10.1055/s-2001-11357 (accessed 2026-10-07)
- Buchheit M. The 30-15 intermittent fitness test: accuracy for individualizing interval training of young intermittent sport players. Journal of Strength and Conditioning Research. 2008;22(2):365-374. https://doi.org/10.1519/JSC.0b013e3181635b2e (accessed 2026-10-07)
- Buchheit M, Haydar B, Hader K, Ufland P, Ahmaidi S. Assessing running economy during field running with changes of direction: application to 20 m shuttle runs. International Journal of Sports Physiology and Performance. 2011;6(3):380-395. https://doi.org/10.1123/ijspp.6.3.380 (accessed 2026-10-07)
- Buchheit M, Laursen PB. High-intensity interval training, solutions to the programming puzzle: Part I: cardiopulmonary emphasis. Sports Medicine. 2013;43(5):313-338. https://doi.org/10.1007/s40279-013-0029-x (accessed 2026-10-07). Cited as Buchheit and Laursen, 2013a.
- Buchheit M, Laursen PB. High-intensity interval training, solutions to the programming puzzle. Part II: anaerobic energy, neuromuscular load and practical applications. Sports Medicine. 2013;43(10):927-954. https://doi.org/10.1007/s40279-013-0066-5 (accessed 2026-10-07). Cited as Buchheit and Laursen, 2013b.
- Collison J, Debenedictis T, Fuller JT, Gerschwitz R, Ling T, Gotch L, Bishop B, Sibley L, Russell J, Hobbs A, Bellenger CR. Supramaximal interval running prescription in Australian Rules Football players: a comparison between maximal aerobic speed, anaerobic speed reserve, and the 30-15 Intermittent Fitness Test. Journal of Strength and Conditioning Research. 2022;36(12):3409-3414. https://doi.org/10.1519/JSC.0000000000004103 (accessed 2026-10-07)
- Haydar B, Al Haddad H, Ahmaidi S, Buchheit M. Assessing inter-effort recovery and change of direction abilities with the 30-15 Intermittent Fitness Test. Journal of Sports Science and Medicine. 2011;10(2):346-354. https://pmc.ncbi.nlm.nih.gov/articles/PMC3761847/ (accessed 2026-10-07)
