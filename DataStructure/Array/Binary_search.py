from typing import List

## Leetcode 875. Koko Eating Bananas
# T(n) = O(NlogN)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        
        while(left < right):
            mid = left + (right - left)//2
            if(self.canFinish(piles, mid, h)):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def canFinish(self, piles, speed, H):
        time = 0
        for pile in piles:
            time += self.eat(pile, speed)
        return time <= H
    
    def eat(self, pile, speed):
        if pile % speed > 0:
            return pile//speed + 1
        else:
            return pile/speed


## 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        
        while(left < right):
            mid = left + (right-left)//2
            if self.canFinish(weights, mid, days):
                right = mid
            else:
                left = mid + 1
            
        return left
    
    def canFinish(self, weights, cap, days):
        i = 0
        
        for day in range(days):
            maxCap = cap
            while ((maxCap - weights[i])) >= 0:
                maxCap -= weights[i]
                i += 1
                if i == len(weights):
                    return True
                
        return False


## 410. Split Array Largest Sum
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)+1
        
        while(left < right):
            mid = left + (right-left)//2
            n = self.split(nums, mid)
            if n == m:
                right = mid
            elif n < m:
                right = mid
            elif n > m:
                left = mid+1
        
        return left
    
    def split(self, nums, maxSum):
        n = 1
        s = 0
        
        for i in range(0, len(nums)):
            if s + nums[i] > maxSum:
                n += 1
                s = nums[i]
            else:
                s += nums[i]
        return n