# Position against a published norm

Last checked: 2026-10-07

## What it measures

Position against a published norm estimates where one athlete's test result sits in a published group of similar athletes, as a percentile with an interval, and with measurement error beside it.

A norm, or normative data, is a published summary of results from a sample of athletes: a mean and SD, a percentile table, or the raw values. A norm is a reference, never a rating. Never use it as a pass mark, a target, a standard to meet, or a band of labels such as "poor" or "excellent".

## Formula

### Check the match before any calculation

Use a published norm only when every item below matches the athlete's test. Ask the user for each item the data does not show:

| Item | What must match |
|---|---|
| Population | Sport, sex, age group, and competitive level |
| Protocol | The test and its version, for example a CMJ with hands on hips, not with arm swing |
| Device and processing | The device type, the calculation method, and the settings, such as the jump height method, onset threshold, and filter |
| Trial summary | Best trial, mean of trials, or a single trial, and the number of trials |
| Units | The same units after conversion |
| Sample | The norm's sample size `n` is stated |

If any item does not match, or the paper does not say, stop. Name the item. Tell the user the norm is not a matched reference for this athlete. Offer the squad comparison in [`squad-position.md`](squad-position.md) instead. Do not adjust a norm to fit.

The force plate reference files list published ranges with their protocols, for example in the reactive strength reference of the `force-plate` skill, under its units and typical range section. Read the protocol notes under each range before you treat it as a norm, and follow the limits on published ranges in the `force-plate` skill.

### Norm given as a mean and SD

Crawford and Howell (1998) treat the athlete as a sample of 1, and use a modified t-test, from Sokal and Rohlf, to estimate the percentage of the norm population below the athlete's score:

```text
t          = (x − norm mean) / (norm SD × √((n + 1) / n))
percentile = 100 × T.DIST(t, n − 1, TRUE)
```

Define every term in the formula:

- `x`: the athlete's result, in the units of the norm.
- `norm mean` and `norm SD`: the mean and the sample SD the norm reports.
- `n`: the number of athletes in the norm sample.
- `t`: a t statistic on `n − 1` degrees of freedom.
- `T.DIST(t, n − 1, TRUE)`: the share of a t distribution below `t`.
- `percentile`: the estimated percentage of the norm population below `x`.

The standard method treats the norm mean and SD as exact, and reads `z = (x − mean) / SD` from the normal curve. Crawford and Howell (1998) suggest the t method when `n` is under 50. Both methods assume the norm results follow a normal distribution, and Crawford and Howell (1998) advise against the t method for markedly skewed data. For a timed test, use `(norm mean − x)` in place of `(x − norm mean)`, so the percentile reads as "percent of the norm slower".

### Interval on the percentile

A norm comes from a sample, so its percentile is an estimate with uncertainty (Crawford et al., 2009). Crawford and Garthwaite (2002) give confidence limits on the percentage below the score, from non-central t distributions:

1. Compute `c = (x − norm mean) / norm SD`.
2. Compute `q = c × √n`.
3. Find `δU`, the non-centrality value that makes `q` the 2.5th percentile of a non-central t distribution on `n − 1` degrees of freedom.
4. Find `δL`, the value that makes `q` the 97.5th percentile.
5. The 95% limits are `100 × Φ(δL / √n)` and `100 × Φ(δU / √n)`, where `Φ` is the standard normal share below a value.

Excel and Google Sheets have no non-central t function. Use the Python code below, or the programs Crawford and Garthwaite (2002) describe.

### Norm given as raw values, or a local norm

When you have each value in the norm sample, use definition C from [`squad-position.md`](squad-position.md#percentile-definition-c). The athlete is not in the norm sample, so `m` and `k` count norm athletes only, and `N` is the norm sample size.

Crawford et al. (2009) treat `x = m + 0.5 × k` as successes out of `N`, and take the Clopper-Pearson interval for a proportion. The Clopper-Pearson limits are quantiles of beta distributions (Thulin, 2014):

```text
lower = 100 × BETA.INV(0.025, x, N − x + 1)
upper = 100 × BETA.INV(0.975, x + 1, N − x)
```

When `x = 0`, the lower limit is 0. When `x = N`, the upper limit is 100. When `k` is odd, `x` is not a whole number. The beta form still runs, but it is an approximation. Crawford et al. (2009) develop a method for ties.

A local norm is a norm built from your own past squads. Treat it as a published norm. Run the same match checks, and state its sample, seasons, and protocol.

### Norm given as a percentile table

Find the two table rows the athlete's result sits between. Report the result as "between the 25th and 50th percentile of [norm]". Do not interpolate between rows unless the user asks. If you interpolate, say so.

Crawford et al. (2009) note that it is often not clear which definition a set of percentile norms used. If the table does not say, say so in the output. Do not report the interval methods above for a table, because the table gives no `m`, `k`, or SD.

### Measurement error beside each value

Put the error range for the athlete's true score, `x ± 1.96 × TE`, beside the percentile (Swinton et al., 2018). Take TE from the typical error reference of the `monitoring-statistics` skill, on your own protocol. Then read the norm at both ends of the error range with the same method. Report the norm interval and the error range separately. They answer two questions: how precise the norm is, and how precise the athlete's score is.

### Use a spreadsheet

These formulas work in Excel and Google Sheets. Put the athlete's result in `B2`, the norm mean in `C2`, the norm SD in `D2`, the norm `n` in `E2`, and TE in `F2`:

```text
Percentile (t method):    =100*T.DIST((B2-C2)/(D2*SQRT((E2+1)/E2)),E2-1,TRUE)
Error range, low:         =B2-1.96*F2
Error range, high:        =B2+1.96*F2
Percentile at low end:    =100*T.DIST((B2-1.96*F2-C2)/(D2*SQRT((E2+1)/E2)),E2-1,TRUE)
Percentile at high end:   =100*T.DIST((B2+1.96*F2-C2)/(D2*SQRT((E2+1)/E2)),E2-1,TRUE)
```

`T.DIST` with `TRUE` returns the left-tail share in both tools, and accepts a negative `t`. Microsoft documents `T.DIST` as left-tailed, and Google's examples give `T.DIST(-1.98, 2, TRUE)` = 0.0931.

For raw norm values, put `m` in `G2`, `k` in `H2`, and `N` in `I2`:

```text
Percentile (C):           =100*(G2+0.5*H2)/I2
Lower 95% limit:          =IF(G2+0.5*H2=0,0,100*BETA.INV(0.025,G2+0.5*H2,I2-(G2+0.5*H2)+1))
Upper 95% limit:          =IF(G2+0.5*H2=I2,100,100*BETA.INV(0.975,G2+0.5*H2+1,I2-(G2+0.5*H2)))
```

`BETA.INV` accepts shape values that are not whole numbers, as long as they are above 0 (Microsoft, `BETA.INV`).

### Calculate it in Power BI and Tableau

In Power BI, store each norm in a `norms` table with one row per test, population, and protocol: `measure_name`, `norm_mean`, `norm_sd`, `norm_n`, `unit`, and `source`. Use this DAX measure with `[Test value (cm)]` from [`squad-position.md`](squad-position.md#calculate-it-in-power-bi-and-tableau). DAX `T.DIST` returns the left-tailed t distribution (Microsoft, DAX `T.DIST`):

```text
Norm percentile (t method) =
VAR x = [Test value (cm)]
VAR m = SELECTEDVALUE ( norms[norm_mean] )
VAR s = SELECTEDVALUE ( norms[norm_sd] )
VAR n = SELECTEDVALUE ( norms[norm_n] )
RETURN
    IF (
        NOT ISBLANK ( x ) && s > 0 && n >= 2,
        100 * T.DIST ( ( x - m ) / ( s * SQRT ( ( n + 1 ) / n ) ), n - 1, TRUE )
    )
```

Filter `norms` to one row that matches the test, population, and protocol. `SELECTEDVALUE` returns blank when more than one row is left, so the measure returns blank instead of mixing norms.

In Tableau, compute the norm percentile and its interval in the spreadsheet or Python, and import them as columns. Keep the norm source and `n` as columns beside them.

### Use Python

This Python code needs `scipy`:

```python
from math import sqrt
from scipy import stats, optimize

def norm_percentile(x, mean, sd, n):
    """Crawford and Howell (1998): estimated % of the norm population below x."""
    t = (x - mean) / (sd * sqrt((n + 1) / n))
    return 100 * stats.t.cdf(t, n - 1)

def norm_percentile_interval(x, mean, sd, n, level=0.95):
    """Crawford and Garthwaite (2002): interval on that percentage, non-central t."""
    a = 1 - level
    q = (x - mean) / sd * sqrt(n)
    f = lambda d, p: stats.nct.cdf(q, n - 1, d) - p
    d_upper = optimize.brentq(f, q - 10, q + 10, args=(a / 2,))
    d_lower = optimize.brentq(f, q - 10, q + 10, args=(1 - a / 2,))
    return 100 * stats.norm.cdf(d_lower / sqrt(n)), 100 * stats.norm.cdf(d_upper / sqrt(n))

def sample_percentile_interval(below, equal, n, level=0.95):
    """Definition C point estimate and Clopper-Pearson interval from raw norm data."""
    a = 1 - level
    x = below + 0.5 * equal
    lo = 0.0 if x == 0 else stats.beta.ppf(a / 2, x, n - x + 1)
    hi = 1.0 if x == n else stats.beta.ppf(1 - a / 2, x + 1, n - x)
    return 100 * x / n, 100 * lo, 100 * hi

te = 1.4
print(norm_percentile(37.4, 40.0, 4.5, 18))                       # 29.1
print(norm_percentile_interval(37.4, 40.0, 4.5, 18))              # 14.2, 47.2
print([norm_percentile(v, 40.0, 4.5, 18) for v in (37.4 - 1.96 * te, 37.4 + 1.96 * te)])  # 13.2, 51.2
print(sample_percentile_interval(11, 0, 40))                      # 27.5, 14.6, 43.9
```

## Calculate the metric

Follow these steps for each test:

1. Find the norm's population, protocol, device, method, trial summary, units, and `n`.
2. Compare each item with the athlete's test, using the match table.
3. Stop and name the item if any item does not match.
4. Convert the athlete's result to the norm's units.
5. Pick the method for the norm's format: mean and SD, raw values, or a percentile table.
6. Calculate the percentile.
7. Calculate the interval on the percentile, when the format allows it.
8. Calculate the error range, `x ± 1.96 × TE`.
9. Read the norm at both ends of the error range.
10. Report the percentile, the norm interval, the error range, the norm's source, its population, and its `n`.

## Worked example

Athlete A07 jumped 37.4 cm in a CMJ, best of 3 trials, with TE = 1.4 cm from the squad's own retest. A made-up norm matches every item in the match table. It reports 40.0 ± 4.5 cm (mean ± SD) from 18 athletes.

| Input | Value |
|---|---|
| Athlete result `x` | 37.4 cm |
| Norm mean | 40.0 cm |
| Norm SD | 4.5 cm |
| Norm `n` | 18 |
| TE | 1.4 cm |

Work out the percentile with the t method:

1. √((18 + 1) / 18) = 1.0274.
2. t = (37.4 − 40.0) / (4.5 × 1.0274) = −2.6 / 4.623 = −0.562.
3. Percentile = 100 × T.DIST(−0.562, 17, TRUE) = 29.1.

Compare the standard method: z = −2.6 / 4.5 = −0.578, and the normal curve gives 28.2. The t method gives a less extreme estimate, as Crawford and Howell (1998) describe.

Work out the 95% interval on the percentile:

1. c = −0.578. q = −0.578 × √18 = −2.451.
2. δU = −0.297 and δL = −4.544, on 17 degrees of freedom.
3. Lower limit = 100 × Φ(−4.544 / √18) = 14.2.
4. Upper limit = 100 × Φ(−0.297 / √18) = 47.2.

Work out the measurement error:

1. Error range = 37.4 ± 2.74 = 34.66 to 40.14 cm.
2. Percentile at 34.66 cm = 13.2. Percentile at 40.14 cm = 51.2.

Result: "A07's CMJ sits at about the 29th percentile of [norm], 18 athletes, matched on population, protocol, device, and trial summary. The norm's 95% interval runs from the 14th to the 47th percentile. With A07's measurement error, the estimate runs from the 13th to the 51st." The result is a position, not a rating.

For raw values, take a made-up local norm of 40 athletes from past seasons, with 11 below the athlete and none tied. Definition C gives 100 × 11 / 40 = 27.5. The Clopper-Pearson interval runs from 14.6 to 43.9.

For a made-up percentile table with 25th percentile 36.9 cm and 50th percentile 40.0 cm, 37.4 cm sits between the 25th and 50th percentiles.

## What changes the number

These choices change the result even when the athlete's performance does not:

- A norm from another population, protocol, device, method, or trial summary. The match table prevents this.
- The norm's sample size. In the worked example, the same mean and SD from 200 athletes give 28.3, with an interval of 23.4 to 33.5. From 8 athletes, they give 30.1, with an interval of 9.4 to 57.7.
- The method. The normal curve gives 28.2 and the t method gives 29.1 in the worked example.
- The percentile definition in a percentile table. Crawford et al. (2009) show differences between definitions that grow with ties and small samples.
- A skewed norm. Both the normal and the t methods assume a normal distribution.
- TE and the confidence level. A larger TE or a higher level widens the error range.

## Units and typical range

Percentiles run from 0 to 100 and have no unit. The norm interval is never narrower than the norm's sample allows. In the worked example, 18 athletes give an interval 33 points wide.

## Data you need

Collect this data:

- Source: a published norm, or a local norm, that states its population, protocol, device, method, trial summary, units, and `n`.
- Sampling: the athlete's result on the same protocol and trial summary as the norm.
- Minimum data: the norm's mean, SD, and `n`; or its raw values; or its percentile table with the definition stated.
- TE on the athlete's protocol, from the typical error reference of the `monitoring-statistics` skill.

## Common mistakes

These are the mistakes AI tools make most often with norms:

- Using a norm from another sex, age group, level, protocol, or device.
- Comparing a mean of 3 trials with a norm built on the best of 3.
- Treating the norm mean as a target or a pass mark, or calling a result below it a deficit.
- Copying a norm table's labels, such as "excellent", "average", or "poor", onto an athlete.
- Reading the normal curve for a norm from a small sample. Use the t method below 50 athletes, as Crawford and Howell (1998) suggest.
- Reporting a percentile with no interval and no `n`.
- Mixing a norm percentile and a squad percentile in one column.
- Citing a norm from memory. Open the source, and confirm the population and protocol.

## Example request

> A paper gives CMJ norms for college soccer players as 40.0 ± 4.5 cm from 18 players. Where does our athlete's 37.4 cm sit?

## Check the result

Run these checks:

- Reproduce the Crawford and Howell (1998) example: a score of 33 against a norm of 50 ± 10 from 15 people gives t = −1.65 on 14 degrees of freedom, and about 6% below.
- Reproduce the Crawford and Garthwaite (2002) example: a score of 30 against 50 ± 10 from 15 people gives 3.7%, with 95% limits of 0.2% and 13.6%.
- Reproduce the Crawford et al. (2009) example: 10 below and 4 tied in 80 people gives 15, with Clopper-Pearson limits of 8.00 and 24.74.
- Confirm every item in the match table is stated and matches.
- Confirm no rating word, target, or pass mark appears in the output.

## Sources

This file cites these sources:

- Crawford JR, Howell DC. Comparing an individual's test score against norms derived from small samples. The Clinical Neuropsychologist. 1998;12(4):482-486. https://doi.org/10.1076/clin.12.4.482.7241 (accessed 2026-10-07). Source of the modified t method, its worked example (read in the author-hosted PDF at https://homepages.abdn.ac.uk/j.crawford/pages/dept/pdfs/ClinicalNeuropsychologist_1998_Individual_vs_Controls.pdf), and the suggestion to use it when the norm sample is under 50.
- Crawford JR, Garthwaite PH. Investigation of the single case in neuropsychology: confidence limits on the abnormality of test scores and test score differences. Neuropsychologia. 2002;40:1196-1208. https://doi.org/10.1016/S0028-3932(01)00224-X (accessed 2026-10-07). Source of the non-central t interval and its worked example, read in the author-hosted PDF at https://homepages.abdn.ac.uk/j.crawford/pages/dept/pdfs/Neuropsychologia_2002_conflims_singlecase.pdf.
- Crawford JR, Garthwaite PH, Slick DJ. On percentile norms in neuropsychology: proposed reporting standards and methods for quantifying the uncertainty over the percentile ranks of test scores. The Clinical Neuropsychologist. 2009;23(7):1173-1195. https://doi.org/10.1080/13854040902795018 (accessed 2026-10-07). Source of definition C, the uncertainty of a norm percentile, and the Clopper-Pearson interval with its worked example, read in the author-hosted PDF at https://homepages.abdn.ac.uk/j.crawford/pages/dept/pdfs/ClinicalNeuropsychologist_2009_Percentile_Norms.pdf.
- Thulin M. The cost of using exact confidence intervals for a binomial proportion. Electronic Journal of Statistics. 2014;8(1):817-840. https://doi.org/10.1214/14-EJS909 (accessed 2026-10-07). Source of the Clopper-Pearson limits as beta quantiles.
- Swinton PA, Hemingway BS, Saunders B, Gualano B, Dolan E. A statistical framework to interpret individual response to intervention: paving the way for personalized nutrition and exercise prescription. Frontiers in Nutrition. 2018;5:41. https://doi.org/10.3389/fnut.2018.00041 (accessed 2026-10-07). Source of the range for a true score as the observed score plus and minus a multiple of TE.
- Microsoft. T.DIST function, BETA.INV function, and DAX T.DIST function. https://support.microsoft.com/en-us/office/t-dist-function-4329459f-ae91-48c2-bba8-1ead1c6c21b2, https://support.microsoft.com/en-us/office/beta-inv-function-e84cb8aa-8df0-4cf6-9892-83a341d252eb, and https://learn.microsoft.com/en-us/dax/t-dist-function-dax (accessed 2026-10-07).
- Google. T.DIST function. https://support.google.com/docs/answer/9369014 (accessed 2026-10-07).
