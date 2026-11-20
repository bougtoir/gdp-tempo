# SUPPLEMENT_INTEGRATION_MATRIX — S.1–S.25 and all supplementary exhibits

Classes: **A** integrate into main text · **B** condense and integrate · **C** repository only · **D** remove from submission narrative.
Default policy applied: essential material belongs in the main manuscript. Result: **no separate supplement is submitted.**
"Repository" = public `bougtoir/gdp-tempo-paper` @ `709f2aba568a9582b4d00f1880f9689dd9a4fb37` (files unchanged, nothing deleted).

| S | Topic (former exhibits) | Class | Scientific justification | New location / repository path |
|---|---|---|---|---|
| S.1 | Population–capital correspondence (Supp. T1) | B | Needed to understand the tempo analogy; the four-row mapping fits in one sentence, and the heuristic nature is now stated. | Sect. 3.3 (prose). `tables/table2_correspondence.csv` |
| S.2 | Observable asset-lag scaling 0.5–2.0 (Supp. T2) | B | Calibration dependence is a core caveat of M_obs; range must be visible to referees. Reported as calibration sensitivity, not a CI. | Sect. 4.2 (median OOS MAPE 3.86–4.39%); Table II note. `tables/table13_asset_lag_robustness.csv` |
| S.3 | In-sample growth-RMSE country ranking (Supp. F1) | C | Descriptive country detail; the cross-country summary (3.07–3.10 pp) is already in Sect. 5.1/Table I. | `data/fair_eval.csv`, `figures/` |
| S.4 | Historical episodes and counterfactual narrative (Supp. T3, T4) | C | Illustrative narrative; no main-text claim depends on it; episode selection is post hoc (see S.22). | `tables/table7_solow_episodes.csv`, `tables/table8_counterfactual_narrative.csv` |
| S.5 | Solow-residual variance decomposition (Supp. T5) | A | Already a main-text result (Sect. 5.5); only the dangling supplementary pointer was removed. | Sect. 5.5. `tables/table6_tempo_artifact.csv` |
| S.6 | TFP paths, six countries (Supp. F2) | C | Country illustrations; the mechanical TFP shift is shown in Figure 4 and Table II. | `figures/`, `data/` |
| S.7 | ρ₂ vs R&D intensity regression (Supp. F3) | B | Supports the interpretation of β; now reported with robust t and R², plus the weaker M0 comparison. | Sect. 6.2. `data/rho2_regression.json` |
| S.8 | Stock-side intangibles β | A | Core model element; already defined in the main framework. | Sect. 3.2 |
| S.9 | γ_price sensitivity | D | Semantic audit: the price-revaluation term is on a log-ratio scale inconsistent with the CWON units (median log ratio ≈ −14), and no country has an in-range zero crossing; any quantitative revaluation claim is unsupported. Only the qualitative non-attribution is kept. | Sect. 5.3/6.5 retain "not attributed". Raw: `data/gamma_price.csv` |
| S.10 | Japan asset-price revaluation case (Supp. F4) | B | The Japan divergence is a real feature of Figure 2 and must be discussed; the specific 2% revaluation attribution was removed (unsupported, see S.9). | Sect. 5.3, 6.5 |
| S.11 | Within-country bootstrap CIs for (μ, β) (Supp. F5) | B | Critical identification evidence. Corrected: μ interval above the 0.01 grid bound in only 5/39; median width 5.7 years; 23/39 estimates on a bound; β excludes 0 in 7/39. | Sect. 4.4. `data/bootstrap_ci.csv` |
| S.12 | Relational PIM diagnostics (Supp. F6, T6) | B | Main flow–stock diagnostic; medians and counts integrated. | Sect. 5.3. `tables/table3_rpim.csv` |
| S.13 | Depreciation ±20% sensitivity (Supp. F7) | B | Confounding of lag and depreciation is a key identification threat. | Sect. 6.2. `data/delta_sensitivity_summary.json` |
| S.14 | Conditional OOS, interior vs boundary (Supp. F8) | B | Negative result essential for honest interpretation: the M2 gain arises in boundary countries (25), not interior (14). | Sect. 4.3, 5.2. `data/conditional_oos.json` |
| S.15 | Extended OOS metrics (Supp. T7) | B | Direction-of-growth accuracy is non-discriminating (100% median); holdout CWON RMSE reported. | Sect. 5.2. `tables/table4_extended_oos.csv` |
| S.16 | Counterfactual wealth with β imputed (Supp. F9) | B | Upper-bound scenario statement needed for the double-counting caveat. | Sect. 5.4. `data/counterfactual_wealth.csv` |
| S.17 | Future scenarios 2020–2040 (Supp. F10, T8) | C | Out of scope for a measurement/accounting paper; extrapolations would invite forecasting claims the paper disavows. | `tables/table9_future_scenarios.csv` |
| S.18 | Clusters by (μ, β) and asset mix (Supp. F11, "Table 9") | D | Validation claims unsupported (SEMANTIC_CODE_AUDIT §5); clusters are built on weakly identified μ. | Raw: `tables/table10_cluster_analysis.csv`, `data/cluster_analysis.csv` |
| S.19 | Time-varying depreciation schedules (Supp. F12, T10) | B | Merged with S.13 (six schedules, mean lag within 2%). | Sect. 6.2. `tables/table11_delta_timevarying.csv` |
| S.20 | Monte Carlo identification (Supp. F13, T11) | B | Critical: corrects the former "sharp identification" claim; μ is weakly identified and biased towards short lags. | Sect. 4.4, 6.5. `tables/table12_monte_carlo.csv` |
| S.21 | Cross-country γ_price summary (Supp. T12) | D | Same unsupported revaluation analysis as S.9. | `tables/table14_gamma_price_summary.csv` |
| S.22 | Historical-episode leave-one-out (Supp. T13) | C | Supports only S.4, which is repository-only. | `tables/table7b_narrative_loo.csv` |
| S.23 | Cluster validation metrics (Supp. T14 = "Table 10b") | D | Silhouette for k = 3 is the lowest of k = 2–6; ARI computed only for k = 3 (0.34). | `tables/table10b_cluster_metrics.csv` |
| S.24 | Cluster diagnostics k = 2–6 (Supp. T15) | D | As S.23. | `tables/table10c_cluster_diagnostics.csv` |
| S.25 | CWON temporal holdout (Supp. F14) | A | Key external-validity check, already in main text; now also reports joint beats M0 in 27/39. | Sect. 5.3. `data/cwon_holdout_summary.json` |
| — | Supp. Table 16: country-level K gap, TFP shift, temporal 2.5–97.5% ranges | C | Country detail; the cross-country distribution and bootstrap CI are in Table II; temporal ranges are labelled as such. | `data/k_level_summary.json`, `data/cross_country_uncertainty.json` |
| — | Supp. Figure 15: implied labour-share correction | C | Identical in magnitude to the TFP shift by the accounting identity stated in Sect. 5.4 (Figure 4). | `data/k_level_summary.json` |

## Counts (S.1–S.25)
* A (integrated): **3** — S.5, S.8, S.25
* B (condensed and integrated): **12** — S.1, S.2, S.7, S.10, S.11, S.12, S.13, S.14, S.15, S.16, S.19, S.20
* C (repository only): **5** — S.3, S.4, S.6, S.17, S.22 (+ former Supp. Table 16 and Figure 15)
* D (removed from submission narrative): **5** — S.9, S.18, S.21, S.23, S.24
* Separate supplement retained: **none** (no item met the "demonstrably necessary" test).
