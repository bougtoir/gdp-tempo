import sys, re, copy, json, os
sys.path.insert(0, os.path.dirname(__file__))
import docx
from docx.oxml.ns import qn
from docx.shared import Pt, Inches
from engine import fill, new_par, words
import spec_front as F, spec_mid, spec_results, spec_disc
SRC = os.path.expanduser('~/work/jes/obes_complete/submission')
REPO = os.path.expanduser('~/repos/wip/gdp_tempo_paper')
OUT = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/work/jes/out')
os.makedirs(OUT + '/figures', exist_ok=True)

S = {}
for m in (F, spec_mid, spec_results, spec_disc): S.update(m.S)

def harvard(t):
    t = t.strip().replace(' & ', ' and ').replace(', and ', ' and ')
    m = re.match(r'^(.*?) \((\d{4}[a-z]?)\)\. (.*)$', t)
    if not m: return t
    au, yr, rest = m.groups()
    j = re.match(r'^(.*?[.?!]) (.*?), (\d+)\((\d+)\), (\d+)[–-](\d+)\.?(.*)$', rest)
    if j:
        ti, jo, v, n, p1, p2, tail = j.groups()
        ti = ti.rstrip('.')
        return f'{au} ({yr}), "{ti}", __{jo}__, Vol. {v} No. {n}, pp. {p1}-{p2}.{tail}'
    return f'{au} ({yr}), {rest}'

NEW_REFS = [
 'Castelli, C., Comincioli, N., Ferrante, C. and Pontarollo, N. (2024), "Tangible, intangible assets and labour productivity growth", __Journal of Economic Studies__, Vol. 51 No. 9, pp. 272-289, doi: 10.1108/JES-11-2023-0620.',
 'Çelik, O. (2021), "How human capital affects labor income share at the sectoral level?: Evidence from the EU-13 countries and the UK", __Journal of Economic Studies__, Vol. 49 No. 8, pp. 1491-1501, doi: 10.1108/JES-02-2021-0072.',
]
REF_OVERRIDE = {
 'Brass, W. (1971)': 'Brass, W. (1971), "On the scale of mortality", in Brass, W. (Ed.), __Biological Aspects of Demography__, Taylor and Francis, London, pp. 69-110.',
 'Corrado, C., Haskel, J., Iommi, M. and Jona-Lasinio, C. (2020)': 'Corrado, C., Haskel, J., Iommi, M. and Jona-Lasinio, C. (2020), "Intangible capital, innovation and productivity à la Jorgenson: evidence from Europe and the US", in Fraumeni, B.M. (Ed.), __Measuring Economic Growth and Productivity__, Academic Press, London, pp. 363-385, doi: 10.1016/B978-0-12-817596-5.00016-0.',
 'Corrado, C., Haskel, J., Jona-Lasinio, C. and Iommi, M. (2016)': 'Corrado, C., Haskel, J., Jona-Lasinio, C. and Iommi, M. (2016), "Intangible investment in the EU and US before and since the Great Recession and its contribution to productivity growth", EIB Working Papers No. 2016/08, European Investment Bank, Luxembourg.',
 'Corrado, C., Hulten, C. and Sichel, D. (2005)': 'Corrado, C., Hulten, C. and Sichel, D. (2005), "Measuring capital and technology: an expanded framework", in Corrado, C., Haltiwanger, J. and Sichel, D. (Eds), __Measuring Capital in the New Economy__, University of Chicago Press, Chicago, IL, pp. 11-46, doi: 10.7208/chicago/9780226116174.003.0002.',
 'Dasgupta, P. (2021)': 'Dasgupta, P. (2021), __The Economics of Biodiversity: The Dasgupta Review__, HM Treasury, London.',
 'Haskel, J. and Westlake, S. (2017)': 'Haskel, J. and Westlake, S. (2017), __Capitalism without Capital: The Rise of the Intangible Economy__, Princeton University Press, Princeton, NJ.',
 'Inklaar, R. and Timmer, M. P. (2013)': 'Inklaar, R. and Timmer, M.P. (2013), "Capital, labor and TFP in PWT 8.0", Research Memorandum GD-144, Groningen Growth and Development Centre, Groningen.',
 'Jorgenson, D. W., Ho, M. S. and Stiroh, K. J. (2005)': 'Jorgenson, D.W., Ho, M.S. and Stiroh, K.J. (2005), __Productivity, Volume 3: Information Technology and the American Growth Resurgence__, MIT Press, Cambridge, MA.',
 'Koeva, P. (2000)': 'Koeva, P. (2000), "The facts about time-to-build", IMF Working Paper No. 00/138, International Monetary Fund, Washington, DC.',
 'Lange, G.-M., Cust, J., Herrera, D., Naikal, E. and Peszko, G. (Eds.). (2021)': 'Lange, G.-M., Cust, J., Herrera, D., Naikal, E. and Peszko, G. (Eds) (2021), __The Changing Wealth of Nations 2021: Managing Assets for the Future__, World Bank, Washington, DC, doi: 10.1596/978-1-4648-1590-4.',
 'Managi, S. and Kumar, P. (Eds.). (2018)': 'Managi, S. and Kumar, P. (Eds) (2018), __Inclusive Wealth Report 2018__, Routledge, Abingdon.',
 'OECD. (2013)': 'OECD (2013), __Supporting Investment in Knowledge Capital, Growth and Innovation__, OECD Publishing, Paris, doi: 10.1787/9789264193307-en.',
 'Roth, F. (2022)': 'Roth, F. (2022), "Intangible capital and labor productivity growth – revisiting the evidence: an update", Hamburg Discussion Papers in International Economics No. 11, University of Hamburg, Hamburg.',
 'Stiglitz, J. E., Sen, A. and Fitoussi, J.-P. (2009)': 'Stiglitz, J.E., Sen, A. and Fitoussi, J.-P. (2009), __Report by the Commission on the Measurement of Economic Performance and Social Progress__, Commission on the Measurement of Economic Performance and Social Progress, Paris.',
 'United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development and World Bank. (2009)': 'United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development and World Bank (2009), __System of National Accounts 2008__, United Nations, New York, NY, available at: https://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf.',
}

def finalize(r):
    for k, v in REF_OVERRIDE.items():
        if r.startswith(k): return v
    r = re.sub(r'\. https://doi\.org/(\S+?)\.?$', r', doi: \1.', r)
    r = re.sub(r'([A-Z])\. (?=[A-Z]\.)', r'\1.', r.split(' (')[0]) + ' (' + r.split(' (', 1)[1]
    return r

DROP_REFS = ('Havranek, T.', 'Haskel, J., & Westlake, S. (2022)')

def build_manuscript():
    d = docx.Document(SRC + '/manuscript.docx')
    body = d.element.body
    kids = list(body.iterchildren())
    tables = {68: copy.deepcopy(kids[68]), 88: copy.deepcopy(kids[88])}
    # front matter
    fill(kids[0], F.TITLE, bold=True, size=14)
    abs_pars = [new_par('Abstract', bold=True)]
    for h, t in F.ABSTRACT: abs_pars.append(new_par(f'**{h}** – {t}'))
    abs_pars.append(new_par(f'**Keywords** – {F.KEYWORDS}'))
    abs_pars.append(new_par(f'**Paper type** – {F.PAPER_TYPE}'))
    abs_pars.append(new_par(f'**JEL classification** – {F.JEL}'))
    for p in reversed(abs_pars): kids[1].addnext(p)
    for i in (1, 2, 3): body.remove(kids[i])
    for i, txt in S.items():
        el = kids[i]
        if txt is None: body.remove(el); continue
        fill(el, txt)
    for i, subs in spec_disc.SUBST.items():
        for old, new in subs:
            hit = False
            for n in kids[i].iter(qn('w:t')):
                if n.text and old in n.text: n.text = n.text.replace(old, new); hit = True
            assert hit, (i, old)
    for i, pars in spec_disc.AFTER.items():
        for t in reversed(pars): kids[i].addnext(new_par(t))
    for i in (68, 88): body.remove(kids[i])
    # references
    refs = []
    for i in range(128, 169):
        t = ''.join(n.text or '' for n in kids[i].iter(qn('w:t')))
        body.remove(kids[i])
        if t.startswith(DROP_REFS): continue
        refs.append(finalize(harvard(t)))
    refs += NEW_REFS
    refs.sort(key=lambda s: re.sub(r'[^a-z]', '', s.lower().replace('ç', 'c'))[:40])
    anchor = kids[127]; fill(anchor, 'References', bold=True)
    last = anchor
    for r in refs:
        p = new_par(r); last.addnext(p); last = p
    hp = new_par('Figure captions', bold=True); last.addnext(hp); last = hp
    for c in spec_disc.CAPTIONS:
        p = new_par(c, size=10); last.addnext(p); last = p
    # heading styling + uniform font
    sec_cap = [False]
    for p in d.paragraphs:
        t = p.text.strip()
        if t == 'Figure captions': sec_cap[0] = True
        if re.match(r'^\d+\.\d+ ', t):
            fill(p._p, t, italic=True)
        elif re.match(r'^\d+\. [A-Z]', t) and len(t) < 60:
            fill(p._p, t, bold=True)
        for r in p._p.iter(qn('w:r')):
            rpr = r.find(qn('w:rPr'))
            if rpr is None or r.getparent().tag.startswith('{http://schemas.openxmlformats.org/officeDocument/2006/math}'):
                continue
            if sec_cap[0]: continue
            for e in rpr.findall(qn('w:sz')) + rpr.findall(qn('w:szCs')): e.set(qn('w:val'), '24')
            for tag in ('w:rFonts', 'w:color', 'w:spacing'):
                for e in rpr.findall(qn(tag)):
                    if tag == 'w:rFonts':
                        for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'): e.set(qn('w:' + a), 'Times New Roman')
                    elif tag == 'w:color': e.set(qn('w:val'), '000000')
                    else: rpr.remove(e)
    cp = d.core_properties
    cp.author = ''; cp.last_modified_by = ''; cp.comments = ''; cp.title = F.TITLE; cp.keywords = ''; cp.subject = ''
    d.save(OUT + '/manuscript_JES_blinded.docx')
    return tables

def build_tables(tables):
    unc = json.load(open(REPO + '/data/cross_country_uncertainty.json'))
    R = {r['statistic']: r for r in unc['results']}
    d = docx.Document()
    st = d.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(12)
    d.add_paragraph().add_run('Table I. Model performance across 39 countries: in-sample fit and out-of-sample MAPE (medians across countries; IQR in brackets)').bold = True
    cap = d.paragraphs[-1]._p; t1 = tables[68]; cap.addnext(t1)
    from engine import fill as _fill
    for tc in t1.iter(qn('w:tc')):
        tx = ''.join(n.text or '' for n in tc.iter() if n.tag in (qn('w:t'), qn('m:t')))
        if 'Time-varying' in tx and 'lag' in tx and len(tx) < 60:
            ps = tc.findall(qn('w:p')); _fill(ps[0], 'Time-varying lag ⟦μ(t)=μ_{0}+μ_{1}(t−t_{0})⟧', size=10)
            for p in ps[1:]: tc.remove(p)
    d.add_paragraph('Notes: Out-of-sample MAPE uses parameters fitted on 1970–2014 and levels for 2015–2019 with observed holdout inputs. M2 versus M0: two-sided Wilcoxon signed-rank p = 0.18 (39 pairs); not statistically significant. M4 is a flow–stock consistency model, not a forecasting model.').runs[0].font.size = Pt(10)
    d.add_page_break()
    d.add_paragraph().add_run('Table II. Capital-level measurement consequences of the observable lag, 2010–2019 country means (35 countries)').bold = True
    rows = [('K gap (%)', 'K_gap_pct'), ('TFP level shift (percentage points)', 'TFP_shift_pp'), ('Implied labour-share shift (percentage points)', 'LS_shift_pp')]
    t = d.add_table(rows=1 + len(rows), cols=6); t.style = 'Table Grid'
    hdr = ['Statistic', 'Median', '95% country-bootstrap interval', 'Interquartile range', 'Min to max', 'Leave-one-country-out median range']
    for c, h in zip(t.rows[0].cells, hdr): c.text = h
    f = lambda x: f'{x:.2f}'.replace('-', '−')
    for (lab, k), row in zip(rows, t.rows[1:]):
        r = R[k]
        vals = [lab, f(r['median']), f'[{f(r["country_boot_ci_lo"])}, {f(r["country_boot_ci_hi"])}]', f'{f(r["q25"])} to {f(r["q75"])}', f'{f(r["min"])} to {f(r["max"])}', f'{f(r["loo_median_min"])} to {f(r["loo_median_max"])}']
        for c, v in zip(row.cells, vals): c.text = v
    b = unc['bootstrap']
    d.add_paragraph(f'Notes: K gap = K_obs/K_M0 − 1. TFP shift = TFP_obs − TFP_M0 (positive = corrected TFP higher). The 95% interval resamples whole countries ({b["B"]:,} draws, seed {b["seed"]}) and is conditional superpopulation inference under exchangeability of countries; it is not an interval for any country-level parameter and excludes uncertainty in the calibrated asset gestation lags (bounded by the 0.5–2.0 scaling check, Supplementary Table 2). Country-level values and temporal 2.5th–97.5th percentile ranges are in Supplementary Table 16.').runs[0].font.size = Pt(10)
    for p in d.paragraphs:
        for r in p.runs: r.font.name = 'Times New Roman'
    d.core_properties.author = ''; d.core_properties.last_modified_by = ''
    d.save(OUT + '/tables_JES.docx')

def build_supplement(tables):
    d = docx.Document(SRC + '/supplementary_material.docx')
    rep = {2: [('Sect. 3.4', 'Sect. 3.3')], 37: [(' (Fig. 3)', '')], 47: [('Section 6.6', 'Section 6.5')], 52: [('Table 1 reports', 'Table I of the main text reports')]}
    for i, subs in rep.items():
        for old, new in subs:
            hit = False
            for n in d.paragraphs[i]._p.iter(qn('w:t')):
                if n.text and old in n.text: n.text = n.text.replace(old, new); hit = True
            assert hit, (i, old)
    d.add_page_break()
    d.add_paragraph().add_run('Supplementary Table 16. Country-level capital-level measurement consequences, 2010–2019 country means (35 countries)').bold = True
    d.paragraphs[-1]._p.addnext(tables[88])
    d.add_paragraph('Notes: K gap = K_obs/K_M0 − 1 (%). TFP shift is reported as TFP_M0 − TFP_obs, so negative values mean that corrected TFP is higher. Bracketed ranges are the 2.5th–97.5th percentiles of each country\'s annual values within 2010–2019: they describe temporal dispersion and are not confidence intervals. Cross-country inference for the medians is reported in Table II of the main text.')
    d.add_paragraph().add_run('Supplementary Figure 15. Implied labour-share correction from the observable-lag capital stock (country means, 2010–2019, 35 countries).').bold = True
    d.add_picture(SRC + '/figures/Figure_5.png', width=Inches(6))
    d.core_properties.author = ''; d.core_properties.last_modified_by = ''; d.core_properties.comments = ''
    d.save(OUT + '/supplementary_material_JES.docx')

def build_figures():
    from PIL import Image
    for k in range(1, 5):
        im = Image.open(f'{SRC}/figures/Figure_{k}.png')
        dpi = im.info.get('dpi', (300, 300))
        im.convert('RGB').save(f'{OUT}/figures/Figure_{k}.tif', compression='tiff_lzw', dpi=dpi)

if __name__ == '__main__':
    tb = build_manuscript(); build_tables(tb); build_supplement(tb); build_figures()
    print('built', OUT)
