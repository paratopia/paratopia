rho = 5
def jac(t, i): 
    tet = np.array([t[0]])
    wo = (1/N1[i])*(1+np.dot(dolz1[i].T, tet))
    pr = np.dot(wo, r1[i])
    return ((1+pr)**(1-rho))/(1-rho)

import autograd.numpy as np 
from autograd import grad
dj = grad(jac, 0)
