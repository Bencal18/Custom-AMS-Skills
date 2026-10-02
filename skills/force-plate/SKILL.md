---
name: force-plate
description: Calculate and check results from force plate and Nordic tests, including CMJ jump height, RSI-modified, IMTP peak force, and eccentric hamstring force. Use for jump, pull, or Nordic data.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "0.1"
  last-tested: "not tested"
---

# Force plate

This skill helps you calculate, clean, and check force plate and Nordic hamstring test results. It covers raw force traces and summary exports from any device.

## When to use

Use this skill when the user asks to:

- Calculate jump height from a countermovement jump, or explain why two jump heights differ.
- Add RSI-modified to a jump export.
- Calculate or compare isometric mid-thigh pull peak force, relative force, or rate of force development.
- Summarize Nordic hamstring test results per leg, per kilogram, or left versus right.
- Write a spreadsheet formula, Python or R code, or a Power BI or Tableau calculation for any of these metrics.
- Check whether a force plate number looks right.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Countermovement jump (CMJ) height | [references/cmj-jump-height.md](references/cmj-jump-height.md) |
| Reactive strength index-modified (RSImod) | [references/rsi-modified.md](references/rsi-modified.md) |
| Isometric mid-thigh pull (IMTP) peak force | [references/imtp-peak-force.md](references/imtp-peak-force.md) |
| Eccentric hamstring force (Nordic hamstring exercise) | [references/eccentric-hamstring-force.md](references/eccentric-hamstring-force.md) |

## Steps

Follow these steps in order:

1. Ask which device and test the data came from, if the user has not said.
2. Load the device file when one exists for that device.
3. Load the reference file for each metric the user asks about.
4. Ask whether the user has the raw force trace or only a summary export, if it is not clear from the data.
5. List each input column with its unit.
6. Convert to SI units before any calculation: N, kg, m, and s.
7. Name the method or variant behind each value. Examples: takeoff velocity or flight time for jump height, net or gross for peak force, and the formula for left versus right imbalance. When the device file lists a vendor metric that matches the value, name that metric too.
8. Use one method per metric for all athletes and sessions. If the data mix methods, stop and tell the user before you calculate.
9. Ask whether to report the best trial or the mean of trials, if the user has not said. Use the same choice for every session.
10. Ask which trials the athlete or tester excluded, and why.
11. Do not drop or restore a trial without saying so. Use the same exclusion rule at every session.
12. Report how many trials you excluded per athlete.
13. Calculate the metric with the formula in the reference file. Follow its "Calculate the metric" steps.
14. Run the checks below.
15. Show the formula, the variant name, and the units next to each result.
16. Name any choice from the reference file's "What changes the number" section that applies.

If the user asks for left versus right comparisons and the `limb-symmetry` skill is installed, use it for the asymmetry formula. If it is not installed, use these defaults and name the one you used:

- Bilateral tests, where both legs push at once on two plates, such as a CMJ or IMTP: bilateral asymmetry index, (right − left) / (right + left) × 100.
- Unilateral tests, where each leg is tested on its own: percentage difference, (right − left) / max(right, left) × 100.
- Nordic hamstring test: percentage difference, as in `references/eccentric-hamstring-force.md`.

Judge any left versus right difference with the asymmetry band in `references/eccentric-hamstring-force.md`.

Keep the test conditions the same at every session: warm-up, time of day, and the athlete's training load in the day before the test. For the IMTP, the reference file recommends a standard warm-up (see `references/imtp-peak-force.md`). For the other tests, this is good practice, not a published rule. Record any change in conditions next to the result.

If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures.

## Checks before answering

Run these checks on your own result before you show it:

- Range check: compare each value with the typical range in the reference file. Flag a value as "check this value" when it falls outside the reported observed range or, where only a mean and standard deviation (SD) are given, more than 3 SD from the mean. The 3 SD line is this skill's choice, not a published rule. Name the population the range came from. For the IMTP, use the internal checks in its reference file instead.
- Population check: an injured, rehabilitating, youth, or untrained athlete can fall outside a healthy-sample range for real reasons. Do not label such a value a data error or abnormal for that reason alone.
- Unit check: confirm jump height is in m or cm and not mixed, time is in s, force is in N, and relative force is in N/kg.
- Method check: confirm every value in one column uses the same method, such as all takeoff velocity or all flight time.
- Recompute check: recompute one athlete by hand and confirm it matches your code or formula.
- Formula check: every result has its formula, variant, and units beside it, including any left-right band.
- Count check: confirm the number of athletes, sessions, trials, and legs matches the input.
- Side check: confirm left and right labels were not swapped between the export and your table.
- Change check: compare the change with the noise band, as described below. Do not use the trial-to-trial coefficient of variation from one session as the noise.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

If the `monitoring-statistics` skill is installed, use it for detail. Follow these rules before you call a change real:

- Typical error (TE) is the test's noise: the SD of one athlete's repeated scores when nothing real changed. Take it from a short-term test-retest study in which no true change is expected. Use the same protocol and the same trial summary (single trial, best of 3, or mean of 3) as the values you compare. Retesting on separate days is an option. It counts normal day-to-day variation as noise, so it gives a larger TE. Label it as a choice. When you quote a published TE, state its retest interval (same day or separate days) and its population.
- Noise band for two single tests: 1.96 × √2 × TE, about 2.77 × TE. For a new value against a baseline mean of n values: 1.96 × TE × √(1 + 1/n). The second form adds the variance of the new value to the variance of the baseline mean. The same error appears in Hopkins's monitoring spreadsheet (Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm, accessed 2026-10-02). The 95% level is a choice.
- The band assumes the athlete's true score did not change, errors are independent, TE is the same across athletes and values, and TE is known. Error alone gives a change smaller than the band about 95 percent of the time. When the assumptions fail, the real false-flag rate can be higher or lower.
- When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study: athletes − 1 for two trials. For 10 athletes, t(9) = 2.26. Never use the SD of the athlete's own baseline values as TE.
- Use 95% by default. Say it is a choice that matches common MDC95 reporting, and state the level.
- A change is clearly larger than the smallest worthwhile change (SWC) only when the change minus the band is still beyond the SWC, in the chosen direction. A change beyond the band but not clearly beyond the SWC reads: "larger than measurement error; may or may not be worthwhile". A common SWC is 0.2 × the between-athlete SD. That is a convention, not a law: it depends on how alike the squad is, and it is imprecise in small squads.
- Across a squad, report how many flags error alone would give: number of results × 5%, or × 2.5% when only one direction matters. Recommend a repeat test before anyone acts on one flag, because an unusual value is often followed by one closer to the athlete's usual level (regression to the mean).
- If the user has no TE for the test, say the change cannot be judged against noise. Tell them to measure TE from repeated baseline tests.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not diagnose an injury or predict injury from any force plate or Nordic value, imbalance, or change.
- Do not label an athlete ready, cleared, recovered, safe, injured, or at risk.
- Use published ranges only to check that data are plausible, not to rate or rank athletes. Do not apply any range or threshold as a pass or fail.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source and population.
- Do not compare values across methods, devices, postures, or arm-swing conditions without saying so.
- Do not calculate Nordic knee torque or muscle force from ankle force. If the export gives a torque, report it as given, labeled as the device's value, and say that it depends on how the knee position is set.
- Do not call a change real when it is inside the noise band.
- Do not advise whether or when an injured or rehabilitating athlete should do a maximal test. That is the clinician's decision.
- If the data note pain during a rep or trial, flag that rep and do not treat it as a valid maximum. Calculate every result without it. You may state once what the top value would be with it, labeled as not valid. Do not use it in relative force, change, or imbalance results.
- Do not quote injury-study cut-offs as targets or flags.

## References

Load these files when needed:

- [references/cmj-jump-height.md](references/cmj-jump-height.md): CMJ jump height, takeoff velocity and flight time methods, body weight, and onset detection
- [references/rsi-modified.md](references/rsi-modified.md): RSI-modified, and how it differs from drop-jump RSI
- [references/imtp-peak-force.md](references/imtp-peak-force.md): IMTP peak force, net and gross force, scaling, and rate of force development
- [references/eccentric-hamstring-force.md](references/eccentric-hamstring-force.md): eccentric hamstring force per leg, relative force, and between-limb imbalance
- [references/vald-forcedecks.md](references/vald-forcedecks.md): how to read and transform VALD ForceDecks API output and exports
- [references/vald-nordbord.md](references/vald-nordbord.md): how to read and transform VALD NordBord API output and exports
- [references/hawkin-dynamics.md](references/hawkin-dynamics.md): how to read and transform Hawkin Dynamics API output and exports, and which Hawkin metrics share a name with VALD metrics but differ
