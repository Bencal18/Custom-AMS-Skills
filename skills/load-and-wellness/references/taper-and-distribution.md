# Taper volume reduction and intensity distribution

Last checked: 2026-10-07

## What it measures

This file covers two descriptions of a training block:

- Taper volume reduction: how much weekly training volume dropped in a taper, as a percentage of normal training. A taper is a planned cut in training before a competition.
- Intensity distribution: how one week's or one block's training time was spread across low, moderate, and high intensity, with a label such as pyramidal or polarized.

Both describe what was done. Neither says what should be done. The coach makes every training decision.

Read these limits before you use them:

- Published taper results are study settings, not recommendations. A meta-analysis of 27 studies of competitive athletes found the largest performance effect for a 2-week taper in which training volume was reduced exponentially by 41% to 60%, with intensity and frequency kept the same (Bosquet et al., 2007). Its authors say this seems to be the most efficient strategy. That is a pooled finding, not a target for any athlete.
- Team sports may differ. A meta-analysis of 14 team-sport studies found that tapering improved maximal power, maximal oxygen uptake, repeated sprint ability, and change of direction speed. Its authors state that the literature lacks studies comparing taper strategies, so it cannot yet support evidence-based recommendations (Vachon et al., 2021).
- The intensity distribution labels come from research on elite endurance athletes (Sperlich et al., 2023). A label describes a week. It does not say which distribution is better for a team-sport athlete.
- The zone model and the input change the label. Sperlich et al. (2023) state that the distribution obtained depends heavily on the method used. Name both with every result.

Tapering is common practice:

- 91% of 58 strength and conditioning practitioners from 9 Southeast and East Asian countries reported applying tapers (Washif et al., 2025).
- 99% of 146 competitive weightlifters reported using a taper. Their reported taper lasted 8.0 ± 4.4 days and cut training volume by 43.1 ± 14.6% (Winwood et al., 2023).

## Formula

### Taper volume reduction

```text
reduction_pct = (baseline_weekly_volume − taper_weekly_volume) ÷ baseline_weekly_volume × 100
```

Define every term in the formula:

- `baseline_weekly_volume`: the mean weekly volume over the baseline weeks, the normal training before the taper. Name the weeks, such as 2026-08-03 to 2026-08-30.
- `taper_weekly_volume`: the volume of one taper week, or the mean weekly volume across all taper weeks. Name which.
- Volume unit: one of training minutes, distance (m), volume load (sets × reps × kg, in kg), or session RPE load (AU). Name the unit. Use one unit for baseline and taper.
- `reduction_pct`: the result, in percent. A positive value is a cut. A negative value means the taper week had more volume than baseline.

Choose the baseline weeks with the user. If the user has no preference, use the 4 full calendar weeks before the taper starts, and label that as this file's choice. No source we read sets the baseline window. A single week, or the peak week, gives a different answer.

Choose the volume unit with care. Session RPE load is RPE × minutes (see [session-rpe-load.md](session-rpe-load.md)), so it falls when sessions get shorter and also when they feel easier. A drop in session RPE load cannot tell you whether volume, intensity, or both fell. To keep volume and intensity apart, measure volume in minutes, distance, or volume load. If the user wants session RPE load, report it with the minutes and the intensity beside it.

Track intensity and frequency separately from volume. Bosquet et al. (2007) treated volume, intensity, and frequency as separate parts of a taper. Use these measures, and name them:

```text
frequency_change_pct = (taper_sessions_per_week − baseline_sessions_per_week) ÷ baseline_sessions_per_week × 100
intensity_au_per_min = weekly session RPE load ÷ weekly training minutes
```

`intensity_au_per_min` is the time-weighted mean session RPE for the week, on the CR-10 scale. It is this file's choice of intensity measure for session RPE data, and no source sets it. Other intensity measures are time above a heart rate or speed threshold, or the share of time in zone 3 from the distribution below. Name the one you use.

### Intensity distribution

Intensity distribution is the share of training in each of three intensity zones:

- Z1: low intensity.
- Z2: moderate intensity.
- Z3: high intensity.

Sperlich et al. (2023) describe this three-zone model as the one most often used in research. They state that no standard criteria separate the zones. Boundaries have been set from maximal values, such as maximal heart rate, and from thresholds, such as lactate or ventilatory thresholds.

Calculate the shares this way:

```text
total = Z1_time + Z2_time + Z3_time
Z1_share = Z1_time ÷ total      (the same for Z2 and Z3)
```

Label the distribution from the order of the three zones. Sperlich et al. (2023) used these labels:

| Label | Order of the zones | Extra condition |
|---|---|---|
| No Z3 | Z1 > Z2 | Z3 = 0 |
| Pyramidal | Z1 > Z2 > Z3 | None |
| Polarized | Z1 > Z3 > Z2 | Polarization index above 2.00 |
| Threshold | Z2 > Z1 > Z3 | None |
| Z2 and Z3 even | Z2 = Z3 | Z2 and Z3 above 0 |
| Other | Any other order, or Z1 > Z3 > Z2 with an index of 2.00 or less | None |

Sperlich et al. (2023) used "no Z3" for two-zone models with Z1 > Z2. This file applies it to any week with Z3 = 0 and Z1 > Z2, including a week with all time in Z1, and checks it before pyramidal. That order is this file's choice. Sperlich et al. (2023) write threshold as Z2 > Z1 = Z3 in the abstract, but as Z2 > Z1 > Z3 in the methods. This file follows the methods.

The polarization index (PI) comes from Treff et al. (2019). Use the zone shares as fractions from 0 to 1:

```text
PI = log10(Z1_share ÷ Z2_share × Z3_share × 100)
```

Apply the rules Treff et al. (2019) give:

- If Z2 is 0 and Z3 is above 0, report PI as the text "not defined". Treff et al. give a separate formula for this case, but they print it without clear brackets, so this file does not calculate it.
- If Z3 is 0, PI is 0.
- If Z3 is larger than Z1, report PI as the text "not valid". Do not calculate it.
- PI above 2.00 marks the distribution as polarized. PI of 2.00 or less marks it as not polarized.

A week with Z1 > Z3 and Z2 = 0 has no defined PI, so it cannot meet the polarized condition. Label it other, and say that PI is not defined because Z2 is 0.

PI has no unit (Treff et al. write it as arbitrary units). It is a label rule, not a load. Keep "not defined", "not valid", and an incomplete week apart. An incomplete week gives a blank, not a PI.

### Choose the zone input

Three inputs are in use. Each one can give a different label for the same week:

- Heart rate time in zone. Start from the minutes in each heart rate zone, as [heart-rate-load.md](heart-rate-load.md#time-in-zone) calculates them. Group them into three zones.
- Session RPE. Put each session into a zone from its CR-10 rating. Count either the session minutes or the number of sessions in each zone.
- Session goal. The coach tags each session as low, moderate, or high from the plan. Count minutes or sessions.

Sperlich et al. (2023) list these methods, among others: heart rate time in zone, heart rate session goal, session RPE by number of sessions, and RPE time in zone. Name the input and the counting unit, minutes or sessions, with every result.

Group heart rate zones into three zones this way:

- Lucia zones: when each athlete has lab thresholds, the three phases of Lucia TRIMP in [heart-rate-load.md](heart-rate-load.md#lucia-trimp) already form a three-zone model. Below VT is Z1. VT to RCP is Z2. Above RCP is Z3.
- Edwards zones: when you only have %HRmax zones, ask the user how to group them. If the user has no rule, offer this grouping, and label it as this file's choice: below 50% and Edwards zones 1 to 3 (below 80% HRmax) as Z1, zone 4 (80% to 90%) as Z2, and zone 5 (90% and above) as Z3. No source we read sets a %HRmax grouping.
- Five-zone threshold models: Sperlich et al. (2023) combined zones 3, 4, and 5 of a five-zone model into Z3 when all three lay above the anaerobic threshold. Follow the user's zone definitions, and say how you grouped them.

Group session RPE into three zones with the user's CR-10 bands. If the user has none, offer CR-10 ratings 0 to 4 as Z1, 5 and 6 as Z2, and 7 to 10 as Z3, and label it as this file's choice. No source we read sets these bands.

Choose the window with the user: a calendar week, a block of weeks, or a season phase. If the user has no preference, use Monday-to-Sunday calendar weeks, as [monotony-and-strain.md](monotony-and-strain.md#choose-calendar-or-rolling-weeks) does, and label that as this file's choice.

### Calculate it in a spreadsheet

Use these formulas in Excel or Google Sheets.

For the taper, use one row per athlete per week. Put `athlete_id` in column `A`, the week start date in column `B`, the phase in column `C` (`baseline`, `taper`, or blank), and the weekly volume in column `D`. Leave a week with missing data blank. Enter these formulas in row 2 and fill them down:

```text
Baseline weeks, E2:  =COUNTIFS($A:$A,A2,$C:$C,"baseline")
Baseline mean, F2:   =IF(OR(E2=0,COUNTIFS($A:$A,A2,$C:$C,"baseline",$D:$D,"")>0),"",AVERAGEIFS($D:$D,$A:$A,A2,$C:$C,"baseline"))
Reduction %, G2:     =IF(OR(C2<>"taper",F2="",NOT(ISNUMBER(D2)),F2<=0),"",(F2-D2)/F2*100)
```

`COUNTIFS` with `""` counts the blank volume cells in the baseline weeks. A baseline with any blank week gives a blank mean, so a missing week is never read as a light week. A baseline of 0 or less gives a blank reduction, because a percentage of 0 is not defined. Add the sessions per week and the minutes in their own columns, and use the same formulas for frequency.

For the distribution, use one row per athlete per week with the minutes in each source zone. For Edwards zones, put the minutes below 50% in `B` and zones 1 to 5 in `C` to `G`. These formulas use the default grouping above:

```text
Complete, H2:  =COUNT(B2:G2)=6
Z1, I2:        =IF(H2,SUM(B2:E2),"")
Z2, J2:        =IF(H2,F2,"")
Z3, K2:        =IF(H2,G2,"")
Total, L2:     =IF(H2,I2+J2+K2,"")
PI, M2:        =IF(OR(NOT(H2),L2=0),"",IF(K2=0,0,IF(K2>I2,"not valid",IF(J2=0,"not defined",LOG10((I2/L2)/(J2/L2)*(K2/L2)*100)))))
Label, N2:     =IF(OR(NOT(H2),L2=0),"",IF(AND(K2=0,I2>J2),"no Z3",IF(AND(I2>J2,J2>K2),"pyramidal",IF(AND(I2>K2,K2>J2,ISNUMBER(M2)),IF(ROUND(M2,9)>2,"polarized","other"),IF(AND(J2>I2,I2>K2),"threshold",IF(AND(J2=K2,J2>0),"Z2 and Z3 even","other"))))))
```

`ROUND(M2,9)` stops rounding error from turning an index of exactly 2.00 into 2.0000000001. An incomplete week gives a blank in `M2`, so it stays apart from the text "not valid" and "not defined". A plain `=SUM(B2:E2)` turns a blank zone into 0 minutes, so the `Complete` test comes first.

For session RPE zones, put the CR-10 rating in column `C`, the top of Z1 in cell `P1`, and the top of Z2 in cell `P2`:

```text
Zone, E2: =IF(NOT(ISNUMBER(C2)),"",IF(C2<=$P$1,1,IF(C2<=$P$2,2,3)))
```

Then add the minutes per athlete, week, and zone with `SUMIFS`, or count sessions with `COUNTIFS`.

### Calculate it in Python

Use these functions:

```python
import math
import pandas as pd

def taper_reduction(weeks, value="volume"):
    """weeks: one row per athlete per week with athlete_id, week_start, phase, and value.
    phase is "baseline", "taper", or empty. Missing volume stays NaN."""
    base = weeks[weeks["phase"] == "baseline"].groupby("athlete_id")[value]
    baseline = base.mean().where(base.count() == base.size())   # any missing week -> NaN
    taper = weeks[weeks["phase"] == "taper"].copy()
    taper["baseline"] = taper["athlete_id"].map(baseline)
    valid = taper["baseline"].where(taper["baseline"] > 0)       # baseline of 0 or less -> NaN
    taper["reduction_pct"] = (valid - taper[value]) / valid * 100
    return taper

def polarization_index(z1, z2, z3):
    total = z1 + z2 + z3
    if total <= 0:
        return None                      # incomplete or empty week
    f1, f2, f3 = z1 / total, z2 / total, z3 / total
    if f3 == 0:
        return 0.0
    if f3 > f1:
        return "not valid"               # Treff et al., 2019
    if f2 == 0:
        return "not defined"             # the source's Z2 = 0 formula is ambiguous
    return math.log10(f1 / f2 * f3 * 100)

def distribution_label(z1, z2, z3):
    if z1 + z2 + z3 <= 0:
        return None, None
    pi = polarization_index(z1, z2, z3)
    if z3 == 0 and z1 > z2:
        return "no Z3", pi
    if z1 > z2 > z3:
        return "pyramidal", pi
    if z1 > z3 > z2 and isinstance(pi, float) and round(pi, 9) > 2:
        return "polarized", pi
    if z2 > z1 > z3:
        return "threshold", pi
    if z2 == z3 and z2 > 0:
        return "Z2 and Z3 even", pi
    return "other", pi
```

Build the zone minutes for each athlete and week first, from complete sessions only. Report every dropped session, and how many sessions had missing heart rate or RPE.

### Calculate it in Power BI and Tableau

These versions follow the spreadsheet and Python rules. A baseline with a missing week gives a blank. The label needs all three zone totals.

For the taper, use a `weeks` table with one row per athlete per week: `athlete_id`, `week_start`, `phase`, and `volume`. Put `athlete_id` and `week_start` in the visual. In Power BI, use these DAX measures:

```text
Week volume =
IF ( HASONEVALUE ( weeks[week_start] ) && COUNTROWS ( weeks ) = 1, MAX ( weeks[volume] ) )

Baseline weekly volume =
VAR n = CALCULATE ( COUNTROWS ( weeks ), weeks[phase] = "baseline", REMOVEFILTERS ( weeks[week_start] ) )
VAR missing = CALCULATE ( COUNTROWS ( weeks ), weeks[phase] = "baseline", ISBLANK ( weeks[volume] ), REMOVEFILTERS ( weeks[week_start] ) )
RETURN IF ( n > 0 && missing = 0, CALCULATE ( AVERAGE ( weeks[volume] ), weeks[phase] = "baseline", REMOVEFILTERS ( weeks[week_start] ) ) )

Reduction % =
VAR b = [Baseline weekly volume]
VAR w = [Week volume]
RETURN IF ( SELECTEDVALUE ( weeks[phase] ) = "taper" && b > 0 && NOT ISBLANK ( w ), ( b - w ) / b * 100 )
```

`ISBLANK` is used on purpose. In DAX, `weeks[volume] = BLANK()` is also true for 0, so it would count a real zero week as missing.

In Tableau, use these calculations on the same table:

```text
Baseline missing weeks (FIXED LOD):
{ FIXED [athlete_id] : SUM(IF [phase] = "baseline" AND ISNULL([volume]) THEN 1 ELSE 0 END) }

Baseline weekly volume (FIXED LOD):
{ FIXED [athlete_id] : AVG(IF [phase] = "baseline" THEN [volume] END) }

Reduction % (row level):
IF [phase] = "taper" AND [Baseline missing weeks] = 0 AND [Baseline weekly volume] > 0
   AND NOT ISNULL([volume])
THEN ([Baseline weekly volume] - [volume]) / [Baseline weekly volume] * 100
END
```

A FIXED calculation runs before dimension filters, so a filter that shows only the taper weeks does not remove the baseline weeks. A context filter does remove them. Do not put the week on a context filter.

For the distribution, use a `zone_time` table with one row per athlete, week, and three-zone code: `athlete_id`, `week_start`, `zone3` (1, 2, or 3), and `minutes`. Build `zone3` from your grouping before you load the table. In Power BI, use these DAX measures:

```text
Z1 min = CALCULATE ( SUM ( zone_time[minutes] ), zone_time[zone3] = 1 ) + 0
Z2 min = CALCULATE ( SUM ( zone_time[minutes] ), zone_time[zone3] = 2 ) + 0
Z3 min = CALCULATE ( SUM ( zone_time[minutes] ), zone_time[zone3] = 3 ) + 0

Polarization index =
VAR t = [Z1 min] + [Z2 min] + [Z3 min]
VAR f1 = DIVIDE ( [Z1 min], t )
VAR f2 = DIVIDE ( [Z2 min], t )
VAR f3 = DIVIDE ( [Z3 min], t )
RETURN
    SWITCH (
        TRUE (),
        t = 0, BLANK (),
        f3 = 0, 0,
        f3 > f1, BLANK (),
        f2 = 0, BLANK (),
        LOG10 ( f1 / f2 * f3 * 100 )
    )

PI status =
VAR t = [Z1 min] + [Z2 min] + [Z3 min]
RETURN
    SWITCH (
        TRUE (),
        t = 0, BLANK (),
        [Z3 min] = 0, "calculated",
        [Z3 min] > [Z1 min], "not valid",
        [Z2 min] = 0, "not defined",
        "calculated"
    )

Distribution label =
VAR z1 = [Z1 min]
VAR z2 = [Z2 min]
VAR z3 = [Z3 min]
VAR pi = [Polarization index]
RETURN
    SWITCH (
        TRUE (),
        z1 + z2 + z3 = 0, BLANK (),
        z3 = 0 && z1 > z2, "no Z3",
        z1 > z2 && z2 > z3, "pyramidal",
        z1 > z3 && z3 > z2 && NOT ISBLANK ( pi ) && ROUND ( pi, 9 ) > 2, "polarized",
        z2 > z1 && z1 > z3, "threshold",
        z2 = z3 && z2 > 0, "Z2 and Z3 even",
        "other"
    )
```

In Tableau, use these calculations:

```text
Z1 min (aggregate): ZN(SUM(IF [zone3] = 1 THEN [minutes] END))
Z2 min (aggregate): ZN(SUM(IF [zone3] = 2 THEN [minutes] END))
Z3 min (aggregate): ZN(SUM(IF [zone3] = 3 THEN [minutes] END))

Polarization index (aggregate):
IF [Z1 min] + [Z2 min] + [Z3 min] = 0 THEN NULL
ELSEIF [Z3 min] = 0 THEN 0
ELSEIF [Z3 min] > [Z1 min] THEN NULL
ELSEIF [Z2 min] = 0 THEN NULL
ELSE LOG([Z1 min] / [Z2 min] * ([Z3 min] / ([Z1 min] + [Z2 min] + [Z3 min])) * 100)
END

PI status (aggregate):
IF [Z1 min] + [Z2 min] + [Z3 min] = 0 THEN NULL
ELSEIF [Z3 min] = 0 THEN "calculated"
ELSEIF [Z3 min] > [Z1 min] THEN "not valid"
ELSEIF [Z2 min] = 0 THEN "not defined"
ELSE "calculated"
END

Distribution label (aggregate):
IF [Z1 min] + [Z2 min] + [Z3 min] = 0 THEN NULL
ELSEIF [Z3 min] = 0 AND [Z1 min] > [Z2 min] THEN "no Z3"
ELSEIF [Z1 min] > [Z2 min] AND [Z2 min] > [Z3 min] THEN "pyramidal"
ELSEIF [Z1 min] > [Z3 min] AND [Z3 min] > [Z2 min] AND NOT ISNULL([Polarization index])
       AND ROUND([Polarization index], 9) > 2 THEN "polarized"
ELSEIF [Z2 min] > [Z1 min] AND [Z1 min] > [Z3 min] THEN "threshold"
ELSEIF [Z2 min] = [Z3 min] AND [Z2 min] > 0 THEN "Z2 and Z3 even"
ELSE "other"
END
```

`LOG` with one argument is base 10 in Tableau, as `LOG10` is in DAX. A measure in DAX or Tableau cannot mix numbers and text, so `PI status` holds the text "not valid" or "not defined" beside the numeric index. Show both. An incomplete week gives a blank status. `Z1_share ÷ Z2_share` equals `Z1 min ÷ Z2 min`, so the last line uses the minutes directly. Put `athlete_id` and `week_start` on Rows. A week with no rows in `zone_time` shows a blank, not a label. A missing row for one zone counts as 0 minutes in both tools, so load complete weeks only, with a 0 row for any zone the athlete did not reach.

Show the results this way in both tools:

- Name the zone input, the grouping, and the counting unit, such as `heart rate time in zone, Edwards zones grouped 1-3 / 4 / 5, minutes`.
- Show the three zone minutes and shares next to the label.
- Show the baseline weeks, the volume unit, and the intensity and frequency next to every reduction.
- Do not add color bands, targets, or labels such as good or bad.

## Calculate taper reduction and distribution

Follow these steps to calculate the metrics from raw inputs:

1. Ask the user which weeks are baseline and which are taper. Offer the 4 full calendar weeks before the taper as the baseline if they have none, and label it as this file's choice.
2. Ask for the volume unit: minutes, distance, volume load, or session RPE load.
3. Add each athlete's sessions into weekly totals for volume, minutes, session count, and session RPE load. Keep a week with any missing session value as missing.
4. Calculate the baseline weekly volume as the mean of the baseline weeks. Report it as missing if any baseline week is missing.
5. Calculate `reduction_pct` for each taper week, and for the mean of the taper weeks.
6. Calculate the frequency change and the intensity measure for the same weeks.
7. For the distribution, ask which input to use: heart rate time in zone, session RPE, or session goal. Ask whether to count minutes or sessions.
8. Ask how to group the source zones into three zones. Offer the defaults in this file if the user has none, and label them as this file's choice.
9. Add each athlete's minutes, or sessions, in Z1, Z2, and Z3 for each week or block.
10. Calculate the shares, the polarization index, and the label.
11. Report the label with the three zone totals, the shares, the input, the grouping, the counting unit, and the window.

## Worked example

One athlete's weekly totals for 4 baseline weeks and a 2-week taper, from Monday 2026-08-03. Volume is in training minutes. Session RPE load is shown beside it.

| Week | Phase | Minutes | Session RPE load (AU) | Sessions | AU per minute |
|---|---|---|---|---|---|
| 2026-08-03 | Baseline | 480 | 3,120 | 6 | 6.50 |
| 2026-08-10 | Baseline | 510 | 3,340 | 6 | 6.55 |
| 2026-08-17 | Baseline | 460 | 2,980 | 6 | 6.48 |
| 2026-08-24 | Baseline | 500 | 3,260 | 6 | 6.52 |
| 2026-08-31 | Taper | 330 | 2,050 | 6 | 6.21 |
| 2026-09-07 | Taper | 240 | 1,560 | 5 | 6.50 |

Work out the taper step by step:

- Baseline weekly minutes: (480 + 510 + 460 + 500) ÷ 4 = 487.5 min.
- Taper week 1: (487.5 − 330) ÷ 487.5 × 100 = 32.3% reduction.
- Taper week 2: (487.5 − 240) ÷ 487.5 × 100 = 50.8% reduction.
- Taper mean: (330 + 240) ÷ 2 = 285 min, so (487.5 − 285) ÷ 487.5 × 100 = 41.5% reduction.
- In session RPE load, the baseline mean is 3,175 AU and the taper mean is 1,805 AU, a 43.1% reduction.
- Frequency: 6 sessions a week at baseline, 6 then 5 in the taper, a 0% then 16.7% drop.
- Intensity: 12,700 AU ÷ 1,950 min = 6.51 AU per minute at baseline, and 3,610 AU ÷ 570 min = 6.33 in the taper, a 2.8% drop.

The minutes fell by 41.5% and the session RPE load by 43.1%. Most of the drop in load came from shorter sessions, not lower ratings.

One week of the same athlete, Monday 2026-08-17, has six sessions and 325 minutes in all. Heart rate time in Edwards zones, grouped with this file's default:

| Edwards zone | Minutes | Three-zone group |
|---|---|---|
| Below 50% | 40 | Z1 |
| 1 (50% to 60%) | 70 | Z1 |
| 2 (60% to 70%) | 85 | Z1 |
| 3 (70% to 80%) | 70 | Z1 |
| 4 (80% to 90%) | 40 | Z2 |
| 5 (90% and above) | 20 | Z3 |

The heart rate input gives these results:

- Z1 = 265 min (81.5%), Z2 = 40 min (12.3%), Z3 = 20 min (6.2%).
- Order: Z1 > Z2 > Z3, so the label is pyramidal.
- PI = log10(0.8154 ÷ 0.1231 × 0.0615 × 100) = log10(40.77) = 1.61.

The same six sessions by CR-10 rating, with this file's default bands:

| Session | CR-10 | Minutes | Zone |
|---|---|---|---|
| 1 | 3 | 70 | Z1 |
| 2 | 4 | 80 | Z1 |
| 3 | 3 | 60 | Z1 |
| 4 | 7 | 45 | Z3 |
| 5 | 8 | 40 | Z3 |
| 6 | 6 | 30 | Z2 |

The RPE input gives these results:

- By minutes: Z1 = 210 min (64.6%), Z2 = 30 min (9.2%), Z3 = 85 min (26.2%).
- Order: Z1 > Z3 > Z2. PI = log10(0.6462 ÷ 0.0923 × 0.2615 × 100) = 2.26, above 2.00, so the label is polarized.
- By number of sessions: 3, 1, and 2. Order Z1 > Z3 > Z2, but PI = log10(0.5 ÷ 0.1667 × 0.3333 × 100) = 2.00, not above 2.00, so the label is other.

One week gives three labels: pyramidal from heart rate minutes, polarized from RPE minutes, and other from RPE session counts. Heart rate time in Z3 (20 min) is much smaller than RPE time in Z3 (85 min). Name the input and the counting unit with every label.

## What changes the number

These choices change the result even when the training does not:

- Baseline weeks. In session RPE load, the taper mean is a 43.1% cut against the 4-week mean, 44.6% against the last baseline week (3,260 AU), and 46.0% against the peak week (3,340 AU).
- Week-on-week instead of against baseline. Taper week 2 is a 50.9% cut against baseline but a 23.9% cut against taper week 1, in session RPE load.
- Volume unit. Minutes fell 41.5%. Session RPE load fell 43.1%, because it also carries the small drop in intensity.
- Taper weeks one by one or as a mean. 32.3% and 50.8% in minutes, or 41.5% for the mean.
- Zone input. The same week is pyramidal from heart rate time and polarized from RPE time.
- Counting unit. RPE minutes give polarized. RPE session counts give other.
- Zone grouping. Moving Edwards zone 3 (70% to 80%) from Z1 to Z2 changes the shares from 81.5%, 12.3%, and 6.2% to 60.0%, 33.8%, and 6.2%, and PI from 1.61 to 1.04. The label stays pyramidal here, but it need not in another week.
- Time below 50% HRmax. Leaving it out changes the shares to 78.9%, 14.0%, and 7.0%. Name the rule.
- Session goal instead of RPE. If the coach planned session 6 as low, not moderate, and planned sessions 4 and 5 as high, the session counts are 4, 0, and 2. Z2 is 0, so PI is not defined and the label is other, not polarized. A plan with 4 low, 1 moderate, and 1 high session gives Z2 = Z3, so the label is "Z2 and Z3 even".
- HRmax setting. A different HRmax moves minutes between Edwards zones. See [heart-rate-load.md](heart-rate-load.md#set-hrmax).

## Units and typical range

Reduction is in percent. Shares are fractions or percent. PI has no unit. The label is text.

| Population | Published value | Source |
|---|---|---|
| Competitive athletes, 27 studies pooled | Largest performance effect with a 2-week taper (effect size 0.59 ± 0.33) and a 41% to 60% volume cut (0.72 ± 0.36), with intensity (0.33 ± 0.14) and frequency (0.35 ± 0.17) kept the same. A study finding, not a target. | Bosquet et al., 2007 (abstract) |
| Team-sport athletes, 14 studies pooled | Tapering improved maximal power, maximal oxygen uptake, repeated sprint ability, and change of direction speed. Too few studies to compare taper strategies. | Vachon et al., 2021 (abstract) |
| Competitive weightlifters, survey | Reported taper of 8.0 ± 4.4 days with a 43.1 ± 14.6% volume cut. Self-reported practice, not a target. | Winwood et al., 2023 (abstract) |
| Elite endurance athletes, 175 reported distributions | 89 pyramidal, 65 polarized, and 8 threshold. The rest were other patterns. In 91%, more than 60% of endurance training was low intensity. | Sperlich et al., 2023 |
| Any athlete | PI above 2.00 means polarized. PI is 0 when Z3 is 0. | Treff et al., 2019 |

## Data you need

Collect this data:

- Source: a session log with date, minutes, and session RPE, or a load export for distance or volume load. For distribution, heart rate time in zone (see [heart-rate-load.md](heart-rate-load.md)), CR-10 ratings, or a session plan with a goal for each session.
- Device files: Polar Team Pro exports time in five heart rate zones (see [polar-team-pro.md](polar-team-pro.md)). The Firstbeat API numbers its zones from the top, so `zone1Time` is the highest zone (see [firstbeat-sports.md](firstbeat-sports.md)). Check the zone limits before you group them.
- Sampling: every session in every week, with the athlete's HRmax and zone limits stored beside the data.
- Minimum data: complete baseline weeks for a reduction. One complete week for a distribution label.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with these metrics:

- Presenting a 41% to 60% cut or a 2-week taper as a recommendation. It is a pooled study finding (Bosquet et al., 2007). The coach sets the taper.
- Not naming the baseline weeks. The same taper gives 43.1% to 46.0% depending on the baseline.
- Using session RPE load as volume and calling the drop a volume cut. It mixes volume and intensity. Show minutes and intensity beside it.
- Treating a missing week as a light week. A blank baseline week makes the baseline mean too high or too low. Report the baseline as missing.
- Reporting a distribution label without its input, grouping, and counting unit. The worked example gives three labels for one week.
- Calling a week polarized from the zone order alone. Sperlich et al. (2023) also required PI above 2.00.
- Using percentages instead of fractions in PI. Treff et al. (2019) give 80% Z1, 5% Z2, and 15% Z3 as a polarized example. As fractions, PI = log10(0.80 ÷ 0.05 × 0.15 × 100) = 2.38. With percentages, it becomes log10(80 ÷ 5 × 15 × 100) = 4.38.
- Reading Firstbeat `zone1Time` as the lowest zone. It is the highest.
- Saying one distribution is better for the athlete. The labels describe training. They do not rank it.

## Example request

> We tapered for two weeks before the conference final. Show how much each player's volume dropped compared with normal training, and tell me if our training was pyramidal or polarized this month.

The correct answer asks for the baseline weeks and the volume unit, reports the reduction with intensity and frequency beside it, and asks which input to use for the distribution. It names the input, the grouping, and the counting unit with each label. It presents the Bosquet et al. (2007) result as a study finding, not a target.

## Check the result

Run these checks:

- Recalculate one taper week by hand: baseline mean, taper volume, and reduction.
- Confirm the baseline weeks, the volume unit, the intensity measure, and the frequency appear with every reduction.
- Confirm no baseline week with missing data entered the mean.
- Confirm the three zone totals add up to the total minutes, or the total sessions, for the week.
- Recalculate PI by hand from the shares as fractions. Confirm "polarized" appears only when Z1 > Z3 > Z2 and PI is above 2.00.
- Confirm the input, the grouping, the counting unit, and the window appear with every label.

## Sources

This file cites these sources:

- Bosquet L, Montpetit J, Arvisais D, Mujika I. Effects of tapering on performance: a meta-analysis. Med Sci Sports Exerc. 2007;39(8):1358-1365. https://doi.org/10.1249/mss.0b013e31806010e0 (abstract, accessed 2026-10-07)
- Vachon A, Berryman N, Mujika I, Paquet JB, Arvisais D, Bosquet L. Effects of tapering on neuromuscular and metabolic fitness in team sports: a systematic review and meta-analysis. Eur J Sport Sci. 2021;21(3):300-311. https://doi.org/10.1080/17461391.2020.1736183 (abstract, accessed 2026-10-07)
- Washif JA, James C, Pagaduan J, Lim J, Lum D, Raja Azidin RMF, Mujika I, Beaven CM. Current periodization, testing, and monitoring practices of strength and conditioning coaches. Int J Sports Physiol Perform. 2025;20(9):1239-1252. https://doi.org/10.1123/ijspp.2025-0051 (abstract, accessed 2026-10-07)
- Winwood PW, Keogh JWL, Travis SK, Pritchard HJ. The tapering practices of competitive weightlifters. J Strength Cond Res. 2023;37(4):829-839. https://doi.org/10.1519/jsc.0000000000004324 (abstract, accessed 2026-10-07)
- Sperlich B, Matzka M, Holmberg HC. The proportional distribution of training by elite endurance athletes at different intensities during different phases of the season. Front Sports Act Living. 2023;5:1258585. https://doi.org/10.3389/fspor.2023.1258585 (accessed 2026-10-07)
- Treff G, Winkert K, Sareban M, Steinacker JM, Sperlich B. The polarization-index: a simple calculation to distinguish polarized from non-polarized training intensity distributions. Front Physiol. 2019;10:707. https://doi.org/10.3389/fphys.2019.00707 (accessed 2026-10-07)
