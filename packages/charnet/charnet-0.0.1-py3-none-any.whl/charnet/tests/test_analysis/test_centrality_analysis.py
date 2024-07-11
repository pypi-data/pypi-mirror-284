import pandas as pd
import networkx as nx

from app.charnet.src import CharNet


def degree_centrality(cnet, start, end):
    """
    Calculate degree centrality for each character in the subset of the data.
    :param cnet: CharNet object
    :param start: start position
    :param end: end position
    :return: pd.DataFrame
    """
    results = pd.DataFrame()
    for index, row in cnet._data.iterrows():
        if start <= row['position'] < end:
            # create subset df for each dialog
            subset = cnet.get_interval(start, row['position'])
            graph = CharNet.get_graph(subset)
            # calculate degree centrality
            in_degree_centrality = nx.in_degree_centrality(graph)
            out_degree_centrality = nx.out_degree_centrality(graph)

            weighted_in_degree_centrality = {node: sum(d['weight'] for _, _, d in graph.in_edges(node, data=True)) for
                                             node in graph.nodes()}
            weighted_out_degree_centrality = {node: sum(d['weight'] for _, _, d in graph.out_edges(node, data=True)) for
                                              node in graph.nodes()}

            for node in graph.nodes:
                position_dict = dict(zip(cnet.idx2pos, row['position']))
                new_row = {
                    **position_dict,
                    'character': node,
                    'in_degree': in_degree_centrality[node],
                    'out_degree': out_degree_centrality[node],
                    'weighted_in_degree': weighted_in_degree_centrality[node],
                    'weighted_out_degree': weighted_out_degree_centrality[node]
                }
                results = pd.concat([results, pd.DataFrame(new_row, index=[0])], ignore_index=True)

    return results
