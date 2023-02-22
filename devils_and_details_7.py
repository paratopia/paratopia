# actuall investment size
sizea_i = []
sizea_ii = []
sizeb_i = []
sizeb_ii = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    sizea_i.append(((np.round((waa_i[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    sizea_ii.append(((np.round((waa_ii[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    sizeb_i.append(((np.round((wbb_i[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    sizeb_ii.append(((np.round((wbb_ii[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
