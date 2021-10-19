from typing import List
from collections import defaultdict
## 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)
        
        for ch in t:
            need[ch] += 1
            
        left = 0;
        right = 0;
        valid = 0;
        start = 0;
        length = float('inf')

        while (right < len(s)): # Move forward the right pointer if not valid 
            # c is the character which will move into the window
            c = s[right]
            # window shift right
            right += 1
            # update window
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
                    print("valid: ", valid)
            
            print("left: , right: ",left, right)

            # Move forward the left pointer if valid (to shrink the window)
            while (valid == len(need.keys())):
                # update the minimum window
                if (right - left < length):
                    start = left
                    length = right - left
                
                # d is the character which will be moved out
                d = s[left]
                left += 1 
                # Update data in the window
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                        
        if length == float('inf'):
            return ""
        else:
            return s[start:start+length]


## 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        window = defaultdict(int)
        for c in s1:
            need[c] += 1
        
        left = 0
        right = 0
        valid = 0

        while(right < len(s2)):
            c = s2[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while (right-left >= len(s1)):
                if valid == len(need.keys()):
                    return True
                d = s2[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False


## 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = defaultdict(int)
        window = defaultdict(int)
        for c in p:
            need[c] += 1
        
        left = 0
        right = 0
        valid = 0
        index = []
        
        while(right < len(s)):
            c = s[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            print(left, right, valid, index)

            while(right-left >= len(p)):
                if valid == len(need.keys()):
                    index.append(left)
                d = s[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return index


## 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = 0
        right = 0
        res = 0

        while(right < len(s)):
            c = s[right]
            right += 1
            window[c] += 1

            while(window[c] > 1):
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)

        return res


