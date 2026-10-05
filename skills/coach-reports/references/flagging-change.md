# Change versus noise

Last checked: 2026-10-02

## What it measures

This file shows how to flag a change in an athlete's result only when it is larger than random measurement error. It also shows how to say whether the change is large enough to matter. It uses the athlete's own baseline, the typical error, and the smallest worthwhile change.

## Formula

Compare each new value to the athlete's own baseline. The baseline is the mean of that athlete's earlier values from a stable period. Do not include the new value in the baseline.

```text
change     = new value - baseline mean
noise band = 1.96 x TE x sqrt(1 + 1/n)
SWC        = 0.2 x between-athlete SD
```

Define every term in the formulas:

- `new value`: the athlete's result from the test you are judging, in the unit of the measure
- `baseline mean`: the mean of `n` earlier values of that athlete, in the unit of the measure
- `n`: the number of values in the baseline. Show it in the report.
- `TE`: the typical error, the standard deviation of one athlete's repeated measurements, in the unit of the measure (Hopkins, 2000)
- `noise band`: when nothing has changed, error alone gives a change smaller than this about 95 percent of the time, if the assumptions below hold
- `SWC`: the smallest worthwhile change, in the unit of the measure
- `between-athlete SD`: the standard deviation of the athletes' scores on the test at baseline

For two single tests, `n = 1`, and the noise band is `1.96 x sqrt(2) x TE`, about 2.77 times TE. Swinton and colleagues (2018) give this as the 95 percent range for an observed change.

For a baseline that is a mean of several tests, the term `sqrt(1 + 1/n)` replaces `sqrt(2)`.

This band is derived by adding the variance of the new value (TE squared) and the variance of the baseline mean (TE squared divided by `n`). Hopkins (2017) uses the same error for a change from the mean of several tests. The 95 percent level is this skill's choice.

Swinton and colleagues (2018) take the SWC as 0.2 times the baseline between-athlete standard deviation. Hopkins and colleagues (2009) list 0.2 as the small standardized difference.

### List the assumptions beside the band

Write these assumptions next to the noise band in every report:

- The athlete's true value stayed the same across the baseline and the new test, apart from the change you want to detect.
- Errors are independent from test to test. A swing that lasts several days breaks this.
- TE is the same for every athlete and at every size of value.
- TE is known. Choose the multiplier as follows:
  - Use 1.96 when TE comes from a large reliability study.
  - When TE comes from few athletes, use a t multiplier with degrees of freedom from the TE study, not from the baseline: athletes minus 1 for two trials.
  - Swinton and colleagues (2018) give 2.26 for a TE from 10 participants. The t value for a TE from 6 athletes is 2.57.
- TE comes from a short-term retest in which no true change is expected, with the same summary as the values you compare: a single trial, the best of 3, or the mean of 3.

With all assumptions met, about 5 percent of unchanged results fall beyond the band in both directions, or 2.5 percent in one direction.

When assumptions fail, the real rate can be higher or lower than 5 percent. It is higher when TE is too small, comes from few athletes, or varies between athletes. It can be lower when TE is overestimated, or when errors are positively correlated over time.

### Choose the flag state

Ask the user which direction matters. A drop in jump height and a rise in a soreness score are different directions. Do not assume. Then give each athlete and measure one of these states:

| State | Rule | Wording |
|---|---|---|
| No flag | The change is inside the noise band. | Within usual variation |
| Noted | The change is beyond the noise band, and the change minus the band is not beyond the SWC. | Larger than measurement error; may or may not be worthwhile |
| Flagged | The change minus the noise band is beyond the SWC in the chosen direction. For a rise, change minus band is above the SWC. For a drop, change plus band is below minus the SWC. | Larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation |
| No data | The new value or the baseline is missing, or `n` is below the minimum the user set. | Not enough data |

The flagged state needs the change to clear the noise band and the SWC together. This follows Swinton and colleagues (2018), who classify a change by whether the confidence interval for the true change lies in a pre-defined region, such as beyond the SWC. The wording describes the likely range of the true change, not only the observed change.

If a change lies beyond the band in the direction the user did not choose, report it with its direction, and do not give it the flagged state unless the user asks.

Use the wording in the table, or the user's own. Do not use words such as `risk`, `fatigued`, or `injured`.

### Get TE and the SWC

Ask the user for the TE of each measure, from their own short-term retest. Swinton and colleagues (2018) take TE from test-retest data over time periods where true scores are not expected to change. Use the same protocol, with athletes who were not trying to change, and the same summary as the values you compare.

Optional: retest on separate days, so that normal day-to-day variation counts as noise. This is a practice choice of this skill, not a published rule. It gives a larger TE than a same-day retest, and so fewer flags.

To compute TE from two retests for each athlete, take the standard deviation of the differences between the two tests, and divide it by the square root of 2. Swinton and colleagues (2018) state that the standard deviation of change scores equals TE times the square root of 2.

With three or more retests for each athlete, take out each athlete's mean and each retest's mean, then pool what is left. The pooled value is the square root of the sum of squared leftovers, divided by (athletes minus 1) times (retests minus 1). That product is also the degrees of freedom for the t multiplier.

This removes a shift in the mean between retests, such as learning or fatigue, which Hopkins (2000) says must not count as error. With two retests, it gives the same TE as the method above.

Hopkins (2000) states that reasonable precision for a reliability estimate needs about 50 participants and at least 3 trials. With fewer, label the TE a rough estimate.

If the user has no TE, tell them how to get one: retest the athletes a short time apart, when no true change is expected, with the same protocol and the same summary as the values compared.

Without a TE, you can describe the change, but you cannot separate it from noise. Do not flag. Do not use the spread of an athlete's own baseline values in place of TE.

Treat the SWC as a convention, with these limits:

- It depends on how alike the athletes are. A squad of similar athletes has a small SD, and so a small SWC.
- It is imprecise in a small squad.
- The observed between-athlete SD includes measurement error. The SD of the athletes' true scores is `sqrt(SD^2 - TE^2)`. This is derived by adding the variances.

### Build the baseline

Ask the user how to build the baseline: which period, and how many values. Do not invent a minimum count. Show `n` in the report. Mark a baseline built from few values as uncertain.

Rebuild the baseline when the athlete's situation changes, such as after a long break, a new training phase, or a new device. Say when you did.

A rolling baseline, such as the mean of the last 4 weeks, moves with the athlete. A slow, steady decline drags the baseline with it, so the decline never flags. Also compare to a fixed baseline from a stable period. Show the trend chart.

### Treat wellness scales with care

Wellness items scored 1 to 5 are ordinal: the steps are ranks, not equal amounts. A mean, a TE, and a noise band assume a continuous scale.

A single answer moves in whole steps, so a band can flag only certain answers. The 95 percent figure does not hold. An athlete who always answers 5 cannot rise, which shrinks the spread.

Show the raw answers next to any band. Call a band on a 1 to 5 item a rough guide. Apart from 2 studies of reliability and responsiveness, a systematic review found no validation studies of the single items most used in sport (Jeffries et al., 2020). So do not assume a published TE exists for a wellness item. A retest minutes apart cannot show day-to-day noise, and wellness states change from day to day. This is a practice judgment of this skill. For wellness answers, compare each answer with the athlete's own usual variation, as the wellness z-score in the `load-and-wellness` skill does. Label it as usual variation, not measurement error.

### Avoid z-score traps

A z-score is the distance of a value from a mean, in units of an SD. Avoid these traps:

- Do not let the SD include the new value. An extreme value then shrinks its own z-score.
- Do not trust an SD from few values.
- Do not read a squad z-score as individual change. It shows where the athlete sits in the squad.
- Do not use a cut point such as plus or minus 1.5 or plus or minus 2 unless the user gives a source for it.

### Expect false flags

With all assumptions met, about 5 percent of unchanged results fall beyond a 95 percent noise band when you look in both directions. When you look in one direction only, about 2.5 percent do.

When assumptions fail, the real rate can be higher or lower than 5 percent. It is higher when TE is too small, comes from few athletes, or varies between athletes. It can be lower when TE is overestimated, or when errors are positively correlated over time.

Across a squad, report the number of flags expected by chance next to the number found. Multiply the number of results by 5 percent, or by 2.5 percent for one direction.

With 30 athletes and 5 measures, you have 150 results. Expect about 7 or 8 changes beyond the band by chance in both directions.

With 25 athletes checked in one direction, expect 0.625 false flags a week. The chance of at least one is 46.9 percent. The flagged state, which also needs the SWC, is rarer by chance. Show this to the user.

Many more flags than that can mean the TE is too small or an assumption fails. It can also mean a real change across the squad, for example after a block of matches. Ask the user what happened before you judge.

Reduce false flags in these ways:

- Flag only the few measures the user chose before they saw the data.
- Recommend a repeat of a flagged test before anyone acts on a single flag, because of regression to the mean.
- Report how many flags to expect by chance next to the number you found.

Flags in consecutive weeks against the same baseline are not independent. They share the baseline, and a swing can last more than a week. Two flags in a row are not two separate confirmations.

An athlete picked because of an extreme value tends to be closer to average at the next test, without any real change (Barnett et al., 2005). A repeat test guards against this.

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They follow the formulas and the flag states above. The baseline holds only tests before the new test date, so the new value and any later test stay out of it. The band uses `sqrt(1 + 1/n)` with the baseline `n`, and the multiplier the user chose for the TE. A missing new value, a baseline shorter than the minimum the user set, a missing TE, or a missing SWC gives the state `No data`, never a flag. The change still shows when it can be computed.

Both versions assume one row per athlete, date, measure, and trial in a `measures` table, with the test in `measure_name`, such as `cmj_jump_height` in `cm`. They take the best trial on each test date with `MAX`, for a measure where higher is better. Use the same summary as the TE. Use `MIN` when lower is better, such as a sprint time. Use `AVERAGE` in Power BI and `AVG` in Tableau when the TE comes from the mean of trials. Change the summary everywhere it appears: `Test value (cm)` in Power BI, and the INCLUDE expressions in `Baseline n` and `Baseline mean (cm)` and `New value (cm)` in Tableau. They also assume a `reliability` table with one row per measure: `measure_name`, `te`, `te_df`, `te_source`, and `multiplier`. Enter 1.96 in `multiplier` for a TE from a large reliability study. For a TE from few athletes, enter the t multiplier for `te_df` from the assumptions list above, such as 2.57 for a TE from 6 athletes.

The user sets five things: the first and last dates of the baseline, the new test date, the minimum baseline `n`, and the direction that matters, `rise` or `fall`. Do not set the minimum for them. Show the results with one athlete per row. Show `Direction of change` next to `Flag wording`, so the reader sees which way each change went.

The SWC is 0.2 times the SD across athletes of each athlete's baseline mean. That uses the baseline mean as each athlete's score at baseline. This is this file's choice, so name it in the report. It uses every athlete with a baseline mean that the filters and slicers leave in the view, so set the comparison group with those filters.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. Add three tables that are not related to anything: `baseline_pick` and `new_pick`, each with one `date` column, and `direction_pick`, with one `direction` column holding `rise` and `fall`. Add a **Between** slicer on `baseline_pick[date]`, and single-select slicers on `new_pick[date]` and `direction_pick[direction]`. Set both baseline dates on the slicer. A **Between** slicer left untouched may apply no filter, and every state then reads `No data`. Add a whole-number what-if parameter `Min baseline tests` with a minimum of 1. Put `athletes[athlete_id]` in the visual. Use these DAX measures. They are measures because each one reads dates chosen in slicers, and the SWC reads every athlete in the group. A calculated column is computed once per row at data refresh and does not change with slicers (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options):

```text
Test value (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)

New value (cm) =
VAR d = SELECTEDVALUE ( new_pick[date] )
RETURN
    IF ( NOT ISBLANK ( d ), CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ), dates[date] = d ) )

Baseline n =
VAR d = SELECTEDVALUE ( new_pick[date] )
VAR vals =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@v", [Test value (cm)] ),
            DATESBETWEEN ( dates[date], MIN ( baseline_pick[date] ), MAX ( baseline_pick[date] ) )
        ),
        dates[date] <> d && NOT ISBLANK ( [@v] )
    )
RETURN IF ( ISFILTERED ( baseline_pick[date] ), COUNTROWS ( vals ) + 0 )

Baseline mean (cm) =
VAR d = SELECTEDVALUE ( new_pick[date] )
VAR vals =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@v", [Test value (cm)] ),
            DATESBETWEEN ( dates[date], MIN ( baseline_pick[date] ), MAX ( baseline_pick[date] ) )
        ),
        dates[date] <> d && NOT ISBLANK ( [@v] )
    )
RETURN IF ( ISFILTERED ( baseline_pick[date] ), AVERAGEX ( vals, [@v] ) )

Change (cm) =
VAR x = [New value (cm)]
VAR b = [Baseline mean (cm)]
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ),
        IF ( NOT ISBLANK ( x ) && NOT ISBLANK ( b ), x - b )
    )

Noise band (cm) =
VAR n = [Baseline n]
VAR te = LOOKUPVALUE ( reliability[te], reliability[measure_name], "cmj_jump_height" )
VAR m = LOOKUPVALUE ( reliability[multiplier], reliability[measure_name], "cmj_jump_height" )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ),
        IF ( n >= 1 && te > 0 && m > 0, m * te * SQRT ( 1 + 1 / n ) )
    )

SWC (cm) =
VAR vals =
    FILTER (
        ADDCOLUMNS ( ALLSELECTED ( athletes[athlete_id] ), "@b", [Baseline mean (cm)] ),
        NOT ISBLANK ( [@b] )
    )
RETURN IF ( COUNTROWS ( vals ) >= 2, 0.2 * STDEVX.S ( vals, [@b] ) )

Flag state =
VAR c = [Change (cm)]
VAR band = [Noise band (cm)]
VAR swc = [SWC (cm)]
VAR dir = SELECTEDVALUE ( direction_pick[direction] )
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ),
        SWITCH (
            TRUE (),
            ISBLANK ( c ) || [Baseline n] < [Min baseline tests Value] || ISBLANK ( band )
                || ISBLANK ( swc ) || ISBLANK ( dir ), "No data",
            ABS ( c ) <= band, "No flag",
            dir = "rise" && c - band > swc, "Flagged",
            dir = "fall" && c + band < -swc, "Flagged",
            "Noted"
        )
    )

Flag wording =
SWITCH (
    [Flag state],
    "No flag", "Within usual variation",
    "Noted", "Larger than measurement error; may or may not be worthwhile",
    "Flagged", "Larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation",
    "Not enough data"
)

Direction of change =
VAR c = [Change (cm)]
RETURN IF ( NOT ISBLANK ( c ), IF ( c > 0, "rise", IF ( c < 0, "fall", "none" ) ) )

Results checked =
COUNTROWS ( FILTER ( ALLSELECTED ( athletes[athlete_id] ), [Flag state] <> "No data" ) ) + 0

Changes beyond the band =
COUNTROWS ( FILTER ( ALLSELECTED ( athletes[athlete_id] ), [Flag state] IN { "Noted", "Flagged" } ) ) + 0

Expected beyond the band by chance =
0.05 * [Results checked]
```

`DATESBETWEEN` includes the first and last baseline dates (https://learn.microsoft.com/en-us/dax/datesbetween-function-dax). `dates[date] < d` keeps only tests before the new test date in the baseline, even when the baseline range runs past that date. The `HASONEVALUE` tests return a blank in a total row, where no single athlete is in the filter. Do not filter the visual on `Flag state` or `Flag wording`. That filter changes what `ALLSELECTED` returns, and so changes the SWC and the counts. To bring flags to the top, sort by `Flag state`, or use conditional formatting on the text without color bands. `Expected beyond the band by chance` counts both directions. Multiply `Results checked` by 0.025 instead to compare with the changes beyond the band in one direction.

In Tableau, relate `reliability` to `measures` on `measure_name`. Make five parameters: `Baseline start` and `Baseline end` as dates, `New date` as a date, `Min baseline tests` as an integer, and `Direction` as a string with the values `rise` and `fall`. Put `athlete_id` on Rows. To list athletes with no test, use a left join from the roster, as the Tableau setup reference in the `ams-data-setup` skill says. Use these calculations:

```text
Baseline test (cm) (row-level):
IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok"
   AND [measure_date] >= [Baseline start] AND [measure_date] <= [Baseline end]
   AND [measure_date] < [New date]
THEN [value] END

Baseline n (aggregate):
COUNT({ INCLUDE [measure_date] : MAX([Baseline test (cm)]) })

Baseline mean (cm) (aggregate):
AVG({ INCLUDE [measure_date] : MAX([Baseline test (cm)]) })

New value (cm) (aggregate):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok"
    AND [measure_date] = [New date] THEN [value] END)

Change (cm) (aggregate):
IF ISNULL([New value (cm)]) OR ISNULL([Baseline mean (cm)]) THEN NULL
ELSE [New value (cm)] - [Baseline mean (cm)]
END

TE (cm) (aggregate of a FIXED LOD):
MIN({ FIXED : MIN(IF [measure_name (reliability)] = "cmj_jump_height" THEN [te] END) })

Multiplier (aggregate of a FIXED LOD):
MIN({ FIXED : MIN(IF [measure_name (reliability)] = "cmj_jump_height" THEN [multiplier] END) })

Noise band (cm) (aggregate):
IF [Baseline n] >= 1 AND NOT ISNULL([TE (cm)]) AND [TE (cm)] > 0
   AND NOT ISNULL([Multiplier]) AND [Multiplier] > 0
THEN [Multiplier] * [TE (cm)] * SQRT(1 + 1 / [Baseline n])
END

Athletes with a baseline (table calculation):
WINDOW_SUM(IIF(ISNULL([Baseline mean (cm)]), 0, 1))

SWC (cm) (table calculation):
IF [Athletes with a baseline] < 2 THEN NULL
ELSE 0.2 * SQRT(MAX(0, ROUND(
    (WINDOW_SUM(ZN([Baseline mean (cm)]) * ZN([Baseline mean (cm)]))
     - WINDOW_SUM(ZN([Baseline mean (cm)])) * WINDOW_SUM(ZN([Baseline mean (cm)])) / [Athletes with a baseline])
    / ([Athletes with a baseline] - 1), 9)))
END

Flag state (table calculation):
IF ISNULL([Change (cm)]) OR [Baseline n] < [Min baseline tests]
   OR ISNULL([Noise band (cm)]) OR ISNULL([SWC (cm)]) THEN "No data"
ELSEIF ABS([Change (cm)]) <= [Noise band (cm)] THEN "No flag"
ELSEIF [Direction] = "rise" AND [Change (cm)] - [Noise band (cm)] > [SWC (cm)] THEN "Flagged"
ELSEIF [Direction] = "fall" AND [Change (cm)] + [Noise band (cm)] < -[SWC (cm)] THEN "Flagged"
ELSE "Noted"
END

Flag wording (table calculation):
CASE [Flag state]
WHEN "No flag" THEN "Within usual variation"
WHEN "Noted" THEN "Larger than measurement error; may or may not be worthwhile"
WHEN "Flagged" THEN "Larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation"
ELSE "Not enough data"
END

Direction of change (aggregate):
IF ISNULL([Change (cm)]) THEN NULL
ELSEIF [Change (cm)] > 0 THEN "rise"
ELSEIF [Change (cm)] < 0 THEN "fall"
ELSE "none"
END

Results checked (table calculation):
WINDOW_SUM(IIF([Flag state] = "No data", 0, 1))

Changes beyond the band (table calculation):
WINDOW_SUM(IIF([Flag state] = "Noted" OR [Flag state] = "Flagged", 1, 0))

Expected beyond the band by chance (table calculation):
0.05 * [Results checked]
```

The INCLUDE expressions take the best trial on each baseline date first, then count and average the dates. An athlete with 3 trials on one date then counts once for that date (https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm). Set **Compute Using** for every table calculation, including those used inside another one, to `athlete_id`. The SWC and the counts then cover every athlete in the view, which is the comparison group (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations.htm). Tableau lets you set **Compute Using** for each nested table calculation on its own, so set each one (https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations_custom.htm). The SD is built from sums, because Tableau Help does not say how `WINDOW_STDEV` treats null marks. `ROUND(..., 9)` and `MAX(0, ...)` stop rounding error from hiding a zero spread.

Blanks behave this way in each tool:

- Power BI: `STDEVX.S` returns an error, not a blank, with fewer than 2 values (https://learn.microsoft.com/en-us/dax/stdevx-s-function-dax). The `>= 2` test stops that, so the SWC is blank and the state reads `No data`.
- Power BI: a blank TE or multiplier compares as 0 (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types), so `te > 0` and `m > 0` are false and the band is blank. A blank `Baseline n` from an empty baseline slicer also gives `No data`.
- Tableau: `COUNT` and `AVG` skip baseline dates with no value (https://help.tableau.com/current/pro/desktop/en-us/functions_all_categories.htm). An athlete with no baseline value gets a null mean, and `Athletes with a baseline` leaves that athlete out of the SWC.
- Both: a reason-coded row is not `ok`, so it adds nothing to the baseline or the new value. A text value becomes null on import and counts as no test.

## Units and typical range

TE, the noise band, and the SWC are in the unit of the measure, or in percent. There is no universal value for any of them. Each depends on the test, the device, the protocol, and the athletes.

Do not use a value from a paper unless the test, device, and group match the user's. Do not state a typical range for them.

Error can differ between athletes, and can grow with the size of the value. One TE for the whole squad then flags too often for the less consistent athletes and too rarely for the more consistent ones. Ask whether some athletes vary more than others.

## Data you need

Collect this data before you flag:

- Source: the user's own short-term retest with no true change expected, and each athlete's earlier values
- Sampling: values from the same test, protocol, time of day, and summary
- Minimum data: a baseline of several values for each athlete, a TE from a short-term retest, and the between-athlete SD at baseline. Ask the user for the baseline rule. Do not set one.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often when they flag change:

- Flagging every change. Most small changes are noise.
- Calling a change worthwhile because the observed change passes the SWC. The change minus the noise band must pass the SWC.
- Comparing an athlete to the squad mean, and calling a difference between athletes a change
- Using one fixed cut point for all athletes, such as `drop of more than 10 percent`, with no source and no TE
- Using a `p < 0.05` result from a group test to flag one athlete
- Including the new value in the baseline. This shrinks the change.
- Building the baseline from few values and not saying so
- Using the standard error of the mean as noise
- Using the spread of an athlete's own baseline values as TE. It mixes real change with error, and a 1.96 band then flags far more than 5 percent of unchanged results.
- Taking TE from retests far enough apart for real change to occur. Real change then inflates TE.
- Building the t multiplier from the baseline `n`. Take its degrees of freedom from the TE study.
- Shading a chart band of `1.96 x TE` while flagging with `1.96 x TE x sqrt(1 + 1/n)`. The chart and the flags then disagree.
- Flagging on one extreme value and not asking for a repeat. Regression to the mean makes this common.
- Flagging 30 athletes on 20 measures and treating every flag as a finding
- Treating a larger-than-noise change as proof of a cause, an injury, or a need to rest
- Showing a percent change when the baseline is near zero. A small difference then looks huge.

## Example request

> Flag which athletes' jump height this week is different from their own normal, and ignore changes that are only testing noise.

Status: not tested.

## Check the result

Run these checks on the flags:

- Pick one flagged athlete. Recompute the baseline mean, the change, and the noise band by hand. Confirm they match.
- Count the changes beyond the noise band. Compare them to the number expected by chance: about 5 percent of the results checked in both directions, or 2.5 percent in one direction, when the assumptions hold.
- Check that no flagged change is inside the noise band, that no change has the flagged state unless the change minus the band passes the SWC, and that no athlete with no baseline is flagged.

## Sources

These sources support the formulas and rules in this file:

- Hopkins WG. Measures of reliability in sports medicine and science. *Sports Medicine*. 2000;30(1):1-15. doi:10.2165/00007256-200030010-00001. Defines the typical error, states that systematic changes in the mean between consecutive trials must be removed from it, and states that reasonable precision needs about 50 participants and at least 3 trials.
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. *Frontiers in Nutrition*. 2018;5:41. doi:10.3389/fnut.2018.00041. Source of TE from test-retest data over periods where true scores are not expected to change, the 95 percent range for an observed change, 1.96 x TE x sqrt(2), larger multiples for a TE from a small sample, the 0.2 x between-athlete SD smallest worthwhile change, and classifying a change by where the confidence interval for the true change lies.
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. *Sportscience*. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm. Accessed 2026-10-02. Its monitoring spreadsheet computes the error of a change from the mean of several reference tests as TE x sqrt(1 + 1/n), with t at the typical error's degrees of freedom.
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. *Medicine and Science in Sports and Exercise*. 2009;41(1):3-13. doi:10.1249/MSS.0b013e31818cb278. Lists 0.2 as the small standardized difference.
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. *International Journal of Epidemiology*. 2005;34(1):215-220. doi:10.1093/ije/dyh299. Explains that unusually large or small measurements tend to be followed by measurements closer to the mean.
- Jeffries AC, Wallace L, Coutts AJ, McLaren SJ, McCall A, Impellizzeri FM. Athlete-reported outcome measures for monitoring training responses: a systematic review of risk of bias and measurement property quality according to the COSMIN guidelines. *International Journal of Sports Physiology and Performance*. 2020;15(9):1203-1215. doi:10.1123/ijspp.2020-0386. Accessed 2026-10-02. Found measurement error inadequate for multiple-item measures. Apart from 2 studies of reliability and responsiveness, it found no validation studies of the single items most used in sport.
