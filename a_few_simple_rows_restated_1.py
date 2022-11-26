import numpy as np
import pandas as pd
inin = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
adj = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
mass = pd.read_csv("massppp.csv", delimiter=";", index_col=("Date")).values

ret = np.vstack([np.full((1, len(inin.T)), np.nan), (adj[1:,]/adj[:-1])-1])     
dolvol = np.log(adj*mass)
dolvol[dolvol==-np.inf] = np.nan

mom = list(map(lambda i: ((1+ret[i-13:i-1,]).cumprod(axis=0)-1)[-1], range(13, len(ret))))
mom = np.vstack([np.full((13, len(np.array(mom).T)), np.nan), np.array(mom)]) 

k1 = 16
adj, ret = adj[k1+1:,], ret[k1+1:,]
inin, dolvol, mom = inin[:-1][k1:,], dolvol[:-1][k1:,], mom[:-1][k1:,]
