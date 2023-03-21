"""
main.py is starting file and for debug
"""
from dijkstra_algorithm import test_dijkstra
from utils import import_data, create_graph

if __name__ == "__main__":
    imported_data = import_data()
    print(imported_data.head(2))

    create_graph()