# Gate 2 — Claim–evidence matrix
| # | Claim in JES manuscript | Evidence | Qualification in text |
|---|---|---|---|
| 1 | Observable lag lowers 2010–2019 K by median 4.3% (IQR −5.3 to −3.8) in 35 countries | `k_level_summary.json`, `cross_country_uncertainty.json` | conditional on calibrated asset lags; scenario, not proof of official mismeasurement |
| 2 | Country-bootstrap 95% interval [−5.0%, −3.9%] | `cross_country_uncertainty.json` (B = 10,000, seed 20261016) | superpopulation inference under exchangeability; excludes lag-calibration uncertainty; not country-level CI |
| 3 | TFP (log level) and implied labour share +1.7 pp, interval [1.5, 2.1] | same | accounting reclassification, not causal explanation of labour-share trends |
| 4 | All 35 country means negative; −0.6% (Greece) to −9.2% (Ireland) | `k_level_summary.json` | temporal ranges in Supp. Table 16 are dispersion, not CIs |
| 5 | M2 OOS MAPE 3.99% vs M0 4.60% | `oos_summary.json` | not significant: Wilcoxon p = 0.18, n = 39; inputs known in holdout |
| 6 | M4 OOS 4.61% ≈ M0 | `oos_summary.json` | M4 is a consistency model, not a forecaster |
| 7 | Joint model beats production-only in CWON 2015–2019 holdout (4.1% vs 5.0%; M0 5.1%), 23/39 countries | `cwon_holdout_summary.json` | CWON is not ground truth |
| 8 | Lag-scaling 0.5–2.0 gives MAPE 3.86–4.39% | Supplementary Table 2 (OBES frozen) | calibration-sensitivity range, not a CI |
| 9 | Intangible correction | Section 4.1 | upper-bound scenario: overlap with IPP already in PWT `rnna`/CWON possible |
| 10 | ρ₂ rises with R&D intensity (slope 0.068, t = 2.34) | Supplementary Figure 3 (OBES frozen) | association, cross-country |
| 11 | Lag within 2% under six depreciation schedules | Supplementary Figure 12 | lag and depreciation confounded in a single equation |
Numerical claims 1–7 re-checked automatically against frozen JSON (`numeric_qc_output.txt`). Claims 8, 10, 11 carried verbatim from the OBES frozen supplement; not recomputed.
