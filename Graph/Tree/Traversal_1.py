# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Leetcode 226. Invert Binary Tree
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


## leetcode 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepth(root)
    
    def maxDepth(self, root):
        if root is None:
            return 0        
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

## Leetcode 111. Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # basic case
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left==0 and right==0:
            minimum = 1
        elif left==0 :
            minimum = right + 1
        elif right==0:
            minimum = left + 1
        else:
            minimum = min(left, right) + 1
        return minimum







## lEETCODE 116. Populating Next Right Pointers in Each Node

## Leetcode 114. Flatten Binary Tree to Linked List