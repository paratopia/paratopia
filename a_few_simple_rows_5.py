from scipy.optimize import minimize
N = 5
gam = 5
def theta(t): 
    tet = np.array([t[0], t[1]])
    w = list(map(lambda i:(1/N)*(1+np.dot(xhat[i].T, tet)), range(len(adj))))
    pr = list(map(lambda i:np.dot(np.exp(np.log(w[i])), ret[i]),                                      
    range(len(adj))))
    u = list(map(lambda i:((1+pr[i])**(1-gam))/(1-gam), range(len(adj))))
    return -np.mean(u)
t0 = 2*[0/2]
res = minimize(theta, t0, method="Nelder-Mead")
