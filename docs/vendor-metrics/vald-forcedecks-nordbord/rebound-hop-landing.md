# VALD ForceDecks and NordBord metrics: rebound, hop, and landing tests

This page explains how VALD ForceDecks calculates each metric for these tests. It covers the countermovement rebound jump (CMRJ, SLCMRJ), hop tests (HJ, SLHJ), Hop and Return (SLHAR), and Land and Hold (LAH, SLLAH), with 60 metric blocks. Checked against: the VALD ForceDecks Technical Glossary V2.0 (March 2024), the VALD ForceDecks User Guide v2 (November 2023), the External ForceDecks API specification (`v2019q3`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

This page is part of [VALD ForceDecks and NordBord metrics](README.md). The index explains how to read each block, and it holds the event and term glossary, the factors that change the numbers, the conflicts in VALD's own sources, the Not published list, the worked example, and the sources with access dates. VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](../vald-other-products/README.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](../hawkin-dynamics/README.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](../hawkin-dynamics/README.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Metric blocks

### Countermovement rebound jump (CMRJ, SLCMRJ)

A CMJ followed immediately by a rebound jump ([User Guide p.16](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Key moments: start of movement (20 N), first take-off (force below 20 N), first landing (above 20 N), peak impact force, contact trough, peak drive-off force, second take-off and second landing ([User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

VALD-stated count: 82 metrics ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). VALD has not published a CMRJ glossary table. The blocks below cover every CMRJ metric name found in public sources; the remainder are Not published.

#### `First Jump Height (Imp-Mom)`

This metric has these fields:

- **What it measures:** Height of the first (countermovement) jump from take-off velocity.
- **Window or phase:** Not published. The metric's definition does not state a window. It refers only to force applied during the contact phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines this metric as how high the first jump went, worked out by the impulse-momentum method, where the velocity change comes from the force that was applied in the contact phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: VALD does not publish the equation; `v_TO1^2 / (2 g)` is a common restatement.
- **Inputs:** Force, body weight, first take-off.
- **Units:** cm.
- **Variants:** Default CMRJ and SLCMRJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Rebound Jump Height (Imp-Mom)`

This metric has these fields:

- **What it measures:** Height of the rebound jump from take-off velocity.
- **Window or phase:** Not published. The metric's definition does not state a window. It refers only to force applied during the contact phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD describes it as how high the rebound jump went, worked out by the impulse-momentum method, where the velocity change comes from the force that was applied in the contact phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Not published as an equation. How velocity is carried through the first flight and landing is not published.
- **Inputs:** Force, body weight, second take-off.
- **Units:** cm.
- **Variants:** Default CMRJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Rebound Jump Height (Flight Time)`

This metric has these fields:

- **What it measures:** Height of the rebound jump from time in the air.
- **Window or phase:** Flight after the rebound: second take-off to second landing ([User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD says it is how high the rebound jump went, worked out from the time the person is airborne ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Not published as an equation; `g * FT^2 / 8` is a common restatement.
- **Inputs:** Second take-off and second landing.
- **Units:** cm.
- **Variants:** Default SLCMRJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Rebound Contact Time`

This metric has these fields:

- **What it measures:** Ground contact time between the first landing and the rebound take-off.
- **Window or phase:** Rebound phase: first landing (force above 20 N) to second take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as how long the individual stays on the plates during the rebound phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `t_TO2 - t_L1`.
- **Inputs:** First landing and second take-off.
- **Units:** ms.
- **Variants:** A release fixed its display unit from cm to ms ([ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes).

#### `Rebound RSI (JH (Flight Time) / Contact Time)`

This metric has these fields:

- **What it measures:** Rebound jump height per unit of rebound contact time.
- **Window or phase:** Combines rebound jump height (flight time) and rebound contact time, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Rebound phase: first landing to second take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines this metric as the rebound's score on the reactive strength index (RSI), found by dividing jump height, based on flight time, by contact time ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `Rebound JH_FT / Rebound Contact Time`.
- **Inputs:** Rebound Jump Height (Flight Time), Rebound Contact Time.
- **Units:** Not published.
- **Variants:** Default CMRJ and SLCMRJ metric; unit shown as `-` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Takeoff Peak Power / BM`

This metric has these fields:

- **What it measures:** Peak power of the first jump relative to body mass.
- **Window or phase:** Not published. The metric's definition does not state a window ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The User Guide names a Takeoff Phase, start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not link this metric to it.
- **Calculation:** VALD describes it as the power the individual produces, normalized to their body mass ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: Not published as a window or equation beyond the description.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Drop Landing Force`

This metric has these fields:

- **What it measures:** Left versus right difference in landing force on the first landing.
- **Window or phase:** Landing from the first jump, as the definition states ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). First landing: force rises above 20 N ([User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The end of the landing window is not published.
- **Calculation:** VALD says it is the L/R difference in the landing force of the first jump ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Left and right force.
- **Units:** Not published.
- **Variants:** The User Guide lists it only under Asymmetry Metrics ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Force`

This metric has these fields:

- **What it measures:** Left versus right difference in landing force on the second landing.
- **Window or phase:** Landing from the second jump, as the definition states ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Second landing: force rises above 20 N ([User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The end of the landing window is not published.
- **Calculation:** VALD defines it as the L/R difference in the landing force of the second jump ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: VALD does not publish which formula this metric uses; the glossary formula is `(left − right) / max(left, right) × 100` ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Left and right force.
- **Units:** Not published.
- **Variants:** The User Guide lists it only under Asymmetry Metrics ([User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.21](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [User Guide p.19](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Takeoff Eccentric Deceleration Peak Force`

This metric has these fields:

- **What it measures:** Highest force while decelerating before the first take-off.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines this metric as the peak force recorded within the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `max F(t)` in the deceleration phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** `/ BW` variant.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Takeoff Eccentric Deceleration Peak Force / BW`

This metric has these fields:

- **What it measures:** Deceleration peak force normalised to body weight.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the peak vertical force in eccentric deceleration, expressed relative to body weight ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: Normalisation basis (weight or mass) not published.
- **Inputs:** Takeoff Eccentric Deceleration Peak Force, body weight.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Takeoff Concentric Impulse:Eccentric Deceleration Impulse Ratio`

This metric has these fields:

- **What it measures:** Push impulse compared with deceleration impulse, first jump.
- **Window or phase:** Combines net concentric impulse and net eccentric deceleration impulse, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD says it is net concentric impulse set against net eccentric deceleration impulse as a ratio ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `J_con / J_dec`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Acceleration Phase Duration`

This metric has these fields:

- **What it measures:** Time from first movement to the fastest downward speed.
- **Window or phase:** Start of movement to maximum negative velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the time from the start of movement to the point of maximum negative velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `t_EPV - t_SoM`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Deceleration Phase Duration`

This metric has these fields:

- **What it measures:** Time from fastest downward speed to the bottom of the dip.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines this metric as the time from maximum negative velocity until velocity is zero, which marks the start of the concentric phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `t_ZV - t_EPV`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Takeoff Concentric Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of first-jump contraction time spent pushing up.
- **Window or phase:** Combines the duration of the concentric phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the concentric phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * concentric duration / contraction time`.
- **Inputs:** Phase durations.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Deceleration:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of first-jump contraction time spent decelerating.
- **Window or phase:** Combines the duration of the eccentric deceleration phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD says it is the share of total contraction time, as a percentage, taken up by the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * deceleration duration / contraction time`.
- **Inputs:** Phase durations.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Unloading Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of first-jump contraction time spent unloading.
- **Window or phase:** Combines the duration of the eccentric unloading phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD defines it as the share of total contraction time, as a percentage, taken up by the eccentric unloading phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * unloading duration / contraction time`.
- **Inputs:** Phase durations.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Yielding Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of first-jump contraction time spent yielding.
- **Window or phase:** Combines the duration of the eccentric yielding phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD defines this metric as the share of total contraction time, as a percentage, taken up by the eccentric yielding phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * yielding duration / contraction time`.
- **Inputs:** Phase durations.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Takeoff Eccentric Acceleration Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of first-jump contraction time spent accelerating downward.
- **Window or phase:** Combines the duration of the eccentric acceleration phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the percentage of total contraction time taken up by the eccentric acceleration phase, which is made up of the eccentric unloading and eccentric yielding phases ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * acceleration-phase duration / contraction time`.
- **Inputs:** Phase durations.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power`

This metric has these fields:

- **What it measures:** Average power while decelerating.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD says it is the mean mechanical power, meaning force multiplied by velocity, over the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** `/ BM` variant.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Eccentric Deceleration Mean Power / BM`

This metric has these fields:

- **What it measures:** Deceleration mean power relative to body mass.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean power over the eccentric deceleration phase, expressed relative to body mass ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `Eccentric Deceleration Mean Power / BM`.
- **Inputs:** Mean power, body mass.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Eccentric Deceleration Mean Velocity`

This metric has these fields:

- **What it measures:** Average downward speed while decelerating.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity to zero velocity ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The User Guide Takeoff Phase runs from start of movement to first take-off ([User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD does not state which jump a deceleration metric without the `Takeoff` prefix uses. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the mean vertical velocity of the center of mass across the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [User Guide p.20](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Take-off Momentum`

This metric has these fields:

- **What it measures:** Body mass times take-off velocity.
- **Window or phase:** Single point: take-off, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Which take-off (first or second) is not published.
- **Calculation:** VALD says it is body mass times the vertical velocity at take-off ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `BM * v_TO`.
- **Inputs:** Take-off velocity, body mass.
- **Units:** Not published.
- **Variants:** None published. Which take-off (first or second) is not published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Mean Landing Force`

This metric has these fields:

- **What it measures:** Average force during landing.
- **Window or phase:** Landing phase; VALD does not state which landing for the CMRJ ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the mean of the vertical force across the landing phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Landing Stiffness`

This metric has these fields:

- **What it measures:** Landing force divided by how far the centre of mass sinks.
- **Window or phase:** Single point: maximum negative displacement during landing, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The end of the landing window is not published.
- **Calculation:** VALD defines it as the result of dividing force by the displacement of the center of mass at its maximum negative displacement while landing ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `F / |s|` at the lowest landing point.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

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

### Hop tests (HJ, SLHJ)

Repeated stiff-legged hops on the forefoot; commonly 10 hops with the best 5 analysed ([ForceDecks Test Protocol - Hop Test](https://support.vald.com/hc/en-au/articles/4999906960153-ForceDecks-Test-Protocol-Hop-Test)). At least 5 hops are required for auto-analysis ([User Guide p.47](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The best hop is the hop with the highest RSI; the best 5 hops are the 5 with the highest RSI ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test)).

VALD-stated count: 54 metrics ([User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). No public glossary table exists for hop tests.

#### `Mean RSI (Jump Height / Contact Time)`

This metric has these fields:

- **What it measures:** Average reactive strength index across the best hops.
- **Window or phase:** Best hops: the hops with the highest RSI. The User Guide describes the best hop and the best 5 hops ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); the default page says 'selected best hops' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines this metric as the mean reactive strength index (RSI) over the chosen best hops, found by taking jump height, derived from flight time, and dividing it by contact time ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `mean over best hops of JH_FT / Contact Time`.
- **Inputs:** Flight time and contact time per hop.
- **Units:** Not published.
- **Variants:** Default HJ metric. The SLHJ default is written `Mean RSI (JH (Flight Time) / Contact Time)` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** The User Guide links the mean of the best 5 of 10 hops to the '10/5 RSI' ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Mean Jump Height (Flight Time)`

This metric has these fields:

- **What it measures:** Average flight-time hop height across the best hops.
- **Window or phase:** Best hops: the hops with the highest RSI. The User Guide describes the best hop and the best 5 hops ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); the default page says 'selected best hops' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD describes it as the mean jump height over the chosen best hops, worked out from flight time ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Mean of per-hop flight-time heights.
- **Inputs:** Flight time per hop.
- **Units:** cm.
- **Variants:** Default HJ and SLHJ metric.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Mean Contact Time`

This metric has these fields:

- **What it measures:** Average ground contact time across the best hops.
- **Window or phase:** Best hops: the hops with the highest RSI. The User Guide describes the best hop and the best 5 hops ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); the default page says 'selected best hops' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD says it is the mean length of time spent touching the plates, taken over the chosen best hops ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Mean of per-hop contact times.
- **Inputs:** Landing and take-off per hop.
- **Units:** ms.
- **Variants:** Default HJ and SLHJ metric.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Mean Impulse`

This metric has these fields:

- **What it measures:** Average impulse per hop across the best hops.
- **Window or phase:** Best hops: the hops with the highest RSI. The User Guide describes the best hop and the best 5 hops ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); the default page says 'selected best hops' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the mean, over the chosen best hops, of the total force applied across time in a hop ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Mean per-hop impulse; whether it is net or absolute is not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Ns.
- **Variants:** `Mean Impulse – Asymmetry` is a default HJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The common-tests page lists the unit as N/s, which conflicts with Ns ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.51](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Best Reactive Strength Index (RSI)`

This metric has these fields:

- **What it measures:** The highest RSI of any single hop.
- **Window or phase:** The single hop with the highest RSI ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test)). The metric's definition names this window ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the absolute best RSI (FT:CT) among a series of hops ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `max over hops of Flight Time / Contact Time`.
- **Inputs:** Flight time and contact time per hop.
- **Units:** Not published.
- **Variants:** None published; the export label may differ from the User Guide wording.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test), [User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RSI (Flight Time/Contact Time)`

This metric has these fields:

- **What it measures:** Flight time divided by contact time.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: `Flight Time / Contact Time` per the User Guide RSI definition ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Inputs:** Flight time, contact time.
- **Units:** Unitless.
- **Variants:** Listed for the Single Leg Hop Test ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)). Window (best hop or mean) not published. The glossary defines the same-named drop jump metric as the ratio of flight time to contact time ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); VALD does not confirm that the hop version uses it.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Contact Time`

This metric has these fields:

- **What it measures:** Time on the ground between hops.
- **Window or phase:** Each hop: time on the ground between hops, as the definition states ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD describes it as the duration spent on the ground in between every hop ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: Per-hop `t_TO - t_L`.
- **Inputs:** Landing and take-off per hop.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Mean Active Stiffness`

This metric has these fields:

- **What it measures:** Average stiffness of the hops.
- **Window or phase:** Not published. The metric's definition does not state a window or which hops are averaged ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD defines it as the result of dividing peak force by displacement ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: Mean over hops of `peak force / displacement`; which hops and which displacement are not published.
- **Inputs:** Force, displacement.
- **Units:** N/m.
- **Variants:** Listed for the SLHJ ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; stability before and after the movement; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Peak Force`

This metric has these fields:

- **What it measures:** Highest force across the hop test.
- **Window or phase:** Entire hop test, as the definition states ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Calculation:** VALD describes it as the top force output reached at any point in the whole hop test ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Force Asymmetry` (per hop) and `Mean Peak Force Asymmetry` (average of per-rep peaks) ([User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Number and style of hops; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.52](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

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

### Hop and Return (SLHAR)

A single-leg hop test listed with Contact Time, Concentric Duration, Eccentric Duration and Time to Stabilization ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD does not publish key moments or a metric count for this test.

#### `Contact Time`

This metric has these fields:

- **What it measures:** Time on the plates during the hop and return.
- **Window or phase:** Not published. The metric's definition does not state a window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD says it is how long the individual stays touching the plates ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Not published.
- **Inputs:** Landing and take-off events.
- **Units:** s.
- **Variants:** Default SLHAR metric.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak First Landing Force`

This metric has these fields:

- **What it measures:** Highest force on the first landing.
- **Window or phase:** First landing. The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the top force measured in the first landing ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max F(t)` on first landing.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Default SLHAR metric.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Takeoff Force`

This metric has these fields:

- **What it measures:** Highest force during the second take-off.
- **Window or phase:** Second take-off phase. The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the top force measured in the second takeoff phase ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Default SLHAR metric.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Time to Stabilization`

This metric has these fields:

- **What it measures:** Time from landing until force settles.
- **Window or phase:** Landing to stabilisation. The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the time between landing and the point where force becomes stable ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: Not published for SLHAR. For Land and Hold, VALD defines stabilised as force within a 15 N standard deviation for 0.5 s ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** A release fixed inconsistent calculation of this metric for Hop and Return ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Duration`

This metric has these fields:

- **What it measures:** Length of the absorbing phase.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for SLHAR.
- **Inputs:** Phase events.
- **Units:** ms.
- **Variants:** Listed for SLHAR in ms and in s on the common-tests page ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

#### `Concentric Duration`

This metric has these fields:

- **What it measures:** Length of the pushing phase.
- **Window or phase:** Not published.
- **Calculation:** VALD's definition: Not published. Restatement: Not published for SLHAR.
- **Inputs:** Phase events.
- **Units:** ms.
- **Variants:** Listed for SLHAR in ms and in s ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application).

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

### Land and Hold (LAH, SLLAH)

Land from a box or the ground and hold still ([ForceDecks Test Protocol - Land and Hold](https://support.vald.com/hc/en-au/articles/4999895084185-ForceDecks-Test-Protocol-Land-and-Hold)). Key moments: drop landing, peak landing force, stabilised (force within a 15 N standard deviation for 0.5 s) ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)). Step off the plates for 3 seconds between trials or reps may be detected as drop jumps ([User Guide p.55](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

VALD-stated count: 3 metrics in 2023 ([User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); new LAH and SLLAH metrics were added on 2026-07-01 ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).

#### `Time to Stabilization`

This metric has these fields:

- **What it measures:** Time from landing until the athlete is still.
- **Window or phase:** Drop landing to the stabilised point: force within a 15 N standard deviation for 0.5 s ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Calculation:** VALD defines it as the time between landing and the point where force becomes stable ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `t_stable - t_DL`, where stable means force within a 15 N standard deviation for 0.5 s ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)).
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** `Time to Stabilization – Bilateral Total` is the LAH default; SLLAH reports the single-leg value ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)). Stepping off too soon, putting the other foot down or hopping prevents detection ([User Guide p.56](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.56](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Drop Landing Force`

This metric has these fields:

- **What it measures:** Highest force during the landing.
- **Window or phase:** During a drop landing, as the definition states ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD does not publish the start and end of this window.
- **Calculation:** VALD defines it as the top force measured in a drop landing ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). Restatement: `max F(t)` after drop landing.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Drop Landing Force – Bilateral Total` and `Peak Drop Landing Force – Asymmetry` are LAH defaults ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Drop Landing Force / BW`

This metric has these fields:

- **What it measures:** Peak landing force relative to body size.
- **Window or phase:** During the drop landing. The release notes describe the metric as the peak force reached in the drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). VALD does not publish the start and end of this window.
- **Calculation:** VALD describes it as the peak force in the drop landing, expressed relative to bodyweight ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: Peak Drop Landing Force divided by body weight or mass; the default page shows N/kg ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Inputs:** Peak Drop Landing Force, body weight.
- **Units:** N/kg.
- **Variants:** SLLAH default.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Landing Force`

This metric has these fields:

- **What it measures:** Highest force produced on landing.
- **Window or phase:** On landing, as the definition states ([User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). VALD does not publish the start and end of this window.
- **Calculation:** VALD defines it as the top force generated when landing ([User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). Restatement: `max F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [User Guide p.57](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Stability Depth`

This metric has these fields:

- **What it measures:** How low the centre of mass sits once the athlete is stable.
- **Window or phase:** Single point: the moment the athlete is stabilised ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)). The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD defines it as the system center-of-mass vertical displacement, in the negative direction, at the moment when the athlete becomes stable ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `s(t_stable)` (negative).
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Peak Drop Landing Acceleration`

This metric has these fields:

- **What it measures:** Highest acceleration during the landing.
- **Window or phase:** During drop landing. VALD lists drop landing as a key moment, not a phase ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)); the start and end of this window are not published. The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD says it is the peak acceleration reached in a drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `max a(t)`.
- **Inputs:** Force, body weight, body mass.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Mean Drop Landing Acceleration`

This metric has these fields:

- **What it measures:** Average acceleration during the landing.
- **Window or phase:** During drop landing. VALD lists drop landing as a key moment, not a phase ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)); the start and end of this window are not published. The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD says it is the mean acceleration over a drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `mean a(t)`.
- **Inputs:** Force, body weight, body mass.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Peak Drop Landing Velocity`

This metric has these fields:

- **What it measures:** Peak velocity during the landing.
- **Window or phase:** During drop landing. VALD lists drop landing as a key moment, not a phase ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)); the start and end of this window are not published. The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD says it is the peak velocity reached in a drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: Extreme of `v(t)`; sign not published.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Peak Drop Landing Power`

This metric has these fields:

- **What it measures:** Peak power during the landing.
- **Window or phase:** During drop landing. VALD lists drop landing as a key moment, not a phase ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)); the start and end of this window are not published. The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD says it is the peak power, which is force x velocity, in a drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: Extreme of `F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Passive Stiffness`

This metric has these fields:

- **What it measures:** Impact force divided by how far the centre of mass sinks.
- **Window or phase:** During drop landing. VALD lists drop landing as a key moment, not a phase ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)); the start and end of this window are not published. The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD defines it as peak passive (impact) force divided by the change in center-of-mass displacement between contact and its minimum value, which is the lowest point on the pink line in the drop landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `F_impact / |s_min - s_contact|`.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Landing Stiffness`

This metric has these fields:

- **What it measures:** Landing force divided by displacement at the lowest point.
- **Window or phase:** Single point: maximum negative displacement during landing, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The end of the landing window is not published.
- **Calculation:** VALD describes it as the result of dividing force by the centre-of-mass displacement, taken at the maximum negative displacement in landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `F / |s|` at the lowest point.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Drop Landing RFD`

This metric has these fields:

- **What it measures:** How fast force rises from landing to the landing peak.
- **Window or phase:** Drop landing to peak landing force ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). The metric's definition names this window ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)).
- **Calculation:** VALD defines it as the rate of force development between the landing and the moment of peak force within the landing ([ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026)). Restatement: `(F_peak - F(t_DL)) / (t_peak - t_DL)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS v3.3.0 Release Notes, 2026-07-01](https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026).

#### `Drop Landing`

This metric has these fields:

- **What it measures:** The time at which the drop landing occurred.
- **Window or phase:** Single point: the drop landing key moment ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD's definition: Not published. Restatement: Not published as a formula; a release fixed the SLLAH 'Drop Landing' metric 'to correctly display the time when the drop landing occurred' ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Inputs:** Force, landing threshold.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

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

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
