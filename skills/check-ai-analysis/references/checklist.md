# Checklist for an analysis of athlete data

Last checked: 2026-10-02

## What it covers

This file holds the eleven checks to run on any analysis of athlete data. For each check, it says what to look at, how to test it, and the failures that AI tools and spreadsheets make most often.

## Method

Run the checks in order. For each, record `pass`, `fail`, or `could not check`, with the evidence. Do the checks on the real data, not on a description of it.

### Check the formula variant

Many metrics have more than one accepted calculation, and the variants give different numbers. For example, you can calculate jump height from a force plate in three ways: from flight time, from the impulse and momentum of the force-time curve, or from the work-energy theorem (Linthorne, 2001).

Test it as follows:

- Find the formula in the code, the sheet, or the AI's answer. If you cannot find it, mark `fail`.
- Confirm the formula has a name, such as `flight time` or `impulse-momentum`.
- Confirm the variant matches the one the user's device or earlier reports use. If it differs, say so, because numbers from two variants are not comparable.
- Confirm a ratio uses the right numerator and denominator, and the right limb in each place.

### Check the units

A unit error often shows as a value that is 10, 100, or 1000 times too large or too small. Test it as follows:

- Find the unit for every column. If a column has no unit, mark `fail`.
- Confirm one unit for each measure across all rows, all sources, and both sides.
- Look at the largest and smallest value for each measure. A scale error such as meters read as millimeters, seconds as milliseconds, newtons as kilonewtons, or a fraction read as a percent puts the maximum far outside the expected range.
- Confirm a percent change is calculated from the right base, and is not a difference in percentage points.

### Check the row counts

Count rows and athletes at each step and write them down. Test it as follows:

- Count the rows in the input, after each join or filter, and in the output.
- Confirm the number of athletes matches the roster, or list who is missing.
- After a join, confirm the row count matches what you expect. A join on date alone can multiply rows. An inner join can drop athletes.
- Confirm no step removed rows without a stated reason, such as an outlier filter.

### Check how the analysis handles missing data

Test it as follows:

- Find how the analysis marks a missing value. It must use `NA` or a similar code in value columns.
- Confirm key columns, such as `side` or `session_id`, hold explicit codes and no missing values. A missing key drops rows from a pandas `groupby` unless it uses `dropna=False`, and never matches in a SQL join.
- Confirm a dedupe step never treats two rows as duplicates because both have a missing record ID.
- Search for zero used as missing, for example `fillna(0)`, `IFERROR(x,0)`, or a blank turned into 0.
- Search for carried-forward values and for averages used as fill.
- Confirm each result shows `n`, the number of values behind it, and coverage, the share of expected athletes with a value. Coverage must count athletes, not rows. A test with 3 trials can push a count of rows past 100 percent. In a review of 108 studies of training load and injury, only 37 reported whether data were missing (Bache-Mathiesen et al., 2022).

If the analysis only uses complete cases, say who is excluded. Dropping incomplete cases can bias a result (Sterne et al., 2009).

### Check the averaging windows

A window is the set of days or sessions that go into one average, total, or baseline. Test it as follows:

- Find the window length, for example 7 days or 28 days.
- Find the window type: calendar days or the last N sessions. They differ when an athlete misses days.
- Find whether the window includes the day being compared. A baseline that includes the test day shrinks the change.
- Find how the window handles missing days. A sum over a window with missing days is lower than the true total.
- Find whether the analysis averaged averages. A mean of session means is not the mean of all values when sessions differ in size.

For a ratio of an acute window to a chronic window, such as the acute:chronic workload ratio, check these three things:

- Confirm the analysis does not present the ratio as a way to predict injury, because Impellizzeri and colleagues (2020) found no evidence to support its use for managing training load.
- Confirm the denominator is stated.
- Confirm the ratio is not the only number shown.

### Check individual versus group

Test it as follows:

- Find whether the result is a group average, an individual value, or both.
- Confirm no individual decision rests on a group average, and no group conclusion rests on one athlete.
- Confirm a group chart shows the spread, such as the standard deviation, and not only the mean. Hopkins and colleagues (2009) advise showing the standard deviation, not the standard error of the mean, so readers can judge the size of differences.
- Confirm a `p` value is not used to say that one athlete changed. A `p` value from a group test does not say whether one athlete changed.

Group results can describe individuals poorly. In six repeated-measures samples of social and psychological data, the variance around the expected value was two to four times larger within individuals than within groups (Fisher et al., 2018). Those were not athlete data, so treat this as a warning, not a figure for sport.

### Check the plausible ranges

Test it as follows:

- Find the minimum and the maximum of each measure. Flag values that are physically impossible, such as a negative time or force.
- Compare each athlete's value to that athlete's own history. Flag values far outside it, and ask whether the cause is a data error.
- Compare to the typical range in the reference file for the metric, if one is available. Use only a range that has a source.
- Check the largest value and the smallest value by hand against the raw data.

Do not invent a range. If you have no source, ask the user for the range they expect, set it before you look at the data, and label it as theirs. If they have none, say you could not check against a range. A wrong value can fall inside a range, so also check that related values agree with each other (Van den Broeck et al., 2005).

### Check change versus noise

Every measurement has random error. A difference between two tests can come from error alone. Load the change-versus-noise reference and run these tests:

- Find the typical error (TE) for the measure. If the analysis has none, mark `could not check` and say so.
- Confirm the TE comes from a short-term retest in which no true change is expected, with the same summary as the values compared, such as best of 3. Confirm any t multiplier takes its degrees of freedom from the TE study, not from the baseline.
- Compare each reported change to the noise band, `1.96 x TE x sqrt(1 + 1/n)`, where `n` is the number of values in the baseline mean. Adding variances gives this band. Hopkins (2017) uses the same error for a change from the mean of several tests. The 95 percent level is this skill's choice. Confirm the assumptions behind the band are stated.
- Across a squad, confirm the report shows the number of flags expected by chance next to the number found, and recommends a repeat test before anyone acts on a single flag.
- Confirm a change is called larger than the smallest worthwhile change only when the change minus the noise band is beyond it. Otherwise it must read as larger than error, and may or may not be worthwhile.
- Check any z-score: the SD must not include the new value, must not come from few values, and a squad z-score must not be read as individual change.
- Check any rolling baseline. A slow decline moves the baseline with it and never flags.
- Check any noise band on a 1 to 5 wellness item. These items move in whole steps, so call the band a rough guide.
- Check for regression to the mean. An athlete picked because of an unusually high or low value tends to be closer to average at the next test (Barnett et al., 2005).
- Check that the analysis does not report a change with no comparison to the noise.

### Check the chart axes

Test it as follows:

- Confirm each axis has a label and a unit.
- Confirm a bar chart starts at zero. Readers rated differences as larger in a bar chart with a truncated axis than in one with a full axis (Pandey et al., 2015).
- Confirm charts that you compare side by side use the same scale.
- Confirm a line chart has gaps where data is missing, and does not join across a gap.
- Confirm the chart does not use two vertical axes to suggest a link between measures.
- Confirm a chart of a small group shows each athlete's points, not only a bar or line of the mean. Many different data sets give the same bar chart (Weissgerber et al., 2015).

### Check for overreach

Monitoring data supports a decision. It does not make one. Test it as follows:

- Search the text for words that diagnose, such as `has a tear`, `is injured`, or `has a deficit that causes`.
- Search for words that predict, such as `will get injured`, `at high risk of injury`, or `likely to break down`. A review of screening tests found no example of a screening test for sports injury with adequate test properties to predict injury (Bahr, 2016).
- Search for words that clear or hold an athlete, such as `cleared`, `ready to return`, `safe to play`, or `should rest`.
- Search for a cause stated from a pattern, such as `the drop was caused by`.
- Search for text that interprets a mood, stress, or free-text answer as a mental-health or welfare state. Remove it. Tell the user to follow their organization's referral process and involve appropriate staff.
- Replace each such phrase with a description of the data, such as `value is below this athlete's baseline by X, which is larger than typical error`. Write only what the analysis states. Leave a missing variant, window, or unit as a placeholder, such as `[variant]`.

### Check the reproducibility

Test it as follows:

- Follow each step from the raw data to each reported number. Mark `fail` if a step is hidden, such as a hand-typed value in a formula.
- Confirm you can rerun it from the raw data and get the same numbers.
- Confirm the analysis states the date range, the athletes included, and the version of the formula.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often in an athlete data analysis:

- Using the wrong variant of a formula and not saying which one it used
- Mixing units, such as `cm` and `in`, or `N` and `kN`, in one column
- Losing or doubling rows in a join, and not counting rows
- Filling missing values with zero
- Averaging over a window that has missing days and treating it as a full window
- Using a group average to judge one athlete
- Reporting a change with no comparison to noise
- Showing a ratio, a percent, or a score with no raw numbers beside it
- Drawing a bar chart with a truncated axis
- Writing a conclusion that diagnoses, predicts injury, or clears an athlete
- Giving a precise number, such as `12.347 cm`, that is more precise than the measure can be

## Example request

> Here is the spreadsheet and the summary the AI gave me about my athletes' jump tests this month. Is it right? Check it before I send it to the coach.

## Check the result

Run these checks on the checklist itself:

- Run the checklist on a spreadsheet where you planted three known errors, such as a zero used for a gap, a doubled row, and a mixed unit. Confirm the checklist finds all three.
- Recalculate three reported values by hand from the raw data. Confirm they match the report to the stated precision.
- Read the conclusion aloud. Confirm that each sentence is something the data shows and not something it implies.

## Sources

These sources support the checks in this file:

- Linthorne NP. Analysis of standing vertical jumps using a force platform. *American Journal of Physics*. 2001;69(11):1198-1204. doi:10.1119/1.1397460. States that jump height can be calculated from flight time, from the impulse-momentum theorem, or from the work-energy theorem.
- Bache-Mathiesen LK, Andersen TE, Clarsen B, Fagerland MW. Handling and reporting missing data in training load and injury risk research. *Science and Medicine in Football*. 2022;6(4):452-464. doi:10.1080/24733938.2021.1998587. Reports that 37 of 108 studies stated whether training load had missing observations.
- Sterne JAC, White IR, Carlin JB, et al. Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls. *BMJ*. 2009;338:b2393. doi:10.1136/bmj.b2393. Shows that complete case analysis can be biased and lose precision.
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. *International Journal of Sports Physiology and Performance*. 2020;15(6):907-913. doi:10.1123/ijspp.2019-0864. Concludes there is no evidence to support use of the ratio in managing training load or for recommendations to reduce injury risk.
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. *Medicine and Science in Sports and Exercise*. 2009;41(1):3-13. doi:10.1249/MSS.0b013e31818cb278. Advises showing the standard deviation rather than the standard error of the mean.
- Fisher AJ, Medaglia JD, Jeronimus BF. Lack of group-to-individual generalizability is a threat to human subjects research. *Proceedings of the National Academy of Sciences*. 2018;115(27):E6106-E6115. doi:10.1073/pnas.1711978115. Reports, from six repeated-measures samples of social and psychological data, that the variance around the expected value was two to four times larger within individuals than within groups.
- Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. *International Journal of Epidemiology*. 2005;34(1):215-220. doi:10.1093/ije/dyh299. Explains that unusually large or small measurements tend to be followed by measurements closer to the mean.
- Pandey AV, Rall K, Satterthwaite ML, Nov O, Bertini E. How deceptive are deceptive visualizations? An empirical analysis of common distortion techniques. *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (CHI '15)*. 2015:1469-1478. doi:10.1145/2702123.2702608. Found that readers rated differences as larger in a bar chart with a truncated axis than with a full axis.
- Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLOS Biology*. 2015;13(4):e1002128. doi:10.1371/journal.pbio.1002128. Shows that many different data distributions can lead to the same bar or line graph.
- Bahr R. Why screening tests to predict injury do not work, and probably never will: a critical review. *British Journal of Sports Medicine*. 2016;50(13):776-780. doi:10.1136/bjsports-2016-096256. Found no example of a screening test for sports injuries with adequate test properties.
- Van den Broeck J, Argeseanu Cunningham S, Eeckels R, Herbst K. Data cleaning: detecting, diagnosing, and editing data abnormalities. *PLoS Medicine*. 2005;2(10):e267. doi:10.1371/journal.pmed.0020267. Accessed 2026-10-02. Recommends predefined expected ranges, soft screening cutoffs, hard cutoffs for impossible values, and checks for wrong values that fall inside the expected range.
