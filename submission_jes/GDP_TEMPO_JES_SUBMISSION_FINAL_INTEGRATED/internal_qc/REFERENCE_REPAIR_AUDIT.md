# REFERENCE_REPAIR_AUDIT — GDP+Tempo, JES integrated revision

Scope: `supplementary_material_JES.docx` in the previous package `GDP_TEMPO_JES_SUBMISSION_FINAL.zip`, checked against the
authoritative OBES files (`obes_complete/submission/supplementary_material.docx`, `obes_complete/submission/tables/*.csv|docx`)
and the frozen computational outputs in the public repository `bougtoir/gdp-tempo-paper` @ `709f2aba568a9582b4d00f1880f9689dd9a4fb37`
(identical to WIP `gdp_tempo_paper/`).

## 1. Confirmation of the reported errors

| # | Reported finding | Confirmed? | Root cause |
|---|---|---|---|
| 1 | S.18 cites "Table 9", which does not exist in the supplement | **Confirmed** | The previous JES supplement builder copied S.1–S.25 prose but embedded only three tables. The prose of S.18 used the legacy OBES file-style label "Table 9" (`table10_cluster_analysis`), never renumbered. |
| 2 | Supplementary Figure 11 caption cites "Table 10b" | **Confirmed** | Legacy file-style label for `tables/table10b_cluster_metrics.csv`, i.e. the content of S.23 ("Supplementary Table 14"). Not a separate result. |
| 3 | S.23 again cites "Supplementary Table 9" | **Confirmed** | Same legacy label; the object meant is the cluster-composition table (`table10_cluster_analysis.csv`). |
| 4 | S.22 describes Table 13, embedded table labelled "Supplementary Table 1" | **Confirmed** | Builder re-numbered the three embedded tables 1–3 by insertion order. Content = `table7b_narrative_loo.csv` = intended Supplementary Table 13. |
| 5 | S.23 describes Table 14, embedded table labelled "Supplementary Table 2" | **Confirmed** | Content = `table10b_cluster_metrics.csv` = intended Supplementary Table 14. |
| 6 | S.24 describes Table 15, embedded table labelled "Supplementary Table 3" | **Confirmed** | Content = `table10c_cluster_diagnostics.csv` = intended Supplementary Table 15. |

Additional errors found during the full audit (not in the user's list):

| # | Finding | Status |
|---|---|---|
| 7 | Supplementary Tables 1–12 were cited in S.1–S.21 but **none was embedded** in the previous JES supplement (document-generation omission; all source CSV/DOCX files exist). | Confirmed; resolved by integration/removal (Section 3). |
| 8 | Main manuscript cited Supplementary Table 1, 4, 5, 16 and Supplementary Figures 1, 3, 9, 12, 14 and "Supplementary Section S.14". | Confirmed; all such references removed or replaced by in-text results (Section 3). |
| 9 | Reference list: "Hayashi and Prescott (2002)" listed but not cited; "dal Borgo et al." listed with lower-case particle while cited as "Borgo et al., 2013". | Fixed: Hayashi and Prescott removed; entry and citation harmonised to "Dal Borgo et al. (2013)", bibliographic data checked against Crossref (`raw_crossref/borgo2013.json`, SHA-256 `c419ab5d…`). |

## 2. Were Tables 9 and 10b omitted, renamed or incorrectly referenced?

* **"Table 9"** = renamed/incorrectly referenced. It is the OBES file `table10_cluster_analysis.csv` (k-means cluster composition, k = 3),
  which in the JES supplement plan was "Supplementary Table 9". It was never embedded (omitted) and was cited under a stale label.
* **"Table 10b"** = incorrectly referenced. It is `table10b_cluster_metrics.csv` (silhouette 0.195, bootstrap ARI 0.34, k = 3),
  i.e. the same object that S.23 calls "Supplementary Table 14". There is no separate "Table 10b" result.
* No result was invented. Both source files exist in the public repository (`tables/`).

## 3. Resolution

The cluster material (S.18, S.23, S.24, Supplementary Figure 11, "Table 9", "Table 10b", Supplementary Tables 14 and 15) was **not
recovered into the submission but removed from the submission narrative (class D)**, because the semantic audit
(`SEMANTIC_CODE_AUDIT.md` §5) showed that its validation claims were not supported by the computations:

* k = 3 has the *lowest* silhouette among k = 2–6 (0.195 vs 0.236, 0.222, 0.220, 0.249), contradicting "near the maximum silhouette";
* bootstrap ARI was computed only for k = 3 (0.34), so no statement about the stability of other k is supported;
* ARI 0.34 indicates weak, not "reasonable", reproducibility.

No main-text claim depends on the cluster results; the main manuscript never cited them. The source files remain in the repository
unchanged (no deletion of authoritative outputs).

Tables 13–15:
* Supplementary Table 13 (`table7b_narrative_loo`, historical-episode leave-one-out) — repository only (class C); the historical-episode
  narrative it supports (S.4) is not used in the main manuscript.
* Supplementary Tables 14–15 (cluster metrics/diagnostics) — removed with the cluster narrative (class D).
* Their mislabelled captions therefore no longer exist anywhere in the submission.

Since no separate supplement is submitted, the "Supplementary Table/Figure N" numbering scheme is retired altogether; the
integrated manuscript contains only Table I–II and Figure 1–4.

## 4. Orphan-reference audit of the integrated submission (automated; `out2/`)

| Object class | Defined | Cited in text | Orphans | Missing targets |
|---|---|---|---|---|
| Tables (I, II) | 2 (tables_JES.docx) | 2 | 0 | 0 |
| Figures (1–4) | 4 TIFF + 4 captions | 4 | 0 | 0 |
| Equations (1)–(n) cross-referenced | equation (2) cited in Sect. 5.3; target exists | — | 0 | 0 |
| Sections/subsections | 1–7, 3.1–3.4, 4.1–4.4, 5.1–5.5, 6.1–6.5 | all cross-references (Sect. 3.2, 3.4, 4.1, 4.2, 4.3, 4.4, 5.2, 5.4, 6.5, …) resolve to existing headings | 0 | 0 |
| Appendix | none | none | 0 | 0 |
| "Supplementary …", "Supporting Information", "S.n" strings in manuscript, tables, cover letter | — | **0 occurrences** | — | — |
| References | 40 | 40 cited | 0 | 0 |

**Gate 1: PASS.** Every retained reference resolves to an existing object; no retained numerical or scientific claim depends on a missing table.
