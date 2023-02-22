# weigths
bud = 5000
wa_i = []
wa_ii = []
wb_i = []
wb_ii = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    wa_i.append(((np.round((waa_i[i]*bud)/adj[i][inx]))*adj[i][inx])/((np.round((waa_i[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    wa_ii.append(((np.round((waa_ii[i]*bud)/adj[i][inx]))*adj[i][inx])/((np.round((waa_ii[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    wb_i.append(((np.round((wbb_i[i]*bud)/adj[i][inx]))*adj[i][inx])/((np.round((wbb_i[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())
    wb_ii.append(((np.round((wbb_ii[i]*bud)/adj[i][inx]))*adj[i][inx])/((np.round((wbb_ii[i]*bud)/adj[i][inx]))*adj[i][inx]).sum())

# returns
ra_i = np.array(list(map(lambda i: np.dot(wa_i[i],r2[i]),range(len(inin2)))))
ra_ii = np.array(list(map(lambda i: np.dot(wa_ii[i],r2[i]),range(len(inin2)))))
rb_i = np.array(list(map(lambda i: np.dot(wb_i[i],r2[i]),range(len(inin2)))))
rb_ii = np.array(list(map(lambda i: np.dot(wb_ii[i],r2[i]),range(len(inin2)))))
