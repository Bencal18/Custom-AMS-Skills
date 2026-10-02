# Polar Team Pro metrics

Polar Team Pro records heart rate, speed, distance, acceleration, and load for team sports with the Polar Pro sensor and strap, and shows the results in an app and a web service. This page lists every metric that Team Pro exports or returns through its API, and says how Polar calculates each one. Checked against: the TeamPro API v1.1.0, the English Polar Team Pro user manual (built 2023-09-14), and Polar white papers, 2026-10-02.

Polar, Polar Team Pro, Polar Pro, Polar Flow, and Training Load Pro are trademarks of their owners. This repository is not affiliated with or endorsed by Polar.

## How to read this page

This page has summary tables, then one block for each metric. Each metric block is a short list with these fields:

- Fields and export columns: the API field names and the web export column names for the metric.
- What it measures: one plain sentence.
- Window or phase: the part of a session the value covers, and the API objects that return it.
- Calculation: Polar's definition in paraphrase, then a formula in plain math where Polar or a cited source gives one.
- Defaults: the default settings and thresholds, with a source.
- Inputs: the data that feed the metric.
- Units: the unit, and what the API does or does not state.
- Variants: the forms the metric takes and the endpoints that return it.
- Comparison with standard methods or other vendors: a comparison only where a source supports one. "None supported by a source" means no source makes the comparison.
- What changes the number: settings, data quality, and sensor factors.
- Sources: links to the vendor documents behind the block.

Follow these rules when you use the blocks:

- A detail with no public source reads "Not published". It means Polar does not publish that detail.
- Polar's own statements are paraphrased, not quoted. Each paraphrase links to its source.
- A formula marked "restatement" is a rewrite of a Polar statement or figure for this page. Polar does not print it as text.
- A value marked "inferred" is not stated by Polar. The block says what it is inferred from.
- The API examples are documentation samples with placeholder values. Do not treat sample values as real results. Several samples contradict their own field types, and the blocks name each case.
- API field names and export column names appear in code font.
- In the summary tables, "Yes" means Polar publishes the calculation. "Partly" means Polar publishes some of it. "Not published" means Polar does not publish the calculation. For a field that holds an entry or a recorded value with no calculation, such as session labels, the column shows "Yes".

## Areas and metric counts

| Area | Metrics | What it covers |
|---|---|---|
| Heart rate | 10 | Average, maximum, minimum, percent of HRmax, zones, samples, RR intervals, RMSSD |
| Training load | 12 | Cardio load, load levels, status, muscle load, power zones, running power, load score, calories |
| Speed and distance | 12 | Distance, speed, speed zones, location, altitude, running index, GPS state |
| Accelerations | 3 | Acceleration zone counts, zone settings, forward acceleration |
| Sprints | 2 | Sprint count and sprint threshold |
| Cadence | 2 | Average and maximum cadence, cadence samples |
| Recovery | 2 | Recovery time, recovery status from linked Flow accounts |
| Session and context | 8 | Duration, times, phases, session labels, players, feeling, raw files, product |
| Total | 51 | |

## Export variable index

The web export offers 33 variables. The manual lists them by name and does not give the API counterpart. The counterpart column below matches by name and is inferred.

Source for the variable list: [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm).

| Web export variable | Likely API field | Block |
|---|---|---|
| Player number | `player_number` | [Player and participant identity](#player-and-participant-identity) |
| Player name | `first_name`, `last_name` | [Player and participant identity](#player-and-participant-identity) |
| Session name | `name` | [Session labels](#session-labels) |
| Type | `type` | [Session labels](#session-labels) |
| Phase name | Marker `name` where `marker_type` is `PHASE` | [Phases and markers](#phases-and-markers) |
| Duration | `duration_ms` | [Duration](#duration) |
| Start time | `start_time`, `trimmed_start_time` | [Session and phase times](#session-and-phase-times) |
| End time | `end_time`, `stop_time` | [Session and phase times](#session-and-phase-times) |
| HR min (bpm) | `heart_rate_min` | [Minimum heart rate](#minimum-heart-rate) |
| HR avg (bpm) | `heart_rate_avg` | [Average heart rate](#average-heart-rate) |
| HR max (bpm) | `heart_rate_max` | [Maximum heart rate](#maximum-heart-rate) |
| HR min (%) | `heart_rate_min_percent` | [Heart rate percent of HRmax](#heart-rate-percent-of-hrmax) |
| HR avg (%) | `heart_rate_avg_percent` | [Heart rate percent of HRmax](#heart-rate-percent-of-hrmax) |
| HR max (%) | `heart_rate_max_percent` | [Heart rate percent of HRmax](#heart-rate-percent-of-hrmax) |
| Time in HR zone | `heart_rate_zones[].in_zone` | [Time in heart rate zones](#time-in-heart-rate-zones) |
| Total distance | `distance_meters` | [Total distance](#total-distance) |
| Distance / Min | None found | [Distance per minute](#distance-per-minute) |
| Maximum speed | `speed_max_kmh` | [Maximum speed](#maximum-speed) |
| Average speed | `speed_avg_kmh` | [Average speed](#average-speed) |
| Sprints | `sprint_counter` | [Sprint count](#sprint-count) |
| Distance in speed zone | `speed_zones_kmh[].in_zone_meters` | [Distance in speed zones](#distance-in-speed-zones) |
| Number of accelerations | `acceleration_zones_ms2[].counter` | [Acceleration zone counts](#acceleration-zone-counts) |
| Calories | `kilo_calories` | [Calories](#calories) |
| Training load score | `training_load` | [Training load score](#training-load-score) |
| Cardio load | `cardio_load` | [Cardio load](#cardio-load) |
| Recovery time | `recovery_time_ms` | [Recovery time](#recovery-time) |
| Time in power zones | `power_zones[].in_zone` | [Power zones](#power-zones) |
| Muscle load in power zones | `power_zones[].in_zone_muscle_load` | [Power zones](#power-zones) |
| Muscle load | `muscle_load` | [Muscle load](#muscle-load) |
| Min RR interval | `minimum_rr` | [RR interval summary](#rr-interval-summary) |
| Max RR interval | `maximum_rr` | [RR interval summary](#rr-interval-summary) |
| Avg RR interval | `average_rr` | [RR interval summary](#rr-interval-summary) |
| HRV (RMSSD) | `rmssd` | [RMSSD](#rmssd) |

These API fields have no web export variable: `cadence_avg`, `cadence_max`, `training_benefit`, `running_index`, `ascent`, `descent`, `walking_duration_ms`, `walking_distance_meters`, `fat_percentage`, `carbo_percentage`, `protein_percentage`, `feeling`, and the zone limits. Cadence appears in the raw data export ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)).

## Summary tables

### Heart rate summary

This table lists the metrics in the heart rate area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Average heart rate](#average-heart-rate) | Mean heart rate over a session or phase | bpm (integer) | Not published |
| [Maximum heart rate](#maximum-heart-rate) | Highest heart rate in a session or phase | bpm (integer) | Not published |
| [Minimum heart rate](#minimum-heart-rate) | Lowest heart rate in a session or phase | bpm (integer) | Not published |
| [Heart rate percent of HRmax](#heart-rate-percent-of-hrmax) | Heart rate as a share of the player's own HRmax | Percent (integer) | Partly |
| [Time in heart rate zones](#time-in-heart-rate-zones) | Time in five heart rate bands | ISO 8601 duration | Partly |
| [Heart rate zone setup](#heart-rate-zone-setup) | Rule that turns heart rate into zones | bpm in the API sample | Partly |
| [Heart rate samples](#heart-rate-samples) | Heart rate over time | bpm (inferred) | Not published |
| [RR intervals](#rr-intervals) | Time between successive heartbeats | Not stated; ms (inferred) | Not published |
| [RR interval summary](#rr-interval-summary) | Shortest, mean, and longest RR interval | Integer; ms (inferred) | Not published |
| [RMSSD](#rmssd) | Beat-to-beat variability of the heart | Integer; ms (inferred) | Partly |

### Training load summary

This table lists the metrics in the training load area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Cardio load](#cardio-load) | Strain a session put on the heart | No unit published | Partly |
| [Cardio load level](#cardio-load-level) | Session cardio load compared with the player's usual session | Integer level (1 to 5 inferred) | Yes |
| [Cardio load status, strain, and tolerance](#cardio-load-status-strain-and-tolerance) | Recent training compared with built-up training | Ratio, no unit | Partly |
| [Muscle load](#muscle-load) | Mechanical work the muscles produced | kJ in the white paper; API unit Not published | Partly |
| [Muscle load level](#muscle-load-level) | Session muscle load compared with the player's usual session | Integer level (1 to 5 inferred) | Yes |
| [Power zones](#power-zones) | Muscle load and time in five power bands | Watts per the API text; not confirmed | Partly |
| [Running power](#running-power) | Rate of mechanical work by the muscles | Watts | Partly |
| [Training load score](#training-load-score) | Older load number tied to carbohydrate and protein use | No unit | Not published |
| [Training benefit](#training-benefit) | Label for the main training effect | Category | Not published |
| [Perceived load](#perceived-load) | Session RPE times duration | Arbitrary units | Yes |
| [Calories](#calories) | Estimated energy use | kcal | Not published |
| [Energy source shares](#energy-source-shares) | Fat, carbohydrate, and protein percentages | Percent (integer) | Not published |

### Speed and distance summary

This table lists the metrics in the speed and distance area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Total distance](#total-distance) | How far a player moved | m | Partly |
| [Distance per minute](#distance-per-minute) | Distance relative to time | Not published | Not published |
| [Average speed](#average-speed) | Mean speed | km/h by field name | Not published |
| [Maximum speed](#maximum-speed) | Top speed | km/h by field name | Not published |
| [Distance in speed zones](#distance-in-speed-zones) | Distance in five speed bands | m; limits in km/h | Partly |
| [Speed zone setup](#speed-zone-setup) | Rule that sets the five speed bands | km/h | Partly |
| [Speed and distance samples](#speed-and-distance-samples) | Speed and cumulative distance over time | `distance` in m; `speed` unit Not published | Not published |
| [Location](#location) | Where a player was | Degrees | Not published |
| [Altitude, ascent, and descent](#altitude-ascent-and-descent) | Height and total climb and drop | m for `ascent` and `descent`; `altitude` unit Not published | Not published |
| [Walking duration and distance](#walking-duration-and-distance) | Time and distance counted as walking | ms and m | Not published |
| [Running index](#running-index) | Single number for running performance | Index, no unit | Partly |
| [GPS state](#gps-state) | GPS mode set for a sport profile | Category | Not published |

### Accelerations summary

This table lists the metrics in the accelerations area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Acceleration zone counts](#acceleration-zone-counts) | Counts of accelerations and decelerations per band | Limits in m/s²; counts | Partly |
| [Acceleration and deceleration zone setup](#acceleration-and-deceleration-zone-setup) | Thresholds for the acceleration bands | m/s² | Partly |
| [Forward acceleration](#forward-acceleration) | Acceleration along the direction of travel | Not published | Not published |

### Sprints summary

This table lists the metrics in the sprints area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Sprint count](#sprint-count) | Accelerations above the sprint threshold | Count | Partly |
| [Sprint threshold setup](#sprint-threshold-setup) | Rule that makes a sprint | m/s² or km/h | Yes |

### Cadence summary

This table lists the metrics in the cadence area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Average and maximum cadence](#average-and-maximum-cadence) | Running step rate | Not published | Not published |
| [Cadence samples](#cadence-samples) | Current cadence over time | Not published | Not published |

### Recovery summary

This table lists the metrics in the recovery area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Recovery time](#recovery-time) | Estimated time to recover from a session | ms in the API | Not published |
| [Recovery status, Nightly Recharge, and sleep](#recovery-status-nightly-recharge-and-sleep) | Recovery and sleep for players with a linked Flow account | Not applicable | Partly |

### Session and context summary

This table lists the metrics in the session and context area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Duration](#duration) | Length of a session or phase | ms | Not published |
| [Session and phase times](#session-and-phase-times) | When a session or phase started and ended | ISO 8601 date-times | Not published |
| [Phases and markers](#phases-and-markers) | Labeled parts of a session, such as drills | Times and text | Yes |
| [Session labels](#session-labels) | What the session was | Text | Yes |
| [Player and participant identity](#player-and-participant-identity) | Who a row belongs to | Text and integers | Yes |
| [Feeling](#feeling) | Five-level feeling rating | Category | Yes |
| [Raw data export files](#raw-data-export-files) | Second-by-second data per player | The CSV header and units are Not published | Partly |
| [Product](#product) | Product that saved the session | Text | Yes |

## Metric details

### Heart rate

#### Average heart rate

This list gives the details for Average heart rate:

- Fields and export columns: `heart_rate_avg` (player session), `heart_rate_average` (team session). Export: HR avg (bpm).
- What it measures: The mean heart rate of one player over a session or phase.
- Window or phase: Session or phase. Summary endpoints return values for the trimmed session.
- Calculation: Polar names the field and gives no method. Polar does not say how it averages samples, or whether it filters bad samples first. How the team session field `heart_rate_average` combines players is Not published. ([API](https://www.polar.com/teampro-api/))
- Defaults: None.
- Inputs: Heart rate samples from the Polar Pro sensor. Polar describes heart rate recorded once per second ([TPS Turku article](https://www.polar.com/blog/tps-turku-use-polar-team-pro/)).
- Units: Beats per minute. The API types `heart_rate_avg` as an integer, so the value is rounded. The rounding rule is Not published. The team field `heart_rate_average` is typed as a number ([API](https://www.polar.com/teampro-api/)).
- Variants: Player session details, player session summary, phase summaries, and team session details return it. The summary endpoint returns values for the trimmed session. Whether the details endpoint returns untrimmed values is Not published ([API](https://www.polar.com/teampro-api/)).
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Strap contact, session trimming, and the phase you choose. The manual tells you to moisten the strap electrodes ([Manual: Wear sensor](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/wear_polar_pro_sensor.htm)). Trimming cannot be undone ([Manual: Analyze in web](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm)).
- Sources: [API](https://www.polar.com/teampro-api/), [TPS Turku article](https://www.polar.com/blog/tps-turku-use-polar-team-pro/), [Manual: Wear sensor](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/wear_polar_pro_sensor.htm), [Manual: Analyze in web](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm).

#### Maximum heart rate

This list gives the details for Maximum heart rate:

- Fields and export columns: `heart_rate_max`. Export: HR max (bpm).
- What it measures: The highest heart rate recorded for a player in the session or phase.
- Window or phase: Session or phase.
- Calculation: Not published. Polar does not say whether it filters spikes. ([API](https://www.polar.com/teampro-api/))
- Defaults: None.
- Inputs: Heart rate samples.
- Units: Beats per minute, integer ([API](https://www.polar.com/teampro-api/)).
- Variants: Player session details, player session summary, and phase summaries.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Strap contact, trimming, and the phase you choose. This value is a session result. It is not the HRmax setting that drives zones. Whether Team Pro updates the HRmax setting from session maximums is Not published.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Minimum heart rate

This list gives the details for Minimum heart rate:

- Fields and export columns: `heart_rate_min`. Export: HR min (bpm).
- What it measures: The lowest heart rate recorded for a player in the session or phase.
- Window or phase: Session summary and phase summaries.
- Calculation: Not published. The field exists only in the summary and phase summary objects ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Heart rate samples.
- Units: Beats per minute, integer.
- Variants: Player session summary and phase summaries.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Warm-up and cool-down time inside the trimmed window, and strap contact. Whether Polar removes low or missing samples first is Not published.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Heart rate percent of HRmax

This list gives the details for Heart rate percent of HRmax:

- Fields and export columns: `heart_rate_avg_percent`, `heart_rate_max_percent`, `heart_rate_min_percent`. Export: HR avg (%), HR max (%), HR min (%).
- What it measures: Heart rate as a share of the player's own maximum heart rate.
- Window or phase: Session summary and phase summaries only.
- Calculation: Polar shows heart rate in beats per minute and as a percent of the individual maximum heart rate ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). Formula, restatement: percent = bpm divided by HRmax, times 100. Polar does not print the rounding rule.
- Defaults: HRmax defaults to 220 minus age. Polar recommends a measured value from a hard session or test ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Inputs: Heart rate and the HRmax setting in the player profile ([Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm)).
- Units: Percent, integer ([API](https://www.polar.com/teampro-api/)).
- Variants: Average, maximum, and minimum, in the summary and phase summaries only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The HRmax setting. The API does not return HRmax, so you cannot rebuild the percent without asking the coach. The sample in the API reference shows 120 bpm as 79 percent and 160 bpm as 96 percent. Those two pairs imply different HRmax values, so the sample is not usable as a check ([API](https://www.polar.com/teampro-api/)). Whether a changed HRmax setting recalculates old sessions is Not published.
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm), [API](https://www.polar.com/teampro-api/).

#### Time in heart rate zones

This list gives the details for Time in heart rate zones:

- Fields and export columns: `heart_rate_zones[]` with `index`, `lower_limit`, `higher_limit`, `in_zone`, and on team sessions `in_zone_meters`; `out_of_heart_rate_zones`. Export: Time in HR zone.
- What it measures: How long a player spent in each of five intensity bands.
- Window or phase: Session or phase. Player summary and phase summaries return time. Team session details return time and distance.
- Calculation: Polar sets zones as percentages of the player's own maximum heart rate. The same percentages apply to the whole team, so the beats-per-minute limits differ by player ([Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm)). The API gives time as an ISO 8601 duration, for example `PT4S` ([API](https://www.polar.com/teampro-api/)). Polar states that a sport profile zone includes its lower limit and excludes its upper limit ([API](https://www.polar.com/teampro-api/)).
- Defaults: Zone 1 is 50 to 60 percent of HRmax, zone 2 is 60 to 70, zone 3 is 70 to 80, zone 4 is 80 to 90, and zone 5 is 90 to 100 ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Polar guide](https://www.polar.com/en/guide/heart-rate-zones)). The manual names the zones Very light, Light, Moderate, Hard, and Maximum ([Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm)).
- Inputs: Heart rate samples, the HRmax setting, and the sport profile zone settings.
- Units: Time as an ISO 8601 duration. Limits in beats per minute. `in_zone_meters` is distance in the zone, in meters.
- Variants: Player summary and phase summaries return time only. Team session details return time and distance per zone. How team-level zone values combine players is Not published. `out_of_heart_rate_zones` is the time outside all zones. Whether it includes time above 100 percent is Not published.
- Comparison with standard methods or other vendors: Edwards TRIMP weights time in these same five bands by 1, 2, 3, 4, and 5. The cited paper writes the bands as 50 to 59, 60 to 69, and so on ([Falk Neto et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/)). Polar does not export an Edwards value. You can compute one from `in_zone` only when the zones are the default percentages.
- What changes the number: The HRmax setting, the zone type (default, free, or threshold), strap contact, and trimming. The manual's example table lists zone 1 as 104 to 114 bpm for HRmax 190, but 50 percent of 190 is 95 (see the worked example). The other four rows match the percentages. Treat the 104 as a likely misprint and ask before you rely on it ([Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm)).
- Sources: [Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm), [API](https://www.polar.com/teampro-api/), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Polar guide](https://www.polar.com/en/guide/heart-rate-zones), [Falk Neto et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/).

#### Heart rate zone setup

This list gives the details for Heart rate zone setup:

- Fields and export columns: `heart_rate_zone_type`, `zones.heart_rate[]` with `lower_limit` and `higher_limit` (sport profile).
- What it measures: The rule that turns heart rate into zones for one sport profile.
- Window or phase: A sport profile. The API returns only the current profile and its `modified` date.
- Calculation: The type is `DEFAULT`, `FREE`, or `THRESHOLD` ([API](https://www.polar.com/teampro-api/)). The manual explains percent-of-HRmax zones and how to pick **Free** to edit them ([Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm)). What `THRESHOLD` means is Not published.
- Defaults: See time in heart rate zones.
- Inputs: Sport profile settings in the web service.
- Units: Beats per minute in the API sample. Whether limits are percent or beats per minute for each type is Not confirmed.
- Variants: One profile per sport per team, returned by `GET /v1/teams/{team_id}/sport-profiles` and inside team details.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Any edit to the profile. The API returns the current profile and its `modified` date. It does not return profile history. Save a copy of the profile each season.
- Sources: [API](https://www.polar.com/teampro-api/), [Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm).

#### Heart rate samples

This list gives the details for Heart rate samples:

- Fields and export columns: the `hr` entry in `samples.fields`. Request with `samples=hr` or `samples=all`.
- What it measures: Heart rate over time within one player session.
- Window or phase: Time series within one player session.
- Calculation: The API describes the field as heart rate, as a double ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: The sensor heart rate signal. Polar describes one-second heart rate recording ([TPS Turku article](https://www.polar.com/blog/tps-turku-use-polar-team-pro/)).
- Units: Beats per minute, inferred from the metric. The sample table does not state the unit.
- Variants: Each row starts with an ISO 8601 time from the start of the session. The sample shows rows 0.1 seconds apart with `null` for missing values. The sample rows are shorter than the `fields` list, so read real responses by position and check the row width ([API](https://www.polar.com/teampro-api/)).
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Strap contact and sensor fit. How Polar fills or flags gaps is Not published.
- Sources: [API](https://www.polar.com/teampro-api/), [TPS Turku article](https://www.polar.com/blog/tps-turku-use-polar-team-pro/).

#### RR intervals

This list gives the details for RR intervals:

- Fields and export columns: `rr_intervals` (player session details). Raw export: the text file in each player folder.
- What it measures: The time between successive heartbeats.
- Window or phase: Time series within one player session (player session details).
- Calculation: The raw export holds unfiltered RR data for use in third-party heart rate variability tools ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)). The API lists `rr_intervals` as a list of integers ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: The sensor heartbeat detection.
- Units: The API does not state a unit. The sample values (485, 483, 800) fit milliseconds. This is inferred.
- Variants: The sample list contains `null` entries between values. What a `null` means is Not published. The request parameter list names `rr`, and the sample response includes `rr_intervals`. Whether the list returns only when you request `rr` is Not published ([API](https://www.polar.com/teampro-api/)).
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Strap contact and heartbeat detection. Missed or extra beats change interval lengths. Polar's white paper reports that the H10 sensor matched an ECG Holter monitor closely, but that study covers the H10, not the Pro sensor ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Sources: [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm), [API](https://www.polar.com/teampro-api/), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf).

#### RR interval summary

This list gives the details for RR interval summary:

- Fields and export columns: `minimum_rr`, `average_rr`, `maximum_rr`. Export: Min RR interval, Avg RR interval, Max RR interval.
- What it measures: The shortest, mean, and longest RR interval in a session or phase.
- Window or phase: Session summary and phase summaries.
- Calculation: Not published ([Manual: RR interval](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/rr-interval.htm)). Whether Polar filters artifacts before it calculates these values is Not published. The raw text export is unfiltered.
- Defaults: None.
- Inputs: RR intervals.
- Units: Integer. The API does not state a unit. The sample values (200, 250, 300) fit milliseconds. This is inferred.
- Variants: Player summary and phase summaries.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Artifacts such as a missed beat produce a very long interval. A single artifact can set the maximum.
- Sources: [Manual: RR interval](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/rr-interval.htm).

#### RMSSD

This list gives the details for RMSSD:

- Fields and export columns: `rmssd`. Export: HRV (RMSSD).
- What it measures: Beat-to-beat variability of the heart over a session or phase.
- Window or phase: Session summary and phase summaries.
- Calculation: Polar describes RMSSD as the square root of the mean of the squared differences between successive RR intervals ([Recovery Pro white paper](https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf)). Formula, restatement: RMSSD = sqrt(mean((RR[i+1] minus RR[i])^2)). Team Pro's artifact handling and window are Not published.
- Defaults: None.
- Inputs: RR intervals.
- Units: Integer. The API does not state a unit. RMSSD is a time value, so milliseconds is likely. This is inferred.
- Variants: Player summary and phase summaries.
- Comparison with standard methods or other vendors: The Recovery Pro white paper uses RMSSD from short, standardized resting tests, not from exercise recordings ([Recovery Pro white paper](https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf)). Do not compare a training-session RMSSD with a resting RMSSD.
- What changes the number: Exercise intensity, artifacts, and the window. A session mean mixes rest and effort.
- Sources: [Recovery Pro white paper](https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf).

### Training load

Polar groups cardio load, muscle load, and perceived load as Training Load Pro. It calls cardio load an internal measure and muscle load an external measure ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).

#### Cardio load

This list gives the details for Cardio load:

- Fields and export columns: `cardio_load`. Export: Cardio load.
- What it measures: How much strain a session put on the heart and circulation.
- Window or phase: Session or phase. Player session details, player summary, phase summaries, and team session details.
- Calculation: Polar shows it as a training impulse (TRIMP) from heart rate and session duration. Resting heart rate, maximum heart rate, and gender affect it. The web service calculates it after sync, so it does not update in the live app ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)). Polar names Banister's TRIMP as the method and says it sums per-second terms ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)). Formula, restatement of the white paper figure: load = sum over time of x times a times e^(b times x), where x = (HR(t) minus HRrest) divided by (HRmax minus HRrest). Men use a = 0.64 and b = 1.92. Women use a = 0.86 and b = 1.67. Polar does not state how it scales per-second terms. Assumption, not Polar's: the worked example divides each one-second term by 60. That choice puts a 60-minute session at 50 to 143 for 50 to 80 percent of reserve, which brackets Polar's typical range of 70 to 130 ([Training Load Pro support page](https://support.polar.com/en/training-load-pro)).
- Defaults: A 60-minute session typically scores 70 to 130 ([Training Load Pro support page](https://support.polar.com/en/training-load-pro)).
- Inputs: Heart rate each second, resting heart rate, maximum heart rate, and gender.
- Units: No unit is published. Polar shows an absolute number.
- Variants: Player session details, player summary, phase summaries, and team session details. How the team value combines players is Not published. The API sample shows 27.2, 27.3, and 27.5 for the same session across endpoints, which is placeholder data.
- Comparison with standard methods or other vendors: Polar's cardio load is Banister TRIMP, an exponential weighting of heart rate reserve. Edwards TRIMP uses fixed weights 1 to 5 by zone ([Falk Neto et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/)). The two do not give the same number. Polar names two limits of the Banister method: heart rate is a poor measure of short, very hard efforts, and the weights separate only men from women ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- What changes the number: The HRmax and resting heart rate settings, gender, strap contact, trimming, and phases. The API returns none of those settings.
- Sources: [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm), [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [Training Load Pro support page](https://support.polar.com/en/training-load-pro), [Falk Neto et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/).

#### Cardio load level

This list gives the details for Cardio load level:

- Fields and export columns: `cardio_load_interpretation`.
- What it measures: How hard a session was compared with the player's usual session.
- Window or phase: Compared with the average session of the last 90 days. Team session details and player summaries.
- Calculation: Polar divides the session's cardio load by the average session over the last 90 days. The level is Very low below 0.5 times, Low from 0.5 to 0.75, Medium from 0.75 to 1.25, High from 1.25 to 2, and Very high at 2 or more. It needs at least three sessions in the 90 days ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- Defaults: The boundaries above. Polar says they come from analysis of customer data and do not rest on firm scientific evidence ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- Inputs: The session's cardio load and the 90-day session history.
- Units: Integer in the API ([API](https://www.polar.com/teampro-api/)).
- Variants: Team session details and player summaries return it.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The player's recent history. A load that scored Medium earlier can score Low later ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)). The API does not map the integer to a label. The Team Pro white paper lists the levels as 1 Very low to 5 Very high, so the mapping 1 to 5 is inferred ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). Whether the 90-day history includes a linked Flow account's personal sessions is Not published.
- Sources: [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [API](https://www.polar.com/teampro-api/), [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf).

#### Cardio load status, strain, and tolerance

This list gives the details for Cardio load status, strain, and tolerance:

- Fields and export columns: none in the API. Web views: roster, Cardio load report.
- What it measures: Whether recent training is below, near, or above what the player has built up.
- Window or phase: Strain is a 7-day average. Tolerance is a 28-day average. The report offers last month, last 3 months, and last 6 months.
- Calculation: Strain is the average daily cardio load over 7 days. Tolerance is the average over 28 days. Status is strain divided by tolerance ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)). Whether rest days count as zero in the average is Not published.
- Defaults: Below 0.8 is Detraining, or Recovering after overreaching in the last 14 days. 0.8 to 1.0 is Maintaining. 1.0 to 1.3 is Productive. Above 1.3 is Productive or Overreaching with an injury and illness alert. Polar needs at least three sessions in 28 days ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [Training Load Pro support page](https://support.polar.com/en/training-load-pro)).
- Inputs: Daily cardio load history.
- Units: A ratio with no unit.
- Variants: The report offers last month, last 3 months, and last 6 months ([Manual: Reports](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm)). The roster shows the status for linked players ([Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm)).
- Comparison with standard methods or other vendors: The status is an acute to chronic workload ratio. Polar cites 0.8 to 1.3 as the sweet spot and cites Blanch and Gabbett (2016) for it ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- What changes the number: Training history length and the cardio load inputs. Whether any export includes strain, tolerance, or status is Not published. The API has no field for them.
- Sources: [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [Training Load Pro support page](https://support.polar.com/en/training-load-pro), [Manual: Reports](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm), [Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm).

#### Muscle load

This list gives the details for Muscle load:

- Fields and export columns: `muscle_load`. Export: Muscle load.
- What it measures: The mechanical work a player's muscles produced in a session.
- Window or phase: Session or phase. Player session details, player summary, and phase summaries.
- Calculation: Polar says muscle load integrates running power over time and equals the positive mechanical work, in joules or kilojoules ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). The Training Load Pro paper gives it as average power times duration ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)). Formula, restatement: muscle load = sum of power times time step.
- Defaults: A 60-minute running session typically scores 700 to 1400 ([Training Load Pro support page](https://support.polar.com/en/training-load-pro)).
- Inputs: Running power, which uses speed, acceleration, and player weight ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Units: The white paper uses kilojoules. The API does not state a unit and its sample shows 34, so confirm the unit on a real export before you compare with the typical range ([API](https://www.polar.com/teampro-api/)).
- Variants: Player session details, player summary, phase summaries, and the level field. Polar turns muscle load on for running-based outdoor sports. For indoor sports a coach turns it on, and the inertial sensor supplies speed. It is not available for ice hockey or volleyball ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Comparison with standard methods or other vendors: None supported by a source. Polar says muscle load is sport-specific and cannot be compared across sports ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- What changes the number: The `muscle_load_setting` in the sport profile, player weight, and the speed source (GPS outdoors, inertial sensor indoors). After a coach changes the setting, the app needs a log out and log in ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [Training Load Pro support page](https://support.polar.com/en/training-load-pro), [API](https://www.polar.com/teampro-api/), [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm).

#### Muscle load level

This list gives the details for Muscle load level:

- Fields and export columns: `muscle_load_interpretation`.
- What it measures: How hard a session was for the muscles compared with the player's usual session.
- Window or phase: Compared with the average session of the last 90 days. Player summary and phase summaries.
- Calculation: The same 90-day comparison as cardio load level, with the same five boundaries ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- Defaults: See cardio load level.
- Inputs: The session's muscle load and the 90-day history.
- Units: Integer. The label mapping is inferred as in cardio load level.
- Variants: Player summary and phase summaries.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The player's recent history and the muscle load setting.
- Sources: [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf).

#### Power zones

This list gives the details for Power zones:

- Fields and export columns: `power_zones[]` with `index`, `lower_limit`, `higher_limit`, `in_zone`, `in_zone_muscle_load`; `out_of_power_zones`. Export: Time in power zones, Muscle load in power zones.
- What it measures: How much muscle load and time a player accumulated in each of five power bands.
- Window or phase: Not stated by the vendor.
- Calculation: Power zones show accumulated muscle load per zone. Heart rate zones show accumulated time ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). The API also returns time per zone.
- Defaults: Zone 1 is 70 to 85 percent of maximal aerobic power (MAP). Zone 2 is 85 to 100. Zone 3 is 100 to 130. Zone 4 is 130 to 180. Zone 5 is over 180 ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Inputs: Running power and the player's MAP. A coach sets MAP through maximal aerobic speed in the player profile. A linked Flow account can supply it from a running test. Without a measured value, Team Pro calculates MAP from VO2max ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Units: Limits in watts per the API text. The sample shows 70, 85, 100, 130, 180, and 400 for a `DEFAULT` profile. Those numbers match the percent-of-MAP defaults, so the unit is Not confirmed ([API](https://www.polar.com/teampro-api/)).
- Variants: The report can limit muscle load to chosen power zones ([Manual: Reports](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm)).
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: MAP, player weight, and the zone type (`power_zone_type`: `DEFAULT` or `FREE`).
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm), [API](https://www.polar.com/teampro-api/), [Manual: Reports](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm).

#### Running power

This list gives the details for Running power:

- Fields and export columns: the `power` entry in `samples.fields`.
- What it measures: The rate at which a player's muscles do mechanical work.
- Window or phase: Time series within one player session.
- Calculation: Polar defines running power as the rate of change of mechanical energy. The Team Pro version uses speed and acceleration. It ignores gradient because a court is flat ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). The wrist-based paper describes speed, acceleration, and slope as the inputs and reports a validation against force plates for that version ([Running Power white paper](https://polar.com/img/static/whitepapers/pdf/polar-running-power-white-paper.pdf)). Validation of the Team Pro version is Not published.
- Defaults: None.
- Inputs: Speed, acceleration, and player weight.
- Units: Watts. The API describes the field as an integer ([API](https://www.polar.com/teampro-api/)).
- Variants: A power sample appears in the sample table. The query list does not name `power` as a `samples` option. Whether `samples=all` returns it is Not published.
- Comparison with standard methods or other vendors: Polar says running power has several definitions and compares poorly across makers ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- What changes the number: Player weight and the speed and acceleration source.
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Running Power white paper](https://polar.com/img/static/whitepapers/pdf/polar-running-power-white-paper.pdf), [API](https://www.polar.com/teampro-api/).

#### Training load score

This list gives the details for Training load score:

- Fields and export columns: `training_load`. Export: Training load score.
- What it measures: An older Polar load number tied to carbohydrate and protein used for energy.
- Window or phase: Session. A typical range is given for a 30 to 90 minute session.
- Calculation: Polar bases it on session intensity and duration. Heart rate measures intensity. Age, sex, weight, VO2max, training history, aerobic and anaerobic thresholds, and a sport factor change the result ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)). The white paper adds calorie use and mechanical impact. It calls this the previous generation, still available and not under development ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). The formula is Not published.
- Defaults: Typically 50 to 250 for a 30 to 90 minute session ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Inputs: As listed above.
- Units: No unit.
- Variants: Team session details, player session details, summaries, and phase summaries. A team setting picks whether the web service shows Cardio load and Muscle load, Recovery time, or Score. Whether that setting changes which API fields are filled is Not published ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The player profile fields above and the sport profile.
- Sources: [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf).

#### Training benefit

This list gives the details for Training benefit:

- Fields and export columns: `training_benefit` (player session details).
- What it measures: A label for the main training effect of a session.
- Window or phase: One player session (player session details only).
- Calculation: Not published.
- Defaults: The values are `NONE`, `RECOVERY_TRAINING`, `BASIC_TRAINING`, `BASIC_TRAINING_LONG`, `BASIC_AND_STEADY_STATE_TRAINING`, `BASIC_AND_STEADY_STATE_TRAINING_LONG`, `STEADY_STATE_TRAINING`, `STEADY_STATE_AND_BASIC_TRAINING`, `STEADY_STATE_AND_BASIC_TRAINING_LONG`, `STEADY_STATE_TRAINING_PLUS`, `STEADY_STATE_AND_TEMPO_TRAINING`, `TEMPO_AND_STEADY_STATE_TRAINING`, `TEMPO_TRAINING`, `TEMPO_TRAINING_PLUS`, `TEMPO_AND_MAXIMUM_TRAINING`, `MAXIMUM_TRAINING`, `MAXIMUM_AND_TEMPO_TRAINING`, and `MAXIMUM_TRAINING_PLUS` ([API](https://www.polar.com/teampro-api/)).
- Inputs: Not published.
- Units: A category.
- Variants: Player session details only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Perceived load

This list gives the details for Perceived load:

- Fields and export columns: none in Team Pro.
- What it measures: How hard a session felt, times its duration.
- Window or phase: Whole session. Duration is part of the formula. Team Pro has no field for it.
- Calculation: Training Load Pro defines perceived load as session RPE on a 1 to 10 scale times duration ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- Defaults: A 60-minute session typically scores 180 to 360 ([Training Load Pro support page](https://support.polar.com/en/training-load-pro)).
- Inputs: RPE entered after the session and duration.
- Units: Arbitrary units.
- Variants: The Team Pro manual and API have no RPE or perceived load field. The only subjective field is `feeling`.
- Comparison with standard methods or other vendors: Session RPE (Foster et al., 2001) is the method Polar cites ([Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf)).
- What changes the number: Not applicable to Team Pro exports. Collect RPE outside Polar.
- Sources: [Training Load Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf), [Training Load Pro support page](https://support.polar.com/en/training-load-pro).

#### Calories

This list gives the details for Calories:

- Fields and export columns: `kilo_calories` (summaries), `calories` (player session details), `kilocalories` (team session details). Export: Calories.
- What it measures: Estimated energy use in a session.
- Window or phase: Session. Summaries, player session details, and team session details.
- Calculation: The Team Pro method is Not published. Polar's Smart Calories paper covers wrist devices and does not mention Team Pro. It says heart-rate-based estimates need heart rate about 30 to 50 bpm above resting heart rate ([Smart Calories white paper](https://polar.com/img/static/whitepapers/pdf/polar-smart-calories-white-paper.pdf)). Do not assume Team Pro uses that method.
- Defaults: None.
- Inputs: Not published.
- Units: Kilocalories ([API](https://www.polar.com/teampro-api/)).
- Variants: Three field names for one concept.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Player weight and other profile fields are likely inputs, but Not published.
- Sources: [Smart Calories white paper](https://polar.com/img/static/whitepapers/pdf/polar-smart-calories-white-paper.pdf), [API](https://www.polar.com/teampro-api/).

#### Energy source shares

This list gives the details for Energy source shares:

- Fields and export columns: `fat_percentage`, `carbo_percentage`, `protein_percentage` (player session details).
- What it measures: The field names say fat, carbohydrate, and protein percentages. Polar gives no further description.
- Window or phase: One player session (player session details only).
- Calculation: Not published. The manual ties the training load score to carbohydrate and protein use ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Defaults: None.
- Inputs: Not published.
- Units: Percent, integer.
- Variants: Player session details only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm).

### Speed and distance

Polar says Team Pro uses 10 Hz GNSS outdoors and picks its source and filters by data quality. Indoors it uses the inertial sensor, which has an accelerometer, gyroscope, and magnetometer ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)). Polar describes a 10 Hz GPS and a 200 Hz motion sensor in the sensor ([TPS Turku article](https://www.polar.com/blog/tps-turku-use-polar-team-pro/)).

#### Total distance

This list gives the details for Total distance:

- Fields and export columns: `distance_meters` (player), `distance` (team session). Export: Total distance.
- What it measures: How far a player moved.
- Window or phase: Session or phase. Player details, summaries, phase summaries, and team session details.
- Calculation: Not published beyond the source selection above. In a study the white paper cites, distance error was 1 percent or less on a 100 m straight path and no more than 2 percent on a 120 m multi-directional path ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Defaults: None.
- Inputs: GNSS outdoors, inertial sensor indoors.
- Units: Meters.
- Variants: Player details, summaries, phase summaries, and team session details. The `distance` sample is cumulative distance in meters ([API](https://www.polar.com/teampro-api/)).
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Satellite view, building cover, the GPS state, indoor mode, trimming, and phases. Polar says real accuracy depends on conditions ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [API](https://www.polar.com/teampro-api/).

#### Distance per minute

This list gives the details for Distance per minute:

- Fields and export columns: Export: Distance / Min. API field: none found.
- What it measures: Distance relative to time.
- Window or phase: Not published. Check the duration basis (trimmed, phase, or whole session) before you compare players.
- Calculation: Not published. The name suggests distance divided by duration. That reading is not confirmed.
- Defaults: None.
- Inputs: Not published.
- Units: Not published.
- Variants: Web export only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published. Check the duration basis (trimmed, phase, or whole session) before you compare players.
- Sources: [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm).

#### Average speed

This list gives the details for Average speed:

- Fields and export columns: `speed_avg_kmh`. Export: Average speed.
- What it measures: A player's mean speed.
- Window or phase: Session summary and phase summaries.
- Calculation: Not published. Polar does not say whether stopped time counts.
- Defaults: None.
- Inputs: Speed from the source above.
- Units: Kilometers per hour by the field name. The API types it as an integer, but the sample shows 7.9 ([API](https://www.polar.com/teampro-api/)). Treat the type as unreliable and read real values.
- Variants: Player summary and phase summaries.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The source, trimming, and the phase.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Maximum speed

This list gives the details for Maximum speed:

- Fields and export columns: `speed_max_kmh`. Export: Maximum speed.
- What it measures: A player's top speed.
- Window or phase: Session summary and phase summaries.
- Calculation: Not published. In the study the white paper cites, maximum speed error in sprints was 3 percent on a straight path and 5 percent on a multi-directional path ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Defaults: None.
- Inputs: Speed from the source above.
- Units: Kilometers per hour by the field name. Integer type, with a decimal in the sample.
- Variants: Player summary and phase summaries.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Satellite view, indoor use, and filtering.
- Sources: [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf).

#### Distance in speed zones

This list gives the details for Distance in speed zones:

- Fields and export columns: `speed_zones_kmh[]` with `index`, `lower_limit`, `higher_limit`, `in_zone_meters`; team session adds `in_zone`; `out_of_speed_zones`. Export: Distance in speed zone.
- What it measures: How far a player moved in each of five speed bands.
- Window or phase: Team session details and player summaries.
- Calculation: Polar sums distance by the speed band the player was in. The summary object reports distance only, and the team object reports distance and time ([API](https://www.polar.com/teampro-api/)).
- Defaults: There are five zones. The manual says the default zones fit a player with relatively high fitness. It does not print the limits, so the defaults are Not published ([Manual: Speed zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm)).
- Inputs: Speed and the sport profile speed zones.
- Units: Distance in meters. Limits in kilometers per hour. Session limits are integers. Sport profile limits can be decimals, as in the sample value 17.1. How Polar rounds them is Not published ([API](https://www.polar.com/teampro-api/)).
- Variants: Team session details and player summaries. `out_of_speed_zones` is distance outside the zones, in meters.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Any zone edit, the speed source, and trimming.
- Sources: [API](https://www.polar.com/teampro-api/), [Manual: Speed zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm).

#### Speed zone setup

This list gives the details for Speed zone setup:

- Fields and export columns: `speed_zone_type` (`DEFAULT` or `FREE`), `zones.speed[]` (sport profile).
- What it measures: The rule that sets the five speed bands for a sport profile.
- Window or phase: A sport profile. The API returns only the current profile.
- Calculation: A coach picks **Free** to edit the limits ([Manual: Speed zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm)). A zone includes its lower limit and excludes its upper limit. Limits are in kilometers per hour ([API](https://www.polar.com/teampro-api/)).
- Defaults: Not published.
- Inputs: Sport profile settings.
- Units: Kilometers per hour.
- Variants: One profile per sport.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Any edit. The API returns only the current profile.
- Sources: [Manual: Speed zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm), [API](https://www.polar.com/teampro-api/).

#### Speed and distance samples

This list gives the details for Speed and distance samples:

- Fields and export columns: `speed` and `distance` in `samples.fields`.
- What it measures: Speed and cumulative distance over time.
- Window or phase: Time series within one session. Request with `samples`.
- Calculation: The API calls `speed` the current speed, as a double, and `distance` the total distance moved in meters, as a double ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: The source selected for the session.
- Units: `distance` in meters. The unit of `speed` is Not published.
- Variants: Request with `samples=speed`, `samples=distance`, or `samples=all`.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: The GPS state and the source.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Location

This list gives the details for Location:

- Fields and export columns: `lat`, `lon` samples; session `latitude` and `longitude`. Raw export: GPX file.
- What it measures: Where a player was.
- Window or phase: Session start position (`latitude`, `longitude`) and a time series (`lat`, `lon`).
- Calculation: The raw export gives a GPX file for third-party tools ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)). The session `latitude` and `longitude` are the start position ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: GNSS.
- Units: Degrees, as doubles.
- Variants: The app and web service show a heat map or a line. The heat map needs a synced sensor and, for a field drawing, a field you create once ([Manual: Analyze in app](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_app.htm)). Polar says the heat map is not available indoors ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Satellite view and indoor use.
- Sources: [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm), [API](https://www.polar.com/teampro-api/), [Manual: Analyze in app](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_app.htm), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf).

#### Altitude, ascent, and descent

This list gives the details for Altitude, ascent, and descent:

- Fields and export columns: `altitude` sample, `ascent`, `descent` (player session details).
- What it measures: Height and total climb and drop.
- Window or phase: One player session (player session details only).
- Calculation: Not published. The sensor list names an accelerometer, gyroscope, and compass, and no barometer ([Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm)).
- Defaults: None.
- Inputs: Not published.
- Units: Meters for `ascent` and `descent`. The unit of the `altitude` sample is Not published.
- Variants: Player session details only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm).

#### Walking duration and distance

This list gives the details for Walking duration and distance:

- Fields and export columns: `walking_duration_ms`, `walking_distance_meters` (player session details).
- What it measures: Time and distance that Polar counts as walking.
- Window or phase: One player session (player session details only).
- Calculation: Not published. The speed cutoff for walking is Not published.
- Defaults: None.
- Inputs: Not published.
- Units: Milliseconds and meters.
- Variants: Player session details only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Running index

This list gives the details for Running index:

- Fields and export columns: `running_index` (player session details).
- What it measures: A single number for running performance.
- Window or phase: One player session (player session details only).
- Calculation: Polar's Running Index paper says it combines speed and heart rate and depends on conditions such as terrain ([Running Index white paper](https://polar.com/img/static/whitepapers/pdf/polar-running-index-white-paper.pdf)). Whether Team Pro uses the same calculation is Not published.
- Defaults: None.
- Inputs: Speed and heart rate, per the paper.
- Units: An index with no unit.
- Variants: Player session details only.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Surface and terrain, heart rate, and speed.
- Sources: [Running Index white paper](https://polar.com/img/static/whitepapers/pdf/polar-running-index-white-paper.pdf).

#### GPS state

This list gives the details for GPS state:

- Fields and export columns: `gps_state` (sport profile): `OFF`, `ON_NORMAL`, `ON_LONG`, `GPS_ON_10_HZ`, `GPS_ON_MEDIUM`.
- What it measures: The GPS mode set for a sport profile.
- Window or phase: A sport profile.
- Calculation: The API lists the values and gives no meaning ([API](https://www.polar.com/teampro-api/)). Only `GPS_ON_10_HZ` has a stated rate in its name. The meaning of the other modes is Not published.
- Defaults: Not published.
- Inputs: Sport profile settings.
- Units: A category.
- Variants: Per sport profile.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: This setting may change the sample rate or battery use, and so speed, distance, sprints, and accelerations. Polar does not say. Record the value with each season's data.
- Sources: [API](https://www.polar.com/teampro-api/).

### Accelerations

#### Acceleration zone counts

This list gives the details for Acceleration zone counts:

- Fields and export columns: `acceleration_zones_ms2[]` with `limit` and `counter` (player summary and phase summaries). Export: Number of accelerations.
- What it measures: How many accelerations and decelerations fell in each acceleration band.
- Window or phase: Session summary and phase summaries.
- Calculation: `limit` is the lower acceleration boundary of the zone in m/s². `counter` is the acceleration count in that zone ([API](https://www.polar.com/teampro-api/)). The sample shows `limit` of -3, so negative limits mark deceleration zones. Polar does not define what counts as one effort, the minimum length, or the gap between efforts.
- Defaults: Not published.
- Inputs: Forward acceleration from GNSS or the inertial sensor.
- Units: Limits in m/s². Counts as numbers.
- Variants: The sport profile holds four acceleration and four deceleration thresholds. Whether the API returns eight entries is Not published ([API](https://www.polar.com/teampro-api/)).
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: The zone edits, the GPS state, and trimming.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Acceleration and deceleration zone setup

This list gives the details for Acceleration and deceleration zone setup:

- Fields and export columns: `acceleration_zones.free_acceleration_zones`, `acceleration_zones.acceleration_zones[]`, `acceleration_zones.deceleration_zones[]` (sport profile).
- What it measures: The thresholds for the acceleration bands.
- Window or phase: A sport profile.
- Calculation: The API describes each list as four thresholds from lowest to highest. The sample shows 0.5, 1, 2, 3 for acceleration and -0.5, -1, -2, -3 for deceleration, with free zones on ([API](https://www.polar.com/teampro-api/)). The setup wizard lets a coach pick default or free for acceleration and for deceleration separately ([Manual: First time setup](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/first_time_setup.htm)).
- Defaults: Not published. The sample is a free setting and is not the default.
- Inputs: Sport profile settings.
- Units: m/s².
- Variants: One profile per sport.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Any edit.
- Sources: [API](https://www.polar.com/teampro-api/), [Manual: First time setup](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/first_time_setup.htm).

#### Forward acceleration

This list gives the details for Forward acceleration:

- Fields and export columns: the `forward_acceleration` entry in `samples.fields`.
- What it measures: Acceleration along the direction of travel.
- Window or phase: Time series within one player session.
- Calculation: The API calls it forward acceleration, as a double ([API](https://www.polar.com/teampro-api/)). Polar says the system measures horizontal acceleration ([Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Defaults: None.
- Inputs: GNSS outdoors, inertial sensor indoors.
- Units: Not published.
- Variants: The raw export CSV holds acceleration and deceleration each second ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)). The CSV header is Not published.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: The source and the GPS state.
- Sources: [API](https://www.polar.com/teampro-api/), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf), [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm).

### Sprints

#### Sprint count

This list gives the details for Sprint count:

- Fields and export columns: `sprint_counter`. Export: Sprints.
- What it measures: How many times a player's acceleration passed the sprint threshold.
- Window or phase: Session or phase. Player session details, summaries, and phase summaries.
- Calculation: Polar counts every acceleration over 2.8 m/s² as a sprint. A short three-step burst and a 20 to 30 m run each count as one sprint ([Manual: Sprints](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm)). Whether the test is greater than or greater than or equal to is Not published. The minimum gap between sprints is Not published.
- Defaults: The default threshold is an acceleration of 2.8 m/s² ([Manual: Sprints](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm)).
- Inputs: Acceleration, or speed if the coach picks a speed threshold.
- Units: A count.
- Variants: Player session details, summaries, and phase summaries.
- Comparison with standard methods or other vendors: The default is an acceleration test, not a speed test. Do not compare it with sprint counts that use a speed cutoff.
- What changes the number: The threshold type and value, the GPS state, and trimming.
- Sources: [Manual: Sprints](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm).

#### Sprint threshold setup

This list gives the details for Sprint threshold setup:

- Fields and export columns: `sprint_threshold_type` (`ACCELERATION` or `SPEED`), `sprint_threshold` (sport profile).
- What it measures: The rule that makes a sprint.
- Window or phase: A sport profile. The API returns only the current profile.
- Calculation: A coach picks default or free. Free lets the coach set a speed in km/h or an acceleration in m/s² ([Manual: Sprints](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm)).
- Defaults: 2.8 m/s².
- Inputs: Sport profile settings.
- Units: m/s² for `ACCELERATION`, km/h for `SPEED`.
- Variants: One profile per sport.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Any edit. The API returns only the current profile.
- Sources: [Manual: Sprints](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm).

### Cadence

#### Average and maximum cadence

This list gives the details for Average and maximum cadence:

- Fields and export columns: `cadence_avg`, `cadence_max` (summaries). No web export variable.
- What it measures: Running step rate.
- Window or phase: Session summary and phase summaries. The raw export CSV holds cadence each second.
- Calculation: Not published. Polar lists running cadence among the sensor outputs, outdoors and indoors ([Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm)).
- Defaults: None.
- Inputs: The motion sensor.
- Units: Not published.
- Variants: The raw export CSV holds cadence each second ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)). The web export variable list has no cadence entry.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm), [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm).

#### Cadence samples

This list gives the details for Cadence samples:

- Fields and export columns: the `cadence` entry in `samples.fields`.
- What it measures: Current cadence over time.
- Window or phase: Time series within one player session.
- Calculation: The API calls it current cadence, as a double ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: The motion sensor.
- Units: Not published.
- Variants: Request with `samples=cadence` or `samples=all`.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Not published.
- Sources: [API](https://www.polar.com/teampro-api/).

### Recovery

#### Recovery time

This list gives the details for Recovery time:

- Fields and export columns: `recovery_time_ms` (player session details). Export: Recovery time.
- What it measures: An estimate of the time a player needs to recover from the session.
- Window or phase: One player session (player session details).
- Calculation: Not published. Polar offers it as one way to view training load ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Defaults: The manual rates it Mild at 0 to 6 hours, Reasonable at 7 to 12, Demanding at 13 to 24, Very demanding at 25 to 48, and Extreme over 48 ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- Inputs: Not published.
- Units: Milliseconds in the API.
- Variants: A team setting picks whether the web service shows it.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Not published.
- Sources: [Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm).

#### Recovery status, Nightly Recharge, and sleep

This list gives the details for Recovery status, Nightly Recharge, and sleep:

- Fields and export columns: none in the API. Web view: player roster.
- What it measures: Recovery and sleep for players who link a personal Polar Flow account.
- Window or phase: Player roster view. The sleep value is the last one in the past 7 days. The roster updates in 10-minute intervals.
- Calculation: The roster shows recovery status, Nightly Recharge, Cardio load status, and sleep. The sleep value is the last one in the past 7 days. The roster updates in 10-minute intervals ([Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm)). Recovery Pro compares a resting RMSSD test with the player's normal range from the past four weeks and needs three tests in 28 days ([Recovery Pro white paper](https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf)).
- Defaults: Not applicable.
- Inputs: Data from the player's own Polar device and Flow account ([Manual: Individual training](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/individual_training.htm)).
- Units: Not applicable.
- Variants: The API can return a player's personal sessions with `type=INDIVIDUAL`. Recovery and sleep have no API field. Whether any export holds them is Not published.
- Comparison with standard methods or other vendors: None supported by a source.
- What changes the number: Whether the player links Flow and syncs a device. Unlinking deletes the player's personal data from the team account ([Manual: Individual training](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/individual_training.htm)).
- Sources: [Manual: Team settings](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm), [Recovery Pro white paper](https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf), [Manual: Individual training](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/individual_training.htm).

### Session and context

#### Duration

This list gives the details for Duration:

- Fields and export columns: `duration_ms`. Export: Duration.
- What it measures: The length of the session, trimmed session, or phase.
- Window or phase: Session, trimmed session, or phase.
- Calculation: Not published beyond the field description ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Session start and end.
- Units: Milliseconds.
- Variants: Player session details, summaries, and phase summaries.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Trimming and phase choice.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Session and phase times

This list gives the details for Session and phase times:

- Fields and export columns: `start_time`, `stop_time` (player); `start_time`, `end_time`, `record_start_time`, `record_end_time` (team); `trimmed_start_time`; `timezone_offset`; `created`, `modified`. Export: Start time, End time.
- What it measures: When a session or phase started and ended.
- Window or phase: Session or phase.
- Calculation: `trimmed_start_time` is local time ([API](https://www.polar.com/teampro-api/)). The `created` examples end in `Z`, and the `start_time` examples have no offset. Which time zone each field uses is Not published. `timezone_offset` is an integer with no stated unit.
- Defaults: None.
- Inputs: Sensor and iPad clocks.
- Units: ISO 8601 date-times.
- Variants: `since` and `until` filter team sessions by `record_start_time` and player sessions by `start_time` ([API](https://www.polar.com/teampro-api/)). The iPad merges session files less than one minute apart when it syncs ([Manual: End session](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/end_training_session.htm)).
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Trimming, merging, and the clock settings.
- Sources: [API](https://www.polar.com/teampro-api/), [Manual: End session](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/end_training_session.htm).

#### Phases and markers

This list gives the details for Phases and markers:

- Fields and export columns: `markers[]` with `start_time`, `end_time`, `marker_type`, `name`, `note`; `GET /v1/training_sessions/{player_session_id}/phase_summaries`. Export: Phase name.
- What it measures: Labeled parts of a session, such as drills.
- Window or phase: A labeled part of a session. Several phases can run at once.
- Calculation: A coach adds a phase in the web service after the session or live in the app. Several phases can run at once ([Manual: Analyze in web](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm), [Manual: Live phases](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/live-phases.htm)). Marker types are `PHASE`, `NOTE`, and `RECOVERY` ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Coach input.
- Units: Times and text.
- Variants: A phase summary has the same fields as a session summary. It has no phase name or phase ID, so you cannot match a row to a marker by key ([API](https://www.polar.com/teampro-api/)). The matching rule is Not published. Match on `trimmed_start_time` and `duration_ms`, and check the result.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Overlapping phases double count if you add them up.
- Sources: [Manual: Analyze in web](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm), [Manual: Live phases](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/live-phases.htm), [API](https://www.polar.com/teampro-api/).

#### Session labels

This list gives the details for Session labels:

- Fields and export columns: `id`, `team_id`, `name`, `type`, `sport`, `note`, `arena`. Export: Session name, Type.
- What it measures: What the session was.
- Window or phase: One session.
- Calculation: Team session `type` is one of `TRAINING`, `DRILL`, `TEST`, `GAME`, `MATCH`, `STRENGTH AND CONDITION`, and `OTHER` ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Coach input.
- Units: Text.
- Variants: A player session also has a `type` field with the values `TEAM` and `INDIVIDUAL`. It is a different field with the same name.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: A coach can edit session labels after the session.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Player and participant identity

This list gives the details for Player and participant identity:

- Fields and export columns: `player_id`, `player_number`, `role`, `first_name`, `last_name`, `player_session_id`. Export: Player number, Player name.
- What it measures: Who a row belongs to.
- Window or phase: Per player and per player session.
- Calculation: `player_id` identifies the person. `player_session_id` identifies that person's recording in one session ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Roster entries.
- Units: Text and integers.
- Variants: A team holds up to 99 players, and up to 60 can be monitored live ([Polar support: team size](https://support.polar.com/en/support/how_many_players_can_there_be_on_a_team)). The API returns no height, weight, birth date, sex, HRmax, resting heart rate, or MAP. Ask the coach for them.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Roster edits.
- Sources: [API](https://www.polar.com/teampro-api/), [Polar support: team size](https://support.polar.com/en/support/how_many_players_can_there_be_on_a_team).

#### Feeling

This list gives the details for Feeling:

- Fields and export columns: `feeling` (player session): `BAD`, `NOT_GOOD`, `OKAY`, `GREAT`, `AWESOME`.
- What it measures: A five-level feeling rating on a player session.
- Window or phase: One player session.
- Calculation: Polar does not say who enters it or where ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Player or coach entry.
- Units: A category.
- Variants: Player session objects only.
- Comparison with standard methods or other vendors: This is not session RPE.
- What changes the number: Not applicable.
- Sources: [API](https://www.polar.com/teampro-api/).

#### Raw data export files

This list gives the details for Raw data export files:

- Source in the web service: **EXPORT RAW DATA** in the web service.
- What it measures: Second-by-second data for each chosen player.
- Window or phase: Second by second, for the players you choose.
- Calculation: A zip file holds one folder per player. Each folder has a CSV file, a text file, and a GPX file. The CSV holds heart rate, speed, distance, acceleration and deceleration, and running cadence for each second. The text file holds unfiltered RR data. The GPX file holds location ([Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm)).
- Defaults: None.
- Inputs: Sensor data after sync.
- Units: The CSV header row and units are Not published.
- Variants: The standard export gives XLS or CSV with the variables you choose.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: The players you choose. The raw export has no phase option in the manual.
- Sources: [Manual: Export Data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm).

#### Product

This list gives the details for Product:

- Fields and export columns: `product` (player session details).
- What it measures: The product that saved the session.
- Window or phase: One player session.
- Calculation: The API says the product used to save the training session. The sample reads `Polar Pro` ([API](https://www.polar.com/teampro-api/)).
- Defaults: None.
- Inputs: Device.
- Units: Text.
- Variants: Other values are Not published.
- Comparison with standard methods or other vendors: Not applicable.
- What changes the number: Not applicable.
- Sources: [API](https://www.polar.com/teampro-api/).

## Device facts that affect the numbers

Use these facts when you judge data quality:

- The Polar Pro sensor holds up to 72 hours of data, per the manual, and 65 hours, per the white paper. The two sources disagree ([Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Polar recommends moistening the strap electrodes. A dry strap loses heart rate contact ([Manual: Wear sensor](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/wear_polar_pro_sensor.htm)).
- A session can run without an iPad. The sensors record it and you view it after sync ([Manual: Start session](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/start_training_session.htm)). Live data does not include cardio load ([Manual: Training Load](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm)).
- A sync handles at most 20 sensors at a time. Unsynced sessions stay on the iPad until they reach the web service ([Manual: Sync data](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sync_data_from_sensors.htm)).
- Signing in needs internet. A signed-in session can start and finish offline ([Polar support: offline use](https://support.polar.com/en/support/can_the_polar_team_pro_app_be_used_offline)).
- Polar's support site says Team Pro works with Polar Pro sensors ([Polar support: sensors](https://support.polar.com/en/support/which_sensors_are_compatible_with_polar_team_pro)).

## Conflicts in the vendor's own sources

The Polar sources disagree, or contain sample values that contradict each other, in these places:

- Device storage: the manual says the Polar Pro sensor holds up to 72 hours of data. The Team Pro white paper says 65 hours ([Manual: Facts and Features](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Heart rate zone 1 for HRmax 190: the manual's example table lists 104 to 114 bpm, but 50 percent of 190 is 95. The other four rows match the percentages. Treat the 104 as a likely misprint and ask before you rely on it ([Manual: Heart rate zones](https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm)).
- Heart rate percent of HRmax: the API sample shows 120 bpm as 79 percent and 160 bpm as 96 percent. Those two pairs imply different HRmax values ([API](https://www.polar.com/teampro-api/)).
- Field types: the API types `speed_avg_kmh` and `speed_max_kmh` as integers, but the samples show decimals, such as 7.9 for `speed_avg_kmh` ([API](https://www.polar.com/teampro-api/)).
- Cardio load samples: the API sample shows 27.2, 27.3, and 27.5 for the same session across endpoints. These are placeholder data ([API](https://www.polar.com/teampro-api/)).
- Sample rows: the documentation sample rows in `samples` are shorter than the `fields` list, so read the width of a real row before you parse it ([API](https://www.polar.com/teampro-api/)).
- Time zones: the `created` examples end in `Z`, the `start_time` examples have no offset, and `trimmed_start_time` is local time. Which time zone each field uses is Not published ([API](https://www.polar.com/teampro-api/)).
- Power zone limits: the API says limits are in watts, but its sample for a `DEFAULT` profile shows 70, 85, 100, 130, 180, and 400, which match the percent-of-MAP defaults. The unit is Not confirmed ([API](https://www.polar.com/teampro-api/), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Muscle load unit: the white paper uses kilojoules. The API does not state a unit, and its sample shows 34 ([API](https://www.polar.com/teampro-api/), [Team Pro white paper](https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf)).
- Samples query list: the query list does not name `power` as a `samples` option, but a power sample appears in the sample table. Whether `samples=all` returns it is Not published. The query list names `rr`, and the sample response includes `rr_intervals`. Whether the list returns only when you request `rr` is Not published ([API](https://www.polar.com/teampro-api/)).

## Not published

The sources do not publish or confirm these details. Confirm them on a real export or with the coach:

- The header row, units, and number formatting of the web export and the raw CSV.
- Default speed zones and default acceleration and deceleration zones.
- What `THRESHOLD` means for heart rate zones, and the meaning of each `gps_state` value.
- How team-level fields (`cardio_load`, `heart_rate_average`, `distance`, zone values) combine players.
- Whether session summary values and session details values differ when a coach trims a session.
- The unit and scale of `muscle_load`, and the unit of the power zone limits.
- The unit of RR intervals, `rmssd`, `speed` samples, `altitude` samples, `forward_acceleration`, and `cadence`.
- How Team Pro handles heart rate above HRmax, missing samples, and RR artifacts.
- The rounding rules for zone limits and integer fields.
- The calculation for calories, recovery time, training load score, training benefit, walking, ascent and descent, and running index in Team Pro.
- Whether HRmax changes recalculate old sessions.
- How a phase summary row matches its marker.

## Worked example in Python

This example uses a synthetic series of 600 samples at 1 Hz. It does four things:

1. It builds the heart rate series from seven linear segments.
2. It counts seconds in the five default zones for three HRmax settings: 190, 200, and 180 bpm.
3. It computes an Edwards TRIMP from those seconds, with weights 1 to 5 and time in minutes.
4. It computes a Banister TRIMP with male weights and a resting heart rate of 60 bpm, to compare with Polar's cardio load.

The code makes these assumptions, which Polar does not publish:

- A sample at or above 100 percent of HRmax counts as out of zones. How Team Pro treats samples above HRmax is Not published.
- Each one-second Banister term is divided by 60. The scale check in the output supports this choice for typical session ranges.
- Zone limits are exact fractions of HRmax. Polar's rounding rule is Not published.

Read the output as follows:

- A higher HRmax moves every zone limit up. The same heart rate then falls in a lower zone, so Edwards TRIMP drops. At HRmax 200, Edwards TRIMP is 23.12 against 28.00 at 190, a drop of 17.4 percent.
- A lower HRmax moves limits down. At HRmax 180, 61 seconds are above 100 percent and fall out of the zones in this code. Edwards TRIMP still drops to 23.65, because those seconds lose their weight of 5. Banister TRIMP rises to 18.85 from 15.37, because its curve keeps rising above 100 percent of reserve.
- The two methods move in opposite directions when HRmax is set below the heart rate the player reaches. Check for samples above HRmax before you trust either number.

### Code

```python
"""Time in heart rate zones and Edwards TRIMP from a synthetic 1 Hz series.

Zone limits are percentages of HRmax: 50-60, 60-70, 70-80, 80-90, 90-100.
Each zone includes its lower limit and excludes its upper limit, as the
Team Pro API states for sport profile zones. Edwards weights are 1 to 5.
Banister TRIMP is added only to compare with Polar's Cardio load formula.
"""
import math

# 1. Build a 600 s synthetic series: (seconds, start bpm, end bpm) segments.
SEGMENTS = [
    (180, 85, 125),   # warm-up ramp
    (120, 135, 135),  # steady block
    (60, 170, 182),   # interval 1
    (60, 182, 140),   # recovery 1
    (60, 178, 188),   # interval 2
    (60, 188, 120),   # recovery 2
    (60, 120, 95),    # cool-down
]


def build_series(segments):
    hr = []
    for secs, start, end in segments:
        for i in range(secs):
            hr.append(round(start + (end - start) * i / secs))
    return hr


hr = build_series(SEGMENTS)

ZONE_PCT = [(50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
EDWARDS_WEIGHT = [1, 2, 3, 4, 5]


def zone_limits_bpm(hrmax):
    return [(lo * hrmax / 100, hi * hrmax / 100) for lo, hi in ZONE_PCT]


def seconds_in_zones(series, hrmax):
    limits = zone_limits_bpm(hrmax)
    secs = [0] * 5
    out = 0
    for v in series:
        for z, (lo, hi) in enumerate(limits):
            if lo <= v < hi:
                secs[z] += 1
                break
        else:
            out += 1
    return secs, out


def edwards_trimp(secs):
    return sum(w * s / 60 for w, s in zip(EDWARDS_WEIGHT, secs))


def banister_trimp(series, hrmax, hrrest, male=True):
    # Polar white paper: sum of per-second terms. Polar does not publish the
    # time scaling. This restatement divides each 1 s term by 60 so the unit
    # matches classic per-minute Banister TRIMP.
    a, b = (0.64, 1.92) if male else (0.86, 1.67)
    total = 0.0
    for v in series:
        r = (v - hrrest) / (hrmax - hrrest)
        total += (r * a * math.exp(b * r)) / 60
    return total


print(f"Samples: {len(hr)} s, min {min(hr)} bpm, max {max(hr)} bpm, "
      f"mean {sum(hr) / len(hr):.1f} bpm")

HRREST = 60
for hrmax in (190, 200, 180):
    print()
    print(f"=== HRmax {hrmax} bpm (HRrest {HRREST} bpm) ===")
    limits = zone_limits_bpm(hrmax)
    secs, out = seconds_in_zones(hr, hrmax)
    print("Zone  Limits bpm (lower incl, upper excl)  Seconds  Minutes  Weight  Weighted")
    for z, ((lo, hi), s, w) in enumerate(zip(limits, secs, EDWARDS_WEIGHT), 1):
        print(f"Z{z}    {lo:6.1f} to {hi:6.1f}                       "
              f"{s:5d}    {s / 60:6.2f}  {w:5d}   {w * s / 60:7.2f}")
    print(f"Out of zones (below 50% or at/above 100% HRmax): {out} s")
    print(f"Seconds above HRmax: {sum(1 for v in hr if v > hrmax)}")
    print(f"Max HR as % of HRmax: {100 * max(hr) / hrmax:.1f}")
    print(f"Edwards TRIMP: {edwards_trimp(secs):.2f}")
    print(f"Banister TRIMP (male weights): {banister_trimp(hr, hrmax, HRREST):.2f}")

print()
base_secs, _ = seconds_in_zones(hr, 190)
alt_secs, _ = seconds_in_zones(hr, 200)
low_secs, _ = seconds_in_zones(hr, 180)
e190, e200, e180 = (edwards_trimp(s) for s in (base_secs, alt_secs, low_secs))
print(f"Edwards TRIMP change, HRmax 190 -> 200: {e200 - e190:+.2f} "
      f"({100 * (e200 - e190) / e190:+.1f}%)")
print(f"Edwards TRIMP change, HRmax 190 -> 180: {e180 - e190:+.2f} "
      f"({100 * (e180 - e190) / e190:+.1f}%)")
b190, b200, b180 = (banister_trimp(hr, m, HRREST) for m in (190, 200, 180))
print(f"Banister TRIMP change, HRmax 190 -> 200: {b200 - b190:+.2f} "
      f"({100 * (b200 - b190) / b190:+.1f}%)")
print(f"Banister TRIMP change, HRmax 190 -> 180: {b180 - b190:+.2f} "
      f"({100 * (b180 - b190) / b190:+.1f}%)")

print()
print("Zone limits in bpm for the manual's example HRmax 190 (220 minus age 30):")
for z, (lo, hi) in enumerate(zone_limits_bpm(190), 1):
    print(f"  Z{z}: {lo:.1f} to {hi:.1f}")

print()
print("Scale check for the per-second restatement of Banister TRIMP.")
print("Polar's support page says 60 min sessions typically score 70 to 130.")
for pct in (50, 60, 70, 80):
    hrmax_chk, hrrest_chk = 190, 60
    steady = [round(hrrest_chk + pct / 100 * (hrmax_chk - hrrest_chk))] * 3600
    print(f"  60 min at {pct}% of heart rate reserve ({steady[0]} bpm): "
          f"{banister_trimp(steady, hrmax_chk, hrrest_chk):.1f} (divided by 60), "
          f"{banister_trimp(steady, hrmax_chk, hrrest_chk) * 60:.0f} (not divided)")
```

### Output

```text
Samples: 600 s, min 85 bpm, max 188 bpm, mean 136.7 bpm

=== HRmax 190 bpm (HRrest 60 bpm) ===
Zone  Limits bpm (lower incl, upper excl)  Seconds  Minutes  Weight  Weighted
Z1      95.0 to  114.0                         130      2.17      1      2.17
Z2     114.0 to  133.0                          78      1.30      2      2.60
Z3     133.0 to  152.0                         152      2.53      3      7.60
Z4     152.0 to  171.0                          47      0.78      4      3.13
Z5     171.0 to  190.0                         150      2.50      5     12.50
Out of zones (below 50% or at/above 100% HRmax): 43 s
Seconds above HRmax: 0
Max HR as % of HRmax: 98.9
Edwards TRIMP: 28.00
Banister TRIMP (male weights): 15.37

=== HRmax 200 bpm (HRrest 60 bpm) ===
Zone  Limits bpm (lower incl, upper excl)  Seconds  Minutes  Weight  Weighted
Z1     100.0 to  120.0                         138      2.30      1      2.30
Z2     120.0 to  140.0                         163      2.72      2      5.43
Z3     140.0 to  160.0                          44      0.73      3      2.20
Z4     160.0 to  180.0                         104      1.73      4      6.93
Z5     180.0 to  200.0                          75      1.25      5      6.25
Out of zones (below 50% or at/above 100% HRmax): 76 s
Seconds above HRmax: 0
Max HR as % of HRmax: 94.0
Edwards TRIMP: 23.12
Banister TRIMP (male weights): 12.84

=== HRmax 180 bpm (HRrest 60 bpm) ===
Zone  Limits bpm (lower incl, upper excl)  Seconds  Minutes  Weight  Weighted
Z1      90.0 to  108.0                         110      1.83      1      1.83
Z2     108.0 to  126.0                         113      1.88      2      3.77
Z3     126.0 to  144.0                         140      2.33      3      7.00
Z4     144.0 to  162.0                          42      0.70      4      2.80
Z5     162.0 to  180.0                          99      1.65      5      8.25
Out of zones (below 50% or at/above 100% HRmax): 96 s
Seconds above HRmax: 61
Max HR as % of HRmax: 104.4
Edwards TRIMP: 23.65
Banister TRIMP (male weights): 18.85

Edwards TRIMP change, HRmax 190 -> 200: -4.88 (-17.4%)
Edwards TRIMP change, HRmax 190 -> 180: -4.35 (-15.5%)
Banister TRIMP change, HRmax 190 -> 200: -2.53 (-16.5%)
Banister TRIMP change, HRmax 190 -> 180: +3.48 (+22.7%)

Zone limits in bpm for the manual's example HRmax 190 (220 minus age 30):
  Z1: 95.0 to 114.0
  Z2: 114.0 to 133.0
  Z3: 133.0 to 152.0
  Z4: 152.0 to 171.0
  Z5: 171.0 to 190.0

Scale check for the per-second restatement of Banister TRIMP.
Polar's support page says 60 min sessions typically score 70 to 130.
  60 min at 50% of heart rate reserve (125 bpm): 50.1 (divided by 60), 3009 (not divided)
  60 min at 60% of heart rate reserve (138 bpm): 72.9 (divided by 60), 4375 (not divided)
  60 min at 70% of heart rate reserve (151 bpm): 103.1 (divided by 60), 6184 (not divided)
  60 min at 80% of heart rate reserve (164 bpm): 142.7 (divided by 60), 8563 (not divided)
```

## Sources

These Polar documents and papers support the facts on this page. All were accessed on 2026-10-02:

- Polar TeamPro API reference: <https://www.polar.com/teampro-api/>, accessed 2026-10-02.
- Polar Team Pro user manual, Export Data: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/export_data.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Polar Heart Rate Zones: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_heart_rate_zones.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Polar Speed Zones: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/polar_speed_zones.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Sprints: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sprints.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Training Load: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/training_load.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, RR interval: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/rr-interval.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Reports: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/reports.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Team Settings: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/team_settings.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, First time setup: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/first_time_setup.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Facts and Features: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/facts_and_features.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Sync data from sensors: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/sync_data_from_sensors.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Analyze Data in Team Pro Web Service: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_web_service.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Analyze Data in Team Pro App: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/analyze_data_in_team_pro_app.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Individual training: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/individual_training.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, End Training Session: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/end_training_session.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Start Training Session: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/start_training_session.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Wear Polar Pro sensor: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/wear_polar_pro_sensor.htm>, accessed 2026-10-02.
- Polar Team Pro user manual, Live phases: <https://support.polar.com/e_manuals/Team_Pro/Polar_Team_Pro_user_manual_English/live-phases.htm>, accessed 2026-10-02.
- Polar, Polar Team Pro System white paper: <https://www.polar.com/img/static/whitepapers/pdf/polar-team-pro-white-paper.pdf>, accessed 2026-10-02.
- Polar, Polar Training Load Pro white paper (2019-11-12, March 2025): <https://www.polar.com/img/static/whitepapers/pdf/polar-training-load-pro-white-paper.pdf>, accessed 2026-10-02.
- Polar, Polar Running Power white paper: <https://polar.com/img/static/whitepapers/pdf/polar-running-power-white-paper.pdf>, accessed 2026-10-02.
- Polar, Polar Recovery Pro white paper: <https://polar.com/img/static/whitepapers/pdf/polar-recovery-pro-white-paper.pdf>, accessed 2026-10-02.
- Polar, Polar Running Index white paper: <https://polar.com/img/static/whitepapers/pdf/polar-running-index-white-paper.pdf>, accessed 2026-10-02.
- Polar, Polar Smart Calories white paper: <https://polar.com/img/static/whitepapers/pdf/polar-smart-calories-white-paper.pdf>, accessed 2026-10-02.
- Polar, Training Load Pro support page: <https://support.polar.com/en/training-load-pro>, accessed 2026-10-02.
- Polar support, how many players can there be on a team: <https://support.polar.com/en/support/how_many_players_can_there_be_on_a_team>, accessed 2026-10-02.
- Polar support, whether the Polar Team Pro app works offline: <https://support.polar.com/en/support/can_the_polar_team_pro_app_be_used_offline>, accessed 2026-10-02.
- Polar support, which sensors are compatible with Polar Team Pro: <https://support.polar.com/en/support/which_sensors_are_compatible_with_polar_team_pro>, accessed 2026-10-02.
- Polar, Expert Insights: How TPS Turku Use Polar Team Pro to Develop Young Players: <https://www.polar.com/blog/tps-turku-use-polar-team-pro/>, accessed 2026-10-02.
- Polar, Heart Rate Zones guide: <https://www.polar.com/en/guide/heart-rate-zones>, accessed 2026-10-02.
- Falk Neto et al., 2020, Edwards and Banister TRIMP definitions: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7435063/>, accessed 2026-10-02.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
