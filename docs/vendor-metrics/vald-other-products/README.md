# VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics

This page explains how the metrics in the exports of five measurement products are calculated. ForceFrame measures isometric force on paddle sensors. DynaMo measures handheld isometric force and range of motion. SmartSpeed measures timing gate splits, sprint profiles, and jump mat times. HumanTrak measures joint angles and positions with markerless 3D tracking. GymAware measures barbell or body displacement, velocity, power, and force for each rep. GymAware has been owned by VALD since VALD announced the acquisition on 2026-08-10 ([source](https://www.valdperformance.com/news/vald-acquires-gymaware-bringing-the-gold-standard-in-velocity-based-training-into-the-worlds-leading-performance-technology-ecosystem)). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](../vald-forcedecks-nordbord/README.md).

Checked against: the VALD knowledge base, VALD education pages, the VALD OpenAPI specs, the `valdr` R package 4.0.0, the GymAware Cloud API guide, and the GymAware help center, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

## How to read these pages

Each metric block names the exact field or Hub name and then lists these items, where the sources give them:

- What it measures.
- Window or phase.
- Calculation: the vendor's definition in paraphrase, then the formula in plain math where the vendor or a cited source gives one.
- Inputs and units.
- Variants.
- Comparison with standard methods or other vendors, only where a source supports it.
- What changes the number.
- Source links.

A formula labeled Restated is a plain restatement on these pages, not the vendor's statement. "Not published" means the vendor does not publish that detail in the public sources checked. It does not mean the vendor lacks the information. None of the VALD OpenAPI specs carry field descriptions, so VALD definitions come from the VALD knowledge base, VALD education pages, and the `valdr` R package.

## Pages in this set

The metrics are split into one page for each product:

- [ForceFrame metrics](forceframe.md)
- [DynaMo metrics](dynamo.md)
- [SmartSpeed metrics](smartspeed.md)
- [HumanTrak metrics](humantrak.md)
- [GymAware metrics](gymaware.md)

The SmartSpeed page includes a worked example for split times and start methods. The GymAware page includes a worked example for velocity, power, and velocity loss.

## Summary tables

Each table lists the metric blocks on the product page. The last column says whether the vendor publishes the calculation: Yes, Partly, or Not published. A block can cover several variant fields, for example left, right, Max, and Avg.

### ForceFrame

ForceFrame measures: isometric force on four paddles (inner and outer, left and right). Details are on [the ForceFrame page](forceframe.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `innerLeftMaxForce` and variants | Highest force on one sensor in the test ("Peak force") | N | Partly |
| `innerLeftAvgForce` and variants | Average force on one sensor in the test | N (unit not stated in the spec) | Not published |
| Imbalance (%) | Percentage difference between left and right max force | % | Partly |
| Strength ratio (inner:outer) | Inner max force compared with outer max force | Unitless | Partly |
| `innerLeftMaxForcePerKg` and variants | Force relative to body mass ("Peak force / BM") | N/kg | Partly |
| `innerLeftMaxRFDNewtonsPerSecond` and variants | Steepest rise in force over time ("Peak RFD") | N/s | Partly |
| `innerLeftMaxRFD50msNewtonsPerSecond` and variants (RFD at 50 to 250 ms) | Highest RFD in the first 50 to 250 ms of the effort | N/s | Partly |
| `innerLeftMinTimeToMaxForceSeconds` and variants | Time from effort start to peak force | s | Partly |
| `innerLeftImpulse` and variants | Area under the force-time curve for one sensor | N·s (unit not stated in the spec) | Yes |
| `innerLeftMaxImpulse50msNewtonSeconds` and variants (impulse at 50 to 250 ms) | Highest impulse in the first 50 to 250 ms of the effort | N·s | Partly |
| `innerLeftRepetitions` and variants | Number of reps detected on one sensor | Count | Partly |
| `startOffsetSeconds`, `endOffsetSeconds` | Start and end time of a rep | s | Not published |
| `leftMaxForcePerKg` and the other KB example fields | Left and right and torque fields in the KB `/metrics` example only | Not published | Not published |
| Torque (no ForceFrame field) | No ForceFrame torque metric is defined | Not published | Not published |
| Personal Best | Best ever left and right result for the test type | Same as the metric | Yes |
| Baseline | A saved reference result | Same as the metric | Partly |
| Moving Average | Average of the last 1 to 10 tests | Same as the metric | Yes |
| Norms | Percentile against VALD data of the same age group and sex | Percentile | Partly |
| `innerLeftForce` and variants (force trace) | Force on each sensor at one sample | N | Partly |
| `ticks` | Timestamp of each force sample | int64 (unit not published) | Not published |
| `forceGoal` | Target force for a training exercise | N in the example (unit not in the spec) | Partly |
| `trainingZone` | How the target force is set | Enum | Partly |
| `tolerance`, `toleranceUnit` | Width of the training zone around the target | % per the KB (the API example shows N) | Yes |
| `contractionTime` | How long each rep is held in the zone | Time span (hh:mm:ss) | Partly |
| `restTime`, `restTimeAfterSet` | Rest between reps and rest after the set | Time span (hh:mm:ss) | Partly |
| `repetitions` (training) | Prescribed reps for an exercise | Count | Partly |
| `timeInZoneLeft`, `timeInZoneRight` | How much of the effort stayed inside the training zone | Not published in the API (Hub shows %) | Not published |
| `stabilityLeft`, `stabilityRight` | Not published | Not published | Not published |
| `impulseLeft`, `impulseRight` (training) | Force accumulated over time during training | N s in Hub (unit not in the API) | Not published |
| Reps Completed, Exercise Type (Hub training export) | Reps performed in an exercise, and the exercise name | Count; text | Not published |

### DynaMo

DynaMo measures: handheld isometric force and IMU range of motion. Details are on [the DynaMo page](dynamo.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `maxForceNewtons` and variants | Highest force in one rep (peak force) | N | Partly |
| `impulseNewtonSeconds` and variants | Force accumulated over time during one rep | N·s | Not published |
| `rateOfForceDevelopmentNewtonsPerSecond` and variants | How fast force rises during one rep | N/s | Partly |
| `timeToPeakForceSeconds` and variants | Time from rep start to peak force | s | Partly |
| `baselineForceNewtons` and variants | Resting force on the device before the effort | N | Not published |
| `netPeakForceNewtons` and variants | Peak force above baseline | N | Partly |
| `netForceAt100msNewtons` and variants | Force above baseline at 100, 150, and 200 ms | N | Not published |
| `netImpulseAt100msNewtonSeconds` and variants | Force above baseline accumulated over the first 100, 150, and 200 ms | N·s | Not published |
| `timeTo80PercentPeakForceSeconds` and variants | Time from effort start to 80 percent of peak force | s | Partly |
| `rateOfForceDevelopment150msNewtonsPerSecond` and variants | Average rate of force rise over the first 150, 200, and 250 ms | N/s | Not published |
| `rangeOfMotionDegrees` and variants | Joint angle range covered in one range of motion rep | degrees | Partly |
| `startOffsetSeconds` and `durationSeconds` on `RepetitionDTO` | Rep start within the recording and rep length | s | Not published |
| `repCount` | Number of reps kept for one side and movement | count | Partly |
| `valuePercentage` on `AsymmetryDTO` | Percentage difference between left and right for one movement | % | Not published |
| `value` on `RatioDTO` | Ratio between two movements on one side | ratio, unitless | Not published |
| `durationSeconds` on `TestDTO` | Length of the whole test recording | s | Not published |
| `forceTrace[].forceNewtons` and `forceTrace[].timeSeconds` | Raw force signal of a strength test | N, s | Partly |
| `imuTrace[].orientation` and `imuTrace[].timeSeconds` | Device orientation over time in a range of motion test | unitless quaternion, s | Partly |
| `analysisInfo` | Analysis settings used for the test | text | Not published |
| Enum fields (`testCategory`, `bodyRegion`, `movement`, `position`, and others) | Test context values | text | Not published |

### SmartSpeed

SmartSpeed measures: timing gate splits, sprint profiles, and jump mat times. Details are on [the SmartSpeed page](smartspeed.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `splitTime` | Time of one segment between two gate breaks | s (Hub); API unit Not published | Partly |
| `cumulativeTime` | Running time from the start to a gate | s (Hub); API unit Not published | Partly |
| `gateIndex` and `splitIndex` | Which gate broke and which split it is | count | Not published |
| `goalSplitTime` and `goalCumulativeTime` | Target split and cumulative times | Not published | Not published |
| `totalOne` and variants | Totals across segments (meaning not given) | Not published | Not published |
| `heightM` and `weightKg` (`additionalTestResult`) | Athlete height and body mass on the test | m and kg by field name | Not published |
| `totalTimeSeconds` | Total time of the trial | s | Partly |
| `bestSplitSeconds` | Best split in the trial | s | Not published |
| `splitAverageSeconds` | Average split in the trial | s | Not published |
| `splitOne` to `splitFour` | First four split times | s (assumed from Hub); API unit Not published | Partly |
| `cumulativeOne` to `cumulativeFour` | Cumulative time at the first four gates | s (assumed from Hub); API unit Not published | Partly |
| `peakVelocityMetersPerSecond` | Highest velocity in the trial | m/s | Partly |
| `meanVelocityMetersPerSecond` | Average velocity over the trial | m/s | Partly |
| `distance` | Drill distance (total or split not stated) | Not published | Not published |
| `startType` | How timing started (option field) | enum | Not published |
| `reactionTime` | Time from start cue to first gate break | Not published | Yes |
| `reactiveDelayEnabled` and variants | Random delay before the go cue and its range (option fields) | boolean, s, s | Partly |
| `direction` (`additionalOptionsFields`) and `cutDirectionChoice` | Configured change of direction (option fields) | enum | Not published |
| `direction` (`additionalTestResult`) and `expectedDirection` | Direction taken and direction cued | string; integer | Not published |
| `colour` and `splitType` | Signal colour at the gate; split type not stated | string | Not published |
| `restDuration` | Rest time for a rep | Not published | Partly |
| `intervalType` | Fixed duration or fixed recovery interval | enum | Partly |
| `testStandardType` and variants | How a trial ends | enum, count, s | Partly |
| `lapCount` | Number of laps set for the trial | count | Partly |
| `maxVelocity` and `vMax` | FVP velocity values (meaning not given) | Not published | Not published |
| `maxForce` and `maxForceNormalised` | FVP force values (meaning not given) | Not published | Not published |
| `maxPower` and `maxPowerNormalised` | FVP power values (meaning not given) | Not published | Not published |
| `forceVelocityCurve` | FVP force-velocity value (meaning not given) | Not published | Not published |
| `drf` and `rfMax` | FVP force-ratio values (meaning not given) | Not published | Not published |
| `tau` | FVP time-constant value (meaning not given) | Not published | Not published |
| `contactTime` and `contactTimeSeconds` | Time on the mat between jumps | ms in Hub; s by name in summary | Yes |
| `flightTime` and `flightTimeSeconds` | Time in the air for a jump | ms in Hub; s by name in summary | Yes |
| `heightMeters` | Jump height | m | Partly |
| `rsi` | Reactive strength | Not published | Yes |
| `flightTimeOverContractionTime` | Flight time relative to contact time | ratio | Yes |
| `flightTimePlusContractionTime` | Ground time plus air time of one jump | Not published | Partly |
| `peakPowerOutput` | Peak power of the jump | Not published | Partly |
| `peakPowerOutputOverTotalMass` | Peak power relative to mass | Not published | Partly |
| `legStiffness` | Interaction of lower limb muscles and joints in a jump | Not published | Partly |
| `impulse` | Take-off impulse | N·s | Partly |
| `dropHeight` and `dropHeightEnabled` | Box height for a drop jump (option fields) | Not published; boolean | Partly |
| `weightKg` (`additionalOptionsFields`) | Mass setting for the test | kg by field name | Not published |
| `isValid` and `tag` | Coach's valid or invalid tag for the trial | boolean; enum | Partly |
| Split speed | Average speed between two gates | m/s or km/h | Yes |
| 10 m sprint momentum | Momentum over the first 10 m | kg·m/s | Yes |
| Curved sprint deceleration (CSD) deficit | Time lost stopping at the end of a curved sprint | % | Yes |
| Curved acceleration-deceleration ability, average deceleration | Average braking rate after a curved sprint | m/s² | Yes |

### HumanTrak

HumanTrak measures: markerless 3D joint angles, positions, and jumps. Details are on [the HumanTrak page](humantrak.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| What the device measures | Camera, tracked points, axes, filtering, sampling rate, center of mass, and scope | n/a | Not published |
| Export routes | VALD Hub, External HumanTrak API v2, valdr, and other routes | n/a | Not published |
| Row level | Row structure of the API, valdr tables, and Hub CSV | n/a | Not published |
| Left and right labels | Side labels and sign rules across fields | n/a | Not published |
| Test types | Test Library categories and tests | n/a | Not published |
| Conditions that change every HumanTrak number | Shared testing conditions | n/a | Not published |
| `summaryMeasurements[].aggregates.max` and variants | Largest, smallest, and mean value of a metric group per side | Unit in `summaryMeasurements[].unit` | Not published |
| `asymmetryMeasurement.aggregates.max` and variants | Left-right difference for a metric group | Unit in `asymmetryMeasurement.unit`, example `"Percent"` | Not published |
| `repetitionCounts[].count` | Reps recorded for a test, per side | reps | Partly |
| `values.isSided` and repetition values | Value of one metric group in one rep | Unit of the metric group | Partly |
| Metric group descriptors | Metric group code, names, classification, trend sentiment | n/a | Not published |
| Identifiers and context fields | Keys and context fields of `/v2/tests-by-modified-date` | n/a | Not published |
| `Ankle Lateral Shift` | Sideways distance of the ankle from the hip midpoint | Not published | Partly |
| `Ankle Plantarflexion` | Foot to shin angle, sagittal plane | degrees | Yes |
| `Body Tilt` | Forward lean of the whole body from vertical | degrees | Yes |
| `Center of Mass (COM)` | Estimated whole-body balance point | Not published | Partly |
| `Elbow Flexion` | Elbow bend angle | degrees | Yes |
| `Head Displacement` | Forward or back position of the head over the feet | Not published | Partly |
| `Hip Abduction` | Thigh angle out to the side, coronal plane | degrees | Yes |
| `Hip Flexion` | Thigh to lower trunk angle, sagittal plane | degrees | Yes |
| `Hip Internal Rotation` | Shin angle from vertical in seated hip rotation | degrees | Yes |
| `Knee Ankle Separation Ratio` | Knee width divided by ankle width | ratio, no unit | Yes |
| `Knee Deviation` | Total side-to-side knee movement | Not published | Partly |
| `Knee Displacement` | Forward travel of the knees over the feet | Not published | Partly |
| `Knee Flexion` | Knee bend angle | degrees | Yes |
| `Knee Translation` | Largest knee shift, forward-back or side to side | Not published | Partly |
| `Knee Valgus` | Knee inward or outward angle, coronal plane | degrees | Yes |
| `Neck Displacement` | Forward or back position of the neck over the feet | Not published | Partly |
| `Neck Flexion` | Head tilt forward from vertical, sagittal plane | degrees | Yes |
| `Neck Lateral Flexion` | Head tilt to the side from vertical, coronal plane | degrees | Yes |
| `Pelvic Displacement` | Forward or back position of the spine base over the feet | Not published | Partly |
| `Pelvic Lateral Tilt` | Hip drop angle from horizontal, coronal plane | degrees | Yes |
| `Shoulder Abduction` | Arm lift to the side, coronal plane | degrees | Yes |
| `Shoulder Flexion` | Arm lift forward and up, sagittal plane | degrees | Yes |
| `Shoulder Internal Rotation` | Forearm angle from horizontal with the arm out to the side | degrees | Yes |
| `Sternum Displacement` | Forward or back position of the mid-chest over the feet | Not published | Partly |
| `Thoracic Rotation` | Shoulder twist relative to the hips, transverse plane | degrees | Yes |
| `Trunk Flexion` | Forward trunk lean from vertical, sagittal plane | degrees | Yes |
| `Trunk Lateral Flexion` | Side trunk lean from vertical, coronal plane | degrees | Yes |
| `Jump Height` | How high the body rises in a vertical jump | cm or in, per display setting | Partly |
| `Countermovement Depth` | How far the body drops before a countermovement jump | Not published | Not published |
| `Jump Distance` | Forward travel of the body in a broad jump | cm or in, per display setting | Partly |
| `Takeoff Angle` | Launch direction of the body at takeoff in a broad jump | degrees | Partly |
| `Knee Over Toe Distance` | Knee travel past the toes in Weight Bearing Dorsiflexion | Not published | Not published |
| `Spinal Rotation` | Spine rotation relative to the pelvis in Trunk Rotation tests | Not published | Not published |
| `Dynamic Knee Valgus` | Knee front-plane angle at the bottom of a single leg squat | degrees | Not published |
| `Hip Flexion at Peak Knee Flexion` | Hip flexion at the moment of peak knee flexion in a squat | degrees | Partly |
| `Peak Knee Flexion` | Most knee bend in a squat rep | degrees | Partly |
| `Hip Adduction at Peak Knee Flexion` | Thigh movement toward the midline at the bottom of a squat | degrees | Not published |
| `Ankle Dorsiflexion at Peak Knee Flexion` | Ankle bend at the bottom of a squat | degrees | Not published |
| `Pelvis Anterior Tilt at Peak Knee Flexion` | Forward pelvis tilt at the bottom of a squat | Not published | Not published |
| `Spine Tilt at Peak Flexion` | Trunk lean at the top of a shoulder flexion rep | Not published | Not published |
| `Shoulder Flexion Range of Motion` | Range of shoulder motion in the flexion test | degrees | Not published |
| `Neck Rotation` | How far the head turns left or right | Not published | Not published |
| `Center of Mass 95% Ellipse Area` | Area the CoM sways within during a balance stand | Not published | Not published |
| `Anteroposterior Center of Mass Excursion` | Forward-back CoM movement during a balance stand | Not published | Not published |
| `Absolute Motion of the Center of Mass` | Total CoM movement during Standing Posture | Not published | Not published |
| `Time to Stability` | Time to settle after a single leg landing | Not published | Not published |
| Sit to Stand outputs | Rep count in the three Sit to Stand tests | reps | Partly |
| Single Leg Heel Raise - Endurance outputs | Single leg heel raises to fatigue or technique failure | reps | Partly |
| Anthropometry outputs: standing height, wingspan, segment lengths | Body dimensions from two still captures | Not published | Not published |
| Custom test metrics | One or two user-named values per custom test | degrees, centimeters, or None | Partly |

### GymAware

GymAware measures: barbell or body displacement, velocity, power, and force per rep. Details are on [the GymAware page](gymaware.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| Identifiers and context fields: `/summaries` | Set identifier, time, athlete, exercise, and activity fields | Not applicable | Partly |
| Identifiers and context fields: `/reps` | Same context fields, plus the `reps` list and `REPNUM` | Not applicable | Partly |
| Identifiers and context fields: `/bests`, `/analysis`, `/exercises`, and activities | Fields returned by the other endpoints | Not applicable | Partly |
| `repCount` | Reps detected and kept in the set | count | Partly |
| `meanVelocity` | Average concentric bar velocity of the best rep | m/s | Yes |
| `peakVelocity` | Highest instantaneous concentric velocity in the set | m/s | Partly |
| `meanPower` | Average concentric power of the best rep | W | Yes |
| `peakPower` | Highest instantaneous concentric power in the best rep | W | Partly |
| `meanWattsPerKg`, `peakWattsPerKg` | Mean or peak power of the best rep relative to body mass | W/kg | Yes |
| `height` | Highest point above the zero point, for the highest rep | Not published in the API | Partly |
| `dip` | Lowest point below the start, for the deepest rep | Not published in the API | Partly |
| `velocityZone` | Velocity zone category of the set | category | Not published |
| `targets` | Target the athlete aimed at during the set | unit of the target metric | Partly |
| `barWeight` | External load lifted | kg | Partly |
| `athleteWeight` | Athlete body mass stored with the set | kg | Partly |
| `height`, `dip`, `meanVelocity`, and variants in `/bests` | Athlete's best values per exercise and bar weight | As in `/summaries` | Partly |
| Conc Mean Velocity | Average velocity over the concentric phase of one rep | m/s | Yes |
| Conc Peak Velocity (Max Velocity) | Highest instantaneous concentric velocity in one rep | m/s | Partly |
| Conc Mean Power | Average power over the concentric phase of one rep | W | Yes |
| Conc Peak Power | Highest instantaneous concentric power in one rep | W | Partly |
| Mean Watts/kg and Peak Watts/kg | Concentric mean or peak power relative to body mass | W/kg or W/lb | Yes |
| Conc Mean Force | Average force over the concentric phase | N | Yes |
| Conc Peak Force | Highest instantaneous concentric force | N | Partly |
| Rate of Force Development, RFD | Fastest rise in force during the concentric phase | kN/s | Yes |
| Time to Peak Velocity, Time to Peak Force, Time to Peak Power | Time from concentric start to each peak | s | Partly |
| Conc Rep Duration | Time of the concentric phase | s | Yes |
| Ecc Rep Duration | Time of the eccentric phase | s | Yes |
| Rep Duration | Time for one full rep | s | Yes |
| Rep Rate | Predicted reps per minute | reps/min | Partly |
| Conc Work | Mechanical work to raise the load in a rep | J | Yes |
| Height | Highest point above the zero point in one rep | m or in | Partly |
| Dip | Lowest point below the start in one rep | m or in | Partly |
| Lift Distance | Raw tether extension from bottom to top of a rep | m or in | Partly |
| Vertical Distance | Angle-corrected vertical displacement of a rep | m or in | Partly |
| Total Travel Path | Total distance travelled in a rep | m or in | Partly |
| Horizontal | Total horizontal displacement over a rep | m | Partly |
| Max Back, Max Forward, and height variants | Furthest backward and forward bar positions, and heights there | m or in | Partly |
| Nordic Displacement | Movement in a Nordic hamstring curl | m or in | Partly |
| Ecc Mean Velocity | Average velocity over the eccentric phase | m/s | Yes |
| Ecc Peak Velocity | Highest instantaneous eccentric velocity | m/s | Partly |
| Eccentric Minimum Velocity | Listed as a Cloud metric | Not published | Not published |
| Ecc Peak Power | Highest instantaneous eccentric power | W | Partly |
| Ecc Peak Force | Highest instantaneous eccentric force | N | Partly |
| Reactive Strength Index, RSI | Reactive jump capacity in a drop jump | m/s | Yes |
| Contact Time | Ground contact time in a drop or rebound jump | s | Partly |
| Flight Time | Time airborne in a jump | s | Partly |
| Peak acceleration, eccentric mean power, and eccentric mean force | Listed on the RS product page | m/s², W, N | Not published |
| Velocity loss, velocity drop-off, or fatigue target | How much rep velocity falls across a set | % | Partly |

## Conflicts in the vendor's own sources

The vendor's own pages disagree in these places. Each conflict also appears next to the metric or setting it affects:

### ForceFrame

- Training tolerance unit: the iOS training guide and Hub say tolerance is a percent ([Hub](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame), [iOS guide](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). The API guide example shows `tolerance` 10 with `toleranceUnit` "N" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- `/tests/{testId}/metrics` field names: the API guide example uses `left` and `right` fields plus four torque per kg fields, but the OpenAPI spec lists only `innerLeft`, `innerRight`, `outerLeft`, and `outerRight` fields and no torque fields. The ForceFrame example is identical to the NordBord API guide example ([ForceFrame guide](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API), [NordBord guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- RFD availability: a VALD article published 2025-07-30 and updated 2025-12-01 still lists RFD as "DynaMo Only" ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). The iOS release notes and KB list RFD for ForceFrame ([iOS notes](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes), [KB](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- Default sampling rate: the three spec sheets list 50 Hz as the default, up to 400 Hz ([Max V7](https://support.vald.com/hc/en-au/article_attachments/62749147143449), [Fold](https://support.vald.com/hc/en-au/article_attachments/25314373779993), [Max V6](https://support.vald.com/hc/en-au/article_attachments/25314362844569)). The iOS v3.0.0 release note (2025-09-29) says the sampling frequency was raised to 400 Hz and does not say whether 400 Hz is the new default ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- API guide titles versus URLs: KB Scenario 7 is titled "Retrieve a single exercise session" but calls `/training/programs/current` with `Id`. KB Scenario 9 is titled "Retrieve a collection of training sessions" but shows the URL `/training/sessions/exercises`, while the spec has a separate `/training/sessions` path ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API), [spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).

### DynaMo

- DynaMo Max size and weight: 400 g ([source](https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models)), 850 g ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)), and 1.5 kg ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). This does not affect the metrics.
- External DynaMo API guide versus OpenAPI spec: the KB names the path segment `{tenantId}`, while the spec names it `{teamId}`. The KB marks `modifiedFromUtc`, `testFromUtc`, and `testToUtc` as required, while the spec marks only the path parameter as required. The KB writes `imutrace`, while the spec field is `imuTrace` ([KB guide](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [spec](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
- `attachments` type: the KB metadata example shows `"attachments": 0`, a number, while the spec defines a string enum ([KB guide](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [spec](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
- Attachment fields within the KB examples: `leftAttachment` and `rightAttachment` read `None` while `attachments` reads `LeftPalmPadRightCurvedPad` ([KB guide](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- Max IMTP attachment: the Max IMTP example reads `LeftPalmPadRightCurvedPad`, but the IMTP uses a tension strap and the Max kit lists no palm pad ([KB guide](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [Max hip strength protocol](https://support.vald.com/hc/en-au/articles/36405455263513-DynaMo-Max-Test-Protocols-Hip-Strength), [Max system hardware](https://support.vald.com/hc/en-au/articles/38449708425369-DynaMo-Max-system-hardware)).
- Force trace resolution: the KB example shows resting values from −3 N to +5 N in 0.5 N steps, though spec sheets list 1 N resolution ([KB guide](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [Max spec sheet](https://support.vald.com/hc/en-au/article_attachments/62792898698009)).

### SmartSpeed

- The KB API guide lists query parameters in camelCase (`athleteId`, `page`) and marks `page` required. The spec uses PascalCase (`AthleteId`, `Page`) ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API), [source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- The KB says "Contact time" for SmartJump ratios. The spec says `flightTimeOverContractionTime` and `flightTimePlusContractionTime` ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- The KB lists SmartJump times in ms. The summary field names say seconds (`flightTimeSeconds`, `contactTimeSeconds`).
- Unit-to-reflector distance: 1 m to 2 m (Plus KB), about 2 m (Dash KB, Plus Quick Start Guide), 1 m to 4 m (Pro and Dash Quick Start Guides), 4 m maximum (Plus spec), 7 m maximum (Dash and Pro specs) ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates), [source](https://support.vald.com/hc/article_attachments/31800152349721), [source](https://support.vald.com/hc/en-au/article_attachments/62792691604889)).
- Dash gate-to-gate range: 60 m (Model Comparison), about 50 m (buyer's guide), 100 m (Dash spec sheet) ([source](https://support.vald.com/hc/en-au/articles/4996484198297-SmartSpeed-Model-Comparison), [source](https://valdperformance.com/news/buyers-guide-to-timing-gates), [source](https://support.vald.com/hc/en-au/article_attachments/62792687636121)).
- valdr renames nested fields to their last name part. `weightKg` in valdr output is `additionalOptionsFields.weightKg`, not the detail `additionalTestResult.weightKg` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)).

### HumanTrak

- Query parameter casing for `GET /v2/test/{testId}/repetitions`: the VALD knowledge base writes `tenantId` and `profileId` in lower camel case ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The OpenAPI spec lists `TenantId` and `ProfileId` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). `valdr` sends `TenantId` and `ProfileId` ([source](https://github.com/cran/valdr/blob/master/R/humantrak_reps_by_id.R)).
- Repetition values object: the spec defines `values` with `isSided` only and `"additionalProperties": false` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). The knowledge base example returns `leftValue`, `rightValue`, and `unsidedValue` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). `valdr` reads those three fields ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). The knowledge base example also lacks a comma after `"leftValue": 11.11`, so it is not valid JSON as printed.
- Catalog fields: `valdr` reads `metricGroups[].asymmetrySupported` and a `side` field on each repetition metric type, and the spec lists neither. The spec lists `movementSide` and `metricSide` instead ([source](https://github.com/cran/valdr/blob/master/R/utils.R), [source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)).
- Camera height: the optimal testing conditions article gives about 1 m ([source](https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions)). The tripod setup article gives about 90 cm ([source](https://support.vald.com/hc/en-au/articles/5001237165593-Assemble-your-HumanTrak-system)).
- Ankle angle reference: the `Ankle Plantarflexion` article sets neutral at 90° with dorsiflexion positive ([source](https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion)). The API example values for the ankle dorsiflexion group, 11.11 and 13.89, suggest a 0° neutral ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The zero point is Not published.
- Neck angle reference: the knowledge base articles for `Neck Flexion` and `Neck Lateral Flexion` measure against vertical ([source](https://support.vald.com/hc/en-au/articles/5001735307545-HumanTrak-Metrics-Neck-Flexion), [source](https://support.vald.com/hc/en-au/articles/5001742621337-HumanTrak-Metrics-Neck-Lateral-Flexion)). VALD's normative report describes cervical flexion and lateral flexion as head inclination relative to the trunk line ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)).

### GymAware

- Pagination window: the guide says "max 1 month per request" and also says "start/end need to be within 60 days of each other" for `/summaries` and `/reps`. Use windows of 1 month or less to satisfy both ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
- API access tier: the API guide says the API is included with the Premium Cloud license ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). The subscription page also lists "External API" as an add-on ([source](https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options)).
- Guide versus example app: the example app reads `reference`, `referenceID`, and `deleted` from `/athletes` while the guide lists `athleteReference`. It reads `notes` from `/summaries`, which the guide does not list. It reads `userID` from `/staff` while the guide lists only `staffReference` ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
- Velocity zones: GymAware's education page gives mean-velocity zones of below 0.5, 0.5 to 0.75, 0.75 to 1.0, 1.0 to 1.3, and above 1.3 m/s ([source](https://gymaware.com/velocity-based-training-zones-framework/)). VALD's VBT 101 sheet shows the same ranges in its "VBT in Practice" panel, but its force-velocity chart on the same page labels some zones with different ranges ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/VBT%20101.pdf)). VALD's zones article gives the same velocity ranges but different %1RM bands ([source](https://valdperformance.com/news/understanding-velocity-zones-applying-velocity-based-training-to-program-design)).
- Velocity loss reference rep: GymAware's worked examples use the first rep ([source](https://gymaware.com/velocity-loss-in-strength-training/), [source](https://gymaware.com/train-to-velocity-failure-using-velocity-stops/), [source](https://gymaware.com/gymaware-flex-app-data-and-implementation/)). A FLEX app screenshot caption says the app compares with the previous rep ([source](https://gymaware.com/train-to-velocity-failure-using-velocity-stops/)). The GymAware app % zone uses the best rep of the set when no target is set ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained)). VALD says velocity loss is typically calculated from the fastest repetition in the set ([source](https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training)).
- RS time-stamp resolution: 8.6 microseconds in the fact sheet ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001133391-GymAware-Fact-sheets)) and 35 microseconds in the sampling PDF ([source](https://kinetic.com.au/pdf/sample.pdf)).

## Not published

The sources checked do not state these items. The lists are by product:

### ForceFrame

- VALD Hub CSV column names for the test, rep, force trace, and training exports.
- Mapping of `FlatLeft` and `FlatRight` to physical paddles; no flat or upper sensor columns in the summary, `/metrics`, or trace schemas.
- API force trace sign convention, and which movement loads the inner versus the outer paddles in each test.
- Protocols for the `Hamstring` and `Dyno` joint values.
- Peak-picking rule for `innerLeftMaxForce` and the other `MaxForce` fields beyond the point where ForceFrame starts looking for a peak.
- Calculation of `innerLeftAvgForce`, `innerRightAvgForce`, `outerLeftAvgForce`, `outerRightAvgForce`.
- Imbalance (%) formula and sign convention.
- Strength ratio: which side or sides it uses, and how "AB:AD" labels map to inner:outer.
- Calculation of the `AvgForcePerKg` fields, and when per kg fields return null.
- RFD window length and slope method for `MaxRFDNewtonsPerSecond`, `AvgRFDNewtonsPerSecond`, and `maxRFDNewtonsPerSecond`; how Max and Avg combine reps.
- Effort start detection for RFD at 50 to 250 ms, impulse at 50 to 250 ms, and time to max force; slope method for RFD at fixed times; whether pretension force is subtracted from fixed-time impulse.
- How `Min` and `Avg` combine reps for `MinTimeToMaxForceSeconds` and `AvgTimeToMaxForceSeconds`.
- Whether the test-level `Impulse` fields sum or average the reps; the default impulse threshold in iOS.
- Default rep threshold per test type (150N is an example only).
- Reference point and boundary rule for `startOffsetSeconds` and `endOffsetSeconds`.
- ForceFrame meaning and unit of the KB example fields `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg`, and the other `left` and `right` `/metrics` example fields.
- Any ForceFrame torque metric, lever arm input, or torque unit.
- Personal Best position matching; Baseline variants; Norms curve-fitting algorithm.
- Filtering of the stored force trace; unit of `ticks` (example values fit .NET ticks).
- Whether `forceGoal` stores newtons or a percentage when `trainingZone` is `Max`; whether in-session zone edits save to `forceGoal`.
- Definition of the `Average` training zone.
- Unit and calculation of `timeInZoneLeft` and `timeInZoneRight` in the API; aggregation from reps to exercises and sessions.
- Definition, unit, and inputs of `stabilityLeft` and `stabilityRight`; whether they equal Hub "Variance (%)".
- Calculation of training `impulseLeft` and `impulseRight`, including threshold and aggregation.
- Calculation of Hub training "Reps Completed" and "Exercise Type".

### DynaMo

- VALD Hub DynaMo CSV export steps and column names. DynaMo Leaderboard CSV columns.
- `maxForceNewtons`: filtering and smoothing.
- `avgForceNewtons`: exact averaging method.
- `impulseNewtonSeconds` and its max and avg variants: window start, end, and baseline handling.
- `rateOfForceDevelopmentNewtonsPerSecond` and its max and avg variants: window and method.
- `timeToPeakForceSeconds` and its avg and min variants: onset detection rule.
- `baselineForceNewtons` and its avg and max variants: baseline window and method.
- `netPeakForceNewtons`: formula (example arithmetic fits peak − baseline).
- `netForceAt100msNewtons`, `netForceAt150msNewtons`, `netForceAt200msNewtons` and their avg and max variants: onset rule.
- `netImpulseAt100msNewtonSeconds`, `netImpulseAt150msNewtonSeconds`, `netImpulseAt200msNewtonSeconds` and their avg and max variants: formula and onset rule.
- `timeTo80PercentPeakForceSeconds` and its avg and min variants: onset rule and crossing rule.
- `rateOfForceDevelopment150msNewtonsPerSecond`, `rateOfForceDevelopment200msNewtonsPerSecond`, `rateOfForceDevelopment250msNewtonsPerSecond` and their avg and max variants: reference force and onset rule.
- Which strength fields are DynaMo Max only.
- `rangeOfMotionDegrees`: angle calculation from the IMU, reference axis, and sign convention. Meaning of `maxRangeOfMotionDegrees` with negative values. Whether two-side range of motion tests return asymmetry.
- `startOffsetSeconds` and rep `durationSeconds`: start and end detection. Minimum rep duration value.
- Recommended rep count and hold duration for DynaMo tests.
- `valuePercentage`: formula, source metric, sign rule, and rounding. What the 2022-07-01 asymmetry update changed.
- `RatioDTO.value`: formula, source metric, scale, and which tests produce ratios.
- Test `durationSeconds` definition.
- Trace filtering. Quaternion frame, axis order, and handedness. Relationship between trace and test `startTimeUTC`.
- `analysisInfo`, `hardwareInfo`, and `softwareInfo` formats. `analysisInfo` value in Manual range of motion mode.
- Meaning of Left and Right in `attachments`, `leftAttachment`, and `rightAttachment`.
- Mapping of paired test-level `movement` values to rep `movement` values. Use of `customPosition`.
- Whether summaries and asymmetry recalculate after rep deletion or laterality edits in Hub.
- Torque, lever arm, and per-kg values: no DynaMo export fields.

### SmartSpeed

- Calculation for `splitTime`, `cumulativeTime`, `totalTimeSeconds`, `bestSplitSeconds`, `splitAverageSeconds`, `splitOne` to `splitFour`, `cumulativeOne` to `cumulativeFour`, `peakVelocityMetersPerSecond`, `meanVelocityMetersPerSecond` (restatements given, VALD formula Not published).
- API units for `splitTime`, `cumulativeTime`, `reactionTime`, `restDuration`, `distance`, `goalSplitTime`, `goalCumulativeTime`, `contactTime`, `flightTime`, `dropHeight`, `rsi`, `peakPowerOutput`, `peakPowerOutputOverTotalMass`, `legStiffness`, `flightTimePlusContractionTime`.
- `distance` meaning (total or split).
- `gateIndex`, `splitIndex`, `trialIndex`, `repIndex` base and mapping to gates.
- `totalOne`, `totalOneToTwo`, `totalOneToThree`, `totalOneToFour`, `totalThreeToFour`: meaning and calculation.
- `heightM`, `weightKg` (both locations): source and use.
- `goalSplitTime`, `goalCumulativeTime`, `colour`, `splitType`, `expectedDirection`, detail `direction`: meaning and encoding.
- `restDuration` calculation.
- All FVP fields: `maxVelocity`, `vMax`, `maxForce`, `maxForceNormalised`, `maxPower`, `maxPowerNormalised`, `forceVelocityCurve`, `drf`, `rfMax`, `tau`.
- Jump height formula for `heightMeters`; `legStiffness` and `peakPowerOutput` calculations; how `impulse` force is estimated; summary jump aggregation method.
- Whether `splitTime` and `cumulativeTime` include reaction time for `TrafficLight` and `ReactiveStart`.
- Flying start run-in distance and any start offset.
- Numeric gate height.
- Which `StartType` value stores a mat start; mapping of app test modes to `TestStandardType`.
- Mapping of `TestTypeName` values to app drill names (name matches only); `TestTypeName` for Beep Test and VAM Eval Test.
- Hub CSV column list and row level; whether ECP was on for a test.

### HumanTrak

- Filter type and cutoff.
- Sampling rate for the Orbbec Femto Bolt camera.
- The full list of the 23 tracked points.
- Hub CSV columns, row level, and side labels.
- The `/v2/test-type/metrics` catalog contents, all metric group codes except three, and all test type codes except `TT_SQUAT-DL`.
- Values and meanings of `classification`, `trendSentiment`, `laterality`, `movementSide` and `metricSide` in the catalog, and `calculationType`.
- Aggregate method for `max`, `min`, and `avg`.
- Asymmetry formula and sign rule. The KB example arithmetic is an observation only.
- Whether the API recomputes aggregates after Hub rep deletion.
- Whether the API returns metric or display units.
- Units of all displacement metrics: `Ankle Lateral Shift`, `Head Displacement`, `Knee Deviation`, `Knee Displacement`, `Knee Translation`, `Neck Displacement`, `Pelvic Displacement`, `Sternum Displacement`, `Center of Mass (COM)`.
- Sign conventions for `Head Displacement`, `Neck Displacement`, `Pelvic Displacement`, `Sternum Displacement`, `Knee Displacement`, and the extension, adduction, and external rotation directions of the shoulder, trunk, and hip angles.
- `Knee Deviation` method (path or range). `Knee Translation` reference position.
- CoM segment model and mass fractions.
- Which neck reference (vertical or trunk) the exported neck angles use.
- Angle definitions for Shoulder Internal and External Rotation - Neutral, Shoulder Arc of Motion, and `Neck Rotation`.
- `Countermovement Depth`, `Knee Over Toe Distance`, `Spinal Rotation`, `Pelvis Anterior Tilt at Peak Knee Flexion`, `Spine Tilt at Peak Flexion`, `Shoulder Flexion Range of Motion`, `Center of Mass 95% Ellipse Area`, `Anteroposterior Center of Mass Excursion`, `Absolute Motion of the Center of Mass`, and `Time to Stability`: calculations and units.
- `Dynamic Knee Valgus` formula and export sign. `Hip Adduction at Peak Knee Flexion` formula and sign. `Ankle Dorsiflexion at Peak Knee Flexion` zero point.
- Export field names for every test-specific metric.
- Metrics for Lunge, Lateral Hop, Medial Hop, Box Lift - Bench, and Box Lift - Overhead.
- Sit to stand time field. Heel raise height threshold and field. Anthropometry field names and segment list. How custom test metrics appear in the API.

### GymAware

- Exact `/analysis` label strings, and their units in the API.
- Units of `height` and `dip` in the API. Whether API values follow the lb or inch display settings.
- How `/summaries` and `/bests` choose the "best rep" and personal best. Whether all best-rep fields come from one rep.
- `velocityZone` values and thresholds.
- `targets.mode` strings.
- Whether `barWeight` includes body mass for +BM exercises. Which exercises are +BM by default.
- Whether API rows mark the recording device (RS or FLEX).
- CSV export columns and row level.
- A GymAware asymmetry formula, and any side field.
- Pagination parameters.
- Rep Rate exact formula.
- Total Travel Path, Horizontal, and Nordic Displacement formulas.
- Sign conventions for eccentric metrics, Max Back, and Max Forward.
- Eccentric Minimum Velocity definition.
- Eccentric phase start and end rules.
- Contact Time and Flight Time detection.
- Peak acceleration, eccentric mean power, and eccentric mean force definitions.
- A formal velocity-loss formula, and the reference rep the app uses for fatigue targets.
- The `notes`, `referenceID`, and `userID` fields used by the example app.
- The URL of the activities endpoint in the guide (the example app uses `activities`).

## Sources

These are the public pages and documents behind the metric blocks, grouped by product page. All were accessed on 2026-10-02:

### ForceFrame

- https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure
- https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf
- https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame
- https://valdhealth.com/news/the-history-and-future-of-forceframe
- https://support.vald.com/hc/en-au/article_attachments/62749147143449
- https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work
- https://support.vald.com/hc/en-au/article_attachments/25314373779993
- https://support.vald.com/hc/en-au/article_attachments/25314362844569
- https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes
- https://valdhealth.com/news/understanding-rate-of-force-development
- https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/4998152248345-Export-ForceFrame-Results
- https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes
- https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/4799421027993-View-Training-Data-in-VALD-Hub
- https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json
- https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API
- https://github.com/cran/valdr/blob/master/R/session.R
- https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package
- https://github.com/cran/valdr/blob/master/R/forceframe_tests.R
- https://github.com/cran/valdr/blob/master/R/utils.R
- https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI
- https://support.vald.com/hc/en-au/articles/56075934514585-Using-VALD-AI-for-data-analysis
- https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App
- https://support.vald.com/hc/en-au/articles/4998486609817-ForceFrame-Test-Protocol-Hip-Abduction-Adduction
- https://support.vald.com/hc/en-au/articles/4998398932377-ForceFrame-Test-Protocol-Hip-Flexion
- https://support.vald.com/hc/en-au/articles/4998462834457-ForceFrame-Test-Protocol-Hip-Extension
- https://support.vald.com/hc/en-au/articles/4998398037657-ForceFrame-Test-Protocol-Hip-Internal-External-Rotation
- https://support.vald.com/hc/en-au/articles/4998376807705-ForceFrame-Test-Protocol-Knee-Flexion
- https://support.vald.com/hc/en-au/articles/12962592988953-ForceFrame-Test-Protocol-Knee-Extension
- https://support.vald.com/hc/en-au/articles/4998507355417-ForceFrame-Test-Protocol-Ankle-Dorsiflexion
- https://support.vald.com/hc/en-au/articles/12960659718809-ForceFrame-Test-Protocol-Ankle-Plantar-Flexion
- https://support.vald.com/hc/en-au/articles/4998488417433-ForceFrame-Test-Protocol-Ankle-Inversion-Eversion
- https://support.vald.com/hc/en-au/articles/4998364117273-ForceFrame-Test-Protocol-Shoulder-Internal-External-Rotation
- https://support.vald.com/hc/en-au/articles/4998379282457-ForceFrame-Test-Protocol-Shoulder-Abduction-Adduction
- https://support.vald.com/hc/en-au/articles/4998329413529-ForceFrame-Test-Protocol-Shoulder-Flexion
- https://support.vald.com/hc/en-au/articles/4998322753689-ForceFrame-Test-Protocol-Shoulder-Extension
- https://support.vald.com/hc/en-au/articles/4998479418137-ForceFrame-Test-Protocol-Elbow-Flexion
- https://support.vald.com/hc/en-au/articles/4998519702681-ForceFrame-Test-Protocol-Elbow-Extension
- https://support.vald.com/hc/en-au/articles/4998344479129-ForceFrame-Test-Protocol-Neck
- https://support.vald.com/hc/en-au/articles/4998193046425-Create-Custom-ForceFrame-Test-Types
- https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS
- https://support.vald.com/hc/en-au/articles/26094908032537-Delete-reps-in-ForceFrame-iOS
- https://support.vald.com/hc/en-au/articles/4998047089305-Run-a-ForceFrame-Test
- https://support.vald.com/hc/en-au/articles/29788227745305-ForceFrame-Windows-Release-Notes
- https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance
- https://valdhealth.com/calculators
- https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making
- https://valdhealth.com/news/benchmarking-for-rehabilitation-providers
- https://valdperformance.com/news/my-dashboard-jo-clubb
- https://valdperformance.com/news/neck-coupling-strength-in-mma-testing-what-matters
- https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics
- https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource
- https://support.vald.com/hc/en-au/articles/4998153143577-Adjusting-detection-thresholds-in-ForceFrame-Windows
- https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API
- https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub
- https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated
- https://support.vald.com/hc/en-au/articles/21651363065753-Normative-data-FAQs
- https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems
- https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame
- https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS
- https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS
- https://valdhealth.com/news/post-surgical-shoulder-rehab-for-a-professional-baseball-pitcher

### DynaMo

- https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models
- https://support.vald.com/hc/en-au/article_attachments/62792898708505
- https://support.vald.com/hc/en-au/article_attachments/62792928707993
- https://support.vald.com/hc/en-au/articles/5457903678745-Connect-your-DynaMo-attachments
- https://support.vald.com/hc/en-au/article_attachments/62792898698009
- https://support.vald.com/hc/en-au/articles/38449708425369-DynaMo-Max-system-hardware
- https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers
- https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes
- https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/17676771546649-Create-a-Leaderboard-in-VALD-Hub
- https://support.vald.com/hc/en-au/articles/8817109682457-Introduction-to-Leaderboard
- https://support.vald.com/hc/en-au/articles/4799421420697-View-test-data-in-VALD-Hub
- https://support.vald.com/hc/en-au/articles/25954041656089-Print-DynaMo-test-results
- https://support.vald.com/hc/en-au/articles/20656475656345-Create-a-Group-Dashboard-monitoring-chart
- https://prd-aue-api-extdynamo.valdperformance.com/
- https://prd-use-api-extdynamo.valdperformance.com/
- https://prd-euw-api-extdynamo.valdperformance.com/
- https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API
- https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json
- https://github.com/cran/valdr/blob/master/R/dynamo_tests.R
- https://support.vald.com/hc/en-au/articles/24517370929049-API-Updates-February-2024-Breaking-Changes
- https://github.com/cran/valdr/blob/master/R/session.R
- https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package
- https://github.com/cran/valdr/blob/master/R/dynamo_tests_by_id.R
- https://github.com/cran/valdr/blob/master/R/utils.R
- https://support.vald.com/hc/en-au/articles/56075934514585-Using-VALD-AI-for-data-analysis
- https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI
- https://support.vald.com/hc/en-au/articles/6827647624729-Record-a-strength-test-with-DynaMo
- https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub
- https://support.vald.com/hc/en-au/articles/15257079218073-DynaMo-Lite-Test-Protocols-Neck-ROM
- https://support.vald.com/hc/en-au/articles/5453099730585-Test-types-available-with-DynaMo
- https://support.vald.com/hc/en-au/articles/36405455263513-DynaMo-Max-Test-Protocols-Hip-Strength
- https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes
- https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings
- https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs
- https://support.vald.com/hc/en-au/articles/26373474010009-Delete-reps-in-DynaMo
- https://support.vald.com/hc/en-au/articles/27432433786009-Customize-Unit-of-Measurement-in-VALD-Hub
- https://valdhealth.com/calculators
- https://valdperformance.com/news/isometrics-static-contractions-dynamic-applications
- https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance
- https://valdhealth.com/news/handheld-dynamometers-101-century-old-technology-for-the-modern-practitioner
- https://support.vald.com/hc/en-au/articles/15342037629721-DynaMo-Lite-Test-Protocols-Hip-Strength
- https://valdhealth.com/news/understanding-rate-of-force-development
- https://support.vald.com/hc/en-au/articles/19112858914329-DynaMo-Plus-Test-Protocols-Knee-Strength
- https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource
- https://valdhealth.com/news/post-surgical-shoulder-rehab-for-a-professional-baseball-pitcher
- https://support.vald.com/hc/en-au/articles/6751104055833-Record-a-range-of-motion-ROM-test-with-DynaMo
- https://support.vald.com/hc/en-au/articles/15416619683609-DynaMo-Lite-Test-Protocols-Knee-ROM
- https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making
- https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated

### SmartSpeed

- https://valdperformance.com/news/timing-gates-101
- https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics
- https://support.vald.com/hc/en-au/articles/4996482906905-SmartSpeed-Optional-Accessories
- https://support.vald.com/hc/article_attachments/31800152349721
- https://support.vald.com/hc/en-au/articles/4996484198297-SmartSpeed-Model-Comparison
- https://support.vald.com/hc/en-au/articles/9848256433049-SmartSpeed-Starter-s-Guide
- https://support.vald.com/hc/en-au/articles/44078746580633-Upgrade-to-the-SmartSpeed-Plus-app
- https://support.vald.com/hc/en-au/articles/28173187417369-Enable-trial-validity-in-the-SmartSpeed-Plus-app
- https://support.vald.com/hc/en-au/articles/42843499827353-Edit-a-SmartSpeed-test
- https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes
- https://support.vald.com/hc/en-au/articles/27432433786009-Customize-Unit-of-Measurement-in-VALD-Hub
- https://prd-aue-api-extsmartspeed.valdperformance.com/
- https://prd-use-api-extsmartspeed.valdperformance.com/
- https://prd-euw-api-extsmartspeed.valdperformance.com/
- https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API
- https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json
- https://github.com/cran/valdr/blob/master/R/smartspeed_tests.R
- https://github.com/cran/valdr/blob/master/R/session.R
- https://github.com/cran/valdr/blob/master/R/utils.R
- https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes
- https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus
- https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List
- https://support.vald.com/hc/en-au/articles/4997545365913-SmartSpeed-Drill-One-Way-Timing
- https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint
- https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills
- https://support.vald.com/hc/en-au/articles/4997398652825-SmartSpeed-Drill-Pro-Agility
- https://support.vald.com/hc/en-au/articles/4997452301849-SmartSpeed-Drill-Reactive-Pro-Agility
- https://support.vald.com/hc/en-au/articles/4997399394201-SmartSpeed-Drill-Free-Timing
- https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine
- https://support.vald.com/hc/en-au/articles/4997511951641-SmartSpeed-Drill-Grid
- https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol
- https://support.vald.com/hc/en-au/articles/4997515544217-SmartSpeed-Drill-Pacing
- https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing
- https://support.vald.com/hc/en-au/articles/4997420680089-SmartSpeed-Drill-Vertical-Jump
- https://valdhealth.com/news/managing-deceleration-in-return-to-sport-scenarios
- https://support.vald.com/hc/en-au/articles/4996430805017-Error-Correction-Processing-ECP
- https://support.vald.com/hc/en-au/articles/4997268643609-SmartSpeed-FAQs
- https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates
- https://support.vald.com/hc/en-au/article_attachments/62792691604889
- https://support.vald.com/hc/en-au/articles/16732705756313-SmartSpeed-Plus-Align-your-timing-gates
- https://support.vald.com/hc/en-au/articles/4996910107289-SmartSpeed-Dash-Set-up-your-timing-gates
- https://support.vald.com/hc/en-au/article_attachments/29460216899737/VALD%20SmartSpeed%20Dash%20Quick%20Start%20Guide%20V1.4%20.pdf
- https://support.vald.com/hc/en-au/article_attachments/62792687636121
- https://support.vald.com/hc/en-au/articles/4996881817881-SmartSpeed-Pro-Setup-Timing-Gates
- https://support.vald.com/hc/article_attachments/29751035498265
- https://support.vald.com/hc/en-au/article_attachments/62792687633433
- https://support.vald.com/hc/en-au/articles/20042352205337-Update-SmartSpeed-Plus-firmware
- https://valdperformance.com/news/buyers-guide-to-timing-gates
- https://support.vald.com/hc/en-au/articles/60458037938585-VALD-Hub-Release-Notes-27-July-2026
- https://valdperformance.com/news/the-quadrant-of-boom-sprint-speed-and-hamstring-strength
- https://valdhealth.com/calculators
- https://valdperformance.com/news/balancing-kinetics-and-kinematics-in-nfl-and-nba-training
- https://support.vald.com/hc/en-au/articles/4996450791321-Portable-Jump-Mat-SmartJump
- https://support.vald.com/hc/en-au/articles/4813503104793-SmartJump-Mat-Sensitivity
- https://valdperformance.com/news/defining-reactive-strength
- https://valdperformance.com/news/quadrant-of-boom-part-2-sprint-momentum-and-hamstring-strength
- https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource
- https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates

### HumanTrak

- https://support.vald.com/hc/en-au/articles/5001231947673-About-the-HumanTrak-system
- https://valdhealth.com/news/understanding-markerless-motion-capture-with-humantrak
- https://support.vald.com/hc/en-au/articles/50790887452185-Configure-your-HumanTrak-settings
- https://support.vald.com/hc/en-au/articles/5001237165593-Assemble-your-HumanTrak-system
- https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes
- https://support.vald.com/hc/en-au/articles/5001513298457-What-HumanTrak-measures
- https://support.vald.com/hc/en-au/articles/26519596796313-How-do-I-know-my-HumanTrak-results-are-valid-and-reliable
- https://support.vald.com/hc/en-au/article_attachments/62792822432025
- https://support.vald.com/hc/en-au/article_attachments/29041300739609
- https://valdhealth.com/news/validity-and-reliability-of-movement-analysis-methods-used-in-humantrak
- https://support.vald.com/hc/en-au/articles/4799520744857-Download-HumanTrak-Test-Data-from-VALD-Hub
- https://support.vald.com/hc/en-au/articles/42414279276441-Upload-HumanTrak-session-reports-to-VALD-Hub
- https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes
- https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API
- https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json
- https://github.com/cran/valdr/blob/master/R/humantrak_reps_by_id.R
- https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package
- https://github.com/cran/valdr/blob/master/R/session.R
- https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI
- https://support.vald.com/hc/en-au/articles/38407310924441-MoveHealth-iOS-and-Android-Release-Notes
- https://github.com/cran/valdr/blob/master/R/utils.R
- https://valdhealth.com/products/humantrak
- https://support.vald.com/hc/en-au/articles/35644465745433-HumanTrak-Test-Protocol-Single-Leg-Stand
- https://support.vald.com/hc/en-au/articles/5001637315225-HumanTrak-test-types
- https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak
- https://support.vald.com/hc/en-au/articles/61610313241113-HumanTrak-v4-3-11-Release-Notes-3-September-2026
- https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions
- https://support.vald.com/hc/en-au/articles/51806561785369-Delete-reps-in-HumanTrak
- https://support.vald.com/hc/en-au/articles/60458037938585-VALD-Hub-Release-Notes-27-July-2026
- https://support.vald.com/hc/en-au/articles/26389212508953-HumanTrak-Features-and-Limitations
- https://valdhealth.com/calculators
- https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making
- https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition
- https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second
- https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance
- https://support.vald.com/hc/en-au/articles/35644419568281-HumanTrak-Test-Protocol-Quiet-Stand
- https://support.vald.com/hc/en-au/articles/59474601544089-HumanTrak-v4-3-9-Release-Notes-7-July-2026
- https://github.com/cran/valdr/blob/master/R/humantrak_tests.R
- https://support.vald.com/hc/en-au/articles/5001791309081-HumanTrak-Metrics-Ankle-Lateral-Shift
- https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion
- https://support.vald.com/hc/en-au/articles/5001790783513-HumanTrak-Metrics-Body-Tilt
- https://support.vald.com/hc/en-au/articles/5001808549401-HumanTrak-Metrics-Center-of-Mass-COM
- https://valdhealth.com/news/centre-of-pressure-centre-of-mass
- https://support.vald.com/hc/en-au/articles/5001778255641-HumanTrak-Metrics-Elbow-Flexion
- https://support.vald.com/hc/en-au/articles/42281363737881-HumanTrak-Test-Protocol-Elbow-Extension-90%C2%BA-Abduction
- https://support.vald.com/hc/en-au/articles/42281201301401-HumanTrak-Test-Protocol-Elbow-Flexion-90%C2%BA-Abduction
- https://support.vald.com/hc/en-au/articles/5001797933849-HumanTrak-Metrics-Head-Displacement
- https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction
- https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics
- https://support.vald.com/hc/en-au/articles/5001801306393-HumanTrak-Metrics-Hip-Flexion
- https://support.vald.com/hc/en-au/articles/5001801133977-HumanTrak-Metrics-Hip-Internal-Rotation
- https://support.vald.com/hc/en-au/articles/35644408157337-HumanTrak-Test-Protocol-Seated-Hip-Internal-Rotation
- https://support.vald.com/hc/en-au/articles/35644410486297-HumanTrak-Test-Protocol-Seated-Hip-External-Rotation
- https://support.vald.com/hc/en-au/articles/62452063621017-HumanTrak-v4-3-12-Release-Notes-22-September-2026
- https://support.vald.com/hc/en-au/articles/5001775075609-HumanTrak-Metrics-Knee-Ankle-Separation-Ratio
- https://support.vald.com/hc/en-au/articles/5001757447321-HumanTrak-Metrics-Knee-Deviation
- https://support.vald.com/hc/en-au/articles/5001758606873-HumanTrak-Metrics-Knee-Displacement
- https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion
- https://support.vald.com/hc/en-au/articles/35644411765785-HumanTrak-Test-Protocol-Single-Leg-Pistol-Squat
- https://support.vald.com/hc/en-au/articles/5001731431833-HumanTrak-Metrics-Knee-Translation
- https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus
- https://support.vald.com/hc/en-au/articles/5001743573273-HumanTrak-Metrics-Neck-Displacement
- https://support.vald.com/hc/en-au/articles/5001735307545-HumanTrak-Metrics-Neck-Flexion
- https://valdhealth.com/news/humantrak-health-normative-data-report
- https://support.vald.com/hc/en-au/articles/5001742621337-HumanTrak-Metrics-Neck-Lateral-Flexion
- https://support.vald.com/hc/en-au/articles/5001742287513-HumanTrak-Metrics-Pelvic-Displacement
- https://support.vald.com/hc/en-au/articles/5001750009881-HumanTrak-Metrics-Pelvic-Lateral-Tilt
- https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case
- https://support.vald.com/hc/en-au/articles/5001734346009-HumanTrak-Metrics-Shoulder-Abduction
- https://support.vald.com/hc/en-au/articles/5001663893913-HumanTrak-Metrics-Shoulder-Flexion
- https://support.vald.com/hc/en-au/articles/34234456047641-HumanTrak-Test-Protocol-Shoulder-Flexion
- https://support.vald.com/hc/en-au/articles/5001723768857-HumanTrak-Metrics-Shoulder-Internal-Rotation
- https://support.vald.com/hc/en-au/articles/42281046622617-HumanTrak-Test-Protocol-Shoulder-External-Rotation-Neutral
- https://support.vald.com/hc/en-au/articles/40183798516761-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-Neutral
- https://support.vald.com/hc/en-au/articles/42935518748953-HumanTrak-Test-Protocol-Shoulder-Arc-of-Motion
- https://support.vald.com/hc/en-au/articles/5001703956633-HumanTrak-Metrics-Sternum-Displacement
- https://support.vald.com/hc/en-au/articles/5001714406553-HumanTrak-Metrics-Thoracic-Rotation
- https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights
- https://support.vald.com/hc/en-au/articles/5001722481177-HumanTrak-Metrics-Trunk-Flexion
- https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak
- https://support.vald.com/hc/en-au/articles/5001662862745-HumanTrak-Metrics-Trunk-Lateral-Flexion
- https://support.vald.com/hc/en-au/articles/25729073432217-HumanTrak-Test-Protocol-Trunk-Lateral-Flexion
- https://support.vald.com/hc/en-au/articles/35644475819033-HumanTrak-Test-Protocol-Tandem-Stand
- https://valdhealth.com/news/how-fighting-fit-increases-client-engagement-with-vald-technology
- https://support.vald.com/hc/en-au/articles/25728748472857-HumanTrak-Test-Protocol-Neck-Flexion
- https://support.vald.com/hc/en-au/articles/25728504625817-HumanTrak-Test-Protocol-Neck-Lateral-Flexion
- https://support.vald.com/hc/en-au/articles/25728643865369-HumanTrak-Test-Protocol-Neck-Rotation
- https://support.vald.com/hc/en-au/articles/25722108164505-HumanTrak-Test-Protocol-Shoulder-Extension
- https://support.vald.com/hc/en-au/articles/25721948248857-HumanTrak-Test-Protocol-Shoulder-Abduction
- https://support.vald.com/hc/en-au/articles/34234043658521-HumanTrak-Test-Protocol-Shoulder-Adduction
- https://support.vald.com/hc/en-au/articles/25724783730585-HumanTrak-Test-Protocol-Shoulder-External-Rotation-90%C2%BA-Abduction
- https://support.vald.com/hc/en-au/articles/34234865780249-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-90%C2%BA-Abduction
- https://valdperformance.com/news/objective-testing-for-golf-performance
- https://support.vald.com/hc/en-au/articles/34235127642649-HumanTrak-Test-Protocol-Trunk-Flexion
- https://support.vald.com/hc/en-au/articles/25728883969561-HumanTrak-Test-Protocol-Trunk-Extension
- https://support.vald.com/hc/en-au/articles/25729213590937-HumanTrak-Test-Protocol-Trunk-Rotation-Standing
- https://support.vald.com/hc/en-au/articles/61731814975257-HumanTrak-Test-Protocol-Trunk-Rotation-Seated
- https://support.vald.com/hc/en-au/articles/25720609736473-HumanTrak-Test-Protocol-Squat
- https://support.vald.com/hc/en-au/articles/25721626775833-HumanTrak-Test-Protocol-Overhead-Squat
- https://support.vald.com/hc/en-au/articles/25719992097433-HumanTrak-Test-Protocol-Single-Leg-Squat
- https://support.vald.com/hc/en-au/articles/28827078860569-HumanTrak-Test-Protocol-Lunge
- https://support.vald.com/hc/en-au/articles/25725170876697-HumanTrak-Test-Protocol-Weight-Bearing-Dorsiflexion
- https://support.vald.com/hc/en-au/articles/45825462652185-HumanTrak-Test-Protocol-Countermovement-Jump
- https://support.vald.com/hc/en-au/articles/47342472997913-HumanTrak-Test-Protocol-Single-Leg-Countermovement-Jump
- https://support.vald.com/hc/en-au/articles/48742958655513-HumanTrak-Test-Protocol-Drop-Jump
- https://support.vald.com/hc/en-au/articles/61732030982681-HumanTrak-Test-Protocol-Single-Leg-Drop-Jump
- https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump
- https://support.vald.com/hc/en-au/articles/61731984065561-HumanTrak-Test-Protocol-Single-Leg-Broad-Jump
- https://support.vald.com/hc/en-au/articles/54247081906713-HumanTrak-Test-Protocol-Lateral-Hop
- https://support.vald.com/hc/en-au/articles/54396465481369-HumanTrak-Test-Protocol-Medial-Hop
- https://support.vald.com/hc/en-au/articles/59475068735129-HumanTrak-Test-Protocol-Single-Leg-Land-and-Hold
- https://support.vald.com/hc/en-au/articles/55422903619225-HumanTrak-Test-Protocol-Sit-to-Stand-Functional
- https://support.vald.com/hc/en-au/articles/57350850787097-HumanTrak-Test-Protocol-Box-Lift-Bench
- https://support.vald.com/hc/en-au/articles/57350773616281-HumanTrak-Test-Protocol-Box-Lift-Overhead
- https://support.vald.com/hc/en-au/articles/31843457793817-HumanTrak-Test-Protocol-Standing-Posture
- https://support.vald.com/hc/en-au/articles/61731955613465-HumanTrak-Test-Protocol-Anthropometry
- https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems
- https://valdhealth.com/news/seasonal-kinematic-profiling-in-female-high-school-athletics
- https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness
- https://support.vald.com/hc/en-au/articles/52152503473561-Record-custom-measurements-with-HumanTrak

### GymAware

- https://www.valdperformance.com/news/vald-acquires-gymaware-bringing-the-gold-standard-in-velocity-based-training-into-the-worlds-leading-performance-technology-ecosystem
- https://gymaware.com/gymaware-joins-vald-performance/
- https://github.com/cran/valdr
- https://gymaware.zendesk.com/hc/en-us/articles/360001422555-How-Does-it-Work
- https://kinetic.com.au/pdf/angle.pdf
- https://gymaware.com/gymaware-rs-vs-flex/
- https://gymaware.zendesk.com/hc/en-us/articles/6947942755983-FLEX-is-not-an-accelerometer
- https://valdperformance.com/products/gymaware
- https://gymaware.zendesk.com/hc/en-us/articles/115001477352-Exporting-data-from-the-GymAware-Cloud
- https://gymaware.zendesk.com/hc/en-us/articles/115000942672-Changing-the-Metrics-on-the-Cloud
- https://gymaware.zendesk.com/hc/en-us/articles/115001477012-Exporting-data-from-the-iPad
- https://gymaware.zendesk.com/hc/en-us/articles/6947870265103-Export
- https://gymaware.com/gymaware-cloud-api-integration-guide/
- https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options
- https://cloud.gymaware.com/api/
- https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py
- https://gymaware.zendesk.com/hc/en-us/articles/15412922699919-Exercises-on-GymAware-Cloud
- https://gymaware.zendesk.com/hc/en-us/articles/115000962571-Force-Velocity-profile
- https://gymaware.zendesk.com/hc/en-us/articles/333757036735-1RM-Predictive-strength-testing
- https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud
- https://gymaware.zendesk.com/hc/en-us/articles/13390560907791-Existing-Classic-Cloud-Users-What-s-Changing-in-the-New-GymAware-Cloud
- https://gymaware.zendesk.com/hc/en-us/articles/14664428761999-Updates-to-Bar-Weight-Body-Mass-and-Distance-Settings
- https://gymaware.zendesk.com/hc/en-us/articles/360000524955-Funky-reps-Rep-mark-up-explained
- https://gymaware.zendesk.com/hc/en-us/articles/6947901584655-Rep-Detection
- https://gymaware.zendesk.com/hc/en-us/articles/115000796691-Recording-Modes
- https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics
- https://gymaware.zendesk.com/hc/en-us/articles/115001133391-GymAware-Fact-sheets
- https://gymaware.zendesk.com/hc/en-us/articles/4414960013199-GymAware-RS-Specifications
- https://gymaware.zendesk.com/hc/en-us/articles/360000067676-Rep-Detection
- https://gymaware.zendesk.com/hc/en-us/articles/360000172515-The-Clean-and-variations-rep-detection
- https://gymaware.com/do-you-need-mean-propulsive-velocity/
- https://gymaware.zendesk.com/hc/en-us/articles/333756988456-What-s-the-difference-between-Peak-Mean-Velocity
- https://gymaware.com/velocity-based-training-zones-framework/
- https://gymaware.zendesk.com/hc/en-us/articles/115001650131-What-does-BM-mean-on-the-top-right-corner-of-my-exercises
- https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware
- https://gymaware.zendesk.com/hc/en-us/articles/6948065276303-Editing-Sets
- https://gymaware.zendesk.com/hc/en-us/articles/115001148431-Peak-Power-or-Mean-Power
- https://gymaware.zendesk.com/hc/en-us/articles/9898695339023-Change-Log-History
- https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure
- https://gymaware.zendesk.com/hc/en-us/articles/6947872421007-FLEX-Metrics-Displayed
- https://gymaware.zendesk.com/hc/en-us/articles/333757036795-Jump-Testing
- https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated
- https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource
- https://valdperformance.com/news/understanding-velocity-zones-applying-velocity-based-training-to-program-design
- https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained
- https://gymaware.zendesk.com/hc/en-us/articles/115000814611-How-do-I-change-the-metric-used-of-my-bodyweight-and-bar-weight
- https://gymaware.zendesk.com/hc/en-us/articles/360000692815-How-do-I-show-hide-the-body-mass-of-my-athletes
- https://gymaware.com/gymaware-rs/
- https://gymaware.com/monitoring-fatigue/
- https://gymaware.com/reliability-and-validity-of-gymaware/
- https://gymaware.zendesk.com/hc/en-us/articles/6947987884943-FLEX-Eccentrics
- https://gymaware.zendesk.com/hc/en-us/articles/7006425471759-GymAware-Eccentrics
- https://gymaware.zendesk.com/hc/en-us/articles/360001365695-Conc-Work-J
- https://gymaware.zendesk.com/hc/en-us/articles/360003388095-Version-2-9-Release-Notes
- https://gymaware.zendesk.com/hc/en-us/articles/115004558528-Positioning-Sideways-mounting
- https://gymaware.zendesk.com/hc/en-us/articles/333756987176-PowerTool-and-Global-settings
- https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI
- https://gymaware.com/velocity-loss-in-strength-training/
- https://gymaware.com/train-to-velocity-failure-using-velocity-stops/
- https://gymaware.com/gymaware-flex-app-data-and-implementation/
- https://gymaware.com/velocity-based-training/
- https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training
- https://gymaware.zendesk.com/hc/en-us/articles/6947985838479-Set-a-Velocity-Target
- https://gymaware.com/understanding-velocity-loss/
- https://gymaware.zendesk.com/hc/en-us/articles/6947985920271-Spike-reps-Inaccurate-reps
- https://gymaware.com/gymaware-1rm-calculation/
- https://kinetic.com.au/pdf/sample.pdf
- https://gymaware.zendesk.com/hc/en-us/articles/115005013548-PowerTool-specifications
- https://gymaware.zendesk.com/hc/en-us/articles/6947901598735-FLEX-Considerations
- https://gymaware.com/barbell-vs-system-velocity/

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
