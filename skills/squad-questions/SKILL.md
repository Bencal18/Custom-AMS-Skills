---
name: squad-questions
description: Answer a coach's quick question about the squad, such as who is over a threshold or how one athlete compares. Restates the question, asks when it is unclear, and checks the answer.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Squad questions

This skill helps you answer a coach's quick question about athlete data, such as "who is over threshold in the last four sessions?" It turns the question into a precise query, asks about anything unclear, and returns a short answer with the counts behind it.

This skill owns only two things: the step from question to query, and the shape of the answer. Every calculation belongs to the metric skill that owns the measure. Every answer goes through the `check-ai-analysis` checks before the coach sees it.

## When to use

Use this skill when the user asks a quick question about the squad or one athlete, for example:

- "Who is over threshold in the last four sessions?"
- "How does Sam's jump compare with last month?"
- "Who missed the most high-speed running this week?"
- "Which forwards had the lowest wellness scores yesterday?"
- "Who is ready for Saturday?" or "Who is struggling?"

Do not use it to build a full report or dashboard. Use the `coach-reports` or `ams-dashboards` skill for that.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| Restate a question as a filter, a time window, a measure, and a comparison, then build the query | [references/question-to-query.md](references/question-to-query.md) |
| Phrases that need a question back, and what to ask | [references/ambiguous-phrases.md](references/ambiguous-phrases.md) |
| The shape of the answer: sentences, table, counts, dates, missing athletes, and noise | [references/answer-format.md](references/answer-format.md) |
| Three worked questions, from question to answer | [references/worked-examples.md](references/worked-examples.md) |

## Route each calculation

Find the measure in the question, then hand its calculation to the skill in this table. Load that skill's reference file and follow its steps and clarifying questions. This skill never defines a formula of its own.

| Question about | Owning skill |
|---|---|
| Session RPE (rating of perceived exertion) load, heart rate load, weekly load, the acute:chronic workload ratio (ACWR), training monotony and strain, wellness scores, wellness z-scores, estimated load for an athlete with no device, taper volume reduction, intensity distribution, or recovery questionnaire scores | `load-and-wellness` |
| Total distance, metres per minute, high-speed running, sprint distance, accelerations, decelerations, peak demands, match-day load, or ice hockey tracking | `gps-running-load` |
| Countermovement jump height, reactive strength index-modified (RSI-modified), isometric mid-thigh pull force, Nordic hamstring force, or strength ratios such as the dynamic strength index and eccentric utilization ratio | `force-plate` |
| Bar speed, mean concentric velocity, velocity loss, or load-velocity profiles | `velocity-based-training` |
| Left versus right differences | `limb-symmetry` |
| A readiness or wellness composite score | `readiness-composites` |
| Sprint split times, sprint profiles, change of direction deficit, or repeated sprint scores | `sprint-testing` (version 1.1) |
| Maximal aerobic speed, anaerobic speed reserve, or interval distances from field test speeds | `conditioning-speeds` (version 1.1) |
| Where one athlete's test result sits against the squad, a position group, or a published norm | `testing-profiles` (version 1.1) |
| Heart rate variability (HRV) trends, submaximal heart rate tests, heart rate recovery, or sleep | `heart-rate-and-sleep` (version 1.2) |
| Volume load, estimated 1RM (one-repetition maximum), or personal bests in the weight room | `strength-training-load` (version 1.2) |
| Pitch counts, throw counts, jump counts, swim distance, or bowling volume | `sport-specific-counts` (version 1.2) |
| Whether a change is real or noise: typical error, smallest worthwhile change, baselines, and z-scores | `monitoring-statistics` |
| Tables, athlete IDs, joining sources, coverage, and missing data | `ams-data-setup` |
| A chart of the answer, or a view of the whole squad | `athlete-data-visualization` |
| What a coach view or an athlete view shows, and how to flag change | `coach-reports` |
| Checking the numbers before you answer | `check-ai-analysis` |

If the owning skill is not installed, say so. Ask the coach for the definition they use: the formula, the units, and any speed or time setting. Label the result with that definition as the coach's own. Do not invent a formula.

If a question touches two measures, route each one to its own skill.

## Steps

Follow these steps in order:

1. Load [references/question-to-query.md](references/question-to-query.md).
2. Write the question back as four parts: who (the filter), when (the time window), what (the measure), and compared with what (the comparison).
3. Load [references/ambiguous-phrases.md](references/ambiguous-phrases.md).
4. Mark each part the coach did not state, or stated with a phrase from that file.
5. Ask about every marked part in one message. Offer a default for each, and label it as a default. Wait for the answer before you calculate.
6. For words such as "ready", "tired", or "struggling", ask which measure the coach means. Do not decide what the word means, and do not judge the athlete.
7. If the question asks to rank the whole squad, follow the no-ranking rules below and offer the alternatives.
8. Find the owning skill for each measure in the routing table. Load its reference file.
9. Ask the owning skill's clarifying questions that apply, such as the device, the speed setting, or best trial versus mean of trials (`force-plate` step 9).
10. Ask for the data, or confirm the columns, units, and athlete IDs. Use the table layout from `ams-data-setup` when it is installed. Use `athlete_id`, not names.
11. Build the query in the coach's tool, as [references/question-to-query.md](references/question-to-query.md) describes. Start from the full roster, so athletes with no data stay in the result.
12. Calculate each value with the owning skill's method.
13. For a change over time, compare it with the noise band from `monitoring-statistics`. The noise band is the size of change that measurement error alone stays inside about 95 percent of the time. If the coach has no typical error, say the change cannot be judged against measurement error.
14. Count the athletes expected, the athletes with data, and the rows used. List each missing athlete with the reason, when known.
15. Run the `check-ai-analysis` checks on your numbers. If that skill is not installed, run the checks below.
16. Load [references/answer-format.md](references/answer-format.md), and write the answer in that shape.

## Answer a request to rank the squad

A ranking turns small, noisy differences into a verdict on each athlete. If the coach asks for the best, the worst, a top five, or a full order, follow the squad views reference in the `athlete-data-visualization` skill. If that skill is not installed, follow these rules:

- Do not number athletes in order, and do not use the words best, worst, top, or bottom in any label, title, or sentence of the answer.
- When the coach says "best" or "worst", ask which measure, then sort by change from each athlete's own baseline. Show the noise band, and say `Sorted by change, not by ability`.
- Give the table a title that describes the data, such as `Change in CMJ height from own baseline, week of 2026-09-28`.
- Offer one row per athlete in roster or position order, with each athlete's value and change.
- Keep athletes with no data in the list, labeled `no data`.
- If the coach still wants an order, show each value with its noise. TE is the typical error, the noise in a test. Say two athletes' single values differ beyond noise only when their difference is larger than `1.96 × √2 × TE`. To compare two athletes' changes from their own baselines of `n` values, use `1.96 × TE × √(2 × (1 + 1/n))`. Do not judge by whether two intervals overlap.

## Checks before answering

Run these checks on your own result before you show it:

- Restatement check: confirm the answer matches the restated query: the same athletes, window, measure, and comparison.
- Window check: confirm the first and last dates in the data used match the window you stated.
- Count check: confirm the athletes in the answer plus the missing athletes equal the athletes expected.
- Missing check: confirm no missing value became zero, and no athlete with no data dropped out of the table.
- Status check: confirm the query kept only rows with a usable status. A text code such as `NA` can pass a `> 600` test in some spreadsheets.
- Threshold check: confirm the threshold is the coach's, with its source, and that the answer says whether "over" means above or at or above.
- Noise check: confirm every change has its noise band, or a line saying it cannot be judged.
- Wording check: confirm the answer does not call an athlete ready, tired, fatigued, struggling, at risk, or cleared, and does not rank athletes. Confirm no label or title uses best, worst, top, bottom, or a rank number.
- Recompute check: recompute one athlete by hand and confirm it matches the query.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. The coach makes every training decision.
- Do not answer a different question from the one the coach asked. If you change a part of the question, say so in the first sentence of the answer.
- Do not infer a judgment about an athlete from a word such as "ready", "tired", or "struggling". Report the measure the coach chose, in its units.
- Do not invent a threshold, window, or range. Use the coach's choice or a figure from the owning skill's reference file, and name the source.
- Do not fill, estimate, or carry forward missing values unless the coach asks. If the coach asks, show the answer with and without the filled values.
- These skills cover monitoring of healthy athletes. If the question is about an injured athlete, an athlete in rehab, or pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- If mood, stress, or free-text answers suggest a mental-health or welfare concern, do not interpret them. Tell the user to follow their organization's referral process and involve appropriate staff.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool. Keep names out of the data, and use `athlete_id`.
- If any athletes are minors, remind the user to check the consent rules and the rules on parent or guardian access to the data.

## References

Load these files when needed:

- [references/question-to-query.md](references/question-to-query.md): how to restate a question as a filter, a window, a measure, and a comparison, and how to build the query in a spreadsheet or SQL
- [references/ambiguous-phrases.md](references/ambiguous-phrases.md): common phrases that need a question back, with the question to ask and a labeled default
- [references/answer-format.md](references/answer-format.md): the answer's sentences, table, counts, date range, missing athletes, and noise statement
- [references/worked-examples.md](references/worked-examples.md): three made-up coach questions worked from question to answer, with spreadsheet formulas and SQL
