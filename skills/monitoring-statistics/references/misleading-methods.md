# Methods that mislead: ACWR and group p-values

Last checked: 2026-10-02

## What it measures

This file covers two methods that often mislead in athlete monitoring: the acute:chronic workload ratio (ACWR) and group p-values used to judge individual athletes.

The ACWR divides a short-term (acute) training load by a longer-term (chronic) load. A p-value is the probability of data at least this extreme if there were no true effect and the model's assumptions hold (Wasserstein & Lazar, 2016). Neither one tells you whether one athlete's change is real or important.

## Formula

The ACWR has three common variants. Name the one you use:

```text
Coupled rolling average:   ACWR = acute_week / mean(last 4 weeks, acute week included)
Uncoupled rolling average: ACWR = acute_week / mean(3 weeks before the acute week)
EWMA:                      EWMA_today = load_today × λ + (1 − λ) × EWMA_yesterday
                           λ = 2 / (N + 1), N = 7 (acute) and N = 28 (chronic)
                           ACWR = EWMA_acute / EWMA_chronic
```

Define every term in the formula:

- `acute_week`: the total load of the last 7 days, in the load's units, such as arbitrary units (AU) from session rating of perceived exertion
- `mean(last 4 weeks)`: the mean weekly load over the last 28 days. In the coupled version it includes the acute week (Lolli et al., 2019a; Windt & Gabbett, 2019).
- `mean(3 weeks before)`: the mean weekly load of the 21 days before the acute week. This is the uncoupled version (Windt & Gabbett, 2019; Ren et al., 2024).
- `EWMA`: exponentially weighted moving average. It weights the last few days more than older days (Williams et al., 2017).
- `λ`: the decay rate, between 0 and 1. With N = 7, λ = 0.25. With N = 28, λ = 0.0690. Williams et al. (2017) set λ = 2 / (N + 1), with N the time decay constant, typically 7 and 28 days, and started both EWMAs at the day 1 load. The authors' accepted manuscript states both. With this λ, the EWMA has the same mean age of data, (N − 1) / 2 days, as an N-day rolling mean.
- `ACWR`: the ratio. It has no units.

The daily version of the coupled ratio, 7-day mean divided by 28-day mean, gives the same value as the weekly version.

## Calculate the ACWR and judge a group change

If the user asks for an ACWR, follow these steps and report it with its limits:

1. Arrange one row per athlete per calendar day, with columns `athlete_id`, `date`, and `load` in one unit.
2. Fill the `load` column with these rules:
   - Enter rest days as 0.
   - Mark days with no data as missing, not 0.
3. Pick and name the variant: coupled, uncoupled, or EWMA.
4. For the rolling versions, sum the load for the acute 7 days and for the chronic period, then divide.
5. For EWMA, set λ = 2 / (N + 1) and apply these rules:
   - Start the series on the first day's load.
   - State that start value.
6. Update the EWMA each day with `load_today × λ + (1 − λ) × EWMA_yesterday`.
7. Show the acute load and the chronic load next to the ratio, with units.
8. State which day the ratio was read on.
9. Add the limits from the sections below. Do not label the ratio as injury risk.

If the user asks whether a group change was "significant", follow these steps instead:

1. Report the group mean change with its units.
2. Label each athlete's change against typical error and the smallest worthwhile change. See the smallest worthwhile change reference.
3. Report how many athletes improved, declined, or stayed inside the noise.
4. If you report a p-value, put it after the individual results, with the sample size.

In the spreadsheet version, put daily load in column B from row 2, with rest days as 0 and missing days blank. Put the acute EWMA in column C, the chronic EWMA in column D, and the ratio in column E from row 29, day 28. On a missing day, each EWMA keeps the previous day's value instead of counting the day as 0, and the ratio stays blank on that day and the 27 days after it. Fill each formula down from the row shown:

```text
C2:  =IF(ISNUMBER(B2),B2,"")
D2:  =IF(ISNUMBER(B2),B2,"")
C3:  =IF(ISNUMBER(B3),IF(ISNUMBER(C2),B3*(2/(7+1))+(1-2/(7+1))*C2,B3),C2)
D3:  =IF(ISNUMBER(B3),IF(ISNUMBER(D2),B3*(2/(28+1))+(1-2/(28+1))*D2,B3),D2)
E29: =IF(COUNT(B2:B29)<28,"",C29/D29)
```

Python version:

```python
import pandas as pd

def ewma(load, n):
    """EWMA with lambda = 2/(n+1), started at the first day's load.
    On a missing day (NaN), it keeps the previous day's value."""
    return load.ewm(alpha=2 / (n + 1), adjust=False, ignore_na=True).mean()

# load: daily pd.Series, one row per calendar day, rest days as 0, missing days as NaN.
# Each ratio is blank before day 28, on a missing day, and on the 27 days after it.
full_28 = load.notna().rolling(28).sum() == 28
acwr_ewma = (ewma(load, 7) / ewma(load, 28)).where(full_28)
acwr_coupled = load.rolling(7).mean() / load.rolling(28).mean()
acwr_uncoupled = load.rolling(7).sum() / (load.shift(7).rolling(21).sum() / 3)
```

Keep `ignore_na=True`. With the pandas default, `ignore_na=False`, `ewm()` gives the first day after a gap extra weight, and the EWMA no longer matches the spreadsheet. On the worked example below, this code gives an EWMA ACWR of 1.0761 on day 42, the same as the spreadsheet.

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They follow steps 1 to 7 above. The series starts on the athlete's first day with a load row with status `ok`, at that day's load. Each value needs one athlete and one date in the visual. Rest days must be rows with a load of 0. A day with no load row is missing. As in the spreadsheet version, each EWMA keeps the previous day's value on a missing day, and the ratio is blank on that day and the 27 days after it. The ratio is also blank before day 28 and when the chronic EWMA is 0.

Report the acute and chronic loads next to the ratio, and add the limits from the sections below. Do not label the ratio as injury risk.

Both versions assume one row per athlete and calendar day with `measure_name` `daily_load` in one unit, such as AU, in a `measures` table.

In Power BI, use a marked date table `dates` related to `measures[measure_date]`. DAX has no step-by-step recursion, so these measures use the closed form of the same EWMA. With start load x0 and λ = 2 / (N + 1), each later recorded day i carries the weight λ × (1 − λ)^k, where k counts the recorded days after day i up to today. The start load carries (1 − λ)^k, where k counts every recorded day after the start. Missing days are not counted, so this equals the spreadsheet recursion, which skips a missing day. They are measures because each value reads every earlier day. The count runs once for each day, so a multi-year series in one visual can be slow:

```text
Daily load (AU) =
CALCULATE (
    SUM ( measures[value] ),
    measures[measure_name] = "daily_load",
    measures[status] = "ok"
)

Acute EWMA (AU) =
VAR n = 7
VAR lambda = 2 / ( n + 1 )
VAR today = MAX ( dates[date] )
VAR start =
    CALCULATE (
        MIN ( measures[measure_date] ),
        measures[measure_name] = "daily_load",
        measures[status] = "ok",
        REMOVEFILTERS ( dates )
    )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESBETWEEN ( dates[date], start, today )
        ),
        NOT ISBLANK ( [@x] )
    )
VAR x0 = MAXX ( FILTER ( recorded, dates[date] = start ), [@x] )
VAR k = COUNTROWS ( recorded ) - 1
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && NOT ISBLANK ( x0 ) && today >= start,
        POWER ( 1 - lambda, k ) * x0
            + SUMX (
                FILTER ( recorded, dates[date] > start ),
                VAR d = dates[date]
                VAR later = COUNTROWS ( FILTER ( recorded, dates[date] > d ) )
                RETURN lambda * POWER ( 1 - lambda, later ) * [@x]
            )
    )

Chronic EWMA (AU) =
VAR n = 28
VAR lambda = 2 / ( n + 1 )
VAR today = MAX ( dates[date] )
VAR start =
    CALCULATE (
        MIN ( measures[measure_date] ),
        measures[measure_name] = "daily_load",
        measures[status] = "ok",
        REMOVEFILTERS ( dates )
    )
VAR recorded =
    FILTER (
        CALCULATETABLE (
            ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
            DATESBETWEEN ( dates[date], start, today )
        ),
        NOT ISBLANK ( [@x] )
    )
VAR x0 = MAXX ( FILTER ( recorded, dates[date] = start ), [@x] )
VAR k = COUNTROWS ( recorded ) - 1
RETURN
    IF (
        HASONEVALUE ( athletes[athlete_id] ) && HASONEVALUE ( dates[date] )
            && NOT ISBLANK ( x0 ) && today >= start,
        POWER ( 1 - lambda, k ) * x0
            + SUMX (
                FILTER ( recorded, dates[date] > start ),
                VAR d = dates[date]
                VAR later = COUNTROWS ( FILTER ( recorded, dates[date] > d ) )
                RETURN lambda * POWER ( 1 - lambda, later ) * [@x]
            )
    )

Recorded days in last 28 =
VAR today = MAX ( dates[date] )
RETURN
    COUNTROWS (
        FILTER (
            CALCULATETABLE (
                ADDCOLUMNS ( VALUES ( dates[date] ), "@x", [Daily load (AU)] ),
                DATESBETWEEN ( dates[date], today - 27, today )
            ),
            NOT ISBLANK ( [@x] )
        )
    ) + 0

EWMA ratio =
VAR a = [Acute EWMA (AU)]
VAR c = [Chronic EWMA (AU)]
RETURN
    IF (
        [Recorded days in last 28] = 28 && NOT ISBLANK ( a ) && NOT ISBLANK ( c ) && c <> 0,
        a / c
    )
```

In Tableau, make a scaffold table with one row for every athlete and every calendar date. Left join `measures` to the scaffold on `athlete_id` and on scaffold `date` equal to `measure_date`. A day with no load row then has a mark with a null load. Use these calculations:

```text
Daily load (AU) (aggregate):
SUM(IF [measure_name] = "daily_load" AND [status] = "ok" THEN [value] END)

First load date (FIXED LOD):
{ FIXED [athlete_id] : MIN(IF [measure_name] = "daily_load" AND [status] = "ok" AND NOT ISNULL([value]) THEN [measure_date] END) }

On or after first load (row-level, use as a filter set to True):
[date] >= [First load date]

Acute EWMA (AU) (table calculation):
IF ISNULL([Daily load (AU)]) THEN PREVIOUS_VALUE([Daily load (AU)])
ELSE (2 / (7 + 1)) * [Daily load (AU)] + (1 - 2 / (7 + 1)) * PREVIOUS_VALUE([Daily load (AU)])
END

Chronic EWMA (AU) (table calculation):
IF ISNULL([Daily load (AU)]) THEN PREVIOUS_VALUE([Daily load (AU)])
ELSE (2 / (28 + 1)) * [Daily load (AU)] + (1 - 2 / (28 + 1)) * PREVIOUS_VALUE([Daily load (AU)])
END

Recorded days in last 28 (table calculation):
WINDOW_SUM(IIF(ISNULL([Daily load (AU)]), 0, 1), -27, 0)

EWMA ratio (table calculation):
IF [Recorded days in last 28] < 28 THEN NULL
ELSEIF ISNULL([Acute EWMA (AU)]) OR ISNULL([Chronic EWMA (AU)]) THEN NULL
ELSEIF [Chronic EWMA (AU)] = 0 THEN NULL
ELSE [Acute EWMA (AU)] / [Chronic EWMA (AU)]
END
```

`PREVIOUS_VALUE` returns this calculation's value on the previous day. On the first day it returns its argument, the first day's load, so the EWMA starts at λ × x0 + (1 − λ) × x0 = x0, as `C2` does in the spreadsheet. On a day with a null load, the EWMA returns the previous day's value. `Recorded days in last 28` counts the days with a load in the 28 days ending on each day. Before day 28 the window holds fewer than 28 days, so the ratio is null.

Put the scaffold's `athlete_id` on Rows and the scaffold `date` as an exact day on Columns. Use the scaffold's fields, not the `measures` fields, in the view and in `First load date`, so days with no row keep their athlete and date. Set **Compute Using** for each table calculation to **Specific Dimensions**, with `date` checked and `athlete_id` unchecked. The `On or after first load` filter is a dimension filter on purpose: it runs before the table calculations, so each series starts on its first load day. FIXED expressions run before dimension filters, so the first load date is not cut by that filter. Use a table calculation filter, not a date filter, to show a shorter range.

Blanks behave this way in each tool:

- Power BI: a day with no row gives a blank daily load. The EWMA leaves that day out of `recorded` and keeps the previous value. `Recorded days in last 28` is below 28 on that day and the 27 days after it, so the ratio is blank. A rest day stored as 0 is a value, not a gap.
- Tableau: a null daily load makes the EWMA return the previous day's value. `Recorded days in last 28` is below 28 on that day and the 27 days after it, so the ratio is null.
- Both: a text load becomes null on import and counts as a missing day, as text does in the spreadsheet.
- Both: a chronic EWMA of 0 gives a blank ratio, where the spreadsheet gives `#DIV/0!`.

## Worked example

The three examples below show how the ACWR variant, mathematical coupling, and sample size change the result.

### Same load series, four ACWR values

One athlete trained for 6 weeks, with similar loads in weeks 1 to 5 and a heavier week 6. The last day of week 6 was a rest day. These are made-up numbers for illustration.

| Week | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Total (AU) |
|---|---|---|---|---|---|---|---|---|
| 1 | 300 | 450 | 0 | 500 | 350 | 600 | 0 | 2200 |
| 2 | 320 | 460 | 0 | 480 | 380 | 560 | 0 | 2200 |
| 3 | 310 | 470 | 0 | 520 | 360 | 580 | 0 | 2240 |
| 4 | 330 | 440 | 0 | 510 | 370 | 590 | 0 | 2240 |
| 5 | 300 | 480 | 0 | 500 | 350 | 620 | 0 | 2250 |
| 6 | 600 | 700 | 0 | 650 | 500 | 800 | 0 | 3250 |

Day 1 of week 1 is day 1 of the series. Day 7 of week 6 is day 42.

Work through the rolling versions:

1. Acute load = week 6 = 3250 AU.
2. Coupled chronic = (2240 + 2240 + 2250 + 3250) / 4 = 2495.00 AU per week.
3. Coupled ACWR = 3250 / 2495.00 = 1.3026.
4. Daily check: 7-day mean 464.2857 AU divided by 28-day mean 356.4286 AU = 1.3026.
5. Uncoupled chronic = (2240 + 2240 + 2250) / 3 = 2243.33 AU per week.
6. Uncoupled ACWR = 3250 / 2243.33 = 1.4487.

Work through the EWMA version:

1. λ acute = 2 / 8 = 0.25. λ chronic = 2 / 29 = 0.0690.
2. Day 1 starts both series at 300 AU. Day 2 acute = 450 × 0.25 + 0.75 × 300 = 337.5 AU.
3. On day 42, a rest day, EWMA acute = 397.0859 AU and EWMA chronic = 369.0058 AU.
4. EWMA ACWR on day 42 = 1.0761.
5. On day 41, the last training day, EWMA ACWR = 529.4478 / 396.3396 = 1.3358.

Days 41 and 42 fall before day 56, so both EWMA values are start-up values. They are shown only to compare the methods. Do not report an EWMA ACWR before day 56 to a coach without the same value from a second start value beside it.

Result: the same 6 weeks of training give 1.30, 1.45, 1.08, or 1.34, depending on the variant and the day you read it.

### Coupled loads create a correlation from nothing

Simulate 1000 athletes with 4 weeks of random, independent weekly loads (mean 2000 AU, SD 400 AU). By design, the acute week has no link to the earlier weeks.

1. Correlation between the acute week and the coupled chronic load = 0.5160.
2. Correlation between the acute week and the uncoupled chronic load = 0.0044.

The coupled chronic load contains the acute week, so the two correlate with no biological link. Lolli et al. reported the same artifact, about r = 0.50 (Windt & Gabbett, 2019; Lolli et al., 2019a).

```python
import numpy as np

rng = np.random.default_rng(2026)
w = rng.normal(2000, 400, size=(1000, 4))     # 1000 athletes, 4 independent weeks (AU)
acute = w[:, 3]
print(np.corrcoef(acute, w.mean(axis=1))[0, 1])       # coupled chronic
print(np.corrcoef(acute, w[:, :3].mean(axis=1))[0, 1])  # uncoupled chronic
```

### A group p-value hides the individuals

Ten athletes did a CMJ before and after a training block. TE is 0.6284 cm and the SWC is 0.6185 cm, from the typical error reference and the smallest worthwhile change reference. These are made-up numbers for illustration.

| Input | Value |
|---|---|
| Changes (cm) | +2.2, −0.3, +1.9, −0.8, +2.3, +0.7, −0.8, +2.3, +0.7, −0.5 |
| Mean change | 0.77 cm, SD of changes 1.3208 cm |
| Paired t-test, n = 10 | t = 1.8435, p = 0.0984 |

Work through the individual view at the default 95% level, with a noise band of 1.96 × √2 × 0.6284 = 1.7418 cm:

1. Four athletes (+2.2, +1.9, +2.3, +2.3) changed by more than measurement error.
2. None of the four is clearly larger than the SWC. For the largest, 2.3 − 1.7418 = 0.5582 cm, which is not beyond 0.6185 cm. Each reads as "real, possibly as large as the SWC".
3. Six athletes are inside the noise. Four of the 10 changes are negative.
4. The TE came from 6 athletes, so t(5) = 2.5706 strictly applies. The band becomes 2.2845 cm, and only the two +2.3 cm changes stay beyond it. The conclusion is the same: the group p-value does not say which athletes changed.

Next, take a squad of 40 with the same pattern of changes, the same 10 changes four times. The mean change is 0.77 cm, but p = 0.000444.

Result: at n = 10 the group test is "not significant", but 4 athletes changed by more than noise with z = 1.96, or 2 with t(5). At n = 40 the same changes are "highly significant".

The p-value moved with the sample size. It said nothing about which athletes changed.

## What changes the number

These choices change the ACWR even when the training does not change:

- **Coupled versus uncoupled.** In the worked example, the coupled ratio is 1.3026 and the uncoupled ratio is 1.4487.
- **Rolling versus EWMA.** On day 42, the rolling ratio is 1.3026 and the EWMA ratio is 1.0761.
- **The day you read it.** EWMA ACWR was 1.3358 on day 41 and 1.0761 on day 42, a rest day.
- **Order of sessions within the week.** With the same week 6 total of 3250 AU, reordered as 800, 650, 600, 700, 500, 0, 0, the rolling ACWR stays 1.3026. The EWMA ACWR drops to 0.8539.
- **EWMA start value.** Starting with the week 1 mean instead of the day 1 load gives 1.0740 instead of 1.0761. The effect is larger in short series.
- **pandas `adjust` setting.** `ewm(adjust=True)` gives 1.0657 on day 42 instead of 1.0761 from the published recursion.
- **Missing days entered as 0.** A missing day counted as rest lowers both loads and shifts the ratio.

These choices change a p-value even when the effect does not change:

- **Sample size.** The same changes gave p = 0.0984 at n = 10 and p = 0.000444 at n = 40.
- **Measurement noise.** More noise widens the spread of changes and raises p, for the same true effect (Batterham & Hopkins, 2006).

## Why ACWR misleads

These problems are documented in the peer-reviewed literature:

- **Mathematical coupling.** In the coupled version, the acute week is part of the chronic load. That builds in a spurious correlation of about 0.50 between the two (Lolli et al., 2019a; Windt & Gabbett, 2019).
- **Ratio assumptions.** A ratio adjusts properly only if the numerator is truly proportional to the denominator. The adjustment must also work the same way across the whole range (Lolli et al., 2019b). The ACWR fails to normalize acute load by chronic load, even in the uncoupled version (Impellizzeri et al., 2020).
- **Noise and artifacts.** The ratio adds noise and creates statistical artifacts (Impellizzeri et al., 2020).
- **A rescaled numerator.** Dividing acute load by fixed or random made-up chronic loads gave injury associations similar to the real ACWR. The ratio mostly rescales acute load (Impellizzeri et al., 2021).
- **No causal evidence.** No study has shown that changing the ACWR changes injury rates (Impellizzeri et al., 2020).
- **The EWMA fixes one problem only.** EWMA addresses the decay of fitness and fatigue that rolling averages ignore (Williams et al., 2017). It is a ratio, so the ratio problems above remain.

## Why group p-values mislead for individual monitoring

These problems are documented in the peer-reviewed literature:

- A p-value does not measure the size of an effect or its importance (Wasserstein & Lazar, 2016).
- Decisions should not rest only on whether p passes a threshold (Wasserstein & Lazar, 2016).
- Null-hypothesis testing is inadequate for judging practical importance (Hopkins et al., 2009). A p-value depends on the size of the effect, the measurement error, and the sample size (Batterham & Hopkins, 2006).
- A group can improve on average while some athletes get worse. Sands et al. (2019) show a group with p = 0.048 in which the three best jumpers declined.
- Measurement error limits what you can say about one athlete, and a larger squad does not fix a low signal-to-noise ratio for one athlete (Hecksteden et al., 2015).
- Random variation within athletes can create apparent differences in response, even when the true response is the same for everyone (Atkinson & Batterham, 2015).

## Units and typical range

The ACWR has no units. A p-value is a probability between 0 and 1.

This file gives no ACWR "safe" range or injury threshold. The sources above find no evidence to support one (Impellizzeri et al., 2020; Impellizzeri et al., 2021).

## Data you need

You need these data to compute an ACWR:

- Source: daily training load for one athlete, in one unit
- Sampling: every calendar day, with rest days as 0 and missing days marked missing
- Minimum data: 28 days for both rolling ratios. The uncoupled ratio uses 7 acute days plus 21 chronic days. For EWMA, early values depend on the start value. Say so.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with these methods:

- Calling the ACWR an injury-risk score. It is not. Report it as a load description only.
- Applying a published "sweet spot" range as a safety threshold. No source supports a causal threshold (Impellizzeri et al., 2020).
- Not naming the variant. Coupled, uncoupled, and EWMA ratios differ for the same data.
- Mixing daily means and weekly totals in one ratio
- Entering missing days as 0, or dropping rest days, which changes the averages
- Writing the EWMA with the weights swapped, `load × (1 − λ) + λ × EWMA_yesterday`
- Using `adjust=True` in pandas `ewm`, which is a different weighting from the published recursion. Use `adjust=False`.
- Showing only the ratio. Show the acute and chronic loads too.
- Reporting "the team improved significantly" as if every athlete improved. Label each athlete's change against noise.
- Running a t-test on one athlete's daily values to call a change "significant". Use typical error, the MDC, and the SWC instead.

## Example request

> Calculate the acute to chronic workload ratio for each player from this daily session RPE log, and tell me who is in the danger zone.

The correct answer computes the named variant, shows acute and chronic loads, and explains that no validated danger zone exists.

## Check the result

Run these checks on the result:

- Recompute one athlete's acute load, chronic load, and ratio by hand.
- Confirm the answer names the variant, the read date, and the units of load.
- Confirm no answer labels a ratio, a z-score, or a p-value as an injury risk or a clearance decision.

## Sources

- Lolli L, Batterham AM, Hawkins R, Kelly DM, Strudwick AJ, Thorpe R, Gregson W, Atkinson G. Mathematical coupling causes spurious correlation within the conventional acute-to-chronic workload ratio calculations. British Journal of Sports Medicine. 2019;53(15):921-922. https://doi.org/10.1136/bjsports-2017-098110 (cited as Lolli et al., 2019a)
- Lolli L, Batterham AM, Hawkins R, Kelly DM, Strudwick AJ, Thorpe RT, Gregson W, Atkinson G. The acute-to-chronic workload ratio: an inaccurate scaling index for an unnecessary normalisation process? British Journal of Sports Medicine. 2019;53(24):1510-1512. https://doi.org/10.1136/bjsports-2017-098884 (cited as Lolli et al., 2019b)
- Windt J, Gabbett TJ. Is it all for naught? What does mathematical coupling mean for acute:chronic workload ratios? British Journal of Sports Medicine. 2019;53(16):988-990. https://doi.org/10.1136/bjsports-2017-098925
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. International Journal of Sports Physiology and Performance. 2020;15(6):907-913. https://doi.org/10.1123/ijspp.2019-0864
- Impellizzeri FM, Woodcock S, Coutts AJ, Fanchini M, McCall A, Vigotsky AD. What role do chronic workloads play in the acute to chronic workload ratio? Time to dismiss ACWR and its underlying theory. Sports Medicine. 2021;51(3):581-592. https://doi.org/10.1007/s40279-020-01378-6
- Williams S, West S, Cross MJ, Stokes KA. Better way to determine the acute:chronic workload ratio? British Journal of Sports Medicine. 2017;51(3):209-210. https://doi.org/10.1136/bjsports-2016-096589. Accepted manuscript: https://purehost.bath.ac.uk/ws/files/147466466/BJSM_correspondence_alternative_to_rolling_averages_r1.pdf (accessed 2026-10-02)
- Murray NB, Gabbett TJ, Townshend AD, Blanch P. Calculating acute:chronic workload ratios using exponentially weighted moving averages provides a more sensitive indicator of injury likelihood than rolling averages. British Journal of Sports Medicine. 2017;51(9):749-754. https://doi.org/10.1136/bjsports-2016-097152
- Ren X, Boisbluche S, Philippe K, Demy M, Hu X, Ding S, Prioux J. Assessing pre-season workload variation in professional rugby union players by comparing three acute:chronic workload ratio models based on playing positions. Heliyon. 2024;10(17):e37176. https://doi.org/10.1016/j.heliyon.2024.e37176
- Wasserstein RL, Lazar NA. The ASA statement on p-values: context, process, and purpose. The American Statistician. 2016;70(2):129-133. https://doi.org/10.1080/00031305.2016.1154108
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. Medicine and Science in Sports and Exercise. 2009;41(1):3-13. https://doi.org/10.1249/MSS.0b013e31818cb278
- Batterham AM, Hopkins WG. Making meaningful inferences about magnitudes. International Journal of Sports Physiology and Performance. 2006;1(1):50-57. https://doi.org/10.1123/ijspp.1.1.50
- Sands W, Cardinale M, McNeal J, Murray S, Sole C, Reed J, Apostolopoulos N, Stone M. Recommendations for measurement and management of an elite athlete. Sports. 2019;7(5):105. https://doi.org/10.3390/sports7050105
- Hecksteden A, Kraushaar J, Scharhag-Rosenberger F, Theisen D, Senn S, Meyer T. Individual response to exercise training: a statistical perspective. Journal of Applied Physiology. 2015;118(12):1450-1459. https://doi.org/10.1152/japplphysiol.00714.2014
- Atkinson G, Batterham AM. True and false interindividual differences in the physiological response to an intervention. Experimental Physiology. 2015;100(6):577-588. https://doi.org/10.1113/EP085070
