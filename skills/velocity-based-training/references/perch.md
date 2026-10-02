# Perch data

Checked against: the Perch help center articles on perch.catapultsports.com, read on 2026-10-02.

This file describes the Perch export format and output, what each metric means, and how to transform the data for analysis. Perch was made by Catalyft Labs, Inc. and has been owned by Catapult since Catapult announced the acquisition on 2025-06-05. Perch and Catapult are trademarks of their owners. This repository is not affiliated with or endorsed by Perch, Catalyft Labs, Inc., or Catapult.

Perch is a rack-mounted camera system. A 3D depth camera gives each pixel a depth value. Perch algorithms find the bar or a body part and convert it to a 3D position. The 3D path is a time-stamped sequence of those positions, and every other metric comes from it. The camera frame rate is not published.

Perch uses this coordinate system:

- Z is up and down, parallel to gravity.
- X is forwards and backwards from the athlete's view.
- Y is side to side.

Perch tracks the bar for lifts. It tracks the athlete's head for jumps, not the bar. A tethered device such as GymAware measures tether length and angle instead. See `gymaware.md` for that device.

## Get the data

Use one of these routes:

- Insights reports: Perch Insights reports export to CSV.
- Train Sets: this is the general data export. It works at set level or rep level. Rep level shows within-set change and left-right asymmetry for lower-body unilateral exercises. The `Sets` and `Reps` levels give different results for the same columns, so record the level you choose.
- Aggregate exports: Perch publishes tonnage, volume, and set counts per user and per exercise in its reports. The Train Sets report exports "sets, reps, volume". The help center pages on exporting aggregated data (`support.perch.fit/exporting-aggregated-data-tonnage-volume-and-sets`) and CSV export (`support.perch.fit/csv-export`) could not be read, so the export steps and column list are not confirmed.
- API: Perch has an article on generating an API token. The token is available on some service tiers. Which tiers is not published. The API schema is not published.
- Integrations: Perch lists integrations with Teamworks (formerly Smartabase), Kinduct, Apollo, RockDaisy, Teambuildr, and Kitman Labs.
- Date and time format: not published in the pages read.

The organization's default weight unit drives exports. Coaches can edit sets after the session, including weight, athlete, exercise, and ghost reps. Export again after edits.

## API output

Perch does not publish an API schema, endpoint list, or response format. Do not guess field names. Ask the user for a sample response, or use the CSV export.

## Export columns

Perch does not publish the column names or the row level of its CSV exports. Ask the user for the header row and the report it came from. Map each column to the metric names in the table below.

Perch does publish the exercise variable names. A coach can set up to 4 variables per exercise. For tracked exercises, `Reps` and `Weight` are fixed. Whether these appear as columns is not published.

| Exercise variable | Meaning | Units |
|---|---|---|
| `Reps` | Reps in the set | Count |
| `Weight` | Load | kg, lb, or %1RM |
| `Time` | Time | Not published |
| `Distance` | Distance | Not published |
| `Height` | Height | Not published |
| `RIR` | Reps in reserve | Not published |
| `RPE` | Rating of perceived exertion | Not published |
| `Calories` | Calories | Not published |
| `Heart Rate` | Heart rate | bpm |
| `Watts` | Untracked power | Not published |

## Metric meanings

Perch measures a 3D path from a camera. Strength movements default to mean metrics in the athlete view. Ballistic and Olympic movements default to peak metrics. Reports show rep level and set level, where set level is the set average, the best rep, or the set minimum. How Perch picks the best rep is not published. Concentric and eccentric mean velocity are stored separately.

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `Mean Velocity` | Average bar speed over the lift | Displacement on the Z axis from the bottom of the rep to the top, divided by the time between those two points. For Olympic lifts, only the propulsive phase is used. | m/s | [mean-concentric-velocity](mean-concentric-velocity.md) | The formula has the same form as the reference, displacement divided by duration. The path comes from a camera, not a tether. Perch uses the Z axis only. For Olympic lifts it is not the full concentric phase. Rep start and end detection changes the value. |
| `Mean Propulsive Velocity` (MPV) | Average bar speed while the athlete accelerates the bar | `MPV = (P1 - P0) / (t1 - t0)` over the propulsive phase | m/s | [mean-concentric-velocity](mean-concentric-velocity.md) | The reference ends the propulsive phase when acceleration first drops below -9.81 m/s². Perch does not publish how it finds the end of the phase. Do not assume the two match. GymAware does not provide MPV. |
| `Peak Velocity` | Fastest bar speed in the movement | The largest velocity between any two consecutive coordinates, from the lowest to the highest point | m/s | [mean-concentric-velocity](mean-concentric-velocity.md) | A single-frame difference. The frame rate and any smoothing are not published, and a single-frame difference is sensitive to noise. GymAware uses a window of about 20 ms. |
| Eccentric Time | How long the lowering phase took | Time between the top of the rep and the lowest point | s | None | Not shown on the tablet for Olympic lifts or jumps. Top and bottom detection changes the value. |
| `Mean Power` | Average power put into the bar | `Mean Power = m × 9.8 × V`, where `m` is bar mass in kg and `V` is mean velocity in m/s. Perch reasons that the bar is at rest before and after the lift, so average force equals the bar's weight. | W by the formula. The unit label is not published. | None | The formula uses bar mass and gravity only. Our reading is that body mass is not counted, for example in squats. Perch writes the unit of 9.8 as m/s. It is m/s². GymAware mean power uses m × (a + 9.81) × v, so the two differ. |
| `Peak Power` | Highest instant power in the lift | For every sample, compute velocity `V` and acceleration `a` from consecutive positions. `Peak Power = m × a × V`. Take the largest value. | W by the formula | None | This formula has no gravity term, and `Mean Power` has gravity only. The two use different force terms. Double differentiation of position amplifies camera noise. Any filter is not published. |
| `T2PP` (Time to Peak Power) | How quickly the athlete reaches peak power | Time from the start of the concentric phase to the sample with peak power | s | None | Depends on concentric start detection and on peak power noise. |
| `T2PV` (Time to Peak Velocity) | How quickly the bar reaches top speed | Time from the start of the concentric phase to peak velocity | s | None | Depends on concentric start detection. |
| `V100` (Velocity at 100ms) | Bar speed early in the lift | Bar velocity within the first 100 ms of the concentric phase | m/s | None | Perch does not say whether this is the speed at 100 ms or the mean over 0 to 100 ms. |
| Displacement | How far the bar moved between two points, such as squat depth | End position minus start position. The Z axis alone gives vertical displacement. | Not stated. Our reading is metres. | None | Depends on the chosen start and end points. |
| `Work` and `Total Work` | Energy the athlete put into the bar | `W = F × d`, where `F` is the average force on the bar and `d` is displacement | kJ | None | With Perch's mean-force assumption, `W` is about m × 9.8 × Δz ÷ 1000 kJ per rep. How reps and sets are summed into `Total Work` is not published. |
| Estimated 1RM (e1RM) and MVT | Predicted one-rep max from load and bar speed | Perch fits a load-velocity line from set history and takes the load where the line meets the minimum velocity threshold (MVT). Every tracked exercise has a default MVT. Coaches can override it per exercise or per athlete, which is a premium feature. | kg or lb. MVT in m/s. | [mean-concentric-velocity](mean-concentric-velocity.md) | Default MVT values are not published. A higher MVT lowers e1RM. Perch says every tracked exercise has a default MVT. The reference file says not to report a squat or deadlift 1RM from velocity. Perch calls its line a line of best fit through set history. Which rep it uses at each load is not stated. The reference uses the fastest rep at each load. Profiles start after at least two loads separated by more than 30 lb according to one Perch page, and by 40 lb or more across multiple sessions according to another. The sources disagree. |
| Entered 1RM, Estimated 1RM, Linked 1RM | Source of the 1RM Perch uses for percent loads | Entered by the coach, estimated from the profile, or a percentage of another exercise. An asterisk marks an e1RM with a changed MVT. | kg or lb | None | Check the source and the asterisk before you compare 1RM values. |
| Speed Score, Strength Score, Total Performance Score | Where the athlete's load-velocity profile sits compared with a group | Speed Score is a z-score of the velocity intercept, which is unloaded max velocity. Strength Score is a z-score of the load intercept, similar to an estimated 1RM. Total Performance Score weights the two equally. | z-score | None | The reference group and whether the total is a mean or a sum are not published. |
| Speed zones (goals) | Five zones based on `Mean Velocity` | Absolute Strength below 0.5 m/s. Accelerative Strength 0.50 to 0.75. Strength Speed 0.75 to 1.0. Speed Strength 1.0 to 1.3. Starting Strength above 1.3 m/s. | m/s | None | Perch credits the zones to research by Dr. Bryan Mann. We did not read that research. The zones come from `Mean Velocity`, not `Mean Propulsive Velocity`. |
| Dynamic goal | A personal target speed zone for a load | Perch finds the velocity midpoint for the entered load on the athlete's profile. The zone runs from 5% below to 7.5% above the midpoint. The profile updates after every lift. | m/s | None | Professional and Championship tiers only. |
| `% Drop` goal | Velocity loss within a set, as a stop rule | A rep is flagged when it falls more than the set percentage below the first rep or the best rep. Choices are 5%, 10%, 15%, 20%, or manual. | % | [velocity-loss](velocity-loss.md) | Perch uses the first rep or the best rep as the reference. The reference file uses the fastest rep by default and the first rep only if the user's device defines it that way. The velocity measure is not stated. Whether `% Drop` appears in exports is not published. |
| `Jump Height` | Jump output from head tracking | Apex head height minus standing head height. Standing height is the head position before the jump. | Not published | None | Perch measures head displacement, not center-of-mass displacement. No comparison with force plates is published. Standard-tier Evaluate customers see `Jump Height` only. |
| `Time To Takeoff` | Time from the start of unweighting to takeoff | Covers the unweighting, braking, and propulsive phases. Takeoff is when the head returns to standing height after the push. | s | None | Depends on head tracking and posture. |
| `Takeoff Velocity` | Speed at takeoff | Instantaneous velocity at takeoff | Not published | None | Depends on head tracking and the arm swing variant. |
| `RSIMod` (also RSImod, RSI Modified) | Jump height relative to time to takeoff | `RSIMod = Jump Height ÷ Time To Takeoff` | No unit, by Perch's choice | None | Perch reports it for CMJ (Arms Fixed), CMJ (Arms Swing), and Continuous Jumps. |
| Readiness | Most recent jump session against earlier sessions | Compares the most recent jump session with the previous session and the 30-day average, then gives a z-score status. Green is above 1. Yellow is between -1 and -2. Red is -2 or below. | z-score | None | The published bands leave -1 to 1 unassigned. |
| Sets | Set counts | By exercise and by day, and sets per user | Count | None | Not applicable. |
| Reps | Rep counts | Reps per set. Compliance compares completed reps with prescribed reps. | Count | None | Not applicable. |
| Tonnage | Load lifted | Shown per user and in Compliance. The formula is not published. | Not published | None | Do not recompute tonnage. Take the exported value. |
| Volume | A volume total | The Train Sets report exports "sets, reps, volume". The meaning of volume is not published. On some pages volume means set count. | Not published | None | Ask the user what volume means in the export. |
| Goal Accuracy | How often reps or sets land inside the goal zone | Above or below the zone counts as inaccurate | % | None | Depends on the goal the coach set. |
| Compliance % | Completed work against the prescription | Inside a prescribed range is 100%. Below is the percent of the lower bound. Above is the percent of the upper bound. Daily totals use the range maximum. The symbols `>` and `<` mean at least and at most. | % | None | Depends on the prescribed range. |
| Time in Velocity Zones | Sets by speed zone | Count of sets by set-average `Mean Velocity` in the five zones | Count | None | Uses the set average, not the best rep. |
| Personal Best | Best result by rep count or by %1RM | Best rep or best set average, by rep count or by %1RM in 5% buckets. The lower edge is included and the upper edge is excluded. Untracked sets are excluded. | Same as the metric | None | Depends on which metric and which bucket the report uses. |

## Transform the data

Follow these steps to turn Perch exports into the athlete, session, and measure tables from `ams-data-setup`:

1. Ask the user for the CSV header row and the report name. Note whether the file is a Train Sets export at `Sets` level or `Reps` level, or an Insights report. Do not mix levels in one table.
2. Build the athlete table from the athlete identifier column in the header row. Perch does not publish the column name. Join sets and reps to athletes on that identifier.
3. Define a session as one athlete and one calendar date, and state the rule. The documented pages name no session identifier or time zone.
4. Convert weight to one unit. The organization's default weight unit drives exports. Record the unit that was used.
5. Reshape rep-level data to one row per athlete, session, exercise, set, rep, and metric. Keep concentric and eccentric mean velocity as separate metrics.
6. Label each velocity metric as `Mean Velocity`, `Mean Propulsive Velocity`, or `Peak Velocity`. For Olympic lifts, note that Perch uses the propulsive phase only for mean velocity.
7. Check the set level of each aggregate. Record whether it is the set average, the best rep, or the set minimum.
8. For lower-body unilateral exercises at rep level, find the left-right asymmetry fields in the header row. Do not assume a column layout.
9. Ask the user whether ghost reps and edited sets appear in the export. Perch deletes some ghost reps automatically, and coaches can edit sets after the session. Use the latest export.
10. Calculate velocity loss yourself from rep-level mean velocity. State the reference rep, the velocity measure, and the formula. Use the first rep or the best rep only if you want to match a Perch `% Drop` flag.
11. Pick the fastest rep per load when you need load-velocity data. If you use the Perch e1RM instead, record the MVT and whether the value has an asterisk.
12. Copy tonnage, volume, and `Total Work` as exported. Perch does not publish how it calculates tonnage, volume, or `Total Work`.

## Common mistakes

These are the mistakes most often made with Perch data:

- Comparing Perch and GymAware values without checking definitions. Perch uses a camera 3D path, and GymAware uses a tether. Perch `Mean Power` uses bar mass and gravity only. GymAware `meanPower` uses m × (a + 9.81) × v. GymAware does not provide mean propulsive velocity. GymAware set fields come from the best rep. Check the measure, the phase, and the rep before you compare.
- Calling `Mean Velocity` mean propulsive velocity. Perch has both. For Olympic lifts, Perch uses the propulsive phase only for `Mean Velocity`.
- Assuming Perch finds the end of the propulsive phase the way the reference file does. Perch does not publish its rule.
- Mixing concentric and eccentric mean velocity. Perch stores them separately.
- Assuming a velocity loss reference rep. Perch `% Drop` uses the first rep or the best rep. The reference file uses the fastest rep by default. State which one you use.
- Dividing `Peak Power` by `Mean Power` as if they share a force term. `Peak Power` has no gravity term, and `Mean Power` has gravity only.
- Using the 30 lb rule or the 40 lb rule for load-velocity profile start without noting the conflict. One Perch page says more than 30 lb, and another says 40 lb or more across multiple sessions. Check how far apart the loads are before you trust an e1RM.
- Reporting an e1RM for a squat or deadlift from velocity. The reference file says velocity cannot give an accurate 1RM in lower-body lifts. Perch gives every tracked exercise a default MVT, so an e1RM can appear. Show it as an estimate, and name the MVT. Do not call a squat or deadlift e1RM plausible because its implied MVT falls inside a published 1RM velocity range. A matching range does not validate it.
- Ignoring the asterisk on e1RM. It marks a changed MVT. A higher MVT lowers e1RM.
- Mixing entered 1RM, estimated 1RM, and linked 1RM in one trend.
- Mixing kg and lb. The organization's default weight unit drives exports.
- Recomputing tonnage or `Total Work` from your own formula. The formulas are not published.
- Treating volume as a known quantity. Its meaning is not published, and on some pages it means set count.
- Trusting values from sets with another object in view or a bar that left the frame. Perch names these as the usual causes of wrong values.
- Picking the wrong exercise on the tablet. Ghost rep rules are exercise-specific, and Perch deletes some ghost reps automatically.
- Comparing `Jump Height` from Perch with values from a force plate. Perch measures the head, not the center of mass.
- Reading readiness status without the gap in the bands. The published bands leave -1 to 1 unassigned.
- Assuming every account sees every metric. Standard-tier Evaluate customers see `Jump Height` only. Dynamic goals need the Professional or Championship tier.
- Treating untracked sets as tracked. Personal Best excludes untracked sets, and `Watts` is untracked power.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against a known set:

- The camera frame rate.
- The CSV export column names, row level, and date and time format.
- The Perch API schema, and which service tiers include an API token.
- The tonnage formula.
- The meaning of volume in the Train Sets export.
- The units of Displacement.
- How Perch finds the end of the propulsive phase for `Mean Propulsive Velocity`.
- Any smoothing or filter applied to velocity and power.
- The unit label for `Mean Power` and `Peak Power`.
- Whether `V100` is the speed at 100 ms or the mean over 0 to 100 ms.
- How reps and sets are summed into `Total Work`.
- The units of jump height and takeoff velocity.
- The default MVT values.
- The reference group for Speed Score and Strength Score, and whether Total Performance Score is a mean or a sum.
- Which of the two profile start rules is correct: two loads more than 30 lb apart, or 40 lb or more across multiple sessions.
- How Perch picks the best rep, and which velocity measure `% Drop` uses.
- Which rep Perch uses at each load when it fits the load-velocity line.
- Whether `% Drop` and the exercise variables appear in exports.
- Any published comparison of `Mean Velocity`, `Mean Propulsive Velocity`, `Peak Velocity`, power, work, scores, or goal zones against another device. We found none.
- The content of Perch's accuracy and reliability case study. It was not read.
- The content of the Bryan Mann research behind the five speed zones. It was not read.
- The content of the three `support.perch.fit` pages on defining metrics, CSV export, and exporting aggregated data. They could not be read.

## Sources

This file draws on these sources:

- Catapult, ASX release, "Catapult acquires Perch" (2025-06-05): <https://announcements.asx.com.au/asxpdf/20250605/pdf/06kg3qmc80p28y.pdf>, accessed 2026-10-02.
- Perch help center, "How Does Perch's Technology work": <https://perch.catapultsports.com/hc/en-us/articles/13221048860687-How-Does-Perch-s-Technology-work>, accessed 2026-10-02.
- Perch help center, "Metrics Measured by Perch": <https://perch.catapultsports.com/hc/en-us/articles/13221007932175-Metrics-Measured-by-Perch>, accessed 2026-10-02.
- Perch help center, "Frequent Ghost Reps": <https://perch.catapultsports.com/hc/en-us/articles/13221016118415-Frequent-Ghost-Reps>, accessed 2026-10-02.
- Perch help center, "Values Seem Wrong or Frequent Missed Reps": <https://perch.catapultsports.com/hc/en-us/articles/13221002633871-Values-Seem-Wrong-or-Frequent-Missed-Reps>, accessed 2026-10-02.
- Perch help center, "What is Perch's Accuracy and Reliability": <https://perch.catapultsports.com/hc/en-us/articles/13221076279439-What-is-Perch-s-Accuracy-and-Reliability>, accessed 2026-10-02.
- Perch help center, "Setting Goals in the Perch App": <https://perch.catapultsports.com/hc/en-us/articles/13220123005583-Setting-Goals-in-the-Perch-App>, accessed 2026-10-02.
- Perch help center, "Perch Insights": <https://perch.catapultsports.com/hc/en-us/articles/13220993284751-Perch-Insights>, accessed 2026-10-02.
- Perch help center, "Analyzing Evaluate Assessments on Perch": <https://perch.catapultsports.com/hc/en-us/articles/13220048058767-Analyzing-Evaluate-Assessments-on-Perch>, accessed 2026-10-02.
- Perch help center, "How Do I View an Individual Athlete's Data in Perch": <https://perch.catapultsports.com/hc/en-us/articles/13220975840015-How-Do-I-View-an-Individual-Athlete-s-Data-in-Perch>, accessed 2026-10-02.
- Perch help center, "Perch TRAIN Overview": <https://perch.catapultsports.com/hc/en-us/articles/13220953796495-Perch-TRAIN-Overview>, accessed 2026-10-02.
- Perch help center, "Setting MVTs, 1RMs and Estimated 1RMs": <https://perch.catapultsports.com/hc/en-us/articles/17032459331983-Setting-MVTs-1RMs-and-Estimated-1RMs>, accessed 2026-10-02.
- Perch help center, "Perch Load Velocity Profiling": <https://perch.catapultsports.com/hc/en-us/articles/13220069999631-Perch-Load-Velocity-Profiling>, accessed 2026-10-02.
- Perch help center, "Perch PLAN": <https://perch.catapultsports.com/hc/en-us/articles/13220766942991-Perch-PLAN>, accessed 2026-10-02.
- Perch help center, "Personal Best Report": <https://perch.catapultsports.com/hc/en-us/articles/14423298918287-Personal-Best-Report>, accessed 2026-10-02.
- Perch help center, "Exercise Variables": <https://perch.catapultsports.com/hc/en-us/articles/16667443904527-Exercise-Variables>, accessed 2026-10-02.
- Perch help center, "Generating an API Token": <https://perch.catapultsports.com/hc/en-us/articles/13220068158735-Generating-an-API-Token>, accessed 2026-10-02.
- Perch help center, "Does Perch Integrate with Third Party Software": <https://perch.catapultsports.com/hc/en-us/articles/13221006091151-Does-Perch-Integrate-with-Third-Party-Software>, accessed 2026-10-02.
- Perch help center, "Customizing Your Organization's Settings": <https://perch.catapultsports.com/hc/en-us/articles/13220015798799-Customizing-Your-Organization-s-Settings>, accessed 2026-10-02.
