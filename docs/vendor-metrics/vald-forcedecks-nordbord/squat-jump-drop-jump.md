# VALD ForceDecks and NordBord metrics: squat jump and drop jump

This page explains how VALD ForceDecks calculates each metric for these tests. It covers the squat jump (SJ, LSJ) and the drop jump (DJ, SLDJ), with 128 metric blocks. Checked against: the VALD ForceDecks Technical Glossary V2.0 (March 2024), the VALD ForceDecks User Guide v2 (November 2023), the External ForceDecks API specification (`v2019q3`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

This page is part of [VALD ForceDecks and NordBord metrics](README.md). The index explains how to read each block, and it holds the event and term glossary, the factors that change the numbers, the conflicts in VALD's own sources, the Not published list, the worked example, and the sources with access dates. VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](../vald-other-products/README.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](../hawkin-dynamics/README.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](../hawkin-dynamics/README.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Metric blocks

### Squat jump (SJ, LSJ)

The SJ starts from a paused partial squat with no downward movement ([ForceDecks Test Protocol - Squat Jump](https://support.vald.com/hc/en-au/articles/7081508615321-ForceDecks-Test-Protocol-Squat-Jump)). The glossary defines one SJ phase before take-off: the concentric phase runs from start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide instead says 'zero velocity until take-off' ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

VALD-stated count: 71 SJ metrics ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The glossary lists 64 SJ metric names.

2026 SJ and LSJ defaults: `Jump Height (Imp-Mom)`, `RSI-modified`, `Concentric Impulse – Asymmetry`, `Contraction Time`, `Peak Power / BM` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).

The SJ blocks reuse the CMJ definitions when the SJ glossary text is identical. Where the text differs, the SJ wording is used. Formula restatements replace zero velocity with start of movement as the start of the concentric phase.

#### `Concentric Impulse`

This metric has these fields:

- **What it measures:** Net push above body weight during the upward phase.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** `Concentric Impulse – Asymmetry` is a 2026 default SJ and LSJ metric, and also a CMJ default ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). VALD describes the asymmetry as the percent difference in left and right net impulse ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks).

#### `Concentric Impulse (Abs) / BM`

This metric has these fields:

- **What it measures:** Total (not net) upward-phase impulse relative to body mass.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the absolute impulse in the concentric phase, divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_TO] F dt / BM`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s/kg.
- **Variants:** A release fixed its display unit from N s to N s/kg ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Concentric Impulse-100ms`

This metric has these fields:

- **What it measures:** Net impulse in the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse over the opening 100ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_SoM+0.1 s] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse-100ms:Concentric Impulse`

This metric has these fields:

- **What it measures:** Share of the upward net impulse produced in the first 100 ms.
- **Window or phase:** Combines `Concentric Impulse-100ms` and `Concentric Impulse`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Concentric Impulse-100ms` compared with `Concentric Impulse`, as a ratio ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Impulse-100ms / Concentric Impulse`.
- **Inputs:** Concentric Impulse-100ms, Concentric Impulse.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Impulse-50ms`

This metric has these fields:

- **What it measures:** Net impulse in the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse over the opening 50ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_SoM+0.05 s] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Maximum RFD`

This metric has these fields:

- **What it measures:** The steepest 50 ms rise in force during the upward phase.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the peak RFD measured across a 50ms window within the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max over t of (F(t + 0.05 s) - F(t)) / 0.05 s` within the concentric phase. Whether VALD uses a sliding window and how it handles the phase edge is not published. The knowledge base marks 'Start of max RFD' as the point of steepest concentric force and 'End of max RFD' at peak take-off force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump).

#### `Concentric Mean Force`

This metric has these fields:

- **What it measures:** Average total force during the upward phase.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average vertical force over the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)` over the concentric phase. The glossary 'Mean' includes the start and end samples ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Concentric Mean Force / BM` (N/kg).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Force / BM`

This metric has these fields:

- **What it measures:** Average upward-phase force relative to body mass.
- **Window or phase:** Same window as `Concentric Mean Force`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric Mean Force` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Mean Force / BM`.
- **Inputs:** Concentric Mean Force, body mass.
- **Units:** N/kg.
- **Variants:** `Concentric Mean Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Mean Power`

This metric has these fields:

- **What it measures:** Average power during the upward phase.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average power over the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)`, `P = F * v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Concentric Mean Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Power / BM`

This metric has these fields:

- **What it measures:** Average upward-phase power relative to body mass.
- **Window or phase:** Same window as `Concentric Mean Power`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric Mean Power` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Mean Power / BM`.
- **Inputs:** Concentric Mean Power, body mass.
- **Units:** W/kg.
- **Variants:** `Concentric Mean Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average upward speed during the upward phase.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average velocity across the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean v(t)` over the concentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Peak Velocity`

This metric has these fields:

- **What it measures:** Highest upward speed before take-off.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the maximum velocity reached in the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max v(t)` over the concentric phase.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD`

This metric has these fields:

- **What it measures:** How fast force rises from the bottom of the dip to the concentric peak force.
- **Window or phase:** Start of the concentric phase (start of movement for the SJ, [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak force, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the span that begins when the concentric phase starts and ends when Peak Force occurs ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_peak - F(t_SoM)) / (t_Fpeak - t_SoM)`. Unlike the CMJ entry, the SJ glossary text does not mention reporting 0 for a downward slope.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Concentric RFD / BM`. An asymmetry variant is listed as commonly used for the SJ ([User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Comparison with standard methods or other vendors:** VALD recommends the SJ for concentric RFD because the CMJ value is often zero ([Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Understanding Rate of Force Development](https://valdhealth.com/news/understanding-rate-of-force-development).

#### `Concentric RFD - 100ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the opening 100ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_SoM + 0.1 s) - F(t_SoM)) / 0.1 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD - 200ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 200 ms of the upward phase.
- **Window or phase:** First 200 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the opening 200ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_SoM + 0.2 s) - F(t_SoM)) / 0.2 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD - 50ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the opening 50ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_SoM + 0.05 s) - F(t_SoM)) / 0.05 s`, using the glossary RFD definition 'change in force over a given time period' ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RFD / BM`

This metric has these fields:

- **What it measures:** Concentric RFD relative to body mass.
- **Window or phase:** Same window as `Concentric RFD`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of the concentric phase (start of movement for the SJ, [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak force, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RFD` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RFD / BM`.
- **Inputs:** Concentric RFD, body mass.
- **Units:** N/s/kg.
- **Variants:** `Concentric RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD`

This metric has these fields:

- **What it measures:** How fast power rises from the bottom of the dip to peak power.
- **Window or phase:** Start of the concentric phase (start of movement for the SJ, [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak power, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RPD over the span that begins when the concentric phase starts and ends when Peak Power occurs ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P_peak - P(t_SoM)) / (t_PP - t_SoM)`, using the glossary RPD definition 'change in power over a given time period' ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353))
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD - 100ms`

This metric has these fields:

- **What it measures:** Rise in power over the first 100 ms of the upward phase.
- **Window or phase:** First 100 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RPD over the opening 100ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P(t_SoM + 0.1 s) - P(t_SoM)) / 0.1 s`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD-100ms / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD - 50ms`

This metric has these fields:

- **What it measures:** Rise in power over the first 50 ms of the upward phase.
- **Window or phase:** First 50 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RPD over the opening 50ms of the concentric phase ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(P(t_SoM + 0.05 s) - P(t_SoM)) / 0.05 s`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W/s.
- **Variants:** `Concentric RPD-50ms / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD / BM`

This metric has these fields:

- **What it measures:** Concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of the concentric phase (start of movement for the SJ, [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak power, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RPD` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD / BM`.
- **Inputs:** Concentric RPD, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD-100ms / BM`

This metric has these fields:

- **What it measures:** 100 ms concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD - 100ms`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): First 100 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RPD-100ms` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD - 100ms / BM`.
- **Inputs:** Concentric RPD - 100ms, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD - 100ms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric RPD-50ms / BM`

This metric has these fields:

- **What it measures:** 50 ms concentric RPD relative to body mass.
- **Window or phase:** Same window as `Concentric RPD - 50ms`, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): First 50 ms of the concentric phase, which for the SJ starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Concentric RPD-50ms` divided by Body Mass ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric RPD - 50ms / BM`.
- **Inputs:** Concentric RPD - 50ms, body mass.
- **Units:** W/s/kg.
- **Variants:** `Concentric RPD - 50ms`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of integration setting; body weight accuracy; detection of the event that starts the fixed window; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Time to Peak Force`

This metric has these fields:

- **What it measures:** Time from the bottom of the dip to the concentric peak force.
- **Window or phase:** Start of the concentric phase (start of movement for the SJ, [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak force, as the definition states ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time span from when the concentric phase starts until Peak Force occurs ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_conPeak - t_SoM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** ms.
- **Variants:** A Windows release fixed `Concentric Time to Peak Force Asymmetry (Left/Right)` not appearing ([ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes).

#### `Contraction Time`

This metric has these fields:

- **What it measures:** Time from the first movement to leaving the ground.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time span running from Start of Movement until Take-off ([Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `CT = t_TO - t_SoM`.
- **Inputs:** Start of movement and take-off events.
- **Units:** ms.
- **Variants:** Default SJ and LSJ metric; the default-metrics page lists the SJ contraction time in s ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** The User Guide glossary gives the same definition and notes it covers eccentric and concentric phases in a CMJ ([User Guide p.101](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)). A long pre-jump movement or a nearby impact before the jump increases contraction time ([Quick Data Quality Check in ForceDecks](https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks)).
- **Sources:** [Glossary V2.0 p.15](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.101](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Quick Data Quality Check in ForceDecks](https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks).

#### `Countermovement Depth`

This metric has these fields:

- **What it measures:** Any downward movement of the centre of mass after the start of the squat jump.
- **Window or phase:** Start of movement to the end of the eccentric phase (the bottom of the squat), as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The SJ movement phases list no eccentric phase ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the maximum displacement from Start of Movement until the eccentric phase ends, which is the bottom of the squat ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `min s(t)` between start of movement and the end of the eccentric phase.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** None published.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; cueing and intent ([factor details](README.md#factors-that-change-the-numbers)). A countermovement before the SJ push makes start-of-movement detection unreliable ([User Guide p.25](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.25](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Displacement at Take-off`

This metric has these fields:

- **What it measures:** How far the centre of mass has risen from standing height at the moment of take-off.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the displacement recorded when Take-off happens ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `s(t_TO)`, displacement relative to the start of integration.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Flight Time`

This metric has these fields:

- **What it measures:** Time in the air between take-off and landing.
- **Window or phase:** Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the elapsed time from Take-off to Landing ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `FT = t_L - t_TO`.
- **Inputs:** Take-off and landing events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Force at Peak Power`

This metric has these fields:

- **What it measures:** Force at the instant of peak power.
- **Window or phase:** Single point: the instant of peak power. The definition gives no search window for peak power ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). VALD defines SJ `Peak Power` as the maximum power during the concentric phase ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)), but `Velocity at Peak Power` searches between start of movement and take-off ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Which one this metric uses is not published.
- **Calculation:** VALD defines it as the vertical force present when Peak Power occurs ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `F(t_PP)`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** N.
- **Variants:** Asymmetry variant listed as commonly used for the SJ ([User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Movement Start to Peak Force`

This metric has these fields:

- **What it measures:** Time from first movement to peak force.
- **Window or phase:** Start of movement to the instant of peak vertical force before take-off, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time from Start of Movement to the peak vertical force that happens before Take-off ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_Fmax - t_SoM`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Movement Start to Peak Power`

This metric has these fields:

- **What it measures:** Time from first movement to peak power.
- **Window or phase:** Start of movement to the instant of peak power before take-off, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time from Start of Movement to the Peak Power that happens before Take-off ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_PP - t_SoM`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `P1 Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse in the first half (by time) of the upward phase.
- **Window or phase:** First half of the concentric phase, split by time. For the SJ the concentric phase starts at start of movement ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across the initial 50% of the concentric phase, measured in terms of time ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_mid] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). `t_mid = (t_SoM + t_TO) / 2`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** VALD maps concentric 'Phase 1' and 'Phase 2' to the first and second 50% of the upward phase ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)).
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks).

#### `P2 Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse in the second half (by time) of the upward phase.
- **Window or phase:** Second half of the concentric phase, split by time. For the SJ the concentric phase ends at take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse across the second 50% portion of the concentric phase, measured in terms of time ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_mid to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `P2 Concentric Impulse:P1 Concentric Impulse`

This metric has these fields:

- **What it measures:** How the upward push is split between the second and first halves.
- **Window or phase:** Combines `P2 Concentric Impulse` and `P1 Concentric Impulse`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `P2 Concentric Impulse` compared with `P1 Concentric Impulse`, as a ratio ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `P2 / P1`.
- **Inputs:** P1 and P2 Concentric Impulse.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Net Take-off Force / BM`

This metric has these fields:

- **What it measures:** Peak force above body weight, relative to body mass.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force from Start of Movement to Take-off, with Body Weight subtracted, and the result divided by Body Mass ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(max F - BW) / BM`.
- **Inputs:** Take-off Peak Force, body weight, body mass.
- **Units:** N/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body weight accuracy; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Power`

This metric has these fields:

- **What it measures:** The highest power produced while pushing up.
- **Window or phase:** Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the maximum power reached in the concentric phase ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max P(t)` over the concentric phase, where `P = F * v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Peak Power / BM`. The SJ default description says 'assuming zero starting velocity' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Power / BM`

This metric has these fields:

- **What it measures:** Peak power relative to body mass.
- **Window or phase:** Same window as `Peak Power`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase. Glossary: start of movement to take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide describes the SJ concentric phase as zero velocity to take-off ([User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Peak Power` divided by Body Mass ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Power / BM`.
- **Inputs:** Peak Power, body mass.
- **Units:** W/kg.
- **Variants:** `Peak Power`. Default SJ and LSJ metric, described as 'assuming zero starting velocity' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Peak Take-off Acceleration`

This metric has these fields:

- **What it measures:** The highest upward acceleration of the centre of mass before take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest acceleration reached by the centre of mass from Start of Movement to Take-off ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max a(t)` with `a = (F - BW) / BM` ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Positive Impulse`

This metric has these fields:

- **What it measures:** Net impulse over the whole rep.
- **Window or phase:** Entire repetition, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition does not list the phases.
- **Calculation:** VALD defines it as the net impulse over the full repetition ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[whole rep] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Flight Time)`

This metric has these fields:

- **What it measures:** How high the athlete jumped, worked out from time in the air.
- **Window or phase:** Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as jump height computed from `Flight Time` ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. A common physics restatement is `h = g * FT^2 / 8`, where `FT` is flight time in seconds.
- **Inputs:** Take-off and landing events.
- **Units:** cm.
- **Variants:** `Jump Height (Flight Time) in Inches`. API identifier `JUMP_HEIGHT`, group `Takeoff`, unit `Centimeter`, trend `Positive`, no asymmetry ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Jump Height (Flight Time) in Inches`

This metric has these fields:

- **What it measures:** The flight-time jump height expressed in inches.
- **Window or phase:** Same window as `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Flight: take-off (force below 20 N) to landing (force above 20 N) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Jump Height (Flight Time)` after conversion to inches ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_in = h_cm / 2.54`.
- **Inputs:** Jump Height (Flight Time).
- **Units:** in.
- **Variants:** `Jump Height (Flight Time)` in cm.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (FT) Relative Landing RFD`

This metric has these fields:

- **What it measures:** Landing RFD per centimetre of jump height.
- **Window or phase:** Combines `Landing RFD` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Landing RFD` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Landing RFD / JH_FT[cm]`.
- **Inputs:** Landing RFD, Jump Height (Flight Time).
- **Units:** N/s/cm.
- **Variants:** API identifier `JUMP_HEIGHT_RELATIVE_LANDING_RFD`, group `Landing`, unit `NewtonPerSecondPerCentimeter` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Jump Height (FT) Relative Peak Landing Force`

This metric has these fields:

- **What it measures:** Peak landing force per centimetre of jump height.
- **Window or phase:** Combines `Peak Landing Force` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Peak Landing Force` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Landing Force / JH_FT[cm]`.
- **Inputs:** Peak Landing Force, Jump Height (Flight Time).
- **Units:** N/cm.
- **Variants:** API identifier `JUMP_HEIGHT_RELATIVE_PEAK_LANDING_FORCE`, group `Landing`, unit `NewtonPerCentimeter` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API).

#### `Jump Height (Imp-Dis)`

This metric has these fields:

- **What it measures:** The highest point the centre of mass reaches in the air, from double-integrated force.
- **Window or phase:** Take-off to landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest displacement reached by the centre of mass from Take-off to Landing ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h = max s(t)` for `t` between take-off and landing, where `s(t)` is displacement from the start of integration. Whether the take-off displacement is subtracted is not published.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Imp-Mom)`

This metric has these fields:

- **What it measures:** How high the centre of mass rises, worked out from take-off velocity.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as jump height computed using the centre-of-mass velocity at the moment of Take-off together with Body Mass ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. A common physics restatement is `h = v_TO^2 / (2 g)`, where `v_TO` is take-off velocity (the integral of `F - BW` from the start of integration to take-off, divided by body mass, from the User Guide relations) and `g` is gravity. VALD's value of `g` is not published.
- **Inputs:** Total vertical force, body weight, start of integration, take-off event.
- **Units:** cm (glossary); in on some displays.
- **Variants:** `Jump Height (Imp-Mom) in Inches` (same value in inches) ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Default SJ and LSJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** VALD states impulse-momentum height reduces variability from flight time or landing errors ([Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump)). A VALD Health article describes it as maximum vertical displacement between take-off and landing ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)), which matches the glossary wording for `Jump Height (Imp-Dis)` rather than Imp-Mom.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks).

#### `Jump Height (Imp-Mom) in Inches`

This metric has these fields:

- **What it measures:** The Imp-Mom jump height expressed in inches.
- **Window or phase:** Same window as `Jump Height (Imp-Mom)`, as the definition states ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Single point: take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Jump Height (Imp-Mom)` after conversion to inches ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_in = h_cm / 2.54` (definition of the inch).
- **Inputs:** Jump Height (Imp-Mom).
- **Units:** in.
- **Variants:** `Jump Height (Imp-Mom)` in cm.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing Impulse`

This metric has these fields:

- **What it measures:** Total impulse from landing to peak landing force.
- **Window or phase:** Landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak landing force. The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the absolute impulse from Landing up to the moment `Peak Landing Force` happens ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_L to t_PLF] F dt`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing Net Peak Force / BM`

This metric has these fields:

- **What it measures:** Peak landing force above body weight, relative to body mass.
- **Window or phase:** After landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force after Landing, with Body Weight subtracted, and the result divided by Body Mass ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(max F - BW) / BM` after landing.
- **Inputs:** Peak Landing Force, body weight, body mass.
- **Units:** N/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing RFD`

This metric has these fields:

- **What it measures:** How fast force rises from landing to peak landing force.
- **Window or phase:** Landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak landing force. The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as RFD measured from Landing up to the moment `Peak Landing Force` happens ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_PLF - F(t_L)) / (t_PLF - t_L)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** `Jump Height (FT) Relative Landing RFD`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing RFD 50ms`

This metric has these fields:

- **What it measures:** Rise in force over the first 50 ms after landing.
- **Window or phase:** First 50 ms after landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD over the first 50ms after Landing ([Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F(t_L + 0.05 s) - F(t_L)) / 0.05 s`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; detection of the event that starts the fixed window ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.16](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Mean Landing Power`

This metric has these fields:

- **What it measures:** Average power from landing to the end of the rep.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the average power from Landing until the rep ends ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean P(t)` over the landing phase.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Acceleration`

This metric has these fields:

- **What it measures:** Highest acceleration of the centre of mass after landing.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest acceleration reached by the centre of mass from Landing until the rep ends ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max a(t)` over the landing phase.
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Force`

This metric has these fields:

- **What it measures:** Highest force after landing.
- **Window or phase:** After landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force that occurs after Landing ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` after landing.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Peak Landing Force / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Force / BM`

This metric has these fields:

- **What it measures:** Peak landing force relative to body mass.
- **Window or phase:** Same window as `Peak Landing Force`, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): After landing ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Peak Landing Force` divided by Body Mass ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Landing Force / BM`.
- **Inputs:** Peak Landing Force, body mass.
- **Units:** N/kg.
- **Variants:** `Peak Landing Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Power`

This metric has these fields:

- **What it measures:** Highest power from landing to the end of the rep.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the maximum power from Landing until the rep ends ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max P(t)` over the landing phase; sign convention not published.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Velocity`

This metric has these fields:

- **What it measures:** Peak centre-of-mass velocity after landing.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest velocity of the centre of mass from landing until the rep is over ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Extreme of `v(t)` over the landing phase; whether VALD reports the largest negative value is not published.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Positive Take-off Impulse`

This metric has these fields:

- **What it measures:** Net impulse from first movement to take-off.
- **Window or phase:** Entire repetition, take-off and landing combined, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the net impulse over the whole repetition, counting the take-off and landing parts together ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: The SJ glossary wording describes the whole rep, the same as Positive Impulse. The User Guide describes it as total concentric work above body weight ([User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.28](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RSI-modified (Imp-Mom)`

This metric has these fields:

- **What it measures:** Imp-Mom jump height per unit of contraction time.
- **Window or phase:** Combines `Jump Height (Imp-Mom)` and `Contraction Time`, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Jump Height (Imp-Mom)` divided by Contraction Time ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `RSImod_IM = JH_IM [m] / CT [s]`.
- **Inputs:** Jump Height (Imp-Mom), Contraction Time.
- **Units:** m/s.
- **Variants:** `RSI-modified` uses flight-time jump height.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `RSI-modified`

This metric has these fields:

- **What it measures:** Jump height per unit of time spent on the ground before take-off.
- **Window or phase:** Combines `Jump Height (Flight Time)` and `Contraction Time`, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD says it is `Jump Height (Flight Time)` divided by Contraction Time ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `RSImod = JH_FT [m] / CT [s]`. A VALD worked table divides 29.1 cm by 650 ms to give 0.45 m/s, which confirms metres over seconds ([RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple))
- **Inputs:** Jump Height (Flight Time), Contraction Time.
- **Units:** m/s.
- **Variants:** `RSI-modified (Imp-Mom)` uses Imp-Mom jump height instead. The default-metrics page lists the unit as `-` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)); the glossary lists m/s.
- **Comparison with standard methods or other vendors:** The User Guide defines RSImod as jump height divided by contraction time ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); VALD's RSI-mod article gives `RSI-Mod = Jump Height / Contraction Time` ([RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple)). Both match the glossary.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; changes in either term of the ratio; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Take-off Peak Force`

This metric has these fields:

- **What it measures:** The highest total force from first movement to take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force from Start of Movement to Take-off ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` between start of movement and take-off.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Take-off Peak Force / BM` (N/kg). The knowledge base names the key moment 'Peak take-off force' ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump).

#### `Take-off Peak Force / BM`

This metric has these fields:

- **What it measures:** Take-off peak force relative to body mass.
- **Window or phase:** Same window as `Take-off Peak Force`, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Take-off Peak Force` divided by Body Mass ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Take-off Peak Force / BM`.
- **Inputs:** Take-off Peak Force, body mass.
- **Units:** N/kg.
- **Variants:** `Take-off Peak Force`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Total Work`

This metric has these fields:

- **What it measures:** Area under the power curve from first movement to take-off.
- **Window or phase:** Start of movement to take-off. The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the integral of power, meaning the area beneath the power-time curve, from Start of Movement to Take-off ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_SoM to t_TO] P(t) dt`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** J.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Velocity at Peak Power`

This metric has these fields:

- **What it measures:** Upward speed at the instant of peak power.
- **Window or phase:** Single point: the instant of peak power, with peak power found between start of movement and take-off, as the definition states ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the centre of mass velocity at the moment Peak Power occurs between Start of Movement and Take-off ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `v(t_PP)`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Vertical Velocity at Take-off`

This metric has these fields:

- **What it measures:** Upward speed of the centre of mass when the feet leave the plates.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the centre of mass velocity at the moment Take-off occurs ([Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `v_TO = (1 / BM) * ∫[t_SoI to t_TO] (F - BW) dt`, using the User Guide relations `a = (F - BW) / m` and `v = v0 + a t` with `v0 = 0` at the start of integration ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf))
- **Inputs:** Total vertical force, body weight, start of integration, take-off event.
- **Units:** m/s.
- **Variants:** `Take-off Momentum` multiplies this by body mass.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.17](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Landing Stiffness`

This metric has these fields:

- **What it measures:** Landing force divided by how far the centre of mass sinks on landing.
- **Window or phase:** Single point: maximum negative displacement during landing, as the definition states ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). The end of the landing window is not published.
- **Calculation:** VALD defines this metric as force divided by the displacement of the center of mass, taken where the displacement reaches its maximum negative value while landing ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `F(t_minS) / |s(t_minS)|` at the lowest landing point. Which displacement reference VALD uses is not published.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; start of integration setting ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Mean Landing Force`

This metric has these fields:

- **What it measures:** Average force during the landing phase.
- **Window or phase:** Landing (force above 20 N after take-off) ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD describes it as the mean vertical force across the landing phase ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `mean F(t)` over the landing phase.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes).

#### `Take-off Momentum`

This metric has these fields:

- **What it measures:** Body mass times take-off velocity.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Calculation:** VALD says it is the vertical velocity at take-off times body mass ([ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)). Restatement: `p = BM * v_TO`. The unit is not published; the API unit list includes `KilogramMeterPerSecond` ([FD API spec](https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json))
- **Inputs:** Vertical Velocity at Take-off, body mass.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Start of movement method and threshold; start of integration setting; body weight accuracy; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes), [FD API spec](https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json).

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
- **Calculation:** VALD defines it as the weight that is estimated before every rep and saved in the `Athlete Standing Weight` metric when the weighing step is skipped ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)). Formula: Not published.
- **Inputs:** Still period before each rep.
- **Units:** Not published.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy ([factor details](README.md#factors-that-change-the-numbers)). Auto-weight settings: minimum weight, maximum standard deviation, steady period and maximum weight deviation ([Manage ForceDecks iOS app settings](https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings), [Weight Settings in ForceDecks Jump](https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump)).
- **Sources:** [FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API), [Manage ForceDecks iOS app settings](https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings), [Weight Settings in ForceDecks Jump](https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump).

### Drop jump (DJ, SLDJ)

The DJ starts on a box behind the plates: step off, land with both feet, jump as high as possible with minimal contact time ([ForceDecks Test Protocol - Drop Jump](https://support.vald.com/hc/en-au/articles/4999913990425-ForceDecks-Test-Protocol-Drop-Jump)). Drop landing is the point where a 20 N threshold is exceeded; take-off is force below 20 N after drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). A body weight is required before the jump, or detection fails ([User Guide p.31](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

VALD-stated count: 59 DJ metrics ([User Guide p.35](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The glossary lists 56 DJ metric names.

2026 defaults: DJ: `RSI (JH (Flight Time) / Contact Time)`, `Jump Height (Imp-Mom)`, `Contact Time`, `Effective Drop`. SLDJ: `RSI (JH (Flight Time) / Contact Time)`, `Jump Height (Flight Time)`, `Contact Time`, `Effective Drop`, `Peak Impact Force` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).

#### `RSI (JH (Flight Time)/Contact Time)`

This metric has these fields:

- **What it measures:** Jump height produced per unit of ground contact time.
- **Window or phase:** Combines `Jump Height (Flight Time)` and `Contact Time`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Jump Height (Flight Time)` set against Contact Time as a ratio ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `JH_FT [m] / Contact Time [s]`.
- **Inputs:** Jump Height (Flight Time), Contact Time.
- **Units:** m/s.
- **Variants:** Default DJ metric written `RSI (JH (Flight Time) / Contact Time)` with unit `-` ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). A VALD Health article allows Imp-Mom or flight-time jump height in RSI ([Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump)).
- **Comparison with standard methods or other vendors:** The User Guide glossary defines RSI as flight time divided by contact time, which matches `RSI (Flight Time/Contact Time)` rather than this metric ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; drop technique and drop height; changes in either term of the ratio; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump), [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `RSI (Flight Time/Contact Time)`

This metric has these fields:

- **What it measures:** Time in the air per unit of ground contact time.
- **Window or phase:** Combines `Flight Time` and `Contact Time`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as Flight Time set against Contact Time as a ratio ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Flight Time / Contact Time`.
- **Inputs:** Flight Time, Contact Time.
- **Units:** Unitless.
- **Variants:** Listed for the Single Leg Drop Jump ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** Matches the User Guide RSI definition ([User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; drop technique and drop height; changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [User Guide p.102](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Contact Time`

This metric has these fields:

- **What it measures:** Time on the plates between drop landing and take-off.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the time from Drop Landing to Take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_TO - t_DL`.
- **Inputs:** Drop landing and take-off events.
- **Units:** s.
- **Variants:** Default DJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)). Drop landing uses a 20 N threshold ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Jump Height (Imp-Mom)`

This metric has these fields:

- **What it measures:** Rebound jump height worked out from take-off velocity.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as jump height worked out from the centre of mass velocity at the moment of Take-off, together with Body Mass ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. `h = v_TO^2 / (2 g)` is a common physics restatement. For a drop jump, VALD says it uses reverse integration from the landing phases for effective drop height ([Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump)); how velocity at contact is initialised for jump height is not published.
- **Inputs:** Total vertical force, body weight, take-off event.
- **Units:** cm.
- **Variants:** `Jump Height (Imp-Mom) in Inches`. Default DJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** If box height is entered wrongly, flight-time and Imp-Mom heights disagree ([User Guide p.33](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Body weight accuracy; take-off threshold (20 N or 30 N); box height entry; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.33](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Jump Height (Imp-Mom) in Inches`

This metric has these fields:

- **What it measures:** Imp-Mom rebound height in inches.
- **Window or phase:** Same window as `Jump Height (Imp-Mom)`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Single point: take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Jump Height (Imp-Mom)` expressed in inches ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_cm / 2.54`.
- **Inputs:** Jump Height (Imp-Mom).
- **Units:** in.
- **Variants:** `Jump Height (Imp-Mom)`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Flight Time)`

This metric has these fields:

- **What it measures:** Rebound jump height worked out from time in the air.
- **Window or phase:** Flight: take-off (force below 20 N after drop landing) to landing (force above 20 N) ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as jump height derived from Flight Time ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation; `h = g * FT^2 / 8` is a common physics restatement.
- **Inputs:** Take-off and landing events.
- **Units:** cm.
- **Variants:** `Jump Height (Flight Time) in Inches`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Flight Time) in Inches`

This metric has these fields:

- **What it measures:** Flight-time rebound height in inches.
- **Window or phase:** Same window as `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Flight: take-off (force below 20 N after drop landing) to landing (force above 20 N) ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Jump Height (Flight Time)` expressed in inches ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `h_cm / 2.54`.
- **Inputs:** Jump Height (Flight Time).
- **Units:** in.
- **Variants:** `Jump Height (Flight Time)`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (Imp-Dis)`

This metric has these fields:

- **What it measures:** Highest point of the centre of mass in the air, from double-integrated force.
- **Window or phase:** Take-off to landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the largest displacement of the centre of mass from Take-off to Landing ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max s(t)` between take-off and landing.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; take-off threshold (20 N or 30 N); landing threshold and impacts during flight; box height entry ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Flight Time`

This metric has these fields:

- **What it measures:** Time in the air after the rebound.
- **Window or phase:** Flight: take-off (force below 20 N after drop landing) to landing (force above 20 N) ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the time from Take-off to Landing ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_L - t_TO`.
- **Inputs:** Take-off and landing events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Take-off threshold (20 N or 30 N); landing threshold and impacts during flight; landing technique ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Drop Height`

This metric has these fields:

- **What it measures:** Height of the drop before landing.
- **Window or phase:** Before drop landing. The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the vertical height of the initial drop ahead of Drop Landing, which is either typed in by hand or calculated from `Effective Drop` ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Manual entry, or `Effective Drop`.
- **Inputs:** Manual entry or Effective Drop.
- **Units:** cm.
- **Variants:** Exported as a test parameter in VALD Hub Results Export since 2026-09-28 ([VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Box height entry; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026).

#### `Effective Drop`

This metric has these fields:

- **What it measures:** Drop height implied by how fast the athlete hits the plates.
- **Window or phase:** Uses `Vertical Velocity at Contact`, as the definition states ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). That velocity is taken at drop landing ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is `Drop Height` computed from `Vertical Velocity at Contact` and gravity ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: VALD does not publish the equation. `h = v_contact^2 / (2 g)` is a common physics restatement. VALD says it uses reverse integration from the landing phases ([Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump)).
- **Inputs:** Vertical Velocity at Contact, gravity.
- **Units:** cm.
- **Variants:** Default DJ metric described as 'the predicted drop height, calculated from the individual's velocity when landing' ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)). In a VALD example, a 50 cm box gave an average effective drop of 38.3 cm. The User Guide says the likely cause was either that the athlete lowered the body before stepping off the box or that the platform height was not accounted for ([User Guide p.33](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [User Guide p.33](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Vertical Velocity at Contact`

This metric has these fields:

- **What it measures:** Downward speed of the centre of mass at drop landing.
- **Window or phase:** Single point: drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the centre of mass velocity at the moment Drop Landing happens ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Not published as a formula; see Effective Drop.
- **Inputs:** Total vertical force, body weight.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Vertical Velocity at Take-off`

This metric has these fields:

- **What it measures:** Upward speed at take-off.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the centre of mass velocity at the moment Take-off happens ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `v_TO`; initial condition for a drop jump not published.
- **Inputs:** Total vertical force, body weight.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Coefficient of Restitution`

This metric has these fields:

- **What it measures:** Compares landing speed and take-off speed.
- **Window or phase:** Combines `Vertical Velocity at Contact` and `Vertical Velocity at Take-off`, as the definition states ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Vertical Velocity at Contact` set against `Vertical Velocity at Take-off` as a ratio ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: As written: `v_contact / v_TO`.
- **Inputs:** Vertical Velocity at Contact, Vertical Velocity at Take-off.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Countermovement Depth`

This metric has these fields:

- **What it measures:** How far the centre of mass sinks during ground contact.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the displacement from Drop Landing to Take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Minimum `s(t)` during contact is a likely reading; the glossary text says only 'displacement between drop landing to take-off'.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Displacement at Take-off`

This metric has these fields:

- **What it measures:** Centre-of-mass position at take-off relative to drop landing.
- **Window or phase:** Single point: take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the displacement measured at the instant Take-off happens ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `s(t_TO)`.
- **Inputs:** Displacement of the centre of mass (from double-integrated force), and the phase events.
- **Units:** cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Duration`

This metric has these fields:

- **What it measures:** Time from drop landing to the lowest point.
- **Window or phase:** Eccentric phase: drop landing (force above 20 N) to zero velocity ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the duration of the Eccentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_ZV - t_DL`.
- **Inputs:** Drop landing and zero velocity events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Duration`

This metric has these fields:

- **What it measures:** Time from the lowest point to take-off.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the duration of the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_TO - t_ZV`.
- **Inputs:** Zero velocity and take-off events.
- **Units:** ms.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse while absorbing the landing.
- **Window or phase:** Eccentric phase: drop landing (force above 20 N) to zero velocity ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the net impulse over the Eccentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_DL to t_ZV] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** Asymmetry variant listed as commonly used ([User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Impulse`

This metric has these fields:

- **What it measures:** Net impulse while pushing up.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the net impulse over the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** Asymmetry variant listed as commonly used ([User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Concentric Impulse (Abs) / BM`

This metric has these fields:

- **What it measures:** Total push impulse relative to body mass.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the absolute impulse over the Concentric Phase, divided by Body Mass ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_ZV to t_TO] F dt / BM`.
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric Mean Force`

This metric has these fields:

- **What it measures:** Average force while absorbing.
- **Window or phase:** Eccentric phase: drop landing (force above 20 N) to zero velocity ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the mean vertical force over the Eccentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Force`

This metric has these fields:

- **What it measures:** Average force while pushing up.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the mean vertical force over the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F(t)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Eccentric:Concentric Mean Force Ratio`

This metric has these fields:

- **What it measures:** Absorbing force compared with pushing force.
- **Window or phase:** Combines `Eccentric Mean Force` and `Concentric Mean Force`, as the definition states ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines it as `Eccentric Mean Force` set against `Concentric Mean Force` as a ratio ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Eccentric Mean Force / Concentric Mean Force`; percentage scaling not published.
- **Inputs:** Eccentric and Concentric Mean Force.
- **Units:** %.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); changes in either term of the ratio ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Power`

This metric has these fields:

- **What it measures:** Average power while pushing up.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the mean power over the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Concentric Mean Power / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Power / BM`

This metric has these fields:

- **What it measures:** Average push power relative to body mass.
- **Window or phase:** Same window as `Concentric Mean Power`, as the definition states ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as `Concentric Mean Power` divided by Body Mass ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Concentric Mean Power / BM`.
- **Inputs:** Concentric Mean Power, body mass.
- **Units:** W/kg.
- **Variants:** `Concentric Mean Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Mean Velocity`

This metric has these fields:

- **What it measures:** Average upward speed while pushing.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the mean velocity over the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Concentric Peak Velocity`

This metric has these fields:

- **What it measures:** Highest upward speed before take-off.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest velocity reached in the Concentric Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Force at Zero Velocity`

This metric has these fields:

- **What it measures:** Force at the lowest point of contact.
- **Window or phase:** Single point: zero velocity before take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the vertical force at the moment velocity is zero before Take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `F(t_ZV)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** `Force at Zero Velocity / BM`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Force at Zero Velocity / BM`

This metric has these fields:

- **What it measures:** Force at the lowest point relative to body mass.
- **Window or phase:** Same window as `Force at Zero Velocity`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Single point: zero velocity before take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as `Force at Zero Velocity` divided by Body Mass ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Force at Zero Velocity / BM`.
- **Inputs:** Force at Zero Velocity, body mass.
- **Units:** N/kg.
- **Variants:** `Force at Zero Velocity`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Impact Force`

This metric has these fields:

- **What it measures:** The first force spike after landing from the box.
- **Window or phase:** The first rise in force after drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the largest vertical force reached during the first spike, or rise, in vertical force after Drop Landing ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` within the first spike.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Default SLDJ metric ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)). The knowledge base calls it the 'greatest passive force on impact from box drop' ([Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump).

#### `Contact Trough`

This metric has these fields:

- **What it measures:** Force at the dip between the impact spike and the drive-off peak.
- **Window or phase:** Between peak impact force and the start of the concentric phase. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest vertical force in the span from when `Peak Impact Force` occurs to the Start of the Concentric Phase ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Glossary text says maximum. The knowledge base and User Guide define the contact trough as the lowest force point between peak impact and peak drive-off force ([Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump), [User Guide p.34](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). The sources conflict; the knowledge base reading is `min F(t)` in that window.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump), [User Guide p.34](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Drive-Off Force`

This metric has these fields:

- **What it measures:** Highest force while pushing off.
- **Window or phase:** Drive-off phase: contact trough to take-off. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest vertical force in the Drive-Off Phase, which runs from `Contact Trough` to Take-off ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` between contact trough and take-off.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Drop Landing Force`

This metric has these fields:

- **What it measures:** Highest force during ground contact.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest vertical force in the Contact Phase ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` during contact.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant is a VALD-suggested starter DJ metric ([Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump).

#### `Drop Landing RFD`

This metric has these fields:

- **What it measures:** How fast force rises from drop landing to the landing peak.
- **Window or phase:** Drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak force while landing. The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the RFD from Drop Landing to the moment Peak Force occurs while landing ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_peak - F(t_DL)) / (t_peak - t_DL)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** Asymmetry variant listed as commonly used ([User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Drop technique and drop height; foot placement and landing timing; sampling rate ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Active Stiffness`

This metric has these fields:

- **What it measures:** Drive-off force divided by how far the centre of mass sinks.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as `Peak Drive-Off Force` divided by the largest displacement of the centre of mass in the Contact Phase ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Drive-Off Force / |min s(t)|` during contact.
- **Inputs:** Peak Drive-Off Force, displacement.
- **Units:** N/m.
- **Variants:** `Active Stiffness Index`. Listed for the Single Leg Drop Jump ([Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- **Comparison with standard methods or other vendors:** The User Guide describes it as peak active force divided by the change in centre-of-mass displacement from contact to the lowest point ([User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application), [User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Active Stiffness Index`

This metric has these fields:

- **What it measures:** Active stiffness scaled by drop height and body weight.
- **Window or phase:** Uses `Active Stiffness`, drop height and body weight, as the definition states ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). See `Active Stiffness` for its window.
- **Calculation:** VALD lists `Active Stiffness`, Drop Height, and Body Weight as the terms, with the operators left out of the glossary text ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Not published. The glossary text is incomplete and does not state whether stiffness is multiplied or divided by drop height.
- **Inputs:** Active Stiffness, Drop Height, body weight.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); box height entry ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Passive Stiffness`

This metric has these fields:

- **What it measures:** Impact force divided by how far the centre of mass sinks.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as `Peak Impact Force` divided by the largest displacement of the CoM in the Contact Phase ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Impact Force / |min s(t)|` during contact.
- **Inputs:** Peak Impact Force, displacement.
- **Units:** N/m.
- **Variants:** `Passive Stiffness Index`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Passive Stiffness Index`

This metric has these fields:

- **What it measures:** Passive stiffness scaled by drop height and body weight.
- **Window or phase:** Uses `Passive Stiffness`, drop height and body weight, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). See `Passive Stiffness` for its window.
- **Calculation:** VALD lists `Passive Stiffness` and Drop Height, then a division by Body Weight, with the operator between the first two terms left out of the glossary text ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Not published. The glossary text is incomplete about how drop height enters.
- **Inputs:** Passive Stiffness, Drop Height, body weight.
- **Units:** Unitless.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; box height entry ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Movement Start to Peak Power`

This metric has these fields:

- **What it measures:** Time from drop landing to peak power.
- **Window or phase:** Drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to peak power, before take-off. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the time from Drop Landing to the moment Peak Power occurs before Take-off ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `t_PP - t_DL`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Take-off Acceleration`

This metric has these fields:

- **What it measures:** Highest upward acceleration during contact.
- **Window or phase:** Contact phase: drop landing to take-off. The glossary phase list does not define a contact phase ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)); `Contact Time` is the time between drop landing and take-off ([Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the highest acceleration of the centre of mass from Drop Landing to Take-off ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max (F - BW) / BM`.
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.11](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Positive Impulse`

This metric has these fields:

- **What it measures:** Net impulse over the rep from drop landing on.
- **Window or phase:** Drop landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the repetition. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the net impulse across the whole repetition, running from Drop Landing until the repetition finishes ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_DL to end of rep] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); landing threshold and impacts during flight ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Positive Take-off Impulse`

This metric has these fields:

- **What it measures:** Net impulse across the contact.
- **Window or phase:** Drop landing and take-off phases combined. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the net impulse over the Drop Landing phase and the Take-off phase together ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `∫[t_DL to t_TO] max(F - BW, 0) dt`, the area above body weight only. This restates the glossary net impulse definition, area under the force curve "only above body weight" ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Inputs:** Total vertical force, body weight, and the phase events.
- **Units:** N s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Power`

This metric has these fields:

- **What it measures:** Highest power while pushing up.
- **Window or phase:** Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest power in the Concentric Phase ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** `Peak Power / BM`.
- **Comparison with standard methods or other vendors:** The User Guide describes DJ peak power as the maximum power during the trial ([User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)), which differs from the glossary concentric-phase window.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.36](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf).

#### `Peak Power / BM`

This metric has these fields:

- **What it measures:** Peak power relative to body mass.
- **Window or phase:** Same window as `Peak Power`, as the definition states ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)): Concentric phase: zero velocity (minimum displacement) to take-off ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as `Peak Power` divided by Body Mass ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Power / BM`.
- **Inputs:** Peak Power, body mass.
- **Units:** W/kg.
- **Variants:** `Peak Power`.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Body weight accuracy; drop technique and drop height; take-off threshold (20 N or 30 N); body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Force`

This metric has these fields:

- **What it measures:** Highest force on the final landing.
- **Window or phase:** After landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest vertical force once Landing has happened ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F(t)` after landing.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N.
- **Variants:** Asymmetry variant exists ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; foot placement and landing timing ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS).

#### `Landing Net Peak Force / BM`

This metric has these fields:

- **What it measures:** Peak landing force above body weight, relative to body mass.
- **Window or phase:** After landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The definition gives no end point. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the highest vertical force after Landing, minus Body Weight, then divided by Body Mass ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(max F - BW) / BM`.
- **Inputs:** Peak Landing Force, body weight, body mass.
- **Units:** N/kg.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; body mass used to normalise ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Landing RFD`

This metric has these fields:

- **What it measures:** How fast force rises from landing to the landing peak.
- **Window or phase:** Landing ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the point of peak landing force. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the RFD from Landing to the moment `Peak Landing Force` occurs ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `(F_PLF - F(t_L)) / (t_PLF - t_L)`.
- **Inputs:** Total vertical force (left plus right) and time.
- **Units:** N/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (FT) Relative Landing RFD`

This metric has these fields:

- **What it measures:** Landing RFD per centimetre of jump height.
- **Window or phase:** Combines `Landing RFD` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD defines this metric as `Landing RFD` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Landing RFD / JH_FT`.
- **Inputs:** Landing RFD, Jump Height (Flight Time).
- **Units:** N/s/cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Jump Height (FT) Relative Peak Landing Force`

This metric has these fields:

- **What it measures:** Peak landing force per centimetre of jump height.
- **Window or phase:** Combines `Peak Landing Force` and `Jump Height (Flight Time)`, as the definition states ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Each term uses its own window.
- **Calculation:** VALD describes it as `Peak Landing Force` divided by `Jump Height (Flight Time)` ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `Peak Landing Force / JH_FT`.
- **Inputs:** Peak Landing Force, Jump Height (Flight Time).
- **Units:** N/cm.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report; take-off threshold (20 N or 30 N) ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Mean Landing Acceleration`

This metric has these fields:

- **What it measures:** Average acceleration after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the mean acceleration of the centre of mass from Landing until the rep finishes ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean a(t)`.
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Mean Landing Power`

This metric has these fields:

- **What it measures:** Average power after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the mean power from Landing until the rep finishes ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean F*v`.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Mean Landing Velocity`

This metric has these fields:

- **What it measures:** Average centre-of-mass velocity after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines this metric as the mean velocity of the centre of mass from Landing until the rep finishes ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `mean v(t)`.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Acceleration`

This metric has these fields:

- **What it measures:** Highest acceleration after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD describes it as the highest acceleration of the centre of mass from Landing until the rep finishes ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max a(t)`.
- **Inputs:** Total vertical force, body weight, body mass.
- **Units:** m/s².
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Power`

This metric has these fields:

- **What it measures:** Highest power after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD says it is the highest power from Landing until the rep finishes ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: `max F*v`; sign not published.
- **Inputs:** Power (force x velocity), and the phase events.
- **Units:** W.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

#### `Peak Landing Velocity`

This metric has these fields:

- **What it measures:** Peak velocity after landing.
- **Window or phase:** Landing after the flight ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)) to the end of the rep. VALD does not publish how it detects the end of the rep. The metric's definition names this window ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- **Calculation:** VALD defines it as the highest velocity of the centre of mass from Landing until the rep finishes ([Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Restatement: Extreme of `v(t)`; sign not published.
- **Inputs:** Velocity of the centre of mass (from integrated force), and the phase events.
- **Units:** m/s.
- **Variants:** None published.
- **Comparison with standard methods or other vendors:** No source-supported comparison found in VALD's public sources.
- **What changes the number:** Landing threshold and impacts during flight; body weight accuracy; which trial you report ([factor details](README.md#factors-that-change-the-numbers)).
- **Sources:** [Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.13](https://support.vald.com/hc/en-au/article_attachments/31552911571353).

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
