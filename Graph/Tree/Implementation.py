## Binary Tree
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Three types of traversal
def traversal(node):
    # Code for pre-order
    traversal(node.left)
    # Code for in-order
    traversal(node.right)
    # Code for post-order


