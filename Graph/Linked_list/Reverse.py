## Leetcode #206. Reverse Linked List
# Recusrion and Iteration
# Iteration
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while(cur is not None):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev

# Recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head is None or head.next is None):
            return head
        
        lastNode = self.reverseList(head.next) # return the new head of reversed linked list
        head.next.next = head
        head.next = None
        
        return lastNode

## Leedcode #92. Reverse Linked List II
#Reverse a linked list from position m to n. (Do it in one-pass)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # base case: reverse from head to n
        if m==1:
            return self.reverseN(head, n)
        
        # the most important part of this recursion: imaging that head is moving forward
        last = self.reverseBetween(head.next, m-1, n-1)
        
        head.next = last
        return head
    
    # Reverse the first n elements
    def reverseN(self, head, n):
        # base case
        if(n==1):
            self.successor = head.next # record trailing node
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        
        return last

## Leetcode #25. Reverse Nodes in k-Group
class Solution:
    def reverseKGroup(self, head:ListNode, k: int) -> ListNode:
        # base case
        a = head
        b = head
        for i in range(k):
            if b is None:
                return head            
            b = b.next
        
        # reverse the K elements [a,b)
        newHead = self.reverse(a, b)
        
        # recursion: reverse next Group starting from b+1
        a.next = self.reverseKGroup(b, k)
        
        return newHead
    
    def reverse(self, a, b):
        prev = None
        cur = a
        while(cur != b):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev

