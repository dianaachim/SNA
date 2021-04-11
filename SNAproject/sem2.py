import collections

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'E')
G.add_edge('B', 'E')
G.add_edge('B', 'F')
G.add_edge('E', 'G')
G.add_edge('G', 'C')
G.add_edge('F', 'C')
G.add_edge('C', 'D')
G.add_edge('C', 'H')
G.add_edge('D', 'H')

print("Diameter:", nx.diameter(G))
print("Shortest path length", nx.average_shortest_path_length(G))

print("Density", nx.density(G))

degree_sequence = sorted([d for n, d in nx.degree(G)], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
plt.bar(deg, cnt, width=0.80, color="b")
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

nx.draw(G, with_labels=True, node_color="lightgreen", node_size=500)
plt.show()
plt.draw()


