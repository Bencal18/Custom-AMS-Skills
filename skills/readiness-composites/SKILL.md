---
name: readiness-composites
description: Build or check a readiness-style composite of wellness and test results, shown as distance from the athlete's own baseline with every sub-score. Decision support only, never clearance.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Readiness composites

This skill helps you build, audit, or explain a composite score that combines several monitoring measures into one number. It keeps every input visible next to the composite, so the reason for a change is never hidden. Label the output "composite distance from baseline", not "readiness score".

## Decision support only

A composite score is decision support. It is never a decision. Follow these rules in every answer:

- Do not clear, rule out, or approve an athlete for training, competition, or return to sport from a composite score or any of its inputs.
- Do not call any composite value or input "ready", "cleared", "safe", "fit to play", or "at risk". Describe a composite or an input as above, near, or below that athlete's own baseline only against a cut-off the user chose, and name that cut-off. Without a cut-off, give numbers instead: for an input, its z-score and its change in raw units; for the composite, its value with each input beside it.
- Do not turn a composite into an injury-risk score, an injury prediction, or a probability.
- Do not recommend a training dose, a load change, a rehab progression, or a return-to-sport stage.
- Do not diagnose illness, injury, or overtraining.
- If the user asks for any of these, say that the decision belongs to the qualified practitioner and the athlete. For training and return to sport, the coach shares it. Offer to show the inputs and their changes for that conversation instead.

Return to sport is a shared decision across a continuum. Clinicians, athletes, and coaches make it, and it weighs risk and risk tolerance (Ardern et al., 2016; Shrier, 2015). A composite score cannot carry that judgment. See [references/readiness-composites.md](references/readiness-composites.md).

## Rehab athletes

Follow these rules for any athlete in rehab:

- Do not calculate a single composite by default. Show a table with one row for each input: the raw value, the change since the last test, and the percentage of the pre-injury value. Calculate a composite only when the medical team asks for one, and show the table beside it.
- Never put a red-flag sign into a composite, a z-score, or a percentage. Show each one as a raw value.
- Sort any report of a red-flag sign into a tier, and tell the user what the tier says to do, whatever the other inputs show. The tiers are listed below.
- Tell the user that no sports-specific red-flag list was found. The tiers come from general clinical guidelines, and a clinician should confirm them. The qualifier "out of proportion to the exercise" is the authors' wording, not a guideline's. The authors added it because breathlessness is normal during training.
- Keep rehab load, such as rehab session RPE, beside the table or the composite. Never put it into a composite, even when the user asks. A direction on rehab load implies a progression call.
- Use a pre-injury baseline only when it used the same test, device, protocol, and arm condition while the athlete was healthy. Record its date and season phase. The clinician decides whether it is too old. Without a valid pre-injury baseline, leave the percentage column blank and say why.
- State that a composite or an input back at the pre-injury baseline is not a return-to-sport criterion.
- Name the baseline: pre-injury or a fixed post-injury block. Prefer a valid pre-injury baseline, and tell the user it shows the remaining deficit. Do not use a rolling baseline in rehab. If you mention one, tell the user it follows the athlete upward and hides progress: steady recovery reads as the same small z-score every day. Against a fixed post-injury block, show the change in raw units, because the z-scores grow very large.

These tiers are safety referrals, not a training recommendation. Use these red-flag tiers:

- Call emergency services: chest pain, sudden or unexplained shortness of breath, out of proportion to the exercise, or coughing up blood. Also severe or worsening weakness or numbness in both legs, with back or leg pain.
- Stop the session and refer the same day for any of these signs:
  - Calf pain, or new swelling, warmth, or tenderness in one calf or leg, which is more urgent after surgery or immobilization
  - Wound redness or discharge
  - Fever
  - New numbness or weakness in one limb
- Pass to the medical team: pain or swelling at the injured joint or tissue, loss of motion, giving way, and locking.

## When to use

Use this skill when the user asks to:

- Combine wellness, jump, or other test results into one readiness score.
- Build a dashboard with colors or arrows from several measures, under the color rules in Limits.
- Check a readiness score from an app, a spreadsheet, or a Power BI or Tableau dashboard they inherited.
- Track a rehab athlete's monitoring measures for the medical team. Show a table for each input, not one score, unless the medical team asks for a composite.
- Understand why a composite score went up or down.

This skill covers this metric:

| Metric | Reference file |
|---|---|
| Readiness and rehab-monitoring composites | [references/readiness-composites.md](references/readiness-composites.md) |

## Steps

Follow these steps in order:

1. Ask what the composite is for and who will read it.
2. If the purpose is clearance, return to sport, or injury prediction, explain the limit above before you continue.
3. Ask which form, app, or device each input came from, and for one example row of each with names removed.
4. Load [references/readiness-composites.md](references/readiness-composites.md).
5. For a rehab athlete, build the table for each input from Rehab athletes. Continue to a composite only if the medical team asked for one.
6. List every input with its unit and its direction (is a higher value better or worse).
7. Confirm the list with the user.
8. Keep load measures, such as session load, distance, or ACWR, out of the composite by default.
9. Show load measures in their own columns beside the composite.
10. If the user insists on adding a load measure for a healthy athlete, ask them to state its direction and the reason. For a rehab athlete, keep rehab load out even when the user asks.
11. Label that load measure as the user's choice.
12. Keep the red-flag signs listed above out of the composite. Show each one raw, with its tier.
13. Remove inputs that count the same thing twice, such as a load and a ratio built from that load.
14. Tell the user which inputs you removed and why.
15. Ask for the baseline window and the minimum number of baseline days for each input. If the user has none, offer at least 10 prior values, labeled as a practice default.
16. Standardize each input against that athlete's own baseline, as a z-score that excludes the day being scored.
17. Flip the sign of any input where a higher value is worse, so a positive z-score means "better than usual" for every input.
18. Ask for the weights.
19. If the user has none, use equal weights and say so. Never invent unequal weights.
20. Say what share of the weight each construct gets.
21. Offer to group related items first.
22. Calculate the composite only on days with every input present, unless the user chooses another rule.
23. Name the missing-input rule you used.
24. Show a table with every input's raw value, change in raw units, baseline mean, z-score, and the composite, side by side.
25. Name the largest contributors to each change in the composite.
26. Show the formula, the weights, the baseline window, and the units next to every result.
27. Run the checks below before you answer.

## Checks before answering

Run these checks on your own result before you show it:

- Sub-score check: every input's z-score, raw value, and change in raw units appear next to the composite in the output.
- Direction check: for every input, a positive z-score means the same thing (better than usual).
- Baseline check: each z-score uses only that athlete's data and excludes the day being scored.
- Weight check: the weights in the formula match what the user gave, and they are shown with each construct's share.
- Load check: no load measure is inside the composite unless the user chose it for a healthy athlete and stated its direction and reason. Rehab load is never inside it.
- Red-flag check: no red-flag sign from the three tiers is inside the composite, and each reported sign shows its tier and what the tier says to do.
- Rehab check: for a rehab athlete, the output is a table for each input unless the medical team asked for a composite. The pre-injury baseline shows its date and season phase.
- Missing check: no missing input was treated as zero or as baseline. Days with missing inputs are marked.
- Double-count check: no two inputs come from the same raw data.
- Arithmetic check: recalculate one athlete-day by hand and show it: each input's z-score from its baseline mean and SD, the direction sign, then the weighted mean.
- Chance check: when you flag composites across a squad against the user's cut-off, show the number of flags expected by chance next to the number found. If the user has no cut-off, do not count athletes past an example cut-off.
- Language check: the answer, its labels, and any color legend contain no clearance, readiness verdict, injury-risk, or training-dose wording.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Keep to these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not invent a threshold, a cut-off, a weight, or a range. Use only the figures in the reference file, and name the source.
- Never show a composite without its sub-scores and raw values.
- Recommend a repeat measurement or a talk with the athlete before anyone acts on a single flag.
- Call the composite a weighted mean of z-scores, not a z-score. Its spread depends on the number and correlation of inputs, so a cut-off on the composite is not comparable with the same cut-off on one z-score.
- Do not rescale the composite to a 0 to 100 "readiness percentage". It is not a percentage or a probability.
- Offer neutral colors or arrows before red, amber, and green. Red, amber, and green read as stop, caution, and go.
- If the user wants colors, tie each one to the user's own distance-from-baseline cut-off, and add this legend: "Colors show distance from this athlete's baseline. Not a training or clearance decision."
- Do not rely on red and green alone. About 8% of men of European descent have red-green color deficiency (Birch, 2012). Add a symbol or text label to each color.
- For a rehab athlete, state which baseline you used: pre-injury or post-injury. Do not compare the two without saying so.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If the `load-and-wellness` or `ams-data-setup` skill is installed, you may use its methods and table layout. This skill works without them.

## References

Load these files when needed:

- [references/readiness-composites.md](references/readiness-composites.md): how composites are built, why sub-scores and raw values must stay visible, why load stays out by default, rehab rules, and why a composite is decision support only
