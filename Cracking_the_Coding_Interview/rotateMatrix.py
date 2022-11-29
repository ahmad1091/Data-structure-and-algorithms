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
