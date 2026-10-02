---
name: check-ai-analysis
description: Check an analysis of athlete data before you trust it, whether the AI wrote it or you pasted it. Test formulas, units, row counts, missing data, windows, noise, charts, and overreach.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "0.1"
  last-tested: "not tested"
---

# Check an AI analysis of athlete data

This skill is a checklist. Run it on any analysis of athlete data, whether you wrote it or the user pasted it, before anyone trusts the result.

## When to use

Use this skill when the user asks to:

- Check, review, or double-check an analysis, spreadsheet, Power BI or Tableau dashboard, chart, or report.
- Tell whether an AI answer about athlete data is right.
- Find out why two analyses of the same data disagree.

Run it on your own work too. Before you answer any request that produces numbers about athletes, run the checks on the numbers.

This skill covers these checks:

| Check | Reference file |
|---|---|
| All eleven checks, with how to test each one and the common failures | [references/checklist.md](references/checklist.md) |
| Typical error, smallest worthwhile change, and the noise band | [references/change-versus-noise.md](references/change-versus-noise.md) |

## Steps

Follow these steps in order:

1. Collect what you are checking: the request, a description of the input data, the method (formulas, code, or sheet steps), and the output.
2. If the method is missing, ask for it. Do not guess the method from the output.
3. Load the references you need:
   - Load [references/checklist.md](references/checklist.md).
   - Load [references/change-versus-noise.md](references/change-versus-noise.md) when the analysis reports a change over time or between tests.
4. Run each check in the order below.
5. Record `pass`, `fail`, or `could not check`, and the evidence for each.
6. Recalculate at least three values by hand from the raw data. Do not reuse the analysis's own code to recalculate. Report each recalculated or corrected value to the same number of decimals as the analysis you check, so the user can compare them line by line. If those decimals are more precise than the measure can be, say so as well.
7. Include one athlete with unusual data among the recalculated values.
8. In the results table, list every `fail` row first, then `could not check`, then `pass`.
9. For each failure, say what is wrong, what it does to the result, and how to fix it.
10. If the user asks you to fix the analysis, do these in order:
   - Fix the analysis.
   - Run the checks again on the fixed version.
11. Show the formula, the variant name, and the units next to each result you report.

## Checks

Run these checks on every analysis:

1. **Formula variant.** Name the formula variant. Confirm it matches the metric and the way the user's source calculates it.
2. **Units.** Confirm every column has a unit and that the unit is the same across rows, sources, and sides.
3. **Row counts.** Count the rows and athletes in the input, after each step, and in the output. Explain every difference.
4. **Missing data.** Confirm gaps are marked as missing, not filled with zero or carried forward. Confirm the report shows `n` and coverage.
5. **Averaging windows.** Confirm the window length, the window type, and whether the window includes the current day. Confirm the window handles missing days.
6. **Individual versus group.** Confirm a group result is not used to judge one athlete, and one athlete's result is not read as a group result.
7. **Plausible ranges.** Compare each value to physical limits, to the user's own history, and to a cited range in a reference file. Flag values that are impossible or far outside.
8. **Change versus noise.** Confirm every reported change is compared with the noise band, `1.96 x TE x sqrt(1 + 1/n)`, where TE is the typical error and `n` is the number of values in the baseline mean. Adding variances gives this band. Hopkins (2017) uses the same error, `TE x sqrt(1 + 1/n)`, for a change from the mean of several tests. The 95 percent level is this skill's choice. For the method, see [references/change-versus-noise.md](references/change-versus-noise.md). Apply these rules:
   - Confirm the assumptions behind the band are stated.
   - Confirm TE comes from a short-term retest with no true change expected, on the user's test, device, and population. Do not build a band from a published TE that does not match them, even as an illustration. Say the change cannot be judged until the user supplies a TE.
   - Pass a change as larger than error only when it lies beyond the band.
   - Pass a change as larger than the smallest worthwhile change only when the change minus the band is beyond it.
   - Make any other change read as not larger, or as larger than error that may or may not be worthwhile.
9. **Chart axes.** Confirm axes start where they should, have labels and units, and use the same scale when charts are compared.
10. **Overreach.** Confirm the text does not diagnose, predict injury, clear an athlete, or interpret a mood, stress, or free-text answer as a mental-health state.
11. **Reproducibility.** Confirm you can follow the steps from the raw data to the output with no hidden steps.

## Report the result

Return the results in a table with one row for each of the eleven checks, even a check that seems not to apply, with the reason in the Evidence column. Use these columns:

- **Check**: the name from the list above
- **Result**: `pass`, `fail`, or `could not check`
- **Evidence**: the numbers or cells you looked at
- **Fix**: what to change, for each `fail`

End the reply with a one-line verdict: `Safe to use`, `Use with the fixes above`, or `Do not use until fixed`. Make it the last line, after the table and any notes, even if you also state it at the top of the reply. If a check says `could not check`, name the information you need.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not invent a threshold or range. Use only figures from reference files you have, or from the user's own data, and name the source.
- Do not say an analysis is correct because it looks reasonable. Say which checks you ran and what you saw.
- Do not rewrite the analysis unless the user asks. A check reports problems. It does not change the work.
- Do not mark a check `pass` if you did not run it. Mark it `could not check`. If the output alone shows the failure, such as a missing unit, `n`, window, or formula, mark it `fail` even without the data.
- If mood, stress, or free-text items suggest a mental-health or welfare concern, do not interpret them. Tell the user to follow their organization's referral process and involve appropriate staff.
- If any athletes are minors, remind the user to check the consent rules and the rules on parent or guardian access to the data.
- If a metric skill is installed for the metric under review, load its reference file for the correct formula variant and range. If none is installed, say you could not check the variant against a reference, and ask the user for the definition they use.

## References

Load these files when needed:

- [references/checklist.md](references/checklist.md): the eleven checks, with how to test each and the failures that AI tools and spreadsheets make most often
- [references/change-versus-noise.md](references/change-versus-noise.md): how to tell a real change from measurement error, with formulas and sources
