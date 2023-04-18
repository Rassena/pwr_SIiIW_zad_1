"""

"""
from datetime import datetime

import heapq


def dijkstra(graph, start: str):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    date_format = '%H:%M:%S'

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weights in graph[current_node].items():
            shortest = float('inf')
            for _, weight in weights.items():
                arrival = datetime.strptime(weight['arrival_time'], date_format)
                departure = datetime.strptime(weight['departure_time'], date_format)
                dif = (arrival-departure).total_seconds()/60
                if shortest > dif:
                    shortest = dif
            distance = current_distance + shortest

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def test_dijkstra():
    graph = {
        'A': {'B': 2, 'C': 1},
        'B': {'A': 2, 'D': 5},
        'C': {'A': 1, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 2},
        'E': {'D': 2}
    }

    distances = dijkstra(graph, 'A')
    print(distances)
