## leetcode 1373 Maximum Sum BST in Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.maxSum = 0
        self.traverse(root)
        return self.maxSum
    
    # return list[isBST, min, max, sum]
    def traverse(self, root):
        # base case
        if root is None:
            res = [1, float('inf'), -float('inf'), 0]
            return res
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        # initalize
        res = [0]
        for i in range(3):
            res.append(0)
        if left[0] == 1 and right[0] == 1 and root.val > left[2] and root.val < right[1]:
            # root and its subtree is a BST
            res[0] = 1
            res[1] = min(left[1], root.val)
            res[2] = max(right[2], root.val)
            res[3] = left[3]+right[3]+root.val
            self.maxSum = max(self.maxSum, res[3])
        else:
            res[0] = 0
            
        return res