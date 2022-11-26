ww = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T, teta[i]))))), range(len(inin2))))
bud = 5000*1/ww[-1].sum()

inv = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    inv.append(np.round((ww[i]*bud)/adj[i][inx]))
