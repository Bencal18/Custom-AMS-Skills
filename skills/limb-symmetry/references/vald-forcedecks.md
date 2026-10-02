# VALD ForceDecks data

Checked against: ForceDecks external API version 1.6.0 (specification `v2019q3`), ForceDecks Technical Glossary V2.0 (March 2024), ForceDecks User Guide (November 2023), the `valdr` R package 4.0.0, and the VALD help articles on the ForceDecks API, default metrics, and Hub release notes that the Sources section lists, on 2026-10-02.

This file describes the VALD ForceDecks API output and export format, what each metric means, and how to transform the data for analysis. VALD, ForceDecks, and VALD Hub are trademarks of their owner. This repository is not affiliated with or endorsed by VALD.

## Get the data

Use one of these three routes:

- Web export: in VALD Hub, go to **Dashboard**, then **Results Export**, then the **ForceDecks** tab. Select the tests, then select **Export**. The file is a CSV.
- API: VALD issues API credentials through VALD Support. The API uses OAuth 2 client credentials. Request a token from `https://auth.prd.vald.com/oauth/token` with `grant_type=client_credentials`, your `client_id` and `client_secret`, and `audience=vald-api-external`. Send the token as `Authorization: Bearer <token>`.
- R: the `valdr` package, published by VALD on CRAN, wraps the API. `get_forcedecks_data()` returns a list of four tables: `profiles`, `result_definitions`, `tests`, and `trials`.

API base URLs follow the pattern `https://prd-<region>-api-<service>.valdperformance.com`. Region codes are `use` (US East), `euw` (Europe West), and `aue` (Australia East). The ForceDecks service is `extforcedecks`. The athlete service is `externalprofile`.

VALD changed API authentication in March 2026. Credentials issued before that change may not work.

## API output

The ForceDecks API returns data at three levels: test, then trial, then result.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /tests?TenantId=&ModifiedFromUtc=` | Tests changed since a date. Returns HTTP 204 when there are no more tests. | `testId`, `profileId`, `testType`, `recordedDateUtc`, `recordedDateOffset`, `recordedDateTimezone`, `modifiedDateUtc`, `weight` |
| `GET /v2019q3/teams/{tenantId}/tests/{testId}/trials` | The trials in one test, each with its results | `id`, `athleteId`, `recordedUTC`, `limb`, `results` |
| `GET /resultdefinitions` | The name, unit, and description of every metric | `resultId`, `resultIdString`, `resultName`, `resultUnitName`, `resultDescription`, `supportsAsymmetry`, `isRepeatResult`, `resultUnitScaleFactor`, `trendDirection` |
| `GET /profiles?TenantId=` (Profile API) | Athletes | `profileId`, `givenName`, `familyName`, `externalId`, `dateOfBirth` |

Each result in a trial has these fields:

- `resultId`: the metric. Join it to `/resultdefinitions` for the name and unit.
- `value`: the number. VALD stores it in the internal unit, typically SI. Multiply it by `resultUnitScaleFactor` from the result definition to get the display unit.
- `limb`: one of `Trial`, `Left`, `Right`, or `Asym`. The same metric appears once per limb value.
- `repeat`: the repetition number, for tests with repeated efforts such as hops and rebound jumps.

Each result definition has a `trendDirection` field. Its values are `Positive`, `Negative`, and `None`. It shows which direction VALD treats as good.

The test-level `weight` field is -1 when weighing was skipped. ForceDecks then estimates the weight before each rep and stores the estimate in the `Athlete Standing Weight` metric. Do not read -1 as a body weight.

Paging works by date. Request tests with `ModifiedFromUtc`, then use the last `modifiedDateUtc` you received as the next `ModifiedFromUtc`. Stop at HTTP 204.

## Export columns

VALD does not publish the column list for the Hub CSV export. A public parser for Hub exports shows these patterns:

- One row per test.
- Headers in the form `Metric name [unit]`, for example `Jump Height (Imp-Mom) [cm]`, `Contraction Time [ms]`, `BW [KG]`, and `Peak Power / BM [W/kg]`.
- Identity and date columns such as `Name`, `ExternalId`, `Test Type`, `Date`, `Time`, `Reps`, and `Tags`.
- Asymmetry cells as text, such as `12.3 L` or `8.1 R`, where the letter names the side with the larger value.

From 2026-09-28, the Hub export adds these columns for the listed test types:

- `Additional Load` for the LCMJ, LSJ, PUSHUPT, SLSQT, and SQT test types.
- `Drop Height` for the DJ, SLDJ, LAH, and SLLAH test types.

Exports vary. Check each file for these differences:

- Square brackets or round brackets around units.
- Comma or semicolon delimiters.
- Dates in `YYYY/MM/DD`, `MM/DD/YYYY`, or `DD/MM/YYYY` order, depending on regional settings.
- Jump height in inches instead of centimeters.
- Trailing spaces, double spaces, or a byte order mark in headers.
- Several test types in one file, for example bilateral CMJ, single-leg CMJ, and IMTP.

## Metric meanings

The definitions below come from the ForceDecks Technical Glossary V2.0. VALD sources disagree on the take-off and landing threshold. The Technical Glossary V2.0 (March 2024) and the User Guide (November 2023) say take-off is when vertical force drops below 20 N, and landing is when it rises above 20 N. The VALD knowledge base pages on the key moments of a countermovement jump and a squat jump say 30 N. Do not assume either value. Ask the user, or check the setting in their software.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `Jump Height (Imp-Mom)` | Jump height from the impulse-momentum method | From center of mass velocity at take-off and body mass | cm | `cmj-jump-height.md` in `force-plate` | Same method. Take-off thresholds may differ, so values may differ slightly. |
| `Jump Height (Flight Time)` | Jump height from time in the air | From flight time | cm | `cmj-jump-height.md` in `force-plate` | Matches the flight time method. Gives different values from impulse-momentum. |
| `Jump Height (Imp-Dis)` | Jump height from displacement | Maximum center of mass displacement between take-off and landing | cm | `cmj-jump-height.md` in `force-plate` | A third method. Do not mix it with the other two. |
| `Flight Time` | Time in the air | Take-off to landing | ms | `cmj-jump-height.md` in `force-plate` | None |
| `Contraction Time` | Time to take-off | Start of movement to take-off | ms | `rsi-modified.md` in `force-plate` | Equals time to take-off |
| `RSI-modified` | Reactive strength index modified | `Jump Height (Flight Time)` divided by `Contraction Time` | m/s | `rsi-modified.md` in `force-plate` | Uses flight time jump height |
| `RSI-modified (Imp-Mom)` | Reactive strength index modified | `Jump Height (Imp-Mom)` divided by `Contraction Time` | m/s | `rsi-modified.md` in `force-plate` | Uses impulse-momentum jump height. Not interchangeable with `RSI-modified`. |
| `Peak Net Take-off Force / BM` | Peak force above body weight, per kg | Maximum vertical force minus body weight, divided by body mass | N/kg | None | None |
| `Peak Vertical Force [N]` (IMTP test) | Highest force in the pull | VALD does not publish whether it includes body weight. VALD also reports `Peak Vertical Force / BM [N/kg]`, `Peak Vertical Force [N] Asymmetry`, and `Start Time to 80% Peak Force`. | N | `imtp-peak-force.md` in `force-plate` | Confirm gross or net before you compare with published values |
| Asymmetry (any metric with `Asym` limb) | Difference between left and right | Glossary: (Left − Right) ÷ max(Left, Right) × 100 | % | `limb-symmetry-index.md` in `limb-symmetry` | A different formula from the limb symmetry index. VALD sources disagree on the sign. |

## Transform the data

Follow these steps to turn ForceDecks data into the athlete, session, and measure tables:

1. Pull profiles, tests, trials, and result definitions. When you use `valdr`, call `get_forcedecks_data()`.
2. Join tests to athletes on `profileId`. Join trials to tests on `testId`. Join results to definitions on `resultId`.
3. Reshape to one row per athlete, test, trial, metric, limb, and repeat. Keep `limb` and `repeat` in the key, or you lose left, right, and asymmetry rows.
4. Filter by `testType` so each analysis uses one test type.
5. Convert `value` to a number. `valdr` stores it as text.
6. Read each metric's unit from `resultUnitName`. Multiply `value` by `resultUnitScaleFactor` to get the display unit. Convert inches to centimeters when a CSV reports jump height in inches.
7. Compute the local test date from the UTC time plus `recordedDateOffset` or `recordedDateTimezone`. Do not take the date from the UTC time alone, because evening tests move to the next day.
8. Remove duplicates. Keep one row per `testId`, using the row with the latest `modifiedDateUtc`. For CSV files, drop rows that are exact copies.
9. Choose one trial rule per metric, such as the best trial or the mean of all trials, and state it. VALD does not define which trial to report. Where the result definition has a `trendDirection` of `Positive` or `Negative`, use it to decide which direction is better. A `trendDirection` of `None` marks no good direction. For time metrics such as `Contraction Time`, the lowest value is the best.
10. Recompute asymmetry from the left and right values with one stated formula and sign convention. Keep VALD's `Asym` value beside it for comparison.

## Common mistakes

These are the mistakes most often made with ForceDecks data:

- Mixing `Jump Height (Flight Time)` and `Jump Height (Imp-Mom)` in one trend. Pick one method and use it for every session.
- Comparing `RSI-modified` with `RSI-modified (Imp-Mom)`. They use different jump heights.
- Using `export_forcedecks_csv()` from `valdr` for limb analysis. That CSV drops the limb columns, so left, right, and asymmetry rows of one metric look identical. Use the `trials` table from `get_forcedecks_data()` instead.
- Removing duplicates by trial and metric only. This silently deletes left, right, and asymmetry rows.
- Taking the calendar date from the UTC time.
- Missing older tests. `valdr` remembers the last pull date and returns only newer tests on the next call. Pass an explicit start date for a full history.
- Reading `12.3 L` as a number without the side, or assuming a sign convention for VALD's asymmetry values.
- Mixing bilateral CMJ, single-leg CMJ, and IMTP rows from one export file.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against the result definitions or a known test:

- The unit of the test-level `weight` field. VALD documents only that it is -1 when weighing was skipped.
- The unit of `recordedDateOffset` (likely minutes).
- Which jump height method VALD Hub shows as the headline jump height. VALD's 2026 default CMJ metrics list `Jump Height (Imp-Mom)` (the iOS default metrics article). Whether Hub shows the same method is not confirmed.
- Whether IMTP `Peak Vertical Force` includes body weight.
- The sign of VALD asymmetry values in the API and in Hub exports.
- How Hub and the API handle trials that a tester excluded.
- The take-off and landing threshold, 20 N or 30 N. VALD sources give both values.

## Sources

- VALD ForceDecks external API specification: <https://prd-use-api-extforcedecks.valdperformance.com/swagger/v2019q3/swagger.json>, accessed 2026-10-02.
- VALD Profile API specification: <https://prd-use-api-externalprofile.valdperformance.com/swagger/v1/swagger.json>, accessed 2026-10-02.
- VALD help article "A guide to using the External ForceDecks API": <https://support.vald.com/hc/en-au/articles/38086939480729-A-guide-to-using-the-External-ForceDecks-API>, accessed 2026-10-02.
- VALD help article "Default result metrics in ForceDecks iOS": <https://support.vald.com/hc/en-au/articles/59342932219289-Default-result-metrics-in-ForceDecks-iOS>, accessed 2026-10-02.
- VALD help article "VALD Hub Release Notes 28 September 2026": <https://support.vald.com/hc/en-au/articles/62663382316697-VALD-Hub-Release-Notes-28-September-2026>, accessed 2026-10-02.
- VALD ForceDecks Technical Glossary V2.0, March 2024: <https://support.vald.com/hc/en-au/article_attachments/31552911571353>, accessed 2026-10-02. An earlier version of this file cited a copy on jsams.org. That copy is a different document, the "Common tests and metrics" page.
- VALD ForceDecks User Guide, November 2023: <https://support.vald.com/hc/article_attachments/31298911123353>, accessed 2026-10-02.
- VALD help article "Key Moments and Phases of a Countermovement Jump": <https://support.vald.com/hc/en-au/articles/4999710329113-Key-Moments-and-Phases-of-a-Countermovement-Jump>, accessed 2026-10-02 through the Internet Archive copy of 2026-09-05.
- VALD help article "Key Moments and Phases of a Squat Jump": <https://support.vald.com/hc/en-au/articles/4999709811737-Key-Moments-and-Phases-of-a-Squat-Jump>, accessed 2026-10-02 through the Internet Archive copy of 2025-10-08.
- `valdr` R package 4.0.0 source: <https://github.com/cran/valdr>, accessed 2026-10-02.
- `valdrViz` R package 1.0.2 source: <https://github.com/cran/valdrViz>, accessed 2026-10-02.
- Public Power BI parser for VALD Hub CMJ exports: <https://github.com/NateKolbSportScience/CMJ-Trend-Report>, accessed 2026-10-02.
- VALD asymmetry calculator: <https://valdhealth.com/calculators>, accessed 2026-10-02.
- VALD help article "Export Test Data from VALD Hub": <https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub>, accessed 2026-10-02.
- VALD help article "Common tests and metrics for ForceDecks application": <https://support.vald.com/hc/en-au/articles/16299047617305-Common-tests-and-metrics-for-ForceDecks-application>, accessed 2026-10-02.
