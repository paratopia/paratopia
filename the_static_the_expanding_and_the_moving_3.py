tetb = []
for window in range (k2, len(inin)):
    inin1, N1, r1, xhat1 = inin[:window], N[:window], r[:window], xhat[:window]
    res = minimize(theta, t0, method="Nelder-Mead", tol=1.e-12)
    tetb.append(res.x) 
