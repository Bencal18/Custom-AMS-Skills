# Hawkin Dynamics metrics: TruStrength tests

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 14 metric blocks for the TruStrength tests. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### TruStrength isometric test

TruStrength is a dynamometer, not a force plate. Its tests come through the same API. Each repetition starts and ends at the pretension threshold ([Hawkin help, pretension]).

This section has 7 metric blocks. They follow the order of the movement.

#### `Pretension` (N)

This metric has these fields:

- Names: API column `Pretension(N)`, metric ID `pretension`, `hawkinR` column `pretension_n`, `hdforce` column `pretension_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The baseline force that starts and ends each repetition.
- Phase or window: Set before the repetitions start ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Force level that marks when a repetition begins and ends ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Set automatically or by hand before the test ([Hawkin help, pretension]).
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Target` (N)

This metric has these fields:

- Names: API column `Target(N)`, metric ID `target`, `hawkinR` column `target_n`, `hdforce` column `target_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The force target set for the repetition.
- Phase or window: Set before the repetitions start ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Target force for the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Set by the user ([hawkinR dictionary]). How it is set is not published.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Avg. Force` (N)

This metric has these fields:

- Names: API column `Avg. Force(N)`, metric ID `avgForce`, `hawkinR` column `avg_force_n`, `hdforce` column `avg_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Mean force during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Duration` (s)

This metric has these fields:

- Names: API column `Duration(s)`, metric ID `duration`, `hawkinR` column `duration_s`, `hdforce` column `duration_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the repetition lasts.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Time from the start to the end of the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_end − t_start` of the repetition ([hawkinR dictionary]).
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Peak Force` (N)

This metric has these fields:

- Names: API column `Peak Force(N)`, metric ID `peakForce`, `hawkinR` column `peak_force_n`, `hdforce` column `peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous force during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Peak RFD` (N/s)

This metric has these fields:

- Names: API column `Peak RFD(N/s)`, metric ID `peakRFD`, `hawkinR` column `peak_rfd_n_s`, `hdforce` column `peak_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The fastest instant rise in force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous rate of force development during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max dF/dt` ([hawkinR dictionary]). The differentiation window is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Total Impulse` (N.s)

This metric has these fields:

- Names: API column `Total Impulse(N.s)`, metric ID `impulse`, `hawkinR` column `total_impulse_n_s`, `hdforce` column `total_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force added up over the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Total impulse (area under the force-time curve) during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the repetition ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N.s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

### TruStrength free run

TruStrength free run records repetitions on the dynamometer. The API returns the same seven metrics as the TruStrength isometric test ([hawkinR dictionary]).

This section has 7 metric blocks. They follow the order of the movement.

#### `Pretension` (N)

This metric has these fields:

- Names: API column `Pretension(N)`, metric ID `pretension`, `hawkinR` column `pretension_n`, `hdforce` column `pretension_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The baseline force that starts and ends each repetition.
- Phase or window: Set before the repetitions start ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Force level that marks when a repetition begins and ends ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Set automatically or by hand before the test ([Hawkin help, pretension]).
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Target` (N)

This metric has these fields:

- Names: API column `Target(N)`, metric ID `target`, `hawkinR` column `target_n`, `hdforce` column `target_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The force target set for the repetition.
- Phase or window: Set before the repetitions start ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Target force for the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Set by the user ([hawkinR dictionary]). How it is set is not published.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Avg. Force` (N)

This metric has these fields:

- Names: API column `Avg. Force(N)`, metric ID `avgForce`, `hawkinR` column `avg_force_n`, `hdforce` column `avg_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The average force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Mean force during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Duration` (s)

This metric has these fields:

- Names: API column `Duration(s)`, metric ID `duration`, `hawkinR` column `duration_s`, `hdforce` column `duration_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: How long the repetition lasts.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Time from the start to the end of the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `t_end − t_start` of the repetition ([hawkinR dictionary]).
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Peak Force` (N)

This metric has these fields:

- Names: API column `Peak Force(N)`, metric ID `peakForce`, `hawkinR` column `peak_force_n`, `hdforce` column `peak_force_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: The highest force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous force during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max F(t)` ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Peak RFD` (N/s)

This metric has these fields:

- Names: API column `Peak RFD(N/s)`, metric ID `peakRFD`, `hawkinR` column `peak_rfd_n_s`, `hdforce` column `peak_rfd_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: The fastest instant rise in force in the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Highest instantaneous rate of force development during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `max dF/dt` ([hawkinR dictionary]). The differentiation window is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N/s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

#### `Total Impulse` (N.s)

This metric has these fields:

- Names: API column `Total Impulse(N.s)`, metric ID `impulse`, `hawkinR` column `total_impulse_n_s`, `hdforce` column `total_impulse_n_s` ([hawkinR dictionary], [hdforce source]).
- What it measures: Force added up over the repetition.
- Phase or window: One repetition. It starts and ends when force crosses the pretension threshold ([hawkinR dictionary], [Hawkin help, pretension]).
- Calculation: Hawkin's definition, paraphrased: Total impulse (area under the force-time curve) during the repetition ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `Σ F(t) × Δt` over the repetition ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N; `Δt` is the sample interval, 0.001 s at 1000 Hz.
- Note: `F(t)` here is the TruStrength load cell force, not force plate force.
- Inputs: TruStrength dynamometer force for one repetition.
- Units: N.s ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Pretension. It sets when each repetition starts and ends ([Hawkin help, pretension]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin help, pretension], [hdforce dictionary].

[Hawkin help, pretension]: https://learning.hawkindynamics.com/knowledge/what-is-pretension
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
