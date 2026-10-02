# Hawkin Dynamics metrics: weigh-in

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

This page is one part of [the Hawkin Dynamics metrics index](hawkin-dynamics.md). It holds 4 metric blocks for the weigh-in. The index explains how to read each block, lists the sources with access dates, and holds the name collisions, conflicts, and the worked example. Checked against the same sources, on 2026-10-02.

## Metric blocks

### Weigh-in

The weigh-in measures body weight with the athlete standing still ([Hawkin metric database]).

This section has 4 metric blocks. They follow the order of the movement.

#### `Standard Deviation` (N)

This metric has these fields:

- Names: API column `Standard Deviation(N)`, metric ID `standardDeviation`, `hawkinR` column `standard_deviation_n`, `hdforce` column `standard_deviation_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: How much force varied during the weigh-in. Large values mean the athlete moved.
- Phase or window: The weigh-in period. You set its duration in test settings. Hawkin suggests at least 5 s ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Standard deviation of force during the weighing period. Hawkin says it can show whether the subject moved too much ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `SD(F(t))` over the weighing period ([hawkinR dictionary]). Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the weigh-in.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `Weight` (kgs)

This metric has these fields:

- Names: API column `Weight(kgs)`, metric ID `weightKgs`, `hawkinR` column `weight_kgs`, `hdforce` column `weight_kgs` ([hawkinR dictionary], [hdforce source]).
- What it measures: Body mass in kilograms.
- Phase or window: The weigh-in period. You set its duration in test settings. Hawkin suggests at least 5 s ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Weight in kilograms ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Weight in N divided by gravitational acceleration. The value Hawkin uses is not published.
- Inputs: Combined force during the weigh-in.
- Units: kgs ([hawkinR dictionary]).
- Variants: `Weight`.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `Weight` (lbs)

This metric has these fields:

- Names: API column `Weight(lbs)`, metric ID `weightLbs`, `hawkinR` column `weight_lbs`, `hdforce` column `weight_lbs` ([hawkinR dictionary], [hdforce source]).
- What it measures: Body weight in pounds.
- Phase or window: The weigh-in period. You set its duration in test settings. Hawkin suggests at least 5 s ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Weight in pounds ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): Hawkin does not publish how it converts to pounds.
- Inputs: Combined force during the weigh-in.
- Units: lbs ([hawkinR dictionary]).
- Variants: `Weight`.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

#### `Weight in Newtons` (N)

This metric has these fields:

- Names: API column `Weight in Newtons(N)`, metric ID `weight`, `hawkinR` column `weight_in_newtons_n`, `hdforce` column `weight_in_newtons_n` ([hawkinR dictionary], [hdforce source]).
- What it measures: Body weight as a force.
- Phase or window: The weigh-in period. You set its duration in test settings. Hawkin suggests at least 5 s ([Hawkin metric database]).
- Calculation: Hawkin's definition, paraphrased: Weight in newtons ([hawkinR dictionary], [hdforce dictionary]). Formula, restated (not Hawkin's text): `mean F(t)` over the weigh-in. The averaging rule is not published. Terms: `F(t)` is combined vertical force from both plates at each 1 ms sample, in N.
- Inputs: Combined force during the weigh-in.
- Units: N ([hawkinR dictionary]).
- Variants: None in this test.
- What changes the number: Stillness. Movement during the still period changes the average and the standard deviation ([Hawkin blog, two key factors], [Hawkin blog, IMTP basics]).
- Sources: [hawkinR dictionary], [hdforce source], [Hawkin metric database], [hdforce dictionary], [Hawkin blog, two key factors], [Hawkin blog, IMTP basics].

[Hawkin blog, IMTP basics]: https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
