#!/usr/bin/env python3
"""Make the synthetic sample data for the dashboards.

Every athlete, name, and value in the output is made up. The data follows the
athlete, session, and measure tables from the `ams-data-setup` skill in the
Custom AMS Skills repository.

Run it from the dashboards folder:

    python3 pipeline/make_sample_data.py

It writes these files to data/sample/:

    athletes.csv            One row for each athlete
    sessions.csv            One row for each session, plus a `none` row
    measures.csv            One row for each athlete, date, session, measure, side, and trial
    availability.csv        One row for each athlete and day: full, modified, or out
    measure_dictionary.csv  One row for each measure name
    import_log.csv          One row for each import
    settings.csv            Choices the user makes, such as baseline windows

The seed is fixed, so every run gives the same files.
"""

from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20261005
START = date(2026, 7, 6)  # A Monday
END = date(2026, 10, 3)  # A Saturday match day, the last day of the sample
FIRST_MATCH = date(2026, 8, 22)
RETEST_DAYS = (date(2026, 7, 7), date(2026, 7, 9))  # Preseason retest for typical error
OUT = Path(__file__).resolve().parent.parent / "data" / "sample"

GROUPS = ["Defenders"] * 9 + ["Midfielders"] * 9 + ["Forwards"] * 7 + ["Goalkeepers"] * 3
WELLNESS_ITEMS = ["sleep_quality", "fatigue", "soreness", "stress", "mood"]


def daterange(a, b):
    d = a
    while d <= b:
        yield d
        d += timedelta(days=1)


def make_athletes():
    rows = []
    for i, group in enumerate(GROUPS, start=1):
        start = START
        if i == 26:
            start = date(2026, 8, 10)  # Joins late, so has a short baseline
        rows.append({
            "athlete_id": f"A{i:04d}",
            "name": f"Athlete {i:02d}",
            "group": group,
            "email": f"a{i:04d}@example.edu",
            "start_date": start.isoformat(),
            "end_date": "NA",
            "status": "active",
        })
    return pd.DataFrame(rows)


def week_phase(d):
    """Return a load multiplier for the training phase of this day."""
    week = (d - START).days // 7 + 1
    if week <= 2:
        return 0.75  # Early preseason
    if week == 3:
        return 1.25  # Preseason camp
    if week <= 6:
        return 1.0
    return 0.95  # In season


def make_sessions():
    rows = [{"session_id": "none", "session_date": "NA", "start_time_local": "NA",
             "time_zone": "NA", "session_type": "none", "group": "NA"}]
    n = 0

    def add(d, kind, time):
        nonlocal n
        n += 1
        rows.append({"session_id": f"S{n:04d}", "session_date": d.isoformat(),
                     "start_time_local": time, "time_zone": "America/Chicago",
                     "session_type": kind, "group": "squad"})

    for d in daterange(START, END):
        wd = d.weekday()  # Monday is 0
        if wd == 6:
            continue  # Sunday off
        if wd == 5 and d >= FIRST_MATCH:
            add(d, "match", "19:00")
            continue
        if wd == 5:
            continue  # Saturday off in preseason
        if wd == 1 or d in RETEST_DAYS:
            add(d, "test", "08:00")
        add(d, "practice", "15:30")
        if wd in (0, 3):
            add(d, "gym", "11:00")
    return pd.DataFrame(rows)


def make_availability(athletes, rng):
    rows = []
    for a in athletes.itertuples():
        start = date.fromisoformat(a.start_date)
        for d in daterange(start, END):
            status = "full"
            if a.athlete_id == "A0019" and date(2026, 9, 1) <= d <= date(2026, 9, 12):
                status = "out"
            elif a.athlete_id == "A0019" and date(2026, 9, 13) <= d <= date(2026, 9, 19):
                status = "modified"
            elif a.athlete_id == "A0004" and date(2026, 8, 18) <= d <= date(2026, 8, 20):
                status = "out"
            elif rng.random() < 0.01:
                status = "modified"
            rows.append({"athlete_id": a.athlete_id, "date": d.isoformat(), "availability": status})
    return pd.DataFrame(rows)


def make_measures(athletes, sessions, availability, rng):
    avail = {(r.athlete_id, r.date): r.availability for r in availability.itertuples()}
    rows = []

    def add(aid, d, sid, name, value, unit, source, trial=1, status="ok", rec="NA"):
        rows.append({
            "athlete_id": aid, "measure_date": d.isoformat(), "session_id": sid,
            "measure_name": name, "side": "bilateral", "trial_number": trial,
            "value": "NA" if value is None else value, "unit": unit, "status": status,
            "source": source, "source_record_id": rec,
            "imported_on": (d + timedelta(days=1)).isoformat(),
        })

    # Each athlete has a stable "true" level for jump height and wellness.
    profile = {}
    for a in athletes.itertuples():
        profile[a.athlete_id] = {
            "cmj": rng.normal(36.0, 4.0) if a.group != "Goalkeepers" else rng.normal(38.0, 3.0),
            "well": rng.normal(3.8, 0.3),
            "run": rng.normal(1.0, 0.08) if a.group != "Goalkeepers" else 0.45,
            "start": date.fromisoformat(a.start_date),
        }

    test_counter = 0
    sess = sessions[sessions.session_id != "none"].copy()
    sess["d"] = sess.session_date.map(date.fromisoformat)

    for d in daterange(START, END):
        day_sessions = sess[sess.d == d]
        for a in athletes.itertuples():
            p = profile[a.athlete_id]
            if d < p["start"]:
                continue
            status = avail[(a.athlete_id, d.isoformat())]

            # Morning wellness form, Monday to Saturday. About 8 percent missed.
            if d.weekday() != 6 and rng.random() > 0.08:
                dip = 0.0
                if a.athlete_id == "A0012" and date(2026, 9, 21) <= d <= date(2026, 9, 26):
                    dip = 1.6  # A run of poor answers late in September
                if d.weekday() == 0 and d >= FIRST_MATCH:
                    dip += 0.4  # The morning after the weekend match block
                for item in WELLNESS_ITEMS:
                    x = p["well"] - dip + rng.normal(0, 0.55)
                    if item == "soreness":
                        x -= 0.2
                    add(a.athlete_id, d, "none", item, int(np.clip(round(x), 1, 5)), "points", "wellness_form")

            if status == "out":
                continue

            for s in day_sessions.itertuples():
                kind = s.session_type
                if kind == "test":
                    # Countermovement jump, 3 trials. A0007 declines from mid September.
                    level = p["cmj"]
                    if a.athlete_id == "A0007" and d >= date(2026, 9, 15):
                        level -= 3.5
                    if a.athlete_id == "A0021" and d >= date(2026, 9, 1):
                        level += 2.5  # A real gain after a strength block
                    day_effect = rng.normal(0, 0.6)
                    for t in (1, 2, 3):
                        test_counter += 1
                        if rng.random() < 0.01:
                            add(a.athlete_id, d, s.session_id, "cmj_jump_height", None, "cm", "force_plate",
                                trial=t, status="device_failure")
                            continue
                        v = round(level + day_effect + rng.normal(0, 0.9), 1)
                        add(a.athlete_id, d, s.session_id, "cmj_jump_height", v, "cm", "force_plate",
                            trial=t, rec=f"T-{test_counter:06d}")
                    continue

                if kind == "practice":
                    base_min = 90 if d.weekday() != 4 else 60  # Friday is a short session
                    minutes = base_min if status == "full" else 45
                    rpe = 5.0 * week_phase(d) + (1.0 if d.weekday() == 1 else 0) - (1.5 if d.weekday() == 4 else 0)
                    dist = 6200 * week_phase(d) * p["run"] * minutes / 90
                elif kind == "match":
                    minutes = int(np.clip(rng.normal(80, 15), 15, 95))
                    if a.group == "Goalkeepers" and a.athlete_id != "A0026":
                        minutes = 90 if a.athlete_id == "A0028" else 0
                    if status == "modified":
                        minutes = 0
                    if minutes == 0:
                        continue
                    rpe = 7.5
                    dist = 10500 * p["run"] * minutes / 90
                else:  # gym
                    minutes = 50 if status == "full" else 30
                    rpe = 4.5 * week_phase(d)
                    dist = None

                # Session RPE about 30 minutes after the session. About 1 percent missed.
                if rng.random() > 0.012:
                    r = int(np.clip(round(rpe + rng.normal(0, 0.8)), 1, 10))
                    add(a.athlete_id, d, s.session_id, "session_rpe_cr10", r, "au", "rpe_form")
                add(a.athlete_id, d, s.session_id, "session_duration", minutes, "min", "session_log")

                if dist is not None:
                    if rng.random() < 0.02:
                        for m, unit in (("total_distance", "m"), ("hsr_distance", "m"), ("accelerations", "count")):
                            add(a.athlete_id, d, s.session_id, m, None, unit, "gps", status="device_failure")
                        continue
                    td = dist * rng.normal(1, 0.06)
                    hsr = td * (0.09 if kind == "match" else 0.06) * rng.normal(1, 0.15)
                    acc = td / 160 * rng.normal(1, 0.12)
                    rec = f"G-{s.session_id}-{a.athlete_id}"
                    add(a.athlete_id, d, s.session_id, "total_distance", round(td), "m", "gps", rec=rec)
                    add(a.athlete_id, d, s.session_id, "hsr_distance", round(hsr), "m", "gps", rec=rec)
                    add(a.athlete_id, d, s.session_id, "accelerations", int(round(acc)), "count", "gps", rec=rec)

    return pd.DataFrame(rows)


def make_dictionary():
    rows = [
        ("sleep_quality", "points", "Morning answer: how well did you sleep? 1 very poorly to 5 very well. Higher is better.", "single item, 1 to 5", "wellness_form"),
        ("fatigue", "points", "Morning answer: how fresh do you feel? 1 very tired to 5 very fresh. Higher is better.", "single item, 1 to 5", "wellness_form"),
        ("soreness", "points", "Morning answer: how do your muscles feel? 1 very sore to 5 not sore. Higher is better. Routine soreness only. Report pain to the medical team.", "single item, 1 to 5", "wellness_form"),
        ("stress", "points", "Morning answer: how relaxed do you feel? 1 very stressed to 5 very relaxed. Higher is better.", "single item, 1 to 5", "wellness_form"),
        ("mood", "points", "Morning answer: how is your mood? 1 very low to 5 very good. Higher is better.", "single item, 1 to 5", "wellness_form"),
        ("session_rpe_cr10", "au", "Rating of the whole session on the CR-10 scale, about 30 minutes after it ends.", "Foster session RPE", "rpe_form"),
        ("session_duration", "min", "Minutes the athlete took part in the session.", "session log", "session_log"),
        ("total_distance", "m", "Distance covered in the session.", "vendor export", "gps"),
        ("hsr_distance", "m", "Distance above the high-speed threshold set in the device software.", "vendor export, threshold set by user", "gps"),
        ("accelerations", "count", "Accelerations above the threshold set in the device software.", "vendor export, threshold set by user", "gps"),
        ("cmj_jump_height", "cm", "Countermovement jump height, hands on hips, one value for each trial.", "takeoff velocity method", "force_plate"),
    ]
    df = pd.DataFrame(rows, columns=["measure_name", "unit", "definition", "formula_variant", "source"])
    df["measure_date_rule"] = "local date of the session or form"
    df["status_codes"] = "ok; device_failure; held"
    return df


def make_import_log(measures):
    m = measures.copy()
    log = (m.groupby(["source", "imported_on"]).size().reset_index(name="rows_imported"))
    log = log.rename(columns={"imported_on": "import_date"})
    log["import_time_local"] = log.source.map({
        "wellness_form": "06:20", "rpe_form": "06:20", "session_log": "06:20",
        "gps": "07:05", "force_plate": "07:10"}).fillna("06:20")
    log["result"] = "ok"
    # One failed GPS import: the file arrived late, and a second run picked it up.
    fail = log[(log.source == "gps") & (log.import_date == "2026-09-09")]
    if len(fail):
        extra = fail.copy()
        extra["rows_imported"] = 0
        extra["import_time_local"] = "07:05"
        extra["result"] = "failed: no new file"
        log.loc[fail.index, "import_time_local"] = "09:40"
        log = pd.concat([log, extra])
    log = log.sort_values(["import_date", "import_time_local", "source"]).reset_index(drop=True)
    log.insert(0, "import_id", [f"I{i:05d}" for i in range(1, len(log) + 1)])
    return log[["import_id", "source", "import_date", "import_time_local", "rows_imported", "result"]]


def make_settings():
    rows = [
        ("load_measure", "srpe_load_au", "Daily load measure for acute and chronic load."),
        ("acute_window_days", "7", "Acute window in days. A convention, not a validated value."),
        ("chronic_window_days", "28", "Chronic window in days. A convention, not a validated value."),
        ("acwr_variant", "rolling_coupled", "ACWR variant. ACWR does not predict injury."),
        ("wellness_baseline_window_days", "28", "Days before today that the wellness baseline looks back."),
        ("wellness_min_baseline_answers", "14", "Fewest answers in the window before a z-score is shown."),
        ("wellness_review_z", "-2.0", "Example only. The total wellness z-score at or below which staff review the athlete. Set your own value. No published cut point exists."),
        ("cmj_trial_summary", "mean_of_3", "One value for each test day: the mean of the ok trials."),
        ("cmj_baseline_start", "2026-07-07", "First day of the fixed baseline period for jump height."),
        ("cmj_baseline_end", "2026-07-28", "Last day of the fixed baseline period for jump height."),
        ("cmj_min_baseline_tests", "3", "Fewest baseline test days before a change state is shown."),
        ("cmj_direction", "drop", "Direction of change that matters for jump height."),
        ("retest_day_1", RETEST_DAYS[0].isoformat(), "First day of the preseason retest used for typical error."),
        ("retest_day_2", RETEST_DAYS[1].isoformat(), "Second day of the preseason retest used for typical error."),
    ]
    return pd.DataFrame(rows, columns=["setting", "value", "meaning"])


def main():
    rng = np.random.default_rng(SEED)
    OUT.mkdir(parents=True, exist_ok=True)
    athletes = make_athletes()
    sessions = make_sessions()
    availability = make_availability(athletes, rng)
    measures = make_measures(athletes, sessions, availability, rng)
    dictionary = make_dictionary()
    log = make_import_log(measures)
    settings = make_settings()

    athletes.to_csv(OUT / "athletes.csv", index=False)
    sessions.to_csv(OUT / "sessions.csv", index=False)
    measures.to_csv(OUT / "measures.csv", index=False)
    availability.to_csv(OUT / "availability.csv", index=False)
    dictionary.to_csv(OUT / "measure_dictionary.csv", index=False)
    log.to_csv(OUT / "import_log.csv", index=False)
    settings.to_csv(OUT / "settings.csv", index=False)
    for name, df in [("athletes", athletes), ("sessions", sessions), ("measures", measures),
                     ("availability", availability), ("import_log", log)]:
        print(f"{name}: {len(df)} rows")


if __name__ == "__main__":
    main()
