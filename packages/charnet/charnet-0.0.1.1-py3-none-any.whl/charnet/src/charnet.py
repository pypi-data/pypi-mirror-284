import contextlib
import warnings

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from .utils import default_directed_agg_weight, default_undirected_agg_weight
from .visualization import (
    plot_graph_matplotlib,
    plot_graph_plotly,
    plot_graph_gravis,
    plot_graph_pyvis
)


class CharNet:

    def __init__(self, data=None, position_columns=None, speakers='speakers', listeners='listeners',
                 interactions='interactions', weights=None, directed=True):
        self.data = None
        self.pos2idx = dict()
        self.idx2pos = None
        self._graph = None
        self._layout = None
        self._directed = directed

        if data is not None:
            self.load_data(data, position_columns, speakers, listeners, interactions, weights)

    def load_data(self, data, position_columns, speakers='speakers', listeners='listeners', interactions='interactions',
                  participants=None, weights=None):
        """
        Load data into CharNet.
        
        :param participants:
        :param data: pd.DataFrame, data containing the conversation lines
                     columns: positions (e.g. season, episodes, etc), speakers, listeners, weights
        :param position_columns: tuple, column names representing the hierarchical order of each line
        :param speakers: str, column name for speakers
        :param listeners: str, column name for listeners
        :param interactions: str, column name for interactions
        :param weights: str or None, column name for weights (if any)
        """
        # get the data
        df = data.copy()
        # check if the columns are present in the data
        if not all(col in df.columns for col in position_columns):
            raise ValueError("Not all position columns found in the data.")
        # create dictionary to store the position of each column
        self.pos2idx.clear()
        for col in position_columns:
            if col in ['position', 'speakers', 'listeners', 'interactions', 'weights', 'participants']:
                raise ValueError(f"Column name '{col}' is reserved for internal use.")
            df[col] = pd.to_numeric(df[col], errors='coerce')
            self.pos2idx[col] = position_columns.index(col)

        df['position'] = df[list(position_columns)].apply(tuple, axis=1)

        def process_column(series):
            return series.apply(lambda x: list(set(
                str(item).strip() for item in (x if isinstance(x, list) else str(x).strip('[]').split(',')) if item)))

        if self._directed:
            df[speakers] = process_column(df[speakers])
            df[listeners] = process_column(df[listeners])
            df = df.rename(columns={speakers: 'speakers', listeners: 'listeners'})
        else:
            # For undirected graphs, we need to combine speakers and listeners
            if participants:
                df[participants] = process_column(df[participants])
                df = df.rename(columns={participants: 'participants'})
            else:
                df[speakers] = process_column(df[speakers])
                df[listeners] = process_column(df[listeners])
                df['participants'] = df.apply(lambda row: list(set(row[speakers] + row[listeners])), axis=1)
                df = df.drop(columns=[speakers, listeners])

        if interactions:
            df = df.rename(columns={interactions: 'interactions'})
        if weights:
            df = df.rename(columns={weights: 'weights'})

        columns_to_keep = (list(position_columns) + ['position'] +
                           (['speakers', 'listeners'] if self._directed else ['participants']) +
                           (['interactions'] if interactions else []) +
                           (['weights'] if weights else []))
        df = df[columns_to_keep]

        self.data = df
        self.idx2pos = position_columns

        self._graph = None
        self._layout = None

        return self

    def get_weights(self, calculator=lambda x: 1):
        """
        Calculate weights based on interactions.
        
        :param interactions: str, column name for interactions
        :param calculator: callable, function to calculate weights
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data using the load_data method.")
        if 'interactions' not in self.data.columns:
            raise ValueError(f"Column 'interactions' not found in the data.")

        self.data['weights'] = self.data['interactions'].apply(calculator)

    def normalize_weights(self):
        """
        Normalize weights.
        """
        if 'weights' not in self.data.columns:
            raise ValueError("Column 'weights' not found in the data.")
        self.data['weights'] = self.data['weights'] / self.data['weights'].max()
        self._graph = None
        return self

    def get_interval(self, start, end):
        """
        Get a subset of the data based on the start and end time points.
        
        :param start: dict, dictionary containing the start time points for some position columns
        :param end: dict, dictionary containing the end time points for some position columns
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data using the load_data method.")

        interval = CharNet(directed=self._directed)
        interval.data = self.data.copy()
        if start:
            interval.data = interval.data[interval.data['position'] >= start]
        if end:
            interval.data = interval.data[interval.data['position'] < end]
        interval.idx2pos = self.idx2pos
        interval.pos2idx = self.pos2idx.copy()
        interval.set_layout(self._layout)

        return interval

    def set_min_step(self, min_step, weight_func=None):
        """
        Set the minimum step size for the position columns.

        :param aggregate_fn:
        :param min_step: int, minimum step size
        """
        if min_step not in self.idx2pos:
            raise ValueError(f"'{min_step}' is not a valid position column.")

        if 'weights' not in self.data.columns:
            self.get_weights()
            warnings.warn("No weights found. Calculating weights using default function.")

        min_step_index = self.pos2idx[min_step]
        group_columns = self.idx2pos[:min_step_index + 1]

        aggregate_fn = lambda df: self.step_agg_func(df, min_step, weight_fn=weight_func)
        grouped_data = self.data.groupby(list(group_columns)).apply(aggregate_fn).reset_index(drop=True)
        self.data = grouped_data

        self.idx2pos = self.idx2pos[:min_step_index + 1]
        self.pos2idx = {col: idx for idx, col in enumerate(self.idx2pos)}

        self._graph = None
        return self

    def step_agg_func(self, df, min_step, weight_fn=None):
        """
        Default aggregation function for minimum step.
        Counts the number of dialogues between each pair of speakers and listeners.

        :param weight_fn: callable, function to calculate weights (df -> dict)
        :param min_step:
        :param df: pd.DataFrame, dataframe containing rows within the minimum step
        :return: pd.DataFrame, aggregated rows with dialogue counts
        """
        if weight_fn is None:
            weight_fn = default_directed_agg_weight if self._directed else default_undirected_agg_weight
        agg_weights = weight_fn(df)

        agg_position = df['position'].iloc[0][:self.pos2idx[min_step] + 1]
        position_dict = dict(zip(self.idx2pos[:self.pos2idx[min_step] + 1], agg_position))

        if self._directed:
            aggregated = pd.DataFrame([
                {
                    **position_dict,
                    'position': agg_position,
                    'speakers': speaker,
                    'listeners': listener,
                    'weights': count
                }
                for (speaker, listener), count in agg_weights.items()
            ])
        else:
            aggregated = pd.DataFrame([
                {
                    **position_dict,
                    'position': agg_position,
                    'participants': participant,
                    'weights': count
                }
                for participant, count in agg_weights.items()
            ])

        return aggregated

    @property
    def is_directed(self):
        return self._directed

    def _create_digraph(self):
        digraph = nx.DiGraph()
        for idx, row in self.data.iterrows():
            speakers, listeners = row['speakers'], row['listeners']
            if isinstance(speakers, str):
                speakers = [speakers]
            if isinstance(listeners, str):
                listeners = [listeners]
            weight = row.get('weights', 0)
            for speaker in speakers:
                if speaker not in digraph:
                    digraph.add_node(speaker, count=1)
                else:
                    digraph.nodes[speaker]['count'] += 1

                for listener in listeners:
                    if listener not in digraph:
                        digraph.add_node(listener, count=1)
                    else:
                        digraph.nodes[listener]['count'] += 1

                    if digraph.has_edge(speaker, listener):
                        digraph[speaker][listener]['weight'] += weight
                    else:
                        digraph.add_edge(speaker, listener, weight=weight)
        return digraph

    def _create_graph(self):
        graph = nx.Graph()
        for idx, row in self.data.iterrows():
            participants = row['participants']
            weight = row.get('weights', 1)
            for i, part_i in enumerate(participants):
                if part_i not in graph:
                    graph.add_node(part_i, count=1)
                else:
                    graph.nodes[part_i]['count'] += 1

                for part_j in participants[i + 1:]:
                    if part_j not in graph:
                        graph.add_node(part_j, count=1)
                    else:
                        graph.nodes[part_j]['count'] += 1

                    if graph.has_edge(part_i, part_j):
                        graph[part_i][part_j]['weight'] += weight
                    else:
                        graph.add_edge(part_i, part_j, weight=weight)
        return graph

    def get_graph(self):
        """
        Get the graph representation of the current data.

        :return: nx.DiGraph, the graph representation
        """
        if self._graph is None:
            if self._layout is None:
                warnings.warn("No layout set. Using 'spring' layout by default.")
                self.set_layout('spring')
            self._graph = self._create_digraph() if self._directed else self._create_graph()
        return self._graph

    @contextlib.contextmanager
    def graph_context(self):
        """
        context manager for graph operations.
        """
        graph = self._graph
        try:
            yield graph
        finally:
            self._graph = None

    @property
    def layout(self):
        return self._layout

    def set_layout(self, layout='spring'):
        """
        Set the layout for the graph representation.

        :param layout: str, the layout algorithm to use
        :return: self, for method chaining
        """
        self._layout = layout
        if self._graph is not None:
            self._apply_layout()

    def _apply_layout(self):
        if self._graph is None:
            raise ValueError("No graph available. Call get_graph() first.")
        if self._layout == 'spring':
            pos = nx.spring_layout(self._graph)
        elif self._layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(self._graph)
        elif self._layout == 'circular':
            pos = nx.circular_layout(self._graph)
        elif self._layout == 'random':
            pos = nx.random_layout(self._graph)
        else:
            raise ValueError(f"Invalid layout '{self._layout}'.")

        pos_scaled = nx.rescale_layout_dict(pos, scale=100)

        node_count = [data['count'] for node, data in self._graph.nodes(data=True)]
        edge_weight = [data['weight'] for u, v, data in self._graph.edges(data=True)]
        min_max_node = (min(node_count), max(node_count))
        min_max_edge = (min(edge_weight), max(edge_weight))

        # Use a colormap to map counts and weights to colors
        cmap = plt.cm.viridis
        norm_node = plt.Normalize(*min_max_node)
        norm_edge = plt.Normalize(*min_max_edge)

        for node in self._graph.nodes:
            self._graph.nodes[node]['x'] = pos_scaled[node][0]
            self._graph.nodes[node]['y'] = pos_scaled[node][1]
            self._graph.nodes[node]['color'] = cmap(norm_node(self._graph.nodes[node]['count']))

        for u, v, data in self._graph.edges(data=True):
            data['color'] = cmap(norm_edge(data['weight']))

    def draw(self, plot: str = 'matplotlib'):
        """
        Draw the dynamic graphs.
        
        :param plot: test_visualization library to use
        :param graph: nx.DiGraph, graph to be plotted
        """
        graph = self.get_graph()
        if self._layout is not None:
            self._apply_layout()
        if plot == 'matplotlib':
            plot_graph_matplotlib(graph)
        elif plot == 'plotly':
            plot_graph_plotly(graph)
        elif plot == 'gravis':
            plot_graph_gravis(graph)
        elif plot == 'pyvis':
            plot_graph_pyvis(graph)
