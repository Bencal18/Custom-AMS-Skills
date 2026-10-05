# Traffic-light flags and their risks

Last checked: 2026-10-02

## What it covers

A traffic-light flag colors an athlete red, amber, or green to show a status such as readiness or load. This file explains the risks of that design and gives a safer way to build one when the user wants it.

## Method

Robertson and colleagues (2017) describe the traffic-light system as a common form of decision support in team sport. They report that there is no standard way to turn data into colors. Each team builds its own rules.

Ask the user first whether they need colors. A table with the change, the noise band, and a plain label often serves the reader better. If the user wants colors, follow these steps:

1. Write, in plain words, what each color means. Define it as a rule on the athlete's own data, for example `amber: change from own baseline is beyond the noise band, but the change minus the band is not beyond the smallest worthwhile change`.
2. Base the rule on the athlete's own baseline, the typical error, and the smallest worthwhile change. See the change-versus-noise reference. Do not set one fixed cut point for all athletes yourself. If the user gives fixed cut points with no source, say so, explain that values near a cut point can change color from measurement error alone, and offer the noise-band rule. If the user keeps them, label them as the user's choice, with no source.
3. Add a grey state for `no data`. Do not show missing data as green.
4. Put a text label and the raw value beside every color.
5. Show every sub-score behind a combined color. Do not show only the one color.
6. Show how many athletes are in each color, and how many you expect by chance.
7. Tell the user what the colors do not mean. They are not a diagnosis, an injury forecast, or a clearance.

### Know the risks

These are the main risks of a traffic-light flag:

- **Cut points are arbitrary.** A color needs a cut point. A cut point turns a continuous number into two or three groups. Dichotomizing a continuous variable loses information, hides variation within each group, and often has no scientific basis for where the line sits (Altman and Royston, 2006). The same logic applies to three colors. Two athletes on either side of a line look different and are almost the same.
- **Noise makes colors flip.** A value near a cut point will cross it from measurement error alone. A color that flips from week to week looks like a real change but is noise.
- **Colors hide sub-scores.** A combined color can stay green while one part falls and another rises. The reader sees one color and cannot tell which part moved.
- **Red can read as a prediction.** A red flag looks like a forecast of injury or a rule to rest. No screening test for sports injury has been shown to have adequate test properties to predict injury (Bahr, 2016). The ratio of acute to chronic load, often used for colors, has no evidence to support its use in managing load to reduce injury (Impellizzeri et al., 2020).
- **Fixed cut points ignore individuals.** One cut point for the whole squad judges each athlete by the group's range, not their own.
- **Color alone excludes some readers.** About 8 percent of men of European origin have red-green color deficiency (Birch, 2012).
- **Missing data looks fine.** An athlete with no data may show as green or blank.
- **Many colors, many false alarms.** With many athletes and measures, some results flag by chance. See the change-versus-noise reference.
- **Athletes may react to the color.** An athlete who sees red may worry, hide a symptom, or change how they answer a wellness form. In interviews at one national sporting institute, half of 8 athletes admitted withholding the truth on self-report forms at times, from fear of looking unprofessional or unmotivated. Some withheld information over concern about who could see their data (Saw et al., 2015). No study has tested the effect of the colors themselves.

### Use a safer design

Use these design choices when the user asks for colors:

- Use three states for change: `within measurement error`, `larger than measurement error; may or may not be worthwhile`, and `larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation`. Add `no data`. See the change-versus-noise reference for the rules. Without a typical error, use only the two usual-variation states, `within usual variation` and `outside usual variation`, from the flagging-change reference.
- Use a palette that readers with red-green color deficiency can tell apart, or shapes, not red and green. Blue and orange are both in the Okabe and Ito color set, chosen to stay distinct for colorblind readers (Okabe and Ito, 2008). Using them for these states is a design choice, not a tested result. Always add a label, because color must not be the only visual means of conveying information (W3C, 2024).
- Show the number, the unit, and the baseline beside the color.
- Keep the colors for coaches and staff. Show athletes no status colors by default. Show each athlete one neutral trend line of their own values, with the usual range shaded, and say in plain words where the latest value sits. Keep `worth a conversation` when a change needs one. Add status colors for athletes only if the user asks, with a plain label on each. See the audience reference.
- Do not combine several measures into one color unless the user defines the rule, and show the parts beside it.

Robertson and colleagues (2017) describe the analysis approaches and the way to visualize and communicate results in a traffic-light system. Use that paper as a starting point if the user wants a full design.

## Common mistakes

These are the mistakes AI tools make most often with traffic lights:

- Picking cut points such as `10 percent drop is red` with no source
- Using one set of cut points for every athlete and every measure
- Making a color from a z-score cut point and calling it a risk level
- Coloring a missing value green, or leaving it blank
- Combining wellness, load, and jump scores into one color, and hiding the parts
- Using red and green with no label
- Writing `at risk`, `high risk`, or `cleared` next to a color
- Not telling the user how many flags to expect by chance
- Showing status colors to athletes by default. Show a neutral trend line, a shaded usual range, and plain words instead.

## Example request

> Build me a red, amber, green sheet for the squad from the wellness scores and the jump tests.

## Check the result

Run these checks on the color rules:

- Read the rule for each color. Confirm it uses each athlete's own baseline and the noise band, and that the top color needs the change minus the band to pass the smallest worthwhile change.
- Find an athlete with no data. Confirm that athlete shows grey with a `no data` label.
- Check that every color has a text label, the raw value, and the sub-scores beside it.
- Read the athlete version. Confirm it shows no status colors unless the user asked for them.

## Sources

These sources support the rules in this file:

- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. *International Journal of Sports Physiology and Performance*. 2017;12(Suppl 2):S2-73-S2-79. doi:10.1123/ijspp.2016-0541. States that traffic-light systems are common in team sport and lack standardization in how they are put into practice.
- Altman DG, Royston P. The cost of dichotomising continuous variables. *BMJ*. 2006;332(7549):1080. doi:10.1136/bmj.332.7549.1080. Explains that dichotomizing a continuous variable loses information and power, and that cut points often have no scientific basis.
- Bahr R. Why screening tests to predict injury do not work, and probably never will: a critical review. *British Journal of Sports Medicine*. 2016;50(13):776-780. doi:10.1136/bjsports-2016-096256. Found no example of a screening test for sports injuries with adequate test properties.
- Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:chronic workload ratio: conceptual issues and fundamental pitfalls. *International Journal of Sports Physiology and Performance*. 2020;15(6):907-913. doi:10.1123/ijspp.2019-0864. Concludes there is no evidence to support use of the ratio in training load management or for recommendations to reduce injury risk.
- Birch J. Worldwide prevalence of red-green color deficiency. *Journal of the Optical Society of America A*. 2012;29(3):313-320. doi:10.1364/JOSAA.29.000313. Reports a prevalence of about 8 percent in men and about 0.4 percent in women of European Caucasian origin.
- Okabe M, Ito K. Color Universal Design (CUD): how to make figures and presentations that are friendly to colorblind people. 2002, revised 2008. https://jfly.uni-koeln.de/color/. Accessed 2026-10-02. Advises against combining red and green, recommends adding shapes, positions, and line types to color, and proposes a color set, including orange and blue, that stays distinct for colorblind readers.
- W3C. Web Content Accessibility Guidelines (WCAG) 2.2. W3C Recommendation, 2024-12-12. https://www.w3.org/TR/WCAG22/. Accessed 2026-10-02. Success criterion 1.4.1, Use of Color, requires that color is not the only visual means of conveying information.
- Saw AE, Main LC, Gastin PB. Monitoring athletes through self-report: factors influencing implementation. *Journal of Sports Science and Medicine*. 2015;14(1):137-146. https://pmc.ncbi.nlm.nih.gov/articles/PMC4306765/. Accessed 2026-10-02. Interviewed 8 athletes, 7 coaches, and 15 staff. Reports that half the athletes admitted withholding the truth at times, and that athletes withheld information over concern about who had access to their data.
