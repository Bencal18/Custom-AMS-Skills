# Swim volume and bowling volume

Last checked: 2026-10-07

## What it measures

Swim volume is the distance an athlete swam in a session, day, or week, split by stroke and intensity zone when the log holds them. Bowling volume is the number of balls a cricket bowler bowled in matches and training, per day and per week.

## Formula

Use these formulas for one athlete and one session. Use the totals method in [count-totals.md](count-totals.md) for days, weeks, and rolling windows:

```text
swim distance (m)          = sum of set distances in m
set distance (m)           = set distance (yd) × 0.9144, for yard pools
zone share (%)             = distance in one zone / swim distance × 100
valid balls                = whole overs × 6 + balls in the part over
```

Define every term in the formula:

- `set distance`: the distance swum in one set, such as 8 × 100 = 800.
- `0.9144`: meters in one yard. US college pools are often measured in yards. Never add yards to meters.
- `zone`: an intensity zone from the coach's own zone system. This skill does not define zones.
- `stroke`: the stroke or set type in the log, such as freestyle, backstroke, individual medley, kick, or pull.
- `over`: 6 valid balls. Under the Laws of Cricket, a wide or a no ball does not count as one of the 6 balls of the over (MCC Law 17).
- `whole overs` and `balls in the part over`: a scorecard can write 4 overs and 3 balls as `4.3`. That is 27 valid balls, not 4.3 × 6.

### What each count misses

Each count sees only part of the work:

- **Swim distance.** In an international survey of 31 people working in competitive swimming programs, 84% used training load monitoring. Swim volume (96%) and session RPE (92%) were the methods used most often (Barry et al., 2022). Distance alone does not show stroke or intensity. Log both when you can.
- **Dryland and competition.** Swim distance leaves out dryland training. Barry et al. (2022) suggest one monitoring system across pool training, dryland training, and competition. Keep dryland load as its own measure, such as session RPE load, not as extra meters.
- **Balls in the scorecard.** A scorecard shows overs in matches only. It leaves out nets, middle practice, and warm-up deliveries.
- **Balls bowled and logbooks.** A systematic review found bowling frequency was usually measured as balls bowled in a session or match, or in a logbook (Constable et al., 2021). It reported that both balls bowled and logbooks have been shown to be unreliable, mainly because of adherence issues in reporting. It also noted that counts without a measure of intensity give only an overview of bowling demand, and that a count does not reflect differences in technique, running speed, or body size between bowlers.

### Calculate it in a spreadsheet

For swimming, put one row per set with the athlete in `A`, the date in `B`, the stroke in `C`, the zone in `D`, the distance in `E`, and the unit (`yd` or `m`) in `F`. Use these formulas:

```text
Set distance (m), G2:      =IF(OR(E2="",F2=""),"",IF(F2="yd",E2*0.9144,IF(F2="m",E2,"check unit")))
```

In a session summary, put the athlete in `I2`, the date in `J2`, and a zone name in `K2`. Use these formulas:

```text
Sets in session, L2:          =COUNTIFS(A:A,I2,B:B,J2)
Sets with a distance, M2:     =COUNTIFS(A:A,I2,B:B,J2,G:G,">=0")
Session distance (m), N2:     =IF(OR(L2=0,M2<L2),"",SUMIFS(G:G,A:A,I2,B:B,J2))
Zone distance (m), O2:        =SUMIFS(G:G,A:A,I2,B:B,J2,D:D,K2)
Zone share (%), P2:           =IF(OR(N2="",N2=0),"",O2/N2*100)
```

`">=0"` counts only sets with a number in meters, so a blank distance or an unknown unit leaves the session total blank.

For cricket, put the whole overs in `B2` and the balls in the part over in `C2`. If the scorecard gives `4.3` in one cell, split it into `4` and `3` first:

```text
Whole overs from 4.3 in A2, B2:    =INT(A2)
Part-over balls from 4.3, C2:      =ROUND(MOD(A2,1)*10,0)
Valid balls, D2:                   =IF(OR(B2="",C2=""),"",IF(C2>5,"check",B2*6+C2))
```

A part-over value above 5 cannot exist in a 6-ball over, so the formula returns `check`. Ask the user how the log writes overs before you split them.

### Calculate it in Power BI and Tableau

For swimming, both versions assume a table `swim_sets` with one row per set: `athlete_id`, `measure_date`, `session_id`, `stroke`, `zone`, `distance`, and `unit`. For cricket, both assume a table `bowling_log` with one row per spell or net session: `athlete_id`, `measure_date`, `session_type` (`match` or `training`), `whole_overs`, `part_over_balls`. For rolling totals, build daily totals as in [count-totals.md](count-totals.md).

In Power BI, add this calculated column to `swim_sets`, then use the measures:

```text
distance_m (calculated column) =
SWITCH (
    swim_sets[unit],
    "yd", swim_sets[distance] * 0.9144,
    "m", swim_sets[distance],
    BLANK ()
)

Swim distance (m) =
VAR sets = COUNTROWS ( swim_sets )
VAR filled = COUNT ( swim_sets[distance_m] )
RETURN IF ( sets > 0 && filled = sets, SUM ( swim_sets[distance_m] ) )

Zone share (%) =
VAR all_zones = CALCULATE ( [Swim distance (m)], REMOVEFILTERS ( swim_sets[zone] ) )
RETURN IF ( NOT ISBLANK ( all_zones ) && all_zones > 0, [Swim distance (m)] / all_zones * 100 )
```

Put `zone` in the visual for `Zone share (%)`. A set with a blank distance or an unknown unit blanks the session total.

For cricket, add these calculated columns to `bowling_log`, then sum them:

```text
valid_balls (calculated column) =
IF (
    ISBLANK ( bowling_log[whole_overs] ) || ISBLANK ( bowling_log[part_over_balls] )
        || bowling_log[part_over_balls] > 5,
    BLANK (),
    bowling_log[whole_overs] * 6 + bowling_log[part_over_balls]
)

Valid balls bowled =
VAR spells = COUNTROWS ( bowling_log )
VAR filled = COUNT ( bowling_log[valid_balls] )
RETURN IF ( spells > 0 && filled = spells, SUM ( bowling_log[valid_balls] ) )
```

These are calculated columns because each input sits on the same row and does not change with filters.

In Tableau, use these calculations:

```text
Set distance (m) (row-level):
IF [unit] = "yd" THEN [distance] * 0.9144
ELSEIF [unit] = "m" THEN [distance]
END

Swim distance (m) (aggregate):
IF COUNT([Set distance (m)]) < COUNT([session_id]) THEN NULL
ELSE SUM([Set distance (m)])
END

Zone share (%) (aggregate, with zone on the view, daily view shown):
SUM([Set distance (m)]) / MIN({ FIXED [athlete_id], [measure_date] : SUM([Set distance (m)]) }) * 100

Valid balls (row-level):
IF ISNULL([whole_overs]) OR ISNULL([part_over_balls]) OR [part_over_balls] > 5 THEN NULL
ELSE [whole_overs] * 6 + [part_over_balls]
END

Valid balls bowled (aggregate):
IF COUNT([Valid balls]) < COUNT([session_type]) THEN NULL
ELSE SUM([Valid balls])
END
```

Set the `FIXED` dimensions in `Zone share (%)` to match the view, leaving out `zone`. For a daily view, use `[athlete_id], [measure_date]`. For a session view, add `[session_id]`. A level finer than the view gives the share of one session, not of the day.

`COUNT` ignores nulls, so a set or spell with a missing value makes the count lower than the number of rows, and the total returns null. A null in any input gives a null row-level sum.

### Calculate it in Python

```python
swim["distance_m"] = swim["distance"].where(swim["unit"].eq("m"),
                     swim["distance"] * 0.9144).where(swim["unit"].isin(["m", "yd"]))
sess = swim.groupby(["athlete_id", "date", "session_id"])["distance_m"].sum(min_count=1)
missing = swim.groupby(["athlete_id", "date", "session_id"])["distance_m"].apply(lambda x: x.isna().any())
sess[missing] = float("nan")

bowl["valid_balls"] = (bowl["whole_overs"] * 6 + bowl["part_over_balls"]).where(bowl["part_over_balls"] <= 5)
```

## Calculate the volume

Follow these steps to calculate swim or bowling volume from raw inputs:

1. Ask which sport and log the data came from, and which unit the pool uses.
2. For swimming, convert every set to meters, and keep the stroke and zone columns.
3. For swimming, add the sets for each session, day, and week. Report distance by zone and by stroke when the log holds them.
4. For cricket, ask how overs are written, and split them into whole overs and part-over balls.
5. For cricket, calculate valid balls. Keep match balls and training balls in separate count types.
6. Mark days with activity but no record as missing, not 0.
7. Build daily, weekly, and rolling totals with [count-totals.md](count-totals.md).

## Worked example

One college swimmer's Monday session in a yard pool:

| Stroke or type | Zone | Distance (yd) |
|---|---|---|
| Freestyle | zone 1 | 800 |
| Freestyle | zone 2 | 2000 |
| Backstroke | zone 2 | 600 |
| Individual medley | zone 3 | 800 |
| Freestyle | zone 4 | 500 |
| Kick | zone 1 | 300 |

Work through the session:

- Total: 5000 yd × 0.9144 = 4572.0 m.
- By zone: zone 1 1100 yd (22.0%), zone 2 2600 yd (52.0%), zone 3 800 yd (16.0%), and zone 4 500 yd (10.0%).
- By stroke or type: freestyle 3300 yd, backstroke 600 yd, individual medley 800 yd, and kick 300 yd.

The wrong method adds this session's 5000 yd to a 5000 m long-course session as 10000 "meters". The true total is 4572.0 + 5000 = 9572.0 m.

One fast bowler's day: a match spell of `4.3` overs, then a net session of 36 balls.

- Valid balls in the match: 4 × 6 + 3 = 27.
- Day total: 27 match balls + 36 training balls = 63 balls.

The wrong method reads `4.3` as a decimal: 4.3 × 6 = 25.8 balls. A second wrong method takes 27 balls from the scorecard as the day's bowling, missing 36 of 63 balls.

## What changes the number

These choices change the result even when the athlete's work does not:

- Pool unit. 5000 yd is 4572.0 m.
- Zone system. Two zone systems split the same session differently. Name the system.
- Overs notation. Reading `4.3` as a decimal gave 25.8 balls instead of 27.
- Training balls. Match counts alone gave 27 of the day's 63 balls in the worked example.

## Units and typical range

Report swim distance in meters, with the pool unit named. Report bowling volume as a whole number of balls, with overs beside it. Name the count type, source, and window with every total.

Swim distance and bowling counts have no population range that applies across ages, events, roles, and training phases. Compare each athlete with their own history from the same log.

## Data you need

Collect this data:

- Source: the swim log and the pool unit. For cricket, the scorebook for matches and a coach or observer tally for training.
- Sampling: every set or spell, every session.
- Minimum data: one complete week before a weekly total means anything. A trend needs several complete weeks from the same log.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with swim and bowling volume:

- Adding yards and meters.
- Reading overs written as `4.3` as a decimal.
- Taking the scorecard as the bowler's whole day, without training balls.
- Treating a bowler's own logbook as an exact count. Constable et al. (2021) report that logbooks have been shown to be unreliable.
- Adding dryland work to swim distance.

## Example request

> My swim log has yards for college season and meters for summer long course. Give me weekly distance per swimmer in meters, and the share in each of my zones.

## Check the result

Run these checks:

- Recompute one session total by hand, with the unit conversion.
- Confirm that zone shares add to 100% for each session.
- Confirm that no part-over value is above 5.
- Confirm that match and training balls stay in separate count types until you add them for a day total.

## Sources

This file draws on these sources:

- Barry L, Lyons M, McCreesh K, Powell C, Comyns T. International survey of training load monitoring practices in competitive swimming: how, what and why not? Physical Therapy in Sport. 2022;53:51-59. https://doi.org/10.1016/j.ptsp.2021.11.005 (abstract, accessed 2026-10-07)
- Constable M, Wundersitz D, Bini R, Kingsley M. Quantification of the demands of cricket bowling and the relationship to injury risk: a systematic review. BMC Sports Science, Medicine and Rehabilitation. 2021;13(1):109. https://doi.org/10.1186/s13102-021-00335-8 (accessed 2026-10-07)
- Marylebone Cricket Club. The Laws of Cricket. Law 17: The over. https://lawsofcricket.lords.org/laws-of-cricket/the-over-scoring-runs-dead-ball-and-extras/the-over (accessed 2026-10-07)
