# WHOOP metrics

WHOOP makes a wrist or body-worn strap that records heart rate, heart rate variability, sleep, and movement around the clock, and scores them in the WHOOP app. This page covers every metric that the WHOOP API v2 returns for cycles, recovery, sleep, workouts, and body values, and uses public sources only. Checked against: the WHOOP API v2 OpenAPI file and Developer Platform pages (changelog entry 2026-09-23), and WHOOP Support articles, 2026-10-07.

WHOOP is a trademark of its owner. This repository is not affiliated with or endorsed by WHOOP.

For how to pull and reshape the data, see the [WHOOP device reference](../../skills/heart-rate-and-sleep/references/whoop.md).

## How to read this page

This page has summary tables, then one block for each metric. Each metric block is a short list with these fields:

- WHOOP name, API field, and unit: the name in the app, the field in the API, and the unit WHOOP states.
- What it measures: one plain sentence.
- Window or phase: the part of the day or night the value covers.
- Calculation: WHOOP's description in paraphrase, then the formula. The formula is the one WHOOP publishes, marked as a restatement, or "Not published".
- Defaults: settings and thresholds, each with a source.
- Inputs, Units, and Variants: what goes in, what comes out, and the forms the metric takes.
- Comparison with standard methods or other vendors: a comparison only where a source supports one.
- What changes the number: settings, data quality, and device factors.
- Sources: links to the vendor documents behind the block.

Follow these rules when you use the blocks:

- Recovery, Strain, Sleep Performance, Sleep Consistency, and Sleep Need are proprietary WHOOP scores. Report them as WHOOP gives them. Never recompute them.
- "Not published" means WHOOP gives no formula or detail in the sources read. "Not confirmed" means a source was blocked or two sources disagree.
- A formula marked "restatement" is a standard definition or a rewrite of a WHOOP statement for this page. WHOOP does not print it as a formula.
- Code font marks API field names.
- In the summary tables, "Yes" means WHOOP publishes the calculation. "Partly" means WHOOP publishes some of it. "Not published" means WHOOP does not publish the calculation.

## Areas and metric counts

The table lists each area, the number of metric blocks in this page, and the number of API fields that those blocks cover:

| Area | Metric blocks | API fields covered |
|---|---|---|
| Recovery and HRV | 5 | 5 |
| Sleep | 7 | 16 |
| Strain and heart rate | 7 | 16 |
| Movement | 2 | 4 |
| Total | 21 | 41 |

Identifiers, time fields, and status flags are listed in [Context fields that are not metrics](#context-fields-that-are-not-metrics).

## Settings and data conditions that change many metrics

These conditions change many metrics at once. Check them first when a number looks wrong:

- Calibration. A new member's Recovery is not yet reliable for a few days. The `user_calibrating` flag shows this ([Get Current Recovery Score](https://developer.whoop.com/docs/tutorials/get-current-recovery-score)).
- Physiological cycle. WHOOP counts days from sleep to sleep, not from midnight to midnight. One cycle has one Recovery ([Cycle](https://developer.whoop.com/docs/developing/user-data/cycle), [WHOOP Cycles help](https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US)).
- Sleep edits. Editing a sleep makes WHOOP calculate Recovery again ([WHOOP 101](https://developer.whoop.com/docs/whoop-101)). Merging a nap into a sleep also changes Recovery ([WHOOP Cycles help](https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US)).
- Maximum and resting heart rate. Heart rate zones use heart rate reserve. Members can edit maximum heart rate. The estimation method, said to be the Gellish formula adjusted from recorded peaks, is Not confirmed (support page not readable by automated check on 2026-10-07). Monthly zone updates from resting heart rate are Not confirmed (support page not readable by automated check on 2026-10-07) ([Max heart rate help](https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US)).
- Device generation. SpO2 and skin temperature need WHOOP 4.0 or later ([OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json)). WHOOP says Strain can read slightly higher or lower on WHOOP 5.0 or MG than on WHOOP 4.0, because of sensor and algorithm changes ([Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US)).
- Algorithm updates. WHOOP changed Sleep Performance from sleep against need alone to a score with four parts ([Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)). Record the date of any such change in your notes.
- Logged strength work. A muscular load part of Strain, and its link to logged exercises, is Not confirmed (support page not readable by automated check on 2026-10-07) ([Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US)).
- Overlapping activities. An activity that overlaps a sleep can stop the sleep from being processed ([WHOOP Cycles help](https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US)).

## API access

WHOOP ties data to OAuth scopes and limits how many members an app can connect. The sources state these rules:

| Rule | What WHOOP states | Source |
|---|---|---|
| Developer account | You need a WHOOP membership to develop an app. | [Overview](https://developer.whoop.com/docs/developing/overview) |
| Member limit | Sandbox 10, Build 100, Growth 1,000, Scale 5,000, then Production with no limit. You request tiers one at a time. | [App Approval](https://developer.whoop.com/docs/developing/app-approval) |
| Scopes | `read:recovery`, `read:cycles`, `read:sleep`, `read:workout`, `read:body_measurement`, `read:profile`, and `offline` for a refresh token | [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [OAuth](https://developer.whoop.com/docs/developing/oauth) |
| Rate limits | 100 requests per minute and 10,000 per day by default | [Rate limiting](https://developer.whoop.com/docs/developing/rate-limiting) |
| Page size | 10 records by default, 25 at most | [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json) |
| Webhooks | Sleep, workout, and Recovery events. None for cycles or body values. | [Webhooks](https://developer.whoop.com/docs/developing/webhooks/) |
| Member export | Several CSV files, per the support page. The file list, the menu steps, the 24-hour email delivery, and the 7-day link expiry are Not confirmed (support page not readable by automated check on 2026-10-07). | [Export help](https://support.whoop.com/s/article/How-to-Export-Your-Data) |
| Team platform | WHOOP Unite. Its help pages need a login. Not confirmed. | None |

## Summary tables

### Recovery and HRV summary

This table lists the metrics in the Recovery and HRV area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Heart rate variability](#heart-rate-variability) | Beat-to-beat variation of heart rhythm during sleep | ms | Partly |
| [Resting heart rate](#resting-heart-rate) | Heart rate at rest during sleep | bpm | Not published |
| [Recovery score](#recovery-score) | WHOOP's readiness score for the day | % (0 to 100) | Not published |
| [Blood oxygen](#blood-oxygen) | Oxygen saturation during sleep | % | Not published |
| [Skin temperature](#skin-temperature) | Skin temperature during sleep | degrees C | Not published |

### Sleep summary

This table lists the metrics in the sleep area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Sleep stage durations](#sleep-stage-durations) | Time in bed, awake, in each stage, and with no data | ms | Not published |
| [Sleep efficiency](#sleep-efficiency) | Share of time in bed spent asleep | % | Yes |
| [Sleep Performance](#sleep-performance) | WHOOP's sleep score | % | Partly |
| [Sleep Consistency](#sleep-consistency) | How regular sleep and wake times are | % | Not published |
| [Sleep Need](#sleep-need) | How much sleep WHOOP says the member needs | ms | Partly |
| [Respiratory rate](#respiratory-rate) | Breathing rate during sleep | breaths per minute | Not published |
| [Disturbances and sleep cycles](#disturbances-and-sleep-cycles) | Number of disturbances and of sleep cycles | count | Not published |

### Strain and heart rate summary

This table lists the metrics in the Strain and heart rate area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Day Strain](#day-strain) | Load over a whole cycle | 0 to 21 | Not published |
| [Activity Strain](#activity-strain) | Load in one workout | 0 to 21 | Not published |
| [Average and maximum heart rate](#average-and-maximum-heart-rate) | Mean and peak heart rate in a cycle or workout | bpm | Not published |
| [Time in heart rate zones](#time-in-heart-rate-zones) | Time in zones 0 to 5 during a workout | ms | Partly |
| [Percent recorded](#percent-recorded) | Share of a workout with heart rate data | % | Not published |
| [Energy](#energy) | Estimated energy used | kJ | Not published |
| [Maximum heart rate setting](#maximum-heart-rate-setting) | The member's maximum heart rate in WHOOP | bpm | Partly |

### Movement summary

This table lists the metrics in the movement area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Steps](#steps) | Steps in a cycle | count | Not published |
| [Workout distance and altitude](#workout-distance-and-altitude) | Distance, height climbed, and net height change | m | Partly |

## Metric details

### Recovery and HRV

#### Heart rate variability

This list gives the details for heart rate variability:

- WHOOP name, API field, and unit: HRV. API: `hrv_rmssd_milli` in the Recovery `score` (ms). [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json)
- What it measures: How much the time between heartbeats varies from one beat to the next during sleep.
- Window or phase: The main sleep of a cycle. WHOOP measures HRV only during sleep. How WHOOP weights or windows the night is Not confirmed (support page not readable by automated check on 2026-10-07).
- Calculation: RMSSD, the root mean square of successive differences between heartbeats ([HRV help](https://support.whoop.com/s/article/Heart-Rate-Variability-HRV-Insights-WHOOP-Metrics?language=en_US)). Formula: Restatement of the standard definition: RMSSD = sqrt( mean( (RR[i+1] - RR[i])^2 ) ), in ms. The averaging weights are Not published.
- Defaults: None stated.
- Inputs: Beat-to-beat intervals from the strap's optical sensor during sleep.
- Units: Ms.
- Variants: One value for each Recovery. The API returns no HRV series.
- Comparison with standard methods or other vendors: WHOOP's value covers a sleep window. A morning RMSSD from a chest strap or phone app covers a few minutes after waking. Do not mix the two in one trend.
- What changes the number: Which sleep counts as the main sleep, sleep edits, nap merges, and fit of the strap.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [HRV help](https://support.whoop.com/s/article/Heart-Rate-Variability-HRV-Insights-WHOOP-Metrics?language=en_US), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US).

#### Resting heart rate

This list gives the details for resting heart rate:

- WHOOP name, API field, and unit: Resting Heart Rate (RHR). API: `resting_heart_rate` in the Recovery `score`. The API gives no unit. The help article describes it in beats per minute.
- What it measures: Heart rate at rest, measured during sleep.
- Window or phase: The main sleep of a cycle.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Heart rate during sleep.
- Units: Bpm.
- Variants: None.
- Comparison with standard methods or other vendors: A sleep value, not a seated or supine morning reading. Do not mix the two in one trend.
- What changes the number: Which sleep counts as the main sleep, and sleep edits.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US).

#### Recovery score

This list gives the details for the Recovery score:

- WHOOP name, API field, and unit: Recovery. API: `recovery_score` (0 to 100 %). [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json)
- What it measures: WHOOP's estimate of how prepared the member is to take on Strain that day.
- Window or phase: One score for each cycle, set in the morning after the main sleep. It does not change through the day unless the sleep is edited.
- Calculation: Proprietary. WHOOP lists HRV and resting heart rate as the two largest inputs. Other inputs are respiratory rate, sleep against need, light sleep and awake time, skin temperature, and SpO2. WHOOP compares HRV with a 30-day baseline. The weights and the formula are Not published.
- Defaults: WHOOP bands the score as green (67 to 100), yellow (34 to 66), and red (0 to 33) ([WHOOP 101](https://developer.whoop.com/docs/whoop-101), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US)).
- Inputs: As listed above.
- Units: Percent.
- Variants: None.
- Comparison with standard methods or other vendors: A proprietary composite. It has no standard equivalent. Do not compare it with another vendor's readiness score.
- What changes the number: Calibration, sleep edits, nap merges, and missing inputs on older devices.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US), [WHOOP 101](https://developer.whoop.com/docs/whoop-101).

#### Blood oxygen

This list gives the details for blood oxygen:

- WHOOP name, API field, and unit: SpO2. API: `spo2_percentage` (%).
- What it measures: The share of oxygen in the blood, as estimated by the strap during sleep.
- Window or phase: The main sleep of a cycle.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Optical sensor data.
- Units: Percent.
- Variants: Present only for WHOOP 4.0 or later.
- What changes the number: Device generation. WHOOP says it also accounts for altitude ([Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US)).
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US).

#### Skin temperature

This list gives the details for skin temperature:

- WHOOP name, API field, and unit: Skin Temperature. API: `skin_temp_celsius` (degrees C).
- What it measures: Skin temperature during sleep.
- Window or phase: The main sleep of a cycle.
- Calculation: Not published. The app shows it relative to the member's baseline. The API returns degrees Celsius.
- Defaults: None stated.
- Inputs: Strap temperature sensor.
- Units: Degrees C.
- Variants: Present only for WHOOP 4.0 or later.
- What changes the number: Room temperature, strap fit, and wear location.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Recovery help](https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US).

### Sleep

#### Sleep stage durations

This list gives the details for sleep stage durations:

- WHOOP name, API field, and unit: Time in bed, awake time, light sleep, slow wave sleep (deep), REM sleep, and no-data time. API: `total_in_bed_time_milli`, `total_awake_time_milli`, `total_light_sleep_time_milli`, `total_slow_wave_sleep_time_milli`, `total_rem_sleep_time_milli`, and `total_no_data_time_milli` in `score.stage_summary` (ms).
- What it measures: How the time of one sleep splits into stages.
- Window or phase: One sleep or nap.
- Calculation: Staged from strap data. The method is Not published. Formula: Restatement: total sleep time = light + slow wave + REM. WHOOP does not return total sleep time as one field.
- Defaults: None stated.
- Inputs: Heart rate and movement from the strap.
- Units: Ms.
- Variants: Each sleep and each nap has its own values.
- What changes the number: Sleep edits, nap merges, and gaps in data. A long `total_no_data_time_milli` means the strap lost contact.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [WHOOP 101](https://developer.whoop.com/docs/whoop-101).

#### Sleep efficiency

This list gives the details for sleep efficiency:

- WHOOP name, API field, and unit: Sleep Efficiency. API: `sleep_efficiency_percentage` (%).
- What it measures: The share of time in bed that the member was asleep.
- Window or phase: One sleep or nap.
- Calculation: WHOOP defines it as the percentage of time in bed spent asleep. Formula: Restatement: efficiency = time asleep / time in bed x 100.
- Defaults: WHOOP calls 90% or more optimal, 80 to 90% sufficient, and below 80% poor ([Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)).
- Inputs: Stage durations.
- Units: Percent.
- Variants: None.
- What changes the number: Sleep start and end times, including edits.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US).

#### Sleep Performance

This list gives the details for Sleep Performance:

- WHOOP name, API field, and unit: Sleep Performance. API: `sleep_performance_percentage` (%).
- What it measures: WHOOP's overall sleep score.
- Window or phase: One sleep.
- Calculation: Proprietary. The help article says the score combines four parts: sleep against need, consistency, efficiency, and stress during sleep. The API text describes only sleep against need. Weights are Not published. See [Conflicts in the vendor's own sources](#conflicts-in-the-vendors-own-sources).
- Defaults: WHOOP calls 85% or more optimal, 70 to 85% sufficient, and below 70% poor ([Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)).
- Inputs: Sleep Need, stage durations, sleep timing, and heart data during sleep.
- Units: Percent.
- Variants: May be missing if WHOOP lacks enough data to set Sleep Need.
- What changes the number: The change from the older one-part score to the four-part score.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US).

#### Sleep Consistency

This list gives the details for Sleep Consistency:

- WHOOP name, API field, and unit: Sleep Consistency. API: `sleep_consistency_percentage` (%).
- What it measures: How similar sleep and wake times are to the day before.
- Window or phase: One sleep, compared with earlier sleeps.
- Calculation: Proprietary. Not published.
- Defaults: Needs 3 nights in a row. WHOOP calls 80% or more optimal, 70 to 80% sufficient, and below 70% poor ([Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)).
- Inputs: Sleep and wake times.
- Units: Percent.
- Variants: May be missing for new members.
- What changes the number: Travel across time zones. WHOOP says it adjusts for these.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US).

#### Sleep Need

This list gives the details for Sleep Need:

- WHOOP name, API field, and unit: Sleep Needed. API: `baseline_milli`, `need_from_sleep_debt_milli`, `need_from_recent_strain_milli`, and `need_from_recent_nap_milli` in `score.sleep_needed` (ms).
- What it measures: How much sleep WHOOP says the member needs, split into a baseline and three adjustments.
- Window or phase: One sleep.
- Calculation: Proprietary. The baseline comes from the member's history. Debt adds sleep missed before. Recent Strain adds sleep. A recent nap takes sleep away, so that part is zero or negative. Formula: Restatement: total need = the sum of the four parts. Not confirmed, because WHOOP does not state the sum.
- Defaults: None stated in the sources read.
- Inputs: Sleep history, Strain, and naps.
- Units: Ms.
- Variants: None.
- What changes the number: Naps and high-Strain days.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US), [Sleep data page](https://developer.whoop.com/docs/developing/user-data/sleep).

#### Respiratory rate

This list gives the details for respiratory rate:

- WHOOP name, API field, and unit: Respiratory Rate. API: `respiratory_rate`. The API gives no unit. The help article says breaths per minute.
- What it measures: Breathing rate during sleep.
- Window or phase: One sleep.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Strap sensor data.
- Units: Breaths per minute.
- Variants: None.
- What changes the number: Data gaps during the sleep.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US).

#### Disturbances and sleep cycles

This list gives the details for disturbances and sleep cycles:

- WHOOP name, API field, and unit: Wake events and sleep cycles. API: `disturbance_count` and `sleep_cycle_count` (count).
- What it measures: The number of times sleep was disturbed, and the number of sleep cycles.
- Window or phase: One sleep.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Stage data.
- Units: Count.
- Variants: None.
- What changes the number: Sleep length. A longer sleep has more cycles.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json).

### Strain and heart rate

#### Day Strain

This list gives the details for day Strain:

- WHOOP name, API field, and unit: Day Strain. API: `strain` in the cycle `score` (0 to 21).
- What it measures: Load over a whole cycle, from training and from daily life.
- Window or phase: One physiological cycle, from sleep to sleep. The current cycle keeps growing until it ends.
- Calculation: Proprietary. The OpenAPI and WHOOP 101 describe Strain as cardiovascular load, from the member's heart rate. A muscular load part is Not confirmed (support page not readable by automated check on 2026-10-07). The scale is not linear, so each point is harder to gain than the last. WHOOP links the scale to the Borg perceived exertion scale. The formula is Not published.
- Defaults: WHOOP bands Strain as light (0 to 9), moderate (10 to 13), high (14 to 17), and all out (18 to 21) ([WHOOP 101](https://developer.whoop.com/docs/whoop-101)).
- Inputs: Heart rate, and maximum and resting heart rate. Muscular load as an input is Not confirmed (support page not readable by automated check on 2026-10-07).
- Units: 0 to 21, no unit.
- Variants: Day Strain and activity Strain.
- Comparison with standard methods or other vendors: A proprietary score. It is not a TRIMP or a session RPE load. Do not compare it with another vendor's load.
- What changes the number: Maximum heart rate, logged strength exercises, and device generation.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [WHOOP 101](https://developer.whoop.com/docs/whoop-101), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US).

#### Activity Strain

This list gives the details for activity Strain:

- WHOOP name, API field, and unit: Activity Strain. API: `strain` in the workout `score` (0 to 21).
- What it measures: Load in one workout.
- Window or phase: The workout `start` to `end`.
- Calculation: As day Strain, over the workout only. Not published.
- Defaults: As day Strain.
- Inputs: As day Strain. How WHOOP estimates muscular load for strength workouts is Not confirmed (support page not readable by automated check on 2026-10-07).
- Units: 0 to 21, no unit.
- Variants: None.
- What changes the number: Workout start and end, logged exercises, and percent recorded.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US).

#### Average and maximum heart rate

This list gives the details for average and maximum heart rate:

- WHOOP name, API field, and unit: Average and max heart rate. API: `average_heart_rate` and `max_heart_rate` in the cycle `score` and in the workout `score` (bpm, whole numbers).
- What it measures: Mean and highest heart rate over a cycle or a workout.
- Window or phase: The cycle or the workout.
- Calculation: Not published.
- Defaults: None.
- Inputs: Strap heart rate.
- Units: Bpm.
- Variants: Cycle and workout.
- Comparison with standard methods or other vendors: The API returns no heart rate series, so you cannot pick out a test stage inside a workout.
- What changes the number: Workout start and end times, and gaps in data.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json).

#### Time in heart rate zones

This list gives the details for time in heart rate zones:

- WHOOP name, API field, and unit: Heart rate zones. API: `zone_zero_milli` to `zone_five_milli` in `score.zone_durations` (ms).
- What it measures: Time spent in each of six heart rate zones during a workout.
- Window or phase: The workout.
- Calculation: WHOOP uses heart rate reserve. Formula: WHOOP publishes: target heart rate = ((maximum heart rate - resting heart rate) x % intensity) + resting heart rate. The default % limits for each zone are Not published.
- Defaults: Monthly zone updates from resting heart rate are Not confirmed (support page not readable by automated check on 2026-10-07). Members can set zones by hand ([Max heart rate help](https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US)).
- Inputs: Heart rate, maximum heart rate, and resting heart rate.
- Units: Ms.
- Variants: Zone 0 to zone 5. The zone names differ between the API and the help article. See [Conflicts in the vendor's own sources](#conflicts-in-the-vendors-own-sources).
- What changes the number: Zone limits, maximum heart rate, and resting heart rate. WHOOP counts zone time only for logged activities.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Max heart rate help](https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US).

#### Percent recorded

This list gives the details for percent recorded:

- WHOOP name, API field, and unit: API: `percent_recorded` in the workout `score` (0 to 100 %).
- What it measures: The share of the workout for which WHOOP received heart rate data.
- Window or phase: The workout.
- Calculation: Not published as a formula. Formula: Restatement: time with heart rate data / workout duration x 100.
- Defaults: None.
- Inputs: Heart rate data stream.
- Units: Percent.
- Variants: None.
- What changes the number: Strap contact and battery.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json).

#### Energy

This list gives the details for energy:

- WHOOP name, API field, and unit: Energy burned. API: `kilojoule` in the cycle `score` and in the workout `score` (kJ).
- What it measures: Estimated energy used over a cycle or a workout.
- Window or phase: The cycle or the workout.
- Calculation: Not published.
- Defaults: None.
- Inputs: Not published.
- Units: Kilojoules. Divide by 4.184 for kilocalories.
- Variants: Cycle and workout.
- What changes the number: Body weight and heart rate settings.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json).

#### Maximum heart rate setting

This list gives the details for the maximum heart rate setting:

- WHOOP name, API field, and unit: Max HR. API: `max_heart_rate` from `GET /v2/user/measurement/body` (bpm).
- What it measures: The maximum heart rate WHOOP holds for the member.
- Window or phase: The value at the time of the call. The API gives no history.
- Calculation: The estimation method, said to be Gellish's non-linear formula adjusted from recorded peaks, is Not confirmed (support page not readable by automated check on 2026-10-07). Members can type a value.
- Defaults: As above.
- Inputs: The inputs to the formula are Not published. Recorded peaks adjust the value.
- Units: Bpm.
- Variants: Estimated or entered by hand. The API does not say which.
- What changes the number: Member edits and new peaks.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Max heart rate help](https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US).

### Movement

#### Steps

This list gives the details for steps:

- WHOOP name, API field, and unit: Steps. API: `step_count` on the cycle (count).
- What it measures: Steps taken during a cycle.
- Window or phase: The cycle, not a calendar day. The current cycle shows steps so far.
- Calculation: Not published.
- Defaults: None.
- Inputs: Strap movement data.
- Units: Count.
- Variants: Null when the strap was not worn for the whole cycle. Added on 2026-09-23.
- What changes the number: Wear time.
- Sources: [Cycle](https://developer.whoop.com/docs/developing/user-data/cycle), [API changelog](https://developer.whoop.com/docs/api-changelog).

#### Workout distance and altitude

This list gives the details for workout distance and altitude:

- WHOOP name, API field, and unit: API: `distance_meter`, `altitude_gain_meter`, and `altitude_change_meter` in the workout `score` (m).
- What it measures: Distance covered, total height climbed, and net change in height from start to end.
- Window or phase: The workout.
- Calculation: WHOOP explains that altitude gain counts only upward travel, and altitude change is end height minus start height. The source of distance is Not published.
- Defaults: None.
- Inputs: Distance or altitude data sent to WHOOP.
- Units: Metres.
- Variants: Present only when distance or altitude data exist.
- What changes the number: Whether GPS data reached WHOOP.
- Sources: [OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json).

## Context fields that are not metrics

These fields are not metrics but change how you read every metric:

- `score_state`: `SCORED`, `PENDING_SCORE`, or `UNSCORABLE`. Scores exist only for `SCORED` records. WHOOP says `UNSCORABLE` is often due to too little data ([OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json)).
- `user_calibrating`: true while WHOOP learns a new member's baseline.
- `nap`: true for a nap. Naps do not create a Recovery. They lower Sleep Need ([WHOOP Cycles help](https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US)).
- `start`, `end`, and `timezone_offset`: time bounds and the local offset at the time, in the format `+hh:mm`, `-hh:mm`, or `Z`.
- `created_at` and `updated_at`: when WHOOP stored and last changed the record. Use `updated_at` to find edits.
- `cycle_id`, `sleep_id`, and `id`: links between cycles, sleeps, Recovery, and workouts. Sleep and workout IDs are UUIDs in v2.
- `sport_name`: the WHOOP sport for a workout. `sport_id` will not exist after 2025-09-01, by WHOOP's own note.
- `height_meter` and `weight_kilogram`: body values from `GET /v2/user/measurement/body`.

## Conflicts in the vendor's own sources

The WHOOP sources disagree on these points:

- Sleep Performance: the API describes it as time asleep over sleep needed. The Sleep help article says it now combines four parts ([OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Sleep help](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)).
- Zone names: the API names zone 0 very light, zone 1 light, zone 2 moderate, zone 3 hard, zone 4 very hard, and zone 5 maximum. The Strain help article names zone 0 resting, zone 1 very light, zone 2 light, zone 3 moderate, zone 4 hard, and zone 5 maximum effort ([OpenAPI](https://api.prod.whoop.com/developer/doc/openapi.json), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US)).
- Strain and zones: the Max heart rate help article says zones do not drive Strain, and Strain depends on time at high heart rate relative to maximum and resting heart rate. A muscular load part from the Strain help article is Not confirmed (support page not readable by automated check on 2026-10-07) ([Max heart rate help](https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US)).
- Strain scale: WHOOP 101 says it takes more stress to rise from 16 to 17 than from 4 to 5. The Strain help article calls the scale logarithmic. Both say the scale is not linear ([WHOOP 101](https://developer.whoop.com/docs/whoop-101), [Strain help](https://support.whoop.com/s/article/WHOOP-Strain?language=en_US)).

## Not published

The sources do not publish or confirm these details. Confirm them with the user or with WHOOP:

- The formulas and weights for Recovery, Strain, Sleep Performance, Sleep Consistency, and Sleep Need.
- The exact HRV averaging window and weights.
- The member export steps, delivery time, and link expiry.
- The maximum heart rate estimation method, and whether zones update each month.
- Whether Strain includes a muscular load part.
- The default % limits of each heart rate zone.
- The column names and units of the member CSV export.
- The export format and access rules of WHOOP Unite. Its help pages need a login.
- The length of the calibration period in days. WHOOP says only "a few days".
- The method for energy, distance, and steps.
- The access token lifetime. The documented example shows 3,600 seconds, but WHOOP says to read `expires_in`.

## Worked example in Python

This example keeps the main sleep apart from naps, reports nap time in its own column, and records a pending Recovery as missing. The records are made up.

The program and its output follow. The output came from Python 3.12 on 2026-10-07.

```python
"""Worked example: keep the main WHOOP sleep apart from naps.

The records are synthetic. They copy the shape of WHOOP API v2 sleep and
recovery records, with only the fields this example needs.
"""
sleeps = [
    {"id": "s1", "cycle_id": 101, "nap": False, "score_state": "SCORED"},
    {"id": "s2", "cycle_id": 101, "nap": True, "score_state": "SCORED",  # asleep_milli: light + slow wave + REM
     "asleep_milli": 1_500_000},
    {"id": "s3", "cycle_id": 102, "nap": False, "score_state": "SCORED"},
    {"id": "s4", "cycle_id": 103, "nap": False, "score_state": "PENDING_SCORE"},
]
recoveries = {
    "s1": {"hrv_rmssd_milli": 61.4, "resting_heart_rate": 52.0, "user_calibrating": False},
    "s3": {"hrv_rmssd_milli": 55.9, "resting_heart_rate": 54.0, "user_calibrating": False},
}

nap_min = {}
for s in sleeps:
    if s["nap"]:
        nap_min[s["cycle_id"]] = nap_min.get(s["cycle_id"], 0) + s["asleep_milli"] / 60000

print("athlete_id,cycle_id,measure_name,value,unit,status,source,source_record_id,nap_min")
for s in sleeps:
    if s["nap"]:
        continue  # naps never feed overnight HRV
    nap = nap_min.get(s["cycle_id"], "")
    if s["score_state"] != "SCORED":
        print(f"A01,{s['cycle_id']},hrv_rmssd,NA,ms,pending,whoop,{s['id']},{nap}")
        continue
    r = recoveries[s["id"]]
    print(f"A01,{s['cycle_id']},hrv_rmssd,{r['hrv_rmssd_milli']},ms,ok,whoop,{s['id']},{nap}")
    print(f"A01,{s['cycle_id']},resting_hr_sleep,{r['resting_heart_rate']},bpm,ok,whoop,{s['id']},{nap}")
```

Output:

```text
athlete_id,cycle_id,measure_name,value,unit,status,source,source_record_id,nap_min
A01,101,hrv_rmssd,61.4,ms,ok,whoop,s1,25.0
A01,101,resting_hr_sleep,52.0,bpm,ok,whoop,s1,25.0
A01,102,hrv_rmssd,55.9,ms,ok,whoop,s3,
A01,102,resting_hr_sleep,54.0,bpm,ok,whoop,s3,
A01,103,hrv_rmssd,NA,ms,pending,whoop,s4,
```

## Sources

This page draws on these WHOOP sources:

- WHOOP API reference: <https://developer.whoop.com/api/>, accessed 2026-10-07.
- OpenAPI file: <https://api.prod.whoop.com/developer/doc/openapi.json>, accessed 2026-10-07.
- Overview: <https://developer.whoop.com/docs/developing/overview>, accessed 2026-10-07.
- Getting Started: <https://developer.whoop.com/docs/developing/getting-started>, accessed 2026-10-07.
- OAuth: <https://developer.whoop.com/docs/developing/oauth>, accessed 2026-10-07.
- App Approval: <https://developer.whoop.com/docs/developing/app-approval>, accessed 2026-10-07.
- Pagination: <https://developer.whoop.com/docs/developing/pagination>, accessed 2026-10-07.
- Rate limiting: <https://developer.whoop.com/docs/developing/rate-limiting>, accessed 2026-10-07.
- Webhooks: <https://developer.whoop.com/docs/developing/webhooks/>, accessed 2026-10-07.
- v1 to v2 Migration Guide: <https://developer.whoop.com/docs/developing/v1-v2-migration>, accessed 2026-10-07.
- API changelog: <https://developer.whoop.com/docs/api-changelog>, accessed 2026-10-07.
- Cycle: <https://developer.whoop.com/docs/developing/user-data/cycle>, accessed 2026-10-07.
- Recovery data page: <https://developer.whoop.com/docs/developing/user-data/recovery>, accessed 2026-10-07.
- Sleep data page: <https://developer.whoop.com/docs/developing/user-data/sleep>, accessed 2026-10-07.
- Workout data page: <https://developer.whoop.com/docs/developing/user-data/workout>, accessed 2026-10-07.
- WHOOP 101: <https://developer.whoop.com/docs/whoop-101>, accessed 2026-10-07.
- Get Current Recovery Score: <https://developer.whoop.com/docs/tutorials/get-current-recovery-score>, accessed 2026-10-07.
- Export help, How to Export Your Data: <https://support.whoop.com/s/article/How-to-Export-Your-Data>, accessed 2026-10-07.
- Recovery help, WHOOP Recovery: <https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US>, accessed 2026-10-07.
- HRV help, Heart Rate Variability (HRV) Insights and WHOOP Metrics: <https://support.whoop.com/s/article/Heart-Rate-Variability-HRV-Insights-WHOOP-Metrics?language=en_US>, accessed 2026-10-07.
- WHOOP Cycles help: <https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US>, accessed 2026-10-07.
- Sleep help, WHOOP Sleep: <https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US>, accessed 2026-10-07.
- Strain help, WHOOP Strain: <https://support.whoop.com/s/article/WHOOP-Strain?language=en_US>, accessed 2026-10-07.
- Max heart rate help, Adjusting and Calculating Max Heart Rate and Heart Rate Zones: <https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US>, accessed 2026-10-07.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
