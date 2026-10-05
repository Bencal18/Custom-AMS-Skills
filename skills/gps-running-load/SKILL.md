---
name: gps-running-load
description: Calculate total distance, metres per minute, high-speed running, and accelerations and decelerations from GPS or local positioning exports. Check thresholds, units, and settings.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
  last-tested: "not tested"
---

# GPS running load

This skill helps you calculate running load from GPS (global positioning system) or local positioning data. Local positioning is radio tracking installed in a venue. Running load is the external work an athlete does on their feet, such as distance and speed.

The skill tells the AI which formula and threshold to use, and how to check that two numbers are comparable before it compares them.

## When to use

Use this skill when the user asks to:

- Total the distance each athlete ran in a session, a week, or a match.
- Calculate metres per minute, also called relative distance.
- Calculate high-speed running, sprint distance, or distance in speed zones.
- Count accelerations and decelerations, or total their distance.
- Compare running load across athletes, positions, sessions, seasons, or devices.
- Set up a running load log in a spreadsheet, R, Python, Power BI, or Tableau from GPS or local positioning exports.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Total distance and distance per minute | [references/total-distance.md](references/total-distance.md) |
| High-speed running distance | [references/high-speed-running.md](references/high-speed-running.md) |
| Accelerations and decelerations | [references/accelerations-decelerations.md](references/accelerations-decelerations.md) |

## Steps

Follow these steps in order:

1. Ask which device and software produced the data, if the user has not said.
2. For Catapult, Kinexon, or Polar Team Pro data, load the matching device file listed under References.
3. Load the reference file for each metric the user asks about.
4. Ask for the column names, the units, and one example row with names removed. Do not guess what a column means.
5. Ask whether the file holds summary values per athlete per session, raw speed samples, or raw positions over time.
6. For raw data, ask for the sampling rate in hertz (Hz), meaning samples per second.
7. Check the sampling rate against the timestamps.
8. Confirm the speed unit.
9. Convert to metres per second (m/s) before you apply any threshold: km/h ÷ 3.6, mph × 0.44704, or ft/s × 0.3048.
10. Confirm the distance unit is metres.
11. Convert kilometres × 1,000, yards × 0.9144, and yd/min × 0.9144 to get m/min.
12. For high-speed running, ask for the speed threshold, its unit, and whether it is the same for every athlete (absolute) or set per athlete (individualized).
13. For accelerations and decelerations, ask for the threshold in m/s², the minimum time beyond the threshold, and the software or filter that produced the counts.
14. Ask for the vendor's boundary rule: does a value exactly on a threshold count?
15. If the user does not know, use one rule for speed and acceleration: count a sample at or above the lower bound and below the upper bound.
16. Say which boundary rule you used.
17. For distance per minute, ask which duration to divide by: whole session, time on field, or drill time.
18. Use one duration rule for every row.
19. For a peak period, ask for the window length and whether it is rolling or fixed.
20. Calculate each athlete and session separately. Do not pool athletes into one value unless the user asks for a group summary.
21. Before you compare two values, confirm they share the device type, the same unit for that athlete, sampling rate, software version, settings, thresholds, session type, and session duration.
22. If any of these differ or are unknown, say which, next to the comparison. A change of vendor changes the device type, software, and settings. A matching label such as `Practice` does not confirm the same session type. Ask whether the drills matched.
23. Show the formula, the variant name, the threshold, and the units next to every result.
24. Run the checks below before you answer.

## Checks before answering

Run these checks on your own result before you show it:

- Unit check: distance is in metres, not km. Speed is in m/s, or km/h as labeled. Acceleration is in m/s². Every threshold uses the same unit as the data it filters. No value in mph, yards, or ft/s is left unconverted.
- Threshold check: the threshold in the answer matches the one the user gave. Name it and the boundary rule next to the result.
- Order check: for each athlete and session, high-speed running distance is no more than total distance, and sprint distance is no more than high-speed running distance.
- Duration check: distance per minute uses the duration rule the user chose, and the duration is in minutes.
- Method check: no trend mixes distance from vendor totals, speed × time, odometer differences, or summed positions. No comparison mixes rolling and fixed peak periods. Each distance result names its method.
- Range check: compare each value with the athlete's own history on the same device and settings. For distance per minute, and for high-speed running with a matching threshold, also compare with the published figures in the reference file. Do not compare acceleration counts with published figures. Flag values far outside the comparison.
- Setting check: values compared across devices, units, software versions, or seasons share the same thresholds and settings. If they do not, or a setting is unknown, say which, next to the comparison.
- Vendor check: if a device reference file says no source supports a cross-vendor comparison of a metric, such as Kinexon `Max. Speed` or Accumulated Acceleration Load, do not show a difference column for it and do not read the direction of the difference. Show each system's values in its own column or table, and quote the reason from the reference file.
- Change check: judge any change with the rules in the next section.
- Arithmetic check: recalculate two rows by hand and show them.
- Count check: the number of athletes, sessions, and rows in the result matches the input. State the three counts in the answer.

If a check fails, say which check failed and why. Do not hide the result. If an input value fails the unit or range check, keep it out of totals and averages until the user confirms it. You may also show the result with it, labeled as an assumption.

## Judge a change over time

Follow these rules before you call a change real. If the `monitoring-statistics` skill is installed, use it for detail:

- Typical error (TE) is the measure's noise: the within-athlete error SD from a short-term test-retest in which no true change is expected. For running load, take TE from a short-term retest of the same athlete, on the same unit, in the same session type or drill, with no true change expected. Compute it on the same summary as the values you compare.
- The error figures in the reference files are between-unit or sled and circuit figures. They are not test-retest TE within one athlete. Use a between-unit figure only when the athlete changed to another unit of the same model between the values you compare. The reference files compare systems with a reference system. They give no figure you can use as one athlete's noise when the athlete changes device type or vendor. For that change, say the change cannot be judged against noise.
- Retesting on separate days is an option. It counts normal day-to-day variation as noise, so it gives a larger TE. Label it as this skill's choice, not a published rule.
- Noise band for two single values: 1.96 × √2 × TE, about 2.77 × TE. For a new value against a baseline mean of n values: 1.96 × TE × √(1 + 1/n). The second form adds the variance of the new value to the variance of the baseline mean. The same error appears in Hopkins's monitoring spreadsheet (Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm, accessed 2026-10-02). The 95% level is a choice.
- The band assumes the true value did not change, errors are independent, TE is the same across athletes and values, and TE is known. Error alone gives a change smaller than the band about 95 percent of the time. When the assumptions fail, the real false-flag rate can be higher or lower than 5%. Never call 5% a lower bound.
- When TE comes from few athletes, replace 1.96 with t at the degrees of freedom of the TE study: athletes − 1 for two trials. For 6 athletes, t(5) = 2.57. For 10, t(9) = 2.26. Never use the SD of the athlete's own baseline values as TE.
- Use 95% by default. Say it is a choice that matches common MDC95 reporting. Offer Hopkins's practical 1.5 to 2.0 × TE only with its cost: for two single values, 1.5 × TE flags 28.9% of pure-noise changes (14.4% in one direction), and 2.0 × TE flags 15.7% (7.9%).
- A change is clearly beyond the smallest worthwhile change (SWC) only when its whole interval lies beyond the SWC in the chosen direction. A change beyond the band but not clearly beyond the SWC reads: "larger than measurement error; may or may not be worthwhile". SWC = 0.2 × the between-athlete SD is a convention. It depends on how alike the squad is and is imprecise in small squads. The SD corrected for error is √(SD² − TE²).
- Across a squad, report the flags expected by chance next to the flags found: results × 5%, or × 2.5% for one direction. For 25 athletes checked in one direction, that is 0.625 a week, with a 46.9% chance of at least one. Flags in consecutive weeks against the same baseline are not independent.
- Recommend a repeat before anyone acts on one flag, because an unusual value is often followed by one closer to the athlete's usual level (regression to the mean).
- If the user has no TE, say the change cannot be judged against noise. Tell the user how to get one: a short-term retest of the same athletes, on the same units, in the same session type or drill, with no true change expected.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not label any running load value as safe, risky, too high, or too low. Report the value, the comparison, and the uncertainty.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- Do not pick a speed or acceleration threshold for the user. Show the options in the reference file and ask which one they use.
- Do not compare acceleration or deceleration counts across devices, software versions, or settings as if they were the same measure.
- Do not call a change real when it is inside the noise band.
- Do not fill missing sessions with zero or an average unless the user asks. If the user asks, name the method and show results with and without the filled values.
- Athlete data is personal data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If the `ams-data-setup` skill is installed, use its table layout. That skill sets up athlete, session, and measure tables. This skill works without it.

## References

Load these files when needed:

- [references/total-distance.md](references/total-distance.md): total distance, distance per minute, peak periods, distance from positions, and how sampling rate and device type change them
- [references/high-speed-running.md](references/high-speed-running.md): high-speed running distance, absolute and individualized thresholds, efforts, and speed units
- [references/accelerations-decelerations.md](references/accelerations-decelerations.md): acceleration and deceleration counts and distance, thresholds, minimum time beyond threshold, and reliability limits
- [references/catapult.md](references/catapult.md): how to read and transform Catapult API output and exports
- [references/kinexon.md](references/kinexon.md): how to read and transform Kinexon API output and exports
- [references/polar-team-pro.md](references/polar-team-pro.md): how to read and transform Polar Team Pro GPS and heart rate exports and API output
