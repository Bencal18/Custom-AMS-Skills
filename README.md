# Custom AMS Skills

Free, open skills that help AI tools analyze athlete monitoring data correctly.

You use ChatGPT, Claude, Gemini, Grok, or Copilot to write spreadsheet formulas, Power BI or Tableau calculations, or code for your athlete data. The AI usually produces something that looks right. These skills make it more likely to be right. Each skill tells the AI which formula to use, what a plausible result looks like, and how to check its own work before it answers.

The skills work with data from any vendor. Reference files for VALD, Hawkin Dynamics, Catapult, Kinexon, Polar, Firstbeat, GymAware, and Perch show the AI how to read those exports.

## Who it's for

These skills are for coaches, sports scientists, performance analysts, and athletic trainers working with healthy athletes. They help you if you:

- Work with athlete data from force plates, GPS or local positioning, velocity devices, wellness forms, or other wearables.
- Use an AI tool to clean, calculate, trend, or chart that data.
- Want to know whether the AI's method is correct.

You do not need to write code.

## What a skill is

A skill is a folder with a `SKILL.md` file of plain-text instructions, plus reference files the AI reads when it needs them. When you ask your AI tool for a task that matches a skill, the tool loads the skill and follows it.

These skills follow the open [Agent Skills](https://agentskills.io) standard, so the same folder works in every tool that supports the standard. You can also open any file and read it yourself. The reference files are written for coaches as well as for the AI.

### Inside a skill

Every skill folder has the same layout. The `force-plate` skill looks like this:

```text
force-plate/
├── SKILL.md                          Instructions the AI follows
└── references/
    ├── cmj-jump-height.md            One file for each metric
    ├── rsi-modified.md
    ├── imtp-peak-force.md
    ├── eccentric-hamstring-force.md
    ├── vald-forcedecks.md            One file for each device export
    ├── vald-nordbord.md
    └── hawkin-dynamics.md
```

The `athlete-data-visualization` skill also has an `assets/` folder with example charts.

The AI reads a skill in three steps:

1. The AI reads the `name` and `description` at the top of each `SKILL.md`. It uses these to decide which skill fits your request.
2. When a skill fits, the AI reads the rest of that `SKILL.md`. This part lists the steps to follow and the reference file for each metric.
3. The AI opens only the reference files the task needs. A question about jump height loads `cmj-jump-height.md` and, if you name your device, the file for that device.

This keeps the AI focused. It also means you can install all the skills at once without slowing down your tool.

## Find your way around

Use this table to go straight to what you need:

| To do this | Go here |
|---|---|
| Install the skills in your AI tool | [Install the skills](#install-the-skills) |
| See which skills exist and what each one covers | [`skills/`](skills/README.md) |
| Check how a metric is calculated | [`docs/calculations.md`](docs/calculations.md) |
| Look up what a vendor's metric means | [`docs/vendor-metrics/`](docs/vendor-metrics/README.md) |
| Plan your own athlete management system | [`docs/build-an-ams.md`](docs/build-an-ams.md) |
| Build AMS screens in Power BI or Tableau | [`skills/ams-dashboards/`](skills/ams-dashboards/SKILL.md) |
| Open a ready-made Power BI and Tableau template | [`dashboards/`](dashboards/README.md) |
| Write a new skill or reference file | [`templates/`](templates/README.md) |
| Report a problem or suggest a change | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Confirm the skills loaded in your AI tool | [Confirm the install works](#confirm-the-install-works) |

The repository is laid out like this:

```text
Custom-AMS-Skills/
├── skills/                      The 13 skills you install
│   ├── ams-architecture/
│   ├── ams-dashboards/
│   ├── ams-data-setup/
│   ├── athlete-data-visualization/
│   ├── check-ai-analysis/
│   ├── coach-reports/
│   ├── force-plate/
│   ├── gps-running-load/
│   ├── limb-symmetry/
│   ├── load-and-wellness/
│   ├── monitoring-statistics/
│   ├── readiness-composites/
│   └── velocity-based-training/
├── dashboards/                  Power BI and Tableau template for the core AMS screens
├── docs/                        Pages for people to read
│   ├── calculations.md
│   ├── build-an-ams.md
│   └── vendor-metrics/          One page or folder for each vendor
├── templates/                   Blank files for new skills and references
├── tests/
│   └── skill-load-test/         Test skill that confirms the install works
├── scripts/                     Maintainer scripts
├── LICENSES/
├── CONTRIBUTING.md
└── LICENSE.md
```

Each folder does this:

<dl>
<dt><a href="skills/README.md"><code>skills/</code></a></dt>
<dd>The skills you install. Each skill folder holds a <code>SKILL.md</code> file that the AI follows, and a <code>references/</code> folder with one file for each metric, device, or topic.</dd>
<dt><a href="dashboards/README.md"><code>dashboards/</code></a></dt>
<dd>A template that builds the core AMS screens in Power BI and Tableau from your own data, with made-up sample data, the script that calculates every metric, and checks for the generated files.</dd>
<dt><a href="docs/README.md"><code>docs/</code></a></dt>
<dd>Pages for people to read: how every metric is calculated, what each vendor metric means, and how to plan an athlete management system.</dd>
<dt><a href="templates/README.md"><code>templates/</code></a></dt>
<dd>Blank files to copy when you write a new skill, metric reference, or device reference.</dd>
<dt><a href="tests/README.md"><code>tests/</code></a></dt>
<dd>A test skill that confirms your AI tool loads skills.</dd>
<dt><a href="scripts/"><code>scripts/</code></a></dt>
<dd>Helper scripts for maintainers: one checks links and skill files, and one builds the skill zips for each release.</dd>
<dt><a href="LICENSES/"><code>LICENSES/</code></a></dt>
<dd>The full license texts.</dd>
</dl>

## Install the skills

Start by downloading the skills. The [latest release](https://github.com/Bencal18/Custom-AMS-Skills/releases/latest) has one ready-made zip file for each skill, such as `force-plate.zip`. Download the zip for each skill you want. Do not unzip it. Claude, ChatGPT, Gemini, and Grok take the zip as it is.

For Copilot in Excel and the coding tools, you need the folders. Unzip the file, or, on the repository page, select **Code**, then **Download ZIP**, and unzip it. Each folder inside `skills/` is one skill.

Menus in AI tools change often. If a step does not match what you see, follow the linked help page for your tool.

### Claude (claude.ai and the Claude desktop app)

1. Download the zip for the skill from the [latest release](https://github.com/Bencal18/Custom-AMS-Skills/releases/latest). If you make your own zip, it must hold the folder itself, for example `force-plate.zip` containing `force-plate/SKILL.md`.
2. In Claude, go to **Customize**, then **Skills**.
3. Select **+**, then **Create skill**, then **Upload a skill**, and upload the zip.
4. Turn on the skill.

Skills need code execution, which you turn on in **Settings**, then **Capabilities**. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### ChatGPT

Skill upload is available on ChatGPT Business, Enterprise, Healthcare, and Edu plans. An admin may need to turn it on first.

1. Download the zip for the skill from the latest release, as in the Claude steps.
2. In ChatGPT, go to **Skills**, then **Create**, then **Upload from your computer**, and upload the zip.

On Free, Plus, and Pro plans, use a project instead. See [Use a skill in a tool without skill support](#use-a-skill-in-a-tool-without-skill-support).

### Gemini (gemini.google.com)

Skills in the Gemini app need a personal Google account, not a work or school account.

1. Open the **Skills** page in Gemini.
2. Upload the zip for the skill from the latest release.

See [Gemini skills help](https://support.google.com/gemini/answer/17094296).

### Grok (grok.com and the Grok apps)

1. Download the zip for the skill from the latest release, as in the Claude steps.
2. Go to [grok.com/skills](https://grok.com/skills).
3. Select **Create skill**, then **Import**, and upload the zip.

Skills you add on grok.com also work in the Grok iOS and Android apps. See the [Grok skills announcement](https://x.ai/news/grok-skills).

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
| Grok Build | `~/.grok/skills/` | `.grok/skills/` |

Grok Build also reads skills from `~/.agents/skills/`, so one copy there serves both Codex and Grok Build. See [Grok Build skills](https://docs.x.ai/build/features/skills-plugins-marketplaces).

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

The [`tests/skill-load-test`](tests/skill-load-test/) folder holds a test skill. The latest release has it as `skill-load-test.zip`. Install it the same way as the other skills, then ask your AI tool: "Is the coach skills test working?"

If the skill loaded, the AI replies with a line that starts with `COACH-SKILLS-LOADED`. Remove the test skill when you are done.

## What the skills do not do

The skills support your decisions. They do not make them. The skills do not:

- Diagnose injuries or predict injury risk.
- Clear an athlete to return to sport or training.
- Replace the judgment of a qualified practitioner.

Check every result before you act on it. Each skill tells the AI to show the formula, the units, and any check that failed.

The skills and documents are general guidance. Do your own research. Read the cited sources, and confirm that each method fits your athletes, your devices, and your organization's rules before you rely on it. Nothing in this repository is legal or medical advice.

## Suggest a fix

Found a wrong formula, a broken link, or a metric we should add? Open an issue or a pull request. Read [CONTRIBUTING.md](CONTRIBUTING.md) first for the content rules and how changes are reviewed.

## License

The skill instructions and reference files use the CC BY 4.0 license. Scripts use the MIT license. See [LICENSE.md](LICENSE.md).

---

Maintained by [Eclipse Performance, Inc.](https://eclipseperf.com)
