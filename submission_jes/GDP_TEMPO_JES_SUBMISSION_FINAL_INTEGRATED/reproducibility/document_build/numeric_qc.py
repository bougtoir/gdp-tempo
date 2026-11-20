import json, re, sys, os, docx
REPO = os.path.expanduser('~/repos/wip/gdp_tempo_paper/data')
OUT = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/work/jes/out')
txt = ' '.join(p.text for p in docx.Document(OUT + '/manuscript_JES_blinded.docx').paragraphs)
tab = ' '.join(c.text for t in docx.Document(OUT + '/tables_JES.docx').tables for r in t.rows for c in r.cells)
oos = json.load(open(REPO + '/oos_summary.json')); unc = {r['statistic']: r for r in json.load(open(REPO + '/cross_country_uncertainty.json'))['results']}
kl = json.load(open(REPO + '/k_level_summary.json')); ho = json.load(open(REPO + '/cwon_holdout_summary.json'))
m = lambda x: f'{x:.1f}'.replace('-', '−')
checks = [
 ('M0 OOS MAPE', f"{oos['M0']:.2f}%", txt), ('M2 OOS MAPE', f"{oos['M2']:.2f}%", txt),
 ('M1 OOS', f"{oos['M1']:.2f}%", txt), ('M3 OOS', f"{oos['M3']:.2f}%", txt), ('M4 OOS', f"{oos['M4']:.2f}%", txt),
 ('Relative reduction', f"{round(100*(oos['M0']-oos['M2'])/oos['M0'])}% relative", txt),
 ('Wilcoxon p', f"p = {oos['m2_vs_m0_wilcoxon_p']:.2f}", txt), ('Wilcoxon n', f"{oos['m2_vs_m0_n_pairs']} paired", txt),
 ('K gap median', m(unc['K_gap_pct']['median']) + '%', txt),
 ('K gap CI', f"[{m(unc['K_gap_pct']['country_boot_ci_lo'])}%, {m(unc['K_gap_pct']['country_boot_ci_hi'])}%]", txt),
 ('K gap IQR', f"{m(kl['K_pct_diff']['q25'])}% to {m(kl['K_pct_diff']['q75'])}%", txt),
 ('K LOO', f"{unc['K_gap_pct']['loo_median_min']:.2f}% and {unc['K_gap_pct']['loo_median_max']:.2f}%".replace('-', '−'), txt),
 ('TFP shift CI', f"[{unc['TFP_shift_pp']['country_boot_ci_lo']:.1f}, {unc['TFP_shift_pp']['country_boot_ci_hi']:.1f}]", txt),
 ('TFP shift median', f"{unc['TFP_shift_pp']['median']:.1f} percentage points", txt),
 ('LS IQR', f"{kl['labor_share_shift_pp']['q25']:.1f}–{kl['labor_share_shift_pp']['q75']:.1f}", txt),
 ('n countries 35', f"{kl['n_countries']} country means are negative", txt) if kl['countries_K_lower_than_M0'] == kl['n_countries'] else ('35 neg', 'FAIL', ''),
 ('Holdout joint', f"{100*ho['joint']['rm_holdout_median']:.1f}% for the joint", txt),
 ('Holdout prod', f"{100*ho['prod_only']['rm_holdout_median']:.1f}% for production-only", txt),
 ('Holdout M0', f"{100*ho['M0']['rm_holdout_median']:.1f}% for M0", txt),
 ('Holdout wins', ho['joint_beats_prod_only'].replace('/', ' of ') + ' countries', txt),
 ('Max K gap IRL', m(kl['K_pct_diff']['min']) + '%', txt), ('Min K gap GRC', m(kl['K_pct_diff']['max']) + '%', txt),
 ('Table II K median', f"{unc['K_gap_pct']['median']:.2f}".replace('-', '−'), tab),
 ('Bootstrap seed', '20261016', txt), ('Bootstrap B', '10,000', txt),
]
ok = True
for name, s, hay in checks:
    hit = s in hay; ok &= hit
    print(('PASS' if hit else 'FAIL'), name, repr(s))
for bad in ['statistically significant improvement', 'confidence interval for each country', 'all prior work', 'first to ', 'proves']:
    if re.search(r'\b' + re.escape(bad), txt): print('FAIL forbidden phrase', bad); ok = False
print('ALL PASS' if ok else 'SOME FAIL')
