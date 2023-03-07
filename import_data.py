"""
import_data function is importing data from files inside folder data

"""

import os

import pandas as pd


def import_data(file_name: str = "connection_graph_new.csv") -> pd.DataFrame:
    """
    :param file_name: name of .csv file to import
    :return: DataFrame

    """
    path = os.path.join("data", file_name)
    data_frame = pd.read_csv(path, low_memory=False)
    return data_frame
