## leetcode 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:
        # create a new linked list as a result
        cur = ListNode()
        ans = cur

        while(l1 and l2):
            if(l1.val < l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return ans.next


## Leetcode 23. Merge k Sorted Lists
# Solution 1: Brute force, O(NlogN) in time, O(n) in space
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        self.nodes = []
        
        # Iterate over lists of nodes and append the value into a new list
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        # Sort the new list of nodes and create a node for every node
        cur = ListNode()
        ans = cur
        for x in sorted(self.nodes):
            cur.next = ListNode(x)
            cur = cur.next

        return ans.next

# Solution 2 : using priorityQueue
# O(Nlogk) in time
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        q = PriorityQueue()
        cur = ListNode()
        ans = cur

        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
            val, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, node))

        return ans.next

# Solution 3 : transform to merge 2 lists at one time:
class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        j = len(lists) - 1
        while(j > 0):
            i = 0
            while(j>i):
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        cur = ListNode()
        ans = cur
        while(l1 and l2):
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return ans.next


# Leetcode 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while(odd.next and even.next):
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        odd.next = even_head
        
        return head

