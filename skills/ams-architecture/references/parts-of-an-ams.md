# Parts of an athlete management system

Last checked: 2026-10-05

## What it covers

This file names the parts every athlete management system (AMS) has, shows how data moves between them, and explains how to start the design from the decisions the system supports.

## Method

### Start from the decisions

An AMS exists to help staff make decisions. Robertson and colleagues (2017) describe decision support systems in sport as information systems that give objective evidence for an organization's decisions. They call for projects driven by a question. Schelling and Robertson (2020) put context first in their development framework: understand the setting and the people who will use the system before you build it.

Before you choose any tool, write a decision list. Use one row for each decision, with these columns:

- `decision`: what the staff decide, for example "adjust today's running volume for each player".
- `who`: the person who decides.
- `when`: the deadline, for example "06:45 on training days".
- `needs`: the metrics or flags the person must see.
- `freshness`: how old the data can be, for example "this morning's form" or "last session".
- `if_missing`: what the person does when data is missing, for example "use the coach's check-in".

Collect only the data that a row in the decision list needs. Add a source when a decision needs it, not because a device exports it.

The `when` and `freshness` columns drive the design. A decision at 06:45 on data from a 06:00 form needs automatic intake and calculation. A weekly review on Monday afternoon can run on manual exports.

### Know the parts

Every AMS has these parts, whether it is one workbook or a database:

| Part | Job | In a spreadsheet setup | In a database setup |
|---|---|---|---|
| Intake | Brings data in from devices, forms, and files | Staff export a file and paste or import it | A scheduled script pulls each vendor API |
| Storage | Holds the raw data and the cleaned tables | Sheets or files in a shared folder | Tables in a database |
| Calculation | Turns clean data into metrics | Formulas in a calculation sheet, or Power Query | SQL views, or a Python or R script |
| Reporting | Shows results to staff and athletes | A report sheet, Power BI, or Tableau | Power BI, Tableau, or a web dashboard |
| Access | Controls who can see and change what | Folder and file sharing | Database roles and report permissions |
| Backup | Keeps copies, and restores them | Version history plus a separate copy | Database backups plus a separate copy |
| Documentation | Lets someone else run and fix the system | A README sheet and a data dictionary | A README, a data dictionary, and code comments |

A missing part does not disappear. It becomes manual work for someone, or a risk nobody owns.

### Keep data moving in one direction

Data flows one way through the layers:

```text
sources -> raw -> clean -> metrics -> reports
```

Each layer reads only from the layer before it. Nobody types into the clean, metric, or report layers by hand. When a number is wrong, fix it at the source or with a recorded correction in the clean layer, then rebuild. See [system-layout.md](system-layout.md).

### Give each part an owner

Name one person who owns each source, each import, and each report. The owner checks that it ran and fixes it when it fails. Name a second person who can cover for the owner.

## Common mistakes

These are the mistakes AI tools and staff make most often when they plan an AMS:

- Starting from the devices and collecting every metric they export. The system grows, and no decision uses most of it.
- Building the dashboard first. The dashboard then fixes the data layout, and every new question needs a rebuild.
- Putting intake, storage, calculation, and reporting in one workbook tab. A change to a report then breaks a calculation.
- Calculating the same metric in two places, such as the workbook and Power BI. The two numbers drift apart.
- Planning no failure alert. A failed import shows as a quiet morning with no data, and staff read it as "no problems".
- Leaving every part to one person. When that person is away, nothing runs.

## Example request

> I'm the only sports scientist for three teams. We have force plates, GPS, and a morning wellness form. Help me plan an athlete management system.

## Check the result

Run these checks on the plan:

- Confirm every source in the plan serves at least one row in the decision list.
- Confirm every row in the decision list has a deadline, and the plan delivers its data before that deadline.
- Confirm every part in the table has a named tool, a named owner, and a named cover person.

## Sources

These sources support the method in this file:

- Robertson S, Bartlett JD, Gastin PB. Red, amber, or green? Athlete monitoring in team sport: the need for decision-support systems. *International Journal of Sports Physiology and Performance*. 2017;12(Suppl 2):S2-73-S2-79. doi:10.1123/ijspp.2016-0541. Defines decision support systems as information systems that give objective evidence for an organization's decisions. Names the time cost of collecting, cleaning, and reporting data, and calls for projects driven by a question.
- Schelling X, Robertson S. A development framework for decision support systems in high-performance sport. *International Journal of Computer Science in Sport*. 2020;19(1):1-23. doi:10.2478/ijcss-2020-0001. A framework to apply before, during, and after building a decision support system. It starts from the context and the users, and checks feasibility, data quality, and system complexity.

The decision list, the parts table, and the owner rule are practical guidance from the authors of this repository. No study tests them.
