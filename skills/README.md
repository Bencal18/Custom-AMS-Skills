# Skills

Each folder in this directory is one skill. Install a skill by copying or uploading its whole folder, as the [README](../README.md#install-the-skills) describes.

Each skill folder has this layout:

```text
<skill-name>/
  SKILL.md          Instructions the AI follows
  references/       One file for each metric, device, or topic, loaded when needed
  assets/           Example images, in some skills only
```

## Version 1, 1.1, and 1.2 skills

Versions 1, 1.1, and 1.2 have these 20 skills:

| Skill | What it covers | Status |
|---|---|---|
| [`ams-data-setup`](ams-data-setup/SKILL.md) | Athlete, session, and measure tables; IDs; joining sources by athlete and date; missing data; auditing a monitoring workbook and rolling it over to a new season | Draft |
| [`monitoring-statistics`](monitoring-statistics/SKILL.md) | Typical error, smallest worthwhile change, minimal detectable change, individual baselines, z-scores, why ACWR and group p-values mislead | Reviewed |
| [`load-and-wellness`](load-and-wellness/SKILL.md) | Session RPE load, ACWR (with limitations), training monotony and strain, wellness score z-score, estimated load for athletes who did not wear a device, taper volume reduction, intensity distribution, and recovery questionnaire scores (Hooper index, TQR, PRS, BAM) | Draft |
| [`gps-running-load`](gps-running-load/SKILL.md) | Total distance, high-speed running, top-speed exposure, accelerations and decelerations, peak demands, match-day load, and ice hockey tracking and time-on-ice data | Draft |
| [`force-plate`](force-plate/SKILL.md) | CMJ jump height, RSI-modified, CMJ strategy metrics (time to takeoff, flight time to contraction time ratio, braking and propulsive impulse, countermovement depth), IMTP peak force, eccentric hamstring force, dynamic strength index, and eccentric utilization ratio | Draft |
| [`velocity-based-training`](velocity-based-training/SKILL.md) | Mean concentric velocity, velocity loss across a set, and reading EliteForm velocity and power data | Draft |
| [`limb-symmetry`](limb-symmetry/SKILL.md) | Limb symmetry index, formula variants, and the reference-limb rule | Reviewed |
| [`readiness-composites`](readiness-composites/SKILL.md) | Readiness composites, and why sub-scores must stay visible | Reviewed |
| [`check-ai-analysis`](check-ai-analysis/SKILL.md) | Questions to answer before trusting a result | Reviewed |
| [`coach-reports`](coach-reports/SKILL.md) | What to show coaches versus athletes, and how to flag changes without noise | Reviewed |
| [`athlete-data-visualization`](athlete-data-visualization/SKILL.md) | Chart choice, time series, complex relationships, uncertainty, color and accessibility, and squad views | Reviewed |
| [`ams-dashboards`](ams-dashboards/SKILL.md) | The core AMS screens in Power BI and Tableau, athlete check-in forms, athlete-only views, and moving off a commercial AMS | Draft |
| [`ams-architecture`](ams-architecture/SKILL.md) | The parts of an AMS, spreadsheet, low-code, or database setups, hosting, data layers, data intake, access and privacy, backups and handover, and buy versus build | Reviewed |
| [`testing-profiles`](testing-profiles/SKILL.md) | Where an athlete's test result sits against the squad, a position group, or a matched published norm, with measurement error | Draft |
| [`sprint-testing`](sprint-testing/SKILL.md) | Sprint profiles from splits, radar, or GPS, change of direction deficit, and repeated sprint scores | Draft |
| [`conditioning-speeds`](conditioning-speeds/SKILL.md) | Maximal aerobic speed from field tests, anaerobic speed reserve, and interval run distances | Draft |
| [`squad-questions`](squad-questions/SKILL.md) | Quick coach questions about the squad, with the question restated and the answer checked | Draft |
| [`heart-rate-and-sleep`](heart-rate-and-sleep/SKILL.md) | Morning HRV (ln rMSSD) trends, submaximal heart rate tests and heart rate recovery, and sleep trends against each athlete's baseline, with WHOOP and Oura exports | Draft |
| [`strength-training-load`](strength-training-load/SKILL.md) | Volume load, estimated 1RM from reps or RPE, personal bests, and relative strength from weight room training logs, with EliteForm exports | Draft |
| [`sport-specific-counts`](sport-specific-counts/SKILL.md) | Totals and rolling windows of pitches and throws, jumps, swim distance, and bowling volume | Draft |

## Device export references

A device export reference tells the AI how to read one vendor's export or API. Each one sits in the `references/` folder of every skill that uses that device's data, so each skill works on its own. Copies of the same device reference in two skills are identical.

| Device | Skills with a reference file |
|---|---|
| VALD ForceDecks | [`force-plate`](force-plate/references/vald-forcedecks.md), [`limb-symmetry`](limb-symmetry/references/vald-forcedecks.md) |
| VALD NordBord | [`force-plate`](force-plate/references/vald-nordbord.md), [`limb-symmetry`](limb-symmetry/references/vald-nordbord.md) |
| Hawkin Dynamics | [`force-plate`](force-plate/references/hawkin-dynamics.md), [`limb-symmetry`](limb-symmetry/references/hawkin-dynamics.md) |
| Catapult | [`gps-running-load`](gps-running-load/references/catapult.md), [`load-and-wellness`](load-and-wellness/references/catapult.md) |
| Kinexon | [`gps-running-load`](gps-running-load/references/kinexon.md), [`load-and-wellness`](load-and-wellness/references/kinexon.md) |
| STATSports | [`gps-running-load`](gps-running-load/references/statsports.md), [`load-and-wellness`](load-and-wellness/references/statsports.md) |
| Polar Team Pro | [`gps-running-load`](gps-running-load/references/polar-team-pro.md), [`load-and-wellness`](load-and-wellness/references/polar-team-pro.md) |
| Firstbeat Sports | [`load-and-wellness`](load-and-wellness/references/firstbeat-sports.md) |
| WHOOP | [`heart-rate-and-sleep`](heart-rate-and-sleep/references/whoop.md) |
| Oura | [`heart-rate-and-sleep`](heart-rate-and-sleep/references/oura.md) |
| GymAware | [`velocity-based-training`](velocity-based-training/references/gymaware.md) |
| Perch | [`velocity-based-training`](velocity-based-training/references/perch.md) |
| EliteForm | [`velocity-based-training`](velocity-based-training/references/eliteform.md), [`strength-training-load`](strength-training-load/references/eliteform.md) |

For the full breakdown of every metric a vendor exports, see the [vendor metrics index](../docs/vendor-metrics/README.md).

## Write a new skill

To write a new skill, copy the templates in [`templates/`](../templates/README.md).
