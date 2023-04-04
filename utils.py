"""
import_data function is importing data from files inside folder data

"""

import os

import mpld3 as mpld3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx import nodes

from constants import CONNECTIONS


def import_data(file_name: str = CONNECTIONS) -> pd.DataFrame:
    """
    :param file_name: name of .csv file to import
    :return: DataFrame

    """
    pd.set_option('display.max_columns', None)
    path = os.path.join("data", file_name)
    data_frame = pd.read_csv(path, low_memory=False)
    return data_frame


def create_graph(dataframe: pd.DataFrame = None, weight: str = "time") -> nx.Graph:
    """

    :param dataframe:
    :return:
    """

    df = pd.DataFrame({
        'source': ['A', 'B', 'C', 'D', 'E'],
        'target': ['B', 'C', 'D', 'E', 'F'],
        'weight': [1, 2, 3, 4, 5]
    })

    if not dataframe:
        dataframe = import_data()

    G = nx.Graph()

    for i, row in dataframe.iterrows():
        G.add_node(row['start_stop'], pos=(row['start_stop_lat'], row['start_stop_lon']))
        G.add_node(row['end_stop'], pos=(row['end_stop_lat'], row['end_stop_lon']))
        G.add_edge(row['start_stop'], row['end_stop'], company=row['company'], line=row['line'], departure_time=row['departure_time'], arrival_time=row['arrival_time'])

    # Set the figure size and DPI
    fig = plt.figure(figsize=(200, 200), dpi=60)
    # Get the node positions
    pos = nx.get_node_attributes(G, 'pos')
    # Draw the graph with node labels
    nx.draw(G, pos, with_labels=True)
    # Get the edge labels
    labels = nx.get_edge_attributes(G, 'line')
    # Draw the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Show the plot
    plt.show()


