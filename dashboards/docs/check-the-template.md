# Check the template

This guide is for maintainers. It shows how to rebuild every generated file and check it without Power BI Desktop or Tableau Desktop.

## Install the developer packages

The tests and the Power BI check need Python 3.10 or later. Install the developer packages once:

```bash
.venv/bin/pip install -r requirements-dev.txt
```

## Rebuild the generated files

Run these commands from the `dashboards` folder, in this order:

```bash
.venv/bin/python pipeline/make_sample_data.py
```

```bash
.venv/bin/python pipeline/build_metrics.py
```

```bash
.venv/bin/python scripts/build_powerbi.py
```

```bash
.venv/bin/python scripts/build_tableau.py
```

The Power BI and Tableau files read the column names of the metric files. Rebuild them after any change to `pipeline/build_metrics.py`.

## Run the tests

Run the known-answer tests for the metric layer:

```bash
.venv/bin/python -m pytest pipeline/tests
```

## Check the Power BI project

Download Microsoft's JSON schemas once, from github.com/microsoft/json-schemas, and unzip them. Then run the check with the path to the unzipped folder:

```bash
.venv/bin/python scripts/check_powerbi.py --schemas path/to/json-schemas-main
```

The check confirms three things:

- Every JSON file passes the Microsoft schema it names.
- Every field a visual uses exists in the semantic model.
- Every relationship, security rule, and DAX reference names a real table, column, or measure.

It does not parse the TMDL model files with Microsoft's own parser. Open the project in Power BI Desktop to confirm it loads.

## Check the Tableau workbooks

Download the official workbook schema `twb_2026.1.0.xsd` once, from github.com/tableau/tableau-document-schemas. Then run the check with its path:

```bash
.venv/bin/python scripts/check_tableau.py --xsd path/to/twb_2026.1.0.xsd
```

The check needs `xmllint`, which ships with macOS and most Linux systems. It confirms three things:

- Each workbook passes the official schema.
- Every field a sheet uses exists in its data source, and every calculation names real fields.
- Every CSV a data source reads exists, with the columns the workbook expects.

It does not prove that every sheet draws the way it should. Open each workbook in Tableau Desktop to confirm.
