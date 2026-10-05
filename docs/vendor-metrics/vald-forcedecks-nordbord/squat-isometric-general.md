# VALD ForceDecks and NordBord metrics: squat, push-up, sit to stand, balance, isometric, and general tests

This page explains how VALD ForceDecks calculates each metric for these tests. It covers the squat assessment (SQT, SLSQT), push-up tests (PUSHUPT, PPU), Sit to Stand to Sit (STSTS), balance tests (QSB, SLSB, SLROSB), isometric tests (IMTP and others), General Force-Time Analysis (GFTA), and the cross-test ratios (DSI, EUR), with 75 metric blocks. Checked against: the VALD ForceDecks Technical Glossary V2.0 (March 2024), the VALD ForceDecks User Guide v2 (November 2023), the External ForceDecks API specification (`v2019q3`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

This page is part of [VALD ForceDecks and NordBord metrics](README.md). The index explains how to read each block, and it holds the event and term glossary, the factors that change the numbers, the conflicts in VALD's own sources, the Not published list, the worked example, and the sources with access dates. VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](../vald-other-products/README.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](../hawkin-dynamics/README.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](../hawkin-dynamics/README.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Metric blocks

### Squat assessment (SQT, SLSQT)

Bodyweight or loaded squats; select the test type before recording, because auto-detect does not detect squats ([User Guide p.39](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Key moments: start of rep, start of deceleration (peak negative velocity), eccentric peak force, start of concentric (zero velocity), concentric peak force, end of rep (force returns to system weight) ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)).

VALD-stated count: 25 metrics ([User Guide p.43](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

#### `Squat Depth`

This metric has these fields:

- **What it measures:** How far the centre of mass drops in the squat.
- **Window or phase:** Single point: the lowest point of the squat, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The reference starting position is not published.
- **Calculation:** VALD says it is how far the individual travels downward until the lowest point reached in a squat ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `min s(t)` in the rep.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** Added for SQT and SLSQT in a release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). VALD Health also describes it as total downward displacement of the centre of mass ([Squat Assessment: Understanding kinetics and kinematics](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [Squat Assessment: Understanding kinetics and kinematics](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics).

#### `Maximum Negative Displacement`

This metric has these fields:

- **What it measures:** Lowest point the centre of mass reaches.
- **Window or phase:** Single point: the lowest point the centre of mass reaches in the squat, as the definition states ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the lowest position the CoM reaches during the squat ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `min s(t)`.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** Listed for SQT, SLSQT and Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Eccentric Peak Velocity`

This metric has these fields:

- **What it measures:** Fastest downward speed in the squat.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the largest negative velocity seen in the eccentric phase ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `min v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** SLSQT default ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Eccentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average downward speed.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD describes it as the mean velocity going downward across the eccentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `mean v(t)` over the eccentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** SQT default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Concentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average upward speed.
- **Window or phase:** Concentric phase: zero velocity to end of rep ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the mean velocity across the concentric phase ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `mean v(t)` over the concentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** SQT default. VALD Health: average upward speed from maximum squat depth to end of movement ([Squat Assessment: Understanding kinetics and kinematics](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Squat Assessment: Understanding kinetics and kinematics](https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics).

#### `Concentric Peak Velocity`

This metric has these fields:

- **What it measures:** Highest upward speed.
- **Window or phase:** Concentric phase: zero velocity to end of rep ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the top vertical velocity attained in the concentric phase, immediately before takeoff ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** SLSQT default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Force`

This metric has these fields:

- **What it measures:** Highest force across the rep.
- **Window or phase:** Whole rep: start of rep to end of rep (force returns to system weight) ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD describes it as the top force output at any time in the whole repetition ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Force Asymmetry` ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Eccentric Peak Force`

This metric has these fields:

- **What it measures:** Highest force on the way down.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)).
- **Calculation:** VALD defines it as the largest force seen within the eccentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). Restatement: `max F(t)` over the eccentric phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant listed for SQT and Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Concentric Peak Force`

This metric has these fields:

- **What it measures:** Highest force on the way up.
- **Window or phase:** Concentric phase: zero velocity to end of rep ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)).
- **Calculation:** VALD defines it as the highest force seen within the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). Restatement: `max F(t)` over the concentric phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant listed for SQT and Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Eccentric Mean Force Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in average force on the way down.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the difference between left and right in the eccentric force produced ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Force Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in average force on the way up.
- **Window or phase:** Concentric phase: zero velocity to end of rep ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the difference between left and right in the concentric force produced ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse on the way down.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD says it is the net force, totaled across time, in the movement's eccentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `∫ max(F - W_ref, 0) dt` over the eccentric phase, restating the glossary net impulse definition (area "only above body weight", [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The reference weight `W_ref` for loaded squats (body weight or system weight): Not published.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** Ns.
- **Variants:** `Eccentric Impulse – Asymmetry` is an SQT default; SLSQT shows the single-leg value ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse on the way up.
- **Window or phase:** Start of the concentric phase to takeoff, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD lists no take-off key moment for squats; the knowledge base concentric phase runs from zero velocity to end of rep ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)).
- **Calculation:** VALD says it is the net force, totaled across time, from when the concentric phase begins until takeoff ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `∫ max(F - W_ref, 0) dt` over the concentric phase, restating the glossary net impulse definition (area "only above body weight", [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The reference weight `W_ref` for loaded squats (body weight or system weight): Not published.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** Ns.
- **Variants:** `Concentric Impulse – Asymmetry` is an SQT default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Power`

This metric has these fields:

- **What it measures:** Highest power on the way down.
- **Window or phase:** Eccentric phase: start of rep to zero velocity ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the top power output reached in the eccentric phase ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: Extreme of `F*v`; sign not published.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Peak Power / BM`

This metric has these fields:

- **What it measures:** Highest upward power relative to body mass.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for SQT.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/kg.
- **Variants:** Listed for SLSQT ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Eccentric Deceleration Peak Force`

This metric has these fields:

- **What it measures:** Highest force while slowing the descent.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the highest force in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `max F(t)` in the deceleration phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** Also for Push Up.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Force`

This metric has these fields:

- **What it measures:** Average force while slowing the descent.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean force in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** Also for Push Up.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Peak Force / BW`

This metric has these fields:

- **What it measures:** Deceleration peak force normalised to body weight.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the highest vertical force in eccentric deceleration of a rep, expressed relative to body weight ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: Normalisation basis not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power`

This metric has these fields:

- **What it measures:** Average power while slowing the descent.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean mechanical power, meaning force x velocity, in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** `/ BM` variant.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power / BM`

This metric has these fields:

- **What it measures:** Deceleration mean power relative to body mass.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean eccentric deceleration power in a rep, scaled to body mass ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean power / BM`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Velocity`

This metric has these fields:

- **What it measures:** Average speed while slowing the descent.
- **Window or phase:** Deceleration phase: peak negative velocity to the start of the concentric phase ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the mean vertical velocity of the center of mass across the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Additional Load`

This metric has these fields:

- **What it measures:** External load used in the test.
- **Window or phase:** Before each rep: ForceDecks gets the load by subtracting body weight from the resting weight before each rep ([Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load)).
- **Calculation:** VALD's definition: Not published. Restatement: Entered manually or calculated by subtracting body weight from the resting weight before each rep ([Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load)).
- **Inputs:** Body weight, resting system weight.
- **Units:** Not published.
- **Variants:** Exported for LCMJ, LSJ, PUSHUPT, SLSQT and SQT since 2026-09-28 ([VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; external load ([factor details](README.md#factors-that-change-the-numbers)). Entering the wrong load produces poor start-of-movement detection and missed reps ([User Guide p.40](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Sources:** [Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load), [VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026), [User Guide p.40](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Bodyweight in Kilograms`

This metric has these fields:

- **What it measures:** The athlete's measured body mass.
- **Window or phase:** Weighing period before the test ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula. VALD added it to 'most tests' and recommends it to retrieve weight for jump and functional tests ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Inputs:** Weighing period.
- **Units:** kg.
- **Variants:** `Bodyweight in Pounds`. Test-level `weight` field in the API, which is -1 when weighing was skipped ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Bodyweight in Pounds`

This metric has these fields:

- **What it measures:** The athlete's measured body mass in pounds.
- **Window or phase:** Weighing period before the test ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula.
- **Inputs:** Weighing period.
- **Units:** lb.
- **Variants:** `Bodyweight in Kilograms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS).

### Push up and plyometric push up (PUSHUPT, PPU)

Push-up tests with hands on the plates ([ForceDecks Test Protocol - Push Up](https://support.vald.com/hc/en-au/articles/4999827968665-ForceDecks-Test-Protocol-Push-Up), [ForceDecks Test Protocol - Plyometric Push Up](https://support.vald.com/hc/en-au/articles/40661192006041-ForceDecks-Test-Protocol-Plyometric-Push-Up)). VALD does not publish key moments or a metric count.

#### `Push Up Depth`

This metric has these fields:

- **What it measures:** How far the body lowers in the push up.
- **Window or phase:** Single point: the lowest point of the push up, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The reference starting position is not published.
- **Calculation:** VALD says it is how far the individual travels downward to reach the lowest position in the push up ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `min s(t)`.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** PUSHUPT default; added in a release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Impulse – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in net impulse on the way down (PUSHUPT, PPU).
- **Window or phase:** Eccentric phase (definition for push-ups not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how much the left side and the right side differ in the net force, totaled across time, within the eccentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The push-up eccentric window is not published.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** %.
- **Variants:** PUSHUPT and PPU default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in net impulse on the way up (PUSHUPT, PPU).
- **Window or phase:** Concentric phase (definition for push-ups not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how much the left side and the right side differ in the net force, totaled across time, within the concentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The push-up concentric window is not published.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** %.
- **Variants:** PUSHUPT and PPU default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average downward speed.
- **Window or phase:** Eccentric phase (definition for push-ups not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD describes it as the mean velocity going downward across the eccentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** PUSHUPT default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Concentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average upward speed.
- **Window or phase:** Concentric phase (definition for push-ups not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD describes it as the mean velocity moving upward across the concentric phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** PUSHUPT default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Eccentric Peak Force`

This metric has these fields:

- **What it measures:** Highest force on the way down.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for push-ups.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant listed for Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Concentric Peak Force`

This metric has these fields:

- **What it measures:** Highest force on the way up.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for push-ups.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant listed for Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Maximum Negative Displacement`

This metric has these fields:

- **What it measures:** Lowest point reached.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for push-ups.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** Listed for Push Up ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Push Up Height (Flight Time)`

This metric has these fields:

- **What it measures:** How high the upper body rises in the plyometric push up, from time in the air.
- **Window or phase:** Flight phase of the plyometric push up (detection not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how far the individual rises in the flight phase, worked out from how long they are in the air ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Not published as an equation.
- **Inputs:** Take-off and landing.
- **Units:** cm.
- **Variants:** PPU default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Takeoff Peak Force / BM`

This metric has these fields:

- **What it measures:** Highest take-off force relative to body mass (PPU).
- **Window or phase:** During take-off, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Take-off detection for push-ups is not published.
- **Calculation:** VALD defines it as the top force measured in takeoff, taken relative to the body mass of the individual ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max F / BM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/kg.
- **Variants:** PPU default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Landing Force – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in peak landing force (PPU).
- **Window or phase:** During landing, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Landing detection for push-ups is not published.
- **Calculation:** VALD defines it as how much the left side and the right side differ in the top force measured during landing ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** PPU default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Deceleration Peak Force`

This metric has these fields:

- **What it measures:** Highest force while slowing the descent (PUSHUPT, PPU).
- **Window or phase:** Eccentric deceleration phase within a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the highest force in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** `/ BW` variant listed for PPU and PUSHUPT.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Force`

This metric has these fields:

- **What it measures:** Average force while slowing the descent (PUSHUPT).
- **Window or phase:** Eccentric deceleration phase within a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean force in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power`

This metric has these fields:

- **What it measures:** Average power while slowing the descent (PUSHUPT).
- **Window or phase:** Eccentric deceleration phase within a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean mechanical power, meaning force x velocity, in the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** `/ BM` variant.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Velocity`

This metric has these fields:

- **What it measures:** Average speed while slowing the descent (PUSHUPT).
- **Window or phase:** Eccentric deceleration phase within a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the mean vertical velocity of the center of mass across the eccentric deceleration phase of a rep ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Additional Load`

This metric has these fields:

- **What it measures:** External load used in the push up.
- **Window or phase:** Before each rep: ForceDecks gets the load by subtracting body weight from the resting weight before each rep ([Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load)).
- **Calculation:** VALD's definition: Not published. Restatement: See Squat Assessment entry.
- **Inputs:** Body weight, resting weight.
- **Units:** Not published.
- **Variants:** Exported for PUSHUPT ([VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** External load ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load), [VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026).

### Sit to Stand to Sit (STSTS)

Stand up from a chair and sit back down ([ForceDecks Test Protocol - Sit to Stand to Sit](https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit)). VALD does not publish key moments or a metric count.

#### `Time to Stand`

This metric has these fields:

- **What it measures:** Time to stand up and settle.
- **Window or phase:** Standing movement phase (start-of-standing detection not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the time from when standing begins until the individual is stable in the standing position ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `t_stable_standing - t_start_standing`.
- **Inputs:** Force and stability detection.
- **Units:** s.
- **Variants:** STSTS default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)). Chair height changes difficulty ([ForceDecks Test Protocol - Sit to Stand to Sit](https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [ForceDecks Test Protocol - Sit to Stand to Sit](https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit).

#### `Time to Sit`

This metric has these fields:

- **What it measures:** Time to sit back down.
- **Window or phase:** Sitting movement phase (detection not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the time from when sitting begins until the movement ends ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `t_end_sitting - t_start_sitting`.
- **Inputs:** Force.
- **Units:** s.
- **Variants:** STSTS default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)). Chair height changes difficulty ([ForceDecks Test Protocol - Sit to Stand to Sit](https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [ForceDecks Test Protocol - Sit to Stand to Sit](https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit).

#### `Mean Standing Force – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in average force while standing up.
- **Window or phase:** Standing movement phase (start-of-standing detection not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how much the left side and the right side differ in average force over the standing movement phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** STSTS default. VALD Health calls it 'Average Standing & Sitting Force Asymmetry' ([The Sit-to-Stand Test](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [The Sit-to-Stand Test](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness).

#### `Mean Sitting Force – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in average force while sitting down.
- **Window or phase:** Sitting movement phase (detection not published). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how much the left side and the right side differ in average force over the sitting movement phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** STSTS default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Standing Force`

This metric has these fields:

- **What it measures:** Highest force while standing up, per side.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Listed as left and right side values ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Mean Standing RFD`

This metric has these fields:

- **What it measures:** How quickly force rises while standing up.
- **Window or phase:** Standing movement phase (start-of-standing detection not published). The metric's definition names this window ([The Sit-to-Stand Test](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness)).
- **Calculation:** VALD describes it as the speed at which the client can generate force during the upward standing phase ([The Sit-to-Stand Test](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness)). Restatement: Not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [The Sit-to-Stand Test](https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness).

#### `Bodyweight in Kilograms`

This metric has these fields:

- **What it measures:** The athlete's measured body mass.
- **Window or phase:** Weighing period before the test ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula. VALD added it to 'most tests' and recommends it to retrieve weight for jump and functional tests ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Inputs:** Weighing period.
- **Units:** kg.
- **Variants:** `Bodyweight in Pounds`. Test-level `weight` field in the API, which is -1 when weighing was skipped ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Bodyweight in Pounds`

This metric has these fields:

- **What it measures:** The athlete's measured body mass in pounds.
- **Window or phase:** Weighing period before the test ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula.
- **Inputs:** Weighing period.
- **Units:** lb.
- **Variants:** `Bodyweight in Kilograms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS).

### Balance tests (QSB, SLSB, SLROSB)

Timed centre-of-pressure tests: Quiet Stand, Single Leg Stand, Single Leg Range of Stability ([Centre of Pressure Measurement with ForceDecks](https://support.vald.com/hc/en-au/articles/5000001373209-Centre-of-Pressure-Measurement-with-ForceDecks)). Options: eyes closed, unstable surface, secondary task, and test length ([Centre of Pressure Measurement with ForceDecks](https://support.vald.com/hc/en-au/articles/5000001373209-Centre-of-Pressure-Measurement-with-ForceDecks)). There are no key moments or phases in a Quiet Stand ([User Guide p.60](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

VALD-stated count: 8 Quiet Stand metrics ([User Guide p.60](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

#### `Total Excursion`

This metric has these fields:

- **What it measures:** Total distance the centre of pressure travels.
- **Window or phase:** Whole timed test. VALD says total excursion scales with test length ([Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics)).
- **Calculation:** VALD says it is the full distance the CoP travels ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)). Restatement: `sum of |CoP(i) - CoP(i-1)|` over the test (path length).
- **Inputs:** Centre of pressure X and Y from each plate.
- **Units:** mm.
- **Variants:** API identifier `BAL_COP_TOTAL_EXCURSION`, unit `Millimeter`, supports asymmetry ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Test length; test conditions; lifting a foot during the test ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Mean Velocity`

This metric has these fields:

- **What it measures:** Average speed of the centre of pressure.
- **Window or phase:** Whole timed test. The metric's definition names this window ([Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics)).
- **Calculation:** VALD says it is the total excursion divided by how long the test lasts ([Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics)). Restatement: `Total Excursion / test duration`.
- **Inputs:** Total Excursion, test length.
- **Units:** mm/s.
- **Variants:** Default for all balance tests ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** VALD prefers it over total excursion because it compares across test lengths ([Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics)).
- **What changes the number:** Test conditions; lifting a foot during the test ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Area of CoP Ellipse`

This metric has these fields:

- **What it measures:** Size of the area the centre of pressure covers.
- **Window or phase:** Not published. The metric's definition does not state a window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the area covered by the smallest oval able to hold 95% of the centre of pressure points recorded ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Area of the smallest ellipse containing 95% of CoP samples; fitting method not published.
- **Inputs:** Centre of pressure samples.
- **Units:** mm2.
- **Variants:** Default for all balance tests.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Test length; test conditions; lifting a foot during the test ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `CoP Range, Medial-Lateral`

This metric has these fields:

- **What it measures:** Side-to-side spread of the centre of pressure.
- **Window or phase:** Not published. The metric's definition does not state a window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the maximum side-to-side separation between points of the centre of pressure ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max(CoP) - min(CoP)` along the side-to-side axis. Which raw column (`COPX` or `COPY`) is the medial-lateral axis: Not published.
- **Inputs:** Centre of pressure.
- **Units:** mm.
- **Variants:** `CoP Range, Medial-Lateral – Bilateral` for QSB uses the combined CoP of both plates ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Test length; test conditions; lifting a foot during the test ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `CoP Range, Anterior-Posterior`

This metric has these fields:

- **What it measures:** Front-to-back spread of the centre of pressure.
- **Window or phase:** Not published. The metric's definition does not state a window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the maximum separation in the forwards and backwards direction between points of the centre of pressure ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max(CoP) - min(CoP)` along the front-to-back axis. Which raw column (`COPX` or `COPY`) is the anterior-posterior axis: Not published.
- **Inputs:** Centre of pressure.
- **Units:** mm.
- **Variants:** `CoP Range, Anterior-Posterior – Bilateral` for QSB ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Test length; test conditions; lifting a foot during the test ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Mean Force – Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right difference in average force during the Quiet Stand.
- **Window or phase:** Whole timed test. The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how much the left side and the right side differ in average force over the test ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** %.
- **Variants:** QSB default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Foot placement and landing timing; test conditions ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

### Isometric tests (IMTP and others)

All isometric tests are detected and analysed the same way as the generic Isometric Test ([User Guide p.68](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Key moments: start of movement ('point where exercise commences') and peak vertical force; there are no distinct phases ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Protocol: contract as hard and fast as possible and hold maximum force for at least 2 seconds ([ForceDecks Test Protocol - Isometric Mid-Thigh Pull](https://support.vald.com/hc/en-au/articles/7667730369817-ForceDecks-Test-Protocol-Isometric-Mid-Thigh-Pull)). Body weight is optional for isometric tests except with auto-detect ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).

VALD-stated count: 44 metrics for an isometric test ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

2026 defaults for every isometric test type: `Peak Vertical Force`, `Peak Vertical Force / BM`, `RFD at 100ms`, `Force at 100ms`, `Start Time to 80% Net Peak Force` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).

#### `Peak Vertical Force`

This metric has these fields:

- **What it measures:** The highest total force in the effort.
- **Window or phase:** Entire trial. The User Guide defines the peak vertical force key moment as the greatest force recorded across the whole trial ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the top vertical force measured in the test ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Vertical Force [N] Asymmetry` ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)); `Peak Vertical Force / BM`; `Peak Vertical Force (Net of BW)`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Pretension; which trial you report ([factor details](README.md#factors-that-change-the-numbers)). An impact without pretension can register as the peak; that peak is not a real muscular action ([User Guide p.66](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Sources:** [User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [User Guide p.66](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Vertical Force / BM`

This metric has these fields:

- **What it measures:** Peak force relative to body mass.
- **Window or phase:** Entire trial. The User Guide defines the peak vertical force key moment as the greatest force recorded across the whole trial ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the top vertical force measured in the test, expressed relative to the body mass of the individual ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `Peak Vertical Force / BM`.
- **Inputs:** Peak Vertical Force, body mass.
- **Units:** N/kg.
- **Variants:** The User Guide writes `Peak Vertical Force/BW` ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Vertical Force (Net of BW)`

This metric has these fields:

- **What it measures:** Peak force above body weight.
- **Window or phase:** Entire trial. The User Guide defines the peak vertical force key moment as the greatest force recorded across the whole trial ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). VALD publishes no definition for this metric.
- **Calculation:** VALD's definition: Not published. Restatement: `Peak Vertical Force - BW` (restatement of the name).
- **Inputs:** Peak Vertical Force, body weight.
- **Units:** N.
- **Variants:** Added in a release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). A VALD article on the Isometric Belt Squat, writing about peak force net of body weight in general rather than this export metric, describes it as a measure that practitioners commonly use to compare athletes and to track change over time ([Isometric Belt Squat: A practical alternative for lower-body strength testing](https://valdperformance.com/news/isometric-belt-squat-a-practical-alternative-for-lower-body-strength-testing)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [Isometric Belt Squat: A practical alternative for lower-body strength testing](https://valdperformance.com/news/isometric-belt-squat-a-practical-alternative-for-lower-body-strength-testing).

#### `Force at 100ms`

This metric has these fields:

- **What it measures:** Force 100 ms after the effort starts.
- **Window or phase:** Single point: 100 ms after start of movement, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The isometric start-of-movement rule is not published.
- **Calculation:** VALD says it is the force measured 100 milliseconds following the start of movement ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `F(t_SoM + 0.1 s)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** The User Guide lists `Force @ 100/150/200ms` ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)). A VALD Health table calls force at fixed time points sensitive to execution strategy (for example pretension) and clinician cueing ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development).

#### `Force @ 150ms`

This metric has these fields:

- **What it measures:** Force 150 ms after the effort starts.
- **Window or phase:** Single point: 150 ms after a start event. The name gives only the time point; VALD does not publish the start event for this metric. The User Guide lists `Force @ 100/150/200ms` without a window ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD's definition: Not published. Restatement: `F(t_SoM + 0.15 s)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Name written as `Force @ 100/150/200ms` in the User Guide ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); exact export label not confirmed.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Force @ 200ms`

This metric has these fields:

- **What it measures:** Force 200 ms after the effort starts.
- **Window or phase:** Single point: 200 ms after a start event. The name gives only the time point; VALD does not publish the start event for this metric. The User Guide lists `Force @ 100/150/200ms` without a window ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD's definition: Not published. Restatement: `F(t_SoM + 0.2 s)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** As above ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RFD at 100ms`

This metric has these fields:

- **What it measures:** How fast force rises over the first 100 ms.
- **Window or phase:** The first 100 ms after start of movement, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The isometric start-of-movement rule is not published.
- **Calculation:** VALD describes it as how fast force increases in the first 100 milliseconds following the start of movement ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `(F(t_SoM + 0.1 s) - F(t_SoM)) / 0.1 s`. A VALD Health article describes it as the 'slope of the force-time curve 100ms after the start of the test' ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)); the two wordings differ.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** The User Guide lists a rate of force development at a time epoch you choose ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks), [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RFD - 100-150`

This metric has these fields:

- **What it measures:** Rate of force rise between 100 and 150 ms.
- **Window or phase:** 100 ms to 150 ms after a start event, from the metric name. VALD does not publish the start event for this metric.
- **Calculation:** VALD's definition: Not published. Restatement: `(F(t_SoM + 0.15 s) - F(t_SoM + 0.1 s)) / 0.05 s` (inferred from the name; not published).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** Listed for SLISOT ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Start Time to 80% Net Peak Force`

This metric has these fields:

- **What it measures:** Time to reach 80% of peak force above body weight.
- **Window or phase:** Start of movement to the time force reaches 80% of net peak vertical force, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The isometric start-of-movement rule is not published.
- **Calculation:** VALD defines it as how long it takes, counting from the start of movement, for vertical force to reach 80% of its net peak ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `t(F - BW = 0.8 * (F_peak - BW)) - t_SoM`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** s.
- **Variants:** `Start Time to 80% Peak Force` is listed for the IMTP ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** The VALD Health default-metrics article describes this net metric as often more reliable than RFD ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)). A separate VALD Health table says `Time to 80% Peak Force` (not the net version) is a more reliable way to assess rapid force development than time to peak force ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks), [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development).

#### `Start Time to 80% Peak Force`

This metric has these fields:

- **What it measures:** Time to reach 80% of peak force.
- **Window or phase:** Start of movement to 80% of peak force, from a general VALD Health table of alternative RFD measures, not a ForceDecks definition ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **Calculation:** VALD defines it as how long it takes, counting from the start of movement, for force to reach 80% of its peak ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development); this is a general VALD Health table of alternative RFD measures that names `Time to 80% Peak Force`, not a ForceDecks metric definition). Restatement: `t(F = 0.8 * F_peak) - t_SoM`; whether VALD uses gross or net force here is not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** Listed for the IMTP ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Start Time to Peak Force`

This metric has these fields:

- **What it measures:** Time from effort start to peak force.
- **Window or phase:** Start of movement to peak force, from a general VALD Health table of alternative RFD measures, not a ForceDecks definition ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **Calculation:** VALD defines it as the elapsed time between the start of movement and peak force ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development); this is a general VALD Health table of alternative RFD measures that names `Time to Peak Force`, not a ForceDecks metric definition). Restatement: `t_Fpeak - t_SoM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** Listed for the ASH test ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Absolute Impulse`

This metric has these fields:

- **What it measures:** Total impulse over the effort.
- **Window or phase:** Not published. The metric's definition does not state a window ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the total work that was performed ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `∫ F dt`; window not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Ns.
- **Variants:** `Absolute Impulse Asymmetry` ([User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.71](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Relative Peak Force`

This metric has these fields:

- **What it measures:** Peak force relative to body size, used in the run-specific iso-push tests.
- **Window or phase:** Entire trial. The User Guide defines the peak vertical force key moment as the greatest force recorded across the whole trial ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). VALD publishes no definition for this metric.
- **Calculation:** VALD's definition: Not published. Restatement: Not published. A VALD cheat sheet plots 'Relative Peak Force (N/N)', which suggests peak force divided by body weight ([Cheat sheet: Quadrant Plots](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/Quadrant_Plot_Natera.pdf)).
- **Inputs:** Peak Vertical Force, body weight.
- **Units:** Not published.
- **Variants:** Named in the Run-Specific Iso-Push protocols ([ForceDecks Test Protocol - Run-Specific Knee Iso-Push](https://support.vald.com/hc/en-au/articles/30764623490713-ForceDecks-Test-Protocol-Run-Specific-Knee-Iso-Push)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Cheat sheet: Quadrant Plots](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/Quadrant_Plot_Natera.pdf), [ForceDecks Test Protocol - Run-Specific Knee Iso-Push](https://support.vald.com/hc/en-au/articles/30764623490713-ForceDecks-Test-Protocol-Run-Specific-Knee-Iso-Push).

#### `Impulse (Net of BW)`

This metric has these fields:

- **What it measures:** Impulse above body weight.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published; added as a new metric in a release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** Not published.
- **Variants:** Test types not stated.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Isometric start-of-movement detection; pretension; weighing position; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Bodyweight in Kilograms`

This metric has these fields:

- **What it measures:** The athlete's measured body mass.
- **Window or phase:** Weighing period, in the test position when only part of the body is on the plates ([ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test), [User Guide p.64](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula. VALD added it to 'most tests' and recommends it to retrieve weight for jump and functional tests ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Inputs:** Weighing period.
- **Units:** kg.
- **Variants:** `Bodyweight in Pounds`. Test-level `weight` field in the API, which is -1 when weighing was skipped ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test), [User Guide p.64](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Bodyweight in Pounds`

This metric has these fields:

- **What it measures:** The athlete's measured body mass in pounds.
- **Window or phase:** Weighing period, in the test position when only part of the body is on the plates ([ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test), [User Guide p.64](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). If the weighing stage is skipped, the system may measure body weight from the period where the individual is stable on the plates ([Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula.
- **Inputs:** Weighing period.
- **Units:** lb.
- **Variants:** `Bodyweight in Kilograms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test), [User Guide p.64](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS).

### General Force-Time Analysis (GFTA)

Manual analysis of any movement after marking trial ranges; Windows only ([User Guide p.73](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). There is no start of movement or phase detection ([User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

#### `Peak Force`

This metric has these fields:

- **What it measures:** Highest force in the marked range.
- **Window or phase:** User-marked trial range. The User Guide names peak force as a GFTA metric ([User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)) and says the marked ranges are analysed ([User Guide p.73](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD's definition: Not published. Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Key moment shown for GFTA ([User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)). The marked range sets the value.
- **Sources:** [User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [User Guide p.73](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Minimum Force`

This metric has these fields:

- **What it measures:** Lowest force in the marked range.
- **Window or phase:** User-marked trial range. The User Guide names minimum force as a GFTA metric ([User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)) and says the marked ranges are analysed ([User Guide p.73](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD's definition: Not published. Restatement: `min F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Key moment shown for GFTA ([User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)). The marked range sets the value.
- **Sources:** [User Guide p.72](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [User Guide p.73](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Standing Weight Asymmetry`

This metric has these fields:

- **What it measures:** Left versus right weight bearing while standing.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Left and right force.
- **Units:** %.
- **Variants:** Listed for GFTA ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

### Cross-test ratios (DSI, EUR)

These combine results from two tests.

#### `Dynamic Strength Index (DSI)`

This metric has these fields:

- **What it measures:** Ballistic peak force compared with isometric peak force.
- **Window or phase:** Two separate tests: a ballistic test and an isometric test ([ForceDecks Dynamic Strength Index](https://support.vald.com/hc/en-au/articles/5000254279065-ForceDecks-Dynamic-Strength-Index-DSI-Reports)).
- **Calculation:** VALD defines this metric as a ratio linking an individual's isometric peak force production with their ballistic peak force production ([ForceDecks Dynamic Strength Index](https://support.vald.com/hc/en-au/articles/5000254279065-ForceDecks-Dynamic-Strength-Index-DSI-Reports)). Restatement: `DSI = ballistic peak force / isometric peak force`. A VALD example gives a DSI of 0.38 for a CMJ peak force of 2,488 N and an Iso Belt Squat peak force of 6,521 N ([Recalibrating DSI with the Isometric Belt Squat](https://valdperformance.com/news/recalibrating-dsi-with-the-isometric-belt-squat)); VALD Hub uses the isometric test as the 'denominator' ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Inputs:** CMJ or SJ peak force; IMTP or Isometric Belt Squat peak force.
- **Units:** Ratio.
- **Variants:** Configured in VALD Hub; the Isometric Belt Squat can be the denominator ([VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Comparison with standard methods or other vendors:** VALD warns IMTP-based thresholds do not transfer to the Iso Belt Squat ([Recalibrating DSI with the Isometric Belt Squat](https://valdperformance.com/news/recalibrating-dsi-with-the-isometric-belt-squat)).
- **What changes the number:** Which trial you report ([factor details](README.md#factors-that-change-the-numbers)). Which test is the isometric denominator; tagging of tests used in the report.
- **Sources:** [ForceDecks Dynamic Strength Index](https://support.vald.com/hc/en-au/articles/5000254279065-ForceDecks-Dynamic-Strength-Index-DSI-Reports), [Recalibrating DSI with the Isometric Belt Squat](https://valdperformance.com/news/recalibrating-dsi-with-the-isometric-belt-squat), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes).

#### `Eccentric Utilization Ratio (EUR)`

This metric has these fields:

- **What it measures:** CMJ height compared with SJ height.
- **Window or phase:** Two separate tests: a countermovement jump (CMJ) and a squat jump (SJ) ([Understanding the Eccentric Utilization Ratio](https://valdperformance.com/news/understanding-the-eccentric-utilization-ratio-eur)).
- **Calculation:** VALD describes it as a comparison of jump height in a countermovement jump (CMJ) with jump height in a squat jump (SJ) ([Understanding the Eccentric Utilization Ratio](https://valdperformance.com/news/understanding-the-eccentric-utilization-ratio-eur)). Restatement: The article shows the formula only as an image. Its example threshold (EUR greater than 1.1) is consistent with `CMJ height / SJ height`, but the text does not state it.
- **Inputs:** CMJ jump height, SJ jump height.
- **Units:** Ratio.
- **Variants:** Not a named ForceDecks export metric in VALD's public sources.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Understanding the Eccentric Utilization Ratio](https://valdperformance.com/news/understanding-the-eccentric-utilization-ratio-eur).

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
