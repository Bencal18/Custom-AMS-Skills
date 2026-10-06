"""Known-answer tests for the metric layer.

The expected values come from the worked examples in docs/calculations.md of
the Custom AMS Skills repository. Run from the repository root:

    python3 -m pytest pipeline/tests
"""

import sys
from math import sqrt
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_metrics as bm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent


def test_rolling_coupled_acwr_matches_worked_example():
    weeks = [
        [450, 600, 300, 550, 250, 0, 0],
        [500, 620, 320, 560, 280, 0, 0],
        [480, 650, 300, 600, 260, 0, 0],
        [520, 640, 350, 580, 300, 0, 0],
        [700, 800, 500, 750, 600, 400, 0],
    ]
    loads = [x for w in weeks for x in w]
    daily = pd.DataFrame({
        "athlete_id": "A0001",
        "date": pd.date_range("2026-08-03", periods=35, freq="D"),
        "srpe_load_au": np.array(loads, dtype=float),
    })
    out = bm.rolling_acwr(daily).set_index("date")
    day35 = out.loc[pd.Timestamp("2026-09-06")]
    assert day35.acute_load_au == pytest.approx(535.71, abs=0.01)
    assert day35.chronic_load_au == pytest.approx(382.50, abs=0.01)
    assert round(day35.acwr_coupled, 2) == 1.40
    # No ratio before the chronic window is full.
    assert out.loc[pd.Timestamp("2026-08-29")].acwr_coupled != out.loc[pd.Timestamp("2026-08-29")].acwr_coupled


def test_missing_day_blanks_the_ratio_for_28_days():
    loads = [300.0] * 60
    loads[30] = np.nan
    daily = pd.DataFrame({"athlete_id": "A0001",
                          "date": pd.date_range("2026-08-01", periods=60, freq="D"),
                          "srpe_load_au": loads})
    out = bm.rolling_acwr(daily).reset_index(drop=True)
    assert out.acwr_coupled.iloc[29] == pytest.approx(1.0)
    assert out.acwr_coupled.iloc[30:58].isna().all()
    assert out.acwr_coupled.iloc[58] == pytest.approx(1.0)


def test_wellness_z_matches_worked_example():
    base = {
        "sleep_quality": [4, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 3, 4, 4],
        "soreness": [3, 4, 4, 3, 4, 3, 3, 4, 3, 4, 4, 3, 3, 4],
        "fatigue": [4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3],
        "stress": [4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4],
        "mood": [4, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4],
    }
    today = {"sleep_quality": 2, "soreness": 3, "fatigue": 4, "stress": 4, "mood": 4}
    days = pd.date_range("2026-09-01", periods=15, freq="D")
    rows = []
    for item, vals in base.items():
        for d, v in zip(days, vals + [today[item]]):
            rows.append({"athlete_id": "A0001", "measure_date": d.strftime("%Y-%m-%d"),
                         "measure_name": item, "value": str(v), "status": "ok"})
    measures = pd.DataFrame(rows)
    w = bm.wellness_scores(measures, window_days=28, min_answers=14)
    last = w[w.date == days[-1]].set_index("item")
    assert round(last.loc["sleep_quality", "z"], 2) == -3.13
    assert round(last.loc["total", "z"], 2) == -2.84
    assert last.loc["total", "answer"] == 17
    # The day before has only 13 earlier answers, so no z-score.
    assert (w[w.date == days[-2]].status == "baseline too short").all()


def test_noise_band_for_a_single_baseline_test_is_multiplier_times_root_2_te():
    values = make_tests()
    settings = dict(SETTINGS, cmj_min_baseline_tests="1")
    out, rel = bm.test_results(values, settings)
    a3 = out[(out.athlete_id == "A3") & (out.date == pd.Timestamp("2026-08-04"))].iloc[0]
    assert a3.baseline_n == 1
    assert a3.noise_band == pytest.approx(rel.multiplier.iloc[0] * rel.te.iloc[0] * sqrt(2))


def test_change_states_for_a_drop():
    swc = 0.6
    assert bm.change_state(-1.0, 2.0, swc, "drop") == "No flag"
    assert bm.change_state(-2.3, 2.0, swc, "drop") == "Noted"   # Beyond band, change + band = -0.3, not below -SWC
    assert bm.change_state(-2.7, 2.0, swc, "drop") == "Flagged"  # change + band = -0.7, below -0.6
    assert bm.change_state(3.0, 2.0, swc, "drop") == "Noted"    # A rise is reported, never flagged
    assert bm.change_state(np.nan, 2.0, swc, "drop") == "No data"


def test_typical_error_from_two_retests():
    values = pd.DataFrame({
        "athlete_id": ["A1", "A2", "A3", "A1", "A2", "A3"],
        "date": pd.to_datetime(["2026-07-07"] * 3 + ["2026-07-09"] * 3),
        "value": [30.0, 35.0, 40.0, 31.0, 34.0, 42.0],
    })
    te, df, mult, n = bm.typical_error(values, "2026-07-07", "2026-07-09")
    diffs = np.array([1.0, -1.0, 2.0])
    assert te == pytest.approx(diffs.std(ddof=1) / sqrt(2))
    assert df == 2 and n == 3
    assert mult == pytest.approx(4.303, abs=0.001)  # t(0.975, 2)


def test_session_with_no_rating_gives_missing_day_and_rest_day_gives_zero():
    measures = pd.DataFrame([
        {"athlete_id": "A1", "measure_date": "2026-09-01", "session_id": "S1", "measure_name": "session_rpe_cr10", "value": "6", "status": "ok"},
        {"athlete_id": "A1", "measure_date": "2026-09-01", "session_id": "S1", "measure_name": "session_duration", "value": "90", "status": "ok"},
        {"athlete_id": "A1", "measure_date": "2026-09-02", "session_id": "S2", "measure_name": "session_duration", "value": "60", "status": "ok"},
    ])
    roster = pd.DataFrame({"athlete_id": "A1", "date": pd.date_range("2026-09-01", periods=3, freq="D")})
    avail = pd.DataFrame({"athlete_id": "A1", "date": ["2026-09-01", "2026-09-02", "2026-09-03"],
                          "availability": "full"})
    d = bm.daily_load(roster, bm.session_loads(measures), avail).set_index("date")
    assert d.loc[pd.Timestamp("2026-09-01"), "srpe_load_au"] == 540
    assert np.isnan(d.loc[pd.Timestamp("2026-09-02"), "srpe_load_au"])
    assert d.loc[pd.Timestamp("2026-09-03"), "srpe_load_au"] == 0


def test_sample_outputs_have_unique_keys_and_no_missing_keys():
    a = pd.read_csv(ROOT / "data" / "metrics" / "athlete_day.csv", dtype=str, keep_default_na=False)
    assert not a.duplicated(["athlete_id", "date"]).any()
    assert (a.athlete_id != "").all() and (a.date != "").all()
    m = pd.read_csv(ROOT / "data" / "sample" / "measures.csv", dtype=str, keep_default_na=False)
    keys = ["athlete_id", "measure_date", "session_id", "measure_name", "side", "trial_number", "source"]
    assert not m.duplicated(keys).any()
    assert not (m[keys] == "NA").any().any()


def test_first_rolling_ratio_on_day_28():
    loads = [450, 600, 300, 550, 250, 0, 0, 500, 620, 320, 560, 280, 0, 0,
             480, 650, 300, 600, 260, 0, 0, 520, 640, 350, 580, 300, 0, 0]
    daily = pd.DataFrame({"athlete_id": "A0001", "date": pd.date_range("2026-08-03", periods=28, freq="D"),
                          "srpe_load_au": np.array(loads, dtype=float)})
    out = bm.rolling_acwr(daily).set_index("date")
    assert np.isnan(out.loc[pd.Timestamp("2026-08-29")].acwr_coupled)
    assert round(out.loc[pd.Timestamp("2026-08-30")].acwr_coupled, 2) == 1.05


def test_change_states_for_a_rise_missing_swc_and_band_edge():
    assert bm.change_state(2.7, 2.0, 0.6, "rise") == "Flagged"
    assert bm.change_state(2.3, 2.0, 0.6, "rise") == "Noted"
    assert bm.change_state(-2.0, 2.0, 0.6, "drop") == "No flag"  # Exactly on the band edge
    assert bm.change_state(-5.0, 1.0, np.nan, "drop") == "No data"


def test_rated_session_with_failed_duration_is_missing_not_rest():
    measures = pd.DataFrame([
        {"athlete_id": "A1", "measure_date": "2026-09-01", "session_id": "S1", "measure_name": "session_rpe_cr10", "value": "6", "status": "ok"},
        {"athlete_id": "A1", "measure_date": "2026-09-01", "session_id": "S1", "measure_name": "session_duration", "value": "NA", "status": "device_failure"},
    ])
    roster = pd.DataFrame({"athlete_id": "A1", "date": pd.date_range("2026-09-01", periods=1, freq="D")})
    avail = pd.DataFrame({"athlete_id": "A1", "date": ["2026-09-01"], "availability": "full"})
    d = bm.daily_load(roster, bm.session_loads(measures), avail)
    assert d.sessions.iloc[0] == 1
    assert np.isnan(d.srpe_load_au.iloc[0])


def test_two_ok_ratings_for_one_session_stop_the_build():
    measures = pd.DataFrame([
        {"athlete_id": "A1", "measure_date": "2026-09-01", "session_id": "S1", "measure_name": "session_rpe_cr10", "value": v, "status": "ok"}
        for v in ("6", "9")])
    with pytest.raises(ValueError):
        bm.session_loads(measures)


def make_tests():
    """Three athletes, mean of 1 trial each day for simplicity. Baseline 2026-07-07 to 2026-07-21."""
    rows = []
    vals = {
        "A1": [30.0, 31.0, 30.0, 26.0],   # Baseline 30.33, then a large drop
        "A2": [40.0, 40.5, 39.5, 43.0],   # Baseline 40.0, then a large rise
        "A3": [35.0, None, None, 35.2],   # One baseline test only
    }
    days = pd.to_datetime(["2026-07-07", "2026-07-14", "2026-07-21", "2026-08-04"])
    for aid, series in vals.items():
        for d, v in zip(days, series):
            rows.append({"athlete_id": aid, "date": d, "value": v, "trials_ok": 1, "trials_attempted": 1})
    return pd.DataFrame(rows)


SETTINGS = {"cmj_baseline_start": "2026-07-07", "cmj_baseline_end": "2026-07-21",
            "cmj_min_baseline_tests": "2", "cmj_direction": "drop", "cmj_trial_summary": "mean_of_1",
            "retest_day_1": "2026-07-07", "retest_day_2": "2026-07-14"}


def test_results_states_band_and_swc():
    values = make_tests()
    out, rel = bm.test_results(values, SETTINGS)
    after = out[out.date == pd.Timestamp("2026-08-04")].set_index("athlete_id")
    # TE from the two retest days: differences 1.0, 0.5 (A3 has no second test).
    te = np.std([1.0, 0.5], ddof=1) / sqrt(2)
    assert rel.te.iloc[0] == pytest.approx(te)
    mult = rel.multiplier.iloc[0]
    assert mult == pytest.approx(12.706, abs=0.001)  # t(0.975, 1)
    # SWC: 0.2 x SD of the baseline means of athletes with at least 2 baseline tests.
    swc = 0.2 * np.std([np.mean([30, 31, 30]), np.mean([40, 40.5, 39.5])], ddof=1)
    assert rel.swc.iloc[0] == pytest.approx(swc)
    band = mult * te * sqrt(1 + 1 / 3)
    assert after.loc["A1", "noise_band"] == pytest.approx(band)
    assert after.loc["A1", "change"] == pytest.approx(26.0 - np.mean([30, 31, 30]))
    assert after.loc["A3", "state"] == "No data"           # Baseline too short
    assert (out[out.date < pd.Timestamp("2026-08-04")].state == "Baseline").all()
    assert out[out.state == "Baseline"].change.isna().all()  # A baseline test gets no change


def test_day_summary_counts_only_the_chosen_direction():
    results = pd.DataFrame({
        "date": pd.to_datetime(["2026-08-04"] * 4),
        "state": ["Flagged", "Noted", "No flag", "No data"],
        "direction": ["drop", "rise", "drop", None],
        "chosen_direction": "drop",
    })
    s = bm.test_day_summary(results).iloc[0]
    assert s.results == 3
    assert s.beyond_band == 1
    assert s.beyond_band_other_direction == 1
    assert s.beyond_band_expected_by_chance == pytest.approx(3 * 0.025)
    assert s.summary_label.startswith("1 drop beyond the noise band, 0.1 expected by chance. 1 rise")
