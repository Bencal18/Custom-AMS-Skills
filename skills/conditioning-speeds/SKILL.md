---
name: conditioning-speeds
description: Work out maximal aerobic speed, anaerobic speed reserve, and interval run distances from 30-15 IFT, Yo-Yo, time trial, and sprint results. You choose the percentages.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Conditioning speeds

This skill turns running test results into each athlete's reference speeds and the distances that match the percentages and durations the coach chooses. It computes. It does not choose any percentage, duration, or group for the coach.

## When to use

Use this skill when the user asks to:

- Work out maximal aerobic speed (MAS) from a time trial, such as a 2,000 m run or a 5-minute run.
- Explain why the 30-15 Intermittent Fitness Test (30-15 IFT) speed, a Yo-Yo test result, and a time trial speed differ.
- Work out anaerobic speed reserve (ASR) from MAS and a sprint or GPS top speed.
- Turn a percentage and a work time the coach picked into a distance for each athlete.
- Build a run sheet in Excel or Google Sheets from a table of test results.
- Sort athletes by speed, or put them into groups at boundaries the coach sets.
- Write a spreadsheet formula, Python code, or a Power BI or Tableau calculation for any of these.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Maximal aerobic speed (MAS), and the 30-15 IFT and Yo-Yo results that are not MAS | [references/maximal-aerobic-speed.md](references/maximal-aerobic-speed.md) |
| Anaerobic speed reserve (ASR) and speed reserve ratio | [references/anaerobic-speed-reserve.md](references/anaerobic-speed-reserve.md) |
| Interval distances, target times, and speed groups | [references/interval-distances.md](references/interval-distances.md) |

## Steps

Follow these steps in order:

1. Ask which test produced each result, if the user has not said. Name the test exactly, such as "2,000 m time trial", "5-minute run", "30-15 IFT", or "Yo-Yo intermittent recovery test level 1".
2. Load the reference file for each metric the user asks about.
3. List each input column with its unit. A time trial gives a time in s or mm:ss. A set-time run gives a distance in m. The 30-15 IFT gives a stage speed in km/h. A Yo-Yo test gives a distance in m or a level.
4. Convert every time to seconds and every speed to m/s before any calculation: km/h ÷ 3.6, and mph × 0.44704.
5. Compute each athlete's reference speed with the formula for that test in `references/maximal-aerobic-speed.md`. Keep the test name next to every speed.
6. Use one test as the reference speed for every athlete on one run sheet. If the athletes did different tests, stop and tell the user before you calculate. Do not mix MAS from a time trial, 30-15 IFT speed, and Yo-Yo results in one column.
7. Do not convert a 30-15 IFT speed or a Yo-Yo result to MAS unless the user asks. If the user asks, follow the rules in `references/maximal-aerobic-speed.md`, and name the study the conversion came from.
8. For ASR, ask where maximal sprint speed came from: a sprint test or the highest valid GPS speed. Follow `references/anaerobic-speed-reserve.md`.
9. Ask the user for every percentage and every work time. Do not suggest one. If the user asks what others use, show the study settings in `references/interval-distances.md` as examples from named studies, not as advice.
10. Calculate each distance with the formula in `references/interval-distances.md`.
11. Sort or group athletes only when the user asks. Ask the user for every group boundary.
12. Run the checks below.
13. Show the formula, the test, the test date, the percentage, the work time, and the units next to each result.

If the `sprint-testing` skill is installed, use it to get maximal sprint speed from timing gates or radar. If the `gps-running-load` skill is installed, use its high-speed running file for speed units and the highest valid GPS speed. If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures.

## Checks before answering

Run these checks on your own result before you show it:

- Test check: every speed in one column comes from the same test, and the test name sits next to it.
- Unit check: every speed is in m/s or km/h as labeled, every time is in s, and every distance is in m. A MAS above 10 m/s almost always means km/h was read as m/s.
- Range check: compare each MAS or 30-15 IFT speed with the typical ranges in `references/maximal-aerobic-speed.md`, and with the athlete's own earlier results on the same test. Flag values far outside both as "check this value". Name the population behind the range.
- Order check: for each athlete, maximal sprint speed is higher than MAS, so ASR is above 0. A 30-15 IFT speed is usually higher than a time trial MAS from the same athlete.
- Date check: show the date of every test. Show the days between the MAS test and the sprint test when you compute ASR.
- Recompute check: recompute one athlete by hand and confirm it matches your formula or code.
- Count check: the number of athletes in the result matches the input. List athletes with no result for the chosen test.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

Follow these rules before you call a change in MAS or 30-15 IFT speed real. If the `monitoring-statistics` skill is installed, use it for detail:

- Typical error (TE) is the test's noise: the SD of one athlete's repeated results when nothing real changed. Take it from a short-term retest in which no true change is expected, on the same test, surface, and protocol. `references/maximal-aerobic-speed.md` gives published figures for the 5-minute run and the 30-15 IFT, with their populations.
- Noise band for two single tests: 1.96 × √2 × TE, about 2.77 × TE. For a new value against a baseline mean of n values: 1.96 × TE × √(1 + 1/n). The same error appears in Hopkins's monitoring spreadsheet (Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm, accessed 2026-10-02). The skills use only its error formula, not its magnitude-based inference. The 95% level is a choice.
- The band assumes the true value did not change, errors are independent, TE is the same across athletes, and TE is known. When the assumptions fail, the real false-flag rate can be higher or lower than 5%.
- The 30-15 IFT moves in steps of 0.5 km/h, one stage. A change smaller than one stage cannot show.
- If the user has no TE for the test, say the change cannot be judged against noise. Tell the user to measure TE from a short-term retest.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not choose the percentage, work time, rest time, number of repetitions, or group boundaries. Show the study settings in the reference files as examples, not recommendations, and leave every choice to the coach.
- Do not call any percentage, distance, or speed safe, right, too hard, or too easy.
- Do not mix speeds from different tests in one column, one run sheet, or one trend. A change of test is not a change in fitness.
- Do not label a 30-15 IFT speed or a Yo-Yo result as MAS.
- Do not invent a conversion, threshold, or range. Use only the figures in the reference files, and name the source and population.
- Do not add a correction for turns in shuttle runs. No source in the reference files gives one. Label every distance as a straight-line distance.
- When you sort athletes, sort only to build a run sheet. Do not number athletes, label anyone best or worst, or show the sorted list in an athlete view.
- These skills cover healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not compute speeds for that athlete here. Tell the user to involve the medical team.
- Athlete data is personal data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed:

- [references/maximal-aerobic-speed.md](references/maximal-aerobic-speed.md): MAS from set-distance and set-time trials, why the 30-15 IFT and Yo-Yo results are not MAS, and why speeds from different tests must stay apart
- [references/anaerobic-speed-reserve.md](references/anaerobic-speed-reserve.md): ASR, speed reserve ratio, speed at a chosen percentage of ASR, and where maximal sprint speed comes from
- [references/interval-distances.md](references/interval-distances.md): distances and target times from a coach-chosen percentage and work time, a per-athlete run sheet from a test table, sorting, and coach-set groups
