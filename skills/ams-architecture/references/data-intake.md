# Bring data into the system

Last checked: 2026-10-05

Product names in this file are examples, checked on the date above. Naming a product is not an endorsement.

## What it covers

This file shows how to bring data from devices, forms, and files into an AMS. It covers manual exports, shared-folder imports, vendor APIs, forms, API keys, schedules, checks on arrival, and failure alerts.

## Method

### Choose an intake method for each source

Use the simplest method that meets the decision deadline for that source:

| Method | How it works | Fits when | What breaks it |
|---|---|---|---|
| Manual export | A staff member exports a file from the vendor platform and imports it | Weekly or daily reviews with time to spare | Missed days, wrong date ranges, files saved over |
| Shared-folder import | Staff save exports to one folder, and a scheduled step imports every new file | Daily deadlines, several staff exporting | Files saved to the wrong folder, renamed files |
| Vendor API pull | A scheduled flow or script requests new data from the vendor's API | Same-day deadlines, many sessions, several sources | Expired keys, changed fields, rate limits |
| Direct form | Athletes submit a form that writes straight to the raw layer | Wellness and RPE questions | Typed names instead of IDs, free-text numbers |

Ask each vendor which options your contract includes: file exports, an API, or a built-in link to another tool. Ask for the API documentation and the terms of use. Confirm the terms let you store the data outside the vendor's platform.

The metric skills in this repository hold device export references for several vendors. Load them if they are installed. Do not guess an export layout.

### Pull from an API

An API (application programming interface) lets a script or flow request data from a vendor's system. Follow these rules for every API pull:

- Request only new or changed records, by the date the vendor last changed them, when the API allows it.
- Pull a few days of overlap each time, so late edits on the vendor side reach you. The import log and the source's record ID stop the overlap from doubling rows.
- Save each response unchanged in the raw layer before you transform it.
- Read the paging rules. Many APIs return results in pages. A script that reads only the first page silently drops data.
- Read the rate limits. Space requests so the vendor does not block the key.
- Read the time zone of every timestamp. Many APIs return UTC. Convert to the local session date in the clean step.

### Protect API keys and passwords

An API key gives full access to the data it can reach. Follow these rules:

- Store keys only in a password manager, a secrets store, or the secure connection settings of a flow tool, that the organization approves.
- Never put a key in a spreadsheet cell, a script file, a shared folder, an email, or a chat with an AI tool.
- Create the key under an organization account, not a personal one.
- Use one key for each system, so you can revoke one without stopping the others.
- Replace every key a departing staff member could see, on their last day.
- If a key is exposed, revoke it at the vendor and create a new one at once.

### Run imports on a schedule that meets the deadline

Set each schedule from the decision list. If staff read the wellness report at 06:45, and athletes finish the form by 06:15, run the import and the calculation at 06:20, and again at 06:40 for late forms.

In a low-code setup, a scheduled flow, such as a Power Automate cloud flow with a recurrence trigger, can run the import. Run every flow under an account the organization owns, and add a second owner. In a database setup, a scheduled script runs the import.

### Check data on arrival

Run these checks before new rows reach the clean layer:

- Count the rows. Compare with the expected count from the session list.
- Confirm the columns match the expected layout. If a column is new, missing, or renamed, stop the import and alert the owner. Do not load it.
- Confirm every source athlete ID maps to an `athlete_id`. Hold rows for unknown IDs, and ask a person to map them.
- Confirm the dates fall in the requested range and are not in the future.
- Confirm the units match the measure dictionary.

Record every count in the import log. See [system-layout.md](system-layout.md).

### Alert someone when an import fails

Send a message to the source owner when any of these happen:

- The import fails.
- The import returns zero rows on a day with a scheduled session.
- A check on arrival stops the import.
- The key is rejected.

Zero rows on a training day is a failure, not a quiet day. Show the date and time of the last successful import on every report.

### Set up forms for athletes

Follow these rules for wellness, RPE, and other athlete forms:

- Use the form tool the organization approves.
- Identify the athlete by their organization sign-in or a fixed list, never by a typed name.
- Use fixed answer scales. Do not let athletes type numbers in free text.
- Record the submission time with its time zone.
- Make the items the decision needs required. Keep the form short.
- Tell athletes who sees their answers and why. See [access-and-privacy.md](access-and-privacy.md).

## Common mistakes

These are the mistakes AI tools and staff make most often with intake:

- Pasting an API key into a script or a chat with an AI tool.
- Reading only the first page of an API response.
- Treating zero rows as "no data today" instead of a failed import.
- Loading a changed export layout without noticing, so a column lands in the wrong field.
- Running flows under one staff member's account with no co-owner. The flows can fail when the account closes.
- Letting athletes type their names. Spelling differences split one athlete into two.

## Example request

> Our GPS vendor has an API. Can you help me set up an automatic pull every morning into our Microsoft 365 setup?

## Check the result

Run these checks on the intake plan:

- Confirm each source has a method, a schedule, an owner, and a failure alert.
- Confirm no key appears in any file, script, sheet, or message in the plan.
- Run one import twice in a test copy. Confirm no rows double.
- Rename one column in a test file. Confirm the import stops and alerts the owner.

## Sources

These sources support the rules in this file:

- OWASP. Secrets Management Cheat Sheet. OWASP Cheat Sheet Series. https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html. Read on 2026-10-05. Describes secrets left in plain text in source code and configuration files, and recommends central storage, rotation, and auditing of secrets.
- Microsoft. Overview of cloud flows. https://learn.microsoft.com/en-us/power-automate/overview-cloud. Read on 2026-10-05. A scheduled cloud flow runs an automation on a schedule, such as a daily data upload.
- Microsoft. Tutorial: Get started with cloud flows. https://learn.microsoft.com/en-us/power-automate/get-started-with-cloud-flows. Read on 2026-10-05. Builds a scheduled flow with a **Recurrence** trigger.
- Microsoft. Manage orphaned flows when owner leaves organization. https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-management/manage-orphan-flow-when-owner-leaves-org. Read on 2026-10-05. A flow with no valid owner can fail if it uses connections tied to that owner's account.

The intake methods, the overlap rule, the checks on arrival, and the alert rules are practical guidance from the authors of this repository.
