## Backtracking 
# result = []
# path = []  
# choices = deque()
# def backtrack(path, choice):
#    if satisfy the end condition:
#       result.add(path)
#    
#    for choice in choices:
#        # make a choice
#        choices.remove(choice)   
#        path.append(choice)
#        self.backtrack(path, choice)
#        # remove the choice from path, add the choice deleted to the choices
#        path.remove(path)
#        choices.add(choice)

## Leetcode 46. Permutations
from typing import List
class Solution:
    def permute(self, nums: List[int]):
        self.res = []
        #visited = set()
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, nums, path):
        if len(path) == len(nums):
            self.res.append(path[:])
            print("res :", self.res)
            return 
    
        
        for num in nums:
            # make a choice
            if num not in path:
                path.append(num)
                print("path after append: ", path)        
                # recursion, move to the next step
                self.backtrack(nums, path)
                # delete the choice from path (back to last step)
                path.pop()
                print("path after pop: ", path)  

s = Solution()
nums = [1,2,3]
print(s.permute(nums))
