---
name: sprint-testing
description: Calculate sprint profiles from splits, radar, or GPS, change of direction deficit from 505 and 10 m times, and repeated sprint decrement. Checks timing, start method, and units.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Sprint testing

This skill helps you turn sprint timing data into sprint profiles, change of direction deficits, and repeated sprint scores. It works with timing gates, radar or laser guns, and GPS, from any vendor.

## When to use

Use this skill when the user asks to:

- Build a sprint profile, or a force-velocity profile, from split times, a radar or laser trace, or GPS speed.
- Calculate maximal sprinting speed, tau, maximal acceleration, F0, V0, Pmax, or the ratio of force.
- Add change of direction deficit for each side from 505 and 10 m sprint times.
- Compare left and right turning in the 505.
- Score a repeated sprint test with percent decrement, best time, and mean time.
- Write a spreadsheet formula, Python or R code, or a Power BI or Tableau calculation for any of these.
- Check whether a sprint result looks right.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Sprint profile: MSS, tau, MAC, F0, V0, Pmax, RF, and DRF | [references/sprint-profile.md](references/sprint-profile.md) |
| Change of direction deficit and its side-to-side difference | [references/change-of-direction-deficit.md](references/change-of-direction-deficit.md) |
| Repeated sprint scores: best time, mean time, and percent decrement | [references/repeated-sprint.md](references/repeated-sprint.md) |

## Steps

Follow these steps in order:

1. Ask which device the data came from, if the user has not said: timing gates, radar or laser, or GPS.
2. Load the reference file for each metric the user asks about.
3. List each input column with its unit.
4. Convert to SI units before any calculation: m, s, m/s, and kg. Convert yards × 0.9144 and ms ÷ 1000.
5. Ask how each sprint started, if the user has not said: the stance, the distance from the front foot to the first gate, and what started the clock.
6. For a sprint profile, ask which time correction to use: none, a fixed value, or an estimated value. Use one choice for every athlete and session.
7. For a change of direction deficit, confirm that the 10 m sprint and the 505 used the same start in the same session. If not, stop and tell the user before you calculate.
8. For a repeated sprint test, record the protocol: distance, number of sprints, recovery time, and recovery type.
9. Ask whether to use the best trial or the mean of trials, if the user has not said. Use the same choice for every session.
10. Ask which trials or sprints the tester excluded, and why.
11. Do not drop or restore a trial without saying so. Report how many trials you excluded per athlete.
12. Calculate the metric with the formula in the reference file. Follow its "Calculate the metric" steps.
13. Run the checks below.
14. Show the formula, the variant, and the units next to each result. For a sprint profile, also show the time correction, the fit method, and the air settings.
15. Name any choice from the reference file's "What changes the number" section that applies.

Keep the test conditions the same at every session: warm-up, surface, footwear, gate height, start, and time of day. Record any change next to the result. This is good practice, not a published rule.

If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures.

## Checks before answering

Run these checks on your own result before you show it:

- Range check: compare each value with the typical range in the reference file. Name the population and protocol the range came from.
- Population check: a youth or untrained athlete can fall outside a published range for real reasons. Do not label such a value a data error for that reason alone.
- Unit check: confirm distance in m, time in s, speed in m/s, and body mass in kg.
- Start check: confirm every sprint in one comparison used the same start and time correction.
- Fit check: for a sprint profile, show the residual at every split and look for a pattern, as `references/sprint-profile.md` describes.
- Sign check: a COD deficit and a percent decrement should be positive. A negative value points to a start, label, or entry problem.
- Recompute check: recompute one athlete by hand and confirm it matches your code or formula.
- Count check: confirm the number of athletes, trials, sides, and sprints matches the input and the protocol.
- Side check: confirm left and right 505 labels were not swapped.
- Change check: compare any change with the test's noise band, as below.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

If the `monitoring-statistics` skill is installed, use it to judge change. Follow these rules before you call a change real:

- Use a typical error (TE) from a retest with the same protocol, the same start, and the same trial summary.
- Use the noise band 1.96 × √2 × TE for two single tests, or 1.96 × TE × √(1 + 1/n) for a new value against a baseline mean of n tests. The 95% level is a choice.
- Expect large relative noise in derived scores. The COD deficit and the percent decrement both carry a large coefficient of variation. See `references/change-of-direction-deficit.md` and `references/repeated-sprint.md` for the figures and their sources.
- If the user has no TE for the test, say the change cannot be judged against noise. Tell them to measure TE from repeated baseline tests.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not diagnose an injury or predict injury from any sprint value, deficit, asymmetry, or change.
- Do not label an athlete ready, cleared, recovered, safe, injured, or at risk.
- Do not prescribe training from a profile. Present any published idea about training as a study finding, never as advice.
- Use published ranges only to check that data are plausible, not to rate or rank athletes. Do not apply any range, band, or asymmetry line as a pass or fail.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source and population.
- Do not compare values across start methods, time corrections, fit methods, devices, or protocols without saying so.
- Present F0, V0, Pmax, and RF as model estimates, not measured forces.
- Do not compute a pro-agility (5-10-5) deficit unless the user asks. If they ask, say that no validated deficit was found and name the formula.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.

## References

Load these files when needed:

- [references/sprint-profile.md](references/sprint-profile.md): sprint acceleration and force-velocity profile from split times, radar, laser, or GPS, with time correction and air resistance
- [references/change-of-direction-deficit.md](references/change-of-direction-deficit.md): 505 change of direction deficit per side, and the side-to-side difference
- [references/repeated-sprint.md](references/repeated-sprint.md): percent decrement, fatigue index, best time, and mean time for repeated sprint tests
