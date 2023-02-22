# method I
waa_i = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_a[i]))))),range(len(inin2))))
wbb_i = list(map(lambda i: np.nan_to_num(np.exp(np.log((1/N2[i])*(1+np.dot(x2[i].T,teta_b[i]))))),range(len(inin2))))
