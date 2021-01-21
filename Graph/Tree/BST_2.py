class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Leetcode 96. Unique Binary Search Trees, return a number
class Solution:
    def numTrees(self, n):
        self.memo = [[0 for i in range(n+1)] for j in range(n+1)]
        return self.count(1,n)

    def count(self, l, h):
        if l > h:
            return 1
        if self.memo[l][h] != 0:
            return self.memo[l][h]

        res = 0
        for i in range(l, h+1):
            left = self.count(l, i-1)
            right = self.count(i+1, h)
            res += left * right
        self.memo[l][h] = res
        return res


## Leetcode 95. Unique Binary Search Trees II, return list[list]
class Solution:
    def generateTrees(self, n: int):
        if n == 0: return []
        return self.build(1,n)

    # return the list which contans all possible sub-trees in [l,h]
    def build(self, l, h):
        res = []
        if l > h:
            res.append(None)
            return res

        for i in range(l, h+1):
            # build left and right BST valid tree
            leftTree = self.build(l, i-1)
            rightTree = self.build(i+1, h)
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
