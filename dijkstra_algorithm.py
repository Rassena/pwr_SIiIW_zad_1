import datetime
from elements import PriorityQueue


def dijkstra_search(graph, start_stop, end_stop, start_time):
    front = PriorityQueue()
    front.put(start_stop, 0)
    came_from = {start_stop: None}
    cost_so_far: dict[str, float] = {start_stop: 0}
    time_so_far: dict[str, datetime.time] = {start_stop: start_time}

    while not front.empty():
        cur_stop = front.get()
        if cur_stop == end_stop:
            break
        try:
            graph.nodes[cur_stop]
        except KeyError:
            continue

        for neighbour in graph.nodes[cur_stop]:
            cost = graph.min_time_cost(cur_stop, neighbour, time_so_far[cur_stop])
            if cost is None:
                continue
            new_cost = cost_so_far[cur_stop] + cost[0]
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost
                front.put(neighbour, priority)
                came_from[neighbour] = cur_stop, cost[1]
                time_so_far[neighbour] = cost[1][2]

    return came_from, cost_so_far
