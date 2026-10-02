# Firstbeat Sports metrics

Firstbeat Sports measures heart rate, beat-to-beat intervals, movement, and recovery for athletes with the Firstbeat Sports Sensor, and analyzes the data in Sports Cloud. This page covers every metric that Sports Cloud exports through the Data Export or returns through the Sports Cloud API, and uses public sources only. Checked against: the Sports Cloud API Variables page and changelog, the Data Export help article, Firstbeat white papers, the Learning Center, and the Sports Guide, 2026-10-02.

Firstbeat, Firstbeat Sports, Firstbeat Sports Cloud, and Bodyguard are trademarks of their owners. This repository is not affiliated with or endorsed by Firstbeat.

## How to read this page

This page has summary tables, then one block for each metric. Each metric block is a short list with these fields:

- Firstbeat name, API variable, and unit: the name in the export and the API, with the unit Firstbeat states.
- What it measures: one plain sentence.
- Window or phase: the part of a measurement the value covers.
- Calculation: Firstbeat's description in paraphrase, then the formula. The formula is the one Firstbeat publishes, marked as a restatement, or "Not published".
- Defaults: settings and thresholds, each with a source.
- Inputs, Units, and Variants: what goes in, what comes out, and the forms the metric takes.
- Comparison with standard methods or other vendors: a comparison only where a source supports one.
- What changes the number: settings, data quality, and sensor factors.
- Sources: links to the vendor documents behind the block.

Follow these rules when you use the blocks:

- Many Firstbeat metrics come from proprietary models. This page says what Firstbeat publishes. "Not published" means Firstbeat gives no formula or detail in the sources read.
- Firstbeat states that all Learning Center content is protected by copyright ([Learning Center home](https://www.firstbeat.com/en/professional-sports/learning-center/)). This page paraphrases Firstbeat text and quotes only short fragments.
- A formula marked "restatement" is a rewrite of a Firstbeat statement or figure for this page, or a standard definition. Firstbeat does not print it as text.
- Export names follow the Data Export help article. The Excel header row is Not published, so the real header may differ.
- Code font marks metric names, API variable names, and export column names.
- In the summary tables, "Yes" means Firstbeat publishes the calculation. "Partly" means Firstbeat publishes some of it. "Not published" means Firstbeat does not publish the calculation. For a recorded signal with no calculation, such as raw RR intervals, the column shows "Yes".
- The API numbers the heart rate zones in the opposite order from the app. `zone1Time` is the highest zone. See [Time in heart rate zones](#time-in-heart-rate-zones).

## Areas and metric counts

The table lists each area, the number of metric blocks in this page, and the number of API variables or export-only columns that those blocks cover:

| Area | Metric blocks | API variables or export columns covered |
|---|---|---|
| Training load | 11 | 27 |
| Movement and external load | 5 | 30 |
| Heart rate and zones | 4 | 21 |
| HRV and recovery | 8 | 17 |
| Stress and sleep | 7 | 5, plus 5 Garmin fields and 1 export-only column |
| Fitness estimates, oxygen, and breathing | 5 | 9 |
| Energy expenditure | 2 | 5 |
| Data quality and raw signals | 4 | 4 |
| Total | 46 | 118, plus 5 Garmin fields and 1 export-only column |

The API Variables page lists 100 scalar variables and 17 time series, 117 in all. The changelog adds `movementEfficiency`, which makes 118 ([API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/)). The "Manual exercise TRIMP" block covers no extra variables. The export-only column is `Overnight Recovery (%)`.

## Settings and data conditions that change many metrics

These conditions change many metrics at once. Check them first when a number looks wrong:

- Maximum heart rate (HRmax) in the athlete profile. If you do not enter a measured value, Firstbeat enters an estimate from age, so a correct date of birth matters ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)). The age formula is Not published in the sources read. Firstbeat can recalculate old sessions after a correction, but calls this time-consuming ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)).
- Automatic HRmax and resting HR updates. Firstbeat's 24-hour method updates resting HR and HRmax from recorded data when it sees a lower resting value or a higher maximum ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). The Session Report shows a notice when it detects a new HRmax, and lets you revert it ([Session Report help](https://support.firstbeatsports.com/hc/en-us/articles/40602510889489-What-is-included-in-the-Session-Report)).
- Measurement-level overrides. In **Measurement settings** you can change the HRmax and resting HR for one measurement. The change does not touch the athlete profile ([Edit or delete measurements](https://support.firstbeatsports.com/hc/en-us/articles/360016072097-How-to-edit-or-delete-individual-measurements-in-Firstbeat-Sports-Cloud)).
- Activity class, a 0 to 10 value for the athlete's activity in the previous month. It scales Training Effect. Firstbeat expects professional athletes to fall between 7.5 and 10 ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). Firstbeat says it may be suitable to give every athlete in a team the same level ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)).
- Age, sex, height, and weight in the profile. The oxygen, energy, and sleep models use them as inputs ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf), [Sleep white paper](https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf)).
- Heart rate zone thresholds. Coaches can change zone names, thresholds, and colors in the account defaults ([Start using Sports Cloud](https://support.firstbeatsports.com/hc/en-us/articles/360015938677-How-to-start-using-Firstbeat-Sports-Cloud)). Changing a single athlete's zones is a one-by-one task ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)).
- Beat-to-beat data quality and sensor contact. See the data quality area at the end.
- Trim and merge. A trim cannot be undone. A merge fills the gap with empty data, and the analysis fills long gaps often with 100 bpm, so average-intensity metrics such as TRIMP per minute and Movement Intensity are not correct for a merged measurement ([Trim and merge](https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud)).
- Sensor firmware. Firmware 3.8 introduced a new Sensor HR algorithm on 2021-10-21 ([What's new in Sports products](https://www.firstbeat.com/en/whats-new-sports-products/)). Expect a small break when you compare sessions across that date.
- Subscription level. Some variables need Premium or Premium+ ([API variables](https://apidocs.firstbeat.com/variables/)).

## API access tiers

Firstbeat ties some variables to a subscription tier or to a named service. The sources state these requirements:

| Variable or feature | Tier or service stated | Source |
|---|---|---|
| General | Some variables need Premium or Premium+. | [API variables](https://apidocs.firstbeat.com/variables/) |
| `playerStatusScore` (Training Status) | Premium+. It needs the `training_status` service. The 2021 brochure lists it under Premium. | [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf) |
| `trimpPerMinHighest30s` to `trimpPerMinHighest2h` | Premium+. Exercise measurements only. | [API variables](https://apidocs.firstbeat.com/variables/) |
| Movement Load, `movementLoadSeries`, and `averageMovementIntensity` | The Sensor page and the brochure say Premium. The API page marks the series and Movement Intensity variables as Premium+. | [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf), [API variables](https://apidocs.firstbeat.com/variables/) |
| `movementIntensityHighest5s` to `movementIntensityHighest2h` | Premium+. Exercise measurements only. They need the `movement_intensity_curve` service. | [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/) |
| `movementEfficiency` | Premium+. Added on 2025-10-22. | [API changelog](https://apidocs.firstbeat.com/changelog/) |
| Heart rate recovery variables | Premium+. They need the `heart_rate_recovery` service. | [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/) |
| Overnight measurements | A Premium feature. | [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf) |
| `rriSeries` (raw RR intervals) | Needs a Premium+ time series export. | [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export) |

## Summary tables

### Training load summary

This table lists the metrics in the training load area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [EPOC](#epoc) | Predicted oxygen use above rest after effort | ml/kg | Partly |
| [TRIMP](#trimp) | Training load that grows with time and heart rate intensity | Index, no unit | Partly |
| [TRIMP per minute](#trimp-per-minute) | How fast training load builds | TRIMP per minute | Partly |
| [Aerobic Training Effect](#aerobic-training-effect) | Likely help to VO2max and aerobic endurance | 0.0 to 5.0 | Not published |
| [Anaerobic Training Effect](#anaerobic-training-effect) | Likely help to repeated sprinting and high-intensity ability | 0.0 to 5.0 | Not published |
| [Acute Training Load](#acute-training-load) | TRIMP taken in the last 7 days | Index (TRIMP units) | Yes |
| [Chronic Training Load](#chronic-training-load) | Typical weekly load over 28 days | Index (TRIMP units, weekly amount) | Yes |
| [Acute to chronic workload ratio (ACWR)](#acute-to-chronic-workload-ratio-acwr) | Last 7 days of load against the usual week | Ratio, no unit | Partly |
| [Training Status](#training-status) | How balanced recent training is, with recovery | 0 to 100 | Not published |
| [Manual exercise TRIMP](#manual-exercise-trimp) | Estimated load for an unrecorded session | Index | Not published |
| [Maximal intensity period, TRIMP per minute](#maximal-intensity-period-trimp-per-minute) | Hardest stretch of a session by TRIMP | 1/min | Not published |

### Movement and external load summary

This table lists the metrics in the movement and external load area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Movement Load](#movement-load) | Movement from the Sensor accelerometer | Index, no physical unit | Not published |
| [Movement Intensity](#movement-intensity) | How fast Movement Load builds | Movement Load per minute | Partly |
| [Maximal intensity period, Movement Intensity](#maximal-intensity-period-movement-intensity) | Most intense stretch of movement | kicks/min | Not published |
| [Movement Efficiency](#movement-efficiency) | Movement per unit of heart-rate load | Not stated | Partly |
| [External variables from Garmin](#external-variables-from-garmin) | Speed, distance, and similar Garmin values | As in the name (m, km/h, min/km, W, and others) | Not published |

### Heart rate and zones summary

This table lists the metrics in the heart rate and zones area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Heart rate](#heart-rate) | Heart rate in beats per minute | bpm | Not published |
| [Percent of HRmax](#percent-of-hrmax) | Heart rate as a share of HRmax | Percent | Partly |
| [Time in heart rate zones](#time-in-heart-rate-zones) | Time in each heart rate zone | min in the API, hh:mm:ss in the export. `zone1Time` is the highest zone. | Partly |
| [Heart rate recovery](#heart-rate-recovery) | How fast heart rate falls after hard work | bpm or percent of HRmax | Yes |

### HRV and recovery summary

This table lists the metrics in the hrv and recovery area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [RMSSD](#rmssd) | Beat-to-beat variation of heart rhythm | ms | Yes |
| [SDNN](#sdnn) | Overall spread of the time between beats | ms | Partly |
| [Frequency-domain HRV](#frequency-domain-hrv) | Heartbeat variation in slow, medium, and fast bands | ms^2 for powers | Partly |
| [Quick Recovery Test score](#quick-recovery-test-score) | Recovery from a 3-minute rest test | Index | Not published |
| [Scaled Quick Recovery Test](#scaled-quick-recovery-test) | Test result between the athlete's lowest and highest values | Percent | Not published |
| [Quick Recovery Test 7-day average](#quick-recovery-test-7-day-average) | Average scaled test score over a week | Percent | Partly |
| [Days since last good recovery](#days-since-last-good-recovery) | Days since the last good recovery test | Days | Not published |
| [Perceived recovery](#perceived-recovery) | Athlete's own recovery rating | Whole number, 1 to 5 | Yes |

### Stress and sleep summary

This table lists the metrics in the stress and sleep area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Overnight Recovery](#overnight-recovery) | Overnight recovery against the athlete's history | Percent | Not published |
| [Recovery Index](#recovery-index) | Strength of recovery reactions during sleep | Index | Partly |
| [Sleep duration](#sleep-duration) | How long the athlete slept | min in the API, hh:mm:ss in the export | Not published |
| [24-hour Stress and Recovery Balance](#24-hour-stress-and-recovery-balance) | Whether recovery offsets stress over a day | Percent, 0 to 100 | Not published |
| [Stress time](#stress-time) | Time in a stress state | min in the API | Partly |
| [Relaxation time](#relaxation-time) | Time in a recovery state | min in the API | Partly |
| [Garmin sleep and overnight data](#garmin-sleep-and-overnight-data) | Overnight values from a Garmin watch | bpm for resting heart rate; others Not published | Not published |

### Fitness estimates, oxygen, and breathing summary

This table lists the metrics in the fitness estimates, oxygen, and breathing area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [VO2max](#vo2max) | Estimated maximal oxygen uptake | ml/kg/min | Not published |
| [Oxygen consumption (VO2)](#oxygen-consumption-vo2) | Estimated oxygen use during the measurement | ml/kg/min | Not published |
| [Percent of VO2max](#percent-of-vo2max) | Oxygen use as a share of VO2max | Percent | Partly |
| [Respiration rate](#respiration-rate) | Breaths per minute, estimated from heartbeats | times per minute | Not published |
| [Ventilation](#ventilation) | Estimated air volume breathed per minute | liters per minute | Not published |

### Energy expenditure summary

This table lists the metrics in the energy expenditure area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Energy expenditure, total](#energy-expenditure-total) | Estimated energy used | kcal; kcal/h for the series | Partly |
| [Energy expenditure, carbohydrates and fats](#energy-expenditure-carbohydrates-and-fats) | Split of energy use between carbohydrate and fat | kcal; percent for the series | Not published |

### Data quality and raw signals summary

This table lists the metrics in the data quality and raw signals area:

| Metric | What it measures | Units | Calculation published |
|---|---|---|---|
| [Measurement error](#measurement-error) | Share of beats Firstbeat could not trust | Percent | Partly |
| [Artifact percentage series](#artifact-percentage-series) | Share of beats rejected in each 5-second period | Percent | Yes |
| [Raw RR intervals](#raw-rr-intervals) | Time between heartbeats before correction | ms | Yes |
| [Artifact-corrected RR intervals](#artifact-corrected-rr-intervals) | Heartbeat intervals after artifact correction | ms | Not published |

## Metric details

### Training load

#### EPOC

This list gives the details for EPOC:

- Firstbeat name, API variable, and unit: `EPOC Peak (ml/kg)` and `EPOC (ml/kg)` in the export. API: `epocPeak`, `epocFinal` (ml/kg), and `epocSeries` (ml/kg, 0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How far the body's oxygen use is predicted to stay above resting use after the effort, so how large the recovery demand is.
- Window or phase: Per measurement: the peak, the final value, and a series with 5-second samples (0.2 Hz).
- Calculation: Firstbeat says EPOC is predicted during exercise from current intensity (%VO2max) and time at that intensity. Neural networks estimate intensity from heart rate, an HRV-derived respiration rate, and on and off kinetics ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). The model was built from a meta-analysis of 48 exercise settings and 158 subjects. At intensities below about 30 to 40 %VO2max EPOC does not build much. Above about 50 %VO2max it builds continuously ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf)). Formula: Not published. The white paper gives only the form EPOC(t) = f(EPOC(t-1), exercise intensity(t), time step). This is a restatement of its equation 1. The function f is not given ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf)).
- Defaults: No user-set threshold. The API series has 5-second samples. The export repeats the same value across each 5 seconds so that all series share a 1-second grid ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- Inputs: Beat-to-beat heart rate, HRV-derived respiration rate, and profile values such as HRmax ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf)).
- Units: Ml/kg.
- Variants: Peak (highest value in the measurement), final (value at the end), and the series. Peak EPOC feeds Aerobic Training Effect ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)). Final EPOC falls during a cool-down, so it is a lower number than peak.
- Comparison with standard methods or other vendors: The laboratory method measures oxygen use after exercise and subtracts the resting level. In a cycle ergometer study of 32 adults, Firstbeat's heart-beat EPOC had r-squared 0.79 against measured EPOC. The mean absolute error was 13.7 ml/kg over all data ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf)). In a published test with 25 people and a clinical Holter reference, a chest strap gave a mean absolute percentage error of 3.90% for EPOC and a vest gave 54.15% ([Parak et al., 2021, doi:10.3390/s21248411](https://doi.org/10.3390/s21248411)).
- What changes the number: HRmax and other profile settings, sensor contact, and artifacts. Firstbeat notes that illness, heat, and altitude raise EPOC for the same work. Strength work can show low EPOC even when the athlete feels exhausted, because EPOC mainly reflects aerobic load ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf), [Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/), [Parak et al., 2021, doi:10.3390/s21248411](https://doi.org/10.3390/s21248411), [Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf).

#### TRIMP

This list gives the details for TRIMP:

- Firstbeat name, API variable, and unit: `TRIMP (index)`. API: `trimp` (index) and `trimpSeries` (0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: One number for training load that grows with both time and heart rate intensity.
- Window or phase: Per measurement, lap, session, and day. The series is at 0.2 Hz.
- Calculation: Firstbeat says its TRIMP follows Banister's 1991 TRIMP with two changes. It uses beat-to-beat heart rate instead of a session mean, and it sets a lower intensity limit so only training builds the number ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). Firstbeat notes that TRIMP keeps building when heart rate is above rest even while the body recovers ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)). Formula: Restatement of the figure on the Learning Center page. TRIMP = T x [(HRex - HRrest) / (HRmax - HRrest)] x 0.64 x e^(1.92 x (HRex - HRrest) / (HRmax - HRrest)). T is duration, HRex is heart rate during the workout, HRrest is resting heart rate, and HRmax is maximal heart rate ([TRIMP formula figure](https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-Formula-800x198.jpg), shown on the [Learning Center page](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)). The lower intensity limit is Not published. Whether women use different coefficients is Not published. The figure shows one pair, 0.64 and 1.92.
- Defaults: Coefficients 0.64 and 1.92 as in the figure. HRmax and resting HR come from the profile.
- Inputs: Beat-to-beat heart rate, HRmax, and resting HR.
- Units: Index, with no unit.
- Variants: Per measurement, per lap, per session, per day (for acute and chronic load), and a manual estimate (see Manual exercise TRIMP).
- Comparison with standard methods or other vendors: Firstbeat names Banister's TRIMP as the base. Its version differs by the two changes above. No source in this page compares the two numerically. Firstbeat's version is not interchangeable with a mean-heart-rate TRIMP from another system.
- What changes the number: HRmax and resting HR. A higher HRmax setting shrinks the intensity fraction and lowers TRIMP, and the exponential weight makes the effect larger at high intensity. Artifacts and merged gaps also change it.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/), [TRIMP formula figure](https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-Formula-800x198.jpg).

#### TRIMP per minute

This list gives the details for TRIMP per minute:

- Firstbeat name, API variable, and unit: `TRIMP/min (index)`. API: `trimpPerMinute` (1/min) and `trimpPerMinuteSeries` (1/min, 0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How fast training load builds, so the intensity of a session or drill.
- Window or phase: The divisor is session duration. The period used for laps and measurements is Not published. The series is at 0.2 Hz.
- Calculation: Firstbeat describes it as "TRIMP / Session Duration" ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)). The API describes it as average TRIMP build-up per minute ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Restatement: TRIMP per minute = TRIMP / duration in minutes. The Learning Center says the divisor is session duration. Which period applies to laps and measurements is Not published.
- Defaults: Firstbeat's guideline figure shows these labels: below 70 TRIMP is easy training, 70 to 140 is moderate, and above 140 is hard. It shows 1, 1.5, and 2.2 TRIMP/min for easy, moderate, and hard. The figure does not say where each band starts ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/), figure at [TRIMP/min scale figure](https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-min-Scale-800x437.jpg)). The Sports Guide gives ranges by sport. For men's soccer, TRIMP/min is 0.5-0.8 for easy sessions, 0.9-1.3 for moderate, 1.4-1.8 for hard, and 1.3-1.9 for games ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)).
- Inputs: The same as TRIMP.
- Units: TRIMP per minute.
- Variants: The series, and the highest values over fixed windows (see Maximal intensity period, TRIMP per minute).
- What changes the number: Everything that changes TRIMP, plus the length of the period. A long warm-up or rest in the measurement lowers the average. Clip drills with laps to get the rate for the drill alone ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/), [TRIMP/min scale figure](https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-min-Scale-800x437.jpg), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf).

#### Aerobic Training Effect

This list gives the details for Aerobic Training Effect:

- Firstbeat name, API variable, and unit: `Aerobic TE (0.0-5.0)`. API: `aerobicTrainingEffect` (0.0 to 5.0), not available for laps and sessions. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much one session is likely to help VO2max and aerobic endurance, scaled to the athlete's activity level.
- Window or phase: Per measurement in the export. Firstbeat can show the value at any moment during a session. The API does not return it for laps and sessions.
- Calculation: Firstbeat bases it on the highest EPOC reached aerobically in the session, set against the athlete's activity class ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). Fit and active people need a higher EPOC for the same score. The model updates the limits when the activity level changes ([Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)). Formula: Not published as numbers. The white paper shows a graph in which five lines, one per Training Effect level, rise as activity class rises. The graph is the only statement of the mapping ([Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)).
- Defaults: The bands are 0.0-0.9 no effect, 1.0-1.9 minor, 2.0-2.9 maintaining, 3.0-3.9 improving, 4.0-4.9 highly improving, and 5.0 overreaching ([API variables](https://apidocs.firstbeat.com/variables/)). Activity class runs 0 to 10. Classes 0 to 7 follow Ross and Jackson (1990). Firstbeat added 7.5 to 10. Class 7.5 means 5 to 7 hours of training a week, 8 means 7 to 9, 8.5 means 9 to 11, 9 means 11 to 13, 9.5 means 13 to 15, and 10 means more than 15 hours ([Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)).
- Inputs: Peak EPOC, activity class, HRmax, and maximal respiration rate ([Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)).
- Units: Score from 0.0 to 5.0.
- Variants: Firstbeat can show the value at any moment during a session. The export shows the value for the measurement. The API does not return it for laps or sessions.
- What changes the number: HRmax, maximal respiration rate, and activity class. If any is set too high, Training Effect is underestimated. If any is set too low, it is overestimated. Illness, heat, humidity, and altitude raise it. Long hard training blocks can lower it ([Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf)). A 3.3 is not comparable between two athletes with different activity class settings.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf).

#### Anaerobic Training Effect

This list gives the details for Anaerobic Training Effect:

- Firstbeat name, API variable, and unit: `Anaerobic TE (0.0-5.0)`. API: `anaerobicTrainingEffect` (0.0 to 5.0), not available for laps and sessions. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much one session is likely to help repeated sprinting and other high-intensity ability.
- Window or phase: Live and final values. The API does not return it for laps and sessions.
- Calculation: Firstbeat identifies high-intensity intervals where the anaerobic system is stressed and oxygen deficit rises. It weighs the intensity and speed of the intervals, their duration, the recovery state before each, and the fatigue built up in the session ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). It uses heartbeat dynamics because work can reach 100 to 200% of VO2max while heart rate cannot pass 100% of HRmax ([Anaerobic Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf)). Formula: Not published. The white paper lists qualitative rules only. Faster and harder intervals raise it, shorter intervals raise it more than long ones, and intervals done while fatigued raise it less ([Anaerobic Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf)).
- Defaults: The same bands as Aerobic Training Effect. The white paper says the model can take running speed or cycling power as extra input. Whether Firstbeat Sports uses Sensor movement data in this metric is Not published.
- Inputs: Beat-to-beat heart rate, HRmax, activity class, and profile values.
- Units: Score from 0.0 to 5.0.
- Variants: None beyond the live and final values.
- What changes the number: The same profile settings as Aerobic Training Effect, plus the work and rest pattern. The white paper reports 10 x 50 m runs at aerobic 1.3 and anaerobic 2.1, and an ice hockey game at aerobic 3.2 and anaerobic 3.7 ([Anaerobic Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [Anaerobic Training Effect white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf).

#### Acute Training Load

This list gives the details for Acute Training Load:

- Firstbeat name, API variable, and unit: `Acute Training Load`. API: `acuteTrainingLoad` (index). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much load the athlete took in the last 7 days.
- Window or phase: The last 7 days. Whether the window ends on the measurement day is Not published.
- Calculation: The sum of TRIMP over the last 7 days ([API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Formula: Restatement: acute load = sum of daily TRIMP over the last 7 days. Manual exercise TRIMP counts toward it ([Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud)).
- Defaults: A 7-day window. Whether the window ends on the measurement day is Not published.
- Inputs: Daily TRIMP, including manual exercise TRIMP.
- Units: Index (TRIMP units).
- Variants: Firstbeat compares it with a personalized load scale in Training Status ([Training Status help](https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status)). The API does not return training-history values for days with no measurement ([Known issues](https://apidocs.firstbeat.com/known-issues/)).
- What changes the number: Any gap in recording, because a missed session adds nothing. Add manual exercise for unrecorded sessions.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud), [Training Status help](https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status), [Known issues](https://apidocs.firstbeat.com/known-issues/).

#### Chronic Training Load

This list gives the details for Chronic Training Load:

- Firstbeat name, API variable, and unit: `Chronic Training Load`. API: `chronicTrainingLoad` (index). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The athlete's typical weekly load over the last 28 days.
- Window or phase: The last 28 days, divided by 4.
- Calculation: The TRIMP sum from the past 28 days, divided by 4 ([API variables](https://apidocs.firstbeat.com/variables/)). The Learning Center and the Sports Guide describe it as the load over, or average of, the last 28 days ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). Formula: Restatement: chronic load = (sum of daily TRIMP over 28 days) / 4. The 28 days appear to include the latest 7. Firstbeat does not use the word "coupled".
- Defaults: A 28-day window and the divisor 4.
- Inputs: Daily TRIMP.
- Units: Index (TRIMP units, as a weekly amount).
- Variants: The Training Summary report draws a balanced range of 0.8 to 1.3 times chronic load ([Training Summary report help](https://support.firstbeatsports.com/hc/en-us/articles/40604830199313-What-is-included-in-the-Training-Summary-Report)).
- What changes the number: The same recording gaps as acute load. A new athlete has no real chronic load until about 28 days of history exist. Firstbeat does not state how it treats the first weeks.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary), [Training Summary report help](https://support.firstbeatsports.com/hc/en-us/articles/40604830199313-What-is-included-in-the-Training-Summary-Report).

#### Acute to chronic workload ratio (ACWR)

This list gives the details for Acute to chronic workload ratio (ACWR):

- Firstbeat name, API variable, and unit: `ACWR`. API: `acwr` (ratio). Firstbeat also calls it Load Ratio. [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)
- What it measures: How the last 7 days of load compare with the athlete's usual weekly load.
- Window or phase: Acute load over the last 7 days divided by chronic load over the last 28 days.
- Calculation: Firstbeat divides acute load by chronic load, and shows the result as a color-coded gauge with ranges scaled to each athlete's history ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). Formula: Restatement: ACWR = acute training load / chronic training load. In sum form this is the coupled rolling-average ACWR described in [the ACWR reference](../../skills/load-and-wellness/references/acwr.md). The numeric limits of the gauge colors are Not published.
- Defaults: Firstbeat says to aim for about 0.8 to 1.3 ([Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/)).
- Inputs: Acute and chronic training load.
- Units: Ratio, with no unit.
- Variants: The dashboard gauge, the Load Ratio in reports, and the balanced range of 0.8 to 1.3 times chronic load.
- What changes the number: The 7-day and 28-day windows, recording gaps, and manual exercise entries.
- Caution: Firstbeat says a high ACWR places the athlete at increased injury risk ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). The repository's ACWR reference reaches a different conclusion. ACWR describes how recent load compares with longer-term load. It does not predict injury.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [Learning Center, Interpreting training data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/).

#### Training Status

This list gives the details for Training Status:

- Firstbeat name, API variable, and unit: `Training Status (0-100)`. API: `playerStatusScore` (0 to 100), a Premium+ variable that needs the `training_status` service. [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/)
- What it measures: How balanced the athlete's recent training is, with recovery included.
- Window or phase: TRIMP history for 7 and 28 days, and Quick Recovery Test history for 14 days.
- Calculation: Firstbeat combines acute training load compared with a personalized scale, ACWR, and recovery. Recovery is the average of the three most recent Quick Recovery Tests, with newer tests weighted more. The recovery part is applied only if at least three tests exist in the last 14 days. Firstbeat weights the data for reliability and availability ([Training Status help](https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status)). Formula: Not published. The weights and the personalized scales are not given.
- Defaults: Above 70 is well balanced, 30 to 70 is moderately balanced, and below 30 is out of balance ([Training Status help](https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status)).
- Inputs: TRIMP history for 7 and 28 days, and Quick Recovery Test history for 14 days.
- Units: Score from 0 to 100.
- Variants: Firstbeat calls Training Status, acute load, chronic load, and ACWR "training history" variables. They are daily values that are not tied to one measurement or session ([Terminology](https://apidocs.firstbeat.com/terminology/)). The export also lists Training Status for the recorded session ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- What changes the number: How often you run Quick Recovery Tests, the same load inputs as ACWR, and HRmax. The subscription level that includes it is not stated the same way everywhere. The 2021 brochure lists Training Status under Premium. The API page lists it as Premium+ ([Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf), [API variables](https://apidocs.firstbeat.com/variables/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/), [Training Status help](https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status), [Terminology](https://apidocs.firstbeat.com/terminology/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf).

#### Manual exercise TRIMP

This list gives the details for Manual exercise TRIMP:

- Firstbeat name, API variable, and unit: `TRIMP (index)` on a manual measurement. The API reports `measurementType` as `manual`. [Basic concepts](https://apidocs.firstbeat.com/basic-concepts/)
- What it measures: An estimated load for a session that nobody recorded.
- Window or phase: One manual measurement with a start time and a duration.
- Calculation: Firstbeat estimates TRIMP from the duration and an intensity rating from 1 to 10 that the user enters. The estimate uses over 1.2 million measurements from the Firstbeat database, fatigue in longer sessions, and the stop-start nature of team sessions ([Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud)). Formula: Not published.
- Defaults: None stated.
- Inputs: Start time, duration, and the 1 to 10 intensity rating.
- Units: Index.
- Variants: The API FAQ says a manual measurement has only start time, end time, TRIMP, and duration ([API FAQ](https://apidocs.firstbeat.com/faq/)). The manual exercise help article lists more. A manual measurement carries start time, end time, duration, TRIMP, TRIMP per minute, acute load, chronic load, ACWR, Training Status, notes, and sports type. No heart-rate variables exist for it ([Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud)).
- What changes the number: The rating the user picks. Do not average a manual TRIMP with measured TRIMP as if both were measured. Flag these rows with `measurementType` of `manual`.
- Sources: [Basic concepts](https://apidocs.firstbeat.com/basic-concepts/), [Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud), [API FAQ](https://apidocs.firstbeat.com/faq/).

#### Maximal intensity period, TRIMP per minute

This list gives the details for Maximal intensity period, TRIMP per minute:

- Firstbeat name, API variable, and unit: `Maximal Intensity Period TRIMP/min 30s` to `2h`. API: `trimpPerMinHighest30s`, `trimpPerMinHighest45s`, `trimpPerMinHighest1min`, `trimpPerMinHighest2min`, `trimpPerMinHighest3min`, `trimpPerMinHighest4min`, `trimpPerMinHighest5min`, `trimpPerMinHighest10min`, `trimpPerMinHighest15min`, `trimpPerMinHighest20min`, `trimpPerMinHighest30min`, `trimpPerMinHighest45min`, `trimpPerMinHighest1h`, `trimpPerMinHighest2h` (1/min). Premium+, exercise measurements only. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The hardest stretch of a session for a stated length of time.
- Window or phase: 14 window lengths from 30 seconds to 2 hours. Exercise measurements only.
- Calculation: Firstbeat defines a maximal intensity period as the highest intensity over the session for the stated duration. Its example is the highest TRIMP per minute over any 4 minutes ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). The API describes the value as the highest increase in TRIMP over the period. The API unit is 1/min, so it is not clear whether the value is a total over the window or a per-minute rate. Treat it as Not confirmed. Formula: Not published.
- Defaults: The window lengths in the variable names.
- Inputs: The TRIMP series.
- Units: 1/min, as the API lists.
- Variants: 14 window lengths.
- What changes the number: The window length, the sampling of the TRIMP series (5 seconds), and short artifacts. Do not compare a 30-second value with a 2-hour value.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary).

### Movement and external load

#### Movement Load

This list gives the details for Movement Load:

- Firstbeat name, API variable, and unit: `Movement Load (index)`. API: `movementLoad` (index), `movementLoadSeries`, and `movementLoadAccumulationRate` (1/min, 0.2 Hz). `movementLoadSeries` is not available for laps and sessions. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much the athlete moved, from the Sensor's accelerometer.
- Window or phase: Per measurement. The value accumulates over a session. `movementLoadSeries` is not available for laps and sessions.
- Calculation: Firstbeat says the accelerometer in the Sensor captures movement in any direction and the value accumulates over a session. It calls Movement Load the external load equivalent of TRIMP ([Learning Center, Interpreting movement data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). The Sensor holds a 9-axis motion sensor ([Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications)). Formula: Not published.
- Defaults: None. Firstbeat's reference values for men's soccer are 128-206 for easy sessions, 188-283 for moderate, 262-397 for hard, and 341-553 for games. For women's soccer they are 101-186, 146-242, 223-369, and 358-521 ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)).
- Inputs: The chest-worn Sensor's accelerometer.
- Units: Index. No physical unit is stated.
- Variants: Total, accumulation rate series, and per-minute intensity.
- Comparison with standard methods or other vendors: In an interunit test with eight professional basketball players and 50 sessions, two Sensors worn together agreed. The coefficient of variation was 2.51% to 5.97% and the intraclass correlation was .98 to 1.00 ([Conte et al., 2025, doi:10.1123/ijspp.2024-0289](https://doi.org/10.1123/ijspp.2024-0289)). No source here compares Movement Load with another vendor's accelerometer load. Do not treat them as equal.
- What changes the number: How the athlete moves. Firstbeat says people who move smoothly collect less for the same work, and men and women differ most here ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). Interpret it next to TRIMP. The subscription tier is stated differently in different places. The Sensor page and the brochure say Premium. The API page marks the series and Movement Intensity variables as Premium+.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Interpreting movement data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary), [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf), [Conte et al., 2025, doi:10.1123/ijspp.2024-0289](https://doi.org/10.1123/ijspp.2024-0289).

#### Movement Intensity

This list gives the details for Movement Intensity:

- Firstbeat name, API variable, and unit: `Average Movement Intensity (index)`. API: `averageMovementIntensity` (index), a Premium+ variable. The Sensor page names the unit as ML/min. [API variables](https://apidocs.firstbeat.com/variables/), [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications)
- What it measures: How fast Movement Load builds, so the movement rate of a session.
- Window or phase: The average over a measurement.
- Calculation: The average of the Movement Load accumulation rate during a measurement ([Terminology](https://apidocs.firstbeat.com/terminology/)). Formula: Restatement: Movement Intensity is about Movement Load / duration. Firstbeat words it as an average accumulation rate. The exact formula is Not published.
- Defaults: None.
- Inputs: The Movement Load series.
- Units: Movement Load per minute. The maximal-period variables use the label kicks/min.
- Variants: Average, series, and the maximal periods below.
- What changes the number: The same factors as Movement Load, and the length of the period, as with TRIMP per minute. Merged gaps count as no movement ([Trim and merge](https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications), [Terminology](https://apidocs.firstbeat.com/terminology/), [Trim and merge](https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud).

#### Maximal intensity period, Movement Intensity

This list gives the details for Maximal intensity period, Movement Intensity:

- Firstbeat name, API variable, and unit: `Maximal Intensity Period MI 5s` to `MI 2h`. API: `movementIntensityHighest5s`, `movementIntensityHighest10s`, `movementIntensityHighest15s`, `movementIntensityHighest20s`, `movementIntensityHighest30s`, `movementIntensityHighest45s`, `movementIntensityHighest1min`, `movementIntensityHighest2min`, `movementIntensityHighest3min`, `movementIntensityHighest4min`, `movementIntensityHighest5min`, `movementIntensityHighest10min`, `movementIntensityHighest15min`, `movementIntensityHighest20min`, `movementIntensityHighest30min`, `movementIntensityHighest45min`, `movementIntensityHighest1h`, `movementIntensityHighest2h` (kicks/min). Premium+, exercise measurements only, and they need the `movement_intensity_curve` service. [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/)
- What it measures: The most intense stretch of movement for a stated length of time.
- Window or phase: 18 window lengths from 5 seconds to 2 hours. Exercise measurements only.
- Calculation: The API describes each value as the highest increase in movement load over the window ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Not published.
- Defaults: The window lengths in the variable names.
- Inputs: The Movement Load series.
- Units: Kicks/min, as the API lists.
- Variants: 18 window lengths.
- What changes the number: The window length and movement style. Do not compare windows of different length.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/).

#### Movement Efficiency

This list gives the details for Movement Efficiency:

- Firstbeat name, API variable, and unit: `Movement Efficiency`. API: `movementEfficiency`, added on 2025-10-22 for Premium+. It is not in the Variables page list. [API changelog](https://apidocs.firstbeat.com/changelog/)
- What it measures: How much movement the athlete produced for each unit of heart-rate load.
- Window or phase: Per measurement.
- Calculation: Firstbeat describes it as the ratio between external and internal load, used as an indicator of endurance performance ([What's new in Sports products](https://www.firstbeat.com/en/whats-new-sports-products/)). The Learning Center defines "Movement Efficiency" for its article as Movement Load / TRIMP ([Learning Center, Interpreting movement data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/)). Formula: Restatement: Movement Efficiency = Movement Load / TRIMP. Whether the exported variable uses exactly this ratio is Not confirmed.
- Defaults: None.
- Inputs: Movement Load and TRIMP.
- Units: Not stated.
- Variants: Per measurement, and as a summary-card variable in custom reports ([Custom session reports](https://support.firstbeatsports.com/hc/en-us/articles/40603643127057-How-to-create-Custom-Session-Reports)).
- What changes the number: Every input of both Movement Load and TRIMP, so HRmax and resting HR move the denominator. Firstbeat cites studies in which ratios of external to internal load track fitness. Its own example plots Yo-Yo test scores against each athlete's average ratio over the next two months. Athletes with better scores generally had a higher ratio ([Learning Center, Interpreting movement data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/)).
- Sources: [API changelog](https://apidocs.firstbeat.com/changelog/), [What's new in Sports products](https://www.firstbeat.com/en/whats-new-sports-products/), [Learning Center, Interpreting movement data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/), [Custom session reports](https://support.firstbeatsports.com/hc/en-us/articles/40603643127057-How-to-create-Custom-Session-Reports).

#### External variables from Garmin

This list gives the details for External variables from Garmin:

- Firstbeat name, API variable, and unit: `Distance (m or mi)`, `Average Speed (km/h or mph)`, `Pace (min/km or min/mi)`, `Power (W)`, `Cadence (rpm)`, `Ascent`, `Descent`. API: `distance` (m), `speedAverage` (km/h), `pace` (min/km), `powerAverage` (W), `cadenceAverage` (1/min), `ascent` (m), `descent` (m). All are not available for laps and sessions. [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)
- What it measures: Speed, distance, and similar values that a Garmin watch recorded.
- Window or phase: The whole Garmin recording. Not available for laps and sessions.
- Calculation: Firstbeat passes these through from the Garmin recording. It does not calculate them. The export labels them "Garmin variables (if available)". Formula: Not a Firstbeat calculation.
- Defaults: Units follow the account setting, for example m or mi.
- Inputs: A Garmin activity synced through Garmin Connect ([Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API)).
- Units: As in the name.
- Variants: None.
- What changes the number: The Garmin device and its settings. These values are missing for sessions recorded only with the Firstbeat Sensor.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API).

### Heart rate and zones

#### Heart rate

This list gives the details for Heart rate:

- Firstbeat name, API variable, and unit: `Average Heart Rate (bpm)`, `Peak Heart Rate (bpm)`, `Minimum Heart Rate (bpm)`. API: `heartRateAverage`, `heartRatePeak`, `heartRateLowest` (1/min), `heartRateSeries` (1/min, 0.2 Hz), `heartRateSeries1s` (1/min, 1 Hz). The export has `Artifact corrected heart rate` as a time series. [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)
- What it measures: Heart rate in beats per minute.
- Window or phase: Per measurement. The series are at 5 seconds and 1 second.
- Calculation: Firstbeat calculates average heart rate from the recorded session for each player ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). It derives heart rate from artifact-corrected beat-to-beat data. Formula: Restatement of the standard form: heart rate in bpm = 60000 / RR interval in ms. Firstbeat does not print a formula. How it averages (by time or by beat) is Not published.
- Defaults: None.
- Inputs: RR intervals from the Sensor, or heart rate levels from a Garmin optical sensor.
- Units: Bpm.
- Variants: The series at 5 seconds and 1 second, and the lowest value.
- What changes the number: Sensor contact and artifacts. A Garmin optical wrist measurement carries heart rate levels but no RR data ([Heart Rate Recovery help](https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery)). Merged gaps fill with about 100 bpm ([Trim and merge](https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Heart Rate Recovery help](https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery), [Trim and merge](https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud).

#### Percent of HRmax

This list gives the details for Percent of HRmax:

- Firstbeat name, API variable, and unit: `Average %HRmax (%)`, `Peak %HRmax (%)`, `Minimum %HRmax (%)`. API: `heartRateAveragePercentage`, `heartRatePeakPercentage`, `heartRateMinimumPercentage` (%), and `heartRatePercentageSeries` (0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: Heart rate as a share of the athlete's maximum heart rate.
- Window or phase: Average, peak, minimum, and a series at 0.2 Hz.
- Calculation: Firstbeat calculates it from the maximum heart rate set in the profile ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Formula: Restatement of the name: %HRmax = heart rate / HRmax x 100. Firstbeat does not print the formula.
- Defaults: HRmax from the profile.
- Inputs: Heart rate and HRmax.
- Units: Percent.
- Variants: Average, peak, minimum, and a series. The API Variables page lists the series unit as 1/min. This looks like an error for a percent series.
- What changes the number: The HRmax setting, directly. A wrong HRmax shifts every %HRmax by the same ratio. Two entries in the API table also map `heartRatePeakPercentage` and `heartRateMinimumPercentage` to export names that read "Peak HR (bpm)" and "Minimum HR (bpm)". Treat that mapping as Not confirmed.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export).

#### Time in heart rate zones

This list gives the details for Time in heart rate zones:

- Firstbeat name, API variable, and unit: `High intensity training`, `Anaerobic threshold zone`, `Aerobic zone 2`, `Aerobic zone 1`, `Recovery training`, and `Time Under Zones` (hh:mm:ss in the export). API: `zone1Time` to `zone5Time` and `underZonesTime` (min). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How long the athlete spent in each heart rate zone.
- Window or phase: Total time in each zone over the measurement.
- Calculation: Firstbeat sorts exercise intensity into zones by percent of personal maximum heart rate ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Time in zone = total time with heart rate inside the zone limits (restatement).
- Defaults: The zone names and the order are in the table after this list. The default %HRmax limits are Not published in the sources read. Firstbeat recommends the same zone limits for everyone unless you have individual test data ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)).
- Inputs: Heart rate, HRmax, and the account's zone limits.
- Units: Min in the API, hh:mm:ss in the export.
- Variants: Names are editable by account, so names alone do not identify a zone. Use the limits.
- What changes the number: HRmax and any change to the zone limits. Changing limits does not rewrite old sessions unless Firstbeat recalculates them. This is not confirmed.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/), [Known issues](https://apidocs.firstbeat.com/known-issues/), [Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf).

Zone numbering note for this metric:

The API numbers the zones in the opposite order from the app. This table shows the mapping from the API documentation:

| API variable | Export name |
|---|---|
| `zone1Time` | High intensity training |
| `zone2Time` | Anaerobic threshold zone |
| `zone3Time` | Aerobic zone 2 |
| `zone4Time` | Aerobic zone 1 |
| `zone5Time` | Recovery training |
| `underZonesTime` | Time Under Zones |

Firstbeat confirms this in its known issues: in the API, zone 1 is the highest zone ([Known issues](https://apidocs.firstbeat.com/known-issues/)). The Sports Guide's "Zone 5 duration" reference values are, by this mapping, the time in the high intensity zone ([Sports Guide, Training Load](https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf)). That reading is an inference, and Firstbeat does not state it.

#### Heart rate recovery

This list gives the details for Heart rate recovery:

- Firstbeat name, API variable, and unit: `HR Recovery (30s, bpm)`, `HR Recovery (60s, bpm)`, `HR Recovery (120s, bpm)`, `HR Recovery (30s, %)`, `HR Recovery (60s, %)`, `HR Recovery (120s, %)`. API: `heartRateRecoveryAbsolute30s`, `heartRateRecoveryAbsolute60s`, `heartRateRecoveryAbsolute120s` (1/min), `heartRateRecoveryRelative30s`, `heartRateRecoveryRelative60s`, `heartRateRecoveryRelative120s` (%). Premium+, and they need the `heart_rate_recovery` service. [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/)
- What it measures: How fast heart rate falls after hard work.
- Window or phase: Rolling windows of 15, 30, 60, and 120 seconds, for measurements, sessions, and laps. The best value shows when a day has more than one measurement.
- Calculation: Firstbeat measures how fast heart rate decreases in a rolling window and calculates it for all measurements, sessions, and laps. It skips data that is not reliable and all abnormally high drops. If an athlete has more than one measurement in a day, it shows the best value ([Heart Rate Recovery help](https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery)). It needs RR data. Formula: Restatement: the absolute value is the largest drop in heart rate (bpm) over a window of 30, 60, or 120 seconds. The relative value is the largest recovery in bpm / athlete HRmax x 100 ([Heart Rate Recovery help](https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery)).
- Defaults: Windows of 15, 30, 60, and 120 seconds are calculated. The API lists 30, 60, and 120.
- Inputs: RR data and HRmax.
- Units: Bpm or percent of HRmax.
- Variants: Absolute and relative, and four windows. The Submaximal Fitness Test report uses Heart Rate Recovery (60s, %) and Peak %HRmax (60s) ([Submaximal Fitness Test report](https://support.firstbeatsports.com/hc/en-us/articles/40637753745937-What-is-included-in-the-Submaximal-Fitness-Test-Report)).
- What changes the number: The part of the data you pick (lap or session), HRmax for the relative value, and data quality. A missing value can mean poor data quality. A Garmin optical measurement cannot produce the value.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/), [Heart Rate Recovery help](https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery), [Submaximal Fitness Test report](https://support.firstbeatsports.com/hc/en-us/articles/40637753745937-What-is-included-in-the-Submaximal-Fitness-Test-Report).

### HRV and recovery

#### RMSSD

This list gives the details for RMSSD:

- Firstbeat name, API variable, and unit: `RMSSD (ms)`, `RMSSD Awake (ms)`, `RMSSD Sleep (ms)`. API: `rmssd`, `rmssdSleepAverage`, `rmssdNonSleepAverage` (ms, the last two only for stress and recovery measurements), and `rmssd1MinSeries`. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much the time between heartbeats varies from one beat to the next, which is a common measure of rest-state HRV.
- Window or phase: The whole measurement, awake and sleep averages, and a series. The series sampling interval is Not confirmed.
- Calculation: Firstbeat defines it as the root mean square of the successive differences in RR intervals, "the most used parameter to describe the level of HRV at rest" ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). Formula: Restatement: RMSSD = sqrt( mean( (RR[i+1] - RR[i])^2 ) ), in ms. The worked example at the end of this page runs it.
- Defaults: A Quick Recovery Test lasts 3 minutes ([QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app)). Firstbeat says night RMSSD should be about double the daytime QRT value ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/)).
- Inputs: Artifact-corrected RR intervals. Firstbeat runs RR data through an artifact filter before HRV analysis ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). The sources do not say that the exported `rmssd` always uses corrected data.
- Units: Ms.
- Variants: Whole measurement, awake and sleep averages, and a series. The series name says 1 minute and the API table shows 0.02 Hz with the text "5min sample rate". The export says 1 minute. The sampling interval is Not confirmed ([API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). The meaning of `rmssd` on an exercise measurement is not stated. Use RMSSD from Quick Recovery Tests and overnight measurements.
- Comparison with standard methods or other vendors: Firstbeat compared its Bodyguard 2 device with a clinical ECG in 19 people. Before artifact correction the RMSSD error was 9.87 ms overall and 20.54 ms during running. After Firstbeat's artifact correction the mean RMSSD difference was -1.30 ms ([Parak and Korhonen, Bodyguard 2 accuracy](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf)). This is a conference paper hosted by Firstbeat, not a journal article.
- What changes the number: Artifacts (see the worked example), posture (use supine or seated, never both), time of day, and test length. Firstbeat says to keep the protocol the same ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)). Sensor contact and sensor model matter too.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary), [QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/), [Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Parak and Korhonen, Bodyguard 2 accuracy](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf), [Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/).

#### SDNN

This list gives the details for SDNN:

- Firstbeat name, API variable, and unit: `SDNN (ms)`. API: `sdnn` (ms). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The overall spread of the time between heartbeats.
- Window or phase: Not stated by the vendor.
- Calculation: Firstbeat describes it as the standard deviation of normal-to-normal RR intervals ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Restatement of the standard definition: the standard deviation of the NN intervals in ms. Firstbeat does not print a formula.
- Defaults: None.
- Inputs: Artifact-corrected RR intervals.
- Units: Ms.
- Variants: None.
- What changes the number: Artifacts and record length. The newer Data Export dropped SDNN because some variables "might not meet our quality criteria anymore" ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). The API Variables page still lists it. Treat it as low confidence.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export).

#### Frequency-domain HRV

This list gives the details for Frequency-domain HRV:

- Firstbeat name, API variable, and unit: `LF/HF (%)`, `LF Average (ms^2)`, `HF Average (ms^2)`, `VLF Average (ms^2)`. API: `lfHfRatio`, `lfAverage`, `hfAverage`, `vlfAverage`, and the 1 Hz series `lfSeries`, `hfSeries`, `vlfSeries` (ms^2). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How much of the heartbeat variation falls in slow, medium, and fast frequency bands.
- Window or phase: Averages and 1 Hz series.
- Calculation: Firstbeat's 24-hour method uses a short-time Fourier transform, with high frequency power at 0.15 to 0.40 Hz and low frequency power at 0.04 to 0.15 Hz. It resamples RR data to 5 Hz and filters it between 0.03 and 1.2 Hz first ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). The VLF band limits are Not published in the sources read. The paper dates from 2014, and the exported variables may use updated settings. Formula: Not published beyond the band limits above. `lfHfRatio` is a ratio between LF and HF power. The API text names HF first and LF second, the export name is `LF/HF (%)`, and the API lists the unit as "%". The order is Not confirmed.
- Defaults: The bands above.
- Inputs: Artifact-corrected RR intervals.
- Units: Ms^2 for powers.
- Variants: Average and series.
- What changes the number: Breathing rate, posture, and artifacts. HF, LF, and the ratio are not in the newer Data Export for the same quality reason as SDNN ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Treat them as low confidence.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export).

#### Quick Recovery Test score

This list gives the details for Quick Recovery Test score:

- Firstbeat name, API variable, and unit: `Quick Recovery Test (index)`. API: `quickRecoveryTestScore` (index, described as a 0 to 100% personalized result). It exists only on quick recovery measurements. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How recovered the athlete looks in a 3-minute rest test, compared with their own history.
- Window or phase: A 3-minute rest test. If two tests fall in one day, Firstbeat shows the higher score.
- Calculation: The Sensor records beat-to-beat data for 3 minutes. Firstbeat takes the RMSSD and the average RR interval and turns them into a percentage score ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)). The Sensor calculates the result at once, using history from the Cloud. The first test is a baseline and the second shows results ([QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app)). Formula: Not published.
- Defaults: The coach app shows four categories: 0-30 Poor, 30-70 Moderate, 70-90 Good, and 90-100 Excellent. Firstbeat does not say which of the two QRT values the bands apply to ([QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app)). The ideal timing is about 10 minutes after waking, or at a fixed time before training ([Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/)).
- Inputs: RR data for 3 minutes, and the athlete's test history.
- Units: Index.
- Variants: When two tests exist in one day, Firstbeat shows the higher score. A recording of 5 minutes or less can be converted to a test ([QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app), [Edit or delete measurements](https://support.firstbeatsports.com/hc/en-us/articles/360016072097-How-to-edit-or-delete-individual-measurements-in-Firstbeat-Sports-Cloud)).
- What changes the number: Test timing, posture, caffeine, meals, and movement. Firstbeat says to avoid them before the test. It also says an app that stays offline for a long time can shift history slightly when it later syncs ([QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app)). Read trends, not single tests ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Introduction](https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/), [QRT help](https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app), [Edit or delete measurements](https://support.firstbeatsports.com/hc/en-us/articles/360016072097-How-to-edit-or-delete-individual-measurements-in-Firstbeat-Sports-Cloud), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/).

#### Scaled Quick Recovery Test

This list gives the details for Scaled Quick Recovery Test:

- Firstbeat name, API variable, and unit: `Quick Recovery (%)`. API: `quickRecoveryScaledScore` (%). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The test result placed between the athlete's lowest and highest test values.
- Window or phase: One test, scaled to the athlete's history. The history window is Not published.
- Calculation: Firstbeat scales the QRT index using the athlete's minimum and maximum QRT index value ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Not published. Min-max scaling is an inferred reading of the description: scaled = (index - min) / (max - min) x 100. The history window for min and max is Not published.
- Defaults: None stated.
- Inputs: The QRT index and the athlete's history.
- Units: Percent.
- Variants: None.
- What changes the number: The athlete's own history. If every test is low, the scaled value can still look normal. Firstbeat tells you to check RMSSD as well ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/).

#### Quick Recovery Test 7-day average

This list gives the details for Quick Recovery Test 7-day average:

- Firstbeat name, API variable, and unit: `Quick recovery test (7 days average) (%)`. API: `scaledQrtWeeklyMean` (%). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The athlete's average scaled test score over the last week.
- Window or phase: The last 7 days.
- Calculation: Firstbeat describes it as the athlete's individual 7-day average ([API variables](https://apidocs.firstbeat.com/variables/)). It prefers this value to a single test for recovery status, and suggests a 3 or 4-day rolling average in exports ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/)). Formula: Restatement: the mean of scaled QRT values over 7 days. How days with no test are handled is Not published.
- Defaults: A 7-day window.
- Inputs: Scaled QRT values.
- Units: Percent.
- Variants: None.
- What changes the number: Test frequency. With few tests, one result dominates the average.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/).

#### Days since last good recovery

This list gives the details for Days since last good recovery:

- Firstbeat name, API variable, and unit: `Quick recovery test (Time since good recovery) (Days)`. API: `daysSinceLastGoodRecovery` (days). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How many days have passed since the athlete's last good recovery test.
- Window or phase: Counted from the last good recovery test. The rule for "good" is Not published.
- Calculation: Firstbeat gives only the description above. Formula: Not published. The rule for "good" is Not published.
- Defaults: None stated.
- Inputs: QRT history.
- Units: Days.
- Variants: None.
- What changes the number: How often you test. Firstbeat fixed incorrect values of this variable on 2024-07-15, so older pulls may be wrong ([API changelog](https://apidocs.firstbeat.com/changelog/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/).

#### Perceived recovery

This list gives the details for Perceived recovery:

- Firstbeat name, API variable, and unit: `Perceived recovery`. API: `perceivedRecovery` (1 to 5), not available for laps and sessions. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The athlete's own rating of recovery after a test.
- Window or phase: Entered after a Quick Recovery Test. Not available for laps and sessions.
- Calculation: The athlete adds it in the Athlete app after a Quick Recovery Test ([QRT help, Athlete app](https://support.firstbeatsports.com/hc/en-us/articles/7894987881233-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Athlete-app)). Formula: None. It is a rating.
- Defaults: None. Which end of the scale is best is Not published.
- Inputs: The athlete's answer.
- Units: Whole number from 1 to 5.
- Variants: None.
- What changes the number: The athlete's mood and the wording of the question. Check the scale direction with the Sports Cloud before you use it.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [QRT help, Athlete app](https://support.firstbeatsports.com/hc/en-us/articles/7894987881233-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Athlete-app).

### Stress and sleep

#### Overnight Recovery

This list gives the details for Overnight Recovery:

- Firstbeat name, API variable, and unit: `Overnight Recovery (%)`. The API Variables page has no variable with this name. The closest listed variable is `sleepRecoveryIndexAbsolute`. [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How well the athlete recovered overnight, compared with their own history.
- Window or phase: One overnight measurement.
- Calculation: Firstbeat describes a score based on HRV and sleep duration, individualized to the athlete ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). A 0 to 100% recovery score is influenced by sleep quality (HRV and the Recovery Index) and by automatically detected sleep duration ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/), annotated report image). Formula: Not published.
- Defaults: A 2021 example report shows sleep bands of under 6.5 hours, 6.5 to 8 hours, and 8 to 9 hours as poor, moderate, and good. The same example shows Recovery Index bands of 58-74, 74-96, and 96-112 ([Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf)). These cut points come from one example report. Do not treat them as current defaults.
- Inputs: An overnight RR measurement, such as one from the Bodyguard 3 ([Bodyguard 3 help](https://support.firstbeatsports.com/hc/en-us/articles/4419781074705-Stress-and-recovery-measurements-using-the-Firstbeat-Bodyguard-3-device)).
- Units: Percent.
- Variants: None.
- What changes the number: Sleep duration, sleep timing, the first night's baseline, and artifacts. Overnight measurements are a Premium feature ([Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf)).
- Sources: [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [API variables](https://apidocs.firstbeat.com/variables/), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf), [Bodyguard 3 help](https://support.firstbeatsports.com/hc/en-us/articles/4419781074705-Stress-and-recovery-measurements-using-the-Firstbeat-Bodyguard-3-device).

#### Recovery Index

This list gives the details for Recovery Index:

- Firstbeat name, API variable, and unit: `Overnight recovery Index (index)` and `Recovery Index (absolute)`. API: `sleepRecoveryIndexAbsolute` (index, stress and recovery measurements only). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How strong the body's recovery reactions were during sleep.
- Window or phase: The 4-hour window that starts 30 minutes after going to bed.
- Calculation: Firstbeat calculates it from heart rate level, HRV (low and high frequency power), and an HRV-based respiration rate. The values come second by second from a short-time Fourier transform, and data filtering selects representative periods. Firstbeat then scales the values to the user's measurement history. For sleep it uses the 4-hour window that starts 30 minutes after going to bed ([Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf), [API variables](https://apidocs.firstbeat.com/variables/)). Formula: Not published.
- Defaults: The 4-hour window that starts 30 minutes after going to bed.
- Inputs: RR data for the night.
- Units: Index.
- Variants: The name "absolute" suggests an unscaled form, while the white paper describes scaling to the history. Which one this variable holds is Not confirmed.
- What changes the number: Whether the athlete fell asleep fast, because the window starts 30 minutes after going to bed. A late sleep start puts light sleep inside the window. Firstbeat shows one example in which an overtrained athlete's Recovery Index range was 15 to 68 and a top performer's was 100 to 270. These are one example, not norms ([Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf), [Learning Center, Interpreting recovery data](https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/).

#### Sleep duration

This list gives the details for Sleep duration:

- Firstbeat name, API variable, and unit: `Sleep duration (hh:mm:ss)`. API: `sleepStateTime` (min, stress and recovery measurements only). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How long the athlete slept in the measurement.
- Window or phase: One stress and recovery measurement.
- Calculation: Firstbeat's sleep method uses a neural network with beat-to-beat data, HRV-derived respiration, wrist or body movement, and time of day. It needs age, height, weight, and sex ([Sleep white paper](https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf)). The paper describes a wearable method, and the sources do not confirm that the Bodyguard 3 analysis in Sports Cloud uses the same model. Formula: Not published.
- Defaults: None.
- Inputs: RR data and acceleration data.
- Units: Min in the API, hh:mm:ss in the export.
- Variants: None.
- Comparison with standard methods or other vendors: Against polysomnography in 110 adults, Firstbeat's method told sleep from wake with 94% sensitivity and 63% specificity. Its epoch-by-epoch agreement across sleep stages was 66% ([Sleep white paper](https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf)). In a peer-reviewed study of 20 adults over 40 nights, wake detection had accuracy 0.93, and Firstbeat overestimated wake time by a mean 14 minutes and underestimated REM sleep by 18 minutes ([Kuula and Pesonen, 2021, doi:10.2196/24704](https://doi.org/10.2196/24704)).
- What changes the number: Movement data, sensor contact, and the first sleep-onset estimate. An overestimate of wake time shortens sleep duration.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Sleep white paper](https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf), [Kuula and Pesonen, 2021, doi:10.2196/24704](https://doi.org/10.2196/24704).

#### 24-hour Stress and Recovery Balance

This list gives the details for 24-hour Stress and Recovery Balance:

- Firstbeat name, API variable, and unit: `24h Stress & Recovery Balance (%)`. API: `firstbeatPointsStressBalance` (0 to 100, night measurements only). [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/)
- What it measures: Whether recovery periods offset the stress reactions across a day.
- Window or phase: A 24-hour measurement. A partial day gives no value.
- Calculation: Firstbeat detects stress, recovery, and physical activity from beat-to-beat data. It then estimates whether the body's resources built up or were used, by weighing the strength and the duration of the reactions ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). It is only available for 24-hour measurements ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Formula: Not published.
- Defaults: In the 2021 example report, a 60% balance is labeled moderate. Stress at 63% of time and recovery at 29% of time are shown with cut points of 60% and 50% for stress and 20% and 30% for recovery ([Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf)). These come from an example report.
- Inputs: A 24-hour RR and acceleration recording.
- Units: Percent, from 0 to 100.
- Variants: None.
- What changes the number: Recording length (a partial day gives no value), artifacts, and activity detection. Firstbeat treats a segment with more than 75% artifacts as an unrecognized state ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [API changelog](https://apidocs.firstbeat.com/changelog/), [Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf).

#### Stress time

This list gives the details for Stress time:

- Firstbeat name, API variable, and unit: `Stress time (hh:mm:ss)`. API: `stressStateTime` (min, stress and recovery measurements only). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How long the athlete's body was in a stress state.
- Window or phase: One stress and recovery measurement.
- Calculation: Stress is detected when heart rate is up and HRV is down without a metabolic need from physical activity ([Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf)). A segment counts as physical activity when estimated VO2 is above 30% of VO2max. A segment between 20 and 30% counts as daily activity ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). Formula: Not published.
- Defaults: The VO2 thresholds above.
- Inputs: RR data, estimated VO2, and acceleration.
- Units: Min in the API.
- Variants: Firstbeat says stress reactions can be good (excitement) or bad (anxiety) ([Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). The number does not tell which.
- What changes the number: VO2max and HRmax settings, which set the activity thresholds. Artifacts also change it.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf), [Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary).

#### Relaxation time

This list gives the details for Relaxation time:

- Firstbeat name, API variable, and unit: `Relaxation time (hh:mm:ss)`. API: `recoveryStateTime` (min, stress and recovery measurements only). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How long the athlete's body was in a recovery state.
- Window or phase: One stress and recovery measurement.
- Calculation: Recovery is detected when heart rate is near the individual resting level and HRV is high and regular. Firstbeat's glossary calls a recovery reaction a calming down of the body with parasympathetic predominance ([Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary)). Formula: Not published.
- Defaults: None stated.
- Inputs: RR data.
- Units: Min in the API. The API table shows the export name with hh:mm:ss. The export help article lists minutes.
- Variants: None.
- What changes the number: The resting heart rate in the profile, because recovery is judged against the individual resting level.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf), [Glossary](https://firstbeat.com/en/professional-sports/learning-center/glossary).

#### Garmin sleep and overnight data

This list gives the details for Garmin sleep and overnight data:

- Firstbeat name, API variable, and unit: `Sleep Duration`, `Sleep Score`, `Resting Heart Rate (bpm)`, `Average Last Night HRV`, `Peak 5-minute Last Night HRV`. Garmin daily data also includes `Active Calories` and `BMR`. These are Garmin's names. They are not in the API Variables list or the Data Export list. [Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API), [Garmin sleep news, 2026-02-05](https://www.firstbeat.com/en/news/firstbeat-sports-announces-integration-of-garmin-sleep-data-to-enhance-recovery-insights-for-athletes/)
- What it measures: Overnight values that a compatible Garmin watch records and Garmin Connect sends to Firstbeat Sports.
- Window or phase: Overnight values. After a link, Firstbeat syncs the past 90 days.
- Calculation: Garmin calculates them. Firstbeat displays them. Firstbeat does not describe how Garmin builds the sleep score or the HRV values. That is Not published in the sources read. Formula: Not published.
- Defaults: After a link is made, Firstbeat syncs Garmin Connect activity, sleep, and recovery data from the past 90 days ([Link Garmin Connect](https://support.firstbeatsports.com/hc/en-us/articles/360016073337-How-to-link-Garmin-Connect-to-the-Firstbeat-Sports-Cloud)).
- Inputs: A supported Garmin device and a Garmin Connect link made by the athlete.
- Units: Bpm for resting heart rate. The units for duration, the score, and the HRV values are Not published in the sources read.
- Variants: Which metrics appear depends on the Garmin model.
- What changes the number: The Garmin model and its settings. If an athlete records an activity with both a Garmin watch and a Firstbeat Sensor, Firstbeat prefers the Garmin recording. Edits or deletions in Garmin Connect do not sync. HRV in activities needs an HR strap and HRV logging turned on ([Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API)). Do not mix Garmin's overnight HRV with Firstbeat's `rmssd`. The methods differ, and Garmin's is not described.
- Sources: [Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API), [Garmin sleep news, 2026-02-05](https://www.firstbeat.com/en/news/firstbeat-sports-announces-integration-of-garmin-sleep-data-to-enhance-recovery-insights-for-athletes/), [Link Garmin Connect](https://support.firstbeatsports.com/hc/en-us/articles/360016073337-How-to-link-Garmin-Connect-to-the-Firstbeat-Sports-Cloud).

### Fitness estimates, oxygen, and breathing

#### VO2max

This list gives the details for VO2max:

- Firstbeat name, API variable, and unit: `VO2max (ml/kg/min)`. API: `vo2max` (ml/kg/min). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: An estimate of the athlete's maximal oxygen uptake, a measure of aerobic fitness.
- Window or phase: Not stated by the vendor.
- Calculation: The export says it is calculated from heart rate variability data ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Firstbeat's VO2max white paper describes a different method: it estimates VO2max from any freely performed workout using the relationship between heart rate and speed, and uses only the most reliable segments. It drops soft ground, steep downhill, stops with a high heart rate, and long-run heart rate drift ([VO2max white paper](https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf)). The sources do not say which method the Sports Cloud `vo2max` uses. The Garmin sync gives a VO2Max result only for the "Running" sports type ([Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API)). Formula: Not published.
- Defaults: The method is submaximal and uses an age-based estimate of HRmax ([VO2max white paper](https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf)).
- Inputs: Heart rate, speed or power, age, and HRmax.
- Units: Ml/kg/min.
- Variants: The profile also holds a VO2max value, which `%VO2max` uses ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Whether that value equals the exported `vo2max` is Not published.
- Comparison with standard methods or other vendors: In 2,690 runs by 79 runners, Firstbeat reports a mean absolute percentage error of about 5% against laboratory VO2max. A typical indirect submaximal test has an error of 10 to 15%. A direct laboratory test has about 5%. If HRmax is set 15 bpm too low, the error is about 9%. If it is 15 bpm too high, the error is about 7%. With a known HRmax the error falls to about 5% ([VO2max white paper](https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf)). These are Firstbeat's own results. A peer-reviewed study of 90 rowers and paddlers found a mean absolute percentage error of 5.0% or less for the Firstbeat fitness test ([Gao et al., 2021, doi:10.3389/fphys.2021.701541](https://doi.org/10.3389/fphys.2021.701541)). Another study of five wrist-worn trackers found a mean absolute percentage error above 10% for all but one VO2max estimate. The Garmin Forerunner 920XT gave 7.3% and underestimated VO2max ([Passler et al., 2019, doi:10.3390/ijerph16173037](https://doi.org/10.3390/ijerph16173037)). The abstract of that study does not name the algorithm inside each device.
- What changes the number: The HRmax setting (see above), the surface and speed data quality, and heat or drift in long runs.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [VO2max white paper](https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf), [Garmin Health API](https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API), [Gao et al., 2021, doi:10.3389/fphys.2021.701541](https://doi.org/10.3389/fphys.2021.701541), [Passler et al., 2019, doi:10.3390/ijerph16173037](https://doi.org/10.3390/ijerph16173037).

#### Oxygen consumption (VO2)

This list gives the details for Oxygen consumption (VO2):

- Firstbeat name, API variable, and unit: `Average VO2 (ml/kg/min)` and `Peak VO2 (ml/kg/min)`. API: `oxygenConsumptionAverage` and `oxygenConsumptionPeak` (ml/kg/min). The API text calls the peak "VO2max", but it is the highest estimated VO2 in the measurement. [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The estimated rate of oxygen use during the measurement.
- Window or phase: Average and peak over the measurement.
- Calculation: Neural networks estimate VO2 from RR intervals, using a respiration rate and on and off kinetics ([VO2 estimation white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_vo2_estimation.pdf)). The method estimates only aerobic energy production. Firstbeat says it is not suitable on its own to estimate VO2max. Formula: Not published.
- Defaults: None.
- Inputs: RR intervals, respiration rate, HRmax, and VO2max from the profile.
- Units: Ml/kg/min.
- Variants: Average and peak.
- Comparison with standard methods or other vendors: In 32 adults on a cycle ergometer and in real-life tasks, the mean absolute error against measured VO2 was 3.7 ml/kg/min from heart rate alone and 1.9 ml/kg/min with respiration rate and on and off kinetics added. These are second-by-second errors ([VO2 estimation white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_vo2_estimation.pdf)). Firstbeat lists published validation papers by Smolander et al. (doi:10.1111/j.1475-097x.2011.01011.x and doi:10.1016/j.apergo.2007.09.001) and Montgomery et al. (doi:10.1519/jsc.0b013e3181a39277). The abstracts were not available in the public records, so this page does not summarize them ([Firstbeat VO2 publication list](https://www.firstbeat.com/en/science-and-physiology/white-papers-and-publications/oxygen-consumption-and-maximal-oxygen-consumption-vo2max/)).
- What changes the number: HRmax and the profile VO2max, because the method works on a fraction of each. The white paper says accuracy depends on how accurate those background values are.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [VO2 estimation white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_vo2_estimation.pdf), [Firstbeat VO2 publication list](https://www.firstbeat.com/en/science-and-physiology/white-papers-and-publications/oxygen-consumption-and-maximal-oxygen-consumption-vo2max/).

#### Percent of VO2max

This list gives the details for Percent of VO2max:

- Firstbeat name, API variable, and unit: `Average %VO2max (%)`, `Peak %VO2max (%)`. API: `oxygenConsumptionAveragePercentage`, `oxygenConsumptionMaximumPercentage` (%). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: Estimated oxygen use as a share of the athlete's VO2max.
- Window or phase: Average and peak over the measurement.
- Calculation: Firstbeat calculates it from the VO2max value set in the profile ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). EPOC is predicted from this intensity ([EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf)). Formula: Restatement: %VO2max = VO2 / profile VO2max x 100.
- Defaults: The profile VO2max, estimated from background data if not measured ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf)).
- Inputs: Estimated VO2 and profile VO2max.
- Units: Percent.
- Variants: Average and peak.
- What changes the number: The profile VO2max, directly. Whether the value can pass 100% is Not published. Firstbeat says work in sprints can reach 150% of VO2max, but it measures that through Anaerobic Training Effect, not through this variable.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [EPOC white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf), [Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf).

#### Respiration rate

This list gives the details for Respiration rate:

- Firstbeat name, API variable, and unit: `Average RespR (times/min)`, `Peak RespR (times/min)`. API: `respirationRateAverage`, `respirationRatePeak` (1/min). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: Breaths per minute, estimated from heartbeat data.
- Window or phase: Average and peak over the measurement.
- Calculation: Firstbeat calculates it from heart rate variability, because breathing changes the time between beats ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). It cites a separate method paper on deriving respiration from heart period data. That paper was not read. Formula: Not published.
- Defaults: None.
- Inputs: Artifact-corrected RR intervals.
- Units: Times per minute.
- Variants: Average and peak.
- What changes the number: Artifacts. A missed beat disturbs the pattern the method reads.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export).

#### Ventilation

This list gives the details for Ventilation:

- Firstbeat name, API variable, and unit: `Average VE (liter/min)` and `Peak VE (liter/min)` in the API table, `Average Ventilation (l/min)` in the export. API: `ventilationAverage`, `ventilationPeak` (liter/min). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The estimated air volume breathed per minute.
- Window or phase: Average and peak over the measurement.
- Calculation: Firstbeat calculates it from heart rate variability data ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)). Formula: Not published.
- Defaults: None.
- Inputs: RR intervals.
- Units: Liters per minute.
- Variants: Average and peak.
- What changes the number: The same factors as respiration rate. Firstbeat removed ventilation from the newer Data Export because some variables might not meet its quality criteria. The API still lists it. Treat it as low confidence ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export).

### Energy expenditure

#### Energy expenditure, total

This list gives the details for Energy expenditure, total:

- Firstbeat name, API variable, and unit: `Energy Expenditure Total (kcal)`. API: `energyConsumptionTotal` (kcal) and `energyConsumptionSeries` (kcal/h, 0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The estimated energy the athlete used during the measurement.
- Window or phase: The whole measurement, plus a series in kcal/h at 0.2 Hz.
- Calculation: Firstbeat first estimates VO2. It then derives energy expenditure from VO2, the respiratory quotient (RQ), and the caloric equivalent. RQ runs from 0.70 to 1.00, and the caloric equivalent from 4.69 to 5.05 kcal per liter of oxygen. Harder exercise raises RQ, and long exercise lowers it. The total is the sum of the momentary values ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf)). Formula: Restatement: momentary EE is about VO2 x caloric equivalent (RQ). The exact model is a neural network and is Not published.
- Defaults: Age, height, weight, sex, and activity level are the stated inputs. Firstbeat estimates HRmax and VO2max when they are not measured ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf)).
- Inputs: RR intervals and profile values.
- Units: Kcal, and kcal/h for the series.
- Variants: The series, and the Garmin daily values `Active Calories` and `BMR`, which Firstbeat receives from Garmin.
- Comparison with standard methods or other vendors: In 32 adults, the mean absolute error was 73 kcal (10.9%) for Firstbeat's method. The paper's four other methods had mean absolute errors of 93 kcal (13.5%), 101 kcal (14.4%), 181 kcal (22.0%), and 180 kcal (27.6%) ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf)). The model estimates only aerobic energy, so it may underestimate very short anaerobic efforts. This is not a concern after 2 to 3 minutes. A published test in 25 people found a mean absolute percentage error of 1.70% for a chest strap and 6.73% for a vest ([Parak et al., 2021, doi:10.3390/s21248411](https://doi.org/10.3390/s21248411)).
- What changes the number: The body weight in the profile and the other background values. Whether the total includes resting use is Not published.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf), [Parak et al., 2021, doi:10.3390/s21248411](https://doi.org/10.3390/s21248411).

#### Energy expenditure, carbohydrates and fats

This list gives the details for Energy expenditure, carbohydrates and fats:

- Firstbeat name, API variable, and unit: `EE Carbohydrates (kcal)`, `EE Fats (kcal)`. API: `energyConsumptionCarbs`, `energyConsumptionFats` (kcal), and `energyConsumptionRelativeFatSeries` (%, 0.2 Hz). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: How the estimated energy use splits between carbohydrate and fat.
- Window or phase: The whole measurement, plus a relative fat series at 0.2 Hz.
- Calculation: The split follows from the RQ in the energy model above ([Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf)). The API describes the series as the share of total expenditure that comes from fats. Formula: Not published.
- Defaults: None.
- Inputs: The same as total energy expenditure.
- Units: Kcal, and percent for the series.
- Variants: Carbohydrate, fat, and the relative fat series.
- What changes the number: Intensity, duration, and the same inputs as total energy. Firstbeat dropped carbohydrate and fat energy from the newer Data Export for quality reasons. The API still lists them, and the 2021 brochure shows a split in its example report ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf)). Treat the split as low confidence.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Energy expenditure white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf).

### Data quality and raw signals

#### Measurement error

This list gives the details for Measurement error:

- Firstbeat name, API variable, and unit: `Measurement Error (%)` in the export and `Missing or poor quality data (%)` in the API table. API: `measurementError` (%). [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)
- What it measures: The share of beats that Firstbeat could not trust, after it corrected the data.
- Window or phase: The whole measurement. For a merged measurement, gaps between the parts count.
- Calculation: The average percentage of RR intervals recognized as artifacts after the artifact correction. For a merged measurement, gaps between the parts count toward it ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Restatement: error % = flagged intervals / all intervals x 100. Firstbeat does not print a formula.
- Defaults: Firstbeat shows the percentage in the Coach app. A high average error can make the server reject the data. The limit is Not published ([Error percentages help](https://support.firstbeatsports.com/hc/en-us/articles/360017022358-Coach-app-troubleshooting-What-can-cause-higher-error-percentages-in-Firstbeat-Sports-Sensor-data)).
- Inputs: RR intervals and the artifact filter's flags.
- Units: Percent.
- Variants: A 5-second series (see Artifact percentage series).
- What changes the number: Dry skin or a dry strap, a loose or worn strap, the Sensor left on the strap after the session, a Sensor worn upside down, shirts that create static electricity, and arm-heavy sports such as CrossFit, tennis, and handball ([Error percentages help](https://support.firstbeatsports.com/hc/en-us/articles/360017022358-Coach-app-troubleshooting-What-can-cause-higher-error-percentages-in-Firstbeat-Sports-Sensor-data)). Check this column before you trust any other metric in the row.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Error percentages help](https://support.firstbeatsports.com/hc/en-us/articles/360017022358-Coach-app-troubleshooting-What-can-cause-higher-error-percentages-in-Firstbeat-Sports-Sensor-data).

#### Artifact percentage series

This list gives the details for Artifact percentage series:

- Firstbeat name, API variable, and unit: Not named in the export list. API: `artifactPercentageSeries` (%, 0.2 Hz, 8-bit). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The share of beats rejected in each 5-second period.
- Window or phase: 5-second periods.
- Calculation: Firstbeat describes it as the percentage of rejected RR intervals within each 5-second period ([API variables](https://apidocs.firstbeat.com/variables/)). Formula: Restatement: rejected intervals / all intervals in the period x 100.
- Defaults: A 5-second period.
- Inputs: RR intervals.
- Units: Percent.
- Variants: The custom report also offers artifact percentage for the Training Chart ([Custom session reports](https://support.firstbeatsports.com/hc/en-us/articles/40603643127057-How-to-create-Custom-Session-Reports)).
- What changes the number: The same sensor factors as measurement error. Use it to find where in a session the signal failed.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Custom session reports](https://support.firstbeatsports.com/hc/en-us/articles/40603643127057-How-to-create-Custom-Session-Reports).

#### Raw RR intervals

This list gives the details for Raw RR intervals:

- Firstbeat name, API variable, and unit: `RR`. API: `rriSeries` (ms, unsigned 16-bit), not available for laps and sessions. It needs a Premium+ time series export. [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)
- What it measures: The time between heartbeats, as recorded and before any correction.
- Window or phase: Beat by beat. The vector has no regular sampling rate. Not available for laps and sessions.
- Calculation: The Sensor records the beat-to-beat intervals. Its stated recording accuracy is under 2 ms ([Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications)). Formula: None. It is a recorded signal.
- Defaults: None.
- Inputs: The heart rate strap and Sensor.
- Units: Ms. The vector has no regular sampling rate.
- Variants: The corrected series below.
- What changes the number: Sensor contact, strap condition, and motion. Use the raw series to run your own HRV.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications).

#### Artifact-corrected RR intervals

This list gives the details for Artifact-corrected RR intervals:

- Firstbeat name, API variable, and unit: `Artifact Corrected RR`. API: `artifactCorrectedRrVector` (ms, 64-bit float). [API variables](https://apidocs.firstbeat.com/variables/)
- What it measures: The heartbeat intervals after Firstbeat fixed missed, extra, and early beats.
- Window or phase: Beat by beat. The vector has no regular sampling rate.
- Calculation: Firstbeat scans RR data through an artifact detection filter that corrects falsely detected, missed, and premature beats ([Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf)). The method itself, by Saalasti and colleagues in 2004, is Not published in the sources read. Formula: Not published.
- Defaults: None.
- Inputs: The raw RR series.
- Units: Ms. The vector has no regular sampling rate. Sample API output holds non-whole values such as 1015.0000000000001, so corrected values can be fractions ([Querying the API](https://apidocs.firstbeat.com/querying-the-api/)).
- Variants: Raw and corrected. Firstbeat's own Bodyguard 2 test found that correction cut extra detections from 0.16% to 0.04% of beats ([Parak and Korhonen, Bodyguard 2 accuracy](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf)).
- What changes the number: How many artifacts the raw series had. A series with many corrections is less reliable. Report `measurementError` with any HRV result.
- Sources: [API variables](https://apidocs.firstbeat.com/variables/), [Stress and recovery white paper](https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf), [Querying the API](https://apidocs.firstbeat.com/querying-the-api/), [Parak and Korhonen, Bodyguard 2 accuracy](https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf).

## Context fields that are not metrics

These fields describe a measurement or session. They are not counted as metrics:

- `measurementType`: `exercise`, `quickRecoveryTest`, `night`, or `manual` ([Querying the API](https://apidocs.firstbeat.com/querying-the-api/)).
- `exerciseType` and `sessionType`: the title.
- `sportsType`: a fixed list of sports, such as `football` and `iceHockey`.
- `eventType`: `race`, `game`, `rehab`, `recovery`, or `training` ([Querying the API](https://apidocs.firstbeat.com/querying-the-api/)).
- `notes`, `startTime`, `endTime`, `startTimeLocal`, `endTimeLocal`, and lap fields.

Sport and event tags depend on what coaches enter ([Querying the API](https://apidocs.firstbeat.com/querying-the-api/)).

## Conflicts in the vendor's own sources

The Firstbeat sources disagree in these places:

- Subscription tier of Training Status: the 2021 brochure lists Training Status under Premium. The API page lists it as Premium+ ([Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf), [API variables](https://apidocs.firstbeat.com/variables/)).
- Subscription tier of Movement Load and Movement Intensity: the Sensor page and the brochure say Premium. The API page marks the series and Movement Intensity variables as Premium+ ([Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications), [Data brochure](https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf), [API variables](https://apidocs.firstbeat.com/variables/)).
- `vo2max` method: the Data Export help says the value is calculated from heart rate variability. The VO2max white paper describes a method that uses the relationship between heart rate and speed. The sources do not say which method Sports Cloud uses ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [VO2max white paper](https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf)).
- `rmssd1MinSeries` sampling: the series name says 1 minute, and the API table shows 0.02 Hz with the text "5min sample rate". The export says 1 minute ([API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- `lfHfRatio`: the API text names HF first and LF second. The export name is `LF/HF (%)`, and the API lists the unit as "%". The order is Not confirmed ([API variables](https://apidocs.firstbeat.com/variables/)).
- Percent of HRmax series and export names: the API Variables page lists the `heartRatePercentageSeries` unit as 1/min, which looks like an error for a percent series. Two API table entries map `heartRatePeakPercentage` and `heartRateMinimumPercentage` to export names that read "Peak HR (bpm)" and "Minimum HR (bpm)" ([API variables](https://apidocs.firstbeat.com/variables/)).
- Overnight Recovery: the Data Export lists `Overnight Recovery (%)`, but the API Variables page has no variable with this name. The closest listed variable is `sleepRecoveryIndexAbsolute` ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [API variables](https://apidocs.firstbeat.com/variables/)).
- Relaxation time unit: the API table shows the export name with hh:mm:ss. The export help article lists minutes ([API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- Other export names: the API Variables page and the Data Export help article give different export names for some variables, such as `Minimum Heart rate` against `Minimum Heart Rate (bpm)`, and `EE Total (kcal)` against `Energy Expenditure Total (kcal)`. This page uses the help article names ([API variables](https://apidocs.firstbeat.com/variables/), [Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export)).
- Variables removed from the newer Data Export: Firstbeat dropped ventilation, carbohydrate and fat energy, HF, LF, the HF/LF ratio, and SDNN because some variables might not meet its quality criteria. The API Variables page still lists them ([Data Export help](https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export), [API variables](https://apidocs.firstbeat.com/variables/)).
- Movement Intensity unit: the API lists `index`, the Sensor page names the unit as ML/min, and the maximal-period variables use the label kicks/min ([API variables](https://apidocs.firstbeat.com/variables/), [Sensor specifications](https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications)).
- Movement Efficiency: the API changelog added `movementEfficiency` on 2025-10-22, but the API Variables page does not list it ([API changelog](https://apidocs.firstbeat.com/changelog/), [API variables](https://apidocs.firstbeat.com/variables/)).
- Manual measurement fields: the API FAQ says a manual measurement has only start time, end time, TRIMP, and duration. The manual exercise help article lists more, including TRIMP per minute, acute load, chronic load, ACWR, Training Status, notes, and sports type ([API FAQ](https://apidocs.firstbeat.com/faq/), [Manual exercise input](https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud)).
- Oxygen consumption peak: the API text calls the peak "VO2max", but it is the highest estimated VO2 in the measurement ([API variables](https://apidocs.firstbeat.com/variables/)).
- Plews et al. (2013) volume: Firstbeat's own reference list gives volume 6. The Crossref record shows volume 8, issue 6 (<https://doi.org/10.1123/ijspp.8.6.688>). Use the Crossref values.

## Not published

The sources do not publish or confirm these details. Confirm them with the user or in Sports Cloud:

- The default HRmax age formula, the default resting HR, and the default heart rate zone limits.
- Whether Firstbeat Sports updates the activity class on its own.
- The TRIMP lower intensity limit and whether the formula changes for women.
- The Training Effect mapping from peak EPOC and activity class, in numbers.
- The Training Status weights and the ACWR gauge limits.
- The header row of the Excel export. The help article lists variable names, and the real header may differ.
- Which subscription tier includes Training Status, Movement Load, and Movement Intensity.
- Whether the exported `rmssd` on exercise measurements is meaningful.
- Whether the Sports Cloud `vo2max` uses the HR and speed method or an HRV method.
- Whether Garmin overnight metrics appear in the API or the export.
- Export names. The API Variables page and the Data Export help article give different export names for some variables, such as `Minimum Heart rate` against `Minimum Heart Rate (bpm)`, and `EE Total (kcal)` against `Energy Expenditure Total (kcal)`. This page uses the help article names.
- Whether Training Status is missing for days with no measurement. Known issues name only acute load, chronic load, and ACWR.

## Worked example in Python

This example runs RMSSD on a 30-beat synthetic RR series, then adds one missed-beat artifact and shows RMSSD with and without a correction. The correction is a simple median rule written for this example. It is not Firstbeat's artifact correction, which is Not published in the sources read. The series is made up, so the numbers show the effect of one bad beat and are not norms for athletes.

The program and its output follow. The output came from Python 3.9 on 2026-10-02.

```python
"""Worked example: RMSSD from a short synthetic RR series, and the effect of
one artifact beat with and without correction.

The series is synthetic. The correction is a simple median rule written for
this example. It is NOT the Firstbeat artifact correction algorithm, which is
not published in the sources used for this file.
"""
import math
import statistics


def rmssd(rr):
    """Root mean square of successive differences, in ms."""
    diffs = [b - a for a, b in zip(rr, rr[1:])]
    return math.sqrt(sum(d * d for d in diffs) / len(diffs))


def mean_hr(rr):
    """Mean heart rate in beats per minute from RR intervals in ms."""
    return 60000.0 / statistics.mean(rr)


def correct_simple(rr, window=2, tol=0.20):
    """Illustrative corrector.

    For each interval, compare with the median of up to `window` neighbors on
    each side. If it is more than `tol` away from that median:
      - if it is close to twice the median, split it into two equal intervals
        (a missed beat), otherwise
      - replace it with the median (a falsely detected or premature beat).
    Returns (corrected_series, number_of_intervals_changed).
    """
    out = []
    changed = 0
    for i, v in enumerate(rr):
        lo, hi = max(0, i - window), min(len(rr), i + window + 1)
        neigh = [rr[j] for j in range(lo, hi) if j != i]
        med = statistics.median(neigh)
        if abs(v - med) / med > tol:
            changed += 1
            if abs(v - 2 * med) / (2 * med) <= tol:
                out.extend([v / 2.0, v / 2.0])
            else:
                out.append(med)
        else:
            out.append(v)
    return out, changed


# 1. Synthetic clean series: 30 beats, about 62 bpm, with a slow
#    breathing-like swing of about +/- 40 ms (values rounded to whole ms).
clean = [round(970 + 40 * math.sin(2 * math.pi * i / 6.5)) for i in range(30)]

# 2. Insert one artifact: a missed beat. Beats 14 and 15 merge into one
#    interval equal to their sum, so the series has 29 intervals.
artifact_index = 14
with_artifact = (
    clean[:artifact_index]
    + [clean[artifact_index] + clean[artifact_index + 1]]
    + clean[artifact_index + 2:]
)

# 3. Apply the illustrative correction to the series with the artifact.
corrected, n_changed = correct_simple(with_artifact)

print("Clean RR series (ms):", clean)
print("Series with one missed-beat artifact (ms):", with_artifact)
print("Corrected series (ms):", [round(x, 1) for x in corrected])
print()
print(f"{'Series':<26}{'Intervals':>10}{'Mean HR (bpm)':>16}{'RMSSD (ms)':>12}")
for label, s in [("Clean", clean),
                 ("Artifact, not corrected", with_artifact),
                 ("Artifact, corrected", corrected)]:
    print(f"{label:<26}{len(s):>10}{mean_hr(s):>16.1f}{rmssd(s):>12.1f}")
print()
print("Intervals changed by the correction:", n_changed)
print("Share of intervals flagged:", f"{100 * n_changed / len(with_artifact):.1f} %")
r_clean, r_raw, r_cor = rmssd(clean), rmssd(with_artifact), rmssd(corrected)
print(f"RMSSD change from the artifact, uncorrected: {r_raw - r_clean:+.1f} ms ({100 * (r_raw / r_clean - 1):+.0f} %)")
print(f"RMSSD change from the artifact, corrected:   {r_cor - r_clean:+.1f} ms ({100 * (r_cor / r_clean - 1):+.0f} %)")
print(f"RMSSD ratio, uncorrected / clean: {r_raw / r_clean:.1f}x")
print(f"ln(RMSSD) clean / uncorrected / corrected: {math.log(r_clean):.2f} / {math.log(r_raw):.2f} / {math.log(r_cor):.2f}")
```

Output:

```text
Clean RR series (ms): [970, 1003, 1007, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 1003, 1007, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 1003, 1007, 980]
Series with one missed-beat artifact (ms): [970, 1003, 1007, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 2010, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 1003, 1007, 980]
Corrected series (ms): [970, 1003, 1007, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 1005.0, 1005.0, 980, 943, 930, 951, 989, 1010, 997, 960, 933, 937, 970, 1003, 1007, 980]

Series                     Intervals   Mean HR (bpm)  RMSSD (ms)
Clean                             30            61.7        26.2
Artifact, not corrected           29            59.6       277.8
Artifact, corrected               30            61.7        26.3

Intervals changed by the correction: 1
Share of intervals flagged: 3.4 %
RMSSD change from the artifact, uncorrected: +251.5 ms (+958 %)
RMSSD change from the artifact, corrected:   +0.0 ms (+0 %)
RMSSD ratio, uncorrected / clean: 10.6x
ln(RMSSD) clean / uncorrected / corrected: 3.27 / 5.63 / 3.27
```

What the output shows: one missed beat in 30 raised RMSSD from 26.2 ms to 277.8 ms, which is 10.6 times the clean value. The simple correction returned it to 26.3 ms. Real data are harder, because real artifacts vary in size and sit next to real variation. Check `measurementError` before you trust any RMSSD.

## Sources

Firstbeat pages and papers support the facts on this page. All were accessed on 2026-10-02:

- API variables: <https://apidocs.firstbeat.com/variables/>, accessed 2026-10-02.
- Sports Guide, Training Load: <https://content.firstbeat.com/hubfs/Sports/Sports%20Guides/Sports%20Guides%20%28English%29/ENG-Sports-Guide-Training%20Load.pdf>, accessed 2026-10-02.
- EPOC white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_epoc.pdf>, accessed 2026-10-02.
- Data Export help: <https://support.firstbeatsports.com/hc/en-us/articles/360016170258-Feature-Firstbeat-Sports-Data-Export>, accessed 2026-10-02.
- Learning Center, Interpreting training data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-training-data/>, accessed 2026-10-02.
- Training Effect white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_training_effect.pdf>, accessed 2026-10-02.
- TRIMP formula figure: <https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-Formula-800x198.jpg>, accessed 2026-10-02.
- TRIMP/min scale figure: <https://exvea4j23ce.exactdn.com/wp-content/uploads/2020/02/Sports-Learning-Center-TRIMP-min-Scale-800x437.jpg>, accessed 2026-10-02.
- Anaerobic Training Effect white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/FFW609US05-171.pdf>, accessed 2026-10-02.
- Manual exercise input: <https://support.firstbeatsports.com/hc/en-us/articles/360017693797-Feature-How-to-use-Manual-Exercise-Input-in-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- Training Status help: <https://support.firstbeatsports.com/hc/en-us/articles/360016170038-Feature-Firstbeat-Sports-Training-Status>, accessed 2026-10-02.
- Known issues: <https://apidocs.firstbeat.com/known-issues/>, accessed 2026-10-02.
- Glossary: <https://firstbeat.com/en/professional-sports/learning-center/glossary>, accessed 2026-10-02.
- Training Summary report help: <https://support.firstbeatsports.com/hc/en-us/articles/40604830199313-What-is-included-in-the-Training-Summary-Report>, accessed 2026-10-02.
- API changelog: <https://apidocs.firstbeat.com/changelog/>, accessed 2026-10-02.
- Terminology: <https://apidocs.firstbeat.com/terminology/>, accessed 2026-10-02.
- Data brochure: <https://www.firstbeat.com/wp-content/uploads/2023/02/ENG-Firstbeat-Sports-Data-Brochure-04-2021-1.pdf>, accessed 2026-10-02.
- Basic concepts: <https://apidocs.firstbeat.com/basic-concepts/>, accessed 2026-10-02.
- API FAQ: <https://apidocs.firstbeat.com/faq/>, accessed 2026-10-02.
- Learning Center, Interpreting movement data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-movement-data/>, accessed 2026-10-02.
- Sensor specifications: <https://support.firstbeatsports.com/hc/en-us/articles/360017634158-Firstbeat-Sports-Sensor-technical-specifications>, accessed 2026-10-02.
- Trim and merge: <https://support.firstbeatsports.com/hc/en-us/articles/42677296920721-How-to-trim-and-merge-measurements-in-Sports-Cloud>, accessed 2026-10-02.
- What's new in Sports products: <https://www.firstbeat.com/en/whats-new-sports-products/>, accessed 2026-10-02.
- Custom session reports: <https://support.firstbeatsports.com/hc/en-us/articles/40603643127057-How-to-create-Custom-Session-Reports>, accessed 2026-10-02.
- Garmin Health API: <https://support.firstbeatsports.com/hc/en-us/articles/360016073377-Feature-Garmin-Health-API>, accessed 2026-10-02.
- Heart Rate Recovery help: <https://support.firstbeatsports.com/hc/en-us/articles/10774273894673-Feature-Heart-Rate-Recovery>, accessed 2026-10-02.
- Learning Center, Introduction: <https://www.firstbeat.com/en/professional-sports/learning-center/introduction-to-firstbeat-sports/>, accessed 2026-10-02.
- Submaximal Fitness Test report: <https://support.firstbeatsports.com/hc/en-us/articles/40637753745937-What-is-included-in-the-Submaximal-Fitness-Test-Report>, accessed 2026-10-02.
- QRT help: <https://support.firstbeatsports.com/hc/en-us/articles/360018737917-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Coach-app>, accessed 2026-10-02.
- Learning Center, Interpreting recovery data: <https://www.firstbeat.com/en/professional-sports/learning-center/interpreting-recovery-data/>, accessed 2026-10-02.
- Stress and recovery white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/Stress-and-recovery_white-paper_20145.pdf>, accessed 2026-10-02.
- Parak and Korhonen, Bodyguard 2 accuracy: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_bodyguard2_final.pdf>, accessed 2026-10-02.
- Edit or delete measurements: <https://support.firstbeatsports.com/hc/en-us/articles/360016072097-How-to-edit-or-delete-individual-measurements-in-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- QRT help, Athlete app: <https://support.firstbeatsports.com/hc/en-us/articles/7894987881233-How-to-perform-the-Quick-Recovery-Test-with-the-Firstbeat-Sports-Athlete-app>, accessed 2026-10-02.
- Bodyguard 3 help: <https://support.firstbeatsports.com/hc/en-us/articles/4419781074705-Stress-and-recovery-measurements-using-the-Firstbeat-Bodyguard-3-device>, accessed 2026-10-02.
- Recovery white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/Recovery-white-paper_15.6.20153.pdf>, accessed 2026-10-02.
- Sleep white paper: <https://www.firstbeat.com/wp-content/uploads/2019/11/A-Sleep-Analysis-Method-Based-on-Heart-Rate-Variability-071119.pdf>, accessed 2026-10-02.
- Garmin sleep news, 2026-02-05: <https://www.firstbeat.com/en/news/firstbeat-sports-announces-integration-of-garmin-sleep-data-to-enhance-recovery-insights-for-athletes/>, accessed 2026-10-02.
- Link Garmin Connect: <https://support.firstbeatsports.com/hc/en-us/articles/360016073337-How-to-link-Garmin-Connect-to-the-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- VO2max white paper: <https://www.firstbeat.com/wp-content/uploads/2017/06/white_paper_VO2max_30.6.2017.pdf>, accessed 2026-10-02.
- VO2 estimation white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_vo2_estimation.pdf>, accessed 2026-10-02.
- Firstbeat VO2 publication list: <https://www.firstbeat.com/en/science-and-physiology/white-papers-and-publications/oxygen-consumption-and-maximal-oxygen-consumption-vo2max/>, accessed 2026-10-02.
- Energy expenditure white paper: <https://www.firstbeat.com/wp-content/uploads/2015/10/white_paper_energy_expenditure_estimation.pdf>, accessed 2026-10-02.
- Error percentages help: <https://support.firstbeatsports.com/hc/en-us/articles/360017022358-Coach-app-troubleshooting-What-can-cause-higher-error-percentages-in-Firstbeat-Sports-Sensor-data>, accessed 2026-10-02.
- Querying the API: <https://apidocs.firstbeat.com/querying-the-api/>, accessed 2026-10-02.
- Session Report help: <https://support.firstbeatsports.com/hc/en-us/articles/40602510889489-What-is-included-in-the-Session-Report>, accessed 2026-10-02.
- Start using Sports Cloud: <https://support.firstbeatsports.com/hc/en-us/articles/360015938677-How-to-start-using-Firstbeat-Sports-Cloud>, accessed 2026-10-02.
- Learning Center home: <https://www.firstbeat.com/en/professional-sports/learning-center/>, accessed 2026-10-02.

Peer-reviewed and conference papers cited on this page, with their DOI links:

- Parak et al., 2021, Sensors 21(24):8411: <https://doi.org/10.3390/s21248411>, accessed 2026-10-02. Abstract. Chest strap against vest, with a Holter reference.
- Conte et al., 2025, Int J Sports Physiol Perform 20(5):727-730: <https://doi.org/10.1123/ijspp.2024-0289>, accessed 2026-10-02. Abstract. Interunit reliability of Movement Load.
- Kuula and Pesonen, 2021, JMIR mHealth uHealth 9(2):e24704: <https://doi.org/10.2196/24704>, accessed 2026-10-02. Abstract. Sleep stages against polysomnography.
- Gao et al., 2021, Front Physiol 12:701541: <https://doi.org/10.3389/fphys.2021.701541>, accessed 2026-10-02. Abstract. Firstbeat fitness test in rowers and paddlers.
- Passler et al., 2019, Int J Environ Res Public Health 16(17):3037: <https://doi.org/10.3390/ijerph16173037>, accessed 2026-10-02. Abstract. Wrist-worn trackers.
- Smolander et al., 2008 (online 2007), Appl Ergon 39(3):325-331: <https://doi.org/10.1016/j.apergo.2007.09.001>, accessed 2026-10-02. No abstract is available in the public record, so this page does not summarize it.
- Smolander et al., 2011, Clin Physiol Funct Imaging 31(4):266-271: <https://doi.org/10.1111/j.1475-097x.2011.01011.x>, accessed 2026-10-02. No abstract is available in the public record, so this page does not summarize it.
- Montgomery et al., 2009, J Strength Cond Res 23(5):1489-1495: <https://doi.org/10.1519/jsc.0b013e3181a39277>, accessed 2026-10-02. No abstract is available in the public record, so this page does not summarize it.
- Ulmer et al., 2019, Biol Sport 36(2):191-194: <https://doi.org/10.5114/biolsport.2019.84670>, accessed 2026-10-02. No abstract is available in the public record, so this page does not summarize it. Firstbeat lists it as a TRIMP reliability study.
- Plews et al., 2013, Int J Sports Physiol Perform 8(6): <https://doi.org/10.1123/ijspp.8.6.688>, accessed 2026-10-02. Listed in Firstbeat's reference list. See the conflicts section for the volume number.

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
