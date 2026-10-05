# Readiness composites

Last checked: 2026-10-05

## What it measures

A readiness composite combines several monitoring measures, such as wellness answers and test results, into one number that shows how far an athlete is from their own usual values overall. Label the output "composite distance from baseline", not "readiness score".

A composite measures nothing directly. It is a weighted summary of its inputs, so it can only be as sound as those inputs and their weights. Read these limits before you build one:

- A composite is decision support. It is never clearance for training, competition, or return to sport. Return to sport is a shared decision across a continuum. Clinicians, athletes, and coaches make it, and it weighs risk and risk tolerance (Ardern et al., 2016). Frameworks for that decision combine many kinds of information and the decision-maker's risk tolerance (Shrier, 2015). One number cannot carry that.
- Combining variables into one loses information and makes the result harder to interpret (Song et al., 2013). A single score hides which input changed.
- Song et al. (2013) discuss composites built across many people for research analyses, not one athlete's daily score. Their points apply to this setting by reasoning, not by direct evidence.
- Traffic-light monitoring systems have no standard set-up (Robertson et al., 2017). A composite's colors are a local choice, not a validated scale. About 8% of men of European descent have red-green color deficiency (Birch, 2012), so never let red and green carry the meaning alone.
- Training-load measures cannot tell you whether a change raises or lowers injury risk (Impellizzeri et al., 2020b). A load input has no agreed "better" direction, and it measures the dose, not the athlete's response. Practitioners adjust training load based on the athlete's response (Impellizzeri et al., 2020b). Self-reported well-being worsened with acute rises in load and improved with acute reductions (Saw et al., 2016). A composite that holds load and wellness counts a dose and its response together. Keep load measures out of the composite by default, and show them beside it. The athlete monitoring cycle also reads load and the athlete's response side by side, as separate steps (Gabbett et al., 2017).
- The user may still add a load measure. The user states its direction and the reason, and the output labels it as the user's choice.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.

## Formula

Build a composite in four steps, with an optional fifth:

```text
1. z_i  = (x_i − baseline_mean_i) ÷ baseline_sd_i        for each input i, per athlete
2. z_i' = z_i × d_i                                      d_i = +1 if higher is better, −1 if higher is worse
3. composite = Σ (w_i × z_i') ÷ Σ w_i                    weighted mean of the aligned z-scores
4. Report every z_i', raw value, and change in raw units next to the composite
5. Optional: composite_z = (composite − mean of past composites) ÷ SD of past composites
```

Define every term in the formula:

- `x_i`: the athlete's value for input `i` on the day scored, in that input's own unit
- `baseline_mean_i` and `baseline_sd_i`: the mean and sample standard deviation (SD) of that athlete's previous values for input `i`, over the baseline window. Exclude the day scored. SD measures the usual spread around the mean.
- `z_i`: the input's z-score, in SD units. No unit.
- `d_i`: the direction sign, so that a positive `z_i'` means "better than usual" for every input
- `w_i`: the weight for input `i`. Equal weights give a simple average.
- `composite`: the result. No unit. It is a weighted mean of z-scores, not itself a z-score.
- `composite_z`: the composite standardized against that athlete's own baseline of composite values. Song et al. (2013) describe re-standardizing a composite, for example as a T score. Use it only if the user asks, and name it.

Why the composite is not a z-score: a mean of k unrelated z-scores has an SD of 1 ÷ √k, which is 0.50 for 4 inputs and 0.447 for 5. When the inputs are correlated, the SD is larger: 0.79 for 4 inputs that each correlate at r = 0.5. The spread of a composite depends on the variances and covariances of its inputs (Song et al., 2013). A cut-off on the composite is therefore not comparable with the same cut-off on a single z-score. In a simulation of 4 unrelated inputs, 2.3% of days fell below a composite of −1, against 15.9% for a single z-score.

When you flag across a squad, report the number of flags expected by chance next to the number found. For 4 unrelated inputs and a cut-off of −1, the normal distribution gives a chance rate of 2.3%: 0.57 flags a day across 25 athletes, with a 43.7% chance of at least one. Flags on consecutive days against the same baseline are not independent. Recommend a repeat measurement or a conversation with the athlete before anyone acts on a single flag, because an unusual value tends to be followed by one closer to the mean (Barnett et al., 2005).

These points explain why each step matters:

- Standardize first. Inputs with different units and spreads cannot be averaged as raw values. Standardization stops the input with the largest variance from dominating the composite (Song et al., 2013).
- Standardize against the athlete's own baseline, not the team. A team baseline mixes athletes who use rating scales differently and train at different volumes.
- Keep raw values visible. A z-score cannot show a chronic problem: an athlete who is always sore scores near 0 on a sore day. On a 1 to 5 scale with a small SD, one point can give a large z-score. Show the raw value and the change in points beside each z-score. A practitioner may also flag on the raw value. That is their choice.
- Align directions. A high soreness score is bad on some forms and good on others. In Gastin et al. (2013), 1 was the positive end of each wellness item.
- Choose weights with care. Weights can come from a prior study or from a statistical method such as principal components analysis (Song et al., 2013). No published weights exist for a general readiness composite. Use equal weights unless the user supplies weights and their source.
- Know what equal weights do. Equal weights per input are not equal weights per construct. With three wellness items and one jump test, wellness carries 75% of the weight. Correlated inputs add to this. Song et al. (2013) describe composites as a way to organize highly correlated variables. Offer to average related items into one group score first, then combine the groups.
- Interpret the composite as a composite. Results for a composite apply to the composite, not to any one of its inputs (Song et al., 2013). Read the sub-scores to learn which input moved.

Use this spreadsheet formula, with aligned z-scores in `B2:D2` and weights in `B1:D1`. Leave missing z-scores as blank cells, not 0:

```text
=IF(COUNT(B2:D2)<COLUMNS(B2:D2),NA(),SUMPRODUCT(B1:D1,B2:D2)/SUM(B1:D1))
```

Use this Python code, with one row per athlete-day and one column per aligned z-score:

```python
import pandas as pd

def composite(z, weights):
    """z: aligned z-scores, higher = better. weights: dict of input -> weight."""
    w = pd.Series(weights, dtype=float)
    used = z[w.index]
    out = used.copy()  # keep every sub-score in the output
    out["composite"] = used.mul(w).sum(axis=1, min_count=len(w)) / w.sum()
    out["inputs_present"] = used.notna().sum(axis=1)
    return out
```

This code returns a missing composite on any day with a missing input.

### Calculate it in Power BI and Tableau

A day with any missing input gives a blank composite, never a composite of the inputs that remain. A z-score of 0 counts as present. Weights that sum to 0 give a blank. Show every aligned z-score, raw value, and change in raw units next to the composite.

Both versions assume one aligned z-score measure or field per input, where a positive value means better than usual. Build each z-score with the baseline rules in this skill or the `monitoring-statistics` skill. Multiply by -1 for an input where a higher value is worse. Show the results with one athlete and one date per row.

In Power BI, use this DAX measure. It is a measure because it combines other measures. Put each weight next to its input. The example uses equal weights:

```text
Composite =
VAR inputs =
    {
        ( 1, [Sleep z aligned] ),
        ( 1, [Soreness z aligned] ),
        ( 1, [CMJ z aligned] )
    }
VAR missingInputs = COUNTROWS ( FILTER ( inputs, ISBLANK ( [Value2] ) ) ) + 0
VAR weightSum = SUMX ( inputs, [Value1] )
RETURN
    IF ( missingInputs = 0 && weightSum <> 0, SUMX ( inputs, [Value1] * [Value2] ) / weightSum )
```

The table constructor names its columns `Value1` (the weight) and `Value2` (the z-score).

In Tableau, make one parameter per weight, such as `Weight sleep`. Use this calculation. If the z-scores are table calculations, the composite is a table calculation too. Set its Compute Using, and the Compute Using of each nested z-score, the same way as for the z-scores:

```text
Composite:
IF ISNULL([Sleep z aligned]) OR ISNULL([Soreness z aligned]) OR ISNULL([CMJ z aligned]) THEN NULL
ELSEIF [Weight sleep] + [Weight soreness] + [Weight cmj] = 0 THEN NULL
ELSE ([Weight sleep] * [Sleep z aligned] + [Weight soreness] * [Soreness z aligned] + [Weight cmj] * [CMJ z aligned])
     / ([Weight sleep] + [Weight soreness] + [Weight cmj])
END
```

Blanks behave this way in each tool:

- Power BI: `ISBLANK` is true for a blank, not for 0, so a z-score of 0 counts as present. A missing input makes `missingInputs` above 0, and the measure returns a blank. The spreadsheet returns `#N/A` there.
- Tableau: a null input makes the first test true, and the result is null.
- Both: a text z-score cannot occur, because the z-score is a calculation, not a typed value.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Join the inputs into one row per `athlete_id` and `date`, with one column per input in its own unit, such as `sleep` (1 to 5) and `cmj_cm` (cm).
2. Keep load measures, such as `load_prev_day_au` (AU), in their own columns beside the composite, not in it.
3. Write down each input's direction with the user: +1 if a higher value is better, −1 if a higher value is worse.
4. Ask the user for the baseline window and the minimum number of baseline days for each input. If the user has none, offer at least 10 prior values, labeled as a practice default.
5. For each athlete, input, and day, calculate the baseline mean and sample SD from the baseline window before that day. Exclude the day being scored.
6. Mark an input as missing for that day if its baseline is too short or its SD is 0.
7. Calculate each input's z-score: (value − baseline mean) ÷ baseline SD.
8. Multiply each z-score by its direction sign to get the aligned z-score.
9. Ask the user for weights.
10. If the user has none, use equal weights and say so.
11. Say what share each construct gets.
12. If any input is missing that day, mark the composite as incomplete and do not calculate it, unless the user chose another rule.
13. Calculate the composite: the sum of weight × aligned z-score, divided by the sum of the weights.
14. Report the composite in one table with every input's raw value, change in raw units, baseline mean, baseline SD, and aligned z-score, and the load columns beside it.

## Worked example

One athlete has four inputs. The baseline mean and SD come from the previous 28 days. Wellness items use a 1 to 5 scale where 5 is best, so a 5 for soreness means not sore. Previous-day load is shown beside the composite, not in it.

| Input | Baseline mean | Baseline SD | Direction |
|---|---|---|---|
| Sleep (1 to 5) | 4.0 | 0.5 | +1 |
| Soreness (1 to 5) | 4.0 | 1.0 | +1 |
| Fatigue (1 to 5) | 4.0 | 0.5 | +1 |
| CMJ jump height (cm) | 38.0 | 1.2 | +1 |

Two mornings give the same composite for different reasons:

| Input | Day A raw | Day A change | Day A aligned z | Day B raw | Day B change | Day B aligned z |
|---|---|---|---|---|---|---|
| Sleep | 3 | −1.0 point | −2.0 | 4 | 0.0 points | 0.0 |
| Soreness | 4 | 0.0 points | 0.0 | 3 | −1.0 point | −1.0 |
| Fatigue | 4 | 0.0 points | 0.0 | 4 | 0.0 points | 0.0 |
| CMJ jump height | 38.0 cm | 0.0 cm | 0.0 | 36.8 cm | −1.2 cm | −1.0 |
| Composite, equal weights | | | −0.5 | | | −0.5 |
| Previous-day load, beside the composite | 690 AU | +240 AU | not in composite | 450 AU | 0 AU | not in composite |

Each aligned z-score is (raw − mean) ÷ SD × direction. For example, Day A sleep is (3 − 4.0) ÷ 0.5 × (+1) = −2.0, and Day B jump height is (36.8 − 38.0) ÷ 1.2 × (+1) = −1.0.

Calculate each composite with equal weights:

- Day A composite: (−2.0 + 0.0 + 0.0 + 0.0) ÷ 4 = −0.5.
- Day B composite: (0.0 − 1.0 + 0.0 − 1.0) ÷ 4 = −0.5.

Both days read −0.5. On Day A, one poor night of sleep drives the score. On Day B, more soreness and a lower jump drive it. A practitioner would follow up these two days in different ways. Only the sub-scores show the difference.

The higher load before Day A is shown for context. The composite does not say whether it helped or harmed.

## What changes the number

These choices change the result even when the athlete has not changed:

- Weights. Doubling the weight on jump height gives Day A −0.4 and Day B −0.6. Doubling the weight on sleep gives Day A −0.8 and Day B −0.4. The order of the two days flips with the weights.
- Grouping. Averaging the three wellness items into one group first, then averaging with jump height, gives Day A −0.33 and Day B −0.67. With four equal inputs, wellness carries 75% of the weight.
- Direction of an input. If soreness were entered with a direction of −1 by mistake, Day B would read 0.0 instead of −0.5.
- Adding load. If the user insists on adding previous-day load, Day A (690 AU, z = +2.0) reads −0.8 with a direction of −1 and 0.0 with +1. No published rule sets that direction (Impellizzeri et al., 2020b). Ask the user to state the direction and the reason, and label it as their choice.
- Missing inputs. If Day B had no jump test, filling the gap with 0 gives −0.25, and averaging the three inputs present gives −0.33. Both differ from the complete −0.5. Mark the day as incomplete instead.
- Number of inputs. Adding or removing an input changes the composite and its spread, even when nothing else changes.
- Baseline window. A shorter or longer baseline changes each input's mean and SD, so every z-score moves.
- Team versus athlete baseline. Standardizing against the team gives a different z-score for every input, and mixes athletes who use the scales differently.
- Rescaling. Converting the composite to a 0 to 100 scale changes how it reads, not what it measures.

## Units and typical range

The composite has no unit. Zero means the weighted inputs average out at the athlete's baseline. It is a weighted mean of z-scores, not a z-score, a percentage, a probability, or a risk.

| Population | Typical range | Source |
|---|---|---|
| Any athlete | No validated range or cut-off exists for a general readiness composite. Use cut-offs the practitioner chose, and label them as their choice. | Robertson et al., 2017 (no standard set-up for traffic-light systems) |

## Data you need

Collect this data:

- Source: each input's form, app, or device, joined by athlete and date
- Sampling: one value per input per athlete per day, collected at the same time of day
- Minimum data: each input needs its own baseline. Use the minimum number of baseline days the user chose for each input. If the user has none, offer at least 10 prior values, labeled as a practice default. Report the count. A baseline should be stable, with low variability and no clear trend (Sands et al., 2019).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Showing only the composite. A drop in one input can be cancelled by a rise in another. Always show every sub-score.
- Showing only z-scores. Show each raw value and its change in raw units, so a chronic problem or a one-point change is visible.
- Calling a value "ready", "cleared", "low risk", or "high risk". The composite describes distance from baseline. It does not clear or rule out anyone.
- Reading the composite as a z-score. Its spread depends on the number and correlation of inputs. A cut-off of −1 means something different on the composite than on one input.
- Averaging raw values with different units, such as minutes of sleep and centimeters of jump height. Standardize each input first (Song et al., 2013).
- Standardizing against the team mean instead of each athlete's own baseline
- Leaving input directions mixed, so a "good" soreness score lowers the composite. Align every input first.
- Treating higher load as worse. Putting yesterday's load into the composite with a direction of −1 assumes load is harmful. Load measures cannot tell you that (Impellizzeri et al., 2020b). Load is the dose, and wellness is the response, so a composite of both counts them together (Saw et al., 2016). Show load beside the composite.
- Inventing weights. An AI tool may assign weights such as 40% wellness and 60% load with no source. Use the user's weights, or equal weights, and show them.
- Assuming equal weights mean equal constructs. Three wellness items and one jump test give wellness 75% of the weight.
- Counting the same data twice. Session load and a ratio built from that load are not two independent inputs.
- Including the acute to chronic workload ratio as an input. It adds noise and statistical artifacts and has no evidence for use in injury-reduction decisions (Impellizzeri et al., 2020a).
- Treating a missing input as zero. A z-score of 0 means "at baseline", so a missing value filled with 0 looks like a normal day. Mark the day as incomplete.
- Changing the number of inputs from day to day. A composite from three inputs is not comparable with one from five.
- Rescaling to 0 to 100 and calling it "% ready". This looks like a probability. It is not one.
- Building the composite from unvalidated questions and treating it as validated. The most used single-item wellness questions have not been validated (Jeffries et al., 2020).
- Assuming subjective and objective inputs move together. They generally did not correlate in a systematic review, and subjective measures tracked training load more consistently (Saw et al., 2016). Disagreement between inputs is information. Show it.

## Example request

> I want one readiness number per player each morning from sleep, soreness, mood, yesterday's sRPE load, and CMJ jump height. Weight it however you think is best and tell me who is good to train.

The correct answer builds an equal-weight composite of aligned, athlete-specific z-scores from sleep, soreness, mood, and jump height. It shows yesterday's load beside the composite and explains why load is not in it. It shows all four sub-scores with their raw values, asks for the user's weights, labels the output as distance from baseline, and declines to say who is good to train.

## Check the result

Run these checks:

- Recalculate one athlete-day by hand: each z-score from its baseline, the direction sign, then the weighted mean.
- Confirm every sub-score, raw value, and change in raw units appears next to the composite, and that each input's direction is stated.
- Confirm no load measure is inside the composite unless the user chose it and stated the direction and reason.
- Confirm days with a missing input show as incomplete, not as a composite near zero.

## Sources

This file cites these sources:

- Song MK, Lin FC, Ward SE, Fine JP. Composite variables: when and how. Nurs Res. 2013;62(1):45-49. https://doi.org/10.1097/NNR.0b013e3182741948
- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. Int J Sports Physiol Perform. 2017;12(Suppl 2):S2-73-S2-79. https://doi.org/10.1123/ijspp.2016-0541
- Ardern CL, Glasgow P, Schneiders A, Witvrouw E, Clarsen B, Cools A, et al. 2016 Consensus statement on return to sport from the First World Congress in Sports Physical Therapy, Bern. Br J Sports Med. 2016;50(14):853-864. https://doi.org/10.1136/bjsports-2016-096278
- Shrier I. Strategic Assessment of Risk and Risk Tolerance (StARRT) framework for return-to-play decision-making. Br J Sports Med. 2015;49(20):1311-1315. https://doi.org/10.1136/bjsports-2014-094569
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. Int J Sports Physiol Perform. 2020;15(6):907-913. https://doi.org/10.1123/ijspp.2019-0864 (cited as 2020a)
- Impellizzeri FM, McCall A, Ward P, Bornn L, Coutts AJ. Training load and its role in injury prevention, part 2: conceptual and methodologic pitfalls. J Athl Train. 2020;55(9):893-901. https://doi.org/10.4085/1062-6050-501-19 (cited as 2020b)
- Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. Br J Sports Med. 2016;50(5):281-291. https://doi.org/10.1136/bjsports-2015-094758
- Jeffries AC, Wallace L, Coutts AJ, McLaren SJ, McCall A, Impellizzeri FM. Athlete-reported outcome measures for monitoring training responses: a systematic review of risk of bias and measurement property quality according to the COSMIN guidelines. Int J Sports Physiol Perform. 2020;15(9):1203-1215. https://doi.org/10.1123/ijspp.2020-0386
- Gastin PB, Meyer D, Robinson D. Perceptions of wellness to monitor adaptive responses to training and competition in elite Australian football. J Strength Cond Res. 2013;27(9):2518-2526. https://doi.org/10.1519/JSC.0b013e31827fd600
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-220. https://doi.org/10.1093/ije/dyh299
- Sands WA, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone MH. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- Gabbett TJ, Nassis GP, Oetter E, Pretorius J, Johnston N, Medina D, Rodas G, Myslinski T, Howells D, Beard A, Ryan A. The athlete monitoring cycle: a practical guide to interpreting and applying training monitoring data. Br J Sports Med. 2017;51(20):1451-1452. https://doi.org/10.1136/bjsports-2016-097298 (accessed 2026-10-02)
- Birch J. Worldwide prevalence of red-green color deficiency. J Opt Soc Am A Opt Image Sci Vis. 2012;29(3):313-320. https://doi.org/10.1364/JOSAA.29.000313 (accessed 2026-10-02)
