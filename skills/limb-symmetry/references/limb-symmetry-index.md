# Limb symmetry index

Last checked: 2026-10-02

## What it measures

A limb symmetry index compares one limb's test result with the other limb's result, as a percentage.

The name covers many different formulas. Studies use the same name for formulas that give different numbers, and different names for the same formula (Bishop et al., 2016; Parkinson et al., 2021). Always name the formula, not only "LSI" or "asymmetry".

## Formula

These are the formula variants you will meet most often. Each one answers a slightly different question:

```text
LSI (symmetry, %)                       = involved limb / uninvolved limb x 100
Percentage difference, signed (%)       = (right - left) / max(right, left) x 100
Dominant-referenced asymmetry (%)       = (dominant - nondominant) / dominant x 100
Bilateral asymmetry index, BAI-1 (%)    = (dominant - nondominant) / (dominant + nondominant) x 100
Mean-referenced asymmetry index (%)     = (dominant - nondominant) / ((dominant + nondominant) / 2) x 100
Log ratio (%)                           = 100 x ln(right / left)
Symmetry angle (%)                      = (45 - arctan(left / right) in degrees) / 90 x 100
```

Define every term in the formula:

- `involved limb`: the injured or operated limb, in rehab settings
- `uninvolved limb`: the other limb, in rehab settings
- `dominant limb`: the limb the athlete prefers, often the kicking leg. Define it once per athlete and do not change it.
- `right`, `left`: the athlete's own right and left
- `max(right, left)`: the larger of the two values on that day
- `reference limb`: the limb in the denominator of a formula. The denominator is the bottom of the fraction.

Use each variant this way:

- LSI expresses the involved limb as a percentage of the uninvolved limb. 100% means equal. It is the most used index in the literature (Parkinson et al., 2021). Use it only when the user works in a rehab setting and names the involved limb.
- Percentage difference divides by the larger value, so it gives the same size of result whichever limb is stronger. Bishop et al. (2018) recommend it for unilateral tests, where each limb is tested on its own, such as single-leg jumps. The signed version is positive when the right limb is larger and negative when the left limb is larger (Bishop et al., 2021).
- Dominant-referenced asymmetry divides by the dominant limb. It gives a larger size of result when the dominant limb is the weaker one. Use it only when the user asks for it.
- BAI-1 divides by the sum of both limbs. Bishop et al. (2018) recommend it for bilateral tests, where both limbs push at the same time, such as a two-plate CMJ, because each limb's force is part of the total. It gives smaller values than the other formulas (Parkinson et al., 2021). BAI-1 needs a dominant limb. When the user names none, calculate (right - left) / (right + left) × 100, so the sign matches the signed percentage difference, and say so.
- The mean-referenced asymmetry index divides by the mean of both limbs. Bishop et al. (2018) list the same calculation under three names: LSI-3, the asymmetry index, and the bilateral asymmetry index 2 (BAI-2), 2 × (D - ND) / (D + ND) × 100. The name "symmetry index" is also used for other formulas, so do not rely on the name (Parkinson et al., 2021).
- The log ratio is the natural log of right divided by left, × 100. It changes sign, but not size, when you swap the limbs, so it gives the same size whichever limb is stronger. That is the reason to offer it. It does not match the published Nordic studies. Opar et al. (2015) used a left-to-right ratio and log-transformed it only to calculate group means, not a value for each athlete.
- The symmetry angle needs no reference limb and gives small values (Zifchock et al., 2008; Bishop et al., 2016). Use it only when both values are above zero. Then the result stays between -50% and 50%. Do not calculate it for zero or negative values.

### The reference-limb rule

Choose the reference limb before you calculate, and follow these rules:

- Name the reference limb in every result, for example "LSI, uninvolved limb as reference" or "percentage difference, larger limb as reference".
- Keep the same reference limb definition across every session for that athlete.
- Report both raw limb values next to the percentage.
- When the reference limb is not the stronger limb, formulas that divide by the reference limb give a different size of result. Only formulas that do not depend on which limb is stronger keep the same size either way: percentage difference against the larger limb, BAI-1, the mean-referenced asymmetry index, the log ratio, and the symmetry angle. Case B below shows this for BAI-1 and the mean-referenced index.
- Never infer the involved limb from the data, for example by assuming the weaker limb is the injured one. If the user does not name the involved limb, do not calculate an LSI.
- An LSI can look better because the uninvolved limb got weaker, not because the involved limb got stronger. After ACL reconstruction, LSIs often overestimated knee function compared with an index that used the uninvolved limb's values from before surgery (Wellsandt et al., 2017). Track each limb's own value over time as well as the index.

### Why the denominator changes the number

The same difference divided by a larger number gives a smaller percentage. With 25 cm and 20 cm, the difference is 5 cm in every formula. Divided by 25 it is 20.00%. Divided by 20 it is 25.00%. Divided by the sum, 45, it is 11.11%. Divided by the mean, 22.5, it is 22.22%.

When both values are close to zero, a tiny difference becomes a huge percentage. Symmetry indexes in normal walking ranged up to more than 13,000% for variables near zero (Herzog et al., 1989).

Use these spreadsheet formulas, with the right value in `B2`, the left value in `C2`, the involved limb value in `D2`, and the uninvolved limb value in `E2`. Each formula returns a blank when a limb value it needs is blank:

```text
LSI:                        =IF(OR(D2="",E2=""),"",D2/E2*100)
Percentage difference:      =IF(OR(B2="",C2=""),"",(B2-C2)/MAX(B2,C2)*100)
BAI-1 (right dominant):     =IF(OR(B2="",C2=""),"",(B2-C2)/(B2+C2)*100)
Log ratio:                  =IF(OR(B2="",C2=""),"",100*LN(B2/C2))
Symmetry angle:             =IF(AND(B2>0,C2>0),(45-DEGREES(ATAN(C2/B2)))/90*100,"")
```

When both limb values are present, the percentage difference formula above gives the same result as the published spreadsheet version, `((100/MAX)*MIN*-1+100)*IF(left<right,1,-1)` (Bishop et al., 2021). When one limb is blank, the published version returns 0, because `MIN` and `MAX` skip blank cells. Add the same blank check before you use it.

Use this Python sketch to return every variant for one pair of values:

```python
import math

def symmetry_variants(right, left, dominant="right", involved="left"):
    d, nd = (right, left) if dominant == "right" else (left, right)
    inv, uninv = (left, right) if involved == "left" else (right, left)
    return {
        "lsi_involved_over_uninvolved_pct": inv / uninv * 100,
        "pct_difference_signed_right_positive": (right - left) / max(right, left) * 100,
        "dominant_referenced_pct": (d - nd) / d * 100,
        "bai1_pct": (d - nd) / (d + nd) * 100,
        "mean_referenced_asymmetry_pct": (d - nd) / ((d + nd) / 2) * 100,
        "log_ratio_pct": 100 * math.log(right / left) if right > 0 and left > 0 else None,
        "symmetry_angle_pct": (45 - math.degrees(math.atan(left / right))) / 90 * 100
        if right > 0 and left > 0 else None,  # undefined for zero or negative values
    }
```

### Calculate it in Power BI and Tableau

Each returns a blank when a limb value it needs is missing. The log ratio and the symmetry angle return a blank unless both values are above zero. The LSI returns a blank unless the user named the involved limb.

Both versions assume one row per athlete, date, test, side, and trial in a `measures` table, with `side` `left` or `right`. They use the best trial for each limb. Use the mean of trials instead if that is the user's summary, and use the same summary for both limbs. The involved limb comes from a column `involved_side` in the `athletes` table, `left` or `right`, entered by the user. Never infer it from the data.

Show the results with one athlete, one date, and one measure per row. Do not put `side` in the visual.

In Power BI, use these DAX measures. They are measures because each result combines a left row and a right row:

```text
Right value =
CALCULATE ( MAX ( measures[value] ), measures[side] = "right", measures[status] = "ok" )

Left value =
CALCULATE ( MAX ( measures[value] ), measures[side] = "left", measures[status] = "ok" )

LSI, involved over uninvolved (%) =
VAR inv = SELECTEDVALUE ( athletes[involved_side] )
VAR r = [Right value]
VAR l = [Left value]
VAR i = SWITCH ( inv, "left", l, "right", r )
VAR u = SWITCH ( inv, "left", r, "right", l )
RETURN IF ( NOT ISBLANK ( i ) && NOT ISBLANK ( u ) && u > 0, i / u * 100 )

Percentage difference, signed (%) =
VAR r = [Right value]
VAR l = [Left value]
VAR hi = IF ( r >= l, r, l )
RETURN IF ( NOT ISBLANK ( r ) && NOT ISBLANK ( l ) && hi > 0, ( r - l ) / hi * 100 )

BAI-1, right dominant (%) =
VAR r = [Right value]
VAR l = [Left value]
RETURN IF ( NOT ISBLANK ( r ) && NOT ISBLANK ( l ) && r + l <> 0, ( r - l ) / ( r + l ) * 100 )

Log ratio (%) =
VAR r = [Right value]
VAR l = [Left value]
RETURN IF ( NOT ISBLANK ( r ) && NOT ISBLANK ( l ) && r > 0 && l > 0, 100 * LN ( r / l ) )

Symmetry angle (%) =
VAR r = [Right value]
VAR l = [Left value]
RETURN
    IF (
        NOT ISBLANK ( r ) && NOT ISBLANK ( l ) && r > 0 && l > 0,
        ( 45 - DEGREES ( ATAN ( l / r ) ) ) / 90 * 100
    )
```

Use `Percentage difference, signed (%)` wherever the published Bishop et al. (2021) spreadsheet form is asked for. It gives the same result and keeps a missing limb blank.

In Tableau, put `athlete_id`, `measure_date`, and `measure_name` on the view, not `side`. Use these aggregate calculations:

```text
Right value:
MAX(IF [side] = "right" AND [status] = "ok" THEN [value] END)

Left value:
MAX(IF [side] = "left" AND [status] = "ok" THEN [value] END)

LSI, involved over uninvolved (%):
IF ATTR([involved_side]) = "left" AND [Right value] > 0 THEN [Left value] / [Right value] * 100
ELSEIF ATTR([involved_side]) = "right" AND [Left value] > 0 THEN [Right value] / [Left value] * 100
END

Percentage difference, signed (%):
IF ISNULL([Right value]) OR ISNULL([Left value]) THEN NULL
ELSEIF MAX([Right value], [Left value]) <= 0 THEN NULL
ELSE ([Right value] - [Left value]) / MAX([Right value], [Left value]) * 100
END

BAI-1, right dominant (%):
IF ISNULL([Right value]) OR ISNULL([Left value]) THEN NULL
ELSEIF [Right value] + [Left value] = 0 THEN NULL
ELSE ([Right value] - [Left value]) / ([Right value] + [Left value]) * 100
END

Log ratio (%):
IF [Right value] > 0 AND [Left value] > 0 THEN 100 * LN([Right value] / [Left value]) END

Symmetry angle (%):
IF [Right value] > 0 AND [Left value] > 0
THEN (45 - DEGREES(ATAN([Left value] / [Right value]))) / 90 * 100
END
```

Blanks behave this way in each tool:

- Power BI: DAX `MAX` and `MIN` with two values treat a blank as 0. The measures above do not use them on the limbs. They test each limb with `ISBLANK` first.
- Power BI: the reference page for `LN` does not say what happens at 0 or below. The `> 0` tests stop that case before `LN` runs.
- Tableau: `LN` returns null for 0 or a negative number. A null limb makes each `> 0` test null, and an `IF` with no `ELSE` returns null.
- Tableau: an athlete with no `involved_side` gets a null LSI, because neither test is true.

## Calculate the metric

Follow these steps to calculate a limb symmetry value from raw inputs:

1. Load one row per limb per trial with `athlete_id`, `test_date`, `test_name`, `side` (left or right), and the measure with its unit, such as `jump_height_m` or `peak_force_n`.
2. Confirm whether the test is unilateral (each limb tested on its own) or bilateral (both limbs at once, one value per limb).
3. Confirm the side labels against the device file, so left and right are not swapped.
4. Choose one trial summary, the best trial or the mean of trials, and use it for both limbs.
5. Record the reference limb definition for each athlete: involved and uninvolved, dominant and nondominant, or larger value.
6. Choose the formula. Use the one the user names.
7. If the user names none, use percentage difference for unilateral tests and BAI-1 for bilateral tests (Bishop et al., 2018), and say so.
8. For the Nordic hamstring test, a two-leg task, use percentage difference against the stronger leg, because Nordic studies express imbalance on a one-leg scale (Opar et al., 2015; Bourne et al., 2015).
9. Offer the log ratio as an option, because it gives the same size whichever leg is stronger. Do not say it matches the Nordic studies.
10. Calculate the value and its sign.
11. State which side is larger.
12. Get a standard error (SE) for each limb's value, in the units of the measure.
13. Use the test's typical error (TE) when you compare single or best trials. TE is the SD of one athlete's repeated scores when nothing real changed, from a short-term test-retest study in which no true change is expected (Hopkins, 2000).
14. For a mean of k trials, use a pooled squad coefficient of variation × the limb's value / √k.
15. Take the TE or coefficient of variation from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own trials or from the same trials you are judging.
16. For a left-right difference from one session, use a within-session TE when such a study exists. If only a separate-day TE exists, use it, and label the band as likely wider than needed. See "Retest interval of the TE" in "What changes the number".
17. State the SE, its source, and its retest interval: the same session or separate days.
18. Calculate the noise band for the left-right difference: 1.96 × √(SE_left² + SE_right²). When the TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study, athletes − 1 for two trials.
19. Compare the difference between the raw limb values, in units, with the band. Use this one rule whatever formula you report.
20. If the difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal or that the athlete has recovered."
21. Report the raw values for both limbs, the formula, the reference limb, the result, the SE and its source, and the band.
22. For a bilateral test, add the device's own asymmetry formula next to BAI-1 only where the device documents it. VALD ForceDecks documents (left − right) / max(left, right) × 100 in its Technical Glossary V2.0. Recompute it from the left and right values, never from the vendor column. Label it with the device name and the larger side. Hawkin Dynamics and the VALD NordBord app do not publish their formulas, so say so and show no device value.

## Worked example

This example uses one pair of values and runs every formula variant on it. It reproduces the example in Bishop et al. (2016).

| Input | Value |
|---|---|
| Right limb | 25 cm |
| Left limb | 20 cm |

Case A: the right limb is dominant, and the left limb is involved.

| Formula | Calculation | Result |
|---|---|---|
| LSI, involved / uninvolved × 100 | 20 / 25 × 100 | 80.00% symmetry |
| Percentage difference, (right - left) / max × 100 | 5 / 25 × 100 | 20.00% |
| Dominant-referenced, (D - ND) / D × 100 | 5 / 25 × 100 | 20.00% |
| BAI-1, (D - ND) / (D + ND) × 100 | 5 / 45 × 100 | 11.11% |
| Mean-referenced asymmetry index, (D - ND) / mean × 100 | 5 / 22.5 × 100 | 22.22% |
| Symmetry angle | (45 - 38.66) / 90 × 100 | 7.04% |

The asymmetry formulas range from 7.04% to 22.22% on the same data. That is a spread of 15.18 percentage points, and the largest is 3.15 times the smallest.

Case B: same numbers, but the left limb is dominant, so the dominant limb is the weaker one.

| Formula | Result |
|---|---|
| LSI, involved (left) / uninvolved (right) × 100 | 80.00% symmetry |
| Percentage difference, signed | 20.00% (right larger) |
| Dominant-referenced | -25.00% |
| BAI-1 | -11.11% |
| Mean-referenced asymmetry index | -22.22% |
| Symmetry angle | 7.04% |

In this case, the asymmetry formulas range from 7.04% to 25.00% in size, a spread of 17.96 percentage points. The largest is 3.55 times the smallest. Only the reference limb changed.

Case C: same numbers, but the right limb is involved, so the involved limb is the stronger one. LSI becomes 125.00%.

Result: one pair of values gave 7.04%, 11.11%, 20.00%, 22.22%, 25.00%, 80.00%, and 125.00%, depending on the formula and reference limb. A percentage without its formula and reference limb cannot be read. The log ratio gives 22.31%, and -22.31% with the limbs swapped.

### Worked example: the noise band

This example uses Nordic test values, left 325 N and right 360 N, best repetition per leg.

| Input | Value |
|---|---|
| Left-right difference | 360 - 325 = 35 N |
| SE per leg, option A | 21.7 N, the lowest typical error Opar et al. (2013) reported, from a retest on a separate occasion |
| SE per leg, option B | Mean of 3 repetitions (317.7 N and 353.0 N) with an assumed pooled squad coefficient of variation of 5%: 5% × 317.7 / √3 = 9.17 N and 5% × 353.0 / √3 = 10.19 N |

Option A: band = 1.96 × √(21.7² + 21.7²) = 60.1 N, which is 16.7% of the larger leg. The 35 N difference is inside the band, so the difference cannot be told apart from measurement noise with these data. This TE comes from a separate-day retest, so label the band as likely wider than needed for a same-session difference.

Option B: band = 1.96 × √(9.17² + 10.19²) = 26.9 N. The mean-of-3 difference, 35.3 N, is outside the band.

The SE decides the answer. Always state it and its source. For the same legs, the percentage difference is 9.72%, the log ratio is 10.23%, and BAI-1 is 5.11%.

## What changes the number

These choices change the result even when the athlete has not changed:

- Formula. In the worked example, the same limbs give asymmetry values from 7.04% to 25.00%.
- Reference limb. Changing the dominant limb from right to left changes the dominant-referenced value from 20.00% to -25.00%.
- Denominator. Dividing by the larger limb, the smaller limb, the sum, or the mean gives 20.00%, 25.00%, 11.11%, or 22.22% for the same 5 cm difference.
- Symmetry or asymmetry. LSI reports symmetry, where 100% means equal. The other formulas report asymmetry, where 0% means equal. An 80% LSI and a 20% asymmetry describe the same data.
- Values near zero. Small absolute values give huge percentages (Herzog et al., 1989).
- Test and metric. The size and direction of asymmetry change between tests and metrics for the same athlete. Asymmetry rarely favored the same limb across tests (Bishop et al., 2021).
- Trial selection. Best trial and mean of trials give different values.
- Intra-limb variability. A between-limb difference can come from trial-to-trial noise within each limb (Exell et al., 2012).
- Retest interval of the TE. Typical error depends on the time between tests (Hopkins, 2011). A separate-day TE includes day-to-day changes. Changes that affect both limbs alike cancel out of a same-session left-right difference, so a separate-day TE gives a wider band than needed. In 22 collegiate basketball players, across 16 force measures from a two-plate CMJ with and without arm swing, within-session TE was a median 0.90 times the separate-day TE, with a range of 0.77 to 0.99 (Heishman et al., 2019).
- Vendor formula and sign. A device export may calculate asymmetry with its own formula and sign. The VALD ForceDecks Technical Glossary V2.0 uses (left - right) / max(left, right) × 100, where a positive value means the left limb is larger. That is the opposite of the signed percentage difference in this file. Hawkin Dynamics and the VALD NordBord app do not publish their formulas.
- Reading vendor values. Never read the sign of a vendor value. Always recompute from the left and right values. See the device file.

## Units and typical range

Report every value in % with the formula name, the reference limb, and the larger side.

| Population | Typical range | Source |
|---|---|---|
| Male soccer players (n = 313), bilateral jump force test, (stronger - weaker) / stronger × 100, given a positive sign when the right leg is stronger | 2.5th to 97.5th percentile of that sample: -15% to 15% | Impellizzeri et al., 2007 |
| Recreational sport athletes (n = 28), unilateral isometric squat and single-leg jumps, percentage difference | Mean asymmetry 5.3% or less; some individuals 20 to 30% | Bishop et al., 2021 |

These ranges describe the samples studied. Use them to check that data are plausible. They are not cut-offs.

Published values on bilateral tests are not always BAI-1. Impellizzeri et al. (2007) used (stronger - weaker) / stronger × 100 on a bilateral jump. Check the formula before you compare.

Thresholds depend on context. Many studies apply a fixed threshold, most often between 10 and 15%, to label asymmetry as abnormal. That threshold was not always supported by appropriate evidence (Parkinson et al., 2021). Prospective evidence that a fixed threshold marks higher injury risk is scarce (Bishop et al., 2018). Do not use any of these figures as a cut-off.

A threshold only means something with the formula, test, metric, and population it came from. A between-limb difference can come from noise within each limb (Exell et al., 2012), so compare asymmetry with the test's variability (Bishop et al., 2018). Use the noise band in "Calculate the metric" as the default rule. Never apply a threshold as a pass or fail, a clearance, or a return-to-sport rule.

Optional lenient screen: Bishop et al. (2021) computed group coefficients of variation for each test, metric, and limb from three trials within a session, and drew one line per metric at the largest of those values. Use this line only if the user asks, cite it, and call it a lenient screen.

It flags more differences than the noise band, because it has no allowance for error in both limbs. With single trials and a coefficient of variation of 5%, the noise band on the difference is about 1.96 × √2 × 5% = 13.9% of the limb value, while the screen's line is 5%. Never compute the coefficient of variation from one athlete's own three trials. An estimate from three values is unstable, so a symmetric athlete is often flagged by chance.

If the user asks about a 90% LSI or any other return-to-sport criterion, state that it belongs to a clinician-run test battery. An LSI alone can overestimate function: after ACL reconstruction, 57.1% of patients reached 90% LSIs on all tests, but only 28.6% reached 90% of estimated pre-injury capacity (Wellsandt et al., 2017). The 90% cut-off rests on consensus and expert opinion, not on outcome data. In 233 athletes, LSI cut-offs did not separate those who returned without a second ACL injury from those who did not (Simonsson et al., 2025). Test batteries have not settled it either. In a meta-analysis, only 23% of patients passed a return-to-sport test battery. Passing lowered the risk of graft rupture but raised the risk of an ACL injury in the other knee, and did not lower the risk of any second ACL injury (Webster and Hewett, 2019). Do not say whether the athlete meets the criterion.

## Data you need

Collect this data:

- Source: any test that gives one value per limb, such as single-leg jumps, a two-plate bilateral jump, an isometric test per limb, or a Nordic test per leg
- Sampling: the sampling needs of the underlying test. See the metric file for that test.
- Minimum data: about three trials per limb (Bishop et al., 2018). You also need a typical error or pooled squad coefficient of variation for the test, from a squad reliability study, or from a published reliability study of the same test, device, and population, and a reference limb definition for each athlete. For any LSI, the user must name the involved limb.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Reporting "asymmetry %" without naming the formula
- Dividing by the wrong limb, such as the involved limb instead of the uninvolved limb in an LSI
- Letting the reference limb switch between sessions because the stronger limb changed
- Mixing LSI (symmetry, 100% = equal) with asymmetry formulas (0% = equal) in one column or trend
- Comparing a value with a threshold or study that used another formula, test, or metric
- Using absolute values and dropping the sign, so the reader cannot tell which side is larger
- Using one trial for one limb and the mean of trials for the other
- Swapping left and right labels between the device and the spreadsheet
- Calculating a percentage for values near zero
- Treating a difference inside the noise band as real
- Judging asymmetry against a coefficient of variation from one athlete's own three trials
- Writing "symmetric" or "recovered" when a difference is inside the noise band
- Reading the sign of a vendor asymmetry value instead of recomputing it from left and right
- Guessing the involved limb from which limb is weaker
- Calling an athlete "at risk", "cleared", or "ready" based on an index

## Example request

> I have single-leg jump heights for my athletes, left and right, three trials each. Can you give me a symmetry column in Excel and tell me which formula you used?

## Check the result

Run these checks:

- Recompute one athlete by hand with the named formula. With right 25 cm and left 20 cm, percentage difference is 20.00% and BAI-1 is 11.11%.
- Check the sign of values you calculated. A positive signed percentage difference means the right limb is larger. This does not apply to vendor values, which you recompute.
- Check that an LSI above 100% only appears when the involved limb has the larger value.
- Check that every row shows both raw limb values, the formula, and the reference limb.

## Sources

This file cites these sources:

- Bishop C, Read P, Chavda S, Turner A. Asymmetries of the lower limb: the calculation conundrum in strength training and conditioning. Strength and Conditioning Journal. 2016;38(6):27-32. https://doi.org/10.1519/SSC.0000000000000264
- Bishop C, Read P, Lake J, Chavda S, Turner A. Interlimb asymmetries: understanding how to calculate differences from bilateral and unilateral tests. Strength and Conditioning Journal. 2018;40(4):1-6. https://doi.org/10.1519/SSC.0000000000000371
- Bishop C, Lake J, Loturco I, Papadopoulos K, Turner A, Read P. Interlimb asymmetries: the need for an individual approach to data analysis. Journal of Strength and Conditioning Research. 2021;35(3):695-701. https://doi.org/10.1519/JSC.0000000000002729
- Parkinson AO, Apps CL, Morris JG, Barnett CT, Lewis MGC. The calculation, thresholds and reporting of inter-limb strength asymmetry: a systematic review. Journal of Sports Science and Medicine. 2021;20(4):594-617. https://doi.org/10.52082/jssm.2021.594
- Zifchock RA, Davis I, Higginson J, Royer T. The symmetry angle: a novel, robust method of quantifying asymmetry. Gait and Posture. 2008;27(4):622-627. https://doi.org/10.1016/j.gaitpost.2007.08.006
- Bourne MN, Opar DA, Williams MD, Shield AJ. Eccentric knee flexor strength and risk of hamstring injuries in rugby union: a prospective study. American Journal of Sports Medicine. 2015;43(11):2663-2670. https://doi.org/10.1177/0363546515599633
- Opar DA, Williams MD, Timmins RG, Hickey J, Duhig SJ, Shield AJ. Eccentric hamstring strength and hamstring injury risk in Australian footballers. Medicine and Science in Sports and Exercise. 2015;47(4):857-865. https://doi.org/10.1249/MSS.0000000000000465 (accessed 2026-10-02)
- Opar DA, Piatkowski T, Williams MD, Shield AJ. A novel device using the Nordic hamstring exercise to assess eccentric knee flexor strength: a reliability and retrospective injury study. Journal of Orthopaedic and Sports Physical Therapy. 2013;43(9):636-640. https://doi.org/10.2519/jospt.2013.4837
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Hopkins WG. A new view of statistics: measures of reliability. Sportscience. Last updated 2011-10-04. https://www.sportsci.org/resource/stats/precision.html (accessed 2026-10-05). No DOI.
- Heishman A, Daub B, Miller R, Brown B, Freitas E, Bemben M. Countermovement jump inter-limb asymmetries in collegiate basketball players. Sports. 2019;7(5):103. https://doi.org/10.3390/sports7050103 (accessed 2026-10-05). The 0.90 ratio and its range were calculated from the typical errors in the paper's within-session and separate-day reliability tables.
- Hickey JT, Timmins RG, Maniar N, Rio E, Hickey PF, Pitcher CA, Williams MD, Opar DA. Pain-free versus pain-threshold rehabilitation following acute hamstring strain injury: a randomized controlled trial. Journal of Orthopaedic and Sports Physical Therapy. 2020;50(2):91-103. https://doi.org/10.2519/jospt.2020.8895 (accessed 2026-10-05). Read in abstract form only. Cited in `SKILL.md`: one group did its rehabilitation within pain-threshold limits, so painful reps can be part of a planned protocol.
- VALD. ForceDecks Technical Glossary V2.0. March 2024. https://support.vald.com/hc/en-au/article_attachments/31552911571353 (accessed 2026-10-02).
- Exell TA, Irwin G, Gittoes MJR, Kerwin DG. Implications of intra-limb variability on asymmetry analyses. Journal of Sports Sciences. 2012;30(4):403-409. https://doi.org/10.1080/02640414.2011.647047
- Herzog W, Nigg BM, Read LJ, Olsson E. Asymmetries in ground reaction force patterns in normal human gait. Medicine and Science in Sports and Exercise. 1989;21(1):110-114. https://doi.org/10.1249/00005768-198902000-00020
- Impellizzeri FM, Rampinini E, Maffiuletti N, Marcora SM. A vertical jump force test for assessing bilateral strength asymmetry in athletes. Medicine and Science in Sports and Exercise. 2007;39(11):2044-2050. https://doi.org/10.1249/mss.0b013e31814fb55c
- Wellsandt E, Failla MJ, Snyder-Mackler L. Limb symmetry indexes can overestimate knee function after anterior cruciate ligament injury. Journal of Orthopaedic and Sports Physical Therapy. 2017;47(5):334-338. https://doi.org/10.2519/jospt.2017.7285
- Simonsson R, Sundberg A, Piussi R, Högberg J, Senorski C, Thomeé R, Samuelsson K, Della Villa F, Hamrin Senorski E. Questioning the rules of engagement: a critical analysis of the use of limb symmetry index for safe return to sport after anterior cruciate ligament reconstruction. British Journal of Sports Medicine. 2025;59(6):376-384. https://doi.org/10.1136/bjsports-2024-108079 (accessed 2026-10-02)
- Webster KE, Hewett TE. What is the evidence for and validity of return-to-sport testing after anterior cruciate ligament reconstruction surgery? A systematic review and meta-analysis. Sports Medicine. 2019;49(6):917-929. https://doi.org/10.1007/s40279-019-01093-x (accessed 2026-10-02)
