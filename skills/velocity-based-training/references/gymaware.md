# GymAware data

Checked against: the GymAware Cloud API integration guide and the GymAware Help Center, read on 2026-10-02.

This file describes the GymAware API output and export format, what each metric means, and how to transform the data for analysis. GymAware is made by Kinetic Performance Technology and has been owned by VALD since VALD announced the acquisition on 2026-08-10. GymAware, FLEX, and VALD are trademarks of their owners. This repository is not affiliated with or endorsed by GymAware, Kinetic Performance Technology, or VALD.

GymAware RS is a linear position transducer. A tether attaches to the bar and the device measures tether length and tether angle over time. GymAware converts these to vertical height, then derives velocity, power, and force from position and time. FLEX is a laser device that clips onto the end of the barbell and measures bar position over a reflective mat. It does not use an accelerometer.

## Get the data

Use one of these routes:

- Cloud export: in GymAware Cloud, go to **View > Sessions**, filter, select the sets, and select **Export**. The file is a CSV. The metric columns follow the account's default metrics under **Settings > Data**. The row level is not published.
- App export: the iPad app and the FLEX Stronger app also export CSV files. The column layout is not published.
- Cloud API: the API is included with the Premium Cloud license. The subscription page also lists "External API" as an add-on. Owners and Admins create API tokens in **Settings > Tokens**. GymAware advises one token per application.
- R: the `valdr` package has no GymAware functions.

The API uses HTTP Basic authentication. The user name is the Account ID and the password is the API token. The base URL is `https://cloud.gymaware.com/api/`. `POST /refresh` invalidates the current token and returns `accountID` and a new `token`. Never put tokens in shared code.

Date range limits:

- `/summaries` and `/reps`: send `start` and `end`, or neither. The guide says "max 1 month per request" and "start/end need to be within 60 days of each other". Use windows of 1 month or less to satisfy both.
- `/summaries` and `/reps`: `modifiedSince` must fall within the last 7 days. These endpoints return only sessions recorded in the last 180 days.
- `/bests`: `start` and `end` allow "max 3 months per request".

Date and time format: all times are UTC seconds since the epoch, as floats. `start` and `end` filter on the `recorded` time.

## API output

GymAware states: "The GymAware Cloud API get endpoints all return a newline separated stream of json objects." Read the body line by line and parse each line as one JSON object. The API has no page or cursor parameters. Use time windows to limit results.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /summaries` | One object per set, with best-rep metrics | `reference`, `recorded`, `modified`, `athleteReference`, `athleteName`, `exerciseName`, `activityName`, `activityReference`, `deleted`, `repCount`, `meanVelocity`, `peakVelocity`, `meanPower`, `peakPower`, `meanWattsPerKg`, `peakWattsPerKg`, `height`, `dip`, `velocityZone`, `targets`, `barWeight`, `athleteWeight` |
| `GET /reps` | One object per set, with a `reps` array | `reference`, `recorded`, `modified`, `athleteReference`, `athleteName`, `exerciseName`, `exerciseReference`, `activityName`, `activityReference`, `deleted`, `barWeight`, `athleteWeight`, `reps` |
| `GET /bests` | Personal bests per athlete, exercise, and bar weight | `athleteReference`, `athleteName`, `exerciseName`, `barWeight`, `height`, `dip`, `meanVelocity`, `peakVelocity`, `meanPower`, `peakPower`, `meanWattsPerKg`, `peakWattsPerKg` |
| `GET /analysis` | The rep metric types and how to aggregate each | `label`, `isPeak`, `isMin`, `isMean`, `isConcentric`, `isEccentric` |
| `GET /exercises` | The exercise list | `reference`, `modified`, `category`, `name`, `subname` |
| `GET` activities | Activity categories. The guide gives no URL. The official example app calls `activities`. | `reference`, `name`, `description`, `category`, `modified`, `vbt` |
| `/athletes` (GET, POST, DELETE), `/staff` (GET), `/squad` (GET, POST, PUT, DELETE), `/refresh` (POST), `/logout` (GET, POST) | Account management | Not described here |

The response nests like this. A set holds one `reps` entry per rep, matching `repCount`, ordered by `REPNUM`. Each `reps` entry holds `REPNUM` plus one float for each analysis type in `/analysis`. In `/bests`, one row is one athlete, exercise, and bar weight.

Details that matter when you read the output:

- Athlete: `athleteReference` and `athleteName`.
- Exercise: `exerciseName` in both endpoints, and `exerciseReference` in `/reps` only.
- Activity: `activityName` and `activityReference`. These fields came with GymAware Cloud 2.0.
- Deleted data: `/summaries` and `/reps` carry `deleted` (boolean). Filter out `deleted == true`. The Cloud removes deleted sets permanently after 30 days.
- Units: `barWeight` and `athleteWeight` are in kg, velocity is in m/s, power is in W, and relative power is in W/kg. The guide does not state units for `height`, `dip`, or the rep analysis values.
- Differences from the official example app: it reads `reference`, `referenceID`, and `deleted` from `/athletes`, `notes` from `/summaries`, and `userID` from `/staff`. The guide does not list these. It also sends an `athleteReference` filter to `/summaries` and `/reps`, and calls an undocumented `account` endpoint.
- Device: RS and FLEX can connect to the same Cloud. Whether API rows say which device recorded a set is not published.
- Left and right: no endpoint has a side field. Side appears only in exercise names, for example `Landmine Press - Left` and `Split Squat - Right`. Parse `exerciseName` or `activityName` to split by side.
- Test types: GymAware has no fixed test types. Every set belongs to an exercise and one activity. The activity categories are Jump, Olympic, Upper Body Horizontal Push, Upper Body Horizontal Pull, Upper Body Vertical Push, Upper Body Vertical Pull, Lower Body Push, and Lower Body Pull.

## Export columns

GymAware does not publish the column names or the row level of the Cloud, iPad, or FLEX CSV exports. Ask the user for the header row. Map each column to the API fields above by name, and to the display names in the table below.

## Metric meanings

GymAware measures bar velocity, not center-of-mass velocity. Set-level fields in `/summaries` come from one rep, the "best rep", or for `peakVelocity` the "peak rep". How GymAware picks the best rep is not published. Per-rep values are in `/reps`. The exact `/analysis` `label` strings are not published, so match each display name below to a label in your own `/analysis` output.

| Vendor name | What it means | How the vendor calculates it | Units | Metric reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `meanVelocity` (set, best rep) and Conc Mean Velocity (rep) | Average bar speed over the lifting phase | Sum of point velocities divided by the number of concentric points, with v = (d2 - d1) / (t2 - t1). The phase starts "where the displacement rapidly changes", not at the lowest point. Olympic lift catches are excluded. | m/s | [mean-concentric-velocity](mean-concentric-velocity.md) | This is mean velocity, not mean propulsive velocity. The phase runs to the top of the bar path. The set field is the best rep, not the set average or necessarily the fastest rep. |
| `peakVelocity` (set, "peak rep") and Conc Peak Velocity (rep) | Highest bar speed in the lifting phase | Instantaneous value over a sample period of about 20 ms | m/s | [mean-concentric-velocity](mean-concentric-velocity.md) | The reference takes the highest velocity sample. GymAware uses a window of about 20 ms. The set field can come from a different rep than `meanVelocity`. |
| Mean propulsive velocity | Not a GymAware metric | GymAware does not provide it | None | [mean-concentric-velocity](mean-concentric-velocity.md) | Do not label GymAware mean velocity as mean propulsive velocity. |
| Velocity loss, velocity drop-off, fatigue target | Percent drop in rep velocity across a set | No API field and no published formula. GymAware's worked examples use the first rep as the reference. VALD's article compares the fastest rep with later reps. | % | [velocity-loss](velocity-loss.md) | The reference file uses the fastest rep by default. GymAware's examples use the first rep. State which you use. |
| Ecc Mean Velocity, Ecc Peak Velocity, Eccentric Minimum Velocity | Lowering phase speed | Eccentric mean velocity sums point velocities over eccentric points. Eccentric minimum velocity has no published definition. | m/s | None | Sign convention is not published. RS eccentric metrics need Premium. |
| `meanPower` and Conc Mean Power | Average power in the lifting phase | Mean of m × (a + 9.81) × v over the concentric points | W | None | Mass is the bar weight, plus body mass for +BM exercises and jumps. |
| `peakPower` and Conc Peak Power | Highest power in the lifting phase | Maximum of m × (a + 9.81) × v, over about 20 ms | W | None | GymAware calls it less repeatable than mean power. |
| `meanWattsPerKg`, `peakWattsPerKg`, Mean Watts/kg, Peak Watts/kg | Power relative to body mass | Power divided by `athleteWeight` | W/kg (W/lb if the Cloud uses lb) | None | Value when body mass is missing is not published. |
| Conc Mean Force, Conc Peak Force, Ecc Peak Force | Force at the bar | Mean or peak of m × (a + 9.81) over the phase | N | None | Derived from position, not measured by a force sensor. |
| Rate of Force Development (RFD) | Fastest rise in force in the lifting phase | Maximum change in force over change in time between consecutive concentric samples | kN/s | None | The initial RFD is ignored. GymAware calls it easily affected by protocol. |
| Time to Peak Velocity, Time to Peak Force, Time to Peak Power | Time from the start of the lifting phase to each peak | Peak time minus concentric start time | s | None | Depends on concentric start detection. |
| Conc Rep Duration, Ecc Rep Duration, Rep Duration, Rep Rate | Phase and rep times, and predicted reps per minute | End time minus start time. Rep Rate is predicted from Rep Duration. | s, reps/min | None | The Rep Rate formula is not published. |
| Conc Work | Work to raise the load through the rep | Work = mass × 9.81 × vertical lift height | J | None | Depends on range of motion. |
| `height` (set) and Height (rep) | Highest point above the zero point | Maximum vertical position minus the zero position, corrected for horizontal displacement | Not published in the API. The Cloud shows m or in. | None | Depends on where zero is set. FLEX height is adjusted for dip. |
| `dip` (set) and Dip (rep) | Lowest point below the start | Start position minus lowest position, corrected for horizontal displacement | Not published in the API. The Cloud shows m or in. | None | Depends on the start point. |
| Lift Distance, Vertical Distance, Total Travel Path | Distance moved in a rep | Lift Distance is raw tether change. Vertical Distance is angle corrected. Total Travel Path ignores displacement corrections. | m or in | None | The Total Travel Path formula is not published. |
| Horizontal, Max Back, Max Forward, Height at Max Back, Height at Max Forward, Nordic Displacement | Horizontal bar movement and Nordic curl movement | Descriptions only. Formulas are not published. | m or in | None | Sign conventions are not published. |
| Reactive Strength Index (RSI), Contact Time, Flight Time | Drop jump and rebound jump measures | RSI = Jump Height / Ground Contact Time. Contact Time is the difference between landing time and takeoff time. | RSI in m/s, times in s | None | Landing and takeoff detection is not published. RSI needs a start position at floor level. |
| `repCount` | Reps detected and kept in the set | Count of reps found by rep detection, after edits | Count | None | A rep under 75% of the size of an earlier movement may not count on RS. Re-racking the bar can register as a rep. |
| `velocityZone` | Velocity zone of the set | Values, thresholds, and the velocity used are not published | Category | None | Do not assume it matches the zones in GymAware's or VALD's articles. |
| `targets` | The target the athlete aimed at in the set | Object with `analysis`, `mode`, and `preset`, `squad`, `last`, and `best`, each with `min` and `max` | Unit of the target metric | None | Coach settings at the time of the set. |
| `barWeight`, `athleteWeight` | External load and body mass stored with the set | Entered by the coach or athlete | kg | None | Whether `barWeight` includes body mass for +BM exercises is not published. |

GymAware also estimates 1RM from a linear load-velocity line. Its bench press example uses a minimum velocity threshold of 0.16 m/s. No API field carries this estimate. See the load-velocity section in `mean-concentric-velocity.md`.

## Transform the data

Follow these steps to turn GymAware API output or exports into the athlete, session, and measure tables from `ams-data-setup`:

1. Pull `/summaries` or `/reps` in windows of 1 month or less, with both `start` and `end`. Read each response line by line as newline-separated JSON.
2. Remove rows where `deleted` is `true`.
3. Build the athlete table from `athleteReference` and `athleteName`. Join sets to athletes on `athleteReference`.
4. Convert `recorded` from UTC seconds since the epoch to a date and time. The documented fields include no session identifier, so define a session as one athlete and one calendar date, and state that rule.
5. Keep `reference` as the set identifier. Keep one row per `reference`, using the row with the latest `modified`.
6. Pull `/analysis`. Match each key in the `reps` entries to its `label`, and record `isPeak`, `isMin`, and `isMean`.
7. Reshape `/reps` to one row per athlete, set, `REPNUM`, and metric. Order reps by `REPNUM`.
8. Parse `exerciseName` or `activityName` to add a side column for exercises that end in Left or Right.
9. Check units. Treat `barWeight` and `athleteWeight` as kg and velocity as m/s. Ask the user about `height`, `dip`, and the rep analysis values.
10. Calculate velocity loss yourself from the rep mean velocities in `/reps`. State the reference rep, the velocity measure, and the formula.
11. Pick the fastest rep per load from `/reps` when you need load-velocity data. Do not rely on the best rep in `/summaries`.

## Common mistakes

These are the mistakes most often made with GymAware data:

- Calling `meanVelocity` mean propulsive velocity. GymAware does not provide mean propulsive velocity.
- Treating set-level fields in `/summaries` as set averages. They come from one rep, and `peakVelocity` may come from a different rep than `meanVelocity`.
- Assuming a velocity loss reference rep. GymAware's examples use the first rep. VALD's article uses the fastest rep. In the made-up example set from the research, where rep 2 is fastest, the last rep shows 23.7% against the first rep and 27.6% against the fastest rep. State which one you use.
- Looking for a velocity loss field. The API has none. Compute it from `/reps`.
- Parsing the response as one JSON array. It is a stream of one JSON object per line.
- Sending only `start` or only `end`, or using a window longer than 1 month. Send both, or neither.
- Hard-coding rep metric keys. Read them from `/analysis`, because the `label` strings are not published.
- Keeping rows with `deleted` set to `true`.
- Reading power and not checking load. Wrong bar weight or body mass changes power, and +BM exercises add body mass automatically.
- Assuming API values follow the Cloud lb or inch display settings. This is not published.
- Mixing RS and FLEX sets without noting the device. API rows may not say which device recorded a set. The two devices measure position differently.
- Comparing GymAware jump height with jump mat values. GymAware says mats typically give higher values.
- Trusting `repCount` for sets with re-racking. Moving the bar into the rack can register as a rep.
- Assuming eccentric, timing, and jump metrics exist for every account. Many need a Premium license or the Advanced Metrics add-on.
- Putting an API token in shared code or in a prompt.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against a known set:

- The CSV export column names and row level.
- The exact `/analysis` `label` strings, and their units in the API.
- The units of `height` and `dip` in the API, and whether API values follow the lb or inch display settings.
- How `/summaries` and `/bests` choose the best rep and the personal best, and whether all best-rep fields come from one rep.
- The values and thresholds of `velocityZone`, and the `targets.mode` strings.
- Whether `barWeight` includes body mass for +BM exercises, and which exercises are +BM by default.
- Whether API rows mark the recording device (RS or FLEX).
- Whether `/analysis` returns eccentric and jump labels on lower license tiers.
- The URL of the activities endpoint, and the fields `notes`, `referenceID`, and `userID` used by the example app.
- Which rep the GymAware app uses for its fatigue target, and whether it can use peak velocity.
- A formal velocity loss formula.
- The formulas for Rep Rate, Total Travel Path, Horizontal, and Nordic Displacement.
- The sign conventions for eccentric metrics, Max Back, and Max Forward.
- How eccentric start and end, and landing and takeoff, are detected.
- The definitions of peak acceleration, eccentric mean power, and eccentric mean force.
- Whether the point average used for mean velocity matches concentric displacement divided by concentric duration. GymAware samples at a variable rate, down-sampled to at most 50 points per second.
- A GymAware asymmetry formula. The API has no side field.

## Sources

This file draws on these sources:

- VALD, "VALD Acquires GymAware" (announced 2026-08-10): <https://www.valdperformance.com/news/vald-acquires-gymaware-bringing-the-gold-standard-in-velocity-based-training-into-the-worlds-leading-performance-technology-ecosystem>, accessed 2026-10-02.
- GymAware Cloud API integration guide: <https://gymaware.com/gymaware-cloud-api-integration-guide/>, accessed 2026-10-02.
- GymAware example API app: <https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py>, accessed 2026-10-02.
- GymAware Help Center, "Parameters explained, measurement metrics": <https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics>, accessed 2026-10-02.
- GymAware Help Center, "Exporting data from the GymAware Cloud": <https://gymaware.zendesk.com/hc/en-us/articles/115001477352-Exporting-data-from-the-GymAware-Cloud>, accessed 2026-10-02.
- GymAware Help Center, "Cloud Subscription options": <https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options>, accessed 2026-10-02.
- GymAware Help Center, "Exercises on GymAware Cloud": <https://gymaware.zendesk.com/hc/en-us/articles/15412922699919-Exercises-on-GymAware-Cloud>, accessed 2026-10-02.
- GymAware Help Center, "Rep Detection": <https://gymaware.zendesk.com/hc/en-us/articles/360000067676-Rep-Detection>, accessed 2026-10-02.
- GymAware Help Center, "Funky reps, rep mark-up explained": <https://gymaware.zendesk.com/hc/en-us/articles/360000524955-Funky-reps-Rep-mark-up-explained>, accessed 2026-10-02.
- GymAware Help Center, "What does BM mean on the top right corner of my exercises": <https://gymaware.zendesk.com/hc/en-us/articles/115001650131-What-does-BM-mean-on-the-top-right-corner-of-my-exercises>, accessed 2026-10-02.
- GymAware Help Center, "Measuring Jumps with GymAware": <https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware>, accessed 2026-10-02.
- GymAware Help Center, "Testing depth jumps and obtaining RSI": <https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI>, accessed 2026-10-02.
- GymAware Help Center, "How is RFD calculated": <https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated>, accessed 2026-10-02.
- GymAware Help Center, "Editing Data on the Cloud": <https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud>, accessed 2026-10-02.
- GymAware, "Angle correction" (Kinetic Performance Technology): <https://kinetic.com.au/pdf/angle.pdf>, accessed 2026-10-02.
- GymAware, "Variable Rate Sampling" (Kinetic Performance Technology): <https://kinetic.com.au/pdf/sample.pdf>, accessed 2026-10-02.
- GymAware, "Do you need mean propulsive velocity": <https://gymaware.com/do-you-need-mean-propulsive-velocity/>, accessed 2026-10-02.
- GymAware, "Velocity loss in strength training": <https://gymaware.com/velocity-loss-in-strength-training/>, accessed 2026-10-02.
- GymAware, "Train to velocity failure using velocity stops": <https://gymaware.com/train-to-velocity-failure-using-velocity-stops/>, accessed 2026-10-02.
- GymAware, "Barbell vs system velocity": <https://gymaware.com/barbell-vs-system-velocity/>, accessed 2026-10-02.
- GymAware, "GymAware 1RM calculation": <https://gymaware.com/gymaware-1rm-calculation/>, accessed 2026-10-02.
- GymAware, "GymAware joins VALD Performance": <https://gymaware.com/gymaware-joins-vald-performance/>, accessed 2026-10-02.
- VALD, "VALD acquires GymAware": <https://valdperformance.com/news/vald-acquires-gymaware-bringing-the-gold-standard-in-velocity-based-training-into-the-worlds-leading-performance-technology-ecosystem>, accessed 2026-10-02.
- VALD, "Using VBT to autoregulate and individualize resistance training": <https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training>, accessed 2026-10-02.
- `valdr` R package source: <https://github.com/cran/valdr>, accessed 2026-10-02.
