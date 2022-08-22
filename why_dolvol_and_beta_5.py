rdol = list(map(lambda i: np.dot(wdol[i], r2[i]), range(len(inin2))))
rbet = list(map(lambda i: np.dot(wbet[i], r2[i]), range(len(inin2))))
rmom = list(map(lambda i: np.dot(wmom[i], r2[i]), range(len(inin2))))
rdolbet = list(map(lambda i: np.dot(wdolbet[i], r2[i]), range(len(inin2))))
rdolmom = list(map(lambda i: np.dot(wdolmom[i], r2[i]), range(len(inin2))))
rbetmom = list(map(lambda i: np.dot(wbetmom[i], r2[i]), range(len(inin2))))
rdolbetmom = list(map(lambda i: np.dot(wdolbetmom[i], r2[i]), range(len(inin2))))

rfr = pd.read_csv("rfppp.csv", delimiter=";", index_col="Date").values  
rfr = rfr[len(rfr)-len(rdol):]      
rdol, rbet, rmom, rdolbet, rdolmom, rbetmom, rdolbetmom = rdol-rfr.T, rbet-rfr.T, rmom-rfr.T, rdolbet-rfr.T, rdolmom-rfr.T, rbetmom-rfr.T, rdolbetmom-rfr.T
