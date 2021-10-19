class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Leetcode 98 Validate Bnary Search Tree
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)
    
    def validate(self, root, minNode, maxNode):
        if root is None:
            return True
        # minNode < root < maxNode
        if minNode != None and root.val < minNode: return False
        if maxNode != None and root.val > maxNode: return False

        # for the left: maxNode = root
        # for the right: minNode = root
        return self.validate(root.left, minNode, root) and self.validate(root.right, root, maxNode)


## Leetcode 700. Search in a binary search tree
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)

## Leetcode 701. Insert into a binary search tree
class Solution:
    def inserIntoBST(self, root: TreeNode, val:int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        if root.val < val:
            root.right = self.inserIntoBST(root.right, val)
        else:
            root.left = self.inserIntoBST(root.left, val)
        return root

## Leetcode 450. Delete Node in a BST
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                # find the smallest node in the right
                minNode = self.getMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
                
        return root

    def getMin(self, node: TreeNode):
        while(node.left is not None):
            node = node.left
        return node

    