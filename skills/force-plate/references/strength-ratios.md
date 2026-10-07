# Strength ratios: dynamic strength index and eccentric utilization ratio

Last checked: 2026-10-07

## What it measures

This file covers two ratios that compare one force plate test with another:

- **Dynamic strength index (DSI):** how much of the force an athlete can produce in an isometric pull the athlete also produces in a jump. It divides jump peak force by isometric mid-thigh pull (IMTP) peak force.
- **Eccentric utilization ratio (EUR):** how much a countermovement helps the athlete jump. It divides countermovement jump (CMJ) performance by squat jump (SJ) performance. A squat jump starts from a held squat, with no dip before the push.

A ratio has no unit. It changes when either test changes. Always report the two test results beside the ratio.

This file found no survey that reports how many practitioners use either ratio. Each ratio needs two tests, and the second test may limit who can calculate it. In a 2024 survey of elite male soccer practitioners, 28 of the 79 who tested strength used the IMTP (35%). 33 of the 74 who tested power or reactive strength used the squat jump (45%). The CMJ was used by 68 of those 74 (92%) (Asimakidis et al., 2024). Those percentages are of subgroups, not of all 102 respondents.

Use these ratios as decision support for healthy athletes. A ratio does not diagnose anything, and it does not decide a training program. Leave every training decision to the coach.

## Formula

Use these formulas:

```text
DSI, gross (no unit)       = CMJ peak propulsive force, gross (N) / IMTP peak force, gross (N)
DSI, net (no unit)         = (CMJ peak propulsive force - CMJ body weight) / (IMTP peak force - IMTP body weight)
DSI, SJ version (no unit)  = SJ peak force (N) / IMTP peak force (N)
EUR, height (no unit)      = CMJ height (m) / SJ height (m)
EUR, peak power (no unit)  = CMJ peak power (W) / SJ peak power (W)
```

Define every term in the formula:

- `CMJ peak propulsive force`: the highest vertical force in the propulsion phase of the CMJ, in newtons (N). The propulsion phase runs from zero velocity, or a threshold of 0.01 m/s, to takeoff. See `cmj-strategy-metrics.md`. Ripley et al. (2025) and McMahon et al. (2017) used this definition.
- `gross`: the force includes body weight. This is the force the plate measures, summed across both plates.
- `net`: the force minus the body weight from the same trial's quiet period, the still period before the test starts.
- `IMTP peak force`: the highest vertical force in the pull. See `imtp-peak-force.md` for the quiet period, body weight, and trial rules.
- `SJ peak force`: the highest vertical force in the squat jump push, in N.
- `CMJ height` and `SJ height`: jump height from the same method for both jumps, in m. Use the takeoff velocity method when you have the raw trace. See `cmj-jump-height.md`.
- `peak power`: the highest product of force and center of mass velocity in the push, in watts (W).

### Name the peak force definition

The DSI is only as good as the match between its two peak forces. Name each of these choices next to every DSI, and use the same choice for both tests:

- **Gross or net.** The published DSI studies do not use the words gross or net. McMahon et al. (2017) report CMJ propulsion peak force of about 25 N/kg and IMTP peak force of 31 to 47 N/kg. This file assumes those values are gross, because the papers describe the highest force recorded and do not describe subtracting body weight. Gross over gross is this repository's default, chosen so your values match the published ones. In the worked example below, net over net gives 0.583 where gross over gross gives 0.710.
- **Phase window for the CMJ.** Take the CMJ peak from the propulsion phase only. The highest force of the whole jump can fall in the braking phase, the part of the dip where the athlete slows the downward movement (see `cmj-strategy-metrics.md`). Say which window you used.
- **Sampling and filtering.** The DSI studies opened for this file sampled at 1000 Hz and analyzed raw force data (McMahon et al., 2017). Two of them state the data were unfiltered (Comfort et al., 2018b; Ripley et al., 2025). A filter can change a peak value. Use the same sampling rate and filter for both tests.
- **Trial rule.** Use the mean of trials or the best trial for both tests. Comfort et al. (2018b) and Ripley et al. (2025) used the mean of three trials.

### Choose the CMJ or the squat jump for the DSI

Use the CMJ version. In 27 male youth soccer and rugby league players, the DSI from the CMJ had nearly perfect within-session reliability in both sessions (intraclass correlation coefficient, ICC, 0.920 to 0.952) and a coefficient of variation (CV) of 3.80 to 4.57%. The DSI from the squat jump had an ICC of 0.419 and a CV of 15.91% in the first session. It improved in the second session. Between sessions, the ICC was 0.924 for the CMJ version and 0.741 for the SJ version. The two versions gave similar values: 0.84 ± 0.15 for the CMJ and 0.82 ± 0.18 for the SJ (Comfort et al., 2018a). Never mix the two versions in one table or trend.

### Know the impulse-based DSI

Some studies divide impulse instead of peak force (Ripley et al., 2025):

- **Fixed impulse DSI:** CMJ propulsive impulse divided by IMTP impulse from onset of the pull to 250 ms.
- **Matched impulse DSI:** CMJ propulsive impulse divided by IMTP impulse over a window as long as that athlete's CMJ propulsion phase.

In 37 team sport athletes (24 men, 13 women), the force-based DSI had good relative reliability and acceptable absolute reliability. Both impulse versions had moderate relative reliability and unacceptable absolute reliability (Ripley et al., 2025). This file uses the force-based DSI. Name the version in every result.

### State the agreement problem beside every DSI

The force-based and impulse-based DSI often put the same athlete in different training groups. In the 37 athletes above, the force-based DSI and the matched impulse DSI agreed on the training emphasis for 17 athletes (45.9%). The force-based DSI and the fixed impulse DSI agreed for 21 (56.8%). The two impulse versions agreed for 32 (86.5%) (Ripley et al., 2025). These are the figures in the body of the paper. Its abstract reports slightly different values: 44.7%, 55.3%, and 84.2%.

Put this sentence beside every DSI you report: "Force-based and impulse-based DSI agreed on training emphasis for 45.9% to 56.8% of athletes in one study, depending on the impulse method (Ripley et al., 2025). The ratio depends on the method."

### Know the published DSI bands

Published studies use these bands. They are study settings, not recommendations, and not targets:

| DSI | What the study used the band to describe | Source |
|---|---|---|
| Below 0.60 | Athletes the study grouped under a ballistic (fast, explosive) training emphasis | Comfort et al., 2018b; Ripley et al., 2025 |
| 0.60 to 0.80 | Athletes the study grouped under a mixed ballistic and strength emphasis | Ripley et al., 2025 |
| Above 0.80 | Athletes the study grouped under a maximal strength training emphasis | Comfort et al., 2018b; Ripley et al., 2025 |

Comfort et al. (2018b) attribute the bands to Sheppard JM, Chapman DW, and Taylor K (Journal of Australian Strength and Conditioning, 2011), which this file could not open. It is not listed in Sources for that reason. McMahon et al. (2017) write the bands as 0.60 or less and 0.80 or more. Follow these rules for the bands:

- Show a band only as a published study setting, with its source. Never write that an athlete "should" train one way.
- Show the athlete's relative IMTP peak force beside the DSI. McMahon et al. (2017) note that a weak athlete can also have a low DSI, so the DSI alone does not show how strong the athlete is.
- Expect the band to change with the method. In the worked example, the same tests fall in the 0.60 to 0.80 band as gross over gross and below 0.60 as net over net.
- Do not read a DSI as how well the athlete can use strength in general. McMahon et al. (2017) note that the DSI shows how the athlete expressed force in the test performed, and that jump strategy changes CMJ peak force. In their 53 male college athletes, the low and high DSI groups had similar CMJ propulsion peak force (25.9 ± 2.2 and 25.4 ± 3.1 N/kg). The low DSI group had a higher IMTP peak force and a deeper, faster countermovement.

### Know what the EUR can and cannot tell you

McGuigan et al. (2006) measured the EUR in 142 athletes from rugby union, Australian football, soccer, softball, and field hockey. They found these results:

- In men, the EUR was higher in soccer, Australian football, and rugby union than in softball. In women, it was higher in soccer than in field hockey and softball. The authors link a higher EUR to sports that rely more on the stretch-shortening cycle, the quick stretch of a muscle just before it shortens.
- In field hockey, the EUR rose from off-season to preseason.
- The height method and the peak power method gave significantly different EUR values in some preseason tests.

These are group findings from one study. This file read only its abstract. The study does not support these readings, so do not use them:

- A threshold or band for one athlete. This file gives none.
- The EUR as a measure of eccentric strength. It compares two jumps. It does not measure force while the muscle lengthens.
- A training prescription from one athlete's EUR.

Never mix the height version and the power version.

### Write the spreadsheet formulas

These formulas work in Excel and Google Sheets. Use one row per athlete, session, test, and trial, with these columns:

| Column | Content | Unit |
|---|---|---|
| A | `athlete_id` | text |
| B | `session_id` | text |
| C | `test_type`: `CMJ`, `SJ`, or `IMTP` | text |
| D | `trial_number` | number |
| E | gross peak force: propulsion phase for the CMJ, the push for the SJ, the pull for the IMTP | N |
| F | body weight from the same trial's quiet period | N |
| G | jump height, takeoff velocity method (blank for the IMTP) | m |

Put each athlete in `R2` and each session in `S2` on a summary sheet. Use these formulas in row 2, then fill down. Each returns a blank when an input is missing:

```text
T2, CMJ mean peak force (N):
=IFERROR(AVERAGEIFS($E$2:$E$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ"),"")

U2, IMTP mean peak force (N):
=IFERROR(AVERAGEIFS($E$2:$E$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"IMTP"),"")

V2, CMJ mean body weight (N):
=IFERROR(AVERAGEIFS($F$2:$F$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ"),"")

W2, IMTP mean body weight (N):
=IFERROR(AVERAGEIFS($F$2:$F$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"IMTP"),"")

X2, DSI gross:
=IF(COUNT(T2,U2)<2,"",IF(U2<=0,"",T2/U2))

Y2, DSI net:
=IF(COUNT(T2,U2,V2,W2)<4,"",IF(U2-W2<=0,"",(T2-V2)/(U2-W2)))

Z2, CMJ mean height (m):
=IFERROR(AVERAGEIFS($G$2:$G$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ"),"")

AA2, SJ mean height (m):
=IFERROR(AVERAGEIFS($G$2:$G$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"SJ"),"")

AB2, EUR height:
=IF(COUNT(Z2,AA2)<2,"",IF(AA2<=0,"",Z2/AA2))

AC2, trials per test, for the count check:
=COUNTIFS($A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ")&" CMJ, "&COUNTIFS($A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"SJ")&" SJ, "&COUNTIFS($A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"IMTP")&" IMTP"
```

For the best trial, use `MAXIFS` in place of `AVERAGEIFS` for both tests. `MAXIFS` returns 0, not an error, when no row matches, so guard it, for example `=IF(COUNTIFS($A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ")=0,"",MAXIFS($E$2:$E$500,$A$2:$A$500,R2,$B$2:$B$500,S2,$C$2:$C$500,"CMJ"))`. Never mix the two rules.

### Calculate it in Power BI

These versions assume one row per athlete, date, session, measure, and trial in a `measures` table. Store the values with these names, and convert units on import:

| `measure_name` | Content | `unit` |
|---|---|---|
| `cmj_peak_propulsive_force` | CMJ gross peak force in the propulsion phase | `N` |
| `imtp_gross_peak_force` | IMTP gross peak force | `N` |
| `cmj_jump_height` | CMJ height, takeoff velocity method | `m` |
| `sj_jump_height` | SJ height, takeoff velocity method | `m` |

Use these DAX measures. With athlete and session in the visual, each mean covers that session's trials:

```text
CMJ peak propulsive force, mean (N) =
CALCULATE (
    AVERAGE ( measures[value] ),
    measures[measure_name] = "cmj_peak_propulsive_force",
    measures[unit] = "N",
    measures[status] = "ok"
)

IMTP gross peak force, mean (N) =
CALCULATE (
    AVERAGE ( measures[value] ),
    measures[measure_name] = "imtp_gross_peak_force",
    measures[unit] = "N",
    measures[status] = "ok"
)

DSI, gross =
VAR c = [CMJ peak propulsive force, mean (N)]
VAR i = [IMTP gross peak force, mean (N)]
RETURN IF ( NOT ISBLANK ( c ) && NOT ISBLANK ( i ) && i > 0, c / i )

CMJ height, mean (m) =
CALCULATE (
    AVERAGE ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "m",
    measures[status] = "ok"
)

SJ height, mean (m) =
CALCULATE (
    AVERAGE ( measures[value] ),
    measures[measure_name] = "sj_jump_height",
    measures[unit] = "m",
    measures[status] = "ok"
)

EUR, height =
VAR c = [CMJ height, mean (m)]
VAR s = [SJ height, mean (m)]
RETURN IF ( NOT ISBLANK ( c ) && NOT ISBLANK ( s ) && s > 0, c / s )
```

A blank input gives a blank ratio, not 0 and not a division error. For the best trial, use `MAX` in place of `AVERAGE` in both inputs.

### Calculate it in Tableau

Put `athlete_id`, `measure_date`, and `session_id` on the view. Use these aggregate calculations:

```text
CMJ peak propulsive force, mean (N):
AVG(IF [measure_name] = "cmj_peak_propulsive_force" AND [unit] = "N" AND [status] = "ok" THEN [value] END)

IMTP gross peak force, mean (N):
AVG(IF [measure_name] = "imtp_gross_peak_force" AND [unit] = "N" AND [status] = "ok" THEN [value] END)

DSI, gross:
IF ISNULL([CMJ peak propulsive force, mean (N)]) OR ISNULL([IMTP gross peak force, mean (N)]) THEN NULL
ELSEIF [IMTP gross peak force, mean (N)] <= 0 THEN NULL
ELSE [CMJ peak propulsive force, mean (N)] / [IMTP gross peak force, mean (N)]
END

EUR, height:
IF ISNULL(AVG(IF [measure_name] = "sj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)) THEN NULL
ELSEIF AVG(IF [measure_name] = "sj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END) <= 0 THEN NULL
ELSE AVG(IF [measure_name] = "cmj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)
   / AVG(IF [measure_name] = "sj_jump_height" AND [unit] = "m" AND [status] = "ok" THEN [value] END)
END
```

`AVG` skips nulls, so a missing trial does not count as 0. A missing test gives a null ratio. For the net DSI, the SJ version, and the peak power EUR, follow the same pattern with the matching measures. Subtract each test's own body weight before dividing.

### Calculate it in Python or R

Use this Python sketch for a table with one row per athlete, session, test, and trial:

```python
import pandas as pd

keys = ["athlete_id", "session_id"]
# trials columns: athlete_id, session_id, test_type, peak_force_n (gross), body_weight_n, jump_height_m
s = trials.groupby(keys + ["test_type"])[["peak_force_n", "body_weight_n", "jump_height_m"]].mean().unstack("test_type")

out = pd.DataFrame(index=s.index)
out["dsi_gross"] = s[("peak_force_n", "CMJ")] / s[("peak_force_n", "IMTP")]
out["dsi_net"] = (s[("peak_force_n", "CMJ")] - s[("body_weight_n", "CMJ")]) / (
    s[("peak_force_n", "IMTP")] - s[("body_weight_n", "IMTP")])
out["eur_height"] = s[("jump_height_m", "CMJ")] / s[("jump_height_m", "SJ")]
out = out.join(trials.groupby(keys + ["test_type"]).size().unstack("test_type").add_prefix("n_"))
```

On the worked example below, this sketch gives a gross DSI of 0.7102, a net DSI of 0.583, and an EUR of 1.1136, with 3 trials of each test.

Use this R sketch for the same table:

```r
library(dplyr)
library(tidyr)

out <- trials |>
  group_by(athlete_id, session_id, test_type) |>
  summarise(pf = mean(peak_force_n), bw = mean(body_weight_n),
            h = mean(jump_height_m), n = n(), .groups = "drop") |>
  pivot_wider(names_from = test_type, values_from = c(pf, bw, h, n)) |>
  mutate(dsi_gross = pf_CMJ / pf_IMTP,
         dsi_net = (pf_CMJ - bw_CMJ) / (pf_IMTP - bw_IMTP),
         eur_height = h_CMJ / h_SJ)
```

A missing test gives `NaN` in Python and `NA` in R. Keep those rows, and say which test is missing.

## Calculate the metric

Follow these steps to calculate the DSI:

1. Confirm the export has a test type column, such as VALD `Test Type` or Hawkin `testType_name`. See `vald-forcedecks.md` and `hawkin-dynamics.md`.
2. Keep the CMJ and IMTP trials for each athlete.
3. Find the CMJ peak force column. Neither device file in this skill maps a CMJ peak propulsive force column. VALD `Peak Net Take-off Force / BM` is net force per kg, and `vald-forcedecks.md` does not state its phase window. Read the vendor's definition, and confirm the phase window and whether the value is gross or net.
4. Find the IMTP peak force column. Confirm gross or net, as in `imtp-peak-force.md`.
5. Convert any net value to gross by adding that trial's body weight in N. Convert a value per kg to N by multiplying by body mass in kg first.
6. Check that both tests used the same sampling rate and filter.
7. Apply one trial rule to both tests, the mean of trials or the best trial.
8. Divide CMJ peak propulsive force by IMTP peak force.
9. Report the DSI with the method name, both peak forces, relative IMTP peak force, and the agreement sentence from Ripley et al. (2025).

Follow these steps to calculate the EUR:

1. Keep the CMJ and SJ trials from the same session for each athlete.
2. Check every SJ trial for a dip before the push, as described under "Data you need". Flag any trial with a dip.
3. Confirm both jump heights use the same method and the same arm condition.
4. Apply one trial rule to both jumps.
5. Divide CMJ height by SJ height. For the power version, divide CMJ peak power by SJ peak power.
6. Report the EUR with the version name and both jump values.

## Worked example

This example uses made-up data for one athlete, all from one session. Every force is gross. Body weight is 822 N in the CMJ quiet period and 820 N in the IMTP quiet period.

| Test | Trial 1 | Trial 2 | Trial 3 | Mean |
|---|---|---|---|---|
| IMTP peak force (N) | 2690 | 2720 | 2700 | 2703.33 |
| CMJ peak propulsive force (N) | 1905 | 1935 | 1920 | 1920.00 |
| CMJ height (m) | 0.352 | 0.361 | 0.346 | 0.3530 |
| SJ height (m) | 0.318 | 0.324 | 0.309 | 0.3170 |

Step 1. Calculate the DSI both ways:

- DSI, gross = 1920.00 / 2703.33 = 0.7102.
- CMJ net peak force = 1920.00 - 822 = 1098.00 N. IMTP net peak force = 2703.33 - 820 = 1883.33 N.
- DSI, net = 1098.00 / 1883.33 = 0.5830.
- With the best trial instead, DSI, gross = 1935 / 2720 = 0.7114.

Step 2. Calculate the EUR:

- EUR, height = 0.3530 / 0.3170 = 1.1136.
- With made-up mean peak powers of 4328.3 W in the CMJ and 4190.0 W in the SJ, EUR, peak power = 1.033. The two versions differ, so name the version.

Step 3. Read the DSI against the published bands:

- The gross DSI, 0.710, falls in the 0.60 to 0.80 band that the studies used. The net DSI, 0.583, falls below 0.60. The athlete did not change. Only the method did.
- Report it this way: "DSI 0.71 (CMJ peak propulsive force ÷ IMTP peak force, both gross, mean of 3, 1000 Hz, unfiltered). Published studies used 0.60 to 0.80 as a mixed-training band; this is a study setting, not a recommendation. Force-based and impulse-based DSI agreed on training emphasis for 45.9% to 56.8% of athletes in one study, depending on the impulse method (Ripley et al., 2025)."

Step 4. Judge a change. Four weeks later, IMTP peak force is 2810, 2850, and 2830 N (mean 2830.00 N). CMJ peak propulsive force is 1925, 1950, and 1940 N (mean 1938.33 N):

- DSI, gross = 1938.33 / 2830.00 = 0.6849. The change is -0.0253.
- The squad's made-up separate-day CV is 3.0% for CMJ peak propulsive force and 3.5% for IMTP peak force, each as a mean of 3.
- Approximate CV of the ratio = √(3.0² + 3.5²) = 4.61%. Approximate TE of the DSI = 0.0461 × 0.7102 = 0.0327.
- Noise band for two single tests = 1.96 × √2 × 0.0327 = ±0.0908.
- The change of -0.0253 is inside the noise band. Report the two tests as well: IMTP peak force rose 4.69%, and CMJ peak force rose 0.95%. Both changes are inside their own bands of about ±9.70% and ±8.32%.

Result: the DSI fell, but by less than measurement error. A falling DSI can come from a rising IMTP peak force with little change in the jump, as Comfort et al. (2018b) found in a group after four weeks of strength training. Report the change, its band, and both tests. Leave training decisions to the coach.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Gross or net force. In the worked example, gross gives 0.710 and net gives 0.583.
- The CMJ phase window. A peak from the whole jump can come from the braking phase and differ from the propulsion phase peak.
- CMJ or SJ for the DSI. The SJ version was less reliable (Comfort et al., 2018a).
- Force or impulse. The impulse versions give different values and different training groups (Ripley et al., 2025).
- Jump strategy. A deeper countermovement can lower CMJ peak propulsive force (McMahon et al., 2017). Keep the same cue at every test.
- SJ start depth. Published starting knee angles ranged from 45° to 110°, and start depth changes SJ peak force (McMahon et al., 2017). Record the depth and keep it the same.
- A hidden dip in the squat jump. It makes the SJ partly a countermovement jump, so the EUR no longer compares the two conditions it is meant to compare.
- Jump height method. Flight time and takeoff velocity heights differ. Use one method for both jumps. See `cmj-jump-height.md`.
- Arm swing. Keep hands on hips, or the same arm condition, in both jumps.
- Trial rule. The best trial and the mean of trials give different ratios. In the worked example, 0.7114 and 0.7102.
- IMTP posture and protocol. See `imtp-peak-force.md`.
- Sampling rate and filtering, as described above.

## Units and typical range

A ratio has no unit. Report it to two or three decimal places, with the method, the trial rule, and both test values.

| Population | Value | Source |
|---|---|---|
| Male youth soccer and rugby league players (n = 27), CMJ version, 3 trials | DSI 0.84 ± 0.15 (mean ± SD) | Comfort et al., 2018a |
| Same players, SJ version | DSI 0.82 ± 0.18 (mean ± SD) | Comfort et al., 2018a |
| Team sport athletes (24 men, 13 women), CMJ propulsion peak force, mean of 3, 1000 Hz, unfiltered | DSI 0.82 ± 0.12 (mean ± SD), as the abstract reports. Table 1 prints 0.79 ± 0.03 for the force-based DSI. | Ripley et al., 2025 |
| Male college athletes (n = 53), lowest and highest 20 DSI scores, CMJ propulsion peak force, 1000 Hz | 0.55 ± 0.10 and 0.92 ± 0.11 (mean ± SD). These are extreme groups, not the whole squad. Do not use them for a 3 SD range check. | McMahon et al., 2017 |
| Male college athletes (n = 19), SJ version | DSI 0.78 ± 0.19 (mean ± SD) | Thomas et al., 2015 |

Use these values to check that data are plausible. Do not use them to rate athletes. This file gives no EUR range, because the EUR source was read as an abstract only and the abstract gives no values.

Run these checks in place of an EUR range:

- In 18 men, a countermovement raised jump height (Harman et al., 1990). Expect CMJ height to be higher than SJ height, so an EUR above 1.00. An EUR below 1.00 is a reason to check the trials, not proof of an error.
- A DSI above 1.00 means the jump force was higher than the pull force. Check the IMTP trials, the units, and the gross or net labels.

### Judge a change

Use the typical error (TE) rules in the `monitoring-statistics` skill, or the noise band in the `force-plate` skill. A ratio carries the error of both tests. Follow these rules:

- Measure the TE of the ratio itself from a short-term retest of your squad, with the same method and trial rule. This is the best option.
- If you have only the TE of each test, as a CV, combine them as √(CV₁² + CV₂²). This approximation assumes the two errors are independent and small. It is this repository's choice, not a published rule. For the net DSI, use CVs of net force, because gross-force CVs understate the noise. When both tests come from the same session, their errors may move together. Then this formula can overstate the noise in the ratio. A typical error measured on the ratio itself, from repeat sessions, is better when you have one.
- This file found one published separate-day reliability result, for the SJ version: in 19 male college athletes, TE was 0.03 and CV was 4.6% (Thomas et al., 2015). Use it only when your protocol and athletes match.
- Within one session, the DSI had a CV of 4.69% in 24 college athletes (Comfort et al., 2018b). That is trial-to-trial spread, not day-to-day noise. Do not use it as the TE for a change between sessions.
- Report the change in each test beside the change in the ratio.

## Data you need

Collect this data:

- Source: a force plate under a fixed bar for the IMTP, and the same force plate for the jumps. You need peak force for the DSI and jump height or peak power for the EUR.
- Export: a test type column, so each trial is labeled CMJ, SJ, or IMTP. Without it, you cannot tell the jumps apart.
- Sampling: 1000 Hz, as in the DSI studies opened for this file (McMahon et al., 2017; Comfort et al., 2018b; Ripley et al., 2025). Use the same rate and filter for every test.
- Minimum data: three trials of each test. Follow the trial rules in `imtp-peak-force.md` and `cmj-jump-height.md`.
- Squat jump protocol: the athlete sinks to a set depth, holds still, then pushes up with no dip. Sheppard and Doyle (2008) used a 90° knee angle and a 3 s hold. Record the depth and the hold time, and keep them the same.
- Squat jump check: look at the force trace just before the push. A drop in force before the push means the athlete dipped. In 125 squat jumps by 30 national team and Olympic athletes, researchers saw a small dip in 69 trials (55.2%). In 43 of the 56 others, force data showed a drop of at least 10%; the abstract says 10% of body mass (Sheppard and Doyle, 2008). Watching the athlete is not enough. Flag every trial with a drop of 10% of body weight or more, the threshold Sheppard and Doyle (2008) used. A stricter rule, such as any drop beyond the quiet period's noise, is a valid choice. Name the rule you used.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with these ratios:

- Dividing a net CMJ force by a gross IMTP force, or the reverse. Use the same definition for both.
- Taking the CMJ peak from the whole jump when the published method uses the propulsion phase only.
- Mixing the CMJ and SJ versions of the DSI in one trend.
- Calling a DSI in a published band a prescription. The bands are study settings.
- Reporting a DSI without the agreement sentence from Ripley et al. (2025).
- Keeping squat jumps with a dip. Check the force trace for every trial.
- Mixing flight time and takeoff velocity heights in the EUR.
- Reading a low EUR as weak eccentric strength.
- Judging a ratio change with the TE of one test only. The ratio carries the error of both.

## Example request

> We test CMJ, squat jump, and IMTP on the same day each block. Can you add the dynamic strength index and the eccentric utilization ratio to my Google Sheet, and tell me which players moved since the last block?

## Check the result

Run these checks:

- Recompute one value by hand: 1800 N / 2600 N = 0.6923. A CMJ height of 0.40 m and an SJ height of 0.36 m give an EUR of 1.1111.
- Confirm both peak forces are gross, or both are net.
- Check any DSI above 1.00. It can be real, since one high DSI group averaged 0.92 ± 0.11 (McMahon et al., 2017), but check the IMTP trials and labels first.
- Confirm the EUR is usually above 1.
- Confirm each ratio uses the same trial rule for both tests, and that the EUR jumps come from the same session.
- Confirm the trial count for each test, and that no SJ trial with a dip was kept without a flag.
- Confirm every DSI has its method, its band source if a band is shown, and the agreement sentence beside it.

## Sources

This file cites these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
- Comfort P, Thomas C, Dos'Santos T, Jones PA, Suchomel TJ, McMahon JJ. Comparison of methods of calculating dynamic strength index. International Journal of Sports Physiology and Performance. 2018;13(3):320-325. https://doi.org/10.1123/ijspp.2017-0255 (abstract, accessed 2026-10-07). Cited as Comfort et al., 2018a.
- Comfort P, Thomas C, Dos'Santos T, Suchomel TJ, Jones PA, McMahon JJ. Changes in dynamic strength index in response to strength training. Sports. 2018;6(4):176. https://doi.org/10.3390/sports6040176 (accessed 2026-10-07). Cited as Comfort et al., 2018b.
- Harman EA, Rosenstein MT, Frykman PN, Rosenstein RM. The effects of arms and countermovement on vertical jumping. Medicine and Science in Sports and Exercise. 1990;22(6):825-833. https://doi.org/10.1249/00005768-199012000-00015 (abstract, accessed 2026-10-07)
- McGuigan MR, Doyle TL, Newton M, Edwards DJ, Nimphius S, Newton RU. Eccentric utilization ratio: effect of sport and phase of training. Journal of Strength and Conditioning Research. 2006;20(4):992-995. https://doi.org/10.1519/R-19165.1 (abstract, accessed 2026-10-07)
- McMahon JJ, Jones PA, Dos'Santos T, Comfort P. Influence of dynamic strength index on countermovement jump force-, power-, velocity-, and displacement-time curves. Sports. 2017;5(4):72. https://doi.org/10.3390/sports5040072 (accessed 2026-10-07)
- Ripley NJ, Fahey J, Guppy S, Comfort P. Comparisons between different methods of calculating dynamic strength index: effect on training recommendations. PLoS ONE. 2025;20(9):e0331519. https://doi.org/10.1371/journal.pone.0331519 (accessed 2026-10-07)
- Sheppard JM, Doyle TL. Increasing compliance to instructions in the squat jump. Journal of Strength and Conditioning Research. 2008;22(2):648-651. https://doi.org/10.1519/JSC.0b013e31816602d4 (abstract, accessed 2026-10-07)
- Thomas C, Jones PA, Comfort P. Reliability of the dynamic strength index in college athletes. International Journal of Sports Physiology and Performance. 2015;10(5):542-545. https://doi.org/10.1123/ijspp.2014-0255 (abstract, accessed 2026-10-07)
