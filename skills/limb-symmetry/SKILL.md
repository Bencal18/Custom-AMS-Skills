---
name: limb-symmetry
description: Calculate and check left versus right limb symmetry or asymmetry percentages from jumps, strength tests, or Nordic data, with the formula and reference limb named. Decision support only.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Limb symmetry

This skill helps you compare an athlete's left and right limbs with a named, consistent formula. It explains why the same data give different percentages in different formulas, and it keeps every result as decision support.

## When to use

Use this skill when the user asks to:

- Calculate a limb symmetry index (LSI), asymmetry percentage, or left versus right difference.
- Compare the dominant limb with the nondominant limb, or the stronger limb with the weaker limb.
- Explain why two reports show different asymmetry numbers for the same athlete.
- Choose a formula for single-leg tests or two-plate tests.
- Write a spreadsheet formula, Python or R code, or a Power BI or Tableau calculation for left versus right comparisons.
- Check whether an asymmetry number looks right.

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| Limb symmetry index and asymmetry formula variants | [references/limb-symmetry-index.md](references/limb-symmetry-index.md) |

## Steps

Follow these steps in order:

1. Ask which device and test the data came from, if the user has not said.
2. Load the device file when one exists for that device.
3. Load `references/limb-symmetry-index.md`.
4. Ask whether the test is unilateral (each limb tested on its own) or bilateral (both limbs push on one shared load at the same time, such as a two-plate jump), if it is not clear. The Nordic hamstring test is a two-leg task: both legs resist at the same time, each on its own sensor. Even so, its default is percentage difference against the stronger leg, because Nordic studies express imbalance on a one-leg scale (Opar et al., 2015; Bourne et al., 2015). BAI-1 would give about half the one-leg values.
5. Offer the log ratio, 100 × ln(right / left), as an option for the Nordic hamstring test. Give this reason: it gives the same size whichever leg is stronger. Do not say it matches the Nordic studies. Opar et al. (2015) used a left-to-right ratio and log-transformed it only to calculate group means.
6. Ask which formula the user's report or comparison uses.
7. If the user names none, use percentage difference for unilateral tests and the Nordic test, and the bilateral asymmetry index (BAI-1) for bilateral tests, and tell the user you chose it.
8. If no dominant limb is named, calculate BAI-1 as right minus left, and say so.
9. Ask which limb is the reference: dominant and nondominant, or the larger value (stronger and weaker). If the user names none, use the larger value, say so, and still ask for each athlete's dominant limb.
10. Record the reference limb for each athlete, and keep it the same across sessions.
11. Never infer the dominant limb from the data. If the user does not name it, do not calculate an LSI.
12. List each input column with its unit.
13. Confirm left and right labels against the device file.
14. Use the same trial summary for both limbs, either the best trial or the mean of trials.
15. Ask which trials the athlete or tester excluded, and why.
16. Apply the same exclusion rule to both limbs and every session.
17. Report how many trials you excluded per limb.
18. Calculate the value with the formula in the reference file. Follow its "Calculate the metric" steps.
19. Judge the left-right difference with one rule, whatever formula you report: the difference in raw units is larger than noise only when it exceeds 1.96 × √(SE_left² + SE_right²). SE is the test's typical error for single or best trials, or a pooled squad coefficient of variation × the limb's value / √k for a mean of k trials.
20. Take the SE from a squad reliability study, or from a published reliability study of the same test, device, and population, never from one athlete's own trials or from the same trials you are judging.
21. For a left-right difference from one session, use a within-session typical error, from trials repeated in the same session, when such a study exists. If only a separate-day typical error exists, use it, and label the band "likely wider than needed". Day-to-day changes that affect both limbs alike cancel out of a same-session difference, so a separate-day typical error widens the band. In one force plate study, within-session typical error was a median 0.90 times the separate-day value (Heishman et al., 2019b).
22. State the SE, its source, and whether it came from the same session or separate days.
23. If no SE exists, say the difference cannot be judged against noise. Judge a change in one limb's value between sessions with the `monitoring-statistics` skill if it is installed, or say it cannot be judged without a typical error.
24. Run the checks below.
25. Report the result in this format: both raw limb values with units, the formula name and equation, the reference limb, the percentage with its sign, the larger side, the SE and its source, the band, and whether the difference is outside it. For a bilateral test, add the device's own asymmetry formula next to BAI-1 only where the device documents it, as described below.
26. When the difference is inside the band, write: "The difference cannot be told apart from measurement noise with these data. This does not show that the limbs are equal."

Bishop et al. (2021) drew one line per metric at the largest group coefficient of variation across the tests and limbs they compared. Use it only if the user asks, and call it an optional, lenient screen. It flags more differences than the band.

If the user wants to compare with a value from another source, recalculate both values with the same formula first. If you cannot, say the values are not comparable.

If the device export gives its own asymmetry column, check the device file for its formula. Never read its sign. Recompute from the left and right values. Do not mix it with values from another formula.

For a bilateral test, follow these rules to show the device's own asymmetry formula next to BAI-1:

- Show it only when the device documents its formula. The VALD ForceDecks Technical Glossary V2.0 gives (left − right) / max(left, right) × 100. A positive value means the left limb is larger.
- Recompute it from the left and right values. Never copy the vendor column.
- Label it with the device name and the larger side. For example, left 920 N and right 1000 N give "BAI-1: 4.17%, right larger" and "VALD ForceDecks formula: −8.00%, right larger".
- Hawkin Dynamics and the VALD NordBord app do not publish their formulas. For those devices, say the formula is unpublished, and show no device value.

If the `ams-data-setup` skill is installed, use its table layout. If the `monitoring-statistics` skill is installed, use it to judge whether a change over time is larger than noise.

## Checks before answering

Run these checks on your own result before you show it:

- Formula check: confirm every value in one column uses the same formula and the same reference limb.
- Recompute check: recompute one athlete by hand and confirm it matches your code or formula.
- Sign check: for values this skill calculates, confirm the sign matches the larger side. In signed percentage difference, positive means right is larger. Vendor values may use the opposite sign.
- Scale check: confirm you did not mix symmetry values (100% means equal) with asymmetry values (0% means equal).
- Denominator check: confirm the denominator is the limb or total the formula names.
- Near-zero check: flag any pair where both values are close to zero. The percentage will be unstable.
- Side check: confirm left and right labels were not swapped between the export and your table.
- Count check: confirm the number of athletes, sessions, and trials per limb matches the input.
- Raw value check: every percentage, including ones in running text and equations, has both limb values with units beside it.
- Noise check: confirm you compared the raw difference with the band from step 19, stated the SE source and its retest interval, and used the required wording when it is inside the band.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

This skill gives decision support only. Follow these limits in every answer:

- Do not make clearance, return-to-sport, return-to-training, injury-risk, or training decisions. Leave those to the practitioner.
- Do not diagnose an injury or say an athlete is injured, at risk, ready, cleared, recovered, or safe.
- Do not apply any threshold as a pass or fail. Thresholds depend on the formula, test, metric, and population. Do not invent one.
- If the user asks whether an athlete can return to sport or play, state that this skill cannot answer that.
- If the user asks about a 90% LSI or any other clearance or return-to-sport criterion, state that symmetry is not a clearance criterion. Do not say whether the athlete meets it.
- These skills cover monitoring of healthy athletes. If an athlete is injured or in rehab, or reports pain or another symptom, do not analyze it here. Tell the user to involve the medical team.
- Do not present an LSI as a measure of change on its own. Either limb can change. Show each limb's own value over time.
- Do not compare percentages from different formulas, tests, metrics, or devices as if they were the same.
- Do not drop the raw limb values. Show both values, with units, next to every percentage, including ones in running text.
- Use only the figures in the reference file, and name the source and population.

## References

Load these files when needed:

- [references/limb-symmetry-index.md](references/limb-symmetry-index.md): limb symmetry index and asymmetry formula variants, the reference-limb rule, the effect of the denominator, and why thresholds depend on context
- [references/vald-forcedecks.md](references/vald-forcedecks.md): how to read and transform VALD ForceDecks API output and exports
- [references/vald-nordbord.md](references/vald-nordbord.md): how to read and transform VALD NordBord API output and exports
- [references/hawkin-dynamics.md](references/hawkin-dynamics.md): how to read and transform Hawkin Dynamics API output and exports, and which Hawkin metrics share a name with VALD metrics but differ
