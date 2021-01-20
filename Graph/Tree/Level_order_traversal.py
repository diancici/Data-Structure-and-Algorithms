## Leetcode 107. Ninary Tree Level Order Traversal II
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        stack = []
        stack.append(root)
        ans = deque()
        
        while stack:
            cur_level = []
            next_level = []
            for node in stack:
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            ans.appendleft(cur_level[:])
            stack = next_level
            
        return ans
                
                
    
    
        
        