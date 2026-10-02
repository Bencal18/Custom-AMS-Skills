# Chart choices for athlete data

Last checked: 2026-10-02

## What it covers

This file helps you choose a chart for each question a coach or athlete asks, and avoid chart designs that mislead. Most rules here are design practice. Where a study supports a rule, the study is named.

## Method

Start from the question the chart answers. Then pick the chart from the table.

| Question | Chart | Notes |
|---|---|---|
| How has one athlete changed over time? | Line chart with a point for each test, and a shaded noise band around the athlete's baseline mean | Leave a gap where a value is missing. Do not join across the gap. |
| Who in the group changed from their own baseline? | Dot plot with one row for each athlete, showing change from baseline with the noise band | Sort by size of change. Mark athletes with no data. |
| How do the athletes' values spread at one time point? | Dot plot or box plot with every athlete's point | Show each athlete's point. Do not show only the mean. |
| How did the same athletes compare across two periods? | Points for each athlete, joined by a line between the two periods, plus the group mean | Use joining lines only when the same athletes appear in both periods. Show the individual lines. |
| How did two different groups compare? | Points for each athlete in each group, side by side, plus each group mean | Do not join points across groups. The athletes are not paired. |
| What are the exact numbers? | Table, with raw value, unit, change, and flag state | Use a table when the reader needs a number, not a shape. |
| How is load spread across the week? | Bar chart starting at zero, one bar per day | Use bars only for totals or counts. |

### Show every athlete's data when the group is small

Bar and line charts of the mean hide the data. Many different data distributions give the same bar or line graph, and the full data may suggest a different conclusion (Weissgerber et al., 2015). For small groups, show each athlete's point.

### Start bar charts at zero

A bar chart that does not start at zero changes how readers answer questions about it. In a study of common distortion techniques, readers rated the difference between bars as larger when the bar chart's axis did not start at zero (Pandey et al., 2015). Truncation inflated perceived effect size across chart types, even when the chart marked the cut (Correll et al., 2020).

A line chart may start above zero. Then label the axis and the unit, and show the noise band, so the reader can judge a change against the noise.

### Show noise on the chart

Show the noise band as a shaded band around the athlete's baseline mean. Use the same band as the flag rule: baseline mean plus or minus `1.96 x TE x sqrt(1 + 1/n)`, where TE is the typical error and `n` is the number of values in the baseline mean. This band adds the variance of the new value to the variance of the baseline mean, as in Hopkins (2017).

A point inside the band is not larger than measurement error, and a point outside it is beyond the noise band.

Define the band in a note under the chart, for example `Band: baseline mean plus or minus 1.96 x TE x sqrt(1 + 1/n), n = 5`. List the assumptions behind the band from the change-versus-noise reference.

Do not shade the baseline mean plus or minus `1.96 x TE`. That band is narrower than the flag rule.

Points then sit outside the band while the report says they are not larger than measurement error.

With `n = 1`, that narrower band holds only about 83 percent of unchanged results. This figure is derived, not taken from a paper.

Show spread as a standard deviation, not as a standard error of the mean. Hopkins and colleagues (2009) advise this, so readers can judge the size of differences between athletes.

### Show missing data

Leave a gap, or a hollow marker with the label `no data`. Do not draw a zero. Do not draw a line across a gap. Put the number of athletes with data, out of the number expected, in the chart subtitle.

### Label everything

Add these to every chart:

- A title that states the question or the finding
- An axis label with the unit on each axis
- The date range and the number of athletes
- The source of the data, and the formula or variant if the measure has more than one

### Use color and scale with care

Use the same scale on charts that you compare side by side. Use one vertical axis for each chart. Two vertical axes can suggest a link between two measures that does not exist, because the ratio between the two scales is arbitrary. This is practice advice.

Do not use color alone to carry meaning. In European Caucasians, about 8 percent of men and 0.4 percent of women have red-green color deficiency (Birch, 2012).

Add a label, a shape, or a position. Use a palette that stays distinct for readers with color deficiency.

### Keep sub-scores visible

When you show a composite score, show its parts in a chart or table next to it. A composite can stay flat when one part rises and another falls. A reader sees `no change` and misses both.

Show the parts with their own baselines. Write the formula and the weights.

## Common mistakes

These are the mistakes AI tools make most often when they chart athlete data:

- Drawing a bar chart with an axis that starts above zero
- Showing a bar of the squad mean, with no points or spread
- Joining a line across a missing week, so the gap looks like a smooth change
- Drawing a missing value as zero
- Using two vertical axes, so two lines look as if they track each other
- Using different scales on side-by-side charts for different athletes, so a small change looks as large as a big one
- Using color as the only signal, such as red and green dots
- Showing a percent change with no raw values
- Showing a chart with no unit, date range, or `n`
- Showing a composite score as one line, with no parts

## Example request

> Chart each athlete's weekly jump height so I can see who has moved away from their own normal. Keep it readable for a coach on a phone.

Status: not tested.

## Check the result

Run these checks on each chart:

- Read each axis label. Confirm it has a unit.
- Count the points. Confirm the number of athletes with data matches the table, and that missing athletes show as gaps.
- Check the shaded band. Confirm it uses the same formula and `n` as the flags, and that every flagged point sits outside it.
- Cover the title. Confirm that a reader can tell what the chart answers from the axis labels and the note under it.

## Sources

These sources support the rules in this file:

- Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLOS Biology*. 2015;13(4):e1002128. doi:10.1371/journal.pbio.1002128. Shows that many different data distributions lead to the same bar or line graph, and recommends showing the full data in small studies.
- Pandey AV, Rall K, Satterthwaite ML, Nov O, Bertini E. How deceptive are deceptive visualizations? An empirical analysis of common distortion techniques. *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (CHI '15)*. 2015:1469-1478. doi:10.1145/2702123.2702608. Found that readers rated differences as larger in a bar chart with a truncated axis than with a full axis.
- Correll M, Bertini E, Franconeri S. Truncating the y-axis: threat or menace? *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*. 2020:1-12. doi:10.1145/3313831.3376222. Finds y-axis truncation increases perceived effect size across chart designs, even with visual cues that mark the truncation.
- Hopkins WG. A spreadsheet for monitoring an individual's changes and trend. *Sportscience*. 2017;21:5-9. https://www.sportsci.org/2017/wghtrend.htm. Accessed 2026-10-02. Its monitoring spreadsheet computes the error of a change from the mean of several reference tests as TE x sqrt(1 + 1/n), with t at the typical error's degrees of freedom.
- Hopkins WG, Marshall SW, Batterham AM, Hanin J. Progressive statistics for studies in sports medicine and exercise science. *Medicine and Science in Sports and Exercise*. 2009;41(1):3-13. doi:10.1249/MSS.0b013e31818cb278. Advises showing the standard deviation rather than the standard error of the mean.
- Birch J. Worldwide prevalence of red-green color deficiency. *Journal of the Optical Society of America A*. 2012;29(3):313-320. doi:10.1364/JOSAA.29.000313. Reports a prevalence in European Caucasians of about 8 percent in men and about 0.4 percent in women.
