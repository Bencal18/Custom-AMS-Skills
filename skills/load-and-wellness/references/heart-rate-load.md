# Heart rate load (time in zone and TRIMP)

Last checked: 2026-10-02

## What it measures

Heart rate load estimates the cardiovascular response to a session by combining time with heart rate intensity.

It is a measure of internal load, like session RPE load (rating of perceived exertion × minutes). Internal load is the athlete's response to the work. External load is the work itself, such as distance run (Impellizzeri et al., 2019).

Heart rate load describes the cardiovascular response to one session. It does not diagnose illness or overtraining, and it does not predict injury or performance.

Define these terms before you start:

- Heart rate (HR): heart beats per minute (bpm).
- Maximal heart rate (HRmax): the highest heart rate the athlete can reach, in bpm.
- Resting heart rate (HRrest): the athlete's heart rate at rest, in bpm.
- Heart rate reserve (HRR): HRmax − HRrest, in bpm.
- Training impulse (TRIMP): a single load number built from time and heart rate. It is in arbitrary units (AU), which have no physical meaning on their own.
- Edwards, Banister, and Lucia TRIMP: three published ways to turn heart rate into a TRIMP. The Formula section defines each one. Edwards's method is also called the summated heart rate zone method.

Heart rate load and session RPE load agree in direction but not in size:

- Foster et al. (2001) compared session RPE with a heart rate method during cycling and basketball. The relationship was consistent, but session RPE scores were higher in absolute terms. Haddad et al. (2017) identify that heart rate method as Edwards's.
- Impellizzeri et al. (2004) correlated session RPE load with the Edwards, Banister, and Lucia methods across 479 soccer sessions. Individual correlations ranged from r = 0.50 to 0.85.
- Alexiou and Coutts (2008) found mean correlations of r = 0.84 with Banister TRIMP and 0.85 with Edwards TRIMP in women soccer players.
- Borresen and Lambert (2008) found r = 0.76 with TRIMP and r = 0.84 with the summated heart rate zone method. The methods deviated when proportionally more time was spent at low or high intensity.

Do not convert heart rate load into session RPE load, or the reverse. Use heart rate load to describe the heart's response and session RPE load to describe the athlete's perception.

## Formula

Several methods are in use. They give different numbers from the same heart rate file. Name the method, the HRmax source, and the HRrest value with every result.

### Express intensity as % HRmax or % HRR

```text
%HRmax = HR ÷ HRmax × 100
%HRR   = (HR − HRrest) ÷ (HRmax − HRrest) × 100
Target HR at a chosen %HRR = HRrest + (%HRR ÷ 100) × (HRmax − HRrest)
```

The %HRR method is known as the Karvonen method, after Karvonen et al. (1957). Oxygen uptake is the oxygen the body uses each minute. %HRR tracks the percentage of oxygen uptake reserve (maximal minus resting oxygen uptake) more closely than the percentage of maximal oxygen uptake (Swain et al., 1998).

The same heart rate gives a different percentage under each method, so never mix them in one report.

### Set HRmax

Use a measured value when one exists:

- Measured HRmax: the highest heart rate in a maximal exercise test. Nes et al. (2013) included only tests where a maximal effort could be verified.
- Peak heart rate (HRpeak): when no maximal test exists, use the highest artifact-checked value from a maximal intermittent field test. Label it HRpeak, with the test name and date. In the Yo-Yo intermittent recovery level 1 test, peak heart rate in 17 men was 187 ± 2 bpm, against 189 ± 2 bpm in a treadmill test to exhaustion (Krustrup et al., 2003). In the level 2 test, heart rate at exhaustion was 98 ± 1 % of HRmax in 13 men (Krustrup et al., 2006). In 20 team sport players, heart rate at exhaustion did not differ between the 30-15 Intermittent Fitness Test and a continuous incremental test (Buchheit et al., 2009).
- Yo-Yo intermittent recovery level 2 peak: accept it as HRpeak. Label it "may be about 2 % below HRmax on average (Krustrup et al., 2006)". Apply no correction factor.
- HRpeak window: use the highest 5-second rolling average of artifact-checked samples, as Paulson et al. (2015) did in a lab test. This window is a practice default of this skill, not a published rule. State it with the result.
- HRpeak update: when a later session gives a higher artifact-checked 5-second average, raise HRpeak to that value. Record the new date and session.
- Age-predicted HRmax: an estimate from age alone. Banister et al. (1992) allowed HRmax to be "measured directly or estimated as 220 − age".

These age-predicted formulas appear in peer-reviewed work:

| Formula | Source | Known error |
|---|---|---|
| 220 − age | The common equation, as described by Tanaka et al., 2001 | Underestimates HRmax in older adults (Tanaka et al., 2001). |
| 208 − 0.7 × age | Tanaka et al., 2001 | Built from group means in 351 studies, then checked in 514 measured adults. Same line for men and women. |
| 211 − 0.64 × age | Nes et al., 2013 | Standard error of the estimate (SEE) 10.8 bpm in 3,320 healthy adults. Earlier formulas underestimated measured HRmax in people older than 30. |

The Nes formula had an SEE of 10.8 bpm. The SEE is the typical gap between one person's measured and predicted value. If errors are roughly normal, about 1 in 3 people are more than 10.8 bpm from the prediction, and about 1 in 20 more than 21 bpm away.

### Time in zone

Time in zone is the minutes spent with heart rate inside each intensity band. This file uses the five zones of Edwards's method:

| Zone | % HRmax | Weight in Edwards TRIMP |
|---|---|---|
| Below zone 1 | Below 50 % | 0 |
| 1 | 50 to 60 % | 1 |
| 2 | 60 to 70 % | 2 |
| 3 | 70 to 80 % | 3 |
| 4 | 80 to 90 % | 4 |
| 5 | 90 to 100 % | 5 |

Values at or above 100 % HRmax count in zone 5.

Sources: Edwards (1993), as described by Paulson et al. (2015) and Hourcade et al. (2018). Paulson et al. (2015) defined the zones on %HRpeak from a graded exercise test to exhaustion. Some papers write the bands as 50 to 59 %, 60 to 69 %, and so on (Scantlebury et al., 2017).

Neither Edwards nor Lucia et al. (2003) say which zone gets a value on a boundary. Edwards wrote the bands with shared end points, such as 50 to 60 % and 60 to 70 %. Use this boundary rule, which matches the Polar Team Pro API: include the lower bound and exclude the upper bound, on the unrounded %HRmax. A value of exactly 60.0 % counts in zone 2. This rule is a practice convention, not a published part of either method.

Use the same rule for Lucia zones. State the rule with every result.

### Edwards summated heart rate zone method

```text
TRIMP_Edwards = (min in zone 1 × 1) + (min in zone 2 × 2) + (min in zone 3 × 3)
              + (min in zone 4 × 4) + (min in zone 5 × 5)
```

Use it when you have a reliable HRmax and no lab thresholds. Time below 50 % HRmax counts as 0.

### Banister TRIMP

```text
x_i = (HR_i − HRrest) ÷ (HRmax − HRrest)
Male weighting:    TRIMP_Banister = Σ ( t_i × x_i × 0.64 × e^(1.92 × x_i) )
Female weighting:  TRIMP_Banister = Σ ( t_i × x_i × 0.86 × e^(1.67 × x_i) )
```

Define every term in the formula:

- `i`: one heart rate sample, or one phase of the session. `Σ` adds the terms for every sample or phase.
- `HR_i`: the heart rate of sample `i`, in bpm. For a phase, use the mean heart rate of that phase.
- `t_i`: the length of sample or phase `i`, in minutes. For 1 Hz data, each sample lasts 1 ÷ 60 min.
- `x_i`: the delta heart rate ratio, which is %HRR as a fraction. It runs from 0 at rest to 1 at HRmax (Banister et al., 1992).
- `0.64 × e^(1.92 × x)` and `0.86 × e^(1.67 × x)`: weighting factors. They give more credit to high-intensity time, based on the exponential rise of blood lactate (a by-product of hard exercise measured in a drop of blood) with intensity (Banister et al., 1992). Banister (1991) prints both multiplier forms. The female form appears earlier, in Banister and Hamilton (1985). Paulson et al. (2015) and Hourcade et al. (2018) print the 0.64 and 1.92 form. Tomoto et al. (2026) print both forms.
- `e`: the base of natural logarithms, about 2.718.

Use the per-sample sum by default whenever the file holds second-by-second heart rate. Banister scored each phase of a session from its length and heart rate, then added the phase scores to give the session total. He recorded periods at different intensities separately (Banister, 1991, pp. 406-409). Applying the formula to each sample and adding the results is the same rule with one-sample phases. Polar also computes its Banister TRIMP each second and adds the results (Polar, 2025). Use the per-phase sum when the file holds a mean heart rate for each phase, such as each drill or lap, but no samples.

Use the session mean only as a fallback, when the file holds the session mean heart rate and duration and nothing finer:

```text
x_mean = (HR_mean − HRrest) ÷ (HRmax − HRrest)
Male weighting:    TRIMP_Banister_mean = duration_min × x_mean × 0.64 × e^(1.92 × x_mean)
Female weighting:  TRIMP_Banister_mean = duration_min × x_mean × 0.86 × e^(1.67 × x_mean)
```

Define the new terms:

- `HR_mean`: the mean heart rate of the whole session, in bpm.
- `duration_min`: the session length in minutes.

Label every result from the fallback "session mean". Paulson et al. (2015), Hourcade et al. (2018), and Tomoto et al. (2026) used this form. The whole-session mean comes from these later papers, not from Banister. It treats the whole session as one phase, so it cannot see intervals. Hourcade et al. (2018) found that it did not separate two sessions with almost equal mean heart rate (p = 0.420). The weighting curves upward, so the per-sample sum is larger than the session mean for any session where heart rate varies. The two are equal only when heart rate is constant. The worked example shows the size of the gap.

Never mix the per-sample sum and the session mean in one athlete's history. Keep session mean results as a separate, labeled series.

Use the 0.64 and 0.86 multiplier form by default, and name it with every result. Know this variant before you compare numbers:

- Exponent-only form. The appendix of Banister et al. (1992) prints the weighting as e^(1.92 × x) for males and e^(1.67 × x) for females, without the 0.64 and 0.86 multipliers. Banister's 1985 and 1991 texts include the multipliers. The exponent-only form gives larger numbers and reverses which sex scores higher. Keep it as a documented variant. Ask which form a tool uses, and whether it sums samples or uses the session mean.

Use Banister TRIMP when you have HRmax and HRrest. The per-sample and per-phase sums can see intervals. The session mean cannot, so say so when you report it for an interval session.

The published weightings are labeled male and female. They come from blood lactate curves in trained men and women (Banister, 1991). They say nothing about an athlete's gender. No published guidance was found for athletes outside those categories. At a delta heart rate ratio from 0.3 to 1.0, the female weighting gives 5 to 25 % more load than the male weighting.

Follow these steps to choose a weighting:

1. Offer Edwards, Lucia, or iTRIMP first. Edwards TRIMP has no sex term.
2. If the user wants Banister TRIMP, ask which weighting to use for each athlete. Never ask for the athlete's gender, and never infer the weighting from a name or roster data. Use this wording: "Banister TRIMP has two published curves, labeled male and female, built from blood lactate in trained men and women. Which curve should I use for this athlete? If you are unsure, I can show both, or use Edwards TRIMP, which has no sex term."
3. If the user does not choose, show both results, each labeled with its weighting.
4. Store both results for every session.
5. Record the chosen weighting, and never switch weightings within one athlete's history.

### Lucia TRIMP

```text
TRIMP_Lucia = (min below VT × 1) + (min from VT to RCP × 2) + (min above RCP × 3)
```

Define every term in the formula:

- `VT`: the heart rate at the ventilatory threshold, the first breathing threshold in a lab ramp test. A ramp test raises the workload in small steps to exhaustion while a mask measures breathing gases.
- `RCP`: the heart rate at the respiratory compensation point, the second, higher breathing threshold in the same test.

Lucia et al. (2003) divided race time into these three phases from each rider's ramp test and multiplied time in each phase by a phase multiplier. Paulson et al. (2015) report the multipliers 1, 2, and 3.

Use Lucia TRIMP only when each athlete has a lab test with both thresholds. It does not use HRmax. Under the boundary rule, a heart rate equal to VT counts in the middle zone, and one equal to RCP counts in the top zone.

### Individualized TRIMP (iTRIMP)

Manzi et al. (2009) replaced Banister's fixed weighting with a weighting built from each athlete's own heart rate and blood lactate profile in a treadmill test. Sheoran et al. (2025) describe iTRIMP as adding the weighted value of every heart rate data point across the session.

Use it only when each athlete has a lactate test. Do not reuse one athlete's weighting for another.

### Average heart rate and % HRmax as session summaries

Mean heart rate and mean %HRmax are simple session summaries. They hide how intensity was spread across the session.

An interval session and a steady session can have the same mean heart rate and large differences in time in zone, as the worked example shows. Hourcade et al. (2018) compared two sessions with almost equal mean heart rate but different intensity distribution. The summated heart rate zone load differed between them (p = 0.007), while Banister TRIMP from the session mean did not (p = 0.420).

Report time in zone next to any mean.

### Calculate it in a spreadsheet or Python

Use this spreadsheet formula for Edwards TRIMP, with 1 Hz heart rate (one sample per second) in `B2:B1201` and HRmax in `F1`. Each sample adds 1 for every zone boundary it reaches, so the sum equals the zone weight:

```text
=SUMPRODUCT((B2:B1201/$F$1>=0.5)+(B2:B1201/$F$1>=0.6)+(B2:B1201/$F$1>=0.7)+(B2:B1201/$F$1>=0.8)+(B2:B1201/$F$1>=0.9))/60
```

Use this spreadsheet formula for the per-sample Banister TRIMP with the male weighting, with HRmax in `F1` and HRrest in `F3`. Leave dropouts blank. The formula adds one term for each recorded second. A plain `SUMPRODUCT` reads a blank cell as 0 bpm, which adds a negative term. The `(B2:B1201<>"")` guard sets the term for a blank cell to 0:

```text
=SUMPRODUCT((B2:B1201<>"")*(B2:B1201-$F$3)/($F$1-$F$3)*0.64*EXP(1.92*(B2:B1201-$F$3)/($F$1-$F$3)))/60
```

Use this formula for the session mean fallback only when you have no samples. Put the session mean heart rate in `F5` and the session minutes in `F6`, and label the result "session mean":

```text
=F6*((F5-$F$3)/($F$1-$F$3))*0.64*EXP(1.92*((F5-$F$3)/($F$1-$F$3)))
```

For the female weighting, replace `0.64` with `0.86` and `1.92` with `1.67` in either Banister formula.

Use these Python functions for the same calculations:

```python
import numpy as np

COEF = {"male": (0.64, 1.92), "female": (0.86, 1.67)}

def edwards_au(hr_bpm, hr_max, dt_s=1.0):
    hr_bpm = np.asarray(hr_bpm, float)  # gaps removed, not zero-filled
    weight = np.digitize(hr_bpm / hr_max, [0.5, 0.6, 0.7, 0.8, 0.9])  # 0 to 5
    return float((weight * dt_s / 60).sum())

def banister_au(hr_bpm, hr_max, hr_rest, weighting, dt_s=1.0):
    # Default: one term for each sample, then add them.
    # For phases, pass phase mean heart rates and phase lengths in seconds as dt_s.
    if weighting not in COEF:
        raise ValueError("weighting must be 'male' or 'female'")
    a, b = COEF[weighting]
    x = (np.asarray(hr_bpm, float) - hr_rest) / (hr_max - hr_rest)  # gaps removed
    return float((np.asarray(dt_s, float) / 60 * x * a * np.exp(b * x)).sum())

def banister_session_mean_au(hr_mean, duration_min, hr_max, hr_rest, weighting):
    # Fallback when only mean heart rate and duration exist: label it "session mean"
    if weighting not in COEF:
        raise ValueError("weighting must be 'male' or 'female'")
    a, b = COEF[weighting]
    x = (hr_mean - hr_rest) / (hr_max - hr_rest)
    return float(duration_min * x * a * np.exp(b * x))

def lucia_au(hr_bpm, hr_vt, hr_rcp, dt_s=1.0):
    hr_bpm = np.asarray(hr_bpm, float)
    weight = np.where(hr_bpm < hr_vt, 1, np.where(hr_bpm < hr_rcp, 2, 3))
    return float((weight * dt_s / 60).sum())
```

### Calculate it in Power BI and Tableau

These versions follow the boundary rule in this file: a heart rate equal to a zone boundary counts in the higher zone. Banister TRIMP adds one term for each sample, as the default form does. Dropouts stay blank and add nothing. Banister TRIMP uses the weighting the user chose for each athlete and returns a blank when none is recorded. A blank means the user has not chosen. Ask, or show both weightings outside this measure. Both return a blank when HRmax is missing or the session has no samples.

Both versions assume an `hr_samples` table with one row per second: `athlete_id`, `session_id`, `time_s`, and `hr_bpm`. They also assume an `athletes` table with `hr_max_bpm`, `hr_rest_bpm`, and `trimp_weighting`, set to `male` or `female` by the user. Never infer the weighting from a name or roster data. Show the results with one athlete and one session per row. In Power BI, relate `athletes[athlete_id]` to `hr_samples[athlete_id]`, one to many, single direction, and put `athletes[athlete_id]` in the visual.

In Power BI, use these DAX measures. They are measures because each result sums many sample rows and reads settings from the `athletes` table:

```text
Edwards TRIMP (AU) =
VAR hrmax = SELECTEDVALUE ( athletes[hr_max_bpm] )
VAR dt = 1
RETURN
    IF (
        NOT ISBLANK ( hrmax ) && hrmax > 0 && COUNT ( hr_samples[hr_bpm] ) > 0,
        SUMX (
            FILTER ( hr_samples, NOT ISBLANK ( hr_samples[hr_bpm] ) ),
            VAR p = hr_samples[hr_bpm] / hrmax
            RETURN
                IF ( p >= 0.5, 1, 0 ) + IF ( p >= 0.6, 1, 0 ) + IF ( p >= 0.7, 1, 0 )
                    + IF ( p >= 0.8, 1, 0 ) + IF ( p >= 0.9, 1, 0 )
        ) * dt / 60
    )

Banister TRIMP (AU) =
VAR hrmax = SELECTEDVALUE ( athletes[hr_max_bpm] )
VAR hrrest = SELECTEDVALUE ( athletes[hr_rest_bpm] )
VAR w = SELECTEDVALUE ( athletes[trimp_weighting] )
VAR a = SWITCH ( w, "male", 0.64, "female", 0.86 )
VAR b = SWITCH ( w, "male", 1.92, "female", 1.67 )
VAR dt = 1
VAR ok =
    COUNT ( hr_samples[hr_bpm] ) > 0 && NOT ISBLANK ( hrmax ) && NOT ISBLANK ( hrrest )
        && NOT ISBLANK ( a ) && hrmax > hrrest
RETURN
    IF (
        ok,
        SUMX (
            FILTER ( hr_samples, NOT ISBLANK ( hr_samples[hr_bpm] ) ),
            VAR x = ( hr_samples[hr_bpm] - hrrest ) / ( hrmax - hrrest )
            RETURN x * a * EXP ( b * x )
        ) * dt / 60
    )
```

`dt` is the seconds between samples. It is 1 for 1 Hz data.

In Tableau, join `athletes` to `hr_samples` on `athlete_id` in the physical layer, so each sample row carries the athlete's settings. Make a parameter `Seconds per sample` set to 1. Use these calculations:

```text
Edwards weight (row-level):
IF ISNULL([hr_bpm]) OR ISNULL([hr_max_bpm]) OR [hr_max_bpm] <= 0 THEN NULL
ELSE IIF([hr_bpm] / [hr_max_bpm] >= 0.5, 1, 0) + IIF([hr_bpm] / [hr_max_bpm] >= 0.6, 1, 0)
   + IIF([hr_bpm] / [hr_max_bpm] >= 0.7, 1, 0) + IIF([hr_bpm] / [hr_max_bpm] >= 0.8, 1, 0)
   + IIF([hr_bpm] / [hr_max_bpm] >= 0.9, 1, 0)
END

Edwards TRIMP (AU) (aggregate):
SUM([Edwards weight]) * [Seconds per sample] / 60

Banister x (row-level):
IF ISNULL([hr_bpm]) OR ISNULL([hr_max_bpm]) OR ISNULL([hr_rest_bpm]) THEN NULL
ELSEIF [hr_max_bpm] <= [hr_rest_bpm] THEN NULL
ELSE ([hr_bpm] - [hr_rest_bpm]) / ([hr_max_bpm] - [hr_rest_bpm])
END

Banister term (row-level):
CASE [trimp_weighting]
WHEN "male" THEN [Banister x] * 0.64 * EXP(1.92 * [Banister x])
WHEN "female" THEN [Banister x] * 0.86 * EXP(1.67 * [Banister x])
END

Banister TRIMP (AU) (aggregate):
SUM([Banister term]) * [Seconds per sample] / 60
```

Blanks behave this way in each tool:

- Power BI: `FILTER` drops blank samples before `SUMX` adds the terms, as the guard does in the spreadsheet. A session with no samples returns a blank, not 0 AU.
- Power BI: a missing weighting gives a blank `a`, and the measure returns a blank. It never falls back to one weighting.
- Tableau: a null sample gives a null weight and a null term, and `SUM` ignores them. A `CASE` with no matching weighting returns null on every row, so the sum is null.
- Power BI and Tableau: a text dropout code becomes null on import, so it adds nothing.
- Spreadsheet: a text dropout code such as "--" gives `#VALUE!` in both the Edwards and the Banister formula. A number stored as text, such as "150", is counted like a number by both formulas.

## Calculate heart-rate load

Follow these steps to calculate the metric from raw inputs:

1. Load one row per heart rate sample with `athlete_id`, `session_id`, `timestamp`, and `hr_bpm`.
2. Find the sampling interval from the timestamps, in seconds. Ask the user if it is not constant.
3. Find gaps, where timestamps jump or `hr_bpm` is 0 or blank.
4. Remove those samples. Do not count them as 0 bpm.
5. Find artifacts: sudden jumps the user or device flags as artifact. Do not interpret them as a heart rhythm problem.
6. Remove artifacts only with the user's agreement, and report how many there were.
7. Find plausible values above HRmax that are not artifacts. Do not remove them.
8. If HRmax is age-predicted, tell the user the HRmax setting is probably too low. The Nes formula had an SEE of 10.8 bpm (Nes et al., 2013). If HRmax is a Yo-Yo intermittent recovery level 2 peak, label it "may be about 2 % below HRmax on average (Krustrup et al., 2006)", and apply no correction factor. If a later artifact-checked 5-second average is higher than HRpeak, raise HRpeak to it.
9. Ask for each athlete's HRmax and how it was set: maximal test, HRpeak from a maximal field test, or an age formula.
10. Ask for HRrest and how it was measured.
11. For Lucia TRIMP, ask for each athlete's heart rate at VT and RCP from a lab test.
12. If the user asks for Banister TRIMP, offer Edwards, Lucia, or iTRIMP first. If the user still wants Banister TRIMP, ask which curve to use for each athlete, with the wording in the Banister TRIMP section. Never ask for the athlete's gender, and never infer the curve from a name or roster data. If the user does not choose, show both results. Store both, and never switch curves within one athlete's history.
13. For Banister TRIMP, use the 0.64 and 0.86 multiplier form unless the user names another. Add one term for each sample when the file holds second-by-second heart rate, or one term for each phase when it holds phase means. Use the session mean only when the file holds nothing finer than the session mean heart rate and duration, and label the result "session mean".
14. Calculate time in each zone in minutes: count samples in the zone, multiply by the sampling interval, and divide by 60. Include the lower bound and exclude the upper bound.
15. Calculate the TRIMP the user asked for, in AU, with the formula above.
16. Report recorded minutes next to planned session minutes, so missing data is visible.
17. Report the method, the zone boundaries and boundary rule, HRmax and its source, HRrest, and the weighting with each result.

## Worked example

The example is one synthetic 20-minute interval session, recorded at 1 Hz, one sample per second (1,200 samples). The athlete is 20 years old. All numbers below come from running the calculation in Python.

| Input | Value |
|---|---|
| Session | 3 min at 110 bpm, 3 min at 140 bpm, then 2 min at 180 bpm and 2 min at 150 bpm, three times, then 2 min at 120 bpm |
| Duration | 20.00 min |
| Mean heart rate | 148.50 bpm |
| Measured HRmax | 205 bpm |
| Age-predicted HRmax, 208 − 0.7 × age | 194 bpm |
| Age-predicted HRmax, 220 − age | 200 bpm |
| HRrest | 55 bpm |
| Lab heart rate at VT and RCP | 160 bpm and 178 bpm |

### Set the zone boundaries

Multiply HRmax by 0.5, 0.6, 0.7, 0.8, and 0.9:

| Zone lower bound | Measured HRmax 205 bpm | Predicted HRmax 194 bpm |
|---|---|---|
| Zone 1 (50 %) | 102.5 bpm | 97.0 bpm |
| Zone 2 (60 %) | 123.0 bpm | 116.4 bpm |
| Zone 3 (70 %) | 143.5 bpm | 135.8 bpm |
| Zone 4 (80 %) | 164.0 bpm | 155.2 bpm |
| Zone 5 (90 %) | 184.5 bpm | 174.6 bpm |

### Count time in zone

| Zone | Minutes, measured HRmax | Minutes, predicted HRmax 194 |
|---|---|---|
| Below 50 % | 0 | 0 |
| 1 | 5 (110 and 120 bpm) | 3 (110 bpm) |
| 2 | 3 (140 bpm) | 2 (120 bpm) |
| 3 | 6 (150 bpm) | 9 (140 and 150 bpm) |
| 4 | 6 (180 bpm) | 0 |
| 5 | 0 | 6 (180 bpm) |

With the measured HRmax, 180 bpm is 87.8 % HRmax, in zone 4. With 194 bpm, it is 92.8 %, in zone 5.

The same five bands applied to %HRR give a third distribution. With the measured HRmax, 110, 120, 140, 150, and 180 bpm are 36.7, 43.3, 56.7, 63.3, and 83.3 % HRR. That puts 5 min below 50 %, 3 min in zone 1, 6 min in zone 2, and 6 min in zone 4.

Edwards defined his zones on %HRmax, so do not use %HRR bands for Edwards TRIMP.

### Calculate Edwards TRIMP

Multiply the minutes in each zone by the zone weight, then add:

- Measured HRmax: 5 × 1 + 3 × 2 + 6 × 3 + 6 × 4 = 53.0 AU.
- Predicted HRmax 194 bpm: 3 × 1 + 2 × 2 + 9 × 3 + 0 × 4 + 6 × 5 = 64.0 AU.
- Predicted HRmax 200 bpm (220 − age): 64.0 AU, with the same zone minutes as 194 bpm. At this HRmax, 120, 140, and 180 bpm fall exactly on the 60, 70, and 90 % boundaries. The result depends on the boundary rule: 64.0 AU with boundaries in the higher zone, 53.0 AU with boundaries in the lower zone.

### Calculate Banister TRIMP

Use the per-sample sum, the default, with the measured HRmax. Every sample in a block has the same heart rate, so the terms for a block add up to its minutes × x × weighting:

| Heart rate | Minutes | x | Male weighting | Male term | Female weighting | Female term |
|---|---|---|---|---|---|---|
| 110 bpm | 3 | 0.3667 | 1.2940 | 1.42 AU | 1.5865 | 1.75 AU |
| 140 bpm | 3 | 0.5667 | 1.8997 | 3.23 AU | 2.2156 | 3.77 AU |
| 180 bpm | 6 | 0.8333 | 3.1699 | 15.85 AU | 3.4585 | 17.29 AU |
| 150 bpm | 6 | 0.6333 | 2.1591 | 8.20 AU | 2.4765 | 9.41 AU |
| 120 bpm | 2 | 0.4333 | 1.4707 | 1.27 AU | 1.7733 | 1.54 AU |
| Total | 20 | | | 30.0 AU | | 33.8 AU |

The male weighting is 0.64 × e^(1.92 × x), and the female weighting is 0.86 × e^(1.67 × x). The totals add the unrounded terms.

Repeat it with the predicted HRmax:

- 194 bpm: 36.1 AU male and 40.0 AU female.
- 200 bpm: 32.5 AU male and 36.4 AU female.

Use the session mean fallback only if the file held nothing but the mean of 148.5 bpm and the 20 minutes. With the measured HRmax:

- x = (148.5 − 55) ÷ (205 − 55) = 0.6233.
- Male weighting: 0.64 × e^(1.92 × 0.6233) = 2.1181. TRIMP = 20 × 0.6233 × 2.1181 = 26.4 AU.
- Female weighting: 0.86 × e^(1.67 × 0.6233) = 2.4355. TRIMP = 20 × 0.6233 × 2.4355 = 30.4 AU.

Repeat the fallback with the predicted HRmax:

- 194 bpm: x = (148.5 − 55) ÷ (194 − 55) = 0.6727. Male weighting 2.3285, so TRIMP = 31.3 AU. Female weighting 2.6446, so TRIMP = 35.6 AU.
- 200 bpm: x = 0.6448. Male TRIMP = 28.5 AU. Female TRIMP = 32.6 AU.

With the measured HRmax, the per-sample sum is 13.5 % higher than the session mean with the male weighting, and 11.2 % higher with the female weighting.

### Calculate Lucia TRIMP

Heart rates of 110, 120, 140, and 150 bpm are below VT, for 14 min. Heart rate of 180 bpm is above RCP, for 6 min. No time falls between VT and RCP.

Lucia TRIMP = 14 × 1 + 0 × 2 + 6 × 3 = 32.0 AU. HRmax does not change it.

### Compare the results

| Method | Measured HRmax 205 bpm | Predicted HRmax 194 bpm | Change |
|---|---|---|---|
| Mean % HRmax | 72.4 % | 76.5 % | +4.1 points |
| Edwards TRIMP | 53.0 AU | 64.0 AU | +11.0 AU (+20.8 %) |
| Banister TRIMP, male weighting, per-sample sum | 30.0 AU | 36.1 AU | +6.1 AU (+20.2 %) |
| Banister TRIMP, female weighting, per-sample sum | 33.8 AU | 40.0 AU | +6.2 AU (+18.5 %) |
| Banister TRIMP, male weighting, session mean | 26.4 AU | 31.3 AU | +4.9 AU (+18.6 %) |
| Banister TRIMP, female weighting, session mean | 30.4 AU | 35.6 AU | +5.2 AU (+17.2 %) |
| Lucia TRIMP | 32.0 AU | 32.0 AU | None |

An HRmax that is 11 bpm too low raises every HRmax-based result for the same session. With the measured HRmax, the female weighting gives a result 12.6 % higher than the male weighting with the per-sample sum, and 15.0 % higher with the session mean.

### See what the mean hides

A steady 20-minute session at 148.5 bpm has the same mean heart rate. With the measured HRmax, it gives:

- Banister TRIMP, per-sample sum: 26.4 AU male and 30.4 AU female. Heart rate is constant, so the sum equals the session mean. The interval session scored 30.0 AU and 33.8 AU.
- Banister TRIMP, session mean: 26.4 AU male and 30.4 AU female, the same as the interval session.
- Edwards TRIMP: 60.0 AU, all 20 min in zone 3. The interval session scored 53.0 AU.
- Lucia TRIMP: 20.0 AU, all 20 min below VT. The interval session scored 32.0 AU.

The session mean cannot tell the two sessions apart. The per-sample sum and time in zone can. These methods do not agree on which session was harder: the per-sample sum and Lucia TRIMP score the interval session higher, and Edwards TRIMP scores the steady session higher.

## What changes the number

These choices change the result even when the athlete's effort does not. Figures are from the worked example, with the measured HRmax, the male weighting, and the per-sample Banister sum unless stated:

- HRmax source. An age formula 11 bpm below the measured value raised Edwards TRIMP from 53.0 to 64.0 AU and Banister TRIMP from 30.0 to 36.1 AU. The Nes formula had an SEE of 10.8 bpm (Nes et al., 2013).
- HRrest. Banister TRIMP was 32.0 AU with HRrest at 45 bpm, 30.0 AU at 55 bpm, and 27.8 AU at 65 bpm. Edwards TRIMP does not use HRrest. %HRR zones do. Measure HRrest the same way every time.
- Zone boundaries and the %HRmax or %HRR choice. The same session gave 6 min in zone 4 on %HRmax bands and a different spread on %HRR bands. The boundary rule alone moved Edwards TRIMP at HRmax 200 bpm from 53.0 to 64.0 AU, a 20.8 % difference, because three heart rates fell exactly on boundaries.
- Banister form. With the 0.64 and 0.86 multipliers, the session scored 30.0 AU male and 33.8 AU female. With the exponent-only form of Banister et al. (1992), it scored 46.8 AU male and 39.2 AU female. The sex ordering reverses.
- Per-sample sum versus session mean. The per-sample sum was 30.0 AU male and 33.8 AU female. The session mean fallback gave 26.4 AU and 30.4 AU for the same session.
- Sensor contact and dropouts. A 60-second dropout during a 180 bpm block, recorded as 0 bpm, cut mean heart rate from 148.50 to 139.50 bpm and Banister TRIMP from 30.0 to 27.2 AU. Each zero adds a small negative term, because its delta heart rate ratio is below 0. Removing the dropout instead gave 19 min, 146.84 bpm, and 27.3 AU. With the session mean fallback, zeros cut Banister TRIMP from 26.4 to 21.3 AU, and removal gave 24.1 AU. Edwards TRIMP fell from 53.0 to 49.0 AU either way. Lucia TRIMP fell to 30.0 AU with zeros and 29.0 AU with removal, because zero bpm counts as below VT. A chest strap with electrodes agreed best with an electrocardiogram (ECG). Optical wrist and forearm monitors varied with exercise type (Gillinov et al., 2017).
- Artifact spikes. An artifact is a false reading from the sensor. A false 15-second spike to 230 bpm raised Edwards TRIMP from 53.0 to 53.5 AU and Banister TRIMP from 30.0 to 31.4 AU. A value above HRmax gives a delta heart rate ratio above 1, outside the range Banister et al. (1992) defined. Separate artifacts from plausible high values. A plausible value above an age-predicted HRmax probably means the HRmax setting is too low. Do not remove it silently.
- Sampling rate and averaging. With 30-second transitions between blocks, Edwards TRIMP was 53.4 AU at 1 s, 53.3 AU from 5 s averages, and 54.0 AU from 60 s averages. Lucia TRIMP was 31.2, 31.1, and 29.0 AU. Averaging over long windows blurs short changes in heart rate. Use the same rate for every session you compare.
- Gaps in duration. Missing minutes reduce TRIMP. Report recorded minutes next to planned minutes.
- Cardiovascular drift. During prolonged exercise, heart rate rises over time while stroke volume, the blood pumped per beat, falls (Coyle and González-Alonso, 2001). Heart rate also rises steadily during exercise in most studies (Achten and Jeukendrup, 2003). An illustrative drift of 0.5 bpm per minute raised Edwards TRIMP from 53.0 to 59.0 AU and Banister TRIMP from 30.0 to 33.8 AU.
- Heat and hydration. Dehydration and air temperature can change the relationship between heart rate and oxygen uptake substantially (Achten and Jeukendrup, 2003). The same work in hot conditions can give a different heart rate load.
- Caffeine. In a meta-analysis of 3 to 6 mg per kg body mass, caffeine did not change heart rate during submaximal exercise, but it lowered ratings of perceived exertion (RPE) (Glaister and Gissane, 2018). Caffeine may change session RPE load without changing heart rate load.
- Illness and fever. Fever raises heart rate. In 27 young men with an acute febrile infection, 24-hour heart rate rose by about 8.5 bpm for each 1 °C (Karjalainen and Viitasalo, 1986). If staff recorded that an athlete was unwell, note it next to the session. Do not infer illness from heart rate, and refer health questions to medical staff.
- Day-to-day variation. Heart rate shows a small day-to-day variability (Achten and Jeukendrup, 2003). Small session-to-session changes may be noise. Do not call a change real without a typical error.

## Units and typical range

Time in zone is in minutes. TRIMP is in AU. No population range for TRIMP applies across sports, session lengths, and methods. Compare each athlete with their own history, on the same method and settings.

This file gives no typical error (TE) for session TRIMP. TE is the standard deviation of an individual's repeated measurements (Hopkins, 2000).

Do not call a change between sessions real unless the user supplies a TE from a test-retest study in which no true change was expected, and the change exceeds the noise band. For two single values, the noise band is 1.96 × √2 × TE, about 2.77 × TE. Error alone gives a change smaller than this about 95 percent of the time.

If the `monitoring-statistics` skill is installed, use its typical error and noise-band rules.

| Population | Typical range | Source |
|---|---|---|
| Any session, Edwards TRIMP | 0 to 5 × `duration_min` AU | Arithmetic of the formula (Paulson et al., 2015) |
| Any session, Lucia TRIMP | 1 to 3 × `duration_min` AU | Arithmetic of the formula (Paulson et al., 2015) |
| Any session, Banister TRIMP with 0.64 or 0.86 multiplier | 0 to 4.365 × `duration_min` AU (male), 0 to 4.568 × `duration_min` AU (female), at x = 1 | Arithmetic of the formula |
| Healthy adults, age-predicted HRmax | SEE 10.8 bpm around 211 − 0.64 × age | Nes et al., 2013 |

## Data you need

Collect this data:

- Source: a heart rate monitor export with one timestamp and one heart rate value per sample, plus each athlete's HRmax, HRrest, and their sources. Lucia TRIMP needs VT and RCP heart rates from a lab test. iTRIMP needs a heart rate and blood lactate test.
- Sampling: 1 sample per second when possible, and the same rate for every session you compare. Record the rate.
- Minimum data: one complete session gives one value. Compare sessions only when HRmax, HRrest, zone boundaries, and method stayed the same.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using 220 − age without saying so. The Nes formula had an SEE of 10.8 bpm (Nes et al., 2013), and 220 − age underestimates HRmax in older adults (Tanaka et al., 2001). Ask for a measured HRmax. If only a prediction exists, name the formula next to every result.
- Mixing %HRmax and %HRR. 150 bpm was 73.2 % HRmax but 63.3 % HRR for the worked example athlete. Edwards zones use %HRmax. Banister's ratio uses HRR.
- Not naming the Banister form. The 0.64 and 0.86 multiplier form and the exponent-only form give different numbers and a different sex ordering. The per-sample sum and the session mean also give different numbers. State the form.
- Using the session mean when second-by-second data exist. The mean hides intervals. Add one term for each sample, and keep the session mean for files with nothing finer.
- Applying the male weighting to every athlete, or guessing the weighting from a name, roster, or gender. Ask which curve to use, record it, keep it fixed, and state it.
- Using one sample as one minute. A 1 Hz file has 60 samples per minute. Divide the sample count by 60, or multiply by the interval in seconds and divide by 60.
- Counting dropouts as 0 bpm. Zeros cut mean heart rate and Banister TRIMP, and they count as zone 1 time in Lucia TRIMP. Remove dropouts and report recorded minutes.
- Treating every value above HRmax the same way. Remove artifacts only with the user's agreement. Keep plausible high values, and tell the user an age-predicted HRmax is probably too low. A delta heart rate ratio above 1 is outside the formula's range.
- Not stating the boundary rule. A heart rate exactly on a boundary changes zone under a different rule. In the worked example at HRmax 200 bpm, Edwards TRIMP was 53.0 or 64.0 AU depending on the rule.
- Reporting only mean heart rate or mean %HRmax. The interval and steady sessions in the worked example had the same mean and different time in zone.
- Using Lucia TRIMP with HRmax-based zones. Lucia TRIMP needs lab VT and RCP heart rates for each athlete. Without them, it is a different method. Name it as such.
- Using heart rate methods for athletes with a limited heart rate response. Paulson et al. (2015) collected heart rate only from wheelchair rugby players without cervical spinal cord injury, because cervical injury limits maximal heart rate to about 120 to 150 bpm. Ask the user whether any athlete has a condition that limits heart rate. Heart rate methods do not fit those athletes.
- Calling a change between two sessions real without a typical error. Use a TE from a test-retest study and the noise band in Units and typical range.
- Comparing heart rate load across athletes. Each athlete has their own HRmax, HRrest, and thresholds. Compare an athlete with their own history.
- Reading heart rate load as equal to session RPE load. Correlations between session RPE load and heart rate methods ranged from r = 0.50 to 0.85 in young soccer players (Impellizzeri et al., 2004). Session RPE gave higher absolute scores than the heart rate method (Foster et al., 2001). The two deviate when more time is spent at low or high intensity (Borresen and Lambert, 2008). Report both, side by side.
- Trusting heart rate load in highly intermittent work. Heart rate methods related better to session RPE in less intermittent soccer sessions (Alexiou and Coutts, 2008). Paulson et al. (2015) note that heart rate methods may underestimate short, near-maximal efforts. Say so when the session was mostly sprints or contacts.
- Treating heart rate load as a fitness or performance score. No single physiological marker measures fitness and fatigue or predicts performance, and training load models have shown poor accuracy (Borresen and Lambert, 2009).

## Example request

> I have second-by-second heart rate exports for my players from today's practice. I know their ages and resting heart rates. Give me time in zones, Edwards TRIMP, and Banister TRIMP for each player, and tell me who worked hardest.

The correct answer asks for measured HRmax or names the age formula used, removes dropouts, shows the zone boundaries and Banister form, and compares each player with their own history rather than ranking players against each other.

## Check the result

Run these checks:

- Confirm the minutes across all zones, including below 50 %, add up to the recorded duration.
- Confirm Edwards TRIMP is no more than 5 × recorded minutes, and Lucia TRIMP is between 1 and 3 × recorded minutes.
- Recalculate one Banister value by hand. Split the session into blocks of steady heart rate, multiply each block's minutes by x and the weighting, and add the blocks, as in the worked example. The result should be close to the per-sample sum.
- Confirm x is between 0 and 1 for every sample, or report the samples outside that range.
- Confirm the per-sample sum is no smaller than the session mean result for the same samples. The weighting curves upward, so the two are equal only when heart rate is constant.
- Confirm no sample is 0 bpm. Report how many artifacts were removed, and how many plausible values were above HRmax.
- Confirm the boundary rule is stated, and that a value on a boundary falls in the higher zone.
- Confirm HRmax source, HRrest, zone boundaries, method, Banister form, and weighting appear next to every result.

## Sources

This file cites these sources:

- Karvonen MJ, Kentala E, Mustala O. The effects of training on heart rate; a longitudinal study. Ann Med Exp Biol Fenn. 1957;35(3):307-315. PMID: 13470504. No DOI.
- Swain DP, Leutholtz BC, King ME, Haas LA, Branch JD. Relationship between % heart rate reserve and % VO2 reserve in treadmill exercise. Med Sci Sports Exerc. 1998;30(2):318-321. https://doi.org/10.1097/00005768-199802000-00022
- Tanaka H, Monahan KD, Seals DR. Age-predicted maximal heart rate revisited. J Am Coll Cardiol. 2001;37(1):153-156. https://doi.org/10.1016/S0735-1097(00)01054-8
- Nes BM, Janszky I, Wisløff U, Støylen A, Karlsen T. Age-predicted maximal heart rate in healthy subjects: the HUNT fitness study. Scand J Med Sci Sports. 2013;23(6):697-704. https://doi.org/10.1111/j.1600-0838.2012.01445.x
- Banister EW, Morton RH, Fitz-Clarke J. Dose/response effects of exercise modeled from training: physical and biochemical measures. Ann Physiol Anthropol. 1992;11(3):345-356. https://doi.org/10.2114/ahs1983.11.345
- Edwards S. The Heart Rate Monitor Book. Sacramento (CA): Fleet Feet Press; Port Washington (NY): Polar CIC; 1993. Third printing, October 1993. The Library of Congress catalogs the book (ISBN 0963463306, LCCN 92062064) as c1992. Book, not peer reviewed. The five zones are listed on p. 56 of the third printing. A text search of that printing found Chapter 12 on pp. 113-123, but no zone weights on those pages. The search covered text only, so a figure could still hold them. The zone weights in this file come from Paulson et al. (2015) and Hourcade et al. (2018).
- Lucia A, Hoyos J, Santalla A, Earnest C, Chicharro JL. Tour de France versus Vuelta a España: which is harder? Med Sci Sports Exerc. 2003;35(5):872-878. https://doi.org/10.1249/01.MSS.0000064999.82036.B4
- Paulson TA, Mason B, Rhodes J, Goosey-Tolfrey VL. Individualized internal and external training load relationships in elite wheelchair rugby players. Front Physiol. 2015;6:388. https://doi.org/10.3389/fphys.2015.00388
- Hourcade JC, Noirez P, Sidney M, Toussaint JF, Desgorces F. Effects of intensity distribution changes on performance and on training loads quantification. Biol Sport. 2018;35(1):67-74. https://doi.org/10.5114/biolsport.2018.70753
- Tomoto T, Tarumi T, Sugawara J. Associations among dynamic cerebral autoregulation, baroreflex sensitivity, and carotid distensibility in young healthy adults: insight from endurance training. Eur J Appl Physiol. 2026;126(6):3201-3220. https://doi.org/10.1007/s00421-026-06155-3
- Scantlebury S, Till K, Atkinson G, Sawczuk T, Jones B. The within-participant correlation between s-RPE and heart rate in youth sport. Sports Med Int Open. 2017;1(6):E195-E199. https://doi.org/10.1055/s-0043-118650
- Manzi V, Castagna C, Padua E, Lombardo M, D’Ottavio S, Massaro M, Volterrani M, Iellamo F. Dose-response relationship of autonomic nervous system responses to individualized training impulse in marathon runners. Am J Physiol Heart Circ Physiol. 2009;296(6):H1733-H1740. https://doi.org/10.1152/ajpheart.00054.2009
- Sheoran S, Stavropoulos-Kalinoglou A, Darrall-Jones J, Weaving D. Internal training exposure: development and construct validation of an individualised method using heart rate variability. Eur J Appl Physiol. 2025;125(11):3341-3350. https://doi.org/10.1007/s00421-025-05841-y
- Foster C, Florhaug JA, Franklin J, Gottschall L, Hrovatin LA, Parker S, Doleshal P, Dodge C. A new approach to monitoring exercise training. J Strength Cond Res. 2001;15(1):109-115. https://doi.org/10.1519/00124278-200102000-00019
- Impellizzeri FM, Rampinini E, Coutts AJ, Sassi A, Marcora SM. Use of RPE-based training load in soccer. Med Sci Sports Exerc. 2004;36(6):1042-1047. https://doi.org/10.1249/01.MSS.0000128199.23901.2F
- Alexiou H, Coutts AJ. A comparison of methods used for quantifying internal training load in women soccer players. Int J Sports Physiol Perform. 2008;3(3):320-330. https://doi.org/10.1123/ijspp.3.3.320
- Borresen J, Lambert MI. Quantifying training load: a comparison of subjective and objective methods. Int J Sports Physiol Perform. 2008;3(1):16-30. https://doi.org/10.1123/ijspp.3.1.16
- Borresen J, Lambert MI. The quantification of training load, the training response and the effect on performance. Sports Med. 2009;39(9):779-795. https://doi.org/10.2165/11317780-000000000-00000
- Haddad M, Stylianides G, Djaoui L, Dellal A, Chamari K. Session-RPE method for training load monitoring: validity, ecological usefulness, and influencing factors. Front Neurosci. 2017;11:612. https://doi.org/10.3389/fnins.2017.00612
- Impellizzeri FM, Marcora SM, Coutts AJ. Internal and external training load: 15 years on. Int J Sports Physiol Perform. 2019;14(2):270-273. https://doi.org/10.1123/ijspp.2018-0935
- Achten J, Jeukendrup AE. Heart rate monitoring: applications and limitations. Sports Med. 2003;33(7):517-538. https://doi.org/10.2165/00007256-200333070-00004
- Coyle EF, González-Alonso J. Cardiovascular drift during prolonged exercise: new perspectives. Exerc Sport Sci Rev. 2001;29(2):88-92. https://doi.org/10.1097/00003677-200104000-00009
- Glaister M, Gissane C. Caffeine and physiological responses to submaximal exercise: a meta-analysis. Int J Sports Physiol Perform. 2018;13(4):402-411. https://doi.org/10.1123/ijspp.2017-0312
- Karjalainen J, Viitasalo M. Fever and cardiac rhythm. Arch Intern Med. 1986;146(6):1169-1171. https://doi.org/10.1001/archinte.1986.00360180179026
- Gillinov S, Etiwy M, Wang R, Blackburn G, Phelan D, Gillinov AM, Houghtaling P, Javadikasgari H, Desai MY. Variable accuracy of wearable heart rate monitors during aerobic exercise. Med Sci Sports Exerc. 2017;49(8):1697-1703. https://doi.org/10.1249/MSS.0000000000001284
- Krustrup P, Mohr M, Amstrup T, Rysgaard T, Johansen J, Steensberg A, Pedersen PK, Bangsbo J. The Yo-Yo intermittent recovery test: physiological response, reliability, and validity. Med Sci Sports Exerc. 2003;35(4):697-705. https://doi.org/10.1249/01.MSS.0000058441.94520.32
- Krustrup P, Mohr M, Nybo L, Jensen JM, Nielsen JJ, Bangsbo J. The Yo-Yo IR2 test: physiological response, reliability, and application to elite soccer. Med Sci Sports Exerc. 2006;38(9):1666-1673. https://doi.org/10.1249/01.mss.0000227538.20799.08 (accessed 2026-10-02)
- Buchheit M, Al Haddad H, Millet GP, Lepretre PM, Newton M, Ahmaidi S. Cardiorespiratory and cardiac autonomic responses to 30-15 intermittent fitness test in team sport players. J Strength Cond Res. 2009;23(1):93-100. https://doi.org/10.1519/JSC.0b013e31818b9721 (accessed 2026-10-02)
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Med. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Banister EW. Modeling elite athletic performance. In: MacDougall JD, Wenger HA, Green HJ, editors. Physiological Testing of the High-Performance Athlete. 2nd ed. Champaign (IL): Human Kinetics Books; 1991:403-424. ISBN 0873223004. Book chapter, not peer reviewed. Read through the Internet Archive full-text search: https://archive.org/details/physiologicaltes0000unse (accessed 2026-10-02). The chapter prints both multiplier forms and, on pp. 406-409, adds phase scores to give session totals.
- Banister EW, Hamilton CL. Variations in iron status with fatigue modelled from training in female distance runners. Eur J Appl Physiol Occup Physiol. 1985;54(1):16-23. https://doi.org/10.1007/BF00426292 (accessed 2026-10-02)
- Polar Electro Oy. Polar Training Load Pro white paper. November 12, 2019; revised March 2025. https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf (accessed 2026-10-02)
- Polar Electro Oy. Polar Team Pro API reference, sport profile zone fields `lower_limit` (inclusive) and `higher_limit` (exclusive). https://www.polar.com/teampro-api/ (accessed 2026-10-02)
