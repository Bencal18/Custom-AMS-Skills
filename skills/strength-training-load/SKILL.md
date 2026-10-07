---
name: strength-training-load
description: Calculate volume load, estimated 1RM from reps or RPE, and personal bests from training logs. Checks units, rep ranges, and which formula was used. You choose the loads.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Strength training load

This skill helps you turn a weight room training log into volume load, estimated one-repetition maximum (1RM), and personal bests. It works with set-level exports from any training log app or spreadsheet.

## When to use

Use this skill when the user asks to:

- Calculate volume load (sets × reps × load) for each exercise, session, or week.
- Decide how to count bodyweight exercises, single-leg or single-arm work, timed holds, or bands and chains.
- Estimate 1RM from a set of reps, or from reps with a rating of perceived exertion (RPE) or reps in reserve (RIR).
- Compare Epley, Brzycki, and other 1RM formulas, or explain why two estimates differ.
- Track each athlete's best tested lift and best estimated 1RM over time.
- Calculate relative strength, the load lifted divided by body mass.
- Read a training log export with one row per set, or reshape one that is not.
- Write a spreadsheet formula, Python or R code, or a Power BI or Tableau calculation for any of these.
- Check whether a strength number looks right.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Volume load by exercise, session, and week | [references/volume-load.md](references/volume-load.md) |
| Estimated 1RM from reps, RPE, or RIR | [references/estimated-1rm.md](references/estimated-1rm.md) |
| Personal bests, tested and estimated, and relative strength | [references/personal-bests.md](references/personal-bests.md) |

Read [references/training-log-exports.md](references/training-log-exports.md) before you calculate anything from a training log export.

## Steps

Follow these steps in order:

1. Ask where the data came from, if the user has not said: a training log app export, a spreadsheet, or a paper log typed in.
2. Load `references/training-log-exports.md`.
3. Load the reference file for each metric the user asks about.
4. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
5. Reshape the data to one row per set, as `references/training-log-exports.md` describes.
6. List each input column with its unit.
7. Convert every load to kilograms. Multiply pounds by 0.45359237. Never mix kg and lb in one sum.
8. Confirm the exercise, its variant, and the equipment for every row, such as free-weight back squat or safety bar squat. Never mix exercises or variants in one calculation.
9. Confirm whether each row is a warm-up, a work set, or a test set. Ask whether to count warm-up sets, if the user has not said.
10. Confirm how the log records single-leg and single-arm sets: reps per side, or reps for both sides together.
11. Confirm how the log records dumbbell and kettlebell loads: one implement, or the total of both.
12. Ask how to treat bodyweight exercises, timed holds, and bands or chains, if the data has them. Show the options in `references/volume-load.md`. Use one choice for every athlete and session.
13. For an estimated 1RM, ask which formula to use. Show the options and their errors in `references/estimated-1rm.md`. Do not pick one for the coach.
14. For an estimated 1RM, ask for the highest rep count to accept. If the user has no preference, offer 10 reps and say it is this skill's choice, as `references/estimated-1rm.md` explains.
15. For an estimated 1RM from RPE, confirm the scale is the RIR-based scale, where RPE 10 means 0 reps in reserve.
16. Keep tested 1RMs and estimated 1RMs in separate columns. Never let an estimate replace a tested value.
17. Calculate each athlete, exercise, and session separately.
18. Calculate the metric with the formula in the reference file. Follow its "Calculate the metric" steps.
19. Run the checks below.
20. Show the formula, the variant, and the units next to each result. For an estimated 1RM, also show the reps, the RIR if used, and the rep limit.
21. Name any choice from the reference file's "What changes the number" section that applies.

The `velocity-based-training` skill estimates 1RM from bar speed instead of reps. If the user has bar speed data, name that skill and keep its estimates in a separate column from estimates made here.

If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures. Keep the set-level log in its own table, as `references/training-log-exports.md` describes.

## Checks before answering

Run these checks on your own result before you show it. In the answer, give each check a one-line result of pass, fail, or could not check. The checks are these:

- Unit check: every load is in kg. No value in lb is left unconverted. Volume load is in kg, and relative strength is in kg per kg of body mass.
- Size check: a load several times larger than the athlete's other sets of the same exercise often means lb read as kg, a total typed in the load column, or a typo. Flag it as "check this value".
- Rep check: every estimated 1RM comes from a set within the chosen rep limit. Report how many sets you left out because they were over the limit.
- Formula check: every estimated 1RM names its formula. No column mixes formulas, or mixes estimates from reps with estimates from bar speed.
- Order check: an estimated 1RM is never lower than the load lifted in that set. A tested 1RM is a successful single.
- Side check: single-leg and single-arm volume load is labeled per side or total.
- Count check: the number of athletes, sessions, exercises, and sets matches the input. Report rows dropped for missing reps or load.
- Recompute check: recompute one set by hand and confirm it matches your formula or code.
- Change check: judge a change in a best lift with the rules below.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

If the `monitoring-statistics` skill is installed, use it for detail. Follow these rules before you call a new best real:

- Typical error (TE) is the test's noise: the standard deviation (SD) of one athlete's repeated scores when nothing real changed. Take it from a short-term retest with the same exercise, equipment, and protocol. `references/personal-bests.md` gives the published spread of 1RM retest error.
- Noise band for two single tests: 1.96 × √2 × TE, about 2.77 × TE. The 95% level is a choice.
- An estimated 1RM carries the formula's error on top of the test's noise. Do not judge a change in an estimated 1RM with a TE from tested 1RMs.
- If the user has no TE, say the change cannot be judged against noise. Tell them to measure TE from a repeated test.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not choose the athlete's load, sets, reps, RPE target, or the 1RM used to set percentage loads. Show the formulas and published figures in the reference files as study settings, not recommendations, and leave the choice to the coach.
- Present every estimated 1RM as an estimate, with its formula, reps, RIR if used, and rep limit. Never present it as a tested 1RM.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source and population.
- Do not compare volume load across exercises as if a kilogram in one lift equals a kilogram in another. Report it by exercise, and label any total across exercises.
- Do not fill missing sets, reps, or loads unless the user asks. If the user asks, name the method and show results with and without the filled values.
- Do not rate, rank, pass, or fail an athlete on relative strength or volume load.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- Athlete data is personal data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed:

- [references/training-log-exports.md](references/training-log-exports.md): how to read set-level training log exports, reshape other layouts, and convert units
- [references/volume-load.md](references/volume-load.md): volume load by exercise, session, and week, with bodyweight, single-leg and single-arm, timed, and band or chain sets, and absolute versus relative load
- [references/estimated-1rm.md](references/estimated-1rm.md): estimated 1RM from reps, RPE, or RIR, with Epley, Brzycki, the error of each, and rep limits
- [references/personal-bests.md](references/personal-bests.md): best tested and best estimated lifts per athlete and exercise over time, and relative strength
- [references/eliteform.md](references/eliteform.md): how to read EliteForm set and rep training logs and 1RMs from its API
