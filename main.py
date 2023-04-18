"""
main.py is starting file and for debug
"""
from dijkstra_algorithm import test_dijkstra, dijkstra
from utils import import_data, create_graph, draw_graph

if __name__ == "__main__":
    # imported_data = import_data()
    # print(imported_data.head(2))

    # draw_graph(create_graph())
    # test_dijkstra()

    graph = create_graph()
    print(dijkstra(graph, "WAŁBRZYSKA"))
