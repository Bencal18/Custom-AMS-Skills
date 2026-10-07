# Oura data

Checked against: Oura API V2 (OpenAPI file `openapi-1.41.json`, served by `https://cloud.ouraring.com/v2/docs`), 2026-10-07.

This file describes the Oura API output and the member data download, what each metric means, and how to transform the data for analysis. Oura and ŌURA are trademarks of Oura Health Oy. This repository is not affiliated with or endorsed by Oura.

## Get the data

Use one of these routes:

- API: the Oura API V2 at `https://api.ouraring.com/v2/usercollection/`. Each athlete grants access through OAuth2. V2 is the only version. V1 has been shut down. Personal access tokens stopped working in December 2025. An API application can connect 10 users before Oura must approve it. Oura says the API is free for personal and commercial use.
- Member data download: each athlete logs in to the Oura Membership Hub, selects **Export data**, then **Request your data**. The file can take up to 10 days. Oura emails the athlete when it is ready. Oura says the data models follow the API V2 documentation, and durations are in seconds. The file format is Not confirmed.
- Team route: Oura's Enterprise Support Center lists a licensed **Enterprise Platform** for organizations, including coaches. Its export format is Not confirmed. Older Oura Teams export help pages returned "page not found" on 2026-10-07. Ask the user for a sample file.

Oura Ring Gen3 and later users need an active Oura Membership for their data to reach the API. Gen2 users do not.

Follow these steps to use the API:

1. Register an API application in the Oura developer portal. Note the client ID and client secret, and list the redirect URIs.
2. Send each athlete to `https://cloud.ouraring.com/oauth/authorize` with `response_type=code` and a space-separated `scope` list. Oura recommends PKCE with `code_challenge_method=S256`.
3. Exchange the returned code at `https://api.ouraring.com/oauth/token`, and keep the refresh token.
4. Send the access token as `Authorization: Bearer <token>` on every call.
5. Refresh the token at the same token URL with `grant_type=refresh_token`.

The scopes are `email`, `personal`, `daily`, `heartrate`, `workout`, `tag`, `session`, `spo2`, and `heart_health`. The `daily` scope covers daily summaries of sleep, activity, and readiness. The `heartrate` scope covers the heart rate series. The API reference does not say which scope the `sleep` route needs, so this is Not confirmed. Each athlete can switch scopes on or off when they consent. Leave out `email` and `personal` unless you need them.

Keep the client secret on a server. Never paste a client secret, an access token, or a refresh token into an AI tool.

Oura limits requests for each access token and for each application. The FAQ gives 5,000 requests per 5 minutes. Over the limit, the API returns HTTP 429 with `Retry-After`. Oura recommends one pull of history when an athlete connects, then webhooks for new data. HTTP 403 means the athlete has not granted that scope or has no active membership.

Date and time format: ISO 8601. Fields such as `bedtime_start`, `bedtime_end`, and `timestamp` carry the athlete's local offset. Heart rate samples use UTC. The `day` field is a date with no time. Oura reads `start_date` and `end_date` in the athlete's local time zone.

## API output

All paths in this table sit under `https://api.ouraring.com`:

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /v2/usercollection/sleep` | Every sleep period, including naps. A day can have several. | `id`, `day`, `type`, `period`, `bedtime_start`, `bedtime_end`, `average_hrv`, `hrv`, `average_heart_rate`, `lowest_heart_rate`, `heart_rate`, `average_breath`, `total_sleep_duration`, `deep_sleep_duration`, `light_sleep_duration`, `rem_sleep_duration`, `awake_time`, `time_in_bed`, `latency`, `efficiency`, `restless_periods`, `readiness`, `low_battery_alert`, `sleep_algorithm_version` |
| `GET /v2/usercollection/daily_readiness` | One Readiness document per day | `id`, `day`, `score`, `contributors`, `temperature_deviation`, `temperature_trend_deviation`, `timestamp` |
| `GET /v2/usercollection/daily_sleep` | One Sleep Score document per day | `id`, `day`, `score`, `contributors`, `timestamp` |
| `GET /v2/usercollection/heartrate` | Heart rate samples, day and night | `timestamp`, `timestamp_unix`, `bpm`, `source` |
| `GET /v2/usercollection/workout` | Workouts | `id`, `day`, `activity`, `start_datetime`, `end_datetime`, `intensity`, `calories`, `distance`, `source` |
| `GET /v2/usercollection/rest_mode_period` | Periods when the athlete turned on Rest Mode | `start_day`, `end_day`, `episodes` |

Each list response holds `data` and `next_token`. Send `next_token` back to get the next page. You have every page when it is null. Filter the daily and sleep routes with `start_date` and `end_date`, and the heart rate route with `start_datetime` and `end_datetime`. Whether `end_date` is inclusive is Not published. Test it on a known date. Add `fields` to return fewer fields.

The `hrv` and `heart_rate` objects in a sleep record hold `interval` (seconds between samples), `items` (the values, which can be null), and `timestamp` (start of the series). Oura's enterprise help lists both series at 5-minute resolution.

Sleep data reach the API only after the athlete opens the Oura app and syncs the ring. Readiness is calculated after that. Heart rate and daily activity sync in the background.

Oura webhooks cover `sleep`, `daily_sleep`, `daily_readiness`, `workout`, and other data types, for `create`, `update`, and `delete` events. A subscription uses the `x-client-id` and `x-client-secret` headers, has an expiry time, and must be renewed. Verify each event with the `x-oura-signature` header. Notifications arrive about 30 seconds after a sync. Your endpoint must reply within 10 seconds.

## Export columns

Oura says the member download follows the API V2 data models, so the column names should match the API fields. The file format and header row are Not confirmed. Ask the user for the header row. These are the fields to look for:

| Column name | Meaning | Units |
|---|---|---|
| `day` | The day the record belongs to | date |
| `average_hrv` | Mean overnight HRV for one sleep period | ms |
| `lowest_heart_rate`, `average_heart_rate` | Lowest and mean heart rate in one sleep period | bpm |
| `total_sleep_duration`, `time_in_bed`, `awake_time`, `deep_sleep_duration`, `light_sleep_duration`, `rem_sleep_duration`, `latency` | Sleep durations | s |
| `efficiency` | Sleep efficiency | 1 to 100 |
| `score` | Readiness score or Sleep Score, depending on the file | 0 to 100 on the Readiness help page. The OpenAPI gives the Readiness score as 1 to 100. |

## Metric meanings

Oura's Readiness Score, Sleep Score, and their contributors are proprietary. Oura does not publish the formulas. Report them as Oura gives them, and never recompute them. The table says what Oura publishes:

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `average_hrv` (sleep) | Mean overnight heart rate variability for one sleep period | Oura measures HRV only during sleep, in 5-minute samples. The average is the mean of all 5-minute samples while asleep. A 2021 peer-reviewed study says the Oura app's Moment feature reports average rMSSD over 5 minutes (Stone et al., 2021). The API field does not name the statistic. | ms (from the Oura HRV help article. The API does not state the unit.) | [HRV trends](hrv-trends.md) | A whole-night mean from a ring, not a timed morning reading. Do not mix it with a morning RMSSD from another device. |
| `hrv` (sleep) | The 5-minute HRV series behind `average_hrv` | As above | ms | [HRV trends](hrv-trends.md) | Oura's app also shows a Max HRV, the highest sample of the night. The API has no Max HRV field. |
| `lowest_heart_rate` (sleep) | Lowest heart rate in the sleep period | Calculated from 30-second samples. The app shows the lowest 5-minute value instead, so the two can differ. | bpm | [HRV trends](hrv-trends.md) | A sleep value, not a seated or supine morning reading. |
| `average_heart_rate` (sleep) | Mean heart rate in the sleep period | Calculated from 30-second samples. The app shows the mean of 5-minute values instead. | bpm | [HRV trends](hrv-trends.md) | As above |
| `average_breath` (sleep) | Breathing rate during sleep | Not published | breaths per minute | [Sleep trends](sleep-trends.md) | None |
| `total_sleep_duration` | Time asleep | Not published | s | [Sleep trends](sleep-trends.md) | None |
| `time_in_bed`, `awake_time`, `latency` | Time in bed, time awake, and time to fall asleep | Not published | s | [Sleep trends](sleep-trends.md) | None |
| `deep_sleep_duration`, `light_sleep_duration`, `rem_sleep_duration` | Time in each sleep stage | Staged by Oura's sleep algorithm. `sleep_algorithm_version` gives `v1` or `v2`. | s | [Sleep trends](sleep-trends.md) | Stages from two algorithm versions are not directly comparable. |
| `efficiency` | Sleep efficiency | Rating from 1 to 100. The formula is Not published. | 1 to 100 | [Sleep trends](sleep-trends.md) | Not confirmed to be time asleep divided by time in bed. |
| `restless_periods` | Number of restless periods | Not published | count | [Sleep trends](sleep-trends.md) | None |
| Readiness `score` | Oura's readiness score for the day | Proprietary. Uses short-term inputs (lowest resting heart rate and its timing, body temperature, previous night's sleep, previous day's activity) and balance inputs. The balance inputs compare a 14-day weighted average with a two-month average. Weights are Not published. | 0 to 100 on the Readiness help page, but 1 to 100 in the OpenAPI. The two sources conflict. | None | A proprietary composite. Report as given. |
| Readiness `contributors` | The parts of the readiness score: `activity_balance`, `body_temperature`, `hrv_balance`, `previous_day_activity`, `previous_night`, `recovery_index`, `resting_heart_rate`, `sleep_balance`, `sleep_regularity` | Proprietary. Each is a rating, not a raw value. | 1 to 100 | None | Use `average_hrv` and `lowest_heart_rate` for trends, not the contributor ratings. |
| `temperature_deviation`, `temperature_trend_deviation` | Body temperature against the athlete's baseline | Not published | degrees C | None | Context only in this skill. |
| Daily sleep `score` and `contributors` | Oura's Sleep Score and its parts: `deep_sleep`, `efficiency`, `latency`, `rem_sleep`, `restfulness`, `timing`, `total_sleep` | Proprietary | 0 to 100, and 1 to 100 for contributors | None | A proprietary composite. Report as given. |
| `bpm` (heart rate) | Heart rate sample | Not published. The route gives 5-minute increments. `source` tells awake, rest, sleep, workout, live, or session. | bpm | [Submaximal heart rate](submaximal-heart-rate.md) | Too coarse for a submaximal test stage unless the sample rate during a workout is finer. Check the timestamps. |
| Workout `intensity`, `calories`, `distance` | Oura's workout summary | Not published. `intensity` is easy, moderate, or hard. | none, kcal, m | None | Report as given. |

## Transform the data

Follow these steps to turn Oura API output into the athlete, session, and measure tables from `ams-data-setup`:

1. Build the athletes table with your own `athlete_id`. Do not store the email or personal fields.
2. Pull `sleep`, `daily_readiness`, and `daily_sleep` for each athlete, one to three months at a time. Page with `next_token` until it is null.
3. Use the Oura `day` field as `measure_date`. Oura sets it in the athlete's local time. Write this rule in the measure dictionary.
4. Pick one sleep period for each athlete and `day`. Use the period with `type` equal to `long_sleep`. If two exist, use the longest `total_sleep_duration`, and record the rule.
5. Report nap time in minutes in its own column beside total sleep time. A `sleep` period is a confirmed nap or short sleep. A `late_nap` ended after 6 pm and counts toward the next day. Drop `rest` and `deleted` periods. Never add a nap into total sleep time, and never average a nap into the night.
6. Keep `average_hrv` in ms, `lowest_heart_rate` and `average_heart_rate` in bpm, and convert durations from seconds to minutes.
7. Reshape to one row per athlete, date, and measure, with `session_id` set to `none`. Set `source` to `oura` and `source_record_id` to the sleep `id` for night measures, or the daily document `id` for scores.
8. Record a null value as missing, with a `status` of `missing`. A night without the ring, or a ring that was not synced, has no record.
9. Flag rows with `low_battery_alert` equal to `true`. Flag days inside a Rest Mode period. Ask the user whether to leave them out of the baseline.
10. Pull the last 7 days again on each import. An athlete can edit a bedtime, and Oura then updates the record.

## Common mistakes

These are the mistakes most often made with this data:

- Using the first sleep record of a day. A day can have naps. Pick the `long_sleep` period.
- Treating `late_nap` as part of that evening's day. Oura counts it toward the next day.
- Building a date from the UTC heart rate timestamps. Use `day`, or convert with the local offset.
- Recomputing the readiness score or Sleep Score. Both are proprietary. Report them as given.
- Trending the `hrv_balance` contributor as if it were HRV. It is a rating. Trend `average_hrv`.
- Comparing `lowest_heart_rate` from the API with the app value. The API uses 30-second samples, and the app uses 5-minute samples.
- Comparing Oura HRV with a morning RMSSD from a chest strap or an app. The window differs, so the values differ.
- Assuming today's sleep is in the API. It arrives only after the athlete opens the app.

## Sources

This file draws on these sources:

- Oura API V2 documentation: <https://cloud.ouraring.com/v2/docs>, and its OpenAPI file <https://cloud.ouraring.com/v2/static/json/openapi-1.41.json>, accessed 2026-10-07.
- Oura API authentication: <https://cloud.ouraring.com/docs/authentication>, accessed 2026-10-07.
- Oura Enterprise Support, Using the Oura API: <https://partnersupport.ouraring.com/hc/en-us/articles/20949682312211-Using-the-Oura-API>, accessed 2026-10-07.
- Oura Enterprise Support, Understanding the Different Types of Oura Days in Oura API Data: <https://partnersupport.ouraring.com/hc/en-us/articles/29160913203219-Understanding-the-Different-Types-of-Oura-Days-in-Oura-API-Data>, accessed 2026-10-07.
- Oura Enterprise Support, Metrics Available via the Oura API: <https://partnersupport.ouraring.com/hc/en-us/articles/28571089902227-Metrics-Available-via-the-Oura-API>, accessed 2026-10-07.
- Oura Enterprise Support Center home page: <https://partnersupport.ouraring.com/hc/en-us>, accessed 2026-10-07.
- Oura Member Care, Heart Rate Variability: <https://support.ouraring.com/hc/en-us/articles/360025441974-Heart-Rate-Variability>, accessed 2026-10-07.
- Oura Member Care, Readiness Score: <https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score>, accessed 2026-10-07.
- Oura Member Care, Export and Share Your Oura Data: <https://support.ouraring.com/hc/en-us/articles/360025441594-Export-Share-Your-Oura-Data>, accessed 2026-10-07.
- Stone JD, Ulman HK, Tran K, et al. Assessing the accuracy of popular commercial technologies that measure resting heart rate and heart rate variability. Front Sports Act Living. 2021;3:585870. <https://doi.org/10.3389/fspor.2021.585870>, accessed 2026-10-07. Used only for the statement that the Oura app's Moment feature reports rMSSD.
