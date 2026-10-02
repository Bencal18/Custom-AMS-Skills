# Hawkin Dynamics metrics: drop landing

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 40 metric blocks for the drop landing. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Drop landing

The athlete drops from a box and sticks the landing for at least 1 s ([Hawkin help, drop landing setup]). Hawkin splits the landing into impact and stabilization phases but does not publish their start and end events.

This section has 40 metric blocks. They follow the order of the movement.

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `weight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: Weighing phase ([hawkinR dictionary]). Which still period Hawkin uses for a drop landing is not published.
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases].

#### `Drop Height` (m)

This metric has these fields:

- Names: API column `Drop Height(m)`, metric ID `dropHeight`, `hawkinR` column `drop_height_m`, `hdforce` column `drop_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The height the center of mass falls before contact. It sets how hard the landing is.
- Phase or window: Before contact: the drop from the box ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Box height entered by the user. The software uses it to estimate the center of mass velocity at initial contact ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): The box height you enter, used to estimate contact velocity ([hawkinR dictionary]). Under free fall, contact velocity is `√(2 × g × h)`. Terms: `g` is 9.81 m/s².
- Inputs: Entered box height, and for the drop jump the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Stiffness` (N/m)

This metric has these fields:

- Names: API column `Stiffness(N/m)`, metric ID `stiffness`, `hawkinR` column `stiffness_n_m`, `hdforce` column `stiffness_n_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force at the lowest point of the landing divided by how far the center of mass dropped.
- Phase or window: The instant of peak negative center of mass displacement ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Vertical force at the moment of the lowest position, divided by the lowest displacement of the system center of mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_min) / |min s(t)|` ([hawkinR dictionary]). The sign of the exported value is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Combined force, displacement, and the contact velocity from drop height.
- Units: N/m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Drop jump method. Since an update announced on 2025-01-14, Hawkin estimates true drop height by reverse integration, then by flight time, then from box height. The method changes contact velocity and every velocity-based value. Check the automatic method tag on the trial ([Hawkin blog, drop jump method]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin blog, drop jump method].

#### `Stability Depth` (m)

This metric has these fields:

- Names: API column `Stability Depth(m)`, metric ID `depth`, `hawkinR` column `stability_depth_m`, `hdforce` column `stability_depth_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: How low the center of mass sits when the athlete has settled.
- Phase or window: The first sample of the stable period that ends time to stabilization ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time to stabilization starts at the first frame in which the athlete is stable. This metric is the vertical displacement, as a negative value, of the system center of mass at that frame ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `s(t)` at the first sample of the time to stabilization period ([hawkinR dictionary]). Terms: `s(t)` is center of mass vertical displacement from integrating velocity, in m.
- Inputs: Displacement trace and time to stabilization.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Settling. The value is blank if the athlete keeps moving or steps off after landing ([Hawkin help, time to stabilization]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, time to stabilization], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Contact Velocity` (m/s)

This metric has these fields:

- Names: API column `Contact Velocity(m/s)`, metric ID `contactVelocity`, `hawkinR` column `contact_velocity_m_s`, `hdforce` column `contact_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast the center of mass moves down when the feet hit the plates.
- Phase or window: The instant of contact with the plates ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Vertical velocity of the system center of mass at contact ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `v(t_contact)`, estimated from drop height ([hawkinR dictionary]). Hawkin does not publish the formula; free fall gives `−√(2 × g × h)`. Terms: `g` is 9.81 m/s².
- Inputs: Drop height.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Peak Force` (N)

This metric has these fields:

- Names: API column `Peak Force(N)`, metric ID `peakForce`, `hawkinR` column `peak_force_n`, `hdforce` column `peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the drop landing.
- Phase or window: The whole drop landing ([hawkinR dictionary]). The start and end events are not published.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass during the drop landing ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the drop landing ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force and system weight.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Force`, `L|R Peak Force`, `Peak Relative Force`, `Right Force at Peak Force`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Peak Relative Force` (%)

This metric has these fields:

- Names: API column `Peak Relative Force(%)`, metric ID `peakRelativeForce`, `hawkinR` column `peak_relative_force_percent`, `hdforce` column `peak_relative_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the drop landing, as a percentage of system weight.
- Phase or window: The whole drop landing ([hawkinR dictionary]). The start and end events are not published.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass during the drop landing, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW` ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined force and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Force`, `L|R Peak Force`, `Peak Force`, `Right Force at Peak Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Left Force at Peak Force` (N)

This metric has these fields:

- Names: API column `Left Force at Peak Force(N)`, metric ID `leftPeakForce`, `hawkinR` column `left_force_at_peak_force_n`, `hdforce` column `left_force_at_peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate at the instant of peak combined force in the drop landing.
- Phase or window: The whole drop landing ([hawkinR dictionary]). The start and end events are not published.
- Calculation: Hawkin's definition, paraphrased: Left vertical force at the moment of the highest instantaneous vertical force in the drop landing ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t*)` ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Plate force traces.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Force`, `Peak Force`, `Peak Relative Force`, `Right Force at Peak Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Right Force at Peak Force` (N)

This metric has these fields:

- Names: API column `Right Force at Peak Force(N)`, metric ID `rightPeakForce`, `hawkinR` column `right_force_at_peak_force_n`, `hdforce` column `right_force_at_peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate at the instant of peak combined force in the drop landing.
- Phase or window: The whole drop landing ([hawkinR dictionary]). The start and end events are not published.
- Calculation: Hawkin's definition, paraphrased: Right vertical force at the moment of the highest instantaneous vertical force in the drop landing ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t*)` ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Plate force traces.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at Peak Force`, `L|R Peak Force`, `Peak Force`, `Peak Relative Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `L|R Peak Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Force(%)`, metric ID `lrPeakForce`, `hawkinR` column `l_r_peak_force_percent`, `hdforce` column `lr_peak_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak force, as a percentage.
- Phase or window: The whole drop landing ([hawkinR dictionary]). The start and end events are not published.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the drop landing ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Force at Peak Force`, `Peak Force`, `Peak Relative Force`, `Right Force at Peak Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Impact Force` (N)

This metric has these fields:

- Names: API column `Avg. Impact Force(N)`, metric ID `avgImpactForce`, `hawkinR` column `avg_impact_force_n`, `hdforce` column `avg_impact_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the impact phase, including body weight.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Relative Impact Force`, `Left Avg. Impact Force`, `L|R Avg. Impact Force`, `Right Avg. Impact Force`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Relative Impact Force` (%)

This metric has these fields:

- Names: API column `Avg. Relative Impact Force(%)`, metric ID `avgRelativeImpactForce`, `hawkinR` column `avg_relative_impact_force_percent`, `hdforce` column `avg_relative_impact_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the impact phase, as a percentage of system weight.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the impact phase, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × mean F(t) / SW` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Force, the phase events, and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Impact Force`, `Left Avg. Impact Force`, `L|R Avg. Impact Force`, `Right Avg. Impact Force`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Left Avg. Impact Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Impact Force(N)`, metric ID `leftAvgImpactForce`, `hawkinR` column `left_avg_impact_force_n`, `hdforce` column `left_avg_impact_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Impact Force`, `Avg. Relative Impact Force`, `L|R Avg. Impact Force`, `Right Avg. Impact Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Right Avg. Impact Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Impact Force(N)`, metric ID `rightAvgImpactForce`, `hawkinR` column `right_avg_impact_force_n`, `hdforce` column `right_avg_impact_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Impact Force`, `Avg. Relative Impact Force`, `Left Avg. Impact Force`, `L|R Avg. Impact Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `L|R Avg. Impact Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Impact Force(%)`, metric ID `lrAvgImpactForce`, `hawkinR` column `l_r_avg_impact_force_percent`, `hdforce` column `lr_avg_impact_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average impact force, as a percentage.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Impact Force`, `Avg. Relative Impact Force`, `Left Avg. Impact Force`, `Right Avg. Impact Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Impact Power` (W)

This metric has these fields:

- Names: API column `Avg. Impact Power(W)`, metric ID `avgImpactPower`, `hawkinR` column `avg_impact_power_w`, `hdforce` column `avg_impact_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Avg. Relative Impact Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Relative Impact Power` (W/kg)

This metric has these fields:

- Names: API column `Avg. Relative Impact Power(W/kg)`, metric ID `avgRelativeImpactPower`, `hawkinR` column `avg_relative_impact_power_w_kg`, `hdforce` column `avg_relative_impact_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the impact phase, per kilogram of system mass.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the impact phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Avg. Impact Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Impact Velocity` (m/s)

This metric has these fields:

- Names: API column `Avg. Impact Velocity(m/s)`, metric ID `avgImpactVelocity`, `hawkinR` column `avg_impact_velocity_m_s`, `hdforce` column `avg_impact_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average center of mass velocity during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean vertical velocity of the system center of mass over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean v(t)` over the window ([hawkinR dictionary]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Impact Phase` (s)

This metric has these fields:

- Names: API column `Impact Phase(s)`, metric ID `impactPhase`, `hawkinR` column `impact_phase_s`, `hdforce` column `impact_phase_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the impact phase lasts.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Duration of the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_b − t_a`. Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Phase start and end events.
- Units: s ([hawkinR dictionary]).
- Variants: `Impact Phase %`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Impact Phase %` (%)

This metric has these fields:

- Names: API column `Impact Phase %`, metric ID `impactPhasePercentage`, `hawkinR` column `impact_phase_percent`, `hdforce` column `impact_phase` ([hawkinR dictionary], [hdforce source]).
- What it measures: The impact phase as a percentage of the whole movement.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Duration of the impact phase as a share of the whole movement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × (t_b − t_a) / T_move`. Hawkin does not define the whole-movement duration further. Terms: `t_a` and `t_b` are the start and end of the window, in s; `T_move` is the duration of the whole movement, which Hawkin does not define further.
- Inputs: Phase start and end events.
- Units: % ([hawkinR dictionary]).
- Variants: `Impact Phase`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Impact RFD` (N/s)

This metric has these fields:

- Names: API column `Impact RFD(N/s)`, metric ID `impactRFD`, `hawkinR` column `impact_rfd_n_s`, `hdforce` column `impact_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_b) − F(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Left Impact RFD`, `L|R Impact RFD`, `Right Impact RFD`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height], [Merrigan 2022].

#### `Left Impact RFD` (N/s)

This metric has these fields:

- Names: API column `Left Impact RFD(N/s)`, metric ID `leftImpactRFD`, `hawkinR` column `left_impact_rfd_n_s`, `hdforce` column `left_impact_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises on the left plate during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the left vertical force over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F_L(t_b) − F_L(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Impact RFD`, `L|R Impact RFD`, `Right Impact RFD`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height], [Merrigan 2022].

#### `Right Impact RFD` (N/s)

This metric has these fields:

- Names: API column `Right Impact RFD(N/s)`, metric ID `rightImpactRFD`, `hawkinR` column `right_impact_rfd_n_s`, `hdforce` column `right_impact_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises on the right plate during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the right vertical force over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F_R(t_b) − F_R(t_a)) / (t_b − t_a)`, the average slope ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Force and the phase events.
- Units: N/s ([hawkinR dictionary]).
- Variants: `Impact RFD`, `Left Impact RFD`, `L|R Impact RFD`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height], [Merrigan 2022].

#### `L|R Impact RFD` (%)

This metric has these fields:

- Names: API column `L|R Impact RFD(%)`, metric ID `lrImpactRFD`, `hawkinR` column `l_r_impact_rfd_percent`, `hdforce` column `lr_impact_rfd` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for impact RFD, as a percentage.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean force slopes over the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of the left and right average slopes, `(F_L(t_b) − F_L(t_a)) / (t_b − t_a)` and the same for `F_R`. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Impact RFD`, `Left Impact RFD`, `Right Impact RFD`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Impact Power` (W)

This metric has these fields:

- Names: API column `Peak Impact Power(W)`, metric ID `peakImpactPower`, `hawkinR` column `peak_impact_power_w`, `hdforce` column `peak_impact_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the impact phase.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the impact phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Peak Relative Impact Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Peak Relative Impact Power` (W/kg)

This metric has these fields:

- Names: API column `Peak Relative Impact Power(W/kg)`, metric ID `peakRelativeImpactPower`, `hawkinR` column `peak_relative_impact_power_w_kg`, `hdforce` column `peak_relative_impact_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The largest braking power during the impact phase, per kilogram of system mass.
- Phase or window: Impact phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Most negative instantaneous mechanical power on the system center of mass in the impact phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `min P(t)` `/ m` over the window ([hawkinR dictionary]). Hawkin calls it the peak negative power, so it is the most negative value. Whether the export keeps the minus sign is not published. Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Peak Impact Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Stabilization Force` (N)

This metric has these fields:

- Names: API column `Avg. Stabilization Force(N)`, metric ID `avgStabilizationForce`, `hawkinR` column `avg_stabilization_force_n`, `hdforce` column `avg_stabilization_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the stabilization phase, including body weight.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the window ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Avg. Stabilization Force`, `L|R Avg. Stabilization Force`, `Right Avg. Stabilization Force`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Left Avg. Stabilization Force` (N)

This metric has these fields:

- Names: API column `Left Avg. Stabilization Force(N)`, metric ID `leftAvgStabilizationForce`, `hawkinR` column `left_avg_stabilization_force_n`, `hdforce` column `left_avg_stabilization_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the left plate during the stabilization phase.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean left vertical force on the system center of mass over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_L(t)` over the window ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Stabilization Force`, `L|R Avg. Stabilization Force`, `Right Avg. Stabilization Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Right Avg. Stabilization Force` (N)

This metric has these fields:

- Names: API column `Right Avg. Stabilization Force(N)`, metric ID `rightAvgStabilizationForce`, `hawkinR` column `right_avg_stabilization_force_n`, `hdforce` column `right_avg_stabilization_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force on the right plate during the stabilization phase.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean right vertical force on the system center of mass over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F_R(t)` over the window ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Force and the phase events.
- Units: N ([hawkinR dictionary]).
- Variants: `Avg. Stabilization Force`, `Left Avg. Stabilization Force`, `L|R Avg. Stabilization Force`.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin help, left and right plate], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `L|R Avg. Stabilization Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Stabilization Force(%)`, metric ID `lrAvgStabilizationForce`, `hawkinR` column `l_r_avg_stabilization_force_percent`, `hdforce` column `lr_avg_stabilization_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average stabilization force, as a percentage.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Stabilization Force`, `Left Avg. Stabilization Force`, `Right Avg. Stabilization Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Relative Stabilization Power` (W/kg)

This metric has these fields:

- Names: API column `Avg. Relative Stabilization Power(W/kg)`, metric ID `avgRelativeStabilizationPower`, `hawkinR` column `avg_relative_stabilization_power_w_kg`, `hdforce` column `avg_relative_stabilization_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the stabilization phase, per kilogram of system mass.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the stabilization phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Avg. Stabilization Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Stabilization Power` (W)

This metric has these fields:

- Names: API column `Avg. Stabilization Power(W)`, metric ID `avgStabilizationPower`, `hawkinR` column `avg_stabilization_power_w`, `hdforce` column `avg_stabilization_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average power during the stabilization phase.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean mechanical power on the system center of mass over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Avg. Relative Stabilization Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Avg. Stabilization Velocity` (m/s)

This metric has these fields:

- Names: API column `Avg. Stabilization Velocity(m/s)`, metric ID `avgStabilizationVelocity`, `hawkinR` column `avg_stabilization_velocity_m_s`, `hdforce` column `avg_stabilization_velocity_m_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average center of mass velocity during the stabilization phase.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Mean vertical velocity of the system center of mass over the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean v(t)` over the window ([hawkinR dictionary]). Terms: `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Velocity trace.
- Units: m/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Peak Relative Stabilization Power` (W/kg)

This metric has these fields:

- Names: API column `Peak Relative Stabilization Power(W/kg)`, metric ID `peakRelativeStabilizationPower`, `hawkinR` column `peak_relative_stabilization_power_w_kg`, `hdforce` column `peak_relative_stabilization_power_w_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the stabilization phase, per kilogram of system mass.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the stabilization phase, per unit of system mass ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` `/ m` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s; `m` is system mass, `SW / g`, in kg.
- Inputs: Combined force and velocity.
- Units: W/kg ([hawkinR dictionary]).
- Variants: `Peak Stabilization Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Peak Stabilization Power` (W)

This metric has these fields:

- Names: API column `Peak Stabilization Power(W)`, metric ID `peakStabilizationPower`, `hawkinR` column `peak_stabilization_power_w`, `hdforce` column `peak_stabilization_power_w` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest power during the stabilization phase.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous mechanical power on the system center of mass in the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max P(t)` over the window ([hawkinR dictionary]). Terms: `P(t)` is power, `F(t) × v(t)`, in W; `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `v(t)` is center of mass vertical velocity from integrating net force divided by mass, in m/s.
- Inputs: Combined force and velocity.
- Units: W ([hawkinR dictionary]).
- Variants: `Peak Relative Stabilization Power`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Stabilization Phase` (s)

This metric has these fields:

- Names: API column `Stabilization Phase(s)`, metric ID `stabilizationPhase`, `hawkinR` column `stabilization_phase_s`, `hdforce` column `stabilization_phase_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the stabilization phase lasts.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Duration of the stabilization phase ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_b − t_a`. Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Phase start and end events.
- Units: s ([hawkinR dictionary]).
- Variants: `Stabilization Phase %`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Stabilization Phase %` (%)

This metric has these fields:

- Names: API column `Stabilization Phase %`, metric ID `stabilizationPhasePercentage`, `hawkinR` column `stabilization_phase_percent`, `hdforce` column `stabilization_phase` ([hawkinR dictionary], [hdforce source]).
- What it measures: The stabilization phase as a percentage of the whole movement.
- Phase or window: Stabilization phase ([hawkinR dictionary]). Hawkin does not publish its start and end events.
- Calculation: Hawkin's definition, paraphrased: Duration of the stabilization phase as a share of the whole movement ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × (t_b − t_a) / T_move`. Hawkin does not define the whole-movement duration further. Terms: `t_a` and `t_b` are the start and end of the window, in s; `T_move` is the duration of the whole movement, which Hawkin does not define further.
- Inputs: Phase start and end events.
- Units: % ([hawkinR dictionary]).
- Variants: `Stabilization Phase`.
- What changes the number: Entered box height. The drop landing estimates contact velocity from the box height you enter ([hawkinR dictionary]). Athletes who step down or jump off the box fall a different height ([Hawkin blog, drop jump method], [Hawkin help, drop height]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, drop jump method], [Hawkin help, drop height].

#### `Time To Stabilization` (ms)

This metric has these fields:

- Names: API column `Time To Stabilization(ms)`, metric ID `timeToStabilization`, `hawkinR` column `time_to_stabilization_ms`, `hdforce` column `time_to_stabilization_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the athlete takes to settle after landing.
- Phase or window: From touchdown to the start of the first 1 s period with force within 5% of system weight ([Hawkin blog, landing metrics], [hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time until vertical force stays within 5% of system weight for 1 s ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Time from touchdown to the first sample of a 1 s period where `|F(t) − SW| ≤ 0.05 × SW` ([hawkinR dictionary], [Hawkin blog, landing metrics]). The value is blank when the athlete keeps moving or steps off ([Hawkin help, time to stabilization]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined force after touchdown and system weight.
- Units: ms ([hawkinR dictionary]). The metric database web page lists `Seconds (s)` ([Hawkin metric database]), which disagrees.
- Variants: None in this test.
- What changes the number: Settling. The value is blank if the athlete keeps moving or steps off after landing ([Hawkin help, time to stabilization]). Units. The API reports this value in ms, while most Hawkin times are in s ([hawkinR dictionary]). Convert before you combine times.
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin blog, landing metrics], [hdforce dictionary], [Hawkin help, time to stabilization], [Hawkin metric database].

#### `Landing Phase` (s)

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: How long the landing takes, from touchdown until the athlete stops moving down.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, landing metrics], [Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased from the metric database: The time from touchdown to the first instant of zero center of mass velocity ([Hawkin metric database]). Formula, restated (not Hawkin's text): `t_b − t_a`. It differs from `Time to Stabilization`, which waits for 1 s of steady force ([Hawkin blog, landing metrics]). Terms: `t_a` and `t_b` are the start and end of the window, in s.
- Inputs: Touchdown and the velocity trace.
- Units: s ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). Integration drift. Velocity and displacement drift as the trial gets longer, so post-landing values carry more error ([Hawkin blog, two key factors], [Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, two key factors], [Hawkin blog, flight time].

#### `Landing Performance Index`

This metric appears only on the Hawkin metric database web page. It has these fields:

- Names: API column, metric ID, and package column are not published. The metric is missing from the `MetricDictionary` in `hawkinR` 2.0.1 and `hdforce` 2.1.0 ([hawkinR dictionary], [hdforce dictionary]).
- What it measures: Landing height per second of landing time. Higher means the athlete stops a bigger fall faster.
- Phase or window: Landing phase. Start: touchdown. End: the first instant center of mass velocity returns to zero ([Hawkin blog, landing metrics], [Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased from the metric database: Landing height divided by landing time ([Hawkin metric database]). Formula, restated (not Hawkin's text): `Landing Height / Landing Phase` ([Hawkin blog, landing metrics]). In the drop landing, Hawkin does not publish whether drop height replaces landing height.
- Inputs: Landing height and landing phase.
- Units: None ([Hawkin metric database]).
- Variants: See the other metrics in this group.
- What changes the number: Landing demand. Landing height sets the braking demand of the landing ([Hawkin blog, landing metrics]). Both parts. A ratio can stay the same while both parts change. Read the parts as well ([Hawkin blog, drop jump measures]).
- Sources: [hawkinR dictionary], [hdforce dictionary], [Hawkin blog, landing metrics], [Hawkin metric database], [Hawkin blog, drop jump measures].

[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, drop jump measures]: https://www.hawkindynamics.com/blog/drop-jumps-what-to-measure
[Hawkin blog, drop jump method]: https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, landing metrics]: https://www.hawkindynamics.com/blog/new-landing-metrics
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, drop height]: https://learning.hawkindynamics.com/knowledge/do-you-have-to-measure-drop-height-when-performing-a-drop-jump
[Hawkin help, drop landing setup]: https://learning.hawkindynamics.com/knowledge/drop-landing-setupguide
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin help, time to stabilization]: https://learning.hawkindynamics.com/knowledge/how-do-i-use-time-to-stabilization
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
