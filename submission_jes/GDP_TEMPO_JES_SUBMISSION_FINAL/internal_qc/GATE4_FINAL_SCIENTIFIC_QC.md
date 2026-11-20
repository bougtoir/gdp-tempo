# Gate 4 — Final scientific QC
| Check | Result | Method |
|---|---|---|
| Sample sizes 39 (full) / 35 (OECD+CWON) | pass | text search + `numeric_qc.py` |
| Windows 1970–2019; CWON 1995–2019; OOS fit 1970–2014 / holdout 2015–2019; K comparison 2010–2019 | pass | text search |
| K gap median −4.3%, IQR −5.3% to −3.8%, country-bootstrap [−5.0%, −3.9%], LOO −4.31% to −4.25% | pass | vs `cross_country_uncertainty.json`, `k_level_summary.json` |
| TFP/labour-share sign: corrected-minus-baseline +1.7 pp, [1.5, 2.1]; Supp. Table 16 uses TFP_M0 − TFP_obs (negative = corrected higher), stated in note | pass | JSON + table notes |
| OOS: M0 4.60, M1 4.06, M2 3.99, M3 4.72, M4 4.61; Wilcoxon p = 0.18 (stat 292.0, n = 39) — reported as not significant | pass | vs `oos_summary.json` |
| CWON holdout 4.1 / 5.0 / 5.1%, 23 of 39 | pass | vs `cwon_holdout_summary.json` |
| Temporal 2.5–97.5% ranges labelled dispersion, not CIs; scaling range not a CI; bootstrap = exchangeability-conditional | pass | text search |
| Intangible overlap / upper-bound wording; calibration dependence in Limitations | pass | text search |
| Negative/non-significant results retained | pass | review |
| Equations native OMML | pass: 96 `m:oMath` objects, 0 pseudo-math markers; rendered correctly in LibreOffice PDF (pages inspected visually) | XML + render |
| Fonts/colour | Times New Roman (+Cambria Math in OMML), black only, 12 pt body / 10 pt captions; no character-spacing overrides | XML |
| Figures/tables | 0 embedded pictures in manuscript; 4 TIFF files; tables in separate DOCX; markers present; first-callout order I, 1, 2, 3, II, 4 | script |
| References | every in-text citation has an entry and vice versa (heuristic family-name/year match; false positives reviewed manually) | script + manual |
| Anonymity | no author names, repository URL, email or tracked comments; docProps author fields empty | XML scan |
| Clean clone / re-estimation | **not performed** (frozen outputs only; see GATE4_PUBLIC_REPOSITORY_STATUS.md) | — |
Limitations of this QC: rendering was checked in LibreOffice, not Microsoft Word; numeric QC is a string-level match of rounded values; supplementary numbers (Supp. Tables 1–15, Figures 1–14) were carried over from the OBES package without recomputation.
