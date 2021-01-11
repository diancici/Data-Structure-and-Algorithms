## Leetcode 652. Find Duplicate Subtrees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.dict = defaultdict(int)
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        # basic case
        if root is None:
            return "#"

        # Build the subTree and its identifier
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        subTree = left + "," + right + "," + str(root.val)

        # Compare with other subTree in the dict
        if self.dict[subTree] == 1:
            self.res.append(root)
        self.dict[subTree] += 1

        return subTree
    