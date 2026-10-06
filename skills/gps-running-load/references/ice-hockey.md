# Ice hockey load data

Last checked: 2026-10-05

## What this file covers

This file helps the AI read ice hockey load data correctly. Hockey data comes from sources that measure different things: league tracking cameras, wearable inertial units, local positioning, heart rate monitors, and official time-on-ice reports. This file says what each source can and cannot give you, and how to keep them apart.

Skating is not running. Ice hockey is a gliding sport (Perez et al., 2022). Players skate in shifts of about 30 to 80 seconds, and get about 15 to 25 minutes on ice per game (Vigh-Larsen & Mohr, 2024). Running thresholds and running ranges in the other reference files do not apply to skating.

## Know what each source measures

Each hockey data source gives you this:

| Source | How it measures | What it gives you | What it cannot give you |
|---|---|---|---|
| NHL puck and player tracking (NHL EDGE) | Infrared emitters in the puck and in each player's jersey, read by cameras above the ice (NHL.com, 2023) | Skating speed, distance skated, speed bursts, zone time, and shot speed | Any accelerometer or inertial load, such as PlayerLoad. No published EDGE field holds one. |
| Wearable inertial unit, such as Catapult | Accelerometer and other inertial sensors in a unit worn on the upper back | Accelerometer load, such as PlayerLoad, and hockey events such as strides and work bouts, from inertial algorithms. The device reference describes the vendor's hockey metrics. | Position on the ice |
| Local positioning, such as Kinexon | Radio tags on the player, read by receivers in the arena | Speed, distance, and acceleration from position | Inertial load, unless the unit also has an accelerometer |
| Heart rate monitor, such as Firstbeat | Chest strap | Heart rate, TRIMP, and time in zones | Movement or skating data |
| Official game reports | Shift-by-shift timing by the league | Time on ice and shifts, split by strength | Any load or intensity |

These sources do not replace each other. In particular, tracking data cannot fill in a missing PlayerLoad. It measures position, not acceleration of the body.

## Read league tracking data

NHL EDGE uses a tracking system built by SMT (SportsMEDIA Technology). Its first full season was 2021-22 (SMT, 2022). The cameras read the players up to 15 times per second and the puck up to 60 times per second (NHL.com, 2023). Sources disagree on the number of cameras, so do not quote one.

EDGE publishes these skater measures (NHL.com, 2023; NHL EDGE data feed):

- Top skating speed, with `imperial` and `metric` values, which the EDGE site shows as mph and km/h.
- Speed burst counts in three bands, in the fields `bursts18To20`, `bursts20To22`, and `burstsOver22`, in mph.
- Distance skated: totals, per 60 minutes, game maximum, and period maximum.
- Distance and time on ice for each game, split by all situations, even strength, power play, and penalty kill. Time on ice in this feed is in seconds, in fields such as `toiAll`.
- Zone time and zone starts, as percentages.

The feed gives distance as `imperial` and `metric` values without naming the unit. Confirm the unit on the EDGE site before you convert.

EDGE does not publish a definition of a burst, such as how long a player must hold the speed. Do not state one.

Convert burst thresholds before you compare them with other data:

| EDGE band | m/s | km/h |
|---|---|---|
| 18 mph | 8.05 | 29.0 |
| 20 mph | 8.94 | 32.2 |
| 22 mph | 9.83 | 35.4 |

The per-game data that EDGE web pages load comes from an NHL feed at `api-web.nhle.com`. The NHL publishes no documentation for this feed, and its fields can change without notice. Check field names against a fresh download each season.

## Get time on ice from the official reports

Time on ice (TOI) is the time a player spends on the ice in play. Take it from the league's official reports, not from a wearable's session length. For NHL games, these reports hold TOI:

- Time on ice shift reports, one per team: `https://www.nhl.com/scores/htmlreports/<season>/TH<game>.HTM` for the home team and `TV<game>.HTM` for the visitors. For example, `20252026/TH020001.HTM` is regular-season game 1 of 2025-26.
- The event summary (`ES<game>.HTM`) in the same folder, with TOI, shifts, average shift, and power play, shorthanded, and even-strength TOI for each player.
- The game's box score in the Game Center, which also gives TOI and shift counts.

The shift report gives each shift's start, end, and duration, and a table by period with columns for shifts, average shift, TOI, even strength, power play, and shorthanded time. Every time is `mm:ss` text.

Follow these steps to load TOI:

1. Convert each `mm:ss` value to decimal minutes: minutes plus seconds divided by 60. `13:59` is 13.98 minutes.
2. Check the conversion on one row by hand. A spreadsheet may read `13:59` as 13 hours and 59 minutes.
3. Keep the even-strength, power play, and shorthanded parts in their own columns.
4. Check that the three parts add up to total TOI. Allow a second per period for rounding. This tolerance is this file's choice.
5. Match players to your athlete IDs by name and sweater number. Names in league reports can differ from your roster.

## Use speed thresholds built for skating

Do not apply a running speed threshold to skating. A threshold set from running studies measures a different thing on ice. The lowest EDGE burst band already starts at 8.05 m/s.

Fixed speed zones can misrepresent skating. In varsity hockey, fixed zones may overestimate skating at very slow, very fast, and sprint speeds, and underestimate it at slow and moderate speeds. The authors recommend zones set relative to each player (Gamble et al., 2022). Ask the user which zones they use. Do not pick one.

## Divide by the right minutes

Per-minute values in hockey use different denominators. Some divide by time on ice. Others divide by the whole session, including the bench and intermissions. Time on ice is shorter than the session, so the same load gives a larger value per TOI minute. In one study, PlayerLoad per minute was 6.26 ± 0.59 AU per minute of shift time and 1.95 ± 0.36 AU per minute of the whole 20-minute period (Perez et al., 2022).

Always state which minutes a per-minute value uses. Never compare a per-TOI value with a per-session value.

## Read wearable inertial data on ice

Wearable inertial data on ice has these limits:

- PlayerLoad test-retest variation in collegiate hockey ranged from 2.2% to 26.6% across nine tasks, and was 26.6% on a repeated shift circuit (Van Iterson et al., 2017).
- PlayerLoad can change when the unit changes orientation, not only when the player works harder. In one small study, PlayerLoad values were about 2.6 to 3 times higher than a second accelerometer measure, Accel'Rate, which the authors found less sensitive to sensor rotation (Perez et al., 2022).
- One study measured stride timing and stride length with sensors on the skates and pelvis (Khandan et al., 2022). No source here tests a unit on the upper back for these measures.
- Local positioning measured peak speed and early acceleration well, with the tag fixed to the back of the shoulder pads each time (Gamble et al., 2023). Other placements were not tested.

Vendors define their own hockey metrics, such as stride and bout counts. Read the device reference for the vendor. If the export uses a hockey metric that no reference file defines, ask the user for the vendor's definition. Do not guess it.

## Expect position and situation differences

Compare players only with others in the same role, or with their own history:

- Defensemen covered 29% more total distance, but forwards did 54% more high-intensity skating per minute, in top-class match play (Lignell et al., 2018).
- Defensemen had lower load per minute than forwards, with similar total load, in professional hockey (Allard et al., 2022).
- Skating speed differed between even strength, power play, and penalty kill, for both defense and forwards (Douglas & Kennedy, 2020).
- Skating intensity fell in period 3 (Douglas & Kennedy, 2020).

## Compare across systems only with care

No published study compares NHL tracking distance or speed with wearable accelerometer load. Show league tracking values and wearable values in separate columns. Do not add them, average them, or read a difference between them as a change in the athlete.

When some players did not wear a device, the `load-and-wellness` skill covers how to estimate their load from time on ice, if it is installed. Do not use tracking distance as a stand-in for a missing PlayerLoad or TRIMP.

## Know the wearable rules before you plan

Wearable use in NHL games is voluntary, under an agreement between the NHL and the NHL Players' Association that is separate from the collective bargaining agreement. Players can ask for a copy of their data and can ask teams to delete it (Daily Faceoff, 2024). The agreement itself is not public. Rules in other leagues differ. Ask the user what their league allows. Do not state it for them.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with ice hockey data:

- Applying a running high-speed threshold, such as one in m/s from a soccer study, to skating speed.
- Reading `mm:ss` time on ice as `hh:mm`.
- Dividing by session length when the user means time on ice, or the reverse.
- Treating league tracking distance and wearable distance as the same measure.
- Using tracking data to fill a missing PlayerLoad.
- Comparing a defenseman's per-minute load with a forward's.
- Stating a definition for an EDGE speed burst, which the NHL does not publish.
- Telling the user what their league allows for in-game wearables.

## Example request

> I have NHL EDGE skating distance and our Catapult PlayerLoad for last night's game, plus TOI from the game report. Build me a per-player table with load per minute of ice time.

## Check the result

Run these checks:

- Unit check: speeds are in one unit, and every threshold is in the same unit as the data.
- Denominator check: every per-minute value names its minutes, TOI or session, and no column mixes them.
- TOI check: even-strength, power play, and shorthanded TOI add up to total TOI for each player.
- Source check: tracking values and wearable values sit in separate columns, with the source named.
- Position check: comparisons stay within a position, or with the athlete's own history.
- Count check: the number of players and games matches the input. State both counts.

## Sources

This file draws on these sources:

- Allard P, Martinez R, Deguire S, Tremblay J. In-season session training load relative to match load in professional ice hockey. J Strength Cond Res. 2022;36(2):486-492. https://doi.org/10.1519/JSC.0000000000003490 Read in abstract form only, 2026-10-05.
- Daily Faceoff. Seravalli F. NHLPA reminds players of their right to control or destroy wearable tech data. 2024-04-30. https://www.dailyfaceoff.com/news/nhlpa-reminds-players-of-their-right-to-control-or-destroy-wearable-tech-data Read on 2026-10-05. Not peer reviewed. Quotes an NHL Players' Association spokesperson.
- Douglas AS, Kennedy CR. Tracking in-match movement demands using local positioning system in world-class men's ice hockey. J Strength Cond Res. 2020;34(3):639-646. https://doi.org/10.1519/JSC.0000000000003414 Read in abstract form only, 2026-10-05.
- Gamble ASD, Bigg JL, Nyman DLE, Spriet LL. Local positioning system-derived external load of female and male varsity ice hockey players during regular season games. Front Physiol. 2022;13:831723. https://doi.org/10.3389/fphys.2022.831723 Full text read on 2026-10-05.
- Gamble ASD, Bigg JL, Pignanelli C, Nyman DLE, Burr JF, Spriet LL. Reliability and validity of an indoor local positioning system for measuring external load in ice hockey players. Eur J Sport Sci. 2023;23(3):311-318. https://doi.org/10.1080/17461391.2022.2032371 Read in abstract form only, 2026-10-05.
- Khandan A, Fathian R, Carey JP, Rouhani H. Measurement of temporal and spatial parameters of ice hockey skating using a wearable system. Sci Rep. 2022;12:22280. https://doi.org/10.1038/s41598-022-26777-9 Read in abstract form only, 2026-10-05.
- Lignell E, Fransson D, Krustrup P, Mohr M. Analysis of high-intensity skating in top-class ice hockey match-play in relation to training status and muscle damage. J Strength Cond Res. 2018;32(5):1303-1310. https://doi.org/10.1519/JSC.0000000000001999 Read in abstract form only, 2026-10-05.
- NHL. NHL EDGE data feed, skater skating speed and skating distance detail. https://api-web.nhle.com/v1/edge/skater-skating-speed-detail/8478402/now and https://api-web.nhle.com/v1/edge/skater-skating-distance-detail/8478402/now Read on 2026-10-05. League data feed with no published documentation. Used for field names and units only.
- NHL.com. NHL EDGE launches website for puck and player tracking data. 2023-10-23. https://www.nhl.com/news/nhl-edge-launches-website-for-puck-and-player-tracking-data Read on 2026-10-05. League document.
- NHL.com. Time on ice shift report, game 2025020001. https://www.nhl.com/scores/htmlreports/20252026/TH020001.HTM Read on 2026-10-05. League document. Used for the report format only.
- Perez J, Brocherie F, Couturier A, Guilhem G. International matches elicit stable mechanical workload in high-level female ice hockey. Biol Sport. 2022;39(4):857-864. https://doi.org/10.5114/biolsport.2022.109455 Full text read on 2026-10-05 at https://pmc.ncbi.nlm.nih.gov/articles/PMC9536379/.
- SMT. How NHL's sensor-embedded puck allows for better broadcast statistics and graphics. Reposted from SportTechie, 2022-10-10. https://smt.com/how-nhls-sensor-embedded-puck-allows-for-better-broadcast-statistics-and-graphics-new-types-of-wagers-more Read on 2026-10-05. Vendor document.
- Van Iterson EH, Fitzgerald JS, Dietz CC, Snyder EM, Peterson BJ. Reliability of triaxial accelerometry for measuring load in men's collegiate ice hockey. J Strength Cond Res. 2017;31(5):1305-1312. https://doi.org/10.1519/JSC.0000000000001611 Read in abstract form only, 2026-10-05.
- Vigh-Larsen JF, Mohr M. The physiology of ice hockey performance: an update. Scand J Med Sci Sports. 2024;34(1):e14284. https://doi.org/10.1111/sms.14284 Read in abstract form only, 2026-10-05.
