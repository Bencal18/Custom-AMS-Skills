---
name: ams-architecture
description: Plan a whole athlete management system (AMS): spreadsheet or database, hosting, automatic device imports, who sees what, backups, handover, and buy vs build. Not table layouts.
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
  last-tested: "not tested"
---

# Plan an athlete management system

This skill helps you plan a whole home-built athlete management system (AMS). It covers where data comes in, where it is stored, where calculations run, who sees what, and how the system survives staff changes. For the tables inside the system, use the `ams-data-setup` skill if it is installed.

## When to use

Use this skill when the user asks to:

- Build, plan, or rebuild an athlete management system, athlete database, or monitoring dashboard.
- Choose between spreadsheets, low-code tools, and a database for athlete data.
- Host an AMS, share it with staff, or decide where athlete data can live.
- Pull device data automatically from a vendor API or a shared folder.
- Set up access for coaches, athletic trainers, medical staff, and athletes.
- Back up an AMS, or hand it over to new staff.
- Decide whether to buy a commercial AMS or build one.

This skill covers these topics:

| Topic | Reference file |
|---|---|
| The parts of an AMS, and starting from the decisions it supports | [references/parts-of-an-ams.md](references/parts-of-an-ams.md) |
| Spreadsheet, low-code, and database setups, and where to host each | [references/choose-a-setup.md](references/choose-a-setup.md) |
| Raw, clean, metric, and report layers; folders; the import log | [references/system-layout.md](references/system-layout.md) |
| Manual exports, shared folders, vendor APIs, forms, and API keys | [references/data-intake.md](references/data-intake.md) |
| Roles, access, privacy questions, consent, and retention | [references/access-and-privacy.md](references/access-and-privacy.md) |
| Backups, restore tests, and the handover document | [references/backups-and-handover.md](references/backups-and-handover.md) |
| Buying a commercial AMS, building one, or combining both | [references/buy-or-build.md](references/buy-or-build.md) |

## Steps

When the user asks about one topic, such as access or handover, load only that reference file and ask only the questions it needs. When the user asks to plan a whole system, follow these steps in order:

1. Load [references/parts-of-an-ams.md](references/parts-of-an-ams.md).
2. Ask which decisions the system must support, who makes each one, and when. Do not start from the list of devices.
3. Ask for the data sources, the number of athletes and teams, and how often each source produces data.
4. Ask who will maintain the system, which tools they can use, and how many hours a week they have for it.
5. Ask which tools the organization already licenses, the budget, and what its IT and compliance rules say about athlete data.
6. Ask whether any athletes are minors, and whether medical or injury data will be in the system.
7. If the user has budget for a commercial product, or no staff time to maintain a build, load [references/buy-or-build.md](references/buy-or-build.md), and help the user decide before you choose a setup.
8. If the user builds the system, or builds on top of a commercial product, load [references/choose-a-setup.md](references/choose-a-setup.md).
9. Recommend the simplest setup that meets the decision deadlines and that the staff can maintain. State its weekly maintenance work.
10. Load [references/system-layout.md](references/system-layout.md).
11. Lay out the raw, clean, metric, and report layers, and the folders or database schemas that hold them.
12. Load [references/data-intake.md](references/data-intake.md).
13. Write the intake plan: one row for each source, with its method, schedule, owner, and failure alert.
14. Load [references/access-and-privacy.md](references/access-and-privacy.md).
15. Write the access table: one row for each role, with what the role can see and change.
16. List the privacy questions the user must take to their compliance, legal, or IT staff.
17. Load [references/backups-and-handover.md](references/backups-and-handover.md).
18. Write the backup plan and the outline of the handover document.
19. Recommend a trial run of two weeks with one decision and one source before the full build.
20. Present the plan in this order: the decisions, the setup and why, the layers, the intake plan, the access table, the backup plan, the trial run, and the open questions.

## Core rules

Apply these rules to every plan:

- Start from the decisions the system supports, not from the data you can collect.
- Choose the simplest setup the staff can maintain. A system that only its builder can fix stops working when the builder leaves.
- Host inside accounts the organization owns and manages. Do not host athlete data in a personal account.
- Keep raw data unchanged, in its own layer. Rebuild every other layer from it.
- Calculate each metric in one place. Reports show metrics. They do not calculate them.
- Store passwords, API keys, and tokens only in a password manager, a secrets store, or the secure connection settings of a flow tool, that the organization approves. Never put them in a spreadsheet, a script, a shared folder, or a chat with an AI tool.
- Give each person the least access their role needs.
- Count a backup as working only after you restore from it.
- Name products only as examples, with the date you checked them. Do not endorse a product, and do not present any list of products as complete.
- If the organization has no IT or compliance staff, ask who is accountable for athlete data, such as the athletic director, the head of school, or the club owner. Tell the user to read the data terms of each tool before they use it.

## Checks before answering

Run these checks on your own plan before you show it:

- Confirm each decision has a deadline, and the intake schedule delivers the data before it.
- Confirm each source has an intake method, an owner, a schedule, and a failure alert.
- Confirm each metric has exactly one place where it is calculated.
- Confirm no step edits or overwrites the raw layer.
- Confirm the access table covers every role, and athletes see only their own data.
- Confirm the plan names every place a copy of the data lives, including backups, exports, and report files.
- Confirm a second person could run the system from the handover document.
- Confirm the plan says which items the organization's IT or compliance staff must approve.

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not give legal advice. Do not say that a tool or setup complies with FERPA, HIPAA, GDPR, or any other law. List the questions, and tell the user to take them to their compliance, legal, or IT staff.
- Do not ask for passwords, API keys, or tokens. If the user pastes one into the chat, do not repeat it in your reply. Tell them to revoke it and create a new one.
- Do not recommend a tool the organization has not approved for athlete data. Tell the user to ask their IT staff first.
- Do not quote prices, free plan limits, or plan features from memory. Tell the user to check the vendor's own page.
- Before you write a custom web application, explain what it needs to stay safe: hosting, sign-in, security updates, and a person to maintain it.
- Treat athlete data as sensitive. Much of it can count as health data. Tell the user to check their organization's data policy before they paste it into a cloud AI tool.
- If any athletes are minors, remind the user to check the consent rules and the rules on parent or guardian access to the data.
- Wellness forms can hold mood, stress, or free-text answers. If an answer suggests a mental-health or welfare concern, do not interpret it. Tell the user to follow their organization's referral process and involve appropriate staff.

## References

Load these files when needed:

- [references/parts-of-an-ams.md](references/parts-of-an-ams.md): the parts of an AMS, and the decision list that drives the design.
- [references/choose-a-setup.md](references/choose-a-setup.md): spreadsheet, low-code, and database setups, sizing, and hosting.
- [references/system-layout.md](references/system-layout.md): the raw, clean, metric, and report layers, folder and schema layouts, and the import log.
- [references/data-intake.md](references/data-intake.md): manual exports, shared folders, vendor APIs, forms, API keys, and checks on arrival.
- [references/access-and-privacy.md](references/access-and-privacy.md): the data inventory, roles and access, privacy questions, consent, and retention.
- [references/backups-and-handover.md](references/backups-and-handover.md): backups, restore tests, account ownership, and the handover document.
- [references/buy-or-build.md](references/buy-or-build.md): when to buy, when to build, the questions to ask a vendor, and the exit plan.

The `ams-data-setup` skill covers the athlete, session, and measure tables. Do not rely on it being installed. If it is not, ask the user how their tables are laid out.
