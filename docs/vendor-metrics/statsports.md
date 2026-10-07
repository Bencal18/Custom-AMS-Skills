# STATSports metrics

STATSports makes Apex GNSS trackers, the Sonra software for elite teams, Sonra Live apps for live data, Sonra Lite for semi-professional and amateur teams, and the Apex Athlete Series for individual players. Viper is the older STATSports system. This page explains how each metric that STATSports publicly describes is defined, so a coach or sports scientist can read STATSports exports correctly. Everything here comes from public STATSports articles and product pages, and each fact links to its source.

Checked against: public STATSports articles dated 2014-10-23 to 2024-04-30, and STATSports product pages for Sonra, Sonra Lite, Apex 2.0, and American football, on 2026-10-07. The Sonra product page names the software version as Sonra 5.0 ([Sonra](https://statsports.com/sonra)).

STATSports, Sonra, Apex, and Viper are trademarks of their owner. This repository is not affiliated with or endorsed by STATSports.

The STATSports support centers, `support.statsports.com` and `elitesupport.statsports.com`, return a browser check instead of the article. This review did not pass that check, so it read none of those articles. See [Pages not publicly readable](#pages-not-publicly-readable).

## How to read this page

Each metric has one block under a `####` heading. Each block is a short list with these fields:

- **Vendor name:** The name as STATSports writes it, in code font.
- **What it measures:** One plain sentence.
- **Window or phase:** The time window, default zone, or default threshold that a STATSports page states.
- **Calculation:** "Vendor definition (paraphrased)" restates STATSports text in other words, with a link. "Restatement, not a vendor statement" is plain math written for this page.
- **Inputs:** The raw signal the metric needs.
- **Units:** As published.
- **Variants:** Absolute, relative, per minute, event, and product variants.
- **Comparison with standard methods or other vendors:** Only where a source supports a comparison.
- **What changes the number:** Settings that a source says affect the value.
- **Source links:** The public pages cited in the block.

Not published means no public STATSports page read for this review gives that detail. It does not mean the detail does not exist.

This page reports proprietary metrics as STATSports defines them. It does not recompute them.

## Background

### Facts that matter most

These points affect how you read every STATSports export:

- Sonra calculates many metrics from six zones per metric. Zones exist for speed, heart rate, accelerations, decelerations, metabolic power, and impacts ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- Each zoned metric can be absolute, from squad or group zones, or relative, from each player's own zones. Sonra reports both, for example `Accelerations (Absolute)` and `Accelerations (Relative)` ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- Sonra Exchange sends raw sessions to another Sonra user, and the receiver's own zones then apply. The same session can show different numbers in two accounts ([Sonra Exchange](https://statsports.com/article/sonra-exchange-share-data-seamlessly-with-other-users)).
- Sampling rates differ by device and by route. See [Sensors and sampling](#sensors-and-sampling).
- STATSports does not publish the formulas for metabolic power, Dynamic Stress Load, Step Balance, or Heart Rate Exertion weights on any page this review could read.

### Product names used on this page

These product names appear on this page:

- **Apex:** The STATSports GNSS tracker. Apex 2.0 is the newer model ([Apex 2.0](https://go.statsports.com/apex-2-0)).
- **Sonra:** The desktop and cloud software for elite teams. ([Sonra](https://statsports.com/sonra)).
- **Sonra Live:** The iPad and watch apps for live data ([Sonra](https://statsports.com/sonra)).
- **Sonra Lite:** Web software for semi-professional and amateur teams, in coach-led and player-led setups ([Sonra Lite](https://statsports.com/sonra-lite)).
- **Apex Athlete Series:** The tracker and app for individual players ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
- **Viper:** The older STATSports system and software ([Speed Zones, Part 1](https://statsports.com/article/individualisation-of-player-monitoring-speed-zones-part-1)).

### Sensors and sampling

STATSports publishes these facts about its sensors and sampling:

- At launch in 2017, Apex had 18 Hz GPS and a 600 Hz accelerometer ([Apex launch](https://statsports.com/article/statsports-launch-the-most-powerful-wearable-in-sport)).
- A 2019 article describes Apex as a 10 Hz augmented multi-GNSS chip with a 952 Hz accelerometer, a 952 Hz gyroscope, and a 10 Hz magnetometer ([Macrocycle overview](https://statsports.com/article/macrocycle-overview-does-player-tracking-aid-periodized-peak-performance)). A 2021 article gives 10 Hz GNSS ([Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer)).
- Apex 2.0 uses dual-band RTK GNSS at 25 Hz ([American football](https://statsports.com/sonra/american-football)). STATSports also describes an ultra-wideband and RTK GNSS smart beacon ([Apex 2.0](https://go.statsports.com/apex-2-0)).
- The API sends raw data with 10 Hz GNSS and 100 Hz accelerometer and gyroscope data ([Sonra Desktop Updates](https://statsports.com/article/sonra-desktop-updates)).
- Apex uses GPS, GLONASS, Galileo, and BeiDou together, with satellite-based augmentation ([Stadium Data: Premier League](https://statsports.com/article/stadium-data-a-premier-league-report)).

## Coverage

STATSports publishes no full public metric list on a page this review could read. This page covers 26 metric blocks:

| Area | Blocks |
|---|---|
| Distance and speed | 4 |
| Speed zones, high-speed running, and sprints | 3 |
| Accelerations and decelerations | 3 |
| Metabolic power and high metabolic load | 5 |
| Bursts and peak periods | 3 |
| Accelerometer and impact metrics | 4 |
| Heart rate | 4 |
| **Total** | **26** |

## Summary tables

Each table lists the metrics in one area. "Calculation published" is Yes when STATSports publishes the full rule, Partly when some part is Not published, and No when STATSports gives no calculation.

### Summary: distance, speed, and zones

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Total Distance` | Distance covered | m, km, miles, or yards | No |
| `Distance Per Minute` | Work rate | m/min | Yes |
| `Max Speed` | Highest speed | m/s, km/h, or mph | Partly |
| Speed zone distance | Distance in each of six speed zones | m | Partly |
| `High Speed Running` (HSR) | Distance in speed zones 5 and 6 | m or yards | Partly |
| `Sprints` | Count of sprint efforts | count | Partly |
| Sprint distance | Distance during sprints | m | Partly |

### Summary: accelerations and decelerations

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Accelerations` and `Decelerations` | Counts of efforts in each zone | count | Partly |
| `Maximum Acceleration` and `Maximum Deceleration` | Largest speed change in the session | m/s² | Partly |
| Acceleration and deceleration magnitude | Size of each event in the event export | m/s/s | No |

### Summary: metabolic power and high metabolic load

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Metabolic power | Estimated energy use per kilogram | W/kg | No |
| `HML Distance` (HMLD) | Distance at high metabolic power | m | Partly |
| `HML Efforts` | Count of high metabolic load efforts | count | Partly |
| `Explosive Distance` | High metabolic power distance below HSR speed | m | Partly |
| `High Intensity Distance` | HSR plus acceleration and deceleration distance | m or yards | Partly |

### Summary: bursts and peak periods

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| High Intensity Bursts (HIB) | Clusters of hard actions | count, m, s | Yes |
| Max Intensity Period (MIP) | Peak moving average of a metric | Metric unit | Partly |
| Drill Intensity | Live drill rate against a set scale | m/min | Partly |

### Summary: accelerometer and impact metrics

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Dynamic Stress Load` (DSL) | Weighted impact load | Not published | Partly |
| `Total Loading` and axis loading | Summed acceleration forces | Not published | Partly |
| Impacts | Impact counts in zones | count | Partly |
| `Step Balance` | Left and right step impact split | % | Partly |

### Summary: heart rate

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Average and max heart rate | Heart rate over the session | bpm | Partly |
| Time in heart rate zones | Time in each of six zones | Time | Partly |
| `Time in Red Zone` | Time above the zone 5 threshold | Time | Yes |
| `Heart Rate Exertion` (HRE) | Weighted heart rate volume | Not published | Partly |

## Metric reference

Each area below holds one block per metric.

### Distance and speed

#### `Total Distance`

The fields for this metric are:

- **Vendor name:** `Total Distance`. Leaderboards also use Total Match Distance ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
- **What it measures:** The volume of the session as distance covered.
- **Window or phase:** The session or drill.
- **Calculation:**
  - Vendor definition (paraphrased): How much work the session held, given as distance ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
  - Restatement, not a vendor statement: `Total Distance = Σ dᵢ`, the sum of distance between samples. Whether STATSports sums position steps or integrates speed is Not published.
- **Inputs:** GNSS position and speed.
- **Units:** m, km, miles, or yards in the app ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
- **Variants:** `Distance Per Minute`.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Drill edges, and GNSS signal quality. STATSports reports HACC, HDOP, and satellite count in the extended raw data export ([Stadium Data: Premier League](https://statsports.com/article/stadium-data-a-premier-league-report)). The filter is Not published.
- **Source links:** [USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [Stadium Data: Premier League](https://statsports.com/article/stadium-data-a-premier-league-report).

#### `Distance Per Minute`

The fields for this metric are:

- **Vendor name:** `Distance Per Minute`.
- **What it measures:** Work rate.
- **Window or phase:** The session or drill.
- **Calculation:**
  - Vendor definition (paraphrased): Metres covered per minute, on average ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster)).
  - Restatement, not a vendor statement: `Distance Per Minute = Total Distance (m) ÷ duration (min)`.
- **Inputs:** Distance and duration.
- **Units:** m/min.
- **Variants:** Sonra Live Drill Intensity can use Distance Per Minute ([Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live)). MIP can use it with a moving window.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Rest time inside a drill lowers the value. Segment Drills split a drill into fixed-length or fixed-number parts ([Segment Drills](https://statsports.com/article/temporal-pattern-analysis-of-physical-data-using-sonras-segment-drills-function)).
- **Source links:** [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live), [Segment Drills](https://statsports.com/article/temporal-pattern-analysis-of-physical-data-using-sonras-segment-drills-function).

#### `Max Speed`

The fields for this metric are:

- **Vendor name:** `Max Speed`.
- **What it measures:** The highest speed in the session or drill.
- **Window or phase:** The session or drill.
- **Calculation:**
  - Vendor definition (paraphrased): The top speed reached within the session or drill ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster)).
  - Restatement, not a vendor statement: `Max Speed = max(vᵢ)` over the selected time.
- **Inputs:** GNSS speed.
- **Units:** m/s, mph, or km/h ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
- **Variants:** Max Speed per sprint in the Sprints event export ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Smoothing, which is Not published. Relative speed zones can be a percentage of the player's maximum speed, so the stored maximum changes those zones ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Source links:** [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### Speed zone distance

The fields for this metric are:

- **Vendor name:** Zone distance, for example `Zone 4 Distance` ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **What it measures:** Distance covered while speed is in one of six zones.
- **Window or phase:** Zone 5 starts at 5.5 m/s and zone 6 starts at 7 m/s by default ([Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study)). Defaults for zones 1 to 4 are Not published on a page this review could read.
- **Calculation:**
  - Vendor definition (paraphrased): Speed is assigned to zones 1 to 6 from low to high. A 2017 article says Viper speed zones were absolute, the same for every player, by default ([Speed Zones, Part 1](https://statsports.com/article/individualisation-of-player-monitoring-speed-zones-part-1)).
  - Restatement, not a vendor statement: sum the distance of samples whose speed falls in the zone.
- **Inputs:** GNSS speed.
- **Units:** m.
- **Variants:** Absolute and relative. Relative speed zones can be fixed values or a percentage of the player's maximum speed ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Zone settings. The minimum time in a zone before distance counts is Not published. The boundary rule is Not published.
- **Source links:** [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring), [Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study), [Speed Zones, Part 1](https://statsports.com/article/individualisation-of-player-monitoring-speed-zones-part-1).

### Speed zones, high-speed running, and sprints

#### `High Speed Running` (HSR)

The fields for this metric are:

- **Vendor name:** `High Speed Running`, abbreviated HSR. Reported as `HSR (Absolute)` and `HSR (Relative)` ([Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study)).
- **What it measures:** Distance at high speed.
- **Window or phase:** By default, distance above 5.5 m/s (19.8 km/h, 12.3 mph) ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards)).
- **Calculation:**
  - Vendor definition (paraphrased): Distance in speed zones 5 and 6 ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study)).
  - Restatement, not a vendor statement: `HSR = zone 5 distance + zone 6 distance`.
- **Inputs:** GNSS speed.
- **Units:** m or yards.
- **Variants:** HSR per minute, used in Sonra Live Drill Intensity ([Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Zone 5 settings. One STATSports case study set relative zones from maximal aerobic speed and anaerobic speed reserve. Relative HSR was 15% of match distance against 5.35% for absolute HSR in that study ([Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study)). These are study settings, not defaults.
- **Source links:** [USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study), [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live).

#### `Sprints`

The fields for this metric are:

- **Vendor name:** `Sprints`. Also number of sprint efforts.
- **What it measures:** How many sprints the athlete made.
- **Window or phase:** Default sprint entry speed 19.8 km/h, held for at least 1 s ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Calculation:**
  - Vendor definition (paraphrased): A sprint counts when the player exceeds the sprint entry speed and holds it for at least the minimum duration. You can change all three sprint settings, including an exit speed, for the whole account or for one player ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Inputs:** GNSS speed.
- **Units:** count.
- **Variants:** The Sprints event export lists each sprint ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Entry speed, exit speed, and minimum duration. The exit speed default is Not published.
- **Source links:** [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### Sprint distance

The fields for this metric are:

- **Vendor name:** Distance in the Sprints event export. A session sprint distance metric is Not published on a page this review could read.
- **What it measures:** Distance covered during each sprint.
- **Window or phase:** The sprint, from start to end time.
- **Calculation:**
  - Vendor definition (paraphrased): The Sprints export lists start and end time, time since the last sprint, duration, distance, max speed, and average metabolic power for each sprint ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Inputs:** GNSS speed.
- **Units:** Not published.
- **Variants:** Some STATSports articles call distance above 25.2 km/h (7 m/s) sprint distance, and one case study tracked sprinting above 7 m/s ([Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer), [MIP field hockey case study](https://statsports.com/article/maximum-intensity-periods-aiding-return-to-performance-a-field-hockey-case-study)). These are article or study settings, not a stated Sonra rule.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The sprint settings in the `Sprints` block.
- **Source links:** [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations), [Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer), [MIP field hockey case study](https://statsports.com/article/maximum-intensity-periods-aiding-return-to-performance-a-field-hockey-case-study).

### Accelerations and decelerations

#### `Accelerations` and `Decelerations`

The fields for this metric are:

- **Vendor name:** `Accelerations` and `Decelerations`, by zone, for example `Zone 5 Accelerations`, with absolute and relative versions ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **What it measures:** Counts of speed-ups and slow-downs in each zone.
- **Window or phase:** Six zones. Zone 5 starts at 4 m/s² by default ([High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design)). A 2020 article counts zones 3 to 6 as efforts of at least 2.0 m/s² that last at least 0.5 s ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster)).
- **Calculation:**
  - Vendor definition (paraphrased): An acceleration or deceleration counts in a zone when it reaches the zone's threshold for the minimum time. Absolute zones are set for all six zones from **Player Management** and apply to every player. Relative zones can be a percentage of each player's maximum acceleration, set in the settings and the player profile ([Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra)).
- **Inputs:** Not published. The event exports give acceleration in m/s/s.
- **Units:** count.
- **Variants:** The High Intensity Activities event export lists each acceleration and deceleration with its magnitude in m/s/s ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Comparison with standard methods or other vendors:** STATSports notes that practitioners often use 3 m/s² and −3 m/s² as high-intensity thresholds ([Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra)). That is not a stated Sonra default.
- **What changes the number:** Zone settings, the minimum duration, and the stored maximum for relative zones. Bounds for zones 1, 2, 4, and 6 are Not published on a page this review could read.
- **Source links:** [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring), [High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### `Maximum Acceleration` and `Maximum Deceleration`

The fields for this metric are:

- **Vendor name:** `Maximum Acceleration` and `Maximum Deceleration` ([Maximum acceleration and deceleration](https://statsports.com/article/maximum-acceleration-and-deceleration-metric-considerations-and-uses)).
- **What it measures:** The largest acceleration and deceleration in the session.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): The athlete's highest value for a given session. Sonra can scan selected players, sessions, and drills for new all-time maximums under **Check for new max values** ([Maximum acceleration and deceleration](https://statsports.com/article/maximum-acceleration-and-deceleration-metric-considerations-and-uses)).
  - Restatement, not a vendor statement: `Maximum Acceleration = max(aᵢ)` over the session.
- **Inputs:** Not published. The event exports give acceleration in m/s/s.
- **Units:** m/s².
- **Variants:** All-time maximum, stored on the player profile and used by relative zones ([Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Smoothing, which is Not published.
- **Source links:** [Maximum acceleration and deceleration](https://statsports.com/article/maximum-acceleration-and-deceleration-metric-considerations-and-uses), [Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra).

#### Acceleration and deceleration magnitude

The fields for this metric are:

- **Vendor name:** Magnitude, in the High Intensity Activities event export.
- **What it measures:** The size of each acceleration or deceleration event.
- **Window or phase:** One event.
- **Calculation:** Not published. Whether magnitude is the peak or the mean of the event is Not published.
- **Inputs:** Not published. The event exports give acceleration in m/s/s.
- **Units:** m/s/s ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The Metric Event Zone setting, absolute or relative ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Source links:** [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations), [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring).

### Metabolic power and high metabolic load

#### Metabolic power

The fields for this metric are:

- **Vendor name:** Metabolic power. Average Metabolic Power appears in event exports ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **What it measures:** Estimated energy use per kilogram of body mass per second.
- **Window or phase:** Each sample, or each event for the average.
- **Calculation:**
  - Vendor definition (paraphrased): Sonra calculates the metabolic power of each running action from speed and acceleration ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)). The formula is Not published.
- **Inputs:** Speed and acceleration from GNSS.
- **Units:** W/kg.
- **Variants:** Metabolic power zones, absolute and relative ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations), [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring).

#### `HML Distance` (HMLD)

The fields for this metric are:

- **Vendor name:** `HML Distance`, High Metabolic Load Distance, abbreviated HMLD.
- **What it measures:** Distance covered at high estimated energy cost.
- **Window or phase:** Metabolic power above 25.5 W/kg ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster)).
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered while metabolic power is above 25.5 W/kg ([U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster)). Another article describes it as HSR combined with acceleration and deceleration activity above 25.5 W/kg ([Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer)). A 2019 article for individual players describes it as HSR plus acceleration and deceleration distance, with no threshold ([What is HMLD](https://statsports.com/article/what-is-hmld-and-why-is-it-important)).
- **Inputs:** Metabolic power.
- **Units:** m.
- **Variants:** HMLD per minute in Sonra Live Drill Intensity ([Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live)).
- **Comparison with standard methods or other vendors:** The [Catapult](catapult.md) page in this folder lists a Catapult HMLD at the same 25.5 W/kg threshold. Neither vendor publishes its full metabolic power processing, so do not treat the two numbers as interchangeable.
- **What changes the number:** The metabolic power formula, which is Not published.
- **Source links:** [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), [Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer), [What is HMLD](https://statsports.com/article/what-is-hmld-and-why-is-it-important), [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live).

#### `HML Efforts`

The fields for this metric are:

- **Vendor name:** `HML Efforts`, High Metabolic Load Efforts.
- **What it measures:** The number of efforts at high metabolic power.
- **Window or phase:** Above 25.5 W/kg.
- **Calculation:**
  - Vendor definition (paraphrased): Any effort above 25.5 W/kg, with metabolic power from speed and acceleration ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)). The minimum effort duration is Not published.
- **Inputs:** Metabolic power.
- **Units:** count.
- **Variants:** The HML Efforts event export lists each effort ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### `Explosive Distance`

The fields for this metric are:

- **Vendor name:** `Explosive Distance`.
- **What it measures:** High-cost distance that is not high-speed running.
- **Window or phase:** Metabolic power above 25.5 W/kg and speed below the HSR threshold.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered with metabolic power above 25.5 W/kg and speed below the HSR threshold ([Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer)).
- **Inputs:** Metabolic power and speed.
- **Units:** m.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The HSR threshold.
- **Source links:** [Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer).

#### `High Intensity Distance`

The fields for this metric are:

- **Vendor name:** `High Intensity Distance`, in the app for individual players.
- **What it measures:** High-speed running plus distance while speeding up and slowing down.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): HSR distance combined with distance covered while accelerating and decelerating ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [High Intensity Distance](https://statsports.com/the-locker/high-intensity-distance-what-is-it-and-why-is-it-important-to-track)). The acceleration cut-off is Not published.
- **Inputs:** Speed and acceleration.
- **Units:** m or yards.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [High Intensity Distance](https://statsports.com/the-locker/high-intensity-distance-what-is-it-and-why-is-it-important-to-track).

### Bursts and peak periods

#### High Intensity Bursts (HIB)

The fields for this metric are:

- **Vendor name:** High Intensity Bursts, abbreviated HIB. Outputs include HIB distance, number of HIB efforts, and time between HIB ([High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design)).
- **What it measures:** Clusters of hard actions with little rest between them.
- **Window or phase:** At least 3 high-intensity activities, each no more than 20 s apart, by default.
- **Calculation:**
  - Vendor definition (paraphrased): A burst counts when the athlete makes at least the minimum number of high-intensity activities within the set time of each other. The activities are accelerations, decelerations, and impacts at or above the chosen zone. The 2022 article also lists sprints, and the 2023 article does not. The defaults are zone 5, which is at least 4 m/s² for accelerations and decelerations, and at least 11 g for impacts. Users change these under **Settings**, then **Drills & HIBs** ([High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Inputs:** Acceleration, deceleration, and impact events.
- **Units:** count, m, and time.
- **Variants:** The High Intensity Bursts event export lists each burst.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The minimum count, the time between activities, and the zone for each activity type.
- **Source links:** [High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### Max Intensity Period (MIP)

The fields for this metric are:

- **Vendor name:** Max Intensity Period, abbreviated MIP. Sub-MIP is a related tool ([American football](https://statsports.com/sonra/american-football)).
- **What it measures:** The most demanding period for a chosen metric.
- **Window or phase:** Default window 3 minutes. Users can set their own window ([Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer), [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live)).
- **Calculation:**
  - Vendor definition (paraphrased): The highest output of a selected metric over a set window, found with moving averages ([Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer)). The step between windows is Not published.
- **Inputs:** Any selected metric.
- **Units:** The selected metric's unit.
- **Variants:** Absolute or relative zone metrics, chosen in settings ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The window length, the metric, and drill edges.
- **Source links:** [Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer), [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live), [American football](https://statsports.com/sonra/american-football), [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring).

#### Drill Intensity

The fields for this metric are:

- **Vendor name:** Drill Intensity, in Sonra Live.
- **What it measures:** How a live drill compares with a target rate.
- **Window or phase:** The live drill.
- **Calculation:**
  - Vendor definition (paraphrased): Choose Distance Per Minute, HSR per minute, or HMLD per minute. Sonra Live shows five intensity indicators against a scale the user sets ([Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live)).
- **Inputs:** The chosen per-minute metric.
- **Units:** m/min.
- **Variants:** Set it in Sonra Live under **Settings**, then **Graphs and Drills**, or in Sonra desktop under **Settings**, then **Live**.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The scale values the user enters.
- **Source links:** [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live).

### Accelerometer and impact metrics

#### `Dynamic Stress Load` (DSL)

The fields for this metric are:

- **Vendor name:** `Dynamic Stress Load`, abbreviated DSL.
- **What it measures:** Weighted load from foot impacts and collisions.
- **Window or phase:** Impacts above 2 g.
- **Calculation:**
  - Vendor definition (paraphrased): Impacts larger than 2 g are weighted and added up. Both running steps and collisions count ([Viper article](https://statsports.com/article/injury-prevention-using-statsports-viper)). The weighting function is Not published.
- **Inputs:** Accelerometer.
- **Units:** Not published.
- **Variants:** DSL per event in the High Intensity Activities and Dives exports ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Comparison with standard methods or other vendors:** STATSports says DSL cannot be compared between athletes ([What is DSL](https://statsports.com/article/what-is-dsl-and-why-is-it-an-important-metric-to-track)). Compare each athlete only with their own history.
- **What changes the number:** Running style, according to STATSports ([Viper article](https://statsports.com/article/injury-prevention-using-statsports-viper)).
- **Source links:** [Viper article](https://statsports.com/article/injury-prevention-using-statsports-viper), [What is DSL](https://statsports.com/article/what-is-dsl-and-why-is-it-an-important-metric-to-track), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations).

#### `Total Loading` and axis loading

The fields for this metric are:

- **Vendor name:** `Total Loading`, and `Lateral`, `Vertical`, and `Anterior-Posterior` impact or loading. Dynamic Loading metrics exist on the same three axes ([Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring)).
- **What it measures:** Accumulated acceleration forces, in total or on one axis.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): The sum of acceleration forces, in total or in one plane. Dynamic Loading sums instantaneous forces on each axis ([Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring)). Filtering and scaling are Not published.
- **Inputs:** Tri-axial accelerometer. STATSports names lateral as x, vertical as y, and anterior-posterior as z.
- **Units:** Not published. STATSports says accelerometer data is measured in g.
- **Variants:** Three axes.
- **Comparison with standard methods or other vendors:** Not published. Do not compare with Catapult PlayerLoad or Kinexon Accumulated Acceleration Load.
- **What changes the number:** Not published.
- **Source links:** [Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring).

#### Impacts

The fields for this metric are:

- **Vendor name:** Impacts, by zone.
- **What it measures:** Counts of accelerometer impacts in six zones.
- **Window or phase:** Zone 5 starts at 11 g by default ([High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design)).
- **Calculation:**
  - Vendor definition (paraphrased): Impact metrics use the magnitude of the tri-axial accelerometer ([Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring)). The detection rule is Not published.
- **Inputs:** Tri-axial accelerometer.
- **Units:** count, with zones in g.
- **Variants:** Absolute and relative impact zones ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Impact zone settings.
- **Source links:** [High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), [Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring), [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring).

#### `Step Balance`

The fields for this metric are:

- **Vendor name:** `Step Balance`.
- **What it measures:** How step impact splits between the left and right foot.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): The average peak impact of each step on the left foot and on the right foot, shown as a percentage for each foot, such as 48:52 ([Viper article](https://statsports.com/article/injury-prevention-using-statsports-viper), [Apex Athlete Series article](https://statsports.com/article/5-ways-your-apex-athlete-series-can-help-you-avoid-injuries)). A 2024 article says it uses average vertical force on each foot ([Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring)). Step detection and foot assignment are Not published.
- **Inputs:** Accelerometer.
- **Units:** %.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published. Report the value as given.
- **What changes the number:** Not published.
- **Source links:** [Viper article](https://statsports.com/article/injury-prevention-using-statsports-viper), [Apex Athlete Series article](https://statsports.com/article/5-ways-your-apex-athlete-series-can-help-you-avoid-injuries), [Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring).

### Heart rate

#### Average and max heart rate

The fields for this metric are:

- **Vendor name:** Average Heart Rate and Max Heart Rate ([Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex)).
- **What it measures:** The mean and highest heart rate in the session.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): In STATSports Academy, max heart rate is the session peak in beats per minute, and average heart rate is the session mean ([Heart rate monitoring](https://statsports.com/the-locker/unlock-the-power-of-heart-rate-monitoring-with-statsports)).
- **Inputs:** Heart rate data.
- **Units:** bpm.
- **Variants:** Heart Rate Variability, the variation in intervals between beats averaged over 2 minutes ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra)). Heart Rate Load is also listed, with no published definition ([Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex), [Heart rate monitoring](https://statsports.com/the-locker/unlock-the-power-of-heart-rate-monitoring-with-statsports).

#### Time in heart rate zones

The fields for this metric are:

- **Vendor name:** Time in heart rate zone, for example `Time in Heart Rate Zone 6` ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **What it measures:** Time in each of six heart rate zones.
- **Window or phase:** Six zones as percentages of each player's maximum heart rate. All six can be changed ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra), [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex)).
- **Calculation:**
  - Vendor definition (paraphrased): Sonra uses six zones so that a heart rate above the set maximum still has a zone. **Check for new Max values** scans sessions for a new maximum heart rate ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra)). Default bounds other than zone 5 are Not published.
- **Inputs:** Heart rate data and each player's maximum heart rate.
- **Units:** Time.
- **Variants:** Absolute and relative heart rate zones ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Comparison with standard methods or other vendors:** STATSports contrasts its six zones with Polar's five ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra)).
- **What changes the number:** The maximum heart rate set for each player.
- **Source links:** [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring), [Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra), [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex).

#### `Time in Red Zone`

The fields for this metric are:

- **Vendor name:** `Time in Red Zone`.
- **What it measures:** Time at very high heart rate.
- **Window or phase:** Above the zone 5 threshold, 85% of the player's maximum heart rate.
- **Calculation:**
  - Vendor definition (paraphrased): Time counts once heart rate crosses the zone 5 threshold of 85% of the player's maximum ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra)).
  - Restatement, not a vendor statement: time with heart rate above 85% of HRmax. The boundary rule is Not published.
- **Inputs:** Heart rate data.
- **Units:** Time.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The player's maximum heart rate, and the zone 5 setting.
- **Source links:** [Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra).

#### `Heart Rate Exertion` (HRE)

The fields for this metric are:

- **Vendor name:** `Heart Rate Exertion`, abbreviated HRE.
- **What it measures:** Weighted volume of heart rate work over the session.
- **Window or phase:** The session.
- **Calculation:**
  - Vendor definition (paraphrased): Each heart rate value gets a weight on a convex, log-scale curve of percent maximum heart rate. Higher heart rates get higher weights. Each weight is multiplied by the time in seconds, and the products are summed ([Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra), [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex)). The weights are Not published.
- **Inputs:** Heart rate and maximum heart rate.
- **Units:** Not published.
- **Variants:** None. A STATSports article shows how to add Edwards TRIMP as a separate custom metric ([Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex)).
- **Comparison with standard methods or other vendors:** It is not Edwards TRIMP. Do not mix the two.
- **What changes the number:** The player's maximum heart rate.
- **Source links:** [Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra), [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex).

## Export routes

STATSports publishes these export routes:

- **Export Data:** pick a default CSV or a saved template, select drills, and select **Generate** ([Segment Drills](https://statsports.com/article/temporal-pattern-analysis-of-physical-data-using-sonras-segment-drills-function)).
- **Metric event exports:** under **Export Data**, then **Metrics**. Sprints, HML Efforts, High Intensity Bursts, High Intensity Activities, Collisions, Scrums, and Dives ([Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations), [High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design)). These exports are CSV. A 2024 article also names an events export in CSV and XML ([Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring)).
- **Raw Data and Raw Data Extended:** a 2022 article names both exports ([Stadium Data: Austrian Bundesliga](https://statsports.com/article/stadium-data-an-austrian-bundesliga-report)). Two articles describe the extended file as CSV. It holds HACC, HDOP, and number of satellites, logged at 10 Hz ([Stadium Data: Austrian Bundesliga](https://statsports.com/article/stadium-data-an-austrian-bundesliga-report), [Stadium Data: Premier League](https://statsports.com/article/stadium-data-a-premier-league-report)). The file format of the standard Raw Data export is Not confirmed.
- **Dashboard PDF:** five dashboards export to PDF ([Sonra Desktop Updates](https://statsports.com/article/sonra-desktop-updates)).
- **Sonra Exchange:** raw sessions to another Sonra user ([Sonra Exchange](https://statsports.com/article/sonra-exchange-share-data-seamlessly-with-other-users)).
- **API:** all metrics, custom metrics, full raw data, drill labels, positions, and a date range endpoint ([Sonra Desktop Updates](https://statsports.com/article/sonra-desktop-updates)). Endpoints and authentication are Not published.

## Conflicts in the vendor's own sources

STATSports pages disagree on these points:

- **HMLD:** two articles define it by the 25.5 W/kg threshold. A 2019 article for individual players describes it as HSR plus acceleration and deceleration distance, with no threshold ([What is HMLD](https://statsports.com/article/what-is-hmld-and-why-is-it-important)). The same wording also describes High Intensity Distance ([High Intensity Distance](https://statsports.com/the-locker/high-intensity-distance-what-is-it-and-why-is-it-important-to-track)).
- **Apex sampling:** 18 Hz GPS and a 600 Hz accelerometer at launch in 2017, against 10 Hz GNSS and a 952 Hz accelerometer in 2019 and 2021, and 25 Hz for Apex 2.0. The API sends 100 Hz accelerometer data.
- **HIB activities:** the 2022 article lists sprints among burst activities. The 2023 article lists only accelerations, decelerations, and impacts ([High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations)).
- **Explosive distance:** a 2022 article says some practitioners call HSR "explosive distance". A 2021 article defines `Explosive Distance` as high metabolic power distance below HSR speed ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer)).
- **HSR boundary:** "over 5.5 m/s" in one article, and "at or above 5.5 m/s" in another ([USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), [Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study)).
- **Step Balance input:** average peak step impact in 2014 and 2019, and average vertical force in 2024.

## Not published

STATSports does not publish these details on any page this review could read:

- The session CSV and raw data CSV headers and row level.
- API base URL, authentication, endpoint names, fields, and paging.
- Speed zones 1 to 4, and acceleration zones 1, 2, 4, and 6 defaults.
- The minimum time in a speed zone, and the boundary rule.
- The sprint exit speed default, and the session sprint distance rule.
- The metabolic power formula, the DSL weighting, the Step Balance step detection, and the Heart Rate Exertion weights.
- The Heart Rate Load definition, and the Heart Rate Variability calculation.
- The file format of the standard Raw Data export.

### Pages not publicly readable

These STATSports pages returned HTTP 403 with a browser check on 2026-10-07. This review did not try to get around the check:

- Support center: <https://support.statsports.com/hc/en-us>, and every article URL tried on it.
- Elite support center: <https://elitesupport.statsports.com/hc/en-us>, and every article URL tried on it.

## Sources

This page draws on these STATSports vendor articles and vendor product pages, all accessed 2026-10-07. Each one supports a product fact linked above:

- [Metric Event Exports](https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations), vendor article, 2023-03-07.
- [Absolute and Relative Metric Options](https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring), vendor article, 2024-04-30.
- [High Intensity Bursts](https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design), vendor article, 2022-11-03.
- [Sonra Desktop Updates](https://statsports.com/article/sonra-desktop-updates), vendor article, 2022-04-14.
- [Segment Drills](https://statsports.com/article/temporal-pattern-analysis-of-physical-data-using-sonras-segment-drills-function), vendor article, 2020-03-12.
- [Stadium Data: Premier League](https://statsports.com/article/stadium-data-a-premier-league-report), vendor article, 2020-06-17.
- [Stadium Data: Austrian Bundesliga](https://statsports.com/article/stadium-data-an-austrian-bundesliga-report), vendor article, 2022-06-24.
- [Sonra Exchange](https://statsports.com/article/sonra-exchange-share-data-seamlessly-with-other-users), vendor article, 2022-08-02.
- [Youth HSR case study](https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study), vendor article, 2020-06-05.
- [U17 Gaelic football](https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster), vendor article, 2020-02-07.
- [Acceleration zones](https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra), vendor article, 2022-05-03.
- [Maximum acceleration and deceleration](https://statsports.com/article/maximum-acceleration-and-deceleration-metric-considerations-and-uses), vendor article, 2021-07-12.
- [USYS Elite 64 metric explainers](https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards), vendor article, 2022-09-23.
- [What is HMLD](https://statsports.com/article/what-is-hmld-and-why-is-it-important), vendor article, 2019-08-29.
- [High Intensity Distance](https://statsports.com/the-locker/high-intensity-distance-what-is-it-and-why-is-it-important-to-track), vendor article, undated.
- [Domestic and European demands](https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer), vendor article, 2021-02-11.
- [Peak game demands](https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer), vendor article, 2020-06-10.
- [Drill intensity in Sonra Live](https://statsports.com/article/real-time-drill-intensity-monitoring-with-sonra-live), vendor article, 2021-10-06.
- [MIP field hockey case study](https://statsports.com/article/maximum-intensity-periods-aiding-return-to-performance-a-field-hockey-case-study), vendor article, 2021-04-08.
- [What is DSL](https://statsports.com/article/what-is-dsl-and-why-is-it-an-important-metric-to-track), vendor article, 2019-09-19.
- [STATSports Viper article on DSL and Step Balance](https://statsports.com/article/injury-prevention-using-statsports-viper), vendor article, 2014-10-23, used for the DSL and Step Balance definitions only.
- [STATSports Apex Athlete Series article on Step Balance](https://statsports.com/article/5-ways-your-apex-athlete-series-can-help-you-avoid-injuries), vendor article, 2019-10-03, used for the Step Balance display only.
- [Accelerometer metrics](https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring), vendor article, 2024-03-05.
- [Heart rate zones](https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra), vendor article, 2020-03-18.
- [Heart rate monitoring](https://statsports.com/the-locker/unlock-the-power-of-heart-rate-monitoring-with-statsports), vendor article, undated.
- [Internal-external load](https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex), vendor article, 2020-07-15.
- [Macrocycle overview](https://statsports.com/article/macrocycle-overview-does-player-tracking-aid-periodized-peak-performance), vendor article, 2019-07-02.
- [Speed Zones, Part 1](https://statsports.com/article/individualisation-of-player-monitoring-speed-zones-part-1), vendor article, 2017-05-30.
- [Apex launch](https://statsports.com/article/statsports-launch-the-most-powerful-wearable-in-sport), vendor article, 2017-06-02.
- [Apex 2.0](https://go.statsports.com/apex-2-0), undated product page.
- [American football](https://statsports.com/sonra/american-football), undated product page.
- [Sonra](https://statsports.com/sonra), undated product page, for Sonra 5.0 and Sonra Live.
- [Sonra Lite](https://statsports.com/sonra-lite), undated product page.
