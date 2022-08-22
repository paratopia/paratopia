twofactors1 = xhata1
def theta2(t): 
    tet = np.array([t[0], t[1]])
    u = [((1+np.dot(np.exp(np.log((1/N1[i])*(1+np.dot(twofactors1[i].T, tet)))), r1[i]))**(1-rho))/(1-rho) for i in range(len(inin1))]
    return - np.mean(u)
t0 = 2*[0/2]
res2 = minimize(theta2, t0, method="Nelder-Mead")

threefactors1 = xhatd1
def theta3(t): 
    tet = np.array([t[0], t[1], t[2]])
    u = [((1+np.dot(np.exp(np.log((1/N1[i])*(1+np.dot(threefactors1[i].T, tet)))), r1[i]))**(1-rho))/(1-rho) for i in range(len(inin1))]
    return - np.mean(u)
t0 = 3*[0/3]
res3 = minimize(theta3, t0, method="Nelder-Mead")

twofactors2 = xhata2
wdolbet1 = list(map(lambda i: (1/N2[i])*(1+np.dot(twofactors2[i].T, res2.x)), range(len(inin2))))
threefactors2 = xhatd2
wdolbetmom1 = list(map(lambda i: (1/N2[i])*(1+np.dot(threefactors2[i].T, res3.x)), range(len(inin2))))

wdolbet = []
wdolbetmom = []
for i in range(len(inin2)):
    inx = np.isnan(inin2[i])==False
    wdolbet.append(np.round((wdolbet1[i]*bud)/adj[i][inx])*adj[i][inx]/bud)
    wdolbetmom.append(np.round((wdolbetmom1[i]*bud)/adj[i][inx])*adj[i][inx]/bud)
