# SEMANTIC_CODE_AUDIT — computational paths affected by the integration

Code/data: public `bougtoir/gdp-tempo-paper` @ `709f2aba568a9582b4d00f1880f9689dd9a4fb37` (`git ls-remote`/GitHub API, main, committed
2026-10-16T08:18:10Z). The WIP copy `gdp_tempo_paper/` used for checks has identical `data/` and `tables/` outputs. **No model was
re-estimated and no analytical result was changed**; only the reporting of existing outputs changed. All integrated numbers are
recomputed from the frozen files by `numeric_qc_task2.py` (30/30 PASS) and the original headline checks by `numeric_qc.py` (25/25 PASS).

## 1. Estimands, signs, units
| Quantity | Definition in code | Sign / unit | Manuscript wording | Status |
|---|---|---|---|---|
| K gap | (K_obs − K_M0)/K_M0 ×100, country mean 2010–2019 (`k_level_summary.json`) | negative = observable-lag stock lower; % | "median −4.3%", "35 country means are negative" | consistent |
| TFP shift | log TFP_obs − log TFP_M0, pp | positive | "+1.7 percentage points" | consistent |
| Labour-share shift | equals TFP shift by the accounting identity in Sect. 5.4 | pp | stated as mechanical identity | consistent |
| OOS MAPE | level MAPE of log-GDP 2015–2019, % | lower = better | M0 4.60, M1 4.06, M2 3.99, M3 4.72, M4 4.61 | consistent |
| CWON holdout residual | |log ratio| with normalisation fitted ≤2014 (`cwon_holdout_validation.py` l.16–20, 43, 62) | % | 4.1 / 5.0 / 5.1 | consistent |
| CWON RMSE (extended OOS) | RMSE of *demeaned* log PIM vs CWON, holdout | log points | 0.0085/0.0077/0.0072/0.0085 | consistent; described as demeaned |
| ρ₂ | RPIM slope of log K_PIM on log K_CWON | dimensionless; 1 = proportional | medians 0.801 (M0), 0.833 (M4) | consistent |

## 2. Aggregation and denominators
* All "x of 39" counts use the full 39-country panel; K-level/TFP/labour-share results use the 35-country OECD asset subsample (stated in Sect. 4.2).
* M1 boundary counts use `fair_eval.csv` (`mu_M1` ≤ 0.011 → 18 lower; ≥ 5.99 → 7 upper; 14 interior) and match `conditional_oos.json` (n_interior 14, n_boundary 25).
* Medians are cross-country medians of country statistics, not pooled observations.

## 3. Temporal separation
* OOS: parameters and TFP projection fitted on ≤2014 (`asset_specific_tempo.py` l.416, 449, 516, 534), evaluated 2015–2019 with observed holdout inputs (conditional forecast; stated in Sect. 4.2).
* CWON holdout: joint/production-only fits use CWON ≤2014; level normalisation fitted on 1995–2014 only (leakage rule in script docstring). Holdout 2015–2019 never used.

## 4. Resampling units
* Within-country identification bootstrap: residual bootstrap of M4 growth residuals, B = 100 per country, block size 1 (`bootstrap_ci.csv`); percentile intervals, no multiplicity adjustment (stated).
* Cross-country uncertainty (Table II): country-level bootstrap, B = 10,000, seed 20261016 — conditional superpopulation inference under exchangeability (stated); the 2.5–97.5% country ranges are **temporal** dispersion, labelled as such.
* Asset-lag scaling 0.5–2.0 is a calibration sweep, not a sampling interval (stated).

## 5. Cluster-validation claims (explicitly requested check)
Code: `scripts/additional_analyses_economica.py` — loop `for k in range(2, 7)` (l.635) computes silhouette and inertia for every k;
`_bootstrap_stability` (l.599) is called **once**, for the selected k = 3 (l.656).

| Former claim (supplement S.18/S.23/S.24) | Computation | Verdict |
|---|---|---|
| "silhouette and bootstrap stability support k = 3" | silhouette k=2 0.236, k=3 **0.195**, k=4 0.222, k=5 0.220, k=6 0.249 | **Unsupported** — k = 3 is the minimum |
| "k = 3 near the maximum silhouette" | as above | **False** |
| "finer partitions are unstable" | no ARI computed for k ≠ 3 | **Unsupported** |
| "partition reasonably reproducible" (ARI 0.34) | ARI 0.34 | Overstated — weak agreement |

Action: all cluster claims removed from the submission (class D). No cluster claim exists in the manuscript, tables, figures or cover letter
(automated string check: "cluster", "silhouette", "k = 3" → 0 hits).

## 6. Other corrected interpretations
| Former statement | Evidence | Correction now in manuscript |
|---|---|---|
| μ interval "excludes zero in 39/39" | μ grid is `linspace(0.01, 6.0, 25)`; lower bound 0.01 > 0 by construction; only 5/39 lower limits exceed the bound; median width 5.74 y; 23/39 point estimates on a bound | Sect. 4.4 reports these facts; μ described as weakly identified |
| Monte Carlo "RMSE below grid resolution / sharp identification" | median μ RMSE ≈1.25 y (T=30), 0.61–0.85 y (T=50) vs grid step 0.25 y; bias −2.1 y at true μ=3 | Sect. 4.4, 6.5: weak identification, short-lag bias |
| Joint objective "less flat in most countries" | 21/39; median near-minimum share 0.13 vs 0.19 | exact count reported |
| ρ₂–R&D slope "t = 2.34" | OLS t 2.34; robust t 2.09, R² 0.13; M0 slope 0.054, robust t 1.56 | robust statistics and M0 contrast reported |
| Japan 2% price revaluation | γ_price units inconsistent with CWON; no in-range zero crossing | attribution removed; non-attribution stated |
| Headline M2 gain as evidence of estimated lags | interior median MAPE: M0 4.27 / M1 4.23 / M2 4.46; boundary: 4.72 / 3.98 / 3.83 | Sect. 5.2 says the gain comes from boundary countries |

Reproduction-record note: `reproducibility/reproduction_instructions.md` (carried over unchanged) lists "bootstrap mu excludes 0 in 39/39" as a
tracked reproduced metric. The number is reproduced correctly, but its interpretation is superseded by §6 above.

**Gate 4: PASS** (all affected paths consistent; every integrated number traced to a frozen output; unsupported claims removed).
