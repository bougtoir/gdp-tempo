# HOSTILE_EDITORIAL_REVIEW — effect of eliminating the Supplement

Reviewer stance: a sceptical JES handling editor/referee who suspects the supplement was cut to hide weaknesses or to meet the word limit.

| # | Question | Finding | Verdict |
|---|---|---|---|
| 1 | Was a critical identification assumption removed? | No. The integration *added* identification evidence to the main text: weak identification of μ (bootstrap widths, 23/39 boundary estimates, Monte Carlo short-lag bias and RMSE), the 21/39 joint-surface result, depreciation confounding, CWON as reference account. Section 6.5 states that country-level point identification is not claimed and that capital-level results use the parameter-free M_obs. | PASS |
| 2 | Was a negative result concealed? | No. Main text now carries: p = 0.18 (non-significant M2 vs M0), M4 better than M0 in only 19/39, M2 gain confined to boundary countries (interior M2 4.46% vs M0 4.27%), non-discriminating direction accuracy, weak μ identification. The removed cluster and γ_price material contained no negative results whose removal flatters the paper; they contained *overstated positive* claims. | PASS |
| 3 | Is reproducibility weakened? | No source output deleted. Every removed or repository-only item is mapped to an exact file in the public repository (SUPPLEMENT_INTEGRATION_MATRIX). Table II note points to replication files. The repository link is withheld from blinded files for double-anonymous review and supplied via the cover letter on request — standard practice, but referees cannot inspect country-level detail during review unless the editor forwards it. | PASS with note |
| 4 | Were unsupported claims introduced? | All 30 integrated numbers recomputed from frozen outputs (numeric_qc_task2.py, 30/30). Wording restricted to what outputs show; no causal claims; calibration range labelled as sensitivity, not CI. | PASS |
| 5 | Was a table/figure/equation reference broken? | 0 dangling references; Table I–II and Figure 1–4 cited in order; 40/40 references cited; Borgo citation/reference mismatch fixed; orphan Hayashi and Prescott removed. | PASS |
| 6 | Is the main text now too compressed to evaluate? | Sect. 4.4 is dense (one paragraph carries bootstrap and Monte Carlo evidence). A referee can still evaluate identification because all key magnitudes and design parameters (B, block size, grids, T, σ, true μ, replications) are given. Country-level heterogeneity is visible only in Figures 2–4 and Table II quantiles. | PASS with note — a referee may request country tables; they exist in the repository |
| 7 | Abstract/results/discussion consistent? | Abstract (Originality) now states weak lag identification and reliance on M_obs, matching Sect. 4.4, 5.4, 6.2, 6.5. Headline numbers (−4.3%, [−5.0, −3.9], +1.7 pp, p = 0.18, 35/39 samples) identical across abstract, results, discussion, conclusion, Table II. | PASS |

## Residual risks an editor could still raise
1. Weak identification of μ, now disclosed, may lead a referee to question the value of M1/M2; the paper's defence is that its measurement results rest on M_obs.
2. Removing the cluster typology eliminates a "policy-relevant" cross-country grouping; this is deliberate because it was not validated.
3. Emerald AI policy: the revision text was drafted by an AI system; authors must review/rewrite and declare (author-only, not certified here).

**Gate 6: PASS (no blocking issue).**
