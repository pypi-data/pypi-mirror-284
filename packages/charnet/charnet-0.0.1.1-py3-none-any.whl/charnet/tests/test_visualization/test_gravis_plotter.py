import gravis as gv
import matplotlib.colors as mcolors


def plot_graph_gravis(graph):
    # using the weights of edges as edge labels
    # using the counts of nodes as node labels
    # use color property of nodes and edges to color them
    # use gravis to display the graph

    temp_graph = graph.copy()
    for node in graph.nodes:
        temp_graph.nodes[node]['color'] = mcolors.to_hex(graph.nodes[node]['color'])
    for u, v, data in graph.edges(data=True):
        temp_graph[u][v]['color'] = mcolors.to_hex(data['color'])
        temp_graph[u][v]['label'] = data['weight']
    g = gv.d3(temp_graph, edge_size_data_source='weight', use_edge_size_normalization=True)
    g.display()
