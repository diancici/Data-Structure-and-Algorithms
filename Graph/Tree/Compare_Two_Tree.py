# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Leetcode 100. Same Tree
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None and q:
            return False
        if q is None and p:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        # post-order
        if left and right and p.val==q.val:
            return True
        else: return False


## lEETCODE 101. Symmetric Tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self,leftN, rightN):
        if(leftN is None and rightN is None): return True
        if(leftN is None or rightN is None):
            return False
        return (leftN.val == rightN.val) and self.isMirror(leftN.left, rightN.right) and self.isMirror(leftN.right, rightN.left)