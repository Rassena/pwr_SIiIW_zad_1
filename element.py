import heapq
from constants import PENALTY
from utils import search, time_diff


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Edge:
    def __init__(self, name, arrive_time, leave_time, start_x, start_y, end_x, end_y):
        self.name = name
        self.arrive_time = arrive_time
        self.leave_time = leave_time
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def min_time_cost(self, start_node, end_node, time):
        possible_edges = self.edges[start_node, end_node]
        edge_found_index = search(possible_edges, 0, len(possible_edges) - 1, time)
        if edge_found_index != -1:
            edge_found = possible_edges[edge_found_index]
            if edge_found.leave_time >= time:
                return time_diff(edge_found.arrive_time, time), (
                    edge_found.name, edge_found.leave_time, edge_found.arrive_time)
        return None

    def min_transfer_cost(self, start_node, end_node, time, cur_line):
        possible_edges = self.edges[start_node, end_node]
        edge_found_index = search(possible_edges, 0, len(possible_edges) - 1, time)
        if edge_found_index != -1:
            edge_found = possible_edges[edge_found_index]
            basic_cost = time_diff(edge_found.arrive_time, time)
            if edge_found.name != cur_line:
                basic_cost += PENALTY
            return basic_cost, (edge_found.name, edge_found.leave_time, edge_found.arrive_time)
        return None
