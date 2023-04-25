from geopy import distance
from elements import PriorityQueue
import datetime


def heuristic(a, b, g):
    edge = g.edges[(a, b)][0]
    return distance.distance((edge.start_x, edge.start_y), (edge.end_x, edge.end_y)).km * 3


def astar_search(graph, start_stop, end_stop, start_time, opt_time=True):
    front = PriorityQueue()
    front.put(start_stop, 0)
    came_from = {start_stop: None}
    cost_so_far: dict[str, float] = {start_stop: 0}
    time_so_far: dict[str, datetime.time] = {start_stop: start_time}
    line_so_far: dict[str, str] = {start_stop: ""}

    while not front.empty():
        cur_stop = front.get()
        if cur_stop == end_stop:
            break
        try:
            graph.nodes[cur_stop]
        except KeyError:
            continue

        for neighbour in graph.nodes[cur_stop]:
            if opt_time:
                cost = graph.min_time_cost(cur_stop, neighbour, time_so_far[cur_stop])
            else:
                cost = graph.min_transfer_cost(cur_stop, neighbour, time_so_far[cur_stop], line_so_far[cur_stop])
            if cost is None:
                continue

            new_cost = cost_so_far[cur_stop] + cost[0]
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic(cur_stop, neighbour, graph)
                front.put(neighbour, priority)
                came_from[neighbour] = cur_stop, cost[1]
                time_so_far[neighbour] = cost[1][2]
                line_so_far[neighbour] = cost[1][0]

    return came_from, cost_so_far
