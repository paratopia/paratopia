import pandas as pd
inin = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
adj = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
mass = pd.read_csv("massppp.csv", delimiter=";", index_col=("Date")).values

import numpy as np
ret = np.vstack([np.full((1, len(inin.T)), np.nan), (adj[1:,]/adj[:-1])-1])   
dolvol = np.log(adj*mass)
beta = pd.read_csv("mktppp.csv", delimiter=",").values
mom = list(map(lambda i: ((1+ret[i-13:i-1,]).cumprod(axis=0)-1)[-1], range(13, len(ret))))
mom = np.vstack([np.full((13, len(inin.T)), np.nan), np.array(mom)]) 

k1 = 16
adj, ret = adj[k1+1:,], ret[k1+1:,]
inin, dolvol, beta, mom = inin[:-1][k1:,], dolvol[:-1][k1:,], beta[:-1][k1:,], mom[:-1][k1:,]

N = []
r = []
dolz = []
betz = []
momz = []
for i in range(len(inin)):
    ini = np.isnan(inin[i])==False
    N.append(np.size(inin[i][ini]))
    r.append(np.nan_to_num(ret[i][ini]))
    dol = (dolvol[i][ini]-np.nanmean(dolvol[i][ini]))/np.nanstd(dolvol[i][ini])
    bet = (beta[i][ini]-np.nanmean(beta[i][ini]))/np.nanstd(beta[i][ini])
    mo = (mom[i][ini]-np.nanmean(mom[i][ini]))/np.nanstd(mom[i][ini])
    dolz.append(np.array([np.nan_to_num(dol)]))
    betz.append(np.array([np.nan_to_num(bet)]))
    momz.append(np.array([np.nan_to_num(mo)]))

k2 = 92
inin1, N1, r1, dolz1, betz1, momz1 = inin[:k2], N[:k2], r[:k2], dolz[:k2], betz[:k2], momz[:k2]   
inin2, N2, r2, dolz2, betz2, momz2, adj = inin[k2:,], N[k2:], r[k2:], dolz[k2:], betz[k2:], momz[k2:], adj[k2:,]
