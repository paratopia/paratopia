from scipy.optimize import minimize
rho = 5

def theta(t): 
  tet = np.array([t[0], t[1]])
  u = [((1+np.dot(np.exp(np.log((1/N1[i])*(1+np.dot(xhat1[i].T, tet)))), r1[i]))**(1-rho))/(1-rho) for i in range(len(inin1))]
  return - np.mean(u)
t0 = 2*[0/2]
res = minimize(theta, t0, method="Nelder-Mead")
teta = np.full((len(inin2), len(res.x)), res.x)
