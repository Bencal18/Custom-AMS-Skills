# Replace a commercial AMS with your own dashboards

Last checked: 2026-10-05

## What it covers

This file shows how to move from a commercial athlete management system (AMS) to dashboards you build, or to a mix of both. It covers which features you can rebuild, which to keep in an approved product, how to get your data out, and how to run both systems side by side before you switch.

Decide first whether to buy, build, or combine both. The buy-or-build reference in the `ams-architecture` skill covers that decision.

## Method

### List what the current product does for you

Write one row for each feature your staff use, not each feature the product offers. Add these columns: the feature, who uses it, how often, and the decision it supports. Features nobody uses do not need a replacement.

### Sort each feature into build, keep, or drop

Most commercial products bundle features that differ in how hard they are to rebuild safely:

| Feature | Rebuild with your own dashboards | Why |
|---|---|---|
| Squad board, athlete profile, load, wellness, testing, availability, and data health screens | Yes | They read tables you already have. See [core-screens.md](core-screens.md). |
| Metric calculations, such as z-scores, rolling loads, and change states | Yes | You control and can check every formula. See the metric skills in this repository. |
| Wellness and session RPE forms | Yes, with an approved form tool | See [athlete-forms.md](athlete-forms.md). Identify athletes by sign-in, not a typed name. |
| Device data intake | Yes, if each vendor gives you an export or an API | See the data intake reference in the `ams-architecture` skill. A vendor that changes its export breaks your import, and you fix it, not the AMS vendor. |
| Athlete view of their own data | Yes, with row-level security | See [power-bi-build.md](power-bi-build.md) and [tableau-build.md](tableau-build.md). |
| Medical records, treatment notes, and injury records | Keep in a product approved for medical records | Medical records often carry rules on access, access logs, and retention. Ask your medical and compliance staff which rules apply. These features are hard to build and maintain yourself. |
| Athlete phone app with push reminders | Keep, or accept a web form and email reminders | A native app needs developers, app store accounts, and updates. |
| Calendar, messaging, and file sharing | Use the tools your organization already approves | Email, calendar, and chat tools often cover these. |
| Strength programming | Keep, or use a programming product | It is a separate product category. |

If you keep a product for some features, confirm that it lets you export all your data, in an open format, on a schedule. Then build your dashboards on that export.

### Get all your data out

Do this before the contract ends:

1. Ask the vendor in writing for a full export of every form, test, and record, in CSV or another open format, with the field definitions.
2. Ask how the product calculated each derived metric, such as a readiness score or a load ratio, so you can match or replace it.
3. Ask how long the vendor keeps your data after the contract ends, and how it confirms deletion.
4. Check the export: count the athletes, the forms, and the rows by month, and compare them with what the product shows.
5. Store the export in the raw layer of your new system, unchanged.
6. Map each export field to the athlete, session, and measure tables. See the `ams-data-setup` skill.

Medical records may have their own rules on transfer and retention. Ask your medical and compliance staff before you move them.

A new question wording or scale starts a new wellness baseline. Mark the switch date, and do not score new answers against the old product's baseline. See the wellness z-score reference in the `load-and-wellness` skill.

### Rebuild the metrics, then check them

Calculate each metric once, in your metric layer. Then compare your numbers with the old product for the same athletes and dates. Expect differences. Products use different windows, trial summaries, and baselines. For each difference, find the reason, and write it in the measure dictionary. Do not change your formula only to match the old number.

### Run both systems side by side

Run your dashboards next to the old product for at least two weeks, or one full training week, whichever is longer, before you switch:

- Use the same data in both.
- Ask the staff who make each decision whether the new screen gave them what they needed, on time.
- Fix what failed. Then switch one decision at a time.

### Plan the people, not just the files

A build depends on the staff who run it. Before you cancel the old product, confirm these points:

- A named person runs the system each week, and a second person can cover.
- The handover document exists, and the second person has used it for a full week. See the backups and handover reference in the `ams-architecture` skill.
- Every account, flow, and key belongs to the organization, not to a person.

### Compare the real cost

Compare the license fee with the staff hours the build takes each week, over the same period, such as three years. A build has no license fee but costs staff time every week. See the buy-or-build reference in the `ams-architecture` skill.

Dashboard tools have their own license costs. Sharing reports with staff and athletes can need a paid license for each viewer, or a capacity license. Check the vendor's own pricing page. Do not rely on a price from memory or from an AI tool.

## Common mistakes

These are the mistakes staff and AI tools make most often when they leave a commercial AMS:

- Cancelling before a full export has been checked.
- Rebuilding every screen the old product had, including screens nobody used.
- Moving medical records into a spreadsheet or a dashboard tool that is not approved for them.
- Copying the old product's readiness score or color bands without knowing the formula.
- Changing your formula to match an old number you cannot explain.
- Switching every decision on the same day.
- Leaving the build with one person who has no cover.
- Forgetting the license cost of sharing dashboards with every coach and athlete.

## Example request

> Our AMS contract ends in June. We use it for the morning wellness form, the squad readiness board, and jump testing. The athletic trainers use its medical records. Help me plan what to build and what to keep.

## Check the result

Run these checks on the plan:

- Confirm every feature the staff use has a row, and each row is build, keep, or drop.
- Confirm medical records stay in a product approved for them.
- Confirm the plan includes a checked full export before the contract ends.
- Confirm the plan includes a side-by-side run and a switch date for each decision.
- Confirm a named person and a second person run the build.
- Confirm the plan names no product as the best.

## Sources

These sources support the method in this file:

- Torres-Ronda L, Schelling X. Critical process for the implementation of technology in sport organizations. *Strength and Conditioning Journal*. 2017;39(6):54-59. doi:10.1519/SSC.0000000000000339. Offers a guideline for vetting and implementing technology in sport organizations. Read in abstract form only.
- Schelling X, Robertson S. A development framework for decision support systems in high-performance sport. *International Journal of Computer Science in Sport*. 2020;19(1):1-23. doi:10.2478/ijcss-2020-0001. Includes feasibility, with legal checks, and system complexity in its framework.

The feature table, the export steps, and the side-by-side run are practical guidance from the authors of this repository. The feature list comes from public product pages read on 2026-10-05.
