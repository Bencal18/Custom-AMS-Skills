# Eccentric hamstring force

Last checked: 2026-10-02

## What it measures

Eccentric hamstring force is the peak force each leg produces at the ankle while the athlete resists falling forward during the Nordic hamstring exercise. "Eccentric" means the muscle is producing force while it lengthens.

In the Nordic hamstring exercise, the athlete kneels with both ankles held in place and lowers the upper body forward as slowly as possible. A sensor at each ankle records force (Opar et al., 2013; Bourne et al., 2015).

## Formula

Calculate each leg separately. Use these formulas:

```text
peak force, per leg (N)          = highest force on that leg's sensor in the best repetition
relative force, per leg (N/kg)   = peak force / body mass
two-limb average (N)             = (left peak force + right peak force) / 2
between-limb imbalance (%)       = (stronger leg - weaker leg) / stronger leg x 100, with the weaker side named
```

Define every term in the formula:

- `peak force`: the highest force in N from one leg's sensor during one repetition. The best of three repetitions has been used (Bourne et al., 2015). Opar et al. (2015) used the mean of the three peaks.
- `body mass`: the athlete's mass in kg, measured on the test day
- `two-limb average`: the mean of left and right peak force. Some studies report it in N and N/kg (Bourne et al., 2015).
- `stronger leg` and `weaker leg`: the legs with the higher and lower peak force on that day
- `between-limb imbalance`: the percentage by which the weaker leg's peak force is below the stronger leg's. Name the weaker side with every value.

This value equals the size of the signed percentage difference, (right - left) / max(right, left) × 100, in the `limb-symmetry` skill. A positive signed value means the right leg is stronger. The imbalance formula above is one of several.

Injury studies on this test did not use the formula above. They used a left-to-right ratio (Opar et al., 2015; Bourne et al., 2015). Opar et al. (2015) log-transformed the ratio only to calculate group means. Neither paper prints an equation for one athlete. Offer the log ratio, 100 × ln(right / left), as an option, because it gives the same size whichever leg is stronger. Do not say it matches the injury studies.

Other asymmetry formulas give different numbers from the same legs (Bishop et al., 2018). If the `limb-symmetry` skill is installed, use it for the full list of formulas. Never compare an imbalance value with a published value calculated another way.

The value is a force at the ankle in N, not a hamstring muscle force and not a knee torque in N·m. This makes direct comparison with torque from an isokinetic dynamometer, a machine that moves the leg at a fixed speed, difficult (Bourne et al., 2015). The two tests measure different things and do not agree closely (Wiesinger et al., 2020).

Use these spreadsheet formulas, with left peak in `B2`, right peak in `C2`, and body mass in kg in `D2`. Each formula returns a blank when an input it needs is blank:

```text
Relative left:          =IF(OR(B2="",D2=""),"",B2/D2)
Two-limb average:       =IF(OR(B2="",C2=""),"",(B2+C2)/2)
Imbalance (%):          =IF(OR(B2="",C2=""),"",(MAX(B2,C2)-MIN(B2,C2))/MAX(B2,C2)*100)
Weaker side:            =IF(OR(B2="",C2=""),"",IF(B2<C2,"Left",IF(C2<B2,"Right","Equal")))
```

Without the blank check, a blank leg gives an imbalance of 0 and names that leg as weaker, because `MIN` and `MAX` skip blank cells.

### Calculate it in Power BI and Tableau

Each result returns a blank when an input it needs is missing: both legs for the two-limb average, the imbalance, and the weaker side, and the left leg and body mass for relative force. They never read a missing leg as 0 N.

Both versions assume one row per athlete, date, side, and repetition in a `measures` table, with `measure_name` `nordic_peak_force`, `side` `left` or `right`, and `unit` `N`. Body mass is a row with `measure_name` `body_mass` and `unit` `kg` on the same date. Show the results with one athlete and one date per row. Do not put `side` in the visual, or each row holds only one leg.

In Power BI, use these DAX measures. They are measures because each result combines rows for two sides and a body mass row, and no single row holds all three:

```text
Left peak (N) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "nordic_peak_force",
    measures[side] = "left",
    measures[unit] = "N",
    measures[status] = "ok"
)

Right peak (N) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "nordic_peak_force",
    measures[side] = "right",
    measures[unit] = "N",
    measures[status] = "ok"
)

Body mass (kg) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "body_mass",
    measures[unit] = "kg",
    measures[status] = "ok"
)

Relative left (N/kg) =
VAR l = [Left peak (N)]
VAR m = [Body mass (kg)]
RETURN IF ( NOT ISBLANK ( l ) && NOT ISBLANK ( m ) && m > 0, l / m )

Two-limb average (N) =
VAR l = [Left peak (N)]
VAR r = [Right peak (N)]
RETURN IF ( NOT ISBLANK ( l ) && NOT ISBLANK ( r ), ( l + r ) / 2 )

Imbalance (%) =
VAR l = [Left peak (N)]
VAR r = [Right peak (N)]
VAR hi = IF ( l >= r, l, r )
VAR lo = IF ( l >= r, r, l )
RETURN IF ( NOT ISBLANK ( l ) && NOT ISBLANK ( r ) && hi > 0, ( hi - lo ) / hi * 100 )

Weaker side =
VAR l = [Left peak (N)]
VAR r = [Right peak (N)]
RETURN
    IF (
        NOT ISBLANK ( l ) && NOT ISBLANK ( r ),
        IF ( l < r, "Left", IF ( r < l, "Right", "Equal" ) )
    )
```

`MAX` over the repetitions gives the best repetition for each leg. Use `AVERAGE` instead for the mean of repetitions, and name the summary in the report.

In Tableau, put `athlete_id` and `measure_date` on the view, not `side`. Use these aggregate calculations:

```text
Left peak (N):
MAX(IF [measure_name] = "nordic_peak_force" AND [side] = "left" AND [unit] = "N" AND [status] = "ok" THEN [value] END)

Right peak (N):
MAX(IF [measure_name] = "nordic_peak_force" AND [side] = "right" AND [unit] = "N" AND [status] = "ok" THEN [value] END)

Body mass (kg):
MAX(IF [measure_name] = "body_mass" AND [unit] = "kg" AND [status] = "ok" THEN [value] END)

Relative left (N/kg):
IF ISNULL([Left peak (N)]) OR ISNULL([Body mass (kg)]) THEN NULL
ELSEIF [Body mass (kg)] <= 0 THEN NULL
ELSE [Left peak (N)] / [Body mass (kg)]
END

Two-limb average (N):
IF ISNULL([Left peak (N)]) OR ISNULL([Right peak (N)]) THEN NULL
ELSE ([Left peak (N)] + [Right peak (N)]) / 2
END

Imbalance (%):
IF ISNULL([Left peak (N)]) OR ISNULL([Right peak (N)]) THEN NULL
ELSEIF MAX([Left peak (N)], [Right peak (N)]) <= 0 THEN NULL
ELSE (MAX([Left peak (N)], [Right peak (N)]) - MIN([Left peak (N)], [Right peak (N)]))
     / MAX([Left peak (N)], [Right peak (N)]) * 100
END

Weaker side:
IF ISNULL([Left peak (N)]) OR ISNULL([Right peak (N)]) THEN NULL
ELSEIF [Left peak (N)] < [Right peak (N)] THEN "Left"
ELSEIF [Right peak (N)] < [Left peak (N)] THEN "Right"
ELSE "Equal"
END
```

Blanks behave this way in each tool:

- Power BI: DAX `MAX` and `MIN` with two values treat a blank as 0, so `MIN` of a blank and 325 N gives 0. The measures above do not use them for the legs. They test each leg with `ISBLANK` first.
- Power BI: a blank plus a number gives the number, so a plain `( l + r ) / 2` with a missing leg halves the other leg. The `ISBLANK` test stops that.
- Tableau: `MAX(a, b)` with two values returns null if either is null. The `ISNULL` tests still come first, so the reason is explicit.
- Both tools return a blank when both legs are 0 N, where the spreadsheet gives `#DIV/0!`.

## Calculate the metric

Follow these steps to calculate the metric from repetition-level data:

1. Load one row per repetition with `athlete_id`, `test_date`, `side` (left or right), and `peak_force_n`.
2. Check the side labels against the device file, so left and right are not swapped.
3. Flag repetitions that did not reach a clear peak followed by a fast drop in force. That pattern marks the point where the athlete could no longer resist the fall (Bourne et al., 2015).
4. For each athlete, date, and side, keep the highest `peak_force_n` among the valid repetitions: those with `status` `ok` that you did not flag in step 3.
5. Divide each leg's peak by `body_mass_kg` from the same day to get relative force in N/kg.
6. Average the left and right peaks to get the two-limb average.
7. Calculate the imbalance from the left and right peaks.
8. Record which side is weaker.
9. For each earlier test the user cites, subtract the earlier value from the new value for each leg.
10. Compare each change with the noise band, 1.96 × TE × √(1 + 1/n), where n is the number of tests in the baseline mean. Use n = 1 for one earlier test, which gives 1.96 × √2 × TE. See "Judge a change and an imbalance" below.
11. To judge the imbalance, compare the left-right difference in N with the asymmetry band, 1.96 × √(SE_left² + SE_right²). See "Judge a change and an imbalance" below.

## Worked example

| Input | Value |
|---|---|
| Left leg, repetitions 1 to 3 | 310 N, 325 N, 318 N |
| Right leg, repetitions 1 to 3 | 352 N, 360 N, 347 N |
| Body mass on the test day | 82 kg |
| Left leg best at the previous test | 300 N |

Step 1. Best repetition per leg: left = 325 N, right = 360 N.

Step 2. Relative force: left = 325 / 82 = 3.96 N/kg. Right = 360 / 82 = 4.39 N/kg.

Step 3. Two-limb average = (325 + 360) / 2 = 342.5 N, which is 342.5 / 82 = 4.18 N/kg.

Step 4. Imbalance = (360 - 325) / 360 × 100 = 9.72%. The left leg is weaker.

Step 5. Change in the left leg since the previous test = 325 - 300 = 25 N. With TE = 21.7 N, the lowest value Opar et al. (2013) reported, and one earlier test (n = 1), the noise band is 1.96 × 21.7 × √2 = 60.1 N. With TE = 27.5 N, it is 76.2 N. These equal the minimal detectable change values Opar et al. (2013) reported. The 25 N change is inside both bands.

Step 6. Left-right difference = 360 - 325 = 35 N. Assume SE = TE = 21.7 N for each leg. The asymmetry band is 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the stronger leg. The 35 N difference is inside the band. This TE comes from a separate-day retest, so label the band as likely wider than needed for a same-session difference.

Result: left 325 N (3.96 N/kg), right 360 N (4.39 N/kg), two-limb average 342.5 N (4.18 N/kg), and imbalance 9.72% with the left side weaker. Neither the 25 N change nor the 35 N difference can be told apart from measurement noise with these data. This does not show that the legs are equal or that nothing changed. Use your own TE when you have it.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Imbalance formula. With the same legs as the worked example, the formula above gives 9.72%. Dividing by the left leg gives 10.77%. Dividing by the sum of both legs gives 5.11%. The log ratio, 100 × ln(360 / 325), gives 10.23%. The left-to-right ratio is 0.903.
- Noise estimate. The estimate can use the mean of 3 repetitions (317.7 N and 353.0 N) and an assumed pooled squad coefficient of variation of 5% for one repetition. Each leg's SE is then 5% × the leg's mean / √3: 9.17 N and 10.19 N. The asymmetry band shrinks to 26.9 N, and the 35.3 N difference is outside it. The choice of SE decides the answer, so state it.
- Multiplier. Opar et al. (2013) had 30 athletes. Using t with 29 degrees of freedom, 2.045, in place of 1.96 raises the change band from 60.1 N to 62.8 N.
- Best repetition or mean of repetitions. With the mean of repetitions, the legs are 317.7 N and 353.0 N, and the imbalance is 10.01%.
- Body mass. The same 325 N is 4.06 N/kg at 80 kg and 3.96 N/kg at 82 kg.
- Summing legs. Adding both legs gives 685 N. That is not a per-leg value and cannot be compared with per-leg ranges.
- Device. A Nordic device and an isokinetic dynamometer give different values and side-to-side ratios for the same athlete (Wiesinger et al., 2020).
- Repetition quality. Repetitions without a clear peak, or with a broken position, lower or raise the peak.

## Units and typical range

Report peak force in N per leg, relative force in N/kg, and imbalance in % with the weaker side named.

| Population | Typical range | Source |
|---|---|---|
| Recreationally active men with no history of hamstring strain | Left 344.7 ± 61.1 N; right 361.2 ± 65.1 N (mean ± SD) | Opar et al., 2013 |

Test variability in that sample came from 30 men who completed the test on 2 separate occasions. Typical error was 21.7 to 27.5 N, typical error as a coefficient of variation 5.8 to 8.5%, and minimal detectable change at 95% confidence 60.1 to 76.2 N (Opar et al., 2013). Typical error is the SD of one athlete's repeated scores when nothing real changed. Because the retest was on a separate occasion, it counts day-to-day variation as noise, and it is larger than a same-day retest would give. Minimal detectable change is the smallest change larger than that noise with 95% confidence. Measure your own for your setup.

### Judge a change and an imbalance

If the `monitoring-statistics` skill is installed, use it for detail. Follow these rules to judge a change or an imbalance (Hopkins, 2000; Swinton et al., 2018):

- Take TE from a short-term test-retest study in which no true change is expected, with the same device, protocol, and repetition summary (best or mean) as your values. Opar et al. (2013) is a valid TE for their device and sample.
- Noise band for a change against a baseline mean of n tests: 1.96 × TE × √(1 + 1/n). It adds variances. Hopkins (2017) uses the same error for a change from the mean of several tests. With n = 1 it equals the minimal detectable change, 1.96 × √2 × TE.
- The band assumes a constant true score, independent errors, the same TE for every athlete and value, and a known TE. Error alone gives a change smaller than the band about 95 percent of the time. When the assumptions fail, the real false-flag rate can be higher or lower.
- When TE comes from few athletes, use t with the degrees of freedom of the TE study (athletes − 1 for two trials) in place of 1.96.
- A change is clearly larger than the smallest worthwhile change (SWC) only when the change minus the band is still beyond the SWC (Swinton et al., 2018). Otherwise, a change beyond the band reads: "larger than measurement error; may or may not be worthwhile".
- Imbalance: treat the left-right difference as larger than noise only when it exceeds 1.96 × √(SE_left² + SE_right²). Use SE = TE for single or best repetitions. For a mean of k repetitions, use SE = pooled squad coefficient of variation × the leg's value / √k. Take the TE or coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own repetitions or from the same repetitions you are judging.
- For a left-right difference from one session, use a within-session TE when such a study exists. If only a separate-day TE exists, such as Opar et al. (2013), use it, and label the band as likely wider than needed. Typical error depends on the time between tests (Hopkins, 2011). Day-to-day changes that affect both legs alike cancel out of a same-session difference. In 22 collegiate basketball players, across 16 force measures from a two-plate CMJ with and without arm swing, within-session TE was a median 0.90 times the separate-day TE, with a range of 0.77 to 0.99 (Heishman et al., 2019b).
- When the difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal."

Side-to-side strength ratios from this test had low reliability (Wiesinger et al., 2020). Treat a single imbalance value with caution.

## Data you need

Collect this data:

- Source: a Nordic hamstring device with a separate force sensor for each ankle, or a per-leg export from one
- Sampling: per-leg force over each repetition. One study recorded at 100 Hz (Bourne et al., 2015).
- Minimum data: a warm-up set, then three maximal repetitions (Bourne et al., 2015). Body mass from the same day for relative force.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Calling the value hamstring muscle force or knee torque. It is force at the ankle in N.
- Calculating knee torque or muscle force from ankle force. Do not calculate it. Report force in N. If the device exports a torque, report it as given, labeled as the device's value, and say that it depends on how the knee position is set.
- Summing or averaging both legs and then treating the result as one leg
- Swapping left and right labels between the device and the spreadsheet
- Calculating imbalance with one formula and comparing it with a published value that used another
- Reporting an imbalance percentage without naming the weaker side
- Using a body mass from another day for relative force
- Treating a change inside the noise band as real, or judging a change against 1 × TE. A change of 1 × TE is well inside the 95% band.
- Comparing values across different devices or with isokinetic results
- Using published injury studies to predict injury for one athlete. Those studies report group-level associations in specific cohorts, and their findings on imbalance disagree (Opar et al., 2015; Bourne et al., 2015). Report the numbers and leave interpretation to the practitioner.
- Quoting injury-study cut-offs, such as force or imbalance cut-offs from Opar et al. (2015) or Bourne et al. (2015), as targets or flags. Do not quote them for one athlete. The cut-offs did not replicate. Later cohorts found a different force cut-off, 337 N in soccer (Timmins et al., 2016), or no link with Nordic strength (van Dyk et al., 2017). A meta-analysis of six cohorts (1100 players) found no difference in pre-season Nordic strength or imbalance between players who later had a hamstring injury and those who did not (Opar et al., 2021).
- Calling low Nordic strength a training target. Training choices stay with the coach.
- Analyzing a repetition with noted pain. These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.

## Example request

> I've got Nordic results for the squad from two test days, left and right peak force for three reps each. Can you build a sheet that shows each player's best rep per leg, force per kg, the left-right difference, and whether anything changed?

## Check the result

Run these checks:

- Recompute one athlete by hand. Left 325 N and right 360 N give an imbalance of 9.72% with the left side weaker.
- Check that every relative value has units of N/kg and sits near the absolute value divided by body mass.
- Check that each athlete has a value for both legs on each date, and that the repetition count matches the input.

## Sources

This file cites these sources:

- Opar DA, Piatkowski T, Williams MD, Shield AJ. A novel device using the Nordic hamstring exercise to assess eccentric knee flexor strength: a reliability and retrospective injury study. Journal of Orthopaedic and Sports Physical Therapy. 2013;43(9):636-640. https://doi.org/10.2519/jospt.2013.4837
- Bourne MN, Opar DA, Williams MD, Shield AJ. Eccentric knee flexor strength and risk of hamstring injuries in rugby union: a prospective study. American Journal of Sports Medicine. 2015;43(11):2663-2670. https://doi.org/10.1177/0363546515599633
- Opar DA, Williams MD, Timmins RG, Hickey J, Duhig SJ, Shield AJ. Eccentric hamstring strength and hamstring injury risk in Australian footballers. Medicine and Science in Sports and Exercise. 2015;47(4):857-865. https://doi.org/10.1249/MSS.0000000000000465
- Wiesinger HP, Gressenbauer C, Kösters A, Scharinger M, Müller E. Device and method matter: a critical evaluation of eccentric hamstring muscle strength assessments. Scandinavian Journal of Medicine and Science in Sports. 2020;30(2):217-226. https://doi.org/10.1111/sms.13569
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02). The skills use only its error formula, not its magnitude-based inference.
- Bishop C, Read P, Lake J, Chavda S, Turner A. Interlimb asymmetries: understanding how to calculate differences from bilateral and unilateral tests. Strength and Conditioning Journal. 2018;40(4):1-6. https://doi.org/10.1519/SSC.0000000000000371
- Opar DA, Timmins RG, Behan FP, Hickey JT, van Dyk N, Price K, Maniar N. Is pre-season eccentric strength testing during the Nordic hamstring exercise associated with future hamstring strain injury? A systematic review and meta-analysis. Sports Medicine. 2021;51(9):1935-1945. https://doi.org/10.1007/s40279-021-01474-1 (accessed 2026-10-05). Read in abstract form only.
- Heishman A, Daub B, Miller R, Brown B, Freitas E, Bemben M. Countermovement jump inter-limb asymmetries in collegiate basketball players. Sports. 2019;7(5):103. https://doi.org/10.3390/sports7050103 (accessed 2026-10-05). Cited as Heishman et al., 2019b, to keep it apart from the 2019a paper in `rsi-modified.md`. The 0.90 ratio and its range were calculated from the typical errors in the paper's within-session and separate-day reliability tables.
- Hopkins WG. A new view of statistics: measures of reliability. Sportscience. Last updated 2011-10-04. https://www.sportsci.org/resource/stats/precision.html (accessed 2026-10-05). No DOI.
- Timmins RG, Bourne MN, Shield AJ, Williams MD, Lorenzen C, Opar DA. Short biceps femoris fascicles and eccentric knee flexor weakness increase the risk of hamstring injury in elite football (soccer): a prospective cohort study. British Journal of Sports Medicine. 2016;50(24):1524-1535. https://doi.org/10.1136/bjsports-2015-095362 (accessed 2026-10-02)
- van Dyk N, Bahr R, Burnett AF, Whiteley R, Bakken A, Mosler A, Farooq A, Witvrouw E. A comprehensive strength testing protocol offers no clinical value in predicting risk of hamstring injury: a prospective cohort study of 413 professional football players. British Journal of Sports Medicine. 2017;51(23):1695-1702. https://doi.org/10.1136/bjsports-2017-097754 (accessed 2026-10-02)
