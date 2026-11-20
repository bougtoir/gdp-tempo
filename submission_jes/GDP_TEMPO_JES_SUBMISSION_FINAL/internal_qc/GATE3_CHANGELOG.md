# Gate 3 — Changelog (OBES manuscript → JES blinded manuscript)
Build is scripted and deterministic: `build/build_jes.py` reads the authoritative OBES DOCX and applies paragraph-level replacements from `build/spec_*.py`; equation paragraphs/equation-layout tables are carried over unchanged (native OMML). New inline mathematics is written as native OMML by `build/engine.py`.

- Title changed to a measurement framing; structured Emerald abstract (4 mandatory headings) with keywords (6), paper type and JEL (E01, E22, O47): 227 words incl. all.
- Body compressed 6,677 → 4,402 words; section structure 1–7 retained; demographic-analogy discussion and policy speculation removed; limitations kept and extended (calibration dependence, intangible overlap).
- Overclaims removed: "all prior work…", instantaneous-PIM-everywhere, "first step", tempo artefact language, causal labour-share language, forecasting superiority.
- Tables: separate `tables_JES.docx`, Roman numerals; Table I = OBES Table 1; Table II new compact summary computed from `cross_country_uncertainty.json`; OBES Table 2 → Supplementary Table 16 with corrected temporal-dispersion note and TFP sign convention.
- Figures: OBES Figures 1–4 → `Figure_1–4.tif` (LZW, same pixels/DPI as PNG); captions listed after references; placement markers `[Figure n about here]`; Figure 5 → Supplementary Figure 15.
- First-callout order verified: Table I, Figure 1, Figure 2, Figure 3, Table II, Figure 4.
- References: converted to Emerald Harvard (Vol./No./pp., doi:), 2 JES articles added, 2 uncited removed; citation↔reference heuristic check passed.
- Formatting: Times New Roman 12 pt black (captions 10 pt), first-level headings bold, second-level italic, character-spacing overrides removed; docProps author/lastModifiedBy blank; no comments; blinding scan: no author names/repo URL/emails (only "Oxford Bulletin" as journal names in two references).
- Supplement: cross-references updated to new section/table numbers; Supplementary Table 16 and Figure 15 appended. Known inherited residual: internal labels "Table 9"/"Table 10b" in Supplementary §§ on clustering refer to supplementary tables and were not renumbered (authors to check).
- Pronouns: "we/our" throughout; no sole-author phrasing found.
