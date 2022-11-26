rho = 5
def jac(t, i): 
    tet = np.array([t[0], t[1]])
    w = (1/N1[i])*(1+np.dot(x1[i].T, tet))
    pr = np.dot(w, r1[i])
    return ((1+pr)**(1-rho))/(1-rho)

import autograd.numpy as np 
from autograd import grad
dj = grad(jac, 0)     
