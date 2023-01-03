# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDia = set() # (r + c)
        negDia = set() # (r - c)
        res = []
        board = [['.']  * n for _ in range(n)]
        
        def backTrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if (c in col) or (r + c in posDia) or (r - c in negDia):
                    continue
                    
                col.add(c) 
                posDia.add(r + c)
                negDia.add(r - c)
                board[r][c] = 'Q'

                backTrack( r + 1)
                
                col.remove(c) 
                posDia.remove(r + c)
                negDia.remove(r - c)
                board[r][c] = '.'

        backTrack(0)
        return res