# Choose a setup and where to host it

Last checked: 2026-10-05

Product names in this file are examples, checked on the date above. Naming a product is not an endorsement. Check prices, plan limits, and features on the vendor's own page.

## What it covers

This file helps you choose between a spreadsheet, a low-code, and a database setup for a home-built AMS, estimate how much data the system will hold, and decide where to host it.

## Method

### Ask the questions that decide the setup

Answer these questions before you pick a tool:

- Who will maintain the system, and which tools do they already know?
- How many hours a week can they give to imports, fixes, and changes?
- How many athletes, teams, and sources are there, and how often does each source produce data?
- Which decisions have a same-day deadline? See the decision list in [parts-of-an-ams.md](parts-of-an-ams.md).
- How many people edit the data, and how many only view reports?
- Which tools does the organization already license and support, such as Microsoft 365 or Google Workspace?
- What do the organization's IT and compliance rules say about where athlete data can be stored?

The maintainer's skills and hours limit the setup more than the features do. Choose the simplest setup that meets the decision deadlines and that the staff can maintain.

### Compare the three setups

| | Spreadsheet | Low-code | Database |
|---|---|---|---|
| Example tools | Excel or Google Sheets, Microsoft Forms or Google Forms, Power BI or Looker Studio for reports | Microsoft Lists or Airtable for reference tables and forms, files in a shared folder for the measures, Power Automate for scheduled imports, Power BI for reports | PostgreSQL or SQL Server, Python or R scripts on a schedule, Power BI, Tableau, R Shiny, or Streamlit for reports |
| Skills needed | Formulas and pivot tables | Formulas, plus building automated flows | SQL, plus Python or R |
| Fits when | One or two staff, manual exports once a day or less, a few teams | Same-day deadlines, no one who codes, the organization uses the vendor's suite | Many sources, many athletes, sample-level data, a staff member who codes |
| Weekly maintenance | Manual exports and imports every day, checks for hand edits | Fixing flows that fail when a vendor changes an export or a password changes | Fixing scripts, applying security updates, managing accounts and backups |
| Main risk | Hand edits, broken formulas, and copies of the file that drift apart | Flows that run under one person's account and can fail when that person leaves | Only one person can fix it |
| Outgrow it when | Manual imports take more time than analysis, several people edit at once, or the file nears the app's size limit | Flows multiply and nobody can see what runs where, or data needs exceed the list tool | Staff time to maintain it exceeds the cost of a commercial product |

List tools, such as Microsoft Lists and Airtable, limit how many records a list or base holds. They suit reference tables and forms, not a large measures table. Compare the yearly row estimate with the tool's record limit on the vendor's own page.

Move up one setup at a time. A spreadsheet setup laid out in long tables, as the `ams-data-setup` skill describes, moves into a database with little rework.

### Estimate the size

Estimate the rows the measures table gains each year. Use one row for each athlete, date, measure, side, and trial:

```text
rows per year = athletes × measures per session × sides × trials × sessions per year
```

Use 1 for `sides` when a measure has no side, and 2 when you store left and right. Add the result for each source. For example, a program with 60 athletes might have:

- GPS: 60 athletes × 25 measures × 1 side × 1 trial × 200 sessions = 300,000 rows.
- Force plate: 60 athletes × 15 measures × 2 sides × 3 trials × 40 test days = 216,000 rows.
- Wellness: 60 athletes × 6 items × 1 side × 1 trial × 300 days = 108,000 rows.
- Total: 624,000 rows a year.

An Excel worksheet holds at most 1,048,576 rows, so this measures table fills one worksheet in under two years. A Google Sheets file holds up to 20 million cells. At 12 columns, 624,000 rows use about 7.5 million cells a year, so the file fills in under three years.

A spreadsheet setup can still work at this size. Use one of these options:

- Load the measures table with Power Query into the Excel Data Model or Power BI, not into a worksheet. The worksheet row limit does not apply there.
- Split the raw files and the measures table by season.

Store session summaries in a spreadsheet setup. Do not store sample-level data, such as every GPS position or every point of a force trace, in a spreadsheet. Sample-level data has many rows for each second, and needs a database or files in a folder.

### Choose where to host it

Host the system inside accounts the organization already owns and manages. The organization then controls sign-in, removes access when staff leave, and holds the contracts with the vendor.

Use these options, best first, from those IT approves for each class of data in your inventory:

- The organization's own cloud suite, such as its Microsoft 365 or Google Workspace accounts. IT already manages the accounts and the vendor contract. The suite is not approved for every class of data by default. Medical data often needs separate approval.
- A database run by the organization's IT staff.
- A managed cloud database bought under an organization account, with IT approval and a contract the organization signs.

Avoid these options:

- A personal account, such as a personal Google account or a personal Dropbox. The organization cannot manage access or recover the data.
- A free plan of any tool, unless IT approves it for athlete data. Free plans often lack the contract terms an organization needs.
- One laptop as the only copy. Loss or theft of the laptop loses the system.
- A custom web application on a public server, unless someone has the time and skills to keep it updated and secure.

Ask IT which options it approves for athlete data before you build anything. If the organization has no IT staff, ask the person accountable for athlete data, such as the athletic director, the head of school, or the club owner. Read the data terms of each tool before you use it. See [access-and-privacy.md](access-and-privacy.md).

## Common mistakes

These are the mistakes AI tools and staff make most often when they choose a setup:

- Recommending a database and a web application to a coach who has two hours a week and no coding skills.
- Choosing a tool because it has a free plan, without asking whether IT approves it for athlete data.
- Building in a personal account and planning to move it to an organization account later. The move rarely happens.
- Storing one column for each measure in a spreadsheet, then running out of columns. Use the long table layout.
- Keeping sample-level device data in a spreadsheet. The file slows down, then fails.
- Quoting prices or plan limits from memory. They change often. Check the vendor's page.

## Example request

> We have about 120 athletes across four teams, GPS every practice, and force plates weekly. I know Excel and a little Power BI. Should I use a spreadsheet, a database, or something else?

## Check the result

Run these checks on the recommendation:

- Confirm the maintainer already knows every tool in the recommended setup, or the plan includes the training they need.
- Recompute the size estimate with the user's own numbers. Confirm the setup holds the years of history the decisions need, and the plan says how to split or move data before it reaches the limit.
- Confirm every part of the system runs under an account the organization owns.
- Confirm the plan lists what IT must approve.

## Sources

These sources support the figures and the method in this file:

- Microsoft. Excel specifications and limits. https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3. Read on 2026-10-05. A worksheet holds at most 1,048,576 rows by 16,384 columns.
- Google. Files you can store in Google Drive. https://support.google.com/drive/answer/37603. Read on 2026-10-05. A Google Sheets spreadsheet holds up to 20 million cells or 100 MB.
- Microsoft. Manage orphaned flows when owner leaves organization. https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-management/manage-orphan-flow-when-owner-leaves-org. Read on 2026-10-05. A flow with no valid owner can fail if it uses connections tied to that owner's account. Admins can add co-owners.

The comparison of setups and the order of hosting options are practical guidance from the authors of this repository. No study compares them. The size example uses made-up counts to show the method.
