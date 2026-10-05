# Hawkin Dynamics metrics: isometric test

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](README.md). It holds 62 metric blocks for the isometric test. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Isometric test

The athlete pulls or pushes against a fixed bar, for example in the isometric mid-thigh pull ([Hawkin help, IMTP setup]). Time bands are measured from the start of the pull. Hawkin does not show phase landmarks for this test ([Merrigan 2022]).

This section has 62 metric blocks. They follow the order of the movement.

#### `Initiation Threshold` (N)

This metric has these fields:

- Names: API column `Initiation Threshold(N)`, metric ID `initiationThreshold`, `hawkinR` column `initiation_threshold_n`, `hdforce` column `initiation_threshold_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: How much force varied during the quiet period before the pull. Lower means a stiller start.
- Phase or window: Quiet period before the pull ([hawkinR dictionary]). It includes any pretension on the bar ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Three standard deviations of the force during the quiet period. Hawkin says it can show test quality. A lower value means less movement in the quiet period ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `3 × SD(F(t))` over the quiet period, in N. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the quiet period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `System Weight` (N)

This metric has these fields:

- Names: API column `System Weight(N)`, metric ID `systemWeight`, `hawkinR` column `system_weight_n`, `hdforce` column `system_weight_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The athlete's weight plus anything they carry, measured while they stand still before the test.
- Phase or window: Quiet period before the pull ([hawkinR dictionary]). It includes any pretension on the bar ([Merrigan 2022]).
- Calculation: Hawkin's definition, paraphrased: Lowest 1 s average of vertical force on the system center of mass in the weighing phase. An optimization loop finds it ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SW = min over 1 s windows of mean F(t)`, inside the weighing phase. Hawkin's optimization loop is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the still period.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]). External load. System weight includes anything the athlete holds or wears ([Hawkin blog, CMJ phases]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases].

#### `RFD 0-100 ms` (N/s)

This metric has these fields:

- Names: API column `RFD 0-100 ms(N/s)`, metric ID `rfd100`, `hawkinR` column `rfd_0_100_ms_n_s`, `hdforce` column `rfd_0_100_ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises over the first 100 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 100 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force from 0 to 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_0 + 100 ms) − F(t_0)) / 0.1 s`, the average slope ([hawkinR dictionary]). Hawkin does not publish whether it uses end-point forces or a fitted slope. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RFD - 100ms` (N/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `RFD 0-150 ms` (N/s)

This metric has these fields:

- Names: API column `RFD 0-150 ms(N/s)`, metric ID `rfd150`, `hawkinR` column `rfd_0_150_ms_n_s`, `hdforce` column `rfd_0_150_ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises over the first 150 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 150 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force from 0 to 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_0 + 150 ms) − F(t_0)) / 0.15 s`, the average slope ([hawkinR dictionary]). Hawkin does not publish whether it uses end-point forces or a fitted slope. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RFD - 150ms` (N/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `RFD 0-200 ms` (N/s)

This metric has these fields:

- Names: API column `RFD 0-200 ms(N/s)`, metric ID `rfd200`, `hawkinR` column `rfd_0_200_ms_n_s`, `hdforce` column `rfd_0_200_ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises over the first 200 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 200 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force from 0 to 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_0 + 200 ms) − F(t_0)) / 0.2 s`, the average slope ([hawkinR dictionary]). Hawkin does not publish whether it uses end-point forces or a fitted slope. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `RFD 0-250 ms` (N/s)

This metric has these fields:

- Names: API column `RFD 0-250 ms(N/s)`, metric ID `rfd250`, `hawkinR` column `rfd_0_250_ms_n_s`, `hdforce` column `rfd_0_250_ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises over the first 250 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 250 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force from 0 to 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_0 + 250 ms) − F(t_0)) / 0.25 s`, the average slope ([hawkinR dictionary]). Hawkin does not publish whether it uses end-point forces or a fitted slope. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RFD - 250ms` (N/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `RFD 0-50 ms` (N/s)

This metric has these fields:

- Names: API column `RFD 0-50 ms(N/s)`, metric ID `rfd50`, `hawkinR` column `rfd_0_50_ms_n_s`, `hdforce` column `rfd_0_50_ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How fast force rises over the first 50 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 50 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Mean slope of the vertical force from 0 to 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `(F(t_0 + 50 ms) − F(t_0)) / 0.05 s`, the average slope ([hawkinR dictionary]). Hawkin does not publish whether it uses end-point forces or a fitted slope. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `RFD - 50ms` (N/s), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Filtering. Merrigan et al. (2022) report a default 50 Hz low-pass filter on Hawkin plates. Rate of force development values depend on filtering and on the method ([Merrigan 2022]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Time to Peak Force` (s)

This metric has these fields:

- Names: API column `Time to Peak Force(s)`, metric ID `timeToPeak`, `hawkinR` column `time_to_peak_force_s`, `hdforce` column `time_to_peak_force_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Time from the start of the pull to peak force.
- Phase or window: From the start of the pull to the instant of peak force ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time from the start of the pull to the peak vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t* − t_0` ([hawkinR dictionary]). Terms: `t*` is the instant of peak combined force in the window; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- Comparison with VALD ForceDecks: `Start Time to Peak Force` (s) ([Merrigan 2022]). VALD starts the pull "when exercise commences", per Merrigan et al.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, IMTP basics].

#### `Length of Pull` (s)

This metric has these fields:

- Names: API column `Length of Pull(s)`, metric ID `lengthOfPull`, `hawkinR` column `length_of_pull_s`, `hdforce` column `length_of_pull_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the pull lasts.
- Phase or window: From the start of the pull to the return of force to the system weight baseline ([hawkinR dictionary]).
- Calculation: Hawkin's definition, paraphrased: Time from the start of the pull until system weight returns to baseline ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_end − t_0`, where `t_end` is when force returns to system weight ([hawkinR dictionary]). Terms: `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [hdforce dictionary], [Merrigan 2022], [Hawkin blog, IMTP basics].

#### `Force at 0 ms` (N)

This metric has these fields:

- Names: API column `Force at 0 ms(N)`, metric ID `forceAt0`, `hawkinR` column `force_at_0_ms_n`, `hdforce` column `force_at_0_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 0 ms after the start of the pull.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at the start of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 0 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 0 ms`, `Net Force at 0 ms`, `Right Force at 0 ms`, `Relative Force at 0 ms`, `Relative Force at 0 ms (BW)`.
- Comparison with VALD ForceDecks: `Baseline Force` (N) ([Merrigan 2022]).
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 0 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 0 ms(N)`, metric ID `netForceAt0`, `hawkinR` column `net_force_at_0_ms_n`, `hdforce` column `net_force_at_0_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 0 ms after the start of the pull.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at the start of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 0 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 0 ms`, `Left Force at 0 ms`, `Right Force at 0 ms`, `Relative Force at 0 ms`, `Relative Force at 0 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 0 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 0 ms(%)`, metric ID `relativeForceAt0`, `hawkinR` column `relative_force_at_0_ms_percent`, `hdforce` column `relative_force_at_0_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 0 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at the start of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 0 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 0 ms`, `Left Force at 0 ms`, `Net Force at 0 ms`, `Right Force at 0 ms`, `Relative Force at 0 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 0 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 0 ms (BW)(N/kg)`, metric ID `relativeForceAt0Bw`, `hawkinR` column `relative_force_at_0_ms_bw_n_kg`, `hdforce` column `relative_force_at_0_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 0 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at the start of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 0 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]).
- Variants: `Force at 0 ms`, `Left Force at 0 ms`, `Net Force at 0 ms`, `Right Force at 0 ms`, `Relative Force at 0 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Left Force at 0 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 0 ms(N)`, metric ID `lForceAt0`, `hawkinR` column `left_force_at_0_ms_n`, `hdforce` column `left_force_at_0_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 0 ms after the start of the pull.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at the start of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 0 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 0 ms`, `Net Force at 0 ms`, `Right Force at 0 ms`, `Relative Force at 0 ms`, `Relative Force at 0 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 0 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 0 ms(N)`, metric ID `rForceAt0`, `hawkinR` column `right_force_at_0_ms_n`, `hdforce` column `right_force_at_0_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 0 ms after the start of the pull.
- Phase or window: The start of the pull (0 ms). Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at the start of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 0 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 0 ms`, `Left Force at 0 ms`, `Net Force at 0 ms`, `Relative Force at 0 ms`, `Relative Force at 0 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Force at 100 ms` (N)

This metric has these fields:

- Names: API column `Force at 100 ms(N)`, metric ID `forceAt100`, `hawkinR` column `force_at_100_ms_n`, `hdforce` column `force_at_100_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 100 ms after the start of the pull.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 100 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 100 ms`, `Net Force at 100 ms`, `Right Force at 100 ms`, `Relative Force at 100 ms`, `Relative Force at 100 ms (BW)`.
- Comparison with VALD ForceDecks: `Force at 100ms` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 100 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 100 ms(N)`, metric ID `netForceAt100`, `hawkinR` column `net_force_at_100_ms_n`, `hdforce` column `net_force_at_100_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 100 ms after the start of the pull.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 100 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 100 ms`, `Left Force at 100 ms`, `Right Force at 100 ms`, `Relative Force at 100 ms`, `Relative Force at 100 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 100 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 100 ms(%)`, metric ID `relativeForceAt100`, `hawkinR` column `relative_force_at_100_ms_percent`, `hdforce` column `relative_force_at_100_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 100 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 100 ms of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 100 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 100 ms`, `Left Force at 100 ms`, `Net Force at 100 ms`, `Right Force at 100 ms`, `Relative Force at 100 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 100 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 100 ms (BW)(N/kg)`, metric ID `relativeForceAt100Bw`, `hawkinR` column `relative_force_at_100_ms_bw_n_kg`, `hdforce` column `relative_force_at_100_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 100 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 100 ms of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 100 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Force at 100 ms`, `Left Force at 100 ms`, `Net Force at 100 ms`, `Right Force at 100 ms`, `Relative Force at 100 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Left Force at 100 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 100 ms(N)`, metric ID `lForceAt100`, `hawkinR` column `left_force_at_100_ms_n`, `hdforce` column `left_force_at_100_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 100 ms after the start of the pull.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 100 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 100 ms`, `Net Force at 100 ms`, `Right Force at 100 ms`, `Relative Force at 100 ms`, `Relative Force at 100 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 100 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 100 ms(N)`, metric ID `rForceAt100`, `hawkinR` column `right_force_at_100_ms_n`, `hdforce` column `right_force_at_100_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 100 ms after the start of the pull.
- Phase or window: The instant 100 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 100 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 100 ms`, `Left Force at 100 ms`, `Net Force at 100 ms`, `Relative Force at 100 ms`, `Relative Force at 100 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Force at 150 ms` (N)

This metric has these fields:

- Names: API column `Force at 150 ms(N)`, metric ID `forceAt150`, `hawkinR` column `force_at_150_ms_n`, `hdforce` column `force_at_150_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 150 ms after the start of the pull.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 150 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 150 ms`, `Net Force at 150 ms`, `Right Force at 150 ms`, `Relative Force at 150 ms`, `Relative Force at 150 ms (BW)`.
- Comparison with VALD ForceDecks: `Force at 150ms` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 150 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 150 ms(N)`, metric ID `netForceAt150`, `hawkinR` column `net_force_at_150_ms_n`, `hdforce` column `net_force_at_150_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 150 ms after the start of the pull.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 150 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 150 ms`, `Left Force at 150 ms`, `Right Force at 150 ms`, `Relative Force at 150 ms`, `Relative Force at 150 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 150 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 150 ms(%)`, metric ID `relativeForceAt150`, `hawkinR` column `relative_force_at_150_ms_percent`, `hdforce` column `relative_force_at_150_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 150 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 150 ms of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 150 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 150 ms`, `Left Force at 150 ms`, `Net Force at 150 ms`, `Right Force at 150 ms`, `Relative Force at 150 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 150 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 150 ms (BW)(N/kg)`, metric ID `relativeForceAt150Bw`, `hawkinR` column `relative_force_at_150_ms_bw_n_kg`, `hdforce` column `relative_force_at_150_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 150 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 150 ms of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 150 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Force at 150 ms`, `Left Force at 150 ms`, `Net Force at 150 ms`, `Right Force at 150 ms`, `Relative Force at 150 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Left Force at 150 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 150 ms(N)`, metric ID `lForceAt150`, `hawkinR` column `left_force_at_150_ms_n`, `hdforce` column `left_force_at_150_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 150 ms after the start of the pull.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 150 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 150 ms`, `Net Force at 150 ms`, `Right Force at 150 ms`, `Relative Force at 150 ms`, `Relative Force at 150 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 150 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 150 ms(N)`, metric ID `rForceAt150`, `hawkinR` column `right_force_at_150_ms_n`, `hdforce` column `right_force_at_150_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 150 ms after the start of the pull.
- Phase or window: The instant 150 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 150 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 150 ms`, `Left Force at 150 ms`, `Net Force at 150 ms`, `Relative Force at 150 ms`, `Relative Force at 150 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Force at 200 ms` (N)

This metric has these fields:

- Names: API column `Force at 200 ms(N)`, metric ID `forceAt200`, `hawkinR` column `force_at_200_ms_n`, `hdforce` column `force_at_200_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 200 ms after the start of the pull.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 200 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 200 ms`, `Net Force at 200 ms`, `Right Force at 200 ms`, `Relative Force at 200 ms`, `Relative Force at 200 ms (BW)`.
- Comparison with VALD ForceDecks: `Force at 200ms` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 200 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 200 ms(N)`, metric ID `netForceAt200`, `hawkinR` column `net_force_at_200_ms_n`, `hdforce` column `net_force_at_200_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 200 ms after the start of the pull.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 200 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 200 ms`, `Left Force at 200 ms`, `Right Force at 200 ms`, `Relative Force at 200 ms`, `Relative Force at 200 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 200 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 200 ms(%)`, metric ID `relativeForceAt200`, `hawkinR` column `relative_force_at_200_ms_percent`, `hdforce` column `relative_force_at_200_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 200 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 200 ms of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 200 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 200 ms`, `Left Force at 200 ms`, `Net Force at 200 ms`, `Right Force at 200 ms`, `Relative Force at 200 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 200 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 200 ms (BW)(N/kg)`, metric ID `relativeForceAt200Bw`, `hawkinR` column `relative_force_at_200_ms_bw_n_kg`, `hdforce` column `relative_force_at_200_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 200 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 200 ms of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 200 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Force at 200 ms`, `Left Force at 200 ms`, `Net Force at 200 ms`, `Right Force at 200 ms`, `Relative Force at 200 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Left Force at 200 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 200 ms(N)`, metric ID `lForceAt200`, `hawkinR` column `left_force_at_200_ms_n`, `hdforce` column `left_force_at_200_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 200 ms after the start of the pull.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 200 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 200 ms`, `Net Force at 200 ms`, `Right Force at 200 ms`, `Relative Force at 200 ms`, `Relative Force at 200 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 200 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 200 ms(N)`, metric ID `rForceAt200`, `hawkinR` column `right_force_at_200_ms_n`, `hdforce` column `right_force_at_200_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 200 ms after the start of the pull.
- Phase or window: The instant 200 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 200 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 200 ms`, `Left Force at 200 ms`, `Net Force at 200 ms`, `Relative Force at 200 ms`, `Relative Force at 200 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Force at 250 ms` (N)

This metric has these fields:

- Names: API column `Force at 250 ms(N)`, metric ID `forceAt250`, `hawkinR` column `force_at_250_ms_n`, `hdforce` column `force_at_250_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 250 ms after the start of the pull.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 250 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 250 ms`, `Net Force at 250 ms`, `Right Force at 250 ms`, `Relative Force at 250 ms`, `Relative Force at 250 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 250 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 250 ms(N)`, metric ID `netForceAt250`, `hawkinR` column `net_force_at_250_ms_n`, `hdforce` column `net_force_at_250_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 250 ms after the start of the pull.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 250 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 250 ms`, `Left Force at 250 ms`, `Right Force at 250 ms`, `Relative Force at 250 ms`, `Relative Force at 250 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 250 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 250 ms(%)`, metric ID `relativeForceAt250`, `hawkinR` column `relative_force_at_250_ms_percent`, `hdforce` column `relative_force_at_250_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 250 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 250 ms of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 250 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 250 ms`, `Left Force at 250 ms`, `Net Force at 250 ms`, `Right Force at 250 ms`, `Relative Force at 250 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 250 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 250 ms (BW)(N/kg)`, metric ID `relativeForceAt250Bw`, `hawkinR` column `relative_force_at_250_ms_bw_n_kg`, `hdforce` column `relative_force_at_250_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 250 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 250 ms of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 250 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Force at 250 ms`, `Left Force at 250 ms`, `Net Force at 250 ms`, `Right Force at 250 ms`, `Relative Force at 250 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Left Force at 250 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 250 ms(N)`, metric ID `lForceAt250`, `hawkinR` column `left_force_at_250_ms_n`, `hdforce` column `left_force_at_250_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 250 ms after the start of the pull.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 250 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 250 ms`, `Net Force at 250 ms`, `Right Force at 250 ms`, `Relative Force at 250 ms`, `Relative Force at 250 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 250 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 250 ms(N)`, metric ID `rForceAt250`, `hawkinR` column `right_force_at_250_ms_n`, `hdforce` column `right_force_at_250_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 250 ms after the start of the pull.
- Phase or window: The instant 250 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 250 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 250 ms`, `Left Force at 250 ms`, `Net Force at 250 ms`, `Relative Force at 250 ms`, `Relative Force at 250 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Force at 50 ms` (N)

This metric has these fields:

- Names: API column `Force at 50 ms(N)`, metric ID `forceAt50`, `hawkinR` column `force_at_50_ms_n`, `hdforce` column `force_at_50_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force 50 ms after the start of the pull.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 50 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Force at 50 ms`, `Net Force at 50 ms`, `Right Force at 50 ms`, `Relative Force at 50 ms`, `Relative Force at 50 ms (BW)`.
- Comparison with VALD ForceDecks: `Force at 50ms` (N), paired by Merrigan et al. (2022) ([Merrigan 2022]). The start-of-pull rules differ, which shifts every time band.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Force at 50 ms` (N)

This metric has these fields:

- Names: API column `Net Force at 50 ms(N)`, metric ID `netForceAt50`, `hawkinR` column `net_force_at_50_ms_n`, `hdforce` column `net_force_at_50_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight 50 ms after the start of the pull.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force at 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 50 ms) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 50 ms`, `Left Force at 50 ms`, `Right Force at 50 ms`, `Relative Force at 50 ms`, `Relative Force at 50 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors].

#### `Relative Force at 50 ms` (%)

This metric has these fields:

- Names: API column `Relative Force at 50 ms(%)`, metric ID `relativeForceAt50`, `hawkinR` column `relative_force_at_50_ms_percent`, `hdforce` column `relative_force_at_50_ms` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 50 ms after the start of the pull, as a percentage of system weight.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 50 ms of the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × F(t_0 + 50 ms) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: % ([hawkinR dictionary]).
- Variants: `Force at 50 ms`, `Left Force at 50 ms`, `Net Force at 50 ms`, `Right Force at 50 ms`, `Relative Force at 50 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Relative Force at 50 ms (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Force at 50 ms (BW)(N/kg)`, metric ID `relativeForceAt50Bw`, `hawkinR` column `relative_force_at_50_ms_bw_n_kg`, `hdforce` column `relative_force_at_50_ms_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force 50 ms after the start of the pull, relative to the last known body weight.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force at 50 ms of the isometric test, expressed as a percent of last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F(t_0 + 50 ms) / m_last`, in N/kg per the dictionary unit. The dictionary text says a percentage of last known bodyweight, so the unit and the text disagree ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `t_0` is the start of the pull (0 ms); `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined force, the athlete's stored body weight, and the start of the pull.
- Units: N/kg ([hawkinR dictionary]). The metric database web page lists `%` ([Hawkin metric database]), which disagrees.
- Variants: `Force at 50 ms`, `Left Force at 50 ms`, `Net Force at 50 ms`, `Right Force at 50 ms`, `Relative Force at 50 ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Left Force at 50 ms` (N)

This metric has these fields:

- Names: API column `Left Force at 50 ms(N)`, metric ID `lForceAt50`, `hawkinR` column `left_force_at_50_ms_n`, `hdforce` column `left_force_at_50_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the left plate 50 ms after the start of the pull.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force at 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_L(t_0 + 50 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_L(t)` is left plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Left plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 50 ms`, `Net Force at 50 ms`, `Right Force at 50 ms`, `Relative Force at 50 ms`, `Relative Force at 50 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Force at 50 ms` (N)

This metric has these fields:

- Names: API column `Right Force at 50 ms(N)`, metric ID `rForceAt50`, `hawkinR` column `right_force_at_50_ms_n`, `hdforce` column `right_force_at_50_ms_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force on the right plate 50 ms after the start of the pull.
- Phase or window: The instant 50 ms after the start of the pull. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force at 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `F_R(t_0 + 50 ms)`. Hawkin's text says peak instantaneous force at that time ([hawkinR dictionary]). Terms: `F_R(t)` is right plate vertical force, in N; `t_0` is the start of the pull (0 ms).
- Inputs: Right plate force and the start of the pull.
- Units: N ([hawkinR dictionary]).
- Variants: `Force at 50 ms`, `Left Force at 50 ms`, `Net Force at 50 ms`, `Relative Force at 50 ms`, `Relative Force at 50 ms (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Impulse 0-100ms` (N.s)

This metric has these fields:

- Names: API column `Impulse 0-100ms(N.s)`, metric ID `impulse100`, `hawkinR` column `impulse_0_100ms_n_s`, `hdforce` column `impulse_0_100ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force added up over the first 100 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 100 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse from 0 to 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_0` to `t_0 + 100 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Net Impulse 0-100ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Impulse 0-100ms` (N.s)

This metric has these fields:

- Names: API column `Net Impulse 0-100ms(N.s)`, metric ID `netImpulse100`, `hawkinR` column `net_impulse_0_100ms_n_s`, `hdforce` column `net_impulse_0_100ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the first 100 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 100 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse from 0 to 100 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` from `t_0` to `t_0 + 100 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Impulse 0-100ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Impulse 0-150ms` (N.s)

This metric has these fields:

- Names: API column `Impulse 0-150ms(N.s)`, metric ID `impulse150`, `hawkinR` column `impulse_0_150ms_n_s`, `hdforce` column `impulse_0_150ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force added up over the first 150 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 150 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse from 0 to 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_0` to `t_0 + 150 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Net Impulse 0-150ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Impulse 0-150ms` (N.s)

This metric has these fields:

- Names: API column `Net Impulse 0-150ms(N.s)`, metric ID `netImpulse150`, `hawkinR` column `net_impulse_0_150ms_n_s`, `hdforce` column `net_impulse_0_150ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the first 150 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 150 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse from 0 to 150 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` from `t_0` to `t_0 + 150 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N.s ([hawkinR dictionary]). The metric database web page lists `Newton second (N/s)` ([Hawkin metric database]), which disagrees.
- Variants: `Impulse 0-150ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin metric database], [Hawkin blog, IMTP basics].

#### `Impulse 0-200ms` (N.s)

This metric has these fields:

- Names: API column `Impulse 0-200ms(N.s)`, metric ID `impulse200`, `hawkinR` column `impulse_0_200ms_n_s`, `hdforce` column `impulse_0_200ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force added up over the first 200 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 200 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse from 0 to 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_0` to `t_0 + 200 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Net Impulse 0-200ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Impulse 0-200ms` (N.s)

This metric has these fields:

- Names: API column `Net Impulse 0-200ms(N.s)`, metric ID `netImpulse200`, `hawkinR` column `net_impulse_0_200ms_n_s`, `hdforce` column `net_impulse_0_200ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the first 200 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 200 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse from 0 to 200 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` from `t_0` to `t_0 + 200 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Impulse 0-200ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Impulse 0-250ms` (N.s)

This metric has these fields:

- Names: API column `Impulse 0-250ms(N.s)`, metric ID `impulse250`, `hawkinR` column `impulse_0_250ms_n_s`, `hdforce` column `impulse_0_250ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force added up over the first 250 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 250 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse from 0 to 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_0` to `t_0 + 250 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Net Impulse 0-250ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Impulse 0-250ms` (N.s)

This metric has these fields:

- Names: API column `Net Impulse 0-250ms(N.s)`, metric ID `netImpulse250`, `hawkinR` column `net_impulse_0_250ms_n_s`, `hdforce` column `net_impulse_0_250ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the first 250 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 250 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse from 0 to 250 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` from `t_0` to `t_0 + 250 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Impulse 0-250ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Impulse 0-50ms` (N.s)

This metric has these fields:

- Names: API column `Impulse 0-50ms(N.s)`, metric ID `impulse50`, `hawkinR` column `impulse_0_50ms_n_s`, `hdforce` column `impulse_0_50ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Total force added up over the first 50 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 50 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Vertical impulse from 0 to 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` from `t_0` to `t_0 + 50 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Net Impulse 0-50ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Impulse 0-50ms` (N.s)

This metric has these fields:

- Names: API column `Net Impulse 0-50ms(N.s)`, metric ID `netImpulse50`, `hawkinR` column `net_impulse_0_50ms_n_s`, `hdforce` column `net_impulse_0_50ms_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force above system weight added up over the first 50 ms of the pull.
- Phase or window: From the start of the pull (0 ms) to 50 ms after it. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Net vertical impulse from 0 to 50 ms of the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ (F(t) − SW) × Δt` from `t_0` to `t_0 + 50 ms`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz; `t_0` is the start of the pull (0 ms).
- Inputs: Combined force, system weight, and the start of the pull.
- Units: N.s ([hawkinR dictionary]).
- Variants: `Impulse 0-50ms`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Net Peak Force` (N)

This metric has these fields:

- Names: API column `Net Peak Force(N)`, metric ID `netPeakForce`, `hawkinR` column `net_peak_force_n`, `hdforce` column `net_peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force above system weight during the pull.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous net vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t) − SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined or plate force and system weight.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `L|R Peak Force`, `Peak Force`, `Right Peak Force`, `Relative Peak Force`, `Relative Peak Force (BW)`.
- What changes the number: System weight. Velocity, displacement, power, net values, and the phase boundaries all depend on it, so the athlete must stand still while it is measured ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors]). Pretension. Taking slack out of the bar before the quiet period adds to system weight ([Merrigan 2022], [Hawkin help, IMTP setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Hawkin help, IMTP setup].

#### `Peak Force` (N)

This metric has these fields:

- Names: API column `Peak Force(N)`, metric ID `peakForce`, `hawkinR` column `peak_force_n`, `hdforce` column `peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest total force during the pull, including body weight.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` ([hawkinR dictionary]). This is gross force; `Net Peak Force` removes system weight. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined or plate force and system weight.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `L|R Peak Force`, `Net Peak Force`, `Right Peak Force`, `Relative Peak Force`, `Relative Peak Force (BW)`.
- Comparison with VALD ForceDecks: `Peak Vertical Force` (N), paired by Merrigan et al. (2022), who found the two within 1 N ([Merrigan 2022]). VALD does not publish whether it includes body weight; Hawkin's is gross.
- What changes the number: Gross or net. This value includes body weight ([hawkinR dictionary]). Compare it only with other gross values.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary].

#### `Relative Peak Force` (%)

This metric has these fields:

- Names: API column `Relative Peak Force(%)`, metric ID `relativePeakForce`, `hawkinR` column `relative_peak_force_percent`, `hdforce` column `relative_peak_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force during the pull, as a percentage of system weight.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force in the isometric test, expressed as a percent of system weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `100 × max F(t) / SW`. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `SW` is `System Weight`, in N.
- Inputs: Combined or plate force and system weight.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `L|R Peak Force`, `Net Peak Force`, `Peak Force`, `Right Peak Force`, `Relative Peak Force (BW)`.
- What changes the number: The denominator. Relative values divide by system weight from the same trial, so a change in system weight changes the percentage even when force does not change. Pretension. Taking slack out of the bar before the quiet period adds to system weight ([Merrigan 2022], [Hawkin help, IMTP setup]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin help, IMTP setup].

#### `Relative Peak Force (BW)` (N/kg)

This metric has these fields:

- Names: API column `Relative Peak Force (BW)(N/kg)`, metric ID `relativePeakForceBw`, `hawkinR` column `relative_peak_force_bw_n_kg`, `hdforce` column `relative_peak_force_bw_n_kg` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force during the pull, relative to the last known body weight.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous vertical force in the isometric test, relative to last known body weight ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t) / m_last`, in N/kg per the dictionary unit ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `m_last` is the last known body mass stored for the athlete, in kg.
- Inputs: Combined or plate force and system weight.
- Units: N/kg ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `L|R Peak Force`, `Net Peak Force`, `Peak Force`, `Right Peak Force`, `Relative Peak Force`.
- What changes the number: Stored body weight. The (BW) variants use the athlete's last known body weight, not this trial's system weight ([hawkinR dictionary]). A stale stored weight changes the value. Hawkin recommends a CMJ before the isometric test so the weight fills in ([Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics].

#### `Left Peak Force` (N)

This metric has these fields:

- Names: API column `Left Peak Force(N)`, metric ID `lPeakForce`, `hawkinR` column `left_peak_force_n`, `hdforce` column `left_peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force on the left plate during the pull.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous left vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F_L(t)` ([hawkinR dictionary]). This is the plate's own peak, not its share at the combined peak. Terms: `F_L(t)` is left plate vertical force, in N.
- Inputs: Combined or plate force and system weight.
- Units: N ([hawkinR dictionary]).
- Variants: `L|R Peak Force`, `Net Peak Force`, `Peak Force`, `Right Peak Force`, `Relative Peak Force`, `Relative Peak Force (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `Right Peak Force` (N)

This metric has these fields:

- Names: API column `Right Peak Force(N)`, metric ID `rPeakForce`, `hawkinR` column `right_peak_force_n`, `hdforce` column `right_peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force on the right plate during the pull.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous right vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F_R(t)` ([hawkinR dictionary]). This is the plate's own peak, not its share at the combined peak. Terms: `F_R(t)` is right plate vertical force, in N.
- Inputs: Combined or plate force and system weight.
- Units: N ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `L|R Peak Force`, `Net Peak Force`, `Peak Force`, `Relative Peak Force`, `Relative Peak Force (BW)`.
- What changes the number: Start of the pull. Pretension or a dip before the pull moves the 0 ms point, which shifts every time-band value. Merrigan et al. (2022) found force at 0 ms the value most affected ([Merrigan 2022], [Hawkin blog, IMTP basics]). Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]).
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, IMTP basics], [Hawkin help, left and right plate].

#### `L|R Peak Force` (%)

This metric has these fields:

- Names: API column `L|R Peak Force(%)`, metric ID `lrPeakForce`, `hawkinR` column `l_r_peak_force_percent`, `hdforce` column `lr_peak_force` ([hawkinR dictionary], [hdforce source]).
- What it measures: The difference between the left and right plates for peak force, as a percentage.
- Phase or window: The whole pull, from the start of the pull to the end of the recording. The end point is not published. Merrigan et al. (2022) report that Hawkin finds the start when force rises 5 standard deviations above body weight, then traces back to within 0 to 2 N of body weight ([Merrigan 2022]). The API dictionary defines `Initiation Threshold` as 3 standard deviations of the quiet period, a check on stillness ([hawkinR dictionary]). It does not say whether this value sets the start.
- Calculation: Hawkin's definition, paraphrased: Difference between the left and right vertical forces at the moment of peak vertical force in the isometric test ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Asymmetry of `F_L(t*)` and `F_R(t*)`, the plate forces at the instant of peak combined force. Hawkin does not publish the asymmetry formula. The asymmetry report shows left-dominant values as positive and right-dominant values as negative ([Hawkin blog, asymmetry report]). Terms: `F_L(t)` is left plate vertical force, in N; `F_R(t)` is right plate vertical force, in N; `t*` is the instant of peak combined force in the window.
- Inputs: Left and right plate force traces and the window events.
- Units: % ([hawkinR dictionary]).
- Variants: `Left Peak Force`, `Net Peak Force`, `Peak Force`, `Right Peak Force`, `Relative Peak Force`, `Relative Peak Force (BW)`.
- Comparison with VALD ForceDecks: VALD reports asymmetry as (Left − Right) ÷ max(Left, Right) × 100 ([VALD glossary]). Hawkin does not publish its formula ([Hawkin blog, asymmetry report]), so the two may not match even with identical plate forces.
- What changes the number: Foot placement. The left foot goes on the left plate and the right foot on the right plate, which has the power and zero button. Swapped feet invert left, right, and asymmetry values ([Hawkin help, left and right plate]). Asymmetry formula. Hawkin does not publish it ([Hawkin blog, asymmetry report]). Recompute asymmetry from the left and right values with one stated formula before you compare devices.
- Sources: [hawkinR dictionary], [hdforce source], [Merrigan 2022], [hdforce dictionary], [Hawkin blog, asymmetry report], [VALD glossary], [Hawkin help, left and right plate].

[Hawkin blog, asymmetry report]: https://www.hawkindynamics.com/blog/asymmetry-report
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, IMTP setup]: https://learning.hawkindynamics.com/knowledge/isometric-mid-thigh-pull-setup-guide
[Hawkin help, left and right plate]: https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
