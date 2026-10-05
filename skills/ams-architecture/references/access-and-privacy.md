# Control access and protect privacy

Last checked: 2026-10-05

This file is not legal advice. It lists questions to take to your organization's compliance, legal, or IT staff. Only they can say which laws and policies apply to your data. The rules differ by country, state, organization, and sport, and they change. Do your own research, and confirm what applies to you before you act.

## What it covers

This file shows how to list the athlete data an AMS holds, decide who can see and change it, and prepare the privacy questions for compliance staff. It covers roles, accounts, medical data, sharing, AI tools, consent, retention, and data incidents.

## Method

### List the data and every copy

Write a data inventory before you share anything. Use one row for each kind of data, with these columns:

- `data`: for example, names and IDs, GPS load, force plate results, wellness answers, injury and rehab notes.
- `class`: `identifier`, `performance`, `wellness`, or `medical`. Treat wellness free text as `medical`.
- `about_minors`: `yes` or `no`.
- `where`: every place a copy lives, including the vendor platform, the AMS, report files, exports, backups, and email.
- `who_sees`: every role with access.
- `keep_for`: how long you keep it.

Missing copies cause most surprises. Include exports saved to laptops and report files sent by email.

### Ask compliance staff which rules apply

Which law applies depends on the country, the type of organization, who holds the data, and why. If the organization has no compliance or IT staff, take the questions to the person accountable for athlete data, such as the athletic director, the head of school, or the club owner. Take the data inventory to your compliance, legal, or IT staff with these questions:

- Which law and which policies apply to each class of data?
- Which tools and storage are approved for each class?
- Which AI tools, if any, are approved for this data?
- Do we need athlete consent, or a parent's or guardian's consent, for each kind of data?
- If we rely on consent, can an athlete refuse without any effect on selection, a scholarship, or a contract?
- How long must or may we keep each kind of data?
- Who must we tell if data is exposed, and how fast?
- Does any contract, such as a vendor agreement or a player agreement, limit how we use the data?
- Who outside the organization may receive athlete data, such as other teams, scouts, sponsors, or researchers?
- Will we use any of this data for research or publication? Which ethics review, such as an institutional review board (IRB), do we need first?
- What happens to an athlete's data when they transfer or leave?
- Does the data leave the country, for example to a cloud host or AI tool abroad? Do we need a data protection impact assessment?

These are examples of rules that compliance staff may name. They are not a full list, and they do not tell you which rule applies to you:

- In the United States, FERPA applies to schools and colleges that receive US Department of Education funds. Health records about students that such a school keeps are generally education records under FERPA. Performance and wellness data a school keeps about a student can also be education records. At colleges, some records made only for treatment are treatment records instead. The HIPAA Privacy Rule excludes both kinds of record from protected health information. A clinic or provider that is a HIPAA covered entity may hold some athlete records under HIPAA instead. The US Departments of Health and Human Services and Education publish joint guidance on where the line falls.
- In the European Union and the United Kingdom, data about health is a special category of personal data under the GDPR and the UK GDPR, with extra conditions for its use. Data from fitness trackers, and conclusions drawn about a person's health, can count as health data. Data with names replaced by codes is still personal data when someone can link the codes back to names, for example with the athletes table.
- At US colleges, the NCAA Committee on Competitive Safeguards and Medical Aspects of Sports recommends that schools write a plan for performance technology. The plan sets who owns the data, where it is stored, who can access it, and how it may be used. These are recommendations, not NCAA rules.
- At professional clubs, employment law, the player contract, and league collective bargaining agreements can limit how a team collects and uses athlete data.
- Many laws give children's data extra protection, and give parents or guardians rights over it. Safeguarding policies may also apply.
- Many other countries have their own privacy laws, and many organizations have policies stricter than the law.

### Write the access table

Use one row for each role. Give each role only the access it needs to do its work. NIST calls this the principle of least privilege. This example is a starting point, not a rule:

| Role | Can see | Can change |
|---|---|---|
| System owner | Everything except medical data, unless they are medical staff | Reference tables, imports, calculations, reports |
| Second admin | Same as the owner | Same as the owner, for cover |
| Sport scientist or S&C coach | Performance data and wellness scores for their teams, not wellness free text | Reference tables for their teams |
| Sport coach | Summaries and availability flags for their team | Nothing |
| Athletic trainer or medical staff | Medical data and performance data for their athletes | Medical records, in the medical system |
| Athlete | Their own data only | Their own form answers |

Follow these rules for accounts:

- Give each person a named account through the organization's sign-in. Never share a login.
- Turn on multi-factor sign-in where the organization's tools support it.
- Remove access on the day a person leaves or changes role.
- Review the access list at the start of each season or term.
- Keep at least two admins, so nobody is locked out when one person leaves.

### Show athletes only their own data

Folder and file sharing cannot show each athlete only their own rows. Use one of these methods, matched to the setup:

- Spreadsheet: create one report file for each athlete from the metric layer, and share each file with that athlete only.
- Low-code: use the form tool's own view of each person's answers, or row-level security in the report tool. Check the license on the vendor's page.
- Database: use row-level security in the report tool or the database.
- Commercial product: use its athlete app or athlete view.

Test the method by signing in as a test athlete and confirming no other athlete's data appears.

### Keep medical data with medical staff

Keep diagnoses, injury notes, and treatment records in the system the medical staff use and control. Share an availability status with coaches, such as `available`, `modified`, or `unavailable`, instead of the diagnosis. Ask the medical staff and compliance staff before you copy any medical detail into the AMS.

### Share reports safely

Follow these rules when you share results:

- Share links with named people or groups. Do not use links that anyone with the link can open.
- Do not email exports or attach athlete data to messages, unless the organization's policy allows it, for example through encrypted email.
- Do not post screenshots with athlete names in group chats.
- Replace names with `athlete_id` before you share data outside the staff who need it. On a small team, a position, a date, or an injury can still identify an athlete. Keep treating the data as personal data.

### Use AI tools with care

Paste athlete data into an AI tool only if the organization approves that tool for that data. Use the tool only through an organization account. Personal and free accounts may keep what you type, or use it to train models. Replace names with `athlete_id` first. This lowers the risk, but it does not make the data anonymous. Prefer asking the AI for a formula or a script, and run it yourself on the data, over pasting the data into the chat.

### Tell athletes what you collect

Tell athletes, in plain words:

- What data you collect, and why
- Who sees it
- How long you keep it
- How they can see their own data, and who to ask about it

FERPA gives parents the right to inspect and review their child's education records. The right moves to the student at age 18, or when the student enrolls in a college at any age. At a college, ask compliance staff before you show a parent any athlete data. The GDPR gives people a right of access to their personal data. Ask compliance staff how these rights work in your organization.

### Keep data only as long as you need it

Set a retention period for each class of data with compliance staff. Delete or anonymize data on that schedule, including the copies in exports. Let backups expire on a matching cycle. Pause deletion if compliance staff place a legal hold. Record each deletion.

### Know what to do if data is exposed

Write down who to contact, usually the IT security team, before anything goes wrong. If a file is shared too widely, a laptop is lost, or a key leaks, contact them at once. Note the time you found the problem, because some laws count deadlines from then. Under the GDPR, the organization must notify the supervisory authority without undue delay, and where feasible within 72 hours of becoming aware of the breach, unless the breach is unlikely to put people at risk. Do not try to handle it alone.

## Common mistakes

These are the mistakes AI tools and staff make most often with access and privacy:

- Telling a user that a tool "is HIPAA compliant" or "is FERPA compliant". Compliance depends on the contract, the setup, and the use, not on the tool alone.
- Sharing a report with a link that anyone can open.
- Giving every coach access to every team, and to medical notes.
- Leaving former staff with access for months.
- Copying injury details into a performance spreadsheet that coaches can open.
- Pasting named athlete data into an AI tool the organization has not approved.
- Forgetting the copies: exports on laptops, files in email, and old backups.

## Example request

> Who should be able to see what in our athlete monitoring system? We have S&C, sport coaches, athletic trainers, and athletes.

## Check the result

Run these checks on the access plan:

- Confirm every copy in the data inventory has an access rule.
- Confirm athletes can see only their own data.
- Confirm coaches see availability, not diagnoses, unless medical and compliance staff approved more.
- Confirm compliance staff answered the consent and access questions for every row marked `about_minors: yes`.
- Confirm the plan lists the questions for compliance staff, and makes no claim that the setup complies with any law.

## Sources

These sources support the facts in this file. None of them is a full statement of the law. Ask compliance staff which rules apply to you.

- US Department of Education and US Department of Health and Human Services. Joint Guidance on the Application of the Family Educational Rights and Privacy Act (FERPA) and the Health Insurance Portability and Accountability Act of 1996 (HIPAA) to Student Health Records. December 2019 update. https://studentprivacy.ed.gov/resources/joint-guidance-application-ferpa-and-hipaa-student-health-records. States that FERPA applies to schools that receive US Department of Education funds, that student health records kept by such a school generally are education records, that some college records are treatment records, and that the HIPAA Privacy Rule excludes records protected by FERPA from protected health information. Also states that FERPA rights move to the student at age 18 or on enrolling in a college.
- US Department of Health and Human Services, Office for Civil Rights. Summary of the HIPAA Privacy Rule. https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html. Read through an archived copy on 2026-10-05. Defines covered entities, and states that protected health information excludes employment records a covered entity keeps as an employer, and education records subject to FERPA. The regulation is 45 CFR 160.103.
- 34 CFR 99.10. Rights of inspection and review of education records. https://www.law.cornell.edu/cfr/text/34/99.10. Read on 2026-10-05.
- Regulation (EU) 2016/679 (General Data Protection Regulation). https://eur-lex.europa.eu/eli/reg/2016/679/oj. Recital 26 and Articles 33 and 35 read on 2026-10-05 in the official text from the EU Publications Office. Article 4(15) defines data concerning health. Article 9 makes it a special category of personal data. Article 15 gives the right of access. Article 33(1) requires notice to the supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware of a breach, unless the breach is unlikely to result in a risk to people. Article 35 requires a data protection impact assessment before processing likely to result in a high risk, including large-scale processing of health data. Recital 26 states that pseudonymised data that can be linked back to a person with additional information is information on an identifiable person.
- Information Commissioner's Office. What is special category data? https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/. Read on 2026-10-05. UK guidance on health data as special category data, including fitness tracker data. The ICO marks this guidance as under review.
- NIST. Security and Privacy Controls for Information Systems and Organizations. SP 800-53 Rev. 5. 2020. doi:10.6028/NIST.SP.800-53r5. Control AC-6 sets the principle of least privilege.
- NCAA Committee on Competitive Safeguards and Medical Aspects of Sports. Performance Technologies Recommendations: Responsible Use in Collegiate Athletics. NCAA Sport Science Institute. March 2026. https://www.ncaa.org/what-we-do/health-safety-and-performance/performance-technologies-guidelines/ and https://ncaaorg.s3.amazonaws.com/ssi/performance/SSI_PerformanceTechRecommendations.pdf. Read on 2026-10-05. Recommendation 1 calls for a written plan. Recommendation 3 covers who owns performance technology data, where it is stored, who can access it, and how it may be used. It also names data for athletes who transfer, and the authority of sports medicine staff over medical decisions.

The access table, the account rules, and the advice on medical data, sharing, and AI tools are practical guidance from the authors of this repository.
