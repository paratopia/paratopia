waa = list(map(lambda i: (1/N2[i])*(1+np.dot(xhat2[i].T, teta[i])), range(len(inin2))))
wbb = list(map(lambda i: (1/N2[i])*(1+np.dot(xhat2[i].T, tetb[i])), range(len(inin2))))
wcc = list(map(lambda i: (1/N2[i])*(1+np.dot(xhat2[i].T, tetc[i])), range(len(inin2))))

bud = 5000

wa = []
wb = []
wc = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    inva = np.round((waa[i]*bud)/adj[i][inx])
    invb = np.round((wbb[i]*bud)/adj[i][inx])
    invc = np.round((wcc[i]*bud)/adj[i][inx])
    wa.append(inva*adj[i][inx]/bud)
    wb.append(invb*adj[i][inx]/bud)
    wc.append(invc*adj[i][inx]/bud)
    
ra = list(map(lambda i: np.dot(wa[i], r2[i]), range(len(inin2))))
rb = list(map(lambda i: np.dot(wb[i], r2[i]), range(len(inin2))))
rc = list(map(lambda i: np.dot(wc[i], r2[i]), range(len(inin2))))
