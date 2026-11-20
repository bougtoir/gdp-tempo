S = {}
S[19] = "3. Framework"
S[20] = "3.1 Flow-side production function with a drifting lag"
S[27] = ("where ⟦μ_{1}⟧ is the drift, or tempo, of the mean lag in the sense of Bongaarts and Feeney (1998). A positive ⟦μ_{1}⟧ means that typical projects take longer to become productive, for example because more investment is in software, R&D platforms or complex systems.")
S[28] = "3.2 Flow–stock joint loss"
S[34] = "3.3 Quantum–tempo correspondence"
S[35] = ("Supplementary Table 1 maps the demographic quantities analysed by Bongaarts and Feeney (1998) and Goldstein et al. (2003) onto their capital-accounting counterparts: investment corresponds to births, the PIM stock to the population stock, ⟦μ(t)⟧ to the mean age at childbearing and ⟦β⟧ to the omitted quantity parameter.")
S[36] = "3.4 Relational PIM diagnostic"
S[40] = ("Values ⟦ρ_{2}=1⟧ and ⟦ρ_{1}=0⟧ indicate that the two accounts measure the same latent stock up to noise; ⟦ρ_{2}<1⟧ (⟦ρ_{2}>1⟧) indicates that the PIM understates (overstates) capital growth relative to CWON; and ⟦ρ_{1}≠0⟧ indicates a level difference arising from base-year calibration, price conversion or asset coverage.")
S[41] = None
S[42] = None
S[43] = ("The diagnostic, adapted from the relational models of Brass (1971), does not treat CWON as truth: it parameterises the relationship between two estimates of the same latent stock and can be computed for each model, so that movement of ⟦ρ_{2}⟧ towards unity is a check on whether the corrections bring the accounts closer together.")
S[44] = "4. Data and methods"
S[49] = "4.2 Models M0, M2, M4 and M_obs"
S[54] = ("•  M_obs: observable tempo, ⟦μ_{obs}(t)=Σ_{a}s_{a}(t)μ_{a}⟧, where ⟦s_{a}(t)⟧ is the share of asset ⟦a⟧ in OECD GFCF and ⟦μ_{a}⟧ is a literature-based gestation lag (dwellings and other buildings 2.0 years; transport equipment 0.5; ICT equipment 0.3; other machinery 0.8; intellectual property products 3.0). M_obs has no free parameters. Scaling all asset lags by 0.5–2.0 gives a median out-of-sample MAPE between 3.86% and 4.39% (Supplementary Table 2). This is a calibration-sensitivity range, not a confidence interval, and the capital-level results below remain conditional on the calibrated lags.")
S[56] = ("We evaluate each model by (i) the level MAPE of fitted against observed log-GDP after removing decade-mean TFP; (ii) the root-mean-squared error (RMSE) of one-year log-GDP growth, in percentage points; and (iii) the out-of-sample level MAPE, with parameters fitted on 1970–2014 and levels predicted for 2015–2019 using a training-window TFP projection and observed holdout inputs. Lower values are better.")
S[57] = None
S[58] = None
S[59] = None
S[60] = "4.3 Estimation by grid search"
S[61] = ("All models are estimated by grid search rather than gradient methods, because the geometric lag kernel makes the objective non-convex when ⟦μ⟧ is small and because explicit objective surfaces are needed for the sensitivity checks. The grids have 25 points for ⟦μ⟧ on [0.01, 6.0] years, 18 points for ⟦β⟧ on [0, 0.34] and 11 points for ⟦μ_{1}⟧ on [−0.08, 0.12] per year, bracketing values reported in prior cross-country studies (Kaboski, 2005; Corrado et al., 2016). Under the constant-lag model M1, 25 of the 39 countries reach a grid boundary for ⟦μ⟧ (18 at the lower and 7 at the upper bound); Supplementary Section S.14 reports out-of-sample results for the 14 interior solutions. The anchor year ⟦t_{0}⟧ is 1970 for all countries.")
S[62] = "4.4 Within-country bootstrap"
S[63] = ("For each country we residual-bootstrap the M4 growth residuals 100 times (block size 1; block size 3 gave nearly identical intervals in a five-country pilot), rebuild synthetic output, investment, R&D and capital series, and re-run the joint grid. We report 95% percentile intervals without multiple-testing adjustment; a Bonferroni threshold of 5%/39 would be more conservative and would reduce the counts below. At the 5% level, the interval for ⟦μ⟧ excludes zero in 39 of 39 countries and that for ⟦β⟧ in 7 countries. Intervals are widest for short or post-transition series such as Estonia, Latvia and Chile.")
