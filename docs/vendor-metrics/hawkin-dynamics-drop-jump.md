# Hawkin Dynamics metrics: drop jump

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 85 metric blocks for the drop jump. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Drop jump

The athlete drops from a box, lands, and jumps ([Hawkin help, drop jump setup]). Ground contact has a braking and a propulsive phase ([Hawkin help, force plate data]). The 2025 method needs the athlete still for the final second ([Hawkin blog, drop jump method]).

This section has 85 metric blocks. They follow the order of the movement.

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `weight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: System weight for the drop jump. Hawkin does not publish which still period it uses. The 2025 method needs the athlete still for the final second ([Hawkin blog, drop jump method]). The help center says the athlete needs a stored weight, for example from an earlier CMJ ([Hawkin help, drop jump error]). Merrigan et al. (2022) report the average of earlier squat and countermovement jumps ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: VALD body weight, or body mass × 9.81 ([Merrigan 2022]).
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, drop jump method], [Hawkin help, drop jump error], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases].

#### `Drop Height` (m)

This metric has these fields:

- Names: API column `Drop Height(m)`, metric ID `dropHeight`, `hawkinR` column `drop_height_m`, `hdforce` column `drop_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The height the center of mass falls before contact. It sets how hard the landing is.
- Phase or window: Before contact: the fall from the box. Since an update announced on 2025-01-14, Hawkin estimates the true fall height by reverse integration from a still final second, falls back to flight time, and uses the entered box height only when the athlete does not land on the plates. An automatic tag names the method used ([Hawkin blog, drop jump method]).
- Calculation: Hawkin's definition, paraphrased: Box height entered by the user. The software uses it to estimate the center of mass velocity at initial contact ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Since an update announced on 2025-01-14: the true fall height from reverse integration, or from flight time, or the entered box height when the athlete does not land on the plates ([Hawkin blog, drop jump method]). The API dictionary still describes it as the user-entered box height ([hawkinR dictionary]). Under free fall, contact velocity is `√(2 × g × h)`. Terms: `g` is 9.81 m/s².
- Inputs: Entered box height, and for the drop jump the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Drop Height` (cm), entered by hand or calculated from `Effective Drop` ([VALD glossary]). Hawkin estimates true drop height by default since 2025 ([Hawkin blog, drop jump method]).
- What changes the number: Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary].

#### `Impact Peak` (Yes/No)

This metric has these fields:

- Names: API column `Impact Peak(Yes/No)`, metric ID `impactPeak`, `hawkinR` column `impact_peak_yes_no`, `hdforce` column `impact_peak_yes_no` ([hawkinR dictionary], [hdforce source]).
- What it measures: Whether peak force lands in the first 20% of ground contact.
- Phase or window: The first 20% of ground contact, measured from initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]) ([hawkinR dictionary], [Hawkin blog, drop jump measures]).
- Calculation: Hawkin's definition, paraphrased: The software flags an impact peak when the highest instantaneous vertical force falls in the first 20% of ground contact ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Yes` when `t* − t_contact ≤ 0.2 × CT`, otherwise `No` ([hawkinR dictionary], [Hawkin blog, drop jump measures]). Terms: `t*` is the instant of peak combined force in the window; `CT` is contact time, in s.
- Inputs: Combined force, contact, and take-off events.
- Units: Yes/No ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [Hawkin blog, drop jump measures], [hdforce dictionary].

#### `Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Avg. Braking Force(N)`, metric ID `avgBrakingForce`, `hawkinR` column `avg_braking_force_n`, `hdforce` column `avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the braking phase, including body weight.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Relative Braking Force`, `Left Avg. Braking Force`, `L|R Avg. Braking Force`, `Right Avg. Braking Force`.
- Comparison with VALD ForceDecks: `Eccentric Mean Force` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). In the VALD drop jump the eccentric phase runs from drop landing to zero velocity ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Avg. Relative Braking Force` (%)

This metric has these fields:

- Names: API column `Avg. Relative Braking Force(%)`, metric ID `avgRelativeBrakingForce`, `hawkinR` column `avg_relative_braking_force_percent`, `hdforce` column `avg_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the braking phase, as a percentage of system weight.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the braking phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Braking Force`, `Left Avg. Braking Force`, `L|R Avg. Braking Force`, `Right Avg. Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Left Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Braking Force(N)`, metric ID `leftAvgBrakingForce`, `hawkinR` column `left_avg_braking_force_n`, `hdforce` column `left_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Braking Force`, `Avg. Relative Braking Force`, `L|R Avg. Braking Force`, `Right Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Right Avg. Braking Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Braking Force(N)`, metric ID `rightAvgBrakingForce`, `hawkinR` column `right_avg_braking_force_n`, `hdforce` column `right_avg_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Braking Force`, `Avg. Relative Braking Force`, `Left Avg. Braking Force`, `L|R Avg. Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `L|R Avg. Braking Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Braking Force(%)`, metric ID `lrAvgBrakingForce`, `hawkinR` column `l_r_avg_braking_force_percent`, `hdforce` column `lr_avg_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average braking force, as a percentage.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Braking Force`, `Avg. Relative Braking Force`, `Left Avg. Braking Force`, `Right Avg. Braking Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Braking Power` (W)

This metric has these fields:

- Names: API column `Avg. Braking Power(W)`, metric ID `avgBrakingPower`, `hawkinR` column `avg_braking_power_w`, `hdforce` column `avg_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Avg. Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Avg. Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `Avg. Relative Braking Power(W/kg)`, metric ID `avgRelativeBrakingPower`, `hawkinR` column `avg_relative_braking_power_w_kg`, `hdforce` column `avg_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the braking phase, per kilogram of system mass.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the braking phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Power is negative while the center of mass moves down. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Avg. Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Avg. Braking Velocity` (m/s)

This metric has these fields:

- Names: API column `Avg. Braking Velocity(m/s)`, metric ID `avgBrakingVelocity`, `hawkinR` column `avg_braking_velocity_m_s`, `hdforce` column `avg_braking_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average center of mass velocity during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical velocity of the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean v(t)` over the window ([hawkinR dictionary]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Braking Impulse` (N.s)

This metric has these fields:

- Names: API column `Braking Impulse(N.s)`, metric ID `brakingImpulse`, `hawkinR` column `braking_impulse_n_s`, `hdforce` column `braking_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Braking Net Impulse`, `L|R Braking Impulse Index`, `Relative Braking Impulse`, `Relative Braking Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Braking Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Braking Net Impulse(N.s)`, metric ID `brakingNetImpulse`, `hawkinR` column `braking_net_impulse_n_s`, `hdforce` column `braking_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Braking Impulse`, `L|R Braking Impulse Index`, `Relative Braking Impulse`, `Relative Braking Net Impulse`.
- Comparison with VALD ForceDecks: `Eccentric Impulse` (N s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Braking Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Braking Impulse(N.s/kg)`, metric ID `relativeBrakingImpulse`, `hawkinR` column `relative_braking_impulse_n_s_kg`, `hdforce` column `relative_braking_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking phase, per kilogram of system mass.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the braking phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Braking Impulse`, `Braking Net Impulse`, `L|R Braking Impulse Index`, `Relative Braking Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Metric ID versus label. In the CMJ, ID `positiveImpulse` carries label `Positive Net Impulse`, and IDs `relativeBrakingImpulse` and `relativePropulsiveImpulse` carry net labels. In the drop jump the same IDs carry gross labels ([hawkinR dictionary]). Map by label, not by ID.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Braking Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Braking Net Impulse(N.s/kg)`, metric ID `relativeBrakingNetImpulse`, `hawkinR` column `relative_braking_net_impulse_n_s_kg`, `hdforce` column `relative_braking_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking phase, per kilogram of system mass.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the braking phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `Braking Impulse`, `Braking Net Impulse`, `L|R Braking Impulse Index`, `Relative Braking Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `L|R Braking Impulse Index` (%)

This metric has these fields:

- Names: API column `L|R Braking Impulse Index(%)`, metric ID `lrBrakingImpulseIndex`, `hawkinR` column `l_r_braking_impulse_index_percent`, `hdforce` column `lr_braking_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for braking impulse, as a percentage.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Braking Impulse`, `Braking Net Impulse`, `Relative Braking Impulse`, `Relative Braking Net Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Braking Phase` (s)

This metric has these fields:

- Names: API column `Braking Phase(s)`, metric ID `brakingPhase`, `hawkinR` column `braking_phase_s`, `hdforce` column `braking_phase_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the braking phase lasts.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_b − t_a`. Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Phase start and end events.
- Units: s ([hawkinR dictionary]).
- Variants: `Braking Phase %`.
- Comparison with VALD ForceDecks: VALD drop landing duration, paired by Merrigan et al. (2022), who describe it as the eccentric phase ([Merrigan 2022]). The VALD glossary calls the drop landing to zero velocity window `Eccentric Duration` (ms) ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Braking Phase %` (%)

This metric has these fields:

- Names: API column `Braking Phase %`, metric ID `brakingPhasePercentage`, `hawkinR` column `braking_phase_percent`, `hdforce` column `braking_phase` ([hawkinR dictionary], [hdforce source]).
- What it measures: The braking phase as a percentage of the whole movement.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the braking phase as a share of the whole movement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × (t_b − t_a) / T_move`. Hawkin does not define the whole-movement duration further. Terms: `t_a` and `t_b` are the start and end of the window, in s; `T_move` is the duration of the whole movement, which Hawkin does not define further.
- Inputs: Phase start and end events.
- Units: % ([hawkinR dictionary]).
- Variants: `Braking Phase`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Avg. Braking RFD` (N/s)

This metric has these fields:

- Names: API column `Avg. Braking RFD(N/s)`, metric ID `avgBrakingRFD`, `hawkinR` column `avg_braking_rfd_n_s`, `hdforce` column `avg_braking_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_b) − F(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Left Avg. Braking RFD`, `L|R Avg. Braking RFD`, `Right Avg. Braking RFD`.
- What changes the number: Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary].

#### `Left Avg. Braking RFD` (N/s)

This metric has these fields:

- Names: API column `Left Avg. Braking RFD(N/s)`, metric ID `leftAvgBrakingRFD`, `hawkinR` column `left_avg_braking_rfd_n_s`, `hdforce` column `left_avg_braking_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises on the left plate during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean slope of the left vertical force over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F_L(t_b) − F_L(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Avg. Braking RFD`, `L|R Avg. Braking RFD`, `Right Avg. Braking RFD`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate].

#### `Right Avg. Braking RFD` (N/s)

This metric has these fields:

- Names: API column `Right Avg. Braking RFD(N/s)`, metric ID `rightAvgBrakingRFD`, `hawkinR` column `right_avg_braking_rfd_n_s`, `hdforce` column `right_avg_braking_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises on the right plate during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean slope of the right vertical force over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F_R(t_b) − F_R(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Avg. Braking RFD`, `Left Avg. Braking RFD`, `L|R Avg. Braking RFD`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate].

#### `L|R Avg. Braking RFD` (%)

This metric has these fields:

- Names: API column `L|R Avg. Braking RFD(%)`, metric ID `lrAvgBrakingRFD`, `hawkinR` column `l_r_avg_braking_rfd_percent`, `hdforce` column `lr_avg_braking_rfd` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average braking RFD, as a percentage.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean force slopes over the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of the left and right average slopes, `(F_L(t_b) − F_L(t_a)) / (t_b − t_a)` and the same for `F_R`. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Braking RFD`, `Left Avg. Braking RFD`, `Right Avg. Braking RFD`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Braking Force` (N)

This metric has these fields:

- Names: API column `Peak Braking Force(N)`, metric ID `peakBrakingForce`, `hawkinR` column `peak_braking_force_n`, `hdforce` column `peak_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the braking phase, including body weight.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Braking Force`, `L|R Peak Braking Force`, `Peak Relative Braking Force`, `Right Force at Peak Braking Force`.
- Comparison with VALD ForceDecks: `Peak Drop Landing Force` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). VALD searches the whole contact phase ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Peak Relative Braking Force` (%)

This metric has these fields:

- Names: API column `Peak Relative Braking Force(%)`, metric ID `peakRelativeBrakingForce`, `hawkinR` column `peak_relative_braking_force_percent`, `hdforce` column `peak_relative_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the braking phase, as a percentage of system weight.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the braking phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Braking Force`, `L|R Peak Braking Force`, `Peak Braking Force`, `Right Force at Peak Braking Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Left Force at Peak Braking Force` (N)

This metric has these fields:

- Names: API column `Left Force at Peak Braking Force(N)`, metric ID `leftPeakBrakingForce`, `hawkinR` column `left_force_at_peak_braking_force_n`, `hdforce` column `left_force_at_peak_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate at the instant of peak combined force in the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Braking Force`, `Peak Braking Force`, `Peak Relative Braking Force`, `Right Force at Peak Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Right Force at Peak Braking Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Braking Force(N)`, metric ID `rightPeakBrakingForce`, `hawkinR` column `right_force_at_peak_braking_force_n`, `hdforce` column `right_force_at_peak_braking_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Braking Force`, `L|R Peak Braking Force`, `Peak Braking Force`, `Peak Relative Braking Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `L|R Peak Braking Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Braking Force(%)`, metric ID `lrRatioPeakBrakingForce`, `hawkinR` column `l_r_peak_braking_force_percent`, `hdforce` column `lr_peak_braking_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak braking force, as a percentage.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Braking Force`, `Peak Braking Force`, `Peak Relative Braking Force`, `Right Force at Peak Braking Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Braking Power` (W)

This metric has these fields:

- Names: API column `Peak Braking Power(W)`, metric ID `peakBrakingPower`, `hawkinR` column `peak_braking_power_w`, `hdforce` column `peak_braking_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the braking phase.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Peak Relative Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Peak Relative Braking Power` (W/kg)

This metric has these fields:

- Names: API column `Peak Relative Braking Power(W/kg)`, metric ID `peakRelativeBrakingPower`, `hawkinR` column `peak_relative_braking_power_w_kg`, `hdforce` column `peak_relative_braking_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the braking phase, per kilogram of system mass.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the braking phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` `/ m` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Peak Braking Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Time to Peak Braking Force` (ms)

This metric has these fields:

- Names: API column `Time to Peak Braking Force(ms)`, metric ID `timeToPeakBrakingForce`, `hawkinR` column `time_to_peak_braking_force_ms`, `hdforce` column `time_to_peak_braking_force_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time from initial contact to peak braking force.
- Phase or window: Braking phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: zero velocity ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Time from initial contact to the moment of the highest instantaneous vertical force in the braking phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t* − t_contact`, with `t*` the instant of peak force in the braking phase ([hawkinR dictionary]). Terms: `t*` is the instant of peak combined force in the window.
- Inputs: Combined force and the contact event.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Units. The API reports this value in ms, while most Hawkin times are in s ([hawkinR dictionary]). Convert before you combine times.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin metric database].

#### `Countermovement Depth` (m)

This metric has these fields:

- Names: API column `Countermovement Depth(m)`, metric ID `depth`, `hawkinR` column `countermovement_depth_m`, `hdforce` column `countermovement_depth_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How far the center of mass drops below its starting height.
- Phase or window: The instant of zero velocity between braking and propulsion ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Lowest vertical position of the system center of mass, as a negative displacement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min s(t)` before take-off. The value is negative ([hawkinR dictionary]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement trace and drop height.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Countermovement Depth` (cm), displacement between drop landing and take-off ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump method].

#### `Force At Min Displacement` (N)

This metric has these fields:

- Names: API column `Force At Min Displacement(N)`, metric ID `forceAtMinDisplacement`, `hawkinR` column `force_at_min_displacement_n`, `hdforce` column `force_at_min_displacement_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip.
- Phase or window: The instant of zero velocity between braking and propulsion ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min)`, where `t_min` is the instant of `min s(t)`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement.
- Units: N ([hawkinR dictionary]).
- Variants: `Relative Force At Min Displacement`.
- Comparison with VALD ForceDecks: `Force at Zero Velocity` (N) ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Relative Force At Min Displacement` (%)

This metric has these fields:

- Names: API column `Relative Force At Min Displacement(%)`, metric ID `relativeForceAtMinDisplacement`, `hawkinR` column `relative_force_at_min_displacement_percent`, `hdforce` column `relative_force_at_min_displacement` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip, as a percentage of system weight.
- Phase or window: The instant of zero velocity between braking and propulsion ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Vertical force on the system center of mass at the moment of its lowest position, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_min) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m; `SW` is `System Weight`, in N.
- Inputs: Combined force, displacement, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Force At Min Displacement`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Stiffness` (N/m)

This metric has these fields:

- Names: API column `Stiffness(N/m)`, metric ID `stiffness`, `hawkinR` column `stiffness_n_m`, `hdforce` column `stiffness_n_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the dip divided by how far the center of mass dropped.
- Phase or window: The instant of zero velocity between braking and propulsion ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Vertical force at the moment of the lowest position, divided by the lowest displacement of the system center of mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min) / |min s(t)|` ([hawkinR dictionary]). Hawkin's text uses the negative displacement; the sign of the exported value is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement.
- Units: N/m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Spring-like behavior. Stiffness assumes peak force and lowest position happen together. Check this before you use it ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Avg. Propulsive Force(N)`, metric ID `avgPropulsiveForce`, `hawkinR` column `avg_propulsive_force_n`, `hdforce` column `avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase, including body weight.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: `Concentric Mean Force` (N) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Avg. Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Avg. Relative Propulsive Force(%)`, metric ID `avgRelativePropulsiveForce`, `hawkinR` column `avg_relative_propulsive_force_percent`, `hdforce` column `avg_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the propulsive phase, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the propulsive phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Left Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Propulsive Force(N)`, metric ID `leftAvgPropulsiveForce`, `hawkinR` column `left_avg_propulsive_force_n`, `hdforce` column `left_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `L|R Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Avg. Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Propulsive Force(N)`, metric ID `rightAvgPropulsiveForce`, `hawkinR` column `right_avg_propulsive_force_n`, `hdforce` column `right_avg_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `L|R Avg. Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `L|R Avg. Propulsive Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Propulsive Force(%)`, metric ID `lrAvgPropulsiveForce`, `hawkinR` column `l_r_avg_propulsive_force_percent`, `hdforce` column `lr_avg_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average propulsive force, as a percentage.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Force`, `Avg. Relative Propulsive Force`, `Left Avg. Propulsive Force`, `Right Avg. Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Propulsive Power` (W)

This metric has these fields:

- Names: API column `Avg. Propulsive Power(W)`, metric ID `avgPropulsivePower`, `hawkinR` column `avg_propulsive_power_w`, `hdforce` column `avg_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Avg. Relative Propulsive Power`.
- Comparison with VALD ForceDecks: `Concentric Mean Power` (W) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Avg. Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Avg. Relative Propulsive Power(W/kg)`, metric ID `avgRelativePropulsivePower`, `hawkinR` column `avg_relative_propulsive_power_w_kg`, `hdforce` column `avg_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Avg. Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Avg. Propulsive Velocity` (m/s)

This metric has these fields:

- Names: API column `Avg. Propulsive Velocity(m/s)`, metric ID `avgPropulsiveVelocity`, `hawkinR` column `avg_propulsive_velocity_m_s`, `hdforce` column `avg_propulsive_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average center of mass velocity during the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Mean vertical velocity of the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean v(t)` over the window ([hawkinR dictionary]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Peak Propulsive Force(N)`, metric ID `peakPropulsiveForce`, `hawkinR` column `peak_propulsive_force_n`, `hdforce` column `peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase, including body weight.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- Comparison with VALD ForceDecks: `Peak Drive-Off Force` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). VALD searches from the contact trough to take-off ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Peak Relative Propulsive Force` (%)

This metric has these fields:

- Names: API column `Peak Relative Propulsive Force(%)`, metric ID `peakRelativePropulsiveForce`, `hawkinR` column `peak_relative_propulsive_force_percent`, `hdforce` column `peak_relative_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the propulsive phase, as a percentage of system weight.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass in the propulsion phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Right Force at Peak Propulsive Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Left Force at Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Left Force at Peak Propulsive Force(N)`, metric ID `leftPeakPropulsiveForce`, `hawkinR` column `left_force_at_peak_propulsive_force_n`, `hdforce` column `left_force_at_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate at the instant of peak combined force in the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Force at Peak Propulsive Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Propulsive Force(N)`, metric ID `rightPeakPropulsiveForce`, `hawkinR` column `right_force_at_peak_propulsive_force_n`, `hdforce` column `right_force_at_peak_propulsive_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). It is the plate's share at the combined peak, not the plate's own peak. Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `L|R Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `L|R Peak Propulsive Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Propulsive Force(%)`, metric ID `lrPeakPropulsiveForce`, `hawkinR` column `l_r_peak_propulsive_force_percent`, `hdforce` column `lr_peak_propulsive_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak propulsive force, as a percentage.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Propulsive Force`, `Peak Propulsive Force`, `Peak Relative Propulsive Force`, `Right Force at Peak Propulsive Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Propulsive Power` (W)

This metric has these fields:

- Names: API column `Peak Propulsive Power(W)`, metric ID `peakPropulsivePower`, `hawkinR` column `peak_propulsive_power_w`, `hdforce` column `peak_propulsive_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Peak Relative Propulsive Power`.
- Comparison with VALD ForceDecks: `Peak Power` (W) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Peak Relative Propulsive Power` (W/kg)

This metric has these fields:

- Names: API column `Peak Relative Propulsive Power(W/kg)`, metric ID `peakRelativePropulsivePower`, `hawkinR` column `peak_relative_propulsive_power_w_kg`, `hdforce` column `peak_relative_propulsive_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Peak Propulsive Power`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Peak Velocity` (m/s)

This metric has these fields:

- Names: API column `Peak Velocity(m/s)`, metric ID `peakVelocity`, `hawkinR` column `peak_velocity_m_s`, `hdforce` column `peak_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest upward center of mass velocity before take-off.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical velocity of the system center of mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max v(t)` before take-off. The metric database places it in the propulsive phase ([Hawkin metric database]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Concentric Peak Velocity` (m/s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Propulsive Impulse` (N.s)

This metric has these fields:

- Names: API column `Propulsive Impulse(N.s)`, metric ID `propulsiveImpulse`, `hawkinR` column `propulsive_impulse_n_s`, `hdforce` column `propulsive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Net Impulse`, `Relative Propulsive Impulse`, `Relative Propulsive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Propulsive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Propulsive Net Impulse(N.s)`, metric ID `propulsiveNetImpulse`, `hawkinR` column `propulsive_net_impulse_n_s`, `hdforce` column `propulsive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Impulse`, `Relative Propulsive Impulse`, `Relative Propulsive Net Impulse`.
- Comparison with VALD ForceDecks: `Concentric Impulse` (N s) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Relative Propulsive Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Propulsive Impulse(N.s/kg)`, metric ID `relativePropulsiveImpulse`, `hawkinR` column `relative_propulsive_impulse_n_s_kg`, `hdforce` column `relative_propulsive_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse on the system center of mass over the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Impulse`, `Propulsive Net Impulse`, `Relative Propulsive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Metric ID versus label. In the CMJ, ID `positiveImpulse` carries label `Positive Net Impulse`, and IDs `relativeBrakingImpulse` and `relativePropulsiveImpulse` carry net labels. In the drop jump the same IDs carry gross labels ([hawkinR dictionary]). Map by label, not by ID.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Relative Propulsive Net Impulse` (N.s/kg)

This metric has these fields:

- Names: API column `Relative Propulsive Net Impulse(N.s/kg)`, metric ID `relativePropulsiveNetImpulse`, `hawkinR` column `relative_propulsive_net_impulse_n_s_kg`, `hdforce` column `relative_propulsive_net_impulse_n_s_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the propulsive phase, per kilogram of system mass.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse on the system center of mass over the propulsion phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` `/ m` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N; `m` is system mass, `SW / g`, in kg; `g` is 9.81 m/s².
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s/kg ([hawkinR dictionary]).
- Variants: `L|R Propulsive Impulse Index`, `Propulsive Impulse`, `Propulsive Net Impulse`, `Relative Propulsive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `L|R Propulsive Impulse Index` (%)

This metric has these fields:

- Names: API column `L|R Propulsive Impulse Index(%)`, metric ID `lrPropulsiveImpulseIndex`, `hawkinR` column `l_r_propulsive_impulse_index_percent`, `hdforce` column `lr_propulsive_impulse_index` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for propulsive impulse, as a percentage.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical impulses over the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `Σ F_L(t) × Δt` and `Σ F_R(t) × Δt` over the window. Whether Hawkin uses gross or net plate impulse is not published. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Propulsive Impulse`, `Propulsive Net Impulse`, `Relative Propulsive Impulse`, `Relative Propulsive Net Impulse`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Propulsive Phase` (s)

This metric has these fields:

- Names: API column `Propulsive Phase(s)`, metric ID `propulsivePhase`, `hawkinR` column `propulsive_phase_s`, `hdforce` column `propulsive_phase_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the propulsive phase lasts.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_b − t_a`. Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Phase start and end events.
- Units: s ([hawkinR dictionary]).
- Variants: `Propulsive Phase %`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Propulsive Phase %` (%)

This metric has these fields:

- Names: API column `Propulsive Phase %`, metric ID `propulsivePhasePercentage`, `hawkinR` column `propulsive_phase_percent`, `hdforce` column `propulsive_phase` ([hawkinR dictionary], [hdforce source]).
- What it measures: The propulsive phase as a percentage of the whole movement.
- Phase or window: Propulsive phase. Start: zero velocity. End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the propulsion phase as a share of the whole movement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × (t_b − t_a) / T_move`. Hawkin does not define the whole-movement duration further. Terms: `t_a` and `t_b` are the start and end of the window, in s; `T_move` is the duration of the whole movement, which Hawkin does not define further.
- Inputs: Phase start and end events.
- Units: % ([hawkinR dictionary]).
- Variants: `Propulsive Phase`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Contact Time` (s)

This metric has these fields:

- Names: API column `Contact Time(s)`, metric ID `contactTime`, `hawkinR` column `contact_time_s`, `hdforce` column `contact_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Ground contact time: braking phase plus propulsive phase.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Braking phase and propulsive phase durations added together ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `CT = t_takeoff − t_contact` ([hawkinR dictionary]).
- Inputs: Contact and take-off events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Contact Time` (s), drop landing to take-off ([Merrigan 2022], [VALD glossary]).
- What changes the number: Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary].

#### `Net Impulse Ratio`

This metric has these fields:

- Names: API column `Net Impulse Ratio`, metric ID `impulseRatio`, `hawkinR` column `net_impulse_ratio`, `hdforce` column `net_impulse_ratio` ([hawkinR dictionary], [hdforce source]).
- What it measures: Braking net impulse compared with propulsive net impulse.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse of the braking phase divided by net vertical impulse of the propulsion phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): The API dictionary gives braking net impulse divided by propulsive net impulse ([hawkinR dictionary]). The metric database page for the CMJ gives the inverse, propulsive net impulse divided by braking net impulse ([Hawkin metric database]). Check the value: a ratio above 1 in a normal jump suggests propulsive over braking.
- Inputs: Braking net impulse and propulsive net impulse.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Ratio direction. Hawkin sources disagree on which impulse is on top ([hawkinR dictionary], [Hawkin metric database]). Check the value against the two impulse columns. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump measures].

#### `mRSI`

This metric has these fields:

- Names: API column `mRSI`, metric ID `modifiedReactivityIndex`, `hawkinR` column `m_rsi`, `hdforce` column `mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Jump height divided by ground contact time.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Jump height from take-off velocity, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH / CT`, with `JH` from take-off velocity. Hawkin lists no unit; the inputs give m/s ([hawkinR dictionary], [Hawkin help, RSI and mRSI]). Terms: `JH` is jump height, in m; `CT` is contact time, in s.
- Inputs: Jump height and contact time.
- Units: None in the dictionary ([hawkinR dictionary]). The inputs give m/s.
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RSI (JH (Flight Time)/Contact Time)` (m/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). VALD uses flight-time jump height; Hawkin uses take-off velocity jump height ([VALD glossary], [Hawkin blog, take-off velocity]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these. Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, RSI and mRSI], [VALD glossary], [Hawkin blog, take-off velocity], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, flight time], [Hawkin blog, drop jump measures].

#### `Positive Impulse` (N.s)

This metric has these fields:

- Names: API column `Positive Impulse(N.s)`, metric ID `positiveImpulse`, `hawkinR` column `positive_impulse_n_s`, `hdforce` column `positive_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force including body weight added up over the braking and propulsive phases.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse of the braking and propulsion phases added together ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Inputs: Combined force and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Positive Net Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Metric ID versus label. In the CMJ, ID `positiveImpulse` carries label `Positive Net Impulse`, and IDs `relativeBrakingImpulse` and `relativePropulsiveImpulse` carry net labels. In the drop jump the same IDs carry gross labels ([hawkinR dictionary]). Map by label, not by ID.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Positive Net Impulse` (N.s)

This metric has these fields:

- Names: API column `Positive Net Impulse(N.s)`, metric ID `positiveNetImpulse`, `hawkinR` column `positive_net_impulse_n_s`, `hdforce` column `positive_net_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the braking and propulsive phases.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Vertical impulse above body weight, summed over the braking and propulsion phases ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `SW` is `System Weight`, in N.
- Note: Net impulse equals the change in momentum over the window.
- Inputs: Combined force, system weight, and the phase events.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Positive Impulse`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `RSI`

This metric has these fields:

- Names: API column `RSI`, metric ID `reactivityIndex`, `hawkinR` column `rsi`, `hdforce` column `rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: Flight time divided by ground contact time.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT / CT` ([hawkinR dictionary], [Hawkin help, RSI and mRSI]). Terms: `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Flight time and contact time.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RSI (Flight Time/Contact Time)` ([Merrigan 2022], [VALD glossary]).
- What changes the number: Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Contact detection. The force threshold for first contact sets the start of the braking phase ([Merrigan 2022]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin help, RSI and mRSI], [VALD glossary], [Hawkin blog, flight time], [Hawkin blog, drop jump measures].

#### `Spring Like Correlation`

This metric has these fields:

- Names: API column `Spring Like Correlation`, metric ID `springLikeCorrelation`, `hawkinR` column `spring_like_correlation`, `hdforce` column `spring_like_correlation` ([hawkinR dictionary], [hdforce source]).
- What it measures: How closely force rises and falls with the center of mass drop during contact, like a spring.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Pearson product-moment correlation between vertical force and vertical displacement of the system center of mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Pearson correlation `r` between `F(t)` and `s(t)` over ground contact ([hawkinR dictionary]). A perfect spring gives −1.0 ([Hawkin blog, drop jump measures]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force and displacement during contact.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [Hawkin blog, drop jump measures], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Time To Takeoff` (s)

This metric has these fields:

- Names: API column `Time To Takeoff(s)`, metric ID `timeToTakeoff`, `hawkinR` column `time_to_takeoff_s`, `hdforce` column `time_to_takeoff_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Ground contact time, from initial contact to take-off.
- Phase or window: Ground contact, the braking phase plus the propulsive phase. Start: initial contact, which Merrigan et al. (2022) report as force above 30 N held for 30 ms ([Merrigan 2022]). Velocity at contact comes from the estimated drop height: reverse integration, then flight time, then box height ([Hawkin blog, drop jump method]). End: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Time from initial contact to take-off ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_takeoff − t_contact`.
- Inputs: Start-of-movement (or contact) and take-off events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Contact Time` (s), drop landing to take-off ([VALD glossary]).
- What changes the number: Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [Hawkin blog, drop jump method], [hdforce dictionary], [VALD glossary], [Hawkin blog, two key factors], [Hawkin help, CMJ setup].

#### `Flight Time` (s)

This metric has these fields:

- Names: API column `Flight Time(s)`, metric ID `flightTime`, `hawkinR` column `flight_time_s`, `hdforce` column `flight_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time in the air.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Duration of the flight phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT = t_touchdown − t_takeoff`.
- Inputs: Take-off and touchdown events.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Flight Time` (ms in VALD) ([Merrigan 2022], [VALD glossary]).
- What changes the number: Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [VALD glossary], [Hawkin blog, flight time].

#### `Jump Height` (m)

This metric has these fields:

- Names: API column `Jump Height(m)`, metric ID `jumpHeight`, `hawkinR` column `jump_height_m`, `hdforce` column `jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How high the center of mass rises after take-off.
- Phase or window: Flight phase. Start: take-off, which Merrigan et al. (2022) report as force below 25 N held for 30 ms ([Merrigan 2022]). End: touchdown, force back above 25 N held for 30 ms ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Rise of the system center of mass from take-off to its highest point. It uses take-off velocity and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH = v_to² / (2 × g)` ([Hawkin blog, take-off velocity], [Hawkin RSI course]). Terms: `v_to` is velocity at take-off, in m/s; `g` is 9.81 m/s².
- Inputs: Take-off velocity, which needs system weight and the start-of-movement event and the drop height.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Jump Height (Imp-Mom)` (cm) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, take-off velocity], [Hawkin RSI course], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, CMJ setup], [Hawkin blog, drop jump method].

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
- Inputs: Combined force, system weight, start of movement, take-off, drop height.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Vertical Velocity at Take-off` (m/s) ([VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Start of movement. Movement before the jump, or a small rise before the dip, moves the start event and every later phase ([Hawkin blog, two key factors], [Hawkin help, CMJ setup]). Take-off detection. The threshold and hold time decide which samples count as contact ([Merrigan 2022]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [VALD glossary], [Hawkin blog, CMJ phases], [Hawkin help, CMJ setup], [Hawkin blog, drop jump method].

#### `Avg. Landing Force` (N)

This metric has these fields:

- Names: API column `Avg. Landing Force(N)`, metric ID `avgLandingForce`, `hawkinR` column `avg_landing_force_n`, `hdforce` column `avg_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the landing phase, including body weight.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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
- Units: N ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Left Force at Peak Landing Force`, `L|R Peak Landing Force`, `Relative Peak Landing Force`, `Right Force at Peak Landing Force`.
- Comparison with VALD ForceDecks: `Peak Landing Force` (N) ([Merrigan 2022], [VALD glossary]).
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin metric database], [Merrigan 2022], [VALD glossary], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

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
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]). Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, CMJ phases], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Right Force at Peak Landing Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Landing Force(N)`, metric ID `rightPeakLandingForce`, `hawkinR` column `right_force_at_peak_landing_force_n`, `hdforce` column `right_force_at_peak_landing_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the landing phase.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]).
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

#### `Box Height` (m)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: The box height you enter.
- Phase or window: Before contact: the fall from the box. Since an update announced on 2025-01-14, Hawkin estimates the true fall height by reverse integration from a still final second, falls back to flight time, and uses the entered box height only when the athlete does not land on the plates. An automatic tag names the method used ([Hawkin blog, drop jump method]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The user-entered box height ([Hawkin metric database]). Formula, restated (not Hawkin's text): The entered value. Hawkin uses it only when the athlete does not land back on the plates ([Hawkin blog, drop jump method]).
- Inputs: Your entry in the app.
- Units: m ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- Comparison with VALD ForceDecks: Not compared. VALD `Drop Height` can be entered by hand or calculated ([VALD glossary]), so it is not always the box height.
- What changes the number: Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin metric database], [VALD glossary].

#### `Landing Height` (m)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How far the center of mass falls from the top of the jump to touchdown.
- Phase or window: From the apex of the jump to touchdown ([Hawkin blog, landing metrics]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The free-fall height of the center of mass from the apex of the jump to contact ([Hawkin metric database]). Formula, restated (not Hawkin's text): `s(t_apex) − s(t_touchdown)`. How Hawkin computes it is not published. It is nearly always slightly more than jump height, because athletes land with the ankle less extended than at take-off ([Hawkin blog, landing metrics]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement or velocity at touchdown.
- Units: m ([Hawkin metric database]). The drop jump web page lists N, which is an error on that page.
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
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, drop jump measures]: https://www.hawkindynamics.com/blog/drop-jumps-what-to-measure
[Hawkin blog, drop jump method]: https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, landing metrics]: https://www.hawkindynamics.com/blog/new-landing-metrics
[Hawkin blog, take-off velocity]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, CMJ setup]: https://learning.hawkindynamics.com/knowledge/countermovement-jump-protocol
[Hawkin help, drop jump error]: https://learning.hawkindynamics.com/knowledge/processing-error-on-drop-jump
[Hawkin help, drop jump setup]: https://learning.hawkindynamics.com/knowledge/drop-jump-test-setup-guide
[Hawkin help, force plate data]: https://learning.hawkindynamics.com/knowledge/understanding-force-plate-data
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin help, RSI and mRSI]: https://learning.hawkindynamics.com/knowledge/what-is-the-difference-between-rsi-and-mrsi
[Hawkin help, time to stabilization]: https://learning.hawkindynamics.com/knowledge/how-do-i-use-time-to-stabilization
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[Hawkin RSI course]: https://www.hawkindynamics.com/hubfs/RSI%2BCourse%2B%E2%94%82%2BHawkin%2BDynamics%2BEdu.pdf
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
