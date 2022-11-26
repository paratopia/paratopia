def jac2(t, i): 
    tet = np.array([t[0], t[1]])
    w = (1/N2[i])*(1+np.dot(x2[i].T, tet))
    pr = np.dot(wo, r2[i])
    return ((1+pr)**(1-rho))/(1-rho)
dj2 = grad(jac2, 0)  
