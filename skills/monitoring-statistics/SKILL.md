---
name: monitoring-statistics
description: Decide if a change in an athlete's data is real or noise. Covers typical error, smallest worthwhile change, MDC, baselines, z-scores, and why ACWR and p-values mislead.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
  last-tested: "not tested"
---

# Statistics for athlete monitoring

This skill helps you decide whether a change in an athlete's data is real, and whether it is big enough to matter. It applies to any measure: jumps, sprints, strength tests, heart rate, wellness scores, or training load.

## When to use

Use this skill when the user asks to:

- Tell whether an athlete's change is real or only noise.
- Work out the typical error, coefficient of variation, or reliability of a test.
- Set a smallest worthwhile change or a minimal detectable change.
- Build a rolling baseline or z-scores against an athlete's own history.
- Flag athletes who are unusually high or low.
- Judge whether a group result was "significant".
- Calculate or explain the acute:chronic workload ratio (ACWR).

This skill covers these topics:

| Topic | Reference file |
|---|---|
| Typical error and coefficient of variation | [references/typical-error.md](references/typical-error.md) |
| Smallest worthwhile change, and comparing a change with noise | [references/smallest-worthwhile-change.md](references/smallest-worthwhile-change.md) |
| Minimal detectable change | [references/minimal-detectable-change.md](references/minimal-detectable-change.md) |
| Individual baselines and z-scores | [references/individual-baselines-z-scores.md](references/individual-baselines-z-scores.md) |
| ACWR problems and group p-values | [references/misleading-methods.md](references/misleading-methods.md) |

## Terms

Use these meanings, and define each term for the user on first use:

- **Typical error (TE):** the noise in a test. It is the SD of one athlete's repeated scores when nothing real changed. It is also called the standard error of measurement (SEM).
- **Coefficient of variation (CV%):** typical error as a percent of the mean
- **Smallest worthwhile change (SWC):** the smallest change that matters in practice. By default, it is 0.2 × the SD between athletes (Hopkins et al., 2009).
- **Minimal detectable change (MDC):** the smallest change larger than noise, at a stated confidence level. MDC95 = SEM × 1.96 × √2 (Weir, 2005).
- **Noise band:** error alone gives a change smaller than this about 95 percent of the time. Against a baseline mean of n values, it is 1.96 × TE × √(1 + 1/n). This form adds the variances of the new value and the baseline mean. Hopkins (2017) uses the same error for a change from the mean of several tests. For two single tests, it is 1.96 × √2 × TE, about 2.77 × TE.
- **Baseline:** an athlete's own normal, from their prior values
- **z-score:** how far today's value is from the athlete's baseline mean, in units of the athlete's baseline SD

## Core rule

Compare every change against measurement noise before you call it meaningful. A change is "real" only if it is larger than the noise of the test.

A change is "worthwhile" only if it is also large enough to matter. Check both, in that order.

Never call a change meaningful, important, or significant from its size alone, from a z-score alone, or from a group p-value.

## Steps

Follow these steps in order:

1. Ask which measure, test protocol, and units the data uses, if the user has not said.
2. Ask for the noise estimate. Follow these rules:
   - Accept the user's own test-retest data, a typical error the user knows, or a published value for the same protocol.
   - If none exists, say the change cannot be judged against noise without one.
   - Show how to collect test-retest data.
3. Load [references/typical-error.md](references/typical-error.md) when you need to compute TE or CV% from test-retest data.
4. Load [references/smallest-worthwhile-change.md](references/smallest-worthwhile-change.md) to set the SWC and to label each change.
5. Load [references/minimal-detectable-change.md](references/minimal-detectable-change.md) when the user asks for an MDC or a "real change" threshold.
6. Load [references/individual-baselines-z-scores.md](references/individual-baselines-z-scores.md) when the user wants baselines, z-scores, or flags.
7. Load [references/misleading-methods.md](references/misleading-methods.md) when the user asks about ACWR, "danger zones", or whether a group change was significant.
8. Compute each change in the units of the measure.
9. Ask which confidence level the user wants. Follow these rules:
   - If the user has no preference, use 95% (z = 1.96).
   - Tell the user the level and why, in these words or close to them: "I used 95% because it matches common MDC95 reporting. It is a default choice, not a rule."
   - Offer 90% as an option.
   - Offer Hopkins's practical threshold of 1.5 to 2.0 × TE only with its cost: for two single tests it flags 28.9% or 15.7% of pure-noise changes, against 5% at 2.77 × TE.
10. Build the interval `change ± z × √2 × TE` for two single tests, or `change ± z × TE × √(1 + 1/n)` against a baseline mean of n values. Follow these rules:
    - If TE comes from few athletes, replace z with t. Take the degrees of freedom from the TE study: athletes − 1 for two trials, or (athletes − 1) × (trials − 1) for the two-way model. TE from 6 athletes gives t(5) = 2.57.
    - Label the change with the table in the SWC reference file.
11. When only one direction matters, such as a drop, say the chance rate of a false flag is 2.5% at z = 1.96, not 5%.
12. For a squad, report the flags expected by chance next to the flags found: number of results × 5%, or × 2.5% for one direction. For 25 athletes checked for drops, you expect 0.625 false flags each week. The chance of at least one is 46.9%. Flags in consecutive weeks against the same baseline are not independent.
13. Recommend a repeat test before anyone acts on a single flag, because of regression to the mean (Barnett et al., 2005).
14. Show the formula, the variant name, and the units next to every result.
15. State the method and the window you used: the baseline window, the number of values in it, the SD type, the confidence level, and the source of TE and SWC.
16. Run the checks below before you answer.

## Report format

Report each athlete's result with these items:

- The value, the baseline or previous value, and the change, with units
- The TE and its source, the SWC and the group it came from, and the confidence level
- The interval and the label, such as "real, and at least as large as the SWC"
- For z-scores: the window, n, the baseline mean, the baseline SD, and the z-score
- One plain sentence a coach can read

## Checks before answering

Run these checks on your own result before you show it:

- Noise check: confirm you compared every change with TE or the MDC before you called it real.
- Formula check: confirm you divided by √2 for TE from difference scores. Confirm you multiplied TE by √2 for two single tests, or by √(1 + 1/n) for a new value against a baseline mean of n values.
- SD check: confirm you used the sample SD (`STDEV.S()`, pandas `.std()`, or `ddof=1`), not the population SD.
- Baseline check: confirm today's value is not part of its own baseline.
- TE check: confirm TE came from a short-term test-retest study with no true change expected, on the same summary (single trial, best of 3, or mean of 3) as the values compared. A separate-day retest is an optional choice that gives a larger TE. Do not use the athlete's own baseline SD as TE.
- Multiplier check: confirm the multiplier fits the TE study. Use t with the TE study's degrees of freedom when TE comes from few athletes, not the baseline count.
- Assumption check: state the noise band's assumptions: the athlete's true score stayed constant over the baseline and the new test, errors are independent, TE is the same across athletes and values, and TE is known. Say that when they fail, the real false flag rate can be higher or lower than 5%. Never call 5% a lower bound.
- Band check: for a band against a baseline mean, say it adds the variance of the new value to the variance of the baseline mean, as Hopkins (2017) does.
- Squad check: confirm squad reports show the flags expected by chance next to the flags found.
- Group check: confirm the SWC used a comparable group, not a mix of sexes, levels, or squads.
- Unit check: confirm the change, TE, SWC, and MDC share one unit, or are all percents.
- Count check: confirm the number of athletes, tests, and baseline values matches the input. Count each label in your per-athlete results, and confirm every count in your summary, headline, and the line that gives the number of flags found matches those labels. Report n with every result.
- Manual check: recompute one athlete's result and confirm it matches.
- Label check: confirm no result is labeled as an injury risk, a readiness verdict, or a clearance decision.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Keep to these limits:

- Frame every result as decision support. Do not diagnose, predict injury, or make clearance, return-to-sport, or training decisions. Leave those to the practitioner.
- Do not invent a threshold, window, or minimum sample size. Use only the figures in the reference files, and name the source. Where the reference files say no source sets a value, ask the user, offer a default, and label it as a default.
- Do not present an ACWR value as an injury risk, and do not apply a "sweet spot" or "danger zone" range.
- Do not use a group p-value to judge an individual athlete. Label each athlete against noise and the SWC. If you report a group p-value, put it after the individual results, with the sample size.
- Do not borrow a typical error from a different test protocol, device, or population without saying so.
- Do not use the athlete's own baseline SD as a stand-in for TE. It needs a t multiplier with few values, and it mixes biological variation with measurement error.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.

## References

Load these files when needed. They hold the full citations for every source named in this file:

- [references/typical-error.md](references/typical-error.md): typical error, coefficient of variation, and test-retest data
- [references/smallest-worthwhile-change.md](references/smallest-worthwhile-change.md): the SWC, its variants, and how to label a change against TE and SWC
- [references/minimal-detectable-change.md](references/minimal-detectable-change.md): the MDC formula, its confidence levels, and how it differs from the SWC
- [references/individual-baselines-z-scores.md](references/individual-baselines-z-scores.md): rolling baselines, z-scores, window choice, and minimum data
- [references/misleading-methods.md](references/misleading-methods.md): ACWR variants and their statistical problems, and why group p-values mislead
