#!/usr/bin/env python3
"""Check the Tableau workbooks without Tableau.

Runs three checks:

1. Schema: the workbook passes the official Tableau workbook XSD, from
   github.com/tableau/tableau-document-schemas, using `xmllint`.
2. Fields: every field a worksheet uses exists in its data source, every
   shelf names a field instance the worksheet declares, and every field a
   calculation names exists.
3. Files: every CSV a data source reads exists in data/metrics, with the
   columns the workbook expects.

This does not prove that Tableau opens the workbook. It catches the
structural mistakes that stop it from opening.

Run it from the repository root:

    python3 scripts/check_tableau.py --xsd /path/to/twb_2026.1.0.xsd

Exits with status 1 if any check fails.
"""

import argparse
import csv
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKBOOKS = sorted((ROOT / "tableau").glob("*.twb"))

# The official XSD imports two namespaces without a file location. These stubs let xmllint load it.
USER_STUB = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.tableausoftware.com/xml/user">
  <xs:attributeGroup name="UserAttributes-AG"><xs:anyAttribute namespace="##any" processContents="lax"/></xs:attributeGroup>
</xs:schema>
"""
XML_STUB = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.w3.org/XML/1998/namespace">
  <xs:attribute name="base" type="xs:anyURI"/><xs:attribute name="lang" type="xs:language"/>
</xs:schema>
"""


def check_schema(xsd, workbook):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "user.xsd").write_text(USER_STUB)
        (tmp / "xml.xsd").write_text(XML_STUB)
        text = Path(xsd).read_text(encoding="utf-8")
        text = text.replace('<xs:import namespace="http://www.tableausoftware.com/xml/user"/>',
                            '<xs:import namespace="http://www.tableausoftware.com/xml/user" schemaLocation="user.xsd"/>')
        text = text.replace('<xs:import namespace="http://www.w3.org/XML/1998/namespace"/>',
                            '<xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="xml.xsd"/>')
        (tmp / "twb.xsd").write_text(text, encoding="utf-8")
        r = subprocess.run(["xmllint", "--noout", "--schema", str(tmp / "twb.xsd"), str(workbook)],
                           capture_output=True, text=True)
    lines = [x for x in r.stderr.splitlines() if x.strip() and not x.endswith(" validates")]
    return lines


def check_fields(tree):
    errors = []
    sources = {}
    for ds in tree.getroot().find("datasources"):
        cols = {c.get("name") for c in ds.findall("column")}
        sources[ds.get("name")] = {"columns": cols, "node": ds}
        for c in ds.findall("column"):
            calc = c.find("calculation")
            if calc is None or ds.get("name") == "Parameters":
                continue
            for ref in re.findall(r"(?<!\.)\[([^\]\[]+)\]", calc.get("formula")):
                if f"[{ref}]" not in cols and ref not in ("Parameters", "athlete_choice"):
                    errors.append(f"data source {ds.get('name')}: calculation {c.get('name')} names [{ref}], which is not a field")
    for ws in tree.getroot().find("worksheets"):
        name = ws.get("name")
        deps = ws.find("table/view/datasource-dependencies")
        src = deps.get("datasource")
        if src not in sources:
            errors.append(f"worksheet {name}: data source {src} does not exist")
            continue
        declared = set()
        for inst in deps.findall("column-instance"):
            if inst.get("column") not in sources[src]["columns"]:
                errors.append(f"worksheet {name}: field {inst.get('column')} is not in {src}")
            declared.add(f"[{src}].{inst.get('name')}")
        used = []
        for shelf in ("rows", "cols"):
            text = ws.find(f"table/{shelf}").text or ""
            used += [x.strip() for x in text.split(" / ") if x.strip()]
        for node in ws.iter():
            for attr in ("column", "using"):
                v = node.get(attr)
                if v and v.startswith("[federated."):
                    used.append(v)
        for u in used:
            if u not in declared:
                errors.append(f"worksheet {name}: {u} is used but not declared")
    sheets = {ws.get("name") for ws in tree.getroot().find("worksheets")}
    for db in tree.getroot().find("dashboards"):
        for z in db.iter("zone"):
            if z.get("name") and z.get("name") not in sheets:
                errors.append(f"dashboard {db.get('name')}: zone names sheet {z.get('name')}, which does not exist")
    return errors


def check_files(tree, workbook):
    errors = []
    for ds in tree.getroot().find("datasources"):
        conn = ds.find(".//connection[@class='textscan']")
        if conn is None:
            continue
        path = (workbook.parent / conn.get("directory") / conn.get("filename")).resolve()
        if not path.exists():
            errors.append(f"data source {ds.get('name')}: {path} does not exist")
            continue
        with open(path, newline="", encoding="utf-8") as f:
            header = next(csv.reader(f))
        expected = [c.get("name") for c in ds.findall(".//relation/columns/column")]
        if header != expected:
            errors.append(f"data source {ds.get('name')}: CSV columns {header} differ from workbook columns {expected}")
    return errors


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--xsd", required=True, help="Path to twb_2026.1.0.xsd or a later version")
    args = p.parse_args()

    failed = not WORKBOOKS
    for workbook in WORKBOOKS:
        schema_errors = check_schema(args.xsd, workbook)
        tree = ET.parse(workbook)
        field_errors = check_fields(tree)
        file_errors = check_files(tree, workbook)
        print(f"{workbook.name}")
        print(f"  Schema: {Path(args.xsd).name}, {len(schema_errors)} errors")
        print(f"  Fields: {len(tree.getroot().find('worksheets'))} worksheets checked, {len(field_errors)} errors")
        print(f"  Files: {len(file_errors)} errors")
        for e in schema_errors + field_errors + file_errors:
            print("    " + e)
        failed = failed or bool(schema_errors or field_errors or file_errors)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
