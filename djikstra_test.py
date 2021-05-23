import unittest
from djikstra import Graph

class TestDjikstra(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Graph()
        self.g.add_node("0", "1", 4)
        self.g.add_node("0", "7", 8)

        self.g.add_node("1", "2", 8)
        self.g.add_node("1", "7", 11)

        self.g.add_node("2", "8", 2)
        self.g.add_node("2", "3", 7)
        self.g.add_node("2", "5", 4)

        self.g.add_node("3", "4", 9)
        self.g.add_node("3", "5", 14)

        self.g.add_node("4", "5", 10)

        self.g.add_node("5", "6", 2)

        self.g.add_node("6", "8", 6)
        self.g.add_node("6", "7", 1)

        self.g.add_node("7", "8", 7)
    
    def test_djikstra(self):        
        self.assertEqual(self.g.djikstra("0", "1"), 4)
        self.assertEqual(self.g.djikstra("0", "2"), 12)
        self.assertEqual(self.g.djikstra("0", "3"), 19)
        self.assertEqual(self.g.djikstra("0", "4"), 21)
        self.assertEqual(self.g.djikstra("0", "5"), 11)
        self.assertEqual(self.g.djikstra("0", "6"), 9)
        self.assertEqual(self.g.djikstra("0", "7"), 8)
        self.assertEqual(self.g.djikstra("0", "8"), 14)

if __name__ == "__main__":
    unittest.main()
