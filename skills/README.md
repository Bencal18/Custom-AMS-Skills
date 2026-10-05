# Skills

Each folder in this directory is one skill. Install a skill by copying or uploading its whole folder, as the [README](../README.md#install-the-skills) describes.

Each skill folder has this layout:

```text
<skill-name>/
  SKILL.md          Instructions the AI follows
  references/       One file for each metric, device, or topic, loaded when needed
  assets/           Example images, in some skills only
```

## Version 1 skills

Version 1 has these 11 skills:

| Skill | What it covers | Status |
|---|---|---|
| [`ams-data-setup`](ams-data-setup/SKILL.md) | Athlete, session, and measure tables; IDs; joining sources by athlete and date; missing data | Reviewed |
| [`monitoring-statistics`](monitoring-statistics/SKILL.md) | Typical error, smallest worthwhile change, minimal detectable change, individual baselines, z-scores, why ACWR and group p-values mislead | Reviewed |
| [`load-and-wellness`](load-and-wellness/SKILL.md) | Session RPE load, ACWR (with limitations), wellness score z-score | Reviewed |
| [`gps-running-load`](gps-running-load/SKILL.md) | Total distance, high-speed running, accelerations and decelerations | Reviewed |
| [`force-plate`](force-plate/SKILL.md) | CMJ jump height, RSI-modified, IMTP peak force, eccentric hamstring force | Reviewed |
| [`velocity-based-training`](velocity-based-training/SKILL.md) | Mean concentric velocity, velocity loss across a set | Reviewed |
| [`limb-symmetry`](limb-symmetry/SKILL.md) | Limb symmetry index, formula variants, and the reference-limb rule | Reviewed |
| [`readiness-composites`](readiness-composites/SKILL.md) | Readiness and rehab-monitoring composites, and why sub-scores must stay visible | Reviewed |
| [`check-ai-analysis`](check-ai-analysis/SKILL.md) | Questions to answer before trusting a result | Reviewed |
| [`coach-reports`](coach-reports/SKILL.md) | What to show coaches versus athletes, and how to flag changes without noise | Reviewed |
| [`athlete-data-visualization`](athlete-data-visualization/SKILL.md) | Chart choice, time series, complex relationships, uncertainty, color and accessibility, and squad views | Reviewed |

## Draft skills

This skill is a draft. It has not been tested or reviewed:

| Skill | What it covers | Status |
|---|---|---|
| [`ams-architecture`](ams-architecture/SKILL.md) | The parts of an AMS, spreadsheet, low-code, or database setups, hosting, data layers, data intake, access and privacy, backups and handover, and buy versus build | Draft |

## Device export references

A device export reference tells the AI how to read one vendor's export or API. Each one sits in the `references/` folder of every skill that uses that device's data, so each skill works on its own. Copies of the same device reference in two skills are identical.

| Device | Skills with a reference file |
|---|---|
| VALD ForceDecks | [`force-plate`](force-plate/references/vald-forcedecks.md), [`limb-symmetry`](limb-symmetry/references/vald-forcedecks.md) |
| VALD NordBord | [`force-plate`](force-plate/references/vald-nordbord.md), [`limb-symmetry`](limb-symmetry/references/vald-nordbord.md) |
| Hawkin Dynamics | [`force-plate`](force-plate/references/hawkin-dynamics.md), [`limb-symmetry`](limb-symmetry/references/hawkin-dynamics.md) |
| Catapult | [`gps-running-load`](gps-running-load/references/catapult.md), [`load-and-wellness`](load-and-wellness/references/catapult.md) |
| Kinexon | [`gps-running-load`](gps-running-load/references/kinexon.md), [`load-and-wellness`](load-and-wellness/references/kinexon.md) |
| Polar Team Pro | [`gps-running-load`](gps-running-load/references/polar-team-pro.md), [`load-and-wellness`](load-and-wellness/references/polar-team-pro.md) |
| Firstbeat Sports | [`load-and-wellness`](load-and-wellness/references/firstbeat-sports.md) |
| GymAware | [`velocity-based-training`](velocity-based-training/references/gymaware.md) |
| Perch | [`velocity-based-training`](velocity-based-training/references/perch.md) |

For the full breakdown of every metric a vendor exports, see the [vendor metrics index](../docs/vendor-metrics/README.md).

## Write a new skill

To write a new skill, copy the templates in [`templates/`](../templates/README.md).
