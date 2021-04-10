import string

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import collections

G=nx.read_edgelist("data/soc-youtube.mtx", comments='%', create_using=nx.Graph(), delimiter=' ', nodetype=int, encoding='utf-8')

degrees=[G.degree[node]for node in G]

N=len(G)
L=G.size()

kmin=np.min(degrees)
kmax=np.max(degrees)
kavg=np.mean(degrees)

print("N=", N)
print("L=", L)

print("Average degree=", kavg)
print("Min degree=", kmin)
print("Max degree=", kmax)

#degree distribution