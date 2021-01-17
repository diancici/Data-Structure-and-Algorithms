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
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, choices, visited):
        if len(visited) == len(choices):
            self.res.append(visited[:])
            return 
    
        
        for choice in choices:
            # make a choice
            if choice not in visited:
                visited.append(choice)       
                # recursion, move to the next step
                self.backtrack(choices, visited)
                # delete the choice from path (back to last step)
                visited.pop()


s = Solution()
nums = [1,2,3]
print(s.permute(nums))

## Leetcode 51. N-Queens
