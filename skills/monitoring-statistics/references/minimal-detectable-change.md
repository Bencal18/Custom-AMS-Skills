# Minimal detectable change

Last checked: 2026-10-02

## What it measures

The minimal detectable change (MDC) is the smallest change in one athlete's score that is larger than measurement noise, at a stated confidence level (Weir, 2005; de Vet et al., 2006).

Weir (2005) calls it the minimal difference (MD). Other names are smallest detectable change and smallest real change (de Vet et al., 2006).

## Formula

Use the confidence level the user picks. If they have no preference, use MDC95 as this skill's default. That default is a choice that matches common MDC95 reporting. Offer MDC90 as an option:

```text
MDC95 = SEM × 1.96 × √2
MDC90 = SEM × 1.645 × √2
MDCz  = SEM × z × √2
```

Define every term in the formula:

- `SEM`: the standard error of measurement, in the units of the measure. With two trials, `SEM = SD(diff) / √2`, which is the same as typical error (Weir, 2005). See the typical error reference.
- `1.96`: the z value for a 95% confidence interval. Another z value gives a looser or stricter threshold (Weir, 2005).
- `1.645`: the z value for a 90% confidence interval (Swinton et al., 2018)
- `√2`: the square root of 2. A change involves two measurements, and each has error (Weir, 2005; de Vet et al., 2006).
- `MDC`: the minimal detectable change, in the units of the measure

Use these variants when they fit:

- **MDC95.** The common reporting standard (Weir, 2005; de Vet et al., 2006; Furlan & Sterr, 2018). It equals about 2.77 × SEM.
- **MDC90.** A less strict threshold. It equals about 2.33 × SEM.
- **Practical threshold.** Hopkins (2000) judges the 95% level too strict for monitoring one athlete. When the smallest important change is set to zero, his monitoring spreadsheet by default flags a single change larger than about 2.0 × TE. Pure noise then gives flagged increases 10% of the time and flagged decreases 10% of the time (Hopkins, 2017). He suggests an observed change of about 1.5 to 2.0 × typical error as a realistic threshold for a real change. Offer it as an option with its cost. For two single tests and pure noise, a threshold of 1.5 × TE flags 28.9% of changes (14.4% in one direction). A threshold of 2.0 × TE flags 15.7% (7.9%), against 5% at 2.77 × TE.
- **Against a baseline mean.** MDC95 is the noise band for two single tests. For a new value against a baseline mean of n values, use `1.96 × SEM × √(1 + 1/n)`. This form adds variances. Hopkins (2017) uses the same error for a change from the mean of several tests. With n = 1, it equals MDC95. The individual baselines and z-scores reference lists the assumptions.
- **Regression-based version.** Weir (2005) notes that a more exact interval uses the estimated true score and the standard error of prediction, `SEP = SD × √(1 − ICC²)`. Use it only if the user asks.
- **Small TE study.** If the SEM comes from few athletes, replace 1.96 with t from the TE study's degrees of freedom: athletes − 1 for two trials. An SEM from 6 athletes gives t(5) = 2.57 (Swinton et al., 2018).

MDC95 is a noise band. Error alone gives a change smaller than MDC95 about 95 percent of the time. When only one direction matters, such as a drop, the chance rate of a false flag is 2.5%, not 5%.

When the assumptions fail, the real rate can be higher or lower than 5%. Never call 5% a lower bound.

## Calculate the MDC

Follow these steps to calculate the MDC and apply it:

1. Get the SEM for the test, in the units of the measure, from a short-term test-retest study with the same protocol. See the typical error reference.
2. Pick the confidence level, and its z value: 1.96 for 95%, the default, or 1.645 for 90%.
3. Multiply: `MDC = SEM × z × 1.4142`.
4. For each athlete, compute `change = new_value − old_value`, from the columns that hold the two test results.
5. Compare the size of the change with the MDC. A change larger than the MDC is larger than noise at that confidence level.
6. Report the MDC with its confidence level, the SEM source, and the units.

Spreadsheet version, with the SEM in cell `E1`, old results in column `B`, and new results in column `C`. Each formula returns a blank when an input it needs is blank or not a number:

```text
MDC95 (E2):          =IF(ISNUMBER(E1),E1*1.96*SQRT(2),"")
MDC90 (E3):          =IF(ISNUMBER(E1),E1*1.645*SQRT(2),"")
Beyond MDC95? (D2):  =IF(OR(COUNT(B2,C2)<2,$E$2=""),"",ABS(C2-B2)>$E$2)
```

Python version:

```python
import math

def mdc(sem, z=1.96):
    """Minimal detectable change. z=1.96 for 95 %, 1.645 for 90 %."""
    return sem * z * math.sqrt(2)

sem = 0.6284                              # cm, from a short-term test-retest study
print(f"MDC95 = {mdc(sem):.4f} cm, MDC90 = {mdc(sem, 1.645):.4f} cm")
```

### Calculate it in Power BI and Tableau

These versions are not tested in Power BI or Tableau. They return a blank MDC when the SEM is missing, so the band never collapses to 0. They compare a change with the MDC only when both tests and the SEM exist. Otherwise they say `not enough data`.

Both versions assume one row per athlete, date, measure, and trial in a `measures` table, and a `reliability` table with one row per measure: `measure_name`, `te` (the SEM, in the unit of the measure), `te_df`, and `te_source`. The user picks the old and the new test dates. Show the results with one athlete per row.

In Power BI, add two single-select date slicers on two tables that are not related to anything, `old_pick` and `new_pick`, each with one `date` column. With no date picked, the old or new value is blank. Use these DAX measures. They are measures because they combine two dates chosen in slicers:

```text
SEM (cm) =
LOOKUPVALUE ( reliability[te], reliability[measure_name], "cmj_jump_height" )

MDC95 (cm) =
VAR sem = [SEM (cm)]
RETURN IF ( NOT ISBLANK ( sem ) && sem > 0, sem * 1.96 * SQRT ( 2 ) )

MDC90 (cm) =
VAR sem = [SEM (cm)]
RETURN IF ( NOT ISBLANK ( sem ) && sem > 0, sem * 1.645 * SQRT ( 2 ) )

Test value (cm) =
CALCULATE (
    MAX ( measures[value] ),
    measures[measure_name] = "cmj_jump_height",
    measures[unit] = "cm",
    measures[status] = "ok"
)

Old value (cm) =
VAR d = SELECTEDVALUE ( old_pick[date] )
RETURN
    IF ( NOT ISBLANK ( d ), CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ), dates[date] = d ) )

New value (cm) =
VAR d = SELECTEDVALUE ( new_pick[date] )
RETURN
    IF ( NOT ISBLANK ( d ), CALCULATE ( [Test value (cm)], REMOVEFILTERS ( dates ), dates[date] = d ) )

Beyond MDC95 =
VAR o = [Old value (cm)]
VAR n = [New value (cm)]
VAR mdc = [MDC95 (cm)]
RETURN
    IF (
        ISBLANK ( o ) || ISBLANK ( n ) || ISBLANK ( mdc ),
        "not enough data",
        IF ( ABS ( n - o ) > mdc, "beyond MDC95", "within MDC95" )
    )
```

In Tableau, relate `reliability` to `measures` on `measure_name`. The SEM calculation picks the CMJ row of `reliability` itself, because the view does not filter `measure_name`, and a plain `MIN([te])` would return the smallest TE of every measure the athlete has. Make two date parameters, `Old date` and `New date`. Put `athlete_id` on Rows. Use these aggregate calculations:

```text
SEM (cm) (aggregate of a FIXED LOD):
MIN({ FIXED : MIN(IF [measure_name (reliability)] = "cmj_jump_height" THEN [te] END) })

MDC95 (cm):
IF ISNULL([SEM (cm)]) OR [SEM (cm)] <= 0 THEN NULL ELSE [SEM (cm)] * 1.96 * SQRT(2) END

MDC90 (cm):
IF ISNULL([SEM (cm)]) OR [SEM (cm)] <= 0 THEN NULL ELSE [SEM (cm)] * 1.645 * SQRT(2) END

Old value (cm):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" AND [measure_date] = [Old date] THEN [value] END)

New value (cm):
MAX(IF [measure_name] = "cmj_jump_height" AND [unit] = "cm" AND [status] = "ok" AND [measure_date] = [New date] THEN [value] END)

Beyond MDC95:
IF ISNULL([Old value (cm)]) OR ISNULL([New value (cm)]) OR ISNULL([MDC95 (cm)]) THEN "not enough data"
ELSEIF ABS([New value (cm)] - [Old value (cm)]) > [MDC95 (cm)] THEN "beyond MDC95"
ELSE "within MDC95"
END
```

Blanks behave this way in each tool:

- Power BI: a blank SEM gives a blank MDC, not 0. A blank compared with a number counts as 0, so a plain `ABS ( n - o ) > mdc` would flag a missing test. The `ISBLANK` tests come first.
- Tableau: a missing test gives a null value. The `ISNULL` tests return `not enough data` before any comparison.
- Both: the label is never blank, so an athlete with no tests still gets a row that reads `not enough data`. That keeps untested athletes visible.
- Both: a text SEM becomes null on import, so the MDC is blank, as in the spreadsheet formula.

## Worked example

The CMJ test has an SEM of 0.6284 cm, from the worked example in the typical error reference. One athlete jumped 40.3 cm last month and 41.9 cm today. These are made-up numbers for illustration.

| Input | Value |
|---|---|
| SEM | 0.6284 cm |
| Old value | 40.3 cm |
| New value | 41.9 cm |

Work through the calculation:

1. √2 = 1.4142, so SEM × √2 = 0.8887 cm.
2. MDC95 = 0.6284 × 1.96 × 1.4142 = 1.7418 cm.
3. MDC90 = 0.6284 × 1.645 × 1.4142 = 1.4619 cm.
4. Change = 41.9 − 40.3 = 1.6 cm.
5. 1.6 cm is larger than MDC90 but smaller than MDC95.

Result: at the default 95% level, the 1.6 cm change is inside the noise band. Report it as "not larger than measurement error at 95%".

If the user chose 90%, the same change would count as larger than noise. Report the level with the result, and let the practitioner decide what to do with it.

## What changes the number

These choices change the MDC even when the athlete does not change:

- **Confidence level.** In the worked example, MDC95 is 1.7418 cm and MDC90 is 1.4619 cm. The same 1.6 cm change fails MDC95 and passes MDC90.
- **Small TE study.** The SEM of 0.6284 cm came from 6 athletes. With t(5) = 2.5706, the band is 2.5706 × 0.6284 × 1.4142 = 2.2845 cm, and the 1.6 cm change is inside it.
- **Baseline mean of n values.** Against a mean of 8 prior tests, the 95% band is 1.96 × 0.6284 × √(1 + 1/8) = 1.3064 cm, smaller than MDC95.
- **Practical threshold.** Hopkins's 1.5 × TE and 2.0 × TE give 0.9426 cm and 1.2568 cm (Hopkins, 2000).
- **Leaving out √2.** `1.96 × SEM` gives 1.2317 cm, which is 29% too small. It makes noise look like change.
- **Which SEM.** An SEM from a different protocol, from tests weeks apart, or from an ICC formula on a different group changes the MDC (Weir, 2005).
- **Individual versus group.** For the mean change of a group of 6, the 95% noise is `t × SEM × √2 / √n` = 2.5706 × 0.6284 × 1.4142 / 2.4495 = 0.9326 cm (Hopkins, 2000). Do not apply that to one athlete.

## MDC compared with SWC

MDC and the smallest worthwhile change (SWC) answer two different questions:

| Question | Statistic | Built from |
|---|---|---|
| Is the change bigger than noise? | MDC | Measurement error (SEM or typical error) |
| Is the change big enough to matter? | SWC | Spread between athletes (0.2 × SD), or a practical value |

The MDC depends on measurement error. A minimal important change depends on what athletes or practitioners judge important. The two are different ideas (de Vet et al., 2006).

A change can exceed the MDC and be too small to matter. A change can be large enough to matter and sit inside the noise.

Report both. Use the interval rule in the smallest worthwhile change reference to label each change. At the same confidence level, "the interval `change ± z × √2 × SEM` excludes zero" is the same test as "the size of the change is larger than the MDC".

## Units and typical range

MDC has the same units as the measure. If SEM is a CV%, the MDC is a percent change.

This file gives no typical MDC values. The MDC depends on the test, the protocol, and the athletes. Compute it from your own reliability data or from a published study that used the same protocol.

## Data you need

You need these data to compute the MDC:

- Source: an SEM or typical error from repeated tests of the same athletes, with no real change between tests
- Timing: a short-term reliability study, so that the SEM holds only noise (Hopkins, 2000)
- Minimum data: Weir (2005) states there is no consensus on how many athletes give a stable SEM. Report the number of athletes and trials.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with the MDC:

- Leaving out √2. `1.96 × SEM` is the interval around one score, not around a change. The MDC needs both measurements' error (Weir, 2005).
- Using the SD of the raw scores instead of the SEM. That puts the spread between athletes into a threshold meant for noise. Use the SEM.
- Using an SEM from an ICC computed on a different population. The ICC version of SEM shifts with how varied the sample is (Weir, 2005). Prefer an SEM from difference scores or `√MSE`.
- Applying an individual MDC to a group mean, or a group-mean threshold to one athlete. The noise in a change of a group mean is smaller: `t × TE × √2 / √n` for n athletes (Hopkins, 2000).
- Calling a change "clinically important" because it exceeds the MDC. The MDC shows detectability only (de Vet et al., 2006).
- Forgetting to state the confidence level. Always write MDC95 or MDC90.
- Mixing units. Use an SEM in centimeters with a change in centimeters, and a CV% with a percent change.

## Example request

> Our isometric mid-thigh pull has an SEM of 85 N from last month's reliability session. One athlete went from 2,410 N to 2,560 N. Is that a real change?

Status: not tested.

## Check the result

Run these checks on the result:

- Confirm MDC95 is about 2.77 × SEM and MDC90 is about 2.33 × SEM.
- Confirm the SEM came from a short-term test-retest study with the same protocol.
- Confirm the answer states the confidence level, the SEM source, and the units.

## Sources

- Weir JP. Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. Journal of Strength and Conditioning Research. 2005;19(1):231-240. https://doi.org/10.1519/15184.1
- de Vet HC, Terwee CB, Ostelo RW, Beckerman H, Knol DL, Bouter LM. Minimal changes in health status questionnaires: distinction between minimally detectable change and minimally important change. Health and Quality of Life Outcomes. 2006;4:54. https://doi.org/10.1186/1477-7525-4-54
- Furlan L, Sterr A. The applicability of standard error of measurement and minimal detectable change to motor learning research: a behavioral study. Frontiers in Human Neuroscience. 2018;12:95. https://doi.org/10.3389/fnhum.2018.00095
- Hopkins WG. Measures of reliability in sports medicine and science. Sports Medicine. 2000;30(1):1-15. https://doi.org/10.2165/00007256-200030010-00001
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. Sportscience. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm (accessed 2026-10-02)
