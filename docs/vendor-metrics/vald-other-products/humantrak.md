# VALD HumanTrak metrics

HumanTrak is a markerless 3D movement analysis system. It uses one depth camera to track the body, and it reports joint angles, positions, and test results for balance, range of motion, jumps, squats, posture, and custom tests. This page lists each HumanTrak metric and test output, how the vendor defines it, and what changes the number. Checked against: the VALD knowledge base HumanTrak articles (metric articles, test protocols, test types, and optimal testing conditions), the HumanTrak release notes through v4.3.12 (2026-09-22), the External HumanTrak API guide, the External HumanTrak API v2 OpenAPI spec, the `valdr` R package 4.0.0, the VALD Hub release notes, and VALD Health and VALD Performance news articles, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

This page is part of [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](README.md). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](../vald-forcedecks-nordbord/README.md).

## How to read this page

Each metric block names the exact field or Hub name and then lists these items, when the block has them:

- What it measures.
- Calculation: VALD's definition in paraphrase, then the formula in plain math where a source gives one.
- Inputs and units.
- Variants.
- Comparison with standard methods or other vendors, only where a source supports it.
- What changes the number.
- Source links.

A formula labeled Restated is this page's plain restatement, not the vendor's statement. A calculation or detail marked Not published is one that the vendor does not publish in the public sources checked. It does not mean the vendor lacks the information. KB means the VALD knowledge base at support.vald.com. None of the VALD OpenAPI specs carry field descriptions, so definitions come from the VALD knowledge base, VALD education pages, and the `valdr` R package.

## HumanTrak

### Overview

#### What the device measures

The device has these properties:

- HumanTrak is a markerless 3D movement analysis system. It uses one depth camera and a laptop. VALD says it measures a range of common single-joint and multi-joint movements ([source](https://support.vald.com/hc/en-au/articles/5001231947673-About-the-HumanTrak-system)).
- Camera: Restated: an RGB-D camera captures color and depth. A machine-learning model finds the person, locates landmarks, and builds a 3D skeleton. HumanTrak then computes joint translations and rotations in three planes ([source](https://valdhealth.com/news/understanding-markerless-motion-capture-with-humantrak)).
- Camera models: Azure Kinect or Orbbec Femto Bolt, selected in **Settings** > **Body tracking camera** ([source](https://support.vald.com/hc/en-au/articles/50790887452185-Configure-your-HumanTrak-settings)). The kit ships with the Orbbec Femto Bolt ([source](https://support.vald.com/hc/en-au/articles/5001237165593-Assemble-your-HumanTrak-system)). Orbbec support arrived in v4.1.0 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- Tracked points: VALD says the system tracks 23 points on the body at all times, in three dimensions ([source](https://support.vald.com/hc/en-au/articles/5001513298457-What-HumanTrak-measures)). The point diagram is an image. A text list of all 23 point names is Not published. Point names that appear in the metric articles: Head, Neck, SpineMid, SpineBase, Shoulder (Left and Right), Elbow, Wrist, Hip (Left and Right), Knee (Left and Right), Ankle (Left and Right), and Foot.
- Reference axes: X is left positive and right negative. Y is up positive. Z is forward negative and backward positive. Planes: transverse (horizontal), sagittal (side), coronal (front) ([source](https://support.vald.com/hc/en-au/articles/5001513298457-What-HumanTrak-measures)).
- Filtering: VALD says both the positional data and the quaternion data are smoothed ([source](https://support.vald.com/hc/en-au/articles/26519596796313-How-do-I-know-my-HumanTrak-results-are-valid-and-reliable)). Filter type and cutoff: Not published.
- Sampling rate: the HumanTrak spec sheet lists "Sampling rate 100 Hz" and "Camera type Azure Kinect DK - infrared + RGB" ([source](https://support.vald.com/hc/en-au/article_attachments/62792822432025)). That sheet names only the Azure Kinect. A rate for the Orbbec Femto Bolt is Not published. The other attachment on the technical specifications page (https://support.vald.com/hc/en-au/article_attachments/29041300739609) holds force plate specifications, not HumanTrak ones.
- Center of mass: Restated: HumanTrak estimates CoM from segment positions and population-based mass distribution data ([source](https://valdhealth.com/news/understanding-markerless-motion-capture-with-humantrak)).
- Scope: HumanTrak assesses discrete, controlled movements in a fixed capture area. It does not provide gait analysis ([source](https://valdhealth.com/news/validity-and-reliability-of-movement-analysis-methods-used-in-humantrak)).
- Validity summary from VALD's write-up of Collings et al. (2024), which used the Azure Kinect: between-day ICCs 0.80 to 0.93, joint angle MAE about 4.8°, and two to four trials enough for most tasks ([source](https://valdhealth.com/news/validity-and-reliability-of-movement-analysis-methods-used-in-humantrak)). The study measured lower-limb angles in jumps, squats, and treadmill walking and running. HumanTrak does not offer the treadmill tasks. No equivalent published data covers the Orbbec Femto Bolt.

#### Export routes

HumanTrak data leaves the system through these routes:

- **VALD Hub.** Session PDF reports, CSV files, and snapshots download from VALD Hub, through a profile's **Results Table** or the **HumanTrak** tab in **VALD Systems** ([steps](https://support.vald.com/hc/en-au/articles/4799520744857-Download-HumanTrak-Test-Data-from-VALD-Hub)). Session report PDFs that were uploaded to VALD Hub can also be exported from **Results Export** under **VALD Systems** or from a profile's **Result Table** ([source](https://support.vald.com/hc/en-au/articles/42414279276441-Upload-HumanTrak-session-reports-to-VALD-Hub)). A 2024-10-31 Hub release note names the same exports as **Profile** > **Result Table** or **Dashboard** > **Results Export** ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). The CSV column list and row layout are Not published.
- **External HumanTrak API v2.** Region hosts are `prd-aue-`, `prd-use-`, and `prd-euw-api-externalhumantrakv2.valdperformance.com` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). All data paths need authentication. The spec lists these paths ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)):
  - `GET /v2/tests-by-modified-date?TenantId=&ModifiedFromUtc=` returns test results: test identifiers, `repetitionCounts`, and `metricGroups` with `summaryMeasurements` and `asymmetryMeasurement`. Results come oldest to newest by modification date. Page until the API returns 204 No Content ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
  - `GET /v2/test/{testId}/repetitions?TenantId=&ProfileId=` returns one entry per repetition with per-rep metric values ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). The KB writes the query parameters in lower camel case, `tenantId` and `profileId` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). valdr sends `TenantId` and `ProfileId` ([source](https://github.com/cran/valdr/blob/master/R/humantrak_reps_by_id.R)).
  - `GET /v2/test-type/metrics` returns the catalog of test types and metric definitions. It takes no parameters ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The catalog contents are not public, so the per-test metric list in this section comes from the KB and VALD articles.
  - `GET /version`, `/liveness`, `/readiness`, and `/diagnostics` are service health paths. They return no athlete data ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)).
- **valdr 4.0.0** ([source](https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package)) has these functions:
  - `get_humantrak_data(start_date)` returns a list of `profiles`, `tests`, `repetition_counts`, `metric_groups`, `summary_measurements`, and `test_type_metrics` ([source](https://github.com/cran/valdr/blob/master/R/session.R)).
  - `get_humantrak_tests_only(start_date)` returns the `tests` table only ([source](https://github.com/cran/valdr/blob/master/R/session.R)).
  - `get_humantrak_repetitions_by_id(test_id, profile_id)` returns one row per repetition metric ([source](https://github.com/cran/valdr/blob/master/R/session.R)).
  - `get_humantrak_test_type_metrics_only()` returns the flattened catalog ([source](https://github.com/cran/valdr/blob/master/R/session.R)).
- **Other routes.** VALD Connect (beta) lists HumanTrak as a supported Power BI dataset. Its HumanTrak table layout is Not published ([source](https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI)). Patients can see some HumanTrak results in MoveHealth ([source](https://support.vald.com/hc/en-au/articles/38407310924441-MoveHealth-iOS-and-Android-Release-Notes)).

#### Row level

The row structure depends on the route:

- API `/v2/tests-by-modified-date`: one object per test. Each test nests one `metricGroups` entry per metric the test type supports. Each metric group nests one `summaryMeasurements` entry per side recorded and one `asymmetryMeasurement` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- API `/v2/test/{testId}/repetitions`: one object per repetition, with one entry per metric group ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- valdr tables ([source](https://github.com/cran/valdr/blob/master/R/utils.R)):
  - `tests`: one row per test.
  - `repetition_counts`: one row per test and `movementSide`.
  - `metric_groups`: one row per test and metric group, with the asymmetry aggregates as columns.
  - `summary_measurements`: one row per test, metric group, and side.
  - repetitions: one row per repetition and metric group.
  - `test_type_metrics`: one row per test type, metric group, and repetition metric type.
- VALD Hub CSV: Not published.

#### Left and right labels

Side labels vary by field:

- `summaryMeasurements[].side` is a free string. The KB example uses `"Left"` and `"Right"` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- `repetitionCounts[].movementSide` uses the `MovementSide` enum: `Left`, `Right`, `Both`, `None`, `NotApplicable` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). The KB example shows `"Both"` for a squat ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- `repetitions[].side` is a free string in the spec, not the enum. The KB lists `"Both"` for bilateral reps, `"Left"` or `"Right"` for unilateral reps, and `"NotApplicable"` for reps with no side, such as trunk flexion ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- Per-rep metric values carry `leftValue` and `rightValue` when `isSided` is true, and `unsidedValue` when false. In a unilateral test the side that did not perform returns null ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- Catalog entries carry `movementSide` and `metricSide` strings. Their values and meanings are Not published ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)).
- HumanTrak detects left and right automatically during testing ([source](https://valdhealth.com/products/humantrak)). Balance stands auto-detect the tested leg ([source](https://support.vald.com/hc/en-au/articles/35644465745433-HumanTrak-Test-Protocol-Single-Leg-Stand)).
- Each metric article sets its own sign. For example, right lateral trunk tilt is positive, but a left hip drop is positive for pelvic tilt. Check each block below.
- Hub CSV side labels: Not published.

#### Test types

The Test Library groups tests into these categories ([source](https://support.vald.com/hc/en-au/articles/5001637315225-HumanTrak-test-types)):

- Balance: Quiet Stand, Tandem Stand, and Single Leg Stand, each with Eyes Open and Eyes Closed.
- Upper Body ROM: Elbow Extension - 90° Shoulder Abduction, Elbow Flexion - 90° Shoulder Abduction, Neck Flexion, Neck Lateral Flexion, Neck Rotation, Shoulder Abduction, Shoulder Adduction, Shoulder Arc of Motion, Shoulder Extension, Shoulder External Rotation - 90° Abduction, Shoulder External Rotation - Neutral, Shoulder Flexion, Shoulder Internal Rotation - 90° Abduction, Shoulder Internal Rotation - Neutral, Trunk Extension, Trunk Flexion, Trunk Lateral Flexion, Trunk Rotation - Seated, Trunk Rotation - Standing.
- Lower Body ROM: Seated Hip External Rotation, Seated Hip Internal Rotation.
- Lower Body Dynamic: Broad Jump, Countermovement Jump, Drop Jump, Lateral Hop, Lunge, Medial Hop, Overhead Squat, Single Leg Broad Jump, Single Leg Countermovement Jump, Single Leg Drop Jump, Single Leg Heel Raise - Endurance, Single Leg Land and Hold, Single Leg Pistol Squat, Single Leg Squat, Sit to Stand - 30-second, Sit to Stand - 5-repetition, Sit to Stand - Functional, Squat, Weight Bearing Dorsiflexion.
- Posture: Anthropometry, Standing Posture.
- Functional Lifts: Box Lift - Bench, Box Lift - Overhead.
- Custom Tests: user-defined tests with one or two metrics ([source](https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak)).

API test type codes: only `TT_SQUAT-DL` appears in a public source, for the Squat example ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). All other codes are Not published.

History that affects old data: in v4.1.1, VALD split four bidirectional tests into eight one-direction tests (Shoulder Flexion, Extension, Abduction, Adduction, External Rotation, Internal Rotation, Trunk Flexion, Trunk Extension). VALD states that the app will not show historical data for the previous bidirectional tests ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). In v4.3.11, Trunk Rotation became separate Seated and Standing tests ([source](https://support.vald.com/hc/en-au/articles/61610313241113-HumanTrak-v4-3-11-Release-Notes-3-September-2026)).

#### Conditions that change every HumanTrak number

These apply to all blocks below. Each block lists only the extra, metric-specific factors. The shared conditions are:

- Calibration: lower-limb sessions start with a standing calibration that captures baseline posture. Fidgeting, talking, or stepping out of the position circle degrades it. Redo the test if results look wrong ([source](https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions)). Since v4.3.0, one calibration covers a run of dynamic lower-limb tests ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- Clothing and hair: loose, dark, shiny, or reflective clothing and long hair over the shoulders interfere with tracking ([source](https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions)).
- Environment: direct sun, bright overhead light, mirrors, and glossy floors interfere. Use the system indoors at 10 to 25°C (50 to 77°F) ([source](https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions)).
- Camera: about 1 m high, not tilted, nothing blocking the view, and the whole body in frame ([source](https://support.vald.com/hc/en-au/articles/52147000726041-HumanTrak-optimal-testing-conditions)). The tripod setup article gives about 90 cm ([source](https://support.vald.com/hc/en-au/articles/5001237165593-Assemble-your-HumanTrak-system)).
- Distance: the position circle places the person 2 m from the camera for neck ROM, 3 m for Weight Bearing Dorsiflexion, 3.5 m for Lunge, and 2.5 m for all other tests (v4.1.2) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Turning the position circle off "may impact accuracy of results" ([source](https://support.vald.com/hc/en-au/articles/50790887452185-Configure-your-HumanTrak-settings)).
- Facing direction: most tests face the camera. Trunk Flexion, Trunk Extension, Broad Jump, Single Leg Broad Jump, Single Leg Heel Raise, Box Lifts, and the second Standing Posture and Anthropometry captures are side-on. See the protocols linked in the test table.
- Rep detection and thresholds: reps are detected automatically. Several tests have minimum ranges (see the test table). Manual Mode or manual override lowers thresholds for some tests, so reps with smaller ranges get recorded ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- Deleted reps: practitioners can delete reps in the app ([source](https://support.vald.com/hc/en-au/articles/51806561785369-Delete-reps-in-HumanTrak)) and, since 2026-07-27, in VALD Hub ([source](https://support.vald.com/hc/en-au/articles/60458037938585-VALD-Hub-Release-Notes-27-July-2026)). Aggregates change when reps are removed. Whether the API recomputes aggregates after a Hub deletion is Not published.
- One side only: VALD states that asymmetry results are unavailable when only one side is tested ([source](https://support.vald.com/hc/en-au/articles/26389212508953-HumanTrak-Features-and-Limitations)).
- Units: distance metrics can display in imperial units based on the organization setting in VALD Hub ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Whether the API returns metric or display units is Not published. Read the `unit` field on every row.

### API result structure

These fields hold the numbers for every metric group. They apply to all metrics in the later sections.

#### `summaryMeasurements[].aggregates.max`, `summaryMeasurements[].aggregates.min`, `summaryMeasurements[].aggregates.avg` (unit in `summaryMeasurements[].unit`)

The block has these fields:

- **What it measures:** The largest, smallest, and mean value of one metric group for one side across the reps of a test.
- **Calculation:** Not published. Restated from the KB: `summaryMeasurements` contains aggregates for each side of the body that was recorded ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). Whether `max` is the largest per-rep value and `avg` is the mean of per-rep values is not stated. The in-app primary metric shows "peak and average of peaks" (v4.1.3) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Inputs and units:** `unit` is a string. The KB example uses `"Degrees"`. Other unit strings are Not published.
- **Variants:** One entry per `side`. valdr columns are `max`, `min`, `avg`, `side`, `unit`, and `metricGroupCode` in `summary_measurements` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). The catalog field `summaryMetricTypes[].calculationType` probably names the aggregate, but its values are Not published ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)).
- **What changes the number:** Deleted reps, partial reps, and rep count. For Squat and Overhead Squat, the in-app best rep is the rep with the highest peak knee flexion on either side, and the primary metric is the higher of left and right from that rep only (v4.2.8) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Whether that rule affects API aggregates is Not published.
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json, https://github.com/cran/valdr/blob/master/R/utils.R, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `asymmetryMeasurement.aggregates.max`, `asymmetryMeasurement.aggregates.min`, `asymmetryMeasurement.aggregates.avg` (unit in `asymmetryMeasurement.unit`, example `"Percent"`)

The block has these fields:

- **What it measures:** The left-right difference for one metric group, as three aggregates.
- **Calculation:** Not published for HumanTrak. VALD's calculator formula is Asymmetry = (Right Value - Left Value) / Higher Value x 100 ([source](https://valdhealth.com/calculators), [source](https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making)). No source says HumanTrak uses it.
- **KB example, as written:** for `MG_SQUAT-DL_HIP-FLEX-AT-KNEE-FLEX-PEAK`, the KB shows `max` 2.59, `min` 16.21, and `avg` 9.34 ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). Here `max` is lower than `min`. Observation, not a VALD statement: each value matches (Right - Left) / higher x 100 applied to the matching pair of side aggregates in the same example. Left and right maxima 69.85 and 71.71 give 2.59. Minima 23.68 and 28.26 give 16.21. Averages 43.22 and 47.67 give 9.34. So in this example, `max` is the asymmetry of the side maxima, not the largest asymmetry. Right was higher in all three pairs, so the example cannot show the sign rule.
- **Inputs and units:** The left and right summary aggregates of the same metric group, if the observation holds.
- **Variants:** valdr flattens these to `asymmetryUnit`, `asymmetryMax`, `asymmetryMin`, and `asymmetryAvg` in `metric_groups` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). The catalog lists `asymmetryMetricTypes[]` with `code`, `name`, `leftSummaryMetricTypeCode`, and `rightSummaryMetricTypeCode` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). That link from asymmetry to a left and a right summary metric fits the observation above.
- **What changes the number:** Testing one side only removes asymmetry ([source](https://support.vald.com/hc/en-au/articles/26389212508953-HumanTrak-Features-and-Limitations)). Unsided metrics have no asymmetry, but the API behavior for them is Not published.
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json, https://github.com/cran/valdr/blob/master/R/utils.R, https://valdhealth.com/calculators

#### `repetitionCounts[].count` (reps)

The block has these fields:

- **What it measures:** The number of reps recorded for a test, per `movementSide`.
- **Calculation:** Restated: a count of detected reps. The KB example shows `"movementSide": "Both"` with `count` 6 for a squat ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- **Inputs and units:** Integer.
- **Variants:** One row per `movementSide` (`Left`, `Right`, `Both`, `None`, `NotApplicable`) ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). valdr columns: `testId`, `movementSide`, `count` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)).
- **What changes the number:** Rep detection thresholds, deleted reps, and test rules. Sit to Stand - 5-repetition ends after five reps ([source](https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition)). Sit to Stand - 30-second counts reps for 30 s ([source](https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second)). Single Leg Heel Raise - Endurance runs to fatigue or technique failure ([source](https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance)). Balance tests record one rep per test ([source](https://support.vald.com/hc/en-au/articles/35644419568281-HumanTrak-Test-Protocol-Quiet-Stand)), though v4.3.9 lets balance tests hold up to 100 reps ([source](https://support.vald.com/hc/en-au/articles/59474601544089-HumanTrak-v4-3-9-Release-Notes-7-July-2026)).
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json, https://github.com/cran/valdr/blob/master/R/utils.R

#### Repetition values: `values.isSided`, `values.leftValue`, `values.rightValue`, `values.unsidedValue` (unit of the metric group)

The block has these fields:

- **What it measures:** The value of one metric group in one rep.
- **Calculation:** Restated from the KB: if `isSided` is true, the rep returns `leftValue` and `rightValue`. If false, it returns `unsidedValue`. In unilateral tests, the side that did not perform is null ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). Which moment in the rep each value comes from depends on the metric group name (for example "at peak knee flexion").
- **Inputs and units:** Units are not returned on the repetitions endpoint. Get them from the catalog `repetitionMetricTypes[].unit` or the summary `unit` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)).
- **Spec versus KB and valdr:** The spec defines the values object with `isSided` only and `"additionalProperties": false` ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)). The KB example returns `leftValue`, `rightValue`, and `unsidedValue` ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). valdr reads `unsidedValue`, `leftValue`, and `rightValue` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). Treat the spec as incomplete here. The KB example also lacks a comma after `"leftValue": 11.11`, so it is not valid JSON as printed.
- **Variants:** valdr columns: `testTypeCode`, `repetitionNumber`, `repetitionSide`, `metricGroupCode`, `isSided`, `unsidedValue`, `leftValue`, `rightValue` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). KB example codes: `MG_SQUAT-DL_ANKLE-DORSIFLEXION-AT-PEAK-KNEE-FLEXION` (sided, 11.11 and 13.89) and `MG_SQUAT-DL_PELVIS-ANTERIOR-TILT-AT-KNEE-FLEX-PEAK` (unsided, 22.22) ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- **What changes the number:** Everything in the shared conditions list above.
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json, https://github.com/cran/valdr/blob/master/R/utils.R

#### Metric group descriptors: `code`, `longName`, `shortName`, `classification`, `trendSentiment`

These are not metric values, so the block has no full field list. The KB example has `code` `MG_SQUAT-DL_HIP-FLEX-AT-KNEE-FLEX-PEAK`, `longName` "Hip Flexion at Peak Knee Flexion", `shortName` "Hip Flexion", `classification` "Secondary", and `trendSentiment` "Negative" ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The full list of `classification` and `trendSentiment` values and their meanings is Not published. VALD removed metric taglines such as "Higher value is generally preferred" from ROM tests in v4.1.2 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). No source links those taglines to `trendSentiment`.

#### Identifiers and context fields

`GET /v2/tests-by-modified-date` returns these fields ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)):

| Field | Type | Notes |
|---|---|---|
| `data.testResults[]` | array | Envelope. Each element is one test. valdr reads `data$testResults`. |
| `testId` | uuid | Test key. |
| `profileId` | uuid | Athlete key. Join to Profiles. |
| `tenantId` | uuid | Organization key. |
| `startDateUtc`, `endDateUtc` | date-time | Test start and end. |
| `modifiedDateUtc` | date-time | Paging cursor. KB: use the exact high-precision value; do not round it ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). |
| `testTypeCode` | string | For example `TT_SQUAT-DL`. |
| `metricGroups[].code` | string | Metric group key. valdr names it `code` in `metric_groups` and `metricGroupCode` in `summary_measurements`. |
| `summaryMeasurements[].side`, `.unit` | string | Side label and unit. |
| `asymmetryMeasurement.unit` | string | Example `"Percent"`. |

Paging note: valdr pages with the exact last `modifiedDateUtc` inside one call. After the call it strips fractional seconds before saving the start date for the next call ([source](https://github.com/cran/valdr/blob/master/R/humantrak_tests.R)). The KB says not to round ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The next valdr call can return tests from the same second again. Upsert by `testId`.

`GET /v2/test/{testId}/repetitions` returns these fields ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)):

| Field | Type | Notes |
|---|---|---|
| `testTypeCode` | string | Test type of the test. |
| `repetitions[].number` | int32 | Rep number, 1, 2, 3, and so on. |
| `repetitions[].side` | string | `Both`, `Left`, `Right`, or `NotApplicable` per the KB. |
| `metrics[].metricGroupCode` | string | Joins to `metricGroups[].code`. |

`GET /v2/test-type/metrics` returns these fields ([source](https://prd-use-api-externalhumantrakv2.valdperformance.com/swagger/v2/swagger.json)):

| Field | Type | Notes |
|---|---|---|
| `testTypes[].code`, `.name`, `.laterality` | string | Test type key, name, and laterality. Laterality values: Not published. |
| `metricGroups[].code`, `.longName`, `.shortName`, `.classification`, `.trendSentiment` | string | As in test results. |
| `repetitionMetricTypes[].code`, `.name`, `.movementSide`, `.metricSide`, `.unit` | string | Per-rep metric definitions. |
| `summaryMetricTypes[].code`, `.name`, `.movementSide`, `.metricSide`, `.unit`, `.calculationType` | string | Per-test aggregate definitions. |
| `asymmetryMetricTypes[].code`, `.name`, `.leftSummaryMetricTypeCode`, `.rightSummaryMetricTypeCode` | string | Links each asymmetry to its left and right summary metrics. |

valdr differs from the spec in these ways for the catalog ([source](https://github.com/cran/valdr/blob/master/R/utils.R)):

- valdr reads `metricGroups[].asymmetrySupported`, which the spec does not list.
- valdr reads `side` on each repetition metric type, which the spec does not list. The spec lists `movementSide` and `metricSide` instead. Unless the live API also sends `side`, the valdr `side` column will be empty.
- valdr outputs only `repetitionMetricTypes`. It drops `summaryMetricTypes` (including `calculationType`) and `asymmetryMetricTypes`.

### Joint angle and position metrics

These 27 metrics come from the KB "HumanTrak Metrics" articles. The articles do not give API codes. Expect the names inside `longName` or `shortName`, often with a time point such as "at Peak Knee Flexion". Angles are in degrees; the articles mark them with °. Displacement units are not stated in the articles; read the `unit` field.

Variants that apply to every block in this section: per-side values where the metric is sided (`leftValue`, `rightValue`, `summaryMeasurements` per `side`), unsided values otherwise (`unsidedValue`), the `max`, `min`, and `avg` aggregates, and asymmetry where the metric is sided. Per kg variants do not exist for these metrics. Which tests report each metric as sided is Not published.

#### `Ankle Lateral Shift` (unit Not published)

The block has these fields:

- **What it measures:** How far the ankle sits sideways from the middle of the hips.
- **Calculation:** VALD defines it as the medial-lateral distance between the hip midpoint and the ankle marker ([source](https://support.vald.com/hc/en-au/articles/5001791309081-HumanTrak-Metrics-Ankle-Lateral-Shift)). Restated: shift = side-to-side distance from the midpoint of HipLeft and HipRight to the Ankle point. Positive when the ankle is lateral to the hip midpoint.
- **Inputs and units:** HipLeft, HipRight, and Ankle points. Unit Not published.
- **Variants:** See the section note. The article does not say which ankle is used in two-leg stance.
- **What changes the number:** Stance width and foot placement. VALD's example use is posture in the Single Leg Stand ([source](https://support.vald.com/hc/en-au/articles/5001791309081-HumanTrak-Metrics-Ankle-Lateral-Shift)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001791309081-HumanTrak-Metrics-Ankle-Lateral-Shift

#### `Ankle Plantarflexion` (degrees)

The block has these fields:

- **What it measures:** The angle between the foot and the shin, seen from the side.
- **Calculation:** VALD defines it as the angle between the foot and tibia segments, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion)). Restated: Foot segment = Foot to Ankle points. Tibia segment = Knee to Ankle points. A flat foot with a vertical tibia reads 90°. Dorsiflexion is positive.
- **Inputs and units:** Foot, Ankle, and Knee points. Degrees.
- **Variants:** See the section note. The article's name says plantarflexion but its sign makes dorsiflexion positive, and it sets neutral at 90°, not 0°. Whether the API "Ankle Dorsiflexion" metric groups (for example `MG_SQUAT-DL_ANKLE-DORSIFLEXION-AT-PEAK-KNEE-FLEXION`) use this angle or a 0° neutral is Not published. The KB example values for that group are 11.11 and 13.89 ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- **What changes the number:** Foot tracking. VALD's example use is foot position on landing in the Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion, https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API

#### `Body Tilt` (degrees)

The block has these fields:

- **What it measures:** How far the whole body leans forward from vertical, seen from the side.
- **Calculation:** VALD defines it as the angle between vertical and the body, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001790783513-HumanTrak-Metrics-Body-Tilt)). Restated: Body = line from the ankle midpoint (between AnkleLeft and AnkleRight) to the Neck point. Vertical is 0°. Forward lean is positive.
- **Inputs and units:** AnkleLeft, AnkleRight, and Neck points. Degrees.
- **Variants:** See the section note. Likely unsided, but not stated.
- **What changes the number:** Facing direction. VALD's example uses are forward lean in Standing Posture and landing position in the Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001790783513-HumanTrak-Metrics-Body-Tilt)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001790783513-HumanTrak-Metrics-Body-Tilt

#### `Center of Mass (COM)` (unit Not published)

The block has these fields:

- **What it measures:** The estimated balance point of the whole body.
- **Calculation:** VALD says the center of mass is determined from the location and estimated mass of the body segments ([source](https://support.vald.com/hc/en-au/articles/5001808549401-HumanTrak-Metrics-Center-of-Mass-COM)). Restated: CoM = mass-weighted average of segment positions, using population-based mass distribution data ([source](https://valdhealth.com/news/understanding-markerless-motion-capture-with-humantrak)). The segment model and mass fractions are Not published.
- **Inputs and units:** All tracked segments. Unit Not published.
- **Variants:** Derived CoM metrics appear in later blocks: jump height, countermovement depth, jump distance, takeoff angle, and balance CoM measures. The article itself defines no exported field name.
- **What changes the number:** Body shape and clothing affect segment tracking. CoM is not the same as centre of pressure from force plates ([source](https://valdhealth.com/news/centre-of-pressure-centre-of-mass)). VALD's example uses are the Single Leg Stand and Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001808549401-HumanTrak-Metrics-Center-of-Mass-COM)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001808549401-HumanTrak-Metrics-Center-of-Mass-COM, https://valdhealth.com/news/understanding-markerless-motion-capture-with-humantrak, https://valdhealth.com/news/centre-of-pressure-centre-of-mass

#### `Elbow Flexion` (degrees)

The block has these fields:

- **What it measures:** How much the elbow bends.
- **Calculation:** VALD defines it as the 3D angle between the upper arm and forearm segments ([source](https://support.vald.com/hc/en-au/articles/5001778255641-HumanTrak-Metrics-Elbow-Flexion)). Restated: Upper Arm = Shoulder to Elbow points. Forearm = Elbow to Wrist points. A straight arm is 0°. Flexion is positive.
- **Inputs and units:** Shoulder, Elbow, and Wrist points. Degrees.
- **Variants:** See the section note. The Elbow Extension test expresses extension as a negative of flexion. VALD's protocol asks for at least 70 degrees of elbow flexion, which it equates to -70 degrees of elbow extension ([source](https://support.vald.com/hc/en-au/articles/42281363737881-HumanTrak-Test-Protocol-Elbow-Extension-90%C2%BA-Abduction)).
- **What changes the number:** Start position at 90° shoulder abduction and 90° elbow flexion. Rep thresholds: 110° flexion for Elbow Flexion ([source](https://support.vald.com/hc/en-au/articles/42281201301401-HumanTrak-Test-Protocol-Elbow-Flexion-90%C2%BA-Abduction)) and 70° for Elbow Extension. VALD's example use is the Overhead Squat ([source](https://support.vald.com/hc/en-au/articles/5001778255641-HumanTrak-Metrics-Elbow-Flexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001778255641-HumanTrak-Metrics-Elbow-Flexion, https://support.vald.com/hc/en-au/articles/42281363737881-HumanTrak-Test-Protocol-Elbow-Extension-90%C2%BA-Abduction, https://support.vald.com/hc/en-au/articles/42281201301401-HumanTrak-Test-Protocol-Elbow-Flexion-90%C2%BA-Abduction

#### `Head Displacement` (unit Not published)

The block has these fields:

- **What it measures:** How far forward or back the head sits over the feet.
- **Calculation:** VALD defines it as the anterior-posterior distance between the head marker and the footbase ([source](https://support.vald.com/hc/en-au/articles/5001797933849-HumanTrak-Metrics-Head-Displacement)). Restated: Footbase = midpoint of AnkleLeft and AnkleRight. The sign convention is Not published.
- **Inputs and units:** Head, AnkleLeft, and AnkleRight points. Unit Not published.
- **Variants:** See the section note. Likely unsided.
- **What changes the number:** Stance and facing direction. VALD's example uses are Standing Posture and the Squat ([source](https://support.vald.com/hc/en-au/articles/5001797933849-HumanTrak-Metrics-Head-Displacement)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001797933849-HumanTrak-Metrics-Head-Displacement

#### `Hip Abduction` (degrees)

The block has these fields:

- **What it measures:** How far the thigh moves out to the side, seen from the front.
- **Calculation:** VALD defines it as the angle between the femur and pelvis segments, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction)). Restated: Femur = Knee to Hip points. Pelvis = HipLeft to HipRight. A femur pointing straight down is 0°. Abduction is positive.
- **Inputs and units:** Knee, HipLeft, and HipRight points. Degrees.
- **Variants:** See the section note. The squat article names "Hip adduction at peak knee flexion" as a HumanTrak squat metric with limb symmetry options ([source](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)). Whether it is this angle with the sign flipped is Not published.
- **What changes the number:** In v4.2.0, VALD fixed the polarity of the hip internal rotation and hip adduction metrics ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Data recorded before v4.2.0 (2024-10-17) may have the opposite sign. VALD's example uses are Standing Posture and the Squat ([source](https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics

#### `Hip Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the thigh bends up toward the trunk, seen from the side.
- **Calculation:** VALD defines it as the angle between the lower trunk and femur segments, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001801306393-HumanTrak-Metrics-Hip-Flexion)). Restated: Lower Trunk = SpineBase to SpineMid. Femur = Knee to Hip. Standing upright is 0°. Flexion is positive.
- **Inputs and units:** SpineBase, SpineMid, Hip, and Knee points. Degrees.
- **Variants:** See the section note. The API example metric group `MG_SQUAT-DL_HIP-FLEX-AT-KNEE-FLEX-PEAK` ("Hip Flexion at Peak Knee Flexion") reads hip flexion at the moment of peak knee flexion, per side ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). It has its own block below.
- **What changes the number:** Trunk posture changes the lower trunk reference, so trunk lean changes the value. VALD's example uses are Standing Posture and the Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001801306393-HumanTrak-Metrics-Hip-Flexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001801306393-HumanTrak-Metrics-Hip-Flexion, https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API

#### `Hip Internal Rotation` (degrees)

The block has these fields:

- **What it measures:** How far the shin swings out from vertical in a seated hip rotation test, seen from the front.
- **Calculation:** VALD defines it as the angle between vertical and the tibia segment, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001801133977-HumanTrak-Metrics-Hip-Internal-Rotation)). Restated: Tibia = Knee to Ankle points. A tibia pointing straight down is 0°. Internal rotation is positive. The external rotation sign is not stated.
- **Inputs and units:** Knee and Ankle points. Degrees.
- **Variants:** See the section note. The Seated Hip External Rotation test uses the same article, per its example use.
- **What changes the number:** Pelvic tilt or hip abduction and adduction during the test. The protocols tell the tester to cue against them ([source](https://support.vald.com/hc/en-au/articles/35644408157337-HumanTrak-Test-Protocol-Seated-Hip-Internal-Rotation)). Reps need at least 10° of rotation ([source](https://support.vald.com/hc/en-au/articles/35644410486297-HumanTrak-Test-Protocol-Seated-Hip-External-Rotation)). v4.2.0 fixed the polarity of hip internal rotation ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). v4.3.9 and v4.3.12 changed calibration and rep detection for these tests, and v4.3.12 added Manual Mode ([source](https://support.vald.com/hc/en-au/articles/62452063621017-HumanTrak-v4-3-12-Release-Notes-22-September-2026)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001801133977-HumanTrak-Metrics-Hip-Internal-Rotation, https://support.vald.com/hc/en-au/articles/35644408157337-HumanTrak-Test-Protocol-Seated-Hip-Internal-Rotation, https://support.vald.com/hc/en-au/articles/35644410486297-HumanTrak-Test-Protocol-Seated-Hip-External-Rotation, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Knee Ankle Separation Ratio` (ratio, no unit)

The block has these fields:

- **What it measures:** Whether the knees are wider or narrower than the ankles.
- **Calculation:** VALD defines it as the medial-lateral distance between the KneeRight and KneeLeft markers, divided by the distance between the AnkleRight and AnkleLeft markers ([source](https://support.vald.com/hc/en-au/articles/5001775075609-HumanTrak-Metrics-Knee-Ankle-Separation-Ratio)). Restated: ratio = knee width / ankle width. Above 1 means the knees are apart. Below 1 means the knees come together.
- **Inputs and units:** KneeLeft, KneeRight, AnkleLeft, and AnkleRight points. No unit.
- **Variants:** Unsided by definition. Aggregates as in the section note.
- **What changes the number:** Stance width. v4.3.2 added this metric to the Overhead Squat ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). VALD's example use is the Squat ([source](https://support.vald.com/hc/en-au/articles/5001775075609-HumanTrak-Metrics-Knee-Ankle-Separation-Ratio)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001775075609-HumanTrak-Metrics-Knee-Ankle-Separation-Ratio, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Knee Deviation` (unit Not published)

The block has these fields:

- **What it measures:** How much the knee wanders side to side over the test.
- **Calculation:** VALD defines it as the total medial-lateral movement of the knee ([source](https://support.vald.com/hc/en-au/articles/5001757447321-HumanTrak-Metrics-Knee-Deviation)). Restated: the summed side-to-side path of the knee point over time. Always positive. Whether it sums the path length or takes the range is Not published.
- **Inputs and units:** Knee point over time. Unit Not published.
- **Variants:** See the section note.
- **What changes the number:** Test duration, if it is a path sum. VALD's example uses are the Single Leg Stand and Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001757447321-HumanTrak-Metrics-Knee-Deviation)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001757447321-HumanTrak-Metrics-Knee-Deviation

#### `Knee Displacement` (unit Not published)

The block has these fields:

- **What it measures:** How far forward the knees travel over the feet.
- **Calculation:** VALD defines it as the anterior-posterior distance between the knee midpoint and the footbase ([source](https://support.vald.com/hc/en-au/articles/5001758606873-HumanTrak-Metrics-Knee-Displacement)). Restated: Knee midpoint = midpoint of KneeLeft and KneeRight. Footbase = midpoint of AnkleLeft and AnkleRight. The sign convention is Not published.
- **Inputs and units:** KneeLeft, KneeRight, AnkleLeft, and AnkleRight points. Unit Not published.
- **Variants:** Uses both knees, so likely unsided. See the section note.
- **What changes the number:** Squat depth and stance. VALD's example uses are the Squat and Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001758606873-HumanTrak-Metrics-Knee-Displacement)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001758606873-HumanTrak-Metrics-Knee-Displacement

#### `Knee Flexion` (degrees)

The block has these fields:

- **What it measures:** How much the knee bends.
- **Calculation:** VALD defines it as the 3D angle between the femur and tibia segments ([source](https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion)). Restated: Femur = Knee to Hip. Tibia = Knee to Ankle. A straight leg is 0°. Flexion is positive.
- **Inputs and units:** Hip, Knee, and Ankle points. Degrees.
- **Variants:** See the section note. Peak knee flexion has its own block below.
- **What changes the number:** Depth cue. The Single Leg Pistol Squat needs at least 30° knee flexion for a rep ([source](https://support.vald.com/hc/en-au/articles/35644411765785-HumanTrak-Test-Protocol-Single-Leg-Pistol-Squat)). VALD's example uses are Standing Posture and the Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion, https://support.vald.com/hc/en-au/articles/35644411765785-HumanTrak-Test-Protocol-Single-Leg-Pistol-Squat

#### `Knee Translation` (unit Not published)

The block has these fields:

- **What it measures:** The largest shift of the knee, forward-back or side to side.
- **Calculation:** VALD defines it as the maximum translation of the knee marker, in the anterior-posterior or medial-lateral direction ([source](https://support.vald.com/hc/en-au/articles/5001731431833-HumanTrak-Metrics-Knee-Translation)). Restated: the largest knee movement from a reference position. The reference position and how the direction is chosen are Not published.
- **Inputs and units:** Knee point. Unit Not published.
- **Variants:** See the section note. The article covers two directions. Whether they export as separate fields is Not published.
- **What changes the number:** VALD's example uses are the Squat, the ankle dorsiflexion test, and the Drop Jump ([source](https://support.vald.com/hc/en-au/articles/5001731431833-HumanTrak-Metrics-Knee-Translation)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001731431833-HumanTrak-Metrics-Knee-Translation

#### `Knee Valgus` (degrees)

The block has these fields:

- **What it measures:** The knee's inward or outward angle, seen from the front.
- **Calculation:** VALD defines it as the angle between the femur and tibia segments, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus)). Restated: Femur = Knee to Hip. Tibia = Knee to Ankle. A straight leg is 0°. The article's sign rule is "Varus = positive". So valgus reads negative under this article.
- **Inputs and units:** Hip, Knee, and Ankle points. Degrees.
- **Variants:** See the section note. "Dynamic knee valgus" for the Single Leg Squat has its own block below.
- **What changes the number:** Foot rotation and camera angle affect a front-plane projection. VALD's example uses are Standing Posture and the Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus

#### `Neck Displacement` (unit Not published)

The block has these fields:

- **What it measures:** How far forward or back the neck sits over the feet.
- **Calculation:** VALD defines it as the anterior-posterior distance between the neck marker and the footbase ([source](https://support.vald.com/hc/en-au/articles/5001743573273-HumanTrak-Metrics-Neck-Displacement)). Restated: Footbase = midpoint of AnkleLeft and AnkleRight. Sign Not published.
- **Inputs and units:** Neck, AnkleLeft, and AnkleRight points. Unit Not published.
- **Variants:** Likely unsided. See the section note.
- **What changes the number:** VALD's example uses are Standing Posture and the Squat ([source](https://support.vald.com/hc/en-au/articles/5001743573273-HumanTrak-Metrics-Neck-Displacement)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001743573273-HumanTrak-Metrics-Neck-Displacement

#### `Neck Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the head tips forward, seen from the side.
- **Calculation:** VALD defines it as the angle between vertical and the head segment, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001735307545-HumanTrak-Metrics-Neck-Flexion)). Restated: Head segment = Head to Neck points. Vertical is 0°. Forward flexion is positive.
- **Inputs and units:** Head and Neck points. Degrees.
- **Variants:** See the section note. VALD's normative report describes cervical flexion and extension differently, as head inclination relative to the trunk line ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). The KB article measures against vertical. Which reference the exported value uses is Not published.
- **What changes the number:** v4.3.7 allowed Neck Flexion side-on to the camera ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). v4.3.11 added Manual Mode ([source](https://support.vald.com/hc/en-au/articles/61610313241113-HumanTrak-v4-3-11-Release-Notes-3-September-2026)). Neck tests stand 2 m from the camera. VALD's example uses are forward head position in Standing Posture and compensation during shoulder ROM ([source](https://support.vald.com/hc/en-au/articles/5001735307545-HumanTrak-Metrics-Neck-Flexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001735307545-HumanTrak-Metrics-Neck-Flexion, https://valdhealth.com/news/humantrak-health-normative-data-report, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Neck Lateral Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the head tips to the side, seen from the front.
- **Calculation:** VALD defines it as the angle between vertical and the head segment, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001742621337-HumanTrak-Metrics-Neck-Lateral-Flexion)). Restated: Head segment = Head to Neck. Vertical is 0°. Right lateral flexion is positive.
- **Inputs and units:** Head and Neck points. Degrees.
- **Variants:** See the section note. The normative report defines cervical lateral flexion as head inclination relative to the trunk line in the frontal plane ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). That differs from the KB's vertical reference. Which one the export uses is Not published.
- **What changes the number:** v4.3.7 changed zeroing for Neck Rotation and Lateral Flexion "to improve repeatability" ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). v4.3.9 moved these tests to the shared standing calibration ([source](https://support.vald.com/hc/en-au/articles/59474601544089-HumanTrak-v4-3-9-Release-Notes-7-July-2026)). Values before and after those versions may not compare. Manual threshold override exists since v4.2.8.
- **Sources:** https://support.vald.com/hc/en-au/articles/5001742621337-HumanTrak-Metrics-Neck-Lateral-Flexion, https://valdhealth.com/news/humantrak-health-normative-data-report, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://support.vald.com/hc/en-au/articles/59474601544089-HumanTrak-v4-3-9-Release-Notes-7-July-2026

#### `Pelvic Displacement` (unit Not published)

The block has these fields:

- **What it measures:** How far forward or back the base of the spine sits over the feet.
- **Calculation:** VALD defines it as the anterior-posterior distance between the SpineBase marker and the footbase ([source](https://support.vald.com/hc/en-au/articles/5001742287513-HumanTrak-Metrics-Pelvic-Displacement)). Restated: Footbase = midpoint of AnkleLeft and AnkleRight. Sign Not published.
- **Inputs and units:** SpineBase, AnkleLeft, and AnkleRight points. Unit Not published.
- **Variants:** Likely unsided. See the section note.
- **What changes the number:** VALD's example uses are Standing Posture and the Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001742287513-HumanTrak-Metrics-Pelvic-Displacement)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001742287513-HumanTrak-Metrics-Pelvic-Displacement

#### `Pelvic Lateral Tilt` (degrees)

The block has these fields:

- **What it measures:** How much one hip drops below the other, seen from the front.
- **Calculation:** VALD defines it as the angle between horizontal and the pelvis segment, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001750009881-HumanTrak-Metrics-Pelvic-Lateral-Tilt)). Restated: Pelvis = HipLeft to HipRight. Level is 0°. The article's sign rule is "Left hip drop = positive".
- **Inputs and units:** HipLeft and HipRight points. Degrees.
- **Variants:** See the section note. The sign is fixed to the left hip, so in a unilateral test a positive value means different things on each stance leg. A VALD case study uses "Peak pelvic lateral tilt" in the Single Leg Stand and "Peak spine and pelvic lateral tilt" in Standing Posture ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). Exact export names are Not published.
- **What changes the number:** Stance leg and hip abductor control. VALD's example uses are Standing Posture and the Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001750009881-HumanTrak-Metrics-Pelvic-Lateral-Tilt)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001750009881-HumanTrak-Metrics-Pelvic-Lateral-Tilt, https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

#### `Shoulder Abduction` (degrees)

The block has these fields:

- **What it measures:** How far the arm lifts out to the side, seen from the front.
- **Calculation:** VALD defines it as the angle between the lower trunk and upper arm segments, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001734346009-HumanTrak-Metrics-Shoulder-Abduction)). Restated: Lower Trunk = SpineMid to SpineBase. Upper Arm = Shoulder to Elbow. Arm straight down is 0°. Abduction is positive.
- **Inputs and units:** SpineMid, SpineBase, Shoulder, and Elbow points. Degrees.
- **Variants:** See the section note. The Shoulder Adduction test uses the same plane. Its sign is not stated. The normative report lists shoulder abduction and adduction with left-right comparison ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)).
- **What changes the number:** Trunk side lean. Because the reference is the lower trunk line, a side lean changes the angle; HumanTrak reports compensations ([source](https://valdhealth.com/products/humantrak)). Manual threshold override since v4.2.8 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001734346009-HumanTrak-Metrics-Shoulder-Abduction, https://valdhealth.com/news/humantrak-health-normative-data-report, https://valdhealth.com/products/humantrak

#### `Shoulder Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the arm lifts forward and up, seen from the side.
- **Calculation:** VALD defines it as the angle between the lower trunk and upper arm segments, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001663893913-HumanTrak-Metrics-Shoulder-Flexion)). Restated: Lower Trunk = SpineMid to SpineBase. Upper Arm = Shoulder to Elbow. Arm straight down is 0°. Flexion is positive.
- **Inputs and units:** SpineMid, SpineBase, Shoulder, and Elbow points. Degrees.
- **Variants:** See the section note. The normative report lists "Peak shoulder flexion", "Spine tilt at peak flexion", "Shoulder flexion range of motion", and "Shoulder flexion asymmetry" ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). Spine tilt and ROM have their own blocks below. The Shoulder Extension test uses the same plane. Its sign is not stated.
- **What changes the number:** Trunk lean. The test faces the camera ([source](https://support.vald.com/hc/en-au/articles/34234456047641-HumanTrak-Test-Protocol-Shoulder-Flexion)). Manual threshold override since v4.2.8.
- **Sources:** https://support.vald.com/hc/en-au/articles/5001663893913-HumanTrak-Metrics-Shoulder-Flexion, https://valdhealth.com/news/humantrak-health-normative-data-report, https://support.vald.com/hc/en-au/articles/34234456047641-HumanTrak-Test-Protocol-Shoulder-Flexion

#### `Shoulder Internal Rotation` (degrees)

The block has these fields:

- **What it measures:** How far the forearm rotates up or down from horizontal with the arm out to the side.
- **Calculation:** VALD defines it as the angle between horizontal and the forearm segment, in the sagittal plane, starting at 90° shoulder abduction and 90° elbow flexion ([source](https://support.vald.com/hc/en-au/articles/5001723768857-HumanTrak-Metrics-Shoulder-Internal-Rotation)). Restated: Forearm = Elbow to Wrist. A horizontal forearm is 0°. The article's sign rule is "External Rotation = positive". So internal rotation reads negative under this article.
- **Inputs and units:** Elbow and Wrist points. Degrees.
- **Variants:** See the section note. The same article covers internal and external rotation at 90° abduction. The Neutral tests (arm at the side) and Shoulder Arc of Motion start from different positions ([source](https://support.vald.com/hc/en-au/articles/42281046622617-HumanTrak-Test-Protocol-Shoulder-External-Rotation-Neutral)). Their angle definitions are Not published.
- **What changes the number:** Start position. Neutral and Arc of Motion tests need at least 20° for a rep ([source](https://support.vald.com/hc/en-au/articles/40183798516761-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-Neutral), [source](https://support.vald.com/hc/en-au/articles/42935518748953-HumanTrak-Test-Protocol-Shoulder-Arc-of-Motion)). The live overlay in Shoulder Internal Rotation - 90° tests shows only above 75° abduction (v4.2.7). Manual Mode exists for External Rotation - Neutral (v4.3.11) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001723768857-HumanTrak-Metrics-Shoulder-Internal-Rotation, https://support.vald.com/hc/en-au/articles/42281046622617-HumanTrak-Test-Protocol-Shoulder-External-Rotation-Neutral, https://support.vald.com/hc/en-au/articles/40183798516761-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-Neutral, https://support.vald.com/hc/en-au/articles/42935518748953-HumanTrak-Test-Protocol-Shoulder-Arc-of-Motion, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Sternum Displacement` (unit Not published)

The block has these fields:

- **What it measures:** How far forward or back the mid-chest sits over the feet.
- **Calculation:** VALD defines it as the anterior-posterior distance between the SpineMid marker and the footbase ([source](https://support.vald.com/hc/en-au/articles/5001703956633-HumanTrak-Metrics-Sternum-Displacement)). Restated: Footbase = midpoint of AnkleLeft and AnkleRight. Sign Not published.
- **Inputs and units:** SpineMid, AnkleLeft, and AnkleRight points. Unit Not published.
- **Variants:** Likely unsided. See the section note.
- **What changes the number:** VALD's example uses are Standing Posture and the Overhead Squat ([source](https://support.vald.com/hc/en-au/articles/5001703956633-HumanTrak-Metrics-Sternum-Displacement)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001703956633-HumanTrak-Metrics-Sternum-Displacement

#### `Thoracic Rotation` (degrees)

The block has these fields:

- **What it measures:** How much the shoulders twist relative to the hips, seen from above.
- **Calculation:** VALD defines it as the angle between the pelvis and shoulder segments, in the transverse plane ([source](https://support.vald.com/hc/en-au/articles/5001714406553-HumanTrak-Metrics-Thoracic-Rotation)). Restated: Pelvis = HipLeft to HipRight. Shoulder = ShoulderLeft to ShoulderRight. Lines parallel is 0°. Left shoulder forward is positive.
- **Inputs and units:** HipLeft, HipRight, ShoulderLeft, and ShoulderRight points. Degrees.
- **Variants:** See the section note. The Trunk Rotation tests report a "Spinal Rotation" metric. Whether it equals this angle is Not published. See its block below.
- **What changes the number:** Pelvic rotation, which the seated variant limits ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). VALD's example uses are Standing Posture and the Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/5001714406553-HumanTrak-Metrics-Thoracic-Rotation)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001714406553-HumanTrak-Metrics-Thoracic-Rotation, https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights

#### `Trunk Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the trunk leans forward from vertical, seen from the side.
- **Calculation:** VALD defines it as the angle between vertical and the trunk segment, in the sagittal plane ([source](https://support.vald.com/hc/en-au/articles/5001722481177-HumanTrak-Metrics-Trunk-Flexion)). Restated: Trunk = Neck to SpineBase. Vertical is 0°. Forward flexion is positive.
- **Inputs and units:** Neck and SpineBase points. Degrees.
- **Variants:** See the section note. The Trunk Extension test uses the same plane. Its sign is not stated. "Peak trunk flexion on landing" is a landing metric in the Broad Jump ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)). Its export name is Not published.
- **What changes the number:** Trunk Flexion and Extension tests are side-on to the camera since v4.1.2 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). v4.3.2 started uploading trunk and spine metrics for the Drop Jump to VALD Hub ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001722481177-HumanTrak-Metrics-Trunk-Flexion, https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Trunk Lateral Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the trunk leans to the side from vertical, seen from the front.
- **Calculation:** VALD defines it as the angle between vertical and the trunk segment, in the coronal plane ([source](https://support.vald.com/hc/en-au/articles/5001662862745-HumanTrak-Metrics-Trunk-Lateral-Flexion)). Restated: Trunk = Neck to SpineBase. Vertical is 0°. Right lateral tilt is positive.
- **Inputs and units:** Neck and SpineBase points. Degrees.
- **Variants:** See the section note. Since v4.1.0, left and right movements in trunk ROM tests can be done on their own ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). A case study uses "Peak spine and pelvic lateral tilt" in Standing Posture ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). Export name Not published.
- **What changes the number:** Leg bend during the test. The protocol says not to lift or bend the legs ([source](https://support.vald.com/hc/en-au/articles/25729073432217-HumanTrak-Test-Protocol-Trunk-Lateral-Flexion)).
- **Sources:** https://support.vald.com/hc/en-au/articles/5001662862745-HumanTrak-Metrics-Trunk-Lateral-Flexion, https://support.vald.com/hc/en-au/articles/25729073432217-HumanTrak-Test-Protocol-Trunk-Lateral-Flexion, https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

### Metrics by test type

The table lists, for each test, the metrics that a public source names for it. "KB example" means a KB metric article names the test in its example use. That is not a full list. For the full list per test, query `/v2/test-type/metrics` with your credentials. All the test protocols are listed in the HumanTrak test types article ([source](https://support.vald.com/hc/en-au/articles/5001637315225-HumanTrak-test-types)).

| Test | Setup and rep rule | Metrics named in public sources |
|---|---|---|
| Quiet Stand, Eyes Open or Closed ([protocol](https://support.vald.com/hc/en-au/articles/35644419568281-HumanTrak-Test-Protocol-Quiet-Stand)) | Faces camera. Timer. One rep per test. Duration and surface are set by the tester. | CoM 95% ellipse area, anteroposterior CoM excursion ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). |
| Tandem Stand, Eyes Open or Closed ([protocol](https://support.vald.com/hc/en-au/articles/35644475819033-HumanTrak-Test-Protocol-Tandem-Stand)) | Auto-detects the front leg. Timer. | CoM changes ([source](https://valdhealth.com/news/how-fighting-fit-increases-client-engagement-with-vald-technology)). Field names Not published. |
| Single Leg Stand, Eyes Open or Closed ([protocol](https://support.vald.com/hc/en-au/articles/35644465745433-HumanTrak-Test-Protocol-Single-Leg-Stand)) | Auto-detects the stance leg. Timer. | Peak pelvic lateral tilt ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). KB examples: Ankle Lateral Shift, Knee Deviation, Center of Mass. |
| Neck Flexion ([protocol](https://support.vald.com/hc/en-au/articles/25728748472857-HumanTrak-Test-Protocol-Neck-Flexion)) | Front or side-on. 2 m. Manual Mode. | Neck Flexion. |
| Neck Lateral Flexion ([protocol](https://support.vald.com/hc/en-au/articles/25728504625817-HumanTrak-Test-Protocol-Neck-Lateral-Flexion)) | Faces camera. | Neck Lateral Flexion. |
| Neck Rotation ([protocol](https://support.vald.com/hc/en-au/articles/25728643865369-HumanTrak-Test-Protocol-Neck-Rotation)) | Faces camera. | Neck rotation angle. Definition Not published. |
| Shoulder Flexion, Shoulder Extension ([protocol](https://support.vald.com/hc/en-au/articles/34234456047641-HumanTrak-Test-Protocol-Shoulder-Flexion), [protocol](https://support.vald.com/hc/en-au/articles/25722108164505-HumanTrak-Test-Protocol-Shoulder-Extension)) | Faces camera. One arm at a time. | Shoulder Flexion; peak shoulder flexion, spine tilt at peak flexion, shoulder flexion ROM, shoulder flexion asymmetry ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). KB examples: Neck Flexion, Neck Lateral Flexion as compensations. |
| Shoulder Abduction, Shoulder Adduction ([protocol](https://support.vald.com/hc/en-au/articles/25721948248857-HumanTrak-Test-Protocol-Shoulder-Abduction), [protocol](https://support.vald.com/hc/en-au/articles/34234043658521-HumanTrak-Test-Protocol-Shoulder-Adduction)) | Faces camera. One arm at a time. | Shoulder Abduction. KB examples: Neck Flexion, Neck Lateral Flexion as compensations. |
| Shoulder External Rotation - 90° Abduction, Shoulder Internal Rotation - 90° Abduction ([protocol](https://support.vald.com/hc/en-au/articles/25724783730585-HumanTrak-Test-Protocol-Shoulder-External-Rotation-90%C2%BA-Abduction), [protocol](https://support.vald.com/hc/en-au/articles/34234865780249-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-90%C2%BA-Abduction)) | Arm at 90° abduction, elbow at 90°. | Shoulder Internal Rotation (ER positive). |
| Shoulder External Rotation - Neutral, Shoulder Internal Rotation - Neutral ([protocol](https://support.vald.com/hc/en-au/articles/42281046622617-HumanTrak-Test-Protocol-Shoulder-External-Rotation-Neutral), [protocol](https://support.vald.com/hc/en-au/articles/40183798516761-HumanTrak-Test-Protocol-Shoulder-Internal-Rotation-Neutral)) | Arm at side, elbow at 90°. Rep needs 20°. | Rotation angle. Definition Not published. |
| Shoulder Arc of Motion ([protocol](https://support.vald.com/hc/en-au/articles/42935518748953-HumanTrak-Test-Protocol-Shoulder-Arc-of-Motion)) | Internal and external rotation in one test (v4.2.3). Rep needs 20° internal rotation. | Total arc ("shoulder total arc", [source](https://valdperformance.com/news/objective-testing-for-golf-performance)). Definition Not published. |
| Elbow Flexion - 90° Shoulder Abduction, Elbow Extension - 90° Shoulder Abduction ([protocol](https://support.vald.com/hc/en-au/articles/42281201301401-HumanTrak-Test-Protocol-Elbow-Flexion-90%C2%BA-Abduction), [protocol](https://support.vald.com/hc/en-au/articles/42281363737881-HumanTrak-Test-Protocol-Elbow-Extension-90%C2%BA-Abduction)) | Rep needs 110° flexion, or 70° flexion for extension. | Elbow Flexion. |
| Trunk Flexion, Trunk Extension ([protocol](https://support.vald.com/hc/en-au/articles/34235127642649-HumanTrak-Test-Protocol-Trunk-Flexion), [protocol](https://support.vald.com/hc/en-au/articles/25728883969561-HumanTrak-Test-Protocol-Trunk-Extension)) | Side-on. Reps have side `NotApplicable`. | Trunk Flexion. |
| Trunk Lateral Flexion ([protocol](https://support.vald.com/hc/en-au/articles/25729073432217-HumanTrak-Test-Protocol-Trunk-Lateral-Flexion)) | Faces camera. | Trunk Lateral Flexion. |
| Trunk Rotation - Standing, Trunk Rotation - Seated ([protocol](https://support.vald.com/hc/en-au/articles/25729213590937-HumanTrak-Test-Protocol-Trunk-Rotation-Standing), [protocol](https://support.vald.com/hc/en-au/articles/61731814975257-HumanTrak-Test-Protocol-Trunk-Rotation-Seated)) | Hands on hips. Seated limits pelvic rotation. | Spinal Rotation ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)), left versus right comparison ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). |
| Seated Hip Internal Rotation, Seated Hip External Rotation ([protocol](https://support.vald.com/hc/en-au/articles/35644408157337-HumanTrak-Test-Protocol-Seated-Hip-Internal-Rotation), [protocol](https://support.vald.com/hc/en-au/articles/35644410486297-HumanTrak-Test-Protocol-Seated-Hip-External-Rotation)) | Seated calibration. Rep needs 10°. Manual Mode. | Hip Internal Rotation. |
| Squat ([protocol](https://support.vald.com/hc/en-au/articles/25720609736473-HumanTrak-Test-Protocol-Squat)) | Calibration. Hands on hips. API code `TT_SQUAT-DL`. | Hip Flexion at Peak Knee Flexion, Ankle Dorsiflexion at Peak Knee Flexion, Pelvis Anterior Tilt at Peak Knee Flexion ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)); peak knee flexion, hip adduction at peak knee flexion ([source](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)); dynamic knee valgus ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). KB examples: Trunk Lateral Flexion, Trunk Flexion, Knee Translation, Neck Displacement, Knee Displacement, Hip Abduction, Knee Ankle Separation Ratio, Head Displacement. |
| Overhead Squat ([protocol](https://support.vald.com/hc/en-au/articles/25721626775833-HumanTrak-Test-Protocol-Overhead-Squat)) | Arms overhead. | Knee Ankle Separation Ratio (v4.3.2), "additional metrics" (v4.2.9) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)); dynamic knee valgus, peak hip and knee flexion ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). KB examples: Shoulder Flexion, Sternum Displacement, Shoulder Abduction, Elbow Flexion. |
| Single Leg Squat ([protocol](https://support.vald.com/hc/en-au/articles/25719992097433-HumanTrak-Test-Protocol-Single-Leg-Squat)) | Non-stance leg behind. | Dynamic knee valgus (v4.2.0) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)); peak hip and knee flexion ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). KB examples: Thoracic Rotation, Pelvic Displacement, Pelvic Lateral Tilt, Knee Valgus, Knee Deviation, Center of Mass. |
| Single Leg Pistol Squat ([protocol](https://support.vald.com/hc/en-au/articles/35644411765785-HumanTrak-Test-Protocol-Single-Leg-Pistol-Squat)) | Non-stance leg in front. Rep needs 30° knee flexion. | Knee Flexion. Others Not published. |
| Lunge ([protocol](https://support.vald.com/hc/en-au/articles/28827078860569-HumanTrak-Test-Protocol-Lunge)) | 3.5 m from camera. | Not published. |
| Weight Bearing Dorsiflexion ([protocol](https://support.vald.com/hc/en-au/articles/25725170876697-HumanTrak-Test-Protocol-Weight-Bearing-Dorsiflexion)) | 3 m from camera. | Knee over toe distance ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). KB example: Knee Translation. |
| Countermovement Jump ([protocol](https://support.vald.com/hc/en-au/articles/45825462652185-HumanTrak-Test-Protocol-Countermovement-Jump)) | Hands on hips. | Jump height, countermovement depth, full-body joint angles ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). |
| Single Leg Countermovement Jump ([protocol](https://support.vald.com/hc/en-au/articles/47342472997913-HumanTrak-Test-Protocol-Single-Leg-Countermovement-Jump)) | Rep needs 5 cm jump height. | Jump height. Others Not published. |
| Drop Jump ([protocol](https://support.vald.com/hc/en-au/articles/48742958655513-HumanTrak-Test-Protocol-Drop-Jump)) | Box. Rep resets after 3 s on the ground. | Jump height; trunk and spine metrics (v4.3.2). KB examples: Knee Translation, Knee Flexion, Knee Displacement, Ankle Plantarflexion, Body Tilt, Hip Flexion. |
| Single Leg Drop Jump ([protocol](https://support.vald.com/hc/en-au/articles/61732030982681-HumanTrak-Test-Protocol-Single-Leg-Drop-Jump)) | Box. Same leg lands and jumps. | Jump height; dynamic knee valgus on landing ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). |
| Broad Jump, Single Leg Broad Jump ([protocol](https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump), [protocol](https://support.vald.com/hc/en-au/articles/61731984065561-HumanTrak-Test-Protocol-Single-Leg-Broad-Jump)) | Side-on (within ±45°). **Start rep** button. | Jump distance, takeoff angle, peak trunk flexion on landing ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)). |
| Lateral Hop, Medial Hop ([protocol](https://support.vald.com/hc/en-au/articles/54247081906713-HumanTrak-Test-Protocol-Lateral-Hop), [protocol](https://support.vald.com/hc/en-au/articles/54396465481369-HumanTrak-Test-Protocol-Medial-Hop)) | Faces camera. **Start rep** button. | Not published. VALD describes them as frontal-plane power, control, and symmetry tests ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). |
| Single Leg Land and Hold ([protocol](https://support.vald.com/hc/en-au/articles/59475068735129-HumanTrak-Test-Protocol-Single-Leg-Land-and-Hold)) | Box. **Start Left Rep** or **Start Right Rep**. | Time to stability ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). |
| Single Leg Heel Raise - Endurance ([protocol](https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance)) | Side-on. Leg nearest the camera. To fatigue. | Rep count for the tested limb. Heel height threshold value Not published. |
| Sit to Stand - 30-second, Sit to Stand - 5-repetition, Sit to Stand - Functional ([protocol](https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second), [protocol](https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition), [protocol](https://support.vald.com/hc/en-au/articles/55422903619225-HumanTrak-Test-Protocol-Sit-to-Stand-Functional)) | Chair. Arms crossed. | Rep count. Time and quality metrics Not published. |
| Box Lift - Bench, Box Lift - Overhead ([protocol](https://support.vald.com/hc/en-au/articles/57350850787097-HumanTrak-Test-Protocol-Box-Lift-Bench), [protocol](https://support.vald.com/hc/en-au/articles/57350773616281-HumanTrak-Test-Protocol-Box-Lift-Overhead)) | Side-on. **Next weight** pauses for a box change. | Not published. |
| Standing Posture ([protocol](https://support.vald.com/hc/en-au/articles/31843457793817-HumanTrak-Test-Protocol-Standing-Posture)) | Front capture, then side-on capture. | Peak spine and pelvic lateral tilt, absolute motion of the CoM ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). KB examples: Trunk Lateral Flexion, Sternum Displacement, Thoracic Rotation, Trunk Flexion, Neck Flexion, Knee Flexion, Pelvic Displacement, Neck Lateral Flexion, Neck Displacement, Pelvic Lateral Tilt, Knee Valgus, Hip Abduction, Body Tilt, Head Displacement, Hip Flexion. |
| Anthropometry ([protocol](https://support.vald.com/hc/en-au/articles/61731955613465-HumanTrak-Test-Protocol-Anthropometry)) | Front capture with arms out (70 to 110° abduction), then side-on. | Standing height, wingspan, segment lengths ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). |
| Custom tests ([source](https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak)) | One or two snapshots, or Video mode (v4.3.8). | One or two user-named metrics. |

VALD Norms exist for many of these tests, by age and sex ([source](https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems)).

### Test-specific metrics

These metrics have no KB "HumanTrak Metrics" article. Each block uses only what a source states.

#### `Jump Height` (cm or in, per display setting)

The block has these fields:

- **What it measures:** How high the body rises in a vertical jump.
- **Calculation:** VALD defines jump height as the difference between standing and the apex of the jump ([source](https://support.vald.com/hc/en-au/articles/45825462652185-HumanTrak-Test-Protocol-Countermovement-Jump)). Restated: jump height = CoM height at the top of the jump - CoM height in quiet standing. The CoM basis comes from VALD's statement that horizontal jump analysis uses the same center-of-mass tracking as vertical jump analysis ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)).
- **Inputs and units:** CoM position over time and a standing baseline. The protocols give values in cm with inches ([source](https://support.vald.com/hc/en-au/articles/47342472997913-HumanTrak-Test-Protocol-Single-Leg-Countermovement-Jump)). Imperial display follows the org setting (v4.2.6).
- **Variants:** Countermovement Jump, Single Leg Countermovement Jump, Drop Jump, and Single Leg Drop Jump. Single-leg tests return per-side values. Export field name Not published.
- **What changes the number:** VALD says the HumanTrak method differs from force plates and gives jump height values "~10 cm (3.9 inches) higher" on average ([source](https://support.vald.com/hc/en-au/articles/48742958655513-HumanTrak-Test-Protocol-Drop-Jump)). Do not mix HumanTrak and force plate jump heights. A single-leg CMJ rep needs at least 5 cm ([source](https://support.vald.com/hc/en-au/articles/47342472997913-HumanTrak-Test-Protocol-Single-Leg-Countermovement-Jump)). Drop jump reps reset if 3 s pass between landing and jumping ([source](https://support.vald.com/hc/en-au/articles/48742958655513-HumanTrak-Test-Protocol-Drop-Jump)). Arm position (hands on hips) and calibration stance set the baseline.
- **Sources:** https://support.vald.com/hc/en-au/articles/45825462652185-HumanTrak-Test-Protocol-Countermovement-Jump, https://support.vald.com/hc/en-au/articles/47342472997913-HumanTrak-Test-Protocol-Single-Leg-Countermovement-Jump, https://support.vald.com/hc/en-au/articles/48742958655513-HumanTrak-Test-Protocol-Drop-Jump, https://support.vald.com/hc/en-au/articles/61732030982681-HumanTrak-Test-Protocol-Single-Leg-Drop-Jump, https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak

#### `Countermovement Depth` (unit Not published)

The block has these fields:

- **What it measures:** How far the body drops before a countermovement jump. Restated from the name only.
- **Calculation:** Not published. v4.2.6 lists it as a reported CMJ metric ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Inputs and units:** Not published.
- **Variants:** Not published.
- **What changes the number:** Not published. The broad jump tips ask for a CoM drop of at least 7 cm in the countermovement for rep detection ([source](https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump)). No source links that to this metric.
- **Sources:** https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Jump Distance` (cm or in, per display setting)

The block has these fields:

- **What it measures:** How far the body travels forward in a broad jump.
- **Calculation:** VALD defines it as the change in center of mass (CoM) position across the screen, in either direction ([source](https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump)). Restated: distance = horizontal CoM position at landing - horizontal CoM position at the start of the rep. The capture runs from quiet standing at the start of the rep until one second after landing ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)).
- **Inputs and units:** CoM position. VALD gives the offset in cm and inches.
- **Variants:** Broad Jump and Single Leg Broad Jump (leg nearest the camera) ([source](https://support.vald.com/hc/en-au/articles/61731984065561-HumanTrak-Test-Protocol-Single-Leg-Broad-Jump)). Export field name Not published.
- **What changes the number:** VALD says HumanTrak distance commonly reads 20-30cm (8-12in) longer than manual methods ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)). Manual methods measure toe at takeoff to heel at landing. The offset does not affect comparisons within HumanTrak. Rep detection needs a side-on stance (±45°), a still start, a clear countermovement, an explosive push, and a landing in view ([source](https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump)).
- **Sources:** https://support.vald.com/hc/en-au/articles/52592595165977-HumanTrak-Test-Protocol-Broad-Jump, https://support.vald.com/hc/en-au/articles/61731984065561-HumanTrak-Test-Protocol-Single-Leg-Broad-Jump, https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak

#### `Takeoff Angle` (degrees)

The block has these fields:

- **What it measures:** The launch direction of the body at takeoff in a broad jump.
- **Calculation:** VALD says the two CoM velocities are estimated from the CoM position in the final frames of ground contact ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)). Restated: takeoff angle = arctan(vertical CoM velocity / horizontal CoM velocity), measured from horizontal, just before the feet leave the ground. The number of frames used is Not published.
- **Inputs and units:** CoM horizontal and vertical velocity. Degrees.
- **Variants:** Broad Jump and Single Leg Broad Jump ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). Export field name Not published.
- **What changes the number:** Higher angles mean more vertical lift. Lower angles mean more forward projection. VALD says most trained athletes take off between 19° and 27° in standing broad jumps ([source](https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak)).
- **Sources:** https://valdperformance.com/news/understanding-horizontal-jump-analysis-in-humantrak, https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights

#### `Knee Over Toe Distance` (unit Not published)

The block has these fields:

- **What it measures:** How far the knee travels past the toes in the Weight Bearing Dorsiflexion test. Restated from the name.
- **Calculation:** Not published. v4.1.2 improved rep detection so that knee over toe distances are captured accurately ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). v4.2.6 lists it among distance metrics with imperial display.
- **Inputs and units:** Not published.
- **Variants:** Per leg, since the test is done on each leg ([source](https://support.vald.com/hc/en-au/articles/25725170876697-HumanTrak-Test-Protocol-Weight-Bearing-Dorsiflexion)). Export name Not published.
- **What changes the number:** The test stands 3 m from the camera. Before v4.1.2, rep detection failed when the knee did not cross the foot ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://support.vald.com/hc/en-au/articles/25725170876697-HumanTrak-Test-Protocol-Weight-Bearing-Dorsiflexion

#### `Spinal Rotation` (unit Not published)

The block has these fields:

- **What it measures:** Rotation of the spine relative to the pelvis in the Trunk Rotation tests.
- **Calculation:** Not published. v4.1.0 added "Spinal Rotation". v4.1.1 added "spinal rotation with respect to pelvis" to isolate spinal rotation ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Whether these are one metric, and whether either equals `Thoracic Rotation`, is Not published.
- **Inputs and units:** Not published.
- **Variants:** Left and right rotation. Seated and Standing tests (v4.3.11) ([source](https://support.vald.com/hc/en-au/articles/61610313241113-HumanTrak-v4-3-11-Release-Notes-3-September-2026)).
- **What changes the number:** Pelvic rotation. The seated test restricts it and reduces compensation ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). Seated and standing results are separate tests and should not be mixed.
- **Sources:** https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights

#### `Dynamic Knee Valgus` (degrees)

The block has these fields:

- **What it measures:** The knee's front-plane angle at the bottom of a single leg squat.
- **Calculation:** Not published as a formula. v4.2.0 added it for the Single Leg Squat ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). A VALD case study used the peak frontal-plane knee angle at peak knee flexion as its single leg squat variable ([source](https://valdhealth.com/news/seasonal-kinematic-profiling-in-female-high-school-athletics)). Restated: likely the `Knee Valgus` angle read at peak knee flexion, but VALD does not confirm it. The `Knee Valgus` article makes varus positive ([source](https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus)). The case study reports "4-5° of dynamic knee valgus", which reads as valgus positive. The sign of the export is Not published.
- **Inputs and units:** Hip, Knee, and Ankle points. Degrees.
- **Variants:** Per leg. Also named for the Squat, Overhead Squat ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)), and Single Leg Drop Jump landing ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). Export names Not published.
- **What changes the number:** Squat depth and foot position. VALD cautions that knee valgus should not be read as a standalone injury predictor ([source](https://valdhealth.com/news/seasonal-kinematic-profiling-in-female-high-school-athletics)).
- **Sources:** https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://valdhealth.com/news/seasonal-kinematic-profiling-in-female-high-school-athletics, https://support.vald.com/hc/en-au/articles/5001752396057-HumanTrak-Metrics-Knee-Valgus

#### `Hip Flexion at Peak Knee Flexion` (degrees; API `MG_SQUAT-DL_HIP-FLEX-AT-KNEE-FLEX-PEAK`)

The block has these fields:

- **What it measures:** Hip flexion at the moment the knee is most bent in a squat.
- **Calculation:** Restated from the name and the `Hip Flexion` article: the hip flexion angle (lower trunk to femur, sagittal plane) sampled at the frame of peak knee flexion ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API), [source](https://support.vald.com/hc/en-au/articles/5001801306393-HumanTrak-Metrics-Hip-Flexion)). Whether peak knee flexion is taken per side is Not published.
- **Inputs and units:** `"Degrees"` in the KB example.
- **Variants:** Left and right `summaryMeasurements` with `max`, `min`, and `avg`, plus `asymmetryMeasurement` in `"Percent"`. `shortName` "Hip Flexion", `classification` "Secondary", `trendSentiment` "Negative" ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- **What changes the number:** Squat depth and trunk lean. VALD says it commonly reaches 105 to 120° in full-depth squats ([source](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)). A case study used it with rep count as a proxy for hip strength-endurance ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)).
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics, https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

#### `Peak Knee Flexion` (degrees)

The block has these fields:

- **What it measures:** The most the knee bends in a squat rep.
- **Calculation:** Restated: the largest `Knee Flexion` value in the rep ([source](https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion)). VALD lists it as a HumanTrak squat metric with limb symmetry options and says it commonly reaches 110 to 130° in full-depth squats ([source](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)).
- **Inputs and units:** Hip, Knee, and Ankle points. Degrees.
- **Variants:** Per leg. Squat, Overhead Squat, and Single Leg Squat ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). Export name Not published.
- **What changes the number:** It picks the in-app "best rep" for Squat and Overhead Squat (v4.2.8) ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). It also sets the time point for every "at Peak Knee Flexion" metric.
- **Sources:** https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics, https://support.vald.com/hc/en-au/articles/5001738748313-HumanTrak-Metrics-Knee-Flexion, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Hip Adduction at Peak Knee Flexion` (degrees)

The block has these fields:

- **What it measures:** How far the thigh moves in toward the midline at the bottom of a squat.
- **Calculation:** Not published as a formula. VALD describes the metric as the maximum frontal plane range of motion that each hip reaches ([source](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)). The `Hip Abduction` article defines the same plane with abduction positive ([source](https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction)). The adduction sign is Not published.
- **Inputs and units:** Knee, HipLeft, and HipRight points. Degrees.
- **Variants:** Per leg, with limb symmetry options. Export name Not published.
- **What changes the number:** v4.2.0 fixed the polarity of hip adduction metrics ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)). Do not compare signs across that version.
- **Sources:** https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics, https://support.vald.com/hc/en-au/articles/5001760871193-HumanTrak-Metrics-Hip-Abduction, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Ankle Dorsiflexion at Peak Knee Flexion` (degrees; API `MG_SQUAT-DL_ANKLE-DORSIFLEXION-AT-PEAK-KNEE-FLEXION`)

The block has these fields:

- **What it measures:** Ankle bend at the bottom of a squat.
- **Calculation:** Not published. The API example shows it as sided, with `leftValue` 11.11 and `rightValue` 13.89 for one rep ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)). The `Ankle Plantarflexion` article puts neutral at 90° with dorsiflexion positive ([source](https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion)). The example values suggest a 0° neutral instead, but the zero point is Not published.
- **Inputs and units:** Foot, Ankle, and Knee points. Unit not returned on the reps endpoint.
- **Variants:** Per leg. Summary aggregates and asymmetry presumably as for other sided groups.
- **What changes the number:** Heel contact and squat depth.
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://support.vald.com/hc/en-au/articles/5001778777881-HumanTrak-Metrics-Ankle-Plantarflexion

#### `Pelvis Anterior Tilt at Peak Knee Flexion` (unit Not published; API `MG_SQUAT-DL_PELVIS-ANTERIOR-TILT-AT-KNEE-FLEX-PEAK`)

The block has these fields:

- **What it measures:** Forward tilt of the pelvis at the bottom of a squat. Restated from the name.
- **Calculation:** Not published. No KB metric article defines pelvic anterior tilt. The API example shows it as unsided, `unsidedValue` 22.22 ([source](https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API)).
- **Inputs and units:** Not published.
- **Variants:** Unsided, so no asymmetry. A case study uses "pelvic tilt ROM" in the Squat ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). Whether that is a separate field is Not published.
- **What changes the number:** Not published.
- **Sources:** https://support.vald.com/hc/en-au/articles/29352184061849-A-guide-to-using-the-External-HumanTrak-API, https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

#### `Spine Tilt at Peak Flexion` (unit Not published)

The block has these fields:

- **What it measures:** Trunk lean at the top of a shoulder flexion rep. Restated from the name.
- **Calculation:** Not published. Listed in the shoulder flexion and extension normative report ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). The product page says HumanTrak shows compensations, such as gaining range by leaning ([source](https://valdhealth.com/products/humantrak)).
- **Inputs and units:** Not published.
- **Variants:** Not published.
- **What changes the number:** Not published.
- **Sources:** https://valdhealth.com/news/humantrak-health-normative-data-report, https://valdhealth.com/products/humantrak

#### `Shoulder Flexion Range of Motion` (degrees)

The block has these fields:

- **What it measures:** The range of shoulder motion in the flexion test.
- **Calculation:** Not published. Listed beside "Peak shoulder flexion" in the normative report ([source](https://valdhealth.com/news/humantrak-health-normative-data-report)). Whether ROM differs from peak, for example peak minus start angle, is Not published.
- **Inputs and units:** Shoulder flexion angle. Degrees.
- **Variants:** Per arm. "Shoulder flexion asymmetry" is listed with it.
- **What changes the number:** Not published beyond the `Shoulder Flexion` factors.
- **Sources:** https://valdhealth.com/news/humantrak-health-normative-data-report

#### `Neck Rotation` (unit Not published)

The block has these fields:

- **What it measures:** How far the head turns left or right.
- **Calculation:** Not published. No KB metric article covers neck rotation. The test is in the library and has norms ([source](https://support.vald.com/hc/en-au/articles/5001637315225-HumanTrak-test-types), [source](https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems)).
- **Inputs and units:** Not published.
- **Variants:** Left and right turns in one test ([source](https://support.vald.com/hc/en-au/articles/25728643865369-HumanTrak-Test-Protocol-Neck-Rotation)).
- **What changes the number:** Zeroing changed in v4.3.7. Calibration changed in v4.3.9. Manual threshold override since v4.2.8 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/25728643865369-HumanTrak-Test-Protocol-Neck-Rotation, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

#### `Center of Mass 95% Ellipse Area` (unit Not published)

The block has these fields:

- **What it measures:** The size of the area the CoM sways within during a balance stand. Restated from the name.
- **Calculation:** Not published. A VALD case study lists it for the Quiet Stand ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). Restated from common use of the term, not taken from a VALD statement: an ellipse that holds 95% of CoM positions. The plane, method, and unit are Not published.
- **Inputs and units:** CoM over time. Unit Not published.
- **Variants:** Not published.
- **What changes the number:** Test duration (options include 45 s and 60 s since v4.2.1), surface condition, eyes open or closed ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)), and foot position. Keep the instructions the same each time ([source](https://support.vald.com/hc/en-au/articles/35644419568281-HumanTrak-Test-Protocol-Quiet-Stand)).
- **Sources:** https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes, https://support.vald.com/hc/en-au/articles/35644419568281-HumanTrak-Test-Protocol-Quiet-Stand

#### `Anteroposterior Center of Mass Excursion` (unit Not published)

The block has these fields:

- **What it measures:** Forward-back CoM movement during a balance stand. Restated from the name.
- **Calculation:** Not published. Listed for the Quiet Stand in a VALD case study ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)). Whether it is path length or range is Not published.
- **Inputs and units:** CoM over time. Unit Not published.
- **Variants:** A medial-lateral version is not named in any source.
- **What changes the number:** As for the ellipse area. If it is a path length, it grows with test duration. That is not confirmed.
- **Sources:** https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

#### `Absolute Motion of the Center of Mass` (unit Not published)

The block has these fields:

- **What it measures:** Total CoM movement during Standing Posture. Restated from the name.
- **Calculation:** Not published. Listed for a 5-second Standing Posture test in a VALD case study ([source](https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case)).
- **Inputs and units:** CoM over time. Unit Not published.
- **Variants:** Not published.
- **What changes the number:** Capture duration.
- **Sources:** https://valdhealth.com/news/hip-replacement-rehab-with-humantrak-use-case

#### `Time to Stability` (unit Not published)

The block has these fields:

- **What it measures:** How long it takes to settle after a single leg landing. Restated from the name.
- **Calculation:** Not published. VALD lists the Single Leg Land and Hold with "(time to stability)" ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)). The stability threshold is Not published.
- **Inputs and units:** Not published.
- **Variants:** Per landing leg, chosen with **Start Left Rep** or **Start Right Rep** ([source](https://support.vald.com/hc/en-au/articles/59475068735129-HumanTrak-Test-Protocol-Single-Leg-Land-and-Hold)).
- **What changes the number:** Box height. The protocol does not set it.
- **Sources:** https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights, https://support.vald.com/hc/en-au/articles/59475068735129-HumanTrak-Test-Protocol-Single-Leg-Land-and-Hold

#### Sit to Stand outputs (rep count; time Not published)

The block has these fields:

- **What it measures:** Sit to Stand - 30-second counts reps in 30 s. Sit to Stand - 5-repetition aims to finish five reps as fast as possible and ends after five reps. Sit to Stand - Functional records a chosen number of reps ([source](https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second), [source](https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition), [source](https://support.vald.com/hc/en-au/articles/55422903619225-HumanTrak-Test-Protocol-Sit-to-Stand-Functional)).
- **Calculation:** Rep count: VALD says a rep counts each time the person completes a full stand and returns to a seated position ([source](https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition)). A HumanTrak time-to-complete field and any joint-angle fields for these tests are Not published. VALD's general sit-to-stand article describes the standard stopwatch scoring, not HumanTrak fields ([source](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness)).
- **Inputs and units:** Reps. Time unit Not published.
- **Variants:** `repetitionCounts[].count`. Other names Not published.
- **What changes the number:** Full hip and knee extension when standing and full chair contact when seated are needed for detection. Arms stay crossed. The 30-second test starts on **Start test** ([source](https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second)). Chair height is not set in the protocols.
- **Sources:** https://support.vald.com/hc/en-au/articles/55421266131609-HumanTrak-Test-Protocol-Sit-to-Stand-30-second, https://support.vald.com/hc/en-au/articles/55422685895961-HumanTrak-Test-Protocol-Sit-to-Stand-5-repetition, https://support.vald.com/hc/en-au/articles/55422903619225-HumanTrak-Test-Protocol-Sit-to-Stand-Functional

#### Single Leg Heel Raise - Endurance outputs (rep count)

The block has these fields:

- **What it measures:** The number of single leg heel raises to fatigue or technique failure ([source](https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance)).
- **Calculation:** Restated: a rep counts when the heel rises past a height threshold and returns to the ground under control. The threshold value is Not published. Heel height as an exported field is Not published.
- **Inputs and units:** Reps.
- **Variants:** Per leg. Repeat on the other side by turning to face the other way.
- **What changes the number:** Pacing (a metronome is optional), wall support (fingertips only), knee bend, and calibration. Each rep needs a short still period first ([source](https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance)).
- **Sources:** https://support.vald.com/hc/en-au/articles/60333537162265-HumanTrak-Test-Protocol-Single-Leg-Heel-Raise-Endurance

#### Anthropometry outputs: standing height, wingspan, segment lengths (unit Not published)

The block has these fields:

- **What it measures:** Body dimensions from two still captures ([source](https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights)).
- **Calculation:** Not published. Field names and the segment list are Not published.
- **Inputs and units:** A front capture with arms out and a side-on capture. Both shoulders must be at 70 to 110° abduction for the first capture ([source](https://support.vald.com/hc/en-au/articles/61731955613465-HumanTrak-Test-Protocol-Anthropometry)).
- **Variants:** Not published.
- **What changes the number:** Arm height and stance. VALD Hub profiles no longer hold anthropometry fields (2024 Hub release notes), which is separate from this test ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Sources:** https://valdhealth.com/news/whats-new-in-humantrak-more-tests-smarter-workflows-and-better-insights, https://support.vald.com/hc/en-au/articles/61731955613465-HumanTrak-Test-Protocol-Anthropometry

#### Custom test metrics (degrees, centimeters, or None)

The block has these fields:

- **What it measures:** One or two user-named values per custom test ([source](https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak)).
- **Calculation:** The practitioner enters the value or measures it on a snapshot. For on-image lengths, VALD says HumanTrak computes the straight-line distance in pixels and then converts it to centimeters ([source](https://support.vald.com/hc/en-au/articles/52152503473561-Record-custom-measurements-with-HumanTrak)). Restated: it places a flat plane at the depth of the selected limb, or the CoM if no body part is set, and scales pixels using field of view and depth. Angles use three points placed by the user.
- **Inputs and units:** Degrees, centimeters, or None. Imperial units allowed since v4.3.2 ([source](https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes)).
- **Variants:** Snapshot mode or Video mode (**Test now, measure later**, v4.3.8). After saving, the test type and metric details cannot change. Names can ([source](https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak)). How custom metrics appear in the API is Not published.
- **What changes the number:** Only vertical and horizontal lengths are supported, not forward-back. Points at different depths give over- or underestimates. Moving or tilting the camera breaks scaling. Choosing the wrong limb sets the wrong depth ([source](https://support.vald.com/hc/en-au/articles/52152503473561-Record-custom-measurements-with-HumanTrak)).
- **Sources:** https://support.vald.com/hc/en-au/articles/50988971004441-Create-and-run-a-custom-test-in-HumanTrak, https://support.vald.com/hc/en-au/articles/52152503473561-Record-custom-measurements-with-HumanTrak, https://support.vald.com/hc/en-au/articles/34319770485785-HumanTrak-Release-Notes

### Details not published

The public sources checked do not publish these details:

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

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
