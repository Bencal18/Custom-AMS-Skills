# Templates

Copy these files when you add to the repository. Each template marks the parts to fill in with angle brackets, such as `<metric name>`.

| Template | Use it for | Copy it to |
|---|---|---|
| [`SKILL.md`](SKILL.md) | A new skill | `skills/<skill-name>/SKILL.md` |
| [`metric-reference.md`](metric-reference.md) | One metric, such as jump height or session RPE load | `skills/<skill-name>/references/<metric>.md` |
| [`device-export-reference.md`](device-export-reference.md) | One vendor's export or API | `skills/<skill-name>/references/<device>.md` |

## Add a skill

Follow these steps to add a skill:

1. Create a folder in `skills/`. Name it in lowercase with hyphens, such as `sprint-testing`.
2. Copy `SKILL.md` into the folder, and set `name` to the folder name. Set `last-tested` to `not tested` until you test the skill.
3. Write the `description` in the words a coach would use to ask for the task. Keep it under 200 characters.
4. Create a `references/` folder, and add one file for each metric from `metric-reference.md`.
5. Optional: Add a device reference for each vendor from `device-export-reference.md`. If another skill already has one for that vendor, copy it unchanged. Add each new device reference to the device table in [`skills/README.md`](../skills/README.md#device-export-references).
6. Add the skill to the table in [`skills/README.md`](../skills/README.md).
7. Add each formula to [`docs/calculations.md`](../docs/calculations.md) in the same change.
