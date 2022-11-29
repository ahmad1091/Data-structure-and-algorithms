# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [[0 for x in range(len(matrix))] for y in range(len(matrix))] 
    
        p = 0

        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix)):
                temp[j][i] = matrix[p][j]
            p +=1
                
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp[i][j]
        print(matrix)