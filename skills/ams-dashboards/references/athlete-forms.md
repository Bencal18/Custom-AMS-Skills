# Build the athlete check-in forms

Last checked: 2026-10-05

## What it covers

This file shows how to build the morning wellness check-in and the session RPE form with a form tool your organization already licenses, such as Microsoft Forms or Google Forms, and how to turn each response into rows of the measures table.

The rules for all athlete forms are in the data intake reference in the `ams-architecture` skill. This file applies them to two forms.

## Method

### Use an approved form tool and an organization account

Ask IT which form tool is approved for athlete data. Build the form under an organization account, never a personal one, and give a second staff member edit access. A form owned by one person stops working when that person leaves.

### Identify the athlete by sign-in

Do not ask athletes to type their name. Typed names have spelling variants, and anyone can type anyone's name.

- Microsoft Forms: in the form settings, limit who can respond to people in your organization, and turn on the option that records each responder's name. The response then carries the athlete's sign-in. Setting names change, so check Microsoft's current help for Forms settings. Microsoft's Power Automate connector for Forms works only with organizational accounts.
- Google Forms: in **Settings**, under **Responses**, set **Collect email addresses** to **Verified**. Google then requires respondents to sign in and collects their account email with each response. **Responder input** lets the athlete type any address, so do not use it to identify athletes.

Map the sign-in to `athlete_id` through the source ID table, with `source` set to `wellness_form` and `source_athlete_id` set to the sign-in address. See the table layout reference in the `ams-data-setup` skill.

### Build the morning wellness form

Use one question for each item, each with a fixed scale. Make every item required. Write each question so that 5 is the best answer, so no item needs flipping later. The item name names the topic, not the direction. On every item, 5 is best:

| Item | Question | 1 | 5 |
|---|---|---|---|
| `sleep_quality` | How well did you sleep? | Very poorly | Very well |
| `fatigue` | How fresh do you feel? | Very tired | Very fresh |
| `soreness` | How do your muscles feel? | Very sore | Not sore |
| `stress` | How relaxed do you feel? | Very stressed | Very relaxed |
| `mood` | How is your mood? | Very low | Very good |

Follow these rules:

- Keep the form short. Ask only the items a decision needs.
- Label every point on the scale, not only the ends, if the form tool allows.
- Add one line under the soreness question: "Report pain or an injury to the athletic trainer, not on this form." A routine soreness rating is monitoring data. Pain is a medical matter. See the `load-and-wellness` skill.
- Do not add free-text questions unless someone reads every answer the same day. Free text can hold a welfare concern. Follow the organization's referral process.
- Write the items in the measure dictionary, with the scale, the wording, and the direction.

Single-item wellness questions have little published validation. See the wellness z-score reference in the `load-and-wellness` skill before you treat any item as a precise measure.

### Build the session RPE form

Ask one question about 30 minutes after the session ends (Foster et al., 2001), such as "How hard was your session?" Show the 0 to 10 CR-10 scale that the session RPE load reference in the `load-and-wellness` skill describes. Check that your organization may use the scale's wording. Add a session choice, such as `practice`, `gym`, or `match`, so the response joins to the right session.

Do not ask for the duration. Take it from the session log, so every athlete in a session gets the same duration rule. See the session RPE load reference.

### Turn each response into measure rows

Each form response becomes one row for each item in the measures table:

```text
athlete_id,measure_date,session_id,measure_name,side,trial_number,value,unit,status,source,source_record_id,imported_on
A0001,2026-10-02,none,sleep_quality,bilateral,1,4,points,ok,wellness_form,R-5512,2026-10-02
A0001,2026-10-02,none,fatigue,bilateral,1,3,points,ok,wellness_form,R-5512,2026-10-02
```

Follow these steps for each import:

1. Copy the raw responses, unchanged, to the raw layer.
2. Look up `athlete_id` from the sign-in. Hold any response whose sign-in has no match, and list it for staff.
3. Convert the submission time to the local date at the athlete's location. Use that date as `measure_date`.
4. Reshape the response from one column for each question to one row for each item.
5. Use the form tool's response ID as `source_record_id`. Skip a response ID already imported, so running the import twice adds no rows.
6. If an athlete submits twice on one day, keep both rows with `status` set to `held`, and ask staff which to keep. Do not keep the last one by default.
7. Write a row to the import log with the count of responses and rows.

### Automate the import

Pick the automation that matches the form tool:

- Microsoft Forms: a Power Automate cloud flow with the trigger **When a new response is submitted**, then the action **Get response details**, then one row written to the raw response list or file. Run the flow under an organization account, and add a second owner.
- Google Forms: link the form to a Google Sheet as the raw layer. An installable Apps Script trigger can run on each form submit. Installable triggers run under the account of the person who created them, and no other account can see or manage them. Create them from an organization-owned account, and record in the handover document how a second staff member signs in to it.
- Either tool: a scheduled export of all responses, read by your import script, which skips response IDs it has already seen.

Run the reshaping step from steps 2 to 7 in one place, such as the import script or Power Query. Do not reshape in the form tool and again in the dashboard.

### Remind athletes and track completion

Send one reminder at a fixed time, such as 06:00, with the form link. Use the tool your organization approves for messages to athletes. Show form completion on the data health screen every day, as forms received out of forms expected. See [core-screens.md](core-screens.md).

### Tell athletes what you collect

Tell athletes who sees their answers, what the answers are used for, and how long you keep them. See the access and privacy reference in the `ams-architecture` skill. If any athletes are minors, check the consent rules first.

## Common mistakes

These are the mistakes staff and AI tools make most often with athlete forms:

- Asking athletes to type their name or ID.
- Using **Responder input** for the email address in Google Forms, so anyone can submit as anyone.
- Mixing scales, where 5 is best on one item and worst on another, then adding them.
- Taking `measure_date` from a UTC timestamp, so late answers land on the next day.
- Keeping only the last response when an athlete submits twice.
- Building the form or the flow under a personal account.
- Asking about pain or injury on a monitoring form that coaches read.
- Treating a missing form as a good day.

## Example request

> Set up a morning wellness form in Microsoft Forms for 40 athletes, and get the answers into my measures table every morning before 06:45.

## Check the result

Run these checks before athletes use the form:

- Submit a test response from a test athlete account. Confirm it arrives as 5 rows with the right `athlete_id`, date, and values.
- Run the import twice. Confirm the row count does not change.
- Submit twice on one day from the test account. Confirm both rows are `held`.
- Submit at 23:30 local time. Confirm `measure_date` is that local date.
- Confirm a second staff member can edit the form and the flow or script.

## Sources

These sources support the steps in this file. Each was read on 2026-10-05:

- Microsoft. Microsoft Forms connector reference. https://learn.microsoft.com/en-us/connectors/microsoftforms/. The connector works only with organizational accounts. Names the trigger **When a new response is submitted** and the action **Get response details**.
- Google. View and manage form responses. https://support.google.com/docs/answer/139706. Steps for **Collect email addresses** with **Verified** and **Responder input**.
- Google. Installable triggers. https://developers.google.com/apps-script/guides/triggers/installable. Form submit triggers for Google Forms and Sheets, the rule that installable triggers run under the account of the person who created them, and the rule that an account cannot see triggers installed from a second account.
- Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. *Journal of Strength and Conditioning Research*. 2001;15(1):109-115. doi:10.1519/00124278-200102000-00019. Collected the session rating about 30 minutes after the session.

The form items, the reshaping steps, and the reminder rules are practical guidance from the authors of this repository. They follow the data intake reference in the `ams-architecture` skill and the `load-and-wellness` skill.
