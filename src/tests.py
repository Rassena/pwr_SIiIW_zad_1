import time

from astar_algorithm import astar_search
from constants import TEST_REPEATS, ROUND_NUMBER
from dijkstra_algorithm import dijkstra_search


def calculate_efficiency(graph, start_stop, end_stop, start_time):
    st_time = time.time()
    for _ in range(TEST_REPEATS):
        _, _ = dijkstra_search(graph, start_stop, end_stop, start_time)
    end_time = time.time()
    average_time = round((((end_time - st_time) * 1000) / TEST_REPEATS), ROUND_NUMBER)
    print(f"dijkstra: {average_time} ms")

    st_time = time.time()
    for _ in range(TEST_REPEATS):
        _, _ = astar_search(graph, start_stop, end_stop, start_time, opt_time=True)
    end_time = time.time()
    average_time = round((((end_time - st_time) * 1000) / TEST_REPEATS), ROUND_NUMBER)
    print(f"astar optimized for time: {average_time} ms")

    st_time = time.time()
    for _ in range(TEST_REPEATS):
        _, _ = astar_search(graph, start_stop, end_stop, start_time, opt_time=False)
    end_time = time.time()
    average_time = round((((end_time - st_time) * 1000) / TEST_REPEATS), ROUND_NUMBER)
    print(f"astar optimized for changes: {average_time} ms")
