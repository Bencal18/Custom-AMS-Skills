# STATSports data

Checked against: public STATSports articles and product pages for Sonra, Sonra Live, Sonra Lite, Apex, and Apex 2.0, on 2026-10-07. The Sonra product page names the software version as Sonra 5.0. The STATSports support centers need a browser check that this review did not pass, so their articles were not read.

This file describes what STATSports publishes about its exports, what each metric means, and how to transform the data for analysis. STATSports, Sonra, Apex, and Viper are trademarks of their owner. This repository is not affiliated with or endorsed by STATSports.

## Get the data

STATSports sells Apex trackers with Sonra software for elite teams, Sonra Lite for semi-professional and amateur teams, and the Apex Athlete Series app for individual players. Viper is the older STATSports system. Sonra Live is the iPad and watch app for live data.

Use one of these routes:

- Session export: in Sonra, select the session and players, then select **Export Data**. Choose the default CSV or a template you built, select the drills, and select **Generate**. Sonra also exports CSV from the **Squad Period** dashboard, and exports dashboards to PDF.
- Metric event exports: in **Export Data**, open the **Metrics** tab, then pick an event export. Each export lists every event of one type, such as each sprint. The types are Sprints, HML Efforts, High Intensity Bursts, High Intensity Activities, Collisions, Scrums, and Dives. These exports are CSV. A 2024 article also names an events export in CSV and XML.
- Raw data: a 2022 STATSports article names a standard **Raw Data** export and an extended **Raw Data Extended** export. Two STATSports articles describe the extended file as CSV. It holds the position quality fields HACC, HDOP, and number of satellites, logged at 10 Hz. The file format of the standard Raw Data export is Not confirmed.
- Sonra Exchange: sends raw sessions to another Sonra user. The receiver's own zones and settings then apply. Use it instead of sending CSV files built with unknown zones.
- API: Sonra has an API. A 2022 STATSports update says it returns all software metrics, including custom metrics, full raw data, drill labels, primary and secondary positions, and has a date range endpoint. The base URL, authentication, endpoint names, and response fields are Not published. Ask the user for the documentation their account manager gave them.

Row level depends on the export:

- Session CSV: Not confirmed. Sonra can split a session into drills before export, so ask the user whether the file holds session totals, drill rows, or both.
- Metric event exports: one entry per event, with start and end time, duration, distance, and other fields listed under [Export columns](#export-columns).
- Raw data: Not confirmed. The extended file logs position quality at 10 Hz. The column names are Not published.

## API output

Not published. STATSports states what the API returns, but it does not publish endpoint names, fields, nesting, or paging. Do not invent endpoint names. The API sends raw data at 10 Hz for GNSS and 100 Hz for the accelerometer and gyroscope.

## Export columns

STATSports does not publish the header row of the session CSV or the raw data CSV. Ask the user for the header row and two rows.

STATSports lists the contents of the metric event exports. It gives them as plain names, not exact column headers:

| Export | Contents STATSports lists | Units STATSports states |
|---|---|---|
| Sprints | Start and end time, time since the last sprint, duration, distance, max speed, average metabolic power | Not published |
| HML Efforts | Start and end time, time since the last HML effort, duration, distance, max speed, average metabolic power | Not published |
| High Intensity Bursts | Start and end time, time since the last burst, duration, distance, max speed | Not published |
| High Intensity Activities (accelerations, decelerations, and sprints) | Start and end time, time since the last activity of that type, duration, distance, magnitude for accelerations and decelerations, average metabolic power, Dynamic Stress Load | Magnitude in m/s/s |
| Collisions (rugby) | Collision load, time to feet, post-collision acceleration | Not published |
| Scrums (rugby) | Impacts by row, sync time, load, time to feet, post-scrum acceleration | Not published |
| Dives (goalkeepers) | For each dive: its direction, power, and load; the gap since the previous dive and the time to get back up; peak impact; top speed, acceleration, and deceleration; Dynamic Stress Load; and loading per axis | Not published |

Choose absolute or relative zones for event exports in Sonra under **Settings**, then **Calculations**, then **Metric Event Zone**. Record which one was used.

## Sampling and units

STATSports publishes these sampling rates, which differ by device and date:

- Apex, in a 2019 STATSports article: 10 Hz augmented multi-GNSS, 952 Hz accelerometer, 952 Hz gyroscope, and 10 Hz magnetometer. A 2021 article gives 10 Hz GNSS.
- Apex at launch in 2017: 18 Hz GPS and 600 Hz accelerometer.
- Apex 2.0: 25 Hz dual-band RTK GNSS.
- API raw data: 10 Hz GNSS, and 100 Hz accelerometer and gyroscope.

Ask which device recorded the data. Do not assume 952 Hz accelerometer data in an export.

Apex uses GPS, GLONASS, Galileo, and BeiDou, with satellite-based augmentation. HACC is a position error score from 0 to 7. STATSports says values below 1 mean less than 0.5 m error, values below 5 mean less than 2 m error, and 7 is almost unusable.

Units depend on settings. Speed can be m/s, km/h, or mph. Distance can be m, km, miles, or yards. Acceleration magnitude is in m/s/s. Metabolic power is in W/kg. Impacts are in g.

## Zones and thresholds

Sonra calculates many metrics from six zones per metric, numbered 1 to 6 from low to high. Zones exist for speed, heart rate, accelerations, decelerations, metabolic power, and impacts.

Each zone set comes in two forms:

- Absolute zones: set on the squad or group profile. Every player uses the same values. Metric names carry `(Absolute)`, for example `Accelerations (Absolute)`.
- Relative zones: set on each player profile. Speed, acceleration, and deceleration zones can be fixed values or a percentage of the player's own maximum. Metric names carry `(Relative)`.

STATSports publishes these defaults:

- Speed zone 5 starts at 5.5 m/s (19.8 km/h). Zone 6 starts at 7 m/s (25.2 km/h). The other speed zone defaults are Not published on a page this review could read.
- Sprints: entry speed 19.8 km/h, held for at least 1 s. You can change all three sprint settings, including an exit speed, for the whole account or for one player.
- Accelerations and decelerations: zone 5 starts at 4 m/s². A 2020 STATSports article counts accelerations and decelerations in zones 3 to 6 as efforts of at least 2.0 m/s² for at least 0.5 s. STATSports notes that practitioners often use 3 m/s² as a high-intensity threshold. That is not a stated Sonra default.
- Impacts: zone 5 starts at 11 g.
- High Intensity Bursts: at least 3 high-intensity activities, each no more than 20 s apart. The activities are accelerations, decelerations, or impacts in zone 5 or above. A 2022 article also lists sprints. The count, the gap, and the zones can be changed.
- Heart rate: six zones. The red zone starts at the zone 5 threshold, 85% of the player's maximum heart rate.
- HML: 25.5 W/kg.

The minimum time in a speed zone before distance counts is Not confirmed. The boundary rule, whether a value exactly on a threshold counts in the lower or upper zone, is Not confirmed. STATSports pages say both "over 5.5 m/s" and "at or above 5.5 m/s". If no one knows, use at or above the lower bound and below the upper bound, and say so.

## Metric meanings

These definitions are paraphrased from public STATSports pages. Proprietary metrics are reported as STATSports defines them. Do not recompute them.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| Total Distance | Distance covered | Not published | m, km, miles, or yards | `total-distance.md` in `gps-running-load` | Filtering is Not published |
| Distance Per Minute | Work rate | Average distance in metres covered each minute | m/min | `total-distance.md` in `gps-running-load` | Depends on how drill edges are drawn |
| Max Speed | Highest speed | The highest speed in the session or drill | m/s, km/h, or mph | `high-speed-running.md` in `gps-running-load` | Smoothing is Not published |
| High Speed Running (HSR) | Distance at high speed | Distance in speed zones 5 and 6. By default, above 5.5 m/s. Reported as HSR (Absolute) and HSR (Relative) | m or yards | `high-speed-running.md` in `gps-running-load` | Depends on zone settings |
| Distance in speed zones | Distance in each of six speed zones, for example `Zone 4 Distance` | Distance while speed is in the zone | m | `high-speed-running.md` in `gps-running-load` | Zone dwell time is Not confirmed |
| Sprints | Count of sprint efforts | A run above the sprint entry speed, held for the minimum duration. Defaults 19.8 km/h and 1 s | count | `high-speed-running.md` in `gps-running-load` | Sprint uses an entry speed, an exit speed, and a minimum time, so it is not the same as zone 6 distance |
| Accelerations and Decelerations | Counts of speed-ups and slow-downs | Efforts in acceleration or deceleration zones, reported by zone, for example `Zone 5 Accelerations`. A 2020 article states at least 2.0 m/s² for at least 0.5 s for zones 3 to 6 | count | `accelerations-decelerations.md` in `gps-running-load` | Count the zones the user names. Zone 4 and zone 6 bounds are Not confirmed |
| Maximum Acceleration and Maximum Deceleration | Largest speed change | The highest value in the session. Sonra can scan sessions for new all-time maximums | m/s² | `accelerations-decelerations.md` in `gps-running-load` | Relative zones are a percentage of the stored maximum. Record the maximum used |
| HML Distance (HMLD, High Metabolic Load Distance) | Distance at high estimated energy cost | Distance while metabolic power is above 25.5 W/kg. A 2019 consumer article instead describes it as HSR plus acceleration and deceleration distance | m | None | Proprietary. The metabolic power formula is Not published |
| HML Efforts | Count of high metabolic load efforts | Efforts above 25.5 W/kg, with metabolic power from speed and acceleration | count | None | Proprietary |
| Explosive Distance | Distance at high energy cost below HSR speed | Distance with metabolic power above 25.5 W/kg and speed below the HSR threshold | m | None | Proprietary |
| High Intensity Distance | STATSports app metric for individual players | HSR distance plus distance while accelerating and decelerating | m or yards | None | Proprietary. The acceleration cut-off is Not published |
| High Intensity Bursts (HIB) | Clusters of hard actions | See [Zones and thresholds](#zones-and-thresholds). Reported as HIB distance, number of HIB efforts, and time between HIB | count, m, s | None | Settings change the count |
| Dynamic Stress Load (DSL) | Weighted impact load | Sum of weighted impacts above 2 g, from steps and collisions. The weighting is Not published. STATSports says DSL is not comparable between athletes | Not published | None | Proprietary. Compare an athlete only with their own history |
| Total Loading, and Lateral, Vertical, and Anterior-Posterior loading | Accelerometer load | Sum of acceleration forces, in total or on one axis | Not published | None | Proprietary. Do not compare with other vendors' accelerometer load |
| Step Balance | Left and right step impact split | Average peak step impact on the left foot against the right, shown as a split such as 48:52. A 2024 article describes it as average vertical force on each foot | % | None | Proprietary. Report as given |
| Max Intensity Period (MIP) | Peak demand | The highest moving average of a chosen metric over a window the user sets. Default 3 minutes. Sub-MIP also exists | Metric unit per window | `peak-demands.md` in `gps-running-load` | Moving-average type and step are Not published |
| Heart rate metrics | Average and max heart rate, time in heart rate zones 1 to 6, Time in Red Zone | Zones are percentages of each player's maximum heart rate | bpm, s | `heart-rate-load.md` in `load-and-wellness` | Six zones, not five |
| Heart Rate Exertion (HRE) | Weighted heart rate volume | Each sample gets a weight that rises as heart rate nears the maximum, on a convex curve. Weight times duration in seconds is summed. The weights are Not published | Not published | `heart-rate-load.md` in `load-and-wellness` | Not Edwards TRIMP. Do not mix the two |
| Heart Rate Variability | Beat-to-beat variation | Variation in the intervals between heart beats, averaged over 2 minutes. The calculation is Not published | Not published | None | Report as given |
| Heart Rate Load | Listed heart rate metric | Not published | Not published | None | Ask the user for the definition |

A 2022 STATSports leaderboard article says it used match data recorded as `Gameday`. Whether `Gameday` is a session type field in the Athlete Series is Not confirmed. Sonra drill labels have primary, secondary, tertiary, and free text fields. Match-day labels such as MD-1 are Not published as a Sonra field. Build them from the fixture list with `match-day-load.md` in `gps-running-load`.

## Transform the data

Follow these steps to turn STATSports data into the athlete, session, and measure tables from `ams-data-setup`:

1. Get the header row and two rows from the user. Map each column to a meaning and unit before any calculation.
2. Ask whether each metric is absolute or relative. Keep `(Absolute)` and `(Relative)` metrics in separate measures.
3. Ask whether the export holds session rows, drill rows, or both. Do not sum drill rows and session rows together. Check drill sums against the session total.
4. Reshape to one row per athlete, session, drill, and metric.
5. Convert units only after you confirm them. Divide km/h by 3.6 to get m/s.
6. Record the zone settings, sprint settings, and maximum values with the data. Sonra Exchange recalculates sessions with the receiver's settings, so a shared session can change.
7. For event exports, count rows per athlete and session to get event counts, and check them against the session totals.
8. For raw data, check HACC, HDOP, and number of satellites. Remove poor samples, and state the rule you used.

## Common mistakes

These are the mistakes most often made with STATSports data:

- Comparing HSR, sprint, or acceleration counts across squads or seasons after someone changed the zones.
- Mixing absolute and relative versions of a metric in one chart.
- Treating Sprints as zone 6 distance. Sprints use an entry speed, exit speed, and minimum time.
- Recomputing HMLD, DSL, Step Balance, or Heart Rate Exertion from raw data. The formulas are not published.
- Comparing DSL between athletes. STATSports says it is a personal score.
- Comparing Total Loading or DSL with Catapult PlayerLoad or Kinexon Accumulated Acceleration Load.
- Comparing STATSports Heart Rate Exertion with Edwards TRIMP. The weights differ.
- Assuming every Apex records at 952 Hz. Rates differ by device and route.

## Details that are not confirmed

Do not assume these details. Ask the user:

- The header row and row level of the session CSV and the raw data files.
- The API base URL, authentication, endpoints, and fields.
- Speed zones 1 to 4, and acceleration zones 1, 2, 4, and 6.
- The minimum time in a speed zone before distance counts.
- The boundary rule for values exactly on a threshold.
- The sprint exit speed default.
- The metabolic power formula, the DSL weighting, and the Heart Rate Exertion weights.
- The definition of Heart Rate Load, and the Heart Rate Variability calculation.
- The file format of the standard Raw Data export.

## Sources

This file draws on these STATSports vendor articles and product pages. Each one supports a product fact stated above:

- Vendor article: STATSports, "Sonra Metric Event Exports: Applications and Visualisations", 2023-03-07: <https://statsports.com/article/sonra-metric-event-exports-applications-and-visualisations>, accessed 2026-10-07.
- Vendor article: STATSports, "Absolute and Relative Metric Options Added To Improve Individual Athlete Monitoring", 2024-04-30: <https://statsports.com/article/absolute-and-relative-metric-options-added-to-improve-individual-athlete-monitoring>, accessed 2026-10-07.
- Vendor article: STATSports, "High Intensity Bursts: Assisting In Drill And Recovery Design", 2022-11-03: <https://statsports.com/article/high-intensity-bursts-assisting-in-drill-and-recovery-design>, accessed 2026-10-07.
- Vendor article: STATSports, "Sonra Desktop Updates", 2022-04-14: <https://statsports.com/article/sonra-desktop-updates>, accessed 2026-10-07.
- Vendor article: STATSports, "Temporal pattern analysis of physical data using Sonra's Segment Drills function", 2020-03-12: <https://statsports.com/article/temporal-pattern-analysis-of-physical-data-using-sonras-segment-drills-function>, accessed 2026-10-07.
- Vendor article: STATSports, "Stadium Data: A Premier League Report", 2020-06-17: <https://statsports.com/article/stadium-data-a-premier-league-report>, accessed 2026-10-07.
- Vendor article: STATSports, "Stadium Data: An Austrian Bundesliga Report", 2022-06-24: <https://statsports.com/article/stadium-data-an-austrian-bundesliga-report>, accessed 2026-10-07.
- Vendor article: STATSports, "Sonra Exchange: Share Data Seamlessly With Other Users", 2022-08-02: <https://statsports.com/article/sonra-exchange-share-data-seamlessly-with-other-users>, accessed 2026-10-07.
- Vendor article: STATSports, "Monitoring High Speed Running Demands in Youth Soccer Players", 2020-06-05: <https://statsports.com/article/monitoring-high-speed-running-demands-in-youth-soccer-players-absolute-or-individualised-thresholds-a-case-study>, accessed 2026-10-07.
- Vendor article: STATSports, "Game Demands of Elite U17 Gaelic Footballers", 2020-02-07: <https://statsports.com/article/game-demands-of-elite-u17-gaelic-footballers-an-insight-into-the-performance-of-a-successful-minor-team-in-ulster>, accessed 2026-10-07.
- Vendor article: STATSports, "Application of Absolute and Individualized Acceleration and Deceleration Zones", 2022-05-03: <https://statsports.com/article/application-of-absolute-and-individualized-acceleration-deceleration-zones-to-quantify-external-training-load-with-statsports-sonra>, accessed 2026-10-07.
- Vendor article: STATSports, "Maximum Acceleration and Deceleration: Metric Considerations and Uses", 2021-07-12: <https://statsports.com/article/maximum-acceleration-and-deceleration-metric-considerations-and-uses>, accessed 2026-10-07.
- Vendor article: STATSports, "USYS Elite 64 players shining bright on Metric Leaderboards", 2022-09-23: <https://statsports.com/article/usys-elite-64-players-shining-bright-on-metric-leaderboards>, accessed 2026-10-07.
- Vendor article: STATSports, "HMLD: What is it and why is it important to track?", 2019-08-29: <https://statsports.com/article/what-is-hmld-and-why-is-it-important>, accessed 2026-10-07.
- Vendor article: STATSports, "High Intensity distance: What Is It and Why Is It Important To Track?": <https://statsports.com/the-locker/high-intensity-distance-what-is-it-and-why-is-it-important-to-track>, accessed 2026-10-07.
- Vendor article: STATSports, "A Comparison of Domestic and European Demands and Positional Differences in Elite Soccer", 2021-02-11: <https://statsports.com/article/a-comparison-of-domestic-and-european-demands-and-positional-differences-in-elite-soccer>, accessed 2026-10-07.
- Vendor article: STATSports, "A Comparison of the Peak Game Demands of Elite Competitive Matchplay in Under 19 and First Team Soccer", 2020-06-10: <https://statsports.com/article/a-comparison-of-the-peak-game-demands-of-elite-competitive-matchplay-in-under-19-and-first-team-soccer>, accessed 2026-10-07.
- Vendor article: STATSports, "What is DSL and why is it an important metric to track?", 2019-09-19: <https://statsports.com/article/what-is-dsl-and-why-is-it-an-important-metric-to-track>, accessed 2026-10-07.
- Vendor article: [STATSports Viper article on DSL and Step Balance](https://statsports.com/article/injury-prevention-using-statsports-viper), 2014-10-23, for the DSL and Step Balance definitions only, accessed 2026-10-07.
- Vendor article: [STATSports Apex Athlete Series article on Step Balance](https://statsports.com/article/5-ways-your-apex-athlete-series-can-help-you-avoid-injuries), 2019-10-03, for the Step Balance display only, accessed 2026-10-07.
- Vendor article: STATSports, "Data-Driven Excellence: Harnessing Accelerometer Metrics with STATSports GPS Monitoring", 2024-03-05: <https://statsports.com/article/accelerometer-metric-insight_statsports_gps_monitoring>, accessed 2026-10-07.
- Vendor article: STATSports, "Maximising the use of heart rate zones, metrics and thresholds", 2020-03-18: <https://statsports.com/article/maximising-the-use-of-heart-rate-zones-metrics-and-thresholds-within-sonra>, accessed 2026-10-07.
- Vendor article: STATSports, "Understanding the internal-external load relationship with STATSports' Apex", 2020-07-15: <https://statsports.com/article/understanding-the-internal-external-load-relationship-with-statsports-apex>, accessed 2026-10-07.
- Vendor article: STATSports, "Macrocycle Overview: Does Player Tracking aid Periodized Peak Performance?", 2019-07-02: <https://statsports.com/article/macrocycle-overview-does-player-tracking-aid-periodized-peak-performance>, accessed 2026-10-07.
- Vendor article: STATSports, "STATSports Launch 'The Most Powerful Wearable in Sport'", 2017-06-02: <https://statsports.com/article/statsports-launch-the-most-powerful-wearable-in-sport>, accessed 2026-10-07.
- Vendor product page: STATSports, American football product page, for Apex 2.0 at 25 Hz: <https://statsports.com/sonra/american-football>, accessed 2026-10-07.
- Vendor product page: STATSports, Sonra product page, for Sonra 5.0 and Sonra Live: <https://statsports.com/sonra>, accessed 2026-10-07.
- Vendor product page: STATSports, Sonra Lite product page: <https://statsports.com/sonra-lite>, accessed 2026-10-07.
