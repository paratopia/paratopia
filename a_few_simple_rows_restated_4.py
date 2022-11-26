from scipy.optimize import minimize
def gas(p, returnme=False): 
    omega = np.array([p[0], p[3]])
    beta = np.array([p[1], p[4]]) 
    alpha = np.array([p[2], p[5]])   
    tets = np.zeros((len(inin1), 2))
    tet = omega
    for i in range(0, len(inin1)):
        tets[i,:] = tet
        S = dj(tet, i)
        tet = omega + (tet - omega)*beta + alpha*S
    w = list(map(lambda i: (1/N1[i])*(1+np.dot(x1[i].T, tets[i,:])), range(len(inin1))))
    pr = list(map(lambda i: np.dot(np.nan_to_num(np.exp(np.log(w[i]))), r1[i]), range(len(inin1))))
    u = list(map(lambda i: ((1+pr[i])**(1-rho))/(1-rho), range(len(inin1))))
    if returnme==True:
        return tets
    return - np.mean(u)

bnds = ((-np.inf, np.inf), (0, 1), (0, 100), (-np.inf, np.inf), (0, 1), (0, 100))
#x0 = [0.0, 0.98, 10, 0.0, 0.98, 10]
x0 = [-0.002, 0.98, 10, 0.006, 0.98, 10]
res = minimize(gas, x0, method="Nelder-Mead", bounds=bnds)
