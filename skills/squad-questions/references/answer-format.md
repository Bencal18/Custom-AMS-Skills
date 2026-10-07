# Answer format

Last checked: 2026-10-07

## What it covers

This file sets the shape of the answer to a coach's quick question. It covers the opening sentences, the table, the counts, the date range, missing athletes, and the statement about noise.

## Method

A coach reads the first lines and may stop there. Put the answer first, then the facts that limit it, then the detail.

### Write two or three sentences first

Write the answer in two or three sentences before the table. Include these items:

- The direct answer, in the measure's units, with the restated question in brief.
- The date range used, as two dates in `YYYY-MM-DD` form.
- The coverage: athletes with data out of athletes expected. Count athletes, not rows.
- The athletes with missing data, by `athlete_id` or the name the coach used, with the reason when known.
- For a change: whether it is inside or beyond the noise band, or that it cannot be judged without a typical error.

If you changed any part of the coach's question, or applied a default, say so in the first sentence.

Use the coach's words where they are precise. Do not add a cause, a diagnosis, a plan, or a judgment such as "ready" or "struggling".

### Show the table

Put one row for each expected athlete under the sentences. Follow these rules:

- Keep athletes with no data in the table. List them after the athletes with data, labeled `no data` with the reason, such as `excused` or `device failure`. Never show them as 0.
- Order rows by roster or position, or by change from each athlete's own baseline. Never order by a judgment of the athlete. When you sort by change, show the noise band beside the change, or say the change cannot be judged against noise, and add the note `Sorted by change, not by ability`.
- Do not use best, worst, top, bottom, or rank numbers in any column heading, label, or title. Write a title that describes the data, such as `Change from own baseline, week of 2026-09-28`.
- Put the unit in every column heading.
- Show the count that each value rests on, such as `sessions with data` or `n` baseline tests.
- For a change, show the baseline, the change, and the noise band side by side.
- For a threshold, show the threshold and its source in a note under the table, such as `Threshold: 600 m, set by the coach`.

### State the counts and dates

Put these items in a short block under the table:

- Athletes expected, athletes with data, and athletes with no data.
- Rows used, and rows left out with the reason, such as `1 row with status device_failure`.
- The window, with both dates, and whether both ends are included.
- The measure, its unit, its variant, and the owning skill.
- The formula or query, or where to find it.

### Say what the noise allows

Follow these rules for any change over time:

- Compare the change with the noise band from the `monitoring-statistics` skill, `1.96 × TE × √(1 + 1/n)`, where TE is the typical error and `n` is the number of baseline values.
- When the change is inside the band, write it in these words or close to them: "The change is inside the noise band, so it may be measurement error."
- When the change is beyond the band, write: "The change is larger than measurement error." Add whether it is also beyond the smallest worthwhile change, as the `monitoring-statistics` skill describes.
- When there is no TE, write: "I cannot judge this change against measurement error without a typical error for this test."
- For several athletes, give the number of changes beyond the band expected by chance next to the number found, as the `coach-reports` skill describes.

### Hand off before you answer

Run the `check-ai-analysis` checks on the numbers before the answer goes to the coach. If a check fails, fix the query or say what failed in the answer. Do not drop the failed check.

### Use this template

Use this template, and fill each part from the query:

```text
<Direct answer, in units, for the restated question.> <Window: YYYY-MM-DD to YYYY-MM-DD.>
<Coverage: X of Y athletes with data. Missing: ID (reason), ID (reason).>
<Noise: inside the band, beyond the band, or cannot be judged.>

| athlete_id | <measure (unit)> | <count it rests on> | <comparison column> | note |
|---|---|---|---|---|

Threshold or baseline: <value, unit, and source>.
Rows used: <n>. Rows left out: <n, with reasons>.
Measure: <name, unit, variant>, from the <owning skill> skill.
Query: <formula or SQL>.
```

## Common mistakes

These are the mistakes AI tools make most often in the answer:

- Leading with method and caveats, so the answer is in the fifth paragraph.
- Leaving out athletes with no data, so the squad looks complete.
- Giving a count of rows as a count of athletes.
- Leaving out the date range, so the coach cannot tell which week the answer covers.
- Calling a change a drop or a gain without saying whether it is inside the noise band.
- Using a judgment word from the question as a label in the answer.
- Ranking athletes in the table, or using the words best, worst, top, or bottom in a label, title, or sentence.

## Example request

> How does Sam's jump compare with last month?

The answer in [worked-examples.md](worked-examples.md) shows the full shape.

## Check the result

Run these checks:

- Confirm the first sentences hold the answer, the window, the coverage, and the noise statement.
- Confirm the table has one row for each expected athlete.
- Confirm every column heading has a unit.
- Confirm no row order or word reads as a judgment of an athlete.

## Sources

The answer shape in this file is practice guidance from the authors of this repository. The noise band and the count of flags expected by chance come from the `monitoring-statistics` and `coach-reports` skills, which hold their sources.
