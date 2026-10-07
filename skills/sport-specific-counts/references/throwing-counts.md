# Pitch and throw counts

Last checked: 2026-10-07

## What it measures

Pitch and throw counts show how many times an athlete threw, split by the kind of throw and where the count came from. Arm-sensor values add a device's estimate of how hard each throw was.

## Formula

Use these formulas for one athlete and one day. Use the totals method in [count-totals.md](count-totals.md) for weeks and rolling windows:

```text
all logged throws (count)   = game pitches + bullpen pitches + warm-up throws
                              + between-innings throws + practice throws
game share (%)              = game pitches / all logged throws × 100
difference from limit       = count − limit the coach supplied
```

Define every term in the formula:

- `game pitches`: pitches thrown to a batter in a game, from the official scorebook or pitch chart. This is the usual "pitch count".
- `bullpen pitches`: pitches thrown off a mound in a bullpen session, outside a game.
- `warm-up throws`: throws before a game or practice, including pregame bullpen warm-up if the log does not count it as a bullpen.
- `between-innings throws`: warm-up pitches between innings in a game.
- `practice throws`: every other throw in practice, such as catch, long toss, flat-ground work, and fielding throws. Split them into more types if the log allows, such as `long_toss_throws`.
- `sensor throws`: every throw an arm-worn sensor detected. It already includes pitches. It is a separate count type, never a part of `all logged throws`.
- `limit the coach supplied`: a pitch or throw number the coach gives, such as a team rule. This skill does not supply one.

Name every count type in the output. Do not call `all logged throws` a pitch count. The grouping of types into `all logged throws`, and the game share, are this skill's choices, not published metrics.

### What each count misses

Each count type sees only part of an athlete's throwing:

- **Game pitch count.** It counts only pitches to batters. Dowling et al. (2020) note that workload standards built on pitch counts leave out warm-up throws, plyometric ball work, long toss, bullpens, flat-ground throws, and pitches between innings.
- **Game pitch count against all throws.** In 19 youth players aged 11 and 12, tracked with an elbow-sleeve sensor for one season, the mean official pitch count per player was 168.1 ± 122.4. The sensor recorded 1666.2 ± 642.2 total throws and 576.9 ± 329.3 high-effort throws per player (Wahl et al., 2020).
- **Pitching days.** In 11 players aged 10 and 11, with a sensor above the middle of the upper arm, game pitches were 36 ± 18 on a pitching day, or 23% of that day's 158 ± 106 total throws. On game days without pitching, players made 119 ± 102 throws (Freehill et al., 2023).
- **Self-reported throw counts.** In 26 elite cricket players over 12 training sessions, self-reported and observed overarm throws correlated at rho = 0.65. Only 22% of players reported within 10% of the observed count. The mean absolute error was 11.17 ± 9.77 throws, and the mean relative error was 24.76 ± 16.04%. Players who reported more than 1 day after training had a mean relative error of 36% (Hoyne et al., 2022). Treat a self-reported throw count as an estimate, not a count. Label it `self_report`.
- **Sensor throws.** A sensor counts only while it is worn, charged, and synced. A day without the sensor is missing, not 0. The sensor's rule for what counts as a throw, and how it splits throws into intensity groups, belongs to that device. Freehill et al. (2023) split throws into low, medium, and high intensity with their own algorithm. Compare intensity groups only within one device and setting.

### Arm-sensor workload values

Some arm sensors report a value per throw, such as an estimate of elbow torque, arm speed, or a workload score. Follow these rules for every such value:

- Never compare values across sensor placements. Agresta et al. (2022) put sensors on the trunk, the throwing upper arm, and the throwing forearm of 10 college pitchers in one bullpen. Sensor location changed every workload estimate. For fastballs, peak resultant acceleration was 160.5 ± 113.4 m/s² at the trunk, 1046.6 ± 184.0 m/s² at the upper arm, and 1288.7 ± 184.1 m/s² at the forearm.
- Never compare values across devices or vendors. Each device uses its own placement and calculation.
- Keep the placement the same every session. Lizzio et al. (2020) describe placing one sensor at the maker's stated spot below the inside of the elbow. They write that its reliability depends almost entirely on a consistent sensor location. They found that a loose sleeve slides down the arm after a few pitches, so they checked the position every 3 to 4 pitches.
- Treat the value as the device's estimate, not a measured force. In 10 high school pitchers, one arm-sleeve sensor gave elbow varus torque that differed from marker-based motion capture by 9.4 ± 12.0 N·m, and it reported lower values than motion capture. The authors suggest it may still be useful for tracking one thrower against their own values (Camp et al., 2021).
- Label every value with the device, the placement, and the vendor's metric name. Use the device's own definition. Do not rebuild the score from raw data.

### Compare a count with a limit the coach supplies

Pitch count limits by age exist as injury-prevention guidelines (Dowling et al., 2020). A systematic review found little agreement on the scientific basis for many pitch count recommendations, and conflicting evidence for college and professional pitchers (Bakshi et al., 2020).

Follow these rules when the coach asks for a comparison:

- Use only a limit the coach gives you. Do not look one up or supply one.
- Name the count type the limit applies to, such as game pitches. Compare it only with that count type.
- Report the count, the limit, and the difference in plain words, such as "78 game pitches, 7 below the limit of 85 you set".
- Do not say what the difference means for injury, rest, or availability. Do not suggest rest days.

### Calculate it in a spreadsheet

Use one row per athlete per day. Put the daily counts in columns `C` to `G`: warm-up, practice, bullpen, between-innings, and game. Put sensor throws in `H`. Put the coach's game pitch limit in `K1`. Use these formulas:

```text
All logged throws, I2:          =IF(COUNT(C2:G2)<5,"",SUM(C2:G2))
Game share (%), J2:             =IF(OR(I2="",I2=0),"",G2/I2*100)
Sensor minus logged, L2:        =IF(OR(H2="",I2=""),"",H2-I2)
Difference from limit, M2:      =IF(OR(G2="",$K$1=""),"",G2-$K$1)
Limit report, N2:               =IF(M2="","",G2&" game pitches, "&IF(M2=0,"at",ABS(M2)&IF(M2>0," above"," below"))&" the limit of "&$K$1&" you set")
```

`COUNT(C2:G2)<5` keeps the total blank when any count type is blank, so a missing type does not shrink the total. `L2` is a cross-check, not a validity test. Ask about a day when the two differ a lot.

### Calculate it in Power BI and Tableau

Both versions assume daily totals in the `measures` table, one row per athlete, day, and count type, as in [count-totals.md](count-totals.md). Use the `measure_name` values `daily_warmup_throws`, `daily_practice_throws`, `daily_bullpen_pitches`, `daily_between_innings_throws`, `daily_game_pitches`, and `daily_sensor_throws`, all with `unit` `count`. Store the coach's limit in a one-row table `coach_limit` with a column `game_pitch_limit`.

In Power BI, put `athletes[athlete_id]` and `dates[date]` in the visual. Use these measures:

```text
All logged throws =
VAR types =
    { "daily_warmup_throws", "daily_practice_throws", "daily_bullpen_pitches",
      "daily_between_innings_throws", "daily_game_pitches" }
VAR logged_rows =
    CALCULATETABLE (
        measures,
        measures[measure_name] IN types,
        measures[unit] = "count",
        measures[status] = "ok"
    )
VAR filled = FILTER ( logged_rows, NOT ISBLANK ( measures[value] ) )
VAR type_count = COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( filled, "t", measures[measure_name] ) ) )
RETURN
    IF ( COUNTROWS ( filled ) = 5 && type_count = 5, SUMX ( filled, measures[value] ) )

Game pitches =
IF (
    CALCULATE ( COUNTROWS ( measures ), measures[measure_name] = "daily_game_pitches" ) = 1,
    CALCULATE (
        MAX ( measures[value] ),
        measures[measure_name] = "daily_game_pitches",
        measures[unit] = "count",
        measures[status] = "ok"
    )
)

Game share (%) =
VAR t = [All logged throws]
RETURN IF ( NOT ISBLANK ( t ) && t > 0, [Game pitches] / t * 100 )

Difference from limit =
VAR c = [Game pitches]
VAR l = SELECTEDVALUE ( coach_limit[game_pitch_limit] )
RETURN IF ( NOT ISBLANK ( c ) && NOT ISBLANK ( l ), c - l )
```

`All logged throws` needs exactly one filled row for each of the 5 types, so it works one athlete and one day at a time. A missing type or a duplicate row gives a blank. For weeks and rolling windows, build `daily_all_logged_throws` before import and use [count-totals.md](count-totals.md). These measures return numbers. Write the plain-words limit report from them, as the spreadsheet version does.

In Tableau, put `athlete_id` and `measure_date` on the view. Use these aggregate calculations:

```text
Logged throw types filled:
COUNTD(IF [measure_name] IN ("daily_warmup_throws", "daily_practice_throws", "daily_bullpen_pitches",
  "daily_between_innings_throws", "daily_game_pitches") AND [unit] = "count" AND [status] = "ok"
  AND NOT ISNULL([value]) THEN [measure_name] END)

Logged throw rows filled:
COUNT(IF [measure_name] IN ("daily_warmup_throws", "daily_practice_throws", "daily_bullpen_pitches",
  "daily_between_innings_throws", "daily_game_pitches") AND [unit] = "count" AND [status] = "ok"
  AND NOT ISNULL([value]) THEN [value] END)

All logged throws:
IF [Logged throw types filled] = 5 AND [Logged throw rows filled] = 5
THEN SUM(IF [measure_name] IN ("daily_warmup_throws", "daily_practice_throws", "daily_bullpen_pitches",
  "daily_between_innings_throws", "daily_game_pitches") AND [unit] = "count" AND [status] = "ok"
  THEN [value] END)
END

Game pitches:
MAX(IF [measure_name] = "daily_game_pitches" AND [unit] = "count" AND [status] = "ok" THEN [value] END)

Game share (%):
IF [All logged throws] > 0 THEN [Game pitches] / [All logged throws] * 100 END

Difference from limit:
[Game pitches] - [Game pitch limit]
```

Make `Game pitch limit` a Tableau parameter that the coach sets. A null game pitch count gives a null difference.

### Calculate it in Python

```python
types = ["warmup_throws", "practice_throws", "bullpen_pitches",
         "between_innings_throws", "game_pitches"]
# One row per athlete and date; NaN when a type was not recorded.
df["all_logged_throws"] = df[types].sum(axis=1, min_count=len(types))
df["game_share_pct"] = df["game_pitches"] / df["all_logged_throws"].where(df["all_logged_throws"] > 0) * 100
df["sensor_minus_logged"] = df["sensor_throws"] - df["all_logged_throws"]
df["diff_from_coach_limit"] = df["game_pitches"] - coach_limit  # coach_limit comes from the coach
```

## Calculate the counts

Follow these steps to calculate the counts from raw inputs:

1. Ask which count types the log holds, and where each comes from: scorebook, coach or observer tally, video, sensor, or the athlete's own report.
2. Put each count type in its own column or `measure_name`.
3. Label self-reported counts as `self_report`.
4. Build one row per athlete per day for each count type, with `0` on rest days and a blank on unrecorded days. Follow [count-totals.md](count-totals.md).
5. Add the logged types to get all logged throws. Keep sensor throws separate.
6. Calculate the game share of all logged throws.
7. Calculate daily, weekly, and rolling totals for each count type with [count-totals.md](count-totals.md).
8. If the coach supplies a limit, compare only the matching count type with it, and report the difference in plain words.
9. For arm-sensor values, confirm that one device and one placement were used for every value in the comparison.

## Worked example

One pitcher's week starts Monday 2026-08-03. The coach logs five count types. The pitcher wears an arm sensor, but not on Thursday. The coach's limit for game pitches is 85.

| Date | Warm-up | Practice | Bullpen | Between innings | Game | All logged | Sensor |
|---|---|---|---|---|---|---|---|
| 2026-08-03 | 20 | 25 | 0 | 0 | 0 | 45 | 48 |
| 2026-08-04 | 20 | 15 | 30 | 0 | 0 | 65 | 67 |
| 2026-08-05 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026-08-06 | 20 | 30 | 0 | 0 | 0 | 50 | missing |
| 2026-08-07 | 15 | 20 | 0 | 0 | 0 | 35 | 37 |
| 2026-08-08 | 30 | 0 | 0 | 24 | 78 | 132 | 138 |
| 2026-08-09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Work through the week:

- Weekly totals by type: warm-up 105, practice 90, bullpen 30, between innings 24, and game 78.
- All logged throws: 105 + 90 + 30 + 24 + 78 = 327 throws, 7 of 7 days.
- Game share: 78 / 327 × 100 = 23.9%. The game pitch count shows less than a quarter of the logged throws.
- Sensor throws: 48 + 67 + 0 + 37 + 138 + 0 = 290, 6 of 7 days. Report it as incomplete. Do not add Thursday's 50 logged throws to it.
- Sensor minus logged on the 6 sensor days: 290 − 277 = 13 throws. Ask the coach which throws the log did not catch, such as extra catch play.
- Limit comparison for Saturday: "78 game pitches, 7 below the limit of 85 you set."

The wrong method adds sensor throws and logged throws: 290 + 327 = 617 throws, which counts most throws twice.

## What changes the number

These choices change the result even when the athlete's throwing does not:

- Count type. In the worked example, the week reads 78 throws from game pitches alone and 327 from all logged throws.
- Source. A self-reported count can be off by about a quarter on average (Hoyne et al., 2022). A sensor count misses any day the sensor was not worn.
- Sensor placement. A forearm, upper arm, or trunk sensor gives different workload values for the same pitches (Agresta et al., 2022).
- Sensor position within a session. A sleeve that slides down the arm moves the sensor (Lizzio et al., 2020).
- Intensity grouping. Each device and study sets its own rule for what counts as a high-effort or high-intensity throw (Wahl et al., 2020; Freehill et al., 2023).
- Where warm-up pitches go. Pregame bullpen pitches logged as `bullpen_pitches` on one day and `warmup_throws` on another change both totals.

## Units and typical range

Report every count as a whole number of throws or pitches, with its count type, source, and window. Report arm-sensor values in the device's units, with the device and placement.

Throw counts have no population range that applies across ages, positions, and levels. These published figures describe single studies. Use them as context for what a count can miss, not to judge an athlete:

| Population and setting | Figure | Source |
|---|---|---|
| Youth players aged 11 and 12, one season, elbow-sleeve sensor | Official pitch count 168.1 ± 122.4; sensor total throws 1666.2 ± 642.2; high-effort throws 576.9 ± 329.3, per player (mean ± SD) | Wahl et al., 2020 |
| Youth players aged 10 and 11, game days, sensor above the middle of the upper arm | Pitching days: 36 ± 18 pitches and 158 ± 106 total throws. Non-pitching game days: 119 ± 102 throws (mean ± SD) | Freehill et al., 2023 |
| Elite cricket players, training, self-report against observation | 22% of players within 10% of the observed count; mean relative error 24.76 ± 16.04% | Hoyne et al., 2022 |

## Data you need

Collect this data:

- Source: a pitch chart or scorebook for game pitches, a session log for other throws, and the sensor export if one is used.
- Sampling: one count per athlete, session, and count type. For a sensor, every throw on every day it is worn.
- Minimum data: one week of complete days before a weekly total means anything. A trend needs several complete weeks from the same sources.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with throw counts:

- Calling the game pitch count the athlete's throwing load. It leaves out most throws (Dowling et al., 2020; Wahl et al., 2020).
- Adding sensor throws to logged throws. The sensor already counts the logged throws.
- Treating a self-reported count as exact. Label it and report it apart from observed counts.
- Comparing arm-sensor values across placements, devices, or vendors.
- Writing 0 on a day the sensor was not worn.
- Supplying a pitch count limit the coach did not give, or describing a count as safe or risky.

## Example request

> Our pitchers wear an arm sensor and we also keep a pitch chart in games. Can you give me weekly totals for each pitcher and show how much of their throwing the pitch chart misses?

## Check the result

Run these checks:

- Recompute one day's all logged throws and game share by hand.
- Confirm that sensor throws never appear inside all logged throws.
- Confirm that every arm-sensor value in a comparison names the same device and placement.
- Confirm that every limit came from the coach and is named as theirs.

## Sources

This file draws on these sources:

- Dowling B, McNally MP, Chaudhari AMW, Oñate JA. A review of workload-monitoring considerations for baseball pitchers. Journal of Athletic Training. 2020;55(9):911-917. https://doi.org/10.4085/1062-6050-0511-19 (accessed 2026-10-07)
- Bakshi NK, Inclan PM, Kirsch JM, Bedi A, Agresta C, Freehill MT. Current workload recommendations in baseball pitchers: a systematic review. American Journal of Sports Medicine. 2020;48(1):229-241. https://doi.org/10.1177/0363546519831010 (abstract, accessed 2026-10-07)
- Wahl EP, Pidgeon TS, Richard MJ. Youth baseball pitch counts vastly underestimate high-effort throws throughout a season. Journal of Pediatric Orthopaedics. 2020;40(7):e609-e615. https://doi.org/10.1097/BPO.0000000000001520 (abstract, accessed 2026-10-07)
- Freehill MT, Rose MJ, McCollum KA, Agresta C, Cain SM. Game-day pitch and throw count feasibility using a single sensor to quantify workload in youth baseball players. Orthopaedic Journal of Sports Medicine. 2023;11(3):23259671231151450. https://doi.org/10.1177/23259671231151450 (abstract, accessed 2026-10-07)
- Hoyne ZG, Cripps AJ, Mosler AB, Joyce C, Chivers PT, Chipchase R, Murphy MC. Self-reported throwing volumes are not a valid tool for monitoring throwing loads in elite Australian cricket players: an observational cohort study. Journal of Science and Medicine in Sport. 2022;25(10):845-849. https://doi.org/10.1016/j.jsams.2022.06.008 (abstract, accessed 2026-10-07)
- Agresta C, Freehill MT, Zendler J, Giblin G, Cain S. Sensor location matters when estimating player workload for baseball pitching. Sensors. 2022;22(22):9008. https://doi.org/10.3390/s22229008 (accessed 2026-10-07)
- Lizzio VA, Cross AG, Guo EW, Makhni EC. Using wearable technology to evaluate the kinetics and kinematics of the overhead throwing motion in baseball players. Arthroscopy Techniques. 2020;9(9):e1429-e1431. https://doi.org/10.1016/j.eats.2020.06.003 (accessed 2026-10-07)
- Camp CL, Loushin S, Nezlek S, Fiegen AP, Christoffer D, Kaufman K. Are wearable sensors valid and reliable for studying the baseball pitching motion? An independent comparison with marker-based motion capture. American Journal of Sports Medicine. 2021;49(11):3094-3101. https://doi.org/10.1177/03635465211029017 (abstract, accessed 2026-10-07)
