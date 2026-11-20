# WORD_COUNT_AUDIT — integrated JES manuscript

Rule (Emerald/JES, archived 2026-10-18): Research Paper ≤ 8,000 words including all text (abstract, references, captions, tables)
plus 280 words per figure/table. Counter: `word_count.py` (whitespace tokens of every paragraph and table cell of
`manuscript_JES_blinded.docx`; OMML equation runs are not counted as words).

| Component | Previous package (same counter) | Integrated version |
|---|---|---|
| Title/front | 15 | 15 |
| Structured abstract incl. keywords, type, JEL | 227 | 241 |
| Body (Sections 1–7) | 4,335 | 4,543 |
| Equation-layout tables | 6 | 6 |
| References | 1,067 | 1,042 (Hayashi and Prescott removed) |
| Figure captions | 81 | 81 |
| **Counted text** | 5,731 | **5,928** |
| Exhibits: 4 figures + 2 tables × 280 | 1,680 | **1,680** |
| **Effective total** | 7,411 | **7,608** |
| Conservative variant: + text inside `tables_JES.docx` (278 words) instead of nothing | — | 7,886 |
| Separate supplement | ~ (not counted by JES) | **none** |

Notes
* The previous handoff reported 5,798/7,478 using an earlier inventory script; re-counting the previous file with the present counter gives 5,731/7,411. The present counter is used for both columns so the delta (+197 text words) is like-for-like.
* Abstract alone (paragraph text, incl. keywords/type/JEL): 242 words ≤ 250.
* Both the standard (7,608) and the conservative (7,886) totals are within 8,000. Cover letter and title page state "approximately 7,600".

**Gate 3 word limit: PASS** (no FORMAT NO-GO needed).
