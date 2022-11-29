# Given two n x n binary matrices mat and target,
# return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

class Solution:
    def rotate(self,matrix:List[List[int]])-> List[List[int]]:
        if (len(matrix) == 0 | len(matrix) != len(matrix[0])):
            return false
        n= len(matrix)
        for layer in range(int(n/2)):
            first = layer
            last = n - 1 - layer

            for i in range(first,last):
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last -offset]
                matrix[last][last -offset] = matrix[i][last]
                matrix[i][last] = top
        return matrix

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        for i in range(len(mat)+1):
            self.rotate(mat)
            if(mat == target):
                return True
            

        return False