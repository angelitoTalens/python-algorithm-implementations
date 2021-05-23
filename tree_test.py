import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree([1, 2, 3, 4, 5 , 6, 7])

    def test_inorder_traversal(self):
        self.assertEqual(self.tree.inorder_traversal(self.tree.root), [4, 2, 5, 1, 6, 3, 7])

    def test_preorder_traversal(self):
        self.assertEqual(self.tree.preorder_traversal(self.tree.root), [1, 2, 4, 5, 3, 6, 7])

    def test_postorder_traversal(self):
        self.assertEqual(self.tree.postorder_traversal(self.tree.root), [4, 5, 2, 6, 7, 3, 1])

if __name__ == "main":
    unittest.main()