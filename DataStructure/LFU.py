from collections import defaultdict, deque

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.keyToVal = dict() # {key: val, ...}  # To realise quick find: Hash Map
        self.keyToFreq = dict() #{key: Freq, ...} 
        self.freqToKeys = defaultdict() #{freq: deque, ...} # To realise quick insert, delete and in order: deque
        
    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        # increase the corresponding freq of the key
        self.increaseFreq(key)
        return self.keyToVal.get(key)        

    def put(self, key: int, val: int) -> None:
        if self.cap <= 0: return
        # if key exists, modify the val, increase the freq
        if key in self.keyToVal:
            self.keyToVal[key] = val
            self.increaseFreq(key)
            return
        # if key not exists, insert new key-val pair
        # if the cache is full, del the least frequently used
        if self.cap <= len(self.keyToVal):
            self.removeMinFreqKey()
        # if not full, insert the key-val pair & freq + 1
        self.keyToVal.update({key: val})
        self.keyToFreq.update({key: 1})
        if 1 not in self.freqToKeys:
            self.freqToKeys[1] = deque()
        self.freqToKeys[1].append(key)
        # update the minimum freq
        self.minFreq = 1
        
    def removeMinFreqKey(self):
        # least frequently used list
        keyList = self.freqToKeys.get(self.minFreq)
        # the leftmost key is the first key inserted, should be deleted firstly
        # from the keyList
        deletedKey = keyList.popleft()
        # if the deque is empty, remove the minFreq from the dict
        if len(keyList) == 0:
            self.freqToKeys.pop(self.minFreq)            
        # update keyToVal & KeyToFreq
        self.keyToVal.pop(deletedKey)
        self.keyToFreq.pop(deletedKey)
        
    def increaseFreq(self, key):
        freq = self.keyToFreq.get(key)
        # update the dict keyToFreq
        self.keyToFreq[key] = freq + 1
        # update the dict FreqToKeys
        # remove the key from deque of Freq
        self.freqToKeys.get(freq).remove(key)
        # add the key to the deque of freq + 1
        if freq+1 not in self.freqToKeys:
            self.freqToKeys[freq+1] = deque()
        self.freqToKeys.get(freq+1).append(key)
        # if the deque of freq is empty, delete
        if len(self.freqToKeys.get(freq)) == 0:
            self.freqToKeys.pop(freq)
            if freq == self.minFreq:
                self.minFreq += 1
        

# Your LRUCache object will be instantiated and called as such:
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))