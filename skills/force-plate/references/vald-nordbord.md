# VALD NordBord data

Checked against: NordBord external API version 1.24.0 and the `valdr` R package 4.0.0, on 2026-10-02.

This file describes the VALD NordBord API output and export format, what each metric means, and how to transform the data for analysis. VALD, NordBord, and VALD Hub are trademarks of their owner. This repository is not affiliated with or endorsed by VALD.

## Get the data

Use one of these three routes:

- Web export: in VALD Hub, go to **Dashboard**, then **Results Export**, then the **NordBord** tab. Select the tests, then select **Export**. The file is a CSV. A separate force trace export gives time in seconds and left and right force in newtons.
- API: VALD issues API credentials through VALD Support. The API uses OAuth 2 client credentials. Request a token from `https://auth.prd.vald.com/oauth/token` with `grant_type=client_credentials`, your `client_id` and `client_secret`, and `audience=vald-api-external`. Send the token as `Authorization: Bearer <token>`.
- R: the `valdr` package, published by VALD on CRAN, wraps the API. `get_nordbord_data()` returns the tests and the athlete profiles.

API base URLs follow the pattern `https://prd-<region>-api-<service>.valdperformance.com`. Region codes are `use` (US East), `euw` (Europe West), and `aue` (Australia East). The NordBord service is `externalnordbord`. The athlete service is `externalprofile`.

VALD changed API authentication in March 2026. Credentials issued before that change may not work.

## API output

The NordBord API returns one row per test, with left and right values in separate fields.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /tests/v2?TenantId=&ModifiedFromUtc=` | Test summaries changed since a date | `profileId`, `testId`, `testDateUtc`, `modifiedDateUtc`, `testTypeName`, `leftMaxForce`, `rightMaxForce`, `leftAvgForce`, `rightAvgForce`, `leftTorque`, `rightTorque`, `leftImpulse`, `rightImpulse`, `leftRepetitions`, `rightRepetitions` |
| `GET /tests/{testId}/metrics?tenantId=` | Extra metrics per side | `leftMaxForcePerKg`, `rightMaxForcePerKg`, `leftAvgForcePerKg`, `leftMaxRFDNewtonsPerSecond`, `leftMaxTorquePerKg`, and RFD and impulse at 50 to 250 ms |
| `GET /tests/{testId}/nordbordtrace?tenantId=` | The force trace | `forces`, a list of `ticks`, `leftForce`, and `rightForce` |
| `GET /tests` (deprecated) | Test summaries, paged by page number | Same as `/tests/v2`, but the athlete ID is `athleteId` and the modified time is `modifiedUtc` |
| `GET /profiles?TenantId=` (Profile API) | Athletes | `profileId`, `givenName`, `familyName`, `externalId` |

Paging on `/tests/v2` works by date. Use the last `modifiedDateUtc` you received as the next `ModifiedFromUtc`. Stop at HTTP 204, or when the last test ID repeats.

## Export columns

VALD does not publish the column list for the NordBord Hub CSV export. Ask the user for the header row, and map it to the API fields in the table above.

## Metric meanings

VALD states the metric units as N for force, Nm for torque, and Ns for impulse. This is not confirmed against the API field metadata. Torque is force multiplied by the lever arm from the knee joint to the ankle hook, which the device estimates from the knee position setting.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| `leftMaxForce`, `rightMaxForce` | Highest force on each leg in the test | Peak force at the ankle hook | N (VALD-stated, not confirmed in the API) | `eccentric-hamstring-force.md` in `force-plate` | Force at the ankle, not hamstring muscle force |
| `leftAvgForce`, `rightAvgForce` | Average force on each leg | In the NordBord app, the average of the peaks of all repetitions in the test. Not confirmed that the API field uses the same rule. | N (VALD-stated, not confirmed in the API) | `eccentric-hamstring-force.md` in `force-plate` | Confirm before you use it |
| `leftMaxForcePerKg`, `rightMaxForcePerKg` | Peak force relative to body mass | Peak force divided by body mass. Body weight is entered in the NordBord app or pulled from VALD Hub, and the per-kg metrics need it. | N/kg | `eccentric-hamstring-force.md` in `force-plate` | Check which body weight was entered or pulled |
| `leftTorque`, `rightTorque` | Turning force at the knee | Force multiplied by the estimated lever arm | N·m (VALD-stated as Nm, not confirmed in the API) | `eccentric-hamstring-force.md` in `force-plate` | Depends on the knee position setting |
| `leftImpulse`, `rightImpulse` | Force over time | Area under the force curve, excluding time below an impulse threshold | N·s (VALD-stated as Ns, not confirmed in the API) | None | Depends on the impulse threshold setting |
| Imbalance (in the NordBord app) | Difference between left and right peak force | The app describes it as the percentage difference between left and right maximums, with a second imbalance on left and right averages. VALD does not publish the formula. A VALD research summary used `\|L − R\| / (L + R)` for hamstring asymmetry. The ForceDecks glossary formula is `(Left − Right) / max(Left, Right) × 100`. The two formulas differ, and VALD does not say which one the app uses. | % | `limb-symmetry-index.md` in `limb-symmetry` | The API has no imbalance field. Compute it yourself with a stated formula. |

## Transform the data

Follow these steps to turn NordBord data into the athlete, session, and measure tables:

1. Pull test summaries from `/tests/v2` and athletes from the Profile API. When you use `valdr`, call `get_nordbord_data()`.
2. Join tests to athletes on `profileId`. When data comes from the deprecated `/tests` endpoint, use `athleteId` instead.
3. Filter by `testTypeName` so each analysis uses one test, for example Nordic or an isometric test.
4. Reshape the wide left and right columns to one row per athlete, test, side, and metric.
5. Use `testDateUtc` as the test time. The API gives no time zone for NordBord tests, so state that dates are in UTC.
6. Remove duplicates. Keep one row per `testId`, using the row with the latest modified time.
7. Compute between-limb imbalance from `leftMaxForce` and `rightMaxForce` with one stated formula and sign convention.
8. Use the force trace or the training repetition endpoints when you need values per repetition. The test summary holds one row per test.

## Common mistakes

These are the mistakes most often made with NordBord data:

- Treating ankle hook force as hamstring muscle force.
- Comparing torque across sessions with different knee position settings.
- Comparing values per kg without checking which body mass was used.
- Reading the deprecated and the v2 endpoints with one set of field names. They name the athlete ID and the modified time differently.
- Assuming an imbalance formula. Compute imbalance yourself and state the formula.
- Mixing Nordic tests with isometric tests from the same export.
- Ignoring deselected repetitions. Testers can deselect unwanted repetitions before upload. Check whether the export or API still includes them.

## Details that are not confirmed

Do not assume these details. Ask the user, or check them against a known test:

- The units of the API force, torque, and impulse fields. VALD states N, Nm, and Ns, but this is not confirmed against API field metadata.
- The unit of `ticks` in the force trace, and the sampling rate.
- The meaning of `leftCalibration` and `rightCalibration`.
- Whether `leftAvgForce` is the mean of repetition peaks.
- The imbalance formula in the NordBord app. VALD sources give two different formulas for left and right differences.
- Whether repetitions deselected in the app are left out of the export and API values.
- The exact `testTypeName` values.

## Sources

- VALD NordBord external API specification: <https://prd-use-api-externalnordbord.valdperformance.com/swagger/v1/swagger.json>, accessed 2026-10-02.
- VALD Profile API specification: <https://prd-use-api-externalprofile.valdperformance.com/swagger/v1/swagger.json>, accessed 2026-10-02.
- `valdr` R package 4.0.0 source: <https://github.com/cran/valdr>, accessed 2026-10-02.
- VALD help article "What Does NordBord Measure?": <https://support.vald.com/hc/en-au/articles/4812624529049-What-Does-NordBord-Measure>, accessed 2026-10-02.
- VALD help article "Understanding Results in the NordBord App": <https://support.vald.com/hc/en-au/articles/4812488985241-Understanding-Results-in-the-NordBord-App>, accessed 2026-10-02.
- VALD help article "NordBord iOS - Release Notes": <https://support.vald.com/hc/en-au/articles/29794963555097-NordBord-iOS-Release-Notes>, accessed 2026-10-02.
- VALD ForceDecks Technical Glossary V2.0, March 2024: <https://support.vald.com/hc/en-au/article_attachments/31552911571353>, accessed 2026-10-02.
- VALD research summary "Eccentric Hamstring Strength": <https://valdperformance.com/news/eccentric-hamstring-strength>, accessed 2026-10-02.
- VALD help article "Export Test Data from VALD Hub": <https://support.vald.com/hc/en-au/articles/4799420849049-Export-Test-Data-from-VALD-Hub>, accessed 2026-10-02.
