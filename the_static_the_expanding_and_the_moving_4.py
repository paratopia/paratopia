window48 = 48
tetc = []
for window in range(window48, len(inin)):
    inin1, N1, r1, xhat1 = inin[window-window48:window], N[window-window48:window], r[window-window48:window], xhat[window-window48:window]
    res = minimize(theta, t0, method="Nelder-Mead", tol=1.e-12)
    tetc.append(res.x)  
tetc = tetc[len(tetc)-len(teta):]
