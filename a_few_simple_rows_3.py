import statsmodels.api as sm
qs = pd.read_csv("ff5.csv", delimiter=";", index_col="Date").values
window = 16
beta = []
for i in range(0, len(ret.T)):
    bet = []
    for t in range(window, len(ret)):
        exog = sm.add_constant(sm.add_constant(qs[t-window:t])
        endog = ret.T[i][t-window:t]
        mod = sm.OLS(endog, exog)
        res = mod.fit(cov_type="HAC", cov_kwds={"maxlags":1})
        p1 = res.params[1]
        bet.append(p1)
    beta.append(bet)
beta = np.array(beta).T
