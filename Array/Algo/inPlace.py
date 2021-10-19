from typing import List
## Fast & Slow pointer
## 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        
        while (fast < len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow+1


## 27. Remove element 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while(fast < len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


## 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while(fast<len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        for i in range(slow, len(nums)):
            nums[i] = 0


## Set, Dict
# 316. Remove Duplicate Letters
from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        for ch in s:
            count[ch] -= 1
            if ch in seen:
                continue
            while(stack and stack[-1] > ch ):
                if count[stack[-1]] == 0:
                    break
                removed_char = stack.pop()
                seen.remove(removed_char)
            stack.append(ch)
            seen.add(ch)
            #print(stack)
        
        return ''.join(stack)

S = Solution()
s = "bcac"
print(S.removeDuplicateLetters(s))
