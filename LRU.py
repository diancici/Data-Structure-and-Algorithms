## 146. LRU Cache
class LRUCache:    
    def __init__(self, capacity: int):
        self.capa = capacity
        # {key: Node(key, val), ...}
        self.map = dict()
        # Head <-> Node(k1, v1) <-> Node(k2, v2)...<-> Tail
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # Update the key as the most recently used key
        self.makeRecently(key) 
        return self.map.get(key).val
   
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Update the value of the key and add it as most recently
            self.deleteKey(key)
            self.addRecently(key, value)
            return
        
        if self.cache.length() == self.capa:
            # Remove the least recently used key
            self.removeLeastRecently()
        # Add the new pair
        self.addRecently(key, value)

    ## Encapsualtion of HashMapDoubleLinked operations         
    # Add a new key-value pair in the cache
    def addRecently(self, key: int, val: int):
        x = Node(key, val)
        self.cache.addLast(x)
        self.map.update({key: x})
    
    # Delete a key-value pair in the cache
    def deleteKey(self, key: int):
        x = self.map.get(key)      
        self.cache.remove(x)
        self.map.pop(key)
        
    # Update the most recently used key
    def makeRecently(self, key: int):
        x = self.map.get(key)
        self.cache.remove(x)
        self.cache.addLast(x)
    
    # Remove the least recently used key
    def removeLeastRecently(self):
        deleteNode = self.cache.removeFirst()
        deleteKey = deleteNode.key
        self.map.pop(deleteKey)
    

# create a Node class
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# create a Double linked list class with help of Node
class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def addLast(self, x: Node) -> Node:
        x.prev = self.tail.prev
        self.tail.prev.next = x
        x.next = self.tail
        self.tail.prev = x
        self.size += 1
        return x
        
    
    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
    
    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first
        
    def length(self):
        return self.size

        


# Your LRUCache object will be instantiated and called as such:
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
