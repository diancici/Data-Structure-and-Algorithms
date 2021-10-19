from typing import List
from implementation import UF

## Leetcode 130.Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # create an instance of class UF and add a virtual point mark
        # all of 'o' connected to 'mark' will not be captured
        uf = UF(m*n+1)
        mark = m*n
        
        # connnect 'o' of the first and last colomn to 'mark'
        for i in range(0, m):
            if board[i][0] == 'O':
                uf.union(i*n, mark)
            if board[i][n-1] == 'O':
                uf.union(i*n + n - 1, mark)
        
        # connect 'o' of the first and last rows to 'mark'
        for i in range(0, n):
            if board[0][i] == 'O':
                uf.union(i, mark)
            if board[m-1][i] == 'O':
                uf.union(n * (m - 1) + i, mark)
        
        # connect adjacent 'o' not on the border
        # create an array which represents four directions
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for k in range(0, 4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)
                            
        # determine if 'o' is connected to 'mark', if not replace with 'x'
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.connected(i*n+j, mark):
                    board[i][j] = 'X'

# s = Solution()
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# s.solve(board)
# print(board)

## Leetcode
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        # check "==" first to connect 
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - 97
                y = ord(eq[3]) - 97
                uf.union(x, y)
        # then check "!=", if two number are already connected, then false     
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - 97
                y = ord(eq[3]) - 97
                if uf.connected(x, y):
                    return False
        return True

s = Solution()
equations = ["a==b","e==c","b==c","a!=e"]
print(s.equationsPossible(equations))