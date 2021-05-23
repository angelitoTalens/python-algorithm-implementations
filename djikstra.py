from collections import defaultdict
from typing import DefaultDict



class Node():
    def __init__(self):
        self.name = str()
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
        node_set = {self.graph[start]}
        adjacency_matrix = {start: 0}

        while node_set:
            node = self.get_min(list(node_set), adjacency_matrix)            
            node_set.remove(node)
            for name, value in node.neighbors:
                path_value = adjacency_matrix[node.name] + value
                if name not in adjacency_matrix.keys() or path_value < adjacency_matrix[name]:           
                    adjacency_matrix[name] = path_value
                    node_set.add(self.graph[name])
        
        return adjacency_matrix[end] if end in adjacency_matrix else None
    
    def get_min(self, nodes: list, adjacency_matrix: dict)->Node:        
        node = nodes[0]
        min = adjacency_matrix[node.name]
        for n in nodes:
            if adjacency_matrix[n.name] < min:
                min, node = adjacency_matrix[n.name], n 
        
        return node
