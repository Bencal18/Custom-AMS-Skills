# Vendor metrics

These pages explain what each metric in a vendor's export means, how the vendor calculates it, and what the vendor does not publish. Use them to check a number in your export, or to compare two vendors' metrics with similar names.

The pages paraphrase vendor definitions and link to the vendor sources. All product names are trademarks of their owners. This repository is not affiliated with or endorsed by any vendor.

## Pages by vendor

Each vendor has one page, or one folder with an overview page and one page for each group of tests:

| Vendor | Products | Data | Page |
|---|---|---|---|
| VALD | ForceDecks and NordBord | Force plate tests and eccentric hamstring force | [VALD ForceDecks and NordBord](vald-forcedecks-nordbord/README.md) |
| VALD | ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware | Isometric force, handheld force and range of motion, sprint timing, markerless motion, and bar velocity | [VALD other products](vald-other-products/README.md) |
| Hawkin Dynamics | Force plates and TruStrength | Force plate tests and isometric strength | [Hawkin Dynamics](hawkin-dynamics/README.md) |
| Catapult | Vector, Catapult One, and Perch | GPS and local positioning, accelerometer load, heart rate, and bar velocity | [Catapult](catapult.md) |
| Kinexon | Kinexon | Local positioning, GNSS, accelerations, jumps, and heart rate | [Kinexon](kinexon.md) |
| Polar | Polar Team Pro | Heart rate, speed, distance, acceleration, and load | [Polar Team Pro](polar-team-pro.md) |
| Firstbeat | Firstbeat Sports | Heart rate, heart rate variability, internal load, and recovery | [Firstbeat Sports](firstbeat-sports.md) |

## Pages for each group of tests

The three vendor folders split their metrics across these pages. Start with the overview page in each folder. It holds the summary tables and the sources:

- VALD ForceDecks and NordBord
  - [Overview](vald-forcedecks-nordbord/README.md), with the glossary of events and terms
  - [Countermovement jump](vald-forcedecks-nordbord/cmj.md)
  - [Squat jump and drop jump](vald-forcedecks-nordbord/squat-jump-drop-jump.md)
  - [Rebound, hop, and landing tests](vald-forcedecks-nordbord/rebound-hop-landing.md)
  - [Squat, push-up, sit to stand, balance, isometric, and general tests](vald-forcedecks-nordbord/squat-isometric-general.md)
  - [NordBord](vald-forcedecks-nordbord/nordbord.md)
- VALD other products
  - [Overview](vald-other-products/README.md)
  - [ForceFrame](vald-other-products/forceframe.md)
  - [DynaMo](vald-other-products/dynamo.md)
  - [SmartSpeed](vald-other-products/smartspeed.md)
  - [HumanTrak](vald-other-products/humantrak.md)
  - [GymAware](vald-other-products/gymaware.md)
- Hawkin Dynamics
  - [Overview](hawkin-dynamics/README.md)
  - [Countermovement jump](hawkin-dynamics/cmj.md)
  - [Squat jump](hawkin-dynamics/squat-jump.md)
  - [Drop jump](hawkin-dynamics/drop-jump.md)
  - [Isometric test](hawkin-dynamics/isometric.md)
  - [Countermovement rebound jump](hawkin-dynamics/cmj-rebound.md)
  - [Multi rebound](hawkin-dynamics/multi-rebound.md)
  - [Drop landing](hawkin-dynamics/drop-landing.md)
  - [Free run](hawkin-dynamics/free-run.md)
  - [Weigh-in](hawkin-dynamics/weigh-in.md)
  - [TruStrength](hawkin-dynamics/trustrength.md)

Some Hawkin Dynamics metrics share a name with VALD metrics but are calculated differently. Read [Hawkin and VALD name collisions](hawkin-dynamics/README.md#hawkin-and-vald-name-collisions) before you compare the two vendors.

## Related pages

These pages and sections connect to the vendor metrics:

- [How every metric is calculated](../calculations.md) lists the vendor equivalent of each metric in the skills.
- The [device export references](../../skills/README.md#device-export-references) in the skills tell the AI how to read each vendor's export.
