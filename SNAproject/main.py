import matplotlib.pyplot as plt
import numpy as np
import collections
import networkx as nx

G=nx.read_edgelist("data/soc-wiki-Vote.mtx", comments='%', create_using=nx.Graph(), delimiter=' ', nodetype=int, encoding='utf-8')

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

degree_sequence = sorted([d for n, d in nx.degree(G)], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
plt.bar(deg, cnt, width=0.80, color="b")
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

# nx.draw(G, with_labels=True, node_color="lightgreen", node_size=500)
plt.show()
# plt.draw()