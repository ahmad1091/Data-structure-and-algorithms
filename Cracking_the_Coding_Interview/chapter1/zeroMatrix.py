# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def nullifyRow(matrix,row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix,col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def setZeros(matrix):
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
            
    print(row)
    print(col)

    for i in range(len(matrix)):
        if(row[i]):
            nullifyRow(matrix, i)

    for j in range(len(matrix[0])):
        if(col[j]):
            nullifyCol(matrix, j)

    return matrix

print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))