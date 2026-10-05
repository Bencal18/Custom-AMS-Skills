# VALD ForceFrame metrics

ForceFrame is a VALD isometric strength device. The athlete pushes or pulls against padded load cells mounted on a crossbar, and the software reports force, asymmetry, rate of force development, impulse, and training results. This page covers the test metrics, the training metrics, the reference points in the app and VALD Hub, and the fields of the External ForceFrame API. Checked against: the VALD knowledge base (support.vald.com), the ForceFrame Testing Guide PDF, the Max V7, Fold, and Max V6 spec sheets, the ForceFrame iOS release notes (through v3.0.0, 2025-09-29), the ForceFrame Windows release notes, the VALD Hub release notes, the External ForceFrame API OpenAPI spec (`swagger/v1`), the VALD RFD cheat sheet, VALD education pages on valdhealth.com and valdperformance.com, and the `valdr` R package 4.0.0, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

This page is part of [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](README.md). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](../vald-forcedecks-nordbord/README.md).

## How to read this page

Each metric block names the exact field or Hub name and then lists the following items:

- **What it measures.**
- **Calculation:** VALD's definition in paraphrase, then the formula in plain math where a source gives one.
- **Inputs and units.**
- **Variants.**
- **Comparison with standard methods or other vendors**, only where a source supports it.
- **What changes the number.**
- **Sources:** full public links.

A formula labeled Restated is this page's plain restatement, not the vendor's statement. A calculation or detail marked Not published is one that the vendor does not publish in the public sources checked. It does not mean the vendor lacks the information. None of the VALD OpenAPI specs carry field descriptions, so definitions come from the VALD knowledge base, VALD education pages, and the `valdr` R package.

## ForceFrame

### Overview

The overview covers the device, its sensors, its sampling rate, its export routes, the row level of each export, the left and right labels, and the test types. It has these items:

- **What the device measures:** VALD says ForceFrame measures the force applied through its sensors ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). The Testing Guide says it measures isometric strength and asymmetry ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). Restated: the athlete pushes or pulls against padded load cells (paddles) mounted on a crossbar. The frame has two inner paddles and two outer paddles, one of each on the left and the right ([source](https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame)). The six-sensor ForceFrame Max adds two sensors for sagittal-plane movements such as flexion and extension ([source](https://valdhealth.com/news/the-history-and-future-of-forceframe)). Its spec sheet calls them "Upper sensor" ([source](https://support.vald.com/hc/en-au/article_attachments/62749147143449)).
- **Sensor behavior:** VALD describes the sensors as uniaxial, designed to read forces perpendicular to their Force Pads ([source](https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work)). Restated: only the part of the force that is perpendicular to the pad is measured.
- **Sampling rate:** All three spec sheets list a sampling rate of 50 Hz (default) up to 400 Hz ([Max V7](https://support.vald.com/hc/en-au/article_attachments/62749147143449), [Fold](https://support.vald.com/hc/en-au/article_attachments/25314373779993), [Max V6](https://support.vald.com/hc/en-au/article_attachments/25314362844569)). The ForceFrame iOS v3.0.0 release notes (2025-09-29) say that VALD raised the sampling frequency to 400 Hz to capture new metrics. It is adjustable in **Settings** on the testing screen ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). A VALD education article lists ForceFrame at 400Hz ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). The release note does not say that 400 Hz is the new default, and the spec sheets list 50 Hz as the default. Check the setting on your device.
- **Resolution and capacity:** Resolution is 1 N on all three spec sheets ([source](https://support.vald.com/hc/en-au/article_attachments/62749147143449)). Inner paddles hold 1000 N. Outer paddles hold 1000 N or 2500 N depending on the model ([source](https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame)). Spec sheets list inner 1,000 N and outer 2,500 N, and upper 2,500 N on the Max V7 ([source](https://support.vald.com/hc/en-au/article_attachments/62749147143449)).
- **Export routes:**
  - **VALD Hub CSV (tests):** **Dashboard** > **Results Export** > **ForceFrame** tab, select tests, then **Export** ([steps](https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub), [ForceFrame steps](https://support.vald.com/hc/en-au/articles/4998152248345-Export-ForceFrame-Results)). Since 2026-03-26, exports from **VALD Systems** > **ForceFrame** can include rep data ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). The CSV column names: Not published.
  - **VALD Hub CSV (force trace):** **Profiles** > profile > **Results Table** > test > **Export Force Trace**. One CSV per test ([source](https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub)). Column names: Not published.
  - **VALD Hub CSV (training):** **Dashboard** > **Results Export** > **ForceFrame** > **Training** tab, select sessions, then **Export** ([source](https://support.vald.com/hc/en-au/articles/4799421027993-View-Training-Data-in-VALD-Hub)). Since 2024-10-17 the export shows Exercise Type, Reps Completed, Time in Zone (%), Impulse (N s), and Variance (%) ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
  - **API:** External ForceFrame API, OAuth2 client credentials flow (declared in the `securitySchemes` of the [spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). Use the base URL for the tenant's region: `prd-aue-`, `prd-use-`, or `prd-euw-api-externalforceframe.valdperformance.com` ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). The endpoints are:
    - `GET /tests/v2`: test summaries (`GetTestSummaryResponseV2`) modified after `ModifiedFromUtc`, optional `ProfileId`. VALD recommends this route. Page by passing the last record's `modifiedDateUtc` as the next `ModifiedFromUtc` until you get 204 ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API), [spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /tests`: paged test summaries (`GetTestSummaryResponse`) by `TestFromUtc` and `TestToUtc` (six months maximum), `Page`, `PageSize` (max 100). VALD marks it "Planned for deprecation" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
    - `GET /tests/{testId}`: one test summary (`GetTestSummaryResponse`) ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
    - `GET /tests/{testId}/metrics`: per kg, RFD, RFD at 50 to 250 ms, and impulse at 50 to 250 ms as Max and Avg, and time to max force as Min and Avg, per sensor (`GetTestSummaryAdditionalMetricsResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /tests/{testId}/repetitions`: one row per rep per sensor (`GetTestRepetitionsResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /tests/{testId}/forceframetrace`: the raw force trace, one `Force` sample per tick for the four sensors (`GetTraceResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /training/programs/current`: training programs and their prescribed exercises; pass `Id` for one program ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /training/sessions`: training sessions with left and right time in zone, stability, and impulse ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /training/sessions/exercises`: one row per exercise performed in a session ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
    - `GET /training/sessions/exercises/repetitions`: one row per training rep ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
  - **valdr 4.0.0:** `get_forceframe_data()` (profiles plus tests), `get_forceframe_tests_only()`, `get_forceframe_test_by_id(test_id)`, and `get_forceframe_repetitions_by_id(test_id)` ([session.R](https://github.com/cran/valdr/blob/master/R/session.R), [KB](https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package)). `valdr` calls `/tests/v2`, `/tests/{testId}`, and `/tests/{testId}/repetitions` only. It has no function for `/metrics`, `/forceframetrace`, or the training endpoints ([forceframe_tests.R](https://github.com/cran/valdr/blob/master/R/forceframe_tests.R), [utils.R](https://github.com/cran/valdr/blob/master/R/utils.R)). `valdr` fills one `profileId` column from `profileId` or `athleteId`, whichever the endpoint returns ([utils.R](https://github.com/cran/valdr/blob/master/R/utils.R)).
  - **Other routes:** VALD Connect for Power BI (beta) lists ForceFrame as supported ([source](https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI)). VALD AI (beta) does not support repetition-level or force trace data ([source](https://support.vald.com/hc/en-au/articles/56075934514585-Using-VALD-AI-for-data-analysis)).
- **Row level:** The table shows what one row is in each export:

| Export | One row is |
|---|---|
| `/tests`, `/tests/v2`, `/tests/{testId}`, `valdr` test functions | One test. All four sensors are columns. |
| `/tests/{testId}/metrics` | One test. All four sensors are columns. |
| `/tests/{testId}/repetitions`, `get_forceframe_repetitions_by_id()` | One rep on one sensor (`sensorType` + `repNumber`). |
| `/tests/{testId}/forceframetrace` | One test. `forces` is an array with one element per sample. |
| `/training/programs/current` | One program. `exercises` is an array with one element per prescribed exercise. |
| `/training/sessions` | One training session. |
| `/training/sessions/exercises` | One exercise within a session. |
| `/training/sessions/exercises/repetitions` | One training rep. |
| Hub test CSV, trace CSV, training CSV | Not published. |

- **Left and right labels:** The labels differ by endpoint:
  - Test summary, `/metrics`, and trace fields use a prefix: `innerLeft`, `innerRight`, `outerLeft`, `outerRight` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
  - Repetitions use the `sensorType` enum: `InnerLeft`, `InnerRight`, `OuterLeft`, `OuterRight`, `FlatLeft`, `FlatRight` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). The `Flat` values have no matching columns in the summary, `/metrics`, or trace schemas. Which physical paddle a `Flat` value maps to: Not published.
  - Training fields use a `Left` or `Right` suffix (`timeInZoneLeft`) and have no inner or outer split ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
  - The app trace shows left in blue and right in orange. Its legend marks negative values (below 0 N) as force on the inner sensors and positive values (above 0 N) as force on the outer sensors ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). Whether the API trace uses the same sign: Not published.
  - Which movement loads the inner or the outer paddles in each test (for example, adduction versus abduction): Not published.
- **Test types:** The KB protocols list these tests and positions:
  - Hip Adduction / Abduction: 45º, 60º, 90º, Seated, Standing Ankle, Standing Knee, Supine Ankle, Supine Knee ([source](https://support.vald.com/hc/en-au/articles/4998486609817-ForceFrame-Test-Protocol-Hip-Abduction-Adduction)).
  - Hip Flexion: Kicker, Prone, Seated, Standing, Supine ([source](https://support.vald.com/hc/en-au/articles/4998398932377-ForceFrame-Test-Protocol-Hip-Flexion)). Hip Extension: Prone, Standing ([source](https://support.vald.com/hc/en-au/articles/4998462834457-ForceFrame-Test-Protocol-Hip-Extension)). Hip Internal / External Rotation: Prone, Supine ([source](https://support.vald.com/hc/en-au/articles/4998398037657-ForceFrame-Test-Protocol-Hip-Internal-External-Rotation)).
  - Knee Flexion: Prone, Standing, Supine ([source](https://support.vald.com/hc/en-au/articles/4998376807705-ForceFrame-Test-Protocol-Knee-Flexion)). Knee Extension: Standing, Seated 10⁰, Seated 45⁰, Seated 90⁰, Supine 10⁰, Supine 45⁰, Supine 90⁰ ([source](https://support.vald.com/hc/en-au/articles/12962592988953-ForceFrame-Test-Protocol-Knee-Extension)).
  - Ankle Dorsiflexion: Seated ([source](https://support.vald.com/hc/en-au/articles/4998507355417-ForceFrame-Test-Protocol-Ankle-Dorsiflexion)). Ankle Plantar Flexion: Seated, Supine ([source](https://support.vald.com/hc/en-au/articles/12960659718809-ForceFrame-Test-Protocol-Ankle-Plantar-Flexion)). Ankle Inversion / Eversion: Supine ([source](https://support.vald.com/hc/en-au/articles/4998488417433-ForceFrame-Test-Protocol-Ankle-Inversion-Eversion)).
  - Shoulder Internal / External Rotation: Supine, Supine with 90º abduction ([source](https://support.vald.com/hc/en-au/articles/4998364117273-ForceFrame-Test-Protocol-Shoulder-Internal-External-Rotation)). Shoulder Abduction / Adduction: Side Lying ([source](https://support.vald.com/hc/en-au/articles/4998379282457-ForceFrame-Test-Protocol-Shoulder-Abduction-Adduction)). Shoulder Flexion ([source](https://support.vald.com/hc/en-au/articles/4998329413529-ForceFrame-Test-Protocol-Shoulder-Flexion)). Shoulder Extension ([source](https://support.vald.com/hc/en-au/articles/4998322753689-ForceFrame-Test-Protocol-Shoulder-Extension)).
  - Elbow Flexion: Seated ([source](https://support.vald.com/hc/en-au/articles/4998479418137-ForceFrame-Test-Protocol-Elbow-Flexion)). Elbow Extension: Seated ([source](https://support.vald.com/hc/en-au/articles/4998519702681-ForceFrame-Test-Protocol-Elbow-Extension)).
  - Neck Extension, Neck Flexion, and Neck Lateral Flexion: Quadruped ([source](https://support.vald.com/hc/en-au/articles/4998344479129-ForceFrame-Test-Protocol-Neck)).
  - Custom test types, built in ForceFrame Windows with inner, outer, or both paddles active ([source](https://support.vald.com/hc/en-au/articles/4998193046425-Create-Custom-ForceFrame-Test-Types)).
  - The API `Joint` enum also lists `Hamstring`, `Dyno`, and `Custom` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). A Dyno test type exists in the apps ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). Neither has a published protocol.

### Peak and average force

#### `innerLeftMaxForce`, `innerRightMaxForce`, `outerLeftMaxForce`, `outerRightMaxForce` (N)

The block has these fields:

- **What it measures:** The highest force recorded on one sensor during the test. The app and Hub call it "Peak force". Protocols show it as "Max Force Left [N]" and "Max Force Right [N]".
- **Calculation:** VALD defines it as the maximum force produced during a test ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Restated: `MaxForce` = the highest force sample on that sensor across the included reps. VALD also says that once force exceeds the rep threshold, ForceFrame starts looking for a peak ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS)). The exact peak-picking rule beyond that: Not published.
- **Inputs and units:** Force from each load cell in newtons ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). The spec gives `number double` with no unit ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** The four sensor fields above. Rep level: `maxForce` on `/tests/{testId}/repetitions`, one value per `sensorType` and `repNumber` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). Relative: see `innerLeftMaxForcePerKg` and the other per kg fields. Left versus right: see **Imbalance**. Inner versus outer: see **Strength ratio**. Hub quadrant charts can show a "Bilateral average" laterality for ForceFrame ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). How Hub computes it: Not published.
- **What changes the number:**
  - Zeroing. The frame zeroes at startup; keep the pads clear for 3 seconds. An unzeroed sensor shows a positive or negative offset ([source](https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work)).
  - Force direction. Force that is not perpendicular to the pad is only partly measured ([source](https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work)).
  - Capacity. Accuracy can drop above the rated capacity. Deselect those reps and ForceFrame recalculates all metrics from the remaining reps ([source](https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame)).
  - Rep selection. Deleted or deselected reps are excluded before upload ([source](https://support.vald.com/hc/en-au/articles/26094908032537-Delete-reps-in-ForceFrame-iOS), [source](https://support.vald.com/hc/en-au/articles/4998047089305-Run-a-ForceFrame-Test)). Hub can delete reps after upload since 2026-06-16 ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
  - Position and setup. Each protocol sets crossbar rotation and body position. Paddle position is fixed in some protocols and "Per individual setup" in others, such as hip adduction / abduction ([source](https://support.vald.com/hc/en-au/articles/4998486609817-ForceFrame-Test-Protocol-Hip-Abduction-Adduction), [source](https://support.vald.com/hc/en-au/articles/4998398037657-ForceFrame-Test-Protocol-Hip-Internal-External-Rotation)). Record your paddle position. In hip adduction / abduction, the Testing Guide puts supine 45⁰ and 60⁰ among the two highest force production positions, and supine neutral (ankle) gives consistently the lowest force values ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). For seated ankle dorsiflexion, the guide says that changing the point of sensor contact or footwear alters torque mechanics and so affects force results ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). For shoulder abduction and adduction, the guide says sensor position is critical to keep a consistent lever arm for retests ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)).
  - Software history. ForceFrame iOS v1.9.0 (2023-11-01) fixed a bug where force metrics were calculated from median-filtered force ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). ForceFrame Windows v3.4.8 (2023-02-06) removed occasional noise spikes ([source](https://support.vald.com/hc/en-au/articles/29788227745305-ForceFrame-Windows-Release-Notes)).
  - Example data. In VALD's `/tests` example, `outerLeftMaxForce` is 32.5 while `outerLeftRepetitions` is 0 ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). Check `Repetitions` before you read a max force.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App, https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work, https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame, https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `innerLeftAvgForce`, `innerRightAvgForce`, `outerLeftAvgForce`, `outerRightAvgForce` (N, unit not stated in the spec)

The block has these fields:

- **What it measures:** An average force for one sensor in the test.
- **Calculation:** Not published. A VALD article on knee extension testing with DynaMo and ForceFrame describes "Mean Force" as the average force calculated across multiple repetitions ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). It does not say this is how `AvgForce` is computed.
- **Inputs and units:** Force from the sensor. The spec gives no unit ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). VALD reports ForceFrame force in newtons ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)).
- **Variants:** The four sensor fields above. Relative: `innerLeftAvgForcePerKg` and the other `AvgForcePerKg` fields on `/metrics`. No rep-level average field exists.
- **What changes the number:** Everything that changes `MaxForce`, plus the number of reps kept. In VALD's `/tests` example, sensors with 0 reps show `AvgForce` equal to `MaxForce` (32.5 and 32.5; 24.625 and 24.625) ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Sources:** https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance, https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf

### Left, right, and opposing-muscle comparisons

#### Imbalance (%) (app and protocol name; no API field)

The block has these fields:

- **What it measures:** The percentage difference between the left and right maximum force. The app shows one value for the inner sensors and one for the outer sensors.
- **Calculation:** The app help page describes imbalance as the percentage difference between left and right maximums ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). The formula ForceFrame uses: Not published. VALD's calculator formula is Asymmetry = (Right Value - Left Value) / Higher Value × 100 ([source](https://valdhealth.com/calculators), [source](https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making)). A VALD article labels this the "VALD asymmetry calculation" and shows two other formulas, limb symmetry index and symmetry index ([source](https://valdhealth.com/news/benchmarking-for-rehabilitation-providers)). Whether ForceFrame uses VALD's calculator formula: Not published.
- **Inputs and units:** Left and right `MaxForce` for the same sensor row (inner or outer). Percent.
- **Variants:** Inner imbalance and outer imbalance ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). The Testing Guide splits asymmetry into "Bilateral asymmetry" (left versus right, same contraction) and "Within limb asymmetry" (opposing muscle groups, same limb) ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). Sign convention and which side is reported as positive: Not published. The API has no imbalance field. Compute it from `innerLeftMaxForce` and `innerRightMaxForce`, or `outerLeftMaxForce` and `outerRightMaxForce`, and state the formula you used.
- **What changes the number:** Anything that changes either side's max force. The Neck Extension and Neck Flexion protocols list no imbalance result; all other protocols list "Imbalance [%]" ([source](https://support.vald.com/hc/en-au/articles/4998344479129-ForceFrame-Test-Protocol-Neck)). Different asymmetry formulas give different results on the same data ([source](https://valdhealth.com/news/benchmarking-for-rehabilitation-providers)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App, https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf, https://valdhealth.com/calculators, https://valdhealth.com/news/benchmarking-for-rehabilitation-providers, https://support.vald.com/hc/en-au/articles/4998344479129-ForceFrame-Test-Protocol-Neck

#### Strength ratio (inner:outer) (app name; protocols show "AB:AD Ratio", "IR:ER Ratio", "IN:EV Ratio"; no API field)

The block has these fields:

- **What it measures:** Inner-sensor maximum force compared with outer-sensor maximum force. VALD describes it as a comparison of opposing muscle groups ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **Calculation:** The app help page says the top-right metrics show the ratio of maximum inner force to maximum outer force. It reads a ratio above 1:1 as inner force dominant and a ratio below 1:1 as outer force dominant ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). Restated: ratio = inner max force ÷ outer max force. Whether it uses the left side, the right side, both, or a combined value: Not published. Why the protocol labels put abduction first ("AB:AD") while the app describes inner:outer: Not published.
- **Inputs and units:** Inner and outer max force. Unitless ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **Variants:** VALD says it appears if you chose a dual movement test, such as Hip Ad/Ab or Shoulder IR/ER ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Protocol labels: "AB:AD Ratio" for hip adduction / abduction ([source](https://support.vald.com/hc/en-au/articles/4998486609817-ForceFrame-Test-Protocol-Hip-Abduction-Adduction)), "IR:ER Ratio" for hip and shoulder rotation ([source](https://support.vald.com/hc/en-au/articles/4998398037657-ForceFrame-Test-Protocol-Hip-Internal-External-Rotation), [source](https://support.vald.com/hc/en-au/articles/4998364117273-ForceFrame-Test-Protocol-Shoulder-Internal-External-Rotation)), and "IN:EV Ratio" for ankle inversion / eversion ([source](https://support.vald.com/hc/en-au/articles/4998488417433-ForceFrame-Test-Protocol-Ankle-Inversion-Eversion)). Compute it from the API with the four `MaxForce` fields.
- **What changes the number:** Test position (hip adduction / abduction offers several positions with different force levels) ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). For neck testing, the Testing Guide says to take the flexion/extension ratio with caution because one direction is gravity assisted ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). Published reference points are third-party practice notes, not ForceFrame rules: an adduction-to-abduction ratio below 0.8 linked to greater injury risk ([source](https://valdperformance.com/news/my-dashboard-jo-clubb)), and UFC neck ratios ([source](https://valdperformance.com/news/neck-coupling-strength-in-mma-testing-what-matters)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App, https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/4998486609817-ForceFrame-Test-Protocol-Hip-Abduction-Adduction, https://support.vald.com/hc/en-au/articles/4998398037657-ForceFrame-Test-Protocol-Hip-Internal-External-Rotation, https://support.vald.com/hc/en-au/articles/4998364117273-ForceFrame-Test-Protocol-Shoulder-Internal-External-Rotation, https://support.vald.com/hc/en-au/articles/4998488417433-ForceFrame-Test-Protocol-Ankle-Inversion-Eversion, https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf

### Relative force

#### `innerLeftMaxForcePerKg`, `innerRightMaxForcePerKg`, `outerLeftMaxForcePerKg`, `outerRightMaxForcePerKg`, `innerLeftAvgForcePerKg`, `innerRightAvgForcePerKg`, `outerLeftAvgForcePerKg`, `outerRightAvgForcePerKg`, rep `maxForcePerKg` (N/kg)

The block has these fields:

- **What it measures:** Force relative to body mass. The app and Hub call it "Peak force / BM".
- **Calculation:** VALD defines it as peak force relative to body mass, which shows how much force is produced per kilogram or pound ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Restated: `MaxForcePerKg` = `MaxForce` ÷ body mass (kg). In VALD's repetitions example, `maxForce` ÷ `maxForcePerKg` = 83.0 kg for all four reps (436 ÷ 5.253, 465 ÷ 5.602, 404.75 ÷ 4.877, 397.5 ÷ 4.789), which fits that formula ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). How `AvgForcePerKg` is computed: Not published.
- **Inputs and units:** Max or average force (N) and body mass. The app shows N/kg or N/lb ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). The API field names say per kg ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** Max and Avg, for each of the four sensors, on `/tests/{testId}/metrics`. Rep level: `maxForcePerKg` on `/tests/{testId}/repetitions` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). All are nullable. What returns null (for example, no body mass on the profile): Not published.
- **What changes the number:** Body mass. The iOS release notes say body weight is pulled from the VALD Hub profile and can be edited in the app and on the results screen ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). The metric arrived in ForceFrame iOS v3.0.0 (2025-09-29), so older tests may lack it ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). Everything that changes max force.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

### Rate of force development

#### `innerLeftMaxRFDNewtonsPerSecond`, `innerRightMaxRFDNewtonsPerSecond`, `outerLeftMaxRFDNewtonsPerSecond`, `outerRightMaxRFDNewtonsPerSecond`, `innerLeftAvgRFDNewtonsPerSecond`, `innerRightAvgRFDNewtonsPerSecond`, `outerLeftAvgRFDNewtonsPerSecond`, `outerRightAvgRFDNewtonsPerSecond`, rep `maxRFDNewtonsPerSecond` (N/s)

The block has these fields:

- **What it measures:** How fast force rises. The app and Hub call it "Peak RFD".
- **Calculation:** VALD defines it as the steepest rise in force over time, which shows how quickly force is produced ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). The window length or slope method: Not published. Observation, not a VALD statement: in VALD's repetitions example, each `maxRFDNewtonsPerSecond` × 0.0425 s gives a round force change (2258.82 → 96.0 N, 1917.65 → 81.5 N, 1735.29 → 73.75 N, 1417.65 → 60.25 N) ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). That fits a 42.5 ms window (17 samples at 400 Hz). Confirm with your own trace before you rely on it. How Max and Avg combine reps: Not published.
- **Inputs and units:** The force trace and time. N/s, from the field names and the KB ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **Variants:** Max and Avg for each of the four sensors on `/metrics`. Rep level: `maxRFDNewtonsPerSecond` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). Fixed-window RFD: see the next block.
- **What changes the number:** Sampling rate. VALD raised iOS sampling to 400 Hz to capture these metrics ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). Pretension. VALD says that applying consistent pretension for 2-3s is critical for capturing valid RFD ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Cueing. VALD recommends telling the athlete to push or pull as hard and as fast as possible ([source](https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics)). Version. The metric arrived in ForceFrame iOS v3.0.0 (2025-09-29) ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). A VALD article published 2025-07-30 and updated 2025-12-01 still lists RFD as "DynaMo Only" ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). The iOS release notes and KB list RFD for ForceFrame.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://valdhealth.com/news/understanding-rate-of-force-development, https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics

#### RFD at 50, 100, 150, 200, and 250 ms (N/s)

These fields are on `/tests/{testId}/metrics` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

- 50 ms: `innerLeftMaxRFD50msNewtonsPerSecond`, `innerRightMaxRFD50msNewtonsPerSecond`, `outerLeftMaxRFD50msNewtonsPerSecond`, `outerRightMaxRFD50msNewtonsPerSecond`, `innerLeftAvgRFD50msNewtonsPerSecond`, `innerRightAvgRFD50msNewtonsPerSecond`, `outerLeftAvgRFD50msNewtonsPerSecond`, `outerRightAvgRFD50msNewtonsPerSecond`.
- 100 ms: `innerLeftMaxRFD100msNewtonsPerSecond`, `innerRightMaxRFD100msNewtonsPerSecond`, `outerLeftMaxRFD100msNewtonsPerSecond`, `outerRightMaxRFD100msNewtonsPerSecond`, `innerLeftAvgRFD100msNewtonsPerSecond`, `innerRightAvgRFD100msNewtonsPerSecond`, `outerLeftAvgRFD100msNewtonsPerSecond`, `outerRightAvgRFD100msNewtonsPerSecond`.
- 150 ms: `innerLeftMaxRFD150msNewtonsPerSecond`, `innerRightMaxRFD150msNewtonsPerSecond`, `outerLeftMaxRFD150msNewtonsPerSecond`, `outerRightMaxRFD150msNewtonsPerSecond`, `innerLeftAvgRFD150msNewtonsPerSecond`, `innerRightAvgRFD150msNewtonsPerSecond`, `outerLeftAvgRFD150msNewtonsPerSecond`, `outerRightAvgRFD150msNewtonsPerSecond`.
- 200 ms: `innerLeftMaxRFD200msNewtonsPerSecond`, `innerRightMaxRFD200msNewtonsPerSecond`, `outerLeftMaxRFD200msNewtonsPerSecond`, `outerRightMaxRFD200msNewtonsPerSecond`, `innerLeftAvgRFD200msNewtonsPerSecond`, `innerRightAvgRFD200msNewtonsPerSecond`, `outerLeftAvgRFD200msNewtonsPerSecond`, `outerRightAvgRFD200msNewtonsPerSecond`.
- 250 ms: `innerLeftMaxRFD250msNewtonsPerSecond`, `innerRightMaxRFD250msNewtonsPerSecond`, `outerLeftMaxRFD250msNewtonsPerSecond`, `outerRightMaxRFD250msNewtonsPerSecond`, `innerLeftAvgRFD250msNewtonsPerSecond`, `innerRightAvgRFD250msNewtonsPerSecond`, `outerLeftAvgRFD250msNewtonsPerSecond`, `outerRightAvgRFD250msNewtonsPerSecond`.

These fields are on `/tests/{testId}/repetitions` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)): `rfd50msNewtonsPerSecond`, `rfd100msNewtonsPerSecond`, `rfd150msNewtonsPerSecond`, `rfd200msNewtonsPerSecond`, `rfd250msNewtonsPerSecond`.

The block has these fields:

- **What it measures:** How fast force rises in the first 50 to 250 ms of the effort. Hub names: "RFD at 50ms" to "RFD at 250ms".
- **Calculation:** VALD defines each field as the highest rate of force development reached within the first 50, 100, 150, 200, or 250 milliseconds after the effort starts ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). VALD also describes RFD as the slope of the force-time curve ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Restated: the steepest force-time slope found between effort start and effort start + X ms. How VALD detects the start of the effort, and the slope method: Not published.
- **Inputs and units:** The force trace from effort start. N/s ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **Variants:** 5 windows × Max and Avg × 4 sensors on `/metrics`. Rep level has one value per window per rep and sensor. Hub shows these; the iOS app does not ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure), [source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **What changes the number:** Start detection and pretension. VALD's RFD cheat sheet rates early-phase RFD (0-150ms) as slightly less reliable because of test initiation and start of movement detection ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf)). Restated: VALD says early-phase RFD (≤150ms) mainly reflects neural drive, and later windows overlap more with peak force ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Sampling rate: VALD says a rate of 300-500Hz is enough to capture peak force and RFD accurately in most isometric and dynamic assessments ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Available from iOS v3.0.0 (2025-09-29) ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://valdhealth.com/news/understanding-rate-of-force-development, https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf

### Time to peak force

#### `innerLeftMinTimeToMaxForceSeconds`, `innerRightMinTimeToMaxForceSeconds`, `outerLeftMinTimeToMaxForceSeconds`, `outerRightMinTimeToMaxForceSeconds`, `innerLeftAvgTimeToMaxForceSeconds`, `innerRightAvgTimeToMaxForceSeconds`, `outerLeftAvgTimeToMaxForceSeconds`, `outerRightAvgTimeToMaxForceSeconds`, rep `timeToMaxForceSeconds` (s)

The block has these fields:

- **What it measures:** Time from the start of the effort to peak force. The app calls it "Min time to peak force". The iOS release notes call it "Time to Peak Force".
- **Calculation:** VALD defines it as the time needed to reach peak force from the start of the effort, and says lower values are generally preferred ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Restated: time to max force = time of peak - time of effort start. Effort start detection: Not published. How `Min` and `Avg` combine the reps: Not published.
- **Inputs and units:** The force trace. Seconds ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** Min and Avg for each of the four sensors on `/metrics`. Rep level: `timeToMaxForceSeconds` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **What changes the number:** Effort strategy and pretension. A VALD education article calls time to peak force highly variable and influenced by isometric strategy ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Hold duration and cueing. Available from iOS v3.0.0 (2025-09-29) ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://valdhealth.com/news/understanding-rate-of-force-development

### Impulse

#### `innerLeftImpulse`, `innerRightImpulse`, `outerLeftImpulse`, `outerRightImpulse`, rep `impulse` (N·s, unit not stated in the spec)

The block has these fields:

- **What it measures:** Force accumulated over time for one sensor (area under the force-time curve).
- **Calculation:** The Testing Guide says impulse is calculated from the area under the force curve, and gives the formula Impulse = Force x Time ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). With a 25N impulse threshold, ForceFrame starts calculating impulse when the applied force exceeds 25N ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS)). Restated: impulse = sum of force × sample interval, counted while force is above the impulse threshold. Whether the test value sums or averages the reps: Not published.
- **Inputs and units:** The force trace and the impulse threshold. VALD lists impulse in "Newton-Seconds (Ns)" ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). The spec gives no unit ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** Four sensor fields on the test summary. Rep level: `impulse` per `sensorType` and `repNumber`. Fixed-window impulse: next block. Training impulse: `impulseLeft` and `impulseRight` (see the training section).
- **What changes the number:** The impulse threshold. ForceFrame Windows lets you change it. In iOS, the threshold for calculating impulse cannot be customized ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS), [source](https://support.vald.com/hc/en-au/articles/4998153143577-Adjusting-detection-thresholds-in-ForceFrame-Windows)). The default threshold value: Not published (25N is an example). Hold time: longer or harder contractions give larger impulse ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). Number of reps kept. In VALD's `/tests` example, sensors with 0 reps show impulse 0.0 ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Sources:** https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf, https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/4998153143577-Adjusting-detection-thresholds-in-ForceFrame-Windows, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### Impulse at 50, 100, 150, 200, and 250 ms (N·s)

These fields are on `/tests/{testId}/metrics` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

- 50 ms: `innerLeftMaxImpulse50msNewtonSeconds`, `innerRightMaxImpulse50msNewtonSeconds`, `outerLeftMaxImpulse50msNewtonSeconds`, `outerRightMaxImpulse50msNewtonSeconds`, `innerLeftAvgImpulse50msNewtonSeconds`, `innerRightAvgImpulse50msNewtonSeconds`, `outerLeftAvgImpulse50msNewtonSeconds`, `outerRightAvgImpulse50msNewtonSeconds`.
- 100 ms: `innerLeftMaxImpulse100msNewtonSeconds`, `innerRightMaxImpulse100msNewtonSeconds`, `outerLeftMaxImpulse100msNewtonSeconds`, `outerRightMaxImpulse100msNewtonSeconds`, `innerLeftAvgImpulse100msNewtonSeconds`, `innerRightAvgImpulse100msNewtonSeconds`, `outerLeftAvgImpulse100msNewtonSeconds`, `outerRightAvgImpulse100msNewtonSeconds`.
- 150 ms: `innerLeftMaxImpulse150msNewtonSeconds`, `innerRightMaxImpulse150msNewtonSeconds`, `outerLeftMaxImpulse150msNewtonSeconds`, `outerRightMaxImpulse150msNewtonSeconds`, `innerLeftAvgImpulse150msNewtonSeconds`, `innerRightAvgImpulse150msNewtonSeconds`, `outerLeftAvgImpulse150msNewtonSeconds`, `outerRightAvgImpulse150msNewtonSeconds`.
- 200 ms: `innerLeftMaxImpulse200msNewtonSeconds`, `innerRightMaxImpulse200msNewtonSeconds`, `outerLeftMaxImpulse200msNewtonSeconds`, `outerRightMaxImpulse200msNewtonSeconds`, `innerLeftAvgImpulse200msNewtonSeconds`, `innerRightAvgImpulse200msNewtonSeconds`, `outerLeftAvgImpulse200msNewtonSeconds`, `outerRightAvgImpulse200msNewtonSeconds`.
- 250 ms: `innerLeftMaxImpulse250msNewtonSeconds`, `innerRightMaxImpulse250msNewtonSeconds`, `outerLeftMaxImpulse250msNewtonSeconds`, `outerRightMaxImpulse250msNewtonSeconds`, `innerLeftAvgImpulse250msNewtonSeconds`, `innerRightAvgImpulse250msNewtonSeconds`, `outerLeftAvgImpulse250msNewtonSeconds`, `outerRightAvgImpulse250msNewtonSeconds`.

These fields are on `/tests/{testId}/repetitions` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)): `impulse50msNewtonSeconds`, `impulse100msNewtonSeconds`, `impulse150msNewtonSeconds`, `impulse200msNewtonSeconds`, `impulse250msNewtonSeconds`.

The block has these fields:

- **What it measures:** Force accumulated in the first 50 to 250 ms of the effort. Hub names: "Impulse at 50ms" to "Impulse at 250ms".
- **Calculation:** VALD defines each field as the highest impulse reached within the first 50, 100, 150, 200, or 250 milliseconds after the effort starts ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)). Restated: area under the force-time curve from effort start to effort start + X ms. Effort start detection, and whether pretension force is subtracted: Not published.
- **Inputs and units:** The force trace. N s ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **Variants:** 5 windows × Max and Avg × 4 sensors on `/metrics`. Rep level has one value per window per rep and sensor. Hub only; not shown in the iOS app ([source](https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure)).
- **What changes the number:** Start detection, pretension, and sampling rate, as for RFD at fixed times ([source](https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics), [source](https://valdhealth.com/news/understanding-rate-of-force-development)). Available from iOS v3.0.0 (2025-09-29) ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4997692915353-What-Does-ForceFrame-Measure, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics

### Reps and rep timing

#### `innerLeftRepetitions`, `innerRightRepetitions`, `outerLeftRepetitions`, `outerRightRepetitions` (count)

The block has these fields:

- **What it measures:** How many reps ForceFrame detected on one sensor.
- **Calculation:** With a 150N rep threshold, ForceFrame detects that a rep has started when the applied force exceeds 150N ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS)). Restated: count of detected reps that remain selected at upload. The default rep threshold per test type: Not published (150N is an example).
- **Inputs and units:** Force trace and rep threshold. Integer ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** Rep rows on `/tests/{testId}/repetitions` carry `repNumber` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **What changes the number:** The rep threshold, set per test type. In iOS it applies only to the current user and device ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS)). Deleting or deselecting reps ([source](https://support.vald.com/hc/en-au/articles/26094908032537-Delete-reps-in-ForceFrame-iOS)). iOS v1.5.1 (2022-08-23) fixed spikes being recorded as reps ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). iOS v2.3.3 (2024-12-10) fixed invalid data for bilateral tests with no reps on one side ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/4998153143577-Adjusting-detection-thresholds-in-ForceFrame-Windows, https://support.vald.com/hc/en-au/articles/26094908032537-Delete-reps-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `startOffsetSeconds`, `endOffsetSeconds` (s)

The block has these fields:

- **What it measures:** When a rep starts and ends, as time offsets. Rep endpoint only.
- **Calculation:** Not published. The reference point for the offset: Not published. In VALD's example, `OuterLeft` rep 2 starts at 0.3425 s and rep 1 starts at 3.3175 s, so offsets may not count from one shared test start ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). Restated: rep duration = `endOffsetSeconds` - `startOffsetSeconds`; what defines the boundaries (for example, rep threshold crossings) is Not published.
- **Inputs and units:** Seconds, `number double`, nullable ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** One pair per rep per `sensorType`.
- **What changes the number:** The rep threshold ([source](https://support.vald.com/hc/en-au/articles/50908860348441-Adjusting-detection-thresholds-in-ForceFrame-iOS)).
- **Sources:** https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API

### Fields in the KB example that the spec does not list

#### `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `rightAvgForcePerKg`, `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg`, and the `left`/`right` RFD, time, and impulse fields (example only)

The block has these fields:

- **What it measures:** The KB's "Scenario 5" example response for `/tests/{testId}/metrics` shows left and right fields instead of inner and outer, plus four torque per kg fields ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). The full list in the example is: `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `rightAvgForcePerKg`, `leftMaxRFDNewtonsPerSecond`, `rightMaxRFDNewtonsPerSecond`, `leftAvgRFDNewtonsPerSecond`, `rightAvgRFDNewtonsPerSecond`, `leftMinTimeToMaxForceSeconds`, `rightMinTimeToMaxForceSeconds`, `leftAvgTimeToMaxForceSeconds`, `rightAvgTimeToMaxForceSeconds`, `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg`, `leftMaxRFD50msNewtonsPerSecond`, `leftAvgRFD50msNewtonsPerSecond`, `rightMaxRFD50msNewtonsPerSecond`, `rightAvgRFD50msNewtonsPerSecond`, `leftMaxRFD100msNewtonsPerSecond`, `leftAvgRFD100msNewtonsPerSecond`, `rightMaxRFD100msNewtonsPerSecond`, `rightAvgRFD100msNewtonsPerSecond`, `leftMaxRFD150msNewtonsPerSecond`, `leftAvgRFD150msNewtonsPerSecond`, `rightMaxRFD150msNewtonsPerSecond`, `rightAvgRFD150msNewtonsPerSecond`, `leftMaxRFD200msNewtonsPerSecond`, `leftAvgRFD200msNewtonsPerSecond`, `rightMaxRFD200msNewtonsPerSecond`, `rightAvgRFD200msNewtonsPerSecond`, `leftMaxRFD250msNewtonsPerSecond`, `leftAvgRFD250msNewtonsPerSecond`, `rightMaxRFD250msNewtonsPerSecond`, `rightAvgRFD250msNewtonsPerSecond`, `leftMaxImpulse50msNewtonSeconds`, `leftAvgImpulse50msNewtonSeconds`, `rightMaxImpulse50msNewtonSeconds`, `rightAvgImpulse50msNewtonSeconds`, `leftMaxImpulse100msNewtonSeconds`, `leftAvgImpulse100msNewtonSeconds`, `rightMaxImpulse100msNewtonSeconds`, `rightAvgImpulse100msNewtonSeconds`, `leftMaxImpulse150msNewtonSeconds`, `leftAvgImpulse150msNewtonSeconds`, `rightMaxImpulse150msNewtonSeconds`, `rightAvgImpulse150msNewtonSeconds`, `leftMaxImpulse200msNewtonSeconds`, `leftAvgImpulse200msNewtonSeconds`, `rightMaxImpulse200msNewtonSeconds`, `rightAvgImpulse200msNewtonSeconds`, `leftMaxImpulse250msNewtonSeconds`, `leftAvgImpulse250msNewtonSeconds`, `rightMaxImpulse250msNewtonSeconds`, `rightAvgImpulse250msNewtonSeconds`.
- **Calculation:** Not published for ForceFrame. The spec for `/tests/{testId}/metrics` lists only `innerLeft`, `innerRight`, `outerLeft`, and `outerRight` fields, and no torque fields ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). The ForceFrame example is identical to the NordBord API guide example: same `athleteId`, same `testId`, and every value matches (text compared on 2026-10-02) ([ForceFrame guide](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API), [NordBord guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). This reference did not call the live API to check which names it returns.
- **Inputs and units:** Torque per kg unit: Not published for ForceFrame.
- **Variants:** None in the spec.
- **What changes the number:** Not applicable. Code against the spec field names, and check one live response.
- **Sources:** https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### Torque (no ForceFrame field)

The block has these fields:

- **What it measures:** Not published for ForceFrame. No ForceFrame source defines a torque metric, a lever arm input, or a torque unit.
- **Calculation:** Not published. The Testing Guide mentions torque only as a source of error: a changed sensor contact point or footwear alters "torque mechanics" in ankle dorsiflexion, and athletes may rotate the torso "to increase torque or leverage the body" in shoulder abduction and adduction ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)).
- **Inputs and units:** Not published.
- **Variants:** Only the KB example fields above, which match the NordBord example.
- **What changes the number:** Not applicable.
- **Sources:** https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

### Reference points in the app and Hub

#### Personal Best (app history option; no API field)

The block has these fields:

- **What it measures:** The athlete's best ever result for the test type.
- **Calculation:** VALD defines Personal Best as the individual's highest ever left and right results for the test type ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). Restated: max of past results, per side.
- **Inputs and units:** Past tests of the same test type. Same unit as the metric.
- **Variants:** Left and right. Whether position is matched: Not published.
- **What changes the number:** Deleted or reassigned tests. Test type edits in Hub ([source](https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App

#### Baseline (app history option; no API field)

The block has these fields:

- **What it measures:** A saved reference result.
- **Calculation:** VALD defines Baseline as a saved reference point, often set at the start of a pre-season or season ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)).
- **Inputs and units:** The chosen test. Same unit as the metric.
- **Variants:** Not published.
- **What changes the number:** Which test you save as baseline.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App

#### Moving Average (app history option; no API field)

The block has these fields:

- **What it measures:** The athlete's recent average.
- **Calculation:** VALD defines Moving Average as the average result from the last 1 to 10 tests, as selected ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). Restated: mean of the last N tests, N from 1 to 10.
- **Inputs and units:** The last N tests of the test type. Same unit as the metric.
- **Variants:** N = 1 to 10.
- **What changes the number:** N, and deleted reps or tests.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App

#### Norms (percentile against VALD data; no API field)

The block has these fields:

- **What it measures:** Where a result sits against other VALD users of the same age group and sex.
- **Calculation:** VALD removes results that lie more than 1.5 times the IQR from the upper or lower quartile as outliers ([source](https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated)). Strength norms are sex specific ([source](https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated)). VALD defines a percentile as the percentage of individuals in the reference population who scored lower than a given test result ([source](https://support.vald.com/hc/en-au/articles/21651363065753-Normative-data-FAQs)). The curve-fitting algorithm that produces the percentile curves: Not published.
- **Inputs and units:** Profile age and sex. Percentile.
- **Variants:** ForceFrame norms exist for listed test types and positions, for example Hip Adduction / Abduction at 45º, 60º, 90º, and Seated ([source](https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems)). In-app norms since iOS v2.3.1 (2024-09-17) ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **What changes the number:** Wrong age or sex on the profile ([source](https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated)). Periodic norm refreshes ([source](https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated)).
- **Sources:** https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated, https://support.vald.com/hc/en-au/articles/21651363065753-Normative-data-FAQs, https://support.vald.com/hc/en-au/articles/26301645046553-Norms-available-in-VALD-systems, https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes

### Force trace (`/tests/{testId}/forceframetrace`)

#### `innerLeftForce`, `innerRightForce`, `outerLeftForce`, `outerRightForce` (N)

The block has these fields:

- **What it measures:** The force on each sensor at one sample.
- **Calculation:** Direct load cell reading. The Testing Guide says force is measured directly from the ForceFrame sensor pads ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). Any filtering applied to the stored trace: Not published. iOS v1.5.1 (2022-08-23) added a median filter to the on-screen graph ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Inputs and units:** Newtons. The spec gives `number double` with no unit ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). The app plots force in newtons ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)).
- **Variants:** Four sensors. The `Force` schema has no flat or upper sensor columns, although the six-sensor Max exists ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json), [source](https://valdhealth.com/news/the-history-and-future-of-forceframe)). Sign: the app shows inner as negative and outer as positive ([source](https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App)). VALD's API example shows small negative values near zero (`innerRightForce` -1.0) ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). API sign convention: Not published.
- **What changes the number:** Zeroing offsets ([source](https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work)). Sampling rate, 50 Hz to 400 Hz ([source](https://support.vald.com/hc/en-au/article_attachments/25314373779993)). Capacity limits ([source](https://support.vald.com/hc/en-au/articles/10326791502617-Force-Capacity-of-ForceFrame)). iOS v1.6.2 (2023-05-04) shipped firmware v2.2 and fixed occasional zero points in the trace ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://support.vald.com/hc/en-au/articles/4998196752281-Understanding-Results-in-the-ForceFrame-App, https://support.vald.com/hc/en-au/articles/4997903244697-How-the-ForceFrame-Sensors-Work, https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub

#### `ticks` (int64, unit not published)

The block has these fields:

- **What it measures:** The timestamp of each force sample.
- **Calculation:** Not published. Observation, not a VALD statement: VALD's example values decode as .NET ticks (100 ns units since 0001-01-01). The first example tick, 638179046401209472, decodes to 2023-04-24 03:44:00.12. The last, 638179050916719232, decodes to 2023-04-24 03:51:31.67, close to the example `testDateUTC` of 2023-04-24T03:51:32.933Z ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). Restated: if that holds, seconds between samples = tick difference ÷ 10,000,000.
- **Inputs and units:** `integer int64` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** None.
- **What changes the number:** Sampling rate sets the spacing between samples ([source](https://support.vald.com/hc/en-au/article_attachments/25314373779993)).
- **Sources:** https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API

### Training prescription (`/training/programs/current`, `TrainingExercise`)

#### `forceGoal` (N in the example; unit not in the spec)

The block has these fields:

- **What it measures:** The target force for a training exercise.
- **Calculation:** Set by the practitioner. Hub calls it "Force Value (Newtons)" ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)). With a Manual zone, the practitioner specifies the target force by hand ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). With a Max zone, the target is a specified percentage of the individual's results from the previous five testing sessions ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). Whether `forceGoal` stores newtons or that percentage when `trainingZone` is `Max`: Not published.
- **Inputs and units:** Newtons per Hub ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)). Example `forceGoal` 200 with `trainingZone` `Manual` ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** Depends on `trainingZone`.
- **What changes the number:** The target can be edited during a session by dragging the training zone ([source](https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS)). Whether those edits are saved to `forceGoal`: Not published.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `trainingZone` (enum `Manual`, `Max`, `Average`)

The block has these fields:

- **What it measures:** How the target force is set.
- **Calculation:** `Manual`: a fixed force. `Max`: a percentage of recent test results ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). `Average`: listed by Hub as a Force Target option ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)); its definition: Not published.
- **Inputs and units:** Enum `ForceTarget` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** iOS offers Max or Manual ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). Hub offers Manual, Average, and Max ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)).
- **What changes the number:** Missing test data. iOS shows a warning icon when there is not enough testing data to calculate a target ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `tolerance`, `toleranceUnit`

The block has these fields:

- **What it measures:** The width of the training zone around the target.
- **Calculation:** Hub lists "Tolerance (%)" ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)). The iOS guide says the training zone range defaults to 10% above or below the target ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)). Restated: zone = target × (1 - tolerance/100) to target × (1 + tolerance/100); a 200N target with 10% gives 180N to 220N ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)).
- **Inputs and units:** The KB says percent. The API example shows `tolerance` 10 with `toleranceUnit` "N" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). These conflict. Read `toleranceUnit` on every row.
- **Variants:** Not published.
- **What changes the number:** Practitioner settings.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `contractionTime` (time span, `hh:mm:ss`)

The block has these fields:

- **What it measures:** How long each rep should be held in the zone.
- **Calculation:** Set by the practitioner. Hub: "Contraction Time (Seconds)" ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)). iOS labels it "Hold (s)" and describes it as the number of seconds each rep is held in the training zone ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS)).
- **Inputs and units:** `date-span`; the example is "00:00:05" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** None.
- **What changes the number:** Practitioner settings.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API

#### `restTime`, `restTimeAfterSet` (time span, `hh:mm:ss`)

The block has these fields:

- **What it measures:** Rest between reps, and rest after the set.
- **Calculation:** Set by the practitioner. Hub: "Rest Time (Seconds)" and "Rest Time After Set (Seconds)" ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)).
- **Inputs and units:** `date-span`; example "00:00:05" and "00:00:00" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** None.
- **What changes the number:** iOS v2.2.1 (2024-06-27) removed the rest timer after the last rep ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API

#### `repetitions` (prescribed reps, count)

The block has these fields:

- **What it measures:** How many reps the exercise prescribes.
- **Calculation:** Set by the practitioner. Hub: "Number of Repetitions" ([source](https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame)).
- **Inputs and units:** Integer ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** Hub's training export shows "Reps Completed", which is the performed count, not this prescription ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). The API has no completed-reps field; count rows in `/training/sessions/exercises/repetitions`.
- **What changes the number:** Practitioner settings.
- **Sources:** https://support.vald.com/hc/en-au/articles/4998302415385-Training-with-ForceFrame, https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

### Training results (`/training/sessions`, `/training/sessions/exercises`, `/training/sessions/exercises/repetitions`)

#### `timeInZoneLeft`, `timeInZoneRight` (unit not published in the API; Hub shows %)

The block has these fields:

- **What it measures:** How much of the effort stayed inside the training zone.
- **Calculation:** Not published. VALD tells the athlete to keep force production inside the training zone shown in green ([source](https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS)). Hub exports "Time in Zone (%)" ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). How sessions and exercises aggregate reps: Not published.
- **Inputs and units:** Force trace, `forceGoal`, and `tolerance`. API unit: Not published. VALD's rep example shows 0.108 on both sides ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** Session level (non-nullable), exercise level (nullable), and rep level ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)). Left and right only.
- **What changes the number:** Tolerance width, target force, hold time, and mid-session zone edits ([source](https://support.vald.com/hc/en-au/articles/33876053887385-Create-a-training-program-in-ForceFrame-iOS), [source](https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS)).
- **Sources:** https://support.vald.com/hc/en-au/articles/33883812513433-Run-a-training-program-in-ForceFrame-iOS, https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### `stabilityLeft`, `stabilityRight` (unit not published)

The block has these fields:

- **What it measures:** Not published.
- **Calculation:** Not published. Hub's training export shows "Variance (%)" and no stability column ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). Whether `stability` is the same value as Hub "Variance (%)": Not published. A VALD case study says ForceFrame "time in zone" and "variance" metrics tracked tolerance to isometric training ([source](https://valdhealth.com/news/post-surgical-shoulder-rehab-for-a-professional-baseball-pitcher)).
- **Inputs and units:** Not published. VALD's rep example shows 2.426 left and 2.623 right ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** Session, exercise, and rep levels. Left and right.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes, https://valdhealth.com/news/post-surgical-shoulder-rehab-for-a-professional-baseball-pitcher

#### `impulseLeft`, `impulseRight` (N s in Hub; unit not in the API)

The block has these fields:

- **What it measures:** Force accumulated over time during training.
- **Calculation:** Not published for training. For testing, impulse is the area under the force curve ([source](https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf)). The iOS v2.2.0 release notes (2024-06-18) say that post-training results now include impulse ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). Whether an impulse threshold applies in training, and how sessions aggregate reps: Not published.
- **Inputs and units:** Hub exports "Impulse (N s)" ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). VALD's rep example shows 54.065 left and 55.017 right ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- **Variants:** Session, exercise, and rep levels. Left and right.
- **What changes the number:** Target force, hold time, and number of reps.
- **Sources:** https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes, https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes, https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API, https://support.vald.com/hc/en-au/article_attachments/24780698651161/VALD%20ForceFrame%20Testing%20Guide.pdf, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

#### Reps Completed, Exercise Type (Hub training export only)

The block has these fields:

- **What it measures:** Reps performed in an exercise, and the exercise name.
- **Calculation:** Not published. Listed in the Hub training export since 2024-10-17 ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Inputs and units:** Count; text.
- **Variants:** API: count rows per `sessionExerciseId` in `/training/sessions/exercises/repetitions`; the program exercise (linked by `programExerciseId`) carries `movement`, `joint`, and `testTypeName`, but the API does not say which of these Hub shows as Exercise Type ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- **What changes the number:** Skipped exercises or reps. iOS v2.2.1 fixed a results bug after a skipped exercise ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes, https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json

### Identifiers and context fields

The tables list the identifier and context fields of each endpoint. This table covers `GET /tests` and `GET /tests/{testId}` (`GetTestSummaryResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Note |
|---|---|---|
| `athleteId` | uuid | Profile ID. V2 calls it `profileId`. |
| `testId` | uuid | |
| `testDateUtc` | date-time | |
| `testTypeId`, `testTypeName` | uuid, string | For example "Ankle IN/EV" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). |
| `testPositionId`, `testPositionName` | uuid, string | For example "Ankle Inversion/Eversion - Supine" ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). |
| `notes` | string | Test notes. The iOS release notes say notes are not available in VALD Hub but can be read through the external API ([source](https://support.vald.com/hc/en-au/articles/29741805118745-ForceFrame-iOS-Release-Notes)). |
| `device` | string | Device name, for example "ForceFrame-1359". |
| `modifiedDateUtc` | date-time | |
| `page`, `pageCount` | int | Wrapper `GetTestsByDateRangeResponse` only. |

This table covers `GET /tests/v2` (`GetTestSummaryResponseV2`, inside `GetTestsByModifiedDateResponse.tests`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Note |
|---|---|---|
| `profileId` | uuid | Replaces `athleteId`. |
| `testId`, `testDateUtc`, `testTypeId`, `testTypeName`, `testPositionId`, `testPositionName`, `notes`, `device` | as above | |
| `modifiedDateUtc` | string, nullable | A date-time in v1. Use it as the next `ModifiedFromUtc` ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). |

This table covers `GET /tests/{testId}/metrics` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type |
|---|---|
| `athleteId` | uuid |
| `testId` | uuid |

This table covers `GET /tests/{testId}/repetitions` ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Note |
|---|---|---|
| `id` | uuid | Rep row ID. |
| `testId` | uuid | |
| `sensorType` | enum | `InnerLeft`, `InnerRight`, `OuterLeft`, `OuterRight`, `FlatLeft`, `FlatRight`. |
| `repNumber` | int | Rep number per sensor. |

This table covers `GET /tests/{testId}/forceframetrace` (`GetTraceResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type |
|---|---|
| `athleteId`, `testId`, `testTypeId`, `testPositionId` | uuid |
| `testTypeName`, `testPositionName`, `device`, `notes` | string |
| `testDateUTC` | date-time |
| `forces` | array of `Force` (`ticks` plus four sensor forces) |

This table covers `GET /training/programs/current` (`GetTrainingProgramResponse`, `TrainingExercise`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Note |
|---|---|---|
| `id`, `name` | uuid, string | Program. The example `name` is a person's name ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). |
| `scheduledDatesUTC` | array of string | |
| `addedDate`, `modifiedDate` | date-time | |
| `exercises[].id` | uuid | Program exercise ID. Training results reference it as `programExerciseId`. |
| `laterality` | enum | `Bilateral`, `UnilateralAlternating`, `Left`, `Right`, `NA`. |
| `movement` | enum | `Abduction`, `Adduction`, `InternalRotation`, `ExternalRotation`, `Flexion`, `Extension`, `Eccentric`, `Concentric`, `AbductionAdduction`, `InternalExternalRotation`, `FlexionExtension`, `EccentricConcentric`, `LateralFlexion`, `Dorsiflexion`, `Inversion`, `Eversion`, `PlantarFlexion`, `InnerPaddles`, `OuterPaddles`. |
| `joint` | enum | `Hamstring`, `Hip`, `Ankle`, `Knee`, `Shoulder`, `Neck`, `Elbow`, `Dyno`, `Custom`. |
| `order` | int | Exercise order in the program. |
| `trainingPositionId`, `testTypeId`, `testPositionId`, `testTypeName` | uuid, string | Last three nullable. |

This table covers `GET /training/sessions` (`GetTrainingSessionsResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type |
|---|---|
| `id`, `profileId`, `tenantId`, `programId` | uuid |
| `sessionDateUtc`, `modifiedDateUTC` | date-time |

This table covers `GET /training/sessions/exercises` (`GetTrainingSessionExercisesResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type |
|---|---|
| `id`, `sessionId`, `programExerciseId` | uuid |
| `profileId`, `tenantId` | uuid, nullable |
| `exerciseDateUtc`, `modifiedDateUTC` | date-time |

This table covers `GET /training/sessions/exercises/repetitions` (`GetTrainingSessionExerciseRepetitionsResponse`) ([spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Note |
|---|---|---|
| `id`, `repetitionId` | uuid | Equal in VALD's example ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)). |
| `profileId`, `tenantId` | uuid, nullable | |
| `sessionId`, `sessionExerciseId`, `programExerciseId` | uuid | |
| `repetition` | int | Rep number. |
| `repetitionDateUTC`, `modifiedDateUTC` | date-time | |

The API guide and the spec differ in these places:

- KB Scenario 7 is titled "Retrieve a single exercise session" but calls `/training/programs/current` with `Id` and returns a program ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API)).
- KB Scenario 9 is titled "Retrieve a collection of training sessions" but shows the URL `/training/sessions/exercises`. The spec has a separate `/training/sessions` path ([source](https://support.vald.com/hc/en-au/articles/29365519335065-A-guide-to-using-the-External-ForceFrame-API), [spec](https://prd-use-api-externalforceframe.valdperformance.com/swagger/v1/swagger.json)).
- The KB `/metrics` example uses NordBord field names (see the block above).

### Marked Not published

The following details are marked Not published in this section:

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

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
