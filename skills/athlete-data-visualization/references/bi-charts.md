# Charts in Power BI and Tableau

Last checked: 2026-10-02

## What the problem is

Power BI and Tableau draw a chart from whatever the data model gives them. Their defaults can break the rules of this skill without a warning: a line joins across a missing week, a sum stands in for a mean, a band has no edge, or a palette carries meaning in color alone.

## Rule

Build every chart with the rules in the other reference files of this skill. Only the menu steps change. This file gives the steps for these charts:

- One athlete against a baseline and its noise band.
- The change interval and the smallest worthwhile change zone.
- Squad small multiples.
- The squad dot plot of "who moved" and the heatmap of athletes by days.
- Relationships: within-athlete and between-athlete scatter plots, lag panels, and the paired limb chart.
- Color-blind-safe palettes, direct labels, and alt text.

Both tools assume the model in the `ams-data-setup` skill's `power-bi.md` and `tableau.md` references, if that skill is installed: a long `measures` table, an `athletes` table, a `reliability` table with each measure's TE, and a marked `dates` table in Power BI or a calendar scaffold in Tableau.

### Build the noise band measures

Every band in this file uses `baseline mean ± 1.96 × TE × √(1 + 1/n)`. Take TE from a test-retest study, never from the athlete's own values. The 95 percent level is a choice. Hopkins (2017) uses the same TE × √(1 + 1/n) error for a change from the mean of several tests.

In Power BI, use these DAX measures. `Baseline mean (cm)` and `Baseline n` come from the baseline measures in the `monitoring-statistics` skill, or from a fixed baseline period:

```text
TE (cm) =
LOOKUPVALUE ( reliability[te], reliability[measure_name], "cmj_jump_height" )

Noise half-width (cm) =
VAR te = [TE (cm)]
VAR n = [Baseline n]
RETURN IF ( NOT ISBLANK ( te ) && te > 0 && n >= 1, 1.96 * te * SQRT ( 1 + 1 / n ) )

Band lower (cm) =
VAR m = [Baseline mean (cm)]
VAR h = [Noise half-width (cm)]
RETURN IF ( NOT ISBLANK ( m ) && NOT ISBLANK ( h ), m - h )

Band upper (cm) =
VAR m = [Baseline mean (cm)]
VAR h = [Noise half-width (cm)]
RETURN IF ( NOT ISBLANK ( m ) && NOT ISBLANK ( h ), m + h )

Outside band (cm) =
VAR x = [Test value (cm)]
VAR lo = [Band lower (cm)]
VAR hi = [Band upper (cm)]
RETURN IF ( NOT ISBLANK ( x ) && NOT ISBLANK ( lo ) && ( x < lo || x > hi ), x )
```

In Tableau, use these calculations, with `[Baseline mean (cm)]` and `[Baseline n]` from the same baseline rules:

```text
TE (cm) (aggregate of a FIXED LOD):
MIN({ FIXED : MIN(IF [measure_name (reliability)] = "cmj_jump_height" THEN [te] END) })

Noise half-width (cm):
IF ISNULL([TE (cm)]) OR [TE (cm)] <= 0 OR ISNULL([Baseline n]) OR [Baseline n] < 1 THEN NULL
ELSE 1.96 * [TE (cm)] * SQRT(1 + 1 / [Baseline n])
END

Band lower (cm):  [Baseline mean (cm)] - [Noise half-width (cm)]
Band upper (cm):  [Baseline mean (cm)] + [Noise half-width (cm)]

Band reading:
IF ISNULL([Test value (cm)]) OR ISNULL([Band lower (cm)]) THEN NULL
ELSEIF [Test value (cm)] < [Band lower (cm)] OR [Test value (cm)] > [Band upper (cm)] THEN "outside band"
ELSE "inside band"
END
```

When TE comes from few athletes, replace 1.96 with the t value from the TE study. DAX has `T.INV.2T ( 0.05, df )`. Tableau has no t-distribution function, so store the t value in the `reliability` table.

The Tableau `TE (cm)` picks the CMJ row of `reliability` itself. A plain `MIN([te])` would return the smallest TE of every measure the athlete has rows for, because the view does not filter `measure_name`.

If the user has no TE, draw no band and no flags, and say why.

Choose the time axis from how often the measure is taken:

- For a daily measure, such as a wellness answer, use every calendar day on the axis. A missing day then shows as a gap.
- For a test taken weekly or less often, use the test occasion or the week on the axis, not every calendar day. On a daily axis, 6 of 7 days are blank, so each test shows as a dot with no line. Mark a missed test occasion as a gap.

### Chart one athlete against a baseline band

In Power BI, follow these steps:

1. Add a line chart. Put `dates[Date]` on the x-axis, and set the x-axis **Type** to **Categorical**.
2. Turn on **Show items with no data** for the date field. Power BI joins points across missing values on a continuous axis. On a categorical axis with this option on, a missing test shows as a gap.
3. Put `Test value (cm)`, `Baseline mean (cm)`, and `Outside band (cm)` on the y-axis.
4. Under **Lines**, set `Test value (cm)` to a dark color from the palette below, `Baseline mean (cm)` to a thin `#767676` line, and `Outside band (cm)` to markers only, with a hollow diamond.
5. In the **Analytics** pane, add **Error bars** to `Baseline mean (cm)`. Set the upper bound to `Band upper (cm)` and the lower bound to `Band lower (cm)`. Under **Error band**, show both the fill and the line. Set the fill to `#E8E8E8` and the line to `#767676`, so the band edges reach 3:1 contrast.
6. Turn on data labels for `Outside band (cm)` only, and add the unit to the label format.
7. Turn on **Series labels**, so each line is named at its end, instead of a legend.
8. Add a text box under the chart with the formula, the TE and its source, `n`, the multiplier, and the assumptions.

In Tableau, follow these steps:

1. Put the scaffold `date` on Columns as a continuous exact date, and `Test value (cm)` on Rows. Set the mark type to **Line** and add circle markers.
2. Select **Format**, then the **Pane** tab. Under **Special Values**, set **Marks** to **Hide (Break Lines)**, so a missing test shows as a gap.
3. Put `Band lower (cm)` and `Band upper (cm)` on Detail.
4. For a fixed baseline, open the **Analytics** pane and drag **Reference Band** to the pane. Set **Band From** to the minimum of `Band lower (cm)` and **Band To** to the maximum of `Band upper (cm)`, with scope **Per Pane**. Fill it `#E8E8E8`. Add a reference line at each edge in `#767676`.
5. For a rolling baseline, the band changes each day, so a reference band cannot draw it. Add a second copy of `Band lower (cm)` to Rows, make it a dual axis, set its mark type to **Gantt Bar**, and set its size to `[Band upper (cm)] - [Band lower (cm)]`. Right-click the second axis and select **Synchronize Axis**, then hide its header. The chart then shows one y-axis, as this skill requires.
6. Put `Band reading` on Shape. Use a hollow diamond for `outside band`. Label those marks with the value and unit.

### Chart a change interval and the SWC zone

The change interval is `change ± 1.96 × TE × √(1 + 1/n)`, the same half-width as the noise band. Read each change against both the interval and the SWC zone, as the uncertainty reference says.

In Power BI, error bars attach to bar, column, line, and combo charts, not to scatter charts. Use a line chart with markers only:

1. Put `athletes[athlete_id]` on the x-axis, as a categorical axis, sorted by `Change (cm)`.
2. Put `Change (cm)` on the y-axis. Set the line width to 0 or the line color to the background, and turn on markers.
3. Add **Error bars** to `Change (cm)`, with `Lower (cm)` and `Upper (cm)` from the `monitoring-statistics` skill as the bounds. Show the error bar lines, not the band.
4. Add three measures: `Zero = 0`, `SWC lower = - [SWC (cm)]`, and `SWC upper = [SWC (cm)]`. Add `Zero` as a second series. Add an error band to it with `SWC lower` and `SWC upper` as the bounds, a `#E8E8E8` fill, and a `#767676` edge. This draws the SWC zone around zero.
5. Write the reading in words in a data label or a table next to the chart.

This layout puts athletes across the bottom and change up the side. The reading rules do not depend on the direction.

In Tableau, follow these steps:

1. Put `athlete_id` on Rows, sorted by `Change (cm)`, and `Change (cm)` on Columns. Set the mark type to **Circle**.
2. Add `Lower (cm)` to Columns as a dual axis with mark type **Gantt Bar** and size `[Upper (cm)] - [Lower (cm)]`. Synchronize the axes and hide the second header.
3. Make `SWC lower (cm)` as `-[SWC (cm)]`, and put it and `SWC (cm)` on Detail. Drag **Reference Band** to the table. Set **Band From** to the minimum of `SWC lower (cm)` and **Band To** to the maximum of `SWC (cm)`, with scope **Entire Table**. Fill it `#E8E8E8`, and add reference lines at the edges in `#767676`.
4. Put the reading, such as `larger than measurement error; may or may not be worthwhile`, on Label or in a text column.

### Draw squad small multiples

Give every panel the same x-axis and y-axis. Order panels by roster or position group, not by score. Split by position group beyond about 20 panels. Keep that limit for a laptop screen or a printed page. For a report read on a phone, use the squad dot plot below instead of small multiples. The evidence on panel numbers comes from screens of at least 9.4 × 6.6 inches, so it does not cover phones. [squad-views.md](squad-views.md) gives the study.

In Power BI, use the line chart from the single-athlete steps and put `athletes[athlete_id]` in the **Small multiples** well. **Shared y-axis** is on by default. Leave it on. Microsoft lists trend lines and forecasting as not available in small multiples. Its page does not mention error bars, so check that the band draws in every panel before you share the report. The same page says **Show items with no data** may not behave as expected in small multiples. Remove one week for one athlete and check that the gap still shows before you rely on it. Small multiples also come only for bar, column, line, and area charts, not for scatter charts.

In Tableau, put `athlete_id` on Rows, or on Rows and Columns for a grid, with the time-series chart in each pane. Keep the axis ranges uniform, which is the default. Set the reference band scope to **Per Pane**, so each athlete gets their own band. Sort `athlete_id` by a roster order field.

### Draw the squad dot plot and the heatmap

For "who moved", use the change interval chart above, sorted by change, with the note `Sorted by change, not by ability`. Keep athletes with no test as rows labeled `no test`. Put `20 of 22 tested` in the title, and print the number of flags expected by chance next to the number found.

To highlight one athlete against the squad:

- In Power BI, put `athlete_id` in the line chart legend, then under **Lines**, use **Apply settings to** to set each teammate to light gray and the athlete of interest to one strong color with a thicker line. For a large squad, show only the athlete and the squad median, with the squad range as an error band from the squad minimum to the squad maximum.
- In Tableau, make a string parameter `Focus athlete` and this calculation, then put it on Color and on Detail:

```text
Highlight:
IIF([athlete_id] = [Focus athlete], [athlete_id], "Squad")
```

Set `Squad` to light gray and the focus athlete to one strong color. Show teammates' identifiable data in coach views only.

For a heatmap of athletes by days, use bins with stated edges, and keep missing days different from rest days. The bin edges below are placeholders. Take them from the user, and print them in the color key.

In Power BI, use a matrix with athletes on Rows and `dates[Date]` on Columns. Turn on **Show items with no data** for both. Add a measure that returns a color, then set **Background color** to **Field value** based on it:

```text
Load cell color =
VAR x = [Daily load (AU)]
RETURN
    SWITCH (
        TRUE (),
        ISBLANK ( x ), "#BDBDBD",
        x = 0, "#EFF3FF",
        x < <edge 1>, "#C6DBEF",
        x < <edge 2>, "#9ECAE1",
        x < <edge 3>, "#6BAED6",
        x < <edge 4>, "#4292C6",
        x < <edge 5>, "#2171B5",
        "#084594"
    )
```

Print `0` in rest-day cells and `no data` in missing cells, so the meaning is not in color alone.

In Tableau, put `athlete_id` on Rows and the scaffold `date` as a discrete day on Columns, with mark type **Square**. Put this calculation on Color, and assign the same colors by hand:

```text
Load bin:
IF ISNULL([Daily load (AU)]) THEN "no data"
ELSEIF [Daily load (AU)] = 0 THEN "rest (0)"
ELSEIF [Daily load (AU)] < <edge 1> THEN "above 0 to below <edge 1>"
ELSE "<edge 1> and above"
END
```

Extend the bins to match the Power BI version. Put the value on Label for the cells you discuss.

For change from baseline, use a diverging scale with a neutral midpoint at 0, such as ColorBrewer `PuOr` below.

### Chart relationships

Decide whether the question is between athletes or within athletes. Count athletes, not rows, in `n`.

For a between-athlete chart, plot one point per athlete:

- In Power BI, use a scatter chart with `athletes[athlete_id]` in **Values** and two measures that average each athlete's values on the axes.
- In Tableau, put `athlete_id` on Detail and the two averages on Rows and Columns.

For a within-athlete chart, plot each value minus that athlete's own mean:

- In Power BI, add calculated columns to a pivoted athlete-day table, for example `load_centered = athlete_day[load_au] - CALCULATE ( AVERAGE ( athlete_day[load_au] ), ALLEXCEPT ( athlete_day, athlete_day[athlete_id] ) )`. A calculated column fits here because the athlete mean does not change with slicers. Wrap it in `IF ( NOT ISBLANK ( athlete_day[load_au] ), ... )`, so a missing day stays blank.
- In Tableau, use `[load_au] - { FIXED [athlete_id] : AVG([load_au]) }` as a row-level calculation, with `IF NOT ISNULL([load_au]) THEN ... END` around it.

For one panel per athlete, Tableau puts `athlete_id` on Rows or Columns with shared axes. Power BI small multiples do not support scatter charts, so use the centered chart, or one scatter chart with an athlete slicer.

For a lag, build it inside each athlete on a complete daily calendar, with rest days as 0 and missing days blank:

- In Power BI, use `Load 2 days earlier = VAR d = MAX ( dates[Date] ) RETURN CALCULATE ( [Daily load (AU)], REMOVEFILTERS ( dates ), dates[Date] = d - 2 )`. That counts calendar days, not rows.
- In Tableau, use `LOOKUP([Daily load (AU)], -2)` on the scaffold, with **Compute Using** set to the date and `athlete_id` unchecked.

For the paired limb chart, put one row per athlete with left and right on one axis:

- In Power BI, use a line chart with markers only, athletes on a categorical axis, and `Left value` and `Right value` from the `limb-symmetry` skill as two series with different marker shapes. Join them with error bars on `Left value`, with these bounds. Each one is blank when a limb is missing, so no bar is drawn to 0:

```text
Limb lower =
VAR l = [Left value]
VAR r = [Right value]
RETURN IF ( NOT ISBLANK ( l ) && NOT ISBLANK ( r ), IF ( l < r, l, r ) )

Limb upper =
VAR l = [Left value]
VAR r = [Right value]
RETURN IF ( NOT ISBLANK ( l ) && NOT ISBLANK ( r ), IF ( l < r, r, l ) )
```

- In Tableau, put `athlete_id` on Rows. Put `Measure Values` on Columns, filtered to `Left value` and `Right value` from the `limb-symmetry` skill, and `Measure Names` on Shape. Duplicate `Measure Values` as a dual axis with mark type **Line** and `Measure Names` on Path, so a line joins each athlete's two points. Synchronize the axes and hide the second header. Do not put the raw `value` field on the view, because its default `SUM` adds trials and measures.

Print the difference and its unit at the end of each row, and write `beyond band` in text, not only in color.

### Set color-blind-safe palettes

Use Okabe-Ito colors for groups, ColorBrewer `Blues` for amounts, and ColorBrewer `PuOr` for change. On white, use blue, vermillion, bluish green, and reddish purple for lines and markers. Use sky blue, orange, and yellow only for fills with a dark outline.

In Power BI Desktop, save this theme as a JSON file, then on the **Design** ribbon select **Import theme**. Menus differ between versions. Microsoft's report themes page names the current path:

```json
{
  "name": "Okabe-Ito, contrast order",
  "dataColors": ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#000000", "#56B4E9", "#E69F00", "#F0E442"],
  "background": "#FFFFFF",
  "foreground": "#000000"
}
```

Series take theme colors in the order they appear in a visual. Set the color of an important series by hand, so it keeps the same color on every chart. Give each series its own marker shape under **Markers**, because Microsoft's accessibility guidance says not to use color as the only carrier of meaning.

In Tableau, add these palettes to `Preferences.tps` in the `My Tableau Repository` folder, then restart Tableau:

```xml
<?xml version='1.0'?>
<workbook>
  <preferences>
    <color-palette name="Okabe-Ito, contrast order" type="regular">
      <color>#0072B2</color>
      <color>#D55E00</color>
      <color>#009E73</color>
      <color>#CC79A7</color>
      <color>#000000</color>
      <color>#56B4E9</color>
      <color>#E69F00</color>
      <color>#F0E442</color>
    </color-palette>
    <color-palette name="ColorBrewer Blues 7" type="ordered-sequential">
      <color>#EFF3FF</color>
      <color>#C6DBEF</color>
      <color>#9ECAE1</color>
      <color>#6BAED6</color>
      <color>#4292C6</color>
      <color>#2171B5</color>
      <color>#084594</color>
    </color-palette>
    <color-palette name="ColorBrewer PuOr 7" type="ordered-diverging">
      <color>#B35806</color>
      <color>#F1A340</color>
      <color>#FEE0B6</color>
      <color>#F7F7F7</color>
      <color>#D8DAEB</color>
      <color>#998EC3</color>
      <color>#542788</color>
    </color-palette>
  </preferences>
</workbook>
```

Tableau Help suggests its built-in **Color Blind** palette for discrete fields. It is not the Okabe-Ito palette that this skill names. If you use it, check each color's contrast on white with the WCAG formula first. Put `Band reading` or a group field on Shape as well as Color.

### Label directly and write alt text

Name each line at its end, and keep label text black or dark gray:

- In Power BI, turn on **Series labels** for line charts.
- In Tableau, put the athlete or series name on Label, and set **Label** to show at the line end.

Write alt text with the pattern in the color and accessibility reference: chart type, measure and unit, who, date range, and the main finding. Put a longer description or a table near the chart:

- In Power BI, select the visual, then the **Format** section, expand **General**, and fill in **Alt Text**. The box holds 250 characters, so put the long description in a text box or a table near the chart. Alt text can come from a measure, so it can name the athlete and dates shown. Readers can press **Alt+Shift+F11** to read the values as a table.
- In Tableau, edit the title and the caption, and set the alt text, as Tableau Help suggests. Users can also open **View Data** with the keyboard to read the values.

## Common mistakes

These are the mistakes AI tools and BI users make most often with these charts:

- Leaving the date axis continuous in Power BI. The line joins across a missing test, which draws a change no test measured.
- Leaving null marks at their default in Tableau. Set **Hide (Break Lines)**, and use the scaffold so missing days exist as marks.
- Putting `value` on a chart with the default `SUM`. Use named measures that pick one trial summary.
- Drawing the band with a light fill only. Add `#767676` edges or label the edge values.
- Using a dual axis that shows two scales. Synchronize the axes and hide the second header, or use separate panels.
- Turning on independent y-axes in small multiples. A 3 cm change then looks different in each panel.
- Ordering panels, rows, or colors by score. Use roster order, or change from each athlete's own baseline with the band shown.
- Using a red, amber, and green conditional format for athlete status. Use the palettes above, with a text label in each cell.
- Hiding athletes with no data. Turn on **Show items with no data** in Power BI, and use a left join from the roster in Tableau.

## Example request

> Build me a Power BI page that shows each athlete's weekly jump height against their own baseline, with a noise band, and a squad view of who changed this week.

## Check the result

Run these checks before you share a chart:

- Remove one week of data for one athlete. Confirm the line breaks there and does not drop to 0.
- Confirm the band edges equal `baseline mean ± 1.96 × TE × √(1 + 1/n)` for one athlete, computed by hand.
- Confirm every small multiple panel has the same y-axis range.
- Confirm the number of athletes in the title matches the roster, and that athletes with no test are listed.
- Confirm every color that carries meaning also has a shape or a label.
- Read the alt text aloud. Confirm it names the chart type, measure, unit, who, date range, and main finding.

## Sources

These pages support the steps in this file. Each was read on 2026-10-02:

- Power BI error bars and the error band on line charts; constant lines: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-analytics-pane
- Power BI line charts: categorical and continuous axes, gaps, markers, series labels, and small multiples axes: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-line-chart
- Power BI small multiples, supported visuals, and unavailable features: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples
- Power BI **Show items with no data**: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-show-items-no-data
- Power BI conditional formatting by field value with hex codes, and empty values in gradients: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting
- Power BI report themes and `dataColors`: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes
- Power BI accessible report design, contrast, and marker shapes: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- DAX `T.INV.2T`: https://learn.microsoft.com/en-us/dax/t-inv-2t-function-dax
- Tableau reference lines, bands, and distributions: https://help.tableau.com/current/pro/desktop/en-us/reference_lines.htm
- Tableau null values in continuous fields, under **Format null values**: https://help.tableau.com/current/pro/desktop/en-us/formatting_specific_numbers.htm
- Tableau dual axes and synchronized axes: https://help.tableau.com/current/pro/desktop/en-us/multiple_measures.htm
- Tableau custom color palettes in `Preferences.tps`: https://help.tableau.com/current/pro/desktop/en-us/formatting_create_custom_colors.htm
- Tableau accessibility guidance, the Color Blind palette, contrast, alt text, and View Data: https://help.tableau.com/current/pro/desktop/en-us/accessibility_create_view.htm
- Tableau table calculation functions, including `LOOKUP`: https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm
- ColorBrewer `Blues` and `PuOr` 7-class hex codes, from the ColorBrewer export file: https://github.com/axismaps/colorbrewer
