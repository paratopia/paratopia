adj = adj[len(adj)-len(beta):]
ret = ret[len(ret)-len(beta):]
dolvol = dolvol[len(dolvol)-len(beta):]
xhat = []
for i in range(len(adj)):
    dolz = (dolvol[i]-np.nanmean(dolvol[i]))/np.nanstd(dolvol[i])
    betz = (beta[i]-np.nanmean(beta[i]))/np.nanstd(beta[i])
    xhat.append(np.array([np.nan_to_num(dolz), np.nan_to_num(betz)]))  
