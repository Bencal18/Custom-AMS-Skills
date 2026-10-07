---
name: heart-rate-and-sleep
description: Trend HRV (ln rMSSD), submaximal heart rate tests, heart rate recovery, and sleep against each athlete's baseline. Checks readings per week, test conditions, and device scores.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Heart rate and sleep

This skill helps you trend morning heart rate variability (HRV), submaximal heart rate tests, heart rate recovery, and sleep for each athlete against their own baseline. Heart rate is in beats per minute (bpm). Total sleep time (TST) is the time asleep in a night. SD means standard deviation. It works with chest straps, apps, rings, wristbands, and sleep diaries, from any vendor.

## When to use

Use this skill when the user asks to:

- Add a 7-day rolling ln rMSSD, or its coefficient of variation, to morning HRV readings.
- Show whether an athlete's HRV this week sits inside their normal range.
- Explain why one low HRV reading differs from the weekly trend.
- Calculate exercise heart rate as a percentage of maximum from a fixed submaximal run or drill.
- Calculate 60-second heart rate recovery after a submaximal test.
- Flag tests run with a different drill, warm-up, time of day, or heat.
- Trend total sleep time, sleep efficiency, sleep midpoint, and how regular sleep timing is, with nap time in a separate column.
- Explain what a wearable's recovery, readiness, or sleep score means, and whether two devices can be compared.
- Write a spreadsheet formula, Python or R code, or a Power BI or Tableau calculation for any of these.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| ln rMSSD, its 7-day rolling mean and CV, weekly means, and the athlete's normal band | [references/hrv-trends.md](references/hrv-trends.md) |
| Submaximal exercise heart rate (HRex) as % HRmax, and 60 s heart rate recovery (HRR60) | [references/submaximal-heart-rate.md](references/submaximal-heart-rate.md) |
| Total sleep time, sleep efficiency, sleep midpoint, and midpoint regularity | [references/sleep-trends.md](references/sleep-trends.md) |

This skill has these device references:

| Device | Reference file |
|---|---|
| WHOOP | [references/whoop.md](references/whoop.md) |
| Oura | [references/oura.md](references/oura.md) |

## Steps

Follow these steps in order:

1. Ask which device, app, or form the data came from, if the user has not said.
2. Load the device reference when one exists for that device. This skill has references for WHOOP and Oura.
3. Load the reference file for each metric the user asks about.
4. List each input column with its unit and, for times, whether it is a clock time or a full date and time.
5. Confirm one device per athlete in each trend. If an athlete changed device, stop and tell the user before you calculate across the change.
6. For HRV, confirm the reading conditions: time after waking, position, recording length, and morning reading or overnight. Do not mix morning and overnight HRV.
7. For HRV, agree with the user what makes a reading valid.
8. For a submaximal test, record the `test_drill` code, warm-up, time of day, temperature, and recovery position for every test.
9. For a submaximal test, confirm the HRmax for each athlete and its source. If the `load-and-wellness` skill is installed, follow the HRmax section of its heart rate load reference.
10. For sleep, date each night by the into-bed time minus 12 hours, and convert times to minutes since noon on that date before any arithmetic.
11. Build a full calendar of days or nights per athlete. Leave missing days blank. Never fill them with 0 or the previous value.
12. Calculate each metric with the formula in its reference file. Follow its "Calculate the metric" steps.
13. Apply the minimum counts: 3 valid HRV readings in a 7-day window, 60 heart rate samples in the HRex window, and 8 nights in a 14-night window for sleep regularity.
14. Build each athlete's band from their own prior values, as the reference file describes.
15. Run the checks below.
16. Show the formula, the window, the count, the band type, and the units next to each result.
17. Name any choice from the reference file's "What changes the number" section that applies.

If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures.

If the data come from a device that has a reference in the `load-and-wellness` or `gps-running-load` skill, use the field meanings in that device reference. Check whether a vendor's heart rate recovery field uses the same method as HRR60 in this skill.

## Checks before answering

Run these checks on your own result before you show it:

- Count check: confirm each HRV 7-day value has at least 3 readings, each HRex has a full 60 s window, and each sleep SD has at least 8 nights. Confirm the number of athletes and days matches the input.
- Window check: confirm rolling windows count calendar days or nights, not rows.
- Baseline check: confirm today, this week, or tonight is not in its own baseline.
- Unit check: confirm rMSSD is in ms before the log, heart rate is in bpm, and sleep times are in minutes.
- Order check: confirm ln rMSSD was taken for each day before averaging.
- Range check: flag ln rMSSD outside about 2 to 6, HRex at or above 100% HRmax, a negative HRR60, efficiency above 100%, or TST longer than time in bed. These limits are this repository's plausibility checks, not published ranges.
- Conditions check: confirm every compared submaximal test used the same `test_drill`. List tests with changed conditions.
- Device check: confirm each trend uses one device and one app version.
- Nap check: confirm total sleep time holds the main sleep only, and nap time sits in its own column.
- Recompute check: recompute one athlete by hand and confirm it matches your code or formula.

If a check fails, say which check failed and why. Do not hide the result.

## Judge a change over time

If the `monitoring-statistics` skill is installed, use it to judge change. Follow these rules before you call a change real:

- For a band from the athlete's own history, use the usual-variation band, `baseline_mean ± t(n − 1) × baseline_SD × √(1 + 1/n)`. It holds real variation as well as error, so never call it noise.
- For HRV, build the band from prior weekly means, not overlapping rolling means.
- For a noise band, use a typical error (TE) from a retest with the same protocol: 1.96 × √2 × TE for two single tests. The 95% level is a choice.
- Expect large noise in heart rate recovery. Published figures differ by source. See `references/submaximal-heart-rate.md`.
- Show published bands, such as 0.5 × SD for HRV, only as study settings, with the source. Never present them as targets or as rules for training.
- Report how many flags chance alone would give across a squad: number of results × 5%, or × 2.5% when only one direction matters.
- If the user has no TE and too few values for a band, say the change cannot be judged yet.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- Do not label an athlete ready, recovered, fatigued, overreached, cleared, safe, injured, ill, or at risk from any HRV, heart rate, or sleep value.
- Do not interpret heart rate, heart rhythm, or HRV for heart health. Do not screen for sleep disorders. Do not detect illness.
- If a value or a note suggests a health problem, or the user asks whether an athlete has a medical condition, stop. Tell the user to involve the medical team. Do not analyze it further here.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- Do not compare HRV, sleep, or scores between devices, or between athletes on different devices.
- Do not treat a vendor's recovery, readiness, or sleep score as a measurement. Say that its formula is not published.
- Do not compare submaximal tests with different drills.
- Do not call a change real when it is inside the noise band.

## References

Load these files when needed:

- [references/hrv-trends.md](references/hrv-trends.md): ln rMSSD, the 7-day rolling mean and CV, weekly means, the minimum of 3 readings, measurement conditions, and the athlete's normal band
- [references/submaximal-heart-rate.md](references/submaximal-heart-rate.md): HRex as % HRmax, HRR60, test conditions, the drill flag, and test variability
- [references/sleep-trends.md](references/sleep-trends.md): total sleep time, efficiency, midpoint, regularity, clock times across midnight, and device differences
- [references/whoop.md](references/whoop.md): how to read WHOOP exports and API output
- [references/oura.md](references/oura.md): how to read Oura exports and API output
