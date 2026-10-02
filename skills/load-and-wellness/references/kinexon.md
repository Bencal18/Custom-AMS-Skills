# Kinexon data

Checked against: public Kinexon product pages, the `floodlight` Python package 1.1.0, and published studies, on 2026-10-02. Kinexon publishes no public API reference or export column list.

This file describes what is publicly known about Kinexon exports, what each metric means, and how to transform the data for analysis. Kinexon is a trademark of its owner. This repository is not affiliated with or endorsed by Kinexon.

## Get the data

Kinexon states that users can get statistics and raw data through CSV exports or a REST API. Kinexon does not publish the API reference or the export steps. Ask the user to do one of these:

- Paste the header row and two rows of their export.
- Share the API documentation their organization received from Kinexon.

Kinexon PERFORM LPS is a local positioning system (LPS) that tracks position with radio tags and fixed anchors, often indoors. Published studies sampled it at 20 Hz. The Kinexon IMU tag samples acceleration at 1 kHz and provides it at 100 Hz.

## API output

Not confirmed. Do not invent endpoint names. Third-party web pages show example Kinexon endpoints that are marked as conceptual. Do not use them.

## Export columns

The `floodlight` Python package reads Kinexon position CSV files. It expects these column names, lowercase with spaces:

| Column name | Meaning | Units |
|---|---|---|
| `ts in ms` | Time stamp | ms |
| `sensor id` | Tag ID | None |
| `mapped id` | Athlete ID mapped to the tag | None |
| `full name` | Athlete name | None |
| `number` | Jersey number | None |
| `group id` | Group ID | None |
| `group name` | Group name, such as team | None |
| `x in m` | Position on the x axis. Axis direction not confirmed. | m |
| `y in m` | Position on the y axis. Axis direction not confirmed. | m |

The column names for session metrics, such as distance, speed, accumulated acceleration load, and jumps, are not confirmed. Ask the user for the header row.

## Metric meanings

Kinexon names these metrics in its product material: Accumulated Acceleration Load, Mechanical Load, Jump Load, Number of Jumps, Jump Height, Max. Speed, Changes of Orientation, Exertion Events, and Total Distance.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| Total Distance | Distance covered | Kinexon publishes no formula. LPS and GPS Pro measure position. An IMU can only estimate distance. One study calls the IMU value "estimated equivalent distance". One Kinexon handball IMU post says an IMU does not track position and also says an IMU uses position data, so Kinexon contradicts itself. | m (yards in American football) | `total-distance.md` in `gps-running-load` | IMU values are estimates, not measured distance |
| Max. Speed | Highest speed | Kinexon publishes no formula. LPS and GPS Pro measure position. An IMU can only estimate speed, and how an IMU reports Max. Speed is not published. The same handball IMU post contradicts itself on whether an IMU uses position data. | km/h and mph | `high-speed-running.md` in `gps-running-load` | Smoothing is not published. No source supports a cross-vendor comparison of the number |
| Accumulated Acceleration Load | Accelerometer load | Proprietary. One published study prints it as the accumulated rate of change in acceleration on three axes, in the same form as Catapult PlayerLoad. | AU (arbitrary units) | None | Do not compare or pool with Catapult PlayerLoad. Kinexon says other manufacturers call this metric Player Load, but formulas, scaling, and sampling may differ |
| Mechanical Load | Load from speed changes | Accelerations and decelerations grouped by intensity, multiplied by proprietary weights, and summed. Mechanical Load is Accel Load plus Decel Load. | AU (arbitrary units) | None | Weights and bands are not published. Mechanical Load is a weighted load, not an event count, and no source supports a Catapult equivalent, so no reference file applies |
| Mechanical Intensity | Rate of Mechanical Load | Mechanical Load divided by time | Not confirmed | None | None |
| Number of Jumps | Jump count | Kinexon describes detection as vertical displacement over height thresholds. The thresholds are not published. One study reports a minimum air time of 0.3 s, and another reports a minimum dwell time of 0.4 s. | count | None | Depends on settings |
| Jump Load | Work done in jumps | Body mass × g × jump height in m, summed over jumps, as described in two studies. Stone et al. uses g = 9.8 m/s². Pantazis et al. (3x3 basketball) uses g = 9.81 m/s². Stone et al. reports Jump Load in J in a table and in arbitrary units in its text. Shown per kg in Kinexon material. | J or J/kg | None | Jump height method not published |

Published studies that used Kinexon set their own thresholds, for example:

- Accelerations at 1.5 m/s² with a 0.5 s minimum in one study, and 2 m/s² in another.
- Sprints at 18.72 km/h (5.2 m/s) with a 1.0 s minimum.
- High-speed running at 4.4 m/s or more in the Carton-Llorente handball study. The Bassek handball LPS study names 5.5 to 7 m/s high-intensity running.

These are study settings, not Kinexon defaults.

## Transform the data

Follow these steps to turn Kinexon data into the athlete, session, and measure tables:

1. Get the header row from the user, and map each column to a meaning and unit before any calculation.
2. Pick one athlete identifier. Use `full name`, then `mapped id`, then `sensor id`, then `number`, in that order, based on which is filled.
3. Convert `ts in ms` to seconds by dividing by 1000. Confirm with the user whether it is Unix time or time from the session start, and which time zone applies.
4. Reshape session metrics to one row per athlete, session, drill or segment, and metric.
5. Ask which thresholds the account uses for speed zones, accelerations, and jumps. Record them with the data.
6. Check whether the export splits a session into drills or segments before you sum rows. Compare sums with the session total.

## Common mistakes

These are the mistakes most often made with Kinexon data:

- Comparing or pooling Accumulated Acceleration Load with Catapult PlayerLoad or acceleration load, or explaining the gap between them. Kinexon's formula is proprietary. Kinexon says other manufacturers call it Player Load, but formulas, scaling, and sampling may differ. The cause of a gap is unknown. Wearing both systems in the same session shows the size of the gap, not its cause.
- Comparing Mechanical Load across accounts or sensor types. The weights and bands are not published.
- Comparing high-speed running or sprint distance with another system without matching thresholds.
- Using a jump count without knowing the minimum air time setting.
- Summing drill rows and a session row together.

## Details that are not confirmed

Do not assume these details. Ask the user:

- The API endpoints and response fields.
- The column names and units of the session metric export.
- The default speed, acceleration, and jump thresholds.
- The boundary rule: whether a value exactly on a speed or acceleration threshold counts. If no one knows, use at or above the lower bound and below the upper bound, and say so.
- The time zone of time stamps.
- Whether drill or segment rows overlap with session rows.

## Sources

- `floodlight` Kinexon reader documentation: <https://floodlight.readthedocs.io/en/latest/modules/io/kinexon.html>, accessed 2026-10-02.
- Kinexon PERFORM LPS product page: <https://kinexon-sports.com/products/perform-lps/>, accessed 2026-10-02.
- Kinexon PERFORM IMU brochure: <https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf>, accessed 2026-10-02.
- Kinexon, "Mechanical load in basketball": <https://kinexon-sports.com/blog/mechanical-load-basketball/>, accessed 2026-10-02.
- Study using Kinexon IMU, with Accumulated Acceleration Load, sprint, and jump settings: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10765436/>, accessed 2026-10-02.
- Stone et al., study using an IMU-based Kinexon system at 20 Hz, with acceleration and jump settings: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8888863/>, accessed 2026-10-02.
- Carton-Llorente et al., handball study using Kinexon LPS, with high-speed running and acceleration settings: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10588589>, accessed 2026-10-02.
- Bassek et al., handball study using LPS KINEXON ONE at 20 Hz, with speed zones: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10244993>, accessed 2026-10-02.
- Pantazis et al., 3x3 basketball study using Kinexon PERFORM IMU, with Jump Load, Mechanical Load, and Accumulated Acceleration Load values: <https://www.mdpi.com/2076-3417/16/4/2037>, accessed 2026-10-02.
- Kinexon PERFORM GPS Pro football brochure, with Max. Speed units: <https://hs.kinexon.com/hubfs/SPO-Football-Collaterals/SPO_Brochure_Football_KINEXON%20PERFORM%20GPS%20Pro_EN.pdf>, accessed 2026-10-02.
- Kinexon, "Tracking the Top Player Metrics in Sports", for jump detection: <https://kinexon-sports.com/blog/data-analytics-in-sports/>, accessed 2026-10-02.
- Kinexon, March Madness load metrics, for the Player Load naming: <https://kinexon-sports.com/blog/maximizing-performance-during-march-madness-key-strategies-load-metrics-for-coaches/>, accessed 2026-10-02.
- Kinexon, individualized football performance data, for yards: <https://kinexon-sports.com/blog/how-individualized-football-performance-data-improves-load-management/>, accessed 2026-10-02.
- Kinexon, LPS, GPS, and IMU compared: <https://kinexon-sports.com/blog/player-tracking-with-lps-gps-and-imu/>, accessed 2026-10-02.
- Kinexon, what an IMU tracks in handball: <https://kinexon-sports.com/blog/what-is-an-imu-sensor-measuring-in-elite-handball/>, accessed 2026-10-02.
