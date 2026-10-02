# Hawkin Dynamics metrics

Hawkin Dynamics makes wireless dual force plates and the TruStrength dynamometer. This page breaks down every metric Hawkin Dynamics publishes for its force plates, and for TruStrength where the same API returns it. Use it to look up what a column means, which window it covers, how it is calculated, and how it differs from a VALD ForceDecks metric with a similar name. Read the [name collisions](#hawkin-and-vald-name-collisions) before you compare the two vendors.

Checked against: `hawkinR` 2.0.1 (CRAN, published 2026-07-21), `hdforce` 2.1.0 (PyPI), Hawkin Beta API Specification 1.12 (2026-03-23), the Hawkin metric database web page, and the Hawkin help center, 2026-10-02.

Hawkin Dynamics and TruStrength are trademarks of their owner. VALD and ForceDecks are trademarks of their owner, and appear here only to compare metric names. This repository is not affiliated with or endorsed by Hawkin Dynamics.

The metric blocks sit on part pages, one per test type. Use these links to open them:

- [Countermovement jump](hawkin-dynamics-cmj.md): 85 metric blocks.
- [Squat jump](hawkin-dynamics-squat-jump.md): 47 metric blocks.
- [Drop jump](hawkin-dynamics-drop-jump.md): 85 metric blocks.
- [Isometric test](hawkin-dynamics-isometric.md): 62 metric blocks.
- [Countermovement rebound jump](hawkin-dynamics-cmj-rebound.md): 115 metric blocks.
- [Multi rebound](hawkin-dynamics-multi-rebound.md): 29 metric blocks.
- [Drop landing](hawkin-dynamics-drop-landing.md): 40 metric blocks.
- [Free run on the force plates](hawkin-dynamics-free-run.md): 29 metric blocks.
- [Weigh-in](hawkin-dynamics-weigh-in.md): 4 metric blocks.
- [TruStrength tests](hawkin-dynamics-trustrength.md): 14 metric blocks.

## How to read this page

Each metric block on a part page has these fields:

- Names: the API column label, the metric ID, the `hawkinR` column, and the `hdforce` column. The `hawkinR` column comes from the dictionary `header` field. The `hdforce` column comes from applying the `clean_names` rules in the `hdforce` source to the API label. It was not confirmed against an API response.
- What it measures: one plain sentence.
- Phase or window: the phase, with the events that start and end it.
- Calculation: Hawkin's definition from the dictionary, paraphrased. Then a formula that restates the definition, with every term defined. The restatement is not Hawkin's text. Where Hawkin does not publish a detail, the block says so.
- Inputs, units, and variants: what the calculation needs, the unit, and the left, right, asymmetry, relative, net, or gross versions in the same test.
- Comparison with VALD ForceDecks: shown only where both sources support the match. A block without this field has no supported match.
- What changes the number: choices and errors that move the value when the athlete's performance does not change.
- Sources: links to the sources that support the block.

Definitions come from the `MetricDictionary` data shipped in `hawkinR` and `hdforce` ([hawkinR dictionary], [hdforce dictionary]). Both packages are released under the MIT License, copyright Hawkin Dynamics. Every definition on this page is paraphrased. Definitions of metrics that appear only on the metric database web page are paraphrased from that page ([Hawkin metric database]). The sources at the end of the page give the full links.

"Not published" means the vendor does not publish that detail. In the summary tables, the last column shows whether Hawkin publishes the calculation:

- Yes: Hawkin's description and the restated formula leave no detail unpublished.
- Partly: Hawkin describes the metric, but a detail such as the sign, a threshold, or an end point is not published.
- Not published: Hawkin does not publish the formula.

## Hawkin and VALD name collisions

These Hawkin and VALD names look alike but measure different things:

- Braking phase. Hawkin's braking phase starts at peak negative velocity ([Hawkin blog, CMJ phases]). VALD's `Eccentric Braking Phase` starts at minimum force, and VALD's `Eccentric Deceleration Phase` starts at peak negative velocity ([VALD glossary]). Hawkin braking matches VALD deceleration ([Merrigan 2022]). So Hawkin `Braking Phase` is not VALD `Braking Phase Duration`, and Hawkin `Braking Net Impulse` is not VALD `Eccentric Braking Impulse`.
- Jump height. Hawkin `Jump Height` uses take-off velocity ([Hawkin blog, take-off velocity]) and matches VALD `Jump Height (Imp-Mom)` ([VALD glossary]). VALD also exports `Jump Height (Flight Time)`. The Hawkin multi rebound uses flight time ([Hawkin blog, flight time]).
- mRSI and RSI. Hawkin CMJ `mRSI` is take-off-velocity jump height divided by time to take-off ([hawkinR dictionary]) and matches VALD `RSI-modified (Imp-Mom)`, not VALD `RSI-modified` ([VALD glossary]). Hawkin CMJ `RSI` is flight time divided by time to take-off and matches VALD `Flight Time:Contraction Time`. In the drop jump and rebound, both divide by contact time.
- Time to take-off and contraction time. Same window, different start rules (5 standard deviations against 20 N) and different units (s against ms) ([Hawkin blog, CMJ phases], [VALD CMJ phases]).
- Positive impulse. Hawkin `Positive Impulse` is gross impulse in braking and propulsion ([hawkinR dictionary]). VALD `Positive Impulse` is net impulse over the whole repetition, including landing ([VALD glossary]).
- Stiffness. Hawkin `Stiffness` divides force at the lowest point by the lowest displacement ([hawkinR dictionary]). VALD `CMJ Stiffness` divides peak concentric force by the displacement at the start of the concentric phase ([VALD glossary]).
- P1 and P2. Hawkin's index is P1 divided by P2 ([Hawkin help, P1 and P2]). VALD's is P2 divided by P1 ([VALD glossary]).
- Relative force. Hawkin reports force as a percentage of system weight ([hawkinR dictionary]). VALD reports N/kg ([VALD glossary]). Convert with N/kg = % × g / 100.
- Units. Hawkin reports times in s and depth and jump height in m. VALD reports many times in ms and heights in cm ([VALD glossary]).

## Test types and metric counts

This table counts metrics per test type. The API count comes from the `MetricDictionary` and excludes the `active` flag. The web page count is the number of metric entries on the metric database page. The blocks cover every API metric plus metrics found only on the web page.

| Test type | Canonical test type ID | Abbreviation | API metrics | Metric database web page entries | Web-only metrics added | Blocks on this page | Part page |
|---|---|---|---|---|---|---|---|
| Countermovement jump | `7nNduHeM5zETPjHxvm7s` | `CMJ` | 79 | 85 | 6 | 85 | [countermovement jump](hawkin-dynamics-cmj.md) |
| Squat jump | `QEG7m7DhYsD6BrcQ8pic` | `SJ` | 41 | 46 | 6 | 47 | [squat jump](hawkin-dynamics-squat-jump.md) |
| Drop jump | `gyBETpRXpdr63Ab2E0V8` | `DJ` | 81 | 84 | 4 | 85 | [drop jump](hawkin-dynamics-drop-jump.md) |
| Isometric test | `2uS5XD5kXmWgIZ5HhQ3A` | `ISO` | 62 | 54 | 0 | 62 | [isometric test](hawkin-dynamics-isometric.md) |
| Countermovement rebound jump | `pqgf2TPUOQOQs6r0HQWb` | `CMJR` | 106 | 114 | 9 | 115 | [countermovement rebound jump](hawkin-dynamics-cmj-rebound.md) |
| Multi rebound | `r4fhrkPdYlLxYQxEeM78` | `MR` | 29 | 29 | 0 | 29 | [multi rebound](hawkin-dynamics-multi-rebound.md) |
| Drop landing | `rKgI4y3ItTAzUekTUpvR` | `DL` | 38 | 40 | 2 | 40 | [drop landing](hawkin-dynamics-drop-landing.md) |
| Free run on the force plates | `5pRSUQVSJVnxijpPMck3` | `FREE` | 0 | 29 | 29 | 29 | [free run on the force plates](hawkin-dynamics-free-run.md) |
| Weigh-in | `ubeWMPN1lJFbuQbAM97s` | `WI` | 4 | 4 | 0 | 4 | [weigh-in](hawkin-dynamics-weigh-in.md) |
| TruStrength isometric test | `umnEZPgi6zaxuw0KhUpM` | `TSISO` | 7 | Not listed | 0 | 7 | [TruStrength tests](hawkin-dynamics-trustrength.md) |
| TruStrength free run | `4KlQgKmBxbOY6uKTLDFL` | `TSFR` | 7 | Not listed | 0 | 7 | [TruStrength tests](hawkin-dynamics-trustrength.md) |
| Total | | | 454 | 485 | 56 | 510 | |

Read the counts with these points in mind:

- The web page and the API name some metrics differently, for example `Average Braking Force` and `Avg. Braking Force`, and `L/R` and `L|R`. The block uses the API name.
- The free run test type exists in the API, with canonical ID `5pRSUQVSJVnxijpPMck3`, but the `MetricDictionary` lists no metrics for it ([hawkinR dictionary], [hdforce source]). Its metrics come from the web page only.
- The `MetricDictionary` lists the TruStrength free run metrics twice. This page counts them once.
- The `hawkinR` manual says the dictionary has 484 rows ([hawkinR manual]). The shipped data has 472 rows, including 8 duplicate rows and one `active` row per test type ([hawkinR dictionary]).
- Hawkin says it provides 450 or more metrics ([Hawkin help, active metrics]).

## Summary tables

Each table lists the metrics of one test type. The last column shows whether Hawkin publishes the calculation, as described in "How to read this page".

### Countermovement jump

The 85 metric blocks are on [the countermovement jump part page](hawkin-dynamics-cmj.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Unweighting Phase` | How long the unweighting phase lasts | s | Yes |
| `Unweighting Phase %` | The unweighting phase as a percentage of the whole movement | % | Partly |
| `Avg. Braking Force` | The average total force during the braking phase, including body weight | N | Yes |
| `Avg. Relative Braking Force` | The average total force during the braking phase, as a percentage of system weight | % | Yes |
| `Left Avg. Braking Force` | The average force on the left plate during the braking phase | N | Yes |
| `Right Avg. Braking Force` | The average force on the right plate during the braking phase | N | Yes |
| `L\|R Avg. Braking Force` | The difference between the left and right plates for average braking force, as a percentage | % | Not published |
| `Avg. Braking Power` | The average power during the braking phase | W | Yes |
| `Avg. Relative Braking Power` | The average power during the braking phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Braking Velocity` | The average center of mass velocity during the braking phase | m/s | Yes |
| `Braking Impulse` | Total force including body weight added up over the braking phase | N.s | Yes |
| `Braking Net Impulse` | Force above system weight added up over the braking phase | N.s | Yes |
| `Relative Braking Impulse` | Total force including body weight added up over the braking phase, per kilogram of system mass | N.s/kg | Yes |
| `Relative Braking Net Impulse` | Force above system weight added up over the braking phase, per kilogram of system mass | N.s/kg | Yes |
| `L\|R Braking Impulse Index` | The difference between the left and right plates for braking impulse, as a percentage | % | Not published |
| `Braking Phase` | How long the braking phase lasts | s | Yes |
| `Braking Phase %` | The braking phase as a percentage of the whole movement | % | Partly |
| `Braking RFD` | How fast force rises during the braking phase | N/s | Yes |
| `Left Avg. Braking RFD` | How fast force rises on the left plate during the braking phase | N/s | Yes |
| `Right Avg. Braking RFD` | How fast force rises on the right plate during the braking phase | N/s | Yes |
| `L\|R Avg. Braking RFD` | The difference between the left and right plates for average braking RFD, as a percentage | % | Not published |
| `Peak Braking Force` | The highest total force during the braking phase, including body weight | N | Yes |
| `Peak Relative Braking Force` | The highest total force during the braking phase, as a percentage of system weight | % | Yes |
| `Left Force at Peak Braking Force` | Force on the left plate at the instant of peak combined force in the braking phase | N | Yes |
| `Right Force at Peak Braking Force` | Force on the right plate at the instant of peak combined force in the braking phase | N | Yes |
| `L\|R Peak Braking Force` | The difference between the left and right plates for peak braking force, as a percentage | % | Not published |
| `Peak Braking Power` | The largest braking power during the braking phase | W | Partly |
| `Peak Relative Braking Power` | The largest braking power during the braking phase, per kilogram of system mass | W/kg | Partly |
| `Peak Braking Velocity` | The fastest downward center of mass velocity, at the start of the braking phase | m/s | Yes |
| `Countermovement Depth` | How far the center of mass drops below its starting height | m | Yes |
| `Force at Min Displacement` | Force at the lowest point of the dip | N | Yes |
| `Relative Force at Min Displacement` | Force at the lowest point of the dip, as a percentage of system weight | % | Yes |
| `Stiffness` | Force at the lowest point of the dip divided by how far the center of mass dropped | N/m | Partly |
| `Avg. Propulsive Force` | The average total force during the propulsive phase, including body weight | N | Yes |
| `Avg. Relative Propulsive Force` | The average total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Avg. Propulsive Force` | The average force on the left plate during the propulsive phase | N | Yes |
| `Right Avg. Propulsive Force` | The average force on the right plate during the propulsive phase | N | Yes |
| `L\|R Avg. Propulsive Force` | The difference between the left and right plates for average propulsive force, as a percentage | % | Not published |
| `Avg. Propulsive Power` | The average power during the propulsive phase | W | Yes |
| `Avg. Relative Propulsive Power` | The average power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Propulsive Velocity` | The average center of mass velocity during the propulsive phase | m/s | Yes |
| `Peak Propulsive Force` | The highest total force during the propulsive phase, including body weight | N | Yes |
| `Peak Relative Propulsive Force` | The highest total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Force at Peak Propulsive Force` | Force on the left plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `Right Force at Peak Propulsive Force` | Force on the right plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `L\|R Peak Propulsive Force` | The difference between the left and right plates for peak propulsive force, as a percentage | % | Not published |
| `Peak Propulsive Power` | The highest power during the propulsive phase | W | Yes |
| `Peak Relative Propulsive Power` | The highest power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Peak Velocity` | The highest upward center of mass velocity before take-off | m/s | Yes |
| `Propulsive Impulse` | Total force including body weight added up over the propulsive phase | N.s | Yes |
| `Propulsive Net Impulse` | Force above system weight added up over the propulsive phase | N.s | Yes |
| `Relative Propulsive Impulse` | Total force including body weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `Relative Propulsive Net Impulse` | Force above system weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `L\|R Propulsive Impulse Index` | The difference between the left and right plates for propulsive impulse, as a percentage | % | Not published |
| `Propulsive Phase` | How long the propulsive phase lasts | s | Yes |
| `Propulsive Phase %` | The propulsive phase as a percentage of the whole movement | % | Partly |
| `Impulse Ratio` | Braking net impulse compared with propulsive net impulse | None listed | Yes |
| `Positive Impulse` | Total force including body weight added up over the braking and propulsive phases | N.s | Yes |
| `Positive Net Impulse` | Force above system weight added up over the braking and propulsive phases | N.s | Yes |
| `mRSI` | Jump height divided by the time taken to jump | None listed | Yes |
| `RSI` | Flight time divided by the time taken to jump | None listed | Yes |
| `Time To Takeoff` | How long the jump takes, from the start of movement to take-off | s | Yes |
| `Flight Time` | Time in the air | s | Yes |
| `Jump Height` | How high the center of mass rises after take-off | m | Yes |
| `Jump Momentum` | The athlete's momentum at take-off: mass times take-off velocity | kg.m/s | Yes |
| `Takeoff Velocity` | How fast the center of mass moves up at the instant the athlete leaves the plates | m/s | Yes |
| `Avg. Landing Force` | The average total force during the landing phase, including body weight | N | Yes |
| `Left Avg. Landing Force` | The average force on the left plate during the landing phase | N | Yes |
| `Right Avg. Landing Force` | The average force on the right plate during the landing phase | N | Yes |
| `L\|R Avg. Landing Force` | The difference between the left and right plates for average landing force, as a percentage | % | Not published |
| `L\|R Landing Impulse Index` | The difference between the left and right plates for landing impulse, as a percentage | % | Not published |
| `Landing Stiffness` | Force at the lowest point of the landing divided by how far the center of mass dropped in the landing | N/m | Partly |
| `Peak Landing Force` | The highest total force during the landing phase, including body weight | N | Yes |
| `Relative Peak Landing Force` | Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak | % | Partly |
| `Left Force at Peak Landing Force` | Force on the left plate at the instant of peak combined force in the landing phase | N | Yes |
| `Right Force at Peak Landing Force` | Force on the right plate at the instant of peak combined force in the landing phase | N | Yes |
| `L\|R Peak Landing Force` | The difference between the left and right plates for peak landing force, as a percentage | % | Not published |
| `Time to Stabilization` | How long the athlete takes to settle after landing | ms | Yes |
| `P1 Propulsive Impulse` | Impulse in the first half of the propulsive phase | N.s | Partly |
| `P2 Propulsive Impulse` | Impulse in the second half of the propulsive phase | N.s | Partly |
| `P1\|P2 Propulsive Impulse Index` | How the first half of the push compares with the second half | None | Yes |
| `Landing Height` | How far the center of mass falls from the top of the jump to touchdown | m | Not published |
| `Landing Phase` | How long the landing takes, from touchdown until the athlete stops moving down | s | Yes |
| `Landing Performance Index` | Landing height per second of landing time. Higher means the athlete stops a bigger fall faster | None | Partly |

### Squat jump

The 47 metric blocks are on [the squat jump part page](hawkin-dynamics-squat-jump.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Avg. Propulsive Force` | The average total force during the propulsive phase, including body weight | N | Yes |
| `Avg. Relative Propulsive Force` | The average total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Avg. Propulsive Force` | The average force on the left plate during the propulsive phase | N | Yes |
| `Right Avg. Propulsive Force` | The average force on the right plate during the propulsive phase | N | Yes |
| `L\|R Avg. Propulsive Force` | The difference between the left and right plates for average propulsive force, as a percentage | % | Not published |
| `Avg. Propulsive Power` | The average power during the propulsive phase | W | Yes |
| `Avg. Relative Propulsive Power` | The average power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Propulsive Velocity` | The average center of mass velocity during the propulsive phase | m/s | Yes |
| `Peak Propulsive Force` | The highest total force during the propulsive phase, including body weight | N | Yes |
| `Peak Relative Propulsive Force` | The highest total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Force at Peak Propulsive Force` | Force on the left plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `Right Force at Peak Propulsive Force` | Force on the right plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `L\|R Peak Propulsive Force` | The difference between the left and right plates for peak propulsive force, as a percentage | % | Not published |
| `Peak Propulsive Power` | The highest power during the propulsive phase | W | Yes |
| `Peak Relative Propulsive Power` | The highest power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Peak Velocity` | The highest upward center of mass velocity before take-off | m/s | Yes |
| `Propulsive Impulse` | Total force including body weight added up over the propulsive phase | N.s | Yes |
| `Propulsive Net Impulse` | Force above system weight added up over the propulsive phase | N.s | Yes |
| `Relative Propulsive Impulse` | Total force including body weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `Relative Propulsive Net Impulse` | Force above system weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `L\|R Propulsive Impulse Index` | The difference between the left and right plates for propulsive impulse, as a percentage | % | Not published |
| `Propulsive Phase` | How long the propulsive phase lasts | s | Yes |
| `Propulsive RFD` | How fast force rises from the start of movement to peak force | N/s | Partly |
| `Time To Takeoff` | How long the jump takes, from the start of movement to take-off | s | Yes |
| `Flight Time` | Time in the air | s | Yes |
| `Jump Height` | How high the center of mass rises after take-off | m | Yes |
| `Jump Momentum` | The athlete's momentum at take-off: mass times take-off velocity | kg.m/s | Yes |
| `Takeoff Velocity` | How fast the center of mass moves up at the instant the athlete leaves the plates | m/s | Yes |
| `Avg. Landing Force` | The average total force during the landing phase, including body weight | N | Yes |
| `Left Avg. Landing Force` | The average force on the left plate during the landing phase | N | Yes |
| `Right Avg. Landing Force` | The average force on the right plate during the landing phase | N | Yes |
| `L\|R Avg. Landing Force` | The difference between the left and right plates for average landing force, as a percentage | % | Not published |
| `L\|R Landing Impulse Index` | The difference between the left and right plates for landing impulse, as a percentage | % | Not published |
| `Landing Stiffness` | Force at the lowest point of the landing divided by how far the center of mass dropped in the landing | N/m | Partly |
| `Peak Landing Force` | The highest total force during the landing phase, including body weight | N | Yes |
| `Relative Peak Landing Force` | Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak | % | Partly |
| `Left Force at Peak Landing Force` | Force on the left plate at the instant of peak combined force in the landing phase | N | Yes |
| `Right Force at Peak Landing Force` | Force on the right plate at the instant of peak combined force in the landing phase | N | Yes |
| `L\|R Peak Landing Force` | The difference between the left and right plates for peak landing force, as a percentage | % | Not published |
| `Time to Stabilization` | How long the athlete takes to settle after landing | ms | Yes |
| `P1 Propulsive Impulse` | Impulse in the first half of the propulsive phase | N.s | Partly |
| `P2 Propulsive Impulse` | Impulse in the second half of the propulsive phase | N.s | Partly |
| `P1\|P2 Propulsive Impulse Index` | How the first half of the push compares with the second half | None | Yes |
| `Landing Height` | How far the center of mass falls from the top of the jump to touchdown | m | Not published |
| `Landing Phase` | How long the landing takes, from touchdown until the athlete stops moving down | s | Yes |
| `Landing Performance Index` | Landing height per second of landing time. Higher means the athlete stops a bigger fall faster | None | Partly |

### Drop jump

The 85 metric blocks are on [the drop jump part page](hawkin-dynamics-drop-jump.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Drop Height` | The height the center of mass falls before contact. It sets how hard the landing is | m | Yes |
| `Impact Peak` | Whether peak force lands in the first 20% of ground contact | Yes/No | Yes |
| `Avg. Braking Force` | The average total force during the braking phase, including body weight | N | Yes |
| `Avg. Relative Braking Force` | The average total force during the braking phase, as a percentage of system weight | % | Yes |
| `Left Avg. Braking Force` | The average force on the left plate during the braking phase | N | Yes |
| `Right Avg. Braking Force` | The average force on the right plate during the braking phase | N | Yes |
| `L\|R Avg. Braking Force` | The difference between the left and right plates for average braking force, as a percentage | % | Not published |
| `Avg. Braking Power` | The average power during the braking phase | W | Yes |
| `Avg. Relative Braking Power` | The average power during the braking phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Braking Velocity` | The average center of mass velocity during the braking phase | m/s | Yes |
| `Braking Impulse` | Total force including body weight added up over the braking phase | N.s | Yes |
| `Braking Net Impulse` | Force above system weight added up over the braking phase | N.s | Yes |
| `Relative Braking Impulse` | Total force including body weight added up over the braking phase, per kilogram of system mass | N.s/kg | Yes |
| `Relative Braking Net Impulse` | Force above system weight added up over the braking phase, per kilogram of system mass | N.s/kg | Yes |
| `L\|R Braking Impulse Index` | The difference between the left and right plates for braking impulse, as a percentage | % | Not published |
| `Braking Phase` | How long the braking phase lasts | s | Yes |
| `Braking Phase %` | The braking phase as a percentage of the whole movement | % | Partly |
| `Avg. Braking RFD` | How fast force rises during the braking phase | N/s | Yes |
| `Left Avg. Braking RFD` | How fast force rises on the left plate during the braking phase | N/s | Yes |
| `Right Avg. Braking RFD` | How fast force rises on the right plate during the braking phase | N/s | Yes |
| `L\|R Avg. Braking RFD` | The difference between the left and right plates for average braking RFD, as a percentage | % | Not published |
| `Peak Braking Force` | The highest total force during the braking phase, including body weight | N | Yes |
| `Peak Relative Braking Force` | The highest total force during the braking phase, as a percentage of system weight | % | Yes |
| `Left Force at Peak Braking Force` | Force on the left plate at the instant of peak combined force in the braking phase | N | Yes |
| `Right Force at Peak Braking Force` | Force on the right plate at the instant of peak combined force in the braking phase | N | Yes |
| `L\|R Peak Braking Force` | The difference between the left and right plates for peak braking force, as a percentage | % | Not published |
| `Peak Braking Power` | The largest braking power during the braking phase | W | Partly |
| `Peak Relative Braking Power` | The largest braking power during the braking phase, per kilogram of system mass | W/kg | Partly |
| `Time to Peak Braking Force` | Time from initial contact to peak braking force | ms | Yes |
| `Countermovement Depth` | How far the center of mass drops below its starting height | m | Yes |
| `Force At Min Displacement` | Force at the lowest point of the dip | N | Yes |
| `Relative Force At Min Displacement` | Force at the lowest point of the dip, as a percentage of system weight | % | Yes |
| `Stiffness` | Force at the lowest point of the dip divided by how far the center of mass dropped | N/m | Partly |
| `Avg. Propulsive Force` | The average total force during the propulsive phase, including body weight | N | Yes |
| `Avg. Relative Propulsive Force` | The average total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Avg. Propulsive Force` | The average force on the left plate during the propulsive phase | N | Yes |
| `Right Avg. Propulsive Force` | The average force on the right plate during the propulsive phase | N | Yes |
| `L\|R Avg. Propulsive Force` | The difference between the left and right plates for average propulsive force, as a percentage | % | Not published |
| `Avg. Propulsive Power` | The average power during the propulsive phase | W | Yes |
| `Avg. Relative Propulsive Power` | The average power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Propulsive Velocity` | The average center of mass velocity during the propulsive phase | m/s | Yes |
| `Peak Propulsive Force` | The highest total force during the propulsive phase, including body weight | N | Yes |
| `Peak Relative Propulsive Force` | The highest total force during the propulsive phase, as a percentage of system weight | % | Yes |
| `Left Force at Peak Propulsive Force` | Force on the left plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `Right Force at Peak Propulsive Force` | Force on the right plate at the instant of peak combined force in the propulsive phase | N | Yes |
| `L\|R Peak Propulsive Force` | The difference between the left and right plates for peak propulsive force, as a percentage | % | Not published |
| `Peak Propulsive Power` | The highest power during the propulsive phase | W | Yes |
| `Peak Relative Propulsive Power` | The highest power during the propulsive phase, per kilogram of system mass | W/kg | Yes |
| `Peak Velocity` | The highest upward center of mass velocity before take-off | m/s | Yes |
| `Propulsive Impulse` | Total force including body weight added up over the propulsive phase | N.s | Yes |
| `Propulsive Net Impulse` | Force above system weight added up over the propulsive phase | N.s | Yes |
| `Relative Propulsive Impulse` | Total force including body weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `Relative Propulsive Net Impulse` | Force above system weight added up over the propulsive phase, per kilogram of system mass | N.s/kg | Yes |
| `L\|R Propulsive Impulse Index` | The difference between the left and right plates for propulsive impulse, as a percentage | % | Not published |
| `Propulsive Phase` | How long the propulsive phase lasts | s | Yes |
| `Propulsive Phase %` | The propulsive phase as a percentage of the whole movement | % | Partly |
| `Contact Time` | Ground contact time: braking phase plus propulsive phase | s | Yes |
| `Net Impulse Ratio` | Braking net impulse compared with propulsive net impulse | None listed | Yes |
| `mRSI` | Jump height divided by ground contact time | None listed | Yes |
| `Positive Impulse` | Total force including body weight added up over the braking and propulsive phases | N.s | Yes |
| `Positive Net Impulse` | Force above system weight added up over the braking and propulsive phases | N.s | Yes |
| `RSI` | Flight time divided by ground contact time | None listed | Yes |
| `Spring Like Correlation` | How closely force rises and falls with the center of mass drop during contact, like a spring | None listed | Yes |
| `Time To Takeoff` | Ground contact time, from initial contact to take-off | s | Yes |
| `Flight Time` | Time in the air | s | Yes |
| `Jump Height` | How high the center of mass rises after take-off | m | Yes |
| `Jump Momentum` | The athlete's momentum at take-off: mass times take-off velocity | kg.m/s | Yes |
| `Takeoff Velocity` | How fast the center of mass moves up at the instant the athlete leaves the plates | m/s | Yes |
| `Avg. Landing Force` | The average total force during the landing phase, including body weight | N | Yes |
| `Left Avg. Landing Force` | The average force on the left plate during the landing phase | N | Yes |
| `Right Avg. Landing Force` | The average force on the right plate during the landing phase | N | Yes |
| `L\|R Avg. Landing Force` | The difference between the left and right plates for average landing force, as a percentage | % | Not published |
| `L\|R Landing Impulse Index` | The difference between the left and right plates for landing impulse, as a percentage | % | Not published |
| `Landing Stiffness` | Force at the lowest point of the landing divided by how far the center of mass dropped in the landing | N/m | Partly |
| `Peak Landing Force` | The highest total force during the landing phase, including body weight | N | Yes |
| `Relative Peak Landing Force` | Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak | % | Partly |
| `Left Force at Peak Landing Force` | Force on the left plate at the instant of peak combined force in the landing phase | N | Yes |
| `Right Force at Peak Landing Force` | Force on the right plate at the instant of peak combined force in the landing phase | N | Yes |
| `L\|R Peak Landing Force` | The difference between the left and right plates for peak landing force, as a percentage | % | Not published |
| `Time to Stabilization` | How long the athlete takes to settle after landing | ms | Yes |
| `Box Height` | The box height you enter | m | Yes |
| `Landing Height` | How far the center of mass falls from the top of the jump to touchdown | m | Not published |
| `Landing Phase` | How long the landing takes, from touchdown until the athlete stops moving down | s | Yes |
| `Landing Performance Index` | Landing height per second of landing time. Higher means the athlete stops a bigger fall faster | None | Partly |

### Isometric test

The 62 metric blocks are on [the isometric test part page](hawkin-dynamics-isometric.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Initiation Threshold` | How much force varied during the quiet period before the pull. Lower means a stiller start | N | Yes |
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `RFD 0-100 ms` | How fast force rises over the first 100 ms of the pull | N/s | Partly |
| `RFD 0-150 ms` | How fast force rises over the first 150 ms of the pull | N/s | Partly |
| `RFD 0-200 ms` | How fast force rises over the first 200 ms of the pull | N/s | Partly |
| `RFD 0-250 ms` | How fast force rises over the first 250 ms of the pull | N/s | Partly |
| `RFD 0-50 ms` | How fast force rises over the first 50 ms of the pull | N/s | Partly |
| `Time to Peak Force` | Time from the start of the pull to peak force | s | Yes |
| `Length of Pull` | How long the pull lasts | s | Yes |
| `Force at 0 ms` | Total force 0 ms after the start of the pull | N | Yes |
| `Net Force at 0 ms` | Force above system weight 0 ms after the start of the pull | N | Yes |
| `Relative Force at 0 ms` | Force 0 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 0 ms (BW)` | Force 0 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 0 ms` | Force on the left plate 0 ms after the start of the pull | N | Yes |
| `Right Force at 0 ms` | Force on the right plate 0 ms after the start of the pull | N | Yes |
| `Force at 100 ms` | Total force 100 ms after the start of the pull | N | Yes |
| `Net Force at 100 ms` | Force above system weight 100 ms after the start of the pull | N | Yes |
| `Relative Force at 100 ms` | Force 100 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 100 ms (BW)` | Force 100 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 100 ms` | Force on the left plate 100 ms after the start of the pull | N | Yes |
| `Right Force at 100 ms` | Force on the right plate 100 ms after the start of the pull | N | Yes |
| `Force at 150 ms` | Total force 150 ms after the start of the pull | N | Yes |
| `Net Force at 150 ms` | Force above system weight 150 ms after the start of the pull | N | Yes |
| `Relative Force at 150 ms` | Force 150 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 150 ms (BW)` | Force 150 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 150 ms` | Force on the left plate 150 ms after the start of the pull | N | Yes |
| `Right Force at 150 ms` | Force on the right plate 150 ms after the start of the pull | N | Yes |
| `Force at 200 ms` | Total force 200 ms after the start of the pull | N | Yes |
| `Net Force at 200 ms` | Force above system weight 200 ms after the start of the pull | N | Yes |
| `Relative Force at 200 ms` | Force 200 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 200 ms (BW)` | Force 200 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 200 ms` | Force on the left plate 200 ms after the start of the pull | N | Yes |
| `Right Force at 200 ms` | Force on the right plate 200 ms after the start of the pull | N | Yes |
| `Force at 250 ms` | Total force 250 ms after the start of the pull | N | Yes |
| `Net Force at 250 ms` | Force above system weight 250 ms after the start of the pull | N | Yes |
| `Relative Force at 250 ms` | Force 250 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 250 ms (BW)` | Force 250 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 250 ms` | Force on the left plate 250 ms after the start of the pull | N | Yes |
| `Right Force at 250 ms` | Force on the right plate 250 ms after the start of the pull | N | Yes |
| `Force at 50 ms` | Total force 50 ms after the start of the pull | N | Yes |
| `Net Force at 50 ms` | Force above system weight 50 ms after the start of the pull | N | Yes |
| `Relative Force at 50 ms` | Force 50 ms after the start of the pull, as a percentage of system weight | % | Yes |
| `Relative Force at 50 ms (BW)` | Force 50 ms after the start of the pull, relative to the last known body weight | N/kg | Yes |
| `Left Force at 50 ms` | Force on the left plate 50 ms after the start of the pull | N | Yes |
| `Right Force at 50 ms` | Force on the right plate 50 ms after the start of the pull | N | Yes |
| `Impulse 0-100ms` | Total force added up over the first 100 ms of the pull | N.s | Yes |
| `Net Impulse 0-100ms` | Force above system weight added up over the first 100 ms of the pull | N.s | Yes |
| `Impulse 0-150ms` | Total force added up over the first 150 ms of the pull | N.s | Yes |
| `Net Impulse 0-150ms` | Force above system weight added up over the first 150 ms of the pull | N.s | Yes |
| `Impulse 0-200ms` | Total force added up over the first 200 ms of the pull | N.s | Yes |
| `Net Impulse 0-200ms` | Force above system weight added up over the first 200 ms of the pull | N.s | Yes |
| `Impulse 0-250ms` | Total force added up over the first 250 ms of the pull | N.s | Yes |
| `Net Impulse 0-250ms` | Force above system weight added up over the first 250 ms of the pull | N.s | Yes |
| `Impulse 0-50ms` | Total force added up over the first 50 ms of the pull | N.s | Yes |
| `Net Impulse 0-50ms` | Force above system weight added up over the first 50 ms of the pull | N.s | Yes |
| `Net Peak Force` | The highest force above system weight during the pull | N | Yes |
| `Peak Force` | The highest total force during the pull, including body weight | N | Yes |
| `Relative Peak Force` | The highest force during the pull, as a percentage of system weight | % | Yes |
| `Relative Peak Force (BW)` | The highest force during the pull, relative to the last known body weight | N/kg | Yes |
| `Left Peak Force` | The highest force on the left plate during the pull | N | Yes |
| `Right Peak Force` | The highest force on the right plate during the pull | N | Yes |
| `L\|R Peak Force` | The difference between the left and right plates for peak force, as a percentage | % | Not published |

### Countermovement rebound jump

The 115 metric blocks are on [the countermovement rebound jump part page](hawkin-dynamics-cmj-rebound.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Avg. Landing Force` | The average total force during the landing phase, including body weight | N | Yes |
| `Left Avg. Landing Force` | The average force on the left plate during the landing phase | N | Yes |
| `Right Avg. Landing Force` | The average force on the right plate during the landing phase | N | Yes |
| `L\|R Avg. Landing Force` | The difference between the left and right plates for average landing force, as a percentage | % | Not published |
| `L\|R Landing Impulse Index` | The difference between the left and right plates for landing impulse, as a percentage | % | Not published |
| `Landing Stiffness` | Force at the lowest point of the landing divided by how far the center of mass dropped in the landing | N/m | Partly |
| `Peak Landing Force` | The highest total force during the landing phase, including body weight | N | Yes |
| `Relative Peak Landing Force` | Landing force as a percentage of system weight. Hawkin's text describes the average, not the peak | % | Partly |
| `Left Force at Peak Landing Force` | Force on the left plate at the instant of peak combined force in the landing phase | N | Yes |
| `Right Force at Peak Landing Force` | Force on the right plate at the instant of peak combined force in the landing phase | N | Yes |
| `L\|R Peak Landing Force` | The difference between the left and right plates for peak landing force, as a percentage | % | Not published |
| `Time to Stabilization` | How long the athlete takes to settle after landing | ms | Yes |
| `CMJ Avg. Braking Force` | The average total force during the braking phase of the countermovement jump, including body weight | N | Yes |
| `CMJ Avg. Relative Braking Force` | The average total force during the braking phase of the countermovement jump, as a percentage of system weight | % | Yes |
| `Left CMJ Avg. Braking Force` | The average force on the left plate during the braking phase of the countermovement jump | N | Yes |
| `Right CMJ Avg. Braking Force` | The average force on the right plate during the braking phase of the countermovement jump | N | Yes |
| `CMJ L\|R Avg. Braking Force` | The difference between the left and right plates for average braking force of the countermovement jump, as a percentage | % | Not published |
| `CMJ Avg. Braking Power` | The average power during the braking phase of the countermovement jump | W | Yes |
| `CMJ Avg. Relative Braking Power` | The average power during the braking phase of the countermovement jump, per kilogram of system mass | W/kg | Yes |
| `CMJ Braking Impulse` | Total force including body weight added up over the braking phase of the countermovement jump | N.s | Yes |
| `CMJ Braking Net Impulse` | Force above system weight added up over the braking phase of the countermovement jump | N.s | Yes |
| `CMJ Relative Braking Impulse` | Total force including body weight added up over the braking phase of the countermovement jump, per kilogram of system mass | N.s/kg | Yes |
| `CMJ Relative Braking Net Impulse` | Force above system weight added up over the braking phase of the countermovement jump, per kilogram of system mass | N.s/kg | Yes |
| `CMJ L\|R Braking Impulse Index` | The difference between the left and right plates for braking impulse of the countermovement jump, as a percentage | % | Not published |
| `CMJ Braking RFD` | How fast force rises during the braking phase of the countermovement jump | N/s | Yes |
| `CMJ Peak Braking Force` | The highest total force during the braking phase of the countermovement jump, including body weight | N | Yes |
| `CMJ Peak Relative Braking Force` | The highest total force during the braking phase of the countermovement jump, as a percentage of system weight | % | Yes |
| `CMJ Peak Braking Power` | The largest braking power during the braking phase of the countermovement jump | W | Partly |
| `CMJ Peak Relative Braking Power` | The largest braking power during the braking phase of the countermovement jump, per kilogram of system mass | W/kg | Partly |
| `CMJ Depth` | How far the center of mass drops below its starting height of the countermovement jump | m | Yes |
| `CMJ Force At Min Displacement` | Force at the lowest point of the dip | N | Yes |
| `CMJ Relative Force At Min Displacement` | Force at the lowest point of the dip, as a percentage of system weight | % | Yes |
| `CMJ Avg. Propulsive Force` | The average total force during the propulsive phase of the countermovement jump, including body weight | N | Yes |
| `CMJ Avg. Relative Propulsive Force` | The average total force during the propulsive phase of the countermovement jump, as a percentage of system weight | % | Yes |
| `Left CMJ Avg. Propulsive Force` | The average force on the left plate during the propulsive phase of the countermovement jump | N | Yes |
| `Right CMJ Avg. Propulsive Force` | The average force on the right plate during the propulsive phase of the countermovement jump | N | Yes |
| `CMJ L\|R Avg. Propulsive Force` | The difference between the left and right plates for average propulsive force of the countermovement jump, as a percentage | % | Not published |
| `CMJ Avg. Propulsive Power` | The average power during the propulsive phase of the countermovement jump | W | Yes |
| `CMJ Avg. Relative Propulsive Power` | The average power during the propulsive phase of the countermovement jump, per kilogram of system mass | W/kg | Yes |
| `CMJ Peak Propulsive Force` | The highest total force during the propulsive phase of the countermovement jump, including body weight | N | Yes |
| `CMJ Peak Relative Propulsive Force` | The highest total force during the propulsive phase of the countermovement jump, as a percentage of system weight | % | Yes |
| `CMJ Peak Propulsive Power` | The highest power during the propulsive phase of the countermovement jump | W | Yes |
| `CMJ Peak Relative Propulsive Power` | The highest power during the propulsive phase of the countermovement jump, per kilogram of system mass | W/kg | Yes |
| `CMJ Propulsive Impulse` | Total force including body weight added up over the propulsive phase of the countermovement jump | N.s | Yes |
| `CMJ Propulsive Net Impulse` | Force above system weight added up over the propulsive phase of the countermovement jump | N.s | Yes |
| `CMJ Relative Propulsive Impulse` | Total force including body weight added up over the propulsive phase of the countermovement jump, per kilogram of system mass | N.s/kg | Yes |
| `CMJ Relative Propulsive Net Impulse` | Force above system weight added up over the propulsive phase of the countermovement jump, per kilogram of system mass | N.s/kg | Yes |
| `CMJ L\|R Propulsive Impulse Index` | The difference between the left and right plates for propulsive impulse of the countermovement jump, as a percentage | % | Not published |
| `Impulse Ratio` | Braking net impulse compared with propulsive net impulse of the countermovement jump | None listed | Yes |
| `Positive Impulse` | Total force including body weight added up over the braking and propulsive phases of the countermovement jump | N.s | Yes |
| `Positive Net Impulse` | Force above system weight added up over the braking and propulsive phases of the countermovement jump | N.s | Yes |
| `CMJ Modified RSI` | Jump height divided by the time taken to jump | None listed | Yes |
| `CMJ RSI` | Flight time divided by the time taken to jump | None listed | Yes |
| `CMJ Time To Takeoff` | How long the jump takes, from the start of movement to take-off of the countermovement jump | s | Yes |
| `CMJ Jump Height` | How high the center of mass rises after take-off of the countermovement jump | m | Yes |
| `CMJ Jump Momentum` | The athlete's momentum at take-off of the countermovement jump: mass times take-off velocity | kg.m/s | Yes |
| `Rebound Impact Peak` | Whether peak force lands in the first 20% of ground contact | Yes/No | Yes |
| `Rebound Avg. Braking Force` | The average total force during the rebound braking phase of the rebound, including body weight | N | Yes |
| `Rebound Avg. Relative Braking Force` | The average total force during the rebound braking phase of the rebound, as a percentage of system weight | % | Yes |
| `Left Rebound Avg. Braking Force` | The average force on the left plate during the rebound braking phase of the rebound | N | Yes |
| `Right Rebound Avg. Braking Force` | The average force on the right plate during the rebound braking phase of the rebound | N | Yes |
| `Rebound L\|R Avg. Braking Force` | The difference between the left and right plates for average braking force of the rebound, as a percentage | % | Not published |
| `Rebound Avg. Braking Power` | The average power during the rebound braking phase of the rebound | W | Yes |
| `Rebound Avg. Relative Braking Power` | The average power during the rebound braking phase of the rebound, per kilogram of system mass | W/kg | Yes |
| `Rebound Braking Impulse` | Total force including body weight added up over the rebound braking phase of the rebound | N.s | Yes |
| `Rebound Braking Net Impulse` | Force above system weight added up over the rebound braking phase of the rebound | N.s | Yes |
| `Rebound Relative Braking Impulse` | Total force including body weight added up over the rebound braking phase of the rebound, per kilogram of system mass | N.s/kg | Yes |
| `Rebound Relative Braking Net Impulse` | Force above system weight added up over the rebound braking phase of the rebound, per kilogram of system mass | N.s/kg | Yes |
| `Rebound L\|R Braking Impulse Index` | The difference between the left and right plates for braking impulse of the rebound, as a percentage | % | Not published |
| `Rebound Peak Braking Force` | The highest total force during the rebound braking phase of the rebound, including body weight | N | Yes |
| `Rebound Peak Relative Braking Force` | The highest total force during the rebound braking phase of the rebound, as a percentage of system weight | % | Yes |
| `Rebound Peak Braking Power` | The largest braking power during the rebound braking phase of the rebound | W | Partly |
| `Rebound Peak Relative Braking Power` | The largest braking power during the rebound braking phase of the rebound, per kilogram of system mass | W/kg | Partly |
| `Rebound Time to Peak Braking Force` | Time from initial contact to peak braking force | ms | Yes |
| `Rebound Depth` | How far the center of mass drops below its starting height of the rebound | m | Yes |
| `Rebound Force At Min Displacement` | Force at the lowest point of the dip | N | Yes |
| `Rebound Relative Force At Min Displacement` | Force at the lowest point of the dip, as a percentage of system weight | % | Yes |
| `Rebound Stiffness` | Force at the lowest point of the dip divided by how far the center of mass dropped | N/m | Partly |
| `Rebound Avg. Propulsive Force` | The average total force during the rebound propulsive phase of the rebound, including body weight | N | Yes |
| `Rebound Avg. Relative Propulsive Force` | The average total force during the rebound propulsive phase of the rebound, as a percentage of system weight | % | Yes |
| `Left Rebound Avg. Propulsive Force` | The average force on the left plate during the rebound propulsive phase of the rebound | N | Yes |
| `Right Rebound Avg. Propulsive Force` | The average force on the right plate during the rebound propulsive phase of the rebound | N | Yes |
| `Rebound L\|R Avg. Propulsive Force` | The difference between the left and right plates for average propulsive force of the rebound, as a percentage | % | Not published |
| `Rebound Avg. Propulsive Power` | The average power during the rebound propulsive phase of the rebound | W | Yes |
| `Rebound Avg. Relative Propulsive Power` | The average power during the rebound propulsive phase of the rebound, per kilogram of system mass | W/kg | Yes |
| `Rebound Peak Propulsive Force` | The highest total force during the rebound propulsive phase of the rebound, including body weight | N | Yes |
| `Rebound Peak Relative Propulsive Force` | The highest total force during the rebound propulsive phase of the rebound, as a percentage of system weight | % | Yes |
| `Rebound Peak Propulsive Power` | The highest power during the rebound propulsive phase of the rebound | W | Yes |
| `Rebound Peak Relative Propulsive Power` | The highest power during the rebound propulsive phase of the rebound, per kilogram of system mass | W/kg | Yes |
| `Rebound Propulsive Impulse` | Total force including body weight added up over the rebound propulsive phase of the rebound | N.s | Yes |
| `Rebound Propulsive Net Impulse` | Force above system weight added up over the rebound propulsive phase of the rebound | N.s | Yes |
| `Rebound Relative Propulsive Impulse` | Total force including body weight added up over the rebound propulsive phase of the rebound, per kilogram of system mass | N.s/kg | Yes |
| `Rebound Relative Propulsive Net Impulse` | Force above system weight added up over the rebound propulsive phase of the rebound, per kilogram of system mass | N.s/kg | Yes |
| `Rebound L\|R Propulsive Impulse Index` | The difference between the left and right plates for propulsive impulse of the rebound, as a percentage | % | Not published |
| `Rebound Impulse Ratio` | Braking net impulse compared with propulsive net impulse of the rebound | None listed | Yes |
| `Rebound Positive Impulse` | Total force including body weight added up over the braking and propulsive phases of the rebound | N.s | Yes |
| `Rebound Positive Net Impulse` | Force above system weight added up over the braking and propulsive phases of the rebound | N.s | Yes |
| `Rebound Contact Time` | Ground contact time: braking phase plus propulsive phase | ms | Yes |
| `Rebound Modified RSI` | Jump height divided by ground contact time | None listed | Yes |
| `Rebound RSI` | Flight time divided by ground contact time | None listed | Yes |
| `Rebound Spring Like Correlation` | How closely force rises and falls with the center of mass drop during contact, like a spring | None listed | Yes |
| `Rebound Time To Takeoff` | Ground contact time, from initial contact to take-off | s | Yes |
| `Rebound Flight Time` | Time in the air of the rebound | ms | Yes |
| `Rebound Jump Height` | How high the center of mass rises after take-off of the rebound | m | Yes |
| `Rebound Jump Momentum` | The athlete's momentum at take-off of the rebound: mass times take-off velocity | kg.m/s | Yes |
| `CMJ P1 Propulsive Impulse` | Impulse in the first half of the propulsive phase | N.s | Partly |
| `CMJ P2 Propulsive Impulse` | Impulse in the second half of the propulsive phase | N.s | Partly |
| `CMJ P1\|P2 Propulsive Impulse Index` | How the first half of the push compares with the second half | None | Yes |
| `Rebound P1 Propulsive Impulse` | Impulse in the first half of the propulsive phase | N.s | Partly |
| `Rebound P2 Propulsive Impulse` | Impulse in the second half of the propulsive phase | N.s | Partly |
| `Rebound P1\|P2 Propulsive Impulse Index` | How the first half of the push compares with the second half | None | Yes |
| `Landing Height` | How far the center of mass falls from the top of the jump to touchdown | m | Not published |
| `Landing Phase` | How long the landing takes, from touchdown until the athlete stops moving down | s | Yes |
| `Landing Performance Index` | Landing height per second of landing time. Higher means the athlete stops a bigger fall faster | None | Partly |

### Multi rebound

The 29 metric blocks are on [the multi rebound part page](hawkin-dynamics-multi-rebound.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Avg. Contact Time` | Average contact time over all jumps | s | Yes |
| `Avg. Force` | The average total force during the trial | N | Partly |
| `L\|R Avg. Force` | The difference between the left and right plates for average force, as a percentage | % | Not published |
| `Avg. Jump Height` | The average jump height over all jumps | m | Yes |
| `Avg. mRSI` | The average mRSI over all jumps | None listed | Yes |
| `Avg. RSI` | The average RSI over all jumps | None listed | Yes |
| `Number of Jumps` | How many jumps the software found in the trial | Count | Yes |
| `Peak Force` | The highest total force during the trial | N | Partly |
| `L\|R Peak Force` | The difference between the left and right plates for peak force, as a percentage | % | Not published |
| `Peak Jump Height` | The highest single jump in the trial | m | Yes |
| `Peak Jump mRSI` | mRSI of the highest jump | None listed | Yes |
| `Peak Jump RSI` | RSI of the highest jump | None listed | Yes |
| `Peak mRSI` | The highest mRSI of any jump | None listed | Yes |
| `Peak RSI` | The highest RSI of any jump | None listed | Yes |
| `Top 3 Jumps Avg. Contact Time` | Average contact time over the three highest jumps | s | Yes |
| `Top 3 Jumps Avg. Jump Height` | The average of the three highest jumps | m | Yes |
| `Top 3 Jumps Avg. mRSI` | The average mRSI of the three highest jumps | None listed | Yes |
| `Top 3 Jumps Avg. RSI` | The average RSI of the three highest jumps | None listed | Yes |
| `Top 3 Jumps Peak mRSI` | The highest mRSI among the three highest jumps | None listed | Yes |
| `Top 3 Jumps Peak RSI` | The highest RSI among the three highest jumps | None listed | Yes |
| `Top 5 Jumps Avg. Contact Time` | Average contact time over the five highest jumps | s | Yes |
| `Top 5 Jumps Avg. Jump Height` | The average of the five highest jumps | m | Yes |
| `Top 5 Jumps Avg. mRSI` | The average mRSI of the five highest jumps | None listed | Yes |
| `Top 5 Jumps Avg. RSI` | The average RSI of the five highest jumps | None listed | Yes |
| `Top 5 Jumps Peak mRSI` | The highest mRSI among the five highest jumps | None listed | Yes |
| `Top 5 Jumps Peak RSI` | The highest RSI among the five highest jumps | None listed | Yes |
| `Total Contact Time` | All contact times added together | s | Yes |
| `Total Flight Time` | All flight times added together | s | Yes |

### Drop landing

The 40 metric blocks are on [the drop landing part page](hawkin-dynamics-drop-landing.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `System Weight` | The athlete's weight plus anything they carry, measured while they stand still before the test | N | Partly |
| `Drop Height` | The height the center of mass falls before contact. It sets how hard the landing is | m | Yes |
| `Stiffness` | Force at the lowest point of the landing divided by how far the center of mass dropped | N/m | Partly |
| `Stability Depth` | How low the center of mass sits when the athlete has settled | m | Yes |
| `Contact Velocity` | How fast the center of mass moves down when the feet hit the plates | m/s | Not published |
| `Peak Force` | The highest total force during the drop landing | N | Yes |
| `Peak Relative Force` | The highest total force during the drop landing, as a percentage of system weight | % | Yes |
| `Left Force at Peak Force` | Force on the left plate at the instant of peak combined force in the drop landing | N | Yes |
| `Right Force at Peak Force` | Force on the right plate at the instant of peak combined force in the drop landing | N | Yes |
| `L\|R Peak Force` | The difference between the left and right plates for peak force, as a percentage | % | Not published |
| `Avg. Impact Force` | The average total force during the impact phase, including body weight | N | Yes |
| `Avg. Relative Impact Force` | The average total force during the impact phase, as a percentage of system weight | % | Yes |
| `Left Avg. Impact Force` | The average force on the left plate during the impact phase | N | Yes |
| `Right Avg. Impact Force` | The average force on the right plate during the impact phase | N | Yes |
| `L\|R Avg. Impact Force` | The difference between the left and right plates for average impact force, as a percentage | % | Not published |
| `Avg. Impact Power` | The average power during the impact phase | W | Yes |
| `Avg. Relative Impact Power` | The average power during the impact phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Impact Velocity` | The average center of mass velocity during the impact phase | m/s | Yes |
| `Impact Phase` | How long the impact phase lasts | s | Yes |
| `Impact Phase %` | The impact phase as a percentage of the whole movement | % | Partly |
| `Impact RFD` | How fast force rises during the impact phase | N/s | Yes |
| `Left Impact RFD` | How fast force rises on the left plate during the impact phase | N/s | Yes |
| `Right Impact RFD` | How fast force rises on the right plate during the impact phase | N/s | Yes |
| `L\|R Impact RFD` | The difference between the left and right plates for impact RFD, as a percentage | % | Not published |
| `Peak Impact Power` | The largest braking power during the impact phase | W | Partly |
| `Peak Relative Impact Power` | The largest braking power during the impact phase, per kilogram of system mass | W/kg | Partly |
| `Avg. Stabilization Force` | The average total force during the stabilization phase, including body weight | N | Yes |
| `Left Avg. Stabilization Force` | The average force on the left plate during the stabilization phase | N | Yes |
| `Right Avg. Stabilization Force` | The average force on the right plate during the stabilization phase | N | Yes |
| `L\|R Avg. Stabilization Force` | The difference between the left and right plates for average stabilization force, as a percentage | % | Not published |
| `Avg. Relative Stabilization Power` | The average power during the stabilization phase, per kilogram of system mass | W/kg | Yes |
| `Avg. Stabilization Power` | The average power during the stabilization phase | W | Yes |
| `Avg. Stabilization Velocity` | The average center of mass velocity during the stabilization phase | m/s | Yes |
| `Peak Relative Stabilization Power` | The highest power during the stabilization phase, per kilogram of system mass | W/kg | Yes |
| `Peak Stabilization Power` | The highest power during the stabilization phase | W | Yes |
| `Stabilization Phase` | How long the stabilization phase lasts | s | Yes |
| `Stabilization Phase %` | The stabilization phase as a percentage of the whole movement | % | Partly |
| `Time To Stabilization` | How long the athlete takes to settle after landing | ms | Yes |
| `Landing Phase` | How long the landing takes, from touchdown until the athlete stops moving down | s | Yes |
| `Landing Performance Index` | Landing height per second of landing time. Higher means the athlete stops a bigger fall faster | None | Partly |

### Free run on the force plates

The 29 metric blocks are on [the free run on the force plates part page](hawkin-dynamics-free-run.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Avg. Force` | The average total force during the recording | N | Yes |
| `Peak Force` | The highest total force during the recording | N | Yes |
| `Avg. Left Force` | The average left plate force | N | Yes |
| `Avg. Right Force` | The average right plate force | N | Yes |
| `Peak Left Force` | The highest left plate force | N | Yes |
| `Peak Right Force` | The highest right plate force | N | Yes |
| `SD Left Force` | How much left plate force varies | N | Partly |
| `SD Right Force` | How much right plate force varies | N | Partly |
| `SD Total Force` | How much total force varies | N | Partly |
| `L\|R Avg. Force` | The left to right difference in average force | % | Not published |
| `L\|R Peak Force` | The left to right difference in peak force | % | Not published |
| `Left AP Sway Length` | Total front-to-back center of pressure path on the left plate | cm | Not published |
| `Left AP Sway Range` | The span of front-to-back center of pressure movement on the left plate | cm | Not published |
| `Left Avg. AP Sway Velocity` | Average speed of front-to-back center of pressure movement on the left plate | cm/s | Not published |
| `Left ML Sway Length` | Total side-to-side center of pressure path on the left plate | cm | Not published |
| `Left ML Sway Range` | The span of side-to-side center of pressure movement on the left plate | cm | Not published |
| `Left Avg. ML Sway Velocity` | Average speed of side-to-side center of pressure movement on the left plate | cm/s | Not published |
| `Left Sway Length` | Total center of pressure path on the left plate | cm | Not published |
| `Left Sway Range` | The span of center of pressure movement on the left plate | cm | Not published |
| `Left Sway Velocity` | Average speed of center of pressure movement on the left plate | cm/s | Not published |
| `Right AP Sway Length` | Total front-to-back center of pressure path on the right plate | cm | Not published |
| `Right AP Sway Range` | The span of front-to-back center of pressure movement on the right plate | cm | Not published |
| `Right Avg. AP Sway Velocity` | Average speed of front-to-back center of pressure movement on the right plate | cm/s | Not published |
| `Right ML Sway Length` | Total side-to-side center of pressure path on the right plate | cm | Not published |
| `Right ML Sway Range` | The span of side-to-side center of pressure movement on the right plate | cm | Not published |
| `Right Avg. ML Sway Velocity` | Average speed of side-to-side center of pressure movement on the right plate | cm/s | Not published |
| `Right Sway Length` | Total center of pressure path on the right plate | cm | Not published |
| `Right Sway Range` | The span of center of pressure movement on the right plate | cm | Not published |
| `Right Sway Velocity` | Average speed of center of pressure movement on the right plate | cm/s | Not published |

### Weigh-in

The 4 metric blocks are on [the weigh-in part page](hawkin-dynamics-weigh-in.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Standard Deviation` | How much force varied during the weigh-in. Large values mean the athlete moved | N | Yes |
| `Weight` | Body mass in kilograms | kgs | Partly |
| `Weight` | Body weight in pounds | lbs | Not published |
| `Weight in Newtons` | Body weight as a force | N | Partly |

### TruStrength isometric test

The 7 metric blocks are on [the TruStrength tests part page](hawkin-dynamics-trustrength.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Pretension` | The baseline force that starts and ends each repetition | N | Yes |
| `Target` | The force target set for the repetition | N | Partly |
| `Avg. Force` | The average force in the repetition | N | Yes |
| `Duration` | How long the repetition lasts | s | Yes |
| `Peak Force` | The highest force in the repetition | N | Yes |
| `Peak RFD` | The fastest instant rise in force in the repetition | N/s | Partly |
| `Total Impulse` | Force added up over the repetition | N.s | Yes |

### TruStrength free run

The 7 metric blocks are on [the TruStrength tests part page](hawkin-dynamics-trustrength.md).

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| `Pretension` | The baseline force that starts and ends each repetition | N | Yes |
| `Target` | The force target set for the repetition | N | Partly |
| `Avg. Force` | The average force in the repetition | N | Yes |
| `Duration` | How long the repetition lasts | s | Yes |
| `Peak Force` | The highest force in the repetition | N | Yes |
| `Peak RFD` | The fastest instant rise in force in the repetition | N/s | Partly |
| `Total Impulse` | Force added up over the repetition | N.s | Yes |

## Events and phases Hawkin uses

Hawkin names its jump phases after McMahon et al. (2018) ([Hawkin blog, CMJ phases], [McMahon 2018]). These are the events behind every window on this page:

| Event or phase | Hawkin definition | Source |
|---|---|---|
| System weight | Lowest 1 s average of force in the weighing phase, found by an optimization loop. The loop is not published. | ([hawkinR dictionary]) |
| Weighing phase | At least 1 s still before a CMJ, squat jump, or CMJ rebound runs. | ([Hawkin blog, CMJ phases], [Hawkin blog, flight time]) |
| Start of movement, CMJ | Force falls below system weight by 5 standard deviations of the weighing force, then the software traces back to the last sample equal to system weight and starts integration at zero velocity. | ([Hawkin blog, CMJ phases], [Hawkin blog, two key factors], [Merrigan 2022]) |
| Start of movement, squat jump and isometric | Force rises 5 standard deviations above body weight, traced back to within 0 to 2 N of body weight. The API dictionary also reports the isometric `Initiation Threshold`, 3 standard deviations of the quiet period, as a stillness check. | ([Merrigan 2022], [hawkinR dictionary]) |
| Squat jump fail rule | Force more than 5% below system weight before the jump fails the trial. | ([Hawkin blog, CMJ or squat jump]) |
| Unweighting phase | Start of movement to peak negative velocity. | ([Hawkin blog, CMJ phases], [Merrigan 2022]) |
| Braking phase, CMJ | Peak negative velocity to zero velocity. | ([Hawkin blog, CMJ phases], [Merrigan 2022]) |
| Braking phase, drop jump | Initial contact (30 N for 30 ms) to zero velocity. | ([Merrigan 2022]) |
| Propulsive phase | Zero velocity to take-off. | ([Hawkin blog, CMJ phases], [Merrigan 2022]) |
| Take-off and touchdown | Force below 25 N for 30 ms, and back above 25 N for 30 ms. | ([Merrigan 2022]) |
| Landing phase | Touchdown to the first instant of zero center of mass velocity. | ([Hawkin blog, CMJ phases], [Hawkin blog, landing metrics]) |
| Time to stabilization | Touchdown to the start of 1 s with force within 5% of system weight. | ([Hawkin blog, landing metrics], [hawkinR dictionary]) |
| Integration | Net force divided by mass, multiplied by the 1 ms sample time, summed sample by sample. | ([Hawkin blog, two key factors], [Hawkin help, force plate data]) |
| Jump height | Take-off velocity squared divided by 2 g for the CMJ, squat jump, CMJ rebound, and drop jump. Flight time for the multi rebound. | ([Hawkin blog, take-off velocity], [Hawkin blog, flight time]) |
| Drop jump start velocity | From true drop height by reverse integration, then flight time, then box height, since an update announced on 2025-01-14. | ([Hawkin blog, drop jump method]) |
| Sampling | 1000 Hz. | ([Hawkin help, force plate data]) |

The 25 N, 30 N, and 30 ms thresholds come from Merrigan et al. (2022), who describe Hawkin's software as used in that study. Hawkin's own pages do not state them. Hawkin changed the drop jump method in an update announced on 2025-01-14 ([Hawkin blog, drop jump method]), after that study.

Two published studies check Hawkin data against criterion methods:

- Badby et al. (2023) placed Hawkin plates on in-ground AMTI plates. They found no bias for 17 CMJ variables, and bias for 2 of 18 drop jump variables: peak braking force and peak braking power ([Badby 2023]).
- Merrigan et al. (2022) compared Hawkin software with custom MATLAB analysis of the same force data. Hawkin showed percent errors under 3% across the squat jump, CMJ, drop jump, and isometric mid-thigh pull ([Merrigan 2022]).

## Conflicts in the vendor's own sources

These conflicts sit inside Hawkin's own data and documents:

- Same metric ID, different meaning. In the CMJ, ID `positiveImpulse` is labeled `Positive Net Impulse`, and `relativeBrakingImpulse` and `relativePropulsiveImpulse` are net impulses. In the drop jump, the same IDs are gross impulses ([hawkinR dictionary]). Map by label.
- `Impulse Ratio` direction. The API dictionary says braking net over propulsive net. The CMJ section of the web page says propulsive net over braking net ([hawkinR dictionary], [Hawkin metric database]).
- `Relative Peak Landing Force`. The name says peak; Hawkin's text says the average landing force as a percentage of system weight ([hawkinR dictionary]).
- Same label, different metric. The weigh-in has two metrics labeled `Weight`, one in kgs and one in lbs ([hawkinR dictionary]). Name measures by label plus unit.
- Isometric (BW) variants. The unit is N/kg; six of the seven texts say a percentage of last known body weight ([hawkinR dictionary]).
- Units that differ between the API and the web page: `Time to Stabilization`, `Time to Peak Braking Force`, and `Rebound Flight Time` are ms in the API and s on the web page; the isometric (BW) variants are N/kg in the API and % on the web page ([hawkinR dictionary], [Hawkin metric database]). Each block flags these.
- Units inside the API: CMJ `Flight Time` is in s, but CMJ rebound `Rebound Flight Time`, `Rebound Contact Time`, and `Rebound Time to Peak Braking Force` are in ms ([hawkinR dictionary]).
- Drop jump `Drop Height`. The dictionary says it is the entered box height ([hawkinR dictionary]). Since the 2025-01-14 update it is the estimated true drop height, and `Box Height` holds the entry ([Hawkin blog, drop jump method], [Hawkin metric database]).
- Dictionary size. The `hawkinR` manual says the dictionary has 484 rows ([hawkinR manual]). The shipped data has 472 rows, including 8 duplicate rows and one `active` row per test type ([hawkinR dictionary]).

The units below differ between the API and the metric database web page. Each row names the metric, the test, the API unit, and the unit the web page lists:

| Metric | Test | Unit in the API dictionary | Unit on the web page |
|---|---|---|---|
| `Time to Stabilization` | Countermovement jump | `ms` | `Seconds (s)` |
| `Time to Stabilization` | Squat jump | `ms` | `Seconds (s)` |
| `Time to Peak Braking Force` | Drop jump | `ms` | `Seconds (s)` |
| `Peak Landing Force` | Drop jump | `N` | `%` |
| `Time to Stabilization` | Drop jump | `ms` | `Seconds (s)` |
| `Landing Height` | Drop jump | m (web page lists N, an error on that page) | N |
| `Relative Force at 100 ms (BW)` | Isometric test | `N/kg` | `%` |
| `Relative Force at 150 ms (BW)` | Isometric test | `N/kg` | `%` |
| `Relative Force at 200 ms (BW)` | Isometric test | `N/kg` | `%` |
| `Relative Force at 250 ms (BW)` | Isometric test | `N/kg` | `%` |
| `Relative Force at 50 ms (BW)` | Isometric test | `N/kg` | `%` |
| `Net Impulse 0-150ms` | Isometric test | `N.s` | `Newton second (N/s)` |
| `Time to Stabilization` | Countermovement rebound jump | `ms` | `Seconds (s)` |
| `Rebound Time to Peak Braking Force` | Countermovement rebound jump | `ms` | `Seconds (s)` |
| `Rebound Stiffness` | Countermovement rebound jump | `N/m` | `Newtons per meter (N/s)` |
| `Rebound Flight Time` | Countermovement rebound jump | `ms` | `Seconds (s)` |
| `Time To Stabilization` | Drop landing | `ms` | `Seconds (s)` |

The 18 free run sway metrics, such as `Left AP Sway Length`, list cm on the web page ([Hawkin metric database]). The API center of pressure trace is in mm ([Hawkin blog, center of pressure]). The free run test has no entries in the API dictionary, so the API unit for these metrics is not published.

Two more conflicts appear only inside metric blocks:

- Hawkin's sources disagree on which impulse is on top in these 4 blocks: `Impulse Ratio` (countermovement jump); `Net Impulse Ratio` (drop jump); `Impulse Ratio` (countermovement rebound jump); `Rebound Impulse Ratio` (countermovement rebound jump).
- The dictionary unit is N/kg, but the dictionary text says a percentage of last known body weight, in these 6 isometric test blocks: `Relative Force at 0 ms (BW)`, `Relative Force at 100 ms (BW)`, `Relative Force at 150 ms (BW)`, `Relative Force at 200 ms (BW)`, `Relative Force at 250 ms (BW)`, `Relative Force at 50 ms (BW)`.

## Not published

Hawkin does not publish these details. The count is the number of metric blocks that say so:

- The formula behind the `L|R` asymmetry metrics, in the countermovement jump, squat jump, drop jump, isometric test, countermovement rebound jump, multi rebound, drop landing, and free run (47 blocks).
- Whether the export keeps the minus sign on signed values such as `Peak Braking Power`, `Stiffness`, and `Peak Impact Power` (18 blocks).
- The optimization loop that picks `System Weight`, and which still period it uses in the drop jump and drop landing (12 blocks).
- The definition of whole-movement duration, which sets the denominator of the `%` phase metrics in the countermovement jump, drop jump, and drop landing (7 blocks).
- Whether Hawkin uses gross or net plate impulse for the left and right impulse metrics in the jump tests (13 blocks).
- Whether Hawkin subtracts system weight in the P1 and P2 propulsive impulses (8 blocks).
- Whether `P1 Propulsive Impulse` and `P2 Propulsive Impulse` are net or gross (6 blocks).
- The start and end events of the drop landing impact and stabilization phases (32 blocks).
- Contact, take-off, and force thresholds for the countermovement rebound jump and the multi rebound (53 blocks).
- The end point of the isometric pull (7 blocks).
- Whether `Initiation Threshold` sets the start of the isometric pull (58 blocks).
- Whether the isometric `RFD 0-50 ms` to `RFD 0-250 ms` metrics and the squat jump `Propulsive RFD` use end-point forces or a fitted slope (6 blocks).
- Whether `Relative Peak Landing Force` computes a peak or an average (4 blocks).
- How Hawkin computes `Landing Height` (4 blocks).
- Whether drop height replaces landing height in `Landing Performance Index` (5 blocks).
- Whether flight samples count in the multi rebound `Avg. Force` and `Peak Force` (2 blocks).
- Whether the free run `SD Left Force`, `SD Right Force`, and `SD Total Force` use the sample or population standard deviation (3 blocks).
- The averaging rule for the weigh-in `Weight in Newtons` (1 block).
- Which value the weigh-in `Weight` metrics use, and how Hawkin converts to pounds (2 blocks).
- The differentiation window for the TruStrength `Peak RFD`, and how the TruStrength `Target` is set (4 blocks).
- The formulas for the free run sway metrics, such as `Left AP Sway Length`. Hawkin describes them only in words (18 blocks).
- The API column, the metric ID, and the package column names for the 56 metrics that appear only on the web page.
- The phase landmarks for the isometric test. Hawkin does not show them.
- The metrics of the force plate free run in the API dictionary. The `MetricDictionary` lists none for that test type.

## Worked CMJ example

This example runs Hawkin's published CMJ rules on a synthetic force trace. The script builds an 80 kg athlete's jump at 1000 Hz with 1.5 N of plate noise. The athlete lands with the center of mass 0.02 m lower than at take-off. The script then detects events and computes metrics the way Hawkin describes. Every number below comes from the run shown at the end.

The script follows these steps:

1. Compute system weight as the lowest 1 s mean inside the first 1.5 s, because Hawkin's optimization loop is not published.
2. Find the start of movement at 5 standard deviations below system weight, then trace back to within 2 N of system weight.
3. Find take-off as force below 25 N for 30 ms, and touchdown as force above 25 N for 30 ms.
4. Integrate net force divided by mass, sample by sample, to get velocity and displacement.
5. Split unweighting, braking, and propulsion at peak negative velocity and zero velocity.
6. Compute jump height, time to take-off, mRSI, RSI, and braking and propulsive metrics.
7. Repeat key steps with changed inputs to show what moves the numbers.

The run gave these results:

| Metric | Value |
|---|---|
| `System Weight(N)` | 784.7257 |
| `Start of movement, backtracked (s)` | 1.5000 |
| `Take-off time (s)` | 2.2790 |
| `Takeoff Velocity(m/s)` | 2.0491 |
| `Jump Height(m)` | 0.2140 |
| `Time To Takeoff(s)` | 0.7790 |
| `mRSI` | 0.2747 |
| `Flight Time(s)` | 0.4260 |
| `RSI (flight time / time to take-off)` | 0.5469 |
| `Jump height from flight time (m), for comparison` | 0.2225 |
| `Unweighting Phase(s)` | 0.2990 |
| `Braking Phase(s)` | 0.1600 |
| `Propulsive Phase(s)` | 0.3200 |
| `Peak Braking Velocity(m/s)` | -1.0305 |
| `Avg. Braking Force(N)` | 1296.2265 |
| `Peak Braking Force(N)` | 1692.1139 |
| `Braking Net Impulse(N.s)` | 81.8401 |
| `Braking RFD(N/s)` | 5735.3278 |
| `Avg. Propulsive Force(N)` | 1298.7903 |
| `Peak Propulsive Force(N)` | 1767.1171 |
| `Propulsive Net Impulse(N.s)` | 164.5007 |
| `Peak Propulsive Power(W)` | 2650.4633 |
| `Countermovement Depth(m)` | -0.2612 |

Read the results this way:

- The synthetic jump's true take-off velocity was 2.0393 m/s. The detected value, 2.0491 m/s, is higher mainly because the 25 N rule ended contact one sample early. That sample, at 20.5 N, would have added −0.0096 m/s.
- Flight-time jump height, 0.2225 m, is higher than take-off velocity jump height, 0.2140 m, because the athlete landed lower than they took off. This is why you never mix the two methods.
- The two impulse ratio directions give 2.0100 and 0.4975 for the same jump. Check which one your export holds.
- A 10 N system weight error moved jump height from 0.2140 m to 0.1893 m or 0.2409 m.
- Moving the start of movement from the traced-back point to the 5 standard deviation crossing changed time to take-off from 0.7790 s to 0.7770 s.

The script is below. It needs Python 3 and `numpy`. It ran with Python 3.9.6 and `numpy` 2.0.2 on 2026-10-02.

```python
"""Worked CMJ example: Hawkin-defined events and metrics from a synthetic force trace.

Every rule below restates a published Hawkin Dynamics definition. Where Hawkin does
not publish a detail, the script says so in a comment and uses a stated choice.
"""
import numpy as np

FS = 1000                  # Hz. Hawkin plates sample at 1000 Hz.
DT = 1.0 / FS              # s
G = 9.81                   # m/s^2, the value Hawkin uses in its jump height example
MASS_TRUE = 80.0           # kg, used only to build the synthetic trace
rng = np.random.default_rng(2026)

# ---------------------------------------------------------------- build the trace
def segment(duration_s, fn):
    t = np.arange(int(round(duration_s * FS))) * DT
    return fn(t)

W_TRUE = MASS_TRUE * G
quiet = segment(1.5, lambda t: np.full_like(t, W_TRUE))
# Unweighting: force dips below body weight, half-cosine shape, 0.30 s.
unweight = segment(0.30, lambda t: W_TRUE - 0.55 * W_TRUE * np.sin(np.pi * t / 0.30))
# Push: one smooth bump above body weight, 0.42 s.
push = segment(0.42, lambda t: W_TRUE + 1.25 * W_TRUE * np.sin(np.pi * t / 0.42))
# Unloading to take-off: body weight falls smoothly to zero, 0.06 s.
unload = segment(0.06, lambda t: W_TRUE * np.cos(0.5 * np.pi * t / 0.06))
contact = np.concatenate([quiet, unweight, push, unload])

# Simulate the true centre of mass motion during contact (rectangle rule).
acc = (contact - W_TRUE) / MASS_TRUE
vel = np.cumsum(acc) * DT
disp = np.cumsum(vel) * DT
v_to_true, y_to = vel[-1], disp[-1]
# Flight: the athlete lands with the centre of mass 0.02 m lower than at take-off.
drop_below_takeoff = 0.02
t_flight_true = (v_to_true + np.sqrt(v_to_true**2 + 2 * G * drop_below_takeoff)) / G
flight = np.zeros(int(round(t_flight_true * FS)))
v_td = v_to_true - G * len(flight) * DT   # negative, touchdown velocity
# Landing: one bump above body weight whose net impulse stops the athlete.
TL = 0.30
B = MASS_TRUE * abs(v_td) * np.pi / (2 * TL)
landing = segment(TL, lambda t: W_TRUE + B * np.sin(np.pi * t / TL))
settle = segment(1.2, lambda t: np.full_like(t, W_TRUE))
force_clean = np.concatenate([contact, flight, landing, settle])

# Plate noise: 1.5 N standard deviation on every sample.
force = force_clean + rng.normal(0.0, 1.5, force_clean.size)
# Left and right plates: a fixed 51 % / 49 % split, so left + right = combined.
left = 0.51 * force
right = force - left
time = np.arange(force.size) * DT

# ---------------------------------------------------------------- Hawkin-defined steps
# 1. System weight. Hawkin: "The lowest 1s average of the vertical ground reaction
#    force ... during the weighting phase, identified by an optimization loop."
#    The loop is not published. Here: every 1 s window inside the first 1.5 s of
#    quiet standing, and keep the lowest mean. The standard deviation comes from
#    the same window.
win = FS
means = np.array([force[i:i + win].mean() for i in range(0, int(1.5 * FS) - win + 1)])
best = int(np.argmin(means))
system_weight = means[best]
sd_weigh = force[best:best + win].std(ddof=1)
system_mass = system_weight / G

# 2. Start of movement. Hawkin: movement onset is a drop below system weight by
#    5 standard deviations of the weighing-phase force (phases blog). Integration
#    starts at the last earlier sample equal to system weight (Lake, "two key
#    factors" blog; Merrigan et al. 2022 report "within 0-2 N of BW").
threshold = system_weight - 5 * sd_weigh
i_5sd = int(np.argmax(force < threshold))
i_start = i_5sd
while i_start > 0 and abs(force[i_start] - system_weight) > 2.0:
    i_start -= 1

# 3. Take-off and touchdown. Merrigan et al. (2022) report the Hawkin flight phase
#    as force below 25 N for 30 ms, ending when force returns above 25 N for 30 ms.
def first_run(mask, start, n):
    run = 0
    for i in range(start, mask.size):
        run = run + 1 if mask[i] else 0
        if run == n:
            return i - n + 1
    raise ValueError("event not found")

i_to = first_run(force < 25.0, i_start, 30)
i_td = first_run(force > 25.0, i_to, 30)

# 4. Velocity and displacement. Hawkin: divide net force by mass, multiply each
#    sample by the sample duration, and sum sample by sample from zero velocity.
net = force - system_weight
a = net / system_mass
v = np.zeros_like(force)
v[i_start:] = np.cumsum(a[i_start:]) * DT
s = np.zeros_like(force)
s[i_start:] = np.cumsum(v[i_start:]) * DT
p = force * v           # power = force x velocity, sample by sample

# 5. Phases (McMahon et al. 2018; Merrigan et al. 2022 Table 1).
i_pnv = i_start + int(np.argmin(v[i_start:i_to]))          # peak negative velocity
i_zero = i_pnv + int(np.argmax(v[i_pnv:i_to] >= 0.0))      # first zero velocity
unweighting = slice(i_start, i_pnv)
braking = slice(i_pnv, i_zero)
propulsive = slice(i_zero, i_to)

# 6. Metrics.
v_to = v[i_to - 1]                       # velocity at the last contact sample
jump_height = v_to**2 / (2 * G)
time_to_takeoff = (i_to - i_start) * DT
mrsi = jump_height / time_to_takeoff
flight_time = (i_td - i_to) * DT
rsi = flight_time / time_to_takeoff
jh_flight_time = G * flight_time**2 / 8

def dur(sl): return (sl.stop - sl.start) * DT
def rfd(sl): return (force[sl.stop - 1] - force[sl.start]) / ((sl.stop - 1 - sl.start) * DT)

braking_net_impulse = net[braking].sum() * DT
propulsive_net_impulse = net[propulsive].sum() * DT

rows = [
    ("System Weight(N)", system_weight),
    ("System mass (kg)", system_mass),
    ("Weighing SD (N)", sd_weigh),
    ("Onset threshold (N)", threshold),
    ("5 SD crossing time (s)", i_5sd * DT),
    ("Start of movement, backtracked (s)", i_start * DT),
    ("Take-off time (s)", i_to * DT),
    ("Touchdown time (s)", i_td * DT),
    ("Takeoff Velocity(m/s)", v_to),
    ("Jump Height(m)", jump_height),
    ("Time To Takeoff(s)", time_to_takeoff),
    ("mRSI", mrsi),
    ("Flight Time(s)", flight_time),
    ("RSI (flight time / time to take-off)", rsi),
    ("Jump height from flight time (m), for comparison", jh_flight_time),
    ("Unweighting Phase(s)", dur(unweighting)),
    ("Braking Phase(s)", dur(braking)),
    ("Propulsive Phase(s)", dur(propulsive)),
    ("Peak Braking Velocity(m/s)", v[i_pnv]),
    ("Avg. Braking Velocity(m/s)", v[braking].mean()),
    ("Avg. Braking Force(N)", force[braking].mean()),
    ("Peak Braking Force(N)", force[braking].max()),
    ("Avg. Relative Braking Force(%)", force[braking].mean() / system_weight * 100),
    ("Braking Impulse(N.s)", force[braking].sum() * DT),
    ("Braking Net Impulse(N.s)", braking_net_impulse),
    ("Relative Braking Net Impulse(N.s/kg)", braking_net_impulse / system_mass),
    ("Braking RFD(N/s)", rfd(braking)),
    ("Avg. Braking Power(W)", p[braking].mean()),
    ("Peak Braking Power(W), most negative", p[braking].min()),
    ("Avg. Propulsive Velocity(m/s)", v[propulsive].mean()),
    ("Peak Velocity(m/s)", v[i_start:i_to].max()),
    ("Avg. Propulsive Force(N)", force[propulsive].mean()),
    ("Peak Propulsive Force(N)", force[propulsive].max()),
    ("Avg. Relative Propulsive Force(%)", force[propulsive].mean() / system_weight * 100),
    ("Propulsive Impulse(N.s)", force[propulsive].sum() * DT),
    ("Propulsive Net Impulse(N.s)", propulsive_net_impulse),
    ("Relative Propulsive Net Impulse(N.s/kg)", propulsive_net_impulse / system_mass),
    ("Avg. Propulsive Power(W)", p[propulsive].mean()),
    ("Peak Propulsive Power(W)", p[propulsive].max()),
    ("Peak Relative Propulsive Power(W/kg)", p[propulsive].max() / system_mass),
    ("Countermovement Depth(m)", s[i_start:i_to].min()),
    ("Impulse ratio, propulsive net / braking net", propulsive_net_impulse / braking_net_impulse),
    ("Impulse ratio, braking net / propulsive net", braking_net_impulse / propulsive_net_impulse),
    ("Left Avg. Braking Force(N)", left[braking].mean()),
    ("Right Avg. Braking Force(N)", right[braking].mean()),
]
print("Synthetic truth: take-off velocity %.4f m/s, jump height %.4f m, flight %.4f s"
      % (v_to_true, v_to_true**2 / (2 * G), t_flight_true))
for name, value in rows:
    print(f"{name:52s} {value:12.4f}")

# 7. Sensitivity: what changes the number.
print("\nSensitivity checks")
def jh_with_weight(offset):
    w = system_weight + offset
    vv = np.cumsum((force[i_start:i_to] - w) / (w / G)) * DT
    return vv[-1] ** 2 / (2 * G)
for off in (-10.0, -5.0, 5.0, 10.0):
    print(f"Jump height with system weight {off:+.0f} N: {jh_with_weight(off):.4f} m")
ttt_5sd = (i_to - i_5sd) * DT
print(f"Time to take-off from the 5 SD crossing instead: {ttt_5sd:.4f} s, mRSI {jump_height / ttt_5sd:.4f}")
print(f"mRSI if jump height is left in cm: {jump_height * 100 / time_to_takeoff:.4f}")
n_contact = contact.size
excluded = contact[i_to:n_contact]
print(f"True contact samples after detected take-off: {excluded.size}, force {excluded.round(1).tolist()} N")
print(f"Velocity those samples would add: {((excluded - system_weight) / system_mass * DT).sum():.4f} m/s")
i_to20 = first_run(force < 20.0, i_start, 1)
print(f"Take-off with a single-sample 20 N rule: {i_to20 * DT:.3f} s (25 N for 30 ms gives {i_to * DT:.3f} s)")
```

The script printed this output:

```text
Synthetic truth: take-off velocity 2.0393 m/s, jump height 0.2120 m, flight 0.4253 s
System Weight(N)                                         784.7257
System mass (kg)                                          79.9924
Weighing SD (N)                                            1.4969
Onset threshold (N)                                      777.2411
5 SD crossing time (s)                                     1.5020
Start of movement, backtracked (s)                         1.5000
Take-off time (s)                                          2.2790
Touchdown time (s)                                         2.7050
Takeoff Velocity(m/s)                                      2.0491
Jump Height(m)                                             0.2140
Time To Takeoff(s)                                         0.7790
mRSI                                                       0.2747
Flight Time(s)                                             0.4260
RSI (flight time / time to take-off)                       0.5469
Jump height from flight time (m), for comparison           0.2225
Unweighting Phase(s)                                       0.2990
Braking Phase(s)                                           0.1600
Propulsive Phase(s)                                        0.3200
Peak Braking Velocity(m/s)                                -1.0305
Avg. Braking Velocity(m/s)                                -0.6729
Avg. Braking Force(N)                                   1296.2265
Peak Braking Force(N)                                   1692.1139
Avg. Relative Braking Force(%)                           165.1821
Braking Impulse(N.s)                                     207.3962
Braking Net Impulse(N.s)                                  81.8401
Relative Braking Net Impulse(N.s/kg)                       1.0231
Braking RFD(N/s)                                        5735.3278
Avg. Braking Power(W)                                   -791.3359
Peak Braking Power(W), most negative                   -1051.2461
Avg. Propulsive Velocity(m/s)                              1.5372
Peak Velocity(m/s)                                         2.2486
Avg. Propulsive Force(N)                                1298.7903
Peak Propulsive Force(N)                                1767.1171
Avg. Relative Propulsive Force(%)                        165.5088
Propulsive Impulse(N.s)                                  415.6129
Propulsive Net Impulse(N.s)                              164.5007
Relative Propulsive Net Impulse(N.s/kg)                    2.0565
Avg. Propulsive Power(W)                                1734.0805
Peak Propulsive Power(W)                                2650.4633
Peak Relative Propulsive Power(W/kg)                      33.1339
Countermovement Depth(m)                                  -0.2612
Impulse ratio, propulsive net / braking net                2.0100
Impulse ratio, braking net / propulsive net                0.4975
Left Avg. Braking Force(N)                               661.0755
Right Avg. Braking Force(N)                              635.1510

Sensitivity checks
Jump height with system weight -10 N: 0.2409 m
Jump height with system weight -5 N: 0.2272 m
Jump height with system weight +5 N: 0.2014 m
Jump height with system weight +10 N: 0.1893 m
Time to take-off from the 5 SD crossing instead: 0.7770 s, mRSI 0.2754
mRSI if jump height is left in cm: 27.4719
True contact samples after detected take-off: 1, force [20.5] N
Velocity those samples would add: -0.0096 m/s
Take-off with a single-sample 20 N rule: 2.280 s (25 N for 30 ms gives 2.279 s)
```

## Sources

These sources support the facts on this page:

- hawkinR 2.0.1 MetricDictionary (CRAN): <https://cran.r-project.org/web/packages/hawkinR/index.html>, accessed 2026-10-02.
- hdforce 2.1.0 MetricDictionary (PyPI): <https://pypi.org/project/hdforce/>, accessed 2026-10-02.
- hawkinR source: <https://github.com/HawkinDynamics/hawkinR>, accessed 2026-10-02.
- hdforce source: <https://github.com/HawkinDynamics/hawkinPy>, accessed 2026-10-02.
- hawkinR manual: <https://cran.r-universe.dev/hawkinR/doc/manual.html>, accessed 2026-10-02.
- Hawkin Beta API Specification 1.12 (power-query repository): <https://github.com/HawkinDynamics/power-query>, accessed 2026-10-02.
- Hawkin metric database: <https://www.hawkindynamics.com/hawkin-metric-database>, accessed 2026-10-02.
- Hawkin blog: phases of the CMJ: <https://www.hawkindynamics.com/blog/phases-of-the-cmj>, accessed 2026-10-02.
- Hawkin blog: two key factors that influence CMJ force data: <https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data>, accessed 2026-10-02.
- Hawkin blog: jump height from take-off velocity: <https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity>, accessed 2026-10-02.
- Hawkin blog: jump height from flight time: <https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time>, accessed 2026-10-02.
- Hawkin blog: drop jump method and metrics (2025): <https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics>, accessed 2026-10-02.
- Hawkin blog: new landing metrics (2025): <https://www.hawkindynamics.com/blog/new-landing-metrics>, accessed 2026-10-02.
- Hawkin blog: drop jumps, what to measure: <https://www.hawkindynamics.com/blog/drop-jumps-what-to-measure>, accessed 2026-10-02.
- Hawkin blog: CMJ or squat jump: <https://www.hawkindynamics.com/blog/countermovement-jump-or-squat-jump>, accessed 2026-10-02.
- Hawkin blog: asymmetry report: <https://www.hawkindynamics.com/blog/asymmetry-report>, accessed 2026-10-02.
- Hawkin blog: center of pressure: <https://www.hawkindynamics.com/blog/cop>, accessed 2026-10-02.
- Hawkin blog: IMTP basics: <https://www.hawkindynamics.com/blog/isometric-mid-thigh-pull-the-basics>, accessed 2026-10-02.
- Hawkin RSI course PDF: <https://www.hawkindynamics.com/hubfs/RSI%2BCourse%2B%E2%94%82%2BHawkin%2BDynamics%2BEdu.pdf>, accessed 2026-10-02.
- Hawkin help: understanding force plate data: <https://learning.hawkindynamics.com/knowledge/understanding-force-plate-data>, accessed 2026-10-02.
- Hawkin help: P1 and P2 propulsive impulse: <https://learning.hawkindynamics.com/knowledge/p1-and-p2-propulsive-impulse-and-the-ratio-between-them>, accessed 2026-10-02.
- Hawkin help: RSI and mRSI: <https://learning.hawkindynamics.com/knowledge/what-is-the-difference-between-rsi-and-mrsi>, accessed 2026-10-02.
- Hawkin help: time to stabilization: <https://learning.hawkindynamics.com/knowledge/how-do-i-use-time-to-stabilization>, accessed 2026-10-02.
- Hawkin help: left and right force plate: <https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate>, accessed 2026-10-02.
- Hawkin help: exporting data from the cloud: <https://learning.hawkindynamics.com/knowledge/exporting-data-from-cloud>, accessed 2026-10-02.
- Hawkin help: active metrics: <https://learning.hawkindynamics.com/knowledge/how-do-i-make-metrics-active>, accessed 2026-10-02.
- Hawkin help: drop jump processing error: <https://learning.hawkindynamics.com/knowledge/processing-error-on-drop-jump>, accessed 2026-10-02.
- Hawkin help: drop height: <https://learning.hawkindynamics.com/knowledge/do-you-have-to-measure-drop-height-when-performing-a-drop-jump>, accessed 2026-10-02.
- Hawkin help: IMTP setup: <https://learning.hawkindynamics.com/knowledge/isometric-mid-thigh-pull-setup-guide>, accessed 2026-10-02.
- Hawkin help: multi rebound setup: <https://learning.hawkindynamics.com/knowledge/multi-rebound-test-setup-guide>, accessed 2026-10-02.
- Hawkin help: free run setup: <https://learning.hawkindynamics.com/knowledge/free-run-test-setup-guide>, accessed 2026-10-02.
- Hawkin help: drop landing setup: <https://learning.hawkindynamics.com/knowledge/drop-landing-setupguide>, accessed 2026-10-02.
- Hawkin help: CMJ setup: <https://learning.hawkindynamics.com/knowledge/countermovement-jump-protocol>, accessed 2026-10-02.
- Hawkin help: CMJ rebound setup: <https://learning.hawkindynamics.com/knowledge/countermovement-rebound-test-setup-guide>, accessed 2026-10-02.
- Hawkin help: drop jump setup: <https://learning.hawkindynamics.com/knowledge/drop-jump-test-setup-guide>, accessed 2026-10-02.
- Hawkin help: pretension: <https://learning.hawkindynamics.com/knowledge/what-is-pretension>, accessed 2026-10-02.
- Hawkin help: imperial units: <https://learning.hawkindynamics.com/knowledge/how-to-i-convert-metrics-to-the-imperial-system>, accessed 2026-10-02.
- Hawkin help: disabled tests: <https://learning.hawkindynamics.com/knowledge/re-enabling-disabled-tests>, accessed 2026-10-02.
- Merrigan et al. 2022, J Strength Cond Res 36(9):2387-2402: <https://doi.org/10.1519/JSC.0000000000004275>, accessed 2026-10-02.
- Badby et al. 2023, Sensors 23(10):4820: <https://doi.org/10.3390/s23104820>, accessed 2026-10-02.
- McMahon et al. 2018, Strength Cond J 40(4):96-106: <https://doi.org/10.1519/SSC.0000000000000375>, accessed 2026-10-02.
- VALD ForceDecks Technical Glossary V2.0: <https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary>, accessed 2026-10-02.
- VALD help: key moments and phases of a CMJ: <https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump>, accessed 2026-10-02.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.

[Badby 2023]: https://doi.org/10.3390/s23104820
[Hawkin blog, center of pressure]: https://www.hawkindynamics.com/blog/cop
[Hawkin blog, CMJ or squat jump]: https://www.hawkindynamics.com/blog/countermovement-jump-or-squat-jump
[Hawkin blog, CMJ phases]: https://www.hawkindynamics.com/blog/phases-of-the-cmj
[Hawkin blog, drop jump method]: https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics
[Hawkin blog, flight time]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time
[Hawkin blog, landing metrics]: https://www.hawkindynamics.com/blog/new-landing-metrics
[Hawkin blog, take-off velocity]: https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity
[Hawkin blog, two key factors]: https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data
[Hawkin help, active metrics]: https://learning.hawkindynamics.com/knowledge/how-do-i-make-metrics-active
[Hawkin help, force plate data]: https://learning.hawkindynamics.com/knowledge/understanding-force-plate-data
[Hawkin help, P1 and P2]: https://learning.hawkindynamics.com/knowledge/p1-and-p2-propulsive-impulse-and-the-ratio-between-them
[Hawkin metric database]: https://www.hawkindynamics.com/hawkin-metric-database
[hawkinR dictionary]: https://cran.r-project.org/web/packages/hawkinR/index.html
[hawkinR manual]: https://cran.r-universe.dev/hawkinR/doc/manual.html
[hdforce dictionary]: https://pypi.org/project/hdforce/
[hdforce source]: https://github.com/HawkinDynamics/hawkinPy
[McMahon 2018]: https://doi.org/10.1519/SSC.0000000000000375
[Merrigan 2022]: https://doi.org/10.1519/JSC.0000000000004275
[VALD CMJ phases]: https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump
[VALD glossary]: https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary
