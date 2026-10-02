# Kinexon metrics

Kinexon makes wearable sensors, positioning systems, and cloud software for team sports. This page lists every Kinexon athlete metric that public sources name, shows how each one is calculated where a source says so, and marks every detail that Kinexon does not publish. Kinexon publishes no formula for any metric, no default thresholds, no public API reference, and no export column list beyond the position columns that the open-source `floodlight` parser reads. Nothing here comes from Kinexon software, firmware, or private documents.

Checked against: Kinexon public product pages, sport pages, blog posts, brochures, and case studies; the Kinexon Sports App versions 12.2 and 12.3 as Kinexon posts name them; the `floodlight` Kinexon parser documentation and source; published studies that used Kinexon systems; and public Catapult pages for comparison, 2026-10-02.

Kinexon and the Kinexon product and software names on this page are trademarks of their owners. This repository is not affiliated with or endorsed by Kinexon. Other vendor and product names on this page are trademarks of their owners.

## How to read this page

Each metric has one block with these fields:

- **What it measures:** The purpose of the metric in plain words.
- **Window or phase:** The period the number covers, if a source says.
- **Calculation:** The vendor's definition, paraphrased, then a formula in plain math where the vendor or a cited source gives one.
- **Thresholds:** Any cut-off the sources give. Study settings are labeled as study settings.
- **Inputs:** The sensor data the metric uses.
- **Units:** The unit a source states.
- **Variants:** Other names and closely related metrics.
- **Comparison with standard methods or other vendors:** A comparison, only where a source supports it.
- **What changes the number:** Settings and conditions that move the value.
- **Sources:** Links to every source for the block.

These terms have fixed meanings:

- **Not published:** The vendor does not publish that detail. The sources reviewed give no public source for it. This page does not fill the gap with a guess.
- **Not stated in the sources reviewed:** The sources do not say. This is not a claim about what Kinexon publishes.
- **Vendor definition (paraphrased):** This page restates what Kinexon says in other words. Open the linked source for the exact wording.
- **Restatement (not a Kinexon statement):** The plain-language wording of this page. It is not a Kinexon formula.
- **Study settings:** Settings that researchers reported. They are not Kinexon defaults. Kinexon does not publish its default thresholds, so every threshold on this page is either a study setting or "Not published".
- **Partly:** In the summary tables, Kinexon describes the metric in words but publishes no formula. **Yes** would mean Kinexon publishes a formula. No metric on this page has a published Kinexon formula. Most formulas on this page come from published studies that describe what the Kinexon software did. Kinexon calls its own formulas proprietary.

Metric names are written exactly as the source writes them, in code font. The same metric often appears under several names, and the block lists them together. A formula appears only when a source states it.

The coverage table uses these flags:

- `Y`: A source ties the metric to that product.
- `B`: Kinexon's blanket statement that all IMU metrics are also available on LPS and GPS covers the metric ([LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/)).
- `P`: A source that lists several products, or none, names the metric, so it cannot be tied to one product.
- Empty: No source.

## Kinexon products in public sources

The sources describe these products:

- **PERFORM LPS.** A permanently installed ultra-wideband (UWB) system with anchors around the playing area. Kinexon says it delivers more than 200 live and post-session metrics and an open API (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). Studies sampled position data at 20 Hz ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/), [Blauberger 2021 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7923412/)).
- **PERFORM GPS Pro.** A GNSS wearable for outdoor sports. It samples at 10 Hz and has a stated speed accuracy of 0.05 m/s ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The brochure says it contains an IMU and lists more than 150 metrics with heart rate and IMU, 130 without IMU, and 110 without heart rate ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Its sensors come from Fitogether ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)).
- **PERFORM IMU.** A 15 g waist-worn wearable with a 3-axis accelerometer (plus or minus 16 g, sampled at 1 kHz, delivered at 100 Hz), a gyroscope, and a magnetometer ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). The handball IMU post says the IMU does not track positions but only movements, and then says in the same post that an IMU system uses position data to calculate metrics like acceleration ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)). The two statements conflict. The LPS, GPS, and IMU post says only that position-based metrics can be predicted with the IMU system in some sport-specific cases ([LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/)). Live data needs one anchor, and only acceleration load and jump count are live with an anchor (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))).
- **KINEXON ONE.** No public product page, brochure, or metric list exists in the sources reviewed. The only public use of the name is in a study that recorded position data at 20 Hz with "LPS KINEXON ONE" ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)). That study computed metabolic power and equivalent distance itself from the position data, so those are the authors' metrics, not Kinexon outputs. All `ONE` cells in the coverage table are therefore empty.
- **Kinexon Sports App.** The cloud software that shows metrics from every product. It has the views `STATISTICS`, `POST`, `DEVELOP`, `LIVE`, and (added in app version 12.2) `DIAGNOSTICS` ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/), [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)). Kinexon says all statistics and raw data are available as CSV exports or through a REST API, and it lists integrations with Teamworks, GPSDataViz, Edge10, Firstbeat, and Polar ([sport pages](https://kinexon-sports.com/sports/volleyball/)). The GPS Pro brochure adds individual PDF, Excel, and raw-data exports ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)).
- **KINEXON POST.** No public product page exists in the sources reviewed. The public sources use `POST` as the name of the Sports App view that shows one practice or match after it ends ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)), as opposed to `DEVELOP`, which tracks metrics over time.

### Metric count claims

Kinexon sources and studies give these totals, and they disagree:

| Claim | Product | Source |
|---|---|---|
| 109 exported external load variables | IMU-based Kinexon system, version 1.0, at 20 Hz | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/) |
| More than 50 live metrics | GPS Pro (older post) | [older GPS Pro post](https://kinexon-sports.com/blog/revolutionary-football-player-tracking-system-how-kinexon-perform-gps-pro-is-changing-the-game/) |
| More than 100 live metrics | GPS Pro | [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf) |
| About 120 live metrics | GPS Pro launch | [GPS Pro launch release](https://kinexon-sports.com/pr/kinexon-launches-new-gps-based-player-tracking-system/) |
| 110, 130, or more than 150 metrics, depending on heart rate and IMU | GPS Pro app package | [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf) |
| More than 180 positional and inertial metrics | Hockey | [NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/) |
| More than 200 live and post-session metrics | PERFORM LPS | product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/)) |
| More than 200 metrics for dashboards | Sports App with GPS Pro | [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf) |
| More than 300 metrics | Bundesliga clubs, handball, sports analytics page | [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [sport pages](https://kinexon-sports.com/sports/volleyball/), [sports data analytics page](https://kinexon-sports.com/technology/sports-data-analytics/) |

These counts cannot be reconciled. The public sources name far fewer distinct metrics than any of these totals. The coverage table lists 61 metric rows.

## Summary tables

Each table gives the metric, what it measures in a few words, its unit, and whether Kinexon publishes its calculation (Yes, Partly, or Not published). The calculation column reflects Kinexon's own material, not a study.

### Load metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Accumulated Acceleration Load` (AAL) | Whole-body acceleration load | AU | Partly |
| `Accumulated Acceleration Load per minute` (AAL/min) | AAL per unit time | AU/min | Partly |
| `Acceleration Load`; `Accel Load`; `Decel Load` | Load from speeding up and slowing down | Not published | Partly |
| `Mechanical Load` | Weighted load from accelerations and decelerations | AU | Partly |
| `Mechanical Intensity` | `Mechanical Load` per unit time | Not published | Partly |
| `Physio Load` | Distance, speed, and body weight combined | Not published | Partly |
| `Physio Intensity` | `Physio Load` per minute | Not published | Partly |
| `Load per Minute` | Per-minute load shown in the app | Not published | Not published |
| `Total Load` | Load total named by one team | Not published | Not published |

### Jump metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Jump Load` | Work done in jumping | J (AU in one study text) | Partly |
| `Jump Load per kilogram`; `Jump Load Per Mass` | `Jump Load` per kg of body mass | J/kg | Partly |
| `Jump Load per minute` | `Jump Load` per minute | Not published | Partly |
| `Number of Jumps`; `Jumps`; `Jump Count` | Jump count | count | Partly |
| `Jump Height` | Estimated height of each jump | cm | Partly |
| `Live Jumps` | Jump count during the session | count | Not published |
| `Airtime` | Time off the ground in a jump | Not published | Partly |
| `Max Jump Height Ratio` | Jump height versus the athlete's maximum | Not published | Not published |
| `High Intensity Jump to Total Jump Ratio` | Share of high-intensity jumps | ratio | Not published |
| `landing load`; `landing forces` | Landing stress | Not published | Not published |
| `vertical efforts` | Vertical effort events | Not published | Not published |
| `jump volume` | Volume of jumping | Not published | Not published |

### Impact and effort metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Impacts`; `Impact`; `impact force` | Hard contacts | Not published | Not published |
| `Exertions`; `Exertion Events`; `Efforts/Exertions` | High-intensity efforts | count | Partly |
| `High Intensity Exertions` | Exertions by intensity band | count | Not published |
| `Distance (Anaerobic Activity)` | Distance during high-load effort | Not published | Partly |
| `Anaerobic distance time` | Time in the anaerobic distance condition | Not published | Not published |
| `movement density` | Named for live tracking | Not published | Not published |

### Direction, speed, and distance metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Changes of Orientation` | Turns | Not published | Not published |
| `Change Of Direction` (COD) | Direction changes | count | Partly |
| `Max. Speed`; `Max Speed`; `Top Speed`; `Sprint Speed` | Fastest speed reached | km/h and mph | Partly |
| `Speed (Avg)`; `Average speed` | Average speed | km/h and mph | Not published |
| `Percentage of Max Speed`; `% of Max Speed` | Speed relative to the athlete's maximum | % | Partly |
| `Total Distance`; `Distance`; `Total Yardage` | Distance moved | m (yards in American football) | Not published |
| `Distance per minute`; `Distance / min` | Distance per minute | m/min | Partly |
| `Distance In Speed Zones` | Distance by speed band | m | Partly |
| `Time In Speed Zones` | Time by speed band | Not published | Not published |
| `Speed Zone Entry`; `Relative Speed Zone Entries` | Moves into a faster band | count | Partly |
| `High-Speed Distance`; `High-Speed Yardage` | Distance above a speed line | m (yd in American football) | Partly |
| `High Intensity Runs` | Named in the Bundesliga list | Not published | Not published |
| `Sprints`; `Sprint`; `Number of Sprints` | Runs above sprint speed | count | Partly |
| `Sprint Duration` | Length of sprint efforts | Not published | Not published |
| `Repeated Sprints`; `speed repetitions` | Sprints with short rest | Not published | Partly |
| `Playing Time`; `Time Played on Offense`; `Time Played on Defense` | Active time by team phase | Not published | Not published |

### Acceleration and deceleration metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Acceleration`; `Deceleration` (event counts) | Hard speed-ups and slow-downs | count | Partly |
| `High / very high acceleration and deceleration counts`; `High Intensity Accelerations` | Only the hardest events | count | Partly |
| `Acceleration (Max)`; `Deceleration (Max)` | Hardest single event | Not published | Partly |
| `Acceleration/Deceleration Zones` | Intensity bands for events | yd/s^2 as printed in the example | Not published |

### Metabolic power metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Metabolic Power` | Energy cost per second | Not published | Not published |
| `Metabolic Power per Mass (Max)` | Peak energy cost per kg | Not published | Partly |
| `High Metabolic Power Distance` (HMPD); `HMLD`; `HMDL`; `High Metabolic Load` | Distance at high energy cost | m | Partly |
| `High Speed And Acceleration Distance`; `High speed and acceleration time` | Fast running and hard acceleration combined | Not published | Not published |

### Heart rate metrics summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Heart Rate (Min, Max, Avg)` | Heart rate during the session | Not published | Partly |
| `Time In Heart Rate Zones` | Time per heart rate band | Not published | Not published |
| `Heart Rate Recoveries`; `heart rate impulse` | Heart rate fall and cumulative dose | Not published | Not published |
| `TRIMP` | Heart-rate-based session load | Not published | Partly |
| `Percentage of maximum heart rate` | Heart rate relative to maximum | % | Not published |

### Distribution and Sports App summary

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `High vs. Low Intensity Distribution` | Share of hard and easy work | Not published | Partly |
| `Sprint Diagnostic` outputs | On-field sprint test | s for splits, other units Not published | Partly |
| `Rolling Window Analysis` outputs | Hardest stretch of play | Depends on the metric chosen | Partly |
| `Relative Analysis` values | Value against a chosen target | ratio (1.2 = 20 % above target) | Partly |
| `Phase Index` values | Typical and high-end range per drill type | count and metric units | Partly |
| Position export columns | Raw position data | ms, m | Not applicable (raw columns) |

## Product coverage

The inventory has 61 metric rows that cover about 95 name variants, plus the 9 position columns. Sport names are the sports in the cited sources. "Unit" is the unit the source states, or "Not published". The `App` column means the Sports App computes or shows the item (widgets and diagnostics), or names it as an app metric. `POST` has one entry because the public sources give it no metric list of its own. `ONE` is empty because no public source names a metric for KINEXON ONE.

| Kinexon name (exact wording) | Unit | LPS | GPS Pro | IMU | ONE | App | POST | Sports |
|---|---|---|---|---|---|---|---|---|
| `Accumulated Acceleration Load (AAL)` | AU (arbitrary units) | B | Y | Y |  | Y |  | basketball, volleyball, handball, football (soccer), American football |
| `Accumulated Acceleration Load per minute (AAL/min)` | AU/min | B | B | Y |  |  |  | basketball, volleyball, handball |
| `Acceleration Load`; `Accel Load`; `Decel Load` | Not published | P | P | Y |  |  |  | basketball, handball, volleyball, football (soccer), ice hockey |
| `Mechanical Load` | AU (arbitrary units) | B | Y | Y |  |  |  | basketball, football (soccer), American football |
| `Mechanical Intensity` | Not published (Mechanical Load per unit time) | P | P | P |  |  |  | basketball, football (soccer) |
| `Physio Load` | Not published | P | P | P |  |  |  | not stated |
| `Physio Intensity (Physio Load per minute)` | Not published | P | P | P |  |  |  | not stated |
| `Load per Minute` | Not published |  |  | P |  | Y |  | volleyball |
| `Total Load` | Not published | P | P |  |  |  |  | American football |
| `Jump Load` | J (joules) in one study table; AU in the same study text | B | B | Y |  |  |  | volleyball, handball, basketball |
| `Jump Load per kilogram`; `Jump Load Per Mass` | J/kg |  |  | Y |  |  |  | volleyball, handball |
| `Jump Load per minute` | Not published | P | P | P |  |  |  | not stated |
| `Number of Jumps`; `Jumps`; `Jump Count` | count | B | B | Y |  |  |  | volleyball, basketball, handball |
| `Jump Height` | cm (also shown in feet and inches) | B | B | Y |  |  |  | volleyball, handball, basketball |
| `Live Jumps` | count (live) |  |  | Y |  |  |  | volleyball |
| `Airtime` | Not published | Y |  |  |  |  |  | handball |
| `Max Jump Height Ratio` | Not published | P |  | P |  |  |  | volleyball |
| `High Intensity Jump to Total Jump Ratio` | Not published (ratio) | P |  | P |  |  |  | volleyball |
| `Landing load`; `landing forces` | Not published | P |  | P |  |  |  | volleyball |
| `Vertical efforts` | Not published | P |  | P |  |  |  | volleyball |
| `Jump volume` | Not published | P |  | P |  |  |  | volleyball |
| `Impacts`; `Impact`; `Impact force` | Not published | P |  | Y |  |  |  | ice hockey, football (soccer), volleyball |
| `Exertions`; `Exertion Events`; `Efforts/Exertions` | count | B | Y | Y |  |  |  | basketball, volleyball, handball, American football, ice hockey, football (soccer) |
| `High Intensity Exertions`; `high and very high exertions` | count | P |  | P |  |  |  | volleyball, handball |
| `Distance (Anaerobic Activity)` | Not published | P |  | P |  |  |  | basketball |
| `Anaerobic distance time` | Not published | P | P |  |  |  |  | football (soccer) |
| `Movement density` | Not published | P |  | P |  |  |  | volleyball |
| `Changes of Orientation` | Not published |  |  | Y |  |  |  | volleyball, handball |
| `Change Of Direction (COD)` | count | Y | Y |  |  |  |  | football (soccer), handball, basketball |
| `Max. Speed`; `Max Speed`; `Top Speed`; `Sprint Speed` | km/h and mph | P | Y | Y |  |  |  | volleyball, football (soccer), American football, handball, basketball |
| `Speed (Avg)`; `Average speed` | km/h and mph |  | Y |  |  | P |  | football (soccer), basketball |
| `Percentage of Max Speed`; `% of Max Speed` | % |  | Y |  |  |  |  | American football, football (soccer) |
| `Total Distance`; `Distance`; `Total Yardage` | m (also yards in American football) | P | Y | Y |  |  |  | volleyball, football (soccer), American football, handball |
| `Distance per minute`; `Distance / min` | m/min |  | Y | P |  |  |  | basketball, football (soccer) |
| `Distance In Speed Zones` | m | P | Y |  |  |  |  | football (soccer), American football, handball |
| `Time In Speed Zones` | Not published |  | Y |  |  |  |  | football (soccer) |
| `Speed Zone Entry`; `Relative Speed Zone Entries` | count |  | Y |  |  |  |  | football (soccer) |
| `High-Speed Distance`; `High-Speed Yardage` | m (yd in American football) | P | Y | P |  |  |  | American football, basketball, football (soccer), handball |
| `High Intensity Runs` | Not published | P | P |  |  |  |  | football (soccer) |
| `Sprints`; `Sprint`; `Number of Sprints` | count | P | Y | P |  |  |  | football (soccer), American football, handball |
| `Sprint Duration` | Not published |  |  |  |  | P |  | basketball |
| `Repeated Sprints`; `speed repetitions` | Not published |  | Y |  |  |  |  | football (soccer) |
| `Playing Time`; `Time Played on Offense`; `Time Played on Defense` | Not published | P |  |  |  |  |  | handball |
| `Acceleration`; `Deceleration (event counts)` | count | P | Y | P |  |  |  | football (soccer), volleyball, handball, basketball |
| `High / very high acceleration and deceleration counts`; `High Intensity Accelerations` | count |  | P | P |  |  |  | basketball, football (soccer) |
| `Acceleration (Max)`; `Deceleration (Max)` | Not published |  | Y |  |  |  |  | football (soccer), American football |
| `Acceleration/Deceleration Zones (Low, Medium, High, Very High)` | yd/s2 as printed in the example |  | P |  |  |  |  | American football |
| `Metabolic Power` | Not published | P | Y |  |  |  |  | football (soccer), handball |
| `Metabolic Power per Mass (Max)` | Not published |  | Y |  |  |  |  | American football |
| `High Metabolic Power Distance (HMPD, HMLD, HMDL)`; `High Metabolic Load` | m | P | Y |  |  | Y |  | football (soccer), volleyball |
| `High Speed And Acceleration Distance`; `High speed and acceleration time` | Not published | P | Y |  |  |  |  | football (soccer) |
| `Heart Rate (Min, Max, Avg)` | Not published | P | Y | Y |  |  |  | volleyball, football (soccer) |
| `Time In Heart Rate Zones` | Not published |  | Y |  |  |  |  | football (soccer) |
| `Heart Rate Recoveries`; `heart rate impulse` | Not published | P | Y |  |  |  |  | football (soccer) |
| `TRIMP` | Not published |  | Y | Y |  |  |  | football (soccer), volleyball |
| `Percentage of maximum heart rate` | % | P | P | P |  |  |  | handball |
| `High vs. Low Intensity Distribution` | Not published |  |  | Y |  |  |  | basketball |
| `Sprint Diagnostic outputs (time splits, average speed, maximum speed, maximum acceleration, velocity and acceleration curves)` | s, speed and acceleration units not published | Y | Y |  |  | Y |  | football (soccer), basketball, American football |
| `Rolling Window Analysis outputs (window counts, average and maximum window value, time of peak)` | Depends on the metric chosen | Y | Y | Y |  | Y |  | basketball, football (soccer), American football, volleyball, ice hockey |
| `Relative Analysis values (relative value, target value, playing time)` | ratio (1.2 = 20 % above target) |  |  |  |  | Y |  | not stated |
| `Phase Index values (phase type, normative range, record count)` | count and metric units |  |  |  |  | Y | Y | football (soccer), basketball |
| `Position export columns: ts in ms`, `sensor id`, `mapped id`, `full name`, `number`, `group id`, `group name`, `x in m`, `y in m` | ms, m |  |  |  |  |  |  | not stated |

### Count by product

One metric can appear in several products, so the product counts do not add up to 61.

| Product | `Y` (tied to the product) | `B` (blanket statement) | `P` (several products or none) | Named in total |
|---|---|---|---|---|
| PERFORM LPS | 4 | 7 | 30 | 41 |
| PERFORM GPS Pro | 27 | 4 | 11 | 42 |
| PERFORM IMU | 18 | 0 | 19 | 37 |
| KINEXON ONE | 0 | 0 | 0 | 0 |
| Kinexon Sports App | 7 | 0 | 2 | 9 |
| KINEXON POST | 1 | 0 | 0 | 1 |

The position columns come from a source that names no product, so the table above does not count them.

## Metric blocks

Each block lists the same fields in the same order. Values from studies are examples from those studies, not benchmarks. A threshold labeled "study setting" is never a Kinexon default.

### Load metrics

#### `Accumulated Acceleration Load` (AAL)

The sources give these details:

- **What it measures:** The total whole-body movement stress from accelerating, slowing, changing direction, and jumping, added up over a drill, session, or game.
- **Window or phase:** A drill, session, or game, as the user selects it.
- **Calculation:**
  - Vendor definition (paraphrased): a load built from a three-dimensional acceleration pattern from the IMU ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). It adds up the effect of rapid accelerations and decelerations in training and games ([acceleration post](https://kinexon-sports.com/blog/athletic-performance-why-track-acceleration/)). It does not separate running from jumping ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)). Kinexon notes that some manufacturers call this metric Player Load ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)).
  - Formula as printed in a study that calls AAL a proprietary measure ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)): `AAL = sqrt[(Ac1(n) - Ac1(n-1))^2 + (Ac2(n) - Ac2(n-1))^2 + (Ac3(n) - Ac3(n-1))^2 / 100]`. `Ac1` to `Ac3` are the three accelerometer axes, and 100 (0.01) is a scaling factor. The study prints the division by 100 in a way that does not show whether it sits inside or outside the square root.
  - Another study ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)) describes "player load" in general, as used by a number of companies, as the accumulated square root of the sum of squared instantaneous rates of acceleration change in the three planes. That study used Kinexon tags but does not call this Kinexon's formula, so this page does not attribute it to Kinexon. A third study says it sums accelerations in the x, y, and z axes ([women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/)).
  - Restatement (not a Kinexon statement): the sample-to-sample change in 3-axis acceleration, summed over time. Kinexon has not published its own formula: Not published.
- **Thresholds:** None for the total. Whether a noise floor is applied: Not published.
- **Inputs:** A 3-axis accelerometer, plus or minus 16 g, sampled at 1 kHz and delivered at 100 Hz ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)).
- **Units:** Arbitrary units (AU). Study values: 150.8 +/- 32.4 AU in 3x3 basketball matches ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)). Kinexon uses 650 AU for a basketball game ([game intensity post](https://kinexon-sports.com/blog/sustaining-game-intensity-athlete-performance-tracking/)) and 800 AU for a hockey forward ([NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/)) as illustrations, not norms. The basketball post names AAL for the 650 AU figure. The NHL post does not name the metric, so the 800 AU figure is not tied to AAL.
- **Variants:** `Accumulated Acceleration Load per minute` (`AAL/min`) is a separate metric, described below. The window-based form appears under the Rolling Window Analysis outputs.
- **Comparison with standard methods or other vendors:** The closest Catapult metric is PlayerLoad. Sources that support the match:
  - Kinexon says other manufacturers call this metric Player Load ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)).
  - The study formula has the same structure as the PlayerLoad equation.
  - Catapult describes PlayerLoad as an instantaneous rate of change of acceleration divided by a scaling factor, and says the total acceleration is divided by 100 ([Catapult PlayerLoad blog](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)).

  The mapping rests on a name match and a similar structure. It does not show that the formulas, scaling, or sampling rate are the same. Sources that point the other way:
  - The Koyama study prints its division by 100 in a way that does not show whether it sits inside or outside the square root ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
  - The Pantazis study describes PlayerLoad as the square root of the sum of squared instantaneous changes in acceleration, divided by 100, and cites another paper for it ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
  - A review reports that device-specific versions of this metric give inconsistent and incomparable results across devices, mostly through scaling and sampling rate, and lists variations "primarily in the scaling factor" ([2025 acceleration-load review](https://www.mdpi.com/1424-8220/25/9/2764)).

  Kinexon's sampling and filtering for AAL are not published. Do not treat AAL and PlayerLoad values as interchangeable. Do not pool values from the two vendors until you check the formula, scaling, and sampling rate for each.
- **What changes the number:**
  - Activity type: running, jumping, and contact all add load, and you cannot tell them apart in the total ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)).
  - Time played. `AAL/min` removes this.
  - Opponent level: in one study, AAL per minute was higher against professional teams than against college teams or scrimmages ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
  - Where the sensor sits. One study used a holster stitched into the shorts "near the right posterior superior iliac spine" and notes that a spot closer to the center of mass gives a more accurate reading ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)). Another study used a position between the scapulae ([women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/)). Whether the two placements give the same values: Not published.
  - Sampling rate. The Stone and women's basketball studies report 20 Hz ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/)), and the Koyama study reports 100 Hz ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)). A review of this equation family says the division by 100 is most likely a scaling factor but may be a residual of the sampling rate ([2025 acceleration-load review](https://www.mdpi.com/1424-8220/25/9/2764)). Whether Kinexon values at different rates agree: Not published.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [acceleration post](https://kinexon-sports.com/blog/athletic-performance-why-track-acceleration/), [March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/), [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037), [game intensity post](https://kinexon-sports.com/blog/sustaining-game-intensity-athlete-performance-tracking/), [NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/), [Catapult PlayerLoad blog](https://www.catapult.com/blog/fundamentals-playerload-athlete-work), [2025 acceleration-load review](https://www.mdpi.com/1424-8220/25/9/2764), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)

#### `Accumulated Acceleration Load per minute` (AAL/min)

The sources give these details:

- **What it measures:** How fast load builds, so a short hard drill and a long easy one can be compared.
- **Window or phase:** The phase or drill you select (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))).
- **Calculation:** Vendor definition (paraphrased): an intensity metric that normalizes AAL over time ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))). Restatement (not a Kinexon statement): AAL divided by minutes in the window. Whether minutes means clock time or active time: Not published. Kinexon warns that an average that includes instruction and waiting time differs from one that counts only active participation (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))).
- **Thresholds:** None. Kinexon suggests no default targets (Not published).
- **Inputs:** AAL and time.
- **Units:** AU/min ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) reports AU per minute).
- **Variants:** The window-based version appears under the Rolling Window Analysis outputs.
- **Comparison with standard methods or other vendors:** No source supports a per-minute match beyond the AAL comparison.
- **What changes the number:** The time you divide by (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))), the phase or drill you select, and everything that changes AAL.
- **Sources:** basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/)), [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)

#### `Acceleration Load`; `Accel Load`; `Decel Load`

The sources give these details:

- **What it measures:** The stress from speeding up (`Accel Load`) and from slowing down (`Decel Load`). Together they make `Mechanical Load`.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): events are sorted into intensity bands, multiplied by a proprietary weighting factor for their band, and summed into `Accel Load` and `Decel Load` ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). In football, Kinexon describes acceleration load as the stress when a player gains speed or leaves a standstill, and deceleration load as the stress when slowing or stopping abruptly ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)). Kinexon also describes `Acceleration Load` as showing how intense movements or phases are ([jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/)), and says it weighs accumulated load from acceleration against deceleration ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)). Number of bands and the weights: Not published.
- **Thresholds:** Not published. Study event thresholds appear under the `Acceleration` and `Deceleration` event counts.
- **Inputs:** Acceleration and deceleration events.
- **Units:** Not published.
- **Variants:** `Accel Load` and `Decel Load` are the two parts of `Mechanical Load`. The sources name the metric for basketball, handball, volleyball, football (soccer), and ice hockey.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Event thresholds and band edges (Not published), time played, and sport and game rules. Kinexon says handball `Jump Load` is usually higher in training than in games, while `Acceleration Load` is often higher in games because accelerations are more demanding there ([jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/)).
- **Sources:** [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/), [football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/), [jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/), [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)

#### `Mechanical Load`

The sources give these details:

- **What it measures:** The load on the legs from accelerations and decelerations, weighted so hard efforts count more than easy ones.
- **Window or phase:** Summed per phase in one study ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
- **Calculation:**
  - Vendor definition (paraphrased): a metric for two-dimensional movement, including accelerations and decelerations. Each event is sorted by intensity, multiplied by a proprietary weighting factor for its band, and summed. `Accel Load` plus `Decel Load` equals `Mechanical Load` ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). In football, Kinexon ties it to stress on the legs ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)) and to acceleration and deceleration events ([individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/)).
  - A study describes the same method: events go into several weighted intensity bins and are summed per phase ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)). Another study says it is derived from horizontal-plane acceleration and deceleration actions ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
  - Formula, bin edges, and weights: Not published.
- **Thresholds:** Not published. Kinexon states that the top intensity band is about 25 % of total work in professional basketball, and that guards run higher ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). This is a vendor observation, not a default.
- **Inputs:** Position-based or IMU-based acceleration events.
- **Units:** Arbitrary units (AU). Study value: 377.9 +/- 54.6 AU in 3x3 basketball matches ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
- **Variants:** `Mechanical Intensity` is the per-time form. `Accel Load` and `Decel Load` are the two parts.
- **Comparison with standard methods or other vendors:** No source supports a Catapult equivalent. Catapult notes a "2D" variant of PlayerLoad that leaves out vertical acceleration ([Catapult PlayerLoad blog](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)), but no source says it equals `Mechanical Load`.
- **What changes the number:** Time played, position (Kinexon says guards accumulate more per minute than forwards and centers, [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)), the event thresholds (Not published), and the data source. Which sensor types produce the same values: Not published.
- **Sources:** [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/), [football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/), [individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037), [Catapult PlayerLoad blog](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)

#### `Mechanical Intensity`

The sources give these details:

- **What it measures:** How hard the legs worked per minute.
- **Window or phase:** A phase or a session ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)).
- **Calculation:** Vendor definition (paraphrased): total `Mechanical Load` divided by time over a phase or a session ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Time basis (clock or active): Not published.
- **Thresholds:** Not published.
- **Inputs:** `Mechanical Load` and time.
- **Units:** Not published. Restatement (not a Kinexon statement): AU per unit time.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The time you divide by and everything that changes `Mechanical Load`. Kinexon says position and playing style change it ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)).
- **Sources:** [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)

#### `Physio Load`

The sources give these details:

- **What it measures:** A volume-of-work measure that mixes how far, how fast, and how heavy the athlete is.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): a combination of distance, speed, and body weight ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Kinexon also names it among volume metrics ([volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)). Formula, weights, and units: Not published. A Kinexon video on how to calculate physio load exists, but its content is not readable in public text (see the Not published summary).
- **Thresholds:** Not published.
- **Inputs:** Distance, speed, and body weight.
- **Units:** Not published.
- **Variants:** `Physio Intensity` is the per-minute form.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Body weight (the athlete's entered mass), distance, and speed. How each is weighted: Not published.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)

#### `Physio Intensity` (Physio Load per minute)

The sources give these details:

- **What it measures:** `Physio Load` per minute of activity.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the intensity form of `Physio Load` ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Restatement (not a Kinexon statement): `Physio Load` divided by minutes.
- **Thresholds:** Not published.
- **Inputs:** `Physio Load` and time.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The time denominator and everything that changes `Physio Load`.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)

#### `Load per Minute`

The sources give these details:

- **What it measures:** A per-minute load value that Stanford volleyball tracks live in the Sports App next to AAL, Jump Count, and High Metabolic Load ([Stanford volleyball post](https://kinexon-sports.com/blog/how-stanford-volleyball-uses-micro-dose-training-to-stay-match-ready/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Not published. Which load it divides: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [Stanford volleyball post](https://kinexon-sports.com/blog/how-stanford-volleyball-uses-micro-dose-training-to-stay-match-ready/)

#### `Total Load`

The sources give these details:

- **What it measures:** A load value that the University of Wyoming football staff names alongside top speed and maximum acceleration and deceleration ([Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Not published. The Wyoming post does not say whether it is AAL, `Mechanical Load`, or another total.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/)

### Jump metrics

#### `Jump Load`

The sources give these details:

- **What it measures:** How much work the athlete did in jumping, so a few high jumps and many small hops are told apart.
- **Window or phase:** Summed over the session in the Stone study ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
- **Calculation:**
  - Vendor definition (paraphrased): a load based on the one-dimensional vertical (z) acceleration pattern ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Kinexon says Jump Count shows how much jumping happened and `Jump Load` adds how demanding those jumps were, for example when jumps come in quick succession or in explosive drills ([volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/)).
  - Formula stated in two published studies: body mass times the gravity constant times jump height in meters, calculated for each jump event, then summed over the session ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)). The Stone study writes the gravity constant as 9.8 m/s (the unit is missing the square, a typo in the paper). The Pantazis study writes `JL = m x g x h` with g = 9.81 m/s^2 ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)). Kinexon has not published its own formula: Not published.
  - Restatement (not a Kinexon statement): `Jump Load = sum over jumps of (body mass x g x jump height)`. The worked example on this page runs this formula.
- **Thresholds:** Not published by Kinexon. Study settings (not Kinexon defaults): a jump needs at least 0.3 s of airtime ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)). A different study identified jumps at a minimum dwell time of 0.4 s ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)). A third counted "high-intensity jumps" above 0.40 m ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Inputs:** Body mass (kg) and jump height in meters (see `Jump Height`).
- **Units:** J (joules) in the Stone results table, while the Stone text says arbitrary units, so the unit label is not consistent across sources ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
- **Variants:** `Jump Load per kilogram` (`Jump Load Per Mass`) and `Jump Load per minute`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Body mass (the same jumps give more joules for a heavier athlete), the jump height estimate and its error (see `Jump Height`), and the minimum jump rule. Kinexon says `Jump Load` is usually higher in training than in games in handball ([jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/)).
- **Sources:** [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/), [jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/)

#### `Jump Load per kilogram`; `Jump Load Per Mass`

The sources give these details:

- **What it measures:** `Jump Load` with body mass removed, so players of different size can be compared.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): `Jump Load` that accounts for player weight, suited to comparing players, where consistently high values may signal a need to change recovery ([jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/)). The IMU brochure shows a sample tile with the unit J/kg ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Formula: Not published. Restatement (not a Kinexon statement): `Jump Load` divided by body mass. Under the Stone formula this equals `g x sum(jump heights)`, which the worked example shows.
- **Thresholds:** Not published.
- **Inputs:** `Jump Load` (J) and body mass (kg).
- **Units:** J/kg ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)).
- **Variants:** Two names appear: `Jump Load per kilogram` and `Jump Load Per Mass`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Jump heights and the minimum jump rule. It does not change with body mass if the same jump heights are measured.
- **Sources:** [jumper's knee post](https://kinexon-sports.com/blog/prevention-jumpers-knee/), [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)

#### `Jump Load per minute`

The sources give these details:

- **What it measures:** `Jump Load` over time, for comparing sessions of different length.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the intensity form of `Jump Load` ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Time basis: Not published.
- **Thresholds:** Not published.
- **Inputs:** `Jump Load` and time.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The time denominator and everything that changes `Jump Load`.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)

#### `Number of Jumps`; `Jumps`; `Jump Count`

The sources give these details:

- **What it measures:** How many jumps the athlete made.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): jumps are counted from vertical displacement over certain height thresholds ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Kinexon lists the count as a core IMU metric ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)) and as one of two live metrics with an anchor (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). The height and airtime thresholds: Not published.
- **Thresholds:** Not published by Kinexon. Study settings (not Kinexon defaults): at least 0.3 s of airtime ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)), and at least 0.4 s of dwell time ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
- **Inputs:** IMU vertical acceleration.
- **Units:** Count.
- **Variants:** Three names appear: `Number of Jumps`, `Jumps`, and `Jump Count`. `Live Jumps` is the live form.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The minimum jump rule. Arizona State volleyball staff say total count can mislead because some jumps are low in amplitude ([Arizona State post](https://kinexon-sports.com/blog/arizona-state-womens-volleyballjump-count-performance-data/)).
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/)), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Arizona State post](https://kinexon-sports.com/blog/arizona-state-womens-volleyballjump-count-performance-data/)

#### `Jump Height`

The sources give these details:

- **What it measures:** How high the athlete jumped, as an estimate of explosiveness.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:**
  - Vendor definition (paraphrased): Kinexon says jump height shows explosiveness and can be split into categories ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)). Kinexon says the sensor measures the time from takeoff impact to landing impact ([EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/)). The estimation formula: Not published.
  - A validation study reports that Kinexon estimates flight time using the data from the IMU and uses it to estimate jump height with Equation 1 of that study ([Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949)).
  - A Kinexon volleyball post gives a different description (standing reach versus peak reach) ([volleyball positions post](https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/)). That text is generic and does not fit a body-worn sensor, so this page does not use it.
- **Thresholds:** Not published. See `Jump Load` and `Number of Jumps` for study minimums.
- **Inputs:** IMU data.
- **Units:** cm. The IMU brochure shows 68 cm as a sample, with feet and inches ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)).
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** The validation study compares Kinexon with the Vert wearable and finds the two close ([Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949)). No source gives a Catapult comparison.
- **What changes the number:** The estimation method and sensor placement. In the volleyball validation study the Kinexon sensor sat between the shoulder blades and read on average 9.46 cm higher than Optojump, with a 1.03 cm difference from the Vert wearable ([Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949)). Do not mix Kinexon jump heights with force plate or Optojump values.
- **Sources:** [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/), [EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/), [Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949), [volleyball positions post](https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/), [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)

#### `Live Jumps`

The sources give these details:

- **What it measures:** The jump count while the session is running.
- **Window or phase:** Live, during the session (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))).
- **Calculation:** The IMU brochure lists it ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). The product pages say live jump count needs one anchor and everything else is available after the session (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). Calculation: Not published. Restatement (not a Kinexon statement): `Number of Jumps` streamed live.
- **Thresholds:** Not published.
- **Inputs:** IMU plus one anchor.
- **Units:** Count.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Anchor range and connection. Range: Not published for IMU anchors.
- **Sources:** product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/)), [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)

#### `Airtime`

The sources give these details:

- **What it measures:** How long an athlete stays off the ground in a jump.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the sensor measures the time from impact at takeoff to impact at landing ([EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/)). Filtering: Not published.
- **Thresholds:** Not published. The Stone study uses 0.3 s as a study minimum for a jump ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
- **Inputs:** Sensor impact events.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** How takeoff and landing impacts are detected: Not published.
- **Sources:** [EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)

#### `Max Jump Height Ratio`

The sources give these details:

- **What it measures:** Jump height compared with the athlete's maximum, so a coach can see whether the athlete is reaching top effort.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names it as a metric to review next to jump data ([volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/)). Definition: Not published. Which maximum it uses: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/)

#### `High Intensity Jump to Total Jump Ratio`

The sources give these details:

- **What it measures:** The share of jumps that were high-intensity.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names it ([volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/)). Definition and the "high intensity" cut-off: Not published.
- **Thresholds:** Not published. Study setting for comparison only (not a Kinexon default): jumps above 0.40 m were called high-intensity ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Inputs:** Jump counts.
- **Units:** A ratio.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The cut-off for high intensity and everything that changes `Number of Jumps`.
- **Sources:** [volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)

#### `landing load`; `landing forces`

The sources give these details:

- **What it measures:** Kinexon says it lets volleyball staff monitor landing stress.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names it on the volleyball sport page ([sport pages](https://kinexon-sports.com/sports/volleyball/)). Definition, unit, and sensor basis: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** Two names appear: `landing load` and `landing forces`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [sport pages](https://kinexon-sports.com/sports/volleyball/)

#### `vertical efforts`

The sources give these details:

- **What it measures:** Vertical effort events, named on the volleyball sport page next to impact force and movement density ([sport pages](https://kinexon-sports.com/sports/volleyball/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [sport pages](https://kinexon-sports.com/sports/volleyball/)

#### `jump volume`

The sources give these details:

- **What it measures:** Volume of jumping, named on the volleyball sport page ([sport pages](https://kinexon-sports.com/sports/volleyball/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Not published. The sport page does not say whether it equals `Jump Count` or `Jump Load`.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [sport pages](https://kinexon-sports.com/sports/volleyball/)

### Impact and effort metrics

#### `Impacts`; `Impact`; `impact force`

The sources give these details:

- **What it measures:** Hard contacts such as collisions or landings, depending on the sport.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon lists `Impacts` as an IMU metric next to `Acceleration Load` and `Exertions` in hockey ([NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/)) and in the Bundesliga metric list ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). A Kinexon volleyball post describes "impact" as swing force measured through ball velocity ([volleyball positions post](https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/)). That description does not fit a waist-worn sensor, so this page treats it as unreliable. Kinexon's definition, threshold, and unit: Not published.
- **Thresholds:** Not published.
- **Inputs:** IMU ([NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/)).
- **Units:** Not published.
- **Variants:** Three names appear: `Impacts`, `Impact`, and `impact force`. The sources name the metric for ice hockey, football (soccer), and volleyball ([sport pages](https://kinexon-sports.com/sports/volleyball/)).
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [NHL post](https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [volleyball positions post](https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/), [sport pages](https://kinexon-sports.com/sports/volleyball/)

#### `Exertions`; `Exertion Events`; `Efforts/Exertions`

The sources give these details:

- **What it measures:** How many high-intensity efforts the athlete made.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:**
  - Vendor definition (paraphrased): high-intensity activity above a certain acceleration load threshold ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Basketball: instances of high-intensity effort based on the instantaneous `Acceleration Load` ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)). Football: a count of separate high-intensity actions, including hard accelerations, decelerations, direction changes, and high-speed bursts ([individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/)). Specific instances of high effort help show stress and injury risk ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)).
  - The sources describe it a little differently by sport and product, and Kinexon does not reconcile them. Formula: Not published.
- **Thresholds:** Not published. Study setting (not a Kinexon default): one study reports exertion events were found when at least 4.5 G was held for 1.0 s, "as dictated by the proprietary software" ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
- **Inputs:** Instantaneous acceleration load.
- **Units:** Count ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) reports cases per minute).
- **Variants:** Three names appear: `Exertions`, `Exertion Events`, and `Efforts/Exertions`. `High Intensity Exertions` groups them by intensity.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The threshold and duration rule, the sport, and the time window.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/), [individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/), [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)

#### `High Intensity Exertions`; high and very high exertions

The sources give these details:

- **What it measures:** Exertions grouped by how hard they were.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names it for volleyball ([volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/)). For handball, Kinexon describes density as high and very high exertions per segment ([handball load post](https://kinexon-sports.com/blog/handball-performance-tracking-load-monitoring/)), so Kinexon grades exertions into bands. Band edges: Not published.
- **Thresholds:** Not published.
- **Inputs:** Exertion events.
- **Units:** Count.
- **Variants:** `High Intensity Exertions` (volleyball) and high and very high exertions (handball).
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The band edges and everything that changes `Exertions`.
- **Sources:** [volleyball jump data post](https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/), [handball load post](https://kinexon-sports.com/blog/handball-performance-tracking-load-monitoring/)

#### `Distance (Anaerobic Activity)`

The sources give these details:

- **What it measures:** How far the athlete traveled while making high-acceleration-load effort.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): distance covered while producing high instantaneous `Acceleration Load` ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)). The load cut-off: Not published.
- **Thresholds:** Not published.
- **Inputs:** Distance and acceleration load.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The cut-off and everything that changes `Exertions`.
- **Sources:** [March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)

#### `Anaerobic distance time`

The sources give these details:

- **What it measures:** Time spent in the anaerobic distance condition ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Named in the Bundesliga metric list ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Definition: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)

#### `movement density`

The sources give these details:

- **What it measures:** Named on the volleyball sport page as something to track live ([sport pages](https://kinexon-sports.com/sports/volleyball/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Not published. The Wyoming football post mentions "acceleration density" ([Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/)), which is also undefined.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match. Catapult's support site lists an article on acceleration density that this page does not cover, so it makes no match.
- **What changes the number:** Not published.
- **Sources:** [sport pages](https://kinexon-sports.com/sports/volleyball/), [Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/)

### Direction, speed, and distance metrics

#### `Changes of Orientation`

The sources give these details:

- **What it measures:** How often the athlete turned.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the IMU brochure ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)) and in Kinexon's handball IMU post ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)). Definition, angle threshold, and unit: Not published. Do not assume it matches `Change Of Direction` (COD). Both names appear in Kinexon text, and the relation between them is not published.
- **Thresholds:** Not published.
- **Inputs:** IMU gyroscope and accelerometer. The IMU brochure lists a gyroscope at 200 Hz ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)).
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)

#### `Change Of Direction` (COD)

The sources give these details:

- **What it measures:** How many times the athlete changed direction.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed as a performance event in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The EHF EURO post lists it as a popular LPS metric ([EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/)). Kinexon groups it with acceleration and deceleration as events derived from changes in velocity ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Definition and angle: Not published.
- **Thresholds:** Not published. Study setting (not a Kinexon default): a study counted high-intensity changes of direction as turns above 90 degrees together with deceleration below -2 m/s^2 ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Inputs:** Position or IMU data.
- **Units:** Count.
- **Variants:** `Changes of Orientation` is a separate name in the IMU material.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The angle and speed rules and the data source.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)

#### `Max. Speed`; `Max Speed`; `Top Speed`; `Sprint Speed`

The sources give these details:

- **What it measures:** The fastest speed the athlete reached.
- **Window or phase:** The fastest effort in the window you select. Kinexon words it as the highest speed in a practice session ([live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)).
- **Calculation:** Vendor definition (paraphrased): the highest speed an athlete achieves in a practice session ([live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)), also called top-end speed ([max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/)). Formula and smoothing: Not published. The handball IMU post says the IMU does not track positions ("does not track positions but only movements"), but says in the same post that "An IMU system uses position data to calculate metrics like acceleration" ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)). The two statements conflict. The LPS, GPS, and IMU post says position-based metrics "can be predicted with the IMU system" in some sport-specific cases ([LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/)). How the IMU reports `Max. Speed`: Not published.
- **Thresholds:** None.
- **Inputs:** GPS Pro: 10 Hz GNSS with a stated speed accuracy of 0.05 m/s ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). LPS: root mean square error for speed is about 0.15 m/s, cited in the Bassek study from earlier work (Hoppe 2018; Fleureau 2020; Blauberger 2021) and not measured there ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
- **Units:** km/h and mph. The GPS Pro brochure shows 29 km/h and 18 mph as a sample ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The Stone study reports mph ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
- **Variants:** Four names appear: `Max. Speed`, `Max Speed`, `Top Speed`, and `Sprint Speed`. The sources name the metric for volleyball, football (soccer), American football, handball, and basketball.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor comparison of the number.
- **What changes the number:** Product and sensor (GNSS, LPS, or IMU estimate), smoothing, and the fastest effort in the window. Study processing for comparison (not a Kinexon default): a 4th-order Butterworth low-pass filter at 1 Hz on position, then central differences ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
- **Sources:** [live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/), [max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/), [handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/), [LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)

#### `Speed (Avg)`; `Average speed`

The sources give these details:

- **What it measures:** Average speed over the window.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** The GPS Pro brochure lists `Speed (Max, Avg)` ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Sprint Diagnostics also report average speed ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)). A study exported it in mph ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)). Calculation and whether standing time is included: Not published.
- **Thresholds:** Not published.
- **Inputs:** Speed.
- **Units:** km/h or mph.
- **Variants:** Two names appear: `Speed (Avg)` and `Average speed`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Whether stoppages and standing time are in the window.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)

#### `Percentage of Max Speed`; `% of Max Speed`

The sources give these details:

- **What it measures:** How close to the athlete's own top speed the athlete ran.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the percentage of the athlete's overall maximum speed reached in practice ([live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)). Kinexon defines relative speed zones as percentages of the athlete's maximum speed ([football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/)). Coaches can set their own percentage for each zone ([max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/)). Restatement (not a Kinexon statement): speed divided by the athlete's maximum speed. Which maximum is used (season, all time, rolling): Not published.
- **Thresholds:** Not published as defaults. Kinexon's return-to-play examples use targets of 70 to 75 %, 80 to 85 %, and 88 to 92 % of max speed in stages, and at least 95 % before game activation ([ACL return-to-play post](https://kinexon-sports.com/blog/acl-injuries-in-american-football-why-data-informed-return-to-play-protocols-protect-athletes/)). These are example targets, not defaults.
- **Inputs:** Speed and the stored maximum.
- **Units:** Percent.
- **Variants:** Two names appear: `Percentage of Max Speed` and `% of Max Speed`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The stored maximum. A coach quoted on the American football page says the system updates past records when an athlete sets a new maximum speed ([sport pages](https://kinexon-sports.com/sports/volleyball/)). So a new maximum changes earlier percentages.
- **Sources:** [live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/), [football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/), [max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/), [ACL return-to-play post](https://kinexon-sports.com/blog/acl-injuries-in-american-football-why-data-informed-return-to-play-protocols-protect-athletes/), [sport pages](https://kinexon-sports.com/sports/volleyball/)

#### `Total Distance`; `Distance`; `Total Yardage`

The sources give these details:

- **What it measures:** How far the athlete moved.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the IMU brochure ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)) and the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The individualized football post uses `Total Yardage` in American football ([individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/)). The Bundesliga list names horizontal and vertical distance ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Formula: Not published. The handball IMU post says the IMU does not track positions, but says in the same post that an IMU system uses position data to calculate metrics like acceleration ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)). The two statements conflict. The LPS, GPS, and IMU post says position-based metrics can be predicted with the IMU system in some sport-specific cases ([LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/)). A study that used the Kinexon Mobile Tag calls its distance "estimated equivalent distance", the sum of estimated horizontal distances derived from velocity predicted from acceleration data ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
- **Thresholds:** None.
- **Inputs:** Position (LPS, GPS) or acceleration (IMU estimate).
- **Units:** Meters. Yards in American football ([individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/)).
- **Variants:** Three names appear: `Total Distance`, `Distance`, and `Total Yardage`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The sensor type (measured or estimated), pauses (a study operator paused LPS recording during stoppages, [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)), and the phase window.
- **Sources:** [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/), [LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)

#### `Distance per minute`; `Distance / min`

The sources give these details:

- **What it measures:** How much ground the athlete covers per minute.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): distance per minute of activity, a proxy of speed ([March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/)). Listed as a live GPS Pro metric ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Restatement (not a Kinexon statement): distance divided by minutes. Time basis: Not published.
- **Thresholds:** Not published.
- **Inputs:** Distance and time.
- **Units:** m/min (the Carton-Llorente study uses the same unit, [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)).
- **Variants:** Two names appear: `Distance per minute` and `Distance / min`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The time basis and the sensor type (see `Total Distance`).
- **Sources:** [March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)

#### `Distance In Speed Zones`

The sources give these details:

- **What it measures:** How far the athlete moved at each speed band.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Kinexon labels the zones by number (a football export uses "Speed Zones 4 to 6", [Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579)). Kinexon says coaches can set zones by position or team and change them during the season ([max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/)). A study of a Kinexon export found that the zone edges and the "high" and "very high" acceleration edges were not in the export ([Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579)). Default zone edges: Not published.
- **Thresholds:** Not published by Kinexon. Study settings (not Kinexon defaults):
  - Handball, LPS: standing under 1 m/s, walking 1 to 2, jogging 2 to 4, running 4 to 5.5, high-intensity running 5.5 to 7, sprinting over 7 m/s ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
  - Basketball, IMU: low up to 5.04 km/h, medium 5.04 to 10.8, high 10.8 to 18.72, very high over 18.72 km/h ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
  - Handball: high-speed running at 4.4 m/s or more ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)). Basketball: high intensity above 18 km/h ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
  - The FIFA test report uses velocity bands of 0 to 5, 5 to 10, 10 to 15, 15 to 20, 20 to 25, and over 25 km/h for device accuracy testing ([FIFA EPTS report](https://kinexon-sports.com/uploads/images/Blog/Kinexon_GPS_PRO_Live_2024_Report_EPTS_FIFA-Quality_Report.pdf.pdf)). That is a test band, not a Kinexon zone.
- **Inputs:** Speed and the zone table.
- **Units:** Meters.
- **Variants:** `Time In Speed Zones` and `Speed Zone Entry` use the same zones.
- **Comparison with standard methods or other vendors:** Catapult's support site lists an article on absolute and relative velocity bands that this page does not cover, so it makes no match.
- **What changes the number:** The zone edges (editable), absolute versus percent-of-max zones (see `Percentage of Max Speed` and `Speed Zone Entry`), and the speed source.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579), [max speed post](https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/), [FIFA EPTS report](https://kinexon-sports.com/uploads/images/Blog/Kinexon_GPS_PRO_Live_2024_Report_EPTS_FIFA-Quality_Report.pdf.pdf)

#### `Time In Speed Zones`

The sources give these details:

- **What it measures:** How long the athlete spent at each speed band.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)) and named as a volume metric in the volume-versus-intensity post ([volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)). It uses the same zones as `Distance In Speed Zones`. Unit: Not published.
- **Thresholds:** See `Distance In Speed Zones`.
- **Inputs:** Speed and the zone table.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** See `Distance In Speed Zones`.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)

#### `Speed Zone Entry`; `Relative Speed Zone Entries`

The sources give these details:

- **What it measures:** How often the athlete moved into a faster band.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): sorts the athlete's speed into zones based on a percentage of the athlete's maximum speed, such as walking, jogging, running, and sprinting ([football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/)). Listed as `Speed Zone Entry` in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). What counts as an entry (boundary crossing, minimum time): Not published.
- **Thresholds:** Not published.
- **Inputs:** Speed and the athlete's maximum.
- **Units:** Count.
- **Variants:** Two names appear: `Speed Zone Entry` and `Relative Speed Zone Entries`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The stored maximum (see `Percentage of Max Speed`) and the zone percentages.
- **Sources:** [football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)

#### `High-Speed Distance`; `High-Speed Yardage`

The sources give these details:

- **What it measures:** How far the athlete moved above a high-speed line.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): distance covered over a certain speed threshold ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Football pairs it with `Percentage of Max Speed` ([individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/)). The threshold: Not published.
- **Thresholds:** Not published. Study settings (not Kinexon defaults): high-speed running at 4.4 m/s or more in handball ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)); high intensity above 18 km/h in basketball ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)); sprint and very high zone above 18.72 km/h in basketball ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
- **Inputs:** Speed.
- **Units:** Meters. Yards in American football. The basketball load posts also name the metric (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))).
- **Variants:** Two names appear: `High-Speed Distance` and `High-Speed Yardage`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The threshold (absolute or percent of max) and the speed source.
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037), basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))

#### `High Intensity Runs`

The sources give these details:

- **What it measures:** Named in the Bundesliga metric list ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Definition and threshold: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)

#### `Sprints`; `Sprint`; `Number of Sprints`

The sources give these details:

- **What it measures:** How many runs the athlete made above sprint speed.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): runs over a certain speed threshold ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). GPS Pro lists `Sprint` and a live tile for the number of sprints ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Kinexon's handball case studies track sprints ([Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf), [Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf)). The speed threshold and minimum duration: Not published. Sprint Diagnostics detects sprints differently: from a standstill, not from a speed trigger ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)).
- **Thresholds:** Not published. Study setting (not a Kinexon default): a sprint was a speed of 18.72 km/h held for 1.0 s, "as dictated by the proprietary software" ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)).
- **Inputs:** Speed.
- **Units:** Count ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) reports cases per minute).
- **Variants:** Three names appear: `Sprints`, `Sprint`, and `Number of Sprints`. Football posts also name the metric ([football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/)), as does the handball IMU post ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)).
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The speed threshold, minimum duration, and the speed source. Traditional detection starts at a speed threshold and can miss the start of the acceleration phase ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)).
- **Sources:** [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf), [Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf), [Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/), [football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/), [handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)

#### `Sprint Duration`

The sources give these details:

- **What it measures:** How long sprint efforts lasted.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** The Rolling Window Analysis post names sprint durations in its summary of a peak-demand study, where they fell as the window grew longer ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)). Whether Kinexon offers it as a stand-alone metric, and its definition and unit: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The sprint rule (see `Sprints`) and the window length (see the Rolling Window Analysis outputs).
- **Sources:** [Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)

#### `Repeated Sprints`; `speed repetitions`

The sources give these details:

- **What it measures:** Whether the athlete can sprint again after a short rest.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the ability to do several sprints in quick succession with short recovery between them ([football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/)). The GPS Pro brochure lists repeated sprints and speed repetitions as advanced metrics ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The recovery limit and minimum count: Not published.
- **Thresholds:** Not published.
- **Inputs:** Sprint events.
- **Units:** Not published.
- **Variants:** Two names appear: `Repeated Sprints` and `speed repetitions`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The sprint rule (see `Sprints`) and the recovery limit.
- **Sources:** [football GPS tracker post](https://kinexon-sports.com/blog/gps-tracker-for-football-players/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)

#### `Playing Time`; `Time Played on Offense`; `Time Played on Defense`

The sources give these details:

- **What it measures:** How long the athlete was active, split by team phase.
- **Window or phase:** Split by offense and defense in the handball case study ([Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf)).
- **Calculation:** Listed in the Rhein-Neckar Loewen case study ([Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf)), and the player metrics post lists `Time` as a volume metric ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/)). How offense and defense are decided and how stoppages are handled: Not published. A study operator paused LPS recording when the game clock stopped ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
- **Thresholds:** Not published.
- **Inputs:** Time and phase tags.
- **Units:** Not published.
- **Variants:** Three names appear: `Playing Time`, `Time Played on Offense`, and `Time Played on Defense`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Phase tagging and how stoppages are treated.
- **Sources:** [Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf), [player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)

### Acceleration and deceleration metrics

#### `Acceleration`; `Deceleration` (event counts)

The sources give these details:

- **What it measures:** How many times the athlete sped up or slowed down hard enough to count.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)), in the Rhein-Neckar Loewen and Dutch case studies ([Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf), [Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf)), and as volleyball IMU metrics ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)). Kinexon says a deceleration is a stop, a slowdown before a direction change, or a rapid drop in speed over a threshold ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Kinexon also says that in an average basketball game a player makes about 10 to 20 % more accelerations than decelerations, and a larger gap held for a long time may signal injury risk ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). This is a vendor observation, not a threshold. Event detection rule: Not published.
- **Thresholds:** Not published. Study settings (not Kinexon defaults):
  - 1.5 m/s^2 with at least 0.5 s duration, "as dictated by the proprietary software" ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)).
  - High-intensity accelerations above 2 m/s^2 and decelerations below -2 m/s^2 ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Inputs:** Position-derived or IMU-derived acceleration. LPS acceleration root mean square error is about 0.2 m/s^2, cited in the Bassek study from earlier work (Hoppe 2018; Fleureau 2020; Blauberger 2021) and not measured there ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
- **Units:** Count.
- **Variants:** `Acceleration` and `Deceleration` are counted separately. The EHF EURO post also names them ([EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/)).
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match of event rules.
- **What changes the number:** The threshold and duration, smoothing, and the data source. The same movement can count as zero, one, or two events under different rules.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Rhein-Neckar Loewen case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf), [Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf), [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/), [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/), [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/), [EHF EURO 2024 post](https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/)

#### `High / very high acceleration and deceleration counts`; `High Intensity Accelerations`

The sources give these details:

- **What it measures:** Only the hardest accelerations and decelerations.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names the number of high accelerations and decelerations as an intensity metric ([volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)), and `High Intensity Accelerations` as a basketball metric that counts high-intensity activities ([basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Its Relative Analysis example uses high-intensity accelerations versus match level ([Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/)). A Kinexon GPS export contains "high" and "very high" counts with no thresholds in the data ([Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579)). Band edges: Not published.
- **Thresholds:** Not published. Study settings (not Kinexon defaults): above 2 m/s^2 ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Inputs:** Acceleration events.
- **Units:** Count.
- **Variants:** Two names appear: `High / very high acceleration and deceleration counts` and `High Intensity Accelerations`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The band edges and everything that changes the `Acceleration` and `Deceleration` event counts.
- **Sources:** [volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/), [basketball mechanical load post](https://kinexon-sports.com/blog/mechanical-load-basketball/), [Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/), [Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579), [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)

#### `Acceleration (Max)`; `Deceleration (Max)`

The sources give these details:

- **What it measures:** The hardest single acceleration or deceleration in the window.
- **Window or phase:** The window you select.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Kinexon describes the maximum as how rapidly an athlete increased velocity ([live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)) and recommends tracking maximum acceleration and deceleration in high-intensity football sessions ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)). Sprint Diagnostics report a maximum acceleration ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)). Formula, smoothing, and unit: Not published. The Wyoming football post also names maximum acceleration and deceleration ([Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/)).
- **Thresholds:** None.
- **Inputs:** Acceleration.
- **Units:** Not published.
- **Variants:** `Acceleration (Max)` and `Deceleration (Max)`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Filtering and smoothing, which strongly change a peak value, and the data source. Study processing for comparison (not a Kinexon default): a 1 Hz low-pass filter and central differences ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)).
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/), [football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/), [Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/), [Wyoming football post](https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)

#### `Acceleration/Deceleration Zones` (Low, Medium, High, Very High)

The sources give these details:

- **What it measures:** Intensity bands for acceleration and deceleration events.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** The football mechanical load post gives an example: low below 37.33, medium 37.33 to 47.17, high 47.17 to 57.5, and very high at or above 57.5, labeled yd/s^2 ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)). The post calls these an example. The unit label looks wrong, because these values are far above plausible accelerations in yd/s^2, and the label cannot be reconciled. Treat the numbers as unverified. Default band edges: Not published.
- **Thresholds:** The example values only ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)). Not a default.
- **Inputs:** Not published.
- **Units:** yd/s^2 as printed in the example. The label is doubtful, as noted above.
- **Variants:** Four bands: Low, Medium, High, and Very High.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Band edges.
- **Sources:** [football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)

### Metabolic power metrics

#### `Metabolic Power`

The sources give these details:

- **What it measures:** An estimate of energy cost per second from speed and acceleration.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)) and the soccer vest post ([soccer vest post](https://kinexon-sports.com/blog/soccer-vest/)). The model Kinexon uses: Not published. A study that computed metabolic power from Kinexon LPS position data used its own merged model of di Prampero and Osgnach with Minetti and Pavei ([Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/)). That is the authors' model, not Kinexon's.
- **Thresholds:** Not published.
- **Inputs:** Speed and acceleration. Body mass handling: Not published.
- **Units:** Not published.
- **Variants:** `Metabolic Power per Mass (Max)` and the high metabolic power distance metrics build on it. The Bundesliga post also names it ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)).
- **Comparison with standard methods or other vendors:** Catapult also has a metabolic power metric with its own settings ([Catapult metabolic power support page](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)). No source says the two models match.
- **What changes the number:** The model, body mass handling, and smoothing of speed and acceleration.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [soccer vest post](https://kinexon-sports.com/blog/soccer-vest/), [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [Catapult metabolic power support page](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)

#### `Metabolic Power per Mass (Max)`

The sources give these details:

- **What it measures:** The peak energy cost per second, per kilogram of body mass.
- **Window or phase:** The peak in the window you select (the name says Max).
- **Calculation:** Vendor definition (paraphrased): a measure of the energy spent during acceleration and deceleration ([live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)). Formula: Not published.
- **Thresholds:** Not published.
- **Inputs:** Speed, acceleration, and body mass.
- **Units:** Not published.
- **Variants:** None named. The source ties it to American football.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The model and filtering.
- **Sources:** [live GPS and recovery post](https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/)

#### `High Metabolic Power Distance` (HMPD); `HMLD`; `HMDL`; `High Metabolic Load`

The sources give these details:

- **What it measures:** How far the athlete moved while the body's energy cost was high, which counts hard accelerations and fast running together.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): the total distance covered at high energetic cost, combining speed and acceleration demands ([match day GPS post](https://kinexon-sports.com/blog/why-gps-player-performance-data-makes-soccer-training-more-effective-for-match-day/)). The GPS Pro brochure writes it as "High Metabolic Power Distance" in its metric list and as HMLD and HMDL in other places ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Stanford volleyball tracks "High Metabolic Load" in the app ([Stanford volleyball post](https://kinexon-sports.com/blog/how-stanford-volleyball-uses-micro-dose-training-to-stay-match-ready/)). The power threshold and model: Not published.
- **Thresholds:** Not published.
- **Inputs:** Metabolic power and distance.
- **Units:** Meters.
- **Variants:** Four names appear: `High Metabolic Power Distance` (HMPD), `HMLD`, `HMDL`, and `High Metabolic Load`. The Bundesliga post also names it ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)).
- **Comparison with standard methods or other vendors:** The closest Catapult metric is High Metabolic Load Distance (HMLD). Catapult sets the threshold at 25.5 W/kg by default, at team level ([Catapult metabolic power support page](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)). Its Vector Core page describes HMLD as the estimated distance at an energy expenditure above 25.5 W/kg, and adds that this equals running at a constant 5.5 m/s ([Catapult Vector Core page](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Both metrics count distance above a metabolic power cut-off, and Kinexon publishes no cut-off, so the values cannot be matched.
- **What changes the number:** The metabolic power model and the power cut-off.
- **Sources:** [match day GPS post](https://kinexon-sports.com/blog/why-gps-player-performance-data-makes-soccer-training-more-effective-for-match-day/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Stanford volleyball post](https://kinexon-sports.com/blog/how-stanford-volleyball-uses-micro-dose-training-to-stay-match-ready/), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/), [Catapult metabolic power support page](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings), [Catapult Vector Core page](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)

#### `High Speed And Acceleration Distance`; `High speed and acceleration time`

The sources give these details:

- **What it measures:** Distance (or time) in which fast running and hard acceleration are combined.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** The distance form is listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)), and the time form in the Bundesliga post ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Definition and thresholds: Not published.
- **Thresholds:** Not published.
- **Inputs:** Speed and acceleration.
- **Units:** Not published.
- **Variants:** A distance form and a time form.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)

### Heart rate metrics

#### `Heart Rate (Min, Max, Avg)`

The sources give these details:

- **What it measures:** The athlete's heart rate during the session.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** The PERFORM IMU has integrated ECG-derived heart rate measurement and works with Polar and Suunto devices ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). GPS Pro uses a Polar OH1 or H10 sensor ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The Bundesliga post lists average, impulse, and recovery values ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Processing: Not published.
- **Thresholds:** Not published.
- **Inputs:** An ECG or optical heart rate sensor.
- **Units:** Not published.
- **Variants:** Minimum, maximum, and average values.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The sensor type and fit.
- **Sources:** [IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)

#### `Time In Heart Rate Zones`

The sources give these details:

- **What it measures:** How long the athlete spent in each heart rate band.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Zone edges and whether they use percent of maximum heart rate: Not published.
- **Thresholds:** Not published.
- **Inputs:** Heart rate and the zone table.
- **Units:** Time. The unit is not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Maximum heart rate value and the zone table.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)

#### `Heart Rate Recoveries`; `heart rate impulse`

The sources give these details:

- **What it measures:** How fast heart rate falls after effort (recoveries), and a cumulative heart rate dose (impulse).
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** `Heart Rate Recoveries` is listed in the GPS Pro brochure ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). `heart rate impulse` and recovery are in the Bundesliga post ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)). Definitions and windows: Not published.
- **Thresholds:** Not published.
- **Inputs:** Heart rate.
- **Units:** Not published.
- **Variants:** Two names appear: `Heart Rate Recoveries` and `heart rate impulse`.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Not published.
- **Sources:** [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)

#### `TRIMP`

The sources give these details:

- **What it measures:** An estimate of how hard the session was on the body, from heart rate.
- **Window or phase:** Practice, drills, and matches ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)).
- **Calculation:** Vendor definition (paraphrased): a player's estimated exhaustion level in practice, drills, and matches ([volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)). The GPS Pro brochure lists it under internal load ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). Which TRIMP formula: Not published.
- **Thresholds:** Not published.
- **Inputs:** Heart rate and time.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Maximum and resting heart rate settings and the formula version.
- **Sources:** [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)

#### `Percentage of maximum heart rate`

The sources give these details:

- **What it measures:** Heart rate relative to the athlete's maximum.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Kinexon names it as an example of an intensity metric in handball ([handball load post](https://kinexon-sports.com/blog/handball-performance-tracking-load-monitoring/)). How the maximum is set: Not published.
- **Thresholds:** Not published.
- **Inputs:** Heart rate and maximum heart rate.
- **Units:** Percent.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The stored maximum.
- **Sources:** [handball load post](https://kinexon-sports.com/blog/handball-performance-tracking-load-monitoring/)

### Distribution metric

#### `High vs. Low Intensity Distribution`

The sources give these details:

- **What it measures:** How much of the athlete's work was high-intensity and how much was easy.
- **Window or phase:** Not stated in the sources reviewed.
- **Calculation:** Vendor definition (paraphrased): shows whether athletes get a good balance of game-like intensity and controlled recovery work. The source is a Columbia basketball example that uses PERFORM IMU metrics (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))). How the bands are set: Not published.
- **Thresholds:** Not published.
- **Inputs:** Not published.
- **Units:** Not published.
- **Variants:** None named.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The band definitions.
- **Sources:** basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))

### Sports App outputs

These blocks cover widgets and diagnostics that the Kinexon Sports App computes or shows. They are not single sensor metrics.

#### `Sprint Diagnostic` outputs

The sources give these details:

- **What it measures:** A repeatable sprint test run on the field, with no timing gates. Outputs: time splits, average speed, maximum speed, maximum acceleration, and velocity and acceleration curves.
- **Window or phase:** One sprint over a set distance of 20, 30, 40, or 60 m, live and after the session ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)).
- **Calculation:** Vendor description (paraphrased): athletes are put in a diagnostic group in the app. They line up at a start line, hold still for at least 2 seconds, and sprint a set distance of 20, 30, 40, or 60 m. The system detects and logs the event automatically. Outputs listed: time splits every 5 m or 10 m, average speed, maximum speed, maximum acceleration, and instantaneous velocity or acceleration curves ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)). The results appear in a `DIAGNOSTICS` section next to `STATISTICS`, `POST`, and `DEVELOP` ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)). It works with LPS or GNSS ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)). GPS Pro lists sprint diagnostics with 5 m and 10 m splits, max speed, and change of direction (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). Filtering, units, and the start detection beyond the 2-second hold: Not published. Kinexon says force-velocity profiling will come in a later update ([Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/)).
- **Thresholds:** Not published beyond the fixed distances and the 2-second hold.
- **Inputs:** LPS or GNSS speed.
- **Units:** Time splits in seconds. Speed and acceleration units: Not published.
- **Variants:** Splits every 5 m or 10 m, and four test distances.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The speed source and its filtering, the start detection, and whether the athlete was truly still at the start.
- **Sources:** [Sprint Diagnostics post](https://kinexon-sports.com/blog/on-field-sprint-diagnostics/), product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))

#### `Rolling Window Analysis` outputs

The sources give these details:

- **What it measures:** The hardest stretch of play, for example the most demanding 30 seconds. Outputs: number of windows, number of high-demand windows, average and maximum window value, and timestamp of peak intensity.
- **Window or phase:** A window length that you set. The example is 30 s, shifted every 2 s ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)).
- **Calculation:** Vendor description (paraphrased): you set a window length (the example is 30 s), a window shift (example: every 2 s), and a key value that defines a high-demand window (example: 70 m in 30 s), plus the range to analyze. The outputs are the total number of windows, the number of high-demand windows, the average and maximum window value, and the time of peak intensity, exportable to CSV or Excel ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)). The post cites distance, accelerations, decelerations, and sprint durations in its study summary ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)). The full list of metrics the widget accepts: Not published. It works with LPS, IMU, and GPS ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)). Kinexon's guidance on sustaining intensity adds that the tool can find the most demanding one-minute periods, peak AAL accumulation, and maximum acceleration density ([game intensity post](https://kinexon-sports.com/blog/sustaining-game-intensity-athlete-performance-tracking/)). The example numbers are examples, not defaults.
- **Thresholds:** The key value is user-set. Study settings for comparison (not Kinexon defaults, [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)): rolling averages over 10, 30, 60, and 120 s with a 1 s step. Peak demand (PD) is the maximum value. High-intensity period (HIP) is 80 to 90 % of PD, and very high-intensity period (VHIP) is above 90 % of PD. The study used 20 Hz position and 100 Hz accelerometer data from Kinexon, and the data came from the Kinexon API.
- **Inputs:** Any supported metric.
- **Units:** The unit follows the metric. The Irid study reports distance in m/min ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Variants:** Window length, shift, and key value are all user-set.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** Window length (shorter windows give higher peak values; in the Irid study, male relative distance fell from 251.34 m/min at 10 s to 113.61 m/min at 120 s), the shift, whether the clock resets at breaks (the Irid study reset at each quarter), and the metric chosen ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)).
- **Sources:** [Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/), [game intensity post](https://kinexon-sports.com/blog/sustaining-game-intensity-athlete-performance-tracking/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)

#### `Relative Analysis` values

The sources give these details:

- **What it measures:** How an athlete's number compares with a target you choose. Outputs: relative value, target value, and playing time.
- **Window or phase:** A time range that you choose, by session type or phase ([Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/)).
- **Calculation:** Vendor description (paraphrased): the relative value is the metric divided by the target, so 1.2 means 20 % above target. Targets can be typed in or calculated from history. You can choose the time range, the players that feed the target, session type or phase, a minimum observation time, and a multiplier such as 1.1 times the match average. You can set an alert threshold such as 90 %. The export holds relative values, target values, and playing time per session, in CSV or Excel ([Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/)). Kinexon announced it for Sports App version 12.3.
- **Thresholds:** User-set. The default target source: Not published.
- **Inputs:** Any metric and a target.
- **Units:** A ratio (1.2 = 20 % above target).
- **Variants:** Targets can be typed in or calculated from history.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** The target definition (team, individual, match, practice), the observation time threshold, and the multiplier.
- **Sources:** [Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/)

#### `Phase Index` values

The sources give these details:

- **What it measures:** What a typical and a high-end drill looks like for each drill type, so coaches can plan practices. Outputs: phase type, metrics normative range, and record count.
- **Window or phase:** One record is one player in one phase ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)).
- **Calculation:** Vendor description (paraphrased): a table by phase type that shows a typical and a high-end range for chosen metrics and a record count. One record is one player in one phase, so 20 players in one warm-up gives 20 records, and two such warm-ups give 40. `POST` shows one session, and `DEVELOP` shows history with a minimum phase duration filter. You can export tables or all data ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)). A Kinexon use case names this tool the Phase Index (basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/))). The Phase Index widget guide also uses the name Drill Index for the insights it gives ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)). How the normative range is calculated (for example, which percentiles): Not published. The Dutch handball federation splits history into quartiles for light (lowest 25 %), medium (25 to 75 %), and heavy (top 25 %) load. That is the federation's method, not a Kinexon default ([Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf)).
- **Thresholds:** The minimum phase duration is user-set. Defaults: Not published.
- **Inputs:** Phase labels you assign and any metric.
- **Units:** Counts and metric units.
- **Variants:** The guide uses both Phase Index and Drill Index.
- **Comparison with standard methods or other vendors:** No source supports a cross-vendor match.
- **What changes the number:** How finely you name phase types (Kinexon advises one type per drill, such as "3 on 2", not a generic "Drill"), the minimum duration, and the date range ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)).
- **Sources:** [Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/), basketball load posts ([load management post](https://kinexon-sports.com/blog/basketball-performance-data-load-management/), [in-season post](https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/), [drill intensity post](https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/)), [Dutch handball case study](https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf)

### Position export

#### Position export columns

The sources give these details:

- **What it measures:** These are position data columns, not performance metrics. The open-source `floodlight` Python package reads Kinexon position CSV files and looks for these exact column names in the header row (floodlight Kinexon parser ([documentation](https://floodlight.readthedocs.io/en/latest/modules/io/kinexon.html), [source](https://github.com/floodlight-sports/floodlight/blob/master/floodlight/io/kinexon.py))). Kinexon does not publish a column list. The delimiter defaults to a comma.
- **Window or phase:** One row per time stamp.
- **Calculation:** Not applicable. These are raw columns. Product: not stated by the source.
- **Thresholds:** None.
- **Inputs:** Position data.
- **Units:** Milliseconds for `ts in ms`, meters for `x in m` and `y in m`.
- **Variants:** The parser accepts these columns:

  | CSV column | `floodlight` field | Required | Note |
  |---|---|---|---|
  | `ts in ms` | `time` | Yes | Time stamp in milliseconds, per the column name |
  | `sensor id` | `sensor_id` | No | Sensor identifier |
  | `mapped id` | `mapped_id` | No | Identifier mapped to a player |
  | `full name` | `name` | No | Player name |
  | `number` | `number` | No | Shirt number |
  | `group id` | `group_id` | No | Numeric group, used when no group name exists |
  | `group name` | `group_name` | No | Group name, preferred over `group id` |
  | `x in m` | `x_coord` | Yes | Meters |
  | `y in m` | `y_coord` | Yes | Meters |

  The parser picks a player identifier in this order: name, mapped id, sensor id, number. If the file has no group column, it uses a default group `0`. It estimates the frame rate from the smallest time step between frames. It reads no other columns. The pattern `quantity in unit` suggests how other columns are named, but no public list of them exists.
- **Comparison with standard methods or other vendors:** Not applicable.
- **What changes the number:** Not applicable.
- **Sources:** floodlight Kinexon parser ([documentation](https://floodlight.readthedocs.io/en/latest/modules/io/kinexon.html), [source](https://github.com/floodlight-sports/floodlight/blob/master/floodlight/io/kinexon.py))

## Study settings (not Kinexon defaults)

These are settings that researchers reported. Where a study says the software set a value, the table notes it, but the studies are not Kinexon documentation. Do not copy these as Kinexon defaults.

| Setting | Value | Study | Device and sport |
|---|---|---|---|
| AAL formula | `sqrt[(dAc1)^2 + (dAc2)^2 + (dAc3)^2 / 100]` | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Kinexon Mobile Tag, 100 Hz, basketball |
| AAL reliability (cited by the study from earlier work) | ICC 0.94 to 0.97, CV 3.6 to 9.4 % | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Basketball |
| Sprint event | 18.72 km/h held for at least 1.0 s | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Basketball |
| Jump event | At least 0.4 s dwell time | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Basketball |
| Exertion event | At least 4.5 G held for 1.0 s | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Basketball |
| Event smoothing | 100 Hz data smoothed to 10 Hz with a Kalman filter | [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Basketball |
| Acceleration and deceleration events | At least 1.5 m/s^2 for at least 0.5 s | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/) | IMU at 20 Hz, NCAA basketball |
| Jump event | At least 0.3 s airtime | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/) | IMU at 20 Hz, NCAA basketball |
| Jump Load | Body mass x 9.8 x jump height (m), summed | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/) | IMU at 20 Hz, NCAA basketball |
| Jump Load | `m x g x h`, g = 9.81 m/s^2 | [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037) | PERFORM IMU, 3x3 basketball |
| Distance zones | Up to 5.04, 5.04 to 10.8, 10.8 to 18.72, over 18.72 km/h | [Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037) (the study cites its reference 30 for the zones) | PERFORM IMU, 3x3 basketball |
| High-speed running | 4.4 m/s or more | [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/) | LPS tag, handball, 5-minute windows |
| High-intensity accelerations and decelerations | Above 2 m/s^2 and below -2 m/s^2 | [Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/) | Handball ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/)), basketball ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)) |
| High intensity running | Above 18 km/h | [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/) | LPS, youth basketball |
| High-intensity jump | Above 0.40 m | [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/) | Youth basketball |
| High-intensity change of direction | Above 90 degrees with deceleration below -2 m/s^2 | [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/) | Youth basketball |
| Speed zones, six | Standing under 1; walking 1 to 2; jogging 2 to 4; running 4 to 5.5; high-intensity running 5.5 to 7; sprinting over 7 m/s | [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/) | LPS at 20 Hz, handball |
| Position filter | 4th-order Butterworth low-pass at 1 Hz, then central differences for speed and acceleration | [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/) | LPS at 20 Hz, handball |
| Rolling windows | 10, 30, 60, and 120 s, 1 s step, reset each quarter; HIP 80 to 90 % of peak, VHIP above 90 % | [Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/) | LPS at 20 Hz plus accelerometer at 100 Hz, basketball |
| Sensor positions | Holster "near the right posterior superior iliac spine" ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)); between shoulder blades ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/), [Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949)); posterior iliac crest ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)); the Frontiers study says the manufacturer recommends placement "above the right posterior superior iliac spine" (that study used the sacrum instead, [2026 change-of-direction study](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1665797/full)) | as listed | Various |
| Position accuracy | About 0.1 m, 0.15 m/s, 0.2 m/s^2 (RMSE) for position, speed, acceleration | Cited in [Bassek 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/) from earlier work (Hoppe 2018; Fleureau 2020; Blauberger 2021) | LPS at 20 Hz |
| Typical error of IMU system | 2.5 % (+/- 1.5 %), cited from earlier work | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/) | Team-sport movements |
| Exported variable count | 109 external load variables, including event counts, acceleration zones 1 to 4, and time in speed zones, in 2D and 3D | [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/) | Kinexon companion software, IMU |

The Pantazis study (3x3 basketball) confirms the `Accumulated Acceleration Load` and `Mechanical Load` values given in the metric blocks, the speed zones above, the `Jump Load` formula, the sensor position at the posterior iliac crest, and an export of raw tri-axial accelerometer data as CSV at 100 Hz ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).

## Export routes

Kinexon describes these ways to get data out:

- Kinexon says coaches and analysts can get all statistics and raw data as CSV files or through a REST API ([sport pages](https://kinexon-sports.com/sports/volleyball/), sport pages). The PERFORM LPS page mentions an open API (product pages ([PERFORM IMU page](https://kinexon-sports.com/products/perform-imu/), [PERFORM LPS page](https://kinexon-sports.com/products/perform-lps/), [PERFORM GPS Pro page](https://kinexon-sports.com/products/perform-gps-pro/))). The GPS Pro brochure lists individual PDF, Excel, and raw-data exports and API connectivity to athlete management systems ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)). The Bundesliga post says the same for the Bundesliga offer ([Bundesliga clubs post](https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/)).
- Kinexon lists third-party integrations: Teamworks, GPSDataViz, Edge10, Firstbeat, and Polar ([sport pages](https://kinexon-sports.com/sports/volleyball/)). The GPS Pro brochure also lists Playsight, Pixellot, Keemotion, Game-On, Sportscode, Dataschema, Strive, and the DFL Data Hub ([GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf)).
- Widgets export CSV or Excel files: Rolling Window Analysis ([Rolling Window Analysis post](https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/)), Relative Analysis ([Relative Analysis post](https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/)), and Phase Index tables ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)).
- Published studies used the Kinexon API for position, speed, acceleration, and jump metrics ([Irid 2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/)) and exported raw tri-axial accelerometer data as CSV files at 100 Hz ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)). A football study received an export with total distance, distance per minute, distance in Speed Zones 4 to 6, maximum speed, high and very high acceleration counts, high and very high deceleration counts, and changes of direction, with no thresholds ([Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579)). Those are the authors' descriptions, not column headers.
- Public API documentation, endpoints, authentication, and the column headers of performance exports: Not published.

## Conflicts in the vendor's own sources

Kinexon's public sources and the studies that used Kinexon systems disagree in these places. This page does not resolve them.

- **Metric counts.** Kinexon sources give counts from 50 to more than 300. See the table of count claims earlier on this page. The public sources name far fewer distinct metrics than any of these totals.
- **Position data in the IMU.** The handball IMU post says the IMU does not track positions but only movements. The same post says an IMU system uses position data to calculate metrics like acceleration ([handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)). The LPS, GPS, and IMU post says only that position-based metrics can be predicted with the IMU system in some sport-specific cases ([LPS, GPS, and IMU post](https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/)). This affects `Max. Speed` and `Total Distance` on the IMU.
- **`Exertions`.** The sources describe the metric a little differently by sport and product, and Kinexon does not reconcile them ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [March Madness post](https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/), [individualized football data post](https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/), [volleyball IMU post](https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/)).
- **`Changes of Orientation` and `Change Of Direction`.** Both names appear in Kinexon text, and their relation is not published ([IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [GPS Pro brochure](https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf), [handball IMU post](https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/)).
- **Volleyball positions post.** It describes `Jump Height` as standing reach versus peak reach, and `Impact` as swing force measured through ball velocity. Neither fits a body-worn sensor, so this page treats the text as unreliable ([volleyball positions post](https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/)).
- **`Physio Load`.** Kinexon names it in text, and a Kinexon video on how to calculate it exists. The video was not readable for this page ([player metrics post](https://kinexon-sports.com/blog/data-analytics-in-sports/), [volume versus intensity post](https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/)).
- **Phase Index and Drill Index.** The Phase Index widget guide uses both names for the same insights ([Phase Index guide](https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/)).
- **`Acceleration/Deceleration Zones` unit.** The example band values are labeled yd/s^2, which is far above plausible accelerations in those units ([football mechanical load post](https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/)).
- **`Jump Load` unit.** The Stone results table gives J, and the Stone text says arbitrary units ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)). The two studies that give the formula write g as 9.8 m/s (missing the square, [Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)) and 9.81 m/s^2 ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)).
- **AAL formula.** The Koyama study prints the division by 100 in a way that does not show whether it sits inside or outside the square root ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)). A review says the 100 is most likely a scaling factor but may be a residual of the sampling rate ([2025 acceleration-load review](https://www.mdpi.com/1424-8220/25/9/2764)).
- **Sampling rate for IMU load studies.** The Stone and women's basketball studies report 20 Hz ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/), [women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/)). The Koyama study reports 100 Hz ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)). Whether Kinexon values at different rates agree: Not published.
- **Sensor placement.** Studies place the sensor at the posterior iliac crest ([Pantazis 2026 study](https://www.mdpi.com/2076-3417/16/4/2037)), between the shoulder blades ([Carton-Llorente 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/), [women's basketball study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/), [Grob 2025 study](https://journal.iusca.org/index.php/Journal/article/download/359/478/4949)), in a holster near the right posterior superior iliac spine ([Koyama 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/)), or at the sacrum ([2026 change-of-direction study](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1665797/full)). The Frontiers study says the manufacturer recommends a place above the right posterior superior iliac spine ([2026 change-of-direction study](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1665797/full)).

## Not published

Kinexon publishes no formula for any metric, no default thresholds, no public API reference, and no export column list beyond the position columns that the open-source `floodlight` parser reads. These details are also not published:

- Public API documentation, endpoints, authentication, and the column headers of performance exports.
- Default speed zone edges, acceleration and deceleration band edges, jump height and airtime thresholds, and the exertion and sprint rules.
- The weights and intensity bands behind `Accel Load`, `Decel Load`, and `Mechanical Load`.
- Whether a noise floor is applied to AAL, and whether AAL values from different sensor placements or sampling rates agree.
- The jump height estimation formula, and the filtering that detects takeoff and landing impacts.
- The weights and units of `Physio Load`.
- The metabolic power model, the body mass handling, and the power cut-off for `High Metabolic Power Distance`.
- Which maximum speed and which maximum heart rate Kinexon uses, and how the stored values update.
- The default target source for `Relative Analysis` and the way `Phase Index` calculates its normative range.
- The full list of metrics the `Rolling Window Analysis` widget accepts.
- Filtering, units, and start detection beyond the 2-second hold for `Sprint Diagnostic` outputs.
- Any public product page, brochure, or metric list for KINEXON ONE, and any metric list for KINEXON POST. The sources name POST only as the Sports App view that shows one practice or match after it ends.
- Anchor range for the IMU.

These 18 metrics are name-only in public sources, with no Kinexon definition or calculation: `Load per Minute`, `Total Load`, `Max Jump Height Ratio`, `High Intensity Jump to Total Jump Ratio`, `landing load`, `vertical efforts`, `jump volume`, `Impacts`, `High Intensity Exertions`, `Anaerobic distance time`, `movement density`, `Changes of Orientation`, `High Intensity Runs`, `Sprint Duration`, `High Speed And Acceleration Distance`, `Time In Heart Rate Zones`, `Heart Rate Recoveries`, and `Percentage of maximum heart rate`.

Every other metric block contains at least one "Not published" detail. The position export block is the one exception, because the `floodlight` parser documents its columns.

Kinexon gates much of its educational material behind forms, so this page does not use it:

- No Kinexon academy, learning hub, knowledge base, glossary, white paper, or written webinar summary exists as a public metric reference on kinexon-sports.com. The industrial site kinexon.com has no athlete metric content.
- All 49 landing pages on hs.kinexon.com for guides and webinar recordings show a form and 19 to 56 words of text. They include guides on tracking load with AAL, handball metrics, mechanical load in American football, American football data, the volleyball IMU, the GPS Pro app report, the demand planners for men and women, and microdosing and return to play.
- The PERFORM LPS brochure, the basketball and handball IMU brochures, and the case studies for Texas A&M, Stanford, SD Eibar, the German Handball Federation, Rhein-Neckar Loewen, and the Dutch team have landing pages that sit behind forms. The two handball case studies are also open PDFs, and this page cites them.
- The 37 listed webinar recordings are video or form-gated. Three are on YouTube.
- The three Sprint Session videos (one covers how to calculate physio load), the podcast audio, and the video of the 2026 Basketball Coaching and Performance Summit talk on athlete monitoring have no written text.
- A search result described a KINEXON Cloud Uploader tool that uploads GPS data to create post data in the app. Its Microsoft Store page has no readable text, so this page does not rely on it.
- A third-party page (sportsfirst.net) describes a Kinexon API in marketing terms and gives no technical details. This page does not use it.

Open public material on kinexon-sports.com and hs.kinexon.com includes:

- The product pages for PERFORM IMU, LPS, and GPS Pro, the sport pages for basketball, handball, football, American football, hockey, and volleyball, and the technology pages. The ice hockey page lives at `/sports/hockey/`.
- The blog. Its sitemap lists 222 posts, and this page cites about 40 of them.
- The PDFs that open without a form: the IMU volleyball brochure, the GPS Pro football brochure, and the two handball case studies. The reference list of the Zecirovic study led to the GPS Pro brochure URL ([Zecirovic 2026 study](https://journal.aesasport.com/index.php/aesa/article/view/579)).
- The Sports Performance Training Guides page (22 guides, all hosted behind forms), the Webinars and Events page (about 37 entries), the Sprint Sessions page (three videos of 1 to 2 minutes), and the podcast page (links to audio, no written summaries).

## Worked example: Jump Load in Python

This script runs the formula from the Stone study ([Stone 2022 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/)): body mass x 9.8 x jump height in meters, summed over jumps. It is a restatement of the published study formula, not Kinexon code. The jump heights are made-up test values. The output below is the unchanged output of running the script with `python3`.

Code:

```python
"""Jump Load = sum over jumps of (body mass x g x jump height).

Formula source: Stone et al. 2022, Front. Sports Act. Living 4:795897
("body mass by the gravity constant (9.8 m/s) and the jump height in meters
for each jump event ... all jump loads were summated").
This script restates that formula. It is not Kinexon code.
"""

G_STONE = 9.8      # value written in Stone et al. 2022
G_PANTAZIS = 9.81  # value written in Pantazis et al. 2026 (JL = m x g x h)


def jump_load_joules(body_mass_kg, jump_heights_m, g=G_STONE):
    """Return (per_jump_loads_J, total_J) for one session."""
    per_jump = [body_mass_kg * g * h for h in jump_heights_m]
    return per_jump, sum(per_jump)


body_mass_kg = 85.0
jump_heights_m = [0.42, 0.47, 0.38, 0.55, 0.44, 0.40, 0.51, 0.36]

per_jump, total_j = jump_load_joules(body_mass_kg, jump_heights_m)
_, total_j_981 = jump_load_joules(body_mass_kg, jump_heights_m, g=G_PANTAZIS)

print(f"body mass: {body_mass_kg:.1f} kg")
print(f"jumps: {len(jump_heights_m)}")
for i, (h, load) in enumerate(zip(jump_heights_m, per_jump), start=1):
    print(f"  jump {i}: height {h:.2f} m -> {load:.1f} J")
print(f"Jump Load, g = {G_STONE}: {total_j:.1f} J")
print(f"Jump Load per kilogram, g = {G_STONE}: {total_j / body_mass_kg:.2f} J/kg")
print(f"Jump Load, g = {G_PANTAZIS}: {total_j_981:.1f} J")
print(f"Difference between the two g values: {total_j_981 - total_j:.2f} J "
      f"({(total_j_981 / total_j - 1) * 100:.2f} %)")

# Same session, different body mass: Jump Load scales with mass.
for mass in (70.0, 85.0, 100.0):
    _, load = jump_load_joules(mass, jump_heights_m)
    print(f"body mass {mass:.0f} kg -> Jump Load {load:.1f} J ({load / mass:.2f} J/kg)")
```

Output:

```text
body mass: 85.0 kg
jumps: 8
  jump 1: height 0.42 m -> 349.9 J
  jump 2: height 0.47 m -> 391.5 J
  jump 3: height 0.38 m -> 316.5 J
  jump 4: height 0.55 m -> 458.2 J
  jump 5: height 0.44 m -> 366.5 J
  jump 6: height 0.40 m -> 333.2 J
  jump 7: height 0.51 m -> 424.8 J
  jump 8: height 0.36 m -> 299.9 J
Jump Load, g = 9.8: 2940.5 J
Jump Load per kilogram, g = 9.8: 34.59 J/kg
Jump Load, g = 9.81: 2943.5 J
Difference between the two g values: 3.00 J (0.10 %)
body mass 70 kg -> Jump Load 2421.6 J (34.59 J/kg)
body mass 85 kg -> Jump Load 2940.5 J (34.59 J/kg)
body mass 100 kg -> Jump Load 3459.4 J (34.59 J/kg)
```

Use this list to read the output:

- Each jump contributes `body mass x g x height` in joules, and the session value is the sum.
- The two values of g (9.8 and 9.81) change the total by the amount printed in the "Difference" line.
- `Jump Load per kilogram` is the same for every body mass in this example, because the heights do not change. Kinexon does not publish whether its per-kilogram value matches this simple division.

## Sources

The page uses these Kinexon sources. Kinexon's sports site is kinexon-sports.com, and Kinexon's industrial site kinexon.com has no athlete metric content:

- Kinexon PERFORM IMU brochure, volleyball (PDF): <https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf>, accessed 2026-10-02.
- Kinexon PERFORM GPS Pro brochure, football (PDF): <https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf>, accessed 2026-10-02.
- Kinexon blog, "Tracking the Top Player Metrics in Sports": <https://kinexon-sports.com/blog/data-analytics-in-sports/>, accessed 2026-10-02.
- Kinexon blog, mechanical load in basketball: <https://kinexon-sports.com/blog/mechanical-load-basketball/>, accessed 2026-10-02.
- Kinexon blog, why track acceleration: <https://kinexon-sports.com/blog/athletic-performance-why-track-acceleration/>, accessed 2026-10-02.
- Kinexon blog, Rolling Window Analysis: <https://kinexon-sports.com/blog/introducing-rolling-window-analysis-capturing-the-most-demanding-scenarios-of-the-game/>, accessed 2026-10-02.
- Kinexon blog, volume versus intensity: <https://kinexon-sports.com/blog/how-to-measure-player-metrics-volume-vs-intensity/>, accessed 2026-10-02.
- Kinexon blog, March Madness load metrics: <https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/>, accessed 2026-10-02.
- Kinexon blog, individualized football performance data: <https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/>, accessed 2026-10-02.
- Kinexon blog, GPS data for match day (HMPD): <https://kinexon-sports.com/blog/why-gps-player-performance-data-makes-soccer-training-more-effective-for-match-day/>, accessed 2026-10-02.
- Kinexon blog, live GPS data and recovery devices: <https://kinexon-sports.com/blog/combining-live-data-from-football-gps-tracker-and-recovery-devices/>, accessed 2026-10-02.
- Kinexon blog, data from a football GPS tracker: <https://kinexon-sports.com/blog/gps-tracker-for-football-players/>, accessed 2026-10-02.
- Kinexon blog, German Bundesliga clubs: <https://kinexon-sports.com/blog/how-german-bundesliga-clubs-benefit-from-player-tracking/>, accessed 2026-10-02.
- Kinexon blog, jumper's knee: <https://kinexon-sports.com/blog/prevention-jumpers-knee/>, accessed 2026-10-02.
- Kinexon blog, Sprint Diagnostics: <https://kinexon-sports.com/blog/on-field-sprint-diagnostics/>, accessed 2026-10-02.
- Kinexon blog, Phase Index widget guide: <https://kinexon-sports.com/blog/kinexon-sports-app-guide-phase-index-widget/>, accessed 2026-10-02.
- Kinexon blog, Relative Analysis widget: <https://kinexon-sports.com/blog/metric-standardization-relative-analysis-introducing-an-easy-way-to-contextualize-athlete-performance/>, accessed 2026-10-02.
- Kinexon blog, volleyball needs more than jump data: <https://kinexon-sports.com/blog/volleyball-coaches-more-than-jump-data/>, accessed 2026-10-02.
- Kinexon blog, volleyball metrics by position (generic text): <https://kinexon-sports.com/blog/which-volleyball-metrics-matter-most-to-each-position/>, accessed 2026-10-02.
- Kinexon blog, handball load monitoring: <https://kinexon-sports.com/blog/handball-performance-tracking-load-monitoring/>, accessed 2026-10-02.
- Kinexon blog, mechanical load in football: <https://kinexon-sports.com/blog/coaches-monitor-mechanical-loading/>, accessed 2026-10-02.
- Kinexon blog, IMU in volleyball (names the POST and DEVELOP views): <https://kinexon-sports.com/blog/5-take-aways-why-performance-tracking-with-imu-is-a-game-changer-in-volleyball/>, accessed 2026-10-02.
- Kinexon blog, soccer vest: <https://kinexon-sports.com/blog/soccer-vest/>, accessed 2026-10-02.
- Kinexon blog, LPS, GPS, and IMU compared: <https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/>, accessed 2026-10-02.
- Kinexon blog, sustaining game intensity: <https://kinexon-sports.com/blog/sustaining-game-intensity-athlete-performance-tracking/>, accessed 2026-10-02.
- Kinexon blogs, Xavier, Columbia, and drill intensity in basketball: load management post: <https://kinexon-sports.com/blog/basketball-performance-data-load-management/>, in-season post: <https://kinexon-sports.com/blog/basketball-in-season-load-management-performance-data/>, drill intensity post: <https://kinexon-sports.com/blog/basketball-drill-intensity-weekly-load-targets/>, accessed 2026-10-02.
- Kinexon blog, ACL return to play in American football: <https://kinexon-sports.com/blog/acl-injuries-in-american-football-why-data-informed-return-to-play-protocols-protect-athletes/>, accessed 2026-10-02.
- Kinexon blog, NHL practice and game data: <https://kinexon-sports.com/blog/bridging-the-gap-how-nhl-teams-align-practice-and-game-data-using-kinexon-perform/>, accessed 2026-10-02.
- Kinexon blog, improving max speed: <https://kinexon-sports.com/blog/how-sports-performance-tracking-technology-improves-speed/>, accessed 2026-10-02.
- Kinexon blog, University of Wyoming football: <https://kinexon-sports.com/blog/kinexon-football-analytics-wyoming/>, accessed 2026-10-02.
- Kinexon blog, EHF EURO 2024 data: <https://kinexon-sports.com/blog/behind-the-scenes-how-the-ehf-uses-sports-data-at-handball-euro-2024/>, accessed 2026-10-02.
- Kinexon case study, Rhein-Neckar Loewen (PDF): <https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230613_Case_Study_Rhein_Neckar_L%C3%B6wen_EN.pdf>, accessed 2026-10-02.
- Kinexon case study, Netherlands women's handball (PDF): <https://hs.kinexon.com/hubfs/SPO-Handball-Collaterals/230615_Case_Study_Netherlands_Womens_National_Handball_Team_EN.pdf>, accessed 2026-10-02.
- Kinexon product pages: PERFORM IMU, PERFORM LPS, PERFORM GPS Pro: PERFORM IMU page: <https://kinexon-sports.com/products/perform-imu/>, PERFORM LPS page: <https://kinexon-sports.com/products/perform-lps/>, PERFORM GPS Pro page: <https://kinexon-sports.com/products/perform-gps-pro/>, accessed 2026-10-02.
- Kinexon sport pages (basketball, handball, football, American football, hockey, volleyball), same path pattern for each sport: <https://kinexon-sports.com/sports/volleyball/>, accessed 2026-10-02.
- Kinexon press release, PERFORM GPS Pro launch: <https://kinexon-sports.com/pr/kinexon-launches-new-gps-based-player-tracking-system/>, accessed 2026-10-02.
- Kinexon blog, Stanford volleyball micro-dose training: <https://kinexon-sports.com/blog/how-stanford-volleyball-uses-micro-dose-training-to-stay-match-ready/>, accessed 2026-10-02.
- Kinexon blog, handball positions and metabolic power: <https://kinexon-sports.com/blog/which-handball-position-covers-the-most-ground/>, accessed 2026-10-02.
- Kinexon blog, "From Court to Code" (IMU modes and exports): <https://kinexon-sports.com/blog/from-court-to-code-the-analytics-behind-athletic-success/>, accessed 2026-10-02.
- Kinexon blog, what an IMU tracks in handball: <https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/>, accessed 2026-10-02.
- Kinexon blog, Arizona State volleyball jump count: <https://kinexon-sports.com/blog/arizona-state-womens-volleyballjump-count-performance-data/>, accessed 2026-10-02.
- Kinexon blog, GPS Pro player tracking system (older post): <https://kinexon-sports.com/blog/revolutionary-football-player-tracking-system-how-kinexon-perform-gps-pro-is-changing-the-game/>, accessed 2026-10-02.
- Kinexon sports data analytics page: <https://kinexon-sports.com/technology/sports-data-analytics/>, accessed 2026-10-02.
- FIFA EPTS test report, Kinexon GPS PRO (Live), 2024 (device accuracy, not metrics): <https://kinexon-sports.com/uploads/images/Blog/Kinexon_GPS_PRO_Live_2024_Report_EPTS_FIFA-Quality_Report.pdf.pdf>, accessed 2026-10-02.

The page uses these studies and other sources:

- Stone et al. 2022, Front Sports Act Living 4:795897 (NCAA men's basketball, IMU at 20 Hz, 109 exported variables): <https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/>, accessed 2026-10-02.
- Koyama et al. 2023, Biol Sport (Kinexon Mobile Tag at 100 Hz; AAL formula): <https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/>, accessed 2026-10-02.
- Carton-Llorente et al. 2023, Biol Sport 40(4) (handball LPS, worst-case scenarios): <https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589/>, accessed 2026-10-02.
- Bassek et al. 2023, J Sports Sci Med 22(2) (handball, "LPS KINEXON ONE" at 20 Hz): <https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993/>, accessed 2026-10-02.
- Irid et al. 2025, Biol Sport 42(4) (youth basketball rolling windows): <https://pmc.ncbi.nlm.nih.gov/articles/PMC12490299/>, accessed 2026-10-02.
- Pantazis et al. 2026, Appl Sci 16(4):2037 (3x3 basketball, PERFORM IMU): <https://www.mdpi.com/2076-3417/16/4/2037>, accessed 2026-10-02.
- Zecirovic et al. 2026, Asian Exerc Sport Sci J 10(1) (football, Kinexon GPS export): <https://journal.aesasport.com/index.php/aesa/article/view/579>, accessed 2026-10-02.
- Game versus practice in U16 and U18 women's basketball (Kinexon at 20 Hz): <https://pmc.ncbi.nlm.nih.gov/articles/PMC12473971/>, accessed 2026-10-02.
- Blauberger et al. 2021, Sensors 21(4):1465 (Kinexon LPS validation): <https://pmc.ncbi.nlm.nih.gov/articles/PMC7923412/>, accessed 2026-10-02.
- Frontiers 2026 change-of-direction study (IMU specifications match the IMU brochure): <https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1665797/full>, accessed 2026-10-02.
- Grob et al. 2025, Int J Strength Cond (jump height: Kinexon versus Optojump and force plate): <https://journal.iusca.org/index.php/Journal/article/download/359/478/4949>, accessed 2026-10-02.
- `floodlight` Kinexon parser, documentation and source: documentation: <https://floodlight.readthedocs.io/en/latest/modules/io/kinexon.html>, source: <https://github.com/floodlight-sports/floodlight/blob/master/floodlight/io/kinexon.py>, accessed 2026-10-02.
- Catapult blog, PlayerLoad fundamentals: <https://www.catapult.com/blog/fundamentals-playerload-athlete-work>, accessed 2026-10-02.
- Catapult support, Configuring Metabolic Power Settings: <https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings>, accessed 2026-10-02.
- Catapult Vector Core, Post-Activity Parameters: <https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters>, accessed 2026-10-02.
- Sensors 2025, 25(9):2764, review of acceleration-based load metrics (no Kinexon content): <https://www.mdpi.com/1424-8220/25/9/2764>, accessed 2026-10-02.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
