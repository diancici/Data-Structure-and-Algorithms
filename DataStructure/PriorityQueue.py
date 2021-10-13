## Data Structure: Complete heap-ordered binary tree
# insert(): T(n) = logN
# remove the maximum/minimum: T(n) = logN
# Basic operations: 
# Bottom-up reheapify : swim
# Top-down reheapify : sink
class maxPQ():
    def __init__(self):
        self.pq = [0] # create a complete binary tree with a[0] = 0
        self.n = 0 # size of the queue

    # Add new key at the end of the array, increment size, swim up
    def insert(self, v):
        self.pq.append(v)
        self.n += 1
        self.swim(self.n)

    # Remove the top(largest), put the item from the end at the top, decrement size, sink down
    def delMax(self):
        max = self.pq[1]
        self.exch(1, self.n)
        self.pq[self.n] = None
        self.n -= 1
        self.sink(1)
        return max

    # Return the maximum 
    def max(self):
        return self.pq[1]

    # print the priority queue
    def printPQ(self):
        print(self.pq)

    # if node at k > node at k/2 (parent), than change two nodes
    # move up the node until it's no longer larger than its parent
    def swim(self, k: int):
        while k > 1 and self.less(k//2, k):
            self.exch(k//2, k)
            k = k // 2

    # if node at k < node at 2k, than change two nodes
    # move down until it's no longer smaller than its children
    def sink(self, k: int):
        while 2*k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j+1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    # exchange two nodes at position i and j
    def exch(self, i: int, j: int):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    # compare two nodes at position i and j
    def less(self, i: int, j: int):
        return self.pq[i] < self.pq[j]


pq = maxPQ()
pq.insert(1)
pq.insert(4)
pq.insert(10)
pq.insert(5)
pq.insert(3)
pq.insert(6)
print(pq.max())
print(pq.printPQ())
