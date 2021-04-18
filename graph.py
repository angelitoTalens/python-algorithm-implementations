from collections import defaultdict

class Node():
    def __init__(self):        
        self.neighbors = []

class Graph():
    def __init__(self):
        self.graph = defaultdict(Node)        
    
    def add_edge(self, current: int, neighbor: int):        
        self.graph[current].neighbors.append(neighbor)

    def bfs(self, start: int)->list:
        result = []
        result.append(start)

        visited = set()
        visited.add(start)

        q = []
        q.extend(self.graph[start].neighbors)   
                                   
        while q:
            n = q.pop(0)                       
            if n not in visited:
                visited.add(n)
                result.append(n)                
                q.extend(self.graph[n].neighbors)
        
        return result
    
    def dfs(self, start: int)->list:
        visited = set()        
        return self._dfs(start, visited)        
    
    def _dfs(self, start: int, visited: set):
        result = []
        if start not in visited:
            visited.add(start)
            result.append(start)            
            for n in self.graph[start].neighbors:
                result.extend(self._dfs(n, visited))
        
        return result
