---
name: load-and-wellness
description: Work out training load from session RPE and heart rate, score wellness and recovery forms, track a taper, and split training by intensity. Shows the formula and checks each result.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "3"
---

# Load and wellness

This skill helps you calculate training load from athlete effort ratings, compare recent load with longer-term load, describe how load was spread across a week or a taper, score recovery questionnaires, and turn daily wellness answers into scores against each athlete's own normal. It tells the AI which formula variant to use, what the result means, and what it cannot tell you.

## When to use

Use this skill when the user asks to:

- Work out session RPE load, daily load, or weekly load from RPE and minutes.
- Work out heart rate load (TRIMP) or time in heart rate zones from heart rate data.
- Calculate an acute to chronic workload ratio, an acute load, or a chronic load.
- Compare rolling averages with exponentially weighted moving averages for load.
- Work out weekly training monotony or training strain from daily load.
- Flag a wellness answer that is unusual for that athlete.
- Turn sleep, soreness, fatigue, stress, or mood scores into z-scores.
- Work out how much training volume dropped in a taper, with intensity and frequency beside it.
- Group a week's or a block's training into three intensity zones, and label it pyramidal or polarized.
- Score the Hooper index, Total Quality Recovery (TQR), Perceived Recovery Status (PRS), or the Brief Assessment of Mood (BAM).
- Estimate TRIMP or accelerometer load for athletes who played but did not wear a device, from minutes played or time on ice.
- Set up a load and wellness log in a spreadsheet, R, Python, Power BI, or Tableau.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Session RPE load | [references/session-rpe-load.md](references/session-rpe-load.md) |
| Heart rate load (TRIMP) and time in zones | [references/heart-rate-load.md](references/heart-rate-load.md) |
| Acute to chronic workload ratio (ACWR) | [references/acwr.md](references/acwr.md) |
| Training monotony and strain | [references/monotony-and-strain.md](references/monotony-and-strain.md) |
| Wellness z-score | [references/wellness-z-score.md](references/wellness-z-score.md) |
| Taper volume reduction and intensity distribution | [references/taper-and-distribution.md](references/taper-and-distribution.md) |
| Hooper index, TQR, PRS, and BAM scores | [references/recovery-questionnaires.md](references/recovery-questionnaires.md) |
| Estimated load for athletes who did not wear a device | [references/estimated-load.md](references/estimated-load.md) |

## Steps

Follow these steps in order:

1. Ask which form, app, or device the data came from, if the user has not said.
2. For Catapult, Kinexon, Polar Team Pro, Firstbeat Sports, or STATSports data, load the matching device file listed under References.
3. Load the reference file for each metric the user asks about.
4. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
5. Confirm the RPE scale. Session RPE load uses the 0 to 10 category ratio scale (CR-10).
6. Stop and ask if the values look like the 6 to 20 scale.
7. Ask about values above 10 before you call them errors: the form may use the Borg CR100 scale.
8. Confirm duration is in minutes.
9. Convert hours or `hh:mm` text to minutes before you multiply. Playing time and time on ice usually arrive as `mm:ss`. Check which format the column uses before you convert.
10. Build one row per athlete per calendar day for any rolling calculation.
11. Put `0` on days with no training.
12. Put a missing value on days when training happened but no rating was recorded.
13. Mark ill, unavailable, or modified-training days in a separate column.
14. For estimated load, ask whether the user has their own estimation formula, and where playing time comes from. Follow [references/estimated-load.md](references/estimated-load.md). Set `load_source` to `estimated` on every estimated row.
15. For ACWR, ask which variant the user wants: rolling average coupled, rolling average uncoupled, or exponentially weighted moving average (EWMA).
16. Ask for the acute and chronic windows.
17. If the user has no preference, show all three and say they differ.
18. For monotony and strain, ask whether to use calendar weeks or rolling 7-day weeks, and whether to use the sample or population standard deviation (SD). Follow [references/monotony-and-strain.md](references/monotony-and-strain.md).
19. If the user has no preference, use Monday-to-Sunday calendar weeks and the sample SD. Label both as this skill's choice.
20. Count rest days as `0` in every monotony week. Report monotony and strain as missing for any week with a missing day.
21. For wellness z-scores, ask which direction each item runs (is a high number good or bad), the baseline window, and the minimum number of baseline days before a z-score is shown.
22. Ask whether the user also flags on the raw answer.
23. For a taper, ask which weeks are baseline and taper, and the volume unit. Offer the 4 full weeks before the taper as the baseline if the user has none, and label it as this skill's choice. Follow [references/taper-and-distribution.md](references/taper-and-distribution.md).
24. For an intensity distribution, ask for the input (heart rate time in zone, session RPE, or session goal), the three-zone grouping, and whether to count minutes or sessions.
25. For a recovery questionnaire, confirm the questionnaire, its version, each item's range and good end, and, for the BAM, whether the points run 0 to 4 or 1 to 5. Follow [references/recovery-questionnaires.md](references/recovery-questionnaires.md).
26. Calculate each athlete separately. Never pool athletes to build one athlete's baseline.
27. Show the formula, the method or variant name with its source (for example, session RPE, Foster et al., 2001), the window, and the units next to every result.
28. Show the acute and chronic loads with every ACWR. Put the ACWR caveat sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text.
29. Show the weekly load, the SD type, and the window with every monotony and strain value. Put the monotony caveat sentence directly under each monotony or strain table or chart, and in the same paragraph as each value in text.
30. Show the raw answer, the change in points, and the status with every wellness z-score.
31. Show the baseline weeks, the volume unit, the intensity, and the frequency with every taper reduction. Show the zone input, the grouping, and the counting unit with every distribution label. Show the questionnaire, its version, its range, and its direction with every questionnaire score.
32. Run the checks below before you answer.

## Checks before answering

Run these checks on your own result before you show it:

- Scale check: every RPE value is between 0 and 10. Ask about any value above 10, which may come from a CR100 form. Do not call it an error until the user confirms the scale.
- Unit check: duration is in minutes, session RPE load is in arbitrary units (AU), strain has the unit of its load (AU for session RPE load), and ACWR, monotony, and z-scores have no unit.
- Formula check: every result and table has its formula, variant, and units beside it. Session RPE load also names its rating scale, such as CR-10 or CR100.
- Arithmetic check: recalculate two rows by hand and show them.
- Day check: the input has one row per calendar day. Rest days hold `0`. Missing days stay missing, unless the user asked for an estimate and the row is marked `estimated`. No blank cell became `0`.
- Window check: the first rolling ACWR appears on day 28 or later, and the first EWMA ACWR on day 56 or later. Any ACWR on a missing day or the 27 days after it shows as missing. Every monotony and strain value covers 7 calendar days with no missing day. The first z-score appears only after the minimum baseline is met.
- Variant check: the ACWR variant and windows in the answer match what the user asked for.
- Caveat check: the sentence that ACWR does not predict injury sits directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text. The sentence that monotony and strain do not predict injury or illness sits the same way with each monotony or strain value. One sentence at the end of the answer is not enough. This includes any summary line you draft for the user to send to someone else.
- Monotony check: every week counts rest days as `0`, names its SD type and window, and uses one SD type throughout. A week with an SD of 0 shows `no variation`, not a number. No week with a rest day at 0 AU shows a monotony above 2.27 (sample SD) or 2.45 (population SD). Strain equals the weekly load times the unrounded monotony.
- Baseline check: each z-score baseline excludes the day being scored and uses only that athlete's data.
- Count check: count with code, not by hand. Report sessions, athletes, filled and missing ratings, athlete-days with training, rest days you added, total athlete-days, and complete athlete-days. Sessions and athletes match the input. Total athlete-days equal the athlete-days in the input plus the days you added. Complete athlete-days are athlete-days with no missing value. Copy every count in the answer from the code output.
- Direction check: the sign of each wellness z-score matches the item's scale direction.
- Raw value check: every wellness z-score shows the raw answer, the change in points, and a status.
- Taper check: every reduction names its baseline weeks and volume unit, and no baseline week with missing data entered the baseline mean.
- Distribution check: the three zone totals add up to the week's total, and "polarized" appears only when Z1 > Z3 > Z2 and the polarization index is above 2.00.
- Questionnaire check: every item's range and good end match the user's form, any flipped item is named, and no score comes from a day with a missing or out-of-range item.
- Estimate check: every estimated load is marked `estimated`, names its method, and shows its leave-one-game-out error. Weekly totals and ACWR that include an estimate say how many days are estimated. No change is judged against the noise band when either value is estimated.
- Chance check: when you flag wellness answers across a squad, flag on the total z-score or the practitioner's own raw-answer rule, not on single-item z-scores. Show each item's raw answer and change in points beside each flagged athlete. Show the number of flags expected by chance next to the number found. Keep item z-scores, labeled approximate, in the athlete detail view.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Keep to these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Never present ACWR as an injury predictor or an injury-risk score. Do not label any ACWR value as safe, a "sweet spot", or a "danger zone". Put this sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text, not once per answer: "ACWR describes how recent load compares with longer-term load. It does not predict injury." The full limits are in [references/acwr.md](references/acwr.md).
- Never present monotony or strain as an injury or illness predictor, and do not flag athletes as likely to get sick. Do not use a monotony of 2.0, or any other value, as a cut-off unless the user sets it, and label it as their choice. Put this sentence directly under each monotony or strain table or chart, and in the same paragraph as each value in text: "Monotony and strain describe how a week's load was spread and how large it was. They do not predict injury or illness." The full limits are in [references/monotony-and-strain.md](references/monotony-and-strain.md).
- Polar Team Pro's Strain is a 7-day average daily load, not the strain in this skill. Do not compare the two.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- Do not set a wellness flag cut-off on your own. Ask the user which cut-off they use, and label it as their choice. A z-score cannot show a chronic problem, so never hide the raw answer. Recommend a repeat answer or a talk with the athlete before anyone acts on a single flag.
- Do not diagnose illness, overtraining, or injury from a wellness score or a recovery questionnaire score.
- Present published taper results, such as a 41% to 60% volume cut over 2 weeks, as study findings, never as a target. Do not call one intensity distribution better than another. The coach makes every training decision.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team. A routine soreness rating on a wellness form is an input. A reported injury, pain, or symptom is not.
- Do not fill missing RPE or wellness answers with zero, an average, or the last value unless the user asks. If the user asks, name the method and show results with and without the filled values.
- Estimate load for an athlete who did not wear a device only when the user asks. Never present an estimate as a measurement.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If the `ams-data-setup` skill is installed, use its table layout. This skill works without it.

## References

Load these files when needed:

- [references/session-rpe-load.md](references/session-rpe-load.md): session RPE load, the CR-10 scale, and when to collect the rating
- [references/heart-rate-load.md](references/heart-rate-load.md): heart rate zones, Edwards, Banister, and Lucia TRIMP, and how HRmax settings change them
- [references/acwr.md](references/acwr.md): acute to chronic workload ratio, its variants, and why it does not predict injury
- [references/monotony-and-strain.md](references/monotony-and-strain.md): weekly training monotony and strain, sample versus population SD, calendar versus rolling weeks, and why they do not predict injury or illness
- [references/wellness-z-score.md](references/wellness-z-score.md): wellness answers as z-scores against the athlete's own baseline
- [references/taper-and-distribution.md](references/taper-and-distribution.md): percent volume reduction in a taper, and weekly or block intensity distribution in three zones, labeled pyramidal or polarized
- [references/recovery-questionnaires.md](references/recovery-questionnaires.md): scoring the Hooper index, Total Quality Recovery, Perceived Recovery Status, and the Brief Assessment of Mood
- [references/estimated-load.md](references/estimated-load.md): estimating TRIMP or accelerometer load from minutes played or time on ice for athletes who did not wear a device, and checking the estimate
- [references/catapult.md](references/catapult.md): how to read external load from Catapult exports
- [references/kinexon.md](references/kinexon.md): how to read external load from Kinexon exports
- [references/polar-team-pro.md](references/polar-team-pro.md): how to read heart rate, internal load, and GPS data from Polar Team Pro exports
- [references/statsports.md](references/statsports.md): how to read external load and heart rate data from STATSports Sonra exports
- [references/firstbeat-sports.md](references/firstbeat-sports.md): how to read heart rate, HRV, internal load, and recovery data from Firstbeat Sports exports and its API
