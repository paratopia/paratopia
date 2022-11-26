N = []
r = []
x = []
for i in range(len(inin)):
    inx = np.isnan(inin[i])==False
    N.append(np.size(inin[i][inx]))
    r.append(np.nan_to_num(ret[i][inx]))
    dv = (dolvol[i][inx]-np.nanmean(dolvol[i][inx]))/np.nanstd(dolvol[i][inx])
    mm = (mom[i][inx]-np.nanmean(mom[i][inx]))/np.nanstd(mom[i][inx])
    x.append(np.array([np.nan_to_num(dv), np.nan_to_num(mm)]))

k2 = 258
inin1, N1, r1, x1 = inin[:k2], N[:k2], r[:k2], x[:k2]  
inin2, N2, r2, x2, adj = inin[k2:,], N[k2:], r[k2:], x[k2:], adj[k2:,] 
