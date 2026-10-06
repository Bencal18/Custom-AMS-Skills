# The core screens of an athlete management system

Last checked: 2026-10-05

## What it covers

This file lists the screens that most commercial athlete management systems (AMS) offer, and shows how to build each one yourself. For each screen it gives the decision the screen supports, who reads it, the data it needs, the layout, and the rules that keep it honest.

The screen list comes from a review of public product pages, help centers, and app store listings, read on 2026-10-05. It names no products. The layouts are design guidance from the authors of this repository, built on the other skills in this repository. They are not results from trials.

## Method

### Start from the decisions

Build a screen only when someone makes a decision with it. Write the decision, the reader, and the deadline at the top of the plan for each screen. A screen with no decision becomes a page nobody opens. See the decision list in the `ams-architecture` skill if it is installed.

### Know the eight core screens

Most products offer these screens under different names:

| Screen | Decision it supports | Main reader | When it is read |
|---|---|---|---|
| Squad board | Whom to talk to before today's session | Coach, sports scientist | Each training morning |
| Athlete profile | What has changed for one athlete, and since when | Sports scientist, coach | When an athlete is listed on the squad board |
| Load | Whether the week went as planned | Sports scientist | After each session and each week |
| Wellness and check-ins | Who answered, and whose answers moved from their usual | Sports scientist | Each training morning |
| Testing | Who changed beyond measurement error since baseline | Sports scientist, strength coach | After each test day |
| Availability | Who can train fully, modified, or not at all | Coach | Each training morning |
| Data health | Whether today's numbers are complete and current | The person who runs the AMS | Before anyone reads the other screens |
| My data | How the athlete's own numbers compare with their usual | Athlete | When the athlete chooses |

Commercial products also offer forms, a calendar, messaging, medical records, and a phone app. See [replace-a-commercial-ams.md](replace-a-commercial-ams.md) for which of those you can build and which you should keep in an approved product.

### Calculate in the metric layer, show in the report layer

Calculate every metric once, before the dashboard reads it. The dashboard filters, sorts, and draws. It does not calculate z-scores, rolling loads, or noise bands. This keeps one formula in one place, and lets you check every number against a file. The `ams-architecture` skill describes the layers.

Give the dashboard these tables:

| Table | One row for each | Main columns |
|---|---|---|
| `athletes` | Athlete | `athlete_id`, `name`, `group`, `email`, `start_date`, `end_date` |
| `dates` | Calendar day | `date`, `week_start` |
| `athlete_day` | Athlete and day on the roster | `athlete_id`, `date`, `availability`, `form_submitted`, `srpe_load_au`, `acute_load_au`, `chronic_load_au`, `wellness_total`, `wellness_total_z`, `wellness_status`, and the latest test value, change, and state |
| `wellness_scores` | Athlete, day, and item, plus the total | Answer, baseline count, baseline mean, change in points, z-score, status |
| `test_results` | Athlete and test day | Value, baseline mean and count, change, noise band, band edges, state, wording |
| `weekly_load` | Athlete and week | Weekly total, days complete, days out, days modified |
| `test_day_summary` | Test day | Results, results beyond the noise band in the chosen direction, and the number expected by chance |
| `reliability` | Tested measure | Typical error, its degrees of freedom, the band multiplier, and the smallest worthwhile change |
| `data_quality` | Day | Forms expected and received, ratings expected and received, device failures |
| `import_log` | Import | Source, date, time, rows, result |
| `profile_series` | Athlete, day, and chart line | `athlete_id`, `date`, `chart`, `series`, `value`, for tools that draw one value column |
| `settings` | Choice the staff make | `setting`, `value`, `meaning` |

Relate each athlete-level table to `athletes` on `athlete_id` and to `dates` on its date column, one to many, filtering in one direction. Relate `data_quality` to `dates` only. Leave `import_log` and `settings` unrelated.

### Build the squad board

Show one row for each athlete on the roster on the chosen date. Default the date to the latest day with data. Add these columns, in this order:

1. Athlete and group.
2. Availability: `full`, `modified`, or `out`.
3. Form submitted: `yes`, `no`, or `not expected`.
4. Wellness total, change in points from the athlete's baseline, the z-score, and its status, such as `baseline too short`.
5. Acute load and chronic load, with the ACWR only if the staff asked for it.
6. Latest test value, its date, the change from baseline, and the state in words.

Add these cards above the table:

- Athletes by availability, as counts.
- Forms received out of forms expected.
- Test results beyond the noise band, next to the number expected by chance.
- The date and time of the last successful import.

Follow these rules:

- Sort athletes by the change relative to the noise band in the direction the staff chose, such as a drop in jump height, largest first. Do not sort by a color or a combined score. See the `coach-reports` skill.
- Show missing data as missing. An athlete with no form today shows `no`, not a blank row and not a 0.
- Use the state wording from the change-versus-noise reference in the `coach-reports` skill: `Within measurement error`, `Larger than measurement error; may or may not be worthwhile`, `Larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation`, and `Not enough data`. Without a typical error, use `Within usual variation` and `Outside usual variation` instead.
- If you add color, use a color-blind-safe pair, such as blue and orange, and keep the words beside each color. See the traffic-light reference in the `coach-reports` skill.
- Put this sentence directly under each table or chart that shows ACWR: "ACWR describes how recent load compares with longer-term load. It does not predict injury." See the `load-and-wellness` skill.
- Show only availability, never a diagnosis, unless medical and compliance staff approved more.

### Build the athlete profile

Use a single-select athlete filter. Show these parts, with dates aligned on one axis where the tool allows:

- Daily load as columns, with acute and chronic load as lines. Show rest days as 0 and missing days as gaps.
- Wellness items as a grid of items by the last 28 days, with the raw answer in each cell.
- Test values as points joined by a line, with the baseline mean and the noise band edges as two flat lines.
- Availability as a strip of days.
- A table of test results with the state wording.

Follow these rules:

- Plot the athlete's own values against the athlete's own baseline. Do not plot the squad mean as the reference unless the reader asks.
- Use a categorical date axis or show items with no data, so a missing day stays a gap. A continuous axis joins points across missing days.
- Show `n` for every baseline.

### Build the load screen

Show these parts:

- Weekly load for each athlete as small multiples, or as a grid of athletes by weeks with the total and the days complete in each cell, such as `2,150 AU, 7 of 7 days`.
- Daily load for the squad, one line for each athlete in gray, with one athlete highlighted.
- The ACWR, only when the staff ask for it, with the variant, the windows, and the sentence that it does not predict injury.

Mark a week with any missing day as incomplete. Do not compare an incomplete week with a complete one. See the session RPE load reference in the `load-and-wellness` skill.

### Build the wellness and check-in screen

Show these parts:

- A grid of athletes by days, with the total wellness z-score as a diverging color and the raw total in each cell.
- Form completion by day, as forms received out of forms expected.
- A list of athletes at or below the review value the staff set, with each item's raw answer and change in points.

Follow these rules:

- Flag on the total z-score or on the staff's raw-answer rule, not on single-item z-scores. See the wellness z-score reference in the `load-and-wellness` skill.
- Do not set a review value for the staff. No published cut point exists. Store the value the staff choose in a settings table, and show it on the screen.
- Show the baseline window and the baseline count. A z-score from a baseline below the minimum count shows `baseline too short`.
- Show the number of athletes at or below the review value next to the number expected by chance. See the wellness z-score reference in the `load-and-wellness` skill.
- Recommend a repeat answer or a conversation with the athlete before anyone acts on a single flag.
- Wellness answers can raise a welfare concern. Do not interpret one. Follow the organization's referral process.

### Build the testing screen

Show these parts for the chosen test day:

- A sorted dot plot of each athlete's change from baseline, with the noise band as a bar around each dot, and the smallest worthwhile change as two vertical lines.
- The count of results beyond the noise band, next to the count expected by chance.
- A table with the value, the baseline mean and count, the change, the noise band, and the state wording.

Follow these rules:

- Use the typical error from the staff's own retest. Show its source and the number of athletes. See the `monitoring-statistics` skill.
- If the staff have no typical error, use the usual-variation band from the change-versus-noise reference, with only the states `Within usual variation`, `Outside usual variation`, and `Not enough data`. Never call that band measurement error.
- Do not show a ranked leaderboard of raw results by default. Ranking reads as judgment. See the squad views reference in the `athlete-data-visualization` skill.
- Recommend a repeat test before anyone acts on a single flag.

### Build the availability screen

Show the count of athletes who are full, modified, and out, for each day, as stacked columns. Add a table of athletes who are modified or out today, with the first day of the current status. Show no reason beyond the status unless medical and compliance staff approved it.

### Build the data health screen

Show these parts:

- The import log, with the newest import first, and every failed import highlighted.
- Form and rating completion by day.
- Device failure rows by day.
- The number of rows held for a duplicate question.

Check this screen before you read any other screen. A complete-looking squad board built on a failed import is wrong without an error message.

### Build the athlete's own view

Show only the signed-in athlete's data. Use these parts:

- One neutral trend line for each measure the staff chose, with the athlete's usual range shaded.
- The latest value, its unit, and one plain sentence, such as `Your jump height this week is within your usual range.`
- No teammates, no ranks, and no status colors by default.

Restrict the view with row-level security, not with a filter the athlete can clear. See [power-bi-build.md](power-bi-build.md) and [tableau-build.md](tableau-build.md). Test it by signing in as a test athlete.

## Common mistakes

These are the mistakes AI tools and staff make most often when they build AMS screens:

- Building a screen for every device instead of for every decision.
- Calculating z-scores, rolling loads, or bands inside the dashboard, then again in a second dashboard, with two answers.
- Showing a red, amber, and green color with no words, no number, and no baseline.
- Sorting the squad board by a combined readiness score that hides its parts.
- Hiding athletes with no data, so the squad looks complete.
- Showing a squad leaderboard to athletes.
- Using an athlete filter instead of row-level security for the athlete view.
- Putting diagnoses on a screen that coaches read.

## Example request

> I want my own version of the squad readiness screen our old AMS had. We have a morning wellness form, session RPE, GPS, and a weekly jump test. Build it in Power BI.

## Check the result

Run these checks on each screen before staff use it:

- Pick one athlete and one day. Find each number on the screen in the metric layer files. Confirm they match, including the unit.
- Confirm an athlete with no form today appears as `no`, not as a blank row or a 0.
- Confirm every color has a word or a number beside it.
- Confirm the ACWR sentence sits directly under each table or chart that shows ACWR.
- Confirm the data health screen shows the time of the last successful import.
- Sign in as a test athlete. Confirm the athlete sees only their own data.

## Sources

These sources support the method in this file:

- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. *International Journal of Sports Physiology and Performance*. 2017;12(Suppl 2):S2-73-S2-79. doi:10.1123/ijspp.2016-0541. Discusses the types and formats of data in monitoring systems, the analysis approaches, and the visualization and communication of results to stakeholders in team sport.
- Schelling X, Robertson S. A development framework for decision support systems in high-performance sport. *International Journal of Computer Science in Sport*. 2020;19(1):1-23. doi:10.2478/ijcss-2020-0001. Frames a monitoring system around the decisions it supports.

The screen list comes from public product pages, help centers, and app store listings read on 2026-10-05. The layouts and rules are practical guidance from the authors of this repository, and they follow the `coach-reports`, `load-and-wellness`, `monitoring-statistics`, and `athlete-data-visualization` skills.
