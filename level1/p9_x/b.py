# Create a directed graph
from igraph import Graph, plot

g = Graph(directed=False)

# Add 5 vertices
g.add_vertices(5)

# Add ids and labels to vertices
for i in range(len(g.vs)):
    g.vs[i]["id"] = i
    g.vs[i]["label"] = str(i)

# Add edges
g.add_edges([(0, 2), (0, 1), (0, 3), (1, 2), (1, 3), (2, 4), (4, 3), (1,4)])  # Add weights and edge labels
# weights = [8, 6, 3, 5, 6, 4, 9]
# g.es['weight'] = weights
# g.es['label'] = weights

visual_style = {}
out_name = 'graph.png'  # Set bbox and margin
visual_style['bbox'] = (500, 500)
visual_style['margin'] = 27  # Set vertex colours
visual_style['vertex_color'] = 'white'  # Set vertex size
visual_style['vertex_size'] = 50  # Set vertex lable size
visual_style['vertex_label_size'] = 22  # Don't curve the edges
visual_style['edge_curved'] = False  # Set the layout
my_layout = g.layout_lgl()
visual_style['layout'] = my_layout  # Plot the graph
plot(g, out_name, **visual_style)
