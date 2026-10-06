# Contribute to Custom AMS Dashboards

Reports from people who open the template in Power BI or Tableau make it better. This page explains how to report a problem and how to propose a change.

## Report a problem

Open an issue. Include these details:

- The tool and its version, such as Power BI Desktop for September 2026 or Tableau Desktop 2026.2.
- The page or dashboard, and what you expected to see.
- The exact error message, if there is one.

Never paste real athlete data into an issue or a pull request. Use the sample data, or made-up numbers.

## Propose a change

Follow these steps to propose a change:

1. Fork the repository, and create a branch for your change.
2. Change a formula only in `pipeline/build_metrics.py`, and add a known-answer test in `pipeline/tests/test_metrics.py`.
3. Change a page only in `scripts/build_powerbi.py` or `scripts/build_tableau.py`. Do not edit the generated files by hand.
4. Rebuild and check every generated file, as [Check the template](docs/check-the-template.md) describes.
5. Open a pull request. Say what changed and why, and list any source for a formula.

## Meet the content rules

Every change must meet these rules:

- Calculate each metric once, in the metric layer. Dashboards only look values up.
- Cite a source for every formula, threshold, and range. The methods follow the skills in this repository, and [`docs/calculations.md`](../docs/calculations.md).
- Frame results as decision support. Do not add diagnosis, injury prediction, or return-to-sport clearance.
- Name no commercial product as better or worse than another. Promote nothing.
- Use made-up data only.

## License your contribution

By contributing, you agree to license your contribution under the same terms as the repository. See [LICENSE.md](LICENSE.md).
