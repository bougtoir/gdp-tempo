# Gate 0 — JES requirements and authoritative baseline

## OBES decision (recorded exactly)
- OBES-26-685, desk decision dated 8 November 2026: the editor found interesting points but judged the paper better suited to a specialist macroeconomics journal. **No external review took place.** Nothing in this package states or implies that OBES validated the science.
- Journal of Macroeconomics is not an option (rejected June 2026; charges a submission fee).

## Authoritative baseline
| Item | Value |
|---|---|
| Source package | `GDP_TEMPO_OBES_SUBMISSION_FINAL_COMPLETE.zip`, SHA-256 `71c6bb9da05cc5f8986e0d3abbcc886fadd5433d0713c6e4b7c09c12f1d2e39e` |
| Manuscript | `submission/manuscript.docx` (161 body elements; 5 inline figures; 2 data tables + 6 equation-layout tables) |
| Supplement | `submission/supplementary_material.docx` (Supplementary Tables 1–15, Figures 1–14) |
| Figures | `submission/figures/Figure_1–5.png`, `Supplementary_Figure_1–14.png` |
| Frozen outputs | `gdp_tempo_paper/data/*.json` in wip (oos_summary, cross_country_uncertainty, k_level_summary, cwon_holdout_summary) |
| Recorded reproduction | public `bougtoir/gdp-tempo-paper` commit `6c0d313129ced627128b7fadfe142a08004d02cc`; branch `obes-v2-uncertainty` @ `45cc1189` |
| Public `main` now | `709f2aba568a9582b4d00f1880f9689dd9a4fb37` (git ls-remote, 2026-11-09T01:00Z) |

## Official rules (sources and access)
Live `emerald.com` pages returned HTTP 403 (Cloudflare) on 2026-11-09 via curl and via headless Chrome. Rules were read from Internet Archive captures of the official pages; raw HTML/text and SHA-256 sums are stored in `raw_guidelines/`.

| Requirement | Rule | Source capture |
|---|---|---|
| Article type / length | Research Paper up to 8,000 words; **count includes all text, figures and tables; allow 280 words per figure or table** (not a text-only limit) | emerald.com/jes/, 2026-10-18 |
| References | Harvard | JES page |
| Keywords | up to 6 | JES page + author guidelines |
| Review | double-anonymous | JES page |
| Files | Microsoft Word; PDF alone not accepted | JES page + author guidelines |
| Language | UK or US English | JES page |
| Abstract | Structured: Purpose; Design/methodology/approach; Findings; Originality (optional: Research limitations/implications; Practical implications; Social implications); **≤250 words including keywords and article classification** | Emerald author guidelines, 2026-07-28 |
| Tables | Separate file; position labelled in main text; Roman numerals; main title; footnotes for symbols | author guidelines |
| Figures | Separate electronic files; .ai, .eps, .jpeg, .bmp, .tif (PNG not listed); Arabic numerals; captions | author guidelines |
| Headings | first level bold; sub-headings medium italics | author guidelines |
| Author details | entered in ScholarOne; biographies/acknowledgements in a separate Word file; funding in acknowledgements | author guidelines |
| Supplementary | separate, clearly labelled files; repository links may break anonymity | author guidelines |
| Charges | No submission fee: "the only time we will ever ask you for money ... is if you have chosen ... gold open access ... never at submission". Hybrid journal; green/subscription route at no cost | author guidelines FAQ + JES page |
| AI | Emerald AI policy (publication-ethics capture 2026-09-29): AI use must be declared; generative-AI copywriting of **any part** of a submission (including abstract/literature review) is not permitted; generating/reporting data or in-text statistics with generative AI is not permitted; AI-assisted analysis permitted with transparent declaration | `raw_guidelines/ai_policy_excerpt.txt` |
| Research data statement | No mandatory JES-specific data statement found in the captured pages; trusted-repository guidance applies | author guidelines |
| JEL codes | Not required by captured pages; included (E01, E22, O47) inside the 250-word abstract budget | — |

Not verifiable offline: whether the live pages changed after the captures; ScholarOne form fields. Authors should re-check the live JES page before upload.

## Word inventory
| Component | OBES baseline | JES build |
|---|---|---|
| Title | 15 | 15 |
| Abstract (+keywords/JEL/type) | 97 | 227 |
| Body text | ≈6,677 | 4,402 |
| References | 918 | 1,067 (Emerald Harvard format is longer) |
| Captions | (inline) | 81 |
| Exhibits | 7 (5 figures + 2 tables) → 1,960 | 6 (4 figures + 2 tables) → 1,680 |
| **Effective total** | **≈10,900** (over limit) | **7,478** |
| Conservative (also count text inside tables file) | — | 7,700 |
Equation-layout tables contribute 6 words. Machine-readable: `word_inventory_JES.json`.
