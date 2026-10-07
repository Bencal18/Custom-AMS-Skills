---
name: sport-specific-counts
description: Total and trend sport-specific counts such as pitches, throws, jumps, swim distance, and bowling overs from logs or sensors. Checks what each count includes and misses.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Sport-specific counts

This skill helps you total and track the actions that many sports count instead of distance run: pitches and throws, jumps, swim distance, and balls bowled. It shows what each count includes and what it misses, so a total is never read as more complete than it is.

## When to use

Use this skill when the user asks to:

- Total pitch counts, bullpen pitches, warm-up throws, or all throws per day, week, or rolling window.
- Show how much of a pitcher's throwing the game pitch count misses.
- Read throw counts or arm-sensor values from an arm-worn sensor.
- Compare a pitch or throw count with a limit the coach sets.
- Total jumps per player from a jump sensor or video, or add up jump heights.
- Check how well a jump sensor's count agrees with video.
- Total swim distance by week, stroke, or intensity zone, and convert yards to meters.
- Total balls and overs for cricket bowlers in matches and training.
- Write a spreadsheet formula, Python code, or a Power BI or Tableau calculation for any of these.
- Check whether a count total looks right.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Daily, weekly, and rolling totals, and zeros versus missing days, for every count | [references/count-totals.md](references/count-totals.md) |
| Pitch counts, throw counts, and arm-sensor values | [references/throwing-counts.md](references/throwing-counts.md) |
| Jump counts, jump height sums, and sensor versus video agreement | [references/jump-counts.md](references/jump-counts.md) |
| Swim distance by stroke and zone, and cricket balls and overs | [references/swim-and-bowling-volume.md](references/swim-and-bowling-volume.md) |

## Steps

Follow these steps in order:

1. Ask which sport and which counts the user has, if they have not said.
2. Ask where each count came from: a scorebook, a coach or observer tally, video, a sensor, a swim log, or the athlete's own report.
3. Load [references/count-totals.md](references/count-totals.md) and the reference file for each sport.
4. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
5. List every count type separately, such as game pitches, bullpen pitches, warm-up throws, and sensor throws. Keep each in its own column or measure.
6. Do not add a sensor count to a logged count of the same actions. The sensor already counts them.
7. Label self-reported counts as self-reported.
8. Convert units before any total: yards to meters for swimming, and cm to m for jump heights.
9. For cricket, ask how overs are written before you convert them to balls.
10. Build one row per athlete per calendar day for each count type.
11. Put `0` on days with no activity of that type.
12. Leave a day blank when activity happened but no count was recorded, or when a sensor was not worn.
13. Mark ill, unavailable, or modified-training days in a separate column.
14. Calculate daily, weekly, and rolling totals with [references/count-totals.md](references/count-totals.md). Use Monday-to-Sunday weeks and 7-day and 28-day windows unless the user names others. Label these as this skill's choice.
15. Report every incomplete weekly or rolling total with the days it covers, such as "6 of 7 days".
16. State what each count includes and misses, from the "What each count misses" section of the reference file.
17. If the user gives a limit, compare only the matching count type with it, and report the count, the limit, and the difference in plain words.
18. Show the count type, the source, the unit, and the window next to every total.
19. Run the checks below.

If the `load-and-wellness` skill is installed, it covers rolling windows and acute and chronic loads in more detail. This skill uses the same 7-day and 28-day windows and the same zero and missing-day rules. If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures.

## Checks before answering

Run these checks on your own result before you show it:

- Count type check: every total names one count type and one source. No column mixes types, such as game pitches on some days and sensor throws on others.
- Double count check: no sensor total was added to a logged total of the same actions.
- Day check: each athlete has one row per calendar day. Rest days hold `0`. Missing days stayed missing. No blank cell became `0`.
- Window check: no complete rolling 7-day total appears before day 7, and no 28-day total before day 28. Each window covers calendar days, not rows.
- Coverage check: every incomplete total shows its recorded days.
- Unit check: swim distance is in meters with the pool unit named, jump heights are in meters, and counts are whole numbers.
- Overs check: no part-over value is above 5, and overs written as `4.3` were not read as a decimal.
- Device check: every arm-sensor or jump-sensor value in one comparison comes from one device and one placement.
- Recompute check: recompute one daily total, one weekly total, and one rolling total by hand.
- Count check: count with code, not by hand. Report athletes, sessions, athlete-days, rest days, missing days, and complete weeks. Copy every count in the answer from the code output.
- Limit check: every limit came from the user and is named as theirs.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

Follow these rules before you describe a change:

- Compare totals only within one athlete, one count type, one source, and one device and placement.
- Compare only complete weeks or complete windows. If either is incomplete, say so, and give the recorded days.
- A count total is not a test score. It changes mostly because the plan changed. Report the change in counts and in percent, and name the weeks compared. Do not call a change in a count total real, meaningful, or significant.
- If the user asks whether a week is unusual for that athlete, use the usual-variation band in the `monitoring-statistics` skill. Say that the band holds planned changes as well as noise, so it is not a measurement-error band.
- For a value measured per action, such as mean jump height, use the typical error and noise band rules in the `monitoring-statistics` skill. If the user has no typical error for that device and setting, say the change cannot be judged against noise.
- A change between two sources, such as from self-report to video, or from one sensor to another, is a change in method. Do not report it as a change in the athlete.

## Decline injury-risk requests

Governing bodies publish age-based pitch count limits as injury-prevention rules. Most throwing and bowling workload research studies injury. This skill uses that research only for how to count.

If the user asks whether a count puts an athlete at risk of injury, asks for a safe count, asks how many rest days to give, or asks whether an athlete is ready to throw, decline that part. Use words like these:

> I can't judge injury risk or recommend rest days from counts. I can show this athlete's counts by type, their weekly and rolling totals, what the counts miss, and how they compare with any limit you set.

Then offer that count report. Do not soften the decline into a hint, such as calling a total "high", "a spike", "safe", or "concerning".

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not predict injury, fatigue, or readiness from any count, total, change, or arm-sensor value.
- Do not supply a pitch count limit, a throw limit, a jump limit, a bowling limit, or a rest-day rule. Use only a limit the user gives, and label it as theirs.
- Do not label an athlete or a total as safe, risky, high, low, overloaded, ready, or cleared.
- Show published figures as the settings of single studies, never as ranges to judge an athlete or as recommendations.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source and population.
- Do not compare arm-sensor values across placements, devices, or vendors. Do not compare jump heights across devices.
- Do not present a self-reported count as an exact count.
- Do not fill a missing day with 0, an average, or the last value unless the user asks. If the user asks, name the method and show results with and without the filled values.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed:

- [references/count-totals.md](references/count-totals.md): daily, weekly, and rolling totals, zeros versus missing days, and spreadsheet, Power BI, Tableau, and Python versions
- [references/throwing-counts.md](references/throwing-counts.md): game, bullpen, warm-up, and practice throw counts, self-reported counts, arm-sensor values, and comparing a count with a coach's limit
- [references/jump-counts.md](references/jump-counts.md): jump counts from sensors or video, jump height sums, and checking a sensor against video
- [references/swim-and-bowling-volume.md](references/swim-and-bowling-volume.md): swim distance by stroke and zone, yards and meters, and cricket balls and overs
