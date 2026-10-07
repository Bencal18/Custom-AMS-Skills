# EliteForm data

Checked against: EliteForm API 1.0 (the public OpenAPI document at `api.eliteform.com/openapi/public.json`), the EliteForm Lift Tracker help center, and the eliteform.com news pages, 2026-10-07.

This file describes the EliteForm API output and export routes, what each metric means, and how to transform the data for analysis. It serves two skills. The `velocity-based-training` skill uses the velocity and power fields. The `strength-training-load` skill uses the set-level training log. EliteForm, PowerTracker, Strength Planner, Lift Tracker, TeamSync, and Paperless are trademarks of their owner. This repository is not affiliated with or endorsed by EliteForm.

EliteForm makes these products:

- PowerTracker: a rack display that shows live rep counts, velocity, power, and work. EliteForm says it brought patented 3D camera technology to college and NFL weight rooms in 2012. The camera model is not published. The API says a tracked set "was measured at an EliteForm rack using the camera".
- Strength Planner: the coach platform for workout design, team setup, 1RM setup, leaderboards, and reports.
- Paperless: a phone or tablet app where athletes open and log the workouts a coach built. Paperless sets are entered, not measured.
- EliteForm Lift Tracker: a separate iPhone and iPad app. It uses the device's color and depth cameras to track the bar and hands. TeamSync is its team app.

EliteForm describes camera-based measurement for PowerTracker and Lift Tracker. Its pages describe no tether or accelerometer. The camera frame rate, any smoothing, and the rep detection rules are not published.

## Get the data

Use one of these routes:

- API: base URL `https://api.eliteform.com`. EliteForm creates the API key for the organization on request. Send it as `Authorization: Bearer <key>`, or as `X-ApiKey: <key>`. Each key has scopes, such as `ReadSets` and `ReadReps`, and can be limited to some teams. Never put the key in shared code, a spreadsheet, or a URL.
- Webhooks: EliteForm posts `set.completed`, `set.updated`, and `set.deleted` events as athletes train. The event body for a completed or updated set is the same record that `/sets/{id}` returns.
- Legacy API: integrations built on the older `/api/v1` endpoints still work. Their reference is not public. Ask EliteForm for it.
- Strength Planner CSV export: not published. The pages read name report tools but no export steps or columns.
- Lift Tracker and TeamSync: in TeamSync, tap **Results**, then **Export**, to get a CSV file. The column names and row level are not published. Whether Lift Tracker data reaches the API is not published. Lift Tracker shows `--` or `N/A` for a rep it could not measure well, and leaves that rep's velocity out.
- Date and time format: dates are `YYYY-MM-DD`. `occurredAtLocal` is the clock time of the rack that recorded the set, with no UTC offset. Weigh-ins are stamped in UTC.

## API output

The API serves JSON. Every list has the same envelope: `data` holds the rows, `page` holds the paging state, and `meta` holds a request ID. A field with no value is `null`, never left out. A single record by ID comes back without the envelope.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /teams` | Teams in the organization | `id`, `name` |
| `GET /athletes` | Active athletes and their teams | `id`, `firstName`, `lastName`, `archived`, `teamIds` |
| `GET /teams/{teamId}/roster` | One team's athletes with positions, categories, and season classification | `athleteId`, `positions`, `categories`, `classification` |
| `GET /exercises` | Exercises defined on each team, with the weight unit | `id`, `teamId`, `name`, `weightUnit` |
| `GET /sessions` | One row per athlete per scheduled workout day | `id`, `athleteId`, `teamId`, `date`, `hasData` |
| `GET /sets` | One row per set on the workout card, done or not | See export columns below |
| `GET /reps` | One row per tracked rep, with its set context | See export columns below |
| `GET /one-rms` | Each athlete's most recently dated 1RM per exercise | `result`, `isPredicted`, `date` |
| `GET /power-one-rms` | Each athlete's most recently dated Power 1RM per exercise | `averagePower`, `peakPower`, `date` |
| `GET /weigh-ins` | Body mass readings from the EliteForm scale | `weight`, `occurredAt` |

The data nests as organization, then team, then athlete, then session (one workout day), then set, then rep. `/sets` and `/reps` need `teamId`, unless the key is limited to one team.

Follow these rules for paging and dates:

- Paging uses a cursor. Send `page[size]` from 1 to 1000. Default is 100. Pass `page.nextCursor` as `page[after]` until `page.hasMore` is `false`. Send the cursor with the same filters, or the API returns `400`.
- `dateAfter` is inclusive and `dateBefore` is exclusive. Both take a plain date only. A window on `/sets`, `/reps`, and `/sessions` can span at most 366 days, and defaults to the last year.
- `/sets`, `/reps`, and `/sessions` list the newest day first. Within a session, rows follow the card order.
- There is no "changed since" filter. Use webhooks, or read the window again.
- The default rate limit is 60 requests a minute, 600 an hour, and 1,200 a day.

## Export columns

These are the fields of one `/sets` row:

| Column name | Meaning | Units |
|---|---|---|
| `id`, `athleteId`, `teamId`, `sessionId`, `exerciseId` | Set ID and its links | ID |
| `date` | Workout day | `YYYY-MM-DD` |
| `exerciseNumber` | Place of the exercise on the card. Exercises in a superset share it. | Count |
| `supersetPosition` | Place within the superset. `1` for an exercise on its own. | Count |
| `setNumber` | Order of the set within the exercise | Count |
| `repsAssigned` | Reps prescribed. `null` on a max-reps set. | Count |
| `isMaxReps` | `true` on an as-many-as-possible set | True or false |
| `weight` | Weight prescribed | The exercise's `weightUnit` |
| `loadFactor` | Target load, written as a decimal share of the athlete's maximum, so `0.85` means 85%. Empty (`null`) for bodyweight sets. | Fraction |
| `isBodyweight` | `true` on a bodyweight set | True or false |
| `hasResults` | `true` once the set is done. Until then every result field is `null`. | True or false |
| `occurredAtLocal` | When the set was done, on the rack's clock | Local time, no offset |
| `repsCompleted` | Reps done | Count |
| `actualWeight` | Weight lifted | The exercise's `weightUnit` |
| `actualRest` | Rest before the set, timed at the rack | s |
| `isTracked` | `true` when the rack camera measured the set. `false` for a Paperless set. | True or false |
| `repCount` | Reps the camera captured. `0` when not tracked. | Count |
| `avgVelocity` | Average of the reps' average velocity | m/s |
| `peakVelocity` | Average of the reps' peak velocity | m/s |
| `avgPower` | Average of the reps' average power | W |
| `peakPower` | Average of the reps' peak power | W |
| `work` | Total work over the reps | J |
| `reactionTimeMs` | Average reaction time over the reps that recorded one | ms |

A `/reps` row repeats the set context (`setId`, athlete, team, date, session, exercise, card position, and `occurredAtLocal`) and adds `repNumber` and these fields:

| Column name | Meaning | Units |
|---|---|---|
| `duration` | Rep duration | s |
| `avgVelocity` | Average velocity | m/s |
| `peakVelocity` | Peak velocity | m/s |
| `avgPower` | Average power | W |
| `peakPower` | Peak power | W |
| `work` | Work done | J |
| `reactionTimeMs` | Reaction time. `0` when the rep recorded none. | ms |
| `eccentricDuration` | Time of the lowering phase. `null` when not recorded. | s |
| `eccentricAvgVelocity`, `eccentricPeakVelocity` | Average and peak velocity while lowering | m/s |
| `eccentricAvgPower`, `eccentricPeakPower` | Average and peak power while lowering | W |
| `eccentricWork` | Work while lowering | J |

The API has no side field and no left or right label. It has no mean propulsive velocity field and no velocity loss field.

## Metric meanings

EliteForm names its rep velocity "average velocity". It does not name the phase that the average covers. The lowering phase has its own `eccentric` fields. The start and end rules of each phase are not published. Treat `avgVelocity` as mean velocity, not mean propulsive velocity, and ask the user to confirm the phase.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| Rep `avgVelocity` | Average bar velocity of one rep | Not published beyond "average velocity" | m/s | `mean-concentric-velocity.md` in `velocity-based-training` | The phase and the rep start and end rules are not published. Camera path, not a tether. Not mean propulsive velocity. |
| Rep `peakVelocity` | Highest bar velocity of one rep | Not published beyond "peak velocity" | m/s | `mean-concentric-velocity.md` in `velocity-based-training` | Sampling window and smoothing are not published |
| Set `avgVelocity` | Set summary of average velocity | Mean of the reps' `avgVelocity` | m/s | `mean-concentric-velocity.md` in `velocity-based-training` | A mean over all tracked reps, not the best or fastest rep |
| Set `peakVelocity` | Set summary of peak velocity | Mean of the reps' `peakVelocity` | m/s | `mean-concentric-velocity.md` in `velocity-based-training` | A mean of peaks, not the highest peak in the set |
| `avgPower`, `peakPower` | Average and peak power | Formula not published. Set values are means over reps. | W | None | Do not compare with another vendor's power without the formula |
| `work` | Work done | Formula not published. Set value is the sum over reps. | J | None | Not published |
| `duration` | Rep duration | Not published | s | None | Phase not published |
| `reactionTimeMs` | Reaction time | What starts and ends the timer is not published | ms | None | A rep with none shows `0`. A set with none shows `null`. |
| `eccentric` fields | Lowering phase duration, velocity, power, and work | Not published | s, m/s, W, J | None | `null` when the rack did not record the lowering phase |
| Velocity loss | Drop in velocity across a set | No vendor field | % | `velocity-loss.md` in `velocity-based-training` | Calculate it from rep `avgVelocity`. State the reference rep. |
| PowerTracker screen colors | Live rep feedback | Blue is above the prescribed velocity range, green is inside it, and red is below it. Gold marks a record. | None | None | Range values come from the prescription. EliteForm gives coaching advice for each color but no velocity values. |
| Lift Tracker velocity zones | Five named speed zones | Absolute Strength 0.00 to 0.50 m/s, Accelerative Strength 0.50 to 0.75, Strength Speed 0.75 to 1.00, Speed Strength 1.00 to 1.30, Starting Strength 1.30 m/s and above. Each zone pre-fills a load of 90%, 72.5%, 55%, 35%, or 10% of 1RM. | m/s | None | Published for Lift Tracker with TeamSync. The velocity measure is not named. Whether PowerTracker uses the same zones is not published. |
| `/one-rms` `result` | The athlete's current 1RM for one exercise | Entered by a coach, or predicted by EliteForm when `isPredicted` is `true` | The exercise's `weightUnit` | `estimated-1rm.md` and `personal-bests.md` in `strength-training-load`, `mean-concentric-velocity.md` in `velocity-based-training` | See Predictive 1RM |
| Predictive 1RM (beta) | 1RM estimated from bar speed | EliteForm records the load and average velocity of every rep, builds a load-velocity profile across loads, and extends it to a minimum velocity threshold set for each lift. EliteForm says it is calibrated by lift and validated for the squat, bench press, and deadlift, and cites the 2021 review "Velocity-Based Training: From Theory to Application" in the NSCA Strength and Conditioning Journal. The reference file cites it as Weakley et al. (2021a). | The exercise's `weightUnit` | `mean-concentric-velocity.md` in `velocity-based-training`, `estimated-1rm.md` in `strength-training-load` | EliteForm gives load guidance: about 50% to 85% of the current 1RM, maximal concentric intent on every rep, and several distinct loads. The threshold values, the fit, the exact rep selection rule, and the validation data are not published. The reference file reads the same review as not supporting a velocity 1RM for the squat or deadlift. Call those values device estimates that this repository has not validated. |
| Power 1RM | Coach-entered power targets for one exercise | `averagePower` and `peakPower`, entered by a coach against a date. The API calls them prescribed values. | W | None | Not a measured result |
| `loadFactor` | Prescribed load as a fraction of a max | Which max it uses, entered or predicted, is not published | Fraction | `volume-load.md` in `strength-training-load` | A prescription, not the load lifted. Use `actualWeight`. |
| Gold screen and leaderboards | New best results and live rankings | With competitions turned on, a gold screen shows when an athlete records a new best result. Coaches pick the ranked metric for each leaderboard. | Same as the metric | `personal-bests.md` in `strength-training-load` | How a best is defined, and which metrics can be ranked, are not published. The API has no personal best endpoint. |
| `/weigh-ins` `weight` | Body mass from the EliteForm scale | Scale reading | lb | `personal-bests.md` in `strength-training-load` | Always in pounds, unlike lift weights |

## Transform the data

Follow these steps to turn the API output into the athlete, session, and measure tables from `ams-data-setup`, and the one-row-per-set table from `strength-training-load`:

1. Pull `/exercises` first. Record each exercise's `weightUnit`. It is `null` on an exercise with no unit set, so ask the user for the unit. An exercise belongs to one team, so the same lift on two teams has two IDs.
2. Build the athlete table from `/athletes`. Join on `athleteId`. Keep names out of the analysis tables.
3. Use `sessionId` as the session. One session is one athlete's workout day on one team.
4. Pull `/sets` with `hasResults=true` for the training log. Pull `/reps` for rep-level velocity.
5. Map `/sets` to the `sets` table in `training-log-exports.md`: `repsCompleted` to `reps`, `actualWeight` to `load`, `setNumber` to `set_number`, and `isBodyweight` to `load_type`. Keep the prescription fields `repsAssigned`, `weight`, and `loadFactor` apart from the results.
6. Convert each weight with its exercise's `weightUnit`. Multiply lb by 0.45359237 to get kg. Weigh-ins are always lb.
7. Keep `isTracked` on every row. Paperless sets have reps and loads but no velocity, power, or work.
8. Reshape `/reps` to one row per athlete, session, exercise, set, rep, and metric. Keep the eccentric fields as separate metrics.
9. Record the velocity measure as average velocity from a camera. Do not label it mean propulsive velocity.
10. Calculate velocity loss from rep `avgVelocity`. Name the reference rep and the formula.
11. For a load-velocity profile, take the fastest rep at each load from `/reps`, not the set `avgVelocity`.
12. Keep `/one-rms` values with `isPredicted` set to `true` in a separate column from coach-entered values.
13. Store `occurredAtLocal` as a local time. Do not convert it to UTC.

## Common mistakes

These are the mistakes most often made with EliteForm data:

- Reading set `peakVelocity` as the highest peak in the set. It is the mean of the reps' peak velocities.
- Reading set `avgVelocity` as the best rep. It is the mean over all tracked reps. GymAware set fields come from the best rep, as `gymaware.md` in `velocity-based-training` describes.
- Calling `avgVelocity` mean propulsive velocity. EliteForm publishes no mean propulsive velocity.
- Comparing EliteForm and Perch values with no check of the definitions. Both use cameras, but the phase rules, power formulas, and set summaries are not the same or are not published.
- Mixing lb and kg. The unit is set per exercise. Weigh-ins are always lb.
- Using `weight` or `loadFactor` as the load lifted. They are the prescription. Use `actualWeight` and `repsCompleted`.
- Counting undone sets. `/sets` lists every set on the card. Filter with `hasResults=true`.
- Treating a Paperless set as a set with zero velocity. Its velocity fields are `null`.
- Averaging `reactionTimeMs` over reps with `0`. A rep with no reaction time shows `0`.
- Mixing predicted and coach-entered 1RMs in one trend. Check `isPredicted`.
- Reporting a predicted squat or deadlift 1RM as validated. EliteForm says it is validated, but its threshold values and data are not published, and the reference file does not accept a velocity 1RM for those lifts.
- Converting `occurredAtLocal` to UTC. It has no offset.
- Expecting left and right labels. The API has no side field. Ask the user how single-leg and single-arm sets are named.
- Assuming the legacy `/api/v1` fields match the API 1.0 fields. Their reference is not public.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against a known set:

- The camera model, frame rate, smoothing, and rep detection rules for PowerTracker.
- The phase that rep `avgVelocity`, `peakVelocity`, `avgPower`, `peakPower`, `work`, and `duration` cover, and the start and end rules.
- The power and work formulas, and whether body mass counts.
- What reaction time measures.
- The PowerTracker velocity zone values, if they differ from the Lift Tracker zones.
- The minimum velocity thresholds, the exact rep selection rule, and the validation data for Predictive 1RM. EliteForm publishes only load guidance: about 50% to 85% of the current 1RM, maximal intent, and several distinct loads.
- Which max `loadFactor` refers to.
- How a new best is defined for the gold screen and leaderboards.
- How `actualWeight` is recorded on a bodyweight set.
- The Strength Planner export steps and columns.
- The TeamSync CSV columns, the units of the 1RM values in its athlete upload file, and whether Lift Tracker data reaches the API.
- The legacy `/api/v1` fields.

## Sources

This file draws on these sources:

- EliteForm API reference: <https://api.eliteform.com/docs/>, and its OpenAPI document, version 1.0: <https://api.eliteform.com/openapi/public.json>, accessed 2026-10-07.
- EliteForm, "About": <https://www.eliteform.com/about>, accessed 2026-10-07.
- EliteForm news, "Predictive 1RM (BETA)": <https://www.eliteform.com/news/predictive1rm>, accessed 2026-10-07.
- EliteForm news, "EliteForm Screen Colors": <https://www.eliteform.com/news/screen-colors>, accessed 2026-10-07.
- EliteForm news, "New PowerTracker UI": <https://www.eliteform.com/news/new-powertracker-ui>, accessed 2026-10-07.
- EliteForm news, "Velocity and Power Side By Side": <https://www.eliteform.com/news/velocitypowersidebyside>, accessed 2026-10-07.
- EliteForm news, "How To Setup Competitions And Leaderboards": <https://www.eliteform.com/news/leaderboardsetupguide>, accessed 2026-10-07.
- EliteForm news, "EliteForm Paperless": <https://www.eliteform.com/news/paperless>, accessed 2026-10-07.
- EliteForm news, "Strength Planner. Enhanced": <https://www.eliteform.com/news/new-strength-planner>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "Which iPhone and iPad versions are supported?": <https://eflifttracker.crisp.help/en/article/which-iphone-and-ipad-versions-are-supported-1cntaqi/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "EliteForm Lift Tracker Keys for Success": <https://eflifttracker.crisp.help/en/article/eliteform-lift-tracker-keys-for-success-1t1a8lp/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "What lifts are able to be tracked?": <https://eflifttracker.crisp.help/en/article/what-lifts-are-able-to-be-tracked-1f3ddca/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "How do Velocity Zones work?": <https://eflifttracker.crisp.help/en/article/how-do-velocity-zones-work-1nlj5k8/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "How do I Export results?": <https://eflifttracker.crisp.help/en/article/how-do-i-export-results-1xl4ro1/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "How do I upload and manage my Athletes?": <https://eflifttracker.crisp.help/en/article/how-do-i-upload-and-manage-my-athletes-1vuytmy/>, accessed 2026-10-07.
- EliteForm Lift Tracker help center, "Why is my velocity value missing for this rep?": <https://eflifttracker.crisp.help/en/article/why-is-my-velocity-value-missing-for-this-rep-kmbdob/>, accessed 2026-10-07.
