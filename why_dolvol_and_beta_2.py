onefactor2 = dolz2
wdol1 = list(map(lambda i: (1/N2[i])*(1+np.dot(onefactor2[i].T,res1.x)),range(len(inin2))))

bud = 5000
wdol = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    wdol.append(np.round((wdol1[i]*bud)/adj[i][inx])*adj[i][inx]/bud)
