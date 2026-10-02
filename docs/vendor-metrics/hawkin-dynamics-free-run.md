# Hawkin Dynamics metrics: free run on the force plates

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 29 metric blocks for the free run on the force plates. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Free run on the force plates

The free run records force, and center of pressure, for any movement. It has no phases ([Hawkin help, free run setup]). Its metrics apply to the dual plates, not the Foundation plate ([Hawkin metric database]).

This section has 29 metric blocks. They follow the order of the movement.

#### `Avg. Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The average total force during the recording.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The mean vertical force during the free run ([Hawkin metric database]). Formula, restated (not Hawkin's text): `mean F(t)`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12].

#### `Peak Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The highest total force during the recording.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The peak instantaneous vertical force during the free run ([Hawkin metric database]). Formula, restated (not Hawkin's text): `max F(t)`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12].

#### `Avg. Left Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The average left plate force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The mean left vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `mean F_L(t)`. Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `Avg. Right Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The average right plate force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The mean right vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `mean F_R(t)`. Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `Peak Left Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The highest left plate force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The peak instantaneous left vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `max F_L(t)`. Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `Peak Right Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The highest right plate force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The peak instantaneous right vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `max F_R(t)`. Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `SD Left Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How much left plate force varies.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The standard deviation of left vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `SD(F_L(t))`. Sample or population standard deviation is not published. Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `SD Right Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How much right plate force varies.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The standard deviation of right vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `SD(F_R(t))`. Sample or population standard deviation is not published. Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `SD Total Force` (N)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How much total force varies.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The standard deviation of vertical force ([Hawkin metric database]). Formula, restated (not Hawkin's text): `SD(F(t))`. Sample or population standard deviation is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: N ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin API specification 1.12].

#### `L|R Avg. Force` (%)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The left to right difference in average force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The asymmetry between left and right average force ([Hawkin metric database]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)`. Hawkin does not publish the formula ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: % ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin blog, asymmetry report], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `L|R Peak Force` (%)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The left to right difference in peak force.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The asymmetry between left and right peak force ([Hawkin metric database]). Formula, restated (not Hawkin's text): Asymmetry of `max F_L(t)` and `max F_R(t)`. Hawkin does not publish the formula ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Plate force traces from `GET /v1/forcetime/{testId}` ([Hawkin API specification 1.12]).
- Units: % ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [Hawkin blog, asymmetry report], [Hawkin API specification 1.12], [Hawkin help, left and right plate].

#### `Left AP Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total front-to-back center of pressure path on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total distance of front-to-back sway on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left AP Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of front-to-back center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of front-to-back sway on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left Avg. AP Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of front-to-back center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average front-to-back sway velocity on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left ML Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total side-to-side center of pressure path on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total distance of side-to-side sway on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left ML Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of side-to-side center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of side-to-side sway on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left Avg. ML Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of side-to-side center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average side-to-side sway velocity on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total center of pressure path on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total sway distance on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of sway on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Left Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of center of pressure movement on the left plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average sway velocity on the left plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right AP Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total front-to-back center of pressure path on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total distance of front-to-back sway on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right AP Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of front-to-back center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of front-to-back sway on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right Avg. AP Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of front-to-back center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average front-to-back sway velocity on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right ML Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total side-to-side center of pressure path on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total distance of side-to-side sway on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right ML Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of side-to-side center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of side-to-side sway on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right Avg. ML Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of side-to-side center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average side-to-side sway velocity on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity along that axis. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right Sway Length` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Total center of pressure path on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The total sway distance on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the total distance of sway. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right Sway Range` (cm)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The span of center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The amplitude of sway on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the amplitude of sway. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

#### `Right Sway Velocity` (cm/s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Average speed of center of pressure movement on the right plate.
- Phase or window: The whole recording. The free run has no phases ([Hawkin help, free run setup]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The average sway velocity on the right plate ([Hawkin metric database]). Formula: Not published. Hawkin describes it only as the average sway velocity. Units are cm per the metric database.
- Inputs: Center of pressure traces from `GET /v1/cop/{testId}`, which the API reports in mm from the plate center ([hdforce source]).
- Units: cm/s ([Hawkin metric database]). The web page lists cm while the API center of pressure trace is in mm. Convert before you compare.
- Variants: See the other metrics in this group.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Task standardization. The free run has no fixed protocol, so set your own and keep it the same at every test ([Hawkin help, free run setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, free run setup], [Hawkin metric database], [hdforce source], [Hawkin help, left and right plate].

[Hawkin API specification 1.12]: https://github.com/HawkinDynamics/power-query
[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin help, free run setup]: https://learning.hawkindynamics.com/knowledge/free-run-test-setup-guide
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
