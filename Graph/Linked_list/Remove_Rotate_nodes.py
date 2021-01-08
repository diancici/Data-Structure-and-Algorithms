## leetcode 19. Remove Nth Node From End of List

# Solution 1: Two pass
# O(n) in time, O(1) in space
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        # First pass : Find the length of list
        p = head
        length = 0
        while(p):
            p = p.next
            length += 1
        
        # Second Pass : Find the element to be deleted
        q = ListNode()
        ans = q
        q.next = head
        count = 0        
        while(count < length - n):
            q = q.next
            count += 1
        # remove the element
        q.next = q.next.next        
        
        return ans.next

# Solution 2: One pass using Two-pointer technique
# O(n) in time and O(1) in space#
class Solution:
    def removeNthFromEnd(self, head, n):
        ans = ListNode()
        ans.next = head
        
        slow = ans
        fast = ans
        
        # Move the fast pointer n nodes ahead
        for i in range(n+1):
            fast = fast.next
            
        while(fast):
            fast = fast.next
            slow = slow.next
            
        # Delete the slow.next
        slow.next = slow.next.next
        
        return ans.next


## Leetcode 203. Remove Linked List Elements
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        
        # create a pointer to save previous node
        prev = ListNode()
        prev.next = head
        ans = prev
        cur = head
        
        while(cur):
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        
        return ans.next


## Leetcode 61. Rotate list
# Given the head of a linked list, rorate the list to the right by k places
class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        # Find the point from which need to be added ahead
        cur = head
        length = 0
        while(cur):
            cur = cur.next 
            length += 1
        rotationTime = k%length

        # Two-pointer technique like the question : remove nth node from the end
        if k==0 or rotationTime == 0:
            return head
        
        slow = fast = head
        index = 0
        while(index < rotationTime):
            fast = fast.next
            index += 1
        if fast:
            while(fast.next):
                slow = slow.next
                fast = fast.next
            fast.next = head
            newhead = slow.next
            slow.next = None
            return newhead
