from typing import List
## Binary search
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = left + (right-left)//2
        if(nums[mid] == target):
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


## Sum of two numbers in a sorted array
# 167. Two Sum II - Input array is sorted
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while (left < right):
        Sum = numbers[left] + numbers[right]
        if Sum == target:
            return [left+1, right+1]
        elif Sum < target:
            left += 1
        elif Sum > target:
            right -= 1
    
    return [-1, -1]


## Reverse array
def reverse(nums: List[int]):
    left = 0
    right = len(nums)-1
    
    while(left < right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
        

        
