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

plt.show()
plt.clf()

print("The network is a power-law")
print("G is a directed graph with unweighted links")
print("The network is weakly connected")
print("The network is highly clustered")

bin_edges=np.logspace(np.log10(kmin),np.log10(kmax),num=20)
density,_=np.histogram(degrees,bins=bin_edges,density=True)
fig=plt.figure(figsize=(6,4))
log_be=np.log10(bin_edges)
x=10**((log_be[1:]+log_be[:-1])/2)
plt.loglog(x,density,marker='o',linestyle='none')
plt.xlabel(r"degree $k$",fontsize=16)
plt.ylabel(r"$P(k)$",fontsize=16)
plt.show()
plt.clf()

fig=plt.figure(figsize=(10,10))
nx.draw_spring(G, node_size=20, node_color="purple")
plt.show()
plt.clf()

print("Is connected: ", nx.is_connected(G))

sorted_components=sorted(nx.connected_components(G), key=len, reverse=True)
print("There are", nx.number_connected_components(G)," connected components, the largest one has",len(sorted_components[0]),"nodes.")

diameter=nx.diameter(G)
print("Diameter =", diameter)

avg_dist=nx.average_shortest_path_length(G)
print("Average shortest path length =", avg_dist)

density=nx.density(G)
print("Edge density in G =", density)

print("Avg clustering coefficient:", nx.average_clustering(G))

#Distribution of the clustering coefficient
cc=nx.clustering(G)
vcc=[]
for n in G.nodes():
    vcc.append(nx.clustering(G, n))
vcc=np.array(vcc)
plt.hist(cc.values(), bins=10, density=True)
plt.grid(True)
plt.title("Distribution of the clustering coefficient")
plt.xlabel("Clustering coefficient (cc)")
plt.ylabel("P(cc)")
plt.show()
plt.clf()

# Betweenness centrality
betweenness_centrality=nx.betweenness_centrality(G)
degree_centrality=nx.degree_centrality(G)
plt.scatter(list(betweenness_centrality.values()),list(degree_centrality.values()))
plt.xlabel("Betweenness Centrality")
plt.ylabel("Degree Centrality")
plt.show()
plt.clf()

#Most important 5 nodes
dc_sorted=sorted(degree_centrality.items(),key=lambda item:item[1],reverse=True)
print("Most important 5 nodes according to degree centrality are:")
for i in range(5):
    print(dc_sorted[i])

bc_sorted=sorted(betweenness_centrality.items(),key=lambda item:item[1],reverse=True)
print("Most important 5 nodes according to betweenness centrality are:")
for i in range(5):
    print(bc_sorted[i])

#Closeness centrality
closeness_centrality=nx.closeness_centrality(G)
cc_sorted=sorted(closeness_centrality.items(),key=lambda item:item[1],reverse=True)
print("Most important 5 nodes according to closeness centrality are:")
for i in range(5):
    print(cc_sorted[i])
plt.scatter(list(closeness_centrality.values()),list(degree_centrality.values()))
plt.xlabel("Closeness Centrality")
plt.ylabel("Degree Centrality")
plt.show()
plt.clf()

#Eigenvector centrality
eigen_centrality=nx.eigenvector_centrality(G)
ec_sorted=sorted(eigen_centrality.items(),key=lambda item:item[1],reverse=True)
print("Most important 5 nodes according to eigenvector centrality are:")
for i in range(5):
    print(ec_sorted[i])
plt.scatter(list(eigen_centrality.values()),list(degree_centrality.values()))
plt.xlabel("Eigenvector Centrality")
plt.ylabel("Degree Centrality")
plt.show()
plt.clf()

#Vizualization
fig=plt.figure(figsize=(8,8))
nx.draw_spring(G,node_size=100)
plt.show()