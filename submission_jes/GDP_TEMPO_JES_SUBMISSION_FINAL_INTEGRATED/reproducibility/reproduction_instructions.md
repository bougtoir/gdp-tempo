# Reproduction instructions (verified 2026-10-16, fresh clone, no private data)
git clone https://github.com/bougtoir/gdp-tempo-paper
cd gdp-tempo-paper
make setup
make reproduce-analysis
# -> ends with "Complete reproduction passed" (reproduction/reproduction_report.json)
# Verified outputs: 23/23 tracked metrics identical, incl. K-gap median -4.29%,
# TFP/LS medians ±1.7pp, OOS M0 4.60%/M2 3.99%, Wilcoxon p=0.1756 (n=39),
# bootstrap mu excludes 0 in 39/39, beta in 7/39, CWON holdout joint 4.1% best.
# Cross-country uncertainty (new):
python scripts/cross_country_uncertainty.py   # B=10,000, seed=20261016
