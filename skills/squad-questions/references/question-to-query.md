# Question to query

Last checked: 2026-10-07

## What it covers

This file shows how to turn a coach's question into a precise query. It covers the four parts of every question, the three kinds of comparison, and the rules that keep a query honest about missing data.

## Why it matters

A quick question from a coach often costs a sports scientist a long time. In a survey of 99 staff at European elite football clubs, Houtmeyers and colleagues (2021) noted that collecting many types of variables makes it challenging to use the data effectively.

An AI tool can build the filter quickly. It can also answer the wrong question quickly. The method below makes the question precise before any number is calculated.

## Method

### Restate the question in four parts

Write every question back to the coach as four parts:

| Part | What it sets | Example |
|---|---|---|
| Who | The filter: the whole squad, a position group, named athletes, or athletes who meet a condition | All 6 active athletes on the roster |
| When | The time window: the first date, the last date, and whether it counts days, sessions, or training weeks | The last four team sessions, 2026-09-29 to 2026-10-03 |
| What | The measure, with its unit, its variant, and its owning skill | High-speed running distance per session, in m, at the speed setting in the GPS export (`gps-running-load`) |
| Compared with what | The comparison: the athlete's own baseline, a threshold the coach supplies, or the squad | Above 600 m, a threshold the coach set |

Write the restated query in one sentence before you calculate, for example: "For all 6 athletes, count the sessions among the last four team sessions (2026-09-29 to 2026-10-03) in which high-speed running was above 600 m."

If the coach did not state a part, or stated it with a phrase from [ambiguous-phrases.md](ambiguous-phrases.md), ask before you calculate.

### Set the filter

Follow these rules for the "who" part:

- Start from the roster of active athletes on the dates in the window, not from the rows in the data. An athlete with no rows is still expected.
- Use `athlete_id` in the data and the query. When the coach names an athlete, ask for the ID or look it up in the coach's ID list. Keep names out of the data you paste into an AI tool.
- Take position groups from the athletes table, not from memory. Ask if the table has no group column.
- When the filter is a condition, such as "athletes who played on Saturday", name the column and the value that define it.

### Set the time window

Follow these rules for the "when" part:

- Write the window as two dates in `YYYY-MM-DD` form, and say whether both ends are included.
- Count sessions from the sessions table, not from one athlete's rows. "The last four sessions" are the squad's last four sessions unless the coach says each athlete's last four.
- Use the local session date. See the joining reference in `ams-data-setup` for time zones.
- If the window ends today and today's data is not complete, say so, or end the window yesterday.
- When the window is a training week, ask which day it starts on. The `load-and-wellness` skill sums weekly load from Monday to Sunday unless the user names another start day.

### Set the measure

Follow these rules for the "what" part:

- Name the measure, its unit, and its variant. Examples: jump height by the takeoff velocity method, or high-speed running above a named speed.
- Route the calculation to the owning skill in the routing table in `SKILL.md`. Use its formula and its trial summary rule.
- If one word could mean several measures, such as "load" or "jump", ask which one.
- If the measure is a composite score, show its parts beside it, as the `readiness-composites` skill requires.

### Choose the comparison

Each question uses one of three comparisons. Name it in the restated query.

**Against the athlete's own baseline.** Use this by default when the coach asks about change, such as "compared with last month" or "down on usual". Follow these rules:

- Take the baseline from the athlete's own earlier values. Do not include the new value in its own baseline.
- State the baseline window and the number of values in it, `n`.
- Compare the change with the noise band from the `monitoring-statistics` skill. The noise band is the size of change that measurement error alone stays inside about 95 percent of the time: `1.96 × TE × √(1 + 1/n)`, where TE is the typical error of the test. TE must come from a short-term retest of the same test, device, and population.
- If the coach has no TE, say the change cannot be judged against measurement error.
- A weekly load total is not a test, so it has no test-retest TE. Describe the change, and do not call it beyond noise. The `monitoring-statistics` skill offers a usual-variation band instead: the range of the athlete's own normal week-to-week values. It needs at least 10 stable baseline values, and it is never a measurement-error band.

**Against a threshold the coach supplies.** Use this when the coach names a line, such as "over 600 m" or "under 30 cm". Follow these rules:

- Use the coach's number. Ask where it came from, and label it as the coach's choice, with that source or with no source.
- Ask whether "over" means above or at or above. The answer changes the count when a value sits on the line.
- Say that a value close to the line can fall on either side of it from measurement error alone. Do not invent a margin.
- Do not suggest a threshold. If the coach asks for one, use only a figure from the owning skill's reference file, with its source and population.

**Against the squad.** Use this when the coach asks where an athlete sits among teammates. Follow these rules:

- Compare each athlete with their own baseline first, as the squad views reference in the `athlete-data-visualization` skill requires.
- Route the comparison to `testing-profiles` (version 1.1) when it is installed. It covers percentiles, and SD units (distance from the group mean in standard deviations), against the squad or a position group.
- Do not rank. See "Answer a request to rank the squad" in `SKILL.md`.

### Build the query

Write the query in the coach's tool: Excel, Google Sheets, SQL, Python, R, Power BI, or Tableau. Follow these rules:

- Join the result to the roster, so every expected athlete has a row. In SQL, use `roster LEFT JOIN data`. In a spreadsheet, put the roster in the first column and use `COUNTIFS`, `SUMIFS`, or `AVERAGEIFS` against it.
- Keep only rows with a usable status, such as `status = 'ok'`. In Excel and Google Sheets, a direct comparison such as `D2>600` treats any text as larger than any number, so a missing code such as `NA` can pass it. `COUNTIFS` with `">600"` counts numbers only, but an array test inside `FILTER` does not skip text.
- Count athletes, not rows. A test with 3 trials gives up to 3 rows for each athlete.
- Expect the Google Sheets `QUERY` function to drop groups with no matching rows. An athlete with zero sessions over a threshold does not appear in a `count` result. Join it back to the roster.
- Use the same window, filter, and status rule in every formula of the answer.
- Show the formula or code with the answer, so the coach or a sports scientist can rerun it.

[worked-examples.md](worked-examples.md) shows each of these rules on made-up data.

## Common mistakes

These are the mistakes AI tools make most often when they turn a question into a query:

- Answering at once with a guessed window, measure, or threshold. Restate the question, and ask about each unclear part.
- Starting from the rows in the data instead of the roster, so athletes with no data disappear.
- Counting "the last four sessions" from each athlete's own rows, so an athlete who missed a session gets a different window.
- Treating a missing value as zero, or letting a text code pass a number test.
- Calling a coach's threshold a published standard.
- Comparing athletes with each other before comparing each with their own baseline.
- Calling a change real without a noise band.
- Changing the question without saying so, for example answering for 7 days when the coach meant the training week.

## Example request

> Who's been over 600 m of high-speed running in the last four sessions?

## Check the result

Run these checks:

- Read the restated query aloud against the coach's words. Confirm each of the four parts is either stated by the coach or confirmed by the coach.
- Confirm the result has one row for each athlete on the roster.
- Confirm the first and last dates of the rows used match the window.
- Recompute one athlete by hand from the raw rows.

## Sources

This file draws on these sources:

- Houtmeyers KC, Vanrenterghem J, Jaspers A, Ruf L, Brink MS, Helsen WF. Load monitoring practice in European elite football and the impact of club culture and financial resources. *Frontiers in Sports and Active Living*. 2021;3:679824. https://doi.org/10.3389/fspor.2021.679824 (accessed 2026-10-07). An online survey of sports-science and sports-medicine staff at European elite football clubs (n = 99, 50% response rate). The discussion notes that collecting different types of variables increases the amount of available data, making it challenging to use the data effectively.
