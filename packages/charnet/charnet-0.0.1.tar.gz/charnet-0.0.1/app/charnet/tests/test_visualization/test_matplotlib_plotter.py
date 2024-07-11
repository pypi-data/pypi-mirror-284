from matplotlib import pyplot as plt
import networkx as nx


def plot_graph_matplotlib(graph):
    # Given a graph, plot it with nodes colored by count and edges colored by weight
    pos = {node: (data['x'], data['y']) for node, data in graph.nodes(data=True)}
    node_colors = [data['color'] for node, data in graph.nodes(data=True)]
    edge_labels = {(u, v): data['weight'] for u, v, data in graph.edges(data=True)}
    edge_colors = {(u, v): data['color'] for u, v, data in graph.edges(data=True)}

    # Find edges (u, v) such that (v, u) exists
    double_edges = [(u, v) for u, v in graph.edges if graph.has_edge(v, u)]
    double_edges = double_edges + [(v, u) for u, v in double_edges]
    double_edges_colors = [edge_colors[edge] for edge in double_edges]

    # Create a copy of the original positions to adjust the edges
    pos_edges = pos.copy()

    # Increase figure size
    plt.figure(figsize=(12, 9))

    single_edges_colors = [edge_colors[edge] for edge in graph.edges if edge not in double_edges]

    for u, v in double_edges:
        offset = 0.1
        pos_edges[(u, v)] = (pos[u][0] + offset, pos[u][1] + offset)
        pos_edges[(v, u)] = (pos[v][0] - offset, pos[v][1] - offset)

    # Draw nodes
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors)

    # Draw edges with arrows, specifying the positions of the edges to avoid overlap
    nx.draw_networkx_edges(graph, pos,
                           edgelist=[(u, v) for u, v in graph.edges if (u, v) not in double_edges],
                           edge_color=single_edges_colors, alpha=0.5, arrows=True)
    nx.draw_networkx_edges(graph, pos_edges,
                           edgelist=double_edges, edge_color=double_edges_colors,
                           connectionstyle='arc3,rad=0.2', alpha=0.5, arrows=True)

    edge_colors = [edge_colors[edge] for edge in graph.edges]

    # Draw labels (if necessary)
    nx.draw_networkx_labels(graph, pos, font_size=12)

    # Draw edge labels with transparent background and different colors
    ax = plt.gca()
    for (u, v), label in edge_labels.items():
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        dx = pos[v][0] - pos[u][0]
        dy = pos[v][1] - pos[u][1]
        # Adjust the label position slightly along the perpendicular direction
        if (u, v) in double_edges:
            # offset_x = -dy * 0.1
            # offset_y = dx * 0.1
            offset_x = dy * 0.1
            offset_y = -dx * 0.1
        else:
            offset_x = 0
            offset_y = 0
        # Positioning label at the middle of the edge with a slight offset
        ax.annotate(round(label, 2), xy=(x + offset_x, y + offset_y),
                    textcoords='offset points', xytext=(0, 0),
                    ha='center', va='center', fontsize=10, color=edge_colors[list(graph.edges).index((u, v))],
                    bbox=dict(facecolor='white', alpha=0.0, edgecolor='none'))

    plt.show()
