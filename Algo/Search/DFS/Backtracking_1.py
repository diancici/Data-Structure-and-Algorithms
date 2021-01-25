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


# s = Solution()
# nums = [1,2,3]
# print(s.permute(nums))

## Leetcode 51. N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n] * n # inialize the board
        self.res = []
        self.backtrack(board, 0)
        return self.res
    
    # path/board: rows less than row have queens successfully
    # choices: All coloumns of this row can be put a queen.
    # end condition: row is over the len pg board
    def backtrack(self, board, row):
        # trigger end condition
        if row == len(board):
            self.res.append(board[:])
            return
        
        n = len(board[row])
        for col in range(n):
            # Rule out unreasonable choices
            if (self.isValid(board,row, col) == False):
                continue
            # make a choice
            board[row]= '.'*col+'Q'+'.'*(n-col-1)
            # move on to the next step
            self.backtrack(board, row+1)
            # Cancel selection
            board[row]= '.'*n
            
    def isValid(self, board, row, col):
        n = len(board)
        # check conflit in a column
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        # check conflit in upper right
        for i, j in zip(range(row-1, -1, -1), range(col+1,n)):        
            if board[i][j] == 'Q':
                return False
        # check conflit in upper left:
        for i, j in zip(range(row-1, -1, -1), range(col-1,-1,-1)):  
            if board[i][j] == 'Q':
                return False
        return True