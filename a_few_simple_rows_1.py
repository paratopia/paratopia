import numpy as np
adj = df["Adj Close"].values
vol = df["Volume"].values
ret = adj[1:,]/adj[:-1]-1
