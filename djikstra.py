from collections import defaultdict
from typing import DefaultDict



class Node():
    def __init__(self):
        self.name = str()
        self.value = None
        self.neighbors = set()

class Graph():
    def __init__(self):
        self.graph = defaultdict(Node)

    def add_node(self, start: str, end: str, value: int):
        start_node = self.graph[start]
        start_node.name = start
        start_node.neighbors.add((end, value))

        end_node = self.graph[end]
        end_node.name = end
        end_node.neighbors.add((start, value))

    def djikstra(self, start: str, end: str)->int:
        start_node = self.graph[start]
        start_node.value = 0

        node_list = [start_node]

        while node_list:
            node_list.sort(key=self.get_node_value)
            node = node_list.pop(0)

            node_set = set(node_list)
            node_set.update(self.update_neighbors(node.value, node.neighbors))
            node_list = list(node_set)

        return self.graph[end].value
    
    def update_neighbors(self, current_value: int, neighbors: set)->set:
        next_node_set = set()
        for neighbor_name, neighbor_value in neighbors:
            path_value = current_value + neighbor_value
            if not self.graph[neighbor_name].value or path_value < self.graph[neighbor_name].value:
                self.graph[neighbor_name].value = path_value                
                next_node_set.add(self.graph[neighbor_name])

        return next_node_set                

    def get_node_value(self, node: Node):
        return node.value
