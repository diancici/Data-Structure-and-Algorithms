## Inorder of BST is sorted ascendingly (left -> root -> right)
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Leetcode 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root:TreeNode, k:int) -> int:
        self.rank = 0
        self.inorder(root,k)
        return self.res

    def inorder(self, root,k):
        # basic case:
        if root is None:
            return

        self.inorder(root.left, k)

        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return
        
        self.inorder(root.right, k)



# Inorder of BST is sorted desendingly (right -> root -> left)
## Leetcode 538/1038 Convert BST to Greater Tree
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        return self.traverse(root)

    def traverse(self, root):
        if root is None:
            return None

        self.traverse(root.right)

        self.sum += root.val
        root.val = self.sum

        self.traverse(root.left)
        return root


## Leetcode 108. Convert Sorted Array to Binary Search Tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums)-1)
                
    def build(self, nums, l, h):
        if h < l:
            return None
        
        index = (h-l)//2+l # index of the current root
        left = self.build(nums, l, index-1)
        right = self.build(nums, index+1, h)
        # post order
        root = TreeNode(nums[index])
        root.left = left
        root.right = right
        
        return root       

