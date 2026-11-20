# FIGURE_TABLE_REFERENCE_AUDIT — integrated submission (`out2/`)

## First-citation order in the manuscript (automated scan of body text)
Table I → Figure 1 → Figure 2 → Figure 3 → Table II → Figure 4. Tables numbered I, II (Roman) and figures 1–4 (Arabic) each in order of first citation. Position markers "[Table I about here]" … "[Figure 4 about here]" follow their first citation.

| Exhibit | File | First cited | Marker | Caption/notes |
|---|---|---|---|---|
| Table I | tables_JES.docx | Sect. 4.2 / 5.1 | Sect. 5.1 | title, headings, notes (models, metrics, Wilcoxon p = 0.18, n = 39) |
| Figure 1 | figures/Figure_1.tif | Sect. 5.2 | Sect. 5.2 | caption in manuscript "Figure captions" |
| Figure 2 | figures/Figure_2.tif | Sect. 5.3 | Sect. 5.3 | caption |
| Figure 3 | figures/Figure_3.tif | Sect. 5.4 | Sect. 5.4 | caption |
| Table II | tables_JES.docx | Sect. 5.4 | Sect. 5.4 | notes distinguish country-bootstrap CI from temporal ranges and calibration range; refer to replication files instead of Supplementary Tables |
| Figure 4 | figures/Figure_4.tif | Sect. 5.4 | Sect. 5.4 | caption |

## Orphans and dangling references
* Strings "Supplementary", "Supporting Information", "S.<n>", "Table 9", "Table 10b", "Table 13/14/15": 0 occurrences in manuscript, tables file, cover letter, title page.
* Every section cross-reference resolves to an existing heading (3.1–3.4, 4.1–4.4, 5.1–5.5, 6.1–6.5); "equation (2)" resolves.
* References: 40 entries, all cited; every in-text author–year citation has an entry; list alphabetically ordered (Harvard).
* Equations: 101 native OMML objects in the manuscript (96 before; 5 added in integrated passages), 2 in the tables file; no equation images.

## Style and format (document and style definitions)
| Check | Manuscript | Tables | Cover letter / title page |
|---|---|---|---|
| Fonts in document.xml | Times New Roman (+ Cambria Math inside OMML) | same | TNR |
| Fonts in styles.xml | TNR only; theme-font references removed | TNR | TNR |
| Font size | 12 pt body (sz 24), 10 pt table notes (sz 20) | same | 12 pt |
| Visible text colour | 000000 only (document and styles) | same | same |
| Character spacing (w:spacing w:val) | 0 in document and styles | 0 | 0 |
| Author metadata (core.xml creator/lastModifiedBy) | blank | blank | — |
| Anonymity: author names, affiliations, repository URL | none in manuscript/tables | none | URL withheld in cover letter |
| Pronouns | we/our/us (two authors) | — | — |

Rendering: LibreOffice → PDF (manuscript 19 pp., tables 2 pp.); pages with new Sect. 4.3–4.4 text inspected visually. Not checked in Microsoft Word.

**Gate 5: PASS.**
