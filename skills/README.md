# Skills

Each folder in this directory is one skill. Version 1 has these 11 skills:

| Skill | What it covers | Status |
|---|---|---|
| `ams-data-setup` | Athlete, session, and measure tables; IDs; joining sources by athlete and date; missing data | Reviewed; tested in Claude: 25 of 27 criteria passed |
| `monitoring-statistics` | Typical error, smallest worthwhile change, minimal detectable change, individual baselines, z-scores, why ACWR and group p-values mislead | Reviewed; tested in Claude: 37 of 45 criteria passed |
| `load-and-wellness` | Session RPE load, ACWR (with limitations), wellness score z-score | Reviewed; tested in Claude: 37 of 43 criteria passed |
| `gps-running-load` | Total distance, high-speed running, accelerations and decelerations | Reviewed; tested in Claude: 20 of 24 criteria passed |
| `force-plate` | CMJ jump height, RSI-modified, IMTP peak force, eccentric hamstring force | Reviewed; tested in Claude: 26 of 26 criteria passed |
| `velocity-based-training` | Mean concentric velocity, velocity loss across a set | Reviewed; tested in Claude: 22 of 25 criteria passed |
| `limb-symmetry` | Limb symmetry index, formula variants, and the reference-limb rule | Reviewed; tested in Claude: 20 of 24 criteria passed |
| `readiness-composites` | Readiness and rehab-monitoring composites, and why sub-scores must stay visible | Reviewed; tested in Claude: 29 of 30 criteria passed |
| `check-ai-analysis` | Questions to answer before trusting a result | Reviewed; tested in Claude: 27 of 30 criteria passed |
| `coach-reports` | What to show coaches versus athletes, and how to flag changes without noise | Reviewed; tested in Claude: 27 of 31 criteria passed |
| `athlete-data-visualization` | Chart choice, time series, complex relationships, uncertainty, color and accessibility, and squad views | Reviewed; tested in Claude: 29 of 29 criteria passed |

Claude test results come from 24 test cases run on 2026-10-02. In each case, a Claude agent read the skill files and answered a coach's request, and a separate Claude agent graded the answer against written criteria. Across all cases, 299 of 334 criteria passed, 32 passed in part, and 3 failed. Claude picked the right skill for 26 of 26 requests. The skills were not installed in the Claude app for these tests, and they were not tested in other AI tools. The Power BI and Tableau versions were not tested in Power BI or Tableau.

Device export references for VALD ForceDecks and NordBord, Hawkin Dynamics, Catapult, Kinexon, Polar Team Pro, Firstbeat Sports, GymAware, and Perch sit in the `references/` folder of each skill that uses that device's data.

To write a new skill, copy the templates in [`templates/`](../templates/).
