from typing import List
## Leetcode 297. Serialize and Deserialize Binary Tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## Pre-order traverse
from collections import deque
class Codec:
    def serialize(self, root):
        # create a list to save the node value
        self.li = []
        self.serializeBuilder(root)
        # convert list to string
        string = ','.join([str(ele) for ele in self.li])
        return string

    def serializeBuilder(self, root):
        if not root:
            self.li.append("#")
            return
        self.li.append(root.val)
        self.serializeBuilder(root.left)
        self.serializeBuilder(root.right)

    def deserialize(self, data):
        # convert string to list
        data_list = data.split(",")
        # create a linked list to save the node decodes for popleft operation
        self.de = deque() 
        for ele in data_list:
            self.de.append(ele)
        return self.deserializeBuilder(self.de)

    def deserializeBuilder(self, de):
        if not de: return None
        # popleft the root
        first = de.popleft()
        if first == "#": return None
        root = TreeNode(int(first))
        root.left = self.deserializeBuilder(de)
        root.right = self.deserializeBuilder(de)

        return root


## Post-order traverse:
class Codec:
    def serialize(self, root):
        # create a list to save the node value
        self.li = []
        self.serializeBuilder(root)
        # convert list to string
        string = ','.join([str(ele) for ele in self.li])
        return string

    def serializeBuilder(self, root):
        if not root:
            self.li.append("#")
            return
        self.serializeBuilder(root.left)
        self.serializeBuilder(root.right)
        self.li.append(root.val)

    def deserialize(self, data):
        # convert string to list
        data_list = data.split(",")
        # create a linked list to save the node decodes for popleft operation
        self.de = deque() 
        for ele in data_list:
            self.de.append(ele)
        return self.deserializeBuilder(self.de)

    def deserializeBuilder(self, de):
        if not de: return None
        # popleft the root
        first = de.pop()
        if first == "#": return None
        root = TreeNode(int(first))
        root.right = self.deserializeBuilder(de)
        root.left = self.deserializeBuilder(de)
        

        return root


## Level Traversal (queue: save the parent node)
class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        # l : save the node value
        l = []
        # queue: save the parent node, like a linked list
        q = deque()
        q.append(root)

        while(q):
            cur = q.popleft()
            if cur is None:
                l.append("#")
                continue

            l.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        # convert list to string
        return ','.join([str(ele) for ele in l])

    def deserialization(self, data):
        if not data: return None
        # list: save nodes values
        nodes = data.split(',')
        # queue: save parent node for popleft
        q = deque()
        root = TreeNode(nodes[0])
        q.append(root)

        for i in range(1, len(nodes), 2):
            if q:
                parent = q.popleft()

                # left tree
                left = nodes[i]
                if left != '#':
                    parent.left = TreeNode(int(left))
                    q.append(parent.left)
                else:
                    parent.left = None

                # right tree
                right = nodes[i+1]
                if right != '#':
                    parent.right = TreeNode(int(right))
                    q.append(parent.right)
                else:
                    parent.right = None

        return root


##  Leetcode 108. Convert Sorted Array to Binary Search Tree
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
        
