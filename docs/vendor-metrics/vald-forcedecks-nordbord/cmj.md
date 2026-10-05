# VALD ForceDecks and NordBord metrics: countermovement jump

This page explains how VALD ForceDecks calculates each metric for these tests. It covers the countermovement jump (CMJ) and its loaded, Abalakov, and single-leg variants, with 125 metric blocks. Checked against: the VALD ForceDecks Technical Glossary V2.0 (March 2024), the VALD ForceDecks User Guide v2 (November 2023), the External ForceDecks API specification (`v2019q3`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

This page is part of [VALD ForceDecks and NordBord metrics](README.md). The index explains how to read each block, and it holds the event and term glossary, the factors that change the numbers, the conflicts in VALD's own sources, the Not published list, the worked example, and the sources with access dates. VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](../vald-other-products/README.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](../hawkin-dynamics/README.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](../hawkin-dynamics/README.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Metric blocks

### Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ)

The CMJ is a jump for maximum height with hands on hips ([ForceDecks Test Protocol - Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999886017817-ForceDecks-Test-Protocol-Countermovement-Jump)). ForceDecks analyses the Loaded CMJ (LCMJ), Abalakov jump (ABCMJ) and Single Leg Jump (SLJ) with the same start-of-movement and start-of-integration settings ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis), [Customise Start of Integration Analysis](https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis)), and the 2026 default metrics are the same for CMJ, LCMJ and ABCMJ ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD's glossary lists CMJ metrics only; it does not publish separate LCMJ, ABCMJ or SLJ tables. Treat the blocks below as the CMJ definitions and check SLJ and loaded variants against your own export.

VALD-stated count: the User Guide says ForceDecks reports 112 CMJ metrics on performance and asymmetry ([User Guide p.14](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The glossary V2.0 lists 106 CMJ metric names; release notes add more. This page covers every CMJ metric name found in public sources.

Key moments (knowledge base): start of movement, start of braking phase (minimum eccentric force), start of deceleration (eccentric peak velocity), start of concentric phase (zero velocity), start and end of max RFD, peak take-off force, take-off, landing, peak landing force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).

2026 default CMJ metrics: `Jump Height (Imp-Mom)`, `RSI-modified`, `Eccentric Peak Velocity`, `Eccentric Deceleration Impulse – Asymmetry`, `Countermovement Depth`, `Concentric Impulse – Asymmetry`, `Peak Landing Force – Asymmetry` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). SLJ defaults: `Jump Height (Imp-Mom)`, `Eccentric Deceleration Impulse`, `Eccentric Peak Velocity`, `Countermovement Depth`, `Concentric Impulse`, `RSI-modified` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).

#### `Jump Height (Imp-Mom)`

This metric has these fields:

- **What it measures:** How high the centre of mass rises, worked out from take-off velocity.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as jump height calculated using Body Mass and the centre of mass velocity at the moment of Take-off ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. A common physics restatement is `h = v_TO^2 / (2 g)`, where `v_TO` is take-off velocity (the integral of `F - BW` from the start of integration to take-off, divided by body mass, from the User Guide relations) and `g` is gravity. VALD's value of `g` is not published.
- **Inputs:** Total vertical force, body weight, start of integration, take-off event.
- **Units:** cm (glossary); in on some displays.
- **Variants:** `Jump Height (Imp-Mom) in Inches` (same value in inches) ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Shown as a default CMJ metric in inches in one VALD article ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)).
- **Comparison with standard methods or other vendors:** VALD states impulse-momentum height reduces variability from flight time or landing errors ([Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump)). A VALD Health article describes it as maximum vertical displacement between take-off and landing ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)), which matches the glossary wording for `Jump Height (Imp-Dis)` rather than Imp-Mom.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks), [Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump).

#### `Jump Height (Imp-Mom) in Inches`

This metric has these fields:

- **What it measures:** The Imp-Mom jump height expressed in inches.
- **Window or phase:** Same window as `Jump Height (Imp-Mom)`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Single point: take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Jump Height (Imp-Mom)` after conversion into inches ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_in = h_cm / 2.54` (definition of the inch).
- **Inputs:** Jump Height (Imp-Mom).
- **Units:** in.
- **Variants:** `Jump Height (Imp-Mom)` in cm.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Flight Time)`

This metric has these fields:

- **What it measures:** How high the athlete jumped, worked out from time in the air.
- **Window or phase:** Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as a jump height worked out from `Flight Time` ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. A common physics restatement is `h = g * FT^2 / 8`, where `FT` is flight time in seconds.
- **Inputs:** Take-off and landing events.
- **Units:** cm.
- **Variants:** `Jump Height (Flight Time) in Inches`. API identifier `JUMP_HEIGHT`, group `Takeoff`, unit `Centimeter`, trend `Positive`, no asymmetry ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Jump Height (Flight Time) in Inches`

This metric has these fields:

- **What it measures:** The flight-time jump height expressed in inches.
- **Window or phase:** Same window as `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Jump Height (Flight Time)` after conversion into inches ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_in = h_cm / 2.54`.
- **Inputs:** Jump Height (Flight Time).
- **Units:** in.
- **Variants:** `Jump Height (Flight Time)` in cm.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Imp-Dis)`

This metric has these fields:

- **What it measures:** The highest point the centre of mass reaches in the air, from double-integrated force.
- **Window or phase:** Take-off to landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest displacement reached by the centre of mass, measured between Take-off and landing ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h = max s(t)` for `t` between take-off and landing, where `s(t)` is displacement from the start of integration. Whether the take-off displacement is subtracted is not published.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `RSI-modified`

This metric has these fields:

- **What it measures:** Jump height per unit of time spent on the ground before take-off.
- **Window or phase:** Combines `Jump Height (Flight Time)` and `Contraction Time`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Jump Height (Flight Time)` divided by `Contraction Time` ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `RSImod = JH_FT [m] / CT [s]`. A VALD worked table divides 29.1 cm by 650 ms to give 0.45 m/s, which confirms metres over seconds ([RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple))
- **Inputs:** Jump Height (Flight Time), Contraction Time.
- **Units:** m/s.
- **Variants:** `RSI-modified (Imp-Mom)` uses Imp-Mom jump height instead. The default-metrics page lists the unit as `-` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)); the glossary lists m/s.
- **Comparison with standard methods or other vendors:** The User Guide defines RSImod as jump height divided by contraction time ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD's RSI-mod article gives `RSI-Mod = Jump Height / Contraction Time` ([RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple)). Both match the glossary.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RSI-modified (Imp-Mom)`

This metric has these fields:

- **What it measures:** Imp-Mom jump height per unit of contraction time.
- **Window or phase:** Combines `Jump Height (Imp-Mom)` and `Contraction Time`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Jump Height (Imp-Mom)` divided by `Contraction Time` ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `RSImod_IM = JH_IM [m] / CT [s]`.
- **Inputs:** Jump Height (Imp-Mom), Contraction Time.
- **Units:** m/s.
- **Variants:** `RSI-modified` uses flight-time jump height.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Contraction Time`

This metric has these fields:

- **What it measures:** Time from the first movement to leaving the ground.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time that passes from Start of Movement until Take-off ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `CT = t_TO - t_SoM`.
- **Inputs:** Start of movement and take-off events.
- **Units:** ms.
- **Variants:** The default-metrics page lists the SJ contraction time in s ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** The User Guide glossary gives the same definition and notes it covers eccentric and concentric phases in a CMJ ([User Guide p.101](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)). A long pre-jump movement or a nearby impact before the jump increases contraction time ([Quick Data Quality Check in ForceDecks](https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.101](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Quick Data Quality Check in ForceDecks](https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks).

#### `Flight Time`

This metric has these fields:

- **What it measures:** Time in the air between take-off and landing.
- **Window or phase:** Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the time that passes between Take-off and landing ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `FT = t_L - t_TO`.
- **Inputs:** Take-off and landing events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Flight Time:Contraction Time`

This metric has these fields:

- **What it measures:** Time in the air compared with time spent preparing the jump.
- **Window or phase:** Combines `Flight Time` and `Contraction Time`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Flight Time` compared with `Contraction Time` as a ratio ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `FT:CT = FT / CT`.
- **Inputs:** Flight Time, Contraction Time.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** The User Guide describes FT:CT as jump performance relative to preparation time ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Flight Time:Eccentric Duration`

This metric has these fields:

- **What it measures:** Time in the air compared with the length of the downward phase.
- **Window or phase:** Combines `Flight Time` and `Eccentric Duration`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Flight Time` compared with `Eccentric Duration` as a ratio ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `FT / Eccentric Duration`.
- **Inputs:** Flight Time, Eccentric Duration.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Vertical Velocity at Take-off`

This metric has these fields:

- **What it measures:** Upward speed of the centre of mass when the feet leave the plates.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as how fast the centre of mass is moving when Take-off happens ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `v_TO = (1 / BM) * ∫[t_SoI to t_TO] (F - BW) dt`, using the User Guide relations `a = (F - BW) / m` and `v = v0 + a t` with `v0 = 0` at the start of integration ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Inputs:** Total vertical force, body weight, start of integration, take-off event.
- **Units:** m/s.
- **Variants:** `Take-off Momentum` multiplies this by body mass.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Take-off Momentum`

This metric has these fields:

- **What it measures:** Body mass times take-off velocity.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD says it is Body Mass times the vertical velocity reached at Take-off ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `p = BM * v_TO`. The unit is not published; the API unit list includes `KilogramMeterPerSecond` ([FD API spec](https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json))
- **Inputs:** Vertical Velocity at Take-off, body mass.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API spec](https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json).

#### `Countermovement Depth`

This metric has these fields:

- **What it measures:** How far the centre of mass drops during the dip.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the largest displacement recorded from Start of Movement through Take-off ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `CMD = min s(t)` between start of movement and take-off; VALD reports more negative values for a deeper dip ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks))
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** Default CMJ metric in VALD's 2026 defaults ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** VALD describes it as the distance from the start position to the lowest point of the countermovement ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Displacement at Take-off`

This metric has these fields:

- **What it measures:** How far the centre of mass has risen from standing height at the moment of take-off.
- **Window or phase:** From the initial starting position to take-off, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the displacement from the starting position to Take-off, meaning from upright standing until the athlete leaves the force plates ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `s(t_TO)`, displacement relative to the start of integration.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Power`

This metric has these fields:

- **What it measures:** The highest power produced while pushing up.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest power reached during the concentric phase ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max P(t)` over the concentric phase, where `P = F * v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Peak Power / BM` (W/kg). The SJ default description adds 'assuming zero starting velocity' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Power / BM`

This metric has these fields:

- **What it measures:** Peak power relative to body mass.
- **Window or phase:** Same window as `Peak Power`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Peak Power` divided by Body Mass ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Power / BM`.
- **Inputs:** Peak Power, body mass.
- **Units:** W/kg.
- **Variants:** `Peak Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Velocity at Peak Power`

This metric has these fields:

- **What it measures:** Upward speed at the instant of peak power.
- **Window or phase:** Single point: the instant of peak power, with peak power found between start of movement and take-off, as the definition states ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the velocity reached by the centre of mass when Peak Power occurs, using the Peak Power found within the span from Start of Movement to Take-off ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `v(t_PP)`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Force at Peak Power`

This metric has these fields:

- **What it measures:** Force at the instant of peak power.
- **Window or phase:** Single point: the instant of peak power. The definition gives no search window for peak power ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). VALD defines `Peak Power` as the maximum power during the concentric phase ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)), but `Velocity at Peak Power` searches between start of movement and take-off ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Which one this metric uses is not published.
- **Calculation:** VALD says it is the vertical force present at the instant of Peak Power ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `F(t_PP)`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** N.
- **Variants:** Asymmetry variant listed as commonly used for the SJ ([User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Movement Start to Peak Power`

This metric has these fields:

- **What it measures:** Time from first movement to peak power.
- **Window or phase:** Start of movement to the instant of peak power before take-off, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time from Start of Movement to the moment of Peak Power, which comes before Take-off ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_PP - t_SoM`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Movement Start to Peak Force`

This metric has these fields:

- **What it measures:** Time from first movement to peak force.
- **Window or phase:** Start of movement to the instant of peak vertical force before take-off, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the time from Start of Movement to the moment of Peak Vertical Force, which comes before Take-off ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_Fmax - t_SoM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Take-off Peak Force`

This metric has these fields:

- **What it measures:** The highest total force from first movement to take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest vertical force reached in the span from Start of Movement to Take-off ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` between start of movement and take-off.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Take-off Peak Force / BM` (N/kg). The knowledge base names the key moment 'Peak take-off force' ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump).

#### `Take-off Peak Force / BM`

This metric has these fields:

- **What it measures:** Take-off peak force relative to body mass.
- **Window or phase:** Same window as `Take-off Peak Force`, as the definition states ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Take-off Peak Force` divided by Body Mass ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Take-off Peak Force / BM`.
- **Inputs:** Take-off Peak Force, body mass.
- **Units:** N/kg.
- **Variants:** `Take-off Peak Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Net Take-off Force / BM`

This metric has these fields:

- **What it measures:** Peak force above body weight, relative to body mass.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest vertical force from Start of Movement to Take-off, with Body Weight subtracted, then divided by Body Mass ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(max F - BW) / BM`.
- **Inputs:** Take-off Peak Force, body weight, body mass.
- **Units:** N/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Take-off Acceleration`

This metric has these fields:

- **What it measures:** The highest upward acceleration of the centre of mass before take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the highest acceleration reached by the centre of mass from Start of Movement to Take-off ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max a(t)` with `a = (F - BW) / BM` ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Duration`

This metric has these fields:

- **What it measures:** Length of the upward pushing phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as how long the concentric phase lasts ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_TO - t_ZV`.
- **Inputs:** Zero velocity and take-off events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse`

This metric has these fields:

- **What it measures:** Net push above body weight during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the net impulse across the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** `Concentric Impulse – Asymmetry` is a 2026 default CMJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD describes the asymmetry as the percent difference in left and right net impulse ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks).

#### `Concentric Impulse (Abs) / BM`

This metric has these fields:

- **What it measures:** Total (not net) upward-phase impulse relative to body mass.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the absolute impulse across the concentric phase, divided by Body Mass ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_TO] F dt / BM`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s/kg.
- **Variants:** A release fixed its display unit from N s to N s/kg ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Concentric Impulse-50ms`

This metric has these fields:

- **What it measures:** Net impulse in the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across the opening 50ms in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_ZV+0.05 s] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse-100ms`

This metric has these fields:

- **What it measures:** Net impulse in the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the net impulse across the opening 100ms in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_ZV+0.1 s] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse-100ms:Concentric Impulse`

This metric has these fields:

- **What it measures:** Share of the upward net impulse produced in the first 100 ms.
- **Window or phase:** Combines `Concentric Impulse-100ms` and `Concentric Impulse`, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Concentric Impulse-100ms` compared with `Concentric Impulse` as a ratio ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Impulse-100ms / Concentric Impulse`.
- **Inputs:** Concentric Impulse-100ms, Concentric Impulse.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `P1 Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse in the first half (by time) of the upward phase.
- **Window or phase:** First half of the concentric phase, split by time. The concentric phase starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the net impulse in the first 50% portion of the concentric phase, split by time ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_mid] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). `t_mid = (t_ZV + t_TO) / 2`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** VALD maps concentric 'Phase 1' and 'Phase 2' to the first and second 50% of the upward phase ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks).

#### `P2 Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse in the second half (by time) of the upward phase.
- **Window or phase:** Second half of the concentric phase, split by time. The concentric phase ends at take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse in the second 50% portion of the concentric phase, split by time ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_mid to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `P2 Concentric Impulse:P1 Concentric Impulse`

This metric has these fields:

- **What it measures:** How the upward push is split between the second and first halves.
- **Window or phase:** Combines `P2 Concentric Impulse` and `P1 Concentric Impulse`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `P2 Concentric Impulse` compared with `P1 Concentric Impulse` as a ratio ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `P2 / P1`.
- **Inputs:** P1 and P2 Concentric Impulse.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Force`

This metric has these fields:

- **What it measures:** Average total force during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the average vertical force throughout the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)` over the concentric phase. The glossary 'Mean' includes the start and end samples ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Concentric Mean Force / BM` (N/kg).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Force / BM`

This metric has these fields:

- **What it measures:** Average upward-phase force relative to body mass.
- **Window or phase:** Same window as `Concentric Mean Force`, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric Mean Force` divided by Body Mass ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Mean Force / BM`.
- **Inputs:** Concentric Mean Force, body mass.
- **Units:** N/kg.
- **Variants:** `Concentric Mean Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Peak Force`

This metric has these fields:

- **What it measures:** Highest total force during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest vertical force reached in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` over the concentric phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Concentric Peak Force / BM` (N/kg).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Peak Force / BM`

This metric has these fields:

- **What it measures:** Upward-phase peak force relative to body mass.
- **Window or phase:** Same window as `Concentric Peak Force`, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Concentric Peak Force` divided by Body Mass ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Peak Force / BM`.
- **Inputs:** Concentric Peak Force, body mass.
- **Units:** N/kg.
- **Variants:** `Concentric Peak Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Power`

This metric has these fields:

- **What it measures:** Average power during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average power throughout the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)`, `P = F * v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Concentric Mean Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Power / BM`

This metric has these fields:

- **What it measures:** Average upward-phase power relative to body mass.
- **Window or phase:** Same window as `Concentric Mean Power`, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Concentric Mean Power` divided by Body Mass ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Mean Power / BM`.
- **Inputs:** Concentric Mean Power, body mass.
- **Units:** W/kg.
- **Variants:** `Concentric Mean Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average upward speed during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the average velocity throughout the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean v(t)` over the concentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Peak Velocity`

This metric has these fields:

- **What it measures:** Highest upward speed before take-off.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest velocity reached in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max v(t)` over the concentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD`

This metric has these fields:

- **What it measures:** How fast force rises from the bottom of the dip to the concentric peak force.
- **Window or phase:** Start of the concentric phase (zero velocity, [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak concentric force, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD from the onset of the concentric phase to Peak Concentric Force, with a value of 0 reported when the slope of Total Vertical Force points downward ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_conPeak - F(t_ZV)) / (t_conPeak - t_ZV)`; reported as 0 when force falls over the window.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Concentric RFD / BM`. An asymmetry variant is listed as commonly used for the SJ ([User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Comparison with standard methods or other vendors:** VALD notes concentric RFD is often recorded as zero in CMJ and rebound jumps and suggests the SJ for concentric RFD ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development).

#### `Concentric RFD / BM`

This metric has these fields:

- **What it measures:** Concentric RFD relative to body mass.
- **Window or phase:** Same window as `Concentric RFD`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of the concentric phase (zero velocity, [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak concentric force, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Concentric RFD` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RFD / BM`.
- **Inputs:** Concentric RFD, body mass.
- **Units:** N/s/kg.
- **Variants:** `Concentric RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD - 50ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the RFD across the opening 50ms in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_ZV + 0.05 s) - F(t_ZV)) / 0.05 s`, using the glossary RFD definition 'change in force over a given time period' ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD - 100ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the RFD across the opening 100ms in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_ZV + 0.1 s) - F(t_ZV)) / 0.1 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD - 200ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 200 ms of the upward phase.
- **Window or phase:** First 200 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD across the opening 200ms in the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_ZV + 0.2 s) - F(t_ZV)) / 0.2 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Maximum RFD`

This metric has these fields:

- **What it measures:** The steepest 50 ms rise in force during the upward phase.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the peak RFD measured over a window of 50ms within the concentric phase ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max over t of (F(t + 0.05 s) - F(t)) / 0.05 s` within the concentric phase. Whether VALD uses a sliding window and how it handles the phase edge is not published. The knowledge base marks 'Start of max RFD' as the point of steepest concentric force and 'End of max RFD' at peak take-off force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump).

#### `Concentric RPD`

This metric has these fields:

- **What it measures:** How fast power rises from the bottom of the dip to peak power.
- **Window or phase:** Start of the concentric phase (zero velocity, [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak power, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the RPD running from the onset of the concentric phase until the moment Peak Power occurs ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P_peak - P(t_ZV)) / (t_PP - t_ZV)`, using the glossary RPD definition 'change in power over a given time period' ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD / BM`

This metric has these fields:

- **What it measures:** Concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of the concentric phase (zero velocity, [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak power, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RPD` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD / BM`.
- **Inputs:** Concentric RPD, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD - 50ms`

This metric has these fields:

- **What it measures:** Rise in power over the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the RPD across the opening 50ms in the concentric phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P(t_ZV + 0.05 s) - P(t_ZV)) / 0.05 s`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD-50ms / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD - 100ms`

This metric has these fields:

- **What it measures:** Rise in power over the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the RPD across the opening 100ms in the concentric phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P(t_ZV + 0.1 s) - P(t_ZV)) / 0.1 s`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD-100ms / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD-50ms / BM`

This metric has these fields:

- **What it measures:** 50 ms concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD - 50ms`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): First 50 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Concentric RPD-50ms` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD - 50ms / BM`.
- **Inputs:** Concentric RPD - 50ms, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD - 50ms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD-100ms / BM`

This metric has these fields:

- **What it measures:** 100 ms concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD - 100ms`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): First 100 ms of the concentric phase, which starts at zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RPD-100ms` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD - 100ms / BM`.
- **Inputs:** Concentric RPD - 100ms, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD - 100ms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Time to Peak Force`

This metric has these fields:

- **What it measures:** Time from the bottom of the dip to the concentric peak force.
- **Window or phase:** Start of the concentric phase (zero velocity, [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak force, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the time that passes from the onset of the concentric phase until Peak Force occurs ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_conPeak - t_ZV`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** ms.
- **Variants:** A Windows release fixed `Concentric Time to Peak Force Asymmetry (Left/Right)` not appearing ([ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes).

#### `Eccentric Duration`

This metric has these fields:

- **What it measures:** Length of the downward phase.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as how long the eccentric phase lasts ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_ZV - t_SoM`.
- **Inputs:** Start of movement and zero velocity events.
- **Units:** ms.
- **Variants:** The Hop and Return test reports it in s in one knowledge base table ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** The User Guide describes it as the length of time spent in the eccentric phase, which matches the glossary ([User Guide p.15](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [User Guide p.15](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Eccentric:Concentric Duration`

This metric has these fields:

- **What it measures:** Downward-phase time compared with upward-phase time.
- **Window or phase:** Combines `Eccentric Duration` and `Concentric Duration`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Eccentric Duration` compared with `Concentric Duration` as a ratio ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Duration / Concentric Duration`, shown as a percentage. Whether VALD multiplies by 100 is not published.
- **Inputs:** Eccentric Duration, Concentric Duration.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Contraction Time:Eccentric Duration`

This metric has these fields:

- **What it measures:** Contraction time compared with the length of the downward phase.
- **Window or phase:** Combines `Contraction Time` and `Eccentric Duration`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD says it is `Contraction Time` compared with `Eccentric Duration` as a ratio ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Contraction Time / Eccentric Duration`, shown as a percentage. Scaling is not published.
- **Inputs:** Contraction Time, Eccentric Duration.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Force`

This metric has these fields:

- **What it measures:** Average force during the downward phase.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the average vertical force throughout the eccentric phase, which equals Body Weight (N) ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)` over the eccentric phase. Restatement of why it equals body weight: velocity is zero at both ends of the phase, so net impulse over the phase is zero.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant listed as commonly used for the SQT ([User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.44](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Eccentric:Concentric Mean Force Ratio`

This metric has these fields:

- **What it measures:** Average downward-phase force compared with average upward-phase force.
- **Window or phase:** Combines `Eccentric Mean Force` and `Concentric Mean Force`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Eccentric Mean Force` compared with `Concentric Mean Force` as a ratio ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Mean Force / Concentric Mean Force`, shown as a percentage. Scaling is not published.
- **Inputs:** Eccentric Mean Force, Concentric Mean Force.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Force`

This metric has these fields:

- **What it measures:** Highest force during the downward phase.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force reached in the eccentric phase ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` over the eccentric phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Eccentric Peak Force / BM` (N/kg).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Force / BM`

This metric has these fields:

- **What it measures:** Downward-phase peak force relative to body mass.
- **Window or phase:** Same window as `Eccentric Peak Force`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Eccentric Peak Force` divided by Body Mass ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Peak Force / BM`.
- **Inputs:** Eccentric Peak Force, body mass.
- **Units:** N/kg.
- **Variants:** `Eccentric Peak Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Minimum Eccentric Force`

This metric has these fields:

- **What it measures:** The lowest force while unweighting at the start of the dip.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the lowest vertical force reached in the eccentric phase ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `min F(t)` over the eccentric phase. This point also starts the braking phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Velocity`

This metric has these fields:

- **What it measures:** The fastest downward speed during the dip.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest velocity reached in the eccentric phase ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `min v(t)` over the eccentric phase (the largest negative value). VALD's EPV article says a search for the "maximum" returns the slowest EPV, and adds that the way to find EPV is to search for the minimum ([The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1))
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** Glossary unit is printed as 'Millisecond (m/s)', a typo; the value is in m/s ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Default CMJ metric since 2026 ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** Also called peak negative velocity or peak braking velocity elsewhere ([The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Eccentric Mean Power`

This metric has these fields:

- **What it measures:** Average power during the downward phase.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average power throughout the eccentric phase ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)` over the eccentric phase, `P = F * v`. The sign convention for this phase is not published.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Eccentric Mean Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Power / BM`

This metric has these fields:

- **What it measures:** Average downward-phase power relative to body mass.
- **Window or phase:** Same window as `Eccentric Mean Power`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Eccentric Mean Power` divided by Body Mass ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Mean Power / BM`.
- **Inputs:** Eccentric Mean Power, body mass.
- **Units:** W/kg.
- **Variants:** `Eccentric Mean Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Power`

This metric has these fields:

- **What it measures:** Highest power during the downward phase.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest power reached in the eccentric phase ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max |P(t)|` or `min P(t)` over the eccentric phase; VALD does not publish which sign it reports.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Eccentric Peak Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Power / BM`

This metric has these fields:

- **What it measures:** Downward-phase peak power relative to body mass.
- **Window or phase:** Same window as `Eccentric Peak Power`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Eccentric Peak Power` divided by Body Mass ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Peak Power / BM`.
- **Inputs:** Eccentric Peak Power, body mass.
- **Units:** W/kg.
- **Variants:** `Eccentric Peak Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Peak Power:Concentric Peak Power`

This metric has these fields:

- **What it measures:** Downward peak power compared with upward peak power.
- **Window or phase:** Combines `Eccentric Peak Power` and Concentric Peak Power, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Eccentric Peak Power` compared with `Concentric Peak Power` as a ratio ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Peak Power / Peak Power`.
- **Inputs:** Eccentric Peak Power, Peak Power.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Acceleration Phase Duration`

This metric has these fields:

- **What it measures:** Time from first movement to the fastest downward speed.
- **Window or phase:** Eccentric acceleration phase: start of movement to maximum negative velocity. The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is how long the eccentric acceleration phase lasts, which begins at Start of Movement and ends when the maximum negative velocity is reached ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_EPV - t_SoM`.
- **Inputs:** Start of movement, eccentric peak velocity.
- **Units:** s.
- **Variants:** `Eccentric Acceleration Phase:Contraction Time Ratio`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Unloading Impulse`

This metric has these fields:

- **What it measures:** Net impulse while the athlete drops before braking begins.
- **Window or phase:** Start of movement to the start of the eccentric deceleration phase, as the metric's definition states. The knowledge base defines the unloading sub-phase as start of movement to minimum force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)). The two windows differ. The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the net impulse across the eccentric unloading phase, which spans the time from Start of Movement until the eccentric deceleration phase begins ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Not published. VALD defines this metric as net impulse in this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)), and defines net impulse as the area "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). In this window force is below body weight, because the athlete is still speeding up downward (User Guide relation `a = (F – BW) ÷ m`, [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf); restatement). VALD does not publish how it computes or signs this metric.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Time to Braking Phase`

This metric has these fields:

- **What it measures:** Time from first movement to the start of braking (minimum force).
- **Window or phase:** Start of movement to the start of the eccentric braking phase (minimum eccentric force) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the time from Start of Movement until the eccentric braking phase begins ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_minF - t_SoM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Braking Phase Duration`

This metric has these fields:

- **What it measures:** Length of the braking phase.
- **Window or phase:** Eccentric braking phase: minimum force in the eccentric phase to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as how long the eccentric braking phase lasts ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_ZV - t_minF`.
- **Inputs:** Minimum eccentric force and zero velocity events.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Braking Phase Duration:Concentric Duration`

This metric has these fields:

- **What it measures:** Braking time compared with upward-phase time.
- **Window or phase:** Combines `Braking Phase Duration` and Concentric Phase Duration, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD says it is `Braking Phase Duration` compared with `Concentric Phase Duration` as a ratio ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Braking Phase Duration / Concentric Duration`.
- **Inputs:** Braking Phase Duration, Concentric Duration.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Braking Phase Duration:Contraction Time`

This metric has these fields:

- **What it measures:** Braking time as a share of contraction time.
- **Window or phase:** Combines `Braking Phase Duration` and `Contraction Time`, as the definition states ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Braking Phase Duration` compared with `Contraction Time` as a ratio ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Braking Phase Duration / Contraction Time`.
- **Inputs:** Braking Phase Duration, Contraction Time.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Braking Impulse`

This metric has these fields:

- **What it measures:** Net impulse during braking, from minimum force to the bottom of the dip.
- **Window or phase:** Eccentric braking phase: minimum force in the eccentric phase to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the net impulse across the eccentric braking phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_minF to t_ZV] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). From minimum force to eccentric peak velocity, force is below body weight (restatement); VALD's sign convention for this metric is not published.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Braking RFD`

This metric has these fields:

- **What it measures:** How fast force rises across the whole braking phase.
- **Window or phase:** Eccentric braking phase: minimum force in the eccentric phase to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD measured across the whole eccentric braking phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_ZV) - F(t_minF)) / (t_ZV - t_minF)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Eccentric Braking RFD / BM`.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Braking RFD / BM`

This metric has these fields:

- **What it measures:** Braking RFD relative to body mass.
- **Window or phase:** Same window as `Eccentric Braking RFD`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric braking phase: minimum force in the eccentric phase to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Eccentric Braking RFD` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Braking RFD / BM`.
- **Inputs:** Eccentric Braking RFD, body mass.
- **Units:** N/s/kg.
- **Variants:** `Eccentric Braking RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Braking RFD-100ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 100 ms of braking.
- **Window or phase:** First 100 ms of the eccentric braking phase, which starts at minimum eccentric force ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the RFD across the opening 100ms in the eccentric braking phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_minF + 0.1 s) - F(t_minF)) / 0.1 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Eccentric Braking RFD-100ms / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Braking RFD-100ms / BM`

This metric has these fields:

- **What it measures:** 100 ms braking RFD relative to body mass.
- **Window or phase:** Same window as `Eccentric Braking RFD-100ms`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): First 100 ms of the eccentric braking phase, which starts at minimum eccentric force ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Eccentric Braking RFD-100ms` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Braking RFD-100ms / BM`.
- **Inputs:** Eccentric Braking RFD-100ms, body mass.
- **Units:** N/s/kg.
- **Variants:** `Eccentric Braking RFD-100ms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Braking Force`

This metric has these fields:

- **What it measures:** Average force during braking.
- **Window or phase:** Eccentric braking phase: minimum force in the eccentric phase to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average vertical force throughout the eccentric braking phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)` from minimum force to zero velocity.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Deceleration Phase Duration`

This metric has these fields:

- **What it measures:** Length of the deceleration phase.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is how long the eccentric deceleration phase lasts ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_ZV - t_EPV`.
- **Inputs:** Eccentric peak velocity and zero velocity events.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Deceleration Impulse`

This metric has these fields:

- **What it measures:** Net impulse used to stop the downward movement.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the net impulse across the eccentric deceleration phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_EPV to t_ZV] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** `Eccentric Deceleration Impulse / BM`; `Eccentric Deceleration Impulse – Asymmetry` is a 2026 default CMJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Deceleration Impulse / BM`

This metric has these fields:

- **What it measures:** Deceleration impulse relative to body mass.
- **Window or phase:** Same window as `Eccentric Deceleration Impulse`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Eccentric Deceleration Impulse` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Deceleration Impulse / BM`.
- **Inputs:** Eccentric Deceleration Impulse, body mass.
- **Units:** N s/kg.
- **Variants:** Added as a new metric in a release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration RFD`

This metric has these fields:

- **What it measures:** How fast force rises while stopping the downward movement.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD measured across the whole eccentric deceleration phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_ZV) - F(t_EPV)) / (t_ZV - t_EPV)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Eccentric Deceleration RFD / BM`; asymmetry variant listed as commonly used ([User Guide p.15](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.15](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Deceleration RFD / BM`

This metric has these fields:

- **What it measures:** Deceleration RFD relative to body mass.
- **Window or phase:** Same window as `Eccentric Deceleration RFD`, as the definition states ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Eccentric Deceleration RFD` divided by Body Mass ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Deceleration RFD / BM`.
- **Inputs:** Eccentric Deceleration RFD, body mass.
- **Units:** N/s/kg.
- **Variants:** `Eccentric Deceleration RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise; slow descent (low eccentric peak velocity) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Deceleration Force`

This metric has these fields:

- **What it measures:** Average force while stopping the downward movement.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the average vertical force throughout the eccentric deceleration phase ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)` from eccentric peak velocity to zero velocity.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Force at Zero Velocity`

This metric has these fields:

- **What it measures:** Force at the bottom of the dip.
- **Window or phase:** Single point: zero velocity before take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the vertical force measured when velocity reaches zero before Take-off ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `F(t_ZV)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Force at Zero Velocity / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Force at Zero Velocity / BM`

This metric has these fields:

- **What it measures:** Force at the bottom of the dip relative to body mass.
- **Window or phase:** Same window as `Force at Zero Velocity`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Single point: zero velocity before take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Force at Zero Velocity` divided by Body Mass ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Force at Zero Velocity / BM`.
- **Inputs:** Force at Zero Velocity, body mass.
- **Units:** N/kg.
- **Variants:** `Force at Zero Velocity`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `CMJ Stiffness`

This metric has these fields:

- **What it measures:** Peak upward-phase force divided by dip depth.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest vertical force reached in the concentric phase, divided by the displacement where the concentric phase begins, which is the minimum displacement ([Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Peak Force / |s(t_ZV)|`. Sign handling is not published.
- **Inputs:** Concentric Peak Force, displacement at zero velocity.
- **Units:** N/m.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** The User Guide defines stiffness generally as peak force / displacement ([User Guide p.103](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.5](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.103](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Lower-Limb Stiffness`

This metric has these fields:

- **What it measures:** Change in force across the downward phase divided by dip depth.
- **Window or phase:** Eccentric phase: start of movement to zero velocity (minimum displacement) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the change in vertical force over the eccentric phase, divided by `Countermovement Depth` ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `ΔF_ecc / |Countermovement Depth|`. VALD does not publish which force values define the change.
- **Inputs:** Total vertical force, Countermovement Depth.
- **Units:** N/m.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Mean Eccentric+Concentric Power:Time`

This metric has these fields:

- **What it measures:** Average power from first movement to take-off, divided by contraction time.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the mean power from Start of Movement to Take-off, divided by Contraction Time ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)[t_SoM to t_TO] / CT`.
- **Inputs:** Power, Contraction Time.
- **Units:** W/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Total Work`

This metric has these fields:

- **What it measures:** Area under the power curve from first movement to take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the integral of power over time, meaning the region beneath the power-time curve, taken from Start of Movement to Take-off ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_TO] P(t) dt`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** J.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Positive Take-off Impulse`

This metric has these fields:

- **What it measures:** Net impulse from first movement to take-off.
- **Window or phase:** Eccentric and concentric phases combined, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): start of movement to take-off ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across Take-off, adding the eccentric and concentric phases together ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary positive impulse definition: area from the start of movement to take-off "but only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Positive Impulse`

This metric has these fields:

- **What it measures:** Net impulse over the whole rep.
- **Window or phase:** Entire repetition. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across the whole repetition, summing the eccentric, concentric, and landing phases ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Per the CMJ table: `∫ max(F - BW, 0) dt` over the whole rep, restating the glossary net impulse definition (area "only above body weight"). The technical-definitions table instead defines it as the area under the curve from the start of movement to take-off, counting only force above body weight ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). VALD does not resolve the difference.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Force`

This metric has these fields:

- **What it measures:** Highest force after landing.
- **Window or phase:** After landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force that occurs after Landing ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` after landing.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Landing Force / BM`; `Peak Landing Force – Asymmetry` is a 2026 default CMJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Landing Force / BM`

This metric has these fields:

- **What it measures:** Peak landing force relative to body mass.
- **Window or phase:** Same window as `Peak Landing Force`, as the definition states ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): After landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Peak Landing Force` divided by Body Mass ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Landing Force / BM`.
- **Inputs:** Peak Landing Force, body mass.
- **Units:** N/kg.
- **Variants:** `Peak Landing Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing Net Peak Force / BM`

This metric has these fields:

- **What it measures:** Peak landing force above body weight, relative to body mass.
- **Window or phase:** After landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force after Landing, with Body Weight subtracted, and the result divided by Body Mass ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(max F - BW) / BM` after landing.
- **Inputs:** Peak Landing Force, body weight, body mass.
- **Units:** N/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing Impulse`

This metric has these fields:

- **What it measures:** Total impulse from landing to peak landing force.
- **Window or phase:** Landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak landing force. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the absolute impulse from Landing up to the moment `Peak Landing Force` happens ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_L to t_PLF] F dt`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing RFD`

This metric has these fields:

- **What it measures:** How fast force rises from landing to peak landing force.
- **Window or phase:** Landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak landing force. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as RFD measured from Landing up to the moment `Peak Landing Force` happens ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_PLF - F(t_L)) / (t_PLF - t_L)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Jump Height (FT) Relative Landing RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing RFD 50ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 50 ms after landing.
- **Window or phase:** First 50 ms after landing ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the first 50ms after Landing ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_L + 0.05 s) - F(t_L)) / 0.05 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (FT) Relative Landing RFD`

This metric has these fields:

- **What it measures:** Landing RFD per centimetre of jump height.
- **Window or phase:** Combines `Landing RFD` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Landing RFD` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Landing RFD / JH_FT[cm]`.
- **Inputs:** Landing RFD, Jump Height (Flight Time).
- **Units:** N/s/cm.
- **Variants:** API identifier `JUMP_HEIGHT_RELATIVE_LANDING_RFD`, group `Landing`, unit `NewtonPerSecondPerCentimeter` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Jump Height (FT) Relative Peak Landing Force`

This metric has these fields:

- **What it measures:** Peak landing force per centimetre of jump height.
- **Window or phase:** Combines `Peak Landing Force` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Peak Landing Force` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Landing Force / JH_FT[cm]`.
- **Inputs:** Peak Landing Force, Jump Height (Flight Time).
- **Units:** N/cm.
- **Variants:** API identifier `JUMP_HEIGHT_RELATIVE_PEAK_LANDING_FORCE`, group `Landing`, unit `NewtonPerCentimeter` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Mean Landing Power`

This metric has these fields:

- **What it measures:** Average power from landing to the end of the rep.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average power from Landing until the rep ends ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)` over the landing phase.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Power`

This metric has these fields:

- **What it measures:** Highest power from landing to the end of the rep.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the maximum power from Landing until the rep ends ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max P(t)` over the landing phase; sign convention not published.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Acceleration`

This metric has these fields:

- **What it measures:** Highest acceleration of the centre of mass after landing.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest acceleration reached by the centre of mass from Landing until the rep ends ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max a(t)` over the landing phase.
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Velocity`

This metric has these fields:

- **What it measures:** Peak centre-of-mass velocity after landing.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest velocity reached by the centre of mass from Landing until the rep ends ([Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Extreme of `v(t)` over the landing phase; whether VALD reports the largest negative value is not published.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.9](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Deceleration Peak Force`

This metric has these fields:

- **What it measures:** Highest force while stopping the downward movement.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the highest vertical force reached within the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `max F(t)` from eccentric peak velocity to zero velocity.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** `Eccentric Deceleration Peak Force / BW`.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Deceleration Peak Force / BW`

This metric has these fields:

- **What it measures:** Deceleration peak force normalised to body weight.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the highest vertical force in the eccentric deceleration phase, normalized against body weight ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: Peak deceleration force divided by body weight; whether VALD divides by weight (N) or mass (kg) is not published.
- **Inputs:** Eccentric Deceleration Peak Force, body weight.
- **Units:** Not published.
- **Variants:** `Eccentric Deceleration Peak Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power`

This metric has these fields:

- **What it measures:** Average power while stopping the downward movement.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD says it is the average mechanical power, found as force times velocity, in the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t) * v(t)` over the deceleration phase.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** Not published.
- **Variants:** `Eccentric Deceleration Mean Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Power / BM`

This metric has these fields:

- **What it measures:** Deceleration mean power relative to body mass.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the average power in eccentric deceleration, normalized against body mass ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `Eccentric Deceleration Mean Power / BM`.
- **Inputs:** Eccentric Deceleration Mean Power, body mass.
- **Units:** Not published.
- **Variants:** `Eccentric Deceleration Mean Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration Mean Velocity`

This metric has these fields:

- **What it measures:** Average downward speed while decelerating.
- **Window or phase:** Eccentric deceleration phase: maximum negative velocity (the moment before positive acceleration) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the average vertical velocity of the center of mass in the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean v(t)` over the deceleration phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Concentric Impulse:Eccentric Deceleration Impulse Ratio`

This metric has these fields:

- **What it measures:** Upward net impulse compared with deceleration net impulse.
- **Window or phase:** Combines net concentric impulse and net eccentric deceleration impulse, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD defines it as net concentric impulse compared with net eccentric deceleration impulse, as a ratio ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `Concentric Impulse / Eccentric Deceleration Impulse`.
- **Inputs:** Concentric Impulse, Eccentric Deceleration Impulse.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Concentric Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of contraction time spent pushing up.
- **Window or phase:** Combines the duration of the concentric phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the concentric phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * Concentric Duration / Contraction Time`.
- **Inputs:** Concentric Duration, Contraction Time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Deceleration:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of contraction time spent decelerating.
- **Window or phase:** Combines the duration of the eccentric deceleration phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the eccentric deceleration phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * Eccentric Deceleration Phase Duration / Contraction Time`.
- **Inputs:** Eccentric Deceleration Phase Duration, Contraction Time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Unloading Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of contraction time spent unloading.
- **Window or phase:** Combines the duration of the eccentric unloading phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the eccentric unloading phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * unloading duration / Contraction Time`. VALD changed how the unloading phase is detected in a 2025 release ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Inputs:** Unloading phase duration, Contraction Time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Yielding Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of contraction time spent in the yielding phase.
- **Window or phase:** Combines the duration of the eccentric yielding phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the eccentric yielding phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * yielding duration / Contraction Time`.
- **Inputs:** Yielding phase duration, Contraction Time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** Phase names differ across the field. ForceDecks calls the window from eccentric peak velocity to zero velocity the deceleration phase; other sources call it the braking phase. The ForceDecks braking phase (minimum force to zero velocity) contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1).

#### `Eccentric Acceleration Phase:Contraction Time Ratio`

This metric has these fields:

- **What it measures:** Share of contraction time spent accelerating downward.
- **Window or phase:** Combines the duration of the eccentric acceleration phase with contraction time, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Each term uses its own window.
- **Calculation:** VALD describes it as the share of total contraction time, as a percentage, taken up by the eccentric acceleration phase, which merges the eccentric unloading phase with the eccentric yielding phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `100 * Eccentric Acceleration Phase Duration / Contraction Time`.
- **Inputs:** Eccentric Acceleration Phase Duration, Contraction Time.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Eccentric Yielding Phase RFD`

This metric has these fields:

- **What it measures:** Rate of force rise during the yielding phase.
- **Window or phase:** Not published. The name refers to the eccentric yielding phase, which VALD defines as minimum force to eccentric peak velocity ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)); VALD publishes no definition for this metric.
- **Calculation:** VALD's definition: Not published. Formula: Not published.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** `Eccentric Yielding Phase RFD / BM`. Named in release notes that fixed its calculation; no definition published ([ForceDecks iOS v3.4.0 Release Notes, 2026-07-27](https://support.vald.com/hc/en-au/articles/60292611662361-ForceDecks-iOS-v3-4-0-Release-Notes-27-July-2026)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [ForceDecks iOS v3.4.0 Release Notes, 2026-07-27](https://support.vald.com/hc/en-au/articles/60292611662361-ForceDecks-iOS-v3-4-0-Release-Notes-27-July-2026).

#### `Eccentric Yielding Phase RFD / BM`

This metric has these fields:

- **What it measures:** Yielding-phase RFD relative to body mass.
- **Window or phase:** Not published. The name refers to the eccentric yielding phase, which VALD defines as minimum force to eccentric peak velocity ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)); VALD publishes no definition for this metric.
- **Calculation:** VALD's definition: Not published. Formula: Not published.
- **Inputs:** Eccentric Yielding Phase RFD, body mass.
- **Units:** Not published.
- **Variants:** Named in release notes; no definition published ([ForceDecks iOS v3.4.0 Release Notes, 2026-07-27](https://support.vald.com/hc/en-au/articles/60292611662361-ForceDecks-iOS-v3-4-0-Release-Notes-27-July-2026)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [ForceDecks iOS v3.4.0 Release Notes, 2026-07-27](https://support.vald.com/hc/en-au/articles/60292611662361-ForceDecks-iOS-v3-4-0-Release-Notes-27-July-2026).

#### `Landing Stiffness`

This metric has these fields:

- **What it measures:** Landing force divided by how far the centre of mass sinks on landing.
- **Window or phase:** Single point: maximum negative displacement during landing, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The end of the landing window is not published.
- **Calculation:** VALD defines it as force divided by the displacement of the center of mass, taken at the point where displacement reaches its maximum negative value during landing ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `F(t_minS) / |s(t_minS)|` at the lowest landing point. Which displacement reference VALD uses is not published.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Mean Landing Force`

This metric has these fields:

- **What it measures:** Average force during the landing phase.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD defines it as the average vertical force across the landing phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t)` over the landing phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

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

#### `Athlete Standing Weight`

This metric has these fields:

- **What it measures:** Weight estimated before each rep when the weighing step was skipped.
- **Window or phase:** The still period before each rep, used when the weighing step was skipped ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Calculation:** VALD says that when the weighing step is skipped, the weight is estimated before each rep and saved in the `Athlete Standing Weight` metric ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)). Formula: Not published.
- **Inputs:** Still period before each rep.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)). Auto-weight settings: minimum weight, maximum standard deviation, steady period and maximum weight deviation ([Manage ForceDecks iOS app settings](https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings), [Weight Settings in ForceDecks Jump](https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump)).
- **Sources:** [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API), [Manage ForceDecks iOS app settings](https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings), [Weight Settings in ForceDecks Jump](https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump).

See [the calculations overview](../../calculations.md) for how these metrics relate to the methods in the skills.
