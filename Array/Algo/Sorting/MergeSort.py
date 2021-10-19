# merging: combining two ordered arrays to make one larger ordereed array
# recursive sort method, divide & conquer
# T(O) = O(nlogn)
# S(O) = O(n)

from typing import List
def merge(arr: List):
    if(len(arr)<=1):
        return arr
    
    # Split array into right and left
    n = len(arr)
    m = n//2
    left = arr[0:m]
    # print("left array is : ", left)
    right = arr[m:]
    # print("right array is : ", right)
    # Top-down
    merge(left)
    merge(right) 
    return mergeSort(left, right)

def mergeSort(left: List, right: List):
    result = [] # extra space to put the compared value
    leftIndex = 0
    rightIndex = 0
    
    while(leftIndex < len(left) and rightIndex < len(right)):
        if(left[leftIndex] <= right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    
    if leftIndex < len(left):
        result.extend(left[leftIndex:])    
    if rightIndex < len(right):
        result.extend(right[rightIndex:])    
    
    return result
