# complete binary tree -> binary heap -> priority queue
# T(O) = O(nlogn)
# S(O) = O(n)
from typing import List   

def heapSort(arr: List):
    heap_size = len(arr)
    build_heap(arr)
    print("the max_heap built of the arr: ", arr)
    
    for i in range(heap_size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        sink(arr, heap_size, 0)
        
    return arr

def sink(arr: List, heap_size: int, i: int):
    # a complete binary tree
    left = 2*i+1 # node child left
    right = 2*i+2 # node child right
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sink(arr, heap_size, largest)

def build_heap(arr):
    heap_size = len(arr)
    for i in range((heap_size//2), -1, -1): # Sort from the leaf node for max_heap
        sink(arr, heap_size, i)

arr = [3, 20, 1, 5, 2, 200, 100, 98, 250]
heapSort(arr)
print(arr)