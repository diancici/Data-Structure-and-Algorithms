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

## Binary Search Tree
# Insert
def insert(root, node):
    if root is None:
        root = node
        return root
    elif root.data < node.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

# Search
def search(node, val):
    if node is None:
        print("No node found")
        return None
    if node.data == val:
        print("Node is found")
        return node
    elif node.data < val:
        search(node.right, val)
    elif node.data > val:
        search(node.left, val)

# Delete
def delete(node, val):
    if (node is None):
        return None
    # find the position of node which has the key value
    if (node.data < val):
        node.right = delete(node.right, val)
        
    elif (node.data > val):
        node.left = delete(node.left, val)
        
    else:
        # node has no child or has one child
        if (node.left is None):
            temp = node.right
            node = None
            return temp
        
        elif (node.right is None):
            temp = node.left
            node = temp
            return temp
        
        # node has two children : find the minimum node of the right subtree
        else:
            temp = minimum(node.right)
            node.data = temp.data #replace node.data
            node.right = delete(node.right, temp.data) # modify node.right
            
    return node

def minimum(node):
    while(node.left is not None):
        node = node.left
    return node

