# Oura metrics

Oura makes a smart ring that records heart rate, heart rate variability, temperature, movement, and sleep, and scores them in the Oura app. This page covers the metrics that the Oura API V2 returns for sleep periods, daily readiness, daily sleep, heart rate, and workouts, and uses public sources only. Checked against: the Oura API V2 OpenAPI file `openapi-1.41.json`, the Oura Enterprise Support API articles, and Oura Member Care articles, 2026-10-07.

Oura and ŌURA are trademarks of Oura Health Oy. This repository is not affiliated with or endorsed by Oura.

For how to pull and reshape the data, see the [Oura device reference](../../skills/heart-rate-and-sleep/references/oura.md).

## How to read this page

This page has summary tables, then one block for each metric. Each metric block is a short list with these fields:

- Oura name, API field, and unit: the name in the app, the field in the API, and the unit Oura states.
- What it measures: one plain sentence.
- Window or phase: the part of the day or night the value covers.
- Calculation: Oura's description in paraphrase, then the formula. The formula is the one Oura publishes, marked as a restatement, or "Not published".
- Defaults: settings and thresholds, each with a source.
- Inputs, Units, and Variants: what goes in, what comes out, and the forms the metric takes.
- Comparison with standard methods or other vendors: a comparison only where a source supports one.
- What changes the number: settings, data quality, and device factors.
- Sources: links to the vendor documents behind the block.

Follow these rules when you use the blocks:

- The Readiness Score, the Sleep Score, and their contributors are proprietary Oura scores. Report them as Oura gives them. Never recompute them.
- "Not published" means Oura gives no formula or detail in the sources read. "Not confirmed" means a source was blocked or two sources disagree.
- A formula marked "restatement" is a standard definition or a rewrite of an Oura statement for this page. Oura does not print it as a formula.
- Code font marks API field names.
- In the summary tables, "Yes" means Oura publishes the calculation. "Partly" means Oura publishes some of it. "Not published" means Oura does not publish the calculation.

## Areas and metric counts

The table lists each area, the number of metric blocks in this page, and the number of API fields that those blocks cover:

| Area | Metric blocks | API fields covered |
|---|---|---|
| HRV and heart rate during sleep | 4 | 6 |
| Sleep durations and quality | 6 | 13 |
| Readiness and Sleep Scores | 6 | 22 |
| Daytime heart rate | 1 | 1 |
| Workouts | 1 | 3 |
| Total | 18 | 45 |

The API has more routes, such as daily activity, stress, resilience, SpO2, tags, sessions, and ring configuration. This page does not cover them. Identifiers, time fields, and status flags are listed in [Context fields that are not metrics](#context-fields-that-are-not-metrics).

## Settings and data conditions that change many metrics

These conditions change many metrics at once. Check them first when a number looks wrong:

- Sync. Sleep data and Readiness reach the API only after the member opens the Oura app and syncs the ring. Heart rate syncs in the background ([API docs](https://cloud.ouraring.com/v2/docs)).
- Sleep Day. Oura assigns sleep to a Sleep Day that runs from 6 pm to 6 pm. The longest continuous sleep in that window gives the Sleep Score for the day ([Oura Days](https://partnersupport.ouraring.com/hc/en-us/articles/29160913203219-Understanding-the-Different-Types-of-Oura-Days-in-Oura-API-Data)). A nap that ends after 6 pm counts toward the next day ([API docs](https://cloud.ouraring.com/v2/docs)).
- Sleep period type. Only some periods feed daily scores. See [Context fields that are not metrics](#context-fields-that-are-not-metrics).
- Sleep algorithm version. `sleep_algorithm_version` is `v1` (the original algorithm) or `v2` (the newer one). Stages can shift when the version changes ([API docs](https://cloud.ouraring.com/v2/docs)).
- Bedtime edits. An edit by the member creates a new version of the sleep. `sleep_analysis_reason` shows `bedtime_edit` ([API docs](https://cloud.ouraring.com/v2/docs)).
- Membership. Gen3 and later rings need an active membership for data to reach the API ([Using the Oura API](https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Using-the-Oura-API)).
- Baselines. The balance contributors compare a 14-day weighted average with a two-month average, so a new member's scores settle over weeks ([Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score)).
- Low battery and Rest Mode. `low_battery_alert` flags a sleep with a low battery. Rest Mode periods have their own route ([API docs](https://cloud.ouraring.com/v2/docs)).

## API access

Oura ties data to OAuth scopes and limits how many members an app can connect. The sources state these rules:

| Rule | What Oura states | Source |
|---|---|---|
| Version | V2 is the only API. V1 has been shut down. | [API docs](https://cloud.ouraring.com/v2/docs) |
| Member limit | 10 users per application before Oura approves it, then no limit | [API docs](https://cloud.ouraring.com/v2/docs) |
| Cost | Free for personal and commercial use | [API docs](https://cloud.ouraring.com/v2/docs) |
| Personal access tokens | Deprecated in December 2025 and no longer usable | [API docs](https://cloud.ouraring.com/v2/docs) |
| Scopes | `email`, `personal`, `daily`, `heartrate`, `workout`, `tag`, `session`, `spo2`, and `heart_health`. The authentication page lists the first 8. | [API docs](https://cloud.ouraring.com/v2/docs), [Authentication](https://cloud.ouraring.com/docs/authentication) |
| Rate limits | Per token and per application. The FAQ gives 5,000 requests per 5 minutes. | [API docs](https://cloud.ouraring.com/v2/docs) |
| Webhooks | Create, update, and delete events for each data type. Subscriptions expire and must be renewed. | [API docs](https://cloud.ouraring.com/v2/docs) |
| Member download | From the Membership Hub, ready within 10 days, durations in seconds | [Export help](https://support.ouraring.com/hc/en-us/articles/360025441594-Export-Share-Your-Oura-Data) |
| Organization platform | A licensed Enterprise Platform is listed. Export details are Not confirmed. | [Enterprise Support home](https://partnersupport.ouraring.com/hc/en-us) |

## Summary tables

### HRV and heart rate during sleep summary

This table lists the metrics in the HRV and heart rate during sleep area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Average HRV](#average-hrv) | Mean overnight heart rate variability, and its 5-minute series | ms | Partly |
| [Lowest heart rate](#lowest-heart-rate) | Lowest heart rate in a sleep period | bpm | Partly |
| [Average heart rate during sleep](#average-heart-rate-during-sleep) | Mean heart rate in a sleep period, and its series | bpm | Partly |
| [Breathing rate](#breathing-rate) | Breaths per minute during sleep | breaths per minute | Not published |

### Sleep durations and quality summary

This table lists the metrics in the sleep durations and quality area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Total sleep duration](#total-sleep-duration) | Time asleep | s | Not published |
| [Time in bed and awake time](#time-in-bed-and-awake-time) | Time in bed and time awake in bed | s | Not published |
| [Latency](#latency) | Time to fall asleep | s | Partly |
| [Sleep stages](#sleep-stages) | Time in deep, light, and REM sleep, and stage strings | s | Not published |
| [Efficiency](#efficiency) | Sleep efficiency rating | 1 to 100 | Not published |
| [Restlessness](#restlessness) | Restless periods and movement classes | count | Not published |

### Readiness and Sleep Scores summary

This table lists the metrics in the Readiness and Sleep Scores area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Readiness Score](#readiness-score) | Oura's readiness score for the day | 0 to 100 (help page) or 1 to 100 (OpenAPI) | Partly |
| [Readiness contributors](#readiness-contributors) | The nine parts of the Readiness Score | 1 to 100 | Partly |
| [Temperature deviation](#temperature-deviation) | Body temperature against baseline | degrees C | Not published |
| [Sleep Score](#sleep-score) | Oura's sleep score for the day | 0 to 100 | Not published |
| [Sleep Score contributors](#sleep-score-contributors) | The seven parts of the Sleep Score | 1 to 100 | Not published |
| [Score deltas](#score-deltas) | Effect of one sleep period on the day's scores | points | Not published |

### Daytime heart rate summary

This table lists the metrics in the daytime heart rate area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Heart rate samples](#heart-rate-samples) | Heart rate through the day and night | bpm | Not published |

### Workouts summary

This table lists the metrics in the workouts area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Workout summary](#workout-summary) | Intensity, energy, and distance of a workout | none, kcal, m | Not published |

## Metric details

### HRV and heart rate during sleep

#### Average HRV

This list gives the details for average HRV:

- Oura name, API field, and unit: Average HRV. API: `average_hrv` (whole number) and the series `hrv` on each sleep period. The API gives no unit. The HRV help article gives milliseconds.
- What it measures: How much the time between heartbeats varies from one beat to the next during sleep.
- Window or phase: One sleep period. Oura measures HRV only during sleep. It takes 5-minute samples through the night.
- Calculation: The average is the mean of all 5-minute samples while asleep ([HRV help](https://support.ouraring.com/hc/en-us/articles/360025441974-Heart-Rate-Variability)). A 2021 peer-reviewed study says the Oura app's Moment feature reports average rMSSD over 5 minutes ([Stone et al., 2021](https://doi.org/10.3389/fspor.2021.585870)). Formula: Restatement: `average_hrv` = mean of the non-null 5-minute samples while asleep, each sample an RMSSD in ms. Not confirmed for the API field, because the API does not name the statistic or say how nulls are handled.
- Defaults: The series interval is in the `interval` field. The enterprise help lists 5-minute resolution ([Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API)).
- Inputs: Beat-to-beat intervals from the ring's optical sensor.
- Units: Ms.
- Variants: The app also shows Max HRV, the highest sample of the night. The API has no Max HRV field. Sessions in the app can give a daytime HRV snapshot, which is a different measure.
- Comparison with standard methods or other vendors: A whole-night mean. A morning RMSSD from a chest strap or phone app covers a few minutes after waking. WHOOP weights its night value differently. Do not mix these in one trend.
- What changes the number: Which period counts as the main sleep, bedtime edits, ring fit, and the sleep algorithm version.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [HRV help](https://support.ouraring.com/hc/en-us/articles/360025441974-Heart-Rate-Variability), [Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API), [Stone et al., 2021](https://doi.org/10.3389/fspor.2021.585870).

#### Lowest heart rate

This list gives the details for lowest heart rate:

- Oura name, API field, and unit: Lowest heart rate. API: `lowest_heart_rate` (whole number). The API gives no unit. Oura describes heart rate in beats per minute.
- What it measures: The lowest heart rate in one sleep period.
- Window or phase: One sleep period.
- Calculation: The API value comes from 30-second samples. The app shows the lowest of the 5-minute values, so the two can differ ([API docs](https://cloud.ouraring.com/v2/docs)). The enterprise help lists the lowest heart rate in a 5-minute window ([Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API)). See [Conflicts in the vendor's own sources](#conflicts-in-the-vendors-own-sources).
- Defaults: None stated.
- Inputs: Ring heart rate during sleep.
- Units: Bpm.
- Variants: API value and app value.
- Comparison with standard methods or other vendors: A sleep value, not a seated or supine morning reading.
- What changes the number: Sample resolution and the choice of main sleep.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API).

#### Average heart rate during sleep

This list gives the details for average heart rate during sleep:

- Oura name, API field, and unit: Average heart rate. API: `average_heart_rate` (beats per minute) and the series `heart_rate` on each sleep period.
- What it measures: Mean heart rate in one sleep period.
- Window or phase: One sleep period.
- Calculation: The API value comes from 30-second samples. The app shows the mean of 5-minute values instead ([API docs](https://cloud.ouraring.com/v2/docs)).
- Defaults: The series interval is in the `interval` field. The enterprise help lists 5-minute resolution.
- Inputs: Ring heart rate during sleep.
- Units: Bpm.
- Variants: API value, app value, and series.
- What changes the number: Sample resolution and the choice of main sleep.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API).

#### Breathing rate

This list gives the details for breathing rate:

- Oura name, API field, and unit: Respiratory rate. API: `average_breath` (breaths per minute).
- What it measures: Mean breathing rate in one sleep period.
- Window or phase: One sleep period.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Ring sensor data.
- Units: Breaths per minute.
- Variants: None.
- What changes the number: The choice of main sleep.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

### Sleep durations and quality

#### Total sleep duration

This list gives the details for total sleep duration:

- Oura name, API field, and unit: Total sleep. API: `total_sleep_duration` (s).
- What it measures: Time asleep in one sleep period.
- Window or phase: One sleep period.
- Calculation: Not published. Formula: Restatement, Not confirmed: deep + light + REM durations.
- Defaults: None stated.
- Inputs: Sleep staging.
- Units: Seconds. Divide by 60 for minutes.
- Variants: None.
- What changes the number: Bedtime edits and the sleep algorithm version.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Export help](https://support.ouraring.com/hc/en-us/articles/360025441594-Export-Share-Your-Oura-Data).

#### Time in bed and awake time

This list gives the details for time in bed and awake time:

- Oura name, API field, and unit: Time in bed and awake time. API: `time_in_bed` and `awake_time` (s).
- What it measures: Time from `bedtime_start` to `bedtime_end`, and time awake within it.
- Window or phase: One sleep period.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Bedtime bounds and staging.
- Units: Seconds.
- Variants: None.
- What changes the number: Bedtime edits.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

#### Latency

This list gives the details for latency:

- Oura name, API field, and unit: Latency. API: `latency` (s).
- What it measures: The time it took to fall asleep after going to bed.
- Window or phase: Start of one sleep period.
- Calculation: Oura defines it as the time from going to bed to falling asleep. The detection method is Not published.
- Defaults: None stated.
- Inputs: Bedtime start and staging.
- Units: Seconds.
- Variants: None.
- What changes the number: Bedtime edits.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

#### Sleep stages

This list gives the details for sleep stages:

- Oura name, API field, and unit: Deep, light, and REM sleep. API: `deep_sleep_duration`, `light_sleep_duration`, and `rem_sleep_duration` (s). Stage strings: `sleep_phase_30_sec`, `sleep_phase_5_min`, and `app_sleep_phase_5_min`.
- What it measures: Time in each sleep stage, and the stage for each 30-second or 5-minute step.
- Window or phase: One sleep period.
- Calculation: Staged by Oura's sleep algorithm. Not published. In the strings, `1` is deep, `2` is light, `3` is REM, and `4` is awake.
- Defaults: None stated.
- Inputs: Ring sensor data.
- Units: Seconds for durations. One character per step for strings.
- Variants: `app_sleep_phase_5_min` matches the app view. Oura says it will be removed after a transition period.
- What changes the number: The sleep algorithm version and bedtime edits.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

#### Efficiency

This list gives the details for efficiency:

- Oura name, API field, and unit: Efficiency. API: `efficiency` (1 to 100).
- What it measures: Oura's rating of sleep efficiency.
- Window or phase: One sleep period.
- Calculation: Not published. The API calls it a rating, so it may not equal time asleep divided by time in bed.
- Defaults: None stated.
- Inputs: Not published.
- Units: 1 to 100.
- Variants: Also a Sleep Score contributor with the same name. The two are different fields.
- What changes the number: Bedtime edits.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

#### Restlessness

This list gives the details for restlessness:

- Oura name, API field, and unit: Restless periods. API: `restless_periods` (count) and `movement_30_sec` (string).
- What it measures: The number of restless periods, and a movement class for each 30 seconds.
- Window or phase: One sleep period.
- Calculation: Not published. In `movement_30_sec`, `1` is no motion, `2` is restless, `3` is tossing and turning, and `4` is active.
- Defaults: None stated.
- Inputs: Ring accelerometer.
- Units: Count, and one character per 30 seconds.
- Variants: None.
- What changes the number: Ring fit.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

### Readiness and Sleep Scores

#### Readiness Score

This list gives the details for the Readiness Score:

- Oura name, API field, and unit: Readiness Score. API: `score` from `daily_readiness`. The Readiness help page gives 0 to 100. The OpenAPI gives the readiness score as 1 to 100. The two sources conflict ([Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score), [API docs](https://cloud.ouraring.com/v2/docs)). The same score sits in the `readiness` object of the sleep period that feeds it.
- What it measures: Oura's estimate of how prepared the member is for the day, from recovery and activity.
- Window or phase: One day.
- Calculation: Proprietary. Oura uses short-term inputs (lowest resting heart rate and its timing, average body temperature, sleep quality, and the previous day's movement) and long-term balance inputs (HRV, sleep, and activity). The weights and the formula are Not published.
- Defaults: Oura bands scores as optimal (85 to 100), good (70 to 84), fair (60 to 69), and pay attention (0 to 59) ([Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score)).
- Inputs: As above.
- Units: 0 to 100 on the Readiness help page, and 1 to 100 in the OpenAPI.
- Variants: None.
- Comparison with standard methods or other vendors: A proprietary composite. It has no standard equivalent. Do not compare it with WHOOP Recovery or another vendor's score.
- What changes the number: Sync timing, bedtime edits, and the length of the member's history.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score).

#### Readiness contributors

This list gives the details for the Readiness contributors:

- Oura name, API field, and unit: Readiness Contributors. API: `activity_balance`, `body_temperature`, `hrv_balance`, `previous_day_activity`, `previous_night`, `recovery_index`, `resting_heart_rate`, `sleep_balance`, and `sleep_regularity` in `contributors` (1 to 100).
- What it measures: How much each part adds to the Readiness Score.
- Window or phase: One day. The balance contributors cover 14 days against two months.
- Calculation: Proprietary. The balance contributors compare a 14-day weighted average, with slightly more weight on the past 2 to 5 days, with the long-term average over two months ([Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score)). Oura says heart rate stabilization is when resting heart rate stays within 3 bpm of the night's lowest value. The mapping to the 1 to 100 rating is Not published.
- Defaults: As above.
- Inputs: HRV, resting heart rate, temperature, sleep, and activity.
- Units: 1 to 100 rating. Not a raw value.
- Variants: None.
- Comparison with standard methods or other vendors: `hrv_balance` is a rating, not an HRV value. Trend `average_hrv` instead.
- What changes the number: History length.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score).

#### Temperature deviation

This list gives the details for temperature deviation:

- Oura name, API field, and unit: Temperature deviation. API: `temperature_deviation` and `temperature_trend_deviation` (degrees C).
- What it measures: Body temperature against the member's baseline, and the trend of that difference.
- Window or phase: The main sleep. The enterprise help lists temperature as collected during the main sleep.
- Calculation: Not published. The baseline window is Not published.
- Defaults: None stated.
- Inputs: Ring temperature sensor.
- Units: Degrees C.
- Variants: Single night and trend.
- What changes the number: Room temperature and ring fit.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API).

#### Sleep Score

This list gives the details for the Sleep Score:

- Oura name, API field, and unit: Sleep Score. API: `score` from `daily_sleep` (0 to 100).
- What it measures: Oura's overall score for the night.
- Window or phase: One Sleep Day. The longest continuous sleep in the 6 pm to 6 pm window gives the score.
- Calculation: Proprietary. Not published.
- Defaults: Oura uses the same bands as the Readiness Score: 85 to 100 optimal, 70 to 84 good, 60 to 69 fair, and 0 to 59 pay attention ([Readiness help](https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score)).
- Inputs: The seven contributors.
- Units: 0 to 100.
- Variants: None.
- What changes the number: Naps and late naps, bedtime edits, and the sleep algorithm version.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs), [Oura Days](https://partnersupport.ouraring.com/hc/en-us/articles/29160913203219-Understanding-the-Different-Types-of-Oura-Days-in-Oura-API-Data).

#### Sleep Score contributors

This list gives the details for the Sleep Score contributors:

- Oura name, API field, and unit: Sleep contributors. API: `deep_sleep`, `efficiency`, `latency`, `rem_sleep`, `restfulness`, `timing`, and `total_sleep` in `contributors` (1 to 100).
- What it measures: How much each part adds to the Sleep Score.
- Window or phase: One Sleep Day.
- Calculation: Proprietary. Not published.
- Defaults: None stated.
- Inputs: Sleep period values.
- Units: 1 to 100 rating. Not a raw value.
- Variants: None.
- Comparison with standard methods or other vendors: Trend the raw durations, not these ratings.
- What changes the number: As the Sleep Score.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

#### Score deltas

This list gives the details for score deltas:

- Oura name, API field, and unit: API: `readiness_score_delta` and `sleep_score_delta` on a sleep period (whole number).
- What it measures: How much one sleep period changed the day's Readiness Score and Sleep Score.
- Window or phase: One sleep period.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Not published.
- Units: Score points.
- Variants: Most useful for naps that add to a day.
- What changes the number: Period type.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

### Daytime heart rate

#### Heart rate samples

This list gives the details for heart rate samples:

- Oura name, API field, and unit: Heart rate. API: `bpm` from `GET /v2/usercollection/heartrate` (beats per minute), with `timestamp` in UTC and `source`.
- What it measures: Heart rate through the day and night.
- Window or phase: Each sample. `source` is `awake`, `rest`, `sleep`, `workout`, `live`, or `session`.
- Calculation: Not published.
- Defaults: Oura says the route gives heart rate in 5-minute increments ([API docs](https://cloud.ouraring.com/v2/docs)). Whether workout samples are finer is Not confirmed.
- Inputs: Ring optical sensor.
- Units: Bpm.
- Variants: Session heart rate sits on the sessions route instead.
- Comparison with standard methods or other vendors: A 5-minute sample is too coarse to time a submaximal test stage. Check the timestamps before you use it for that.
- What changes the number: Wear time and sync.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

### Workouts

#### Workout summary

This list gives the details for the workout summary:

- Oura name, API field, and unit: Workout. API: `intensity` (`easy`, `moderate`, or `hard`), `calories` (kcal), and `distance` (m).
- What it measures: Oura's summary of one workout.
- Window or phase: `start_datetime` to `end_datetime`.
- Calculation: Not published.
- Defaults: None stated.
- Inputs: Ring data or third-party heart rate, as `source` shows.
- Units: None, kcal, and m.
- Variants: `source` is `manual`, `autodetected`, `confirmed`, `workout_heart_rate`, `live_third_party_heart_rate`, or `live_oura_heart_rate`.
- What changes the number: The workout source.
- Sources: [API docs](https://cloud.ouraring.com/v2/docs).

## Context fields that are not metrics

These fields are not metrics but change how you read every metric:

- `day`: the date a record belongs to. Oura reads date filters in the member's local time zone ([API docs](https://cloud.ouraring.com/v2/docs)).
- `type` on a sleep period: `long_sleep` is a sleep longer than 3 hours that counts toward daily scores on its own. `sleep` is a confirmed nap or short sleep of 15 minutes to 3 hours that counts toward daily scores. `late_nap` is a confirmed nap that ended after the 6 pm day change and counts toward the next day. `rest` is a period the member rejected as sleep. `deleted` is a period the member deleted ([API docs](https://cloud.ouraring.com/v2/docs)).
- `period`: Oura's identifier for the sleep period within its processing.
- `bedtime_start` and `bedtime_end`: local time with offset.
- `low_battery_alert`: true when the ring battery ran low during the period.
- `sleep_algorithm_version`: `v1` or `v2`.
- `sleep_analysis_reason`: why the latest version of the sleep was created, such as `bedtime_edit`.
- `timestamp` on daily documents: local time of the daily record.
- `ring_id`: deprecated, returns null.
- Rest Mode periods: `start_day`, `end_day`, and `episodes` from the Rest Mode route.

## Conflicts in the vendor's own sources

The Oura sources disagree on these points:

- Lowest heart rate: the API says `lowest_heart_rate` comes from 30-second samples, and the app shows the lowest 5-minute value. The enterprise help lists the lowest heart rate in a 5-minute window as the API metric ([API docs](https://cloud.ouraring.com/v2/docs), [Metrics Available](https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API)).
- Access token life: one API page says tokens typically expire after 24 hours. The API FAQ says they typically last 30 days ([API docs](https://cloud.ouraring.com/v2/docs)).
- Scopes: the authentication page lists 8 scopes. The OpenAPI file lists 9, adding `heart_health` ([Authentication](https://cloud.ouraring.com/docs/authentication), [API docs](https://cloud.ouraring.com/v2/docs)).
- Rate limits: the API overview describes two limit layers without numbers. The FAQ gives 5,000 requests per 5 minutes ([API docs](https://cloud.ouraring.com/v2/docs)).

## Not published

The sources do not publish or confirm these details. Confirm them with the user or with Oura:

- The formulas and weights of the Readiness Score, the Sleep Score, and every contributor.
- That the API `average_hrv` is RMSSD, and how null samples are handled.
- The unit of `average_hrv` and `lowest_heart_rate` in the API. The help articles give ms and bpm.
- The temperature baseline window.
- Whether `end_date` is inclusive.
- Which scope the `sleep` route needs.
- The file format and header row of the Membership Hub download.
- The export format of the Enterprise Platform. Older Oura Teams help pages returned "page not found" on 2026-10-07.
- Whether heart rate samples during a workout are finer than 5 minutes.
- The exact rule Oura uses to set `day` for a sleep period. The Oura Days article gives the 6 pm to 6 pm Sleep Day and an example in which the score goes to the date the member woke up.

## Worked example in Python

This example picks one sleep period for each day: the `long_sleep` period, or the longest if there are two. It keeps naps apart and drops `rest` periods. The records are made up. The last line shows how a plain mean of every period on a day mixes naps into the night.

The program and its output follow. The output came from Python 3.12 on 2026-10-07.

```python
"""Worked example: pick one Oura sleep period for each day.

The records are synthetic. They copy the shape of Oura API V2 sleep records,
with only the fields this example needs. The rule is the one in this page:
keep long_sleep, take the longest if there are two, and keep naps apart.
"""
periods = [
    {"id": "p1", "day": "2026-10-05", "type": "long_sleep", "total_sleep_duration": 26700, "average_hrv": 48},
    {"id": "p2", "day": "2026-10-05", "type": "sleep", "total_sleep_duration": 1500, "average_hrv": 71},
    {"id": "p3", "day": "2026-10-06", "type": "late_nap", "total_sleep_duration": 2400, "average_hrv": 66},
    {"id": "p4", "day": "2026-10-06", "type": "long_sleep", "total_sleep_duration": 24900, "average_hrv": 44},
    {"id": "p5", "day": "2026-10-06", "type": "long_sleep", "total_sleep_duration": 11100, "average_hrv": 52},
    {"id": "p6", "day": "2026-10-07", "type": "rest", "total_sleep_duration": 3000, "average_hrv": None},
]

main = {}
naps = []
for p in periods:
    if p["type"] == "long_sleep":
        best = main.get(p["day"])
        if best is None or p["total_sleep_duration"] > best["total_sleep_duration"]:
            main[p["day"]] = p
    elif p["type"] in ("sleep", "late_nap"):
        naps.append(p)
    # rest and deleted periods are dropped

for day in ("2026-10-05", "2026-10-06", "2026-10-07"):
    p = main.get(day)
    if p is None:
        print(f"{day}: no main sleep, average_hrv missing")
    else:
        print(f"{day}: main sleep {p['id']}, {p['total_sleep_duration'] / 60:.0f} min, average_hrv {p['average_hrv']} ms")
print("naps kept apart:", [(p["id"], p["day"], p["type"]) for p in naps])
print("naive mean of every 2026-10-06 period:",
      round(sum(p["average_hrv"] for p in periods if p["day"] == "2026-10-06") / 3, 1), "ms")
```

Output:

```text
2026-10-05: main sleep p1, 445 min, average_hrv 48 ms
2026-10-06: main sleep p4, 415 min, average_hrv 44 ms
2026-10-07: no main sleep, average_hrv missing
naps kept apart: [('p2', '2026-10-05', 'sleep'), ('p3', '2026-10-06', 'late_nap')]
naive mean of every 2026-10-06 period: 54.0 ms
```

## Sources

This page draws on these Oura sources:

- API docs, Oura API V2 documentation: <https://cloud.ouraring.com/v2/docs>, and its OpenAPI file <https://cloud.ouraring.com/v2/static/json/openapi-1.41.json>, accessed 2026-10-07.
- Authentication: <https://cloud.ouraring.com/docs/authentication>, accessed 2026-10-07.
- Using the Oura API: <https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Using-the-Oura-API>, accessed 2026-10-07.
- Oura Days, Understanding the Different Types of Oura Days in Oura API Data: <https://partnersupport.ouraring.com/hc/en-us/articles/29160913203219-Understanding-the-Different-Types-of-Oura-Days-in-Oura-API-Data>, accessed 2026-10-07.
- Metrics Available, Metrics Available via the Oura API: <https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API>, accessed 2026-10-07.
- Enterprise Support home: <https://partnersupport.ouraring.com/hc/en-us>, accessed 2026-10-07.
- HRV help, Heart Rate Variability: <https://support.ouraring.com/hc/en-us/articles/360025441974-Heart-Rate-Variability>, accessed 2026-10-07.
- Readiness help, Readiness Score: <https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score>, accessed 2026-10-07.
- Export help, Export and Share Your Oura Data: <https://support.ouraring.com/hc/en-us/articles/360025441594-Export-Share-Your-Oura-Data>, accessed 2026-10-07.
- Stone JD, Ulman HK, Tran K, et al. Assessing the accuracy of popular commercial technologies that measure resting heart rate and heart rate variability. Front Sports Act Living. 2021;3:585870. <https://doi.org/10.3389/fspor.2021.585870>, accessed 2026-10-07. Used only for the statement that the Oura app's Moment feature reports rMSSD.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
