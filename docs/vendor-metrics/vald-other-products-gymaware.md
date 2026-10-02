# VALD GymAware metrics

GymAware measures bar position over time and derives velocity, power, force, and distance for lifts and jumps. GymAware has been owned by VALD since VALD announced the acquisition on 2026-08-10 ([source](https://www.valdperformance.com/news/vald-acquires-gymaware-bringing-the-gold-standard-in-velocity-based-training-into-the-worlds-leading-performance-technology-ecosystem)). GymAware is made by Kinetic Performance Technology ([source](https://gymaware.com/gymaware-joins-vald-performance/)). Checked against: the GymAware Cloud API integration guide, the GymAware Help Center articles, the Kinetic Performance Technology PDFs on angle correction and sampling, GymAware web pages, VALD product and news pages, and the VALD VBT 101 cheat sheet, 2026-10-02.

ForceFrame, DynaMo, SmartSpeed, HumanTrak, NordBord, ForceDecks, VALD Hub, and VALD are trademarks of VALD. GymAware is a trademark of its owner. This repository is not affiliated with or endorsed by VALD or GymAware.

This page is part of [VALD ForceFrame, DynaMo, SmartSpeed, HumanTrak, and GymAware metrics](vald-other-products.md). ForceDecks and NordBord are on a separate page: [VALD ForceDecks and NordBord metrics](vald-forcedecks-nordbord.md).

## How to read this page

Each metric block names the exact field or GymAware Cloud display name and then lists the following items:

- What it measures.
- Window or phase.
- Calculation: GymAware's definition in paraphrase, then the formula in plain math where a source gives one.
- Inputs and units.
- Variants.
- Comparison with standard methods or other vendors, only where a source supports it.
- What changes the number.
- Source links.

A formula labeled Restated is this page's plain restatement, not the vendor's statement. A calculation or detail marked Not published is one that the vendor does not publish in the public sources checked. It does not mean the vendor lacks the information. Definitions come from the GymAware Cloud API integration guide, the GymAware Help Center, and GymAware's education pages. VALD pages are cited where they add a definition. The `valdr` package has no GymAware functions ([source](https://github.com/cran/valdr)).

## GymAware

### Overview

The overview covers these topics:

- **What the device measures:**
  - GymAware RS is a linear position transducer (LPT). A tether attaches to the bar or athlete. It measures displacement over time and the tether angle ([source](https://gymaware.zendesk.com/hc/en-us/articles/360001422555-How-Does-it-Work)).
  - Each data point holds time, tether extension, and tether angle. GymAware converts the angle and length to vertical height with y = r sin θ ([source](https://kinetic.com.au/pdf/angle.pdf)).
  - FLEX is a laser device that clips onto the end of a barbell. It measures vertical and horizontal bar position relative to the ground over a reflective mat ([source](https://gymaware.com/gymaware-rs-vs-flex/)). FLEX does not use an accelerometer ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947942755983-FLEX-is-not-an-accelerometer)).
  - Velocity, power, and force are derived from position and time. VALD lists two GymAware models. GymAware RS uses linear position transducer technology with built-in angle correction. FLEX uses laser-based velocity-based training (VBT) technology ([source](https://valdperformance.com/products/gymaware)).
- **Export routes:**
  - GymAware Cloud CSV export: go to **View > Sessions**, filter, select sets, and click **Export**. The metric columns follow the account's default metrics under **Settings > Data** ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001477352-Exporting-data-from-the-GymAware-Cloud), [source](https://gymaware.zendesk.com/hc/en-us/articles/115000942672-Changing-the-Metrics-on-the-Cloud)). CSV column names and the row level of the CSV: Not published.
  - iPad app CSV export ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001477012-Exporting-data-from-the-iPad)) and FLEX Stronger app CSV export ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947870265103-Export)). Column layout: Not published.
  - GymAware Cloud API. It is included with the Premium Cloud license ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). The subscription page also lists "External API" as an add-on ([source](https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options)). Endpoints, all under `https://cloud.gymaware.com/api/` ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)):
    - `/summaries` (GET): one JSON object per set, with best-rep metrics.
    - `/reps` (GET): one JSON object per set, with a `reps` array. Each rep holds one value per analysis type.
    - `/bests` (GET): personal bests grouped by athlete, exercise, and weight.
    - `/analysis` (GET): the list of analysis types (rep metric labels) and flags that say how to aggregate each one.
    - `/exercises` (GET): the exercise list.
    - Activities (GET): activity categories. The guide gives no URL. The official example app calls `activities` ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
    - `/athletes` (GET, POST, DELETE), `/staff` (GET), `/squad` (GET, POST, PUT, DELETE), `/refresh` (POST), and `/logout` (GET, POST).
    - The example app also calls an undocumented `account` endpoint ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
  - valdr functions: none. The `valdr` package has no GymAware functions ([source](https://github.com/cran/valdr)).
- **Row level:**
  - `/summaries`: one row per set, identified by a unique set identifier ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
  - `/reps`: one object per set. It nests one entry per rep in `reps`, ordered by `REPNUM` ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
  - `/bests`: one row per athlete, exercise, and bar weight ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
- **Left and right labels:** No API endpoint has a side field ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Side appears only in exercise names in the default library, for example `Landmine Press - Left`, `Landmine Press - Right`, `Split Squat - Left`, and `Split Squat - Right` ([source](https://gymaware.zendesk.com/hc/en-us/articles/15412922699919-Exercises-on-GymAware-Cloud)). To split by side, parse `exerciseName` or `activityName`. A GymAware asymmetry formula: Not published.
- **Test types:** GymAware has no fixed test types. Every set belongs to an exercise and one activity. The activity categories are these ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)):
  - Jump
  - Olympic
  - Upper Body Horizontal Push
  - Upper Body Horizontal Pull
  - Upper Body Vertical Push
  - Upper Body Vertical Pull
  - Lower Body Push
  - Lower Body Pull

  The default Cloud library has 80+ exercises ([source](https://gymaware.zendesk.com/hc/en-us/articles/15412922699919-Exercises-on-GymAware-Cloud)). Cloud reports include force/velocity profile and 1RM prediction ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000962571-Force-Velocity-profile), [source](https://gymaware.zendesk.com/hc/en-us/articles/333757036735-1RM-Predictive-strength-testing)).
- **FLEX and the API:** RS and FLEX can connect to the same Cloud ([source](https://gymaware.com/gymaware-rs-vs-flex/)). FLEX Bridge is a Premium feature or an add-on ([source](https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options)). Whether API rows say which device recorded a set: Not published.

### API basics for coaches

The API basics are:

- **Authentication:** HTTP Basic. The user name is the Account ID. The password is an API token ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Owners and Admins create tokens in **Settings > Tokens**. GymAware advises one token per application. `POST /refresh` invalidates the current token and returns `accountID` and a new `token` ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Never put tokens in shared code.
- **Base URL:** `https://cloud.gymaware.com/api/` ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). The example app lets you override the domain with an environment variable ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
- **Response format:** All GET endpoints return a stream of JSON objects separated by newlines. Restated: read the body line by line, and parse each line as one JSON object ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/), [source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
- **Pagination:** No page or cursor parameters are published. Use time windows to limit results ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)):
  - `/summaries` and `/reps` take `start` and `end`, in UTC seconds since the epoch, on the `recorded` time. Send both or neither. The guide says "max 1 month per request" and also says "start/end need to be within 60 days of each other". Use windows of 1 month or less to satisfy both.
  - `/summaries` and `/reps` also take `modifiedSince`, which must fall within the last 7 days. It returns only sessions recorded in the last 180 days.
  - `/bests` takes `start` and `end` with "max 3 months per request".
  - The example app also sends an `athleteReference` filter to `/summaries` and `/reps`. The guide does not document it ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).
- **Deleted data:** `/summaries` and `/reps` carry `deleted` (boolean). Filter out `deleted == true` ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Deleted Cloud sets are removed permanently after 30 days ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)).
- **How the API identifies things** ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)):
  - Athlete: `athleteReference` and `athleteName`.
  - Exercise: `exerciseName` (both endpoints) and `exerciseReference` (`/reps` only). `/exercises` returns `reference`, `category`, `name`, and `subname`.
  - Activity: `activityName` and `activityReference`. These fields were added with GymAware Cloud 2.0 ([source](https://gymaware.zendesk.com/hc/en-us/articles/13390560907791-Existing-Classic-Cloud-Users-What-s-Changing-in-the-New-GymAware-Cloud)).
  - Load: `barWeight`, the mass lifted in kg. Body mass: `athleteWeight` in kg.
- **Units:** The API guide gives kg for `barWeight` and `athleteWeight`, m/s for velocity, W for power, and W/kg for relative power. Times are UTC seconds since the epoch. Units for `height`, `dip`, and the rep analysis values are not stated in the API guide. The Cloud can display distance in inches and mass in lb ([source](https://gymaware.zendesk.com/hc/en-us/articles/14664428761999-Updates-to-Bar-Weight-Body-Mass-and-Distance-Settings)). Whether API values follow those display settings: Not published.
- **Differences between the guide and the example app** ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)):
  - The example reads `reference`, `referenceID`, and `deleted` from `/athletes`. The guide lists `athleteReference`.
  - The example reads `notes` from `/summaries`. The guide does not list it.
  - The example reads `userID` from `/staff`. The guide lists only `staffReference`.

#### Identifiers and context fields: `/summaries`

The `/summaries` endpoint returns these identifier and context fields:

| Field | Type | Meaning (from the guide) |
|---|---|---|
| `reference` | string | Unique set identifier |
| `recorded` | float | Set time, UTC seconds since the epoch |
| `modified` | float | Last change, UTC seconds since the epoch |
| `athleteReference` | string | Athlete identifier |
| `athleteName` | string | Athlete display name |
| `exerciseName` | string | General exercise name |
| `activityName` | string | Account's exercise or activity name |
| `activityReference` | string | Activity identifier |
| `deleted` | boolean | Record deleted flag |
| `notes` | not stated | Used in the example app only ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)) |

Source: [GymAware Cloud API integration guide](https://gymaware.com/gymaware-cloud-api-integration-guide/).

#### Identifiers and context fields: `/reps`

The `/reps` endpoint returns these identifier and context fields:

| Field | Type | Meaning (from the guide) |
|---|---|---|
| `reference` | string | Unique set identifier |
| `recorded`, `modified` | float | UTC seconds since the epoch |
| `athleteReference`, `athleteName` | string | Athlete identifier and name |
| `exerciseName`, `exerciseReference` | string | Exercise name and identifier |
| `activityName`, `activityReference` | string | Activity name and identifier |
| `deleted` | boolean | Record deleted flag |
| `reps` | list | One entry per rep, matching `repCount` |
| `reps[].REPNUM` | integer | Order of the reps within the set |

Source: [GymAware Cloud API integration guide](https://gymaware.com/gymaware-cloud-api-integration-guide/).

#### Identifiers and context fields: `/bests`, `/analysis`, `/exercises`, and activities

These endpoints return the following fields:

| Endpoint | Fields |
|---|---|
| `/bests` | `athleteReference`, `athleteName`, `exerciseName`, `barWeight` (kg) |
| `/analysis` | `label` (string), `isPeak`, `isMin`, `isMean`, `isConcentric`, `isEccentric` (bool) |
| `/exercises` | `reference`, `modified`, `category`, `name`, `subname` |
| activities | `reference`, `name`, `description`, `category`, `modified`, `vbt` (bool: VBT exercise or custom activity) |

Source: [GymAware Cloud API integration guide](https://gymaware.com/gymaware-cloud-api-integration-guide/).

### Set-level metrics (`/summaries`)

The set-level metrics come from one rep: the best rep, or for `peakVelocity` the peak rep. How GymAware picks the best rep for `/summaries`: Not published ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Whether all best-rep fields come from the same rep: Not published.

#### `repCount` (count)

The block has these fields:

- **What it measures:** How many reps were detected and kept in the set.
- **Calculation:** GymAware describes `repCount` as the number of reps marked up in the set ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Restated: the count of reps found by rep detection, after any edits.
- **Inputs and units:** Integer.
- **Variants:** The same field appears in `/reps`. There, `reps` has one entry per counted rep.
- **What changes the number:** On RS, a rep under 75% of the size of an earlier movement may not count. Moving the bar into the rack can register as a rep ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000524955-Funky-reps-Rep-mark-up-explained)). On FLEX, each rep must be "within 75% of the last rep". FLEX also uses a per-exercise minimum movement threshold, for example 18 cm on bench press ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947901584655-Rep-Detection)). The auto-record timeout defaults to 7 s on RS ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000524955-Funky-reps-Rep-mark-up-explained)) and can be set up to 60 s ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000796691-Recording-Modes)). Coaches can delete, split, or merge reps and sets in the Cloud ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/360000524955-Funky-reps-Rep-mark-up-explained , https://gymaware.zendesk.com/hc/en-us/articles/6947901584655-Rep-Detection

#### `meanVelocity` (m/s)

The block has these fields:

- **What it measures:** Average bar velocity over the concentric phase of the set's best rep.
- **Calculation:** GymAware describes `meanVelocity` as the mean velocity of the best rep, in m/s ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). GymAware defines concentric mean velocity as the sum of point velocities divided by the number of concentric data points, with v = (d2 - d1) / (t2 - t1) ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: mean velocity = (sum of v_i) / n, for the n data points in the concentric phase. v_i is the change in vertical position divided by the change in time between points.
- **Inputs and units:** Position in m and time in s. RS samples by Variable Rate Sampling, down-sampled to at most 50 points per second ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001133391-GymAware-Fact-sheets), [source](https://gymaware.zendesk.com/hc/en-us/articles/4414960013199-GymAware-RS-Specifications)).
- **Variants:** Per-rep values come from the `/reps` analysis label for concentric mean velocity. Personal best: `/bests.meanVelocity`. Eccentric mean velocity is a separate rep metric.
- **What changes the number:** Concentric phase detection. GymAware starts the phase "where the displacement rapidly changes", not at the lowest point. It excludes the catch in Olympic lifts ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000067676-Rep-Detection)). In a light clean with a high catch, the rep end may include the stand-up, which "will report low". Coaches can move the end of the rep in the Cloud ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000172515-The-Clean-and-variations-rep-detection)). Angle correction converts tether length to vertical height ([source](https://kinetic.com.au/pdf/angle.pdf)). Mean velocity runs to the top of the bar path, unlike mean propulsive velocity, which GymAware does not provide ([source](https://gymaware.com/do-you-need-mean-propulsive-velocity/)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics , https://gymaware.zendesk.com/hc/en-us/articles/333756988456-What-s-the-difference-between-Peak-Mean-Velocity

#### `peakVelocity` (m/s)

The block has these fields:

- **What it measures:** Highest instantaneous concentric velocity in the set.
- **Calculation:** GymAware describes `peakVelocity` as the peak velocity of the peak rep, in m/s ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). GymAware says peak velocity is an instantaneous value taken over a sample period of about 20 milliseconds ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: the largest v = Δd / Δt over about 20 ms within the concentric phase, from the rep where it is highest.
- **Inputs and units:** Position in m and time in s.
- **Variants:** Per-rep concentric peak velocity in `/reps`. `/bests.peakVelocity`. Eccentric peak velocity is a separate rep metric.
- **What changes the number:** Sample timing (about 20 ms) and rep detection. GymAware says mean and peak velocity "typically correlate well" ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756988456-What-s-the-difference-between-Peak-Mean-Velocity)). GymAware suggests peak velocity for Olympic lifts and jumps ([source](https://gymaware.com/velocity-based-training-zones-framework/)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### `meanPower` (W)

The block has these fields:

- **What it measures:** Average power over the concentric phase of the best rep.
- **Calculation:** GymAware describes `meanPower` as the mean power of the best rep, in W ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Concentric mean power is the sum of point powers divided by the number of concentric data points. Power is p = f × v, and force is f = m × (a + g) with g = 9.81 ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: for each data point, p_i = m × (a_i + 9.81) × v_i. Mean power = (sum of p_i) / n over the concentric points. m is the moved mass in kg, a_i is vertical acceleration in m/s², and v_i is vertical velocity in m/s.
- **Inputs and units:** Mass in kg. Power and work always use angle-corrected vertical height ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **Which mass m includes:** For most exercises, m is the entered bar weight. Some exercises include body mass automatically; these show "+BM", and coaches can turn the setting on or off per exercise ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001650131-What-does-BM-mean-on-the-top-right-corner-of-my-exercises)). For jumps, GymAware adds the athlete's body mass to the external mass of the bar automatically ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware)). Whether `barWeight` in the API includes body mass for +BM exercises: Not published. Which exercises are +BM by default: Not published.
- **Variants:** `meanWattsPerKg` (relative). Per-rep concentric mean power in `/reps`. `/bests.meanPower`.
- **What changes the number:** Wrong bar weight or body mass. GymAware stresses that correct load entry matters most for power values ([source](https://gymaware.zendesk.com/hc/en-us/articles/6948065276303-Editing-Sets)). An unusually low value often means the algorithm included bar movement outside the lift ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001148431-Peak-Power-or-Mean-Power)). An app release (v4.1.7, date Not published) fixed "body mass calculation for some exercises" ([source](https://gymaware.zendesk.com/hc/en-us/articles/9898695339023-Change-Log-History)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics , https://kinetic.com.au/pdf/angle.pdf

#### `peakPower` (W)

The block has these fields:

- **What it measures:** Highest instantaneous concentric power in the best rep.
- **Calculation:** GymAware describes `peakPower` as the peak power of the best rep, in W ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). It is an instantaneous value over about 20 ms, with p = f × v ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: the maximum of m × (a + 9.81) × v over the concentric phase.
- **Inputs and units:** Same as `meanPower`.
- **Variants:** `peakWattsPerKg`. Per-rep concentric peak power. `/bests.peakPower`. Eccentric peak power is a separate rep metric.
- **What changes the number:** GymAware calls peak power "less repeatable" than mean power because it is a single point in time ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001148431-Peak-Power-or-Mean-Power)). In power cleans, power spikes can come from rapid deceleration when the bar hits the floor; rep detection excludes the catch ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001148431-Peak-Power-or-Mean-Power)). Load entry and the +BM setting also apply.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/115001148431-Peak-Power-or-Mean-Power

#### `meanWattsPerKg`, `peakWattsPerKg` (W/kg)

The block has these fields:

- **What it measures:** Mean or peak power of the best rep relative to body mass.
- **Calculation:** GymAware describes `meanWattsPerKg` as the mean power of the best rep divided by the athlete's body mass, in W/kg. The peak field is defined the same way ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Restated: `meanWattsPerKg` = `meanPower` / `athleteWeight`, and `peakWattsPerKg` = `peakPower` / `athleteWeight`.
- **Inputs and units:** Power in W and body mass in kg.
- **Variants:** Per-rep "Mean Watts/kg" and "Peak Watts/kg" analysis types ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure)). `/bests.meanWattsPerKg` and `/bests.peakWattsPerKg`. The Cloud can label these W/lb if body mass is set to lb ([source](https://gymaware.zendesk.com/hc/en-us/articles/14664428761999-Updates-to-Bar-Weight-Body-Mass-and-Distance-Settings)).
- **What changes the number:** Body mass entry. Coaches can edit body mass on a set ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)). Value when body mass is missing: Not published.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### `height` (unit Not published in the API; Cloud shows m or in)

The block has these fields:

- **What it measures:** The highest point reached above the zero point, for the highest rep in the set.
- **Calculation:** GymAware describes `height` as the height of the highest rep, useful for jumps ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Height is the distance moved above the zero point, corrected for horizontal displacement. The zero point is set when the user presses **Set zero** and can be reset on the graph ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: height = maximum vertical position minus the zero position.
- **Inputs and units:** Vertical position.
- **Variants:** Per-rep Height. `/bests.height`. FLEX Height is "adjusted for any dip in the movement" ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947872421007-FLEX-Metrics-Displayed)).
- **What changes the number:** The start position. For jumps, GymAware recommends Manual Record and starting the recording with the athlete "Standing Tall" ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware)). The broomstick setup and unit placement also matter ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757036795-Jump-Testing)). GymAware measures jump height directly. GymAware says jump mats "typically" give higher values ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### `dip` (unit Not published in the API; Cloud shows m or in)

The block has these fields:

- **What it measures:** The lowest point below the start, for the deepest rep in the set.
- **Calculation:** GymAware describes `dip` as the height of the lowest dip, useful in squats ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Dip is the distance the weight moves below the start point of the eccentric phase, corrected for horizontal displacement ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: dip = start position minus lowest position.
- **Inputs and units:** Vertical position.
- **Variants:** Per-rep Dip. `/bests.dip`.
- **What changes the number:** Where the zero or start point is set ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### `velocityZone` (category)

The block has these fields:

- **What it measures:** The velocity zone of the set.
- **Calculation:** GymAware describes `velocityZone` as the velocity zone category ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). The possible values, the thresholds, and which velocity the field uses: Not published. GymAware's education page uses mean-velocity zones ([source](https://gymaware.com/velocity-based-training-zones-framework/)):
  - Absolute strength: below 0.5 m/s.
  - Accelerative strength: 0.5 to 0.75 m/s.
  - Strength-speed: 0.75 to 1.0 m/s.
  - Speed-strength: 1.0 to 1.3 m/s.
  - Starting strength: above 1.3 m/s.

  VALD's VBT 101 sheet shows the same ranges in its "VBT in Practice" panel ([source](https://resources.vald.com/hubfs/VALD%20Cheat%20Sheets%20(Resource)/VBT%20101.pdf)). Its force-velocity chart on the same page labels some zones with different ranges. VALD's zones article gives the same velocity ranges but different %1RM bands ([source](https://valdperformance.com/news/understanding-velocity-zones-applying-velocity-based-training-to-program-design)). Do not assume these zones map to `velocityZone`.
- **Inputs and units:** String.
- **Variants:** None.
- **What changes the number:** Not published.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.com/velocity-based-training-zones-framework/

#### `targets` (object)

The block has these fields:

- **What it measures:** The target the athlete aimed at during the set.
- **Calculation:** The object has these keys ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)):
  - `analysis`: the analysis parameter the target uses.
  - `mode`: personal, squad, last set, or personal best.
  - `preset`, `squad`, `last`, and `best`: each an object with `min` and `max` at the time of collection.

  In the app, a % zone with no target is a percentage "of the best rep of the set" ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained)).
- **Inputs and units:** `min` and `max` use the unit of the target metric. Exact `mode` strings: Not published.
- **Variants:** Squad, athlete, personal best, last rep, and % zone targets ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained)).
- **What changes the number:** Coach settings at the time of the set.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/ , https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained

#### `barWeight` (kg)

The block has these fields:

- **What it measures:** The external load lifted.
- **Calculation:** GymAware describes `barWeight` as the lift mass in kg ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Restated: the load the coach or athlete entered.
- **Inputs and units:** kg in the API. The app can take lb or kg ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000814611-How-do-I-change-the-metric-used-of-my-bodyweight-and-bar-weight)).
- **Variants:** Present in `/summaries`, `/reps`, and `/bests`. In `/bests`, it is part of the row key.
- **What changes the number:** Manual entry and later edits ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)). Whether the value includes body mass for +BM exercises: Not published.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/

#### `athleteWeight` (kg)

The block has these fields:

- **What it measures:** Athlete body mass stored with the set.
- **Calculation:** GymAware describes `athleteWeight` as the athlete's body mass in kg ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
- **Inputs and units:** kg.
- **Variants:** Present in `/summaries` and `/reps`. Not present in `/bests`.
- **What changes the number:** Manual entry and set edits ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)). The app can hide body mass from display ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000692815-How-do-I-show-hide-the-body-mass-of-my-athletes)).
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/

### Personal bests (`/bests`)

#### `height`, `dip`, `meanVelocity`, `peakVelocity`, `meanPower`, `peakPower`, `meanWattsPerKg`, `peakWattsPerKg` in `/bests`

The block has these fields:

- **What it measures:** The athlete's best values for one exercise at one bar weight.
- **Calculation:** GymAware describes the `/bests` fields as personal best information per athlete, per exercise, and per weight. The field descriptions match `/summaries`. For example, `meanVelocity` is the mean velocity of the best rep, in m/s ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). How the personal best is chosen, and whether each field can come from a different rep or set: Not published. The `start` and `end` filter on `recorded` time, so bests are within the window ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
- **Inputs and units:** Same as the `/summaries` fields.
- **Variants:** The app's "PB" target uses the best rep that one athlete has completed at a given weight ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained)).
- **What changes the number:** The time window, the bar weight grouping, and deleted or edited sets.
- **Sources:** https://gymaware.com/gymaware-cloud-api-integration-guide/

### Rep-level metrics (`/reps`)

Each entry in `reps` holds `REPNUM` plus one float per analysis type. For each analysis type in the `/analysis` endpoint, the rep entry carries one more value ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). Use `/analysis` to get the key names (`label`) and how to aggregate each key. `isPeak` means the highest value is best, `isMin` means the lowest, and `isMean` means the average ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). The example app applies `min`, mean, or `max` per set based on these flags ([source](https://bitbucket.org/KineticPerformance/gymawareapi/src/master/example.py)).

The exact `label` strings are Not published. The blocks below use GymAware's display names from the Help Center. Match each display name to a label in your own `/analysis` output before you use it ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Many eccentric, timing, and jump metrics need a Premium license or the Advanced Metrics add-on ([source](https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options)). Whether `/analysis` returns those labels on lower tiers: Not published.

#### Conc Mean Velocity (m/s)

The block has these fields:

- **What it measures:** Average velocity over the concentric phase of one rep.
- **Calculation:** GymAware defines it as the average velocity over the concentric phase of the lift. It sums point velocities and divides by the number of points, with v = (d2 - d1) / (t2 - t1) ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: mean of Δd / Δt across all concentric data points of the rep.
- **Inputs and units:** Vertical position in m and time in s.
- **Variants:** The set-level `meanVelocity` is this value for the best rep. Average mean velocity across a set is a separate Cloud aggregate ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756988456-What-s-the-difference-between-Peak-Mean-Velocity)).
- **What changes the number:** Concentric phase detection, angle correction, and protocol. See `meanVelocity`.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Peak Velocity (Max Velocity) (m/s)

The block has these fields:

- **What it measures:** Highest instantaneous velocity in the concentric phase of one rep.
- **Calculation:** GymAware says it is an instantaneous value, taken over a sample period of about 20 milliseconds ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: maximum Δd / Δt over about 20 ms in the concentric phase.
- **Inputs and units:** m and s.
- **Variants:** Set-level `peakVelocity`. Ecc Peak Velocity.
- **What changes the number:** See `peakVelocity`.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Mean Power (W)

The block has these fields:

- **What it measures:** Average power over the concentric phase of one rep.
- **Calculation:** GymAware sums point powers and divides by the number of concentric points, with p = f × v and f = m × (a + g), g = 9.81 ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: mean of m × (a_i + 9.81) × v_i over the concentric points.
- **Inputs and units:** Mass in kg (bar weight, plus body mass for +BM exercises and jumps), and vertical acceleration and velocity ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001650131-What-does-BM-mean-on-the-top-right-corner-of-my-exercises), [source](https://gymaware.zendesk.com/hc/en-us/articles/360000463415-Measuring-Jumps-with-GymAware)).
- **Variants:** Set-level `meanPower`.
- **What changes the number:** Load entry, the +BM setting, and rep detection.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Peak Power (W)

The block has these fields:

- **What it measures:** Highest instantaneous concentric power in one rep.
- **Calculation:** An instantaneous value over about 20 ms, with p = f × v ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: maximum of m × (a + 9.81) × v in the concentric phase.
- **Inputs and units:** As for Conc Mean Power.
- **Variants:** Set-level `peakPower`. Ecc Peak Power.
- **What changes the number:** As for `peakPower`.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Mean Watts/kg and Peak Watts/kg (W/kg or W/lb)

The block has these fields:

- **What it measures:** Concentric mean or peak power of one rep relative to body mass.
- **Calculation:** GymAware defines the mean version as the average power applied over the concentric phase, divided by the athlete's body mass. The peak version is defined the same way ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: Conc Mean Power / body mass, and Conc Peak Power / body mass.
- **Inputs and units:** W and kg or lb ([source](https://gymaware.zendesk.com/hc/en-us/articles/14664428761999-Updates-to-Bar-Weight-Body-Mass-and-Distance-Settings)).
- **Variants:** Set-level `meanWattsPerKg` and `peakWattsPerKg`.
- **What changes the number:** Body mass entry.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Mean Force (N)

The block has these fields:

- **What it measures:** Average force over the concentric phase.
- **Calculation:** GymAware sums point forces and divides by the number of concentric points, with f = m × (a + g), g = 9.81 ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: mean of m × (a_i + 9.81).
- **Inputs and units:** Mass in kg and acceleration in m/s².
- **Variants:** Conc Peak Force. Eccentric mean force appears on the RS product page without a definition ([source](https://gymaware.com/gymaware-rs/)).
- **What changes the number:** Load entry and the +BM setting. GymAware notes that mean force "barely changes in response to training" in jump monitoring research ([source](https://gymaware.com/monitoring-fatigue/)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Peak Force (N)

The block has these fields:

- **What it measures:** Highest instantaneous concentric force.
- **Calculation:** GymAware says it is an instantaneous measure taken over a sample period of about 20 milliseconds, with f = m × (a + g) ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: maximum of m × (a + 9.81) in the concentric phase.
- **Inputs and units:** kg and m/s².
- **Variants:** Ecc Peak Force. Time to Peak Force.
- **What changes the number:** Load entry, the +BM setting, and sampling.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Rate of Force Development, RFD (kN/s)

The block has these fields:

- **What it measures:** The fastest rise in force during the concentric phase.
- **Calculation:** GymAware defines RFD as the steepest part of the force curve between two sample points. It is measured only in the concentric phase, so the initial RFD is ignored ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated)). The parameters page defines it as the change in force divided by the change in time over the concentric phase ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: maximum of (f_(i+1) - f_i) / (t_(i+1) - t_i) across consecutive concentric samples, in kN/s.
- **Inputs and units:** Force in N and time in s, reported in kN/s.
- **Variants:** None.
- **What changes the number:** GymAware calls the value "easily affected by protocol and athlete coordination", especially in continuous jumps. GymAware suggests mean power or peak velocity instead ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated

#### Time to Peak Velocity, Time to Peak Force, Time to Peak Power (s)

The block has these fields:

- **What it measures:** Time from the start of the concentric phase to the peak of each metric.
- **Calculation:** GymAware defines Time to Peak Velocity as the time taken to reach peak velocity during the concentric phase. Force and power are defined the same way ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: t(peak) - t(concentric start).
- **Inputs and units:** s. The Cloud lists them as "Time Peak Velocity (s pk m/s)", "Time Peak Force (s pk N)", and "Time Peak Power (s pk W)" ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure)).
- **Variants:** One per metric, as named above.
- **What changes the number:** Concentric start detection.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Rep Duration (s)

The block has these fields:

- **What it measures:** Time of the concentric (lifting) phase.
- **Calculation:** t = t2 - t1, from concentric start to concentric finish ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** s.
- **Variants:** Ecc Rep Duration and Rep Duration.
- **What changes the number:** Rep detection. In a 2010 calibration-rig study, GymAware's typical error was up to 0.16 s for repetition duration ([source](https://gymaware.com/reliability-and-validity-of-gymaware/)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Ecc Rep Duration (s)

The block has these fields:

- **What it measures:** Time of the eccentric (lowering) phase.
- **Calculation:** T = t2 - t1, from eccentric start to eccentric finish ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). FLEX calls it "Eccentric Time" ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947987884943-FLEX-Eccentrics)).
- **Inputs and units:** s.
- **Variants:** On RS, eccentric metrics need Premium ([source](https://gymaware.zendesk.com/hc/en-us/articles/7006425471759-GymAware-Eccentrics)).
- **What changes the number:** How the start and end of the eccentric phase are detected: Not published.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Rep Duration (s)

The block has these fields:

- **What it measures:** Time for one full rep, eccentric plus concentric.
- **Calculation:** GymAware defines it as the difference between the rep start time and the rep end time ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** s.
- **Variants:** Rep Rate.
- **What changes the number:** Rep detection.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Rep Rate (reps/min)

The block has these fields:

- **What it measures:** Predicted reps per minute.
- **Calculation:** GymAware says Rep Rate takes the rep duration in seconds and predicts how many reps the athlete could produce in a minute ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: likely 60 / Rep Duration. The exact formula is Not published.
- **Inputs and units:** reps/min. The Cloud shows "Rep Rate (M)" ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure)).
- **Variants:** None.
- **What changes the number:** Rep Duration.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Conc Work (J)

The block has these fields:

- **What it measures:** Mechanical work to raise the load from the lowest to the highest point of a rep.
- **Calculation:** GymAware gives the formula "W=mgh", with g = 9.81 and h = height of lift ([source](https://gymaware.zendesk.com/hc/en-us/articles/360001365695-Conc-Work-J)). Restated: work = mass × 9.81 × vertical lift height.
- **Inputs and units:** kg and m. h uses angle-corrected vertical height ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **Variants:** None.
- **What changes the number:** Range of motion. Shallower squats lower the value. Taller athletes do more work at the same load ([source](https://gymaware.zendesk.com/hc/en-us/articles/360001365695-Conc-Work-J)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/360001365695-Conc-Work-J

#### Height (m or in)

The block has these fields:

- **What it measures:** The highest point reached above the zero point in one rep.
- **Calculation:** See `height` in `/summaries` ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** m or in.
- **Variants:** Set-level `height` (highest rep).
- **What changes the number:** The zero point and the jump protocol.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Dip (m or in)

The block has these fields:

- **What it measures:** The lowest point below the start in one rep.
- **Calculation:** See `dip` in `/summaries` ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** m or in.
- **Variants:** Set-level `dip` (lowest dip).
- **What changes the number:** The start point.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Lift Distance (m or in)

The block has these fields:

- **What it measures:** Total tether extension from the bottom to the top of a rep, with no angle correction.
- **Calculation:** GymAware states that Lift Distance is not corrected for errors from horizontal displacement ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: raw tether length change from bottom to top.
- **Inputs and units:** m or in.
- **Variants:** Vertical Distance (corrected). FLEX "Distance" is vertical displacement from the lowest to the highest point ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947872421007-FLEX-Metrics-Displayed)).
- **What changes the number:** Unit placement relative to the bar path ([source](https://gymaware.com/gymaware-rs-vs-flex/)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Vertical Distance (m or in)

The block has these fields:

- **What it measures:** Vertical displacement from the bottom to the top of a rep.
- **Calculation:** GymAware defines it as the bottom-to-top distance, corrected for errors from horizontal displacement ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Restated: sum of r sin θ changes, the vertical component only ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **Inputs and units:** m or in.
- **Variants:** Lift Distance (raw).
- **What changes the number:** Angle measurement. In a power clean example, the correction changed displacement from 0.56 m to 0.54 m ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics , https://kinetic.com.au/pdf/angle.pdf

#### Total Travel Path (m or in)

The block has these fields:

- **What it measures:** Total distance travelled in a rep.
- **Calculation:** GymAware defines it as the total distance travelled, without accounting for horizontal or vertical displacement ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). The exact formula is Not published.
- **Inputs and units:** m or in.
- **Variants:** None.
- **What changes the number:** Not published.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Horizontal (m)

The block has these fields:

- **What it measures:** Total horizontal displacement of the bar or tether from the vertical axis over a rep.
- **Calculation:** GymAware says the value is calculated and corrected for errors from vertical displacement ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). The exact formula is Not published.
- **Inputs and units:** m.
- **Variants:** Max Back and Max Forward. Bar path display ([source](https://gymaware.zendesk.com/hc/en-us/articles/360003388095-Version-2-9-Release-Notes)).
- **What changes the number:** RS angle range is -50° to +70° ([source](https://gymaware.zendesk.com/hc/en-us/articles/4414960013199-GymAware-RS-Specifications)). GymAware says the angle sensor targets "a relatively small horizontal component" ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Max Back, Max Forward, Height at Max Back, Height at Max Forward (m or in)

The block has these fields:

- **What it measures:** The furthest backward and forward horizontal bar positions, and the vertical height where each occurs.
- **Calculation:** GymAware defines Max Back and Max Forward as the distance the tether moves to the furthest backward or forward horizontal point from the vertical axis. It defines Height at Max Back and Height at Max Forward as the vertical height, measured from the start of the concentric phase, at those points ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** m or in. Sign convention for back and forward: Not published.
- **Variants:** The four named fields.
- **What changes the number:** Which side of the athlete the unit sits on: Not published.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Nordic Displacement (m or in)

The block has these fields:

- **What it measures:** Movement in a Nordic hamstring curl.
- **Calculation:** GymAware says it measures the Nordic movement from the concentric phase to the free fall phase ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). The exact formula is Not published.
- **Inputs and units:** m or in.
- **Variants:** None.
- **What changes the number:** Mounting. Sideways mounting works only if the unit is woken in an upright orientation first ([source](https://gymaware.zendesk.com/hc/en-us/articles/115004558528-Positioning-Sideways-mounting)). Some users turn the angle measurement off for Nordic curls ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756987176-PowerTool-and-Global-settings)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Ecc Mean Velocity (m/s)

The block has these fields:

- **What it measures:** Average velocity over the eccentric phase.
- **Calculation:** GymAware sums point velocities and divides by the number of eccentric points, with v = (d2 - d1) / (t2 - t1) ([source](https://gymaware.zendesk.com/hc/en-us/articles/7006425471759-GymAware-Eccentrics)). Sign convention (positive or negative): Not published.
- **Inputs and units:** m/s.
- **Variants:** FLEX "Eccentric Mean Velocity" ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947987884943-FLEX-Eccentrics)).
- **What changes the number:** Eccentric metrics on RS need Premium ([source](https://gymaware.zendesk.com/hc/en-us/articles/7006425471759-GymAware-Eccentrics)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/7006425471759-GymAware-Eccentrics

#### Ecc Peak Velocity (m/s)

The block has these fields:

- **What it measures:** Highest instantaneous eccentric velocity.
- **Calculation:** An instantaneous value over about 20 ms ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Sign convention: Not published.
- **Inputs and units:** m/s.
- **Variants:** FLEX "Eccentric Peak Velocity" ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947987884943-FLEX-Eccentrics)).
- **What changes the number:** Sampling and phase detection.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Eccentric Minimum Velocity (m/s)

The block has these fields:

- **What it measures:** Listed as a Cloud metric ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure)).
- **Calculation:** Not published.
- **Inputs and units:** Unit Not published.
- **Variants:** None.
- **What changes the number:** Not published.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/115000820192-What-parameters-does-GymAware-measure , https://gymaware.zendesk.com/hc/en-us/articles/4408138835599-Cloud-Subscription-options

#### Ecc Peak Power (W)

The block has these fields:

- **What it measures:** Highest instantaneous power in the eccentric phase.
- **Calculation:** An instantaneous value over about 20 ms, with p = f × v ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Sign convention: Not published.
- **Inputs and units:** W.
- **Variants:** Eccentric mean power appears on the RS product page without a definition ([source](https://gymaware.com/gymaware-rs/)).
- **What changes the number:** Load entry and the +BM setting.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Ecc Peak Force (N)

The block has these fields:

- **What it measures:** Highest instantaneous force in the eccentric phase.
- **Calculation:** An instantaneous value over about 20 ms, with f = m × (a + g) ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- **Inputs and units:** N.
- **Variants:** Conc Peak Force.
- **What changes the number:** Load entry and the +BM setting.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Reactive Strength Index, RSI (m/s)

The block has these fields:

- **What it measures:** Reactive jump capacity in a drop jump.
- **Calculation:** GymAware gives the formula "RSI = Jump Height / Ground Contact Time" ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI)).
- **Inputs and units:** Height in m and Contact Time in s.
- **Variants:** Available only in Cloud analysis, not on the iPad ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI)).
- **What changes the number:** GymAware says RSI does not calculate unless the start position is set at floor level. The Cloud removes the step-up onto the box ([source](https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/360000463695-Testing-depth-jumps-and-obtaining-RSI

#### Contact Time (s)

The block has these fields:

- **What it measures:** Ground contact time in a drop jump or rebound jump.
- **Calculation:** GymAware defines it as the difference between the time of landing and the time of takeoff ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). How GymAware detects landing and takeoff: Not published.
- **Inputs and units:** s.
- **Variants:** Flight Time.
- **What changes the number:** The starting position, the same way it affects height and dip ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000942652-How-is-RFD-calculated)).
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Flight Time (s)

The block has these fields:

- **What it measures:** Time airborne in a jump.
- **Calculation:** GymAware defines it as the difference between the time of takeoff and the time of landing ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)). Detection method: Not published.
- **Inputs and units:** s.
- **Variants:** None.
- **What changes the number:** Not published.
- **Sources:** https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics

#### Concentric and eccentric peak acceleration (m/s²), eccentric mean power (W), eccentric mean force (N)

The block has these fields:

- **What it measures:** Listed on the RS product page ([source](https://gymaware.com/gymaware-rs/)).
- **Calculation:** Not published.
- **Inputs and units:** As listed.
- **Variants:** Not published.
- **What changes the number:** Not published.
- **Sources:** https://gymaware.com/gymaware-rs/

### Derived values not in the API

#### Velocity loss, velocity drop-off, or fatigue target (%)

The block has these fields:

- **What it measures:** How much rep velocity falls across a set.
- **Calculation:** No API field carries velocity loss ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)). GymAware publishes no formal formula. Its worked examples all use the first rep as the reference:
  - First rep 1.5 m/s, rep 4 1.28 m/s: GymAware's example gives a velocity loss of 0,22 m/s, or 15% ([source](https://gymaware.com/velocity-loss-in-strength-training/)).
  - First rep 1.5 m/s, 9th rep 1.2 m/s: 20% ([source](https://gymaware.com/train-to-velocity-failure-using-velocity-stops/)).
  - First rep 0.52 m/s, final rep 0.41 m/s: "around 21%" ([source](https://gymaware.com/gymaware-flex-app-data-and-implementation/)).
  - GymAware defines VL30 as a 30% decrease in velocity between the first lift and the last lift ([source](https://gymaware.com/velocity-based-training/)).

  Restated from these examples: velocity loss % = (V_first - V_rep) / V_first × 100. V is the rep's mean velocity in m/s.
- **Conflicting reference reps:**
  - A FLEX app screenshot caption says the app shows velocity loss "compared to the previous rep" ([source](https://gymaware.com/train-to-velocity-failure-using-velocity-stops/)).
  - The GymAware app % zone uses "the best rep of the set" when no target is set ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756999116-Targets-Explained)).
  - VALD says velocity loss is typically calculated by comparing the fastest repetition in a set with the later repetitions ([source](https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training)). VALD's example: a fastest rep of 0.70 m/s with a 20% threshold gives about 0.56 m/s.
  - Which rep the GymAware app uses for its fatigue target: Not published.
- **Inputs and units:** Rep mean velocity, from the `/reps` analysis label for concentric mean velocity, ordered by `REPNUM`. GymAware's examples use mean velocity. Whether the app can use peak velocity for drop-offs: Not published. On FLEX, fatigue targets are entered as a % drop ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947985838479-Set-a-Velocity-Target)).
- **Variants:** Velocity stop is a fixed m/s cut-off, for example 1.2 m/s ([source](https://gymaware.com/train-to-velocity-failure-using-velocity-stops/)). VALD's heuristic thresholds are about 10% for power, 20% for strength, and 30% for hypertrophy ([source](https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training)). A GymAware author calls 10 to 20% loss "little to no fatigue" and 40% or more "extreme fatigue" ([source](https://gymaware.com/understanding-velocity-loss/)).
- **What changes the number:** The reference rep (first, fastest, or previous). Rep detection and deleted reps. Spike reps on FLEX when the device leaves the mat ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947985920271-Spike-reps-Inaccurate-reps)).
- **Sources:** https://gymaware.com/velocity-loss-in-strength-training/ , https://gymaware.com/train-to-velocity-failure-using-velocity-stops/ , https://gymaware.com/velocity-based-training/ , https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training

Other derived values: GymAware estimates 1RM where a linear load-velocity line crosses the exercise's minimum velocity threshold. Its example uses 0.16 m/s for bench press ([source](https://gymaware.com/gymaware-1rm-calculation/)). The Cloud help page says maximum strength is "predicted to occur at approximately 0.3m/s" ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757036735-1RM-Predictive-strength-testing)). Neither value is an API field.

### What changes any GymAware number

These factors change any GymAware number:

- **Sampling:** RS uses Variable Rate Sampling with level-crossing detection, down-sampled to at most 50 points per second. GymAware says this needs no filtering ([source](https://kinetic.com.au/pdf/sample.pdf)). Time-stamp resolution is stated as 8.6 microseconds ([source](https://gymaware.zendesk.com/hc/en-us/articles/115001133391-GymAware-Fact-sheets)) and as 35 microseconds ([source](https://kinetic.com.au/pdf/sample.pdf)).
- **RS specifications:** 0.8 mm position resolution, 3.66 m tether, and 6.5 m/s maximum velocity ([source](https://gymaware.zendesk.com/hc/en-us/articles/4414960013199-GymAware-RS-Specifications)). The older PowerTool lists 0.3 mm resolution and 7 m/s ([source](https://gymaware.zendesk.com/hc/en-us/articles/115005013548-PowerTool-specifications)).
- **Zero:** Zero RS with the tether fully retracted. The app flags a wrong zero ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756987176-PowerTool-and-Global-settings)).
- **Angle:** Angle correction is on by default. Turning it off changes distance-based values ([source](https://gymaware.zendesk.com/hc/en-us/articles/333756987176-PowerTool-and-Global-settings)). A large angle change within a set flags a suspect result ([source](https://kinetic.com.au/pdf/angle.pdf)).
- **FLEX:** The laser range is 2.2 m, and the mat must lie flat ([source](https://gymaware.zendesk.com/hc/en-us/articles/6947901598735-FLEX-Considerations)).
- **Edits:** Coaches can change athlete, exercise, bar weight, and body mass on a set, and delete reps ([source](https://gymaware.zendesk.com/hc/en-us/articles/115000941271-Editing-Data-on-the-Cloud)). Use `modified` and `modifiedSince` to catch edits ([source](https://gymaware.com/gymaware-cloud-api-integration-guide/)).
- **Barbell versus system velocity:** GymAware measures bar velocity, not center-of-mass velocity ([source](https://gymaware.com/barbell-vs-system-velocity/)).

### Not published

GymAware does not publish these details in the public sources checked:

- Exact `/analysis` label strings, and their units in the API.
- Units of `height` and `dip` in the API. Whether API values follow the lb or inch display settings.
- How `/summaries` and `/bests` choose the "best rep" and personal best. Whether all best-rep fields come from one rep.
- `velocityZone` values and thresholds.
- `targets.mode` strings.
- Whether `barWeight` includes body mass for +BM exercises. Which exercises are +BM by default.
- Whether API rows mark the recording device (RS or FLEX).
- CSV export columns and row level.
- A GymAware asymmetry formula, and any side field.
- Pagination parameters.
- Rep Rate exact formula.
- Total Travel Path, Horizontal, and Nordic Displacement formulas.
- Sign conventions for eccentric metrics, Max Back, and Max Forward.
- Eccentric Minimum Velocity definition.
- Eccentric phase start and end rules.
- Contact Time and Flight Time detection.
- Peak acceleration, eccentric mean power, and eccentric mean force definitions.
- A formal velocity-loss formula, and the reference rep the app uses for fatigue targets.
- The `notes`, `referenceID`, and `userID` fields used by the example app.
- The URL of the activities endpoint in the guide (the example app uses `activities`).

## Worked example

This example uses made-up values and was run with Python 3.9 on 2026-10-02. The output below is copied from that run.

### GymAware mean velocity, peak velocity, mean power, and velocity loss

What the script does:

- Builds an example concentric position trace for each rep in a six-rep set.
- Computes point velocity v = (d2 - d1) / (t2 - t1), mean concentric velocity, peak velocity over about 20 ms, and mean power p = m(a + 9.81)v, as GymAware defines them ([source](https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics)).
- Computes velocity loss two ways. GymAware's worked examples use the first rep as the reference ([source](https://gymaware.com/velocity-loss-in-strength-training/)). VALD describes the fastest rep ([source](https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training)). Neither publishes a formal formula, so name the reference rep you use.

```python
"""GymAware worked example: rep velocity, power, and velocity loss in one set.

All inputs are made-up example values, not athlete data.

Definitions used (GymAware Help Center,
https://gymaware.zendesk.com/hc/en-us/articles/333757013756-Parameters-explained-measurement-metrics):
- Point velocity v = (d2 - d1) / (t2 - t1).
- Mean concentric velocity = sum of point velocities / number of points.
- Peak velocity = highest value over a sample period of about 20 ms.
- Power p = f * v, with f = m * (a + 9.81).
Velocity loss has no API field and no published formula. GymAware's worked
examples use the first rep as the reference; VALD describes the fastest rep.
This script prints both.
"""

G = 9.81
DT = 0.001          # s between example position samples
PEAK_WINDOW = 0.020 # s, the "approximately 20 milliseconds" peak window
BAR_KG = 100.0      # example bar load; body mass not added (no +BM)
ROM_M = 0.45        # example concentric displacement per rep

# Example set: concentric duration (s) per rep. Rep 2 is fastest, then reps slow down.
rep_durations_s = [0.58, 0.55, 0.60, 0.64, 0.69, 0.76]


def concentric_positions(duration, rom):
    """Example position trace (m): smooth rise from 0 to rom over duration."""
    import math
    n = int(round(duration / DT))
    return [rom * (1 - math.cos(math.pi * i / n)) / 2 for i in range(n + 1)]


def rep_metrics(positions, mass):
    # Point velocities: v = (d2 - d1) / (t2 - t1)
    vel = [(b - a) / DT for a, b in zip(positions, positions[1:])]
    mean_v = sum(vel) / len(vel)
    # Peak velocity over a ~20 ms window (moving average of point velocities)
    w = int(round(PEAK_WINDOW / DT))
    windows = [sum(vel[i:i + w]) / w for i in range(len(vel) - w + 1)]
    peak_v = max(windows)
    # Acceleration from successive velocities, then f = m(a + g), p = f * v
    acc = [(b - a) / DT for a, b in zip(vel, vel[1:])]
    power = [mass * (a + G) * v for a, v in zip(acc, vel[1:])]
    mean_p = sum(power) / len(power)
    return mean_v, peak_v, mean_p


reps = []
for repnum, dur in enumerate(rep_durations_s, start=1):
    mv, pv, mp = rep_metrics(concentric_positions(dur, ROM_M), BAR_KG)
    reps.append({"REPNUM": repnum, "mean_velocity": mv,
                 "peak_velocity": pv, "mean_power": mp})

first_mv = reps[0]["mean_velocity"]
fastest_mv = max(r["mean_velocity"] for r in reps)

print(f"Example set: bar {BAR_KG:.0f} kg, concentric displacement {ROM_M} m, sample step {DT*1000:.0f} ms")
print(f"{'REPNUM':>6} {'conc time (s)':>13} {'mean vel (m/s)':>15} {'peak vel (m/s)':>15} "
      f"{'mean power (W)':>15} {'loss vs first (%)':>18} {'loss vs fastest (%)':>20}")
for r, dur in zip(reps, rep_durations_s):
    loss_first = (first_mv - r["mean_velocity"]) / first_mv * 100
    loss_fast = (fastest_mv - r["mean_velocity"]) / fastest_mv * 100
    print(f"{r['REPNUM']:>6} {dur:>13.2f} {r['mean_velocity']:>15.3f} {r['peak_velocity']:>15.3f} "
          f"{r['mean_power']:>15.1f} {loss_first:>18.1f} {loss_fast:>20.1f}")

best = max(reps, key=lambda r: r["mean_velocity"])
avg_mv = sum(r["mean_velocity"] for r in reps) / len(reps)
last = reps[-1]
print()
print(f"Best rep by mean velocity: REPNUM {best['REPNUM']} ({best['mean_velocity']:.3f} m/s)")
print(f"Average of rep mean velocities: {avg_mv:.3f} m/s")
print(f"Set velocity loss, first to last rep: {(first_mv - last['mean_velocity']) / first_mv * 100:.1f} %")

# Stopping rule check: VALD's heuristic of about 20 % loss for strength work
# (https://valdperformance.com/news/using-vbt-to-autoregulate-and-individualize-resistance-training)
cutoff = fastest_mv * (1 - 0.20)
stop = next((r["REPNUM"] for r in reps if r["mean_velocity"] < cutoff), None)
print(f"20 % cut-off from fastest rep: {cutoff:.3f} m/s; first rep below it: {stop}")

# Check against GymAware's own worked example: 1.5 m/s to 1.28 m/s
v1, v4 = 1.5, 1.28
print(f"GymAware example check: ({v1} - {v4}) / {v1} = {(v1 - v4) / v1 * 100:.1f} %")
```

Output:

```text
Example set: bar 100 kg, concentric displacement 0.45 m, sample step 1 ms
REPNUM conc time (s)  mean vel (m/s)  peak vel (m/s)  mean power (W)  loss vs first (%)  loss vs fastest (%)
     1          0.58           0.776           1.218           763.5                0.0                  5.2
     2          0.55           0.818           1.284           805.4               -5.5                  0.0
     3          0.60           0.750           1.178           737.9                3.3                  8.3
     4          0.64           0.703           1.104           691.6                9.4                 14.1
     5          0.69           0.652           1.024           641.3               15.9                 20.3
     6          0.76           0.592           0.930           582.0               23.7                 27.6

Best rep by mean velocity: REPNUM 2 (0.818 m/s)
Average of rep mean velocities: 0.715 m/s
Set velocity loss, first to last rep: 23.7 %
20 % cut-off from fastest rep: 0.655 m/s; first rep below it: 5
GymAware example check: (1.5 - 1.28) / 1.5 = 14.7 %
```

See [the calculations overview](../calculations.md) for how these metrics relate to the methods in the skills.
