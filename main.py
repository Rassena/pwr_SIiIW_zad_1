"""
main.py is starting file and for debug
"""
from datetime import datetime
from constants import CONNECTIONS
from utils import load_data

if __name__ == "__main__":
    graph = load_data(CONNECTIONS)

    start_stop = "kwiska"
    end_stop = "most grunwaldzki"
    start_time = datetime.time(7, 52)
    algorithm = "d"
    option = "t"

    # dijkstra(graph, "kwiska", "most grunwaldzki", datetime.time(7, 52))
