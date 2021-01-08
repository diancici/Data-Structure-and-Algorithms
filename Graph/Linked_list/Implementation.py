## LeetCode 707. Design Linked List
# Single Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        count = 0
        temp = self.head        
        while(temp is not None):
            if count == index:
                return temp.val
            else:
                temp = temp.next
                count += 1                
        return -1
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        temp = self.head
        if temp is None:   # add at the begining if list is empty
            self.head = new_node
        else:    
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(val)
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if (index == 0):  # add at the begining
            node.next = self.head
            self.head = node
                   
        temp = self.head
        temp_pos = 0
        while (temp_pos < index-1 and temp.next is not None):
            temp = temp.next
            temp_pos += 1

        node.next = temp.next
        temp.next = node  
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """        
        if (index == 0): # delete at the begining
            self.head = self.head.next            
        else:   
            temp = self.head
            temp_pos = 0
            while (temp_pos < index-1):
                temp = temp.next
                temp_pos += 1
            if (temp is not None and temp.next is not None):
                temp.next = temp.next.next

# Double Linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        count = 0
        temp = self.head
        while(temp is not None):
            if count == index:
                return temp.val
            else:
                temp = temp.next
                count += 1
                
        return -1
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if (self.head is None): # if the list is empty
            self.head = node
        else:   
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        temp = self.head
        if temp is None: # add at the begining is the list is empty
            self.head = new_node
        else:    
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if (index == 0): # add at the begining
            node.next = self.head
            self.head = node
       
        else:   
            temp = self.head
            temp_pos = 0
            while (temp_pos < index-1 and temp.next is not None):
                temp = temp.next
                temp_pos += 1

            nextNode = temp.next
            if nextNode:
                node.next = nextNode
                node.prev = temp
                temp.next = node 
                nextNode.prev = node
            else:                   # add at the end 
                temp.next = node
                node.prev = temp
                
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if (index == 0): # delete at the begining
            self.head = self.head.next            
        else:   
            temp = self.head
            temp_pos = 0

            while (temp_pos < index-1):
                temp = temp.next
                temp_pos += 1

            if (temp is not None and temp.next is not None):
                nextNode = temp.next.next
                temp.next = nextNode
                if nextNode:
                    nextNode.prev = temp