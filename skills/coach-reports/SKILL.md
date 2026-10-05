---
name: coach-reports
description: Build reports and dashboards from athlete data for coaches and athletes. Covers what each audience needs, flagging real change without noise, chart choices, and traffic-light risks.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Coach and athlete reports

This skill helps you turn athlete monitoring data into reports, dashboards, and charts that a coach or an athlete can read in under a minute and act on. It keeps the report honest about noise, missing data, and what the data cannot say.

## When to use

Use this skill when the user asks to:

- Build a weekly report, dashboard, or summary for coaches, staff, or athletes.
- Flag athletes whose numbers changed, or set up traffic-light or red, amber, green flags.
- Choose a chart for athlete data, or fix a chart that is hard to read.
- Show a readiness, wellness, or composite score.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| What to show coaches and what to show athletes | [`references/audience.md`](references/audience.md) |
| Flagging change from an individual baseline, with typical error and smallest worthwhile change | [`references/flagging-change.md`](references/flagging-change.md) |
| Chart choices | [`references/charts.md`](references/charts.md) |
| Traffic-light flags and their risks | [`references/traffic-lights.md`](references/traffic-lights.md) |

## Steps

Follow these steps in order:

1. Ask the user for the report details:
   - Who reads the report (coach, athlete, or both).
   - What decision the report supports.
   - How often the report goes out.
   - Which measures the report holds.
   - Which device or form the data comes from.
   - A sample export.

   Do not guess column meanings or units.
2. Prepare one version for each audience:
   - Load [`references/audience.md`](references/audience.md).
   - Make one version for each audience.
   - Do not send the coach view to athletes.
3. Get the typical error:
   - Ask for the typical error from a short-term retest in which no true change is expected, with the same summary as the values compared.
   - If the user has none, tell them how to get it.
   - Without it, describe changes, but do not give the flag states from step 4. Tell the user that without a typical error no change can be called beyond measurement error. This holds when the user gives cut points: show what their cut points do, labeled as the user's choice with their source, or with no source if they gave none, and offer the noise-band rule from step 4.
   - Without it, offer the usual-variation band from [`references/flagging-change.md`](references/flagging-change.md) when the athlete has at least 10 stable baseline values: `baseline mean ± t(n - 1) x baseline SD x sqrt(1 + 1/n)`. Give two states only, `Within usual variation` or `Outside usual variation`. Never call this band measurement error.
4. Flag change beyond the noise:
   - Load [`references/flagging-change.md`](references/flagging-change.md).
   - Compare each athlete to that athlete's own baseline.
   - Flag only changes beyond the noise band, `1.96 x TE x sqrt(1 + 1/n)`, where TE is the typical error and `n` is the number of values in the baseline mean.
   - Say the band adds the variance of the new value to the variance of the baseline mean, as Hopkins (2017) does, and that the 95 percent level is a choice.
   - List the assumptions beside the band.
5. Give the top flag state only when the change minus the noise band is beyond the smallest worthwhile change in the chosen direction. Otherwise, say the change is larger than measurement error and may or may not be worthwhile.
6. Choose the charts:
   - Load [`references/charts.md`](references/charts.md).
   - Choose each chart from the question it answers.
   - Shade the same noise band that the flags use.
7. If the user asks for traffic lights or uses them, set the color rules:
   - Load [`references/traffic-lights.md`](references/traffic-lights.md).
   - Write the rule for each color before you use it.
8. Keep every sub-score visible. If you show a composite score, show its parts beside it, and show the formula.
9. Show the number of athletes with data out of the number expected, and the date of the last value, on every table and chart.
10. Show the formula, the variant name, and the units next to each result.

## Core rules

Apply these rules to every report:

- Compare an athlete to that athlete's own baseline before you compare to the squad.
- Show a change only with its typical error and the smallest worthwhile change next to it.
- Show missing data as missing. Never show it as zero, green, or normal.
- Use plain words. Write `below her usual range`, not `negative z-score`.
- Put the raw value and its unit beside every flag, score, and color.
- Use a label as well as a color. Do not rely on color alone.
- Keep the report short. Put the athletes who need a conversation at the top.
- Write what the data shows, and stop there. Do not write a cause, a diagnosis, or a plan.

## Checks before answering

Run these checks on your own result before you show it:

- Confirm each flag has a stated rule, and the rule uses the athlete's own baseline.
- Confirm each flagged change is beyond the noise band, or is labeled as not larger.
- Confirm each listed athlete has the raw value, baseline, unit, typical error, and noise band beside it, plus the smallest worthwhile change when one is set.
- Confirm the top flag state appears only when the change minus the noise band is beyond the smallest worthwhile change.
- Confirm each chart band uses the same formula and `n` as the flags.
- Confirm the band text says it adds the variance of the new value to the variance of the baseline mean, as Hopkins (2017) does, says 95 percent is a choice, and lists the assumptions.
- Confirm the number of athletes in the report matches the roster, and missing athletes are listed.
- Confirm every chart has labeled axes with units, the same scale where charts are compared, and a bar chart that starts at zero.
- Confirm sub-scores are visible next to every composite score.
- Confirm no text diagnoses, predicts injury, or says an athlete is cleared, ready, or should rest.
- Confirm the athlete version shows only that athlete's data.
- Count how many changes beyond the noise band to expect by chance. With all assumptions met, about 5 percent of unchanged results fall beyond a 95 percent band in both directions, and 2.5 percent in one direction. The real rate can be higher or lower when assumptions fail.
- Report the expected count next to the number found.
- Recommend a repeat test before anyone acts on a single flag.
- If far more flag, check the typical error and the assumptions. Ask whether the whole squad changed, for example after a block of matches.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not label an athlete as `at risk`, `injured`, `fatigued`, `cleared`, or `ready`. Describe the data.
- Do not invent a threshold, cut point, or range. Use the user's own data or a cited source, and name it.
- Do not set a color cut point because it looks reasonable. Ask the user, and show them what the rule does on their data: the count in each color, and each athlete the rule has no state for, such as one with a missing value. If the user gives cut points with no source, say they have no source and that values near a cut point can change color from measurement error alone. Ask for the source and the typical error, and offer the noise-band rule from step 4. If the user keeps the cut points, label them as the user's choice, with no source.
- Do not show one athlete's data to another athlete or to anyone the user has not named.
- Athlete data is personal health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If mood, stress, or free-text items suggest a mental-health or welfare concern, do not interpret them or put them in a report. Tell the user to follow their organization's referral process and involve appropriate staff.
- If any athletes are minors, remind the user to check the consent rules and the rules on parent or guardian access to the data and the reports.

## References

Load these files when needed:

- [`references/audience.md`](references/audience.md): What to show coaches and athletes
- [`references/flagging-change.md`](references/flagging-change.md): Flagging change with individual baselines, typical error, and smallest worthwhile change
- [`references/charts.md`](references/charts.md): Chart choices for athlete data
- [`references/traffic-lights.md`](references/traffic-lights.md): Traffic-light flags, their risks, and a safer design
