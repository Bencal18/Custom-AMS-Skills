# Worked examples

Last checked: 2026-10-07

## What it covers

This file works three made-up coach questions from question to answer. Each example shows the data, the questions asked back, the restated query, a spreadsheet formula, an SQL query, and the short answer. All athletes, values, and thresholds are synthetic.

The SQL uses the SQLite dialect. Every number in this file came from running the SQL below on the tables shown, and from a separate check in Python. The spreadsheet formulas follow the same logic.

## Method

Each example follows the steps in `SKILL.md`: restate, ask, route, query, count, check, and answer.

### Example 1: who is over a threshold

> Who's been over 600 m of high-speed running in the last four sessions?

**Ask back.** The question names a number and a measure, but leaves three parts open. Ask in one message:

- "Is 600 m your own line, or from a source?" The coach says it is the staff's own number.
- "Above 600 m, or at or above?" The coach says above.
- "The squad's last four sessions, or each athlete's own last four?" The coach says the squad's.

High-speed running here is the distance above the speed setting in the GPS export. The `gps-running-load` skill owns that setting. Ask which speed the export uses if the coach does not know.

**Restated query.** For all 6 active athletes, count the sessions among the squad's last four sessions (2026-09-29 to 2026-10-03, both included) in which high-speed running distance was above 600 m, a threshold the coach set. Report the count out of sessions with data.

**Data.** The `gps` table has one row for each athlete and session. The `sessions` table also holds an earlier session, `S20` on 2026-09-26, which the window must leave out. These are the rows in the window:

| athlete_id | session_date | session_id | hsr_m | status |
|---|---|---|---|---|
| A01 | 2026-09-29 | S21 | 720 | ok |
| A01 | 2026-09-30 | S22 | 410 | ok |
| A01 | 2026-10-02 | S23 | 655 | ok |
| A01 | 2026-10-03 | S24 | 590 | ok |
| A02 | 2026-09-29 | S21 | 610 | ok |
| A02 | 2026-09-30 | S22 | 630 | ok |
| A02 | 2026-10-02 | S23 | 702 | ok |
| A02 | 2026-10-03 | S24 | 615 | ok |
| A03 | 2026-09-29 | S21 | 380 | ok |
| A03 | 2026-09-30 | S22 | NA | device_failure |
| A03 | 2026-10-02 | S23 | 520 | ok |
| A03 | 2026-10-03 | S24 | 605 | ok |
| A04 | 2026-09-29 | S21 | 540 | ok |
| A04 | 2026-09-30 | S22 | 560 | ok |
| A04 | 2026-10-02 | S23 | 590 | ok |
| A04 | 2026-10-03 | S24 | 598 | ok |
| A05 | 2026-09-29 | S21 | 680 | ok |
| A05 | 2026-09-30 | S22 | 640 | ok |
| A05 | 2026-10-02 | S23 | NA | excused |
| A05 | 2026-10-03 | S24 | NA | excused |
| A06 | 2026-09-29 | S21 | 600 | ok |
| A06 | 2026-09-30 | S22 | 655 | ok |
| A06 | 2026-10-02 | S23 | 601 | ok |
| A06 | 2026-10-03 | S24 | 580 | ok |

**Excel.** Put the threshold in `H1`. Find the window from the `sessions` table: the start in `H2` and the end in `H3`. Put the roster IDs in `J2:J7`, then fill `K2:M2` down:

```text
H1: 600
H2: =LARGE(UNIQUE(sessions[session_date]),4)
H3: =MAX(sessions[session_date])
K2 (sessions with data): =COUNTIFS(gps[athlete_id],J2,gps[session_date],">="&$H$2,gps[session_date],"<="&$H$3,gps[status],"ok")
L2 (sessions over):      =COUNTIFS(gps[athlete_id],J2,gps[session_date],">="&$H$2,gps[session_date],"<="&$H$3,gps[status],"ok",gps[hsr_m],">"&$H$1)
M2 (sessions missing):   =COUNTIFS(sessions[session_date],">="&$H$2,sessions[session_date],"<="&$H$3)-K2
```

The `H2` formula assumes one session for each date. To list the rows over the line, use `FILTER`. Keep the status test: without it, the text `NA` passes `gps[hsr_m]>$H$1`.

```text
=FILTER(gps,(gps[session_date]>=$H$2)*(gps[session_date]<=$H$3)*(gps[status]="ok")*(gps[hsr_m]>$H$1),"none")
```

**Google Sheets.** Use `QUERY` with the `gps` sheet in columns A to E:

```text
=QUERY(gps!A1:E,"select A, count(D) where B >= date '2026-09-29' and B <= date '2026-10-03' and E = 'ok' and D > 600 group by A label count(D) 'sessions_over'",1)
```

This returns 5 rows, not 6. A04 has no session over the line, so `QUERY` leaves A04 out. Join the result back to the roster.

**SQL.** Start from the roster, so every athlete keeps a row. `COALESCE` turns the empty sum for an athlete with no rows into 0 sessions, so that athlete shows 4 sessions missing instead of a blank:

```sql
WITH last4 AS (
  SELECT session_id FROM sessions ORDER BY session_date DESC LIMIT 4
)
SELECT r.athlete_id,
       COALESCE(SUM(g.status = 'ok'), 0)                   AS sessions_with_data,
       COALESCE(SUM(g.status = 'ok' AND g.hsr_m > 600), 0) AS sessions_over_600,
       4 - COALESCE(SUM(g.status = 'ok'), 0)               AS sessions_missing
FROM roster r
LEFT JOIN gps g
  ON g.athlete_id = r.athlete_id
 AND g.session_id IN (SELECT session_id FROM last4)
GROUP BY r.athlete_id
ORDER BY r.athlete_id;
```

**Answer.**

Over the squad's last four sessions, 2026-09-29 to 2026-10-03, A02 was above 600 m of high-speed running in all 4 sessions. A01 and A06 were above it in 2 of 4, A05 in 2 of 2 with data, A03 in 1 of 3 with data, and A04 in none. All 6 athletes have data, covering 21 of 24 athlete-sessions: A05 was excused from 2 sessions, and A03 has 1 session missing from a device failure.

| athlete_id | Sessions over 600 m | Sessions with data | Sessions missing |
|---|---|---|---|
| A01 | 2 | 4 | 0 |
| A02 | 4 | 4 | 0 |
| A03 | 1 | 3 | 1 (device failure) |
| A04 | 0 | 4 | 0 |
| A05 | 2 | 2 | 2 (excused) |
| A06 | 2 | 4 | 0 |

Threshold: above 600 m, set by the coach, with no published source. A06 ran exactly 600 m on 2026-09-29. At or above 600 m, A06's count would be 3 of 4. Values close to the line can fall on either side from measurement error alone. Rows used: 21. Rows left out: 3, with status `excused` (2) or `device_failure` (1). Measure: high-speed running distance per session, in m, at the export's speed setting, from the `gps-running-load` skill.

### Example 2: how one athlete compares with last month

> How does Sam's jump compare with last month?

**Ask back.** Ask in one message:

- "Which athlete ID is Sam?" The coach says A03.
- "Which jump measure: countermovement jump (CMJ) height?" The coach says yes, the mean of 3 trials, by the takeoff velocity method. The `force-plate` skill owns the measure and the trial summary.
- "Last month as September, 2026-09-01 to 2026-09-30, or the 30 days before the latest test?" The coach says September.
- "Do you have a typical error for this test?" The coach gives 1.1 cm, from a same-day retest of 20 athletes in the squad, with the same protocol. In this example the value is made up.

**Restated query.** For athlete A03, compare the latest CMJ height (mean of 3 trials, takeoff velocity method, in cm) with the mean of A03's September 2026 tests. Judge the change against the noise band `1.96 × TE × √(1 + 1/n)`, with TE 1.1 cm.

**Data.** The `cmj` table has one row for each athlete and test day:

| athlete_id | test_date | jump_height_cm | summary | status |
|---|---|---|---|---|
| A03 | 2026-09-01 | 40.2 | mean_of_3 | ok |
| A03 | 2026-09-08 | 39.4 | mean_of_3 | ok |
| A03 | 2026-09-15 | 37.9 | mean_of_3 | ok |
| A03 | 2026-09-22 | 38.8 | mean_of_3 | ok |
| A03 | 2026-09-29 | NA | mean_of_3 | not_measured |
| A03 | 2026-10-06 | 37.2 | mean_of_3 | ok |

**Excel.** Put the inputs in `B1:B4`, then the results in `B6:B12`:

```text
B1: A03
B2: 2026-09-01
B3: 2026-09-30
B4: 1.1
B6 (baseline mean):  =AVERAGEIFS(cmj[jump_height_cm],cmj[athlete_id],B1,cmj[test_date],">="&B2,cmj[test_date],"<="&B3,cmj[status],"ok")
B7 (n):              =COUNTIFS(cmj[athlete_id],B1,cmj[test_date],">="&B2,cmj[test_date],"<="&B3,cmj[status],"ok")
B8 (latest date):    =MAXIFS(cmj[test_date],cmj[athlete_id],B1,cmj[test_date],">"&B3,cmj[status],"ok")
B9 (latest value):   =AVERAGEIFS(cmj[jump_height_cm],cmj[athlete_id],B1,cmj[test_date],B8,cmj[status],"ok")
B10 (change):        =B9-B6
B11 (noise band):    =1.96*B4*SQRT(1+1/B7)
B12:                 =IF(ABS(B10)<B11,"inside the noise band","beyond the noise band")
```

Enter `B2` and `B3` as dates, not text. The `">"&B3` test keeps the latest value after the baseline window, so the new value is never part of its own baseline. `MAXIFS` needs Excel 2019 or later. `UNIQUE`, `FILTER`, and `SORTBY` need Excel 2021 or later, or Excel for Microsoft 365.

**Google Sheets.** Use `QUERY` for the baseline mean and `n`. Column B must hold real dates, not text, for the `date` tests to work:

```text
=QUERY(cmj!A1:E,"select avg(C), count(C) where A = 'A03' and B >= date '2026-09-01' and B <= date '2026-09-30' and E = 'ok'",1)
```

**SQL.**

```sql
WITH base AS (
  SELECT AVG(jump_height_cm) AS baseline_cm, COUNT(jump_height_cm) AS n
  FROM cmj
  WHERE athlete_id = 'A03' AND status = 'ok'
    AND test_date BETWEEN '2026-09-01' AND '2026-09-30'
),
latest AS (
  SELECT test_date, jump_height_cm AS latest_cm
  FROM cmj
  WHERE athlete_id = 'A03' AND status = 'ok'
    AND test_date > '2026-09-30'
  ORDER BY test_date DESC LIMIT 1
)
SELECT latest.test_date, latest_cm,
       ROUND(baseline_cm, 3)                      AS baseline_cm,
       n,
       ROUND(latest_cm - baseline_cm, 3)          AS change_cm,
       ROUND(1.96 * 1.1 * SQRT(1 + 1.0 / n), 3)   AS band_cm
FROM base, latest;
```

**Answer.**

Sam (A03) jumped 37.2 cm on 2026-10-06, 1.9 cm below the September mean of 39.1 cm, from 4 tests between 2026-09-01 and 2026-09-22. The change is inside the noise band of ±2.4 cm, so it may be measurement error. The 2026-09-29 test was not done.

| Item | Value |
|---|---|
| Latest CMJ height, 2026-10-06 | 37.2 cm |
| September mean, n = 4 | 39.075 cm |
| Change | −1.875 cm |
| Noise band, 1.96 × 1.1 × √(1 + 1/4) | ±2.410 cm |
| Result | Inside the noise band |

Measure: CMJ height, mean of 3 trials, takeoff velocity method, from the `force-plate` skill. TE: 1.1 cm, from the coach's same-day retest of 20 athletes in the squad. The band uses 1.96. With a TE from few athletes, use t at the TE study's degrees of freedom instead, which widens the band, as the `monitoring-statistics` skill describes. The band adds the variance of the new value to the variance of the baseline mean, and the 95 percent level is a choice. It assumes the true score did not change, errors are independent, and TE is the same for every athlete and value.

The window changes the baseline. With the 30 days before the latest test, 2026-09-06 to 2026-10-05, the baseline is 38.7 cm from 3 tests, the change is −1.5 cm, and the band is ±2.49 cm. That change is also inside the band.

### Example 3: who missed the most

> Who missed the most HSR this week?

HSR is the coach's short form for high-speed running distance.

The coach asks on Sunday 2026-10-04.

**Ask back.** Ask in one message:

- "Missed sessions, or less high-speed running than usual, or less than planned?" The coach says less than usual.
- "This training week, Monday 2026-09-28 to today, Sunday 2026-10-04?" The coach says yes.
- "Usual as the mean of the previous 4 complete training weeks?" The coach says yes. The 4 weeks are the coach's choice.
- "Most in metres, or most as a percent of usual?" The coach asks to see both.

**Restated query.** For all 6 athletes, compare high-speed running distance (m) in the training week 2026-09-28 to 2026-10-04 with each athlete's mean of the 4 previous complete training weeks, 2026-08-31 to 2026-09-27. Show the change in metres and as a percent of usual. Sort by percent of usual, and list incomplete weeks last.

This week's totals are the sums of the four sessions in Example 1.

**Data.** The `weekly` table has one row for each athlete and training week. `week_start` is the Monday. `sessions_expected` is 4 in every week.

| athlete_id | 2026-08-31 | 2026-09-07 | 2026-09-14 | 2026-09-21 | 2026-09-28 | Sessions with data, week of 2026-09-28 |
|---|---|---|---|---|---|---|
| A01 | 2400 | 2550 | 2300 | 2480 | 2375 | 4 |
| A02 | 2900 | 2750 | 3010 | 2880 | 2557 | 4 |
| A03 | 1800 | 1950 | 1700 | 1880 | 1505 | 3 |
| A04 | 2600 | 2500 | 2700 | 2650 | 2288 | 4 |
| A05 | 2200 | 2350 | 2280 | 2300 | 1320 | 2 |
| A06 | 2500 | 2450 | 2600 | 2550 | 2436 | 4 |

All 4 baseline weeks are complete for every athlete. This table is shown wide to save space. Store it long, one row for each athlete and week.

**Excel.** Add a column `complete` to `weekly`, `=[@sessions_with_data]=[@sessions_expected]`. Put the roster IDs in `A2:A7`, then fill `B2:G2` down:

```text
B2 (usual, m):           =AVERAGEIFS(weekly[hsr_m],weekly[athlete_id],A2,weekly[week_start],">="&DATE(2026,8,31),weekly[week_start],"<="&DATE(2026,9,21),weekly[complete],TRUE)
C2 (this week, m):       =SUMIFS(weekly[hsr_m],weekly[athlete_id],A2,weekly[week_start],DATE(2026,9,28))
D2 (sessions with data): =SUMIFS(weekly[sessions_with_data],weekly[athlete_id],A2,weekly[week_start],DATE(2026,9,28))
E2 (change, m):          =C2-B2
F2 (% of usual):         =C2/B2*100
G2 (note):               =IF(D2<4,"incomplete week","")
```

`SUMIFS` returns 0 for an athlete with no row this week. Check `D2` before you read `C2`. Sort with complete weeks first, by percent of usual:

```text
=SORTBY(A2:G7,G2:G7="incomplete week",1,F2:F7,1)
```

**Google Sheets.** Use `QUERY` for each athlete's usual week. The `D = E` test keeps complete weeks only:

```text
=QUERY(weekly!A1:E,"select A, avg(C) where B >= date '2026-08-31' and B <= date '2026-09-21' and D = E group by A label avg(C) 'usual_m'",1)
```

This `QUERY` leaves out any athlete with no complete baseline week. Join the result back to the roster.

**SQL.**

```sql
WITH usual AS (
  SELECT athlete_id, AVG(hsr_m) AS usual_m, COUNT(*) AS n_weeks
  FROM weekly
  WHERE week_start BETWEEN '2026-08-31' AND '2026-09-21'
    AND sessions_with_data = sessions_expected
  GROUP BY athlete_id
)
SELECT r.athlete_id, w.hsr_m AS this_week_m, w.sessions_with_data,
       u.usual_m, u.n_weeks,
       ROUND(w.hsr_m - u.usual_m, 1)               AS change_m,
       ROUND(100.0 * w.hsr_m / u.usual_m, 1)       AS pct_of_usual,
       CASE WHEN w.athlete_id IS NULL THEN 'no data this week'
            WHEN w.sessions_with_data < w.sessions_expected
            THEN 'incomplete week' ELSE '' END      AS note
FROM roster r
LEFT JOIN weekly w ON w.athlete_id = r.athlete_id AND w.week_start = '2026-09-28'
LEFT JOIN usual u  ON u.athlete_id = r.athlete_id
ORDER BY COALESCE(w.sessions_with_data < w.sessions_expected, 1), pct_of_usual;
```

An athlete with no row this week gives `NULL` for the incomplete test, and SQLite sorts `NULL` first. `COALESCE(..., 1)` treats that athlete as an incomplete week, so the row is listed with the incomplete weeks. The `note` column labels that row `no data this week`.

**Answer.**

In the training week 2026-09-28 to 2026-10-04, all 6 athletes have data, and 4 have every session recorded. A04 (87.6% of usual, −324.5 m) and A02 (88.6% of usual, −328.0 m) were furthest below their own usual week among those 4, and the data does not single out one: A04 is lower in percent and A02 in metres, by about 1 percentage point and 3.5 m. A03 (3 of 4 sessions, device failure) and A05 (2 of 4, excused) have incomplete weeks, and weekly totals have no typical error, so I cannot judge any drop against noise.

| athlete_id | This week (m) | Usual week (m), n = 4 | Change (m) | % of usual | Sessions with data | Note |
|---|---|---|---|---|---|---|
| A04 | 2288 | 2612.5 | −324.5 | 87.6 | 4 of 4 | |
| A02 | 2557 | 2885.0 | −328.0 | 88.6 | 4 of 4 | |
| A06 | 2436 | 2525.0 | −89.0 | 96.5 | 4 of 4 | |
| A01 | 2375 | 2432.5 | −57.5 | 97.6 | 4 of 4 | |
| A05 | 1320 | 2282.5 | −962.5 | 57.8 | 2 of 4 | incomplete week, excused |
| A03 | 1505 | 1832.5 | −327.5 | 82.1 | 3 of 4 | incomplete week, device failure |

Sorted by percent of usual, not by ability. Incomplete weeks are listed last, because a missing session lowers the total. Usual: mean of 4 complete training weeks, 2026-08-31 to 2026-09-27, the coach's choice. Measure: weekly high-speed running distance, in m, at the export's speed setting, from the `gps-running-load` and `load-and-wellness` skills. A weekly total is not a test, so it has no test-retest typical error. The `monitoring-statistics` skill's usual-variation band needs at least 10 stable baseline values, and each athlete has 4.

## Common mistakes

These are the mistakes these examples guard against:

- Letting `QUERY` drop A04 in Example 1, so an athlete with no sessions over the line disappears.
- Leaving out the status test in `FILTER`, so `NA` rows count as over the line.
- Counting A06's 600 m as over the line when the coach meant above.
- Taking "last month" as 30 days in Example 2 without asking. It changes the baseline from 39.075 cm to 38.7 cm.
- Ranking A05 first in Example 3 because the week is 42% down, when two sessions are missing.
- Naming one athlete as "most" in Example 3 when metres and percent disagree.

## Example request

> Who's been over 600 m of high-speed running in the last four sessions?

## Check the result

Run these checks on each example:

- Example 1: add the sessions with data across athletes. Confirm 4 + 4 + 3 + 4 + 2 + 4 = 21, out of 6 × 4 = 24 expected.
- Example 2: recompute the baseline by hand. (40.2 + 39.4 + 37.9 + 38.8) / 4 = 39.075 cm. Then 37.2 − 39.075 = −1.875 cm.
- Example 3: recompute A04 by hand. (2600 + 2500 + 2700 + 2650) / 4 = 2612.5 m, and 2288 / 2612.5 × 100 = 87.6%.

## Sources

The data in this file is synthetic. The noise band comes from the `monitoring-statistics` skill, which holds its sources. The Monday-to-Sunday training week follows the `load-and-wellness` skill's session RPE load reference.
