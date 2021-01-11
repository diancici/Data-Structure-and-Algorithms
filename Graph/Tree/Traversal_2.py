## Leetcode 654. Maximum Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums)-1)


    def build(self, nums, l, h):
        # base case:
        if l > h:
            return None

        # pre-order, build the root
        index = 0
        maxVal = -float("inf")
        for i in range(l,h+1):
            if maxVal < nums[i]:
                maxVal = nums[i]
                index = i
                break

        root = TreeNode(maxVal)
        root.left = self.build(nums, l, index-1)
        root.right = self.build(nums, index+1, h)

        return root


## Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder)-1,
                            inorder, 0, len(inorder)-1)

    def build(self, preorder, preStart, preEnd,
                    inorder, inStart, inEnd):
        # basic case:
        if preStart > preEnd:
            return None
        # build root
        rootVal = preorder[preStart]
        index = 0
        for i in range(inStart, inEnd):
            if inorder[i] == rootVal:
                index = i
                break

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart+1, preStart+leftSize,
                                inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd,
                                inorder, index+1, inEnd)
        return root



## Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder)-1,
                        postorder, 0, len(postorder)-1)
        
        
    def build(self, inorder, inStart, inEnd,
                    postorder, postStart, postEnd):
        # basic case:
        if postStart > postEnd:
            return None
        # build the root
        rootVal = postorder[postEnd]
        root = TreeNode(rootVal)
        
        # Find the index of root in inorder
        index = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break
                
        # Find the size of left tree
        sizeLeft = index - inStart
            
        root.left = self.build(inorder, inStart, index-1,
                            postorder, postStart, postStart+sizeLeft-1)
        root.right = self.build(inorder, index+1, inEnd,
                            postorder, postStart+sizeLeft, postEnd-1)
        return root
        