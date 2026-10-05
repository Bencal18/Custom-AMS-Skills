# Firstbeat Sports data

Checked against: Firstbeat Sports Cloud API version 1.1.0 and the Sports Cloud Data Export help article (updated 2022-08-03), on 2026-10-02.

This file describes the Firstbeat Sports Cloud API output and Data Export format, what each metric means, and how to transform the data for analysis. Firstbeat is a trademark of its owner. This repository is not affiliated with or endorsed by Firstbeat.

## Get the data

Use one of these routes:

- Web export: in Sports Cloud, open the top-left menu, then **Data Export**. Premium and Premium+ accounts have it. The export is an Excel file, not CSV. Several files are zipped. Pick a date range of up to one month, a team, and the measurement types: exercises, Quick Recovery Tests, and Stress and Recovery data. The summary file holds all selected variables for measurements, laps, and sessions, with an `Analysis period` column. Premium+ accounts can also export time series and RR data, with one file for each measurement. Exports are queued, and Firstbeat keeps each file for 30 days.
- API: the Firstbeat Sports Cloud API, served over HTTPS from host `api.firstbeat.com` under the path `/v1`. Premium accounts get access only through an API partner platform. Premium+ accounts can build their own client. Standard accounts can add partner access as a paid feature. Partners listed by Firstbeat include gpexe, XPS Network, Kinexon, Kitman Lab, Apollo V2, Teamworks, and SAP Sports One.
- Other routes into Sports Cloud: a Garmin Connect link, a single `.fit` file import, manual exercise entry, and Bodyguard 3 files for stress and recovery. These add data to Sports Cloud. They are not export routes.

To get direct API access, follow these steps:

1. Register an API consumer with `POST /account/register`. Firstbeat returns an `id` and a `sharedSecret`.
2. Email `sports-cloud-api@firstbeat.com` with the consumer name, the `id`, and the account names to link. Firstbeat approves the consumer.
3. Ask a Coach to open **Settings**, then **Cloud API** in Sports Cloud, and to tick the account for your consumer.
4. Build a JSON Web Token (JWT) signed with HS256, using `iss`, `iat`, and `exp`. A token may be valid for at most 5 minutes.
5. Call `GET /account/api-key` with the token to get the permanent API key.
6. Send `Authorization: Bearer <token>` and `x-api-key: <key>` on every other call.

Keep the shared secret private. Never paste it into an AI tool. Firstbeat says never to send it to Firstbeat support.

API limits are 1 request per second, a burst of 60 requests per minute, and 5,000 requests per day. The daily count resets at 00:00 UTC. The limits are shared by every account linked to one consumer. A response is capped at 6 MB. The API has no webhooks and no field that shows when data changed.

Date and time format: RFC 3339. `startTime` and `endTime` are in UTC and end in `Z`. `startTimeLocal` and `endTimeLocal` show the recorded local clock time with an offset, such as `+02:00`. The `fromTime` and `toTime` filters apply to the UTC `startTime`. The API does not give an IANA time zone name. The time format inside the Excel export is not confirmed.

## API output

All paths in this table sit under the `/v1` path on host `api.firstbeat.com`, over HTTPS:

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /sports/accounts` | Accounts the consumer can reach | `accountId`, `name`, `authorizedBy.coachId` |
| `GET /sports/accounts/{accountId}/athletes` | Athletes in the account | `athleteId`, `firstName`, `lastName`, `email` |
| `GET /sports/accounts/{accountId}/teams` | Teams, with groups | `teamId`, `name`, `athleteIds`, `groups` |
| `GET /sports/accounts/{accountId}/athletes/{athleteId}/measurements` | One athlete's measurements, filtered by `fromTime`, `toTime`, `exerciseType`, `measurementType`, `sportsType`, and `eventType`. Add `includeLaps` for laps. | `measurementId`, `athleteId`, `sessionId`, `startTime`, `startTimeLocal`, `endTime`, `endTimeLocal`, `measurementType`, `exerciseType`, `sportsType`, `eventType`, `notes`, `laps` |
| `GET .../measurements/{measurementId}/results` | Analysis results for one measurement. Add `var` to pick variables and `format` to set the time series format. | `variables` with `name`, `unit`, and `value` |
| `GET .../measurements/{measurementId}/laps/{lapId}/results` | Analysis results for one measurement lap | Same as above, plus `lapId` and `name` |
| `GET /sports/accounts/{accountId}/teams/{teamId}/sessions` | Coach-made sessions, filtered by `fromTime`, `toTime`, `type`, `sportsType`, and `eventType` | `sessionId`, `sessionType`, `coachId`, `athleteIds`, `startTime`, `endTime`, `eventType`, `sportsType`, `notes`, `laps` |
| `GET .../sessions/{sessionId}/results` | Analysis results for a session, one entry for each athlete's measurement | `athleteId`, `measurementId`, `variables` |
| `GET .../sessions/{sessionId}/laps/{lapId}/results` | Analysis results for a session lap | `lapId`, `athleteId`, `variables` |
| `GET /sports/sports-types` and `GET /sports/event-types` | The allowed values for `sportsType` and `eventType` | A list of values |
| `GET /sports/accounts/{accountId}/coaches` | Coaches in the account | `coachId`, `firstName`, `lastName`, `email` |

The data nest like this. An account holds athletes, coaches, and teams. A team can hold groups. An athlete has measurements. A team has sessions, which a Coach creates by choosing athletes and a time range. Measurements and sessions can have laps. A measurement, a session, or a lap has analysis results. Each result is a scalar, which is one value, or a time series, which is a list of values.

Page through long lists with `offset`. The API returns up to 1,000 rows and sets `"more": true` when more exist. Set `offset` to the number of rows you already have.

The measurement types are `exercise`, `quickRecoveryTest`, `night`, and `manual`. A `night` measurement is a Stress and Recovery measurement. A `manual` measurement has no recorded data.

Request only the variables you need, with a comma-separated `var` list, for example `?var=trimp,trimpPerMinute,heartRateAverage`. Series marked in the documentation as data-heavy, such as `rriSeries`, return only when you name them. By default, a time series arrives zlib-compressed and Base64-encoded. Set `format=list` for plain numbers, or decode it yourself, which saves bandwidth.

These status codes need handling:

- `202`: Firstbeat is still analyzing an older measurement. Wait 5 seconds and repeat the call.
- `204`: the analysis failed, and no results exist.
- `413`: the response is over 6 MB. Request fewer variables, or fewer athletes in a session result.
- `429`: you passed a limit. The `x-amzn-ErrorType` header shows `ThrottledException` for the per-minute limit and `LimitExceededException` for the daily limit.

## Export columns

The help article lists the variable names that follow. Firstbeat does not publish the header row of the Excel file. Ask the user for the header row, and map it to this list. API variable names are in code font after the column name.

The export has these general columns:

| Column name | Meaning | Units |
|---|---|---|
| `Measurement type` | `Exercise`, `Quick Recovery`, or `Stress & Recovery` | None |
| `Analysis period` | Whether the row is a measurement, a lap, or a session | None |
| `Sport` | The sport tag of the measurement or session | None |
| `Notes` | Notes written for the measurement | None |
| `Measurement Error (%)` | Share of beats flagged as artifacts after correction (`measurementError`) | % |

The intensity columns are:

| Column name | Meaning | Units |
|---|---|---|
| `Average Heart Rate (bpm)`, `Peak Heart Rate (bpm)`, `Minimum Heart Rate (bpm)` | Heart rate summary (`heartRateAverage`, `heartRatePeak`, `heartRateLowest`) | bpm |
| `Average %HRmax (%)`, `Peak %HRmax (%)`, `Minimum %HRmax (%)` | Heart rate as a share of the HRmax in the profile | % |
| `Average %VO2max (%)`, `Peak %VO2max (%)` | Estimated oxygen use as a share of the profile VO2max | % |
| `Average VO2 (ml/kg/min)`, `Peak VO2 (ml/kg/min)` | Estimated oxygen use | ml/kg/min |
| `VO2max (ml/kg/min)` | Estimated maximal oxygen uptake (`vo2max`) | ml/kg/min |
| `Average RespR (times/min)`, `Peak RespR (times/min)` | Respiration rate estimated from HRV | breaths per minute |
| `Average Ventilation (l/min)` | Estimated ventilation. The same article says Firstbeat removed ventilation from the new export, so it may be missing. | l/min |

The physiological load columns are:

| Column name | Meaning | Units |
|---|---|---|
| `Training Status (0-100)` | Training balance score (`playerStatusScore`) | 0 to 100 |
| `Aerobic TE (0.0-5.0)`, `Anaerobic TE (0.0-5.0)` | Training Effect (`aerobicTrainingEffect`, `anaerobicTrainingEffect`) | 0.0 to 5.0 |
| `EPOC Peak (ml/kg)`, `EPOC (ml/kg)` | Highest EPOC, and EPOC at the end (`epocPeak`, `epocFinal`) | ml/kg |
| `TRIMP (index)`, `TRIMP/min (index)` | Training load, and load per minute (`trimp`, `trimpPerMinute`) | index |
| `Energy Expenditure Total (kcal)` | Estimated energy use (`energyConsumptionTotal`) | kcal |
| `Acute Training Load`, `Chronic Training Load`, `ACWR` | The 7-day TRIMP sum, the 28-day TRIMP sum divided by 4, and their ratio | index, index, ratio |
| `Time Under Zones`, `Recovery training`, `Aerobic zone 1`, `Aerobic zone 2`, `Anaerobic threshold zone`, `High intensity training` | Time in each heart rate zone. These names come from the API Variables table, not the help article. In the API these are `underZonesTime` and `zone5Time` to `zone1Time`, in that order. | hh:mm:ss |

The recovery and HRV columns are:

| Column name | Meaning | Units |
|---|---|---|
| `Quick Recovery (%)` | Test result scaled to the athlete's minimum and maximum (`quickRecoveryScaledScore`) | % |
| `Quick Recovery Test (index)` | The athlete's test index (`quickRecoveryTestScore`) | index |
| `Quick recovery test (7 days average) (%)` | The 7-day average (`scaledQrtWeeklyMean`). Firstbeat also suggests a 3 or 4-day rolling average in exports. | % |
| `Quick recovery test (Time since good recovery) (Days)` | Days since a good test (`daysSinceLastGoodRecovery`) | days |
| `Overnight Recovery (%)` | Overnight recovery score. It has no matching name on the API variables page. | % |
| `Overnight recovery Index (index)` | Recovery during sleep (`sleepRecoveryIndexAbsolute`) | index |
| `Sleep duration (hh:mm:ss)` | Detected sleep time (`sleepStateTime`) | hh:mm:ss |
| `24h Stress & Recovery Balance (%)` | Stress and recovery balance over 24 hours (`firstbeatPointsStressBalance`). It exists only for 24-hour measurements. | % |
| `RMSSD (ms)`, `RMSSD Awake (ms)`, `RMSSD Sleep (ms)` | Heart rate variability (`rmssd`, `rmssdNonSleepAverage`, `rmssdSleepAverage`) | ms |
| `Relaxation time (min)`, `Stress time (min)` | Time in the recovery state and the stress state (`recoveryStateTime`, `stressStateTime`). The help article names these with minutes. The API Variables table names them `Relaxation time (hh:mm:ss)` and `Stress time (hh:mm:ss)`. The two sources conflict. | min (help article) or hh:mm:ss (API table) |

The external load and Garmin columns are:

| Column name | Meaning | Units |
|---|---|---|
| `Movement Load (index)`, `Average Movement Intensity (index)` | Accelerometer movement, and its average rate (`movementLoad`, `averageMovementIntensity`) | index |
| `Distance`, `Average Speed`, `Pace`, `Ascent`, `Descent`, `Power (W)`, `Cadence (rpm)` | Values passed through from a Garmin recording, when present | m or mi, km/h or mph, min/km or min/mi, W, rpm |

The Premium+ time series files hold these columns: `Artifact corrected heart rate`, `TRIMP`, `TRIMP / min`, `EPOC`, `Energy Expenditure` (kcal/h), `Movement Load`, `Movement Intensity`, `RMSSD 1Min Average`, `RR`, and `Artifact Corrected RR`. The export puts the EPOC and TRIMP series on a 1-second grid. These values change only every 5 seconds, so each value repeats five times. `RMSSD 1Min Average` has one value a minute. The `RR` series is raw, and the corrected series is not. Neither has a regular sampling rate.

Other Premium+ variables appear in the API and in custom reports: heart rate recovery, Movement Efficiency, and maximal intensity periods for TRIMP per minute and Movement Intensity. Their column names in the export are not confirmed. The API Variables page gives an export name for most of them, for example `HR Recovery (60s, bpm)` and `Maximal Intensity Period MI 5s`.

Firstbeat removed these variables from the new export because some variables "might not meet our quality criteria anymore": ventilation, energy from fats and carbohydrates, HF, LF, HF/LF, and SDNN. The API Variables page still lists them.

## Metric meanings

Firstbeat's models are proprietary. The table says what Firstbeat publishes and writes "Not published" where it gives no formula:

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `EPOC Peak`, `EPOC` | Predicted extra oxygen use after effort, so the recovery demand | Predicted from %VO2max and time at that intensity, using beat-to-beat data. The function is Not published. | ml/kg | None | Predicted from heartbeats, not measured from breathing gases. Firstbeat reports a mean absolute error of 13.7 ml/kg against laboratory EPOC. |
| `TRIMP` | Load from heart rate and time | Banister TRIMP, restated from the formula figure on the Firstbeat Learning Center: T x HRratio x 0.64 x e^(1.92 x HRratio), where HRratio = (HRex - HRrest) / (HRmax - HRrest). Firstbeat uses beat-to-beat heart rate and a lower intensity limit. The limit is Not published. | index | None | A mean-heart-rate TRIMP from another system gives different numbers. |
| `TRIMP/min` | Intensity of a session or drill | TRIMP divided by session duration (Firstbeat's words). The period used for laps and sessions is Not published. | index per minute | None | None |
| `Aerobic TE` | Likely effect of the session on VO2max and aerobic endurance | Based on peak EPOC and the athlete's activity class (0 to 10). The thresholds are Not published as numbers. | 0.0 to 5.0 | None | A proprietary scale. Two athletes with different activity classes are not directly comparable. The API does not return it for laps or sessions. |
| `Anaerobic TE` | Likely effect on repeated sprints and high-intensity ability | Based on detected high-intensity intervals, their length and recovery, and fatigue. Not published. | 0.0 to 5.0 | None | Same as aerobic Training Effect. |
| `Acute Training Load` | Load in the last 7 days | Sum of daily TRIMP over 7 days | index | [ACWR](acwr.md) | A sum, not a daily mean. |
| `Chronic Training Load` | Typical weekly load | Sum of daily TRIMP over 28 days, divided by 4 | index | [ACWR](acwr.md) | A weekly amount. The 28 days appear to include the acute week. |
| `ACWR` | Recent load compared with usual load | Acute load divided by chronic load. The gauge colors use limits that are Not published. | ratio | [ACWR](acwr.md) | This is the coupled rolling-sum form. Firstbeat says a high ACWR raises injury risk. The ACWR reference file does not support that claim. |
| `Training Status` | How balanced recent training is | Combines acute load, ACWR, and the last three Quick Recovery Tests. Weights are Not published. Above 70 is well balanced, 30 to 70 is moderate, and below 30 is out of balance. | 0 to 100 | None | A proprietary composite. It needs at least 3 tests in 14 days to include recovery. |
| `Movement Load` | Movement from the Sensor's accelerometer | Not published | index | None | Not comparable with another vendor's accelerometer load. |
| `Movement Intensity` | Rate of Movement Load | Average accumulation rate of Movement Load | index per minute | None | The maximal-period variables use the unit label kicks/min. |
| `Movement Efficiency` | External load relative to internal load | Described as Movement Load divided by TRIMP. The exact variable is Not confirmed. | None stated | None | A ratio of two proprietary numbers. |
| `%HRmax` | Heart rate as a share of maximum | Uses the HRmax in the profile. The formula is not printed. | % | None | A wrong HRmax shifts every value. |
| Time in heart rate zones | Minutes spent in each zone | Time with heart rate between zone limits set in %HRmax. Default limits are Not published. | min or hh:mm:ss | None | The API numbers zones from the top: `zone1Time` is the highest zone. |
| `HR Recovery` | How fast heart rate falls | The largest drop in heart rate over a rolling window. Firstbeat calculates windows of 15, 30, 60, and 120 s, and the API lists 30, 60, and 120 s. Relative values divide by HRmax. | bpm or % | None | A rolling-window maximum, not a drop from a marked stop time. |
| `RMSSD` | Beat-to-beat heart rate variability | Root mean square of successive differences in RR intervals | ms | None | The standard definition. Artifacts change it a lot. |
| `Quick Recovery Test` | Recovery snapshot from a 3-minute rest test | RMSSD and mean RR turned into a score against the athlete's history. Not published. | index | None | Personal scaling. Compare an athlete only with their own history. |
| `Quick Recovery (%)` | The test result scaled to the athlete's range | Scaled using the athlete's minimum and maximum index. Not published. | % | None | If every test is low, the scaled value can still look normal. Check `RMSSD`. |
| `Overnight recovery Index` | Strength of recovery reactions during sleep | Calculated from heart rate, HRV, and respiration over the 4 hours that start 30 minutes after going to bed | index | None | Personal scaling. |
| `Overnight Recovery (%)` | Overnight recovery score | Based on HRV and sleep duration, individualized. Not published. | % | None | A proprietary composite. |
| `Sleep duration` | Detected sleep time | Neural network on heartbeat, respiration, and movement data | hh:mm:ss | None | Against polysomnography, Firstbeat overestimated wake time by a mean 14 minutes in one study. |
| `24h Stress & Recovery Balance` | Whether recovery offsets stress over a day | Weighs the strength and duration of detected stress and recovery states. Not published. | % | None | A proprietary composite. |
| `VO2max` | Estimated maximal oxygen uptake | Not published. Described as calculated from HRV in the export. | ml/kg/min | None | Firstbeat reports about 5% error in running against laboratory VO2max. |
| `VO2`, `%VO2max` | Estimated oxygen use, and its share of VO2max | Neural network on RR data with respiration rate and on and off kinetics | ml/kg/min, % | None | Aerobic energy only. |
| `Energy Expenditure` | Estimated energy use | From VO2, the respiratory quotient, and the caloric equivalent | kcal | None | The model estimates only aerobic energy, so it may underestimate very short anaerobic efforts. This is not a concern after 2 to 3 minutes. |
| `Measurement Error` | Share of beats flagged as artifacts | Percentage of RR intervals recognized as artifacts after correction | % | None | None |
| Garmin sleep and overnight fields | Sleep Duration, Sleep Score, Resting Heart Rate, Average Last Night HRV, Peak 5-minute Last Night HRV | Garmin calculates them. Firstbeat does not describe the methods. | Not published | None | Do not mix Garmin overnight HRV with Firstbeat `RMSSD`. |

## Transform the data

Follow these steps to turn Firstbeat API output or an export into the athlete, session, and measure tables from `ams-data-setup`:

1. Pull accounts, athletes, and teams. Build the athletes table with your own `athlete_id`. Store Firstbeat's `athleteId` as text in the source ID table. Remove `firstName`, `lastName`, and `email` before you paste anything into an AI tool.
2. Pull each athlete's measurements with `GET .../athletes/{athleteId}/measurements`, using `fromTime` and `toTime` in UTC. Page with `offset` until `more` is false.
3. Pull sessions for each team. Take the athlete and measurement link from the session results. Do not use the `sessionId` in a measurement row, because a measurement can sit in several sessions and the row shows only one.
4. Pull results for each measurement, one call at a time, with a `var` list. Retry `202` after 5 seconds. Record a `204` as a missing value with a `status` of `analysis_failed`. Stay under 1 request per second.
5. Split the rows by `measurementType`. Keep `exercise`, `quickRecoveryTest`, `night`, and `manual` apart. Variables such as `rmssd` mean different things in each type.
6. Reshape to one row per athlete, date, session, measure, and trial. Set `source` to `firstbeat_sports` and `source_record_id` to `measurementId`. Take `unit` from the API `unit` field.
7. Set `measure_date` from the date in `startTimeLocal`. Keep the UTC `startTime` for ordering. Ask the user for the time zone name, because the API gives only an offset.
8. Rename the heart rate zone variables so that your table's zone 1 is the lowest zone. The API's `zone5Time` is the lowest zone. Store the zone limits next to the data. The API does not return the athlete profile, so ask the user for the limits, the HRmax, and the resting HR used.
9. Convert units after you check them. Zone times are minutes in the API and hh:mm:ss in the export. Distance and speed follow the account's unit setting.
10. Build daily TRIMP by summing `trimp` over the measurements of each athlete and day. Add manual measurements, because Firstbeat counts them. Do not add a session row on top of its measurements, and do not add laps. Put `0` on rest days.
11. Treat the acute load, chronic load, ACWR, and Training Status as daily history values. Firstbeat says the API lacks acute load, chronic load, and ACWR for days with no measurement. The known issues do not name Training Status, so whether it is missing on those days is not confirmed. If you need every day, recompute them from your daily TRIMP with the variant in the ACWR reference file, and compare with Firstbeat's `acwr` on days that have a value.
12. Keep `measurementError` as a measure. Flag rows above a limit that the user chooses, and state the limit.
13. Remove duplicates. If a Garmin watch and a Sensor recorded the same activity, Firstbeat prefers the Garmin recording, so one of the two may be missing. Check for two Quick Recovery Tests on one day and keep the one Firstbeat shows, which is the higher score.
14. Pick one value for each day and measure. For recovery, use the Quick Recovery Test 7-day average for status and `RMSSD` for tracking adaptation, as Firstbeat advises. Firstbeat also suggests a 3 or 4-day rolling average in exports.

## Common mistakes

These are the mistakes most often made with Firstbeat data:

- Reading `zone1Time` as the lowest zone. In the API it is the highest zone.
- Calling the export CSV. It is Excel, and the header row is not published.
- Comparing Training Effect between athletes with different activity classes or HRmax settings. Both change the score.
- Trusting any metric from a measurement with a high `measurementError`. Check it first.
- Reading `RMSSD` from an exercise measurement as a recovery value. Use Quick Recovery Tests and overnight measurements.
- Comparing Quick Recovery Test scores between athletes. Firstbeat scales each score to the athlete's own history.
- Treating `Quick Recovery (%)` as absolute when an athlete is low on every test. Check `RMSSD` too.
- Summing session rows, measurement rows, and laps together. They overlap.
- Assuming the API returns acute load, chronic load, or ACWR for days without a measurement. It does not.
- Using the `sessionId` in a measurement row as the full session list.
- Reading TRIMP as a count of minutes or a percentage. It is an index. Chronic load is a weekly amount, not a 28-day total.
- Treating the Firstbeat ACWR as an injury predictor. ACWR describes how recent load compares with longer-term load. It does not predict injury.
- Comparing Movement Load with another vendor's accelerometer load. Formulas differ, and Firstbeat's is not published.
- Mixing Garmin overnight HRV with Firstbeat `RMSSD`.
- Using ventilation, the carbohydrate and fat energy split, HF, LF, or SDNN as if they were as reliable as TRIMP. Firstbeat dropped them from the new export.
- Comparing sessions across a change in HRmax, zone limits, or Sensor firmware without recording the change.
- Expecting the API to show changes. It has no webhooks and no modified date, so poll with `fromTime` and re-pull recent days to catch edits.

## Details that are not confirmed

Do not assume these details. Ask the user, or check Sports Cloud:

- The header row of the Excel export, and the time format inside it. The export names in the API Variables page differ from the Data Export help article for some variables, such as `Minimum Heart rate` and `EE Total (kcal)`.
- The default HRmax age formula, the default resting HR, and the default heart rate zone limits.
- Whether the user's account changed its zone limits or names.
- The athlete's activity class, HRmax, and resting HR. The API does not return them.
- The TRIMP lower intensity limit, and whether the formula changes for women.
- The Training Effect mapping from peak EPOC and activity class.
- The Training Status weights and the ACWR gauge limits.
- Whether Training Status is missing for days with no measurement. The known issues name only acute load, chronic load, and ACWR.
- The unit of stress time and relaxation time in the export. The API Variables table says hh:mm:ss and the help article says minutes.
- Which subscription tier includes Training Status, Movement Load, and Movement Intensity. Firstbeat's pages disagree.
- Whether Garmin overnight metrics appear in the API or the export.
- Whether the Sports Cloud `vo2max` comes from the heart rate and speed method or from an HRV method.
- The Firstbeat SPORTS 4.7 User Guide. Its host did not resolve on 2026-10-02, so this file does not use it.

## Sources

- Firstbeat Sports Cloud API documentation: <https://apidocs.firstbeat.com/>, accessed 2026-10-02.
- API Variables: <https://apidocs.firstbeat.com/variables/>, accessed 2026-10-02.
- Getting started (registration and authentication): <https://apidocs.firstbeat.com/getting-started/>, accessed 2026-10-02.
- Querying the API: <https://apidocs.firstbeat.com/querying-the-api/>, accessed 2026-10-02.
- Basic concepts: <https://apidocs.firstbeat.com/basic-concepts/>, accessed 2026-10-02.
- Usage limits: <https://apidocs.firstbeat.com/usage-limits/>, accessed 2026-10-02.
- Troubleshooting: <https://apidocs.firstbeat.com/troubleshooting/>, accessed 2026-10-02.
- Known issues: <https://apidocs.firstbeat.com/known-issues/>, accessed 2026-10-02.
- FAQ: <https://apidocs.firstbeat.com/faq/>, accessed 2026-10-02.
- Changelog: <https://apidocs.firstbeat.com/changelog/>, accessed 2026-10-02.
- API Specification (version 1.1.0): <https://apidocs.firstbeat.com/api-specification/>, accessed 2026-10-02.
- Feature: Firstbeat Sports Data Export: <https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export>, accessed 2026-10-02.
- Feature: Garmin Health API: <https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API>, accessed 2026-10-02.
- Feature: Firstbeat Sports Training Status: <https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status>, accessed 2026-10-02.
- Feature: Heart Rate Recovery: <https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery>, accessed 2026-10-02.
- Feature: Manual Exercise Input: <https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- How to perform the Quick Recovery Test with the Coach app: <https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app>, accessed 2026-10-02.
- Coach app troubleshooting, higher error percentages: <https://support.firstbeatsports.com/hc/en-us/articles/360017022358-Coach-app-troubleshooting-What-can-cause-higher-error-percentages-in-Firstbeat-Sports-Sensor-data>, accessed 2026-10-02.
- Trim and merge measurements: <https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud>, accessed 2026-10-02.
- Edit or delete measurements: <https://support.firstbeatsports.com/hc/en-us/articles/360016072097-How-to-edit-or-delete-individual-measurements-in-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- Firstbeat Sports Sensor technical specifications: <https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications>, accessed 2026-10-02.
- Firstbeat Learning Center, glossary: <https://firstbeat.com/en/professional-sports/learning-center/glossary>, accessed 2026-10-02.
- Learning Center, Interpreting training data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/>, accessed 2026-10-02.
- Learning Center, Interpreting recovery data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/>, accessed 2026-10-02.
- Learning Center, Interpreting movement data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/>, accessed 2026-10-02.
- Learning Center, Introduction to Firstbeat Sports: <https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/>, accessed 2026-10-02.
- Firstbeat Sports Guide, Understanding Athlete Training Load: <https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf>, accessed 2026-10-02.
- Firstbeat white paper, EPOC: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf>, accessed 2026-10-02.
- Firstbeat white paper, Training Effect: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf>, accessed 2026-10-02.
- Firstbeat white paper, Anaerobic Training Effect: <https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf>, accessed 2026-10-02.
- Firstbeat white paper, VO2max estimation: <https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf>, accessed 2026-10-02.
- Firstbeat white paper, VO2 estimation: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_vo2_estimation.pdf>, accessed 2026-10-02.
- Firstbeat white paper, energy expenditure: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf>, accessed 2026-10-02.
- Firstbeat white paper, recovery analysis: <https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf>, accessed 2026-10-02.
- Firstbeat white paper, stress and recovery: <https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf>, accessed 2026-10-02.
- Firstbeat white paper, sleep analysis: <https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf>, accessed 2026-10-02.
- Parak and Korhonen, accuracy of the Bodyguard 2: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf>, accessed 2026-10-02.
- Firstbeat news, Garmin sleep data integration (2026-02-05): <https://www.firstbeat.com/en/news/firstbeat-sports-announces-integration-of-garmin-sleep-data-to-enhance-recovery-insights-for-athletes/>, accessed 2026-10-02.
- Firstbeat, What's new in Sports products: <https://www.firstbeat.com/en/whats-new-sports-products/>, accessed 2026-10-02.
- Firstbeat Sports data brochure: <https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf>, accessed 2026-10-02.
- Firstbeat, Sports API data management (partner list): <https://content.firstbeat.com/firstbeat-sports-api-data-management>, accessed 2026-10-02.
- Parak et al., 2021, chest strap and vest accuracy: <https://doi.org/10.3390/s21248411>, accessed 2026-10-02.
- Conte et al., 2025, interunit reliability of Firstbeat Sport sensors: <https://doi.org/10.1123/ijspp.2024-0289>, accessed 2026-10-02.
- Kuula and Pesonen, 2021, Firstbeat sleep stages against polysomnography: <https://doi.org/10.2196/24704>, accessed 2026-10-02.
- Gao et al., 2021, Firstbeat fitness test in rowers and paddlers: <https://doi.org/10.3389/fphys.2021.701541>, accessed 2026-10-02.
