from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

## Leetcode 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque([root]) # FIFO: BFS
        ans = []
        if root is None: return ans

        while(q):
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(cur[:])
            cur.clear()
        return ans
            
## Leetcode 107. Binary Tree Level Order Traversal II
# Definition for a binary tree node.
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
                
                
## Leetcode 103. Binary Tree Zigzag Level Order Traversal
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:        
        if(root is None): return []
        res = []
        q = deque() # BFS: FIFO, queue
        q.append(root)
        zigzag = False # Flag

        while(q):
            cur = []
            for _ in range(len(q)):
                if zigzag: # Flag = True, this level: right to left; next level: left to right
                    node = q.pop()
                    cur.append(node.val)
                    if node.right: q.appendleft(node.right)
                    if node.left: q.appendleft(node.left)
                if not zigzag: # Flag = False, this level: left to right; next level: right to left
                    node = q.popleft()
                    cur.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.rigth:
                        q.append(node.right)
            res.append(cur[:])
            zigzag = not zigzag
            cur.clear()
        return res

                

            

    
        
        