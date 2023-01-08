# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDia = set()
        posDia = set()
        res = []
        board = [['.'] * n for _ in range(n)]

        def BT(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in cols or (r + c) in posDia or (r - c) in negDia:
                    continue
                
                cols.add(c)
                posDia.add(r + c)
                negDia.add(r - c)
                board[r][c] = 'Q'

                BT(r + 1)

                cols.remove(c)
                posDia.remove(r + c)
                negDia.remove(r- c)
                board[r][c] = '.'
        BT(0)
        return res