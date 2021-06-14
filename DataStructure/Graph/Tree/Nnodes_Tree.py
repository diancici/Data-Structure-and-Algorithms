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
class NestedIterator:
    def __init__(self, nestedList: List):
        self.stack = nestedList[::-1]

    def next(self)->int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while(self.stack):
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


