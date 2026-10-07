# Match-day load

Last checked: 2026-10-07

## What it measures

Match-day load labels each training session by its days to or from a match, and expresses the session's load as a percent of the player's own match value for the same measure.

The label uses MD for match day. MD-4 is 4 days before the next match. MD+1 is 1 day after the last match. The percent answers "how much of a match did this session give this player?" It describes the training week. It does not say what the week should be. The coach makes every training decision.

Any measure works when training and matches use the same device, settings, and calculation: total distance, high-speed running, sprint distance, accelerations, decelerations, or a peak from [peak-demands.md](peak-demands.md).

## Formula

Label each session, then divide the session value by the player's match reference:

```text
days_to_next     = next_match_date − session_date, in days
days_since_last  = session_date − last_match_date, in days
label            = "MD"                        on a match date
                 = "MD+" & days_since_last     if days_since_last ≤ post_match_days
                 = "MD-" & days_to_next        otherwise
match_reference  = mean of the player's qualifying match values for the measure
pct_of_match     = session_value ÷ match_reference × 100
week_pct         = Σ session values in the microcycle ÷ match_reference × 100
```

Define every term in the formula:

- `next_match_date`, `last_match_date`: the dates of the next and the last match in the team's fixture list
- `post_match_days`: how many days after a match the coach labels as MD+. In a study of one La Liga reserve team, the day after a match was MD+1 and the rest of the week counted down from MD-4 to MD-1 (Martín-García et al., 2018). Ask the user for their number.
- `session_value`: the player's value for one session, such as total distance in metres
- `match_reference`: the player's match value for the same measure. Choose it with the rules in [Choose the match reference](#choose-the-match-reference).
- `pct_of_match`: the session as a percent of the match reference
- Microcycle: the training days between two matches
- `week_pct`: the microcycle's accumulated load as a percent of the match reference. Baptista et al. (2020) summed the four sessions of each typical week this way.

Store `days_to_next` and `days_since_last` for every session, not only the label. A congested week gives a session two true descriptions, such as MD+1 and MD-2. The two numbers keep both.

The studies cited here calculated the percent in two ways:

- Group ratio: Martín-García et al. (2018) divided the mean training session value by the mean match value, times 100, for the squad or a position.
- Player reference: Baptista et al. (2020) set the average of each variable across 15 tracked matches as 100%, by position.

This file calculates the percent for each player against their own reference. A group ratio and the mean of player percents are different numbers. Name which one you report.

### Choose the match reference

The match reference changes every percent, so choose it on purpose and state it. Use these options:

- Full matches only. Martín-García et al. (2018) excluded players who did not complete a full competitive match.
- A minimum time on the field. Baptista et al. (2020) used matches where a player completed at least 60 minutes in the same position, and extrapolated volume measures from shorter samples to 90 minutes.
- Extrapolation. Volume measures scale as `value × 90 ÷ minutes_played`. This assumes the player kept the same rate for the whole match. The worked example shows how a short appearance can inflate the reference.
- A position reference. Use the mean of the match references of every player in the same position with at least one qualifying match, including this player when they qualify. Use it for a player with no qualifying match, or when the coach asks for one reference per position. Label it as a position reference.
- Number of matches. Use the mean of the player's last qualifying matches, and say how many. A single match gives an unstable reference, because match running varies from match to match (Gregson et al., 2010).

Use a rate measure, such as m/min or a peak per minute, when playing time varies a lot. A rate needs no extrapolation, but it describes intensity, not volume. See [total-distance.md](total-distance.md#formula).

### Handle congested weeks

A congested week has two matches, such as Saturday, Wednesday, and Saturday. It changes the labels and the comparison. Follow these rules:

- Label with the same rule as any other week. With `post_match_days` set to 1, the day after Wednesday is MD+1, and Friday is MD-1.
- Keep a `days_between_matches` column for each microcycle. Compare an MD-2 from a microcycle with 3 days between matches only with other MD-2 sessions from microcycles with 3 days between matches.
- Both studies cited here analyzed only weeks with 6 days between matches (Martín-García et al., 2018; Baptista et al., 2020). Their percents describe that week shape only.
- In a congested week, a player can have two match values. Report each match as 100% of itself, and do not add matches into `week_pct`. Report weekly match load and weekly training load as separate lines.

### Handle players who did not play the full match

Players with little or no match time often do different sessions the next day. In the La Liga study, players with more than 60 minutes did a recovery session (MD+1R). Players with less than 60 minutes did a compensatory session that replicated competition loads (MD+1C) (Martín-García et al., 2018). The 60 minute split is that study's setting.

Follow these rules:

- Label each MD+1 session by its type as well as its day, such as MD+1 recovery or MD+1 compensatory.
- Compare a player's compensatory session with their own match reference, not with the minutes they played in the last match.
- Show minutes played next to every match value.

### Handle goalkeepers

Both studies cited here left goalkeepers out of the analysis. Martín-García et al. (2018) studied outfield players. Baptista et al. (2020) studied centre-backs, wing-backs, centre midfielders, and centre forwards. Neither study gives a percent for goalkeepers.

Follow these rules:

- Compare goalkeepers only with their own match values. Never put a goalkeeper in an outfield position group or squad average.
- Goalkeepers cover little high-speed or sprint distance. A small match value makes the percent swing. In the worked example, 10 m more high-speed distance moves a goalkeeper from 64.3% to 135.7%.
- Ask the user for a minimum match reference for each measure. Below it, show the raw values and no percent.

### Use this spreadsheet method

Put the fixture list on a sheet named `matches`, with match dates in column `A`. Put sessions on another sheet, with one row per player and session. Use these columns and cells:

- Column `A`: `session_date`
- Column `B`: `athlete_id`
- Column `C`: `session_type`, `match` or `training`
- Column `D`: `minutes_played`, for match rows
- Column `E`: the measure, such as total distance in metres
- Column `F`: `days_to_next`. Column `G`: `days_since_last`. Column `H`: the label. Column `I`: the match reference. Column `J`: the percent.
- Cell `M1`: `post_match_days`. Cell `M2`: the minimum minutes for a qualifying match. Cell `M3`: the minimum match reference for a percent.

Enter these formulas in row 2, and fill them down:

```text
F2:  =IF(COUNTIF(matches!A:A,">"&A2)=0,"",MINIFS(matches!A:A,matches!A:A,">"&A2)-A2)
G2:  =IF(COUNTIF(matches!A:A,"<"&A2)=0,"",A2-MAXIFS(matches!A:A,matches!A:A,"<"&A2))
H2:  =IF(COUNTIF(matches!A:A,A2)>0,"MD",
       IF(AND(G2<>"",G2<=$M$1),"MD+"&G2,IF(F2<>"","MD-"&F2,"")))
I2:  =IFERROR(AVERAGEIFS(E:E,B:B,B2,C:C,"match",D:D,">="&$M$2),"")
J2:  =IF(OR(I2="",NOT(ISNUMBER(E2))),"",IF(I2<=$M$3,"",E2/I2*100))
```

The formulas work this way:

- `MINIFS` and `MAXIFS` find the next and the last match. The `COUNTIF` tests return a blank before the first match or after the last, instead of a wrong number. Both functions need Excel 2019 or later, or Google Sheets.
- `AVERAGEIFS` takes the mean of the player's matches with at least the minimum minutes. It returns an error when no match qualifies, and `IFERROR` turns that into a blank.
- `J2` gives no percent when the reference is at or below the minimum in `M3`.

For a position reference or a reference from the last few matches only, add the condition to `AVERAGEIFS`, and label the column.

Use this Python code. `sessions` has one row per player and session with `session_date`, `athlete_id`, `session_type`, `minutes_played`, and the measure columns. `matches` has one row per match with `match_date`:

```python
import pandas as pd

post_match_days, min_minutes, min_ref = 1, 60, 0       # ask the user for all three
m = pd.Series(sorted(pd.to_datetime(matches["match_date"]).unique()))
d = pd.to_datetime(sessions["session_date"])
nxt = m.searchsorted(d, side="right")                    # first match after the date
prv = m.searchsorted(d, side="left") - 1                 # last match before the date
mv = list(m) + [pd.NaT]
sessions["days_to_next"] = [(mv[i] - x).days if i < len(m) else None for i, x in zip(nxt, d)]
sessions["days_since_last"] = [(x - m[i]).days if i >= 0 else None for i, x in zip(prv, d)]
is_match = d.isin(m)

def label(row, match):
    if match:
        return "MD"
    s, t = row["days_since_last"], row["days_to_next"]
    if pd.notna(s) and s <= post_match_days:
        return f"MD+{int(s)}"
    return f"MD-{int(t)}" if pd.notna(t) else None

sessions["md_label"] = [label(r, x) for (_, r), x in zip(sessions.iterrows(), is_match)]

measure = "total_distance_m"                             # ask the user
q = sessions[(sessions["session_type"] == "match") & (sessions["minutes_played"] >= min_minutes)]
ref = q.groupby("athlete_id")[measure].agg(["mean", "count"])
sessions = sessions.join(ref.rename(columns={"mean": "match_ref", "count": "ref_matches"}),
                         on="athlete_id")
ok = sessions["match_ref"] > min_ref
sessions["pct_of_match"] = (sessions[measure] / sessions["match_ref"] * 100).where(ok)
```

`ref_matches` counts the matches in each player's reference. Report it with the percent.

### Calculate it in Power BI and Tableau

These versions follow the spreadsheet formulas. They label sessions from the fixture list, take the mean of each player's qualifying matches as the reference, and return a blank when no match qualifies or the reference is below the minimum.

Both versions assume a long `measures` table with one row per athlete, session, and measure: `athlete_id`, `session_id`, `measure_name`, `unit`, `value`, and `status`. Each row also carries `session_type` and `minutes_played`. Fill `minutes_played` on match rows from the official match report. A `sessions` table holds one row per session with `session_id` and `session_date`. A `matches` table holds one row per match date in `match_date`.

In Power BI, add these calculated columns to `sessions`. They are columns because the label is a fixed property of the date and the fixture list:

```text
Days to next =
VAR d = sessions[session_date]
VAR nxt = CALCULATE ( MIN ( matches[match_date] ), FILTER ( ALL ( matches ), matches[match_date] > d ) )
RETURN IF ( ISBLANK ( nxt ), BLANK (), INT ( nxt - d ) )

Days since last =
VAR d = sessions[session_date]
VAR prv = CALCULATE ( MAX ( matches[match_date] ), FILTER ( ALL ( matches ), matches[match_date] < d ) )
RETURN IF ( ISBLANK ( prv ), BLANK (), INT ( d - prv ) )

MD label =
VAR postDays = 1
VAR isMatch =
    NOT ISEMPTY ( FILTER ( ALL ( matches ), matches[match_date] = sessions[session_date] ) )
RETURN
    SWITCH (
        TRUE (),
        isMatch, "MD",
        NOT ISBLANK ( sessions[Days since last] ) && sessions[Days since last] <= postDays,
            "MD+" & sessions[Days since last],
        NOT ISBLANK ( sessions[Days to next] ), "MD-" & sessions[Days to next]
    )
```

Relate `sessions[session_id]` to `measures[session_id]` and `athletes[athlete_id]` to `measures[athlete_id]`, one to many, single direction. Leave `matches` unrelated. Put `measures[measure_name]` in a slicer, and pick one. Use these DAX measures:

```text
Match reference =
VAR minMinutes = 60
RETURN
    CALCULATE (
        AVERAGE ( measures[value] ),
        REMOVEFILTERS ( sessions ),
        measures[session_type] = "match",
        measures[minutes_played] >= minMinutes,
        measures[status] = "ok"
    )

% of match =
VAR minRef = 0
VAR v = CALCULATE ( SUM ( measures[value] ), measures[status] = "ok" )
VAR r = [Match reference]
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( measures[measure_name] )
            && NOT ISBLANK ( v ) && NOT ISBLANK ( r ) && r > minRef,
        v / r * 100
    )
```

The measures work this way:

- `REMOVEFILTERS ( sessions )` lets the reference look at every match, whatever session is in the visual. Put `sessions[session_id]` in the visual, not `measures[session_id]`, or the session filter stays.
- A blank `minutes_played` compares as 0, so training rows never qualify.
- With one session per row, `% of match` is the session percent. With a microcycle column on the axis instead, the `SUM` adds the sessions, and the result is `week_pct`. Leave match rows out of a weekly total.

In Tableau, make a data source `session_calendar` for the labels. In the physical layer, join `sessions` to `matches` with a join calculation of `1` on both sides, so each session row meets every match date. Make an integer parameter `Post-match days` set to 1. Use these calculations:

```text
Next match date:
{FIXED [session_id] : MIN(IF [match_date] > [session_date] THEN [match_date] END)}

Last match date:
{FIXED [session_id] : MAX(IF [match_date] < [session_date] THEN [match_date] END)}

Is match day:
{FIXED [session_id] : MAX(IIF([match_date] = [session_date], 1, 0))}

Days to next:
DATEDIFF('day', [session_date], [Next match date])

Days since last:
DATEDIFF('day', [Last match date], [session_date])

MD label:
IF [Is match day] = 1 THEN "MD"
ELSEIF NOT ISNULL([Days since last]) AND [Days since last] <= [Post-match days]
    THEN "MD+" + STR([Days since last])
ELSEIF NOT ISNULL([Days to next]) THEN "MD-" + STR([Days to next])
END
```

Relate `session_calendar` to `measures` on `session_id` in the logical layer. The duplicate rows from the join stay inside `session_calendar`, so they do not repeat measure values. In `measures`, make a parameter `Minimum minutes` set to 60 and a parameter `Minimum reference` set to 0. Put `athlete_id`, `session_id`, and `measure_name` on the view, and use these calculations:

```text
Match reference:
{FIXED [athlete_id], [measure_name] :
    AVG(IF [session_type] = "match" AND [minutes_played] >= [Minimum minutes]
        AND [status] = "ok" THEN [value] END)}

% of match:
IF ISNULL(MIN([Match reference])) OR MIN([Match reference]) <= [Minimum reference] THEN NULL
ELSE SUM(IF [status] = "ok" THEN [value] END) / MIN([Match reference]) * 100
END
```

The `FIXED` reference ignores the session on the view, so every session row gets the player's match mean (https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod_fixed.htm).

Blanks behave this way in each tool:

- Power BI and Tableau: a session before the first match has no `Days since last`, and a session after the last match has no `Days to next`. The label falls back to the other number, or stays blank.
- Both: a player with no qualifying match has a blank reference and a blank percent. Use a position reference only if the user asks, and label it.
- Both: a missing session value gives a blank percent, not 0%.

## Calculate the metric

Follow these steps to calculate the metric from raw inputs:

1. Get the fixture list with every match date, including cup and friendly matches the user counts.
2. Ask how many days after a match to label as MD+.
3. Calculate `days_to_next` and `days_since_last` for every session.
4. Label each session.
5. Record the days between matches for each microcycle.
6. Ask for the measure, and confirm training and matches use the same device, settings, and calculation.
7. Ask for the match reference rule: full matches, a minimum number of minutes, extrapolation, or a position reference.
8. Ask how many recent qualifying matches to include.
9. Calculate each player's match reference, and count the matches in it.
10. Ask for a minimum reference below which no percent is shown, most of all for goalkeepers.
11. Divide each session value by the player's reference, and multiply by 100.
12. For a week, add the training session values in the microcycle, then divide by the reference.
13. Label each result with the measure, the reference rule, the number of matches in the reference, and the microcycle length.

## Worked example

This example uses one team's fixture list and three made-up players. Every value below came from running the calculation in Python.

The team plays on these dates: 2026-09-05, 2026-09-12, 2026-09-16, and 2026-09-19. The coach labels 1 day after a match as MD+.

| Date | Day | Days since last match | Days to next match | Label |
|---|---|---|---|---|
| 2026-09-06 | Sun | 1 | 6 | MD+1 |
| 2026-09-07 | Mon | 2 | 5 | MD-5 |
| 2026-09-08 | Tue | 3 | 4 | MD-4 |
| 2026-09-09 | Wed | 4 | 3 | MD-3 |
| 2026-09-10 | Thu | 5 | 2 | MD-2 |
| 2026-09-11 | Fri | 6 | 1 | MD-1 |
| 2026-09-12 | Sat | 7 | 4 | MD |
| 2026-09-13 | Sun | 1 | 3 | MD+1 |
| 2026-09-14 | Mon | 2 | 2 | MD-2 |
| 2026-09-15 | Tue | 3 | 1 | MD-1 |
| 2026-09-16 | Wed | 4 | 3 | MD |
| 2026-09-17 | Thu | 1 | 2 | MD+1 |
| 2026-09-18 | Fri | 2 | 1 | MD-1 |

The week of 2026-09-06 has 6 days between matches. The week of 2026-09-13 is congested: it has no MD-3 or MD-4, and 2026-09-14 is both 2 days after and 2 days before a match.

Player A played three full matches: 10,200, 10,650, and 10,500 m of total distance, and 650, 720, and 700 m above 19.8 km/h. The match references are 10,450 m and 690 m. Player A's 6-day week gives these values:

| Label | Total distance | Percent of match | High-speed distance | Percent of match |
|---|---|---|---|---|
| MD+1 | 3,200 m | 30.6% | 40 m | 5.8% |
| MD-4 | 6,100 m | 58.4% | 310 m | 44.9% |
| MD-3 | 5,900 m | 56.5% | 250 m | 36.2% |
| MD-2 | 4,300 m | 41.1% | 120 m | 17.4% |
| MD-1 | 3,000 m | 28.7% | 60 m | 8.7% |
| Week, 5 sessions | 22,500 m | 215.3% | 780 m | 113.0% |

For one session: 5,900 ÷ 10,450 × 100 = 56.5%.

Player B plays the same position as Player A. Both players qualify, so the position reference is the mean of their two references: (10,450 + 9,950) ÷ 2 = 10,200 m. Player B came on for 30 minutes in the last match and covered 3,900 m. Player B also played two earlier full matches, with 9,800 and 10,100 m. On MD-3, Player B ran 5,900 m. The reference rule changes the percent:

| Match reference rule | Reference | MD-3 percent |
|---|---|---|
| Matches of at least 60 minutes | 9,950 m | 59.3% |
| Last match extrapolated: 3,900 × 90 ÷ 30 | 11,700 m | 50.4% |
| Position reference, mean of Player A's and Player B's references | 10,200 m | 57.8% |

The extrapolated reference assumes Player B would have kept a fresh substitute's rate for 90 minutes. It gives the lowest percent for the same session.

A goalkeeper covered 12, 16, and 14 m above 19.8 km/h in three matches, a reference of 14 m. An MD-3 session with 9 m reads 64.3%. One with 19 m reads 135.7%. Ten metres moved the percent by 71.4 points. Show these values raw, with no percent.

## What changes the number

These choices change the result even when the athlete's training does not:

- Match reference rule. In the worked example, the same 5,900 m session reads 50.4% to 59.3% for Player B.
- Number of matches in the reference. Match running varies from match to match. In English Premier League players, match-to-match coefficient of variation was 16.2% for high-speed running and 30.8% for sprint distance (Gregson et al., 2010). A reference from one match moves with that match.
- Labeling rule. The number of post-match days changes which sessions are MD+ and which are MD-. A congested week changes which labels exist.
- Group ratio or player percent. The ratio of means and the mean of player percents differ.
- Measure and threshold. High-speed and sprint percents run lower than distance percents in the studies cited here. Use the same threshold in training and matches.
- Device, software, and settings. A match tracked by a camera system and training tracked by GPS do not give comparable values. See [total-distance.md](total-distance.md#what-changes-the-number).
- Session content. MD-3 in one team is not MD-3 in another. Both studies describe the content of each day for one team only.

## Units and typical range

The percent has no unit. The values below are findings from single teams under their own settings. They are not targets, and they do not transfer to another team.

| Population | Finding | Source |
|---|---|---|
| Spanish La Liga reserve team, 24 outfield players, 10 Hz GPS, weeks with 6 days between matches | Load declined from MD-4 to MD-1. At MD-3, total distance was 57%, high-speed running (above 19.8 km/h) 37%, and sprint distance (above 25.2 km/h) 29% of match values. At MD-4, high-speed running was 43% and sprint distance 45%. | Martín-García et al., 2018 |
| Same team, accelerations and decelerations above 3 m/s² | MD+1 compensatory 80% to 86%, MD-4 71% to 72%, MD-3 62% to 69%, MD-2 56% to 61% of match values | Martín-García et al., 2018 |
| Same team, MD+1 compensatory session, players with less than 60 minutes | Total distance 53% of match values | Martín-García et al., 2018 |
| Norwegian elite team, local positioning, four sessions in a typical week, by position | Accelerations 131% to 166%, decelerations 108% to 134%, sprint distance 36% to 61%, and high-intensity running 57% to 71% of match values | Baptista et al., 2020 |
| English Premier League, camera tracking, match-to-match variation | Coefficient of variation 16.2% for high-speed running, 30.8% for sprint distance | Gregson et al., 2010 |

Martín-García et al. (2018) computed the percent as the mean training value times 100, divided by the mean match value. Baptista et al. (2020) set high-intensity running at 19.8 km/h or more and sprinting at 25.2 km/h or more.

## Data you need

Collect this data:

- Fixture list: every match date the user counts, with competition type.
- Minutes played: from the official match report, for every player and match.
- Positions: the position each player played in each match.
- Session data: one value per player per session for each measure, from the same device and settings in training and matches.
- Session type: recovery, compensatory, or main session, for MD+ days.
- Minimum data: a reference needs at least one qualifying match. Ask the user how many to use, and report the count.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Labeling only by days to the next match. MD+1 sessions then read as MD-5 or MD-2. Store both numbers, and use the coach's post-match rule.
- Comparing the same label across week shapes. MD-2 in a congested week is not MD-2 in a 6-day week.
- Using a squad reference for every player. Use each player's own match reference.
- Extrapolating a short appearance without saying so. It assumes the same rate for 90 minutes. Name the rule.
- Putting goalkeepers in outfield groups, or showing a percent of a near-zero match value.
- Mixing match data from one system with training data from another.
- Presenting a study percent as a target. Report it as one team's finding under its settings. The coach decides the plan.
- Adding match load into a training week percent. Report match and training load as separate lines.

## Example request

> Our fixtures are in one sheet and our GPS totals in another, one row per player per session. Label every session by match day, and show each player's total distance and distance above 19.8 km/h as a percent of their own match average. Use matches where they played at least 60 minutes. We had two matches last week.

## Check the result

Run these checks:

- Confirm every match date has the label MD, and no training date does.
- Confirm a congested week has no MD-4 or MD-3 when there are 3 days between matches.
- Recalculate two percents by hand: session value ÷ reference × 100.
- Confirm each reference states its rule and the number of matches in it.
- Confirm goalkeepers are reported on their own, and no percent rests on a match value below the user's minimum.
- State the counts of players, sessions, and matches in the answer.

## Sources

These sources support the figures and methods in this file:

- Martín-García A, Gómez Díaz A, Bradley PS, Morera F, Casamichana D. Quantification of a professional football team's external load using a microcycle structure. J Strength Cond Res. 2018;32(12):3511-3518. https://doi.org/10.1519/JSC.0000000000002816 Read in full from the open-access copy at https://researchonline.ljmu.ac.uk/id/eprint/9011/ (accessed 2026-10-07)
- Baptista I, Johansen D, Figueiredo P, Rebelo A, Pettersen SA. Positional differences in peak- and accumulated- training load relative to match load in elite football. Sports. 2020;8(1):1. Published online 2019-12-23. https://doi.org/10.3390/sports8010001 (accessed 2026-10-07)
- Gregson W, Drust B, Atkinson G, Di Salvo V. Match-to-match variability of high-speed activities in premier league soccer. Int J Sports Med. 2010;31(4):237-242. https://doi.org/10.1055/s-0030-1247546
