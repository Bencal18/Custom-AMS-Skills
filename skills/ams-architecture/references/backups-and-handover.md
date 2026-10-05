# Back up the system and plan the handover

Last checked: 2026-10-05

## What it covers

This file shows how to back up an AMS, prove the backup works, keep every account under the organization's control, and write a handover document that lets another person run the system.

## Method

### Back up everything the system needs

Back up all of these, not only the data:

- The raw layer.
- The reference tables, including the corrections table.
- The import log.
- Scripts, flows, Power Query steps, and report files.
- The README, the data dictionary, and the change log.

You can rebuild the clean and metric layers from these. See [system-layout.md](system-layout.md).

### Follow the 3-2-1 rule

Keep 3 copies of the data, on 2 different kinds of storage, with 1 copy off site. US-CERT published this 3-2-1 rule in 2012, and CISA repeats it in its guidance for businesses. This example meets the rule:

- The live system, in the organization's cloud suite or database.
- A scheduled copy to a second kind of storage the organization approves.
- A copy off site, such as a separate backup service run by IT.

Ask IT whether its backups already cover the system, and how far back they go. Backups hold the same athlete data as the system, so the same access and retention rules apply to them.

### Know that sync is not a backup

A synced folder copies every change, including a deletion or a file saved over. Version history in a cloud suite helps, but it may keep old versions only for a limited time. Check the limit for your tool. Keep at least one copy that a mistake in the live system cannot change.

### Prove the backup works

A backup counts only after you restore from it. CISA tells businesses to test that they can restore data in full and in part, and NIST control CP-9 calls for testing backups and restoring from a sample. Test a restore at the start of each season or term with these steps:

1. Restore the backup to a separate test location.
2. Rebuild the clean and metric layers from the restored raw layer and reference tables.
3. Pick one athlete and one week. Confirm the restored numbers match the live system.
4. Record the date and the result in the change log.

### Keep every account under the organization

Run every part of the system under accounts the organization owns:

- Shared folders, databases, and report workspaces.
- Scheduled flows and scripts.
- Vendor platform logins and API keys.
- Form tools.

Give each part at least two admins. When an account belongs to one person, the system stops when that person leaves.

### Write the handover document

Keep a README at the top of the system folder. Wilson and colleagues (2017) recommend a short README that explains the project and how to run it. Include these sections:

- What the system is for, with the decision list.
- A map of the parts: where each layer, reference table, script, flow, and report lives.
- Daily and weekly tasks, with the time each one runs and who does it.
- How to add an athlete, a team, a source, and a measure.
- How to fix the five most common failures, such as a failed import or an unknown athlete ID.
- Where the keys and passwords are stored. Never write the keys themselves in the README.
- Who to contact at each vendor, and in IT.
- The change log: each change, its date, and who made it.

Keep scripts in version control, such as a Git repository owned by the organization, when the setup uses scripts. Wilson and colleagues (2017) also recommend a change log and version control.

### Test the handover

Ask a second person to run one full week from the README alone, without help. Fix every step they could not follow. Repeat when the system changes.

## Common mistakes

These are the mistakes AI tools and staff make most often with backups and handover:

- Trusting a synced folder as the backup.
- Backing up the data but not the scripts, flows, and reference tables.
- Never testing a restore.
- Running flows, logins, and keys under the builder's personal account.
- Writing the handover document in the last week before the builder leaves.
- Storing passwords in the README.

## Example request

> I'm leaving at the end of the season. What do I need to set up so the next person can keep our athlete monitoring system running?

## Check the result

Run these checks on the plan:

- Confirm the backup plan has 3 copies, 2 kinds of storage, and 1 separate location.
- Confirm a restore test is scheduled, with the steps written down.
- Confirm every account, flow, and key belongs to the organization and has two admins.
- Confirm a second person has run a full week from the README.

## Sources

These sources support the method in this file:

- Ruggiero P, Heckathorn MA. Data Backup Options. US-CERT. 2012. https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf. States the 3-2-1 rule: 3 copies of any important file, on 2 different media types, with 1 copy off site.
- CISA. Back Up Business Data. https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data. Read on 2026-10-05. Repeats the 3-2-1 rule, and says to test that you can restore data in full and in part.
- NIST. Security and Privacy Controls for Information Systems and Organizations. SP 800-53 Rev. 5. 2020. doi:10.6028/NIST.SP.800-53r5. Control CP-9(1) tests backups for reliability and integrity. Control CP-9(2) tests restoration from a sample of backup information.
- Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK. Good enough practices in scientific computing. *PLOS Computational Biology*. 2017;13(6):e1005510. doi:10.1371/journal.pcbi.1005510. Recommends backing up raw data in more than one location, a README that explains the project, a change log, and version control.

The restore steps, the account rules, and the handover test are practical guidance from the authors of this repository.
