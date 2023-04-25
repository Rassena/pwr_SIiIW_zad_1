"""
import_data function is importing data from files inside folder data

"""
import pandas
import time
from astar_algorithm import astar_search
from dijkstra_algorithm import dijkstra_search
from element import Graph, Edge


def load_data(file):
    df = pandas.read_csv(
        file,
        parse_dates=['departure_time', 'arrival_time'],
        date_parser=lambda x: pandas.to_datetime(x, format='%H:%M:%S').time,
        low_memory=False
    )

    graph = Graph()
    for row in df.values[1:]:
        start_stop = str(row[6]).lower()
        end_stop = str(row[7]).lower()

        if start_stop in graph.nodes.keys():
            graph.nodes[start_stop].append(end_stop)
        else:
            graph.nodes[start_stop] = [end_stop]

        edge = Edge(row[3], row[5], row[4], row[8], row[9], row[10], row[11])

        if (start_stop, end_stop) in graph.edges.keys():
            graph.edges[(start_stop, end_stop)].append(edge)
        else:
            graph.edges[(start_stop, end_stop)] = [edge]

    for row in graph.edges.values():
        row.sort(key=lambda x: x.leave_time)

    return graph


def search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid].leave_time == x:
            return mid
        elif arr[mid].leave_time > x:
            return search(arr, low, mid - 1, x)
        else:
            return search(arr, mid + 1, high, x)
    else:
        if low >= len(arr):
            return -1
        if arr[low].leave_time > x:
            return low
        else:
            return -1


def time_diff(end_time, start_time):
    return (end_time.hour * 60 + end_time.minute) - (start_time.hour * 60 + start_time.minute)


def create_path(came_from, start, goal):
    current = goal
    path = []
    lines = []

    if goal not in came_from:
        return []

    while current != start:
        path.append(current)
        current = came_from[current][0]
        if current != start:
            lines.append(came_from[current][1])

    path.append(start)
    path.reverse()
    lines.reverse()
    lines.append(came_from[goal][1])

    return path, lines


def efficiency(graph, start_stop, end_stop, start_time, algorithm, opt_time):
    end_time, start_time, came_from, cost = None

    if algorithm == "d":
        start_time = time.time()
        came_from, cost = dijkstra_search(graph, start_stop, end_stop, start_time)
        end_time = time.time()
    elif algorithm == "a":
        start_time = time.time()
        came_from, cost = astar_search(graph, start_stop, end_stop, start_time, opt_time)
        end_time = time.time()

    return came_from, cost, end_time - start_time


def display_results(path, lines):
    cur_stop = lines[0][0]
    print(f"Line: {str(cur_stop)} Stop: {str(path[0])} departure: {str(lines[0][1])} arrival: {str(lines[0][2])}")
    i = 2
    changes = 0
    for elem in lines[2:]:
        if elem[0] != cur_stop:
            changes += 1
            cur_stop = elem[0]
            print("Bus change!")
            print(f"Line: {str(cur_stop)} Stop: {str(path[i])} departure: {str(elem[1])}")
        i += 1
    time = time_diff(lines[-1][2], lines[0][1])
    print(f"Arrival Time: {str(lines[-1][2])} Stop: {str(path[-1])}")
    print(f"Travel time: {str(time)} min")
    print(f"Changes: {changes}")
    print("")


def generate_results(graph, start_stop, end_stop, start_time, algorithm, option=None):
    if algorithm == "a":
        if option == "t":
            came_from, cost = astar_search(graph, start_stop, end_stop, start_time, opt_time=True)
        elif option == "p":
            came_from, cost = astar_search(graph, start_stop, end_stop, start_time, opt_time=False)
    elif algorithm == "d":
        came_from, cost = dijkstra_search(graph, start_stop, end_stop, start_time)

    return came_from, start_stop, end_stop
