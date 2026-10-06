---
name: ams-dashboards
description: "Build your own AMS screens in Power BI or Tableau: squad board, athlete profile, load, wellness, testing, availability, check-in forms, athlete-only views, and leaving a paid AMS."
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# Build AMS dashboards in Power BI and Tableau

This skill helps you build the screens of an athlete management system (AMS) yourself, in Power BI or Tableau, from your own data. It covers the screens most commercial products offer, the athlete check-in forms that feed them, the athlete-only view, and the move away from a commercial product.

## When to use

Use this skill when the user asks to:

- Build a squad readiness board, athlete profile, load, wellness, testing, availability, or data health dashboard.
- Rebuild a screen from a commercial AMS in Power BI or Tableau.
- Set up a morning wellness form or a session RPE form that feeds a dashboard.
- Show athletes only their own data.
- Publish, share, or refresh an AMS dashboard.
- Replace a commercial AMS, or use one alongside their own dashboards.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| The eight core screens, what each shows, and the tables they read | [references/core-screens.md](references/core-screens.md) |
| Building the screens in Power BI, row-level security, publishing, and refresh | [references/power-bi-build.md](references/power-bi-build.md) |
| Building the screens in Tableau, user filters, publishing, and refresh | [references/tableau-build.md](references/tableau-build.md) |
| Morning wellness and session RPE forms, and turning responses into rows | [references/athlete-forms.md](references/athlete-forms.md) |
| Moving off a commercial AMS: what to build, what to keep, and the data export | [references/replace-a-commercial-ams.md](references/replace-a-commercial-ams.md) |

## Steps

When the user asks about one topic, load only that reference file. When the user asks to build a set of screens, follow these steps in order:

1. Ask which decisions the screens support, who reads each one, and by when. Do not start from the list of devices.
2. Ask which tool the user has: Power BI, Tableau, or neither yet.
3. Ask which licenses the organization holds.
4. If the user has neither tool, do not choose one for them. Tell them to ask IT which tool the organization licenses and approves for athlete data.
5. Ask how the data is laid out. If it is not in athlete, session, and measure tables, use the `ams-data-setup` skill if it is installed, or ask the user to share the column names.
6. Load [references/core-screens.md](references/core-screens.md). Pick only the screens the decisions need.
7. Confirm where each metric is calculated. Calculate every metric once, in the metric layer, before the dashboard. Use the metric skills in this repository for each formula.
8. Load [references/power-bi-build.md](references/power-bi-build.md) or [references/tableau-build.md](references/tableau-build.md) for the user's tool.
9. Build one screen at a time, starting with the data health screen, then the screen for the most urgent decision.
10. If athletes will see the dashboard, set up row-level security before anyone shares it.
11. Sign in as a test athlete, and confirm the athlete sees only their own rows.
12. If the user needs a check-in form, load [references/athlete-forms.md](references/athlete-forms.md).
13. If the user is leaving a commercial AMS, load [references/replace-a-commercial-ams.md](references/replace-a-commercial-ams.md).
14. Show the user how to check each screen against the metric layer files before staff use it.

## Checks before answering

Run these checks on your own design before you show it:

- Confirm each screen supports a named decision and has a named reader.
- Confirm no metric is calculated in two places, such as in Python and again in DAX.
- Confirm missing data shows as missing, not as 0 and not as a hidden row.
- Confirm every color has a word or a number beside it, and that red and green are not the only cue.
- Confirm the ACWR sentence sits directly under each ACWR table or chart, and in the same paragraph as each ACWR value in text: "ACWR describes how recent load compares with longer-term load. It does not predict injury."
- Confirm any review value, such as a wellness z-score at which staff look closer, comes from the user and is shown on the screen.
- Confirm athlete views use row-level security, not a filter the athlete can clear.
- Confirm no screen that coaches read shows a diagnosis.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every screen as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not build an injury risk score or a readiness score that hides its parts. Show the parts.
- Do not invent a threshold. Use only the figures in the reference files of this repository, or values the user sets.
- Do not quote license prices or plan limits from memory. Tell the user to check the vendor's own pricing page.
- Never publish athlete data to a public gallery or a public web link. Tableau Public and Power BI **Publish to web** make data public.
- Do not move medical records into a dashboard tool. Keep them in a product approved for medical records.
- Do not ask for passwords, API keys, or tokens. If the user pastes one, do not repeat it. Tell them to revoke it and create a new one.
- Do not give legal advice. Do not say that a tool or setup complies with FERPA, HIPAA, GDPR, or any other law. Tell the user to take the question to their compliance, legal, or IT staff.
- Treat athlete data as sensitive. Tell the user to check the organization's data policy before they paste it into a cloud AI tool.
- Wellness answers can raise a welfare concern. Do not interpret one. Tell the user to follow the organization's referral process.

## References

Load these files when needed:

- [references/core-screens.md](references/core-screens.md): the eight core screens and the tables they read.
- [references/power-bi-build.md](references/power-bi-build.md): Power BI model, pages, row-level security, publishing, and refresh.
- [references/tableau-build.md](references/tableau-build.md): Tableau data source, dashboards, user filters, publishing, and refresh.
- [references/athlete-forms.md](references/athlete-forms.md): wellness and session RPE forms, and the import into the measures table.
- [references/replace-a-commercial-ams.md](references/replace-a-commercial-ams.md): build, keep, or drop each feature, the data export, and the side-by-side run.

The `ams-data-setup` skill covers the athlete, session, and measure tables. The `ams-architecture` skill covers hosting, intake, access, and backups. The `coach-reports` skill covers the change-versus-noise states. Do not rely on them being installed.
