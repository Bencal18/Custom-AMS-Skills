# Hawkin Dynamics metrics: multi rebound

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 29 metric blocks for the multi rebound. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Multi rebound

The athlete hops continuously for a set time, for example the 10/5 or 5/3 protocol ([Hawkin help, multi rebound setup]). Hawkin calculates jump height from flight time for this test ([Hawkin blog, flight time]).

This section has 29 metric blocks. They follow the order of the movement.

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `weight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: Weighing phase before the first jump ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases].

#### `Avg. Contact Time` (s)

This metric has these fields:

- Names: API column `Avg. Contact Time(s)`, metric ID `avgContactTime`, `hawkinR` column `avg_contact_time_s`, `hdforce` column `avg_contact_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Average contact time over all jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean contact time of every jump in the multi rebound, measured from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean CT_j` over all jumps, where each `CT_j` runs from initial contact to take-off ([hawkinR dictionary]). Terms: `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Avg. Force` (N)

This metric has these fields:

- Names: API column `Avg. Force(N)`, metric ID `avgForce`, `hawkinR` column `avg_force_n`, `hdforce` column `avg_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average total force during the trial.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean vertical force on the system center of mass over the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the trial ([hawkinR dictionary]). Whether flight samples count in the mean is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Avg. Force`.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `L|R Avg. Force` (%)

This metric has these fields:

- Names: API column `L|R Avg. Force(%)`, metric ID `lrAvgForce`, `hawkinR` column `l_r_avg_force_percent`, `hdforce` column `lr_avg_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for average force, as a percentage.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right mean vertical forces over the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `mean F_L(t)` and `mean F_R(t)` over the window. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Avg. Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Avg. Jump Height` (m)

This metric has these fields:

- Names: API column `Avg. Jump Height(m)`, metric ID `avgJumpHeight`, `hawkinR` column `avg_jump_height_m`, `hdforce` column `avg_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average jump height over all jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean of every jump height in the multi rebound. Each height comes from time in the air and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean JH_j`, jump height from flight time, `g × FT² / 8`, per jump ([Hawkin blog, flight time], [hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `g` is 9.81 m/s².
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Avg. mRSI`

This metric has these fields:

- Names: API column `Avg. mRSI`, metric ID `avgMRsi`, `hawkinR` column `avg_m_rsi`, `hdforce` column `avg_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average mRSI over all jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean mRSI of every jump in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `JH_j / CT_j`, with flight-time jump height over all jumps ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Avg. RSI`

This metric has these fields:

- Names: API column `Avg. RSI`, metric ID `avgRsi`, `hawkinR` column `avg_rsi`, `hdforce` column `avg_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average RSI over all jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean RSI of every jump in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `FT_j / CT_j` over all jumps ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Number of Jumps` (Count)

This metric has these fields:

- Names: API column `Number of Jumps(Count)`, metric ID `jumpCount`, `hawkinR` column `number_of_jumps_count`, `hdforce` column `number_of_jumps_count` ([hawkinR dictionary], [hdforce source]).
- What it measures: How many jumps the software found in the trial.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Count of jumps in the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Count of detected jumps ([hawkinR dictionary]).
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: Count ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Peak Force` (N)

This metric has these fields:

- Names: API column `Peak Force(N)`, metric ID `peakForce`, `hawkinR` column `peak_force_n`, `hdforce` column `peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the trial.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force on the system center of mass during the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` over the trial ([hawkinR dictionary]). Whether flight samples count in the mean is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Force`.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `L|R Peak Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Force(%)`, metric ID `lrPeakForce`, `hawkinR` column `l_r_peak_force_percent`, `hdforce` column `lr_peak_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak force, as a percentage.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right peak instantaneous vertical forces during the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Peak Force`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

#### `Peak Jump Height` (m)

This metric has these fields:

- Names: API column `Peak Jump Height(m)`, metric ID `peakJumpHeight`, `hawkinR` column `peak_jump_height_m`, `hdforce` column `peak_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest single jump in the trial.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest jump height in the multi rebound, from time in the air and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max JH_j`, jump height from flight time, `g × FT² / 8`, per jump ([Hawkin blog, flight time], [hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `g` is 9.81 m/s².
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Peak Jump mRSI`

This metric has these fields:

- Names: API column `Peak Jump mRSI`, metric ID `peakJumpMRsi`, `hawkinR` column `peak_jump_m_rsi`, `hdforce` column `peak_jump_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: mRSI of the highest jump.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Jump height from time in the air for the highest jump in the multi rebound, divided by that jump's time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `JH_j / CT_j`, with flight-time jump height, for the jump with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Peak Jump RSI`

This metric has these fields:

- Names: API column `Peak Jump RSI`, metric ID `peakJumpRsi`, `hawkinR` column `peak_jump_rsi`, `hdforce` column `peak_jump_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: RSI of the highest jump.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Flight time of the highest jump in the multi rebound, divided by that jump's time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `FT_j / CT_j`, for the jump with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Peak mRSI`

This metric has these fields:

- Names: API column `Peak mRSI`, metric ID `peakMRsi`, `hawkinR` column `peak_m_rsi`, `hdforce` column `peak_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest mRSI of any jump.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest mRSI in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `JH_j / CT_j`, with flight-time jump height ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Peak RSI`

This metric has these fields:

- Names: API column `Peak RSI`, metric ID `peakRsi`, `hawkinR` column `peak_rsi`, `hdforce` column `peak_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest RSI of any jump.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest RSI in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `FT_j / CT_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 3 Jumps Avg. Contact Time` (s)

This metric has these fields:

- Names: API column `Top 3 Jumps Avg. Contact Time(s)`, metric ID `top3AvgContactTime`, `hawkinR` column `top_3_jumps_avg_contact_time_s`, `hdforce` column `top_3_jumps_avg_contact_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Average contact time over the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean contact time of the three highest jumps in the multi rebound, measured from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean CT_j` over the three highest jumps, where each `CT_j` runs from initial contact to take-off ([hawkinR dictionary]). Terms: `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Top 3 Jumps Avg. Jump Height` (m)

This metric has these fields:

- Names: API column `Top 3 Jumps Avg. Jump Height(m)`, metric ID `top3AvgJumpHeight`, `hawkinR` column `top_3_jumps_avg_jump_height_m`, `hdforce` column `top_3_jumps_avg_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average of the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean of the three highest jump heights in the multi rebound. Each height comes from time in the air and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Mean of the three largest `JH_j`, jump height from flight time, `g × FT² / 8`, per jump ([Hawkin blog, flight time], [hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `g` is 9.81 m/s².
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Top 3 Jumps Avg. mRSI`

This metric has these fields:

- Names: API column `Top 3 Jumps Avg. mRSI`, metric ID `top3AvgMRsi`, `hawkinR` column `top_3_jumps_avg_m_rsi`, `hdforce` column `top_3_jumps_avg_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average mRSI of the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean mRSI of the three highest jumps in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `JH_j / CT_j`, with flight-time jump height over the three jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 3 Jumps Avg. RSI`

This metric has these fields:

- Names: API column `Top 3 Jumps Avg. RSI`, metric ID `top3AvgRsi`, `hawkinR` column `top_3_jumps_avg_rsi`, `hdforce` column `top_3_jumps_avg_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average RSI of the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean RSI of the three highest jumps in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `FT_j / CT_j` over the three jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 3 Jumps Peak mRSI`

This metric has these fields:

- Names: API column `Top 3 Jumps Peak mRSI`, metric ID `top3PeakMRsi`, `hawkinR` column `top_3_jumps_peak_m_rsi`, `hdforce` column `top_3_jumps_peak_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest mRSI among the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest mRSI among the three highest jumps in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `JH_j / CT_j`, with flight-time jump height over the three jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 3 Jumps Peak RSI`

This metric has these fields:

- Names: API column `Top 3 Jumps Peak RSI`, metric ID `top3PeakRsi`, `hawkinR` column `top_3_jumps_peak_rsi`, `hdforce` column `top_3_jumps_peak_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest RSI among the three highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest RSI among the three highest jumps in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `FT_j / CT_j` over the three jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 5 Jumps Avg. Contact Time` (s)

This metric has these fields:

- Names: API column `Top 5 Jumps Avg. Contact Time(s)`, metric ID `top5AvgContactTime`, `hawkinR` column `top_5_jumps_avg_contact_time_s`, `hdforce` column `top_5_jumps_avg_contact_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Average contact time over the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean contact time of the five highest jumps in the multi rebound, measured from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean CT_j` over the five highest jumps, where each `CT_j` runs from initial contact to take-off ([hawkinR dictionary]). Terms: `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Top 5 Jumps Avg. Jump Height` (m)

This metric has these fields:

- Names: API column `Top 5 Jumps Avg. Jump Height(m)`, metric ID `top5AvgJumpHeight`, `hawkinR` column `top_5_jumps_avg_jump_height_m`, `hdforce` column `top_5_jumps_avg_jump_height_m` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average of the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean of the five highest jump heights in the multi rebound. Each height comes from time in the air and the equations for uniformly accelerated motion ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Mean of the five largest `JH_j`, jump height from flight time, `g × FT² / 8`, per jump ([Hawkin blog, flight time], [hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `g` is 9.81 m/s².
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: m ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Top 5 Jumps Avg. mRSI`

This metric has these fields:

- Names: API column `Top 5 Jumps Avg. mRSI`, metric ID `top5AvgMRsi`, `hawkinR` column `top_5_jumps_avg_m_rsi`, `hdforce` column `top_5_jumps_avg_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average mRSI of the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean mRSI of the five highest jumps in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `JH_j / CT_j`, with flight-time jump height over the five jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 5 Jumps Avg. RSI`

This metric has these fields:

- Names: API column `Top 5 Jumps Avg. RSI`, metric ID `top5AvgRsi`, `hawkinR` column `top_5_jumps_avg_rsi`, `hdforce` column `top_5_jumps_avg_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average RSI of the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Mean RSI of the five highest jumps in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean` of `FT_j / CT_j` over the five jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 5 Jumps Peak mRSI`

This metric has these fields:

- Names: API column `Top 5 Jumps Peak mRSI`, metric ID `top5PeakMRsi`, `hawkinR` column `top_5_jumps_peak_m_rsi`, `hdforce` column `top_5_jumps_peak_mrsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest mRSI among the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest mRSI among the five highest jumps in the multi rebound. Each mRSI is jump height from time in the air, divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `JH_j / CT_j`, with flight-time jump height over the five jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Top 5 Jumps Peak RSI`

This metric has these fields:

- Names: API column `Top 5 Jumps Peak RSI`, metric ID `top5PeakRsi`, `hawkinR` column `top_5_jumps_peak_rsi`, `hdforce` column `top_5_jumps_peak_rsi` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest RSI among the five highest jumps.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Highest RSI among the five highest jumps in the multi rebound. Each RSI is flight time divided by the time from initial contact to take-off (called Time to Take-off) ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max` of `FT_j / CT_j` over the five jumps with the largest `JH_j` ([hawkinR dictionary]). Terms: `JH` is jump height, in m; `FT` is flight time, in s; `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: None in the dictionary ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]). Leg tuck. Tucking the legs in the air lengthens flight time and inflates flight-time values ([Hawkin blog, flight time]). Jump height method. Hawkin uses take-off velocity for the CMJ, squat jump, CMJ rebound, and drop jump, and flight time for the multi rebound ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]). Do not compare RSI-type values across these.
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time], [Hawkin blog, take-off velocity].

#### `Total Contact Time` (s)

This metric has these fields:

- Names: API column `Total Contact Time(s)`, metric ID `totalContactTime`, `hawkinR` column `total_contact_time_s`, `hdforce` column `total_contact_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: All contact times added together.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Sum of the contact times of every jump in the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ CT_j` over all jumps ([hawkinR dictionary]). Terms: `CT` is contact time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

#### `Total Flight Time` (s)

This metric has these fields:

- Names: API column `Total Flight Time(s)`, metric ID `totalFlightTime`, `hawkinR` column `total_flight_time_s`, `hdforce` column `total_flight_time_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: All flight times added together.
- Phase or window: The whole multi rebound trial ([hawkinR dictionary]). Each jump runs from initial contact to take-off, then flight. Contact and take-off thresholds for this test are not published.
- Calculation: Hawkin's definition, paraphrased: Sum of the time in the air of every jump in the multi rebound ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ FT_j` over all jumps ([hawkinR dictionary]). Terms: `FT` is flight time, in s.
- Inputs: Each jump's flight time and contact time, and the force trace.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Integration drift. Hawkin uses flight time for the multi rebound because integration drifts over long trials ([Hawkin blog, flight time]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Hawkin blog, flight time].

[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, take-off velocity]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin help, multi rebound setup]: https://learning.hawkindynamics.com/knowledge/multi-rebound-test-setup-guide
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
