# Verified public URLs (checked 2026-11-09T01:00Z)
- Code/data repository: https://github.com/bougtoir/gdp-tempo-paper — main `709f2aba568a9582b4d00f1880f9689dd9a4fb37`; recorded reproduction commit `6c0d313129ced627128b7fadfe142a08004d02cc`; uncertainty branch `obes-v2-uncertainty` `45cc11890057abefb4a913d51e550507714f6aa2` (verified with `git ls-remote`).
- Data sources: see `public_sources.md` (Penn World Table 10.01, World Bank WDI, World Bank CWON 2021, OECD SNA Table 8A).
- `document_build/` contains the scripts that build the JES documents from the OBES manuscript and frozen JSON; they do not change any estimate. Paths inside the scripts point to the build VM and must be adapted.
- The reproduction record files here are carried over unchanged from the earlier package; they describe a reproduction made before this session. No new reproduction was performed.

## Integrated revision (2026-11-12)
- All outputs cited by the integrated manuscript were checked blob-for-blob (`git hash-object` vs GitHub contents API) against public main `709f2aba568a9582b4d00f1880f9689dd9a4fb37`: 18/18 identical (data/bootstrap_ci.csv, conditional_oos.json, cwon_holdout_summary.json, identification_surface.csv, rho2_regression.json, counterfactual_wealth.csv, delta_sensitivity_summary.json, fair_eval.csv, oos.csv; tables/table3, table4, table10b, table10c, table11, table12, table13; scripts/additional_analyses_economica.py, cwon_holdout_validation.py).
- Former supplementary material now repository-only is listed with exact paths in `internal_qc/SUPPLEMENT_INTEGRATION_MATRIX.md`.
- `document_build/` now includes `spec_task2.py` (integration text), `style_fix.py`, `word_count.py`, `numeric_qc_task2.py`. Build order: build_jes.py OUT → build_letters.py OUT → style_fix.py OUT/*.docx → numeric_qc.py OUT → numeric_qc_task2.py OUT.
- Interpretation note: the reproduced metric "bootstrap mu excludes 0 in 39/39" in reproduction_instructions.md is a grid-bound artefact (lower bound 0.01); see internal_qc/SEMANTIC_CODE_AUDIT.md §6.
- No re-estimation or clean-clone rebuild was performed in this revision.
