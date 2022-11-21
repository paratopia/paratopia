import pandas as pd
inin = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
adj = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
mass = pd.read_csv("massppp.csv", delimiter=";", index_col=("Date")).values

import numpy as np
ret = np.vstack([np.full((1, len(inin.T)), np.nan),(adj[1:,]/adj[:-1])-1])   
dolvol = np.log(adj*mass)

k1 = 16
adj, ret = adj[k1+1:,], ret[k1+1:,]
inin, dolvol = inin[:-1][k1:,], dolvol[:-1][k1:,]

N = []
r = []
dolz = []
for i in range(len(inin)):
    ini = np.isnan(inin[i])==False
    N.append(np.size(inin[i][ini]))
    r.append(np.nan_to_num(ret[i][ini]))
    dol = (dolvol[i][ini]-np.nanmean(dolvol[i][ini]))/np.nanstd(dolvol[i][ini])
    dolz.append(np.array([np.nan_to_num(dol)]))
     
k2 = 92
inin1, N1, r1, dolz1 = inin[:k2], N[:k2], r[:k2], dolz[:k2]   
inin2, N2, r2, dolz2, adj = inin[k2:,], N[k2:], r[k2:], dolz[k2:], adj[k2:,]
