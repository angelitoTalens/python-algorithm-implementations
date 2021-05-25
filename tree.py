class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, arr):
        self.root = self.create_level_order(arr, Node(arr[0]), 0)

    def create_level_order(self, arr, root, i):
        if i < len(arr):
            node = Node(arr[i])

            # add left node
            node.left = self.create_level_order(arr, node.left, 2 * i + 1)

            # add right node
            node.right = self.create_level_order(arr, node.right, 2 * i + 2)

            return node

    def inorder_traversal(self, root):
        retval = []
        if root:
            retval.extend(self.inorder_traversal(root.left))
            retval.append(root.data)
            retval.extend(self.inorder_traversal(root.right))

        return retval

    def preorder_traversal(self, root):
        retval = []
        if root:
            retval.append(root.data)
            retval.extend(self.preorder_traversal(root.left))
            retval.extend(self.preorder_traversal(root.right))

        return retval

    def postorder_traversal(self, root):
        retval = []
        if root:
            retval.extend(self.postorder_traversal(root.left))
            retval.extend(self.postorder_traversal(root.right))
            retval.append(root.data)

        return retval
