# Custom AMS Skills

Free, open skills that help AI tools analyze athlete monitoring data correctly.

You use ChatGPT, Claude, Gemini, or Copilot to write spreadsheet formulas, Power BI or Tableau calculations, or code for your athlete data. The AI usually produces something that looks right. These skills make it more likely to be right. Each skill tells the AI which formula to use, what a plausible result looks like, and how to check its own work before it answers.

The skills work with data from any vendor. Reference files for VALD, Hawkin Dynamics, Catapult, Kinexon, Polar, Firstbeat, GymAware, and Perch show the AI how to read those exports.

## Who it's for

These skills are for coaches, sports scientists, performance analysts, athletic trainers, and physical therapists who:

- Work with athlete data from force plates, GPS or local positioning, velocity devices, wellness forms, or other wearables.
- Use an AI tool to clean, calculate, trend, or chart that data.
- Want to know whether the AI's method is correct.

You do not need to write code.

## What a skill is

A skill is a folder with a `SKILL.md` file of plain-text instructions, plus reference files the AI reads when it needs them. When you ask your AI tool for a task that matches a skill, the tool loads the skill and follows it.

These skills follow the open [Agent Skills](https://agentskills.io) standard, so the same folder works in every tool that supports the standard. You can also open any file and read it yourself. The reference files are written for coaches as well as for the AI.

## Skills in this repository

See [`skills/README.md`](skills/README.md) for the full list and the status of each skill.

See [`docs/calculations.md`](docs/calculations.md) for how every metric is calculated, in one place.

## Install the skills

Start by downloading the skills. On the repository page, select **Code**, then **Download ZIP**, and unzip the file. Each folder inside `skills/` is one skill.

Menus in AI tools change often. If a step does not match what you see, follow the linked help page for your tool.

### Claude (claude.ai and the Claude desktop app)

1. Zip one skill folder so the zip holds the folder itself, for example `force-plate.zip` containing `force-plate/SKILL.md`. On a Mac, right-click the folder and select **Compress**.
2. In Claude, go to **Customize**, then **Skills**.
3. Select **+**, then **Create skill**, then **Upload a skill**, and upload the zip.
4. Turn on the skill.

Skills need code execution, which you turn on in **Settings**, then **Capabilities**. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### ChatGPT

Skill upload is available on ChatGPT Business, Enterprise, Healthcare, and Edu plans. An admin may need to turn it on first.

1. Zip one skill folder, as in the Claude steps.
2. In ChatGPT, go to **Skills**, then **Create**, then **Upload from your computer**, and upload the zip.

On Free, Plus, and Pro plans, use a project instead. See [Use a skill in a tool without skill support](#use-a-skill-in-a-tool-without-skill-support).

### Gemini (gemini.google.com)

Skills in the Gemini app need a personal Google account, not a work or school account.

1. Open the **Skills** page in Gemini.
2. Upload a zip of one skill folder.

See [Gemini skills help](https://support.google.com/gemini/answer/17094296).

### Copilot in Excel

Copilot in Excel needs the Office display language set to English.

1. In Copilot in Excel, go to **Settings**, then **Manage plugins & skills**, then **Custom skills**.
2. Select **Create OneDrive folder**.
3. Copy each skill folder into that OneDrive folder.

See [Copilot in Excel skills](https://support.microsoft.com/en-au/excel/copilot/copilot-in-excel-skills).

### Coding tools

Copy each skill folder into the skills directory for your tool:

| Tool | Skills directory for all your projects | Skills directory for one project |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |
| GitHub Copilot (VS Code, JetBrains, Copilot CLI) | `~/.copilot/skills/` | `.github/skills/` |

Gemini CLI can also install a skill straight from this repository:

```bash
gemini skills install <repository-url> --path skills/force-plate
```

## Use a skill in a tool without skill support

If your tool or plan does not support skills, give the AI the skill as instructions:

- **Claude Projects:** Paste the text of `SKILL.md` into the project instructions. Add the files in `references/` to the project knowledge.
- **ChatGPT Projects:** Paste the text of `SKILL.md` into the project instructions. Add the files in `references/` to the project files.
- **Gemini Gems:** Paste the text of `SKILL.md` into the Gem instructions. Add the files in `references/` as knowledge. Google is replacing Gems with skills.
- **Any chat:** Paste the text of `SKILL.md` at the start of the chat, and attach the reference files you need.

## Confirm the install works

The [`tests/skill-load-test`](tests/skill-load-test/) folder holds a test skill. Install it the same way as the other skills, then ask your AI tool: "Is the coach skills test working?"

If the skill loaded, the AI replies with a line that starts with `COACH-SKILLS-LOADED`. Remove the test skill when you are done.

## What the skills do not do

The skills support your decisions. They do not make them. The skills do not:

- Diagnose injuries or predict injury risk.
- Clear an athlete to return to sport or training.
- Replace the judgment of a qualified practitioner.

Check every result before you act on it. Each skill tells the AI to show the formula, the units, and any check that failed.

## Suggest a fix

Found a wrong formula, a broken link, or a metric we should add? Open an issue or a pull request.

## License

The skill instructions and reference files use the CC BY 4.0 license. Scripts use the MIT license. See [LICENSE.md](LICENSE.md).

---

Maintained by [Eclipse Performance, Inc.](https://eclipseperf.com)
