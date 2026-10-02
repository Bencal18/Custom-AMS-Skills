---
name: velocity-based-training
description: Calculate mean concentric velocity, velocity loss in a set, and load-velocity profiles from data recorded by a bar speed device. Check the velocity type, units, and reference rep.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "0.1"
  last-tested: "not tested"
---

# Velocity-based training

This skill helps you work with bar speed data from the weight room. Velocity-based training uses how fast a bar or body moves during a lift to describe how heavy a load is for that athlete and how much they slowed down within a set. The skill tells the AI which velocity measure to use, how to calculate velocity loss, and how to check the result.

## When to use

Use this skill when the user asks to:

- Find the mean velocity, mean propulsive velocity, or peak velocity of each rep.
- Calculate velocity loss, also called velocity drop-off, within a set.
- Build a load-velocity profile or estimate a one-repetition maximum (1RM) from bar speed.
- Compare an athlete's bar speed at a fixed load across days or weeks.
- Set up a lifting log with bar speed in a spreadsheet, R, Python, Power BI, or Tableau.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Mean concentric velocity, with mean propulsive velocity, peak velocity, and load-velocity profiles | [references/mean-concentric-velocity.md](references/mean-concentric-velocity.md) |
| Velocity loss within a set | [references/velocity-loss.md](references/velocity-loss.md) |

## Steps

Follow these steps in order:

1. Ask which device and app produced the data, if the user has not said.
2. Ask whether it is a linear position transducer (a tether attached to the bar), an accelerometer, a camera, or another device.
3. For GymAware or Perch data, load the matching device file listed under References.
4. Load the reference file for each metric the user asks about.
5. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
6. Confirm which velocity each column holds: mean concentric velocity, mean propulsive velocity, or peak velocity. These are different numbers for the same rep. Stop and ask if the column name does not say.
7. Confirm velocity is in metres per second (m/s).
8. Convert cm/s by dividing by 100, and ft/s by multiplying by 0.3048.
9. Confirm the exercise, its variant, and the equipment for every row, such as free-weight back squat or Smith machine squat, and touch-and-go or paused bench press. Never mix exercises, variants, or equipment in one calculation.
10. Use the device's own per-rep values when they exist.
11. If you must recalculate from a velocity trace, state the phase start and end rule and the averaging method.
12. Label a recalculated result "recalculated".
13. Keep reps in order within each set, and keep sets in order within each session.
14. Check the rep count against the training log.
15. For velocity loss, ask whether to use the first rep or the fastest rep as the reference.
16. If the user has no preference, use the fastest rep and say so.
17. When the fastest rep is not the first, report the first-rep value beside it and flag the difference.
18. For a 1RM estimate, confirm the lift has a published 1RM velocity and a validation in the reference file.
19. Ask which 1RM velocity to use.
20. Name the equipment behind that velocity.
21. Say the estimate changes with that choice.
22. Calculate each athlete, exercise, and session separately.
23. Show the formula, the velocity measure, the reference rep, and the units next to every result. Name the measure as mean, mean propulsive, or peak velocity, not only the column name. For GymAware Conc Mean Velocity, write "mean velocity, not mean propulsive velocity".
24. Run the checks below before you answer.

## Checks before answering

Run these checks on your own result before you show it. In the answer, give each check a one-line result: pass, fail, or could not check:

- Unit check: velocity is in m/s, velocity loss is in percent, and load is in kg or percent of 1RM as labeled. No value in cm/s or ft/s is left unconverted.
- Measure check: every value in one calculation uses the same velocity measure and the same device. No calculation mixes device values with recalculated values.
- Order check: mean velocity is lower than peak velocity for every rep. Mean propulsive velocity should not be lower than mean velocity for the same rep. Flag any rep where it is.
- Range check: compare values with the figures in the reference files for the same exercise, equipment, and velocity measure, and with the athlete's own history. Flag any value far outside them.
- Reference check: velocity loss uses the reference rep the user chose, and the answer names it.
- Exercise check: no calculation mixes exercises, variants, or equipment.
- Change check: judge any change with the rules in the next section.
- Arithmetic check: recalculate one rep or one set by hand and show it.
- Count check: the number of athletes, sets, and reps in the result matches the input.
- Source check: every published figure names its source, and every 1RM velocity names its equipment.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

Follow these rules before you call a change in bar speed real. If the `monitoring-statistics` skill is installed, use it for detail:

- Typical error (TE) is the measure's noise: the within-athlete error SD from a short-term test-retest in which no true change is expected. Use a retest with the same exercise, equipment, device, velocity measure, and load. Compute it on the same summary (single rep, fastest rep, or mean of reps) as the values you compare.
- Retesting on separate days is an option. It counts normal day-to-day variation as noise, so it gives a larger TE. Label it as this skill's choice, not a published rule.
- Noise band for two single values: 1.96 × √2 × TE, about 2.77 × TE. For a new value against a baseline mean of n values: 1.96 × TE × √(1 + 1/n). The second form adds the variance of the new value to the variance of the baseline mean. The same error appears in Hopkins's monitoring spreadsheet (Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm, accessed 2026-10-02). The 95% level is a choice.
- The band assumes the true value did not change, errors are independent, TE is the same across athletes and values, and TE is known. Error alone gives a change smaller than the band about 95 percent of the time. When the assumptions fail, the real false-flag rate can be higher or lower than 5%. Never call 5% a lower bound.
- When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study: athletes − 1 for two trials. For 6 athletes, t(5) = 2.57. For 10, t(9) = 2.26. Never use the SD of the athlete's own baseline values as TE.
- Use 95% by default. Say it is a choice that matches common MDC95 reporting. Offer Hopkins's practical 1.5 to 2.0 × TE only with its cost: for two single values, 1.5 × TE flags 28.9% of pure-noise changes (14.4% in one direction), and 2.0 × TE flags 15.7% (7.9%).
- A change is clearly beyond the smallest worthwhile change (SWC) only when its whole interval lies beyond the SWC in the chosen direction. A change beyond the band but not clearly beyond the SWC reads: "larger than measurement error; may or may not be worthwhile". SWC = 0.2 × the between-athlete SD is a convention. It depends on how alike the squad is and is imprecise in small squads. The SD corrected for error is √(SD² − TE²).
- Across a squad, report the flags expected by chance next to the flags found: results × 5%, or × 2.5% for one direction. For 25 athletes checked in one direction, that is 0.625 a week, with a 46.9% chance of at least one. Flags in consecutive weeks against the same baseline are not independent.
- Recommend a repeat before anyone acts on one flag, because an unusual value is often followed by one closer to the athlete's usual level (regression to the mean).
- If the user has no TE, say the change cannot be judged against noise. Do not call a value inside or outside noise without a TE. These rules judge change over time. Do not apply them, or the repeat advice, to one set against the coach's velocity loss threshold.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not choose the athlete's load, set length, threshold for velocity loss, or the 1RM used to set percentage loads. Show the options and sources in the reference files as study settings, not recommendations, and leave the choice to the coach.
- Present any 1RM from a load-velocity profile as an estimate, with its method, its 1RM velocity, and the equipment behind that velocity. Never present it as a measured 1RM.
- Do not estimate 1RM from velocity for a lift without a published 1RM velocity and validation in the reference file. This rules out the squat, deadlift, and other lower-body lifts. Explain why, and offer the load-velocity profile without a 1RM. If a device shows an e1RM for such a lift, call it an unvalidated estimate. List other 1RM sources, such as a tested or an entered 1RM, as options, and do not tell the coach which one to use.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- Do not apply a published velocity table from one exercise, equipment, device, velocity measure, or population to another without saying so.
- Do not call a change real when it is inside the noise band.
- Do not fill missing reps or sets unless the user asks. If the user asks, name the method and show results with and without the filled values.
- Athlete data is personal data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If the `ams-data-setup` skill is installed, use its table layout. That skill sets up athlete, session, and measure tables. This skill works without it.

## References

Load these files when needed:

- [references/mean-concentric-velocity.md](references/mean-concentric-velocity.md): mean concentric velocity, mean propulsive velocity, peak velocity, calculation conventions, units, and load-velocity profiles
- [references/velocity-loss.md](references/velocity-loss.md): velocity loss within a set, first versus fastest rep, and its link to repetitions in reserve and fatigue
- [references/gymaware.md](references/gymaware.md): how to read and transform GymAware RS and FLEX data (owned by VALD)
- [references/perch.md](references/perch.md): how to read and transform Perch camera-based velocity data (owned by Catapult)
