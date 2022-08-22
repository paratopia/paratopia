import statsmodels.api as sm
ff5 = pd.read_csv("ff5ppp.csv", delimiter=";", index_col="Date").values
ff5 = ff5[len(ff5)-len(rdol.T):]
exog = sm.add_constant(sm.add_constant(ff5))

mod = sm.OLS(rdol.T, exog)
ardol = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rbet.T, exog)
arbet = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rmom.T, exog)
armom = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rdolbet.T, exog)
ardolbet = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rdolmom.T, exog)
ardolmom = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rbetmom.T, exog)
arbetmom = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rdolbetmom.T, exog)
ardolbetmom = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})

ar = np.array([ardol.params[0], arbet.params[0], armom.params[0], ardolbet.params[0], ardolmom.params[0], arbetmom.params[0], ardolbetmom.params[0]])*100
prtin(ar)
[0.92094106, 0.6667883, 0.67995251, 0.90940689, 0.8310025, 0.72960523, 0.86917452]
