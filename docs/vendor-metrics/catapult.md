# Catapult metrics

Catapult makes wearable GNSS and local positioning (LPS) devices in the Vector family, the OpenField software, the Catapult One product for individual players and small teams, and, through Perch, a rack-mounted depth camera for weight room velocity-based training. Perch has been owned by Catapult since the acquisition Catapult announced on 2025-06-05. This page explains how each metric that Catapult publicly documents is defined and calculated, so a coach or sports scientist can read Catapult exports correctly. Everything here comes from public pages and peer-reviewed papers, and each fact links to its source. Checked against: Catapult Vector Core, OpenField, Catapult One, and Perch help centre articles; the Connect API reference; Catapult blog and white paper pages; Catapult's ASX release of 2025-06-05; five public Kinexon pages used for comparison notes; and 11 peer-reviewed papers. Software versions named by those pages include OpenField Console 3.12.0, Vector Live 2.9.0, and device firmware 8.8.0 for Gen 2 metabolic power. The worked examples ran on Python 3.9.6 and NumPy 2.0.2, 2026-10-02.

Catapult, OpenField, Vector, PlayerLoad, Perch, and Kinexon are trademarks of their owners. This repository is not affiliated with or endorsed by Catapult or Kinexon.

Kinexon appears on this page only in comparison notes. Kinexon has its own page in this folder: [Kinexon metrics](kinexon.md).

## How to read this page

Each metric has one block under a `####` heading. Each block is a short list with these fields:

- **Vendor name:** The name as Catapult writes it, in code font, with abbreviations and live-app names.
- **What it measures:** One plain sentence.
- **Window or phase:** The time window, phase, default thresholds, or default bands that a Catapult page states. Examples on a Catapult page are labelled as examples.
- **Calculation:** Up to three parts. "Vendor definition (paraphrased)" is a close paraphrase of Catapult's own text, with a link. "Formula as Catapult publishes it" is a formula taken from a Catapult page, with its weights and numbers exact. "Restatement, not a vendor statement" is a plain-math version written for this page. It is not Catapult's wording.
- **Inputs:** The raw signal the metric needs.
- **Units:** As published.
- **Variants:** Per minute, banded, relative, live versus post-session, and product variants.
- **Comparison with standard methods or other vendors:** Only where a source supports a comparison. "Standard methods" covers peer-reviewed methods. "Other vendors" covers the closest Kinexon metric.
- **What changes the number:** Settings and processing steps that a source says affect the value.
- **Source links:** The public pages cited in the block.

Not published means Catapult does not publish that detail in any public source cited on this page. It does not mean the item does not exist. Many Catapult definitions sit behind a customer sign-in. See [Pages not publicly readable](#pages-not-publicly-readable).

This page paraphrases vendor text. Formulas, weights, and numbers match the source. Exact metric names, field names, and units are in code font.

## Background

### Five facts that matter most

These five points affect how you read every Catapult export:

- Most Catapult numbers depend on settings you control: velocity bands, acceleration bands, heart rate bands, dwell times, and team thresholds. Two teams with the same name for a metric can export different numbers. Record the settings with every export.
- New settings apply only to new sessions until you reprocess old ones ([Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands)).
- Catapult does not publish its velocity filter or its full effort rules. Rebuilding Catapult numbers from raw 10 Hz data will come close but will not match exactly ([Vector T7 white paper](https://www.catapult.com/blog/vector-t7-white-paper)).
- Player Load is driven mostly by running impacts and by how the vest fits. Compare an athlete with their own history, not with teammates ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load), [Barrett et al. 2014](https://doi.org/10.1123/ijspp.2013-0418)).
- Vector Core and OpenField compute Heart Rate Exertion with different weights. Catapult One and Vector use different sprint thresholds. Do not mix products in one chart without converting.

### Product names used on this page

These product names appear on this page:

- **Vector Core:** Catapult's simplified Vector package. Its metrics are listed on the Vector Core help centre ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **Vector (Plus or Pro) with OpenField:** The full Vector system. OpenField Console is the desktop software. OpenField Cloud is the web platform. Many Pro metrics need a Vector Pro licence or an account module ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **Vector app and Vector Live app:** Catapult's iPhone, iPad, and watch apps for live data ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **Catapult One:** Catapult's product for individual players and small teams ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **Connect API:** Catapult's data API for OpenField ([Connect API index](https://docs.connect.catapultsports.com/llms.txt)).

### Sensors and sampling, as Catapult publishes them

Catapult publishes these facts about its sensors and sampling:

- GNSS velocity comes from Doppler shift. LPS (ClearSky) velocity comes from differentiating position ([Catapult Glossary](https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary)).
- GPS data is sampled at 10 Hz. IMA uses inertial data at 100 Hz ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- On the Vector X7, the accelerometer runs at 400 Hz and is smoothed to 100 Hz for PlayerLoad ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)). Catapult One states the same 400 Hz to 100 Hz path ([What is Player Load? (Catapult One)](https://onesupport.catapultsports.com/hc/en-us/articles/7443837147023-What-is-Player-Load)). The smoothing method is Not published.
- A 2018 Catapult article says its accelerometers measured at 10,000 Hz and recorded at 100 Hz, with gyroscopes and magnetometers at 100 Hz ([Catapult Fundamentals: GPS tracking](https://www.catapult.com/blog/catapult-fundamentals-gps-tracking-technology)). This is an older device description. Treat the X7 figure above as the device-specific value.
- The Vector T7 LPS device samples at 10 Hz and uses a Time Difference of Arrival protocol ([Vector T7 white paper](https://www.catapult.com/blog/vector-t7-white-paper)).

### Three rules that change many numbers at once

Apply these three rules when you read or compare numbers:

1. **Bands apply forward only.** New bands apply to future activities. You must reprocess old activities to apply new bands to them ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands), [Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands), [How Do I Reprocess Activities?](https://core.catapultsports.com/hc/en-us/articles/7361794930063-How-Do-I-Reprocess-Activities)).
2. **Live values need a device sync.** Band changes reach devices only after you sync or remap devices ([Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands), [Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
3. **Velocity is stored in m/s to two decimal places.** A band typed in km/h or mph is converted and rounded. For example, 3.05 km/h is stored as 0.85 m/s and displays back as 3.06 km/h ([Why velocity bands change (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000675156-Why-do-my-Velocity-Bands-sometimes-change-slightly-after-editing-them-in-the-Cloud), [Why velocity bands change (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7352034984079-Why-Do-My-Velocity-Bands-Sometimes-Change-Slightly-After-Editing-Them-in-the-Cloud)).

Parameter names can also change. OpenField lets you rename a parameter. The API `slug` and `original_name` stay fixed ([Connect API: Parameters](https://docs.connect.catapultsports.com/reference/parameters)). Join exported data on the slug, not the display name. You can also build custom parameters from equations, such as `$velocity_band5_total_distance+$velocity_band6_total_distance` ([How to Create Custom Parameters](https://support.catapultsports.com/hc/en-us/articles/360000509596-How-to-Create-Custom-Parameters)). A custom parameter's export name is whatever the account owner chose.

## Coverage

The table counts what this page covers for each product. "Listed by the vendor" is the number of metrics on the vendor's own public list, where one exists.

| Product | Listed by the vendor | Covered on this page | Notes |
|---|---|---|---|
| Vector Core, post-activity (OpenField Cloud) | 43 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)); Catapult's launch post says "up to 43" ([Vector Core launch](https://www.catapult.com/blog/vector-core-load-management-simplified)) | 43 | The six heart rate band durations share one block |
| Vector Core, live (Vector app) | 13 rows ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)); the launch post says 11 live metrics ([Vector Core launch](https://www.catapult.com/blog/vector-core-load-management-simplified)) | 13 | |
| Vector 7, Bluetooth live (Vector app and watch) | 12 rows ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)) | 12 | Bands 1 to 8 counted as one row, as Catapult lists them |
| Vector Live app, custom parameters | 19 named outputs in three groups: velocity, Player Load, and heart rate ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)) | 19 | Covered in three blocks |
| Vector Pro and Plus with OpenField Console and Cloud | Full list Not published (sign-in) | 40 further blocks beyond the Vector Core lists, plus 117 sport-specific table rows | See [Pages not publicly readable](#pages-not-publicly-readable) |
| Connect API | 20 sensor stream field names (19 on the Sensor Data page plus `pli` on the endpoint page), 2 effort types, 28 event types ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)) | All 20 field names (18 table rows: `lat` and `long` share a row, `id` is in a note), 2 effort types, 28 event types | Account parameter list needs a token |
| Catapult One | 12 in the coach guide plus `Power` in the player guide ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation)) | 13 | |
| Perch | No single public list; full export list on unreadable pages | 16 metric blocks plus 11 aggregate and export rows | See [Perch](#perch-weight-room-velocity-based-training) |

Metric blocks by area:

| Area | Blocks | Table rows |
|---|---|---|
| Distance and speed | 11 | |
| Velocity bands | 17 | |
| Accelerations and decelerations | 11 | |
| PlayerLoad and accelerometer load | 7 | |
| Metabolic power and HMLD | 9 | |
| Heart rate | 9 | |
| Load scores | 4 | 7 benchmark rows |
| Impacts and IMA events | 11 | |
| Jumps | 5 | |
| Intervals and repeated efforts | 7 | |
| Running symmetry | 4 | |
| Sport-specific (basketball, tennis, rugby union, rugby league, football, ice hockey, American football, baseball, cricket) | 0 | 117 |
| Connect API exports | 0 | 18 sensor field rows |
| Perch | 16 | 11 |
| **Total** | **111** | |

Kinexon has its own page. This page does not cover Kinexon metrics.

## Summary tables

Each table below lists the metrics in one area. "Calculation published" is Yes when the vendor publishes the full calculation, Partly when some part is Not published, and Not published when the vendor gives no calculation. The sport-specific tables, the Connect API field table, and the Perch aggregates table later on this page act as their own summaries.

### Summary: distance and speed

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Duration` (h:mm:ss) | How long the period or activity lasted | h:mm:ss | Yes |
| `Distance` (m) | How far the athlete travelled | m | Partly |
| `Meterage Per Minute` (m/min) | Average running speed over the period, often called work rate | m/min | Yes |
| `Max Velocity` (m/s) | The top speed reached | Your chosen speed unit | Yes |
| `Max Vel (% Max)` (%) | The session top speed as a share of the athlete's own top speed | % | Yes |
| `% Max Velocity` (%), live | Live speed as a share of the athlete's top speed | % | Yes |
| `Work/Rest Ratio` (ratio) | How much time the athlete spent running compared with resting | Ratio, no unit | Yes |
| `Distance` (Catapult One) | Total ground covered | m, km, yds, miles | Partly |
| `Distance per Minute` (Catapult One, m/min) | Average work rate | m/min, miles/min, yd/min | Yes |
| `Top Speed` (Catapult One) | The fastest speed the player held | m/s, km/h, mph, or yd/min | Yes |
| `Work Ratio` (Catapult One, %) | The share of time the player was moving with purpose | % | Yes |

### Summary: velocity bands

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Standing Distance` (m), Velocity Band 1 | Distance covered while nearly still | m | Yes |
| `Walking Distance` (m), Velocity Band 2 | Distance covered while walking | m | Yes |
| `Jogging Distance` (m), Velocity Band 3 | Distance covered while jogging | m | Yes |
| `Running Distance` (m), Velocity Band 4 | Distance covered at moderate running speed | m | Yes |
| `HI Distance` (m), Velocity Band 5 | Distance covered at high running speed, below sprint speed | m | Yes |
| `Sprint Distance` (m), Velocity Band 6 | Distance covered at sprint speed | m | Yes |
| `HS Distance` (m) | All distance at high speed and sprint speed together | m | Yes |
| `HS Dist Per Min` (m/min) | High-speed running rate | m/min | Yes |
| `Sprint Dist Per Min` (m/min) | Sprint distance rate | m/min | Yes |
| `Sprint Efforts` (count) | How many separate sprints the athlete made | Count | Partly |
| `HS Efforts` (count) | How many separate high-speed runs the athlete made | Count | Partly |
| `Velocity Distance Band 1 - 8` (m), live | Live distance in each speed band | m | Yes |
| `Velocity Efforts Band 2+` (count), live | Live count of efforts in each band | Count | Yes |
| `Velocity (Set 2)` banded metrics (relative bands) | Banded distance, duration, and efforts against each athlete's own maximum | m, s, count | Yes |
| Vector Live custom speed parameters | Time, distance, and efforts in user-chosen high-speed bands, live | s, %, m, count | Yes |
| Velocity effort attributes (Efforts Breakdown and Connect API) | The profile of each single speed effort | s, %, m/s, m | Yes |
| `Sprint Distance` (Catapult One) | Distance at sprint speed | m, yds | Yes |

### Summary: accelerations and decelerations

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Max Acceleration` (m/s²) | The hardest acceleration in the period | m/s² | Partly |
| `Max Deceleration` (m/s²) | The hardest deceleration in the period | m/s² | Partly |
| `Acceleration Efforts` (count) | How many hard speed-ups the athlete made | Count | Partly |
| `Deceleration Efforts` (count) | How many hard slow-downs the athlete made | Count | Partly |
| `Accel&Decel Efforts` (count) | All hard speed changes together | Count | Yes |
| `Accel&Decel Efforts Per Minute` (count/min) | How often hard speed changes happen | Efforts per minute | Yes |
| Acceleration effort attributes (effort tables and Connect API) | The profile of each single acceleration or deceleration | s, user speed units, m/s², m | Yes |
| `Acceleration load` (sum of absolute acceleration) | The total amount of speeding up and slowing down, with no threshold | Not published | Partly |
| `Acceleration density` (mean absolute acceleration) | How intense the speed changes were on average | Not published | Yes |
| `Acceleration density index` (per 10 m) | Speed-change intensity during movement only, ignoring rest time | Not published | Yes |
| `Max Acceleration` and `Max Deceleration` (Catapult One) | The hardest speed-up and slow-down the player held | m/s² | Partly |

### Summary: PlayerLoad and accelerometer load

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Player Load` (AU) | Total body movement work from the accelerometer | Arbitrary units (AU) | Yes |
| `Player Load Per Minute` (AU/min) | Movement work rate | AU/min | Yes |
| Instantaneous Player Load (`pli`) | Movement load at each moment | AU | Partly |
| `PlayerLoad 2D` (AU) | Player Load without the vertical component | AU | Yes |
| Player Load bands and Vector Live custom Player Load parameters | Time and load spent at high movement intensity | s, %, AU | Yes |
| Smooth Load (`sl`) | A smoothed form of instantaneous Player Load | Smoothed PlayerLoad units | Not published |
| `Player Load` (Catapult One) | Total load on the body from running and impacts | AU | Yes |

### Summary: metabolic power and HMLD

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Metabolic Power (`mp`, W/kg) | The estimated energy cost per second of running and speed changes | W/kg | Yes |
| `Energy` | Estimated energy used in the session | Not published for Vector Core | Partly |
| `High Metabolic Load Distance` (m) | Distance covered while working hard, from fast running or from hard speed changes | m | Yes |
| Peak Metabolic Power (W/kg) | The highest metabolic power reached | W/kg | Yes |
| Metabolic power bands and efforts | Time, distance, and efforts above chosen power levels | s, m, count | Yes |
| `Energy` (Catapult One, kcal) | Energy used in a game or session | kcal | Partly |
| `Power Plays` (Catapult One, count) | The number of intense actions, such as hard accelerations or fast runs | Count | Partly |
| `Power Score` (Catapult One, W/kg) | Average power output per kilogram, useful for small-sided games | W/kg | Partly |
| `Power` (Catapult One player view) | A combined intensity score for the session | Not published | Partly |

### Summary: heart rate

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Max Heart Rate` (bpm) | The highest heart rate in the period | bpm | Yes |
| `Avg Heart Rate` (bpm) | Average heart rate | bpm | Partly |
| `Avg HR (% Max)` (%) | Average heart rate as a share of the athlete's max | % | Yes |
| `Max HR (% Max)` (%) | Peak heart rate as a share of the athlete's max | % | Yes |
| `Heart Rate Band 1 Duration` to `Heart Rate Band 6 Duration` (h:mm:ss) | Time spent in each heart rate zone | h:mm:ss | Yes |
| `Red Zone` (h:mm:ss or min) | Time spent at very high heart rate | h:mm:ss (post), minutes (live) | Yes |
| `Heart Rate Exertion` (Vector Core, AU) | One number for cardiovascular load, weighting hard zones more | Arbitrary | Partly |
| `Heart Rate Exertion` (OpenField, AU) | As above | Arbitrary | Yes |
| `%HR Max` live tile and thresholds | Live heart rate as a share of max, colour coded | % | Yes |

### Summary: load scores

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Volume` (%) | How much work the session held compared with the benchmark day | % | Yes |
| `Intensity` (%) | How hard the session was per minute compared with the benchmark day | % | Yes |
| `Overall` (%) | A single combined load score | % (as displayed) | Partly |
| Acute:Chronic Workload Ratio (OpenField chart) | Recent load compared with longer-term load | Ratio | Partly |

### Summary: impacts and IMA events

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Impacts` (Vector Core, count) | How many big hits or collisions the athlete took | Count | Partly |
| `Impacts` (Catapult One, count) | Large hits such as tackles and collisions | Count | Yes |
| IMA Acceleration count | Forward bursts detected from the inertial sensors, without GPS | Count | Yes |
| IMA Deceleration count | Braking movements detected from the inertial sensors | Count | Yes |
| IMA Change of Direction Left and Right | Sideways cuts to each side | Count | Yes |
| IMA intensity event (`ima_acceleration`) | The size and direction of each inertial movement event | m/s; direction in 1/12 circle | Yes |
| IMA Impact event (`ima_impact`) | The size and main direction of each collision | g | Yes |
| Free running (IMA and `free_running` event) | Stretches of uninterrupted straight-line running | s, count, accumulated PlayerLoad units, m | Yes |
| Average stride rate (IMA) | Steps per unit time during running | Not published | Not published |
| Asymmetrical loading (IMA) | Imbalance between left and right movement load | Not published | Not published |
| Tackle and impact event tables | Per-event detail for collisions | AU, s, g | Yes |

### Summary: jumps

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| IMA Jump (`ima_jump`, height in m) | Each jump and its height | m | Partly |
| Jump Height export (OpenField Console) | Height of each IMA jump | Not stated on the export page | Partly |
| Indoor Jumps (T7 Indoor Analytics) | Jumps detected from inertial sensors indoors, sorted Low, Medium, High | Count; bands in centiseconds | Yes |
| Estimated distance (T7 Indoor Analytics) | Distance estimated from inertial sensors when no positioning system is available | Not published | Not published |
| Live Jumps | Total jumps in real time | Count | Not published |

### Summary: intervals and repeated efforts

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Repeat High Intensity Efforts (RHIE) | Clusters of hard efforts with too little recovery between them | Count, s | Yes |
| `Work Rate - % Distance` (%) | The share of distance covered inside work-rate intervals | % | Yes |
| `Work Rate - Duration` (s) | Time spent in work-rate intervals | s | Yes |
| `Work Rate - Interval Count` (count) | How many work-rate intervals occurred | Count | Yes |
| `Work Rate - Interval Distance` (m) | Distance covered inside work-rate intervals | m | Yes |
| `Maximum Intensity Distance Interval 1`, `2`, `3` (m) | The most distance covered in any window of a set length | m | Yes |
| `Maximum Intensity Player Load Interval 1`, `2`, `3` (AU) | The most Player Load gathered in any window of a set length | AU | Yes |

### Summary: running symmetry

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Running Imbalance` (%) | The load difference between legs while running | % | Partly |
| `Footstrikes` (count) | Footstrikes counted inside qualifying running efforts | Count | Yes |
| `Running Imbalance Standard Deviation` (%) | How consistent the imbalance is from run to run | % | Yes |
| `Running Series #` (count) | How many qualifying running efforts were found | Count | Yes |

### Summary: Perch

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Displacement (m) | How far the bar moved between two points, for example squat depth on the Z axis | Not stated | Yes |
| `Mean Velocity` (m/s) | Average bar speed over the lift | m/s | Yes |
| `Mean Propulsive Velocity` (MPV, m/s) | Average bar speed during only the part of the lift where the athlete accelerates the bar | m/s | Partly |
| `Peak Velocity` (m/s) | The fastest bar speed during the movement | m/s | Yes |
| `Eccentric Time` (s) | How long the lowering phase took | s | Yes |
| `Mean Power` (W) | Average power put into the bar during the lift | W (by the formula) | Yes |
| `Peak Power` (W) | The highest instant power during the lift | W (by the formula) | Yes |
| `Time to Peak Power` (T2PP, s) | How quickly the athlete reaches peak power | s | Yes |
| `Time to Peak Velocity` (T2PV, s) | How quickly the bar reaches top speed | s | Yes |
| `Velocity at 100ms` (V100, m/s) | Bar speed early in the lift, as a sign of explosiveness | m/s | Partly |
| `Work` (kJ) | Energy the athlete put into the bar | kJ | Partly |
| Jump metrics: `Jump Height`, `Time To Takeoff`, `Takeoff Velocity`, `RSIMod`, `Rep Count` | Jump output from head tracking | s for Time To Takeoff, no unit for RSIMod, Not published for height and takeoff velocity | Yes |
| `Estimated 1RM` and `Minimum Velocity Threshold` (MVT) | The predicted one-rep max from load and bar speed | kg or lb; MVT in m/s | Partly |
| `Speed Score`, `Strength Score`, `Total Performance Score` | Where an athlete's load-velocity profile sits compared with their group | z-score | Partly |
| Dynamic velocity goal zone | A personal target speed zone for a given load | m/s | Yes |
| `% Drop` goal | Velocity loss within a set, as a fatigue stop rule | % | Yes |

## Metric reference

Each area below holds one block per metric. Blocks that start with a product name in the heading, such as "Catapult One", describe that product only.

### Distance and speed

#### `Duration` (h:mm:ss)

The fields for this metric are:

- **Vendor name:** `Duration`, in hours, minutes, and seconds.
- **What it measures:** How long the period or activity lasted.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Length of time in hours, minutes, and seconds ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Duration = end time − start time` of the selected period or activity.
- **Inputs:** Device clock and period edits.
- **Units:** h:mm:ss.
- **Variants:** Activity duration and period duration. Every "per minute" metric divides by this value ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** How you draw and edit periods. A Catapult ice hockey article shows that a session clock and an active-shift clock give very different per-minute values for the same file ([Ice Hockey Auto Shift Detection](https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads)).
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Ice Hockey Auto Shift Detection](https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads).

#### `Distance` (m)

The fields for this metric are:

- **Vendor name:** `Distance` (Vector Core post-activity). Live name: `Total Distance`, abbreviated `Dist` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** How far the athlete travelled.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The total distance achieved ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Distance = Σ dᵢ`, where `dᵢ` is the distance travelled between consecutive 10 Hz samples. The 10 Hz stream exposes an accumulated odometer field `o` ([Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz)). Whether Catapult sums positional steps or integrates speed is Not published.
- **Inputs:** GNSS outdoors, or LPS (ClearSky) indoors.
- **Units:** m. You can change the display distance unit in **My Account** ([Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics)).
- **Variants:** Banded distances (see [Velocity bands](#velocity-bands)). Per-minute rate (`Meterage Per Minute`). Catapult One `Distance`.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon lists `Distance` and `Distance per minute` as volume and intensity metrics ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Kinexon does not publish its processing, so the two numbers are not interchangeable by default.
- **What changes the number:** Signal quality (satellites, HDOP, LPS anchors), filtering, and sampling rate. A peer-reviewed review lists sampling rate, device fit, satellite signal, and data filtering as factors that change GPS outputs ([Malone et al. 2017](https://doi.org/10.1123/ijspp.2016-0236)). Catapult does not publish its position or velocity filter. A validation study of the T7 says the manufacturer filter details were withheld as intellectual property ([Vector T7 white paper](https://www.catapult.com/blog/vector-t7-white-paper)).
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics), [Malone et al. 2017](https://doi.org/10.1123/ijspp.2016-0236), [Vector T7 white paper](https://www.catapult.com/blog/vector-t7-white-paper), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Meterage Per Minute` (m/min)

The fields for this metric are:

- **Vendor name:** `Meterage Per Minute` (Vector Core). Live: `Distance / min`, abbreviated `Dist/min` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)). In the load score formula: `Dist Per Minute` ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- **What it measures:** Average running speed over the period, often called work rate.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Distance in metres divided by time in minutes ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). The load score article states `Dist Per Minute = Distance / Duration` ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `Meterage Per Minute = Distance (m) ÷ Duration (min)`.
- **Inputs:** Distance and duration.
- **Units:** m/min. Changing the distance unit changes the intensity units ([Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics)).
- **Variants:** Catapult One `Distance per Minute`. `HS Dist Per Min`. `Sprint Dist Per Min`.
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon `Distance per minute` is the closest name ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). The distance source differs (see `Distance`).
- **What changes the number:** Period edges. Rest time inside a period lowers the value.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Max Velocity` (m/s)

The fields for this metric are:

- **Vendor name:** `Max Velocity`. Live: `Max Vel` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** The top speed reached.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The peak speed reached in any single maximal sprint ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Live: the maximum velocity reached in the selected period or activity ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
  - Restatement, not a vendor statement: `Max Velocity = max(vᵢ)` over the selected time.
- **Inputs:** GNSS Doppler velocity or LPS velocity ([Catapult Glossary](https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary)).
- **Units:** Your chosen speed unit ([Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics)).
- **Variants:**
  - `Max Vel (% Max)`: see the next block.
  - Rolling Max Velocity: an OpenField Console setting. It gives a 60 second rolling window so a missed live packet does not lose the peak ([What is Rolling Max Velocity?](https://support.catapultsports.com/hc/en-us/articles/360002239475-What-is-Rolling-Max-Velocity)).
  - Catapult One `Top Speed`: requires the speed to be held for at least half a second ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon lists `Max. Speed` ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Its method is Not published.
- **What changes the number:** A single data point sets the value, so a missed point loses it in live mode ([What is Rolling Max Velocity?](https://support.catapultsports.com/hc/en-us/articles/360002239475-What-is-Rolling-Max-Velocity)). Velocity filtering changes peaks. The filter is Not published.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Catapult Glossary](https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary), [Change units](https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics), [What is Rolling Max Velocity?](https://support.catapultsports.com/hc/en-us/articles/360002239475-What-is-Rolling-Max-Velocity), [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

#### `Max Vel (% Max)` (%)

The fields for this metric are:

- **Vendor name:** `Max Vel (% Max)`.
- **What it measures:** The session top speed as a share of the athlete's own top speed.
- **Window or phase:** None. The profile max velocity is set per athlete, or prefilled from the account's default athlete profile settings ([Default Athlete Profile Settings](https://core.catapultsports.com/hc/en-us/articles/7347413350159-Default-Athlete-Profile-Settings)).
- **Calculation:**
  - Vendor definition (paraphrased): Peak speed in any single maximal sprint, as a percentage of the athlete's individual maximum velocity ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Max Vel (% Max) = 100 × Max Velocity ÷ profile max velocity`.
- **Inputs:** `Max Velocity` and the athlete profile.
- **Units:** %.
- **Variants:** Live `% Max Velocity` uses instantaneous speed (next block).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** The profile max velocity value. A wrong or stale profile max makes every percentage wrong.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Default Athlete Profile Settings](https://core.catapultsports.com/hc/en-us/articles/7347413350159-Default-Athlete-Profile-Settings).

#### `% Max Velocity` (%), live

The fields for this metric are:

- **Vendor name:** `% Max Velocity`, abbreviated `% Max Vel`.
- **What it measures:** Live speed as a share of the athlete's top speed.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Instantaneous velocity as a percentage of the athlete's max velocity ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
  - Restatement, not a vendor statement: `% Max Velocity(t) = 100 × v(t) ÷ profile max velocity`.
- **Inputs:** Live velocity and the athlete profile.
- **Units:** %.
- **Variants:** Post-session `Max Vel (% Max)`.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Profile max velocity. Live packet loss.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7).

#### `Work/Rest Ratio` (ratio)

The fields for this metric are:

- **Vendor name:** `Work/Rest Ratio`.
- **What it measures:** How much time the athlete spent running compared with resting.
- **Window or phase:** 3 m/s for work, 2 m/s for rest ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Whether these follow your velocity bands is Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Time running above 3 m/s divided by time below 2 m/s ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Work/Rest Ratio = T(v > 3 m/s) ÷ T(v < 2 m/s)`. Time between 2 and 3 m/s counts in neither term.
- **Inputs:** Velocity.
- **Units:** Ratio, no unit.
- **Variants:** Catapult One `Work Ratio` uses a different definition (below).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Period edges, velocity filtering. Worked example 1 gives 24.9 s above 3 m/s, 15.4 s below 2 m/s, and a ratio of 1.617.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Distance` (Catapult One)

The fields for this metric are:

- **Vendor name:** `Distance`, in m, km, yds, or miles ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Total ground covered.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Total distance, described as a global view of exercise volume ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: Same idea as Vector `Distance`. The method is Not published.
- **Inputs:** GNSS.
- **Units:** m, km, yds, miles.
- **Variants:** `Distance per Minute`.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: See Vector `Distance`.
- **What changes the number:** Not published.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

#### `Distance per Minute` (Catapult One, m/min)

The fields for this metric are:

- **Vendor name:** `Distance per Minute`, in m/min, miles/min, or yd/min ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Average work rate.
- **Window or phase:** None. Catapult One quotes 100 to 120 m/min as typical for professional matches. That is a reference value, not a threshold ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **Calculation:**
  - Vendor definition (paraphrased): Metres per minute as an overall view of how hard the player worked ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: `Distance ÷ Duration (min)`. Catapult One does not state the formula. This is a reading of the name and unit by this page.
- **Inputs:** Distance, duration.
- **Units:** m/min, miles/min, yd/min.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: See `Meterage Per Minute`.
- **What changes the number:** Session edges.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

#### `Top Speed` (Catapult One)

The fields for this metric are:

- **Vendor name:** `Top Speed`, in m/s, km/h, mph, or yd/min ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** The fastest speed the player held.
- **Window or phase:** 0.5 s minimum hold.
- **Calculation:**
  - Vendor definition (paraphrased): The maximum speed sustained for at least half a second ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: `Top Speed = max over t of min(v) across any 0.5 s window starting at t`. This is one reading of "sustained". Catapult does not publish the exact windowing.
- **Inputs:** GNSS velocity.
- **Units:** As listed above.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon `Max. Speed` ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Kinexon's hold rule is Not published.
- **What changes the number:** The 0.5 s rule lowers the value compared with a single-sample peak.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

#### `Work Ratio` (Catapult One, %)

The fields for this metric are:

- **Vendor name:** `Work Ratio`, in % ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** The share of time the player was moving with purpose.
- **Window or phase:** 1.5 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): The percentage of total time spent working, where work is walking or running faster than 1.5 m/s ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: `Work Ratio = 100 × T(v > 1.5 m/s) ÷ total time`.
- **Inputs:** GNSS velocity.
- **Units:** %.
- **Variants:** Vector Core `Work/Rest Ratio` is a different formula with different thresholds. Do not compare them.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Session edges.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

### Velocity bands

**Default velocity bands**

Vector Core publishes six default bands ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)):

| Band | Vector Core name | Default range (m/s) |
|---|---|---|
| 1 | `Standing Distance` | 0 to 0.2 |
| 2 | `Walking Distance` | 0.2 to 2 |
| 3 | `Jogging Distance` | 2 to 4 |
| 4 | `Running Distance` | 4 to 5.5 |
| 5 | `HI Distance` | 5.5 to 7 |
| 6 | `Sprint Distance` | above 7 |

Other facts about velocity bands:

- Vector Core allows up to six velocity bands. Set unused bands to 0. The exit value of one band must equal the entry value of the next ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
- OpenField allows up to eight speed bands ([Catapult Glossary](https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary)). The Connect API reports velocity effort bands 1 to 8 ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)). OpenField does not publish default values on its public Bands page ([Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands)).
- A Catapult best-practice page shows the same six values as an example of absolute bands, not as a default ([Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene)).
- Bands can be relative. Tick **Use Percentage** to set bands as a percentage of each athlete's profile max ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)). In OpenField, relative bands live in a second set called `Velocity (Set 2)`, so absolute and relative bands can run side by side ([How to Set Absolute and Relative Velocity Bands](https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands)).
- The Vector Core intensity trace colours speed from white below 2 m/s to red above 7 m/s. This is a display setting and does not change any metric ([Heatmaps and Intensity Traces](https://core.catapultsports.com/hc/en-us/articles/8600354543887-Heatmaps-and-Intensity-Traces)).
- Whether a band includes its lower edge or upper edge is Not published. The worked examples include the lower edge and exclude the upper edge.
- How Catapult assigns the distance of a sample that sits across a band edge is Not published.

#### `Standing Distance` (m), Velocity Band 1

The fields for this metric are:

- **Vendor name:** `Standing Distance`.
- **What it measures:** Distance covered while nearly still.
- **Window or phase:** 0 to 0.2 m/s ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 1 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for samples with `0 ≤ vᵢ < 0.2 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V1 Dist` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)). Relative version if you use percentage bands.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band edges, reprocessing, velocity noise near zero.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions).

#### `Walking Distance` (m), Velocity Band 2

The fields for this metric are:

- **Vendor name:** `Walking Distance`.
- **What it measures:** Distance covered while walking.
- **Window or phase:** 0.2 to 2 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 2 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for `0.2 ≤ vᵢ < 2 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V2 Dist`.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band edges, reprocessing.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Jogging Distance` (m), Velocity Band 3

The fields for this metric are:

- **Vendor name:** `Jogging Distance`.
- **What it measures:** Distance covered while jogging.
- **Window or phase:** 2 to 4 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 3 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for `2 ≤ vᵢ < 4 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V3 Dist`.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band edges, reprocessing.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Running Distance` (m), Velocity Band 4

The fields for this metric are:

- **Vendor name:** `Running Distance`.
- **What it measures:** Distance covered at moderate running speed.
- **Window or phase:** 4 to 5.5 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 4 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for `4 ≤ vᵢ < 5.5 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V4 Dist`.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band edges, reprocessing.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `HI Distance` (m), Velocity Band 5

The fields for this metric are:

- **Vendor name:** `HI Distance`.
- **What it measures:** Distance covered at high running speed, below sprint speed.
- **Window or phase:** 5.5 to 7 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 5 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for `5.5 ≤ vᵢ < 7 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V5 Dist`.
- **Comparison with standard methods or other vendors:** Standard methods: A peer-reviewed study of effort detection used 4.17 m/s for high-speed running and 7.00 m/s for sprinting. It showed that filter choice and minimum duration change effort counts ([Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534)). That study's thresholds differ from Catapult's 5.5 m/s default. Other vendors: Kinexon lists `High-Speed Distance` as distance over a speed threshold. The threshold value is Not published ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)).
- **What changes the number:** Band edges, reprocessing, velocity filtering.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Sprint Distance` (m), Velocity Band 6

The fields for this metric are:

- **Vendor name:** `Sprint Distance`.
- **What it measures:** Distance covered at sprint speed.
- **Window or phase:** Above 7 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Distance covered in Velocity Band 6 ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Σ dᵢ` for `vᵢ ≥ 7 m/s`.
- **Inputs:** Velocity and distance.
- **Units:** m.
- **Variants:** Live `V6 Dist`. `Sprint Dist Per Min`. Catapult One `Sprint Distance` uses a different threshold (see below).
- **Comparison with standard methods or other vendors:** Standard methods: See `HI Distance`. Other vendors: Kinexon `Sprints` are runs over a speed threshold. The threshold is Not published ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)).
- **What changes the number:** Band edges, reprocessing, velocity filtering. Whether banded distance needs a minimum time in band is Not published. Worked example 1 counts every sample above 7 m/s: 49.56 m.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `HS Distance` (m)

The fields for this metric are:

- **Vendor name:** `HS Distance` (post-activity). Live: `High Speed Distance`, abbreviated `HSR Dist` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** All distance at high speed and sprint speed together.
- **Window or phase:** Bands 5 and 6 (above 5.5 m/s). On Vector 7 Bluetooth activities, Pro users can change which bands count ([Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7)).
- **Calculation:**
  - Vendor definition (paraphrased): The sum of distance in Velocity Band 5 and Velocity Band 6. By default, distance above 5.5 m/s ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). The load score article states `HS Distance = HI Distance + Sprint Distance` ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `HS Distance = HI Distance + Sprint Distance`.
- **Inputs:** Banded distances.
- **Units:** m.
- **Variants:** `HS Dist Per Min`. Vector Live custom `High Speed` and `Very High Speed` parameters (see below).
- **Comparison with standard methods or other vendors:** Standard methods: See `HI Distance`. Other vendors: Kinexon `High-Speed Distance` ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Threshold Not published.
- **What changes the number:** Which bands you include. Band edges. Worked example 1 gives 102.67 m.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `HS Dist Per Min` (m/min)

The fields for this metric are:

- **Vendor name:** `HS Dist Per Min`. In the load score formula: `HS Dist Per Minute`.
- **What it measures:** High-speed running rate.
- **Window or phase:** Above 5.5 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): The Band 5 plus Band 6 distance per minute ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Stated as `(HI Distance + Sprint Distance) / Duration` ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `HS Dist Per Min = HS Distance ÷ Duration (min)`.
- **Inputs:** `HS Distance`, `Duration`.
- **Units:** m/min.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Band edges, period edges.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load).

#### `Sprint Dist Per Min` (m/min)

The fields for this metric are:

- **Vendor name:** `Sprint Dist Per Min`.
- **What it measures:** Sprint distance rate.
- **Window or phase:** Above 7 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): Band 6 distance per minute ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Sprint Distance ÷ Duration (min)`.
- **Inputs:** `Sprint Distance`, `Duration`.
- **Units:** m/min.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Band edges, period edges.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Sprint Efforts` (count)

The fields for this metric are:

- **Vendor name:** `Sprint Efforts`. Live: `Sprint Eff` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** How many separate sprints the athlete made.
- **Window or phase:** Band 6, above 7 m/s.
- **Calculation:**
  - Vendor definition (paraphrased): The number of efforts in Velocity Band 6, above 7 m/s by default ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: The count of separate entries into Band 6 that meet Catapult's effort rules. The effort rules (minimum time in band, called dwell time) are on a sign-in page and are Not published publicly.
- **Inputs:** Velocity.
- **Units:** Count.
- **Variants:** Effort details per sprint in the Efforts Breakdown (see `Velocity effort attributes`). Velocity efforts can be counted per band in Vector 7 live (`V2+ Eff`, `V3+ Eff`, and so on) ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **Comparison with standard methods or other vendors:** Standard methods: A peer-reviewed study showed that minimum effort duration (0.1 to 0.9 s) and the velocity filter change sprint counts ([Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534)). Other vendors: Kinexon `Sprints` ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Threshold and minimum duration Not published.
- **What changes the number:** Dwell time, filtering, band edges. Worked example 1 has one long sprint and one 0.5 s surge above 7 m/s. With no minimum time in band, the count is 2. With a 1.0 s minimum, the count is 1.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7), [Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `HS Efforts` (count)

The fields for this metric are:

- **Vendor name:** `HS Efforts`. Live: `High Speed Efforts`, abbreviated `HS Eff` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** How many separate high-speed runs the athlete made.
- **Window or phase:** Band 5 and above. Vector 7 Bluetooth activities let Pro users change the bands ([Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7)).
- **Calculation:**
  - Vendor definition (paraphrased): The number of efforts in Band 5 or Band 6, above 5.5 m/s by default ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). The live app describes it as a count of efforts in band 5 and above ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
  - Restatement, not a vendor statement: The count of separate entries above the Band 5 lower edge. The effort rules are Not published publicly.
- **Inputs:** Velocity.
- **Units:** Count.
- **Variants:** None beyond band choice.
- **Comparison with standard methods or other vendors:** Standard methods: See `Sprint Efforts`. Other vendors: Not published.
- **What changes the number:** Dwell time, filtering, band edges. Whether a run that climbs from Band 5 into Band 6 counts once or twice is Not published. Worked example 1 gives 2 at both 0 s and 1.0 s minimum duration.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7).

#### `Velocity Distance Band 1 - 8` (m), live

The fields for this metric are:

- **Vendor name:** `Velocity Distance Band 1 - 8`, abbreviated `V1 Dist`, `V2 Dist`, and so on. Each band is its own parameter ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)). The Vector Core live app lists bands 1 to 6 ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** Live distance in each speed band.
- **Window or phase:** As set in Bands.
- **Calculation:**
  - Vendor definition (paraphrased): Total distance in each band ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
  - Restatement, not a vendor statement: Same as the post-activity banded distances, computed live.
- **Inputs:** Live velocity.
- **Units:** m.
- **Variants:** Post-activity banded distances.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Live packet loss. Device band settings, which update only after a sync ([Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands)).
- **Source links:** [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7), [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands).

#### `Velocity Efforts Band 2+` (count), live

The fields for this metric are:

- **Vendor name:** `Velocity Efforts Band 2+`, abbreviated `V2+ Eff`, `V3+ Eff`, and so on ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **What it measures:** Live count of efforts in each band.
- **Window or phase:** As set in Bands.
- **Calculation:**
  - Vendor definition (paraphrased): A count of efforts in each band ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
  - Restatement, not a vendor statement: The "+" in the name suggests "this band or higher". The Catapult page does not state it.
- **Inputs:** Live velocity.
- **Units:** Count.
- **Variants:** `HS Efforts`, `Sprint Efforts`.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Dwell rules (Not published), packet loss, band settings.
- **Source links:** [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7).

#### `Velocity (Set 2)` banded metrics (relative bands)

The fields for this metric are:

- **Vendor name:** `Velocity (Set 2)`, a second band set in OpenField ([How to Set Absolute and Relative Velocity Bands](https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands)).
- **What it measures:** The same banded distances, durations, and efforts, but against each athlete's own maximum.
- **Window or phase:** Not published. A Catapult best-practice page gives an example relative scheme: Band 1 from 0 to maximal aerobic speed (MAS), Band 2 from MAS to 30% of anaerobic speed reserve (ASR), Band 3 above 30% ASR up to maximum sprint speed. It is an example only ([Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene)).
- **Calculation:**
  - Vendor definition (paraphrased): A second band set used to report velocity efforts, distance, and duration in relative terms, using a percentage of each athlete's max velocity ([How to Set Absolute and Relative Velocity Bands](https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands)).
  - Restatement, not a vendor statement: `Band edge (m/s) = edge (%) × profile max velocity ÷ 100`. Then the band metrics work as above.
- **Inputs:** Velocity, athlete profile max velocity.
- **Units:** m, s, count.
- **Variants:** Absolute set (`Velocity`).
- **Comparison with standard methods or other vendors:** Standard methods: Catapult's own article on individualised thresholds warns that anchoring all zones to peak sprint speed can over- or under-estimate high-speed running. It points to methods that combine maximal aerobic speed and peak speed ([Individualisation of GPS speed thresholds](https://www.catapult.com/blog/individualisation-gps-speed-thresholds-challenges-complexities)). Other vendors: Kinexon product copy mentions analysing relative and absolute workload by intensity zone. Zone values are Not published ([Kinexon PERFORM LPS](https://kinexon-sports.com/products/perform-lps/)).
- **What changes the number:** Profile max velocity. First use of Set 2 needs reprocessing of history ([How to Set Absolute and Relative Velocity Bands](https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands)). Set 2 efforts do not appear in the Efforts Breakdown ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)).
- **Source links:** [How to Set Absolute and Relative Velocity Bands](https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands), [Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene), [Individualisation of GPS speed thresholds](https://www.catapult.com/blog/individualisation-gps-speed-thresholds-challenges-complexities), [Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown), [Kinexon PERFORM LPS](https://kinexon-sports.com/products/perform-lps/).

#### Vector Live custom speed parameters

The fields for this metric are:

- **Vendor name:** `High Speed` and `Very High Speed`, each with `Duration`, `Duration %`, `Distance`, `Distance %`, `Effort` (count), and `Effort %` ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
- **What it measures:** Time, distance, and efforts in user-chosen high-speed bands, live.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Pre-filled custom parameters built from velocity bands. You choose which bands to include ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
  - Restatement, not a vendor statement: `Distance % = 100 × distance in chosen bands ÷ total distance`, and the same pattern for duration and efforts. The Catapult page lists the names only. The percentage formula is a reading by this page.
- **Inputs:** Live velocity.
- **Units:** s, %, m, count.
- **Variants:** Cloud custom parameters. Catapult advises matching live and Cloud band choices so values agree ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Band selection.
- **Source links:** [Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App).

#### Velocity effort attributes (Efforts Breakdown and Connect API)

The fields for this metric are:

- **Vendor name:** In OpenField Cloud's Efforts Breakdown: `Duration`, `Start Time`, `Start Velocity`, `Max Velocity`, `Distance`, `Percent of Max`, `Time since last` ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)). In the Connect API: `start_time`, `end_time`, `band` (1 to 8), `start_velocity`, `end_velocity`, `max_velocity`, `distance` ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)).
- **What it measures:** The profile of each single speed effort.
- **Window or phase:** Effort detection rules Not published publicly.
- **Calculation:**
  - Vendor definition (paraphrased): Duration is start to end of the effort in seconds. Percent of Max is the effort's max velocity as a share of the athlete's profile max. Time since last is the time since the previous effort in the same band ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)).
  - Restatement, not a vendor statement: Per effort `k`: `Duration_k = end_k − start_k`, `Percent of Max_k = 100 × max(v in effort k) ÷ profile max`.
- **Inputs:** 10 Hz velocity.
- **Units:** Connect API: UNIX timestamps with milliseconds, m/s, and m ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)). Efforts Breakdown: seconds and % ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)).
- **Variants:** Only Velocity Gen2 Set 1 efforts appear. Set 2 and Gen1 efforts do not ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)). The Efforts Breakdown is part of Vector Pro and Core+, with a 10 Hz velocity trace and a field map of where each effort happened ([Efforts Breakdown blog](https://www.catapult.com/blog/vector-efforts-breakdown-game-speed-insights)).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** The breakdown shows all efforts above each band threshold by default, so it can look like more efforts than you expect. Catapult advises filtering to one band ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)).
- **Source links:** [Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown), [Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data), [Efforts Breakdown blog](https://www.catapult.com/blog/vector-efforts-breakdown-game-speed-insights).

#### `Sprint Distance` (Catapult One)

The fields for this metric are:

- **Vendor name:** `Sprint Distance`, in m or yds ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Distance at sprint speed.
- **Window or phase:** 5 m/s, held 1 s. You cannot change the threshold in the app ([Can I adjust my sprint speed threshold?](https://onesupport.catapultsports.com/hc/en-us/articles/9436643027471-Can-I-adjust-my-sprint-speed-threshold)).
- **Calculation:**
  - Vendor definition (paraphrased): Distance in speed zones 4 and 5. Sprinting is above 5 m/s by default ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)). A help article adds that the athlete must be above 5 m/s (18 km/h) for at least 1 second ([How is sprint distance measured?](https://onesupport.catapultsports.com/hc/en-us/articles/9436632476303-How-is-sprint-distance-measured)).
  - Restatement, not a vendor statement: `Σ dᵢ` while `v > 5 m/s` within runs that last at least 1 s.
- **Inputs:** GNSS velocity.
- **Units:** m, yds.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Do not compare with Vector `Sprint Distance` (above 7 m/s by default).
- **What changes the number:** Catapult sources disagree on the threshold. One Catapult One page gives 7 m/s ([Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation)). Two give 5 m/s ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Know your core metrics](https://one.catapultsports.com/blog/know-your-metrics/)). Treat the threshold as unconfirmed for older app versions. Recalculate sessions after zone changes ([How to Recalculate a Session](https://onesupport.catapultsports.com/hc/en-us/articles/7443890603919-How-to-Recalculate-a-Session)).
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [How is sprint distance measured?](https://onesupport.catapultsports.com/hc/en-us/articles/9436632476303-How-is-sprint-distance-measured), [Can I adjust my sprint speed threshold?](https://onesupport.catapultsports.com/hc/en-us/articles/9436643027471-Can-I-adjust-my-sprint-speed-threshold), [Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation), [Know your core metrics](https://one.catapultsports.com/blog/know-your-metrics/), [How to Recalculate a Session](https://onesupport.catapultsports.com/hc/en-us/articles/7443890603919-How-to-Recalculate-a-Session).

### Accelerations and decelerations

**Default acceleration bands**

Catapult publishes these facts about acceleration bands:

- The default threshold for acceleration and deceleration efforts is 2 m/s² ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- The `Gen2Acceleration` band set has three deceleration bands and three acceleration bands. Bands 1 to 3 are decelerations, from highest to lowest intensity. Bands 6 to 8 are accelerations, from lowest to highest intensity. Bands 4 and 5 touch zero and are blocked from reporting because acceleration is noisy near zero ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
- `Accelerations` are the sum of Band 6 to 8 efforts. `Decelerations` are the sum of Band 1 to 3 efforts. Decelerations are entered as negative numbers ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)).
- To move the acceleration threshold below 3 m/s², edit Band 5. Between 3 and 4 m/s², edit Bands 5 and 6. Above 4 m/s², edit Bands 5, 6, and 7 ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)). Reading, not stated by the vendor: the default edges between acceleration bands sit near 3 and 4 m/s². The Catapult page does not print the full default table.
- The Connect API reports acceleration effort bands from −3 to 3 ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)).
- The Gen2 effort rules exclude movements shorter than 0.9 s ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
- The full Gen2 acceleration definition, the Gen1 definition, and the LPS (TDOA) acceleration effort algorithm are on sign-in pages. See [Pages not publicly readable](#pages-not-publicly-readable).
- Acceleration is the derivative of velocity, and Catapult notes it can come from GNSS or from accelerometers ([Catapult Glossary](https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary)). For the efforts below, the source is velocity-derived. Metabolic power uses GPS acceleration explicitly ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)).

#### `Max Acceleration` (m/s²)

The fields for this metric are:

- **Vendor name:** `Max Acceleration`, in m/s/s.
- **What it measures:** The hardest acceleration in the period.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The peak value of any single maximal acceleration, in m/s/s ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Max Acceleration = max(aᵢ)`, where `aᵢ` is acceleration derived from filtered velocity. The filter is Not published.
- **Inputs:** Velocity (GNSS or LPS).
- **Units:** m/s².
- **Variants:** Catapult One `Max Acceleration` (requires 1 s above a threshold). Per-effort `Max Accel` in effort tables.
- **Comparison with standard methods or other vendors:** Standard methods: A peer-reviewed study showed that the time interval used to derive acceleration (0.2 s or 0.3 s) and the filter change acceleration results ([Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534)). Other vendors: Not published.
- **What changes the number:** Velocity filter and derivative window. In worked example 1, the raw first difference gives 2.50 m/s².
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534).

#### `Max Deceleration` (m/s²)

The fields for this metric are:

- **Vendor name:** `Max Deceleration`, in m/s/s.
- **What it measures:** The hardest deceleration in the period.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The peak value of any single maximal deceleration ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Max Deceleration = min(aᵢ)` (the most negative value). Whether Catapult displays it as a positive or negative number is Not published.
- **Inputs:** Velocity.
- **Units:** m/s².
- **Variants:** Catapult One `Max Deceleration`.
- **Comparison with standard methods or other vendors:** Standard methods: See `Max Acceleration`. Other vendors: Not published.
- **What changes the number:** Filter and derivative window. Worked example 1 gives −3.00 m/s².
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Acceleration Efforts` (count)

The fields for this metric are:

- **Vendor name:** `Acceleration Efforts` (Vector Core post-activity). Live: `Acceleration Total Efforts B1 -3 (Gen2)`, abbreviated `Acc` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)); `Accelerations`, abbreviated `Acc` on Vector 7 ([Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **What it measures:** How many hard speed-ups the athlete made.
- **Window or phase:** 2 m/s². On Vector 7 Bluetooth activities, Catapult says Accelerations and Decelerations each default to bands 1 to 3 ([Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7)). This numbering differs from the `Gen2Acceleration` numbering, where accelerations are Bands 6 to 8 ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)).
- **Calculation:**
  - Vendor definition (paraphrased): A count of acceleration efforts, above 2 m/s/s by default ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Equal to the sum of Band 6 to 8 efforts ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)).
  - Restatement, not a vendor statement: The number of separate runs where `a > 2 m/s²` that last at least 0.9 s ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)). Other parts of the Gen2 rule set are Not published.
- **Inputs:** Velocity.
- **Units:** Count.
- **Variants:** Banded counts per acceleration band. Per-effort attributes (below). `Accel&Decel Efforts`.
- **Comparison with standard methods or other vendors:** Standard methods: A peer-reviewed study tested an acceleration threshold of 2.78 m/s² with minimum durations from 0.1 to 0.9 s. Filter and minimum duration both changed the count ([Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534)). Other vendors: Kinexon puts each acceleration into an intensity band, multiplies it by a proprietary weight, and sums the result as `Accel Load` ([Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Catapult counts efforts. One is a weighted load, one is a count, so the numbers are not interchangeable.
- **What changes the number:** Threshold, minimum duration, velocity filter, band edits, reprocessing. Worked example 1 has a 2 s acceleration at 2.5 m/s² and a 0.3 s burst at about 2.3 m/s². With no minimum duration the count is 2. With the 0.9 s minimum the count is 1. A 0.5 s moving average on speed also drops the count to 1.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands), [Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index), [Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7), [Varley et al. 2017](https://doi.org/10.1123/ijspp.2016-0534), [Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/).

#### `Deceleration Efforts` (count)

The fields for this metric are:

- **Vendor name:** `Deceleration Efforts`. Live: `Deceleration Total Efforts B1 -3 (Gen2)` or `Decelerations`, abbreviated `Dcc` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **What it measures:** How many hard slow-downs the athlete made.
- **Window or phase:** 2 m/s² (entered as −2).
- **Calculation:**
  - Vendor definition (paraphrased): A count of deceleration efforts, above 2 m/s/s by default ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Equal to the sum of Band 1 to 3 efforts ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)).
  - Restatement, not a vendor statement: The number of separate runs where `a < −2 m/s²` that last at least 0.9 s. Other rule details are Not published.
- **Inputs:** Velocity.
- **Units:** Count.
- **Variants:** Banded counts. `Accel&Decel Efforts`.
- **Comparison with standard methods or other vendors:** Standard methods: See `Acceleration Efforts`. Other vendors: Kinexon `Decel Load` is a weighted sum by intensity band ([Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Not interchangeable with a count.
- **What changes the number:** As for `Acceleration Efforts`. Worked example 1 gives 1.
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands), [Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/).

#### `Accel&Decel Efforts` (count)

The fields for this metric are:

- **Vendor name:** `Accel&Decel Efforts`. In the load score formula: `Accel+Decel Efforts`.
- **What it measures:** All hard speed changes together.
- **Window or phase:** 2 m/s².
- **Calculation:**
  - Vendor definition (paraphrased): The sum of acceleration and deceleration efforts ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `Accel&Decel Efforts = Acceleration Efforts + Deceleration Efforts`.
- **Inputs:** Effort counts.
- **Units:** Count.
- **Variants:** Per minute (next block).
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon `Mechanical Load` is `Accel Load + Decel Load`, each a weighted sum ([Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Another Kinexon article describes Mechanical Load more broadly, including running distances, sprints, and changes of direction ([Kinexon: bowl season data](https://kinexon-sports.com/blog/sports-performance-data-bowl-season/)). Not interchangeable with a count.
- **What changes the number:** As for the two effort counts. Worked example 1 gives 3 with no minimum duration and 2 with the 0.9 s minimum.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/), [Kinexon: bowl season data](https://kinexon-sports.com/blog/sports-performance-data-bowl-season/).

#### `Accel&Decel Efforts Per Minute` (count/min)

The fields for this metric are:

- **Vendor name:** `Accel&Decel Efforts Per Minute`. In the load score formula: `Accel+Decel Eff Per Minute`.
- **What it measures:** How often hard speed changes happen.
- **Window or phase:** 2 m/s².
- **Calculation:**
  - Vendor definition (paraphrased): The sum of acceleration and deceleration efforts divided by time in minutes ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)). Stated as `(Acceleration Efforts + Deceleration Efforts) / Duration` ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `Accel&Decel Efforts ÷ Duration (min)`.
- **Inputs:** Effort counts, duration.
- **Units:** Efforts per minute.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon `Mechanical Intensity` is total Mechanical Load divided by time ([Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/)). Weighted load per minute is not the same as a count per minute.
- **What changes the number:** Effort rules and period edges.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Kinexon: Mechanical Load in basketball](https://kinexon-sports.com/blog/mechanical-load-basketball/).

#### Acceleration effort attributes (effort tables and Connect API)

The fields for this metric are:

- **Vendor name:** OpenField Console `Acceleration Efforts (Gen2) Table`: `Duration`, `Start Vel`, `Max Accel`, `Distance`, `Time Since Last` ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)). Efforts Breakdown also shows `Acceleration` ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)). Connect API: `start_time`, `end_time`, `band` (−3 to 3), `acceleration` (m/s/s), `distance` ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)).
- **What it measures:** The profile of each single acceleration or deceleration.
- **Window or phase:** As set in `Gen2Acceleration` bands.
- **Calculation:**
  - Vendor definition (paraphrased): Duration is the effort length in seconds. Start Vel is the speed when detection started. Max Accel is the peak value in m/s². Distance is the effort distance in metres. Time Since Last is the time from the previous effort, counting all efforts regardless of band ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)).
  - Restatement, not a vendor statement: Per effort `k`: `Max Accel_k = max |a|` within the effort, signed.
- **Inputs:** Velocity.
- **Units:** s, user speed units, m/s², m.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Catapult defines `Time Since Last` two ways. The Console table counts all efforts regardless of band ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)). The Cloud Efforts Breakdown counts the previous effort in the same band ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)). Check which view produced your export.
- **Source links:** [Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events), [Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown), [Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data).

#### `Acceleration load` (sum of absolute acceleration)

The fields for this metric are:

- **Vendor name:** `Acceleration load` ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
- **What it measures:** The total amount of speeding up and slowing down, with no threshold.
- **Window or phase:** None. No minimum duration ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
- **Calculation:**
  - Vendor definition (paraphrased): The accumulation of absolute acceleration values, derived from smoothed velocity and sampled at 10 Hz. Accelerations and decelerations count equally ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
  - Restatement, not a vendor statement: `Acceleration load = Σ |aᵢ|` over 10 Hz samples. Whether Catapult multiplies each term by the 0.1 s sample time is Not published, so the unit is Not published.
- **Inputs:** Smoothed velocity at 10 Hz.
- **Units:** Not published.
- **Variants:** `Acceleration density`, `Acceleration density index`.
- **Comparison with standard methods or other vendors:** Standard methods: Catapult says the metric followed Duthie and Delaney (2015) on acceleration-based running intensities in rugby league ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)). The matching Crossref record is Delaney, Duthie, et al., published 2016 in IJSPP ([Delaney et al. 2016](https://doi.org/10.1123/ijspp.2015-0424)). That study used average acceleration over moving windows. Other vendors: Kinexon `Accumulated Acceleration Load` sounds similar but is described as based on a three-dimensional acceleration pattern from the IMU ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Catapult `Acceleration load` uses speed-derived acceleration. The inputs differ, so the numbers are not interchangeable.
- **What changes the number:** The velocity smoothing method (Not published). Period edges.
- **Source links:** [Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index), [Delaney et al. 2016](https://doi.org/10.1123/ijspp.2015-0424), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Acceleration density` (mean absolute acceleration)

The fields for this metric are:

- **Vendor name:** `Acceleration density`. Shown as `Acc Density` in a Catapult example table ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
- **What it measures:** How intense the speed changes were on average.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The average of absolute acceleration values over the period, which is acceleration load over time ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
  - Restatement, not a vendor statement: `Acceleration density = mean(|aᵢ|)`.
- **Inputs:** Smoothed velocity.
- **Units:** Not published. If the mean is taken over samples, the unit is m/s².
- **Variants:** `Acceleration density index`.
- **Comparison with standard methods or other vendors:** See `Acceleration load`.
- **What changes the number:** Smoothing, period edges, rest time. Worked example 1 gives 0.354 m/s² with no smoothing.
- **Source links:** [Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index).

#### `Acceleration density index` (per 10 m)

The fields for this metric are:

- **Vendor name:** `Acceleration density index`. Shown as `Acc Density Index` in an example ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
- **What it measures:** Speed-change intensity during movement only, ignoring rest time.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Acceleration load per 10 m of distance covered ([Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index)).
  - Restatement, not a vendor statement: `Acceleration density index = Acceleration load ÷ (Distance ÷ 10)`.
- **Inputs:** `Acceleration load`, `Distance`.
- **Units:** Not published.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Standard methods: See `Acceleration load`. Other vendors: Not published.
- **What changes the number:** Smoothing, distance quality.
- **Source links:** [Acceleration load, density, and density index](https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index).

#### `Max Acceleration` and `Max Deceleration` (Catapult One)

The fields for this metric are:

- **Vendor name:** `Max Acceleration` and `Max Deceleration`, in m/s/s ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** The hardest speed-up and slow-down the player held.
- **Window or phase:** 1 s minimum. Threshold Not published.
- **Calculation:**
  - Vendor definition (paraphrased): How quickly the player can accelerate (or decelerate) above the acceleration threshold for at least 1 second ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: A peak value taken only from efforts that stay past the threshold for at least 1 s. The threshold value is Not published.
- **Inputs:** GNSS velocity.
- **Units:** m/s².
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The 1 s rule makes this lower than a single-sample peak.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

### PlayerLoad and accelerometer load

#### `Player Load` (AU)

The fields for this metric are:

- **Vendor name:** `Player Load`, abbreviated `PL`. Catapult also writes `PlayerLoad` ([Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)).
- **What it measures:** Total body movement work from the accelerometer, including work that is not running, such as tackles and rucks.
- **Window or phase:** None for the total. Player Load bands can be set in OpenField ([What is Player Load? (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load)). Default band values are Not published.
- **Calculation:**
  - Vendor definition (paraphrased): The sum of accelerations across all three axes of the tri-axial accelerometer during movement. It uses the instantaneous rate of change of acceleration and divides by a scaling factor of 100 ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load), [What is Player Load? (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load)).
  - Formula as Catapult publishes it (accumulated): `PlayerLoad = Σ_{i=1}^{n} √[ (ax_i − ax_{i−1})² + (ay_i − ay_{i−1})² + (az_i − az_{i−1})² ]`, where `ax`, `ay`, and `az` are the accelerations on the x, y, and z axes, and `i = 0 … n` indexes the `n + 1` accelerometer samples ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
  - Formula as Catapult publishes it (instantaneous): `Plyr.Load = √[ (fwd_{t=i+1} − fwd_{t=i})² + (side_{t=i+1} − side_{t=i})² + (up_{t=i+1} − up_{t=i})² ]`, where `fwd`, `side`, and `up` are forward, sideways, and upward acceleration and `t` is time ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
  - Restatement, not a vendor statement: For each pair of neighbouring 100 Hz samples, take the change in acceleration on each axis. Combine the three changes with Pythagoras. Add these over the session. Divide by 100. The formula image does not show the ÷100. The text does ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
- **Inputs:** Tri-axial accelerometer. On the X7, 400 Hz smoothed to 100 Hz ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
- **Units:** Arbitrary units (AU) ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)). The acceleration unit inside the formula (g or m/s²) is Not published on the Catapult page. The worked example assumes g.
- **Variants:** `Player Load Per Minute`, instantaneous Player Load, `PlayerLoad 2D`, Player Load bands, Maximum Intensity Player Load intervals, Catapult One `Player Load`.
- **Comparison with standard methods or other vendors:** Standard methods: Catapult says the formula was developed at the Australian Institute of Sport for rugby union and cites three supporting papers ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)). The three papers are: [Scott et al. 2013](https://doi.org/10.1123/ijspp.8.2.195), [Colby et al. 2014](https://doi.org/10.1519/JSC.0000000000000362), [Barron et al. 2014](https://doi.org/10.1080/24748668.2014.11868754). A reliability study on Catapult MinimaxX devices reported within-device and between-device CVs near 1% in the lab and 1.9% between devices in matches ([Boyd et al. 2011](https://doi.org/10.1123/ijspp.6.3.311)). Other vendors: Kinexon `Accumulated Acceleration Load` is described as a volume metric based on a three-dimensional IMU acceleration pattern ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Kinexon does not publish its formula, so you cannot convert between the two.
- **What changes the number:**
  - Running style: Catapult says Player Load is dominated by running impacts and is not directly comparable between players. Players with similar match distance can range from 400 to 800 ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
  - Device position: In treadmill running, Player Load was higher at the centre of mass than at the scapulae (223.4 versus 185.5 AU), and the vertical axis contributed about 55.7% at the scapulae ([Barrett et al. 2014](https://doi.org/10.1123/ijspp.2013-0418)).
  - Device fit and orientation: A loose vest or a device mounted the wrong way gives wrong inertial data ([Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene)).
  - Sampling and smoothing: The 400 Hz to 100 Hz smoothing method is Not published. In worked example 2, decimating the same signal from 100 Hz to 50 Hz drops Player Load from 1.491 to 1.123 AU.
  - Scaling: Without the ÷100, worked example 2 gives 149.1 instead of 1.491.
  - A constant offset such as gravity cancels out because the formula uses sample-to-sample changes. Worked example 2 shows the same 1.491 AU with and without a 1 g offset.
- **Source links:** [Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work), [What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load), [What is Player Load? (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load), [Scott et al. 2013](https://doi.org/10.1123/ijspp.8.2.195), [Colby et al. 2014](https://doi.org/10.1519/JSC.0000000000000362), [Barron et al. 2014](https://doi.org/10.1080/24748668.2014.11868754), [Boyd et al. 2011](https://doi.org/10.1123/ijspp.6.3.311), [Barrett et al. 2014](https://doi.org/10.1123/ijspp.2013-0418), [Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Player Load Per Minute` (AU/min)

The fields for this metric are:

- **Vendor name:** `Player Load Per Minute`.
- **What it measures:** Movement work rate.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Player load divided by time in minutes ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Player Load ÷ Duration (min)`.
- **Inputs:** `Player Load`, `Duration`.
- **Units:** AU/min.
- **Variants:** Player Load per unit distance. Catapult describes PL per distance or per time as an indicator of movement efficiency ([Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)).
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon lists `Accumulated Acceleration Load per minute` as an intensity metric ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Not interchangeable (see `Player Load`).
- **What changes the number:** The time window. In ice hockey, studies that divided by total game time reported about 2.1 to 2.3 PL/min. Studies that divided by time on ice reported about 6.3 PL/min ([Ice Hockey Auto Shift Detection](https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads)). Worked example 2 gives 8.947 AU/min (3D).
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work), [Ice Hockey Auto Shift Detection](https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### Instantaneous Player Load (`pli`)

The fields for this metric are:

- **Vendor name:** `pli` (Instantaneous Player Load) in the 10 Hz sensor stream. The stream also has `pl`, Player Load accumulated ([Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity), [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz)).
- **What it measures:** Movement load at each moment.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): See the instantaneous formula under `Player Load` ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
  - Restatement, not a vendor statement: The value of one step of the sum. How the 100 Hz values are summarised into a 10 Hz stream is Not published.
- **Inputs:** Accelerometer.
- **Units:** AU.
- **Variants:** `pl` accumulated.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Stream resampling. The API can resample up to 20 Hz. Upsampling interpolates and adds no measured detail ([Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity)).
- **Source links:** [Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity), [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load).

#### `PlayerLoad 2D` (AU)

The fields for this metric are:

- **Vendor name:** `PlayerLoad 2D` ([Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)).
- **What it measures:** Player Load without the up-and-down component, for sports with short distances or tight spaces.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Player Load with the vertical accelerometer axis left out of the calculation ([Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work)).
  - Restatement, not a vendor statement: `PlayerLoad 2D = Σ √[ (fwd_i − fwd_{i−1})² + (side_i − side_{i−1})² ] ÷ 100`.
- **Inputs:** Forward and sideways accelerometer axes.
- **Units:** AU.
- **Variants:** 3D `Player Load`.
- **Comparison with standard methods or other vendors:** Standard methods: Barrett et al. reported plane-by-plane contributions (anteroposterior, mediolateral, vertical) to Player Load ([Barrett et al. 2014](https://doi.org/10.1123/ijspp.2013-0418)). Catapult does not state that 2D uses the same method. Other vendors: Not published.
- **What changes the number:** Device orientation and mounting. A waist-front device has its axes inverted during processing ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)). In worked example 2, 2D is 0.934 AU, or 62.6% of the 3D value.
- **Source links:** [Catapult: Understanding Player Load](https://www.catapult.com/blog/fundamentals-playerload-athlete-work), [Barrett et al. 2014](https://doi.org/10.1123/ijspp.2013-0418), [Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics).

#### Player Load bands and Vector Live custom Player Load parameters

The fields for this metric are:

- **Vendor name:** Player Load bands in OpenField ([What is Player Load? (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load), [Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands)). Vector Live custom parameters: `High Intensity Player Load` and `Very High Intensity Player Load`, each with `Duration`, `Duration %`, and `Total Accumulation %` ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
- **What it measures:** Time and load spent at high movement intensity.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Custom parameters built from Player Load bands you choose ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
  - Restatement, not a vendor statement: `Duration` = time with instantaneous Player Load inside the chosen bands. `Total Accumulation %` = 100 × Player Load gathered in those bands ÷ total Player Load. The Catapult page gives names only. The formulas are a reading by this page.
- **Inputs:** Instantaneous Player Load.
- **Units:** s, %, AU.
- **Variants:** Cloud custom parameters.
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon `Exertions` count high-intensity activity above an acceleration load threshold ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Both are thresholded accelerometer load. Thresholds are Not published on either side.
- **What changes the number:** Band edges and band selection.
- **Source links:** [What is Player Load? (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load), [Bands (OpenField)](https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands), [Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### Smooth Load (`sl`)

The fields for this metric are:

- **Vendor name:** `sl`, Smooth Load, instantaneous ([Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz)). Several Connect events report values in "smoothed PlayerLoad units" ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
- **What it measures:** A smoothed form of instantaneous Player Load.
- **Window or phase:** Not published.
- **Calculation:** Not published.
- **Inputs:** Accelerometer.
- **Units:** Smoothed PlayerLoad units.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data).

#### `Player Load` (Catapult One)

The fields for this metric are:

- **Vendor name:** `Player Load` ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Total load on the body from running and impacts.
- **Window or phase:** None.
- **Calculation:** Same formula and same 400 Hz to 100 Hz path as Vector ([What is Player Load? (Catapult One)](https://onesupport.catapultsports.com/hc/en-us/articles/7443837147023-What-is-Player-Load)).
- **Inputs:** Accelerometer.
- **Units:** AU.
- **Variants:** A percentage view against the player's typical game value, once you set that game value ([What is Player Load? (Catapult One)](https://onesupport.catapultsports.com/hc/en-us/articles/7443837147023-What-is-Player-Load)).
- **Comparison with standard methods or other vendors:** See `Player Load`.
- **What changes the number:** See `Player Load`.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [What is Player Load? (Catapult One)](https://onesupport.catapultsports.com/hc/en-us/articles/7443837147023-What-is-Player-Load).

### Metabolic power and HMLD

**How Catapult computes metabolic power**

Catapult publishes this model on its support site ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)):

- **Input:** Acceleration is derived from GPS velocity before any smoothing filter is applied. Catapult then uses a discrete Gaussian filter with a 1 s width. Accelerations above 1 g are excluded as GPS errors. Metabolic power is available outdoors with GNSS only.
- **Model:** Based on Minetti et al. (2002) and Osgnach et al. (cited by Catapult as 2010 in the text and 2009 in its reference list; the Crossref record shows the issue date as 2010-01) ([Minetti et al. 2002](https://doi.org/10.1152/japplphysiol.01177.2001), [Osgnach et al. 2010](https://doi.org/10.1249/MSS.0b013e3181ae5cfd)). Catapult says it uses a revised model designed for team sports. The revisions are Not published.
- **Equivalent slope:** `ES = tan(90 − α)`, where `α` is the angle between the runner and the ground.
- **Equivalent mass:** `EM = g′ ÷ g`, where `g′` is the vector sum of forward acceleration and gravity, and `g` is gravity. Restatement, not a vendor statement: `g′ = √(a_f² + g²)`, where `a_f` is forward acceleration.
- **Energy cost:** `EC (J/kg/m) = fn(ES) × EM × KT`.
- **Terrain constant:** `KT = 1.29`, for the extra cost of grass.
- **Slope polynomial:** `fn = 155.4·ES⁵ − 30.4·ES⁴ − 43.3·ES³ + 46.3·ES² + 19.5·ES + 3.6`.
- **Power:** `MP (W/kg) = EC × v`, where `v` is running speed.

The Catapult page does not state how `α` is computed from forward acceleration. The Osgnach paper describes accelerated running as equivalent to uphill running at a slope set by the acceleration ([Osgnach et al. 2010](https://doi.org/10.1249/MSS.0b013e3181ae5cfd)).

Consistency check (worked example 1b): At constant speed on flat ground, `ES = 0` and `EM = 1`, so `EC = 3.6 × 1.29 = 4.644 J/kg/m`. At 5.5 m/s, `MP = 25.542 W/kg`. This matches Catapult's statement that the 25.5 W/kg HMLD threshold equals running at a constant 5.5 m/s ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).

**Gen 1 versus Gen 2:** Gen 2 metabolic power changed the filtering slightly so it can run live. In Catapult's own two-device test, Gen 2 read less than 1.2% lower for total and banded metrics, and 5.5% lower for peak metabolic power ([What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power)). Gen 2 needs OpenField Console 3.12.0, Vector Live 2.9.0, and device firmware 8.8.0 or later ([What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power), [Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console)).

#### Metabolic Power (`mp`, W/kg)

The fields for this metric are:

- **Vendor name:** `mp`, Metabolic Power, in the 10 Hz stream ([Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz)). OpenField parameter groups `Met Power` and `Metabolic Power Bands` ([Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console)).
- **What it measures:** The estimated energy cost per second of running and speed changes.
- **Window or phase:** Metabolic power bands are user set. Defaults are Not published ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **Calculation:** See the model above ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)).
- **Inputs:** GNSS velocity and GNSS-derived acceleration.
- **Units:** W/kg.
- **Variants:** Average metabolic power, banded time and distance, metabolic power efforts. Their exact OpenField names are on a sign-in page (Not published).
- **Comparison with standard methods or other vendors:** Standard methods: Based on Osgnach and Minetti, with an extra terrain constant of 1.29 and unpublished team-sport revisions ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)). Other vendors: Kinexon lists `Physio Load` as a combination of distance, speed, and body weight ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Its formula is Not published. Do not treat the two as equal.
- **What changes the number:** Gen 1 or Gen 2 processing ([What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power)). The 1 g acceleration cut-off and the 1 s Gaussian filter ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)). GPS only, so no LPS values.
- **Source links:** [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console), [What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power), [Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings), [What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### `Energy`

The fields for this metric are:

- **Vendor name:** `Energy` (Vector Core) ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** Estimated energy used in the session.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The estimated caloric expenditure based on GPS acceleration ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: Likely the time integral of metabolic power times body mass. Catapult does not publish the formula. Not published.
- **Inputs:** GNSS velocity and acceleration. Body mass is likely needed. Not published.
- **Units:** Not published for Vector Core.
- **Variants:** Catapult One `Energy` in kcal.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `High Metabolic Load Distance` (m)

The fields for this metric are:

- **Vendor name:** `High Metabolic Load Distance`, abbreviated HMLD ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **What it measures:** Distance covered while working hard, from fast running or from hard speed changes.
- **Window or phase:** 25.5 W/kg. Set at team level in OpenField Cloud (**Settings > Teams > Edit**). Gen 2 lets you set it apart from metabolic power bands ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings), [What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power)).
- **Calculation:**
  - Vendor definition (paraphrased): Estimated distance at an energy cost above 25.5 W/kg, the cost of running at a constant 5.5 m/s. It includes both acceleration work and high-speed running ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `HMLD = Σ dᵢ` for samples with `MPᵢ > 25.5 W/kg`.
- **Inputs:** Metabolic power and distance.
- **Units:** m.
- **Variants:** Live HMLD in Gen 2 ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **Comparison with standard methods or other vendors:** Standard methods: HMLD appears in peer-reviewed soccer research alongside high-speed running and accelerations ([Tierney et al. 2016](https://doi.org/10.1016/j.humov.2016.05.007)). The abstract does not state the threshold. Other vendors: Not published.
- **What changes the number:** The threshold. You must sync devices and reprocess history after a change ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)). Gen 1 versus Gen 2.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings), [What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power), [Tierney et al. 2016](https://doi.org/10.1016/j.humov.2016.05.007).

#### Peak Metabolic Power (W/kg)

The fields for this metric are:

- **Vendor name:** `Peak Metabolic Power` ([Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console)).
- **What it measures:** The highest metabolic power reached.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Live, the value uses a 60 second rolling maximum sent by the device, so a missed peak can be recovered ([Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console)).
  - Restatement, not a vendor statement: `max(MPᵢ)`.
- **Inputs:** Metabolic power.
- **Units:** W/kg.
- **Variants:** Live (rolling max) and post-download.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Gen 2 reads 5.5% lower than Gen 1 for peak values in Catapult's test ([What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power)).
- **Source links:** [Detect Metabolic Power live in Console](https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console), [What is Gen 2 Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power).

#### Metabolic power bands and efforts

The fields for this metric are:

- **Vendor name:** Metabolic Power bands (set under **Bands**), metabolic power efforts, and `Metabolic Power Dwell Time (Seconds)` ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **What it measures:** Time, distance, and efforts above chosen power levels.
- **Window or phase:** Band values and default dwell time are Not published.
- **Calculation:**
  - Vendor definition (paraphrased): The dwell time is how many seconds an athlete must stay inside a metabolic power band for an effort to count ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
  - Restatement, not a vendor statement: An effort is a run of samples inside a band that lasts at least the dwell time.
- **Inputs:** Metabolic power.
- **Units:** s, m, count.
- **Variants:** Can be added to Athlete Thresholds for live alerts in Vector Live ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band values and dwell time (team level). Sync and reprocess after changes ([Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings)).
- **Source links:** [Configuring Metabolic Power Settings](https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings).

#### `Energy` (Catapult One, kcal)

The fields for this metric are:

- **Vendor name:** `Energy`, in kcal ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Energy used in a game or session.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): A measure of energy expended, calculated using the player's weight ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: Not published beyond the use of body weight.
- **Inputs:** GNSS data and body weight.
- **Units:** kcal.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The player's entered weight.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

#### `Power Plays` (Catapult One, count)

The fields for this metric are:

- **Vendor name:** `Power Plays`, a count ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** The number of intense actions, such as hard accelerations or fast runs.
- **Window or phase:** 20 W/kg, more than 1 s.
- **Calculation:**
  - Vendor definition (paraphrased): An action with power output above 20 W/kg for more than one second ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: The count of runs where `MP > 20 W/kg` lasts longer than 1 s. Whether Catapult One uses the same metabolic power model as Vector is Not published.
- **Inputs:** GNSS velocity and acceleration.
- **Units:** Count.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Standard methods: Osgnach et al. used 20 W/kg as their high-power cut-off in Serie A data ([Osgnach et al. 2010](https://doi.org/10.1249/MSS.0b013e3181ae5cfd)). Other vendors: Not published.
- **What changes the number:** Not published.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Osgnach et al. 2010](https://doi.org/10.1249/MSS.0b013e3181ae5cfd).

#### `Power Score` (Catapult One, W/kg)

The fields for this metric are:

- **Vendor name:** `Power Score`, in W/kg ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Average power output per kilogram, useful for small-sided games.
- **Window or phase:** None. Catapult One describes small-sided games above 10 W/kg as intense, and 7 to 8 as normal in amateur football. These are reference values ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **Calculation:**
  - Vendor definition (paraphrased): Power output used per kilogram of body weight ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: Probably the session mean of metabolic power. Not published.
- **Inputs:** GNSS.
- **Units:** W/kg.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

#### `Power` (Catapult One player view)

The fields for this metric are:

- **Vendor name:** `Power` score ([Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation), [Know your core metrics](https://one.catapultsports.com/blog/know-your-metrics/)).
- **What it measures:** A combined intensity score for the session.
- **Window or phase:** Not published. Catapult quotes 60 to 80 for professionals and 50 to 60 for amateurs as reference values ([Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation)).
- **Calculation:**
  - Vendor definition (paraphrased): A total of high accelerations, high decelerations, and sprints ([Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation)).
  - Restatement, not a vendor statement: A combination of three counts. Weights, thresholds, and the unit are Not published.
- **Inputs:** GNSS.
- **Units:** Not published.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation), [Know your core metrics](https://one.catapultsports.com/blog/know-your-metrics/).

### Heart rate

**Default heart rate bands (Vector Core)**

| Band | Default range, % of athlete max HR |
|---|---|
| 1 | 0 to 50 |
| 2 | 50 to 60 |
| 3 | 60 to 70 |
| 4 | 70 to 85 |
| 5 | 85 to 95 |
| 6 | above 95 |

Source: [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters). Vector Core allows up to six heart rate bands ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)). OpenField heart rate exertion uses eight band weights ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion)). OpenField defaults for those eight bands are Not published.

Heart rate sources: coded Polar straps ([How Does Catapult Measure Heart Rate?](https://support.catapultsports.com/hc/en-us/articles/360001236836-How-Does-Catapult-Measure-Heart-Rate)), integrated heart rate in Vector Elite vests with S7 and G7 devices ([How to Enable Integrated Heart Rate](https://support.catapultsports.com/hc/en-us/articles/360002066375-How-to-Enable-Integrated-Heart-Rate)), and Bluetooth optical armbands such as Polar OH1 with S7, X7, and G7 devices ([How to Enable Optical Heart Rate](https://support.catapultsports.com/hc/en-us/articles/360002740715-How-to-Enable-Optical-Heart-Rate)). Enabling Bluetooth heart rate disables integrated and magnetic ("mag") heart rate ([How to Enable Optical Heart Rate](https://support.catapultsports.com/hc/en-us/articles/360002740715-How-to-Enable-Optical-Heart-Rate)).

#### `Max Heart Rate` (bpm)

The fields for this metric are:

- **Vendor name:** `Max Heart Rate`. Live: `Max HR` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)).
- **What it measures:** The highest heart rate in the period.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Peak heart rate in beats per minute ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `max(HRᵢ)`.
- **Inputs:** Heart rate sensor (`hr` in the 10 Hz stream ([Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz))).
- **Units:** bpm. Heart rate bands can also be shown in beats per second ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
- **Variants:** `Max HR (% Max)`.
- **Comparison with standard methods or other vendors:** Standard methods: Not applicable. Other vendors: Kinexon PERFORM IMU has integrated ECG-derived heart rate and supports Polar and Suunto ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Raw beats per minute are comparable in principle. Sensor type and artefact handling differ.
- **What changes the number:** Heart rate dropouts and spikes. Catapult advises flagging heart rate dropouts ([Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene)).
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands), [Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

#### `Avg Heart Rate` (bpm)

The fields for this metric are:

- **Vendor name:** `Avg Heart Rate`.
- **What it measures:** Average heart rate.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): The average heart rate in bpm ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `mean(HRᵢ)`. Whether zero or missing samples are excluded is Not published.
- **Inputs:** Heart rate.
- **Units:** bpm.
- **Variants:** `Avg HR (% Max)`.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Dropouts, period edges.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Avg HR (% Max)` (%)

The fields for this metric are:

- **Vendor name:** `Avg HR (% Max)`.
- **What it measures:** Average heart rate as a share of the athlete's max.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Average heart rate as a percentage of the athlete's max set in bands or athlete settings ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `100 × Avg Heart Rate ÷ profile max HR`.
- **Inputs:** Heart rate, profile max HR.
- **Units:** %.
- **Variants:** `Max HR (% Max)`.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** The profile max HR value ([Default Athlete Profile Settings](https://core.catapultsports.com/hc/en-us/articles/7347413350159-Default-Athlete-Profile-Settings)).
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Default Athlete Profile Settings](https://core.catapultsports.com/hc/en-us/articles/7347413350159-Default-Athlete-Profile-Settings).

#### `Max HR (% Max)` (%)

The fields for this metric are:

- **Vendor name:** `Max HR (% Max)`.
- **What it measures:** Peak heart rate as a share of the athlete's max.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Peak heart rate as a percentage of the athlete's max ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `100 × Max Heart Rate ÷ profile max HR`.
- **Inputs:** Heart rate, profile max HR.
- **Units:** %.
- **Variants:** Live `%HR Max` tile (below).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Profile max HR.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters).

#### `Heart Rate Band 1 Duration` to `Heart Rate Band 6 Duration` (h:mm:ss)

The fields for this metric are:

- **Vendor name:** `Heart Rate Band 1 Duration` through `Heart Rate Band 6 Duration` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** Time spent in each heart rate zone.
- **Window or phase:** See the table above.
- **Calculation:**
  - Vendor definition (paraphrased): Time in hours, minutes, and seconds spent in each band ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `T_k = Σ Δt` for samples with HR inside band `k`.
- **Inputs:** Heart rate, profile max HR.
- **Units:** h:mm:ss. OpenField Cloud tables can show seconds ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion)).
- **Variants:** Absolute bpm bands or relative % bands ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Band edges and the profile max HR. Reprocessing for old sessions.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion), [Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands).

#### `Red Zone` (h:mm:ss or min)

The fields for this metric are:

- **Vendor name:** `Red Zone`. Live: `Red Zone`, abbreviated `RZ Min` ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)). Vector Live custom: `Heart Rate Red Zone: Total Time (Minutes)` ([Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App)).
- **What it measures:** Time spent at very high heart rate.
- **Window or phase:** Bands 5 and 6 (above 85% of max). On Vector 7 Bluetooth activities, Pro users can change which bands count ([Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7)).
- **Calculation:**
  - Vendor definition (paraphrased): Typically time above 85% of max heart rate, calculated as Band 5 duration plus Band 6 duration ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: `Red Zone = T_5 + T_6`.
- **Inputs:** Heart rate band durations.
- **Units:** h:mm:ss (post), minutes (live).
- **Variants:** Live custom version.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Band 5 lower edge. Band selection live. Worked example 3 gives 360 s (6.0 min).
- **Source links:** [Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions), [Custom Parameters in the Vector Live App](https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App), [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7), [Vector 7 Bluetooth Live Parameters](https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7).

#### `Heart Rate Exertion` (Vector Core, AU)

The fields for this metric are:

- **Vendor name:** `Heart Rate Exertion` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** One number for cardiovascular load, weighting hard zones more.
- **Window or phase:** Bands as in the table above. Weights 1, 1.2, 1.5, 2.2, 4.5, 9.
- **Calculation:**
  - Formula as Catapult publishes it: `HRE = T₁ + (T₂ × 1.2) + (T₃ × 1.5) + (T₄ × 2.2) + (T₅ × 4.5) + (T₆ × 9)`, where `T_k` is the time in heart rate band `k` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: A weighted sum of time in zones. The time unit (seconds or minutes) is Not published for Vector Core.
- **Inputs:** Heart rate band durations.
- **Units:** Arbitrary.
- **Variants:** OpenField `Heart Rate Exertion` with eight weights (next block).
- **Comparison with standard methods or other vendors:** Standard methods: Catapult calls heart rate exertion comparable with training impulse (TRIMP) ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion), [Catapult Fundamentals: internal and external load](https://www.catapult.com/blog/fundamentals-internal-external-load-performance-questions)). Catapult does not publish which TRIMP model it follows. Other vendors: Not published.
- **What changes the number:** Band edges, profile max HR, and the time unit. Worked example 3 gives 5,694.0 when durations are in seconds and 94.90 when durations are in minutes.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion), [Catapult Fundamentals: internal and external load](https://www.catapult.com/blog/fundamentals-internal-external-load-performance-questions).

#### `Heart Rate Exertion` (OpenField, AU)

The fields for this metric are:

- **Vendor name:** `HRE`, Heart Rate Exertion ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion)).
- **What it measures:** As above.
- **Window or phase:** The weights are fixed and cannot be edited. Band edges are user set ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion)).
- **Calculation:**
  - Formula as Catapult publishes it: Time in seconds in each heart rate band times a fixed scaling factor, summed. Factors: Band 1 = 1, Band 2 = 1.122, Band 3 = 1.322, Band 4 = 1.554, Band 5 = 2.037, Band 6 = 3.252, Band 7 = 5.439, Band 8 = 9.0 ([What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion)).
  - Restatement, not a vendor statement: `HRE = Σ_{k=1}^{8} T_k (s) × w_k`.
- **Inputs:** Heart rate band durations in seconds.
- **Units:** Arbitrary.
- **Variants:** Vector Core six-band version.
- **Comparison with standard methods or other vendors:** Standard methods: See above. Other vendors: Not published.
- **What changes the number:** The two Catapult products use different weights. Worked example 3 applies both weight sets to the same seconds in bands 1 to 6: 5,694.0 with Vector Core weights and 3,910.6 with OpenField weights. This is only an illustration, because real band edges would differ.
- **Source links:** [What Is Heart Rate Exertion](https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion).

#### `%HR Max` live tile and thresholds

The fields for this metric are:

- **Vendor name:** `%HR Max` (main parameter on the iPad Heart Rate dashboard) ([Heart Rate Dashboard](https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard)).
- **What it measures:** Live heart rate as a share of max, colour coded.
- **Window or phase:** Amber at 75%, red at 85% ([Heart Rate Dashboard](https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard)).
- **Calculation:**
  - Vendor definition (paraphrased): Thresholds are relative to the athlete's max HR set in the Cloud ([Heart Rate Dashboard](https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard)).
  - Restatement, not a vendor statement: `100 × HR(t) ÷ profile max HR`.
- **Inputs:** Live heart rate.
- **Units:** %.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Profile max HR. Live connection loss shows a waiting state ([Heart Rate Dashboard](https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard)).
- **Source links:** [Heart Rate Dashboard](https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard).

### Load scores

**Benchmark logic**

Vector Core uses these rules to build its benchmarks:

- Vector Core compares each session with a matchday (MD) benchmark average ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- For an athlete, the benchmark is chosen in this order: the athlete's own average for that day type, then their positional average, then the team average, then the initial sport benchmark ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- An athlete is included in benchmarks only with a `Full` participation tag and a day code. The Catapult page names `Part` and `Rehab` data as excluded. The other tags (`Modified`, `Injury`, `Other`) are not `Full`, so this page reads them as excluded too ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- There are 33 average sets: day codes MD-5 to MD+5, each for team, position, and athlete ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- Before the first tagged match, a sport benchmark is used ([How is the MD Comparison Calculated Prior to Your First Match?](https://core.catapultsports.com/hc/en-us/articles/8789796545935-How-is-the-MD-Comparison-Calculated-Prior-to-Your-First-Match)). Catapult says these benchmarks come from client data, for example 250 football matches from English and Scottish Premier League players who completed 90 minutes, using median values, then rounded.

Default sport benchmarks ([How is the MD Comparison Calculated Prior to Your First Match?](https://core.catapultsports.com/hc/en-us/articles/8789796545935-How-is-the-MD-Comparison-Calculated-Prior-to-Your-First-Match)):

| Sport | Duration (min) | Distance (m) | HS Dist (m) | Accel+Decel | m/min | HS Dist/min | Accel+Decel per min |
|---|---|---|---|---|---|---|---|
| AFL | 94.5 | 11590 | 704 | 172 | 123 | 7.4 | 1.8 |
| American Football | 189 | 4376 | 270 | 35 | 23 | 1.4 | 0.2 |
| Field Hockey | 50 | 6302 | 374 | 155 | 126 | 7.5 | 3.1 |
| Football | 96 | 10200 | 625 | 235 | 106 | 6.5 | 2.4 |
| Lacrosse | 63 | 4284 | 221 | 67 | 68 | 3.5 | 1.1 |
| Rugby League | 73 | 6142 | 302 | 161 | 84 | 4.1 | 2.2 |
| Rugby Union | 51 | 3716 | 360 | 88 | 73 | 7.1 | 1.7 |

The column headers in the source table repeat "Accel+Decel" for the last column. This page reads the last column as per minute. The duration unit is not labelled. This page reads it as minutes.

#### `Volume` (%)

The fields for this metric are:

- **Vendor name:** `Volume` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** How much work the session held compared with the benchmark day.
- **Window or phase:** Uses default velocity bands (HS above 5.5 m/s) and the 2 m/s² effort threshold unless changed.
- **Calculation:**
  - Formula as Catapult publishes it: `Average((Distance / Benchmark Average Distance), (HS Distance / Benchmark Average HS Distance), (Accel+Decel Efforts / Benchmark Average Accel+Decel Efforts))`, converted to a percentage ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `Volume = 100 × (D/D_b + HSD/HSD_b + AD/AD_b) ÷ 3`.
- **Inputs:** `Distance`, `HS Distance`, `Accel&Decel Efforts`, benchmark averages.
- **Units:** %.
- **Variants:** Against MD or other day codes, team, position, or athlete averages ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
- **Comparison with standard methods or other vendors:** Standard methods: Catapult says the model is adapted from an Owens (2017) model and is similar to a model by Jack Sharkey ([Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)). The Owens reference is not given in full. Not published. Other vendors: Not published.
- **What changes the number:** Tagging (`Full` and day codes), the benchmark that applies, band and effort settings. A training day reported as 60% volume means 60% of the match workload ([Catapult Fundamentals: internal and external load](https://www.catapult.com/blog/fundamentals-internal-external-load-performance-questions)).
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load), [Catapult Fundamentals: internal and external load](https://www.catapult.com/blog/fundamentals-internal-external-load-performance-questions).

#### `Intensity` (%)

The fields for this metric are:

- **Vendor name:** `Intensity` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** How hard the session was per minute compared with the benchmark day.
- **Window or phase:** As for `Volume`.
- **Calculation:**
  - Formula as Catapult publishes it: `Average((Dist Per Minute / Benchmark Average Dist Per Minute), (HS Dist Per Minute / Benchmark HS Dist Per Minute), (Accel+Decel Eff Per Minute / Benchmark Average Accel+Decel Eff Per Minute))`, converted to a percentage ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: `Intensity = 100 × (m/min ÷ b + HS m/min ÷ b + AD/min ÷ b) ÷ 3`.
- **Inputs:** The three per-minute metrics and their benchmarks.
- **Units:** %.
- **Variants:** As for `Volume`.
- **Comparison with standard methods or other vendors:** Standard methods: As for `Volume`. Other vendors: Not published.
- **What changes the number:** As for `Volume`, plus period edges.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load).

#### `Overall` (%)

The fields for this metric are:

- **Vendor name:** `Overall` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** A single combined load score.
- **Window or phase:** None.
- **Calculation:**
  - Formula as Catapult publishes it: `Volume x Intensity` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load)).
  - Restatement, not a vendor statement: If both are ratios, `Overall = (Volume/100) × (Intensity/100) × 100`. How Catapult scales the product of two percentages is Not published.
- **Inputs:** `Volume`, `Intensity`.
- **Units:** % (as displayed).
- **Variants:** As for `Volume`.
- **Comparison with standard methods or other vendors:** Standard methods: As for `Volume`. Other vendors: Not published.
- **What changes the number:** Everything that changes `Volume` or `Intensity`.
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Understanding Volume, Intensity and Overall Load](https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load).

#### Acute:Chronic Workload Ratio (OpenField chart)

The fields for this metric are:

- **Vendor name:** `Acute Load`, `Chronic Load`, `Acute:Chronic Ratio` in the OpenField Cloud chart wizard ([How to Set Up an Acute:Chronic Workload Ratio Chart](https://support.catapultsports.com/hc/en-us/articles/360000538795-How-to-Set-Up-an-Acute-Chronic-Workload-Ratio-Chart)).
- **What it measures:** Recent load compared with longer-term load.
- **Window or phase:** Catapult's article cites 0.8 to 1.3 as a target range and above 1.5 as a spike. These are guidance, not system defaults ([How to Set Up an Acute:Chronic Workload Ratio Chart](https://support.catapultsports.com/hc/en-us/articles/360000538795-How-to-Set-Up-an-Acute-Chronic-Workload-Ratio-Chart)).
- **Calculation:**
  - Vendor definition (paraphrased): Acute load is the most recent workload (typically 3 to 7 days). Chronic load is the load the athlete has adapted to (typically 3 to 6 weeks). You set both durations at team level ([How to Set Up an Acute:Chronic Workload Ratio Chart](https://support.catapultsports.com/hc/en-us/articles/360000538795-How-to-Set-Up-an-Acute-Chronic-Workload-Ratio-Chart)).
  - Restatement, not a vendor statement: `ACWR = Acute Load ÷ Chronic Load` for the chosen parameter. Whether OpenField uses rolling averages or exponentially weighted averages, and whether the acute window sits inside the chronic window, is Not published.
- **Inputs:** Any parameter, often Player Load.
- **Units:** Ratio.
- **Variants:** Any parameter.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Acute and chronic window lengths. The averaging method (Not published).
- **Source links:** [How to Set Up an Acute:Chronic Workload Ratio Chart](https://support.catapultsports.com/hc/en-us/articles/360000538795-How-to-Set-Up-an-Acute-Chronic-Workload-Ratio-Chart).

### Impacts and IMA events

**How IMA works**

Catapult publishes these facts about Inertial Movement Analysis (IMA) ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)):

- IMA needs a Vector Pro licence.
- IMA uses the tri-axial accelerometer and tri-axial gyroscope at 100 Hz. GPS is not needed, so it works indoors.
- A gravity filtering model separates athlete movement from device movement. A Catapult article adds that Kalman filtering is applied to accelerometer and gyroscope data ([White Paper: Introduction to IMA](https://www.catapult.com/blog/white-paper-introduction-ima)).
- IMA movement intensity is expressed in m/s.
- Direction uses a clock face of 12 segments of 30°. Acceleration is −45° to 45°. Deceleration is 135° to 180° and −180° to −135°. Change of direction left is −135° to −45°. Change of direction right is 45° to 135°.
- Change-of-direction side follows the applied force. Planting the left foot to cut right registers as a change of direction to the right.
- IMA bands are set for `IMA Impact`, `IMA Intensity`, and `IMA Jumps`.
- The full list of IMA parameters is in the OpenField Cloud Parameter Definitions article, which needs a sign-in. Default IMA band values are Not published.
- IMA tracks: acceleration count, deceleration count, asymmetrical loading, change of direction count left and right, free running event count, free running total time, average stride rate, impacts, and jump count ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [White Paper: Introduction to IMA](https://www.catapult.com/blog/white-paper-introduction-ima)).
- When the device is worn at the front of the waist, OpenField inverts the device axes during processing. This affects IMA accelerations, decelerations, changes of direction, clock-face accelerations, and some sport plugins ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).

The Catapult IMA white paper download needs a form submission. The white paper was not used for this page ([White Paper: Introduction to IMA](https://www.catapult.com/blog/white-paper-introduction-ima)).

#### `Impacts` (Vector Core, count)

The fields for this metric are:

- **Vendor name:** `Impacts` ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
- **What it measures:** How many big hits or collisions the athlete took.
- **Window or phase:** 5 g.
- **Calculation:**
  - Vendor definition (paraphrased): The number of impacts above 5 g ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)).
  - Restatement, not a vendor statement: The count of events where acceleration magnitude exceeds 5 g. Whether Catapult uses the resultant of all three axes, and how it separates one event from the next, is Not published.
- **Inputs:** Accelerometer.
- **Units:** Count.
- **Variants:** Catapult One `Impacts`. IMA impact events with bands.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Device fit ([Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene)). Event separation rule (Not published).
- **Source links:** [Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters), [Best Practice for Good Data Hygiene](https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene).

#### `Impacts` (Catapult One, count)

The fields for this metric are:

- **Vendor name:** `Impacts` ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
- **What it measures:** Large hits such as tackles and collisions.
- **Window or phase:** 5 g.
- **Calculation:**
  - Vendor definition (paraphrased): Accelerometer data at 400 samples per second on each axis is used to detect impacts above 5 g (49 m/s²). Normal footsteps are excluded ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches)).
  - Restatement, not a vendor statement: As for Vector Core, at 400 Hz.
- **Inputs:** Accelerometer at 400 Hz.
- **Units:** Count.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches).

#### IMA Acceleration count

The fields for this metric are:

- **Vendor name:** "Acceleration count" in the IMA list ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)). OpenField parameter names are Not published publicly.
- **What it measures:** Forward bursts detected from the inertial sensors, without GPS.
- **Window or phase:** Low, medium, and high intensity zones exist ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)). Values are Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Micro-movements whose direction falls between −45° and 45° on the IMA clock ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
  - Restatement, not a vendor statement: Count of IMA events in the forward quarter whose intensity passes the IMA band threshold.
- **Inputs:** Accelerometer and gyroscope at 100 Hz.
- **Units:** Count.
- **Variants:** Banded counts. IMA RHIE bands ([What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** IMA band edges, device location setting ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs), [Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics).

#### IMA Deceleration count

The fields for this metric are:

- **Vendor name:** "Deceleration count" in the IMA list ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** Braking movements detected from the inertial sensors.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Micro-movements between 135° and 180°, or −180° and −135° ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
  - Restatement, not a vendor statement: Count of IMA events in the rear quarter above the band threshold.
- **Inputs:** Accelerometer and gyroscope.
- **Units:** Count.
- **Variants:** Banded counts.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** As above.
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA).

#### IMA Change of Direction Left and Right

The fields for this metric are:

- **Vendor name:** "Change of direction (COD) count, left and right" ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** Sideways cuts to each side.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Left is −135° to −45°. Right is 45° to 135°. Side follows the applied force ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
  - Restatement, not a vendor statement: Count of IMA events in each side quarter above the band threshold.
- **Inputs:** Accelerometer and gyroscope.
- **Units:** Count.
- **Variants:** Left, right, banded.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon lists `Changes of Orientation` ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Its definition is Not published, so the two counts are not interchangeable.
- **What changes the number:** Device orientation. Waist-front devices need axis inversion ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

#### IMA intensity event (`ima_acceleration`)

The fields for this metric are:

- **Vendor name:** Connect API event `ima_acceleration` (IMA v2.0 and v2.1) with `intensity` and `direction` ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). OpenField band set `IMA Intensity` ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** The size and direction of each inertial movement event.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): `intensity` is in metres per second, the peak area (integral of acceleration). `direction` is in twelfths of a circle ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
  - Restatement, not a vendor statement: `intensity ≈ ∫ a dt` over the event (a velocity change). `degrees = direction ÷ 12 × 360`.
- **Inputs:** Accelerometer and gyroscope.
- **Units:** m/s; direction in 1/12 circle.
- **Variants:** Gen1 IMA intensity bands for older accounts ([What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon `Exertion Events` are high-intensity activity above an acceleration load threshold ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Thresholds and integration methods are Not published, so the counts are not interchangeable.
- **What changes the number:** IMA version, device location.
- **Source links:** [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### IMA Impact event (`ima_impact`)

The fields for this metric are:

- **Vendor name:** Connect API event `ima_impact` (IMA v2.0, or v2.3 from the impacts plugin) with `impact` and `direction` ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). OpenField band set `IMA Impact` ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** The size and main direction of each collision.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): `impact` is the force of the impact in g. `direction` is side (0, mainly horizontal) or vertical (1) ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
  - Restatement, not a vendor statement: One event per detected collision with peak g and plane.
- **Inputs:** Accelerometer and gyroscope.
- **Units:** g.
- **Variants:** Impact tables with `Impact (g)`, `Impact Direction`, and `Band`. Tables use a "band and above" filter, so `B3+` shows bands 3 to 8 ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band settings, plugin version.
- **Source links:** [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events).

#### Free running (IMA and `free_running` event)

The fields for this metric are:

- **Vendor name:** IMA "free running event count" and "free running total time" ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)). Connect API event `free_running` (movementmetrics plugin) with `burst_duration`, `stride_count`, `burst_load`, and `burst_distance` ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
- **What it measures:** Stretches of uninterrupted straight-line running.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): An inertial algorithm that detects passages of uninterrupted straight-line running ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
  - Restatement, not a vendor statement: Event count, summed duration, strides, Player Load, and distance per running burst.
- **Inputs:** Inertial sensors. Distance input is Not published.
- **Units:** s, count, accumulated PlayerLoad units, m.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data).

#### Average stride rate (IMA)

The fields for this metric are:

- **Vendor name:** "Average stride rate" ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** Steps per unit time during running.
- **Window or phase:** Not published.
- **Calculation:** Not published.
- **Inputs:** Inertial sensors.
- **Units:** Not published.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA).

#### Asymmetrical loading (IMA)

The fields for this metric are:

- **Vendor name:** "Asymmetrical loading" ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** Imbalance between left and right movement load.
- **Window or phase:** Not published.
- **Calculation:** Not published. See [Running symmetry](#running-symmetry) for a published left-right method.
- **Inputs:** Inertial sensors.
- **Units:** Not published.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Not published.
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA).

#### Tackle and impact event tables

The fields for this metric are:

- **Vendor name:** OpenField Console efforts and events tables for Dives, Throws, Tackles, and Impacts. Tackles show `Tackle Intensity (AU)`, `Tackle Duration (s)`, `Tackle Impact (g)`, and `Band (#)` ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)).
- **What it measures:** Per-event detail for collisions.
- **Window or phase:** Not published.
- **Calculation:**
  - Vendor definition (paraphrased): Events are listed by band using a "band and above" rule ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)).
  - Restatement, not a vendor statement: One row per event.
- **Inputs:** Inertial sensors.
- **Units:** AU, s, g.
- **Variants:** Rugby league tackle event in the API (see sport-specific section).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Band filter in the table.
- **Source links:** [Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events).

### Jumps

#### IMA Jump (`ima_jump`, height in m)

The fields for this metric are:

- **Vendor name:** IMA "jump count" ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)). Connect API event `ima_jump` (IMA v2.0) with `height` in metres ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). OpenField band set `IMA Jumps` ([What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA)).
- **What it measures:** Each jump and its height.
- **Window or phase:** IMA Jump band defaults are Not published.
- **Calculation:**
  - Vendor definition (paraphrased): An inertial jump detection algorithm that reports jump height for each detected jump ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
  - Restatement, not a vendor statement: Event count and per-event height. How height is computed (for example from flight time) is Not published.
- **Inputs:** Accelerometer and gyroscope.
- **Units:** m.
- **Variants:** Jump Height export (next block). Jumps can be graphed with goalkeeper events in the Cloud Web Editor ([Graphing Goalkeeper Events and IMA Jumps](https://support.catapultsports.com/hc/en-us/articles/15519822056207-Graphing-Goalkeeper-Events-and-IMA-Jumps-in-the-Web-Editor)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon lists `Number of Jumps` and `Jump Height` ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)) and `Jump Load` based on a one-dimensional vertical acceleration pattern ([Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/)). Catapult does not publish a jump load metric. Methods differ, so heights are not interchangeable without a side-by-side test.
- **What changes the number:** Band settings. Device fit.
- **Source links:** [What is IMA?](https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [Graphing Goalkeeper Events and IMA Jumps](https://support.catapultsports.com/hc/en-us/articles/15519822056207-Graphing-Goalkeeper-Events-and-IMA-Jumps-in-the-Web-Editor), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf), [Kinexon: three player metrics](https://kinexon-sports.com/blog/data-analytics-in-sports/).

#### Jump Height export (OpenField Console)

The fields for this metric are:

- **Vendor name:** Jump height in the OpenField Console event CSV ([How to Export Jump Height Data in OpenField](https://support.catapultsports.com/hc/en-us/articles/360002282956-How-to-Export-Jump-Height-Data-in-OpenField)).
- **What it measures:** Height of each IMA jump.
- **Window or phase:** Not published.
- **Calculation:** As `ima_jump`.
- **Inputs:** IMA jump events.
- **Units:** Not stated on the export page. The API unit is metres ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).
- **Variants:** Available for IMA Jumps only, not Indoor Jumps ([How to Export Jump Height Data in OpenField](https://support.catapultsports.com/hc/en-us/articles/360002282956-How-to-Export-Jump-Height-Data-in-OpenField)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: See IMA Jump.
- **What changes the number:** The **Flatten Parameters** export option must be off ([How to Export Jump Height Data in OpenField](https://support.catapultsports.com/hc/en-us/articles/360002282956-How-to-Export-Jump-Height-Data-in-OpenField)).
- **Source links:** [How to Export Jump Height Data in OpenField](https://support.catapultsports.com/hc/en-us/articles/360002282956-How-to-Export-Jump-Height-Data-in-OpenField), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data).

#### Indoor Jumps (T7 Indoor Analytics)

The fields for this metric are:

- **Vendor name:** Indoor Jumps, in the Indoor Analytics category ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)).
- **What it measures:** Jumps detected by the T7 or S7 inertial sensors indoors, sorted into Low, Medium, and High.
- **Window or phase:** Three bands (Low, Medium, High), in centiseconds. A default set is applied when the module is turned on. The values are Not published ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)).
- **Calculation:**
  - Vendor definition (paraphrased): Indoor Analytics algorithms use inertial sensors to detect jumps and estimate total distance without GPS ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)).
  - Restatement, not a vendor statement: Count of jumps per band. The band variable is in centiseconds ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)). The Connect API reports a jump width in centiseconds for basketball jumps ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). This page reads the bands as sorting jumps by duration. The Catapult page does not say so directly.
- **Inputs:** Inertial sensors. Device location (vest, waist-back, waist-front) must be set ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).
- **Units:** Count; bands in centiseconds.
- **Variants:** Live on T7 only. Post-download on T7 or S7 ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Device location setting, band values, reprocessing.
- **Source links:** [How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics).

#### Estimated distance (T7 Indoor Analytics)

The fields for this metric are:

- **Vendor name:** Estimated Total Distance in Indoor Analytics ([How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics)).
- **What it measures:** Distance estimated from inertial sensors when no positioning system is available.
- **Window or phase:** Not published.
- **Calculation:** Not published. The parameter definitions page needs a sign-in.
- **Inputs:** Inertial sensors.
- **Units:** Not published.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Do not compare with GNSS or LPS distance.
- **What changes the number:** Device location setting ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).
- **Source links:** [How to Detect Indoor Analytics](https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics), [Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics).

#### Live Jumps

The fields for this metric are:

- **Vendor name:** Live jump analytics ([Can Live Jumps Differentiate Between Left Foot and Right Foot Jumping?](https://support.catapultsports.com/hc/en-us/articles/6912559339279-Can-Live-Jumps-Differentiate-Between-Left-Foot-and-Right-Foot-Jumping)).
- **What it measures:** Total jumps in real time.
- **Window or phase:** Not published.
- **Calculation:** Not published. Live jumps cannot tell left-foot from right-foot jumps ([Can Live Jumps Differentiate Between Left Foot and Right Foot Jumping?](https://support.catapultsports.com/hc/en-us/articles/6912559339279-Can-Live-Jumps-Differentiate-Between-Left-Foot-and-Right-Foot-Jumping)).
- **Inputs:** Inertial sensors.
- **Units:** Count.
- **Variants:** Post-download IMA or Indoor jumps.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Kinexon lists `Live Jumps` ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Method Not published.
- **What changes the number:** Not published.
- **Source links:** [Can Live Jumps Differentiate Between Left Foot and Right Foot Jumping?](https://support.catapultsports.com/hc/en-us/articles/6912559339279-Can-Live-Jumps-Differentiate-Between-Left-Foot-and-Right-Foot-Jumping), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

### Intervals and repeated efforts

#### Repeat High Intensity Efforts (RHIE)

The fields for this metric are:

- **Vendor name:** Repeat High Intensity Efforts (RHIEs), grouped into RHIE bouts ([What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs)).
- **What it measures:** Clusters of hard efforts with too little recovery between them.
- **Window or phase:** Not published, except that only Gen2 velocity and acceleration efforts count when both Gen1 and Gen2 exist ([What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs)). A goalkeeper team setting `Dive Load RHIE` defaults to 3 ([How to Detect Goal Keeper Dives](https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField)).
- **Calculation:**
  - Vendor definition (paraphrased): High-intensity efforts repeated within a set time are grouped into a bout. Settings are: `RHIE Effort Count` (minimum efforts in a bout), `RHIE Effort Recovery` (maximum time between efforts), `Velocity RHIE Bands`, and `Acceleration RHIE Bands`. IMA intensity, IMA jump, IMA impact or tackle bands, and goalkeeping dive load bands can also count ([What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs)).
  - Restatement, not a vendor statement: Sort all qualifying efforts by time. Start a bout when at least `RHIE Effort Count` efforts follow each other with gaps no longer than `RHIE Effort Recovery`.
- **Inputs:** Velocity, acceleration, and IMA efforts.
- **Units:** Count, s.
- **Variants:** RHIE parameter definitions are on a sign-in page. Not published.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Every RHIE team setting, plus the underlying effort rules.
- **Source links:** [What are RHIEs?](https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs), [How to Detect Goal Keeper Dives](https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField).

#### `Work Rate - % Distance` (%)

The fields for this metric are:

- **Vendor name:** `Work Rate - % Distance (m)` ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **What it measures:** The share of distance covered inside work-rate intervals.
- **Window or phase:** Duration and distance thresholds are team settings. The 60 s and 100 m values are examples, not stated defaults ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **Calculation:**
  - Formula as Catapult publishes it: Distance in Work Rate Intervals ÷ Total Distance × 100 ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
  - Restatement, not a vendor statement: A work-rate interval is any window of the set duration in which distance exceeds the set distance (for example 60 s and 100 m).
- **Inputs:** 10 Hz distance.
- **Units:** %.
- **Variants:** Live and post-activity. Needs the WorkRate module and Console 3.3 or later ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Thresholds. You must sync and bake the activity after changes ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)). How overlapping windows are counted is Not published.
- **Source links:** [What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals).

#### `Work Rate - Duration` (s)

The fields for this metric are:

- **Vendor name:** `Work Rate - Duration` ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **What it measures:** Time spent in work-rate intervals.
- **Window or phase:** As above.
- **Calculation:** Formula as published: total duration in seconds of work-rate intervals ÷ session count ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **Inputs:** Distance.
- **Units:** s.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** As above. The ÷ session count means multi-session selections show an average.
- **Source links:** [What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals).

#### `Work Rate - Interval Count` (count)

The fields for this metric are:

- **Vendor name:** `Work Rate - Interval Count (#)` ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **What it measures:** How many work-rate intervals occurred.
- **Window or phase:** As above.
- **Calculation:** Formula as published: total number of intervals ÷ session count ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **Inputs:** Distance.
- **Units:** Count.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** As above.
- **Source links:** [What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals).

#### `Work Rate - Interval Distance` (m)

The fields for this metric are:

- **Vendor name:** `Work Rate - Interval Distance (m)` ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **What it measures:** Distance covered inside work-rate intervals.
- **Window or phase:** As above.
- **Calculation:** Formula as published: total distance in intervals ÷ session count ([What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals)).
- **Inputs:** Distance.
- **Units:** m.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** As above.
- **Source links:** [What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals).

#### `Maximum Intensity Distance Interval 1`, `2`, `3` (m)

The fields for this metric are:

- **Vendor name:** `Maximum Intensity Distance Interval 1 (m)`, `2 (m)`, `3 (m)` ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
- **What it measures:** The most distance covered in any window of a set length. Often called peak demands or worst-case scenario.
- **Window or phase:** Windows of 1, 3, and 5 minutes ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
- **Calculation:**
  - Vendor definition (paraphrased): The highest accumulated distance for a set duration across the whole period or activity, using a rolling window on 10 Hz distance ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
  - Restatement, not a vendor statement: `MII_D(w) = max over t of [D(t + w) − D(t)]`, where `D` is cumulative distance and `w` is the window length.
- **Inputs:** 10 Hz distance.
- **Units:** m.
- **Variants:** Player Load version (next block). Needs the MII module and Console 2.4 or later. Post-activity only ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
- **Comparison with standard methods or other vendors:** Standard methods: A rolling window, as in peak-intensity research such as moving-average analysis of rugby league ([Delaney et al. 2016](https://doi.org/10.1123/ijspp.2015-0424)). Other vendors: Not published.
- **What changes the number:** Window length. The period must be at least as long as the window ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)). Sync and reprocess after changes.
- **Source links:** [What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals), [Delaney et al. 2016](https://doi.org/10.1123/ijspp.2015-0424).

#### `Maximum Intensity Player Load Interval 1`, `2`, `3` (AU)

The fields for this metric are:

- **Vendor name:** `Maximum Intensity Player Load Interval 1`, `2`, `3` ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
- **What it measures:** The most Player Load gathered in any window of a set length.
- **Window or phase:** 1, 3, and 5 minutes.
- **Calculation:** Same rolling-window rule on 10 Hz Player Load ([What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).
- **Inputs:** 10 Hz Player Load.
- **Units:** AU.
- **Variants:** Distance version.
- **Comparison with standard methods or other vendors:** Standard methods: As above. Other vendors: Not published.
- **What changes the number:** As above.
- **Source links:** [What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals).

### Running symmetry

Running symmetry needs the RunningSymmetry module and OpenField Console 2.0 or later. An effort counts only when every footstrike is above the minimum speed and the number of consecutive footstrikes meets the minimum. Defaults are 3.3 m/s and 8 footstrikes, set at team level. An indoor option computes symmetry without velocity, which Catapult calls less accurate. Device fit, surface, straight-line running, and constant speed all affect quality ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)). The Connect API event `running_symmetry` returns `foostrikes` (spelled this way in the API), `imbalance`, `distance`, `line_deviation`, `avg_velocity`, and `max_velocity` ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).

#### `Running Imbalance` (%)

The fields for this metric are:

- **Vendor name:** `Running Imbalance (%)` ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **What it measures:** The load difference between legs while running.
- **Window or phase:** 3.3 m/s and 8 consecutive footstrikes.
- **Calculation:**
  - Vendor definition (paraphrased): Average percentage load difference between left and right legs across all running symmetry efforts. Negative means x% more load on the left. Positive means x% more on the right ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
  - Restatement, not a vendor statement: `mean(imbalance_k)` over efforts `k`. How each effort's imbalance is computed is Not published.
- **Inputs:** Inertial sensors and velocity.
- **Units:** %.
- **Variants:** Console widget thresholds can differ from Cloud thresholds. The Cloud always uses team settings ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Speed and footstrike thresholds, fit, surface, curved running.
- **Source links:** [How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics).

#### `Footstrikes` (count)

The fields for this metric are:

- **Vendor name:** `Footstrikes` ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **What it measures:** Footstrikes counted inside qualifying running efforts.
- **Window or phase:** As above.
- **Calculation:** The count of footstrikes across all efforts that meet the thresholds ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **Inputs:** Inertial sensors.
- **Units:** Count.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Thresholds.
- **Source links:** [How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics).

#### `Running Imbalance Standard Deviation` (%)

The fields for this metric are:

- **Vendor name:** `Running Imbalance Standard Deviation` ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **What it measures:** How consistent the imbalance is from run to run.
- **Window or phase:** Guidance values 2 and 4.
- **Calculation:** Standard deviation of the per-series imbalance scores. Catapult says an SD below 2 suggests a consistent gait and above 4 suggests varying compensation ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **Inputs:** Per-series imbalance.
- **Units:** %.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Number of series. Thresholds.
- **Source links:** [How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics).

#### `Running Series #` (count)

The fields for this metric are:

- **Vendor name:** `Running Series #` ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **What it measures:** How many qualifying running efforts were found.
- **Window or phase:** As above.
- **Calculation:** The total number of running symmetry series or efforts ([How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics)).
- **Inputs:** Inertial sensors, velocity.
- **Units:** Count.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Thresholds.
- **Source links:** [How to Detect Running Symmetry Metrics](https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics).

## Sport-specific metrics

These metrics need sport modules or plugins, and most need a Vector Pro licence. To keep this page usable, each sport uses a table. Every row shares the block fields: the table gives the name, the vendor definition (paraphrased), and the unit. The notes under each table give inputs, defaults, variants, and what changes the number. Comparisons with standard methods and other vendors are Not published for every metric in this section unless stated.

### Basketball Movement Profile (BMP)

BMP classifies every movement into five categories: Active, Running, Dynamic, Jumping, and Passive ([BMP Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/10024943670159-Basketball-Movement-Profile-BMP-Parameter-Definitions)). A Catapult blog says the algorithm classifies one-second segments and calls the standing category "Settled" ([Basketball Movement Profile blog](https://www.catapult.com/blog/vector-t7-movement-profile)). Inputs: inertial sensors. The device location (vest, waist-back, waist-front) must be set ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)). Needs the BasketballAnalytics module. Post-download only in OpenField Cloud ([How to Detect BMP Metrics](https://support.catapultsports.com/hc/en-us/articles/10024923779471-How-to-Detect-Basketball-Movement-Profile-BMP-Metrics)). The detailed method article needs a sign-in. Thresholds are Not published.

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `BMP Jumping Load` | Load accumulated in the Jumping category | arb |
| `BMP Dynamic Load` | Load accumulated in the Dynamic category | arb |
| `BMP Running Load` | Load accumulated in the Running category | arb |
| `BMP Active Load` | Load accumulated in the Active category | arb |
| `BMP Passive Load` | Load accumulated in the Passive category | arb |
| `BMP Total Basketball Load` | Sum of the five category loads | arb |
| `BMP Jumping Load Average (Session)` | Average Jumping load per selected activity | arb |
| `BMP Dynamic Load Average (Session)` | Average Dynamic load per activity | arb |
| `BMP Running Load Average (Session)` | Average Running load per activity | arb |
| `BMP Active Load Average (Session)` | Average Active load per activity | arb |
| `BMP Passive Load Average (Session)` | Average Passive load per activity | arb |
| `BMP Total Basketball Load Average (Session)` | Average total load per activity | arb |
| `BMP Jumping Duration` | Time spent gathering Jumping load | h:mm:ss |
| `BMP Dynamic Duration` | Time spent gathering Dynamic load | h:mm:ss |
| `BMP Running Duration` | Time spent gathering Running load | h:mm:ss |
| `BMP Active Duration` | Time spent gathering Active load | h:mm:ss |
| `BMP Passive Duration` | Time spent gathering Passive load | h:mm:ss |
| `BMP Jumping Duration %` | Jumping time as a share of the activity or period | listed as h:mm:ss in the source, likely % |
| `BMP Dynamic Duration %` | Dynamic time as a share | % |
| `BMP Running Duration %` | Running time as a share | % |
| `BMP Active Duration %` | Active time as a share | % |
| `BMP Passive Duration %` | Passive time as a share | % |
| `BMP Jumping Duration Average (Session)` | Average Jumping time per activity | h:mm:ss |
| `BMP Dynamic Duration Average (Session)` | Average Dynamic time per activity | h:mm:ss |
| `BMP Running Duration Average (Session)` | Average Running time per activity | h:mm:ss |
| `BMP Active Duration Average (Session)` | Average Active time per activity | h:mm:ss |
| `BMP Passive Duration Average (Session)` | Average Passive time per activity | h:mm:ss |

Source for all rows: [BMP Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/10024943670159-Basketball-Movement-Profile-BMP-Parameter-Definitions). The formula for "basketball load" is Not published. In the Connect API, each `basketball` event returns `movement_type` (1 to 4 for vest, 101 to 104 for waist), `basketball_load` (arbitrary unit), and `jump_attribute` (jump width in centiseconds) ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data), [How to Detect BMP Metrics](https://support.catapultsports.com/hc/en-us/articles/10024923779471-How-to-Detect-Basketball-Movement-Profile-BMP-Metrics)).

### Tennis Analytics

Tennis Analytics classifies five movement categories (Running, Dynamic, Alert, Low Intensity, Passive) and four stroke types (Serve, Right-to-left, Left-to-right, Other). Inputs: inertial sensors. Needs the TennisAnalytics module. Post-download in OpenField Cloud ([Tennis Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/10024959888655-Tennis-Parameter-Definitions), [How to Detect Tennis Metrics](https://support.catapultsports.com/hc/en-us/articles/10024968443791-How-to-Detect-Tennis-Metrics)). The method article needs a sign-in. The formula for "tennis load" is Not published.

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `Total Stroke Count` | Sum of serve, right-to-left, left-to-right, and other strokes | # |
| `Serve Count` | Number of serves | # |
| `Right-to-left Stroke Count` | Right-handed forehands and left-handed backhands | # |
| `Left-to-right Stroke Count` | Left-handed forehands and right-handed backhands | # |
| `Other Stroke Count` | Overheads, volleys, blocks, improvised shots | # |
| `Total Strokes / Min` | `(Total Strokes / Duration in seconds) × 60` | # (per minute by the formula) |
| `Total Tennis Load` | Sum of the four stroke loads and four movement loads | arb |
| `Serve Load` | Tennis load during serves | arb |
| `Right-to-left Stroke Load` | Tennis load during right-to-left strokes | arb |
| `Left-to-right Stroke Load` | Tennis load during left-to-right strokes | arb |
| `Other Stroke Load` | Tennis load during other strokes | arb |
| `Tennis Dynamic Load` | Load in the Dynamic category | arb |
| `Tennis Alert Load` | Load in the Alert category | arb |
| `Tennis Running Load` | Load in the Running category | arb |
| `Tennis Low intensity Load` | Load in the Low intensity category | arb |
| `Total Tennis Load / Min` | `(Total Tennis Load / Duration in seconds) × 60` | arb (per minute by the formula) |
| `Serve Duration` | Time spent serving | h:mm:ss |
| `Right-to-left Stroke Duration` | Time in right-to-left strokes | h:mm:ss |
| `Left-to-right Stroke Duration` | Time in left-to-right strokes | h:mm:ss |
| `Other Stroke Duration` | Time in other strokes | h:mm:ss |
| `Tennis Dynamic Duration` | Time in Dynamic movement | h:mm:ss |
| `Tennis Alert Duration` | Time in Alert movement | h:mm:ss |
| `Tennis Running Duration` | Time in Running movement | h:mm:ss |
| `Tennis Low intensity Duration` | Time in Low intensity movement | h:mm:ss |
| `Tennis Passive Duration` | Time in Passive movement | h:mm:ss |
| `Serve Duration %` | Serve time as a share of the activity | % |
| `Right-to-left Stroke Duration %` | Share of time | % |
| `Left-to-right Stroke Duration %` | Share of time | % |
| `Other Stroke Duration %` | Share of time | % |
| `Tennis Dynamic Duration %` | Share of time | % |
| `Tennis Alert Duration %` | Share of time | % |
| `Tennis Running Duration %` | Share of time | % |
| `Tennis Low intensity Duration %` | Share of time | % |
| `Tennis Passive Duration %` | Share of time | % |
| `Serve mean rotation magnitude` | Total serve rotation ÷ serve count | rev/s |
| `Right-to-left Stroke mean rotation magnitude` | Total rotation ÷ stroke count | rev/s |
| `Left-to-right Stroke mean rotation magnitude` | Total rotation ÷ stroke count | rev/s |
| `Other Stroke mean rotation magnitude` | Total rotation ÷ stroke count | rev/s |

Source for all rows: [Tennis Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/10024959888655-Tennis-Parameter-Definitions). In the Connect API, each `tennis` event returns `movement_type` (1 to 8), `tennis_load`, and, for strokes, `rotation_magnitude` in revolutions per second ([How to Detect Tennis Metrics](https://support.catapultsports.com/hc/en-us/articles/10024968443791-How-to-Detect-Tennis-Metrics), [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). The API page also describes the rotation unit as degrees per second or (radians/2π)/s. Treat the unit as revolutions per second, which matches both the parameter page and (radians/2π)/s.

### Rugby union

Rugby suite events: scrums, contact involvements, lineout jumps, and kicks. `Duration` is the time for the player to return upright (time to feet). Back-in-Game (`BiG`) time is the time to accumulate 0.50 Player Load after the event. Catapult chose 0.50 after comparing many thresholds. BiG time applies only when the period after the event is active ([Rugby Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/360001447456-Rugby-Parameter-Definitions)). Short, Medium, and Long bands are user set under **Bands** as Band 1, 2, and 3 for `Scrum BiG`, `Contact Involvement BiG`, and `Contact Involvement Duration`. Default band values are Not published.

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `Scrum BiG Time` | Time to gather 0.50 Player Load after leaving a scrum | s |
| `Average Scrum Count (Session)` | Average scrums per activity | count |
| `Average Scrum Duration` | Average time back to upright after a scrum | s |
| `Scrum BiG Time Short Count` | Scrums with short BiG time (Band 1) | count |
| `Scrum BiG Time Medium Count` | Scrums with medium BiG time (Band 2) | count |
| `Scrum BiG Time Long Count` | Scrums with long BiG time (Band 3) | count |
| `Scrum Count` | Scrums in an activity | count |
| `Total Scrum BiG Time` | Sum of BiG times after each scrum | s |
| `Contact Involvement Average BiG Time` | Average BiG time after contact involvements | s |
| `Contact Involvement Avg Duration` | Average time back to upright | s |
| `Contact Involvement BiG Time Short / Medium / Long Count` | Contact involvements in each BiG band (3 metrics) | count |
| `Contact Involvement Duration Short / Medium / Long Avg Count` | Average count in each duration band (3 metrics) | count |
| `Contact Involvement Duration Short BiG Time Short / Medium / Long Count` | Short duration crossed with each BiG band (3 metrics) | count |
| `Contact Involvement Duration Medium BiG Time Short / Medium / Long Count` | Medium duration crossed with each BiG band (3 metrics) | count |
| `Contact Involvement Duration Long BiG Time Short / Medium / Long Count` | Long duration crossed with each BiG band (3 metrics) | count |
| `Contact Involvement Duration Short / Medium / Long Count` | Count in each duration band (3 metrics) | count |
| `Contact Involvement Total Count` | Contact involvements within the duration band settings | count |
| `Contact Involvement Total Duration` | Summed duration of those involvements | s |
| `Total Lineout Jump Count` | Lineout jumps in an activity | count |
| `Average Lineout Jump Count (Session)` | Average lineout jumps per activity | count |
| `Average Lineout Jump Count` | Average lineout jumps per period | count |
| `Kick Count` | Detected big kicks in an activity | count |
| `Kicks Per Min` | Kicks ÷ activity duration | count/min |
| `Average Kick Count` | Average kicks detected | count |

Source for all rows: [Rugby Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/360001447456-Rugby-Parameter-Definitions). Connect API events: `rugby_union_scrum` (`confidence`, `duration`, `post_event_load`, `post_event_active`), `rugby_union_contact_involvement` (`confidence`, `duration`, `active_percentage`, `post_event_load`, `post_event_active`, `post_event_back_in_game_time`), `rugby_union_kick` (`confidence`, `class`: box kick, conversion or penalty, drop kick, play punt, punt or free kick, not a kick), and `rugby_union_lineout` (`confidence`). These are machine-learning inertial algorithms ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). Device axis inversion affects scrums and lineouts for waist-front devices ([Device Location Setting](https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics)).

### Rugby league

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `rugby_league_tackle`: `intensity_load` | Load during a tackle event, detected as a change of orientation, then impact, then return upright | accumulated PlayerLoad units |
| `rugby_league_tackle`: `duration` | Event duration | s |
| `rugby_league_tackle`: `impact_load` | Impact component | raw PlayerLoad units |

Source: [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data).

### Football (soccer): Football Movement Profile and goalkeeping

Football Movement Profile (FMP) classifies movement into dynamic (multi-directional) and linear categories at low, medium, and high intensity, using one-second segments. It is available live and post-activity on S7, G7, or X7 devices and needs the FootballMovementProfile module ([How to Detect FMP Metrics](https://support.catapultsports.com/hc/en-us/articles/360001601736-How-to-Detect-Football-Movement-Profile-FMP-Metrics)). The FMP parameter definitions and thresholds article needs a sign-in. The Connect API `football_movement_analysis` event returns a `movement_type`: Low_Intensity, Running_Medium_Intensity, Running_High_Intensity, Dynamic_Medium_Intensity, or Dynamic_High_Intensity (Very_Low_Intensity is stored but not reported) ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). FMP parameter names and thresholds are Not published publicly.

Goalkeeping V2 ([How to Detect Goal Keeper Dives](https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField)):

| Vendor name | Vendor definition (paraphrased) | Default bands | Unit |
|---|---|---|---|
| `Dive Load` | Intensity of each dive | 0 to 6, 6 to 9, 9+ | load units (API: five load units) |
| `Time to Feet` | Time to return upright after a dive | 0 to 1, 1 to 1.5, 1.5+ | s |
| `Dive Count` | Number of detected dives | No numeric default; dives are also grouped by direction (left, centre, right) | count |

Other goalkeeping facts: team settings `Dive Load RHIE` default 3 and `Dive Confidence %` default 50% ([How to Detect Goal Keeper Dives](https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField)). GK V1 combines `IMA Dive Intensity Band`, dive direction, and `IMA Dive Return Band` ([How to Detect Goal Keeper Dives](https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField)). Connect API `goalkeeping_v2` returns `direction` (left 10, right 4, middle 0), `load`, `time_to_feet`, `pre_event_load`, `impact_load`, and `post_event_load`. `goalkeeping_v1` returns `intensity` (g, negative for left dives) and `time_to_feet` ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). The Dive Load formula is Not published.

### Ice hockey

Settings ([How to Detect Ice Hockey Metrics](https://support.catapultsports.com/hc/en-us/articles/360001465176-How-to-Detect-Ice-Hockey-Metrics)):

- `Hockey Bout Dwell Time (Seconds)`: minimum duration for a bout.
- `Hockey Player Load Bout Threshold`: minimum Player Load in a bout.
- Stride Force bands.
- Athlete weight must be correct because some parameters use it.

Default values for all four are Not published. The Ice Hockey Parameter Definitions article needs a sign-in.

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `ice_hockey_stride`: `acceleration` | Acceleration magnitude of a skating stride | g |
| `ice_hockey_stride`: `direction` | Side the stride started from (left 10, right 4) | code |
| `ice_hockey_bout`: `max_load` | Peak load in a bout, based on banded Player Load and time | smoothed PlayerLoad units |
| `ice_hockey_bout`: `duration` | Bout length | s |
| `ice_hockey_mp`: `movement_type` | Skating, Skating_High, Dynamic, Dynamic_High, Rotation_High, Mobile, Engaged, Ready (Passive not reported) | code |

Source: [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data). Catapult says it offers 45 hockey-specific metrics in a downloadable brochure ([LA Kings goalie metrics](https://www.catapult.com/blog/la-kings-goalie-metrics-360-view-of-every-player)). The brochure was not read for this page.

Ice hockey goalie analytics need S7, G7, or T6 devices, Console 3.4 or later, the IceHockeyModule, and a position abbreviation of `G` or `GK` ([How to Detect Ice Hockey Goalie Analytics](https://support.catapultsports.com/hc/en-us/articles/4406552770831-How-to-Detect-Ice-Hockey-Goalie-Analytics)). The definitions article needs a sign-in. Catapult's public blog names four metrics ([LA Kings goalie metrics](https://www.catapult.com/blog/la-kings-goalie-metrics-360-view-of-every-player)):

| Vendor name | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `Down Count` | Times the goalie drops from feet to knees in a blocking position | count |
| `Goalie Load` | Volume of goalie work in a session | Not published |
| `Goalie Load per Minute` | Goalie Load over session duration | Not published |
| `Asymmetry` | Volume and intensity of left and right movements | Not published |

Catapult's Ice Hockey Auto Shift Detection identifies active shifts from the wearables. Per-minute values computed over active shifts differ sharply from values over the whole session ([Ice Hockey Auto Shift Detection](https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads)).

### American football

Needs the Lineman Contact plugin and module, Football Throws, and Football Impacts. Bands: `Contact Load`, `Throw Load`, `Impact Load`. For Impact Load and Throw Load only Bands 1 to 5 apply ([How to Detect American Football Metrics](https://support.catapultsports.com/hc/en-us/articles/360001491695-How-to-Detect-American-Football-Metrics)). The American Football Parameter Definitions article needs a sign-in.

| Vendor name (Connect API event: attribute) | Vendor definition (paraphrased) | Unit |
|---|---|---|
| `us_football_lineman_contact`: `total_load` | Player Load during contact at the line of scrimmage | accumulated PlayerLoad units |
| `us_football_throw`: `confidence` | Confidence of the detected throw | % |
| `us_football_throw`: `total_load` | Player Load during the throw | accumulated PlayerLoad units |
| `us_football_throw`: `yaw` | Rotation rate | deg/s |
| `us_football_impact`: `confidence` | Confidence of the detected collision | % |
| `us_football_impact`: `total_load` | Player Load during the collision | accumulated PlayerLoad units |

Source: [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data).

### Baseball

Baseball V2 detects pitches, throws, and swings, separates pitches from throws, and labels pitch delivery as stretch or windup. Needs the Baseball.V2 module and Console 3.4 or later ([How to Detect Baseball Metrics](https://support.catapultsports.com/hc/en-us/articles/360001439835-How-to-Detect-Baseball-Metrics)). The parameter definitions article needs a sign-in.

| Vendor name (Connect API event) | Attributes | Units |
|---|---|---|
| `baseball_pitch_v1` | `confidence`, `max_player_load` | %, accumulated PlayerLoad units |
| `baseball_pitch` (v2) | `confidence`, `max_player_load`, `forward_load_pct`, `side_load_pct`, `up_load_pct`, `max_rotation`, `delivery_type` (stretch 1, windup 0) | %, PlayerLoad units, %, %, %, circles/s, code |
| `baseball_swing_v1` | `confidence`, `max_player_load`, `forward_load_pct`, `side_load_pct`, `up_load_pct`, `max_rotation` | as above |
| `baseball_swing` (v2) | same as swing v1 | as above |
| `baseball_throw` (v2) | same as swing v1 | as above |

Source: [Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data). The `forward_load_pct`, `side_load_pct`, and `up_load_pct` fields suggest a per-axis split of Player Load. The split method is Not published.

### Cricket

Catapult states that cricket parameter definitions are not public ([How to Detect Cricket Metrics](https://support.catapultsports.com/hc/en-us/articles/360001443875-How-to-Detect-Cricket-Metrics)). The Connect API lists two delivery events ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)):

| Vendor name (Connect API event) | Attributes | Units |
|---|---|---|
| `cricket_delivery_au` (with Cricket Australia) | `delivery_velocity`, `runup_distance`, `delivery_load`, `delivery_yaw`, `delivery_roll`, `delivery_resultant`, `runup_velocity`, `delivery_runup_avg_velocity`, `delivery_runup_max_velocity` | km/h, m, smoothed PlayerLoad units, deg/s, deg/s, g, m/s, m/s, m/s |
| `cricket_delivery` (with the ECB) | `confidence`, `total_load`, `max_load`, `max_runup_velocity`, `delivery_runup_velocity`, `peak_rotation`, `delivery_velocity` | %, accumulated PlayerLoad units, smoothed PlayerLoad units, m/s, m/s, deg/s, m/s |

## Connect API exports

The Connect API is the main export route for OpenField data ([Connect API index](https://docs.connect.catapultsports.com/llms.txt)). Its parameter list is account-specific. `GET /parameters` returns each parameter's `name`, `original_name`, `base_name`, `band`, `aggregation`, `group_by`, `slug`, `unit_type`, and `calculation` ([Connect API: Get all Parameters](https://docs.connect.catapultsports.com/reference/getparameters)). The endpoint needs a bearer token, so the full parameter list is Not published publicly. `unit_type` is one of: arbitrary (empty string), count, distance, duration, percentage, speed, or weight ([Connect API: Get all Parameters](https://docs.connect.catapultsports.com/reference/getparameters)). Calculated parameters expose their formula in `calculation`, for example `$velocity_band1_total_distance+$velocity_band2_total_distance` ([Connect API: Get all Parameters](https://docs.connect.catapultsports.com/reference/getparameters)).

The stats endpoint must be called separately for activities and for periods. It has a 60 second timeout ([Connect API FAQ](https://docs.connect.catapultsports.com/docs/frequently-asked-questions-faqs)).

### 10 Hz sensor stream fields

| Field | Meaning, as published | Source |
|---|---|---|
| `ts` | Timestamp, seconds | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity) |
| `cs` | Timestamp, centiseconds | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity) |
| `lat`, `long` | Latitude, longitude | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `o` | Odometer, accumulated | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `v` | Velocity, instantaneous | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `a` | Acceleration, instantaneous | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `hr` | Heart rate, instantaneous | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `pl` | Player Load, accumulated | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `pli` | Instantaneous Player Load | [Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity) |
| `mp` | Metabolic power | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `sl` | Smooth load, instantaneous | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `pq` | Positional quality, % | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `ref` | Satellites (GPS) or ClearSky receivers (LPS) used in the fix | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `hdop` | Horizontal dilution of precision, GPS only | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `rv` | Raw velocity, instantaneous | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `alt` | Altitude | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `face` | Facing direction | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |
| `xy` | Field x, y coordinates | [Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz) |

Notes ([Connect API: Sensor Data](https://docs.connect.catapultsports.com/reference/sensor-data-10hz), [Connect API: 10 Hz Sensor Data endpoint](https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity)):

- The stream can also return `id`, the database identifier of each record.
- `x, y` default to the distance from the field's bottom-left corner. The unit is not stated. This page reads it as metres. `xy_middle=1` measures from the centre. `lps_field=1` uses a generic LPS field.
- The endpoint can resample up to 20 Hz. Upsampling interpolates and adds no measured detail. The default is no resampling.
- You can query live data instead of the default post-activity data.
- Set a flag to return null instead of zero for invalid positions.
- The difference between `v` and `rv` (filtered versus raw velocity) is implied by the names. The filter is Not published.

### Effort and event exports

The Connect API exports efforts and events as follows:

- Efforts: `velocity` (band 1 to 8) and `acceleration` (band −3 to 3) with start and end times, speeds, peak value, and distance ([Connect API: Efforts Data](https://docs.connect.catapultsports.com/reference/efforts-data)).
- Events: 28 event types, each listed in the sport sections above or in the IMA, jumps, and running symmetry sections ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). The full list: `ima_acceleration`, `ima_jump`, `ima_impact`, `goalkeeping_v1`, `goalkeeping_v2`, `cricket_delivery_au`, `cricket_delivery`, `running_symmetry`, `ice_hockey_mp`, `ice_hockey_stride`, `ice_hockey_bout`, `baseball_pitch_v1`, `baseball_pitch`, `baseball_swing_v1`, `baseball_swing`, `baseball_throw`, `free_running`, `football_movement_analysis`, `rugby_union_scrum`, `rugby_union_contact_involvement`, `rugby_union_kick`, `rugby_union_lineout`, `rugby_league_tackle`, `us_football_lineman_contact`, `us_football_throw`, `us_football_impact`, `basketball`, `tennis`.
- The events available in an account are configured by Catapult staff by sport ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)).

### OpenField Console exports

OpenField Console exports data in these ways:

- 10 Hz sensor CSV and a CTR CSV export from Console. 100 Hz CSV exports are generated when a raw file is processed in Console. For Vector 8, raw files go to the Cloud through the dock, so you must download raw files and import them into Console to get 100 Hz exports ([Downloading 10Hz and 100Hz Data Back to Console](https://support.catapultsports.com/hc/en-us/articles/12803971257103-Downloading-10Hz-and-100Hz-Data-Back-to-Console-VECTOR-8)).
- Efforts and events tables, work-rate intervals, and maximum intensity intervals export to CSV from Console widgets ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events), [What are Work Rate Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals), [What are Maximum Intensity Intervals?](https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals)).

## Perch (weight room velocity-based training)

Perch has been owned by Catapult since the acquisition Catapult announced on 2025-06-05. The announcement was an ASX release naming Perch (Catalyft Labs, Inc.) ([Catapult ASX release: Catapult acquires Perch](https://announcements.asx.com.au/asxpdf/20250605/pdf/06kg3qmc80p28y.pdf)).

Perch is a different kind of product from Vector. It uses a rack-mounted 3D depth camera, not a wearable. Each pixel carries a depth value. Perch algorithms find the bar or body part and convert it to a 3D position ([How Does Perch's Technology Work?](https://perch.catapultsports.com/hc/en-us/articles/13221048860687-How-Does-Perch-s-Technology-work), [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)). The camera frame rate is Not published.

The Perch pages at support.perch.fit (`how-are-you-defining-metrics`, `csv-export`, and `exporting-aggregated-data-tonnage-volume-and-sets`) could not be retrieved on 2026-10-02. The full CSV column list and the tonnage formula are therefore Not published in any source cited here.

### Coordinate system and core signals

Perch publishes these facts about its coordinate system and core signals:

- Z is up and down (parallel to gravity). X is forwards and backwards from the athlete's view. Y is side to side ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- The 3D path is a time-stamped sequence of 3D positions. Every other metric comes from this path ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- Jumps are tracked from the athlete's head, not the bar ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- Perch deletes some "ghost reps" automatically, using the whole set as context. The rules are exercise-specific, so picking the right exercise matters ([Frequent Ghost Reps](https://perch.catapultsports.com/hc/en-us/articles/13221016118415-Frequent-Ghost-Reps)).
- Wrong values usually come from another object in view or the bar leaving the frame ([Values Seem Wrong or Frequent Missed Reps](https://perch.catapultsports.com/hc/en-us/articles/13221002633871-Values-Seem-Wrong-or-Frequent-Missed-Reps)).
- Perch states it is valid and reliable and links to a case study. The case study was not read for this page ([What is Perch's Accuracy and Reliability?](https://perch.catapultsports.com/hc/en-us/articles/13221076279439-What-is-Perch-s-Accuracy-and-Reliability)).

### Perch metrics

#### Displacement (m)

The fields for this metric are:

- **Vendor name:** Displacement ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** How far the bar moved between two points, for example squat depth on the Z axis.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): End position minus start position. Taking only the Z axis gives vertical displacement ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `Δz = z_end − z_start`.
- **Inputs:** 3D camera path.
- **Units:** Not stated. Velocities are in m/s, so this page reads it as metres.
- **Variants:** Per axis.
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Choice of start and end points.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Mean Velocity` (m/s)

The fields for this metric are:

- **Vendor name:** Mean Velocity (concentric and eccentric, stored separately) ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** Average bar speed over the lift.
- **Window or phase:** Speed-zone goals based on Mean Velocity: Absolute Strength below 0.5 m/s, Accelerative Strength 0.50 to 0.75, Strength Speed 0.75 to 1.0, Speed Strength 1.0 to 1.3, Starting Strength above 1.3 m/s ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **Calculation:**
  - Vendor definition (paraphrased): Displacement on the Z axis from the bottom of the rep to the top, divided by the time between those two points. For Olympic lifts, only the propulsive phase is used ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `MV = (z_top − z_bottom) ÷ (t_top − t_bottom)`.
- **Inputs:** 3D path.
- **Units:** m/s.
- **Variants:** Rep level and set level (set average, best rep, set minimum) in reports ([Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights), [Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch)). Strength movements default to mean metrics ([How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch)).
- **Comparison with standard methods or other vendors:** Standard methods: Perch credits the five zones to research by Dr. Bryan Mann ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)). That research was not read for this page. Other vendors: Not published.
- **What changes the number:** Rep start and end detection. Olympic-lift phase rule.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App), [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights), [Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch), [How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch).

#### `Mean Propulsive Velocity` (MPV, m/s)

The fields for this metric are:

- **Vendor name:** Mean Propulsive Velocity (MPV) ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** Average bar speed during only the part of the lift where the athlete accelerates the bar.
- **Window or phase:** None.
- **Calculation:**
  - Formula as published: `MPV = (P1 − P0) / (t1 − t0)` over the propulsive phase ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: Displacement over the propulsive phase divided by its duration. How Perch finds the end of the propulsive phase is Not published.
- **Inputs:** 3D path.
- **Units:** m/s.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Propulsive-phase detection.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Peak Velocity` (m/s)

The fields for this metric are:

- **Vendor name:** Peak Velocity ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** The fastest bar speed during the movement.
- **Window or phase:** `Ballistic` goals use Peak Velocity, with a minimum only by default ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **Calculation:**
  - Vendor definition (paraphrased): The largest velocity between any two consecutive coordinates from the lowest to the highest point ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `PV = max_i (z_{i+1} − z_i) ÷ (t_{i+1} − t_i)`.
- **Inputs:** 3D path.
- **Units:** m/s.
- **Variants:** Ballistic and Olympic movements default to peak metrics ([How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Camera frame rate (Not published) and any smoothing (Not published). A single-frame difference is sensitive to noise.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App), [How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch).

#### `Eccentric Time` (s)

The fields for this metric are:

- **Vendor name:** Eccentric Time ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** How long the lowering phase took.
- **Window or phase:** Goals of above 1, 2, 3, 4, or 5 s, or manual ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **Calculation:**
  - Vendor definition (paraphrased): The time between the top of the rep and the lowest point ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `t_bottom − t_top`.
- **Inputs:** 3D path.
- **Units:** s.
- **Variants:** Not shown on the tablet for Olympic lifts or jumps ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **Comparison with standard methods or other vendors:** Not applicable for standard methods. Not published for other vendors.
- **What changes the number:** Top and bottom detection.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App).

#### `Mean Power` (W)

The fields for this metric are:

- **Vendor name:** Mean Power ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** Average power put into the bar during the lift.
- **Window or phase:** None.
- **Calculation:**
  - Formula as published: `Mean Power = m × 9.8 × V`, where `m` is bar mass in kg and `V` is mean velocity in m/s ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)). Perch reasons that the bar is at rest before and after the lift, so average force equals the bar's weight.
  - Restatement, not a vendor statement: `P̄ = m g v̄`, with `g = 9.8 m/s²`. Perch writes the unit of 9.8 as m/s; it is m/s².
- **Inputs:** Bar load entered on the tablet, 3D path.
- **Units:** W (by the formula). The unit label is Not published.
- **Variants:** Rep and set aggregates.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** The load entered. Reading, not stated by the vendor: the formula uses bar mass only, so body mass does not count, for example in squats.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Peak Power` (W)

The fields for this metric are:

- **Vendor name:** Peak Power ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** The highest instant power during the lift.
- **Window or phase:** None.
- **Calculation:**
  - Formula as published: For every sample, compute instantaneous velocity `V` and acceleration `a` from consecutive positions, then `Peak Power = m × a × V`. Take the largest value ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `P_peak = max_i (m × a_i × V_i)`. Reading, not stated by the vendor: this formula has no gravity term, while `Mean Power` uses gravity only, so the two use different force terms.
- **Inputs:** Bar load, 3D path.
- **Units:** W (by the formula).
- **Variants:** Power curve for Olympic and ballistic lifts ([How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Double differentiation of position amplifies camera noise. Any filter is Not published.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [How Do I View an Individual Athlete's Data?](https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch).

#### `Time to Peak Power` (T2PP, s)

The fields for this metric are:

- **Vendor name:** Time to Peak Power, shown as `T2PP` ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** How quickly the athlete reaches peak power.
- **Window or phase:** None.
- **Calculation:** Time from the start of the concentric phase to the sample with peak power ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **Inputs:** 3D path, load.
- **Units:** s.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Concentric start detection, peak power noise.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Time to Peak Velocity` (T2PV, s)

The fields for this metric are:

- **Vendor name:** Time to Peak Velocity, shown as `T2PV` ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** How quickly the bar reaches top speed.
- **Window or phase:** None.
- **Calculation:** Time from the start of the concentric phase to peak velocity ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **Inputs:** 3D path.
- **Units:** s.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Concentric start detection.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Velocity at 100ms` (V100, m/s)

The fields for this metric are:

- **Vendor name:** Velocity at 100ms, shown as `V100` ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** Bar speed early in the lift, as a sign of explosiveness.
- **Window or phase:** None.
- **Calculation:** Bar velocity within the first 100 ms of the concentric phase ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)). Whether this is the speed at 100 ms or the mean over 0 to 100 ms is Not published.
- **Inputs:** 3D path.
- **Units:** m/s.
- **Variants:** None.
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Concentric start detection, frame rate.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Work` (kJ)

The fields for this metric are:

- **Vendor name:** Work, and `Total Work` in aggregates ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview)).
- **What it measures:** Energy the athlete put into the bar.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): `W = F × d`, where `F` is the average force on the bar and `d` is displacement. Reported in kJ ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: With Perch's mean-force assumption, `W ≈ m × 9.8 × Δz ÷ 1000` kJ per rep. How reps and sets are summed into `Total Work` is Not published.
- **Inputs:** Load, 3D path.
- **Units:** kJ.
- **Variants:** Per user over a time range in the Set History Users tab ([Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview)).
- **Comparison with standard methods or other vendors:** Not published.
- **What changes the number:** Load entered, range of motion.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview).

#### Jump metrics: `Jump Height`, `Time To Takeoff`, `Takeoff Velocity`, `RSIMod`, `Rep Count`

The fields for this metric are:

- **Vendor name:** Jump Height, Time To Takeoff, Takeoff Velocity, RSIMod (also written RSImod or RSI Modified), and Rep Count, for CMJ (Arms Fixed), CMJ (Arms Swing), and Continuous Jumps ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch)).
- **What it measures:** Jump output from head tracking.
- **Window or phase:** Readiness status uses an athlete's z-score: green above 1, yellow between −1 and −2, red at −2 or below ([Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights)). The published bands leave −1 to 1 unassigned.
- **Calculation:**
  - Vendor definitions ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)): Standing height is the head position before the jump. Takeoff is when the head returns to standing height after the push. Jump Height is apex height minus standing height. Time To Takeoff runs from the start of unweighting to takeoff (unweighting, braking, and propulsive phases). Takeoff Velocity is the instantaneous velocity at takeoff. RSIMod is Jump Height ÷ Time To Takeoff, reported without a unit.
  - Restatement, not a vendor statement: `RSImod = h ÷ t_TT`.
- **Inputs:** 3D path of the head.
- **Units:** Time To Takeoff in s. Height and takeoff velocity units are Not published on the pages cited here. RSIMod has no unit by Perch's choice.
- **Variants:** Standard-tier Evaluate customers see Jump Height only ([Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch)). Set reports offer Set Min, Best Rep, and Set Avg ([Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch)).
- **Comparison with standard methods or other vendors:** Standard methods: Perch measures head displacement, not centre-of-mass displacement. No comparison with force plates is published. Other vendors: Kinexon reports `Jump Height` from an IMU ([Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf)). Perch uses a camera on the head. Not interchangeable.
- **What changes the number:** Standing posture, head movement, arm swing variant.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Analyzing Evaluate Assessments](https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch), [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights), [Kinexon PERFORM IMU brochure](https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf).

#### `Estimated 1RM` and `Minimum Velocity Threshold` (MVT)

The fields for this metric are:

- **Vendor name:** Estimated 1RM (e1RM), MVT ([Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs), [Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)).
- **What it measures:** The predicted one-rep max from load and bar speed.
- **Window or phase:** Profiles start after the athlete has used at least two loads separated by more than 30 lb (about 13 kg) ([Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)). Another Perch page says 40 lb or more across multiple sessions ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)). The sources disagree.
- **Calculation:**
  - Vendor definition (paraphrased): Perch fits a load-velocity line from set history and takes the load where the line meets the MVT. Every tracked exercise has a default MVT. Coaches can override it per exercise or per athlete (premium feature) ([Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs), [Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)).
  - Restatement, not a vendor statement: Fit `v = a + b × load`. Then `e1RM = (MVT − a) ÷ b`. Perch describes a line of best fit through the set history ([Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)) and also refers to a velocity curve ([Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs)). Default MVT values are Not published.
- **Inputs:** Load and mean velocity history.
- **Units:** kg or lb; MVT in m/s.
- **Variants:** Entered 1RM, Estimated 1RM, or Linked 1RM (a percentage of another exercise). An asterisk marks e1RM with a changed MVT ([Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Not applicable.
- **What changes the number:** MVT. A higher MVT lowers e1RM ([Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs)). Effort level and load spread ([Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)).
- **Source links:** [Setting MVTs, 1RMs and Estimated 1RMs](https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs), [Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling), [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch).

#### `Speed Score`, `Strength Score`, `Total Performance Score`

The fields for this metric are:

- **Vendor name:** Speed Score, Strength Score, Total Performance Score (Perch Performance Scores) ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **What it measures:** Where an athlete's load-velocity profile sits compared with their group.
- **Window or phase:** None.
- **Calculation:**
  - Vendor definition (paraphrased): Speed Score is a z-score of the profile's velocity intercept (unloaded max velocity). Strength Score is a z-score of the load intercept, similar to an estimated 1RM. Total Performance Score weights the two equally ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
  - Restatement, not a vendor statement: `Speed = (v₀ − mean_group) ÷ SD_group`. `Strength = (L₀ − mean_group) ÷ SD_group`. `Total = (Speed + Strength) ÷ 2`. The reference group and whether Total is a mean or a sum are Not published.
- **Inputs:** Load-velocity profile per exercise.
- **Units:** z-score.
- **Variants:** Team Exercise dashboard ([Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights)).
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Not applicable.
- **What changes the number:** The group used for normalisation.
- **Source links:** [Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch), [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights).

#### Dynamic velocity goal zone

The fields for this metric are:

- **Vendor name:** Dynamic goal ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **What it measures:** A personal target speed zone for a given load.
- **Window or phase:** −5% and +7.5%.
- **Calculation:** Perch finds the velocity midpoint for the entered load on the athlete's profile, then sets the zone from 5% below to 7.5% above the midpoint. The profile updates after every lift ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **Inputs:** Load-velocity profile.
- **Units:** m/s.
- **Variants:** Professional and Championship tiers only.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Not applicable.
- **What changes the number:** Profile updates after each lift.
- **Source links:** [Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App).

#### `% Drop` goal

The fields for this metric are:

- **Vendor name:** % Drop ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **What it measures:** Velocity loss within a set, as a fatigue stop rule.
- **Window or phase:** 5%, 10%, 15%, or 20%, or manual.
- **Calculation:** A rep is flagged when it falls more than the set percentage below the first rep or the best rep ([Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App)).
- **Inputs:** Rep velocities.
- **Units:** %.
- **Variants:** First-rep or best-rep reference.
- **Comparison with standard methods or other vendors:** Standard methods: Not published. Other vendors: Not applicable.
- **What changes the number:** Reference rep choice.
- **Source links:** [Setting Goals in the Perch App](https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App).

### Perch aggregates and exports

| Name | What Perch publishes | Source |
|---|---|---|
| Sets | Set counts by exercise and by day; sets per user | [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview) |
| Reps | Reps per set; completed versus prescribed in Compliance | [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights) |
| Tonnage | Shown per user and in Compliance. The formula is Not published on the pages cited here. | [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview), [Perch PLAN](https://perch.catapultsports.com/hc/en-us/articles/13220766942991-Perch-PLAN) |
| Total Work | Per user over a time range, in kJ | [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview) |
| Volume | Train Sets report exports "sets, reps, volume". The meaning of volume is Not published. On some pages "volume" means set count. | [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights), [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview) |
| Goal Accuracy | How often reps or sets land inside the goal zone. Above or below the zone counts as inaccurate. | [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview) |
| Compliance % | Inside a prescribed range = 100%. Below = % of the lower bound. Above = % of the upper bound. Daily totals use the range maximum. `>` and `<` mean ≥ and ≤. | [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights) |
| Time in Velocity Zones | Count of sets by set-average mean velocity in the five zones | [Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview) |
| Personal Best | Best rep or best set average by rep count, or by %1RM in 5% buckets (lower edge included, upper excluded). Untracked sets are excluded. | [Personal Best Report](https://perch.catapultsports.com/hc/en-us/articles/14423298918287-Personal-Best-Report) |
| Readiness | Most recent jump session versus the previous session and the 30-day average, with a z-score status | [Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights) |
| Exercise Variables | Up to 4 per exercise: Reps, Weight (kg, lb, %1RM), Time, Distance, Height, RIR, RPE, Calories, Heart Rate (bpm), Watts (untracked power). For tracked exercises, Reps and Weight are fixed. | [Exercise Variables](https://perch.catapultsports.com/hc/en-us/articles/16667443904527-Exercise-Variables) |

Export routes: Insights reports export to CSV. Train Sets is the general data export at set or rep level. Rep level shows within-set change and left-right asymmetry for lower-body unilateral exercises ([Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights)). An API token is available on some service tiers ([Generating an API Token](https://perch.catapultsports.com/hc/en-us/articles/13220068158735-Generating-an-API-Token)). Perch lists integrations with Teamworks (formerly Smartabase), Kinduct, Apollo, RockDaisy, Teambuildr, and Kitman Labs ([Does Perch Integrate with Third Party Software?](https://perch.catapultsports.com/hc/en-us/articles/13221006091151-Does-Perch-Integrate-with-Third-Party-Software)). The CSV column list and API schema are Not published on the pages cited here.

What changes Perch numbers across reports: the organisation's default weight unit drives exports ([Customizing Your Organization's Settings](https://perch.catapultsports.com/hc/en-us/articles/13220015798799-Customizing-Your-Organization-s-Settings)). The `Sets` versus `Reps` level in Train Sets gives different results for the same columns ([Perch Insights](https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights)). Coaches can edit sets after the session, including weight, athlete, exercise, and ghost reps ([Perch TRAIN Overview](https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview)).

## Conflicts in the vendor's own sources

Catapult's public pages disagree with each other, or contain an error or gap that changes how you read a value, in these cases:

- **Catapult One sprint threshold.** One Catapult One page gives 7 m/s ([Catapult One Players Metrics Explanation](https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation)). Two give 5 m/s ([Catapult One Complete Metrics Guide](https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches), [Know your core metrics](https://one.catapultsports.com/blog/know-your-metrics/)). A help article adds that the athlete must hold more than 5 m/s (18 km/h) for at least 1 second ([How is sprint distance measured?](https://onesupport.catapultsports.com/hc/en-us/articles/9436632476303-How-is-sprint-distance-measured)). Treat the threshold as unconfirmed for older app versions. See the `Sprint Distance` (Catapult One) block.
- **Accelerometer sampling.** A 2018 Catapult article says its accelerometers measured at 10,000 Hz and recorded at 100 Hz ([Catapult Fundamentals: GPS tracking](https://www.catapult.com/blog/catapult-fundamentals-gps-tracking-technology)). The Vector X7 page says 400 Hz, smoothed to 100 Hz for PlayerLoad ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)). The 2018 text is an older device description. Treat the X7 figure as the device-specific value.
- **Acceleration band numbering.** On Vector 7 Bluetooth activities, Catapult says Accelerations and Decelerations each default to bands 1 to 3 ([Parameter Selection During Bluetooth Activities](https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7)). In the `Gen2Acceleration` band set, accelerations are Bands 6 to 8 and decelerations are Bands 1 to 3 ([Configuring Acceleration & Deceleration Bands](https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands)). See the `Acceleration Efforts` block.
- **`Time Since Last`.** The OpenField Console table counts the time since the previous effort in any band ([Table of Efforts / Events](https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events)). The OpenField Cloud Efforts Breakdown counts the time since the previous effort in the same band ([Efforts Breakdown](https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown)). Check which view produced your export.
- **Player Load formula image.** The formula image on the Vector Core page does not show the division by 100. The text on the same page does ([What is Player Load? (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load)).
- **Number of Vector Core metrics.** The post-activity list has 43 rows ([Post-Activity Parameters](https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters)), while the launch post says "up to 43" ([Vector Core launch](https://www.catapult.com/blog/vector-core-load-management-simplified)). The live list has 13 rows ([Vector App Parameter Definitions](https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions)), while the launch post says 11 live metrics.
- **Football benchmark table headers.** The source table of default sport benchmarks repeats the header "Accel+Decel" for the last column. This page reads that column as per minute. The duration unit is not labelled, and this page reads it as minutes ([How is the MD Comparison Calculated Prior to Your First Match?](https://core.catapultsports.com/hc/en-us/articles/8789796545935-How-is-the-MD-Comparison-Calculated-Prior-to-Your-First-Match)).
- **Osgnach citation year.** Catapult cites Osgnach et al. as 2010 in the text and 2009 in its reference list ([What is Metabolic Power?](https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power)). The Crossref record shows the issue date as 2010-01 ([Osgnach et al. 2010](https://doi.org/10.1249/MSS.0b013e3181ae5cfd)).
- **Tennis rotation unit.** The Connect API page describes the rotation unit as degrees per second or (radians/2π)/s ([Connect API: Events Data](https://docs.connect.catapultsports.com/reference/events-data)). The tennis parameter page gives revolutions per second ([Tennis Parameter Definitions](https://support.catapultsports.com/hc/en-us/articles/10024959888655-Tennis-Parameter-Definitions)). Treat the unit as revolutions per second, which matches the parameter page and (radians/2π)/s.
- **Perch Mean Power unit.** Perch writes the unit of 9.8 as m/s. It is m/s² ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).
- **Perch load-velocity profile start.** Perch Load Velocity Profiling says profiles start after the athlete has used at least two loads separated by more than 30 lb ([Perch Load Velocity Profiling](https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling)). Another Perch page says 40 lb or more across multiple sessions ([Metrics Measured by Perch](https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch)).

## Not published

The table lists every metric block where at least one field is Not published, in full or in part. Notes on other vendors are left out because almost all are Not published.

| Area | Metric | Fields marked Not published, in full or in part |
|---|---|---|
| Distance and speed | `Distance` (m) | Calculation, Comparison with standard methods or other vendors |
| Distance and speed | `Max Velocity` (m/s) | Comparison with standard methods or other vendors, What changes the number |
| Distance and speed | `Work/Rest Ratio` (ratio) | Window or phase, Comparison with standard methods or other vendors |
| Distance and speed | `Distance` (Catapult One) | Calculation, Comparison with standard methods or other vendors, What changes the number |
| Distance and speed | `Top Speed` (Catapult One) | Comparison with standard methods or other vendors |
| Distance and speed | `Work Ratio` (Catapult One, %) | Comparison with standard methods or other vendors |
| Velocity bands | `Standing Distance` (m), Velocity Band 1 | Comparison with standard methods or other vendors |
| Velocity bands | `Walking Distance` (m), Velocity Band 2 | Comparison with standard methods or other vendors |
| Velocity bands | `Jogging Distance` (m), Velocity Band 3 | Comparison with standard methods or other vendors |
| Velocity bands | `Running Distance` (m), Velocity Band 4 | Comparison with standard methods or other vendors |
| Velocity bands | `Sprint Distance` (m), Velocity Band 6 | What changes the number |
| Velocity bands | `Sprint Efforts` (count) | Calculation |
| Velocity bands | `HS Efforts` (count) | Calculation, What changes the number |
| Velocity bands | `Velocity Distance Band 1 - 8` (m), live | Comparison with standard methods or other vendors |
| Velocity bands | `Velocity Efforts Band 2+` (count), live | Comparison with standard methods or other vendors, What changes the number |
| Velocity bands | `Velocity (Set 2)` banded metrics (relative bands) | Window or phase |
| Velocity bands | Vector Live custom speed parameters | Window or phase |
| Velocity bands | Velocity effort attributes (Efforts Breakdown and Connect API) | Window or phase |
| Velocity bands | `Sprint Distance` (Catapult One) | Comparison with standard methods or other vendors |
| Accelerations and decelerations | `Max Acceleration` (m/s²) | Calculation |
| Accelerations and decelerations | `Max Deceleration` (m/s²) | Calculation |
| Accelerations and decelerations | `Acceleration Efforts` (count) | Calculation |
| Accelerations and decelerations | `Deceleration Efforts` (count) | Calculation |
| Accelerations and decelerations | `Acceleration load` (sum of absolute acceleration) | Calculation, Units, What changes the number |
| Accelerations and decelerations | `Acceleration density` (mean absolute acceleration) | Units |
| Accelerations and decelerations | `Acceleration density index` (per 10 m) | Units |
| Accelerations and decelerations | `Max Acceleration` and `Max Deceleration` (Catapult One) | Calculation, Window or phase, Comparison with standard methods or other vendors |
| PlayerLoad and accelerometer load | `Player Load` (AU) | Window or phase, Units, What changes the number |
| PlayerLoad and accelerometer load | Instantaneous Player Load (`pli`) | Calculation |
| PlayerLoad and accelerometer load | Player Load bands and Vector Live custom Player Load parameters | Window or phase |
| PlayerLoad and accelerometer load | Smooth Load (`sl`) | Calculation, Window or phase, Comparison with standard methods or other vendors, What changes the number |
| Metabolic power and HMLD | Metabolic Power (`mp`, W/kg) | Window or phase, Variants |
| Metabolic power and HMLD | `Energy` | Calculation, Inputs, Units, Comparison with standard methods or other vendors, What changes the number |
| Metabolic power and HMLD | Peak Metabolic Power (W/kg) | Comparison with standard methods or other vendors |
| Metabolic power and HMLD | Metabolic power bands and efforts | Window or phase, Comparison with standard methods or other vendors |
| Metabolic power and HMLD | `Energy` (Catapult One, kcal) | Calculation, Comparison with standard methods or other vendors |
| Metabolic power and HMLD | `Power Plays` (Catapult One, count) | Calculation, What changes the number |
| Metabolic power and HMLD | `Power Score` (Catapult One, W/kg) | Calculation, Comparison with standard methods or other vendors, What changes the number |
| Metabolic power and HMLD | `Power` (Catapult One player view) | Calculation, Window or phase, Units, Comparison with standard methods or other vendors, What changes the number |
| Heart rate | `Avg Heart Rate` (bpm) | Calculation |
| Heart rate | `Heart Rate Exertion` (Vector Core, AU) | Calculation |
| Load scores | `Volume` (%) | Comparison with standard methods or other vendors |
| Load scores | `Overall` (%) | Calculation |
| Load scores | Acute:Chronic Workload Ratio (OpenField chart) | Calculation, Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | `Impacts` (Vector Core, count) | Calculation, Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | `Impacts` (Catapult One, count) | Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | IMA Acceleration count | Vendor name, Window or phase, Comparison with standard methods or other vendors |
| Impacts and IMA events | IMA Deceleration count | Window or phase, Comparison with standard methods or other vendors |
| Impacts and IMA events | IMA Change of Direction Left and Right | Window or phase, Comparison with standard methods or other vendors |
| Impacts and IMA events | IMA intensity event (`ima_acceleration`) | Window or phase, Comparison with standard methods or other vendors |
| Impacts and IMA events | IMA Impact event (`ima_impact`) | Window or phase, Comparison with standard methods or other vendors |
| Impacts and IMA events | Free running (IMA and `free_running` event) | Window or phase, Inputs, Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | Average stride rate (IMA) | Calculation, Window or phase, Units, Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | Asymmetrical loading (IMA) | Calculation, Window or phase, Units, Comparison with standard methods or other vendors, What changes the number |
| Impacts and IMA events | Tackle and impact event tables | Window or phase, Comparison with standard methods or other vendors |
| Jumps | IMA Jump (`ima_jump`, height in m) | Calculation, Window or phase, Comparison with standard methods or other vendors |
| Jumps | Jump Height export (OpenField Console) | Window or phase, Comparison with standard methods or other vendors |
| Jumps | Indoor Jumps (T7 Indoor Analytics) | Window or phase, Comparison with standard methods or other vendors |
| Jumps | Estimated distance (T7 Indoor Analytics) | Calculation, Window or phase, Units, Comparison with standard methods or other vendors |
| Jumps | Live Jumps | Calculation, Window or phase, Comparison with standard methods or other vendors, What changes the number |
| Intervals and repeated efforts | Repeat High Intensity Efforts (RHIE) | Window or phase, Variants, Comparison with standard methods or other vendors |
| Intervals and repeated efforts | `Work Rate - % Distance` (%) | Comparison with standard methods or other vendors, What changes the number |
| Intervals and repeated efforts | `Work Rate - Duration` (s) | Comparison with standard methods or other vendors |
| Intervals and repeated efforts | `Work Rate - Interval Count` (count) | Comparison with standard methods or other vendors |
| Intervals and repeated efforts | `Work Rate - Interval Distance` (m) | Comparison with standard methods or other vendors |
| Running symmetry | `Running Imbalance` (%) | Calculation, Comparison with standard methods or other vendors |
| Running symmetry | `Footstrikes` (count) | Comparison with standard methods or other vendors |
| Running symmetry | `Running Imbalance Standard Deviation` (%) | Comparison with standard methods or other vendors |
| Running symmetry | `Running Series #` (count) | Comparison with standard methods or other vendors |
| Perch | `Mean Propulsive Velocity` (MPV, m/s) | Calculation, Comparison with standard methods or other vendors |
| Perch | `Peak Velocity` (m/s) | Comparison with standard methods or other vendors, What changes the number |
| Perch | `Mean Power` (W) | Units, Comparison with standard methods or other vendors |
| Perch | `Peak Power` (W) | Comparison with standard methods or other vendors, What changes the number |
| Perch | `Time to Peak Power` (T2PP, s) | Comparison with standard methods or other vendors |
| Perch | `Time to Peak Velocity` (T2PV, s) | Comparison with standard methods or other vendors |
| Perch | `Velocity at 100ms` (V100, m/s) | Calculation, Comparison with standard methods or other vendors |
| Perch | `Work` (kJ) | Calculation, Comparison with standard methods or other vendors |
| Perch | Jump metrics: `Jump Height`, `Time To Takeoff`, `Takeoff Velocity`, `RSIMod`, `Rep Count` | Units |
| Perch | `Estimated 1RM` and `Minimum Velocity Threshold` (MVT) | Calculation, Comparison with standard methods or other vendors |
| Perch | `Speed Score`, `Strength Score`, `Total Performance Score` | Calculation, Comparison with standard methods or other vendors |
| Perch | Dynamic velocity goal zone | Comparison with standard methods or other vendors |
| Perch | `% Drop` goal | Comparison with standard methods or other vendors |

In the sport-specific tables, these items are Not published for every sport: the load formulas (`basketball_load`, `tennis_load`, Dive Load, Goalie Load), all default band values except the goalkeeping V2 bands, the FMP and ice hockey parameter definitions, and every cricket parameter definition (Catapult states cricket definitions are not public ([How to Detect Cricket Metrics](https://support.catapultsports.com/hc/en-us/articles/360001443875-How-to-Detect-Cricket-Metrics))).

Product-level items that are Not published:

- The full OpenField and OpenField Cloud parameter list. It sits behind a sign-in, and the API list is account-specific and needs a token ([Connect API: Get all Parameters](https://docs.connect.catapultsports.com/reference/getparameters)).
- Catapult's GNSS and LPS velocity filters ([Vector T7 white paper](https://www.catapult.com/blog/vector-t7-white-paper)).
- The Gen2 velocity and acceleration effort rules beyond the 0.9 s minimum for accelerations.
- The default `Gen2Acceleration` band table. The Vector Core Bands page refers to an image that did not display ([Bands (Vector Core)](https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands)).
- The Perch CSV column list, the Perch API schema, the tonnage formula, and the Perch camera frame rate.

### Pages not publicly readable

The pages in this table could not be used as sources, for the reason shown:

| Page | Reason |
|---|---|
| OpenField Cloud Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360000531996 | Sign-in required |
| Vector Live Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360002610575 | Sign-in required |
| Vector Smartwatch App Parameters Definitions, https://support.catapultsports.com/hc/en-us/articles/360001935876 | Sign-in required |
| Vector Smartphone App Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360001935636 | Sign-in required |
| What is Acceleration (Gen1)?, https://support.catapultsports.com/hc/en-us/articles/360000522695 | Sign-in required |
| What is Acceleration Generation 2 (Gen2)?, https://support.catapultsports.com/hc/en-us/articles/360000519736 | Sign-in required |
| What is Velocity (Gen1)?, https://support.catapultsports.com/hc/en-us/articles/360001465076 | Sign-in required |
| What is Velocity Generation 2 (Gen2)?, https://support.catapultsports.com/hc/en-us/articles/360000517496 | Sign-in required |
| What is Velocity (Set 2)?, https://support.catapultsports.com/hc/en-us/articles/360001452336 | Sign-in required |
| What is Dwell Time?, https://support.catapultsports.com/hc/en-us/articles/360001457876 | Sign-in required |
| LPS TDOA Acceleration Effort Algorithm, https://support.catapultsports.com/hc/en-us/articles/14065524352783 | Sign-in required |
| Indoor Analytics Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/6692007771023 | Sign-in required |
| Indoor Analytics Explained, https://support.catapultsports.com/hc/en-us/articles/10176498499599 | Sign-in required |
| American Football Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360001500256 | Sign-in required |
| Baseball Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360001456896 | Sign-in required |
| Baseball Series Overview & Verification, https://support.catapultsports.com/hc/en-us/articles/360001355676 | Sign-in required |
| Basketball Movement Profile (BMP) Explained, https://support.catapultsports.com/hc/en-us/articles/10060483865359 | Sign-in required |
| Cricket Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360001461256 | Sign-in required |
| Football Movement Profile (FMP) Parameter Definitions and Thresholds, https://support.catapultsports.com/hc/en-us/articles/360001604296 | Sign-in required |
| Goalkeeping Parameters (V2) Definitions, https://support.catapultsports.com/hc/en-us/articles/360001457916 | Sign-in required |
| Ice Hockey Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/360001450135 | Sign-in required |
| Ice Hockey Goalie Parameter Definitions, https://support.catapultsports.com/hc/en-us/articles/4407065202319 | Sign-in required |
| Ice Hockey Goalie Analytics Explained, https://support.catapultsports.com/hc/en-us/articles/4408190885647 | Sign-in required |
| Ice Hockey Auto Shift Detection Validation, https://support.catapultsports.com/hc/en-us/articles/14051837627535 | Sign-in required |
| Rugby Lineout Jumps Explained, https://support.catapultsports.com/hc/en-us/articles/10065681101967 | Sign-in required |
| Tennis Analytics Explained, https://support.catapultsports.com/hc/en-us/articles/10024987311247 | Sign-in required |
| Contact Involvement Explained, https://support.catapultsports.com/hc/en-us/articles/4514785772559 | Sign-in required |
| Learning Hub sections (Best Practice & Tips, Reference Values by Sport, Expert Insights & Deep Dives, 5-in-5 Series), https://support.catapultsports.com/hc/en-us/articles/16795353175311 and the matching Vector Core sections | Public welcome pages only; content needs a sign-in |
| IMA white paper download, https://go.catapult.com/inertial-movement-analysis-whitepaper | Form submission required; not used |
| Catapult hockey metrics brochure (45 metrics), linked from https://www.catapult.com/blog/la-kings-goalie-metrics-360-view-of-every-player | Not read (download behind a link) |
| Default `Gen2Acceleration` band table image on https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands | Image did not display |
| Connect API `GET /parameters` and `POST /stats` live data | Need a bearer token |
| https://support.perch.fit/how-are-you-defining-metrics | Could not be retrieved on 2026-10-02 |
| https://support.perch.fit/csv-export | Could not be retrieved on 2026-10-02 |
| https://support.perch.fit/exporting-aggregated-data-tonnage-volume-and-sets | Could not be retrieved on 2026-10-02 |
| Perch accuracy case study linked from https://perch.catapultsports.com/hc/en-us/articles/13221076279439 | Not read |
| Full texts of the peer-reviewed papers | Not read; only titles and metadata on Crossref and abstracts on Europe PMC were used |

## Worked examples

All numbers below come from the script in [Code](#code) and the output in [Output](#output). Run it with Python 3.9.6 and NumPy 2.0.2. The results here are from 2026-10-02. The data is synthetic. Where Catapult does not publish a step, the script states its assumption.

### Example 1: a 60 s speed trace at 10 Hz

Input: 600 samples. The trace stands, walks, jogs, accelerates at 2.5 m/s² from 3 to 8 m/s, sprints for 5 s, decelerates at 3.0 m/s² to 2 m/s, runs, builds to 6.5 m/s, makes a 0.3 s surge at about 2.3 m/s² to 7.2 m/s, and eases off. The trace is continuous.

Assumptions: Distance is speed × 0.1 s summed. Bands include the lower edge and exclude the upper edge. Acceleration is the first difference of speed with no filter.

| Metric | Result |
|---|---|
| Total distance | 216.02 m |
| `Standing Distance` (0 to 0.2 m/s) | 0.51 m |
| `Walking Distance` (0.2 to 2) | 14.91 m |
| `Jogging Distance` (2 to 4) | 53.83 m |
| `Running Distance` (4 to 5.5) | 44.10 m |
| `HI Distance` (5.5 to 7) | 53.11 m |
| `Sprint Distance` (above 7) | 49.56 m |
| `HS Distance` | 102.67 m |
| `Meterage Per Minute` | 216.02 m/min |
| `HS Dist Per Min` | 102.67 m/min |
| `Sprint Dist Per Min` | 49.56 m/min |
| `Work/Rest Ratio` | 24.9 s ÷ 15.4 s = 1.617 |
| `Sprint Efforts`, no minimum time / 1.0 s minimum | 2 / 1 |
| `HS Efforts`, no minimum time / 1.0 s minimum | 2 / 2 |
| `Max Acceleration` / `Max Deceleration` | 2.50 / −3.00 m/s² |
| `Acceleration Efforts` at 2 m/s², no minimum / 0.9 s minimum | 2 / 1 |
| `Deceleration Efforts`, no minimum / 0.9 s minimum | 1 / 1 |
| `Accel&Decel Efforts`, no minimum / 0.9 s minimum | 3 / 2 |
| `Acceleration density` (mean of absolute acceleration) | 0.354 m/s² |
| `Acceleration Efforts` after a 0.5 s moving average on speed | 1 |

What this shows a coach: the banded distances add up to the total. The effort counts change with the minimum-duration rule and with smoothing, even though the speed trace does not change. The 0.5 s surge above 7 m/s adds sprint distance but only counts as a sprint effort if no minimum time applies.

### Example 1b: metabolic power at constant speed

Using Catapult's published polynomial and terrain constant, at constant speed `ES = 0` and `EM = 1`:

| Speed | Energy cost | Metabolic power |
|---|---|---|
| 4.0 m/s | 4.6440 J/kg/m | 18.576 W/kg |
| 5.5 m/s | 4.6440 J/kg/m | 25.542 W/kg |
| 7.0 m/s | 4.6440 J/kg/m | 32.508 W/kg |

The speed that gives exactly 25.5 W/kg is 5.491 m/s. This confirms that the HMLD default of 25.5 W/kg matches running at 5.5 m/s.

### Example 2: PlayerLoad from a 100 Hz tri-axial accelerometer

Input: 10 s at 100 Hz (1,000 samples). Forward, sideways, and vertical signals in g, with a 2.8 Hz step rhythm, a 1 g vertical offset, and small noise (seed 42). Assumption: the acceleration unit is g.

| Metric | Result |
|---|---|
| PlayerLoad 3D (sum ÷ 100) | 1.491 AU |
| PlayerLoad 2D (vertical axis dropped) | 0.934 AU |
| 2D as a share of 3D | 62.6% |
| `Player Load Per Minute`, 3D / 2D | 8.947 / 5.605 AU/min |
| Single-axis load: forward / sideways / vertical | 0.611 / 0.576 / 1.016 AU |
| 3D with the 1 g offset removed | 1.491 AU (unchanged) |
| 3D after decimating to 50 Hz | 1.123 AU |
| 3D without the ÷100 | 149.1 |

What this shows a coach: dropping the vertical axis removes most of the running signal, so 2D suits sports with little running. The sampling rate changes the number. A constant offset does not.

### Example 3: Heart Rate Exertion

Input: seconds in heart rate bands 1 to 6 of 600, 420, 480, 900, 300, and 60 (2,760 s in total).

| Metric | Result |
|---|---|
| Vector Core weights (1, 1.2, 1.5, 2.2, 4.5, 9), durations in seconds | 5,694.0 |
| Same, durations in minutes | 94.90 |
| `Red Zone` (Band 5 + Band 6) | 360 s = 6.0 min |
| OpenField weights (1, 1.122, 1.322, 1.554, 2.037, 3.252, 5.439, 9.0) on the same seconds in bands 1 to 6 | 3,910.6 |

Per-band products with Vector Core weights: 600.0, 504.0, 720.0, 1,980.0, 1,350.0, and 540.0.

What this shows a coach: the time unit changes the number by a factor of 60. The two Catapult products use different weights, so HRE from Vector Core and from OpenField are not directly comparable.

### Code

Copy the script below into a file and run it with `python3`. It needs NumPy.

```python
"""Worked examples for the Catapult metric reference.

Every number in the reference file that comes from a worked example is printed by this script.
Synthetic data only. No vendor code is used. Where Catapult does not publish a processing step,
the script states the assumption it makes.
"""
import numpy as np

np.set_printoptions(precision=3, suppress=True)
print("=" * 72)
print("EXAMPLE 1. Speed series at 10 Hz")
print("=" * 72)

DT = 0.1  # 10 Hz
# Build a 60 s speed trace (m/s) from simple phases. Each phase: (duration s, start speed, end speed)
# The trace is continuous: each phase starts at the speed where the last one ended.
phases = [
    (5.0, 0.1, 0.1),   # standing
    (1.0, 0.1, 1.5),   # 1.4 m/s^2 build
    (9.0, 1.5, 1.5),   # walking
    (1.0, 1.5, 3.0),   # 1.5 m/s^2 build
    (9.0, 3.0, 3.0),   # jogging
    (2.0, 3.0, 8.0),   # acceleration at 2.5 m/s^2
    (5.0, 8.0, 8.0),   # sprint
    (2.0, 8.0, 2.0),   # deceleration at 3.0 m/s^2
    (9.0, 2.0, 2.0),   # slow running
    (2.0, 2.0, 5.0),   # 1.5 m/s^2 build
    (6.0, 5.0, 5.0),   # running
    (2.0, 5.0, 6.5),   # 0.75 m/s^2 build
    (2.0, 6.5, 6.5),   # high-intensity running
    (0.3, 6.5, 7.2),   # brief surge at about 2.3 m/s^2
    (0.3, 7.2, 7.2),   # brief time above 7 m/s
    (0.5, 7.2, 6.5),   # ease off
    (2.2, 6.5, 6.5),   # high-intensity running
    (1.7, 6.5, 5.0),   # ease off
]
v = []
for dur, v0, v1 in phases:
    n = int(round(dur / DT))
    v.extend(np.linspace(v0, v1, n, endpoint=False))
v = np.array(v)
t = np.arange(len(v)) * DT
duration_s = len(v) * DT
print(f"Samples: {len(v)}  Duration: {duration_s:.1f} s")

# Distance: integrate speed over time (rectangle rule, one sample = 0.1 s).
step_dist = v * DT
total_distance = step_dist.sum()
print(f"Total distance: {total_distance:.2f} m")

# Catapult Vector Core default velocity bands (m/s), from Post-Activity Parameters.
bands = {
    "Standing Distance (B1, 0-0.2)": (0.0, 0.2),
    "Walking Distance (B2, 0.2-2)": (0.2, 2.0),
    "Jogging Distance (B3, 2-4)": (2.0, 4.0),
    "Running Distance (B4, 4-5.5)": (4.0, 5.5),
    "HI Distance (B5, 5.5-7)": (5.5, 7.0),
    "Sprint Distance (B6, >7)": (7.0, np.inf),
}
band_dist = {}
for name, (lo, hi) in bands.items():
    # Assumption: lower edge inclusive, upper edge exclusive. Catapult does not publish edge handling.
    mask = (v >= lo) & (v < hi)
    band_dist[name] = step_dist[mask].sum()
    print(f"  {name:32s} {band_dist[name]:8.2f} m   time {mask.sum() * DT:5.1f} s")
print(f"  Sum of bands: {sum(band_dist.values()):.2f} m")
hs = band_dist["HI Distance (B5, 5.5-7)"] + band_dist["Sprint Distance (B6, >7)"]
sprint = band_dist["Sprint Distance (B6, >7)"]
mins = duration_s / 60
print(f"HS Distance (B5 + B6): {hs:.2f} m")
print(f"Sprint Distance (B6): {sprint:.2f} m")
print(f"Meterage Per Minute: {total_distance / mins:.2f} m/min")
print(f"HS Dist Per Min: {hs / mins:.2f} m/min")
print(f"Sprint Dist Per Min: {sprint / mins:.2f} m/min")

# Work/Rest Ratio (Vector Core): time above 3 m/s divided by time below 2 m/s.
work_t = (v > 3.0).sum() * DT
rest_t = (v < 2.0).sum() * DT
print(f"Work/Rest Ratio: time > 3 m/s = {work_t:.1f} s, time < 2 m/s = {rest_t:.1f} s, ratio = {work_t / rest_t:.3f}")

# Band entry counts (efforts). Catapult does not publish its public dwell-time rule for Gen2 velocity efforts.
def count_runs(mask, min_len_samples=1):
    runs, n = 0, 0
    for m in list(mask) + [False]:
        if m:
            n += 1
        else:
            if n >= min_len_samples:
                runs += 1
            n = 0
    return runs

for dwell in (0.0, 1.0):
    k = max(1, int(round(dwell / DT)))
    print(f"Sprint Efforts (v > 7), min time in band {dwell:.1f} s: {count_runs(v > 7.0, k)}")
    print(f"HS Efforts (v > 5.5), min time in band {dwell:.1f} s: {count_runs(v > 5.5, k)}")

# Acceleration from speed. Assumption: simple first difference of the 10 Hz speed, no extra filter.
a = np.diff(v, prepend=v[0]) / DT
print(f"Max Acceleration: {a.max():.2f} m/s^2   Max Deceleration: {a.min():.2f} m/s^2")
for min_dur in (0.0, 0.9):
    k = max(1, int(round(min_dur / DT)))
    acc = count_runs(a > 2.0, k)
    dec = count_runs(a < -2.0, k)
    print(f"Acceleration Efforts (> 2 m/s^2), min duration {min_dur:.1f} s: {acc}")
    print(f"Deceleration Efforts (< -2 m/s^2), min duration {min_dur:.1f} s: {dec}")
    print(f"Accel&Decel Efforts: {acc + dec}   per minute: {(acc + dec) / mins:.2f}")
def run_lengths(mask):
    out, n = [], 0
    for m in list(mask) + [False]:
        if m:
            n += 1
        elif n:
            out.append(round(n * DT, 1))
            n = 0
    return out
print(f"Durations of runs with a > 2 m/s^2 (s): {run_lengths(a > 2.0)}")
print(f"Durations of runs with a < -2 m/s^2 (s): {run_lengths(a < -2.0)}")
print(f"Durations of runs with v > 7 m/s (s): {run_lengths(v > 7.0)}")
print(f"Durations of runs with v > 5.5 m/s (s): {run_lengths(v > 5.5)}")

# Acceleration Density: average of absolute acceleration values over the period.
print(f"Acceleration Density (mean |a|, no smoothing): {np.abs(a).mean():.3f} m/s^2")

# Effect of a light smoothing filter on the acceleration effort count (illustration only).
kernel = np.ones(5) / 5  # 0.5 s moving average on speed; not Catapult's filter
v_s = np.convolve(v, kernel, mode="same")
a_s = np.diff(v_s, prepend=v_s[0]) / DT
print(f"With a 0.5 s moving average on speed: Max Acceleration {a_s[5:-5].max():.2f} m/s^2, "
      f"Acceleration Efforts (> 2 m/s^2, any duration): {count_runs(a_s > 2.0)}")

print()
print("Example 1b. Metabolic power at constant speed (Catapult support article constants)")
def fn(es):
    return 155.4 * es**5 - 30.4 * es**4 - 43.3 * es**3 + 46.3 * es**2 + 19.5 * es + 3.6
KT = 1.29
for speed in (5.5, 4.0, 7.0):
    es, em = 0.0, 1.0  # constant speed on flat ground: no equivalent slope, equivalent mass = 1
    ec = fn(es) * em * KT
    mp = ec * speed
    print(f"  v = {speed:.1f} m/s: EC = {ec:.4f} J/kg/m, MP = {mp:.3f} W/kg")
print(f"  Speed at which MP = 25.5 W/kg at constant speed: {25.5 / (fn(0) * KT):.3f} m/s")

print()
print("=" * 72)
print("EXAMPLE 2. PlayerLoad from a tri-axial accelerometer at 100 Hz")
print("=" * 72)
rng = np.random.default_rng(42)
FS = 100
dur = 10.0
tt = np.arange(0, dur, 1 / FS)
step_hz = 2.8  # running cadence, steps per second
# Synthetic signals in g. Vertical carries gravity (1 g) plus foot-strike oscillation.
fwd = 0.30 * np.sin(2 * np.pi * step_hz * tt) + 0.05 * rng.standard_normal(tt.size)
side = 0.15 * np.sin(2 * np.pi * step_hz / 2 * tt) + 0.05 * rng.standard_normal(tt.size)
up = 1.0 + 0.80 * np.sin(2 * np.pi * step_hz * tt + 0.5) + 0.05 * rng.standard_normal(tt.size)

def playerload(f, s, u, scale=100.0):
    df, ds, du = np.diff(f), np.diff(s), np.diff(u)
    inst = np.sqrt(df**2 + ds**2 + du**2)
    return inst.sum() / scale, inst

pl3, inst3 = playerload(fwd, side, up)
pl2, _ = playerload(fwd, side, np.zeros_like(up))
print(f"Samples: {tt.size} over {dur:.0f} s")
print(f"PlayerLoad 3D (sum of instantaneous values / 100): {pl3:.3f} AU")
print(f"PlayerLoad 2D (vertical axis dropped):            {pl2:.3f} AU")
print(f"2D as a share of 3D: {100 * pl2 / pl3:.1f} %")
print(f"PlayerLoad per minute (3D): {pl3 / (dur / 60):.3f} AU/min;  (2D): {pl2 / (dur / 60):.3f} AU/min")
# Single-axis sums for context (each axis alone through the same formula).
for name, sig in (("forward", fwd), ("sideways", side), ("vertical", up)):
    print(f"  Single-axis load, {name:8s}: {np.abs(np.diff(sig)).sum() / 100:.3f} AU")
# Gravity offset: a constant 1 g on the vertical axis does not change the result (differences cancel it).
pl3_nog, _ = playerload(fwd, side, up - 1.0)
print(f"PlayerLoad 3D with the 1 g offset removed: {pl3_nog:.3f} AU (same as above)")
# Sampling rate: decimate to 50 Hz and recompute.
pl3_50, _ = playerload(fwd[::2], side[::2], up[::2])
print(f"PlayerLoad 3D after decimating to 50 Hz: {pl3_50:.3f} AU")
# Scaling factor: without the /100.
print(f"PlayerLoad 3D without the /100 scaling: {pl3 * 100:.1f}")

print()
print("=" * 72)
print("EXAMPLE 3. Heart Rate Exertion from band durations")
print("=" * 72)
dur_s = np.array([600, 420, 480, 900, 300, 60], dtype=float)  # seconds in HR bands 1-6
w_core = np.array([1.0, 1.2, 1.5, 2.2, 4.5, 9.0])  # Vector Core Post-Activity Parameters
print("Band durations (s):", dur_s.astype(int).tolist(), " total", int(dur_s.sum()), "s")
hre_core_s = (dur_s * w_core).sum()
print(f"Vector Core HRE with durations in seconds: {hre_core_s:.1f}")
print(f"Vector Core HRE with durations in minutes: {(dur_s / 60 * w_core).sum():.2f}")
print(f"Red Zone (Band 5 + Band 6): {dur_s[4] + dur_s[5]:.0f} s = {(dur_s[4] + dur_s[5]) / 60:.1f} min")
w_of = np.array([1.0, 1.122, 1.322, 1.554, 2.037, 3.252, 5.439, 9.0])  # OpenField support article, 8 bands
dur8 = np.concatenate([dur_s, [0.0, 0.0]])
print(f"OpenField 8-band weights applied to the same seconds in bands 1-6: {(dur8 * w_of).sum():.1f}")
print("  (Only an illustration of weight sensitivity: the OpenField band edges are user set, so the")
print("   same session would not fall into the same eight bands.)")
for i, (d, w) in enumerate(zip(dur_s, w_core), 1):
    print(f"  Band {i}: {d:5.0f} s x {w:4.1f} = {d * w:7.1f}")
```

### Output

Output of the run on 2026-10-02 (Python 3.9.6, NumPy 2.0.2):

```text
========================================================================
EXAMPLE 1. Speed series at 10 Hz
========================================================================
Samples: 600  Duration: 60.0 s
Total distance: 216.02 m
  Standing Distance (B1, 0-0.2)        0.51 m   time   5.1 s
  Walking Distance (B2, 0.2-2)        14.91 m   time  10.3 s
  Jogging Distance (B3, 2-4)          53.83 m   time  21.0 s
  Running Distance (B4, 4-5.5)        44.10 m   time   8.9 s
  HI Distance (B5, 5.5-7)             53.11 m   time   8.4 s
  Sprint Distance (B6, >7)            49.56 m   time   6.3 s
  Sum of bands: 216.02 m
HS Distance (B5 + B6): 102.67 m
Sprint Distance (B6): 49.56 m
Meterage Per Minute: 216.02 m/min
HS Dist Per Min: 102.67 m/min
Sprint Dist Per Min: 49.56 m/min
Work/Rest Ratio: time > 3 m/s = 24.9 s, time < 2 m/s = 15.4 s, ratio = 1.617
Sprint Efforts (v > 7), min time in band 0.0 s: 2
HS Efforts (v > 5.5), min time in band 0.0 s: 2
Sprint Efforts (v > 7), min time in band 1.0 s: 1
HS Efforts (v > 5.5), min time in band 1.0 s: 2
Max Acceleration: 2.50 m/s^2   Max Deceleration: -3.00 m/s^2
Acceleration Efforts (> 2 m/s^2), min duration 0.0 s: 2
Deceleration Efforts (< -2 m/s^2), min duration 0.0 s: 1
Accel&Decel Efforts: 3   per minute: 3.00
Acceleration Efforts (> 2 m/s^2), min duration 0.9 s: 1
Deceleration Efforts (< -2 m/s^2), min duration 0.9 s: 1
Accel&Decel Efforts: 2   per minute: 2.00
Durations of runs with a > 2 m/s^2 (s): [2.0, 0.3]
Durations of runs with a < -2 m/s^2 (s): [2.0]
Durations of runs with v > 7 m/s (s): [5.7, 0.5]
Durations of runs with v > 5.5 m/s (s): [6.8, 7.8]
Acceleration Density (mean |a|, no smoothing): 0.354 m/s^2
With a 0.5 s moving average on speed: Max Acceleration 2.50 m/s^2, Acceleration Efforts (> 2 m/s^2, any duration): 1

Example 1b. Metabolic power at constant speed (Catapult support article constants)
  v = 5.5 m/s: EC = 4.6440 J/kg/m, MP = 25.542 W/kg
  v = 4.0 m/s: EC = 4.6440 J/kg/m, MP = 18.576 W/kg
  v = 7.0 m/s: EC = 4.6440 J/kg/m, MP = 32.508 W/kg
  Speed at which MP = 25.5 W/kg at constant speed: 5.491 m/s

========================================================================
EXAMPLE 2. PlayerLoad from a tri-axial accelerometer at 100 Hz
========================================================================
Samples: 1000 over 10 s
PlayerLoad 3D (sum of instantaneous values / 100): 1.491 AU
PlayerLoad 2D (vertical axis dropped):            0.934 AU
2D as a share of 3D: 62.6 %
PlayerLoad per minute (3D): 8.947 AU/min;  (2D): 5.605 AU/min
  Single-axis load, forward : 0.611 AU
  Single-axis load, sideways: 0.576 AU
  Single-axis load, vertical: 1.016 AU
PlayerLoad 3D with the 1 g offset removed: 1.491 AU (same as above)
PlayerLoad 3D after decimating to 50 Hz: 1.123 AU
PlayerLoad 3D without the /100 scaling: 149.1

========================================================================
EXAMPLE 3. Heart Rate Exertion from band durations
========================================================================
Band durations (s): [600, 420, 480, 900, 300, 60]  total 2760 s
Vector Core HRE with durations in seconds: 5694.0
Vector Core HRE with durations in minutes: 94.90
Red Zone (Band 5 + Band 6): 360 s = 6.0 min
OpenField 8-band weights applied to the same seconds in bands 1-6: 3910.6
  (Only an illustration of weight sensitivity: the OpenField band edges are user set, so the
   same session would not fall into the same eight bands.)
  Band 1:   600 s x  1.0 =   600.0
  Band 2:   420 s x  1.2 =   504.0
  Band 3:   480 s x  1.5 =   720.0
  Band 4:   900 s x  2.2 =  1980.0
  Band 5:   300 s x  4.5 =  1350.0
  Band 6:    60 s x  9.0 =   540.0
```

## Sources

All pages were read on 2026-10-02. Catapult help centre article dates are the updated dates the help centre reported at that time. The sources are grouped by publisher:

### Catapult Vector Core help centre

The sources in this group are:

- Post-Activity Parameters: <https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters>, accessed 2026-10-02.
- What is Player Load? (Vector Core): <https://core.catapultsports.com/hc/en-us/articles/7209578939151-What-is-Player-Load>, accessed 2026-10-02.
- Understanding Volume, Intensity and Overall Load: <https://core.catapultsports.com/hc/en-us/articles/7257535900687-Understanding-Volume-Intensity-and-Overall-Load>, accessed 2026-10-02.
- Catapult Vector App - Parameter Definitions: <https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions>, accessed 2026-10-02.
- Bands (Vector Core): <https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands>, accessed 2026-10-02.
- Configuring Acceleration & Deceleration Bands: <https://core.catapultsports.com/hc/en-us/articles/7331871882255-Configuring-Acceleration-Deceleration-Bands>, accessed 2026-10-02.
- Why Do My Velocity Bands Sometimes Change Slightly After Editing Them in the Cloud? (Vector Core): <https://core.catapultsports.com/hc/en-us/articles/7352034984079-Why-Do-My-Velocity-Bands-Sometimes-Change-Slightly-After-Editing-Them-in-the-Cloud>, accessed 2026-10-02.
- How Do I Reprocess Activities?: <https://core.catapultsports.com/hc/en-us/articles/7361794930063-How-Do-I-Reprocess-Activities>, accessed 2026-10-02.
- How is the MD Comparison Calculated Prior to Your First Match?: <https://core.catapultsports.com/hc/en-us/articles/8789796545935-How-is-the-MD-Comparison-Calculated-Prior-to-Your-First-Match>, accessed 2026-10-02.
- Heatmaps and Intensity Traces: <https://core.catapultsports.com/hc/en-us/articles/8600354543887-Heatmaps-and-Intensity-Traces>, accessed 2026-10-02.
- How Do I Change the Units of Measurement Used in Metrics?: <https://core.catapultsports.com/hc/en-us/articles/8013274300815-How-Do-I-Change-the-Units-of-Measurement-Used-in-Metrics>, accessed 2026-10-02.
- Default Athlete Profile Settings: <https://core.catapultsports.com/hc/en-us/articles/7347413350159-Default-Athlete-Profile-Settings>, accessed 2026-10-02.

### Catapult support help centre (OpenField)

The sources in this group are:

- What is Player Load? (OpenField): <https://support.catapultsports.com/hc/en-us/articles/360000510795-What-is-Player-Load>, accessed 2026-10-02.
- What is IMA?: <https://support.catapultsports.com/hc/en-us/articles/360000510856-What-is-IMA>, accessed 2026-10-02.
- What is Metabolic Power?: <https://support.catapultsports.com/hc/en-us/articles/360001343976-What-is-Metabolic-Power>, accessed 2026-10-02.
- What is Gen 2 Metabolic Power?: <https://support.catapultsports.com/hc/en-us/articles/9880348689935-What-is-Gen-2-Metabolic-Power>, accessed 2026-10-02.
- Configuring Metabolic Power Settings: <https://support.catapultsports.com/hc/en-us/articles/9501243714575-Configuring-Metabolic-Power-Settings>, accessed 2026-10-02.
- How to Detect Metabolic Power Live in OpenField Console: <https://support.catapultsports.com/hc/en-us/articles/9500694248079-How-to-Detect-Metabolic-Power-Live-in-OpenField-Console>, accessed 2026-10-02.
- Acceleration load, acceleration density and acceleration density index: <https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index>, accessed 2026-10-02.
- What are Repeat High Intensity Efforts (RHIEs)?: <https://support.catapultsports.com/hc/en-us/articles/360000716535-What-are-Repeat-High-Intensity-Efforts-RHIEs>, accessed 2026-10-02.
- What is Rolling Max Velocity?: <https://support.catapultsports.com/hc/en-us/articles/360002239475-What-is-Rolling-Max-Velocity>, accessed 2026-10-02.
- What Is Heart Rate Exertion: <https://support.catapultsports.com/hc/en-us/articles/360002137375-What-Is-Heart-Rate-Exertion>, accessed 2026-10-02.
- What are Work Rate Intervals?: <https://support.catapultsports.com/hc/en-us/articles/360001476596-What-are-Work-Rate-Intervals>, accessed 2026-10-02.
- What are Maximum Intensity Intervals?: <https://support.catapultsports.com/hc/en-us/articles/360001442095-What-are-Maximum-Intensity-Intervals>, accessed 2026-10-02.
- How to Set Absolute and Relative Velocity Bands: <https://support.catapultsports.com/hc/en-us/articles/360000552555-How-to-Set-Absolute-and-Relative-Velocity-Bands>, accessed 2026-10-02.
- How to Detect Running Symmetry Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001044935-How-to-Detect-Running-Symmetry-Metrics>, accessed 2026-10-02.
- How to Create Custom Parameters: <https://support.catapultsports.com/hc/en-us/articles/360000509596-How-to-Create-Custom-Parameters>, accessed 2026-10-02.
- Bands (OpenField): <https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands>, accessed 2026-10-02.
- Why do my Velocity Bands sometimes change slightly after editing them in the Cloud? (OpenField): <https://support.catapultsports.com/hc/en-us/articles/360000675156-Why-do-my-Velocity-Bands-sometimes-change-slightly-after-editing-them-in-the-Cloud>, accessed 2026-10-02.
- Catapult Vector App - Bluetooth Live Parameters - VECTOR 7: <https://support.catapultsports.com/hc/en-us/articles/14824357639311-Catapult-Vector-App-Bluetooth-Live-Parameters-VECTOR-7>, accessed 2026-10-02.
- Parameter Selection During Bluetooth Activities - VECTOR 7: <https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7>, accessed 2026-10-02.
- How to Create Custom Parameters in the Vector Live App: <https://support.catapultsports.com/hc/en-us/articles/15764414194703-How-to-Create-Custom-Parameters-in-the-Vector-Live-App>, accessed 2026-10-02.
- Efforts Breakdown: <https://support.catapultsports.com/hc/en-us/articles/13013666028303-Efforts-Breakdown>, accessed 2026-10-02.
- Table of Efforts / Events: <https://support.catapultsports.com/hc/en-us/articles/360000526716-Table-of-Efforts-Events>, accessed 2026-10-02.
- Catapult Glossary: <https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary>, accessed 2026-10-02.
- Heart Rate Dashboard: <https://support.catapultsports.com/hc/en-us/articles/360000494295-Heart-Rate-Dashboard>, accessed 2026-10-02.
- Basketball Movement Profile (BMP) Parameter Definitions: <https://support.catapultsports.com/hc/en-us/articles/10024943670159-Basketball-Movement-Profile-BMP-Parameter-Definitions>, accessed 2026-10-02.
- How to Detect Basketball Movement Profile (BMP) Metrics: <https://support.catapultsports.com/hc/en-us/articles/10024923779471-How-to-Detect-Basketball-Movement-Profile-BMP-Metrics>, accessed 2026-10-02.
- Tennis Parameter Definitions: <https://support.catapultsports.com/hc/en-us/articles/10024959888655-Tennis-Parameter-Definitions>, accessed 2026-10-02.
- How to Detect Tennis Metrics: <https://support.catapultsports.com/hc/en-us/articles/10024968443791-How-to-Detect-Tennis-Metrics>, accessed 2026-10-02.
- Rugby Parameter Definitions: <https://support.catapultsports.com/hc/en-us/articles/360001447456-Rugby-Parameter-Definitions>, accessed 2026-10-02.
- How to Detect Goal Keeper Dives in OpenField: <https://support.catapultsports.com/hc/en-us/articles/360000443656-How-to-Detect-Goal-Keeper-Dives-in-OpenField>, accessed 2026-10-02.
- How to Detect Ice Hockey Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001465176-How-to-Detect-Ice-Hockey-Metrics>, accessed 2026-10-02.
- How to Detect Ice Hockey Goalie Analytics: <https://support.catapultsports.com/hc/en-us/articles/4406552770831-How-to-Detect-Ice-Hockey-Goalie-Analytics>, accessed 2026-10-02.
- How to Detect Indoor Analytics: <https://support.catapultsports.com/hc/en-us/articles/6692092419087-How-to-Detect-Indoor-Analytics>, accessed 2026-10-02.
- Device Location Setting - Basketball Movement Profile / Indoor Analytics: <https://support.catapultsports.com/hc/en-us/articles/14178392218255-Device-Location-Setting-Basketball-Movement-Profile-Indoor-Analytics>, accessed 2026-10-02.
- How to Detect Football Movement Profile (FMP) Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001601736-How-to-Detect-Football-Movement-Profile-FMP-Metrics>, accessed 2026-10-02.
- How to Detect American Football Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001491695-How-to-Detect-American-Football-Metrics>, accessed 2026-10-02.
- How to Detect Baseball Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001439835-How-to-Detect-Baseball-Metrics>, accessed 2026-10-02.
- How to Detect Cricket Metrics: <https://support.catapultsports.com/hc/en-us/articles/360001443875-How-to-Detect-Cricket-Metrics>, accessed 2026-10-02.
- How to Export Jump Height Data in OpenField: <https://support.catapultsports.com/hc/en-us/articles/360002282956-How-to-Export-Jump-Height-Data-in-OpenField>, accessed 2026-10-02.
- Can Live Jumps Differentiate Between Left Foot and Right Foot Jumping?: <https://support.catapultsports.com/hc/en-us/articles/6912559339279-Can-Live-Jumps-Differentiate-Between-Left-Foot-and-Right-Foot-Jumping>, accessed 2026-10-02.
- Graphing Goalkeeper Events and IMA Jumps in the Web Editor: <https://support.catapultsports.com/hc/en-us/articles/15519822056207-Graphing-Goalkeeper-Events-and-IMA-Jumps-in-the-Web-Editor>, accessed 2026-10-02.
- How Does Catapult Measure Heart Rate?: <https://support.catapultsports.com/hc/en-us/articles/360001236836-How-Does-Catapult-Measure-Heart-Rate>, accessed 2026-10-02.
- How to Enable Integrated Heart Rate: <https://support.catapultsports.com/hc/en-us/articles/360002066375-How-to-Enable-Integrated-Heart-Rate>, accessed 2026-10-02.
- How to Enable Optical Heart Rate: <https://support.catapultsports.com/hc/en-us/articles/360002740715-How-to-Enable-Optical-Heart-Rate>, accessed 2026-10-02.
- How to Set Up an Acute:Chronic Workload Ratio Chart: <https://support.catapultsports.com/hc/en-us/articles/360000538795-How-to-Set-Up-an-Acute-Chronic-Workload-Ratio-Chart>, accessed 2026-10-02.
- Best Practice for Good Data Hygiene: <https://support.catapultsports.com/hc/en-us/articles/5207893410703-Best-Practice-for-Good-Data-Hygiene>, accessed 2026-10-02.
- Downloading 10Hz and 100Hz Data Back to Console - VECTOR 8: <https://support.catapultsports.com/hc/en-us/articles/12803971257103-Downloading-10Hz-and-100Hz-Data-Back-to-Console-VECTOR-8>, accessed 2026-10-02.

### Catapult One help centre and site

The sources in this group are:

- Catapult One - Complete Metrics Guide for Coaches: <https://onesupport.catapultsports.com/hc/en-us/articles/7443807365775-Catapult-One-Complete-Metrics-Guide-for-Coaches>, accessed 2026-10-02.
- Catapult One - Players Metrics Explanation: <https://onesupport.catapultsports.com/hc/en-us/articles/7443807410447-Catapult-One-Players-Metrics-Explanation>, accessed 2026-10-02.
- How is sprint distance measured?: <https://onesupport.catapultsports.com/hc/en-us/articles/9436632476303-How-is-sprint-distance-measured>, accessed 2026-10-02.
- Can I adjust my sprint speed threshold?: <https://onesupport.catapultsports.com/hc/en-us/articles/9436643027471-Can-I-adjust-my-sprint-speed-threshold>, accessed 2026-10-02.
- How to Recalculate a Session: <https://onesupport.catapultsports.com/hc/en-us/articles/7443890603919-How-to-Recalculate-a-Session>, accessed 2026-10-02.
- What is Player Load? (Catapult One): <https://onesupport.catapultsports.com/hc/en-us/articles/7443837147023-What-is-Player-Load>, accessed 2026-10-02.
- Know your core metrics: <https://one.catapultsports.com/blog/know-your-metrics/>, accessed 2026-10-02.

### Catapult Connect API

The sources in this group are:

- Connect API index (llms.txt): <https://docs.connect.catapultsports.com/llms.txt>, accessed 2026-10-02.
- Efforts Data: <https://docs.connect.catapultsports.com/reference/efforts-data>, accessed 2026-10-02.
- Events Data: <https://docs.connect.catapultsports.com/reference/events-data>, accessed 2026-10-02.
- Sensor Data (10Hz): <https://docs.connect.catapultsports.com/reference/sensor-data-10hz>, accessed 2026-10-02.
- Get Dual Stream 10Hz Sensor Data for Athlete in Activity: <https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity>, accessed 2026-10-02.
- Parameters: <https://docs.connect.catapultsports.com/reference/parameters>, accessed 2026-10-02.
- Get all Parameters: <https://docs.connect.catapultsports.com/reference/getparameters>, accessed 2026-10-02.
- Frequently Asked Questions: <https://docs.connect.catapultsports.com/docs/frequently-asked-questions-faqs>, accessed 2026-10-02.

### Catapult blog and education pages

The sources in this group are:

- Understanding Player Load: A Comprehensive Guide to Athlete Workload Analysis (2024-01-23): <https://www.catapult.com/blog/fundamentals-playerload-athlete-work>, accessed 2026-10-02.
- White Paper: An Introduction to Inertial Movement Analysis (IMA) (2024-01-19): <https://www.catapult.com/blog/white-paper-introduction-ima>, accessed 2026-10-02.
- Catapult Fundamentals: Why use GPS tracking technology? (2018-05-17): <https://www.catapult.com/blog/catapult-fundamentals-gps-tracking-technology>, accessed 2026-10-02.
- Individualisation of GPS speed thresholds: Challenges and complexities (2017-08-29): <https://www.catapult.com/blog/individualisation-gps-speed-thresholds-challenges-complexities>, accessed 2026-10-02.
- Unlocking Game-Speed Insights: Inside Vector's New Efforts Breakdown Reporting (2025-07-15): <https://www.catapult.com/blog/vector-efforts-breakdown-game-speed-insights>, accessed 2026-10-02.
- Load Management Simplified: Vector Core (2023-05-17): <https://www.catapult.com/blog/vector-core-load-management-simplified>, accessed 2026-10-02.
- White Paper: Validation Vector T7 (2023-11-22): <https://www.catapult.com/blog/vector-t7-white-paper>, accessed 2026-10-02.
- Basketball Movement Profile: Inside the High-Tech World of Vector T7 (2023-09-04): <https://www.catapult.com/blog/vector-t7-movement-profile>, accessed 2026-10-02.
- Catapult Fundamentals: Using internal and external load to answer performance questions (2018-05-31): <https://www.catapult.com/blog/fundamentals-internal-external-load-performance-questions>, accessed 2026-10-02.
- Ice Hockey Auto Shift Detection (2026-06-19): <https://www.catapult.com/blog/ice-hockey-auto-shift-detection-a-cleaner-way-to-compare-ice-hockey-workloads>, accessed 2026-10-02.
- How the LA Kings Use New Goalie Metrics (2021-11-02): <https://www.catapult.com/blog/la-kings-goalie-metrics-360-view-of-every-player>, accessed 2026-10-02.

### Perch (Catapult)

The sources in this group are:

- Catapult ASX release, Catapult acquires Perch (2025-06-05): <https://announcements.asx.com.au/asxpdf/20250605/pdf/06kg3qmc80p28y.pdf>, accessed 2026-10-02.
- How Does Perch's Technology work?: <https://perch.catapultsports.com/hc/en-us/articles/13221048860687-How-Does-Perch-s-Technology-work>, accessed 2026-10-02.
- Metrics Measured by Perch: <https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch>, accessed 2026-10-02.
- Frequent Ghost Reps: <https://perch.catapultsports.com/hc/en-us/articles/13221016118415-Frequent-Ghost-Reps>, accessed 2026-10-02.
- Values Seem Wrong or Frequent Missed Reps: <https://perch.catapultsports.com/hc/en-us/articles/13221002633871-Values-Seem-Wrong-or-Frequent-Missed-Reps>, accessed 2026-10-02.
- What is Perch's Accuracy and Reliability?: <https://perch.catapultsports.com/hc/en-us/articles/13221076279439-What-is-Perch-s-Accuracy-and-Reliability>, accessed 2026-10-02.
- Setting Goals in the Perch App: <https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App>, accessed 2026-10-02.
- Perch Insights: <https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights>, accessed 2026-10-02.
- Analyzing Evaluate Assessments on Perch: <https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch>, accessed 2026-10-02.
- How Do I View an Individual Athlete's Data in Perch?: <https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch>, accessed 2026-10-02.
- Perch TRAIN Overview: <https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview>, accessed 2026-10-02.
- Setting MVTs, 1RMs and Estimated 1RMs: <https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs>, accessed 2026-10-02.
- Perch Load Velocity Profiling: <https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling>, accessed 2026-10-02.
- Perch PLAN: <https://perch.catapultsports.com/hc/en-us/articles/13220766942991-Perch-PLAN>, accessed 2026-10-02.
- Personal Best Report: <https://perch.catapultsports.com/hc/en-us/articles/14423298918287-Personal-Best-Report>, accessed 2026-10-02.
- Exercise Variables: <https://perch.catapultsports.com/hc/en-us/articles/16667443904527-Exercise-Variables>, accessed 2026-10-02.
- Generating an API Token: <https://perch.catapultsports.com/hc/en-us/articles/13220068158735-Generating-an-API-Token>, accessed 2026-10-02.
- Does Perch Integrate with Third Party Software?: <https://perch.catapultsports.com/hc/en-us/articles/13221006091151-Does-Perch-Integrate-with-Third-Party-Software>, accessed 2026-10-02.
- Customizing Your Organization's Settings: <https://perch.catapultsports.com/hc/en-us/articles/13220015798799-Customizing-Your-Organization-s-Settings>, accessed 2026-10-02.

### Peer-reviewed papers

The papers below are the ones cited on this page. Each DOI was checked on 2026-10-02 against `https://api.crossref.org/works/<DOI>`. Title, journal, and year matched. Abstracts were read on Europe PMC, not full texts. The list is:

- Boyd LJ, Ball K, Aughey RJ. The Reliability of MinimaxX Accelerometers for Measuring Physical Activity in Australian Football. Int J Sports Physiol Perform. 2011;6:311-321. <https://doi.org/10.1123/ijspp.6.3.311>, accessed 2026-10-02.
- Barrett S, Midgley A, Lovell R. PlayerLoad™: Reliability, Convergent Validity, and Influence of Unit Position during Treadmill Running. Int J Sports Physiol Perform. 2014;9:945-952. <https://doi.org/10.1123/ijspp.2013-0418>, accessed 2026-10-02.
- Osgnach C, Poser S, Bernardini R, Rinaldo R, di Prampero PE. Energy Cost and Metabolic Power in Elite Soccer. Med Sci Sports Exerc. 2010;42:170-178. <https://doi.org/10.1249/MSS.0b013e3181ae5cfd>, accessed 2026-10-02.
- Minetti AE, Moia C, Roi GS, Susta D, Ferretti G. Energy cost of walking and running at extreme uphill and downhill slopes. J Appl Physiol. 2002;93:1039-1046. <https://doi.org/10.1152/japplphysiol.01177.2001>, accessed 2026-10-02.
- Scott BR, Lockie RG, Knight TJ, Clark AC, Janse de Jonge XAK. A Comparison of Methods to Quantify the In-Season Training Load of Professional Soccer Players. Int J Sports Physiol Perform. 2013;8:195-202. <https://doi.org/10.1123/ijspp.8.2.195>, accessed 2026-10-02.
- Colby MJ, Dawson B, Heasman J, Rogalski B, Gabbett TJ. Accelerometer and GPS-Derived Running Loads and Injury Risk in Elite Australian Footballers. J Strength Cond Res. 2014;28:2244-2252. <https://doi.org/10.1519/JSC.0000000000000362>, accessed 2026-10-02.
- Barron D, Atkins S, Edmundson C, Fewtrell D. Accelerometer derived load according to playing position in competitive youth soccer. Int J Perform Anal Sport. 2014. <https://doi.org/10.1080/24748668.2014.11868754>, accessed 2026-10-02.
- Tierney PJ, Young A, Clarke ND, Duncan MJ. Match play demands of 11 versus 11 professional football using Global Positioning System tracking: Variations across common playing formations. Hum Mov Sci. 2016;49:1-8. <https://doi.org/10.1016/j.humov.2016.05.007>, accessed 2026-10-02.
- Varley MC, Jaspers A, Helsen WF, Malone JJ. Methodological Considerations When Quantifying High-Intensity Efforts in Team Sport Using Global Positioning System Technology. Int J Sports Physiol Perform. 2017;12:1059-1068. <https://doi.org/10.1123/ijspp.2016-0534>, accessed 2026-10-02.
- Malone JJ, Lovell R, Varley MC, Coutts AJ. Unpacking the Black Box: Applications and Considerations for Using GPS Devices in Sport. Int J Sports Physiol Perform. 2017;12:S2-18-S2-26. <https://doi.org/10.1123/ijspp.2016-0236>, accessed 2026-10-02.
- Delaney JA, Duthie GM, Thornton HR, Scott TJ, Gay D, Dascombe BJ. Acceleration-Based Running Intensities of Professional Rugby League Match Play. Int J Sports Physiol Perform. 2016;11:802-809. <https://doi.org/10.1123/ijspp.2015-0424>, accessed 2026-10-02.

Note on Varley et al. 2017: the abstract prints the high-speed and sprint thresholds with the unit m/s². From context they are speeds in m/s. This page reports them as m/s.

### Kinexon pages cited in comparison notes

The sources in this group are:

- Kinexon blog, three player metrics (volume, intensity, density): <https://kinexon-sports.com/blog/data-analytics-in-sports/>, accessed 2026-10-02.
- Kinexon blog, Mechanical Load in basketball: <https://kinexon-sports.com/blog/mechanical-load-basketball/>, accessed 2026-10-02.
- Kinexon PERFORM IMU brochure (volleyball): <https://hs.kinexon.com/hubfs/SPO-Volleyball%20Collaterals/KINEXON%20PERFORM%20IMU_Brochure_Volleyball_EN.pdf>, accessed 2026-10-02.
- Kinexon PERFORM LPS product page: <https://kinexon-sports.com/products/perform-lps/>, accessed 2026-10-02.
- Kinexon blog, sports performance data in bowl season: <https://kinexon-sports.com/blog/sports-performance-data-bowl-season/>, accessed 2026-10-02.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
