# Ambiguous phrases

Last checked: 2026-10-07

## What it covers

This file lists phrases coaches use that can mean more than one thing. For each one, it gives the question to ask and a default to offer. It also covers words that sound like a judgment about an athlete, such as "ready" or "struggling".

## Method

Ask before you calculate. A question costs the coach one reply. A wrong window or measure costs a wrong answer that looks right.

Follow these rules:

- Ask about every unclear part in one message, not one question at a time.
- Offer a default for each question, so the coach can answer "yes". Label it as a default, not a rule.
- Never apply a default without telling the coach. If the coach says "just pick", use the default and state it in the first sentence of the answer.
- Keep the coach's own words in the restated query, next to your precise version, for example: "last week (Monday 2026-09-28 to Sunday 2026-10-04)".
- The defaults below are this skill's choices. No published source sets them.

### Ask about time words

| Phrase | What it could mean | Ask | Default to offer |
|---|---|---|---|
| "last week" | The last 7 days, the last full training week, or the previous calendar week | "Do you mean the last 7 days, or the last full training week? Which day does your training week start on?" | The last full training week, Monday to Sunday |
| "this week" | The training week so far, or the last 7 days | "The training week so far, from Monday to today? This week is not complete yet." | The training week so far, with the days counted and the week marked incomplete |
| "last month" | The previous calendar month, or the last 30 days | "The calendar month, such as 2026-09-01 to 2026-09-30, or the 30 days before the latest test?" | The previous calendar month |
| "this season" | Since the first session, the first match, or a date in the season plan | "Which date does the season start on for this question?" | The first session date in the sessions table, stated in the answer |
| "recently" or "lately" | Any window | "How far back? For example, the last 14 days or the last 4 sessions." | No default. Ask. |
| "the last four sessions" | The squad's last four sessions, or each athlete's last four sessions they attended | "The squad's last four sessions, or each athlete's own last four?" | The squad's last four sessions, from the sessions table |
| "since the break" or "since camp" | A date the coach knows | "Which date should I start from?" | No default. Ask. |

### Ask about threshold and comparison words

| Phrase | What it could mean | Ask | Default to offer |
|---|---|---|---|
| "over threshold" or "over the line" | Whose threshold, which measure, above or at or above, and in how many sessions | "Which measure, and what number? Above, or at or above? In any of the sessions, or all of them?" | No default for the number or the measure. Ask. For the rest, offer "above", and a count of sessions over the line out of sessions with data. |
| "high" or "low" | Against a threshold, the athlete's own baseline, or the squad | "High compared with what: a number you set, their own usual, or the squad?" | Their own baseline |
| "compared with" or "versus" | Latest value against a baseline mean, or two single tests | "Latest test against their average over a window, or against one earlier test?" | Latest test against the mean of the baseline window |
| "down" or "up" | A change in units or in percent | "Do you want the change in units, in percent, or both?" | Both |
| "normal" or "usual" | The athlete's own baseline over a window | "Over which window?" | The athlete's own baseline window from the owning skill, stated with `n` |

### Ask about ranking words

These words ask for an order: "best", "worst", "top", "bottom", "most", "least", "highest", "lowest", and "most improved". Follow these rules:

- Ask what the order is by: the raw value, the change in units, the change in percent, or the change against the noise band. The answer can change the order. In the third worked example, one athlete has the largest drop in metres and another the largest drop in percent.
- For "most improved", ask over which window, and compare each change with the noise band. Say that an unusually low first value tends to be followed by one closer to the athlete's usual level, so part of a large gain can be regression to the mean. The `monitoring-statistics` skill covers this.
- For the whole squad, follow the no-ranking rules in `SKILL.md` and offer the alternatives there.
- When a few athletes are asked for, such as "who missed the most", show every athlete sorted by change from their own baseline, with the noise band, and list athletes who have no data last. Do not crown one athlete.
- Keep the coach's ranking word out of the answer. Do not use best, worst, top, bottom, or rank numbers in any label or title. Write a title that describes the data, such as `Change in high-speed running from own usual week, week of 2026-09-28`.

| Phrase | Ask | Default to offer |
|---|---|---|
| "best" or "worst" | "Which measure, and compared with what?" | Sorted by change from own baseline, with the noise band, a title that describes the data, and the note `Sorted by change, not by ability` |
| "most improved" | "Over which window? Do you want only changes larger than the test's noise?" | Change from own baseline over the coach's window, with the noise band |
| "missed the most" | "Missed sessions, or less of the measure than usual, or less than planned?" | No default. Ask. |

### Ask about judgment words

Some words describe an athlete, not a measure: "ready", "tired", "fatigued", "fresh", "struggling", "flat", "fit", "recovered", "at risk", and "overloaded". Follow these rules:

- Ask which measure the coach means. Offer the measures the data holds, for example: "Which measure should I use for 'ready': jump height against their own baseline, wellness score, session load, or something else?"
- Do not pick a measure for the coach.
- Do not answer with the coach's word. Answer with the measure: "Jump height is below her usual range", not "She is not ready".
- Do not combine measures into one score to answer the word. If the coach wants a composite, use the `readiness-composites` skill and keep every sub-score visible.
- If the word points to pain, injury, illness, or rehab, do not analyze it here. Tell the user to involve the medical team.
- If the word points to mood, stress, or welfare, do not interpret it. Tell the user to follow their organization's referral process and involve appropriate staff.

| Phrase | Ask | Default to offer |
|---|---|---|
| "ready" | "Which measure should I use, and compared with what?" | No default. Ask. |
| "tired" or "fatigued" | "Which measure should I use: a jump test, wellness answers, or load?" | No default. Ask. |
| "struggling" | "Struggling on which measure: running output, a test, or wellness answers?" | No default. Ask. |
| "fit" | "Which test: a conditioning test, a sprint test, or a strength test?" | No default. Ask. |

### Ask about who

| Phrase | Ask | Default to offer |
|---|---|---|
| "the squad" or "everyone" | "All active athletes, or only those who trained in the window?" | All active athletes on the roster, with those who did not train listed as no data |
| "the forwards" or another group | "Should I use the position column in the athletes table?" | The athletes table's position column |
| An athlete's first name | "Which athlete ID is that?" | Look it up in the coach's ID list. Keep the name out of the data. |
| "the starters" or "the bench" | "Which column or session marks who started?" | No default. Ask. |

## Common mistakes

These are the mistakes AI tools make most often with ambiguous phrases:

- Choosing "last 7 days" when the coach meant the training week, or the reverse, without saying so.
- Answering "who is ready" with a guessed measure and a judgment about each athlete.
- Asking one question per message, so the coach answers four times.
- Applying a default without stating it in the answer.
- Treating "most" as a ranking of the whole squad by raw value.
- Treating "missed" as one meaning when it could be absence or less output.

## Example request

> Who's struggling this week?

A good reply asks two things in one message: "Struggling on which measure: running output, a jump test, or wellness answers? And do you mean the training week so far, from Monday 2026-10-05 to today?"

## Check the result

Run these checks:

- Confirm every phrase from the tables above in the coach's question has a question or a confirmed default.
- Confirm the restated query keeps the coach's words next to the precise version.
- Confirm no judgment word appears in the answer as a label for an athlete.

## Sources

The questions and defaults in this file are practice guidance from the authors of this repository. No published source sets them. The Monday-to-Sunday training week follows the default in the `load-and-wellness` skill's session RPE load reference.
