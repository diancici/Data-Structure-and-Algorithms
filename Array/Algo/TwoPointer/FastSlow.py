## Leetcode 141. Linked List Cycle
# fast, slow technique
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False


## Leetcode 142. Linked List Cycle II
# Return the node where the cycle begins
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                slow = head
                while (slow != fast):
                    slow = slow.next
                    fast = fast.next
                return fast

        return None


## Leetcode 160. Intersection of two Linked Lists
class Solution:
    def getIntersectionNode(self, headA, headB):
        p = headA
        q = headB

        while (p != q):
            p = p.next if p else headB
            q = q.next if q else headA
            
        return p


## Find the penultimate kth element of the linked list
def findKthelement(head, k):
    slow = head
    fast = head

    while (k > 0):
        fast = fast.next
        k -= 1

    while(fast):
        fast = fast.next
        slow = slow.next

    return slow

    
    


