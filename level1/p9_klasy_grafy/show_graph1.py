# Create a directed graph
from igraph import Graph, plot

from level1.p10_routes.graph_utils import default_style

"""
Zadanie: przedstawić graficznie drzewo zadane przez listę dzieci, 

gg = [[1, 2], [], [3, 4], [], []]
"""

gg = [[1, 2], [], [3, 4], [], []]
n = len(gg)

g = Graph(directed=True)
g.add_vertices(n)

# Add ids and labels to vertices
for i in range(n):
    g.vs[i]["id"] = i
    g.vs[i]["label"] = 'node' + str(i)


g.vs['color'] = (['green'] * n)  # kolory węzłów

# Add edges
edges = []
for i in range(n):
    for c in gg[i]:
        edges.append((i, c))


g.add_edges(edges)
out_name = 'tree.png'
plot(g, out_name, **default_style(g))
