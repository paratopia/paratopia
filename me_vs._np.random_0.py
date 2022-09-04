import numpy as np
n = 30
mu = 1/n
sigma = 1
s = 100
seed = np.linspace(1, s, s)

randomwjul = []
randomwaug = []
for i in range(0, len(seed)):
    s = np.int(111*seed[i])
    np.random.seed(s)
    r = np.random.lognormal(mu, sigma, n)
    randomwjul.append(r/np.sum(r))
    s = np.int(222*seed[i])
    np.random.seed(s)
    r = np.random.lognormal(mu, sigma, n)
    randomwaug.append(r/np.sum(r))
