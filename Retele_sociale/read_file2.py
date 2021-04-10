import collections

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

f = open("example_2.txt", "rb")
G = nx.read_edgelist(f)
f.close()


def logscale():
    fig = plt.figure(figsize=(6, 4))
    degree_sequence = sorted([d for n, d in nx.degree(G)], reverse=True)
    y, bin_edges = np.histogram(degree_sequence, density=True, bins=10)
    x = [(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(bin_edges) - 1)]
    plt.loglog(x, y, marker="o", markersize=10, color="r", linestyle='none')
    plt.xlabel(r"degree $k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.show()


def normalScale():
    degree_sequence = sorted([d for n, d in nx.degree(G)], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    plt.bar(deg, cnt, width=0.80, color="b")
    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    plt.show()


logscale()
