# WHOOP data

Checked against: WHOOP API v2 (OpenAPI file served at `https://api.prod.whoop.com/developer/doc/openapi.json`, API changelog entry 2026-09-23), 2026-10-07.

This file describes the WHOOP API output and the member data export, what each metric means, and how to transform the data for analysis. WHOOP is a trademark of its owner. This repository is not affiliated with or endorsed by WHOOP.

## Get the data

Use one of these routes:

- API: the WHOOP Developer Platform at `https://api.prod.whoop.com/developer`. Each athlete grants access through OAuth 2.0. You need a WHOOP membership to register an app in the WHOOP Developer Dashboard. A new app starts on the Sandbox tier, which allows 10 connected members. Higher tiers allow 100, 1,000, 5,000, and then unlimited members. You request each tier in turn, and WHOOP reviews each request by hand.
- Member data export: each athlete requests an export in the WHOOP app. The menu steps, the email delivery within 24 hours, and the 7-day link expiry are Not confirmed (support page not readable by automated check on 2026-10-07). Ask the athlete how they got the file. The support page describes the export as several CSV files, for physiological cycles, sleeps, workouts, and journal entries. That file list is also Not confirmed. WHOOP does not publish the column headers.
- Team route: WHOOP runs a team platform called WHOOP Unite. Its help pages need a login, so its export format is Not confirmed. Ask the user for a sample file.

Follow these steps to use the API:

1. Create an app in the WHOOP Developer Dashboard. Note the client ID and client secret. Register at least one redirect URL.
2. Send each athlete to `https://api.prod.whoop.com/oauth/oauth2/auth` with the scopes you need. Add the `offline` scope to receive a refresh token.
3. Exchange the returned code at `https://api.prod.whoop.com/oauth/oauth2/token`.
4. Send the access token as `Authorization: Bearer <token>` on every call. Tokens are short-lived. The `expires_in` value gives the life in seconds.
5. Refresh the token at the same token URL. Each refresh makes the old access token and the old refresh token invalid, so run one refresh at a time for each athlete.

The data scopes are:

- `read:recovery`: Recovery score, HRV, and resting heart rate.
- `read:cycles`: day Strain, average heart rate, and steps for each physiological cycle.
- `read:sleep`: sleep durations, stages, and sleep percentages.
- `read:workout`: workout Strain, heart rate, and heart rate zones.
- `read:body_measurement`: height, weight, and maximum heart rate.
- `read:profile`: name and email. Leave this scope out unless you need it.

Keep the client secret on a server. Never paste a client secret, an access token, or a refresh token into an AI tool.

The default rate limits are 100 requests per minute and 10,000 requests per day. The `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` headers show your state. Over the limit, the API returns HTTP 429.

Date and time format: ISO 8601 date-times. The documentation examples end in `Z`, which is UTC. Each cycle, sleep, and workout carries a `timezone_offset`, such as `-05:00`, for the athlete's local clock at the time. The API gives no time zone name.

## API output

All paths in this table sit under `https://api.prod.whoop.com/developer`:

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /v2/cycle` | Physiological cycles, newest first | `id`, `user_id`, `start`, `end`, `timezone_offset`, `score_state`, `score.strain`, `score.kilojoule`, `score.average_heart_rate`, `score.max_heart_rate`, `step_count` |
| `GET /v2/cycle/{cycleId}/sleep` | The sleep that belongs to one cycle | Same fields as a sleep record |
| `GET /v2/cycle/{cycleId}/recovery` | The Recovery for one cycle | Same fields as a Recovery record |
| `GET /v2/recovery` | Recoveries, newest first by sleep start | `cycle_id`, `sleep_id`, `score_state`, `score.recovery_score`, `score.hrv_rmssd_milli`, `score.resting_heart_rate`, `score.user_calibrating`, `score.spo2_percentage`, `score.skin_temp_celsius` |
| `GET /v2/activity/sleep` | Sleeps and naps, newest first | `id`, `cycle_id`, `start`, `end`, `timezone_offset`, `nap`, `score_state`, `score.stage_summary`, `score.sleep_needed`, `score.respiratory_rate`, `score.sleep_performance_percentage`, `score.sleep_consistency_percentage`, `score.sleep_efficiency_percentage` |
| `GET /v2/activity/workout` | Workouts, newest first | `id`, `start`, `end`, `timezone_offset`, `sport_name`, `score_state`, `score.strain`, `score.average_heart_rate`, `score.max_heart_rate`, `score.kilojoule`, `score.percent_recorded`, `score.zone_durations` |
| `GET /v2/user/measurement/body` | One athlete's body values | `height_meter`, `weight_kilogram`, `max_heart_rate` |
| `GET /v2/user/profile/basic` | Name and email | Do not store these in the measures table. |

A cycle is WHOOP's day. It runs from one sleep to the next, not from midnight to midnight. A cycle has one Recovery and one main sleep. It can also hold naps. The current cycle has no `end`.

Each record has a `score_state` of `SCORED`, `PENDING_SCORE`, or `UNSCORABLE`. The `score` object is present only when the state is `SCORED`.

Page through a collection with `limit` (default 10, maximum 25) and `nextToken`. Each response holds `records` and `next_token`. You have every page when `next_token` is missing. Filter with `start` and `end`. A record is returned when it occurred during or after `start`. `end` is exclusive and defaults to now.

WHOOP sends webhooks for `sleep.updated`, `sleep.deleted`, `workout.updated`, `workout.deleted`, `recovery.updated`, and `recovery.deleted`. A new record arrives as an `updated` event. There are no webhooks for cycles or body values. WHOOP retries a failed webhook five times over about one hour, so it also advises a regular job that pulls recent data again.

The v1 API is no longer supported. In v2, sleep and workout IDs are UUIDs, and cycle IDs are integers.

## Export columns

WHOOP lists the content of each CSV file in the member export but does not publish the column names. Ask the user for the header row, and map each column to the API field in this table:

| Column name | Meaning | Units |
|---|---|---|
| Physiological cycles file | Recovery score, resting heart rate, HRV, Strain, energy, heart rate, sleep onset and wake times, sleep stages, SpO2, and skin temperature. WHOOP marks SpO2 and skin temperature as WHOOP 4.0 or later. | Not published |
| Sleeps file | Total sleep time, sleep debt, sleep efficiency, sleep performance, respiratory rate, and time in light, deep, and REM sleep | Not published |
| Workouts file | Activity name, duration, Strain, heart rate zones, energy, and GPS data when enabled | Not published |
| Journal entries file | The athlete's answers to WHOOP Journal questions | None |

Do not assume the export uses the same units as the API. The API gives durations in milliseconds and energy in kilojoules. Check the export header for its units.

## Metric meanings

WHOOP Recovery, Strain, Sleep Performance, Sleep Consistency, and Sleep Need are proprietary. WHOOP does not publish their formulas. Report them as WHOOP gives them, and never recompute them. The table says what WHOOP publishes:

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `hrv_rmssd_milli` | Overnight heart rate variability | RMSSD, the root mean square of successive differences between heartbeats, measured only during sleep. How WHOOP weights or windows the night is Not confirmed (support page not readable by automated check on 2026-10-07). | ms | [HRV trends](hrv-trends.md) | A sleep value from a wrist sensor, not a timed morning reading. Do not mix it with a morning RMSSD from another device. |
| `resting_heart_rate` | Resting heart rate | Measured during sleep. The method is Not published. | bpm | [HRV trends](hrv-trends.md) | A sleep value, not a seated or supine morning reading. |
| `recovery_score` | WHOOP's readiness score for the day | Proprietary. WHOOP names HRV and resting heart rate as the two largest inputs, and lists respiratory rate, sleep against need, sleep stages, skin temperature, and SpO2 as other inputs. HRV is compared with a 30-day baseline. Weights are Not published. | % (0 to 100) | None | A proprietary composite. Report as given. |
| `user_calibrating` | Whether WHOOP is still learning a new athlete's baseline | WHOOP says calibration lasts a few days | true or false | [HRV trends](hrv-trends.md) | Exclude calibrating days from an athlete's baseline. |
| `respiratory_rate` | Breathing rate during the sleep | Not published | breaths per minute (unit from the WHOOP Sleep help article) | [Sleep trends](sleep-trends.md) | None |
| `total_in_bed_time_milli` | Time in bed | Not published | ms | [Sleep trends](sleep-trends.md) | None |
| `total_awake_time_milli` | Time awake during the sleep | Not published | ms | [Sleep trends](sleep-trends.md) | None |
| `total_light_sleep_time_milli`, `total_slow_wave_sleep_time_milli`, `total_rem_sleep_time_milli` | Time in light, slow wave (deep), and REM sleep | Staged from the wrist sensor. The method is Not published. | ms | [Sleep trends](sleep-trends.md) | Total sleep time is the sum of these three. WHOOP does not return it as one field. |
| `total_no_data_time_milli` | Time with no data from the sensor during the sleep | Not published | ms | [Sleep trends](sleep-trends.md) | Use it as a data quality flag. |
| `sleep_efficiency_percentage` | Share of time in bed spent asleep | Time asleep divided by time in bed | % | [Sleep trends](sleep-trends.md) | None |
| `sleep_performance_percentage` | WHOOP's sleep score | Proprietary. WHOOP combines sleep against need, consistency, efficiency, and stress during sleep. The API text describes only the sleep against need part. Weights are Not published. | % | None | A proprietary composite. Report as given. |
| `sleep_consistency_percentage` | How similar sleep and wake times are to the day before | Proprietary. Needs 3 nights in a row. | % | None | Report as given. |
| `sleep_needed` fields | WHOOP's sleep need, with parts for baseline, sleep debt, recent Strain, and recent naps | Proprietary | ms | None | Report as given. |
| `disturbance_count`, `sleep_cycle_count` | Number of disturbances and sleep cycles | Not published | count | [Sleep trends](sleep-trends.md) | None |
| Cycle `strain` | Day Strain | Proprietary. The OpenAPI and WHOOP 101 describe it as cardiovascular load from heart rate. A muscular load part is Not confirmed (support page not readable by automated check on 2026-10-07). Scale is 0 to 21 and not linear. | 0 to 21 | None | Report as given. Not comparable with another vendor's load. |
| Workout `strain` | Strain of one workout | Proprietary, as day Strain | 0 to 21 | None | Report as given. |
| Workout `average_heart_rate`, `max_heart_rate` | Mean and peak heart rate in the workout | Not published | bpm | [Submaximal heart rate](submaximal-heart-rate.md) | Use only when the workout is the standard submaximal test, and the workout start and end match the test stages. WHOOP gives no second-by-second series. |
| `percent_recorded` | Share of the workout with heart rate data | Not published | % | [Submaximal heart rate](submaximal-heart-rate.md) | Use it as a data quality flag. |
| `zone_durations` | Time in heart rate zones 0 to 5 | Zones use heart rate reserve, from maximum and resting heart rate. Monthly zone updates from resting heart rate are Not confirmed (support page not readable by automated check on 2026-10-07). Athletes can set the zones by hand. | ms | None | Zone limits can change over time and between athletes. |
| `max_heart_rate` (body) | WHOOP's maximum heart rate for the athlete | The estimation method, said to be the Gellish formula adjusted from recorded peaks, is Not confirmed (support page not readable by automated check on 2026-10-07). Athletes can edit it. | bpm | [Submaximal heart rate](submaximal-heart-rate.md) | Ask whether the value was measured or estimated. |
| `kilojoule` | Estimated energy used | Not published | kJ | None | None |
| `step_count` | Steps in the cycle | Not published. Added on 2026-09-23. | count | None | Covers a cycle, not a calendar day. |
| `spo2_percentage`, `skin_temp_celsius` | Blood oxygen and skin temperature during sleep | Not published. WHOOP 4.0 or later only. | %, degrees C | None | Context only in this skill. |

## Transform the data

Follow these steps to turn WHOOP API output into the athlete, session, and measure tables from `ams-data-setup`:

1. Build the athletes table with your own `athlete_id`. Store WHOOP's `user_id` as text in the source ID table. Do not store the name or email from `read:profile`.
2. Pull cycles, recoveries, and sleeps for each athlete with `start` and `end` in UTC. Page with `nextToken` until `next_token` is missing.
3. Keep only records with `score_state` equal to `SCORED`. Record `PENDING_SCORE` as missing with a `status` of `pending`, and pull it again later. Record `UNSCORABLE` as missing with a `status` of `unscorable`.
4. Split sleeps by `nap`. Use the sleep with `nap` equal to `false` for overnight HRV, resting heart rate, and sleep measures. Report nap time in minutes in its own column beside total sleep time. Never add a nap into total sleep time, and never average a nap into the night.
5. Join each Recovery to its sleep on `sleep_id`, and to its cycle on `cycle_id`.
6. Convert units. Divide `_milli` durations by 60,000 for minutes. Keep `hrv_rmssd_milli` in ms. It is already in ms.
7. Reshape to one row per athlete, date, and measure, with `session_id` set to `none`. Set `source` to `whoop` and `source_record_id` to the sleep `id` for night measures, or the cycle `id` for cycle measures.
8. Flag rows where `user_calibrating` is `true`. Leave them out of the athlete's baseline.
9. Check for edits. WHOOP rescores Recovery when an athlete edits a sleep. Pull the last 7 days again on each import, and replace rows whose `updated_at` changed.

## Common mistakes

These are the mistakes most often made with this data:

- Treating a cycle as a calendar day. A cycle runs from sleep to sleep.
- Averaging a nap into overnight HRV, or adding it into sleep time. Filter on `nap`, and report nap time in its own column.
- Comparing WHOOP HRV with a morning RMSSD from a chest strap or an app. The window differs, so the values differ.
- Recomputing Recovery or Strain. Both are proprietary. Report them as given.
- Comparing Recovery or Strain between athletes. WHOOP scales both to the athlete's own baseline.
- Treating a missing Recovery as zero. A cycle with no worn night has no Recovery.
- Expecting webhooks for cycles. Pull cycles on a schedule.
- Running two token refreshes at once. The second one fails, and the athlete must authorize again.

## Sources

This file draws on these sources:

- WHOOP API reference and OpenAPI file: <https://developer.whoop.com/api/> and <https://api.prod.whoop.com/developer/doc/openapi.json>, accessed 2026-10-07.
- WHOOP Developer Platform, Overview: <https://developer.whoop.com/docs/developing/overview>, accessed 2026-10-07.
- Getting Started: <https://developer.whoop.com/docs/developing/getting-started>, accessed 2026-10-07.
- OAuth 2.0: <https://developer.whoop.com/docs/developing/oauth>, accessed 2026-10-07.
- App Approval: <https://developer.whoop.com/docs/developing/app-approval>, accessed 2026-10-07.
- Pagination: <https://developer.whoop.com/docs/developing/pagination>, accessed 2026-10-07.
- API Rate Limiting: <https://developer.whoop.com/docs/developing/rate-limiting>, accessed 2026-10-07.
- Webhooks: <https://developer.whoop.com/docs/developing/webhooks/>, accessed 2026-10-07.
- v1 to v2 Migration Guide: <https://developer.whoop.com/docs/developing/v1-v2-migration>, accessed 2026-10-07.
- API Changelog: <https://developer.whoop.com/docs/api-changelog>, accessed 2026-10-07.
- Cycle, Recovery, Sleep, and Workout data pages: <https://developer.whoop.com/docs/developing/user-data/cycle>, <https://developer.whoop.com/docs/developing/user-data/recovery>, <https://developer.whoop.com/docs/developing/user-data/sleep>, and <https://developer.whoop.com/docs/developing/user-data/workout>, accessed 2026-10-07.
- WHOOP 101: <https://developer.whoop.com/docs/whoop-101>, accessed 2026-10-07.
- Get Current Recovery Score tutorial: <https://developer.whoop.com/docs/tutorials/get-current-recovery-score>, accessed 2026-10-07.
- WHOOP Support, How to Export Your Data: <https://support.whoop.com/s/article/How-to-Export-Your-Data>, accessed 2026-10-07.
- WHOOP Support, WHOOP Recovery: <https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US>, accessed 2026-10-07.
- WHOOP Support, Heart Rate Variability (HRV) Insights and WHOOP Metrics: <https://support.whoop.com/s/article/Heart-Rate-Variability-HRV-Insights-WHOOP-Metrics?language=en_US>, accessed 2026-10-07.
- WHOOP Support, WHOOP Cycles: <https://support.whoop.com/s/article/WHOOP-Cycles?language=en_US>, accessed 2026-10-07.
- WHOOP Support, WHOOP Sleep: <https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US>, accessed 2026-10-07.
- WHOOP Support, WHOOP Strain: <https://support.whoop.com/s/article/WHOOP-Strain?language=en_US>, accessed 2026-10-07.
- WHOOP Support, Adjusting and Calculating Max Heart Rate and Heart Rate Zones: <https://support.whoop.com/s/article/What-is-Max-Heart-Rate-and-How-Do-I-Adjust-It?language=en_US>, accessed 2026-10-07.
