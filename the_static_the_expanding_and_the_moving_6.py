rfr = pd.read_csv("rfppp.csv", delimiter=";", index_col="Date").values  
rfr = rfr[len(rfr)-len(teta):]      

ra, rb, rc = ra-rfr.T, rb-rfr.T, rc-rfr.T
exr = np.array([np.mean(ra), np.mean(rb), np.mean(rc)]) 
vol = np.array([np.std(ra), np.std(rb), np.std(rc)])
sr = exr/vol

ff5 = pd.read_csv("ff5ppp.csv", delimiter=";", index_col="Date").values
ff5 = ff5[len(ff5)-len(teta):]

import statsmodels.api as sm
exog = sm.add_constant(sm.add_constant(ff5))

mod = sm.OLS(ra.T, exog)
alpa = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rb.T, exog)
alpb = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
mod = sm.OLS(rc.T, exog)
alpc = mod.fit(cov_type='HAC', cov_kwds={'maxlags':1})
ar = np.array([alpa.params[0], alpb.params[0], alpc.params[0]])
