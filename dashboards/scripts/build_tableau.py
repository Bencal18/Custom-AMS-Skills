#!/usr/bin/env python3
"""Generate the Tableau workbooks for the Custom AMS dashboards.

Writes two plain XML workbooks for Tableau 2026.1 or later:

    tableau/CustomAMS-staff.twb    Squad board, athlete profile, load, wellness, testing,
                                   availability, and data health. Staff only.
    tableau/CustomAMS-athlete.twb  My data. Each athlete sees only their own rows once published.

The athlete workbook holds no athlete list and no squad sheet.
Each data source reads one CSV from data/metrics. Every calculated field only
filters or looks values up. No metric is calculated in Tableau.

Run it from the dashboards folder after the metric layer is built:

    python3 pipeline/build_metrics.py
    python3 scripts/build_tableau.py
"""

import re
import uuid
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "tableau"
VERSION = "26.1"
NS = uuid.UUID("0b8e7a43-6a4f-4d0e-9a7e-2f1e5c3d8b21")
STAFF_GROUP = "AMS staff"
DATE_COLUMNS = {"date", "week_start", "cmj_date", "import_date", "start_date", "end_date"}
ACWR_NOTE = "ACWR describes how recent load compares with longer-term load. It does not predict injury."

# Row-level security. On Tableau Server or Cloud, members of the staff group see every row,
# and everyone else sees only rows whose email matches their sign-in. In Tableau Desktop,
# ISMEMBEROF returns null, so every row shows.
SECURE = f'IFNULL(ISMEMBEROF("{STAFF_GROUP}"), TRUE) OR LOWER([email]) = LOWER(USERNAME())'
REF = re.compile(r"\[([^\[\]]+)\]")
PARAM = "[Parameters].[athlete_choice]"
PARAM_COL = ""  # Set when the staff workbook is built
# Staff profile filter: staff pick an athlete by ID with the parameter, which shows names as aliases.
PICKED = "[athlete_id] = [Parameters].[athlete_choice]"


def uid(*parts):
    return "{" + str(uuid.uuid5(NS, "/".join(parts))).upper() + "}"


def a(v):
    return quoteattr(str(v))


def tab_type(name, values):
    if name in DATE_COLUMNS:
        return "date"
    vals = [v for v in values if v not in ("", "NA")]
    if not vals or name.endswith("_id"):
        return "string"
    try:
        nums = [float(v) for v in vals]
    except ValueError:
        return "string"
    if all(n.is_integer() for n in nums) and all("." not in v for v in vals):
        return "integer"
    return "real"


class Source:
    """One Tableau data source for one CSV file."""

    def __init__(self, key, file, secure=True):
        self.key, self.file = key, file
        self.name = f"federated.{key}"
        df = pd.read_csv(ROOT / "data" / "metrics" / file, dtype=str, keep_default_na=False)
        self.columns = [(c, tab_type(c, df[c].tolist())) for c in df.columns]
        self.types = dict(self.columns)
        self.calcs = []  # (name, caption, datatype, role, type, formula)
        self.secure = secure and "email" in self.types
        if self.secure:
            self.calc("secure_rows", "Row security", "boolean", "dimension", "nominal", SECURE)

    def calc(self, name, caption, datatype, role, ctype, formula):
        self.calcs.append((name, caption, datatype, role, ctype, formula))
        self.types[name] = datatype

    def ref(self, field):
        return f"[{self.name}].[{field}]"

    def xml(self):
        rel_cols = "\n".join(
            f"              <column datatype={a(t)} name={a(c)} ordinal={a(i)} />"
            for i, (c, t) in enumerate(self.columns))
        meta = []
        for c, t in self.columns:
            role, ctype = ("measure", "quantitative") if t in ("integer", "real") else ("dimension", "nominal")
            if t == "date":
                role, ctype = "dimension", "ordinal"
            fmt = " default-format='n#,##0.00'" if t == "real" else ""
            meta.append(f"      <column datatype={a(t)}{fmt} name={a('[' + c + ']')} role={a(role)} type={a(ctype)} />")
        for name, caption, dt, role, ctype, formula in self.calcs:
            meta.append(
                f"      <column caption={a(caption)} datatype={a(dt)} name={a('[' + name + ']')} role={a(role)} type={a(ctype)}>\n"
                f"        <calculation class='tableau' formula={a(formula)} />\n"
                f"      </column>")
        flt = ""
        if self.secure:
            flt = (f"      <filter class='categorical' column='[secure_rows]' filter-group='2'>\n"
                   f"        <groupfilter function='member' level='[secure_rows]' member='true' "
                   f"user:ui-domain='database' user:ui-enumeration='inclusive' user:ui-marker='enumerate' />\n"
                   f"      </filter>\n")
        if any(PARAM in c[5] for c in self.calcs):
            flt = ("      <datasource-dependencies datasource='Parameters'>\n" + PARAM_COL +
                   "      </datasource-dependencies>\n") + flt
        table = self.file.replace(".", "#")
        return (
            f"    <datasource caption={a(self.key)} inline='true' name={a(self.name)} version={a(VERSION)}>\n"
            f"      <connection class='federated'>\n"
            f"        <named-connections>\n"
            f"          <named-connection caption={a(self.key)} name={a('textscan.' + self.key)}>\n"
            f"            <connection class='textscan' directory='../data/metrics' filename={a(self.file)} password='' server='' />\n"
            f"          </named-connection>\n"
            f"        </named-connections>\n"
            f"        <relation connection={a('textscan.' + self.key)} name={a(self.file)} table={a('[' + table + ']')} type='table'>\n"
            f"          <columns character-set='UTF-8' header='yes' locale='en_US' separator=','>\n"
            f"{rel_cols}\n"
            f"          </columns>\n"
            f"        </relation>\n"
            f"      </connection>\n"
            + "\n".join(meta) + "\n" + flt +
            f"    </datasource>\n")


class Field:
    """A column instance on a shelf: a field with an aggregation or a date part."""

    PREFIX = {"None": "none", "Sum": "sum", "Avg": "avg", "Count": "cnt", "Day-Trunc": "tdy", "Attribute": "attr"}

    def __init__(self, src, field, derivation="None", discrete=True):
        self.src, self.field, self.derivation = src, field, derivation
        dt = src.types[field]
        if derivation in ("Sum", "Avg", "Count"):
            self.ctype, suffix = "quantitative", "qk"
        elif discrete:
            self.ctype, suffix = ("ordinal", "ok") if dt in ("date", "integer", "real") else ("nominal", "nk")
        else:
            self.ctype, suffix = "quantitative", "qk"
        self.instance = f"[{self.PREFIX[derivation]}:{field}:{suffix}]"

    @property
    def ref(self):
        return f"[{self.src.name}].{self.instance}"

    def dep(self):
        return (f"            <column-instance column={a('[' + self.field + ']')} derivation={a(self.derivation)} "
                f"name={a(self.instance)} pivot='key' type={a(self.ctype)} />")


class Sheet:
    def __init__(self, name, src, rows, cols, mark, encodings=None, filters=None, sort=None):
        self.name, self.src, self.rows, self.cols, self.mark = name, src, rows, cols, mark
        self.encodings = encodings or []  # (kind, Field)
        self.filters = filters or []      # (Field, [members])
        self.sort = sort                  # (dimension Field, measure Field, direction)

    def fields(self):
        out = list(self.rows) + list(self.cols) + [f for _, f in self.encodings] + [f for f, _ in self.filters]
        if self.sort:
            out += [self.sort[0], self.sort[1]]
        seen, uniq = set(), []
        for f in out:
            if f.instance not in seen:
                seen.add(f.instance)
                uniq.append(f)
        return uniq

    def xml(self):
        s = self.src
        base_cols, seen = [], set()
        for f in self.fields():
            if f.field not in seen:
                seen.add(f.field)
                base_cols.append(f.field)
        for c in base_cols:
            calc = next((x for x in s.calcs if x[0] == c), None)
            if calc:
                for r in REF.findall(calc[5].replace(PARAM, "")):
                    if r in s.types and r not in seen:
                        seen.add(r)
                        base_cols.append(r)
        uses_param = any(PARAM in x[5] for x in s.calcs if x[0] in seen)
        deps = []
        for c in base_cols:
            calc = next((x for x in s.calcs if x[0] == c), None)
            dt = s.types[c]
            if calc:
                _, caption, dt, role, ctype, formula = calc
                deps.append(f"            <column caption={a(caption)} datatype={a(dt)} name={a('[' + c + ']')} role={a(role)} type={a(ctype)}>\n"
                            f"              <calculation class='tableau' formula={a(formula)} />\n"
                            f"            </column>")
            else:
                role, ctype = ("measure", "quantitative") if dt in ("integer", "real") else ("dimension", "nominal")
                if dt == "date":
                    role, ctype = "dimension", "ordinal"
                deps.append(f"            <column datatype={a(dt)} name={a('[' + c + ']')} role={a(role)} type={a(ctype)} />")
        deps += [f.dep() for f in self.fields()]
        filters = []
        for f, members in self.filters:
            inner = "\n".join(
                f"              <groupfilter function='member' level={a(f.instance)} member={a(m)} />" for m in members)
            if len(members) == 1:
                body = (f"            <groupfilter function='member' level={a(f.instance)} member={a(members[0])} "
                        f"user:ui-domain='database' user:ui-enumeration='inclusive' user:ui-marker='enumerate' />")
            else:
                body = (f"            <groupfilter function='union' user:ui-domain='database' user:ui-enumeration='inclusive' user:ui-marker='enumerate'>\n"
                        f"{inner}\n            </groupfilter>")
            filters.append(f"          <filter class='categorical' column={a(f.ref)}>\n{body}\n          </filter>")
        sort = ""
        if self.sort:
            dim, mea, direction = self.sort
            sort = f"          <computed-sort column={a(dim.ref)} direction={a(direction)} using={a(mea.ref)} />\n"
        slices = ""
        if self.filters:
            slices = "          <slices>\n" + "\n".join(
                f"            <column>{escape(f.ref)}</column>" for f, _ in self.filters) + "\n          </slices>\n"
        enc = ""
        if self.encodings:
            enc = "              <encodings>\n" + "\n".join(
                f"                <{k} column={a(f.ref)} />" for k, f in self.encodings) + "\n              </encodings>\n"
        shelf = lambda fs: " / ".join(f.ref for f in fs)  # noqa: E731
        return (
            f"    <worksheet name={a(self.name)}>\n"
            f"      <table>\n"
            f"        <view>\n"
            f"          <datasources>\n            <datasource caption={a(s.key)} name={a(s.name)} />\n"
            + ("            <datasource name='Parameters' />\n" if uses_param else "") +
            f"          </datasources>\n"
            f"          <datasource-dependencies datasource={a(s.name)}>\n" + "\n".join(deps) + "\n"
            f"          </datasource-dependencies>\n"
            + ("          <datasource-dependencies datasource='Parameters'>\n" + PARAM_COL + "          </datasource-dependencies>\n" if uses_param else "")
            + "\n".join(filters) + ("\n" if filters else "") + sort + slices +
            f"          <aggregation value='true' />\n"
            f"        </view>\n"
            f"        <style />\n"
            f"        <panes>\n"
            f"          <pane selection-relaxation-option='selection-relaxation-allow'>\n"
            f"            <view>\n              <breakdown value='auto' />\n            </view>\n"
            f"            <mark class={a(self.mark)} />\n" + enc +
            f"          </pane>\n"
            f"        </panes>\n"
            f"        <rows>{escape(shelf(self.rows))}</rows>\n"
            f"        <cols>{escape(shelf(self.cols))}</cols>\n"
            f"      </table>\n"
            f"      <simple-id uuid={a(uid('sheet', self.name))} />\n"
            f"    </worksheet>\n")


# The standard card layout Tableau writes for a worksheet window.
CARDS = (
    "      <cards>\n"
    "        <edge name='left'>\n          <strip size='160'>\n"
    "            <card type='pages' />\n            <card type='filters' />\n            <card type='marks' />\n"
    "          </strip>\n        </edge>\n"
    "        <edge name='top'>\n"
    "          <strip size='2147483647'>\n            <card type='columns' />\n          </strip>\n"
    "          <strip size='2147483647'>\n            <card type='rows' />\n          </strip>\n"
    "          <strip size='2147483647'>\n            <card type='title' />\n          </strip>\n"
    "        </edge>\n"
    "      </cards>\n")


def dashboard(name, zones, title=None, param=False):
    """Stack the sheets top to bottom, with an optional parameter control at the top."""
    parts, y, n = [], 0, 3
    items = []
    if title:
        items.append(("text", title, 8000))
    if param:
        items.append(("param", None, 8000))
    share = (100000 - sum(h for _, _, h in items)) // max(len(zones), 1)
    items += [("sheet", z, share) for z in zones]
    for kind, val, h in items:
        if kind == "text":
            parts.append(f"          <zone h={a(h)} id={a(n)} type-v2='text' w='100000' x='0' y={a(y)}>\n"
                         f"            <formatted-text>\n              <run>{escape(val)}</run>\n            </formatted-text>\n"
                         f"          </zone>")
        elif kind == "param":
            parts.append(f"          <zone h={a(h)} id={a(n)} mode='compact' param='[Parameters].[athlete_choice]' "
                         f"type-v2='paramctrl' w='100000' x='0' y={a(y)} />")
        else:
            parts.append(f"          <zone h={a(h)} id={a(n)} name={a(val)} w='100000' x='0' y={a(y)} />")
        y += h
        n += 1
    return (f"    <dashboard name={a(name)}>\n      <style />\n"
            f"      <size maxheight='900' maxwidth='1400' minheight='900' minwidth='1400' />\n"
            f"      <zones>\n        <zone h='100000' id='1' type-v2='layout-basic' w='100000' x='0' y='0'>\n"
            + "\n".join(parts) + "\n        </zone>\n      </zones>\n"
            f"      <simple-id uuid={a(uid('dash', name, *zones))} />\n    </dashboard>\n")


def write_workbook(path, sources, sheets, dashboards, params=""):
    """Write one workbook. Each dashboard is (name, sheet names, title, show the athlete parameter)."""
    windows = "".join(
        f"    <window class='worksheet' hidden='true' name={a(s.name)}>\n" + CARDS +
        f"      <simple-id uuid={a(uid('win', path.name, s.name))} />\n    </window>\n"
        for s in sheets)
    windows += "".join(
        f"    <window class='dashboard'{' maximized=' + a('true') if i == 0 else ''} name={a(name)}>\n      <viewpoints>\n"
        + "".join(f"        <viewpoint name={a(z)} />\n" for z in zones)
        + f"      </viewpoints>\n      <active id='-1' />\n      <simple-id uuid={a(uid('wind', path.name, name))} />\n    </window>\n"
        for i, (name, zones, _, _) in enumerate(dashboards))
    dash_xml = "".join(dashboard(name, zones, title, param) for name, zones, title, param in dashboards)
    xml = (
        "<?xml version='1.0' encoding='utf-8' ?>\n"
        f"<workbook original-version={a(VERSION)} source-build='0.0.0 (0000.0.0.0)' source-platform='mac' "
        f"version={a(VERSION)} xmlns:user='http://www.tableausoftware.com/xml/user'>\n"
        "  <document-format-change-manifest>\n    <ManifestByVersion />\n  </document-format-change-manifest>\n"
        "  <preferences />\n"
        "  <datasources>\n" + params + "".join(s.xml() for s in sources) + "  </datasources>\n"
        "  <worksheets>\n" + "".join(s.xml() for s in sheets) + "  </worksheets>\n"
        "  <dashboards>\n" + dash_xml + "  </dashboards>\n"
        "  <windows>\n" + windows + "  </windows>\n"
        "  <explain-data enabled-for-viewer='false' extreme-values-enabled-for-all='false'>\n    <explanation-types />\n  </explain-data>\n"
        "</workbook>\n")
    path.write_text(xml, encoding="utf-8")
    print(f"{path.name}: {len(sources)} data sources, {len(sheets)} worksheets, {len(dashboards)} dashboards")


def staff_workbook(athletes):
    global PARAM_COL
    day = Source("athlete_day", "athlete_day.csv")
    day.calc("latest_day", "Latest day", "boolean", "dimension", "nominal", "[date] = {FIXED : MAX([date])}")
    tests = Source("test_results", "test_results.csv")
    tests.calc("latest_test_day", "Latest test day", "boolean", "dimension", "nominal",
               "[date] = {FIXED : MAX([date])}")
    series = Source("profile_series", "profile_series.csv")
    series.calc("picked", "Athlete picked", "boolean", "dimension", "nominal", PICKED)
    weekly = Source("weekly_load", "weekly_load.csv")
    quality = Source("data_quality", "data_quality.csv", secure=False)
    log = Source("import_log", "import_log.csv", secure=False)
    sources = [day, tests, series, weekly, quality, log]

    F = Field
    true = ["true"]
    day_axis = F(series, "date", "Day-Trunc")  # Discrete day, so a missing day stays a gap
    sheets = [
        Sheet("Squad board table", day,
              rows=[F(day, c) for c in ["name", "group", "availability", "form_submitted", "wellness_total",
                                         "wellness_change_points", "wellness_total_z", "wellness_status",
                                         "acute_load_au", "chronic_load_au", "acwr_coupled", "cmj_date",
                                         "cmj_change_cm", "cmj_noise_band_cm"]],
              cols=[], mark="Text", encodings=[("text", F(day, "cmj_wording"))], filters=[(F(day, "latest_day"), true)],
              sort=(F(day, "name"), F(day, "cmj_change_vs_band", "Avg"), "ASC")),
        Sheet("Profile load", series, rows=[F(series, "value", "Avg")], cols=[day_axis],
              mark="Line", encodings=[("color", F(series, "series"))],
              filters=[(F(series, "chart"), ['"load"']), (F(series, "picked"), true)]),
        Sheet("Profile jump", series, rows=[F(series, "value", "Avg")], cols=[F(series, "date", "Day-Trunc", discrete=False)],
              mark="Line", encodings=[("color", F(series, "series"))],
              filters=[(F(series, "chart"), ['"jump"']), (F(series, "picked"), true)]),
        Sheet("Profile wellness", series, rows=[F(series, "value", "Avg")], cols=[day_axis],
              mark="Line", filters=[(F(series, "chart"), ['"wellness"']), (F(series, "picked"), true)]),
        Sheet("Wellness grid", day, rows=[F(day, "name")], cols=[F(day, "date", "Day-Trunc")], mark="Square",
              encodings=[("color", F(day, "wellness_total_z", "Avg")), ("text", F(day, "wellness_total_z", "Avg"))],
              filters=[(F(day, "in_last_28_days"), ['"yes"'])]),
        Sheet("Form completion", quality, rows=[F(quality, "form_completion_pct", "Avg")],
              cols=[F(quality, "date", "Day-Trunc", discrete=False)], mark="Line"),
        Sheet("Jump changes", tests, rows=[F(tests, "name")], cols=[F(tests, "change", "Avg")], mark="Bar",
              encodings=[("color", F(tests, "wording"))],
              filters=[(F(tests, "latest_test_day"), true)],
              sort=(F(tests, "name"), F(tests, "change_vs_band", "Avg"), "ASC")),
        Sheet("Weekly load", weekly, rows=[F(weekly, "name")], cols=[F(weekly, "week_start")], mark="Text",
              encodings=[("text", F(weekly, "week_label"))]),
        Sheet("Availability by day", day, rows=[F(day, "athlete_id", "Count")], cols=[F(day, "date", "Day-Trunc")], mark="Bar",
              encodings=[("color", F(day, "availability"))]),
        Sheet("Import log", log, rows=[F(log, c) for c in ["import_date", "import_time_local", "source", "rows_imported"]],
              cols=[], mark="Text", encodings=[("text", F(log, "result"))]),
    ]
    dashboards = [
        ("Squad board", ["Squad board table"],
         "Squad board for the latest day. Staff only. Jump state compares the latest test with the athlete's "
         "baseline and the noise band.\n" + ACWR_NOTE, False),
        ("Athlete profile", ["Profile load", "Profile jump", "Profile wellness"],
         "Pick one athlete. Every chart compares the athlete with their own data.", True),
        ("Load", ["Weekly load"], "Weekly session RPE load and the days with complete data.", False),
        ("Wellness", ["Wellness grid", "Form completion"],
         "Total wellness z-score against each athlete's previous 28 days. Orange is below usual, blue is above.", False),
        ("Testing", ["Jump changes"],
         "Change in jump height from baseline on the latest test day. Repeat a test before anyone acts on a single flag.", False),
        ("Availability", ["Availability by day"],
         "Athletes who are full, modified, or out each day. Status only, never a diagnosis.", False),
        ("Data health", ["Form completion", "Import log"], "Check this page first.", False),
    ]
    roster = athletes.sort_values("name")
    first = roster.athlete_id.iloc[0]
    members = "\n".join(f"        <member alias={a(r.name)} value={a(chr(34) + r.athlete_id + chr(34))} />"
                        for r in roster.itertuples())
    PARAM_COL = (
        f"      <column caption='Athlete' datatype='string' name='[athlete_choice]' param-domain-type='list' role='measure' "
        f"type='nominal' value={a(chr(34) + first + chr(34))}>\n"
        f"        <calculation class='tableau' formula={a(chr(34) + first + chr(34))} />\n"
        f"        <members>\n{members}\n        </members>\n      </column>\n")
    params = ("    <datasource hasconnection='false' inline='true' name='Parameters' version=" + a(VERSION) + ">\n"
              "      <aliases enabled='yes' />\n" + PARAM_COL + "    </datasource>\n")
    write_workbook(OUT_DIR / "CustomAMS-staff.twb", sources, sheets, dashboards, params)


def athlete_workbook():
    tests = Source("test_results", "test_results.csv")
    tests.calc("latest_own_test", "Latest test for athlete", "boolean", "dimension", "nominal",
               "[date] = {FIXED [athlete_id] : MAX([date])}")
    series = Source("profile_series", "profile_series.csv")
    F = Field
    true = ["true"]
    # Once published, row security leaves each athlete one row. In Desktop, every athlete shows as a row.
    sheets = [
        Sheet("My latest jump", tests, rows=[F(tests, "name")], cols=[], mark="Text",
              encodings=[("text", F(tests, "athlete_sentence"))], filters=[(F(tests, "latest_own_test"), true)]),
        Sheet("My jump", series, rows=[F(series, "name"), F(series, "value", "Avg")],
              cols=[F(series, "date", "Day-Trunc", discrete=False)], mark="Line",
              encodings=[("color", F(series, "series"))], filters=[(F(series, "chart"), ['"jump"'])]),
        Sheet("My wellness", series, rows=[F(series, "name"), F(series, "value", "Avg")],
              cols=[F(series, "date", "Day-Trunc")], mark="Line", filters=[(F(series, "chart"), ['"wellness"'])]),
    ]
    dashboards = [("My data", ["My latest jump", "My jump", "My wellness"],
                   "Your own jump height and morning wellness, against your own usual range.", False)]
    write_workbook(OUT_DIR / "CustomAMS-athlete.twb", [tests, series], sheets, dashboards)


def main():
    athletes = pd.read_csv(ROOT / "data" / "metrics" / "athletes.csv", dtype=str, keep_default_na=False)
    OUT_DIR.mkdir(exist_ok=True)
    staff_workbook(athletes)
    athlete_workbook()


if __name__ == "__main__":
    main()
