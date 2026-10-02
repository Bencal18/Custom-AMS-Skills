---
name: athlete-data-visualization
description: Make clear, honest charts of athlete data, such as trends against baseline, squad views, how two measures relate, noise bands, and color-blind-safe colors. Use for any chart.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "0.1"
  last-tested: "not tested"
---

# Athlete data visualization

This skill helps you chart athlete monitoring data so a coach reads the right answer the first time. It covers which chart to use, how to show one athlete against their own baseline, how to show a whole squad, how to show relationships between measures, how to show noise, and how to use color that every reader can see. It works with any tool: a spreadsheet, Python (matplotlib or plotly), R (ggplot2), Power BI, or Tableau.

## When to use

Use this skill when the user asks to:

- Plot, chart, graph, or visualize athlete data of any kind.
- Show an athlete's trend, or whether a change is real.
- Show the whole squad, a position group, or one athlete against the team.
- Show how two measures relate, such as load and next-day jump height, or left and right limbs.
- Fix a chart that is hard to read, misleading, or not color-blind safe.
- Write alt text for a chart.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| Which chart answers which question, and charts to avoid | [references/chart-choice.md](references/chart-choice.md) |
| One athlete over time: baseline, noise band, gaps, events, rolling windows | [references/time-series.md](references/time-series.md) |
| Relationships: repeated measures, lags, limbs, dose-response, profiles | [references/relationships.md](references/relationships.md) |
| Noise and uncertainty: error bars, standard deviation versus standard error, smallest worthwhile change | [references/uncertainty.md](references/uncertainty.md) |
| Color, contrast, direct labels, text size, and alt text | [references/color-and-accessibility.md](references/color-and-accessibility.md) |
| Many athletes at once without ranking them | [references/squad-views.md](references/squad-views.md) |
| Building these charts in Power BI and Tableau | [references/bi-charts.md](references/bi-charts.md) |

Example images for every topic sit in the `assets/` folder. Each reference file links its own images.

## Steps

Follow these steps in order:

1. Ask what question the chart must answer, in one sentence, and what decision it supports. If the user has not said, offer a likely question and confirm it.
2. Ask who reads the chart (coach, staff, or athlete) and where (phone, printed report, slide). If the `coach-reports` skill is installed, use its audience guidance.
3. Ask which tool the user will use: spreadsheet, Python, R, Power BI, or Tableau. For Power BI or Tableau, load [references/bi-charts.md](references/bi-charts.md). Ask for a sample of the data with column names and units. Do not guess what a column means or what unit it uses.
4. Load [references/chart-choice.md](references/chart-choice.md). Choose the chart from the question, not from the shape of the table. If a table answers the question better, make a table.
5. Load the reference file for the chart type: [time-series.md](references/time-series.md), [relationships.md](references/relationships.md), or [squad-views.md](references/squad-views.md).
6. For any data with several rows per athlete, decide whether the question is between athletes or within athletes. Plot that level. Report the number of athletes, not rows, for between-athlete results.
7. Load [references/uncertainty.md](references/uncertainty.md) for any chart that shows change, spread, or a flag. Ask for the typical error (TE), the random test-to-test variation of the measure. Take it from a short-term test-retest study, in which the same athletes repeat the test with no true change expected, on the same summary as the plotted values. If the user has no TE, draw no noise band and no flags, and say why.
8. Draw any noise band, the range that measurement error alone stays within about 95 percent of the time, as `baseline mean ± 1.96 × TE × √(1 + 1/n)`. Here `n` is the number of values in the baseline mean. Say the 95 percent level is a choice. Say the √(1 + 1/n) term adds the variance of the baseline mean, as in Hopkins (2017). List the assumptions under the chart.
9. Load [references/color-and-accessibility.md](references/color-and-accessibility.md). Pick the scale type from the job the color does. Use Okabe-Ito colors for groups and ColorBrewer scales for amounts and changes. Add a marker shape or text label to every color that carries meaning.
10. Label lines and flagged points directly. Give every axis a label with its unit. Put `n`, the date range, and missing athletes in the title or subtitle. For one athlete over time, `n` is the number of tests with a value. List missed tests as missing. This `n` is not the baseline `n` in step 8.
11. Leave gaps for missing data. Never draw a missing value as zero, and never join a line across a gap.
12. Write a note under the chart with the formula, the units, the TE source, `n`, and the multiplier for every derived value or band. When a formula has named variants, such as a limb-symmetry index, name the variant.
13. Write alt text: a short description that names the chart type, measure, unit, who, and date range, plus the main finding in one sentence. Add a longer description or a data table near the chart.
14. If your tool can render the chart, render it and look at it. Fix overlapping labels, clipped text, and unreadable colors before you answer.

## Rules that do not depend on the tool

These choices hold in every tool. Only the menu steps or code change:

- The chart type for each question.
- One y-axis per chart, and bar charts that start at zero.
- Each athlete compared to their own baseline first.
- The noise band formula, its assumptions, and the smallest worthwhile change zone.
- Between-athlete versus within-athlete level for repeated measures.
- Gaps for missing data.
- Color-blind-safe palettes, contrast minimums, and a second cue for every color.
- Direct labels, units, `n`, dates, and alt text.

Tool-specific notes for spreadsheets, Python plotly, R ggplot2, Power BI, and Tableau sit at the end of each reference file. The Python snippets use matplotlib. Step-by-step Power BI and Tableau builds sit in [references/bi-charts.md](references/bi-charts.md).

## Checks before answering

Run these checks on your own chart before you show it:

- **Axis start:** every bar chart starts at zero. A line chart that starts above zero shows its unit and a noise band or noise bar.
- **One axis:** no chart has two y-axes.
- **Units:** every axis label and every printed value has a unit.
- **Text size:** every text element in the image, including any note, is at least 12 pt at the size the chart is viewed.
- **Counts:** the number of athletes shown matches the data, and missing athletes are listed, not dropped.
- **Gaps:** no missing value is drawn as zero or bridged by a line.
- **Noise bands:** each band uses `1.96 × TE × √(1 + 1/n)`, or a stated t value (a wider multiplier for a TE from few athletes). TE comes from a test-retest study, not from the athlete's own values. The band matches any flag rule in the same report.
- **Band note:** the note says the 95 percent level is a choice, says the √(1 + 1/n) term adds the variance of the baseline mean, as in Hopkins (2017), and lists the band's assumptions.
- **Band edges:** bands and zones have edges at 3:1 contrast or labeled edge values. A light fill alone is not enough.
- **Chance flags:** a squad chart with flags states how many flags to expect by chance next to the number found.
- **Smallest worthwhile change:** a change is labeled clearly beyond it only when its whole interval lies beyond it.
- **Error bars:** the caption says what every error bar shows. Spread between athletes uses the standard deviation (SD), not the standard error of the mean (SEM).
- **Color:** every meaning carried by color is also carried by a shape or a label. No meaning depends on red versus green. Lines and markers reach 3:1 contrast and text reaches 4.5:1. Gray marks that carry information use `#767676` or darker.
- **Causation:** no title or label says `causes`, `leads to`, `drives`, or `predicts` for a correlation.
- **Repeated measures:** no correlation pools rows from several athletes without saying so. Between-athlete and within-athlete results are shown separately.
- **Ranking:** no squad chart ranks athletes best to worst or colors them by rank.
- **Alt text:** the alt text names the chart type, measure, unit, who, date range, and main finding.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every chart as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not put `injury risk`, `at risk`, `injured`, `cleared`, `ready`, `fatigued`, or `safe` in titles, labels, legends, or color keys. Describe the data, for example `below her noise band`.
- Do not use a color scale whose colors mean danger or safety, such as red for `high risk`.
- Do not invent a threshold, band, cut point, or smallest worthwhile change. Use the user's TE and squad data, or a cited source, and name it.
- Do not draw a fitted curve or forecast past the range of the data.
- Do not show one athlete's identifiable data to another athlete, or squad charts to athletes, unless the user confirms this is allowed.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed:

- [references/chart-choice.md](references/chart-choice.md): which chart answers which question, and which charts to avoid.
- [references/time-series.md](references/time-series.md): one athlete's trend against baseline, noise bands, gaps, events, rolling windows, and aligned time axes.
- [references/relationships.md](references/relationships.md): scatter plots with repeated measures, small multiples, correlation matrices, lags, connected scatter plots, limb comparisons, dose-response, and profiles.
- [references/uncertainty.md](references/uncertainty.md): error bars, intervals, SD versus SEM, noise bands, and the smallest worthwhile change.
- [references/color-and-accessibility.md](references/color-and-accessibility.md): color-blind-safe palettes, scale types, contrast, direct labels, text size, and alt text.
- [references/squad-views.md](references/squad-views.md): small multiples, sorted dot plots, heatmaps, highlighting one athlete, and avoiding rankings.
- [references/bi-charts.md](references/bi-charts.md): the noise band measures, and each chart in this skill built step by step in Power BI and Tableau, with palettes and alt text.
