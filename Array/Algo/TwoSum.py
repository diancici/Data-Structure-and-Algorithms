from typing import List
from collections import defaultdict
## 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(nums)):
            m[nums[i]] = i
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in m.keys() and m[complement] != j:
                return [j, m[complement]]
        return []


## Add a number in the set , find target value
class Solution:
    def __init__(self):
        self.sums = set()
        self.nums = []

    def add(self, number):
        for num in self.nums:
            self.sums.add(num+number)
        self.nums.append(number)

    def find(self, value):
        if value in self.sums:
            return True
        else:
            return False
            
## 2Sum: avoid repetive set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        res = []
        while (lo < hi):
            Sum = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            if Sum < target:
                while (lo < hi and nums[lo] == left): 
                    lo += 1
            elif Sum > target:
                while (lo < hi and nums[hi] == right):
                    hi -= 1
            elif Sum == target:
                res.append([left, right])
                while (lo < hi and nums[lo] == left):
                    lo += 1
                while (lo < hi and nums[hi] == right):
                    hi -= 1
        
        return res


## 15. 3Sum
class Solution:
    def twoSum(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        res = []
        while (lo < hi):
            Sum = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            if Sum < target:
                while (lo < hi and nums[lo] == left): 
                    lo += 1
            elif Sum > target:
                while (lo < hi and nums[hi] == right):
                    hi -= 1
            elif Sum == target:
                res.append([left, right])
                while (lo < hi and nums[lo] == left):
                    lo += 1
                while (lo < hi and nums[hi] == right):
                    hi -= 1       
        return res

    def threeSum(self, nums: List[int], start, target) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        tuples = []
        res = []
        i = start

        while (i < n):         
            tuples = self.twoSum(nums, i+1, target-nums[i])        
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)                       
            while (i < n - 1 and nums[i] == nums[i+1]):
                i += 1
            i += 1 
                    
        return res


## 18. 4Sum 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        tuples = []
        res = []
        i = 0

        while (i < n):         
            tuples = self.threeSum(nums, i+1, target-nums[i])        
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)                       
            while (i < n - 1 and nums[i] == nums[i+1]):
                i += 1
            i += 1 
                    
        return res
    
    def threeSum(self, nums, start, target):
        n = len(nums)
        tuples = []
        res = []
        i = start

        while (i < n):         
            tuples = self.twoSum(nums, i+1, target-nums[i])        
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)                        
            while (i < n - 1 and nums[i] == nums[i+1]):
                i += 1
            i += 1 
                    
        return res
    
    def twoSum(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        res = []
        while (lo < hi):
            Sum = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            if Sum < target:
                while (lo < hi and nums[lo] == left): 
                    lo += 1
            elif Sum > target:
                while (lo < hi and nums[hi] == right):
                    hi -= 1
            elif Sum == target:
                res.append([left, right])
                while (lo < hi and nums[lo] == left):
                    lo += 1
                while (lo < hi and nums[hi] == right):
                    hi -= 1       
        return res

    
## NSum
## nums.sort() before call nSum

def nSum(nums, n, start, target):
    size = len(nums)
    tuples = []
    res = []

    if (n < 2 or size < n):
        return res
    # base case
    if (n == 2):
        lo = start
        hi = size - 1
        res = []
        while (lo < hi):
            Sum = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            if Sum < target:
                while (lo < hi and nums[lo] == left): 
                    lo += 1
            elif Sum > target:
                while (lo < hi and nums[hi] == right):
                    hi -= 1
            elif Sum == target:
                res.append([left, right])
                while (lo < hi and nums[lo] == left):
                    lo += 1
                while (lo < hi and nums[hi] == right):
                    hi -= 1       

    else:
        i = start
        while (i < size):         
            tuples = nSum(nums, n-1, i+1, target-nums[i])        
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)                       
            while (i < size - 1 and nums[i] == nums[i+1]):
                i += 1
            i += 1 
                
    return res

nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()
print(nSum(nums, 4, 0, 0))







