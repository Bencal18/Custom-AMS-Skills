# VALD SmartSpeed metrics

SmartSpeed is a timing gate system. It records split times, cumulative times, and derived speeds for sprint, change of direction, interval, and timing drills. The optional SmartJump mat records flight time and contact time for jump drills. Checked against: the VALD knowledge base (including the SmartSpeed Plus iOS release notes, the VALD Hub release notes, and the External SmartSpeed API guide), the External SmartSpeed API OpenAPI spec, VALD SmartSpeed spec sheets and quick start guides, VALD education pages, VALD cheat sheets, and the `valdr` R package source, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

This page is part of [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](vald-other-products.md). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](vald-forcedecks-nordbord.md).

## How to read this page

Each metric block names the exact field or Hub name and then lists the following items, where the sources support them:

- What it measures.
- Calculation: VALD's definition in paraphrase, then the formula in plain math where a source gives one.
- Inputs and units.
- Variants.
- What changes the number.
- Source links.

A formula labeled Restated is this page's plain restatement, not the vendor's statement. A calculation or detail marked Not published is one that the vendor does not publish in the public sources checked. It does not mean the vendor lacks the information. None of the VALD OpenAPI specs carry field descriptions, so definitions come from the VALD knowledge base, VALD education pages, and the `valdr` R package.

## SmartSpeed

### Overview

The SmartSpeed system has these parts:

- **What the device measures.** SmartSpeed is a timing gate system. Each gate is a timing unit on a tripod that points a beam at a reflector on a second tripod. The system records the time when an athlete breaks each beam. VALD describes time splits as measured when the athlete passes through an infrared or laser beam ([source](https://valdperformance.com/news/timing-gates-101)). The optional SmartJump jump mat records flight time and contact time during a jumping protocol ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). The SmartPad start pad and SmartShoxx impact sensor plug into a gate ([source](https://support.vald.com/hc/en-au/articles/4996482906905-SmartSpeed-Optional-Accessories), [source](https://support.vald.com/hc/article_attachments/31800152349721)).
- **Models.** SmartSpeed Plus (time of flight LiDAR and reflector), SmartSpeed Dash (single beam photocell and reflector), and SmartSpeed Pro (single beam photocell, superseded by Plus). Plus and Dash log time to 1/1000 s ([source](https://support.vald.com/hc/en-au/articles/4996484198297-SmartSpeed-Model-Comparison)). The Pro time unit is Not published. VALD marks Pro as superseded by SmartSpeed Plus ([source](https://support.vald.com/hc/en-au/articles/9848256433049-SmartSpeed-Starter-s-Guide)). All models run in the SmartSpeed Plus iOS app. The older SmartSpeed app was discontinued on 2025-03-15 ([source](https://support.vald.com/hc/en-au/articles/44078746580633-Upgrade-to-the-SmartSpeed-Plus-app)).
- **Export routes.** Data leaves SmartSpeed by these routes:
  - VALD Hub CSV. Restated: in VALD Hub, open **Dashboard** > **Results Export** > **SmartSpeed**, filter by test type and date, then export ([source](https://support.vald.com/hc/en-au/articles/28173187417369-Enable-trial-validity-in-the-SmartSpeed-Plus-app), [source](https://support.vald.com/hc/en-au/articles/42843499827353-Edit-a-SmartSpeed-test), [source](https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub)). The full Hub CSV column list is Not published. Release notes say the CSV includes 4 splits, reaction time, and trial number ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). The Hub velocity unit setting (km/h, m/s, mph, or yd/s) changes velocity values in Results Export, Result Table, and CSV exports ([source](https://support.vald.com/hc/en-au/articles/27432433786009-Customize-Unit-of-Measurement-in-VALD-Hub)).
  - External SmartSpeed API. Base URLs: `https://prd-aue-api-extsmartspeed.valdperformance.com/` (Australia East), `https://prd-use-api-extsmartspeed.valdperformance.com/` (United States East), and `https://prd-euw-api-extsmartspeed.valdperformance.com/` (Europe West) ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)). The spec declares OAuth2 security and has no field descriptions ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). The endpoints are:
    - `GET /v1/team/{teamId}/tests`: an array of test summaries (`GetTestSummariesHttpResponse`). Query parameters: `AthleteId`, `TestFromUtc`, `TestToUtc`, `ModifiedFromUtc`, `GroupUnderTestId`, `Page`. VALD describes the summaries as a high-level, easy-to-read view of the test results ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)).
    - `GET /v1/team/{teamId}/tests/{testId}/detail`: one test with every rep, split, and jump (`GetTestDetailHttpResponse`). VALD says this information covers the individual split timings between gates and the individual jump results in the test ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)).
    - `GET /v1/test/tests-by-modified-date`: query `TenantId` and `ModifiedFromUtc`. Returns `TestCursorHttpResponse` with a `summaries` array. Each summary has the same metric groups as the team endpoint, plus `testSessionId`, `modifiedDateUtc`, and `trialNumber` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). The KB API guide does not describe this endpoint. valdr uses it ([source](https://github.com/cran/valdr/blob/master/R/smartspeed_tests.R)).
    - `GET /version`, `/liveness`, `/readiness`, `/diagnostics`: service health. No athlete data.
  - valdr (R). `get_smartspeed_data()` returns a list with `profiles` and `tests`. `get_smartspeed_tests_only()` returns the tests data frame ([source](https://github.com/cran/valdr/blob/master/R/session.R)). Both page through `/v1/test/tests-by-modified-date` until the API returns 204 or an empty list ([source](https://github.com/cran/valdr/blob/master/R/smartspeed_tests.R)). valdr flattens nested summary fields into columns that keep only the last name part, for example `runningSummaryFields.velocityFields.fvpSummaryDto.maxVelocity` becomes `maxVelocity`. It stores `allGroups` as a JSON string ([source](https://github.com/cran/valdr/blob/master/R/utils.R)). valdr has no function for the detail endpoint, so splits beyond `splitFour`, per-gate times, jump-by-jump data, and `reactionTime` are not in valdr output.
- **Row level.** Each source has a different row unit:
  - Summary endpoints: one record per test. VALD defines `id` as the unique identifier of the test ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)). One test is one trial within a session. VALD defines `trialIndex` as the number of the test within the testing session ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)).
  - Detail endpoint: one test, with `repResults` (one item per rep). Each rep holds `splitResults` (one item per gate break) and `jumpResults` (one item per jump) ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
  - valdr: one row per summary record ([source](https://github.com/cran/valdr/blob/master/R/utils.R)).
  - Hub CSV: Not published. Hub charts and Timeline show the session or day best, not each trial ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)).
- **Left and right labels.** SmartSpeed has no left and right limb fields. Change of direction drills store a direction. The `Direction` enum is `Left`, `Right`, `Random`, `Both`. The app offers "random, left, right, or both" for change of direction ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). The detail endpoint has a free-text `direction` string and an integer `expectedDirection` per split. Their encodings are Not published. How single-leg jump drills record the leg is Not published.
- **Test types.** The API `TestTypeName` enum lists 18 values ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). The app drill list groups drills as Sprints, Change of Direction, Jumps, Free Timing, Intervals, Intermittent Fitness Tests, and Other ([source](https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List)). VALD does not publish a mapping from app drill names to `TestTypeName`. The table below matches them by name and cites the KB drill article for each.

The table below maps each `TestTypeName` value to the KB drill with the matching name:

| `TestTypeName` | KB drill (matched by name) | Notes |
|---|---|---|
| `OneWay` | One-Way Timing, Sprint, 40m Traffic Light Start | A drill with one defined start and a separate defined finish ([source](https://support.vald.com/hc/en-au/articles/4997545365913-SmartSpeed-Drill-One-Way-Timing)). 2+ gates. |
| `TrafficLightSprint` | Traffic Light Sprint | Traffic light or reactive start ([source](https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint)). |
| `Cut` | Cut Drills, custom change of direction | 3+ gates, uses "levels" ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)). |
| `TrafficLightStart_0121` | Cut (0-1-2-1) Traffic Light Start | Name match only ([source](https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List)). |
| `TrafficLightStart_0123` | Cut (0-1-2-3) Traffic Light Start | Name match only. |
| `TrafficLightStart_013` | Cut (0-1-3) Traffic Light Start | Name match only. KB: "Cut 0-1-3 is 2 levels with level 1 set as 0 (Reactive)." ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)) |
| `AutoStart_112` | Y Agility (1-1-2) | Digits match only. KB: "Cut 1-1-2 is 3 levels with level 1 set as 1 (Start Gate)." ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)) Mapping Not published. |
| `ProAgility` | Pro Agility Drill 5-10-5 | In-beam start in the middle gate ([source](https://support.vald.com/hc/en-au/articles/4997398652825-SmartSpeed-Drill-Pro-Agility)). |
| `ReactiveProAgility` | Reactive Pro Agility Drill 5-10-5 | Measures reaction time plus drill time ([source](https://support.vald.com/hc/en-au/articles/4997452301849-SmartSpeed-Drill-Reactive-Pro-Agility)). |
| `Free` | Free Timing (5-0-5, Box, L-Drill, Lane Agility, T-Test) | Any beam in any order ([source](https://support.vald.com/hc/en-au/articles/4997399394201-SmartSpeed-Drill-Free-Timing)). |
| `Serpentine` | 30m Serpentine | Colour cue at the next gate ([source](https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine)). |
| `Grid` | 4 Point Grid | Colour cue, reps or duration ([source](https://support.vald.com/hc/en-au/articles/4997511951641-SmartSpeed-Drill-Grid)). |
| `IntervalProtocol` | 30m Repeat Sprint Ability Test | Fixed Recovery or Fixed Duration ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)). |
| `IntervalShuttle` | Custom Shuttle Runs | Name match only. Shuttle Runs do not run in the SmartSpeed Plus app ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). |
| `Pacing` | Pacing (Pro) | Light cues set pace ([source](https://support.vald.com/hc/en-au/articles/4997515544217-SmartSpeed-Drill-Pacing)). Not in SmartSpeed Plus app ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). |
| `LapTiming` | 10 Lap Timing | Start and finish at the same gate ([source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)). |
| `FvpSprint` | FVP Sprint | No KB drill article. Not in SmartSpeed Plus app ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). |
| `Jumping` | Abalakov, CMJ, Drop Jump, Hop Test, single leg CMJ, single leg hop, Squat Jump, Vert jump | Needs the jump mat ([source](https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List), [source](https://support.vald.com/hc/en-au/articles/4997420680089-SmartSpeed-Drill-Vertical-Jump)). |

Beep Test and VAM Eval Test appear in the app drill list ([source](https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List)). Their `TestTypeName` is Not published.

### How timing works

This section applies to every timed field below. The timing rules are:

- **Start of timing by start type.** The API `StartType` enum is `Standard`, `InBeam`, `TrafficLight`, `ReactiveStart` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). The SmartSpeed Plus app offers "break beam, in-beam, or SmartJump/SmartPad" ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). The start types work as follows:
  - `Standard` (break beam). VALD says the athlete begins ahead of the start beam, and timing begins when the athlete breaks that beam ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)). VALD recommends a lead-in distance of 12 in (30 cm) for break beam starts, to avoid false triggers ([source](https://valdperformance.com/news/timing-gates-101)). Restated: time zero is the break of the first gate, so the first split is gate 1 to gate 2.
  - `InBeam` (also mat start). VALD says the athlete begins with the beam directly on the body, and timing begins when the athlete leaves the beam ([source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)). With a SmartPad, timing begins when pressure is removed from the pad ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)). The SmartSpeed Plus jump mat or SmartPad start needs a 3 s hold before the drill starts ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). VALD advises you to center the beam on the athlete's midline and to avoid a "false step" ([source](https://valdperformance.com/news/timing-gates-101)).
  - `TrafficLight`. VALD says the athlete hears a 1-2-Go countdown, and timing begins when the light turns green or the buzzer sounds ([source](https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint)).
  - `ReactiveStart`. VALD says timing starts when the gate flashes green after a randomised delay. Reaction time is captured from the gate flash to the first break of the first gate ([source](https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint)). The delay range comes from `reactiveDelayMinimumInSeconds` and `reactiveDelayMaximumInSeconds`.
  - Whether `splitTime` and `cumulativeTime` include the cue-to-first-gate interval for `TrafficLight` and `ReactiveStart` tests is Not published.
- **Flying starts and start offsets.** No flying start type exists in the API. A flying 10 m is a common SmartSpeed test ([source](https://valdperformance.com/news/timing-gates-101), [source](https://valdhealth.com/news/managing-deceleration-in-return-to-sport-scenarios)). Run-in distance for a flying sprint is Not published. A start offset field is Not published.
- **End of timing.** Timing stops when the athlete breaks the final gate ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)).
- **Restarts.** For break-beam sprint starts, an athlete can retrigger the start by passing through the first gate again ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). A bug before v1.17.0 (2024-09-26) made cumulative times count from the first break of a repeatedly broken start gate ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **Error Correction Processing (ECP).** VALD says the gate records data for one second and uses the longest break as the reference for the break time ([source](https://support.vald.com/hc/en-au/articles/4996430805017-Error-Correction-Processing-ECP)). VALD describes this as moving the start time to the longest break, which is typically the first break of the torso ([source](https://support.vald.com/hc/en-au/articles/4997268643609-SmartSpeed-FAQs)). With ECP off, the gate uses the first break as the time reference ([source](https://support.vald.com/hc/en-au/articles/4996430805017-Error-Correction-Processing-ECP)). Users may turn ECP off for racquets, balls, sticks, bicycles, or wheelchairs ([source](https://support.vald.com/hc/en-au/articles/4997268643609-SmartSpeed-FAQs)). Restated: the timestamp for a gate is the start of the longest beam break within 1 s of the first break. The API does not report whether ECP was on for a test.
- **Gate distances.** You set a split distance in the app. VALD defines it as the distance from gate 1 to gate 2, gate 2 to gate 3, and so on ([source](https://support.vald.com/hc/en-au/articles/4997545365913-SmartSpeed-Drill-One-Way-Timing)). In VALD Hub you can re-enter split distances per gate when you change a sprint drill type. VALD says that with only two gates connected, the split distance equals the total distance ([source](https://support.vald.com/hc/en-au/articles/42843499827353-Edit-a-SmartSpeed-test)). The detail endpoint does not return per-gate distances. The summary returns one `distance` value ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). Measure distances with a tape measure ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates)).
- **Gate alignment and spacing (unit to reflector).** The sources give these values by model:
  - SmartSpeed Plus: place the unit and reflector 1 m to 2 m apart, perpendicular to the direction of travel. VALD warns that under 1 m the gate "may not function correctly" ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates)). The Plus spec sheet lists a 4 m unit-to-reflector range ([source](https://support.vald.com/hc/en-au/article_attachments/62792691604889)). Since v1.22.0 the app prompts you to verify alignment when a gate's alignment distance is under 100 cm or when gates differ by more than 60 cm ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). If a gate goes out of alignment mid-drill, realign it and tap **Reset** to rerun the trial ([source](https://support.vald.com/hc/en-au/articles/16732705756313-SmartSpeed-Plus-Align-your-timing-gates)).
  - SmartSpeed Dash: about 2 m apart in the KB ([source](https://support.vald.com/hc/en-au/articles/4996910107289-SmartSpeed-Dash-Set-up-your-timing-gates)), 1 m to 4 m in the Quick Start Guide ([source](https://support.vald.com/hc/en-au/article_attachments/29460216899737/VALD%20SmartSpeed%20Dash%20Quick%20Start%20Guide%20V1.4%20.pdf)), 7 m maximum in the spec sheet ([source](https://support.vald.com/hc/en-au/article_attachments/62792687636121)).
  - SmartSpeed Pro: 1 m to 2 m in the KB ([source](https://support.vald.com/hc/en-au/articles/4996881817881-SmartSpeed-Pro-Setup-Timing-Gates)), 1 m to 4 m in the Quick Start Guide ([source](https://support.vald.com/hc/article_attachments/29751035498265)), 7 m maximum in the spec sheet ([source](https://support.vald.com/hc/en-au/article_attachments/62792687633433)).
- **Gate height.** VALD says to set the tripod height so the beam breaks around the athlete's torso ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates)). VALD also advises you to keep the gate height consistent, so that different body parts do not break the beam between tests ([source](https://valdperformance.com/news/timing-gates-101)). A numeric height is Not published.
- **Run-off.** VALD recommends 20 yd or more after the final gate ([source](https://valdperformance.com/news/timing-gates-101)).
- **Gate rearm.** The time for a gate to reactivate for the next athlete. The One-Way Timing setup steps list "Confirm Re-arm: 500 ms" and tell you to adjust it as required ([source](https://support.vald.com/hc/en-au/articles/4997545365913-SmartSpeed-Drill-One-Way-Timing)).
- **Timing resolution.** 1/1000 s on Plus and Dash ([source](https://support.vald.com/hc/en-au/articles/4996484198297-SmartSpeed-Model-Comparison)). The Dash spec sheet lists a 4 kHz oscillator with 10 PPM tolerance ([source](https://support.vald.com/hc/en-au/article_attachments/62792687636121)).
- **Firmware.** VALD warns that gates on mixed firmware can cause issues with uploaded testing data ([source](https://support.vald.com/hc/en-au/articles/20042352205337-Update-SmartSpeed-Plus-firmware)).

### Sprint and split drills: per-gate detail

These fields come from `GET /v1/team/{teamId}/tests/{testId}/detail`, inside `repResults[].splitResults[]` and `additionalTestResult`.

#### `splitTime` (unit Not published in the API; Hub shows seconds)

This block has these fields:

- **What it measures:** the time for one segment of the drill, between two gate breaks.
- **Calculation:** Not published as a formula. VALD lists "Individual split" in seconds as a SmartSpeed time metric ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). The app shows "split times (S)" and "cumulative time (C)" for each trial ([source](https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine)). Restated: `splitTime` is the time from the previous gate break to this gate break. VALD defines the split distance setting as the distance from gate 1 to gate 2, gate 2 to gate 3, and so on ([source](https://support.vald.com/hc/en-au/articles/4997545365913-SmartSpeed-Drill-One-Way-Timing)), which supports this reading.
- **Inputs and units:** gate break timestamps after ECP. Float in the API with no unit in the name ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** summary `splitOne` to `splitFour`, `bestSplitSeconds`, `splitAverageSeconds` (see below). Each split also has `splitCompleteDate` (date-time of the split) and `additionalSplitData`.
- **What changes the number:** ECP on or off ([source](https://support.vald.com/hc/en-au/articles/4996430805017-Error-Correction-Processing-ECP)), gate height and limb breaks ([source](https://valdperformance.com/news/timing-gates-101)), gate distance accuracy ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates)), surface, footwear, wind, warm-up, and cueing ([source](https://valdperformance.com/news/timing-gates-101)).
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json, https://valdperformance.com/news/buyers-guide-to-timing-gates, https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine

#### `cumulativeTime` (unit Not published in the API; Hub shows seconds)

This block has these fields:

- **What it measures:** the running total time from the start of timing to this gate.
- **Calculation:** Not published as a formula. VALD names cumulative time as the default gate display ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). A fixed bug made cumulative times count from the first break of the starting gate when that gate was broken repeatedly ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). Restated: `cumulativeTime` at gate k = sum of `splitTime` from the first split through split k, counted from the start event of the trial.
- **Inputs and units:** start event (see start types above) and gate break timestamps.
- **Variants:** summary `cumulativeOne` to `cumulativeFour`. `goalCumulativeTime` in `additionalSplitData`.
- **What changes the number:** start type ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)), restarts through the first gate ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)), ECP, and setup factors listed for `splitTime`.
- **Sources:** https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus, https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes

#### `gateIndex` and `splitIndex` (count)

This block has these fields:

- **What it measures:** which gate was broken (`gateIndex`) and which split in the rep this is (`splitIndex`).
- **Calculation:** Not published. Whether the indexes start at 0 or 1 is Not published. In the app each gate gets a letter in layout order ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). Dash gates use ID 0 for the start gate, then 1, 2, 3 ([source](https://support.vald.com/hc/en-au/articles/4996910107289-SmartSpeed-Dash-Set-up-your-timing-gates)). How either maps to `gateIndex` is Not published.
- **Inputs and units:** integers ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** in free timing, lap, serpentine, and grid drills the same gate can be broken more than once ([source](https://support.vald.com/hc/en-au/articles/4997399394201-SmartSpeed-Drill-Free-Timing), [source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)), so `gateIndex` can repeat while `splitIndex` advances. Restated from the drill rules; the API behavior is Not published.
- **What changes the number:** the gate order you confirm in **Review gates layout** ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)).
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `goalSplitTime` and `goalCumulativeTime` (unit Not published)

This block has these fields:

- **What it measures:** a target time for the split and for the cumulative time, stored in `additionalSplitData`.
- **Calculation:** Not published. Pacing drills on Pro set a "Pace in seconds" ([source](https://support.vald.com/hc/en-au/articles/4997515544217-SmartSpeed-Drill-Pacing)). Whether these fields hold that pace is Not published.
- **Inputs and units:** nullable floats ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** none.
- **What changes the number:** drill configuration. Not published in detail.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `totalOne`, `totalOneToTwo`, `totalOneToThree`, `totalOneToFour`, `totalThreeToFour` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The names suggest totals across segments one, one to two, one to three, one to four, and three to four.
- **Calculation:** Not published.
- **Inputs and units:** nullable floats in `additionalTestResult` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** compare with summary `cumulativeOne` to `cumulativeFour`. Whether they match is Not published.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `heightM` and `weightKg` in `additionalTestResult` (m and kg, by field name)

This block has these fields:

- **What it measures:** athlete height and body mass attached to the test. Not published by VALD.
- **Calculation:** none. Source of the values (profile or entered at test time) is Not published.
- **Inputs and units:** nullable floats. Units come from the field names only ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** `weightKg` also appears in `additionalOptionsFields` on the summaries (see Jumping).
- **What changes the number:** profile data. Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

### Sprint and split drills: summaries

These fields come from `GET /v1/team/{teamId}/tests` and `GET /v1/test/tests-by-modified-date`, inside `runningSummaryFields` (with `velocityFields` and `gateSummaryFields`) and `additionalOptionsFields`. valdr returns them as flat columns ([source](https://github.com/cran/valdr/blob/master/R/utils.R)).

#### `totalTimeSeconds` (s)

This block has these fields:

- **What it measures:** total time of the trial.
- **Calculation:** Not published. VALD lists "Total time" in seconds as a SmartSpeed time metric ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). The API guide says summaries include the total test time ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)). Restated: start of timing to the final gate break. For lap timing the app shows lap times, total time, split time, and cumulative time ([source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)).
- **Inputs and units:** seconds by field name.
- **Variants:** compare with the last `cumulativeTime` in the detail endpoint. Equality is Not published.
- **What changes the number:** start type, ECP, gate setup, and reaction time inclusion (Not published).
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates, https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API

#### `bestSplitSeconds` (s)

This block has these fields:

- **What it measures:** the best split in the trial.
- **Calculation:** Not published. VALD lists "Best split" in seconds ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). Whether "best" means the shortest split time regardless of split distance is Not published.
- **Inputs and units:** seconds by field name.
- **Variants:** `splitAverageSeconds`.
- **What changes the number:** unequal split distances make the shortest time not the fastest segment. This is a property of the math, not a VALD statement.
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates

#### `splitAverageSeconds` (s)

This block has these fields:

- **What it measures:** the average split time in the trial.
- **Calculation:** Not published. VALD lists "Average split" in seconds ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)).
- **Inputs and units:** seconds by field name.
- **Variants:** `bestSplitSeconds`.
- **What changes the number:** number of gates and split distances.
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates

#### `splitOne`, `splitTwo`, `splitThree`, `splitFour` (s, assumed from Hub; API unit Not published)

This block has these fields:

- **What it measures:** the first four split times of the trial, in `gateSummaryFields`.
- **Calculation:** Not published. Release notes say the CSV export includes "4 splits" ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). Restated: same meaning as `splitTime` for splits 1 to 4. Drills with more than four splits need the detail endpoint.
- **Inputs and units:** nullable floats ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)). Null when the drill has fewer splits (inferred from nullability; Not published).
- **Variants:** `cumulativeOne` to `cumulativeFour`.
- **What changes the number:** same as `splitTime`.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json, https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes

#### `cumulativeOne`, `cumulativeTwo`, `cumulativeThree`, `cumulativeFour` (s, assumed from Hub; API unit Not published)

This block has these fields:

- **What it measures:** cumulative time at the first four timed gates.
- **Calculation:** Not published. Restated: same meaning as `cumulativeTime` for splits 1 to 4.
- **Inputs and units:** nullable floats.
- **Variants:** `splitOne` to `splitFour`.
- **What changes the number:** same as `cumulativeTime`.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `peakVelocityMetersPerSecond` (m/s)

This block has these fields:

- **What it measures:** the highest velocity in the trial.
- **Calculation:** Not published for this field. VALD lists "Peak velocity" as a SmartSpeed velocity metric ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). Peak Velocity became a VALD Hub metric for SmartSpeed drills on 2026-07-27 ([source](https://support.vald.com/hc/en-au/articles/60458037938585-VALD-Hub-Release-Notes-27-July-2026)). In one VALD study write-up, VALD says peak velocity was the highest velocity across the four 10 m intervals ([source](https://valdperformance.com/news/the-quadrant-of-boom-sprint-speed-and-hamstring-strength)). Restated for that study: peak velocity = max over splits of (split distance / split time). VALD does not say the API field uses this method.
- **Inputs and units:** split distances and split times. m/s by field name. The Hub unit setting changes Hub views, not the API field name ([source](https://support.vald.com/hc/en-au/articles/27432433786009-Customize-Unit-of-Measurement-in-VALD-Hub)).
- **Variants:** `meanVelocityMetersPerSecond`, FVP `maxVelocity` and `vMax`. Split velocity can show on the gate LED panels in sprint drills ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **What changes the number:** split distance accuracy, gate spacing (shorter splits give more local velocity, longer splits smooth it), and ECP. VALD encourages practitioners to use time as the primary metric, to avoid calculation error ([source](https://valdperformance.com/news/timing-gates-101)).
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates, https://support.vald.com/hc/en-au/articles/60458037938585-VALD-Hub-Release-Notes-27-July-2026, https://valdperformance.com/news/the-quadrant-of-boom-sprint-speed-and-hamstring-strength

#### `meanVelocityMetersPerSecond` (m/s)

This block has these fields:

- **What it measures:** the average velocity over the trial.
- **Calculation:** Not published for this field. VALD lists "Average velocity" ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). VALD's speed calculator gives the formula "Speed = Distance (between timing gates) / Time (in seconds)" ([source](https://valdhealth.com/calculators)). Restated: average speed = distance / time. Whether the field uses total `distance` / `totalTimeSeconds` is Not published.
- **Inputs and units:** distance and time. m/s by field name.
- **Variants:** `peakVelocityMetersPerSecond`.
- **What changes the number:** start type (an in-beam or reactive start adds time with little distance), split distance entry, and ECP.
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates, https://valdhealth.com/calculators

#### `distance` (unit Not published)

This block has these fields:

- **What it measures:** a drill distance in `velocityFields`.
- **Calculation:** Not published. Whether it is total distance or split distance is Not published. VALD lists "Total distance" and "Split distance" in m, yd, or ft as SmartSpeed metrics ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)). Drills can be set in metric or imperial distances ([source](https://support.vald.com/hc/en-au/articles/13761581849497-SmartSpeed-Drill-List)), and a Hub bug once showed yard drills under metric settings ([source](https://support.vald.com/hc/en-au/articles/29742770121241-VALD-Hub-Release-Notes)). Check the unit against the drill name before use.
- **Inputs and units:** float. The split distance you entered in the app or Hub ([source](https://support.vald.com/hc/en-au/articles/42843499827353-Edit-a-SmartSpeed-test)).
- **Variants:** none in the API. Per-gate distances are not in the API.
- **What changes the number:** drill configuration and Hub edits.
- **Sources:** https://valdperformance.com/news/buyers-guide-to-timing-gates, https://support.vald.com/hc/en-au/articles/42843499827353-Edit-a-SmartSpeed-test

#### `startType` (enum)

This block has these fields:

- **What it measures:** how timing started. Values `Standard`, `InBeam`, `TrafficLight`, `ReactiveStart` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Calculation:** none. See **How timing works** for when the clock starts for each value.
- **Inputs and units:** enum in `additionalOptionsFields`.
- **Variants:** a jump mat or SmartPad start is an in-beam/mat start in the app ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)). Which enum value stores a mat start is Not published.
- **What changes the number:** every timed field depends on it. Compare trials only within one start type.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint, https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing

#### `reactionTime` (unit Not published)

This block has these fields:

- **What it measures:** time from the start cue to the athlete breaking the first gate.
- **Calculation:** VALD says reaction time is captured between the gate flash and the first break of the first gate ([source](https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint)). Restated: `reactionTime` = time of first gate break − time of the go cue.
- **Inputs and units:** nullable float in `additionalTestResult`. Not in the summaries or valdr. The Hub CSV includes "reactive time" ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **Variants:** VALD says Reactive Pro Agility trains reaction time in addition to the time it takes to complete the drill ([source](https://support.vald.com/hc/en-au/articles/4997452301849-SmartSpeed-Drill-Reactive-Pro-Agility)).
- **What changes the number:** cue type (light, buzzer, or both) ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)), the random delay range, and distance from the athlete to the first gate. A bug before v1.6.2 (2023-11-01) did not randomise the reactive delay ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4997399222681-SmartSpeed-Drill-Traffic-Light-Sprint

#### `reactiveDelayEnabled`, `reactiveDelayMinimumInSeconds`, `reactiveDelayMaximumInSeconds` (boolean, s, s)

This block has these fields:

- **What it measures:** whether a random delay precedes the go cue, and its range.
- **Calculation:** VALD defines the minimum and maximum as the range of time delay before the start cue triggers ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)). The distribution inside the range is Not published.
- **Inputs and units:** seconds by field name, in `additionalOptionsFields`.
- **Variants:** the app also has a "Signal delay" for change of direction, serpentine, and grid cues ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). Which field stores that delay is Not published.
- **What changes the number:** drill setup only.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills

### Agility and cut drills

#### `direction` in `additionalOptionsFields` (enum) and `cutDirectionChoice` (enum)

This block has these fields:

- **What it measures:** `direction` is the configured change of direction: `Left`, `Right`, `Random`, or `Both`. `cutDirectionChoice` is `Random` or `Fixed` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Calculation:** none. The app option reads "random, left, right, or both" ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). Cut drill options are "Random Direction" and "Fixed Direction" ([source](https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills)).
- **Inputs and units:** enums.
- **Variants:** planned direction can be overridden during testing ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **What changes the number:** random cues add decision time. VALD separates change of direction (a pre-planned movement) from agility (a movement in reaction to a stimulus) ([source](https://valdperformance.com/news/timing-gates-101)). Compare planned and reactive trials separately.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997519064217-SmartSpeed-Drill-Cut-Drills, https://valdperformance.com/news/timing-gates-101

#### `direction` in `additionalTestResult` (string) and `expectedDirection` in `additionalSplitData` (integer)

This block has these fields:

- **What it measures:** the direction taken in the trial and the direction cued at a split. Not published by VALD.
- **Calculation:** none. VALD says the app shows the actual and expected direction in results ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). The string values and the integer encoding are Not published.
- **Inputs and units:** string; nullable integer.
- **Variants:** compare with the summary `direction` enum.
- **What changes the number:** cue setup.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `colour` and `splitType` in `additionalSplitData` (string)

This block has these fields:

- **What it measures:** `colour` is likely the signal colour shown at the gate. `splitType` is Not published.
- **Calculation:** none. Serpentine live results show "signal colours (Sig)" per split, from red, green, blue, or all/white ([source](https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine)). The link to `colour` is a name match only.
- **Inputs and units:** nullable strings.
- **Variants:** none.
- **What changes the number:** drill cue settings.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997398946073-SmartSpeed-Drill-Serpentine

### Interval and pacing drills

#### `restDuration` (unit Not published)

This block has these fields:

- **What it measures:** rest time for a rep in `repResults`. Not published by VALD.
- **Calculation:** Not published. VALD defines the interval types this way: Fixed Recovery sets a fixed amount of recovery time, and Fixed Duration sets a fixed amount of time to complete each rep, including recovery ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)). Fixed Duration countdown starts at the first gate. Fixed Recovery countdown starts when the athlete breaks the final gate ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)). Restated for Fixed Duration: rest = interval duration − rep time.
- **Inputs and units:** nullable float.
- **Variants:** `intervalType`, `durationInSeconds`.
- **What changes the number:** a bug before v1.18.0 (2024-12-10) calculated Fixed Duration recovery times wrongly ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol

#### `intervalType` (enum)

This block has these fields:

- **What it measures:** `FixedDuration` or `FixedRecovery`.
- **Calculation:** VALD says that with Fixed Duration the rest period is included in the interval, and that Fixed Recovery starts when the athlete finishes one interval ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)).
- **Inputs and units:** enum in `additionalOptionsFields`.
- **Variants:** each rep after the first can start from either end ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)).
- **What changes the number:** shorter recovery raises fatigue across reps.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol

#### `testStandardType`, `events`, `durationInSeconds` (enum, count, s)

This block has these fields:

- **What it measures:** how a trial ends. `TestStandardType` values: `Standard`, `Free`, `Events`, `Duration` ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Calculation:** none. VALD defines Events as the number of times the athlete breaks a beam for the drill ([source](https://support.vald.com/hc/en-au/articles/4997515544217-SmartSpeed-Drill-Pacing)). VALD defines Duration as the amount of time the athlete has to run through the drill ([source](https://support.vald.com/hc/en-au/articles/4997399394201-SmartSpeed-Drill-Free-Timing)). The app's test mode offers "free, reps, or time-based" ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)). The exact match of app modes to enum values is Not published.
- **Inputs and units:** nullable integer; seconds by field name.
- **Variants:** grid drills use breaks or duration ([source](https://support.vald.com/hc/en-au/articles/4997511951641-SmartSpeed-Drill-Grid)). Duration-based jumps and free timing exist ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **What changes the number:** compare duration trials by count of breaks; compare event trials by time.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997399394201-SmartSpeed-Drill-Free-Timing, https://support.vald.com/hc/en-au/articles/4997515544217-SmartSpeed-Drill-Pacing

### Lap timing

#### `lapCount` (count)

This block has these fields:

- **What it measures:** number of laps set for the trial.
- **Calculation:** none. VALD says the field holds the number of laps to complete in each trial, and that you must set at least 1 lap ([source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)).
- **Inputs and units:** nullable integer in `additionalOptionsFields`.
- **Variants:** lap times appear as splits. Restated: with one gate, each lap is one split. With more gates, the app also shows split and cumulative time ([source](https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing)). API behavior is Not published.
- **What changes the number:** course length, which is not stored.
- **Sources:** https://support.vald.com/hc/en-au/articles/4997485634841-SmartSpeed-Drill-Lap-Timing

### FVP sprint

These fields live in `runningSummaryFields.velocityFields.fvpSummaryDto`. VALD publishes no definition, unit, or method for any of them. The `FvpSprint` drill does not run in the SmartSpeed Plus app ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). VALD mentions force-velocity profiling sprint testing with SmartSpeed ([source](https://valdperformance.com/news/balancing-kinetics-and-kinematics-in-nfl-and-nba-training)) and lists "Force-velocity profiles" as an assessment example ([source](https://valdperformance.com/news/buyers-guide-to-timing-gates)), without a method. The field names resemble terms from published sprint force-velocity profiling research. Do not assume VALD uses that method. The fields are non-nullable in the spec, so non-FVP tests may return 0 (Not published).

#### `maxVelocity` and `vMax` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The names suggest a measured maximum velocity and a modelled maximum velocity.
- **Calculation:** Not published.
- **Inputs and units:** floats ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** `peakVelocityMetersPerSecond`.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `maxForce` and `maxForceNormalised` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The names suggest maximum horizontal force and force normalised to body mass.
- **Calculation:** Not published. The body mass source is Not published (see `weightKg`).
- **Inputs and units:** floats.
- **Variants:** absolute versus normalised.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `maxPower` and `maxPowerNormalised` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The names suggest maximum power and power normalised to body mass.
- **Calculation:** Not published.
- **Inputs and units:** floats.
- **Variants:** absolute versus normalised.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `forceVelocityCurve` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The name suggests the slope of the force-velocity relationship.
- **Calculation:** Not published.
- **Inputs and units:** a single float, not an array ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** none.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `drf` and `rfMax` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The names suggest the decrease in ratio of force and the maximum ratio of force.
- **Calculation:** Not published.
- **Inputs and units:** floats.
- **Variants:** none.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

#### `tau` (unit Not published)

This block has these fields:

- **What it measures:** Not published. The name suggests the time constant of a velocity-time model.
- **Calculation:** Not published.
- **Inputs and units:** float.
- **Variants:** none.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

### Jumping (SmartJump mat)

Summary values sit in `jumpingSummaryFields`. Per-jump values sit in the detail `repResults[].jumpResults[]`. The mat plugs into a timing unit and needs no calibration ([source](https://support.vald.com/hc/en-au/articles/4996450791321-Portable-Jump-Mat-SmartJump)). Hub shows contact time, flight time, jump height, flight time / contact time, RSI, peak power output / total mass, leg stiffness, impulse, and flight time + contact time. The app also shows average contact time, average flight time, and jump count ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).

**Mat sensitivity applies to every jump field.** VALD says the mat ignores flight times under 100 ms by default ([source](https://support.vald.com/hc/en-au/articles/4813503104793-SmartJump-Mat-Sensitivity)). Lower sensitivity helps on soft ground. Higher sensitivity helps rapid jumps or ball triggers. VALD states that changing the sensitivity does not alter the accuracy of the data ([source](https://support.vald.com/hc/en-au/articles/4813503104793-SmartJump-Mat-Sensitivity)). The sensitivity value is not in the API.

#### `contactTime` (JumpResult) and `contactTimeSeconds` (summary) (Hub: ms; summary: s by name; detail: unit Not published)

This block has these fields:

- **What it measures:** time on the mat between jumps.
- **Calculation:** VALD defines contact time as the time, in milliseconds, that an athlete spends in contact with the mat between consecutive jumps ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- **Inputs and units:** mat contact events. Hub and app use ms. The summary field name says seconds ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- **Variants:** per jump in `jumpResults[]` with `jumpIndex` and `splitCompleteDate`. Summary aggregate method (mean, best, or last) is Not published. App shows "Average contact time" ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- **What changes the number:** mat sensitivity, mat on soft ground ([source](https://support.vald.com/hc/en-au/articles/4813503104793-SmartJump-Mat-Sensitivity)), and drill type (single jumps have no contact between jumps).
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `flightTime` (JumpResult) and `flightTimeSeconds` (summary) (Hub: ms; summary: s by name; detail: unit Not published)

This block has these fields:

- **What it measures:** time in the air for a jump.
- **Calculation:** VALD defines flight time as the time, in milliseconds, that an athlete spends in the air during a jump ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- **Inputs and units:** mat take-off and landing events.
- **Variants:** per jump and summary. App shows "Average flight time".
- **What changes the number:** flight times under the sensitivity threshold (default 100 ms) are ignored ([source](https://support.vald.com/hc/en-au/articles/4813503104793-SmartJump-Mat-Sensitivity)). Landing with bent knees or tucked legs lengthens flight time; VALD does not discuss this for SmartJump.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `heightMeters` (m)

This block has these fields:

- **What it measures:** jump height.
- **Calculation:** VALD defines jump height as the height an athlete jumped, shown in centimetres or inches ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). The formula from flight time is Not published.
- **Inputs and units:** Hub shows cm or in. API field name says metres.
- **Variants:** none.
- **What changes the number:** flight time and landing technique.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `rsi` (unit Not published)

This block has these fields:

- **What it measures:** reactive strength.
- **Calculation:** VALD defines the Reactive Strength Index (RSI) as the jump height divided by the contact time ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). Restated: `rsi` = jump height / contact time. Units of the inputs (m and s, or cm and ms) are Not published.
- **Inputs and units:** `heightMeters` and `contactTimeSeconds`.
- **Variants:** VALD's general definition describes RSI as jump height relative to contact time ([source](https://valdperformance.com/news/defining-reactive-strength)).
- **What changes the number:** VALD fixed a bug in v1.18.1, 2025-01-16, where RSI values were reported incorrectly in VALD Hub Results Export and the External API ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). Treat older `rsi` values with care. Drop height and the cue to minimise contact also change RSI ([source](https://valdperformance.com/news/defining-reactive-strength)).
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics, https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes

#### `flightTimeOverContractionTime` (ratio)

This block has these fields:

- **What it measures:** flight time relative to ground time.
- **Calculation:** VALD defines the Hub metric "Flight time / Contact time" as the flight time divided by the contact time ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). Restated: flight time / contact time. The API name says "contraction time"; the KB says "contact time". VALD does not explain the difference. Treat them as the same input unless VALD says otherwise.
- **Inputs and units:** flight time and contact time. Unitless if both use the same unit.
- **Variants:** `flightTimePlusContractionTime`.
- **What changes the number:** mat sensitivity.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `flightTimePlusContractionTime` (unit Not published)

This block has these fields:

- **What it measures:** one jump cycle: ground time plus air time.
- **Calculation:** Hub lists "Flight time + Contact time" ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). Restated: flight time + contact time. Same contact versus contraction naming gap as above.
- **Inputs and units:** flight time and contact time.
- **Variants:** `flightTimeOverContractionTime`.
- **What changes the number:** mat sensitivity.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `peakPowerOutput` (unit Not published)

This block has these fields:

- **What it measures:** peak power of the jump.
- **Calculation:** VALD defines Peak Power Output (PPO) as the maximum output of the jump ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). The equation is Not published.
- **Inputs and units:** Not published. A mat measures only times, so body mass must come from elsewhere (see `weightKg`). Not published.
- **Variants:** `peakPowerOutputOverTotalMass`.
- **What changes the number:** body mass entry (Not published).
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `peakPowerOutputOverTotalMass` (unit Not published)

This block has these fields:

- **What it measures:** peak power relative to mass.
- **Calculation:** VALD defines it as the mat output divided by the total mass ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). Restated: `peakPowerOutput` / total mass. What "total mass" includes is Not published.
- **Inputs and units:** Not published.
- **Variants:** `peakPowerOutput`.
- **What changes the number:** mass entry.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `legStiffness` (unit Not published)

This block has these fields:

- **What it measures:** VALD describes leg stiffness as a measure of how the lower limb muscles and joints interact to produce a jump ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- **Calculation:** Not published.
- **Inputs and units:** Not published.
- **Variants:** none.
- **What changes the number:** Not published.
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `impulse` (N·s)

This block has these fields:

- **What it measures:** take-off impulse.
- **Calculation:** VALD defines impulse as the product of the athlete's force and time during the take-off phase of a jump, in Newton-seconds (Ns) ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)). How force is estimated from a mat is Not published.
- **Inputs and units:** N·s.
- **Variants:** none.
- **What changes the number:** body mass entry (Not published).
- **Sources:** https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics

#### `dropHeight` and `dropHeightEnabled` (unit Not published, boolean)

This block has these fields:

- **What it measures:** box height for a drop jump.
- **Calculation:** none. VALD describes the field as the designated box height for a drop jump drill ([source](https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus)).
- **Inputs and units:** nullable float and boolean in `additionalOptionsFields`.
- **Variants:** none.
- **What changes the number:** set by the coach. Compare RSI only at the same drop height.
- **Sources:** https://support.vald.com/hc/en-au/articles/16465986124953-Set-up-and-run-a-drill-with-SmartSpeed-Plus

#### `weightKg` in `additionalOptionsFields` (kg, by field name)

This block has these fields:

- **What it measures:** a mass setting for the test. Not published by VALD.
- **Calculation:** none. Whether power, impulse, and FVP normalisation use it is Not published.
- **Inputs and units:** nullable float.
- **Variants:** `weightKg` in the detail `additionalTestResult`.
- **What changes the number:** Not published.
- **Sources:** https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json

### Trial quality

#### `isValid` (summary, boolean) and `tag` (detail, enum `Valid` or `Invalid`)

This block has these fields:

- **What it measures:** the coach's valid or invalid tag for the trial.
- **Calculation:** none. VALD describes the field as the flag for the valid or invalid tag applied to a test ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)). You enable **Trial validity** in drill setup with a tagging window in 5 s steps. If the window lapses with no tap, the trial is marked valid ([source](https://support.vald.com/hc/en-au/articles/28173187417369-Enable-trial-validity-in-the-SmartSpeed-Plus-app)). Invalid trials still upload to Hub ([source](https://support.vald.com/hc/en-au/articles/28173187417369-Enable-trial-validity-in-the-SmartSpeed-Plus-app)).
- **Inputs and units:** boolean; enum `TestTag`.
- **Variants:** for interval drills the tag applies to the whole trial, not each rep ([source](https://support.vald.com/hc/en-au/articles/4997399170329-SmartSpeed-Drill-Interval-Protocol)).
- **What changes the number:** a bug before v1.18.0 did not pass trial validity settings from Hub to the app ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)). Filter out `isValid == false` before analysis.
- **Sources:** https://support.vald.com/hc/en-au/articles/28173187417369-Enable-trial-validity-in-the-SmartSpeed-Plus-app

### Derived metrics VALD publishes

These are not export fields. VALD education pages show how to compute them from SmartSpeed times.

#### Split speed (m/s or km/h)

This block has these fields:

- **What it measures:** average speed between two gates.
- **Calculation:** VALD's speed calculator gives the formula "Speed = Distance (between timing gates) / Time (in seconds)" ([source](https://valdhealth.com/calculators)). Restated: v = d / t, where d is the gate-to-gate distance and t is `splitTime`. The calculator shows km/h and m/s. Restated: km/h = m/s × 3.6.
- **Inputs and units:** your measured gate distance; `splitTime` in s.
- **Variants:** split velocity can display on Plus gates ([source](https://support.vald.com/hc/en-au/articles/29730735766553-SmartSpeed-Plus-iOS-Release-Notes)).
- **What changes the number:** distance errors pass straight into speed ([source](https://valdperformance.com/news/timing-gates-101)).
- **Sources:** https://valdhealth.com/calculators

#### 10 m sprint momentum (kg·m/s)

This block has these fields:

- **What it measures:** momentum over the first 10 m.
- **Calculation:** VALD's steps are to calculate the 10 m velocity (10 m / sprint time), then multiply it by body mass: "10m velocity [m/s] x body mass [kg]" ([source](https://valdperformance.com/news/quadrant-of-boom-part-2-sprint-momentum-and-hamstring-strength)). The 10 m time is the initial 10 m split of a 40 m sprint test ([source](https://valdperformance.com/news/quadrant-of-boom-part-2-sprint-momentum-and-hamstring-strength)).
- **Inputs and units:** first split time (s) with gates at 0 m and 10 m; body mass (kg).
- **Variants:** none.
- **What changes the number:** start type and lead-in distance.
- **Sources:** https://valdperformance.com/news/quadrant-of-boom-part-2-sprint-momentum-and-hamstring-strength, https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/QoB_2.pdf

#### Curved sprint deceleration (CSD) deficit (%)

This block has these fields:

- **What it measures:** time lost when an athlete must stop at the end of a curved sprint.
- **Calculation:** the VALD cheat sheet gives CSD Deficit = ((Time with stop × 100) / (Time without stop)) − 100 ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/CSD_Deficit.pdf)). The course is a 17 m sprint on the penalty arc with a 1 m × 1 m stop box ([source](https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates)). Preliminary elite soccer benchmarks: 10% to 20% good, 20% to 25% normal, above 25% poor ([source](https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates)).
- **Inputs and units:** two trial times in s.
- **Variants:** clockwise and counterclockwise runs ([source](https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates)).
- **What changes the number:** braking strategy and approach speed.
- **Sources:** https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/CSD_Deficit.pdf, https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates

#### Curved acceleration-deceleration ability, average deceleration (m/s²)

This block has these fields:

- **What it measures:** average braking rate after a curved sprint.
- **Calculation:** VALD gives the formula "a = -(vi²) / (2 x d)", where vi is approach velocity (m/s) and d is stopping distance (m) ([source](https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates)). Approach velocity comes from gates 1 m apart at the 16 m line. Stopping distance is taped from the final gate to the heel. VALD advises excluding trials where approach velocity is more than 10% below maximum effort.
- **Inputs and units:** approach velocity = 1 m / split time; stopping distance in m.
- **Variants:** none.
- **What changes the number:** early braking ([source](https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates)).
- **Sources:** https://valdperformance.com/news/testing-curvilinear-sprints-and-decelerations-with-smartspeed-timing-gates

### Identifiers and context fields

The table below covers `GET /v1/team/{teamId}/tests` (`GetTestSummariesHttpResponse`). The descriptions paraphrase the KB API guide ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)).

| Field | Type | Meaning |
|---|---|---|
| `id` | uuid | The unique identifier for the test. Use as `testId` for the detail endpoint. |
| `testResultId` | uuid | An alternative unique identifier for the test. The guide says it is reserved for use in future versions. |
| `profileId` | uuid | The athlete. |
| `groupUnderTestId` | uuid, nullable | The group that was selected when the test was performed. |
| `testDateUtc` | date-time | Test date in UTC. |
| `deviceCount` | int | The number of devices used for the test (for example, 4 gates). |
| `repCount` | int | The number of reps in the test. |
| `testTypeName` | `TestTypeName` | An enum for the high-level type of the test. |
| `testName` | string | The name of the test type. For example a drill name. |
| `isValid` | boolean | See Trial quality. |
| `allGroups` | string array | The unique group identifiers that the athlete belonged to at the time of testing. |

The table below lists the fields that `GET /v1/test/tests-by-modified-date` (`TestCursorHttpResponse.summaries[]`) adds to the fields above ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)):

| Field | Type | Meaning |
|---|---|---|
| `testSessionId` | uuid | The session. Matches `sessionId` in the detail endpoint (by name; Not published). |
| `modifiedDateUtc` | date-time | Last change. valdr uses the last value to page ([source](https://github.com/cran/valdr/blob/master/R/smartspeed_tests.R)). |
| `trialNumber` | int | Trial number in the session. Not described by VALD. |

The table below covers `GET /v1/team/{teamId}/tests/{testId}/detail` (`GetTestDetailHttpResponse`) ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API)):

| Field | Type | Meaning |
|---|---|---|
| `sessionId` | uuid | The unique identifier for the testing session that the test was performed within. |
| `profileId` | uuid | The athlete. |
| `groupUnderTestId` | uuid, nullable | Group selected at test time. |
| `testDateUtc` | date-time | Test date in UTC. |
| `trialIndex` | int | The number of the test within the testing session. Base (0 or 1) Not published. |
| `tag` | `TestTag` | The "Valid" or "Invalid" tag. |
| `repResults[].repIndex` | int | Rep number. Base Not published. |
| `repResults[].splitResults[].splitCompleteDate` | date-time | When the split finished. |
| `repResults[].jumpResults[].jumpIndex` | int | Jump number. |
| `repResults[].jumpResults[].splitCompleteDate` | date-time | When the jump finished. |

### Enums

The table below lists each enum with its values and its source:

| Enum | Values | Source |
|---|---|---|
| `StartType` | `Standard`, `InBeam`, `TrafficLight`, `ReactiveStart` | ([source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)) |
| `Direction` | `Left`, `Right`, `Random`, `Both` | same |
| `CutChoice` | `Random`, `Fixed` | same |
| `IntervalType` | `FixedDuration`, `FixedRecovery` | same |
| `TestStandardType` | `Standard`, `Free`, `Events`, `Duration` | same |
| `TestTag` | `Valid`, `Invalid` | same |
| `TestTypeName` | `TrafficLightSprint`, `Cut`, `Free`, `LapTiming`, `Serpentine`, `IntervalShuttle`, `Grid`, `IntervalProtocol`, `Pacing`, `ReactiveProAgility`, `TrafficLightStart_0121`, `AutoStart_112`, `TrafficLightStart_0123`, `TrafficLightStart_013`, `ProAgility`, `OneWay`, `FvpSprint`, `Jumping` | same |

### Source disagreements

VALD's own sources disagree in these places:

- The KB API guide lists query parameters in camelCase (`athleteId`, `page`) and marks `page` required. The spec uses PascalCase (`AthleteId`, `Page`) ([source](https://support.vald.com/hc/en-au/articles/38093151187865-A-guide-to-using-the-External-SmartSpeed-API), [source](https://prd-use-api-extsmartspeed.valdperformance.com/swagger/v1/swagger.json)).
- The KB says "Contact time" for SmartJump ratios. The spec says `flightTimeOverContractionTime` and `flightTimePlusContractionTime` ([source](https://support.vald.com/hc/en-au/articles/4813517571481-SmartJump-Metrics)).
- The KB lists SmartJump times in ms. The summary field names say seconds (`flightTimeSeconds`, `contactTimeSeconds`).
- Unit-to-reflector distance: 1 m to 2 m (Plus KB), about 2 m (Dash KB, Plus Quick Start Guide), 1 m to 4 m (Pro and Dash Quick Start Guides), 4 m maximum (Plus spec), 7 m maximum (Dash and Pro specs) ([source](https://support.vald.com/hc/en-au/articles/15854427158041-SmartSpeed-Plus-Set-up-your-timing-gates), [source](https://support.vald.com/hc/article_attachments/31800152349721), [source](https://support.vald.com/hc/en-au/article_attachments/62792691604889)).
- Dash gate-to-gate range: 60 m (Model Comparison), about 50 m (buyer's guide), 100 m (Dash spec sheet) ([source](https://support.vald.com/hc/en-au/articles/4996484198297-SmartSpeed-Model-Comparison), [source](https://valdperformance.com/news/buyers-guide-to-timing-gates), [source](https://support.vald.com/hc/en-au/article_attachments/62792687636121)).
- valdr renames nested fields to their last name part. `weightKg` in valdr output is `additionalOptionsFields.weightKg`, not the detail `additionalTestResult.weightKg` ([source](https://github.com/cran/valdr/blob/master/R/utils.R)).

### Marked Not published

The following items are marked Not published in this section:

- Calculation for `splitTime`, `cumulativeTime`, `totalTimeSeconds`, `bestSplitSeconds`, `splitAverageSeconds`, `splitOne` to `splitFour`, `cumulativeOne` to `cumulativeFour`, `peakVelocityMetersPerSecond`, `meanVelocityMetersPerSecond` (restatements given, VALD formula Not published).
- API units for `splitTime`, `cumulativeTime`, `reactionTime`, `restDuration`, `distance`, `goalSplitTime`, `goalCumulativeTime`, `contactTime`, `flightTime`, `dropHeight`, `rsi`, `peakPowerOutput`, `peakPowerOutputOverTotalMass`, `legStiffness`, `flightTimePlusContractionTime`.
- `distance` meaning (total or split).
- `gateIndex`, `splitIndex`, `trialIndex`, `repIndex` base and mapping to gates.
- `totalOne`, `totalOneToTwo`, `totalOneToThree`, `totalOneToFour`, `totalThreeToFour`: meaning and calculation.
- `heightM`, `weightKg` (both locations): source and use.
- `goalSplitTime`, `goalCumulativeTime`, `colour`, `splitType`, `expectedDirection`, detail `direction`: meaning and encoding.
- `restDuration` calculation.
- All FVP fields: `maxVelocity`, `vMax`, `maxForce`, `maxForceNormalised`, `maxPower`, `maxPowerNormalised`, `forceVelocityCurve`, `drf`, `rfMax`, `tau`.
- Jump height formula for `heightMeters`; `legStiffness` and `peakPowerOutput` calculations; how `impulse` force is estimated; summary jump aggregation method.
- Whether `splitTime` and `cumulativeTime` include reaction time for `TrafficLight` and `ReactiveStart`.
- Flying start run-in distance and any start offset.
- Numeric gate height.
- Which `StartType` value stores a mat start; mapping of app test modes to `TestStandardType`.
- Mapping of `TestTypeName` values to app drill names (name matches only); `TestTypeName` for Beep Test and VAM Eval Test.
- Hub CSV column list and row level; whether ECP was on for a test.

## Worked example

This example uses made-up values, not athlete data. It was run with Python 3.9 on 2026-10-02. The output below is copied from that run.

### SmartSpeed: splits, split speed, and start method

What the script does:

- Part 1 turns example gate break times into split times, cumulative times, and speed per split. Speed per split uses VALD's calculator formula, speed = distance between gates / time ([source](https://valdhealth.com/calculators)).
- Part 2 runs one simulated athlete through three start methods. The sprint speed curve is this example's assumption, not a VALD method. The 30 cm lead-in for a beam-break start comes from VALD ([source](https://valdperformance.com/news/timing-gates-101)). Whether exported splits include reaction time for `TrafficLight` and `ReactiveStart` is Not published, so the signal-start row shows the case where they do.

What the output shows:

- The start method changes the first split. Later splits barely change.
- A signal start that includes reaction time adds about the reaction time to split 1, plus the run-up the beam-break start gets for free.
- Compare first splits only between tests with the same `startType`.

```python
"""SmartSpeed worked example: splits, split speed, and start method.

All inputs are made-up example values, not athlete data.
VALD publishes no formula for split or cumulative time. This script uses the
plain reading: a split is the time between two consecutive gate breaks, and
cumulative time is the sum of splits up to that gate.
Split speed uses VALD's calculator formula: speed = distance between gates / time.
Source: https://valdhealth.com/calculators
"""
import math

# ---------------------------------------------------------------------------
# Part 1. Split times from gate times, then speed per split.
# ---------------------------------------------------------------------------
# Example 40 m sprint with five gates at 0, 10, 20, 30, and 40 m.
# gate_times_s holds the clock time (s) at which each gate beam broke.
gate_positions_m = [0.0, 10.0, 20.0, 30.0, 40.0]
gate_times_s = [0.000, 1.850, 3.050, 4.150, 5.230]

splits_s = [round(b - a, 3) for a, b in zip(gate_times_s, gate_times_s[1:])]
split_dist_m = [b - a for a, b in zip(gate_positions_m, gate_positions_m[1:])]
cumulative_s = []
running = 0.0
for s in splits_s:
    running = round(running + s, 3)
    cumulative_s.append(running)

print("Part 1. Splits and split speed (example gate times)")
print(f"{'split':>5} {'from-to (m)':>12} {'splitTime (s)':>14} {'cumulative (s)':>15} {'speed (m/s)':>12} {'speed (km/h)':>13}")
for i, (s, d, c) in enumerate(zip(splits_s, split_dist_m, cumulative_s), start=1):
    v = d / s
    print(f"{i:>5} {gate_positions_m[i-1]:>5.0f}-{gate_positions_m[i]:<6.0f} {s:>14.3f} {c:>15.3f} {v:>12.2f} {v*3.6:>13.2f}")

total_time = cumulative_s[-1]
best_split = min(splits_s)
mean_split = sum(splits_s) / len(splits_s)
mean_speed = (gate_positions_m[-1] - gate_positions_m[0]) / total_time
top_split_speed = max(d / s for d, s in zip(split_dist_m, splits_s))
print(f"Total time: {total_time:.3f} s")
print(f"Best split: {best_split:.3f} s")
print(f"Mean of splits: {mean_split:.4f} s")
print(f"Mean speed over 40 m (distance / total time): {mean_speed:.3f} m/s")
print(f"Fastest split speed (highest of the four 10 m splits): {top_split_speed:.3f} m/s")
print()

# ---------------------------------------------------------------------------
# Part 2. Effect of start method on the first split.
# ---------------------------------------------------------------------------
# One simulated athlete runs the same sprint three ways. Movement follows a
# mono-exponential speed curve, v(t) = vmax * (1 - exp(-t / tau)), a common
# sprint model. It is this example's assumption, not a VALD method.
VMAX = 9.0     # m/s, example value
TAU = 1.10     # s, example value
REACTION = 0.250  # s, example time from light to first movement
LEAD_IN = 0.30    # m, lead-in behind the start gate for a beam-break start
# 30 cm lead-in for break-beam starts: https://valdperformance.com/news/timing-gates-101


def position(t):
    """Distance run (m) t seconds after first movement."""
    return VMAX * (t - TAU * (1 - math.exp(-t / TAU)))


def time_at(x):
    """Seconds after first movement to reach x metres (bisection)."""
    lo, hi = 0.0, 30.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if position(mid) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


gates_from_line = [10.0, 20.0, 30.0, 40.0]  # gates after the start line

# a) Standard (beam break): athlete starts LEAD_IN behind the start gate.
#    The clock starts when the athlete breaks the start gate.
t0 = time_at(LEAD_IN)
std = [time_at(LEAD_IN + g) - t0 for g in gates_from_line]

# b) InBeam: the athlete starts in the beam and the clock starts on leaving it.
#    Modelled here as the clock starting at first movement.
inbeam = [time_at(g) for g in gates_from_line]

# c) TrafficLight or ReactiveStart: the clock starts at the signal, so the
#    first split carries the reaction time. VALD does not publish whether the
#    exported split includes reaction time; this models the case where it does.
light = [REACTION + time_at(g) for g in gates_from_line]


def to_splits(cum):
    out, prev = [], 0.0
    for c in cum:
        out.append(c - prev)
        prev = c
    return out


print("Part 2. Same simulated athlete, three start methods")
print(f"Model: vmax={VMAX} m/s, tau={TAU} s, reaction={REACTION} s, lead-in={LEAD_IN} m")
print(f"{'start method':<28} {'split 1':>8} {'split 2':>8} {'split 3':>8} {'split 4':>8} {'40 m total':>11}")
for name, cum in [("Standard (0.3 m lead-in)", std),
                  ("InBeam (clock at movement)", inbeam),
                  ("Signal start (+reaction)", light)]:
    sp = to_splits(cum)
    print(f"{name:<28} " + " ".join(f"{s:>8.3f}" for s in sp) + f" {cum[-1]:>11.3f}")

sp_std, sp_in, sp_light = to_splits(std), to_splits(inbeam), to_splits(light)
print()
print(f"First split, InBeam minus Standard: {sp_in[0] - sp_std[0]:+.3f} s")
print(f"First split, signal start minus Standard: {sp_light[0] - sp_std[0]:+.3f} s")
print(f"Split 4, largest difference across methods: "
      f"{max(sp_std[3], sp_in[3], sp_light[3]) - min(sp_std[3], sp_in[3], sp_light[3]):.4f} s")
print(f"First 10 m speed, Standard: {10 / sp_std[0]:.2f} m/s; signal start: {10 / sp_light[0]:.2f} m/s")
```

Output:

```text
Part 1. Splits and split speed (example gate times)
split  from-to (m)  splitTime (s)  cumulative (s)  speed (m/s)  speed (km/h)
    1     0-10              1.850           1.850         5.41         19.46
    2    10-20              1.200           3.050         8.33         30.00
    3    20-30              1.100           4.150         9.09         32.73
    4    30-40              1.080           5.230         9.26         33.33
Total time: 5.230 s
Best split: 1.080 s
Mean of splits: 1.3075 s
Mean speed over 40 m (distance / total time): 7.648 m/s
Fastest split speed (highest of the four 10 m splits): 9.259 m/s

Part 2. Same simulated athlete, three start methods
Model: vmax=9.0 m/s, tau=1.1 s, reaction=0.25 s, lead-in=0.3 m
start method                  split 1  split 2  split 3  split 4  40 m total
Standard (0.3 m lead-in)        1.796    1.223    1.147    1.123       5.288
InBeam (clock at movement)      2.039    1.227    1.148    1.124       5.537
Signal start (+reaction)        2.289    1.227    1.148    1.124       5.787

First split, InBeam minus Standard: +0.243 s
First split, signal start minus Standard: +0.493 s
Split 4, largest difference across methods: 0.0004 s
First 10 m speed, Standard: 5.57 m/s; signal start: 4.37 m/s
```

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
