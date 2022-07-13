wa = (1/N)*(1+np.dot(xhat[-1].T, res.x))
print(wa)
[0.29999662 0.16793625 0.30643076 0.09730178 0.1283346]
bud = 5000
st = np.round(wa*bud/adj[-1])
print(st)
[1. 7. 9. 3. 4.]
wb = st*adj[-1]/bud
print(wb)
[0.2821 0.15778 0.323892 0.09513 0.13252]
