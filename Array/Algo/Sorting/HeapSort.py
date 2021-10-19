# complete binary tree -> binary heap -> priority queue
# T(O) = O(nlogn)
# S(O) = O(n)
from typing import List   

class heapSort():
    def heapSort(self, arr: List):
        heap_size = len(arr)
        self.build_heap(arr, heap_size)
        print("the max_heap built of the arr: ", arr)
        
        for i in range(heap_size-1, 0, -1):
            temp = arr[i]
            arr[i] = arr[0]
            arr[0] = temp
            heap_size -= 1
            self.sink(arr, heap_size, 0)
            print(i, heap_size, arr)
            
        return arr

    def sink(self, arr: List, n: int, k: int):
        # a complete binary tree
        while (2*k < n - 1):
            j = 2*k + 1 # node child left
            if j < n-1 and arr[j] < arr[j+1]:
                j += 1
            if arr[k] > arr[j]: break # heap is maintained
            arr[k], arr[j] = arr[j], arr[k] # exchange two nodes if child > parent
            k = j

    def build_heap(self, arr: List, heap_size: int):
        for i in range((heap_size//2), -1, -1): # Sort from the halfway back through the array
            self.sink(arr, heap_size, i)

arr = [3, 20, 4, 5, 2, 200, 100, 98, 250]
s = heapSort()
arr = s.heapSort(arr)
print(arr)