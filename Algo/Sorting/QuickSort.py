# divide -and-conquer method, complementary to mergesort
# works by partitioning
# T(O) = O(nlogn), worst case  O(n^2)
# S(O) = O(logn)
from typing import List

def quickSort(arr: List, left: int, right: int):
    if (left < right):
        pivot = right
        partitionIndex = partition(arr, pivot, left, right)        
        # sort left and right
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
        
    return arr

def partition(arr, pivot, left, right):
    partitionIndex = left    
    for i in range(left, right):
        if arr[i] < arr[pivot]:
            swap(arr, i, partitionIndex)
            partitionIndex += 1    
    swap(arr, right, partitionIndex)
    return partitionIndex

def swap(arr: List, firstIndex: int, secondIndex: int):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp

arr = [99, 44, 6, 2, 1, 5, 63, 291, 283, 4, 0]
quickSort(arr, 0, len(arr)-1)
print(arr)