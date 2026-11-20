# Task-2 checks: every number integrated from former Supplement, recomputed from frozen outputs.
import json, sys, os, docx, pandas as pd
R = os.path.expanduser('~/repos/wip/gdp_tempo_paper')
OUT = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/work/jes/out2')
txt = ' '.join(p.text for p in docx.Document(OUT + '/manuscript_JES_blinded.docx').paragraphs)
b = pd.read_csv(R + '/data/bootstrap_ci.csv'); mc = pd.read_csv(R + '/tables/table12_monte_carlo.csv')
co = json.load(open(R + '/data/conditional_oos.json')); ex = pd.read_csv(R + '/tables/table4_extended_oos.csv').set_index('Model')
rp = pd.read_csv(R + '/tables/table3_rpim.csv').set_index('Model'); rg = json.load(open(R + '/data/rho2_regression.json'))
ds = json.load(open(R + '/data/delta_sensitivity_summary.json')); dt = pd.read_csv(R + '/tables/table11_delta_timevarying.csv')
ids = pd.read_csv(R + '/data/identification_surface.csv'); cw = pd.read_csv(R + '/data/counterfactual_wealth.csv')
fe = pd.read_csv(R + '/data/fair_eval.csv'); oo = pd.read_csv(R + '/data/oos.csv'); ho = json.load(open(R + '/data/cwon_holdout_summary.json'))
al = pd.read_csv(R + '/tables/table13_asset_lag_robustness.csv')
g = mc.groupby(['T', 'sigma']).mu_rmse.median(); t50 = g.loc[50]
C = [
 ('beta excl 0', f"excludes zero in {(b.beta_lo > 0).sum()} of 39", True),
 ('beta width', f"median width {(b.beta_hi - b.beta_lo).median():.2f}", True),
 ('mu above lower bound', f"in only {(b.mu_lo > 0.011).sum()} countries", True),
 ('mu width', f"median width is {(b.mu_hi - b.mu_lo).median():.1f} years", True),
 ('mu at bound', f"{((b.mu_central <= 0.011) | (b.mu_central >= 5.99)).sum()} of the 39 point estimates", True),
 ('MC bias mu=3', f"median bias {mc[mc.mu_true == 3.0].mu_bias.median():.1f} years".replace('-', '−'), True),
 ('MC rmse T30', f"about {g.loc[30].median():.2f} years", abs(g.loc[30].median() - 1.25) < 0.02),
 ('MC rmse T50', f"{t50.min():.2f}–{t50.max():.2f} years", True),
 ('MC beta rmse', f"RMSE {mc.groupby(['T','sigma']).beta_rmse.median().min():.2f}–{mc.groupby(['T','sigma']).beta_rmse.median().max():.2f}", True),
 ('MC grid', '0.25 years', abs((6.0 - 0.01) / 24 - 0.25) < 0.001),
 ('MC countries', 'United States, the Republic of Korea, France and Colombia', set(mc.country) == {'United States', 'Republic of Korea', 'France', 'Colombia'}),
 ('M1 bounds', f"{((fe.mu_M1 <= 0.011) | (fe.mu_M1 >= 5.99)).sum()} of the 39 countries reach a grid boundary", True),
 ('M1 lower/upper', f"({(fe.mu_M1 <= 0.011).sum()} at the lower and {(fe.mu_M1 >= 5.99).sum()} at the upper bound)", True),
 ('interior', f"In the {co['n_interior']} interior countries the median MAPE is {co['interior_M0_median']:.2f}% under M0, {co['interior_M1_median']:.2f}% under M1 and {co['interior_M2_median']:.2f}% under M2", True),
 ('boundary', f"in the {co['n_boundary']} boundary countries it is {co['boundary_M0_median']:.2f}%, {co['boundary_M1_median']:.2f}% and {co['boundary_M2_median']:.2f}%", True),
 ('M2 wins', f"M2 improves on M0 in {(oo.M2_oos_mape < oo.M0_oos_mape).sum()} of 39", True),
 ('M4 wins', f"M4 in only {(oo.M4_oos_mape < oo.M0_oos_mape).sum()}", True),
 ('dir acc', f"{ex.loc['M0','Dir. acc. median (%)']:.0f}% at the median", (ex['Dir. acc. median (%)'] == 100).all()),
 ('cwon rmse', f"{ex.loc['M0','CWON RMSE median']:.4f} under M0, {ex.loc['M1','CWON RMSE median']:.4f} under M1, {ex.loc['M2','CWON RMSE median']:.4f} under M2 and {ex.loc['M4','CWON RMSE median']:.4f} under M4", True),
 ('rho2', f"{rp.loc['M0','rho2 median']:.3f} under M0, with {rp.loc['M0','N(rho2 in 0.9-1.1)']} countries within [0.9, 1.1], and {rp.loc['M4','rho2 median']:.3f} under M4, with {rp.loc['M4','N(rho2 in 0.9-1.1)']}", True),
 ('R2', f"is {rp.loc['M0','R2 median']:.2f} under both", round(rp.loc['M4','R2 median'], 2) == round(rp.loc['M0','R2 median'], 2)),
 ('rho2 reg M4', f"slope {rg['M4_slope']:.3f}, heteroskedasticity-robust t = {rg['M4_t_stat']:.2f}", True),
 ('rho2 reg R2', f"= {rg['M4_R2']:.2f} under M4; slope {rg['M0_slope']:.3f}, t = {rg['M0_t_stat']:.2f} under M0", True),
 ('dep 2%', 'within 2%', (abs(dt.mean_mu_M1 / dt.set_index('scenario').loc['baseline', 'mean_mu_M1'] - 1) < 0.02).all() and dt.median_mu_M1.nunique() == 1),
 ('dep ±20', f"from {ds['d0.80']['mu_mean']:.2f} to {ds['d1.20']['mu_mean']:.2f} years with the median unchanged at {ds['d1.00']['mu_median']:.2f}", len({round(v['mu_median'], 2) for v in ds.values()}) == 1),
 ('ident flat', f"in {(ids.flat_joint < ids.flat_prod).sum()} of 39 countries (median share of near-minimal grid cells {ids.flat_joint.median():.2f} versus {ids.flat_prod.median():.2f})", True),
 ('cw max', f"at most {cw.pca_gap_pct.max():.1f}% of 2019 produced capital in the {(cw.beta_j > 0).sum()} countries", True),
 ('holdout vs M0', f"than M0 in {ho['joint_beats_M0'].split('/')[0]}", True),
 ('asset scaling', f"between {al['Median OOS MAPE (%)'].min():.2f}% and {al['Median OOS MAPE (%)'].max():.2f}%", True),
]
ok = True
for n, s, cond in C:
    hit = (s in txt) and bool(cond); ok &= hit; print('PASS' if hit else 'FAIL', n, repr(s))
for bad in ['Supplementary', 'Supporting Information', 'S.1', 'statistically sharp', 'excludes zero in 39']:
    if bad in txt: ok = False; print('FAIL forbidden', bad)
print('ALL PASS' if ok else 'SOME FAIL')
