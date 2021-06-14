""" Find a number in a sorted array """
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


""" Find the left border """
def leftBorder(nums, target):
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = left + (right-left)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid - 1
    # check if left is overborder or right is overborder 
    if (left >= len(nums) or nums[left] != target):
        return -1
    return left


""" Find the right border """
def rightBorder(nums, target):
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = left + (right - left)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            left = mid + 1
    # check if right is overborder
    if(right < 0 or nums[right] != target):
        return -1
    return right