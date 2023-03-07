import os

import pandas as pd


def import_data(file_name: str = "connection_graph_new.csv") -> pd.DataFrame:
    path = os.path.join("data", file_name)
    df = pd.read_csv(path, low_memory=False)
    return df
