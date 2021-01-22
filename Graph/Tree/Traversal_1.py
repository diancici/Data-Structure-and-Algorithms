from typing import List
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


## Leetcode 110.Balanced Binary Tree
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root) != -1
        
    def check(self, root):
        """Return the height of tree"""
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == -1 or right == -1 or abs(right-left) > 1 :
            return -1
        return 1 + max(left, right)


## Leetcode 112. Path Sum
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasSum(root, sum, 0)
    
    def hasSum(self, node, target, cur_sum):
        if node is None: return False
        cur_sum += node.val
        if cur_sum == target and node.right is None and node.left is None: return True
        return self.hasSum(node.right, target, cur_sum) or self.hasSum(node.left, target, cur_sum)


## Leetcode 113. Path Sum II
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        self.traverse(root, sum, 0, [])
        return self.ans
    
    def traverse(self, root, target, cur_sum, path):
        if root is None: 
            return         
        cur_sum += root.val
        path.append(root.val)
        if root.left is None and root.right is None:
            if cur_sum == target:
                self.ans.append(path[:])
            
                    
        self.traverse(root.left, target, cur_sum, path[:]) # deep copy because path is mutable
        self.traverse(root.right, target, cur_sum, path[:])
        


## lEETCODE 116. Populating Next Right Pointers in Each Node

## Leetcode 114. Flatten Binary Tree to Linked List