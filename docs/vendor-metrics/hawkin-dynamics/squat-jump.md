# Hawkin Dynamics metrics: squat jump

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](README.md). It holds 47 metric blocks for the squat jump. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Squat jump

The squat jump starts from a held squat. It has a propulsive phase only, and the software fails the trial if the athlete dips more than 5% below system weight ([Hawkin blog, CMJ or squat jump]).

This section has 47 metric blocks. They follow the order of the movement.

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `weight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: Weighing phase, before the start of movement. Hawkin requires at least 1 s of still standing before a countermovement jump, squat jump, or CMJ rebound runs ([Hawkin blog, CMJ phases], [Hawkin blog, flight time]).
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: VALD body weight, or body mass × 9.81 ([Merrigan 2022]).
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, flight time], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Avg. Propulsive Force(N)`, metric ID `avgPropulsiveForce`, `hawkinR` column `avg_propulsive_force_n`, `hdforce` column `avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase, including body weight.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: `Concentric Mean Force` (N) ([Merrigan 2022], [VALD glossary]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Avg. Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Avg. Relative Propulsive Force(%)`, metric ID `avgRelativePropulsiveForce`, `hawkinR` column `avg_relative_propulsive_force_percent`, `hdforce` column `avg_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsive phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Left Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Propulsive Force(N)`, metric ID `leftAvgPropulsiveForce`, `hawkinR` column `left_avg_propulsive_force_n`, `hdforce` column `left_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Right Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Propulsive Force(N)`, metric ID `rightAvgPropulsiveForce`, `hawkinR` column `right_avg_propulsive_force_n`, `hdforce` column `right_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `L|R Avg. Propulsive Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Propulsive Force(%)`, metric ID `lrAvgPropulsiveForce`, `hawkinR` column `l_r_avg_propulsive_force_percent`, `hdforce` column `lr_avg_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average propulsive force, as a percentage.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Propulsive Power` (W)

This metric has these fields:

- Names: API column `Avg. Propulsive Power(W)`, metric ID `avgPropulsivePower`, `hawkinR` column `avg_propulsive_power_w`, `hdforce` column `avg_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Avg. Relative Propulsive Power`.
- Comparison with VALD ForceDecks: `Concentric Mean Power` (W) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Avg. Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Avg. Relative Propulsive Power(W/kg)`, metric ID `avgRelativePropulsivePower`, `hawkinR` column `avg_relative_propulsive_power_w_kg`, `hdforce` column `avg_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Avg. Propulsive Velocity` (m/s)

This metric has these fields:

- Names: API column `Avg. Propulsive Velocity(m/s)`, metric ID `avgPropulsiveVelocity`, `hawkinR` column `avg_propulsive_velocity_m_s`, `hdforce` column `avg_propulsive_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average center of mass velocity during the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical velocity of the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean v(t)` over the window ([hawkinR dictionary]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Peak Propulsive Force(N)`, metric ID `peakPropulsiveForce`, `hawkinR` column `peak_propulsive_force_n`, `hdforce` column `peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase, including body weight.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- Comparison with VALD ForceDecks: `Concentric Peak Force` (N) ([Merrigan 2022]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Peak Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Peak Relative Propulsive Force(%)`, metric ID `peakRelativePropulsiveForce`, `hawkinR` column `peak_relative_propulsive_force_percent`, `hdforce` column `peak_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Right Force at Peak Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Left Force at Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left Force at Peak Propulsive Force(N)`, metric ID `leftPeakPropulsiveForce`, `hawkinR` column `left_force_at_peak_propulsive_force_n`, `hdforce` column `left_force_at_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate at the instant of peak combined force in the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Right Force at Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Propulsive Force(N)`, metric ID `rightPeakPropulsiveForce`, `hawkinR` column `right_force_at_peak_propulsive_force_n`, `hdforce` column `right_force_at_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `L|R Peak Propulsive Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Propulsive Force(%)`, metric ID `lrPeakPropulsiveForce`, `hawkinR` column `l_r_peak_propulsive_force_percent`, `hdforce` column `lr_peak_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak propulsive force, as a percentage.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Propulsive Power` (W)

This metric has these fields:

- Names: API column `Peak Propulsive Power(W)`, metric ID `peakPropulsivePower`, `hawkinR` column `peak_propulsive_power_w`, `hdforce` column `peak_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Peak Relative Propulsive Power`.
- Comparison with VALD ForceDecks: `Peak Power` (W) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Peak Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Peak Relative Propulsive Power(W/kg)`, metric ID `peakRelativePropulsivePower`, `hawkinR` column `peak_relative_propulsive_power_w_kg`, `hdforce` column `peak_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Peak Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Peak Velocity` (m/s)

This metric has these fields:

- Names: API column `Peak Velocity(m/s)`, metric ID `peakVelocity`, `hawkinR` column `peak_velocity_m_s`, `hdforce` column `peak_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest upward center of mass velocity before take-off.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical velocity of the system center of mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max v(t)` before take-off. The metric database places it in the propulsive phase ([Hawkin metric database]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Concentric Peak Velocity` (m/s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin metric database], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Propulsive Impulse` (N.s)

This metric has these fields:

- Names: API column `Propulsive Impulse(N.s)`, metric ID `totalPropulsiveImpulse`, `hawkinR` column `propulsive_impulse_n_s`, `hdforce` column `propulsive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Net Impulse`, `Relative Propulsive Net Impulse`, `Relative Propulsive Impulse`.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Propulsive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Propulsive Net Impulse(N.s)`, metric ID `propulsiveNetImpulse`, `hawkinR` column `propulsive_net_impulse_n_s`, `hdforce` column `propulsive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Relative Propulsive Net Impulse`, `Propulsive Impulse`, `Relative Propulsive Impulse`.
- Comparison with VALD ForceDecks: `Concentric Impulse` (N s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Relative Propulsive Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Propulsive Impulse(N.s/kg)`, metric ID `totalRelativePropulsiveImpulse`, `hawkinR` column `relative_propulsive_impulse_n_s_kg`, `hdforce` column `relative_propulsive_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Impulse per kilogram produced in the propulsive phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Net Impulse`, `Relative Propulsive Net Impulse`, `Propulsive Impulse`.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Metric ID versus label. In the CMJ, ID `positiveImpulse` carries label `Positive Net Impulse`, and IDs `relativeBrakingImpulse` and `relativePropulsiveImpulse` carry net labels. In the drop jump the same IDs carry gross labels ([hawkinR dictionary]). Map by label, not by ID.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Relative Propulsive Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Propulsive Net Impulse(N.s/kg)`, metric ID `relativePropulsiveNetImpulse`, `hawkinR` column `relative_propulsive_net_impulse_n_s_kg`, `hdforce` column `relative_propulsive_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Net Impulse`, `Propulsive Impulse`, `Relative Propulsive Impulse`.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `L|R Propulsive Impulse Index` (%)

This metric has these fields:

- Names: API column `L|R Propulsive Impulse Index(%)`, metric ID `lrPropulsiveImpulseIndex`, `hawkinR` column `l_r_propulsive_impulse_index_percent`, `hdforce` column `lr_propulsive_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for propulsive impulse, as a percentage.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Propulsive Net Impulse`, `Relative Propulsive Net Impulse`, `Propulsive Impulse`, `Relative Propulsive Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Propulsive Phase` (s)

This metric has these fields:

- Names: API column `Propulsive Phase(s)`, metric ID `propulsivePhase`, `hawkinR` column `propulsive_phase_s`, `hdforce` column `propulsive_phase_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the propulsive phase lasts.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased: Duration of the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_b − t_a`. Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Phase start and end events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Contraction Time` (ms), paired by Merrigan et al. (2022) ([Merrigan 2022]). In the VALD squat jump the concentric phase runs from start of movement to take-off ([VALD glossary]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Propulsive RFD` (N/s)

This metric has these fields:

- Names: API column `Propulsive RFD(N/s)`, metric ID `propulsiveRFD`, `hawkinR` column `propulsive_rfd_n_s`, `hdforce` column `propulsive_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises from the start of movement to peak force.
- Phase or window: From the start of movement to peak force. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: the instant of peak force ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Rate of force development from the onset of the test to peak force. Hawkin adds that higher values are typically better for explosive athletes ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t*) − F(t_a)) / (t* − t_a)`. Hawkin's text: rate of force development from onset to peak force ([hawkinR dictionary]). The exact slope method is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t*` is the instant of peak combined force in the window; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the start of movement.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Concentric RFD` (N/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). VALD measures from the start of the concentric phase to peak force ([VALD glossary]). Merrigan et al. found the two did not agree well.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Time To Takeoff` (s)

This metric has these fields:

- Names: API column `Time To Takeoff(s)`, metric ID `timeToTakeoff`, `hawkinR` column `time_to_takeoff_s`, `hdforce` column `time_to_takeoff_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the jump takes, from the start of movement to take-off.
- Phase or window: Whole movement. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Time from the start of movement to take-off ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `TTT = t_takeoff − t_start`.
- Inputs: Start-of-movement (or contact) and take-off events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Contraction Time` (ms), start of movement to take-off ([VALD glossary]). VALD uses a 20 N start threshold for the squat jump ([Merrigan 2022]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Flight Time` (s)

This metric has these fields:

- Names: API column `Flight Time(s)`, metric ID `flightTime`, `hawkinR` column `flight_time_s`, `hdforce` column `flight_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time in the air.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the flight phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT = t_touchdown − t_takeoff`.
- Inputs: Take-off and touchdown events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Flight Time` (ms in VALD, s in Hawkin) ([Merrigan 2022], [VALD glossary]).
- What changes the number: Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, flight time].

#### `Jump Height` (m)

This metric has these fields:

- Names: API column `Jump Height(m)`, metric ID `jumpHeight`, `hawkinR` column `jump_height_m`, `hdforce` column `jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How high the center of mass rises after take-off.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Rise of the system center of mass from take-off to its highest point. It uses take-off velocity and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH = v_to² / (2 × g)` ([Hawkin blog, take-off velocity], [Hawkin RSI course]). Terms: `v_to` is velocity at take-off, in m/s; `g` is 9.81 m/s².
- Inputs: Take-off velocity, which needs system weight and the start-of-movement event.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Jump Height (Imp-Mom)` (cm) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, take-off velocity], [Hawkin RSI course], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Jump Momentum` (kg.m/s)

This metric has these fields:

- Names: API column `Jump Momentum(kg.m/s)`, metric ID `jumpMomentum`, `hawkinR` column `jump_momentum_kg_m_s`, `hdforce` column `jump_momentum_kg_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's momentum at take-off: mass times take-off velocity.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical momentum of the system center of mass at take-off ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `m × v_to`. Terms: `m` is system mass, `SW / g`, in kg; `v_to` is velocity at take-off, in m/s.
- Inputs: System weight and take-off velocity.
- Units: kg.m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Takeoff Velocity` (m/s)

This metric has these fields:

- Names: API column `Takeoff Velocity(m/s)`, metric ID `takeoffVelocity`, `hawkinR` column `takeoff_velocity_m_s`, `hdforce` column `takeoff_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast the center of mass moves up at the instant the athlete leaves the plates.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical velocity of the system center of mass at take-off ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `v_to = v(t_takeoff)`, where `v(t) = Σ ((F(t) − SW) / m) × Δt`, summed from the start of integration at zero velocity ([Hawkin blog, two key factors]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force, system weight, start of movement, take-off.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Vertical Velocity at Take-off` (m/s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin help, CMJ setup].

#### `Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Avg. Landing Force(N)`, metric ID `avgLandingForce`, `hawkinR` column `avg_landing_force_n`, `hdforce` column `avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the landing phase, including body weight.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Avg. Landing Force`, `L|R Avg. Landing Force`, `Right Avg. Landing Force`.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Left Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Landing Force(N)`, metric ID `leftAvgLandingForce`, `hawkinR` column `left_avg_landing_force_n`, `hdforce` column `left_avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the landing phase.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Landing Force`, `L|R Avg. Landing Force`, `Right Avg. Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Right Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Landing Force(N)`, metric ID `rightAvgLandingForce`, `hawkinR` column `right_avg_landing_force_n`, `hdforce` column `right_avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the landing phase.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Landing Force`, `Left Avg. Landing Force`, `L|R Avg. Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `L|R Avg. Landing Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Landing Force(%)`, metric ID `lrAvgLandingForce`, `hawkinR` column `l_r_avg_landing_force_percent`, `hdforce` column `lr_avg_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average landing force, as a percentage.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- Comparison with VALD ForceDecks: `Peak Landing Force` (N) ([Merrigan 2022], [VALD glossary]). VALD searches from landing to the end of the repetition.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Merrigan 2022], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Relative Peak Landing Force` (%)

This metric has these fields:

- Names: API column `Relative Peak Landing Force(%)`, metric ID `relativePeakLandingForce`, `hawkinR` column `relative_peak_landing_force_percent`, `hdforce` column `relative_peak_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Landing Force`, `Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `Right Force at Peak Landing Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Landing Force(N)`, metric ID `rightPeakLandingForce`, `hawkinR` column `right_force_at_peak_landing_force_n`, `hdforce` column `right_force_at_peak_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the landing phase.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the landing phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Peak Landing Force`, `Relative Peak Landing Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Merrigan 2022].

#### `L|R Peak Landing Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Landing Force(%)`, metric ID `lrPeakLandingForce`, `hawkinR` column `l_r_peak_landing_force_percent`, `hdforce` column `lr_peak_landing_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak landing force, as a percentage.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: From touchdown to the start of the first 1 s period with force within 5% of system weight ([Hawkin blog, landing metrics], [hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time until vertical force stays within 5% of system weight for 1 s ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Time from touchdown to the first sample of a 1 s period where `|F(t) − SW| ≤ 0.05 × SW` ([hawkinR dictionary], [Hawkin blog, landing metrics]). The value is blank when the athlete keeps moving or steps off ([Hawkin help, time to stabilization]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined force after touchdown and system weight.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Settling. The value is blank if the athlete keeps moving or steps off after landing ([Hawkin help, time to stabilization]). Units. The API reports this value in ms, while most Hawkin times are in s ([hawkinR dictionary]). Convert before you combine times.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, time to stabilization], [Hawkin metric database].

#### `P1 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the first half of the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]). Window: the first half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the first half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a` to `t_a + (t_b − t_a) / 2`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- Comparison with VALD ForceDecks: `P1 Concentric Impulse` and `P2 Concentric Impulse` (N s), net impulse in the first and second 50% of the concentric phase by time ([VALD glossary]). VALD's ratio is `P2 Concentric Impulse:P1 Concentric Impulse`, the inverse of Hawkin's P1 to P2 index. Whether Hawkin's P1 and P2 are net or gross is not published.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [Hawkin help, P1 and P2], [Hawkin metric database], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `P2 Propulsive Impulse` (N.s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Impulse in the second half of the propulsive phase.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]). Window: the second half of the propulsive phase by time ([Hawkin help, P1 and P2]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The propulsive impulse applied during the second half of the propulsive phase ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_a + (t_b − t_a) / 2` to `t_b`. Whether Hawkin subtracts system weight is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Combined force and the propulsive phase events.
- Units: N.s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- Comparison with VALD ForceDecks: `P1 Concentric Impulse` and `P2 Concentric Impulse` (N s), net impulse in the first and second 50% of the concentric phase by time ([VALD glossary]). VALD's ratio is `P2 Concentric Impulse:P1 Concentric Impulse`, the inverse of Hawkin's P1 to P2 index. Whether Hawkin's P1 and P2 are net or gross is not published.
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [Hawkin help, P1 and P2], [Hawkin metric database], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `P1|P2 Propulsive Impulse Index`

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How the first half of the push compares with the second half.
- Phase or window: Propulsive phase. Start: start of movement, where Merrigan et al. (2022) report force rising 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight ([Merrigan 2022]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). The software fails the trial when force drops 5% below system weight before the jump, so a squat jump has no unweighting or braking phase ([Hawkin blog, CMJ or squat jump]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The ratio of first-half to second-half propulsive impulse ([Hawkin metric database]). Formula, restated (not Hawkin's text): `P1 / P2` ([Hawkin help, P1 and P2]).
- Inputs: P1 and P2 propulsive impulse.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- Comparison with VALD ForceDecks: `P1 Concentric Impulse` and `P2 Concentric Impulse` (N s), net impulse in the first and second 50% of the concentric phase by time ([VALD glossary]). VALD's ratio is `P2 Concentric Impulse:P1 Concentric Impulse`, the inverse of Hawkin's P1 to P2 index. Whether Hawkin's P1 and P2 are net or gross is not published.
- What changes the number: Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, CMJ or squat jump], [Hawkin metric database], [Hawkin help, P1 and P2], [VALD glossary], [Hawkin blog, drop jump measures].

#### `Landing Height` (m)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How far the center of mass falls from the top of the jump to touchdown.
- Phase or window: From the apex of the jump to touchdown ([Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased from the metric database: Landing height divided by landing time ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Landing Height / Landing Phase` ([Hawkin blog, landing metrics]). In the drop landing, Hawkin does not publish whether drop height replaces landing height.
- Inputs: Landing height and landing phase.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, drop jump measures].

[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin blog, CMJ or squat jump]: https://www.hawkindynamics.com/blog/countermovement-jump-or-squat-jump
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, drop jump measures]: https://www.hawkindynamics.com/blog/drop-jumps-what-to-measure
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, landing metrics]: https://www.hawkindynamics.com/blog/new-landing-metrics
[Hawkin blog, take-off velocity]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, CMJ setup]: https://learning.hawkindynamics.com/knowledge/countermovement-jump-protocol
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin help, P1 and P2]: https://learning.hawkindynamics.com/knowledge/p1-and-p2-propulsive-impulse-and-the-ratio-between-them
[Hawkin help, time to stabilization]: https://learning.hawkindynamics.com/knowledge/how-do-i-use-time-to-stabilization
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[Hawkin RSI course]: https://www.hawkindynamics.com/hubfs/RSI%2BCourse%2B%E2%94%82%2BHawkin%2BDynamics%2BEdu.pdf
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
