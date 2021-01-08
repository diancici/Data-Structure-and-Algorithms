## Leetcode 2. Add Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        curNode = ListNode
        count = 0
        # save the head node of the result
        newHead = curNode
        
        while(l1 or l2):
            Sum = 0
            if(l1):
                Sum += l1.val
                l1 = l1.next
            if(l2):
                Sum += l2.val
                l2 = l2.next
            
            Sum += count
            
            # Create the next Node
            curNode.next = ListNode(Sum%10)
            curNode = curNode.next
            
            # Update the count
            count = Sum//10
            
        if(count):
            curNode.next = ListNode(count)   
        
        return newHead.next


