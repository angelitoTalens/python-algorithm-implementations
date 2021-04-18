import unittest
from graph import Graph

class GraphTest(unittest.TestCase):
    def setUp(self):

        # undirected graph
        #       1
        #     /   \
        #    2     3
        #    | \   |
        #    |   \ |
        #    4 --- 5
        #     \   /
        #       6

        self.graph = Graph()        
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(2, 5)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(4, 2)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(4, 6)
        self.graph.add_edge(5, 2)
        self.graph.add_edge(5, 3)
        self.graph.add_edge(5, 4)
        self.graph.add_edge(5, 6)
        self.graph.add_edge(6, 4)
        self.graph.add_edge(6, 5)

        # directed graph (binary tree)
        # 
        #         1
        #       /   \
        #      2     3
        #    /   \
        #   4     5        

        self.binary_tree = Graph()
        self.binary_tree.add_edge(1, 2)
        self.binary_tree.add_edge(1, 3)
        self.binary_tree.add_edge(2, 4)
        self.binary_tree.add_edge(2, 5)

    def test_graph_bfs(self):
        self.assertEqual(self.graph.bfs(1), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.graph.bfs(4), [4, 2, 5, 6, 1, 3])
        self.assertEqual(self.binary_tree.bfs(1), [1, 2, 3, 4, 5])

    
    def test_graph_dfs(self):
        self.assertEqual(self.graph.dfs(1), [1, 2, 4, 5, 3, 6])
        self.assertEqual(self.graph.dfs(4), [4, 2, 1, 3, 5, 6])
        self.assertEqual(self.binary_tree.dfs(1), [1, 2, 4, 5, 3])

if __name__ == "__main__":
    unittest.main()