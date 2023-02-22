# data
import pandas as pd
inin = pd.read_csv("ininppp.csv",delimiter=";",index_col=("Date")).values
adj = pd.read_csv("adjcloseppp.csv",delimiter=";",index_col=("Date")).values
mass = pd.read_csv("massppp.csv",delimiter=";",index_col=("Date")).values

# returns, dolvol, and momentum
import numpy as np
ret = np.vstack([np.full((1,len(inin.T)),np.nan),(adj[1:,]/adj[:-1])-1])     
dolvol = np.log(adj*mass)
mom = list(map(lambda i: ((1+ret[i-13:i-1,]).cumprod(axis=0)-1)[-1],range(13,len(ret))))
mom = np.vstack([np.full((13,len(np.array(mom).T)),np.nan),np.array(mom)]) 

k1 = 16
adj, ret = adj[k1:,], ret[k1:,]
inin, dolvol, mom = inin[k1:,], dolvol[k1:,], mom[k1:,]

# x matrix
N = []
r = []
x = []
for i in range(len(inin)):
    inx = np.isnan(inin[i])==False
    N.append(np.size(inin[i][inx]))
    r.append(np.nan_to_num(ret[i][inx]))
    dv = (dolvol[i][inx]-np.nanmean(dolvol[i][inx]))/np.nanstd(dolvol[i][inx])
    mm = (mom[i][inx]-np.nanmean(mom[i][inx]))/np.nanstd(mom[i][inx])
    x.append(np.array([np.nan_to_num(dv),np.nan_to_num(mm)]))

# samples
k2 = 131
inin1, N1, r1, x1 = inin[:k2], N[:k2], r[:k2], x[:k2]   
inin2, N2, r2, x2, adj = inin[k2:,], N[k2:], r[k2:], x[k2:], adj[k2:,]

# scaled score function
rho = 5
def jac(t,i): 
   tet = np.array([t[0],t[1]])
   wo = (1/N1[i])*(1+np.dot(x1[i].T,tet))
   pr = np.dot(wo,r1[i])
   return ((1+pr)**(1-rho))/(1-rho)

import autograd.numpy as np 
from autograd import grad   
dj = grad(jac,0)     

# model A
from scipy.optimize import minimize
def gas_a(p,returnme=False): 
    omega = np.array([p[0],p[3]])
    beta = np.array([p[1],p[4]]) 
    alpha = np.array([p[2],p[5]])   
    tets = np.zeros((len(inin1),2))
    tet = omega
    for i in range(0,len(inin1)):
        tets[i,:] = tet
        S = dj(tet,i)
        tet = omega+(tet-omega)*beta+alpha*S
    w = list(map(lambda i: np.exp(np.log((1/N1[i])*(1+np.dot(x1[i].T,tets[i,:])))),range(len(inin1))))
    pr = list(map(lambda i: np.dot(np.nan_to_num(w[i]),r1[i]),range(len(inin1))))
    u = list(map(lambda i: ((1+pr[i])**(1-rho))/(1-rho),range(len(inin1))))
    if returnme == True:
        return tets
    return -np.mean(u)

bnds = ((-np.inf,np.inf),(0,1),(0,100),(-np.inf,np.inf),(0,1),(0,100))
x0 = [0.01,0.98,10,-0.00,0.98,10]
res_a = minimize(gas_a,x0,method="Nelder-Mead",bounds=bnds)
