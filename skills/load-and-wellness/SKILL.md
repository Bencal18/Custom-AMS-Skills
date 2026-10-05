---
name: load-and-wellness
description: Calculate session RPE load, heart rate load (TRIMP), ACWR, and wellness z-scores from training logs, wellness forms, heart rate, or GPS exports. Shows the formula and checks each result.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Load and wellness

This skill helps you calculate training load from athlete effort ratings, compare recent load with longer-term load, and turn daily wellness answers into scores against each athlete's own normal. It tells the AI which formula variant to use, what the result means, and what it cannot tell you.

## When to use

Use this skill when the user asks to:

- Work out session RPE load, daily load, or weekly load from RPE and minutes.
- Work out heart rate load (TRIMP) or time in heart rate zones from heart rate data.
- Calculate an acute to chronic workload ratio, an acute load, or a chronic load.
- Compare rolling averages with exponentially weighted moving averages for load.
- Flag a wellness answer that is unusual for that athlete.
- Turn sleep, soreness, fatigue, stress, or mood scores into z-scores.
- Set up a load and wellness log in a spreadsheet, R, Python, Power BI, or Tableau.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Session RPE load | [references/session-rpe-load.md](references/session-rpe-load.md) |
| Heart rate load (TRIMP) and time in zones | [references/heart-rate-load.md](references/heart-rate-load.md) |
| Acute to chronic workload ratio (ACWR) | [references/acwr.md](references/acwr.md) |
| Wellness z-score | [references/wellness-z-score.md](references/wellness-z-score.md) |

## Steps

Follow these steps in order:

1. Ask which form, app, or device the data came from, if the user has not said.
2. For Catapult, Kinexon, Polar Team Pro, or Firstbeat Sports data, load the matching device file listed under References.
3. Load the reference file for each metric the user asks about.
4. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
5. Confirm the RPE scale. Session RPE load uses the 0 to 10 category ratio scale (CR-10).
6. Stop and ask if the values look like the 6 to 20 scale.
7. Ask about values above 10 before you call them errors: the form may use the Borg CR100 scale.
8. Confirm duration is in minutes.
9. Convert hours or `hh:mm` text to minutes before you multiply.
10. Build one row per athlete per calendar day for any rolling calculation.
11. Put `0` on days with no training.
12. Put a missing value on days when training happened but no rating was recorded.
13. Mark injured, ill, or modified-training days in a separate column.
14. For ACWR, ask which variant the user wants: rolling average coupled, rolling average uncoupled, or exponentially weighted moving average (EWMA).
15. Ask for the acute and chronic windows.
16. If the user has no preference, show all three and say they differ.
17. For wellness z-scores, ask which direction each item runs (is a high number good or bad), the baseline window, and the minimum number of baseline days before a z-score is shown.
18. Ask whether the user also flags on the raw answer.
19. Calculate each athlete separately. Never pool athletes to build one athlete's baseline.
20. Show the formula, the method or variant name with its source (for example, session RPE, Foster et al., 2001), the window, and the units next to every result.
21. Show the acute and chronic loads with every ACWR. Put the ACWR caveat sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text.
22. Show the raw answer, the change in points, and the status with every wellness z-score.
23. Run the checks below before you answer.

## Checks before answering

Run these checks on your own result before you show it:

- Scale check: every RPE value is between 0 and 10. Ask about any value above 10, which may come from a CR100 form. Do not call it an error until the user confirms the scale.
- Unit check: duration is in minutes, session RPE load is in arbitrary units (AU), and ACWR and z-scores have no unit.
- Formula check: every result and table has its formula, variant, and units beside it. Session RPE load also names its rating scale, such as CR-10 or CR100.
- Arithmetic check: recalculate two rows by hand and show them.
- Day check: the input has one row per calendar day. Rest days hold `0`. Missing days stay missing. No blank cell became `0`.
- Window check: the first rolling ACWR appears on day 28 or later, and the first EWMA ACWR on day 56 or later. Any ACWR on a missing day or the 27 days after it shows as missing. The first z-score appears only after the minimum baseline is met.
- Variant check: the ACWR variant and windows in the answer match what the user asked for.
- Caveat check: the sentence that ACWR does not predict injury sits directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text. One sentence at the end of the answer is not enough. This includes any summary line you draft for the user to send to someone else.
- Baseline check: each z-score baseline excludes the day being scored and uses only that athlete's data.
- Count check: count with code, not by hand. Report sessions, athletes, filled and missing ratings, athlete-days with training, rest days you added, total athlete-days, and complete athlete-days. Sessions and athletes match the input. Total athlete-days equal the athlete-days in the input plus the days you added. Complete athlete-days are athlete-days with no missing value. Copy every count in the answer from the code output.
- Direction check: the sign of each wellness z-score matches the item's scale direction.
- Raw value check: every wellness z-score shows the raw answer, the change in points, and a status.
- Chance check: when you flag wellness answers across a squad, show the number of flags expected by chance next to the number found.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Keep to these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Never present ACWR as an injury predictor or an injury-risk score. Do not label any ACWR value as safe, a "sweet spot", or a "danger zone". Put this sentence directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text, not once per answer: "ACWR describes how recent load compares with longer-term load. It does not predict injury." The full limits are in [references/acwr.md](references/acwr.md).
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- Do not set a wellness flag cut-off on your own. Ask the user which cut-off they use, and label it as their choice. A z-score cannot show a chronic problem, so never hide the raw answer. Recommend a repeat answer or a talk with the athlete before anyone acts on a single flag.
- Do not diagnose illness, overtraining, or injury from a wellness score.
- Do not fill missing RPE or wellness answers with zero, an average, or the last value unless the user asks. If the user asks, name the method and show results with and without the filled values.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If the `ams-data-setup` skill is installed, use its table layout. This skill works without it.

## References

Load these files when needed:

- [references/session-rpe-load.md](references/session-rpe-load.md): session RPE load, the CR-10 scale, and when to collect the rating
- [references/heart-rate-load.md](references/heart-rate-load.md): heart rate zones, Edwards, Banister, and Lucia TRIMP, and how HRmax settings change them
- [references/acwr.md](references/acwr.md): acute to chronic workload ratio, its variants, and why it does not predict injury
- [references/wellness-z-score.md](references/wellness-z-score.md): wellness answers as z-scores against the athlete's own baseline
- [references/catapult.md](references/catapult.md): how to read external load from Catapult exports
- [references/kinexon.md](references/kinexon.md): how to read external load from Kinexon exports
- [references/polar-team-pro.md](references/polar-team-pro.md): how to read heart rate, internal load, and GPS data from Polar Team Pro exports
- [references/firstbeat-sports.md](references/firstbeat-sports.md): how to read heart rate, HRV, internal load, and recovery data from Firstbeat Sports exports and its API
