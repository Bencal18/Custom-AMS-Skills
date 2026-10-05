# Estimated load for athletes who did not wear a device

Last checked: 2026-10-05

## What it measures

An estimated load is a stand-in value for an athlete who played but did not wear the device. You build it from the playing time the athlete had and from the load the same athlete recorded in earlier games when they did wear it.

The most common case is a game. Some leagues limit wearables in games, and some athletes choose not to wear them. In ice hockey, for example, wearable use in NHL games is voluntary under a separate NHL and NHL Players' Association agreement (Daily Faceoff, 2024). Staff then estimate heart rate load (TRIMP) or accelerometer load (such as PlayerLoad) for the athletes who did not wear a device. They need the estimate so that weekly load and acute load are not missing a game.

An estimated load is not a measurement. It carries model error on top of the device's own measurement error. Always mark it, and always report how far off the method was on games where you can check it.

The NHL and NHL Players' Association wearable agreement is not public (Daily Faceoff, 2024). Do not tell the user what their league allows. Ask them.

## Formula

No published study validates a model that predicts one athlete's game load from playing time alone, with a reported prediction error. Treat every method here as unvalidated until you check it on the user's own data.

Use the athlete's own load per playing minute from games they wore the device, multiplied by today's playing time:

```text
rate_athlete       = Σ load_measured ÷ Σ playing_min_measured
estimated_load     = rate_athlete × playing_min_today
held_out_error_pct = |estimate_without_game − load_measured| ÷ load_measured × 100
```

Define every term in the formula:

- `load_measured`: the load the device recorded in a game the athlete wore it, in the device's unit, such as TRIMP in arbitrary units (AU) or PlayerLoad in AU.
- `playing_min_measured`: the athlete's playing time in that same game, in minutes. In ice hockey this is time on ice (TOI). In other sports it is minutes played.
- `Σ`: the sum over the measured games the user chooses, such as all games this season of the same session type.
- `rate_athlete`: load per playing minute, in AU per minute. This is a ratio of totals, not the mean of each game's ratio.
- `playing_min_today`: playing time in the game being estimated, in minutes.
- `estimated_load`: the stand-in value, in the same unit as `load_measured`.
- `estimate_without_game`: the estimate for one measured game, made from all the athlete's other measured games. This is a leave-one-game-out check.
- `held_out_error_pct`: how far that held-out estimate was from what the device measured, as a percentage.

Use these variants when the athlete-rate method does not fit:

- **The user's own model.** Many staff already have a formula, such as one built by their head of performance. Apply it as given. Do not change it. Still run the leave-one-game-out check, and report its error.
- **Athlete line.** Fit `load = a + b × playing_min` to the athlete's measured games by least squares, the standard method for fitting a straight line that makes the squared gaps between line and points as small as possible. This allows load per minute to change with playing time. It needs more games than the rate method. This file's choice is at least 10 measured games. That number is not a published rule.
- **Position rate.** When the athlete has no measured games, use `Σ load ÷ Σ playing_min` across athletes of the same position who wore the device. Label it as a group estimate. In Australian football, models built for each athlete predicted session RPE from GPS data with less error than one model for the whole group (Bartlett et al., 2017). Expect a group rate to miss by more.
- **Imputation methods from research.** These fill gaps in a data set for later analysis. In one simulation, multiple imputation with predictive mean matching was best in most scenarios (Bache-Mathiesen et al., 2022). Two other studies disagree about the daily team mean. It was the best of 12 methods for soccer session RPE (Griffin et al., 2021), and the worst of 10 methods for rugby RPE (Epp-Stobbe et al., 2022). In youth basketball, only machine-learning models that combined session and individual information beat the daily team mean (Benson et al., 2021). These studies tested filling random gaps, not estimating a game for a player who never wore a device. Ask a statistician before you use them.

### Use the same playing time in the numerator and the denominator

The device on a wearer records the whole game, including time on the bench and intermissions. Playing time counts only time in play. Divide the measured load by the same playing time you will multiply by.

Do not use a vendor's load-per-minute value as the rate unless the device reference confirms that its minutes are playing minutes. A vendor's per-minute value may divide by the recording time instead. Published ice hockey studies differ in the same way. Some divide by time on ice (Rago et al., 2022, *Journal of Human Kinetics*). Others divide by the whole session (Nightingale et al., 2024). Never mix the two in one rate.

### Calculate it in a spreadsheet or Python

In a spreadsheet, put one row per athlete per game, with `athlete_id` in column `A`, `load_source` in `B` (`measured` or `estimated`), `load` in `C`, playing minutes in `D`, and the time on ice text from the report in `E`. This formula returns one athlete's rate from measured rows only, or a blank if there are none:

```text
=IFERROR(SUMIFS(C:C,A:A,"A07",B:B,"measured")/SUMIFS(D:D,A:A,"A07",B:B,"measured"),"")
```

Replace `"A07"` with a cell that holds the athlete ID. The formula filters only by athlete and source. Keep only games of the same type and season in the sheet, or add a criterion for them.

Time on ice usually arrives as `mm:ss` text, such as `17:10`. A spreadsheet may read it as 17 hours and 10 minutes. Convert the text in column `E` to minutes in column `D` with this formula:

```text
=VALUE(LEFT(E2,FIND(":",E2)-1))+VALUE(MID(E2,FIND(":",E2)+1,2))/60
```

If the cell already holds a time value, the spreadsheet has read `mm:ss` as `hh:mm`. Multiply that value by 24, not by 1,440, to get minutes. Check one row by hand.

Use this Python code for the rate, the estimate, and the leave-one-game-out check. `games` holds one row per measured game for one athlete, with the columns `game`, `toi` (`mm:ss` text), and `load`:

```python
import pandas as pd

def to_min(t):                       # "17:10" -> 17.1667 minutes
    m, s = t.split(":")
    return int(m) + int(s) / 60

games["play_min"] = games["toi"].map(to_min)
rate = games["load"].sum() / games["play_min"].sum()
estimate = rate * to_min("18:30")

rows = []
for i in games.index:                # leave one game out
    rest = games.drop(i)
    r = rest["load"].sum() / rest["play_min"].sum()
    pred = r * games.at[i, "play_min"]
    err = pred - games.at[i, "load"]
    rows.append({"game": games.at[i, "game"], "pred": pred, "err": err,
                 "err_pct": abs(err) / games.at[i, "load"] * 100})
check = pd.DataFrame(rows)
print(round(rate, 3), round(estimate, 1))
print(check.round(1))
print("mean error %:", round(check["err_pct"].mean(), 1),
      "largest %:", round(check["err_pct"].max(), 1))
```

## Calculate estimated load

Follow these steps to estimate load for one athlete and one game:

1. Ask whether the user already has an estimation formula. If they do, convert playing time as in step 4, apply their formula as given, and go to step 9.
2. Ask which load to estimate, such as TRIMP or PlayerLoad, and which device produced the measured values.
3. Ask for the source of playing time, such as time on ice from the official game report.
4. Convert every playing time to decimal minutes.
5. Keep only measured games of the same session type and season that the user chooses.
6. Count the athlete's measured games. With fewer than 5, say the rate rests on few games. This cut-off is this file's choice, not a published rule.
7. Calculate `rate_athlete` as the sum of measured load divided by the sum of measured playing minutes.
8. Multiply the rate by today's playing minutes.
9. Run the leave-one-game-out check on every measured game, and report the mean and largest error in percent. The check needs at least 2 measured games. With 1, say the error cannot be checked.
10. Check whether today's playing time falls inside the range of the measured games. If it does not, say the estimate goes beyond the data.
11. Store the result with `load_source` set to `estimated`, the method name, and the check's mean error.

## Worked example

These numbers are made up. One forward wore a heart rate monitor in six games. The device total is TRIMP in AU for the whole game recording. Time on ice comes from the official game report:

| Game | Time on ice | Minutes | TRIMP (AU) | TRIMP per TOI minute |
|---|---|---|---|---|
| G1 | 17:10 | 17.17 | 94 | 5.48 |
| G2 | 15:40 | 15.67 | 78 | 4.98 |
| G3 | 19:05 | 19.08 | 97 | 5.08 |
| G4 | 16:20 | 16.33 | 92 | 5.63 |
| G5 | 18:15 | 18.25 | 88 | 4.82 |
| G6 | 14:50 | 14.83 | 80 | 5.39 |

In game 7, the athlete did not wear the monitor and played 18:30, which is 18.50 minutes.

Calculate the rate and the estimate:

```text
rate_athlete   = 529 ÷ 101.33 = 5.220 AU per TOI minute
estimated_load = 5.220 × 18.50 = 96.6 AU, reported as 97 AU
```

Leave each game out in turn, and estimate it from the other five:

| Game left out | Rate from the other five | Estimate (AU) | Measured (AU) | Error (AU) | Error (%) |
|---|---|---|---|---|---|
| G1 | 5.168 | 88.7 | 94 | −5.3 | 5.6 |
| G2 | 5.265 | 82.5 | 78 | +4.5 | 5.7 |
| G3 | 5.252 | 100.2 | 97 | +3.2 | 3.3 |
| G4 | 5.141 | 84.0 | 92 | −8.0 | 8.7 |
| G5 | 5.308 | 96.9 | 88 | +8.9 | 10.1 |
| G6 | 5.191 | 77.0 | 80 | −3.0 | 3.8 |

The mean error is 6.2%, and the largest is 10.1%. The 18.50 minutes in game 7 fall inside the measured range of 14.83 to 19.08 minutes. Report the result this way: "Estimated TRIMP 97 AU (athlete rate from 6 games; held-out error 6.2% on average, up to 10.1%)."

The wrong denominator gives a very different number. Each game recording lasted about 150 minutes. The rate per recording minute is 529 ÷ (6 × 150) = 0.588 AU per minute. Multiplied by 18.50 minutes of time on ice, it gives 10.9 AU, about one ninth of the right estimate.

## What changes the number

These choices change the estimate even when the athlete's game does not:

- **Playing time does not scale load in a straight line.** In Danish elite ice hockey, players with more time on ice had fewer accelerations and decelerations per minute and less time above 85% of maximal heart rate (r = −0.63 to −0.18) (Rago et al., 2022, *Journal of Human Kinetics*). A constant rate can overestimate a long game and underestimate a short one. Watch for this in the held-out errors.
- **Position.** Ice hockey defensemen play more minutes at a lower intensity per minute than forwards (Allard et al., 2022; Lignell et al., 2018). Do not apply a forward's rate to a defenseman.
- **Game situation.** Skating speed differed by game situation, such as power play and penalty kill, for both defense and forwards (Douglas & Kennedy, 2020). A game with more special-teams time can have a different rate.
- **Period.** Load per period changed across a game. In varsity hockey, Banister TRIMP rose from period 1 to period 3 (Bigg et al., 2021). In professional hockey, load per minute fell in period 3 (Allard et al., 2022).
- **Which games feed the rate.** A rate built on training sessions does not fit a game. Use games for games.
- **Playing time alone does not capture external load.** In one Kontinental Hockey League (KHL) team, the authors concluded that time on ice alone is not an accurate measure of external load (Nightingale et al., 2024).

## Units and typical range

An estimate has the unit of the load it replaces. It has no published typical range of its own. These figures show how widely game load varies, and how noisy the measured values are. SD is the standard deviation, the usual spread around the mean. Typical error is the spread of repeat measurements on the same athlete when nothing has changed. CV, the coefficient of variation, is that spread as a percentage of the mean:

| Measure | Figure | Source |
|---|---|---|
| Game TRIMP, men's varsity ice hockey | 98 ± 59 AU (mean ± SD) | Bigg et al., 2022 |
| TRIMP test-retest typical error, collegiate ice hockey practices | 12.2% | Ulmer et al., 2019 |
| PlayerLoad test-retest CV, collegiate ice hockey tasks | 2.2% to 26.6% across nine tasks. 26.6% on a repeated shift circuit. | Van Iterson et al., 2017 |
| Time on ice per game, KHL | 16.9 ± 3.5 min for defenders, 14.8 ± 3.0 min for forwards | Nightingale et al., 2024 |

The estimate's own error adds to the device's measurement error. A held-out error of 6% does not make the estimate as good as a measurement.

## Data you need

Collect this data:

- Source: load from the device for games the athlete wore it, and playing time from an official source for every game.
- Sampling: one value per athlete per game for both load and playing time.
- Minimum data: at least 5 measured games of the same type for the athlete rate, and at least 10 for the athlete line. Both cut-offs are this file's choices.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with estimated load:

- Dividing by recording minutes and multiplying by playing minutes. Use playing minutes for both.
- Taking the mean of each game's load per minute instead of total load divided by total minutes. The two differ when games differ in length.
- Reading `17:10` time on ice as 17 hours and 10 minutes. Convert `mm:ss` text to minutes first.
- Mixing estimated and measured values in one column with no marker. Keep a `load_source` column.
- Reporting an estimate with no error figure. Always give the leave-one-game-out error.
- Judging a change in load against the noise band with estimated values in it. Measurement noise figures do not include model error. Say the change cannot be judged against noise when either value is estimated.
- Applying one athlete's rate to another athlete, or a forward's rate to a defenseman.
- Estimating beyond the range of measured playing time without saying so.
- Calling the estimate a measurement in a report to coaches.

## Example request

> Only 5 of our guys wore heart rate monitors last night. I have their TRIMP, and time on ice for everyone from the game report. Can you estimate TRIMP for the rest so our weekly load isn't missing a game?

## Check the result

Run these checks:

- Unit check: playing time is in decimal minutes, and the rate's minutes are the same kind as today's minutes.
- Source check: every estimated row has `load_source` set to `estimated` and names its method.
- Error check: the answer gives the leave-one-game-out mean and largest error for each athlete.
- Range check: today's playing time is inside the athlete's measured range, or the answer says it is not.
- Count check: the answer states how many athletes were measured, how many were estimated, and how many measured games each rate used.
- Total check: weekly totals that include an estimate show the measured part and the estimated part.

## Sources

This file draws on these sources:

- Allard P, Martinez R, Deguire S, Tremblay J. In-season session training load relative to match load in professional ice hockey. J Strength Cond Res. 2022;36(2):486-492. https://doi.org/10.1519/JSC.0000000000003490 Read in abstract form only, 2026-10-05.
- Bache-Mathiesen LK, Andersen TE, Clarsen B, Fagerland MW. Handling and reporting missing data in training load and injury risk research. Science and Medicine in Football. 2022;6(4):452-464. https://doi.org/10.1080/24733938.2021.1998587 Read in abstract form only, 2026-10-05.
- Bartlett JD, O'Connor F, Pitchford N, Torres-Ronda L, Robertson SJ. Relationships between internal and external training load in team-sport athletes: evidence for an individualized approach. Int J Sports Physiol Perform. 2017;12(2):230-234. https://doi.org/10.1123/ijspp.2015-0791 Read in abstract form only, 2026-10-05.
- Benson LC, Stilling C, Owoeye OBA, Emery CA. Evaluating methods for imputing missing data from longitudinal monitoring of athlete workload. J Sports Sci Med. 2021;20(2):188-196. https://doi.org/10.52082/jssm.2021.188 Read in abstract form only, 2026-10-05.
- Bigg JL, Gamble ASD, Spriet LL. Internal physiological load measured using training impulse in varsity men's and women's ice hockey players between game periods. J Strength Cond Res. 2021;35(10):2824-2832. https://doi.org/10.1519/JSC.0000000000004120 Read in abstract form only, 2026-10-05.
- Bigg JL, Gamble ASD, Spriet LL. Internal load of male varsity ice hockey players during training and games throughout an entire season. Int J Sports Physiol Perform. 2022;17(2):286-295. https://doi.org/10.1123/ijspp.2021-0089 Read in abstract form only, 2026-10-05.
- Daily Faceoff. Seravalli F. NHLPA reminds players of their right to control or destroy wearable tech data. 2024-04-30. https://www.dailyfaceoff.com/news/nhlpa-reminds-players-of-their-right-to-control-or-destroy-wearable-tech-data Read on 2026-10-05. Not peer reviewed. Quotes an NHL Players' Association spokesperson that wearable use is voluntary and covered by an agreement separate from the collective bargaining agreement.
- Douglas AS, Kennedy CR. Tracking in-match movement demands using local positioning system in world-class men's ice hockey. J Strength Cond Res. 2020;34(3):639-646. https://doi.org/10.1519/JSC.0000000000003414 Read in abstract form only, 2026-10-05.
- Epp-Stobbe A, Tsai M-C, Klimstra MD. Comparison of imputation methods for missing rate of perceived exertion data in rugby. Mach Learn Knowl Extr. 2022;4(4):827-838. https://doi.org/10.3390/make4040041 Read in abstract form only, 2026-10-05.
- Griffin A, Kenny IC, Comyns TM, Purtill H, Tiernan C, O'Shaughnessy E, Lyons M. Training load monitoring in team sports: a practical approach to addressing missing data. J Sports Sci. 2021;39(19):2161-2171. https://doi.org/10.1080/02640414.2021.1923205 Read in abstract form only, 2026-10-05.
- Lignell E, Fransson D, Krustrup P, Mohr M. Analysis of high-intensity skating in top-class ice hockey match-play in relation to training status and muscle damage. J Strength Cond Res. 2018;32(5):1303-1310. https://doi.org/10.1519/JSC.0000000000001999 Read in abstract form only, 2026-10-05.
- Nightingale S, Hughes J, De Ste Croix M, Pfeifer C. Practice and match load characteristics of elite men's ice hockey. International Journal of Strength and Conditioning. 2024;4(1). The DOI 10.47206/ijsc.v4i1.379 did not resolve on 2026-10-05. Full text read at https://eprints.glos.ac.uk/14636/ on 2026-10-05.
- Rago V, Muschinsky A, Deylami K, Vigh-Larsen JF, Mohr M. Game demands of a professional ice hockey team with special emphasis on fatigue development and playing position. J Hum Kinet. 2022;84:195-205. https://doi.org/10.2478/hukin-2022-000078 Full text read on 2026-10-05.
- Ulmer JG, Tomkinson GR, Short S, Short M, Fitzgerald JS. Test-retest reliability of TRIMP in collegiate ice hockey players. Biol Sport. 2019;36(2):191-194. https://doi.org/10.5114/biolsport.2019.84670 Read in abstract form only, 2026-10-05.
- Van Iterson EH, Fitzgerald JS, Dietz CC, Snyder EM, Peterson BJ. Reliability of triaxial accelerometry for measuring load in men's collegiate ice hockey. J Strength Cond Res. 2017;31(5):1305-1312. https://doi.org/10.1519/JSC.0000000000001611 Read in abstract form only, 2026-10-05.
