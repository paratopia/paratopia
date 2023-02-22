# method II
waa_ii = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_a[i])))))
             /np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_a[i]))))).sum(),range(len(inin2))))
wbb_ii = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_b[i])))))
             /np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_b[i]))))).sum(),range(len(inin2))))
