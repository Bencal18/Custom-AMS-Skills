# Anaerobic speed reserve

Last checked: 2026-10-07

## What it measures

Anaerobic speed reserve (ASR) is the range of running speeds between an athlete's maximal aerobic speed (MAS) and maximal sprint speed (MSS). It shows how much faster than MAS the athlete can run (Sandford et al., 2019a; Sandford et al., 2021).

## Formula

Use these formulas:

```text
ASR (m/s)                  = MSS (m/s) - MAS (m/s)
Speed reserve ratio (SRR)  = MSS (m/s) / MAS (m/s)
Speed at q% of ASR (m/s)   = MAS (m/s) + (q / 100) x ASR (m/s)
Percent of ASR at a speed  = (speed - MAS) / ASR x 100
```

Define every term in the formula:

- `MSS`: maximal sprint speed, the fastest speed the athlete reaches in an all-out sprint, in m/s. Bundle et al. (2003) took it as the fastest speed over a burst of 8 steps, about 3 s or less.
- `MAS`: maximal aerobic speed from a continuous test, in m/s. See `maximal-aerobic-speed.md`. Do not use the 30-15 IFT speed (VIFT) or a Yo-Yo result as MAS.
- `ASR`: anaerobic speed reserve, in m/s.
- `SRR`: speed reserve ratio, with no unit. Sandford et al. (2019a) defined it as MSS / MAS.
- `q`: a percentage of ASR that the coach chooses.

Blondel et al. (2001) expressed running speed as a percentage of the difference between maximal speed and vVO2max, which is the same range. The "speed at q% of ASR" formula follows from that definition.

### Why ASR changes what a percentage of MAS means

Two athletes with the same MAS can have different sprint speeds. At the same percentage of MAS, the faster sprinter uses a smaller share of their reserve. In 10 participants, time to exhaustion at 120% and 140% of vVO2max varied between people. It correlated most closely with speed expressed as a percentage of this reserve (r = −0.83 and −0.94) (Blondel et al., 2001).

Sandford et al. (2021) argue that above MAS the proportion of ASR used likely matters more than the percentage of MAS. That is a review argument, not a tested rule for every sport.

### Where maximal sprint speed comes from

Use one source of MSS for every athlete on one sheet. Ask the user which one they used:

- A sprint test with radar, a laser, or timing gates. If the `sprint-testing` skill is installed, use it. Timing gates give the average speed over a split, which is lower than the peak speed inside that split. Name the split.
- The highest valid GPS speed. If the `gps-running-load` skill is installed, follow its speed units and checks in its high speed running reference. Ask how the user decided a speed was valid, and over what period they took the highest value. Reardon et al. (2015), cited in that file, took maximum speed from all training and match data over a season.

GPS and sprint test speeds come from different systems. Do not mix them in one column, and do not compare an ASR from one with an ASR from the other.

Take MAS and MSS close together in time. Sandford et al. (2019b) set their laboratory test within 6 weeks of the race they compared it with. That is a study setting, not a rule. Show the days between the two tests next to each ASR.

### Calculate it in a spreadsheet

Use the run sheet in `interval-distances.md`. It finds each athlete's latest MAS and MSS from a test table. With MAS in `D2` and MSS in `H2`, both in m/s, use these formulas. They return a blank when either value is missing:

```text
ASR (m/s):            =IF(AND(ISNUMBER(D2),ISNUMBER(H2)),H2-D2,"")
SRR:                  =IF(AND(ISNUMBER(D2),ISNUMBER(H2),D2>0),H2/D2,"")
Speed at q% of ASR:   =IF(AND(ISNUMBER(I2),ISNUMBER(settings!$B$5)),D2+settings!$B$5/100*I2,"")
```

`I2` holds ASR. `settings!$B$5` holds the percentage of ASR the coach chose. Leave it blank until the coach enters one.

### Calculate it in Power BI and Tableau

These versions use the `MAS 2000 m TT (m/s)` measure from `maximal-aerobic-speed.md`. MSS is `measure_name` `max_sprint_speed` in `m/s`, from one source only. They take the highest MSS on the latest MSS test date.

In Power BI, use these DAX measures. `ASR percent` is a what-if parameter the coach sets:

```text
MSS (m/s) =
VAR lastDate =
    CALCULATE (
        MAX ( measures[measure_date] ),
        measures[measure_name] = "max_sprint_speed",
        measures[unit] = "m/s",
        measures[status] = "ok"
    )
RETURN
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "max_sprint_speed",
        measures[unit] = "m/s",
        measures[status] = "ok",
        measures[measure_date] = lastDate
    )

ASR (m/s) =
VAR mas = [MAS 2000 m TT (m/s)]
VAR mss = [MSS (m/s)]
RETURN IF ( NOT ISBLANK ( mas ) && NOT ISBLANK ( mss ), mss - mas )

Speed at chosen % ASR (m/s) =
VAR q = SELECTEDVALUE ( 'ASR percent'[ASR percent] )
VAR asr = [ASR (m/s)]
RETURN IF ( NOT ISBLANK ( q ) && NOT ISBLANK ( asr ), [MAS 2000 m TT (m/s)] + q / 100 * asr )
```

In Tableau, add a parameter `[ASR percent]` that the coach sets, and use these calculations. Put `athlete_id` on the view, and use `MIN` of each:

```text
Latest MSS date:
{ FIXED [athlete_id] :
  MAX(IF [measure_name] = "max_sprint_speed" AND [unit] = "m/s" AND [status] = "ok"
      THEN [measure_date] END) }

MSS (m/s):
{ FIXED [athlete_id] :
  MAX(IF [measure_name] = "max_sprint_speed" AND [unit] = "m/s" AND [status] = "ok"
      AND [measure_date] = [Latest MSS date] THEN [value] END) }

ASR (m/s):
[MSS (m/s)] - [MAS 2000 m TT (m/s)]

Speed at chosen % ASR (m/s):
[MAS 2000 m TT (m/s)] + [ASR percent] / 100 * [ASR (m/s)]
```

A null MAS or MSS gives a null result in both tools. A Tableau parameter always holds a value, so the coach must set it before reading the result.

### Calculate it in Python

```python
def asr_m_s(mss_m_s, mas_m_s):
    """Return ASR in m/s, or None when an input is missing."""
    if mss_m_s is None or mas_m_s is None:
        return None
    return mss_m_s - mas_m_s

def speed_at_asr_percent(mas_m_s, asr, q):
    """q is the percentage of ASR the coach chose."""
    return mas_m_s + q / 100 * asr
```

## Calculate the metric

Follow these steps to calculate ASR:

1. Get MAS in m/s from a continuous test, with its test name and date.
2. Get MSS in m/s, with its source and date. Convert km/h by dividing by 3.6.
3. Confirm MSS is higher than MAS.
4. Subtract MAS from MSS to get ASR.
5. Divide MSS by MAS to get SRR, if the user asks for it.
6. If the coach gives a percentage of ASR, add that share of ASR to MAS.
7. Show the days between the MAS test and the MSS test.

## Worked example

This example uses made-up results for two athletes with the same MAS.

| Input | Athlete 1 | Athlete 2 |
|---|---|---|
| MAS, 2,000 m time trial in 450 s | 4.444 m/s | 4.444 m/s |
| MSS, radar sprint test | 8.00 m/s | 9.40 m/s |

Step 1. ASR for athlete 1 = 8.00 − 4.444 = 3.556 m/s. ASR for athlete 2 = 9.40 − 4.444 = 4.956 m/s.

Step 2. SRR for athlete 1 = 8.00 / (2000 / 450) = 1.800. SRR for athlete 2 = 9.40 / (2000 / 450) = 2.115. These use MAS before rounding to 4.444 m/s.

Step 3. The coach picks 120% of MAS. Speed = 4.444 × 1.20 = 5.333 m/s for both athletes.

Step 4. As a share of ASR, 5.333 m/s is (5.333 − 4.444) / 3.556 × 100 = 25.0% for athlete 1 and (5.333 − 4.444) / 4.956 × 100 = 17.9% for athlete 2.

Step 5. The coach picks 20% of ASR instead. Speed = 4.444 + 0.20 × 3.556 = 5.156 m/s for athlete 1, and 4.444 + 0.20 × 4.956 = 5.436 m/s for athlete 2.

Result: ASR is 3.556 m/s for athlete 1 and 4.956 m/s for athlete 2. The same percentage of MAS uses 25.0% and 17.9% of their reserves.

## What changes the number

These choices change the result even when the athlete does not change:

- MSS source. In a made-up case with MAS 4.444 m/s, a radar MSS of 8.90 m/s gives ASR 4.456 m/s. A GPS top speed of 8.60 m/s gives 4.156 m/s.
- MAS test. Using VIFT in place of MAS shrinks ASR, because VIFT is faster than MAS. Use a continuous test for MAS.
- Timing gate split. The average speed over a split is lower than the peak speed inside it.
- Time between tests. Fitness and speed can change between a MAS test and a sprint test weeks apart.
- Units. MSS in km/h minus MAS in m/s gives a meaningless number. Convert both to m/s first.

## Units and typical range

Report ASR in m/s or km/h, and name the MAS test and the MSS source. SRR has no unit.

| Population | Typical range | Source |
|---|---|---|
| 19 elite 800 m and 1,500 m runners, MSS from 50 m sprint, MAS predicted from 1,500 m race | SRR of 1.36 to 1.58 or more across 3 subgroups: 400 to 800 m runners ≥ 1.58, 800 m runners 1.48 to 1.57, 800 to 1,500 m runners 1.36 to 1.47 | Sandford et al., 2019a |

This file has no verified ASR range for team-sport athletes. Team-sport athletes can fall outside the runners' range for real reasons. Use the range to catch unit errors, not to rate athletes.

## Data you need

Collect this data:

- Source: MAS from a continuous test, and MSS from one sprint system, each with a date.
- Sampling: for GPS MSS, the device's sampling rate and the rule used to reject spikes. For radar or gates, the split or window used.
- Minimum data: one valid MAS and one valid MSS per athlete, taken close together in time.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using VIFT or a Yo-Yo result as MAS. Use MAS from a continuous test.
- Subtracting a km/h value from an m/s value. Convert both to m/s.
- Mixing GPS top speeds and sprint test speeds in one MSS column.
- Writing "20% ASR" and computing 20% of ASR alone. The speed is MAS plus 20% of ASR.
- Using an MSS from last season with this month's MAS without saying so.

## Example request

> I have 2 km time trial MAS and 40 m radar top speed for my squad. Can you work out each player's ASR in Excel, and show what speed 25% of ASR is for each of them?

## Check the result

Run these checks:

- Recompute one value by hand: 8.90 − 4.444 = 4.456 m/s.
- Check that ASR is above 0 for every athlete. A value at or below 0 means a unit error or a wrong column.
- Check that SRR is above 1. Compare any SRR far from the range above with the athlete's own earlier values before you trust it.

## Sources

This file cites these sources:

- Blondel N, Berthoin S, Billat V, Lensel G. Relationship between run times to exhaustion at 90, 100, 120, and 140% of vVO2max and velocity expressed relatively to critical velocity and maximal velocity. International Journal of Sports Medicine. 2001;22(1):27-33. https://doi.org/10.1055/s-2001-11357 (accessed 2026-10-07)
- Bundle MW, Hoyt RW, Weyand PG. High-speed running performance: a new approach to assessment and prediction. Journal of Applied Physiology. 2003;95(5):1955-1962. https://doi.org/10.1152/japplphysiol.00921.2002 (accessed 2026-10-07)
- Reardon C, Tobin DP, Delahunt E. Application of individualized speed thresholds to interpret position specific running demands in elite professional rugby union: a GPS study. PLoS ONE. 2015;10(7):e0133410. https://doi.org/10.1371/journal.pone.0133410 (accessed 2026-10-07)
- Sandford GN, Allen SV, Kilding AE, Ross A, Laursen PB. Anaerobic speed reserve: a key component of elite male 800-m running. International Journal of Sports Physiology and Performance. 2019;14(4):501-508. https://doi.org/10.1123/ijspp.2018-0163 (accessed 2026-10-07). Cited as Sandford et al., 2019a.
- Sandford GN, Rogers SA, Sharma AP, Kilding AE, Ross A, Laursen PB. Implementing anaerobic speed reserve testing in the field: validation of vVO2max prediction from 1500-m race performance in elite middle-distance runners. International Journal of Sports Physiology and Performance. 2019;14(8):1147-1150. https://doi.org/10.1123/ijspp.2018-0553 (accessed 2026-10-07). Cited as Sandford et al., 2019b.
- Sandford GN, Laursen PB, Buchheit M. Anaerobic speed/power reserve and sport performance: scientific basis, current applications and future directions. Sports Medicine. 2021;51(10):2017-2028. https://doi.org/10.1007/s40279-021-01523-9 (accessed 2026-10-07)
