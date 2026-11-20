# Task-2 (supplement integration) overrides applied on top of spec_front/mid/results/disc.
import spec_mid, spec_results, spec_disc

def rep(s, old, new):
    assert old in s, old
    return s.replace(old, new)

S = {}
S[35] = ("We map the demographic quantities analysed by Bongaarts and Feeney (1998) and Goldstein et al. (2003) onto their capital-accounting counterparts: investment corresponds to births, the PIM stock to the population stock, ⟦μ(t)⟧ to the mean age at childbearing and ⟦β⟧ to the omitted quantity parameter. The analogy is heuristic, because depreciation, unlike mortality, is itself an estimated quantity (Section 6.5).")
S[54] = rep(spec_mid.S[54], "(Supplementary Table 2)", "(factors 0.5, 0.75, 1.0, 1.25, 1.5 and 2.0; 35 countries)")
S[61] = rep(spec_mid.S[61], "; Supplementary Section S.14 reports out-of-sample results for the 14 interior solutions", "; Section 5.2 reports out-of-sample results separately for the 14 interior solutions")
S[62] = "4.4 Within-country bootstrap and Monte Carlo experiments"
S[63] = ("For each country we residual-bootstrap the M4 growth residuals 100 times (block size 1; block size 3 gave nearly identical intervals in a five-country pilot), rebuild synthetic output, investment, R&D and capital series, and re-run the joint grid. We report 95% percentile intervals without multiple-testing adjustment. The intervals are wide. The interval for ⟦β⟧ excludes zero in 7 of 39 countries (median width 0.23 on a 0–0.34 grid). The interval for ⟦μ⟧ lies above the lower grid bound of 0.01 years in only 5 countries, its median width is 5.7 years on a 0.01–6.0-year grid, and 23 of the 39 point estimates lie on a grid bound. "
         "Monte Carlo experiments calibrated to the United States, the Republic of Korea, France and Colombia (sample lengths of 30, 40 and 50 years, three output-shock variances, three true lags and 100 replications per cell) confirm that ⟦μ⟧ is weakly identified: the joint estimator is biased towards short lags (median bias −2.1 years when the true lag is 3 years), and its median RMSE falls from about 1.25 years at 30 years of data to 0.61–0.85 years at 50 years, against a grid step of 0.25 years. ⟦β⟧ is estimated more precisely (RMSE 0.05–0.15). The capital-level results in Section 5.4 therefore rely on the parameter-free M_obs rather than on estimated lags.")
S[75] = ("The median masks heterogeneity: M2 improves on M0 in 23 of 39 countries and M4 in only 19. The gain also differs across the M1 lag regimes of Section 4.3. In the 14 interior countries the median MAPE is 4.27% under M0, 4.23% under M1 and 4.46% under M2; in the 25 boundary countries it is 4.72%, 3.98% and 3.83%. The headline M2 gain therefore comes from countries whose lag is inoperative or constrained, not from freely estimated lags. Direction-of-growth accuracy is 100% at the median for every model and does not discriminate. On the holdout, the median RMSE of demeaned log PIM capital against CWON is 0.0085 under M0, 0.0077 under M1, 0.0072 under M2 and 0.0085 under M4.")
S[77] = rep(spec_results.S[77], "which a revaluation sensitivity check attributes plausibly to asset prices rather than quantities (Hayashi and Prescott, 2002; Supplementary Figure 4).",
            "which we do not attribute: land and asset-price revaluations that CWON carries but our quantity-based PIM omits are one candidate that our data cannot test. The relational diagnostic of Section 3.4 summarises the comparison for all 39 countries: the median ⟦ρ_{2}⟧ is 0.801 under M0, with 9 countries within [0.9, 1.1], and 0.833 under M4, with 12, while the median ⟦R^{2}⟧ is 0.99 under both. The corrections move the two accounts modestly towards consistency.")
S[78] = rep(spec_results.S[78], "in 23 of 39 countries (Supplementary Figure 14)", "in 23 of 39 countries and than M0 in 27")
s86 = rep(spec_results.S[86], "country values are reported in Supplementary Table 16", "country values are deposited with the replication files")
S[86] = rep(s86, "the country ranges in Supplementary Table 16 are", "the country-level ranges in the replication files are")
S[89] = rep(spec_results.S[89], "; Supplementary Figure 15", "")
S[95] = rep(spec_results.S[95], "implies adjustments below 1.1% of produced capital in all countries (Supplementary Table 4 and Supplementary Figure 9)",
            "implies upward revisions of at most 1.1% of 2019 produced capital in the 21 countries with ⟦β>0⟧")
S[107] = ("A natural objection is that ⟦μ(t)⟧ and ⟦β⟧ may not be separately identified from production data alone: a longer lag slows measured capital accumulation much as a smaller intangible share does. Section 4.4 shows that this concern is material for ⟦μ⟧. Three sources of discipline narrow, but do not remove, the problem.")
S[108] = rep(spec_disc.S[108], "is less flat than the production-only objective in most countries", "is less flat than the production-only objective in 21 of 39 countries (median share of near-minimal grid cells 0.13 versus 0.19)")
S[109] = rep(spec_disc.S[109], "(slope 0.068, t = 2.34 under M4; Supplementary Figure 3)", "(slope 0.068, heteroskedasticity-robust t = 2.09, ⟦R^{2}⟧ = 0.13 under M4; slope 0.054, t = 1.56 under M0)")
S[110] = rep(spec_disc.S[110], "stay within 2% of their baseline values (Supplementary Figure 12), so", "stay within 2% of their baseline values, and a uniform ±20% change in ⟦δ⟧ moves the mean lag from 1.61 to 1.52 years with the median unchanged at 0.26 years, so")
S[122] = ("Three caveats apply. First, our identification of ⟦β⟧ against CWON is only as clean as CWON itself, which combines national sources of heterogeneous quality; the treatment of land and sub-soil assets differs materially across countries (Lange et al., 2021, Chap. 2), and our quantity-based PIM cannot capture revaluations that CWON carries, plausibly including Japanese land prices. Separating revaluation from quantity effects would require sector-specific deflators, national land-price indices (Shimizu and Nishimura, 2007) and chained price indices for intangibles (Jorgenson et al., 2005). "
          "Second, the bootstrap and Monte Carlo evidence (Section 4.4) shows that ⟦μ⟧ is weakly identified and biased towards short lags; we do not claim point identification of country lags, and country-specific conclusions should be cross-checked with national-accounts micro-data. Third, the demographic-tempo analogy is suggestive but not exact: capital depreciates via ⟦δ⟧, which is itself a derived estimate in PWT and imprecisely measured in transition economies (Inklaar and Timmer, 2013). If ⟦δ⟧ drifts, some of what we attribute to ⟦μ(t)⟧ could be absorbed by depreciation; disentangling the two requires capacity-utilisation and retirement data that are not uniformly available across the 39 countries.")
SUBST = {50: [("are reported in the Supporting Information as intermediate benchmarks", "are intermediate benchmarks reported in Table I")],
         97: [(" (Supplementary Table 5)", "")]}
import spec_front as _F
_F.ABSTRACT = [(h, t + " Estimated lags are weakly identified, so the capital-level results use the parameter-free observable lag." if h == 'Originality' else t) for h, t in _F.ABSTRACT]
import spec_front as _sf
for _m in (_sf, spec_mid, spec_results, spec_disc):
    for _k, _v in _m.S.items():
        if isinstance(_v, str) and 'Borgo et al., 2013' in _v and 'Dal Borgo' not in _v:
            S[_k] = S.get(_k, _v).replace('Borgo et al., 2013', 'Dal Borgo et al., 2013')
