# Skills

Each folder in this directory is one skill. Version 1 has these 11 skills:

| Skill | What it covers | Status |
|---|---|---|
| `ams-data-setup` | Athlete, session, and measure tables; IDs; joining sources by athlete and date; missing data | Reviewed |
| `monitoring-statistics` | Typical error, smallest worthwhile change, minimal detectable change, individual baselines, z-scores, why ACWR and group p-values mislead | Reviewed |
| `load-and-wellness` | Session RPE load, ACWR (with limitations), wellness score z-score | Reviewed |
| `gps-running-load` | Total distance, high-speed running, accelerations and decelerations | Reviewed |
| `force-plate` | CMJ jump height, RSI-modified, IMTP peak force, eccentric hamstring force | Reviewed |
| `velocity-based-training` | Mean concentric velocity, velocity loss across a set | Reviewed |
| `limb-symmetry` | Limb symmetry index, formula variants, and the reference-limb rule | Reviewed |
| `readiness-composites` | Readiness and rehab-monitoring composites, and why sub-scores must stay visible | Reviewed |
| `check-ai-analysis` | Questions to answer before trusting a result | Reviewed |
| `coach-reports` | What to show coaches versus athletes, and how to flag changes without noise | Reviewed |
| `athlete-data-visualization` | Chart choice, time series, complex relationships, uncertainty, color and accessibility, and squad views | Reviewed |

Device export references for VALD ForceDecks and NordBord, Hawkin Dynamics, Catapult, Kinexon, Polar Team Pro, Firstbeat Sports, GymAware, and Perch sit in the `references/` folder of each skill that uses that device's data.

To write a new skill, copy the templates in [`templates/`](../templates/).
