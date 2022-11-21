ww = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(dolz2[i].T, teta[i]))))), range(len(inin2))))

bud = 5000
w = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    w.append(np.round((ww[i]*bud)/adj[i][inx])*adj[i][inx]/bud)
    
r = list(map(lambda i: np.dot(w[i], r2[i]), range(len(inin2))))
