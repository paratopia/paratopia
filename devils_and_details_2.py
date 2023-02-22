# thetas
def jac2(t,i): 
    tet = np.array([t[0],t[1]])
    wo = (1/N2[i])*(1+np.dot(x2[i].T,tet))
    pr = np.dot(wo,r2[i])
    return ((1+pr)**(1-rho))/(1-rho)

dj2 = grad(jac2,0)  

omega_a, omega_b = np.array([res_a.x[0],res_a.x[3]]), np.array([res_b.x[0],res_b.x[3]])
alpha_a, alpha_b = np.array([res_a.x[2],res_a.x[5]]), np.array([res_b.x[2],res_b.x[5]]) 
beta_a, beta_b = np.array([res_a.x[1],res_a.x[4]]), np.array([res_b.x[1],res_b.x[4]]) 
tets_a, tets_b = np.zeros((len(inin2),2)), np.zeros((len(inin2),2))
tet_a, tet_b = gas_a(res_a.x,True)[-1], gas_b(res_b.x,True)[-1]
for i in range(0,len(inin2)):
    tets_a[i,:] = tet_a
    tets_b[i,:] = tet_b
    S_a = dj2(tet_a,i)
    S_b = dj2(tet_b,i)
    tet_a = omega_a+(tet_a-omega_a)*beta_a+alpha_a*S_a 
    tet_b = omega_b+(tet_b-omega_b)*beta_b+alpha_b*S_b 
teta_a, teta_b = tets_a, tets_b 
