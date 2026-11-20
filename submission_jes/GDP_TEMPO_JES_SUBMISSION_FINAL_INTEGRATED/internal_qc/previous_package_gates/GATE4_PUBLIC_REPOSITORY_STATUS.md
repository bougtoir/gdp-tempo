# Gate 4 — Public repository status (checked 2026-11-09T01:00Z with `git ls-remote`)
| Item | Value |
|---|---|
| Repository | https://github.com/bougtoir/gdp-tempo-paper (name contains no journal name) |
| `main` HEAD | `709f2aba568a9582b4d00f1880f9689dd9a4fb37` |
| Recorded OBES reproduction commit | `6c0d313129ced627128b7fadfe142a08004d02cc` (from OBES `reproducibility/repository_commit.txt`) |
| Uncertainty branch | `obes-v2-uncertainty` @ `45cc11890057abefb4a913d51e550507714f6aa2` |
| Open refs | `refs/pull/1/head`, `refs/pull/2/head` exist; not modified |

## What was and was not done in this session
- **No full re-estimation was run** and **no clean-clone rebuild was performed** in this session. The repository's own `.venv` was absent in the VM; no environment repair was attempted because the JES work needs no new estimation.
- All JES numbers come from frozen JSON outputs in `wip/gdp_tempo_paper/data/` (from the OBES-era pipeline) and are re-checked by `build/numeric_qc.py` (string-level comparison of rounded values; 25/25 PASS).
- The only new code is document-building (`build/*.py`). It received focused smoke tests: OMML generation, DOCX open via python-docx, PDF render via LibreOffice, numeric/string QC. It does not alter any scientific output.
- PR #692 was not recreated or touched.
- The repository URL is excluded from anonymised files; it appears only in the title page (local completion) and in this QC folder.
- Authors should confirm which commit to cite at submission (6c0d313 = recorded reproduction; 709f2ab = current main) and that the repository README contains no journal names or author-revealing text if the link is shared with reviewers.
