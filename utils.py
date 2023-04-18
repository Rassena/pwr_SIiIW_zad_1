"""
import_data function is importing data from files inside folder data

"""

import os

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

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


def create_graph(dataframe: pd.DataFrame = None) -> nx.MultiGraph:
    """

    :param dataframe:
    :return:
    """

    if not dataframe:
        dataframe = import_data()

    graph = nx.MultiGraph()

    for i, row in dataframe.iterrows():
        graph.add_node(row['start_stop'], pos=(row['start_stop_lon'], row['start_stop_lat']))
        graph.add_node(row['end_stop'], pos=(row['end_stop_lon'], row['end_stop_lat']))
        if row['start_stop'] != row['end_stop']:
            graph.add_edge(row['start_stop'], row['end_stop'], company=row['company'], line=row['line'],
                           departure_time=row['departure_time'], arrival_time=row['arrival_time'])

    return graph


def draw_graph(graph: nx.MultiGraph, graph_name: str = "my_plot") -> None:
    plt.figure(figsize=(300, 300), dpi=80)
    pos: dict = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True)
    labels: dict = nx.get_edge_attributes(graph, 'line')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.savefig(f"{graph_name}.pdf", format="pdf")
