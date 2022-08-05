import pandas as pd
inin = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
adj = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
volume = pd.read_csv("volumeppp.csv", delimiter=";", index_col=("Date")).values

import numpy as np
ret = np.vstack([np.full((1, len(inin.T)), np.nan), (adj[1:,]/adj[:-1])-1])   
dolvol = np.log(adj*volume)
beta = pd.read_csv("betappp.csv", delimiter=",").values

k1 = 16
adj, ret = adj[k1+1:,], ret[k1+1:,]
inin, dolvol, beta = inin[:-1][k1:,], dolvol[:-1][k1:,], beta[:-1][k1:,]

N = []
r = []
xhat = []
for i in range(len(inin)):
  ini = np.isnan(inin[i])==False
  N.append(np.size(inin[i][ini]))
  r.append(np.nan_to_num(ret[i][ini]))
  dolz = (dolvol[i][ini]-np.nanmean(dolvol[i][ini]))/np.nanstd(dolvol[i][ini])
  betz = (beta[i][ini]-np.nanmean(beta[i][ini]))/np.nanstd(beta[i][ini])
  xhat.append(np.array([np.nan_to_num(dolz), np.nan_to_num(betz)]))
