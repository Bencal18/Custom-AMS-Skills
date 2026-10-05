# Session RPE load

Last checked: 2026-10-02

## What it measures

Session RPE load estimates how hard a whole session was for the athlete by multiplying their effort rating by the session length.

It is a measure of internal load. Internal load is the athlete's response to the work. External load is the work itself, such as distance run or weight lifted (Impellizzeri et al., 2019). Session RPE load does not replace external load, and external load does not replace it.

## Formula

Use the session RPE method from Foster et al. (2001):

```text
session_rpe_load_au = rpe_cr10 × duration_min
```

Define every term in the formula:

- `rpe_cr10`: the athlete's rating of the whole session on the 0 to 10 category ratio scale (CR-10), where 0 is rest and 10 is maximal. According to Haddad et al. (2017), Foster et al. (2001) changed some of Borg's verbal labels to American English, for example "light" became "easy". No unit.
- `duration_min`: the session length in minutes. Foster et al. (2001) and Impellizzeri et al. (2004) multiply by session duration in minutes.
- `session_rpe_load_au`: the result, in arbitrary units (AU) (Haddad et al., 2017). AU is not a physical unit such as meters or joules. Compare AU only for the same athlete, scale, and method.

Check which rating scale the form used:

- CR-10: the scale this file assumes. Ratings run from 0 to 10.
- Borg CR100, also called centiMax (Borg and Kaijser, 2006): a category ratio scale with a wider number range than CR-10. It is valid for session RPE in soccer and can be used interchangeably with CR-10 (Fanchini et al., 2016). If most ratings are above 10, ask whether the form used CR100. Do not mix CR100 and CR-10 loads in one series without a conversion the user names.
- Ratings above 10 on a CR-10 form: Borg's CR-10 is often described as allowing a rating above 10 for an effort harder than any before. We could not confirm this in the sources cited here, so treat it as unverified. Ask the user about any value above 10 before you call it an error.
- The 6 to 20 RPE scale: a different scale. The product with minutes is not session RPE load.

Collect the rating this way:

- Show the athlete the CR-10 scale with its labels, and ask for one rating of the whole session. Foster et al. (2001) asked "How was your workout?"
- Collect the rating about 30 minutes after the session ends. Foster et al. (2001) waited 30 minutes so that an unusually hard or easy final drill would not dominate the rating.
- Keep the delay the same every day. One study of 15 well-trained adults found no difference in session RPE collected between 5 minutes and 24 hours after 30-minute cycling bouts (Christen et al., 2016). The participants rated on a visual analog scale without the CR-10 verbal labels, and the authors note that whether a cool-down was done may matter. Treat that as one study, not as permission to vary the delay.

For more than one session in a day, calculate each session's load, then add them. Daily load is the sum of session loads. Weekly load is the sum of daily loads.

Record injured, ill, or modified-training days this way:

- Mark each day in a separate column, such as `availability`, with values such as `full`, `modified`, and `out`.
- Rate a modified session the usual way, with its own duration.
- Record a day with no activity as `0` AU, with the reason in the `availability` column. Keep a day with activity but no rating as missing.
- Report these days apart, so you do not read a drop in load as a planned easy week.

These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.

Use these spreadsheet formulas, with RPE in column `C`, minutes in column `D`, and session load in column `E`. The first keeps a blank rating or duration blank instead of 0 AU. The second leaves a day blank if any of its sessions has a blank load. Here the sessions are rows 2 and 3:

```text
Session load, E2: =IF(OR(C2="",D2=""),"",C2*D2)
Daily load:       =IF(COUNT(E2:E3)<ROWS(E2:E3),"",SUM(E2:E3))
```

A plain `=C2*D2` turns a blank rating into 0 AU, which reads as a rest day.

Python:

```python
df["srpe_load_au"] = df["rpe_cr10"] * df["duration_min"]
# A day with any missing rating stays missing, so it is not undercounted.
daily = (df.groupby(["athlete_id", "date"])["srpe_load_au"]
           .agg(lambda x: x.sum(min_count=len(x))))
```

### Calculate it in Power BI and Tableau

A missing rating or duration keeps the session load blank, not 0 AU. A day with any blank session load stays blank, so it is not undercounted. A rating of 0 is a real 0.

Both versions work on a session table with one row per athlete, date, and session: `athlete_id`, `measure_date`, `session_id`, `rpe_cr10`, and `duration_min`. Build it from the long `measures` table by pivoting `measure_name` to columns.

In Power Query, first set `value` to null on rows whose `status` is not `ok`. Then keep only `athlete_id`, `measure_date`, `session_id`, `measure_name`, and `value`. Select `measure_name`, then **Transform**, then **Pivot column**, with `value` as the value column. Under **Advanced**, choose **Don't aggregate**. The default is a sum, which would silently add two ratings for one session. With **Don't aggregate**, a duplicate shows as an error in that cell. Fix the duplicate at the source.

In Power BI, use a calculated column for the session load and a measure for the daily load. The session load is a calculated column because both inputs sit on the same row and do not change with slicers. The daily load is a measure because it sums rows:

```text
srpe_load_au (calculated column on session_load) =
IF (
    ISBLANK ( session_load[rpe_cr10] ) || ISBLANK ( session_load[duration_min] ),
    BLANK (),
    session_load[rpe_cr10] * session_load[duration_min]
)

Daily load (AU) (measure) =
VAR sessions = COUNTROWS ( session_load )
VAR rated = COUNT ( session_load[srpe_load_au] )
RETURN IF ( sessions > 0 && rated = sessions, SUM ( session_load[srpe_load_au] ) )
```

Show the daily load with one athlete and one date per row.

In Tableau, build the same session table in Tableau Prep with a rows-to-columns pivot, or in the spreadsheet, Python, or R. Check that the pivot does not add two values for one session. Then use these calculations:

```text
Session load (AU) (row-level):
IF ISNULL([rpe_cr10]) OR ISNULL([duration_min]) THEN NULL
ELSE [rpe_cr10] * [duration_min]
END

Daily load (AU) (aggregate, with athlete_id and measure_date on the view):
IF COUNT([Session load (AU)]) < COUNT([session_id]) THEN NULL
ELSE SUM([Session load (AU)])
END
```

To work on the long table instead, put `athlete_id`, `measure_date`, and `session_id` on the view, and use a table calculation for the day:

```text
Session load, long table (aggregate):
IF ISNULL(MAX(IF [measure_name] = "rpe_cr10" AND [status] = "ok" THEN [value] END))
   OR ISNULL(MAX(IF [measure_name] = "duration_min" AND [status] = "ok" THEN [value] END))
THEN NULL
ELSE MAX(IF [measure_name] = "rpe_cr10" AND [status] = "ok" THEN [value] END)
   * MAX(IF [measure_name] = "duration_min" AND [status] = "ok" THEN [value] END)
END

Daily load, long table (table calculation):
IF WINDOW_SUM(IIF(ISNULL([Session load, long table]), 1, 0)) > 0 THEN NULL
ELSE WINDOW_SUM([Session load, long table])
END
```

Set **Compute Using** for `Daily load, long table` to `session_id` only. Tableau then partitions by `athlete_id` and `measure_date`, and each day restarts.

Blanks behave this way in each tool:

- Power BI: DAX multiplies a blank by a number to a blank, but the explicit `ISBLANK` test keeps the rule visible. `COUNT` skips blank loads, so a day with a blank session has `rated` below `sessions` and returns a blank.
- Tableau: `COUNT` ignores nulls, so the daily test works the same way. A null rating makes the product null.
- Both: a text rating becomes null on import. In the spreadsheet, a rating that is not a number, such as "six", gives `#VALUE!`. A number stored as text, such as "6", is multiplied like a number.

## Calculate session load

Follow these steps to calculate the metric from raw inputs:

1. Load one row per athlete per session with the columns `athlete_id`, `date`, `session`, `rpe_cr10` (0 to 10, no unit), and `duration_min` (minutes).
2. Confirm every `rpe_cr10` value is between 0 and 10.
3. Ask the user about any value above 10 before you call it an error. It may come from a CR100 form.
4. Convert any duration in hours or `hh:mm` text to minutes, and store it in `duration_min`.
5. Multiply `rpe_cr10` by `duration_min` for each session, and store the result in `srpe_load_au` (AU). Keep the result missing if either input is missing.
6. Add `srpe_load_au` across sessions for each `athlete_id` and `date` to get daily load in AU. If any session that day has a missing rating, mark the day as missing.
7. Add daily loads across each calendar week, Monday to Sunday unless the user names another start day, to get weekly load in AU. Do this even when the user asked only for daily load. Report how many days had complete data and how many were marked injured, ill, or modified. Mark a week with any missing day as incomplete, and give its total with the number of days it covers, such as 6 of 7 days.

## Worked example

One athlete trains three days. Monday has a practice and a lift.

| Date | Session | `rpe_cr10` | `duration_min` |
|---|---|---|---|
| 2026-08-03 | Practice | 6 | 75 |
| 2026-08-03 | Lift | 4 | 45 |
| 2026-08-04 | Practice | 7 | 90 |
| 2026-08-05 | Practice | 5 | 60 |

Multiply each session, then add by day:

- 2026-08-03 practice: 6 × 75 = 450 AU.
- 2026-08-03 lift: 4 × 45 = 180 AU.
- 2026-08-03 daily load: 450 + 180 = 630 AU.
- 2026-08-04 daily load: 7 × 90 = 630 AU.
- 2026-08-05 daily load: 5 × 60 = 300 AU.
- Three-day total: 630 + 630 + 300 = 1,560 AU.

The wrong method averages Monday's RPE and multiplies by Monday's total minutes: 5 × 120 = 600 AU. That is 30 AU short of the correct 630 AU.

## What changes the number

These choices change the result even when the athlete's performance does not:

- Duration definition. Adding a 15-minute warm-up to Monday's practice changes it from 450 AU to 6 × 90 = 540 AU. Use one rule for each session type, such as training and matches.
- Duration unit. Entering Monday's practice as 1.25 hours gives 6 × 1.25 = 7.5 AU instead of 450 AU.
- Rating timing. The end of a session can dominate a rating taken straight away (Foster et al., 2001). If that changed Monday's rating from 6 to 7, the practice would read 7 × 75 = 525 AU. Collect the rating at the same delay every day.
- Rating scale. A rating on the 6 to 20 scale is not a CR-10 rating. A CR100 rating is on a different range from a CR-10 rating. Name the scale with every load.
- Splitting or merging sessions. Rating a practice and a lift separately and adding them gives a different number from one rating of the whole day. Pick one method and keep it.
- How the question is asked. Use the same scale, labels, and wording every time. Haddad et al. (2017) list many factors that can alter RPE.

## Units and typical range

Session RPE load has no population range that applies across sports, ages, and training phases. Compare each athlete with their own history.

| Population | Possible range | Source |
|---|---|---|
| Any session, CR-10 | 0 to 10 × `duration_min` AU. Ask about any value above this before you call it an error. | Foster et al., 2001 (scale bounds) |

Haddad et al. (2017) give a published example: an 87-minute session at RPE 4 gives 87 × 4 = 348 AU.

## Data you need

Collect this data:

- Source: a post-session RPE form or app, plus the session duration from a training plan, timer, or device.
- Sampling: one rating per athlete per session, and one `availability` value per athlete per day.
- Minimum data: one session gives one load value. Any trend needs weeks of complete data for that athlete.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Using the 6 to 20 RPE scale. Borg (1982) described his category RPE scale and a separate category ratio scale. The session RPE method uses the 0 to 10 category ratio scale (Foster et al., 2001). Multiplying a 6 to 20 rating by minutes gives a different, non-comparable number. Ask which scale the form used.
- Calling every rating above 10 an error. The form may use the Borg CR100 scale (Fanchini et al., 2016). Ask before you flag or drop the value.
- Duration in hours or as text. A 90-minute session entered as `1.5` gives a load 60 times too small. A `1:30` text value may read as a time of day. Convert to minutes first.
- Mixing what counts as duration. No consensus says whether duration includes the warm-up or the cool-down. Ask, keep one rule for each session type, and record it. If the user has no rule, offer this default and label it as this skill's choice: training time from the start of the team warm-up to the end of the last drill, without a separate cool-down. Pustina et al. (2017) defined training duration the same way: it includes the warm-up and recovery periods and excludes the cool-down. For matches, ask whether to use minutes played. In one study of college soccer, match loads from minutes played correlated with GPS distance more closely than loads from total match duration: r = 0.808 against 0.566 (Pustina et al., 2017). Under minutes played, an unused substitute's warm-up scores 0 AU. The cool-down can change the rating itself, not only the minutes (Rodríguez-Marroyo et al., 2021).
- Averaging RPE across sessions and multiplying by total minutes. This is not the same as adding each session's load. Multiply first, then add.
- Treating a missing rating as zero. A zero load means no training. A missing rating means unknown. Keep it missing and report coverage. A spreadsheet `=C2*D2` makes this mistake on every blank row.
- Hiding injured, ill, or modified-training days. A low load from an injury looks like a planned easy day. Mark these days.
- Collecting the rating straight after the last drill. The end of the session can dominate the rating (Foster et al., 2001). Collect it at a fixed delay.
- Comparing AU across athletes as if they were the same scale. Two athletes can rate the same session differently. Use each athlete's own history.
- Calling session RPE load "external load" or adding it to GPS distance. Internal and external load are different constructs (Impellizzeri et al., 2019).

## Example request

> I have a Google Sheet with athlete, date, session type, RPE out of 10, and minutes. Some days have two sessions. Give me daily and weekly sRPE load per athlete.

## Check the result

Run these checks:

- Recalculate two rows by hand: RPE × minutes. Confirm the units are AU.
- Confirm the largest single-session value is no more than 10 × that session's minutes, or that the user confirmed the scale for any larger value.
- Confirm the number of sessions in the output matches the input, that athlete-days equal the athlete-days in the input plus any days you added, and that missing ratings stayed missing.

## Sources

This file cites these sources:

- Foster C, Florhaug JA, Franklin J, Gottschall L, Hrovatin LA, Parker S, Doleshal P, Dodge C. A new approach to monitoring exercise training. J Strength Cond Res. 2001;15(1):109-115. https://doi.org/10.1519/00124278-200102000-00019
- Borg GA. Psychophysical bases of perceived exertion. Med Sci Sports Exerc. 1982;14(5):377-381. https://doi.org/10.1249/00005768-198205000-00012
- Borg E, Kaijser L. A comparison between three rating scales for perceived exertion and two different work tests. Scand J Med Sci Sports. 2006;16(1):57-69. https://doi.org/10.1111/j.1600-0838.2005.00448.x
- Fanchini M, Ferraresi I, Modena R, Schena F, Coutts AJ, Impellizzeri FM. Use of the CR100 scale for session rating of perceived exertion in soccer and its interchangeability with the CR10. Int J Sports Physiol Perform. 2016;11(3):388-392. https://doi.org/10.1123/ijspp.2015-0273
- Impellizzeri FM, Rampinini E, Coutts AJ, Sassi A, Marcora SM. Use of RPE-based training load in soccer. Med Sci Sports Exerc. 2004;36(6):1042-1047. https://doi.org/10.1249/01.MSS.0000128199.23901.2F
- Impellizzeri FM, Marcora SM, Coutts AJ. Internal and external training load: 15 years on. Int J Sports Physiol Perform. 2019;14(2):270-273. https://doi.org/10.1123/ijspp.2018-0935
- Haddad M, Stylianides G, Djaoui L, Dellal A, Chamari K. Session-RPE method for training load monitoring: validity, ecological usefulness, and influencing factors. Front Neurosci. 2017;11:612. https://doi.org/10.3389/fnins.2017.00612
- Christen J, Foster C, Porcari JP, Mikat RP. Temporal robustness of the session rating of perceived exertion. Int J Sports Physiol Perform. 2016;11(8):1088-1093. https://doi.org/10.1123/ijspp.2015-0438
- Pustina AA, Sato K, Liu C, Kavanaugh AA, Sams ML, Liu J, Uptmore KD, Stone MH. Establishing a duration standard for the calculation of session rating of perceived exertion in NCAA Division I men's soccer. J Trainol. 2017;6(1):26-30. https://doi.org/10.17338/trainology.6.1_26 (accessed 2026-10-02)
- Rodríguez-Marroyo JA, González B, Foster C, Carballo-Leyenda AB, Villa JG. Effect of the cooldown type on session rating of perceived exertion. Int J Sports Physiol Perform. 2021;16(4):573-577. https://doi.org/10.1123/ijspp.2020-0225 (accessed 2026-10-02)
