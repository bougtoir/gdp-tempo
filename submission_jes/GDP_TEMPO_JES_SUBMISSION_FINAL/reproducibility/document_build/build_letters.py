import os, sys, docx
from docx.shared import Pt
OUT = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/work/jes/out')
TITLE = "Investment gestation lags, intangible capital and the measurement of capital and productivity in 39 economies"
A = "[AUTHOR TO COMPLETE]"
def doc():
    d = docx.Document(); s = d.styles['Normal']; s.font.name = 'Times New Roman'; s.font.size = Pt(12)
    d.core_properties.author = ''; d.core_properties.last_modified_by = ''
    return d
# cover letter
d = doc()
for t in [f"{A}: date", "The Editor", "Journal of Economic Studies", "", "Dear Editor,",
 f"We submit our manuscript, \u201c{TITLE}\u201d, for consideration as a Research Paper in the Journal of Economic Studies.",
 "The paper studies how two conventions in capital measurement — treating the investment-to-output lag as constant or negligible and leaving much intangible investment outside produced capital — affect measured capital, total factor productivity (TFP) and labour shares across countries. We estimate time-varying gestation lags and country-specific intangible shares for 39 economies over 1970–2019, discipline them with World Bank Changing Wealth of Nations produced-capital series, and construct a parameter-free observable lag from OECD asset composition for 35 economies.",
 "Under calibrated asset lags, the observable correction lowers 2010–2019 capital by a median 4.3% (country-bootstrap 95% interval −5.0% to −3.9%) and raises log-level TFP and the implied labour share by about 1.7 percentage points. We report these as assumption-conditional measurement scenarios rather than as proof of mismeasurement in official statistics. We also report evidence that does not favour strong claims: the out-of-sample improvement from a time-varying lag is not statistically significant (Wilcoxon p = 0.18), and the joint flow–stock model is a consistency device, not a forecasting model.",
 "We believe the paper fits the journal's balance between economic theory and application at the macro level and its international scope: it offers a transparent cross-country measurement framework relevant to productivity comparisons, growth accounting and the relationship between national-income and wealth accounts. It relates to recent work in the journal on intangible assets and productivity and on labour income shares.",
 "The manuscript is approximately 7,500 words under the journal's counting rule (all text plus 280 words for each of four figures and two tables). Tables are supplied in a separate file, figures as separate TIFF files and robustness material in a supplementary file. Code and public-data provenance are available in a public repository; the link is withheld from the anonymised files to preserve double-anonymous review and will be supplied to the editorial office on request or added at acceptance.",
 f"{A}: confirm that the manuscript is original, has not been published and is not under consideration elsewhere, and that both authors approved the submission.",
 f"{A}: declarations of funding, competing interests and use of generative AI tools, completed in line with Emerald's current AI policy.",
 "Yours sincerely,", f"{A}: names of both authors, on behalf of both authors", f"{A}: corresponding author contact details"]:
    d.add_paragraph(t)
d.save(OUT + '/cover_letter_JES.docx')
# title page
d = doc()
d.add_paragraph().add_run(TITLE).bold = True
d.add_paragraph("Title page for local completion by the authors — not part of the anonymised manuscript. Do not upload this file until every placeholder has been replaced by the authors.")
t = d.add_table(rows=1, cols=3); t.style = 'Table Grid'
for c, h in zip(t.rows[0].cells, ['Field', 'Author 1', 'Author 2']): c.text = h
for f in ['Full name exactly as to be published', 'Affiliation (where the research was conducted)', 'ORCID iD', 'Institutional email', 'Corresponding author (yes/no)', 'Contribution (e.g. CRediT roles)', 'Brief biography (≤100 words, optional)']:
    r = t.add_row().cells; r[0].text = f; r[1].text = A; r[2].text = A
for h, v in [("Acknowledgements", A), ("Funding (all external sources and the funder's role, or a statement of no external funding)", A),
 ("Declaration of competing interests", A),
 ("Declaration of generative AI use (tool name and version, purpose, sections affected; Emerald's AI policy does not permit generative-AI copywriting of any part of a submission or generative-AI reporting of statistics — authors must verify compliance)", A),
 ("Data availability", "Public input data: Penn World Table 10.01, World Bank WDI and CWON 2021, OECD GFCF by asset (SNA Table 8A). Code and frozen outputs: public repository https://github.com/bougtoir/gdp-tempo-paper (commit to be confirmed by the authors). Do not include this link in anonymised files."),
 ("Originality / not under consideration elsewhere", A),
 ("Word count (Emerald rule)", "≈7,500 including all text and 280 words for each of 6 exhibits; see FINAL_HANDOFF.txt")]:
    d.add_paragraph().add_run(h).bold = True; d.add_paragraph(v)
d.save(OUT + '/title_page_JES_LOCAL_COMPLETION.docx')
print('ok')
