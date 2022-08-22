xhata=[]
xhatb=[]
xhatc=[]
xhatd=[]
for i in range(len(inin)):
    ini= np.isnan(inin[i])==False
    dol=(dolvol[i][ini]-np.nanmean(dolvol[i][ini]))/np.nanstd(dolvol[i][ini])
    bet=(beta[i][ini]-np.nanmean(beta[i][ini]))/np.nanstd(beta[i][ini])
    mo=(mom[i][ini]-np.nanmean(mom[i][ini]))/np.nanstd(mom[i][ini])
    xhata.append(np.array([np.nan_to_num(dol), np.nan_to_num(bet)]))
    xhatb.append(np.array([np.nan_to_num(dol), np.nan_to_num(mo)]))
    xhatc.append(np.array([np.nan_to_num(bet), np.nan_to_num(mo)]))
    xhatd.append(np.array([np.nan_to_num(dol), np.nan_to_num(bet), np.nan_to_num(mo)]))   
     
k2 = 92
xhata1, xhatb1, xhatc1, xhatd1 = xhata[:k2], xhatb[:k2], xhatc[:k2], xhatd[:k2]    
xhata2, xhatb2, xhatc2, xhatd2 = xhata[k2:], xhatb[k2:], xhatc[k2:], xhatd[k2:]
