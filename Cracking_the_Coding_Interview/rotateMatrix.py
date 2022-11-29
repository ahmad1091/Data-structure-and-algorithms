# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

def rotate(matrix):
    temp = [[0 for x in range(len(matrix))] for y in range(len(matrix))] 
    
    p = 0

    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix)):
            temp[j][i] = matrix[p][j]
        p +=1
                
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp[i][j]


# Solution 2.
def rotate(matrix):
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
    print(matrix)
    return True

rotate([[1,2,3],[4,5,6],[7,8,9]])