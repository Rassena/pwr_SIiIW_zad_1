"""
import_data function is importing data from files inside folder data

"""

import os

import pandas as pd
import networkx as nx

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

    graph = nx.Graph()

    # Add nodes to the graph
    graph.add_nodes_from(dataframe['start_stop'])
    graph.add_nodes_from(dataframe['end_stop'])

    for i, row in dataframe.iterrows():
        graph.add_edge(row['start_stop'], row['end_stop'], weight=row['departure_time'],)
    print(graph.nodes())
    print(graph.edges())
