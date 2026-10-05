# Catapult data

Checked against: OpenField Connect API version 6.0.0 and the `catapultR` R package 0.0.0.69, on 2026-10-02.

This file describes the Catapult OpenField API output and export format, what each metric means, and how to transform the data for analysis. Catapult, OpenField, Vector, and PlayerLoad are trademarks of their owner. This repository is not affiliated with or endorsed by Catapult.

## Get the data

Use one of these four routes:

- Web export: in OpenField, select a session, then select **Export**, then **Export to CSV**. A widget export holds only the parameters, players, bands, and periods selected in the widget. A Configurable Team Report (CTR) export holds all parameters or a chosen parameter group.
- 10 Hz export: OpenField can export GPS and inertial data at 10 Hz as CSV. Position quality columns are `Positional Quality (%)`, `HDOP`, and `#Sats`.
- API: the OpenField Connect API. Create an API token in OpenField under **Settings**, then **API Tokens**. OpenField shows the token once. Send it as `Authorization: Bearer <token>`.
- R: the `catapultR` package, published by Catapult, wraps the API. The account needs the `apiScope:catapultR` module.

API base URLs depend on region:

- North and South America: `https://connect-us.catapultsports.com/api/v6`
- Europe, Middle East, and Africa: `https://connect-eu.catapultsports.com/api/v6`
- Asia Pacific: `https://connect-au.catapultsports.com/api/v6`
- China: `https://connect-cn.catapultsports-cn.com/api/v6`

Older guides use `/api/v4`. Use `/api/v6`.

## API output

The Connect API organizes data as activities (sessions), periods (drills or halves), and athletes.

| Endpoint | Returns | Key fields |
|---|---|---|
| `GET /athletes` | Athletes | `id`, `first_name`, `last_name`, `jersey`, `position_name`, `weight`, `velocity_max`, `tag_list` |
| `GET /activities` | Sessions, paged with `page` and `page_size`, filtered by `start_time` and `end_time` in Unix seconds | `id`, `name`, `start_time`, `end_time`, `period_count`, `athlete_count`, `periods` |
| `GET /activities/{id}/periods` | Periods in one session | `id`, `activity_id`, `name`, `start_time`, `end_time`, `period_depth_id`, `lft`, `rgt` |
| `POST /stats` | Aggregated metrics | One row per group, with one field per requested parameter `slug` |
| `GET /parameters` | Every metric on the account | `slug`, `name`, `unit_type`, `calculation`, `band` |
| `GET /periods/{id}/athletes/{athlete_id}/sensor` | 10 Hz data | `ts`, `cs`, `lat`, `long`, `o`, `v`, `a`, `hr`, `pl`, `pli`, `mp`, `sl`, `pq`, `ref`, `hdop`, `rv`, `alt`, `face`, `xy`, `id` |
| `GET /activities/{id}/athletes/{athlete_id}/efforts` | Velocity and acceleration efforts | `start_time`, `end_time`, `band`, `distance`, `max_velocity`, `acceleration` |
| `GET /athletes/{id}/bands` | The athlete's velocity and acceleration bands, including past bands | Rows with `end_time` of 0 are the current band |

The `POST /stats` body takes four main fields:

- `parameters`: a list of parameter slugs, such as `total_distance`, `total_player_load`, and `max_vel`.
- `group_by`: for example `athlete`, `activity`, or `period`.
- `filters`: a list of `{name, comparison, values}`, for example an `activity_id` filter.
- `source`: `cached_stats` or `annotation_stats`.

A metric that fails to calculate returns `null` with an `errors` object.

The 10 Hz sensor fields use these units: `v` in m/s, `a` in m/s², `o` (odometer, cumulative distance) in m, `hr` in beats per minute, `pl` in PlayerLoad units, and `pq` (position quality) in percent. `ts` is Unix time in seconds and `cs` adds centiseconds. `ref` is the number of satellites for GPS data, or anchors for indoor positioning.

The Connect API pages list 20 sensor fields in total. These fields have the following meanings and units:

- `lat` and `long`: latitude and longitude. The pages publish no unit.
- `pli`: instantaneous PlayerLoad, in AU. `pl` is the accumulated value.
- `mp`: metabolic power, in W/kg.
- `sl`: smooth load, instantaneous. The sensor page publishes no unit. Connect event pages use smoothed PlayerLoad units.
- `hdop`: horizontal dilution of precision, GPS only.
- `rv`: raw velocity, instantaneous. The pages publish no unit. Catapult publishes no filter for `v`, so the difference from `v` is implied by the names.
- `alt`: altitude. The pages publish no unit.
- `face`: facing direction. The pages publish no unit.
- `xy`: field x and y coordinates. By default they measure from the bottom-left corner of the field. The pages do not state the unit. The unit is probably meters.
- `id`: the database ID of each record, returned in some responses.

## Export columns

Catapult does not publish the header row of the web CSV export in a public page. Ask the user for the header row, and map it to the parameter names from `GET /parameters`.

Through the API, `catapultR` returns aggregated columns named by slug, such as `athlete_name`, `activity_name`, `period_id`, `period_name`, `start_time`, `end_time`, `position_name`, `total_distance`, `total_duration`, `total_player_load`, `max_vel`, `hsr_efforts`, and `date`. In the published example, `date` is text in month, day, year order.

The 100 Hz raw CSV has three metadata lines before the header. The first line holds the reference time in UTC, in month, day, year order.

## Metric meanings

Catapult metrics depend on account settings. Use `GET /parameters` to read the exact calculation and unit on each account.

| Vendor name | What it means | How the vendor calculates it | Units | Reference file | Difference from the reference method |
|---|---|---|---|---|---|
| Total Distance (`total_distance`) | Distance covered | Sum over the selected periods | m | `total-distance.md` in `gps-running-load` | None |
| HS Distance | Distance at high speed | Distance in velocity bands 5 and 6. By default, above 5.5 m/s. | m | `high-speed-running.md` in `gps-running-load` | Depends on the account's band settings |
| Sprint Distance | Distance at sprint speed | Distance in velocity band 6. By default, above 7 m/s. | m | `high-speed-running.md` in `gps-running-load` | Depends on the account's band settings |
| Velocity bands | Speed zones | Set per athlete or group, as absolute speeds or as a percentage of each athlete's maximum. Vector Core allows up to six bands, with these defaults: band 1 0 to 0.2 m/s, band 2 0.2 to 2, band 3 2 to 4, band 4 4 to 5.5, band 5 5.5 to 7, band 6 above 7. OpenField allows up to eight bands, and the Connect API reports velocity effort bands 1 to 8. The public OpenField Bands page publishes no defaults. | m/s, km/h, or other units set on the account | `high-speed-running.md` in `gps-running-load` | Thresholds change by account and season |
| Acceleration Efforts and Deceleration Efforts | Counts of hard speed-ups and slow-downs | Default threshold above 2 m/s². In the `Gen2Acceleration` band set, bands 1 to 3 are decelerations and bands 6 to 8 are accelerations. Bands 4 and 5, near zero, cannot be reported. On Vector 7 Bluetooth activities, Catapult says Accelerations and Decelerations each default to bands 1 to 3. | count | `accelerations-decelerations.md` in `gps-running-load` | The Gen2 effort rules exclude movements shorter than 0.9 s. The fuller Gen2 rules need a Catapult sign-in |
| HMLD (High Metabolic Load Distance) | Distance at high estimated energy cost | Distance above 25.5 W/kg, the cost of running at a constant 5.5 m/s | m | None | Includes acceleration work as well as high-speed running |
| PlayerLoad (`total_player_load`) | Accelerometer load | For each pair of neighboring samples, take the square root of the sum of the squared changes in acceleration on the three axes. Sum these square roots over time, then divide the total by 100 | AU | None | Only comparable with Catapult PlayerLoad |
| PlayerLoad 2D | PlayerLoad without the vertical axis | Catapult defines it as PlayerLoad with the vertical axis left out. Catapult publishes no separate formula. A restatement: drop the vertical term from the square root, then sum and divide by 100 as for PlayerLoad | AU | None | Do not compare with PlayerLoad |
| Player Load per Minute | Rate of PlayerLoad | PlayerLoad divided by duration | AU/min | None | None |
| Acceleration load | Accumulated acceleration from speed | Sum of absolute acceleration values from smoothed 10 Hz speed | Not confirmed | None | A different quantity from PlayerLoad and from acceleration effort counts |
| `max_vel` | Highest speed | Maximum speed in the selected time | m/s, or the account unit | `high-speed-running.md` in `gps-running-load` | None |

## Transform the data

Follow these steps to turn Catapult data into the athlete, session, and measure tables:

1. Pull athletes from `GET /athletes`, sessions from `GET /activities`, and periods from `GET /activities/{id}/periods`.
2. Pull metrics with one `POST /stats` call grouped by athlete and period, or by athlete and activity.
3. Join periods to sessions on `activity_id`. Join stats rows to periods on `period_id` and to athletes on `athlete_id`.
4. Reshape to one row per athlete, session, period, and metric.
5. Convert `start_time` and `end_time` from Unix seconds to dates in the team's time zone. The account time zone is in `user_default_timezone` from the customer info endpoint.
6. Read the unit of each metric from `GET /parameters` and the account settings. Convert km/h to m/s by dividing by 3.6 only after you confirm the unit.
7. Export the band table from `GET /athletes/{id}/bands` with the data. Record the thresholds used for each session.
8. Build session totals from the session-level stats, or from periods that do not overlap. Check the result against the session total distance.
9. For 10 Hz data, compute distance as the last odometer value minus the first, not as a sum of odometer values. Remove samples with poor position quality, and state the rule you used.

## Ice hockey metrics

Catapult's ice hockey metrics need a Vector Pro licence and the OpenField Ice Hockey module. The module uses inertial algorithms to detect hockey strides and hockey bouts. A bout is a period above an intensity threshold that lasts longer than a minimum time. The user sets the bout dwell time in seconds, the PlayerLoad threshold for a bout, and the stride force bands. Metrics that use body weight need the athlete's weight set in OpenField. The metrics are detected after the session, not live (Catapult support, "How to Detect Ice Hockey Metrics").

The detailed definitions of each hockey parameter need a Catapult login to read. If an export holds a hockey metric that this file does not define, ask the user for Catapult's definition. Do not guess it.

## Common mistakes

These are the mistakes most often made with Catapult data:

- Comparing high speed or sprint distance across seasons or teams after someone changed the velocity bands.
- Summing every period row in a session. Periods can nest, so a whole-session period and its drills may both appear. The nesting fields `lft`, `rgt`, and `period_depth_id` suggest a tree, but Catapult does not document the rule. Check sums against the session total.
- Mixing km/h and m/s. The unit follows the account settings.
- Comparing PlayerLoad with accelerometer load from another vendor, or explaining the gap between them. Formulas differ, so the cause of a gap is unknown. Wearing both systems in the same session shows the size of the gap, not its cause.
- Assuming old sessions use new bands. New bands apply only to future sessions unless someone reprocesses the old sessions.
- Reading `date` as day, month, year when it is month, day, year.
- Ignoring position quality fields (`hdop`, `ref`, `pq`) in 10 Hz data.

## Details that are not confirmed

Do not assume these details. Ask the user, or read them from `GET /parameters` and the account settings:

- The header row of the web CSV export.
- The bands set on the user's account. The defaults in this file apply only when nobody changed them.
- The full Gen2 effort rules. A public Catapult page gives only the 0.9 s minimum for acceleration efforts. The fuller rules need a login.
- The boundary rule: whether a value exactly on a velocity or acceleration band boundary counts in the lower or the upper band. Catapult does not publish it. Ask the user. If no one knows, use at or above the lower bound and below the upper bound, and say so.
- The rule for nested periods.
- The exact formula for PlayerLoad 2D. Catapult defines it only as PlayerLoad with the vertical axis left out.

## Sources

- OpenField Connect API reference: <https://docs.connect.catapultsports.com/llms.txt>, accessed 2026-10-02.
- Connect API stats endpoint: <https://docs.connect.catapultsports.com/reference/poststats.md>, accessed 2026-10-02.
- Connect API 10 Hz sensor endpoint: <https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinperiod.md>, accessed 2026-10-02.
- Connect API efforts endpoint: <https://docs.connect.catapultsports.com/reference/geteffortsdataforathleteinactivity.md>, accessed 2026-10-02.
- `catapultR` documentation: <https://catapultr.catapultsports.com/>, and source: <https://github.com/SBGSports/catapultr>, accessed 2026-10-02.
- Catapult, "Understanding Player Load" (also titled "Fundamentals of PlayerLoad"), for the PlayerLoad 2D definition: <https://www.catapult.com/blog/fundamentals-playerload-athlete-work>, accessed 2026-10-02.
- Catapult support, "Acceleration load, acceleration density and acceleration density index", for the 0.9 s Gen2 rule: <https://support.catapultsports.com/hc/en-us/articles/360001559976-Acceleration-load-acceleration-density-and-acceleration-density-index>, accessed 2026-10-02.
- Catapult support, "Catapult Glossary", for OpenField's eight speed bands: <https://support.catapultsports.com/hc/en-us/articles/360001235575-Catapult-Glossary>, accessed 2026-10-02.
- Catapult support, "Parameter Selection During Bluetooth Activities - VECTOR 7": <https://support.catapultsports.com/hc/en-us/articles/15156212637967-Parameter-Selection-During-Bluetooth-Activities-VECTOR-7>, accessed 2026-10-02.
- Connect API sensor data page (10 Hz): <https://docs.connect.catapultsports.com/reference/sensor-data-10hz>, accessed 2026-10-02.
- Connect API 10 Hz dual-stream sensor endpoint for an activity: <https://docs.connect.catapultsports.com/reference/get10hzdualstreamsensordataforathleteinactivity>, accessed 2026-10-02.
- PlayerLoad formula and its variants in the literature: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7052708>, accessed 2026-10-02.
- Catapult, "Individualisation of GPS speed thresholds": <https://www.catapult.com/blog/individualisation-gps-speed-thresholds-challenges-complexities>, accessed 2026-10-02.
- Catapult support, "Bands": <https://support.catapultsports.com/hc/en-us/articles/360000420615-Bands>, accessed 2026-10-02.
- Catapult support, "How to Detect Ice Hockey Metrics": <https://support.catapultsports.com/hc/en-us/articles/360001465176-How-to-Detect-Ice-Hockey-Metrics>, accessed 2026-10-05.
- Catapult Vector Core, "Bands": <https://core.catapultsports.com/hc/en-us/articles/7209599125263-Bands>, accessed 2026-10-02.
- Catapult Vector Core, "Post-Activity Parameters": <https://core.catapultsports.com/hc/en-us/articles/7209919599375-Post-Activity-Parameters>, accessed 2026-10-02.
- Catapult Vector Core, "Catapult Vector App - Parameter Definitions": <https://core.catapultsports.com/hc/en-us/articles/7209931599887-Catapult-Vector-App-Parameter-Definitions>, accessed 2026-10-02.
- Review of acceleration and deceleration methods across devices: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8245618>, accessed 2026-10-02.
