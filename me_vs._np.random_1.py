import pandas as pd
adj = pd.read_csv("adjcloseppp.csv", delimiter=";", index_col=("Date")).values
jul = adj[271:272]
aug = adj[272:273]

bud = 5000
randomin4jul = [np.round((randomwjul[i]*bud)/jul) for i in range(0, len(seed))]
randomin8aug = [np.round((randomwaug[i]*bud)/aug) for i in range(0, len(seed))]
