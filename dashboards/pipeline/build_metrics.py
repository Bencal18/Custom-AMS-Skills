#!/usr/bin/env python3
"""Build the metric layer from the clean tables.

This is the one place where every metric is calculated. Power BI and Tableau
read the files it writes and only display them.

Run it from the dashboards folder:

    python3 pipeline/build_metrics.py
    python3 pipeline/build_metrics.py --input data/sample --output data/metrics

Inputs (in --input): athletes.csv, measures.csv, availability.csv,
settings.csv, import_log.csv.

Outputs (in --output):

    athlete_day.csv       One row for each athlete and calendar day on the roster
    wellness_scores.csv   One row for each athlete, day, and wellness item, plus the total
    test_results.csv      One row for each athlete and jump test day
    weekly_load.csv       One row for each athlete and week
    reliability.csv       Typical error and smallest worthwhile change for each tested measure
    test_day_summary.csv  Flags found and flags expected by chance for each test day
    data_quality.csv      Forms, ratings, and device failures for each day
    profile_series.csv    One row for each athlete, day, and chart line, for the profile charts
    dates.csv             One row for each calendar day

It also copies athletes.csv, settings.csv, and import_log.csv unchanged, so
the dashboards read one folder.

The formulas follow the Custom AMS Skills repository: session RPE load,
rolling coupled ACWR, wellness z-score, and the change-versus-noise states.
"""

import argparse
from math import sqrt
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
WELLNESS_ITEMS = ["sleep_quality", "fatigue", "soreness", "stress", "mood"]
STATE_WORDING = {
    "No flag": "Within measurement error",
    "Noted": "Larger than measurement error; may or may not be worthwhile",
    "Flagged": "Larger than measurement error; likely range beyond the smallest worthwhile change; worth a conversation",
    "No data": "Not enough data",
    "Baseline": "Baseline test",
}
ACWR_NOTE = "ACWR describes how recent load compares with longer-term load. It does not predict injury."


def read(folder, name):
    """Read a CSV with every column as text, so IDs keep leading zeros and NA stays visible."""
    return pd.read_csv(Path(folder) / f"{name}.csv", dtype=str, keep_default_na=False)


def to_number(series):
    """Turn text values into numbers. The code NA becomes a true missing value."""
    return pd.to_numeric(series.replace("NA", np.nan), errors="raise")


def roster_days(athletes, last_day):
    """One row for each athlete and each day between start_date and end_date."""
    rows = []
    for a in athletes.itertuples():
        start = pd.Timestamp(a.start_date)
        end = pd.Timestamp(last_day) if a.end_date == "NA" else pd.Timestamp(a.end_date)
        for d in pd.date_range(start, end, freq="D"):
            rows.append((a.athlete_id, d))
    return pd.DataFrame(rows, columns=["athlete_id", "date"])


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------

def check_unique(m, keys, what):
    """Stop when two ok rows share a key. The table layout reference says not to pick one."""
    dup = m[m.duplicated(keys, keep=False)]
    if len(dup):
        raise ValueError(f"Two or more ok rows share a key in {what}. Mark them held and resolve them first:\n"
                         + dup[keys].head(10).to_string(index=False))


def session_loads(measures):
    """Session RPE load = rpe_cr10 x duration_min, one row for each athlete and session.

    A session with either a rating or a duration counts. If either is missing or
    not ok, the session load is missing, not 0.
    """
    m = measures[measures.measure_name.isin(["session_rpe_cr10", "session_duration"])].copy()
    m["value"] = to_number(m.value)
    m.loc[m.status != "ok", "value"] = np.nan
    keys = ["athlete_id", "measure_date", "session_id", "measure_name"]
    check_unique(m[m.status == "ok"], keys, "session RPE and duration")
    m = m.sort_values("status").drop_duplicates(keys)  # One row per key; an ok row sorts first.
    wide = m.pivot(index=["athlete_id", "measure_date", "session_id"], columns="measure_name",
                   values="value").reset_index()
    for col in ["session_rpe_cr10", "session_duration"]:
        if col not in wide:
            wide[col] = np.nan
    wide["srpe_load_au"] = wide.session_rpe_cr10 * wide.session_duration
    wide["date"] = pd.to_datetime(wide.measure_date)
    return wide[["athlete_id", "date", "session_id", "session_rpe_cr10", "session_duration", "srpe_load_au"]]


def daily_load(roster, sessions_load, availability):
    """Daily session RPE load on a full calendar.

    Rest days and days marked out with no session are 0. A day with a session but
    a missing rating is missing.
    """
    day = (sessions_load.groupby(["athlete_id", "date"])
           .agg(srpe_load_au=("srpe_load_au", lambda s: s.sum() if s.notna().all() else np.nan),
                sessions=("session_id", "count"))
           .reset_index())
    out = roster.merge(day, on=["athlete_id", "date"], how="left")
    out["sessions"] = out.sessions.fillna(0).astype(int)
    out.loc[out.sessions == 0, "srpe_load_au"] = 0.0
    av = availability.copy()
    av["date"] = pd.to_datetime(av.date)
    out = out.merge(av, on=["athlete_id", "date"], how="left")
    if out.duplicated(["athlete_id", "date"]).any():
        raise ValueError("More than one row for an athlete and day in the daily load table.")
    return out


def rolling_acwr(daily, acute_days=7, chronic_days=28):
    """Rolling coupled ACWR from mean daily load.

    A window with any missing day gives a missing mean. No ratio before the
    chronic window is full. This follows the acwr reference file.
    """
    out = []
    for aid, g in daily.sort_values("date").groupby("athlete_id", sort=False):
        g = g.copy()
        s = g.srpe_load_au
        g["acute_load_au"] = s.rolling(acute_days, min_periods=acute_days).mean()
        g["chronic_load_au"] = s.rolling(chronic_days, min_periods=chronic_days).mean()
        ratio = g.acute_load_au / g.chronic_load_au
        ratio[g.chronic_load_au == 0] = np.nan
        g["acwr_coupled"] = ratio
        out.append(g)
    return pd.concat(out)


def external_daily(measures, roster):
    """Daily totals of distance and high-speed running.

    A day with no GPS session is 0 m. A day with any failed or held session is missing.
    """
    m = measures[measures.measure_name.isin(["total_distance", "hsr_distance"])].copy()
    m["value"] = to_number(m.value)
    m.loc[m.status != "ok", "value"] = np.nan
    m["date"] = pd.to_datetime(m.measure_date)
    agg = (m.groupby(["athlete_id", "date", "measure_name"])
           .value.apply(lambda s: s.sum() if s.notna().all() else np.nan)
           .unstack().reset_index())
    agg = agg.rename(columns={"total_distance": "distance_m", "hsr_distance": "hsr_m"})
    out = roster.merge(agg, on=["athlete_id", "date"], how="left")
    has_gps = out.set_index(["athlete_id", "date"]).index.isin(
        m.set_index(["athlete_id", "date"]).index)
    out.loc[~has_gps, ["distance_m", "hsr_m"]] = 0.0
    return out


def weekly_load(daily):
    """Weekly totals, Monday to Sunday, with the number of complete days."""
    d = daily.copy()
    d["week_start"] = d.date - pd.to_timedelta(d.date.dt.weekday, unit="D")
    g = d.groupby(["athlete_id", "week_start"])
    w = g.agg(days_on_roster=("date", "count"),
              days_complete=("srpe_load_au", lambda s: int(s.notna().sum())),
              srpe_week_au=("srpe_load_au", "sum"),
              distance_week_m=("distance_m", lambda s: s.sum() if s.notna().all() else np.nan),
              hsr_week_m=("hsr_m", lambda s: s.sum() if s.notna().all() else np.nan),
              distance_days_missing=("distance_m", lambda s: int(s.isna().sum())),
              days_out=("availability", lambda s: int((s == "out").sum())),
              days_modified=("availability", lambda s: int((s == "modified").sum()))).reset_index()
    w["week_complete"] = np.where((w.days_complete == 7) & (w.days_on_roster == 7), "yes", "no")
    w["days_label"] = w.days_complete.astype(str) + " of 7 days"
    w["week_label"] = [f"{t:,.0f} AU, {d}" for t, d in zip(w.srpe_week_au, w.days_label)]
    return w


# ---------------------------------------------------------------------------
# Wellness
# ---------------------------------------------------------------------------

def wellness_scores(measures, window_days=28, min_answers=14):
    """Wellness z-score for each item and for the daily total.

    Every item is already scored so that higher is better. The baseline is the
    athlete's previous answers in the window before today, excluding today.
    """
    m = measures[measures.measure_name.isin(WELLNESS_ITEMS) & (measures.status == "ok")].copy()
    m["answer"] = to_number(m.value)
    m["date"] = pd.to_datetime(m.measure_date)
    check_unique(m, ["athlete_id", "date", "measure_name"], "wellness answers")
    wide = m.pivot(index=["athlete_id", "date"], columns="measure_name", values="answer").reset_index()
    for item in WELLNESS_ITEMS:
        if item not in wide:
            wide[item] = np.nan
    wide["total"] = wide[WELLNESS_ITEMS].sum(axis=1, min_count=len(WELLNESS_ITEMS))
    long = wide.melt(id_vars=["athlete_id", "date"], value_vars=WELLNESS_ITEMS + ["total"],
                     var_name="item", value_name="answer").dropna(subset=["answer"])

    rows = []
    for (aid, item), g in long.sort_values("date").groupby(["athlete_id", "item"], sort=False):
        dates = g.date.to_numpy()
        vals = g.answer.to_numpy()
        for i in range(len(g)):
            today = dates[i]
            lo = today - np.timedelta64(window_days, "D")
            mask = (dates < today) & (dates >= lo)
            base = vals[mask]
            n = len(base)
            rec = {"athlete_id": aid, "date": pd.Timestamp(today), "item": item,
                   "answer": vals[i], "baseline_n": n, "baseline_mean": np.nan,
                   "baseline_sd": np.nan, "change_points": np.nan, "z": np.nan}
            if n < min_answers:
                rec["status"] = "baseline too short"
            else:
                mean = base.mean()
                sd = base.std(ddof=1)
                rec.update(baseline_mean=mean, baseline_sd=sd, change_points=vals[i] - mean)
                if sd == 0:
                    rec["status"] = "no variation in baseline"
                else:
                    rec["z"] = (vals[i] - mean) / sd
                    rec["status"] = "ok"
            rows.append(rec)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Jump tests and change versus noise
# ---------------------------------------------------------------------------

def test_day_values(measures, measure="cmj_jump_height", trials_needed=3):
    """One value for each athlete and test day: the mean of the ok trials.

    A day with fewer ok trials than the summary rule needs, such as 3 for mean_of_3,
    has no value. The typical error must use the same summary as the values compared.
    """
    m = measures[(measures.measure_name == measure)].copy()
    m["value"] = to_number(m.value)
    m["date"] = pd.to_datetime(m.measure_date)
    ok = m[(m.status == "ok") & m.value.notna()]
    g = ok.groupby(["athlete_id", "date"]).value.agg(["mean", "count"]).reset_index()
    g = g.rename(columns={"mean": "value", "count": "trials_ok"})
    attempted = m.groupby(["athlete_id", "date"]).size().reset_index(name="trials_attempted")
    out = attempted.merge(g, on=["athlete_id", "date"], how="left")
    out["trials_ok"] = out.trials_ok.fillna(0).astype(int)
    out.loc[out.trials_ok < trials_needed, "value"] = np.nan
    out["measure_name"] = measure
    return out


def typical_error(values, day1, day2):
    """TE from two retest days: SD of the differences divided by sqrt(2)."""
    a = values[values.date == pd.Timestamp(day1)].set_index("athlete_id").value
    b = values[values.date == pd.Timestamp(day2)].set_index("athlete_id").value
    diff = (b - a).dropna()
    n = len(diff)
    te = diff.std(ddof=1) / sqrt(2)
    df = n - 1
    multiplier = float(stats.t.ppf(0.975, df))
    return te, df, multiplier, n


def change_state(change, band, swc, direction):
    """The four states from the flagging-change reference, for one direction."""
    if pd.isna(change) or pd.isna(band) or pd.isna(swc):
        return "No data"
    if abs(change) <= band:
        return "No flag"
    if direction == "drop" and change + band < -swc:
        return "Flagged"
    if direction == "rise" and change - band > swc:
        return "Flagged"
    return "Noted"


def athlete_sentence(state, change):
    """Plain words for the athlete's own view. No colors, no ranks."""
    if state == "Baseline":
        return "This test is part of your baseline."
    if state == "No data":
        return "There is not enough data yet to compare this test with your usual range."
    if state == "No flag":
        return "Your jump height on this test was within your usual range."
    where = "below" if change < 0 else "above"
    if state == "Flagged":
        return f"Your jump height on this test was {where} your usual range. It is worth a conversation with your coach."
    return f"Your jump height on this test was {where} your usual range."


def test_results(values, settings):
    s = settings
    base_lo, base_hi = pd.Timestamp(s["cmj_baseline_start"]), pd.Timestamp(s["cmj_baseline_end"])
    min_n = int(s["cmj_min_baseline_tests"])
    direction = {"drop": "drop", "fall": "drop", "rise": "rise"}.get(s["cmj_direction"])
    if direction is None:
        raise ValueError("cmj_direction must be drop, fall, or rise.")

    te, te_df, mult, te_n = typical_error(values, s["retest_day_1"], s["retest_day_2"])
    in_base = values[(values.date >= base_lo) & (values.date <= base_hi) & values.value.notna()]
    base = in_base.groupby("athlete_id").value.agg(["mean", "count"]).rename(
        columns={"mean": "baseline_mean", "count": "baseline_n"})
    swc_athletes = base.loc[base.baseline_n >= min_n, "baseline_mean"]
    swc = 0.2 * swc_athletes.std(ddof=1)

    out = values.merge(base, left_on="athlete_id", right_index=True, how="left")
    out["baseline_n"] = out.baseline_n.fillna(0).astype(int)
    out["change"] = out.value - out.baseline_mean
    out["te"] = te
    out["multiplier"] = mult
    out["noise_band"] = mult * te * np.sqrt(1 + 1 / out.baseline_n.where(out.baseline_n > 0))
    out["swc"] = swc
    out.loc[out.baseline_n < min_n, ["change", "noise_band"]] = np.nan
    # Band edges around the baseline mean, for trend charts. Reports draw them; they do not calculate them.
    out["band_low_cm"] = out.baseline_mean - out.noise_band
    out["band_high_cm"] = out.baseline_mean + out.noise_band
    # A baseline test is part of its own baseline, and a test before the baseline has no earlier baseline.
    # Neither gets a change.
    in_window = (out.date >= base_lo) & (out.date <= base_hi)
    out.loc[in_window | (out.date < base_lo), ["change", "noise_band"]] = np.nan
    out["direction"] = np.where(out.change < 0, "drop", np.where(out.change > 0, "rise", None))
    out["state"] = [change_state(c, b, swc, direction) for c, b in zip(out.change, out.noise_band)]
    out.loc[in_window, "state"] = "Baseline"
    out.loc[out.value.isna() & ~in_window, "state"] = "No data"
    out["wording"] = out.state.map(STATE_WORDING)
    out["change_low"] = out.change - out.noise_band
    out["change_high"] = out.change + out.noise_band
    out["change_vs_band"] = out.change / out.noise_band
    out["athlete_sentence"] = [athlete_sentence(st, c) for st, c in zip(out.state, out.change)]
    out["chosen_direction"] = direction

    reliability = pd.DataFrame([{
        "measure_name": "cmj_jump_height", "unit": "cm", "trial_summary": s["cmj_trial_summary"],
        "te": te, "te_df": te_df, "multiplier": mult, "swc": swc, "te_athletes": te_n,
        "te_source": (f"Preseason retest on {s['retest_day_1']} and {s['retest_day_2']}, {te_n} athletes. "
                      "Rough estimate: Hopkins (2000) asks for about 50 athletes and at least 3 trials."),
        "swc_source": (f"0.2 x between-athlete SD of baseline means, from the {len(swc_athletes)} athletes "
                       f"with at least {min_n} baseline tests"),
    }])
    return out, reliability


def test_day_summary(results):
    """Results beyond the noise band in the chosen direction, and the number expected by chance.

    Only one direction is counted, so about 2.5 percent of unchanged results fall beyond
    the band by chance. Changes in the other direction are counted separately.
    """
    r = results[~results.state.isin(["Baseline"])].copy()
    beyond = r.state.isin(["Flagged", "Noted"])
    r["beyond_chosen"] = beyond & (r.direction == r.chosen_direction)
    r["beyond_other"] = beyond & (r.direction != r.chosen_direction)
    g = r.groupby("date")
    s = g.agg(chosen_direction=("chosen_direction", "first"),
              results=("state", lambda x: int((x != "No data").sum())),
              flagged=("state", lambda x: int((x == "Flagged").sum())),
              beyond_band=("beyond_chosen", "sum"),
              beyond_band_other_direction=("beyond_other", "sum"),
              no_data=("state", lambda x: int((x == "No data").sum()))).reset_index()
    s["beyond_band_expected_by_chance"] = s.results * 0.025
    other = {"drop": "rise", "rise": "drop"}

    def count(n, word):
        return f"{n} {word}" + ("" if n == 1 else "s")

    s["summary_label"] = [
        f"{count(b, d)} beyond the noise band, {e:.1f} expected by chance. {count(o, other[d])} beyond the band."
        for b, e, o, d in zip(s.beyond_band, s.beyond_band_expected_by_chance,
                              s.beyond_band_other_direction, s.chosen_direction)]
    return s


# ---------------------------------------------------------------------------
# Data quality
# ---------------------------------------------------------------------------

def data_quality(measures, roster, sessions_load, log):
    m = measures.copy()
    m["date"] = pd.to_datetime(m.measure_date)
    active = roster.groupby("date").athlete_id.nunique().rename("athletes_on_roster")
    form_days = roster[roster.date.dt.weekday != 6].groupby("date").athlete_id.nunique().rename("forms_expected")
    forms = (m[m.source == "wellness_form"].groupby("date").athlete_id.nunique().rename("forms_received"))
    rpe_exp = sessions_load.groupby("date").size().rename("ratings_expected")
    rpe_got = sessions_load[sessions_load.session_rpe_cr10.notna()].groupby("date").size().rename("ratings_received")
    fails = m[m.status == "device_failure"].groupby("date").size().rename("device_failure_rows")
    dq = pd.concat([active, form_days, forms, rpe_exp, rpe_got, fails], axis=1).reset_index()
    dq = dq.rename(columns={"index": "date"})
    for c in ["forms_expected", "forms_received", "ratings_expected", "ratings_received", "device_failure_rows"]:
        dq[c] = dq[c].fillna(0).astype(int)
    dq["form_completion_pct"] = np.where(dq.forms_expected > 0, dq.forms_received / dq.forms_expected * 100, np.nan)
    dq["rating_completion_pct"] = np.where(dq.ratings_expected > 0, dq.ratings_received / dq.ratings_expected * 100, np.nan)
    ok = log[log.result == "ok"].copy()
    ok["stamp"] = ok.import_date + " " + ok.import_time_local
    stamps = sorted(ok.stamp)
    dq["last_ok_import"] = [max((x for x in stamps if x[:10] <= d.strftime("%Y-%m-%d")), default="none")
                            for d in dq.date]
    dq["forms_label"] = dq.forms_received.astype(str) + " of " + dq.forms_expected.astype(str)
    return dq


# ---------------------------------------------------------------------------
# Athlete-day table for the squad board
# ---------------------------------------------------------------------------

def athlete_day(daily, wellness, results, settings):
    out = daily.copy()
    answered = wellness.loc[wellness.item != "total", ["athlete_id", "date"]].drop_duplicates().assign(any_answer=True)
    total = wellness[wellness.item == "total"][["athlete_id", "date", "answer", "z", "status", "baseline_n", "change_points"]]
    total = total.rename(columns={"answer": "wellness_total", "z": "wellness_total_z",
                                  "status": "wellness_status", "baseline_n": "wellness_baseline_n",
                                  "change_points": "wellness_change_points"})
    out = out.merge(total, on=["athlete_id", "date"], how="left")
    out = out.merge(answered, on=["athlete_id", "date"], how="left")
    out["form_submitted"] = np.where(out.any_answer.eq(True), "yes", "no")
    out = out.drop(columns="any_answer")
    out.loc[out.date.dt.weekday == 6, "form_submitted"] = "not expected"
    out["wellness_status"] = out.wellness_status.fillna("no form")
    review_z = float(settings["wellness_review_z"])
    out["wellness_review"] = np.where(out.wellness_total_z <= review_z, "review", "")

    # Latest jump test on or before each day.
    r = results[["athlete_id", "date", "value", "change", "noise_band", "state", "wording", "change_vs_band"]].rename(
        columns={"date": "cmj_date", "value": "cmj_cm", "change": "cmj_change_cm", "change_vs_band": "cmj_change_vs_band",
                 "noise_band": "cmj_noise_band_cm", "state": "cmj_state", "wording": "cmj_wording"})
    out = out.sort_values("date")
    r = r.sort_values("cmj_date")
    out = pd.merge_asof(out, r, left_on="date", right_on="cmj_date", by="athlete_id", direction="backward")
    out["cmj_days_ago"] = (out.date - out.cmj_date).dt.days
    return out.sort_values(["athlete_id", "date"])


def dates_table(first, last):
    """One row for every calendar day, for the dashboards' date filters."""
    d = pd.DataFrame({"date": pd.date_range(first, last, freq="D")})
    d["week_start"] = d.date - pd.to_timedelta(d.date.dt.weekday, unit="D")
    d["days_before_latest"] = (pd.Timestamp(last) - d.date).dt.days
    d["in_last_28_days"] = np.where(d.days_before_latest < 28, "yes", "no")
    return d


def profile_series(board, results):
    """One long table of the lines on the athlete profile, for tools that chart one value column."""
    parts = []
    for series, column in [("Daily load (AU)", "srpe_load_au"), ("7-day mean daily load (AU)", "acute_load_au"),
                           ("28-day mean daily load (AU)", "chronic_load_au")]:
        parts.append(board[["athlete_id", "date", column]].rename(columns={column: "value"}).assign(chart="load", series=series))
    parts.append(board[["athlete_id", "date", "wellness_total"]].rename(columns={"wellness_total": "value"})
                 .assign(chart="wellness", series="Wellness total (points)"))
    for series, column in [("Jump height (cm)", "value"), ("Noise band, low (cm)", "band_low_cm"),
                           ("Noise band, high (cm)", "band_high_cm")]:
        parts.append(results[["athlete_id", "date", column]].rename(columns={column: "value"}).assign(chart="jump", series=series))
    out = pd.concat(parts, ignore_index=True)
    return out[["athlete_id", "date", "chart", "series", "value"]]


def with_names(df, athletes):
    """Add name, group, and email so a report tool can show and secure each row without a join."""
    return df.merge(athletes[["athlete_id", "name", "group", "email"]], on="athlete_id", how="left")


def fmt(df):
    """Write dates as YYYY-MM-DD, round numbers, and write missing values as empty cells."""
    df = df.copy()
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            df[c] = df[c].dt.strftime("%Y-%m-%d")
        elif pd.api.types.is_float_dtype(df[c]):
            df[c] = df[c].round(4)
    return df


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--input", default=str(ROOT / "data" / "sample"))
    p.add_argument("--output", default=str(ROOT / "data" / "metrics"))
    args = p.parse_args()

    athletes = read(args.input, "athletes")
    measures = read(args.input, "measures")
    availability = read(args.input, "availability")
    log = read(args.input, "import_log")
    settings = dict(read(args.input, "settings")[["setting", "value"]].values)

    last_day = max(measures.measure_date.max(), availability.date.max())
    roster = roster_days(athletes, last_day)

    loads = session_loads(measures)
    daily = daily_load(roster, loads, availability)
    daily = rolling_acwr(daily, int(settings["acute_window_days"]), int(settings["chronic_window_days"]))
    ext = external_daily(measures, roster)
    daily = daily.merge(ext, on=["athlete_id", "date"], how="left")
    weekly = weekly_load(daily)

    well = wellness_scores(measures, int(settings["wellness_baseline_window_days"]),
                           int(settings["wellness_min_baseline_answers"]))
    summary_rule = settings["cmj_trial_summary"]
    if not summary_rule.startswith("mean_of_"):
        raise ValueError("cmj_trial_summary must be mean_of_N, such as mean_of_3.")
    values = test_day_values(measures, trials_needed=int(summary_rule.split("_")[-1]))
    results, reliability = test_results(values, settings)
    summary = test_day_summary(results)
    dq = data_quality(measures, roster, loads, log)
    board = athlete_day(daily, well, results, settings)
    board["acwr_note"] = ACWR_NOTE

    dates = dates_table(roster.date.min(), roster.date.max())
    board = board.merge(dates[["date", "in_last_28_days"]], on="date", how="left")
    series = profile_series(board, results)

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    files = {
        "athlete_day": with_names(board, athletes), "wellness_scores": with_names(well, athletes),
        "test_results": with_names(results, athletes), "weekly_load": with_names(weekly, athletes),
        "profile_series": with_names(series, athletes), "reliability": reliability,
        "test_day_summary": summary, "data_quality": dq, "dates": dates,
        # Reference tables, copied unchanged so the report layer reads one folder.
        "athletes": athletes, "settings": read(args.input, "settings"), "import_log": log,
    }
    for name, df in files.items():
        fmt(df).to_csv(out / f"{name}.csv", index=False)
        print(f"{name}: {len(df)} rows")


if __name__ == "__main__":
    main()
