# Sprint profile

Last checked: 2026-10-07

## What it measures

A sprint profile describes how fast an athlete gets up to speed and how fast they can run, from one maximal sprint. It has two layers:

- **Acceleration-velocity profile:** maximal sprinting speed (MSS), the time constant tau (τ), and maximal acceleration (MAC). These come straight from the timing data.
- **Force-velocity profile:** theoretical maximal horizontal force (F0), theoretical maximal velocity (V0), maximal horizontal power (Pmax), the slope of the force-velocity line (SFV), the ratio of force (RF), and its decrease with speed (DRF). These add body mass, height, and air resistance to the first layer (Samozino et al., 2016).

Each force-velocity value is a model estimate, not a measured force. The model treats the athlete as one point, the center of mass, and averages over whole steps (Samozino et al., 2016). It shows the athlete's sprint output under the test conditions. It does not diagnose anything, and it does not say what to train.

Practitioners use sprint tests often. Of 67 elite soccer practitioners who tested linear speed, 43 (64%) used a 10 m sprint (Asimakidis et al., 2024). In a review of 14 soccer studies of the sprint force-velocity profile, the results section reports that all 14 used the Samozino method. The abstract says the method was consistently used. 11 of the 14 studies (78.6%) were rated at high risk of bias (Lipčák et al., 2025).

## Formula

The model starts from the speed curve of a maximal sprint from a standstill (Samozino et al., 2016, eq. 1 to 5):

```text
v(t) = MSS × (1 − e^(−t/τ))
d(t) = MSS × (t + τ × e^(−t/τ)) − MSS × τ
a(t) = (MSS / τ) × e^(−t/τ)
MAC  = MSS / τ
```

The force-velocity layer uses these equations (Samozino et al., 2016, eq. 6 to 13):

```text
F_H(t)   = m × a(t) + F_aero(t)
F_aero(t) = k × (v(t) − v_wind)^2
k        = 0.5 × ρ × A_f × C_d,  with C_d = 0.9
ρ        = 1.293 × (P_b / 760) × 273 / (273 + T)
A_f      = 0.2025 × h^0.725 × m^0.425 × 0.266
F_V      = m × g
RF(t)    = 100 × F_H / √(F_H^2 + F_V^2)
P(t)     = F_H(t) × v(t)
F0, SFV  = intercept and slope of the straight line fitted to F_H against v
V0       = −F0 / SFV
Pmax     = F0 × V0 / 4
DRF      = slope of the straight line fitted to RF against v, for t > 0.3 s
```

Define every term in the formula:

- `t`: time since the athlete started to push, in seconds (s). The model needs `t = 0` at the first movement. See "What changes the number".
- `v(t)`: horizontal speed of the center of mass, in meters per second (m/s).
- `d(t)`: distance covered, in meters (m).
- `a(t)`: horizontal acceleration, in meters per second squared (m/s²).
- `MSS`: maximal sprinting speed, the speed the curve levels off at, in m/s.
- `τ` (tau): the time constant, in s. It is the time the model takes to reach 63.2% of MSS (Jovanović and Vescovi, 2022).
- `MAC`: maximal acceleration, the model's acceleration at `t = 0`, in m/s² (Jovanović and Vescovi, 2022).
- `m`: body mass, in kilograms (kg), measured on the test day.
- `h`: standing height, in m.
- `F_H`: net horizontal force on the center of mass, averaged over each step, in newtons (N).
- `F_aero`: air resistance, in N.
- `v_wind`: wind speed along the track, in m/s. Use 0 indoors. This skill uses positive for a tailwind and negative for a headwind, as the `shorts` R package does.
- `k`: the athlete's air resistance coefficient, in kg/m.
- `ρ` (rho): air density, in kg/m³. 1.293 kg/m³ is air density at 760 Torr and 0 °C.
- `P_b`: barometric pressure, in Torr (mmHg).
- `T`: air temperature, in degrees Celsius (°C).
- `A_f`: the athlete's frontal area, in square meters (m²), estimated from height and mass.
- `C_d`: drag coefficient, fixed at 0.9.
- `F_V`: vertical force, set equal to body weight. The model assumes almost no vertical acceleration of the center of mass when averaged over a step (Samozino et al., 2016).
- `g`: 9.81 m/s².
- `RF`: ratio of force, the share of the total ground force that points forward, in percent (%).
- `F0`: theoretical maximal horizontal force at zero speed, in N or N/kg.
- `V0`: theoretical maximal velocity at zero force, in m/s.
- `SFV`: slope of the force-velocity line, in N·s/m, or N·s/m/kg when divided by body mass.
- `Pmax`: maximal horizontal power, in watts (W) or W/kg.
- `RFmax`: the highest RF after 0.3 s, in %.
- `DRF`: how fast RF falls as speed rises, in % per m/s (written %·s/m).

Samozino et al. (2016) computed RF and DRF only for `t > 0.3 s`, because the first push lasts about that long. They computed every value every 0.1 s, and they fitted MSS and τ by least squares on distance, eq. 3, with time as the input. They also give Pmax as the top of a curve fitted to power against speed. This skill uses the `F0 × V0 / 4` form, their eq. 13.

### Variants

Choose the variant that fits the data:

| Variant | Use it when | What differs |
|---|---|---|
| Acceleration-velocity profile only (MSS, τ, MAC) | You have no body mass or height, or you want only timing outputs | No force, power, or RF |
| Force-velocity profile with air resistance (Samozino et al., 2016) | You have body mass, height, and air conditions | The full method in this file |
| Force-velocity profile without air resistance | You compute in a BI tool from imported MSS and τ | `F0 = m × MSS / τ`, `V0 = MSS`, `Pmax = m × MSS × MAC / 4`. This is the method's equations with `F_aero = 0`, so the force-velocity line is exactly straight. Label it "no air resistance". |

The no-air-resistance form follows from eq. 5 and 6 with `F_aero = 0`. The `shorts` paper reports `PMAX` in the same form: with MSS 9 m/s and MAC 8 m/s², `PMAX` is 18.0 W/kg, which is 9 × 8 / 4 (Jovanović and Vescovi, 2022). Never mix the two forms in one trend.

### Fit to split times in a spreadsheet

Use this layout on the first sheet, named `Sheet1`. Put split distances in m in `A2:A6` and split times in s in `B2:B6`, after any time correction. Put body mass in kg in `E1`, height in m in `E2`, temperature in °C in `E3`, pressure in Torr in `E4`, and wind in m/s in `E5`.

In Excel, use Solver:

1. Put a first guess for MSS in `H1`, such as `8`, and for τ in `H2`, such as `1`.
2. In `C2`, enter the model distance, and fill it down to `C6`: `=$H$1*(B2+$H$2*EXP(-B2/$H$2))-$H$1*$H$2`
3. In `D2`, enter the residual in m, and fill it down to `D6`: `=A2-C2`
4. In `H3`, enter the sum of squared residuals: `=SUMSQ(D2:D6)`
5. Open **Data**, then **Solver**. Set the objective to `H3`, **To Min**, by changing `H1:H2`.
6. Add the constraints `H1 >= 0.1` and `H2 >= 0.1`, and choose **GRG Nonlinear**.
7. Select **Solve**. `H1` is MSS and `H2` is τ.
8. In `H4`, enter MAC: `=H1/H2`

Google Sheets has no built-in Solver. Use this scan instead. It also works in Excel. For each τ from 0.500 to 2.000 s in steps of 0.001 s, it finds the best MSS exactly, because the model is a straight line in MSS once τ is fixed:

1. In `J2`, enter `=0.5+(ROW()-2)/1000`, and fill it down to `J1502`.
2. In `K2`, enter the best MSS for that τ, and fill it down:
   `=SUMPRODUCT($A$2:$A$6,$B$2:$B$6+J2*EXP(-$B$2:$B$6/J2)-J2)/SUMPRODUCT(($B$2:$B$6+J2*EXP(-$B$2:$B$6/J2)-J2)^2)`
3. In `L2`, enter the sum of squared residuals, and fill it down:
   `=SUMPRODUCT(($A$2:$A$6-K2*($B$2:$B$6+J2*EXP(-$B$2:$B$6/J2)-J2))^2)`
4. In `H6`, enter `=MATCH(MIN(L2:L1502),L2:L1502,0)`.
5. In `H7`, enter τ: `=INDEX(J2:J1502,H6)`. In `H8`, enter MSS: `=INDEX(K2:K1502,H6)`.
6. If τ is 0.500 or 2.000, the best value lies outside the scan. Widen the range and repeat.

In Google Sheets, if `SUMPRODUCT` returns an error on the array arithmetic, wrap the expression in `ARRAYFORMULA`.

Then build the force-velocity table on a new sheet. Put MSS in `B1` and τ in `B2`. Compute `k` in `B3` from the inputs: `=0.5*(1.293*(Sheet1!E4/760)*273/(273+Sheet1!E3))*(0.2025*Sheet1!E2^0.725*Sheet1!E1^0.425*0.266)*0.9`. Then fill these columns down in 0.1 s steps, from 0 s to the last split time rounded to 0.1 s:

| Column | Header | Formula in row 6 |
|---|---|---|
| A | `t_s` | `=(ROW()-6)/10` |
| B | `v_m_s` | `=$B$1*(1-EXP(-A6/$B$2))` |
| C | `a_m_s2` | `=$B$1/$B$2*EXP(-A6/$B$2)` |
| D | `f_aero_N` | `=$B$3*(B6-Sheet1!$E$5)^2` |
| E | `f_h_N` | `=Sheet1!$E$1*C6+D6` |
| F | `p_W` | `=E6*B6` |
| G | `rf_pct` | `=100*E6/SQRT(E6^2+(Sheet1!$E$1*9.81)^2)` |

Use these summary formulas, with the table in rows 6 to 64 for a last split at 5.8 s:

- `F0 (N)`: `=INTERCEPT(E6:E64,B6:B64)`
- `SFV (N·s/m)`: `=SLOPE(E6:E64,B6:B64)`
- `V0 (m/s)`: `=-F0/SFV`, with the two cells above
- `Pmax (W)`: `=F0*V0/4`
- `RFmax (%)`: the RF in the first row after 0.3 s, which is row 10 (0.4 s)
- `DRF (%·s/m)`: `=SLOPE(G10:G64,B10:B64)`

Divide F0, SFV, and Pmax by body mass for the per-kilogram values.

### Fit a radar, laser, or GPS speed trace

For a speed trace, fit speed, not distance. Use this model, where `t0` is the moment the athlete starts to move on the device clock:

```text
v(t) = MSS × (1 − e^(−(t − t0)/τ)),  for t ≥ t0
```

In Excel Solver, change MSS, τ, and `t0` to minimize the sum of squared differences between measured and model speed. Keep samples from just before the start to the top speed. Drop samples after the athlete slows down. The `shorts` package fits the same kind of time correction for radar data (Jovanović and Vescovi, 2022).

GPS gives a speed trace at a lower rate than radar. Clavel et al. (2023) built an acceleration-speed profile from GPS training data in elite youth soccer players. Its outputs, theoretical maximal acceleration (A0) and speed (S0), come from a different method and are not the same numbers as MAC and MSS. Their reliability improved when the data reached 95% of maximal speed or more, and they advise covering 20% to 95% of maximal speed. Do not mix GPS-derived and gate-derived profiles in one trend.

### Calculate it in R and Python

In R, the `shorts` package fits split times, radar or laser traces, and GPS data (Jovanović and Vescovi, 2022). Use this code:

```r
library(shorts)
m1 <- model_timing_gates(
  distance = c(5, 10, 20, 30, 40),
  time = c(1.38, 2.11, 3.40, 4.62, 5.79)
)
m1$parameters      # MSS, MAC, TAU, PMAX
m1$predictions     # observed, predicted, and residual for each split
m_tc <- model_timing_gates_TC(distance = m1$data$distance, time = m1$data$time)
fv <- create_FVP(MSS = m1$parameters$MSS, MAC = m1$parameters$MAC,
                 bodymass = 78, bodyheight = 1.80)
```

The `shorts` package differs from the spreadsheet method in three ways:

- Its timing gate models treat time as the outcome and distance as the input. Jovanović and Vescovi (2022) call that the statistically correct choice. Samozino et al. (2016) fitted distance, as the spreadsheet does. The two can give slightly different MSS and τ from the same splits.
- The package documentation says `create_FVP` modifies the Samozino et al. (2016) method with later work by Samozino and colleagues. F0 and V0 can differ slightly from the regression in this file.
- `get_air_resistance` defaults to 25 °C. Samozino et al. (2016) used 20 °C. Pass the real temperature.

`PMAX` in `m1$parameters` is per kilogram and has no air resistance. It is not the same value as `Pmax` from `create_FVP`.

Use this Python code. It uses the standard library only:

```python
import math

def fit_splits(dist_m, time_s, tc_s=0.0):
    """Least squares on distance (Samozino et al., 2016, eq. 3). Returns MSS, tau."""
    t = [x + tc_s for x in time_s]
    g = lambda ti, tau: ti + tau * math.exp(-ti / tau) - tau
    def mss_sse(tau):
        mss = sum(d * g(ti, tau) for d, ti in zip(dist_m, t)) / sum(g(ti, tau) ** 2 for ti in t)
        return mss, sum((d - mss * g(ti, tau)) ** 2 for d, ti in zip(dist_m, t))
    lo, hi, r = 0.3, 3.0, (math.sqrt(5) - 1) / 2     # golden-section search on tau
    for _ in range(200):
        a, b = hi - r * (hi - lo), lo + r * (hi - lo)
        if mss_sse(a)[1] < mss_sse(b)[1]: hi = b
        else: lo = a
    tau = (lo + hi) / 2
    return mss_sse(tau)[0], tau

def fv_profile(mss, tau, mass_kg, height_m, t_end_s, temp_c=20.0, pb_torr=760.0, wind_m_s=0.0):
    rho = 1.293 * (pb_torr / 760) * 273 / (273 + temp_c)
    af = 0.2025 * height_m ** 0.725 * mass_kg ** 0.425 * 0.266
    k = 0.5 * rho * af * 0.9
    rows = []
    for i in range(int(round(t_end_s / 0.1)) + 1):
        t = i * 0.1
        v = mss * (1 - math.exp(-t / tau))
        fh = mass_kg * (mss / tau) * math.exp(-t / tau) + k * (v - wind_m_s) ** 2
        rf = 100 * fh / math.hypot(fh, mass_kg * 9.81)
        rows.append((t, v, fh, rf))
    def line(x, y):                                   # least squares slope and intercept
        mx, my = sum(x) / len(x), sum(y) / len(y)
        s = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
        return s, my - s * mx
    s_fv, f0 = line([r[1] for r in rows], [r[2] for r in rows])
    v0 = -f0 / s_fv
    late = [r for r in rows if r[0] > 0.3 + 1e-9]     # RF only after 0.3 s
    drf, _ = line([r[1] for r in late], [r[3] for r in late])
    return {"F0_N": f0, "F0_N_kg": f0 / mass_kg, "V0_m_s": v0, "Pmax_W": f0 * v0 / 4,
            "Pmax_W_kg": f0 * v0 / 4 / mass_kg, "SFV_N_s_m_kg": s_fv / mass_kg,
            "RFmax_pct": max(r[3] for r in late), "DRF_pct_s_m": drf}
```

To estimate a time correction in Python, wrap `fit_splits` in a second search over `tc_s` that minimizes the same sum of squares. Estimating a time correction adds a third parameter, so it needs at least 4 splits (Jovanović and Vescovi, 2022).

### Calculate it in Power BI and Tableau

Fit MSS and τ outside the BI tool, in a spreadsheet, R, or Python. A BI tool has no built-in curve fit. Import one MSS and one τ per trial. Then compute MAC and the no-air-resistance values in the BI tool. Label them "no air resistance".

Both versions assume one row per athlete, date, session, measure, and trial in a `measures` table. MSS is `measure_name` `sprint_mss` in `m/s`. τ is `sprint_tau` in `s`. Both come from the same fit of the same trial.

In Power BI, use this DAX measure. It works one trial at a time, as the RSImod measure in the `force-plate` skill does:

```text
Sprint MAC (m/s²) =
MAXX (
    VALUES ( measures[trial_number] ),
    VAR mss =
        CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sprint_mss",
            measures[unit] = "m/s", measures[status] = "ok" )
    VAR tau =
        CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sprint_tau",
            measures[unit] = "s", measures[status] = "ok" )
    RETURN IF ( NOT ISBLANK ( mss ) && NOT ISBLANK ( tau ) && tau > 0, mss / tau )
)

Sprint Pmax, no air resistance (W/kg) =
MAXX (
    VALUES ( measures[trial_number] ),
    VAR mss =
        CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sprint_mss",
            measures[unit] = "m/s", measures[status] = "ok" )
    VAR tau =
        CALCULATE ( MAX ( measures[value] ), measures[measure_name] = "sprint_tau",
            measures[unit] = "s", measures[status] = "ok" )
    RETURN IF ( NOT ISBLANK ( mss ) && NOT ISBLANK ( tau ) && tau > 0, mss * mss / tau / 4 )
)
```

F0 without air resistance, in N/kg, equals MAC. V0 without air resistance equals MSS.

In Tableau, put `athlete_id`, `measure_date`, `session_id`, and `trial_number` on the view. Use these aggregate calculations:

```text
MSS (m/s):
MAX(IF [measure_name] = "sprint_mss" AND [unit] = "m/s" AND [status] = "ok" THEN [value] END)

Tau (s):
MAX(IF [measure_name] = "sprint_tau" AND [unit] = "s" AND [status] = "ok" THEN [value] END)

MAC (m/s²):
IF ISNULL([MSS (m/s)]) OR ISNULL([Tau (s)]) OR [Tau (s)] <= 0 THEN NULL
ELSE [MSS (m/s)] / [Tau (s)] END

Pmax, no air resistance (W/kg):
IF ISNULL([MAC (m/s²)]) THEN NULL ELSE [MSS (m/s)] * [MAC (m/s²)] / 4 END
```

Blanks behave this way in each tool:

- Power BI: the `IF` returns a blank when either value is blank or τ is 0. `MAXX` skips blank trials.
- Tableau: a null MSS or τ gives a null result.

## Calculate the metric

Follow these steps to calculate the profile from raw inputs:

1. Find the split distances in m and the split times in s. Convert yards to meters (× 0.9144) and ms to s.
2. Record how timing started: a gate at the start line, a gate in front of the start line, a pad or touch trigger, or a reaction to a signal.
3. Record the start stance and how far behind the first gate the front foot was.
4. Decide the time correction: none, a fixed value, or an estimated value. Use the same choice at every test.
5. Add the time correction to every split time.
6. Fit MSS and τ by least squares, in a spreadsheet, R, or Python.
7. Compute MAC = MSS / τ.
8. Compute the residual for each split: measured distance minus model distance.
9. Check the residuals, as in "Check the result".
10. Stop at the acceleration-velocity profile if body mass or height is missing.
11. Record body mass in kg and height in m from the test day.
12. Record air temperature, pressure, and wind for an outdoor test. Use 20 °C, 760 Torr, and 0 m/s indoors, and say so.
13. Build the time table from 0 s to the last split time in 0.1 s steps.
14. Compute speed, acceleration, air resistance, horizontal force, power, and RF for each row.
15. Fit a straight line to horizontal force against speed. Take F0, SFV, and V0 from it.
16. Compute Pmax = F0 × V0 / 4.
17. Fit a straight line to RF against speed for rows after 0.3 s. Its slope is DRF.
18. Report MSS, τ, MAC, F0, V0, Pmax, RFmax, and DRF with units, the time correction, and the variant.

## Worked example

This example uses one made-up 40 m sprint. The splits come from a model athlete with MSS 8.50 m/s and τ 1.10 s, with small timing noise added and times rounded to 0.01 s. The athlete started from a stance with the first movement at `t = 0`, so no time correction applies. Every number below came from running the calculation in Python.

| Input | Value |
|---|---|
| Split distances | 5, 10, 20, 30, 40 m |
| Split times | 1.38, 2.11, 3.40, 4.62, 5.79 s |
| Body mass | 78.0 kg |
| Height | 1.80 m |
| Air | 20 °C, 760 Torr, no wind |

Step 1. The least squares fit gives MSS = 8.523 m/s and τ = 1.107 s. The spreadsheet scan gives 8.522 m/s and 1.107 s.

Step 2. MAC = MSS / τ = 7.696 m/s², from the unrounded fit (8.5226 / 1.1074).

Step 3. The residuals, measured minus model distance, are −0.038, 0.051, 0.023, −0.082, and 0.042 m at 5, 10, 20, 30, and 40 m. As times, they are within ±0.01 s of each split.

Step 4. Air density ρ = 1.2047 kg/m³. Frontal area A_f = 0.5254 m². k = 0.5 × 1.2047 × 0.5254 × 0.9 = 0.2849 kg/m.

Step 5. At t = 0.4 s, the table gives v = 2.584 m/s, a = 5.363 m/s², F_aero = 1.90 N, F_H = 78.0 × 5.363 + 1.90 = 420.2 N, and RF = 48.13%.

Step 6. The straight line through F_H against v, over 59 rows from 0 to 5.8 s, gives F0 = 595.0 N (7.63 N/kg) and SFV = −67.5 N·s/m (−0.87 N·s/m/kg).

Step 7. V0 = −F0 / SFV = 595.0 / 67.51 = 8.81 m/s.

Step 8. Pmax = 595.0 × 8.813 / 4 = 1310.9 W (16.81 W/kg).

Step 9. RFmax = 48.13% at 0.4 s. The line through RF against v after 0.3 s gives DRF = −7.94 %·s/m.

Result: MSS 8.52 m/s, τ 1.107 s, MAC 7.70 m/s², F0 7.63 N/kg, V0 8.81 m/s, Pmax 16.81 W/kg, RFmax 48.1%, and DRF −7.94 %·s/m, with no time correction.

Without air resistance, the same fit gives F0 = MAC = 7.70 N/kg, V0 = MSS = 8.52 m/s, and Pmax = 8.523 × 7.696 / 4 = 16.40 W/kg. Do not compare these with the values above.

## What changes the number

These choices change the result even when the athlete's sprint does not change.

The start and the time correction change the result most. The model needs `t = 0` at the first push. A gate at the start line triggers when the body breaks the beam, after the athlete is already moving (Jovanović and Vescovi, 2022). To show the effect, the model athlete above (MSS 8.50 m/s, τ 1.10 s) ran again from 0.5 m behind the first gate. Its splits became 1.07, 1.80, 3.08, 4.29, and 5.48 s. These fits came from Python:

| Time correction | MSS (m/s) | τ (s) | MAC (m/s²) | F0 (N/kg) | Pmax (W/kg) |
|---|---|---|---|---|---|
| Athlete's true values, no correction needed | 8.50 | 1.10 | 7.73 | 7.66 | 16.83 |
| None | 8.17 | 0.605 | 13.50 | 13.44 | 27.94 |
| Fixed +0.3 s | 8.50 | 1.077 | 7.89 | 7.82 | 17.17 |
| Fixed +0.5 s | 8.86 | 1.477 | 6.00 | 5.93 | 13.76 |
| Estimated (0.266 s) | 8.45 | 1.017 | 8.31 | 8.24 | 17.95 |

The first row uses the true MSS and τ with the same air settings, over 0 to 5.8 s.

These results agree with the published simulations and field data:

- With no correction, a flying start underestimates MSS and τ and overestimates MAC and Pmax. The bias grows with the flying distance (Jovanović and Vescovi, 2022).
- Haugen et al. (2019) added 0.5 s to every time when the center of mass was about 0.5 m in front of the start line at the trigger. Too large a correction underestimates power (Jovanović and Vescovi, 2022), as the +0.5 s row shows here.
- No single fixed correction suits every athlete, flying distance, and gate layout (Jovanović and Vescovi, 2022). In this example, +0.3 s came closest. Do not take that as a rule.
- In 116 female soccer players starting 5 cm behind the first beam, the estimated correction averaged 0.25 ± 0.09 s. Without a correction, mean F0 was 11.2 N/kg. With a fixed +0.3 s it was 6.6 N/kg, and with an estimated correction 7.1 N/kg (Vescovi and Jovanović, 2021).
- Start trigger: over 40 m, a hand-release start was 0.17 ± 0.09 s faster than a block start reacting to a gun. A photocell at the start line was 0.27 ± 0.12 s faster, and a foot-release start 0.69 ± 0.11 s faster (Haugen et al., 2012).

Other choices change the result too:

- Gate height. Studies set gates at about hip height so that one body part breaks the beam (Dos'Santos et al., 2019), or at about 1.0 m (Vescovi and Jovanović, 2021). Keep the height the same at every test.
- Body mass. F0 and Pmax in N and W scale with body mass. In the worked example, 83 kg instead of 78 kg raises F0 from 595.0 to 633.3 N and Pmax from 1310.9 to 1393.6 W. The per-kilogram values barely change (7.63 N/kg; 16.79 W/kg). Use body mass from the test day.
- Wind. In the worked example, a 2 m/s headwind with the same splits raises F0 to 7.64 N/kg, V0 to 8.98 m/s, and Pmax to 17.16 W/kg. The athlete had to push harder to run the same times. Record wind outdoors.
- Air temperature. 25 °C instead of 20 °C changes Pmax from 16.81 to 16.80 W/kg in the worked example. The effect is small, but name the value.
- RF start time. RF after 0.3 s gives RFmax 48.13% at 0.4 s. Starting at 0.5 s gives 44.94% and DRF −8.03 %·s/m. Haugen et al. (2019) took RFmax at 0.5 s.
- Fit method. Fitting distance (Samozino et al., 2016) and fitting time (Jovanović and Vescovi, 2022) give slightly different MSS and τ. Use one method.
- Surface and footwear. Test on the same surface in the same footwear. This is good practice, not a published rule.
- Number of splits. A fit needs more splits than parameters: at least 3 for MSS and τ, and at least 4 with an estimated time correction (Jovanović and Vescovi, 2022). Samozino et al. (2016) suggest about 5.
- Sprint length. The athlete must get close to top speed before the last split. Otherwise MSS is a guess beyond the data.

## Units and typical range

Report MSS and V0 in m/s, τ in s, MAC in m/s², F0 in N or N/kg, Pmax in W or W/kg, SFV in N·s/m/kg, RF in %, and DRF in %·s/m. Name the time correction and the air settings.

| Population | Typical range | Source |
|---|---|---|
| Elite or sub-elite male sprinters (n = 9), block start, split times with the trigger delay added from video | MSS 10.05 ± 0.66 m/s; τ 1.24 ± 0.14 s; F0 638 ± 84 N; V0 10.51 ± 0.74 m/s; Pmax 1680 ± 280 W; DRF −6.80 ± 0.74 %·s/m; body mass 76.4 ± 7.1 kg (mean ± SD) | Samozino et al., 2016 |
| High-level female soccer players (n = 116), gates at the start line, 5 cm behind the beam, estimated time correction | MSS 7.77 ± 0.43 m/s; MAC 7.2 ± 0.9 m/s²; τ 1.10 ± 0.16 s; F0 7.1 ± 0.9 N/kg; V0 8.03 ± 0.48 m/s; Pmax 14.2 ± 1.8 W/kg; RFmax 48 ± 3%; DRF −8.2 ± 1.1 %·s/m | Vescovi and Jovanović, 2021 |
| Elite athletes from 23 sports (n = 666), 0.5 s added to every time | Group means of SFV from −0.75 to −1.10 N·s/m/kg in men and −0.80 to −1.15 in women | Haugen et al., 2019 |

Haugen et al. (2019) also computed RFmax at 0.5 s as high as 56% to 57% in world-class male sprinters and 52% to 53% in women, from public split times.

Use these ranges to check that data are plausible, not to rate athletes. Values from another start, time correction, or fit method are not comparable.

To judge a change in one athlete, measure your own typical error for your athletes and setup, as the `monitoring-statistics` skill describes. This file gives no published reliability figure for the sprint profile.

## Data you need

Collect this data:

- Source: timing gates with at least 3 splits (4 for an estimated time correction), or a radar, laser, or GPS speed trace of one maximal sprint.
- Sampling: Samozino et al. (2016) sampled radar at 46.875 Hz, and Morin et al. (2019) used a 100 Hz laser.
- Start: the start stance, the distance from the front foot to the first gate, and the trigger method.
- Athlete: body mass in kg and height in m from the test day, for the force-velocity layer.
- Conditions: indoor or outdoor, surface, footwear, temperature, pressure, and wind.
- Minimum data: one maximal sprint long enough to near top speed. Samozino et al. (2016) suggest two or three sprints, keeping the best.

## Common mistakes

These are the mistakes AI tools and spreadsheets make most often with this metric:

- Fitting gate splits with no thought about the start. A flying start with no correction can nearly double MAC and Pmax, as the table above shows.
- Changing the time correction between tests. Pick one rule and keep it.
- Mixing time in ms with distance in yards. Convert to s and m first.
- Fitting a speed trace that includes the slowdown after the finish. Drop samples after the top speed.
- Comparing values with and without air resistance, or values from `shorts` with values from the spreadsheet, in one trend.
- Treating F0 or Pmax as measured forces. They are model estimates.
- Reporting a profile when the residuals show a pattern, such as a large first-split residual.
- Using an old body mass. F0 and Pmax in N and W move with it.

## Example request

> I have 5, 10, 20, 30, and 40 m splits from our timing gates for the whole squad. Athletes start half a meter behind the first gate. Can you build sprint profiles in Google Sheets and tell me which ones look wrong?

## Check the result

Run these checks:

- Recompute one value by hand: MAC = MSS / τ, such as 8.523 / 1.107 = 7.70 m/s².
- Check the residuals. Look for a pattern, such as all residuals at the short splits having one sign, or one large first-split residual. A flying start leaves that pattern (Jovanović and Vescovi, 2022). In the example without a correction, the 5 m residual was 0.359 m. With the estimated correction, all residuals were 0.009 m or less.
- Compare each residual with the distance the athlete covers in one timing step. At 8 m/s and 0.01 s, that is 0.08 m. A residual several times larger points to a timing or start problem. This comparison is this skill's choice, not a published rule.
- Check that τ is not at the edge of the fit range, such as 0.5 or 2.0 s in the spreadsheet scan.
- Check that MSS is close to the speed over the last split. If MSS is well above it, the sprint was too short to reach top speed.
- Check that the force-velocity line slopes down. A positive SFV means the fit failed.

## Sources

This file draws on these sources:

- Asimakidis ND, Bishop CJ, Beato M, Mukandi IN, Kelly AL, Weldon A, Turner AN. A survey into the current fitness testing practices of elite male soccer practitioners: from assessment to communicating results. Frontiers in Physiology. 2024;15:1376047. https://doi.org/10.3389/fphys.2024.1376047 (accessed 2026-10-07)
- Lipčák A, Lipková L, Kalina T, Michaelides M, Parpa K, Paludo AC. The use of horizontal force-velocity profile in soccer: a rapid systematic review. BMC Sports Science, Medicine and Rehabilitation. 2025;17:200. https://doi.org/10.1186/s13102-025-01232-0 (accessed 2026-10-07, full text read in Europe PMC, PMC12261650)
- Samozino P, Rabita G, Dorel S, Slawinski J, Peyrot N, Saez de Villarreal E, Morin JB. A simple method for measuring power, force, velocity properties, and mechanical effectiveness in sprint running. Scandinavian Journal of Medicine and Science in Sports. 2016;26(6):648-658. https://doi.org/10.1111/sms.12490 (author manuscript at https://hal.science/hal-01389134, accessed 2026-10-07)
- Jovanović M, Vescovi JD. {shorts}: An R package for modeling short sprints. International Journal of Strength and Conditioning. 2022;2(1). https://doi.org/10.47206/ijsc.v2i1.74 (accessed 2026-10-07)
- Jovanović M. shorts: Short Sprints. R package version 3.2.0. 2024. https://cran.r-project.org/package=shorts (accessed 2026-10-07)
- Vescovi JD, Jovanović M. Sprint mechanical characteristics of female soccer players: a retrospective pilot study to examine a novel approach for correction of timing gate starts. Frontiers in Sports and Active Living. 2021;3:629694. https://doi.org/10.3389/fspor.2021.629694 (accessed 2026-10-07)
- Haugen TA, Breitschädel F, Seiler S. Sprint mechanical variables in elite athletes: are force-velocity profiles sport specific or individual? PLoS ONE. 2019;14(7):e0215551. https://doi.org/10.1371/journal.pone.0215551 (accessed 2026-10-07)
- Haugen TA, Tønnessen E, Seiler SK. The difference is in the start: impact of timing and start procedure on sprint running performance. Journal of Strength and Conditioning Research. 2012;26(2):473-479. https://doi.org/10.1519/JSC.0b013e318226030b (abstract, accessed 2026-10-07)
- Morin JB, Samozino P, Murata M, Cross MR, Nagahara R. A simple method for computing sprint acceleration kinetics from running velocity data: replication study with improved design. Journal of Biomechanics. 2019;94:82-87. https://doi.org/10.1016/j.jbiomech.2019.07.020 (abstract, accessed 2026-10-07)
- Clavel P, Leduc C, Morin JB, Buchheit M, Lacome M. Reliability of individual acceleration-speed profile in-situ in elite youth soccer players. Journal of Biomechanics. 2023;153:111602. https://doi.org/10.1016/j.jbiomech.2023.111602 (abstract, accessed 2026-10-07)
- Dos'Santos T, Thomas C, Jones PA, Comfort P. Assessing asymmetries in change of direction speed performance: application of change of direction deficit. Journal of Strength and Conditioning Research. 2019;33(11):2953-2961. https://doi.org/10.1519/JSC.0000000000002438 (accepted manuscript, accessed 2026-10-07)
