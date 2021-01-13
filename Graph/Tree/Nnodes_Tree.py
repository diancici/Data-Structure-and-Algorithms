# N nodes tree traverse
from typing import List
class TreeNode:
    def __init__(self, val: int, children: List):
        self.val = val
        self.children = children

def traverse(root: TreeNode):
    for child in root.children:
        traverse(child)

## Leetcode 341. Flatten Nested List Iterator

