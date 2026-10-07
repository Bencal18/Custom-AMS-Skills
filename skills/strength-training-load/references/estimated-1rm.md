# Estimated 1RM

Last checked: 2026-10-07

## What it measures

An estimated one-repetition maximum (1RM) is a prediction of the heaviest load an athlete could lift once, made from a set of several reps with a lighter load. It is an estimate, not a test. A tested 1RM is a successful single at the heaviest load the athlete lifted.

This file covers estimates from reps, and from reps with a rating of perceived exertion (RPE) or reps in reserve (RIR). The `velocity-based-training` skill estimates 1RM from bar speed. Keep the two kinds of estimate in separate columns.

## Formula

Every formula here assumes the set went to failure, or that you know how many more reps the athlete could have done. Work out reps to failure first:

```text
reps to failure = reps completed + RIR
RIR             = 10 − RPE, on the RIR-based RPE scale
```

Then use one of these formulas. They give different numbers for the same set:

```text
Epley:    estimated 1RM (kg) = load (kg) × (1 + 0.0333 × reps to failure)
Brzycki:  estimated 1RM (kg) = load (kg) ÷ (1.0278 − 0.0278 × reps to failure)
```

Define every term in the formula:

- `load`: the load lifted in the set, in kg.
- `reps completed`: reps the athlete finished in the set.
- `RIR`: reps in reserve, the number of extra reps the athlete thinks they could have done. A set to failure has an RIR of 0.
- `RPE`: rating of perceived exertion on the RIR-based scale, where RPE 10 means 0 RIR, RPE 9 means 1 RIR, and so on (Zourdos et al., 2016). Some versions of the scale use half points, such as 9.5.
- `reps to failure`: the reps the athlete could have done in that set. It can be a decimal when RPE uses half points.

The Epley formula as written above is from Macarilla et al. (2022), citing DiStasio (2014), a thesis this skill did not read. The Brzycki formula is from the table of equations in Beia et al. (2024), citing Brzycki (1993). Beia et al. (2024) and Oberhofer et al. (2021) cite Epley (1985) for the Epley formula. Oberhofer et al. (2021) wrote Brzycki in another form, load × 36 ÷ (37 − reps). The two forms are nearly equal within 1 to 10 reps, but not identical. At 100 kg and 10 reps, they give 133.37 and 133.33 kg. This skill could not open the original Epley chart or the original Brzycki article. Epley (1985) is a poundage chart, not a peer-reviewed paper.

Other formulas are in use. Beia et al. (2024) list Lander, Mayhew et al., O'Conner et al., Wathen, and Kemmler et al. as well. Use one of them only if the user gives the formula and its source.

Follow these rules:

- At 1 rep to failure, Brzycki returns the load itself. Epley returns 1.0333 × the load. This skill returns the load itself for Epley at 1 rep. That is this skill's choice. Say so.
- Brzycki cannot be used at 37 reps or more, because the divisor reaches 0. The two Brzycki forms are nearly equal within 1 to 10 reps, so the limit is the same in practice.
- The coach chooses the formula. Do not pick one. Use the same formula for every athlete, exercise, and session.
- The coach chooses which 1RM sets percentage loads: a tested 1RM, an estimate from reps, or an estimate from bar speed. Do not pick one.

### Choose a rep limit

This skill uses a default limit of 10 reps to failure. Sets above the limit get no estimate. The limit is this skill's choice. No study found here tested it for Epley or Brzycki. It draws on these study settings:

- Reynolds et al. (2006) tested 70 adults aged 18 to 69 on the chest press and leg press. In their own regression equations, 5RM data gave the most accurate prediction. They concluded that no more than 10 reps should be used in linear equations to estimate 1RM for those two lifts.
- Roberts et al. (2025) cross-validated 18 published equations in recreationally active men, on the bench press and leg extension, with sets at 80% of 1RM. For their own modified equations, they used loads that give 4 to 10 reps to failure.

The coach can change the limit. Name it next to every estimate.

### Why estimates from high-rep sets are less certain

Three findings explain why an estimate from 15 or 20 reps is less trustworthy than one from 3 to 5:

- Athletes differ more at light loads. A meta-regression is a statistical method that pools results across many studies. In one of 952 repetitions-to-failure tests from 7289 people in 269 studies, the between-individual standard deviation (SD, the typical spread between people) of reps to failure was 2.51 reps at 80% of 1RM and 4.36 reps at 60% of 1RM (Nuzzo et al., 2024). One formula cannot fit everyone at light loads.
- Reps at a given %1RM differ by exercise. At 80% of 1RM, the estimated reps to failure were 8.8 in the bench press and 13.1 in the leg press. At 70%, they were 14.1 and 19.0 (Nuzzo et al., 2024). The main model estimated about 5 reps at 90% and about 15 at 70%, against 4 and 11 in a common textbook table (Nuzzo et al., 2024).
- The formulas differ by rep count. At 100 kg, Epley minus Brzycki is 3.80 kg at 2 reps, 4.14 kg at 5, 2.48 kg at 8, and −0.07 kg at 10. The two nearly agree near 10 reps and differ more away from it, most above 10. At 15 reps, the gap is −13.77 kg. See the worked example.

### Estimate from RPE or RIR

Helms et al. (2016) describe how reps and RIR trade off at a similar load. In their chart, 6 reps at 0 RIR, 5 at 1 RIR, 4 at 2 RIR, and 3 at 3 RIR are roughly the same load. The chart came from the mean scores of trained lifters in the back squat. Helms et al. (2016) warn that it is not an absolute conversion, because of individual differences and day-to-day changes in strength.

This skill adds RIR to reps and puts the sum into a rep formula. This skill found no study that checked a 1RM estimated this way against a tested 1RM. Treat it as less certain than an estimate from a set to failure, and say so.

### The error of each method

Use these published figures to describe how far an estimate can be from a tested 1RM, and how far a rated RIR or RPE can be from the truth. Each comes from one population and set of lifts. The standard error of the estimate is the typical gap between predicted and tested values. A 95% confidence interval (CI) is the range likely to hold the true average:

| Method | Finding | Source |
|---|---|---|
| Seven rep formulas, bench press, squat, and deadlift, 67 untrained college students | Correlations with tested 1RM above 0.95. In the bench press, the mean difference from tested 1RM was significantly different from zero for 5 of the 7 formulas. In the squat, it was significantly different from zero for 6 of the 7. Every formula underestimated the deadlift. | LeSuer et al., 1997 (abstract) |
| Regression from 5RM, 70 adults | Standard error of the estimate 2.98 kg for the chest press and 16.16 kg for the leg press | Reynolds et al., 2006 (abstract) |
| Mayhew and Wathen formulas, lat pull-down and seated cable row, 23 healthy adults, one set to failure at 80% of 1RM | Both underestimated tested 1RM, by 2.14 to 6.65 kg | Pérez-Castilla et al., 2021 (abstract) |
| Predicting reps left before failure, meta-analysis of 12 studies with 414 participants | People underpredicted reps to failure by 0.95 reps on average (95% CI 0.17 to 1.73), with large differences between studies. Predictions were better in sets of 12 reps or fewer. Predictions closer to failure were only slightly improved, and the 95% CI of that effect crossed zero. | Halperin et al., 2022 (abstract) |
| RPE scores for single reps, 15 experienced squatters | SD of RPE scores 0.32 at 100%, 0.92 at 90%, 0.97 at 75%, and 1.18 at 60% of 1RM | Zourdos et al., 2016, as reported by Helms et al., 2016 |
| RPE at a tested 1RM, 15 powerlifters | RPE 9.6 ± 0.5 in the squat, 9.7 ± 0.4 in the bench press, and 9.6 ± 0.5 in the deadlift | Helms et al., 2017 (abstract) |

A high correlation does not mean an estimate is close. LeSuer et al. (1997) found correlations above 0.95 alongside mean differences that were significantly different from zero.

### Calculate it in a spreadsheet

Put one set per row, with load in kg in `B2`, reps in `C2`, RPE in `D2`, and RIR in `E2`. These column letters are for this file only. Remap them to the user's sheet. Enter 0 in `E2` for a set to failure. Put the rep limit in `K1`, such as 10. Use these formulas:

```text
RIR from RPE, E2:        =IF(ISNUMBER(D2),10-D2,"")
Reps to failure, F2:     =IF(COUNT(C2,E2)<2,"",C2+E2)
Epley e1RM (kg), G2:     =IF(COUNT(B2,F2)<2,"",IF(OR(F2<1,F2>$K$1),"",IF(F2=1,B2,B2*(1+0.0333*F2))))
Brzycki e1RM (kg), H2:   =IF(COUNT(B2,F2)<2,"",IF(OR(F2<1,F2>$K$1,F2>=37),"",B2/(1.0278-0.0278*F2)))
```

Use the RIR-from-RPE formula only when the log records RPE in `D2` instead of RIR. Leave warm-up rows out of the sheet, or blank their estimates, so they cannot enter a best. Each formula returns a blank when an input is missing or the set is over the rep limit. Never fill a blank RIR with 0 unless the set went to failure.

### Calculate it in Power BI and Tableau

Both versions assume the `sets` table in `training-log-exports.md`.

In Power BI, add these calculated columns to `sets`. Change `maxReps` to the coach's rep limit:

```text
Reps to failure =
VAR rir =
    IF (
        NOT ISBLANK ( sets[rir] ),
        sets[rir],
        IF ( NOT ISBLANK ( sets[rpe] ), 10 - sets[rpe] )
    )
RETURN
    IF ( NOT ISBLANK ( sets[reps] ) && NOT ISBLANK ( rir ), sets[reps] + rir )

e1RM Epley (kg) =
VAR r = sets[Reps to failure]
VAR w = sets[load]
VAR maxReps = 10
RETURN
    IF (
        sets[status] = "ok" && sets[set_type] = "work" && sets[load_unit] = "kg"
            && sets[load_type] = "external"
            && NOT ISBLANK ( w ) && NOT ISBLANK ( r ) && r >= 1 && r <= maxReps,
        IF ( r = 1, w, w * ( 1 + 0.0333 * r ) )
    )

e1RM Brzycki (kg) =
VAR r = sets[Reps to failure]
VAR w = sets[load]
VAR maxReps = 10
RETURN
    IF (
        sets[status] = "ok" && sets[set_type] = "work" && sets[load_unit] = "kg"
            && sets[load_type] = "external"
            && NOT ISBLANK ( w ) && NOT ISBLANK ( r ) && r >= 1 && r <= maxReps && r < 37,
        w / ( 1.0278 - 0.0278 * r )
    )
```

The `ISBLANK` tests matter: in DAX, a blank plus a number gives the number, so a missing RIR would count as 0. For the best estimate in a session, use a measure such as `Best e1RM Epley (kg) = MAX ( sets[e1RM Epley (kg)] )` with `athlete_id`, `session_id`, and `exercise` in the visual.

In Tableau, create a parameter `Max reps` set to the coach's limit, and use these row-level calculations:

```text
Reps to failure:
IF NOT ISNULL([rir]) THEN [reps] + [rir]
ELSEIF NOT ISNULL([rpe]) THEN [reps] + 10 - [rpe]
END

e1RM Epley (kg):
IF [status] = "ok" AND [set_type] = "work" AND [load_unit] = "kg" AND [load_type] = "external"
   AND [Reps to failure] >= 1 AND [Reps to failure] <= [Max reps]
THEN IF [Reps to failure] = 1 THEN [load] ELSE [load] * (1 + 0.0333 * [Reps to failure]) END
END

e1RM Brzycki (kg):
IF [status] = "ok" AND [set_type] = "work" AND [load_unit] = "kg" AND [load_type] = "external"
   AND [Reps to failure] >= 1 AND [Reps to failure] <= [Max reps] AND [Reps to failure] < 37
THEN [load] / (1.0278 - 0.0278 * [Reps to failure])
END
```

Take `MAX` of either field for the best estimate in a session.

Blanks behave this way in each tool:

- Power BI: a missing load, reps, or RIR and RPE gives a blank estimate. `MAX` skips blanks.
- Tableau: a null input makes the test null, so the estimate is null. `MAX` skips nulls.

### Calculate it in Python or R

Use this Python code. It uses the standard library only. Pass only work sets with status `ok`, load in kg, and external load:

```python
def reps_to_failure(reps, rir=None, rpe=None):
    if reps is None:
        return None
    if rir is not None:
        return reps + rir
    if rpe is not None:
        return reps + (10 - rpe)
    return None  # unknown; do not assume failure

def e1rm(load_kg, rtf, formula, max_reps=10):
    if load_kg is None or rtf is None or rtf < 1 or rtf > max_reps:
        return None
    if formula == "epley":
        return load_kg if rtf == 1 else load_kg * (1 + 0.0333 * rtf)
    if formula == "brzycki":
        return None if rtf >= 37 else load_kg / (1.0278 - 0.0278 * rtf)
    raise ValueError("name the formula")
```

Use this R code. Pass only work sets with status `ok`, load in kg, and external load:

```r
e1rm <- function(load_kg, rtf, formula, max_reps = 10) {
  ok <- !is.na(load_kg) & !is.na(rtf) & rtf >= 1 & rtf <= max_reps
  est <- switch(formula,
    epley   = ifelse(rtf == 1, load_kg, load_kg * (1 + 0.0333 * rtf)),
    brzycki = ifelse(rtf >= 37, NA, load_kg / (1.0278 - 0.0278 * rtf)),
    stop("name the formula"))
  ifelse(ok, est, NA)
}
```

## Calculate the metric

Follow these steps to estimate 1RM from a training log:

1. Reshape the log to one row per set, in kg, as `training-log-exports.md` describes.
2. Keep work sets only. Leaving out warm-up sets is this skill's default choice.
3. Ask which formula the coach uses.
4. Ask for the rep limit, or offer this skill's default limit of 10 reps to failure. The default is this skill's choice.
5. Find the RIR for each set. Use the RIR column, or 10 − RPE on the RIR-based scale.
6. If a set has no RIR or RPE, ask whether it went to failure. Use RIR 0 only if it did.
7. Add RIR to reps completed to get reps to failure.
8. Leave out sets with reps to failure above the limit, and count them.
9. Apply the chosen formula to each remaining set.
10. Keep the highest estimate per athlete, exercise, and session, if the user wants one value per session.
11. Label every estimate with the formula, reps, RIR, and rep limit.
12. Keep estimates apart from tested 1RMs and from bar speed estimates.

## Worked example

This example uses one made-up athlete's back squat sets. Every number below came from running the calculation in Python.

| Set | Load | Reps | RIR | Reps to failure |
|---|---|---|---|---|
| A | 100 kg | 5 | 0, to failure | 5 |
| B | 100 kg | 5 | 2, from RPE 8 | 7 |
| C | 70 kg | 15 | 0, to failure | 15 |

Step 1. Set A with Epley: 100 × (1 + 0.0333 × 5) = 116.65 kg.

Step 2. Set A with Brzycki: 100 ÷ (1.0278 − 0.0278 × 5) = 100 ÷ 0.8888 = 112.51 kg. The two formulas differ by 4.14 kg for the same set.

Step 3. Set B with Epley: 100 × (1 + 0.0333 × 7) = 123.31 kg. With Brzycki: 120.02 kg.

Step 4. If the athlete misjudged set B by 1 rep, and really had 3 RIR, reps to failure is 8. Epley gives 126.64 kg, 3.33 kg higher.

Step 5. Set C has 15 reps to failure, above the 10-rep limit, so it gets no estimate by default. If the coach raises the limit, Epley gives 104.97 kg and Brzycki gives 114.60 kg, 9.64 kg apart.

Step 6. For comparison, 100 kg for 10 reps gives 133.30 kg with Epley and 133.37 kg with Brzycki. The formulas nearly agree at 10 reps and differ more above it. At 60 kg for 20 reps, they give 99.96 and 127.17 kg.

Result: from set A, the estimated 1RM is 116.65 kg (Epley) or 112.51 kg (Brzycki), from 5 reps to failure, rep limit 10. Report the formula the coach chose, not both, unless the coach asks for both.

## What changes the number

These choices change the result even when the athlete's strength does not:

- Formula. In the worked example, the same 5-rep set gives 116.65 or 112.51 kg.
- RIR judgment. One rep of error in RIR moved set B's Epley estimate by 3.33 kg. People underpredicted reps to failure by 0.95 reps on average (Halperin et al., 2022).
- Rep count. Above 10 reps, the formulas differ more, by 9.64 kg at 15 reps in the worked example.
- Exercise. Reps at a given %1RM differ by exercise (Nuzzo et al., 2024), and every formula underestimated the deadlift in LeSuer et al. (1997).
- Failure. A set stopped short of failure, with no RIR recorded, gives an estimate that is too low.
- Rep tempo, range of motion, and rest between sets. Keep them the same when you compare estimates.
- Epley at 1 rep. Returning the load itself, as this skill does, gives 100 kg for a 100 kg single. The raw formula gives 103.33 kg.

## Units and typical range

Report the estimated 1RM in kg, with the formula, reps to failure, and rep limit.

This skill does not give a typical range for estimated 1RM. It depends on the exercise and the athlete. Check every estimate against the load lifted in the same set and against the athlete's tested 1RM, if one exists.

## Data you need

Collect this data:

- Source: a training log with one row per set.
- Fields: load in kg and reps completed for each set, plus RIR or RIR-based RPE, or a note that the set went to failure.
- Exercise: the exercise, variant, and equipment for each set.
- Minimum data: one set within the rep limit. More sets give more estimates to compare, not a more accurate single estimate.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using reps completed from a set not taken to failure, with no RIR. The estimate is too low.
- Writing Epley with 0.333 instead of 0.0333. This makes the estimate far too high. One published table has this typo (Beia et al., 2024).
- Writing Brzycki with + 0.0278 × reps in the divisor instead of − 0.0278 × reps. One published paper has this typo (Macarilla et al., 2022).
- Mixing formulas between athletes or sessions.
- Estimating from 15 or 20 reps and treating it like an estimate from 5.
- Reading RPE on a 1 to 10 effort scale as if it were the RIR-based scale.
- Replacing a tested 1RM with a higher estimate.
- Calling an estimated 1RM a 1RM, with no label.
- Computing load from a planned %1RM in the log instead of using the load lifted.

## Example request

> Our log has load, reps, and RPE for every squat and bench set. Can you add an estimated 1RM for each session in Google Sheets, and tell me how much to trust it?

## Check the result

Run these checks:

- Recompute one value by hand: 100 × (1 + 0.0333 × 5) = 116.65 kg.
- Check that every estimate is at least the load lifted in the set.
- Check that no estimate came from a set above the rep limit.
- Check that every estimate names its formula, reps to failure, and rep limit.
- Check estimates against the athlete's tested 1RM in the same exercise, if one exists. A large gap often means a wrong RIR, wrong units, or a set not taken to failure.

## Sources

This file draws on these sources:

- Nuzzo JL, Pinto MD, Nosaka K, Steele J. Maximal number of repetitions at percentages of the one repetition maximum: a meta-regression and moderator analysis of sex, age, training status, and exercise. Sports Medicine. 2024;54(2):303-321. https://doi.org/10.1007/s40279-023-01937-7 (accessed 2026-10-07)
- Macarilla CT, Sautter NM, Robinson ZP, Juber MC, Hickmott LM, Cerminaro RM, Benitez B, Carzoli JP, Bazyler CD, Zoeller RF, Whitehurst M, Zourdos MC. Accuracy of predicting one-repetition maximum from submaximal velocity in the barbell back squat and bench press. Journal of Human Kinetics. 2022;82:201-212. https://doi.org/10.2478/hukin-2022-0046 (accessed 2026-10-07)
- Beia R, Wassermann A, Raps S, Mayhew J, Uder M, Kemmler W. Developing accurate repetition prediction equations for trained older adults with osteopenia. Sports. 2024;12(9):233. https://doi.org/10.3390/sports12090233 (accessed 2026-10-07). Cited for its table of formulas only.
- Oberhofer K, Erni R, Sayers M, Huber D, Lüthy F, Lorenzetti S. Validation of a smartwatch-based workout analysis application in exercise recognition, repetition count and prediction of 1RM in the strength training-specific setting. Sports. 2021;9(9):118. https://doi.org/10.3390/sports9090118 (accessed 2026-10-07). Cited for its form of the Brzycki formula only.
- Reynolds JM, Gordon TJ, Robergs RA. Prediction of one repetition maximum strength from multiple repetition maximum testing and anthropometry. Journal of Strength and Conditioning Research. 2006;20(3):584-592. https://doi.org/10.1519/R-15304.1 (abstract, accessed 2026-10-07)
- Roberts TD, Smith RW, Arnett JE, Ortega DG, Schmidt RJ, Housh TJ. Cross-validation of equations for estimating 1 repetition maximum from repetitions to failure for the bench press and leg extension. Journal of Strength and Conditioning Research. 2025;39(2):e96-e105. https://doi.org/10.1519/JSC.0000000000004987 (abstract, accessed 2026-10-07)
- LeSuer DA, McCormick JH, Mayhew JL, Wasserstein RL, Arnold MD. The accuracy of prediction equations for estimating 1-RM performance in the bench press, squat, and deadlift. Journal of Strength and Conditioning Research. 1997;11(4):211-213. https://doi.org/10.1519/00124278-199711000-00001 (abstract, accessed 2026-10-07)
- Pérez-Castilla A, Suzovic D, Domanovic A, Fernandes JFT, García-Ramos A. Validity of different velocity-based methods and repetitions-to-failure equations for predicting the 1 repetition maximum during 2 upper-body pulling exercises. Journal of Strength and Conditioning Research. 2021;35(7):1800-1808. https://doi.org/10.1519/JSC.0000000000003076 (abstract, accessed 2026-10-07)
- Zourdos MC, Klemp A, Dolan C, Quiles JM, Schau KA, Jo E, Helms E, Esgro B, Duncan S, Garcia Merino S, Blanco R. Novel resistance training-specific rating of perceived exertion scale measuring repetitions in reserve. Journal of Strength and Conditioning Research. 2016;30(1):267-275. https://doi.org/10.1519/JSC.0000000000001049 (abstract, accessed 2026-10-07)
- Helms ER, Cronin J, Storey A, Zourdos MC. Application of the repetitions in reserve-based rating of perceived exertion scale for resistance training. Strength and Conditioning Journal. 2016;38(4):42-49. https://doi.org/10.1519/SSC.0000000000000218 (accessed 2026-10-07)
- Helms ER, Storey A, Cross MR, Brown SR, Lenetsky S, Ramsay H, Dillen C, Zourdos MC. RPE and velocity relationships for the back squat, bench press, and deadlift in powerlifters. Journal of Strength and Conditioning Research. 2017;31(2):292-297. https://doi.org/10.1519/JSC.0000000000001517 (abstract, accessed 2026-10-07)
- Halperin I, Malleron T, Har-Nir I, Androulakis-Korakakis P, Wolf M, Fisher J, Steele J. Accuracy in predicting repetitions to task failure in resistance exercise: a scoping review and exploratory meta-analysis. Sports Medicine. 2022;52(2):377-390. https://doi.org/10.1007/s40279-021-01559-x (abstract, accessed 2026-10-07)
