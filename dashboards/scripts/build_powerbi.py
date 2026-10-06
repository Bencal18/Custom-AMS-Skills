#!/usr/bin/env python3
"""Generate the Power BI project (PBIP) for the Custom AMS dashboards.

The project is plain text: a semantic model in TMDL and a report in PBIR JSON.
Power BI Desktop opens `powerbi/CustomAMS.pbip`.

Run it from the dashboards folder after the metric layer is built:

    python3 pipeline/build_metrics.py
    python3 scripts/build_powerbi.py

The model reads the CSV headers in data/metrics, so it always
matches the files. Every measure only looks values up for the chosen athlete
and date. No metric is calculated in Power BI.
"""

import json
import re
import shutil
import uuid
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "powerbi"
NAME = "CustomAMS"
NS = uuid.UUID("5f1d7a52-7a2e-4c66-9d0b-6f7d0f1d2a10")

SCHEMA = "https://developer.microsoft.com/json-schemas/fabric"
V_REPORT = "3.0.0"
V_PAGE = "2.0.0"
V_VISUAL = "2.4.0"

# Table name: (folder, file). The DataFolder parameter points at data/metrics.
TABLES = {
    "athletes": ("metrics", "athletes.csv"),
    "settings": ("metrics", "settings.csv"),
    "import_log": ("metrics", "import_log.csv"),
    "dates": ("metrics", "dates.csv"),
    "athlete_day": ("metrics", "athlete_day.csv"),
    "wellness_scores": ("metrics", "wellness_scores.csv"),
    "test_results": ("metrics", "test_results.csv"),
    "weekly_load": ("metrics", "weekly_load.csv"),
    "reliability": ("metrics", "reliability.csv"),
    "test_day_summary": ("metrics", "test_day_summary.csv"),
    "data_quality": ("metrics", "data_quality.csv"),
}

DATE_COLUMNS = {"date", "week_start", "start_date", "end_date", "import_date", "cmj_date",
                "session_date", "measure_date", "imported_on"}

# Many side, one side.
RELATIONSHIPS = [
    ("athlete_day.athlete_id", "athletes.athlete_id"),
    ("athlete_day.date", "dates.date"),
    ("wellness_scores.athlete_id", "athletes.athlete_id"),
    ("wellness_scores.date", "dates.date"),
    ("test_results.athlete_id", "athletes.athlete_id"),
    ("test_results.date", "dates.date"),
    ("weekly_load.athlete_id", "athletes.athlete_id"),
    ("weekly_load.week_start", "dates.date"),
    ("data_quality.date", "dates.date"),
    ("test_day_summary.date", "dates.date"),
]

ACWR_NOTE = "ACWR describes how recent load compares with longer-term load. It does not predict injury."


def guid(*parts):
    return str(uuid.uuid5(NS, "/".join(parts)))


def q(name):
    """Quote a TMDL object name when it holds anything but letters, digits, and underscores."""
    return name if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name) else "'" + name.replace("'", "''") + "'"


# ---------------------------------------------------------------------------
# Measures. Each one looks a value up. None calculates a metric.
# ---------------------------------------------------------------------------

def lookup_on_day(table, column):
    return (f"VAR d = [As of date]\n"
            f"RETURN\n"
            f"    CALCULATE ( SELECTEDVALUE ( {table}[{column}] ), REMOVEFILTERS ( dates ), {table}[date] = d )")


def one_athlete(table, column):
    return f"IF ( HASONEVALUE ( athletes[athlete_id] ), SELECTEDVALUE ( {table}[{column}] ) )"


def on_test_day(column):
    return (f"VAR t = [Test day shown]\n"
            f"RETURN\n"
            f"    CALCULATE ( SELECTEDVALUE ( test_results[{column}] ), REMOVEFILTERS ( test_results[date] ), "
            f"REMOVEFILTERS ( dates ), test_results[date] = t )")


def count_on_day(status):
    return (f"VAR d = [As of date]\n"
            f"RETURN\n"
            f"    CALCULATE ( COUNTROWS ( athlete_day ), REMOVEFILTERS ( dates ), REMOVEFILTERS ( athletes ), "
            f"athlete_day[date] = d, athlete_day[availability] = \"{status}\" ) + 0")


MEASURES = {
    "athlete_day": [
        ("As of date", "IF (\n    HASONEVALUE ( dates[date] ),\n    VALUES ( dates[date] ),\n"
                       "    CALCULATE ( MAX ( athlete_day[date] ), REMOVEFILTERS () )\n)", "yyyy-mm-dd"),
        ("As of label", "\"As of \" & FORMAT ( [As of date], \"yyyy-mm-dd\" )", None),
        ("Availability status", lookup_on_day("athlete_day", "availability"), None),
        ("Form submitted", lookup_on_day("athlete_day", "form_submitted"), None),
        ("Wellness total (points)", lookup_on_day("athlete_day", "wellness_total"), "0"),
        ("Wellness change (points)", lookup_on_day("athlete_day", "wellness_change_points"), "+0.0;-0.0;0.0"),
        ("Wellness z", lookup_on_day("athlete_day", "wellness_total_z"), "+0.00;-0.00;0.00"),
        ("Wellness status", lookup_on_day("athlete_day", "wellness_status"), None),
        ("Wellness review", lookup_on_day("athlete_day", "wellness_review"), None),
        ("Acute load (AU)", lookup_on_day("athlete_day", "acute_load_au"), "#,0.00"),
        ("Chronic load (AU)", lookup_on_day("athlete_day", "chronic_load_au"), "#,0.00"),
        ("ACWR, rolling coupled 7:28", lookup_on_day("athlete_day", "acwr_coupled"), "0.00"),
        ("Last jump date", lookup_on_day("athlete_day", "cmj_date"), "yyyy-mm-dd"),
        ("Last jump (cm)", lookup_on_day("athlete_day", "cmj_cm"), "0.0"),
        ("Jump change (cm)", lookup_on_day("athlete_day", "cmj_change_cm"), "+0.0;-0.0;0.0"),
        ("Jump noise band (cm)", lookup_on_day("athlete_day", "cmj_noise_band_cm"), "0.0"),
        ("Jump state", lookup_on_day("athlete_day", "cmj_wording"), None),
        ("Jump change vs band, chosen direction", lookup_on_day("athlete_day", "cmj_change_vs_band_chosen"), "0.00"),
        ("Athletes full", count_on_day("full"), "0"),
        ("Athletes modified", count_on_day("modified"), "0"),
        ("Athletes out", count_on_day("out"), "0"),
        ("Availability summary", "[Athletes full] & \" full, \" & [Athletes modified] & \" modified, \" & "
                                 "[Athletes out] & \" out\"", None),
        ("Daily load (AU)", one_athlete("athlete_day", "srpe_load_au"), "#,0"),
        ("Acute load, one athlete (AU)", one_athlete("athlete_day", "acute_load_au"), "#,0.00"),
        ("Chronic load, one athlete (AU)", one_athlete("athlete_day", "chronic_load_au"), "#,0.00"),
        ("Wellness total, one athlete (points)", one_athlete("athlete_day", "wellness_total"), "0"),
        ("Wellness z by day", "SELECTEDVALUE ( athlete_day[wellness_total_z] )", "+0.0;-0.0;0.0"),
        ("Athletes full by day", "CALCULATE ( COUNTROWS ( athlete_day ), athlete_day[availability] = \"full\" ) + 0", "0"),
        ("Athletes modified by day", "CALCULATE ( COUNTROWS ( athlete_day ), athlete_day[availability] = \"modified\" ) + 0", "0"),
        ("Athletes out by day", "CALCULATE ( COUNTROWS ( athlete_day ), athlete_day[availability] = \"out\" ) + 0", "0"),
    ],
    "data_quality": [
        ("Forms received", "VAR d = [As of date]\nRETURN\n    CALCULATE ( SELECTEDVALUE ( data_quality[forms_label] ), "
                           "REMOVEFILTERS ( dates ), data_quality[date] = d )", None),
        ("Last successful import", "VAR d = [As of date]\nRETURN\n    CALCULATE ( SELECTEDVALUE ( data_quality[last_ok_import] ), "
                                   "REMOVEFILTERS ( dates ), data_quality[date] = d )", None),
        ("Form completion (%)", "SELECTEDVALUE ( data_quality[form_completion_pct] )", "0"),
        ("Rating completion (%)", "SELECTEDVALUE ( data_quality[rating_completion_pct] )", "0"),
        ("Device failure rows", "SELECTEDVALUE ( data_quality[device_failure_rows] )", "0"),
    ],
    "test_day_summary": [
        ("Jump flags, last test day", "VAR d = [As of date]\n"
                                      "VAR t = CALCULATE ( MAX ( test_day_summary[date] ), REMOVEFILTERS ( dates ), test_day_summary[date] <= d )\n"
                                      "RETURN\n    IF (\n        NOT ISBLANK ( t ),\n        CALCULATE ( SELECTEDVALUE ( test_day_summary[summary_label] ), REMOVEFILTERS ( dates ), "
                                      "test_day_summary[date] = t ) & \" (\" & FORMAT ( t, \"yyyy-mm-dd\" ) & \")\"\n    )", None),
        ("Jump flags, test day shown", "VAR t = [Test day shown]\nRETURN\n    CALCULATE ( SELECTEDVALUE ( test_day_summary[summary_label] ), "
                                       "REMOVEFILTERS ( dates ), test_day_summary[date] = t )", None),
    ],
    "test_results": [
        ("Test day shown", "VAR picked = CALCULATE ( SELECTEDVALUE ( test_results[date] ), REMOVEFILTERS ( athletes ) )\n"
                           "RETURN\n    IF ( ISBLANK ( picked ), CALCULATE ( MAX ( test_results[date] ), REMOVEFILTERS () ), picked )",
         "yyyy-mm-dd"),
        ("Jump on test day (cm)", on_test_day("value"), "0.0"),
        ("Baseline mean (cm)", on_test_day("baseline_mean"), "0.0"),
        ("Baseline tests", on_test_day("baseline_n"), "0"),
        ("Change on test day (cm)", on_test_day("change"), "+0.0;-0.0;0.0"),
        ("Noise band on test day (cm)", on_test_day("noise_band"), "0.0"),
        ("State on test day", on_test_day("wording"), None),
        ("Change vs band on test day, chosen direction", on_test_day("change_vs_band_chosen"), "0.00"),
        ("Jump height, one athlete (cm)", one_athlete("test_results", "value"), "0.0"),
        ("Band low, one athlete (cm)", one_athlete("test_results", "band_low_cm"), "0.0"),
        ("Band high, one athlete (cm)", one_athlete("test_results", "band_high_cm"), "0.0"),
        ("Latest jump sentence", "IF (\n    HASONEVALUE ( athletes[athlete_id] ),\n"
                                 "    VAR t = CALCULATE ( MAX ( test_results[date] ), REMOVEFILTERS ( dates ), REMOVEFILTERS ( test_results[date] ) )\n"
                                 "    RETURN\n        CALCULATE ( SELECTEDVALUE ( test_results[athlete_sentence] ), "
                                 "REMOVEFILTERS ( dates ), test_results[date] = t )\n)", None),
    ],
    "wellness_scores": [
        ("Wellness answer, one athlete", one_athlete("wellness_scores", "answer"), "0"),
    ],
    "weekly_load": [
        ("Week load label", "SELECTEDVALUE ( weekly_load[week_label] )", None),
    ],
    "reliability": [
        ("Typical error label", "VAR r = SELECTEDVALUE ( reliability[te_source] )\n"
                                "RETURN\n    \"Typical error \" & FORMAT ( SELECTEDVALUE ( reliability[te] ), \"0.00\" ) & "
                                "\" cm. Smallest worthwhile change \" & FORMAT ( SELECTEDVALUE ( reliability[swc] ), \"0.00\" ) & \" cm. \" & r", None),
    ],
    "settings": [
        ("Wellness review value", "\"Staff review at a total wellness z-score of \" & "
                                  "CALCULATE ( SELECTEDVALUE ( settings[value] ), settings[setting] = \"wellness_review_z\" ) & "
                                  "\" or lower. \" & CALCULATE ( SELECTEDVALUE ( settings[meaning] ), settings[setting] = \"wellness_review_z\" )", None),
    ],
}


# ---------------------------------------------------------------------------
# Semantic model (TMDL)
# ---------------------------------------------------------------------------

def column_type(name, values):
    if name in DATE_COLUMNS:
        return "dateTime"
    vals = [v for v in values if v not in ("", "NA")]
    if not vals:
        return "string"
    try:
        nums = [float(v) for v in vals]
    except ValueError:
        return "string"
    if name.endswith("_id"):
        return "string"
    if all(float(n).is_integer() for n in nums) and all("." not in v for v in vals):
        return "int64"
    return "double"


def m_type(dtype):
    return {"dateTime": "type date", "int64": "Int64.Type", "double": "type number", "string": "type text"}[dtype]


# Columns the metric layer adds for tools that cannot join. Power BI reads them from athletes instead.
NAME_COLUMNS = ["name", "group", "email"]


def table_tmdl(table, folder, file):
    df = pd.read_csv(ROOT / "data" / folder / file, dtype=str, keep_default_na=False)
    if table != "athletes":
        df = df.drop(columns=[c for c in NAME_COLUMNS if c in df.columns])
    cols = [(c, column_type(c, df[c].tolist())) for c in df.columns]
    lines = [f"table {q(table)}", f"\tlineageTag: {guid('table', table)}", ""]

    for mname, expr, fmt in MEASURES.get(table, []):
        expr_lines = expr.split("\n")
        if len(expr_lines) == 1:
            lines.append(f"\tmeasure {q(mname)} = {expr}")
        else:
            lines.append(f"\tmeasure {q(mname)} =")
            lines += ["\t\t\t" + x for x in expr_lines]
        if fmt:
            lines.append(f"\t\tformatString: {fmt}")
        lines.append(f"\t\tlineageTag: {guid('measure', table, mname)}")
        lines.append("")

    for c, t in cols:
        lines.append(f"\tcolumn {q(c)}")
        lines.append(f"\t\tdataType: {t}")
        if t == "dateTime":
            lines.append("\t\tformatString: yyyy-mm-dd")
        if table == "athletes" and c == "athlete_id" or table == "dates" and c == "date":
            lines.append("\t\tisKey")
        lines.append(f"\t\tlineageTag: {guid('column', table, c)}")
        lines.append("\t\tsummarizeBy: none")
        lines.append(f"\t\tsourceColumn: {c}")
        lines.append("")
        lines.append("\t\tannotation SummarizationSetBy = User")
        lines.append("")
        if t == "dateTime":
            lines.append("\t\tannotation UnderlyingDateTimeDataType = Date")
            lines.append("")

    typed = ", ".join(f'{{"{c}", {m_type(t)}}}' for c, t in cols)
    nontext = ", ".join(f'"{c}"' for c, t in cols if t != "string")
    m = [
        "let",
        f'    Source = Csv.Document(File.Contents(DataFolder & "{file}"), [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]),',
        "    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),",
        "    Headers = Table.SelectColumns(Promoted, {" + ", ".join(f'"{c}"' for c, _ in cols) + "}),",
    ]
    if nontext:
        m += [
            f'    NoEmpty = Table.ReplaceValue(Headers, "", null, Replacer.ReplaceValue, {{{nontext}}}),',
            f'    NoNA = Table.ReplaceValue(NoEmpty, "NA", null, Replacer.ReplaceValue, {{{nontext}}}),',
            f'    Typed = Table.TransformColumnTypes(NoNA, {{{typed}}}, "en-US")',
        ]
    else:
        m.append(f'    Typed = Table.TransformColumnTypes(Headers, {{{typed}}}, "en-US")')
    m += ["in", "    Typed"]
    lines.append(f"\tpartition {q(table)} = m")
    lines.append("\t\tmode: import")
    lines.append("\t\tsource =")
    lines += ["\t\t\t\t" + x for x in m]
    lines.append("")
    lines.append("\tannotation PBI_ResultType = Table")
    lines.append("")
    return "\n".join(lines), cols


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    # UTF-8 without a byte order mark, as the PBIP docs require.
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def write_json(path, obj):
    write(path, json.dumps(obj, indent=2, ensure_ascii=False))


def build_model():
    base = OUT / f"{NAME}.SemanticModel"
    defn = base / "definition"
    write_json(base / "definition.pbism", {
        "$schema": f"{SCHEMA}/item/semanticModel/definitionProperties/1.0.0/schema.json",
        "version": "4.2", "settings": {}})
    write_json(base / ".platform", {
        "$schema": f"{SCHEMA}/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "SemanticModel", "displayName": NAME},
        "config": {"version": "2.0", "logicalId": guid("item", "model")}})
    write(defn / "database.tmdl", "database\n\tcompatibilityLevel: 1601\n")
    order = ["DataFolder"] + list(TABLES)
    model = [
        "model Model",
        "\tculture: en-US",
        "\tdefaultPowerBIDataSourceVersion: powerBI_V3",
        "\tsourceQueryCulture: en-US",
        "\tdataAccessOptions",
        "\t\tlegacyRedirects",
        "\t\treturnErrorValuesAsNull",
        "",
        "annotation __PBI_TimeIntelligenceEnabled = 0",
        "",
        "annotation PBI_QueryOrder = " + json.dumps(order),
        "",
    ]
    model += [f"ref table {q(t)}" for t in TABLES]
    model += ["", "ref role Staff", "ref role Athlete", ""]
    write(defn / "model.tmdl", "\n".join(model))
    write(defn / "expressions.tmdl", "\n".join([
        'expression DataFolder = "C:\\Custom-AMS-Skills\\dashboards\\data\\metrics\\" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]',
        f"\tlineageTag: {guid('expression', 'DataFolder')}",
        "",
        "\tannotation PBI_ResultType = Text",
        "",
    ]))
    schema = {}
    for table, (folder, file) in TABLES.items():
        text, cols = table_tmdl(table, folder, file)
        schema[table] = {"columns": [c for c, _ in cols], "measures": [m for m, _, _ in MEASURES.get(table, [])]}
        write(defn / "tables" / f"{table}.tmdl", text)
    rel = []
    for frm, to in RELATIONSHIPS:
        rel += [f"relationship {guid('rel', frm, to)}", f"\tfromColumn: {frm}", f"\ttoColumn: {to}", ""]
    write(defn / "relationships.tmdl", "\n".join(rel))
    write(defn / "roles" / "Staff.tmdl", "\n".join([
        "/// Staff see every athlete. Give this role only to staff who need it.",
        "role Staff", "\tmodelPermission: read", ""]))
    write(defn / "roles" / "Athlete.tmdl", "\n".join([
        "/// Athletes see only their own rows. The email column must hold the value USERPRINCIPALNAME() returns.",
        "role Athlete",
        "\tmodelPermission: read",
        "",
        "\ttablePermission athletes = [email] = USERPRINCIPALNAME()",
        "",
        "\ttablePermission data_quality = FALSE()",
        "",
        "\ttablePermission test_day_summary = FALSE()",
        "",
        "\ttablePermission import_log = FALSE()",
        "",
    ]))
    return schema


# ---------------------------------------------------------------------------
# Report (PBIR)
# ---------------------------------------------------------------------------

def col(table, name):
    return {"Column": {"Expression": {"SourceRef": {"Entity": table}}, "Property": name}}


def mea(table, name):
    return {"Measure": {"Expression": {"SourceRef": {"Entity": table}}, "Property": name}}


def proj(field, display=None):
    kind = "Column" if "Column" in field else "Measure"
    table = field[kind]["Expression"]["SourceRef"]["Entity"]
    prop = field[kind]["Property"]
    p = {"field": field, "queryRef": f"{table}.{prop}", "nativeQueryRef": prop}
    if display:
        p["displayName"] = display
    return p


def lit(value):
    return {"expr": {"Literal": {"Value": value}}}


def title(text):
    return {"title": [{"properties": {"show": lit("true"), "text": lit("'" + text.replace("'", "''") + "'")}}]}


class Page:
    def __init__(self, name, display):
        self.name, self.display, self.visuals = name, display, []

    def add(self, vname, x, y, w, h, visual, filters=None):
        v = {
            "$schema": f"{SCHEMA}/item/report/definition/visualContainer/{V_VISUAL}/schema.json",
            "name": vname,
            "position": {"x": x, "y": y, "z": len(self.visuals) * 1000, "width": w, "height": h,
                         "tabOrder": len(self.visuals) * 1000},
            "visual": visual,
        }
        if filters:
            v["filterConfig"] = {"filters": filters}
        self.visuals.append(v)


NO_TOTALS = {"subTotals": [{"properties": {"rowSubtotals": {"expr": {"Literal": {"Value": "false"}}},
                                           "columnSubtotals": {"expr": {"Literal": {"Value": "false"}}}}}]}


def visual(vtype, roles, heading=None, sort=None, objects=None):
    if vtype == "pivotTable":
        objects = {**NO_TOTALS, **(objects or {})}
    v = {"visualType": vtype,
         "query": {"queryState": {r: {"projections": ps} for r, ps in roles.items()}},
         "drillFilterOtherVisuals": True}
    if sort:
        v["query"]["sortDefinition"] = {"sort": sort, "isDefaultSort": False}
    if objects:
        v["objects"] = objects
    if heading:
        v["visualContainerObjects"] = title(heading)
    return v


def textbox(text):
    return {"visualType": "textbox", "objects": {"general": [{"properties": {
        "paragraphs": [{"textRuns": [{"value": t}]} for t in text.split("\n")]}}]}}


def slicer(field, heading):
    return visual("slicer", {"Values": [proj(field)]}, heading, objects={
        "data": [{"properties": {"mode": lit("'Dropdown'")}}],
        "selection": [{"properties": {"strictSingleSelect": lit("true")}}],
    })


def card(field, heading):
    return visual("card", {"Values": [proj(field)]}, heading,
                  objects={"categoryLabels": [{"properties": {"show": lit("false")}}]})


def in_filter(name, table, column, values):
    return {
        "name": name,
        "field": col(table, column),
        "type": "Categorical",
        "filter": {
            "Version": 2,
            "From": [{"Name": "t", "Entity": table, "Type": 0}],
            "Where": [{"Condition": {"In": {
                "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "t"}}, "Property": column}}],
                "Values": [[{"Literal": {"Value": "'" + v + "'"}}] for v in values]}}}],
        },
    }


def diverging_fill(measure_field, queryref):
    color = lambda hexv: {"Literal": {"Value": f"'{hexv}'"}}  # noqa: E731
    return {"values": [{
        "properties": {"backColor": {"solid": {"color": {"expr": {"FillRule": {
            "Input": measure_field,
            "FillRule": {"linearGradient3": {
                "min": {"color": color("#E69F00"), "value": {"Literal": {"Value": "-3D"}}},
                "mid": {"color": color("#FFFFFF"), "value": {"Literal": {"Value": "0D"}}},
                "max": {"color": color("#56B4E9"), "value": {"Literal": {"Value": "3D"}}},
                "nullColoringStrategy": {"strategy": {"Literal": {"Value": "'noColor'"}}},
            }},
        }}}}}},
        "selector": {"data": [{"dataViewWildcard": {"matchingOption": 1}}], "metadata": queryref},
    }]}


def build_pages():
    A = "athlete_day"
    pages = []

    # 1. Squad board
    p = Page("squad_board", "Squad board")
    p.add("title", 16, 8, 900, 48, textbox("Squad board. One row for each athlete on the chosen day. Pick a day, or leave it blank for the latest day."))
    p.add("date", 940, 8, 324, 64, slicer(col("dates", "date"), "Day"))
    p.add("asof", 16, 64, 240, 80, card(mea(A, "As of label"), "Day shown"))
    p.add("avail", 264, 64, 300, 80, card(mea(A, "Availability summary"), "Availability"))
    p.add("forms", 572, 64, 200, 80, card(mea("data_quality", "Forms received"), "Forms received"))
    p.add("flags", 780, 64, 484, 80, card(mea("test_day_summary", "Jump flags, last test day"), "Jump tests"))
    board = [proj(col("athletes", "name"), "Athlete"), proj(col("athletes", "group"), "Group")] + [
        proj(mea(A, m)) for m in [
            "Availability status", "Form submitted", "Wellness total (points)", "Wellness change (points)",
            "Wellness z", "Wellness status", "Wellness review", "Acute load (AU)", "Chronic load (AU)",
            "ACWR, rolling coupled 7:28", "Last jump date", "Jump change (cm)", "Jump noise band (cm)", "Jump state",
            "Jump change vs band, chosen direction"]]
    p.add("board", 16, 152, 1248, 500, visual(
        "tableEx", {"Values": board}, "Athletes, largest jump change in the chosen direction against the noise band first",
        sort=[{"field": mea(A, "Jump change vs band, chosen direction"), "direction": "Descending"}]))
    p.add("note", 16, 660, 1248, 52, textbox(
        ACWR_NOTE + " Wellness z compares today's total with the athlete's own last 28 days. "
        "Jump state compares the latest test with the athlete's baseline and the noise band. Show this board to staff only."))
    pages.append(p)

    # 2. Athlete profile
    p = Page("athlete_profile", "Athlete profile")
    p.add("athlete", 16, 8, 320, 64, slicer(col("athletes", "name"), "Athlete"))
    p.add("intro", 352, 8, 912, 64, textbox("Pick one athlete. Every chart compares the athlete with their own data. Rest days show as 0. Missing days show as gaps."))
    p.add("load", 16, 80, 760, 300, visual("lineClusteredColumnComboChart", {
        "Category": [proj(col("dates", "date"))],
        "ColumnY": [proj(mea(A, "Daily load (AU)"))],
        "Y": [proj(mea(A, "Acute load, one athlete (AU)")), proj(mea(A, "Chronic load, one athlete (AU)"))],
    }, "Daily session RPE load, with 7-day and 28-day mean daily load"))
    p.add("jump", 784, 80, 480, 300, visual("lineChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea("test_results", "Jump height, one athlete (cm)")),
              proj(mea("test_results", "Band low, one athlete (cm)")),
              proj(mea("test_results", "Band high, one athlete (cm)"))],
    }, "Jump height against the baseline noise band (cm)"))
    p.add("wellness", 16, 388, 760, 324, visual("pivotTable", {
        "Rows": [proj(col("wellness_scores", "item"), "Item")],
        "Columns": [proj(col("dates", "date"))],
        "Values": [proj(mea("wellness_scores", "Wellness answer, one athlete"), "Answer")],
    }, "Wellness answers, last 28 days (5 is best)"), filters=[in_filter("last28", "dates", "in_last_28_days", ["yes"])])
    p.add("tests", 784, 388, 480, 324, visual("tableEx", {"Values": [
        proj(col("athletes", "name"), "Athlete"), proj(col("test_results", "date"), "Test day"), proj(col("test_results", "value"), "Jump (cm)"),
        proj(col("test_results", "change"), "Change (cm)"), proj(col("test_results", "noise_band"), "Noise band (cm)"),
        proj(col("test_results", "wording"), "State")]}, "Jump tests"))
    pages.append(p)

    # 3. Load
    p = Page("load", "Load")
    p.add("intro", 16, 8, 1248, 56, textbox(
        "Weekly session RPE load for each athlete, Monday to Sunday, with the number of days that have complete data. "
        "Do not compare a week with missing days with a complete week.\n" + ACWR_NOTE))
    p.add("weeks", 16, 72, 1248, 640, visual("pivotTable", {
        "Rows": [proj(col("athletes", "name"), "Athlete")],
        "Columns": [proj(col("weekly_load", "week_start"), "Week starting")],
        "Values": [proj(mea("weekly_load", "Week load label"), "Load")],
    }, "Weekly load (AU) and days complete"))
    pages.append(p)

    # 4. Wellness and check-ins
    p = Page("wellness", "Wellness and check-ins")
    p.add("intro", 16, 8, 800, 56, textbox(
        "Total wellness z-score for each athlete and day, against the athlete's own previous 28 days. "
        "Orange is below the athlete's usual answers, blue is above. The number is in every cell."))
    p.add("review", 824, 8, 440, 56, card(mea("settings", "Wellness review value"), "Review value set by staff"))
    p.add("grid", 16, 72, 1248, 440, visual("pivotTable", {
        "Rows": [proj(col("athletes", "name"), "Athlete")],
        "Columns": [proj(col("dates", "date"))],
        "Values": [proj(mea(A, "Wellness z by day"), "z")],
    }, "Total wellness z-score, last 28 days", objects=diverging_fill(mea(A, "Wellness z by day"), f"{A}.Wellness z by day")),
        filters=[in_filter("last28", "dates", "in_last_28_days", ["yes"])])
    p.add("completion", 16, 520, 1248, 192, visual("lineChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea("data_quality", "Form completion (%)"))],
    }, "Forms received out of forms expected (%)"))
    pages.append(p)

    # 5. Testing
    p = Page("testing", "Testing")
    p.add("day", 16, 8, 320, 64, slicer(col("test_results", "date"), "Test day"))
    p.add("summary", 344, 8, 440, 64, card(mea("test_day_summary", "Jump flags, test day shown"), "Results beyond the noise band"))
    p.add("te", 792, 8, 472, 64, card(mea("reliability", "Typical error label"), "Measurement error"))
    p.add("bars", 16, 80, 560, 632, visual("clusteredBarChart", {
        "Category": [proj(col("athletes", "name"), "Athlete")],
        "Y": [proj(mea("test_results", "Change on test day (cm)"))],
        "Tooltips": [proj(mea("test_results", "Change vs band on test day, chosen direction"))],
    }, "Change in jump height from baseline (cm)",
        sort=[{"field": mea("test_results", "Change vs band on test day, chosen direction"), "direction": "Descending"}]))
    p.add("table", 584, 80, 680, 560, visual("tableEx", {"Values": [
        proj(col("athletes", "name"), "Athlete")] + [proj(mea("test_results", m)) for m in [
            "Jump on test day (cm)", "Baseline mean (cm)", "Baseline tests", "Change on test day (cm)",
            "Noise band on test day (cm)", "State on test day", "Change vs band on test day, chosen direction"]]}, "Change against measurement error",
        sort=[{"field": mea("test_results", "Change vs band on test day, chosen direction"), "direction": "Descending"}]))
    p.add("note", 584, 648, 680, 64, textbox(
        "Repeat a test before anyone acts on a single flag. The chance count assumes the noise band holds and counts only the direction the card above names."))
    pages.append(p)

    # 6. Availability
    p = Page("availability", "Availability")
    p.add("intro", 16, 8, 1248, 40, textbox("Athletes who are full, modified, or out each day. This page shows status only, never a diagnosis."))
    p.add("chart", 16, 56, 1248, 360, visual("columnChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea(A, "Athletes full by day")), proj(mea(A, "Athletes modified by day")),
              proj(mea(A, "Athletes out by day"))],
    }, "Athletes by availability"))
    p.add("list", 16, 424, 1248, 288, visual("tableEx", {"Values": [
        proj(col(A, "date"), "Day"), proj(col("athletes", "name"), "Athlete"), proj(col(A, "availability"), "Status")]},
        "Days modified or out"), filters=[in_filter("notfull", A, "availability", ["modified", "out"])])
    pages.append(p)

    # 7. Data health
    p = Page("data_health", "Data health")
    p.add("intro", 16, 8, 800, 56, textbox("Check this page first. A complete-looking board built on a failed import is wrong without any error message."))
    p.add("last", 824, 8, 440, 56, card(mea("data_quality", "Last successful import"), "Last successful import"))
    p.add("completion", 16, 72, 624, 300, visual("lineChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea("data_quality", "Form completion (%)")), proj(mea("data_quality", "Rating completion (%)"))],
    }, "Form and rating completion (%)"))
    p.add("failures", 648, 72, 616, 300, visual("columnChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea("data_quality", "Device failure rows"))],
    }, "Device failure rows"))
    p.add("log", 16, 380, 1248, 332, visual("tableEx", {"Values": [
        proj(col("import_log", c)) for c in ["import_id", "import_date", "import_time_local", "source", "rows_imported", "result"]]},
        "Import log, newest first", sort=[{"field": col("import_log", "import_id"), "direction": "Descending"}]))
    pages.append(p)

    # 8. My data
    p = Page("my_data", "My data")
    p.add("athlete", 16, 8, 320, 64, slicer(col("athletes", "name"), "Athlete (athletes see only themselves)"))
    p.add("sentence", 344, 8, 920, 64, card(mea("test_results", "Latest jump sentence"), "Your latest jump test"))
    p.add("jump", 16, 80, 1248, 300, visual("lineChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea("test_results", "Jump height, one athlete (cm)"), "Your jump height (cm)"),
              proj(mea("test_results", "Band low, one athlete (cm)"), "Usual range, low"),
              proj(mea("test_results", "Band high, one athlete (cm)"), "Usual range, high")],
    }, "Your jump height and your usual range"))
    p.add("wellness", 16, 388, 1248, 324, visual("lineChart", {
        "Category": [proj(col("dates", "date"))],
        "Y": [proj(mea(A, "Wellness total, one athlete (points)"), "Your wellness total (points)")],
    }, "Your morning wellness total (5 to 25, higher is better)"))
    pages.append(p)
    return pages


def build_report():
    base = OUT / f"{NAME}.Report"
    defn = base / "definition"
    write_json(base / "definition.pbir", {
        "$schema": f"{SCHEMA}/item/report/definitionProperties/2.0.0/schema.json",
        "version": "4.0",
        "datasetReference": {"byPath": {"path": f"../{NAME}.SemanticModel"}}})
    write_json(base / ".platform", {
        "$schema": f"{SCHEMA}/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "Report", "displayName": NAME},
        "config": {"version": "2.0", "logicalId": guid("item", "report")}})
    write_json(defn / "version.json", {
        "$schema": f"{SCHEMA}/item/report/definition/versionMetadata/1.0.0/schema.json", "version": "2.0.0"})
    write_json(defn / "report.json", {
        "$schema": f"{SCHEMA}/item/report/definition/report/{V_REPORT}/schema.json",
        # No theme file is referenced. Microsoft supports edits to theme resources only after Power BI
        # Desktop registers them, so the color-blind-safe theme ships as powerbi/CustomAMS-theme.json
        # for you to import with View, Themes, Browse for themes.
        "themeCollection": {},
        "settings": {"useStylableVisualContainerHeader": True, "exportDataMode": "AllowSummarized"},
    })
    write_json(OUT / "CustomAMS-theme.json", {
        "name": "Custom AMS",
        "dataColors": ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00", "#F0E442", "#000000"],
        "background": "#FFFFFF", "foreground": "#1F1F1F", "tableAccent": "#0072B2",
    })
    pages = build_pages()
    write_json(defn / "pages" / "pages.json", {
        "$schema": f"{SCHEMA}/item/report/definition/pagesMetadata/1.0.0/schema.json",
        "pageOrder": [p.name for p in pages], "activePageName": pages[0].name})
    for p in pages:
        write_json(defn / "pages" / p.name / "page.json", {
            "$schema": f"{SCHEMA}/item/report/definition/page/{V_PAGE}/schema.json",
            "name": p.name, "displayName": p.display, "displayOption": "FitToPage", "height": 720, "width": 1280})
        for v in p.visuals:
            write_json(defn / "pages" / p.name / "visuals" / v["name"] / "visual.json", v)
    return pages


def main():
    if OUT.exists():
        for item in [f"{NAME}.SemanticModel", f"{NAME}.Report"]:
            shutil.rmtree(OUT / item, ignore_errors=True)
    OUT.mkdir(exist_ok=True)
    write_json(OUT / f"{NAME}.pbip", {
        "$schema": f"{SCHEMA}/pbip/pbipProperties/1.0.0/schema.json",
        "version": "1.0", "artifacts": [{"report": {"path": f"{NAME}.Report"}}],
        "settings": {"enableAutoRecovery": True}})
    write(OUT / ".gitignore", "**/.pbi/localSettings.json\n**/.pbi/cache.abf\n")
    schema = build_model()
    pages = build_report()
    print(f"{len(schema)} tables, {sum(len(v['measures']) for v in schema.values())} measures, "
          f"{len(pages)} pages, {sum(len(p.visuals) for p in pages)} visuals")


if __name__ == "__main__":
    main()
