import pytest
import pandas as pd
import networkx as nx
from app.charnet.src import CharNet


@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Season': [1, 1, 1, 1],
        'Episode': [1, 1, 1, 1],
        'Scene': [1, 1, 2, 2],
        'Line': [1, 2, 1, 2],
        'Speaker': ['Sheldon', 'Leonard', 'Penny', 'Sheldon'],
        'Listener': ['Leonard', 'Sheldon', 'Sheldon', 'Penny'],
        'Words': ['Hello', 'Hi there', 'How are you?', 'Fine, thank you']
    })


def test_charnet_initialization(sample_data):
    print(type(sample_data))
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    assert net.data is not None
    assert len(net.pos2idx) == 4
    assert net.idx2pos == ('Season', 'Episode', 'Scene', 'Line')


def test_get_weights(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    net.get_weights(lambda x: len(x))
    assert 'weights' in net.data.columns
    assert net.data['weights'].tolist() == [5, 8, 12, 15]


def test_normalize_weights(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    net.get_weights(lambda x: len(x))
    net.normalize_weights()
    assert net.data['weights'].max() == 1.0


def test_get_interval(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    subset = net.get_interval((1, 1, 1, 1), (1, 1, 2, 1))
    assert len(subset.data) == 2


def test_set_min_step(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    print(net.data.columns)
    net.set_min_step('Scene')
    assert len(net.data) == 4


def test_get_graph(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    net.get_weights(lambda x: 1)
    graph = net.get_graph()
    assert isinstance(graph, nx.DiGraph)
    assert len(graph.nodes) == 3
    assert len(graph.edges) == 4


def test_set_layout(sample_data):
    net = CharNet(sample_data, ('Season', 'Episode', 'Scene', 'Line'),
                  speakers='Speaker', listeners='Listener', interactions='Words')
    net.get_weights(lambda x: 1)
    net.set_layout('spring')
    assert net.layout == 'spring'
