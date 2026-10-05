# Isometric mid-thigh pull peak force

Last checked: 2026-10-02

## What it measures

Isometric mid-thigh pull (IMTP) peak force is the highest vertical force an athlete produces while pulling as hard and fast as possible on a fixed bar at mid-thigh height. "Isometric" means the bar does not move.

## Formula

Four versions are in use. Name the version in every result, because they differ by hundreds of newtons or by a factor of 9.81:

```text
gross peak force (N)               = highest vertical force during the pull
net peak force (N)                 = gross peak force - body weight
relative peak force (N/kg)         = peak force / body mass
allometric peak force (N/kg^0.67)  = peak force / body mass^0.67
```

Define every term in the formula:

- `vertical force`: the force the plate measures, in newtons (N). Sum both plates when the athlete stands on two.
- `body weight`: mean vertical force during the quiet period before the pull, with the athlete in the pull position and strapped to the bar, in N (Comfort et al., 2019)
- `gross peak force`: peak force that includes body weight
- `net peak force`: peak force with body weight removed (Comfort et al., 2019)
- `body mass`: in kg. Body weight in N divided by 9.81 gives body mass.
- `relative peak force`: peak force divided by body mass, also called ratio scaling. State whether you used net or gross force.
- `allometric peak force`: peak force divided by body mass raised to a power. Jaric (2002) recommends the power 0.67 for force, and Kraska et al. (2009) used it for IMTP force. Always state the power.

Neither net nor gross force is agreed to be better. Always report which one you used (Comfort et al., 2019).

### Rate of force development

Rate of force development (RFD) is how fast force rises. It is calculated over a time window measured from the onset of the pull:

```text
RFD 0-X ms (N/s) = (force at X ms after onset - force at onset) / (X / 1000)
```

Follow these rules for RFD:

- Find the onset of the pull with a threshold of 5 standard deviations of body weight, taken from a 1 s quiet period (Comfort et al., 2019; Dos'Santos et al., 2017).
- Use fixed time windows from onset, such as 0-50, 0-100, 0-150, 0-200, and 0-250 ms. These were reliable (Haff et al., 2015; Comfort et al., 2019).
- Do not use average RFD (peak force divided by time to peak force). It failed reliability standards (Haff et al., 2015).
- If you report peak RFD, name the sampling window. Published methods used windows from 2 to 50 ms, and the method changes reliability (Haff et al., 2015). Only peak RFD from a 20 ms moving window was reliable (Comfort et al., 2019, citing Haff et al., 2015).
- Expect RFD to be less reliable than peak force (Maffiuletti et al., 2016).

Use these spreadsheet formulas, with gross peak force in N in `B2` and body mass in kg in `C2`. Set `C2` to the body mass from the quiet period on the test day, body weight in N divided by 9.81. A scale weight gives a wrong net force. Each formula returns a blank when either input is blank:

```text
Net peak force:       =IF(OR(B2="",C2=""),"",B2-C2*9.81)
Relative net force:   =IF(OR(B2="",C2=""),"",(B2-C2*9.81)/C2)
Allometric gross:     =IF(OR(B2="",C2=""),"",B2/C2^0.67)
```

Without the blank check, a blank body mass makes net force equal gross force.

### Calculate it in Power BI and Tableau

These versions return a blank, not gross force, when body mass is missing.

Both versions assume one row per athlete, date, session, measure, and trial in a `measures` table. Gross peak force is `measure_name` `imtp_gross_peak_force` in `N`. Body mass from the quiet period is `measure_name` `imtp_body_mass` in `kg`, in the same session, as body weight in N divided by 9.81. Show the results with one athlete and one session per row.

In Power BI, use these DAX measures. They are measures because each result combines the force row and the body mass row:

```text
Gross peak force (N) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "imtp_gross_peak_force",
    measures[unit] = "N",
    measures[status] = "ok"
)

IMTP body mass (kg) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "imtp_body_mass",
    measures[unit] = "kg",
    measures[status] = "ok"
)

Net peak force (N) =
VAR f = [Gross peak force (N)]
VAR m = [IMTP body mass (kg)]
RETURN IF ( NOT ISBLANK ( f ) && NOT ISBLANK ( m ) && m > 0, f - m * 9.81 )

Relative net force (N/kg) =
VAR f = [Gross peak force (N)]
VAR m = [IMTP body mass (kg)]
RETURN IF ( NOT ISBLANK ( f ) && NOT ISBLANK ( m ) && m > 0, ( f - m * 9.81 ) / m )

Allometric gross (N/kg^0.67) =
VAR f = [Gross peak force (N)]
VAR m = [IMTP body mass (kg)]
RETURN IF ( NOT ISBLANK ( f ) && NOT ISBLANK ( m ) && m > 0, f / POWER ( m, 0.67 ) )
```

`MAX` over the trials gives the best trial. Put `trial_number` in the visual to see each trial.

In Tableau, put `athlete_id`, `measure_date`, and `session_id` on the view. Use these aggregate calculations:

```text
Gross peak force (N):
MAX(IF [measure_name] = "imtp_gross_peak_force" AND [unit] = "N" AND [status] = "ok" THEN [value] END)

IMTP body mass (kg):
MAX(IF [measure_name] = "imtp_body_mass" AND [unit] = "kg" AND [status] = "ok" THEN [value] END)

Net peak force (N):
IF ISNULL([Gross peak force (N)]) OR ISNULL([IMTP body mass (kg)]) THEN NULL
ELSEIF [IMTP body mass (kg)] <= 0 THEN NULL
ELSE [Gross peak force (N)] - [IMTP body mass (kg)] * 9.81
END

Relative net force (N/kg):
IF ISNULL([Gross peak force (N)]) OR ISNULL([IMTP body mass (kg)]) THEN NULL
ELSEIF [IMTP body mass (kg)] <= 0 THEN NULL
ELSE ([Gross peak force (N)] - [IMTP body mass (kg)] * 9.81) / [IMTP body mass (kg)]
END

Allometric gross (N/kg^0.67):
IF ISNULL([Gross peak force (N)]) OR ISNULL([IMTP body mass (kg)]) THEN NULL
ELSEIF [IMTP body mass (kg)] <= 0 THEN NULL
ELSE [Gross peak force (N)] / POWER([IMTP body mass (kg)], 0.67)
END
```

Blanks behave this way in each tool:

- Power BI: a blank body mass times 9.81 is blank, and a number minus a blank is the number. So a plain `f - m * 9.81` silently gives gross force. The `ISBLANK` test stops that.
- Tableau: a null body mass makes the arithmetic null. The `ISNULL` test makes that explicit, and the `<= 0` test stops a division by 0.

## Calculate the metric

Follow these steps to calculate peak force from a raw trace:

1. Load the vertical force column in N and the time column in s. If the export has one column per plate, add them into one `force_n` column.
2. In the 1 s quiet period with the athlete in the pull position, calculate the mean as `body_weight_n` and the standard deviation as `bw_sd_n`.
3. Check the quiet period. If force changes by more than 50 N, reject the trial (Comfort et al., 2019).
4. Divide `body_weight_n` by 9.81 to get `body_mass_kg`.
5. Find the onset of the pull: the first sample where `force_n` is above `body_weight_n + 5 × bw_sd_n`.
6. Find the highest `force_n` between onset and the end of the pull. This is gross peak force.
7. Subtract `body_weight_n` to get net peak force.
8. Repeat for each trial.
9. Collect at least two trials, and add trials until peak forces are within 250 N of each other (Comfort et al., 2019).
10. Apply your trial rule, the best trial or the mean of trials, and state it. Use the same rule at every session.
11. Divide by `body_mass_kg` for relative peak force, or by `body_mass_kg` raised to 0.67 for allometric peak force. Name net or gross.
12. For RFD, read force at onset and at each fixed time after onset.
13. Apply the RFD formula.

## Worked example

This example uses a simplified synthetic pull sampled at 1000 Hz.

| Input | Value |
|---|---|
| Quiet period | 1.000 s, alternating 832 N and 836 N |
| Gross peak force, trials 1 to 3 | 2905 N, 2610 N, 2840 N |
| Force at onset | 846 N |
| Force at 50, 100, 150, 200, 250 ms after onset | 1120, 1490, 1820, 2080, 2260 N |

Step 1. Calculate body weight and body mass:

- Mean quiet force = 834.00 N. Standard deviation = 2.0010 N.
- Body mass = 834.00 / 9.81 = 85.0153 kg.
- Onset threshold = 834.00 + 5 × 2.0010 = 844.01 N.

Step 2. Check the trials:

- The three trials span 295 N, which is more than 250 N.
- The two highest trials, 2905 N and 2840 N, are 65 N apart, so no more trials are needed. With the best-trial rule, report 2905 N.

Step 3. Calculate the peak force versions:

- Gross peak force = 2905.0 N.
- Net peak force = 2905.0 - 834.0 = 2071.0 N.
- Relative gross = 2905.0 / 85.0153 = 34.17 N/kg.
- Relative net = 2071.0 / 85.0153 = 24.36 N/kg.
- Allometric gross = 2905.0 / 85.0153^0.67 = 148.0 N/kg^0.67.
- Allometric net = 2071.0 / 85.0153^0.67 = 105.5 N/kg^0.67.

Step 4. Calculate RFD over fixed windows:

- RFD 0-50 ms = (1120 - 846) / 0.050 = 5480 N/s.
- RFD 0-100 ms = (1490 - 846) / 0.100 = 6440 N/s.
- RFD 0-150 ms = (1820 - 846) / 0.150 = 6493 N/s.
- RFD 0-200 ms = (2080 - 846) / 0.200 = 6170 N/s.
- RFD 0-250 ms = (2260 - 846) / 0.250 = 5656 N/s.

Result: the same pull is 2905.0 N gross, 2071.0 N net, 34.17 or 24.36 N/kg relative, and 148.0 or 105.5 N/kg^0.67 allometric. Each label is needed to read the number.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Net or gross force. In the worked example, the gap is the full body weight, 834.0 N.
- Scaling. Ratio scaling and allometric scaling give different values. Published studies use both, so check which one before you compare (Comfort et al., 2019).
- Dividing by body weight in N instead of body mass in kg. In the worked example this gives 3.483 with no units, instead of 34.17 N/kg.
- Onset threshold. Fixed thresholds such as 75 N above body weight or 10% of body weight above body weight move the onset later than 5 standard deviations of body weight, and change time-specific force and RFD (Dos'Santos et al., 2017). In a second synthetic pull with a smooth force rise, moving from the 5 standard deviation threshold to a threshold 75 N above body weight moved onset 4 ms later. It raised force at 100 ms from 2012.4 N to 2041.7 N.
- Posture. Different knee and hip angles change force output, so record and repeat them (Comfort et al., 2019).
- Sampling rate and filtering. These change early force-time measures most (Comfort et al., 2019).
- RFD method. Fixed windows, peak RFD, and average RFD give different values with different reliability (Haff et al., 2015).
- Pre-tension. Pulling on the bar before the start changes the measured body weight and the onset (Comfort et al., 2019).

## Units and typical range

Report peak force in N, relative force in N/kg, and allometric force in N/kg^0.67. Name net or gross, and the knee and hip angles.

This file gives no published range. Peak force depends on body mass, sex, training, posture, and whether body weight is included, so a range from another setup cannot show a data error. Compare an athlete with their own earlier tests in the same setup.

Run these internal checks in place of a range check:

- Net peak force is smaller than gross peak force by exactly one body weight. In the worked example, 2905.0 - 2071.0 = 834.0 N.
- Gross peak force is above body weight. If it is not, the trace or the trial is wrong.
- The trials you used are within 250 N of each other (Comfort et al., 2019). In the worked example, the two highest are 65 N apart.
- A relative value is not 9.81 times too small. In the worked example, 34.17 N/kg is 9.81 times 3.483, the value from dividing by body weight in N.

Use this test variability from a retest on a separate day to judge a change in one athlete. In elite male ice hockey players (n = 21 for this test), the standard error of measurement of peak force was 104 N, a coefficient of variation of 3.1% (Godhe et al., 2025). The protocol used hip and knee angles of about 145°, the best of 3 trials, and a retest 24 h later.

Use it only when your protocol and athletes match. Otherwise, measure your own typical error from a short-term retest in which no true change is expected. A separate-day retest counts day-to-day variation as noise and gives a larger typical error than a same-day retest. Judge a change with the noise band, 1.96 × TE × √(1 + 1/n) for a baseline mean of n tests, as the `force-plate` skill describes.

## Data you need

Collect this data:

- Source: a force plate under a fixed bar, such as a rack with pins or a custom pull frame
- Sampling: IMTP data can be collected accurately at 500 Hz. Use at least 1000 Hz for early force-time measures such as RFD or force at 100 ms. Use unfiltered data where possible (Comfort et al., 2019).
- Posture: knee angle of 125 to 145° and hip angle of 140 to 150°. Record the angles and bar height, and keep them the same at every test (Comfort et al., 2019).
- Minimum data: at least two clean trials. Add trials until peak force values are within 250 N of each other (Comfort et al., 2019).
- Warm-up: a standard generalized warm-up, the same at every session (Comfort et al., 2019). Comfort et al. (2019) also recommend submaximal pulls before the maximal trials.
- Quiet period: at least 1 s of stable force before the pull. Reject the trial if force changes by more than 50 N during this period (Comfort et al., 2019).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Mixing net and gross values in one column, or comparing a gross value with a published net value
- Dividing by body weight in N instead of body mass in kg. The result is 9.81 times too small and has no units.
- Using allometric scaling without stating the power
- Reading one plate of a two-plate setup as the whole force. Sum both plates.
- Changing knee angle, hip angle, or bar height between sessions and then comparing peak force
- Keeping trials with a countermovement, a dip before the pull, too much pre-tension on the bar, or leaning on the bar (Comfort et al., 2019). Flag them instead.
- Finding onset with a fixed force threshold such as 75 N or 10% of body weight above body weight. These gave unacceptable agreement with the 5 standard deviation threshold (Dos'Santos et al., 2017).
- Reporting average RFD as if it were a reliable measure
- Taking the peak from outside the pull, such as a spike when the athlete lets go of the bar. Restrict the search to the pull.
- Using a different body mass for relative force than the one measured on the day

## Example request

> I have IMTP peak force for my team from three test days, plus body weight. Can you make a table of relative peak force and tell me who improved?

## Check the result

Run these checks:

- Recompute one value by hand. For gross peak force of 2500 N and body mass of 80 kg: net = 2500 - 784.8 = 1715.2 N, relative net = 21.44 N/kg, relative gross = 31.25 N/kg.
- Check that net peak force is smaller than gross by one body weight. If a relative value is about 9.81 times too small and has no units, body weight in N was used in place of body mass in kg.
- Check that the trials you used are within 250 N of each other, and say so if they are not.

## Sources

This file cites these sources:

- Comfort P, Dos'Santos T, Beckham GK, Stone MH, Guppy SN, Haff GG. Standardization and methodological considerations for the isometric midthigh pull. Strength and Conditioning Journal. 2019;41(2):57-79. https://doi.org/10.1519/SSC.0000000000000433
- Dos'Santos T, Jones PA, Comfort P, Thomas C. Effect of different onset thresholds on isometric midthigh pull force-time variables. Journal of Strength and Conditioning Research. 2017;31(12):3463-3473. https://doi.org/10.1519/JSC.0000000000001765
- Haff GG, Ruben RP, Lider J, Twine C, Cormie P. A comparison of methods for determining the rate of force development during isometric midthigh clean pulls. Journal of Strength and Conditioning Research. 2015;29(2):386-395. https://doi.org/10.1519/JSC.0000000000000705
- Maffiuletti NA, Aagaard P, Blazevich AJ, Folland J, Tillin N, Duchateau J. Rate of force development: physiological and methodological considerations. European Journal of Applied Physiology. 2016;116(6):1091-1116. https://doi.org/10.1007/s00421-016-3346-6
- Jaric S. Muscle strength testing: use of normalisation for body size. Sports Medicine. 2002;32(10):615-631. https://doi.org/10.2165/00007256-200232100-00002
- Kraska JM, Ramsey MW, Haff GG, Fethke N, Sands WA, Stone ME, Stone MH. Relationship between strength characteristics and unweighted and weighted vertical jump height. International Journal of Sports Physiology and Performance. 2009;4(4):461-473. https://doi.org/10.1123/ijspp.4.4.461
- Godhe M, Bergman S, Petré H. Between-session reliability of portable isometric mid-thigh pull and countermovement jump tests in elite male ice hockey players from the Swedish Hockey League. Sports. 2025;13(12):456. https://doi.org/10.3390/sports13120456
