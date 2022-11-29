# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def nullifyRow(self,matrix,row):
        for i in range(len(matrix[0])):
            matrix[row][i] = 0

    def nullifyCol(self,matrix,col):
        for i in range(len(matrix)):
             matrix[i][col] = 0
                
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False] * len(matrix)
        col = [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True


        for i in range(len(matrix)):
            if(row[i]):
                self.nullifyRow(matrix, i)

        for j in range(len(matrix[0])):
            if(col[j]):
                self.nullifyCol(matrix, j)
