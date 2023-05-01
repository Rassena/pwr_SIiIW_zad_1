"""
import_data function is importing data from files inside folder data

"""
import os

from astar_algorithm import astar_search
from dijkstra_algorithm import dijkstra_search
from elements import Graph, Edge
from constants import DATA_FOLDER, CSV_DATA_TYPE


def time_diff(end_time: int, start_time: int) -> int:
    """
    :param end_time:
    :param start_time:
    :return:
    """
    return end_time - start_time


def time_minutes_from_noon(hour: str) -> int:
    """
    :param hour: str in '%H:%M:%S' format
    :return:
    """

    h, m, _ = hour.split(':')
    return int((int(h) * 60) + int(m))


def time_format_to_str(minutes: int) -> str:
    return f"{minutes // 60}:{(minutes % 60):02d}"


def load_data(file: str) -> Graph:
    """
    :param file:
    :return:
    """

    import pandas
    df = pandas.read_csv(os.path.join(DATA_FOLDER, file), dtype=CSV_DATA_TYPE)

    graph: Graph = Graph()
    for row in df.values[1:]:
        start_stop = str(row[6]).lower()
        end_stop = str(row[7]).lower()

        if start_stop in graph.nodes.keys():
            graph.nodes[start_stop].append(end_stop)
        else:
            graph.nodes[start_stop] = [end_stop]

        edge = Edge(
            name=row[3],
            arrive_time=time_minutes_from_noon(row[5]),
            leave_time=time_minutes_from_noon(row[4]),
            start_x=row[8],
            start_y=row[9],
            end_x=row[10],
            end_y=row[11]
        )

        if (start_stop, end_stop) in graph.edges.keys():
            graph.edges[(start_stop, end_stop)].append(edge)
        else:
            graph.edges[(start_stop, end_stop)] = [edge]

    for row in graph.edges.values():
        row.sort(key=lambda x: x.leave_time)

    return graph


def create_path(came_from, start_stop, end_stop):
    current = end_stop
    path = []
    lines = []

    if end_stop not in came_from:
        return []

    while current != start_stop:
        path.append(current)
        current = came_from[current][0]
        if current != start_stop:
            lines.append(came_from[current][1])

    path.append(start_stop)
    path.reverse()
    lines.reverse()
    lines.append(came_from[end_stop][1])

    return path, lines


def display_results(path, lines):
    cur_stop = lines[0][0]
    print(
        f"Line: {str(cur_stop)} Stop: {str(path[0])} departure: {time_format_to_str(lines[0][1])} arrival: {time_format_to_str(lines[0][2])}")
    i = 2
    changes = 0
    for elem in lines[2:]:
        if elem[0] != cur_stop:
            changes += 1
            cur_stop = elem[0]
            print(f"Bus change! Line: {str(cur_stop)} Stop: {str(path[i])} departure: {time_format_to_str(elem[1])}")
        i += 1
    diff_in_time = time_diff(lines[-1][2], lines[0][1])
    print(f"Arrival Time: {time_format_to_str(lines[-1][2])} Stop: {str(path[-1])}")
    print(f"Travel time: {str(diff_in_time)} min")
    print(f"Changes: {changes}")
    print("")


def generate_results(graph, start_stop, end_stop, start_time, algorithm, option=None):
    came_from = None
    if algorithm == "a":
        if option == "t":
            came_from, cost = astar_search(graph, start_stop, end_stop, start_time, opt_time=True)
        elif option == "p":
            came_from, cost = astar_search(graph, start_stop, end_stop, start_time, opt_time=False)
    elif algorithm == "d":
        came_from, cost = dijkstra_search(graph, start_stop, end_stop, start_time)

    return came_from, start_stop, end_stop
