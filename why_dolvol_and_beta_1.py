from scipy.optimize import minimize
rho = 5
onefactor1 = dolz1

def theta1(t): 
    tet = np.array([t[0]])
    u = [((1+np.dot(np.exp(np.log((1/N1[i])*(1+np.dot(onefactor1[i].T, tet)))), r1[i]))**(1-rho))/(1-rho) for i in range(len(inin1))]
    return - np.mean(u)
t0 = 1*[0/1]
res1 = minimize(theta1, t0, method="Nelder-Mead")
