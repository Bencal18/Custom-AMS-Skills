# Recovery questionnaires

Last checked: 2026-10-07

## What it measures

A recovery questionnaire asks athletes how recovered, tired, or in what mood they feel, and turns the answers into a score. This file covers the scoring of four named questionnaires:

- Hooper index: four ratings of sleep quality, stress, fatigue, and muscle soreness, added into one total (Hooper and Mackinnon, 1995).
- Total Quality Recovery (TQR): one rating of overall recovery (Kenttä and Hassmén, 1998).
- Perceived Recovery Status (PRS): one rating of how recovered the athlete feels (Laurent et al., 2011).
- Brief Assessment of Mood (BAM): six mood ratings, added into a total mood disturbance score (Shearer et al., 2015).

Questionnaires are common in practice:

- 68% of 41 high-level football clubs monitored players' responses to training with questionnaires (Akenhead and Nassis, 2016).
- In a survey of high performance coaching and sport science staff, 84% of respondents (55% of 100 invited) named self-report questionnaires among their methods for monitoring fatigue and recovery (Taylor et al., 2012). The abstract says most practice rested on experience rather than published protocols.

The abstracts of these surveys do not say which named questionnaires, if any, the respondents used.

Read these limits before you use the scores:

- Most daily wellness forms use single items, and the single items most used in sport have not been validated. [wellness-z-score.md](wellness-z-score.md) covers this. TQR and PRS are single items.
- A score describes how the athlete says they feel. It does not identify illness, injury, or a training problem. Use it to start a conversation with the athlete.
- Scores from two questionnaires are not interchangeable. A TQR of 13 and a PRS of 6 are on different scales.

This file leaves out the Recovery-Stress Questionnaire for Athletes (RESTQ-Sport). Its versions and scoring are documented in a commercial user manual (Kellmann and Kallus, 2025). This file does not reproduce or score it. Use that manual.

### Use the item wording

We did not find a license statement for the item wording of any of the four questionnaires. This file describes each scale, its range, its direction, and its end labels as published studies print them. It does not copy any full form. Get the form from the original paper or its authors.

We could not read the full text of any of the four original papers. The scale ranges and directions below come from later peer-reviewed studies that describe each scale and cite the original. The source for each is named.

## Formula

### Hooper index

```text
hooper_index = sleep + stress + fatigue + soreness
```

Define every term in the formula:

- `sleep`, `stress`, `fatigue`, `soreness`: four ratings, each on a 7-point scale from 1 to 7. No unit.
- `hooper_index`: the sum, from 4 to 28. No unit beyond points (studies write it as arbitrary units).

Direction, as later studies describe it:

- Stress, fatigue, and muscle soreness run from 1, very, very low, to 7, very, very high (Douchet et al., 2024; Juillard et al., 2024).
- Sleep quality runs from 1, very, very good, to 7, very, very bad, in the same two studies.
- On that form, 7 is the worst answer for every item, and a higher index means the athlete reports feeling worse.

Some studies print the sleep item the other way round. In Perazzetti et al. (2025), sleep runs from 1, very, very bad, to 7, very, very good, and the four ratings are still added. In Silva et al. (2022), the text describes sleep as 1 very, very bad to 7 very, very good, but the table prints 1 as very, very good. Check the direction of every item on the user's own form before you add them.

If the sleep item runs from bad to good on the user's form, flip it before you add: `sleep_flipped = 8 − sleep`. Name the flip with the result.

### Total quality recovery (TQR)

```text
tqr = the athlete's single rating
```

Read the TQR scale this way:

- Range: 6 to 20. Later studies describe 6 as very, very poor recovery and 20 as very, very good recovery (Selmi et al., 2025; Dutra et al., 2026). A higher score means better reported recovery.
- Kenttä and Hassmén (1998) built the TQR scale around the scale used for ratings of perceived exertion, and paired it with RPE to set recovery against training.
- A 0 to 10 version is also in use. Pino-Mulero et al. (2025) describe TQR from 0, very, very poor recovery, to 10, very, very good recovery. Name the version. Do not mix the two in one series.

### Perceived recovery status (PRS)

```text
prs = the athlete's single rating
```

Read the PRS scale this way:

- Range: 0 to 10. Later studies describe 0 as very poorly recovered and extremely tired, and 10 as very well recovered and highly energetic (Delp et al., 2023; de Sousa Neto et al., 2022). A higher score means better reported recovery.
- Laurent et al. (2011) collected the rating after a warm-up and before each sprint session, and found a moderate negative correlation (r = −0.63) between PRS and change in sprint performance in 16 adults.
- Some forms allow half points, such as 4.5 (Bauer et al., 2024). Ask the user whether theirs does.

### Brief assessment of mood (BAM)

```text
bam_tmd = anxiety + depression + anger + fatigue + confusion + vigour_inverted
vigour_inverted = (lowest point + highest point) − vigour
```

Read the BAM scale this way:

- Items: six, one for each mood factor: anxiety, depression, confusion, anger, vigour, and fatigue (Lipinski et al., 2025). The BAM is a short version of the Profile of Mood States and takes less than 30 seconds (Shearer et al., 2015).
- Response scale: 5 points of intensity, answered for how the athlete feels right now (Lipinski et al., 2025).
- `bam_tmd`: BAM total mood disturbance, the sum of the six items after inverting vigour (Lipinski et al., 2025). A higher score means more reported mood disturbance.
- Number on each point: we could not confirm whether the original form numbers the 5 points 0 to 4 or 1 to 5. The total changes with the numbering: 0 to 24, or 6 to 30. Check the user's form, and name the numbering with the result.
- Energy index: Shearer et al. (2015) also report an energy index from the BAM. We could not confirm its formula, so this file does not calculate it.
- BAM+: an adapted version. Apweiler et al. (2018) list 10 items, each marked on a 100 mm visual analog scale, with sleep and confidence among them. It is a different scale. Do not mix BAM and BAM+ scores.

### Trend the scores

Trend each score against the athlete's own usual scores with the z-score method in [wellness-z-score.md](wellness-z-score.md#formula). Use the total-score variant for the Hooper index and the BAM, and the single-item rules for TQR and PRS. That file sets the baseline window, the minimum baseline, and the chance-flag rules.

Keep the scale direction visible:

- A higher Hooper index or BAM score is worse. A positive z-score means worse than usual.
- A higher TQR or PRS is better. A negative z-score means worse than usual.
- To combine any of these with other items so that a high number is good, flip them first: `32 − hooper_index` for a 1 to 7 Hooper form, and `(highest total + lowest total) − bam_tmd` for the BAM.

### Calculate it in a spreadsheet

Use one row per athlete per day, and put each questionnaire on its own sheet. These formulas work in Excel and Google Sheets.

For the Hooper index, put sleep, stress, fatigue, and soreness in columns `B` to `E`. If the sleep item runs from bad to good on the form, set cell `H1` to `TRUE`, otherwise `FALSE`:

```text
Complete, F2: =AND(COUNT(B2:E2)=4,MIN(B2:E2)>=1,MAX(B2:E2)<=7)
Hooper, G2:   =IF(NOT(F2),"",IF($H$1,8-B2,B2)+C2+D2+E2)
```

For TQR in column `B`, and PRS in column `C`:

```text
TQR, D2: =IF(AND(ISNUMBER(B2),B2>=6,B2<=20),B2,"")
PRS, E2: =IF(AND(ISNUMBER(C2),C2>=0,C2<=10),C2,"")
```

For the BAM, put anxiety, depression, anger, fatigue, confusion, and vigour in columns `B` to `G`. Put the lowest point in cell `J1` and the highest point in cell `J2`, such as `0` and `4`:

```text
Complete, H2: =AND(COUNT(B2:G2)=6,MIN(B2:G2)>=$J$1,MAX(B2:G2)<=$J$2)
BAM TMD, I2:  =IF(NOT(H2),"",SUM(B2:F2)+($J$1+$J$2-G2))
```

Each formula leaves a blank, a text answer, or an out-of-range answer as a blank score. A plain `=SUM(B2:E2)` adds the answers it finds and treats a blank as 0, so an athlete who skipped one item gets a lower, better-looking Hooper index.

### Calculate it in Python

Use these functions:

```python
import pandas as pd

def hooper_index(df, sleep_runs_bad_to_good=False):
    """df: sleep, stress, fatigue, soreness on a 1-7 form. Returns NaN if any item is missing or out of range."""
    items = df[["sleep", "stress", "fatigue", "soreness"]].apply(pd.to_numeric, errors="coerce")
    if sleep_runs_bad_to_good:
        items["sleep"] = 8 - items["sleep"]
    ok = items.notna().all(axis=1) & items.ge(1).all(axis=1) & items.le(7).all(axis=1)
    return items.sum(axis=1).where(ok)

def single_item(values, low, high):
    """TQR (6, 20), TQR 0-10 version (0, 10), or PRS (0, 10)."""
    v = pd.to_numeric(pd.Series(values), errors="coerce")
    return v.where(v.between(low, high))

def bam_tmd(df, low, high):
    """df: anxiety, depression, anger, bam_fatigue, confusion, vigour. low and high: the form's end points."""
    cols = ["anxiety", "depression", "anger", "bam_fatigue", "confusion", "vigour"]
    items = df[cols].apply(pd.to_numeric, errors="coerce")
    ok = items.notna().all(axis=1) & items.ge(low).all(axis=1) & items.le(high).all(axis=1)
    total = items[cols[:5]].sum(axis=1) + (low + high - items["vigour"])
    return total.where(ok)
```

Then pass each score to the z-score function in [wellness-z-score.md](wellness-z-score.md).

### Calculate it in Power BI and Tableau

These versions follow the spreadsheet rules. A missing or out-of-range item gives a blank score.

Both versions assume one row per athlete per day in a `questionnaires` table, with one column per item. Name the BAM fatigue item `bam_fatigue`, so it does not clash with the Hooper `fatigue` item. In Power BI, add these calculated columns. They are columns because each score uses only its own row:

```text
Hooper index =
VAR s = questionnaires[sleep]
VAR items = { s, questionnaires[stress], questionnaires[fatigue], questionnaires[soreness] }
VAR ok = COUNTROWS ( FILTER ( items, NOT ISBLANK ( [Value] ) && [Value] >= 1 && [Value] <= 7 ) ) = 4
RETURN IF ( ok, s + questionnaires[stress] + questionnaires[fatigue] + questionnaires[soreness] )

TQR score =
VAR v = questionnaires[tqr]
RETURN IF ( NOT ISBLANK ( v ) && v >= 6 && v <= 20, v )

PRS score =
VAR v = questionnaires[prs]
RETURN IF ( NOT ISBLANK ( v ) && v >= 0 && v <= 10, v )

BAM TMD =
VAR lo = 0
VAR hi = 4
VAR items = { questionnaires[anxiety], questionnaires[depression], questionnaires[anger],
              questionnaires[bam_fatigue], questionnaires[confusion], questionnaires[vigour] }
VAR ok = COUNTROWS ( FILTER ( items, NOT ISBLANK ( [Value] ) && [Value] >= lo && [Value] <= hi ) ) = 6
RETURN
    IF ( ok,
        questionnaires[anxiety] + questionnaires[depression] + questionnaires[anger]
            + questionnaires[bam_fatigue] + questionnaires[confusion] + ( lo + hi - questionnaires[vigour] ) )
```

If the sleep item runs from bad to good, change `VAR s = questionnaires[sleep]` to `VAR s = IF ( NOT ISBLANK ( questionnaires[sleep] ), 8 - questionnaires[sleep] )`. Set `lo` and `hi` to the BAM form's end points. A blank compares as 0 in DAX, so the `NOT ISBLANK` tests come first. Without them, a blank PRS would score as 0.

In Tableau, use these row-level calculations:

```text
Hooper index:
IF NOT ISNULL([sleep]) AND NOT ISNULL([stress]) AND NOT ISNULL([fatigue]) AND NOT ISNULL([soreness])
   AND MIN(MIN([sleep], [stress]), MIN([fatigue], [soreness])) >= 1
   AND MAX(MAX([sleep], [stress]), MAX([fatigue], [soreness])) <= 7
THEN [sleep] + [stress] + [fatigue] + [soreness]
END

TQR score:
IF [tqr] >= 6 AND [tqr] <= 20 THEN [tqr] END

PRS score:
IF [prs] >= 0 AND [prs] <= 10 THEN [prs] END

BAM TMD (with a 0 to 4 form):
IF NOT ISNULL([anxiety]) AND NOT ISNULL([depression]) AND NOT ISNULL([anger])
   AND NOT ISNULL([bam_fatigue]) AND NOT ISNULL([confusion]) AND NOT ISNULL([vigour])
   AND MIN(MIN(MIN([anxiety], [depression]), MIN([anger], [bam_fatigue])), MIN([confusion], [vigour])) >= 0
   AND MAX(MAX(MAX([anxiety], [depression]), MAX([anger], [bam_fatigue])), MAX([confusion], [vigour])) <= 4
THEN [anxiety] + [depression] + [anger] + [bam_fatigue] + [confusion] + (0 + 4 - [vigour])
END
```

Replace `[sleep]` with `(8 - [sleep])` in the sum if the sleep item runs from bad to good. In Tableau, a comparison with a null is null, and `IF` treats null as false, so a blank TQR or PRS gives a blank score. Then follow the z-score steps for Power BI and Tableau in [wellness-z-score.md](wellness-z-score.md#calculate-it-in-power-bi-and-tableau), with the score as the value.

## Calculate questionnaire scores

Follow these steps to calculate the scores from raw answers:

1. Ask which questionnaire the form uses, and get one blank copy of the form or its labels.
2. For each item, confirm the range and which end is good. For the BAM, confirm whether the points are numbered 0 to 4 or 1 to 5.
3. Load one row per athlete per day, with one column per item.
4. Mark any answer that is blank, text, or outside the range as missing. Do not fill it.
5. Flip any Hooper item that runs from bad to good, with `8 − answer`.
6. Calculate the score: the Hooper sum, the TQR or PRS rating, or the BAM total with vigour inverted.
7. Leave the score missing if any item is missing.
8. Trend each athlete's score against their own baseline with [wellness-z-score.md](wellness-z-score.md).
9. Report the score with the questionnaire name, the version, the range, the direction, and the item answers beside it.

## Worked example

One athlete's answers on the morning of 2026-09-15:

| Questionnaire | Answers | Score | Range | Higher means |
|---|---|---|---|---|
| Hooper index | Sleep 3, stress 2, fatigue 4, soreness 5 | 3 + 2 + 4 + 5 = 14 | 4 to 28 | Worse |
| TQR, 6 to 20 | 12 | 12 | 6 to 20 | Better |
| PRS | 6 | 6 | 0 to 10 | Better |
| BAM, points numbered 0 to 4 | Anxiety 1, depression 0, anger 0, fatigue 3, confusion 1, vigour 1 | 1 + 0 + 0 + 3 + 1 + (0 + 4 − 1) = 8 | 0 to 24 | Worse |

If the form prints sleep from 1, very, very bad, to 7, very, very good, the same sleep quality is an answer of 5. Flip it: 8 − 5 = 3, and the index is 14 again. Added without the flip, the index is 5 + 2 + 4 + 5 = 16.

Trend the Hooper index. The athlete's 14 previous scores are 10, 11, 9, 10, 12, 10, 11, 10, 9, 11, 10, 12, 10, and 11:

- Baseline mean: 10.43. Baseline SD: 0.94.
- Change: 14 − 10.4286 = 3.57 points.
- z = (14 − 10.4286) ÷ 0.9376 = 3.81. A higher Hooper index is worse, so this is 3.81 SDs worse than usual.
- Flipped first, as `32 − hooper_index`, the same day gives z = −3.81.

Report the four item answers with the total, as [wellness-z-score.md](wellness-z-score.md) requires. Here, soreness of 5 and fatigue of 4 carry most of the index.

## What changes the number

These choices change the score even when the athlete feels the same:

- Sleep direction on the Hooper form. An unflipped sleep item that runs from bad to good turns the worked example's 14 into 16, and a better night into a higher, worse-looking index.
- BAM numbering. The same answers give 8 on a form numbered 0 to 4, and 14 on a form numbered 1 to 5.
- BAM vigour. Adding vigour without inverting it gives 6 instead of 8, so more energy lowers the total, which reads as less disturbance for the wrong reason.
- TQR version. A 6 to 20 form and a 0 to 10 form give different numbers for the same state. Do not join them in one series.
- PRS half points. A form that allows 4.5 changes the step size and the z-scores.
- Missing items. Adding only the answered items gives a lower Hooper index and a lower BAM total.
- Time of day and wording. Collect at the same time each day, with the same wording. A changed form starts a new baseline, as [wellness-z-score.md](wellness-z-score.md#what-changes-the-number) says.

## Units and typical range

All four scores are points with no physical unit.

| Questionnaire | Possible range | Direction | Source |
|---|---|---|---|
| Hooper index | 4 to 28 (four items, 1 to 7) | Higher is worse when every item runs 1 good to 7 bad | Douchet et al., 2024; Juillard et al., 2024 |
| TQR | 6 to 20 | Higher is better | Selmi et al., 2025; Dutra et al., 2026 |
| TQR, 0 to 10 version | 0 to 10 | Higher is better | Pino-Mulero et al., 2025 |
| PRS | 0 to 10 | Higher is better | Delp et al., 2023; de Sousa Neto et al., 2022 |
| BAM total mood disturbance | 0 to 24 or 6 to 30, by the form's numbering | Higher is worse | Lipinski et al., 2025 |

No population norm or flag cut-off from these sources applies across sports. Compare each athlete with their own baseline.

## Data you need

Collect this data:

- Source: a daily form or app with the named questionnaire, and a blank copy of its labels.
- Sampling: one set of answers per athlete per day, at the same time and before training.
- Minimum data: one complete set of answers for a score. For a z-score, the baseline minimum in [wellness-z-score.md](wellness-z-score.md).

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with these scores:

- Adding Hooper items without checking the sleep direction. Published forms differ (Perazzetti et al., 2025; Douchet et al., 2024).
- Reading a higher Hooper index or BAM total as better. Both run the other way from TQR and PRS.
- Adding vigour into the BAM total without inverting it.
- Assuming the BAM numbering. Check whether the form runs 0 to 4 or 1 to 5.
- Treating a blank item as 0. The total looks better than the athlete reported.
- Mixing the 6 to 20 and 0 to 10 TQR versions, or BAM and BAM+ scores, in one series.
- Using a fixed cut-off, such as a TQR or PRS level, as if it were validated. Ask the user which rule they use, and label it as their choice.
- Copying a full questionnaire form into a report or app without permission. Describe the scale, and get the form from its source.
- Treating a low recovery score as a diagnosis. It is the athlete's report. Follow up with the athlete.

## Example request

> Our players fill in the Hooper questionnaire every morning on a 1 to 7 scale. Add up the index and flag anyone who is well above their usual score.

The correct answer asks which end of each item is good, flips any item that runs the other way, leaves incomplete days blank, and trends the index with the z-score method. It shows each item answer beside the index and asks the user for their flag cut-off.

## Check the result

Run these checks:

- Recalculate one score by hand from the item answers.
- Confirm every item's direction and range against the user's form, and that any flipped item is named.
- Confirm no score was calculated from a day with a missing or out-of-range item.
- Confirm every score shows the questionnaire, the version, the range, and the direction.
- Confirm every z-score follows the checks in [wellness-z-score.md](wellness-z-score.md#check-the-result).

## Sources

This file cites these sources:

- Hooper SL, Mackinnon LT. Monitoring overtraining in athletes. Recommendations. Sports Med. 1995;20(5):321-327. https://doi.org/10.2165/00007256-199520050-00003 (searched 2026-10-07). Not read: neither the full text nor an abstract was available to us. Scale details come from the studies below that cite it.
- Kenttä G, Hassmén P. Overtraining and recovery. A conceptual model. Sports Med. 1998;26(1):1-16. https://doi.org/10.2165/00007256-199826010-00001 (abstract, accessed 2026-10-07)
- Laurent CM, Green JM, Bishop PA, Sjökvist J, Schumacker RE, Richardson MT, Curtner-Smith M. A practical approach to monitoring recovery: development of a perceived recovery status scale. J Strength Cond Res. 2011;25(3):620-628. https://doi.org/10.1519/jsc.0b013e3181c69ec6 (abstract, accessed 2026-10-07)
- Shearer DA, Kilduff LP, Finn C, Jones RM, Bracken RM, Mellalieu SD, Owen N, Crewther BT, Cook CJ. Measuring recovery in elite rugby players: the Brief Assessment of Mood, endocrine changes, and power. Res Q Exerc Sport. 2015;86(4):379-386. https://doi.org/10.1080/02701367.2015.1066927 (abstract, accessed 2026-10-07)
- Akenhead R, Nassis GP. Training load and player monitoring in high-level football: current practice and perceptions. Int J Sports Physiol Perform. 2016;11(5):587-593. https://doi.org/10.1123/ijspp.2015-0331 (abstract, accessed 2026-10-07)
- Taylor KL, Chapman DW, Cronin JB, Newton MJ, Gill N. Fatigue monitoring in high performance sport: a survey of current trends. J Aust Strength Cond. 2012;20(1):12-23. No DOI. Abstract read through the SPOLIT database record: https://lida.sport-iat.de/twm/Record/4024682 (abstract, accessed 2026-10-07)
- Douchet T, Paizis C, Carling C, Babault N. Influence of a modified versus a typical microcycle periodization on the weekly external loads and match day readiness in elite academy soccer players. J Hum Kinet. 2024;93:133-144. https://doi.org/10.5114/jhk/182984 (accessed 2026-10-07)
- Juillard E, Douchet T, Paizis C, Babault N. Impact of the menstrual cycle on physical performance and subjective ratings in elite academy women soccer players. Sports. 2024;12(1):16. https://doi.org/10.3390/sports12010016 (accessed 2026-10-07)
- Perazzetti A, Kaçurri A, Gjaka M, Pernigoni M, Lupo C, Tessitore A. Impact of a congested match schedule on internal load, recovery, well-being, and enjoyment in U16 youth water polo players. Sports. 2025;13(9):286. https://doi.org/10.3390/sports13090286 (accessed 2026-10-07)
- Silva RM, Clemente FM, González-Fernández FT, Nobari H, Oliveira R, Silva AF, Cancela-Carral JM. Relationships between internal training intensity and well-being changes in youth football players. Healthcare. 2022;10(10):1814. https://doi.org/10.3390/healthcare10101814 (accessed 2026-10-07)
- Selmi O, Rahmoune MA, Bouassida A, Marsigliante S, Muscella A. Comparative analysis of morning and evening training on performance and well-being in elite soccer players. Physiol Rep. 2025;13(15):e70510. https://doi.org/10.14814/phy2.70510 (accessed 2026-10-07)
- Dutra YM, Mendonça PT, Goodall S, Zagatto AM. Neuromuscular fatigue and perceived fatigability in the hours following a high-intensity endurance running depend on the exercise protocol. Eur J Sport Sci. 2026;26(8):e70176. https://doi.org/10.1002/ejsc.70176 (accessed 2026-10-07)
- Pino-Mulero V, Soriano MA, Giuliano F, González-García J. Effects of a priming session with heavy sled pushes on neuromuscular performance and perceived recovery in soccer players: a crossover design study during competitive microcycles. Biol Sport. 2025;42(1):59-66. https://doi.org/10.5114/biolsport.2025.139082 (accessed 2026-10-07)
- Delp M, Chesbro GA, Pribble BA, Miller RM, Pereira HM, Black CD, Larson RD. Higher rating of perceived exertion and lower perceived recovery following a graded exercise test during menses compared to non-bleeding days in untrained females. Front Physiol. 2023;14:1297242. https://doi.org/10.3389/fphys.2023.1297242 (accessed 2026-10-07)
- de Sousa Neto IV, de Sousa NMF, Neto FR, Falk Neto JH, Tibana RA. Time course of recovery following CrossFit Karen benchmark workout in trained men. Front Physiol. 2022;13:899652. https://doi.org/10.3389/fphys.2022.899652 (accessed 2026-10-07)
- Bauer J, Muehlbauer T, Geiger S, Gruber M. Interaction between the leg recovery test and subjective measures of fatigue in handball players: short-, mid-, and long-term assessment. Front Sports Act Living. 2024;6:1474385. https://doi.org/10.3389/fspor.2024.1474385 (accessed 2026-10-07)
- Lipinski D, Whelan JP, Stiglets BE, Andersland MD, Ginley MK, Pfund RA. The influence of winning and losing gambling experience on mood state and alcohol cravings. J Gambl Stud. 2025;41(2):841-855. https://doi.org/10.1007/s10899-024-10367-7 (accessed 2026-10-07). Cited only for the BAM items and scoring.
- Kellmann M, Kallus KW, editors. The Recovery-Stress Questionnaires: A User Manual. 1st ed. Routledge; 2025. Book, not peer reviewed, no DOI. Publisher page: https://routledge.com/The-Recovery-Stress-Questionnaires-A-User-Manual/Kellmann-Kallus/p/book/9781032620503 (accessed 2026-10-07)
- Apweiler E, Wallace D, Stansfield S, Allerton DM, Brown MA, Stevenson EJ, Clifford T. Pre-bed casein protein supplementation does not enhance acute functional recovery in physically active males and females when exercise is performed in the morning. Sports. 2018;7(1):5. https://doi.org/10.3390/sports7010005 (accessed 2026-10-07)
