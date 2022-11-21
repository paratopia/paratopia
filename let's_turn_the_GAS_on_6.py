tet = gas(res.x, True)[-1]
tets = np.zeros((len(inin2), 1))
for i in range(0, len(inin2)):
    tets[i,:] = tet
    S = dj2(tet, i)
    tet = omega+(tet-omega)*beta+alpha*S 
teta = tets 
