"""

"""

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

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
