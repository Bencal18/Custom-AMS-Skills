# VALD ForceDecks and NordBord metrics: NordBord

This page explains how VALD NordBord calculates each metric on its test and training exports. It covers NordBord test metrics and training mode metrics, with 38 metric blocks. Checked against: the VALD NordBord Test Guide, the NordBord Technical Specifications, the External NordBord API specification (`v1`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

This page is part of [VALD ForceDecks and NordBord metrics](vald-forcedecks-nordbord.md). The index explains how to read each block, and it holds the event and term glossary, the factors that change the numbers, the conflicts in VALD's own sources, the Not published list, the worked example, and the sources with access dates. VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](vald-other-products.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](hawkin-dynamics.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](hawkin-dynamics.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Metric blocks

### NordBord overview

NordBord measures force from a load cell in each ankle hook, and calculates torque and impulse ([What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)). Test types: Nordic and Razor (eccentric, bilateral rep detection), ISO Prone (0°), ISO 30° and ISO 60° (isometric, unilateral rep detection), and Custom ([NordBord Test Types](https://support.vald.com/hc/en-au/articles/4812656102169-NordBord-Test-Types)).

Key settings:

- Rep threshold: a rep starts when force goes above the threshold, then the app looks for a peak. Example: 150 N ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)).
- Impulse threshold: impulse is counted only above it. Example: 25 N ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)).
- Knee position: needed for torque; record where the knees touch the pad with the hooks at the top of the shoe ([Select a NordBord knee position](https://support.vald.com/hc/en-au/articles/4812416471065-Select-a-NordBord-knee-position)).
- Sampling: 50 Hz default up to 400 Hz on the spec sheet; resolution 1 N; capacity 2,000 N per sensor ([NordBord Technical Specifications](https://support.vald.com/hc/en-au/article_attachments/29041300739609)). The iOS app raised sampling to 400 Hz to capture new metrics ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- Body weight: entered in the app or pulled from VALD Hub, needed for per-kg metrics ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- Defaults for the thresholds: Not published.

Exports: the test summary API returns per-leg max force, average force, torque, impulse, calibration and repetitions; a second endpoint returns additional metrics ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). The trace endpoint returns `ticks`, `leftForce` and `rightForce` ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json)). VALD Hub exports test and training data as CSV ([Export Test Data from VALD Hub](https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). VALD Hub added `Peak Force / Body Mass`, `Torque / Body Mass`, `Time to Peak Force`, RFD (isometric tests only), RFD at time points (isometric only) and impulse at time points for new tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).

VALD-stated count: Not published. This page covers every field in the public NordBord API specification.

### NordBord test metrics

#### `leftMaxForce`, `rightMaxForce`

This metric has these fields:

- **What it measures:** The highest force of any rep for each leg.
- **Window or phase:** Not published.
- **Calculation:** VALD says `leftMaxForce` is the maximum left leg force, drawn in blue, and `rightMaxForce` is the maximum right leg force, drawn in orange ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). Restatement: `max over selected reps of peak force`, per leg.
- **Inputs:** Force from each ankle-hook load cell.
- **Units:** N.
- **Variants:** Left and right fields (`left...`, `right...`). API fields `leftMaxForce`, `rightMaxForce` ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sensor zeroing; hook alignment; rep selection; technique ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftAvgForce`, `rightAvgForce`

This metric has these fields:

- **What it measures:** The average of the rep peaks for each leg.
- **Window or phase:** Peaks of all reps performed during the test, per leg ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). The metric's definition names this window ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)).
- **Calculation:** VALD defines this metric as the average, which is the mean of the peaks across all reps performed in the test ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). Restatement: `mean of per-rep peak force`, per leg.
- **Inputs:** Per-rep peak force.
- **Units:** N.
- **Variants:** Left and right fields (`left...`, `right...`). API fields `leftAvgForce`, `rightAvgForce` ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). The iOS app lets you switch the display between Peak and Average ([Record a test in NordBord iOS](https://support.vald.com/hc/en-au/articles/30033699909017-Record-a-test-in-NordBord-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sensor zeroing; rep selection ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Record a test in NordBord iOS](https://support.vald.com/hc/en-au/articles/30033699909017-Record-a-test-in-NordBord-iOS).

#### `Imbalance (maximum force)`

This metric has these fields:

- **What it measures:** Left versus right difference in maximum force.
- **Window or phase:** Not published.
- **Calculation:** VALD describes it as the imbalance, which is how far apart the left and right maximums are as a percentage, displayed above ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). Restatement: VALD does not publish the NordBord imbalance formula. The ForceDecks glossary asymmetry formula is `(L - R) / max(L, R) * 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); a VALD research summary computed hamstring asymmetry as `|L - R| / (L + R)` ([Eccentric Hamstring Strength research summary](https://valdperformance.com/news/eccentric-hamstring-strength)). Which one the NordBord app uses is not published.
- **Inputs:** Left and right max force.
- **Units:** %.
- **Variants:** Not an API field; app display.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sensor zeroing; rep selection ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Eccentric Hamstring Strength research summary](https://valdperformance.com/news/eccentric-hamstring-strength).

#### `Imbalance (average force)`

This metric has these fields:

- **What it measures:** Left versus right difference in average force.
- **Window or phase:** Peaks of all reps performed during the test, per leg ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). The metric's definition names this window ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)).
- **Calculation:** VALD describes it as the imbalance, which is how far apart the left and right averages are as a percentage, displayed above ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App)). Restatement: Formula not published (see Imbalance (max)).
- **Inputs:** Left and right average force.
- **Units:** %.
- **Variants:** Not an API field; app display.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; rep selection ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App).

#### `leftTorque`, `rightTorque`

This metric has these fields:

- **What it measures:** Knee-flexor torque: force times the knee-to-hook lever.
- **Window or phase:** Not published.
- **Calculation:** VALD defines this metric as torque equal to Force x Length, where Length is taken from Knee Position ([What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)). Restatement: `Torque = F * L`, where `L` is the knee-joint-to-ankle-hook distance approximated from the knee position setting. In VALD's API examples, torque divided by max force gives 0.2925 m and 0.3735 m (see [Arithmetic checks on numbers VALD publishes](vald-forcedecks-nordbord.md#arithmetic-checks-on-numbers-vald-publishes)), so torque uses max force.
- **Inputs:** Max force, knee position.
- **Units:** Nm.
- **Variants:** Left and right fields (`left...`, `right...`). Only shown when a knee position is selected ([Record a test in NordBord iOS](https://support.vald.com/hc/en-au/articles/30033699909017-Record-a-test-in-NordBord-iOS), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Knee position setting; rep threshold; sensor zeroing ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)). Moving the body forward in ISO Prone changes the hook contact point and the torque calculation ([VALD NordBord Test Guide p.9](https://support.vald.com/hc/en-au/article_attachments/17161683969817/VALD_NordBord_Test_Guide.pdf)).
- **Sources:** [What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure), [Record a test in NordBord iOS](https://support.vald.com/hc/en-au/articles/30033699909017-Record-a-test-in-NordBord-iOS), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes), [VALD NordBord Test Guide p.9](https://support.vald.com/hc/en-au/article_attachments/17161683969817/VALD_NordBord_Test_Guide.pdf).

#### `leftImpulse`, `rightImpulse`

This metric has these fields:

- **What it measures:** Area under the force curve while above the impulse threshold.
- **Window or phase:** Periods when force is above the impulse threshold: NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)). Whether the value covers one rep or all reps is not published.
- **Calculation:** VALD defines this metric as impulse equal to Force x Time, leaving out any periods that fall below Impulse Threshold ([What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)). Restatement: `∫ F dt` over the test while `F > impulse threshold`. Whether it sums all reps or reports a per-rep value is not published; VALD notes longer contractions give larger impulse ([What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)).
- **Inputs:** Force, impulse threshold.
- **Units:** Ns.
- **Variants:** Left and right fields (`left...`, `right...`). API fields `leftImpulse`, `rightImpulse` ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Impulse threshold; rep threshold; rep selection ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftCalibration`, `rightCalibration`

This metric has these fields:

- **What it measures:** A value stored with each test for each sensor; its meaning is not published.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. VALD's API guide example payloads show `leftCalibration` and `rightCalibration` as 0 in some tests and 1.0165 and 1.0118 in another ([NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). What the value means: Not published.
- **Inputs:** Device calibration.
- **Units:** Not published.
- **Variants:** Left and right fields (`left...`, `right...`). API fields only ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Not published.
- **Sources:** [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json).

#### `leftRepetitions`, `rightRepetitions`

This metric has these fields:

- **What it measures:** Number of reps detected per leg.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Count of detected reps (restatement of the field name).
- **Inputs:** Rep detection.
- **Units:** count.
- **Variants:** Left and right fields (`left...`, `right...`). ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; rep selection ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `rightAvgForcePerKg`

This metric has these fields:

- **What it measures:** Peak force relative to body mass.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published; field names imply max force divided by body mass.
- **Inputs:** Max force, body weight.
- **Units:** N/kg (inferred).
- **Variants:** Left and right fields (`left...`, `right...`). Max and average versions: `leftMaxForcePerKg`, `leftAvgForcePerKg` and right equivalents ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). App name `Peak Force / Body Mass` ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Entered body weight; rep threshold ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes).

#### `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg`

This metric has these fields:

- **What it measures:** Torque relative to body mass.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. In the API example, `MaxTorquePerKg / MaxForcePerKg` equals 0.3015 m on both sides (see [Arithmetic checks on numbers VALD publishes](vald-forcedecks-nordbord.md#arithmetic-checks-on-numbers-vald-publishes)), consistent with torque per kg = force per kg x lever length.
- **Inputs:** Torque, body weight.
- **Units:** N m/kg (inferred).
- **Variants:** Left and right fields (`left...`, `right...`). Max and average versions ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). App name `Torque / Body Mass` ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Entered body weight; knee position setting ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes).

#### `leftMaxRFDNewtonsPerSecond`, `rightMaxRFDNewtonsPerSecond`, `leftAvgRFDNewtonsPerSecond`, `rightAvgRFDNewtonsPerSecond`

This metric has these fields:

- **What it measures:** The fastest rise in force.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. The window and method behind 'Peak RFD' are not published.
- **Inputs:** Force at up to 400 Hz.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and average versions (`leftMaxRFDNewtonsPerSecond`, `leftAvgRFDNewtonsPerSecond`) ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits RFD metrics to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Sampling rate; rep threshold ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMinTimeToMaxForceSeconds`, `rightMinTimeToMaxForceSeconds`, `leftAvgTimeToMaxForceSeconds`, `rightAvgTimeToMaxForceSeconds`

This metric has these fields:

- **What it measures:** Time to reach peak force.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. The API gives the minimum and average across reps (`leftMinTimeToMaxForceSeconds`, `leftAvgTimeToMaxForceSeconds`).
- **Inputs:** Force, rep start.
- **Units:** s.
- **Variants:** Left and right fields (`left...`, `right...`). ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxRFD50msNewtonsPerSecond`, `rightMaxRFD50msNewtonsPerSecond`, `leftAvgRFD50msNewtonsPerSecond`, `rightAvgRFD50msNewtonsPerSecond`

This metric has these fields:

- **What it measures:** Rate of force rise over the first 50 ms of the rep.
- **Window or phase:** 50 ms, from the field name. The start event is not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply the RFD over the first 50 ms, reported as the best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits time-point RFD to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMaxRFD100msNewtonsPerSecond`, `rightMaxRFD100msNewtonsPerSecond`, `leftAvgRFD100msNewtonsPerSecond`, `rightAvgRFD100msNewtonsPerSecond`

This metric has these fields:

- **What it measures:** Rate of force rise over the first 100 ms of the rep.
- **Window or phase:** 100 ms, from the field name. The start event is not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply the RFD over the first 100 ms, reported as the best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits time-point RFD to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMaxRFD150msNewtonsPerSecond`, `rightMaxRFD150msNewtonsPerSecond`, `leftAvgRFD150msNewtonsPerSecond`, `rightAvgRFD150msNewtonsPerSecond`

This metric has these fields:

- **What it measures:** Rate of force rise over the first 150 ms of the rep.
- **Window or phase:** 150 ms, from the field name. The start event is not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply the RFD over the first 150 ms, reported as the best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits time-point RFD to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMaxRFD200msNewtonsPerSecond`, `rightMaxRFD200msNewtonsPerSecond`, `leftAvgRFD200msNewtonsPerSecond`, `rightAvgRFD200msNewtonsPerSecond`

This metric has these fields:

- **What it measures:** Rate of force rise over the first 200 ms of the rep.
- **Window or phase:** 200 ms, from the field name. The start event is not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply the RFD over the first 200 ms, reported as the best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits time-point RFD to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMaxRFD250msNewtonsPerSecond`, `rightMaxRFD250msNewtonsPerSecond`, `leftAvgRFD250msNewtonsPerSecond`, `rightAvgRFD250msNewtonsPerSecond`

This metric has these fields:

- **What it measures:** Rate of force rise over the first 250 ms of the rep.
- **Window or phase:** 250 ms, from the field name. The start event is not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply the RFD over the first 250 ms, reported as the best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N/s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Hub limits time-point RFD to isometric tests ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `leftMaxImpulse50msNewtonSeconds`, `rightMaxImpulse50msNewtonSeconds`, `leftAvgImpulse50msNewtonSeconds`, `rightAvgImpulse50msNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the first 50 ms of the rep.
- **Window or phase:** 50 ms, from the field name. VALD says NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)); VALD does not say whether this window starts there.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply impulse over the first 50 ms, best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; impulse threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxImpulse100msNewtonSeconds`, `rightMaxImpulse100msNewtonSeconds`, `leftAvgImpulse100msNewtonSeconds`, `rightAvgImpulse100msNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the first 100 ms of the rep.
- **Window or phase:** 100 ms, from the field name. VALD says NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)); VALD does not say whether this window starts there.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply impulse over the first 100 ms, best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; impulse threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxImpulse150msNewtonSeconds`, `rightMaxImpulse150msNewtonSeconds`, `leftAvgImpulse150msNewtonSeconds`, `rightAvgImpulse150msNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the first 150 ms of the rep.
- **Window or phase:** 150 ms, from the field name. VALD says NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)); VALD does not say whether this window starts there.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply impulse over the first 150 ms, best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; impulse threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxImpulse200msNewtonSeconds`, `rightMaxImpulse200msNewtonSeconds`, `leftAvgImpulse200msNewtonSeconds`, `rightAvgImpulse200msNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the first 200 ms of the rep.
- **Window or phase:** 200 ms, from the field name. VALD says NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)); VALD does not say whether this window starts there.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply impulse over the first 200 ms, best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; impulse threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftMaxImpulse250msNewtonSeconds`, `rightMaxImpulse250msNewtonSeconds`, `leftAvgImpulse250msNewtonSeconds`, `rightAvgImpulse250msNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the first 250 ms of the rep.
- **Window or phase:** 250 ms, from the field name. VALD says NordBord starts calculating impulse when force goes above the impulse threshold ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)); VALD does not say whether this window starts there.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Field names imply impulse over the first 250 ms, best (Max) and average (Avg) across reps.
- **Inputs:** Force, rep start.
- **Units:** N s.
- **Variants:** Left and right fields (`left...`, `right...`). Max and Avg fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json) (`/tests/{testId}/metrics`), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold; impulse threshold; sampling rate ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

### NordBord training mode metrics

Training mode stores session, exercise and repetition records for eccentric and isometric programs ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). Eccentric programs use a training threshold and a target zone; isometric programs use a training zone around a target force ([Create a training program in NordBord iOS](https://support.vald.com/hc/en-au/articles/37292091781657-Create-a-training-program-in-NordBord-iOS)).

#### `totalRepsCompleted`, `totalRepsAboveThreshold`, `totalRepsInTargetZone`

This metric has these fields:

- **What it measures:** How many eccentric reps were done, and how many crossed the threshold or entered the target zone.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Training threshold, target zone.
- **Units:** count.
- **Variants:** Eccentric exercise-session fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Health lists 'Repetitions completed', 'Repetitions above threshold' and 'Repetitions in the target zone' under Quantity Metrics ([Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2).

#### `totalImpulseInTargetZoneNewtonSeconds`, `leftImpulseInTargetZoneNewtonSeconds`, `rightImpulseInTargetZoneNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse produced while force was inside the target zone.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, target zone.
- **Units:** N s.
- **Variants:** Session total and per-rep left and right fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Health lists 'Total impulse in target zone' under Quality Metrics in Target Zone ([Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2).

#### `totalImpulseInTargetZoneAsymmetryPercentage`

This metric has these fields:

- **What it measures:** Left-right difference in target-zone impulse.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Formula not published.
- **Inputs:** Left and right target-zone impulse.
- **Units:** %.
- **Variants:** Session field ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `totalDurationInTargetZoneSeconds`, `durationInTargetZoneSeconds`, `leftTimeInTargetZoneSeconds`, `rightTimeInTargetZoneSeconds`

This metric has these fields:

- **What it measures:** Time spent inside the target zone.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, target zone.
- **Units:** s.
- **Variants:** Session and per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `totalImpulseAboveThresholdNewtonSeconds`, `leftImpulseAboveThresholdNewtonSeconds`, `rightImpulseAboveThresholdNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse produced while force was above the training threshold.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, training threshold.
- **Units:** N s.
- **Variants:** Session and per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Health lists 'Total impulse above threshold' under Quality Metrics Above Threshold ([Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2).

#### `totalImpulseAboveThresholdAsymmetryPercentage`

This metric has these fields:

- **What it measures:** Left-right difference in impulse above threshold.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Formula not published.
- **Inputs:** Left and right impulse above threshold.
- **Units:** %.
- **Variants:** Session field ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `totalDurationAboveThresholdSeconds`, `durationAboveThresholdSeconds`, `leftTimeAboveThresholdSeconds`, `rightTimeAboveThresholdSeconds`

This metric has these fields:

- **What it measures:** Time spent above the training threshold.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, training threshold.
- **Units:** s.
- **Variants:** Session and per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Health lists 'Time above threshold' under Quality Metrics Above Threshold ([Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2).

#### `leftImpulseBelowThresholdNewtonSeconds`, `rightImpulseBelowThresholdNewtonSeconds`, `leftTimeBelowThresholdSeconds`, `rightTimeBelowThresholdSeconds`, `durationBelowThresholdSeconds`

This metric has these fields:

- **What it measures:** Impulse and time while force was below the training threshold.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, training threshold.
- **Units:** N s, s.
- **Variants:** Per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftImpulseBeforePeakNewtonSeconds`, `rightImpulseBeforePeakNewtonSeconds`, `leftImpulseAfterPeakNewtonSeconds`, `rightImpulseAfterPeakNewtonSeconds`, `leftImpulseAboveThresholdBeforePeakNewtonSeconds`, `rightImpulseAboveThresholdBeforePeakNewtonSeconds`, `leftImpulseAboveThresholdAfterPeakNewtonSeconds`, `rightImpulseAboveThresholdAfterPeakNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse split at the moment of peak force, overall and above threshold.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, peak time, threshold.
- **Units:** N s.
- **Variants:** Per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). VALD Health lists 'Impulse above threshold and before peak force' and 'Impulse above threshold and after peak force' under Quality Metrics with Reference to Peak Force ([Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [Understanding the Nordic Hamstring Exercise: Part 2](https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2).

#### `leftPeakForceNewtons`, `rightPeakForceNewtons`, `timeToPeakSeconds`, `leftTimeToPeakSeconds`, `rightTimeToPeakSeconds`, `repDurationSeconds`

This metric has these fields:

- **What it measures:** Peak force and timing of each training rep.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force.
- **Units:** N, s.
- **Variants:** Per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `leftImpulseEntireRepNewtonSeconds`, `rightImpulseEntireRepNewtonSeconds`

This metric has these fields:

- **What it measures:** Impulse over the whole training rep.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force.
- **Units:** N s.
- **Variants:** Per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Impulse threshold ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `exceededTrainingThreshold`, `enteredTargetZone`

This metric has these fields:

- **What it measures:** Whether the rep crossed the threshold or entered the target zone.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Training threshold, target zone.
- **Units:** Boolean.
- **Variants:** Per-rep fields ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `timeInZoneLeft`, `timeInZoneRight`

This metric has these fields:

- **What it measures:** Time each leg held force inside the isometric training zone.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published beyond the field names.
- **Inputs:** Force, training zone.
- **Units:** Not published.
- **Variants:** Session, exercise and rep levels ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)). Release notes say post-training results include 'impulse, time in zone, and variance' ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes).

#### `impulseLeft`, `impulseRight`

This metric has these fields:

- **What it measures:** Impulse produced in isometric training.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published.
- **Inputs:** Force.
- **Units:** Not published.
- **Variants:** Session, exercise and rep levels ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Impulse threshold ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `stabilityLeft`, `stabilityRight`

This metric has these fields:

- **What it measures:** How steady force stayed during isometric training.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. Release notes mention 'variance' in post-training results, but do not link it to this field ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Inputs:** Force.
- **Units:** Not published.
- **Variants:** Session, exercise and rep levels ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Training threshold and target zone settings ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes), [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

#### `totalRepetitions`, `repNumber`

This metric has these fields:

- **What it measures:** Number of isometric training reps.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Count (restatement of field name).
- **Inputs:** Rep detection.
- **Units:** count.
- **Variants:** Exercise and rep levels ([NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Rep threshold ([factor details](vald-forcedecks-nordbord.md#factors-that-change-the-numbers)).
- **Sources:** [NordBord API spec](https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json), [NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API).

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
