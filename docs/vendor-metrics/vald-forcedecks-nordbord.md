# VALD ForceDecks and NordBord metrics

This page explains how VALD ForceDecks and VALD NordBord calculate each metric in their exports, so you can see what every number means. ForceDecks force plates measure only force and time, and ForceDecks derives body mass, impulse, acceleration, velocity, power, and displacement from them. NordBord measures force with a load cell in each ankle hook, and calculates torque and impulse. The metric blocks sit on part pages, one for each group of tests. This page holds the summary tables, the glossary, the factors that change the numbers, the conflicts, the list of what VALD does not publish, a worked example, and the sources.

Checked against: the VALD ForceDecks Technical Glossary V2.0 (March 2024), the VALD ForceDecks User Guide v2 (November 2023), the VALD NordBord Test Guide, the NordBord Technical Specifications, the External ForceDecks API specification (`v2019q3`) and its guide, the External NordBord API specification (`v1`) and its guide, VALD support articles and release notes, and VALD Performance and VALD Health articles, 2026-10-02.

VALD, ForceDecks, NordBord, VALD Hub, and Hawkin Dynamics are trademarks of their owners. This repository is not affiliated with or endorsed by VALD.

VALD's other products (ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware) are on [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](vald-other-products.md). Hawkin Dynamics force plates are on [Hawkin Dynamics metrics](hawkin-dynamics.md). Some Hawkin metrics share a name with VALD metrics but differ. See [Hawkin and VALD name collisions](hawkin-dynamics.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Pages in this set

Open the metric blocks on these part pages:

- [Countermovement jump](vald-forcedecks-nordbord-cmj.md): 125 metric blocks. Covers the countermovement jump (CMJ) and its loaded, Abalakov, and single-leg variants.
- [Squat jump and drop jump](vald-forcedecks-nordbord-squat-jump-drop-jump.md): 128 metric blocks. Covers the squat jump (SJ, LSJ) and the drop jump (DJ, SLDJ).
- [Rebound, hop, and landing tests](vald-forcedecks-nordbord-rebound-hop-landing.md): 60 metric blocks. Covers the countermovement rebound jump (CMRJ, SLCMRJ), hop tests (HJ, SLHJ), Hop and Return (SLHAR), and Land and Hold (LAH, SLLAH).
- [Squat, push-up, sit to stand, balance, isometric, and general tests](vald-forcedecks-nordbord-squat-isometric-general.md): 75 metric blocks. Covers the squat assessment (SQT, SLSQT), push-up tests (PUSHUPT, PPU), Sit to Stand to Sit (STSTS), balance tests (QSB, SLSB, SLROSB), isometric tests (IMTP and others), General Force-Time Analysis (GFTA), and the cross-test ratios (DSI, EUR).
- [NordBord](vald-forcedecks-nordbord-nordbord.md): 38 metric blocks. Covers NordBord test metrics and training mode metrics.

## How to read this page

Each metric block on a part page has these fields:

- What it measures: one plain sentence.
- Window or phase: the part of the movement used, with the start and end events.
- Calculation: VALD's definition in paraphrase, then the formula in plain math where VALD or a cited source gives one. A `Restatement:` is this page's plain-math version, not VALD's statement. A restatement never adds a rule VALD did not publish. Where VALD is silent, the block says Not published.
- Inputs: the raw signals or other metrics needed.
- Units: as published by VALD.
- Variants: related metrics such as `/ BM`, left, right, asymmetry, or inches.
- Comparison with standard methods or other vendors: only where a source supports it.
- What changes the number: short factor names, with the detail and sources in [Factors that change the numbers](#factors-that-change-the-numbers).
- Sources: the VALD pages and documents behind the block.

Not published means VALD does not publish that detail in the public sources checked. It does not mean VALD lacks the information. The knowledge base is VALD's support site, `support.vald.com`.

This page uses this notation in restatements:

- `F(t)`: total vertical force (left plus right plate) at time `t`, in N.
- `BW`: body weight in N. `BM`: body mass in kg. The User Guide writes "Body Mass (BM) = F ÷ g" ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- `g`: gravity. VALD does not publish the value it uses.
- `a(t) = (F - BW) / BM`, `v = v0 + a t`, `P = F * v`, `s = v t` (User Guide relations) ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)). ForceDecks integrates numerically and restarts integration before each rep ([How ForceDecks Minimize Integration Drift](https://valdperformance.com/news/how-forcedecks-minimize-integration-drift)).
- `t_SoM`: start of movement. `t_minF`: minimum eccentric force. `t_EPV`: eccentric peak velocity. `t_ZV`: zero velocity. `t_TO`: take-off. `t_L`: landing. `t_DL`: drop landing.

## Test types and metric counts

The table lists each test type, the number of metric blocks on these pages, and the metric count VALD states in its User Guide (November 2023). VALD does not publish the full list of exportable metrics. The complete list sits behind the `/resultdefinitions` endpoint of the ForceDecks API, which needs API credentials ([A guide to using the External ForceDecks API](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)). Where VALD states a higher count than these pages cover, the missing names are Not published. ForceDecks also reports up to 200 summary metrics per test ([User Guide p.101](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)), and VALD says ForceDecks contains several hundred metrics across assessments ([Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)).

| Test group | Test codes | Metric blocks | VALD-stated metric count | Page |
|---|---|---|---|---|
| Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ) | CMJ, LCMJ, ABCMJ, SLJ | 125 | 112 (User Guide, 2023) | [cmj](vald-forcedecks-nordbord-cmj.md) |
| Squat jump (SJ, LSJ) | SJ, LSJ | 70 | 71 (User Guide, 2023) | [squat-jump-drop-jump](vald-forcedecks-nordbord-squat-jump-drop-jump.md) |
| Drop jump (DJ, SLDJ) | DJ, SLDJ | 58 | 59 (User Guide, 2023) | [squat-jump-drop-jump](vald-forcedecks-nordbord-squat-jump-drop-jump.md) |
| Countermovement rebound jump (CMRJ, SLCMRJ) | CMRJ, SLCMRJ | 26 | 82 (User Guide, 2023) | [rebound-hop-landing](vald-forcedecks-nordbord-rebound-hop-landing.md) |
| Hop tests (HJ, SLHJ) | HJ, SLHJ | 11 | 54 (User Guide, 2023) | [rebound-hop-landing](vald-forcedecks-nordbord-rebound-hop-landing.md) |
| Hop and Return (SLHAR) | SLHAR | 8 | Not published | [rebound-hop-landing](vald-forcedecks-nordbord-rebound-hop-landing.md) |
| Land and Hold (LAH, SLLAH) | LAH, SLLAH | 15 | 3 (2023), more added 2026-07-01 | [rebound-hop-landing](vald-forcedecks-nordbord-rebound-hop-landing.md) |
| Squat assessment (SQT, SLSQT) | SQT, SLSQT | 24 | 25 (User Guide, 2023) | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| Push up and plyometric push up (PUSHUPT, PPU) | PUSHUPT, PPU | 16 | Not published | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| Sit to Stand to Sit (STSTS) | STSTS | 8 | Not published | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| Balance tests (QSB, SLSB, SLROSB) | QSB, SLSB, SLROSB | 6 | 8 for QSB (User Guide, 2023) | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| Isometric tests (IMTP and others) | IMTP, ISOT, SLISOT, ISOSQT, SLISOSQT, IBSQT, ISOPU, STICR, SLSTICR, SEICR, SLSEICR, SLIMTP, SLHTTI, SLHSSI, SLHNTI, SLHNNI, SHLDISOI, SHLDISOT, SHLDISOY, RSAIP, RSHIP, RSKIP | 16 | 44 (User Guide, 2023) | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| General Force-Time Analysis (GFTA) | GFTA | 3 | Not published | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| Cross-test ratios (DSI, EUR) | Reports | 2 | Not applicable | [squat-isometric-general](vald-forcedecks-nordbord-squat-isometric-general.md) |
| NordBord test metrics | Nordic, Razor, ISO Prone, ISO 30°, ISO 60°, Custom | 22 | Not published | [nordbord](vald-forcedecks-nordbord-nordbord.md) |
| NordBord training metrics | Eccentric and isometric training mode | 16 | Not published | [nordbord](vald-forcedecks-nordbord-nordbord.md) |
| **Total** | | **426** | | |

ForceFrame, DynaMo, SmartSpeed, and HumanTrak are out of scope here. See the other VALD products page above.

## Summary tables

Each table lists the metric blocks for one test group, in page order. The last column says whether VALD publishes the calculation: Yes, Partly, or Not published. Yes means VALD gives a definition of the calculation and the block adds no caveat. Partly means VALD gives only a description, or the block notes that an equation or detail is not published. Not published means VALD gives no definition. The `Calculation published` column describes VALD's public sources, not a verdict on the metric.

### Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ)

The blocks for this group are on [the countermovement jump page](vald-forcedecks-nordbord-cmj.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Jump Height (Imp-Mom)` | How high the centre of mass rises, worked out from take-off velocity | cm (glossary); in on some displays | Partly |
| `Jump Height (Imp-Mom) in Inches` | The Imp-Mom jump height expressed in inches | in | Yes |
| `Jump Height (Flight Time)` | How high the athlete jumped, worked out from time in the air | cm | Partly |
| `Jump Height (Flight Time) in Inches` | The flight-time jump height expressed in inches | in | Yes |
| `Jump Height (Imp-Dis)` | The highest point the centre of mass reaches in the air, from double-integrated force | cm | Partly |
| `RSI-modified` | Jump height per unit of time spent on the ground before take-off | m/s | Yes |
| `RSI-modified (Imp-Mom)` | Imp-Mom jump height per unit of contraction time | m/s | Yes |
| `Contraction Time` | Time from the first movement to leaving the ground | ms | Yes |
| `Flight Time` | Time in the air between take-off and landing | ms | Yes |
| `Flight Time:Contraction Time` | Time in the air compared with time spent preparing the jump | Unitless | Yes |
| `Flight Time:Eccentric Duration` | Time in the air compared with the length of the downward phase | Unitless | Yes |
| `Vertical Velocity at Take-off` | Upward speed of the centre of mass when the feet leave the plates | m/s | Yes |
| `Take-off Momentum` | Body mass times take-off velocity | Not published | Partly |
| `Countermovement Depth` | How far the centre of mass drops during the dip | cm | Yes |
| `Displacement at Take-off` | How far the centre of mass has risen from standing height at the moment of take-off | cm | Yes |
| `Peak Power` | The highest power produced while pushing up | W | Yes |
| `Peak Power / BM` | Peak power relative to body mass | W/kg | Yes |
| `Velocity at Peak Power` | Upward speed at the instant of peak power | m/s | Yes |
| `Force at Peak Power` | Force at the instant of peak power | N | Yes |
| `Movement Start to Peak Power` | Time from first movement to peak power | s | Yes |
| `Movement Start to Peak Force` | Time from first movement to peak force | s | Yes |
| `Take-off Peak Force` | The highest total force from first movement to take-off | N | Yes |
| `Take-off Peak Force / BM` | Take-off peak force relative to body mass | N/kg | Yes |
| `Peak Net Take-off Force / BM` | Peak force above body weight, relative to body mass | N/kg | Yes |
| `Peak Take-off Acceleration` | The highest upward acceleration of the centre of mass before take-off | m/s² | Yes |
| `Concentric Duration` | Length of the upward pushing phase | ms | Yes |
| `Concentric Impulse` | Net push above body weight during the upward phase | N s | Yes |
| `Concentric Impulse (Abs) / BM` | Total (not net) upward-phase impulse relative to body mass | N s/kg | Yes |
| `Concentric Impulse-50ms` | Net impulse in the first 50 ms of the upward phase | N s | Yes |
| `Concentric Impulse-100ms` | Net impulse in the first 100 ms of the upward phase | N s | Yes |
| `Concentric Impulse-100ms:Concentric Impulse` | Share of the upward net impulse produced in the first 100 ms | Unitless | Yes |
| `P1 Concentric Impulse` | Net impulse in the first half (by time) of the upward phase | N s | Yes |
| `P2 Concentric Impulse` | Net impulse in the second half (by time) of the upward phase | N s | Yes |
| `P2 Concentric Impulse:P1 Concentric Impulse` | How the upward push is split between the second and first halves | Unitless | Yes |
| `Concentric Mean Force` | Average total force during the upward phase | N | Yes |
| `Concentric Mean Force / BM` | Average upward-phase force relative to body mass | N/kg | Yes |
| `Concentric Peak Force` | Highest total force during the upward phase | N | Yes |
| `Concentric Peak Force / BM` | Upward-phase peak force relative to body mass | N/kg | Yes |
| `Concentric Mean Power` | Average power during the upward phase | W | Yes |
| `Concentric Mean Power / BM` | Average upward-phase power relative to body mass | W/kg | Yes |
| `Concentric Mean Velocity` | Average upward speed during the upward phase | m/s | Yes |
| `Concentric Peak Velocity` | Highest upward speed before take-off | m/s | Yes |
| `Concentric RFD` | How fast force rises from the bottom of the dip to the concentric peak force | N/s | Yes |
| `Concentric RFD / BM` | Concentric RFD relative to body mass | N/s/kg | Yes |
| `Concentric RFD - 50ms` | Rise in force over the first 50 ms of the upward phase | N/s | Yes |
| `Concentric RFD - 100ms` | Rise in force over the first 100 ms of the upward phase | N/s | Yes |
| `Concentric RFD - 200ms` | Rise in force over the first 200 ms of the upward phase | N/s | Yes |
| `Concentric Maximum RFD` | The steepest 50 ms rise in force during the upward phase | N/s | Partly |
| `Concentric RPD` | How fast power rises from the bottom of the dip to peak power | W/s | Yes |
| `Concentric RPD / BM` | Concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric RPD - 50ms` | Rise in power over the first 50 ms of the upward phase | W/s | Yes |
| `Concentric RPD - 100ms` | Rise in power over the first 100 ms of the upward phase | W/s | Yes |
| `Concentric RPD-50ms / BM` | 50 ms concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric RPD-100ms / BM` | 100 ms concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric Time to Peak Force` | Time from the bottom of the dip to the concentric peak force | ms | Yes |
| `Eccentric Duration` | Length of the downward phase | ms | Yes |
| `Eccentric:Concentric Duration` | Downward-phase time compared with upward-phase time | % | Partly |
| `Contraction Time:Eccentric Duration` | Contraction time compared with the length of the downward phase | % | Partly |
| `Eccentric Mean Force` | Average force during the downward phase | N | Yes |
| `Eccentric:Concentric Mean Force Ratio` | Average downward-phase force compared with average upward-phase force | % | Partly |
| `Eccentric Peak Force` | Highest force during the downward phase | N | Yes |
| `Eccentric Peak Force / BM` | Downward-phase peak force relative to body mass | N/kg | Yes |
| `Minimum Eccentric Force` | The lowest force while unweighting at the start of the dip | N | Yes |
| `Eccentric Peak Velocity` | The fastest downward speed during the dip | m/s | Yes |
| `Eccentric Mean Power` | Average power during the downward phase | W | Partly |
| `Eccentric Mean Power / BM` | Average downward-phase power relative to body mass | W/kg | Yes |
| `Eccentric Peak Power` | Highest power during the downward phase | W | Partly |
| `Eccentric Peak Power / BM` | Downward-phase peak power relative to body mass | W/kg | Yes |
| `Eccentric Peak Power:Concentric Peak Power` | Downward peak power compared with upward peak power | Unitless | Yes |
| `Eccentric Acceleration Phase Duration` | Time from first movement to the fastest downward speed | s | Yes |
| `Eccentric Unloading Impulse` | Net impulse while the athlete drops before braking begins | N s | Partly |
| `Time to Braking Phase` | Time from first movement to the start of braking (minimum force) | s | Yes |
| `Braking Phase Duration` | Length of the braking phase | s | Yes |
| `Braking Phase Duration:Concentric Duration` | Braking time compared with upward-phase time | Unitless | Yes |
| `Braking Phase Duration:Contraction Time` | Braking time as a share of contraction time | Unitless | Yes |
| `Eccentric Braking Impulse` | Net impulse during braking, from minimum force to the bottom of the dip | N s | Partly |
| `Eccentric Braking RFD` | How fast force rises across the whole braking phase | N/s | Yes |
| `Eccentric Braking RFD / BM` | Braking RFD relative to body mass | N/s/kg | Yes |
| `Eccentric Braking RFD-100ms` | Rise in force over the first 100 ms of braking | N/s | Yes |
| `Eccentric Braking RFD-100ms / BM` | 100 ms braking RFD relative to body mass | N/s/kg | Yes |
| `Eccentric Mean Braking Force` | Average force during braking | N | Yes |
| `Eccentric Deceleration Phase Duration` | Length of the deceleration phase | s | Yes |
| `Eccentric Deceleration Impulse` | Net impulse used to stop the downward movement | N s | Yes |
| `Eccentric Deceleration Impulse / BM` | Deceleration impulse relative to body mass | N s/kg | Yes |
| `Eccentric Deceleration RFD` | How fast force rises while stopping the downward movement | N/s | Yes |
| `Eccentric Deceleration RFD / BM` | Deceleration RFD relative to body mass | N/s/kg | Yes |
| `Eccentric Mean Deceleration Force` | Average force while stopping the downward movement | N | Yes |
| `Force at Zero Velocity` | Force at the bottom of the dip | N | Yes |
| `Force at Zero Velocity / BM` | Force at the bottom of the dip relative to body mass | N/kg | Yes |
| `CMJ Stiffness` | Peak upward-phase force divided by dip depth | N/m | Partly |
| `Lower-Limb Stiffness` | Change in force across the downward phase divided by dip depth | N/m | Partly |
| `Mean Eccentric+Concentric Power:Time` | Average power from first movement to take-off, divided by contraction time | W/s | Yes |
| `Total Work` | Area under the power curve from first movement to take-off | J | Yes |
| `Positive Take-off Impulse` | Net impulse from first movement to take-off | N s | Yes |
| `Positive Impulse` | Net impulse over the whole rep | N s | Yes |
| `Peak Landing Force` | Highest force after landing | N | Yes |
| `Peak Landing Force / BM` | Peak landing force relative to body mass | N/kg | Yes |
| `Landing Net Peak Force / BM` | Peak landing force above body weight, relative to body mass | N/kg | Yes |
| `Landing Impulse` | Total impulse from landing to peak landing force | N s | Yes |
| `Landing RFD` | How fast force rises from landing to peak landing force | N/s | Yes |
| `Landing RFD 50ms` | Rise in force over the first 50 ms after landing | N/s | Yes |
| `Jump Height (FT) Relative Landing RFD` | Landing RFD per centimetre of jump height | N/s/cm | Yes |
| `Jump Height (FT) Relative Peak Landing Force` | Peak landing force per centimetre of jump height | N/cm | Yes |
| `Mean Landing Power` | Average power from landing to the end of the rep | W | Yes |
| `Peak Landing Power` | Highest power from landing to the end of the rep | W | Partly |
| `Peak Landing Acceleration` | Highest acceleration of the centre of mass after landing | m/s² | Yes |
| `Peak Landing Velocity` | Peak centre-of-mass velocity after landing | m/s | Partly |
| `Eccentric Deceleration Peak Force` | Highest force while stopping the downward movement | Not published | Yes |
| `Eccentric Deceleration Peak Force / BW` | Deceleration peak force normalised to body weight | Not published | Partly |
| `Eccentric Deceleration Mean Power` | Average power while stopping the downward movement | Not published | Yes |
| `Eccentric Deceleration Mean Power / BM` | Deceleration mean power relative to body mass | Not published | Yes |
| `Eccentric Deceleration Mean Velocity` | Average downward speed while decelerating | Not published | Yes |
| `Concentric Impulse:Eccentric Deceleration Impulse Ratio` | Upward net impulse compared with deceleration net impulse | Not published | Yes |
| `Concentric Phase:Contraction Time Ratio` | Share of contraction time spent pushing up | % | Yes |
| `Eccentric Deceleration:Contraction Time Ratio` | Share of contraction time spent decelerating | % | Yes |
| `Eccentric Unloading Phase:Contraction Time Ratio` | Share of contraction time spent unloading | % | Yes |
| `Eccentric Yielding Phase:Contraction Time Ratio` | Share of contraction time spent in the yielding phase | % | Yes |
| `Eccentric Acceleration Phase:Contraction Time Ratio` | Share of contraction time spent accelerating downward | % | Yes |
| `Eccentric Yielding Phase RFD` | Rate of force rise during the yielding phase | Not published | Partly |
| `Eccentric Yielding Phase RFD / BM` | Yielding-phase RFD relative to body mass | Not published | Partly |
| `Landing Stiffness` | Landing force divided by how far the centre of mass sinks on landing | Not published | Partly |
| `Mean Landing Force` | Average force during the landing phase | Not published | Yes |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |
| `Athlete Standing Weight` | Weight estimated before each rep when the weighing step was skipped | Not published | Yes |

### Squat jump (SJ, LSJ)

The blocks for this group are on [the squat jump and drop jump page](vald-forcedecks-nordbord-squat-jump-drop-jump.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Concentric Impulse` | Net push above body weight during the upward phase | N s | Yes |
| `Concentric Impulse (Abs) / BM` | Total (not net) upward-phase impulse relative to body mass | N s/kg | Yes |
| `Concentric Impulse-100ms` | Net impulse in the first 100 ms of the upward phase | N s | Yes |
| `Concentric Impulse-100ms:Concentric Impulse` | Share of the upward net impulse produced in the first 100 ms | Unitless | Yes |
| `Concentric Impulse-50ms` | Net impulse in the first 50 ms of the upward phase | N s | Yes |
| `Concentric Maximum RFD` | The steepest 50 ms rise in force during the upward phase | N/s | Partly |
| `Concentric Mean Force` | Average total force during the upward phase | N | Yes |
| `Concentric Mean Force / BM` | Average upward-phase force relative to body mass | N/kg | Yes |
| `Concentric Mean Power` | Average power during the upward phase | W | Yes |
| `Concentric Mean Power / BM` | Average upward-phase power relative to body mass | W/kg | Yes |
| `Concentric Mean Velocity` | Average upward speed during the upward phase | m/s | Yes |
| `Concentric Peak Velocity` | Highest upward speed before take-off | m/s | Yes |
| `Concentric RFD` | How fast force rises from the bottom of the dip to the concentric peak force | N/s | Yes |
| `Concentric RFD - 100ms` | Rise in force over the first 100 ms of the upward phase | N/s | Yes |
| `Concentric RFD - 200ms` | Rise in force over the first 200 ms of the upward phase | N/s | Yes |
| `Concentric RFD - 50ms` | Rise in force over the first 50 ms of the upward phase | N/s | Yes |
| `Concentric RFD / BM` | Concentric RFD relative to body mass | N/s/kg | Yes |
| `Concentric RPD` | How fast power rises from the bottom of the dip to peak power | W/s | Yes |
| `Concentric RPD - 100ms` | Rise in power over the first 100 ms of the upward phase | W/s | Yes |
| `Concentric RPD - 50ms` | Rise in power over the first 50 ms of the upward phase | W/s | Yes |
| `Concentric RPD / BM` | Concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric RPD-100ms / BM` | 100 ms concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric RPD-50ms / BM` | 50 ms concentric RPD relative to body mass | W/s/kg | Yes |
| `Concentric Time to Peak Force` | Time from the bottom of the dip to the concentric peak force | ms | Yes |
| `Contraction Time` | Time from the first movement to leaving the ground | ms | Yes |
| `Countermovement Depth` | Any downward movement of the centre of mass after the start of the squat jump | cm | Yes |
| `Displacement at Take-off` | How far the centre of mass has risen from standing height at the moment of take-off | cm | Yes |
| `Flight Time` | Time in the air between take-off and landing | ms | Yes |
| `Force at Peak Power` | Force at the instant of peak power | N | Yes |
| `Movement Start to Peak Force` | Time from first movement to peak force | s | Yes |
| `Movement Start to Peak Power` | Time from first movement to peak power | s | Yes |
| `P1 Concentric Impulse` | Net impulse in the first half (by time) of the upward phase | N s | Yes |
| `P2 Concentric Impulse` | Net impulse in the second half (by time) of the upward phase | N s | Yes |
| `P2 Concentric Impulse:P1 Concentric Impulse` | How the upward push is split between the second and first halves | Unitless | Yes |
| `Peak Net Take-off Force / BM` | Peak force above body weight, relative to body mass | N/kg | Yes |
| `Peak Power` | The highest power produced while pushing up | W | Yes |
| `Peak Power / BM` | Peak power relative to body mass | W/kg | Yes |
| `Peak Take-off Acceleration` | The highest upward acceleration of the centre of mass before take-off | m/s² | Yes |
| `Positive Impulse` | Net impulse over the whole rep | N s | Yes |
| `Jump Height (Flight Time)` | How high the athlete jumped, worked out from time in the air | cm | Partly |
| `Jump Height (Flight Time) in Inches` | The flight-time jump height expressed in inches | in | Yes |
| `Jump Height (FT) Relative Landing RFD` | Landing RFD per centimetre of jump height | N/s/cm | Yes |
| `Jump Height (FT) Relative Peak Landing Force` | Peak landing force per centimetre of jump height | N/cm | Yes |
| `Jump Height (Imp-Dis)` | The highest point the centre of mass reaches in the air, from double-integrated force | cm | Partly |
| `Jump Height (Imp-Mom)` | How high the centre of mass rises, worked out from take-off velocity | cm (glossary); in on some displays | Partly |
| `Jump Height (Imp-Mom) in Inches` | The Imp-Mom jump height expressed in inches | in | Yes |
| `Landing Impulse` | Total impulse from landing to peak landing force | N s | Yes |
| `Landing Net Peak Force / BM` | Peak landing force above body weight, relative to body mass | N/kg | Yes |
| `Landing RFD` | How fast force rises from landing to peak landing force | N/s | Yes |
| `Landing RFD 50ms` | Rise in force over the first 50 ms after landing | N/s | Yes |
| `Mean Landing Power` | Average power from landing to the end of the rep | W | Yes |
| `Peak Landing Acceleration` | Highest acceleration of the centre of mass after landing | m/s² | Yes |
| `Peak Landing Force` | Highest force after landing | N | Yes |
| `Peak Landing Force / BM` | Peak landing force relative to body mass | N/kg | Yes |
| `Peak Landing Power` | Highest power from landing to the end of the rep | W | Partly |
| `Peak Landing Velocity` | Peak centre-of-mass velocity after landing | m/s | Partly |
| `Positive Take-off Impulse` | Net impulse from first movement to take-off | N s | Yes |
| `RSI-modified (Imp-Mom)` | Imp-Mom jump height per unit of contraction time | m/s | Yes |
| `RSI-modified` | Jump height per unit of time spent on the ground before take-off | m/s | Yes |
| `Take-off Peak Force` | The highest total force from first movement to take-off | N | Yes |
| `Take-off Peak Force / BM` | Take-off peak force relative to body mass | N/kg | Yes |
| `Total Work` | Area under the power curve from first movement to take-off | J | Yes |
| `Velocity at Peak Power` | Upward speed at the instant of peak power | m/s | Yes |
| `Vertical Velocity at Take-off` | Upward speed of the centre of mass when the feet leave the plates | m/s | Yes |
| `Landing Stiffness` | Landing force divided by how far the centre of mass sinks on landing | Not published | Partly |
| `Mean Landing Force` | Average force during the landing phase | Not published | Yes |
| `Take-off Momentum` | Body mass times take-off velocity | Not published | Partly |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |
| `Athlete Standing Weight` | Weight estimated before each rep when the weighing step was skipped | Not published | Yes |

### Drop jump (DJ, SLDJ)

The blocks for this group are on [the squat jump and drop jump page](vald-forcedecks-nordbord-squat-jump-drop-jump.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `RSI (JH (Flight Time)/Contact Time)` | Jump height produced per unit of ground contact time | m/s | Yes |
| `RSI (Flight Time/Contact Time)` | Time in the air per unit of ground contact time | Unitless | Yes |
| `Contact Time` | Time on the plates between drop landing and take-off | s | Yes |
| `Jump Height (Imp-Mom)` | Rebound jump height worked out from take-off velocity | cm | Partly |
| `Jump Height (Imp-Mom) in Inches` | Imp-Mom rebound height in inches | in | Yes |
| `Jump Height (Flight Time)` | Rebound jump height worked out from time in the air | cm | Partly |
| `Jump Height (Flight Time) in Inches` | Flight-time rebound height in inches | in | Yes |
| `Jump Height (Imp-Dis)` | Highest point of the centre of mass in the air, from double-integrated force | cm | Yes |
| `Flight Time` | Time in the air after the rebound | ms | Yes |
| `Drop Height` | Height of the drop before landing | cm | Yes |
| `Effective Drop` | Drop height implied by how fast the athlete hits the plates | cm | Partly |
| `Vertical Velocity at Contact` | Downward speed of the centre of mass at drop landing | m/s | Partly |
| `Vertical Velocity at Take-off` | Upward speed at take-off | m/s | Partly |
| `Coefficient of Restitution` | Compares landing speed and take-off speed | Unitless | Yes |
| `Countermovement Depth` | How far the centre of mass sinks during ground contact | cm | Yes |
| `Displacement at Take-off` | Centre-of-mass position at take-off relative to drop landing | cm | Yes |
| `Eccentric Duration` | Time from drop landing to the lowest point | ms | Yes |
| `Concentric Duration` | Time from the lowest point to take-off | ms | Yes |
| `Eccentric Impulse` | Net impulse while absorbing the landing | N s | Yes |
| `Concentric Impulse` | Net impulse while pushing up | N s | Yes |
| `Concentric Impulse (Abs) / BM` | Total push impulse relative to body mass | N s/kg | Yes |
| `Eccentric Mean Force` | Average force while absorbing | N | Yes |
| `Concentric Mean Force` | Average force while pushing up | N | Yes |
| `Eccentric:Concentric Mean Force Ratio` | Absorbing force compared with pushing force | % | Partly |
| `Concentric Mean Power` | Average power while pushing up | W | Yes |
| `Concentric Mean Power / BM` | Average push power relative to body mass | W/kg | Yes |
| `Concentric Mean Velocity` | Average upward speed while pushing | m/s | Yes |
| `Concentric Peak Velocity` | Highest upward speed before take-off | m/s | Yes |
| `Force at Zero Velocity` | Force at the lowest point of contact | N | Yes |
| `Force at Zero Velocity / BM` | Force at the lowest point relative to body mass | N/kg | Yes |
| `Peak Impact Force` | The first force spike after landing from the box | N | Yes |
| `Contact Trough` | Force at the dip between the impact spike and the drive-off peak | N | Yes |
| `Peak Drive-Off Force` | Highest force while pushing off | N | Yes |
| `Peak Drop Landing Force` | Highest force during ground contact | N | Yes |
| `Drop Landing RFD` | How fast force rises from drop landing to the landing peak | N/s | Yes |
| `Active Stiffness` | Drive-off force divided by how far the centre of mass sinks | N/m | Yes |
| `Active Stiffness Index` | Active stiffness scaled by drop height and body weight | Unitless | Partly |
| `Passive Stiffness` | Impact force divided by how far the centre of mass sinks | N/m | Yes |
| `Passive Stiffness Index` | Passive stiffness scaled by drop height and body weight | Unitless | Partly |
| `Movement Start to Peak Power` | Time from drop landing to peak power | s | Yes |
| `Peak Take-off Acceleration` | Highest upward acceleration during contact | m/s² | Yes |
| `Positive Impulse` | Net impulse over the rep from drop landing on | N s | Yes |
| `Positive Take-off Impulse` | Net impulse across the contact | N s | Yes |
| `Peak Power` | Highest power while pushing up | W | Yes |
| `Peak Power / BM` | Peak power relative to body mass | W/kg | Yes |
| `Peak Landing Force` | Highest force on the final landing | N | Yes |
| `Landing Net Peak Force / BM` | Peak landing force above body weight, relative to body mass | N/kg | Yes |
| `Landing RFD` | How fast force rises from landing to the landing peak | N/s | Yes |
| `Jump Height (FT) Relative Landing RFD` | Landing RFD per centimetre of jump height | N/s/cm | Yes |
| `Jump Height (FT) Relative Peak Landing Force` | Peak landing force per centimetre of jump height | N/cm | Yes |
| `Mean Landing Acceleration` | Average acceleration after landing | m/s² | Yes |
| `Mean Landing Power` | Average power after landing | W | Yes |
| `Mean Landing Velocity` | Average centre-of-mass velocity after landing | m/s | Yes |
| `Peak Landing Acceleration` | Highest acceleration after landing | m/s² | Yes |
| `Peak Landing Power` | Highest power after landing | W | Partly |
| `Peak Landing Velocity` | Peak velocity after landing | m/s | Partly |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Countermovement rebound jump (CMRJ, SLCMRJ)

The blocks for this group are on [the rebound, hop, and landing tests page](vald-forcedecks-nordbord-rebound-hop-landing.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `First Jump Height (Imp-Mom)` | Height of the first (countermovement) jump from take-off velocity | cm | Partly |
| `Rebound Jump Height (Imp-Mom)` | Height of the rebound jump from take-off velocity | cm | Partly |
| `Rebound Jump Height (Flight Time)` | Height of the rebound jump from time in the air | cm | Partly |
| `Rebound Contact Time` | Ground contact time between the first landing and the rebound take-off | ms | Yes |
| `Rebound RSI (JH (Flight Time) / Contact Time)` | Rebound jump height per unit of rebound contact time | Not published | Yes |
| `Takeoff Peak Power / BM` | Peak power of the first jump relative to body mass | Not published | Partly |
| `Peak Drop Landing Force` | Left versus right difference in landing force on the first landing | Not published | Partly |
| `Peak Landing Force` | Left versus right difference in landing force on the second landing | Not published | Partly |
| `Takeoff Eccentric Deceleration Peak Force` | Highest force while decelerating before the first take-off | Not published | Yes |
| `Takeoff Eccentric Deceleration Peak Force / BW` | Deceleration peak force normalised to body weight | Not published | Partly |
| `Takeoff Concentric Impulse:Eccentric Deceleration Impulse Ratio` | Push impulse compared with deceleration impulse, first jump | Not published | Yes |
| `Takeoff Eccentric Acceleration Phase Duration` | Time from first movement to the fastest downward speed | Not published | Yes |
| `Takeoff Eccentric Deceleration Phase Duration` | Time from fastest downward speed to the bottom of the dip | Not published | Yes |
| `Takeoff Concentric Phase:Contraction Time Ratio` | Share of first-jump contraction time spent pushing up | % | Yes |
| `Takeoff Eccentric Deceleration:Contraction Time Ratio` | Share of first-jump contraction time spent decelerating | % | Yes |
| `Takeoff Eccentric Unloading Phase:Contraction Time Ratio` | Share of first-jump contraction time spent unloading | % | Yes |
| `Takeoff Eccentric Yielding Phase:Contraction Time Ratio` | Share of first-jump contraction time spent yielding | % | Yes |
| `Takeoff Eccentric Acceleration Phase:Contraction Time Ratio` | Share of first-jump contraction time spent accelerating downward | % | Yes |
| `Eccentric Deceleration Mean Power` | Average power while decelerating | Not published | Yes |
| `Eccentric Deceleration Mean Power / BM` | Deceleration mean power relative to body mass | Not published | Yes |
| `Eccentric Deceleration Mean Velocity` | Average downward speed while decelerating | Not published | Yes |
| `Take-off Momentum` | Body mass times take-off velocity | Not published | Yes |
| `Mean Landing Force` | Average force during landing | Not published | Yes |
| `Landing Stiffness` | Landing force divided by how far the centre of mass sinks | Not published | Yes |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Hop tests (HJ, SLHJ)

The blocks for this group are on [the rebound, hop, and landing tests page](vald-forcedecks-nordbord-rebound-hop-landing.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Mean RSI (Jump Height / Contact Time)` | Average reactive strength index across the best hops | Not published | Yes |
| `Mean Jump Height (Flight Time)` | Average flight-time hop height across the best hops | cm | Yes |
| `Mean Contact Time` | Average ground contact time across the best hops | ms | Yes |
| `Mean Impulse` | Average impulse per hop across the best hops | Ns | Partly |
| `Best Reactive Strength Index (RSI)` | The highest RSI of any single hop | Not published | Yes |
| `RSI (Flight Time/Contact Time)` | Flight time divided by contact time | Unitless | Partly |
| `Contact Time` | Time on the ground between hops | Not published | Yes |
| `Mean Active Stiffness` | Average stiffness of the hops | N/m | Partly |
| `Peak Force` | Highest force across the hop test | N | Yes |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Hop and Return (SLHAR)

The blocks for this group are on [the rebound, hop, and landing tests page](vald-forcedecks-nordbord-rebound-hop-landing.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Contact Time` | Time on the plates during the hop and return | s | Partly |
| `Peak First Landing Force` | Highest force on the first landing | N | Yes |
| `Peak Takeoff Force` | Highest force during the second take-off | N | Yes |
| `Time to Stabilization` | Time from landing until force settles | s | Partly |
| `Eccentric Duration` | Length of the absorbing phase | ms | Not published |
| `Concentric Duration` | Length of the pushing phase | ms | Not published |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Land and Hold (LAH, SLLAH)

The blocks for this group are on [the rebound, hop, and landing tests page](vald-forcedecks-nordbord-rebound-hop-landing.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Time to Stabilization` | Time from landing until the athlete is still | s | Yes |
| `Peak Drop Landing Force` | Highest force during the landing | N | Yes |
| `Peak Drop Landing Force / BW` | Peak landing force relative to body size | N/kg | Yes |
| `Peak Landing Force` | Highest force produced on landing | N | Yes |
| `Stability Depth` | How low the centre of mass sits once the athlete is stable | Not published | Yes |
| `Peak Drop Landing Acceleration` | Highest acceleration during the landing | Not published | Yes |
| `Mean Drop Landing Acceleration` | Average acceleration during the landing | Not published | Yes |
| `Peak Drop Landing Velocity` | Peak velocity during the landing | Not published | Partly |
| `Peak Drop Landing Power` | Peak power during the landing | Not published | Yes |
| `Passive Stiffness` | Impact force divided by how far the centre of mass sinks | Not published | Yes |
| `Landing Stiffness` | Landing force divided by displacement at the lowest point | Not published | Yes |
| `Drop Landing RFD` | How fast force rises from landing to the landing peak | Not published | Yes |
| `Drop Landing` | The time at which the drop landing occurred | s | Not published |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Squat assessment (SQT, SLSQT)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Squat Depth` | How far the centre of mass drops in the squat | cm | Yes |
| `Maximum Negative Displacement` | Lowest point the centre of mass reaches | cm | Yes |
| `Eccentric Peak Velocity` | Fastest downward speed in the squat | m/s | Yes |
| `Eccentric Mean Velocity` | Average downward speed | m/s | Yes |
| `Concentric Mean Velocity` | Average upward speed | m/s | Yes |
| `Concentric Peak Velocity` | Highest upward speed | m/s | Yes |
| `Peak Force` | Highest force across the rep | N | Yes |
| `Eccentric Peak Force` | Highest force on the way down | N | Yes |
| `Concentric Peak Force` | Highest force on the way up | N | Yes |
| `Eccentric Mean Force Asymmetry` | Left versus right difference in average force on the way down | % | Partly |
| `Concentric Mean Force Asymmetry` | Left versus right difference in average force on the way up | % | Partly |
| `Eccentric Impulse` | Net impulse on the way down | Ns | Partly |
| `Concentric Impulse` | Net impulse on the way up | Ns | Partly |
| `Eccentric Peak Power` | Highest power on the way down | W | Partly |
| `Concentric Peak Power / BM` | Highest upward power relative to body mass | W/kg | Not published |
| `Eccentric Deceleration Peak Force` | Highest force while slowing the descent | Not published | Yes |
| `Eccentric Deceleration Mean Force` | Average force while slowing the descent | Not published | Yes |
| `Eccentric Deceleration Peak Force / BW` | Deceleration peak force normalised to body weight | Not published | Partly |
| `Eccentric Deceleration Mean Power` | Average power while slowing the descent | Not published | Yes |
| `Eccentric Deceleration Mean Power / BM` | Deceleration mean power relative to body mass | Not published | Yes |
| `Eccentric Deceleration Mean Velocity` | Average speed while slowing the descent | Not published | Yes |
| `Additional Load` | External load used in the test | Not published | Partly |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Push up and plyometric push up (PUSHUPT, PPU)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Push Up Depth` | How far the body lowers in the push up | cm | Yes |
| `Eccentric Impulse – Asymmetry` | Left versus right difference in net impulse on the way down (PUSHUPT, PPU) | % | Partly |
| `Concentric Impulse – Asymmetry` | Left versus right difference in net impulse on the way up (PUSHUPT, PPU) | % | Partly |
| `Eccentric Mean Velocity` | Average downward speed | m/s | Yes |
| `Concentric Mean Velocity` | Average upward speed | m/s | Yes |
| `Eccentric Peak Force` | Highest force on the way down | N | Not published |
| `Concentric Peak Force` | Highest force on the way up | N | Not published |
| `Maximum Negative Displacement` | Lowest point reached | cm | Not published |
| `Push Up Height (Flight Time)` | How high the upper body rises in the plyometric push up, from time in the air | cm | Partly |
| `Takeoff Peak Force / BM` | Highest take-off force relative to body mass (PPU) | N/kg | Yes |
| `Peak Landing Force – Asymmetry` | Left versus right difference in peak landing force (PPU) | % | Partly |
| `Eccentric Deceleration Peak Force` | Highest force while slowing the descent (PUSHUPT, PPU) | Not published | Yes |
| `Eccentric Deceleration Mean Force` | Average force while slowing the descent (PUSHUPT) | Not published | Yes |
| `Eccentric Deceleration Mean Power` | Average power while slowing the descent (PUSHUPT) | Not published | Yes |
| `Eccentric Deceleration Mean Velocity` | Average speed while slowing the descent (PUSHUPT) | Not published | Yes |
| `Additional Load` | External load used in the push up | Not published | Partly |

### Sit to Stand to Sit (STSTS)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Time to Stand` | Time to stand up and settle | s | Yes |
| `Time to Sit` | Time to sit back down | s | Yes |
| `Mean Standing Force – Asymmetry` | Left versus right difference in average force while standing up | % | Partly |
| `Mean Sitting Force – Asymmetry` | Left versus right difference in average force while sitting down | % | Partly |
| `Peak Standing Force` | Highest force while standing up, per side | N | Not published |
| `Mean Standing RFD` | How quickly force rises while standing up | Not published | Partly |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### Balance tests (QSB, SLSB, SLROSB)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Total Excursion` | Total distance the centre of pressure travels | mm | Yes |
| `Mean Velocity` | Average speed of the centre of pressure | mm/s | Yes |
| `Area of CoP Ellipse` | Size of the area the centre of pressure covers | mm2 | Partly |
| `CoP Range, Medial-Lateral` | Side-to-side spread of the centre of pressure | mm | Partly |
| `CoP Range, Anterior-Posterior` | Front-to-back spread of the centre of pressure | mm | Partly |
| `Mean Force – Asymmetry` | Left versus right difference in average force during the Quiet Stand | % | Partly |

### Isometric tests (IMTP and others)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Peak Vertical Force` | The highest total force in the effort | N | Yes |
| `Peak Vertical Force / BM` | Peak force relative to body mass | N/kg | Yes |
| `Peak Vertical Force (Net of BW)` | Peak force above body weight | N | Partly |
| `Force at 100ms` | Force 100 ms after the effort starts | N | Yes |
| `Force @ 150ms` | Force 150 ms after the effort starts | N | Partly |
| `Force @ 200ms` | Force 200 ms after the effort starts | N | Partly |
| `RFD at 100ms` | How fast force rises over the first 100 ms | N/s | Yes |
| `RFD - 100-150` | Rate of force rise between 100 and 150 ms | N/s | Partly |
| `Start Time to 80% Net Peak Force` | Time to reach 80% of peak force above body weight | s | Yes |
| `Start Time to 80% Peak Force` | Time to reach 80% of peak force | s | Partly |
| `Start Time to Peak Force` | Time from effort start to peak force | s | Yes |
| `Absolute Impulse` | Total impulse over the effort | Ns | Partly |
| `Relative Peak Force` | Peak force relative to body size, used in the run-specific iso-push tests | Not published | Not published |
| `Impulse (Net of BW)` | Impulse above body weight | Not published | Not published |
| `Bodyweight in Kilograms` | The athlete's measured body mass | kg | Not published |
| `Bodyweight in Pounds` | The athlete's measured body mass in pounds | lb | Not published |

### General Force-Time Analysis (GFTA)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Peak Force` | Highest force in the marked range | N | Partly |
| `Minimum Force` | Lowest force in the marked range | N | Partly |
| `Standing Weight Asymmetry` | Left versus right weight bearing while standing | % | Partly |

### Cross-test ratios (DSI, EUR)

The blocks for this group are on [the squat, push-up, sit to stand, balance, isometric, and general tests page](vald-forcedecks-nordbord-squat-isometric-general.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Dynamic Strength Index (DSI)` | Ballistic peak force compared with isometric peak force | Ratio | Yes |
| `Eccentric Utilization Ratio (EUR)` | CMJ height compared with SJ height | Ratio | Yes |

### NordBord test metrics

The blocks for this group are on [the NordBord page](vald-forcedecks-nordbord-nordbord.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `leftMaxForce`, `rightMaxForce` | The highest force of any rep for each leg | N | Yes |
| `leftAvgForce`, `rightAvgForce` | The average of the rep peaks for each leg | N | Yes |
| `Imbalance (maximum force)` | Left versus right difference in maximum force | % | Partly |
| `Imbalance (average force)` | Left versus right difference in average force | % | Partly |
| `leftTorque`, `rightTorque` | Knee-flexor torque: force times the knee-to-hook lever | Nm | Yes |
| `leftImpulse`, `rightImpulse` | Area under the force curve while above the impulse threshold | Ns | Partly |
| `leftCalibration`, `rightCalibration` | A value stored with each test for each sensor; its meaning is not published | Not published | Partly |
| `leftRepetitions`, `rightRepetitions` | Number of reps detected per leg | count | Partly |
| `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `rightAvgForcePerKg` | Peak force relative to body mass | N/kg (inferred) | Not published |
| `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg` | Torque relative to body mass | N m/kg (inferred) | Partly |
| `leftMaxRFDNewtonsPerSecond`, `rightMaxRFDNewtonsPerSecond`, `leftAvgRFDNewtonsPerSecond`, `rightAvgRFDNewtonsPerSecond` | The fastest rise in force | N/s | Not published |
| `leftMinTimeToMaxForceSeconds`, `rightMinTimeToMaxForceSeconds`, `leftAvgTimeToMaxForceSeconds`, `rightAvgTimeToMaxForceSeconds` | Time to reach peak force | s | Partly |
| `leftMaxRFD50msNewtonsPerSecond`, `rightMaxRFD50msNewtonsPerSecond`, `leftAvgRFD50msNewtonsPerSecond`, `rightAvgRFD50msNewtonsPerSecond` | Rate of force rise over the first 50 ms of the rep | N/s | Not published |
| `leftMaxRFD100msNewtonsPerSecond`, `rightMaxRFD100msNewtonsPerSecond`, `leftAvgRFD100msNewtonsPerSecond`, `rightAvgRFD100msNewtonsPerSecond` | Rate of force rise over the first 100 ms of the rep | N/s | Not published |
| `leftMaxRFD150msNewtonsPerSecond`, `rightMaxRFD150msNewtonsPerSecond`, `leftAvgRFD150msNewtonsPerSecond`, `rightAvgRFD150msNewtonsPerSecond` | Rate of force rise over the first 150 ms of the rep | N/s | Not published |
| `leftMaxRFD200msNewtonsPerSecond`, `rightMaxRFD200msNewtonsPerSecond`, `leftAvgRFD200msNewtonsPerSecond`, `rightAvgRFD200msNewtonsPerSecond` | Rate of force rise over the first 200 ms of the rep | N/s | Not published |
| `leftMaxRFD250msNewtonsPerSecond`, `rightMaxRFD250msNewtonsPerSecond`, `leftAvgRFD250msNewtonsPerSecond`, `rightAvgRFD250msNewtonsPerSecond` | Rate of force rise over the first 250 ms of the rep | N/s | Not published |
| `leftMaxImpulse50msNewtonSeconds`, `rightMaxImpulse50msNewtonSeconds`, `leftAvgImpulse50msNewtonSeconds`, `rightAvgImpulse50msNewtonSeconds` | Impulse over the first 50 ms of the rep | N s | Not published |
| `leftMaxImpulse100msNewtonSeconds`, `rightMaxImpulse100msNewtonSeconds`, `leftAvgImpulse100msNewtonSeconds`, `rightAvgImpulse100msNewtonSeconds` | Impulse over the first 100 ms of the rep | N s | Not published |
| `leftMaxImpulse150msNewtonSeconds`, `rightMaxImpulse150msNewtonSeconds`, `leftAvgImpulse150msNewtonSeconds`, `rightAvgImpulse150msNewtonSeconds` | Impulse over the first 150 ms of the rep | N s | Not published |
| `leftMaxImpulse200msNewtonSeconds`, `rightMaxImpulse200msNewtonSeconds`, `leftAvgImpulse200msNewtonSeconds`, `rightAvgImpulse200msNewtonSeconds` | Impulse over the first 200 ms of the rep | N s | Not published |
| `leftMaxImpulse250msNewtonSeconds`, `rightMaxImpulse250msNewtonSeconds`, `leftAvgImpulse250msNewtonSeconds`, `rightAvgImpulse250msNewtonSeconds` | Impulse over the first 250 ms of the rep | N s | Not published |

### NordBord training mode metrics

The blocks for this group are on [the NordBord page](vald-forcedecks-nordbord-nordbord.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `totalRepsCompleted`, `totalRepsAboveThreshold`, `totalRepsInTargetZone` | How many eccentric reps were done, and how many crossed the threshold or entered the target zone | count | Not published |
| `totalImpulseInTargetZoneNewtonSeconds`, `leftImpulseInTargetZoneNewtonSeconds`, `rightImpulseInTargetZoneNewtonSeconds` | Impulse produced while force was inside the target zone | N s | Not published |
| `totalImpulseInTargetZoneAsymmetryPercentage` | Left-right difference in target-zone impulse | % | Not published |
| `totalDurationInTargetZoneSeconds`, `durationInTargetZoneSeconds`, `leftTimeInTargetZoneSeconds`, `rightTimeInTargetZoneSeconds` | Time spent inside the target zone | s | Not published |
| `totalImpulseAboveThresholdNewtonSeconds`, `leftImpulseAboveThresholdNewtonSeconds`, `rightImpulseAboveThresholdNewtonSeconds` | Impulse produced while force was above the training threshold | N s | Not published |
| `totalImpulseAboveThresholdAsymmetryPercentage` | Left-right difference in impulse above threshold | % | Not published |
| `totalDurationAboveThresholdSeconds`, `durationAboveThresholdSeconds`, `leftTimeAboveThresholdSeconds`, `rightTimeAboveThresholdSeconds` | Time spent above the training threshold | s | Not published |
| `leftImpulseBelowThresholdNewtonSeconds`, `rightImpulseBelowThresholdNewtonSeconds`, `leftTimeBelowThresholdSeconds`, `rightTimeBelowThresholdSeconds`, `durationBelowThresholdSeconds` | Impulse and time while force was below the training threshold | N s, s | Not published |
| `leftImpulseBeforePeakNewtonSeconds`, `rightImpulseBeforePeakNewtonSeconds`, `leftImpulseAfterPeakNewtonSeconds`, `rightImpulseAfterPeakNewtonSeconds`, `leftImpulseAboveThresholdBeforePeakNewtonSeconds`, `rightImpulseAboveThresholdBeforePeakNewtonSeconds`, `leftImpulseAboveThresholdAfterPeakNewtonSeconds`, `rightImpulseAboveThresholdAfterPeakNewtonSeconds` | Impulse split at the moment of peak force, overall and above threshold | N s | Not published |
| `leftPeakForceNewtons`, `rightPeakForceNewtons`, `timeToPeakSeconds`, `leftTimeToPeakSeconds`, `rightTimeToPeakSeconds`, `repDurationSeconds` | Peak force and timing of each training rep | N, s | Not published |
| `leftImpulseEntireRepNewtonSeconds`, `rightImpulseEntireRepNewtonSeconds` | Impulse over the whole training rep | N s | Not published |
| `exceededTrainingThreshold`, `enteredTargetZone` | Whether the rep crossed the threshold or entered the target zone | Boolean | Not published |
| `timeInZoneLeft`, `timeInZoneRight` | Time each leg held force inside the isometric training zone | Not published | Not published |
| `impulseLeft`, `impulseRight` | Impulse produced in isometric training | Not published | Not published |
| `stabilityLeft`, `stabilityRight` | How steady force stayed during isometric training | Not published | Not published |
| `totalRepetitions`, `repNumber` | Number of isometric training reps | count | Partly |

## Event and term glossary

### Measured signals and sampling

- Force plates measure only force and time; ForceDecks derives body mass, impulse, acceleration, velocity, power and displacement from them ([Understanding ForceDecks test metrics](https://support.vald.com/hc/en-au/articles/4999090004633-Understanding-ForceDecks-test-metrics), [User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- ForceDecks samples force at up to 1,000 Hz ([User Guide p.4](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); the default is 1,000 Hz ([User Guide p.103](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- The ForceDecks raw data export contains time, left force and right force ([Export ForceDecks Results - Raw Data](https://support.vald.com/hc/en-au/articles/4998953955609-Export-ForceDecks-Results-Raw-Data-Excel)). The API recording example also has centre-of-pressure columns (`COPX Left`, `COPY Left`, `COPX Right`, `COPY Right`); the API guide does not say which tests include them ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- Integration drift is limited by starting a fresh integration before each rep and sampling at 1,000 Hz ([How ForceDecks Minimize Integration Drift](https://valdperformance.com/news/how-forcedecks-minimize-integration-drift)).

### Body weight and body mass

- Body mass and body weight: the glossary defines body mass (`BM`) as the mass measured during weighing, in kg, and body weight (`BW`) as the mass captured during the Weigh Profile stage, in N ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Weighing rule: the athlete stands still until the stability indicator stays green and weight fluctuates by no more than ±0.1 kg ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). Talking, looking around and chewing gum change the weight ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)).
- If weighing is skipped, ForceDecks estimates weight from the still period before each rep ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks), [Weighing profiles in ForceDecks iOS](https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS)). The API then shows `weight` as -1 and stores the estimate in `Athlete Standing Weight` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- Auto-weight settings: minimum weight, maximum standard deviation, steady period, maximum weight deviation ([Manage ForceDecks iOS app settings](https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings), [Weight Settings in ForceDecks Jump](https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump)).
- Loaded tests: weigh without the load; ForceDecks gets the load by subtracting body weight from the resting weight before each rep ([Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load)).
- System weight is the total weight on the plates: body weight, body weight plus load, or limb weight in single-limb isometric tests ([User Guide p.103](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- Isometric tests with only part of the body on the plates: weigh relaxed in the test position ([ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test)).
- Zero the plates with nothing on them before weighing ([Zeroing ForceDecks](https://support.vald.com/hc/en-au/articles/5000438165785-Zeroing-ForceDecks)).

### Start of movement (SoM)

- Glossary: start of movement is the moment force leaves its steady state, and the glossary says three detection methods are available ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Default method: total force moves ±20 N from measured body weight, working backwards from when the movement is known to have begun ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)).
- Other methods ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)):
  - 50 ms moving average of force moves ±20 N from body weight, working backwards.
  - Force moves ±20 N from body weight, working forwards from the start of the trial.
  - 50 ms moving average, working forwards from the start of the trial.
  - Standard deviation method: find the 1 s quiet period with the lowest force SD within a 3 s search window, then detect a ±(5 × SD) deviation; falls back to the default when no quiet period exists.
  - Yank method: force smoothed with a 5 Hz 4th order Butterworth filter, yank rectified and differentiated; SoM is where the derivative of yank deviates from zero; force must be within 10% of body weight.
- These settings apply to CMJ, LCMJ, SJ, LSJ, ABCMJ and SLJ ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)). The User Guide says the default is 20 N for every test ([User Guide p.6](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- Different SoM methods change timing metrics such as eccentric duration ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)).
- Isometric tests: SoM is the point where the exercise commences ([User Guide p.70](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)); Windows lets you pick an SoM method for isometric tests ([ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes)). The isometric detection rule is not published.

### Start of integration (SoI)

- ForceDecks integrates force and acceleration to get velocity, height and impulse. Integration must start when the athlete is completely still ([Customise Start of Integration Analysis](https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis)).
- Methods: integrate from start of movement (default), from a period before SoM, from a stable point before SoM, or from start of trial ([Customise Start of Integration Analysis](https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis)).
- A positive impulse before SoM (for example a heel raise) means velocity is already positive at SoM and displacement and jump height are wrong ([User Guide p.12](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

### Take-off and landing

- Take-off: the glossary defines it as the point where vertical force falls below 20 N after start of movement. Landing is the point where vertical force rises above 20 N after take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). The User Guide uses 20 N ([User Guide p.13](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- Conflict: the knowledge base CMJ and SJ pages state take-off below 30 N and landing above 30 N ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump), [Key Moments and Phases of a Squat Jump](https://support.vald.com/hc/en-au/articles/4999709811737-Key-Moments-and-Phases-of-a-Squat-Jump)). The worked example further down this page shows how 20 N versus 30 N changes the result.
- Drop landing (DJ): the point where force exceeds a 20 N threshold ([Glossary V2.0 p.10](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).

### CMJ phases

- Eccentric phase: start of movement to minimum displacement (zero velocity) ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). VALD notes muscles are not only lengthening in this phase, so it is also called the downward phase ([The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- Unloading sub-phase: start of movement to minimum force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump), [Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)).
- Eccentric braking phase: minimum eccentric force to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). It contains the yielding and deceleration sub-phases ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)).
- Yielding sub-phase: minimum force to eccentric peak velocity; added to ForceDecks in 2025 ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- Eccentric deceleration phase: from the moment just before vertical acceleration turns positive (the point of maximum negative velocity) to zero velocity ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Elsewhere in the literature this window is called the braking phase ([The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- Eccentric acceleration phase: start of movement to maximum negative velocity, which is unloading plus yielding ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- Concentric phase: zero velocity to take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). Phase 1 and Phase 2 are the first and second 50% of the concentric phase by time ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)).
- Flight: take-off to landing. Landing phase: landing to end of rep ([Introducing the Yielding Phase and New Metrics in ForceDecks](https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks)). VALD does not publish the end-of-rep rule for jumps.
- Start of max RFD: point of steepest concentric force. End of max RFD: peak take-off force ([Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).

### Other test events

- Squat assessment: start of rep, start of deceleration (peak negative velocity), start of concentric (zero velocity), end of rep (force returns to system weight) ([Key Moments and Phases of a Squat Assessment](https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment)).
- Land and Hold: stabilised when force stays within a 15 N standard deviation for 0.5 s ([Key Moments of a Land and Hold Test](https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test)).
- Hop test: best hop is the hop with the highest RSI; best 5 hops are the five highest ([Key Moments and Phases of a Hop Test](https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test)).
- Drop jump: peak impact force, contact trough, start of concentric, peak drive-off force ([Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump)).

### Calculation terms

- Asymmetry: the glossary formula subtracts the right metric value from the left metric value, divides by the larger of the two values, and multiplies by 100 ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)). In symbols (restatement): `(Left - Right) / max(Left, Right) × 100`. A positive value means left is higher (restatement of the sign of the formula).
- Absolute impulse: area under the force curve over a time period. Net impulse: area under the force curve above body weight. Positive impulse: area from start of movement to take-off, only above body weight ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- RFD: the change in force over a given time period or phase, in N/s. RPD: the change in power over a given time period or phase, in W/s ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Mean: the average of all data points in a dataset or phase, counting the start and end points of the phase ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Power: force times velocity ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Left metric and right metric: calculated from the left or right plate force only ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).

### How metrics appear in exports and the API

- Each trial has a `limb` value: `Both` for bilateral tests such as a CMJ, or `Left` or `Right` for single-limb tests ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- Each trial result has a `limb` value. Metrics from combined left and right force (for example jump height) have one result with `limb` = `Both`; metrics with separate left and right forces have `Trial`, `Left`, `Right` and `Asym` entries ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- Tests with several repeats in one trial (for example squats) report each repeat with a zero-based `repeat` number ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- A result definition has `resultIdString`, `resultName`, `resultDescription`, `resultGroup`, `supportsAsymmetry`, `isRepeatResult`, `resultUnit`, `resultUnitName`, `resultUnitScaleFactor`, `numberOfDecimalPlaces` and `trendDirection` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- `value` is stored in the internal unit, typically SI. Multiply by `resultUnitScaleFactor` to get the display unit ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- `trendDirection` shows which direction VALD treats as good: `Positive`, `Negative` or `None` ([FD API guide](https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API)).
- Result groups: `None`, `General`, `EISPhases`, `EISVariables`, `Performance`, `Takeoff`, `Rebound`, `Landing`, `Balance`, `Functional`, `BestHop`, `BestNHops`, `Fatigue` ([FD API spec](https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json)).
- ForceDecks Windows export profiles group results into Performance, Asymmetry, and Left and Right Results ([ForceDecks Custom Reports and Export Profiles](https://support.vald.com/hc/en-au/articles/4998993975193-ForceDecks-Custom-Reports-and-Export-Profiles)). Some asymmetries exist only from single-limb tests, for example peak power asymmetry ([ForceDecks Custom Reports and Export Profiles](https://support.vald.com/hc/en-au/articles/4998993975193-ForceDecks-Custom-Reports-and-Export-Profiles)).
- VALD Hub Results Export includes Additional Load (LCMJ, LSJ, PUSHUPT, SLSQT, SQT) and Drop Height (DJ, SLDJ, LAH, SLLAH) from 2026-09-28 ([VALD Hub Release Notes, 2026-09-28](https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026)).
- VALD Hub lets each user show up to 20 performance and asymmetry metrics per test type ([Manage ForceDecks Display Metrics in VALD Hub](https://support.vald.com/hc/en-au/articles/4799435088409-Manage-F-orceDecks-D-isplay-Metrics-in-VALD-Hub)).

## Factors that change the numbers

Each metric block lists short factor names. This section gives the detail and sources for each factor.

### ForceDecks factors

- **Start of movement method and threshold:** The default is a 20 N deviation from body weight; VALD offers moving-average, forward-search, standard-deviation and yank-based alternatives, and changing the method changes timing metrics ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)).
- **Isometric start-of-movement detection:** VALD states it improved this detection and lets Windows users select a method, but does not publish the isometric rule ([ForceDecks Windows - Release Notes](https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes), [ForceDecks iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes)).
- **Start of integration setting:** The default is to integrate from start of movement. The athlete must be still at that point; a pre-jump positive impulse shifts velocity and displacement ([Customise Start of Integration Analysis](https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis), [User Guide p.12](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Body weight accuracy:** Movement during weighing changes body weight, which changes acceleration, velocity, displacement and power ([User Guide p.4](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)).
- **Body mass used to normalise:** The User Guide writes "Body Mass (BM) = F ÷ g" ([User Guide p.5](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Take-off threshold (20 N or 30 N):** The glossary and User Guide use 20 N; the knowledge base CMJ and SJ pages state 30 N ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).
- **Landing threshold and impacts during flight:** Landing threshold (20 N in the glossary, 30 N on the knowledge base CMJ page). An impact near the plates during flight can trigger landing early ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump), [Quick Data Quality Check in ForceDecks](https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks)).
- **Landing technique:** Landing with bent knees can inflate flight-time jump height ([Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump)).
- **Cueing and intent:** Velocity cues change eccentric peak velocity and the eccentric metrics that follow it ([The Power of EPV: Part 2](https://valdhealth.com/news/the-power-of-epv-part-2-context-is-key), [The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **Sampling rate:** ForceDecks samples at up to 1,000 Hz ([User Guide p.4](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [How ForceDecks Minimize Integration Drift](https://valdperformance.com/news/how-forcedecks-minimize-integration-drift)).
- **Which trial you report:** ForceDecks shows the average of trials by default and the maximum on request; VALD Hub tiles offer maximum, average and minimum ([Viewing Results in ForceDecks](https://support.vald.com/hc/en-au/articles/4998743584153-Viewing-Results-in-ForceDecks), [VALD Hub - Release Notes](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Foot placement and landing timing:** Uneven landing or stepping off a box with one leg first exaggerates asymmetry ([User Guide p.32](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Understanding the Countermovement Jump](https://valdperformance.com/news/understanding-the-countermovement-jump)).
- **External load:** For loaded tests ForceDecks subtracts body weight from the resting weight before each rep to get the load ([Performing a test in ForceDecks with external load](https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load)).
- **Drop technique and drop height:** Lowering the body before stepping off reduces the effective drop and contact behaviour ([User Guide p.32](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf), [Understanding the Drop Jump](https://valdhealth.com/news/understanding-the-drop-jump)).
- **Box height entry:** A wrong manual drop height creates a mismatch between flight-time and Imp-Mom jump height ([User Guide p.33](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Pretension:** Too little (under 50 N) affects start of movement detection; too much (over 100 N) affects validity; inconsistent pretension shifts all time-based values ([Explosive Strength: Understanding, assessing and applying early force metrics](https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics), [User Guide p.66](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Weighing position:** Weigh the athlete relaxed in the exact test position when only part of the body is on the plates ([ForceDecks Test Protocol - Isometric Test](https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test)).
- **Test length:** Total excursion scales with test duration; compare only equal-length tests ([Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics](https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics), [ForceDecks Test Protocol - Quiet Stand](https://support.vald.com/hc/en-au/articles/4999827454617-ForceDecks-Test-Protocol-Quiet-Stand)).
- **Test conditions:** Test conditions include eyes closed, a foam surface, or a secondary task ([Centre of Pressure Measurement with ForceDecks](https://support.vald.com/hc/en-au/articles/5000001373209-Centre-of-Pressure-Measurement-with-ForceDecks)).
- **Lifting a foot during the test:** Lifting a foot during the test makes centre of pressure jump and inflates the metrics ([User Guide p.60](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Detection of the event that starts the fixed window:** The window has a fixed length. The value depends on where the window starts, so start-event detection matters.
- **Slow descent (low eccentric peak velocity):** A slow eccentric phase lowers eccentric metrics even when the jump height is similar ([The Power of Eccentric Peak Velocity](https://valdhealth.com/news/the-power-of-epv-part-1)).
- **Changes in either term of the ratio:** A ratio can stay the same while both parts change, so check each part.
- **Number and style of hops:** Auto-analysis fails with fewer than 5 hops; knee bend during hops changes the test ([User Guide p.47](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- **Stability before and after the movement:** An unstable period causes displacement drift ([User Guide p.49](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).

### NordBord factors

- **Rep threshold:** A rep starts when force exceeds the rep threshold (example 150 N) and the app then looks for a peak ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds)).
- **Impulse threshold:** Impulse counts only while force is above it (example 25 N), which removes repositioning between reps ([NordBord Detection Thresholds](https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds), [What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure)).
- **Knee position setting:** Torque uses a lever length approximated from the knee position setting; the lookup is not published ([What Does NordBord Measure?](https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure), [Select a NordBord knee position](https://support.vald.com/hc/en-au/articles/4812416471065-Select-a-NordBord-knee-position)).
- **Sensor zeroing:** NordBord zeroes at start-up; an offset makes one trace lag or sit above 0 N ([How the NordBord Sensors Work](https://support.vald.com/hc/en-au/articles/4808553425689-How-the-NordBord-Sensors-Work)).
- **Hook alignment:** Hooks pushed into the sides of their sockets put bending load on the uniaxial sensors ([How the NordBord Sensors Work](https://support.vald.com/hc/en-au/articles/4808553425689-How-the-NordBord-Sensors-Work)).
- **Rep selection:** You can deselect unwanted reps before upload ([Understanding Results in the NordBord App](https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App), [Record a test in NordBord Windows](https://support.vald.com/hc/en-au/articles/4812175128985-Record-a-test-in-NordBord-Windows)).
- **Technique:** Hip hinging, stopping early, or toes digging into the pad change Nordic peak force ([VALD NordBord Test Guide p.6](https://support.vald.com/hc/en-au/article_attachments/17161683969817/VALD_NordBord_Test_Guide.pdf)).
- **Entered body weight:** Body weight entered in the app or pulled from VALD Hub ([NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Sampling rate:** The default is 50 Hz, up to 400 Hz on the spec sheet; the iOS app raised it to 400 Hz to capture new metrics ([NordBord Technical Specifications](https://support.vald.com/hc/en-au/article_attachments/29041300739609), [NordBord iOS - Release Notes](https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes)).
- **Joint angle consistency:** Knee and hip angle consistency for isometric tests ([VALD NordBord Test Guide p.11](https://support.vald.com/hc/en-au/article_attachments/17161683969817/VALD_NordBord_Test_Guide.pdf)).
- **Training threshold and target zone settings:** Defaults: threshold 80% of personal best or 250 N; target zone 90% of personal best or 300 N; isometric zone plus or minus 10% ([Create a training program in NordBord iOS](https://support.vald.com/hc/en-au/articles/37292091781657-Create-a-training-program-in-NordBord-iOS)).

## Conflicts in the vendor's own sources

VALD's own sources disagree in these places. Each conflict also appears next to the metric or setting it affects:

- Take-off and landing threshold: 20 N in the glossary and User Guide; 30 N on the knowledge base CMJ and SJ key-moment pages ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump), [Key Moments and Phases of a Squat Jump](https://support.vald.com/hc/en-au/articles/4999709811737-Key-Moments-and-Phases-of-a-Squat-Jump)).
- SJ concentric phase: start of movement to take-off in the glossary; zero velocity to take-off in the User Guide ([Glossary V2.0 p.14](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [User Guide p.27](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- Eccentric unloading window: start of movement to the start of the deceleration phase in the glossary metric table; start of movement to minimum force on the knowledge base ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Countermovement Jump](https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump)).
- Positive impulse: "only above body weight" from start of movement to take-off in the technical definitions; "net impulse during the entire repetition" in the CMJ table ([Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Contact trough: "Maximum Vertical Force" in the glossary; "lowest force point" on the knowledge base and in the User Guide ([Glossary V2.0 p.12](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Key Moments and Phases of a Drop Jump](https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump), [User Guide p.34](https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf)).
- Eccentric Peak Velocity unit printed as "Millisecond (m/s)" in the glossary ([Glossary V2.0 p.7](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- RSI-modified unit: m/s in the glossary; `-` on the default-metrics page ([Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- Contraction Time unit: ms in the glossary; s on the default-metrics page for SJ ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS)).
- Mean Impulse unit: Ns on the default-metrics page; N/s on the common-tests page ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Common tests and metrics for ForceDecks application](https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application)).
- RFD at 100ms: "during the first 100 milliseconds after movement starts" versus "slope of the force-time curve 100ms after the start of the test" ([Default metrics](https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS), [Updated ForceDecks Default Metrics for Streamlined Assessments](https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks)).
- NordBord asymmetry: the app formula is not published; a VALD research summary used `|L - R| / (L + R)`, which differs from the ForceDecks glossary formula ([Eccentric Hamstring Strength research summary](https://valdperformance.com/news/eccentric-hamstring-strength), [Glossary V2.0 p.3](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).

## Not published

VALD's public sources do not state these items. Each metric block marks the same gaps:

- The full list of exportable ForceDecks metrics. It sits behind the authenticated `/resultdefinitions` endpoint of the ForceDecks API.
- The value of gravity (`g`) that ForceDecks uses.
- The averaging window ForceDecks uses to estimate weight.
- The rule that detects the start of movement in isometric tests.
- The end-of-rep rule for jumps.
- The defaults for the NordBord rep and impulse thresholds.
- The NordBord knee-position lookup that sets the lever length for torque.
- The NordBord asymmetry formula in the app.
- The metric count for several tests: Hop and Return, push-up tests, Sit to Stand to Sit, General Force-Time Analysis, and NordBord.

These metrics have a VALD name from the API, release notes, protocols, or VALD articles, but VALD publishes no definition text for them. Their blocks mark the definition as Not published:

- Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ): `Eccentric Yielding Phase RFD`
- Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ): `Eccentric Yielding Phase RFD / BM`
- Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ): `Bodyweight in Kilograms`
- Countermovement jump (CMJ, LCMJ, ABCMJ, SLJ): `Bodyweight in Pounds`
- Squat jump (SJ, LSJ): `Bodyweight in Kilograms`
- Squat jump (SJ, LSJ): `Bodyweight in Pounds`
- Drop jump (DJ, SLDJ): `Bodyweight in Kilograms`
- Drop jump (DJ, SLDJ): `Bodyweight in Pounds`
- Countermovement rebound jump (CMRJ, SLCMRJ): `Bodyweight in Kilograms`
- Countermovement rebound jump (CMRJ, SLCMRJ): `Bodyweight in Pounds`
- Hop tests (HJ, SLHJ): `RSI (Flight Time/Contact Time)`
- Hop tests (HJ, SLHJ): `Bodyweight in Kilograms`
- Hop tests (HJ, SLHJ): `Bodyweight in Pounds`
- Hop and Return (SLHAR): `Eccentric Duration`
- Hop and Return (SLHAR): `Concentric Duration`
- Hop and Return (SLHAR): `Bodyweight in Kilograms`
- Hop and Return (SLHAR): `Bodyweight in Pounds`
- Land and Hold (LAH, SLLAH): `Drop Landing`
- Land and Hold (LAH, SLLAH): `Bodyweight in Kilograms`
- Land and Hold (LAH, SLLAH): `Bodyweight in Pounds`
- Squat assessment (SQT, SLSQT): `Concentric Peak Power / BM`
- Squat assessment (SQT, SLSQT): `Additional Load`
- Squat assessment (SQT, SLSQT): `Bodyweight in Kilograms`
- Squat assessment (SQT, SLSQT): `Bodyweight in Pounds`
- Push up and plyometric push up (PUSHUPT, PPU): `Eccentric Peak Force`
- Push up and plyometric push up (PUSHUPT, PPU): `Concentric Peak Force`
- Push up and plyometric push up (PUSHUPT, PPU): `Maximum Negative Displacement`
- Push up and plyometric push up (PUSHUPT, PPU): `Additional Load`
- Sit to Stand to Sit (STSTS): `Peak Standing Force`
- Sit to Stand to Sit (STSTS): `Bodyweight in Kilograms`
- Sit to Stand to Sit (STSTS): `Bodyweight in Pounds`
- Isometric tests (IMTP and others): `Peak Vertical Force (Net of BW)`
- Isometric tests (IMTP and others): `Force @ 150ms`
- Isometric tests (IMTP and others): `Force @ 200ms`
- Isometric tests (IMTP and others): `RFD - 100-150`
- Isometric tests (IMTP and others): `Relative Peak Force`
- Isometric tests (IMTP and others): `Impulse (Net of BW)`
- Isometric tests (IMTP and others): `Bodyweight in Kilograms`
- Isometric tests (IMTP and others): `Bodyweight in Pounds`
- General Force-Time Analysis (GFTA): `Peak Force`
- General Force-Time Analysis (GFTA): `Minimum Force`
- General Force-Time Analysis (GFTA): `Standing Weight Asymmetry`
- NordBord: `leftCalibration`, `rightCalibration`
- NordBord: `leftRepetitions`, `rightRepetitions`
- NordBord: `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `rightAvgForcePerKg`
- NordBord: `leftMaxTorquePerKg`, `rightMaxTorquePerKg`, `leftAvgTorquePerKg`, `rightAvgTorquePerKg`
- NordBord: `leftMaxRFDNewtonsPerSecond`, `rightMaxRFDNewtonsPerSecond`, `leftAvgRFDNewtonsPerSecond`, `rightAvgRFDNewtonsPerSecond`
- NordBord: `leftMinTimeToMaxForceSeconds`, `rightMinTimeToMaxForceSeconds`, `leftAvgTimeToMaxForceSeconds`, `rightAvgTimeToMaxForceSeconds`
- NordBord: `leftMaxRFD50msNewtonsPerSecond`, `rightMaxRFD50msNewtonsPerSecond`, `leftAvgRFD50msNewtonsPerSecond`, `rightAvgRFD50msNewtonsPerSecond`
- NordBord: `leftMaxRFD100msNewtonsPerSecond`, `rightMaxRFD100msNewtonsPerSecond`, `leftAvgRFD100msNewtonsPerSecond`, `rightAvgRFD100msNewtonsPerSecond`
- NordBord: `leftMaxRFD150msNewtonsPerSecond`, `rightMaxRFD150msNewtonsPerSecond`, `leftAvgRFD150msNewtonsPerSecond`, `rightAvgRFD150msNewtonsPerSecond`
- NordBord: `leftMaxRFD200msNewtonsPerSecond`, `rightMaxRFD200msNewtonsPerSecond`, `leftAvgRFD200msNewtonsPerSecond`, `rightAvgRFD200msNewtonsPerSecond`
- NordBord: `leftMaxRFD250msNewtonsPerSecond`, `rightMaxRFD250msNewtonsPerSecond`, `leftAvgRFD250msNewtonsPerSecond`, `rightAvgRFD250msNewtonsPerSecond`
- NordBord: `leftMaxImpulse50msNewtonSeconds`, `rightMaxImpulse50msNewtonSeconds`, `leftAvgImpulse50msNewtonSeconds`, `rightAvgImpulse50msNewtonSeconds`
- NordBord: `leftMaxImpulse100msNewtonSeconds`, `rightMaxImpulse100msNewtonSeconds`, `leftAvgImpulse100msNewtonSeconds`, `rightAvgImpulse100msNewtonSeconds`
- NordBord: `leftMaxImpulse150msNewtonSeconds`, `rightMaxImpulse150msNewtonSeconds`, `leftAvgImpulse150msNewtonSeconds`, `rightAvgImpulse150msNewtonSeconds`
- NordBord: `leftMaxImpulse200msNewtonSeconds`, `rightMaxImpulse200msNewtonSeconds`, `leftAvgImpulse200msNewtonSeconds`, `rightAvgImpulse200msNewtonSeconds`
- NordBord: `leftMaxImpulse250msNewtonSeconds`, `rightMaxImpulse250msNewtonSeconds`, `leftAvgImpulse250msNewtonSeconds`, `rightAvgImpulse250msNewtonSeconds`
- NordBord training: `totalRepsCompleted`, `totalRepsAboveThreshold`, `totalRepsInTargetZone`
- NordBord training: `totalImpulseInTargetZoneNewtonSeconds`, `leftImpulseInTargetZoneNewtonSeconds`, `rightImpulseInTargetZoneNewtonSeconds`
- NordBord training: `totalImpulseInTargetZoneAsymmetryPercentage`
- NordBord training: `totalDurationInTargetZoneSeconds`, `durationInTargetZoneSeconds`, `leftTimeInTargetZoneSeconds`, `rightTimeInTargetZoneSeconds`
- NordBord training: `totalImpulseAboveThresholdNewtonSeconds`, `leftImpulseAboveThresholdNewtonSeconds`, `rightImpulseAboveThresholdNewtonSeconds`
- NordBord training: `totalImpulseAboveThresholdAsymmetryPercentage`
- NordBord training: `totalDurationAboveThresholdSeconds`, `durationAboveThresholdSeconds`, `leftTimeAboveThresholdSeconds`, `rightTimeAboveThresholdSeconds`
- NordBord training: `leftImpulseBelowThresholdNewtonSeconds`, `rightImpulseBelowThresholdNewtonSeconds`, `leftTimeBelowThresholdSeconds`, `rightTimeBelowThresholdSeconds`, `durationBelowThresholdSeconds`
- NordBord training: `leftImpulseBeforePeakNewtonSeconds`, `rightImpulseBeforePeakNewtonSeconds`, `leftImpulseAfterPeakNewtonSeconds`, `rightImpulseAfterPeakNewtonSeconds`, `leftImpulseAboveThresholdBeforePeakNewtonSeconds`, `rightImpulseAboveThresholdBeforePeakNewtonSeconds`, `leftImpulseAboveThresholdAfterPeakNewtonSeconds`, `rightImpulseAboveThresholdAfterPeakNewtonSeconds`
- NordBord training: `leftPeakForceNewtons`, `rightPeakForceNewtons`, `timeToPeakSeconds`, `leftTimeToPeakSeconds`, `rightTimeToPeakSeconds`, `repDurationSeconds`
- NordBord training: `leftImpulseEntireRepNewtonSeconds`, `rightImpulseEntireRepNewtonSeconds`
- NordBord training: `exceededTrainingThreshold`, `enteredTargetZone`
- NordBord training: `timeInZoneLeft`, `timeInZoneRight`
- NordBord training: `impulseLeft`, `impulseRight`
- NordBord training: `stabilityLeft`, `stabilityRight`
- NordBord training: `totalRepetitions`, `repNumber`

## Worked example: CMJ from a synthetic force trace

This example builds a simplified CMJ force trace at 1,000 Hz for an 80 kg athlete and applies VALD's published rules. Every number in this section comes from the code output below.

Rules taken from VALD sources:

- Body weight comes from a still weighing period before the jump ([Weighing Profiles in ForceDecks](https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks)). The example uses the mean force of the first 1 s; VALD does not publish its averaging window.
- Start of movement: force moves more than 20 N from body weight ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)). The code searches forward from the start of the trial, which is one of VALD's optional methods; the VALD default searches backwards from when the movement is known to have begun ([Customise Start of Movement Analysis](https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis)). The code does not run the backward search.
- Integration starts at start of movement with zero velocity ([Customise Start of Integration Analysis](https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis)).
- Take-off: first sample below 20 N after start of movement. Landing: first sample above 20 N after take-off ([Glossary V2.0 p.4](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).
- Contraction time, flight time and both RSI-modified versions follow the glossary definitions ([Glossary V2.0 p.6](https://support.vald.com/hc/en-au/article_attachments/31552911571353), [Glossary V2.0 p.8](https://support.vald.com/hc/en-au/article_attachments/31552911571353)).

Assumptions VALD does not publish:

- `g = 9.81 m/s²`.
- `Jump Height (Imp-Mom) = v_TO² / (2 g)`.
- `Jump Height (Flight Time) = g × FT² / 8`.
- Trapezoid integration.

What the output shows:

- With the default rules, Imp-Mom and flight-time jump heights differ slightly, because each method uses different events.
- Switching the take-off and landing threshold from 20 N to 30 N (the value on the knowledge base CMJ page) moves take-off earlier and changes net impulse, take-off velocity, both jump heights and both RSI-modified values.
- A body weight 0.5% too heavy lowers net impulse, take-off velocity and Imp-Mom jump height, and moves the zero-velocity point, which changes eccentric and concentric durations and countermovement depth. Flight-time jump height does not change, because it uses only the take-off and landing events.

### Code

```python
"""Worked CMJ example: synthetic vertical force at 1000 Hz, analysed with VALD's published event rules.

Event rules used (VALD sources cited in the markdown file):
- Body weight: mean force during a still weighing period before the jump.
- Start of movement: total force moves 20 N away from body weight (VALD default threshold).
- Integration starts at start of movement with zero velocity (VALD default start of integration).
- Take-off: first sample after start of movement where force drops below 20 N (glossary V2.0).
- Landing: first sample after take-off where force rises above 20 N (glossary V2.0).
Assumptions that VALD does not publish (flagged in the markdown):
- g = 9.81 m/s^2.
- Jump Height (Imp-Mom) = v_takeoff^2 / (2 g).
- Jump Height (Flight Time) = g * FT^2 / 8.
- Trapezoid integration.
"""
import numpy as np

FS = 1000            # samples per second
DT = 1.0 / FS
G = 9.81             # m/s^2, assumed
MASS = 80.0          # kg, synthetic athlete


def ramp(tau, T):
    """Smooth 0 -> 1 ramp over T seconds."""
    return 0.5 * (1.0 - np.cos(np.pi * tau / T))


def build_force():
    """Build a simplified CMJ force trace from a piecewise acceleration profile."""
    seg = []  # list of acceleration arrays

    def t_axis(T):
        return np.arange(0, T, DT)

    # 1. Quiet standing (weighing) 1.0 s
    seg.append(np.zeros(len(t_axis(1.0))))
    # 2. Unloading 0.30 s: CoM accelerates downward
    T = 0.30; tau = t_axis(T)
    seg.append(-6.0 * np.sin(np.pi * tau / T))
    dv_unload = -6.0 * 2 * T / np.pi
    # 3. Braking 0.25 s: brings downward velocity back to zero
    T = 0.25; tau = t_axis(T)
    a_brake = -dv_unload * np.pi / (2 * T)
    seg.append(a_brake * np.sin(np.pi * tau / T))
    # 4. Propulsion 0.30 s
    T = 0.30; tau = t_axis(T)
    seg.append(13.6 * np.sin(np.pi * tau / T))
    # 5. Force falls from body weight to zero over 0.10 s (late concentric)
    T = 0.10; tau = t_axis(T)
    seg.append(-G * ramp(tau, T))
    a_pre = np.concatenate(seg)
    v_pre = np.concatenate([[0.0], np.cumsum((a_pre[1:] + a_pre[:-1]) / 2) * DT])
    v_end = v_pre[-1]
    # 6. Flight: free fall until CoM returns to take-off height
    ft_true = 2 * v_end / G
    seg.append(np.full(int(round(ft_true * FS)), -G))
    # 7. Landing 0.40 s: force rises from zero, arrests downward velocity, returns to body weight
    T = 0.40; tau = t_axis(T)
    B = (v_end + G * T / 2) * np.pi / (2 * T)
    seg.append(-G * (1 - ramp(tau, T)) + B * np.sin(np.pi * tau / T))
    # 8. Quiet standing 1.0 s
    seg.append(np.zeros(len(t_axis(1.0))))
    a = np.concatenate(seg)
    force = MASS * (G + a)
    force[force < 0] = 0.0
    return force


def analyse(force, sm_threshold=20.0, flight_threshold=20.0, bw_error=0.0):
    t = np.arange(len(force)) * DT
    # Body weight from the 1.0 s weighing period
    bw = force[:1000].mean() * (1 + bw_error)
    bm = bw / G
    # Start of movement: first sample where |F - BW| > threshold
    som = int(np.argmax(np.abs(force - bw) > sm_threshold))
    # Take-off: first sample after SoM where F < threshold
    to = som + int(np.argmax(force[som:] < flight_threshold))
    # Landing: first sample after take-off where F > threshold
    land = to + int(np.argmax(force[to:] > flight_threshold))
    # Integration from SoM with zero initial velocity
    net = force[som:to + 1] - bw
    acc = net / bm
    vel = np.concatenate([[0.0], np.cumsum((acc[1:] + acc[:-1]) / 2) * DT])
    disp = np.concatenate([[0.0], np.cumsum((vel[1:] + vel[:-1]) / 2) * DT])
    net_impulse = np.trapezoid(net, dx=DT)
    v_to = net_impulse / bm
    jh_impmom = v_to ** 2 / (2 * G)
    ft = t[land] - t[to]
    jh_ft = G * ft ** 2 / 8
    ct = t[to] - t[som]
    # Phase boundaries for context
    i_min_v = int(np.argmin(vel))                      # eccentric peak velocity
    i_zero = i_min_v + int(np.argmax(vel[i_min_v:] >= 0))  # zero velocity
    return dict(
        bw=bw, bm=bm, som_s=t[som], to_s=t[to], land_s=t[land],
        net_impulse=net_impulse, v_to=v_to, jh_impmom=jh_impmom, ft=ft,
        jh_ft=jh_ft, ct=ct, rsi_mod=jh_ft / ct, rsi_mod_impmom=jh_impmom / ct,
        epv=vel[i_min_v], ecc_dur=i_zero * DT, con_dur=(len(vel) - 1 - i_zero) * DT,
        cmd=disp[i_zero], peak_force=force[som:to + 1].max(),
    )


def report(r, label):
    print(f"--- {label} ---")
    print(f"Body weight (BW)                 {r['bw']:9.2f} N")
    print(f"Body mass (BM = BW / g)          {r['bm']:9.3f} kg")
    print(f"Start of movement                {r['som_s']:9.3f} s")
    print(f"Take-off                         {r['to_s']:9.3f} s")
    print(f"Landing                          {r['land_s']:9.3f} s")
    print(f"Net impulse, SoM to take-off     {r['net_impulse']:9.2f} N s")
    print(f"Take-off velocity                {r['v_to']:9.3f} m/s")
    print(f"Jump Height (Imp-Mom)            {r['jh_impmom'] * 100:9.2f} cm")
    print(f"Flight Time                      {r['ft'] * 1000:9.0f} ms")
    print(f"Jump Height (Flight Time)        {r['jh_ft'] * 100:9.2f} cm")
    print(f"Contraction Time                 {r['ct'] * 1000:9.0f} ms")
    print(f"RSI-modified (JH FT / CT)        {r['rsi_mod']:9.3f} m/s")
    print(f"RSI-modified (Imp-Mom)           {r['rsi_mod_impmom']:9.3f} m/s")
    print(f"Eccentric Peak Velocity          {r['epv']:9.3f} m/s")
    print(f"Eccentric Duration               {r['ecc_dur'] * 1000:9.0f} ms")
    print(f"Concentric Duration              {r['con_dur'] * 1000:9.0f} ms")
    print(f"Countermovement Depth            {r['cmd'] * 100:9.2f} cm")
    print(f"Take-off Peak Force              {r['peak_force']:9.1f} N")


if __name__ == "__main__":
    f = build_force()
    print(f"Samples: {len(f)} at {FS} Hz ({len(f) / FS:.3f} s)")
    base = analyse(f)
    report(base, "Default rules: 20 N start of movement, 20 N take-off and landing")
    alt = analyse(f, flight_threshold=30.0)
    report(alt, "Sensitivity: 30 N take-off and landing threshold")
    heavy = analyse(f, bw_error=0.005)
    report(heavy, "Sensitivity: body weight measured 0.5% too heavy")
```

### Output

Run the code above with Python and NumPy to reproduce this output.

```text
Samples: 3782 at 1000 Hz (3.782 s)
--- Default rules: 20 N start of movement, 20 N take-off and landing ---
Body weight (BW)                    784.80 N
Body mass (BM = BW / g)             80.000 kg
Start of movement                    1.004 s
Take-off                             1.940 s
Landing                              2.384 s
Net impulse, SoM to take-off        176.37 N s
Take-off velocity                    2.205 m/s
Jump Height (Imp-Mom)                24.77 cm
Flight Time                            444 ms
Jump Height (Flight Time)            24.17 cm
Contraction Time                       936 ms
RSI-modified (JH FT / CT)            0.258 m/s
RSI-modified (Imp-Mom)               0.265 m/s
Eccentric Peak Velocity             -1.145 m/s
Eccentric Duration                     543 ms
Concentric Duration                    393 ms
Countermovement Depth               -31.49 cm
Take-off Peak Force                 1872.8 N
--- Sensitivity: 30 N take-off and landing threshold ---
Body weight (BW)                    784.80 N
Body mass (BM = BW / g)             80.000 kg
Start of movement                    1.004 s
Take-off                             1.938 s
Landing                              2.385 s
Net impulse, SoM to take-off        177.90 N s
Take-off velocity                    2.224 m/s
Jump Height (Imp-Mom)                25.20 cm
Flight Time                            447 ms
Jump Height (Flight Time)            24.50 cm
Contraction Time                       934 ms
RSI-modified (JH FT / CT)            0.262 m/s
RSI-modified (Imp-Mom)               0.270 m/s
Eccentric Peak Velocity             -1.145 m/s
Eccentric Duration                     543 ms
Concentric Duration                    391 ms
Countermovement Depth               -31.49 cm
Take-off Peak Force                 1872.8 N
--- Sensitivity: body weight measured 0.5% too heavy ---
Body weight (BW)                    788.72 N
Body mass (BM = BW / g)             80.400 kg
Start of movement                    1.004 s
Take-off                             1.940 s
Landing                              2.384 s
Net impulse, SoM to take-off        172.70 N s
Take-off velocity                    2.148 m/s
Jump Height (Imp-Mom)                23.52 cm
Flight Time                            444 ms
Jump Height (Flight Time)            24.17 cm
Contraction Time                       936 ms
RSI-modified (JH FT / CT)            0.258 m/s
RSI-modified (Imp-Mom)               0.251 m/s
Eccentric Peak Velocity             -1.154 m/s
Eccentric Duration                     566 ms
Concentric Duration                    370 ms
Countermovement Depth               -32.09 cm
Take-off Peak Force                 1872.8 N
```

## Arithmetic checks on numbers VALD publishes

These scripts check arithmetic on numbers quoted in VALD sources. Inputs come from the cited pages.

NordBord API example payloads ([NordBord API guide](https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API)): torque divided by max force gives the lever length the app used.

```python
"""Check VALD's published NordBord API example payloads (A guide to using the External NordBord API).
Torque / MaxForce gives the implied lever length in metres for each example test."""
examples = [
    ("Scenario 1 example, left",  64.13062500000001, 219.25),
    ("Scenario 1 example, right", 66.763125,         228.25),
    ("Scenario 2 example A, left",  126.80325000000002, 339.5),
    ("Scenario 2 example A, right", 126.89662500000001, 339.75),
    ("Scenario 2 example B, left",  48.55500000000001, 166.0),
    ("Scenario 2 example B, right", 47.53125000000001, 162.5),
]
for label, torque, max_force in examples:
    print(f"{label:30s} torque {torque:8.3f} N m / max force {max_force:7.2f} N = {torque / max_force:.4f} m")
# Scenario 5 example: per-kg values
lmf, lmt = 2.569277108433735, 0.7746370481927711
rmf, rmt = 2.4879518072289155, 0.7501174698795182
print(f"Scenario 5 left  MaxTorquePerKg / MaxForcePerKg = {lmt / lmf:.4f} m")
print(f"Scenario 5 right MaxTorquePerKg / MaxForcePerKg = {rmt / rmf:.4f} m")
```

```text
Scenario 1 example, left       torque   64.131 N m / max force  219.25 N = 0.2925 m
Scenario 1 example, right      torque   66.763 N m / max force  228.25 N = 0.2925 m
Scenario 2 example A, left     torque  126.803 N m / max force  339.50 N = 0.3735 m
Scenario 2 example A, right    torque  126.897 N m / max force  339.75 N = 0.3735 m
Scenario 2 example B, left     torque   48.555 N m / max force  166.00 N = 0.2925 m
Scenario 2 example B, right    torque   47.531 N m / max force  162.50 N = 0.2925 m
Scenario 5 left  MaxTorquePerKg / MaxForcePerKg = 0.3015 m
Scenario 5 right MaxTorquePerKg / MaxForcePerKg = 0.3015 m
```

RSI-modified table ([RSI-Mod Made Simple](https://valdperformance.com/news/rsi-mod-made-simple)) and DSI example ([Recalibrating DSI with the Isometric Belt Squat](https://valdperformance.com/news/recalibrating-dsi-with-the-isometric-belt-squat)):

```python
"""Arithmetic checks on numbers published by VALD (inputs quoted from VALD pages)."""
# RSI-Mod Made Simple table: jump height (cm) / contraction time (ms)
for jh_cm, ct_ms in [(29.1, 650), (29.2, 998)]:
    print(f"RSI-mod check: {jh_cm} cm / {ct_ms} ms = {(jh_cm / 100) / (ct_ms / 1000):.3f} m/s")
# Recalibrating DSI article: CMJ peak force / Iso Belt Squat peak force
print(f"DSI check: 2488 N / 6521 N = {2488 / 6521:.4f}")
```

```text
RSI-mod check: 29.1 cm / 650 ms = 0.448 m/s
RSI-mod check: 29.2 cm / 998 ms = 0.293 m/s
DSI check: 2488 N / 6521 N = 0.3815
```

## Sources

These are the public pages and documents behind the metric blocks. All were accessed on 2026-10-02:

- A guide to using the External ForceDecks API: <https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API>, accessed 2026-10-02.
- Common tests and metrics for ForceDecks application: <https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application>, accessed 2026-10-02.
- Centre of Pressure Measurement with ForceDecks: <https://support.vald.com/hc/en-au/articles/5000001373209-Centre-of-Pressure-Measurement-with-ForceDecks>, accessed 2026-10-02.
- Cheat sheet: Quadrant Plots (PDF): <https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/Quadrant_Plot_Natera.pdf>, accessed 2026-10-02.
- Default result metrics in ForceDecks iOS: <https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS>, accessed 2026-10-02.
- Quick Data Quality Check in ForceDecks: <https://support.vald.com/hc/en-au/articles/5000482837017-Quick-Data-Quality-Check-in-ForceDecks>, accessed 2026-10-02.
- ForceDecks Dynamic Strength Index (DSI) Reports: <https://support.vald.com/hc/en-au/articles/5000254279065-ForceDecks-Dynamic-Strength-Index-DSI-Reports>, accessed 2026-10-02.
- ForceDecks Custom Reports and Export Profiles: <https://support.vald.com/hc/en-au/articles/4998993975193-ForceDecks-Custom-Reports-and-Export-Profiles>, accessed 2026-10-02.
- External ForceDecks API specification (Swagger v2019q3): <https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json>, accessed 2026-10-02.
- VALD ForceDecks Technical Glossary V2.0, March 2024 (PDF on support.vald.com): <https://support.vald.com/hc/en-au/article_attachments/31552911571353>, accessed 2026-10-02.
- ForceDecks Technical Metric Glossary (knowledge base page): <https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary>, accessed 2026-10-02.
- VALD Hub Release Notes, 2026-09-28: <https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026>, accessed 2026-10-02.
- Export Test Data from VALD Hub: <https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub>, accessed 2026-10-02.
- Manage ForceDecks Display Metrics in VALD Hub: <https://support.vald.com/hc/en-au/articles/4799435088409-Manage-F-orceDecks-D-isplay-Metrics-in-VALD-Hub>, accessed 2026-10-02.
- VALD Hub - Release Notes: <https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes>, accessed 2026-10-02.
- ForceDecks iOS v3.3.0 Release Notes, 2026-07-01: <https://support.vald.com/hc/en-au/articles/59548906192537-ForceDecks-iOS-v3-3-0-Release-Notes-1-July-2026>, accessed 2026-10-02.
- ForceDecks iOS v3.4.0 Release Notes, 2026-07-27: <https://support.vald.com/hc/en-au/articles/60292611662361-ForceDecks-iOS-v3-4-0-Release-Notes-27-July-2026>, accessed 2026-10-02.
- ForceDecks iOS - Release Notes: <https://support.vald.com/hc/en-au/articles/29732555497241-ForceDecks-iOS-Release-Notes>, accessed 2026-10-02.
- Manage ForceDecks iOS app settings: <https://support.vald.com/hc/en-au/articles/4999639497753-Manage-ForceDecks-iOS-app-settings>, accessed 2026-10-02.
- Key Moments and Phases of a Countermovement Jump: <https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump>, accessed 2026-10-02.
- Key Moments and Phases of a Drop Jump: <https://support.vald.com/hc/en-au/articles/4999724187289-Key-Moments-and-Phases-of-a-Drop-Jump>, accessed 2026-10-02.
- Key Moments and Phases of a Hop Test: <https://support.vald.com/hc/en-au/articles/4999706431001-Key-Moments-and-Phases-of-a-Hop-Test>, accessed 2026-10-02.
- Key Moments of a Land and Hold Test: <https://support.vald.com/hc/en-au/articles/4999681991065-Key-Moments-of-a-Land-and-Hold-Test>, accessed 2026-10-02.
- Key Moments and Phases of a Squat Jump: <https://support.vald.com/hc/en-au/articles/4999709811737-Key-Moments-and-Phases-of-a-Squat-Jump>, accessed 2026-10-02.
- Key Moments and Phases of a Squat Assessment: <https://support.vald.com/hc/en-au/articles/4999722757401-Key-Moments-and-Phases-of-a-Squat-Assessment>, accessed 2026-10-02.
- Performing a test in ForceDecks with external load: <https://support.vald.com/hc/en-au/articles/5978399478041-Performing-a-test-in-ForceDecks-with-external-load>, accessed 2026-10-02.
- Understanding ForceDecks test metrics: <https://support.vald.com/hc/en-au/articles/4999090004633-Understanding-ForceDecks-test-metrics>, accessed 2026-10-02.
- Balance testing with ForceDecks: A beginner's guide to Centre of Pressure metrics (VALD Health): <https://valdhealth.com/news/balance-testing-beginners-guide-centre-of-pressure-metrics>, accessed 2026-10-02.
- Isometric Belt Squat: A practical alternative for lower-body strength testing (VALD Performance): <https://valdperformance.com/news/isometric-belt-squat-a-practical-alternative-for-lower-body-strength-testing>, accessed 2026-10-02.
- Understanding the Countermovement Jump (VALD Performance): <https://valdperformance.com/news/understanding-the-countermovement-jump>, accessed 2026-10-02.
- Updated ForceDecks Default Metrics for Streamlined Assessments (VALD Health): <https://valdhealth.com/news/smarter-defaults-for-aligned-decision-making-in-forcedecks>, accessed 2026-10-02.
- Understanding the Drop Jump (VALD Health): <https://valdhealth.com/news/understanding-the-drop-jump>, accessed 2026-10-02.
- How ForceDecks Minimize Integration Drift (VALD Performance): <https://valdperformance.com/news/how-forcedecks-minimize-integration-drift>, accessed 2026-10-02.
- Recalibrating DSI with the Isometric Belt Squat (VALD Performance): <https://valdperformance.com/news/recalibrating-dsi-with-the-isometric-belt-squat>, accessed 2026-10-02.
- Eccentric Hamstring Strength research summary (VALD Performance): <https://valdperformance.com/news/eccentric-hamstring-strength>, accessed 2026-10-02.
- The Power of Eccentric Peak Velocity (EPV): Part 1 (VALD Health): <https://valdhealth.com/news/the-power-of-epv-part-1>, accessed 2026-10-02.
- The Power of EPV: Part 2 (VALD Health): <https://valdhealth.com/news/the-power-of-epv-part-2-context-is-key>, accessed 2026-10-02.
- Understanding the Eccentric Utilization Ratio (VALD Performance): <https://valdperformance.com/news/understanding-the-eccentric-utilization-ratio-eur>, accessed 2026-10-02.
- Explosive Strength: Understanding, assessing and applying early force metrics (VALD Performance): <https://valdperformance.com/news/explosive-strength-understanding-assessing-and-applying-early-force-metrics>, accessed 2026-10-02.
- Understanding the Nordic Hamstring Exercise: Part 2 (VALD Health): <https://valdhealth.com/news/understanding-the-nordic-hamstring-exercise-part-2>, accessed 2026-10-02.
- Understanding Rate of Force Development (VALD Health): <https://valdhealth.com/news/understanding-rate-of-force-development>, accessed 2026-10-02.
- RSI-Mod Made Simple (VALD Performance): <https://valdperformance.com/news/rsi-mod-made-simple>, accessed 2026-10-02.
- Squat Assessment: Understanding kinetics and kinematics (VALD Health): <https://valdhealth.com/news/squat-assessment-understanding-kinetics-and-kinematics>, accessed 2026-10-02.
- The Sit-to-Stand Test (VALD Health): <https://valdhealth.com/news/the-sit-to-stand-test-a-key-assessment-tool-in-modern-rehabilitation-and-fitness>, accessed 2026-10-02.
- Introducing the Yielding Phase and New Metrics in ForceDecks (VALD Performance): <https://valdperformance.com/news/introducing-the-yielding-phase-and-new-metrics-in-forcedecks>, accessed 2026-10-02.
- A guide to using the External NordBord API: <https://support.vald.com/hc/en-au/articles/29364033087513-A-guide-to-using-the-External-NordBord-API>, accessed 2026-10-02.
- VALD NordBord Test Guide (PDF): <https://support.vald.com/hc/en-au/article_attachments/17161683969817/VALD_NordBord_Test_Guide.pdf>, accessed 2026-10-02.
- Record a test in NordBord iOS: <https://support.vald.com/hc/en-au/articles/30033699909017-Record-a-test-in-NordBord-iOS>, accessed 2026-10-02.
- Select a NordBord knee position: <https://support.vald.com/hc/en-au/articles/4812416471065-Select-a-NordBord-knee-position>, accessed 2026-10-02.
- What Does NordBord Measure?: <https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure>, accessed 2026-10-02.
- Understanding Results in the NordBord App: <https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App>, accessed 2026-10-02.
- NordBord iOS - Release Notes: <https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes>, accessed 2026-10-02.
- NordBord Technical Specifications (PDF): <https://support.vald.com/hc/en-au/article_attachments/29041300739609>, accessed 2026-10-02.
- How the NordBord Sensors Work: <https://support.vald.com/hc/en-au/articles/4808553425689-How-the-NordBord-Sensors-Work>, accessed 2026-10-02.
- External NordBord API specification (Swagger v1): <https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json>, accessed 2026-10-02.
- NordBord Detection Thresholds: <https://support.vald.com/hc/en-au/articles/4812436829593-NordBord-Detection-Thresholds>, accessed 2026-10-02.
- Create a training program in NordBord iOS: <https://support.vald.com/hc/en-au/articles/37292091781657-Create-a-training-program-in-NordBord-iOS>, accessed 2026-10-02.
- NordBord Test Types: <https://support.vald.com/hc/en-au/articles/4812656102169-NordBord-Test-Types>, accessed 2026-10-02.
- Record a test in NordBord Windows: <https://support.vald.com/hc/en-au/articles/4812175128985-Record-a-test-in-NordBord-Windows>, accessed 2026-10-02.
- ForceDecks Test Protocol - Countermovement Jump: <https://support.vald.com/hc/en-au/articles/4999886017817-ForceDecks-Test-Protocol-Countermovement-Jump>, accessed 2026-10-02.
- ForceDecks Test Protocol - Drop Jump: <https://support.vald.com/hc/en-au/articles/4999913990425-ForceDecks-Test-Protocol-Drop-Jump>, accessed 2026-10-02.
- ForceDecks Test Protocol - Hop Test: <https://support.vald.com/hc/en-au/articles/4999906960153-ForceDecks-Test-Protocol-Hop-Test>, accessed 2026-10-02.
- ForceDecks Test Protocol - Isometric Mid-Thigh Pull: <https://support.vald.com/hc/en-au/articles/7667730369817-ForceDecks-Test-Protocol-Isometric-Mid-Thigh-Pull>, accessed 2026-10-02.
- ForceDecks Test Protocol - Isometric Test: <https://support.vald.com/hc/en-au/articles/4999815982361-ForceDecks-Test-Protocol-Isometric-Test>, accessed 2026-10-02.
- ForceDecks Test Protocol - Land and Hold: <https://support.vald.com/hc/en-au/articles/4999895084185-ForceDecks-Test-Protocol-Land-and-Hold>, accessed 2026-10-02.
- ForceDecks Test Protocol - Plyometric Push Up: <https://support.vald.com/hc/en-au/articles/40661192006041-ForceDecks-Test-Protocol-Plyometric-Push-Up>, accessed 2026-10-02.
- ForceDecks Test Protocol - Push Up: <https://support.vald.com/hc/en-au/articles/4999827968665-ForceDecks-Test-Protocol-Push-Up>, accessed 2026-10-02.
- ForceDecks Test Protocol - Quiet Stand: <https://support.vald.com/hc/en-au/articles/4999827454617-ForceDecks-Test-Protocol-Quiet-Stand>, accessed 2026-10-02.
- ForceDecks Test Protocol - Run-Specific Knee Iso-Push: <https://support.vald.com/hc/en-au/articles/30764623490713-ForceDecks-Test-Protocol-Run-Specific-Knee-Iso-Push>, accessed 2026-10-02.
- ForceDecks Test Protocol - Squat Jump: <https://support.vald.com/hc/en-au/articles/7081508615321-ForceDecks-Test-Protocol-Squat-Jump>, accessed 2026-10-02.
- ForceDecks Test Protocol - Sit to Stand to Sit: <https://support.vald.com/hc/en-au/articles/6725192582425-ForceDecks-Test-Protocol-Sit-to-Stand-to-Sit>, accessed 2026-10-02.
- Export ForceDecks Results - Raw Data (Excel): <https://support.vald.com/hc/en-au/articles/4998953955609-Export-ForceDecks-Results-Raw-Data-Excel>, accessed 2026-10-02.
- Customise Start of Integration Analysis: <https://support.vald.com/hc/en-au/articles/5000087012505-Customise-Start-of-Integration-Analysis>, accessed 2026-10-02.
- Customise Start of Movement Analysis: <https://support.vald.com/hc/en-au/articles/5000196381209-Customise-Start-of-Movement-Analysis>, accessed 2026-10-02.
- VALD ForceDecks User Guide v2, November 2023 (PDF): <https://support.vald.com/hc/en-au/article_attachments/31298911123353/VALD%20ForceDecks%20User%20Guide%20v2.pdf>, accessed 2026-10-02.
- Viewing Results in ForceDecks: <https://support.vald.com/hc/en-au/articles/4998743584153-Viewing-Results-in-ForceDecks>, accessed 2026-10-02.
- Weighing Profiles in ForceDecks: <https://support.vald.com/hc/en-au/articles/5000560831641-Weighing-Profiles-in-ForceDecks>, accessed 2026-10-02.
- ForceDecks Windows - Release Notes: <https://support.vald.com/hc/en-au/articles/29733426841113-ForceDecks-Windows-Release-Notes>, accessed 2026-10-02.
- Weighing profiles in ForceDecks iOS: <https://support.vald.com/hc/en-au/articles/4999643957913-Weighing-profiles-in-ForceDecks-iOS>, accessed 2026-10-02.
- Weight Settings in ForceDecks Jump: <https://support.vald.com/hc/en-au/articles/5349963760409-Weight-Settings-in-ForceDecks-Jump>, accessed 2026-10-02.
- Zeroing ForceDecks: <https://support.vald.com/hc/en-au/articles/5000438165785-Zeroing-ForceDecks>, accessed 2026-10-02.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
