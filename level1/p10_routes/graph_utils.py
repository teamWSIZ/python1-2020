from typing import Dict

from igraph import Graph


def default_style(g: Graph) -> Dict:
    # my_layout = g.layout_lgl()
    my_layout = g.layout_fruchterman_reingold()
    visual_style = {'bbox': (1200, 1200), 'margin': 30,
                    'vertex_size': 15, 'vertex_label_size': 12,
                    'edge_curved': False, 'layout': my_layout}
    return visual_style
