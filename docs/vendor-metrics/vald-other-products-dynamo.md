# VALD DynaMo metrics

DynaMo is a handheld dynamometer and inclinometer. It measures force with a load cell and orientation with a 9-axis inertial sensor. This page covers the strength and range of motion fields in the DynaMo VALD Hub views and the External DynaMo API. Checked against: the VALD knowledge base (including the External DynaMo API guide, the DynaMo app settings and FAQ articles, and the DynaMo iOS and Android release notes), the VALD Hub release notes, the DynaMo spec sheets, the External DynaMo OpenAPI spec (`v1` spec with `/v2022q2` endpoints), VALD education and calculator pages, the VALD RFD cheat sheet, and the `valdr` R package 4.0.0, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

This page is part of [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](vald-other-products.md). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](vald-forcedecks-nordbord.md).

## How to read this page

Each metric block names the exact field or Hub name and then lists the following items:

- What it measures.
- Calculation: VALD's definition in paraphrase, then the formula in plain math where a source gives one.
- Inputs and units.
- Variants.
- Comparison with standard methods or other vendors, only where a source supports it.
- What changes the number.
- Source links.

A formula labeled Restated is this page's plain restatement, not the vendor's statement. A calculation or detail marked Not published is one that the vendor does not publish in the public sources checked. It does not mean the vendor lacks the information. None of the VALD OpenAPI specs carry field descriptions, so definitions come from the VALD knowledge base, VALD education pages, and the `valdr` R package.

## DynaMo

### Overview

The overview covers the device, the export routes, the row structure, the side labels, the test types, and the settings that affect every strength metric:

- **What the device measures.** DynaMo is a handheld dynamometer and inclinometer. It measures force with a load cell and orientation with a 9-axis inertial sensor (IMU) ([source](https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models), [source](https://support.vald.com/hc/en-au/article_attachments/62792898708505)). There are three models:
  - **DynaMo Lite:** compression only, 100 kg (1000 N) capacity, force at 225 Hz, IMU at 225 Hz, 1 N resolution ([source](https://support.vald.com/hc/en-au/article_attachments/62792928707993)).
  - **DynaMo Plus:** compression 1000 N and tension 2000 N, force at 225 Hz, IMU at 225 Hz, 1 N resolution, OLED screen, NFC Smart Attachments, grip attachment ([source](https://support.vald.com/hc/en-au/article_attachments/62792898708505), [source](https://support.vald.com/hc/en-au/articles/5457903678745-Connect-your-DynaMo-attachments)).
  - **DynaMo Max:** tension and compression 10,000 N (1,000 kg), force at 1,200 Hz, IMU at 225 Hz, 1 N resolution, optional IMTP and belt squat hardware ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009), [source](https://support.vald.com/hc/en-au/articles/38449708425369-DynaMo-Max-system-hardware)).
  - Sources disagree on DynaMo Max size and weight: 400 g ([source](https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models)), 850 g ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)), and 1.5 kg ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). This does not affect the metrics.
- **Export routes.**
  - **VALD Hub CSV.** The Hub export article gives CSV steps for NordBord, ForceFrame, and ForceDecks only. It has no DynaMo steps ([source](https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub)). Hub does have a DynaMo Results Export view that you can filter by group, profile, test category, body region, movement, and position, and sort by column ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). DynaMo CSV steps and column names: Not published. VALD states that Hub exports force trace data for NordBord and ForceFrame systems only ([source](https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub)). A DynaMo Leaderboard (strength only) can be exported to CSV ([source](https://support.vald.com/hc/en-au/articles/17676771546649-Create-a-Leaderboard-in-VALD-Hub), [source](https://support.vald.com/hc/en-au/articles/8817109682457-Introduction-to-Leaderboard)). Its columns: Not published.
  - **Other Hub views.** Profile Overview tiles, Result Table, Timeline (copy results as plain text), Group Dashboard monitoring and quadrant charts, Leaderboard, and printed reports all show DynaMo data ([source](https://support.vald.com/hc/en-au/articles/4799421420697-View-test-data-in-VALD-Hub), [source](https://support.vald.com/hc/en-au/articles/25954041656089-Print-DynaMo-test-results), [source](https://support.vald.com/hc/en-au/articles/20656475656345-Create-a-Group-Dashboard-monitoring-chart)). Since 2026-09-28, Overview tiles support more metrics, and VALD says the tiles are no longer split by the side chosen when the test was run ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
  - **API.** Base URLs are region specific: `https://prd-aue-api-extdynamo.valdperformance.com/`, `https://prd-use-api-extdynamo.valdperformance.com/`, and `https://prd-euw-api-extdynamo.valdperformance.com/` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Authentication is OAuth2 client credentials ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Endpoints ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)):
    - `GET /v2022q2/teams/{teamId}/tests`: a page of tests (`PagedDTO` of `TestDTO`). Query: `athleteId`, `testFromUTC`, `testToUTC`, `modifiedFromUTC`, `includeRepSummaries`, `includeReps`, `page`. The KB says it returns 50 tests per page and that summaries and reps are off by default ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
    - `GET /v2022q2/teams/{teamId}/tests/{testId}`: one `TestDTO` with `repetitionTypeSummaries`, `repetitions`, `asymmetries`, and `ratios`.
    - `GET /v2022q2/teams/{teamId}/tests/{testId}/trace`: the raw recording (`forceTrace` for strength, `imuTrace` for range of motion).
    - `GET /v1/test/tests-by-modified-date?TenantId=&ModifiedFromUtc=`: a `tests` array of `TestDtoWithModifiedDate` (the `TestDTO` fields plus `modifiedDateUtc`). The KB guide does not document this endpoint. valdr uses it ([source](https://github.com/cran/valdr/blob/master/R/dynamo_tests.R)).
    - `GET /version`, `/liveness`, `/readiness`, `/diagnostics`: service status. No athlete data.
  - **Spec versus KB differences.** The KB names the path segment `{tenantId}`, while the spec names it `{teamId}`. The KB marks `modifiedFromUtc`, `testFromUtc`, and `testToUtc` as required. The spec marks only the path parameter as required. The KB writes `imutrace`, while the spec field is `imuTrace` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Since 2023-11, VALD requires the last retrieval time when you fetch tests ([source](https://support.vald.com/hc/en-au/articles/24517370929049-API-Updates-February-2024-Breaking-Changes)).
  - **valdr 4.0.0.** `get_dynamo_data()` returns profiles plus five tables: `tests`, `repetition_type_summaries`, `repetitions`, `asymmetries`, and `ratios`. `get_dynamo_tests_only()` returns the tests table. `get_dynamo_test_by_id(test_id)` returns the five tables for one test ([source](https://github.com/cran/valdr/blob/master/R/session.R), [source](https://support.vald.com/hc/en-au/articles/48730811824281-A-guide-to-using-the-valdr-R-package)). valdr has no DynaMo trace function. The by-ID call uses `/v2022q2/.../tests/{testId}`, which has no `modifiedDateUtc`, so that column is empty there ([source](https://github.com/cran/valdr/blob/master/R/dynamo_tests_by_id.R), [source](https://github.com/cran/valdr/blob/master/R/utils.R)).
  - **Beta tools.** VALD AI and VALD Connect for Power BI list DynaMo test data as supported. VALD AI excludes repetition-level and force trace data ([source](https://support.vald.com/hc/en-au/articles/56075934514585-Using-VALD-AI-for-data-analysis), [source](https://support.vald.com/hc/en-au/articles/58767784395289-Getting-started-with-VALD-Connect-in-Power-BI)).
- **Row level.**
  - `TestDTO` and valdr `tests`: one row per test. A test is one body region, one movement (or movement pair), one position, and one or both sides.
  - `RepetitionTypeSummaryDTO` and valdr `repetition_type_summaries`: one row per test, movement, and side. VALD says the `repetitionTypeSummaries` array aggregates the data from all reps ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
  - `RepetitionDTO` and valdr `repetitions`: one row per rep. `repNo` restarts for each side. Both reps in the KB strength example have `repNo` 1 ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
  - `AsymmetryDTO` and valdr `asymmetries`: one row per test and movement.
  - `RatioDTO` and valdr `ratios`: one row per test, side, and movement pair.
  - Trace: one row per sample.
  - VALD advises that in most cases you should use `repetitionTypeSummaries` results instead of the `repetitions` array ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Left and right labels.**
  - The `laterality` enum has five values: `None`, `LeftSide`, `RightSide`, `LeftThenRight`, and `RightThenLeft` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
  - On a test, `laterality` gives the sides tested and their order. VALD describes `LeftThenRight` as a test done on the left side, then on the right side. It describes `None` as a body region with no laterality, such as the neck or trunk ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
  - On summaries and reps, `laterality` is `LeftSide`, `RightSide`, or `None`. It names the athlete's side for that row. VALD says a bilateral test (`LeftThenRight` or `RightThenLeft`) always returns `repetitionTypeSummaries` for both `LeftSide` and `RightSide` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
  - Do not infer side from rep order. In the KB strength example the test is `LeftThenRight`, but the `RightSide` rep starts at 1.90 s and the `LeftSide` rep at 7.28 s ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Read the row's `laterality` field.
  - In the app, you pick the starting side as Left or Right. Neck and trunk tests have one option ([source](https://support.vald.com/hc/en-au/articles/6827647624729-Record-a-strength-test-with-DynaMo)).
  - Hub users can change side labels after upload. VALD says you can edit laterality for reps, one at a time or all at once ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes), [source](https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub)). Re-pull edited tests by `modifiedFromUTC`.
  - Some `movement` values carry Left or Right: `LateralFlexionLeft`, `LateralFlexionRight`, `RotationLeft`, `RotationRight`, and the pairs `LateralFlexionLeftLateralFlexionRight` and `RotationLeftRotationRight` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). These name a movement direction for neck or trunk, for example "Neck Rotation (Left) - Seated" ([source](https://support.vald.com/hc/en-au/articles/15257079218073-DynaMo-Lite-Test-Protocols-Neck-ROM)). They are not limb sides.
  - The `attachments` values (for example `LeftPalmPadRightCurvedPad`) and `leftAttachment` and `rightAttachment` use Left and Right too. What Left and Right mean there: Not published. Do not read them as athlete sides.
- **Test types.**
  - `testCategory` is `Strength` or `RangeofMotion` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
  - Strength modes by model ([source](https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models)): push (compression) on all models, pull (tension) on Plus and Max, fixed point on all models, grip on Plus only, and range of motion on all models. Lite has a pinch grip option that VALD says works differently from the Plus grip ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)).
  - Body regions for strength: neck, shoulder, scapula, thoracic, elbow, wrist, hand (Plus only), hip, knee, ankle, and foot. For range of motion: neck, shoulder, thoracic, elbow, wrist, hip, knee, and ankle ([source](https://support.vald.com/hc/en-au/articles/5453099730585-Test-types-available-with-DynaMo)). The API enum uses `Trunk`, not Thoracic ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
  - VALD lists over 300 test types for Lite and Max and over 400 for Plus ([source](https://support.vald.com/hc/en-au/articles/14642933112985-Compare-DynaMo-models)). Max adds the isometric mid-thigh pull and isometric belt squat ([source](https://support.vald.com/hc/en-au/articles/36405455263513-DynaMo-Max-Test-Protocols-Hip-Strength)).
  - Test name: VALD suggests `bodyRegion` + `movement` + " - " + `position`, for example "Knee Flexion - Seated". VALD advises against using the `laterality`, `leftAttachment`, or `rightAttachment` arrays to rebuild a test type name ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Which fields fill in.** Strength tests return `rangeOfMotionDegrees` of 0. Range of motion tests return 0 for every force field. Treat these zeros as "not measured", not as a real zero ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). The nullable baseline, net, 80 percent, and fixed-time RFD fields appear only in the DynaMo Max example. The Lite and Plus examples omit them ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). VALD's release note for app v1.8.4 (2024-08-15) says users see additional metrics for DynaMo Max strength tests ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)). The exact list of Max-only fields: Not published.
- **Settings that change every strength metric.**
  - Rep threshold. VALD says force below this threshold is not counted as a rep. The default is 30 N, adjustable from 10 N to 100 N ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings), [source](https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs)).
  - Sampling frequency. VALD gives 225 Hz as the default for strength testing. Users can lower it to 50 Hz ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings)). Max force samples at 1,200 Hz ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)). `analysisInfo` records the value used for each test.
  - Minimum rep duration. VALD's release note for app v1.10.0 (2025-11-06) says strength testing now uses a minimum rep duration when it records reps ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)). Value: Not published.
  - Zeroing. VALD says that if the force reading fluctuates before you apply force to the DynaMo, you click the **Zero Device** button ([source](https://support.vald.com/hc/en-au/articles/6827647624729-Record-a-strength-test-with-DynaMo)).
  - Rep deletion. Users can delete reps in the app before upload and in Hub after upload ([source](https://support.vald.com/hc/en-au/articles/26373474010009-Delete-reps-in-DynaMo), [source](https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub)). Whether summaries and asymmetry recalculate after a Hub edit: Not published.
  - Known app bugs. v1.2.1 (2022-09-14) fixed duplicate strength reps. v1.9.0 (2024-11-25) fixed deleted "ghost reps" that were uploaded in some cases ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)). `softwareInfo` holds the app version for each test.
  - Display units. The app shows N, kg, or lb. VALD says this setting does not apply to results displayed in VALD Hub ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings)). Hub has its own DynaMo Force setting: Metric (kgs), Imperial (lbs), or Scientific (N) ([source](https://support.vald.com/hc/en-au/articles/27432433786009-Customize-Unit-of-Measurement-in-VALD-Hub)). API field names state Newtons, and the KB examples are in Newtons.
- **Body mass and torque.** The DynaMo API has no body mass, limb length, lever arm, or torque field ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Per-kg and torque variants are not exported. VALD's calculators give Relative Strength = Peak Force / Body Weight (N/kg) and Torque = Peak Force x Effort Arm Length, with the effort arm measured from joint line to limb attachment in meters ([source](https://valdhealth.com/calculators)). Restated: to normalize, bring your own body mass and lever length.

### Strength metrics (rep level and summary)

#### `maxForceNewtons` (N)

This block has these fields:

- **What it measures:** The highest force in one rep (peak force).
- **Calculation:** VALD describes peak force as the maximum force generated during a test ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). VALD's general isometric definition is the maximum force registered within the testing duration ([source](https://valdperformance.com/news/isometrics-static-contractions-dynamic-applications)). Restated: peak force = the largest force sample inside the rep window. Filtering, smoothing, and whether baseline is subtracted: Not published. The Max example shows `maxForceNewtons` 185 with `baselineForceNewtons` 50.19, so this field includes baseline force ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Inputs and units:** Load cell force in Newtons. Resolution 1 N on all models ([source](https://support.vald.com/hc/en-au/article_attachments/62792928707993), [source](https://support.vald.com/hc/en-au/article_attachments/62792898708505), [source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)).
- **Variants:**
  - `RepetitionDTO.maxForceNewtons`: one rep.
  - `RepetitionTypeSummaryDTO.maxForceNewtons`: the highest rep for that side and movement (restated from the name).
  - `RepetitionTypeSummaryDTO.avgForceNewtons`: the mean across reps for that side and movement. VALD defines Mean Force as the average force calculated across multiple repetitions ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). Restated: it averages the reps' peak forces. It is not the mean force over time. Exact method: Not published.
  - Left and right: separate summary rows with `laterality` `LeftSide` and `RightSide`.
  - Per kg: not in the API.
  - Asymmetry: see `valuePercentage`.
  - Net of baseline: see `netPeakForceNewtons`.
- **What changes the number:**
  - Rep threshold, sampling frequency, and minimum rep duration (see Overview).
  - Device capacity. Lite and Plus compression top out at 1000 N, Plus tension at 2000 N, and Max at 10,000 N ([source](https://support.vald.com/hc/en-au/article_attachments/62792898708505), [source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)). The app warns Lite users about the 100 kg limit on knee extension and ankle plantar flexion (v1.3.8) ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)).
  - Handheld versus fixed setup. VALD notes that most handheld dynamometers need the assessor to apply equal and opposite forces to the tested limb, which can give variable results ([source](https://valdhealth.com/news/handheld-dynamometers-101-century-old-technology-for-the-modern-practitioner)).
  - Lever length. Long lever and short lever positions move the contact point. Hip extension prone long lever contacts just above the ankle. Short lever contacts just above the knee ([source](https://support.vald.com/hc/en-au/articles/15342037629721-DynaMo-Lite-Test-Protocols-Hip-Strength)). Force from different `position` values is not comparable.
  - Stabilization. VALD cites up to 15 percent overestimation of knee extension strength with poor stabilization ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)).
  - Joint angle. VALD lists 45, 60, and 90 degree knee extension angles with different meanings ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)).
  - Display unit settings change the number you see in the app and Hub, not the Newton fields.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers, https://valdperformance.com/news/isometrics-static-contractions-dynamic-applications, https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance, https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings, https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json

#### `impulseNewtonSeconds` (N·s)

This block has these fields:

- **What it measures:** Force accumulated over time during one rep.
- **Calculation:** Not published for this field. VALD's general definition of impulse at fixed time points is force multiplied by time, integrated from movement onset to a defined time point ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Restated: impulse = sum of (force x sample interval) across the rep window. The window start, end, and whether baseline force is included: Not published.
- **Inputs and units:** Force trace (N) and time (s). Output in N·s.
- **Variants:**
  - `RepetitionDTO.impulseNewtonSeconds`: one rep.
  - `RepetitionTypeSummaryDTO.maxImpulseNewtonSeconds`: highest rep value for the side and movement.
  - `RepetitionTypeSummaryDTO.avgImpulseNewtonSeconds`: mean across reps.
  - Net impulse at fixed times: see `netImpulseAt100msNewtonSeconds` and related fields.
- **What changes the number:** Rep window length, which depends on the rep threshold and minimum rep duration (see Overview). A longer hold gives a larger impulse at the same force. Hold duration guidance for DynaMo tests: Not published. The protocols cue "3, 2, 1 - push, push, push and relax" with no stated seconds ([source](https://support.vald.com/hc/en-au/articles/19112858914329-DynaMo-Plus-Test-Protocols-Knee-Strength)). Sampling frequency.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/news/understanding-rate-of-force-development, https://support.vald.com/hc/en-au/articles/19112858914329-DynaMo-Plus-Test-Protocols-Knee-Strength

#### `rateOfForceDevelopmentNewtonsPerSecond` (N/s)

This block has these fields:

- **What it measures:** How fast force rises during one rep.
- **Calculation:** VALD describes RFD as a measure of how rapidly force is generated over time ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). VALD also describes it as the rate at which force is produced within a given time interval (for example 0-100 ms) or within a test (for example max RFD) ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). The RFD cheat sheet gives RFD as the slope of the force-time curve, Δforce / Δtime ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf)). Which window or method this field uses: Not published. Check on the KB example (our arithmetic, not a VALD definition): it is not peak force divided by time to peak force. 84 N / 0.56 s = 150 N/s, but the field reads 341.4 N/s ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Inputs and units:** Force (N) and time (s). Output in N/s.
- **Variants:**
  - `RepetitionDTO.rateOfForceDevelopmentNewtonsPerSecond`: one rep.
  - `RepetitionTypeSummaryDTO.maxRateOfForceDevelopmentNewtonsPerSecond`: highest rep.
  - `RepetitionTypeSummaryDTO.avgRateOfForceDevelopmentNewtonsPerSecond`: mean across reps.
  - Fixed-window RFD: see `rateOfForceDevelopment150msNewtonsPerSecond` and related fields.
- **What changes the number:**
  - Sampling frequency. Lite and Plus sample force at 225 Hz, Max at 1,200 Hz, and users can lower strength sampling to 50 Hz ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings), [source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)). VALD's RFD article names only DynaMo Max among DynaMo models for RFD and states that 300 to 500 Hz suffices for most isometric RFD ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Compare RFD only within one model and sampling setting.
  - Pretension. VALD says that holding consistent pretension for 2-3 s before the assessment, to remove slack in the system, is critical for valid RFD ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). DynaMo Max can show pretension during the test (v1.8.4) ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)).
  - Cueing. VALD recommends the cue "Push as hard and fast as possible" for knee extension ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). Most DynaMo protocols cue "as hard as you can" with no speed cue ([source](https://support.vald.com/hc/en-au/articles/19112858914329-DynaMo-Plus-Test-Protocols-Knee-Strength)). The Max IMTP protocol cues "as hard and as fast as possible" ([source](https://support.vald.com/hc/en-au/articles/36405455263513-DynaMo-Max-Test-Protocols-Hip-Strength)).
- **Sources:** https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers, https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance, https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf, https://valdhealth.com/news/understanding-rate-of-force-development, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

#### `timeToPeakForceSeconds` (s)

This block has these fields:

- **What it measures:** Time from the start of the rep to peak force.
- **Calculation:** VALD describes time to peak force as a measure of how quickly peak force is reached ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). VALD's general definition in a ForceDecks context is the time from the start of movement to peak force ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Restated: time to peak force = time of peak force − time of rep onset. How DynaMo detects onset: Not published.
- **Inputs and units:** Force trace and time. Output in seconds.
- **Variants:**
  - `RepetitionDTO.timeToPeakForceSeconds`: one rep.
  - `RepetitionTypeSummaryDTO.avgTimeToPeakForceSeconds`: mean across reps.
  - `RepetitionTypeSummaryDTO.minTimeToPeakForceSeconds`: the fastest rep. Lower is faster, so the summary keeps the minimum, not the maximum.
- **What changes the number:** Pacing and strategy. VALD says time to peak force varies widely and depends on execution strategy ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Pretension, rep threshold (which sets onset), and sampling frequency. The app shows time to peak force in the rep counter since v1.0.9 ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)).
- **Sources:** https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers, https://valdhealth.com/news/understanding-rate-of-force-development, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

#### `baselineForceNewtons` (N)

This block has these fields:

- **What it measures:** The resting force on the device before the effort, such as pretension or limb weight.
- **Calculation:** Not published. The baseline window and averaging method: Not published. Field is nullable and appears in the KB DynaMo Max example only ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Inputs and units:** Force trace before onset. Newtons.
- **Variants:**
  - `RepetitionDTO.baselineForceNewtons`: one rep.
  - `RepetitionTypeSummaryDTO.avgBaselineForceNewtons`: mean across reps.
  - `RepetitionTypeSummaryDTO.maxBaselineForceNewtons`: highest rep.
- **What changes the number:** Pretension before the pull, device zeroing, and setup (strap tension, bar or belt position). VALD says DynaMo assessment protocols include a pretension phase to ensure accurate force measurement ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). A large or variable baseline changes every net metric.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance

#### `netPeakForceNewtons` (N)

This block has these fields:

- **What it measures:** Peak force above baseline.
- **Calculation:** Not published as a formula. Check on the KB example (our arithmetic): `maxForceNewtons` 185 − `baselineForceNewtons` 50.194 = 134.806, which equals `netPeakForceNewtons` 134.806 ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Restated: net peak force = peak force − baseline force.
- **Inputs and units:** Newtons.
- **Variants:**
  - `RepetitionDTO.netPeakForceNewtons`: one rep.
  - `RepetitionTypeSummaryDTO.avgNetPeakForceNewtons`: mean across reps.
  - `RepetitionTypeSummaryDTO.maxNetPeakForceNewtons`: highest rep.
  - Nullable. In KB examples it appears only for DynaMo Max.
- **What changes the number:** Everything that moves `maxForceNewtons` or `baselineForceNewtons`. Use net peak when pretension differs between tests.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

#### `netForceAt100msNewtons`, `netForceAt150msNewtons`, `netForceAt200msNewtons` (N)

This block has these fields:

- **What it measures:** Force above baseline at 100, 150, and 200 ms after the effort starts.
- **Calculation:** Not published for DynaMo. VALD's general definition in a ForceDecks context is the force produced at predefined time points from movement onset ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Restated: net force at X ms = force at (onset + X ms) − baseline force. The onset rule: Not published.
- **Inputs and units:** Force trace, baseline, and onset time. Newtons.
- **Variants:**
  - Rep: `netForceAt100msNewtons`, `netForceAt150msNewtons`, `netForceAt200msNewtons`.
  - Summary mean: `avgNetForceAt100msNewtons`, `avgNetForceAt150msNewtons`, `avgNetForceAt200msNewtons`.
  - Summary highest: `maxNetForceAt100msNewtons`, `maxNetForceAt150msNewtons`, `maxNetForceAt200msNewtons`.
  - All nullable. In KB examples they appear only for DynaMo Max.
- **What changes the number:** Onset detection, pretension, and cueing. VALD says force at fixed time points is sensitive to execution strategy (for example pretension) and clinician cueing ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). VALD links early-phase windows (0 to 150 ms) to neural drive ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Values are small in the KB example (3.3 to 8.8 N), so 1 N device resolution matters ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)).
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/news/understanding-rate-of-force-development

#### `netImpulseAt100msNewtonSeconds`, `netImpulseAt150msNewtonSeconds`, `netImpulseAt200msNewtonSeconds` (N·s)

This block has these fields:

- **What it measures:** Force above baseline accumulated over the first 100, 150, and 200 ms of the effort.
- **Calculation:** Not published for DynaMo. VALD's general definition is force multiplied by time, integrated from movement onset to a defined time point ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Restated: net impulse at X ms = sum over samples from onset to onset + X ms of (force − baseline) x sample interval. The exact subtraction and onset rule: Not published.
- **Inputs and units:** Force trace, baseline, and onset time. N·s.
- **Variants:**
  - Rep: `netImpulseAt100msNewtonSeconds`, `netImpulseAt150msNewtonSeconds`, `netImpulseAt200msNewtonSeconds`.
  - Summary mean: `avgNetImpulseAt100msNewtonSeconds`, `avgNetImpulseAt150msNewtonSeconds`, `avgNetImpulseAt200msNewtonSeconds`.
  - Summary highest: `maxNetImpulseAt100msNewtonSeconds`, `maxNetImpulseAt150msNewtonSeconds`, `maxNetImpulseAt200msNewtonSeconds`.
  - All nullable. In KB examples they appear only for DynaMo Max.
- **What changes the number:** Same as net force at fixed times. VALD says impulse at fixed time points is typically more variable than simpler timing-based RFD metrics ([source](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/news/understanding-rate-of-force-development

#### `timeTo80PercentPeakForceSeconds` (s)

This block has these fields:

- **What it measures:** Time from the start of the effort to 80 percent of peak force.
- **Calculation:** VALD defines this as the time the subject needs to reach 80% of the test's peak force ([source](https://valdperformance.com/news/isometrics-static-contractions-dynamic-applications)). For DynaMo, VALD names it "time to 80% peak force (net of baseline)" ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). Restated: find 0.8 x net peak force, then measure time from onset until net force first reaches it. The onset rule and "first crossing" detail: Not published. In the KB Max example this value (0.812 s) equals `timeToPeakForceSeconds` (0.812 s) ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Inputs and units:** Force trace, baseline, onset. Seconds.
- **Variants:**
  - `RepetitionDTO.timeTo80PercentPeakForceSeconds`: one rep.
  - `RepetitionTypeSummaryDTO.avgTimeTo80PercentPeakForceSeconds`: mean across reps.
  - `RepetitionTypeSummaryDTO.minTimeTo80PercentPeakForceSeconds`: fastest rep.
  - Nullable. In KB examples it appears only for DynaMo Max.
- **What changes the number:** VALD says DynaMo's "time to 80% peak force (net of baseline)" gives a consistent proxy for RFD when pretension varies ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). VALD rates it as more reliable than time to peak force for assessing rapid force development ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). Onset detection and sampling frequency.
- **Sources:** https://valdperformance.com/news/isometrics-static-contractions-dynamic-applications, https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance, https://valdhealth.com/news/understanding-rate-of-force-development, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

#### `rateOfForceDevelopment150msNewtonsPerSecond`, `rateOfForceDevelopment200msNewtonsPerSecond`, `rateOfForceDevelopment250msNewtonsPerSecond` (N/s)

This block has these fields:

- **What it measures:** Average rate of force rise over the first 150, 200, and 250 ms of the effort.
- **Calculation:** Not published for DynaMo. VALD's general slope definition is Δforce / Δtime ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf)). Restated: RFD over 0 to X ms = (force at onset + X ms − force at onset) / X. Check on the KB example (our arithmetic): RFD at 150 ms is 10.0 N/s, while `netForceAt150msNewtons` / 0.15 s = 22.0 N/s. So the field is not net force at 150 ms divided by 0.15 s ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). The reference force and onset rule: Not published.
- **Inputs and units:** Force trace and onset time. N/s.
- **Variants:**
  - Rep: `rateOfForceDevelopment150msNewtonsPerSecond`, `rateOfForceDevelopment200msNewtonsPerSecond`, `rateOfForceDevelopment250msNewtonsPerSecond`.
  - Summary mean: `avgRateOfForceDevelopment150msNewtonsPerSecond`, `avgRateOfForceDevelopment200msNewtonsPerSecond`, `avgRateOfForceDevelopment250msNewtonsPerSecond`.
  - Summary highest: `maxRateOfForceDevelopment150msNewtonsPerSecond`, `maxRateOfForceDevelopment200msNewtonsPerSecond`, `maxRateOfForceDevelopment250msNewtonsPerSecond`.
  - All nullable. In KB examples they appear only for DynaMo Max.
  - Note the windows differ from the net force and net impulse windows (100, 150, and 200 ms).
- **What changes the number:** VALD says early-phase RFD (0-150 ms) mainly reflects neural drive and the speed of motor unit recruitment ([source](https://valdhealth.com/news/understanding-rate-of-force-development)). The cheat sheet says early-phase RFD is "slightly less reliable" due to start detection, and late phase is slightly more reliable ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf)). Pretension, cueing, sampling frequency.
- **Sources:** https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/RFD.pdf, https://valdhealth.com/news/understanding-rate-of-force-development, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

### Range of motion metric

#### `rangeOfMotionDegrees` (degrees)

This block has these fields:

- **What it measures:** The joint angle range covered in one range of motion rep, from the device's inertial sensor.
- **Calculation:** VALD describes ROM as a measure of the full movement potential of a joint ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). How the angle comes from the IMU orientation, the reference axis, and the sign convention: Not published. The KB example for seated knee extension reads −32.04 degrees, so values can be negative ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Strength tests report 0.
- **Inputs and units:** 9-axis IMU (accelerometer, gyroscope, magnetometer) sampled at 225 Hz on all models ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009), [source](https://support.vald.com/hc/en-au/article_attachments/62792928707993)). Degrees.
- **Variants:**
  - `RepetitionDTO.rangeOfMotionDegrees`: one rep.
  - `RepetitionTypeSummaryDTO.maxRangeOfMotionDegrees`: "max" rep. With negative values, whether "max" means largest signed value or largest magnitude: Not published. In the one-rep example both are −32.04.
  - `RepetitionTypeSummaryDTO.avgRangeOfMotionDegrees`: mean across reps.
  - Left and right: separate summary rows by `laterality`. Range of motion asymmetry: the KB range of motion example returns an empty `asymmetries` array for a one-side test. Whether DynaMo returns range of motion asymmetry for two-side tests: Not published. The app shows asymmetry between sides for passive range of motion in a VALD case study ([source](https://valdhealth.com/news/post-surgical-shoulder-rehab-for-a-professional-baseball-pitcher)).
- **What changes the number:**
  - Detection mode. Users choose Auto Detect or Manual. VALD recommends Manual mode for better control over the start and end of movements ([source](https://support.vald.com/hc/en-au/articles/6751104055833-Record-a-range-of-motion-ROM-test-with-DynaMo)). In Manual mode you click Start and Finish for each rep. In Auto mode the patient must be in the start position when you click Ready to test ([source](https://support.vald.com/hc/en-au/articles/6751104055833-Record-a-range-of-motion-ROM-test-with-DynaMo)).
  - Start angle threshold. VALD gives 10 degrees as the default threshold for a range of motion repetition. Users can change it under ROM Settings ([source](https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs)).
  - Sampling. VALD says the sampling frequency for range of motion tests cannot be customised ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings)).
  - Device placement. The device is held, strapped with the range of motion strap, or held by the examiner against the limb ([source](https://support.vald.com/hc/en-au/articles/38449708425369-DynaMo-Max-system-hardware)). Protocols cue "keeping the DynaMo Lite as still as possible" ([source](https://support.vald.com/hc/en-au/articles/15416619683609-DynaMo-Lite-Test-Protocols-Knee-ROM)).
  - Position. The same movement in seated, supine, prone, or long lever positions is a different test.
- **Sources:** https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://support.vald.com/hc/en-au/articles/6751104055833-Record-a-range-of-motion-ROM-test-with-DynaMo, https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs, https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings, https://support.vald.com/hc/en-au/article_attachments/62792898698009

### Rep timing and counts

#### `startOffsetSeconds` and `durationSeconds` on `RepetitionDTO` (s)

This block has these fields:

- **What it measures:** When a rep starts within the recording, and how long the rep lasts.
- **Calculation:** Not published. Restated from the names: `startOffsetSeconds` = rep start time − test start time. `durationSeconds` = rep end time − rep start time. How start and end are detected: Not published. For strength, the rep threshold and minimum rep duration apply (see Overview). For range of motion, Auto Detect or Manual Start and Finish apply.
- **Inputs and units:** Seconds.
- **Variants:** Rep level only. Use `startOffsetSeconds` to cut the matching window from the trace. The trace's own `startTimeUTC` versus the test's `startTimeUTC`: relationship Not published.
- **What changes the number:** Rep threshold (default 30 N, 10 to 100 N), minimum rep duration (since app v1.10.0), and range of motion detection mode ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings), [source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes), [source](https://support.vald.com/hc/en-au/articles/6751104055833-Record-a-range-of-motion-ROM-test-with-DynaMo)).
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json

#### `repCount` (count)

This block has these fields:

- **What it measures:** Number of reps kept for one side and movement.
- **Calculation:** VALD says the summaries include a `repCount` that indicates how many reps were performed for each laterality or side ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Restated: count of `RepetitionDTO` rows with that movement and laterality. Whether deleted reps are excluded: reps deleted in the app are removed before upload ([source](https://support.vald.com/hc/en-au/articles/26373474010009-Delete-reps-in-DynaMo)). App v1.9.0 fixed a bug that uploaded some deleted reps ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)).
- **Inputs and units:** Integer.
- **Variants:** One per summary row. Left and right counts can differ. The app lets you record "any number of repetitions" per side ([source](https://support.vald.com/hc/en-au/articles/6827647624729-Record-a-strength-test-with-DynaMo)). Recommended rep count: Not published.
- **What changes the number:** Rep threshold, minimum rep duration, rep deletion in app or Hub.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://support.vald.com/hc/en-au/articles/26373474010009-Delete-reps-in-DynaMo

### Test-level results

#### `valuePercentage` on `AsymmetryDTO` (%)

This block has these fields:

- **What it measures:** The percentage difference between left and right for one movement in a test.
- **Calculation:** Not published for DynaMo. VALD describes asymmetry as a way to identify strength imbalances between limbs or movements ([source](https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers)). VALD's calculator formula is Asymmetry = (Right Value − Left Value) / Higher Value x 100 ([source](https://valdhealth.com/calculators), [source](https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making)). VALD does not say DynaMo uses this formula. Check on the KB example (our arithmetic): left max force 84 N, right 73.1 N, `valuePercentage` −13. (73.1 − 84) / 84 x 100 = −12.98, which rounds to −13 ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). The example fits the calculator formula. It also fits (Right − Left) / Left, because left is the higher side here. Restated: in this example a negative value means the right side was lower. Which metric feeds it (max or average force), rounding, and the sign rule in general: Not published. The example has one rep per side, so max and average are the same.
- **Inputs and units:** Left and right values for one movement. Percent. The spec type is a double; the example shows a whole number.
- **Variants:**
  - One row per movement in `asymmetries`. Each row has `movement` and `valuePercentage`, with no side and no metric name ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
  - Empty for one-side tests and for no-laterality tests in the KB examples.
  - VALD's knee extension article lists "Peak Force Asymmetry (%)" for DynaMo and ForceFrame, described as the percentage difference in peak force capacity between limbs ([source](https://valdhealth.com/news/knee-extension-strength-assessment-execution-and-clinical-significance)). Whether that equals this API field: Not published.
  - If you compute your own asymmetry from summary rows, state the formula and the metric you used.
- **What changes the number:** Everything that moves peak force on either side. Side label edits in Hub. App v1.1.1 (2022-07-01) changed it. VALD's release note says the asymmetry calculation for strength tests on the test summary screen was updated ([source](https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes)). Details of the change: Not published. Normative comparisons for asymmetry are not split by sex ([source](https://support.vald.com/hc/en-au/articles/16120582173337-How-is-normative-data-calculated)).
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/calculators, https://valdhealth.com/news/msk-calculators-practical-tools-for-clinical-decision-making, https://valdhealth.com/news/buyers-guide-to-handheld-dynamometers, https://support.vald.com/hc/en-au/articles/29596387051545-DynaMo-iOS-and-Android-Release-Notes

#### `value` on `RatioDTO` (ratio, unitless)

This block has these fields:

- **What it measures:** A ratio between two movements on one side, for example from a multi-movement test.
- **Calculation:** Not published. Each row carries `laterality`, `numeratorMovement`, `denominatorMovement`, and `value` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Restated from the field names only: value = (metric for numerator movement) / (metric for denominator movement) on that side. Which metric is used (max or average force) and whether the result is a fraction or a percentage: Not published. Every KB example returns an empty `ratios` array ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). VALD's Joint Ratio calculator uses Agonist MVIC Peak Force / Antagonist MVIC Peak Force ([source](https://valdhealth.com/calculators)). VALD does not say DynaMo uses it.
- **Inputs and units:** Two movements on one side. Unitless.
- **Variants:** One row per side and movement pair. Multi-movement tests use paired `movement` values such as `InternalRotationExternalRotation` or `FlexionExtension` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Which tests produce ratios: Not published.
- **What changes the number:** The order of numerator and denominator. Check `numeratorMovement` before you compare with a published ratio such as ER:IR. Position and lever arm of each movement.
- **Sources:** https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://valdhealth.com/calculators

#### `durationSeconds` on `TestDTO` (s)

This block has these fields:

- **What it measures:** Length of the whole test recording.
- **Calculation:** Not published. KB examples range from 8.4 s to 82.1 s ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **Inputs and units:** Seconds.
- **Variants:** Test level only. Not a performance metric. Use it to sanity check trace length.
- **What changes the number:** Time spent between reps and sides.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

### Trace (`/v2022q2/teams/{teamId}/tests/{testId}/trace`)

#### `forceTrace[].forceNewtons` with `forceTrace[].timeSeconds` (N, s)

This block has these fields:

- **What it measures:** The raw force signal of a strength test.
- **Calculation:** VALD says strength tests return force in Newtons and time in seconds within the `forceTrace` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Filtering: Not published.
- **Inputs and units:** Force in N. Time in s from the trace start. In the KB example, time steps are 0.000833 s, which is 1,200 Hz (Max) ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Lite and Plus default to 225 Hz ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings)).
- **Variants:** One array per test. It holds both sides of a two-side test. Split it by rep using `startOffsetSeconds` and `durationSeconds`. Hub does not export DynaMo traces ([source](https://support.vald.com/hc/en-au/articles/4799506027929-Export-Force-Trace-Data-from-VALD-Hub)). valdr does not fetch them.
- **What changes the number:** Zeroing. The KB example shows resting values from −3 N to +5 N in 0.5 N steps, though spec sheets list 1 N resolution ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)). Sampling setting.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json

#### `imuTrace[].orientation` (`x`, `y`, `z`, `w`) with `imuTrace[].timeSeconds` (unitless quaternion, s)

This block has these fields:

- **What it measures:** Device orientation over time during a range of motion test.
- **Calculation:** VALD says range of motion tests return the IMU quaternion and time in seconds in the `imutrace` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Restated: each sample is a unit quaternion (x, y, z, w) for the device's rotation. Reference frame, axis order, handedness, and how DynaMo turns it into `rangeOfMotionDegrees`: Not published. The KB shows no non-empty IMU example.
- **Inputs and units:** Floats with no unit. Time in s. IMU sampled at 225 Hz on all models ([source](https://support.vald.com/hc/en-au/article_attachments/62792898698009)).
- **Variants:** One array per test. The KB field name is `imutrace`; the spec name is `imuTrace` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
- **What changes the number:** Device placement on the limb and movement of the device during the test.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/article_attachments/62792898698009

### Test context

#### `analysisInfo` (text)

This block has these fields:

- **What it measures:** The analysis settings used for the test.
- **Calculation:** Format Not published. KB examples read `Dynamo.Analysis;1.0.0.0;225Hz;30N;Auto ROM Detection` (Lite and Plus), `Dynamo.Analysis;1.0.0.0;1200Hz;30N;Auto ROM Detection` (Max), and `Dynamo.Analysis;99.9.9.0;225Hz;30N;Auto ROM Detection` (range of motion example) ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Restated: the parts match these documented settings, in order: analysis name, analysis version, sampling frequency, strength rep threshold, and range of motion detection mode ([source](https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings), [source](https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs)). The value for Manual range of motion mode: Not published.
- **Inputs and units:** Semicolon-separated text.
- **Variants:** One per test.
- **What changes the number:** App settings at test time. Parse the Hz and N parts and do not mix tests with different settings in one trend.
- **Sources:** https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API, https://support.vald.com/hc/en-au/articles/25956300111129-Customize-your-DynaMo-app-settings

#### Enum fields

The enum and context fields on `TestDTO` hold these values:

- **`testCategory`:** `Strength` or `RangeofMotion`. Use it to decide which metric fields carry data ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)).
- **`bodyRegion`:** `Neck`, `Shoulder`, `Trunk`, `Hip`, `Elbow`, `Wrist`, `Hand`, `Knee`, `Ankle`, `Foot`, `Scapula` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)).
- **`movement`:** 58 values. They include single movements (`Flexion`, `ExternalRotation`), paired movements for multi-movement tests (`InternalRotationExternalRotation`, `FlexionExtension`, `AdductionAbduction`), direction movements for neck and trunk (`RotationLeft`, `LateralFlexionRight`), Max tests (`IsometricMidThighPull`, `IsometricBeltSquat`), shoulder tests (`ISOITest`, `ISOYTest`, `ISOTTest`), grip and pinch tests, and `Custom` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Multi-movement tests can run in movement order or limb order ([source](https://support.vald.com/hc/en-au/articles/10292277634201-DynaMo-FAQs)). How a paired test-level value maps to rep `movement` values: Not published.
- **`position`:** 85 values, such as `Seated`, `Prone`, `Supine90DegreesHipFlexion`, `SeatedLongLever`, `SeatedShortLever`, `Knee45Degrees`, `MidThigh`, and `Custom` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Values that start with a number carry a `p` prefix, for example `p90DegreesAbduction`. Some values are near duplicates, such as `p90DegreeElbowFlexionWristNeutral` and `p90DegreesElbowFlexionWristNeutral`. Group by exact value and check near duplicates by hand. Hub users can change a test's position after upload ([source](https://support.vald.com/hc/en-au/articles/16312411866009-Edit-or-delete-test-rep-data-in-VALD-Hub)).
- **`customPosition`:** free text. Use: Not published. KB examples show an empty string.
- **`laterality`:** see Left and right labels.
- **`attachments`, `leftAttachment`, `rightAttachment`:** `attachments` combines two ends, such as `LeftPalmPadRightCurvedPad` or `LeftTensionLinkRightTensionLink`. `leftAttachment` and `rightAttachment` use `None`, `CurvedPad`, `FlatPad`, `PalmPad`, `TensionLink`, `GripInner`, `GripOuter` ([source](https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json)). Plus Smart Attachments use NFC to detect the attachment and the device end ([source](https://support.vald.com/hc/en-au/articles/5457903678745-Connect-your-DynaMo-attachments)). Treat these fields with care:
  - The KB metadata example shows `"attachments": 0`, a number, while the spec defines a string enum.
  - KB examples show `leftAttachment` and `rightAttachment` as `None` while `attachments` reads `LeftPalmPadRightCurvedPad`.
  - The Max IMTP example reads `LeftPalmPadRightCurvedPad`, but the IMTP uses a tension strap and the Max kit lists no palm pad ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API), [source](https://support.vald.com/hc/en-au/articles/36405455263513-DynaMo-Max-Test-Protocols-Hip-Strength), [source](https://support.vald.com/hc/en-au/articles/38449708425369-DynaMo-Max-system-hardware)).
- **`hardwareInfo`:** for example `DynaMoLite-00784;DYNL-221221-FW0R2-HW0R5`, `DynaMo-00197;DYNO-220426-FW1R4-HW1R0`, and `DynaMoMax-00000;DYNM-240729-FW0R1-HW0R7` ([source](https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API)). Restated: the first part names the model and unit. Use it to separate Lite, Plus, and Max data, because sampling rate and available fields differ. Full format: Not published.
- **`softwareInfo`:** for example `iOS;iPhone12,1;17.5.1;1.8.4;#99`. Restated: platform, phone model, OS version, app version, build. Use the app version to match release note changes. Full format: Not published.

### Identifiers and context fields

The following table lists the identifier and context fields by endpoint or object:

| Endpoint or object | Fields |
|---|---|
| `TestDTO` (tests list, test by ID) | `id`, `athleteId`, `teamId`, `startTimeUTC`, `analysedDateUTC`, plus context fields `testCategory`, `bodyRegion`, `movement`, `position`, `customPosition`, `laterality`, `attachments`, `leftAttachment`, `rightAttachment`, `hardwareInfo`, `softwareInfo`, `analysisInfo` |
| `TestDtoWithModifiedDate` (`/v1/test/tests-by-modified-date`) | All `TestDTO` fields plus `modifiedDateUtc` |
| `PagedDTO` (tests list) | `items`, `currentPage`, `totalItems`, `totalPages` |
| `RepetitionTypeSummaryDTO` | `id`, `testId`, `movement`, `laterality` |
| `RepetitionDTO` | `id`, `testId`, `movement`, `laterality`, `repNo` |
| `AsymmetryDTO` | `movement` (no `testId`; valdr adds the parent test `id` as `testId`) |
| `RatioDTO` | `laterality`, `numeratorMovement`, `denominatorMovement` (valdr adds `testId`) |
| `GetTestTraceResponse` | `id`, `profileId`, `tenantId`, `startTimeUTC`. Trace uses `profileId` and `tenantId` where tests use `athleteId` and `teamId`. The KB calls the team path segment `tenantId`. |

Sources: https://prd-use-api-extdynamo.valdperformance.com/swagger/v1/swagger.json, https://github.com/cran/valdr/blob/master/R/utils.R, https://support.vald.com/hc/en-au/articles/30388298175385-A-guide-to-using-the-External-DynaMo-API

### Not published in the public sources

The public sources checked do not publish these details:

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

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
