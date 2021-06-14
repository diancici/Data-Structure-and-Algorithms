## leetcode 234. Palindrome Linked List

# Solution 1: O(n) time and O(n) space
# Way1: Create a new list which is the reversed old one and compare
# Way2: Post-order traversal using the recursion stack to save the node

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        
        self.left = head
        return self.traverse(head)
        
    def traverse(self, right):
        # basic case
        if right==None: 
            return True
        # recursion
        res = self.traverse(right.next)
        res = res and right.val == self.left.val
        self.left = self.left.next
        return res

# Solution 2: Optimize, O(n) time and O(1) space 
# 1. Find the midpoint using two-pointer technique 
# 2. Reverse the right half to save space 
# 3. Compare the left half with right half

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        
        # Find the mid point using two-pointer technique
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next
        # Move the slow pointer to the right part if length of list is odd
        if(fast is not None):
            slow = slow.next
            
        # reverse the right part of the linked list, from slow to the end
        right = self.reverse(slow)
        left = head
        
        # compare the left part and the reversed right part 
        while(right):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
            
        return True
    
    # reverse linked list
    def reverse(self, head):
        if head.next is None:
            return head
        prev = None
        cur = head
        while(cur):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev




