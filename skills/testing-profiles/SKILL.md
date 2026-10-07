---
name: testing-profiles
description: Show where an athlete's test results sit against the squad, position group, or matched norms, with measurement error. Checks sample size, protocol match, and trial choice.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Testing profiles

This skill helps you show where one athlete's result on each test sits against the squad, the athlete's position group, or a matched published norm. It reports each position as a percentile or in SD units, with measurement error beside it. It never ranks the squad.

## When to use

Use this skill when the user asks to:

- Show where an athlete sits in the squad on a jump, sprint, strength, or fitness test.
- Compare an athlete with their position group.
- Compare an athlete's result with a published norm or a local norm from past squads.
- Build a test profile of one athlete across several tests.
- Turn test results into percentiles or SD units in a spreadsheet, Power BI, Tableau, or Python.
- Rank the squad, build a leaderboard, or combine tests into one score. This skill declines that part. See [Decline a ranking request](#decline-a-ranking-request).

This skill covers these topics:

| Topic | Reference file |
|---|---|
| Percentile and SD units within the squad and position group, with measurement error | [references/squad-position.md](references/squad-position.md) |
| When a published norm may be used, and how to read it | [references/published-norms.md](references/published-norms.md) |

## Steps

Follow these steps in order:

1. Ask which tests, device, and test day the data came from, if the user has not said.
2. If a skill for the test is installed, such as `force-plate`, use it to calculate each result. Name the method and variant.
3. Ask what to compare with: the squad, the position group, a published norm, or more than one.
4. Ask who will see the result: staff or the athlete. For an athlete view, follow the athlete view rules in the audience reference of the `coach-reports` skill. Show squad position to an athlete only if the user confirms it is allowed, and never show teammates by name.
5. Ask whether each result is the best trial or the mean of trials, if the user has not said. Use one choice for every athlete, for the TE, and for any norm. This follows step 9 of the `force-plate` skill.
6. Ask which trials were excluded, and why. Use the same exclusion rule for every athlete.
7. Ask for the typical error (TE) of each test, on the same protocol and trial summary. TE is the noise in a test: the SD of one athlete's repeated scores when nothing real changed. Use the `monitoring-statistics` skill to calculate or check it.
8. If the user has no TE, show the positions, and say they carry no measurement error. Show how to collect a short retest.
9. Build each comparison group from results on the same test day, protocol, device, method, and trial summary.
10. List every athlete in the group with no result. Do not fill a missing result.
11. Load [references/squad-position.md](references/squad-position.md) for squad and position group comparisons.
12. Calculate the percentile with definition C, the step size, and SD units, for each test and group.
13. Load [references/published-norms.md](references/published-norms.md) for any norm.
14. Check every item in its match table. If one item does not match, stop and name it.
15. Calculate the norm percentile and its interval with the method for the norm's format.
16. Put measurement error beside every value: the error range in raw units, and the matching range in percentiles or SD units.
17. Flip timed tests so a higher percentile means a faster time. Say so in the row label.
18. Show one athlete per view. Use one row per test, in a fixed test order.
19. For a chart, use the profile dot plot in the relationships reference of the `athlete-data-visualization` skill. Add an error bar for each test. Do not use a radar chart.
20. Write each test as one plain sentence, for example: "CMJ: 58th percentile of 12 squad athletes (definition C, steps of 8.3). With measurement error, 21st to 79th."
21. Run the checks below.
22. Show the formula, the definition, the group, `N`, the TE source, and the units next to each result.

If the `ams-data-setup` skill is installed, use its table layout for athletes, sessions, and measures. If the `check-ai-analysis` skill is installed, use it to review the result before a report goes out.

## Decline a ranking request

This repository does not rank athletes against each other. The rules sit in these places. Name them, and do not restate them:

- The ranking check in the `athlete-data-visualization` skill.
- The section on ranking that reads as judgment, in the squad views reference of the `athlete-data-visualization` skill.
- The athlete view and common mistakes, in the audience reference of the `coach-reports` skill.
- The sub-score rules in the `readiness-composites` skill.

A ranking request includes any of these:

- Rank the squad, or list athletes best to worst on a test.
- Number athletes, such as `#1` to `#25`, or name a top 5, a bottom 5, a best, or a worst.
- Build a leaderboard, medals, or a table sorted by a result or a percentile.
- Combine several tests into one score, total, or index to compare athletes.

When the user asks for any of these, follow these steps:

1. Say in one sentence that this skill does not build an ordered list, rank numbers, or a score across tests.
2. Say why in one sentence: rank order between athletes moves with measurement error, and these skills keep every test visible.
3. Offer the outputs in the list below.
4. Build the output the user picks.

Offer these outputs instead:

- A profile for each athlete: every test as a percentile and in SD units, with measurement error, one athlete per page.
- A squad dot plot for one test: every athlete's value with an error bar, in roster or position order.
- The athlete's position within the squad and within the position group, side by side, with `N` and the step size.
- A comparison with a matched published norm, with its interval.
- For a "who changed" question, change from each athlete's own baseline, as in the squad views reference of the `athlete-data-visualization` skill.

If the user insists, keep declining the ordered list. Do not produce it in another form, such as a table sorted by percentile, a highlighted top group, or a color scale by rank. Do not answer "who is the best" with a name. Show the distribution instead.

## Checks before answering

Run these checks on your own result before you show it:

- Definition check: every percentile names definition C, or the norm method used.
- Count check: `N` for each group matches the athletes with a result. Athletes with no result are listed.
- Step check: the step, `100 / N`, appears next to every squad or group percentile.
- Error check: every value has measurement error beside it, with the TE and its source. If no TE exists, the output says so.
- Trial check: every athlete, the TE, and any norm use the same trial summary.
- Match check: every norm passed every item in the match table, and the output states the norm's population, protocol, and `n`.
- Direction check: timed tests are flipped and labeled.
- Order check: no output lists athletes in order of a result or a percentile. Rows sit in roster or position order.
- Composite check: no output adds, averages, or weights results across tests.
- Language check: no rating word, such as `elite`, `poor`, `weak`, `below standard`, `pass`, or `fail`, and no rank number.
- Recompute check: recompute one percentile and one SD unit value by hand, and confirm they match.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- A position against the squad or a norm describes where a result sits. It is not a rating, a target, or a standard to meet.
- Use a published norm only as a reference, and only when it matches. Never apply it as a pass or fail.
- Do not invent a norm, a threshold, a band, or a minimum group size. Use only the figures in the reference files, and name the source.
- Do not quote a norm from memory. Ask the user for the source, or open it.
- Do not rank, order, or number athletes, and do not build a composite across tests. See [Decline a ranking request](#decline-a-ranking-request).
- Do not compare results across protocols, devices, methods, trial summaries, or test days without saying so.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed:

- [references/squad-position.md](references/squad-position.md): percentile with definition C, ties, step size, small groups, SD units, measurement error beside each value, and timed tests
- [references/published-norms.md](references/published-norms.md): when a norm matches, the t method for a mean and SD, intervals on a norm percentile, raw and local norms, and percentile tables
