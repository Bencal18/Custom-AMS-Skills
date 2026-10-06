#!/usr/bin/env python3
"""Check the Power BI project without Power BI Desktop.

Runs three checks:

1. Schemas: every JSON file in the project passes the Microsoft schema named
   in its `$schema` property, read from a local copy of
   github.com/microsoft/json-schemas.
2. Fields: every table, column, and measure a visual uses exists in the
   semantic model.
3. Model: every relationship and row-level security rule names a column or
   table that exists, and every measure reference in DAX names a measure that
   exists.

This does not prove that Power BI Desktop opens the project. It catches the
structural mistakes that stop it from opening.

Run it from the dashboards folder:

    python3 scripts/check_powerbi.py --schemas /path/to/json-schemas-main

Needs the `jsonschema` package. Exits with status 1 if any check fails.
"""

import argparse
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft7Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "powerbi"
PREFIX = "https://developer.microsoft.com/json-schemas/"


def load_registry(schemas_dir):
    def retrieve(uri):
        if not uri.startswith(PREFIX):
            raise LookupError(uri)
        path = Path(schemas_dir) / uri[len(PREFIX):]
        return Resource.from_contents(json.loads(path.read_text(encoding="utf-8")))
    return Registry(retrieve=retrieve)


def check_schemas(schemas_dir):
    registry = load_registry(schemas_dir)
    errors, count = [], 0
    for path in sorted(PROJECT.rglob("*")):
        if path.suffix not in (".json", ".pbip", ".pbir", ".pbism") and path.name != ".platform":
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        uri = doc.get("$schema") if isinstance(doc, dict) else None
        if not uri or not uri.startswith(PREFIX):
            continue
        schema = json.loads((Path(schemas_dir) / uri[len(PREFIX):]).read_text(encoding="utf-8"))
        count += 1
        for e in Draft7Validator(schema, registry=registry).iter_errors(doc):
            errors.append(f"{path.relative_to(ROOT)}: {'/'.join(map(str, e.absolute_path))}: {e.message[:200]}")
    return count, errors


def read_model():
    """Return {table: {"columns": set, "measures": set}} parsed from the TMDL table files."""
    model = {}
    for f in (PROJECT / "CustomAMS.SemanticModel" / "definition" / "tables").glob("*.tmdl"):
        text = f.read_text(encoding="utf-8")
        table = re.search(r"^table (.+)$", text, re.M).group(1).strip("'")
        cols = {m.strip("'") for m in re.findall(r"^\tcolumn (.+)$", text, re.M)}
        meas = {m.strip("'").replace("''", "'") for m in re.findall(r"^\tmeasure (.+?) =", text, re.M)}
        model[table] = {"columns": cols, "measures": meas, "text": text}
    return model


def walk_fields(obj, found):
    if isinstance(obj, dict):
        for kind in ("Column", "Measure"):
            if kind in obj and isinstance(obj[kind], dict) and "Property" in obj[kind]:
                ref = obj[kind]["Expression"].get("SourceRef", {})
                if "Entity" in ref:
                    found.append((kind, ref["Entity"], obj[kind]["Property"]))
        for v in obj.values():
            walk_fields(v, found)
    elif isinstance(obj, list):
        for v in obj:
            walk_fields(v, found)


def check_fields(model):
    errors, count = [], 0
    for path in (PROJECT / "CustomAMS.Report" / "definition" / "pages").rglob("visual.json"):
        found = []
        walk_fields(json.loads(path.read_text(encoding="utf-8")), found)
        for kind, table, prop in found:
            count += 1
            key = "columns" if kind == "Column" else "measures"
            if table not in model or prop not in model[table][key]:
                errors.append(f"{path.relative_to(ROOT)}: {kind.lower()} {table}.{prop} is not in the model")
    return count, errors


def check_model(model):
    errors = []
    defn = PROJECT / "CustomAMS.SemanticModel" / "definition"
    rel = (defn / "relationships.tmdl").read_text(encoding="utf-8")
    for ref in re.findall(r"(?:fromColumn|toColumn): (\S+)", rel):
        table, column = ref.split(".", 1)
        if table not in model or column not in model[table]["columns"]:
            errors.append(f"relationships.tmdl: {ref} is not in the model")
    for role in (defn / "roles").glob("*.tmdl"):
        for table, rule in re.findall(r"tablePermission (\S+) = (.+)", role.read_text(encoding="utf-8")):
            if table not in model:
                errors.append(f"{role.name}: table {table} is not in the model")
            for column in re.findall(r"\[([^\]]+)\]", rule):
                if column not in model.get(table, {}).get("columns", set()):
                    errors.append(f"{role.name}: column {table}[{column}] is not in the model")
    for table, m in model.items():
        clash = {x.lower() for x in m["measures"]} & {x.lower() for x in m["columns"]}
        for name in sorted(clash):
            errors.append(f"{table}.tmdl: measure and column share the name {name} (names ignore case)")
    all_measures = set().union(*(m["measures"] for m in model.values()))
    for table, m in model.items():
        # Measures come before the first column in each table file. Partitions hold Power Query, not DAX.
        body = m["text"].split("\n\tcolumn ", 1)[0]
        for t, c in re.findall(r"\b([a-z_]+)\[([^\]]+)\]", body):
            if t in model and c not in m["columns"] | model[t]["columns"]:
                errors.append(f"{table}.tmdl: DAX names column {t}[{c}], which is not in the model")
        for ref in re.findall(r"(?<![\w\]])\[([^\]]+)\]", body):
            if ref not in all_measures and not any(ref in x["columns"] for x in model.values()):
                errors.append(f"{table}.tmdl: DAX names [{ref}], which is not a measure or column")
    return errors


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--schemas", required=True, help="Folder of a github.com/microsoft/json-schemas checkout")
    args = p.parse_args()

    n_json, schema_errors = check_schemas(args.schemas)
    model = read_model()
    n_fields, field_errors = check_fields(model)
    model_errors = check_model(model)

    print(f"Schemas: {n_json} JSON files checked, {len(schema_errors)} errors")
    print(f"Fields: {n_fields} visual field references checked, {len(field_errors)} errors")
    print(f"Model: {len(model)} tables checked, {len(model_errors)} errors")
    for e in schema_errors + field_errors + model_errors:
        print("  " + e)
    sys.exit(1 if schema_errors or field_errors or model_errors else 0)


if __name__ == "__main__":
    main()
