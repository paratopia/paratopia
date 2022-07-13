dolvol = np.log(adj*vol)[1:]
dolvol[dolvol==-np.inf] = np.nan
