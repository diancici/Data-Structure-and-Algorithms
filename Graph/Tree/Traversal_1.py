## Leetcode 226. Invert Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        # base case:
        if root is None:
            return None
        # pre-order traversal
        temp = root.right
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


## lEETCODE 116. Populating Next Right Pointers in Each Node

## Leetcode 114. Flatten Binary Tree to Linked List