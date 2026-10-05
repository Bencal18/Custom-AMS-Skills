# Contribute to Custom AMS Skills

Corrections and new content from coaches, sports scientists, and researchers make these skills better. This page explains how to report a problem, how to propose a change, and the rules every change must meet.

## Report a problem

Open an issue, and choose the form that fits:

- **Wrong formula, figure, or citation:** a formula, range, threshold, or citation that is wrong or unsupported.
- **Add a metric or device:** a metric, test, or device the skills should cover.
- **Vendor export or API changed:** a vendor export or metric definition that no longer matches a reference file.

For a broken link, a typo, or anything else, open a blank issue.

Never paste real athlete data into an issue or a pull request. Use made-up numbers, and remove names from any example.

## Propose a change

Follow these steps to propose a change:

1. Fork the repository, and create a branch for your change.
2. Make the change. To add a skill, a metric, or a device reference, start from the [templates](templates/README.md).
3. If you change a formula, update [`docs/calculations.md`](docs/calculations.md) in the same change.
4. If you change a device reference that two skills share, change both copies so they stay identical. The [device table](skills/README.md#device-export-references) lists where each copy lives.
5. Run the checks from the repository root with `python3 scripts/check_repo.py`, and fix every failure.
6. Write a commit message that says what changed and why. The git history is the record of changes.
7. Open a pull request. Link the issue it fixes, and list the sources you used.

The checks also run automatically on every pull request.

## Meet the content rules

Every change must meet these rules:

- **Cite a source for every figure.** Every formula, threshold, and range needs a peer-reviewed source or an official vendor document. Remove any figure without a source.
- **Check every citation yourself.** Open the source and confirm it exists and supports the figure. AI tools invent citations that look real. Say in the pull request if you read only the abstract.
- **Keep methods vendor-neutral.** Write each metric reference so it works with data from any vendor. Put vendor-specific details only in device references.
- **Describe vendors factually.** Paraphrase vendor definitions and link to the vendor source. Do not copy vendor documentation. Claim no endorsement or partnership.
- **Promote nothing.** Add no product claims, pricing, or calls to action for any company, including the maintainer.
- **Frame results as decision support.** Do not add diagnosis, injury prediction, or return-to-sport clearance. Leave training and clearance decisions to the practitioner.
- **Keep skills model-agnostic.** Follow the open [Agent Skills](https://agentskills.io) standard, and use no feature specific to one AI vendor. Make every skill work from its instructions alone. Scripts are optional helpers.
- **Keep the description short.** Write each skill's `description` in the words a coach would use, in under 200 characters.
- **Use made-up data only.** Worked examples and test data must be synthetic.

## Write in the house style

Write for a coach, not a researcher. Follow these style rules:

- Use short sentences, with one idea each.
- Use active voice, and the imperative mood for instructions.
- Use plain words. Define every technical term the first time you use it.
- Do not use em-dashes, idioms, or exclamation marks.
- Use serial commas.
- Write dates as `YYYY-MM-DD`.
- Use sentence case for headings. Start task headings with a verb, such as "Check the units".
- Introduce every list with a full sentence that ends in a colon.
- Use numbered lists only for steps in order.

## Know how changes are reviewed

The maintainers review issues and pull requests every two weeks.

## License your contribution

By contributing, you agree to license your contribution under the same terms as the repository. Skill instructions, reference files, and documentation use [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Scripts use the [MIT license](LICENSES/MIT.txt). See [LICENSE.md](LICENSE.md).
