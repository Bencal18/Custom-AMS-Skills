# Polar Team Pro data

Checked against: TeamPro API version 1.1.0 and the English Polar Team Pro user manual (built 2023-09-14), on 2026-10-02.

This file describes the Polar Team Pro API output and export format, what each metric means, and how to transform the data for analysis. Polar, Polar Team Pro, Polar Pro, and Polar Flow are trademarks of their owner. This repository is not affiliated with or endorsed by Polar.

## Get the data

Use one of these four routes:

- Web export: in the Team Pro web service, open a session in the **Activities** view, select **EXPORT**, choose the players, choose the phases, choose the variables, then select **EXPORT AS XLS** or **EXPORT AS CSV**. You can export the whole session or chosen phases. Polar does not state the row level. The choices suggest one row per player for each phase or session. Confirm this on a real file.
- Summary report export: in the **Reports** section, a summary report exports to CSV, one file for each chosen player. Polar does not publish its columns.
- Raw export: in the **EXPORT** view, choose players, then select **EXPORT RAW DATA**. You get a zip file with one folder for each player. Each folder holds a CSV file with second-by-second data, a `.txt` file with unfiltered RR intervals, and a GPX file with location.
- API: the TeamPro API at `https://teampro.api.polar.com/`. A coach authorizes access with OAuth2.

Follow these steps to use the API:

1. Register a client at `https://admin.polaraccesslink.com/` with a Polar account. Leave the data subscriptions empty.
2. Send the coach to `https://auth.polar.com/oauth/authorize` with `response_type=code` and `scope=team_read`. The coach grants access to team and player exercise data.
3. Exchange the returned code at `https://auth.polar.com/oauth/token`. Send HTTP Basic authentication built from the client ID and secret, and `grant_type=authorization_code`.
4. Send the access token as `Authorization: Bearer <token>`. The token lasts 12 hours. Renew it with `grant_type=refresh_token`.
5. Keep to 1 request per second. The API allows bursts of up to 100 requests and returns HTTP 429 when you go over.

The API is read-only (`team_read`). The API reference links a license agreement. I did not read it.

Follow these rules for dates and times:

- API date-times follow ISO 8601. The samples show no offset on `start_time` (`2017-04-14T09:20:06`) and a `Z` on `created`. Polar says `trimmed_start_time` is local time. The time zone of the other fields is Not published.
- Time in a zone is an ISO 8601 duration, for example `PT4.2S`.
- The date and time format of the web export is Not published.

## API output

The API wraps every response in `data`. List endpoints add a `page` object.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /v1/teams` | Teams, paged | `id`, `name`, `organisation`, `created`, `modified` |
| `GET /v1/teams/{team_id}` | One team with its roster and sport profiles | `players[]` (`player_id`, `player_number`, `role`, `first_name`, `last_name`), `sport_profiles[]` |
| `GET /v1/teams/{team_id}/sport-profiles` | Zone and threshold settings for each sport | `sport`, `sprint_threshold_type`, `sprint_threshold`, `gps_state`, `muscle_load_setting`, `heart_rate_zone_type`, `speed_zone_type`, `power_zone_type`, `zones`, `acceleration_zones` |
| `GET /v1/teams/{team_id}/training_sessions` | Team sessions, paged, filtered by `since` and `until` on `record_start_time` | `id`, `team_id`, `name`, `type`, `sport`, `record_start_time`, `record_end_time`, `start_time`, `end_time` |
| `GET /v1/teams/training_sessions/{training_session_id}` | One team session | `participants[]` (`player_id`, `player_number`, `role`, `player_session_id`), `markers[]`, `heart_rate_zones[]`, `speed_zones_kmh[]`, `power_zones[]`, `distance`, `kilocalories`, `training_load`, `heart_rate_average`, `cardio_load`, `cardio_load_interpretation` |
| `GET /v1/players/{player_id}/training_sessions` | One player's sessions, paged, filtered by `since` and `until` on `start_time`, and by `type` (`ALL`, `TEAM`, `INDIVIDUAL`) | `id` (the player session ID), `type`, `sport`, `name`, `feeling`, `start_time`, `stop_time`, `duration_ms`, `timezone_offset` |
| `GET /v1/training_sessions/{player_session_id}` | One player session, with optional samples | `calories`, `distance_meters`, `training_load`, `training_benefit`, `cardio_load`, `muscle_load`, `recovery_time_ms`, `heart_rate_max`, `heart_rate_avg`, `running_index`, `ascent`, `descent`, `sprint_counter`, `product`, `samples`, `rr_intervals` |
| `GET /v1/training_sessions/{player_session_id}/session_summary` | Trimmed team session values for one player | `trimmed_start_time`, `duration_ms`, `distance_meters`, `heart_rate_*`, `speed_*_kmh`, `cadence_*`, `cardio_load`, `muscle_load`, zones, `rmssd`, `minimum_rr` |
| `GET /v1/training_sessions/{player_session_id}/phase_summaries` | One summary for each phase, with the same fields as the session summary | Same as the session summary |

Follow this nesting: team, then team session, then participant, then player session, then summary, phase summaries, and samples.

- A team session lists its players in `participants[]`. Each entry holds a `player_session_id`.
- A player session object has no team session ID. Link a player session to its team session through `participants[]`, not through the player list.
- A phase summary has no phase name or ID. Polar does not say how to match a row to a marker in `markers[]`.
- Only sessions recorded while the player was on the team roster appear.

Use these paging and filter rules:

- List endpoints return 20 items by default. Send `page` (from 0) and `per_page` (1 to 100). The `page` object returns `per_page`, `total_elements`, `page_number`, and `total_pages`.
- Send `since` and `until` as date-times. Team sessions filter on `record_start_time`. Player sessions filter on `start_time`.
- Send `samples=all`, or a comma-separated list from `distance`, `location`, `hr`, `speed`, `cadence`, `altitude`, `forward_acceleration`, and `rr`, to get samples.
- The `samples` object holds `fields` and `values`. Each row starts with an ISO 8601 time from the session start. The documentation sample rows are shorter than the `fields` list, so read the width of a real row before you parse it.
- A 404 means the ID did not match one of the user's records.

## Export columns

The web export offers the variables below. The manual lists variable names only. It does not publish the header text, the order, the time format, or units other than for heart rate. The unit column shows what Polar states. The API unit is in brackets where it helps.

| Column name | Meaning | Units |
|---|---|---|
| `Player number` | The player's team number | Number |
| `Player name` | The player's name | Text |
| `Session name` | The session name | Text |
| `Type` | The session type | Text |
| `Phase name` | The phase the row covers | Text |
| `Duration` | Length of the session or phase | Not published (API: ms) |
| `Start time` | Start of the session or phase | Not published |
| `End time` | End of the session or phase | Not published |
| `HR min (bpm)` | Lowest heart rate | bpm |
| `HR avg (bpm)` | Mean heart rate | bpm |
| `HR max (bpm)` | Highest heart rate | bpm |
| `HR min (%)` | Lowest heart rate as a share of HRmax | Percent |
| `HR avg (%)` | Mean heart rate as a share of HRmax | Percent |
| `HR max (%)` | Highest heart rate as a share of HRmax | Percent |
| `Time in HR zone` | Time in each of five heart rate zones | Not published (API: ISO 8601 duration) |
| `Total distance` | Distance covered | Not published (API: m) |
| `Distance / Min` | Distance relative to time. Polar gives no definition. | Not published |
| `Maximum speed` | Top speed | Not published (API: km/h) |
| `Average speed` | Mean speed | Not published (API: km/h) |
| `Sprints` | Count of accelerations above the sprint threshold | Count |
| `Distance in speed zone` | Distance in each of five speed zones | Not published (API: m) |
| `Number of accelerations` | Counts in each acceleration zone | Count |
| `Calories` | Estimated energy use | Not published (API: kcal) |
| `Training load score` | Older load score | No unit |
| `Cardio load` | Heart rate load (TRIMP) | No unit published |
| `Recovery time` | Estimated recovery time | Not published (API: ms) |
| `Time in power zones` | Time in each of five power zones | Not published (API: ISO 8601 duration) |
| `Muscle load in power zones` | Muscle load in each power zone | Not published |
| `Muscle load` | Mechanical work from running power | Not published (white paper: kJ) |
| `Min RR interval` | Shortest RR interval | Not published |
| `Max RR interval` | Longest RR interval | Not published |
| `Avg RR interval` | Mean RR interval | Not published |
| `HRV (RMSSD)` | Heart rate variability, RMSSD | Not published |

Cadence is not in the web export variable list. It appears in the API and in the raw export CSV. The CSV header row is Not published.

## Metric meanings

Zones, thresholds, and load settings come from each team's sport profile. Read them with `GET /v1/teams/{team_id}/sport-profiles` and store them with the data.

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `heart_rate_zones` and Time in HR zone | Time in five intensity bands | Five bands of a player's own HRmax. Defaults: 50 to 60, 60 to 70, 70 to 80, 80 to 90, and 90 to 100 percent. A band includes its lower limit and excludes its upper limit. The coach can edit the bands. | ISO 8601 duration | `heart-rate-load.md` in `load-and-wellness` | The reference file also puts a boundary value in the higher zone. Polar does not state how it treats a value at or above 100 percent of HRmax. |
| `heart_rate_avg`, `heart_rate_max`, `heart_rate_min` | Heart rate over the session or phase | Not published | bpm | `heart-rate-load.md` in `load-and-wellness` | The API returns integers. Polar does not state the averaging method. |
| `heart_rate_avg_percent` and the max and min versions | Heart rate as a share of HRmax | Heart rate relative to the player's HRmax. HRmax defaults to 220 minus age. | Percent | `heart-rate-load.md` in `load-and-wellness` | The reference file asks you to name the HRmax source. The API does not return HRmax. |
| `cardio_load` | Strain on the heart from one session | Banister TRIMP, summed from per-second heart rate. It uses resting heart rate, maximum heart rate, and gender. The web service calculates it after sync. | No unit published. A 60-minute session typically scores 70 to 130. | `heart-rate-load.md` in `load-and-wellness` | The reference file's default Banister form uses the session's mean heart rate. Polar sums per-second terms, which matches the reference file's labeled per-sample option. Polar does not publish the scaling of the sum. |
| `cardio_load_interpretation` | Session load compared with the player's usual session | Session load divided by the 90-day session average. Bands: below 0.5, 0.5 to 0.75, 0.75 to 1.25, 1.25 to 2, and 2 or more. Needs three sessions. | Integer level, labels inferred as 1 (Very low) to 5 (Very high) | None | Polar says the bands come from customer data, not firm scientific evidence. |
| Strain, Tolerance, and Cardio load status (web only) | Recent load compared with built-up load | Strain is the 7-day average daily cardio load. Tolerance is the 28-day average. Status is strain divided by tolerance. Bands: below 0.8, 0.8 to 1.0, 1.0 to 1.3, and above 1.3. | Ratio | `acwr.md` in `load-and-wellness` | This matches the coupled rolling ACWR in form. Polar attaches injury and illness wording to the bands. The reference file says ACWR does not predict injury. Report the ratio without that wording. Whether rest days count as zero is Not published. |
| `muscle_load` | Mechanical work from running power | The integral of running power over time. Not available for ice hockey or volleyball. | White paper: kJ. API: Not published. | None | An external load. Do not combine it with cardio load. Polar says it cannot be compared across sports. |
| `power_zones` | Time and muscle load in five power bands | Defaults: 70 to 85, 85 to 100, 100 to 130, 130 to 180, and over 180 percent of maximal aerobic power (MAP) | ISO 8601 duration and muscle load | None | The API says limits are in watts, but its default-profile sample matches percent of MAP. The unit is Not confirmed. |
| `training_load` | Older load score | Not published. Polar names heart rate, age, sex, weight, VO2max, training history, thresholds, and sport as inputs. | No unit. Typically 50 to 250 for a 30 to 90 minute session. | None | Do not compare it with cardio load. |
| `recovery_time_ms` | Estimated time to recover | Not published | ms | None | The manual rates it from Mild (0 to 6 hours) to Extreme (over 48 hours). |
| `distance_meters` and Total distance | Distance covered | GNSS at 10 Hz outdoors. The inertial sensor indoors. Not published beyond that. | m | `total-distance.md` in `gps-running-load` | Polar reports distance error of 1 percent or less on a 100 m straight path and 2 percent or less on a 120 m multi-directional path, from a study its white paper cites. |
| `speed_zones_kmh` and Distance in speed zone | Distance in five speed bands | Five bands set in the sport profile. Defaults are Not published. | m, with limits in km/h | `high-speed-running.md` in `gps-running-load` | Zone limits are team settings and change by edit. The default sprint rule is not speed-based. |
| `speed_avg_kmh`, `speed_max_kmh` | Mean and top speed | Not published | km/h by field name | `high-speed-running.md` in `gps-running-load` | The API types them as integers, but the sample shows decimals. |
| `sprint_counter` and Sprints | Count of accelerations above a threshold | Each acceleration above 2.8 m/s² counts once, whatever its length. The coach can switch to a speed threshold in km/h. | Count | `accelerations-decelerations.md` in `gps-running-load` | The default is an acceleration test, not a high-speed distance test. |
| `acceleration_zones_ms2` and Number of accelerations | Counts in acceleration bands | Four acceleration and four deceleration thresholds. Defaults are Not published. | Count, with limits in m/s² | `accelerations-decelerations.md` in `gps-running-load` | Polar does not publish the effort definition or minimum duration. |
| `rmssd` | Heart rate variability | Square root of the mean squared difference of successive RR intervals. Artifact handling is Not published. | Not published | None | Polar's Recovery Pro uses resting tests. A session RMSSD is not comparable. |
| `minimum_rr`, `average_rr`, `maximum_rr`, `rr_intervals` | Time between heartbeats | The raw export is unfiltered. The summary method is Not published. | Not published. The sample values fit ms. | None | One artifact can set the maximum. |
| `cadence_avg`, `cadence_max` | Running step rate | Not published | Not published | None | Not in the web export. |
| `power` sample | Running power | Rate of mechanical work from speed and acceleration, with player weight | W | None | Polar says running power definitions differ between makers. |
| `kilo_calories` and Calories | Estimated energy use | Not published for Team Pro | kcal | None | None known. |

## Transform the data

Follow these steps to turn Polar Team Pro data into the athlete, session, and measure tables from `ams-data-setup`:

1. Pull the roster from `GET /v1/teams/{team_id}`. Map each `player_id` to your `athlete_id` in the source ID table, with `source` set to `polar_team_pro`. Store `player_id` as text.
2. Ask the coach for HRmax, resting heart rate, sex, weight, and MAP for each player. The API returns none of them. Store them with the date you got them.
3. Pull the sport profiles from `GET /v1/teams/{team_id}/sport-profiles` at each import. Save zones, thresholds, `gps_state`, and `muscle_load_setting` with the import date. The API returns only the current profile.
4. Pull team sessions from `GET /v1/teams/{team_id}/training_sessions`. Page until `page_number` plus 1 equals `total_pages`. Write one row to the sessions table for each team session. Set `session_type` from `type`.
5. Pull each team session from `GET /v1/teams/training_sessions/{training_session_id}`. Keep `participants[]`. It links each `player_id` to a `player_session_id`.
6. Pull `session_summary` for each `player_session_id`. Pull `phase_summaries` only if you need phases. Pull the player session details for `training_benefit`, `running_index`, `rr_intervals`, and samples.
7. Convert times. Parse the date-times. Take `session_date` from `trimmed_start_time`, which is local time, and set `time_zone` from the team's location. Convert `PT` durations and `duration_ms` to seconds or minutes, and say which in `unit`.
8. Reshape to one row per athlete, session, and measure. Use `bilateral` for `side` and `1` for `trial_number`. Set `source_record_id` to the `player_session_id`. For zones, write one `measure_name` for each zone, for example `hr_zone_3_time_s`.
9. Give each phase its own `session_id`, for example `S0101-P1`, if you load phases. Never add phase rows to the whole-session row.
10. Remove duplicates on `player_session_id` and `measure_name`. The same player session can arrive through a team session and through the player list.
11. Keep `type=INDIVIDUAL` player sessions in a separate `session_type`. They come from a linked Flow account. Polar's own reports leave them out.
12. Check each summary. Compare the sum of `in_zone` and `out_of_heart_rate_zones` with `duration_ms`. Record any gap.
13. Throttle requests to 1 per second, and refresh the token before 12 hours pass.

## Common mistakes

These are the mistakes most often made with Polar Team Pro data:

- Comparing cardio load across players, or across HRmax changes, without the HRmax and resting heart rate settings. The API does not return them.
- Copying the sample values in the API reference. They are placeholders, and several contradict their own field types.
- Adding up phase summaries and the whole session. Phases can overlap, and a phase summary has no phase ID.
- Treating `type` as one field. A team session has `TRAINING`, `MATCH`, and similar values. A player session has `TEAM` or `INDIVIDUAL`.
- Reading team-level values, such as `cardio_load`, `heart_rate_average`, or `distance`, as a sum or a mean. Polar does not say which.
- Reading `sprint_counter` as a count of high-speed runs. The default test is an acceleration above 2.8 m/s².
- Comparing zone data after someone edited the sport profile. Polar keeps no history, so save a copy at each import.
- Assuming default speed zones. Polar does not publish them.
- Using the web export for cadence. Cadence is not in its variable list.
- Using the session summary and the session details as the same numbers. The summary returns trimmed values.
- Reading Polar's strain and tolerance bands as injury prediction.
- Comparing `training_load` with `cardio_load`. They are different methods.
- Parsing `samples` by position without checking the row width, or treating `null` in `rr_intervals` as a beat.
- Comparing a session RMSSD with a resting RMSSD.
- Ignoring that heart rate above HRmax changes zone time and TRIMP. Check for it before you use either number.
- Letting the access token run past 12 hours, or exceeding 1 request per second.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them on a real export:

- The header row, order, time format, and units of the web export, the summary report CSV, and the raw CSV.
- The row level of the web export.
- Default speed zones, and default acceleration and deceleration zones.
- What `heart_rate_zone_type` `THRESHOLD` means, and what each `gps_state` value does.
- How team-level fields combine players.
- Whether the details endpoint returns untrimmed values when the summary returns trimmed ones.
- The unit and scale of `muscle_load`, and the unit of power zone limits.
- The unit of `rr_intervals`, `rmssd`, `speed` samples, `altitude`, `forward_acceleration`, and `cadence`.
- How Team Pro handles heart rate above HRmax, missing samples, and RR artifacts.
- How `cardio_load` scales its per-second terms.
- The calculation for calories, recovery time, training load score, training benefit, walking, ascent and descent, and running index.
- Whether a changed HRmax recalculates old sessions.
- The time zone of each API date-time.
- How to match a phase summary to its marker.
- Whether strain, tolerance, and status appear in any export.

## Sources

These sources support the facts in this file:

- Polar TeamPro API reference: <https://www.polar.com/teampro-api/>, accessed 2026-10-02.
- Polar Team Pro user manual, introduction: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/introduction_to_polar_team_pro.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Export Data": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Reports": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Polar Heart Rate Zones": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Polar Speed Zones": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Sprints": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Training Load": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "RR interval": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/rr-interval.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Team Settings": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Analyze Data in Team Pro Web Service": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "Individual training": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/individual_training.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, "End Training Session": <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/end_training_session.htm>, accessed 2026-10-02.
- Polar, "Polar Team Pro System" white paper (2022-03-11): <https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf>, accessed 2026-10-02.
- Polar, "Polar Training Load Pro" white paper (2019-11-12, March 2025): <https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf>, accessed 2026-10-02. The `/sites/default/files/static/science/white-papers/` path returned a Polar redirect page, not the PDF.
- Polar, "Training Load Pro" support page: <https://support.polar.com/en/training-load-pro>, accessed 2026-10-02.
- Polar, "Polar Recovery Pro" white paper: <https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf>, accessed 2026-10-02.
- Polar, "Polar Running Power" white paper (2018-07-17): <https://polar.com/img/static/whitepapers/pdf/polar-running-power-white-paper.pdf>, accessed 2026-10-02.
- Polar, "Heart Rate Zones" guide: <https://www.polar.com/en/guide/heart-rate-zones>, accessed 2026-10-02.
- Polar, "How many players can there be on a team?": <https://support.polar.com/en/support/how_many_players_can_there_be_on_a_team>, accessed 2026-10-02.
- Polar, "Expert Insights: How TPS Turku Use Polar Team Pro to Develop Young Players" (sensor sampling rates): <https://www.polar.com/blog/tps-turku-use-polar-team-pro/>, accessed 2026-10-02.
- Falk Neto et al., Edwards and Banister TRIMP definitions, Frontiers in Physiology, 2020: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/>, accessed 2026-10-02.
