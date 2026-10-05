# Hawkin Dynamics metrics: countermovement rebound jump

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](README.md). It holds 115 metric blocks for the countermovement rebound jump. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Countermovement rebound jump

The athlete performs a CMJ, lands, and rebounds straight into a second jump, then sticks the landing ([Hawkin help, CMJ rebound setup]). Metrics prefixed `CMJ` use CMJ windows. Metrics prefixed `Rebound` use contact windows like the drop jump.

This section has 115 metric blocks. They follow the order of the movement.

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `weight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: Weighing phase, before the start of movement. Hawkin requires at least 1 s of still standing before a countermovement jump, squat jump, or CMJ rebound runs ([Hawkin blog, CMJ phases], [Hawkin blog, flight time]).
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, flight time], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Avg. Landing Force(N)`, metric ID `avgLandingForce`, `hawkinR` column `avg_landing_force_n`, `hdforce` column `avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the landing phase, including body weight.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Avg. Landing Force`, `L|R Avg. Landing Force`, `Right Avg. Landing Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Left Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Landing Force(N)`, metric ID `leftAvgLandingForce`, `hawkinR` column `left_avg_landing_force_n`, `hdforce` column `left_avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the landing phase.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Landing Force`, `L|R Avg. Landing Force`, `Right Avg. Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Landing Force(N)`, metric ID `rightAvgLandingForce`, `hawkinR` column `right_avg_landing_force_n`, `hdforce` column `right_avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the landing phase.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Landing Force`, `Left Avg. Landing Force`, `L|R Avg. Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `L|R Avg. Landing Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Landing Force(%)`, metric ID `lrAvgLandingForce`, `hawkinR` column `l_r_avg_landing_force_percent`, `hdforce` column `lr_avg_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average landing force, as a percentage.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Landing Force`, `Left Avg. Landing Force`, `Right Avg. Landing Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `L|R Landing Impulse Index` (%)

This metric has these fields:

- Names: API column `L|R Landing Impulse Index(%)`, metric ID `lrLandingImpulseIndex`, `hawkinR` column `l_r_landing_impulse_index_percent`, `hdforce` column `lr_landing_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for landing impulse, as a percentage.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Landing Stiffness` (N/m)

This metric has these fields:

- Names: API column `Landing Stiffness(N/m)`, metric ID `landingStiffness`, `hawkinR` column `landing_stiffness_n_m`, `hdforce` column `landing_stiffness_n_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the landing divided by how far the center of mass dropped in the landing.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Vertical force at the moment of the lowest position, divided by the lowest displacement of the system center of mass in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min) / |min s(t)|` within the landing phase ([hawkinR dictionary]). The sign of the exported value is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement after touchdown.
- Units: N/m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Integration drift. Velocity and displacement drift as the trial gets longer, so post-landing values carry more error ([Hawkin blog, two key factors], [Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, flight time].

#### `Peak Landing Force` (N)

This metric has these fields:

- Names: API column `Peak Landing Force(N)`, metric ID `peakLandingForce`, `hawkinR` column `peak_landing_force_n`, `hdforce` column `peak_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the landing phase, including body weight.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Relative Peak Landing Force` (%)

This metric has these fields:

- Names: API column `Relative Peak Landing Force(%)`, metric ID `relativePeakLandingForce`, `hawkinR` column `relative_peak_landing_force_percent`, `hdforce` column `relative_peak_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the landing phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Per Hawkin's text: `100 × mean F(t) / SW` over the landing phase ([hawkinR dictionary]). The name says peak. Hawkin has not published which one the software computes. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined force after touchdown and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Peak Landing Force`, `Right Force at Peak Landing Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary].

#### `Left Force at Peak Landing Force` (N)

This metric has these fields:

- Names: API column `Left Force at Peak Landing Force(N)`, metric ID `leftPeakLandingForce`, `hawkinR` column `left_force_at_peak_landing_force_n`, `hdforce` column `left_force_at_peak_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate at the instant of peak combined force in the landing phase.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Landing Force`, `Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Force at Peak Landing Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Landing Force(N)`, metric ID `rightPeakLandingForce`, `hawkinR` column `right_force_at_peak_landing_force_n`, `hdforce` column `right_force_at_peak_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the landing phase.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Peak Landing Force`, `Relative Peak Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `L|R Peak Landing Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Landing Force(%)`, metric ID `lrPeakLandingForce`, `hawkinR` column `l_r_peak_landing_force_percent`, `hdforce` column `lr_peak_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak landing force, as a percentage.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Time to Stabilization` (ms)

This metric has these fields:

- Names: API column `Time to Stabilization(ms)`, metric ID `timeToStabilization`, `hawkinR` column `time_to_stabilization_ms`, `hdforce` column `time_to_stabilization_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the athlete takes to settle after landing.
- Phase or window: From final touchdown to the start of the first 1 s period with force within 5% of system weight ([Hawkin blog, landing metrics], [hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time until vertical force stays within 5% of system weight for 1 s ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Time from touchdown to the first sample of a 1 s period where `|F(t) − SW| ≤ 0.05 × SW` ([hawkinR dictionary], [Hawkin blog, landing metrics]). The value is blank when the athlete keeps moving or steps off ([Hawkin help, time to stabilization]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined force after touchdown and system weight.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Settling. The value is blank if the athlete keeps moving or steps off after landing ([Hawkin help, time to stabilization]). Units. The API reports this value in ms, while most Hawkin times are in s ([hawkinR dictionary]). Convert before you combine times.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, time to stabilization], [Hawkin metric database].

#### `CMJ Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `CMJ Avg. Braking Force(N)`, metric ID `avgCmjBrakingForce`, `hawkinR` column `cmj_avg_braking_force_n`, `hdforce` column `cmj_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the braking phase of the countermovement jump, including body weight.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Relative Braking Force`, `Left CMJ Avg. Braking Force`, `CMJ L|R Avg. Braking Force`, `Right CMJ Avg. Braking Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Avg. Relative Braking Force` (%)

This metric has these fields:

- Names: API column `CMJ Avg. Relative Braking Force(%)`, metric ID `avgCmjRelativeBrakingForce`, `hawkinR` column `cmj_avg_relative_braking_force_percent`, `hdforce` column `cmj_avg_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the braking phase of the countermovement jump, as a percentage of system weight.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase of the countermovement jump, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Avg. Braking Force`, `Left CMJ Avg. Braking Force`, `CMJ L|R Avg. Braking Force`, `Right CMJ Avg. Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Left CMJ Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Left CMJ Avg. Braking Force(N)`, metric ID `leftCmjAvgBrakingForce`, `hawkinR` column `left_cmj_avg_braking_force_n`, `hdforce` column `left_cmj_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Braking Force`, `CMJ Avg. Relative Braking Force`, `CMJ L|R Avg. Braking Force`, `Right CMJ Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Right CMJ Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Right CMJ Avg. Braking Force(N)`, metric ID `rightCmjAvgBrakingForce`, `hawkinR` column `right_cmj_avg_braking_force_n`, `hdforce` column `right_cmj_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Braking Force`, `CMJ Avg. Relative Braking Force`, `Left CMJ Avg. Braking Force`, `CMJ L|R Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ L|R Avg. Braking Force` (%)

This metric has these fields:

- Names: API column `CMJ L|R Avg. Braking Force(%)`, metric ID `lrCmjAvgBrakingForce`, `hawkinR` column `cmj_l_r_avg_braking_force_percent`, `hdforce` column `cmj_lr_avg_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average braking force of the countermovement jump, as a percentage.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Avg. Braking Force`, `CMJ Avg. Relative Braking Force`, `Left CMJ Avg. Braking Force`, `Right CMJ Avg. Braking Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `CMJ Avg. Braking Power` (W)

This metric has these fields:

- Names: API column `CMJ Avg. Braking Power(W)`, metric ID `cmjAvgBrakingPower`, `hawkinR` column `cmj_avg_braking_power_w`, `hdforce` column `cmj_avg_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `CMJ Avg. Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Avg. Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `CMJ Avg. Relative Braking Power(W/kg)`, metric ID `cmjAvgRelativeBrakingPower`, `hawkinR` column `cmj_avg_relative_braking_power_w_kg`, `hdforce` column `cmj_avg_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the braking phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `CMJ Avg. Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Braking Impulse` (N.s)

This metric has these fields:

- Names: API column `CMJ Braking Impulse(N.s)`, metric ID `cmjBrakingImpulse`, `hawkinR` column `cmj_braking_impulse_n_s`, `hdforce` column `cmj_braking_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `CMJ Braking Net Impulse`, `CMJ Relative Braking Impulse`, `CMJ Relative Braking Net Impulse`, `CMJ L|R Braking Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Braking Net Impulse` (N.s)

This metric has these fields:

- Names: API column `CMJ Braking Net Impulse(N.s)`, metric ID `cmjBrakingNetImpulse`, `hawkinR` column `cmj_braking_net_impulse_n_s`, `hdforce` column `cmj_braking_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `CMJ Braking Impulse`, `CMJ Relative Braking Impulse`, `CMJ Relative Braking Net Impulse`, `CMJ L|R Braking Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Relative Braking Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `CMJ Relative Braking Impulse(N.s/kg)`, metric ID `cmjRelativeBrakingImpulse`, `hawkinR` column `cmj_relative_braking_impulse_n_s_kg`, `hdforce` column `cmj_relative_braking_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `CMJ Braking Impulse`, `CMJ Braking Net Impulse`, `CMJ Relative Braking Net Impulse`, `CMJ L|R Braking Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Relative Braking Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `CMJ Relative Braking Net Impulse(N.s/kg)`, metric ID `cmjRelativeNetBrakingImpulse`, `hawkinR` column `cmj_relative_braking_net_impulse_n_s_kg`, `hdforce` column `cmj_relative_braking_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `CMJ Braking Impulse`, `CMJ Braking Net Impulse`, `CMJ Relative Braking Impulse`, `CMJ L|R Braking Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ L|R Braking Impulse Index` (%)

This metric has these fields:

- Names: API column `CMJ L|R Braking Impulse Index(%)`, metric ID `lrCmjBrakingImpulseIndex`, `hawkinR` column `cmj_l_r_braking_impulse_index_percent`, `hdforce` column `cmj_lr_braking_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for braking impulse of the countermovement jump, as a percentage.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Braking Impulse`, `CMJ Braking Net Impulse`, `CMJ Relative Braking Impulse`, `CMJ Relative Braking Net Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `CMJ Braking RFD` (N/s)

This metric has these fields:

- Names: API column `CMJ Braking RFD(N/s)`, metric ID `cmjBrakingRFD`, `hawkinR` column `cmj_braking_rfd_n_s`, `hdforce` column `cmj_braking_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises during the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force over the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_b) − F(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Braking Force` (N)

This metric has these fields:

- Names: API column `CMJ Peak Braking Force(N)`, metric ID `peakCmjBrakingForce`, `hawkinR` column `cmj_peak_braking_force_n`, `hdforce` column `cmj_peak_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the braking phase of the countermovement jump, including body weight.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Peak Relative Braking Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Relative Braking Force` (%)

This metric has these fields:

- Names: API column `CMJ Peak Relative Braking Force(%)`, metric ID `peakCmjRelativeBrakingForce`, `hawkinR` column `cmj_peak_relative_braking_force_percent`, `hdforce` column `cmj_peak_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the braking phase of the countermovement jump, as a percentage of system weight.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase of the countermovement jump, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Peak Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Braking Power` (W)

This metric has these fields:

- Names: API column `CMJ Peak Braking Power(W)`, metric ID `cmjPeakBrakingPower`, `hawkinR` column `cmj_peak_braking_power_w`, `hdforce` column `cmj_peak_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the braking phase of the countermovement jump.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `CMJ Peak Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `CMJ Peak Relative Braking Power(W/kg)`, metric ID `cmjPeakRelativeBrakingPower`, `hawkinR` column `cmj_peak_relative_braking_power_w_kg`, `hdforce` column `cmj_peak_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the braking phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Braking phase. Start: peak negative center of mass velocity ([Hawkin blog, CMJ phases]). End: zero velocity, the lowest center of mass position ([Merrigan 2022], [McMahon 2018]).
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` `/ m` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `CMJ Peak Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [McMahon 2018], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Depth` (m)

This metric has these fields:

- Names: API column `CMJ Depth(m)`, metric ID `cmjCounterDepth`, `hawkinR` column `cmj_depth_m`, `hdforce` column `cmj_depth_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How far the center of mass drops below its starting height of the countermovement jump.
- Phase or window: The instant of zero velocity between braking and propulsion. The metric database calls this location Transfer ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Lowest vertical position of the system center of mass in the countermovement jump, as a negative displacement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min s(t)` before take-off. The value is negative ([hawkinR dictionary]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Force At Min Displacement` (N)

This metric has these fields:

- Names: API column `CMJ Force At Min Displacement(N)`, metric ID `cmjForceAtMinDisplacement`, `hawkinR` column `cmj_force_at_min_displacement_n`, `hdforce` column `cmj_force_at_min_displacement_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip.
- Phase or window: The instant of zero velocity between braking and propulsion. The metric database calls this location Transfer ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position in the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min)`, where `t_min` is the instant of `min s(t)`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Relative Force At Min Displacement`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Relative Force At Min Displacement` (%)

This metric has these fields:

- Names: API column `CMJ Relative Force At Min Displacement(%)`, metric ID `cmjRelativeForceAtMinDisplacement`, `hawkinR` column `cmj_relative_force_at_min_displacement_percent`, `hdforce` column `cmj_relative_force_at_min_displacement` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip, as a percentage of system weight.
- Phase or window: The instant of zero velocity between braking and propulsion. The metric database calls this location Transfer ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_min) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m; `SW` is `System Weight`, in N.
- Inputs: Combined force, displacement, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Force At Min Displacement`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `CMJ Avg. Propulsive Force(N)`, metric ID `avgCmjPropulsiveForce`, `hawkinR` column `cmj_avg_propulsive_force_n`, `hdforce` column `cmj_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase of the countermovement jump, including body weight.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Relative Propulsive Force`, `Left CMJ Avg. Propulsive Force`, `CMJ L|R Avg. Propulsive Force`, `Right CMJ Avg. Propulsive Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Avg. Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `CMJ Avg. Relative Propulsive Force(%)`, metric ID `avgCmjRelativePropulsiveForce`, `hawkinR` column `cmj_avg_relative_propulsive_force_percent`, `hdforce` column `cmj_avg_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase of the countermovement jump, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsion phase of the countermovement jump, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Avg. Propulsive Force`, `Left CMJ Avg. Propulsive Force`, `CMJ L|R Avg. Propulsive Force`, `Right CMJ Avg. Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Left CMJ Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left CMJ Avg. Propulsive Force(N)`, metric ID `leftCmjAvgPropulsiveForce`, `hawkinR` column `left_cmj_avg_propulsive_force_n`, `hdforce` column `left_cmj_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Propulsive Force`, `CMJ Avg. Relative Propulsive Force`, `CMJ L|R Avg. Propulsive Force`, `Right CMJ Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Right CMJ Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right CMJ Avg. Propulsive Force(N)`, metric ID `rightCmjAvgPropulsiveForce`, `hawkinR` column `right_cmj_avg_propulsive_force_n`, `hdforce` column `right_cmj_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Avg. Propulsive Force`, `CMJ Avg. Relative Propulsive Force`, `Left CMJ Avg. Propulsive Force`, `CMJ L|R Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ L|R Avg. Propulsive Force` (%)

This metric has these fields:

- Names: API column `CMJ L|R Avg. Propulsive Force(%)`, metric ID `lrCmjAvgPropulsiveForce`, `hawkinR` column `cmj_l_r_avg_propulsive_force_percent`, `hdforce` column `cmj_lr_avg_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average propulsive force of the countermovement jump, as a percentage.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Avg. Propulsive Force`, `CMJ Avg. Relative Propulsive Force`, `Left CMJ Avg. Propulsive Force`, `Right CMJ Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `CMJ Avg. Propulsive Power` (W)

This metric has these fields:

- Names: API column `CMJ Avg. Propulsive Power(W)`, metric ID `cmjAvgPropulsivePower`, `hawkinR` column `cmj_avg_propulsive_power_w`, `hdforce` column `cmj_avg_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `CMJ Avg. Relative Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Avg. Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `CMJ Avg. Relative Propulsive Power(W/kg)`, metric ID `cmjAvgRelativePropulsivePower`, `hawkinR` column `cmj_avg_relative_propulsive_power_w_kg`, `hdforce` column `cmj_avg_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `CMJ Avg. Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `CMJ Peak Propulsive Force(N)`, metric ID `peakCmjPropulsiveForce`, `hawkinR` column `cmj_peak_propulsive_force_n`, `hdforce` column `cmj_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase of the countermovement jump, including body weight.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `CMJ Peak Relative Propulsive Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `CMJ Peak Relative Propulsive Force(%)`, metric ID `peakCmjRelativePropulsiveForce`, `hawkinR` column `cmj_peak_relative_propulsive_force_percent`, `hdforce` column `cmj_peak_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase of the countermovement jump, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase of the countermovement jump, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Peak Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Propulsive Power` (W)

This metric has these fields:

- Names: API column `CMJ Peak Propulsive Power(W)`, metric ID `cmjPeakPropulsivePower`, `hawkinR` column `cmj_peak_propulsive_power_w`, `hdforce` column `cmj_peak_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `CMJ Peak Relative Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Peak Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `CMJ Peak Relative Propulsive Power(W/kg)`, metric ID `cmjPeakRelativePropulsivePower`, `hawkinR` column `cmj_peak_relative_propulsive_power_w_kg`, `hdforce` column `cmj_peak_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `CMJ Peak Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Propulsive Impulse` (N.s)

This metric has these fields:

- Names: API column `CMJ Propulsive Impulse(N.s)`, metric ID `cmjPropulsiveImpulse`, `hawkinR` column `cmj_propulsive_impulse_n_s`, `hdforce` column `cmj_propulsive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `CMJ Propulsive Net Impulse`, `CMJ Relative Propulsive Net Impulse`, `CMJ Relative Propulsive Impulse`, `CMJ L|R Propulsive Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Propulsive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `CMJ Propulsive Net Impulse(N.s)`, metric ID `cmjPropulsiveNetImpulse`, `hawkinR` column `cmj_propulsive_net_impulse_n_s`, `hdforce` column `cmj_propulsive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase of the countermovement jump.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `CMJ Propulsive Impulse`, `CMJ Relative Propulsive Net Impulse`, `CMJ Relative Propulsive Impulse`, `CMJ L|R Propulsive Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Relative Propulsive Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `CMJ Relative Propulsive Impulse(N.s/kg)`, metric ID `cmjRelativePropulsiveImpulse`, `hawkinR` column `cmj_relative_propulsive_impulse_n_s_kg`, `hdforce` column `cmj_relative_propulsive_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `CMJ Propulsive Impulse`, `CMJ Propulsive Net Impulse`, `CMJ Relative Propulsive Net Impulse`, `CMJ L|R Propulsive Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Relative Propulsive Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `CMJ Relative Propulsive Net Impulse(N.s/kg)`, metric ID `cmjRelativeNetPropulsiveImpulse`, `hawkinR` column `cmj_relative_propulsive_net_impulse_n_s_kg`, `hdforce` column `cmj_relative_propulsive_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase of the countermovement jump, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase of the countermovement jump, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `CMJ Propulsive Impulse`, `CMJ Propulsive Net Impulse`, `CMJ Relative Propulsive Impulse`, `CMJ L|R Propulsive Impulse Index`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ L|R Propulsive Impulse Index` (%)

This metric has these fields:

- Names: API column `CMJ L|R Propulsive Impulse Index(%)`, metric ID `lrCmjPropulsiveImpulseIndex`, `hawkinR` column `cmj_l_r_propulsive_impulse_index_percent`, `hdforce` column `cmj_lr_propulsive_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for propulsive impulse of the countermovement jump, as a percentage.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `CMJ Propulsive Impulse`, `CMJ Propulsive Net Impulse`, `CMJ Relative Propulsive Net Impulse`, `CMJ Relative Propulsive Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Impulse Ratio`

This metric has these fields:

- Names: API column `Impulse Ratio`, metric ID `cmjImpulseRatio`, `hawkinR` column `impulse_ratio`, `hdforce` column `impulse_ratio` ([hawkinR dictionary], [hdforce source]).
- What it measures: Braking net impulse compared with propulsive net impulse of the countermovement jump.
- Phase or window: Braking phase plus propulsive phase. Start: peak negative velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse of the braking phase divided by net vertical impulse of the propulsion phase of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): The API dictionary gives braking net impulse divided by propulsive net impulse ([hawkinR dictionary]). The metric database page for the CMJ gives the inverse, propulsive net impulse divided by braking net impulse ([Hawkin metric database]). Check the value: a ratio above 1 in a normal jump suggests propulsive over braking.
- Inputs: Braking net impulse and propulsive net impulse.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Ratio direction. Hawkin sources disagree on which impulse is on top ([hawkinR dictionary], [Hawkin metric database]). Check the value against the two impulse columns. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `Positive Impulse` (N.s)

This metric has these fields:

- Names: API column `Positive Impulse(N.s)`, metric ID `cmjPositiveImpulse`, `hawkinR` column `positive_impulse_n_s`, `hdforce` column `positive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking and propulsive phases of the countermovement jump.
- Phase or window: Braking phase plus propulsive phase. Start: peak negative velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse of the braking and propulsion phases added together of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Positive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Positive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Positive Net Impulse(N.s)`, metric ID `cmjPositiveNetImpulse`, `hawkinR` column `positive_net_impulse_n_s`, `hdforce` column `positive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking and propulsive phases of the countermovement jump.
- Phase or window: Braking phase plus propulsive phase. Start: peak negative velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse above body weight, summed over the braking and propulsion phases of the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Positive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Modified RSI`

This metric has these fields:

- Names: API column `CMJ Modified RSI`, metric ID `cmjModifiedRsi`, `hawkinR` column `cmj_modified_rsi`, `hdforce` column `cmj_modified_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Jump height divided by the time taken to jump.
- Phase or window: Whole movement. Start: start of movement, where force falls 5 standard deviations of the weighing force below system weight ([Hawkin blog, CMJ phases]), traced back to the last sample at system weight ([Hawkin blog, two key factors], [Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Jump height from take-off velocity, divided by the time from start of movement to take-off (called Time to Take-off), in the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mRSI = JH / TTT`, with `JH` in m from take-off velocity and `TTT` in s ([Hawkin RSI course], [Hawkin help, RSI and mRSI]). Hawkin lists no unit; the inputs give m/s. Terms: `JH` is jump height, in m; `TTT` is time to take-off, in s.
- Inputs: Jump height and time to take-off.
- Units: None in the dictionary ([hawkinR dictionary]). The inputs give m/s.
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Units. Use jump height in m and time in s. In the worked example, jump height in cm turned mRSI 0.2747 into 27.4719. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Merrigan 2022], [hdforce dictionary], [Hawkin RSI course], [Hawkin help, RSI and mRSI], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `CMJ RSI`

This metric has these fields:

- Names: API column `CMJ RSI`, metric ID `cmjRsi`, `hawkinR` column `cmj_rsi`, `hdforce` column `cmj_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Flight time divided by the time taken to jump.
- Phase or window: Whole movement. Start: start of movement, where force falls 5 standard deviations of the weighing force below system weight ([Hawkin blog, CMJ phases]), traced back to the last sample at system weight ([Hawkin blog, two key factors], [Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Flight time divided by the time from start of movement to take-off (called Time to Take-off), in the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT / TTT` ([hawkinR dictionary]). Terms: `FT` is flight time, in s; `TTT` is time to take-off, in s.
- Inputs: Flight time and time to take-off.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `CMJ Time To Takeoff` (s)

This metric has these fields:

- Names: API column `CMJ Time To Takeoff(s)`, metric ID `timeToTakeoff`, `hawkinR` column `cmj_time_to_takeoff_s`, `hdforce` column `cmj_time_to_takeoff_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the jump takes, from the start of movement to take-off of the countermovement jump.
- Phase or window: Whole movement. Start: start of movement, where force falls 5 standard deviations of the weighing force below system weight ([Hawkin blog, CMJ phases]), traced back to the last sample at system weight ([Hawkin blog, two key factors], [Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Time from the start of movement to take-off in the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `TTT = t_takeoff − t_start`.
- Inputs: Start-of-movement (or contact) and take-off events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Merrigan 2022], [hdforce dictionary], [Hawkin help, CMJ setup].

#### `CMJ Jump Height` (m)

This metric has these fields:

- Names: API column `CMJ Jump Height(m)`, metric ID `cmjJumpHeight`, `hawkinR` column `cmj_jump_height_m`, `hdforce` column `cmj_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How high the center of mass rises after take-off of the countermovement jump.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Rise of the system center of mass from take-off to its highest point in the countermovement jump. It uses take-off velocity and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH = v_to² / (2 × g)` ([Hawkin blog, take-off velocity], [Hawkin RSI course]). Terms: `v_to` is velocity at take-off, in m/s; `g` is 9.81 m/s².
- Inputs: Take-off velocity, which needs system weight and the start-of-movement event.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, take-off velocity], [Hawkin RSI course], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ Jump Momentum` (kg.m/s)

This metric has these fields:

- Names: API column `CMJ Jump Momentum(kg.m/s)`, metric ID `cmjJumpMomentum`, `hawkinR` column `cmj_jump_momentum_kg_m_s`, `hdforce` column `cmj_jump_momentum_kg_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's momentum at take-off of the countermovement jump: mass times take-off velocity.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical momentum of the system center of mass at take-off in the countermovement jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `m × v_to`. Terms: `m` is system mass, `SW / g`, in kg; `v_to` is velocity at take-off, in m/s.
- Inputs: System weight and take-off velocity.
- Units: kg.m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Rebound Impact Peak` (Yes/No)

This metric has these fields:

- Names: API column `Rebound Impact Peak(Yes/No)`, metric ID `reboundImpactPeak`, `hawkinR` column `rebound_impact_peak_yes_no`, `hdforce` column `rebound_impact_peak_yes_no` ([hawkinR dictionary], [hdforce source]).
- What it measures: Whether peak force lands in the first 20% of ground contact.
- Phase or window: The first 20% of rebound ground contact ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: The software flags an impact peak when the highest instantaneous vertical force falls in the first 20% of ground contact of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Yes` when `t* − t_contact ≤ 0.2 × CT`, otherwise `No` ([hawkinR dictionary], [Hawkin blog, drop jump measures]). Terms: `t*` is the instant of peak combined force in the window; `CT` is contact time, in s.
- Inputs: Combined force, contact, and take-off events.
- Units: Yes/No ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump measures], [Merrigan 2022].

#### `Rebound Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Rebound Avg. Braking Force(N)`, metric ID `avgReboundBrakingForce`, `hawkinR` column `rebound_avg_braking_force_n`, `hdforce` column `rebound_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the rebound braking phase of the rebound, including body weight.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Relative Braking Force`, `Left Rebound Avg. Braking Force`, `Rebound L|R Avg. Braking Force`, `Right Rebound Avg. Braking Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Avg. Relative Braking Force` (%)

This metric has these fields:

- Names: API column `Rebound Avg. Relative Braking Force(%)`, metric ID `avgReboundRelativeBrakingForce`, `hawkinR` column `rebound_avg_relative_braking_force_percent`, `hdforce` column `rebound_avg_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the rebound braking phase of the rebound, as a percentage of system weight.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase of the rebound, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Avg. Braking Force`, `Left Rebound Avg. Braking Force`, `Rebound L|R Avg. Braking Force`, `Right Rebound Avg. Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Left Rebound Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Left Rebound Avg. Braking Force(N)`, metric ID `leftReboundAvgBrakingForce`, `hawkinR` column `left_rebound_avg_braking_force_n`, `hdforce` column `left_rebound_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Braking Force`, `Rebound Avg. Relative Braking Force`, `Rebound L|R Avg. Braking Force`, `Right Rebound Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Rebound Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Right Rebound Avg. Braking Force(N)`, metric ID `rightReboundAvgBrakingForce`, `hawkinR` column `right_rebound_avg_braking_force_n`, `hdforce` column `right_rebound_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Braking Force`, `Rebound Avg. Relative Braking Force`, `Left Rebound Avg. Braking Force`, `Rebound L|R Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound L|R Avg. Braking Force` (%)

This metric has these fields:

- Names: API column `Rebound L|R Avg. Braking Force(%)`, metric ID `lrReboundAvgBrakingForce`, `hawkinR` column `rebound_l_r_avg_braking_force_percent`, `hdforce` column `rebound_lr_avg_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average braking force of the rebound, as a percentage.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Avg. Braking Force`, `Rebound Avg. Relative Braking Force`, `Left Rebound Avg. Braking Force`, `Right Rebound Avg. Braking Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Rebound Avg. Braking Power` (W)

This metric has these fields:

- Names: API column `Rebound Avg. Braking Power(W)`, metric ID `reboundAvgBrakingPower`, `hawkinR` column `rebound_avg_braking_power_w`, `hdforce` column `rebound_avg_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Rebound Avg. Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Avg. Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `Rebound Avg. Relative Braking Power(W/kg)`, metric ID `reboundAvgRelativeBrakingPower`, `hawkinR` column `rebound_avg_relative_braking_power_w_kg`, `hdforce` column `rebound_avg_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the rebound braking phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Rebound Avg. Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Braking Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Braking Impulse(N.s)`, metric ID `reboundBrakingImpulse`, `hawkinR` column `rebound_braking_impulse_n_s`, `hdforce` column `rebound_braking_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound L|R Braking Impulse Index`, `Rebound Braking Net Impulse`, `Rebound Relative Braking Impulse`, `Rebound Relative Braking Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Braking Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Braking Net Impulse(N.s)`, metric ID `reboundBrakingNetImpulse`, `hawkinR` column `rebound_braking_net_impulse_n_s`, `hdforce` column `rebound_braking_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound L|R Braking Impulse Index`, `Rebound Braking Impulse`, `Rebound Relative Braking Impulse`, `Rebound Relative Braking Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Relative Braking Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Rebound Relative Braking Impulse(N.s/kg)`, metric ID `reboundRelativeBrakingImpulse`, `hawkinR` column `rebound_relative_braking_impulse_n_s_kg`, `hdforce` column `rebound_relative_braking_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the rebound braking phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Rebound L|R Braking Impulse Index`, `Rebound Braking Impulse`, `Rebound Braking Net Impulse`, `Rebound Relative Braking Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Relative Braking Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Rebound Relative Braking Net Impulse(N.s/kg)`, metric ID `reboundRelativeNetBrakingImpulse`, `hawkinR` column `rebound_relative_braking_net_impulse_n_s_kg`, `hdforce` column `rebound_relative_braking_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the rebound braking phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Rebound L|R Braking Impulse Index`, `Rebound Braking Impulse`, `Rebound Braking Net Impulse`, `Rebound Relative Braking Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound L|R Braking Impulse Index` (%)

This metric has these fields:

- Names: API column `Rebound L|R Braking Impulse Index(%)`, metric ID `lrReboundBrakingImpulseIndex`, `hawkinR` column `rebound_l_r_braking_impulse_index_percent`, `hdforce` column `rebound_lr_braking_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for braking impulse of the rebound, as a percentage.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Braking Impulse`, `Rebound Braking Net Impulse`, `Rebound Relative Braking Impulse`, `Rebound Relative Braking Net Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Rebound Peak Braking Force` (N)

This metric has these fields:

- Names: API column `Rebound Peak Braking Force(N)`, metric ID `peakReboundBrakingForce`, `hawkinR` column `rebound_peak_braking_force_n`, `hdforce` column `rebound_peak_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the rebound braking phase of the rebound, including body weight.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Peak Relative Braking Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Relative Braking Force` (%)

This metric has these fields:

- Names: API column `Rebound Peak Relative Braking Force(%)`, metric ID `peakReboundRelativeBrakingForce`, `hawkinR` column `rebound_peak_relative_braking_force_percent`, `hdforce` column `rebound_peak_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the rebound braking phase of the rebound, as a percentage of system weight.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase of the rebound, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Peak Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Braking Power` (W)

This metric has these fields:

- Names: API column `Rebound Peak Braking Power(W)`, metric ID `reboundPeakBrakingPower`, `hawkinR` column `rebound_peak_braking_power_w`, `hdforce` column `rebound_peak_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the rebound braking phase of the rebound.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Rebound Peak Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `Rebound Peak Relative Braking Power(W/kg)`, metric ID `reboundPeakRelativeBrakingPower`, `hawkinR` column `rebound_peak_relative_braking_power_w_kg`, `hdforce` column `rebound_peak_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the rebound braking phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` `/ m` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Rebound Peak Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Time to Peak Braking Force` (ms)

This metric has these fields:

- Names: API column `Rebound Time to Peak Braking Force(ms)`, metric ID `reboundTimeToPeakBrakingForce`, `hawkinR` column `rebound_time_to_peak_braking_force_ms`, `hdforce` column `rebound_time_to_peak_braking_force_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time from initial contact to peak braking force.
- Phase or window: Rebound braking phase. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: zero velocity.
- Calculation: Hawkin's definition, paraphrased: Time from initial contact to the moment of the highest instantaneous vertical force in the braking phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t* − t_contact`, with `t*` the instant of peak force in the braking phase ([hawkinR dictionary]). Terms: `t*` is the instant of peak combined force in the window.
- Inputs: Combined force and the contact event.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Units. The API reports this value in ms, while most Hawkin times are in s ([hawkinR dictionary]). Convert before you combine times.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin metric database], [Merrigan 2022].

#### `Rebound Depth` (m)

This metric has these fields:

- Names: API column `Rebound Depth(m)`, metric ID `reboundCounterDepth`, `hawkinR` column `rebound_depth_m`, `hdforce` column `rebound_depth_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How far the center of mass drops below its starting height of the rebound.
- Phase or window: The instant of zero velocity between rebound braking and propulsion.
- Calculation: Hawkin's definition, paraphrased: Lowest vertical position of the system center of mass during the rebound, as a negative displacement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min s(t)` before take-off. The value is negative ([hawkinR dictionary]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement trace and drop height.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Rebound Force At Min Displacement` (N)

This metric has these fields:

- Names: API column `Rebound Force At Min Displacement(N)`, metric ID `reboundForceAtMinDisplacement`, `hawkinR` column `rebound_force_at_min_displacement_n`, `hdforce` column `rebound_force_at_min_displacement_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip.
- Phase or window: The instant of zero velocity between rebound braking and propulsion.
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position during the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min)`, where `t_min` is the instant of `min s(t)`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Relative Force At Min Displacement`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Rebound Relative Force At Min Displacement` (%)

This metric has these fields:

- Names: API column `Rebound Relative Force At Min Displacement(%)`, metric ID `reboundRelativeForceAtMinDisplacement`, `hawkinR` column `rebound_relative_force_at_min_displacement_percent`, `hdforce` column `rebound_relative_force_at_min_displacement` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip, as a percentage of system weight.
- Phase or window: The instant of zero velocity between rebound braking and propulsion.
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position during the rebound, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_min) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m; `SW` is `System Weight`, in N.
- Inputs: Combined force, displacement, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Force At Min Displacement`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Rebound Stiffness` (N/m)

This metric has these fields:

- Names: API column `Rebound Stiffness(N/m)`, metric ID `reboundStiffness`, `hawkinR` column `rebound_stiffness_n_m`, `hdforce` column `rebound_stiffness_n_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip divided by how far the center of mass dropped.
- Phase or window: The instant of zero velocity between rebound braking and propulsion.
- Calculation: Hawkin's definition, paraphrased: Vertical force at the moment of the lowest position of the system center of mass, divided by that lowest displacement, in the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min) / |min s(t)|` ([hawkinR dictionary]). Hawkin's text uses the negative displacement; the sign of the exported value is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement.
- Units: N/m ([hawkinR dictionary]). The metric database web page lists `Newtons per meter (N/s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Spring-like behavior. Stiffness assumes peak force and lowest position happen together. Check this before you use it ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `Rebound Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Rebound Avg. Propulsive Force(N)`, metric ID `avgReboundPropulsiveForce`, `hawkinR` column `rebound_avg_propulsive_force_n`, `hdforce` column `rebound_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the rebound propulsive phase of the rebound, including body weight.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Relative Propulsive Force`, `Left Rebound Avg. Propulsive Force`, `Rebound L|R Avg. Propulsive Force`, `Right Rebound Avg. Propulsive Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Avg. Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Rebound Avg. Relative Propulsive Force(%)`, metric ID `avgReboundRelativePropulsiveForce`, `hawkinR` column `rebound_avg_relative_propulsive_force_percent`, `hdforce` column `rebound_avg_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the rebound propulsive phase of the rebound, as a percentage of system weight.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsive phase of the rebound, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Avg. Propulsive Force`, `Left Rebound Avg. Propulsive Force`, `Rebound L|R Avg. Propulsive Force`, `Right Rebound Avg. Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Left Rebound Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left Rebound Avg. Propulsive Force(N)`, metric ID `leftReboundAvgPropulsiveForce`, `hawkinR` column `left_rebound_avg_propulsive_force_n`, `hdforce` column `left_rebound_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Propulsive Force`, `Rebound Avg. Relative Propulsive Force`, `Rebound L|R Avg. Propulsive Force`, `Right Rebound Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Rebound Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right Rebound Avg. Propulsive Force(N)`, metric ID `rightReboundAvgPropulsiveForce`, `hawkinR` column `right_rebound_avg_propulsive_force_n`, `hdforce` column `right_rebound_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Avg. Propulsive Force`, `Rebound Avg. Relative Propulsive Force`, `Left Rebound Avg. Propulsive Force`, `Rebound L|R Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound L|R Avg. Propulsive Force` (%)

This metric has these fields:

- Names: API column `Rebound L|R Avg. Propulsive Force(%)`, metric ID `lrReboundAvgPropulsiveForce`, `hawkinR` column `rebound_l_r_avg_propulsive_force_percent`, `hdforce` column `rebound_lr_avg_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average propulsive force of the rebound, as a percentage.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Avg. Propulsive Force`, `Rebound Avg. Relative Propulsive Force`, `Left Rebound Avg. Propulsive Force`, `Right Rebound Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Rebound Avg. Propulsive Power` (W)

This metric has these fields:

- Names: API column `Rebound Avg. Propulsive Power(W)`, metric ID `reboundAvgPropulsivePower`, `hawkinR` column `rebound_avg_propulsive_power_w`, `hdforce` column `rebound_avg_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Rebound Avg. Relative Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Avg. Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Rebound Avg. Relative Propulsive Power(W/kg)`, metric ID `reboundAvgRelativePropulsivePower`, `hawkinR` column `rebound_avg_relative_propulsive_power_w_kg`, `hdforce` column `rebound_avg_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the rebound propulsive phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Rebound Avg. Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Rebound Peak Propulsive Force(N)`, metric ID `peakReboundPropulsiveForce`, `hawkinR` column `rebound_peak_propulsive_force_n`, `hdforce` column `rebound_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the rebound propulsive phase of the rebound, including body weight.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Rebound Peak Relative Propulsive Force`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Rebound Peak Relative Propulsive Force(%)`, metric ID `peakReboundRelativePropulsiveForce`, `hawkinR` column `rebound_peak_relative_propulsive_force_percent`, `hdforce` column `rebound_peak_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the rebound propulsive phase of the rebound, as a percentage of system weight.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase of the rebound, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Peak Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Propulsive Power` (W)

This metric has these fields:

- Names: API column `Rebound Peak Propulsive Power(W)`, metric ID `reboundPeakPropulsivePower`, `hawkinR` column `rebound_peak_propulsive_power_w`, `hdforce` column `rebound_peak_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Rebound Peak Relative Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Peak Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Rebound Peak Relative Propulsive Power(W/kg)`, metric ID `reboundPeakRelativePropulsivePower`, `hawkinR` column `rebound_peak_relative_propulsive_power_w_kg`, `hdforce` column `rebound_peak_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the rebound propulsive phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Rebound Peak Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Propulsive Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Propulsive Impulse(N.s)`, metric ID `reboundPropulsiveImpulse`, `hawkinR` column `rebound_propulsive_impulse_n_s`, `hdforce` column `rebound_propulsive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound L|R Propulsive Impulse Index`, `Rebound Propulsive Net Impulse`, `Rebound Relative Propulsive Net Impulse`, `Rebound Relative Propulsive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Propulsive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Propulsive Net Impulse(N.s)`, metric ID `reboundPropulsiveNetImpulse`, `hawkinR` column `rebound_propulsive_net_impulse_n_s`, `hdforce` column `rebound_propulsive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the rebound propulsive phase of the rebound.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound L|R Propulsive Impulse Index`, `Rebound Propulsive Impulse`, `Rebound Relative Propulsive Net Impulse`, `Rebound Relative Propulsive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Relative Propulsive Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Rebound Relative Propulsive Impulse(N.s/kg)`, metric ID `reboundRelativePropulsiveImpulse`, `hawkinR` column `rebound_relative_propulsive_impulse_n_s_kg`, `hdforce` column `rebound_relative_propulsive_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the rebound propulsive phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Rebound L|R Propulsive Impulse Index`, `Rebound Propulsive Impulse`, `Rebound Propulsive Net Impulse`, `Rebound Relative Propulsive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Relative Propulsive Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Rebound Relative Propulsive Net Impulse(N.s/kg)`, metric ID `reboundRelativeNetPropulsiveImpulse`, `hawkinR` column `rebound_relative_propulsive_net_impulse_n_s_kg`, `hdforce` column `rebound_relative_propulsive_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the rebound propulsive phase of the rebound, per kilogram of system mass.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase of the rebound, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Rebound L|R Propulsive Impulse Index`, `Rebound Propulsive Impulse`, `Rebound Propulsive Net Impulse`, `Rebound Relative Propulsive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound L|R Propulsive Impulse Index` (%)

This metric has these fields:

- Names: API column `Rebound L|R Propulsive Impulse Index(%)`, metric ID `lrReboundPropulsiveImpulseIndex`, `hawkinR` column `rebound_l_r_propulsive_impulse_index_percent`, `hdforce` column `rebound_lr_propulsive_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for propulsive impulse of the rebound, as a percentage.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Rebound Propulsive Impulse`, `Rebound Propulsive Net Impulse`, `Rebound Relative Propulsive Net Impulse`, `Rebound Relative Propulsive Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Rebound Impulse Ratio`

This metric has these fields:

- Names: API column `Rebound Impulse Ratio`, metric ID `reboundImpulseRatio`, `hawkinR` column `rebound_impulse_ratio`, `hdforce` column `rebound_impulse_ratio` ([hawkinR dictionary], [hdforce source]).
- What it measures: Braking net impulse compared with propulsive net impulse of the rebound.
- Phase or window: Rebound braking plus propulsive phase, from rebound contact to rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse of the braking phase divided by net vertical impulse of the propulsion phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): The API dictionary gives braking net impulse divided by propulsive net impulse ([hawkinR dictionary]). The metric database page for the CMJ gives the inverse, propulsive net impulse divided by braking net impulse ([Hawkin metric database]). Check the value: a ratio above 1 in a normal jump suggests propulsive over braking.
- Inputs: Braking net impulse and propulsive net impulse.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Ratio direction. Hawkin sources disagree on which impulse is on top ([hawkinR dictionary], [Hawkin metric database]). Check the value against the two impulse columns. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `Rebound Positive Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Positive Impulse(N.s)`, metric ID `reboundPositiveImpulse`, `hawkinR` column `rebound_positive_impulse_n_s`, `hdforce` column `rebound_positive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking and propulsive phases of the rebound.
- Phase or window: Rebound braking plus propulsive phase, from rebound contact to rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse of the braking and propulsion phases added together of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound Positive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Positive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Rebound Positive Net Impulse(N.s)`, metric ID `reboundPositiveNetImpulse`, `hawkinR` column `rebound_positive_net_impulse_n_s`, `hdforce` column `rebound_positive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking and propulsive phases of the rebound.
- Phase or window: Rebound braking plus propulsive phase, from rebound contact to rebound take-off.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse above body weight, summed over the braking and propulsion phases of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Rebound Positive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Rebound Contact Time` (ms)

This metric has these fields:

- Names: API column `Rebound Contact Time(ms)`, metric ID `contactTime`, `hawkinR` column `rebound_contact_time_ms`, `hdforce` column `rebound_contact_time_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Ground contact time: braking phase plus propulsive phase.
- Phase or window: Rebound ground contact. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: rebound take-off ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Contact time of the rebound jump ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `CT = t_takeoff − t_contact` ([hawkinR dictionary]).
- Inputs: Contact and take-off events.
- Units: ms ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Merrigan 2022].

#### `Rebound Modified RSI`

This metric has these fields:

- Names: API column `Rebound Modified RSI`, metric ID `reboundModifiedRsi`, `hawkinR` column `rebound_modified_rsi`, `hdforce` column `rebound_modified_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Jump height divided by ground contact time.
- Phase or window: Rebound ground contact. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: rebound take-off ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Jump height of the rebound from take-off velocity, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH / CT`, with `JH` from take-off velocity. Hawkin lists no unit; the inputs give m/s ([hawkinR dictionary], [Hawkin help, RSI and mRSI]). Terms: `JH` is jump height, in m; `CT` is contact time, in s.
- Inputs: Jump height and contact time.
- Units: None in the dictionary ([hawkinR dictionary]). The inputs give m/s.
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, RSI and mRSI], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method], [Merrigan 2022], [Hawkin blog, take-off velocity], [Hawkin blog, flight time], [Hawkin blog, drop jump measures].

#### `Rebound RSI`

This metric has these fields:

- Names: API column `Rebound RSI`, metric ID `reboundRsi`, `hawkinR` column `rebound_rsi`, `hdforce` column `rebound_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Flight time divided by ground contact time.
- Phase or window: Rebound ground contact. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: rebound take-off ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Flight time of the rebound divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT / CT` ([hawkinR dictionary], [Hawkin help, RSI and mRSI]). Terms: `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Flight time and contact time.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, RSI and mRSI], [Hawkin blog, flight time], [Merrigan 2022], [Hawkin blog, drop jump measures].

#### `Rebound Spring Like Correlation`

This metric has these fields:

- Names: API column `Rebound Spring Like Correlation`, metric ID `reboundSpringLikeCorrelation`, `hawkinR` column `rebound_spring_like_correlation`, `hdforce` column `rebound_spring_like_correlation` ([hawkinR dictionary], [hdforce source]).
- What it measures: How closely force rises and falls with the center of mass drop during contact, like a spring.
- Phase or window: Rebound ground contact. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: rebound take-off ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Pearson product-moment correlation between vertical force and vertical displacement of the system center of mass in the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Pearson correlation `r` between `F(t)` and `s(t)` over ground contact ([hawkinR dictionary]). A perfect spring gives −1.0 ([Hawkin blog, drop jump measures]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement during contact.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump measures], [Hawkin blog, drop jump method], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Rebound Time To Takeoff` (s)

This metric has these fields:

- Names: API column `Rebound Time To Takeoff(s)`, metric ID `reboundTimeToTakeoff`, `hawkinR` column `rebound_time_to_takeoff_s`, `hdforce` column `rebound_time_to_takeoff_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Ground contact time, from initial contact to take-off.
- Phase or window: Rebound ground contact. Start: initial contact of the rebound, the touchdown that ends the countermovement jump flight ([hawkinR dictionary]). The force threshold for this test is not published. End: rebound take-off ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time from initial contact to take-off of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_takeoff − t_contact`.
- Inputs: Start-of-movement (or contact) and take-off events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Rebound Flight Time` (ms)

This metric has these fields:

- Names: API column `Rebound Flight Time(ms)`, metric ID `flightTime`, `hawkinR` column `rebound_flight_time_ms`, `hdforce` column `rebound_flight_time_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time in the air of the rebound.
- Phase or window: Rebound flight phase. Start: rebound take-off. End: final touchdown. Thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Duration of the flight phase of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT = t_touchdown − t_takeoff`.
- Inputs: Take-off and touchdown events.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin metric database], [Merrigan 2022], [Hawkin blog, flight time].

#### `Rebound Jump Height` (m)

This metric has these fields:

- Names: API column `Rebound Jump Height(m)`, metric ID `reboundJumpHeight`, `hawkinR` column `rebound_jump_height_m`, `hdforce` column `rebound_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How high the center of mass rises after take-off of the rebound.
- Phase or window: Rebound flight phase. Start: rebound take-off. End: final touchdown. Thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Rise of the system center of mass from take-off to its highest point in the rebound. It uses take-off velocity and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH = v_to² / (2 × g)` ([Hawkin blog, take-off velocity], [Hawkin RSI course]). Terms: `v_to` is velocity at take-off, in m/s; `g` is 9.81 m/s².
- Inputs: Take-off velocity, which needs system weight and the start-of-movement event and the drop height.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, take-off velocity], [Hawkin RSI course], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Rebound Jump Momentum` (kg.m/s)

This metric has these fields:

- Names: API column `Rebound Jump Momentum(kg.m/s)`, metric ID `reboundJumpMomentum`, `hawkinR` column `rebound_jump_momentum_kg_m_s`, `hdforce` column `rebound_jump_momentum_kg_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's momentum at take-off of the rebound: mass times take-off velocity.
- Phase or window: Rebound flight phase. Start: rebound take-off. End: final touchdown. Thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Vertical momentum of the system center of mass at take-off of the rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `m × v_to`. Terms: `m` is system mass, `SW / g`, in kg; `v_to` is velocity at take-off, in m/s.
- Inputs: System weight and take-off velocity.
- Units: kg.m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `CMJ P1 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the first half of the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). Window: the first half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the first half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a` to `t_a + (t_b − t_a) / 2`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Merrigan 2022], [Hawkin help, P1 and P2], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ P2 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the second half of the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). Window: the second half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the second half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a + (t_b − t_a) / 2` to `t_b`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Merrigan 2022], [Hawkin help, P1 and P2], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `CMJ P1|P2 Propulsive Impulse Index`

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How the first half of the push compares with the second half.
- Phase or window: Propulsive phase. Start: zero velocity, when the center of mass starts to rise ([Hawkin blog, CMJ phases]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The ratio of first-half to second-half propulsive impulse ([Hawkin metric database]). Formula, restated (not Hawkin's text): `P1 / P2` ([Hawkin help, P1 and P2]).
- Inputs: P1 and P2 propulsive impulse.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Merrigan 2022], [Hawkin metric database], [Hawkin help, P1 and P2], [Hawkin blog, drop jump measures].

#### `Rebound P1 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the first half of the propulsive phase.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off. Window: the first half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the first half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a` to `t_a + (t_b − t_a) / 2`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, P1 and P2], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Rebound P2 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the second half of the propulsive phase.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off. Window: the second half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the second half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a + (t_b − t_a) / 2` to `t_b`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin help, P1 and P2], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Rebound P1|P2 Propulsive Impulse Index`

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How the first half of the push compares with the second half.
- Phase or window: Rebound propulsive phase. Start: zero velocity. End: rebound take-off.
- Calculation: Hawkin's definition, paraphrased from the metric database: The ratio of first-half to second-half propulsive impulse ([Hawkin metric database]). Formula, restated (not Hawkin's text): `P1 / P2` ([Hawkin help, P1 and P2]).
- Inputs: P1 and P2 propulsive impulse.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin metric database], [Hawkin help, P1 and P2], [Hawkin blog, drop jump measures].

#### `Landing Height` (m)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How far the center of mass falls from the top of the jump to touchdown.
- Phase or window: From the apex of the jump to final touchdown ([Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The free-fall height of the center of mass from the apex of the jump to contact ([Hawkin metric database]). Formula, restated (not Hawkin's text): `s(t_apex) − s(t_touchdown)`. How Hawkin computes it is not published. It is nearly always slightly more than jump height, because athletes land with the ankle less extended than at take-off ([Hawkin blog, landing metrics]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement or velocity at touchdown.
- Units: m ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Landing Phase` (s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How long the landing takes, from touchdown until the athlete stops moving down.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The time from touchdown to the first instant of zero center of mass velocity ([Hawkin metric database]). Formula, restated (not Hawkin's text): `t_b − t_a`. It differs from `Time to Stabilization`, which waits for 1 s of steady force ([Hawkin blog, landing metrics]). Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Touchdown and the velocity trace.
- Units: s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). Integration drift. Velocity and displacement drift as the trial gets longer, so post-landing values carry more error ([Hawkin blog, two key factors], [Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin blog, flight time].

#### `Landing Performance Index`

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Landing height per second of landing time. Higher means the athlete stops a bigger fall faster.
- Phase or window: Landing phase. Start: final touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased from the metric database: Landing height divided by landing time ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Landing Height / Landing Phase` ([Hawkin blog, landing metrics]). In the drop landing, Hawkin does not publish whether drop height replaces landing height.
- Inputs: Landing height and landing phase.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, drop jump measures].

[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, drop jump measures]: https://www.hawkindynamics.com/blog/drop-jumps-what-to-measure
[Hawkin blog, drop jump method]: https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, landing metrics]: https://www.hawkindynamics.com/blog/new-landing-metrics
[Hawkin blog, take-off velocity]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, CMJ rebound setup]: https://learning.hawkindynamics.com/knowledge/countermovement-rebound-test-setup-guide
[Hawkin help, CMJ setup]: https://learning.hawkindynamics.com/knowledge/countermovement-jump-protocol
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin help, P1 and P2]: https://learning.hawkindynamics.com/knowledge/p1-and-p2-propulsive-impulse-and-the-ratio-between-them
[Hawkin help, RSI and mRSI]: https://learning.hawkindynamics.com/knowledge/what-is-the-difference-between-rsi-and-mrsi
[Hawkin help, time to stabilization]: https://learning.hawkindynamics.com/knowledge/how-do-i-use-time-to-stabilization
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[Hawkin RSI course]: https://www.hawkindynamics.com/hubfs/RSI%2BCourse%2B%E2%94%82%2BHawkin%2BDynamics%2BEdu.pdf
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[McMahon 2018]: https://doi.org/10.1519/SSC.0000000000000375
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
