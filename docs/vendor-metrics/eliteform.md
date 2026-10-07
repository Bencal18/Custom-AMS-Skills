# EliteForm metrics

EliteForm makes PowerTracker, a camera-based bar tracking display at the rack, and Strength Planner, a coach platform for workouts, teams, maxes, and reports. It also makes Paperless, an app for logging workouts away from the rack, and EliteForm Lift Tracker, an iPhone and iPad app. This page explains how each metric that EliteForm publicly documents is defined, so a coach or sports scientist can read EliteForm data correctly. Each fact links to its source. Checked against: EliteForm API 1.0 (the public OpenAPI document), the EliteForm Lift Tracker help center, and the eliteform.com news and about pages, 2026-10-07.

EliteForm, PowerTracker, Strength Planner, Paperless, Lift Tracker, and TeamSync are trademarks of their owner. This repository is not affiliated with or endorsed by EliteForm.

## How to read this page

Each metric block names the exact API field and then lists these items:

- What it measures.
- Calculation: EliteForm's definition in paraphrase. A formula labeled Restated is this page's plain restatement, not EliteForm's statement.
- Inputs and units.
- Variants.
- Comparison with standard methods or other vendors, only where a source supports it.
- What changes the number.
- Source links.

A detail marked Not published is one that EliteForm does not publish in the public sources checked. It does not mean EliteForm lacks the information.

## Overview

The overview covers these topics:

- **What the device measures:**
  - EliteForm says it brought patented 3D camera technology to major college and NFL weight rooms in 2012 ([source](https://www.eliteform.com/about)). The camera model: Not published.
  - The API says a tracked set was measured at an EliteForm rack using the camera ([source](https://api.eliteform.com/docs/)). EliteForm's pages describe no tether or accelerometer.
  - PowerTracker shows velocity, power, and work in the same graph format. The post-set summary marks the best rep and shows peak, average, and full-set results ([source](https://www.eliteform.com/news/new-powertracker-ui)). How the summary picks the best rep: Not published.
  - Coaches choose the main display for each exercise: velocity, power, work, or velocity and power side by side ([source](https://www.eliteform.com/news/velocitypowersidebyside), [source](https://www.eliteform.com/news/enablevelocitypower)).
  - Camera model, frame rate, smoothing, and rep detection rules for PowerTracker: Not published.
  - Lift Tracker uses the color and depth cameras of supported iPhone and iPad Pro models ([source](https://eflifttracker.crisp.help/en/article/which-iphone-and-ipad-versions-are-supported-1cntaqi/)). It tracks the hang clean, squat, bench press, trap bar deadlift, and barbell deadlift. It cannot track dumbbells or kettlebells ([source](https://eflifttracker.crisp.help/en/article/what-lifts-are-able-to-be-tracked-1f3ddca/)).
- **Export routes:**
  - EliteForm API 1.0 at `https://api.eliteform.com`. Read-only `GET` endpoints for teams, athletes, rosters, exercises, sessions, sets, reps, 1RMs, Power 1RMs, and weigh-ins, plus webhook subscriptions ([source](https://api.eliteform.com/docs/)).
  - Legacy `/api/v1` endpoints on each organization's EliteForm hostname still work, but are frozen. Their reference is Not published ([source](https://api.eliteform.com/docs/)).
  - Strength Planner CSV export: Not published.
  - TeamSync CSV export for Lift Tracker results: tap **Results**, then **Export** ([source](https://eflifttracker.crisp.help/en/article/how-do-i-export-results-1xl4ro1/)). Column names and row level: Not published.
- **Row level:**
  - `/sets`: one row per set on the workout card, done or not.
  - `/reps`: one row per tracked rep, with the set context repeated.
  - `/sessions`: one row per athlete per scheduled workout day.
  - `/one-rms` and `/power-one-rms`: the most recently dated max per athlete and exercise ([source](https://api.eliteform.com/docs/)).
- **Left and right labels:** No API field holds a side ([source](https://api.eliteform.com/openapi/public.json)). An asymmetry formula: Not published.
- **Tracked and Paperless sets:** A tracked set has `isTracked` set to `true` and velocity, power, and work values. A Paperless set was entered in the mobile app or a tracker in Paperless mode. It has `isTracked` set to `false`, `repCount` of `0`, and `null` aggregates ([source](https://api.eliteform.com/docs/)).

## API basics for coaches

The API basics are:

- **Authentication:** EliteForm creates an API key for the organization on request. Send it as `Authorization: Bearer <key>` or as `X-ApiKey: <key>`. Each key carries scopes, such as `ReadSets`, `ReadReps`, and `ReadOneRMs`, and can be limited to some teams ([source](https://api.eliteform.com/docs/)). Never put a key in shared code, a spreadsheet, or a URL.
- **Response format:** JSON. Each list holds `data`, `page`, and `meta`. A field with no value is `null`, never left out. Field names are `camelCase` ([source](https://api.eliteform.com/docs/)).
- **Paging:** Cursor-based. `page[size]` runs from 1 to 1000, default 100. Pass `page.nextCursor` as `page[after]` until `page.hasMore` is `false`. A cursor sent with different filters returns `400` ([source](https://api.eliteform.com/docs/)).
- **Dates:** `dateAfter` is inclusive and `dateBefore` is exclusive. Both take a plain date only. A window on sets, reps, and sessions spans at most 366 days and defaults to the last year. `/sets` and `/reps` need `teamId` unless the key is limited to one team ([source](https://api.eliteform.com/docs/)).
- **Time zones:** `occurredAtLocal` is the clock time of the rack that recorded the set, with no UTC offset. EliteForm states it does not attach an offset on purpose. Weigh-in `occurredAt` is in UTC ([source](https://api.eliteform.com/docs/)).
- **Changes:** No "changed since" filter exists. Webhook events `set.completed`, `set.updated`, and `set.deleted` report new and edited sets. A rep deleted at the rack or an edited Paperless set sends `set.updated` ([source](https://api.eliteform.com/docs/)).
- **Rate limits:** 60 requests a minute, 600 an hour, and 1,200 a day by default ([source](https://api.eliteform.com/docs/)).

## Rep-level metrics (`/reps`)

`/reps` holds the camera's per-rep measurements. Eccentric fields are `null` when the rack did not measure the lowering phase ([source](https://api.eliteform.com/docs/)).

### `avgVelocity` (m/s)

The block has these fields:

- **What it measures:** Average bar velocity of one rep.
- **Calculation:** EliteForm describes it as average velocity, in m/s ([source](https://api.eliteform.com/openapi/public.json)). The Predictive 1RM page says PowerTracker records the average velocity of every rep ([source](https://www.eliteform.com/news/predictive1rm)). The phase it covers and the start and end rules: Not published.
- **Inputs and units:** Camera bar path. m/s.
- **Variants:** Set `avgVelocity` is the mean of these values. `eccentricAvgVelocity` covers the lowering phase.
- **Comparison with standard methods or other vendors:** The repository's [mean concentric velocity reference](../../skills/velocity-based-training/references/mean-concentric-velocity.md) defines mean velocity over the concentric phase. EliteForm publishes no mean propulsive velocity field. GymAware also reports mean velocity, from a tether ([GymAware metrics](vald-other-products/gymaware.md)).
- **What changes the number:** Camera view and mounting. For Lift Tracker, a moving camera gives inaccurate velocities or rep counts ([source](https://eflifttracker.crisp.help/en/article/what-kind-of-mount-should-i-use-zwaj9w/)), and a rep without a good measurement shows `--` and is left out ([source](https://eflifttracker.crisp.help/en/article/why-is-my-velocity-value-missing-for-this-rep-kmbdob/)). PowerTracker equivalents: Not published.
- **Sources:** https://api.eliteform.com/openapi/public.json , https://www.eliteform.com/news/predictive1rm

### `peakVelocity` (m/s)

The block has these fields:

- **What it measures:** Highest bar velocity in one rep.
- **Calculation:** EliteForm describes it as peak velocity, in m/s ([source](https://api.eliteform.com/openapi/public.json)). Sampling window and smoothing: Not published.
- **Inputs and units:** Camera bar path. m/s.
- **Variants:** Set `peakVelocity` is the mean of these values, not the highest one. `eccentricPeakVelocity` covers the lowering phase.
- **What changes the number:** Frame rate and smoothing, both Not published.
- **Sources:** https://api.eliteform.com/openapi/public.json

### `avgPower` and `peakPower` (W)

The block has these fields:

- **What it measures:** Average and peak power of one rep.
- **Calculation:** EliteForm describes them as average power and peak power, in watts ([source](https://api.eliteform.com/openapi/public.json)). Formula, and whether body mass counts: Not published.
- **Inputs and units:** W.
- **Variants:** Set values are means over reps. `eccentricAvgPower` and `eccentricPeakPower` cover the lowering phase.
- **Comparison with standard methods or other vendors:** Perch and GymAware publish different power formulas ([Catapult metrics](catapult.md#perch-weight-room-velocity-based-training), [GymAware metrics](vald-other-products/gymaware.md)). With EliteForm's formula Not published, do not compare power across vendors.
- **Sources:** https://api.eliteform.com/openapi/public.json

### `work` (J)

The block has these fields:

- **What it measures:** Work done in one rep.
- **Calculation:** EliteForm describes it as work done, in joules ([source](https://api.eliteform.com/openapi/public.json)). Formula: Not published.
- **Variants:** Set `work` is the sum over reps. `eccentricWork` covers the lowering phase.
- **Sources:** https://api.eliteform.com/openapi/public.json

### `duration` (s) and `eccentricDuration` (s)

The block has these fields:

- **What it measures:** Rep duration, and the time of the lowering phase.
- **Calculation:** Phase start and end rules: Not published ([source](https://api.eliteform.com/openapi/public.json)).
- **Sources:** https://api.eliteform.com/openapi/public.json

### `reactionTimeMs` (ms)

The block has these fields:

- **What it measures:** Reaction time.
- **Calculation:** What starts and stops the timer: Not published. A rep with no reaction time shows `0` ([source](https://api.eliteform.com/openapi/public.json)).
- **Variants:** Set `reactionTimeMs` is the mean over the reps that recorded one, and `null` when none did.
- **What changes the number:** Restated: exclude reps with `0` before you average rep values yourself.
- **Sources:** https://api.eliteform.com/openapi/public.json

## Set-level fields (`/sets`)

A set record holds the prescription and, once done, the result. Set aggregates are means over the tracked reps. `work` is a sum ([source](https://api.eliteform.com/docs/)). This differs from GymAware, whose set fields come from the best rep ([GymAware metrics](vald-other-products/gymaware.md)).

### Prescription fields

The block has these fields:

- **What it measures:** What the workout card asked for.
- **Calculation:** `repsAssigned` is the reps prescribed, `null` on a max-reps set. `weight` is the weight prescribed, in the exercise's `weightUnit`. `loadFactor` is the target load written as a decimal share of the athlete's maximum, so `0.85` means 85%. It is empty (`null`) for bodyweight sets ([source](https://api.eliteform.com/openapi/public.json)). Which max `loadFactor` uses, entered or predicted: Not published.
- **Inputs and units:** Count, lb or kg, and fraction.
- **Variants:** `isMaxReps` and `isBodyweight` flag the two kinds of prescription that are not a number.
- **Sources:** https://api.eliteform.com/openapi/public.json , https://api.eliteform.com/docs/

### Result fields

The block has these fields:

- **What it measures:** What the athlete did.
- **Calculation:** `repsCompleted` is reps done. `actualWeight` is weight lifted, in the exercise's `weightUnit`. `actualRest` is rest before the set, timed at the rack, in seconds. `repCount` is the reps the camera captured, `0` when not tracked. `hasResults` is `true` once the set is done ([source](https://api.eliteform.com/openapi/public.json)).
- **Comparison with standard methods or other vendors:** The repository's [volume load reference](../../skills/strength-training-load/references/volume-load.md) uses reps and load lifted. Restated: volume load for one set is `repsCompleted × actualWeight`, in the exercise's unit. EliteForm publishes no tonnage or volume field.
- **Variants:** To reshape sets into one row per set, see the [training log exports reference](../../skills/strength-training-load/references/training-log-exports.md).
- **What changes the number:** Edits. A rep deleted at the rack changes the set and sends `set.updated`. A coach who republishes a workout over results replaces the sets ([source](https://api.eliteform.com/docs/)). How `actualWeight` is recorded on a bodyweight set: Not published.
- **Sources:** https://api.eliteform.com/openapi/public.json , https://api.eliteform.com/docs/

## Maxes and body mass

### `/one-rms` `result` and Predictive 1RM

The block has these fields:

- **What it measures:** The athlete's current one-rep max (1RM) for one exercise.
- **Calculation:** A 1RM is entered by a coach or predicted by EliteForm from tracked sets. `isPredicted` says which ([source](https://api.eliteform.com/docs/)). EliteForm describes Predictive 1RM, a beta feature, in three steps. PowerTracker records the load and average velocity of each rep. EliteForm builds a load-velocity profile across loads. It then extends the profile to a minimum velocity threshold set for each lift, and reports the load at that speed ([source](https://www.eliteform.com/news/predictive1rm)).
- **Inputs and units:** The exercise's `weightUnit`, `lb` or `kg`. It is `null` on an exercise with no unit set ([source](https://api.eliteform.com/openapi/public.json)).
- **Variants:** In Strength Planner, the 1RM Tests board shows Predicted, Best, and Current values. A coach previews predictions before applying them ([source](https://www.eliteform.com/news/predictive1rm)).
- **Comparison with standard methods or other vendors:** EliteForm says it is calibrated by lift and validated for the squat, bench press, and deadlift, and follows the 2021 review "Velocity-Based Training: From Theory to Application" in the NSCA Strength and Conditioning Journal ([source](https://www.eliteform.com/news/predictive1rm)). The repository's [mean concentric velocity reference](../../skills/velocity-based-training/references/mean-concentric-velocity.md) cites that review as Weakley et al. (2021a) and reads it as not supporting a velocity 1RM for the squat or deadlift. EliteForm publishes load guidance for the reps that feed the profile, listed under **What changes the number**. Threshold values, the fit, the exact rep selection rule, and the validation data: Not published. For 1RM estimates from reps, see the [estimated 1RM reference](../../skills/strength-training-load/references/estimated-1rm.md). Track coach-entered and predicted values apart, as the [personal bests reference](../../skills/strength-training-load/references/personal-bests.md) describes.
- **What changes the number:** EliteForm advises loads across about 50% to 85% of the current 1RM, maximum intent on every rep, and several distinct loads ([source](https://www.eliteform.com/news/predictive1rm)).
- **Sources:** https://api.eliteform.com/docs/ , https://www.eliteform.com/news/predictive1rm

### `/power-one-rms` `averagePower` and `peakPower` (W)

The block has these fields:

- **What it measures:** A Power 1RM, the power-training counterpart of a 1RM.
- **Calculation:** Entered by a coach against a date. The API describes both fields as prescribed power, in watts ([source](https://api.eliteform.com/openapi/public.json)). It is a target, not a measured result.
- **Sources:** https://api.eliteform.com/openapi/public.json

### `/weigh-ins` `weight` (lb)

The block has these fields:

- **What it measures:** Body mass from the EliteForm digital scale.
- **Calculation:** Scale reading, always in pounds, stamped in UTC ([source](https://api.eliteform.com/docs/)).
- **Comparison with standard methods or other vendors:** The repository's [personal bests reference](../../skills/strength-training-load/references/personal-bests.md) uses body mass for relative strength. Convert to kg first.
- **Sources:** https://api.eliteform.com/docs/

## Feedback and zones

### PowerTracker screen colors

EliteForm publishes these meanings ([source](https://www.eliteform.com/news/screen-colors)):

- Blue: faster than the prescribed velocity range.
- Green: inside the prescribed velocity range.
- Red: below the prescribed velocity range.
- Gold: a record performance. With competitions on for an exercise, a gold screen shows when an athlete records a new best result ([source](https://www.eliteform.com/news/leaderboardsetupguide)).

The range values come from the coach's prescription. How a new best is defined: Not published.

### Lift Tracker velocity zones

With TeamSync, Lift Tracker offers these zones. The screen turns green when the last rep is in the selected zone and red when it is not ([source](https://eflifttracker.crisp.help/en/article/how-do-velocity-zones-work-1nlj5k8/)):

| Zone | Velocity range | Pre-filled load |
|---|---|---|
| Absolute Strength | 0.00 to 0.50 m/s | 90% of 1RM |
| Accelerative Strength | 0.50 to 0.75 m/s | 72.5% of 1RM |
| Strength Speed | 0.75 to 1.00 m/s | 55% of 1RM |
| Speed Strength | 1.00 to 1.30 m/s | 35% of 1RM |
| Starting Strength | 1.30 m/s and above | 10% of 1RM |

The velocity measure behind the zones: Not published. Whether PowerTracker uses the same zones: Not published. These are vendor settings, not thresholds from the repository's reference files.

### Leaderboards

Coaches build a leaderboard from a competition group, an exercise, and a performance metric. The Velocity Meter style shows each result as a percentage of the leader's ([source](https://www.eliteform.com/news/leaderboardsetupguide), [source](https://www.eliteform.com/news/leaderboards)). Which metrics can be ranked: Not published.

## Not published

EliteForm does not publish these details in the public sources checked:

- PowerTracker camera model, frame rate, smoothing, and rep detection rules.
- The phase that rep velocity, power, work, and duration cover, and the start and end rules.
- Power and work formulas.
- What reaction time measures.
- How the post-set summary picks the best rep, and how a new best is defined.
- Which max `loadFactor` uses.
- Predictive 1RM threshold values, fit method, exact rep selection rule, and validation data. EliteForm publishes only load guidance.
- PowerTracker velocity zone values.
- How `actualWeight` is recorded on a bodyweight set.
- Strength Planner CSV export steps and columns.
- TeamSync CSV columns, and the unit of 1RM values in the TeamSync athlete upload file.
- Whether Lift Tracker data reaches the API.
- The legacy `/api/v1` reference.

## Worked example

This example uses made-up values and was run with Python 3.12.13 on 2026-10-07. The output below is copied from that run. It shows that set `peakVelocity` is a mean, not a maximum, and that velocity loss depends on the reference rep. The [velocity loss reference](../../skills/velocity-based-training/references/velocity-loss.md) explains the choice of reference rep.

```python
# Made-up EliteForm-style rep rows for one tracked set (back squat, 225 lb).
reps = [
    {"repNumber": 1, "avgVelocity": 0.64, "peakVelocity": 0.98},
    {"repNumber": 2, "avgVelocity": 0.66, "peakVelocity": 1.01},
    {"repNumber": 3, "avgVelocity": 0.61, "peakVelocity": 0.95},
    {"repNumber": 4, "avgVelocity": 0.57, "peakVelocity": 0.90},
    {"repNumber": 5, "avgVelocity": 0.52, "peakVelocity": 0.84},
]
n = len(reps)
set_avg = sum(r["avgVelocity"] for r in reps) / n
set_peak_mean = sum(r["peakVelocity"] for r in reps) / n
set_peak_max = max(r["peakVelocity"] for r in reps)
first = reps[0]["avgVelocity"]
fastest = max(r["avgVelocity"] for r in reps)
last = reps[-1]["avgVelocity"]
print(f"Set avgVelocity (mean of rep avgVelocity): {set_avg:.3f} m/s")
print(f"Set peakVelocity (mean of rep peakVelocity): {set_peak_mean:.3f} m/s")
print(f"Highest rep peakVelocity, for comparison: {set_peak_max:.3f} m/s")
print(f"Velocity loss, first rep to last rep: {(first - last) / first * 100:.1f} %")
print(f"Velocity loss, fastest rep to last rep: {(fastest - last) / fastest * 100:.1f} %")
actual_weight_lb, reps_completed = 225, 5
print(f"Volume load: {reps_completed} x {actual_weight_lb} lb = {reps_completed * actual_weight_lb} lb "
      f"= {reps_completed * actual_weight_lb * 0.45359237:.1f} kg")
```

Output:

```text
Set avgVelocity (mean of rep avgVelocity): 0.600 m/s
Set peakVelocity (mean of rep peakVelocity): 0.936 m/s
Highest rep peakVelocity, for comparison: 1.010 m/s
Velocity loss, first rep to last rep: 18.8 %
Velocity loss, fastest rep to last rep: 21.2 %
Volume load: 5 x 225 lb = 1125 lb = 510.3 kg
```

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.

## Sources

This page draws on these sources, all accessed 2026-10-07:

- EliteForm API reference: <https://api.eliteform.com/docs/>
- EliteForm API OpenAPI document, version 1.0: <https://api.eliteform.com/openapi/public.json>
- EliteForm, "About": <https://www.eliteform.com/about>
- EliteForm news, "Predictive 1RM (BETA)": <https://www.eliteform.com/news/predictive1rm>
- EliteForm news, "EliteForm Screen Colors": <https://www.eliteform.com/news/screen-colors>
- EliteForm news, "New PowerTracker UI": <https://www.eliteform.com/news/new-powertracker-ui>
- EliteForm news, "Velocity and Power Side By Side": <https://www.eliteform.com/news/velocitypowersidebyside>
- EliteForm news, "Enable Velocity and Power On One Screen": <https://www.eliteform.com/news/enablevelocitypower>
- EliteForm news, "Leaderboards Built For You": <https://www.eliteform.com/news/leaderboards>
- EliteForm news, "How To Setup Competitions And Leaderboards": <https://www.eliteform.com/news/leaderboardsetupguide>
- EliteForm news, "EliteForm Paperless": <https://www.eliteform.com/news/paperless>
- EliteForm Lift Tracker help center, "Which iPhone and iPad versions are supported?": <https://eflifttracker.crisp.help/en/article/which-iphone-and-ipad-versions-are-supported-1cntaqi/>
- EliteForm Lift Tracker help center, "What lifts are able to be tracked?": <https://eflifttracker.crisp.help/en/article/what-lifts-are-able-to-be-tracked-1f3ddca/>
- EliteForm Lift Tracker help center, "What kind of mount should I use?": <https://eflifttracker.crisp.help/en/article/what-kind-of-mount-should-i-use-zwaj9w/>
- EliteForm Lift Tracker help center, "Why is my velocity value missing for this rep?": <https://eflifttracker.crisp.help/en/article/why-is-my-velocity-value-missing-for-this-rep-kmbdob/>
- EliteForm Lift Tracker help center, "How do Velocity Zones work?": <https://eflifttracker.crisp.help/en/article/how-do-velocity-zones-work-1nlj5k8/>
- EliteForm Lift Tracker help center, "How do I Export results?": <https://eflifttracker.crisp.help/en/article/how-do-i-export-results-1xl4ro1/>
