# Hawkin Dynamics force plate data

Checked against: Hawkin Beta API Specification 1.12 (2026-03-23), the `hawkinR` R package 2.0.1, the `hdforce` Python package 2.1.0, the Hawkin metric database, and the Hawkin help center, on 2026-10-02.

This file describes the Hawkin Dynamics API output and export format, what each metric means, and how to transform the data for analysis. Hawkin Dynamics and TruStrength are trademarks of their owner. This repository is not affiliated with or endorsed by Hawkin Dynamics.

## Get the data

Use one of these four routes:

- Web export: in the Hawkin Cloud, open the **Tests** tab, select a team, group, or athlete, set a custom **Date Range**, and select **Export**. Without a date range the export holds only the 100 most recent tests. Choose an **Export Type**: **Tests** gives one row per trial, **Averages** gives one row per athlete per day, and **Averages & Tests** gives both. A session is one day. Select **Include Inactive Metrics** to export every metric; otherwise only active metrics export. **Deidentify Data** replaces names with a 20-digit code. A single test can also be exported as raw force, velocity, or power at 1000 rows per second (Hawkin help, exporting data).
- API: only the organization administrator can create an API token, in the Hawkin Cloud under **Settings**, then **Integrations** (Hawkin help, API token). The token is a refresh token. Send it as `Authorization: Bearer <refresh token>` to `GET <base>/token` to get an `access_token`, then send the `access_token` as a bearer token on every call (API specification 1.12).
- R: the `hawkinR` package, published by Hawkin on CRAN. Store the token with `hd_auth_store()`, connect with `hd_connect(region = "Americas")`, and pull trials with `get_tests()`.
- Python: the `hdforce` package, published by Hawkin on PyPI. Connect with `AuthManager(region="Americas", authMethod="env")` and pull trials with `GetTests()`.

The API base URL depends on where your organization's data lives (API specification 1.12):

| Region | Base URL | `hawkinR` `region` | `hdforce` `region` |
|---|---|---|---|
| Americas | `https://cloud.hawkindynamics.com/api` | `"Americas"` | `"Americas"` |
| Europe | `https://eu.cloud.hawkindynamics.com/api` | `"Europe"` | `"Europe"` |
| Asia/Pacific | `https://apac.cloud.hawkindynamics.com/api` | `"APAC"` or `"Asia/Pacific"` | `"Asia/Pacific"` |

Data calls go to `<base>/v1`. Both packages let you replace `v1` with an organization-specific path, set with `org_id` in `hawkinR` or `orgName` in `hdforce`. Use `v1` unless Hawkin gives you another path. Check your cloud web address to confirm the region.

Each package wraps the same endpoints with these functions:

| Task | `hawkinR` 2.0.1 | `hdforce` 2.1.0 |
|---|---|---|
| Store the refresh token | `hd_auth_store(profile)`, OS keychain; or environment variable `HAWKIN_KEY_<PROFILE>` with `environment = "production"` | `AuthManager(authMethod = "env", "file", "manual", or "keyring")`; default variable `HD_REFRESH_TOKEN` |
| Connect | `hd_connect(profile, org_id = "v1", region)` | `AuthManager(region, orgName)` |
| Trials with metrics | `get_tests(from, to, sync, athleteId, typeId, teamId, groupId, includeInactive, includeEid)` | `GetTests(from_, to_, sync, athleteId, typeId, teamId, groupId, includeInactive, includeEid, useNulls, rounding, nestMetrics)` |
| Athletes | `get_athletes(includeInactive)` | `GetAthletes(includeInactive)` |
| Teams, groups, tags | `get_teams()`, `get_groups()`, `get_tags()` | `GetTeams()`, `GetGroups()`, `GetTags()` |
| Test types | `get_testTypes()` | `GetTypes()` |
| Metric list | `get_metrics(testType)` | `GetMetrics(test_type)` |
| Raw force trace | `get_forcetime(testId)`, `get_forcetime_bulk()` | `GetForceTime(testId)`, `GetForceTimeBulk()` |
| Center of pressure, free run only | `get_cop(testId)` | `GetCOP(testId)` |

`get_metrics()` and `GetMetrics()` do not call the API. Both read a `MetricDictionary` table shipped inside the package. It has one row per test type and metric. Its columns are `canonicalTestTypeId`, `testTypeName`, `id`, `label`, `label_unit` (the API column name), `units`, `description`, and `header` (the `hawkinR` column name). The shipped table has 472 rows: 454 unique metrics, one `active` row per test type, and the TruStrength free run listed twice. It lists no metrics for the force plate free run.

Times are Unix timestamps in seconds. The API does not return a time zone or offset (API specification 1.12). `hawkinR` converts force-trace times with the computer's time zone; `hdforce` converts them as UTC.

## API output

The API returns trials. Each trial carries its athlete, its test type, and its metrics as flat fields.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET <base>/token` | A bearer token for API calls | `access_token`, `token_type`, `expires_at` (Unix seconds) |
| `GET <base>/v1` | Trials that match the query | `data[]`: `id`, `timestamp`, `segment`, `testType`, `athlete`, one field per metric; envelope `count`, `lastTestTime`, `lastSyncTime`, `nextCursor` |
| `GET <base>/v1/athletes` | Athletes | `id`, `name`, `active`, `teams`, `groups`, `external`; with API 1.14 also `image`, `position`, `dob`, `sport`, `height`, `lastTestedOn` |
| `GET <base>/v1/forcetime/{testId}` | The raw trace for one trial | `Time(s)`, `LeftForce(N)`, `RightForce(N)`, `CombinedForce(N)`, `Velocity(m/s)`, `Displacement(m)`, `Power(W)`, `rsi`; some trials also carry tri-axial `X` and `Y` plate forces and moments |
| `GET <base>/v1/cop/{testId}` | Center of pressure for one free run trial | `copX`, `copY`, `leftCopX`, `leftCopY`, `rightCopX`, `rightCopY`, in mm from the plate center |
| `GET <base>/v1/teams`, `/groups`, `/tags`, `/test_types` | Lookup lists | `id`, `name`; tags also `description` |
| `GET <base>/v1/metrics` | Metrics per test type | `canonicalTestTypeId`, `testType`, `metrics[]` with `id`, `label`, `units`, `description` |

Each trial in `data[]` has these parts:

- `id`: the trial ID. Use it to fetch the raw trace.
- `timestamp`: the trial time in Unix seconds.
- `segment`: the test type and the trial number in the session, for example `"Countermovement Jump:5"`.
- `testType`: `id`, `name`, `canonicalId`, and `tags[]` with `id`, `name`, and `description`. Filter on `canonicalId`, the test type ID that both packages use.
- `athlete`: `id`, `name`, `teams`, `groups`, `active`, and `external` custom properties.
- One field per metric, named with the label and unit, for example `"Jump Height(m)"` or `"L|R Avg. Braking Force(%)"`.
- `active`: false for a disabled trial. Hawkin no longer deletes trials; it disables them (Hawkin help, disabled tests). The API leaves this field out when you exclude inactive trials. `hdforce` then fills it with true; `hawkinR` leaves the column out.

Query the trials endpoint with these parameters:

- `from` and `to`: Unix timestamps for the trial time. Use them for history.
- `syncFrom` and `syncTo`: Unix timestamps for when trials changed. Send the last `lastSyncTime` you received as the next `syncFrom` to pick up new and edited trials.
- One of `athleteId`, `testTypeId`, `teamId`, or `groupId`. Team and group IDs accept a comma-separated list of up to 10. The API specification says each filter works only with `from` and `to`, and `hdforce` refuses more than one.
- `paginate=true` and `cursor`: cursor paging from API 1.13. Each page holds up to 1000 trials. Repeat with `nextCursor` until it is missing.
- `includeInactive`: both packages send `false` by default. A comment in Hawkin's Power Query free run script states that the API itself defaults to including inactive trials.
- `includeEid=true`: adds an `eid` equipment ID to each trial.
- `useNulls`, `rounding`, `nestMetrics` (API 1.16): `nestMetrics=true` returns a `metrics[]` list per trial with `metricId`, `metricLabel`, `metricUnits`, and `metricValue`. `useNulls=false` returns `"N/A"` text for metrics that cannot be calculated instead of null.

Metrics can be added at any time, and a trial may lack a metric that could not be calculated (API specification 1.12). The `hdforce` README gives a 256 MB limit per response, so pull long histories month by month.

## Export columns

Hawkin does not publish the column list for the Hawkin Cloud CSV export. The help center confirms these points:

- **Tests** exports one row per trial with each metric in a column. **Averages** exports one row per athlete and date. **Averages & Tests** adds the average row under the trials.
- You choose the date format at export.
- The single-test raw force export has four columns: time, left force, right force, and combined force, at 1000 rows per second.

The package tables are better documented. These are the columns from `get_tests()` and `GetTests()`:

| Column name | Meaning | Units |
|---|---|---|
| `id` | Trial ID | Text |
| `timestamp` | Trial time | Unix seconds |
| `segment` | Test type and trial number in the session | Text |
| `testType_name`, `testType_canonicalId` | Test type name and canonical ID | Text |
| `testType_tags_name` (`hawkinR`), `tag_names` (`hdforce`) | Tags, such as `Arm Swing` or `SL Left` | List of text |
| `athlete_id`, `athlete_name`, `athlete_teams`, `athlete_groups`, `athlete_active` | Athlete fields | Text, list, logical |
| `athlete_<key>` (`hawkinR`), `external_<key>` (`hdforce`) | Custom athlete properties, such as an AMS ID | Text |
| `active` | False for a disabled trial. Present only when inactive trials are included, or always in `hdforce` | Logical |
| `last_test_time`, `last_sync_time` (`hawkinR`); `last_sync_time` column and `attrs` values (`hdforce`) | Envelope values from the API | Unix seconds |
| `eid` | Equipment ID, with `includeEid` | Text |
| One column per metric | The metric value | Unit in the column name |

Metric column names differ between the packages. `hawkinR` turns `L|R Avg. Braking Force(%)` into `l_r_avg_braking_force_percent`. `hdforce` calls pyjanitor `clean_names(remove_special=True)` and strips trailing underscores. Applying those rules to the same label gives `lr_avg_braking_force`, which drops the `%`. Check both against your own output. The `header` column of the `MetricDictionary` lists the `hawkinR` names.

Exports vary. Check each file for these differences:

- Imperial units. The cloud can show imperial units under **Settings**, then **Metric Settings** (Hawkin help, imperial units). Whether this changes exports is not confirmed.
- Inactive metrics missing from the file.
- Several test types in one file. Each test type has its own columns.
- Averages rows mixed with trial rows.

## Metric meanings

The definitions below come from the `MetricDictionary` in `hawkinR` and `hdforce`, the Hawkin metric database, and Hawkin's blog. Hawkin finds the start of a CMJ when force falls 5 standard deviations of the weighing force below system weight, then traces back to the last sample at system weight and integrates from zero velocity (Hawkin blogs, phases of the CMJ and two key factors). Merrigan et al. (2022) report take-off as force below 25 N for 30 ms.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `Jump Height(m)` (CMJ, squat jump, drop jump), `CMJ Jump Height(m)` and `Rebound Jump Height(m)` (CMJ rebound) | Rise of the center of mass after take-off | Take-off velocity squared divided by 2 × 9.81 | m | `cmj-jump-height.md` in the `force-plate` skill | Matches the takeoff velocity method. Integration starts at the traced-back start of movement, not at the start of quiet standing. Drop jump start velocity comes from drop height, found by reverse integration, then flight time, then box height; an automatic tag names the method. |
| `Takeoff Velocity(m/s)` | Center of mass velocity at take-off | Net force divided by system mass, summed sample by sample from the start of movement | m/s | `cmj-jump-height.md` in the `force-plate` skill | Body weight is `System Weight`, the lowest 1 s average found by an optimization loop, not the mean of the first 1 s |
| `Flight Time(s)` | Time in the air | Take-off to touchdown | s | `cmj-jump-height.md` in the `force-plate` skill | Hawkin does not turn it into a jump height for these tests. CMJ rebound `Rebound Flight Time` is in ms. |
| `Avg. Jump Height(m)`, `Peak Jump Height(m)`, `Top 3 Jumps Avg. Jump Height(m)`, `Top 5 Jumps Avg. Jump Height(m)` (multi rebound) | Jump height in repeated hops | Flight time method, 9.81 × flight time² / 8, per jump | m | `cmj-jump-height.md` in the `force-plate` skill | Flight time method. Do not compare with take-off velocity jump heights. |
| `Time To Takeoff(s)` (CMJ, squat jump), `CMJ Time To Takeoff(s)` | Time from the start of movement to take-off | Take-off time minus start time | s | `rsi-modified.md` in the `force-plate` skill | Start of movement is traced back to system weight, with no fixed 30 ms step. In the drop jump, `Time To Takeoff` is contact time. |
| `mRSI` (CMJ), `CMJ Modified RSI` | Reactive strength index modified | `Jump Height` divided by `Time To Takeoff` | None listed; the inputs give m/s | `rsi-modified.md` in the `force-plate` skill | Matches RSImod with take-off velocity jump height |
| `RSI` (CMJ), `CMJ RSI` | Flight time per second of jump time | `Flight Time` divided by `Time To Takeoff` | None | None | Not RSImod and not drop-jump RSI |
| `mRSI` (drop jump), `Rebound Modified RSI` | Jump height per second of contact | Take-off velocity jump height divided by contact time | None listed; the inputs give m/s | `rsi-modified.md` in the `force-plate` skill | This is what `rsi-modified.md` calls drop-jump RSI, not RSImod |
| `RSI` (drop jump), `Rebound RSI` | Flight time per second of contact | Flight time divided by contact time | None | `rsi-modified.md` in the `force-plate` skill | Matches the reactive strength ratio in `rsi-modified.md`, not drop-jump RSI. |
| `Peak Force(N)` (isometric test) | Highest force in the pull | Highest combined force, including body weight | N | `imtp-peak-force.md` in the `force-plate` skill | Gross peak force |
| `Net Peak Force(N)` | Highest force above body weight | `Peak Force` minus `System Weight` | N | `imtp-peak-force.md` in the `force-plate` skill | Net peak force. System weight includes any pretension on the bar (Merrigan et al., 2022). |
| `Relative Peak Force(%)`, `Relative Peak Force (BW)(N/kg)` | Peak force scaled to the athlete | `%` divides by this trial's system weight; `(BW)` divides by the athlete's last known body weight | %, N/kg | `imtp-peak-force.md` in the `force-plate` skill | `%` is not N/kg. N/kg = % × 9.81 / 100 when the same weight is used. `(BW)` uses a stored weight, not this trial's. |
| `RFD 0-50 ms(N/s)` to `RFD 0-250 ms(N/s)`, `Force at 50 ms(N)` to `Force at 250 ms(N)`, `Time to Peak Force(s)` | Force rise from the start of the pull | Average slope from 0 ms to the window end | N/s, N, s | `imtp-peak-force.md` in the `force-plate` skill | Fixed windows match the reference method. Merrigan et al. (2022) report a start-of-pull rule of 5 standard deviations above body weight. The API dictionary also reports `Initiation Threshold`, 3 standard deviations of the quiet period, as a quality check; it does not say whether this sets the start. |
| `L\|R ...(%)` metrics, for example `L\|R Avg. Braking Force(%)`, `L\|R Peak Force(%)` | Left to right difference | Hawkin does not publish the formula. The asymmetry report shows left-dominant values as positive. | % | `limb-symmetry-index.md` in the `limb-symmetry` skill | Unknown formula. Recompute from the `Left` and `Right` columns. |
| `Left ...` and `Right ...` metrics | One plate's value | Plate force over the same window. `Force at Peak` columns give each plate's force at the instant of combined peak force, not each plate's own peak. | N, N/s | `limb-symmetry-index.md` in the `limb-symmetry` skill | Use these as the limb values for any symmetry formula |
| `System Weight(N)` | Athlete weight plus any load | Lowest 1 s average of force in the weighing phase, found by an optimization loop | N | `cmj-jump-height.md` in the `force-plate` skill | The reference method uses the mean of the first 1 s. The loop is not published. |

## Transform the data

Follow these steps to turn Hawkin data into the athlete, session, and measure tables from `ams-data-setup`:

1. Pull athletes with `get_athletes()` or `GetAthletes()`.
2. Pull trials one test type at a time with `typeId`, because each test type has its own metric columns. Set `includeInactive` explicitly. For a full history, pull month by month with `from` and `to`.
3. Map each Hawkin athlete to your `athlete_id` in the source ID table. Use `athlete_id` from Hawkin as `source_athlete_id`. A custom `external` property can hold your own ID.
4. Convert `timestamp` from Unix seconds to the local date and time of the session. The API gives no time zone, so store each team's time zone yourself.
5. Build sessions by local date. Hawkin's own exports treat one day as one session.
6. Reshape to one row per athlete, trial `id`, metric, and side. Read `side` from the label: `Left` gives `left`, `Right` gives `right`, everything else `NA`. Store `L|R` metrics as their own asymmetry measures, not as a side.
7. Name each measure from the API column name, label plus unit, not the metric ID. Some IDs mean different metrics in different test types. The label alone is not enough: the weigh-in has two metrics labeled `Weight`, one in kgs and one in lbs.
8. Read the unit from the label or the dictionary `units` field. Convert ms to s for `Time to Stabilization` (spelled `Time To Stabilization` in the drop landing), `Time to Peak Braking Force`, `Rebound Time to Peak Braking Force`, `Rebound Flight Time`, and `Rebound Contact Time` before you combine them with other times. Match on the unit in the column name, not on the label text.
9. Convert values to numbers. Treat `"N/A"` text and nulls as missing.
10. Remove duplicates by trial `id`. When a sync pull returns a trial you already have, replace the old row. Mark trials with `active` false as excluded.
11. Take the trial number from the end of `segment`, or rank trials by `timestamp` within the session.
12. Choose one trial rule per metric, such as the best trial or the mean of all trials, and state it. The cloud **Averages** export uses the mean of the day's trials.
13. Keep the drop jump method tag and ``Drop Height`` with each drop jump trial. Hawkin adds the tag automatically (Hawkin blog, drop jump method).
14. Recompute asymmetry from the `Left` and `Right` values with one stated formula and sign convention. Keep Hawkin's `L|R` value beside it for comparison.

## Common mistakes

These are the mistakes most often made with Hawkin data:

- Pairing Hawkin and VALD metrics by name. Hawkin's braking phase starts at peak negative velocity. So Hawkin `Braking Phase` and `Braking Net Impulse` match VALD `Eccentric Deceleration Phase Duration` and `Eccentric Deceleration Impulse` (Merrigan et al., 2022). They do not match VALD `Braking Phase Duration` or `Eccentric Braking Impulse`, which start at minimum force (VALD glossary).
- Comparing Hawkin CMJ `mRSI` with VALD `RSI-modified`. Hawkin uses take-off velocity jump height, so it matches VALD `RSI-modified (Imp-Mom)`. VALD `RSI-modified` uses flight-time jump height.
- Treating Hawkin CMJ `RSI` as any VALD RSI. It is flight time divided by time to take-off, which VALD calls `Flight Time:Contraction Time`.
- Comparing Hawkin `Positive Impulse` with VALD `Positive Impulse`, or Hawkin `Stiffness` with VALD `CMJ Stiffness`. The names look alike but the definitions differ.
- Comparing `Time To Takeoff` in s with VALD `Contraction Time` in ms, or depth in m with VALD depth in cm. The start-of-movement rules also differ: Hawkin uses 5 standard deviations. VALD does not publish a single start-of-movement threshold; its 20 N figure is the take-off and landing threshold.
- Treating Hawkin relative force as N/kg. Hawkin `Relative` force metrics are percentages of system weight. Only the isometric `(BW)` metrics are N/kg.
- Mapping by metric ID. In the CMJ, ID `positiveImpulse` is `Positive Net Impulse`, and `relativeBrakingImpulse` and `relativePropulsiveImpulse` are net impulses. In the drop jump, the same IDs are gross impulses. Map by label.
- Mixing multi rebound jump heights, which use flight time, with CMJ jump heights, which use take-off velocity.
- Reading `Impulse Ratio` the wrong way up. The API dictionary says braking over propulsive; the CMJ section of the metric database says propulsive over braking. Check against the two impulse columns.
- Trusting `Relative Peak Landing Force` as a peak. Hawkin's own description calls it the average landing force as a percentage of system weight.
- Mixing drop jump trials from different drop height methods. Since an update announced on 2025-01-14, Hawkin uses reverse integration, then flight time, then box height.
- Missing tests in a cloud export. Without a date range you get only the 100 most recent tests, and without **Include Inactive Metrics** you get only active metrics.
- Missing pages in R. `get_tests()` in `hawkinR` 2.0.1 logs a warning and returns the pages it has when the API returns an error. Compare the row count with what you expect. `hdforce` raises an error instead.
- Trusting `from` and `to` in `hawkinR` to the second. The 2.0.1 source turns both into dates at 00:00 UTC, even when you pass a Unix timestamp, so `to = "2026-10-02"` stops at the start of that day. `hdforce` reads date strings at 00:00 in the computer's time zone.
- Athletes on the wrong plates. Left foot on the left plate, right foot on the right plate, which has the power and zero button. Swapped feet invert all left, right, and asymmetry values, and only Hawkin tech support can fix stored trials (Hawkin help, left and right plate).
- Passing `region = "APAC"` to `hdforce`. `hawkinR` accepts it, but `hdforce` needs `"Asia/Pacific"`. Any other value sends `hdforce` to Hawkin's development server, `https://cloud.dev.hawkindynamics.com/api`.
- Taking free run metric names from the `MetricDictionary`. It lists none for the force plate free run.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against a known trial:

- The asymmetry formula behind `L|R` metrics, and the sign in the API.
- Take-off, touchdown, and contact thresholds. The 25 N, 30 N, and 30 ms values come from Merrigan et al. (2022), not from Hawkin's documentation.
- The optimization loop that picks `System Weight`.
- The start-of-pull rule for the isometric test. Merrigan et al. (2022) report 5 standard deviations; Hawkin's own pages do not state it.
- The direction of `Impulse Ratio`.
- Whether `Relative Peak Landing Force` is a peak or an average.
- Whether `P1 Propulsive Impulse` and `P2 Propulsive Impulse` are net or gross. They are on the metric database page but not in the API dictionary.
- The denominator of the phase percentage metrics, such as `Braking Phase %`.
- The start and end events of the drop landing impact and stabilization phases.
- The column names and units of the cloud CSV export, and whether the imperial setting changes them.
- The API names of the force plate free run metrics.
- Whether the API includes inactive trials when `includeInactive` is not sent.
- Whether a time zone or offset is stored with each trial.

## Sources

These sources support the facts in this file:

- Hawkin Beta API Specification 1.12, in the Hawkin power-query repository: <https://github.com/HawkinDynamics/power-query>, accessed 2026-10-02.
- Hawkin Power Query script for the free run, which states the API's `includeInactive` default: <https://github.com/HawkinDynamics/power-query/blob/HEAD/Generics/Tests%20by%20Test%20Type/FreeRun.pq>, accessed 2026-10-02.
- `hawkinR` 2.0.1 on CRAN: <https://cran.r-project.org/web/packages/hawkinR/index.html>, accessed 2026-10-02.
- `hawkinR` manual: <https://cran.r-universe.dev/hawkinR/doc/manual.html>, accessed 2026-10-02.
- `hawkinR` source: <https://github.com/HawkinDynamics/hawkinR>, accessed 2026-10-02.
- `hdforce` 2.1.0 on PyPI: <https://pypi.org/project/hdforce/>, accessed 2026-10-02.
- `hdforce` source: <https://github.com/HawkinDynamics/hawkinPy>, accessed 2026-10-02.
- Hawkin metric database: <https://www.hawkindynamics.com/hawkin-metric-database>, accessed 2026-10-02.
- Hawkin blog, phases of the CMJ: <https://www.hawkindynamics.com/blog/phases-of-the-cmj>, accessed 2026-10-02.
- Hawkin blog, two key factors that influence CMJ force data: <https://www.hawkindynamics.com/blog/two-key-factors-that-can-influence-cmj-force-data>, accessed 2026-10-02.
- Hawkin blog, jump height from take-off velocity: <https://www.hawkindynamics.com/blog/calculate-jump-height-from-take-off-velocity>, accessed 2026-10-02.
- Hawkin blog, jump height from flight time: <https://www.hawkindynamics.com/blog/calculate-jump-height-from-flight-time>, accessed 2026-10-02.
- Hawkin blog, drop jump method and metrics: <https://www.hawkindynamics.com/blog/leading-drop-jump-method-and-metrics>, accessed 2026-10-02.
- Hawkin blog, new landing metrics: <https://www.hawkindynamics.com/blog/new-landing-metrics>, accessed 2026-10-02.
- Hawkin blog, asymmetry report: <https://www.hawkindynamics.com/blog/asymmetry-report>, accessed 2026-10-02.
- Hawkin RSI course: <https://www.hawkindynamics.com/hubfs/RSI%2BCourse%2B%E2%94%82%2BHawkin%2BDynamics%2BEdu.pdf>, accessed 2026-10-02.
- Hawkin help, exporting data from the cloud: <https://learning.hawkindynamics.com/knowledge/exporting-data-from-cloud>, accessed 2026-10-02.
- Hawkin help, API token: <https://learning.hawkindynamics.com/knowledge/how-to-create-an-api-token>, accessed 2026-10-02.
- Hawkin help, active metrics: <https://learning.hawkindynamics.com/knowledge/how-do-i-make-metrics-active>, accessed 2026-10-02.
- Hawkin help, imperial units: <https://learning.hawkindynamics.com/knowledge/how-to-i-convert-metrics-to-the-imperial-system>, accessed 2026-10-02.
- Hawkin help, disabled tests: <https://learning.hawkindynamics.com/knowledge/re-enabling-disabled-tests>, accessed 2026-10-02.
- Hawkin help, left and right plate: <https://learning.hawkindynamics.com/knowledge/is-there-a-left-and-right-force-plate>, accessed 2026-10-02.
- Hawkin help, RSI and mRSI: <https://learning.hawkindynamics.com/knowledge/what-is-the-difference-between-rsi-and-mrsi>, accessed 2026-10-02.
- Merrigan JJ, Stone JD, Galster SM, Hagen JA. Analyzing force-time curves: comparison of commercially available automated software and custom MATLAB analyses. Journal of Strength and Conditioning Research. 2022;36(9):2387-2402. <https://doi.org/10.1519/JSC.0000000000004275>
- Badby AJ, Mundy PD, Comfort P, Lake JP, McMahon JJ. The validity of Hawkin Dynamics wireless dual force plates for measuring countermovement jump and drop jump variables. Sensors. 2023;23(10):4820. <https://doi.org/10.3390/s23104820>
- McMahon JJ, Suchomel TJ, Lake JP, Comfort P. Understanding the key phases of the countermovement jump force-time curve. Strength and Conditioning Journal. 2018;40(4):96-106. <https://doi.org/10.1519/SSC.0000000000000375>
- VALD ForceDecks Technical Glossary V2.0: <https://support.vald.com/hc/en-au/articles/31552969607321-ForceDecks-Technical-Metric-Glossary>, accessed 2026-10-02.
- VALD help, key moments and phases of a CMJ: <https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump>, accessed 2026-10-02.
